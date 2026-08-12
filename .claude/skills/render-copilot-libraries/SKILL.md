---
name: render-copilot-libraries
description: Generate Copilot library renders (stage-1 JSON + stage-2 .bal.txt) into old/ or new/ for a set of Ballerina libraries at their pinned versions, from a given ballerina-vscode source checkout. Use when asked to "render", "regenerate", or "generate the renders" for libraries into the old or new side of this repo.
---

# Render Copilot libraries

Two-stage pipeline. There is no CLI — stage 1 must be driven from a TestNG test, because package
resolution needs the Ballerina distribution the test task wires up.

```
Java (language server)                          TypeScript (VS Code extension)
CopilotLibraryManager.loadFilteredLibraries  →  Library model
ModelToJsonConverter.libraryToJson           →  JSON  ──►  toSyntaxString([json])  →  .bal.txt
```

## Parameters

| Parameter | Required | Notes |
|---|---|---|
| `--side` | **yes** | `old` or `new` — which subdirectory to write into |
| `--source` | **yes** | Path to a `ballerina-vscode` checkout, or a git URL. The render represents *this* source's behaviour |
| `--libs` | no | Space-separated `org/name` subset. Default: **all** libraries in the `CLAUDE.md` table |
| `--root` | no | Repo root holding `CLAUDE.md` and the library directories. Default: this skill's repo |
| `--scratch` | no | Work directory. Default: `$TMPDIR/copilot-render-<side>` |
| `--donor-home` | no | A previous run's `build/ballerina_dependencies/home`, to copy balas instead of re-downloading |
| `--skip-seed` | no | Skip seeding (only when the home is already known-good) |

Typical invocation:

```
/render-copilot-libraries --side new --source /path/to/ballerina-vscode
/render-copilot-libraries --side old --source https://github.com/ballerina-platform/ballerina-vscode \
                          --libs "ballerina/http ballerinax/kafka"
```

**`--source` is never guessed** (`CLAUDE.md` rule 4). If the user didn't give one, ask. If they gave
two, confirm which maps to `old` and which to `new`. If they gave one, confirm which side it is.
Record the resulting commit — it is the provenance of the render.

**Versions are never invented** (rule 7). They come only from the `CLAUDE.md` table; a requested
library absent from that table is a hard error, not a guess.

## Quick path

`scripts/run.sh` executes the whole pipeline with the parameters above and stops at the first failed
gate:

```bash
.claude/skills/render-copilot-libraries/scripts/run.sh \
    --side new --source /path/to/ballerina-vscode [--libs "org/a org/b"] [--donor-home <dir>]
```

Run the steps below manually when a run needs babysitting (a long Gradle build, a partial re-run, or
diagnosing a gate failure).

## Procedure

### 1. Build the pinned list

```bash
python3 .claude/skills/render-copilot-libraries/scripts/parse_libs.py \
    --root <repo-root> --out <scratch>/pinned.txt [--only org/name ...]
```

Writes `org/name:version` lines straight from the `CLAUDE.md` table. It fails loudly on a requested
library that is absent from the table rather than guessing a version.

### 2. Copy the source into scratch (never build in the user's checkout)

```bash
.claude/skills/render-copilot-libraries/scripts/prepare_source.sh <src-or-url> <scratch>/src
```

Copies (or clones) and then **restores tracked files that the `build/` exclude wrongly deleted** —
see gotcha 5. Record the resulting `git rev-parse HEAD`; it is the provenance of the render.

### 3. Install the probe

```bash
python3 .claude/skills/render-copilot-libraries/scripts/gen_probe.py \
    --src <scratch>/src --scratch <scratch> --side <side>
```

It detects whether this source has the version-aware overload
`loadFilteredLibraries(String[], Map<String,String>)`:

- **present** (spec-v2 branches) → resolves by **exact version**. Strongest guarantee.
- **absent** (`main`) → falls back to the version-less call, which makes step 5's cache pinning the
  only thing binding the version.

It also registers the class in `testng.xml` (mandatory — see gotcha 2).

### 4. Provision the build-owned Ballerina home

```bash
cd <scratch>/src/packages/ballerina-language-server && ./gradlew resolveBallerinaDependencies
```

Do this **before** step 5. It can `delete` the home directory, wiping pinned packages pulled earlier.

### 5. Put every pinned version into that home — the step that actually pins

```bash
.claude/skills/render-copilot-libraries/scripts/seed_home.sh <scratch>/src <scratch>/pinned.txt [<donor-home>]
```

Pass a `<donor-home>` (a previous run's `build/ballerina_dependencies/home`) to copy balas instead of
re-downloading — this is much faster and the cache is path-independent.

Then **gate on the audit**:

```bash
python3 .claude/skills/render-copilot-libraries/scripts/audit_home.py --src <scratch>/src --pinned <scratch>/pinned.txt
```

Do not continue until it reports every pin present. When the source lacks the version-aware overload,
each pin must also be the **highest** version in that home; the script flags it if not, and the fix is
to delete the newer version directory from the home.

### 6. Run stage 1

```bash
cd <scratch>/src/packages/ballerina-language-server
./gradlew :flow-model-generator:flow-model-generator-ls-extension:test --rerun-tasks \
  --tests "io.ballerina.flowmodelgenerator.extension.CatalogProbeTest"
```

Produces `<scratch>/json-out-<side>/` and `<scratch>/resolved-versions-<side>.txt`.

**Gate: every row must read `PIN_OK`.** A `PIN_MISMATCH` with a resolved version means that library
rendered at the *wrong* version and looks perfectly valid — never ship it. Report `UNRESOLVED` and
`ERROR` rows by name.

### 7. Render (stage 2)

Needs `ts-node` + **TypeScript 5** (see gotcha 4):

```bash
mkdir -p <scratch>/tsrun && cd <scratch>/tsrun && npm init -y
npm install ts-node typescript@5.6.3 @types/node

./node_modules/.bin/ts-node \
  --compiler-options '{"module":"commonjs","esModuleInterop":true,"skipLibCheck":true,"target":"es2020"}' \
  <scratch>/render.ts <scratch>/src <scratch>/json-out-<side> <repo-root> <side> <scratch>/render-report-<side>.txt
```

Copy `scripts/render.ts` to `<scratch>/render.ts` first. It writes both the JSON and the `.bal.txt`
into `<repo-root>/<name>/<side>/`.

### 8. Verify

```bash
python3 .claude/skills/render-copilot-libraries/scripts/verify_output.py \
    --root <repo-root> --pinned <scratch>/pinned.txt --side <side>
```

Checks every JSON parses and its top-level `name` matches, every render carries the matching
`// Library: <org>/<name>` header, nothing is empty or missing, and the *other* side is untouched.

### 9. Clean up and report

Delete the probe class and revert `testng.xml`, then confirm:

```bash
git -C <scratch>/src status --short   # expect no probe, no testng.xml change
```

Report: source commit, counts, the pinned-vs-resolved outcome, and every failure **by name**. Do not
summarize failures away.

## Gotchas that will cost hours

1. **The tests do not use `~/.ballerina`.** `build.gradle` points every test JVM at
   `build/ballerina_dependencies/home` via `BALLERINA_HOME_DIR` and sets `-Dls.test.offline=true`,
   which puts `PackageUtil` in `FORCE_OFFLINE`: it never contacts Central, treats "latest" as the
   highest version *in that home*, and returns empty for anything uncached. Pulling into
   `~/.ballerina` accomplishes nothing. This is the single most expensive mistake.

2. **`testng.xml` registration is mandatory.** `build.gradle` uses
   `useTestNG { suites "src/test/resources/testng.xml" }`, so `--tests` alone fails with
   "No tests found for given includes".

3. **`toSyntaxString` takes `Library[]`,** not a single library. Wrap it: `toSyntaxString([json])`.

4. **TypeScript 7 breaks `ts-node`** (`Cannot read properties of undefined (reading 'fileExists')` —
   the native port drops `ts.sys`). Pin `typescript@5.x`.

5. **macOS rsync is 2.6.9.** No `--info=progress2`. And excluding `build/` deletes tracked files that
   legitimately live in a `build` directory (checkstyle config, `.github/actions/build/action.yml`);
   `prepare_source.sh` restores them with `git checkout` and verifies `git ls-files -d` is empty.

6. **Gradle `-Dfoo=bar` does not reach the forked test JVM.** Paths in the probe must be hardcoded —
   `gen_probe.py` substitutes them into the template.

7. **`bal pull` exit code lies.** It returns non-zero when a *successfully downloaded* package fails
   to compile (e.g. `ballerinax/copybook` has real type errors). Check for the version directory on
   disk, not the exit code. Transient `package not found` also happens — retry once before believing it.

8. **`--rerun-tasks` is safe for the home.** `resolveBallerinaDependencies` skips its `delete` when
   the `Dependencies.toml` hash is unchanged and the home exists. Don't edit that file.

## Known upstream behaviors, not pipeline bugs

- **`main` crashes rendering `ballerina/mcp`** — `renderFixedService` iterates `service.methods`
  unguarded and mcp's fixed service has none. Fix is `service.methods ?? []`, but **ask first**: it
  makes the output diverge from what the source actually produces. Not present on spec-v2 branches.
- **`main` emits `// Unknown type:`** for `Error`, untagged object types, and `Other` —
  `renderTypeDef` only handles Record/Enum/Union/Constant/Class. Spec-v2 branches render these.
- **Submodule-only APIs render as README-only** (`azure_storage_service`, formerly `candid`):
  extraction reads `pkg.getDefaultModule()` only.
- Some libraries genuinely export nothing (`amp`, `idetraceprovider`) — an empty render is correct.

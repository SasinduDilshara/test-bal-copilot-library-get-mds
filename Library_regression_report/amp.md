# ballerinax/amp 1.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/amp` |
| Pinned version | `1.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-amp |
| Tag reviewed | `v1.1.0` (commit `2b5c84af1c931f08ce2593d6fcc63cfd779e1e55`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/amp/1.1.0` |
| Old render | `60` lines |
| New render | `60` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`old` and `new` are **byte-identical** (same MD5 for both the `.bal.txt` renders and the intermediate
JSONs). This is the expected outcome: `ballerinax/amp` is an observability *extension* package whose
single module `amp` exports **zero public symbols**. Its only module-level declarations are two
private `const`s, eleven module-private `configurable` variables, a private `init()` and a private
`external` function — none of them `public`, so nothing reaches the extractor. Both renders therefore
consist of the header banner, the `import` line, and the verbatim README block. The spec v2 changes
(real definitions for `Error`/object/`Other` types, dropped version-qualified type refs) have no
surface to act on here — `old` contains 0 `// Unknown type:` lines and 0 version-qualified refs to
begin with.

One pre-existing, shared defect was found and confirmed by compilation: the render's `import
ballerinax/amp;` line does not compile (`unused module prefix 'amp'`); the package's own README
prescribes `import ballerinax/amp as _;`. It is identical in both sides, so it is not a regression,
but it is an inaccuracy an LLM would copy.

## 2. Change inventory

| Metric | old | new | delta |
|---|---|---|---|
| Render lines | 60 | 60 | 0 |
| Render bytes | 2079 | 2079 | 0 |
| Render MD5 | `35eda12edb097628c27314d4b75559b6` | `35eda12edb097628c27314d4b75559b6` | identical |
| JSON bytes | 2214 | 2214 | 0 |
| JSON MD5 | `a76fc2ef855e100953c7cd25abeb4b3d` | `a76fc2ef855e100953c7cd25abeb4b3d` | identical |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Section markers (`// --- `) | 2 | 2 | 0 |
| Declaration lines (function/type/class/enum/const/annotation/listener/service/configurable) | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |

`diff -u old/ballerinax_amp.bal.txt new/ballerinax_amp.bal.txt` exits 0 (no output).
`diff old/ballerinax_amp.json new/ballerinax_amp.json` exits 0.

By kind — added / removed / modified between `old` and `new`:

| Kind | Added | Removed | Modified |
|---|---|---|---|
| function | 0 | 0 | 0 |
| type (record/enum/union/error/object/other) | 0 | 0 | 0 |
| class / client | 0 | 0 | 0 |
| const | 0 | 0 | 0 |
| annotation | 0 | 0 | 0 |
| service / listener | 0 | 0 | 0 |
| client method / resource | 0 | 0 | 0 |
| README lines | 0 | 0 | 0 |

JSON payload on both sides: `typeDefs: []`, `clients: []`, `functions: []`, `services: []`,
`annotations: []`, plus `name` (14 chars), `description` (143 chars), `readme` (1712 chars).

## 3. Correctness against library source

Nothing was added or changed by `new`, so this section verifies that the empty API surface is
*correct* rather than a truncation.

- Bala default module contains exactly one source file:
  `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/amp/1.1.0/java21/modules/amp/tracer_provider.bal`
  (58 lines). It is **byte-identical** to the upstream tag source
  `work/amp/src/ballerina/tracer_provider.bal` at `v1.1.0` (`diff` exits 0).
- `grep -c 'public ' tracer_provider.bal` → **0**. Every declaration is module-private:
  - `tracer_provider.bal:21-22` — `const PROVIDER_NAME`, `const DEFAULT_SAMPLER_TYPE` (not `public`)
  - `tracer_provider.bal:24-34` — eleven `configurable` variables (`otelEndpoint`, `apiKey`,
    `serviceName`, `orgUid`, `projectUid`, `componentUid`, `environmentUid`, `samplerType`,
    `samplerParam`, `reporterFlushInterval`, `reporterBufferSize`) — none `public`
  - `tracer_provider.bal:36` — `function init()` (not `public`)
  - `tracer_provider.bal:52-57` — `function externInitializeConfigurations(...) = @java:Method {...} external` (not `public`)
- `package.json` `export: ["amp"]` — a single exported module, which is the default module; Central
  metadata `modules` also lists exactly one module named `amp`. There is no submodule API.
- README block in the render (lines 8–59) is a verbatim copy of
  `java21/docs/README.md` (51 lines); the only `diff` hunk is one trailing blank line added by the
  renderer (`51a52 > `). No content dropped, no truncation, no encoding damage.
- Header description line (render line 3) matches the Central `summary` field exactly, including the
  embedded raw HTML anchor (which comes from the package metadata itself, not the renderer).

Conclusion: an empty declaration set is the factually correct rendering of this package.

## 4. Regressions

**None found.**

Basis for that conclusion: the two renders and the two JSONs are byte-identical (MD5 match on all
four files; `diff` exits 0 on both pairs). There is no declaration, parameter, default, return type,
doc string, README line, annotation, or section marker present in `old` that is absent or altered in
`new` — because the files are the same file content. The precomputed diff
(`OLD_AND_NEW_DIFFS/amp_diff.md`: 0 added, 0 removed, 0 hunks) agrees and was independently verified.

## 5. Issues in `new` (independent of `old`)

1. **The emitted import line does not compile.** Render line 5 is `import ballerinax/amp;`. Because
   the module exports no symbols, the prefix can never be used. Verified by building a probe package
   against the pinned bala:
   `bal build --offline` → `ERROR [main.bal:(1:19,1:22)] unused module prefix 'amp'`.
   The package's own README (render lines 22–24) prescribes `import ballerinax/amp as _;`. An LLM
   consuming this render would emit a non-compiling import. This is present in `old` too, so it is a
   pre-existing renderer-template issue, not a spec-v2 regression, but it is a real defect for this
   class of "extension" package (no public API, import-for-side-effect only).
2. **README is emitted as raw Markdown inside a `.bal.txt` body** (lines 8–59: `## Package
   Overview`, fenced code blocks, etc.), so the file as a whole is not valid Ballerina. Framed by
   `// --- README ---` / `// --- END README ---` markers, so this is the renderer's intended format
   and shared with `old`; noted only because for this library the README *is* the entire payload.
3. The description/banner carries raw HTML (`<a target="_blank" href="https://ballerina.io/">`)
   inside a `//` comment. It originates from the package summary in Central, not from the renderer.

## 6. Coverage gaps vs. the library

**0 gaps.** Public symbols exported by the default module (`amp`) that appear in neither render:
**none** — the default module has zero `public` declarations (`grep -c 'public ' ` → 0 over the only
`.bal` file in the bala module directory).

Submodule-only API: **none**. `package.json` `export` lists only `amp`, and
`java21/modules/` contains only the `amp` directory, so the `getDefaultModule()`-only extraction
limitation described in the brief costs nothing for this library.

Informational (not a coverage gap under the brief's definition, which is scoped to *public* symbols):
the eleven `configurable` variables at `tracer_provider.bal:24-34` are module-private and thus
correctly absent from the declaration sections; however they are the package's entire user-facing
contract, and they *are* documented in the README block that both renders carry (render lines 40–56
list `otelEndpoint`, `apiKey`, `orgUid`, `projectUid`, `componentUid`, `environmentUid`). The README
does not mention `serviceName`, `samplerType`, `samplerParam`, `reporterFlushInterval`, or
`reporterBufferSize`, so those five configurables are invisible to a consumer of either render. That
is an upstream documentation gap, identical on both sides.

## 7. Compiler plugin

The package ships **no compiler plugin**:
- `ls -a` on `.../amp/1.1.0/java21/` → only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
  `package.json`, `platform`. No `compiler-plugin/` directory, no `compiler-plugin.json`.
- Upstream at `v1.1.0`: `find src -type d -name '*compiler-plugin*'` → no results;
  `find src -name CompilerPlugin.toml` → no results. The `native/` module is the JVM implementation
  of `AmpTracerProvider` (bound via `@java:Method`), not a compiler plugin.

Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- **Not deprecated.** Central: `"isDeprecated": false`, `"deprecateMessage": ""`.
- **Post-1.0, stable version line** (`1.1.0`); `graalvmCompatible: Yes`; built for
  `ballerina_version 2201.13.0`, `language_spec_version 2024R1`; `pullCount` 558.
- **Size/token implications**: trivial — 60 lines / 2079 bytes per render. Essentially all of it is
  README prose. No token-budget concern.
- **Runtime deps** are all `ballerina/io`, `ballerina/jballerina.java`, `ballerina/observe` plus ten
  Java platform jars (OpenTelemetry SDK/exporters, OkHttp, Kotlin stdlib) — none of which surface in
  the render, correctly.
- The published package compiles as a dependency (the probe build's only error was the unused-prefix
  error from the import style, not from the package itself).
- Because the useful content is 100% README, this library's render quality is entirely a function of
  README fidelity, which is exact here. Any future extractor work on configurables would be the only
  way to improve it.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ballerinax_amp.bal.txt new/ballerinax_amp.bal.txt` | 60 / 60 |
| 2 | `diff -u old/ballerinax_amp.bal.txt new/ballerinax_amp.bal.txt` | exit 0, no output |
| 3 | `diff old/ballerinax_amp.json new/ballerinax_amp.json` | exit 0 (`JSON_IDENTICAL`) |
| 4 | `md5` on all four files | renders `35eda12edb097628c27314d4b75559b6`; JSONs `a76fc2ef855e100953c7cd25abeb4b3d` |
| 5 | `wc -c old/*.json new/*.json` | 2214 / 2214 |
| 6 | `grep -c '^// Unknown type:'` on both renders | 0 / 0 |
| 7 | `grep -c '^// --- '` on both renders | 2 / 2 |
| 8 | `grep -cE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service\|configurable)'` on both renders | 0 / 0 |
| 9 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:' old/...bal.txt` | 0 |
| 10 | JSON key/shape dump via `python3 -c json.load` | `typeDefs/clients/functions/services/annotations` all length 0; `readme` 1712 chars |
| 11 | `ls -R .../bala/ballerinax/amp/1.1.0` | one platform `java21`; modules → `amp` only; single file `tracer_provider.bal` |
| 12 | `cat .../java21/package.json` | `export: ["amp"]`, `ballerina_version 2201.13.0`, `graalvmCompatible true`, `readme: docs/README.md` |
| 13 | `git ls-remote --tags https://github.com/ballerina-platform/module-ballerinax-amp` | `v1.0.0`, `v1.1.0` (peeled `2b5c84af…`) |
| 14 | `git clone --depth 1 --branch v1.1.0 … src` | success |
| 15 | `cat src/gradle.properties \| grep version` | `version=1.1.0` (matches pin) |
| 16 | `diff src/ballerina/tracer_provider.bal <bala>/modules/amp/tracer_provider.bal` | identical (`BAL_IDENTICAL`) |
| 17 | `grep -c 'public ' src/ballerina/tracer_provider.bal` | 0 |
| 18 | `find src -type d -name '*compiler-plugin*'` / `find src -name CompilerPlugin.toml` | no results |
| 19 | `diff <bala>/docs/README.md <render lines 8-59>` | only `51a52 >` (one trailing blank line) |
| 20 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/amp/1.1.0` | `isDeprecated:false`, one module `amp`, `graalvmCompatible: Yes`, pullCount 558, summary matches render line 3 |
| 21 | Probe package `import ballerinax/amp;` + `bal build --offline` | `ERROR [main.bal:(1:19,1:22)] unused module prefix 'amp'` |
| 22 | `cat OLD_AND_NEW_DIFFS/amp_diff.md` | 0 added, 0 removed, 0 hunks — verified against checks 2–4 |

Files read in full: `<bala>/java21/modules/amp/tracer_provider.bal` (58 lines);
`amp/new/ballerinax_amp.bal.txt` (60 lines); `<bala>/java21/docs/README.md` (via diff);
`src/ballerina/Ballerina.toml`.

Scratch dir used: `…/scratchpad/work/amp` (clone at `src/`, probe package at `probe/`).

## 10. Caveats and unverified items

- The `old` render was not re-generated by me; I audited the committed artifacts under `amp/old/`
  and `amp/new/`. That both were produced at the same pinned version is taken from the brief's
  `PIN_OK` statement plus the fact that both JSONs are byte-identical and consistent with the
  1.1.0 bala — I did not re-run the two-stage pipeline.
- The probe compilation (check 21) used the locally installed distribution
  (`/Users/admin/.ballerina/ballerina-home/bin/bal`), not necessarily `2201.13.0`; the
  `unused module prefix` diagnostic is distribution-stable, but the exact distribution version used
  for the probe was not pinned.
- The Java native side (`native/`, `AmpTracerProvider`) was not reviewed beyond confirming it is not
  a compiler plugin; it cannot contribute Ballerina declarations to the render.
- Central `sourceCodeLocation` is empty for this package, so the repo URL was taken from the
  manifest (verified reachable, and the tag source matches the bala byte-for-byte, which
  independently confirms the repo is the right one).

# ballerinax/idetraceprovider 0.9.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/idetraceprovider` |
| Pinned version | `0.9.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-idetraceprovider |
| Tag reviewed | `v0.9.0` (commit `e01b2af603434a699e72ef994107240545d7da69`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/idetraceprovider/0.9.0/java21` |
| Old render | `44` lines |
| New render | `44` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

The `old` and `new` renders are **byte-for-byte identical** (same MD5), and so are the two
intermediate JSONs. This library is an observability *extension*, not an API library: its single
module contains **zero public declarations**, so both pipelines correctly emit an empty API section
and only the header + README. Spec v2 has nothing to change here because there was nothing degraded
in `old` — no `// Unknown type:` lines, no version-qualified type refs, no type/function/client/
service/annotation entries at all.

Verified exhaustively (the whole library is one 33-line `.bal` file), not spot-checked.

## 2. Change inventory

| Metric | old | new | delta |
|---|---|---|---|
| Render lines | 44 | 44 | 0 |
| Render MD5 | `32b9ad124c557e9716b926a2cf4a9ec3` | `32b9ad124c557e9716b926a2cf4a9ec3` | identical |
| JSON bytes | 1592 | 1592 | 0 |
| JSON MD5 | `0dc772f32ee326f31ef090a39618f2b1` | `0dc772f32ee326f31ef090a39618f2b1` | identical |
| `typeDefs` | 0 | 0 | 0 |
| `clients` | 0 | 0 | 0 |
| `functions` | 0 | 0 | 0 |
| `services` | 0 | 0 | 0 |
| `annotations` | 0 | 0 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Declarations (`function`/`type`/`class`/`enum`/`const`/`annotation`/`listener`/`service`) | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| Section markers | `// --- README ---` (L7), `// --- END README ---` (L44) | same | none |

Declarations added / removed / modified between `old` and `new`, by kind: **0 / 0 / 0** in every
kind. `diff old new` produces no output for both the `.bal.txt` and the `.json`. The precomputed
mechanical diff (`OLD_AND_NEW_DIFFS/idetraceprovider_diff.md`: 0 added, 0 removed, 0 hunks) was
re-verified against the files and is correct.

## 3. Correctness against library source

The bala's module source is one file, `modules/idetraceprovider/tracer_provider.bal`, and it is
**identical** to the upstream tag `v0.9.0` file `ballerina/tracer_provider.bal` (`diff` → no output).
Its entire declaration set:

| Symbol | Kind | Visibility | In render? | Correct? |
|---|---|---|---|---|
| `PROVIDER_NAME` (`tracer_provider.bal:20`) | `const` | module-private (no `public`) | no | correct to omit |
| `endpoint` (`tracer_provider.bal:22`) | `configurable string` | module-private | no | correct to omit (see §8) |
| `init()` (`tracer_provider.bal:24`) | `function` | module-private, lifecycle init | no | correct to omit |
| `externInitializeConfigurations(string)` (`tracer_provider.bal:30`) | `function`, `@java:Method` external | module-private | no | correct to omit |

`grep -nE '\bpublic\b' src/ballerina/tracer_provider.bal` → **no matches**. There is no public API to
render, so an empty API body in both renders is the correct output. Nothing is invented in `new`.

README fidelity: the `readme` field in the render JSON is **string-equal** to the bala's
`docs/README.md` (1110 chars both), which is in turn **identical** to upstream `ballerina/README.md`
and to the `readme` returned by Ballerina Central for `ballerinax/idetraceprovider/0.9.0`. The
render's lines 8–42 reproduce it verbatim including both fenced `toml` blocks and the
`endpoint=...` default-value comment. The header description (line 3) matches the Central `summary`
field exactly, HTML anchor and all.

## 4. Regressions

**None found.**

Basis for that conclusion — every one of these was run and returned "no difference":
- `diff old/ballerinax_idetraceprovider.bal.txt new/ballerinax_idetraceprovider.bal.txt` → empty.
- `diff old/ballerinax_idetraceprovider.json new/ballerinax_idetraceprovider.json` → empty.
- `md5` on all four files → old and new hashes match pairwise.
- Line counts, section markers, `// Unknown type:` counts, declaration counts, and
  version-qualified-ref counts are equal on both sides (all measured, §2).

Since the files are identical, no declaration, parameter, default, return type, doc string, README
line, or annotation can have been dropped, truncated, mangled, or made less accurate in `new`.

## 5. Issues in `new` (independent of `old`)

One low-severity issue, present identically in both sides (so not a regression, but it is a defect
in `new`):

1. **Header import form contradicts the package's prescribed usage.** Render line 5 emits
   `import ballerinax/idetraceprovider;`. Because the module exports **nothing**, a prefixed import
   is unusable and the package README itself — reproduced two lines later at render line 20 —
   prescribes `import ballerinax/idetraceprovider as _;`. An LLM copying the header line would
   produce an unused-module-prefix import rather than the documented `as _` form. This comes from
   the renderer's generic header template, not from the library. Both renders carry it.

No wrong types, invented symbols, broken doc text, or encoding issues were found. The HTML anchor
tag in the description/README (`<a target="_blank" href="https://ballerina.io/">`) is present in the
authoritative Central `summary` and README, so it is faithful passthrough, not corruption.

## 6. Coverage gaps vs. the library

**0 gaps.** `package.json` `"export": ["idetraceprovider"]` — a single exported module, which is the
default module. `modules/` contains exactly one directory, `idetraceprovider`, with one `.bal` file;
there are **no submodules**, so the known shared `getDefaultModule()`-only limitation is not
exercised here. The default module exports no public symbols, so there is nothing that "appears in
neither render" but should.

Submodule-only API: none (n/a).

## 7. Compiler plugin

**No compiler plugin exists.** Evidence:
- The bala root contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json`, `platform/` — there is no `compiler-plugin/` directory and no
  `compiler-plugin.json`.
- The upstream tag `v0.9.0` file tree contains no `compiler-plugin`/`*-compiler-plugin` module;
  `settings.gradle` wires only `ballerina` and `native`.
- The native side is a **runtime SPI provider**, not a compiler plugin:
  `native/src/main/resources/META-INF/services/io.ballerina.runtime.observability.tracer.spi.TracerProvider`
  registering `io.ballerina.observe.trace.idetraceprovider.IdeTracerProvider`.

Consequently nothing plugin-derived (code actions, validations, generated artifacts, annotations) is
expected in the render, and nothing is missing.

## 8. Other considerations

- **Pre-1.0 / unstable.** Version `0.9.0`, first published 2025-11-04 (`createdDate`
  `1762243388000`), 553 pulls. API may change without semver guarantees.
- **Not deprecated.** Central: `"isDeprecated": false`, `"visibility": "public"`,
  `"graalvmCompatible": "Yes"`.
- **Version drift: none.** `Ballerina.toml` at tag `v0.9.0` declares `version = "0.9.0"`;
  `gradle.properties` `version=0.9.0`; bala `package.json` `"version": "0.9.0"`. All three agree
  with the pin.
- **The `configurable string endpoint` is not modelled by either render.** It is module-private and
  configurables are not part of the Copilot library model, so this is not a coverage gap in the
  sense of §6 — and it is not information loss either, because the README block (render lines 34–42)
  documents the `[ballerinax.idetraceprovider] endpoint=...` key and its default
  `http://localhost:59500/v1/traces`. An LLM consuming this render still has what it needs to
  configure the extension.
- **Token/size implications: negligible.** 44 lines, ~1.6 KB of JSON, of which the README is ~1.1 KB.
  The render is essentially "README + a usage note", which is the right shape for a package whose
  entire contract is an import plus TOML configuration.
- **Central metadata is thin**: `licenses`, `authors`, `keywords`, and `sourceCodeLocation` are all
  empty on Central even though `Ballerina.toml` sets `license`, `authors`, `keywords`, and
  `repository`. This affects Central's UI, not the render.

## 9. Evidence log

| # | Check (command / file:line) | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 44 and 44 |
| 2 | `diff old/ballerinax_idetraceprovider.bal.txt new/...bal.txt` | no output (identical) |
| 3 | `diff old/ballerinax_idetraceprovider.json new/...json` | no output (identical) |
| 4 | `wc -c old/*.json new/*.json` | 1592, 1592 |
| 5 | `md5 old/* new/*` | render `32b9ad12…` both; json `0dc772f3…` both |
| 6 | `grep -c '^// Unknown type:'` on both renders | 0, 0 |
| 7 | `grep -cE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service)'` on both | 0, 0 |
| 8 | `grep -n '^// --- '` on both | L7 `README`, L44 `END README` — same on both |
| 9 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` on both | 0, 0 |
| 10 | Python: lengths of `typeDefs/clients/functions/services/annotations` in `new` JSON | 0/0/0/0/0 |
| 11 | Python: `new` JSON `readme` == bala `docs/README.md` | `True` (1110 == 1110 chars) |
| 12 | `ls -R` bala `0.9.0` | one platform `java21`; `modules/idetraceprovider/tracer_provider.bal` only; no `compiler-plugin/` |
| 13 | `cat` bala `package.json` | `"export": ["idetraceprovider"]`, `"version": "0.9.0"`, `ballerina_version 2201.12.0`, `graalvmCompatible true` |
| 14 | `cat` bala `dependency-graph.json` | deps `ballerina/observe 1.6.0`, `ballerina/jballerina.java 0.0.0`; one module |
| 15 | `git ls-remote --tags <repo>` | exactly one tag: `v0.9.0` → `e01b2af6…` |
| 16 | `git clone --depth 1 --branch v0.9.0` | success; tree has `ballerina/`, `native/`, `build-config/` only |
| 17 | `diff src/ballerina/tracer_provider.bal <bala>/modules/idetraceprovider/tracer_provider.bal` | no output (identical) |
| 18 | `diff src/ballerina/README.md <bala>/docs/README.md` | no output (identical) |
| 19 | `grep -nE '\bpublic\b' src/ballerina/tracer_provider.bal` | no matches → zero public symbols |
| 20 | `src/ballerina/Ballerina.toml` `[package]` | `version = "0.9.0"`, `distribution = "2201.12.0"` |
| 21 | `grep -i version src/gradle.properties` | `version=0.9.0`, `ballerinaLangVersion=2201.12.0` |
| 22 | `curl` Central `/2.0/registry/packages/ballerinax/idetraceprovider/0.9.0` | `isDeprecated false`, 1 module `idetraceprovider`, `summary` matches render L3, `readme` matches render L8–42 |
| 23 | `find src -type f` | no `compiler-plugin*`; native SPI file `META-INF/services/io.ballerina.runtime.observability.tracer.spi.TracerProvider` present |
| 24 | Render L5 vs README L20 | header emits plain import; README prescribes `as _` (issue §5.1) |

## 10. Caveats and unverified items

- **Not verified: whether an unused prefixed import of this module is a hard compile error or a
  warning** on distribution `2201.12.0`. §5.1 is stated as an inconsistency with the package's own
  documented usage, which *is* verified (render L5 vs render L20 / upstream `ballerina/README.md`);
  the exact diagnostic severity was not reproduced by compiling.
- **Not verified: the Java native implementation's behaviour.** `IdeTracerProvider.java` was located
  but not audited line by line; it is out of scope for a render regression review since no Java
  symbol reaches the render.
- Everything else asserted in this report was measured or read directly; no estimates were used.

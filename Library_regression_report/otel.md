# ballerina/otel 0.9.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/otel` |
| Pinned version | `0.9.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-otel |
| Tag reviewed | `v0.9.0` (commit `3083537502c3d26e63ec019a14b77a52b2ccd62d`) |
| Bala inspected | `/private/tmp/claude-501/-Users-admin-Desktop-Copilot-Changes-Check-contents-test-bal-copilot-library-get-mds/19909936-2e4b-46de-9886-3075396fe81e/scratchpad/extrabala/otel/0.9.0` |
| Old render | `103` lines |
| New render | `103` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`ballerina/otel` is an observability *extension*, not an API library. Its single module `otel`
exports **zero public symbols** — every declaration in the published sources is module-private
(`configurable` variables, unexported `function`s, one unexported `class MetricsSnapshotJob`, and
`const`s). Consequently the Copilot model for this package legitimately contains an empty
`typeDefs`/`clients`/`functions`/`services`/`annotations` set, and the render is README-only.

`old` and `new` are **byte-identical** on both stages of the pipeline: the stage-1 JSON and the
stage-2 `.bal.txt` have matching MD5s. Spec v2 changed nothing here because there was nothing for
`renderTypeDef` to degrade — `// Unknown type:` count is 0 on both sides.

## 2. Change inventory

| metric | old | new |
|---|---|---|
| `.bal.txt` lines | 103 | 103 |
| `.bal.txt` MD5 | `11d1f18a7569ac78eb9d30ad31f89842` | `11d1f18a7569ac78eb9d30ad31f89842` |
| `.json` lines | 9 | 9 |
| `.json` MD5 | `b09871aa0c874a1606fc4c6f42994c09` | `b09871aa0c874a1606fc4c6f42994c09` |
| `typeDefs` / `clients` / `functions` / `services` / `annotations` | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |
| `// Unknown type:` lines | 0 | 0 |
| `// --- ` section markers | 2 (`README`, `END README`) | 2 |
| declaration lines (`function`/`type`/`class`/`enum`/`const`/`annotation`/`listener`/`service`/`configurable`) | 0 | 0 |

Declarations added: **0**. Removed: **0**. Modified: **0**.
`diff -u old/ballerina_otel.bal.txt new/ballerina_otel.bal.txt` exits 0 with no output.
`diff old/ballerina_otel.json new/ballerina_otel.json` produces no output.

This matches the precomputed diff at `OLD_AND_NEW_DIFFS/otel_diff.md` ("The two files are
identical", 0 hunks) — verified independently, not copied.

## 3. Correctness against library source

The render's entire payload is the package README. Verified exactly:

- `json["readme"]` on both sides equals `<bala>/docs/README.md` **character for character**
  (4678 chars each; Python string equality returned `True` for both `old` and `new`).
- The `.bal.txt` region between `// --- README ---` and `// --- END README ---` equals
  `bala README + "\n"` exactly (4679 chars) — the single extra byte is the renderer's separating
  newline, not truncation.
- `<bala>/docs/README.md` is byte-identical to upstream `ballerina/README.md` at tag `v0.9.0`
  (`diff -q` clean), so the render's doc text is faithful to the tagged source.
- All five published module sources in the bala (`configs.bal`, `constants.bal`,
  `metrics_reporter.bal`, `observability_initializer.bal`, `tracer_provider.bal`) are
  byte-identical to `ballerina/*.bal` at `v0.9.0` (`diff -q` clean on all five). GitHub and the
  bala do not disagree, so there is no bala-wins situation to resolve.

There are no signatures to check: `grep -rn "^public \|^annotation \|^listener \|^service "` over
both `<bala>/modules/otel/` and `<src>/ballerina/*.bal` returns nothing on both. The `class
MetricsSnapshotJob` (`metrics_reporter.bal:57`) is unexported; its `public function execute()`
is a member of a private class, so it is not part of the package's public surface. The two
`external` functions (`metrics_reporter.bal:74`, `tracer_provider.bal:60`) are also private.

## 4. Regressions

**None found.**

Basis for that conclusion — every one of these checks was run and came back clean:
- `diff -u` of the two `.bal.txt` files: no hunks, exit 0.
- MD5 equality of both `.bal.txt` and both `.json` files.
- Both JSONs have identical, empty `typeDefs`/`clients`/`functions`/`services`/`annotations`.
- `readme` field identical on both sides and equal to the bala README.
- `// Unknown type:` count is 0 in `old` as well as `new`, so the spec-v2 "degraded Error/object
  type" class of change does not apply to this package — there was no degraded content in `old`
  that `new` could have lost or that `new` had to repair.
- No version-qualified type refs (`mod:x.y.z:Type`) exist in either file, since there are no type
  refs at all.

Nothing was dropped, truncated, mangled, or made less accurate. The relevant foundational-type
concern from the addendum (`sql:Error`, `time:Utc`, …) does not arise: this package re-exports no
types and its dependencies (`observe`, `log`, `io`, `task`, `jballerina.java`) are only used
internally.

## 5. Issues in `new` (independent of `old`)

One item, cosmetic but potentially misleading to an LLM consumer. It is present identically in
`old`, so it is **not** a regression:

1. **Line 4 of the render is `import ballerina/otel;`** — the renderer's boilerplate import header.
   For this package that import is wrong: the module exports no symbols, so a user program
   containing `import ballerina/otel;` would nothing to reference and Ballerina rejects unused
   imports. The package's own README (render lines 21–24) states the correct form is
   `import ballerina/otel as _;`. An LLM copying the header line would emit non-compiling code.
   This is a generic renderer behaviour applied to a `_`-import-only extension package, not an
   otel-specific extractor bug.

No invented symbols, no wrong types, no broken doc text, no encoding problems. The README's
em-dashes and `©` characters survive correctly in both the JSON (`—`, `©`) and the
rendered UTF-8 text (render lines 96–99).

## 6. Coverage gaps vs. the library

**Zero.** The default module `otel` exports no public symbols, so there is nothing that could be
missing from the render.

- `package.json` `"export": ["otel"]` — a single module, which is also the default module.
- `<bala>/modules/` contains exactly one directory, `otel`. There are **no submodules**, so the
  known shared `getDefaultModule()`-only limitation has no effect on this package.
- Central metadata for `ballerina/otel/0.9.0` lists exactly one module, `otel`.
- `grep -rn "^public "` over `<bala>/modules/otel/` returns nothing.

## 7. Compiler plugin

**No compiler plugin.** Confirmed three ways, matching `has_plugin: false` in the manifest:

- `<bala>/compiler-plugin` does not exist (`ls` → "No such file or directory"). The bala root
  contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`,
  `platform/`.
- `package.json` has no `compiler-plugin` / `compilerPlugin` key (`grep -i compiler` → no match).
- The upstream clone at `v0.9.0` has no `compiler-plugin`, `*-compiler-plugin`, or
  `ballerina-*-compiler-plugin` directory (`find -maxdepth 3 -type d` → no results). Top-level
  dirs are `ballerina`, `ballerina-tests`, `build-config`, `gradle`, `native`, `size-reduction-test`.

Nothing plugin-implied is therefore absent from the render.

## 8. Other considerations

- **Pre-1.0 version.** `0.9.0` is pre-release; the package is not API-stable. It also has no API
  to be stable about, so churn risk is confined to configurable names.
- **The library's public contract is `Config.toml` keys, not Ballerina symbols.** The 22
  `configurable` variables in `configs.bal:17–53` are the real user-facing surface, and the Copilot
  model has no slot for configurables — it captures them only incidentally, because the README
  happens to document them in its TOML snippets. This is a structural limitation of the model for
  extension packages, shared by both sides. As it happens the README covers all of the
  configurables a user needs (`tracesEndpoint`, `tracesSampler`, `tracesSamplerArg`,
  `tracesExporterTimeoutMillis`, `tracesMaxExportBatchSize`, `tracesProtocol`, `tracesLogConsole`,
  `tracesLogFile`, `tracesLogLevel`, `tracesExporterHeaders`, `tracesResourceAttributes`, and the
  eight `metrics*` equivalents), so the render is functionally adequate despite carrying no
  declarations.
- **Broken/incorrect link in the library's own README**, faithfully reproduced by both renders
  (render line 9): "a [Otel](https://www.oteltracing.io/) Agent". `www.oteltracing.io` does not
  resolve (`host` → `NXDOMAIN`; `curl` → HTTP code `000`). The phrasing "Otel Agent" and the
  domain shape look like a search-and-replace artefact from the Jaeger extension README. This is a
  defect in the upstream package, not in either render, but it means both renders feed an LLM a
  dead URL and a slightly confused description.
- **Size/token implications:** trivial. 103 lines / 4.7 KB of README. No token pressure either way.
- **Distribution/bala note:** contrary to the batch addendum's expectation for the seven
  Central-fetched packages, this bala *does* have a `platform/` subdirectory (`platform/java21`
  with 13 jars). `modules/` and `docs/` sit at the bala root as described. Nothing depended on
  this, but it is recorded so the assumption is not carried forward.
- Package is not deprecated (`deprecated: null` in Central metadata), `visibility: public`,
  `graalvmCompatible: true`, built for distribution `2201.13.4` — the same distribution used for
  the renders.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l otel/{old,new}/ballerina_otel.{bal.txt,json}` | 103 / 103 lines `.bal.txt`; 9 / 9 lines `.json` |
| 2 | `diff -u old/ballerina_otel.bal.txt new/ballerina_otel.bal.txt` | no output, exit 0 |
| 3 | `diff old/ballerina_otel.json new/ballerina_otel.json` | no output (IDENTICAL) |
| 4 | `md5` on all four files | `.bal.txt` both `11d1f18a7569ac78eb9d30ad31f89842`; `.json` both `b09871aa0c874a1606fc4c6f42994c09` |
| 5 | `grep -c '^// Unknown type:'` on both renders | 0 and 0 |
| 6 | `grep -c '^// --- '` on both renders | 2 and 2 (README / END README) |
| 7 | `grep -cE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service\|configurable)'` on both renders | 0 and 0 |
| 8 | Python: JSON `typeDefs/clients/functions/services/annotations` lengths (new) | 0 / 0 / 0 / 0 / 0 |
| 9 | Python: `json["readme"] == <bala>/docs/README.md` for old and new | `True`, `True` (4678 chars each) |
| 10 | Python: render README block == bala README + `"\n"` | `True` (4679 chars) |
| 11 | `ls -R <bala>` | `bala.json`, `dependency-graph.json`, `docs/`, `modules/otel/`, `package.json`, `platform/java21/` (13 jars) |
| 12 | `ls <bala>/modules` | single entry `otel` — no submodules |
| 13 | `ls <bala>/modules/otel` | `configs.bal`, `constants.bal`, `metrics_reporter.bal`, `observability_initializer.bal`, `tracer_provider.bal` |
| 14 | `grep -rn "^public \|^isolated public\|^public isolated\|^@display\|^annotation " <bala>/modules/otel/` | `(none)` |
| 15 | `grep -rn "listener\|client class\|service " <bala>/modules/otel/` | `(none)` |
| 16 | `cat <bala>/package.json` | `"export": ["otel"]`, `ballerina_version 2201.13.4`, `graalvmCompatible true`, no compiler-plugin key |
| 17 | `ls <bala>/compiler-plugin` | No such file or directory |
| 18 | `git ls-remote --tags .../module-ballerina-otel` | only `v0.9.0` → `3083537502c3d26e63ec019a14b77a52b2ccd62d` |
| 19 | `git clone --depth 1 --branch v0.9.0 …` | succeeded into scratch `work/otel/src` |
| 20 | `grep -rn "^public \|^annotation \|^listener \|^service " <src>/ballerina/*.bal` | `(none)` |
| 21 | `diff -q <src>/ballerina/<f>.bal <bala>/modules/otel/<f>.bal` for all 5 files | all IDENTICAL |
| 22 | `diff -q <src>/ballerina/README.md <bala>/docs/README.md` | IDENTICAL |
| 23 | `find <src> -maxdepth 3 -type d -name "*compiler-plugin*"` (and `*compiler_plugin*`) | no results |
| 24 | `cat <src>/ballerina/Ballerina.toml` | `org=ballerina name=otel version=0.9.0 distribution=2201.13.4` — pin confirmed |
| 25 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/otel/0.9.0` | 1 module `otel`; `deprecated: null`; `ballerinaVersion 2201.13.4`; `balaVersion 3.0.0`; `visibility public` |
| 26 | `host www.oteltracing.io` / `curl -o /dev/null -w %{http_code}` | `NXDOMAIN` / `000` — README link is dead |
| 27 | `cat OLD_AND_NEW_DIFFS/otel_diff.md` | 0 added, 0 removed, 0 hunks — consistent with checks 2–4 |
| 28 | `cat <bala>/dependency-graph.json` | otel depends on `observe 1.7.1`, `log 2.17.0`, `io 1.8.1`, `task 2.11.2`, `jballerina.java` |

## 10. Caveats and unverified items

- **Not verified: that the two renders were actually produced by the two different `ballerina-vscode`
  commits.** Because the outputs are byte-identical, nothing in the artefacts themselves proves
  `new` was regenerated rather than copied. I take the brief's statement of provenance at face
  value. For a package with an empty API surface, identical output is the expected result either
  way, so this does not change the verdict.
- **Not verified: runtime behaviour.** I did not build or execute the package, so claims about
  what the extension does at runtime rest on reading `tracer_provider.bal` / `metrics_reporter.bal`
  and the README, not on observation.
- **Not verified: the native jar.** `platform/java21/otel-extension-native-0.9.0.jar` was not
  decompiled; the Java classes referenced by the `@java:Method` externs
  (`io.ballerina.observe.trace.otel.OtelTracerProvider`, `…OtelMetricsProvider`) were not confirmed
  to exist in it. Irrelevant to the render, which contains no external function declarations.
- **Claim in §5 that `import ballerina/otel;` would fail to compile** is based on Ballerina's
  unused-import rule plus the confirmed absence of any public symbol; I did not compile a test
  program to demonstrate the diagnostic.

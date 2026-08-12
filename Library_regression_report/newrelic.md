# ballerinax/newrelic 1.0.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/newrelic` |
| Pinned version | `1.0.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-newrelic |
| Tag reviewed | `v1.0.3` (commit `860ec1515b313bfcd60142f170a98c45bd4db696`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/newrelic/1.0.3` |
| Old render | `111` lines |
| New render | `111` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`old` and `new` are **byte-identical** — same MD5 for both the `.bal.txt` renders and the intermediate
`.json` files. Nothing changed, and nothing could have: `ballerinax/newrelic` is an observability
extension whose default module `newrelic` declares **zero public symbols**. Every function, const and
`configurable` in the published sources is module-private, so the extractor's `typeDefs`, `clients`,
`functions`, `services` and `annotations` arrays are all empty on both sides. The render therefore
consists only of the header banner, the `import` line, and the verbatim `Package.md` README block.

Spec v2's headline behaviours (replacing `// Unknown type:` stubs, dropping version-qualified type
refs) have no surface to act on here — there are 0 `// Unknown type:` lines in either file, and 0
declarations in either file.

## 2. Change inventory

| Metric | old | new | delta |
|---|---|---|---|
| Lines | 111 | 111 | 0 |
| MD5 (`.bal.txt`) | `844203863e87a2052cf78e72a3888b42` | `844203863e87a2052cf78e72a3888b42` | identical |
| MD5 (`.json`) | `cc91a8b2005f0a0039ff11cc92226f33` | `cc91a8b2005f0a0039ff11cc92226f33` | identical |
| JSON `typeDefs` / `clients` / `functions` / `services` / `annotations` | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| `// --- ` section markers | 2 (`README`, `END README`) | 2 | 0 |
| Declaration lines (function/type/class/enum/const/annotation/listener/service) | 0 | 0 | 0 |

Added: 0. Removed: 0. Modified: 0. `diff -u` exits 0 for both the render and the JSON.
This matches `OLD_AND_NEW_DIFFS/newrelic_diff.md` ("The two files are identical", 0 hunks) — verified
independently, not copied.

## 3. Correctness against library source

Upstream `v1.0.3` was shallow-cloned and compared file-by-file against the bala; the three `.bal`
files and `Package.md` are **identical** between GitHub `ballerina/` and the bala
`modules/newrelic/` + `docs/`, so there is no GitHub-vs-bala disagreement to arbitrate.

Public API check — `grep -n 'public ' ` over all three sources returns **no matches** in either
copy:

| File (bala `modules/newrelic/`) | Declarations | Visibility |
|---|---|---|
| `observe.bal` (65 lines) | `const REPORTER_NAME`, `const PROVIDER_NAME`, `const NEW_RELIC_API_KEY_ENV`, `configurable string\|string[] apiKey`, `configurable boolean isTraceLoggingEnabled`, `configurable boolean isPayloadLoggingEnabled`, `function init()`, `function parseStringArray()` | all module-private |
| `metrics_reporter.bal` (41 lines) | `configurable int metricReporterFlushInterval`, `configurable int metricReporterClientTimeout`, `configurable map<string> additionalAttributes`, `isolated function startMetricsReporter()`, `isolated function externSendMetrics()` (`@java:Method`) | all module-private |
| `tracer_provider.bal` (54 lines) | `const DEFAULT_SAMPLER_TYPE`, `configurable string tracingSamplerType`, `configurable decimal tracingSamplerParam`, `configurable int tracingReporterFlushInterval`, `configurable int tracingReporterBufferSize`, `function startTracerProvider()`, `function externStartPublishingTraces()` (`@java:Method`) | all module-private |

An empty API section is therefore the **correct** rendering, on both sides.

README fidelity: the render's README block (lines 8–110) is character-for-character the bala's
`docs/Package.md` (102 lines), with one trailing blank line inserted before the `// --- END README ---`
marker. It also matches the `readme` field returned by Ballerina Central for `1.0.3`. The header
comment on line 3 matches Central's `summary` field exactly, HTML anchors included.

## 4. Regressions

**None found.** Basis: the two `.bal.txt` files and the two `.json` files are byte-identical
(`diff -u` exit 0; matching MD5s). No declaration, parameter, default, return type, doc line, README
line, or annotation can have been dropped, because no byte differs.

## 5. Issues in `new` (independent of `old`)

1. **No machine-readable surface for the module's `configurable` variables** (shared with `old`).
   The only thing a user actually interacts with in this package is its ten `configurable` values
   (`apiKey`, `tracingSamplerType`, `tracingSamplerParam`, `tracingReporterFlushInterval`,
   `tracingReporterBufferSize`, `metricReporterFlushInterval`, `metricReporterClientTimeout`,
   `additionalAttributes`, `isTraceLoggingEnabled`, `isPayloadLoggingEnabled`). The extractor emits
   no representation of these — they survive only as prose inside the README's `Config.toml` snippet
   (render lines 42–56). The prose is accurate and includes defaults, so an LLM is not misled, but
   the information is untyped. This is an extractor-model limitation, identical on both sides, not a
   `new` regression.
2. **The README block is not comment-prefixed** (shared with `old`). Render lines 8–110 are raw
   Markdown (`## Package Overview`, fenced code blocks, tables) emitted inside a `.bal.txt` file
   between `// --- README ---` markers, so the file as a whole is not compilable Ballerina. This is
   the renderer's intended README framing and is unchanged between sides.

No wrong types, invented symbols, broken doc text, or encoding issues were found — the README bytes
match the bala and Central exactly.

## 6. Coverage gaps vs. the library

**0 gaps.** `package.json` declares `"export": ["newrelic"]` — a single module, which is the default
module, so the `getDefaultModule()`-only extraction path loses nothing here. The bala's
`modules/` listing contains exactly one directory (`newrelic`); there are no submodules and hence no
submodule-only shared gap. That default module exports zero public symbols, so there is nothing the
render could be missing.

## 7. Compiler plugin

No compiler plugin exists. The upstream repo at `v1.0.3` has no `compiler-plugin/` or
`*-compiler-plugin/` directory (only `ballerina/`, `native/`, `build-config/`), and the bala contains
no `compiler-plugin/` entry or `compiler-plugin.json`. The `native/` module supplies the runtime Java
classes referenced by `@java:Method` (`io.ballerina.observe.metrics.newrelic.NewRelicMetricsReporter`,
`io.ballerina.observe.trace.newrelic.NewRelicTracerProvider`), shipped as
`newrelic-extension-native-1.0.3.jar` — a runtime dependency, not a plugin. Nothing plugin-derived is
therefore expected in, or absent from, the render.

## 8. Other considerations

- **Not deprecated.** Central reports `isDeprecated: false`, `deprecateMessage: ""`. Stable 1.0.x.
  `graalvmCompatible: "Yes"`, `pullCount: 3013`.
- **Usage is import-only.** The package is consumed as `import ballerinax/newrelic as _;` plus
  `Config.toml`/`Ballerina.toml` settings — the README documents this correctly, which is the entire
  value this render carries.
- **Size/token cost is trivial**: 111 lines, ~4 KB, dominated by the README. No token-budget concern.
- **Central metadata is thin**: `licenses`, `authors`, `keywords` empty and `sourceCodeLocation` is
  `""`, so the repo URL cannot be confirmed from Central metadata (it was confirmed by the tag
  `v1.0.3` existing and its sources matching the bala byte-for-byte).
- Ballerina distribution `2201.11.0`, language spec `2024R1`, platform `java21`.

## 9. Evidence log

| Check | Command / file | Result |
|---|---|---|
| Line counts | `wc -l old/…bal.txt new/…bal.txt` | 111 / 111 |
| Render diff | `diff -u old/…bal.txt new/…bal.txt` | exit 0, no output |
| JSON diff | `diff -u old/…json new/…json` | exit 0; 5559 lines each |
| Checksums | `md5 old/* new/*` | render `8442…b42` both; json `cc91…f33` both |
| JSON model counts | `python3` load of `new/ballerinax_newrelic.json` | keys `name, description, readme, typeDefs, clients, functions, services, annotations`; all five arrays length 0 |
| Degraded types | `grep -c '^// Unknown type:'` | 0 in old, 0 in new |
| Section markers | `grep -c '^// --- '` | 2 in old, 2 in new |
| Declarations | `grep -cE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service) '` | 0 in old, 0 in new |
| Bala module list | `ls .../1.0.3/java21/modules` | `newrelic` only |
| Bala sources | `wc -l .../modules/newrelic/*.bal` | `metrics_reporter.bal` 41, `observe.bal` 65, `tracer_provider.bal` 54 (160 total) |
| Public symbols in bala | `grep -n 'public ' .../modules/newrelic/*.bal` | no matches |
| Exports | `.../java21/package.json` | `"export": ["newrelic"]`, `ballerina_version 2201.11.0`, `platform java21` |
| Compiler plugin in bala | `ls .../1.0.3/java21 \| grep -i plugin` | none |
| Tag resolution | `git ls-remote --tags <repo>` | `v1.0.3` → `860ec15…` (peeled `fc11f11…`) |
| Upstream clone | `git clone --depth 1 --branch v1.0.3` into scratch `src` | succeeded |
| Upstream public symbols | `grep -c 'public ' src/ballerina/*.bal` | 0, 0, 0 |
| Upstream vs bala sources | `diff -q src/ballerina/{observe,metrics_reporter,tracer_provider}.bal` vs bala | identical (exit 0) |
| Upstream vs bala README | `diff -q src/ballerina/Package.md .../docs/Package.md` | identical |
| Render README vs bala Package.md | `diff` of render lines 8–110 vs `docs/Package.md` | identical except one extra trailing blank line in render |
| Upstream layout | `ls src` | no `compiler-plugin` dir; `ballerina/`, `native/`, `build-config/` |
| Central metadata | `GET https://api.central.ballerina.io/2.0/registry/packages/ballerinax/newrelic/1.0.3` | `isDeprecated false`, 1 module `newrelic`, `readme` matches render, `summary` matches render line 3 |
| Precomputed diff cross-check | `OLD_AND_NEW_DIFFS/newrelic_diff.md` | claims 0 added / 0 removed / 0 hunks — confirmed |

## 10. Caveats and unverified items

- The `@java:Method` externals (`NewRelicMetricsReporter.sendMetrics`,
  `NewRelicTracerProvider.startPublishingTraces`) were not decompiled from
  `newrelic-extension-native-1.0.3.jar`; their behaviour is out of scope since both are bound to
  private Ballerina functions that neither render can expose.
- Central's `sourceCodeLocation` is empty, so the repo URL is confirmed only indirectly — by the
  `v1.0.3` tag's sources matching the bala byte-for-byte, which is strong evidence.
- Whether the empty-API render is *desirable* (versus, say, the extractor being extended to emit
  `configurable` variables) is a product question, not a regression question; this report only
  establishes that both sides behave identically and match the library.

# ballerinax/moesif 1.0.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/moesif` |
| Pinned version | `1.0.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-moesif |
| Tag reviewed | `v1.0.3` (exact tag, commit `0d6f8b7ca919dbef013a22b1d1eac349cfce610c`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/moesif/1.0.3` |
| Old render | `295` lines |
| New render | `295` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`old` and `new` are **byte-identical** — same MD5 for both the `.bal.txt` renders and both `.json`
intermediates. This is the expected outcome: `ballerinax/moesif` is a pure observability *extension*
package whose default module `moesif` exports **zero public symbols**. There are no types, clients,
functions, services or annotations for the extractor to emit, so neither the spec-v2 type-definition
work nor the `// Unknown type:` fix has anything to act on. Both renders consist of the header
banner, a single `import` line, and the full README verbatim.

The README is reproduced with 100% fidelity (byte-equal to `docs/README.md` in the bala, 9,388
characters). One pre-existing inaccuracy is carried by both sides: the emitted `import
ballerinax/moesif;` line does not compile (`unused module prefix`), whereas the package's own README
instructs `import ballerinax/moesif as _;`.

## 2. Change inventory

| Metric | old | new | delta |
|---|---|---|---|
| Lines | 295 | 295 | 0 |
| MD5 (`.bal.txt`) | `50e41f06b2d316e528237dd061f520a2` | `50e41f06b2d316e528237dd061f520a2` | identical |
| MD5 (`.json`) | `72c8aea70f30f7740edeae0cb5bb8a6b` | `72c8aea70f30f7740edeae0cb5bb8a6b` | identical |
| `// Unknown type:` lines | 0 | 0 | 0 |
| `// --- ` section markers | 2 (`README`, `END README`) | 2 | 0 |
| JSON `typeDefs` | 0 | 0 | 0 |
| JSON `clients` | 0 | 0 | 0 |
| JSON `functions` | 0 | 0 | 0 |
| JSON `services` | 0 | 0 | 0 |
| JSON `annotations` | 0 | 0 | 0 |

`diff -u old/ballerinax_moesif.bal.txt new/ballerinax_moesif.bal.txt` → empty (exit 0).
`diff -q old/ballerinax_moesif.json new/ballerinax_moesif.json` → identical (exit 0).

Declarations added / removed / modified, by kind: **none in any kind** (function 0, type 0, class 0,
enum 0, const 0, annotation 0, service 0, listener 0, client method 0).

The precomputed diff at `OLD_AND_NEW_DIFFS/moesif_diff.md` claims "The two files are identical,
0 hunks" — verified true against the files.

## 3. Correctness against library source

The bala's `modules/moesif/` contains exactly two files, both byte-identical to the upstream
`v1.0.3` sources (`diff` returned no output for both):

- `constants.bal` (9 lines) ↔ `src/ballerina/constants.bal`
- `observability_provider.bal` (73 lines) ↔ `src/ballerina/observability_provider.bal`

`grep -n "public" modules/moesif/*.bal` → **no matches (exit 1)**. Every declaration is
module-private:

- 9 module-private `const` declarations (`PROVIDER_NAME`, `DEFAULT_SAMPLER_TYPE`,
  `METRIC_TYPE_GAUGE`, `METRIC_TYPE_SUMMARY`, `EMPTY_STRING`, `NEW_LINE`, `EXPIRY_TAG`,
  `PERCENTILE_TAG`, `APP_ID_HEADER`) — `constants.bal:1-9`.
- 11 module-private `configurable` variables — `observability_provider.bal:20-31`.
- `function init()` — `observability_provider.bal:34`, not public.
- `function externInitializeConfigurations(...) external` — `observability_provider.bal:61`, not public.
- `isolated function externSendMetrics(...) external` — `observability_provider.bal:67`, not public.

Ballerina Central corroborates: the API for `ballerinax/moesif/1.0.3` lists one module (`moesif`)
with `0` functions and `0` classes.

Therefore an empty API render is the *correct* render. Both sides produce it.

README fidelity (verified programmatically): the JSON `readme` field is `==` to
`bala/.../docs/README.md` read as text (9,388 chars, exact equality `True`), and render lines 8–294
stripped are `==` to that README stripped (`True`). Upstream `src/ballerina/README.md` is also
byte-identical to the bala README. Nothing is truncated, re-wrapped, or HTML-escaped — the embedded
`docker-compose.yml`, `fluent-bit.conf` and `otelcol.yaml` fenced blocks survive intact, including
the non-ASCII characters (`→`, `’`) which round-trip correctly as UTF-8.

## 4. Regressions

**None found.**

Basis for that conclusion, in full:
- `diff -u` of the two `.bal.txt` files produces zero hunks; MD5s match.
- `diff -q` of the two `.json` files reports no difference; MD5s match.
- All five JSON API arrays are length 0 on both sides, so nothing could have been dropped.
- README length and content are byte-identical between the two JSONs and the bala source.

Since the two artifacts are the same bytes, no declaration, parameter, default, return type, doc
comment, annotation, or README section can have been lost in `new`.

## 5. Issues in `new` (independent of `old`)

1. **Non-compiling import line (shared with `old`, so not a regression, but wrong in `new`).**
   Render line 5 emits:
   ```
   import ballerinax/moesif;
   ```
   Because the package exports nothing, this is a hard compile error. Verified empirically with the
   local distribution (`2201.12.7`): a probe package containing only that import fails with
   `ERROR [main.bal:(1:19,1:25)] unused module prefix 'moesif'` / `error: compilation contains errors`.
   The package's own README (rendered immediately below, line 28) says the correct form is
   `import ballerinax/moesif as _;`. An LLM copying the render's header import will emit
   non-compiling code. The renderer emits this header import unconditionally and has no notion of
   an "extension-only" package; the fix belongs in `toSyntaxString`, not in the library.

No other issues: no invented symbols (there are no symbols), no wrong types, no broken doc text, no
encoding damage, no missing default-module public API.

## 6. Coverage gaps vs. the library

**0 gaps.** The default module `moesif` exports zero public symbols (`grep -n "public"` over the
bala's `.bal` files returns nothing; Central reports 0 functions / 0 classes), so there is no public
symbol that appears in neither render.

Submodule-only API: none. `bala/.../modules/` contains exactly one directory, `moesif`, which *is*
the default module (`package.json` `"export": ["moesif"]`). The shared `getDefaultModule()`
limitation described in the brief therefore has no effect here.

Worth noting rather than counting as a gap: the package's entire *usable* surface is its 11
module-level `configurable` variables (`applicationId`, `reporterBaseUrl`, `samplerType`,
`samplerParam`, `tracingReporterFlushInterval`, `tracingReporterBufferSize`,
`metricsReporterFlushInterval`, `metricsReporterClientTimeout`, `additionalAttributes`,
`isTraceLoggingEnabled`, `isPayloadLoggingEnabled`, `idleTimePublishingEnabled`). The Copilot
library model has no slot for configurables, and neither render emits them structurally — but all
of them except `samplerType`, `samplerParam` and `idleTimePublishingEnabled` are documented with
their defaults in the rendered README (`Config.toml` blocks, render lines 43–77). So the practical
information loss is limited to those three, and it is identical on both sides.

## 7. Compiler plugin

**The package ships no compiler plugin.** Evidence:
- `ls -R` of the bala shows no `compiler-plugin/` directory and no `compiler-plugin.json`.
- Upstream `v1.0.3` has no `compiler-plugin`-named directory; `grep -rl
  "CompilerPlugin\|CodeAnalyzer\|CodeModifier"` over the clone returns nothing.
- The only Java in the repo is the runtime native extension:
  `native/src/main/java/io/ballerina/observe/metrics/moesif/MoesifMetricReporter.java`,
  `native/src/main/java/io/ballerina/observe/trace/moesif/MoesifTracerProvider.java`,
  `.../sampler/RateLimiter.java`, `.../sampler/RateLimitingSampler.java`, `module-info.java`.
  These are the `@java:Method` targets of the two `extern` functions, shipped as
  `platform/java21/moesif-extension-native-1.0.3.jar`.

Nothing a plugin implies is missing from the render, because there is no plugin. There are also no
annotations to surface (JSON `annotations` = 0 on both sides).

## 8. Other considerations

- **Not deprecated.** Central returns an empty `deprecateMessage` and no `deprecated: true`.
  `pullCount` 62, `visibility` public, `template` false.
- **Stable 1.x** version; no pre-1.0 instability caveat.
- **Package description contains raw HTML.** The header line 3 and the JSON `description` are
  `The Moesif observability extension is one of the observability extensions of the<a target="_blank"
  href="https://ballerina.io/"> Ballerina</a> language.` — an unclosed-looking inline anchor with a
  missing space before `<a`. This originates in the package summary itself (Central returns the same
  string), not in the renderer. Both sides carry it identically.
- **Size / token implications:** 295 lines, ~9.4 KB, essentially all README. This is one of the
  cheapest renders in the set. The README is heavy on YAML/conf infrastructure config (Fluent Bit,
  OTEL Collector) that is only marginally useful for Ballerina code generation, but it is the
  package's own documentation and truncating it is not the renderer's call.
- **Published package compiles**: not separately verified beyond the import probe above; the bala
  is a normal published artifact and its sources are byte-identical to the tagged upstream.
- Distribution pinned by the package: `2201.12.7` (`Ballerina.toml`, `package.json`
  `ballerina_version`).

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ballerinax_moesif.bal.txt new/ballerinax_moesif.bal.txt` | 295 / 295 |
| 2 | `diff -u old/ballerinax_moesif.bal.txt new/ballerinax_moesif.bal.txt` | no output, exit 0 |
| 3 | `diff -q old/ballerinax_moesif.json new/ballerinax_moesif.json` | identical, exit 0 |
| 4 | `md5` on all four artifacts | render `50e41f06…` both; json `72c8aea7…` both |
| 5 | `grep -c '^// Unknown type:'` on both renders | 0 / 0 |
| 6 | `grep -c '^// --- '` on both renders | 2 / 2 |
| 7 | Python: lengths of JSON `typeDefs`/`clients`/`functions`/`services`/`annotations` (new) | 0 / 0 / 0 / 0 / 0 |
| 8 | Python: same for old (via `diff -q` equality) | identical to new |
| 9 | `ls -R` of bala `1.0.3` | `java21/{bala.json,dependency-graph.json,docs,modules,package.json,platform}`; no `compiler-plugin/` |
| 10 | `cat bala .../package.json` | `"export": ["moesif"]`, `ballerina_version 2201.12.7`, 13 platform jars |
| 11 | `wc -l bala modules/moesif/*.bal` | `constants.bal` 9, `observability_provider.bal` 73 |
| 12 | `grep -n "public" bala modules/moesif/*.bal` | no matches (exit 1) |
| 13 | `git ls-remote --tags <repo>` | tags v1.0.0–v1.0.3; `v1.0.3` → `0d6f8b7ca919dbef013a22b1d1eac349cfce610c` |
| 14 | `git clone --depth 1 --branch v1.0.3` | succeeded |
| 15 | `diff src/ballerina/constants.bal bala/.../constants.bal` | IDENTICAL |
| 16 | `diff src/ballerina/observability_provider.bal bala/.../observability_provider.bal` | IDENTICAL |
| 17 | `diff src/ballerina/README.md bala/.../docs/README.md` | IDENTICAL |
| 18 | `cat src/ballerina/Ballerina.toml` | `version = "1.0.3"`, `distribution = "2201.12.7"` — pin confirmed on the source side |
| 19 | Python: JSON `readme` == bala `docs/README.md` | `True` (9,388 chars) |
| 20 | Python: render lines 8–294 (stripped) == README (stripped) | `True` |
| 21 | `find src -name '*.java'` under `native/src` | 5 files, all runtime (MetricReporter, TracerProvider, RateLimiter, RateLimitingSampler, module-info) |
| 22 | `grep -rl "CompilerPlugin\|CodeAnalyzer\|CodeModifier" src` | no matches |
| 23 | `curl` Central `packages/ballerinax/moesif/1.0.3` | modules `[('moesif', 0 functions, 0 classes)]`; no deprecation; pullCount 62 |
| 24 | `bal build` probe with `import ballerinax/moesif;` only | `ERROR [main.bal:(1:19,1:25)] unused module prefix 'moesif'` — render's import line does not compile |

## 10. Caveats and unverified items

- **Full-package compilability of the published bala** was not tested (only the import-form probe in
  evidence #24). Nothing observed suggests a problem.
- **Native Java behaviour** (`MoesifTracerProvider`, `MoesifMetricReporter`) was read only for the
  purpose of confirming there is no compiler plugin; its runtime correctness is out of scope for a
  render review and was not audited.
- The brief's stated `old`/`new` source commits (`eb5d81b3` / `412ba01e`) were taken as given; the
  two `ballerina-vscode` checkouts were not independently inspected. For this library it is moot —
  the outputs are byte-identical, so no renderer-behaviour claim depends on them.
- Whether `samplerType`, `samplerParam` and `idleTimePublishingEnabled` are *intentionally*
  undocumented in the README (vs. an upstream docs omission) is unknown; noted in §6 as an
  observation only, and it affects both sides equally.

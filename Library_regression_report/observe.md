# ballerina/observe 1.7.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/observe` |
| Pinned version | `1.7.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-observe |
| Tag reviewed | `v1.7.1` (commit `5906f44`, exact tag) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/observe/1.7.1/java21` |
| Old render | `508` lines |
| New render | `570` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old`. The two `// Unknown type:` placeholders in `old` (`Counter`,
`Gauge`) are replaced by full class definitions with all 14 member functions, and a new
`// --- Annotations ---` section surfaces `Observable`, which `old` omitted entirely. Nothing is
removed: `diff` reports 2 removed lines, both of which are the placeholder comments themselves.

The two JSONs differ in exactly two ways: `typeDefs[Counter]` and `typeDefs[Gauge]` gain
`"type": "Class"`, and `annotations` goes from `[]` (length 0) to length 1. `readme`, `functions`
(18 entries) and the four record `typeDefs` are byte-identical between the two JSONs. So all of the
render delta is attributable to the renderer/extractor change, not to any library difference —
consistent with the brief.

Three real inaccuracies survive in `new`, all inherited from the extractor (they are present in the
`old` JSON too but were invisible because `old` never rendered class bodies): the numeric default
values of `Counter.increment`, `Gauge.increment` and `Gauge.decrement` are rendered as `0` / `0.0`
when the library declares `1` / `1.0`.

## 2. Change inventory

Line counts (`wc -l`): old **508**, new **570** (+62). `diff -u`: 2 hunks, +64 / −2 lines.

Top-level declaration lines (`grep -nE '^(public )?(function|type|class|enum|const|annotation|listener|service) '`):
old **22**, new **25**.

| Kind | old | new | delta |
|---|---|---|---|
| `type … record` | 4 (`Metric`, `Snapshot`, `PercentileValue`, `StatisticConfig`) | 4 (identical text) | 0 |
| `class` | 0 | 2 (`Counter`, `Gauge`) | **+2** |
| class member functions (`^    function `) | 0 | 14 | **+14** |
| module-level `function` | 18 | 18 (identical text) | 0 |
| `annotation` | 0 | 1 (`Observable`) | **+1** |
| `// Unknown type:` placeholders | 2 | 0 | **−2** |
| `// --- section ---` markers | 4 | 5 (`Annotations` added) | +1 |

Added class members — Counter (6): `init`, `register`, `unregister`, `increment`, `reset`,
`getValue`. Gauge (8): `init`, `register`, `unregister`, `increment`, `decrement`, `setValue`,
`getValue`, `getSnapshot`.

**Removed: nothing.** The only `-` lines in the unified diff are
`-// Unknown type: Counter` and `-// Unknown type: Gauge`.

README section: identical in both (`readme` strings compare equal in Python; 11,501 chars).
No version/module-qualified type refs (`mod:x.y.z:Type`) in either file (0 / 0).

## 3. Correctness against library source

The clone at `v1.7.1` and the bala agree byte-for-byte for the whole default module —
`diff -q` on `annotations.bal`, `commons.bal`, `natives.bal` produced no output for all three.
Citations below are to the bala (= clone) paths.

Default module public surface, enumerated from the clone
(`grep -hnE '^public ' ballerina/*.bal` → 25 declarations): 18 functions, 2 classes, 4 records,
1 annotation. All 25 appear in `new`. Exhaustive check of the newly added material:

`natives.bal:135` `public isolated class Counter`:

| render (new) | source | verdict |
|---|---|---|
| `function init(string name, string\|() desc = "", map<string>\|() tags = ()) returns ();` | `natives.bal:148` `init(string name, string? desc = "", map<string>? tags = ())` | correct (`T?` ≡ `T\|()`) |
| `function register() returns error?;` | `natives.bal:163` | correct |
| `function unregister() returns ();` | `natives.bal:168` | correct |
| `function increment(int amount = 0) returns ();` | `natives.bal:176` `increment(int amount = 1)` | **WRONG default** (see §5) |
| `function reset() returns ();` | `natives.bal:181` | correct |
| `function getValue() returns int;` | `natives.bal:188` | correct |

`natives.bal:231` `public isolated class Gauge`:

| render (new) | source | verdict |
|---|---|---|
| `function init(string name, string\|() desc = "", map<string>\|() tags = (), StatisticConfig[]\|() statisticConfig = ()) returns ();` | `natives.bal:249-250` | correct |
| `function register() returns error?;` | `natives.bal:262` | correct |
| `function unregister() returns ();` | `natives.bal:267` | correct |
| `function increment(float amount = 0.0) returns ();` | `natives.bal:275` `increment(float amount = 1.0)` | **WRONG default** |
| `function decrement(float amount = 0.0) returns ();` | `natives.bal:283` `decrement(float amount = 1.0)` | **WRONG default** |
| `function setValue(float amount) returns ();` | `natives.bal:290` | correct |
| `function getValue() returns float;` | `natives.bal:297` | correct |
| `function getSnapshot() returns Snapshot[]\|();` | `natives.bal:305` `returns Snapshot[]?` | correct |

Doc strings on both classes and all 14 methods match the source doc comments verbatim (e.g.
new:403-404 vs `natives.bal:141-142`; new:438 "Unregister the counter metric instance…" reproduces
the copy-paste wording that actually appears on `Gauge.unregister` at `natives.bal:266` — the render
is faithful, the typo is upstream).

Annotation, new:567-570 `public annotation Observable on function;` vs `annotations.bal:20`
`public const annotation Observable on source function;` — the symbol and attachment point are real;
`const` and `source` are dropped (§5).

Module-level functions (unchanged between sides) spot-checked exhaustively against
`commons.bal:52-97` and `natives.bal:29-128`: all 18 names, parameter names/types/defaults and
return types match, including the non-trivial ones —
`startSpan(string spanName, map<string>|() tags = (), int parentSpanId = -1) returns int|error`
(`natives.bal:40`), `addTagToSpan(string tagKey, string tagValue, int spanId = -1) returns error?`
(`natives.bal:70`), `finishSpanWithError(int spanId, error 'error) returns error?`
(`natives.bal:99`, quoted identifier preserved), and
`lookupMetric(string name, map<string>|() tags = ()) returns Counter|Gauge|()` (`natives.bal:125`).
Note the module-level `-1` defaults *are* rendered correctly, which is what isolates the defect in §5
to class-method numeric defaults.

The four records match `natives.bal:358, 372, 382, 395` field-for-field, including
`Snapshot[]|() summary` for `Snapshot[]? summary`. Foundational types other packages depend on
(`observe:Counter`, `observe:Gauge`, `observe:Metric`, `observe:Snapshot`, `observe:StatisticConfig`)
are therefore rendered with correct shapes in `new`; in `old`, `Counter` and `Gauge` were opaque.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new` shows exactly 2 hunks and exactly 2 removed lines, both the
  `// Unknown type:` placeholders. No declaration, parameter, default, return type or doc line is
  present in `old` and absent in `new`.
- Structural JSON comparison: `readme` equal, `functions` list equal, all four record `typeDefs`
  equal; the only field-level differences are the *added* `"type": "Class"` on `Counter`/`Gauge` and
  the *added* `annotations` entry.
- The `// --- README ---` / `// --- END README ---` block is identical (11,501 chars either side, and
  it still contains both the package README and the appended `## Module: observe.mockextension`
  section, new:327-339).
- Section marker set in `new` is a superset of `old` (4 → 5).
- No malformed output introduced: the added text follows the same stub grammar as the rest of the
  file (declaration + `;`, doc comments prefixed `#`); no unbalanced braces (`class Counter {` …
  `}` at new:406/426, `class Gauge {` … `}` at new:431/460).

## 5. Issues in `new` (independent of `old`)

1. **`Counter.increment` default rendered as `0`, actual `1`** — new:418. Origin is the JSON, not the
   renderer: `new/ballerina_observe.json` `typeDefs[Counter].functions[increment].parameters[0]` has
   `"default": "0"`. The same wrong value is already in `old/ballerina_observe.json` (verified), so
   this is a pre-existing extractor defect that `new` merely made visible. Misleading: the parameter
   doc immediately above it says "The amount is defaulted as 1", so the render contradicts itself,
   and an LLM could emit `counter.increment()` expecting a no-op.
2. **`Gauge.increment` default rendered as `0.0`, actual `1.0`** — new:443, same mechanism.
3. **`Gauge.decrement` default rendered as `0.0`, actual `1.0`** — new:447, same mechanism.
   Scope of the defect: only class-method numeric literal defaults are affected. String (`""`),
   nil (`()`) and module-level numeric (`-1`) defaults are all rendered correctly, so this is not a
   blanket defaults problem.
4. **Annotation qualifiers lost** — new:570 renders `public annotation Observable on function;`
   where the source is `public const annotation Observable on source function;`
   (`annotations.bal:20`). The JSON carries `"attachmentPoint": "FUNCTION"` with no `source` flag and
   no const marker. Low impact for code generation (usage is `@observe:Observable` either way), but
   the render is not a faithful declaration.
5. **`isolated` and `public` qualifiers dropped throughout** — all 18 module-level functions and both
   classes are `public isolated` in the source (`grep '^public ' ballerina/*.bal`) but render as bare
   `function` / `class`. Shared with `old` for the functions; newly applicable to `Counter`/`Gauge`
   in `new`. For a foundational module this loses information a caller needs: whether these can be
   called from an `isolated` function. Inconsistent too — the annotation line *is* rendered with
   `public`.

Not issues: `returns ()` on `init` and on nil-returning methods, and method bodies replaced by `;`,
are the render format's stub convention, applied consistently across the file.

## 6. Coverage gaps vs. the library

**Default module (`observe`) — top-level public symbols missing from both renders: 0.**
All 25 (`18 functions + 2 classes + 4 records + 1 annotation`, from
`grep -hnE '^public ' <clone>/ballerina/*.bal`) are present in `new`. In `old`, `Counter` and `Gauge`
were present in name only.

**Missing sub-declarations: 7 public class fields**, in neither render:
- `Counter`: `public final string name`, `public final string description`,
  `public final map<string> & readonly metricTags` (`natives.bal:137-139`)
- `Gauge`: `name`, `description`, `metricTags`, plus
  `public final StatisticConfig[] & readonly statisticConfigs` (`natives.bal:233-236`)

These are readable public state (`counter.name`, `gauge.statisticConfigs`) that the render gives no
way to discover. The JSON has no `fields` key on the `Class` typeDefs at all, so this is an extractor
gap, present on both sides.

**Submodule-only API — shared gap, not a regression.** `package.json` `export` is
`["observe", "observe.mockextension"]` and `modules/` contains both, but extraction is
`getDefaultModule()`-only, so `observe.mockextension`'s **13** public symbols appear in neither
render: types `Event`, `Span` (`tracing.bal:23,36`), `Tag`, `MetricId`, `PercentileValue`,
`TimeWindow`, `Snapshot`, `Counter`, `Gauge`, `PolledGauge`, `Metrics` (`metrics.bal:22-103`), and
functions `getFinishedSpans(string serviceName) returns Span[]` (`tracing.bal:49`) and
`getMetrics() returns Metrics` (`metrics.bal:112`).

Worth flagging: the mockextension README **is** inlined into both renders (new:327-339) and shows
`mockextension:getFinishedSpans()` with no argument, while the real signature requires
`string serviceName`. That is an upstream README error, faithfully copied — but it means both renders
contain a call example that will not compile, for a module they otherwise do not document.

**Configurable variables** (`enabled`, `provider`, `metricsEnabled`, `metricsReporter`,
`tracingEnabled`, `tracingProvider`, `metricsLogsEnabled`, `commons.bal:20-26`) are non-`public`, so
their exclusion is correct by the extractor's rule, but it means the render offers no hint of the
`[ballerina.observe]` Config.toml knobs that are the primary way this module is used. Not counted as
a gap above.

## 7. Compiler plugin

`has_plugin: false` in the manifest — **confirmed**. `ls <bala>/compiler-plugin` →
"No such file or directory"; the bala root contains only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`, `platform/`. The clone has no `*compiler-plugin*` directory and
no `CompilerPlugin.toml` (`find` returned nothing). `Ballerina.toml` declares no
`[[package.compilerPlugin]]`. Nothing plugin-related should surface in the render, and nothing does.

The Java side of this package is a runtime native library (`platform/java21/observe-native-1.7.1.jar`
plus four OpenTelemetry SDK jars), not a compiler plugin.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerina/observe/1.7.1`: `deprecated: None`,
  `visibility: public`, `pullCount: 53832`, `ballerinaVersion: 2201.13.2`, modules
  `['observe', 'observe.mockextension']`. Stable 1.x.
- **Bala built with 2201.13.2, resolved from distribution 2201.13.4** — normal, and both renders came
  from the same bala, so it cannot explain any diff.
- **Size**: 570 lines, of which 335 (59%) are the inlined README. The API surface itself is ~230
  lines. Token cost is negligible; the +62 lines buy the two most useful types in the module.
- **README quality**: the inlined README is dated — it documents
  `--b7a.observability.enabled=true` CLI flags and `checkpanic observe:startSpan(...)` style, and
  uses `new("SimpleCounter")` (inferred-type `new`) which no longer matches current idiom. It also
  contains `observe:Counter gaugeWithTags = new("GaugeWithTags", …)` (a Counter typed variable in the
  Gauge section — an upstream copy-paste error). Both renders carry this verbatim; it is a source
  problem, not a pipeline problem, but it is the largest single block of text an LLM will read here.
- The `getSnapshot`/`summary` nil-union rendering (`Snapshot[]|()`) is semantically identical to the
  source's `Snapshot[]?` but is the less idiomatic spelling; consistent across both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v1.7.1 <repo> <scratch>/src` | succeeded; `git log --oneline -1` → `5906f44 [Gradle Release Plugin] - pre tag commit: 'v1.7.1'`; `git describe --tags` → `v1.7.1` |
| `diff -q <bala>/modules/observe/{annotations,commons,natives}.bal <clone>/ballerina/…` | no output for all three — bala and tag are byte-identical |
| `wc -l old/ballerina_observe.bal.txt new/ballerina_observe.bal.txt` | 508 / 570 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- '` old / new | old: README(7), END README(341), Types(343), Functions(407). new: same + Annotations(565); Functions at 462 |
| `diff -u old new` | 2 hunks, +64 / −2; removed lines are only the 2 placeholders |
| `grep -cE '^(public )?(function\|type\|class\|enum\|const\|annotation\|listener\|service) '` old / new | 22 / 25 |
| `grep -cE '^    function ' new` | 14 class member functions |
| Python JSON top-level key sizes | old: typeDefs 6, clients 0, functions 18, services 0, annotations 0. new: identical except annotations 1 |
| Python `o['readme']==n['readme']`, `o['functions']==n['functions']` | both `True` |
| Python per-typeDef comparison | only diffs: `Counter.type` and `Gauge.type` `None → 'Class'` |
| `new['annotations']` dump | `{"name":"Observable","attachmentPoint":"FUNCTION","description":"This is used for making a function observable.…"}` |
| Counter method defaults in **old** JSON | `init [(name,None),(desc,'\"\"'),(tags,'()')]`, `increment [(amount,'0')]` — wrong default pre-exists in `old` JSON |
| Old JSON module-function defaults | `startRootSpan tags='()'`, `startSpan tags='()' parentSpanId='-1'`, `addTagToSpan spanId='-1'`, `lookupMetric tags='()'` — all correct |
| `natives.bal:176, 275, 283` | `increment(int amount = 1)`, `increment(float amount = 1.0)`, `decrement(float amount = 1.0)` |
| `annotations.bal:20` | `public const annotation Observable on source function;` |
| `grep -hnE '^public ' <clone>/ballerina/*.bal` | 25 declarations: 18 functions, 2 classes, 4 records, 1 annotation |
| `grep -nE '^public ' <bala>/modules/observe.mockextension/*.bal` | 13 symbols (11 types + `getFinishedSpans`, `getMetrics`) |
| `<bala>/package.json` | `export: ['observe','observe.mockextension']`, `ballerina_version: 2201.13.2` |
| `ls <bala>/compiler-plugin` | No such file or directory |
| `find <clone> -iname '*compiler-plugin*' -o -name CompilerPlugin.toml` | no matches |
| `cat <clone>/ballerina/Ballerina.toml` | no `[[package.compilerPlugin]]`; only java21 platform deps |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/observe/1.7.1` | `deprecated: None`, `visibility: public`, `pullCount: 53832`, modules `['observe','observe.mockextension']` |
| Python: bala `docs/README.md` (11,227 chars) and `docs/modules/observe.mockextension/README.md` (238 chars) both contained in JSON `readme` (11,501 chars) | `True` / `True` |
| `OLD_AND_NEW_DIFFS/observe_diff.md` cross-check | its figures (508/570, +64/−2, 2 hunks, 2→0 placeholders, 4→5 markers) all reproduced independently |

## 10. Caveats and unverified items

- The mechanical diff file lists "Declarations added (12)"; that is a de-duplicated name set
  (`register`, `unregister`, `increment`, `getValue`, `init` each occur in both classes). My count of
  14 added member functions + 2 classes + 1 annotation comes from counting the render lines directly.
  Not a discrepancy, just different counting units — noted so the numbers reconcile.
- I could not determine *why* the extractor emits `0` / `0.0` for class-method numeric defaults while
  emitting `-1` correctly for module-level function defaults; the Java extractor source
  (`CopilotLibraryManager` / `ModelToJsonConverter`) is outside this repo and was not read. The
  *fact* of the wrong values is verified from both JSON files and the library source; the *cause* is
  unverified.
- Whether the `on source function` → `on function` and `const annotation` → `annotation` reduction is
  intentional in spec v2 or an oversight is unverified — I only verified that the JSON's
  `attachmentPoint` field has no room to express `source`.
- I did not attempt to compile the rendered `.bal.txt`; it is a stub format (bodiless methods inside
  a `class`) and is not expected to compile. Structural well-formedness was checked by eye and by
  brace pairing only.

# ballerina/cache 3.10.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/cache` |
| Pinned version | `3.10.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-cache |
| Tag reviewed | `v3.10.0` (exact tag; clone verified byte-identical to bala sources) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/cache/3.10.0/java21` |
| Old render | `78` lines |
| New render | `180` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`cache` is a small, single-module standard library: 5 public symbols in the default module
(`AbstractCache`, `CacheConfig`, `EvictionPolicy`, `Cache`, `Error`) across 382 lines of `.bal`.

`old` degraded two of those five to bare placeholders (`// Unknown type: Error`,
`// Unknown type: Cache`) and rendered `AbstractCache` as an empty `class {}`. `new` emits all five
with members: the `Cache` class with all 9 methods, the 8 `AbstractCache` methods, `type Error error;`,
and the four `@constraint:*` annotations on `CacheConfig` fields. Nothing present in `old` is missing
from `new`; the README block (lines 1–42) is byte-identical on both sides. **No regressions found.**

The newly surfaced content does carry pre-existing extractor inaccuracies that were previously invisible
because the whole `Cache` class was dropped — most notably two wrong/invented `decimal` defaults and an
`init` parameter list that is not valid Ballerina. These are `new`-visible issues, not regressions
(the same wrong values are already present in `old/ballerina_cache.json`).

## 2. Change inventory

Line counts (`wc -l`): old 78, new 180 (+102).

| Kind | old | new | Delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 | −2 |
| `// --- ` section markers | 3 | 3 | 0 |
| Top-level type decls rendered | 4 (`const LRU`, `class AbstractCache`, `type CacheConfig`, `enum EvictionPolicy`) | 6 (adds `type Error`, `class Cache`) | +2 |
| `AbstractCache` methods | 0 | 8 | +8 |
| `Cache` methods (incl. `init`) | 0 | 9 | +9 |
| `@constraint:*` annotations | 0 | 4 | +4 |
| Declarations removed | — | — | **0** |

Added declarations (verified by `grep -nE '^(type|class|enum|const|function|public|// Unknown)'` on both files):
- `type Error error;` (new:114)
- `class Cache { … }` (new:121–180) with `init, put, get, invalidate, invalidateAll, hasKey, keys, size, capacity`
- `class AbstractCache` body filled in (new:50–84) with `put, get, invalidate, invalidateAll, hasKey, keys, size, capacity`
- `@constraint:Int`, `@constraint:Float`, `@constraint:Number` ×2 inside `CacheConfig` (new:91, 94, 101, 104)

JSON level: both files have 6 `typeDefs`, 0 clients / 0 functions / 0 services / 0 annotations, and
identical `name`, `description` (223 chars) and `readme` (2397 chars). The `Cache.functions` array is
**byte-identical** between `old/ballerina_cache.json` and `new/ballerina_cache.json` — old simply lacked
`"type": "Class"` on the `Cache` typeDef, so `renderTypeDef` fell through to the placeholder. New adds
`"type":"Class"` on `Cache`, `functions` on `AbstractCache`, `baseType:"error"` on `Error`, and
`annotations` on 4 `CacheConfig` fields.

## 3. Correctness against library source

Bala sources are byte-identical to the `v3.10.0` clone (`diff -q` on all three `.bal` files → IDENTICAL),
so GitHub line numbers below apply to both.

| Rendered item | Source | Verdict |
|---|---|---|
| 8 `AbstractCache` methods, names/params/returns | `ballerina/abstract_cache.bal:19–72` | Correct — matches `put(string,any,decimal maxAge=-1)`, `get`, `invalidate`, `invalidateAll`, `hasKey`, `keys`, `size`, `capacity` |
| `AbstractCache.put` default `maxAge = -1` | `abstract_cache.bal:28` | Correct |
| 9 `Cache` methods present | `ballerina/cache.bal:102,136,170,188,202,214,224,234,244` | All 9 present, names and return types match |
| `Cache.get returns any\|Error` | `cache.bal:170` | Correct |
| `Cache.keys() returns string[]`, `size()/capacity() returns int`, `hasKey() returns boolean` | `cache.bal:214–244` | Correct |
| `EvictionPolicy` enum with single member `LRU` | `cache.bal:53` | Correct |
| `CacheConfig` field names/types/docs | `cache.bal:31–49` | Correct |
| `@constraint:Int {minValue:1}` on `capacity` | `cache.bal:32–34` | Correct |
| `@constraint:Float {minValueExclusive:0, maxValue:1}` on `evictionFactor` | `cache.bal:35–38` | Correct |
| `@constraint:Number {minValue:-1}` on `defaultMaxAge` | `cache.bal:42–44` | Correct |
| `@constraint:Number {minValueExclusive:0}` on `cleanupInterval` | `cache.bal:45–47` | Correct |
| `Cache.put` default `maxAge = 0.0d` | `cache.bal:136` says `decimal maxAge = -1` | **Wrong** (see §5.1) |
| `init` param `cleanupInterval = 0.0d` | `cache.bal:48` — `decimal cleanupInterval?;`, no default | **Invented** (see §5.2) |
| `init` trailing `CacheConfig cacheConfig` param | `cache.bal:102` — `init(*CacheConfig cacheConfig)` | **Malformed** (see §5.3) |
| `type Error error;` | `cache_errors.bal:18` — `public type Error distinct error;` | `distinct` lost (see §5.4) |

Non-public symbols correctly excluded from both renders: `Cleanup` class (`cache.bal:66`),
`CacheEntry` record (`cache.bal:57`), `prepareError` (`cache_errors.bal:24`), `externInit`/`externCleanUp`.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff` of the top-level declaration sets of both renders: the `old` set is a strict subset of `new`;
  `OLD_AND_NEW_DIFFS/cache_diff.md` reports "Declarations removed (0)" and I confirmed it independently
  with `grep -nE '^(type|class|enum|const|function|public|// Unknown)'` on both files.
- Lines 1–42 (header, module description, full README block) are byte-identical (`diff` → no output).
- Section markers: 3 in both (`// --- README ---`, `// --- END README ---`, `// --- Types ---`).
- `CacheConfig`: all 5 fields, their types and their doc comments are unchanged between the two renders;
  `new` only inserts annotation lines above 4 of them. No field, doc, or type was dropped.
- `EvictionPolicy`, `const string LRU`, and the `AbstractCache` doc comment are unchanged.
- Nothing in `old` was more accurate than the corresponding text in `new`: the two removed lines are
  `// Unknown type: Error` and `// Unknown type: Cache`, both replaced by real definitions.
- No version/module-qualified refs (`mod:x.y.z:Type`) exist on either side (0 matches both).

## 5. Issues in `new` (independent of `old`)

Six inaccuracies. All originate in the Java extractor / JSON (items 1, 5, 6 are already present in
`old/ballerina_cache.json`) but only 1–4 become visible in the rendered text because `old` dropped `Cache`.

1. **`Cache.put` default value is wrong.** new:130 renders
   `function put(string key, any value, decimal maxAge = 0.0d) returns Error|();`
   The library declares `public isolated function put(string key, any value, decimal maxAge = -1)`
   (`cache.bal:136`). `0.0d` means "expires immediately" semantics to a reader; `-1` means "valid forever".
   This is the single most misleading line in the render. The bad value is in both JSONs
   (`"default": "0.0d"`), so it is an extractor defect, not a renderer one.
   Note the *same* method on `AbstractCache` is rendered correctly with `-1` (new:55), so the render
   contradicts itself between the object type and its implementing class.

2. **`init` invents a default for `cleanupInterval`.** new:122 renders `decimal cleanupInterval = 0.0d`.
   `CacheConfig.cleanupInterval` is an optional field with **no** default (`cache.bal:48`), and its
   absence is semantically load-bearing: `cache.bal:110` does `if interval is decimal` to decide whether
   to schedule the cleanup task at all. Worse, `0` violates the field's own
   `@constraint:Number {minValueExclusive: 0}` (rendered two lines earlier at new:104) and would be
   flagged at compile time by the shipped compiler plugin as `CACHE_104`.

3. **`init` parameter list is not valid Ballerina.** new:122 ends with a required parameter after
   defaultable ones: `… decimal cleanupInterval = 0.0d, CacheConfig cacheConfig) returns ()`.
   The real signature is `init(*CacheConfig cacheConfig)` (`cache.bal:102`). The extractor flattened the
   included record into 5 defaultable params *and* kept the record parameter itself; the JSON marks it
   `"optional": true` with no `default`, and the renderer emits it as required. A code generator copying
   this will produce `new cache:Cache(…, cacheConfig)` calls that do not compile.

4. **`distinct` lost on the error type.** new:114 renders `type Error error;`; source is
   `public type Error distinct error;` (`cache_errors.bal:18`). `cache:Error` is a distinct error type
   that other packages match on; the render understates its subtyping.

5. **`AbstractCache` is rendered as a `class`, not an object type, and its body is not valid class
   syntax.** Source is `public type AbstractCache object { … }` (`abstract_cache.bal:19`) — a method-only
   object type. `new` emits `class AbstractCache { function put(...) returns Error|(); … }` — body-less
   methods inside a `class`, which does not compile. `old` had the same wrong `Class` kind (from
   `"type":"Class"` in both JSONs) but an empty body, so `new` makes the mislabel more visible.

6. **`CacheConfig` is rendered open and default-less.** Source is a **closed** record
   `record {| … |}` with defaults `capacity = 100`, `evictionFactor = 0.25`, `evictionPolicy = LRU`,
   `defaultMaxAge = -1` (`cache.bal:31–49`). Both renders show `record { … }` with every field marked
   optional (`?`) and no defaults; the JSON `fields` carry `"optional": true` and no `default` on both
   sides. Shared old/new gap, unchanged by spec v2.

Minor, shared, not counted above: `public` and `isolated` qualifiers are stripped from every method in
both renders (source methods are all `public isolated function`). An LLM copying the render into a custom
`AbstractCache` implementation would produce a non-isolated, non-public object that fails to match.

## 6. Coverage gaps vs. the library

Public symbols exported by the default module (the only module — `package.json` `"export": ["cache"]`,
`modules/` contains only `cache/`, Central lists exactly one module):

| Symbol | old | new |
|---|---|---|
| `AbstractCache` (`abstract_cache.bal:19`) | name only, empty body | full (8 methods) |
| `CacheConfig` (`cache.bal:31`) | yes | yes (+annotations) |
| `EvictionPolicy` (`cache.bal:53`) | yes | yes |
| `Cache` (`cache.bal:87`) | **missing** (placeholder) | full (9 methods) |
| `Error` (`cache_errors.bal:18`) | **missing** (placeholder) | yes |

**Coverage gaps in `new`: 0.** No submodule-only API exists for this library, so the shared
`getDefaultModule()` limitation has no effect here.

## 7. Compiler plugin

`has_plugin` is true and confirmed from the bala:
`compiler-plugin/compiler-plugin.json` → `plugin_id: cache-compiler-plugin`,
`plugin_class: io.ballerina.stdlib.cache.compiler.CacheCompilerPlugin`,
jar `compiler-plugin/libs/cache-compiler-plugin-3.10.0.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/stdlib/cache/compiler/`): a `CodeAnalyzer`
(`CacheCodeAnalyzer.java:33`) registering `CacheConfigValidator` on `LOCAL_VAR_DECL` and `MODULE_VAR_DECL`.
It validates literal `cache:CacheConfig` / `new cache:Cache(...)` argument values at compile time
(`CacheConfigValidator.java:180–220`, codes in `DiagnosticsCodes.java:29–36`):

| Code | Rule |
|---|---|
| CACHE_101 | `capacity` must be > 0 |
| CACHE_102 | `evictionFactor` must be in `[0, 1)` |
| CACHE_103 | `defaultMaxAge` must be > 0 or exactly `-1` |
| CACHE_104 | `cleanupInterval` must be > 0 |
| CACHE_105 | `evictionPolicy` must be `cache:LRU` |
| CACHE_106 | generic invalid value |

No code actions, no generated artifacts, no plugin-defined annotations — nothing the plugin implies is
missing from the render as a *declaration*. The plugin's value constraints are now partly conveyed by the
four `@constraint:*` annotations `new` adds, which is a genuine improvement for LLM consumption. The one
conflict: the render's own `cleanupInterval = 0.0d` default (§5.2) is exactly the value CACHE_104 rejects,
and `evictionFactor`'s plugin rule (`[0,1)`) differs from the `@constraint:Float` rule
(`(0,1]`) — an upstream inconsistency, not a render defect.

## 8. Other considerations

- Size: 180 lines / ~5.9 KB rendered — negligible token cost; the +102 lines buy the entire client-facing
  API surface. Strongly favourable trade.
- Stability: 3.10.0 is a stable release; Central metadata for `ballerina/cache/3.10.0` returns no
  deprecation flag and exactly one module.
- Doc quality: doc comments survive well, including the fenced ```ballerina examples on each `Cache`
  method. Parameter-level `+ key - …` docs are folded into the JSON `parameters[].description` but the
  renderer discards them, leaving a stray `# ` line before each signature (e.g. new:54, 129) — cosmetic
  noise present on both sides.
- The README block reproduced in the render hand-writes the `AbstractCache` object with
  `int maxAgeInSeconds` (render line 30) while the actual API uses `decimal maxAge` — an upstream README
  staleness carried identically into both renders.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_cache.bal.txt new/ballerina_cache.bal.txt` | 78 / 180 |
| `wc -c` on both JSONs | 14274 / 20571 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- '` old / new | 3 markers each, same order |
| `grep -nE '^(type\|class\|enum\|const\|function\|public\|// Unknown)'` both | old: 7 lines; new: 7 lines — old's 2 placeholders replaced by `type Error` + `class Cache` |
| `diff` of render lines 1–42 | identical (no output) |
| `sed -n '50,84p' new … \| grep -c '^    function'` | 8 (AbstractCache methods) |
| `sed -n '121,180p' new … \| grep -c '^    function'` | 9 (Cache methods) |
| `grep -c '@constraint:'` old / new | 0 / 4 |
| Python compare of `typeDefs` keys | old `Cache` has no `type` key; new has `"type":"Class"`; new `AbstractCache` gains `functions`; new `Error` gains `baseType:"error"` |
| Python: `json.dumps(old Cache.functions) == json.dumps(new Cache.functions)` | `True` — identical, incl. `"default":"0.0d"` on `put.maxAge` and `cleanupInterval` |
| `git clone --depth 1 --branch v3.10.0 …` | tag exists, clone succeeded |
| `diff -q clone/ballerina/*.bal bala/modules/cache/*.bal` | all 3 IDENTICAL |
| `grep -rn '^public ' bala/modules/cache/*.bal` | 5 public symbols: CacheConfig:31, EvictionPolicy:53, Cache:87, Error(cache_errors):18, AbstractCache(abstract_cache):19 |
| `sed -n 136p cache.bal` | `public isolated function put(string key, any value, decimal maxAge = -1) returns Error?` — render says `0.0d` |
| `sed -n 102p cache.bal` | `public isolated function init(*CacheConfig cacheConfig)` |
| `sed -n 45,48p cache.bal` | `@constraint:Number {minValueExclusive: 0}` / `decimal cleanupInterval?;` — no default |
| `cat bala/compiler-plugin/compiler-plugin.json` | plugin id/class/jar as quoted in §7 |
| `cat bala/package.json` | `"export": ["cache"]`, platform java21, graalvmCompatible true |
| `ls bala/modules/` | single dir `cache` — no submodules |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/cache/3.10.0` | one module `cache`, no deprecation field |
| `DiagnosticsCodes.java:29–36`, `CacheConfigValidator.java:180–220` | 6 diagnostic codes / validation rules as tabulated |
| `OLD_AND_NEW_DIFFS/cache_diff.md` claims (78/180 lines, +104/−2, 0 removed decls, 2→0 placeholders) | all independently reproduced |

## 10. Caveats and unverified items

- The `0.0d` defaults for `Cache.put.maxAge` and `init.cleanupInterval` are demonstrably wrong against the
  source, but I did **not** trace them to a specific line in the Java extractor (`ModelToJsonConverter` /
  `CopilotLibraryManager`) — the ballerina-vscode checkouts were not in scope for this review. Attribution
  ("extractor, not renderer") rests on the fact that the identical strings appear in both the `old` and
  `new` JSON, which I did verify.
- I did not compile the rendered `.bal.txt`; the "does not compile" claims in §5.3 and §5.5 are from
  reading the Ballerina grammar rules (required param after defaultable param; body-less method in a
  `class`), not from a `bal build` run.
- The evictionFactor discrepancy between the compiler plugin (`[0,1)`) and the `@constraint:Float`
  annotation (`(0,1]`) is reported as observed in the two sources; I did not test which one wins at
  build time.

# ballerina/etl 0.8.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/etl` |
| Pinned version | `0.8.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-etl |
| Tag reviewed | `v0.8.0` (clone HEAD `cba24c3`, `git describe --tags` → `v0.8.0`) |
| Bala inspected | `/private/tmp/claude-501/.../scratchpad/extrabala/etl/0.8.0` (fetched from Central; `modules/`, `platform/`, `docs/` directly under root) |
| Old render | `588` lines |
| New render | `593` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders differ in exactly 2 hunks, both in the `// --- Types ---` section. `new` replaces
the 2 `// Unknown type:` placeholders that `old` emitted (`Error`, `CategoryRanges`) with real type
definitions carrying their doc comments. Nothing is removed, reordered, or altered anywhere else:
the README block (129 lines), all 20 function declarations, all 3 enums and all 11 synthesized
constants are byte-identical between the two files. The underlying JSON differs only by two added
`baseType` fields. No regression of any kind was found.

Residual inaccuracies exist in `new`, but every one of them except the `distinct` loss is also
present in `old` (they live in the unchanged function/enum region), so they are pre-existing
renderer behaviour rather than spec-v2 fallout.

## 2. Change inventory

Mechanical totals (`diff -u old new`, whole-file): 2 hunks, 7 lines added, 2 lines removed, net +5
(588 → 593). Confirms `OLD_AND_NEW_DIFFS/etl_diff.md`.

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 | −2 |
| `type` declarations (top-level, rendered) | 1 (`type Customer` inside README code block) | 3 | +2 |
| `enum` | 3 | 3 | 0 |
| `const` | 11 | 11 | 0 |
| `function` (top-level, `^function `) | 20 | 20 | 0 |
| `class` / `service` / `listener` / `annotation` | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |

Declarations added in `new` (set-diff of `^(function|type|enum|const|class) ` lines, sorted):

- `type Error error;` (+ doc `# Represents ETL module related errors.`)
- `type CategoryRanges [float, float[], float];` (+ 4-line doc)

Declarations removed in `new`: **none** (set-diff empty in that direction).

JSON delta (`diff` of pretty-printed old vs new JSON) — 2 changes only:

```
127c127,128        "type": "Error"        →  "type": "Error", "baseType": "error"
178c179,180        "type": "Other"        →  "type": "Other", "baseType": "[float, float[], float]"
```

Note the JSON `type` discriminator is unchanged (`Error` / `Other`); spec v2 only adds `baseType`,
which is what lets the renderer stop degrading to a placeholder.

## 3. Correctness against library source

Bala default module `modules/etl/` (12 `.bal` files) is the authoritative source; it matches the
v0.8.0 clone.

Both new declarations are correct in substance:

- `Error` — `modules/etl/errors.bal:18`: `public type Error distinct error;`, preceded by the doc
  `# Represents ETL module related errors.` (line 17). `new` renders the doc verbatim and the
  definition as `type Error error;` — correct base type, **`distinct` dropped** (see §5).
- `CategoryRanges` — `modules/etl/types.bal:57`: `public type CategoryRanges [float, float[], float];`
  with the 4-line doc at lines 52–56. `new` reproduces both the tuple type and the doc exactly.

The unchanged parts were also checked against source:

- All 20 `public function` declarations in the bala (`grep -h '^public function' modules/etl/*.bal | wc -l`
  → 20) appear in both renders (`grep -c '^function '` → 20 / 20). Names and order of parameters
  match, e.g. `sortData(record {}[] dataset, string fieldName, SortDirection direction = ASCENDING, ...)`
  (`cleaning.bal:176`) and `maskSensitiveData(..., string:Char maskingCharacter = "X", ...)`
  (`security.bal:82`) — the `ASCENDING` and `"X"` defaults are preserved.
- Enums `Operation` (`types.bal:25`), `SortDirection` (`types.bal:38`), `Model` (`types.bal:47`) are
  present with the full member sets.
- README: render lines 8–136 are identical to `docs/README.md` lines 1–128 (`diff` → only one
  trailing blank line extra). Nothing truncated.
- `returns returnType[]|Error` / `returnType[][]|Error` / `returnType|Error` return shapes match the
  source per-function.

## 4. Regressions

**None found.**

What was checked to conclude that:
- Full `diff -u old new`: only the 2 additive hunks quoted in §2; no removal hunk exists.
- Set-diff of all top-level declaration lines (`function|type|enum|const|class`) in both directions:
  only the 2 additions, zero removals.
- Section markers: 4 in both; README block identical (lines 1–137 unchanged in the diff).
- Function section (render lines 197–593) untouched — no parameter, default, return type, or doc
  line changed.
- No malformed syntax introduced: `type Error error;` and `type CategoryRanges [float, float[], float];`
  are both syntactically valid Ballerina.
- No version/module-qualified type refs in either side (0 / 0), so nothing lost there either.

## 5. Issues in `new` (independent of `old`)

1. **`distinct` lost on `Error`** (new only, since `old` had no definition at all).
   Source `errors.bal:18` is `public type Error distinct error;`; `new` emits `type Error error;`.
   An LLM reading the render cannot tell this is a distinct error type, so generated code that
   defines its own `distinct error` subtype relationship or relies on `error` interchangeability
   could be subtly wrong. Still strictly better than `old`'s `// Unknown type: Error`.
2. **`typedesc<...>` inferred-default parameters are mangled** (present identically in `old`).
   Source: `typedesc<record {}> returnType = <>`. Both renders emit
   `record {|anydata...;|} returnType = record {|anydata...;|}` — the `typedesc<>` wrapper is gone
   and the inferred-type default `<>` is replaced by a record-type-descriptor used as a value
   expression, which is not valid as written. Affects all 20 functions.
3. **Enum associated values are stripped and re-emitted as invented module-level constants**
   (present identically in `old`). Source `Model { GPT_4_TURBO = "gpt-4-turbo", ... }` renders as
   `enum Model { GPT_4O_MINI, GPT_4O, GPT_4_TURBO }` plus 11 top-level
   `const string GPT_4O = "gpt-4o";` style declarations (render lines 141–161). `ballerina/etl`
   exports **no** public constants (`grep '^public const'` → 0 matches), so these 11 symbols do not
   exist in the library and could be cited by an LLM as `etl:GPT_4O` constants.
4. **Enum member documentation dropped**, leaving a dangling `# ` line (render lines 176–177,
   187–188): the `# + GREATER_THAN - Checks if ...` lines from `types.bal:19–24` and `35–37` are not
   rendered. Present identically in `old`.

Cosmetic / conventional, not counted above: `public` is omitted on every declaration in both
renders (uniform renderer convention), and enum members are emitted in reverse source order.

## 6. Coverage gaps vs. the library

**None.** `package.json` `"export": ["etl"]` and Central metadata list exactly one module (`etl`),
so there is no submodule API at all — the shared `getDefaultModule()` limitation is a non-issue here.

Full public surface of `modules/etl/` (`grep -rE '^public (function|type|enum|class|const|annotation|listener)'`):
20 functions, `type Error`, `type CategoryRanges`, `enum Operation`, `enum SortDirection`,
`enum Model` = 25 symbols. All 25 appear in `new` (23 of 25 in `old`; `Error` and `CategoryRanges`
were placeholders there).

Non-public and therefore correctly absent: `type ModelConfig` and `configurable ModelConfig modelConfig`
(`init.bal:19–29`), `OpenAiClient`, `init()`, `setModule()` — all module-private.

## 7. Compiler plugin

`has_plugin: false` is confirmed: the bala root contains only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`, `platform/` — no `compiler-plugin/` directory and no
`compiler-plugin.json`. The clone's `ballerina/Ballerina.toml` has no `[[tool.*]]`/`compilerPlugin`
entry (`grep 'compiler-plugin\|compilerPlugin'` → no match). The only native artifact is
`platform/java21/etl-native-0.8.0.jar`, which backs the `@java:Method` externals, not a plugin.
Nothing plugin-implied is missing from the render.

## 8. Other considerations

- **Pre-1.0 (`0.8.0`)**, `pullCount` 29, `ballerinaVersion` 2201.12.3, `deprecated: null` per Central.
  API is not yet stable; renders will need refreshing on each minor bump.
- **Runtime configuration is invisible to the render.** Every semantic API (`categorizeSemantic`,
  `extractFromText`, `groupApproximateDuplicates`, ...) requires `modelConfig.openAiToken` via a
  *private* `configurable` (`init.bal:25`). Because it is not public, neither render mentions it, so
  an LLM has no way to learn from the render that a `Config.toml` with
  `[ballerina.etl.modelConfig]` is mandatory. The README block does not cover it either
  (checked: no `Config.toml` / `openAiToken` occurrence in the rendered README). This is a
  documentation/coverage limitation of the library + pipeline, not a regression.
- **Size**: 27,895 → 28,152 bytes (+0.9%); token impact negligible. The 11 synthesized constants
  cost ~11 lines of context for symbols that do not exist.
- Doc quality is otherwise good: every function carries a runnable ` ```ballerina ` example and full
  `+ param - ...` docs, all preserved.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v0.8.0 .../module-ballerina-etl` → `git log --oneline -1`; `git describe --tags` | `cba24c3` "[Gradle Release Plugin] - pre tag commit: 'v0.8.0'"; `v0.8.0` |
| `wc -l etl/old/...bal.txt etl/new/...bal.txt` | 588 / 593 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- ' ` old / new | 4 markers each (README 7/137, Types 139, Functions 192 vs 197) |
| `diff -u old new` | 2 hunks, +7/−2, both in Types section |
| `diff <(grep -E '^(function\|type\|enum\|const\|class) ' old\|sort) <(... new\|sort)` | only `+type CategoryRanges`, `+type Error` |
| `diff <(json.tool old.json) <(json.tool new.json)` | 2 changes, both adding `baseType` (`error`, `[float, float[], float]`) |
| `grep -c '^function ' old new` | 20 / 20 |
| `grep -rh '^public function' bala/modules/etl/*.bal \| wc -l` | 20 |
| `grep -rE '^public (function\|type\|enum\|class\|const\|annotation)' bala/modules/etl/*.bal` | 20 functions + `Error`, `CategoryRanges`, `Operation`, `SortDirection`, `Model` = 25 |
| `bala/modules/etl/errors.bal:17–18` | `# Represents ETL module related errors.` / `public type Error distinct error;` |
| `bala/modules/etl/types.bal:52–57` | 4-line doc + `public type CategoryRanges [float, float[], float];` |
| `bala/modules/etl/types.bal:25,38,47` | `public enum Operation` / `SortDirection` / `Model`, with `= "..."` values |
| `bala/modules/etl/init.bal:19–29` | private `type ModelConfig` + `configurable ModelConfig modelConfig` |
| `cat bala/package.json` | `"export": ["etl"]`, `ballerina_version 2201.12.3`, `platform java21`, single native jar |
| `ls bala/` | no `compiler-plugin/` directory |
| `grep 'compiler-plugin\|compilerPlugin' src/ballerina/Ballerina.toml` | no match |
| `diff <(sed -n '8,136p' new) <(sed -n '1,129p' bala/docs/README.md)` | identical except one trailing blank line |
| `curl api.central.ballerina.io/.../ballerina/etl/0.8.0` | 1 module (`etl`), `deprecated: null`, pullCount 29 |
| `ls -R bala/modules` | 12 `.bal` files, single module `etl` |

## 10. Caveats and unverified items

- The renders were not recompiled or re-executed; the pipeline output files as committed were taken
  as given. Claims about what the extractor "saw" rest on the bala contents plus the committed JSON.
- The bala was fetched from Central for this review (`bala_source: fetched from Central`) rather than
  taken from the distribution used for the renders. Its `package.json` records
  `ballerina_version 2201.12.3` while the render pipeline runs on distribution 2201.13.4; the
  published module sources are version-stamped 0.8.0 and matched the v0.8.0 git tag, so this is
  considered equivalent, but it is not byte-proof that the render pipeline read this exact file set.
- Whether the invented `const string GPT_4O = "gpt-4o";` style declarations are intentional
  renderer design (enum-value surfacing) or a defect was not determined — no renderer source was
  consulted. Reported as an accuracy observation, and it is unchanged between `old` and `new`.
- `distinct` handling in spec v2 for other error types was not surveyed beyond this library.

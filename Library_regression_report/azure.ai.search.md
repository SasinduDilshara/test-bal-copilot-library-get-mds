# ballerinax/azure.ai.search 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/azure.ai.search` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-azure.ai.search |
| Tag reviewed | `v1.0.2` (commit `b3d71ae7611b70bf01734a1c71485f3fec9e6808`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/azure.ai.search/1.0.2` |
| Old render | `1856` lines |
| New render | `1859` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module OpenAPI-generated connector: one default module (`azure.ai.search`), 156 public
types, 1 public client class with `init` + 31 remote functions. No compiler plugin.
Upstream `v1.0.2` sources are byte-identical to the bala (`client.bal`, `types.bal`, `utils.bal`
all `diff`-identical), so the bala and GitHub agree.

`new` differs from `old` in exactly four ways, all strictly better:

1. Two degraded `// Unknown type:` placeholders (`CharFilterName`, `VectorEncodingFormat`) are
   replaced by their real, correct definitions.
2. All 15 version-qualified type references `ballerina/lang.int:0.0.0:Signed32` become `int:Signed32`.
3. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` is now emitted.
4. A bogus synthetic parameter `anydata Additional Values` is dropped from all 31 remote-function
   signatures (it was not a real parameter and its name contains a space, so it could never compile).

No declaration, parameter, default, return type, doc line or README content is lost. Zero regressions.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 1856 | 1859 |
| File size (bytes) | 89486 | 88514 |
| `// --- ` section markers | 4 (`README`, `END README`, `Types`, `Client`) | 4 (identical) |
| `// Unknown type:` placeholders | 2 | 0 |
| `type` declarations rendered | 154 | 156 |
| Client classes | 1 | 1 |
| `function init` | 1 | 1 |
| `remote function` declarations | 31 | 31 |
| `enum` / `const` / `annotation` / `service` / `listener` declarations | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 15 | 0 |
| `int:Signed32` refs | 0 | 15 |
| `@display` annotations | 0 | 1 |
| `anydata Additional Values` params | 31 | 0 |
| Doc-comment (`#`) lines | 619 | 621 |
| Record-field lines | 398 | 398 |
| `Special Agent Note` cross-package hints | 14 | 14 |
| Non-ASCII bytes | 0 | 0 |

**Declarations added (2)** — `diff` of the sorted `^type <Name>` sets:

```
> CharFilterName
> VectorEncodingFormat
```

**Declarations removed: 0.** The sorted `remote function <name>` sets are identical (31 = 31).

**Modified (by kind)**

| Kind | Count | Change |
|---|---|---|
| Record fields | 15 | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (records `AnalyzedTokenInfo`, `IndexingParameters`, `IndexerExecutionResult`, `SearchIndexerError`, `BinaryQuantizationCompression`(truncationDimension), `SearchField`(dimensions), `ServiceLimits` ×4) |
| Type definitions | 2 | placeholder → real union-of-string-literal definition |
| Record annotations | 1 | `ConnectionConfig` gains `@display {label: "Connection Config"}` |
| Client remote functions | 31 | synthetic `anydata Additional Values` parameter removed; everything else byte-identical |

The residual `diff` after masking those four classes of change is empty — verified by
`diff old new | grep -E '^[<>]' | grep -v 'anydata Additional Values' | grep -v 'Signed32'`,
which leaves only the `@display` line and the two type definitions/placeholders.

## 3. Correctness against library source

Every `new`-side addition/change was checked against the bala module source
(`.../1.0.2/any/modules/azure.ai.search/`), which is identical to the `v1.0.2` tag.

| New render | Source | Verdict |
|---|---|---|
| `# Defines the names of all character filters supported by the search engine.`<br>`type CharFilterName "html_strip";` | `types.bal:774-775` — `public type CharFilterName "html_strip";` with the identical doc line | exact match |
| `# The encoding format for interpreting vector field contents.`<br>`type VectorEncodingFormat "packedBit";` | `types.bal:835-836` — `public type VectorEncodingFormat "packedBit";` with the identical doc line | exact match |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:128` — `@display {label: "Connection Config"}` | exact match |
| `int:Signed32` in 15 field positions | `grep -c "int:Signed32" types.bal` → `15` | count and spelling match |
| Removal of `anydata Additional Values` | No such parameter exists. Source signatures use an included record param, e.g. `client.bal:41` `remote isolated function dataSourcesGet(string dataSourceName, DataSourcesGetHeaders headers = {}, *DataSourcesGetQueries queries)`. The JSON shows the old entry as `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}` — a synthetic surfacing of the open record's implicit `anydata` rest field | removal is correct |

Openness of the `*…Queries` records is still conveyed in `new`: those records are rendered as
open `record { … }` (no `|}`), so nothing the `Additional Values` pseudo-parameter carried is lost.

Public-symbol coverage (`comm` of the sorted source `^public type` set against the rendered
`^type` set): 156 source public types, 156 in `new`, **0 in source-not-in-render and 0 in
render-not-in-source**. The only other public symbol in the module is
`public isolated client class Client` (`client.bal:24`), present in both renders with all 31
remote functions and `init`.

README: the rendered `// --- README ---` block (lines 8-219) is byte-identical to
`.../1.0.2/any/docs/README.md` (211 lines) apart from one trailing blank line, and is identical
between `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Sorted declaration-name set diff for `type` (old ⊂ new, +2, −0) and for `remote function`
  (identical, 31 = 31).
- Field-line count unchanged (398 = 398); doc-comment lines increased (619 → 621, the two new
  type docs); no doc line removed anywhere in the unified diff.
- README block byte-identical between sides.
- Section markers identical (4 = 4, same names, same order).
- The complete unified diff (11 hunks, +51/−48) was read in full; every removed line has a
  corresponding improved replacement. The only lines removed without replacement are the 31
  occurrences of the non-compiling `anydata Additional Values` token and the 2 `// Unknown type:`
  placeholders.
- `Special Agent Note` cross-package annotations unchanged (14 = 14).
- No encoding change (0 non-ASCII bytes both sides).

## 5. Issues in `new` (independent of `old`)

All four below are **pre-existing and identical in `old`** — they are renderer/extractor
behaviours, not regressions, but they are inaccurate against the library source.

1. **Required query field rendered with a fake default.** All 31 remote functions render
   `string api\-version = ""`, but `api\-version` is a *required* field in every `…Queries`
   record (e.g. `types.bal:842-845`, `DataSourcesGetQueries record { string api\-version; }`).
   The render implies the caller may omit it; the real client requires it. Same for
   `string \$select = ""` on the six `…List` operations, where `\$select?` is optional and has no
   default. This is the most misleading item for an LLM consuming the render.
2. **Duplicated / non-compiling parameter list.** The included-record parameter is both flattened
   *and* re-emitted as a whole, e.g.
   `remote function dataSourcesGet(string dataSourceName, DataSourcesGetHeaders headers = {}, string api\-version = "", DataSourcesGetQueries queries)`.
   The real signature is `(string dataSourceName, DataSourcesGetHeaders headers = {}, *DataSourcesGetQueries queries)`.
   As written, a required-looking `queries` parameter follows defaulted parameters, which is not
   valid Ballerina, and `api\-version` is bound twice.
3. **Record field defaults dropped.** The source has 22 fields with default values
   (`grep -cE '^\s+[a-zA-Z].* = .*;$' types.bal` → 22); the Types section of the render contains 0
   (`sed -n '222,1729p' new | grep -cE '^\s+[a-zA-Z].* = .*;$'` → 0). They are re-expressed as
   optional markers, e.g. source `http:HttpVersion httpVersion = http:HTTP_2_0;` →
   render `http:HttpVersion httpVersion?;`; `decimal timeout = 30;` → `decimal timeout?;`;
   `int:Signed32? maxFailedItems = 0;` → `int:Signed32? maxFailedItems?;`.
4. **Closed record rendered as open.** `ConnectionConfig` is `record {|…|}` at `types.bal:129`
   but is rendered `record { … }`. (The two `record {|…|}` occurrences in the render are inline
   anonymous map types, not this one.)

Render conventions, not defects: `public` and `isolated` qualifiers are stripped from all type,
class and function declarations on both sides.

## 6. Coverage gaps vs. the library

**None.** The bala exports exactly one module (`package.json` `"export": ["azure.ai.search"]`,
`modules/` contains only `azure.ai.search`), so there is no submodule-only API and the
`getDefaultModule()`-only extraction limitation does not apply here.

- 156 of 156 public types present in `new` (0 missing).
- The single public class `Client` present, with `init` and all 31 remote functions.
- `utils.bal` contains no public symbols (`grep -nE '^(public|public isolated)' utils.bal` → no hits).
- `old` had 2 coverage gaps (`CharFilterName`, `VectorEncodingFormat` rendered as bare
  `// Unknown type:` lines with no value information); `new` has 0.

Note: both JSON files already contained 156 `typeDefs`. The `old` gap was purely a *renderer*
failure — `old` JSON has `{"type":"Other"}` with no `baseType`, `new` JSON adds
`"baseType":"\"html_strip\""` / `"baseType":"\"packedBit\""`. So spec v2 fixed this on the
extractor side as well.

## 7. Compiler plugin

The package has **no compiler plugin**. Verified two ways:

- `find <bala> -name "compiler-plugin*"` → no results (no `compiler-plugin/` directory, no
  `compiler-plugin.json`).
- The `v1.0.2` clone has no `*compiler-plugin*` path at depth ≤ 3; top-level directories are
  `ballerina/ build-config/ docs/ examples/ gradle/`, and `ballerina/` holds only
  `Ballerina.toml`, `Dependencies.toml`, `build.gradle`, `client.bal`, `types.bal`, `utils.bal`,
  `icon.png`, `README.md`, `tests/`.

Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- **Version/stability.** `1.0.2`, GA (≥1.0). No `@deprecated` markers in the source
  (`grep -n "@deprecated"` → no hits). `Ballerina.toml` pins distribution `2201.12.0`;
  `package.json` reports `graalvmCompatible: true`.
- **Size.** `new` is 3 lines longer but 972 bytes *smaller* (89486 → 88514) because the removed
  `anydata Additional Values, ` tokens outweigh the two added type definitions. Token cost is
  effectively flat with strictly more information.
- **Doc quality.** Doc comments are carried through verbatim from the OpenAPI-generated source and
  are dense; the README section reproduces the full 211-line published README including code
  samples, unchanged on both sides.
- **Escaping.** Identifiers with special characters are correctly escaped in both renders
  (`api\-version`, `\$select`, `x\-ms\-client\-request\-id`, `If\-Match`), matching the source.
- **Cross-package references.** 14 `// Special Agent Note: … FROM ballerina/http package` hints are
  emitted identically on both sides for the `http:*` types referenced by `ConnectionConfig`.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 1856 / 1859 |
| `ls -la old new` | old 89486 B / 258879 B JSON; new 88514 B / 251514 B JSON |
| `git ls-remote --tags <repo>` | tags `v1.0.0`, `v1.0.1`, `v1.0.2` — exact match `v1.0.2` |
| `git clone --depth 1 --branch v1.0.2 …` | HEAD `b3d71ae7611b70bf01734a1c71485f3fec9e6808`, tag `v1.0.2` |
| `diff ballerina/{client,types,utils}.bal <bala>/modules/azure.ai.search/` | all three IDENTICAL |
| `ls <bala>/any/modules` | only `azure.ai.search` (single module) |
| `cat <bala>/any/package.json` | `"export": ["azure.ai.search"]`, `ballerina_version 2201.12.0` |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep '^// Unknown type:' old` | `VectorEncodingFormat`, `CharFilterName` |
| `grep -n '^// --- ' both` | both: 7 README, 220 END README, 222 Types; Client at 1727 (old) / 1730 (new) |
| `grep -oE '^type \w+' \| sort \| diff` | +`CharFilterName`, +`VectorEncodingFormat`; nothing removed |
| `grep -oE '^public type \w+' types.bal \| sort` → `comm` vs new render | 156 source types; 0 missing, 0 invented |
| `grep -oE 'remote function \w+' \| sort \| diff` | identical, 31 each |
| `grep -nE 'remote (isolated )?function' <bala>/client.bal` | 31 remote functions (lines 41-441) |
| `grep -nE '^(public\|public isolated)' <bala>/*.bal` (non-type) | only `client.bal:24 public isolated client class Client` |
| `grep -c 'anydata Additional Values'` | old 31, new 0 |
| `grep -c 'ballerina/lang.int:0.0.0:'` old / regex for `mod:x.y.z:` new | 15 / 0 |
| `grep -c 'int:Signed32'` new render / `types.bal` | 15 / 15 |
| `grep -n '@display' <bala>/*.bal` | `types.bal:128 @display {label: "Connection Config"}` |
| `grep -c '@display'` renders | old 0, new 1 |
| `types.bal:774-775`, `types.bal:835-836` | `public type CharFilterName "html_strip";` / `public type VectorEncodingFormat "packedBit";` with matching docs |
| `diff <(sed -n '8,219p' new) <bala>/docs/README.md` | 1 diff line (trailing blank) |
| `diff <(sed -n '7,220p' old) <(sed -n '7,220p' new)` | no differences |
| `grep -c '^\s*#'` (doc lines) | old 619, new 621 |
| `grep -cE '^\s+[A-Za-z].*;$'` (field lines) | old 398, new 398 |
| `grep -cE '^\s+[a-zA-Z].* = .*;$' types.bal` vs render Types section | 22 vs 0 (both sides) |
| `grep -c 'record {\|' types.bal` / render | 2 named closed records in source; render's 2 hits are inline anonymous maps at lines 494, 1054 |
| `LC_ALL=C grep -c '[^ -~]'` | 0 both sides |
| `grep -c 'Special Agent Note'` | 14 both sides |
| JSON top-level keys + `typeDefs` length | same keys both; 156 typeDefs both; `clients` len 1 both; 32 client functions both |
| JSON `typeDefs[CharFilterName]` | old `{"type":"Other"}`; new `{"type":"Other","baseType":"\"html_strip\""}` |
| JSON `clients[0].functions[dataSourcesGet].parameters` | old has 5 params incl. `Additional Values` (`anydata`, "Capture key value pairs"); new has 4 |
| `find <bala> -name 'compiler-plugin*'` / clone `-iname '*compiler-plugin*'` | no results |
| `grep -n '@deprecated' <bala>/*.bal` | no hits |
| Full unified diff read | 11 hunks, +51/−48, all accounted for |

## 10. Caveats and unverified items

- The renders were **not compiled**. Ballerina-validity statements (e.g. that
  `anydata Additional Values` and the trailing non-defaulted `queries` parameter are not valid
  syntax) are from reading the language rules, not from running `bal build` on the render. The
  render is a documentation artefact and is not expected to compile as-is.
- Runtime behaviour of the connector against the live Azure AI Search API was not exercised; all
  correctness checks are source-to-render comparisons.
- The `old`/`new` `ballerina-vscode` commits (`eb5d81b3`, `412ba01e`) were taken from the brief and
  not independently re-verified; conclusions here rest only on the two render/JSON pairs and the
  library sources, which were verified directly.
- Rendered `http:*` types (`http:HttpVersion`, `http:ClientHttp1Settings`, …) were not chased into
  the `ballerina/http` package; only their spelling against `azure.ai.search`'s own `types.bal`
  was checked. Both sides render them identically, so this cannot hide a regression.

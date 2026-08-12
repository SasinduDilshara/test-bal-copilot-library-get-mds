# ballerinax/sap.s4hana.ce_salesorder_0001 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.ce_salesorder_0001` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `ce_salesorder_0001-v2.1.0` (module-scoped tag in monorepo; subdirectory `ballerina/ce_salesorder_0001`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.ce_salesorder_0001/2.1.0` |
| Old render | `2070` lines (101,843 bytes) |
| New render | `2419` lines (140,323 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Every one of the 434 added lines and 85
removed lines was accounted for and classified; nothing was dropped.

Three concrete improvements:

1. **47 `// Unknown type:` placeholders → 47 real type definitions.** All 47 are OData
   `…SelectOptions` / `…ExpandOptions` / `…OrderByOptions` string-literal-union array aliases. All
   47 bodies are **byte-identical** to the bala source (modulo the `public` keyword, which the
   renderer omits on both sides). Type coverage goes from 81/128 to **128/128** of the package's
   public types.
2. **347 `@constraint:String {maxLength: N}` annotations recovered**, plus 2 `@display`
   annotations. All 347 are attached to the exact same `(record, field)` pairs as the bala source —
   0 missing, 0 mismatched, 0 spurious.
3. **A malformed synthetic parameter was removed from 38 client method signatures.** `old` emitted
   `anydata Additional Values,` (an identifier containing a space — not valid Ballerina) inside 38
   `remote function` signatures. `new` drops it. This came from the open-record implicit rest field
   of the `…Queries` records being surfaced as a parameter in the JSON model.

No declaration, doc comment, README line, parameter, default value, or return type present in `old`
is absent from `new`.

## 2. Change inventory

Line accounting from the unified diff (`diff -u old new`): 434 added, 85 removed, net +349
(2070 → 2419). Every line classified:

| Added lines | Count |
|---|---|
| `type <X> …;` alias definitions (formerly `// Unknown type:`) | 47 |
| `@constraint:String {maxLength: N}` | 347 |
| `@display {…}` | 2 |
| `remote function …` (rewritten signatures) | 38 |
| **Total** | **434** |

| Removed lines | Count |
|---|---|
| `// Unknown type: <X>` | 47 |
| `remote function …` (old signatures, all re-emitted) | 38 |
| **Total** | **85** |

Declarations by kind:

| Kind | old | new | bala (default module) |
|---|---|---|---|
| `type` declarations | 81 | 128 | 128 public types |
| `// Unknown type:` placeholders | 47 | 0 | — |
| `client class` | 1 | 1 | 1 (`Client`) |
| `init` function | 1 | 1 | 1 |
| `remote function` | 62 | 62 | 62 |
| module-level `function` / `const` / `enum` / `annotation` / `service` / `listener` | 0 | 0 | 0 |
| `@constraint` annotations | 0 | 347 | 347 |
| `@display` annotations | 0 | 2 | 2 |
| Section markers (`// --- `) | 4 | 4 | — |
| README lines | 106 | 106 | 105 (+1 trailing blank) |

**Declarations removed in `new`: 0.** The remote-function name set is identical across
`old`, `new`, and the bala (`diff` of the three sorted name lists is empty). The type name set of
`new` equals the bala's public type name set exactly (both `comm -23` and `comm -13` are empty).

Underlying JSON mechanism: both JSONs contain 128 `typeDefs` (80 `Record`, 47 `Other`, 1 `Union`)
and 1 client. The 47 `Other` entries gained a `baseType` field in `new`
(e.g. `"baseType": "(\"*\"|\"_Item\"|\"_Partner\"|\"_PricingElement\"|\"_Text\")[]"`), which is what
lets the renderer emit a real definition. The `Additional Values` parameter object is present in
`old`'s client function parameter lists and absent from `new`'s.

## 3. Correctness against library source

Upstream at tag `ce_salesorder_0001-v2.1.0` and the bala are **identical**: `diff` of
`client.bal`, `types.bal`, `utils.bal` between `src/ballerina/ce_salesorder_0001/` and
`…/bala/…/modules/sap.s4hana.ce_salesorder_0001/` reports no differences. `Ballerina.toml` confirms
`version = "2.1.0"`. So GitHub and bala agree; no tie-breaking needed.

Verified (exhaustive, not spot-check, via scripted comparison):

- **All 47 newly-emitted type aliases** match the bala `types.bal` right-hand side exactly.
  Script result: `added simple type aliases: 47 / exact match vs bala: 47 / mismatch: 0`.
  Examples: `types.bal:678` `SalesOrderExpandOptions ("*"|"_Item"|"_Partner"|"_PricingElement"|"_Text")[]`
  → render line 897, identical; `types.bal:1182` `ItemTextOfSalesOrderItemSelectOptions` → identical;
  `types.bal:308` `SalesOrderOrderByOptions` → identical; `types.bal:1684`
  `ScheduleLineOfSalesOrderItemOrderByOptions` → identical.
- **All 347 `@constraint` annotations**: scripted `(record, field) → annotation` map extracted from
  both `types.bal` (347 entries) and the new render (347 entries) — `missing in new: 0`,
  `mismatched: 0`, `extra in new: 0`.
- **Both `@display` annotations**: `types.bal:270` `@display {label: "Connection Config"}` on
  `ConnectionConfig` → render line 1009 on `ConnectionConfig`; `types.bal:1938`
  `@display {label: "", kind: "password"}` on `ProxyConfig.password` → render line 1080 on
  `ProxyConfig.password`. Correct placement.
- **All 62 remote function names** match `client.bal` (`grep -c 'remote isolated function' = 62`).
- **Rewritten signatures**: e.g. `client.bal:341`
  `remote isolated function getSalesOrder(string salesOrder, map<string|string[]> headers = {}, *GetSalesOrderQueries queries) returns SalesOrder|error`.
  `GetSalesOrderQueries` (`types.bal:1175`) has fields `$expand?`, `$select?`. `new` renders
  `getSalesOrder(string salesOrder, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderQueries queries)`
  — the flattened fields are correctly typed; `old` had the same plus the bogus
  `anydata Additional Values,`.
- **Non-query methods unchanged and correct**: `client.bal:81`
  `createItemOfSalesOrder(string SalesOrder, CreateSalesOrderItem payload, map<string|string[]> headers = {}) returns SalesOrderItem|error`
  → render line 2174, matching.
- **80 record bodies**: extracted from both renders and the bala. All 80 bala records are present in
  `new`. Only 4 differ from the bala (`ConnectionConfig`, `ClientHttp1Settings`,
  `OAuth2RefreshTokenGrantConfig`, `ProxyConfig`) — and those 4 differ **identically in `old`**,
  i.e. pre-existing renderer behaviour, see §5.
- **README**: render lines 8–113 are byte-identical to `any/docs/README.md` (105 lines) plus one
  trailing blank. Unchanged between `old` and `new`.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Every removed line in the unified diff was enumerated and classified: 47 `// Unknown type:`
  placeholders (replaced by real definitions) and 38 `remote function` signature lines (all
  re-emitted in the same position with only the invalid `anydata Additional Values,` parameter
  removed). There is no third category.
- Remote-function name sets: `old` == `new` == bala (empty `diff`).
- Type name sets: `new` is a strict superset of `old` (47 additions, 0 deletions).
- Record field bodies for all 80 records: `old` vs `new` differ only by added `@constraint` /
  `@display` annotation lines; no field, type, optionality marker, or doc comment was dropped
  (23 records showed a body delta, and in every case the delta is annotation-only).
- README region: identical in both.
- Section markers: 4 in both, same order.
- `// Unknown type:` count: 47 → 0.
- No new malformed syntax: the only invalid-Ballerina construct in the pair
  (`anydata Additional Values`) exists in `old` and was **removed** by `new`.

## 5. Issues in `new` (independent of `old`)

Five inaccuracies exist in `new` when compared to the library source. Four of them are identical in
`old` (pre-existing renderer behaviour, listed here per the brief, not regressions); one is
introduced by the new annotation support.

1. **`@constraint:` prefix has no module attribution (new-only).** `types.bal:20` has
   `import ballerina/constraint;`. The render emits `@constraint:String {maxLength: 3}` etc. with no
   import line and no `// Special Agent Note: … FROM ballerina/constraint package` comment — even
   though the renderer *does* add such notes for type references (`http:KeepAlive`,
   `oauth2:ClientConfiguration`). A consumer cannot resolve the `constraint` prefix from the render
   alone. Cosmetic/low impact; the semantic content (max lengths) is correct.
2. **Included-record parameter rendered twice and in an invalid order (shared with `old`).** Source
   `…, *GetSalesOrderQueries queries)` is rendered as the flattened fields **plus** a trailing
   required `GetSalesOrderQueries queries`. The `*` inclusion marker is lost, and the trailing
   required parameter follows defaulted parameters, which does not compile. Affects all 38 query
   methods (`grep -c 'Queries queries)'` = 38 in both files).
3. **`public` / `isolated` / class modifiers dropped (shared).** `grep -c '^public '` is 0 in both
   renders; the bala has 128 `public type` and `public isolated client class Client`. The render
   emits `type X …` and `client class Client`.
4. **Closed records widened and field defaults dropped (shared).** `ProxyConfig` is
   `record {| string host = ""; int port = 0; string userName = ""; @display… string password = ""; |}`
   (`types.bal:1930-1940`); both renders emit an open `record {` with `string host?; int port?;
   string userName?; string password?;` — defaults lost, required-with-default turned into optional.
   Same for `ClientHttp1Settings` (`http:KeepAlive keepAlive = http:KEEPALIVE_AUTO` →
   `keepAlive?`) and `ConnectionConfig`.
5. **Type inclusion `*T;` flattened (shared).** `OAuth2RefreshTokenGrantConfig` is
   `record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl = "https://{host}:{port}"; |}`
   (`types.bal:1851-1855`); both renders inline the inherited fields and drop the `refreshUrl`
   default.

## 6. Coverage gaps vs. the library

**0 gaps for the default module.**

- `package.json` `export` = `["sap.s4hana.ce_salesorder_0001"]` only.
- Public symbols in the default module: 128 `public type` (all in `types.bal`) and 1
  `public isolated client class Client` (`client.bal:38`). `utils.bal` contains only non-public
  `isolated function`s. There are no public module-level functions, constants, enums, annotations,
  services, or listeners (`grep -oE '^public (type|const|function|class|isolated|enum|annotation)'`
  over `*.bal` yields exactly `128 public type` + `1 public isolated`).
- All 128 types and the client with all 62 remote methods + `init` are present in `new`.
- `old` is missing 47 of the 128 types (rendered as `// Unknown type:` with no body).

**Submodule note (shared gap, not a regression):** the bala contains
`modules/sap.s4hana.ce_salesorder_0001.mock`, declared in `package.json` as
`{"name": "sap.s4hana.ce_salesorder_0001.mock", "export": false}`. It is not exported and Ballerina
Central lists only `sap.s4hana.ce_salesorder_0001` as a module. Its absence from both renders is
correct, not a gap.

## 7. Compiler plugin

**None.** The bala has no `compiler-plugin/` directory and no `compiler-plugin.json`. The upstream
monorepo has no `compiler-plugin` / `*-compiler-plugin` directory anywhere (`find -maxdepth 3
-iname '*compiler-plugin*'` returns nothing). This is a pure OpenAPI-generated connector
(`client.bal` header: "AUTO-GENERATED FILE… by the Ballerina OpenAPI tool"). Nothing plugin-implied
is missing from the render.

The only annotations in play are `ballerina/constraint` (`@constraint:String`) and the built-in
`@display`, both of which `new` now surfaces — see §3 and §5.1.

## 8. Other considerations

- **Not deprecated.** Ballerina Central metadata for `ballerinax/sap.s4hana.ce_salesorder_0001/2.1.0`
  returns an empty `deprecateMessage`, `ballerinaVersion 2201.13.0`, `balaVersion 3.0.0`. Stable
  2.x version.
- **Size / token impact.** `new` is +349 lines (+16.9%) and +38,480 bytes (+37.8%). The byte growth
  is disproportionate because 347 of the 434 added lines are `@constraint` annotations. That is a
  real cost, but the payload is genuine API semantics (SAP field max-lengths) that an LLM needs to
  generate valid payloads, and it replaces 47 information-free placeholder lines.
- **Practical value of the fix.** The 47 recovered types are exactly the `$select` / `$expand` /
  `$orderby` OData option enums. In `old` an LLM saw `// Unknown type: SalesOrderSelectOptions` and
  had no way to know the legal values; in `new` it sees the full literal union. Together with the
  `@constraint` max-lengths this is a large accuracy gain for this connector specifically.
- **Docs quality.** The package README (105 lines) is fully carried into both renders. The client
  class doc comment starts with two empty `#` lines (an artifact of the source
  `client.bal:23-24`), reproduced faithfully on both sides.
- **`\$` escaping** of `$expand` / `$select` / `$orderby` / `$filter` / `$top` / `$skip` / `$count`
  is correct Ballerina quoted-identifier syntax and matches the source on both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old new` | 2070 / 2419 |
| 2 | `wc -c old new` | 101,843 / 140,323 |
| 3 | `grep -c '^// Unknown type:'` | old 47, new 0 |
| 4 | `grep -n '^// --- '` | 4 markers each; Client section at old:1803, new:2152 |
| 5 | `diff -u old new \| grep -c '^+[^+]' / '^-[^-]'` | 434 added / 85 removed |
| 6 | Classification of all 434 added lines | 347 `@constraint`, 47 `type` alias, 38 `remote function`, 2 `@display` (sums to 434) |
| 7 | Classification of all 85 removed lines | 47 `// Unknown type:`, 38 `remote function` (sums to 85) |
| 8 | `grep -c '^    remote function '` | old 62, new 62 |
| 9 | `grep -c 'remote isolated function ' client.bal` (bala) | 62 |
| 10 | `diff` of sorted remote-fn names old vs new | empty (SAME) |
| 11 | `diff` of sorted remote-fn names bala vs new | empty (SAME_AS_BALA) |
| 12 | `grep -c '^type '` | old 81, new 128 |
| 13 | `diff` of sorted type names old vs new | 47 additions, 0 deletions |
| 14 | `comm` bala public types (128) vs new render types (128) | both directions empty — exact set equality |
| 15 | Scripted RHS comparison of the 47 added aliases vs `types.bal` | 47/47 exact match, 0 mismatch |
| 16 | `grep -c '@constraint'` | old 0, new 347, bala `types.bal` 347 |
| 17 | Scripted `(record, field) → @constraint` map, bala vs new | 347 vs 347; missing 0, mismatched 0, extra 0 |
| 18 | `grep -n '@display'` | bala `types.bal:270,1938`; new render `1009,1080` — same targets |
| 19 | Scripted 80-record body comparison old vs new | 23 records differ; every delta is annotation-only |
| 20 | Scripted 80-record body comparison bala vs new | 4 differ: `ConnectionConfig`, `ClientHttp1Settings`, `OAuth2RefreshTokenGrantConfig`, `ProxyConfig` |
| 21 | Manual `awk` dump of those 4 records in old and new | bodies identical except the added `@display` on `ProxyConfig.password` → shared, not a regression |
| 22 | `grep -c 'Additional Values'` | old 38, new 0 |
| 23 | JSON: `getSalesOrder` parameter arrays old vs new | old has `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`; new does not |
| 24 | JSON `typeDefs` kind counts | old and new both `Record 80, Other 47, Union 1`; `Other` entries gained `baseType` in new |
| 25 | JSON top-level array sizes | both: typeDefs 128, clients 1, functions 0, services 0, annotations 0 |
| 26 | `git ls-remote --tags` filtered on `salesorder_0001` | `ce_salesorder_0001-v1.0.0`, `-v2.0.0`, `-v2.1.0` → used `ce_salesorder_0001-v2.1.0` |
| 27 | `diff` clone `ballerina/ce_salesorder_0001/{client,types,utils}.bal` vs bala module | CLIENT_SAME, TYPES_SAME, UTILS_SAME |
| 28 | `cat Ballerina.toml` (clone) | `version = "2.1.0"`, org `ballerinax` |
| 29 | `ls bala/any` + `find -iname '*compiler-plugin*'` | no compiler-plugin in bala or repo |
| 30 | `cat bala/any/package.json` | `export: ["sap.s4hana.ce_salesorder_0001"]`; `modules: [{mock, export:false}]` |
| 31 | `grep -oE '^public (type\|const\|function\|class\|isolated\|enum\|annotation)' bala/*.bal` | 128 `public type`, 1 `public isolated` — no other public symbols |
| 32 | `grep '^public\|^isolated function' utils.bal` | 6 non-public `isolated function`s only |
| 33 | `diff` render README region (lines 8–113) vs `bala/any/docs/README.md` | identical + 1 trailing blank |
| 34 | Central API `/2.0/registry/packages/ballerinax/sap.s4hana.ce_salesorder_0001/2.1.0` | `deprecateMessage` empty; modules `['sap.s4hana.ce_salesorder_0001']`; ballerinaVersion 2201.13.0 |
| 35 | `grep -c 'Queries queries)'` | 38 in both renders (shared duplicated-param issue) |
| 36 | `grep -n '^import'` in renders | only the self-import lines (5, 59) in both; no `ballerina/constraint` attribution |
| 37 | `grep -n 'function createItemOfSalesOrder'` bala vs new render | `client.bal:81` matches render line 2174 |
| 38 | `grep -n 'function getSalesOrder' client.bal` | line 341, `*GetSalesOrderQueries queries` confirmed |

## 10. Caveats and unverified items

- The renders were not compiled. Claims about syntactic validity (§5.2 — required parameter after
  defaulted parameters; §4 — `anydata Additional Values` containing a space) are based on reading
  the Ballerina grammar, not on running `bal build`. The renders are intentionally
  signature-only stubs and are not expected to compile as-is on either side.
- Token counts were not measured; §8 cites line and byte deltas only.
- The claim that the `Additional Values` pseudo-parameter originates from the implicit `anydata`
  rest field of the open `…Queries` records is an inference from the JSON
  (`"description": "Capture key value pairs"`, `"type": {"name": "anydata"}`) and from the records
  being declared `record {` rather than `record {| |}`. The extractor code itself was not read.
- I did not read the two `ballerina-vscode` source trees (`main` @ `eb5d81b3`,
  `L1_json_and_annotations_with_spec_v2` @ `412ba01e`); all conclusions about renderer behaviour are
  derived from the JSON and render artifacts, not from the extractor/renderer source.
- The `sap.s4hana.ce_salesorder_0001.mock` submodule was not analysed beyond confirming
  `export: false` in `package.json` and its absence from the Central module list.

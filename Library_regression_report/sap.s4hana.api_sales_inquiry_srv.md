# ballerinax/sap.s4hana.api_sales_inquiry_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sales_inquiry_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | default branch `main` @ `bc75bb7` — no `api_sales_inquiry_srv-v2.1.0` tag exists (only `-v1.0.0`, `-v2.0.0`). Branch source verified byte-identical to the 2.1.0 bala (see §9). |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sales_inquiry_srv/2.1.0` |
| Old render | `1131` lines (58,270 bytes) |
| New render | `1149` lines (83,938 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better. It eliminates all 39 `// Unknown type:` placeholders by emitting the real
type definitions (verified character-for-character against the bala), adds the 15 `@constraint:String`
and 2 `@display` annotations that `old` dropped entirely, and removes the 24 malformed
`anydata Additional Values` parameters that made every query-bearing client method non-parseable in
`old`. Nothing present and correct in `old` is missing from `new`: the only `old`-only lines are the
63 lines those two defects occupied (39 placeholders + 24 mangled remote-function signatures).

Both renders share a set of fidelity gaps against the library source (dropped `isolated`/`public`
qualifiers, included-record `*T queries` parameters rendered as duplicated non-compiling params,
closed records rendered as open, 11 record-field defaults dropped). None of these were introduced by
`new`.

## 2. Change inventory

`diff -u old new`: **26 hunks, 82 lines added, 64 lines removed**.

| Signal | old | new |
|---|---|---|
| Total lines | 1131 | 1149 |
| Bytes | 58,270 | 83,938 (+44%) |
| `// Unknown type:` placeholders | 39 | 0 |
| Rendered `type X ...` declarations | 56 | 95 |
| `remote function` declarations | 25 | 25 |
| `client class` | 1 | 1 |
| `@constraint:String` annotations | 0 | 15 |
| `@display` annotations | 0 | 2 |
| Version/module-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `Special Agent Note` cross-module hints | 14 | 14 |
| `anydata Additional Values` params | 24 | 0 |

**Declarations added (39, all `type`)** — every one replaces a `// Unknown type:` line, i.e. the
symbol was already listed in `old` but with no definition:

`A_SalesInquiryExpandOptions`, `A_SalesInquiryItemExpandOptions`, `A_SalesInquiryItemOrderByOptions`,
`A_SalesInquiryItemPartnerExpandOptions`, `A_SalesInquiryItemPartnerOrderByOptions`,
`A_SalesInquiryItemPartnerSelectOptions`, `A_SalesInquiryItemPrcgElmntExpandOptions`,
`A_SalesInquiryItemPrcgElmntOrderByOptions`, `A_SalesInquiryItemPrcgElmntSelectOptions`,
`A_SalesInquiryItemSelectOptions`, `A_SalesInquiryOrderByOptions`, `A_SalesInquiryPartnerExpandOptions`,
`A_SalesInquiryPartnerOrderByOptions`, `A_SalesInquiryPartnerSelectOptions`,
`A_SalesInquiryPrcgElmntExpandOptions`, `A_SalesInquiryPrcgElmntOrderByOptions`,
`A_SalesInquiryPrcgElmntSelectOptions`, `A_SalesInquirySelectOptions`,
`PricingElementOfA_SalesInquiryExpandOptions`, `PricingElementOfA_SalesInquiryItemExpandOptions`,
`PricingElementOfA_SalesInquiryItemOrderByOptions`, `PricingElementOfA_SalesInquiryItemSelectOptions`,
`PricingElementOfA_SalesInquiryOrderByOptions`, `PricingElementOfA_SalesInquirySelectOptions`,
`SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions`,
`SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions`,
`SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions`,
`SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions`,
`SalesInquiryOfA_SalesInquiryItemExpandOptions`, `SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions`,
`SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions`,
`SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions`,
`SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions`, `SalesInquiryOfA_SalesInquiryItemSelectOptions`,
`SalesInquiryOfA_SalesInquiryPartnerExpandOptions`, `SalesInquiryOfA_SalesInquiryPartnerSelectOptions`,
`SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions`, `SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions`,
`count`.

**Declarations removed: 0.** `diff` of sorted `^type` name sets and of `remote function` name sets is
empty in the `old`-only direction.

**Declarations modified (25):**
- 24 of the 25 `remote function` signatures lost the parameter `anydata Additional Values`
  (`performBatchOperation` has no `*Queries` param and is unchanged).
- 6 record types gained `@constraint:String` field annotations
  (`A_SalesInquiryItemPrcgElmnt` ×4, `A_SalesInquiry` ×1, `A_SalesInquiryItem` ×2,
  `A_SalesInquiryItemPartner` ×3, `A_SalesInquiryPartner` ×2, `A_SalesInquiryPrcgElmnt` ×3 = 15 total).
- `ConnectionConfig` gained `@display {label: "Connection Config"}`;
  `ProxyConfig.password` gained `@display {label: "", kind: "password"}`.

**Unchanged:** README block (lines 1–114 byte-identical, `diff` empty), all 56 record bodies' field
names/order/types, all 25 remote-function names and return types, the 14 `Special Agent Note` hints.

**JSON-level:** both JSONs carry the same 95 `typeDefs` (56 `Record`, 39 `Other`) and the same 26
client functions. The only schema additions in `new` are `typeDefs[].annotations`,
`typeDefs[].baseType`, and `typeDefs[].fields[].annotations`. No JSON path exists only in `old`.
So the placeholder fix is renderer-side (`renderTypeDef` now handles `Other` via `baseType`), and the
annotations are a genuine extractor addition.

## 3. Correctness against library source

Verification was exhaustive, not spot-check.

- **All 39 newly emitted one-line types match the bala exactly.** Script compared each
  `^type X <rhs>;` in `new` against `^public type X <rhs>;` in
  `.../modules/sap.s4hana.api_sales_inquiry_srv/types.bal`: 39 in source, 39 in render, **0 mismatches**.
  The only normalisation allowed was dropping redundant parentheses around a single-member array
  (source `types.bal:530 public type A_SalesInquiryPartnerExpandOptions ("to_SalesInquiry")[];` →
  render line 570 `type A_SalesInquiryPartnerExpandOptions "to_SalesInquiry"[];` — semantically identical,
  applies to 3 types).
- **`count`**: source `types.bal:268-269` — doc comment plus `public type count string;`. `new` line 526
  reproduces both the doc line and `type count string;` verbatim. `old` had only `// Unknown type: count`,
  which is a real problem because `CollectionOfA_SalesInquiry.__count` is typed `count` and `old` gave
  the consumer no definition for it.
- **All 56 record types match.** Script parsed record bodies from both source and `new` render:
  56 records on each side, identical name sets, identical field name *and order*, and identical field
  types after stripping the `// Special Agent Note` suffix — **0 field diffs**.
- **Annotations match the source exactly**: source `types.bal` contains 15 `@constraint:String` and 2
  `@display`; `new` contains 15 and 2, in the same positions. Checked individually:
  `types.bal:324 @constraint:String {maxLength: 10}` on `A_SalesInquiryItemPrcgElmnt.SalesInquiry`;
  `types.bal:202 @display {label: "Connection Config"}` on `ConnectionConfig`;
  `types.bal:806 @display {label: "", kind: "password"}` on `ProxyConfig.password`.
- **Client**: source `client.bal` declares `init` (line 32), 25 `remote isolated function`s (lines
  67–397). `new` renders 25 remote functions + `init`, all names and return types matching.
- **`anydata Additional Values` is correctly gone.** It is not a real parameter: the source signature is
  `client.bal:67 remote isolated function getA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, *GetA_SalesInquiryQueries queries)`.
  `Additional Values` is the Ballerina-docs artefact for the open record's implicit rest field. `old`
  rendered it literally — an identifier containing a space, which is not valid Ballerina and would
  break any LLM that copied the signature. `new` filters it. Confirmed at the JSON level: the parameter
  `{"name":"Additional Values","type":{"name":"anydata"}}` is present in `old.json` and absent in
  `new.json`, on 24 functions.

## 4. Regressions

**None found.**

Evidence for that conclusion:
- `comm -23 <(sort old|uniq) <(sort new|uniq)` yields exactly **63** lines, and every one of them is
  either a `// Unknown type:` placeholder (39) or an `old` remote-function signature carrying
  `anydata Additional Values` (24). Filtering those two categories leaves **0** `old`-only lines.
- No declaration name (type, remote function, class) is present in `old` and absent in `new`
  (`diff` of extracted name sets is empty in that direction).
- No `typeDef` lost a field: per-name field-set comparison over both JSONs returned an empty list.
- No `typeDef` description changed (`desc changed: []`).
- README block is byte-identical (lines 1–114).
- Cross-module hints unchanged at 14 on both sides.
- `new` introduces no `mod:x.y.z:Type` qualified refs (0 on both sides), so no new noise there.

## 5. Issues in `new` (independent of `old`)

All of the following are also present in `old` — they are pre-existing pipeline limitations, listed
because the brief asks for inaccuracies that exist in `new` regardless of `old`.

1. **Included-record parameters are rendered twice and non-compilably.** Source:
   `*GetA_SalesInquiryQueries queries`. Render (line 1052):
   `... A_SalesInquiryExpandOptions \$expand = [], A_SalesInquirySelectOptions \$select = [], GetA_SalesInquiryQueries queries`.
   The record's fields are flattened into params *and* the record itself is repeated as a bare param;
   the `*` is lost, and `queries` carries no default while following defaulted params, which Ballerina
   rejects. Affects all 24 query-bearing remote functions.
2. **Invented parameter defaults.** `\$expand = []`, `\$select = []`, `\$skip = 0`, `\$top = 0`,
   `\$filter = ""`, `\$inlinecount = "allpages"` appear in the render, but the source record fields are
   plain optionals with no defaults (`types.bal` `A_SalesInquiryExpandOptions \$expand?;`,
   `int \$skip?;`). The `"default"` values come from the Ballerina-docs JSON, so this is upstream of the
   extractor, but the render presents them as language-level defaults.
3. **Record-field defaults dropped.** Source has 11 fields with initialisers
   (`types.bal:207 http:HttpVersion httpVersion = http:HTTP_2_0;`, `:213 decimal timeout = 60;`,
   `:215 string forwarded = "disable";`, `:221 compression`, `:233 validation`, `:800/802/804/807`
   ProxyConfig, `:871/873` ClientHttp1Settings). All render as `field?;` with no value. An LLM reading
   the render cannot know the client's actual defaults.
4. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:203`), `ProxyConfig` (`:798`) and
   `ClientHttp1Settings` (`:869`) are `record {| |}` in source; the render emits `record { }` for all
   three (0 occurrences of `record {|` in `new`).
5. **`isolated` / `public` qualifiers dropped.** Source `client.bal:32 public isolated function init(...)`
   renders as `function init(...)` (line 1048); all 25 `remote isolated function`s render as
   `remote function`. All `public type`s render as `type`.
6. **No import hint for the annotation modules.** `new` emits `@constraint:String {...}` while the JSON
   knows `"module": "ballerina/constraint"`, but no `// Special Agent Note: ... FROM ballerina/constraint`
   line is produced (all 14 notes are `ballerina/http`). Cosmetic, but inconsistent with how `http:` refs
   are annotated.

## 6. Coverage gaps vs. the library

**None for the default module.** The bala's default module `sap.s4hana.api_sales_inquiry_srv` exports
95 public types (`grep -c '^public type' types.bal` = 95) and one client class; `new` renders 95 types
and the client. `comm` of the two sorted name sets is empty in both directions. `grep` for
`^public (const|enum|class|isolated function|function|annotation|listener|configurable)` across the
module's `.bal` files returns nothing else to render.

Submodule note: the bala contains a second module `sap.s4hana.api_sales_inquiry_srv.mock`, but
`package.json` marks it `"export": false` and Ballerina Central lists only the default module. So the
`getDefaultModule()`-only extraction loses nothing here — this is not even a shared gap.

## 7. Compiler plugin

The package ships **no compiler plugin**: the bala root contains only
`bala.json, dependency-graph.json, docs/, modules/, package.json` (no `compiler-plugin/`), and the
upstream package directory `ballerina/api_sales_inquiry_srv/` contains no plugin sources. Nothing the
plugin would imply is therefore missing from the render.

The only compile-time behaviour worth noting is `ballerina/constraint` 1.7.0 (a direct dependency per
`dependency-graph.json`), whose `@constraint:String {maxLength: n}` annotations drive runtime
validation. `old` hid these entirely; `new` surfaces all 15, which is the single most useful semantic
gain of this change for an LLM generating payloads.

## 8. Other considerations

- Not deprecated. Central `2.0/registry/packages/ballerinax/sap.s4hana.api_sales_inquiry_srv/2.1.0`
  returns `deprecateMessage: ""`, pullCount 22, single exported module.
- Stable major version (2.1.0), built with `ballerina_version 2201.13.0`, `graalvmCompatible: true`.
- **Size/token cost**: `new` is +44% bytes (58,270 → 83,938) for +18 lines. The growth is concentrated
  in ~30 very long single-line union types (the `*OrderByOptions` unions run to ~4,000 characters each).
  That is real, correct information, but it is by far the dominant token cost of this render and is
  highly repetitive across the ten `sap.s4hana.*` sibling packages.
- Doc quality is good: every record field and remote function carries a doc comment from the source, and
  the README (4,363 bytes) is embedded in full.
- The `\$`-escaped identifiers (`\$expand`, `\$select`, `\$skip`, `\$top`, `\$filter`, `\$inlinecount`,
  `\$orderby`) are rendered correctly on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 1131 / 1149 |
| `wc -c old new` | 58,270 / 83,938 |
| `grep -c '^// Unknown type:'` old/new | 39 / 0 |
| `grep -n '^// --- '` old/new | both: README@7, END README@114, Types@116, Client@1026 (old) / @1044 (new) |
| `diff -u old new` → `grep -c '^@@' / '^+' / '^-'` | 26 hunks, 82 added, 64 removed |
| `grep -c '^type '` old/new | 56 / 95 |
| `grep -c 'remote function '` old/new | 25 / 25 |
| `diff` of sorted `^type <name>` sets | 39 names added, 0 removed |
| `diff` of sorted `remote function <name>` sets | empty |
| `grep -c 'Additional Values'` old/new | 24 / 0 |
| `grep -oE '@[a-zA-Z:]+' \| uniq -c` old | (none) |
| `grep -oE '@[a-zA-Z:]+' \| uniq -c` new | 15 `@constraint:String`, 2 `@display` |
| same on bala `types.bal` | 15 `@constraint:String`, 2 `@display` — exact match |
| `comm -23 <(sort old\|uniq) <(sort new\|uniq)` | 63 lines; 0 remain after excluding `// Unknown type:` and `remote function` lines |
| `comm -13 …` (new-only) | 70 lines: 39 `type …`, 24 `remote function …`, 5 annotation lines, 1 `count` doc line, 1 `@display` type-level line |
| JSON: `len(typeDefs)` old/new | 95 / 95 (56 `Record`, 39 `Other` on both) |
| JSON: per-typeDef field-set loss in new | `[]` |
| JSON: per-typeDef description change | `[]` |
| JSON: schema paths present only in `old` | `[]` |
| JSON: schema paths present only in `new` | `typeDefs[].annotations{,[].name,[].value}`, `typeDefs[].baseType`, `typeDefs[].fields[].annotations{,[].module,[].name,[].value}` |
| JSON: client functions old/new | 26 / 26, identical name sets |
| JSON: total params removed across functions | 24 (all `Additional Values: anydata`) |
| JSON: `readme` field equality | `True` |
| Render README (lines 1–114) old vs new | `diff` empty |
| 39 one-line types in `new` vs `types.bal` | 39 vs 39, **0 mismatches** |
| 56 record bodies in `new` vs `types.bal` (names, order, types) | **0 diffs** |
| `grep -c '^public type' types.bal` vs `grep -c '^type ' new` | 95 vs 95; `comm` empty both directions |
| `git ls-remote --tags` on repo | no `api_sales_inquiry_srv-v2.1.0`; only `-v1.0.0`, `-v2.0.0` |
| `diff -q` GitHub `main` vs bala for `client.bal`, `types.bal`, `utils.bal` | identical (no output) |
| GitHub `ballerina/api_sales_inquiry_srv/Ballerina.toml:4` | `version = "2.1.0"` |
| bala `package.json` | `export: ["sap.s4hana.api_sales_inquiry_srv"]`; `modules: [{mock, export:false}]` |
| bala root listing | no `compiler-plugin/` |
| Central API `…/2.1.0` | not deprecated, pullCount 22, 1 module |
| `grep -c 'record {|'` source / new render | 3 / 0 |
| `grep -cE '^\s+[A-Za-z].* \w+ = .+;'` source `types.bal` | 11 field defaults, none rendered |
| `grep -c 'Special Agent Note'` old/new | 14 / 14 |

## 10. Caveats and unverified items

- **No module-scoped tag for 2.1.0 exists.** The repo only has `api_sales_inquiry_srv-v1.0.0` and
  `-v2.0.0`; I therefore cloned the default branch `main` (`bc75bb7`, `gradle.properties` at
  `2.1.1-SNAPSHOT`). This is mitigated, not merely assumed: `client.bal`, `types.bal` and `utils.bal` on
  `main` are byte-identical to the 2.1.0 bala (`diff -q` silent) and `Ballerina.toml` still reads
  `version = "2.1.0"`, so the branch is an exact match for the reviewed artefact. All correctness claims
  in §3 were nevertheless made against the **bala**, which is authoritative.
- I did not compile the render. Claims that specific rendered constructs (`anydata Additional Values`,
  the trailing `T queries` param after defaulted params) are non-compiling are from reading the
  Ballerina grammar, not from running `bal build`.
- I did not inspect the `.mock` submodule's contents beyond confirming it is `export: false`; it is out
  of scope for the default-module extraction on both sides.
- The origin of the `"default": "[]"` / `"allpages"` values in the docs JSON was traced to the JSON
  itself, but I did not read the Ballerina API-docs generator source to confirm *why* it emits them, so
  §5.2's attribution to the docs generator is inference rather than verified fact.

# ballerinax/hubspot.crm.commerce.orders 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.commerce.orders` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.commerce.orders |
| Tag reviewed | `v2.0.2` (commit `d32f1471`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.commerce.orders/2.0.2` |
| Old render | `785` lines |
| New render | `786` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders are near-identical: 15 diff hunks, +16 / −15 lines. Every difference is an
improvement produced by spec v2:

1. **11 version/module-qualified type refs normalised** — `ballerina/lang.int:0.0.0:Signed32` →
   `int:Signed32`, `record {|ballerinax/hubspot.crm.commerce.orders:2.0.2:ValueWithTimestamp[]...;|}`
   → `record {|ValueWithTimestamp[]...;|}`. The `new` form matches the library source verbatim; the
   `old` form was non-compiling Ballerina.
2. **`@display {label: "Connection Config"}` annotation now emitted** on `ConnectionConfig`
   (the +1 net line). Present in the source at `types.bal:254`, absent from `old`.
3. **The bogus `anydata Additional Values` pseudo-parameter removed** from 4 client resource
   signatures. It was an artefact of the open-record rest field of the `*…Queries` included-record
   parameter, and it contained a space in the identifier — i.e. syntactically invalid.

No declaration is added or removed on either side. Type coverage is 41/41 public types plus the
client class — complete. `// Unknown type:` count is 0 on both sides (this connector defines only
records, so the main spec-v2 headline improvement does not apply here).

Nothing is lost in `new`. Several rendering inaccuracies exist, but all of them are present
identically in `old` and are therefore not regressions.

## 2. Change inventory

Line counts (`wc -l`): old **785**, new **786**.

| Kind | old | new | delta |
|---|---|---|---|
| `^type ` declarations | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| `init` functions | 1 | 1 | 0 |
| `resource function` declarations | 11 | 11 | 0 |
| Module-level functions (JSON `functions`) | 0 | 0 | 0 |
| Services / annotations (JSON) | 0 / 0 | 0 / 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 11 | 0 | **−11** |
| README characters (JSON `readme`) | 8484 | 8484 | 0 |

Declaration name sets are byte-identical (`diff` of sorted `^type <Name>` lists → IDENTICAL;
JSON `typeDefs` name sets → `only old: {}`, `only new: {}`).

Field-level JSON diff over all 41 `typeDefs` yields exactly **13 differing leaf fields**:

* 12 × `.type.name` normalisations (7 × `int:Signed32`, 5 × inline `record {| … |}` refs) —
  affecting `GetCrmV3ObjectsOrdersQueries`, `AssociationSpec`, `ValueWithTimestamp`,
  `BatchResponseSimplePublicUpsertObjectWithErrors`, `BatchResponseSimplePublicObjectWithErrors`,
  `CollectionResponseWithTotalSimplePublicObjectForwardPaging`, `PublicObjectSearchRequest`,
  `SimplePublicObject`, `SimplePublicUpsertObject`, `SimplePublicObjectWithAssociations` (×2).
* 1 × annotation added: `ConnectionConfig.annotations[0] = {name: "display", value: '{label: "Connection Config"}'}`
  (`None` in `old`).

Client JSON: 12 functions on both sides, same accessors, same names, same order. The only
parameter-list difference is the removal of the `('Additional Values', {'name':'anydata'})` entry
from 4 functions (`post batch/read`, `get [orderId]`, `patch [orderId]`, `get .`).

## 3. Correctness against library source

Upstream clone at tag `v2.0.2` is byte-identical to the bala for all three module sources
(`diff -q` on `client.bal`, `types.bal`, `utils.bal` → no differences; `README.md` likewise). So
GitHub and the bala agree and either can be cited.

Verified for each `new`-side change:

| Change in `new` | Source evidence | Verdict |
|---|---|---|
| `int:Signed32 'limit?` in `GetCrmV3ObjectsOrdersQueries` | `types.bal:73` `int:Signed32 'limit = 10;` | type correct |
| `int:Signed32 associationTypeId` | `types.bal:380` | correct |
| `int:Signed32 updatedByUserId?` | `types.bal:193` | correct |
| `int:Signed32 numErrors?` (×2) | `types.bal:141`, `types.bal:344` | correct |
| `int:Signed32 total` | `types.bal:228` | correct |
| `int:Signed32 'limit?` in `PublicObjectSearchRequest` | `types.bal:316` | correct |
| `record {|ValueWithTimestamp[]...;|}` (×3) and `record {|CollectionResponseAssociatedId...;|}` | `types.bal` inline rest-field records; type name is module-local, so the unqualified form is the correct source form | correct |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:254` — exact string match | correct |
| `Additional Values` parameter dropped from 4 resource functions | `client.bal:47,67,100,170` declare `*PostCrmV3ObjectsOrdersBatchReadQueries queries`, `*GetCrmV3ObjectsOrdersOrderIdQueries queries`, `*PatchCrmV3ObjectsOrdersOrderIdQueries queries`, `*GetCrmV3ObjectsOrdersQueries queries` — there is no such parameter in any signature | removal correct |

Client surface, exhaustively checked against `client.bal`: `init` (`client.bal:31`, incl. the
`serviceUrl = "https://api.hubapi.com/crm/v3/objects/orders"` default) plus 11 resource functions at
`client.bal:47, 67, 84, 100, 118, 135, 152, 170, 186, 203, 220`. All 12 appear in both renders with
matching accessor, path, payload type and return type.

## 4. Regressions

**None found.**

What was checked to conclude this:

* Full `diff -u old new` (15 hunks) read line by line — every removed line is a version-qualified
  type ref or the invalid `anydata Additional Values` token; every added line is its corrected
  counterpart or the `@display` annotation.
* Sorted declaration-name sets of both renders are identical (no dropped `type`/`class`/function).
* JSON `typeDefs` compared field-by-field (recursive leaf flattening): 13 differing leaves, all
  listed in §2, all additive or corrective; **zero** fields present in `old` and absent/emptied in `new`.
* JSON `readme` strings are equal (`o['readme'] == n['readme']` → True, 8484 chars each) and equal to
  `docs/README.md` in the bala, so no README content was lost.
* `description` strings equal on both sides.
* Doc comments: no `#` doc line was removed by the diff; per-field docs on all changed fields are
  byte-identical across the hunks.
* Section markers: 4 on both sides, same order (`README`, `END README`, `Types`, `Client`).

## 5. Issues in `new` (independent of `old`)

All nine below are **pre-existing and identical in `old`** — they are renderer-wide behaviours, not
things `new` introduced. Listed because they misrepresent the library to an LLM consumer.

1. **Included-record params are both expanded and retained.** Source `client.bal:47` is
   `(… , *PostCrmV3ObjectsOrdersBatchReadQueries queries)`. The render emits
   `(… , boolean archived = false, PostCrmV3ObjectsOrdersBatchReadQueries queries)` — the record's
   fields are flattened into positional params *and* the record itself is kept, with the `*`
   dropped. Affects 4 resource functions (`batch/read`, `get [orderId]`, `patch [orderId]`, `get .`).
   A model copying this signature would write a call that does not compile.
2. **Required parameter after defaultable parameters.** In those same 4 signatures `queries` carries
   no default and follows `headers = {}` etc., which Ballerina does not permit.
3. **`resource function get (` has no resource path.** Source is `resource isolated function get .(…)`
   (`client.bal:170`); the render (line 773 new / 772 old) omits the `.`.
4. **Record field defaults dropped.** e.g. `ConnectionConfig` source has `decimal timeout = 30;`,
   `http:HttpVersion httpVersion = http:HTTP_2_0;`, `boolean validation = true;`
   (`types.bal:265, 259, 290`); the render shows `timeout?`, `httpVersion?`, `validation?`.
   Same for `GetCrmV3ObjectsOrdersQueries.'limit = 10` → `'limit?` (`types.bal:73`).
5. **Invented default `int:Signed32 limit = 0`** in the `get .` signature (render line 773) where the
   source default is `10`. Actively wrong, not merely missing.
6. **Invented `[]` / `""` defaults** for `associations`, `propertiesWithHistory`, `properties`,
   `after`, `idProperty` in the flattened signatures — these are optional fields with no default in
   the source query records.
7. **Closed records rendered as open.** `ConnectionConfig` and `ApiKeysConfig` are `record {| … |}`
   in source (`types.bal:255, 492`); the render emits `record { … }`.
8. **`public` / `isolated` / `client` modifiers dropped** — `public isolated client class Client`
   (`client.bal:23`) renders as `client class Client`; all 41 `public type` render as bare `type`;
   `resource isolated function` renders as `resource function`.
9. **Multi-line doc comment loses its `#` continuation prefix.** New line 605 (old line 604) reads
   `and absent fields are handled as \`nilable\` types. Enabled by default` with no leading `#`,
   breaking out of the doc comment into invalid top-level text inside a record body.

## 6. Coverage gaps vs. the library

**Zero gaps.**

* The bala has exactly one module: `modules/hubspot.crm.commerce.orders` (= the default module), so
  the known `getDefaultModule()`-only limitation cannot bite here. Confirmed against Central
  metadata: `modules` array has a single entry.
* Public symbols in that module: 41 `public type` + 1 `public isolated client class Client`.
  `comm` of the sorted source type list against the render type list returns empty in **both**
  directions — no missing type, no invented type.
* The only other module-level declaration is `enum EncodingStyle` at `utils.bal:37`, which is **not**
  `public` and is correctly excluded from both renders.
* `utils.bal` contains no public functions; JSON `functions` is `[]` on both sides, which is correct.

## 7. Compiler plugin

The repository at `v2.0.2` contains **no compiler plugin** (`find . -iname "*compiler-plugin*"`
returns nothing; the bala has no `compiler-plugin/` directory). `Ballerina.toml` declares no
`[[platform.*]]` or plugin sections. Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

* Version is stable (2.0.2, post-1.0) and **not deprecated** (`deprecated: None`, empty
  `deprecateMessage` from Central).
* Built with `ballerinaVersion 2201.12.2`; `Ballerina.toml` pins `distribution = "2201.12.0"`.
* Size impact is negligible: render 785 → 786 lines; JSON payload actually *shrank* 85,839 → 84,709
  bytes (−1.3%) because the long qualified type names were normalised. Slightly fewer tokens for
  strictly more information.
* Doc quality is good — every public type field except `ApiKeysConfig`'s two fields carries a doc
  comment, and `ApiKeysConfig` has none in the source either, so the render matches.
* The README block (193 rendered lines) is reproduced in full and identically on both sides,
  including the quickstart and the three example links.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 785 / 786 |
| 2 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 3 | `diff -u old new` | 15 hunks, +16 / −15 |
| 4 | `grep -cE '^type ' old new` | 41 / 41 |
| 5 | `grep -cE '^    resource function' old new` | 11 / 11 |
| 6 | `grep -n '^// --- ' new` | lines 7, 200, 202, 738 |
| 7 | `wc -c old/*.json new/*.json` | 85,839 / 84,709 |
| 8 | Python: JSON top-level keys + list lengths | `typeDefs` 41/41, `clients` 1/1, `functions` 0/0, `services` 0/0, `annotations` 0/0 |
| 9 | Python: recursive leaf diff of all 41 `typeDefs` | 13 differing leaves (12 type-name normalisations + 2 annotation fields on `ConnectionConfig`; counted as 13 leaves) |
| 10 | Python: `o['readme'] == n['readme']` | True (8484 chars); also equal to bala `docs/README.md` |
| 11 | Python: `o['description'] == n['description']` | True |
| 12 | Python: client function param dump, old vs new | same 12 functions; only delta = `('Additional Values','anydata')` removed from 4 |
| 13 | `git ls-remote --tags <repo>` | `v2.0.2` → `d32f1471` (peeled) |
| 14 | `git clone --depth 1 --branch v2.0.2` | OK |
| 15 | `diff -q src/ballerina/{client,types,utils}.bal` vs bala `modules/**` | identical (all 3) |
| 16 | `diff -q src/ballerina/README.md` vs bala `docs/README.md` | identical |
| 17 | `grep -n 'Signed32\|@display\|ConnectionConfig' types.bal` | lines 73, 141, 193, 228, 254, 255, 316, 344, 380 |
| 18 | `grep -n 'resource isolated function\|function init' client.bal` | 12 entries: 31, 47, 67, 84, 100, 118, 135, 152, 170, 186, 203, 220 |
| 19 | `grep -oE '^public type' types.bal \| sort` vs render type list, `comm` both ways | empty both directions (41 = 41) |
| 20 | `grep -nE '^(public\|enum\|const\|annotation\|listener\|service\|class)' *.bal` | only `client.bal:23` public class, `utils.bal:37` non-public enum |
| 21 | `ls -R <bala>` | single module `hubspot.crm.commerce.orders`; no `compiler-plugin/` |
| 22 | `find src -iname '*compiler-plugin*'` | no matches |
| 23 | `curl` Central `/2.0/registry/packages/ballerinax/hubspot.crm.commerce.orders/2.0.2` | `deprecated: None`, 1 module, `ballerinaVersion 2201.12.2` |
| 24 | `sed -n '254,300p' types.bal` vs render lines 566–607 | field names/order/docs match; defaults and `record {\|` closedness dropped in both renders |
| 25 | `grep -n '^and absent fields' old new` | old:604, new:605 — same defect both sides |
| 26 | `OLD_AND_NEW_DIFFS/hubspot.crm.commerce.orders_diff.md` claims (785/786, +16/−15, 15 hunks, 11→0 qualified refs, 0 decls added/removed) | all independently reproduced above |

## 10. Caveats and unverified items

* Compile-checking the render was not attempted — the renders are deliberately declaration-only
  stubs (no bodies), so they cannot compile as-is. Syntax claims in §5 (items 1, 2, 9) are based on
  reading the Ballerina grammar rules for parameter ordering, included-record params and doc
  comments, not on a compiler run.
* The `old`-side `mcp`-specific renderer patch mentioned in the brief is irrelevant here and was not
  exercised; not verified beyond confirming this library has no services.
* Whether the flattened-plus-retained `*Queries` parameter behaviour is intentional in the
  extractor was not investigated in the `ballerina-vscode` sources — it is reported purely as an
  observed mismatch against the library, and it is identical on both sides.
* Runtime/example correctness of the connector itself (e.g. that the HubSpot endpoints behave as
  documented) is out of scope and was not checked.

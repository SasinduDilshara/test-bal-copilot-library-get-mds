# ballerinax/hubspot.crm.commerce.taxes 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.commerce.taxes` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.commerce.taxes |
| Tag reviewed | `v2.0.2` (commit `9ea08aa454f78a8b5d3f5d73febf9f158b09e0eb`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.commerce.taxes/2.0.2` |
| Old render | `761` lines |
| New render | `762` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The `new` render differs from `old` in exactly 15 lines (15 removed, 16 added, 15 hunks). Every
change is a strict improvement:

- 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
  `ballerinax/hubspot.crm.commerce.taxes:2.0.2:ValueWithTimestamp`) are replaced with the plain,
  compilable forms that appear in the library source (`int:Signed32`, `ValueWithTimestamp`).
- The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — which exists in
  the published source (`types.bal:224`) and was silently dropped by `old` — is now emitted.
- The bogus pseudo-parameter `anydata Additional Values` (an identifier containing a space, i.e.
  non-parsable Ballerina) is removed from the 4 resource functions that take an included query
  record.

No declaration was added or removed on either side. Both renders cover 100% of the library's
public API (41 public types + the `Client` class with `init` and 11 resource functions). Zero
`// Unknown type:` placeholders on both sides — this connector has no error/object/`Other` type
defs, so the headline spec-v2 improvement does not apply here.

## 2. Change inventory

Counts from `diff -u` and from grep over both files.

| Metric | old | new |
|---|---|---|
| Lines | 761 | 762 |
| Section markers (`// --- `) | 4 | 4 |
| `// Unknown type:` | 0 | 0 |
| Version/module-qualified type refs | 11 | 0 |
| `@display` annotations | 0 | 1 |
| Doc-comment lines (`^\s*#`) | 233 | 233 |
| Top-level type declarations | 41 | 41 |
| Resource functions in `Client` | 11 | 11 |
| Client functions in JSON (`clients[0].functions`) | 12 | 12 |
| `record {\|` occurrences | 19 | 19 |

**Declarations added / removed: 0 / 0.** The extracted declaration sets are byte-identical:
`diff <(grep -oE '^(public )?(type|enum|const|class|annotation) [A-Za-z0-9_]+' old) <(… new)` →
no output ("DECLS IDENTICAL"), 41 lines each.

**Modified (11 type defs, from a structural JSON comparison):**

| Type def | Field | old type | new type |
|---|---|---|---|
| `AssociationSpec` | `associationTypeId` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `ValueWithTimestamp` | `updatedByUserId` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `BatchResponseSimplePublicObjectWithErrors` | `numErrors` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `BatchResponseSimplePublicUpsertObjectWithErrors` | `numErrors` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `CollectionResponseWithTotalSimplePublicObjectForwardPaging` | `total` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `GetCrmV3ObjectsTaxesGetPageQueries` | `'limit` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `PublicObjectSearchRequest` | `'limit` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `SimplePublicObject` | `propertiesWithHistory` | `record {\|ballerinax/hubspot.crm.commerce.taxes:2.0.2:ValueWithTimestamp[]...;\|}` | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicUpsertObject` | `propertiesWithHistory` | same qualified form | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `associations`, `propertiesWithHistory` | qualified forms | `record {\|CollectionResponseAssociatedId...;\|}`, `record {\|ValueWithTimestamp[]...;\|}` |
| `ConnectionConfig` | — (type-level) | no `annotations` key | `annotations: [{name: "display", value: '{label: "Connection Config"}'}]` |

**Modified (4 client resource functions):** the parameter `Additional Values`
(`{"name":"Additional Values","type":{"name":"anydata"},"optional":true,"description":"Capture key
value pairs"}`) is dropped from `post batch/read`, `get [taxId]`, `patch [taxId]`, and `get .`.
No other parameter, default, or return type changed in any of the 12 client functions
(verified by per-parameter JSON comparison).

The JSON `typeDefs` gained a new optional key `annotations` in `new` (absent in `old`); `name`,
`description`, `fields`, `type` are unchanged. `readme` (6516 chars), `description`, and `name`
are byte-identical between the two JSONs.

## 3. Correctness against library source

Upstream `v2.0.2` and the bala are byte-identical — `diff` of `ballerina/{client,types,utils}.bal`
from the tag against `bala/…/modules/hubspot.crm.commerce.taxes/{client,types,utils}.bal` reports
no differences for all three files. So the bala is a faithful stand-in for the tag.

Every `new`-side change is confirmed correct against the source:

- `int:Signed32` — `types.bal:117` (`numErrors`), `:169` (`updatedByUserId`), `:198` (`total`),
  `:296` (`'limit`), `:316` (`'limit`), `:344` (`numErrors`), `:380` (`associationTypeId`). The
  source uses the lang-library alias `int:Signed32`; `old`'s `ballerina/lang.int:0.0.0:Signed32`
  matches no textual form in the source and does not compile.
- `record {|ValueWithTimestamp[]...;|}` — `types.bal:214`, `:394`, `:454`; exact string match with
  the `new` render.
- `record {|CollectionResponseAssociatedId...;|}` — `types.bal:386`; exact string match.
- `@display {label: "Connection Config"}` — `types.bal:224`, immediately preceding
  `public type ConnectionConfig record {|` at `:225`. This is the only annotation anywhere in the
  module (grep for `@` over all three `.bal` files returns exactly this one line), and `new`
  renders it in the right place (new render line 510, directly above `type ConnectionConfig`).
- Removal of `anydata Additional Values`: the four affected functions take an *included record*
  parameter — `client.bal:47` `*PostCrmV3ObjectsTaxesBatchReadReadQueries queries`, `:67`
  `*GetCrmV3ObjectsTaxesTaxIdGetByIdQueries queries`, `:100`
  `*PatchCrmV3ObjectsTaxesTaxIdUpdateQueries queries`, `:170`
  `*GetCrmV3ObjectsTaxesGetPageQueries queries`. Those query records are *open* records
  (`record {` … `}` at `types.bal:262`-style declarations, e.g. `:274`, `:288`), so an implicit
  `anydata` rest field does exist — but `old` surfaced it as a *function parameter literally named
  `Additional Values`*, which is not a legal Ballerina identifier and cannot be written by a caller.
  The openness is still conveyed correctly in `new` via the open-record syntax of the rendered
  query type defs (`type GetCrmV3ObjectsTaxesGetPageQueries record {` at new:577,
  `type PostCrmV3ObjectsTaxesBatchReadReadQueries record {` at new:671). No information is lost.

Public-API coverage against the bala default module: 41 `public type` declarations in `types.bal`
and one `public isolated client class Client` (`client.bal:23`); nothing else is `public`
(`grep -nE '^public ' *.bal` excluding `public type` returns only the class). All 41 type names
appear in both renders — `comm` of the bala name set against the render name set is empty in both
directions. The three module-private declarations in `utils.bal` (`SimpleBasicType`, `Encoding`,
`EncodingStyle`) are correctly excluded from both renders.

The rendered README (new lines 8–175) is identical to `bala/any/docs/README.md` apart from one
trailing blank line (`diff` → `167a168 >`), and identical between `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Declaration-set diff `old` vs `new` (types/enums/consts/classes/annotations): identical, 41 each.
- Client function set and per-parameter JSON comparison across all 12 functions: the only delta is
  the removal of the `Additional Values` pseudo-parameter; every real parameter, its type, its
  `optional` flag, its `default`, and every return type are unchanged.
- Doc-comment line count identical (233/233); README block identical; `description` identical.
- Section markers identical (4/4, same order, `README`/`END README`/`Types`/`Client`).
- Nothing that was correct in `old` is missing, truncated, or less accurate in `new`; the reverse
  holds in 12 places (11 type refs + 1 annotation), plus 4 malformed parameter lists fixed.

## 5. Issues in `new` (independent of `old`)

All six items below are present **identically in `old`**, so none is a regression; they are
pre-existing pipeline limitations that still mislead a consumer of the `new` render.

1. **Included-record parameter is both expanded and duplicated.** Source `client.bal:170` is
   `resource isolated function get .(map<string|string[]> headers = {}, *GetCrmV3ObjectsTaxesGetPageQueries queries)`.
   The render (new:749) emits the record's fields as individual defaulted parameters *and* a
   trailing **required** `GetCrmV3ObjectsTaxesGetPageQueries queries` parameter. A required
   parameter after defaultable ones is not valid Ballerina, and the duplication invites an LLM to
   pass the same data twice. Same shape at new:718 (`post batch/read`), new:725 (`get [taxId]`),
   new:733 (`patch [taxId]`).
2. **Wrong default value.** `types.bal:296` declares `int:Signed32 'limit = 10;`. The render emits
   `int:Signed32 limit = 0` (new:749, old:748). A generated call relying on this would request
   0 results per page.
3. **Fabricated defaults for optional fields.** `associations`, `propertiesWithHistory`,
   `idProperty`, `properties`, `after` are declared *optional with no default*
   (`types.bal:276, 280, 282, 284, 290, 294, 298, 300`), but the render invents
   `= []` / `= ""` for them (new:725, new:749). Sending `idProperty=""` is not the same as omitting
   the query parameter.
4. **Record-field defaults dropped in the type defs.** `boolean archived = false`
   (`types.bal:278, 292`) and `int:Signed32 'limit = 10` (`types.bal:296`) render as
   `boolean archived?` and `int:Signed32 'limit?` (new:582, new:585). The defaults survive only in
   the (partly wrong) client parameter list.
5. **Closed records rendered as open.** `OAuth2RefreshTokenGrantConfig` (`types.bal:183`),
   `ConnectionConfig` (`:225`), and `ApiKeysConfig` (`:492`) are all `record {| … |}` in source but
   render as `type X record {` (new:511, new:555, and the `OAuth2RefreshTokenGrantConfig` block).
   This wrongly suggests arbitrary extra fields are accepted.
6. **Resource path `.` is dropped, producing unparsable syntax.** Source `client.bal:170`
   `get .(…)` and `:186` `post .(…)` render as `resource function get (…)` (new:749) and
   `resource function post (…)` (new:753).

Minor / cosmetic (not counted above): parameter-level doc comments (`# + headers - …`) are stripped,
leaving an empty `# ` line under every function description; `public`/`isolated` qualifiers are
dropped (`client class Client`, `function init`); `record {}` at `types.bal:25` renders as
`record {|anydata...;|}` (semantically equivalent). All identical in `old` and `new`.

## 6. Coverage gaps vs. the library

**Zero.** The package exports exactly one module (`package.json` `"export": ["hubspot.crm.commerce.taxes"]`;
Central metadata lists one module), which is the default module, so the known
`getDefaultModule()`-only limitation costs nothing here. Set comparison of the 41 `public type`
names in `bala/…/types.bal` against the 41 type names in the `new` render is empty in both
directions, and the `Client` class with all 11 resource functions plus `init` is present.

## 7. Compiler plugin

None. The upstream tag tree (70 paths) contains no `compiler-plugin` directory or
`CompilerPlugin.toml` (`grep -ci compiler-plugin tree.txt` → 0), and the bala contains no
`compiler-plugin/` directory (`bala/2.0.2/any/` holds only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`). Nothing plugin-derived is therefore expected in, or missing
from, the render.

## 8. Other considerations

- Not deprecated: Central `isDeprecated: false`, `deprecateMessage: ""`; `visibility: public`,
  `pullCount: 28`, built with `ballerinaVersion 2201.12.2`.
- Stable major version (`2.0.2`), Apache-2.0, `graalvmCompatible: true`.
- Fully auto-generated by the Ballerina OpenAPI tool (`client.bal:1-2`), so the render's quality is
  bounded by the generated source; doc strings are present on every type field and every function,
  and the render preserves them all.
- Size/token impact of the change is negligible: +1 line, and the removal of 11 long qualified type
  names actually shortens 11 lines. The `new` render is marginally cheaper and strictly more
  compilable.
- The `'limit` field keeps its quoted-identifier form in the type def but appears unquoted as
  `limit` in the client parameter list — inconsistent, in both renders.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 761, new 762 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | old 7,176,178,713; new 7,176,178,714 (same 4 markers) |
| `grep -cE '[a-z]+/[A-Za-z0-9_.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both | old 11, new 0 |
| `grep -c '@display'` both | old 0, new 1 (new:510) |
| `grep -c '^\s*#'` both | 233 / 233 |
| `diff` of extracted declaration sets | identical, 41 lines each |
| `grep -cE '^\s+resource function'` both | 11 / 11 |
| JSON structural compare (`typeDefs`, `clients`, `readme`, `description`) | readme equal (6516 chars), names equal, 11 typeDefs differ, 12/12 client functions, 4 differ |
| Per-parameter JSON diff of client functions | only `Additional Values` removed in 4 functions |
| `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2`; `v2.0.2` → `9ea08aa4…` |
| `gh api …/contents/ballerina/{client,types,utils}.bal?ref=v2.0.2` vs bala | `diff -q` → identical for all three |
| `gh api …/git/trees/v2.0.2?recursive=1` | 70 paths; no compiler-plugin; `ballerina/{client,types,utils}.bal` only |
| `grep -nE '^public ' bala/*.bal` | 41 `public type` + `public isolated client class Client` (client.bal:23) |
| `comm` bala type names vs render type names | empty both directions (41 vs 41) |
| `diff bala/docs/README.md` vs rendered README block | only `167a168 >` (trailing blank line) |
| `diff` old README block vs new README block | identical |
| `grep -n 'record {\|'` counts | 19 in each render; source has 3 top-level `record {\|` type decls at types.bal:183, 225, 492 rendered as open |
| `types.bal:296` | `int:Signed32 'limit = 10;` vs render `limit = 0` |
| `client.bal:47,67,100,170` | `*<X>Queries queries` included-record params |
| Central API `…/ballerinax/hubspot.crm.commerce.taxes/2.0.2` | `isDeprecated:false`, 1 module, ballerinaVersion 2201.12.2 |
| Bala `package.json` | version 2.0.2, `export: ["hubspot.crm.commerce.taxes"]`, graalvmCompatible true |

## 10. Caveats and unverified items

- `git clone` to github.com is blocked in this environment (connection timeout, sandboxed and
  unsandboxed). Upstream source was retrieved instead via the authenticated `gh api` contents/tree
  endpoints pinned to `ref=v2.0.2`, and verified byte-identical to the bala. The tag's *tests* and
  *examples* directories were listed but not read; they are not part of the rendered API surface.
- I did not compile either render. Claims that specific rendered lines are "not valid Ballerina"
  (`anydata Additional Values`, required parameter after defaultable ones, `resource function get (`)
  are based on the language rules and on the identifier containing a space, not on a compiler run.
- Neither renderer's source was inspected; the attribution of each delta to the spec-v2 change is
  inferred from the brief plus the observed output, not from reading the extractor code.
- `pullCount` and other Central fields were read once, at review time.

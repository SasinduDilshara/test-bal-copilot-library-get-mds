# ballerinax/sap.s4hana.api_sd_incoterms_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sd_incoterms_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_sd_incoterms_srv-v2.1.0` (commit `509822f`, module-scoped tag in monorepo) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sd_incoterms_srv/2.1.0` |
| Old render | `498` lines |
| New render | `507` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. All 15 `// Unknown type:` placeholders in `old`
are replaced with real, source-accurate type definitions in `new` (14 array-of-string-union option
types + `type count string`), and 8 annotations (`@constraint:String` ×6, `@display` ×2) that exist
in the published source are now surfaced. `new` also removes a malformed synthetic parameter
`anydata Additional Values` from all 10 client methods that carry an included-record `*…Queries`
parameter — that token contained a space in an identifier and could never compile.

Nothing present in `old` is lost in `new`. Set-difference of sorted lines: the only lines unique to
`old` are the 15 `// Unknown type:` lines and the 10 client-method lines that were rewritten (and
those 10 differ from `new` *only* by the removal of `, anydata Additional Values`). Declaration name
sets are identical on both sides (46 type names + 1 client class + 12 client functions), and both
match the bala's default module exactly — no coverage gap either way.

## 2. Change inventory

Line counts (`wc -l`): old `498`, new `507` (+9 net; 34 added / 25 removed, 14 hunks).

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 15 | 0 |
| `type <Name>` definitions rendered | 31 | 46 |
| Distinct type names referenced (defs + placeholders) | 46 | 46 |
| `@constraint:` annotations | 0 | 6 |
| `@display` annotations | 0 | 2 |
| `anydata Additional Values` occurrences | 10 | 0 |
| `// --- section ---` markers | 4 | 4 |
| Client classes / client functions | 1 / 12 | 1 / 12 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 |

**Types promoted from placeholder to real definition (15, all `type = "Other"` in JSON, all gained a
`baseType`):**
`A_IncotermsClassificationExpandOptions`, `A_IncotermsClassificationOrderByOptions`,
`A_IncotermsClassificationSelectOptions`, `A_IncotermsClassificationTextOrderByOptions`,
`A_IncotermsClassificationTextSelectOptions`, `A_IncotermsVersionExpandOptions`,
`A_IncotermsVersionOrderByOptions`, `A_IncotermsVersionSelectOptions`,
`A_IncotermsVersionTextOrderByOptions`, `A_IncotermsVersionTextSelectOptions`,
`IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions`,
`IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions`,
`IncotermsVersionTextOfA_IncotermsVersionOrderByOptions`,
`IncotermsVersionTextOfA_IncotermsVersionSelectOptions`, `count`.

**Records modified (6, annotations added, field sets unchanged):** `A_IncotermsClassification`,
`A_IncotermsClassificationText`, `A_IncotermsVersion`, `A_IncotermsVersionText`, `ConnectionConfig`,
`ProxyConfig`.

**Client functions modified (10):** all `get*`/`list*` remote methods — synthetic
`anydata Additional Values` parameter removed. `init` and `performBatchOperation` byte-identical.

**Declarations removed:** 0. **Enums / consts / annotations / services / listeners:** 0 on both sides
(JSON `annotations: []`, `services: []`, `functions: []` on both).

JSON-level: 46 typeDefs on both sides, 21 differ (15 gained `baseType`, 6 records gained annotation
data); 1 client with 12 functions on both, names identical; `name`, `description` and `readme`
byte-identical between the two JSONs.

## 3. Correctness against library source

Upstream at tag `api_sd_incoterms_srv-v2.1.0` is byte-identical to the bala for all three default-module
files (`diff` on `client.bal`, `types.bal`, `utils.bal` → identical), so source and bala agree.

- **All 15 promoted types verified verbatim** against `types.bal` (script comparison ignoring only
  parentheses/whitespace): 15 ok / 0 mismatch. Examples:
  `A_IncotermsClassificationSelectOptions` → `("IncotermsClassification"|"LocationIsMandatory"|"to_IncotermsClassificationText")[]`
  (types.bal:195); `A_IncotermsVersionOrderByOptions` → `("IncotermsVersion"|"IncotermsVersion desc")[]`
  (types.bal:124); `count` → `string` with the `$inlinecount` doc string (types.bal:217-218).
  `new` renders singleton unions without the redundant parentheses (`"to_IncotermsVersionText"[]` for
  types.bal:65 `("to_IncotermsVersionText")[]`) — semantically identical and valid Ballerina.
- **All 6 `@constraint:String` and both `@display` annotations match source exactly**: counts in
  `new` (6 / 2) equal counts in `types.bal` (6 / 2); spot-checked `A_IncotermsVersionText`
  (types.bal:220-226 → `maxLength: 4` on `IncotermsVersion`, `maxLength: 2` on `Language`),
  `A_IncotermsClassification` (types.bal:117 → `maxLength: 3`), `ConnectionConfig`
  (types.bal:135 `@display {label: "Connection Config"}`), `ProxyConfig.password`
  (types.bal:239 `@display {label: "", kind: "password"}`).
- **Record field sets exhaustively verified**: all 31 record types in `new`, field name + type pairs
  compared against `types.bal` → 0 missing records, 0 extra records, 0 field differences.
- **Client methods verified against `client.bal`**: 12 functions, names match `init` (client.bal:31)
  plus the 11 `remote isolated function`s (client.bal:65,80,94,109,123,135,147,159,172,185,195).
  Return types and the leading path/`headers` parameters match, e.g.
  `getA_IncotermsClassificationText(string IncotermsClassification, string Language, map<string|string[]> headers = {}, …) returns A_IncotermsClassificationTextWrapper|error`
  (client.bal:80) and `performBatchOperation(http:Request request, map<string|string[]> headers = {}) returns http:Response|error`
  (client.bal:195).
- **README preserved verbatim**: render lines 8-113 equal bala `docs/README.md` lines 1-105 (only a
  trailing blank line differs); identical between `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `comm -23 <(sort old) <(sort new)` → 25 lines unique to `old`: 15 `// Unknown type:` placeholders
  (each replaced by a real definition in `new`) and 10 client-method lines. `diff` of the
  `remote function` lines after deleting the literal `, anydata Additional Values` from `old`
  produced **no output**, proving those 10 lines are otherwise byte-identical.
- Declaration name sets (46 type names in each, derived from `type X` + `// Unknown type: X`) are
  identical: `diff` → "SAME NAME SET".
- Record field name/type sets, per record, identical in `old` and `new` and to source (section 3).
- Defaults/requiredness fidelity is *identical* on both sides: 11 record fields whose source default
  is not represented in the render, same 11 in `old` and in `new` (see section 5 item 1).
- README section: `diff` of render lines 8-113 old vs new → identical. JSON `readme` fields equal
  (4373 chars each).
- Section markers, client class name and description, and `init` signature unchanged.

## 5. Issues in `new` (independent of `old`)

7 items. Items 1-4, 6, 7 are present identically in `old` (shared renderer behaviour, not caused by
spec v2); item 5 is introduced by `new`.

1. **Record defaults dropped, defaulted fields shown as optional.** 11 fields whose source form is
   `T f = <default>` are rendered `T f?` with no default: `ConnectionConfig.httpVersion`
   (`http:HTTP_2_0`), `.timeout` (`60`), `.forwarded` (`"disable"`), `.compression`
   (`http:COMPRESSION_AUTO`), `.validation` (`true`); `ProxyConfig.host`/`.port`/`.userName`/
   `.password` (`""`,`0`,`""`,`""`); `ClientHttp1Settings.keepAlive` (`http:KEEPALIVE_AUTO`),
   `.chunking` (`http:CHUNKING_AUTO`). Verified programmatically: 11 in `old`, the same 11 in `new`.
2. **Closed records rendered as open.** `ConnectionConfig` (types.bal:136), `ProxyConfig`
   (types.bal:231) and `ClientHttp1Settings` (types.bal:309) are `record {| … |}` in source but
   `record { … }` in both renders — an LLM would believe extra fields are permitted.
3. **`isolated` and `public` qualifiers dropped.** `grep -c isolated` = 0 in both renders, while the
   client class and all 12 functions are `isolated` (`public isolated client class Client`,
   `remote isolated function …`). Render shows `client class Client` / `remote function …`.
4. **Client method signatures are not valid Ballerina.** The included-record parameter
   `*GetA_IncotermsClassificationQueries queries` is expanded into individual defaulted parameters
   *and* a trailing `GetA_IncotermsClassificationQueries queries` with no `?`/default, i.e. a
   required parameter after defaultable ones, with the query fields duplicated. In the JSON that
   parameter carries `"optional": true`, so the information loss is in `toSyntaxString`, not the
   extractor. Affects all 10 methods with a `*…Queries` parameter, on both sides.
5. **`@constraint:` prefix used without an import or provenance note (new only).** `new` emits
   `@constraint:String {maxLength: N}` 6 times, but the render's only `import` is
   `ballerinax/sap.s4hana.api_sd_incoterms_srv` (line 5). Cross-package *types* get an inline
   `// Special Agent Note: X FROM ballerina/http package` hint; annotations get none, so a consumer
   copying the record has no signal that `import ballerina/constraint;` is required (source
   `types.bal:20`). Cosmetic/low impact — the annotations themselves are accurate.
6. **Parameter-level doc comments dropped from the client section.** Source docs such as
   `# + IncotermsClassification - Incoterms (Part 1)` (client.bal:62) are absent; each method shows
   only its summary line followed by an empty `# `. The data exists in the JSON
   (`parameters[].description`), so this is a renderer omission. Identical in both sides.
7. **Package description truncated mid-sentence.** Header line 3 is
   `// [S/4HANA](…) is a robust enterprise resource planning (ERP) solution,` — the README's overview
   sentence is cut at its newline (README.md:3-4 continues "designed for large-scale enterprises by
   SAP SE."). Same in both JSONs (`description` fields equal), so shared.

## 6. Coverage gaps vs. the library

**0 gaps.** The bala's `package.json` exports exactly one module,
`sap.s4hana.api_sd_incoterms_srv`; `sap.s4hana.api_sd_incoterms_srv.mock` is listed with
`export: false` and Ballerina Central reports `modules = ['sap.s4hana.api_sd_incoterms_srv']`, so
there is no submodule public API to miss (the mock module is correctly absent from both renders).

Default-module public symbols: 46 `public type` declarations in `types.bal` + `public isolated
client class Client` in `client.bal`. `comm` against the render's declaration set:
0 source symbols missing from `new`, 0 symbols in `new` that do not exist in source. The client class
and all 12 of its functions are rendered.

`utils.bal` symbols (`SimpleBasicType`, `Encoding`, `EncodingStyle`, `defaultEncoding`,
`getEncodedUri`, `getPathForQueryParam`) are module-private (no `public` qualifier, verified at
utils.bal:22,25,36,40) and are correctly absent from both renders.

## 7. Compiler plugin

This package has **no compiler plugin**. The bala contains only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/` directory and no
`compiler-plugin.json`; the upstream module directory (`ballerina/api_sd_incoterms_srv/`) contains no
`compiler-plugin` sources either. Nothing plugin-derived is therefore expected in, or missing from,
the render.

## 8. Other considerations

- Version and identity are consistent everywhere: `Ballerina.toml` (upstream) `version = "2.1.0"`,
  bala path `2.1.0`, Central `version = 2.1.0`. Not deprecated (`deprecated: None`,
  `deprecateMessage: ""`), `visibility: public`, built with `ballerinaVersion 2201.13.0`.
- Stable 2.x version; no pre-1.0 instability caveat.
- Size/token impact of `new` is negligible: +9 lines (+1.8%), JSON 88,651 → 89,318 bytes (+0.75%).
  In exchange, 15 type definitions that were previously opaque to an LLM are now fully specified —
  and these are precisely the `$select`/`$orderby`/`$expand` enumerations a model needs to build a
  valid OData query, so the information gain is far larger than the byte cost.
- The library is a fully generated OpenAPI/OData connector (`// AUTO-GENERATED FILE`), which is why
  doc coverage is uniform and why the flattened `*…Queries` parameter pattern dominates the diff.
- `type count` shadows nothing in the render, but a lowercase type name (`count`) mirrored from the
  OData `__count` property is inherently confusing; that is the library's own choice, faithfully
  reproduced.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 498 / 507 |
| `grep -c '^// Unknown type:'` old / new | 15 / 0 |
| `grep -n '^// --- ' ` old / new | 4 markers each (README, END README, Types, Client) |
| `diff -u old new` | 14 hunks, +34 / −25 |
| `comm -23 <(sort old) <(sort new)` | 25 lines: 15 placeholders + 10 method lines |
| `comm -13 <(sort old) <(sort new)` | 34 lines |
| `diff <(sed 's/, anydata Additional Values//' old \| grep '    remote function') <(grep '    remote function' new)` | no output → only that token removed; 11 indented remote methods |
| `grep -c 'Additional Values'` old / new | 10 / 0 |
| Type-name set comparison (`type X` + `// Unknown type: X`, sorted) | 46 / 46, `diff` → SAME NAME SET |
| `grep -oE '^public type [A-Za-z_0-9]+' types.bal \| sort` vs new render set (`comm`) | 46 source types; 0 missing, 0 extra |
| Script: 15 promoted defs vs `types.bal` (parens/whitespace-insensitive) | ok 15, bad 0 |
| Script: 31 record types, field name+type sets vs `types.bal` | 0 missing, 0 extra, 0 field diffs |
| Script: source-defaulted fields not represented in render | 11 in `old`, same 11 in `new` |
| `grep -c '@constraint:'` old / new / `types.bal` | 0 / 6 / 6 |
| `grep -c '@display'` old / new / `types.bal` | 0 / 2 / 2 |
| `grep -c 'isolated'` old / new | 0 / 0 (source: 12 isolated functions + isolated class) |
| `grep -n '^import' new` | line 5 (module import), line 59 (inside README sample) |
| JSON: `len(typeDefs)`, `len(clients)`, `len(clients[0].functions)`, `annotations` | old 46/1/12/[] — new 46/1/12/[] |
| JSON: typeDefs differing old→new | 21 (15 `Other` gained `baseType`; 6 `Record` gained annotations) |
| JSON: `name`/`description`/`readme` equality old vs new | all equal (readme 4373 chars) |
| JSON `getA_IncotermsClassification` params | old 6 params incl. `Additional Values` (`anydata`, "Capture key value pairs"); new 5, otherwise identical; `queries` `optional: true` on both |
| `git ls-remote --tags` | `api_sd_incoterms_srv-v2.1.0` → `509822f0ba4e…` (exact match found) |
| `git log --oneline -1` in clone | `509822f [Gradle Release Plugin] - pre tag commit: 'api_sd_incoterms_srv-v2.1.0'` |
| `diff bala/modules/…/{client,types,utils}.bal` vs `src/ballerina/api_sd_incoterms_srv/` | all three IDENTICAL |
| `cat gradle.properties` | `api_sd_incoterms_srvVersion=2.1.0` (only non-SNAPSHOT module → tag is module-scoped) |
| `ls bala/any` | no `compiler-plugin/`; no plugin in upstream module dir |
| `package.json` `export` / `modules` | `['sap.s4hana.api_sd_incoterms_srv']` / mock with `export: false` |
| Central `…/packages/ballerinax/sap.s4hana.api_sd_incoterms_srv/2.1.0` | `deprecated: None`, `visibility: public`, `modules: ['sap.s4hana.api_sd_incoterms_srv']`, `ballerinaVersion 2201.13.0` |
| `wc -l bala/docs/README.md` + `diff` vs render lines 8-113 | 105 lines; identical except one trailing blank line |
| `grep -nE '^(public\|…)' utils.bal` | all utils symbols module-private (lines 22, 25, 36, 40) |

## 10. Caveats and unverified items

- **Compilability not mechanically tested.** I did not run `bal build` on either render. The claim in
  §5 item 4 (required parameter after defaultable parameters) is from the Ballerina parameter-order
  rule applied to the rendered text, not from a compiler run. Renders are also not intended to
  compile standalone (types are emitted without `public`, and `http:`/`constraint:` prefixes are used
  with no corresponding imports), so a compiler run would produce noise unrelated to this review.
- **`old`/`new` provenance taken from the brief.** I did not re-verify that the two renders came from
  commits `eb5d81b3` and `412ba01e`, nor did I inspect `renderTypeDef` / `toSyntaxString` sources; my
  conclusions rest entirely on the two render files, the two JSONs, the bala, and upstream at the tag.
- **Semantics of the `*…Queries` flattening** (whether emitting both the flattened query parameters
  and the record parameter is intended renderer behaviour) is unverified — I report it as a shared
  fidelity issue, identical on both sides, not as a spec-v2 change.
- Everything else asserted above comes from a command whose output is recorded in §9.

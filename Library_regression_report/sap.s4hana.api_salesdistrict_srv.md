# ballerinax/sap.s4hana.api_salesdistrict_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_salesdistrict_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_salesdistrict_srv-v2.1.0` (commit `d8641505e88e1dc63a257d95a68f596a24f3f01a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_salesdistrict_srv/2.1.0` |
| Old render | `360` lines |
| New render | `366` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small auto-generated (Ballerina OpenAPI tool) SAP S/4HANA OData connector: 27 public types + 1 client
class with 6 remote methods and `init`, all in the single default module. The bala's `client.bal`,
`types.bal` and `utils.bal` are byte-identical to the upstream tag (`diff -q` → identical), so
GitHub and the bala agree.

`new` is strictly better than `old` on every axis measured:

- All 9 `// Unknown type:` placeholders in `old` become real, correct type definitions in `new`
  (`grep -c '^// Unknown type:'`: old 9, new 0).
- `new` adds 4 annotations that `old` dropped entirely (`@constraint:String {maxLength: 6}` ×2,
  `@constraint:String {maxLength: 2}`, `@display {label: "Connection Config"}`,
  `@display {label: "", kind: "password"}`) — all verified present in the library source.
- `new` removes the malformed synthetic parameter `anydata Additional Values` from all 6 remote
  method signatures. That identifier contains a space and does not exist in the library; it was the
  extractor's rendering of the open-record rest field of the `*…Queries` included-record parameter.

Nothing is removed, truncated or made less accurate. Zero declarations lost. Zero coverage gaps
against the default module.

## 2. Change inventory

`diff -u old new` → **21 lines added, 15 lines removed, 10 hunks** (matches the precomputed diff).

Declaration counts (`grep -c '^type '`): old 18, new 27. Client class: 1 in both.
JSON: both sides have `typeDefs` 27, `clients` 1, `functions` 0, `services` 0, `annotations` 0.
Type-def **name sets are identical** between the two JSONs (verified by set comparison) — the 9 new
`type` lines correspond exactly to the 9 `// Unknown type:` placeholders in `old`.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations rendered | 18 | 27 | +9 |
| `// Unknown type:` placeholders | 9 | 0 | −9 |
| Client classes / remote methods / `init` | 1 / 6 / 1 | 1 / 6 / 1 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 | 0 |

Added (all previously `// Unknown type:`), all of Ballerina kind `Other` (array-of-singleton
aliases and a string alias) which `main`'s `renderTypeDef` could not emit:

| New declaration in `new` | Source |
|---|---|
| `type A_SalesDistrictTextExpandOptions "to_SalesDistrict"[];` | types.bal:23 |
| `type A_SalesDistrictOrderByOptions ("SalesDistrict"\|"SalesDistrict desc")[];` | types.bal:51 |
| `type count string;` (+ its doc comment) | types.bal:159–160 |
| `type A_SalesDistrictExpandOptions "to_Text"[];` | types.bal:179 |
| `type SalesDistrictOfA_SalesDistrictTextExpandOptions "to_Text"[];` | types.bal:186 |
| `type A_SalesDistrictTextOrderByOptions (…6 members…)[];` | types.bal:196 |
| `type A_SalesDistrictTextSelectOptions ("SalesDistrict"\|"Language"\|"SalesDistrictName"\|"to_SalesDistrict")[];` | types.bal:198 |
| `type A_SalesDistrictSelectOptions ("SalesDistrict"\|"to_Text")[];` | types.bal:200 |
| `type SalesDistrictOfA_SalesDistrictTextSelectOptions ("SalesDistrict"\|"to_Text")[];` | types.bal:212 |

Modified (JSON-level diff of each `typeDef`, additive only — no key removed on any of the 27):

- `A_SalesDistrict`, `A_SalesDistrictText`: `annotations` array added on fields
  (`ballerina/constraint` `String {maxLength: 6}` / `{maxLength: 2}`).
- `ConnectionConfig`: type-level `annotations` `display {label: "Connection Config"}` added.
- `ProxyConfig`: field-level `annotations` `display {label: "", kind: "password"}` added on `password`.
- `count`: `baseType: "string"` added; the 8 option aliases gained `baseType` strings.

Removed: **none** at declaration level. The only removals in the text diff are the 6 occurrences of
`anydata Additional Values, ` inside client method parameter lists (one per remote method), plus the
9 placeholder comment lines that were replaced by real definitions.

## 3. Correctness against library source

Verified each `new` addition against `types.bal` in the bala (identical to the tag):

- `A_SalesDistrictTextExpandOptions` — source `public type A_SalesDistrictTextExpandOptions ("to_SalesDistrict")[];`
  (types.bal:23); render `"to_SalesDistrict"[]` — semantically identical (redundant parens dropped),
  valid array-of-singleton type descriptor.
- `A_SalesDistrictOrderByOptions` (:51), `A_SalesDistrictTextOrderByOptions` (:196),
  `A_SalesDistrictTextSelectOptions` (:198), `A_SalesDistrictSelectOptions` (:200),
  `A_SalesDistrictExpandOptions` (:179), `SalesDistrictOfA_SalesDistrictTextExpandOptions` (:186),
  `SalesDistrictOfA_SalesDistrictTextSelectOptions` (:212) — member lists and ordering match the
  source exactly, character for character.
- `count` (:159–160) — `public type count string;` with the `# The number of entities in the
  collection. Available when using the [$inlinecount](…) query option.` doc; both the alias and the
  doc are reproduced verbatim in `new` (render lines 206–207).
- `@constraint:String {maxLength: 6}` on `A_SalesDistrict.SalesDistrict` (types.bal:62) and
  `A_SalesDistrictText.SalesDistrict` (types.bal:215); `{maxLength: 2}` on
  `A_SalesDistrictText.Language` (types.bal:217) — all three match.
- `@display {label: "Connection Config"}` on `ConnectionConfig` (types.bal:94) and
  `@display {label: "", kind: "password"}` on `ProxyConfig.password` (types.bal:176) — match.
- Removal of `anydata Additional Values`: the 6 remote methods declare
  `*GetA_SalesDistrictQueries queries` etc. (client.bal:65, 79, 93, 105, 116, 128). There is no
  parameter named `Additional Values` and no `anydata` parameter anywhere in `client.bal`
  (`grep -n 'anydata' client.bal` → no match). The `new` behaviour is the correct one.
- Client shape: `init(ConnectionConfig config, string hostname, int port = 443) returns error?`
  matches client.bal:31. All 6 remote method names and return types match client.bal.

## 4. Regressions

**None found.**

Basis for that conclusion:

- Declaration-name set comparison of the two JSONs: identical (27 typeDefs, same names; 1 client
  with the same 7 functions including `init`).
- Per-`typeDef` JSON diff for all 27 types: every difference is a key **added** in `new`
  (`annotations`, `baseType`); no key or field is dropped.
- Per-function parameter-list diff for all 7 client functions: the only delta is the deletion of the
  `('Additional Values', anydata)` entry; every real parameter, its type, its `optional` flag and its
  `default` are unchanged.
- `readme` and `description` JSON fields compare equal between old and new (`o["readme"]==n["readme"]`
  → True), so no README/section content was lost; both renders carry the same 4 section markers.
- Text-level: 15 removed lines total, all accounted for (9 placeholder comments + 6 signature lines
  that reappear in `new` minus the bogus parameter).

## 5. Issues in `new` (independent of `old`)

None of these are caused by spec v2 — items 1–4 are present identically in `old` — but they are
inaccuracies a consumer of the `new` render would hit:

1. **Invented default values on the flattened query parameters.** `new` (and `old`) renders
   `int \$skip = 0, int \$top = 0, string \$filter = "", …OrderByOptions \$orderby = [],
   "allpages"|"none" \$inlinecount = "allpages", …SelectOptions \$select = []`. In the source these
   are *optional record fields with no default* (`int \$skip?;` … `"allpages"|"none" \$inlinecount?;`,
   types.bal:28–41). The JSON carries `"optional": true, "default": "0"` / `"\"allpages\""` etc., so
   the extractor synthesises zero-values. An LLM would conclude `$inlinecount` defaults to
   `"allpages"` and that `$skip`/`$top` are sent as `0`, which is wrong (the fields are simply
   omitted from the query string).
2. **Included-record parameter is emitted twice.** Each remote method shows both the flattened
   fields of the `*…Queries` included record *and* a trailing `GetA_SalesDistrictQueries queries`
   parameter (e.g. render line 345). The source has only the included-record parameter.
3. **Resulting signature does not compile.** Because `queries` is rendered with no default *after*
   defaulted parameters, e.g. `remote function listA_SalesDistricts(map<string|string[]> headers = {},
   …, A_SalesDistrictSelectOptions \$select = [], ListA_SalesDistrictsQueries queries)` is invalid
   Ballerina (required parameter after defaultable ones).
4. **Record defaults dropped and closedness lost.** `ConnectionConfig` is `record {| … |}` with
   `httpVersion = http:HTTP_2_0`, `timeout = 60`, `forwarded = "disable"`,
   `compression = http:COMPRESSION_AUTO`, `validation = true` (types.bal:95–127); the render shows an
   **open** `record {` with those fields as bare optionals (`http:HttpVersion httpVersion?;`,
   `decimal timeout?;`, `boolean validation?;`). Same for `ProxyConfig` (`host = ""`, `port = 0`,
   `userName = ""`, `password = ""`) and `ClientHttp1Settings`.
5. **New-only, cosmetic:** the emitted `@constraint:String {…}` annotations use the `constraint:`
   prefix, but the render's import block (line 5) imports only the connector module, and unlike type
   references (which get `// Special Agent Note: X FROM ballerina/http package`) the annotation
   carries no provenance marker even though the JSON records `"module": "ballerina/constraint"`.
   Same for `@display` (from `ballerina/jballerina.java`-adjacent `display` annotation). Low impact,
   but the render is not self-contained on those prefixes.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala's default module `sap.s4hana.api_salesdistrict_srv` exports 27 public types
(`grep -c '^public' types.bal` → 27) and 1 public client class (`client.bal:24`). All 27 type names
appear in `new` as `type <Name> …` (checked programmatically, no misses) and in `old` either as a
`type` or as a `// Unknown type:` placeholder (no misses). `utils.bal` has 0 public symbols
(`grep -c '^public' utils.bal` → 0), so its `Encoding`/`getPathForQueryParam` helpers are correctly
absent.

Submodule note (shared, not a gap): the bala contains a second module
`sap.s4hana.api_salesdistrict_srv.mock`, but `package.json` marks it `"export": false` and Ballerina
Central lists only the default module. So the `getDefaultModule()`-only extraction misses nothing
public here.

Not rendered on either side (extractor-wide behaviour, not library-specific): the client's `final
sap:Client clientEp` field, and the `isolated`/`public` qualifiers on the class and its methods
(render shows `client class Client` / `remote function …`, source has `public isolated client class
Client` / `remote isolated function`).

## 7. Compiler plugin

The package has **no compiler plugin**: no `[[platform.java*.dependency]]` / `CompilerPlugin.toml`
in `ballerina/api_salesdistrict_srv/Ballerina.toml`, no `*compiler-plugin*` path anywhere in the
cloned tag, and no `compiler-plugin/` entry in the bala. Nothing plugin-derived is expected in the
render, and nothing is missing on that account.

## 8. Other considerations

- Version is stable (2.1.0), package not deprecated (Central `deprecated: null`), `pullCount` 21,
  built for `2201.13.0`, `graalvmCompatible: true`.
- Size impact is negligible: +6 lines (360 → 366). The 9 restored aliases are exactly the enumerated
  `$select`/`$expand`/`$orderby` option sets, which are the highest-value tokens in this connector —
  without them (`old`) an LLM had no way to know which literals are legal for `$select`/`$orderby`.
  This is the single biggest practical improvement here.
- Both renders escape `$` as `\$` in identifiers (`\$select`), consistent with Ballerina quoted
  identifiers — correct.
- README is auto-included and identical on both sides; it references sibling modules
  (`sap.s4hana.api_sales_order_srv`) in its Examples section, which is upstream content, not a
  render artefact.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/new .bal.txt` | 360 / 366 |
| `diff -u old new` counts | 21 added, 15 removed, 10 hunks |
| `grep -c '^// Unknown type:'` | old 9, new 0 |
| `grep -c '^type '` | old 18, new 27 |
| JSON top-level array sizes both sides | typeDefs 27, clients 1, functions 0, services 0, annotations 0 |
| Python set-compare of typeDef names old vs new | equal |
| Python per-typeDef JSON diff (27 types) | 13 differ; every diff is an added `annotations`/`baseType` key, 0 removals |
| Python per-function param diff (7 client functions) | only delta = `('Additional Values','anydata')` removed from the 6 remote methods |
| `o["readme"]==n["readme"]`, `o["description"]==n["description"]` | True, True |
| `git ls-remote --tags …sap.s4hana.sales \| grep salesdistrict` | `api_salesdistrict_srv-v2.1.0` → `d8641505e…` |
| `git clone --depth 1 --branch api_salesdistrict_srv-v2.1.0` | OK; module dir `ballerina/api_salesdistrict_srv`, `Ballerina.toml` version = 2.1.0 |
| `diff -q` bala vs tag for `client.bal`, `types.bal`, `utils.bal` | identical (all three) |
| `grep -c '^public'` types.bal / client.bal / utils.bal | 27 / 1 / 0 |
| Loop: every `public type X` present in new render as `^type X ` | 0 missing (also 0 missing in old counting placeholders) |
| `find src -iname '*compiler-plugin*'` | no matches |
| bala `package.json` `export` / `modules` | exports default module only; `.mock` module `export: false` |
| Central `GET /2.0/registry/packages/ballerinax/sap.s4hana.api_salesdistrict_srv/2.1.0` | version 2.1.0, `deprecated: null`, 1 module listed |
| `grep -n 'anydata' bala client.bal` | no match (confirms `Additional Values` is synthetic) |

## 10. Caveats and unverified items

- The renders were not compiled. Statements about `new`'s type-alias syntax being valid Ballerina
  (`type X "lit"[];`, `type X ("a"|"b")[];`) are based on reading the source/spec, not on a `bal build`
  run; the render as a whole is not a compilable unit by design (it embeds raw README markdown).
- Item 5 in §5 (missing `constraint:` import / provenance note in the render) is an observation about
  render self-containment; I did not check the `toSyntaxString` implementation to confirm whether
  annotation-module provenance is intentionally omitted.
- The default values reported as synthesized (§5.1) were read from the JSON `"default"` fields; I did
  not read the Java extractor to confirm where those zero-values are generated, only that they are
  absent from the library source.

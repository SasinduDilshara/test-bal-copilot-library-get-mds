# ballerinax/sap.s4hana.api_salesorganization_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_salesorganization_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_salesorganization_srv-v2.1.0` (commit `71c4bc2`, monorepo — only `ballerina/api_salesorganization_srv/` reviewed) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_salesorganization_srv/2.1.0` |
| Old render | `365` lines |
| New render | `371` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. `new` eliminates all 9 `// Unknown type:` placeholders by emitting the
real type definitions (8 union-array option types + `type count string`), all of which match
`types.bal` in the bala byte-for-byte in meaning. `new` additionally surfaces 5 annotations
(`@constraint:String` ×3, `@display` ×2) that `old` silently dropped, and removes a synthetic,
non-compiling `anydata Additional Values` parameter from all 6 remote methods. Nothing present in
`old` is missing, truncated, or made less accurate in `new`. The README section, the type-name set,
the client, and all 7 client functions are identical between sides.

A handful of inaccuracies vs. the library source remain in `new`, but every one of them is present
identically in `old` (fabricated parameter defaults, dropped record-field defaults, open-vs-closed
records, dropped `public`/`isolated`). They are pre-existing extractor behaviour, not spec-v2
regressions.

## 2. Change inventory

Line counts (`wc -l`): old 365, new 371. Diff: 10 hunks, +21 / −15 lines.

| Kind | old | new | Delta |
|---|---|---|---|
| `type` declarations rendered as real definitions | 18 | 27 | **+9** |
| `// Unknown type:` placeholders | 9 | 0 | **−9** |
| Type names present (real + placeholder) | 27 | 27 | 0 |
| `client class` | 1 | 1 | 0 |
| `init` function | 1 | 1 | 0 |
| `remote function` | 6 | 6 | 0 |
| Section markers (`// --- `) | 4 | 4 | 0 |
| README section lines (render lines 8–113) | identical | identical | 0 |
| JSON `typeDefs` | 27 | 27 | 0 |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 | 0 |

**Declarations added (9)** — all previously `// Unknown type:` lines, now real definitions:
`A_SalesOrganizationExpandOptions`, `A_SalesOrganizationOrderByOptions`,
`A_SalesOrganizationSelectOptions`, `A_SalesOrganizationTextExpandOptions`,
`A_SalesOrganizationTextOrderByOptions`, `A_SalesOrganizationTextSelectOptions`,
`SalesOrganizationOfA_SalesOrganizationTextExpandOptions`,
`SalesOrganizationOfA_SalesOrganizationTextSelectOptions`, `count`.

**Declarations removed:** none (`comm` on the sorted name sets is empty in both directions).

**Annotations added in `new` (5, all absent from `old`):**

| Location | Annotation | Bala source |
|---|---|---|
| `A_SalesOrganizationText.SalesOrganization` | `@constraint:String {maxLength: 4}` | `types.bal:152` |
| `A_SalesOrganizationText.Language` | `@constraint:String {maxLength: 2}` | `types.bal:154` |
| `A_SalesOrganization.SalesOrganization` | `@constraint:String {maxLength: 4}` | `types.bal:216` |
| `ConnectionConfig` (type-level) | `@display {label: "Connection Config"}` | `types.bal:64` |
| `ProxyConfig.password` | `@display {label: "", kind: "password"}` | `types.bal:141` |

**Parameters removed in `new` (6, one per remote method):** synthetic
`anydata Additional Values` (JSON: `{"name":"Additional Values","description":"Capture key value
pairs","type":{"name":"anydata"},"optional":true}`). This was the open-record rest field of the
`*Queries` included-record parameter rendered as a positional parameter with a space in its name —
invalid Ballerina. The real `queries` parameter is retained on both sides. Documented separately in §5.

**Type-level docs:** `count`'s doc comment (`# The number of entities in the collection…`) was present
in the `old` JSON but lost in the `old` render because the placeholder path emits no doc; `new`
emits it.

## 3. Correctness against library source

The upstream tag `api_salesorganization_srv-v2.1.0` was cloned and its
`ballerina/api_salesorganization_srv/{types.bal,client.bal,utils.bal}` diffed against the bala's
`modules/sap.s4hana.api_salesorganization_srv/` — **all three files are byte-identical**. So GitHub
and the bala agree; line references below hold for both.

All 9 newly-emitted definitions verified against `types.bal`:

| Render (`new`) | Bala `types.bal` | Match |
|---|---|---|
| `type A_SalesOrganizationTextExpandOptions "to_SalesOrganization"[];` | L47 `("to_SalesOrganization")[]` | yes (redundant parens dropped; equivalent) |
| `type A_SalesOrganizationTextSelectOptions ("SalesOrganization"\|"Language"\|"SalesOrganizationName"\|"to_SalesOrganization")[];` | L31 | exact |
| `type SalesOrganizationOfA_SalesOrganizationTextExpandOptions "to_Text"[];` | L37 `("to_Text")[]` | yes |
| `type SalesOrganizationOfA_SalesOrganizationTextSelectOptions ("SalesOrganization"\|"SalesOrganizationCurrency"\|"CompanyCode"\|"IntercompanyBillingCustomer"\|"to_Text")[];` | L61 | exact |
| `type A_SalesOrganizationExpandOptions "to_Text"[];` | L149 `("to_Text")[]` | yes |
| `type A_SalesOrganizationSelectOptions (…4 fields…\|"to_Text")[];` | L227 | exact |
| `type A_SalesOrganizationOrderByOptions (…8 alternatives…)[];` | L165 | exact |
| `type A_SalesOrganizationTextOrderByOptions (…6 alternatives…)[];` | L213 | exact |
| `type count string;` + doc | L129–130 | exact, doc included |

All 5 new annotations verified at the `types.bal` lines listed in §2. No invented symbols: the set of
`type X` names in `new` is exactly the set of `public type` names in `types.bal` (27 = 27, `comm`
empty both ways).

Client: `client.bal:24` declares `public isolated client class Client` with `init` (L32) and 6 remote
methods (L67, L81, L95, L107, L119, L132). `new` renders exactly those 7, with matching names, return
types (`A_SalesOrganizationWrapper|error`, `A_SalesOrganizationTextWrapper|error`,
`CollectionOfA_SalesOrganization[Text]Wrapper|error`) and path/key parameters
(`SalesOrganization`, `Language`). `init(ConnectionConfig config, string hostname, int port = 443)
returns error?` matches `client.bal:32`.

## 4. Regressions

**None found.**

Checked, with the result of each check:
- Declaration name sets: `comm -3` on sorted `type` names (old incl. placeholders vs. new) → empty.
- Client function name sets from both JSONs → identical 7 names.
- Return types, per-method: identical strings in both renders (only the `Additional Values` token
  differs in the 6 diff hunks in the Client section).
- README: `sed -n '8,113p'` of both renders → `diff` empty; and matches the bala `docs/README.md`
  (105 lines) exactly, plus one trailing blank line, on both sides.
- `description`, `readme`, `annotations` keys of both JSONs → equal (`==` in Python).
- Record field counts, per changed record: `A_SalesOrganization` 5/5, `A_SalesOrganizationText` 4/4,
  `ProxyConfig` 4/4, `ConnectionConfig` 15/15 — no field dropped.
- Doc comments: no `# …` doc line present in `old` is absent from `new` (all 15 removed diff lines
  are the 9 placeholders and the 6 `Additional Values` parameter tokens).
- Type-qualified refs (`mod:1.2.3:Type`): 0 in both.
- The only removed parameter (`anydata Additional Values`) corresponds to no declared parameter in
  `client.bal`; its removal loses no real API surface (see §5.6 for the one nuance).

## 5. Issues in `new` (independent of `old`)

All five below are present **identically in `old`** — they are pre-existing extractor/renderer
behaviour, not introduced by spec v2. Listed because they are still wrong in `new`.

1. **Fabricated parameter defaults.** The flattened query parameters are rendered with defaults —
   `int \$skip = 0`, `int \$top = 0`, `string \$filter = ""`, `\$orderby = []`, `\$expand = []`,
   `\$select = []`, `"allpages"|"none" \$inlinecount = "allpages"`. In `types.bal` these are
   *optional record fields with no default* (`int \$skip?;` L114/L170/L198;
   `"allpages"|"none" \$inlinecount?;` L124/L180/L208). Both JSONs carry `"default":"0"` /
   `"\"allpages\""` etc. An LLM would wrongly conclude `$inlinecount` defaults to `"allpages"`.
2. **Duplicated / non-compiling client signatures.** Each remote method lists the flattened fields of
   the included record *and* a trailing `GetA_SalesOrganizationQueries queries` (etc.) parameter —
   the same data twice, and a required-looking parameter after defaultable ones, which does not
   compile. Source uses a single `*GetA_SalesOrganizationQueries queries` (`client.bal:67`).
3. **Record-field defaults dropped and turned into optional fields.** `ConnectionConfig`
   `httpVersion = http:HTTP_2_0` (L69), `timeout = 60` (L75), `forwarded = "disable"` (L77),
   `compression = http:COMPRESSION_AUTO` (L83), `validation = true` (L95); `ClientHttp1Settings`
   `keepAlive`/`chunking` (L188–189); `ProxyConfig` `host`/`port`/`userName`/`password` (L135–142) —
   all render as bare `?` optional fields with no default. This changes the semantics the model sees.
4. **Closed records rendered as open.** `ConnectionConfig`, `ProxyConfig`, `ClientHttp1Settings` are
   `record {| … |}` in source (L65, L133, L186); both renders emit `record { … }`.
5. **Qualifiers and imports lost.** `public isolated client class Client` → `client class Client`;
   `remote isolated function` → `remote function`; `public type` → `type`. The render's only import
   is `import ballerinax/sap.s4hana.api_salesorganization_srv;`, yet the body references `http:*`
   types, `@constraint:String` and `@display` with no corresponding imports — the render is not
   compilable as-is (it is a synopsis, so this may be by design).
6. **Nuance on the removed parameter.** The `*Queries` records are *open* (`record { … }`), so callers
   may legitimately pass extra query parameters. `old` expressed that as the malformed
   `anydata Additional Values`; `new` expresses it not at all. Net: `new` is better formed but the
   open-record extensibility is now invisible on both the parameter list and the (open-rendered)
   record — a negligible loss, and the old form was invalid syntax.

## 6. Coverage gaps vs. the library

**0 gaps.**

- Default module `sap.s4hana.api_salesorganization_srv` exports 28 public symbols:
  27 `public type` (`grep -c '^public type' types.bal` → 27) + `public isolated client class Client`
  (`client.bal:24`). `utils.bal` contains no `public` declarations (`grep -nE '^public ' utils.bal`
  → no hits), so `Encoding`, `getEncodedUri`, `getPathForQueryParam` are correctly absent.
- All 27 type names appear as real `type` definitions in `new` (`comm` both ways → empty).
- `Client` and all 7 of its functions appear in both renders.
- The bala contains a second module `sap.s4hana.api_salesorganization_srv.mock`, but
  `package.json` marks it `"export": false` and Central lists only
  `["sap.s4hana.api_salesorganization_srv"]` as a module. Its absence from both renders is correct,
  not a submodule gap.

## 7. Compiler plugin

None. `find . -iname '*compiler-plugin*'` over the cloned tag returns nothing, and the bala contains
no `compiler-plugin/` directory or `compiler-plugin.json` (bala file list is exactly `bala.json`,
`dependency-graph.json`, `package.json`, `docs/README.md`, `docs/icon.png`, plus `modules/`).
Nothing plugin-implied is therefore missing from the render.

The only annotation-bearing behaviour in the package is `ballerina/constraint` validation, and `new`
now surfaces those `@constraint:String` annotations — previously invisible.

## 8. Other considerations

- **Stability / deprecation.** Central reports `deprecated: null`, `graalvmCompatible: Yes`,
  `ballerinaVersion: 2201.13.0`, pull count 21. Version 2.1.0 is a stable release; no deprecation
  notice to propagate.
- **Size.** +6 lines (+1.6%), JSON +391 bytes (59,355 → 59,746). Negligible token impact for a
  clear accuracy gain — the 8 option types are exactly the enum-like literal sets an LLM needs to
  fill `$select`/`$expand`/`$orderby` correctly, and in `old` they were completely opaque.
- **Doc-comment bug in the library itself (not a render issue).** `client.bal:30` documents
  `+ serviceUrl - URL of the target service` but the parameter is `hostname`; `serviceUrl` is a local
  computed inside `init` (L33). Both renders drop the `init` parameter docs entirely, so this bug is
  not propagated.
- **Auto-generated package.** `client.bal`/`types.bal` are OpenAPI-tool generated ("AUTO-GENERATED
  FILE. DO NOT MODIFY."), so the render quality here is representative of the other
  `sap.s4hana.*` sibling modules in the same monorepo.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 365 / 371 |
| 2 | `diff -u old new` (full) | 10 hunks, +21/−15 |
| 3 | `grep -c '^// Unknown type:'` old / new | 9 / 0 |
| 4 | `grep -n '^// --- '` old / new | 4 markers each (README/END README/Types/Client) |
| 5 | `grep -cE '^type '` old / new | 18 / 27 |
| 6 | `grep -c 'remote function'` new; `grep -c 'remote isolated function' bala/client.bal` | 6 / 6 |
| 7 | `comm -23/-13` sorted type names bala vs. new render | both empty (27 = 27) |
| 8 | `comm -3` bala types vs. old render names (incl. placeholders) | empty |
| 9 | Python: `o['readme']==n['readme']`, `o['description']==n['description']`, `o['annotations']==n['annotations']` | True, True, `[] == []` |
| 10 | Python: JSON `typeDefs`/`clients`/`functions`/`services` counts | 27/1/0/0 both sides |
| 11 | Python: per-typeDef deep diff | 13 differ; 9 gain `baseType`, `ConnectionConfig` gains type-level `annotations`, `A_SalesOrganization`/`A_SalesOrganizationText`/`ProxyConfig` gain field `annotations` |
| 12 | Python: per-client-function deep diff | only difference is removal of the `Additional Values` parameter in all 6 remote methods; `init` unchanged |
| 13 | `git ls-remote --tags` on the monorepo | `api_salesorganization_srv-v2.1.0` exists (`71c4bc2`) |
| 14 | `git clone --depth 1 --branch api_salesorganization_srv-v2.1.0` | OK |
| 15 | `diff src/ballerina/api_salesorganization_srv/{types,client,utils}.bal` vs. bala `modules/…` | all three IDENTICAL |
| 16 | `cat Ballerina.toml` at tag | `version = "2.1.0"`, org `ballerinax`, name `sap.s4hana.api_salesorganization_srv` → PIN_OK |
| 17 | `grep -nE '^public '` over bala module `.bal` files | 27 `public type` + 1 `public isolated client class Client`; 0 in `utils.bal` |
| 18 | `find . -iname '*compiler-plugin*'` in clone; bala file listing | no plugin on either side |
| 19 | `diff <(sed -n '1,106p' bala/docs/README.md) <(sed -n '8,113p' new render)` | identical except one trailing blank line; old vs. new README sections `diff` → empty |
| 20 | `curl api.central.ballerina.io/.../2.1.0` | `deprecated: null`, `graalvmCompatible: Yes`, modules `['sap.s4hana.api_salesorganization_srv']` |
| 21 | `wc -c old/*.json new/*.json` | 59,355 / 59,746 |
| 22 | `awk '/^type ConnectionConfig/,/^};/'` on old, and ProxyConfig on new | field defaults absent on both sides; `record {` open on both sides |
| 23 | Bala `package.json` `modules` entry | `sap.s4hana.api_salesorganization_srv.mock` with `"export": false` |
| 24 | Cross-check of `OLD_AND_NEW_DIFFS/…_diff.md` figures against files | all figures (365/371, +21/−15, 9→0 placeholders, 9 added decls, 0 removed) reproduced independently |

## 10. Caveats and unverified items

- The two renders were supplied pre-generated; the pipeline was **not** re-run, so the claim that the
  only variable between sides is the extractor/renderer version rests on the brief, not on my own
  observation. All content-level checks above are consistent with that claim (identical README,
  identical type-name set, identical function set).
- The `old` renderer's `// Unknown type:` path is inferred from the diff and the JSON shape
  (`type: "Other"` with no `baseType` in `old`, with `baseType` in `new`); I did not read the
  `renderTypeDef` / `toSyntaxString` sources, so the exact mechanism is unverified.
- Whether the render is *intended* to be compilable Ballerina is unknown; §5.2/§5.5 are reported as
  fidelity issues on that assumption. If the render is only a synopsis, those items are cosmetic.
  Either way they are identical on both sides.
- The `.mock` submodule's contents were not audited — it is non-exported and out of scope.

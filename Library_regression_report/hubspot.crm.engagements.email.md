# ballerinax/hubspot.crm.engagements.email 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.engagements.email` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.engagements.email |
| Tag reviewed | `v2.0.2` (commit `45330760cfbf74ce95c410c8c6ebb2673f537ad1`, peeled `17cffae7c58a235021aae1e26bae00401edc79bc`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.engagements.email/2.0.2` |
| Old render | `777` lines (34,294 bytes) |
| New render | `778` lines (33,889 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module OpenAPI-generated HubSpot connector: 41 public types + 1 client class with `init` and
11 resource methods. Both renders carry the complete public API surface — no declaration is added or
removed by `new`. All 15 diff hunks are strictly corrective:

- 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
  `ballerinax/hubspot.crm.engagements.email:2.0.2:ValueWithTimestamp`) collapse to the plain,
  compilable forms `int:Signed32` / `ValueWithTimestamp`.
- 4 bogus parameters literally named `Additional Values` (type `anydata`, an identifier containing a
  space — non-compiling Ballerina) are removed from the client resource signatures.
- 1 annotation, `@display {label: "Connection Config"}`, is newly emitted on `ConnectionConfig`,
  matching `types.bal:229`.

Zero `// Unknown type:` placeholders on either side, so the spec-v2 type-definition improvement is a
no-op here. No regression was found. A set of pre-existing inaccuracies (dropped record-field
defaults, one wrong default value, a non-compiling trailing `queries` parameter, lost `.` resource
path) is present identically in **both** renders and is reported in §5 as unfixed, not as regression.

## 2. Change inventory

Diff totals (`diff old new`): 62 output lines, 15 hunks, 16 lines added, 15 removed.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations in render | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `resource function` members | 11 | 11 | 0 |
| `remote function` members | 0 | 0 | 0 |
| Module-level functions / services / annotations (JSON arrays) | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| Section markers `// --- ` | 4 | 4 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 11 | 0 | **−11** |
| `Additional Values` phantom params | 4 | 0 | **−4** |
| Top-level `@display` annotations rendered | 0 | 1 | **+1** |
| `record {\|` closed-record renderings | 19 | 19 | 0 |
| `Special Agent Note` cross-package hints | 17 | 17 | 0 |

Declaration name sets are byte-identical: `diff <(types in old) <(types in new)` → SAME (41 names each).

Changes by category:

1. **Type-reference normalisation (12 lines, 6 in Types section fields + 6 more).** Examples:
   - L309 `ballerina/lang.int:0.0.0:Signed32 associationTypeId;` → `int:Signed32 associationTypeId;`
   - L346 `record {|ballerinax/hubspot.crm.engagements.email:2.0.2:ValueWithTimestamp[]...;|}` →
     `record {|ValueWithTimestamp[]...;|}`
   - Same pattern at old L365, L413, L440, L533, L597, L614, L666, L674, L722.
2. **Annotation added (1 line).** New L542 `@display {label: "Connection Config"}` above
   `type ConnectionConfig`.
3. **Phantom-parameter removal (4 client signatures).** `post batch/read`, `get [string emailId]`,
   `patch [string emailId]`, `get ` each lose `anydata Additional Values`.

At JSON level the shape is unchanged: both have keys
`annotations, clients, description, functions, name, readme, services, typeDefs`; `typeDefs` = 41 both;
`clients[0].functions` = 12 both. The `ConnectionConfig` typeDef gains an `annotations` key in `new`
(`[{"name":"display","value":"{label: \"Connection Config\"}"}]`); it is absent in `old`.

README block (render lines 1–210) is byte-identical between the two files.

## 3. Correctness against library source

Verified against the bala (authoritative) and cross-checked with the `v2.0.2` clone.

- **Type inventory.** `grep -oE '^public type [A-Za-z0-9_]+' types.bal` → 41 names.
  `grep -oE '^type [A-Za-z0-9_]+' new render` → 41 names. `comm` both directions → empty.
  Every public type is rendered, nothing invented.
- **`int:Signed32`.** `types.bal:459` declares `int:Signed32 'limit = 10;`, `types.bal:368`
  `int:Signed32 associationTypeId;`. The `new` spelling `int:Signed32` matches the source verbatim;
  `old`'s `ballerina/lang.int:0.0.0:Signed32` does not appear anywhere in the source.
- **`ValueWithTimestamp` / `CollectionResponseAssociatedId` rest-field records.**
  `types.bal:381` `record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;` — `new` matches
  exactly; `old` prefixed the org/module/version.
- **`@display` annotation.** `types.bal:229` `@display {label: "Connection Config"}` immediately
  above `public type ConnectionConfig record {|`. It is the **only** annotation in the whole module
  (`grep -n '^\s*@' *.bal` → 1 hit). `new` renders exactly that one; `old` rendered none.
- **`Additional Values` is not in the library.** `grep -c 'Additional Values'` over all three bala
  `.bal` files → 0. It was an artifact of `old` materialising the implicit `anydata` rest field of
  the open `*Queries` records as a parameter. Its removal in `new` is correct.
- **Client shape.** `client.bal:23` `public isolated client class Client`; `client.bal:31` `init`;
  11 `resource isolated function` declarations at lines 47, 67, 84, 100, 119, 137, 155, 174, 191,
  209, 227. `new` renders `init` + 11 resource functions with matching accessors, paths, payload
  types and return unions — e.g. `client.bal:209` `post batch/upsert(BatchInputSimplePublicObjectBatchInputUpsert payload, ...) returns BatchResponseSimplePublicUpsertObject|BatchResponseSimplePublicUpsertObjectWithErrors|error`
  matches new render L771 verbatim.
- **Query-record expansion.** `client.bal:47` takes `*PostCrmV3ObjectsEmailsBatchReadReadQueries queries`;
  that record (`types.bal:51`) has exactly one field `boolean archived = false`. `new` L737 renders
  `boolean archived = false` — correct.

## 4. Regressions

**None found.**

Basis for that conclusion:

- Full `diff old new` was read line by line (62 lines, all 15 hunks reproduced above). No hunk
  deletes a declaration, a parameter that exists in the library, a default that exists in the
  library, a doc line, or README content.
- Declaration-name sets are identical (`comm` on sorted `type` names → empty both ways; resource
  function count 11 = 11; JSON `typeDefs` 41 = 41, `clients[0].functions` 12 = 12).
- Render lines 1–210 (header + README) are byte-identical.
- `Special Agent Note` cross-package annotations: 17 in both.
- The only parameter dropped in `new` is `anydata Additional Values`, which has no counterpart in
  the library source (verified `grep` = 0 hits in the bala) and was syntactically invalid.
- The 11 type-reference rewrites all move *towards* the source spelling, never away.

## 5. Issues in `new` (independent of `old`)

All six items below are present **identically in `old`**, i.e. spec v2 neither fixed nor caused them.
Listed because they are inaccuracies in the shipped `new` render.

1. **Wrong default value on `limit`.** New L765
   `resource function get (..., int:Signed32 limit = 0, ...)`. Source `types.bal:459` declares
   `int:Signed32 'limit = 10;`. `0` is invented and would mislead an LLM into requesting a
   zero-size page. (Identical in old L764.)
2. **Invented defaults on optional query fields.** `GetCrmV3ObjectsEmailsEmailIdGetByIdQueries`
   (`types.bal:342-355`) declares `string[] associations?`, `string[] propertiesWithHistory?`,
   `string idProperty?`, `string[] properties?` — optional, no defaults. The render emits
   `associations = []`, `propertiesWithHistory = []`, `idProperty = ""`, `properties = []`
   (new L741, L765). Only `archived = false` is a genuine source default.
3. **Non-compiling trailing `queries` parameter.** 4 signatures (new L737, L741, L749, L765) expand
   the included-record parameter into individual defaultable parameters *and* keep a trailing
   required `<X>Queries queries` with no default and no `*` prefix — a required parameter after
   defaultable ones. Neither form matches `client.bal`, which has only `*XQueries queries`.
   (`grep -c 'queries)'` → 4 in both files.)
4. **Resource path `.` lost.** `client.bal:174` `resource isolated function get .(...)` and
   `client.bal:191` `resource isolated function post .(...)`. Render emits
   `resource function get (` / `resource function post (` — the dot path segment is gone, leaving an
   ambiguous declaration.
5. **Record-field defaults and closedness dropped throughout.** `ConnectionConfig`
   (`types.bal:230-269`) is `record {| ... |}` with 11 defaulted fields
   (`httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`).
   The render shows an **open** `record {` and turns every defaulted field into `?` optional
   (new L543-580). Same for `GetCrmV3ObjectsEmailsGetPageQueries` (new L715-728): source
   `boolean archived = false` / `int:Signed32 'limit = 10` become `archived?` / `'limit?`.
6. **Type-inclusion flattened with default lost.** `types.bal:188-193`
   `public type OAuth2RefreshTokenGrantConfig record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl = "https://api.hubapi.com/oauth/v1/token"; |}`.
   The render (new L495-507) usefully flattens the inclusion into 10 effective fields, but emits
   `string refreshUrl?` — losing the HubSpot-specific token URL default, which is the one piece of
   information a code generator most needs here.

Minor, non-misleading: `public` / `isolated` qualifiers are dropped from the class and all methods
(render says `client class Client`, source says `public isolated client class Client`); resource
doc comments render the description then a bare `# ` line with the `+ headers` / `+ queries` /
`+ return` parameter docs omitted. Both identical in `old`.

Encoding: no mojibake or replacement characters observed in either file.

## 6. Coverage gaps vs. the library

**0 gaps.**

The bala exports exactly one module (`package.json` `"export": ["hubspot.crm.engagements.email"]`,
`modules/` contains only `hubspot.crm.engagements.email`), so the `getDefaultModule()`-only
extraction loses nothing here — there is no submodule API.

Default-module public symbols: 41 `public type` + 1 `public isolated client class Client`. All 42
appear in both renders. There are no `public` module-level functions, enums, constants, listeners or
services (`grep -nE '^public ' *.bal` → 43 hits = 41 types + Client + the closed-record continuation;
`grep -nE '^(public )?(enum|const|final)'` → `enum EncodingStyle` and `final ... defaultEncoding`,
both **non-public** internals in `utils.bal`). The six `utils.bal` helper functions and the
`SimpleBasicType` / `Encoding` type aliases are module-private and correctly absent.

## 7. Compiler plugin

The package has **no compiler plugin**: `find` over the bala returns no `compiler-plugin/` directory
and no `compiler-plugin.json`; the `v2.0.2` clone has no `compiler-plugin`, `*-compiler-plugin`, or
`ballerina-*-compiler-plugin` directory at depth 2. Nothing plugin-derived is therefore expected in,
or missing from, the render.

## 8. Other considerations

- **Version/health.** Central reports `deprecated: null`, empty `deprecateMessage`, built with
  Ballerina `2201.12.2`, `graalvmCompatible: true`, pullCount 18. Stable 2.x, no advisories.
- **Provenance.** `client.bal` and `types.bal` are marked `AUTO-GENERATED ... by the Ballerina
  OpenAPI tool`; upstream GitHub `ballerina/` sources and the bala module sources agree, so no
  bala-vs-GitHub divergence to arbitrate.
- **Size/tokens.** `new` is 405 bytes smaller than `old` (33,889 vs 34,294) despite being one line
  longer, because the removed version-qualified prefixes and phantom parameters outweigh the added
  annotation line. Net token win with strictly higher fidelity.
- **LLM impact of the fixes.** The 11 `org/mod:version:Type` spellings in `old` are not valid
  Ballerina and would be copied into generated code verbatim; likewise `anydata Additional Values`.
  Removing both materially reduces the chance of emitting non-compiling code.
- **Residual LLM risk.** Items 1–4 in §5 remain in `new`: a model following the render will write
  `limit = 0` instead of `10`, and will not know how to pass the `*Queries` included record.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 777 / 778 |
| 2 | `wc -c old/…bal.txt new/…bal.txt` | 34,294 / 33,889 |
| 3 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 4 | `grep -n '^// --- '` both | 4 markers each; old 7/209/211/729, new 7/209/211/730 |
| 5 | `diff old new` | 62 lines, 15 hunks, +16 / −15 (full text reviewed) |
| 6 | `grep -cE '[A-Za-z0-9._]+/[A-Za-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 11, new 0 |
| 7 | `grep -c 'Additional Values'` renders | old 4, new 0 |
| 8 | `grep -c 'Additional Values'` bala `*.bal` | 0 (symbol does not exist in library) |
| 9 | `grep -c 'queries)'` renders | 4 / 4 (trailing param retained in both) |
| 10 | `grep -c 'Special Agent Note'` | 17 / 17 |
| 11 | `grep -c 'record {\|'` | 19 / 19 |
| 12 | `grep -n '^@'` renders | old: none; new: L542 `@display {label: "Connection Config"}` |
| 13 | `grep -n '^\s*@'` bala `*.bal` | 1 hit — `types.bal:229` `@display {label: "Connection Config"}` |
| 14 | type-name sets `comm -13` / `comm -23` (render new vs bala public types) | empty both directions; 41 = 41 |
| 15 | `diff <(old type names) <(new type names)` | SAME |
| 16 | `grep -c '^    resource function '` renders | 11 / 11 |
| 17 | `grep -c '^    function '` renders | 1 / 1 (`init`) |
| 18 | `grep -cE '^(public )?type '` renders | 41 / 41 |
| 19 | `client.bal` read in full (240 lines) | `init` + 11 resource functions at L47,67,84,100,119,137,155,174,191,209,227 |
| 20 | `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** |
| 21 | `git clone --depth 1 --branch v2.0.2` | success; `ballerina/{client.bal,types.bal,utils.bal}` present |
| 22 | `find <bala> -iname '*compiler*'` | no results |
| 23 | `find <clone> -maxdepth 2 -iname '*compiler*'` | no results |
| 24 | `bala/…/any/modules/` listing | single module `hubspot.crm.engagements.email` |
| 25 | `package.json` `export` | `["hubspot.crm.engagements.email"]`; ballerina_version 2201.12.2; graalvmCompatible true |
| 26 | Central API `…/ballerinax/hubspot.crm.engagements.email/2.0.2` | deprecated null, 1 module, pullCount 18 |
| 27 | JSON top-level key/array compare | identical keys; typeDefs 41=41, clients 1=1, functions 0=0, services 0=0, annotations 0=0 |
| 28 | JSON `ConnectionConfig` typeDef keys | old `[description,fields,name,type]`; new adds `annotations` = `[{name: display, value: {label: "Connection Config"}}]` |
| 29 | JSON per-function parameter-name compare | 4 functions differ, each only by removal of `Additional Values` |
| 30 | `diff` of render lines 1–210 | identical (README + header preserved) |
| 31 | `types.bal:230-269` vs new render L543-580 | source `record {\|`+11 defaults; render open `record {`, defaults → `?` (same in old) |
| 32 | `types.bal:453-467` vs new render L715-728 and L765 | `'limit = 10` → type section `'limit?`, signature `limit = 0` (same in old) |
| 33 | `types.bal:188-193` vs new render L495-507 | inclusion flattened to 10 fields; `refreshUrl` default lost (same in old) |
| 34 | `grep -nE '^public '` / `^(public )?(enum\|const\|final)` on bala | 41 public types + Client; `EncodingStyle`/`defaultEncoding` non-public |
| 35 | `wc -l bala docs/README.md` | 200 lines; render README block = 202 lines (7→209) incl. markers |

## 10. Caveats and unverified items

- **Renderer/extractor code not inspected.** I reviewed only the two render outputs, the two JSONs,
  the bala and the upstream source. The claim that the `@display` emission and the type-reference
  normalisation come from the spec-v2 change (rather than from some other difference between the two
  `ballerina-vscode` checkouts) is inferred from the JSON delta, not read from the extractor source.
- **Compilability not machine-checked.** I did not run `bal build` on the render text; the
  "non-compiling" judgements in §5 (items 3 and 4) and on `anydata Additional Values` are from
  reading the Ballerina grammar rules, not from a compiler run.
- **Doc-comment fidelity spot-checked, not exhaustive.** I compared the `ConnectionConfig`,
  `GetCrmV3ObjectsEmailsGetPageQueries`, `GetCrmV3ObjectsEmailsEmailIdGetByIdQueries`,
  `PostCrmV3ObjectsEmailsBatchReadReadQueries`, `OAuth2RefreshTokenGrantConfig`, `StandardError` and
  all 11 resource-function doc blocks against source. The remaining ~34 record types were verified
  by name/field-count and by the fact that `diff old new` touches none of their doc lines, not by
  field-by-field comparison against `types.bal`.
- **Line numbers cited for the bala** are from
  `.../2.0.2/any/modules/hubspot.crm.engagements.email/{client,types}.bal`; the GitHub clone's
  `ballerina/` copies were confirmed present but were not diffed line-for-line against the bala.

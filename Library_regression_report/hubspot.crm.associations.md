# ballerinax/hubspot.crm.associations 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.associations` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.associations |
| Tag reviewed | `v2.0.2` (commit `472c6d7bbd779db49b3556e26fe9c79670430ebf`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.associations/2.0.2` |
| Old render | `681` lines |
| New render | `682` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Ten diff hunks, all of them improvements or neutral. `new` fixes 8 malformed
version-qualified type references (`ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`),
adds the `@display {label: "Connection Config"}` annotation that exists in the library source
and was dropped by `old`, and removes a synthetic, non-compiling parameter
(`anydata Additional Values`) from one resource method signature.

No declaration is added or removed on either side: both renders carry the same 33 type
definitions, the same 1 client class, the same 10 resource methods + `init`. Both renders have
0 `// Unknown type:` placeholders. Public API coverage of the default module is complete
(33/33 public types, 1/1 client class). Several rendering inaccuracies exist, but every one of
them is present identically in `old` and `new` — none is introduced by spec v2.

## 2. Change inventory

Line counts: `old` 681, `new` 682 (`wc -l`). Diff: 10 hunks, +10 / −9 lines.

| Kind | old | new | delta |
|---|---|---|---|
| `typeDefs` (JSON) | 33 | 33 | 0 |
| `clients` (JSON) | 1 | 1 | 0 |
| `functions` / `services` / `annotations` (JSON, top-level) | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| Client functions (JSON `clients[0].functions`) | 11 | 11 | 0 |
| `type ` declarations in render | 33 | 33 | 0 |
| `resource function` in render | 10 | 10 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Version/module-qualified type refs (`ballerina/lang…`) | 8 | 0 | −8 |

Declarations added: **0**. Declarations removed: **0**.

The three change classes, exhaustively:

1. **Type-reference normalisation (8 occurrences, 7 type defs).**
   `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` in
   `ReportCreationResponse.userId`, `DateTime.timeZoneShift`,
   `AssociationSpecWithLabel.typeId`, `AssociationSpec.associationTypeId`,
   `BatchResponsePublicAssociationMultiWithLabelWithErrors.numErrors`,
   `BatchResponsePublicDefaultAssociation.numErrors`,
   `BatchResponseLabelsBetweenObjectPairWithErrors.numErrors`,
   `GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries.'limit`.
   Confirmed at the JSON level: the `type.name` field changes for exactly these 8 fields and
   nothing else.
2. **Annotation added (1).** `ConnectionConfig` gains
   `@display {label: "Connection Config"}`. JSON: `new` typeDef `ConnectionConfig` has an
   `annotations` key `[{"name":"display","value":"{label: \"Connection Config\"}"}]`; `old` has
   no `annotations` key at all.
3. **Synthetic parameter removed (1).** In
   `resource function get objects/[string objectType]/[string objectId]/associations/[string toObjectType]`,
   `old` emitted a parameter `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`,
   rendered as the literal text `anydata Additional Values`. `new` omits it. No other parameter
   of any of the 11 client functions differs (verified by whole-object JSON comparison of all 11
   function objects — only this one function differed).

## 3. Correctness against library source

Upstream `v2.0.2` sources are **byte-identical** to the bala module sources
(`diff -q` on `client.bal`, `types.bal`, `utils.bal` returned no differences), so both sources
agree and either can be cited.

- `int:Signed32` is what the library actually writes. `types.bal:61`
  (`int:Signed32 userId;` in `ReportCreationResponse`), `types.bal:102`
  (`int:Signed32 timeZoneShift;`), `types.bal:130` (`int:Signed32 typeId;`),
  `types.bal:327` (`int:Signed32 associationTypeId;`), `types.bal:376`
  (`int:Signed32 'limit = 500;`). `new` matches the source form; `old`'s
  `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina and appears nowhere in the library.
- `@display {label: "Connection Config"}` exists verbatim at
  `.../modules/hubspot.crm.associations/types.bal:170`, directly above
  `public type ConnectionConfig record {|` at line 171. It is the only `@display` annotation in
  the package (`grep -rn "@display"` → 1 hit). `new` reproduces it exactly; `old` dropped it.
- The `Additional Values` parameter removed in `new` does **not** exist in the library. The
  source signature (`client.bal:203`) is
  `resource isolated function get objects/[string objectType]/[string objectId]/associations/[string toObjectType](map<string|string[]> headers = {}, *GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries queries)`.
  `Additional Values` was a synthesised stand-in for the open record's rest field
  (the queries record is declared `record { … }`, i.e. open, at `types.bal:374`). Its removal
  loses no real API surface, and the record's openness is still conveyed because the typedef
  itself renders as `record {` (unsealed).
- Client method inventory checked against `client.bal`: `init` (line 30) plus 10 resource
  methods (`post …/batch/archive` 47, `post …/batch/create` 66, `post associations/usage/high-usage-report/[int:Signed32 userId]` 84, `post …/batch/labels/archive` 101, `post …/batch/read` 120, `post …/batch/associate/default` 139, `put objects/…/[toObjectId]` 158, `delete objects/…/[toObjectId]` 177, `get objects/…/associations/[toObjectType]` 203, `put objects/…/associations/default/…` 226). All 11 appear in both renders with matching path segments, payload types and return unions.
- 33 `public type` declarations in `types.bal`; 33 typeDefs in both renders; name sets identical
  (set difference in both directions is empty).

## 4. Regressions

**None found.**

What was checked to conclude that:
- Full `diff -u old new` (10 hunks) reviewed line by line — every hunk is one of the three
  change classes in §2.
- Set difference of typeDef names between the two JSONs: empty in both directions.
- All 33 typeDefs compared field-by-field between the JSONs: the only field-level differences are
  the 8 `int:Signed32` type-name fixes; no field, description, optionality flag or default was
  dropped.
- All 11 client function objects compared whole between the JSONs: only the `get` function
  differed, and only by removal of the synthetic `Additional Values` parameter.
- `readme`, `description`, `name` strings compared: byte-identical between the two JSONs, so no
  README/section content was lost. Section markers 4 → 4.
- The one removed parameter is the only text `new` loses, and it was invalid Ballerina
  (an identifier containing a space, placed after defaulted parameters). Its removal makes the
  signature strictly closer to the source, not further from it.

## 5. Issues in `new` (independent of `old`)

All of the following are present identically in `old` — they are pipeline-wide rendering
limitations, not spec-v2 regressions. Listed because they can mislead an LLM consuming this render.

1. **Field defaults dropped; defaulted fields shown as optional.** Source
   `types.bal:376` is `int:Signed32 'limit = 500;` (a required field with a default of 500); both
   renders emit `int:Signed32 'limit?;`. Same pattern throughout `ConnectionConfig`: source has
   `httpVersion = http:HTTP_2_0`, `timeout = 30`, `forwarded = "disable"`, `cache = {}`,
   `compression = http:COMPRESSION_AUTO`, `responseLimits = {}`, `socketConfig = {}`,
   `validation = true`, `laxDataBinding = true` (`types.bal:171–212`); the render marks every one
   `?` with no value. Also `OAuth2RefreshTokenGrantConfig.refreshUrl` has default
   `"https://api.hubapi.com/oauth/v1/token"` (`types.bal:166`), rendered as `string refreshUrl?;`.
2. **Wrong default value on the `get` resource parameter.** Both renders show
   `int:Signed32 limit = 0`; the library's effective default is `500` (`types.bal:376`). An LLM
   reading this would generate a request with `limit=0`.
3. **Closed records rendered as open.** `ConnectionConfig`, `OAuth2RefreshTokenGrantConfig` and
   `ApiKeysConfig` are `record {| … |}` in the source (`types.bal:163, 171, 382`); both renders
   emit `record { … }`.
4. **`get` signature does not compile.** `new` renders
   `(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", GetObjects…Queries queries)`
   — a non-defaultable positional parameter after defaulted ones, and the included-record
   (`*`) parameter is expanded into its fields *and* also listed as a whole record, so `limit`
   and `after` appear twice in effect. Same shape in `old` (plus the extra bogus parameter).
5. **Doc-comment continuation line loses its `#` prefix.** `new:495` / `old:494`:
   `and absent fields are handled as `nilable` types. Enabled by default` sits at column 0 inside
   the `ConnectionConfig` body, breaking the surrounding record syntax.
6. **`public` / `isolated` modifiers stripped** from all types, the client class and all resource
   methods; the source declares them `public isolated`. Appears to be a deliberate render
   convention, applied equally on both sides.

No invented symbols, no wrong types (beyond the above), no encoding problems: all non-ASCII in
the README section (e.g. the curly apostrophe in "don't have one") round-trips correctly.

## 6. Coverage gaps vs. the library

**0 gaps.**

- The package exports exactly one module (`package.json` `"export": ["hubspot.crm.associations"]`;
  Central metadata lists a single module). It *is* the default module, so the
  `getDefaultModule()`-only extraction limitation costs nothing here. No submodule-only API.
- Public symbols in the default module: 33 `public type` (all in `types.bal`) +
  1 `public isolated client class Client` (`client.bal:23`). Both renders contain all 34.
- `utils.bal` contains no `public` declarations (grep for `^public` returned nothing in that
  file), so nothing is expected from it.
- No public constants, enums, annotations, listeners or module-level functions exist in the
  library, matching the empty `functions` / `services` / `annotations` arrays in both JSONs.

## 7. Compiler plugin

The package has **no compiler plugin**. There is no `compiler-plugin/`,
`*-compiler-plugin/` directory in the upstream repo at `v2.0.2`, no `[[plugin]]` /
`compilerPlugin` entry in `ballerina/Ballerina.toml`, and no `compiler-plugin/` directory or
`compiler-plugin.json` in the bala. Nothing plugin-derived is therefore expected in the render,
and nothing is missing on that account.

## 8. Other considerations

- This is a stable release (`2.0.2`), not deprecated: Central returns an empty
  `deprecateMessage` and no `deprecated: true` flag.
- Built with Ballerina `2201.12.2` (bala `package.json`), declared distribution `2201.12.0`
  (`Ballerina.toml`). `graalvmCompatible: true`.
- Sources are OpenAPI-tool generated ("AUTO-GENERATED FILE. DO NOT MODIFY."), which explains the
  wide record surface and the mechanically-named
  `GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries`.
- Size/token impact of spec v2 here is negligible: +1 line (682 vs 681). The 8 type-ref fixes
  actually shorten lines (`ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`), so token count
  likely drops slightly despite the added annotation line.
- Doc quality is good: every rendered record field and every client method carries a doc comment
  inherited from the source.
- The `// Special Agent Note: X FROM ballerina/http package` inline annotations for cross-package
  types are present and identical on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 681, new 682 |
| `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| `diff -u old new` | 10 hunks, +10/−9, all reviewed |
| `grep -c 'ballerina/lang'` old / new | 8 / 0 |
| `grep -nE '[a-z]+/[a-z.]+:[0-9]'` on new render | no matches (no version-qualified refs remain) |
| `grep -n '^// --- '` on new render | 4 markers: README 7, END README 220, Types 222, Client 638 |
| `grep -cE '^type '` new render | 33 |
| `grep -cE '^\s+resource function'` new render | 10 |
| Python JSON compare, top-level keys | `name`/`description`/`readme` byte-equal; typeDefs 33/33; clients 1/1; functions 0/0; services 0/0; annotations 0/0 |
| Python JSON compare, typeDef name sets | symmetric difference empty |
| Python JSON compare, typeDef contents | 8 type-name fixes + 1 added `annotations` key on `ConnectionConfig`; nothing else |
| Python JSON compare, all 11 client functions | only `get objects/…` differs; only the `Additional Values` param removed |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`472c6d7…`) |
| `git clone --depth 1 --branch v2.0.2` | succeeded |
| `diff -q` upstream `ballerina/{client,types,utils}.bal` vs bala module files | identical, all three |
| `cat ballerina/Ballerina.toml` | `version = "2.0.2"`, distribution `2201.12.0`, no plugin section |
| `grep -rn "@display"` in bala module | 1 hit: `types.bal:170` `@display {label: "Connection Config"}` |
| `grep -nE '^public (type\|isolated client class\|…)'` in bala module | 33 public types + 1 public client class |
| `grep -cE '^public type' types.bal` | 33 |
| `sed -n '374,379p' types.bal` | `'limit = 500;` confirmed (render shows `'limit?`, param default `0`) |
| `sed -n '203p' client.bal` | source `get` signature uses `*…Queries queries` |
| `ls -R` bala | modules/hubspot.crm.associations only; no compiler-plugin dir |
| `cat` bala `package.json` | `"export": ["hubspot.crm.associations"]` — single module |
| Central API `…/ballerinax/hubspot.crm.associations/2.0.2` | 1 module, ballerinaVersion 2201.12.2, empty deprecateMessage |
| `grep -n '^and absent fields'` both renders | old:494, new:495 — shared doc-comment defect |
| Precomputed `OLD_AND_NEW_DIFFS/hubspot.crm.associations_diff.md` | claims (681/682 lines, 10 hunks, 8→0 qualified refs, 0 decls added/removed) independently reproduced and confirmed |

## 10. Caveats and unverified items

- The renders were not compiled. Statements about non-compiling syntax (§5 items 4 and 5) are
  based on reading the Ballerina grammar rules, not on a `bal build` run — but they hold
  identically for `old` and `new`, so they do not affect the verdict.
- The effective runtime default of the `limit` query parameter is taken from the record field
  declaration `'limit = 500` (`types.bal:376`); the HubSpot API's own server-side default was not
  independently verified. This does not change the finding that the render's `limit = 0` does not
  match the library source.
- Central's package metadata was queried for deprecation/module list only; download counts,
  pull-request history and issue tracker were not reviewed.

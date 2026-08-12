# ballerinax/hubspot.crm.obj.contacts 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.contacts` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.contacts |
| Tag reviewed | `v1.0.2` (exact match; commit `aedd564b90041b94fd3607948e6fa2061c1b48fb`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.contacts/1.0.2` |
| Old render | `782` lines |
| New render | `783` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders are declaration-identical: 42 type definitions and 1 client class with 13 resource
functions plus `init` on both sides, same names, same order, README section byte-identical
(lines 1–181). The only differences are three renderer fixes, all improvements:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.obj.contacts:1.0.2:ValueWithTimestamp`, …) are now emitted as the plain
   `int:Signed32` / `ValueWithTimestamp` forms that actually appear in the library source. `old` 11,
   `new` 0.
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — present in the
   bala at `types.bal:231` and dropped entirely by `old` — is now rendered.
3. Three occurrences of the syntactically invalid parameter `anydata Additional Values` (the
   synthesised open-record rest field of the `*…Queries` included-record parameters) are removed.
   `old` 3, `new` 0.

Nothing was dropped, truncated, or made less accurate. Zero `// Unknown type:` placeholders on
either side. No coverage gap: all 42 public types and the single client exported by the default
module appear in both renders, and the package exports exactly one module.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 782 | 783 |
| `// --- ` section markers | 4 (README / END README / Types / Client) | 4 (same) |
| `// Unknown type:` | 0 | 0 |
| `type X …` declarations | 42 | 42 |
| `resource function` | 13 | 13 |
| top-level `function` / `enum` / `const` / `class` / `annotation` / `listener` | 0 | 0 |
| version-qualified type refs | 11 | 0 |
| `Additional Values` params | 3 | 0 |
| `@display` annotations | 0 | 1 |
| JSON `typeDefs` entries | 42 | 42 |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 |

**Declarations added: 0. Declarations removed: 0.** Verified by
`diff <(grep -oE '^type [A-Za-z0-9_]+' old|sort) <(… new|sort)` → empty, and by a sorted diff of all
non-comment, non-blank lines, whose *entire* output is the single line `> @display {label: "Connection Config"}`.

Modified (14 hunks, all inside existing declarations):

| Kind | Count | Detail |
|---|---|---|
| Type-reference normalisation, record fields | 11 | 7× `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`; 3× `record {\|ballerinax/…:1.0.2:ValueWithTimestamp[]...;\|}` → `record {\|ValueWithTimestamp[]...;\|}`; 1× same for `CollectionResponseAssociatedId` |
| Annotation added | 1 | `ConnectionConfig` gains `@display {label: "Connection Config"}` |
| Malformed parameter removed | 3 | `anydata Additional Values` dropped from `post batch/read`, `get [string contactId]`, `get ` |

The normalised JSON diff (`python3 -m json.tool --sort-keys`) contains exactly these three classes of
change and nothing else — 3 removed `"name": "Additional Values"` parameter objects, 11 changed
`"name"` type strings, 1 added `annotations` array on `ConnectionConfig`.

## 3. Correctness against library source

The bala's `modules/hubspot.crm.obj.contacts/{client,types,utils}.bal` are byte-identical to
`ballerina/{client,types,utils}.bal` at tag `v1.0.2` (`diff -q` → identical for all three), so GitHub
and bala agree and either can be cited.

Each of the 11 normalised type references was checked against `types.bal` in the bala:

| Render (new) | Source line | Source text |
|---|---|---|
| `AssociationSpec.associationTypeId` → `int:Signed32` | `types.bal:379` | `int:Signed32 associationTypeId?;` |
| `ValueWithTimestamp.updatedByUserId` → `int:Signed32` | `types.bal:176` | `int:Signed32 updatedByUserId?;` |
| `BatchResponse…WithErrors.numErrors` → `int:Signed32` | `types.bal:108` | `int:Signed32 numErrors?;` |
| `BatchResponse…numErrors` (2nd) | `types.bal:321` | `int:Signed32 numErrors?;` |
| `GetCrmV3ObjectsContactsGetPageQueries.'limit` | `types.bal:160` | `int:Signed32 'limit = 10;` |
| `PublicObjectSearchRequest.'limit` | `types.bal:293` | `int:Signed32 'limit?;` |
| `CollectionResponseWithTotal….total` | `types.bal:205` | `int:Signed32 total;` |
| `SimplePublicObject.propertiesWithHistory` | `types.bal:221` | `record {\|ValueWithTimestamp[]...;\|} propertiesWithHistory?;` |
| `SimplePublicUpsertObject.propertiesWithHistory` | `types.bal:393` | same |
| `SimplePublicObjectWithAssociations.propertiesWithHistory` | `types.bal:447` | same |
| `SimplePublicObjectWithAssociations.associations` | `types.bal:385` | `record {\|CollectionResponseAssociatedId...;\|} associations?;` |

All 11 match the source exactly. `new` is right, `old` was wrong (it embedded org/module/version into
the type name, which is not valid Ballerina and is noise for an LLM).

`@display {label: "Connection Config"}` is verified at `types.bal:230–231` of the bala, immediately
above `public type ConnectionConfig record {|`. `new` reproduces it verbatim.

The three removed `anydata Additional Values` parameters correspond to no source parameter. The three
affected resource functions in `client.bal` are:

- `client.bal:44` `resource isolated function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, *PostCrmV3ObjectsContactsBatchReadReadQueries queries)`
- `client.bal:63` `resource isolated function get [string contactId](map<string|string[]> headers = {}, *GetCrmV3ObjectsContactsContactIdGetByIdQueries queries)`
- `client.bal:196` `resource isolated function get .(map<string|string[]> headers = {}, *GetCrmV3ObjectsContactsGetPageQueries queries)`

`Additional Values` was a synthesised stand-in for the implicit `anydata...` rest field of the open
`*…Queries` records. It is not a real parameter, and `Additional Values` is not a legal Ballerina
identifier, so `old`'s signatures could never compile. No information is lost by removing it: the
openness of the three query records is still conveyed by their type definitions, which both renders
emit as open `record {` (render lines 453, 632, 716 in `new`).

Client surface: `grep -c 'resource function'` = 13 in both renders; `grep -c 'resource isolated function'`
in `client.bal` = 13. Names and paths line up one-for-one (`post batch/read`, `get [string contactId]`,
`delete [string contactId]`, `patch [string contactId]`, `post merge`, `post batch/archive`,
`post batch/create`, `post batch/update`, `post gdpr\-delete`, `get .`, `post .`, `post batch/upsert`,
`post search`).

## 4. Regressions

**None found.**

Checked to reach that conclusion:
- Sorted set-diff of every non-blank, non-doc line between the two files: the only line present in
  one and absent in the other is the *added* `@display` line. Nothing in `old` is absent from `new`
  except the three malformed `anydata Additional Values` fragments and the 11 over-qualified type
  names, both replaced by strictly more accurate text.
- Type-name set diff: empty both directions.
- README block (lines 1–181): `diff` → identical.
- Section markers: 4 on both sides, same order, offset by one line only because of the added
  annotation.
- JSON diff: no removed `typeDefs`, no removed client methods, no removed fields, no removed docs.
- Doc comments: every `#` doc line in `old` is present in `new` (the sorted line diff covers `#`-prefixed
  lines and reports no deletions).

## 5. Issues in `new` (independent of `old`)

All seven below are present identically in `old`; they are shared pipeline limitations, not new
defects, but they are inaccuracies against the library source that a consumer of `new` would hit.

1. **Wrong default value on `limit`.** Render line 770: `int:Signed32 limit = 0`. Source
   (`types.bal:160`) is `int:Signed32 'limit = 10;`. An LLM copying the render would use the wrong
   page size, and would also drop the required quoted-identifier form `'limit`.
2. **Invented defaults for optional fields.** Same line renders `string[] associations = []`,
   `string[] propertiesWithHistory = []`, `string after = ""`, `string[] properties = []`. In
   `types.bal:152–165` these fields are optional (`?`) with no default at all.
3. **Included-record parameter rendered twice and without `*`.** The `*…Queries queries` parameter is
   expanded into individual parameters *and* re-emitted as a plain parameter
   (`… , PostCrmV3ObjectsContactsBatchReadReadQueries queries)`). The result is a duplicated argument
   list and a required parameter positioned after defaulted ones — not compilable, and misleading
   about how the API is called.
4. **`get .` resource path lost.** `client.bal:196` is `resource isolated function get .(...)`; the
   render emits `resource function get (...)` with no path segment (render line 770). Same for
   `post .` at render line 774.
5. **Record-field defaults dropped in type definitions.** `boolean archived = false` (`types.bal:154`,
   `:355`, `:459`) renders as `boolean archived?`; `int:Signed32 'limit = 10` renders as
   `int:Signed32 'limit?`; `http:HttpVersion httpVersion = http:HTTP_2_0` (`types.bal:236`) renders as
   `http:HttpVersion httpVersion?`. Required-with-default becomes plain optional.
6. **`ConnectionConfig` closedness lost.** Source is `public type ConnectionConfig record {|` …
   (`types.bal:232`); render emits open `record {`.
7. **Blank line between doc comment and declaration.** e.g. render lines 521–524: the `#` doc line,
   a blank line, then `@display`/`type ConnectionConfig`. In Ballerina the doc must immediately
   precede the declaration, so as literal source these docs would not attach.

`isolated` on resource functions and `public` on type definitions are also dropped, but that appears
to be deliberate normalisation of the render format rather than an accuracy problem.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` (`any/package.json`) lists `"export": ["hubspot.crm.obj.contacts"]` — a single
  module, no submodules. `ls modules/` confirms one directory. So the `getDefaultModule()`-only
  extraction loses nothing here.
- Public types in the bala default module: 42 (`grep -oE '^public type …' types.bal | sort`).
  Types in `new`: 42. `comm -23` and `comm -13` between the two sorted lists are both empty — exact
  set equality.
- No other public declarations exist: `grep -nE '^public (const|enum|class|function|listener|annotation)'`
  across all three `.bal` files returns nothing (the client class is declared as `isolated client class Client`
  and is captured in the render's `Client` section).
- `utils.bal` contains only non-public helpers, so its absence from the render is correct.

## 7. Compiler plugin

The package ships no compiler plugin. `find` over the `v1.0.2` clone for `*compiler-plugin*` or
`CompilerPlugin.toml` returns nothing, and the bala contains no `compiler-plugin/` directory
(`ls any/` → `bala.json  dependency-graph.json  docs  modules  package.json`). Nothing plugin-derived
is therefore expected in, or missing from, the render.

## 8. Other considerations

- Version `1.0.2` is a stable release; `package.json` carries no `deprecated` / `deprecateMessage`
  field. Keywords: `Type/Connector`, `Area/CRM & Sales`, `Vendor/HubSpot`.
- Size is essentially unchanged (782 → 783 lines; JSON 2625 → 2607 pretty-printed lines), so no token
  budget impact. The removal of the 11 long qualified names slightly reduces token count per type
  reference.
- Doc quality is good: every rendered type field and every resource function carries a description
  sourced from the library.
- The `// Special Agent Note: X FROM ballerina/http package` trailer comments on `ConnectionConfig`
  fields are identical on both sides.
- The render is not compilable Ballerina on either side (see §5 items 3, 4, 7); `new` reduces but does
  not eliminate that — it fixes the `Additional Values` illegal identifier and the illegal
  `org/mod:ver:Type` references.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | 782 / 783 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old | 7, 180, 182, 726 |
| `grep -n '^// --- '` new | 7, 180, 182, 727 |
| `grep -cE '[a-z]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 11 / 0 |
| `grep -c 'Additional Values'` old / new | 3 / 0 |
| `grep -cE '^type [A-Za-z]'` old / new | 42 / 42 |
| `grep -c 'resource function'` old / new | 13 / 13 |
| `grep -cE '^(enum\|const\|class\|annotation\|listener\|public )'` old / new | 0 / 0 |
| `diff <(grep -oE '^type [A-Za-z0-9_]+' old\|sort) <(… new\|sort)` | empty |
| `diff <(grep -E '^[a-zA-Z@#]' old\|sort) <(… new\|sort)` | one line: `> @display {label: "Connection Config"}` |
| `diff <(sed -n '1,181p' old) <(sed -n '1,181p' new)` | identical (README block) |
| `diff <(json.tool --sort-keys old.json) <(… new.json)` | 3 removed `Additional Values` param objects, 11 changed type `name`s, 1 added `annotations` array |
| JSON top-level array lengths | `typeDefs` 42/42, `clients` 1/1, `functions` 0/0, `services` 0/0, `annotations` 0/0 |
| `git ls-remote --tags` on repo | tags `v0.1.0 v1.0.0 v1.0.1 v1.0.2`; `v1.0.2` → `aedd564b90041b94fd3607948e6fa2061c1b48fb` |
| `git clone --depth 1 --branch v1.0.2` | succeeded |
| `diff -q src/ballerina/{client,types,utils}.bal  bala/modules/…/` | all three IDENTICAL |
| `src/ballerina/Ballerina.toml:5` | `version = "1.0.2"` |
| `grep -n 'int:Signed32' bala types.bal` | lines 108, 160, 176, 205, 293, 321, 379 |
| `grep -n 'ValueWithTimestamp\[\]\.\.\.\|CollectionResponseAssociatedId\.\.\.' bala types.bal` | lines 221, 385, 393, 447 |
| `sed -n '228,236p' bala types.bal` | `@display {label: "Connection Config"}` at 231, `public type ConnectionConfig record {\|` at 232 |
| `grep -n 'resource isolated function' bala client.bal` | 13 matches (lines 44, 63, 79, 93, 110, 127, 144, 161, 178, 196, 212, 229, 246) |
| `sed -n '151,175p;352,375p;456,480p' bala types.bal` | three `*…Queries` records, all open (`record {`), defaults `archived = false`, `'limit = 10` |
| `grep -oE '^public type …' \| comm` vs render types | both `comm -23` and `comm -13` empty (42 = 42) |
| `grep -nE '^public (const\|enum\|class\|function\|listener\|annotation)' bala *.bal` | no matches |
| `find src -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no matches |
| `ls bala/any/` | `bala.json  dependency-graph.json  docs  modules  package.json` (no compiler-plugin) |
| `package.json` export / deprecated | `["hubspot.crm.obj.contacts"]` / absent |

## 10. Caveats and unverified items

- Ballerina Central metadata was not re-queried over the network; module list, export list and
  deprecation status were read from the bala's `any/package.json`, which is the artefact the
  extractor actually consumed and is authoritative for this comparison.
- The claim that these renders were produced from the two `ballerina-vscode` commits named in the
  brief is taken from the brief; it was not independently re-derived (no pipeline was re-run).
- `bala.json` records `built_by: WSO2` but no `ballerinaVersion` field is present in
  `any/package.json`, so the distribution version the package was built against was not verified.
- §5 items are judged against the library source; whether the render format *intends* to drop
  `public`/`isolated` and record defaults is a renderer-design question that was not confirmed
  against the renderer implementation.

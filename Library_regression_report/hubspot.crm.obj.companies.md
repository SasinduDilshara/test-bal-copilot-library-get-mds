# ballerinax/hubspot.crm.obj.companies 2.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.companies` |
| Pinned version | `2.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.companies |
| Tag reviewed | `v2.0.1` (tag `883b685b5e5bd2bd494330a505e161b1e4b4940a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.companies/2.0.1` |
| Old render | `648` lines |
| New render | `649` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders are structurally identical: same 4 section markers, same 42 record types, same
`Client` class with `init` + 12 resource functions, byte-identical README block, zero
`// Unknown type:` placeholders on both sides. The only differences (13 hunks, +16/−15 lines) are
three classes of change, all of which move `new` **closer** to the published source:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.obj.companies:2.0.1:ValueWithTimestamp`, …) collapse to the plain
   `int:Signed32` / `ValueWithTimestamp` spellings that the library source actually uses.
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — present in the
   source, dropped by `old` — is now emitted.
3. Four malformed `anydata Additional Values` pseudo-parameters (identifier containing a space →
   non-compiling Ballerina, and no such parameter exists in the library) are gone from `new`.

No declaration, parameter, return type, doc comment, or README line was lost. Nothing regressed.
A handful of accuracy problems remain in `new`, but every one of them is also present in `old`
(default values, closed-record `{|…|}` fidelity, included-record `*Queries` parameter expansion).

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 648 | 649 |
| Bytes | 24798 | 24409 |
| `// --- ` section markers | 4 | 4 |
| `// Unknown type:` | 0 | 0 |
| `type X record {` declarations | 42 | 42 |
| `client class` | 1 | 1 |
| Client functions (JSON) | 13 (`init` + 12 resource) | 13 (`init` + 12 resource) |
| Top-level `functions` / `services` / module `annotations` (JSON) | 0 / 0 / 0 | 0 / 0 / 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 11 | 0 |
| `@display` annotations | 0 | 1 |
| `Additional Values` pseudo-params | 4 | 0 |

Diff shape: 13 hunks, 16 added lines, 15 removed lines (`diff -u`, counted with
`grep -c '^+[^+]'` / `'^-[^-]'` / `'^@@'`).

**Declarations added: 0. Declarations removed: 0.** All change is *within* existing declarations.

Grouped by kind:

- **Types (10 hunks)** — 11 type-reference respellings across `GetCrmV3ObjectsCompaniesGetPageQueries`,
  `AssociationSpec`, `CollectionResponseSimplePublicObjectWithAssociationsForwardPaging` (via
  `SimplePublicObject*` records), `ValueWithTimestamp`, `BatchResponseSimplePublicUpsertObjectWithErrors`,
  `SimplePublicUpsertObject`, `CollectionResponseWithTotalSimplePublicObjectForwardPaging`,
  `PublicObjectSearchRequest`, `BatchResponseSimplePublicObjectWithErrors`,
  `SimplePublicObjectWithAssociations`; plus 1 annotation line added on `ConnectionConfig`.
- **Client (3 hunks)** — `anydata Additional Values` removed from `post companies/batch/read`,
  `get companies/[string companyId]`, `patch companies/[string companyId]`, `get companies`.
  (4 removals across 3 hunks; two are in the same hunk region.)
- **README** — identical on both sides (`diff` of lines 8–207 → no output).
- **JSON** — 60 changed lines total; deltas are exactly the 11 type-name strings, one added
  `annotations` block on `ConnectionConfig`, and four removed `Additional Values` parameter objects.
  `typeDefs` 42 on both, `clients` 1 on both, `readme`/`description`/`name` identical.

## 3. Correctness against library source

Upstream `v2.0.1` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's
`modules/hubspot.crm.obj.companies/{client,types,utils}.bal` (`diff` → IDENTICAL for all three), so
GitHub and the bala do not disagree here.

Verified for the things `new` changes:

- `int:Signed32` — source `types.bal:30` (`int:Signed32 'limit = 10;`), `:138`
  (`int:Signed32 updatedByUserId?;`), `:285` (`int:Signed32 associationTypeId?;`). `new` matches the
  source spelling exactly; `old`'s `ballerina/lang.int:0.0.0:Signed32` is a name no Ballerina program
  can write.
- `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}` — source
  `types.bal:286–294` (`SimplePublicObjectWithAssociations`). `new` reproduces the record body
  field-for-field, in source order; `old` embedded `ballerinax/hubspot.crm.obj.companies:2.0.1:` in
  the rest-descriptor type.
- `@display {label: "Connection Config"}` — source `types.bal:181`, immediately above
  `public type ConnectionConfig record {|` at `:182`. Correct annotation, correct target, correct value.
- Removal of `anydata Additional Values` — no parameter of that name exists in any of the 12 resource
  functions (`client.bal:47,66,82,97,115,132,149,166,184,200,217,232`). It was a rendering of the
  open-record rest descriptor of the `*…Queries` included-record parameter. Its removal loses nothing
  real and removes non-compiling text.

Spot checks of unchanged content against source (all exact matches):

- `ValueWithTimestamp` — render vs `types.bal:134–141`: 6 fields, same names/types/optionality.
- `ApiKeysConfig` — render vs `types.bal:348–351`: `privateAppLegacy`, `privateApp`, both required.
- Client surface — 12 resource functions in the render vs 12 in `client.bal`; accessors, resource
  paths, payload types and return unions match one-for-one (e.g. `post companies/search(...) returns
  CollectionResponseWithTotalSimplePublicObjectForwardPaging|error` = `client.bal:232`).
- `init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v3/objects")` =
  `client.bal:31`, including the default service URL.
- Query records `GetCrmV3ObjectsCompaniesCompanyIdGetByIdQueries` (`types.bal:55`),
  `PatchCrmV3ObjectsCompaniesCompanyIdUpdateQueries` (`types.bal:148`),
  `PostCrmV3ObjectsCompaniesBatchReadReadQueries` (`types.bal:229`) — field sets match the expanded
  parameters shown on the corresponding resource functions.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Declaration-set diff: sorted `type` names in `new` vs `public type` names in the bala's `types.bal`
  → identical, 42/42, no residue either way. Same set in `old`.
- Client function list from both JSONs → 13 vs 13, same accessors, same order, same return types.
- Parameter-level diff of both JSONs → the ONLY parameter objects removed in `new` are the four
  `Additional Values` entries; no real parameter, default, or description was dropped.
- README block (render lines 8–207) `diff old new` → no output; and vs the bala `docs/README.md`
  (199 lines) → 1 line of difference, a trailing blank line added by the renderer. No content loss.
- `// Unknown type:` count 0 → 0 (this library never had degraded types on either side).
- No section marker, doc comment, or `# +`-style description text appears in `old` and not in `new`
  (the 15 removed lines are exactly the 11 respelled type lines and the 4 `Additional Values` lines).

## 5. Issues in `new` (independent of `old`)

All four are shared with `old` — none is introduced by spec v2 — but they are real inaccuracies vs.
the library source and would mislead an LLM.

1. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:182`),
   `OAuth2RefreshTokenGrantConfig` (`:154`) and `ApiKeysConfig` (`:348`) are declared `record {| … |}`
   in the source; both renders emit `record { … };`. Callers are told they may add arbitrary fields.
2. **Default values dropped on `ConnectionConfig`.** Source fields with defaults —
   `httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}` (`types.bal:185–210`) — are all rendered as bare optional `?` fields with no
   default shown.
3. **Fabricated / wrong defaults on expanded query parameters.** `get companies` renders
   `int:Signed32 limit = 0`, but the source default is `'limit = 10` (`types.bal:30`). Optional
   fields with *no* default (`associations?`, `propertiesWithHistory?`, `after?`, `properties?`,
   `idProperty?`) are rendered with invented defaults `[]` / `""`. The quoted identifier `'limit` is
   also flattened to `limit`. The JSONs carry no `defaultValue` for any of these, so the renderer is
   synthesising them from the type.
4. **Included-record parameter expanded *and* duplicated.** Source uses
   `*GetCrmV3ObjectsCompaniesGetPageQueries queries` (`client.bal:184`, likewise `:47`, `:66`, `:97`).
   Both renders emit the record's fields as individual parameters **and** a trailing
   `GetCrmV3ObjectsCompaniesGetPageQueries queries` parameter. The `*` include marker is lost and the
   resulting signature is not valid Ballerina (a non-defaultable positional parameter follows
   defaultable ones, and the same data appears twice).

Note (not counted): both renders strip `public` and `isolated` everywhere
(`public isolated client class Client` → `client class Client`; `resource isolated function` →
`resource function`). This is a uniform renderer convention, not a per-library defect.

## 6. Coverage gaps vs. the library

**0 gaps.**

- The bala exports exactly one module: `package.json` `"export": ["hubspot.crm.obj.companies"]`,
  and `modules/` contains only `hubspot.crm.obj.companies`. There is **no submodule API**, so the
  shared `getDefaultModule()`-only limitation is a no-op for this library.
- Default-module public symbols in the bala: 42 `public type` declarations + 1
  `public isolated client class Client`. All 42 types appear in both renders (set diff → empty);
  `Client` appears in both.
- Everything in `utils.bal` (`SimpleBasicType`, `Encoding`, `enum EncodingStyle`, `defaultEncoding`,
  and 6 helper functions at lines 48/74/111/151/175/189) is module-private — correctly absent.
- No public constants, enums, annotations, listeners or services exist in the library; both renders
  report 0 for each in JSON. Nothing missing.

## 7. Compiler plugin

The library ships **no compiler plugin**. `find` over the `v2.0.1` clone for
`*compiler-plugin*` / `CompilerPlugin.toml` returns nothing, and the bala contains no
`compiler-plugin/` directory (bala root holds only `bala.json`, `dependency-graph.json`, `docs/`,
`modules/`, `package.json`). Nothing plugin-implied is therefore absent from the render.

## 8. Other considerations

- **Not deprecated.** Ballerina Central `2.0.1`: `deprecated: null`, `deprecateMessage: ""`,
  `pullCount: 38`, built with `2201.12.2` (`Ballerina.toml` declares `distribution = "2201.12.0"`).
- **Generated connector.** Header of `types.bal`: "AUTO-GENERATED FILE… by the Ballerina OpenAPI
  tool." Doc quality is inherited from the HubSpot OpenAPI spec — thorough on the query records,
  thin elsewhere (e.g. `post companies/search` has only `# + headers` / `# + return` and so renders
  with no summary line, which faithfully reflects the source).
- **Size/tokens.** `new` is 649 lines / 24409 bytes vs `old` 648 lines / 24798 bytes — one line
  longer but 389 bytes smaller, because the verbose `org/module:version:` prefixes shrink more than
  the added annotation line costs. A small net token win alongside the accuracy win.
- **Repo naming.** The manifest repo (`…-hubspot.crm.obj.companies`) and the `source_repository`
  recorded in the bala / `Ballerina.toml` (`…-hubspot.crm.object.companies`) differ, but
  `git ls-remote --tags` returns byte-identical tag→SHA lists for both URLs; they are the same
  repository (one redirects). No ambiguity in what was reviewed.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/… new/…` | 648 / 649 |
| `ls -la old new` | old 24798 B, new 24409 B (`.bal.txt`) |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; `Client` at 598 (old) / 599 (new) |
| `diff -u old new` | 13 hunks, +16 / −15 |
| `grep -cE '\b[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 11, new 0 |
| `grep -oE …` occurrence breakdown (old) | 7× `ballerina/lang.int:0.0.0:Signed32`, 3× `…:2.0.1:ValueWithTimestamp`, 1× `…:2.0.1:CollectionResponseAssociatedId` |
| `grep -c '@display'` | old 0, new 1 |
| `grep -c 'Additional Values'` | old 4, new 0 |
| `grep -cE '^type '` both renders | 42 / 42 |
| `grep -cE '^public type' bala types.bal` | 42 |
| `diff <(source type names sorted) <(new render type names sorted)` | empty → TYPE_SETS_IDENTICAL |
| `json.tool` diff of both JSONs | 60 changed lines; only the 11 type strings, 1 added `annotations` block, 4 removed `Additional Values` params |
| JSON key/array sizes | `typeDefs` 42/42, `clients` 1/1, `functions` 0/0, `services` 0/0, `annotations` 0/0, `readme`/`description`/`name` identical |
| JSON client function dump (new) | 13 functions: `init` + 12 resource (`post`×8, `get`×2, `delete`×1, `patch`×1) |
| `grep -nE 'function' bala client.bal` | `init` at :31 + 12 resource functions at :47,66,82,97,115,132,149,166,184,200,217,232 |
| JSON param dump for `get companies`, old vs new | identical except `Additional Values` present only in old; no `defaultValue` on any param on either side |
| `git ls-remote --tags` (both repo URLs) | v1.0.0, v2.0.0, v2.0.1 — identical SHAs; `v2.0.1^{}` = `883b685b…` |
| `git clone --depth 1 --branch v2.0.1` | OK → `<scratch>/src` |
| `diff src/ballerina/{client,types,utils}.bal` vs bala modules | IDENTICAL ×3 |
| `find src -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no matches |
| `cat bala package.json` | `export: ["hubspot.crm.obj.companies"]`, `ballerina_version 2201.12.2`, single module |
| `ls bala/any/modules` | one entry: `hubspot.crm.obj.companies` |
| `sed -n '178,215p' types.bal` vs render `ConnectionConfig` | `@display` matched; `record {|` → `record {`; 8 defaults dropped |
| `sed -n '286,300p;134,142p;348,357p' types.bal` vs render | `ValueWithTimestamp`, `SimplePublicObjectWithAssociations`, `ApiKeysConfig` bodies match field-for-field |
| `sed -n '55,67p;147,153p;228,233p' types.bal` | query-record field sets match the expanded resource-function params |
| `diff bala/docs/README.md <(sed -n '8,207p' new)` | 1 line (trailing blank added); `diff` of old vs new README block → identical |
| `curl api.central.ballerina.io/…/2.0.1` | `deprecated: null`, 1 module, pullCount 38 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that a rendered signature "does not compile" (old's
  `anydata Additional Values`; the duplicated `queries` parameter in both) are read off the Ballerina
  grammar, not from a `bal build` run — no Ballerina distribution was invoked in this review.
- The two renders were taken as given; the extraction pipeline was not re-run, so I cannot
  independently confirm the `old`/`new` source commits stated in the brief.
- `bala.json` was not read (only `package.json`, `dependency-graph.json` head, `docs/`, `modules/`);
  nothing in the review depends on it.
- Doc-comment text inside the render was compared to source only for the declarations spot-checked
  above and for every line touched by the diff, not exhaustively for all 42 types.

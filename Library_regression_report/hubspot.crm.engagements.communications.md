# ballerinax/hubspot.crm.engagements.communications 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.engagements.communications` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.engagements.communications |
| Tag reviewed | `v2.0.2` (exact match; `ballerina/types.bal` and `ballerina/client.bal` byte-identical to the bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.engagements.communications/2.0.2` |
| Old render | `772` lines |
| New render | `773` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module OpenAPI-generated HubSpot connector: 41 public types, 1 client class, 11 resource
methods + `init`. Both renders carry exactly the same declaration set — nothing added, nothing
removed. The 15 diff hunks are all fidelity fixes in `new`:

- 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
  `ballerinax/hubspot.crm.engagements.communications:2.0.2:ValueWithTimestamp`) collapsed to the
  correct source-level spelling (`int:Signed32`, `ValueWithTimestamp`). All 11 verified against the
  bala source.
- The library's single annotation, `@display {label: "Connection Config"}`, is emitted in `new` and
  was absent from `old`.
- A synthetic, non-compiling parameter `anydata Additional Values` (4 occurrences) is gone from `new`.

No regression found. Remaining inaccuracies are identical on both sides and pre-date spec v2.

## 2. Change inventory

Mechanical (verified, not copied from the precomputed diff):

| Metric | old | new |
|---|---|---|
| Total lines | 772 | 773 |
| `// --- section ---` markers | 4 | 4 |
| `// Unknown type:` placeholders | 0 | 0 |
| `^type` / `^public type` declarations | 41 | 41 |
| `client class` declarations | 1 | 1 |
| Client method declarations (`^    ... function`) | 12 | 12 |
| Annotation lines (`^@`) | 0 | 1 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 11 | 0 |
| `anydata Additional Values` params | 4 | 0 |
| JSON `typeDefs` entries | 41 | 41 |
| JSON `clients[0].functions` | 12 | 12 |
| JSON `functions` / `services` / `annotations` arrays | 0 / 0 / 0 | 0 / 0 / 0 |

**Declarations added: 0. Declarations removed: 0.**
`diff <(grep -oE '^(public )?type [A-Za-z0-9_]+' old|sort) <(… new|sort)` → empty (identical type
name sets). JSON `typeDefs` name sets compare equal (41 == 41). JSON `readme` and `description`
fields compare byte-equal between old and new.

Modifications, grouped:

| Kind | Count | Change |
|---|---|---|
| Record field type ref (int lang-lib) | 6 | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` |
| Record field type ref (self-module) | 5 | `ballerinax/hubspot.crm.engagements.communications:2.0.2:X` → `X` (inside `record {\|X…;\|}` rest types) |
| Type annotation | +1 | `@display {label: "Connection Config"}` added on `ConnectionConfig` |
| Client resource method signature | 4 | synthetic `anydata Additional Values` parameter dropped |

The 4 affected methods are exactly the 4 that take an included-record `*…Queries` parameter:
`post batch/read`, `get [string communicationId]`, `patch [string communicationId]`, `get` (dot).
In the `old` JSON the parameter is `{"name":"Additional Values","description":"Capture key value
pairs","type":{"name":"anydata"},"optional":true}` — a placeholder for the open-record rest field.
It is absent from the `new` JSON.

## 3. Correctness against library source

Every change in `new` was checked against
`…/bala/…/2.0.2/any/modules/hubspot.crm.engagements.communications/types.bal`:

| New render text | Bala source | Line |
|---|---|---|
| `int:Signed32 associationTypeId;` | `int:Signed32 associationTypeId;` | types.bal:380 |
| `int:Signed32 updatedByUserId?;` | `int:Signed32 updatedByUserId?;` | types.bal:183 |
| `int:Signed32 numErrors?;` (×2) | `int:Signed32 numErrors?;` | types.bal:131, 328 |
| `int:Signed32 total;` | `int:Signed32 total;` | types.bal:212 |
| `int:Signed32 'limit?;` (search req) | `int:Signed32 'limit?;` | types.bal:300 |
| `int:Signed32 'limit?;` (getPage queries) | `int:Signed32 'limit = 10;` | types.bal:360 — default lost, see §5 |
| `record {\|ValueWithTimestamp[]...;\|} propertiesWithHistory?;` (×3) | identical | types.bal:228, 394, 454 |
| `record {\|CollectionResponseAssociatedId...;\|} associations?;` | identical | types.bal:386 |
| `@display {label: "Connection Config"}` above `ConnectionConfig` | identical, directly above `public type ConnectionConfig` | types.bal:238 |

The 11 resource methods in the render match the 11 in `client.bal` (lines 47, 67, 84, 100, 118, 135,
152, 170, 186, 203, 220) by accessor, path and return type; `init` matches `client.bal:31`
including the `serviceUrl` default `"https://api.hubapi.com/crm/v3/objects/communications"`.

Dropping `anydata Additional Values` is correct behaviour: the `*Queries` records are open records,
but "the record is open" is not a positional parameter, and `Additional Values` is not a legal
Ballerina identifier. The `queries` record parameter it accompanied is still rendered on all 4
methods, so no user-callable API information was lost.

## 4. Regressions

**None found.**

What was checked to conclude that:
- Full `diff -u old new` reviewed hunk by hunk (15 hunks, +16/−15 lines); every hunk is one of the
  three improvement classes listed in §2.
- Sorted declaration-name sets identical (types, client class, client methods).
- JSON `typeDefs` name sets, `readme`, and `description` byte-identical between sides.
- Per-parameter comparison of the JSON for the most heavily changed method (`get` dot resource):
  old and new parameter lists are identical apart from the removed `Additional Values` entry — same
  names, same types, same defaults, same optionality.
- `// Unknown type:` count 0 on both sides; section marker count 4 on both sides; README block
  (lines 7–187) unchanged.
- No doc comment, default value, return type, or `// Special Agent Note:` line lost: 17 such notes
  in old, 17 in new.

## 5. Issues in `new` (independent of `old`)

All five are present identically in `old` — they are pipeline-wide, not spec-v2 regressions.

1. **Closed records rendered as open.** The bala declares 3 closed records
   (`OAuth2RefreshTokenGrantConfig` types.bal:197, `ConnectionConfig` types.bal:239,
   `ApiKeysConfig` types.bal:492, all `record {|`). The render emits `record {` for all 41 types
   (`grep -c '^type … record {|'` = 0, `record {$` = 41). Misleads an LLM into thinking arbitrary
   extra fields are allowed on the connection config.
2. **`public` / `isolated` qualifiers dropped.** All 41 types are `public type` in the bala; the
   render prints bare `type`. `public isolated client class Client` (client.bal:23) renders as
   `client class Client`, and `public isolated function init` renders as `function init`. The only
   `^public` line in the render is `public function main()` inside the README block.
3. **Wrong default on `limit`.** `GetCrmV3ObjectsCommunicationsGetPageQueries.'limit` is
   `int:Signed32 'limit = 10` (types.bal:360). The render shows `int:Signed32 'limit?;` in the type
   and `int:Signed32 limit = 0` in the expanded client signature. `0` appears in the JSON
   (`{"name":"limit","default":"0"}`) on both sides — an invented, incorrect default.
4. **Invented defaults on expanded query parameters.** `associations`, `propertiesWithHistory`,
   `properties` are optional-with-no-default in the source records but render as `= []`;
   `idProperty` renders as `= ""`. `archived = false` is the only one that matches the source.
   Also, `boolean archived = false` (source) renders as `boolean archived?;` inside the Queries
   record types — the record-level default is dropped while a synthesized one is added at the
   parameter level.
5. **Non-compiling dot-resource paths.** `resource isolated function get .(…)` and
   `post .(…)` (client.bal:170, 186) render as `resource function get (…)` / `resource function
   post (…)` — the `.` path segment is missing, which is not valid Ballerina.

## 6. Coverage gaps vs. the library

**None.**

- The bala contains exactly one module (`any/modules/hubspot.crm.engagements.communications`), which
  is the default module — so the `getDefaultModule()`-only extraction loses nothing here.
- `grep -cE '^public type ' types.bal` = 41; the render contains all 41.
  `comm -23 <bala public type names> <render type names>` → empty, and `comm -13` → empty
  (no invented types either).
- `utils.bal` defines 6 functions, all module-private (`isolated function …`, no `public`), so their
  absence is correct. No public module-level functions, constants, listeners, services, or
  annotations exist in the package (JSON `functions`/`services`/`annotations` arrays are empty on
  both sides, consistent with the source).

## 7. Compiler plugin

The package ships **no compiler plugin**: no `compiler-plugin/` directory in the bala
(`ls …/2.0.2/any/` → `bala.json, dependency-graph.json, docs, modules, package.json`), and
`find` for `*compiler-plugin*` in the v2.0.2 checkout returns nothing. `Ballerina.toml` declares no
`[[plugin]]` section. Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- Not deprecated. Central metadata for `ballerinax/hubspot.crm.engagements.communications/2.0.2`
  returns `deprecated: null`, `deprecateMessage: ""`, `ballerinaVersion: 2201.12.2`, one module.
- Version is stable (2.0.2, post-1.0).
- Size impact is negligible: +1 line (+0.13%).
- Doc quality is good — every record field and every resource method carries a doc comment, and the
  README block (180 lines) survives intact.
- Net effect for an LLM consumer: `new` is strictly easier to use — `int:Signed32` and
  `ValueWithTimestamp` are copy-pasteable where `ballerina/lang.int:0.0.0:Signed32` was not, and the
  bogus `anydata Additional Values` parameter can no longer be copied into generated code.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 772 / 773 |
| `diff -u old new` | 15 hunks, +16 / −15 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each (README 7, END README 187, Types 189, Client 724/725) |
| `grep -cE '^(public )?type ' ` old / new | 41 / 41 |
| `grep -cE '^(public )?(client )?class '` old / new | 1 / 1 |
| `grep -cE '^    (resource \|remote )?function '` old / new | 12 / 12 |
| `grep -cE '^@'` old / new | 0 / 1 |
| `diff <(grep -oE '^(public )?type \w+' old\|sort) <(… new\|sort)` | empty — identical type sets |
| JSON: `len(typeDefs)`, `len(clients[0].functions)` | 41/12 old, 41/12 new |
| JSON: sorted typeDef name sets equal | `True` |
| JSON: `readme` equal, `description` equal | `True`, `True` |
| JSON: `get` dot-resource parameter tuples old vs new | identical except removed `('Additional Values', None, 'anydata', True)` |
| `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2` → `v2.0.2` used |
| `git clone --depth 1 --branch v2.0.2` | success |
| `diff src/ballerina/types.bal bala/types.bal` | identical |
| `diff src/ballerina/client.bal bala/client.bal` | identical |
| `grep -n "function" bala/client.bal` | `init` @31 + 11 resource functions @47,67,84,100,118,135,152,170,186,203,220 |
| `grep -cE '^public type ' bala/types.bal` | 41 |
| `comm -23 bala_types render_types` / `comm -13` | empty / empty |
| `grep -n '^@' bala/types.bal bala/client.bal` | 1 hit: `types.bal:238 @display {label: "Connection Config"}` |
| `grep -n '^@' new render` | 1 hit: line 536, same text |
| `grep -cE '^public type \w+ record \{\|' bala/types.bal` | 3 (lines 197, 239, 492) |
| `grep -cE '^type \w+ record \{\|' render` old / new | 0 / 0 |
| `grep -n "'limit" bala/types.bal` | 300 (`'limit?`), 360 (`'limit = 10`) |
| `grep -rn "deprecated" bala/modules/…` | no hits |
| `ls bala/2.0.2/any/` and `find src -iname '*compiler-plugin*'` | no compiler plugin |
| `ls bala/2.0.2/any/modules/` | 1 module (default module only) |
| `grep -c "Special Agent Note"` old / new | 17 / 17 |
| Central API `…/ballerinax/hubspot.crm.engagements.communications/2.0.2` | version 2.0.2, `deprecated: null`, 1 module |

## 10. Caveats and unverified items

- The `@display` annotation is rendered in `new` with a blank line between the doc comment and the
  annotation (`# Provides a set of configurations…` / blank / `@display …` / `type ConnectionConfig`).
  In real Ballerina the annotation attaches directly under the doc. This is cosmetic and does not
  break parsing of the render as reference material, but I did not verify whether the renderer emits
  the same blank-line pattern for annotations elsewhere in the corpus.
- I did not compile either render; "non-compiling" claims in §5 (dot-resource paths, identifier with
  a space in `old`) are based on Ballerina grammar, not on a `bal build` run.
- The removed `Additional Values` parameter is judged to carry no user-facing API information because
  the `*Queries` records are open. I verified they are open (`record {`, types.bal:23, 49, 352, 438)
  but did not confirm the HubSpot API actually accepts arbitrary extra query parameters —
  that is an upstream-API question, not a render question.

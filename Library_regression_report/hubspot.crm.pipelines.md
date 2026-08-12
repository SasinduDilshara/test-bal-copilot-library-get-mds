# ballerinax/hubspot.crm.pipelines 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.pipelines` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.pipelines |
| Tag reviewed | `v2.0.2` (commit `1bb53eef024d77b4edff1b4508906d0e7ea04363`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.pipelines/2.0.2` |
| Old render | `469` lines |
| New render | `470` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders are declaration-for-declaration identical: 16 record types, 1 `client class Client`
with `init` + 14 resource functions, in both files. Nine diff hunks, all in `new`'s favour:

1. 8 occurrences of the version/module-qualified type ref `ballerina/lang.int:0.0.0:Signed32`
   became the correct `int:Signed32` (matches the bala source verbatim).
2. `@display {label: "Connection Config"}` is now emitted on `ConnectionConfig` — the annotation
   genuinely exists in the published source (`types.bal:192`); `old` dropped it.
3. A bogus synthetic parameter `anydata Additional Values` (an identifier with a space, i.e.
   non-compiling Ballerina) was removed from the three resource functions that take an included
   query record.

Nothing was lost. The README section, the client docs, every type and every field name is byte-wise
unchanged apart from those three improvements. No regression found.

## 2. Change inventory

Line counts: `old` 469, `new` 470 (`wc -l`). 9 hunks, +12 / −11 lines.

| Kind | old | new | added | removed | modified |
|---|---|---|---|---|---|
| `type` (record) declarations | 16 | 16 | 0 | 0 | 8 field type refs across 7 types + 1 annotation |
| `client class` | 1 | 1 | 0 | 0 | 3 resource signatures |
| `resource function` | 14 | 14 | 0 | 0 | 3 |
| `function init` | 1 | 1 | 0 | 0 | 0 |
| `enum` / `const` / `annotation` / `service` / `listener` | 0 | 0 | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | — | — | — |
| `// --- section ---` markers | 4 | 4 | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:T`) | 8 | 0 | — | −8 | — |

Sorted type-name sets are identical between the two renders (`diff` of extracted `^type <Name>`
lists returned no output; 16 names each).

Modified declarations, exactly:

| Type | Field | old | new |
|---|---|---|---|
| `PipelineStagePatchInput` | `displayOrder?` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `PipelinePatchInput` | `displayOrder?` | same | `int:Signed32` |
| `PipelineStage` | `displayOrder` | same | `int:Signed32` |
| `PublicAuditInfo` | `fromUserId?` | same | `int:Signed32` |
| `PublicAuditInfo` | `portalId` | same | `int:Signed32` |
| `Pipeline` | `displayOrder` | same | `int:Signed32` |
| `PipelineStageInput` | `displayOrder` | same | `int:Signed32` |
| `PipelineInput` | `displayOrder` | same | `int:Signed32` |
| `ConnectionConfig` | — | (no annotation) | `@display {label: "Connection Config"}` |

Client changes (all three: drop of `anydata Additional Values`):
`put [objectType]/[pipelineId]`, `delete [objectType]/[pipelineId]`,
`patch [objectType]/[pipelineId]`.

JSON level (`old/*.json` vs `new/*.json`, 64,790 vs 64,053 bytes): `readme`, `description`,
`annotations` (`[]`), `functions` (`[]`), `services` (`[]`) are equal; `typeDefs` 16 vs 16 with the
same names; `clients[0].functions` 15 vs 15. The only JSON deltas are the 8 `Signed32` type refs,
a new `annotations` key on the `ConnectionConfig` typeDef, and the removal of the parameter
`{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`
from the three functions above.

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/types.bal` and `ballerina/client.bal` are **byte-identical** to the
bala's `modules/hubspot.crm.pipelines/types.bal` and `client.bal` (`diff` returned nothing), so
GitHub and the bala agree; no tie-break needed.

- `int:Signed32` — the bala source uses exactly `int:Signed32` at `types.bal:33,43,63,103,105,137,157,165`
  (8 occurrences, matching the 8 render sites 1:1). `new` is correct; `old` was wrong.
- `@display {label: "Connection Config"}` — present at `types.bal:192`, immediately above
  `public type ConnectionConfig record {|` (`types.bal:193`). `new` is correct; `old` omitted it.
  It is the only annotation in the whole package (`grep '@display\|@constraint\|@deprecated'` over
  `*.bal` returns only this one line).
- `Additional Values` — no such parameter exists anywhere in `client.bal`. The three affected
  resource functions declare an *included record* param:
  `client.bal:89` `resource isolated function put [string objectType]/[string pipelineId](PipelineInput payload, map<string|string[]> headers = {}, *PutCrmV3PipelinesObjectTypePipelineIdReplaceQueries queries)`,
  and likewise `client.bal:111` (delete) and `client.bal:130` (patch). The synthetic param in `old`
  was the extractor surfacing the open-record rest descriptor of those query records; removing it is
  correct.
- All 14 resource functions and `init` in the render match `client.bal` lines 36, 54, 71, 89, 111,
  130, 151, 168, 185, 204, 220, 241, 259, 280, 298 by accessor, resource path and return type.
- Field-level check, scripted: for 15 of the 16 types the render's field-name set equals the bala
  source's field-name set exactly. The 16th, `OAuth2RefreshTokenGrantConfig`, has 9 extra fields in
  the render (`refreshToken`, `clientId`, `clientSecret`, `scopes`, `defaultTokenExpTime`,
  `clockSkew`, `optionalParams`, `credentialBearer`, `clientConfig`) — these are the inherited
  members of `*http:OAuth2RefreshTokenGrantConfig` (`types.bal:180`) expanded inline. Correct
  expansion, and identical in `old` (render lines 339–349 in both files).

## 4. Regressions

**None found.**

What was checked to conclude this:
- Extracted and sorted the `^type <Name>` declaration sets from both renders — identical (16/16).
- `grep -c 'resource function'` — 14 in both.
- Full `diff -u old new` reviewed hunk by hunk (9 hunks, all listed in §2); every hunk is either a
  type-ref correction, an annotation addition, or removal of a fabricated parameter.
- JSON comparison at object level: `readme` identical (6,997 chars both sides, equal to the bala's
  `docs/README.md` byte count), `description` identical, `clients[0].functions` 15 vs 15, `typeDefs`
  16 vs 16 with identical names; no field, doc string, or return type was dropped.
- No parameter, default value, or doc line present in `old` is absent from `new` other than the
  fabricated `anydata Additional Values`.

One nuance worth recording (not a regression): by dropping `Additional Values`, `new` no longer
signals that the three `*Queries` records are **open** records that accept extra query parameters.
That information was only ever conveyed through a non-compiling identifier-with-a-space, and the
render still shows the `*Queries` record type by name, so the net effect is an improvement.

## 5. Issues in `new` (independent of `old`)

All of the following are present in `new`; all are also present in `old`, so they are pre-existing
renderer behaviour rather than spec-v2 regressions. They matter because they can mislead an LLM.

1. **Closed records rendered as open.** `OAuth2RefreshTokenGrantConfig`, `ApiKeysConfig` and
   `ConnectionConfig` are `record {| ... |}` in the source (`types.bal:179, 186, 193`) but are
   rendered as `record { ... }` (new lines 339, 355, 362). The three inline `record {|string...;|}`
   metadata fields survive, so the renderer can emit `{|` — it just doesn't for named types.
2. **Default values dropped; defaulted fields become optional.** E.g. `http:HttpVersion httpVersion = http:HTTP_2_0`
   → `http:HttpVersion httpVersion?`; `decimal timeout = 30` → `decimal timeout?`;
   `string refreshUrl = "https://api.hubapi.com/oauth/v1/token"` → `string refreshUrl?`;
   `boolean validateDealStageUsagesBeforeDelete = false` → `boolean validateDealStageUsagesBeforeDelete?`
   (new:278). An LLM cannot learn the defaults from this render.
3. **Non-compiling doc continuation.** New line 401 is
   `and absent fields are handled as `nilable` types. Enabled by default` — a wrapped documentation
   line emitted without its leading `#`, so the block would not parse. (old:400, identical.)
4. **Included-record params rendered twice and out of order.** `*PutCrmV3...Queries queries` becomes
   `..., boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, PutCrmV3...Queries queries`
   (new:424) — the fields are flattened *and* the record is repeated as a trailing param, with a
   non-defaulted param after defaulted ones. Not valid Ballerina and ambiguous to a reader.
   Same in `old` plus the extra bogus param.
5. **Qualifiers dropped.** `public isolated function init` → `function init`; every
   `resource isolated function` → `resource function`. Identical in both renders.

## 6. Coverage gaps vs. the library

**None.** The package exports exactly one module — `package.json` `"export": ["hubspot.crm.pipelines"]`,
and `modules/` contains only `hubspot.crm.pipelines`, which is the default module. Central metadata
for `2.0.2` lists a single module. So there is no submodule-only API and no shared submodule gap.

Public symbols in the default module: 16 `public type` declarations (`types.bal` lines 23, 39, 49,
75, 83, 89, 97, 115, 121, 129, 149, 163, 173, 179, 186, 193) and `public isolated client class Client`.
`utils.bal` declares no public symbols (`grep -nE '^public ' utils.bal` → no output). All 16 type
names appear in both renders (set `diff` empty), and `Client` with all 15 of its functions appears
in both. No public constants, enums, annotations, listeners or module-level functions exist to miss.

## 7. Compiler plugin

The package has **no compiler plugin**. `find` for `*compiler-plugin*` / `*native*` under the
upstream clone returns nothing; the bala has no `compiler-plugin/` directory (its `any/` contains
only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived
is therefore expected in, or missing from, the render.

## 8. Other considerations

- Not deprecated: Central returns `"deprecated": null`, `"deprecateMessage": ""`.
- Stable major version (`2.0.2`), built with Ballerina `2201.12.2`. Pull count 21 (young package).
- Size is small and stable: 469 → 470 lines, JSON 64.8 KB → 64.1 KB. The `new` render is slightly
  cheaper in tokens (`ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` alone saves ~8 × 6 tokens)
  while being more accurate.
- README fidelity is good: the render's README block (new lines 8–163) is identical to the bala's
  `docs/README.md` (155 lines) plus one trailing blank line — no truncation, and identical in `old`.
- `// Special Agent Note: <T> FROM ballerina/http package` annotations on cross-package types are
  present and unchanged in both renders.
- Note for downstream consumers: the render's type section resolves `int:Signed32` but the render
  never emits an `import ballerina/lang.'int;` — this is the normal implicit lang-lib import, so it
  is fine.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 469 / 470 |
| `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| `grep -n '^// --- '` both renders | 4 markers each (README, END README, Types, Client) |
| `diff -u old new` | 9 hunks, +12/−11, all reproduced in §2 |
| `grep -c 'resource function'` both renders | 14 / 14 |
| `diff` of sorted `^type <Name>` lists | no output (16 identical names) |
| `grep -oE '^public type \w+' bala/types.bal` vs render type list | identical sets — "ALL 16 TYPES PRESENT" |
| `grep -n 'function' bala/client.bal` | `init` at :36 + 14 resource functions at :54,71,89,111,130,151,168,185,204,220,241,259,280,298 |
| `grep -n 'int:Signed32' bala/types.bal` | 8 hits: lines 33, 43, 63, 103, 105, 137, 157, 165 |
| `grep -n '@display\|@constraint\|@deprecated' bala/*.bal` | one hit: `types.bal:192 @display {label: "Connection Config"}` |
| `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2`; used `v2.0.2` → `1bb53eef…` |
| `git clone --depth 1 --branch v2.0.2` then `diff src/ballerina/types.bal bala/.../types.bal` | IDENTICAL_TYPES |
| same for `client.bal` | IDENTICAL_CLIENT |
| `grep version src/ballerina/Ballerina.toml` | `version = "2.0.2"` |
| `find src -iname '*compiler-plugin*'` | no results |
| `ls bala/2.0.2/any` and `.../modules` | `bala.json, dependency-graph.json, docs, modules, package.json`; single module `hubspot.crm.pipelines` |
| `package.json` | `export: ["hubspot.crm.pipelines"]`, `ballerina_version: 2201.12.2`, `template: false` |
| `curl api.central.ballerina.io/.../2.0.2` | `deprecated: null`, 1 module, pullCount 21 |
| Python JSON compare (top-level keys, typeDefs, clients) | readme/description/annotations/functions/services equal; only Signed32 refs, `ConnectionConfig.annotations`, and 3 dropped params differ |
| Python JSON param diff on `clients[0].functions` | `Additional Values` dropped from `put`, `delete`, `patch`; no other param change |
| Python field-set compare, 16 types, bala source vs `new` render | 15/16 exact match; `OAuth2RefreshTokenGrantConfig` has 9 extra inherited fields from `*http:OAuth2RefreshTokenGrantConfig` (also in `old`) |
| `diff <(sed -n '8,163p' new render) bala/docs/README.md` | only a trailing blank line differs |
| `wc -c bala/docs/README.md` vs JSON `readme` length | 6,997 / 6,997, equal on both sides |
| `grep -n '^and absent fields' old new` | old:400, new:401 — doc continuation without `#`, both sides |
| `grep -c 'record {|' old new` | 3 / 3 (inline metadata records only; named closed records rendered open on both sides) |
| `OLD_AND_NEW_DIFFS/hubspot.crm.pipelines_diff.md` | every figure (469/470, +12/−11, 9 hunks, 8→0 qualified refs, 0 decls added/removed) independently reproduced |

## 10. Caveats and unverified items

- The renders were not compiled. Statements about non-compiling constructs (§5 items 3 and 4, and
  the `anydata Additional Values` identifier) are based on Ballerina grammar reading, not a
  `bal build` run — I did not attempt to compile the `.bal.txt` files, which are not intended to be
  compilable artefacts anyway.
- I did not run the two-stage pipeline myself; I audited the committed `old`/`new` renders and JSONs
  as given. The claim that both sides used the same pinned bala rests on the brief's `PIN_OK` and on
  the fact that both JSONs carry identical `readme` and `description` payloads matching the 2.0.2
  bala.
- Central's `modules[0].readme` and `summary` are empty strings in the registry response; I used the
  bala's `docs/README.md` as the authority for README content instead.

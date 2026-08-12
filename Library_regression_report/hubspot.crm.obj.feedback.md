# ballerinax/hubspot.crm.obj.feedback 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.feedback` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.feedback |
| Tag reviewed | `v2.0.2` (exact match, commit `dca95d5`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.feedback/2.0.2` |
| Old render | `780` lines |
| New render | `781` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module OpenAPI-generated HubSpot connector: one `Client` class (init + 11 resource
functions) and 41 public record types, no compiler plugin, no submodules. The `new` render is
byte-identical to `old` except for three classes of change, all of which are corrections:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.obj.feedback:2.0.2:ValueWithTimestamp`) normalized to the real source
   spellings `int:Signed32` / `ValueWithTimestamp`.
2. 4 occurrences of the malformed synthetic parameter `anydata Additional Values` (an identifier
   containing a space — not valid Ballerina) dropped from the client resource-function signatures.
3. `@display {label: "Connection Config"}` on `ConnectionConfig` now emitted; it exists in the
   library source and was silently dropped by `old`.

No declaration, field, parameter, default, doc line or README byte was lost. Zero regressions.
The inaccuracies that remain in `new` (Section 5) are all present identically in `old`.

## 2. Change inventory

Line counts (`wc -l`): old 780, new 781 (+1, the `@display` line).

| Kind | old | new | Δ |
|---|---|---|---|
| `type` declarations | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| Client functions (JSON `clients[0].functions`) | 12 | 12 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Annotation lines (`^@`) | 0 | 1 | +1 |
| Version-qualified type refs | 11 | 0 | −11 |
| `anydata Additional Values` params | 4 | 0 | −4 |
| Empty `#` doc continuation lines | 11 | 11 | 0 |

Declarations added: **0**. Declarations removed: **0**.
Type-name sets identical (`diff` of sorted `^type <Name>` extractions: no output).
Client function key sets identical (accessor+path), verified from both JSONs.

Modified declarations — 11 record fields, type reference only (JSON `typeDefs[].fields[].type.name`):

| Type | Field | old type | new type |
|---|---|---|---|
| `AssociationSpec` | `associationTypeId` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `ValueWithTimestamp` | `updatedByUserId` | same | `int:Signed32` |
| `BatchResponseSimplePublicObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `BatchResponseSimplePublicUpsertObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `CollectionResponseWithTotalSimplePublicObjectForwardPaging` | `total` | same | `int:Signed32` |
| `GetCrmV3ObjectsFeedbackSubmissionsGetPageQueries` | `'limit` | same | `int:Signed32` |
| `PublicObjectSearchRequest` | `'limit` | same | `int:Signed32` |
| `SimplePublicObject` | `propertiesWithHistory` | `record {\|ballerinax/hubspot.crm.obj.feedback:2.0.2:ValueWithTimestamp[]...;\|}` | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicUpsertObject` | `propertiesWithHistory` | same pattern | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `propertiesWithHistory` | same pattern | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `associations` | `record {\|…:2.0.2:CollectionResponseAssociatedId...;\|}` | `record {\|CollectionResponseAssociatedId...;\|}` |

Modified client functions — 4 signatures, parameter removal only:
`post batch/read`, `get [feedbackSubmissionId]`, `patch [feedbackSubmissionId]`, `get .` each lost
the parameter `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`.

Added metadata — `typeDefs["ConnectionConfig"].annotations = [{"name":"display","value":"{label: \"Connection Config\"}"}]` (key absent in `old`).

README block (render lines 1–196) is byte-identical between the two sides.

## 3. Correctness against library source

GitHub `v2.0.2` and the bala are byte-identical for all three source files:
`diff` of `client.bal`, `types.bal`, `utils.bal` (bala `modules/hubspot.crm.obj.feedback/` vs repo
`ballerina/`) → IDENTICAL for all three. So both sources agree; either is authoritative.

**Type inventory.** Parsed all `public type … record` blocks out of `types.bal` (41) and compared
type names and field-name sets against `new`'s JSON `typeDefs`:
- types missing from render: none
- types invented by render: none
- field-set mismatches: 1 — `OAuth2RefreshTokenGrantConfig`, which is `record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl = "…"; |}` (`types.bal:177-181`). The render **flattens the type inclusion** and lists the 9 inherited `oauth2` fields plus `refreshUrl` (new render lines 475–487). That is an enrichment, correct against the included type, and identical in `old`.

**The three changed constructs verified against source:**
- `int:Signed32` — `types.bal:374` (`AssociationSpec.associationTypeId`), `types.bal:158` (`ValueWithTimestamp.updatedByUserId`), `types.bal:193` (`…ForwardPaging.total`), `types.bal:277` (`GetPageQueries.'limit`), `types.bal:296` (`PublicObjectSearchRequest.'limit`). Source writes `int:Signed32`; `new` matches exactly, `old` did not.
- `record {|ValueWithTimestamp[]...;|}` and `record {|CollectionResponseAssociatedId...;|}` — `types.bal:389` and `types.bal:386` inside `SimplePublicObjectWithAssociations`. `new` matches the source text verbatim.
- `@display {label: "Connection Config"}` — `types.bal:218`, directly above `public type ConnectionConfig record {|`. `new` reproduces it verbatim.

**Removal of `anydata Additional Values` is correct.** The 4 affected resource functions are the
only ones taking an included-record parameter: `client.bal:47` `*PostCrmV3ObjectsFeedbackSubmissionsBatchReadReadQueries queries`,
`client.bal:67` `*GetCrmV3…GetByIdQueries queries`, `client.bal:100` `*PatchCrmV3…Queries queries`,
`client.bal:170` `*GetCrmV3…GetPageQueries queries`. Those Queries records are open records
(`record { … }`, e.g. `types.bal:268`, `types.bal:348`, `types.bal:378`, `types.bal:470`), so `old`
was materializing their implicit `anydata` rest descriptor as a positional parameter literally named
`Additional Values`. No such parameter exists in the source, and the name is not a valid Ballerina
identifier. Dropping it is a correctness fix.

**Client surface.** `client.bal` declares `init` (line 31) and 11 resource functions (lines 47, 67,
84, 100, 118, 135, 152, 170, 186, 203, 220). Both renders carry exactly those 12, with matching
accessors and resource paths (`batch/read`, `[feedbackSubmissionId]`, `batch/archive`,
`batch/create`, `batch/update`, `batch/upsert`, `search`, and the two `.` paths). `init`'s
`serviceUrl` default `"https://api.hubapi.com/crm/v3/objects/feedback_submissions"` matches
`client.bal:31`.

**Module-private types correctly excluded.** `utils.bal:23 SimpleBasicType`, `utils.bal:26 Encoding`,
`utils.bal:37 enum EncodingStyle` carry no `public` qualifier and appear in neither render — correct.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff` of sorted `^type <Name>` extractions from the two renders: no output → no type lost.
- JSON `typeDefs` name-set equality → True; per-type key diff shows only `annotations` **added** to `ConnectionConfig`, never removed.
- Per-type, per-field JSON comparison: field-name sets identical for all 41 types; only 11 `type.name` strings differ, all in the direction of the source spelling.
- Per-function parameter comparison over `clients[0].functions`: only removals are the 4 `Additional Values` entries; no real parameter, default, or return type dropped (`CHANGED` set empty).
- Render lines 1–196 (header + README) `diff` → identical.
- `grep -c '^// Unknown type:'` → 0 on both sides.
- `grep -c '^    # $'` → 11 on both sides (no doc line lost).
- Net line delta +1 is fully accounted for by the single `@display` line.

## 5. Issues in `new` (independent of `old`)

All eight below are present **identically in `old`** — they are renderer-level limitations, not
regressions introduced by spec v2. Listed because they are inaccuracies an LLM consumer would see.

1. **Included-record parameters double-rendered.** `client.bal:170` is
   `resource isolated function get .(map<string|string[]> headers = {}, *GetCrmV3ObjectsFeedbackSubmissionsGetPageQueries queries)`.
   New render line 768 emits both the flattened query fields **and** a trailing
   `GetCrmV3ObjectsFeedbackSubmissionsGetPageQueries queries` parameter, and drops the `*`. The
   signature is ambiguous and would not compile. Same for lines 740, 744, 752.
2. **Wrong default value.** Source `types.bal:277` is `int:Signed32 'limit = 10;`; render line 768
   emits `int:Signed32 limit = 0`. Both the value and the quoted-identifier form are wrong.
3. **Invented defaults for optional fields.** `associations?`, `propertiesWithHistory?`,
   `properties?`, `after?`, `idProperty?` are optional with no default in `types.bal:270-282` /
   `types.bal:349-360`, but the render gives them `= []` / `= ""` (lines 744, 752, 768).
4. **Required-with-default fields turned optional in the type defs.** `boolean archived = false;`
   (`types.bal:272`, `:352`, `:472`) renders as `boolean archived?;` (e.g. line 730, 582). Likewise
   every `ConnectionConfig` field with a default (`httpVersion = http:HTTP_2_0`, `timeout = 30`,
   `forwarded = "disable"`, `validation = true`, `laxDataBinding = true`) renders as `?` with the
   default erased (lines 524-565).
5. **Closed-record syntax lost.** `types.bal` has 3 top-level `record {| … |}` types
   (`ConnectionConfig`, `OAuth2RefreshTokenGrantConfig`, `ApiKeysConfig`); the render emits 0
   top-level `record {|` — all three become open `record {` (lines 523, 475, 567). Inline closed
   records inside fields are preserved (19 occurrences).
6. **`.` resource path rendered as empty.** `resource isolated function get .` / `post .`
   (`client.bal:170`, `:186`) render as `resource function get (` / `resource function post (`
   (lines 768, 772) — non-compiling and ambiguous against the `[path]` variants.
7. **Parameter/return doc comments dropped.** Source functions carry `# + headers - …`,
   `# + queries - …`, `# + return - …` (e.g. `client.bal:43-46`); the render keeps only the summary
   and leaves 11 dangling empty `# ` lines.
8. **Qualifiers dropped.** `public isolated client class Client` → `client class Client`;
   `public isolated function init` → `function init`; `resource isolated function` → `resource function`.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

`package.json` `export` lists exactly one module: `hubspot.crm.obj.feedback`. `bala .../modules/`
contains only that directory. There is no submodule API, so the known `getDefaultModule()`-only
limitation does not bite here.

Public symbols in the default module: 41 `public type` + 1 `public isolated client class Client`
(with `init` + 11 resource functions). All 41 types and all 12 client functions appear in both
renders (verified by set comparison in Section 3). There are no `public const`, `public function`,
`public enum`, `public annotation`, `public listener`, or `service` declarations in the module
(`grep -nE '^public (const|function|isolated function|enum|annotation|listener|service|class)' *.bal`
returned only `client.bal:23` for the client class). `services`, `functions` and `annotations` are
empty arrays in both JSONs — correct.

## 7. Compiler plugin

**No compiler plugin exists.** `Ballerina.toml` (repo `ballerina/Ballerina.toml`) has no
`[[platform.*.dependency]]` or `CompilerPlugin` entry; the repo tree at `v2.0.2` has no
`compiler-plugin/` directory; and `find` over the bala for `*compiler*` returned nothing (the bala
contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`).
Nothing plugin-derived is therefore expected in, or missing from, the render.

## 8. Other considerations

- Version is stable (2.0.2, post-1.0). `package.json` shows no deprecation flag; keywords
  `Type/Connector`, `Area/CRM & Sales`, `Vendor/HubSpot`; `graalvmCompatible: true`.
- Sources are marked `// AUTO-GENERATED FILE. DO NOT MODIFY. … Ballerina OpenAPI tool`
  (`client.bal:1-2`), which explains the machine-shaped `…Queries` records and the doc style.
- Size impact is negligible: JSON 87,969 B → 86,851 B (−1.3%); render 780 → 781 lines. The new
  render is slightly cheaper in tokens despite the extra line, because the long
  `ballerinax/hubspot.crm.obj.feedback:2.0.2:` prefixes are gone.
- Doc quality is good: every public record field carries a `#` description in both renders.
- The `// Special Agent Note: X FROM ballerina/http package` trailing comments (for `http:*` and
  `oauth2:*` references) are present and unchanged on both sides.
- Neither render is compilable Ballerina as-is (Section 5 items 1, 6). That is a pre-existing
  property of this renderer for OpenAPI-generated connectors, unchanged by spec v2.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 780 / 781 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; `Client` at 732 (old) / 733 (new) |
| `grep -n '^@'` both | old: none; new: line 522 `@display {label: "Connection Config"}` |
| `diff` of sorted `^type <Name>` sets | no output — TYPES IDENTICAL (41 each) |
| `diff` of `bala_types` vs `new_types` | no output — render covers all 41 public source types |
| `diff` of function lines old vs new | 4 hunks, all `anydata Additional Values` removals |
| `grep -c 'anydata Additional Values'` | old 4, new 0 |
| Python JSON top-level key/array compare | `typeDefs` 41/41, `clients` 1/1, `services` 0/0, `functions` 0/0, `annotations` 0/0 |
| Python per-type JSON diff | 11 types differ; only `ConnectionConfig` gains a key (`annotations`) |
| Python per-field JSON diff | 11 fields, `type.name` only; field-name sets identical everywhere |
| Python per-client-function param diff | 4 × removal of `Additional Values`; no other param change |
| `wc -c` on both JSONs | 87,969 → 86,851 bytes |
| `diff` render lines 1–196 | identical (README + header) |
| `grep -c '^    # $'` | 11 / 11 |
| `git ls-remote --tags` | `v2.0.2` → `dca95d5` (annotated) |
| `git clone --depth 1 --branch v2.0.2` | succeeded |
| `diff` bala `client.bal`/`types.bal`/`utils.bal` vs repo `ballerina/` | IDENTICAL ×3 |
| `types.bal:218` | `@display {label: "Connection Config"}` present in source |
| `types.bal:374, 158, 193, 277, 296` | `int:Signed32` in source |
| `types.bal:386, 389` | `record {\|CollectionResponseAssociatedId...;\|}`, `record {\|ValueWithTimestamp[]...;\|}` |
| `types.bal:177-181` | `OAuth2RefreshTokenGrantConfig` includes `*http:OAuth2RefreshTokenGrantConfig` — explains the 9 extra rendered fields |
| `client.bal` grep for resource/remote/public functions | init@31 + 11 resource functions @47,67,84,100,118,135,152,170,186,203,220 |
| `grep -cE '^public type … record \{\|' types.bal` vs render | 3 closed in source, 0 closed at top level in render |
| `grep -nE '^public (const\|function\|enum\|annotation\|listener\|service\|class)' *.bal` | only `client.bal:23` (Client) |
| `ls bala/…/2.0.2/any/modules/` | single module `hubspot.crm.obj.feedback` |
| `package.json` `export` | `["hubspot.crm.obj.feedback"]` |
| `find bala -iname '*compiler*'` | no results |
| `ls repo root` @ v2.0.2 | no `compiler-plugin/` directory |
| Python parse of `types.bal` vs new JSON field sets | 0 missing types, 0 invented types, 1 explained mismatch |

## 10. Caveats and unverified items

- Neither render was compiled; the "non-compiling" observations in Section 5 (items 1, 6) are from
  reading the emitted syntax against the Ballerina grammar, not from a `bal build` run. They apply
  equally to `old` and `new`, so they do not affect the verdict.
- Ballerina Central registry metadata was not re-queried over the network; module list, version and
  keyword facts in this report come from the bala's `package.json` and `bala.json`, which are the
  artifacts the extractor actually consumed.
- The exact renderer/extractor commits (`eb5d81b3` / `412ba01e`) were taken from the brief and not
  independently inspected; the causal attribution of each change to spec v2 is inferred from the
  change shapes matching the documented spec-v2 behaviours, not from reading the renderer diff.

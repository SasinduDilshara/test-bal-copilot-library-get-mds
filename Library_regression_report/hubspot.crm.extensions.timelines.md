# ballerinax/hubspot.crm.extensions.timelines 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.extensions.timelines` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.extensions.timelines |
| Tag reviewed | `v2.0.2` (commit `984886024e1f9887f321d3d9df661419baa16543`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.extensions.timelines/2.0.2` |
| Old render | `604` lines |
| New render | `605` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module OpenAPI-generated HubSpot connector: 20 public record types, one `Client`
class (`init` + 13 resource methods), no module-level functions, no services, no listeners, no
compiler plugin. Both renders capture the full public surface of the default module — nothing is
missing on either side.

The diff between `old` and `new` is 4 hunks / 5 added / 4 removed lines, and all three semantic
changes are improvements:

1. Three record field types de-qualified: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`.
2. `@display {label: "Connection Config"}` now emitted on `ConnectionConfig` (it exists in the
   library source and was silently dropped by `old`).
3. The bogus parameter `anydata Additional Values` — an unparseable identifier produced from an
   open-record rest field — is gone from the `.../render` resource signature.

No regression of any kind was found. Several accuracy issues remain, but every one of them is
present identically in `old` and `new` (record closedness, field default values, doc-comment
continuation lines, included-record parameter flattening).

## 2. Change inventory

Structural counts (from the two JSON models, `python3` over `*.json`):

| element | old | new |
|---|---|---|
| `typeDefs` | 20 | 20 |
| `clients` | 1 | 1 |
| client functions (`init` + resources) | 14 | 14 |
| module-level `functions` | 0 | 0 |
| `services` | 0 | 0 |
| `annotations` (declared) | 0 | 0 |
| `readme` characters | 9212 | 9212 |
| `// Unknown type:` lines in render | 0 | 0 |

Declaration sets are identical: `set(old typeDef names) - set(new)` = ∅ and the reverse = ∅.
No declaration added, removed, or renamed. Section markers are identical
(`// --- README ---`, `// --- END README ---`, `// --- Types ---`, `// --- Client ---`); only the
`// --- Client ---` marker shifts 547 → 548 because of the one added annotation line.

Modified declarations (3 types + 1 client method), full list:

| # | Declaration | old | new | kind |
|---|---|---|---|---|
| 1 | `TimelineEventIFrame.width` | `ballerina/lang.int:0.0.0:Signed32 width;` | `int:Signed32 width;` | type-ref fix |
| 2 | `TimelineEventIFrame.height` | `ballerina/lang.int:0.0.0:Signed32 height;` | `int:Signed32 height;` | type-ref fix |
| 3 | `BatchResponseTimelineEventResponseWithErrors.numErrors` | `ballerina/lang.int:0.0.0:Signed32 numErrors?;` | `int:Signed32 numErrors?;` | type-ref fix |
| 4 | `ConnectionConfig` | (no annotation) | `@display {label: "Connection Config"}` added above the type | annotation gained |
| 5 | `Client.get events/[eventTemplateId]/[eventId]/render` | `(..., boolean detail = false, anydata Additional Values, GetEvents…Queries queries)` | `(..., boolean detail = false, GetEvents…Queries queries)` | bogus param dropped |

`grep -c 'ballerina/lang'` = 3 in `old`, 0 in `new`. Path parameters (`[int:Signed32 appId]`, 7
occurrences) were already unqualified in `old`, so the fix is confined to record fields.

## 3. Correctness against library source

Upstream tag `v2.0.2` was cloned and its `ballerina/{client,types,utils}.bal` are **byte-identical**
to the bala's `modules/hubspot.crm.extensions.timelines/{client,types,utils}.bal` (`diff -q`, no
output for all three). `Ballerina.toml` line 5 is `version = "2.0.2"`; bala `package.json` reports
`version 2.0.2`, `ballerina_version 2201.12.2`, `export ["hubspot.crm.extensions.timelines"]`
(single module). So GitHub, the bala, and the pinned version agree.

Verification of the five changed items:

1–3. `types.bal:29` `int:Signed32 width;`, `types.bal:33` `int:Signed32 height;`,
   `types.bal:307` `int:Signed32 numErrors?;`. `grep -n Signed32 types.bal` returns exactly these
   three lines. `new` matches the source spelling; `old` did not.
4. `types.bal:259` `@display {label: "Connection Config"}` immediately precedes
   `types.bal:260 public type ConnectionConfig record {|`. It is the **only** annotation in the
   whole module (`grep -rn '^@' *.bal` → one hit). `new` renders it verbatim; `old` dropped it.
5. `client.bal:160` is
   `resource isolated function get events/[string eventTemplateId]/[string eventId]/render(map<string|string[]> headers = {}, *GetEventsEventTemplateIdEventIdRenderGetRenderByIdQueries queries) returns string|error`.
   The included record `GetEventsEventTemplateIdEventIdRenderGetRenderByIdQueries` (`types.bal:135-138`)
   has exactly one field, `boolean detail?;`, and is an **open** record (`record {` … `};`), whose
   implicit `anydata...;` rest field is what the API-doc model surfaces as the pseudo-field
   `"Additional Values" / anydata / "Capture key value pairs"`. There is no parameter named
   `Additional Values` in the library; `old` invented it. `new` removing it is correct.

Broader spot-checks against `types.bal` / `client.bal`:

- All 20 `public type` declarations in `types.bal` appear in the render, with matching field name
  sets (checked programmatically; the 4 flagged "mismatches" were artifacts of my regex not
  handling escaped identifiers `'in` / `'type` and `*http:OAuth2RefreshTokenGrantConfig` inclusion —
  manual re-check of `ErrorDetail`, `TimelineEventTemplateToken`, `OAuth2RefreshTokenGrantConfig`
  and `ConnectionConfig` shows every source field present).
- `ConnectionConfig`: all 20 fields present in the render in source order (`auth`, `httpVersion`,
  `http1Settings`, `http2Settings`, `timeout`, `forwarded`, `followRedirects`, `poolConfig`,
  `cache`, `compression`, `circuitBreaker`, `retryConfig`, `cookieConfig`, `responseLimits`,
  `secureSocket`, `proxy`, `socketConfig`, `validation`, `laxDataBinding` + doc text).
- `OAuth2RefreshTokenGrantConfig` correctly expands the included `*http:OAuth2RefreshTokenGrantConfig`
  into `refreshToken`, `clientId`, `clientSecret`, `scopes`, `defaultTokenExpTime`, `clockSkew`,
  `optionalParams`, `credentialBearer`, `clientConfig`, plus the module's own `refreshUrl`.
- Escaped identifiers survive: `'in?` (render line 289 ← `ErrorDetail`), `'type` with the
  `"date"|"enumeration"|"number"|"string"` union (render line 332 ← `types.bal` token type).
- Client: `client.bal` contains `public isolated function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/integrators/timeline/v3") returns error?` (line 32) and
  exactly 13 `resource isolated function` declarations (`grep -c` = 13). All 14 appear in both
  renders with matching paths, payload/param types and return unions, e.g.
  `post events/batch/create(BatchInputTimelineEvent payload, …) returns BatchResponseTimelineEventResponse|BatchResponseTimelineEventResponseWithErrors|json|error` matches `client.bal:139`.
- README: the render embeds 9212 characters, and `docs/README.md` in the bala is exactly 9212
  characters and `R.startswith(render_readme)` is `True` — i.e. the full README, unmodified, on
  both sides (and the bala README is identical to the repo's `ballerina/README.md`).

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full `diff -u old new` (4 hunks, 5 `+`, 4 `-` lines) reviewed line by line — every hunk is one of
  the three improvements in §2.
- Sorted-key JSON model diff (`diff -u old.json new.json`) → 22 `+`/`-` lines, all accounted for by
  the same three changes (3 type-name strings, 1 annotation object added, 1 parameter object removed).
- Declaration name sets identical (∅ symmetric difference) for typeDefs; client function count
  14 = 14; README byte length identical; section markers identical.
- `// Unknown type:` count is 0 on both sides, so the spec-v2 "degraded type" improvement does not
  apply to this library — there was nothing to lose or gain there.
- Nothing was truncated: `new` is one line *longer*, and the only removed content is the
  syntactically invalid `anydata Additional Values` parameter.

## 5. Issues in `new` (independent of `old`)

All five below exist **identically in `old`** — they are pipeline-wide behaviours, not spec-v2
regressions — but they are inaccuracies a consumer of the `new` render would be misled by.

1. **Included-record parameter is both flattened and kept** (render line 580). Source is
   `(map<string|string[]> headers = {}, *GetEvents…Queries queries)`; the render emits
   `(map<string|string[]> headers = {}, boolean detail = false, GetEvents…Queries queries)`.
   Two problems: the `*` included-record sigil is lost so `queries` looks like a plain required
   parameter following defaultable ones (not valid Ballerina), and `detail` is duplicated as a
   separate parameter. An LLM would write `client->/events/[a]/[b]/render(detail = true)` or pass a
   record positionally; neither matches the real signature.
2. **Invented default `= false`** on that same `detail` parameter. `types.bal:137` is
   `boolean detail?;` — optional, with **no** default. The JSON carries `"default": "false"` on both
   sides.
3. **Closed records rendered as open.** `ConnectionConfig`, `ApiKeysConfig` and
   `OAuth2RefreshTokenGrantConfig` are `record {| … |}` in `types.bal` (lines 260, 250, 244 region)
   but render as `record { … }`. Wrong closedness changes what an LLM believes is legal.
4. **Field default values dropped, defaulted fields turned optional.** `ConnectionConfig` loses
   `httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`; each
   becomes `field?`. `OAuth2RefreshTokenGrantConfig.refreshUrl` loses its default
   `"https://api.hubapi.com/oauth/v1/token"` — a materially useful value for this connector.
5. **Multi-line doc comments lose the `#` on continuation lines.** In the `ConnectionConfig`
   `laxDataBinding` doc, the second line `and absent fields are handled as \`nilable\` types. Enabled by default`
   is emitted at column 0 with no `#`, breaking the surrounding pseudo-Ballerina block.

Also worth noting (cosmetic, both sides): `public` and `isolated` qualifiers are stripped from all
types and from the client and its methods, and `http:`/`oauth2:` referenced types are annotated with
`// Special Agent Note: … FROM ballerina/http package` instead of an `import` line. The only import
emitted is `import ballerinax/hubspot.crm.extensions.timelines;`.

## 6. Coverage gaps vs. the library

**Zero.** The package exports a single module (`package.json` `export: ["hubspot.crm.extensions.timelines"]`,
and `modules/` contains only that one directory), so the `getDefaultModule()`-only extraction loses
nothing here — there is no submodule API.

Public symbols in the default module: 20 `public type` records (all rendered), 1
`public isolated client class Client` with `init` + 13 resource methods (all rendered). `utils.bal`
declares no `public` symbols (`grep -nE '^public '` over `*.bal` returns hits only in `types.bal`
and `client.bal`). No public constants, enums, listeners, services, or annotation declarations exist
in the library, which matches the empty `functions`/`services`/`annotations` arrays in both JSONs.

## 7. Compiler plugin

The library ships **no compiler plugin**: the bala contains only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` (no `compiler-plugin/` directory, no
`compiler-plugin.json`), and `find -maxdepth 2 -iname '*compiler-plugin*'` over the cloned repo
returns nothing. Consequently there are no plugin-contributed code actions, validations, or
generated artifacts that should have surfaced in the render. Nothing absent.

## 8. Other considerations

- **Version is stable (2.x)** and not deprecated; `package.json` has no deprecation fields.
- **Size**: 605 lines / ~34 KB of render for a connector with 13 operations. The README occupies
  209 of the 605 lines (lines 7–216, 35%), including base64-free image URLs and OAuth setup steps —
  useful for auth guidance, but it is the dominant token cost here.
- **`ConnectionConfig` bloat**: 20 fields of transport configuration, 17 of them `http:*` types the
  render cannot define, are emitted for a connector whose realistic usage is
  `check new ({auth: {token}})`. Same on both sides.
- The three `// Special Agent Note: … FROM ballerina/http package` comment suffixes are the only
  signal that `http:`/`oauth2:` types are external; there is no import statement for them, so the
  render is not compilable as-is (both sides, by design).
- The `.../render` resource is the only operation with query parameters in this connector, so issue
  §5.1/§5.2 affects exactly 1 of 13 operations.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 604 / 605 |
| 2 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 3 | `diff -u old new \| grep -c '^@@'`, `'^\+[^+]'`, `'^-[^-]'` | 4 hunks, 5 added, 4 removed |
| 4 | Full `diff -u old/*.bal.txt new/*.bal.txt` | 3 `int:Signed32` fixes, `@display` added, `anydata Additional Values` removed |
| 5 | `grep -c 'ballerina/lang'` old / new | 3 / 0 |
| 6 | JSON model sizes (python) | typeDefs 20/20, clients 1/1, client funcs 14/14, functions 0/0, services 0/0, annotations 0/0, readme 9212/9212 |
| 7 | typeDef name set difference old↔new | ∅ both directions |
| 8 | `diff -u old.json new.json` (sorted keys, indent 1) | 22 changed lines, all three known changes |
| 9 | `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`9848860…`, peeled `66332d0…`) |
| 10 | `git clone --depth 1 --branch v2.0.2` | succeeded |
| 11 | `diff -q src/ballerina/{client,types,utils}.bal bala/modules/**/…` | identical (no output) for all three |
| 12 | `diff -q src/ballerina/README.md bala/any/docs/README.md` | identical |
| 13 | `grep -n version src/ballerina/Ballerina.toml` | line 5: `version = "2.0.2"` |
| 14 | bala `package.json` | version 2.0.2, ballerina_version 2201.12.2, export `["hubspot.crm.extensions.timelines"]`, template false |
| 15 | `ls -R` bala | `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`; modules dir has one module with `client.bal`, `types.bal`, `utils.bal` |
| 16 | `find src -maxdepth 2 -iname '*compiler-plugin*'` | no matches |
| 17 | `grep -rn '^@' bala modules/*.bal` | 1 hit: `types.bal:259 @display {label: "Connection Config"}` |
| 18 | `grep -n Signed32 types.bal` | lines 29, 33, 307 — all `int:Signed32` |
| 19 | `client.bal:160` | `resource isolated function get …/render(map<string\|string[]> headers = {}, *GetEvents…Queries queries) returns string\|error` |
| 20 | `types.bal:135-138` | `public type GetEvents…Queries record { boolean detail?; };` — open record, one optional field, no default |
| 21 | `grep -c 'resource isolated function' client.bal` | 13 (+ `init` at line 32 = 14) |
| 22 | `grep -nE '^public (type\|const\|enum\|class\|…)' bala/*.bal` | 20 hits, all in `types.bal`; none in `utils.bal` |
| 23 | Render field-set vs source field-set for all 20 typeDefs (python) | 16 exact; 4 flagged only by regex limitations, manually confirmed correct |
| 24 | `render_readme in bala README` / `README.startswith(render_readme)` | `True` / `True`, both 9212 chars |
| 25 | Render lines 481–546 (`new`) and 478–540 (`old`) read for `ConnectionConfig` | all 20 fields present both sides; defaults dropped both sides |
| 26 | Render lines 449–461 (`new`) `OAuth2RefreshTokenGrantConfig` | included `*http:OAuth2RefreshTokenGrantConfig` fields expanded; `refreshUrl` default lost |
| 27 | `grep -n "'in\|'type"` new render | lines 289, 332 — escaped identifiers preserved |
| 28 | Section markers `grep -n '^// --- '` | old 7/216/218/547, new 7/216/218/548 |
| 29 | Precomputed `OLD_AND_NEW_DIFFS/hubspot.crm.extensions.timelines_diff.md` header | 604/605 lines, 5 added, 4 removed, 4 hunks — matches my own computation |

## 10. Caveats and unverified items

- I did not re-query `api.central.ballerina.io` for this package; version, module list and
  deprecation state were taken from the bala's `package.json` and the `v2.0.2` tag, which agree
  with each other. Deprecation status is therefore verified only from bala metadata (no
  deprecation fields present), not from the Central API.
- I did not compile either render. Statements about non-compiling constructs (§5.1, §5.3) are from
  reading the Ballerina grammar rules against the emitted text, not from a `bal build`.
- The automated field-set comparison (evidence #23) flagged 4 types due to my own regex's handling
  of escaped identifiers and record inclusion; I resolved those manually by reading both the source
  and the rendered blocks. They are correct, but the resolution is by inspection rather than by a
  clean automated check.
- The claim that `"Additional Values"` originates from the open record's implicit `anydata` rest
  field is an inference from the API-doc model's description string (`"Capture key value pairs"`)
  plus the record being open; I did not read the `CopilotLibraryManager` extractor source to confirm
  the code path.

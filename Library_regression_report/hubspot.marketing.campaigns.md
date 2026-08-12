# ballerinax/hubspot.marketing.campaigns 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.campaigns` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.campaigns |
| Tag reviewed | `v2.0.2` (commit `9967416010a4921f4f4af5474f83ff778222b78a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.campaigns/2.0.2` |
| Old render | `672` lines |
| New render | `673` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. The two renders are structurally identical (same 41 type
definitions, same single `Client` class, same 16 resource methods + `init`, same 8 599-char README
block). `new` differs in exactly three ways, all of them corrections:

1. 18 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.marketing.campaigns:2.0.2:CollectionResponsePublicCampaignAsset`) are
   normalised to the forms the library source actually uses (`int:Signed32`,
   `CollectionResponsePublicCampaignAsset`).
2. 7 bogus `anydata Additional Values` positional parameters — a name containing a space, i.e.
   non-parsable Ballerina — are removed from the resource signatures that take an included query
   record.
3. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig`, which exists in the
   published source (`types.bal:167`) and was silently dropped by `old`, is now emitted.

Nothing was lost. No declaration, parameter, doc line, default value or README content present in
`old` is absent from `new`. Both renders contain 0 `// Unknown type:` lines, so the spec-v2
type-definition improvement is a no-op for this library.

Several inaccuracies remain in `new`, but every one of them is byte-identical in `old` — they are
pre-existing renderer behaviour, not regressions (section 5).

## 2. Change inventory

`diff -u old new` yields 9 hunks / 33 changed lines. No line is a pure deletion of content and no
declaration is added or removed.

| Kind | old | new | delta |
|---|---|---|---|
| `type` definitions (render) | 41 | 41 | 0 |
| `typeDefs` (JSON) | 41 | 41 | 0 |
| `clients` (JSON) | 1 | 1 | 0 |
| client functions (JSON, incl. `init`) | 17 | 17 | 0 |
| `resource function` lines (render) | 16 | 16 | 0 |
| top-level `functions` / `services` / `annotations` (JSON) | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| README chars (JSON `readme`) | 8 599 | 8 599 | 0 |
| section markers | 4 | 4 | 0 |

Modified only:

| Change | count | evidence |
|---|---|---|
| `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` | 17 | `grep -o` on `old/*.json` = 17; 0 remain in `new` |
| `ballerinax/hubspot.marketing.campaigns:2.0.2:CollectionResponsePublicCampaignAsset` → bare name | 1 | `PublicCampaignWithAssets.assets`, render line 301 |
| `anydata Additional Values` parameter removed | 7 | `grep -c '"Additional Values"'`: old 7, new 0 |
| `@display {label: "Connection Config"}` added | 1 | new render line 410; JSON `typeDefs[].annotations` |
| Net line count | +1 | the added `@display` line |

Any qualified-reference form `org/pkg:version:Type` remaining in `new`: 0
(`grep -cE '"name": "[a-z]+/[a-zA-Z0-9._]+:[0-9]' new/*.json` → 0).

The 7 signatures that lost `anydata Additional Values` are exactly the 7 resource methods that
declare an included query-record parameter (`*…Queries queries`) in `client.bal`
(lines 47, 81, 119, 137, 208, 257, 309).

## 3. Correctness against library source

Upstream tag `v2.0.2` clone is byte-identical to the bala for all four relevant files, so GitHub
and bala do not disagree:

```
diff -q src/ballerina/client.bal  bala/.../client.bal  -> identical
diff -q src/ballerina/types.bal   bala/.../types.bal   -> identical
diff -q src/ballerina/utils.bal   bala/.../utils.bal   -> identical
diff -q src/ballerina/README.md   bala/any/docs/README.md -> identical
src/ballerina/Ballerina.toml:5  version = "2.0.2"
```

Spot checks of everything `new` changes:

| Item in `new` | Source evidence | Verdict |
|---|---|---|
| `MetricsCounters { int:Signed32 sessions; newContactsFirstTouch; influencedContacts; newContactsLastTouch; }` | `types.bal:236-241` — identical, uses `int:Signed32` | correct; `old`'s `ballerina/lang.int:0.0.0:Signed32` was wrong |
| `PublicSpendItem` / `PublicBudgetItem` `createdAt`, `'order`, `updatedAt` as `int:Signed32` | `types.bal:243-250` (and the `PublicSpendItem` block) | correct |
| `PublicCampaignWithAssets.assets` = `record {\|CollectionResponsePublicCampaignAsset...;\|}` | `types.bal:160` — exact string match | correct; `old` inserted a version-qualified name that does not appear anywhere in the source |
| `GetMarketingV3CampaignsQueries.'limit` = `int:Signed32` optional | `types.bal:341-355` | correct |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:166-168`; it is the only `@` annotation in the entire published package (`grep -n '^@' bala/modules/*/*.bal` → 1 hit) | correct, and `old` omitted it |
| Removal of `anydata Additional Values` | No such parameter exists in `client.bal`; the 7 methods declare `*XxxQueries queries` (an open record's implicit `anydata` rest field is what `old` materialised as a fake parameter with a space in its name) | removal is correct |
| `function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/marketing/v3/campaigns") returns error?` | `client.bal:31` — exact match | correct (both sides) |
| 16 resource methods, accessors/paths/payload/return types | `client.bal:47,63,81,100,119,137,152,173,192,208,223,241,257,274,289,309` — all 16 present with matching accessor, path segments, payload type and return union | correct (both sides) |

## 4. Regressions

**None found.**

What was checked to conclude that:
- Full `diff -u old new` reviewed line by line (9 hunks, 33 lines) — every `-` line is either a
  version-qualified type name replaced by its correct short form, or the `anydata Additional Values`
  pseudo-parameter. No declaration, doc comment, default value, parameter, or return type is
  removed.
- Declaration-set comparison: `type`/`enum`/`const`/`class` names extracted and sorted from both
  renders — identical sets (41 each). Resource-function count identical (16 each).
- JSON-level comparison: `typeDefs` name sets identical (`only old: []`, `only new: []`);
  `clients[0].functions` length 17 on both; `functions`, `services`, `annotations` all empty on
  both; `name`, `description`, `readme` byte-identical.
- README block: `readme` field is 8 599 chars on both sides and equals `docs/README.md` in the bala
  byte for byte; the render's `// --- README ---` / `// --- END README ---` markers are at the same
  positions (lines 7 / 196) in both files, ending with the same Examples list.
- Pre-existing malformed constructs are present in *equal numbers* on both sides, so none of them
  is a `new` regression: 19 orphan doc-continuation lines (`awk` count 19 old / 19 new) and 2
  resource functions whose `.` path was dropped (`grep -c` 2 old / 2 new).

## 5. Issues in `new` (independent of `old`)

All five below are byte-identical in `old`; they are renderer behaviour, not spec-v2 damage.

1. **Included query-record parameters are double-rendered with fabricated defaults.** Example
   (new line 612):
   `resource function get (map<string|string[]> headers = {}, int:Signed32 limit = 0, string name = "", string sort = "", string after = "", string[] properties = [], GetMarketingV3CampaignsQueries queries) returns …`
   The source declares `resource isolated function get .(map<string|string[]> headers = {}, *GetMarketingV3CampaignsQueries queries)` (`client.bal:47`). The render both flattens the record's
   fields into positional parameters *and* keeps the record parameter, and invents defaults
   (`limit = 0`, `name = ""`, `sort = ""`) that do not exist — `types.bal:341-355` declares those
   fields as optional with no default value. An LLM copying this will emit a call that does not
   compile and will pass `limit = 0` where the API default is 50. Affects all 7 query-record methods.

2. **Resource path `.` is dropped.** `resource function get (` and `resource function post (`
   (new lines 612, 616) should be `resource function get .(` / `post .(` per `client.bal:47,63`.
   Non-parsable as written; also loses which method is the collection root.

3. **Record `readonly`/closed-ness is lost.** The source has 3 closed records
   (`OAuth2RefreshTokenGrantConfig` `types.bal:152`, `ConnectionConfig` `:168`,
   `ApiKeysConfig` `:367`, all `record {|`); the render emits 0 closed records
   (`grep -cE '^type … record \{\|'` → 0). Extra fields would be wrongly assumed acceptable.

4. **Field default values are dropped and defaulted fields are re-typed as optional.**
   `ConnectionConfig` has 11 fields with defaults (`httpVersion = http:HTTP_2_0`,
   `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`, `forwarded = "disable"`,
   `cache = {}`, `compression = http:COMPRESSION_AUTO`, `responseLimits = {}`,
   `socketConfig = {}`, `validation = true`, `laxDataBinding = true`). All 11 appear in the render
   as `field?` with no default (new lines 411-450). The information that `timeout` defaults to 30 s
   is gone.

5. **Multi-line doc comments lose the `#` on continuation lines** — 19 occurrences, e.g. new
   lines 508-510: `# Limit for the number of contacts to fetch` followed by a bare
   `Default: 100` line, from `types.bal` doc `# Default: 100`. Breaks the render as valid Ballerina
   and can be mis-read as code.

Not counted as issues: `public` and `isolated` qualifiers are stripped from types, the client class
and its methods throughout both renders — this appears to be a deliberate, uniform convention of the
renderer rather than an inaccuracy about a specific symbol.

## 6. Coverage gaps vs. the library

**None.**

- The package exports exactly one module (`package.json` `"export": ["hubspot.marketing.campaigns"]`;
  Central `modules` list has a single entry), and it is the default module — so the
  `getDefaultModule()`-only extraction loses nothing here. `bala/any/modules/` contains only
  `hubspot.marketing.campaigns/` with `client.bal`, `types.bal`, `utils.bal`.
- Public types: 41 in `types.bal`, 41 in the render; `comm` of the sorted sets is empty in both
  directions.
- Other public symbols in the bala: `public isolated client class Client` (`client.bal:23`) — present.
  `grep -nE '^public (isolated )?function|^public const|^public enum|^public annotation|^public listener'`
  over all three module files returns nothing else; `utils.bal` contains only module-private helpers.
- All 16 resource methods and `init` are rendered.

## 7. Compiler plugin

The package ships no compiler plugin: `find` over the bala for `*compiler*` returns nothing (no
`compiler-plugin/`, no `compiler-plugin.json`), and the upstream `v2.0.2` tree has no
`compiler-plugin`/`ballerina-*-compiler-plugin` directory (`build.gradle`, `ballerina/`,
`examples/`, `docs/`, `build-config/` only). Nothing plugin-derived is therefore expected in, or
missing from, the render.

## 8. Other considerations

- Not deprecated: Central returns `deprecateMessage: ""` and no deprecation flag for 2.0.2.
- Stable 2.x, `graalvmCompatible: true`, built with Ballerina `2201.12.2`, Apache-2.0, pullCount 27.
- Fully auto-generated from OpenAPI (`types.bal` header: "AUTO-GENERATED FILE … by the Ballerina
  OpenAPI tool"), which explains the large inline currency-code union repeated in
  `PublicBudgetTotals` and `RevenueAttributionAggregate` — two ~1 400-char single lines that
  dominate token cost in a 673-line render. Identical in both sides.
- Size impact of the change is negligible: +1 line, and the shortened type names make `new` slightly
  cheaper in tokens.
- Doc quality is good: every query record field carries a description; the README is complete
  through the Examples section.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 672 / 673 |
| `diff -u old new` | 9 hunks, 33 changed lines (full output reviewed) |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each; README 7/196, Types 198, Client 604 (old) / 605 (new) |
| `grep -cE '^type '` old / new | 41 / 41 |
| `grep -cE '^ *resource function'` old / new | 16 / 16 |
| JSON key-by-key compare | `name`, `description`, `readme` identical; `typeDefs` 41/41; `clients` 1/1; `clients[0].functions` 17/17; `functions`/`services`/`annotations` 0/0 both |
| `typeDefs` name-set diff | `only old: []`, `only new: []` |
| `grep -o 'ballerina/lang.int:0.0.0:Signed32' old/*.json \| wc -l` | 17 |
| `grep -o 'ballerinax/hubspot.marketing.campaigns:2.0.2:' old/*.json \| wc -l` | 1 |
| `grep -cE '"name": "[a-z]+/[a-zA-Z0-9._]+:[0-9]' new/*.json` | 0 |
| `grep -c '"Additional Values"' old/*.json` / `new/*.json` | 7 / 0 |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, v2.0.2 — exact match `v2.0.2` (`9967416…`) |
| `git clone --depth 1 --branch v2.0.2` then `diff -q` vs bala for `client.bal`, `types.bal`, `utils.bal`, `README.md` | all identical |
| `wc -l bala modules/*.bal` | client.bal 319, types.bal 376, utils.bal 219 |
| `grep -n 'resource isolated function' client.bal` | 16 methods at lines 47…309; `init` at 31 |
| `grep -n '^@' bala/modules/*/*.bal` | 1 hit: `types.bal:167  @display {label: "Connection Config"}` |
| `grep -oE '^public type' types.bal \| wc -l` vs render type set (`comm`) | 41 vs 41, empty both directions |
| `grep -nE '^public (isolated )?function\|^public const\|^public enum\|^public annotation\|^public listener' bala/modules/*/*.bal` | only `client.bal:23 public isolated client class Client` |
| `grep -cE '^public type … record \{\|' types.bal` / same on new render | 3 / 0 |
| ConnectionConfig defaulted fields in source (`types.bal:168-208`) | 11, all rendered as `?` with no default |
| `awk` orphan doc-continuation count old / new | 19 / 19 |
| `grep -nE 'resource function (get\|post\|put\|delete\|patch) \('` old / new | 2 / 2 (same two methods) |
| `readme` field vs `bala/any/docs/README.md` | both 8 599 chars, equal |
| `find bala -iname '*compiler*'` ; upstream `find -maxdepth 2 -iname '*compiler*'` | no matches |
| Central `…/registry/packages/ballerinax/hubspot.marketing.campaigns/2.0.2` | version 2.0.2, one module, `deprecateMessage: ""`, ballerinaVersion 2201.12.2 |

## 10. Caveats and unverified items

- The renders were not compiled or parsed by the Ballerina compiler; claims that specific lines are
  "non-parsable" (dropped `.` path, doc continuations without `#`, `anydata Additional Values`) are
  based on reading the grammar, not on a compiler run.
- The `old`/`new` provenance (branches `main @ eb5d81b3` vs
  `L1_json_and_annotations_with_spec_v2 @ 412ba01e`) is taken from the brief; the `ballerina-vscode`
  sources themselves were not inspected, so the *cause* attributed to each change (spec-v2 type-ref
  normalisation, annotation capture, included-record parameter handling) is inferred from the
  artefacts, not read from the extractor code.
- The runtime behaviour of the HubSpot API (e.g. whether `limit`'s real default is 50) is taken from
  the library's own doc comments, not verified against HubSpot.

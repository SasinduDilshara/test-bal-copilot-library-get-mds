# ballerinax/hubspot.crm.obj.leads 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.leads` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.leads |
| Tag reviewed | `v2.0.2` (commit `1f34733`, "[Gradle Release Plugin] - pre tag commit: 'v2.0.2'") |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.leads/2.0.2` |
| Old render | `803` lines |
| New render | `804` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three changes, all improvements, no losses:

1. **11 version/module-qualified type references normalised** (`ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`; `ballerinax/hubspot.crm.obj.leads:2.0.2:ValueWithTimestamp` → `ValueWithTimestamp`). `old` had 11 such refs, `new` has 0. All 11 now match the library source text exactly.
2. **`@display {label: "Connection Config"}` recovered** on `ConnectionConfig` — the module's only annotation, present at `types.bal:240` in both bala and upstream, entirely absent from `old`.
3. **4 bogus `anydata Additional Values` parameters removed** from client resource functions. This was a doc-model artifact (the anydata rest field of an open included-record query param), rendered as a positional parameter with a space in its identifier — invalid Ballerina and misleading to an LLM.

Declaration inventory is otherwise byte-identical: 41 types in, 41 types out on both sides; 1 client class, 1 `init`, 11 resource functions on both sides; README block (lines 1–219) identical; 0 `// Unknown type:` placeholders on either side (this library exports only records, so the spec-v2 `Error`/object-type recovery path is not exercised here).

Seven accuracy problems remain in `new`, but every one of them is also present verbatim in `old`, so none is a regression. They are listed in §5.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 803 | 804 |
| Diff lines added / removed | — | +16 / −15 (15 hunks) |
| `// --- ` section markers | 4 | 4 |
| `type ` declarations | 41 | 41 |
| `client class` | 1 | 1 |
| `resource function` | 11 | 11 |
| `function init` | 1 | 1 |
| `@display` annotations | 0 | 1 |
| `// Unknown type:` placeholders | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 11 | 0 |
| `Additional Values` params | 4 | 0 |

### Declarations added / removed

**None.** JSON-level set comparison of `typeDefs` names: `only old: set()`, `only new: set()`. Client function count 12 vs 12 (init + 11 resource functions). Render-level declaration-header sets are identical modulo the two changes below.

### Declarations modified (15 total)

**Kind: type (record) — 11 modified**

| Type | Change |
|---|---|
| `GetCrmV3ObjectsLeadsGetPageQueries` | `'limit`: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` |
| `AssociationSpec` | `associationTypeId`: same normalisation |
| `ValueWithTimestamp` | `updatedByUserId`: same |
| `BatchResponseSimplePublicObjectWithErrors` | `numErrors`: same |
| `BatchResponseSimplePublicUpsertObjectWithErrors` | `numErrors`: same |
| `CollectionResponseWithTotalSimplePublicObjectForwardPaging` | `total`: same |
| `PublicObjectSearchRequest` | `'limit`: same |
| `SimplePublicObject` | `propertiesWithHistory`: `record {\|ballerinax/hubspot.crm.obj.leads:2.0.2:ValueWithTimestamp[]...;\|}` → `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicUpsertObject` | `propertiesWithHistory`: same |
| `SimplePublicObjectWithAssociations` | `associations` and `propertiesWithHistory`: same (2 refs) |
| `ConnectionConfig` | **gained** `annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]` → renders as `@display {label: "Connection Config"}` at `new` line 569 |

7 `int:Signed32` refs + 4 inline-record refs = 11 normalised refs, matching the `grep -c` of 11 → 0.

**Kind: client resource function — 4 modified** (parameter `Additional Values` / type `anydata` / description "Capture key value pairs" dropped)

| Resource | old params | new params |
|---|---|---|
| `post batch/read` | payload, headers, archived, **Additional Values**, queries | payload, headers, archived, queries |
| `get [string leadsId]` | leadsId, headers, associations, archived, propertiesWithHistory, idProperty, properties, **Additional Values**, queries | same minus Additional Values |
| `patch [string leadsId]` | leadsId, payload, headers, idProperty, **Additional Values**, queries | same minus Additional Values |
| `get ` (list page) | headers, associations, archived, propertiesWithHistory, limit, after, properties, **Additional Values**, queries | same minus Additional Values |

Return types, docs, defaults and every other parameter are unchanged on all 12 client functions.

## 3. Correctness against library source

Upstream `v2.0.2` and the bala are byte-identical for the two source files that feed the render:
`diff src/ballerina/client.bal <bala>/modules/hubspot.crm.obj.leads/client.bal` → empty; `diff` on `types.bal` → empty. So GitHub and bala agree; no reconciliation needed.

**Type-ref normalisation (all 11 confirmed correct).** `grep -n "int:Signed32" src/ballerina/types.bal` returns exactly 7 lines — 65, 133, 185, 214, 308, 336, 372 — matching the 7 scalar refs `new` emits as `int:Signed32`. `grep -n "ValueWithTimestamp\[\]\.\.\.\|CollectionResponseAssociatedId\.\.\."` returns exactly 4 lines — 230, 378, 386, 440 — matching the 4 inline-record refs `new` emits unqualified. `new` reproduces the source token exactly; `old` did not.

**`@display` annotation (confirmed correct).** `src/ballerina/types.bal:239-241`:
```
# Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
@display {label: "Connection Config"}
public type ConnectionConfig record {|
```
`grep -rn "@display" <bala>/modules/` returns exactly one hit (`types.bal:240`), so `new`'s single `@display` is complete and there is no second annotation still missing.

**`Additional Values` removal (confirmed correct to drop).** The 4 affected resources are exactly the 4 whose source signature takes an included record param (`client.bal:47, 67, 100, 170`, all `*<X>Queries queries`). All four query records are **open** records (`record {` not `record {|`) — `types.bal:23`, `:57`, `:284`, `:450` — so each has an implicit `anydata` rest field, which the Ballerina doc model surfaces as a pseudo-parameter named "Additional Values" with description "Capture key value pairs". The remaining 8 client functions have no included-record param and had no `Additional Values` on either side. The correspondence is exact, confirming `old` was leaking a doc artifact rather than a real parameter. `anydata Additional Values` is not valid Ballerina (space in identifier) and no such parameter exists in the source.

**Full-API spot check.** All 41 `public type` declarations in the bala (`grep -cE '^public type' types.bal` → 41) appear in both renders (`grep -c '^type '` → 41 both). `ConnectionConfig` field count verified 19 in source (`types.bal:241-283`) vs 19 in `new` JSON and 19 in the `new` render. `OAuth2RefreshTokenGrantConfig` correctly flattens the `*http:OAuth2RefreshTokenGrantConfig` inclusion into 10 fields (`refreshUrl`, `refreshToken`, `clientId`, `clientSecret`, `scopes`, `defaultTokenExpTime`, `clockSkew`, `optionalParams`, `oauth2:CredentialBearer credentialBearer`, `oauth2:ClientConfiguration clientConfig`) — no fields lost. `ApiKeysConfig` → 2 fields, matching `types.bal:492-496`.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full unified diff of the two renders (31 changed lines, 15 hunks) read line by line; every hunk falls into exactly one of the three categories in §1.
- JSON structural diff: `typeDefs` name sets identical (0 added, 0 removed); per-type canonical-JSON comparison isolated 11 differing types, each inspected field by field — the only removals anywhere in the JSON are the four `Additional Values` parameter objects and the eleven version-qualified name strings (replaced, not dropped).
- Render declaration-header sets compared after normalising away the `Additional Values` substring: identical except one added `@display` line. No signature, return type, parameter, default value, or doc comment differs otherwise.
- README: `diff` of lines 1–219 → identical; JSON `readme` field string-equal on both sides (8583 chars), `description` and `name` string-equal.
- Section markers: 4 on both sides, same order (`README`, `END README`, `Types`, `Client`).
- Nothing that was correct in `old` is missing, truncated, or less accurate in `new`. The four removed items were incorrect in `old`; the eleven rewritten refs are more accurate in `new`.

Note on the one thing removed that carried *any* signal: dropping `Additional Values` also drops the (implicit) hint that the four `*Queries` records are open and accept arbitrary extra query parameters. That signal was unusable as rendered — a positional `anydata` parameter with a space in its name cannot be written in Ballerina, and the correct way to pass extras is inside the record. I do not count this as a regression, but a future renderer could express it as `record {| ... anydata...; |}` on the query record instead.

## 5. Issues in `new` (independent of `old`)

All seven are byte-identical in `old` — they are pre-existing renderer limitations, not introduced by spec v2. Listed because they would mislead an LLM consuming `new`.

1. **`public` and `isolated` modifiers dropped everywhere.** Source has `public type X` ×41 and `public isolated client class Client` (`client.bal:23`); render emits `type X` and `client class Client`. All 11 resource functions are `resource isolated function` in source (`client.bal:47,67,84,100,118,135,152,170,186,203,220`) but `resource function` in the render. `init` is `public isolated function` in source, `function init` in the render. `grep -c '^public' new/*.bal.txt` → 1, and that single hit (line 180) is inside the README code sample.
2. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:241`), `OAuth2RefreshTokenGrantConfig` (`:199`) and `ApiKeysConfig` (`:492`) are `record {| ... |}` in source; the render emits `record { ... }`. `grep -c 'record {|$'` on the render → 0. (Inline rest-field records like `record {|string...;|}` are preserved correctly.)
3. **Record field default values dropped.** `boolean archived = false` → `boolean archived?` in `PostCrmV3ObjectsLeadsBatchReadReadQueries` (`types.bal:25`), `GetCrmV3ObjectsLeadsGetPageQueries` (`:61`) and `GetCrmV3ObjectsLeadsLeadsIdGetByIdQueries` (`:455`); `int:Signed32 'limit = 10` → `int:Signed32 'limit?` (`:65`); `string refreshUrl = "https://api.hubapi.com/oauth/v1/token"` → `string refreshUrl?` (`:202`). The render turns defaulted fields into plain optionals, losing the documented default.
4. **Included-record query params are duplicated.** Source: `resource isolated function get .(map<string|string[]> headers = {}, *GetCrmV3ObjectsLeadsGetPageQueries queries)`. Render emits *both* the flattened fields *and* the record param: `resource function get (..., string[] properties = [], GetCrmV3ObjectsLeadsGetPageQueries queries)`. Same for `post batch/read`, `get [string leadsId]`, `patch [string leadsId]`. Non-compiling, and an LLM could plausibly emit either half.
5. **Invented defaults on flattened query params.** `associations = []`, `propertiesWithHistory = []`, `properties = []`, `after = ""`, `idProperty = ""` — in source these are optional fields with *no* default (`string[] associations?` etc., `types.bal:59,63,69,67,287`). The render asserts defaults the library does not define.
6. **One outright wrong default.** `get ` (list page) renders `int:Signed32 limit = 0`; the source default is `10` (`types.bal:65`). Confirmed in both JSONs: `('limit','int:Signed32','0',True)`.
7. **Resource path `.` omitted.** Source `resource isolated function get .(...)` and `post .(...)` (`client.bal:170,186`) render as `resource function get (...)` / `resource function post (...)` — the `.` path segment is lost, so the declaration is not valid Ballerina and the "root resource" nature is only inferable from the empty path.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

- Bala `modules/` contains exactly one module — `hubspot.crm.obj.leads` — which is the default module, and `package.json` `"export": ["hubspot.crm.obj.leads"]` confirms it is the only export. There is **no submodule API**, so the known shared `getDefaultModule()` limitation does not bite this library at all.
- Public symbols in the bala's default module: 41 `public type` + 1 `public isolated client class Client` (with `public isolated function init` and 11 `resource isolated function`s). All 41 types and all 12 client functions are present in both renders.
- The only non-rendered declaration is `enum EncodingStyle` at `utils.bal:37`, which is **module-private** (no `public`) and therefore correctly excluded. `utils.bal` contains no public declarations.

## 7. Compiler plugin

**No compiler plugin exists for this library.** The upstream repo at `v2.0.2` contains only `ballerina/`, `build-config/`, `docs/`, `examples/`, `gradle/` — `find . -iname "*compiler-plugin*" -maxdepth 3` returns nothing. The bala has no `compiler-plugin/` directory (`ls -R` on the bala shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-implied is therefore absent from the render.

## 8. Other considerations

- **Version stability.** Bala `package.json` reports `version 2.0.2`, `ballerina_version 2201.12.2`, `graalvmCompatible true`, `template false`. Upstream `ballerina/Ballerina.toml:5` → `version = "2.0.2"`. Both sides pinned correctly; no drift.
- **Stable major version, not deprecated.** `2.0.2` is post-1.0. No deprecation markers found in the bala or upstream source.
- **Size/token impact is negligible:** +1 line net (+16/−15). The `@display` line adds 1 line; the four `Additional Values` removals shorten four long signature lines; the eleven ref normalisations shorten eleven field lines substantially (`ballerinax/hubspot.crm.obj.leads:2.0.2:` is 38 characters removed per occurrence). Net token count is slightly *lower* in `new` despite the extra line.
- **Doc quality is good.** Every public type and every field carries a `#` doc comment, and all 12 client functions carry a summary line. The renderer's `// Special Agent Note: X FROM ballerina/http package` trailer annotations on `ConnectionConfig`/`OAuth2RefreshTokenGrantConfig` fields are present and correct on both sides.
- **The `type` bodies are not valid standalone Ballerina** (missing `public`, missing `record {|`), but that is a consistent renderer convention across the repo, not specific to this library.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 803 / 804 |
| 2 | `diff old new \| grep -c '^>'` / `'^<'` | 16 added / 15 removed |
| 3 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 4 | `grep -c -E '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | old 11, new 0 |
| 5 | `grep -c 'Additional Values'` both renders | old 4, new 0 |
| 6 | `grep -n '^// --- '` both renders | 4 markers each: README 7, END README 218, Types 220, Client 755(old)/756(new) |
| 7 | `grep -c '^type '` both renders | 41 / 41 |
| 8 | `grep -c '^    resource function'` both renders | 11 / 11 |
| 9 | `grep -c '^@display'` both renders | 0 / 1 |
| 10 | Python: `typeDefs` name-set diff between JSONs | `only old: set()`, `only new: set()` |
| 11 | Python: per-type canonical JSON diff | 11 types differ; 10 are ref normalisations, 1 (`ConnectionConfig`) is the added `annotations` array |
| 12 | Python: client function count + per-function param-name diff | 12 vs 12; 4 functions differ, each only by dropped `Additional Values` |
| 13 | Python: `readme`/`description`/`name` equality between JSONs | all `True`; readme 8583 chars |
| 14 | `diff <(sed -n '1,219p' old) <(sed -n '1,219p' new)` | identical |
| 15 | Normalised declaration-header set diff (old vs new) | only difference: `+ @display {label: "Connection Config"}` |
| 16 | `git ls-remote --tags <repo>` | tags v0.1.0, v2.0.0, v2.0.1, **v2.0.2** |
| 17 | `git clone --depth 1 --branch v2.0.2`; `git log --oneline -1`; `git describe --tags` | `1f34733 [Gradle Release Plugin] - pre tag commit: 'v2.0.2'`; `v2.0.2` |
| 18 | `diff src/ballerina/types.bal <bala>/modules/.../types.bal` | identical |
| 19 | `diff src/ballerina/client.bal <bala>/modules/.../client.bal` | identical |
| 20 | `grep -n "int:Signed32" src/ballerina/types.bal` | 7 hits: lines 65, 133, 185, 214, 308, 336, 372 |
| 21 | `grep -n "ValueWithTimestamp\[\]\.\.\.\|CollectionResponseAssociatedId\.\.\." types.bal` | 4 hits: 230, 378, 386, 440 (7+4 = 11 = old's versioned-ref count) |
| 22 | `grep -rn "@display" <bala>/modules/` | 1 hit: `types.bal:240` `@display {label: "Connection Config"}` |
| 23 | `grep -n "resource function\|isolated function" <bala>/.../client.bal` | 1 `public isolated function init` + 11 `resource isolated function` = 12 |
| 24 | `sed -n '23,26p;284,289p;450,463p' types.bal` | all four `*Queries` records are open (`record {`), i.e. have an anydata rest field |
| 25 | `grep -cE '^public type' <bala>/.../types.bal` | 41 (= 41 typeDefs in both JSONs, all `"type": "Record"`) |
| 26 | `grep -nE '^(public|isolated public)' types.bal client.bal utils.bal` | 41 public types + 1 public client class; `utils.bal` exposes nothing public |
| 27 | `grep -nE '^(public )?(const\|enum\|annotation\|listener\|class\|service)' *.bal` | only `utils.bal:37 enum EncodingStyle` (module-private) |
| 28 | `ls -R <bala>` | `bala.json`, `dependency-graph.json`, `docs/{README.md,icon.png}`, `modules/hubspot.crm.obj.leads/{client,types,utils}.bal`, `package.json` — single module, no compiler-plugin dir |
| 29 | `find src -iname "*compiler-plugin*" -maxdepth 3`; `ls -d src/*/` | no matches; `ballerina/ build-config/ docs/ examples/ gradle/` |
| 30 | `cat <bala>/package.json` | version 2.0.2, ballerina_version 2201.12.2, `export: ["hubspot.crm.obj.leads"]`, graalvmCompatible true |
| 31 | ConnectionConfig field count: source `sed -n '241,283p' \| grep -c` vs new JSON vs new render | 19 / 19 / 19 |
| 32 | New JSON `OAuth2RefreshTokenGrantConfig` fields | 10 fields, `*http:` inclusion fully flattened, `refreshUrl` default lost |
| 33 | New JSON `get .` param defaults | `('limit','int:Signed32','0',True)` vs source default `10` (`types.bal:65`) |
| 34 | `grep -c 'record {|$'` new render | 0 (closed-record syntax lost for the 3 closed types) |
| 35 | `grep -c '^public' new render` | 1, and it is `public function main()` inside the README sample (line 180) |

## 10. Caveats and unverified items

- The **`ballerina/oauth2` bala is not present locally** (`grep -rl "public type RefreshTokenGrantConfig record" .../bala/ballerina/oauth2/` found nothing), so I could not verify against oauth2's own source that the 10 flattened fields of `OAuth2RefreshTokenGrantConfig` are the *complete* field set of `oauth2:RefreshTokenGrantConfig`. I verified the inclusion chain (`hubspot types.bal:199-203` → `http auth_types.bal:58-60` `*oauth2:RefreshTokenGrantConfig`) and that the render's 10 fields are plausible and identically rendered on both sides. This affects only §5 completeness, not the regression verdict, since old and new are byte-identical there.
- I did **not compile** either render or the library. Claims of "non-compiling syntax" in §5 (items 4 and 7, plus `anydata Additional Values` in `old`) rest on Ballerina grammar reading, not on a `bal build` run.
- I did **not** re-query `api.central.ballerina.io`; version, export list, keywords and Ballerina version were taken from the bala's `package.json`, which is authoritative for what the extractor consumed, and cross-checked against upstream `Ballerina.toml`.
- The `src/` clone directory already existed in my scratch dir when I ran `git clone`; I therefore verified its identity explicitly (`git log --oneline -1` → `1f34733 ... 'v2.0.2'`, `git describe --tags` → `v2.0.2`) rather than relying on the clone command's output.
- The two renders' provenance (`old` = upstream `main` @ `eb5d81b3`, `new` = local `L1_json_and_annotations_with_spec_v2` @ `412ba01e`) was taken from the brief and not independently re-verified; I did not re-run the two-stage pipeline.

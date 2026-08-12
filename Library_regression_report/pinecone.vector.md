# ballerinax/pinecone.vector 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/pinecone.vector` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/openapi-connectors/tree/main/openapi/pinecone.vector |
| Tag reviewed | none — no module-scoped tag exists in `openapi-connectors`; reviewed default branch `main` @ `81158a45` (repo tag `v2.5.5`), whose `openapi/pinecone.vector` sources are **byte-identical** to the 1.0.2 bala and whose `Ballerina.toml` declares `version = "1.0.2"` |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/pinecone.vector/1.0.2` |
| Old render | `305` lines |
| New render | `314` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small OpenAPI-generated connector: one module (`pinecone.vector`), 26 public types, 1 client class with `init` + 6 resource methods, no compiler plugin.

`new` is a strict superset of `old`. All 10 diff hunks are improvements:

- 5 `// Unknown type:` placeholders (`NamespaceName`, `VectorData`, `VectorId`, `VectorDimensionality`, `ErrorMessage`) are replaced with real subtype definitions carrying their doc comments and, where present, their `@constraint` annotation.
- 2 version-qualified inline record refs (`record {|ballerinax/pinecone.vector:1.0.2:IndexNamespaceStats...;|}`, `…:Vector…`) are now written as clean local refs.
- 3 `@display` annotations and 2 `@constraint:Int` annotations that exist in the library source are now emitted (client class, `ConnectionConfig`, `ProxyConfig.password`, `QueryRequest.topK`, `VectorDimensionality`).

Nothing was removed, reworded, truncated, or made less accurate. Zero regressions. Declaration coverage of the default module's public API is now 100 %.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 305 | 314 |
| `^type ` declarations | 21 | 26 |
| `// Unknown type:` placeholders | 5 | 0 |
| `client class` | 1 | 1 |
| `resource function` methods | 6 | 6 |
| `function init` | 1 | 1 |
| Version-qualified type refs (`pinecone.vector:1.0.2:`) | 2 | 0 |
| `@display` annotations | 0 | 3 |
| `@constraint` annotations | 0 | 2 |
| `// --- ` section markers | 4 | 4 |
| JSON `typeDefs` entries | 26 | 26 |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 |
| JSON bytes | 34 801 | 35 682 |

**Declarations added (5)** — all previously degraded to `// Unknown type:` lines:

| Symbol | New render | Kind |
|---|---|---|
| `NamespaceName` | `type NamespaceName string;` | subtype |
| `VectorData` | `type VectorData float[];` | subtype |
| `VectorId` | `type VectorId string;` | subtype |
| `VectorDimensionality` | `@constraint:Int {minValue: 1, maxValue: 20000}` + `type VectorDimensionality int;` | subtype |
| `ErrorMessage` | `type ErrorMessage string;` | subtype |

**Declarations removed:** none (`diff` of the extracted declaration sets shows only additions).

**Declarations modified (5)** — all annotation/type-ref fixes, no signature change:

1. `ConnectionConfig` gains `@display {label: "Connection Config"}`.
2. `ProxyConfig.password` gains `@display {label: "", kind: "password"}`.
3. `QueryRequest.topK` gains `@constraint:Int {maxValue: 10000}`.
4. `DescribeIndexStatsResponse.namespaces`: `record {|ballerinax/pinecone.vector:1.0.2:IndexNamespaceStats...;|}` → `record {|IndexNamespaceStats...;|}`.
5. `FetchResponse.vectors`: same fix for `Vector`.
6. `client class Client` gains `@display {label: "Pinecone Vector", iconPath: "icon.png"}`.

**JSON-level cause** (verified by structural diff of the two JSONs): the 5 subtypes gained a `baseType` field (`"string"`, `"float[]"`, `"int"`), which is what lets the renderer emit a definition instead of a placeholder; `ConnectionConfig`, `VectorDimensionality` and the client gained `annotations` arrays; `QueryRequest.topK` and `ProxyConfig.password` gained field-level `annotations`. Client `functions` arrays, `readme`, and `description` are byte-identical between the two JSONs.

## 3. Correctness against library source

Upstream `main` sources for this module are byte-identical to the bala (`diff types.bal client.bal utils.bal` → all IDENTICAL), so both agree; citations below are to the bala.

Every one of the 5 added declarations verified against `.../modules/pinecone.vector/types.bal`:

| Rendered in `new` | Source | Match |
|---|---|---|
| `# An index namespace name` / `type NamespaceName string;` | types.bal:139-140 `public type NamespaceName string;` | exact |
| `# Vector dense data…` / `type VectorData float[];` | types.bal:136-137 `public type VectorData float[];` | exact |
| `# The unique ID of a vector` / `type VectorId string;` | types.bal:215-216 `public type VectorId string;` | exact |
| `@constraint:Int {minValue: 1, maxValue: 20000}` / `type VectorDimensionality int;` | types.bal:132-134 (doc, annotation, `public type VectorDimensionality int;`) | exact incl. annotation values |
| `type ErrorMessage string;` (no doc) | types.bal:194 `public type ErrorMessage string;` (has no doc comment) | exact |

Modified declarations verified:

- `@display {label: "Connection Config"}` — types.bal:21.
- `@display {label: "", kind: "password"}` on `password` — types.bal:72-73 (the empty `label` is genuinely empty in the source).
- `@constraint:Int {maxValue: 10000}` on `topK` — types.bal:90-91.
- `record {|IndexNamespaceStats...;|}` — types.bal:117; `record {|Vector...;|}` — types.bal:127. Both now match the source spelling exactly; `old` did not.
- `@display {label: "Pinecone Vector", iconPath: "icon.png"}` on the client — client.bal:20.

Client surface (exhaustive, `new` lines 288-314 vs client.bal):

| Render | Source | Match |
|---|---|---|
| `function init(ApiKeysConfig apiKeyConfig, string serviceUrl, ConnectionConfig config = {}) returns error?` | client.bal:32 | exact (qualifiers `public isolated` elided by format) |
| `resource function post describe_index_stats(DescribeIndexStatsRequest payload) returns DescribeIndexStatsResponse\|error` | client.bal:64 | exact |
| `resource function post query(QueryRequest payload) returns QueryResponse\|error` | client.bal:78 | exact |
| `resource function post vectors/delete(DeleteRequest payload) returns DeleteResponse\|error` | client.bal:92 | exact |
| `resource function get vectors/fetch(string[] ids, string\|() namespace = ()) returns FetchResponse\|error` | client.bal:107 (`string? namespace = ()`) | equivalent (`string?` expanded to `string\|()`) |
| `resource function post vectors/update(UpdateRequest payload) returns UpdateResponse\|error` | client.bal:121 | exact |
| `resource function post vectors/upsert(UpsertRequest payload) returns UpsertResponse\|error` | client.bal:135 | exact |

The `# Fetch` doc on `vectors/update` (render line 307) is a copy-paste bug **in the library source** (client.bal:117) faithfully reproduced by both renders — not a render defect.

README block (render lines 8-59) matches the Central `readme` + module readme verbatim; `readme` and `description` fields are identical in both JSONs.

## 4. Regressions

**None found.**

What was checked to conclude that:

- `diff <(extract-decls old) <(extract-decls new)` over `type` / `client class` / `resource function` / `function init` / `// Unknown type:` lines → the only differences are the 5 placeholder lines disappearing and the 5 real type definitions appearing. No declaration is present in `old` and absent in `new`.
- Full `diff -u old new` is 10 hunks, +16/−7 lines. Every removed line is either a `// Unknown type:` placeholder (5) or a version-qualified type ref later re-emitted in clean form (2). No doc comment, parameter, default value, or return type is lost.
- JSON-level: `clients[0].functions` (7 entries), `readme`, `description`, `typeDefs` name set, and every `typeDefs` entry's `fields` array are equal between old and new except for the added `annotations`/`baseType` keys and the de-qualified inline record type names.
- No malformed syntax introduced: the 5 new type definitions and the 5 new annotation lines are well-formed Ballerina.

## 5. Issues in `new` (independent of `old`)

All five below are shared with `old` (i.e. renderer-format limitations, not spec-v2 regressions), but they are inaccuracies vs. the library source that a consumer of `new` would hit:

1. **Record field default values are dropped and the fields are turned optional.** Source `ConnectionConfig` (types.bal:22-51) has non-optional fields with defaults — `http:HttpVersion httpVersion = http:HTTP_2_0`, `decimal timeout = 60`, `string forwarded = "disable"`, `boolean validation = true`; `ProxyConfig` has `string host = ""`, `int port = 0`, `string userName = ""`, `string password = ""`; `QueryRequest` has `boolean includeValues = false`, `boolean includeMetadata = false`. All render as bare `?` optional fields with no default (render lines 70-96, 113-121, 150-151). An LLM reading this loses every default. (Parameter defaults on functions *are* preserved: `config = {}`, `namespace = ()`.)
2. **Closed records rendered as open.** 4 of the 6 `record {|…|}` in types.bal (lines 22, 54, 64, 77 — `ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`, `ApiKeysConfig`) render as `record {` … `};`. The 2 inline ones (lines 117, 127) keep `record {|…|}` correctly.
3. **`@display` annotations on the 6 resource methods are absent.** client.bal:63, 77, 91, 106, 120, 134 each carry `@display {label: "…"}`; `grep -c` for those labels in `new` → 0. Spec v2 added class-level and record-field-level annotations but not client-function-level ones (the JSON `clients[0].functions` entries have no `annotations` key at all).
4. **Client function docs and parameter docs are dropped by the renderer even though they are in the JSON.** `clients[0].functions[0]` (init) carries `"Gets invoked to initialize the `connector`. …"` and per-parameter descriptions (`apiKeyConfig`, `config`, `serviceUrl`, `return`), and `vectors/fetch` carries `ids - The vector IDs to fetch. Does not accept values containing spaces.` — none of this reaches the `.bal.txt` (render line 289 has no preceding doc; lines 292/296/300/304/308/312 are empty `# ` lines).
5. **The render is not compilable as written** — the preamble only emits `import ballerinax/pinecone.vector;` (line 5), while the body references `http:` (14 fields), `constraint:` (2 new annotations) and declares types without `public`. Spec v2 slightly widens this by adding `@constraint:Int` without a `ballerina/constraint` import. This is a known property of the render format, not a defect of this library.

Cosmetic only: a blank line separates the doc comment from `@display`/`type` for the pre-existing records (e.g. render lines 65-68), which in real Ballerina would detach the doc; identical in `old`. `type ErrorMessage string;` (line 272) uses one blank-line separation while neighbours use two.

## 6. Coverage gaps vs. the library

**Zero gaps.**

- The bala's default (and only) module is `pinecone.vector`; `package.json` `"export": ["pinecone.vector"]` and `modules/` contains exactly one directory. There is no submodule-only API, so the shared `getDefaultModule()` limitation does not bite here.
- `grep -nE '^public ' modules/pinecone.vector/*.bal` yields 27 public declarations: 26 types + 1 client class. All 26 types appear as `^type ` in `new` (count 26, name sets equal to the JSON `typeDefs` name set), and `Client` appears as `client class Client`. In `old`, 5 of the 26 appeared only as `// Unknown type:` comments with no body.
- `utils.bal` declares `SimpleBasicType`, `Encoding`, `EncodingStyle`, `defaultEncoding` and 8 helper functions — none are `public`, so their absence from both renders is correct.

## 7. Compiler plugin

None. `ls` over the bala root shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/` directory and no `compiler-plugin.json`. The upstream module directory contains only `Ballerina.toml`, `Package.md`, `Module.md`, `openapi.yaml`, `icon.png`, `client.bal`, `types.bal`, `utils.bal` — no plugin sources. `Ballerina.toml` declares no `[[tool]]` / `balToolId` (Central reports `"balToolId": ""`). Nothing plugin-implied is missing from the render.

The only annotation-processing dependency is `ballerina/constraint` (imported at types.bal:18), used for runtime payload validation. Spec v2 now surfaces both of its usages, which is exactly the plugin-adjacent metadata an LLM needs (`topK` ≤ 10000; dimensionality 1–20000).

## 8. Other considerations

- **Not deprecated.** Central: `"isDeprecated": false`, `"deprecateMessage": ""`. `graalvmCompatible: "Yes"`, pullCount 7745.
- **Stale distribution.** Built with `ballerina_version: 2201.4.1` / `language_spec_version: 2022R4` (May 2023). Old generator style — `ConnectionConfig` still carries the pre-`http:ClientConfiguration` shape.
- **Size/tokens:** +9 lines / +881 JSON bytes (+2.5 %) for the removal of all 5 placeholders — a very good ratio. The render is tiny (314 lines) and poses no context-budget concern.
- **Semantic value of the change is high for this library specifically:** `VectorId`, `VectorData`, `NamespaceName`, `VectorDimensionality` are referenced 17 times across the rendered record fields. In `old` an LLM saw those field types with no definition anywhere, so it could not know `VectorData` is `float[]` or that `VectorId` is a `string`. `new` closes that.
- **Source-level doc bug carried through:** `vectors/update` is documented `# Fetch` (client.bal:117). Worth an upstream fix, out of scope here.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/… new/…` | 305 / 314 |
| `diff -u old new` | 10 hunks, +16/−7 |
| `grep -c '^// Unknown type:'` old / new | 5 / 0 |
| `grep -c 'pinecone.vector:1.0.2:'` old / new | 2 / 0 |
| `grep -cE '^type '` old / new | 21 / 26 |
| `grep -c '^client class '` old / new | 1 / 1 |
| `grep -c '    resource function '` old / new | 6 / 6 |
| `grep -c '@display'` old / new | 0 / 3 |
| `grep -c '@constraint'` old / new | 0 / 2 |
| `diff <(grep -oE '^type [A-Za-z0-9_]+' old\|sort) <(… new\|sort)` | 5 additions, 0 removals |
| `diff` of full declaration set (type/client/resource/init/unknown) | only 5 placeholders removed, 5 types added |
| `ls -R` bala | 1 module `pinecone.vector`; `client.bal`, `types.bal`, `utils.bal`; no compiler-plugin |
| `wc -l` bala module | client.bal 145, types.bal 216, utils.bal 236 |
| `grep -nE '^public ' bala/*.bal` | 26 public types + 1 public client class |
| `grep -nE '^(type\|enum\|final\|isolated function) ' utils.bal` | 3 non-public types/enum + 8 non-public functions (correctly absent from renders) |
| `cat bala/package.json` | version 1.0.2, `export: ["pinecone.vector"]`, ballerina_version 2201.4.1 |
| `git ls-remote --tags openapi-connectors \| grep -i pinecone` | 0 matches (48 tags total, all repo-level `vX.Y.Z`) |
| `git clone --depth 1 --sparse` + `sparse-checkout set openapi/pinecone.vector` | HEAD `81158a45` (`main`, tag `v2.5.5`) |
| `cat openapi/pinecone.vector/Ballerina.toml` | `version = "1.0.2"`, `distribution = "2201.4.1"` |
| `diff upstream/{types,client,utils}.bal bala/…` | all three IDENTICAL |
| `ls -d compiler-plugin*` in upstream module | no matches |
| `curl api.central.ballerina.io/…/ballerinax/pinecone.vector/1.0.2` | `isDeprecated: false`, 1 module, graalvmCompatible Yes |
| Python structural diff of the two JSONs | `typeDefs` 26/26, name sets equal; deltas confined to `baseType` (5 types), `annotations` (3 places), de-qualified inline record names (2); `clients[0].functions`, `readme`, `description` identical |
| types.bal:132-140, 194, 215-216 | source definitions of the 5 added types confirmed |
| types.bal:21, 72-73, 90-91, 117, 127; client.bal:20 | source annotations / inline records confirmed |
| client.bal:32, 64, 78, 92, 107, 121, 135 | all 7 client signatures confirmed against render |
| `grep -c 'label: "Query"\|label: "Upsert"\|label: "Fetch"' new` | 0 (resource-method `@display` absent) |
| `grep -c 'record {\|' new` / `grep -n 'record {\|' types.bal` | 2 in render vs 6 in source (4 top-level closed records opened) |

## 10. Caveats and unverified items

- **No module-scoped tag exists** for `pinecone.vector` in `openapi-connectors`; the repo carries only 48 repo-level `vX.Y.Z` tags. I therefore reviewed the default branch `main` @ `81158a45`. This is safe here because the module's `Ballerina.toml` on `main` still declares `version = "1.0.2"` and its three `.bal` files are byte-identical to the 1.0.2 bala — i.e. the module has not changed since publication. Recorded as a caveat only because the tag itself could not be resolved.
- `dependency-graph.json` was read only in part (first 1200 chars); I did not enumerate the full transitive dependency set, as it has no bearing on the render.
- The precomputed diff at `OLD_AND_NEW_DIFFS/pinecone.vector_diff.md` was cross-checked against the files: its line counts (305/314), hunk count (10), added/removed (+16/−7), placeholder counts (5→0), version-qualified-ref counts (2→0) and the list of 5 added types all reproduce exactly.
- I did not compile the renders (they are not intended to compile) nor execute the two-stage pipeline; the JSONs supplied in the library folder were taken as the pipeline's actual output.

# ballerinax/milvus 1.1.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/milvus` |
| Pinned version | `1.1.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-milvus |
| Tag reviewed | `v1.1.1` (commit `1bf32131935bb54f41565c67bd2a83bebadea117`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/milvus/1.1.1` |
| Old render | `342` lines |
| New render | `343` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders differ in exactly two hunks (`diff -u old new` → 2 hunks, +3/−2 lines). Both are
improvements from spec v2:

1. `// Unknown type: Error` (old) becomes a real definition `type Error error;` with its doc comment (new).
2. The `Client.init` signature loses the malformed pseudo-parameter `anydata Additional Values` and
   the version-qualified return type `ballerinax/milvus:1.1.1:Error?` becomes `Error?`.

Nothing present and correct in `old` is missing from `new`. The library is small (4 `.bal` files,
324 lines) and was reviewed exhaustively: all 15 public types + `Error`, the client class and all
9 client methods appear in both renders. Coverage gap vs. the default module is zero; the package
exports a single module (`export: ["milvus"]`), so there is no submodule blind spot here.

Several inaccuracies remain in `new`, but every one of them is also present in `old` (identical
lines outside the two hunks), so they are pre-existing renderer behaviour, not regressions.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 342 | 343 |
| `// Unknown type:` placeholders | 1 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `type X` declarations | 15 | 16 |
| `client class` | 1 | 1 |
| `remote function` in client | 8 | 8 |
| `init` constructor | 1 | 1 |
| JSON `typeDefs` entries | 16 | 16 |
| JSON `functions` / `services` / `annotations` | 0 / 0 / 0 | 0 / 0 / 0 |

Declarations added in `new` (1): `type Error error;` (rendered form of `public type Error distinct error;`).
Declarations removed in `new`: none.
Declarations modified in `new` (1): `Client.init`.

JSON-level deltas (structural, not textual):
- `typeDefs["Error"]` gains `"baseType": "error"` (old had only `name`/`description`/`type`); this is
  what lets the renderer emit a definition instead of the `Unknown type` placeholder.
- `clients[0].functions["init"]`: the parameter list drops the entry
  `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`
  (15 params → 14), and `return.type.name` changes from `ballerinax/milvus:1.1.1:Error?` to `Error?`.
- `readme`, `description`, `name`, and all 15 other `typeDefs` are byte-identical between the two JSONs.

## 3. Correctness against library source

Upstream `v1.1.1` `ballerina/*.bal` is byte-identical to the bala's `modules/milvus/*.bal`
(`diff` over `client.bal`, `error.bal`, `init.bal`, `types.bal` → identical), and upstream
`ballerina/README.md` is identical to the bala's `docs/README.md`. So GitHub and the bala agree;
no tie-breaking needed.

Exhaustive check of every rendered declaration against the bala source:

| Rendered symbol | Source | Match |
|---|---|---|
| `type Error error;` | `error.bal:18` `public type Error distinct error;` | partial — `distinct` dropped (see §5 N1) |
| `type ConnectionConfig record {…12 fields}` | `types.bal:18-43` | field names/types/docs all match; defaults dropped (§5 N3) |
| `type SecureConfig` (4 fields) | `types.bal:46-55` | exact |
| `type AuthConfig` (`string token`) | `types.bal:58-61` | exact |
| `type CredentialsConfig` (`username`,`password`) | `types.bal:64-69` | exact |
| `type UpsertRequest` (4 fields) | `types.bal:72-81` | exact |
| `type Entry` (`primaryKey?`,`vectors`,`properties?`) | `types.bal:84-94` | inline record rendered `record {\|string fieldName; int value; anydata...;\|}`; `fieldName = "id"` default dropped |
| `type Properties record {}` | `types.bal:97-98` | exact (genuinely empty) |
| `type DeleteRequest` (4 fields) | `types.bal:101-110` | exact |
| `type SearchRequest` (6 fields, `float[][]\|float[] vectors`) | `types.bal:113-126` | exact |
| `type QueryRequest` (4 fields) | `types.bal:129-138` | exact |
| `type SearchResult` (4 fields) | `types.bal:141-150` | closed `record {\| \|}` rendered as open `record { }` (§5 N4) |
| `type QueryResult record {}` | `types.bal:154-155` | exact |
| `type OutputFields` (`float[] vector?`) | `types.bal:160-162` | exact; the `# + vector -` doc is correctly attached to the field |
| `type CreateCollectionRequest` (3 fields) | `types.bal:165-172` | `primaryFieldName = "id"` default dropped |
| `type CreateIndexRequest` (3 fields) | `types.bal:175-181` | exact |
| `client class Client` | `client.bal:21` `public isolated client class Client` | `public`/`isolated` dropped (renderer convention) |
| `init(... ) returns Error?` | `client.bal:28` `init(string serviceUrl, *ConnectionConfig config) returns Error?` | return type now correct; parameter list flattened (§5 N2) |
| `listCollections() returns string[]\|Error` | `client.bal:39` | exact |
| `createCollection(CreateCollectionRequest) returns Error\|()` | `client.bal:48` (`returns Error?`) | equivalent |
| `loadCollection(string collectionName) returns Error\|()` | `client.bal:56` | equivalent |
| `createIndex(CreateIndexRequest) returns Error\|()` | `client.bal:64` | equivalent |
| `upsert(UpsertRequest) returns Error\|()` | `client.bal:72` | equivalent |
| `delete(DeleteRequest) returns int\|Error` | `client.bal:80` | exact |
| `search(SearchRequest) returns SearchResult[][]\|Error` | `client.bal:88` | exact |
| `query(QueryRequest) returns QueryResult[][]\|Error` | `client.bal:96` | exact |

The new `type Error error;` is correct in substance: `Error` is a distinct error type declared at
`error.bal:18` with exactly the doc comment the render reproduces.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff -u old new` over the whole file: only the two hunks listed in §2. Every other line
  (README block lines 8–118, all 15 shared type definitions, all 8 remote methods, section markers)
  is byte-identical.
- Sorted declaration sets extracted with `grep -oE '^type [A-Za-z]+|^client class [A-Za-z]+'`:
  `new` is a strict superset of `old` (adds `Error`, removes nothing).
- JSON comparison: `typeDefs` name sets identical; only `Error` differs (gains `baseType`), and only
  `clients[0].functions.init` differs. `readme`, `description`, `functions`, `services`,
  `annotations` all identical.

The one thing `new` drops — the `anydata Additional Values` parameter on `init` — is deliberately
**not** counted as a regression: `Additional Values` contains a space, so it is not a legal Ballerina
identifier and the old line could never compile; it is an artefact of the extractor materialising the
open-record rest field of `ConnectionConfig` as a parameter. The only information lost is the weak
hint that `ConnectionConfig` is an open record, and that hint is still recoverable from the
`ConnectionConfig config` parameter that both renders keep. Informational, not a regression.

## 5. Issues in `new` (independent of `old`)

All five are also present in `old`; they are listed here because §5 asks for accuracy of `new` on its
own terms.

- **N1 — `distinct` dropped from `Error`.** Render: `type Error error;`. Source `error.bal:18`:
  `public type Error distinct error;`. An LLM told the type is a plain `error` may believe an
  arbitrary `error` value is assignable to `milvus:Error`, which is false for a distinct type.
- **N2 — `Client.init` signature does not match the source.** Source `client.bal:28` is
  `public isolated function init(string serviceUrl, *ConnectionConfig config) returns Error?`.
  The render flattens the included record into 12 individual parameters **and** appends
  `ConnectionConfig config`, i.e. the config surface appears twice. Two further problems:
  (a) the flattened parameters carry defaults the source does not have — `authConfig = {token: ""}`,
  `credentialsConfig = {username: "", password: ""}`, `idleTimeout = 0`, `databaseName = ""`,
  `serverName = ""`, `proxyAddress = ""`, `secureConfig = {…all empty…}` — whereas in
  `types.bal:20-42` those fields are optional (`?`) with no default at all; only `keepAliveTime = 55`,
  `keepAliveTimeout = 20`, `keepAliveWithoutCalls = false`, `rpcDeadline = 0`, `connectTimeout = 10`
  genuinely have defaults. (b) the trailing `ConnectionConfig config` is printed without a default,
  so a required parameter follows defaultable ones — the rendered line is not valid Ballerina
  (the JSON does mark it `"optional": true`; the renderer just omits the `=`).
- **N3 — record field defaults dropped; defaultable fields shown as optional.**
  `ConnectionConfig.keepAliveTime = 55` (`types.bal:26`) renders as `int keepAliveTime?`; likewise
  `keepAliveTimeout`, `keepAliveWithoutCalls`, `rpcDeadline`, `connectTimeout`,
  `CreateCollectionRequest.primaryFieldName = "id"` (`types.bal:169`) and
  `Entry.primaryKey.fieldName = "id"` (`types.bal:87`). This both loses the default values and
  misstates required-with-default fields as optional.
- **N4 — `SearchResult` closed record rendered as open.** Source `types.bal:141` is
  `record {| … |}`; the render emits `record { … }`, implying the result may carry arbitrary extra
  fields.
- **N5 — parameter and return doc descriptions dropped for client methods.** e.g. `client.bal:38`
  `# + return - A list of collection names` and `client.bal:46` `# + request - The request to create
  a collection` are absent; every method doc in the render is the summary line followed by an empty
  `# `. The descriptions *are* present in the JSON (`parameters[].description`,
  `return.description`), so this is a renderer-side loss, not an extractor loss.

Not counted as issues (renderer conventions applied uniformly): `public` and `isolated` qualifiers
are stripped from all declarations; `returns Error?` is printed as `returns Error|()` for methods.

## 6. Coverage gaps vs. the library

**Zero.** The bala's `modules/` directory contains exactly one module (`milvus`), and `package.json`
declares `"export": ["milvus"]`, so the default module is the entire public API — there is no
submodule-only API and therefore no shared `getDefaultModule()` gap for this library.

Public symbols in the default module: 15 `public type` declarations in `types.bal`, `public type
Error` in `error.bal`, and `public isolated client class Client` with `init` + 8 `remote` methods.
All 16 types, the class, and all 9 methods appear in `new`. Non-public symbols correctly absent:
`Client.initiateClient` (private, `client.bal:32`), module-level `init()`/`setModule()`
(`init.bal:19,23` — not `public`).

## 7. Compiler plugin

The package has **no compiler plugin**. The bala has no `compiler-plugin/` directory and no
`compiler-plugin.json` (`ls` of the bala root shows only `bala.json`, `dependency-graph.json`,
`docs`, `modules`, `package.json`, `platform`, `resources`); upstream `v1.1.1` has no
`*compiler-plugin*` directory or `CompilerPlugin.toml` (`find -maxdepth 3` → no hits). The `native`
directory holds the JVM interop implementation (`io.ballerina.lib.milvus.Client` / `ModuleUtils`),
not a plugin. Nothing plugin-derived is therefore expected in the render, and nothing is missing.

## 8. Other considerations

- **Not deprecated.** Ballerina Central metadata for `ballerinax/milvus/1.1.1` returns an empty
  `deprecateMessage`, `pullCount` 2683, `ballerinaVersion` 2201.12.0, `graalvmCompatible: "No"`.
- **Version is stable (1.1.1)**, so the API surface is expected to be stable.
- **Encoding:** the extracted `readme` field carries CRLF line endings (110 `\r` characters) while
  the bala `docs/README.md` has none. Content is otherwise line-for-line identical
  (`difflib.unified_diff` → 0 diff lines). Present identically in old and new; cosmetic.
- **README contains raw HTML `<img>` tags and absolute `raw.githubusercontent.com` links** to the
  five images shipped in `resources/`. Harmless for an LLM, but ~40% of the render (111 of 343 lines)
  is README prose, of which the six image blocks are pure noise.
- **Size:** 343 lines total is small; no token-budget concern.
- **`TODO` in the source** (`client.bal:43`, "Add support for both dynamic fields and collection
  schema when creating a collection") is correctly not surfaced in the render.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/new render` | 342 / 343 |
| `diff -u old new` (full file) | 2 hunks, +3/−2; hunk 1 at old 120–126, hunk 2 at old 306–312 |
| `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 1 / 0 |
| `grep -n '^// --- '` new | lines 7, 119, 121, 305 (4 markers, same count in old) |
| `grep -c '^type '` old / new | 15 / 16 |
| `grep -c '^    remote function'` old / new | 8 / 8 |
| `grep -oE '^type …' \| sort` both | new = old ∪ {`Error`}; nothing removed |
| Python JSON compare: top-level keys | identical sets; `readme`, `description`, `name` equal; `functions`/`services`/`annotations` empty (0) on both |
| Python JSON compare: `typeDefs` | 16 vs 16, name sets equal; only `Error` differs — `new` adds `"baseType": "error"` |
| Python JSON compare: `clients[0]` | only `functions` differs; only `init` differs — 15 params → 14 (`Additional Values` dropped), return `ballerinax/milvus:1.1.1:Error?` → `Error?` |
| `git ls-remote --tags <repo>` | tags v1.0.0, v1.0.1, v1.1.0, **v1.1.1** (`1bf3213…`) — exact match cloned |
| `diff <upstream v1.1.1>/ballerina/*.bal <bala>/modules/milvus/*.bal` | identical for `client.bal`, `error.bal`, `init.bal`, `types.bal` |
| `diff <upstream>/ballerina/README.md <bala>/docs/README.md` | identical |
| `wc -l <bala>/modules/milvus/*.bal` | client 99, error 18, init 25, types 182 = 324 |
| `ls <bala>` / `ls <bala>/java21/modules` | no `compiler-plugin/`; single module `milvus` |
| `cat <bala>/java21/package.json` | `"export": ["milvus"]`, ballerina_version 2201.12.0, graalvmCompatible false |
| `find <upstream> -maxdepth 3 -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no hits |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/milvus/1.1.1` | 1 module, empty deprecate message, pullCount 2683 |
| Python: JSON `readme` vs bala README | line-for-line identical (0 unified-diff lines); JSON copy has 110 CR chars, file has 0; `old.readme == new.readme` → True |
| Source cites for §3/§5 | `error.bal:18`; `client.bal:21,28,32,38,39,43,46,48,56,64,72,80,88,96`; `types.bal:18-43,26,46-55,58-61,64-69,72-81,84-94,87,97-98,101-110,113-126,129-138,141-150,154-155,160-162,165-172,169,175-181`; `init.bal:19,23` |

## 10. Caveats and unverified items

- The renders were not re-generated; the audit compares the supplied `old`/`new` artefacts as given.
  That both were produced at the pinned version is taken from the brief's `PIN_OK` statement plus the
  version string `ballerinax/milvus:1.1.1:Error?` that appears in the `old` render — consistent, but
  the pipeline run itself was not reproduced.
- The `new` render was not fed to a Ballerina compiler. The claim in §5 N2 that the `init` line is not
  valid Ballerina rests on the language rule that required parameters must precede defaultable ones;
  it was reasoned about, not compiler-verified.
- The `native/` Java sources at `v1.1.1` were not read; the mapping from `@java:Method` externals to
  runtime behaviour is out of scope for a render audit and no render claim depends on it.
- Whether the spec-v2 renderer *intended* to drop the `Additional Values` rest-field parameter (as
  opposed to it being incidental) was not confirmed against the `ballerina-vscode` diff; only the
  effect on this library's output was measured.

# ballerinax/ai.pgvector 1.0.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.pgvector` |
| Pinned version | `1.0.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.pgvector |
| Tag reviewed | `v1.0.5` (exact match, commit `c988ae36a6a39249687bb4b77ddca79a706a6b42`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.pgvector/1.0.5` |
| Old render | `120` lines |
| New render | `136` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library has exactly three public symbols in its single (default) module: the class `VectorStore`,
the record type `Configuration`, and the enum `SimilarityMetric`. `old` rendered `VectorStore` as the
single degraded line `// Unknown type: VectorStore`, i.e. the entire client surface of this connector
— the constructor and all three operations — was invisible to any LLM consuming the render. `new`
emits the full class with its four methods, all parameter types, all defaults, and the `@display`
annotations. Nothing present in `old` was removed, reworded, or truncated: lines 1–119 are
byte-identical between the two files, and the only hunk replaces line 120 with the class body.

Public-API coverage in `new` is complete (3/3 public symbols, 4/4 public methods). No regressions
found. Six accuracy issues remain in `new` when checked against the published source; three of them
are newly *visible* because `new` renders the class at all, and three are pre-existing shared issues
in the `Configuration` / `SimilarityMetric` rendering that `old` had identically.

## 2. Change inventory

Line counts (`wc -l`): old **120**, new **136**. Diff: 1 hunk, +17 / −1, confined to lines 117–136.
Lines 1–119 identical (`diff` shows no other hunk).

| Kind | old | new | Delta |
|---|---|---|---|
| `// --- ` section markers | 3 | 3 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Module-level `const` | 3 | 3 | 0 |
| `type ... record` | 1 | 1 | 0 |
| `enum` | 1 | 1 | 0 |
| `class` | 0 | 1 | **+1** |
| Class methods rendered | 0 | 4 | **+4** |
| Version-qualified type refs in render | 0 | 0 | 0 |

Declarations **added** in `new` (5): `class VectorStore`, `function init`, `function add`,
`function delete`, `function query`.
Declarations **removed** in `new`: none.
Declarations **modified** in `new`: none (all of `COSINE`, `EUCLIDEAN`, `MANHATTAN`,
`Configuration`, `SimilarityMetric` and the README block are byte-identical).

### JSON-level change (upstream of the renderer)

The two JSON payloads differ in exactly one typeDef, `VectorStore`; `name`, `description`, `readme`,
`clients` (`[]`), `functions` (`[]`), `services` (`[]`), `annotations` (`[]`) and the other five
typeDefs compare equal. Within `VectorStore`, `new` adds:

- `"type": "Class"` — the discriminator whose absence made `old`'s `renderTypeDef` fall through to
  `// Unknown type:`. This is the root cause of the whole delta.
- `annotations` on all 9 `init` parameters (`@display {label: ...}`); annotation-bearing nodes went
  from 1 to 10 across the file.
- `init` return type normalized from `"ballerina/ai:1.13.0:Error?"` (old) to `"ai:Error?"` (new).
  Old JSON contained 1 version-qualified ref; new contains 0. It never surfaced in `old`'s render
  because the whole class was suppressed.

Method bodies, parameter lists, defaults, and doc strings for `add`/`delete`/`query` are unchanged
between the two JSONs.

## 3. Correctness against library source

Upstream `v1.0.5` `ballerina/*.bal` is byte-identical to the bala's `modules/ai.pgvector/*.bal`
(verified with `diff` on all three files), so GitHub and the bala agree; no tie-break needed.

Everything `new` adds, checked against `vector_store.bal`:

| Rendered (new) | Source | Verdict |
|---|---|---|
| `class VectorStore` | `vector_store.bal:28` `public isolated class VectorStore` | exists; `public isolated` dropped by renderer convention (see §5) |
| `init(string host, string user, string password, string database, string tableName = "vector_store", int port = 5432, postgresql:Options options = {}, sql:ConnectionPool connectionPool = {}, Configuration configs = {}) returns ai:Error?` | `vector_store.bal:47–56` | **exact match** — all 9 params, order, types, and all 5 defaults correct |
| `@display` labels on all 9 params | `vector_store.bal:48–56` | **exact match**, label-for-label |
| `add(ai:VectorEntry[] entries) returns ai:Error\|()` | `vector_store.bal:76` `returns ai:Error?` | correct (`E\|()` ≡ `E?`) |
| `delete(string\|string[] ids) returns ai:Error\|()` | `vector_store.bal:120` | **exact match** |
| `query(ai:VectorStoreQuery query) returns ai:VectorMatch[]\|ai:Error` | `vector_store.bal:139` | **exact match** |
| method doc strings | `vector_store.bal:71, 115, 134` | match the source doc first lines |
| `postgresql:Options` / `sql:ConnectionPool` "FROM" notes | imports at `vector_store.bal:18,20` | correct package attribution |

No invented symbols: every method rendered in `new` exists as a `public isolated function` in
`vector_store.bal`. The four private helpers on the class/module (`initializeDatabase`,
`sanitizeValue`, `generateFilter`, `serializeSparseEmbedding`, …) are correctly *not* rendered —
`utils.bal` contains no `public` declarations (`grep -n 'public' utils.bal` → no matches).

README: the render's lines 8–89 are byte-identical to the bala's `docs/README.md` (82 lines),
in both `old` and `new` (`diff` → identical). No truncation on either side.

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff -u old new` produces exactly one hunk, at old line 117–120 → new 117–136, with 1 removed
  line (`// Unknown type: VectorStore`) and 17 added lines. No other text changed anywhere.
- Declaration-set comparison: the set of declarations in `old` is a strict subset of `new`
  (0 removed, 5 added).
- JSON comparison: 7 of 8 top-level keys compare equal; the one differing typeDef only gains fields
  (`type`, `annotations`) and loses only the redundant version qualifier `ballerina/ai:1.13.0:` on a
  return type that never reached `old`'s render.
- README/section markers/const/record/enum blocks: identical byte-for-byte.
- Nothing in `new` is truncated, mangled, or less accurate than `old`; there is no declaration,
  parameter, default, return type, doc line, annotation, or README fragment that `old` had and
  `new` lacks.

## 5. Issues in `new` (independent of `old`)

Six inaccuracies vs. the published source survive in `new`. None is a regression; three are newly
*visible* only because `new` renders the class, three are shared with `old` verbatim.

**Newly visible (the class was suppressed in `old`, so these had no `old` counterpart):**

1. **Class doc is wrong — it is the constructor's doc, not the class's.** `new:120` reads
   `# Initializes the pgvector vector store with the provided configuration.` The real class doc
   (`vector_store.bal:23–27`) is *"Pgvector Vector Store implementation with support for Dense,
   Sparse, and Hybrid vector search modes. … This class implements the ai:VectorStore interface…"*.
   The substitution originates in the JSON (`typeDefs[VectorStore].description` is the init doc in
   **both** old and new JSON), not in the renderer. The lost sentence is the only place the library
   tells a consumer it implements `ai:VectorStore`.
2. **The `*ai:VectorStore` type inclusion is not rendered.** `vector_store.bal:29` declares
   `*ai:VectorStore;`. Neither JSON carries an inclusions field, so `new` shows a standalone class.
   Combined with (1), a consumer of the render has no way to know the README's own idiom —
   `ai:VectorStore vectorStore = check new(...)` at render line 55 — is valid. This is the most
   material remaining gap for LLM consumption.
3. **`public` and `isolated` qualifiers dropped** from the class and all four methods
   (`class VectorStore {`, `function init(...)`). `isolated` is load-bearing here: assigning the
   class to an `ai:VectorStore` (an isolated object type) requires it. Renderer convention, applied
   consistently (it also drops `public` from `type Configuration` and `enum SimilarityMetric`).

**Shared with `old` (identical text on both sides, listed for completeness):**

4. **`Configuration` loses its closedness and its defaults.** Source (`types.bal:43–48`) is
   `public type Configuration record {| ai:VectorStoreQueryMode embeddingType = ai:DENSE; int
   vectorDimension = 1536; SimilarityMetric similarityMetric = COSINE; |}` — a **closed** record with
   three **required** fields carrying defaults. Both renders emit an **open** `record { ... }` with
   all three fields marked optional (`?`) and no defaults. An LLM reading this would believe extra
   fields are permitted and would not know `vectorDimension` defaults to 1536 — the exact value the
   README's Step 2 sets explicitly.
5. **`SimilarityMetric` is rendered twice, incompatibly.** Both renders emit three module-level
   `const string COSINE/EUCLIDEAN/MANHATTAN` (lines 95–99) *and* an `enum SimilarityMetric` whose
   members reuse those same identifiers (lines 114–118) with the `= "<=>"` etc. values stripped. In
   real Ballerina this is a redefinition of `COSINE`/`EUCLIDEAN`/`MANHATTAN` and would not compile.
   Member order is also reversed vs. `types.bal:50–54` (source `COSINE, EUCLIDEAN, MANHATTAN`).
6. **Prefixed types used without imports.** The render's only import is
   `import ballerinax/ai.pgvector;` (line 5), yet `ai:`, `postgresql:` and `sql:` prefixes appear at
   lines 106, 123, 127, 131, 135. Partly mitigated by the trailing `// Special Agent Note: … FROM …`
   comments, which are accurate.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** The bala exports one module only (`package.json` `"export": ["ai.pgvector"]`;
Central `modules: ['ai.pgvector']`; `any/modules/` contains only `ai.pgvector`), so the
`getDefaultModule()`-only extraction limitation described in the brief cannot bite here — there are
no submodules.

Complete public surface of the default module (`grep -n 'public' *.bal`, 7 hits):

| Public symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `class VectorStore` | `vector_store.bal:28` | degraded to `// Unknown type:` | rendered in full |
| `VectorStore.init` | `vector_store.bal:47` | absent | rendered |
| `VectorStore.add` | `vector_store.bal:76` | absent | rendered |
| `VectorStore.delete` | `vector_store.bal:120` | absent | rendered |
| `VectorStore.query` | `vector_store.bal:139` | absent | rendered |
| `type Configuration` | `types.bal:43` | rendered | rendered |
| `enum SimilarityMetric` | `types.bal:50` | rendered | rendered |

Correctly excluded (non-public, so not part of the API): `SearchResult`, `Metadata` (`types.bal:26,
34`) and the seven `isolated function`s in `utils.bal` (lines 20, 41, 57, 68, 75, 103, 114).
No listeners, services, annotations, or `configurable` variables exist in the module
(`grep -n 'annotation \|listener \|^service \|configurable '` → no matches), consistent with the
JSON's empty `clients`, `functions`, `services`, `annotations` arrays on both sides.

## 7. Compiler plugin

**This package ships no compiler plugin.** The bala has no `compiler-plugin/` directory and no
`compiler-plugin.json` (`find` over the bala root shows only `bala.json`, `dependency-graph.json`,
`package.json`, `docs/`, `modules/`). The upstream repo at `v1.0.5` has no plugin module either
(`ls src` → `ballerina`, `build-config`, `examples`, `gradle`, plus build/metadata files). Nothing a
plugin would imply is therefore missing from the render.

## 8. Other considerations

- **Not deprecated.** Central reports `deprecated: None`, empty `deprecateMessage`, 2022 pulls,
  `graalvmCompatible: Yes`, built for distribution `2201.12.0`.
- **Pre-1.1 connector.** Version `1.0.5` is a young module (tags v1.0.0…v1.0.5 only); API churn is
  plausible across patch releases, but that is orthogonal to this review — both sides rendered the
  same 1.0.5 bala.
- **`ballerina/ai` version skew, now moot.** The bala's `dependency-graph.json` pins
  `ballerina/ai 1.12.0`, while `old`'s JSON emitted `ballerina/ai:1.13.0:Error?` — i.e. the old
  extractor stamped the *resolved-at-extraction-time* version (1.13.0, the pinned `ballerina/ai` in
  this run), not the version the package was built against. `new` drops the qualifier entirely
  (`ai:Error?`), which removes a class of misleading, environment-dependent output.
- **Size/tokens.** +16 lines (+13%), JSON 11,229 → 12,893 bytes (+14.8%). Trivial cost for
  recovering 100% of the connector's callable surface; this render remains one of the smallest in
  the set.
- **Consistency nit in `new`:** `init` returns `ai:Error?` while `add`/`delete` return
  `ai:Error|()`. Both are valid and semantically identical; the difference is inherited from the JSON
  (`"ai:Error?"` vs `"Error|()"`) and is present in `old`'s JSON too.

## 9. Evidence log

| # | Check (command / file:line) | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 120 / 136 |
| 2 | `wc -c old/*.json new/*.json` | 11,229 / 12,893 |
| 3 | `diff -u old new` (via precomputed diff, re-verified against files) | 1 hunk, +17/−1, lines 117–136 only |
| 4 | `grep -c '^// Unknown type:'` both renders | old 1, new 0 |
| 5 | `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | old 0, new 0 |
| 6 | `grep -oE '"[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:[^"]*"'` both JSONs | old: 1 × `"ballerina/ai:1.13.0:Error?"`; new: 0 |
| 7 | `grep -c '"annotations"'` both JSONs | old 1, new 10 |
| 8 | Python per-key JSON compare (`name/description/readme/typeDefs/clients/functions/services/annotations`) | only `typeDefs` differs |
| 9 | Python per-typeDef compare | 6 typeDefs each side, same names; only `VectorStore` differs |
| 10 | Full dump of `VectorStore` typeDef both sides | new adds `"type":"Class"` + 9 param `annotations`; return `ballerina/ai:1.13.0:Error?` → `ai:Error?`; `add`/`delete`/`query` identical |
| 11 | `git ls-remote --tags <repo>` | tags v1.0.0…v1.0.5; `v1.0.5` → `c988ae36a6a39249687bb4b77ddca79a706a6b42` |
| 12 | `git clone --depth 1 --branch v1.0.5` | succeeded; `src/ballerina/{types,utils,vector_store}.bal` |
| 13 | `diff src/ballerina/<f>.bal bala/modules/ai.pgvector/<f>.bal` × 3 | all three IDENTICAL |
| 14 | `src/ballerina/Ballerina.toml` | `version = "1.0.5"`, org `ballerinax`, name `ai.pgvector` — pin confirmed on the upstream side |
| 15 | `bala any/package.json` | `"version":"1.0.5"`, `"export":["ai.pgvector"]`, `graalvmCompatible: true` — pin confirmed on the bala side |
| 16 | `find bala -maxdepth 3` + `ls compiler-plugin` | no `compiler-plugin/`; modules dir holds only `ai.pgvector` |
| 17 | `ls src` (upstream root) | no compiler-plugin module |
| 18 | `wc -l bala/any/modules/ai.pgvector/*.bal` | types 54, utils 122, vector_store 263 = 439 |
| 19 | `grep -n 'public' *.bal` (bala module) | 7 hits: class + 4 methods (`vector_store.bal:28,47,76,120,139`), `types.bal:43,50` |
| 20 | `grep -n 'annotation \|listener \|^service \|configurable '` (bala module) | no matches |
| 21 | `grep -n 'function' utils.bal` | 7 functions, all non-public (lines 20,41,57,68,75,103,114) |
| 22 | `types.bal:43–48` read | `Configuration` is `record {| |}` with 3 required fields + defaults `ai:DENSE`, `1536`, `COSINE` |
| 23 | `types.bal:50–54` read | enum order `COSINE, EUCLIDEAN, MANHATTAN` with values `<=>`, `<->`, `<#>` |
| 24 | `vector_store.bal:23–29` read | class doc mentions Dense/Sparse/Hybrid + `ai:VectorStore` interface; `*ai:VectorStore;` inclusion at line 29 |
| 25 | `vector_store.bal:47–56` read vs `new:123` | 9 params, types, order, 5 defaults, 9 `@display` labels all match exactly |
| 26 | `wc -l bala docs/README.md` + `diff <(sed -n '8,89p' new render) docs/README.md` | 82 lines; IDENTICAL, no truncation |
| 27 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/ai.pgvector/1.0.5` | `deprecated: None`, pulls 2022, `modules: ['ai.pgvector']`, ballerinaVersion 2201.12.0 |
| 28 | `bala dependency-graph.json` filtered | `ballerina/ai 1.12.0`, `ballerina/sql 1.17.1`, `ballerinax/postgresql 1.17.0` |
| 29 | `grep -n 'import ' new render` | only `import ballerinax/ai.pgvector;` at line 5 (lines 48–49 are inside the README code block) |

## 10. Caveats and unverified items

- The `@display` label text, parameter defaults, and method signatures were verified against the
  source **by reading**, not by compiling. I did not build the package or compile the rendered
  `.bal.txt`; claims about non-compiling constructs (§5 item 5 — duplicate `COSINE`/`EUCLIDEAN`/
  `MANHATTAN` identifiers) are from reading the Ballerina spec rules, not from a compiler run.
- I did not independently re-run the two-stage extraction pipeline; the analysis of *why* `old`
  degraded `VectorStore` (missing `"type"` discriminator → `renderTypeDef` fallthrough) is inferred
  from the JSON delta plus the brief's description of `main`'s `renderTypeDef`, and matches the
  observed output exactly, but the `renderTypeDef` source itself was not read in this review.
- Whether the class-doc-vs-init-doc substitution (§5 item 1) and the missing `*ai:VectorStore`
  inclusion (§5 item 2) are intentional extractor design or oversights is **unverified** — I observed
  only that both JSONs behave identically, so neither is attributable to spec v2.
- `ai:VectorStoreQueryMode`, `ai:VectorEntry`, `ai:VectorStoreQuery`, `ai:VectorMatch`,
  `postgresql:Options`, `sql:ConnectionPool` were confirmed as the names used in this library's
  source; I did not open the `ballerina/ai`, `ballerinax/postgresql`, or `ballerina/sql` balas to
  confirm those types still exist at their resolved versions.

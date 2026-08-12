# ballerinax/ai.weaviate 1.0.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.weaviate` |
| Pinned version | `1.0.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.weaviate |
| Tag reviewed | `v1.0.5` (commit `a1923c9225effb9dd87193dbf82dd81a195b153d`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.weaviate/1.0.5` |
| Old render | `160` lines |
| New render | `176` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library is tiny: the default (and only) module `ai.weaviate` exports exactly three public
symbols — `Configuration`, `ConnectionConfig`, and `class VectorStore`. `old` rendered the first
two and degraded the class to a single `// Unknown type: VectorStore` line. `new` renders the class
in full: constructor + 3 methods, with parameter types, the `{}` default on `httpConfig`, and the
four `@display` annotations. Lines 1–159 are byte-identical between the two renders (verified by
`diff`), so the entire delta is the one hunk that replaces the placeholder.

No regression of any kind was found. `new` also drops the version-qualified type reference
`ballerina/ai:1.13.0:Error?` in favour of `ai:Error?` — which matters here because the bala's own
`dependency-graph.json` records `ballerina/ai 1.12.0`, i.e. the version-qualified string in `old`
was wrong for this published package.

Residual inaccuracies do exist in `new`, but they are renderer-model limitations shared with `old`
where `old` rendered the same construct, or newly visible only because `new` finally renders the
class at all (misattributed class doc, dropped `*ai:VectorStore` inclusion, dropped `public
isolated`, dropped per-parameter doc lines).

## 2. Change inventory

Line counts: `old` 160, `new` 176 (`wc -l`). One diff hunk, +17 / −1.

| Kind | old | new | delta |
|---|---|---|---|
| Top-level `type` (record) | 2 (`Configuration`, `ConnectionConfig`) | 2 (identical text) | 0 |
| `class` | 0 | 1 (`VectorStore`) | +1 |
| Class members rendered | 0 | 4 (`init`, `add`, `delete`, `query`) | +4 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| `@display` annotations rendered | 0 | 4 | +4 |
| `// Special Agent Note:` lines | 12 | 15 | +3 |
| `// --- section ---` markers | 3 (`README`, `END README`, `Types`) | 3 (same) | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) in render | 0 | 0 | 0 |
| Version-qualified type refs in JSON | 1 (`ballerina/ai:1.13.0:Error?`) | 0 | −1 |
| Declarations removed | — | — | 0 |

JSON-level delta (`typeDefs` length is 3 on both sides):
- `VectorStore.type` was absent in `old` JSON, is `"Class"` in `new` — this is exactly what unblocks
  `renderTypeDef` and eliminates the placeholder.
- `init` parameters gain an `annotations` array (4 × `display`) in `new`.
- `init.return.type.name`: `"ballerina/ai:1.13.0:Error?"` → `"ai:Error?"`.
- `add` / `delete` / `query` entries are otherwise byte-equivalent between the two JSONs.

README section: rendered lines 8–110 match `bala/.../docs/README.md` (102 lines) exactly except for
one trailing blank line — identical on both sides. No README content lost.

## 3. Correctness against library source

Upstream `v1.0.5` `ballerina/{types,utils,vector_store}.bal` are **byte-identical** to the bala's
`modules/ai.weaviate/*.bal` (`diff` returned no differences for all three files), so source and bala
agree and either can be cited.

Checked exhaustively (library is small enough):

| Rendered (new) | Source | Verdict |
|---|---|---|
| `class VectorStore` | `vector_store.bal:27` `public isolated class VectorStore` | exists; qualifiers dropped (see §5) |
| `function init(@display{...} string serviceUrl, @display{...} string apiKey, @display{...} Configuration config, @display{...} ConnectionConfig httpConfig = {}) returns ai:Error?` | `vector_store.bal:42-46` | param names, order, types, annotations, `= {}` default, and return type all match |
| `function add(ai:VectorEntry[] entries) returns ai:Error\|()` | `vector_store.bal:66` `public isolated function add(ai:VectorEntry[] entries) returns ai:Error?` | matches (`ai:Error\|()` ≡ `ai:Error?`) |
| `function delete(string\|string[] ids) returns ai:Error\|()` | `vector_store.bal:110` | matches |
| `function query(ai:VectorStoreQuery query) returns ai:VectorMatch[]\|ai:Error` | `vector_store.bal:136` | matches |
| `type Configuration { string collectionName; string chunkFieldName?; }` | `types.bal:24-28` | field names/types/optionality match; closedness lost (§5) |
| `type ConnectionConfig { ... 16 fields ... }` | `types.bal:30-61` | all 16 fields present, names and types match; defaults lost (§5) |

The three `Special Agent Note` cross-package attributions on the new lines are correct:
`VectorEntry`, `Error`, `VectorStoreQuery`, `VectorMatch` are all from `ballerina/ai` (imported at
`vector_store.bal:17`).

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff <(head -159 old) <(head -159 new)` → no output; the first 159 lines are identical, so nothing
  in the README or the two record types could have changed.
- The full unified diff is a single hunk at old 157–160 / new 157–176; it contains exactly one
  removed line (`// Unknown type: VectorStore`) and 17 added lines. `Declarations removed: 0`.
- Every declaration name present in `old` (`Configuration`, `ConnectionConfig`) is present in `new`
  with identical text; no parameter, default, doc line, or return type was dropped.
- No malformed syntax introduced: the added block is a well-formed class body with `;`-terminated
  method stubs.

## 5. Issues in `new` (independent of `old`)

Six inaccuracies vs. the library source. None is a regression (items 4–6 are also present in `old`,
items 1–3 concern a construct `old` did not render at all), but all could mislead an LLM.

1. **Class doc-string is the constructor's doc, not the class's.** `new` line 160 reads
   `# Initializes the Weaviate vector store with the given configuration.` The real class doc
   (`vector_store.bal:22-25`) is *"Weaviate Vector Store implementation with support for Dense,
   Sparse, and Hybrid vector search modes. This class implements the ai:VectorStore interface..."*.
   The misattribution originates in the JSON (`typeDefs[VectorStore].description` is the init doc in
   **both** old and new), so it is an extractor issue, not a `toSyntaxString` issue.
2. **`*ai:VectorStore` type inclusion is dropped.** Source `vector_store.bal:28`. The README block in
   the same render tells the consumer to write
   `ai:VectorStore vectorStore = check new weaviate:VectorStore(...)`; without the inclusion, the
   rendered class gives no evidence that this assignment type-checks. Highest-value omission here.
3. **`public` and `isolated` qualifiers dropped** on the class and on all four methods
   (`vector_store.bal:27, 42, 66, 110, 136`). An LLM cannot tell the methods are `isolated`, which
   matters for use inside `lock`/isolated contexts.
4. **Per-parameter doc lines dropped for class methods.** The JSON carries them (e.g.
   `entries` → *"The list of vector entries to add"*), but the render emits only the method summary.
   Same for the four `init` params.
5. **`ConnectionConfig` required-with-default fields are rendered as optional and their defaults
   lost.** Source `types.bal`: `http:HttpVersion httpVersion = http:HTTP_2_0`, `decimal timeout = 60`,
   `string forwarded = "disable"`, `http:Compression compression = http:COMPRESSION_AUTO`,
   `boolean validation = true`. All five render as `... name?;` with no default, in **both** renders.
6. **`Configuration` closed record rendered as open.** Source is `record {| ... |}`
   (`types.bal:24`); both renders emit `record { ... }`. Also, neither render marks the two record
   types `public`. Additionally the render's only top-level import is
   `import ballerinax/ai.weaviate;` (line 5) while the body uses `http:`, `weaviate:` and `ai:`
   prefixes — mitigated by the `Special Agent Note` comments, and identical on both sides.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.**

- `package.json` `export` = `["ai.weaviate"]`; `bala/.../modules/` contains exactly one directory,
  `ai.weaviate`. There are **no submodules**, so the known `getDefaultModule()`-only limitation
  cannot bite this library.
- Public symbols in the default module (from `grep -nE '^(public|type|isolated|...)'` over
  `types.bal` and `utils.bal`, plus `vector_store.bal`): `Configuration` (types.bal:24),
  `ConnectionConfig` (types.bal:30), `VectorStore` (vector_store.bal:27). All three appear in `new`.
- Correctly excluded because they are module-private: `type QueryResult` (types.bal:63) and the six
  non-public functions `convertWeaviateFilters`, `mapWeaviateOperator`, `mapWeaviateCondition`,
  `mapToGraphQLObjectString`, `getCollectionProperties` (utils.bal) and `deleteById`
  (vector_store.bal, end of file).
- Gap in `old`: 1 of 3 public symbols (`VectorStore`, i.e. the entire usable API surface) was
  degraded to a comment.

## 7. Compiler plugin

The package has **no compiler plugin**. `find` over the bala found no `compiler-plugin*` path and no
`compiler-plugin.json`; `find` over the upstream `v1.0.5` checkout found no `*compiler*plugin*`
directory, and `ballerina/Ballerina.toml` has no `[[tool.*]]` or plugin declaration (only `[package]`
and `[platform.java21] graalvmCompatible = true`). Nothing plugin-derived is therefore expected in,
or missing from, the render.

## 8. Other considerations

- **Version consistency.** Both renders are of `1.0.5`; the bala inspected is `1.0.5`; upstream tag
  `v1.0.5` exists and matches the bala byte-for-byte. No version drift.
- **Stale dependency version in `old`'s JSON.** `old` emitted `ballerina/ai:1.13.0:Error?` while the
  published `dependency-graph.json` for this bala records `ballerina/ai 1.12.0` (also `ballerina/http
  2.14.11`, `ballerinax/weaviate 1.0.2`). `new` emits the plain `ai:Error?`, avoiding the mismatch —
  an accuracy win, not just cosmetic.
- **Deprecation.** Ballerina Central reports `deprecated: null` for `ballerinax/ai.weaviate/1.0.5`
  (pullCount 2024). Not deprecated.
- **Pre-1.x?** No — `1.0.5` is a stable release, though early in the 1.0.x line.
- **Size/tokens.** The render is dominated by the README (lines 7–111, ~65% of the file). `new` adds
  17 lines (+10.6%) for the entire client API — an excellent accuracy-per-token trade.
- **Doc quality.** Source doc comments are complete (every param and return documented); the render
  discards the param-level ones (§5.4), so the render is materially less informative than the
  library's own API docs even after the improvement.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 160 / 176 |
| 2 | `git ls-remote --tags <repo>` | tags v1.0.0 … v1.0.5; `v1.0.5` → `a1923c9…` |
| 3 | `git clone --depth 1 --branch v1.0.5`; `git rev-parse HEAD` | `a1923c9225effb9dd87193dbf82dd81a195b153d`, `git describe` = `v1.0.5` |
| 4 | `diff src/ballerina/{types,utils,vector_store}.bal  bala/modules/ai.weaviate/…` | all three identical (SAME ×3) |
| 5 | `diff <(head -159 old) <(head -159 new)` | no differences → `IDENTICAL_1_159` |
| 6 | `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| 7 | `grep -n '^// --- '` old / new | both: 7, 111, 113 |
| 8 | `sed -n '159,160p' old` | last decl is `// Unknown type: VectorStore` |
| 9 | `Read new` lines 160–176 | class `VectorStore` with `init`, `add`, `delete`, `query` |
| 10 | JSON `typeDefs` names/kinds both sides | old: Record, Record, **(no type)**; new: Record, Record, **Class** |
| 11 | `grep -o 'ballerina/ai:[0-9.]*:Error?' old/*.json` | `ballerina/ai:1.13.0:Error?` (1 hit); new has `ai:Error?` |
| 12 | `grep -c '"annotations"' old/new json` | 1 / 5 (4 new `display` param annotations) |
| 13 | `grep -o '@display' new/*.bal.txt \| wc -l` | 4 |
| 14 | `grep -c 'Special Agent Note'` old / new | 12 / 15 |
| 15 | `grep -nE '^(public\|type\|isolated\|…)' bala types.bal utils.bal` | public: Configuration:24, ConnectionConfig:30; non-public: QueryResult:63 + 5 utils fns |
| 16 | `grep -n 'VectorStore' bala/vector_store.bal` | `:27 public isolated class VectorStore`, `:28 *ai:VectorStore`, `:136 public isolated function query(...)` |
| 17 | `sed -n '18,70p' bala/types.bal` | `Configuration` is `record {\|…\|}`; ConnectionConfig has 5 defaulted fields |
| 18 | `ls bala/.../modules/` and `package.json` `export` | single module `ai.weaviate`; export `["ai.weaviate"]` → no submodules |
| 19 | `find bala -iname '*compiler*'` / `find src -iname '*compiler*plugin*'` | no matches on either |
| 20 | `python3 -c` over `dependency-graph.json` | ai 1.12.0, http 2.14.11, time 2.8.1, weaviate 1.0.2 |
| 21 | `curl api.central.ballerina.io/.../ai.weaviate/1.0.5` | `deprecated: null`, 1 module, pullCount 2024 |
| 22 | `diff <(sed -n '8,110p' new) bala/docs/README.md` | only a trailing blank line differs (103d102) |
| 23 | `cat OLD_AND_NEW_DIFFS/ai.weaviate_diff.md` | +17/−1, 1 hunk, 5 declarations added, 0 removed — all figures reproduced independently above |

## 10. Caveats and unverified items

- The claim that the two renders came from the stated `ballerina-vscode` commits (`eb5d81b3` /
  `412ba01e`) is taken from the brief; the renderer source was not inspected in this review, so the
  attribution of each behaviour change to a specific renderer commit is **unverified**. The
  behaviours themselves (placeholder → class, annotations added, version-qualified ref removed) are
  verified from the artifacts.
- Whether `toSyntaxString` *intends* to omit `public`/`isolated`, type inclusions (`*ai:VectorStore`),
  and per-parameter doc lines for classes, or whether these are unintended drops, is **unverified** —
  it cannot be determined from this library's artifacts alone. They are reported as accuracy issues,
  not as defects with a known cause.
- `ballerina/ai` version discrepancy (1.13.0 in `old`'s JSON vs 1.12.0 in the bala dependency graph):
  the resolution path that produced 1.13.0 was not traced; only the two recorded values were
  verified.
- Nothing else was left unchecked — the library's entire public surface (3 symbols) was compared
  line-by-line against the bala and the tagged upstream source.

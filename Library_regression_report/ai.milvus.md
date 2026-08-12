# ballerinax/ai.milvus 1.0.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.milvus` |
| Pinned version | `1.0.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.milvus |
| Tag reviewed | `v1.0.4` (exact match; commit `2d17e1fe04398377c331f597974daffadd46ae09`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.milvus/1.0.4` |
| Old render | `130` lines |
| New render | `146` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Tiny library: one exported module (`ai.milvus`, the default module), three `.bal` files, exactly two
public symbols — `Configuration` (record) and `VectorStore` (class with `init`/`add`/`delete`/`query`).

`old` degraded the entire `VectorStore` class to a single `// Unknown type: VectorStore` line, i.e.
100% of the library's callable API was invisible to the LLM. `new` emits the full class with all four
methods, their parameters, defaults, `@display` annotations, and doc summaries. Nothing that `old`
contained was lost: lines 1–113 (header + README + `Configuration`) are byte-identical between the
two renders. There are no regressions.

Residual accuracy issues in `new` are all inherited from the JSON extractor and are minor
(`public`/`isolated` qualifiers dropped, `*ai:VectorStore` inclusion not shown, class doc taken from
`init`'s doc, record defaults dropped). None of them make `new` worse than `old`.

## 2. Change inventory

Line counts (`wc -l`): old 130, new 146. Diff: 1 hunk, +17 / −1, confined to lines 127–146.
Lines 1–113 verified byte-identical (`diff <(head -113 old) <(head -113 new)` → no output).

| Kind | old | new | Delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| `// --- section ---` markers | 3 (`README`, `END README`, `Types`) | 3 (same) | 0 |
| Record types rendered | 1 (`Configuration`, 4 fields) | 1 (identical) | 0 |
| Classes rendered | 0 | 1 (`VectorStore`) | +1 |
| Class methods rendered | 0 | 4 (`init`, `add`, `delete`, `query`) | +4 |
| Free functions / clients / services / annotations | 0 | 0 | 0 |
| Version-qualified type refs in render (`mod:1.2.3:Type`) | 0 | 0 | 0 |

Declarations **added** (5): `class VectorStore`, `function init`, `function add`, `function delete`,
`function query`. Declarations **removed**: 0. Declarations **modified**: 0 (`Configuration` is
character-for-character the same in both).

JSON-level diff (`diff <(json.tool old) <(json.tool new)`) — only 5 changes, all additive/normalising:

1. `typeDefs[1]` gains `"type": "Class"` (its absence in `old` is exactly why `renderTypeDef` fell
   through to `// Unknown type:`).
2. `init.parameters[0..3]` each gain an `annotations` entry carrying the `@display` label.
3. `init.return.type.name` changes `ballerina/ai:1.13.0:Error?` → `ai:Error?` (version-qualified ref
   normalised away). No other return type changed; `add`/`delete`/`query` already carried
   `Error|()` / `VectorMatch[]|Error` with `links` in both.

The rest of both JSONs (name, description, readme, `Configuration` fields, all doc strings, all
parameter names/types/defaults) is identical.

## 3. Correctness against library source

Bala module sources are byte-identical to upstream `v1.0.4` (`diff -q` on `types.bal`, `utils.bal`,
`vector_store.bal` → all IDENTICAL), and the bala README is identical to `ballerina/README.md`.
So GitHub and the bala agree; both were used.

Every added declaration in `new` checked against `ballerina/vector_store.bal`:

| new render | source | Verdict |
|---|---|---|
| `class VectorStore` (line 132) | `public isolated class VectorStore` — vector_store.bal:27 | exists; qualifiers dropped |
| `function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Milvus Configuration"} Configuration config, @display {label: "HTTP Configuration"} milvus:ConnectionConfig httpConfig = {}) returns ai:Error?` (line 133) | vector_store.bal:43–47 — same 4 params, same order, same `@display` labels, same `= {}` default, same `returns ai:Error?` | **exact match** |
| `function add(ai:VectorEntry[] entries) returns ai:Error\|()` (line 137) | `public isolated function add(ai:VectorEntry[] entries) returns ai:Error?` — vector_store.bal:71 | signature correct (`ai:Error\|()` ≡ `ai:Error?`) |
| `function delete(string\|string[] ids) returns ai:Error\|()` (line 141) | vector_store.bal:119 | signature correct |
| `function query(ai:VectorStoreQuery query) returns ai:VectorMatch[]\|ai:Error` (line 145) | vector_store.bal:136 | **exact match** |

Cross-package attributions in the `// Special Agent Note:` comments are correct:
`ConnectionConfig` is from `ballerinax/milvus` (import at vector_store.bal:20), and
`VectorEntry`/`Error`/`VectorStoreQuery`/`VectorMatch` are from `ballerina/ai` (import at
vector_store.bal:17). No invented symbols.

README section (render lines 8–112) matches `docs/README.md` (104 lines) exactly, modulo one trailing
blank line. No content lost, no encoding damage — the embedded `<img>` tags, fenced code blocks and
links all survive.

For a library this small the check is exhaustive: 2 public symbols, 4 public methods, all verified.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Lines 1–113 of the two renders are byte-identical (header, module description, whole README,
  `// --- Types ---` marker).
- `Configuration` (render lines 117–128) is byte-identical in both, including all four field names,
  types, `?` markers and doc comments.
- The only removed line in the entire diff is `// Unknown type: VectorStore`, which carried zero
  information.
- The JSON diff contains no deletions at all — every `<` line in the diff is a line that only lost a
  trailing comma or gained a sibling key; no field, parameter, default, doc string, or link was
  dropped.
- `grep -c '^// Unknown type:'`: old 1 → new 0. Section markers 3 → 3.

## 5. Issues in `new` (independent of `old`)

These exist in `new` regardless of `old`; none of them is a regression (in `old` this whole class was
absent), but they are fidelity gaps a reviewer should know about.

1. **`public` and `isolated` qualifiers dropped.** Source has `public isolated class VectorStore`
   (vector_store.bal:27) and `public isolated function` on all four methods (lines 43, 71, 119, 136).
   The render emits bare `class VectorStore` and `function <name>`. An LLM reading this cannot tell
   the class/methods are `isolated`, which matters when the caller is itself `isolated`.
2. **`*ai:VectorStore` type inclusion not rendered.** vector_store.bal:28 declares
   `*ai:VectorStore;`. The render omits it, so nothing in the class body says this class implements
   the `ai:VectorStore` interface — even though the README block immediately above it shows the
   canonical usage `ai:VectorStore vectorStore = check new milvus:VectorStore(...)`. This is the
   single most useful fact about the type and it is absent.
3. **Parameter and return doc descriptions dropped by the renderer.** The JSON carries them (e.g.
   `serviceUrl` → "The URL of the Milvus service"; `init.return.description` → "An error if the
   Milvus client initialization fails."), but the `.bal.txt` emits only the summary line followed by a
   stray empty `# ` line (render lines 131, 136, 140, 144). Information present in the JSON is lost at
   the render stage.
4. **Class description is the constructor's description.** The render (line 130) labels the class
   "Initializes the Milvus vector store with the given configuration." The actual class doc
   (vector_store.bal:22–26) is "Milvus Vector Store implementation with support for Dense, Sparse, and
   Hybrid vector search modes… implements the ai:VectorStore interface…". The extractor put `init`'s
   doc in `typeDefs[1].description` (identical in both JSONs), so this is a pre-existing extractor bug
   that only became visible now that the class renders at all. The correct, more informative text —
   including the "implements ai:VectorStore" sentence — never reaches the render.
5. **`Configuration` loses closedness and all default values** (shared with `old`, so not a
   regression). Source (types.bal:18–27) is a **closed** record `record {| … |}` with
   `string collectionName = "default"`, `string primaryKeyField = "id"`,
   `string[] additionalFields = []` and only `chunkFieldName` genuinely optional. The render emits an
   **open** `record { }` with all four fields marked `?` and no defaults. `public` is also dropped.
   Consequence: an LLM cannot learn that the default collection is `"default"` or the default primary
   key field is `"id"`, and may believe extra fields are allowed (they are not — the closed record
   would reject them at compile time).

Minor / not counted:
- `returns ai:Error|()` for `add`/`delete` vs `ai:Error?` for `init` — semantically identical, but
  inconsistent within the same class. Comes straight from the JSON `return.type.name`, unchanged
  between old and new.
- The render body uses declaration-only method stubs (`function …;`) inside `class`, which is not
  compilable Ballerina. This is the renderer's long-standing stub convention, not new — verified
  present in `old` renders of other libraries (e.g. `ai/old/ballerinax_ai.pinecone…`-style client
  stubs; `ai/old/*.bal.txt:2503` shows the same `function init(…) returns error?;` form).
- The render header imports only `ballerinax/ai.milvus`; the `ai:` and `milvus:` prefixes used in the
  class body have no corresponding import line. The `// Special Agent Note:` comments name the owning
  packages, which mitigates this.

## 6. Coverage gaps vs. the library

**0 gaps.** The bala exports exactly one module (`package.json` → `"export": ["ai.milvus"]`), which is
the default module, so there is no submodule-only API and therefore no shared `getDefaultModule()`
gap for this library.

Public symbols in the default module (`grep -n '^public\|public isolated function'` over the three
module sources): `Configuration` (types.bal:18), `VectorStore` (vector_store.bal:27) plus its four
public methods. All appear in `new`. `utils.bal` contains only module-private functions
(`generateFilter`, `generateValueField`, `combineElements`, `buildVectorMatch` — all non-`public`),
correctly absent from both renders.

For reference: `old` had 1 coverage gap (`VectorStore` and its 4 methods), now closed.

## 7. Compiler plugin

The package ships **no compiler plugin**. Verified: `find` over the upstream clone for
`*compiler-plugin*` / `CompilerPlugin.toml` returned nothing, and the bala contains no
`compiler-plugin/` directory (`ls -R` of the bala shows only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`). `Ballerina.toml` declares only `[package]` and
`[platform.java21]` — no `[[tool]]`, no plugin dependency. Nothing plugin-implied is therefore missing
from the render.

## 8. Other considerations

- **Version / deprecation**: Ballerina Central reports `deprecated: null`, empty `deprecateMessage`,
  pullCount 2027, single module `ai.milvus`. Version is post-1.0 and stable. Distribution
  `2201.12.0`, `graalvmCompatible = true`.
- **Size**: 146 lines / ~12.4 KB JSON — negligible token cost. 105 of the 146 render lines (72%) are
  README; the actual API surface is 16 lines. The README is high quality (setup guide, quick start,
  runnable snippets) and is the main value in this render.
- **No version drift**: both sides rendered the same 1.0.4 bala; bala sources are identical to the
  `v1.0.4` tag.
- The `new` render's `Configuration` block sits directly above the `VectorStore` class and is
  correctly referenced by the `init` signature, so an LLM can wire the two together — the one thing
  it will get wrong is the defaults (see §5.5).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | old 130, new 146 |
| `git ls-remote --tags <repo>` | `v1.0.4` → `2d17e1fe04398377c331f597974daffadd46ae09` (exact tag exists) |
| `git clone --depth 1 --branch v1.0.4 …` | succeeded into scratch `/…/work/ai.milvus/src` |
| `diff -q <bala>/modules/ai.milvus/{types,utils,vector_store}.bal <src>/ballerina/…` | all IDENTICAL |
| `diff <src>/ballerina/README.md <bala>/docs/README.md` | identical, 104 lines each |
| `diff <(head -113 old) <(head -113 new)` | no differences |
| `diff <(sed 8,112p new) <bala>/docs/README.md` | only a trailing blank line differs |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -n '^// --- '` | 3 markers in each, same line numbers (7, 113, 115) |
| `diff <(json.tool old.json) <(json.tool new.json)` | 5 changes: `"type":"Class"` added; 4 `@display` annotation arrays added; `ballerina/ai:1.13.0:Error?` → `ai:Error?`. Zero deletions |
| python: top-level JSON key counts | both: typeDefs 2, clients 0, functions 0, services 0, annotations 0 |
| python: `typeDefs[1]` keys | old `['name','description','functions']`; new `['name','description','type','functions']` |
| `grep -n '^public\|public isolated function' <src>/ballerina/*.bal` | types.bal:18 `public type Configuration record {\|`; vector_store.bal:27,43,71,119,136 |
| `cat <bala>/modules/ai.milvus/types.bal` | closed record with defaults `"default"`, `"id"`, `[]`; only `chunkFieldName?` optional |
| `cat <bala>/modules/ai.milvus/vector_store.bal` | `*ai:VectorStore;` at line 28; class doc at 22–26 differs from `init` doc at 37 |
| `find <src> -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no matches |
| `ls -R <bala>` | `bala.json`, `dependency-graph.json`, `docs/{README.md,icon.png}`, `modules/ai.milvus/{types,utils,vector_store}.bal`, `package.json` |
| `cat <bala>/package.json` | `"export": ["ai.milvus"]` — single (default) module |
| `curl api.central.ballerina.io/…/ai.milvus/1.0.4` | `deprecated: null`, 1 module, pullCount 2027 |
| `grep -m3 'returns .*;' ai/old/*.bal.txt` | stub-declaration syntax pre-exists in `old` renders (line 2503) |
| Precomputed diff `OLD_AND_NEW_DIFFS/ai.milvus_diff.md` | claims +17/−1, 1 hunk, 5 declarations added — independently reproduced and confirmed |

## 10. Caveats and unverified items

- The claim that `old`'s `// Unknown type: VectorStore` is caused by the missing `"type"` key in the
  JSON is inferred from the JSON diff plus the documented `renderTypeDef` behaviour in the brief; the
  `main` renderer source was not read directly. The observable facts (old JSON lacks `"type"`, old
  render degrades; new JSON has `"type":"Class"`, new render expands) are verified.
- Whether the missing `*ai:VectorStore` inclusion, the dropped `public`/`isolated` qualifiers, and the
  dropped parameter/return doc descriptions are extractor-side or renderer-side is only partly
  determined: the param/return docs are demonstrably present in the JSON and lost at render time; the
  type inclusion and the qualifiers are absent from the JSON, so they are lost at extraction time. No
  extractor/renderer code was read to confirm the mechanism.
- No attempt was made to compile the render — the "not compilable Ballerina" note is a syntax
  observation about declaration-only method stubs, and is a pre-existing convention, not a finding.

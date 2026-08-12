# ballerinax/ai.pinecone 1.1.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.pinecone` |
| Pinned version | `1.1.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.pinecone |
| Tag reviewed | `v1.1.5` (commit `5876722a6f2690e02d736d90c9476c80e6a69aee`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.pinecone/1.1.5` |
| Old render | `73` lines |
| New render | `89` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ai.pinecone` is a tiny library: one default module (`ai.pinecone`), three `.bal` files, and exactly
two public symbols — `public type Configuration record` and `public isolated class VectorStore`.

In `old`, `VectorStore` — the entire usable API surface of the library — was emitted as the single
line `// Unknown type: VectorStore`. `new` emits the real class with all four public methods
(`init`, `add`, `query`, `delete`), their full parameter lists, defaults, `@display` annotations and
return types. The JSON already contained the method data in `old`; the `old` renderer discarded it
because the typeDef carried no `"type"` tag (`new` adds `"type": "Class"`).

Nothing present in `old` is absent, truncated, or degraded in `new`. Zero regressions. The remaining
issues in `new` are pre-existing extractor/renderer limitations that were simply invisible before
because the class was not rendered at all.

## 2. Change inventory

Line counts (`wc -l`): old **73**, new **89** (+16 net; diff reports +17/−1, 1 hunk).

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 1 | 0 |
| `// --- ` section markers | 3 | 3 |
| version-qualified type refs (`mod:1.2.3:Type`) in render | 0 | 0 |

Declarations **added** in `new` (5):

| Kind | Name |
|---|---|
| class | `VectorStore` |
| class method (constructor) | `init` |
| class method | `add` |
| class method | `query` |
| class method | `delete` |

Declarations **removed**: none. Declarations **modified**: none (`Configuration` record is
byte-identical between the two renders; lines 1–71 of both files are identical).

JSON-level diff (`diff` of pretty-printed old vs new JSON) — 3 categories, no deletions:

1. `+ "type": "Class"` on the `VectorStore` typeDef (this alone is what unblocks rendering).
2. `+ "annotations": [{"name":"display","value":"{label: \"...\"}"}]` on all 5 `init` parameters.
3. `init` return type name `"ballerina/ai:1.13.0:Error?"` → `"ai:Error?"` (version-qualified ref
   dropped, matching the documented spec-v2 behaviour).

README section, package description, and the `Configuration` record are unchanged.

## 3. Correctness against library source

Upstream `v1.1.5` sources are byte-identical to the bala module sources (`diff` returned no
differences for `vector_store.bal`, `types.bal`, `utils.bal`), so both agree.

Every declaration `new` adds was checked against `modules/ai.pinecone/vector_store.bal`:

| Rendered (new) | Source | Verdict |
|---|---|---|
| `class VectorStore` | `vector_store.bal:32` `public isolated class VectorStore` | correct name; qualifiers dropped (§5) |
| `function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Query Mode"} ai:VectorStoreQueryMode queryMode = ai:DENSE, @display {label: "Pinecone Configuration"} Configuration config = {}, @display {label: "HTTP Configuration"} vector:ConnectionConfig httpConfig = {}) returns ai:Error?` | `vector_store.bal:49–53` | exact match — all 5 params, both defaults `ai:DENSE` / `{}` / `{}`, all 5 `@display` labels, return type |
| `function add(ai:VectorEntry[] entries) returns ai:Error\|()` | `vector_store.bal:72` `public isolated function add(ai:VectorEntry[] entries) returns ai:Error?` | semantically exact (`ai:Error\|()` ≡ `ai:Error?`) |
| `function query(ai:VectorStoreQuery queryVector) returns ai:VectorMatch[]\|ai:Error` | `vector_store.bal:102` | exact match |
| `function delete(string\|string[] refDocIds) returns ai:Error\|()` | `vector_store.bal:177` | semantically exact |

Cross-package type provenance in the "Special Agent Note" comments was verified against the imports
at `vector_store.bal:17–19`: `MetadataFilters`, `SparseVector`, `VectorStoreQueryMode`,
`VectorEntry`, `VectorStoreQuery`, `VectorMatch`, `Error` are all from `ballerina/ai`;
`ConnectionConfig` is from `ballerinax/pinecone.vector`. All notes are accurate.

`Configuration` (both renders) matches `types.bal:20–27` exactly: three optional fields
`namespace`/`filters`/`sparseVector` with the correct types and field docs.

README section in the render is character-identical to the bala's `docs/README.md` (only a trailing
blank line differs), for both sides — no README content lost.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Full textual diff of the two renders: a single hunk at old 70–73 / new 70–89, purely additive
  except for the removal of the `// Unknown type: VectorStore` placeholder line, which is replaced
  by the real definition.
- Diff of the two pretty-printed JSONs: no key or value is removed on the `new` side; all changes
  are additions plus one type-name de-qualification.
- Declaration extraction on both files: `old` has 1 top-level declaration (`type Configuration`),
  `new` has 2 (`type Configuration`, `class VectorStore`); nothing dropped.
- README, package header, `import` line, section markers, and the `Configuration` record are
  byte-identical between the two files (lines 1–71).
- No malformed constructs introduced: the added block is balanced (`class VectorStore { … }`), and
  the version-qualified `ballerina/ai:1.13.0:Error?` that `old`'s JSON carried never reaches either
  render (`old` swallowed it in the Unknown-type line).

## 5. Issues in `new` (independent of `old`)

All five below are extractor/renderer limitations, not regressions — the same data (or same
omission) exists in `old`'s JSON; they were invisible only because `old` refused to render the class.

1. **Class doc is the `init` doc, not the class doc.** JSON `typeDefs[VectorStore].description` is
   `"Initializes the PineconeVectorStore with the given configuration.\n"` — that is the docstring
   of `init` (`vector_store.bal:40`). The real class docstring at `vector_store.bal:21–31`
   ("Pinecone Vector Store implementation with support for Dense, Sparse, and Hybrid vector search
   modes…") is not captured anywhere. Consequence: the render never tells an LLM that DENSE /
   SPARSE / HYBRID modes exist or what they mean, and `init` itself is rendered with no doc comment
   because its doc was hoisted to the class. Identical `description` value in both JSONs → shared
   extractor gap.
2. **`*ai:VectorStore` type inclusion is dropped.** `vector_store.bal:33` includes the
   `ai:VectorStore` object type; the JSON has no inclusion/`typeInclusions` field at all. The render
   therefore does not state that this class implements `ai:VectorStore`, which is the whole point of
   the connector. Partially mitigated by the README snippet
   (`ai:VectorStore vectorStore = check new pinecone:VectorStore(...)`), which is preserved.
3. **`public` and `isolated` qualifiers omitted** on the class and on all four methods (source:
   `public isolated class` / `public isolated function` at lines 32, 49, 72, 102, 177). The JSON
   carries no `qualifiers` field. Cosmetic for comprehension, but the rendered `class VectorStore`
   is not usable as-is in an example.
4. **Parameter and return documentation present in JSON but dropped by the renderer.** Each
   parameter has a `description` in the JSON (e.g. `serviceUrl` → "URL of the Pinecone API service")
   and each function has a return `description` (e.g. `query` → "A list of matching ai:VectorMatch
   values, or an ai:Error on failure"); none of it reaches the `.bal.txt`. Lost signal for an LLM
   consumer.
5. **The rendered class body is not compilable Ballerina** — method declarations end in `;` with no
   body, which is `object type` syntax, not `class` syntax. This is the renderer's signature-stub
   convention rather than a library-specific defect, but it is worth knowing that the block cannot
   be pasted into a `.bal` file.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `"export": ["ai.pinecone"]` and `modules/` contains only `ai.pinecone` → there is
  no submodule API, so the `getDefaultModule()`-only extraction loses nothing here.
- Public symbols in the default module (`grep -nE '^public '` over the bala module):
  `types.bal:20 public type Configuration record` and
  `vector_store.bal:32 public isolated class VectorStore`. Both appear in `new`.
- Public class methods (`grep -nE '^    public '`): `init`, `add`, `query`, `delete` — all four
  appear in `new`.
- The 7 module-level functions in `utils.bal` (`mapPineconeOperator`, `mapPineconeCondition`,
  `convertPineconeFilters`, `getContent`, `mapEntryToVector`, `transformMetadata`,
  `createAiMetadata`) are all non-`public` `isolated function`s — correctly excluded from both
  renders.
- No listeners, services, annotations, constants, enums or module-level public functions exist in
  the library; the JSON's `clients`, `functions`, `services`, `annotations` arrays are empty on both
  sides, which is correct.

`old` had exactly one coverage gap — the whole `VectorStore` class — and `new` closes it.

## 7. Compiler plugin

The package ships **no compiler plugin**. Verified two ways:

- Upstream `v1.1.5` tree: `find` for any path matching `*compiler-plugin*` returns nothing; the repo
  contains only `ballerina/`, `build-config/`, `gradle/` and top-level metadata.
- Bala: `any/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json` — no `compiler-plugin/` directory and no `compiler-plugin.json`.

Consequently there are no plugin-contributed code actions, validations, generated artifacts or
annotations that ought to surface in the render. Nothing missing on this axis.

## 8. Other considerations

- **Version integrity.** `Ballerina.toml` at tag `v1.1.5` declares `version = "1.1.5"`,
  `org = "ballerinax"`, `name = "ai.pinecone"`; bala `package.json` agrees. Both renders were
  produced from the same pinned bala. No drift.
- **Library doc bug (upstream, not renderer).** `vector_store.bal:45` documents the parameter as
  `+ conf - Additional Pinecone configurations`, but the actual parameter at line 52 is named
  `config`. Because of the mismatch the extractor records `description: null` for `config` in both
  JSONs. Fixing this belongs upstream.
- **Upstream README is longer than the published one.** Repo root `README.md` is 94 lines; the
  packaged `ballerina/README.md` (= bala `docs/README.md`) is 49 lines and is what the pipeline
  consumes. Correct behaviour — the render faithfully reproduces the packaged README.
- **README contains a duplicated snippet.** The "Step 2" example declares
  `ai:VectorStore vectorStore` twice with near-identical arguments (render lines 47–55). This is a
  defect in the published README that both renders faithfully reproduce; it would be mildly
  confusing to an LLM (redeclaration of the same variable). Upstream issue, not a render issue.
- **Size/token impact.** +16 lines (~+22%) for the full API surface of the library — an excellent
  ratio. Total render is 89 lines, negligible token cost.
- **Practical impact of the change.** For this library specifically, `old` was effectively unusable:
  it described a vector-store connector without disclosing a single callable operation. `new` makes
  it usable.
- Package is post-1.0 (`1.1.5`), not deprecated, `graalvmCompatible = true`, built for distribution
  `2201.12.0`.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 73, new 89 |
| 2 | `git ls-remote --tags <repo>` | `v1.1.5` exists → `5876722a6f2690e02d736d90c9476c80e6a69aee` |
| 3 | `git clone --depth 1 --branch v1.1.5 …` | succeeded; `git log -1` = `5876722a…` |
| 4 | `cat src/ballerina/Ballerina.toml` | `version = "1.1.5"`, org `ballerinax`, name `ai.pinecone` |
| 5 | `diff src/ballerina/{vector_store,types,utils}.bal bala/modules/ai.pinecone/…` | all three IDENTICAL |
| 6 | `ls -R` bala | one module `ai.pinecone`; files `types.bal`, `utils.bal`, `vector_store.bal` |
| 7 | `cat bala/package.json` | `"export": ["ai.pinecone"]` → no submodules |
| 8 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 9 | `grep -c '^// --- '` | old 3, new 3 |
| 10 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` on renders | old 0, new 0 |
| 11 | `grep -cE '^(type\|class\|public \|function\|…) '` | old 1 top-level decl, new 2 |
| 12 | `diff <(json.tool old.json) <(json.tool new.json)` | only `+"type":"Class"`, +5 `annotations` blocks, `ballerina/ai:1.13.0:Error?`→`ai:Error?`; **zero deletions** |
| 13 | Python dump of `typeDefs[VectorStore]` both sides | same 4 functions, same params/defaults/descriptions on both sides; `description` = init's doc on both |
| 14 | `grep -nE '^public ' bala/modules/ai.pinecone/*.bal` | `types.bal:20`, `vector_store.bal:32` — only 2 public symbols |
| 15 | `grep -nE '^    public ' vector_store.bal` | lines 49, 72, 102, 177 → `init`, `add`, `query`, `delete` |
| 16 | `grep -cE '^isolated function' utils.bal` | 7 non-public functions (correctly excluded) |
| 17 | `diff bala/docs/README.md <(sed -n '8,57p' new render)` | only `49a50 >` (trailing blank line) → README preserved verbatim |
| 18 | `find` for `*compiler-plugin*` in upstream tree, `ls` bala `any/` | no compiler plugin in either |
| 19 | `wc -l` upstream `README.md` vs `ballerina/README.md` | 94 vs 49 — packaged README is the shorter one, and is what is rendered |
| 20 | Manual signature comparison, render lines 76/80/84/88 vs `vector_store.bal:49–53,72,102,177` | all match |

## 10. Caveats and unverified items

- I did not execute the two-stage pipeline myself; I audited the delivered JSON and `.bal.txt`
  artefacts. The claim that both sides used the same pinned bala is taken from the manifest and the
  brief (`PIN_OK`), corroborated by the two renders' identical README/description/`Configuration`
  output, but not independently re-run.
- The commit identities of the two `ballerina-vscode` sides (`eb5d81b3` / `412ba01e`) are taken from
  the brief; I did not inspect the extractor/renderer source, so statements about *why* `old`
  degraded the class (missing `"type"` tag) are inferred from the JSON diff, not read from code.
- `ai:Error|()` vs `ai:Error?` is asserted to be semantically identical on the strength of the
  Ballerina type system (`T?` is sugar for `T|()`); not verified by compiling the render.
- Claim 5 in §5 (class body not compilable) is a judgement about Ballerina grammar, not the output
  of a compiler run — the render was not fed to `bal build`.

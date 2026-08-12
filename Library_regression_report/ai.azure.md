# ballerinax/ai.azure 1.5.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.azure` |
| Pinned version | `1.5.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.azure |
| Tag reviewed | `v1.5.0` (commit `46db51d85f26867e25b197013d0d77ab84f692b7`, 2026-08-05) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.azure/1.5.0/java21` |
| Old render | `262` lines |
| New render | `297` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old`: nothing is dropped, and three classes of `old` defect are
fixed — the `// Unknown type: AiSearchKnowledgeBase` placeholder becomes a real class body with all
four public methods, the two `ballerina/ai:1.13.0:Error?` version-qualified return types collapse to
`ai:Error?`, and 31 `@display` annotations plus the module's one `public annotation`
(`JsonSchema`) now appear. The `@display` count matches the bala source exactly (31 = 31).

The newly-surfaced `AiSearchKnowledgeBase` body carries several inaccuracies that come from the
extractor JSON (they are present in the `old` JSON too, but `old`'s renderer never printed them):
a doubled `ai:ai:Document` type prefix, a wrong `maxLimit` default (`0` instead of `10`), and three
unquoted/unqualified default-value literals. These are new *render* issues but not regressions —
nothing correct in `old` was made worse.

## 2. Change inventory

Counts from the two `.bal.txt` files:

| Metric | old | new |
|---|---|---|
| Total lines | 262 | 297 |
| `// Unknown type:` placeholders | 1 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:`) | 2 | 0 |
| Section markers `// --- ` | 4 | 5 |
| Top-level declarations (`const`/`type`/`enum`/`class`/`annotation`) | 13 | 15 |
| Class member functions | 6 | 10 |
| `@display` occurrences | 0 | 31 |

Declaration-set diff (`grep -oE '^(public )?(client )?(class|type|enum|const|annotation) [A-Za-z_]+' | sort`):

- **Added (2 top-level):** `class AiSearchKnowledgeBase`, `public annotation map<json> JsonSchema on type`
- **Removed:** none
- **Added (4 member functions, all inside `AiSearchKnowledgeBase`):** `init`, `ingest`, `retrieve`, `deleteByFilter`
- **New section:** `// --- Annotations ---` (new line 295)

Modified (3 lines, all signature lines):

| Line (new) | Change |
|---|---|
| 262 | `EmbeddingProvider.init` — `returns ballerina/ai:1.13.0:Error?` → `returns ai:Error?`; 5 `@display` annotations added to params |
| 283 | `OpenAiModelProvider.init` — same version-qualifier fix; 8 `@display` annotations added |
| 292 | `OpenAiModelProvider.generate` — `@display {label: "Expected type"}` added to `td` |

Annotation additions on types: `@display {label: "Connection Configuration"}` on `ConnectionConfig`
(new:155), one `@display` per each of its 14 fields, `@display {label: "OpenAI API Type"}` on
`ApiType` (new:213).

README section (lines 1–126) is byte-identical between the two renders (`diff` returned no output).

JSON-level diff: `typeDefs` 12 → 12, `clients` 2 → 2, `functions` 0 → 0, `services` 0 → 0,
`annotations` 0 → 1. `AiSearchKnowledgeBase` exists in **both** JSONs; `old` lacks the `"type"`
field, `new` has `"type": "Class"` — that is exactly why `old`'s `renderTypeDef` degraded it.
Its `functions` payload is identical between the two JSONs except the `ai:Error?` return-type
qualifier.

## 3. Correctness against library source

The `v1.5.0` tag's `ballerina/*.bal` files are byte-identical to the bala's
`modules/ai.azure/*.bal` (`diff -r --brief` reported differences only for non-`.bal` project files:
`Ballerina.toml`, `CompilerPlugin.toml`, `Dependencies.toml`, `README.md`, `build.gradle`,
`icon.png`, `tests/`). So GitHub and the bala agree.

Verified additions in `new`:

| Render (new) | Source | Verdict |
|---|---|---|
| `class AiSearchKnowledgeBase` (236) | `azure_ai_search_knowledgebase.bal:78` `public distinct isolated class AiSearchKnowledgeBase` | exists; qualifiers dropped (see §5) |
| `function init(...) returns ai:Error?` (237) | `azure_ai_search_knowledgebase.bal:113–120` | 11 params, order and names all match |
| `function ingest(...) returns ai:Error\|()` (240) | `azure_ai_search_knowledgebase.bal:187` `ingest(ai:Chunk[]\|ai:Document[]\|ai:Document documents) returns ai:Error?` | name/arity match; type string mangled (§5) |
| `function retrieve(string query, int maxLimit = 0, ...)` (244) | `azure_ai_search_knowledgebase.bal:239–240` `retrieve(string query, int maxLimit = 10, ai:MetadataFilters? filters = ())` | **default wrong** (§5) |
| `function deleteByFilter(ai:MetadataFilters filters) returns ai:Error\|()` (248) | `azure_ai_search_knowledgebase.bal:333` | exact match |
| `public annotation map<json> JsonSchema on type;` (297) | `to_json_schema.bal:32` `public annotation map<json> JsonSchema on type;` | exact match |
| 31 `@display` annotations | `grep -o '@display' modules/ai.azure/*.bal \| wc -l` = 31 | count matches exactly; labels spot-checked against `types.bal:19–76`, `model-provider.bal:87–95`, `model-provider.bal:149`, `embedding_provider.bal:62–67` — all identical |
| `returns ai:Error?` on both `init`s | `model-provider.bal:95`, `embedding_provider.bal:67` both `returns ai:Error?` | correct; `old`'s `ballerina/ai:1.13.0:Error?` was the wrong form |

Unchanged content re-verified against source:

- `ConnectionConfig` 14 fields, names and order — `types.bal:20–77`. Match.
- `ApiType` members `RESPONSES`, `CHAT_COMPLETIONS` — `types.bal:93–99`. Match (render lists them in
  reverse source order; the JSON `members` array carries that order on both sides).
- `ReasoningEffort` members — `types.bal:106–119`. All six present.
- 8 constants with values `"chat_completions"`, `"responses"`, `"none"`, `"minimal"`, `"low"`,
  `"medium"`, `"high"`, `"xhigh"` — these are the enum member values from `types.bal:93–119`. Correct.
- `EmbeddingProvider.embed` render `returns ai:Vector|ai:SparseVector|ai:HybridVector|ai:Error`
  vs. source `returns ai:Embedding|ai:Error` (`embedding_provider.bal:92`) — correct expansion:
  `ballerina/ai` `rag-types.bal:37` defines `public type Embedding Vector|SparseVector|HybridVector`.
- `OpenAiModelProvider.chat` signature — `model-provider.bal:134–136`. Match.
- `chunker` type expansion `ai:Chunker|"AUTO"|"DISABLE"` vs. source `ai:Chunker|ai:AUTO|ai:DISABLE` —
  correct: `ballerina/ai` `types.bal:122` defines `public const AUTO = "AUTO"`.

## 4. Regressions

**None found.**

Checked:
- Declaration-set diff of the two renders: 0 removed, 2 added at top level, 4 added as members.
- Unified diff of the two files: 4 removed lines total — one is the `// Unknown type:` placeholder,
  the other three are the signature lines replaced by strictly richer versions of themselves
  (`old`'s `ballerina/ai:1.13.0:Error?` → `ai:Error?`, plus `@display` additions). No parameter,
  default, return type, or doc comment is lost on any of the three.
- README block (lines 1–126) diffed: identical.
- All 8 constants, `ConnectionConfig`'s 14 fields, both enums' 8 members, and all 6 pre-existing
  member functions present in `old` are present verbatim in `new`.

## 5. Issues in `new` (independent of `old`)

All seven are inside the newly-surfaced `AiSearchKnowledgeBase` block; all trace to the extractor
JSON, which is byte-identical on both sides for this class (only `old` never rendered it).

1. **Doubled module prefix — malformed type** (new:240):
   `function ingest(ai:Chunk[]|ai:ai:Document[]|ai:ai:Document documents)`.
   Source is `ai:Chunk[]|ai:Document[]|ai:Document` (`azure_ai_search_knowledgebase.bal:187`).
   Cause: the JSON type is `"Chunk[]|Document[]|Document"` with **three** `links` entries, two of
   which are both `recordName: "Document"` — the prefixing pass applies `ai:` twice.
   `ai:ai:Document` is not valid Ballerina.
2. **Wrong default value** (new:244): `int maxLimit = 0`. Source default is `10`
   (`azure_ai_search_knowledgebase.bal:239`). The JSON carries `"default": "0"`. This is actively
   misleading: the method's own guard is `if maxLimit != -1 && maxLimit <= 0 { return error ... }`
   (`azure_ai_search_knowledgebase.bal:241–243`), so an LLM told the default is `0` may believe the
   default call errors.
3. **Unquoted string default** (new:237): `string apiVersion = 2025-09-01`. Source default is the
   const `AI_AZURE_KNOWLEDGE_BASE_API_VERSION = "2025-09-01"`
   (`azure_ai_search_knowledgebase.bal:25`). The const was inlined but the quotes were dropped —
   `2025-09-01` is a subtraction expression, not a string; the line does not compile.
4. **Unquoted string default** (new:237): `string contentFieldName = content`. Source const is
   `CONTENT_FIELD_NAME = "content"` (`azure_ai_search_knowledgebase.bal:23`). Same defect; `content`
   reads as an undefined identifier.
5. **Unqualified default symbol** (new:237): `ai:Chunker|"AUTO"|"DISABLE" chunker = AUTO`. Source is
   `chunker = ai:AUTO`. Bare `AUTO` is not in scope in a consumer's file.
6. **Class doc replaced by constructor doc** (new:234): the render shows
   `# Initializes a new AiSearchKnowledgeBase instance.` as the class-level doc. The class's real doc
   is `# Represents the Azure Search Knowledge Base implementation.`
   (`azure_ai_search_knowledgebase.bal:77`); the shown text is `init`'s doc
   (`azure_ai_search_knowledgebase.bal:105`). The JSON's `description` for the typeDef is already the
   constructor's text, so this is an extractor-side mis-attribution.
7. **Qualifiers and type inclusion dropped** (new:236): rendered as `class AiSearchKnowledgeBase`;
   source is `public distinct isolated class AiSearchKnowledgeBase { *ai:KnowledgeBase; ... }`
   (`azure_ai_search_knowledgebase.bal:78–79`). The `*ai:KnowledgeBase` inclusion is the fact that
   tells a consumer this type is usable wherever an `ai:KnowledgeBase` is expected — a material
   omission for an agent-building library.

**Shared inaccuracies present in BOTH renders** (listed for completeness — not regressions, and not
counted above):

- Included-record parameters lose their `*`: `*ConnectionConfig config` /
  `*ConnectionConfig connectionConfig` (`embedding_provider.bal:67`, `model-provider.bal:94`) render
  as ordinary `ConnectionConfig config` params, wrongly implying a single positional record argument
  rather than spread-in named args. Present in `old` (line 231/252) and `new` (262/283).
- `generate`'s inferred typedesc param `typedesc<anydata> td = <>` (`model-provider.bal:149`) renders
  as `anydata td = anydata` on both sides — not valid Ballerina.
- `ConnectionConfig` is a closed record `record {| |}` (`types.bal:20`) but renders as open
  `record { }`; its defaulted fields (`httpVersion = http:HTTP_2_0`, `timeout = 60`,
  `forwarded = "disable"`, `compression = http:COMPRESSION_AUTO`, `validation = true`) render as
  optional `?` fields with the defaults lost. Both sides.
- Enum member values are dropped in the enum bodies (`RESPONSES` not `RESPONSES = "responses"`),
  though the values do survive as the 8 top-level constants. Both sides.
- `public` / `isolated` / `distinct` qualifiers are absent throughout on both sides.

## 6. Coverage gaps vs. the library

The bala contains exactly one module, `modules/ai.azure` — the default module
(`ls .../1.5.0/java21/modules` → `ai.azure`). Ballerina Central metadata for
`ballerinax/ai.azure/1.5.0` also lists a single module, `ai.azure`. **There is no submodule-only API,
so the shared `getDefaultModule()` limitation costs nothing here.**

Complete list of public symbols in the default module and their render status:

| Symbol | Kind | Source | old | new |
|---|---|---|---|---|
| `ConnectionConfig` | record | `types.bal:21` | present | present |
| `ApiType` | enum | `types.bal:93` | present | present |
| `ReasoningEffort` | enum | `types.bal:106` | present | present |
| `JsonSchema` | annotation | `to_json_schema.bal:32` | **missing** | present |
| `OpenAiModelProvider` | client class | `model-provider.bal:36` | present | present |
| `EmbeddingProvider` | client class | `embedding_provider.bal` (init at :62) | present | present |
| `AiSearchKnowledgeBase` | class | `azure_ai_search_knowledgebase.bal:78` | **degraded to `// Unknown type:`** | present |

**Coverage gaps in `new`: 0.** Gaps in `old`: 2. Everything else at module level
(`ResponseSchema`, `DocumentContentPart`, `AzureChat*`, `Responses*`, `IndexSchemaInfo`,
`JsonSchema`/`JsonArraySchema` records, the `const` helpers, and ~60 module-private functions) is
non-`public` and correctly excluded.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.lib.ai.azure.AiAzureCompilerPlugin`,
shipped as `ai.azure-compiler-plugin-1.5.0.jar` plus `ballerina-to-openapi-2.3.0.jar`.

`AiAzureCompilerPlugin.init` registers exactly one thing: `context.addCodeModifier(new AiAzureCodeModifier())`.
The modifier's work is in `GenerateMethodModificationTask`, which rewrites `->generate(...)` remote
call sites: it resolves the expected `typedesc<anydata>` at the call site and injects the JSON schema
for it. That is why `generate` is declared `typedesc<anydata> td = <>` and is `external`
(`model-provider.bal:149–152`, `@java:Method {'class: "io.ballerina.lib.ai.azure.Generator"}`), and
why `public annotation map<json> JsonSchema on type` exists — the plugin attaches the generated
schema through it.

The plugin contributes **no** code actions, no diagnostics/validators, and no additional public
symbols. Nothing the plugin implies is missing from `new`: the one artifact it depends on
(`JsonSchema`) is now rendered, and it was the symbol `old` dropped. The `<>` inferred-typedesc form
is not conveyed by either render (see §5, shared list) — a reader of either render will not learn
that `td` is inferred from the LHS binding rather than passed.

## 8. Other considerations

- Version `1.5.0`, stable (≥1.0), not deprecated — Central returns `deprecateMessage: ""` and no
  `deprecated: true` flag.
- Size impact is negligible: +35 lines (+13.4%). Most of the growth is the `AiSearchKnowledgeBase`
  body (16 lines) and inline `@display` annotations.
- The 14 per-field `@display` annotations on `ConnectionConfig` add 14 lines of low-information
  content (each label is a title-cased restatement of the field name). They are faithful to the
  source but contribute little for an LLM consumer.
- The README block is substantial (119 lines) and high quality: routing matrix tables, v1-GA vs.
  legacy URL rules, and runnable quickstart snippets. It is preserved identically. Note the README
  documents only `OpenAiModelProvider` and `EmbeddingProvider` — the new `AiSearchKnowledgeBase` is
  absent from it, so the render's class body is the only place a consumer learns about it. That makes
  the §5 defects in that block more consequential than they would otherwise be.
- README contains a pre-existing typo, "the nessary configuration" (new:69), and jumps from
  "Step 2" to "Step 4" (new:87, 116). Both come from the published README; both renders reproduce
  them faithfully.
- `ReasoningEffort` is a declared public enum but is never referenced by name in the render — the
  `reasoningEffort` param is expanded to `"xhigh"|"high"|"medium"|"low"|"minimal"|"none"|()` on both
  sides. Behaviourally equivalent, but the link between the enum and the parameter is invisible.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 262 / 297 |
| 2 | `grep -c '^// Unknown type:'` on both | old 1, new 0 |
| 3 | `grep -n '^// --- '` on both | old: 7,125,127,220 (4); new: 7,125,127,251,295 (5) |
| 4 | `grep -oE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` | old 2, new 0 |
| 5 | `grep -o '@display' \| wc -l` on renders | old 0, new 31 |
| 6 | `grep -o '@display' bala/modules/ai.azure/*.bal \| wc -l` | 31 — matches new exactly |
| 7 | `grep -cE '^(public )?(client )?(class\|type\|enum\|const\|annotation) '` | old 13, new 15 |
| 8 | `grep -cE '^    (remote )?function '` | old 6, new 10 |
| 9 | `diff <(grep -oE '^...decl...' old\|sort) <(... new\|sort)` | only `+class AiSearchKnowledgeBase`, `+public annotation map`; nothing removed |
| 10 | `diff <(sed -n 1,126p old) <(sed -n 1,126p new)` | no output — README identical |
| 11 | `git ls-remote --tags <repo>` | `v1.5.0` present → `46db51d85f26867e25b197013d0d77ab84f692b7` |
| 12 | `git clone --depth 1 --branch v1.5.0` then `diff -r --brief src/ballerina bala/modules/ai.azure` | all `.bal` files identical; only project files (`Ballerina.toml`, `CompilerPlugin.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png`, `tests/`) are repo-only |
| 13 | `ls bala/.../modules` and Central API `modules[]` | single module `ai.azure` (= default module) |
| 14 | Python compare of both JSONs' top-level arrays | typeDefs 12/12, clients 2/2, functions 0/0, services 0/0, annotations 0/1 (`+JsonSchema`) |
| 15 | Python dump of `typeDefs[*].type` | `AiSearchKnowledgeBase` has no `type` in old, `"Class"` in new — root cause of the placeholder |
| 16 | Python unified diff of `AiSearchKnowledgeBase.functions` old vs new | single hunk: `ballerina/ai:1.13.0:Error?` → `ai:Error?` |
| 17 | `azure_ai_search_knowledgebase.bal:239` | `retrieve(string query, int maxLimit = 10, ...)` vs render `= 0` |
| 18 | JSON `retrieve.parameters[1].default` | `"0"` — extractor-side, identical in both JSONs |
| 19 | JSON `ingest.parameters[0].type.links` | 3 entries, `Document` listed twice → `ai:ai:Document` |
| 20 | `azure_ai_search_knowledgebase.bal:23,25` | `CONTENT_FIELD_NAME = "content"`, `AI_AZURE_KNOWLEDGE_BASE_API_VERSION = "2025-09-01"` — quotes lost in render |
| 21 | `azure_ai_search_knowledgebase.bal:77,78` | class doc `# Represents the Azure Search Knowledge Base implementation.`; `public distinct isolated class`, `*ai:KnowledgeBase` |
| 22 | `bala/ballerina/ai/1.13.0/.../rag-types.bal:37` | `public type Embedding Vector\|SparseVector\|HybridVector` — confirms `embed` expansion correct |
| 23 | `bala/ballerina/ai/1.13.0/.../types.bal:122` | `public const AUTO = "AUTO"` — confirms `"AUTO"\|"DISABLE"` expansion correct |
| 24 | `to_json_schema.bal:32` | `public annotation map<json> JsonSchema on type;` — exact match to new:297 |
| 25 | `model-provider.bal:149` | `generate(ai:Prompt prompt, @display {label: "Expected type"} typedesc<anydata> td = <>)` |
| 26 | `AiAzureCompilerPlugin.java` (tag v1.5.0) | registers only `AiAzureCodeModifier`; no code actions, no analyzers |
| 27 | `curl api.central.ballerina.io/.../ai.azure/1.5.0` | `deprecateMessage: ""`, platform `java21`, one module |
| 28 | grep for module-level `public function` / `public const` in bala | none — public surface is the 7 symbols in §6 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific lines are "not valid Ballerina"
  (`ai:ai:Document`, `apiVersion = 2025-09-01`, `contentFieldName = content`, `chunker = AUTO`,
  `td = anydata`) are from reading the grammar, not from a `bal build`.
- The compiler plugin was reviewed from Java source at tag `v1.5.0`, not by decompiling the shipped
  `ai.azure-compiler-plugin-1.5.0.jar`. The two are assumed to correspond because every `.bal` file
  in the tag matches the bala byte-for-byte (evidence #12), but the jar itself was not byte-compared.
- Whether the doubled `ai:` prefix and the wrong `maxLimit` default originate in
  `CopilotLibraryManager` or upstream in the Ballerina docs/semantic model was not traced past the
  JSON — both JSONs contain the defects identically, so they are not attributable to the spec-v2
  renderer change.
- `ReasoningEffort`'s render order (XHIGH→NONE) is the reverse of source order (NONE→XHIGH) and
  `ApiType`'s is likewise reversed. This holds on both sides and was not investigated further; it
  has no semantic effect.

# ballerina/ai 1.13.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/ai` |
| Pinned version | `1.13.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-ai |
| Tag reviewed | `v1.13.0` (commit `20e4313`, exact match) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/ai/1.13.0/java21` |
| Old render | `2683` lines |
| New render | `3172` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` in content. Nothing present in `old` was dropped, truncated or
made less accurate. The extractor produced an identical type inventory on both sides
(`typeDefs` = 265, `clients` = 3, `functions` = 15, `services` = 1 in both JSONs); the entire delta
comes from the renderer.

Three classes of improvement:

- **49 `// Unknown type:` placeholders eliminated (49 → 0).** All 49 previously-degraded symbols now
  render with real definitions — 27 error types, 17 classes, and 5 type aliases
  (`FunctionTool`, `Url`, `Vector`, `Context`, plus the `client class` upgrades).
- **88 version-qualified type references removed (`ballerina/ai:1.13.0:Type` → `Type`), across 39 lines.**
- **Annotations section added** (`JsonSchema`, `AgentTool`) — absent from `old` entirely; and
  **53 `@display` annotations recovered** (3 → 56).
- Two invalid-Ballerina keyword identifiers fixed: `string type;` → `string 'type;` (2 sites) and
  `json const;` → `json 'const;`; `XmlSchema xml?` → `XmlSchema 'xml?` (13 sites). The `old` forms do
  not parse.

`new` does carry a set of *fidelity* defects of its own (all in newly-emitted content, so none are
regressions): `distinct` is dropped from the whole error hierarchy, two rest parameters lose their
`...`, and three method defaults render as dangling identifiers. These are listed in §5.

## 2. Change inventory

Line counts (`wc -l`): old **2683**, new **3172** (+489 net; diff reports +601 / −112 across 65 hunks).

Top-level declaration sets, extracted from body only (lines > 394, i.e. after `// --- END README ---`):
old **171**, new **222**.

| | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 49 | 0 |
| `ballerina/ai:1.13.0:` qualified refs (lines / occurrences) | 39 / 88 | 0 / 0 |
| `@display` annotation lines | 3 | 56 |
| `// --- section ---` markers | 6 | 7 |
| Top-level declarations (body) | 171 | 222 |
| JSON `typeDefs` / `clients` / `functions` / `services` / `annotations` | 265/3/15/1/**0** | 265/3/15/1/**3** |
| Bytes | 99,657 | 121,490 |

**Removed in `new`: 0.** `comm -23` on the sorted declaration sets returns only
`class EmbeddingProvider` and `class ModelProvider` — both re-appear in `new` as
`client class EmbeddingProvider` / `client class ModelProvider`, which is correct (both are `client`
object types in the source). No symbol is lost.

**Added in `new`: 51 top-level declarations**, grouped by kind:

- **Error type aliases (27)** — `Error`, `LlmError`, `LlmInvalidGenerationError`, `LlmInvalidResponseError`,
  `LlmConnectionError`, `ToolExecutionError`, `ToolInvalidInputError`, `ToolInvalidOutputError`,
  `ToolNotFoundError`, `MemoryError`, `UnauthorizedError`, `OpenApiParsingError`,
  `ParsingStackOverflowError`, `UnsupportedSerializationError`, `UnsupportedOpenApiVersion`,
  `InvalidReferenceError`, `IncompleteSpecificationError`, `UnsupportedMediaTypeError`,
  `InvalidParameterDefinition`, `TaskCompletedError`, `HttpServiceToolKitError`,
  `HttpResponseParsingError`, `TokenAcquisitionError`, `TokenValidationError`,
  `MissingHttpParameterError`, `InsufficientScopeError`, `MaxIterationExceededError`,
  `ApprovalRequiredError`, `ApprovalNotFoundError`, `UnknownApprovalIdError` (30 names total; 27 were
  `// Unknown type:` in `old`, 3 were absent).
- **Classes (17)** — `Agent`, `Context`, `ToolStore`, `ShortTermMemory`, `GenericRecursiveChunker`,
  `MarkdownChunker`, `HtmlChunker`, `TextDataLoader`, `Listener`, `MessageWindowChatMemory`,
  `VectorRetriever`, `VectorKnowledgeBase`, `InMemoryShortTermMemoryStore`, `McpToolKit`,
  `HttpServiceToolKit`, `InMemoryVectorStore`, plus the two `client class` upgrades.
- **Non-error type aliases (3)** — `FunctionTool`, `Url`, `Vector`.
- **Annotations (2 declarations / 3 JSON entries)** — `annotation map<json> JsonSchema on type;` and
  `annotation ToolAnnotationConfig AgentTool on function, object function;`.

**Modified (member level).** 11 previously-empty classes gained their methods:
`ModelProvider` (2), `EmbeddingProvider` (2), `BaseToolKit` (1), `McpBaseToolKit` (1), `Memory` (3),
`DependentlyTypedAgent` (1), `FixedTypedAgent` (2), `Chunker` (1), `DataLoader` (1), `Retriever` (1),
`KnowledgeBase` (3), `ShortTermMemoryStore` (13), `VectorStore` (3), `ChatService` (1).
Records gained `@display` labels (`SystemPrompt`, `Credential`, `AgentConfiguration`, `ToolConfig`,
`AgentIdAuthConfig`, `ToolAnnotationConfig`, `ConnectionConfig`, `GeneratorConfig`, `RetryConfig`).

**README.** `diff <(head -394 old) <(head -394 new)` → identical. No README content lost.

## 3. Correctness against library source

Everything spot-checked below is verified against the `v1.13.0` clone and cross-checked against the
bala (`modules/ai/*.bal`); the two agree throughout — no bala/GitHub divergence was found.

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `type Vector float[];` | `ballerina/rag-types.bal:18` `public type Vector float[];` | correct |
| `type Url string;` + `@constraint:String {pattern:{value: urlRegExpr, ...}}` | `ballerina/document-types.bal:92-99` | correct (see §5.7) |
| `type ApprovalRequiredError error<record {\|ApprovalRequest[] requests;\|}>;` | `ballerina/error.bal:101` `distinct (Error & error<record {\| ApprovalRequest[] requests; \|}>)` | shape correct, `distinct (Error & …)` dropped |
| `type MaxIterationExceededError error<record {\|(ExecutionResult\|ExecutionError\|Error)[] steps;\|}>;` | `ballerina/error.bal:93` | shape correct, `distinct (Error & …)` dropped |
| `resource function post chat(@http:Payload ChatReqMessage request) returns ChatRespMessage\|error;` (in `class ChatService`) | `ballerina/types.bal:41-44` | exact match |
| `class HttpServiceToolKit { function init(string serviceUrl, HttpTool[] httpTools, http:ClientConfiguration clientConfig = {}, map<string\|string[]> headers = {}) returns Error?; …}` | `ballerina/toolkit.bal:205-220` | exact match |
| `class InMemoryVectorStore { function init(SimilarityMetric similarityMetric = COSINE) returns Error?; …}` | `ballerina/vector-store.bal:44-52` | exact match |
| `class Listener { function init(int\|http:Listener listenOn = 8090) returns error?; attach/detach/'start/gracefulStop/immediateStop }` | `ballerina/listener.bal:20-50` | exact match |
| `@deprecated class MessageWindowChatMemory` | `ballerina/memory.bal:48-49` `@deprecated public isolated class MessageWindowChatMemory` | correct, deprecation preserved |
| `class Agent { function init(… @display {label: "Agent Configuration"} AgentConfiguration config) returns Error?; …}` | `ballerina/agent.bal:241` `public isolated function init(@display {label: "Agent Configuration"} *AgentConfiguration config)` | included-record param expanded (renderer convention, same as `old` did for `Wso2*`) |
| `@display` labels on `SystemPrompt` / `Credential` / `AgentConfiguration` fields | `ballerina/agent.bal:30-100` | every label matches verbatim |
| `public annotation map<json> JsonSchema on type;` | `ballerina/to_json_schema.bal:31` | exact match |
| `public annotation ToolAnnotationConfig AgentTool on function, object function;` | `ballerina/tool_types.bal:178` | exact match |
| `string 'type;` in `Chunk`/`Document` | `ballerina/document-types.bal:87` `readonly "text-chunk" 'type` — the field name is the quoted keyword | `new` correct, `old` (`string type;`) invalid |
| `json 'const;` in `InternalValueSchema` | `ballerina/tool_types.bal:37` `json 'const;` | `new` correct, `old` invalid |
| `XmlSchema 'xml?;` (13 sites) | `ballerina/openapi_types.bal:145,350,…` `XmlSchema 'xml?;` | `new` correct, `old` invalid |
| `client class ModelProvider` / `client class EmbeddingProvider` | `ballerina/model-provider.bal`, `ballerina/embedding-provider.bal` | correct upgrade from bare `class` |

## 4. Regressions

**None found.**

Method used: normalised both bodies (`awk 'NR>394'`), stripped `@display` lines, and rewrote
`ballerina/ai:1.13.0:` → `` on the `old` side, then `diff`ed. The complete set of surviving
`old`-only lines is:

```
    string type;                    (2×)   -> fixed to 'type
    XmlSchema xml?;                 (13×)  -> fixed to 'xml
    json const;                     (1×)   -> fixed to 'const
class ModelProvider {                      -> client class ModelProvider {
class EmbeddingProvider {                  -> client class EmbeddingProvider {
}                               (2×)       -> brace moved, bodies now populated
    function init(string serviceUrl, string accessToken, decimal temperature = 0.7, …)   -> same line + @display labels
    remote function generate(Prompt prompt, anydata td = anydata) …                      -> same line + @display label
    remote function chat(ChatReqMessage request) returns ChatRespMessage|error;          -> ai:-qualified in Service block
```

Every one of these is a fix, a formatting change, or an addition — none is a loss. Declaration-set
`comm` confirms 0 removed symbols. README byte-identical. No parameter, default, return type or doc
comment present in `old` is absent from `new`.

The one arguably-neutral change is in the `// --- Service ---` template:
`remote function chat(ChatReqMessage request)` → `remote function chat(ai:ChatReqMessage request)
returns ai:ChatRespMessage|error;`. Since that block is a copy-paste template for user code
(`service ai:ChatService on new ai:Listener(...)`), the `ai:` qualification is more correct in `new`
and internally consistent with the already-qualified `ai:ChatService` / `ai:Listener`. Counted as an
improvement, not a regression.

## 5. Issues in `new` (independent of `old`)

All nine below live in content that `new` emits and `old` did not, so none is a regression — but each
would mislead an LLM consuming the render.

1. **Rest parameter lost, with wrong parenthesization — `ToolStore.init`.**
   `new:2746` renders `function init(BaseToolKit|ToolConfig|FunctionTool[] tools) returns Error?;`
   Source `ballerina/tool.bal:64` is `public isolated function init((BaseToolKit|ToolConfig|FunctionTool)... tools)`.
   Two errors: the rest marker `...` is dropped, and `A|B|C[]` parses as `A|B|(C[])`, not `(A|B|C)[]`.
2. **Rest parameter lost — `TextDataLoader.init`.** `new:2817` renders `function init(string paths)`;
   source `ballerina/data-loaders.bal:37` is `public isolated function init(string... paths)`.
   The render says the loader takes one path; it takes any number.
3. **Malformed default on `Agent.run`.** `new:2739`:
   `function run(… Trace|anydata td = ai:Trace|anydata) returns td|Error;`
   Source `ballerina/agent.bal:401-404`: `typedesc<Trace|anydata> td = <>`. The `typedesc<>` wrapper is
   dropped and the *type* is printed as the default value — `td = ai:Trace|anydata` is not valid
   Ballerina. Also `string sessionId = ""` where the source default is `DEFAULT_SESSION_ID` = `"sessionId"`.
4. **Dangling identifier defaults — `string sessionId = sessionId` (3 occurrences).**
   `new:1049` (`DependentlyTypedAgent.run`) and the two `FixedTypedAgent` methods. The renderer
   substituted the *value* of the private const `DEFAULT_SESSION_ID` (`constants.bal:27` =
   `"sessionId"`) without quoting it, producing a self-referential undefined symbol.
5. **Entire error hierarchy flattened.** `error.bal` declares 30 `distinct` error types
   (`grep -c "^public type .* distinct" error.bal` → 30), e.g. `public type Error distinct error;`,
   `public type LlmError distinct Error;`. `new` renders all of them as bare `type X error;`
   (`new:792,795,798,801,804,…`). Consequence: the render tells the model that `LlmError`,
   `MemoryError`, `ToolExecutionError` … are all just `error`, with no subtyping relationship to
   `Error` and no `distinct`ness. `grep -c distinct` on the new render → 1 (a README occurrence only).
6. **`isolated` dropped from `FunctionTool`.** `new:963` `type FunctionTool function;`; source
   `ballerina/tool_types.bal:181` is `public type FunctionTool isolated function;`. A non-isolated
   function value will not bind.
7. **`Url` annotation references an unexported symbol.** `new:1255-1256` emits
   `@constraint:String { pattern: { value: urlRegExpr, … } }`. `urlRegExpr` is a module-private
   `final string:RegExp` (`document-types.bal:20`) and is not declared anywhere in the render — the
   emitted snippet cannot compile in user code.
8. **`ai:` qualification leaks into the Types section.** `new:693`
   (`Context.getWithType(… ai:Cloneable[] | map<ai:Cloneable> … targetType = ai:ContextEntry)`) and
   `new:1049` (`ai:Trace|anydata td = <>`), while the surrounding 220 declarations use bare names.
   Source `ballerina/context.bal:108` is `typedesc<ContextEntry> targetType = <>` — the `typedesc<>`
   wrapper is again expanded into the raw union, and the default is printed as a type name.
9. **`distinct object` / `distinct service object` type aliases rendered as `class`.**
   `DependentlyTypedAgent` and `FixedTypedAgent` (`agent.bal:160,181`) are
   `public type X distinct isolated object {…}`; `ChatService` (`types.bal:41`) is
   `distinct service object`. All three render as `class`. `isolated` appears 23 times in the render
   but never on these. `old` had the same shape (empty `class` stubs), so this is not new — but `new`
   now fills the bodies, which makes the mislabelling more consequential.

Note that #3/#4/#8 (`td = <type>`, unquoted const defaults, `typedesc<>` expansion) follow a pattern
already present in `old` for `Wso2ModelProvider.generate` (`anydata td = anydata`), so this is a
long-standing renderer behaviour rather than a spec-v2 introduction.

## 6. Coverage gaps vs. the library

**Default module (`modules/ai`): 0 gaps in `new`.**

Extracted all `public` top-level declarations from the bala's default module —
221 unique symbols — and checked each against the new render: every one is present. (Two initial
apparent misses, `AUTO` and `DISABLE`, are present at `new:569` and `new:573` as
`const string AUTO = "AUTO";` / `const string DISABLE = "DISABLE";`; they were false negatives of a
`const <name>` grep against the renderer's `const string <name>` form.)

For contrast, `old` was missing 49 of the same 221 (the `// Unknown type:` set).

**Shared gap (both sides): submodules.** The bala ships three modules —
`ai`, `ai.intelligence`, `ai.observe`. Only the default module is extracted (per the pipeline's
`pkg.getDefaultModule()`), so neither render contains **52** public symbols from `ai.intelligence`
(`Client`, `ChatCompletion*`, `Embedding*`, `ConnectionConfig`, …) nor **39** from `ai.observe`.
This is a pipeline-wide limitation, identical on both sides, not a spec-v2 regression.

**Fidelity gaps affecting both sides** (pre-existing renderer conventions, listed for completeness,
not counted as new issues):
- Closed records `record {| … |}` are all rendered as open `record { … }` (e.g. `SystemPrompt`,
  `Credential`, `AgentConfiguration`, `Chunk` — all closed in source).
- Required fields with defaults (`tools = []`, `maxIter = INFER_TOOL_COUNT`, `verbose = false`,
  `toolLoadingStrategy = NO_FILTER`, `executeToolCallsInParallel = true` in `AgentConfiguration`)
  render as optional (`tools?`, `maxIter?`, …) with the default value discarded.
- `(BaseToolKit|ToolConfig|FunctionTool)[] tools` renders unparenthesised as
  `BaseToolKit|ToolConfig|FunctionTool[]`.
- `public` is absent from all but 2 body declarations (the two annotations), so the render does not
  distinguish exported from module-private symbols.
- The `// --- Service ---` block renders the resource method as `remote function chat(...)`; the
  source (`types.bal:43`) declares `resource function post chat(...)`. `new`'s Types section gets this
  right; the Service template does not.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` in the bala declares
`io.ballerina.stdlib.ai.plugin.AiCompilerPlugin`, with `ai-compiler-plugin-1.13.0.jar` and
`ballerina-to-openapi-2.3.2.jar`.

What it contributes (from `compiler-plugin/src/main/java/io/ballerina/stdlib/ai/plugin/`):

- **Code modification** — `AiCodeModifier`, `AiSourceModifier`, `JsonSchemaModificationTask`,
  `TypeMapperImplInitializer`: the plugin *generates* the `@ai:JsonSchema` payload for tool functions
  at compile time. This is why `JsonSchema` exists as an annotation on `type` and why user code never
  writes it by hand.
- **Analysis / validation** — `AiCodeAnalyzer`, `ToolAnnotationAnalysisTask`, `CustomAgentAnalysisTask`,
  `ModuleLevelAgentAnalysisTask`, `InitFunctionAnalysisTask`, `ListenerVisitor`. 11 diagnostics
  (`diagnostics/CompilationDiagnostic.java:34-44`): `AI_101` unable to generate schema for function,
  `AI_102` parameter not a subtype of `anydata`, `AI_103` xml parameter not supported by tool,
  `AI_104` invalid return type in tool, `AI_105` agent must be `final`, `AI_106` `Context` param must
  be first, `AI_107`/`AI_108` (warnings) unable to obtain valid server port, `AI_109` invalid auth
  config, `AI_110` invalid agent-id auth config, `AI_111` invalid approval predicate signature.
- **OpenAPI generation** — `OpenAPIGenerator`, `ChatServiceOpenAPISchema`, `ServersMapper`,
  `XmlTypeInspector`: emits an OpenAPI spec for `ai:ChatService` implementations.

Plugin-implied constraints **not** surfaced by either render, which an LLM would need in order to
generate compiling code:

- `AI_105`: an `Agent` variable must be declared `final`. The render's `class Agent` gives no hint.
- `AI_106`: if a tool function takes a `Context`, it must be the **first** parameter.
- `AI_102`/`AI_104`: `@ai:AgentTool` function parameters must be `anydata` subtypes and returns are
  restricted. The render shows only `annotation ToolAnnotationConfig AgentTool on function, object function;`.
- `AI_111`: the `requiresApproval` function-value predicate has a fixed signature; the render types it
  only as `RequiresApproval`.

This is a shared gap — `old` surfaced none of it either, and `new` at least now emits the `AgentTool`
and `JsonSchema` annotation declarations, which `old` omitted entirely.

## 8. Other considerations

- **Version.** Both renders were produced from the same bala at `1.13.0`; no version drift. The one
  version-bearing artefact in the text — the `ballerina/ai:1.13.0:` qualifier — is gone in `new`,
  which removes 88 tokens of noise and makes the render version-agnostic.
- **Deprecation.** `MessageWindowChatMemory` is `@deprecated` in source (`memory.bal:48`). `new`
  carries the `@deprecated` marker; `old` did not render the class at all. Improvement.
- **Size / token cost.** +21,833 bytes (+21.9%), +489 lines (+18.2%). The added bytes are almost
  entirely real API surface (49 previously-missing symbols and ~35 method bodies), offset slightly by
  the 88 removed version qualifiers. Good value per token.
- **Doc quality.** Doc comments carried across faithfully, including multi-line ones. Two source typos
  are reproduced verbatim (`"Stackoverflow errors due to lenthy OpenAPI specification"`,
  `"Errors occurred due to missing mandotary path or query parameters"`) — upstream defects, not
  renderer defects. No encoding damage: the em-dash and `—` in `AgentConfiguration.maxIter`'s doc
  survive intact in both renders.
- **Non-compiling render.** Neither render is copy-paste compilable as a module (no `public`, open
  records, `$ref` escaping, expanded included-record params). `new` reduces the number of hard syntax
  errors (`string type`, `json const`, `XmlSchema xml` are all reserved-word violations in `old`) but
  introduces a few of its own (§5.1–5.4, §5.7).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 2683 / 3172 |
| `git ls-remote --tags …module-ballerina-ai \| grep v1.13` | `v1.13.0` → `bed37a0`, peeled `20e4313` |
| `git log -1 --oneline` in clone; `git describe --tags` | `20e4313 [Gradle Release Plugin] - pre tag commit: 'v1.13.0'`; `v1.13.0` |
| `ls <bala>/java21/modules` | `ai`, `ai.intelligence`, `ai.observe` |
| `grep -c '^// Unknown type:'` old / new | 49 / 0 |
| `grep -c 'ballerina/ai:1.13.0:'` old / new (lines) | 39 / 0 |
| `grep -o 'ballerina/ai:1.13.0:' old \| wc -l` | 88 |
| `grep -c '@display'` old / new | 3 / 56 |
| `grep -n '^// --- ' old / new` | 6 markers / 7 markers (`Annotations` added at new:3167) |
| `diff <(head -394 old) <(head -394 new)` | no output → README identical |
| Top-level decl extraction + `comm` | old 171, new 222; 0 removed, 51 added |
| Normalised body diff (strip `@display`, strip version qualifier) — `old`-only lines | 21 lines, all keyword fixes / `client class` upgrades / brace moves / `@display`-added lines |
| 221 bala default-module `public` symbols × `grep` in new render | all present (0 gaps) |
| same × `grep` in old render | 49 missing |
| `new:569`, `new:573` | `const string AUTO = "AUTO";`, `const string DISABLE = "DISABLE";` |
| `ai.intelligence` / `ai.observe` public symbol counts | 52 / 39 — in neither render |
| `error.bal` `grep -c '^public type .* distinct'` | 30 |
| `grep -c distinct` new render | 1 (README only) |
| `error.bal:18,45,93,101` | `Error distinct error`, `LlmError distinct Error`, `MaxIterationExceededError distinct (Error & error<record{\|…\|}>)`, `ApprovalRequiredError distinct (Error & error<record{\|…\|}>)` |
| `new:792,795,1378,855` | `type Error error;`, `type LlmError error;`, `type MaxIterationExceededError error<record{\|…\|}>;`, `type ApprovalRequiredError error<record{\|…\|}>;` |
| `tool_types.bal:181` vs `new:963` | `isolated function` vs `function` |
| `document-types.bal:20,92-99` vs `new:1255-1256` | `urlRegExpr` is module-private `final string:RegExp`; render emits it as a bare reference |
| `rag-types.bal:18` vs `new:2221` | `public type Vector float[];` — match |
| `types.bal:41-44` vs new `class ChatService` | `resource function post chat(@http:Payload ChatReqMessage request) returns ChatRespMessage\|error;` — exact match |
| `toolkit.bal:205-220` vs new `class HttpServiceToolKit` | exact match |
| `vector-store.bal:44-52` vs new `class InMemoryVectorStore` | exact match |
| `listener.bal:20-50` vs new `class Listener` | exact match (all 6 methods) |
| `memory.bal:48-49` vs new | `@deprecated` preserved on `MessageWindowChatMemory` |
| `data-loaders.bal:37` vs `new:2817` | `init(string... paths)` vs `init(string paths)` — rest lost |
| `tool.bal:64` vs `new:2746` | `init((BaseToolKit\|ToolConfig\|FunctionTool)... tools)` vs `init(BaseToolKit\|ToolConfig\|FunctionTool[] tools)` |
| `agent.bal:401-404` vs `new:2739` | `typedesc<Trace\|anydata> td = <>`, `sessionId = DEFAULT_SESSION_ID` vs `Trace\|anydata td = ai:Trace\|anydata`, `sessionId = ""` |
| `constants.bal:27` | `const DEFAULT_SESSION_ID = "sessionId";` |
| `grep -c "sessionId = sessionId" new` | 3 |
| `context.bal:108` vs `new:693` | `typedesc<ContextEntry> targetType = <>` vs expanded union + `= ai:ContextEntry` |
| `document-types.bal:87`, `tool_types.bal:37`, `openapi_types.bal:145,350` | `'type`, `'const`, `'xml` — confirms `new`'s quoting, invalidates `old`'s |
| `agent.bal:30-100` vs new `SystemPrompt`/`Credential`/`AgentConfiguration` | all 12 `@display` labels match verbatim |
| `to_json_schema.bal:31`, `tool_types.bal:178` vs `new:3169,3172` | both annotation declarations match exactly |
| JSON element counts (python `json.load`) | old & new both: typeDefs 265, clients 3, functions 15, services 1; annotations 0 → 3 |
| `compiler-plugin/compiler-plugin.json` (bala) | `AiCompilerPlugin`; deps `ai-compiler-plugin-1.13.0.jar`, `ballerina-to-openapi-2.3.2.jar` |
| `diagnostics/CompilationDiagnostic.java:34-44` | 11 diagnostics `AI_101`–`AI_111` (9 ERROR, 2 WARNING) |
| `find compiler-plugin -name '*.java'` | 21 classes incl. `OpenAPIGenerator`, `AiSourceModifier`, `JsonSchemaModificationTask`, `CustomAgentAnalysisTask` |

## 10. Caveats and unverified items

- **Method-level exhaustiveness.** Every one of the 222 top-level declarations was diffed
  set-wise, and ~35 newly-emitted methods were compared against source; the 13 methods of
  `ShortTermMemoryStore` and the 13 of `InMemoryShortTermMemoryStore` were reviewed only against the
  diff text (name, params, return type read out of `short_term_memory_store.bal` headers), not
  line-by-line against source. No discrepancy was seen, but this is spot-check confidence, not proof.
- **Submodule symbol counts (52 / 39)** were derived by grepping `^public …` in the bala's
  `ai.intelligence` / `ai.observe` `.bal` files. They are an accurate count of the source's top-level
  `public` declarations but do not distinguish re-exports; treat as an order-of-magnitude figure for
  the shared submodule gap.
- **Ballerina Central metadata** (`api.central.ballerina.io`) was **not** re-queried in this review;
  the bala and the `v1.13.0` tag were used as the authorities and they agree. Deprecation status of
  the *package* (as opposed to `MessageWindowChatMemory`) is therefore unverified.
- **Renderer intent for `distinct` / `isolated` / `typedesc<>`.** It is unverified whether spec v2
  deliberately elides these or whether they are lost in the Java extractor before the renderer sees
  them. The JSON `typeDefs` count being identical (265) on both sides suggests the extractor output is
  unchanged and the elision is in `toSyntaxString`, but the JSON field-level content was not diffed to
  confirm.
- **No compilation of either render was attempted.** Claims that `string type;` / `json const;` are
  invalid rest on Ballerina's reserved-word rules and on the source using the quoted forms, not on a
  compiler run.

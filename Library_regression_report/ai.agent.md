# ballerinax/ai.agent 0.9.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.agent` |
| Pinned version | `0.9.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.agent |
| Tag reviewed | `v0.9.2` (commit `559c86f`, "[Gradle Release Plugin] - pre tag commit: 'v0.9.2'") |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.agent/0.9.2/java21` |
| Old render | `2128` lines |
| New render | `2315` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Nothing that `old` rendered was dropped,
truncated, or made less accurate. `new` eliminates all 31 `// Unknown type:` stubs, all 36
version-qualified type references, 3 mangled return types, and 13 keyword-collision identifiers, and
adds 33 method signatures, 50 `@display` annotations, 9 `@jsondata:Name` annotations and the module's
single public annotation (`Tool`). Every declaration name present in `old` (115 extracted) is present
in `new` (146 extracted); the set difference in the removal direction is empty.

Coverage of the default module is now complete: all 140 `public` top-level symbols declared in
`modules/ai.agent/*.bal` appear in the `new` render. The submodule `ai.agent.mistral` (97 public
symbols) is absent from both renders — a shared `getDefaultModule()` gap, not a regression.

Residual inaccuracies in `new` are real but all are either inherited from `old` (unquoted string
defaults, lost parentheses around union-array types) or are the price of newly rendering types that
`old` did not render at all (loss of `distinct` and the error subtype hierarchy).

## 2. Change inventory

Line counts (`wc -l`): old `2128`, new `2315` (+187). JSON payloads: old `303,111` bytes, new
`327,032` bytes (+7.9%).

Top-level declaration kinds (`grep -oE '^(public |isolated |distinct |client |readonly |final )*(type|class|enum|const|annotation|function|listener|service)[[:space:]]'`):

| kind | old | new | delta |
|---|---|---|---|
| `type` | 78 | 102 | +24 |
| `class` (incl. `client class`) | 17 | 24 | +7 |
| `const` | 89 | 89 | 0 |
| `enum` | 10 | 10 | 0 |
| `function` (module-level) | 9 | 9 | 0 |
| `annotation` | 0 | 1 | +1 |
| **distinct names extracted** | **115** | **146** | **+31** |

Removed from `new`: **none**. `comm -23 d_old.txt d_new.txt` is empty.

Added in `new` (31 names, exactly the 31 `// Unknown type:` stubs in `old`):

- **24 error types**: `Error`, `LlmError`, `LlmInvalidGenerationError`, `LlmInvalidResponseError`,
  `LlmConnectionError`, `ToolExecutionError`, `ToolInvalidOutputError`, `ToolNotFoundError`,
  `ToolInvalidInputError`, `MissingHttpParameterError`, `MemoryError`, `OpenApiParsingError`,
  `ParsingStackOverflowError`, `UnsupportedSerializationError`, `UnsupportedOpenApiVersion`,
  `InvalidReferenceError`, `IncompleteSpecificationError`, `UnsupportedMediaTypeError`,
  `InvalidParameterDefinition`, `TaskCompletedError`, `HttpServiceToolKitError`,
  `HttpResponseParsingError`, `MaxIterationExceededError` — plus the function-type alias `FunctionTool`.
- **7 classes**: `ToolStore`, `Iterator`, `Executor`, `Listener`, `MessageWindowChatMemory`,
  `DefaultMessageWindowChatMemoryManager`, `HttpServiceToolKit`.
- **1 annotation**: `public annotation ToolAnnotationConfig Tool on function, object function;`
  (new `// --- Annotations ---` section, new:2312-2315; no such section exists in `old`).

Modified in place:

| change | count | evidence |
|---|---|---|
| `// Unknown type: X` stub → real definition | 31 | `grep -c '^// Unknown type:'`: old 31, new 0 |
| version-qualified type refs `ballerinax/ai.agent:0.9.2:T` → bare `T` | 36 | `grep -c 'ballerinax/ai.agent:0.9.2:'`: old 36, new 0 |
| mangled return type `returns ExecutionError)[] steps; string answer?;\|};` → `returns record {\|(ExecutionResult\|ExecutionError)[] steps; string answer?;\|};` | 3 | `grep -c 'returns ExecutionError)\[\]'`: old 3, new 0 |
| `XmlSchema xml?` → `XmlSchema 'xml?` | 13 | old 13 unquoted + 2 already quoted; new 0 unquoted, 15 quoted |
| `string type;` → `string 'type;`, `json const;` → `json 'const;` | 2 | diff hunks @@ -1330 and @@ -1890 |
| `class BaseAgent`/`class Model` → `client class …` (+ bodies) | 2 | diff hunk @@ -763 |
| `remote function` → `function` on `parseLlmResponse` / `selectNextTool` in `FunctionCallAgent` and `ReActAgent` | 4 | diff hunks @@ -2000, @@ -2061 |
| method signatures inside class bodies | 24 → 57 (+33) | `grep -cE '^    (remote \|resource \|isolated )*function '` |
| `@display {…}` occurrences | 0 → 50 | `grep -c '@display'` |
| `@jsondata:Name {…}` occurrences | 0 → 9 | `grep -c '@jsondata:Name'` |

README block (lines 1–509) is byte-identical between the two renders (`diff` of `sed -n '1,509p'`
returns empty). Const and enum sections are unchanged.

## 3. Correctness against library source

Every construct `new` adds was checked against the bala (authoritative) and cross-checked in the
`v0.9.2` clone.

| rendered in `new` | source | verdict |
|---|---|---|
| `public annotation ToolAnnotationConfig Tool on function, object function;` | `modules/ai.agent/tool_types.bal:161` — identical text | exact match |
| `client class BaseAgent` with `parseLlmResponse`, `selectNextTool`, `remote function run(... maxIter = 5 ... verbose = true ...)` | `agent-utils.bal:76-96` — `public type BaseAgent distinct isolated client object`; `run` is `isolated remote function`, others `public isolated function` | signatures, defaults and remote-ness all match |
| `client class Model { remote function chat(ChatMessage[] messages, ChatCompletionFunctions[] tools = [], string\|() stop = ()) returns ChatAssistantMessage[]\|LlmError; }` | `model.bal:310-317` | match |
| `class MemoryManager { function getMemory(string memoryId) returns Memory\|MemoryError; }` | `memory.bal:2-9` | match |
| `class Memory { get() / update(ChatMessage) / delete() }` | `memory.bal:12-26` | match (`MemoryError?` rendered as `MemoryError\|()`, equivalent) |
| `class BaseToolKit { function getTools() returns ToolConfig[]; }` | `toolkit.bal:117-121` | match |
| `class ChatService { resource function post chat(@http:Payload ChatReqMessage request) returns ChatRespMessage\|error; }` | `types.bal:41-44` | match |
| `class Listener { init(int\|http:Listener listenOn = 8090); attach; detach; 'start; gracefulStop; immediateStop }` | `listener.bal:20-47` | all six methods and the default `8090` match |
| `class HttpServiceToolKit { init(string serviceUrl, HttpTool[] httpTools, http:ClientConfiguration clientConfig = {}, map<string\|string[]> headers = {}) returns Error?; getTools() }` | `toolkit.bal:125-140` | match |
| `class MessageWindowChatMemory { init(int size = 10); get; update; delete }` | `memory.bal:28+` | match |
| `class DefaultMessageWindowChatMemoryManager { init(int size = 10); getMemory }` | `memory.bal` | match |
| `class Executor { init(BaseAgent, string memoryId, …); hasNext; reason; act; update; next }` | `agent-utils.bal:123-…` | all six members match |
| `class Iterator { init(BaseAgent, string memoryId, …); iterator() returns object {public function next() …} }` | `agent-utils.bal:99-120` | match |
| `type MaxIterationExceededError error<record {\|(ExecutionResult\|ExecutionError)[] steps;\|}>;` | `error.bal:80-81` — `distinct (Error & error<record{\|(ExecutionResult\|ExecutionError)[] steps;\|}>)` | payload correct; `distinct`/intersection lost (see §5) |
| 9 × `@jsondata:Name {value: "…"}` on `OllamaModelParameters` | `ollama-model.bal:34,40,45,52,59,75,82,89,95` — same 9 names (`mirostat_eta`, `mirostat_tau`, `num_ctx`, `repeat_last_n`, `repeat_penalty`, `num_predict`, `top_k`, `top_p`, `min_p`) | exact 1:1 |
| `@display {label: "Agent Configuration"}` on `Agent.init` param; `@display {label: "Query"}` / `{label: "Memory ID"}` on `Agent.run` params | `agent.bal:82,95` — identical labels | exact |
| `XmlSchema 'xml?`, `string 'type`, `json 'const` | `openapi_types.bal:145,154` etc. use `'xml`, `'type` | `new` matches source, `old` did not |
| `function parseLlmResponse` / `selectNextTool` (non-remote) on `FunctionCallAgent`/`ReActAgent` | `function-call-agent.bal:46,78`; `react-agent.bal:53,62` — all `public isolated function`, not remote | `new` correct; `old`'s `remote function` was wrong |

## 4. Regressions

**None found.**

Checks performed to reach that conclusion:

1. Set difference of extracted top-level declaration names, old minus new: empty
   (`comm -23 d_old.txt d_new.txt`).
2. All removed lines in `diff -u old new` classified: 92 `-` lines total = 31 `// Unknown type:`
   stubs + 61 lines each of which has a `+` counterpart in the same hunk (13 `XmlSchema xml?`,
   36 version-qualified refs, 3 mangled `run` returns, 4 `remote`→plain method lines, 2 class
   headers, `string type;`, `json const;`, and 2 `init` lines that only lost the version qualifier).
   `grep -cE '^-#' full.diff` = **0** → no doc-comment line was removed.
3. README/prose block identical (lines 1–509, byte-for-byte).
4. Const (89) and enum (10) counts identical; no enum member lost (diff shows only `@display`
   insertions above enum headers).
5. Module-level function count identical (9); the three functions whose text changed
   (`run`, `extractToolsFromOpenApiSpecFile`, `extractToolsFromOpenApiJsonSpec`) became *more*
   accurate, not less.
6. The one signature change that could look like a downgrade — `remote function
   parseLlmResponse`/`selectNextTool` becoming plain `function` — was verified against
   `function-call-agent.bal:46,78` and `react-agent.bal:53,62`: the source declares them
   `public isolated function`. `old` was wrong; `new` is right.

## 5. Issues in `new` (independent of `old`)

Nine distinct inaccuracies remain in `new`. Items 1–4 are newly visible because `new` renders types
`old` skipped; items 5–9 are shared with `old`.

1. **`distinct` and the whole error hierarchy are flattened.** All 24 error types render as
   `type X error;`. Source (`error.bal:18-83`) declares them `public type Error distinct error;`,
   `public type LlmError distinct Error;`, `public type ToolNotFoundError distinct
   LlmInvalidGenerationError;` etc. An LLM reading `new` cannot tell that `LlmError` is a subtype of
   `Error`, so it cannot reason about `is`/`check` narrowing. Material, but strictly better than the
   bare names `old` emitted.
2. **`MaxIterationExceededError` loses the `Error &` intersection** — rendered as
   `error<record {|…steps;|}>` instead of `distinct (Error & error<…>)` (`error.bal:80-81`).
3. **`type FunctionTool function;` drops `isolated`** — source `tool_types.bal:164` is
   `public type FunctionTool isolated function;`. Tool functions must be isolated; the render does
   not say so.
4. **Public object fields are not rendered.** `BaseAgent` has `public Model model; public ToolStore
   toolStore; public MemoryManager memoryManager;` (`agent-utils.bal:77-79`), `ToolStore` has
   `public final map<AgentTool> & readonly tools;` (`tool.bal:41`), `Executor` has
   `public ExecutionProgress progress;` (`agent-utils.bal:128`), `FunctionCallAgent` has three public
   finals (`function-call-agent.bal:24-28`). None appear in either render; `new` shows only methods.
5. **Parentheses lost around union-array types.** Source `(BaseToolKit|ToolConfig|FunctionTool)[]
   tools` (`function-call-agent.bal:35`) renders as `BaseToolKit|ToolConfig|FunctionTool[] tools`,
   which in Ballerina parses as `BaseToolKit | ToolConfig | (FunctionTool[])` — a different type.
   Same defect on `ToolStore.init`, where source is additionally a **rest parameter**
   `(BaseToolKit|ToolConfig|FunctionTool)... tools` (`tool.bal:48`) rendered as a single array param,
   so the call form `new ToolStore(t1, t2)` is not derivable. Present in `old` too.
6. **String defaults are emitted unquoted**, producing non-compiling Ballerina: 4 occurrences of
   `= https://…` / `= http://localhost:11434` in both renders, and `string memoryId = memoryId`
   (the value of `const DEFAULT_MEMORY_ID = "memoryId"`, `constants.bal:40`) — 1 occurrence in `old`,
   3 in `new` simply because `new` renders two more methods that take that default.
7. **`DEFAULT_MEMORY_ID` defaults are inconsistent**: `Agent.run`, `FunctionCallAgent.selectNextTool`
   and `ReActAgent.run` show `string memoryId = ""` although source uses `DEFAULT_MEMORY_ID`
   (`"memoryId"`). Shared with `old`.
8. **Included-record parameters are double-rendered.** `Agent.init` source is
   `init(@display {…} *AgentConfiguration config)` (`agent.bal:82`) but both renders emit the seven
   flattened `AgentConfiguration` fields *and* a trailing `AgentConfiguration config` param, plus an
   invented default `Model model = object {}`. Same pattern on `Iterator.init` / `Executor.init`
   (`*ExecutionProgress progress`). Shared with `old`, but it now affects more declarations in `new`.
9. **`@display` coverage is partial**: source carries 75 `@display` occurrences
   (`agent.bal` 14, `model.bal` 44, `ollama-model.bal` 17); `new` renders 50. The missing 25 are
   class-level / private-field labels. Not wrong, just incomplete (`old` had 0).

## 6. Coverage gaps vs. the library

**Default module (`modules/ai.agent`) — 0 gaps.** 140 distinct `public` top-level symbols were
extracted from the bala's 21 `.bal` files; `comm -23 src_pub.txt d_new.txt` is empty, i.e. every one
of them appears in the `new` render. For `old`, the same comparison yields **31 missing** — exactly
the `// Unknown type:` set.

**Submodule — shared gap.** The bala ships a second module, `modules/ai.agent.mistral`
(`client.bal`, `types.bal`, `utils.bal`) with **97** public top-level symbols. It appears in neither
render, consistent with the pipeline's `pkg.getDefaultModule()`-only extraction. Not a `new`
regression.

Field-level gap (both sides): public object *fields* are never emitted — see §5 item 4.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.lib.ai.plugin.AiCompilerPlugin` with
two jars (`ai.agent-compiler-plugin-0.9.2.jar`, `ballerina-to-openapi-2.3.0.jar`). Upstream sources
at `v0.9.2` show:

- **`AiCodeModifier` / `AiSourceModifier` / `SchemaUtils` / `XmlTypeInspector`** — a source modifier
  that derives the JSON parameter schema for every function annotated `@agent:Tool` and injects it
  into the `ToolAnnotationConfig`. This is why `Tool` needs no explicit `parameters` field at the
  call site. Neither render explains this; the render only shows the annotation's shape.
- **`OpenAPIGenerator`** — generates an OpenAPI contract for `ChatService`, pulled in via the
  bundled `ballerina-to-openapi` jar. Not surfaced.
- **Five compile-time diagnostics** (`CompilationDiagnostic.java`): `AI_101` schema generation
  failure, `AI_102` parameter not a subtype of `anydata`, `AI_103` `xml` parameter unsupported in a
  tool, `AI_104` invalid tool return type, `AI_105` **"Agent must be marked as 'final'"**
  (`InitFunctionAnalysisTask` / `ModuleLevelAgentAnalysisTask`).

`AI_105` and `AI_102` are the two an LLM would most often violate: `new` renders
`client class Agent` with no indication that a module-level `Agent` variable must be declared
`final`, and renders `type FunctionTool function;` with no `anydata`-subtype constraint on tool
parameters. Both renders are equally silent, so this is a shared documentation gap rather than a
regression — but it is the single most useful thing missing from the render.

## 8. Other considerations

- **Pre-1.0 / unstable.** `0.9.2` is pre-release. Upstream has since shipped through `v1.2.3`
  (`git ls-remote --tags`), and the API changed substantially after 1.0 (the `ai.agent` package was
  largely superseded by `ballerina/ai`). The render is accurate for the pinned version only.
- **Stale README.** The README block (identical in both renders, lines 232–242) instructs users to
  extend `agent:BaseAgent` with `public final agent:ChatLlmModel model;`. `ChatLlmModel` does not
  exist in the 0.9.2 API — `grep -rn 'ChatLlmModel'` over the bala matches only a doc comment in
  `react-agent.bal:31`. An LLM following the README verbatim will emit a non-existent type. This is a
  library-side defect, unchanged by the render work.
- **Non-compiling render.** Neither render is copy-pasteable Ballerina (unquoted URL defaults,
  `Model model = object {}`, empty class bodies where fields belong). `new` narrows the gap
  considerably — it removes 36 illegal `org/name:version:Type` refs and 3 truncated return types that
  would break any parser — but does not close it.
- **Size/tokens.** +187 lines (+8.8%), +23.9 KB JSON (+7.9%) for +31 type definitions, +33 method
  signatures and +59 annotations. Good density; the added content is all high-value API surface.
- **Ballerina distribution field** is absent from the bala's `package.json` (`ballerinaVersion` is
  `None`); not needed for this review.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l` on both renders | old 2128, new 2315 |
| 2 | `git ls-remote --tags …module-ballerinax-ai.agent` | `refs/tags/v0.9.2` → `e2cf078` / `^{}` `559c86f` |
| 3 | `git clone --depth 1 --branch v0.9.2`; `git log --oneline -1`; `git describe --tags` | `559c86f "[Gradle Release Plugin] - pre tag commit: 'v0.9.2'"`; `v0.9.2` |
| 4 | `ls -R` bala | modules `ai.agent` (21 `.bal`) + `ai.agent.mistral` (3 `.bal`); `compiler-plugin/`, `docs/README.md`, `platform/java21/ai.agent-native-0.9.2.jar` |
| 5 | `python3 … package.json` | `ballerinax ai.agent 0.9.2` — version pin confirmed on the artifact the pipeline consumed |
| 6 | `grep -n '^// --- '` both | old: README/END README/Types/Client/Functions; new: same + `// --- Annotations ---` at 2312 |
| 7 | `grep -c '^// Unknown type:'` | old 31, new 0 |
| 8 | `grep -n '^// Unknown type:'` old | 31 names listed (lines 742–1978) |
| 9 | declaration-name extraction + `comm` | old 115, new 146; old−new = ∅; new−old = 31 names |
| 10 | kind histogram | type 78→102, class 17→24, const 89→89, enum 10→10, function 9→9, annotation 0→1 |
| 11 | `diff -u old new` | 931 lines, 55 hunks, 92 `-` / 251 `+` |
| 12 | `grep -cE '^-#' full.diff` | 0 — no doc line removed |
| 13 | `diff` of lines 1–509 | identical (README preserved) |
| 14 | `grep -c 'ballerinax/ai.agent:0.9.2:'` | old 36, new 0 |
| 15 | `grep -c 'returns ExecutionError)\[\]'` | old 3, new 0 |
| 16 | `grep -c "XmlSchema xml?"` / `"XmlSchema 'xml?"` | old 13/2, new 0/15 |
| 17 | `grep -cE '^    (remote \|resource \|isolated )*function '` | old 24, new 57 |
| 18 | `grep -c '@display'` / `'@jsondata:Name'` | old 0/0, new 50/9 |
| 19 | `grep -rc '@display' bala/modules/ai.agent/*.bal` | agent.bal 14, model.bal 44, ollama-model.bal 17 = 75 |
| 20 | `grep -n 'jsondata:Name' ollama-model.bal` | 9 hits at lines 34,40,45,52,59,75,82,89,95 — 1:1 with render |
| 21 | `agent-utils.bal:76-96` | `BaseAgent distinct isolated client object`; `parseLlmResponse`/`selectNextTool` = `public isolated function`; `run` = `isolated remote function` |
| 22 | `function-call-agent.bal:46,78`; `react-agent.bal:53,62` | `public isolated function` — confirms `old`'s `remote` was wrong |
| 23 | `error.bal:18-83` | 24 error types, all `distinct`; hierarchy Error→LlmError→LlmInvalidGenerationError→ToolNotFoundError/ToolInvalidInputError→MissingHttpParameterError etc. |
| 24 | `tool_types.bal:161,164` | annotation `Tool` text matches render exactly; `FunctionTool` is `isolated function` |
| 25 | `memory.bal:2-26` | `MemoryManager.getMemory`, `Memory.get/update/delete` — match render |
| 26 | `types.bal:41-44` | `ChatService` `resource function post chat(@http:Payload ChatReqMessage) returns ChatRespMessage\|error` — match |
| 27 | `model.bal:310-317` | `Model` `isolated remote function chat(...)` — match |
| 28 | `listener.bal:20-47` | 6 methods, `listenOn = 8090` — match |
| 29 | `toolkit.bal:117-140` | `BaseToolKit.getTools`, `HttpServiceToolKit.init/getTools` — match |
| 30 | `tool.bal:40-48` | `ToolStore` has `public final map<AgentTool> & readonly tools` (not rendered) and rest-param `init` (rendered as array) |
| 31 | `agent.bal:73-103` | `Agent` is `isolated distinct client class`; `*AgentConfiguration config`; `@display` labels match render |
| 32 | public-symbol extraction from bala default module + `comm` | 140 public symbols; new−missing = 0; old−missing = 31 |
| 33 | public-symbol count for `modules/ai.agent.mistral` | 97 — in neither render |
| 34 | `cat compiler-plugin/compiler-plugin.json` | `AiCompilerPlugin` + 2 jars |
| 35 | `CompilationDiagnostic.java:33-37`, `DiagnosticMessage.java:25-34` | AI_101…AI_105, incl. "Agent must be marked as 'final'" |
| 36 | `grep -rn 'ChatLlmModel' bala/modules/ai.agent/` | only a doc comment at `react-agent.bal:31` — README reference is stale |
| 37 | `grep -c '= https\?://'` | 4 in both renders (unquoted string defaults, shared) |
| 38 | `grep -c 'memoryId = memoryId'` | old 1, new 3 |
| 39 | `wc -c` on both JSONs | old 303,111; new 327,032 |

## 10. Caveats and unverified items

- The renders were not compiled or parsed with a Ballerina toolchain; syntax judgements in §5/§8 are
  from reading the emitted text against the language rules, not from a parser run.
- I did not diff the two `ballerina-vscode` sources; the attribution of each change to "spec v2"
  rests on the brief plus the observed shape of the changes, not on reading the extractor code.
- The `@display` shortfall (50 rendered vs 75 in source) was measured by raw `grep` counts on both
  sides, not by pairing each annotation to its declaration; the characterisation of the missing 25
  as class-level/private labels is from spot inspection of `model.bal` and `agent.bal`, not an
  exhaustive mapping.
- Compiler-plugin behaviour is read from the `v0.9.2` Java sources; I did not run the plugin, so the
  claim that `@agent:Tool` schemas are injected at compile time is source-derived, not executed.
- `ai.agent.mistral`'s 97 public symbols were counted by regex over the bala's 3 `.bal` files; the
  number could differ slightly from a semantic API listing (e.g. re-exports).
- The scratch clone directory already contained `src` from a prior run of this session's tooling; I
  verified it is checked out at `v0.9.2` (`git describe --tags`) with a detached HEAD and clean tree
  before using it.

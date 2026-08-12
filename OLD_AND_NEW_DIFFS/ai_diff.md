# ai — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai` |
| **Old file** | `ai/old/ballerina_ai.bal.txt` |
| **New file** | `ai/new/ballerina_ai.bal.txt` |
| **Old lines** | 2683 |
| **New lines** | 3172 |
| **Lines added** | 601 |
| **Lines removed** | 112 |
| **Hunks** | 65 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 49 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 88 | 0 |
| `// --- section ---` markers | 6 | 7 |

### Declarations added (93)

- `annotation AgentTool`
- `class Agent`
- `class Context`
- `class GenericRecursiveChunker`
- `class HtmlChunker`
- `class HttpServiceToolKit`
- `class InMemoryShortTermMemoryStore`
- `class InMemoryVectorStore`
- `class Listener`
- `class MarkdownChunker`
- `class McpToolKit`
- `class MessageWindowChatMemory`
- `class ShortTermMemory`
- `class TextDataLoader`
- `class ToolStore`
- `class VectorKnowledgeBase`
- `class VectorRetriever`
- `client class EmbeddingProvider`
- `client class ModelProvider`
- `function 'start`
- `function add`
- `function attach`
- `function batchEmbed`
- `function callTool`
- `function chunk`
- `function delete`
- `function deleteByFilter`
- `function detach`
- `function embed`
- `function execute`
- `function get`
- `function getAccessToken`
- `function getAll`
- `function getCapacity`
- `function getChatInteractiveMessages`
- `function getChatSystemMessage`
- `function getCheckpoint`
- `function getTools`
- `function getWithType`
- `function gracefulStop`
- `function hasKey`
- `function immediateStop`
- `function ingest`
- `function isFull`
- `function keys`
- `function load`
- `function put`
- `function putCheckpoint`
- `function query`
- `function remove`
- `function removeAll`
- `function removeChatInteractiveMessages`
- `function removeChatSystemMessage`
- `function removeCheckpoint`
- `function retrieve`
- `function run`
- `function set`
- `function takeCheckpoint`
- `function trace`
- `function update`
- `type ApprovalNotFoundError`
- `type ApprovalRequiredError`
- `type Error`
- `type FunctionTool`
- `type HttpResponseParsingError`
- `type HttpServiceToolKitError`
- `type IncompleteSpecificationError`
- `type InsufficientScopeError`
- `type InvalidParameterDefinition`
- `type InvalidReferenceError`
- `type LlmConnectionError`
- `type LlmError`
- `type LlmInvalidGenerationError`
- `type LlmInvalidResponseError`
- `type MaxIterationExceededError`
- `type MemoryError`
- `type MissingHttpParameterError`
- `type OpenApiParsingError`
- `type ParsingStackOverflowError`
- `type TaskCompletedError`
- `type TokenAcquisitionError`
- `type TokenValidationError`
- `type ToolExecutionError`
- `type ToolInvalidInputError`
- `type ToolInvalidOutputError`
- `type ToolNotFoundError`
- `type UnauthorizedError`
- `type UnknownApprovalIdError`
- `type UnsupportedMediaTypeError`
- `type UnsupportedOpenApiVersion`
- `type UnsupportedSerializationError`
- `type Url`
- `type Vector`

### Declarations removed (2)

- `class EmbeddingProvider`
- `class ModelProvider`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 640–646 | 640–646 | Types | +1 | −1 |
| 2 | 665–677 | 665–707 | Types | +33 | −3 |
| 3 | 726–732 | 756–762 | Types | +1 | −1 |
| 4 | 758–774 | 788–810 | Types | +12 | −6 |
| 5 | 813–875 | 849–941 | Types | +32 | −2 |
| 6 | 884–916 | 950–992 | Types | +11 | −1 |
| 7 | 940–945 | 1016–1032 | Types | +11 | −0 |
| 8 | 952–968 | 1039–1071 | Types | +17 | −1 |
| 9 | 1023–1029 | 1126–1132 | Types | +1 | −1 |
| 10 | 1073–1078 | 1176–1184 | Types | +3 | −0 |
| 11 | 1120–1125 | 1226–1234 | Types | +3 | −0 |
| 12 | 1142–1148 | 1251–1259 | Types | +3 | −1 |
| 13 | 1192–1246 | 1303–1389 | Types | +58 | −26 |
| 14 | 1293–1299 | 1436–1442 | Types | +1 | −1 |
| 15 | 1372–1378 | 1515–1521 | Types | +1 | −1 |
| 16 | 1383–1389 | 1526–1532 | Types | +1 | −1 |
| 17 | 1391–1397 | 1534–1540 | Types | +1 | −1 |
| 18 | 1421–1427 | 1564–1570 | Types | +1 | −1 |
| 19 | 1451–1457 | 1594–1600 | Types | +1 | −1 |
| 20 | 1469–1475 | 1612–1618 | Types | +1 | −1 |
| 21 | 1479–1485 | 1622–1628 | Types | +1 | −1 |
| 22 | 1500–1511 | 1643–1654 | Types | +2 | −2 |
| 23 | 1529–1535 | 1672–1678 | Types | +1 | −1 |
| 24 | 1545–1551 | 1688–1694 | Types | +1 | −1 |
| 25 | 1559–1565 | 1702–1708 | Types | +1 | −1 |
| 26 | 1569–1575 | 1712–1718 | Types | +1 | −1 |
| 27 | 1583–1594 | 1726–1737 | Types | +2 | −2 |
| 28 | 1600–1606 | 1743–1749 | Types | +1 | −1 |
| 29 | 1612–1618 | 1755–1761 | Types | +1 | −1 |
| 30 | 1626–1632 | 1769–1775 | Types | +1 | −1 |
| 31 | 1638–1644 | 1781–1787 | Types | +1 | −1 |
| 32 | 1656–1662 | 1799–1805 | Types | +1 | −1 |
| 33 | 1673–1681 | 1816–1824 | Types | +2 | −2 |
| 34 | 1696–1702 | 1839–1845 | Types | +1 | −1 |
| 35 | 1707–1713 | 1850–1856 | Types | +1 | −1 |
| 36 | 1720–1726 | 1863–1869 | Types | +1 | −1 |
| 37 | 1743–1749 | 1886–1892 | Types | +1 | −1 |
| 38 | 1754–1760 | 1897–1903 | Types | +1 | −1 |
| 39 | 1806–1812 | 1949–1955 | Types | +1 | −1 |
| 40 | 1822–1838 | 1965–1981 | Types | +6 | −6 |
| 41 | 1885–1891 | 2028–2034 | Types | +1 | −1 |
| 42 | 1965–1971 | 2108–2114 | Types | +1 | −1 |
| 43 | 2026–2032 | 2169–2175 | Types | +1 | −1 |
| 44 | 2038–2044 | 2181–2187 | Types | +1 | −1 |
| 45 | 2053–2059 | 2196–2202 | Types | +1 | −1 |
| 46 | 2074–2080 | 2217–2224 | Types | +2 | −1 |
| 47 | 2095–2101 | 2239–2245 | Types | +1 | −1 |
| 48 | 2199–2208 | 2343–2368 | Types | +16 | −0 |
| 49 | 2222–2228 | 2382–2388 | Types | +1 | −1 |
| 50 | 2234–2239 | 2394–2457 | Types | +58 | −0 |
| 51 | 2244–2250 | 2462–2468 | Types | +1 | −1 |
| 52 | 2279–2285 | 2497–2503 | Types | +1 | −1 |
| 53 | 2294–2303 | 2512–2523 | Types | +2 | −0 |
| 54 | 2316–2321 | 2536–2544 | Types | +3 | −0 |
| 55 | 2362–2399 | 2585–2639 | Types | +17 | −0 |
| 56 | 2401–2406 | 2641–2647 | Types | +1 | −0 |
| 57 | 2408–2415 | 2649–2658 | Types | +2 | −0 |
| 58 | 2464–2501 | 2707–2983 | Types | +256 | −17 |
| 59 | 2509–2515 | 2991–2997 | Client | +1 | −1 |
| 60 | 2522–2528 | 3004–3010 | Client | +1 | −1 |
| 61 | 2531–2537 | 3013–3019 | Client | +1 | −1 |
| 62 | 2590–2596 | 3072–3078 | Functions | +1 | −1 |
| 63 | 2599–2605 | 3081–3087 | Functions | +1 | −1 |
| 64 | 2633–2639 | 3115–3121 | Functions | +1 | −1 |
| 65 | 2679–2683 | 3161–3172 | Service | +8 | −1 |

---

## Unified diff

`````diff
--- ai/old/ballerina_ai.bal.txt	2026-08-12 12:57:29
+++ ai/new/ballerina_ai.bal.txt	2026-08-12 13:19:19
@@ -640,7 +640,7 @@
 # Represents a chunk of a document.
 
 type Chunk record {
-    string type;
+    string 'type;
     Metadata metadata?;
     anydata content;
 };
@@ -665,13 +665,43 @@
     string id?;
 };
 
-// Unknown type: Context
+# Represents a contextual storage object used to pass additional data to tools during agent execution.
+class Context {
 
+    # Adds or updates an entry in the context.
+    # 
+    function set(string key, ContextEntry value) returns ();
+
+    # Retrieves a value from the context by key. Panics if the key does not exist.
+    # 
+    function get(string key) returns ContextEntry;
+
+    # Checks if the context contains an entry for the given key.
+    # 
+    function hasKey(string key) returns boolean;
+
+    # Returns all the keys currently stored in the context.
+    # 
+    function keys() returns string[];
+
+    # Retrieves the access token associated with the specified tool.
+    # 
+    function getAccessToken(string toolName) returns string|error;
+
+    # Retrieves and casts a value from the context to the specified type.
+    # 
+    function getWithType(string key, any & readonly|xml|ai:Cloneable[]|map<ai:Cloneable>|table<map<ai:Cloneable>>|isolated object {} targetType = ai:ContextEntry) returns targetType|Error;
+
+    # Removes the entry associated with the given key. Panics if the key does not exist.
+    # 
+    function remove(string key) returns ();
+}
+
 # Represents a non-error type that can be cloned.
-type Cloneable any & readonly|xml|ballerina/ai:1.13.0:Cloneable[]|map<ballerina/ai:1.13.0:Cloneable>|table<map<ballerina/ai:1.13.0:Cloneable>>;
+type Cloneable any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>;
 
 # Represents the type of a value stored in the `Context` object.
-type ContextEntry any & readonly|xml|ballerina/ai:1.13.0:Cloneable[]|map<ballerina/ai:1.13.0:Cloneable>|table<map<ballerina/ai:1.13.0:Cloneable>>|isolated object {};
+type ContextEntry any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>|isolated object {};
 
 # User chat message record.
 
@@ -726,7 +756,7 @@
 };
 
 # Chat message record.
-type ChatMessage ballerina/ai:1.13.0:ChatUserMessage|ballerina/ai:1.13.0:ChatSystemMessage|ballerina/ai:1.13.0:ChatAssistantMessage|ballerina/ai:1.13.0:ChatFunctionMessage;
+type ChatMessage ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage;
 
 # Execution step information
 
@@ -758,17 +788,23 @@
     string observation;
 };
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
-// Unknown type: LlmError
+# Any error occurred during LLM generation is classified under this error type.
+type LlmError error;
 
-// Unknown type: LlmInvalidGenerationError
+# Errors occurred due to invalid LLM generation.
+type LlmInvalidGenerationError error;
 
-// Unknown type: ToolExecutionError
+# Errors during tool execution.
+type ToolExecutionError error;
 
-// Unknown type: MemoryError
+# Represents errors that occur during memory-related operations.  
+type MemoryError error;
 
-// Unknown type: UnauthorizedError
+# Error returned when the request is unauthorized.
+type UnauthorizedError error;
 
 # Output from executing an action
 
@@ -813,63 +849,93 @@
     int batchIndex;
 };
 
-// Unknown type: ApprovalRequiredError
+# Raised when the agent pauses to request human approval for one or more sensitive tool calls
+# proposed in the same turn. Usually carries a single entry in `requests`; more than one when
+# the LLM proposed several gated calls together and none of them have a decision yet.
+type ApprovalRequiredError error<record {|ApprovalRequest[] requests;|}>;
 
 # Represents the system prompt given to the agent.
 
+@display {label: "System Prompt"}
 type SystemPrompt record {
     # The role or responsibility assigned to the agent
+    @display {label: "Role"}
     string role;
     # Specific instructions for the agent
+    @display {label: "Instructions"}
     string instructions;
 };
 
 # Represents the authentication credentials of an autonomous agent.
 
+@display {label: "Agent Credential"}
 type Credential record {
     # The unique identifier assigned to the agent.
+    @display {label: "Agent ID"}
     string id;
     # The secret associated with the agent.
+    @display {label: "Agent Secret"}
     string secret;
 };
 
 # Provides a set of configurations for the agent.
 
+@display {label: "Agent Configuration"}
 type AgentConfiguration record {
     # The system prompt assigned to the agent
+    @display {label: "System Prompt"}
     SystemPrompt systemPrompt;
     # The model used by the agent
+    @display {label: "Model"}
     ModelProvider model;
     # The tools available for the agent
+    @display {label: "Tools"}
     BaseToolKit|ToolConfig|FunctionTool[] tools?;
     # The maximum number of reasoning-action cycles the agent performs to complete the task.
 A single cycle is one LLM call plus the execution of every tool call returned in
 that response, so multiple tool calls from one response count as one iteration.
 Defaults to `max(number of tools, 10)` — i.e., at least 10, or more if the
 agent has more tools available.
+    @display {label: "Maximum Iterations"}
     "INFER_TOOL_COUNT"|int maxIter?;
     # Specifies whether verbose logging is enabled
+    @display {label: "Verbose"}
     boolean verbose?;
     # The memory used by the agent to store and manage conversation history.
 Defaults to use an in-memory message store that trims on overflow, if unspecified.
+    @display {label: "Memory"}
     Memory|() memory?;
     # Defines the strategies for loading tool schemas into an Agent.
 By default, all tools are loaded without any filtering.
+    @display {label: "Tool Loading Strategy"}
     ToolLoadingStrategy toolLoadingStrategy?;
     # Specifies whether multiple tool calls returned in a single LLM response are executed in parallel.
 If `true`, all tool calls from one LLM response are executed concurrently;
 otherwise, they are executed sequentially, one after another.
+    @display {label: "Execute Tool Calls in Parallel"}
     boolean executeToolCallsInParallel?;
     # Optional authentication details of the agent.
+    @display {label: "Agent Credential"}
     Credential credential?;
 };
 
 # Represents an extendable client for interacting with an AI model.
-class ModelProvider {
+client class ModelProvider {
+
+    # Sends a chat request to the model with the given messages and tools.
+    remote function chat(ChatMessage[]|ChatUserMessage messages, ChatCompletionFunctions[] tools = [], string|() stop = ()) returns ChatAssistantMessage|Error;
+
+    # Sends a chat request to the model and generates a value that belongs to the type
+    # corresponding to the type descriptor argument.
+    # 
+    remote function generate(Prompt prompt, @display {label: "Expected type"} anydata td = <>) returns td|Error;
 }
 
 # Allows implmenting custom toolkits by extending this type. Toolkits can help to define new types of tools so that agent can understand them.
 class BaseToolKit {
+
+    # Useful to retrieve the Tools extracted from the Toolkit.
+    function getTools() returns ToolConfig[];
 }
 
 # Defines a tool. This is the only tool type directly understood by the agent. All other tool types are converted to this type using toolkits.
@@ -884,33 +950,43 @@
     # Pointer to the function that should be called when the tool is invoked.
     FunctionTool caller;
     # Optional authorization configuration required to invoke this tool.
+    @display {label: "Authorization Configuration"}
     AgentIdAuthConfig|Scopes auth?;
     # When `true`, the agent pauses and requests human approval before invoking this tool.
 A function value gates only the calls it evaluates to `true` for, based on the proposed
 arguments.
+    @display {label: "Requires Approval"}
     RequiresApproval requiresApproval?;
 };
 
-// Unknown type: FunctionTool
+# Represents a type alias for an isolated function, representing a function tool.
+type FunctionTool function;
 
 # Represents the OAuth 2.0 client configuration required to interact
 # with an external Authorization Server and validate issued access tokens.
 
+@display {label: "OAuth Client Configuration"}
 type AgentIdAuthConfig record {
     # The base URL of the Authorization Server used to resolve
 OAuth 2.0 endpoints such as authorization, token, and introspection.
+    @display {label: "Authorization Server Base URL"}
     string baseAuthUrl;
     # The OAuth 2.0 client identifier issued to this client application.
+    @display {label: "Client ID"}
     string clientId;
     # The OAuth 2.0 client secret issued to this client application.
+    @display {label: "Client Secret"}
     string clientSecret?;
     # The redirect URI registered for the OAuth client and used
 in the Authorization Code flow.
+    @display {label: "Redirect URI"}
     string redirectUri;
     # Scopes required to invoke this tool
+    @display {label: "Required Scopes"}
     string|string[] scopes?;
     # Indicates whether PKCE (Proof Key for Code Exchange) is enabled
 for the Authorization Code flow.
+    @display {label: "Enable PKCE"}
     boolean isPkceEnabled?;
     # SSL/TLS-related options
     http:ClientSecureSocket|() secureSocket?; // Special Agent Note: ClientSecureSocket FROM ballerina/http package
@@ -940,6 +1016,17 @@
 
 # Represents the memory interface for the agents.
 class Memory {
+
+    # Retrieves all stored chat messages.
+    # 
+    function get(string sessionId) returns ChatMessage[]|MemoryError;
+
+    # Stores one or more chat messages in memory for the specified session.
+    # 
+    function update(string sessionId, ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage|ChatMessage[] message) returns MemoryError|();
+
+    # Deletes all stored messages.
+    function delete(string sessionId) returns MemoryError|();
 }
 
 # Defines the strategies for loading tool schemas into an Agent.
@@ -952,17 +1039,33 @@
 # Callers decide whether they want the full `Trace`, the raw `string` answer, or the answer bound 
 # to a structured `anydata` type.
 class DependentlyTypedAgent {
+
+    # Executes the agent for the given query and binds the result to the inferred return type.
+    # 
+    # Pass a `string`/`Prompt` to start a new turn, or a `Resume` (the human's decisions on a
+    # previously paused run) to continue a run that paused for human approval. The input type is
+    # what distinguishes the two - there is no separate resume operation.
+    # 
+    function run(@display {label: "Query"} string|Prompt|Resume query, @display {label: "Session ID"} string sessionId = sessionId, Context context = new, ai:Trace|anydata td = <>) returns td|Error;
 }
 
 # Represents a reusable agent definition with a fixed `anydata` return type. Implementations typically
 # compose an `Agent` and delegate to it, exposing a domain-specific return type from `run` while still
 # surfacing the full execution `Trace` via `trace`.
 class FixedTypedAgent {
+
+    # Executes the agent for the given query and returns the result bound to the implementation's fixed type.
+    # 
+    function run(@display {label: "Query"} string|Prompt query, @display {label: "Session ID"} string sessionId = sessionId, Context context = new) returns anydata|Error;
+
+    # Executes the agent for the given query and returns the full execution trace.
+    # 
+    function trace(@display {label: "Query"} string|Prompt query, @display {label: "Session ID"} string sessionId = sessionId, Context context = new) returns Trace|Error;
 }
 
 # Represents the supported agent type abstractions: an agent whose return type is inferred from the call
 # site, or one that fixes its return type to a specific `anydata` value.
-type AgentType ballerina/ai:1.13.0:DependentlyTypedAgent|ballerina/ai:1.13.0:FixedTypedAgent;
+type AgentType DependentlyTypedAgent|FixedTypedAgent;
 
 # Represents the kind of a tool entry available to an agent.
 enum ToolKind {
@@ -1023,7 +1126,7 @@
 
 type Resume record {
     # The human's decisions on the pending tool calls, keyed by `ApprovalRequest.id`
-    map<ballerina/ai:1.13.0:HumanResponse> decisions;
+    map<HumanResponse> decisions;
 };
 
 # The pending approval persisted across a pause, sufficient to resume the run
@@ -1073,6 +1176,9 @@
 
 # Represents a chunker that can process documents and return chunks.
 class Chunker {
+
+    # Chunks the provided document.
+    function chunk(Document document) returns Chunk[]|Error;
 }
 
 # Represents the available strategies for recursively chunking a document.
@@ -1120,6 +1226,9 @@
 
 # Represents a data loader that can load documents from various sources.
 class DataLoader {
+
+    # Loads documents from a source.
+    function load() returns Document[]|Document|Error;
 }
 
 # Represents documents containing plain text content
@@ -1142,7 +1251,9 @@
     Metadata metadata?;
 };
 
-// Unknown type: Url
+# Represents a URL.
+@constraint:String { pattern: { value: urlRegExpr, message: "Must be a valid URL" } }
+type Url string;
 
 # Represents an image document.
 
@@ -1192,55 +1303,87 @@
 };
 
 # Represents an embedding provider that converts chunk into vector embeddings for similarity search.
-class EmbeddingProvider {
-}
+client class EmbeddingProvider {
 
-// Unknown type: OpenApiParsingError
+    # Converts the given chunk into a vector embedding.
+    # 
+    remote function embed(Chunk chunk) returns Vector|SparseVector|HybridVector|Error;
 
-// Unknown type: ParsingStackOverflowError
+    # Converts a batch of chunks into vector embeddings.
+    # 
+    remote function batchEmbed(Chunk[] chunks) returns Embedding[]|Error;
+}
 
-// Unknown type: UnsupportedSerializationError
+# Any error occurred during parsing OpenAPI specification is classified under this error type.
+type OpenApiParsingError error;
 
-// Unknown type: UnsupportedOpenApiVersion
-
-// Unknown type: InvalidReferenceError
+# Stackoverflow errors due to lenthy OpenAPI specification or cyclic references in the specification.
+type ParsingStackOverflowError error;
 
-// Unknown type: IncompleteSpecificationError
+# Errors occurred due to unsupported path parameter serializations.
+type UnsupportedSerializationError error;
 
-// Unknown type: UnsupportedMediaTypeError
+# Errors due to unsupported OpenAPI specification version.
+type UnsupportedOpenApiVersion error;
 
-// Unknown type: InvalidParameterDefinition
+# Errors due to invalid or broken references in the OpenAPI specification.
+type InvalidReferenceError error;
 
-// Unknown type: LlmInvalidResponseError
+# Errors due to incomplete OpenAPI specification.
+type IncompleteSpecificationError error;
 
-// Unknown type: LlmConnectionError
+# Errors due to unsupported media type.
+type UnsupportedMediaTypeError error;
 
-// Unknown type: TaskCompletedError
+# Error through due to invalid parameter definition that does not include either schema or content.
+type InvalidParameterDefinition error;
 
-// Unknown type: HttpServiceToolKitError
+# Errors occurred due to unexpected responses from the LLM.
+type LlmInvalidResponseError error;
 
-// Unknown type: HttpResponseParsingError
+# Errors occurred during LLM generation due to connection.
+type LlmConnectionError error;
 
-// Unknown type: ToolInvalidOutputError
+# Errors occurred due to termination of the Agent's execution.
+type TaskCompletedError error;
 
-// Unknown type: TokenAcquisitionError
+# Errors occurred due while running HTTP service toolkit.
+type HttpServiceToolKitError error;
 
-// Unknown type: TokenValidationError
+# Any error occurred during parsing HTTP response is classified under this error type.
+type HttpResponseParsingError error;
+
+# Error during unexpected output by the tool
+type ToolInvalidOutputError error;
 
-// Unknown type: ToolNotFoundError
+# Represents an error that occurs when getting token for tool 
+type TokenAcquisitionError error;
 
-// Unknown type: ToolInvalidInputError
+# Represents an error that occurs when validating token for tool
+type TokenValidationError error;
 
-// Unknown type: MissingHttpParameterError
+# Errors occurred due to invalid tool name generated by the LLM.
+type ToolNotFoundError error;
 
-// Unknown type: InsufficientScopeError
+# Errors occurred due to invalid input to the tool generated by the LLM.
+type ToolInvalidInputError error;
 
-// Unknown type: MaxIterationExceededError
+# Errors occurred due to missing mandotary path or query parameters.
+type MissingHttpParameterError error;
 
-// Unknown type: ApprovalNotFoundError
+# Errors occurred when validating tool scope.
+type InsufficientScopeError error;
 
-// Unknown type: UnknownApprovalIdError
+# Represents an error that occurs when the maximum number of iterations has been exceeded.
+type MaxIterationExceededError error<record {|(ExecutionResult|ExecutionError|Error)[] steps;|}>;
+
+# Raised when `run` is given a `Resume` but no approval is pending for the session.
+type ApprovalNotFoundError error;
 
+# Raised when a `Resume` passed to `run` names an id that is not among the approvals currently
+# pending for the session (a stale id, a typo, or an id from a different session).
+type UnknownApprovalIdError error;
+
 # Represents the trace of an agent's execution.
 
 type Trace record {
@@ -1293,7 +1436,7 @@
 
 # Interactive chat messages.
 # This is the type `ChatMessage` excluding the type `ChatSystemMessage`.
-type ChatInteractiveMessage ballerina/ai:1.13.0:ChatUserMessage|ballerina/ai:1.13.0:ChatAssistantMessage|ballerina/ai:1.13.0:ChatFunctionMessage;
+type ChatInteractiveMessage ChatUserMessage|ChatAssistantMessage|ChatFunctionMessage;
 
 # Function definitions for function calling API.
 
@@ -1372,7 +1515,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1383,7 +1526,7 @@
     never properties?;
     # Can not have items in a primitive type schema
     never items?;
-    string type;
+    string 'type;
     never anyOf?;
     never oneOf?;
     never allOf?;
@@ -1391,7 +1534,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1421,7 +1564,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1451,7 +1594,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1469,7 +1612,7 @@
     # Regular expression pattern of the string value
     string pattern?;
     # Enum values of the string value
-    (ballerina/ai:1.13.0:PrimitiveType?)[] 'enum?;
+    (PrimitiveType?)[] 'enum?;
     never properties?;
     never items?;
     never anyOf?;
@@ -1479,7 +1622,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1500,12 +1643,12 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
 # Primitive type schema object.
-type PrimitiveTypeSchema ballerina/ai:1.13.0:IntegerSchema|ballerina/ai:1.13.0:NumberSchema|ballerina/ai:1.13.0:StringSchema|ballerina/ai:1.13.0:BooleanSchema;
+type PrimitiveTypeSchema IntegerSchema|NumberSchema|StringSchema|BooleanSchema;
 
 # Array schema object.
 
@@ -1529,7 +1672,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1545,7 +1688,7 @@
     # List of required properties
     boolean|string[] required?;
     # List of properties
-    map<ballerina/ai:1.13.0:Schema> properties?;
+    map<Schema> properties?;
     # Additional properties
     boolean|IntegerSchema|NumberSchema|StringSchema|BooleanSchema|ArraySchema|ObjectSchemaType1|ObjectSchemaType2|OneOfSchema|AllOfSchema|AnyOfSchema|NotSchema|Reference additionalProperties?;
     # Discriminator
@@ -1559,7 +1702,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1569,7 +1712,7 @@
     # To match when type is not specified, but properties are specified
     never 'type?;
     # List of properties
-    map<ballerina/ai:1.13.0:Schema> properties;
+    map<Schema> properties;
     int minProperties?;
     int maxProperties?;
     boolean|string[] required?;
@@ -1583,12 +1726,12 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
 # Defines an object schema.
-type ObjectSchema ballerina/ai:1.13.0:ObjectSchemaType1|ballerina/ai:1.13.0:ObjectSchemaType2;
+type ObjectSchema ObjectSchemaType1|ObjectSchemaType2;
 
 # One of schema object.
 
@@ -1600,7 +1743,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1612,7 +1755,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1626,7 +1769,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1638,7 +1781,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1656,7 +1799,7 @@
 };
 
 # Defines a OpenAPI schema.
-type Schema ballerina/ai:1.13.0:IntegerSchema|ballerina/ai:1.13.0:NumberSchema|ballerina/ai:1.13.0:StringSchema|ballerina/ai:1.13.0:BooleanSchema|ballerina/ai:1.13.0:ArraySchema|ballerina/ai:1.13.0:ObjectSchemaType1|ballerina/ai:1.13.0:ObjectSchemaType2|ballerina/ai:1.13.0:OneOfSchema|ballerina/ai:1.13.0:AllOfSchema|ballerina/ai:1.13.0:AnyOfSchema|ballerina/ai:1.13.0:NotSchema|ballerina/ai:1.13.0:Reference;
+type Schema IntegerSchema|NumberSchema|StringSchema|BooleanSchema|ArraySchema|ObjectSchemaType1|ObjectSchemaType2|OneOfSchema|AllOfSchema|AnyOfSchema|NotSchema|Reference;
 
 # Discriminator object.
 
@@ -1673,9 +1816,9 @@
     # A short description of the response
     string description?;
     # A map containing schema of the response headers
-    map<ballerina/ai:1.13.0:Header|ballerina/ai:1.13.0:Reference> headers?;
+    map<Header|Reference> headers?;
     # A map containing the structure of the response body
-    map<ballerina/ai:1.13.0:MediaType> content?;
+    map<MediaType> content?;
     # Not allowed $ref
     never \$ref?;
 };
@@ -1696,7 +1839,7 @@
     # Schema of the header parameter
     Schema schema?;
     # Content of the header parameter
-    map<ballerina/ai:1.13.0:MediaType> content?;
+    map<MediaType> content?;
     # Not allowed $ref
     never \$ref?;
 };
@@ -1707,7 +1850,7 @@
     # Schema of the content
     Schema schema?;
     # Encoding of the content
-    map<ballerina/ai:1.13.0:Encoding> encoding?;
+    map<Encoding> encoding?;
 };
 
 # Describes a encoding definition applied to a schema property.
@@ -1720,7 +1863,7 @@
     # The Content-Type for encoding a specific property
     string contentType?;
     # A map allowing additional information to be provided as headers
-    map<ballerina/ai:1.13.0:Header|ballerina/ai:1.13.0:Reference> headers?;
+    map<Header|Reference> headers?;
 };
 
 # Describes a single operation parameter.
@@ -1743,7 +1886,7 @@
     # Schema of the parameter
     Schema schema?;
     # Content of the parameter
-    map<ballerina/ai:1.13.0:MediaType> content?;
+    map<MediaType> content?;
     # Null value is allowed
     boolean nullable?;
 };
@@ -1754,7 +1897,7 @@
     # A brief description of the request body. This could contain examples of use.
     string description?;
     # The content of the request body. 
-    map<ballerina/ai:1.13.0:MediaType> content;
+    map<MediaType> content;
     # Whether the request body is mandatory in the request.
     boolean required?;
 };
@@ -1806,7 +1949,7 @@
     # The request body applicable for this operation
     RequestBody|Reference requestBody?;
     # The list of possible responses as they are returned from executing this operation
-    map<ballerina/ai:1.13.0:Response|ballerina/ai:1.13.0:Reference> responses?;
+    map<Response|Reference> responses?;
 };
 
 # Server information object.
@@ -1822,17 +1965,17 @@
 
 type Components record {
     # A map of reusable schemas for different data types
-    map<ballerina/ai:1.13.0:Schema|ballerina/ai:1.13.0:Reference> schemas?;
+    map<Schema|Reference> schemas?;
     # A map of reusable response objects 
-    map<ballerina/ai:1.13.0:Response|ballerina/ai:1.13.0:Reference> responses?;
+    map<Response|Reference> responses?;
     # A map of reusable parameter objects
-    map<ballerina/ai:1.13.0:Parameter|ballerina/ai:1.13.0:Reference> parameters?;
+    map<Parameter|Reference> parameters?;
     # A map of reusable request body objects
-    map<ballerina/ai:1.13.0:RequestBody|ballerina/ai:1.13.0:Reference> requestBodies?;
+    map<RequestBody|Reference> requestBodies?;
     # A map of reusable header objects
-    map<ballerina/ai:1.13.0:Header|ballerina/ai:1.13.0:Reference> headers?;
+    map<Header|Reference> headers?;
     # A map of PathItem objects
-    map<ballerina/ai:1.13.0:PathItem|ballerina/ai:1.13.0:Reference> pathItems?;
+    map<PathItem|Reference> pathItems?;
 };
 
 # Map of pathItem objects.
@@ -1885,7 +2028,7 @@
     # Path of the Http resource
     string path;
     # path and query parameters definitions of the Http resource
-    map<ballerina/ai:1.13.0:ParameterSchema> parameters?;
+    map<ParameterSchema> parameters?;
     # Request body definition of the Http resource
     RequestBodySchema requestBody?;
 };
@@ -1965,7 +2108,7 @@
     # List of required properties
     string[] required?;
     # Schema of the object properties
-    map<ballerina/ai:1.13.0:JsonSubSchema> properties?;
+    map<JsonSubSchema> properties?;
     string description?;
     json default?;
     boolean nullable?;
@@ -2026,7 +2169,7 @@
 };
 
 # Defines a json input schema
-type JsonInputSchema ballerina/ai:1.13.0:ObjectInputSchema|ballerina/ai:1.13.0:ArrayInputSchema|ballerina/ai:1.13.0:AnyOfInputSchema|ballerina/ai:1.13.0:OneOfInputSchema|ballerina/ai:1.13.0:AllOfInputSchema|ballerina/ai:1.13.0:NotInputSchema;
+type JsonInputSchema ObjectInputSchema|ArrayInputSchema|AnyOfInputSchema|OneOfInputSchema|AllOfInputSchema|NotInputSchema;
 
 # Defines a primitive input field in the schema.
 
@@ -2038,7 +2181,7 @@
     # Pattern of the input. This is only applicable for `STRING` type.
     string pattern?;
     # Enum values of the input. This is only applicable for `STRING` type.
-    (ballerina/ai:1.13.0:PrimitiveType?)[] 'enum?;
+    (PrimitiveType?)[] 'enum?;
     # Default value of the input
     PrimitiveType default?;
     string description?;
@@ -2053,7 +2196,7 @@
 };
 
 # Defines a json sub schema
-type JsonSubSchema ballerina/ai:1.13.0:ObjectInputSchema|ballerina/ai:1.13.0:ArrayInputSchema|ballerina/ai:1.13.0:AnyOfInputSchema|ballerina/ai:1.13.0:OneOfInputSchema|ballerina/ai:1.13.0:AllOfInputSchema|ballerina/ai:1.13.0:NotInputSchema|ballerina/ai:1.13.0:PrimitiveInputSchema|ballerina/ai:1.13.0:ConstantValueSchema;
+type JsonSubSchema ObjectInputSchema|ArrayInputSchema|AnyOfInputSchema|OneOfInputSchema|AllOfInputSchema|NotInputSchema|PrimitiveInputSchema|ConstantValueSchema;
 
 
 type RequestBodySchema record {
@@ -2074,7 +2217,8 @@
     boolean extractDefault?;
 };
 
-// Unknown type: Vector
+# Represents a dense vector with floating-point values.
+type Vector float[];
 
 # Represents a sparse vector storing only non-zero values with their corresponding indices.
 
@@ -2095,7 +2239,7 @@
 };
 
 # Represents possible vector types.
-type Embedding ballerina/ai:1.13.0:Vector|ballerina/ai:1.13.0:SparseVector|ballerina/ai:1.13.0:HybridVector;
+type Embedding Vector|SparseVector|HybridVector;
 
 # Represents the set of supported operators used for metadata filtering during vector search operations.
 enum MetadataFilterOperator {
@@ -2199,10 +2343,26 @@
 
 # Represents chunk retriever that finds relevant chunks based on query similarity.
 class Retriever {
+
+    # Retrieves relevant chunks for the given query.
+    # 
+    function retrieve(string query, int maxLimit, MetadataFilters|() filters = ()) returns QueryMatch[]|Error;
 }
 
 # Represents a knowledge base for managing chunk indexing and retrieval operations.
 class KnowledgeBase {
+
+    # Ingests a collection of chunks.
+    # 
+    function ingest(Chunk[]|Document[]|Document documents) returns Error|();
+
+    # Retrieves relevant chunks for the given query.
+    # 
+    function retrieve(string query, int maxLimit, MetadataFilters|() filters = ()) returns QueryMatch[]|Error;
+
+    # Deletes chunks that match the given metadata filters.
+    # 
+    function deleteByFilter(MetadataFilters filters) returns Error|();
 }
 
 # Represents configuration to trim messages when overflow occurs.
@@ -2222,7 +2382,7 @@
 };
 
 # Represents configuration for handling overflow in short-term memory.
-type OverflowHandlerConfiguration ballerina/ai:1.13.0:TrimOverflowHandlerConfiguration|ballerina/ai:1.13.0:ModelAssistedOverflowHandlerConfiguration;
+type OverflowHandlerConfiguration TrimOverflowHandlerConfiguration|ModelAssistedOverflowHandlerConfiguration;
 
 # Represents a short-term memory store that retains a fixed number of recent messages by a key,
 # and persists human-in-the-loop pause checkpoints keyed by session ID.
@@ -2234,6 +2394,64 @@
 # built-in `InMemoryShortTermMemoryStore` keeps both in memory (not durable across a restart or a
 # run on another replica).
 class ShortTermMemoryStore {
+
+    # Retrieves the system message, if it was provided, for a given key.
+    # 
+    function getChatSystemMessage(string key) returns ChatSystemMessage|MemoryError|();
+
+    # Retrieves all stored interactive chat messages (i.e., all chat messages except the system
+    # message) for a given key.
+    # 
+    function getChatInteractiveMessages(string key) returns ChatInteractiveMessage[]|MemoryError;
+
+    # Retrieves all stored chat messages for a given key.
+    # 
+    function getAll(string key) returns [ChatSystemMessage, ChatInteractiveMessage...]|ChatInteractiveMessage[]|MemoryError;
+
+    # Adds one or more chat messages to the memory store for a given key.
+    # 
+    function put(string key, ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage|ChatMessage[] message) returns MemoryError|();
+
+    # Removes the system chat message, if specified, for a given key.
+    # 
+    function removeChatSystemMessage(string key) returns MemoryError|();
+
+    # Removes all stored interactive chat messages (i.e., all chat messages except the system
+    # message) for a given key.
+    # 
+    function removeChatInteractiveMessages(string key, int|() count = ()) returns MemoryError|();
+
+    # Removes all stored chat messages for a given key.
+    # 
+    function removeAll(string key) returns MemoryError|();
+
+    # Checks if the memory store is full for a given key.
+    # 
+    function isFull(string key) returns boolean|MemoryError;
+
+    # Returns the capacity configured for each key in the store.
+    # 
+    function getCapacity() returns int;
+
+    # Stores (or replaces) the pending human-in-the-loop approval for its session. Named
+    # distinctly from the message operations so a single object (e.g. `ShortTermMemory`) can
+    # expose both concerns without collision.
+    # 
+    function putCheckpoint(PendingApproval approval) returns Error|();
+
+    # Returns the pending human-in-the-loop approval for a session, if any.
+    # 
+    function getCheckpoint(string sessionId) returns PendingApproval|()|Error;
+
+    # Removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
+
+    # Atomically fetches and removes the pending human-in-the-loop approval for a session, if
+    # any. Used to "claim" an approval before resolving it, so a concurrent duplicate resume
+    # call for the same session cannot also claim and execute the same approved tool call.
+    # 
+    function takeCheckpoint(string sessionId) returns PendingApproval|()|Error;
 }
 
 # Represents a conversation thread containing multiple agent interaction traces.
@@ -2244,7 +2462,7 @@
     # Human-readable description of the conversation thread
     string description;
     # Sequence of traces representing individual agent executions within this thread
-    ballerina/ai:1.13.0:Trace[] & readonly traces;
+    Trace[] & readonly traces;
 };
 
 # Represent the execution result of a tool.
@@ -2279,7 +2497,7 @@
 # Defines a internal value field in the schema
 
 type InternalValueSchema record {
-    json const;
+    json 'const;
 };
 
 # Defines the configuration of the Tool annotation.
@@ -2294,10 +2512,12 @@
 If not provided, the input schema is generated automatically. 
     ObjectInputSchema|() parameters?;
     # Optional authorization configuration required to invoke this tool.
+    @display {label: "Authorization Configuration"}
     AgentIdAuthConfig|Scopes auth?;
     # When `true`, the agent pauses and requests human approval before invoking this tool.
 A function value gates only the calls it evaluates to `true` for, based on the proposed
 arguments.
+    @display {label: "Requires Approval"}
     RequiresApproval requiresApproval?;
 };
 
@@ -2316,6 +2536,9 @@
 
 # Represents a base type for MCP toolkits.
 class McpBaseToolKit {
+
+    # Useful to retrieve the Tools extracted from the Toolkit.
+    function getTools() returns ToolConfig[];
 }
 
 # Represents a request message for the chat service.
@@ -2362,38 +2585,55 @@
 
 # Defines a chat service interface that handles incoming chat messages.
 class ChatService {
+
+    resource function post chat(@http:Payload ChatReqMessage request) returns ChatRespMessage|error;
 }
 
 # Configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Configuration"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
+    @display {label: "HTTP Version"}
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
     # Configurations related to HTTP/1.x protocol
+    @display {label: "HTTP1 Settings"}
     http:ClientHttp1Settings http1Settings?; // Special Agent Note: ClientHttp1Settings FROM ballerina/http package
     # Configurations related to HTTP/2 protocol
+    @display {label: "HTTP2 Settings"}
     http:ClientHttp2Settings http2Settings?; // Special Agent Note: ClientHttp2Settings FROM ballerina/http package
     # The maximum time to wait (in seconds) for a response before closing the connection
+    @display {label: "Timeout"}
     decimal timeout?;
     # The choice of setting `forwarded`/`x-forwarded` header
+    @display {label: "Forwarded"}
     string forwarded?;
     # Configurations associated with request pooling
+    @display {label: "Pool Configuration"}
     http:PoolConfiguration poolConfig?; // Special Agent Note: PoolConfiguration FROM ballerina/http package
     # HTTP caching related configurations
+    @display {label: "Cache Configuration"}
     http:CacheConfig cache?; // Special Agent Note: CacheConfig FROM ballerina/http package
     # Specifies the way of handling compression (`accept-encoding`) header
+    @display {label: "Compression"}
     http:Compression compression?; // Special Agent Note: Compression FROM ballerina/http package
     # Configurations associated with the behaviour of the Circuit Breaker
+    @display {label: "Circuit Breaker Configuration"}
     http:CircuitBreakerConfig circuitBreaker?; // Special Agent Note: CircuitBreakerConfig FROM ballerina/http package
     # Configurations associated with retrying
+    @display {label: "Retry Configuration"}
     http:RetryConfig retryConfig?; // Special Agent Note: RetryConfig FROM ballerina/http package
     # Configurations associated with inbound response size limits
+    @display {label: "Response Limit Configuration"}
     http:ResponseLimitConfigs responseLimits?; // Special Agent Note: ResponseLimitConfigs FROM ballerina/http package
     # SSL/TLS-related options
+    @display {label: "Secure Socket Configuration"}
     http:ClientSecureSocket secureSocket?; // Special Agent Note: ClientSecureSocket FROM ballerina/http package
     # Proxy server related options
+    @display {label: "Proxy Configuration"}
     http:ProxyConfig proxy?; // Special Agent Note: ProxyConfig FROM ballerina/http package
     # Enables the inbound payload validation functionality which provided by the constraint package. Enabled by default
+    @display {label: "Payload Validation"}
     boolean validation?;
 };
 
@@ -2401,6 +2641,7 @@
 
 type GeneratorConfig record {
     # Configuration for retrying on response parsing failures
+    @display {label: "Retry Configuration"}
     RetryConfig retryConfig?;
 };
 
@@ -2408,8 +2649,10 @@
 
 type RetryConfig record {
     # Number of retry attempts
+    @display {label: "Retry Count"}
     int count?;
     # Retry interval in seconds
+    @display {label: "Retry Interval"}
     decimal interval?;
 };
 
@@ -2464,38 +2707,277 @@
 
 # Represents a vector store that provides persistence, management, and search capabilities for vector embeddings.
 class VectorStore {
-}
 
-// Unknown type: Agent
-
-// Unknown type: ToolStore
+    # Adds vector entries to the store.
+    # 
+    function add(VectorEntry[] entries) returns Error|();
 
-// Unknown type: ShortTermMemory
+    # Searches for vectors in the store that are most similar to a given query.
+    # 
+    function query(VectorStoreQuery query) returns VectorMatch[]|Error;
 
-// Unknown type: GenericRecursiveChunker
+    # Deletes a vector entry from the store by its unique ID.
+    # 
+    function delete(string|string[] ids) returns Error|();
+}
 
-// Unknown type: MarkdownChunker
+# Initialize an Agent.
+# 
+class Agent {
+    function init(SystemPrompt systemPrompt = {role: "", instructions: ""}, ModelProvider model = object {}, BaseToolKit|ToolConfig|FunctionTool[] tools = [], "INFER_TOOL_COUNT"|int maxIter = INFER_TOOL_COUNT, boolean verbose = false, Memory|() memory = (), ToolLoadingStrategy toolLoadingStrategy = NO_FILTER, boolean executeToolCallsInParallel = true, Credential credential = {id: "", secret: ""}, @display {label: "Agent Configuration"} AgentConfiguration config) returns Error?;
 
-// Unknown type: HtmlChunker
+    # Executes the agent for a given query.
+    # 
+    # Pass a `string`/`Prompt` to start a new turn, or a `Resume` (the human's decisions on a
+    # previously paused run) to continue a run that paused for human approval on this session. The
+    # input type is what distinguishes a fresh turn from a resume - there is no separate resume
+    # operation. A `Resume` for a session with no pending approval fails with `ApprovalNotFoundError`.
+    # 
+    # **Note:** Calls to this function using the same session ID must be invoked sequentially by the caller,
+    # as this operation is not thread-safe.
+    # 
+    function run(@display {label: "Query"} string|Prompt|Resume query, @display {label: "Session ID"} string sessionId = "", Context context = new (), Trace|anydata td = ai:Trace|anydata) returns td|Error;
+}
 
-// Unknown type: TextDataLoader
+# Register tools to the agent. 
+# These tools will be by the LLM to perform tasks.
+# 
+class ToolStore {
+    function init(BaseToolKit|ToolConfig|FunctionTool[] tools) returns Error?;
 
-// Unknown type: Listener
+    # execute the tool decided by the LLM.
+    # 
+    function execute(LlmToolResponse action, Context context = new ()) returns ToolOutput|LlmInvalidGenerationError|ToolExecutionError;
+}
+
+# Initializes short-term memory with an optional store and overflow configuration.
+# 
+class ShortTermMemory {
+    function init(ShortTermMemoryStore|() store = (), OverflowHandlerConfiguration overflowConfiguration = <TrimOverflowHandlerConfiguration> {}) returns MemoryError?;
 
-// Unknown type: MessageWindowChatMemory
+    # Retrieves all stored chat messages.
+    # 
+    function get(string key) returns ChatMessage[]|MemoryError;
 
-// Unknown type: VectorRetriever
+    # Adds one or more chat messages to the memory, handling overflow as configured.
+    # 
+    function update(string key, ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage|ChatMessage[] message) returns MemoryError|();
 
-// Unknown type: VectorKnowledgeBase
+    # Deletes all messages stored against a key.
+    # 
+    function delete(string key) returns MemoryError|();
 
-// Unknown type: InMemoryShortTermMemoryStore
+    # Stores (or replaces) the pending approval for its session.
+    # 
+    function putCheckpoint(PendingApproval approval) returns Error|();
 
-// Unknown type: McpToolKit
+    # Returns the pending approval for a session, if any.
+    # 
+    function getCheckpoint(string sessionId) returns PendingApproval|()|Error;
 
-// Unknown type: HttpServiceToolKit
+    # Removes the pending approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
 
-// Unknown type: InMemoryVectorStore
+    # Atomically fetches and removes the pending approval for a session, if any.
+    # 
+    function takeCheckpoint(string sessionId) returns PendingApproval|()|Error;
+}
 
+# Initializes a new instance of the `GenericRecursiveChunker`.
+# 
+class GenericRecursiveChunker {
+    function init(int maxChunkSize = 200, int maxOverlapSize = 40, RecursiveChunkStrategy strategy = PARAGRAPH) returns ();
+
+    # Chunks the provided document.
+    function chunk(Document document) returns Chunk[]|Error;
+}
+
+# Initializes a new instance of the `MarkdownChunker`.
+# 
+class MarkdownChunker {
+    function init(int maxChunkSize = 200, int maxOverlapSize = 40, MarkdownChunkStrategy strategy = MARKDOWN_HEADER) returns ();
+
+    # Chunks the provided document.
+    function chunk(Document document) returns Chunk[]|Error;
+}
+
+# Initializes a new instance of the `HtmlChunker`.
+# 
+class HtmlChunker {
+    function init(int maxChunkSize = 200, int maxOverlapSize = 40, HtmlChunkStrategy strategy = HTML_HEADER) returns ();
+
+    # Chunks the provided document.
+    # 
+    function chunk(Document document) returns Chunk[]|Error;
+}
+
+# Initializes the data loader with the given paths.
+class TextDataLoader {
+    function init(string paths) returns Error?;
+
+    # Loads documents as `TextDocument`s from a source.
+    function load() returns Document[]|Document|Error;
+}
+
+class Listener {
+    function init(int|http:Listener listenOn = 8090) returns error?; // Special Agent Note: Listener FROM ballerina/http package
+
+    function attach(ChatService chatService, string[]|string|() name = ()) returns error?;
+
+    function detach(ChatService chatService) returns error?;
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+# Initializes a new memory window with a default or given size.
+@deprecated
+class MessageWindowChatMemory {
+    function init(int size = 10) returns ();
+
+    # Retrieves a copy of all stored messages, with an optional system prompt.
+    # 
+    function get(string sessionId) returns ChatMessage[]|MemoryError;
+
+    # Stores one or more chat messages in memory for the specified session.
+    # 
+    function update(string sessionId, ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage|ChatMessage[] message) returns MemoryError|();
+
+    # Removes all messages from the memory.
+    # 
+    function delete(string sessionId) returns MemoryError|();
+}
+
+# Initializes a new `Retriever` instance.
+# 
+class VectorRetriever {
+    function init(VectorStore vectorStore, EmbeddingProvider embeddingModel) returns ();
+
+    # Retrieves relevant chunks for the given query.
+    # 
+    function retrieve(string query, int topK = 0, MetadataFilters|() filters = ()) returns QueryMatch[]|Error;
+}
+
+# Initializes a new `VectorKnowledgeBase` instance.
+# 
+class VectorKnowledgeBase {
+    function init(VectorStore vectorStore, EmbeddingProvider embeddingModel, Chunker|"AUTO"|"DISABLE" chunker = AUTO) returns ();
+
+    # Indexes a collection of chunks.
+    # Converts each chunk to an embedding and stores it in the vector store,
+    # making the chunk searchable through the retriever.
+    # 
+    function ingest(Document|Document[]|Chunk[] documents) returns Error|();
+
+    # Retrieves relevant chunk for the given query.
+    # 
+    function retrieve(string query, int topK = 0, MetadataFilters|() filters = ()) returns QueryMatch[]|Error;
+
+    # Deletes chunks that match the given metadata filters.
+    # 
+    function deleteByFilter(MetadataFilters filters) returns Error|();
+}
+
+# Initializes a new in-memory store.
+# 
+class InMemoryShortTermMemoryStore {
+    function init(int size = 10) returns MemoryError?;
+
+    # Retrieves the system message, if it was provided, for a given key.
+    # 
+    function getChatSystemMessage(string key) returns ChatSystemMessage|();
+
+    # Retrieves a copy of all stored messages, with an optional system prompt.
+    # 
+    function getChatInteractiveMessages(string key) returns ChatInteractiveMessage[];
+
+    # Retrieves all stored chat messages for a given key.
+    # 
+    function getAll(string key) returns [ChatSystemMessage, ChatInteractiveMessage...]|ChatInteractiveMessage[]|MemoryError;
+
+    # Adds one or more chat messages to the memory store for a given key.
+    # 
+    function put(string key, ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage|ChatMessage[] message) returns MemoryError|();
+
+    # Removes the system chat message, if specified, for a given key.
+    # 
+    function removeChatSystemMessage(string key) returns ();
+
+    # Removes stored messages for a given key.
+    # 
+    function removeChatInteractiveMessages(string key, int|() count = ()) returns MemoryError|();
+
+    # Removes all stored chat messages for a given key.
+    # 
+    function removeAll(string key) returns MemoryError|();
+
+    # Checks if the memory store is full for a given key.
+    # 
+    function isFull(string key) returns boolean;
+
+    # Returns the capacity configured for each key in the `InMemoryShortTermMemoryStore`.
+    # 
+    function getCapacity() returns int;
+
+    # Stores (or replaces) the pending human-in-the-loop approval for its session.
+    # 
+    function putCheckpoint(PendingApproval approval) returns Error|();
+
+    # Returns the pending human-in-the-loop approval for a session, if any.
+    # 
+    function getCheckpoint(string sessionId) returns PendingApproval|()|Error;
+
+    # Removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
+
+    # Atomically fetches and removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function takeCheckpoint(string sessionId) returns PendingApproval|()|Error;
+}
+
+class McpToolKit {
+    function init(string serverUrl, string[]|() permittedTools = (), mcp:Implementation info = {name: "MCP Client", version: "1.0.0"}, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 30, string forwarded = "disable", http:FollowRedirects|() followRedirects = (), http:PoolConfiguration|() poolConfig = (), http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig|() circuitBreaker = (), http:RetryConfig|() retryConfig = (), http:CookieConfig|() cookieConfig = (), http:CredentialsConfig|http:BearerTokenConfig|http:JwtIssuerConfig|http:OAuth2ClientCredentialsGrantConfig|http:OAuth2PasswordGrantConfig|http:OAuth2RefreshTokenGrantConfig|http:OAuth2JwtBearerGrantConfig|AgentIdAuthConfig|() auth = (), http:ResponseLimitConfigs responseLimits = {}, http:ProxyConfig|() proxy = (), boolean validation = true, http:ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, http:ClientSecureSocket|() secureSocket = (), string sessionId = "", StreamableHttpClientTransportConfig config) returns Error?; // Special Agent Note: Implementation FROM ballerina/mcp package, HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, CookieConfig, CredentialsConfig, BearerTokenConfig, JwtIssuerConfig, OAuth2ClientCredentialsGrantConfig, OAuth2PasswordGrantConfig, OAuth2RefreshTokenGrantConfig, OAuth2JwtBearerGrantConfig, ResponseLimitConfigs, ProxyConfig, ClientSocketConfig, ClientSecureSocket FROM ballerina/http package
+
+    function callTool(mcp:CallToolParams params) returns mcp:CallToolResult|error; // Special Agent Note: CallToolParams, CallToolResult FROM ballerina/mcp package
+
+    function getTools() returns ToolConfig[];
+}
+
+# Initializes the toolkit with the given service url and http tools.
+# 
+class HttpServiceToolKit {
+    function init(string serviceUrl, HttpTool[] httpTools, http:ClientConfiguration clientConfig = {}, map<string|string[]> headers = {}) returns Error?; // Special Agent Note: ClientConfiguration FROM ballerina/http package
+
+    # Useful to retrieve the Tools extracted from the HttpTools.
+    function getTools() returns ToolConfig[];
+}
+
+# Initializes a new in-memory vector store.
+# 
+class InMemoryVectorStore {
+    function init(SimilarityMetric similarityMetric = COSINE) returns Error?;
+
+    # Adds vector entries to the in-memory store.
+    # Only supports dense vectors in this implementation. 
+    # If a vector entry with the same ID already exists, it will be replaced.
+    # 
+    function add(VectorEntry[] entries) returns Error|();
+
+    # Queries the vector store for vectors similar to the given query.
+    # 
+    function query(VectorStoreQuery query) returns VectorMatch[]|Error;
+
+    # Deletes a vector entry from the in-memory store.
+    # Remove entries that matches the given reference identifiers.
+    # 
+    function delete(string|string[] ids) returns Error|();
+}
+
 // --- Client ---
 
 # A client class for interacting with a chat service.
@@ -2509,7 +2991,7 @@
 
 # WSO2 embedding provider implementation that provides embedding capabilities using WSO2's AI service.
 client class Wso2EmbeddingProvider {
-    function init(string serviceUrl, string accessToken, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(string serviceUrl, string accessToken, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Converts chunk to embedding.
     # 
@@ -2522,7 +3004,7 @@
 
 # WSO2 model provider implementation that provides chat completion capabilities using WSO2's AI services.
 client class Wso2ModelProvider {
-    function init(string serviceUrl, string accessToken, decimal temperature = 0.7, ai:GeneratorConfig & readonly generatorConfig = {}, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "Access Token"} string accessToken, @display {label: "Temperature"} decimal temperature = 0.7, @display {label: "Generator Configuration"} ai:GeneratorConfig & readonly generatorConfig = {}, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the model with the given messages and tools.
     # 
@@ -2531,7 +3013,7 @@
     # Sends a chat request to the model and generates a value that belongs to the type
     # corresponding to the type descriptor argument.
     # 
-    remote function generate(Prompt prompt, anydata td = anydata) returns td|Error;
+    remote function generate(Prompt prompt, @display {label: "Expected type"} anydata td = anydata) returns td|Error;
 }
 
 // --- Functions ---
@@ -2590,7 +3072,7 @@
 # + extractDefault - Flag to extract default values of parameters and schema attributes from the OpenAPI specification
 # + additionInfoFlags - Flags to extract additional information from the OpenAPI specification
 # + return - A record with the list of extracted tools and the service URL (if available)
-function extractToolsFromOpenApiSpecFile(string filePath, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns ballerina/ai:1.13.0:HttpApiSpecification & readonly|Error;
+function extractToolsFromOpenApiSpecFile(string filePath, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns HttpApiSpecification & readonly|Error;
 
 # Extracts the Http tools from the given OpenAPI specification as a JSON 
 # 
@@ -2599,7 +3081,7 @@
 # + extractDefault - Flag to extract default values of parameters and schema attributes from the OpenAPI specification
 # + additionInfoFlags - Flags to extract additional information from the OpenAPI specification
 # + return - A record with the list of extracted tools and the service URL (if available)
-function extractToolsFromOpenApiJsonSpec(map<json> openApiSpec, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns ballerina/ai:1.13.0:HttpApiSpecification & readonly|Error;
+function extractToolsFromOpenApiJsonSpec(map<json> openApiSpec, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns HttpApiSpecification & readonly|Error;
 
 # Parses the given OpenAPI specification as a JSON to a OpenApiSpec object.
 # 
@@ -2633,7 +3115,7 @@
 # 
 # + evalSetPath - Path to the JSON file containing the evaluation dataset
 # + return - Map of conversation threads indexed by thread ID, or an `Error` if the file cannot be read or parsed
-function loadConversationThreads(string evalSetPath) returns map<[ballerina/ai:1.13.0:ConversationThread & readonly]>|Error;
+function loadConversationThreads(string evalSetPath) returns map<[ConversationThread & readonly]>|Error;
 
 # Extracts the user query from a conversation trace.
 # 
@@ -2679,5 +3161,12 @@
 // --- Service ---
 
 service ai:ChatService on new ai:Listener(int|http:Listener listenOn = 8090) {
-    remote function chat(ChatReqMessage request) returns ChatRespMessage|error;
+    remote function chat(ai:ChatReqMessage request) returns ai:ChatRespMessage|error;
 }
+
+// --- Annotations ---
+
+public annotation map<json> JsonSchema on type;
+
+# Represents the annotation of a function tool.
+public annotation ToolAnnotationConfig AgentTool on function, object function;
`````

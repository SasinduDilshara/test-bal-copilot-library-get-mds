# ai.agent — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.agent` |
| **Old file** | `ai.agent/old/ballerinax_ai.agent.bal.txt` |
| **New file** | `ai.agent/new/ballerinax_ai.agent.bal.txt` |
| **Old lines** | 2128 |
| **New lines** | 2315 |
| **Lines added** | 280 |
| **Lines removed** | 93 |
| **Hunks** | 54 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 31 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 75 | 0 |
| `// --- section ---` markers | 5 | 6 |

### Declarations added (50)

- `annotation Tool`
- `class DefaultMessageWindowChatMemoryManager`
- `class Executor`
- `class HttpServiceToolKit`
- `class Iterator`
- `class Listener`
- `class MessageWindowChatMemory`
- `class ToolStore`
- `client class BaseAgent`
- `client class Model`
- `function 'start`
- `function act`
- `function attach`
- `function chat`
- `function delete`
- `function detach`
- `function get`
- `function getMemory`
- `function getTools`
- `function gracefulStop`
- `function hasNext`
- `function immediateStop`
- `function iterator`
- `function next`
- `function reason`
- `function update`
- `type Error`
- `type FunctionTool`
- `type HttpResponseParsingError`
- `type HttpServiceToolKitError`
- `type IncompleteSpecificationError`
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
- `type ToolExecutionError`
- `type ToolInvalidInputError`
- `type ToolInvalidOutputError`
- `type ToolNotFoundError`
- `type UnsupportedMediaTypeError`
- `type UnsupportedOpenApiVersion`
- `type UnsupportedSerializationError`

### Declarations removed (2)

- `class BaseAgent`
- `class Model`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 739–754 | 739–759 | Types | +11 | −6 |
| 2 | 763–776 | 768–799 | Types | +21 | −3 |
| 3 | 828–834 | 851–857 | Types | +1 | −1 |
| 4 | 889–895 | 912–918 | Types | +1 | −1 |
| 5 | 901–907 | 924–930 | Types | +1 | −1 |
| 6 | 919–940 | 942–971 | Types | +9 | −1 |
| 7 | 942–966 | 973–1008 | Types | +11 | −0 |
| 8 | 976–1018 | 1018–1079 | Types | +38 | −19 |
| 9 | 1026–1031 | 1087–1101 | Types | +9 | −0 |
| 10 | 1037–1042 | 1107–1113 | Types | +1 | −0 |
| 11 | 1070–1075 | 1141–1147 | Types | +1 | −0 |
| 12 | 1081–1086 | 1153–1159 | Types | +1 | −0 |
| 13 | 1108–1141 | 1181–1229 | Types | +15 | −0 |
| 14 | 1203–1209 | 1291–1297 | Types | +1 | −1 |
| 15 | 1219–1265 | 1307–1375 | Types | +22 | −0 |
| 16 | 1319–1325 | 1429–1435 | Types | +1 | −1 |
| 17 | 1330–1336 | 1440–1446 | Types | +1 | −1 |
| 18 | 1338–1344 | 1448–1454 | Types | +1 | −1 |
| 19 | 1368–1374 | 1478–1484 | Types | +1 | −1 |
| 20 | 1398–1404 | 1508–1514 | Types | +1 | −1 |
| 21 | 1416–1422 | 1526–1532 | Types | +1 | −1 |
| 22 | 1426–1432 | 1536–1542 | Types | +1 | −1 |
| 23 | 1444–1455 | 1554–1565 | Types | +2 | −2 |
| 24 | 1473–1479 | 1583–1589 | Types | +1 | −1 |
| 25 | 1489–1495 | 1599–1605 | Types | +1 | −1 |
| 26 | 1503–1509 | 1613–1619 | Types | +1 | −1 |
| 27 | 1513–1519 | 1623–1629 | Types | +1 | −1 |
| 28 | 1527–1538 | 1637–1648 | Types | +2 | −2 |
| 29 | 1544–1550 | 1654–1660 | Types | +1 | −1 |
| 30 | 1556–1562 | 1666–1672 | Types | +1 | −1 |
| 31 | 1570–1576 | 1680–1686 | Types | +1 | −1 |
| 32 | 1582–1588 | 1692–1698 | Types | +1 | −1 |
| 33 | 1600–1606 | 1710–1716 | Types | +1 | −1 |
| 34 | 1617–1625 | 1727–1735 | Types | +2 | −2 |
| 35 | 1640–1646 | 1750–1756 | Types | +1 | −1 |
| 36 | 1651–1657 | 1761–1767 | Types | +1 | −1 |
| 37 | 1664–1670 | 1774–1780 | Types | +1 | −1 |
| 38 | 1687–1693 | 1797–1803 | Types | +1 | −1 |
| 39 | 1698–1704 | 1808–1814 | Types | +1 | −1 |
| 40 | 1750–1756 | 1860–1866 | Types | +1 | −1 |
| 41 | 1766–1782 | 1876–1892 | Types | +6 | −6 |
| 42 | 1829–1835 | 1939–1945 | Types | +1 | −1 |
| 43 | 1890–1896 | 2000–2006 | Types | +1 | −1 |
| 44 | 1963–1991 | 2073–2173 | Types | +80 | −8 |
| 45 | 2000–2023 | 2182–2205 | Client | +5 | −5 |
| 46 | 2026–2032 | 2208–2214 | Client | +1 | −1 |
| 47 | 2035–2041 | 2217–2223 | Client | +1 | −1 |
| 48 | 2043–2049 | 2225–2231 | Client | +1 | −1 |
| 49 | 2052–2058 | 2234–2240 | Client | +1 | −1 |
| 50 | 2061–2079 | 2243–2261 | Client | +4 | −4 |
| 51 | 2087–2093 | 2269–2275 | Functions | +1 | −1 |
| 52 | 2104–2110 | 2286–2292 | Functions | +1 | −1 |
| 53 | 2113–2119 | 2295–2301 | Functions | +1 | −1 |
| 54 | 2126–2128 | 2308–2315 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- ai.agent/old/ballerinax_ai.agent.bal.txt	2026-08-12 12:57:29
+++ ai.agent/new/ballerinax_ai.agent.bal.txt	2026-08-12 13:19:19
@@ -739,16 +739,21 @@
     string observation;
 };
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
-// Unknown type: LlmError
-
-// Unknown type: LlmInvalidGenerationError
+# Any error occurred during LLM generation is classified under this error type.
+type LlmError error;
 
-// Unknown type: ToolExecutionError
+# Errors occurred due to invalid LLM generation.
+type LlmInvalidGenerationError error;
 
-// Unknown type: MemoryError
+# Errors during tool execution.
+type ToolExecutionError error;
 
+# Represents errors that occur during memory-related operations.  
+type MemoryError error;
+
 # An chat response by the LLM
 
 type LlmChatResponse record {
@@ -763,14 +768,32 @@
     anydata|error value;
 };
 
-class BaseAgent {
+client class BaseAgent {
+
+    # Parse the llm response and extract the tool to be executed.
+    # 
+    function parseLlmResponse(json llmResponse) returns LlmToolResponse|LlmChatResponse|LlmInvalidGenerationError;
+
+    # Use LLM to decide the next tool/step.
+    # 
+    function selectNextTool(ExecutionProgress progress, string memoryId = memoryId) returns json|LlmError;
+
+    remote function run(string query, int maxIter = 5, string|map<json> context = {}, boolean verbose = true, string memoryId = memoryId) returns record {|(ExecutionResult|ExecutionError)[] steps; string answer?;|};
 }
 
 # Represents an extendable client for interacting with an AI model.
-class Model {
+client class Model {
+
+    # Sends a chat request to the model with the given messages and tools.
+    remote function chat(ChatMessage[] messages, ChatCompletionFunctions[] tools = [], string|() stop = ()) returns ChatAssistantMessage[]|LlmError;
 }
 
-// Unknown type: ToolStore
+# Register tools to the agent. 
+# These tools will be by the LLM to perform tasks.
+# 
+class ToolStore {
+    function init(BaseToolKit|ToolConfig|FunctionTool[] tools) returns Error?;
+}
 
 # This is the tool used by LLMs during reasoning.
 # This tool is same as the Tool record, but it has a clear separation between the variables that should be generated with the help of the LLMs and the constants that are defined by the users. 
@@ -828,7 +851,7 @@
     # List of required properties
     string[] required?;
     # Schema of the object properties
-    map<ballerinax/ai.agent:0.9.2:JsonSubSchema> properties?;
+    map<JsonSubSchema> properties?;
     string description?;
     json default?;
     boolean nullable?;
@@ -889,7 +912,7 @@
 };
 
 # Defines a json input schema
-type JsonInputSchema ballerinax/ai.agent:0.9.2:ObjectInputSchema|ballerinax/ai.agent:0.9.2:ArrayInputSchema|ballerinax/ai.agent:0.9.2:AnyOfInputSchema|ballerinax/ai.agent:0.9.2:OneOfInputSchema|ballerinax/ai.agent:0.9.2:AllOfInputSchema|ballerinax/ai.agent:0.9.2:NotInputSchema;
+type JsonInputSchema ObjectInputSchema|ArrayInputSchema|AnyOfInputSchema|OneOfInputSchema|AllOfInputSchema|NotInputSchema;
 
 # Defines a primitive input field in the schema.
 
@@ -901,7 +924,7 @@
     # Pattern of the input. This is only applicable for `STRING` type.
     string pattern?;
     # Enum values of the input. This is only applicable for `STRING` type.
-    (ballerinax/ai.agent:0.9.2:PrimitiveType?)[] 'enum?;
+    (PrimitiveType?)[] 'enum?;
     # Default value of the input
     PrimitiveType default?;
     string description?;
@@ -919,22 +942,30 @@
 };
 
 # Defines a json sub schema
-type JsonSubSchema ballerinax/ai.agent:0.9.2:ObjectInputSchema|ballerinax/ai.agent:0.9.2:ArrayInputSchema|ballerinax/ai.agent:0.9.2:AnyOfInputSchema|ballerinax/ai.agent:0.9.2:OneOfInputSchema|ballerinax/ai.agent:0.9.2:AllOfInputSchema|ballerinax/ai.agent:0.9.2:NotInputSchema|ballerinax/ai.agent:0.9.2:PrimitiveInputSchema|ballerinax/ai.agent:0.9.2:ConstantValueSchema;
+type JsonSubSchema ObjectInputSchema|ArrayInputSchema|AnyOfInputSchema|OneOfInputSchema|AllOfInputSchema|NotInputSchema|PrimitiveInputSchema|ConstantValueSchema;
 
 # Represents the interface of a memory manager.
 class MemoryManager {
+
+    # Retrieves memory based on the given memory ID.
+    # 
+    function getMemory(string memoryId) returns Memory|MemoryError;
 }
 
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
 
 # Represents the different types of agents supported by the module.
+@display {label: "Agent Type"}
 enum AgentType {
     FUNCTION_CALL_AGENT,
     REACT_AGENT
@@ -942,25 +973,36 @@
 
 # Provides a set of configurations for the agent.
 
+@display {label: "Agent Configuration"}
 type AgentConfiguration record {
     # The system prompt assigned to the agent
+    @display {label: "System Prompt"}
     SystemPrompt systemPrompt;
     # The model used by the agent
+    @display {label: "Model"}
     Model model;
     # The tools available for the agent
+    @display {label: "Tools"}
     BaseToolKit|ToolConfig|FunctionTool[] tools?;
     # Type of the agent
+    @display {label: "Agent Type"}
     AgentType agentType?;
     # The maximum number of iterations the agent performs to complete the task
+    @display {label: "Maximum Iterations"}
     int maxIter?;
     # Specifies whether verbose logging is enabled
+    @display {label: "Verbose"}
     boolean verbose?;
     # The memory manager used by the agent to store and manage conversation history
+    @display {label: "Memory Manager"}
     MemoryManager memoryManager?;
 };
 
 # Allows implmenting custom toolkits by extending this type. Toolkits can help to define new types of tools so that agent can understand them.
 class BaseToolKit {
+
+    # Useful to retrieve the Tools extracted from the Toolkit.
+    function getTools() returns ToolConfig[];
 }
 
 # Defines a tool. This is the only tool type directly understood by the agent. All other tool types are converted to this type using toolkits.
@@ -976,43 +1018,62 @@
     FunctionTool caller;
 };
 
-// Unknown type: FunctionTool
+# Represents a type alias for an isolated function, representing a function tool.
+type FunctionTool function;
 
-// Unknown type: OpenApiParsingError
+# Any error occurred during parsing OpenAPI specification is classified under this error type.
+type OpenApiParsingError error;
 
-// Unknown type: ParsingStackOverflowError
+# Stackoverflow errors due to lenthy OpenAPI specification or cyclic references in the specification.
+type ParsingStackOverflowError error;
 
-// Unknown type: UnsupportedSerializationError
+# Errors occurred due to unsupported path parameter serializations.
+type UnsupportedSerializationError error;
 
-// Unknown type: UnsupportedOpenApiVersion
+# Errors due to unsupported OpenAPI specification version.
+type UnsupportedOpenApiVersion error;
 
-// Unknown type: InvalidReferenceError
+# Errors due to invalid or broken references in the OpenAPI specification.
+type InvalidReferenceError error;
 
-// Unknown type: IncompleteSpecificationError
+# Errors due to incomplete OpenAPI specification.
+type IncompleteSpecificationError error;
 
-// Unknown type: UnsupportedMediaTypeError
+# Errors due to unsupported media type.
+type UnsupportedMediaTypeError error;
 
-// Unknown type: InvalidParameterDefinition
+# Error through due to invalid parameter definition that does not include either schema or content.
+type InvalidParameterDefinition error;
 
-// Unknown type: LlmInvalidResponseError
+# Errors occurred due to unexpected responses from the LLM.
+type LlmInvalidResponseError error;
 
-// Unknown type: LlmConnectionError
+# Errors occurred during LLM generation due to connection.
+type LlmConnectionError error;
 
-// Unknown type: TaskCompletedError
+# Errors occurred due to termination of the Agent's execution.
+type TaskCompletedError error;
 
-// Unknown type: HttpServiceToolKitError
+# Errors occurred due while running HTTP service toolkit.
+type HttpServiceToolKitError error;
 
-// Unknown type: HttpResponseParsingError
+# Any error occurred during parsing HTTP response is classified under this error type.
+type HttpResponseParsingError error;
 
-// Unknown type: ToolInvalidOutputError
+# Error during unexpected output by the tool
+type ToolInvalidOutputError error;
 
-// Unknown type: ToolNotFoundError
+# Errors occurred due to invalid tool name generated by the LLM.
+type ToolNotFoundError error;
 
-// Unknown type: ToolInvalidInputError
+# Errors occurred due to invalid input to the tool generated by the LLM.
+type ToolInvalidInputError error;
 
-// Unknown type: MissingHttpParameterError
+# Errors occurred due to missing mandotary path or query parameters.
+type MissingHttpParameterError error;
 
-// Unknown type: MaxIterationExceededError
+# Represents an error that occurs when the maximum number of iterations has been exceeded.
+type MaxIterationExceededError error<record {|(ExecutionResult|ExecutionError)[] steps;|}>;
 
 enum EncodingStyle {
     DEEPOBJECT,
@@ -1026,6 +1087,15 @@
 
 # Represents the memory interface for the agents.
 class Memory {
+
+    # Retrieves all stored chat messages.
+    function get() returns ChatMessage[]|MemoryError;
+
+    # Adds a chat message to the memory.
+    function update(ChatMessage message) returns MemoryError|();
+
+    # Deletes all stored messages.
+    function delete() returns MemoryError|();
 }
 
 # Roles for the chat messages.
@@ -1037,6 +1107,7 @@
 }
 
 # Model types for OpenAI
+@display {label: "OpenAI Model Names"}
 enum OPEN_AI_MODEL_NAMES {
     GPT_3_5_TURBO_16K_0613,
     GPT_3_5_TURBO_0125,
@@ -1070,6 +1141,7 @@
 }
 
 # Models types for Anthropic
+@display {label: "Anthropic Model Names"}
 enum ANTHROPIC_MODEL_NAMES {
     CLAUDE_3_HAIKU_20240307,
     CLAUDE_3_SONNET_20240229,
@@ -1081,6 +1153,7 @@
 }
 
 # Models types for Mistral AI
+@display {label: "Mistral AI Model Names"}
 enum MISTRAL_AI_MODEL_NAMES {
     MISTRAL_LARGE_MODEL,
     MISTRAL_MEDIUM_MODEL,
@@ -1108,34 +1181,49 @@
 
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
 
@@ -1203,7 +1291,7 @@
 };
 
 # Chat message record.
-type ChatMessage ballerinax/ai.agent:0.9.2:ChatUserMessage|ballerinax/ai.agent:0.9.2:ChatSystemMessage|ballerinax/ai.agent:0.9.2:ChatAssistantMessage|ballerinax/ai.agent:0.9.2:ChatFunctionMessage;
+type ChatMessage ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage;
 
 # Function definitions for function calling API.
 
@@ -1219,47 +1307,69 @@
 # Represents the model parameters for Ollama text generation.
 # These parameters control the behavior and output of the model.
 
+@display {label: "Ollama Model Parameters"}
 type OllamaModelParameters record {
     # Enable Mirostat sampling for controlling perplexity.  
 - `0` = disabled  
 - `1` = Mirostat  
 - `2` = Mirostat 2.0  
+    @display {label: "Mirostat Sampling"}
     0|1|2 mirostat?;
     # Influences how quickly the algorithm responds to feedback from the generated text.  
 A lower value results in slower adjustments, while a higher value makes the model more responsive.  
+    @jsondata:Name {value: "mirostat_eta"}
+    @display {label: "Mirostat eta"}
     float mirostatEta?;
     # Controls the balance between coherence and diversity of the output.  
 A lower value results in more focused and coherent text.  
+    @jsondata:Name {value: "mirostat_tau"}
+    @display {label: "Mirostat tau"}
     float mirostatTau?;
     # Sets the size of the context window used to generate the next token.  
+    @jsondata:Name {value: "num_ctx"}
+    @display {label: "Context Window Size"}
     int numCtx?;
     # Sets how far back the model should look to prevent repetition.  
 - `0` = disabled  
 - `-1` = num_ctx  
+    @jsondata:Name {value: "repeat_last_n"}
+    @display {label: "Repeat Last N"}
     int repeatLastN?;
     # Sets how strongly to penalize repetitions.  
 A higher value (e.g., `1.5`) will penalize repetitions more strongly,  
 while a lower value (e.g., `0.9`) will be more lenient.  
+    @jsondata:Name {value: "repeat_penalty"}
+    @display {label: "Repeat Penalty"}
     float repeatPenalty?;
     # Controls the creativity of the model's responses.  
 A higher value makes the output more diverse, while a lower value makes it more focused.  
+    @display {label: "Temperature"}
     float temperature?;
     # Sets the random number seed for deterministic text generation.  
 A specific value ensures the same output for identical prompts.  
+    @display {label: "Seed"}
     int seed?;
     # Maximum number of tokens to generate.  
 `-1` allows infinite generation.  
+    @jsondata:Name {value: "num_predict"}
+    @display {label: "Number of Tokens to Predict"}
     int numPredict?;
     # Controls randomness by selecting the top-k most likely next words.  
 A higher value (e.g., `100`) increases diversity,  
 while a lower value (e.g., `10`) makes responses more conservative.  
+    @jsondata:Name {value: "top_k"}
+    @display {label: "Top K"}
     int topK?;
     # Controls randomness by considering the cumulative probability of choices.  
 A higher value (e.g., `0.95`) increases diversity,  
 while a lower value (e.g., `0.5`) makes responses more conservative.  
+    @jsondata:Name {value: "top_p"}
+    @display {label: "Top P"}
     float topP?;
     # Ensures a balance between quality and variety.  
 Filters out low-probability tokens relative to the highest probability token.  
+    @jsondata:Name {value: "min_p"}
+    @display {label: "Min P"}
     float minP?;
 };
 
@@ -1319,7 +1429,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1330,7 +1440,7 @@
     never properties?;
     # Can not have items in a primitive type schema
     never items?;
-    string type;
+    string 'type;
     never anyOf?;
     never oneOf?;
     never allOf?;
@@ -1338,7 +1448,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1368,7 +1478,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1398,7 +1508,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1416,7 +1526,7 @@
     # Regular expression pattern of the string value
     string pattern?;
     # Enum values of the string value
-    (ballerinax/ai.agent:0.9.2:PrimitiveType?)[] 'enum?;
+    (PrimitiveType?)[] 'enum?;
     never properties?;
     never items?;
     never anyOf?;
@@ -1426,7 +1536,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1444,12 +1554,12 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
 # Primitive type schema object.
-type PrimitiveTypeSchema ballerinax/ai.agent:0.9.2:IntegerSchema|ballerinax/ai.agent:0.9.2:NumberSchema|ballerinax/ai.agent:0.9.2:StringSchema|ballerinax/ai.agent:0.9.2:BooleanSchema;
+type PrimitiveTypeSchema IntegerSchema|NumberSchema|StringSchema|BooleanSchema;
 
 # Array schema object.
 
@@ -1473,7 +1583,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1489,7 +1599,7 @@
     # List of required properties
     boolean|string[] required?;
     # List of properties
-    map<ballerinax/ai.agent:0.9.2:Schema> properties?;
+    map<Schema> properties?;
     # Additional properties
     boolean|IntegerSchema|NumberSchema|StringSchema|BooleanSchema|ArraySchema|ObjectSchemaType1|ObjectSchemaType2|OneOfSchema|AllOfSchema|AnyOfSchema|NotSchema|Reference additionalProperties?;
     # Discriminator
@@ -1503,7 +1613,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1513,7 +1623,7 @@
     # To match when type is not specified, but properties are specified
     never 'type?;
     # List of properties
-    map<ballerinax/ai.agent:0.9.2:Schema> properties;
+    map<Schema> properties;
     int minProperties?;
     int maxProperties?;
     boolean|string[] required?;
@@ -1527,12 +1637,12 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
 # Defines an object schema.
-type ObjectSchema ballerinax/ai.agent:0.9.2:ObjectSchemaType1|ballerinax/ai.agent:0.9.2:ObjectSchemaType2;
+type ObjectSchema ObjectSchemaType1|ObjectSchemaType2;
 
 # One of schema object.
 
@@ -1544,7 +1654,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1556,7 +1666,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1570,7 +1680,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1582,7 +1692,7 @@
     string description?;
     json default?;
     boolean nullable?;
-    XmlSchema xml?;
+    XmlSchema 'xml?;
     never \$ref?;
 };
 
@@ -1600,7 +1710,7 @@
 };
 
 # Defines a OpenAPI schema.
-type Schema ballerinax/ai.agent:0.9.2:IntegerSchema|ballerinax/ai.agent:0.9.2:NumberSchema|ballerinax/ai.agent:0.9.2:StringSchema|ballerinax/ai.agent:0.9.2:BooleanSchema|ballerinax/ai.agent:0.9.2:ArraySchema|ballerinax/ai.agent:0.9.2:ObjectSchemaType1|ballerinax/ai.agent:0.9.2:ObjectSchemaType2|ballerinax/ai.agent:0.9.2:OneOfSchema|ballerinax/ai.agent:0.9.2:AllOfSchema|ballerinax/ai.agent:0.9.2:AnyOfSchema|ballerinax/ai.agent:0.9.2:NotSchema|ballerinax/ai.agent:0.9.2:Reference;
+type Schema IntegerSchema|NumberSchema|StringSchema|BooleanSchema|ArraySchema|ObjectSchemaType1|ObjectSchemaType2|OneOfSchema|AllOfSchema|AnyOfSchema|NotSchema|Reference;
 
 # Discriminator object.
 
@@ -1617,9 +1727,9 @@
     # A short description of the response
     string description?;
     # A map containing schema of the response headers
-    map<ballerinax/ai.agent:0.9.2:Header|ballerinax/ai.agent:0.9.2:Reference> headers?;
+    map<Header|Reference> headers?;
     # A map containing the structure of the response body
-    map<ballerinax/ai.agent:0.9.2:MediaType> content?;
+    map<MediaType> content?;
     # Not allowed $ref
     never \$ref?;
 };
@@ -1640,7 +1750,7 @@
     # Schema of the header parameter
     Schema schema?;
     # Content of the header parameter
-    map<ballerinax/ai.agent:0.9.2:MediaType> content?;
+    map<MediaType> content?;
     # Not allowed $ref
     never \$ref?;
 };
@@ -1651,7 +1761,7 @@
     # Schema of the content
     Schema schema?;
     # Encoding of the content
-    map<ballerinax/ai.agent:0.9.2:Encoding> encoding?;
+    map<Encoding> encoding?;
 };
 
 # Describes a encoding definition applied to a schema property.
@@ -1664,7 +1774,7 @@
     # The Content-Type for encoding a specific property
     string contentType?;
     # A map allowing additional information to be provided as headers
-    map<ballerinax/ai.agent:0.9.2:Header|ballerinax/ai.agent:0.9.2:Reference> headers?;
+    map<Header|Reference> headers?;
 };
 
 # Describes a single operation parameter.
@@ -1687,7 +1797,7 @@
     # Schema of the parameter
     Schema schema?;
     # Content of the parameter
-    map<ballerinax/ai.agent:0.9.2:MediaType> content?;
+    map<MediaType> content?;
     # Null value is allowed
     boolean nullable?;
 };
@@ -1698,7 +1808,7 @@
     # A brief description of the request body. This could contain examples of use.
     string description?;
     # The content of the request body. 
-    map<ballerinax/ai.agent:0.9.2:MediaType> content;
+    map<MediaType> content;
     # Whether the request body is mandatory in the request.
     boolean required?;
 };
@@ -1750,7 +1860,7 @@
     # The request body applicable for this operation
     RequestBody|Reference requestBody?;
     # The list of possible responses as they are returned from executing this operation
-    map<ballerinax/ai.agent:0.9.2:Response|ballerinax/ai.agent:0.9.2:Reference> responses?;
+    map<Response|Reference> responses?;
 };
 
 # Server information object.
@@ -1766,17 +1876,17 @@
 
 type Components record {
     # A map of reusable schemas for different data types
-    map<ballerinax/ai.agent:0.9.2:Schema|ballerinax/ai.agent:0.9.2:Reference> schemas?;
+    map<Schema|Reference> schemas?;
     # A map of reusable response objects 
-    map<ballerinax/ai.agent:0.9.2:Response|ballerinax/ai.agent:0.9.2:Reference> responses?;
+    map<Response|Reference> responses?;
     # A map of reusable parameter objects
-    map<ballerinax/ai.agent:0.9.2:Parameter|ballerinax/ai.agent:0.9.2:Reference> parameters?;
+    map<Parameter|Reference> parameters?;
     # A map of reusable request body objects
-    map<ballerinax/ai.agent:0.9.2:RequestBody|ballerinax/ai.agent:0.9.2:Reference> requestBodies?;
+    map<RequestBody|Reference> requestBodies?;
     # A map of reusable header objects
-    map<ballerinax/ai.agent:0.9.2:Header|ballerinax/ai.agent:0.9.2:Reference> headers?;
+    map<Header|Reference> headers?;
     # A map of PathItem objects
-    map<ballerinax/ai.agent:0.9.2:PathItem|ballerinax/ai.agent:0.9.2:Reference> pathItems?;
+    map<PathItem|Reference> pathItems?;
 };
 
 # Map of pathItem objects.
@@ -1829,7 +1939,7 @@
     # Path of the Http resource
     string path;
     # path and query parameters definitions of the Http resource
-    map<ballerinax/ai.agent:0.9.2:ParameterSchema> parameters?;
+    map<ParameterSchema> parameters?;
     # Request body definition of the Http resource
     RequestBodySchema requestBody?;
 };
@@ -1890,7 +2000,7 @@
 # Defines a internal value field in the schema
 
 type InternalValueSchema record {
-    json const;
+    json 'const;
 };
 
 # Defines the configuration of the Tool annotation.
@@ -1963,29 +2073,101 @@
 
 # Defines a chat service interface that handles incoming chat messages.
 class ChatService {
+
+    resource function post chat(@http:Payload ChatReqMessage request) returns ChatRespMessage|error;
 }
 
-// Unknown type: Iterator
+# Initialize the iterator with the agent and the query.
+# 
+class Iterator {
+    function init(BaseAgent agent, string memoryId, string query = "", ExecutionStep[] history = [], map<json>|string|() context = (), ExecutionProgress progress) returns ();
 
-// Unknown type: Executor
+    # Iterate over the agent's execution steps.
+    function iterator() returns object {public function next() returns record {|ExecutionResult|LlmChatResponse|ExecutionError|Error value;|}?;};
+}
 
-// Unknown type: Listener
+# Initialize the executor with the agent and the query.
+# 
+class Executor {
+    function init(BaseAgent agent, string memoryId, string query = "", ExecutionStep[] history = [], map<json>|string|() context = (), ExecutionProgress progress) returns ();
 
-// Unknown type: MessageWindowChatMemory
+    # Checks whether agent has more steps to execute.
+    # 
+    function hasNext() returns boolean;
 
-// Unknown type: DefaultMessageWindowChatMemoryManager
+    # Reason the next step of the agent.
+    # 
+    function reason() returns json|TaskCompletedError|LlmError;
 
-// Unknown type: HttpServiceToolKit
+    # Execute the next step of the agent.
+    # 
+    function act(json llmResponse) returns ExecutionResult|LlmChatResponse|ExecutionError;
+
+    # Update the agent with an execution step.
+    # 
+    function update(ExecutionStep step) returns ();
+
+    # Reason and execute the next step of the agent.
+    # 
+    function next() returns record {|ExecutionResult|LlmChatResponse|ExecutionError|Error value;|}?;
+}
+
+class Listener {
+    function init(int|http:Listener listenOn = 8090) returns error?; // Special Agent Note: Listener FROM ballerina/http package
 
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
+class MessageWindowChatMemory {
+    function init(int size = 10) returns ();
+
+    # Retrieves a copy of all stored messages, with an optional system prompt.
+    function get() returns ChatMessage[]|MemoryError;
+
+    # Adds a message to the window.
+    function update(ChatMessage message) returns MemoryError|();
+
+    # Removes all messages from the memory.
+    function delete() returns MemoryError|();
+}
+
+# Initializes a new `agent:DefaultMessageWindowChatMemoryManager`.
+# 
+class DefaultMessageWindowChatMemoryManager {
+    function init(int size = 10) returns ();
+
+    # Retrieves memory based on the given memory ID.
+    # 
+    function getMemory(string memoryId) returns Memory|MemoryError;
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
 // --- Client ---
 
 # Represents an agent.
 client class Agent {
-    function init(SystemPrompt systemPrompt = {role: "", instructions: ""}, Model model = object {}, BaseToolKit|ToolConfig|FunctionTool[] tools = [], AgentType agentType = FUNCTION_CALL_AGENT, int maxIter = 5, boolean verbose = false, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager(), AgentConfiguration config) returns ballerinax/ai.agent:0.9.2:Error?;
+    function init(SystemPrompt systemPrompt = {role: "", instructions: ""}, Model model = object {}, BaseToolKit|ToolConfig|FunctionTool[] tools = [], AgentType agentType = FUNCTION_CALL_AGENT, int maxIter = 5, boolean verbose = false, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager(), @display {label: "Agent Configuration"} AgentConfiguration config) returns Error?;
 
     # Executes the agent for a given user query.
     # 
-    remote function run(string query, string memoryId = "") returns string|Error;
+    remote function run(@display {label: "Query"} string query, @display {label: "Memory ID"} string memoryId = "") returns string|Error;
 }
 
 # A client class for interacting with a chat service.
@@ -2000,24 +2182,24 @@
 # Function call agent. 
 # This agent uses OpenAI function call API to perform the tool selection.
 client class FunctionCallAgent {
-    function init(Model model, BaseToolKit|ToolConfig|FunctionTool[] tools, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager()) returns ballerinax/ai.agent:0.9.2:Error?;
+    function init(Model model, BaseToolKit|ToolConfig|FunctionTool[] tools, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager()) returns Error?;
 
     # Parse the function calling API response and extract the tool to be executed.
     # 
-    remote function parseLlmResponse(json llmResponse) returns LlmToolResponse|LlmChatResponse|LlmInvalidGenerationError;
+    function parseLlmResponse(json llmResponse) returns LlmToolResponse|LlmChatResponse|LlmInvalidGenerationError;
 
     # Use LLM to decide the next tool/step based on the function calling APIs.
     # 
-    remote function selectNextTool(ExecutionProgress progress, string memoryId = "") returns json|LlmError;
+    function selectNextTool(ExecutionProgress progress, string memoryId = "") returns json|LlmError;
 
     # Execute the agent for a given user's query.
     # 
-    remote function run(string query, int maxIter = 0, string|map<json> context = "", boolean verbose = false, string memoryId = "") returns ExecutionError)[] steps; string answer?;|};
+    remote function run(string query, int maxIter = 0, string|map<json> context = "", boolean verbose = false, string memoryId = "") returns record {|(ExecutionResult|ExecutionError)[] steps; string answer?;|};
 }
 
 # OpenAiModel is a client class that provides an interface for interacting with OpenAI language models.
 client class OpenAiModel {
-    function init(string apiKey, OPEN_AI_MODEL_NAMES modelType, string serviceUrl = https://api.openai.com/v1, int maxTokens = 512, decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerinax/ai.agent:0.9.2:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} OPEN_AI_MODEL_NAMES modelType, @display {label: "Service URL"} string serviceUrl = https://api.openai.com/v1, @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the OpenAI model with the given messages and tools.
     # 
@@ -2026,7 +2208,7 @@
 
 # AzureOpenAiModel is a client class that provides an interface for interacting with Azure-hosted OpenAI language models.
 client class AzureOpenAiModel {
-    function init(string serviceUrl, string apiKey, string deploymentId, string apiVersion, int maxTokens = 512, decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerinax/ai.agent:0.9.2:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Deployment ID"} string deploymentId, @display {label: "API Version"} string apiVersion, @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the OpenAI model with the given messages and tools.
     # 
@@ -2035,7 +2217,7 @@
 
 # AnthropicModel is a client class that provides an interface for interacting with Anthropic language models.
 client class AnthropicModel {
-    function init(string apiKey, ANTHROPIC_MODEL_NAMES modelType, string apiVersion, string serviceUrl = https://api.anthropic.com/v1, int maxTokens = 512, decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerinax/ai.agent:0.9.2:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} ANTHROPIC_MODEL_NAMES modelType, @display {label: "API Version"} string apiVersion, @display {label: "Service URL"} string serviceUrl = https://api.anthropic.com/v1, @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Uses Anthropic API to generate a response
     remote function chat(ChatMessage[] messages, ChatCompletionFunctions[] tools = [], string|() stop = ()) returns ChatAssistantMessage[]|LlmError;
@@ -2043,7 +2225,7 @@
 
 # MistralAiModel is a client class that provides an interface for interacting with Mistral AI language models.
 client class MistralAiModel {
-    function init(string apiKey, MISTRAL_AI_MODEL_NAMES modelType, string serviceUrl = https://api.mistral.ai/v1, int maxTokens = 512, decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerinax/ai.agent:0.9.2:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} MISTRAL_AI_MODEL_NAMES modelType, @display {label: "Service URL"} string serviceUrl = https://api.mistral.ai/v1, @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Uses function call API to determine next function to be called
     # 
@@ -2052,7 +2234,7 @@
 
 # Represents a client for interacting with an Ollama models.
 client class OllamaModel {
-    function init(string modelType, string serviceUrl = http://localhost:11434, 0|1|2 mirostat = 0, float mirostatEta = 0.1, float mirostatTau = 5.0, int numCtx = 2048, int repeatLastN = 64, float repeatPenalty = 1.1, float temperature = 0.8, int seed = 0, int numPredict = -1, int topK = 40, float topP = 0.9, float minP = 0.0, OllamaModelParameters modleParameters, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerinax/ai.agent:0.9.2:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Model Type"} string modelType, @display {label: "Service URL"} string serviceUrl = http://localhost:11434, 0|1|2 mirostat = 0, float mirostatEta = 0.1, float mirostatTau = 5.0, int numCtx = 2048, int repeatLastN = 64, float repeatPenalty = 1.1, float temperature = 0.8, int seed = 0, int numPredict = -1, int topK = 40, float topP = 0.9, float minP = 0.0, @display {label: "Ollama Model Parameters"} OllamaModelParameters modleParameters, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the Ollama model with the given messages and tools.
     # 
@@ -2061,19 +2243,19 @@
 
 # A ReAct Agent that uses ReAct prompt to answer questions by using tools.
 client class ReActAgent {
-    function init(Model model, BaseToolKit|ToolConfig|FunctionTool[] tools, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager()) returns ballerinax/ai.agent:0.9.2:Error?;
+    function init(Model model, BaseToolKit|ToolConfig|FunctionTool[] tools, MemoryManager memoryManager = new DefaultMessageWindowChatMemoryManager()) returns Error?;
 
     # Parse the ReAct llm response and extract the tool to be executed.
     # 
-    remote function parseLlmResponse(json llmResponse) returns LlmToolResponse|LlmChatResponse|LlmInvalidGenerationError;
+    function parseLlmResponse(json llmResponse) returns LlmToolResponse|LlmChatResponse|LlmInvalidGenerationError;
 
     # Use LLM to decide the next tool/step based on the ReAct prompting.
     # 
-    remote function selectNextTool(ExecutionProgress progress, string memoryId = "") returns json|LlmError;
+    function selectNextTool(ExecutionProgress progress, string memoryId = "") returns json|LlmError;
 
     # Execute the agent for a given user's query.
     # 
-    remote function run(string query, int maxIter = 0, string|map<json> context = "", boolean verbose = false, string memoryId = "") returns ExecutionError)[] steps; string answer?;|};
+    remote function run(string query, int maxIter = 0, string|map<json> context = "", boolean verbose = false, string memoryId = "") returns record {|(ExecutionResult|ExecutionError)[] steps; string answer?;|};
 }
 
 // --- Functions ---
@@ -2087,7 +2269,7 @@
 # + verbose - If true, then print the reasoning steps (default: true)
 # + memoryId - The ID associated with the memory
 # + return - Returns the execution steps tracing the agent's reasoning and outputs from the tools
-function run(BaseAgent agent, string query, int maxIter, string|map<json> context, boolean verbose, string memoryId = memoryId) returns ExecutionError)[] steps; string answer?;|};
+function run(BaseAgent agent, string query, int maxIter, string|map<json> context, boolean verbose, string memoryId = memoryId) returns record {|(ExecutionResult|ExecutionError)[] steps; string answer?;|};
 
 # Get the tools registered with the agent.
 # 
@@ -2104,7 +2286,7 @@
 # + extractDefault - Flag to extract default values of parameters and schema attributes from the OpenAPI specification
 # + additionInfoFlags - Flags to extract additional information from the OpenAPI specification
 # + return - A record with the list of extracted tools and the service URL (if available)
-function extractToolsFromOpenApiSpecFile(string filePath, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns ballerinax/ai.agent:0.9.2:HttpApiSpecification & readonly|Error;
+function extractToolsFromOpenApiSpecFile(string filePath, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns HttpApiSpecification & readonly|Error;
 
 # Extracts the Http tools from the given OpenAPI specification as a JSON 
 # 
@@ -2113,7 +2295,7 @@
 # + extractDefault - Flag to extract default values of parameters and schema attributes from the OpenAPI specification
 # + additionInfoFlags - Flags to extract additional information from the OpenAPI specification
 # + return - A record with the list of extracted tools and the service URL (if available)
-function extractToolsFromOpenApiJsonSpec(map<json> openApiSpec, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns ballerinax/ai.agent:0.9.2:HttpApiSpecification & readonly|Error;
+function extractToolsFromOpenApiJsonSpec(map<json> openApiSpec, boolean extractDescription = false, boolean extractDefault = false, AdditionInfoFlags additionInfoFlags) returns HttpApiSpecification & readonly|Error;
 
 # Parses the given OpenAPI specification as a JSON to a OpenApiSpec object.
 # 
@@ -2126,3 +2308,8 @@
 # + tools - Array of function pointers annotated with `@agent:Tool` annotation
 # + return - Array of `agent:ToolConfig` instances
 function getToolConfigs(FunctionTool[] tools) returns ToolConfig[];
+
+// --- Annotations ---
+
+# Represents the annotation of a function tool.
+public annotation ToolAnnotationConfig Tool on function, object function;
`````

# ai.openai — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.openai` |
| **Old file** | `ai.openai/old/ballerinax_ai.openai.bal.txt` |
| **New file** | `ai.openai/new/ballerinax_ai.openai.bal.txt` |
| **Old lines** | 370 |
| **New lines** | 393 |
| **Lines added** | 26 |
| **Lines removed** | 3 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 211–248 | 211–264 | Types | +16 | −0 |
| 2 | 259–264 | 275–281 | Types | +1 | −0 |
| 3 | 269–274 | 286–292 | Types | +1 | −0 |
| 4 | 333–338 | 351–357 | Types | +1 | −0 |
| 5 | 343–349 | 362–368 | Client | +1 | −1 |
| 6 | 357–363 | 376–382 | Client | +1 | −1 |
| 7 | 366–370 | 385–393 | Client | +5 | −1 |

---

## Unified diff

`````diff
--- ai.openai/old/ballerinax_ai.openai.bal.txt	2026-08-12 12:57:29
+++ ai.openai/new/ballerinax_ai.openai.bal.txt	2026-08-12 13:19:19
@@ -211,38 +211,54 @@
 
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
 
 # Defines which OpenAI API endpoint to use for model interactions.
+@display {label: "OpenAI API Type"}
 enum ApiType {
     RESPONSES,
     CHAT_COMPLETIONS
@@ -259,6 +275,7 @@
 # Note: the `max` effort accepted by the `gpt-5.6` family cannot be represented yet, because
 # `ballerinax/openai.chat` and `ballerinax/openai.responses` declare a closed `ReasoningEffort`
 # union without it. Add `MAX` here once those connectors are regenerated.
+@display {label: "Reasoning Effort"}
 enum ReasoningEffort {
     XHIGH,
     HIGH,
@@ -269,6 +286,7 @@
 }
 
 # Model types for OpenAI
+@display {label: "OpenAI Model Names"}
 enum OPEN_AI_MODEL_NAMES {
     CODEX_MINI_LATEST,
     COMPUTER_USE_PREVIEW,
@@ -333,6 +351,7 @@
     GPT_4O
 }
 
+@display {label: "OpenAI Embedding Model Names"}
 enum OPEN_AI_EMBEDDING_MODEL_NAMES {
     TEXT_EMBEDDING_ADA_002,
     TEXT_EMBEDDING_3_LARGE,
@@ -343,7 +362,7 @@
 
 # EmbeddingProvider provides an interface for interacting with OpenAI Embedding Models.
 client class EmbeddingProvider {
-    function init(string apiKey, OPEN_AI_EMBEDDING_MODEL_NAMES modelType, string serviceUrl = https://api.openai.com/v1, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Embedding Model Type"} OPEN_AI_EMBEDDING_MODEL_NAMES modelType, @display {label: "Service URL"} string serviceUrl = https://api.openai.com/v1, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Generates an embedding vector for the provided chunk.
     # 
@@ -357,7 +376,7 @@
 # ModelProvider is a client class that provides an interface for interacting with OpenAI Large Language Models.
 # Supports both the Chat Completions API (default) and the Responses API, selected via the `apiType` configuration.
 client class ModelProvider {
-    function init(string apiKey, OPEN_AI_MODEL_NAMES modelType, string serviceUrl = https://api.openai.com/v1, int maxTokens = 4096, decimal|() temperature = (), "xhigh"|"high"|"medium"|"low"|"minimal"|"none"|() reasoningEffort = (), ApiType apiType = CHAT_COMPLETIONS, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} OPEN_AI_MODEL_NAMES modelType, @display {label: "Service URL"} string serviceUrl = https://api.openai.com/v1, @display {label: "Maximum Tokens"} int maxTokens = 4096, @display {label: "Temperature"} decimal|() temperature = (), @display {label: "Reasoning Effort"} "xhigh"|"high"|"medium"|"low"|"minimal"|"none"|() reasoningEffort = (), @display {label: "API Type"} ApiType apiType = CHAT_COMPLETIONS, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the OpenAI model with the given messages and tools.
     # 
@@ -366,5 +385,9 @@
     # Sends a chat request to the model and generates a value that belongs to the type
     # corresponding to the type descriptor argument.
     # 
-    remote function generate(ai:Prompt prompt, anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
+    remote function generate(ai:Prompt prompt, @display {label: "Expected type"} anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
 }
+
+// --- Annotations ---
+
+public annotation map<json> JsonSchema on type;
`````

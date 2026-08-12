# ai.azure — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.azure` |
| **Old file** | `ai.azure/old/ballerinax_ai.azure.bal.txt` |
| **New file** | `ai.azure/new/ballerinax_ai.azure.bal.txt` |
| **Old lines** | 262 |
| **New lines** | 297 |
| **Lines added** | 39 |
| **Lines removed** | 4 |
| **Hunks** | 6 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (4)

- `class AiSearchKnowledgeBase`
- `function deleteByFilter`
- `function ingest`
- `function retrieve`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 152–185 | 152–200 | Types | +15 | −0 |
| 2 | 195–200 | 210–216 | Types | +1 | −0 |
| 3 | 215–222 | 231–253 | Types | +16 | −1 |
| 4 | 228–234 | 259–265 | Client | +1 | −1 |
| 5 | 249–255 | 280–286 | Client | +1 | −1 |
| 6 | 258–262 | 289–297 | Client | +5 | −1 |

---

## Unified diff

`````diff
--- ai.azure/old/ballerinax_ai.azure.bal.txt	2026-08-12 12:57:29
+++ ai.azure/new/ballerinax_ai.azure.bal.txt	2026-08-12 13:19:19
@@ -152,34 +152,49 @@
 
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
 
@@ -195,6 +210,7 @@
 # On the legacy surface `legacyBase` is the `serviceUrl` completed with `/openai` when it is a bare origin
 # (e.g. `https://<resource>.openai.azure.com`) and used verbatim when it already carries a path (e.g. an API
 # Management base path).
+@display {label: "OpenAI API Type"}
 enum ApiType {
     RESPONSES,
     CHAT_COMPLETIONS
@@ -215,8 +231,23 @@
     NONE
 }
 
-// Unknown type: AiSearchKnowledgeBase
+# Initializes a new `AiSearchKnowledgeBase` instance.
+# 
+class AiSearchKnowledgeBase {
+    function init(string serviceUrl, string apiKey, string|search:SearchIndex index, ai:EmbeddingProvider|() embeddingModel = (), ai:Chunker|"AUTO"|"DISABLE" chunker = AUTO, boolean verbose = false, string apiVersion = 2025-09-01, string contentFieldName = content, search:ConnectionConfig searchClientConnectionConfig = {}, index:ConnectionConfig indexClientConnectionConfig = {}, string|() semanticConfigurationName = ()) returns ai:Error?; // Special Agent Note: SearchIndex, ConnectionConfig FROM ballerinax/azure.ai.search package, EmbeddingProvider, Chunker FROM ballerina/ai package, ConnectionConfig FROM ballerinax/azure.ai.search.index package
 
+    # Ingests documents into the Azure search knowledge base.
+    function ingest(ai:Chunk[]|ai:ai:Document[]|ai:ai:Document documents) returns ai:Error|(); // Special Agent Note: Chunk, Document, Error FROM ballerina/ai package
+
+    # Retrieves relevant chunks for the given query using vector search.
+    # 
+    function retrieve(string query, int maxLimit = 0, ai:MetadataFilters|() filters = ()) returns ai:QueryMatch[]|ai:Error; // Special Agent Note: MetadataFilters, QueryMatch, Error FROM ballerina/ai package
+
+    # Deletes chunks that match the given metadata filters.
+    # 
+    function deleteByFilter(ai:MetadataFilters filters) returns ai:Error|(); // Special Agent Note: MetadataFilters, Error FROM ballerina/ai package
+}
+
 // --- Client ---
 
 # EmbeddingProvider provides an interface for interacting with Azure OpenAI Embedding Models.
@@ -228,7 +259,7 @@
 # `ballerinax/azure.openai.embeddings` connector, where `legacyBase` is the `serviceUrl` completed with `/openai`
 # when it is a bare origin and used verbatim when it already carries a path.
 client class EmbeddingProvider {
-    function init(string serviceUrl, string accessToken, string|() apiVersion, string deploymentId, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig config) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "Access Token"} string accessToken, @display {label: "API Version"} string|() apiVersion, @display {label: "Deployment ID"} string deploymentId, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "HTTP Configurations"} ConnectionConfig config) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Generates an embedding vector for the provided chunk.
     # 
@@ -249,7 +280,7 @@
 # **legacy** route (`?api-version=...`) through a raw HTTP client. See the `ApiType` documentation for the full
 # routing matrix.
 client class OpenAiModelProvider {
-    function init(string serviceUrl, string apiKey, string deploymentId, string|() apiVersion = (), int maxTokens = 4096, decimal|() temperature = (), "xhigh"|"high"|"medium"|"low"|"minimal"|"none"|() reasoningEffort = (), ApiType apiType = CHAT_COMPLETIONS, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Deployment ID"} string deploymentId, @display {label: "API Version"} string|() apiVersion = (), @display {label: "Maximum Tokens"} int maxTokens = 4096, @display {label: "Temperature"} decimal|() temperature = (), @display {label: "Reasoning Effort"} "xhigh"|"high"|"medium"|"low"|"minimal"|"none"|() reasoningEffort = (), @display {label: "API Type"} ApiType apiType = CHAT_COMPLETIONS, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the OpenAI model with the given messages and tools.
     # 
@@ -258,5 +289,9 @@
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

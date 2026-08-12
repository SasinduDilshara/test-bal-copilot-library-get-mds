# ai.googleapis.vertex — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.googleapis.vertex` |
| **Old file** | `ai.googleapis.vertex/old/ballerinax_ai.googleapis.vertex.bal.txt` |
| **New file** | `ai.googleapis.vertex/new/ballerinax_ai.googleapis.vertex.bal.txt` |
| **Old lines** | 257 |
| **New lines** | 277 |
| **Lines added** | 25 |
| **Lines removed** | 5 |
| **Hunks** | 6 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 5 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type ServiceAccountJsonFilePath`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 139–172 | 139–187 | Types | +15 | −0 |
| 2 | 192–198 | 207–216 | Types | +4 | −1 |
| 3 | 200–206 | 218–224 | Types | +1 | −1 |
| 4 | 213–220 | 231–239 | Client | +2 | −1 |
| 5 | 242–249 | 261–269 | Client | +2 | −1 |
| 6 | 253–257 | 273–277 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- ai.googleapis.vertex/old/ballerinax_ai.googleapis.vertex.bal.txt	2026-08-12 12:57:29
+++ ai.googleapis.vertex/new/ballerinax_ai.googleapis.vertex.bal.txt	2026-08-12 13:19:19
@@ -139,34 +139,49 @@
 
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
 
@@ -192,7 +207,10 @@
     string[] & readonly scopes?;
 };
 
-// Unknown type: ServiceAccountJsonFilePath
+# Path to a Google Cloud service account JSON key file.
+# The connector reads `client_email` and `private_key` from the file and refreshes
+# the token automatically. Use `ServiceAccountConfig` if you need to override scopes.
+type ServiceAccountJsonFilePath string;
 
 # Authentication configuration for Vertex AI.
 # - `OAuth2RefreshConfig` — OAuth2 refresh token flow. HTTP client auto-refreshes forever.
@@ -200,7 +218,7 @@
 # re-signed and exchanged automatically before expiry.
 # - `ServiceAccountJsonFilePath` — Path to a Google Cloud service account JSON key file.
 # Use `ServiceAccountConfig` instead if you need to override scopes.
-type VertexAiAuth ballerinax/ai.googleapis.vertex:1.0.2:OAuth2RefreshConfig|ballerinax/ai.googleapis.vertex:1.0.2:ServiceAccountConfig|ballerinax/ai.googleapis.vertex:1.0.2:ServiceAccountJsonFilePath;
+type VertexAiAuth OAuth2RefreshConfig|ServiceAccountConfig|ServiceAccountJsonFilePath;
 
 # Embedding model names supported by the Vertex AI embedding provider.
 enum VertexAiEmbeddingModelNames {
@@ -213,8 +231,9 @@
 
 # EmbeddingProvider is a client class that provides an interface for generating
 # vector embeddings using Google Vertex AI text embedding models.
+@display {label: "Google Vertex Embedding Provider"}
 client class EmbeddingProvider {
-    function init(VertexAiAuth auth, string projectId, string location = "global", VertexAiEmbeddingModelNames modelType = TEXT_EMBEDDING_005, string serviceUrl = "", http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Auth"} VertexAiAuth auth, @display {label: "Project ID"} string projectId, @display {label: "Location"} string location = "global", @display {label: "Model Type"} VertexAiEmbeddingModelNames modelType = TEXT_EMBEDDING_005, @display {label: "Service URL"} string serviceUrl = "", http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Converts the given chunk into a vector embedding.
     # 
@@ -242,8 +261,9 @@
 # - `"qwen/qwen3-235b-a22b"` — OpenAI-compatible open-models endpoint
 # - `"kimi/kimi-k2"` — OpenAI-compatible open-models endpoint
 # - `"minimax/minimax-m2"` — OpenAI-compatible open-models endpoint
+@display {label: "Google Vertex Model Provider"}
 client class ModelProvider {
-    function init(VertexAiAuth auth, string projectId, string model, string location = "global", string serviceUrl = "", int maxTokens = 512, decimal|() temperature = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Auth"} VertexAiAuth auth, @display {label: "Project ID"} string projectId, @display {label: "Model"} string model, @display {label: "Location"} string location = "global", @display {label: "Service URL"} string serviceUrl = "", @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal|() temperature = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the model. The request is routed to the correct
     # publisher-specific endpoint and serialised using the appropriate wire format.
@@ -253,5 +273,5 @@
     # Sends a prompt to the model and generates a value of the type specified by
     # the `td` type descriptor. Supports all publishers (Gemini, Anthropic, Mistral).
     # 
-    remote function generate(ai:Prompt prompt, anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
+    remote function generate(ai:Prompt prompt, @display {label: "Expected type"} anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
 }
`````

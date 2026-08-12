# ai.openrouter — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.openrouter` |
| **Old file** | `ai.openrouter/old/ballerinax_ai.openrouter.bal.txt` |
| **New file** | `ai.openrouter/new/ballerinax_ai.openrouter.bal.txt` |
| **Old lines** | 148 |
| **New lines** | 165 |
| **Lines added** | 20 |
| **Lines removed** | 3 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 82–115 | 82–130 | Types | +15 | −0 |
| 2 | 118–125 | 133–141 | Client | +2 | −1 |
| 3 | 133–140 | 149–157 | Client | +2 | −1 |
| 4 | 144–148 | 161–165 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- ai.openrouter/old/ballerinax_ai.openrouter.bal.txt	2026-08-12 12:57:29
+++ ai.openrouter/new/ballerinax_ai.openrouter.bal.txt	2026-08-12 13:19:19
@@ -82,34 +82,49 @@
 
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
 
@@ -118,8 +133,9 @@
 # EmbeddingProvider is a client class that provides an interface for generating
 # vector embeddings via the OpenRouter unified API, which supports embedding models
 # from OpenAI, Google, Mistral, and other providers.
+@display {label: "OpenRouter Embedding Provider"}
 client class EmbeddingProvider {
-    function init(string apiKey, string modelType, string serviceUrl = https://openrouter.ai/api/v1, string|() siteUrl = (), string|() siteName = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} string modelType, @display {label: "Service URL"} string serviceUrl = https://openrouter.ai/api/v1, @display {label: "Site URL"} string|() siteUrl = (), @display {label: "Site Name"} string|() siteName = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Converts the given chunk into a vector embedding.
     # 
@@ -133,8 +149,9 @@
 # ModelProvider is a client class that provides an interface for interacting with
 # LLMs via the OpenRouter unified API, which supports models from OpenAI, Anthropic,
 # Google, Meta, Mistral, and many other providers.
+@display {label: "OpenRouter Model Provider"}
 client class ModelProvider {
-    function init(string apiKey, string modelType, string serviceUrl = https://openrouter.ai/api/v1, string|() siteUrl = (), string|() siteName = (), int maxTokens = 512, decimal|() temperature = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} string modelType, @display {label: "Service URL"} string serviceUrl = https://openrouter.ai/api/v1, @display {label: "Site URL"} string|() siteUrl = (), @display {label: "Site Name"} string|() siteName = (), @display {label: "Maximum Tokens"} int maxTokens = 512, @display {label: "Temperature"} decimal|() temperature = (), http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the OpenRouter model with the given messages and tools.
     # 
@@ -144,5 +161,5 @@
     # the `td` type descriptor. For complex record types, annotate the type with
     # `@ai:JsonSchema` to enable compile-time schema generation.
     # 
-    remote function generate(ai:Prompt prompt, anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
+    remote function generate(ai:Prompt prompt, @display {label: "Expected type"} anydata td = anydata) returns td|ai:Error; // Special Agent Note: Prompt, Error FROM ballerina/ai package
 }
`````

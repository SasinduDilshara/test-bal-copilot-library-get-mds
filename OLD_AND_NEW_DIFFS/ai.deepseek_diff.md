# ai.deepseek — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.deepseek` |
| **Old file** | `ai.deepseek/old/ballerinax_ai.deepseek.bal.txt` |
| **New file** | `ai.deepseek/new/ballerinax_ai.deepseek.bal.txt` |
| **Old lines** | 125 |
| **New lines** | 144 |
| **Lines added** | 21 |
| **Lines removed** | 2 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 71–104 | 71–119 | Types | +15 | −0 |
| 2 | 112–118 | 127–133 | Client | +1 | −1 |
| 3 | 121–125 | 136–144 | Client | +5 | −1 |

---

## Unified diff

`````diff
--- ai.deepseek/old/ballerinax_ai.deepseek.bal.txt	2026-08-12 12:57:29
+++ ai.deepseek/new/ballerinax_ai.deepseek.bal.txt	2026-08-12 13:19:19
@@ -71,34 +71,49 @@
 
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
 
@@ -112,7 +127,7 @@
 
 # Deepseek is a client class that provides an interface for interacting with Deepseek Large Language Models.
 client class ModelProvider {
-    function init(string apiKey, DEEPSEEK_MODEL_NAMES modelType = DEEPSEEK_CHAT, string serviceUrl = https://api.deepseek.com, int maxTokens = 512, decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "API Key"} string apiKey, @display {label: "Model Type"} DEEPSEEK_MODEL_NAMES modelType = DEEPSEEK_CHAT, @display {label: "Service URL"} string serviceUrl = https://api.deepseek.com, @display {label: "Maximum Token"} int maxTokens = 512, @display {label: "Temperature"} decimal temperature = 0.7, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Generates a chat completion message from a Deepseek model
     # 
@@ -121,5 +136,9 @@
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

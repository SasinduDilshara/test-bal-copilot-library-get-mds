# ai.ollama — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.ollama` |
| **Old file** | `ai.ollama/old/ballerinax_ai.ollama.bal.txt` |
| **New file** | `ai.ollama/new/ballerinax_ai.ollama.bal.txt` |
| **Old lines** | 155 |
| **New lines** | 197 |
| **Lines added** | 44 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

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
| 1 | 60–148 | 60–186 | Types | +39 | −1 |
| 2 | 151–155 | 189–197 | Client | +5 | −1 |

---

## Unified diff

`````diff
--- ai.ollama/old/ballerinax_ai.ollama.bal.txt	2026-08-12 12:57:29
+++ ai.ollama/new/ballerinax_ai.ollama.bal.txt	2026-08-12 13:19:19
@@ -60,89 +60,127 @@
 
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
 
 // --- Client ---
 
 # Provider represents a client for interacting with an Ollama language models.
+@display {label: "Ollama Model Provider"}
 client class ModelProvider {
-    function init(string modelType, string serviceUrl = http://localhost:11434, 0|1|2 mirostat = 0, float mirostatEta = 0.1, float mirostatTau = 5.0, int numCtx = 2048, int repeatLastN = 64, float repeatPenalty = 1.1, float temperature = 0.8, int seed = 0, int numPredict = -1, int topK = 40, float topP = 0.9, float minP = 0.0, OllamaModelParameters modleParameters, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, ConnectionConfig connectionConfig) returns ballerina/ai:1.13.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
+    function init(@display {label: "Model Type"} string modelType, @display {label: "Service URL"} string serviceUrl = http://localhost:11434, 0|1|2 mirostat = 0, float mirostatEta = 0.1, float mirostatTau = 5.0, int numCtx = 2048, int repeatLastN = 64, float repeatPenalty = 1.1, float temperature = 0.8, int seed = 0, int numPredict = -1, int topK = 40, float topP = 0.9, float minP = 0.0, @display {label: "Ollama Model Parameters"} OllamaModelParameters modleParameters, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, string forwarded = "disable", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = AUTO, http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = true, @display {label: "Connection Configuration"} ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package
 
     # Sends a chat request to the Ollama model with the given messages and tools.
     # 
@@ -151,5 +189,9 @@
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

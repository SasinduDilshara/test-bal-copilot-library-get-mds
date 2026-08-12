# ai.devant — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.devant` |
| **Old file** | `ai.devant/old/ballerinax_ai.devant.bal.txt` |
| **New file** | `ai.devant/new/ballerinax_ai.devant.bal.txt` |
| **Old lines** | 79 |
| **New lines** | 94 |
| **Lines added** | 18 |
| **Lines removed** | 3 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 3 | 3 |

### Declarations added (6)

- `class BinaryDataLoader`
- `class Chunker`
- `function chunk`
- `function init`
- `function load`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 64–70 | 64–71 | Types | +2 | −1 |
| 2 | 74–79 | 75–94 | Types | +16 | −2 |

---

## Unified diff

`````diff
--- ai.devant/old/ballerinax_ai.devant.bal.txt	2026-08-12 12:57:29
+++ ai.devant/new/ballerinax_ai.devant.bal.txt	2026-08-12 13:19:19
@@ -64,7 +64,8 @@
 # Split the text into character-level chunks.
 const string CHARACTER = "character";
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Specifies the strategy to split text into chunks.
 enum ChunkStrategy {
@@ -74,6 +75,20 @@
     RECURSIVE
 }
 
-// Unknown type: Chunker
+# Initializes a new `Chunker` instance.
+# 
+class Chunker {
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "Access Token"} string accessToken, @display {label: "Maximum Chunk Size in Characters"} int maxChunkSize = 500, @display {label: "Maximum Overlap Size in Characters"} int maxOverlapSize = 50, @display {label: "Chunking Strategy"} ChunkStrategy strategy = RECURSIVE, http:HttpVersion httpVersion = "2.0", http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", http:PoolConfiguration poolConfig = {}, http:CacheConfig cache = {}, http:Compression compression = "AUTO", http:CircuitBreakerConfig circuitBreaker = {}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:ProxyConfig proxy = {}, boolean validation = false, @display {label: "Connection Configuration"} ai:ConnectionConfig connectionConfig) returns ai:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, CacheConfig, Compression, CircuitBreakerConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, ProxyConfig FROM ballerina/http package, ConnectionConfig FROM ballerina/ai package
 
-// Unknown type: BinaryDataLoader
+    # Chunks the provided document.
+    function chunk(ai:Document document) returns ai:Chunk[]|ai:Error; // Special Agent Note: Document, Chunk, Error FROM ballerina/ai package
+}
+
+# Creates a new `BinaryDataLoader` instance.
+class BinaryDataLoader {
+    function init(string path) returns ai:Error?;
+
+    # Loads documents from the specified path.
+    # 
+    function load() returns ai:Document[]|ai:Document|ai:Error; // Special Agent Note: Document, Error FROM ballerina/ai package
+}
`````

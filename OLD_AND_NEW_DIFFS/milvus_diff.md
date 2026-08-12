# milvus — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `milvus` |
| **Old file** | `milvus/old/ballerinax_milvus.bal.txt` |
| **New file** | `milvus/new/ballerinax_milvus.bal.txt` |
| **Old lines** | 342 |
| **New lines** | 343 |
| **Lines added** | 3 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 120–126 | 120–127 | END README | +2 | −1 |
| 2 | 306–312 | 307–313 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- milvus/old/ballerinax_milvus.bal.txt	2026-08-12 12:57:30
+++ milvus/new/ballerinax_milvus.bal.txt	2026-08-12 13:19:19
@@ -120,7 +120,8 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents any error related to Ballerina Milvus connector.
+type Error error;
 
 # Represents the configuration for the Milvus connection.
 
@@ -306,7 +307,7 @@
 # Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search.
 # 
 client class Client {
-    function init(string serviceUrl, AuthConfig authConfig = {token: ""}, CredentialsConfig credentialsConfig = {username: "", password: ""}, int idleTimeout = 0, int keepAliveTime = 55, int keepAliveTimeout = 20, boolean keepAliveWithoutCalls = false, int rpcDeadline = 0, int connectTimeout = 10, string databaseName = "", string serverName = "", string proxyAddress = "", SecureConfig secureConfig = {clientKeyPath: "", clientPemPath: "", serverPemPath: "", caPemPath: ""}, anydata Additional Values, ConnectionConfig config) returns ballerinax/milvus:1.1.1:Error?;
+    function init(string serviceUrl, AuthConfig authConfig = {token: ""}, CredentialsConfig credentialsConfig = {username: "", password: ""}, int idleTimeout = 0, int keepAliveTime = 55, int keepAliveTimeout = 20, boolean keepAliveWithoutCalls = false, int rpcDeadline = 0, int connectTimeout = 10, string databaseName = "", string serverName = "", string proxyAddress = "", SecureConfig secureConfig = {clientKeyPath: "", clientPemPath: "", serverPemPath: "", caPemPath: ""}, ConnectionConfig config) returns Error?;
 
     # Lists all the collections in the Milvus vector database.
     # 
`````

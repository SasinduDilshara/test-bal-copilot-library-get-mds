# ibm.ctg — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ibm.ctg` |
| **Old file** | `ibm.ctg/old/ballerinax_ibm.ctg.bal.txt` |
| **New file** | `ibm.ctg/new/ballerinax_ibm.ctg.bal.txt` |
| **Old lines** | 253 |
| **New lines** | 254 |
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
| 1 | 176–182 | 176–183 | END README | +2 | −1 |
| 2 | 234–240 | 235–241 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- ibm.ctg/old/ballerinax_ibm.ctg.bal.txt	2026-08-12 12:57:30
+++ ibm.ctg/new/ballerinax_ibm.ctg.bal.txt	2026-08-12 13:19:19
@@ -176,7 +176,8 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents a IBM CTG distinct error.
+type Error error;
 
 # Represents the Client configurations for IBM CTG client.
 
@@ -234,7 +235,7 @@
 
 # IBM CTG client.
 client class Client {
-    function init(string host = "", int port = 0, string cicsServer = "", int socketConnectTimeout = 15, Auth auth = {userId: "", password: ""}, SecureSocket secureSocket = {sslKeyring: ""}, boolean enableTrace = false, ConnectionConfig configs) returns ballerinax/ibm.ctg:0.1.1:Error?;
+    function init(string host = "", int port = 0, string cicsServer = "", int socketConnectTimeout = 15, Auth auth = {userId: "", password: ""}, SecureSocket secureSocket = {sslKeyring: ""}, boolean enableTrace = false, ConnectionConfig configs) returns Error?;
 
     # Executes the specified CICS transaction gateway request and retrieves the results.
     # ```ballerina
`````

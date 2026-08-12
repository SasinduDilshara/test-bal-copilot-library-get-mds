# wso2.apim.catalog — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `wso2.apim.catalog` |
| **Old file** | `wso2.apim.catalog/old/ballerinax_wso2.apim.catalog.bal.txt` |
| **New file** | `wso2.apim.catalog/new/ballerinax_wso2.apim.catalog.bal.txt` |
| **Old lines** | 449 |
| **New lines** | 473 |
| **Lines added** | 25 |
| **Lines removed** | 1 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (8)

- `annotation ServiceCatalogConfig`
- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function init`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 82–87 | 82–88 | Types | +1 | −0 |
| 2 | 154–159 | 155–161 | Types | +1 | −0 |
| 3 | 167–172 | 169–175 | Types | +1 | −0 |
| 4 | 182–190 | 185–197 | Types | +4 | −0 |
| 5 | 255–260 | 262–268 | Types | +1 | −0 |
| 6 | 328–335 | 336–355 | Types | +13 | −1 |
| 7 | 447–449 | 467–473 | Client | +4 | −0 |

---

## Unified diff

`````diff
--- wso2.apim.catalog/old/ballerinax_wso2.apim.catalog.bal.txt	2026-08-12 12:57:30
+++ wso2.apim.catalog/new/ballerinax_wso2.apim.catalog.bal.txt	2026-08-12 13:19:20
@@ -82,6 +82,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2PasswordGrantConfig auth;
@@ -154,6 +155,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -167,6 +169,7 @@
 
 type ServiceInfo record {
     string id?;
+    @constraint:String {pattern: re `^[^\*]+$`}
     string name?;
     string 'key?;
     string version?;
@@ -182,9 +185,13 @@
 
 type Service record {
     string id?;
+    @constraint:String {maxLength: 255, minLength: 1, pattern: re `^[^\*]+$`}
     string name;
+    @constraint:String {maxLength: 1024}
     string description?;
+    @constraint:String {maxLength: 30, minLength: 1}
     string version;
+    @constraint:String {maxLength: 512}
     string serviceKey?;
     string serviceUrl;
     # The type of the provided API definition
@@ -255,6 +262,7 @@
 
 
 type Verifier record {
+    @constraint:String {pattern: re `^[^\*]+$`}
     string 'key;
     string md5;
 };
@@ -328,8 +336,20 @@
     BASIC
 }
 
-// Unknown type: Listener
+class Listener {
+    function init(int port) returns ();
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
 
+    function immediateStop() returns error?;
+
+    function detach(service object {} s) returns error?;
+
+    function attach(service object {} s, string[]|() name = ()) returns error?;
+}
+
 // --- Client ---
 
 # This specifies a **RESTful API** for Service Catalog.
@@ -447,3 +467,7 @@
     # 
     resource function get settings() returns Settings|error;
 }
+
+// --- Annotations ---
+
+public annotation ServiceCatalogMetaData ServiceCatalogConfig on service;
`````

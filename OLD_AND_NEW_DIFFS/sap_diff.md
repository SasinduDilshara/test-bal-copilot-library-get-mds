# sap — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap` |
| **Old file** | `sap/old/ballerinax_sap.bal.txt` |
| **New file** | `sap/new/ballerinax_sap.bal.txt` |
| **Old lines** | 207 |
| **New lines** | 209 |
| **Lines added** | 13 |
| **Lines removed** | 11 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type CSRFTokenFetchFailure`
- `type ClientError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 135–157 | 135–159 | END README | +7 | −5 |
| 2 | 159–165 | 161–167 | Client | +1 | −1 |
| 3 | 167–173 | 169–175 | Client | +1 | −1 |
| 4 | 175–181 | 177–183 | Client | +1 | −1 |
| 5 | 183–189 | 185–191 | Client | +1 | −1 |
| 6 | 191–197 | 193–199 | Client | +1 | −1 |
| 7 | 199–205 | 201–207 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- sap/old/ballerinax_sap.bal.txt	2026-08-12 12:57:30
+++ sap/new/ballerinax_sap.bal.txt	2026-08-12 13:19:19
@@ -135,23 +135,25 @@
 
 // --- Types ---
 
-// Unknown type: ClientError
+# Defines the possible client error types.
+type ClientError http:ClientError;
 
-// Unknown type: CSRFTokenFetchFailure
+# Represents an error, which occured due to a CSRF token fetch failure.
+type CSRFTokenFetchFailure http:ClientError;
 
 # The `sap` client return type for the HTTP client actions.
-type TargetType ballerina/http:2.16.6:Response|anydata;
+type TargetType http:Response|anydata;
 
 // --- Client ---
 
 # The `sap` client provides the capability for initiating contact with a remote HTTP service provided by any SAP products. The API it
 # provides includes the functions for the standard HTTP methods.
 client class Client {
-    function init(string url, http:ClientConfiguration config) returns ballerinax/sap:1.3.1:ClientError?; // Special Agent Note: ClientConfiguration FROM ballerina/http package
+    function init(string url, http:ClientConfiguration config) returns ClientError?; // Special Agent Note: ClientConfiguration FROM ballerina/http package
 
     # The client resource function to send HTTP POST requests to SAP HTTP endpoints.
     # 
-    resource function post [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParamType, QueryParams FROM ballerina/http package
+    resource function post [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParams FROM ballerina/http package
 
     # The `Client.post()` function can be used to send HTTP POST requests to SAP HTTP endpoints.
     # 
@@ -159,7 +161,7 @@
 
     # The client resource function to send HTTP PUT requests to SAP HTTP endpoints.
     # 
-    resource function put [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParamType, QueryParams FROM ballerina/http package
+    resource function put [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParams FROM ballerina/http package
 
     # The `Client.put()` function can be used to send HTTP PUT requests to SAP HTTP endpoints.
     # 
@@ -167,7 +169,7 @@
 
     # The client resource function to send HTTP PATCH requests to SAP HTTP endpoints.
     # 
-    resource function patch [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParamType, QueryParams FROM ballerina/http package
+    resource function patch [... path](http:RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParams FROM ballerina/http package
 
     # The `Client.patch()` function can be used to send HTTP PATCH requests to SAP HTTP endpoints.
     # 
@@ -175,7 +177,7 @@
 
     # The client resource function to send HTTP DELETE requests to SAP HTTP endpoints.
     # 
-    resource function delete [... path](http:RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParamType, QueryParams FROM ballerina/http package
+    resource function delete [... path](http:RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: RequestMessage, QueryParams FROM ballerina/http package
 
     # The `Client.delete()` function can be used to send HTTP DELETE requests to SAP HTTP endpoints.
     # 
@@ -183,7 +185,7 @@
 
     # The client resource function to send HTTP HEAD requests to SAP HTTP endpoints.
     # 
-    resource function head [... path](map<string|string[]>|() headers = (), http:QueryParamType Additional Values, http:QueryParams params) returns http:Response|ClientError; // Special Agent Note: QueryParamType, QueryParams, Response FROM ballerina/http package
+    resource function head [... path](map<string|string[]>|() headers = (), http:QueryParams params) returns http:Response|ClientError; // Special Agent Note: QueryParams, Response FROM ballerina/http package
 
     # The `Client.head()` function can be used to send HTTP HEAD requests to SAP HTTP endpoints.
     # 
@@ -191,7 +193,7 @@
 
     # The client resource function to send HTTP GET requests to SAP HTTP endpoints.
     # 
-    resource function get [... path](map<string|string[]>|() headers = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: QueryParamType, QueryParams FROM ballerina/http package
+    resource function get [... path](map<string|string[]>|() headers = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: QueryParams FROM ballerina/http package
 
     # The `Client.get()` function can be used to send HTTP GET requests to SAP HTTP endpoints.
     # 
@@ -199,7 +201,7 @@
 
     # The client resource function to send HTTP OPTIONS requests to SAP HTTP endpoints.
     # 
-    resource function options [... path](map<string|string[]>|() headers = (), TargetType targetType = sap:TargetType, http:QueryParamType Additional Values, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: QueryParamType, QueryParams FROM ballerina/http package
+    resource function options [... path](map<string|string[]>|() headers = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType|ClientError; // Special Agent Note: QueryParams FROM ballerina/http package
 
     # The `Client.options()` function can be used to send HTTP OPTIONS requests to SAP HTTP endpoints.
     # 
`````

# snowflake — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `snowflake` |
| **Old file** | `snowflake/old/ballerinax_snowflake.bal.txt` |
| **New file** | `snowflake/new/ballerinax_snowflake.bal.txt` |
| **Old lines** | 288 |
| **New lines** | 290 |
| **Lines added** | 9 |
| **Lines removed** | 7 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 215–232 | 215–233 | Types | +4 | −3 |
| 2 | 250–266 | 251–268 | Client | +4 | −3 |
| 3 | 284–288 | 286–290 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- snowflake/old/ballerinax_snowflake.bal.txt	2026-08-12 12:57:30
+++ snowflake/new/ballerinax_snowflake.bal.txt	2026-08-12 13:19:19
@@ -215,18 +215,19 @@
 };
 
 # Represents the authentication configuration for the Snowflake client.
-type AuthConfig ballerinax/snowflake:2.2.2:BasicAuth|ballerinax/snowflake:2.2.2:KeyBasedAuth;
+type AuthConfig BasicAuth|KeyBasedAuth;
 
 // --- Client ---
 
 # Represents a Snowflake database client.
+@display {label: "Snowflake", iconPath: "icon.png"}
 client class AdvancedClient {
-    function init(string accountIdentifier, AuthConfig authConfig, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string accountIdentifier, AuthConfig authConfig, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes the query, which may return multiple results.
     # When processing the stream, make sure to consume all fetched data or close the stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes the query, which is expected to return at most one row of the result.
     # If the query does not return any results, `sql:NoRowsError` is returned.
@@ -250,17 +251,18 @@
 
     # Closes the SQL client and shuts down the connection pool.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
 
 # Represents a Snowflake database client.
+@display {label: "Snowflake", iconPath: "icon.png"}
 client class Client {
-    function init(string account_identifier, string user, string password, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string account_identifier, string user, string password, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes the query, which may return multiple results.
     # When processing the stream, make sure to consume all fetched data or close the stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes the query, which is expected to return at most one row of the result.
     # If the query does not return any results, `sql:NoRowsError` is returned.
@@ -284,5 +286,5 @@
 
     # Closes the SQL client and shuts down the connection pool.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
`````

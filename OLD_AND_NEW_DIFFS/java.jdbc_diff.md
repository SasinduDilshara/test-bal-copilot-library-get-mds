# java.jdbc — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `java.jdbc` |
| **Old file** | `java.jdbc/old/ballerinax_java.jdbc.bal.txt` |
| **New file** | `java.jdbc/new/ballerinax_java.jdbc.bal.txt` |
| **Old lines** | 545 |
| **New lines** | 545 |
| **Lines added** | 3 |
| **Lines removed** | 3 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 511–522 | 511–522 | Client | +2 | −2 |
| 2 | 541–545 | 541–545 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- java.jdbc/old/ballerinax_java.jdbc.bal.txt	2026-08-12 12:57:30
+++ java.jdbc/new/ballerinax_java.jdbc.bal.txt	2026-08-12 13:19:19
@@ -511,12 +511,12 @@
 
 # Represents a JDBC client.
 client class Client {
-    function init(string url, string|() user = (), string|() password = (), Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string url, string|() user = (), string|() password = (), Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes the query, which may return multiple results.
     # When processing the stream, make sure to consume all fetched data or close the stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes the query, which is expected to return at most one row of the result.
     # If the query does not return any results, an `sql:NoRowsError` is returned.
@@ -541,5 +541,5 @@
     # Closes the JDBC client and shuts down the connection pool. The client must be closed only at the end of the
     # application lifetime (or closed for graceful stops in a service).
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
`````

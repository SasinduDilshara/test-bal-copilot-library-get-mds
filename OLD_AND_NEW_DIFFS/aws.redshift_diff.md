# aws.redshift — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.redshift` |
| **Old file** | `aws.redshift/old/ballerinax_aws.redshift.bal.txt` |
| **New file** | `aws.redshift/new/ballerinax_aws.redshift.bal.txt` |
| **Old lines** | 199 |
| **New lines** | 200 |
| **Lines added** | 4 |
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
| 1 | 166–177 | 166–178 | Types | +3 | −2 |
| 2 | 195–199 | 196–200 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.redshift/old/ballerinax_aws.redshift.bal.txt	2026-08-12 12:57:30
+++ aws.redshift/new/ballerinax_aws.redshift.bal.txt	2026-08-12 13:19:19
@@ -166,12 +166,13 @@
 
 // --- Client ---
 
+@display {label: "Redshift", iconPath: "icon.png"}
 client class Client {
-    function init(string url, string user, string password, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string url, string user, string password, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Queries the database with the provided query and returns the result as a stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes the query, which is expected to return at most one row of the result. 
     # If the query does not return any results, an sql:NoRowsError is returned.
@@ -195,5 +196,5 @@
 
     # Closes the client and shuts down the connection pool.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
`````

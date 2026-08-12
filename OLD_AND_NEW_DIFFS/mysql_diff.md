# mysql — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mysql` |
| **Old file** | `mysql/old/ballerinax_mysql.bal.txt` |
| **New file** | `mysql/new/ballerinax_mysql.bal.txt` |
| **Old lines** | 886 |
| **New lines** | 934 |
| **Lines added** | 54 |
| **Lines removed** | 6 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (9)

- `class CdcListener`
- `class CustomResultIterator`
- `function 'start`
- `function attach`
- `function detach`
- `function getNextQueryResult`
- `function gracefulStop`
- `function immediateStop`
- `function nextResult`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 828–846 | 828–876 | Types | +34 | −4 |
| 2 | 863–886 | 893–934 | Client | +20 | −2 |

---

## Unified diff

`````diff
--- mysql/old/ballerinax_mysql.bal.txt	2026-08-12 12:57:30
+++ mysql/new/ballerinax_mysql.bal.txt	2026-08-12 13:19:19
@@ -828,19 +828,49 @@
     cdc:TimePrecisionMode timePrecisionMode?; // Special Agent Note: TimePrecisionMode FROM ballerinax/cdc package
 };
 
-// Unknown type: CdcListener
+# Initializes the MySQL listener with the given configuration.
+# 
+class CdcListener {
+    function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {}, cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d, MySqlDatabaseConnection database = {username: "", password: ""}, MySqlOptions options = {}, MySqlListenerConfiguration config) returns (); // Special Agent Note: InternalSchemaStorage, OffsetStorage FROM ballerinax/cdc package
 
-// Unknown type: CustomResultIterator
+    # Attaches a CDC service to the MySQL listener.
+    # 
+    function attach(cdc:Service s, string[]|string|() name = ()) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
+
+    # Starts the MySQL listener.
+    # 
+    function 'start() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+
+    # Detaches a CDC service from the MySQL listener.
+    # 
+    function detach(cdc:Service s) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
+
+    # Stops the MySQL listener gracefully.
+    # 
+    function gracefulStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+
+    # Stops the MySQL listener immediately.
+    # 
+    function immediateStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+}
+
+# The iterator for the stream returned in `query` function to be used to override the default behaviour of `sql:ResultIterator`.
+class CustomResultIterator {
+
+    function nextResult(sql:ResultIterator iterator) returns record {|anydata...;|}|sql:Error|(); // Special Agent Note: ResultIterator, Error FROM ballerina/sql package
+
+    function getNextQueryResult(sql:ProcedureCallResult callResult) returns boolean|sql:Error; // Special Agent Note: ProcedureCallResult, Error FROM ballerina/sql package
+}
 
 // --- Client ---
 
 # MySQL database client that enables interaction with MySQL servers and supports standard SQL operations.
 client class Client {
-    function init(string host = "localhost", string|() user = "root", string|() password = (), string|() database = (), int port = 3306, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string host = "localhost", string|() user = "root", string|() password = (), string|() database = (), int port = 3306, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes a SQL query and returns multiple results as a stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes a SQL query that is expected to return a single row or value as the result.
     # If the query returns no results, `sql:NoRowsError` is returned.
@@ -863,24 +893,42 @@
     # Closes the MySQL client and shuts down the connection pool.
     # The client should be closed only at the end of the application lifetime, or when performing graceful stops in a service.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
 
 // --- Service ---
 
-service mysql:Service on new mysql:CdcListener(MySqlListenerConfiguration config = {database: {username: "", password: ""}}) {
+service mysql:Service on new mysql:CdcListener(mysql:MySqlListenerConfiguration config = {database: {username: "", password: ""}}) {
     # Triggers initially to read existing records from the monitored table
+    # + afterEntry - The existing record from the monitored table
+    # + tableName - The name of the table where the record was created
+    # Required parameters: afterEntry
+    # Optional parameters (may be omitted): tableName
     remote function onRead(record {} afterEntry, string tableName) returns error?;
 
     # Triggers when a new record is created in the monitored table
+    # + afterEntry - The new record created in the monitored table
+    # + tableName - The name of the table where the record was created
+    # Required parameters: afterEntry
+    # Optional parameters (may be omitted): tableName
     remote function onCreate(record {} afterEntry, string tableName) returns error?;
 
     # Triggers when an existing record is updated in the monitored table
+    # + beforeEntry - The record before the update in the monitored table
+    # + afterEntry - The record after the update in the monitored table
+    # + tableName - The name of the table where the record was created
+    # Required parameters: beforeEntry, afterEntry
+    # Optional parameters (may be omitted): tableName
     remote function onUpdate(record {} beforeEntry, record {} afterEntry, string tableName) returns error?;
 
     # Triggers when a record is deleted from the monitored table
+    # + beforeEntry - The record before the deletion in the monitored table
+    # + tableName - The name of the table where the record was created
+    # Required parameters: beforeEntry
+    # Optional parameters (may be omitted): tableName
     remote function onDelete(record {} beforeEntry, string tableName) returns error?;
 
     # Triggers when an error occurs during event processing before mandatory functions are invoked
+    # + cdcError - The error occurred during message processing
     remote function onError(cdc:Error cdcError);
 }
`````

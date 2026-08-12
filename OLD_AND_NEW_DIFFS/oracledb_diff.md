# oracledb — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `oracledb` |
| **Old file** | `oracledb/old/ballerinax_oracledb.bal.txt` |
| **New file** | `oracledb/new/ballerinax_oracledb.bal.txt` |
| **Old lines** | 1091 |
| **New lines** | 1151 |
| **Lines added** | 79 |
| **Lines removed** | 19 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 9 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 8 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (17)

- `class CdcListener`
- `class CustomResultIterator`
- `class IntervalDayToSecondOutParameter`
- `class IntervalYearToMonthOutParameter`
- `class NestedTableValue`
- `class ObjectOutParameter`
- `class ObjectTypeValue`
- `class VarrayValue`
- `class XmlOutParameter`
- `function 'start`
- `function attach`
- `function detach`
- `function get`
- `function getNextQueryResult`
- `function gracefulStop`
- `function immediateStop`
- `function nextResult`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 962–970 | 962–970 | Types | +2 | −2 |
| 2 | 974–984 | 974–984 | Types | +3 | −3 |
| 3 | 1000–1006 | 1000–1006 | Types | +1 | −1 |
| 4 | 1010–1046 | 1010–1106 | Types | +72 | −12 |
| 5 | 1087–1091 | 1147–1151 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- oracledb/old/ballerinax_oracledb.bal.txt	2026-08-12 12:57:30
+++ oracledb/new/ballerinax_oracledb.bal.txt	2026-08-12 13:19:19
@@ -962,9 +962,9 @@
     # Sign of the interval value
     Sign sign?;
     # Number of years
-    ballerina/lang.int:0.0.0:Unsigned32 years?;
+    int:Unsigned32 years?;
     # Number of months
-    ballerina/lang.int:0.0.0:Unsigned32 months?;
+    int:Unsigned32 months?;
 };
 
 # Represents a period of time in days, hours, minutes, and seconds.
@@ -974,11 +974,11 @@
     # Sign of the interval value
     Sign sign?;
     # Number of days
-    ballerina/lang.int:0.0.0:Unsigned32 days?;
+    int:Unsigned32 days?;
     # Number of hours
-    ballerina/lang.int:0.0.0:Unsigned32 hours?;
+    int:Unsigned32 hours?;
     # Number of minutes
-    ballerina/lang.int:0.0.0:Unsigned32 minutes?;
+    int:Unsigned32 minutes?;
     # Number of seconds
     decimal seconds?;
 };
@@ -1000,7 +1000,7 @@
     # Name of the varray
     string name;
     # Elements of the Varray
-    ballerinax/oracledb:1.17.0:ArrayValueType? elements;
+    ArrayValueType? elements;
 };
 
 # Represents an ordered set of data elements with a variable size.
@@ -1010,37 +1010,97 @@
     # Name of the varray
     string name;
     # Elements of the Varray
-    ballerinax/oracledb:1.17.0:ArrayValueType? elements;
+    ArrayValueType? elements;
 };
 
-// Unknown type: CdcListener
+# Initializes the Oracle listener with the given configuration.
+# 
+class CdcListener {
+    function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {}, cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d, OracleDatabaseConnection database = {databaseName: "", username: "", password: ""}, OracleOptions options = {}, OracleListenerConfiguration config) returns cdc:Error?; // Special Agent Note: InternalSchemaStorage, OffsetStorage FROM ballerinax/cdc package
 
-// Unknown type: ObjectTypeValue
+    # Attaches a CDC service to the Oracle listener.
+    # 
+    function attach(cdc:Service s, string[]|string|() name = ()) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
 
-// Unknown type: VarrayValue
+    # Starts the Oracle listener.
+    # 
+    function 'start() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
 
-// Unknown type: NestedTableValue
+    # Detaches a CDC service from the Oracle listener.
+    # 
+    function detach(cdc:Service s) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
 
-// Unknown type: ObjectOutParameter
+    # Stops the Oracle listener gracefully.
+    # 
+    function gracefulStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
 
-// Unknown type: XmlOutParameter
+    # Stops the Oracle listener immediately.
+    # 
+    function immediateStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+}
 
-// Unknown type: IntervalYearToMonthOutParameter
+class ObjectTypeValue {
+    function init(ObjectType|() value = ()) returns ();
+}
 
-// Unknown type: IntervalDayToSecondOutParameter
+class VarrayValue {
+    function init(Varray|() value = ()) returns ();
+}
 
-// Unknown type: CustomResultIterator
+class NestedTableValue {
+    function init(NestedTableType|() value = ()) returns ();
+}
 
+class ObjectOutParameter {
+    function init(string typeName) returns ();
+
+    # Parses the returned Oracle OBJECT SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
+
+# Represents the `XML range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class XmlOutParameter {
+
+    # Parses the returned `Xml` SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
+
+# Represents the `IntervalYearToMonth` `OutParameter` in `sql:ParameterizedCallQuery`.
+class IntervalYearToMonthOutParameter {
+
+    # Parses the returned `IntervalYearToMonthOutParameter` SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
+
+# Represents the `IntervalDayToSecond` `OutParameter` in `sql:ParameterizedCallQuery`.
+class IntervalDayToSecondOutParameter {
+
+    # Parses the returned `IntervalDayToSecondOutParameter` SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
+
+# The iterator for the stream returned from the `query` function to be used to override the default behaviour of `sql:ResultIterator`.
+class CustomResultIterator {
+
+    function nextResult(sql:ResultIterator iterator) returns record {|anydata...;|}|sql:Error|(); // Special Agent Note: ResultIterator, Error FROM ballerina/sql package
+
+    function getNextQueryResult(sql:ProcedureCallResult callResult) returns boolean|sql:Error; // Special Agent Note: ProcedureCallResult, Error FROM ballerina/sql package
+}
+
 // --- Client ---
 
 # Represents a OracleDB client.
 client class Client {
-    function init(string host = "localhost", string|() user = "sys", string|() password = (), string|() database = (), int port = 1521, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string host = "localhost", string|() user = "sys", string|() password = (), string|() database = (), int port = 1521, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes the query, which may return multiple results.
     # When processing the stream, make sure to consume all fetched data or close the stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes the query, which is expected to return at most one row of the result.
     # If the query does not return any results, an `sql:NoRowsError` is returned.
@@ -1087,5 +1147,5 @@
     # Closes the JDBC client and shuts down the connection pool. The client must be closed only at the end of the
     # application lifetime (or closed for graceful stops in a service).
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
`````

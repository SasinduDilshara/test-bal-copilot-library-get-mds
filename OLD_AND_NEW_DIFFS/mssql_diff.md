# mssql — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mssql` |
| **Old file** | `mssql/old/ballerinax_mssql.bal.txt` |
| **New file** | `mssql/new/ballerinax_mssql.bal.txt` |
| **Old lines** | 837 |
| **New lines** | 899 |
| **Lines added** | 94 |
| **Lines removed** | 32 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 13 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 15 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (18)

- `class CdcListener`
- `class CircularStringValue`
- `class CompoundCurveValue`
- `class CurvePolygonValue`
- `class GeometryCollectionValue`
- `class LineStringValue`
- `class MoneyValue`
- `class MultiLineStringValue`
- `class MultiPointValue`
- `class MultiPolygonValue`
- `class PointValue`
- `class PolygonValue`
- `class SmallMoneyValue`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 620–654 | 620–672 | Types | +32 | −14 |
| 2 | 773–795 | 791–843 | Types | +36 | −6 |
| 3 | 814–837 | 862–899 | Client | +26 | −12 |

---

## Unified diff

`````diff
--- mssql/old/ballerinax_mssql.bal.txt	2026-08-12 12:57:30
+++ mssql/new/ballerinax_mssql.bal.txt	2026-08-12 13:19:19
@@ -620,35 +620,53 @@
     decimal y;
 };
 
-// Unknown type: LineStringValue
+class LineStringValue {
+    function init(Point[]|string|() value = (), int|() srid = ()) returns ();
+}
 
-// Unknown type: CircularStringValue
+class CircularStringValue {
+    function init(Point[]|string|() value = (), int|() srid = ()) returns ();
+}
 
 # Represents an element (LineString or Circular String) of a MSSQL Compound Curve type.
 # 
-type CompoundCurveElement ballerinax/mssql:1.19.0:LineStringValue|ballerinax/mssql:1.19.0:CircularStringValue;
+type CompoundCurveElement LineStringValue|CircularStringValue;
 
-// Unknown type: CompoundCurveValue
+class CompoundCurveValue {
+    function init(CompoundCurveElement[]|string|() value = (), int|() srid = ()) returns ();
+}
 
 # Represents the MSSQL circular arc ring (LineString, Circular String or Compound Curve) type.
 # 
-type CircularArcRing ballerinax/mssql:1.19.0:LineStringValue|ballerinax/mssql:1.19.0:CircularStringValue|ballerinax/mssql:1.19.0:CompoundCurveValue;
+type CircularArcRing LineStringValue|CircularStringValue|CompoundCurveValue;
 
-// Unknown type: PointValue
-
-// Unknown type: PolygonValue
-
-// Unknown type: CurvePolygonValue
+class PointValue {
+    function init(Point|string|() value = (), int|() srid = ()) returns ();
+}
 
-// Unknown type: MultiPointValue
+class PolygonValue {
+    function init(LineStringValue[]|string|() value = (), int|() srid = ()) returns ();
+}
 
-// Unknown type: MultiLineStringValue
+class CurvePolygonValue {
+    function init(CircularArcRing[]|string|() value = (), int|() srid = ()) returns ();
+}
+
+class MultiPointValue {
+    function init(Point[]|string|() value = (), int|() srid = ()) returns ();
+}
+
+class MultiLineStringValue {
+    function init(LineStringValue[]|string|() value = (), int|() srid = ()) returns ();
+}
 
-// Unknown type: MultiPolygonValue
+class MultiPolygonValue {
+    function init(PolygonValue[]|string|() value = (), int|() srid = ()) returns ();
+}
 
 # Represents an element of an MSSQL Geometry Collection type.
 # 
-type GeometryCollectionElement ballerinax/mssql:1.19.0:PointValue|ballerinax/mssql:1.19.0:LineStringValue|ballerinax/mssql:1.19.0:CircularStringValue|ballerinax/mssql:1.19.0:CompoundCurveValue|ballerinax/mssql:1.19.0:PolygonValue|ballerinax/mssql:1.19.0:CurvePolygonValue|ballerinax/mssql:1.19.0:MultiPointValue|ballerinax/mssql:1.19.0:MultiLineStringValue|ballerinax/mssql:1.19.0:MultiPolygonValue;
+type GeometryCollectionElement PointValue|LineStringValue|CircularStringValue|CompoundCurveValue|PolygonValue|CurvePolygonValue|MultiPointValue|MultiLineStringValue|MultiPolygonValue;
 
 # SQL Server streaming and query configuration.
 # 
@@ -773,23 +791,53 @@
     cdc:TimePrecisionMode timePrecisionMode?; // Special Agent Note: TimePrecisionMode FROM ballerinax/cdc package
 };
 
-// Unknown type: CdcListener
+# Initializes the MSSQL listener with the given configuration.
+# 
+class CdcListener {
+    function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {}, cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d, MsSqlDatabaseConnection database = {databaseNames: "", username: "", password: ""}, MssqlOptions options = {}, MsSqlListenerConfiguration config) returns (); // Special Agent Note: InternalSchemaStorage, OffsetStorage FROM ballerinax/cdc package
 
-// Unknown type: GeometryCollectionValue
+    # Attaches a CDC service to the MSSQL listener.
+    # 
+    function attach(cdc:Service s, string[]|string|() name = ()) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
 
-// Unknown type: MoneyValue
+    # Starts the MSSQL listener.
+    # 
+    function 'start() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
 
-// Unknown type: SmallMoneyValue
+    # Detaches a CDC service from the MSSQL listener.
+    # 
+    function detach(cdc:Service s) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
+
+    # Stops the MSSQL listener gracefully.
+    # 
+    function gracefulStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+
+    # Stops the MSSQL listener immediately.
+    # 
+    function immediateStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+}
 
+class GeometryCollectionValue {
+    function init(GeometryCollectionElement[]|string|() value = (), int|() srid = ()) returns ();
+}
+
+class MoneyValue {
+    function init(decimal|float|string|() value = ()) returns ();
+}
+
+class SmallMoneyValue {
+    function init(decimal|float|string|() value = ()) returns ();
+}
+
 // --- Client ---
 
 # MSSQL (Microsoft SQL) client that enables interaction with MSSQL servers and supports standard SQL operations.
 client class Client {
-    function init(string host = "localhost", string|() user = "sa", string|() password = (), string|() database = (), int port = 1433, string instance = "", Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string host = "localhost", string|() user = "sa", string|() password = (), string|() database = (), int port = 1433, string instance = "", Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes a SQL query and returns multiple results as a stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes a SQL query that is expected to return a single row or value as the result.
     # If the query returns no results, `sql:NoRowsError` is returned.
@@ -814,24 +862,38 @@
     # Closes the MSSQL client and shuts down the connection pool.
     # The client should be closed only at the end of the application lifetime, or when performing graceful stops in a service.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
 
 // --- Service ---
 
-service mssql:Service on new mssql:CdcListener(MsSqlListenerConfiguration config = {database: {databaseNames: "", username: "", password: ""}}) {
-    # Triggers initially to read existing records from the monitored table
-    remote function onRead(record {} afterEntry, string tableName) returns error?;
+# Requires: import ballerinax/mssql.cdc.driver as _;
+# A CDC service must declare at least one change handler. onError alone never receives a change event, so the service would do nothing.
+# Mandatory: this service must carry the @cdc:ServiceConfig annotation. Replace {...} with its fields, which are those of cdc:CdcServiceConfig.
+@cdc:ServiceConfig {...} // required; Special Agent Note: ServiceConfig, CdcServiceConfig FROM ballerinax/cdc package
+service cdc:Service on new mssql:CdcListener(mssql:MsSqlListenerConfiguration config = {database: {databaseNames: "", username: "", password: ""}}) { // Special Agent Note: Service FROM ballerinax/cdc package
+    # Invoked for each row captured during the initial snapshot of a table, before streaming of live changes begins.
+    # + afterEntry - The row as captured. Declare a record type to project its columns, see the rowState data-binding rule.
+    # + tableName - Name of the table the row came from, useful when one service handles several tables.
+    remote function onRead(record {} afterEntry, string tableName) returns error?; // optional
 
-    # Triggers when a new record is created in the monitored table
-    remote function onCreate(record {} afterEntry, string tableName) returns error?;
+    # Invoked when a row is inserted.
+    # + afterEntry - The row's state after the insert. Declare a record type to project its columns, see the rowState data-binding rule.
+    # + tableName - Name of the table the change occurred in.
+    remote function onCreate(record {} afterEntry, string tableName) returns error?; // optional
 
-    # Triggers when an existing record is updated in the monitored table
-    remote function onUpdate(record {} beforeEntry, record {} afterEntry, string tableName) returns error?;
+    # Invoked when a row is updated, with both the pre- and post-change images of the row.
+    # + beforeEntry - The row's state before the update.
+    # + afterEntry - The row's state after the update.
+    # + tableName - Name of the table the change occurred in.
+    remote function onUpdate(record {} beforeEntry, record {} afterEntry, string tableName) returns error?; // optional
 
-    # Triggers when a record is deleted from the monitored table
-    remote function onDelete(record {} beforeEntry, string tableName) returns error?;
+    # Invoked when a row is deleted. Only the pre-change image is available.
+    # + beforeEntry - The row's state immediately before it was deleted.
+    # + tableName - Name of the table the change occurred in.
+    remote function onDelete(record {} beforeEntry, string tableName) returns error?; // optional
 
-    # Triggers when an error occurs during event processing before mandatory functions are invoked
-    remote function onError(cdc:Error cdcError);
+    # Invoked when the connector fails to capture or dispatch a change event.
+    # + cdcError - The failure that interrupted change capture.
+    remote function onError(cdc:Error cdcError); // optional
 }
`````

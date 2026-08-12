# sql — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sql` |
| **Old file** | `sql/old/ballerina_sql.bal.txt` |
| **New file** | `sql/new/ballerina_sql.bal.txt` |
| **Old lines** | 1027 |
| **New lines** | 1551 |
| **Lines added** | 646 |
| **Lines removed** | 122 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 113 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 18 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (131)

- `annotation Column`
- `class ArrayOutParameter`
- `class ArrayValue`
- `class BigIntArrayOutParameter`
- `class BigIntArrayValue`
- `class BigIntOutParameter`
- `class BigIntValue`
- `class BinaryArrayOutParameter`
- `class BinaryArrayValue`
- `class BinaryOutParameter`
- `class BinaryValue`
- `class BitArrayOutParameter`
- `class BitArrayValue`
- `class BitOutParameter`
- `class BitValue`
- `class BlobOutParameter`
- `class BlobValue`
- `class BooleanArrayOutParameter`
- `class BooleanArrayValue`
- `class BooleanOutParameter`
- `class BooleanValue`
- `class CharArrayOutParameter`
- `class CharArrayValue`
- `class CharOutParameter`
- `class CharValue`
- `class ClobOutParameter`
- `class ClobValue`
- `class CursorOutParameter`
- `class DateArrayOutParameter`
- `class DateArrayValue`
- `class DateOutParameter`
- `class DateTimeArrayOutParameter`
- `class DateTimeArrayValue`
- `class DateTimeOutParameter`
- `class DateTimeValue`
- `class DateValue`
- `class DecimalArrayOutParameter`
- `class DecimalArrayValue`
- `class DecimalOutParameter`
- `class DecimalValue`
- `class DoubleArrayOutParameter`
- `class DoubleArrayValue`
- `class DoubleOutParameter`
- `class DoubleValue`
- `class FloatArrayOutParameter`
- `class FloatArrayValue`
- `class FloatOutParameter`
- `class FloatValue`
- `class InOutParameter`
- `class IntegerArrayOutParameter`
- `class IntegerArrayValue`
- `class IntegerOutParameter`
- `class IntegerValue`
- `class NCharOutParameter`
- `class NCharValue`
- `class NClobOutParameter`
- `class NClobValue`
- `class NVarcharArrayOutParameter`
- `class NVarcharArrayValue`
- `class NVarcharOutParameter`
- `class NVarcharValue`
- `class NumericArrayOutParameter`
- `class NumericArrayValue`
- `class NumericOutParameter`
- `class NumericValue`
- `class ProcedureCallResult`
- `class RealArrayOutParameter`
- `class RealArrayValue`
- `class RealOutParameter`
- `class RealValue`
- `class RefOutParameter`
- `class RefValue`
- `class ResultIterator`
- `class RowOutParameter`
- `class RowValue`
- `class SmallIntArrayOutParameter`
- `class SmallIntArrayValue`
- `class SmallIntOutParameter`
- `class SmallIntValue`
- `class StructOutParameter`
- `class StructValue`
- `class TextOutParameter`
- `class TextValue`
- `class TimeArrayOutParameter`
- `class TimeArrayValue`
- `class TimeOutParameter`
- `class TimeValue`
- `class TimeWithTimezoneArrayOutParameter`
- `class TimeWithTimezoneOutParameter`
- `class TimestampArrayOutParameter`
- `class TimestampArrayValue`
- `class TimestampOutParameter`
- `class TimestampValue`
- `class TimestampWithTimezoneArrayOutParameter`
- `class TimestampWithTimezoneOutParameter`
- `class VarBinaryArrayOutParameter`
- `class VarBinaryArrayValue`
- `class VarBinaryOutParameter`
- `class VarBinaryValue`
- `class VarcharArrayOutParameter`
- `class VarcharArrayValue`
- `class VarcharOutParameter`
- `class VarcharValue`
- `class XMLOutParameter`
- `client class Client`
- `client class SchemaClient`
- `function batchExecute`
- `function call`
- `function close`
- `function execute`
- `function get`
- `function getNextQueryResult`
- `function getRoutineInfo`
- `function getTableInfo`
- `function init`
- `function listRoutines`
- `function listTables`
- `function next`
- `function nextResult`
- `function query`
- `function queryRow`
- `type ApplicationError`
- `type BatchExecuteError`
- `type ConversionError`
- `type DataError`
- `type DatabaseError`
- `type Error`
- `type FieldMismatchError`
- `type NoRowsError`
- `type TypeMismatchError`
- `type UnsupportedTypeError`

### Declarations removed (2)

- `class Client`
- `class SchemaClient`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 509–515 | 509–558 | Types | +44 | −1 |
| 2 | 555–561 | 598–604 | Types | +1 | −1 |
| 3 | 616–640 | 659–694 | Types | +21 | −10 |
| 4 | 751–757 | 805–831 | Types | +21 | −1 |
| 5 | 766–772 | 840–846 | Types | +1 | −1 |
| 6 | 777–790 | 851–880 | Types | +19 | −3 |
| 7 | 797–1006 | 887–1525 | Types | +533 | −104 |
| 8 | 1024–1027 | 1543–1551 | Functions | +6 | −1 |

---

## Unified diff

`````diff
--- sql/old/ballerina_sql.bal.txt	2026-08-12 23:21:51
+++ sql/new/ballerina_sql.bal.txt	2026-08-12 23:23:51
@@ -509,7 +509,50 @@
 };
 
 # Represents an SQL client.
-class Client {
+client class Client {
+
+    # Executes the query, which may return multiple results.
+    # When processing the stream, make sure to consume all fetched data or close the stream.
+    # 
+    remote function query(ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = <>) returns stream<rowType, Error?>;
+
+    # Executes the query, which is expected to return at most one row of the result.
+    # If the query does not return any results, `sql:NoRowsError` is returned.
+    # 
+    remote function queryRow(ParameterizedQuery sqlQuery, anydata returnType = <>) returns returnType|Error;
+
+    # Executes the SQL query. Only the metadata of the execution is returned (not the results from the query).
+    # 
+    remote function execute(ParameterizedQuery sqlQuery) returns ExecutionResult|Error;
+
+    # Executes the SQL query with multiple sets of parameters in a batch. Only the metadata of the execution is returned (not the results from the query).
+    # If one of the commands in the batch fails, an `sql:BatchExecuteError` will be returned. However, the driver may
+    # or may not continue to process the remaining commands in the batch after a failure.
+    # 
+    remote function batchExecute(ParameterizedQuery[] sqlQueries) returns ExecutionResult[]|Error;
+
+    # Executes an SQL query, which calls a stored procedure or function. This may or may not
+    # return results. Once the results are processed, the `close` method on `sql:ProcedureCallResult` must be called.
+    # 
+    # This method supports two JDBC call syntaxes:
+    # - **Procedure call**: `` `{call procedureName(${param1}, ${param2})}` ``
+    # - **Function call**: `` `{${returnParam} = call functionName(${param1})}` ``
+    # 
+    # For function calls, use an `OutParameter` (e.g., `VarcharOutParameter`) as the return parameter to capture
+    # the function's return value:
+    # ```ballerina
+    # sql:VarcharOutParameter retVal = new;
+    # sql:ProcedureCallResult ret = check dbClient->call(`{${retVal} = call myFunc(${param})}`);
+    # string result = check retVal.get(string);
+    # check ret.close();
+    # ```
+    # 
+    remote function call(ParameterizedCallQuery sqlQuery, typedesc<record {|anydata...;|}>[] rowTypes = []) returns ProcedureCallResult|Error;
+
+    # Closes the SQL client and shuts down the connection pool. The client must be closed only at the end of the
+    # application lifetime (or closed for graceful stops in a service).
+    # 
+    function close() returns Error|();
 }
 
 
@@ -555,7 +598,7 @@
 `TRANSACTION_READ_UNCOMMITTED`, `TRANSACTION_READ_COMMITTED`, `TRANSACTION_REPEATABLE_READ`,
 `TRANSACTION_SERIALIZABLE`.
 This can be changed through the configuration API with the `ballerina.sql.transactionIsolation` key
-    ballerina/sql:1.19.0:TransactionIsolation? transactionIsolation?;
+    TransactionIsolation? transactionIsolation?;
     # SQL query to validate a connection. Leave unset to use driver-native validation. The default value is
 nil. This can be changed through the configuration API with the `ballerina.sql.connectionTestQuery` key
     string? connectionTestQuery?;
@@ -616,25 +659,36 @@
     string? sqlState;
 };
 
-// Unknown type: Error
+# Defines the generic error type for the `sql` module.
+type Error error;
 
-// Unknown type: DatabaseError
+# Represents an error caused by an issue related to database accessibility, erroneous queries, constraint violations,
+# database resource clean-up, and other similar scenarios.
+type DatabaseError error<record {|int errorCode; string? sqlState; anydata...;|}>;
 
-// Unknown type: BatchExecuteError
+# Represents an error that occurs during the execution of batch queries.
+type BatchExecuteError error<record {|int errorCode; string? sqlState; ExecutionResult[] executionResults; anydata...;|}>;
 
-// Unknown type: NoRowsError
+# Represents an error that occurs when a query retrieves does not retrieve any rows when at least one row is expected.
+type NoRowsError error;
 
-// Unknown type: ApplicationError
+# Represents an error originating from application-level configurations.
+type ApplicationError error;
 
-// Unknown type: DataError
+# Represents an error that occurs during the processing of the parameters or returned results.
+type DataError error;
 
-// Unknown type: TypeMismatchError
+# Represents an error that occurs when a query retrieves a result that differs from the supported result type.
+type TypeMismatchError error;
 
-// Unknown type: ConversionError
+# Represents an error that occurs when a query retrieves a result that is corrupted and cannot be converted to the expected type.
+type ConversionError error;
 
-// Unknown type: FieldMismatchError
+# Represents an error that occurs when a query retrieves a result that cannot be mapped to the expected record type.
+type FieldMismatchError error;
 
-// Unknown type: UnsupportedTypeError
+# Represents an error that occurs when an unsupported parameter type is added to the query.
+type UnsupportedTypeError error;
 
 # Represents the type of the table/view retrieved through the `getTableInfo` function.
 # 
@@ -751,7 +805,27 @@
 
 # Represents an SQL metadata client.
 # 
-class SchemaClient {
+client class SchemaClient {
+
+    # Retrieves all tables in the database.
+    # 
+    remote function listTables() returns string[]|Error;
+
+    # Retrieves information relevant to the provided table in the database.
+    # 
+    remote function getTableInfo(string tableName, ColumnRetrievalOptions include = COLUMNS_ONLY) returns TableDefinition|Error;
+
+    # Retrieves all routines in the database.
+    # 
+    remote function listRoutines() returns string[]|Error;
+
+    # Retrieves information relevant to the provided routine in the database.
+    # 
+    remote function getRoutineInfo(string name) returns RoutineDefinition|Error;
+
+    # Closes the SQL metadata client.
+    # 
+    function close() returns Error|();
 }
 
 enum ColumnRetrievalOptions {
@@ -766,7 +840,7 @@
 }
 
 # Generic type of ballerina basic types that can be passed to `sql:ParameterizedQuery` to represent parameters in the SQL query.
-type Value string|int|boolean|float|decimal|byte[]|xml|record {|anydata...;|}|ballerina/time:2.8.1:Utc|ballerina/time:2.8.1:Civil|ballerina/time:2.8.1:Date|ballerina/time:2.8.1:TimeOfDay|ballerina/time:2.8.1:Civil[]|ballerina/time:2.8.1:TimeOfDay[]|(string?)[]|(int?)[]|(boolean?)[]|(float?)[]|(decimal?)[]|(byte[]?)[]|ballerina/sql:1.19.0:TypedValue|();
+type Value string|int|boolean|float|decimal|byte[]|xml|record {|anydata...;|}|time:Utc|time:Civil|time:Date|time:TimeOfDay|time:Civil[]|time:TimeOfDay[]|(string?)[]|(int?)[]|(boolean?)[]|(float?)[]|(decimal?)[]|(byte[]?)[]|TypedValue|();
 
 # The object constructed through backtick surrounded strings. Dynamic parameters of `sql:Value` type can be indicated using `${<variable name>}`
 # such as `` `The sql:ParameterizedQuery is ${variable_name}` ``.
@@ -777,14 +851,30 @@
 
 # Represents the generic OUT Parameters in `sql:ParameterizedCallQuery`.
 class OutParameter {
+
+    # Parses returned Char SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = <>) returns typeDesc|Error;
 }
 
-// Unknown type: InOutParameter
+class InOutParameter {
+    function init(Value 'in) returns ();
 
-// Unknown type: CursorOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
+# Represents the Cursor Out Parameters in `sql:ParameterizedCallQuery`.
+class CursorOutParameter {
+
+    # Parses returned SQL result set values to a ballerina stream value.
+    # 
+    function get(record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, Error?>;
+}
+
 # Generic type that can be passed to `sql:ParameterizedCallQuery` to indicate procedure/function parameters.
-type Parameter string|int|boolean|float|decimal|byte[]|xml|record {|anydata...;|}|ballerina/time:2.8.1:Utc|ballerina/time:2.8.1:Civil|ballerina/time:2.8.1:Date|ballerina/time:2.8.1:TimeOfDay|ballerina/time:2.8.1:Civil[]|ballerina/time:2.8.1:TimeOfDay[]|(string?)[]|(int?)[]|(boolean?)[]|(float?)[]|(decimal?)[]|(byte[]?)[]|ballerina/sql:1.19.0:TypedValue|()|ballerina/sql:1.19.0:InOutParameter|ballerina/sql:1.19.0:OutParameter|ballerina/sql:1.19.0:CursorOutParameter;
+type Parameter string|int|boolean|float|decimal|byte[]|xml|record {|anydata...;|}|time:Utc|time:Civil|time:Date|time:TimeOfDay|time:Civil[]|time:TimeOfDay[]|(string?)[]|(int?)[]|(boolean?)[]|(float?)[]|(decimal?)[]|(byte[]?)[]|TypedValue|()|InOutParameter|OutParameter|CursorOutParameter;
 
 # The object constructed through backtick surrounded strings. Dynamic parameters of `sql:Parameter` type can be indicated using `${<variable name>}`
 # such as `` `The sql:ParameterizedQuery is ${variable_name}` ``.
@@ -797,210 +887,639 @@
 
 # The iterator for the stream returned in the `query` function to be used to override the default behavior of the `sql:ResultIterator`.
 class CustomResultIterator {
-}
 
-// Unknown type: VarcharValue
+    function nextResult(ResultIterator iterator) returns record {|anydata...;|}|Error|();
 
-// Unknown type: VarcharArrayValue
+    function getNextQueryResult(ProcedureCallResult callResult) returns boolean|Error;
+}
 
-// Unknown type: NVarcharValue
+class VarcharValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: NVarcharArrayValue
+class VarcharArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: CharValue
+class NVarcharValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: CharArrayValue
-
-// Unknown type: NCharValue
+class NVarcharArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: TextValue
+class CharValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: ClobValue
+class CharArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: NClobValue
+class NCharValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: SmallIntValue
+class TextValue {
+    function init(io:ReadableCharacterChannel|string|() value = ()) returns (); // Special Agent Note: ReadableCharacterChannel FROM ballerina/io package
+}
 
-// Unknown type: SmallIntArrayValue
+class ClobValue {
+    function init(io:ReadableCharacterChannel|string|() value = ()) returns (); // Special Agent Note: ReadableCharacterChannel FROM ballerina/io package
+}
 
-// Unknown type: IntegerValue
+class NClobValue {
+    function init(io:ReadableCharacterChannel|string|() value = ()) returns (); // Special Agent Note: ReadableCharacterChannel FROM ballerina/io package
+}
 
-// Unknown type: IntegerArrayValue
+class SmallIntValue {
+    function init(int|() value = ()) returns ();
+}
 
-// Unknown type: BigIntValue
+class SmallIntArrayValue {
+    function init((int?)[] value = []) returns ();
+}
 
-// Unknown type: BigIntArrayValue
+class IntegerValue {
+    function init(int|() value = ()) returns ();
+}
 
-// Unknown type: NumericValue
+class IntegerArrayValue {
+    function init((int?)[] value = []) returns ();
+}
 
-// Unknown type: NumericArrayValue
+class BigIntValue {
+    function init(int|() value = ()) returns ();
+}
 
-// Unknown type: DecimalValue
+class BigIntArrayValue {
+    function init((int?)[] value = []) returns ();
+}
 
-// Unknown type: DecimalArrayValue
+class NumericValue {
+    function init(int|float|decimal|() value = ()) returns ();
+}
 
-// Unknown type: RealValue
+class NumericArrayValue {
+    function init((int?)[]|(float?)[]|(decimal?)[] value = <int?[]>[]) returns ();
+}
 
-// Unknown type: RealArrayValue
+class DecimalValue {
+    function init(int|decimal|() value = ()) returns ();
+}
 
-// Unknown type: FloatValue
+class DecimalArrayValue {
+    function init((int?)[]|(decimal?)[] value = <int?[]>[]) returns ();
+}
 
-// Unknown type: FloatArrayValue
+class RealValue {
+    function init(int|float|decimal|() value = ()) returns ();
+}
 
-// Unknown type: DoubleValue
+class RealArrayValue {
+    function init((int?)[]|(float?)[]|(decimal?)[] value = <int?[]>[]) returns ();
+}
 
-// Unknown type: DoubleArrayValue
+class FloatValue {
+    function init(int|float|() value = ()) returns ();
+}
 
-// Unknown type: BitValue
+class FloatArrayValue {
+    function init((int?)[]|(float?)[] value = <int?[]>[]) returns ();
+}
 
-// Unknown type: BitArrayValue
+class DoubleValue {
+    function init(int|float|decimal|() value = ()) returns ();
+}
 
-// Unknown type: BooleanValue
+class DoubleArrayValue {
+    function init((int?)[]|(float?)[]|(decimal?)[] value = <int?[]>[]) returns ();
+}
 
-// Unknown type: BooleanArrayValue
+class BitValue {
+    function init(boolean|int|() value = ()) returns ();
+}
 
-// Unknown type: BinaryValue
+class BitArrayValue {
+    function init((boolean?)[]|(int?)[] value = <int?[]>[]) returns ();
+}
+
+class BooleanValue {
+    function init(boolean|() value = ()) returns ();
+}
 
-// Unknown type: BinaryArrayValue
+class BooleanArrayValue {
+    function init((boolean?)[] value = []) returns ();
+}
 
-// Unknown type: VarBinaryValue
+class BinaryValue {
+    function init(byte[]|io:ReadableByteChannel|() value = ()) returns (); // Special Agent Note: ReadableByteChannel FROM ballerina/io package
+}
 
-// Unknown type: VarBinaryArrayValue
+class BinaryArrayValue {
+    function init(io:ReadableByteChannel[]|byte[]|()[] value = <byte[]?[]>[]) returns (); // Special Agent Note: ReadableByteChannel FROM ballerina/io package
+}
 
-// Unknown type: BlobValue
+class VarBinaryValue {
+    function init(byte[]|io:ReadableByteChannel|() value = ()) returns (); // Special Agent Note: ReadableByteChannel FROM ballerina/io package
+}
 
-// Unknown type: DateValue
+class VarBinaryArrayValue {
+    function init(byte[]|()[]|io:ReadableByteChannel[] value = <byte[]?[]>[]) returns (); // Special Agent Note: ReadableByteChannel FROM ballerina/io package
+}
 
-// Unknown type: DateArrayValue
+class BlobValue {
+    function init(byte[]|io:ReadableByteChannel|() value = ()) returns (); // Special Agent Note: ReadableByteChannel FROM ballerina/io package
+}
 
-// Unknown type: TimeValue
+class DateValue {
+    function init(string|time:Date|() value = ()) returns (); // Special Agent Note: Date FROM ballerina/time package
+}
 
-// Unknown type: TimeArrayValue
+class DateArrayValue {
+    function init(string|()[]|time:Date|()[] value = <string?[]>[]) returns (); // Special Agent Note: Date FROM ballerina/time package
+}
 
-// Unknown type: DateTimeValue
+class TimeValue {
+    function init(string|time:TimeOfDay|() value = ()) returns (); // Special Agent Note: TimeOfDay FROM ballerina/time package
+}
 
-// Unknown type: DateTimeArrayValue
+class TimeArrayValue {
+    function init(string|()[]|time:TimeOfDay|()[] value = <string?[]>[]) returns (); // Special Agent Note: TimeOfDay FROM ballerina/time package
+}
 
-// Unknown type: TimestampValue
+class DateTimeValue {
+    function init(string|time:Civil|() value = ()) returns (); // Special Agent Note: Civil FROM ballerina/time package
+}
 
-// Unknown type: TimestampArrayValue
+class DateTimeArrayValue {
+    function init(string|()[]|time:Civil|()[] value = <string?[]>[]) returns (); // Special Agent Note: Civil FROM ballerina/time package
+}
 
-// Unknown type: ArrayValue
+class TimestampValue {
+    function init(string|time:Utc|() value = ()) returns (); // Special Agent Note: Utc FROM ballerina/time package
+}
 
-// Unknown type: RefValue
+class TimestampArrayValue {
+    function init(string|()[]|time:Utc|()[] value = <string?[]>[]) returns (); // Special Agent Note: Utc FROM ballerina/time package
+}
 
-// Unknown type: StructValue
+@deprecated
+class ArrayValue {
+    function init(string[]|int[]|boolean[]|float[]|decimal[]|byte[][]|() value = ()) returns ();
+}
 
-// Unknown type: RowValue
+class RefValue {
+    function init(record {|anydata...;|}|() value = ()) returns ();
+}
 
-// Unknown type: CharOutParameter
+class StructValue {
+    function init(record {|anydata...;|}|() value = ()) returns ();
+}
 
-// Unknown type: CharArrayOutParameter
+class RowValue {
+    function init(byte[]|() value = ()) returns ();
+}
 
-// Unknown type: VarcharOutParameter
+# Represents Char Out Parameter in `sql:ParameterizedCallQuery`.
+class CharOutParameter {
 
-// Unknown type: VarcharArrayOutParameter
+    # Parses returned Char SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: NCharOutParameter
+# Represents Char Array Out Parameter in `sql:ParameterizedCallQuery`.
+class CharArrayOutParameter {
 
-// Unknown type: NVarcharOutParameter
+    # Parses returned Char SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: NVarcharArrayOutParameter
+# Represents Varchar Out Parameter in `sql:ParameterizedCallQuery`.
+class VarcharOutParameter {
 
-// Unknown type: BinaryOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: BinaryArrayOutParameter
+# Represents Varchar Array Out Parameter in `sql:ParameterizedCallQuery`.
+class VarcharArrayOutParameter {
 
-// Unknown type: VarBinaryOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: VarBinaryArrayOutParameter
+# Represents NChar Out Parameter in `sql:ParameterizedCallQuery`.
+class NCharOutParameter {
 
-// Unknown type: TextOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: BlobOutParameter
+# Represents NVarchar Out Parameter in `sql:ParameterizedCallQuery`.
+class NVarcharOutParameter {
 
-// Unknown type: ClobOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: NClobOutParameter
+# Represents NVarchar Array Out Parameter in `sql:ParameterizedCallQuery`.
+class NVarcharArrayOutParameter {
 
-// Unknown type: DateOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: DateArrayOutParameter
+# Represents Binary Out Parameter in `sql:ParameterizedCallQuery`.
+class BinaryOutParameter {
 
-// Unknown type: TimeOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: TimeArrayOutParameter
+# Represents Binary Array Out Parameter in `sql:ParameterizedCallQuery`.
+class BinaryArrayOutParameter {
 
-// Unknown type: TimeWithTimezoneOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: TimeWithTimezoneArrayOutParameter
+# Represents VarBinary Out Parameter in `sql:ParameterizedCallQuery`.
+class VarBinaryOutParameter {
 
-// Unknown type: DateTimeOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: DateTimeArrayOutParameter
+# Represents VarBinary Array Out Parameter in `sql:ParameterizedCallQuery`.
+class VarBinaryArrayOutParameter {
 
-// Unknown type: TimestampOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: TimestampArrayOutParameter
-
-// Unknown type: TimestampWithTimezoneOutParameter
+# Represents Text Out Parameter in `sql:ParameterizedCallQuery`.
+class TextOutParameter {
 
-// Unknown type: TimestampWithTimezoneArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: ArrayOutParameter
+# Represents Blob Out Parameter in `sql:ParameterizedCallQuery`.
+class BlobOutParameter {
 
-// Unknown type: RowOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: SmallIntOutParameter
+# Represents Clob Out Parameter in `sql:ParameterizedCallQuery`.
+class ClobOutParameter {
 
-// Unknown type: SmallIntArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: IntegerOutParameter
+# Represents NClob Out Parameter in `sql:ParameterizedCallQuery`.
+class NClobOutParameter {
 
-// Unknown type: BigIntOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: IntegerArrayOutParameter
+# Represents Date Out Parameter in `sql:ParameterizedCallQuery`.
+class DateOutParameter {
 
-// Unknown type: BigIntArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: RealOutParameter
+# Represents Date Array Out Parameter in `sql:ParameterizedCallQuery`.
+class DateArrayOutParameter {
 
-// Unknown type: RealArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: FloatOutParameter
+# Represents Time Out Parameter in `sql:ParameterizedCallQuery`.
+class TimeOutParameter {
 
-// Unknown type: FloatArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: DoubleOutParameter
+# Represents Time Array Out Parameter in `sql:ParameterizedCallQuery`.
+class TimeArrayOutParameter {
 
-// Unknown type: DoubleArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: NumericOutParameter
+# Represents Time With Timezone Out Parameter in `sql:ParameterizedCallQuery`.
+class TimeWithTimezoneOutParameter {
 
-// Unknown type: NumericArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: DecimalOutParameter
+# Represents Time With Timezone Array Out Parameter in `sql:ParameterizedCallQuery`.
+class TimeWithTimezoneArrayOutParameter {
 
-// Unknown type: DecimalArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: BitOutParameter
+# Represents DateTime Out Parameter in `sql:ParameterizedCallQuery`.
+class DateTimeOutParameter {
 
-// Unknown type: BitArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: BooleanOutParameter
+# Represents DateTime Array Out Parameter in `sql:ParameterizedCallQuery`.
+class DateTimeArrayOutParameter {
 
-// Unknown type: BooleanArrayOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: RefOutParameter
+# Represents Timestamp Out Parameter in `sql:ParameterizedCallQuery`.
+class TimestampOutParameter {
 
-// Unknown type: StructOutParameter
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: XMLOutParameter
+# Represents Timestamp Array Out Parameter in `sql:ParameterizedCallQuery`.
+class TimestampArrayOutParameter {
 
-// Unknown type: ResultIterator
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
 
-// Unknown type: ProcedureCallResult
+# Represents Timestamp with Timezone Out Parameter in `sql:ParameterizedCallQuery`.
+class TimestampWithTimezoneOutParameter {
 
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Timestamp with Timezone Array Out Parameter in `sql:ParameterizedCallQuery`.
+class TimestampWithTimezoneArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Array Out Parameter in `sql:ParameterizedCallQuery`.
+class ArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Row Out Parameter in `sql:ParameterizedCallQuery`.
+class RowOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents SmallInt Out Parameter in `sql:ParameterizedCallQuery`.
+class SmallIntOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents SmallInt Array Out Parameter in `sql:ParameterizedCallQuery`.
+class SmallIntArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Integer Out Parameter in `sql:ParameterizedCallQuery`.
+class IntegerOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents BigInt Out Parameter in `sql:ParameterizedCallQuery`.
+class BigIntOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Integer Array Out Parameter in `sql:ParameterizedCallQuery`.
+class IntegerArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents BigInt Array Out Parameter in `sql:ParameterizedCallQuery`.
+class BigIntArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Real Out Parameter in `sql:ParameterizedCallQuery`.
+class RealOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Real Array Out Parameter in `sql:ParameterizedCallQuery`.
+class RealArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Float Out Parameter in `sql:ParameterizedCallQuery`.
+class FloatOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Float Array Out Parameter in `sql:ParameterizedCallQuery`.
+class FloatArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Double Out Parameter in `sql:ParameterizedCallQuery`.
+class DoubleOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Double Array Out Parameter in `sql:ParameterizedCallQuery`.
+class DoubleArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Numeric Out Parameter in `sql:ParameterizedCallQuery`.
+class NumericOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Numeric Array Out Parameter in `sql:ParameterizedCallQuery`.
+class NumericArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Decimal Out Parameter in `sql:ParameterizedCallQuery`.
+class DecimalOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Decimal Out Parameter in `sql:ParameterizedCallQuery`.
+class DecimalArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Bit Out Parameter in `sql:ParameterizedCallQuery`.
+class BitOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Bit Array Out Parameter in `sql:ParameterizedCallQuery`.
+class BitArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Boolean Out Parameter in `sql:ParameterizedCallQuery`.
+class BooleanOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Boolean Array Out Parameter in `sql:ParameterizedCallQuery`.
+class BooleanArrayOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Ref Out Parameter in `sql:ParameterizedCallQuery`.
+class RefOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents Struct Out Parameter in `sql:ParameterizedCallQuery`.
+class StructOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+# Represents XML Out Parameter in `sql:ParameterizedCallQuery`.
+class XMLOutParameter {
+
+    # Parses returned SQL value to a ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|Error;
+}
+
+class ResultIterator {
+    function init(Error|() err = (), CustomResultIterator|() customResultIterator = ()) returns ();
+
+    function next() returns record {|record {|anydata...;|} value;|}|Error|();
+
+    function close() returns Error|();
+}
+
+class ProcedureCallResult {
+    function init(CustomResultIterator|() customResultIterator = ()) returns ();
+
+    # Updates `executionResult` or `queryResult` field with the succeeding result in the result list. This will also close the current
+    # result when called. The `close` method must be called once all the results are processed.
+    # 
+    function getNextQueryResult() returns boolean|Error;
+
+    # Releases the associated resources such as the database connection, results, etc.
+    # This method must be called once all results are processed.
+    # 
+    function close() returns Error|();
+}
+
 // --- Functions ---
 
 # Returns the global connection pool.
@@ -1024,4 +1543,9 @@
 # 
 # + message - Error message used to initialise an `sql:Error`
 # + return - A stream
-function generateApplicationErrorStream(string message) returns Error?>;
+function generateApplicationErrorStream(string message) returns stream<record {|anydata...;|}, Error?>;
+
+// --- Annotations ---
+
+# The Annotation used to specify which database column matches the Typed record field.
+public annotation ColumnConfig Column on record field;
`````

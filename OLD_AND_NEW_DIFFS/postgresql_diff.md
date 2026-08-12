# postgresql — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `postgresql` |
| **Old file** | `postgresql/old/ballerinax_postgresql.bal.txt` |
| **New file** | `postgresql/new/ballerinax_postgresql.bal.txt` |
| **Old lines** | 1393 |
| **New lines** | 1864 |
| **Lines added** | 603 |
| **Lines removed** | 132 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 126 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (134)

- `class BitStringArrayValue`
- `class BitStringValue`
- `class BoxArrayValue`
- `class BoxOutParameter`
- `class BoxValue`
- `class ByteaOutParameter`
- `class CdcListener`
- `class CidrArrayValue`
- `class CidrOutParameter`
- `class CidrValue`
- `class CircleArrayValue`
- `class CircleOutParameter`
- `class CircleValue`
- `class CustomResultIterator`
- `class CustomTypeValue`
- `class DateRangeArrayValue`
- `class DateRangeOutParameter`
- `class DateRangeValue`
- `class EnumOutParameter`
- `class EnumValue`
- `class InOutParameter`
- `class InetArrayValue`
- `class InetOutParameter`
- `class InetValue`
- `class IntegerRangeArrayValue`
- `class IntegerRangeOutParameter`
- `class IntegerRangeValue`
- `class IntervalArrayValue`
- `class IntervalOutParameter`
- `class IntervalValue`
- `class JsonArrayValue`
- `class JsonBinaryArrayValue`
- `class JsonBinaryValue`
- `class JsonOutParameter`
- `class JsonPathArrayValue`
- `class JsonPathOutParameter`
- `class JsonPathValue`
- `class JsonValue`
- `class JsonbOutParameter`
- `class LineArrayValue`
- `class LineOutParameter`
- `class LineSegmentArrayValue`
- `class LineSegmentValue`
- `class LineValue`
- `class LongRangeArrayValue`
- `class LongRangeOutParameter`
- `class LongRangeValue`
- `class LsegOutParameter`
- `class MacAddr8ArrayValue`
- `class MacAddr8OutParameter`
- `class MacAddr8Value`
- `class MacAddrArrayValue`
- `class MacAddrOutParameter`
- `class MacAddrValue`
- `class MoneyArrayValue`
- `class MoneyOutParameter`
- `class MoneyValue`
- `class NumericRangeArrayValue`
- `class NumericRangeOutParameter`
- `class NumericRangeValue`
- `class PGBitArrayValue`
- `class PGBitOutParameter`
- `class PGBitValue`
- `class PGXmlArrayValue`
- `class PGXmlOutParameter`
- `class PGXmlValue`
- `class PathArrayValue`
- `class PathOutParameter`
- `class PathValue`
- `class PglsnArrayValue`
- `class PglsnOutParameter`
- `class PglsnValue`
- `class PointArrayValue`
- `class PointOutParameter`
- `class PointValue`
- `class PolygonArrayValue`
- `class PolygonOutParameter`
- `class PolygonValue`
- `class RegClassArrayValue`
- `class RegClassOutParameter`
- `class RegClassValue`
- `class RegConfigArrayValue`
- `class RegConfigOutParameter`
- `class RegConfigValue`
- `class RegDictionaryArrayValue`
- `class RegDictionaryOutParameter`
- `class RegDictionaryValue`
- `class RegNamespaceArrayValue`
- `class RegNamespaceOutParameter`
- `class RegNamespaceValue`
- `class RegOperArrayValue`
- `class RegOperOutParameter`
- `class RegOperValue`
- `class RegOperatorArrayValue`
- `class RegOperatorOutParameter`
- `class RegOperatorValue`
- `class RegProcArrayValue`
- `class RegProcOutParameter`
- `class RegProcValue`
- `class RegProcedureArrayValue`
- `class RegProcedureOutParameter`
- `class RegProcedureValue`
- `class RegRoleArrayValue`
- `class RegRoleOutParameter`
- `class RegRoleValue`
- `class RegTypeArrayValue`
- `class RegTypeOutParameter`
- `class RegTypeValue`
- `class TimestampRangeOutParameter`
- `class TimestampTzRangeOutParameter`
- `class TsQueryArrayValue`
- `class TsQueryOutParameter`
- `class TsQueryValue`
- `class TsRangeArrayValue`
- `class TsRangeValue`
- `class TsTzRangeArrayValue`
- `class TsTzRangeValue`
- `class TsVectorArrayValue`
- `class TsVectorOutParameter`
- `class TsVectorValue`
- `class UuidArrayValue`
- `class UuidOutParameter`
- `class UuidValue`
- `class VarBitStringArrayValue`
- `class VarBitStringOutParameter`
- `class VarBitStringValue`
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
| 1 | 1084–1350 | 1084–1800 | Types | +580 | −130 |
| 2 | 1367–1393 | 1817–1864 | Client | +23 | −2 |

---

## Unified diff

`````diff
--- postgresql/old/ballerinax_postgresql.bal.txt	2026-08-12 12:57:30
+++ postgresql/new/ballerinax_postgresql.bal.txt	2026-08-12 13:19:19
@@ -1084,267 +1084,717 @@
     boolean lowerboundInclusive?;
 };
 
-// Unknown type: CdcListener
+# Initializes the Postgresql listener with the given configuration.
+# 
+class CdcListener {
+    function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {}, cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d, PostgresDatabaseConnection database = {databaseName: "", username: "", password: ""}, PostgreSqlOptions options = {}, PostgresListenerConfiguration config) returns (); // Special Agent Note: InternalSchemaStorage, OffsetStorage FROM ballerinax/cdc package
 
-// Unknown type: IntervalOutParameter
+    # Attaches a CDC service to the Postgresql listener.
+    # 
+    function attach(cdc:Service s, string[]|string|() name = ()) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
 
-// Unknown type: InetOutParameter
+    # Starts the Postgresql listener.
+    # 
+    function 'start() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
 
-// Unknown type: CidrOutParameter
+    # Detaches a CDC service from the Postgresql listener.
+    # 
+    function detach(cdc:Service s) returns cdc:Error|(); // Special Agent Note: Service, Error FROM ballerinax/cdc package
 
-// Unknown type: MacAddrOutParameter
+    # Stops the Postgresql listener gracefully.
+    # 
+    function gracefulStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
 
-// Unknown type: MacAddr8OutParameter
+    # Stops the Postgresql listener immediately.
+    # 
+    function immediateStop() returns cdc:Error|(); // Special Agent Note: Error FROM ballerinax/cdc package
+}
 
-// Unknown type: PointOutParameter
+# Represents the `Interval` `OutParameter` in `sql:ParameterizedCallQuery`.
+class IntervalOutParameter {
 
-// Unknown type: LineOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: LsegOutParameter
+# Represents the `Inet` `OutParameter` in `sql:ParameterizedCallQuery`.
+class InetOutParameter {
 
-// Unknown type: PathOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PolygonOutParameter
+# Represents the `Cidr` `OutParameter` in `sql:ParameterizedCallQuery`.
+class CidrOutParameter {
 
-// Unknown type: BoxOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: CircleOutParameter
+# Represents the `MacAddr` `OutParameter` in `sql:ParameterizedCallQuery`.
+class MacAddrOutParameter {
 
-// Unknown type: UuidOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PglsnOutParameter
+# Represents the `MacAddr8` `OutParameter` in `sql:ParameterizedCallQuery`.
+class MacAddr8OutParameter {
 
-// Unknown type: JsonOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: JsonbOutParameter
+# Represents the `Point` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PointOutParameter {
 
-// Unknown type: JsonPathOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: IntegerRangeOutParameter
+# Represents the `Line` `OutParameter` in `sql:ParameterizedCallQuery`.
+class LineOutParameter {
 
-// Unknown type: LongRangeOutParameter
-
-// Unknown type: NumericRangeOutParameter
-
-// Unknown type: TimestampRangeOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TimestampTzRangeOutParameter
+# Represents the `Lseg` `OutParameter` in `sql:ParameterizedCallQuery`.
+class LsegOutParameter {
 
-// Unknown type: DateRangeOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: VarBitStringOutParameter
+# Represents the `Path` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PathOutParameter {
 
-// Unknown type: PGBitOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: ByteaOutParameter
+# Represents the `Polygon` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PolygonOutParameter {
 
-// Unknown type: PGXmlOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TsVectorOutParameter
+# Represents the `Box` `OutParameter` in `sql:ParameterizedCallQuery`.
+class BoxOutParameter {
 
-// Unknown type: TsQueryOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: RegClassOutParameter
+# Represents the `Circle` `OutParameter` in `sql:ParameterizedCallQuery`.
+class CircleOutParameter {
 
-// Unknown type: RegNamespaceOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: RegConfigOutParameter
+# Represents the `UUID` `OutParameter` in `sql:ParameterizedCallQuery`.
+class UuidOutParameter {
 
-// Unknown type: RegDictionaryOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: RegOperOutParameter
+# Represents the `Pglsn` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PglsnOutParameter {
 
-// Unknown type: RegOperatorOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: RegProcOutParameter
+# Represents the `JSON` `OutParameter` in `sql:ParameterizedCallQuery`.
+class JsonOutParameter {
 
-// Unknown type: RegProcedureOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: RegRoleOutParameter
+# Represents the `JSONB` `OutParameter` in `sql:ParameterizedCallQuery`.
+class JsonbOutParameter {
 
-// Unknown type: RegTypeOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: MoneyOutParameter
+# Represents the `JSONPath` `OutParameter` in `sql:ParameterizedCallQuery`.
+class JsonPathOutParameter {
 
-// Unknown type: EnumOutParameter
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: InOutParameter
+# Represents the `Int4 range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class IntegerRangeOutParameter {
 
-// Unknown type: CustomResultIterator
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: InetValue
+# Represents the `Int8 Range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class LongRangeOutParameter {
 
-// Unknown type: InetArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: CidrValue
+# Represents the `Numeric range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class NumericRangeOutParameter {
 
-// Unknown type: CidrArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: MacAddrValue
+# Represents the `Timestamp Range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class TimestampRangeOutParameter {
 
-// Unknown type: MacAddrArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: MacAddr8Value
+# Represents the `Timestamp with Timezone Range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class TimestampTzRangeOutParameter {
 
-// Unknown type: MacAddr8ArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PointValue
+# Represents the `Date Range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class DateRangeOutParameter {
 
-// Unknown type: PointArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: LineValue
+# Represents the `Varbitstring` `OutParameter` in `sql:ParameterizedCallQuery`.
+class VarBitStringOutParameter {
 
-// Unknown type: LineArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: LineSegmentValue
+# Represents the `PGBit` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PGBitOutParameter {
 
-// Unknown type: LineSegmentArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: BoxValue
+# Represents the `Bytea range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class ByteaOutParameter {
 
-// Unknown type: BoxArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PathValue
+# Represents the `XML range` `OutParameter` in `sql:ParameterizedCallQuery`.
+class PGXmlOutParameter {
 
-// Unknown type: PathArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PolygonValue
+# Represents the `Text Vector` `OutParameter` in `sql:ParameterizedCallQuery`.
+class TsVectorOutParameter {
 
-// Unknown type: PolygonArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: CircleValue
+# Represents the `Text Query` `OutParameter` in `sql:ParameterizedCallQuery`.
+class TsQueryOutParameter {
 
-// Unknown type: CircleArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: UuidValue
+# Represents the `Regclass` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegClassOutParameter {
 
-// Unknown type: UuidArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TsVectorValue
+# Represents the `Regnamespace` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegNamespaceOutParameter {
 
-// Unknown type: TsVectorArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TsQueryValue
+# Represents the `Regconfig` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegConfigOutParameter {
 
-// Unknown type: TsQueryArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: JsonValue
+# Represents the `Regdictionary` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegDictionaryOutParameter {
 
-// Unknown type: JsonArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: JsonBinaryValue
+# Represents the `Regoper` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegOperOutParameter {
 
-// Unknown type: JsonBinaryArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: JsonPathValue
+# Represents the `Regoperator` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegOperatorOutParameter {
 
-// Unknown type: JsonPathArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: IntervalValue
+# Represents the `Regproc` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegProcOutParameter {
 
-// Unknown type: IntervalArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: IntegerRangeValue
+# Represents the `Regprocedure` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegProcedureOutParameter {
 
-// Unknown type: IntegerRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: LongRangeValue
+# Represents the `Regrole` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegRoleOutParameter {
 
-// Unknown type: LongRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: NumericRangeValue
+# Represents the `Regtype` `OutParameter` in `sql:ParameterizedCallQuery`.
+class RegTypeOutParameter {
 
-// Unknown type: NumericRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TsRangeValue
+# Represents the `Money` `OutParameter` in `sql:ParameterizedCallQuery`.
+class MoneyOutParameter {
 
-// Unknown type: TsRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: TsTzRangeValue
+# Represents the `Enum` `OutParameter` in `sql:ParameterizedCallQuery`.
+class EnumOutParameter {
 
-// Unknown type: TsTzRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: DateRangeValue
+class InOutParameter {
+    function init(sql:Value 'in) returns (); // Special Agent Note: Value FROM ballerina/sql package
 
-// Unknown type: DateRangeArrayValue
+    # Parses the returned SQL value to a Ballerina value.
+    # 
+    function get(anydata typeDesc = anydata) returns typeDesc|sql:Error; // Special Agent Note: Error FROM ballerina/sql package
+}
 
-// Unknown type: PglsnValue
+# The iterator for the stream returned in `query` function to be used in overriding the default behaviour of `sql:ResultIterator`.
+class CustomResultIterator {
 
-// Unknown type: PglsnArrayValue
+    # Retrieves the next result from the `sql:ResultIterator`.
+    # 
+    function nextResult(sql:ResultIterator iterator) returns record {|anydata...;|}|sql:Error|(); // Special Agent Note: ResultIterator, Error FROM ballerina/sql package
 
-// Unknown type: BitStringValue
+    # Retrieves the next query result from the `sql:ProcedureCallResult`.
+    # 
+    function getNextQueryResult(sql:ProcedureCallResult callResult) returns boolean|sql:Error; // Special Agent Note: ProcedureCallResult, Error FROM ballerina/sql package
+}
 
-// Unknown type: BitStringArrayValue
+class InetValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: VarBitStringValue
+class InetArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: VarBitStringArrayValue
+class CidrValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: PGBitValue
+class CidrArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class MacAddrValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: PGBitArrayValue
+class MacAddrArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: MoneyValue
+class MacAddr8Value {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: MoneyArrayValue
+class MacAddr8ArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: RegClassValue
+class PointValue {
+    function init(Point|string|() value = ()) returns ();
+}
 
-// Unknown type: RegClassArrayValue
+class PointArrayValue {
+    function init(Point[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegConfigValue
+class LineValue {
+    function init(Line|string|() value = ()) returns ();
+}
 
-// Unknown type: RegConfigArrayValue
+class LineArrayValue {
+    function init(Line|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegDictionaryValue
+class LineSegmentValue {
+    function init(LineSegment|string|() value = ()) returns ();
+}
 
-// Unknown type: RegDictionaryArrayValue
+class LineSegmentArrayValue {
+    function init(LineSegment|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegNamespaceValue
+class BoxValue {
+    function init(Box|string|() value = ()) returns ();
+}
 
-// Unknown type: RegNamespaceArrayValue
+class BoxArrayValue {
+    function init(Box|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegOperValue
+class PathValue {
+    function init(Path|Point[]|string|() value = ()) returns ();
+}
 
-// Unknown type: RegOperArrayValue
+class PathArrayValue {
+    function init(Path|()[]|Point[]|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegOperatorValue
+class PolygonValue {
+    function init(Point[]|string|() value = ()) returns ();
+}
 
-// Unknown type: RegOperatorArrayValue
+class PolygonArrayValue {
+    function init(Point[]|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegProcValue
+class CircleValue {
+    function init(Circle|string|() value = ()) returns ();
+}
 
-// Unknown type: RegProcArrayValue
+class CircleArrayValue {
+    function init(Circle|()[]|string|()[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: RegProcedureValue
+class UuidValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: RegProcedureArrayValue
+class UuidArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: RegRoleValue
+class TsVectorValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: RegRoleArrayValue
+class TsVectorArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: RegTypeValue
+class TsQueryValue {
+    function init(string|() value = ()) returns ();
+}
 
-// Unknown type: RegTypeArrayValue
+class TsQueryArrayValue {
+    function init((string?)[] value = []) returns ();
+}
 
-// Unknown type: PGXmlValue
+class JsonValue {
+    function init(json|string|() value = ()) returns ();
+}
 
-// Unknown type: PGXmlArrayValue
+class JsonArrayValue {
+    function init(json[]|(string?)[] value = <string?[]>[]) returns ();
+}
 
-// Unknown type: CustomTypeValue
+class JsonBinaryValue {
+    function init(json|string|() value = ()) returns ();
+}
 
-// Unknown type: EnumValue
+class JsonBinaryArrayValue {
+    function init(json[]|(string?)[] value = <string?[]>[]) returns ();
+}
 
+class JsonPathValue {
+    function init(string|() value = ()) returns ();
+}
+
+class JsonPathArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class IntervalValue {
+    function init(Interval|string|() value = ()) returns ();
+}
+
+class IntervalArrayValue {
+    function init(Interval|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class IntegerRangeValue {
+    function init(IntegerRange|string|() value = ()) returns ();
+}
+
+class IntegerRangeArrayValue {
+    function init(IntegerRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class LongRangeValue {
+    function init(LongRange|string|() value = ()) returns ();
+}
+
+class LongRangeArrayValue {
+    function init(LongRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class NumericRangeValue {
+    function init(NumericRange|string|() value = ()) returns ();
+}
+
+class NumericRangeArrayValue {
+    function init(NumericRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class TsRangeValue {
+    function init(TimestampRange|TimestampCivilRange|string|() value = ()) returns ();
+}
+
+class TsRangeArrayValue {
+    function init(TimestampRange|()[]|TimestampCivilRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class TsTzRangeValue {
+    function init(TimestamptzRange|TimestamptzCivilRange|string|() value = ()) returns ();
+}
+
+class TsTzRangeArrayValue {
+    function init(TimestamptzRange|()[]|TimestamptzCivilRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class DateRangeValue {
+    function init(DateRange|DateRecordRange|string|() value = ()) returns ();
+}
+
+class DateRangeArrayValue {
+    function init(DateRange|()[]|DateRecordRange|()[]|string|()[] value = <string?[]>[]) returns ();
+}
+
+class PglsnValue {
+    function init(string|() value = ()) returns ();
+}
+
+class PglsnArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class BitStringValue {
+    function init(string|() value = ()) returns ();
+}
+
+class BitStringArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class VarBitStringValue {
+    function init(string|() value = ()) returns ();
+}
+
+class VarBitStringArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class PGBitValue {
+    function init(boolean|string|() value = ()) returns ();
+}
+
+class PGBitArrayValue {
+    function init((boolean?)[]|(string?)[] value = <string?[]>[]) returns ();
+}
+
+class MoneyValue {
+    function init(decimal|float|string|() value = ()) returns ();
+}
+
+class MoneyArrayValue {
+    function init((decimal?)[]|(float?)[]|(string?)[] value = <string?[]>[]) returns ();
+}
+
+class RegClassValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegClassArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegConfigValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegConfigArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegDictionaryValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegDictionaryArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegNamespaceValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegNamespaceArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegOperValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegOperArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegOperatorValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegOperatorArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegProcValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegProcArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegProcedureValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegProcedureArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegRoleValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegRoleArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class RegTypeValue {
+    function init(string|() value = ()) returns ();
+}
+
+class RegTypeArrayValue {
+    function init((string?)[] value = []) returns ();
+}
+
+class PGXmlValue {
+    function init(string|xml|() value = ()) returns ();
+}
+
+class PGXmlArrayValue {
+    function init((string?)[]|(xml?)[] value = <string?[]>[]) returns ();
+}
+
+class CustomTypeValue {
+    function init(string sqlTypeName, CustomValues|() value = ()) returns ();
+}
+
+class EnumValue {
+    function init(string sqlTypeName, Enum|() value = ()) returns ();
+}
+
 // --- Client ---
 
 # PostgreSQL database client that enables interaction with PostgreSQL servers and supports standard SQL operations.
 client class Client {
-    function init(string host = "localhost", string|() username = "postgres", string|() password = (), string|() database = (), int port = 5432, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns ballerina/sql:1.19.0:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
+    function init(string host = "localhost", string|() username = "postgres", string|() password = (), string|() database = (), int port = 5432, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?; // Special Agent Note: ConnectionPool FROM ballerina/sql package
 
     # Executes a SQL query and returns multiple results as a stream.
     # 
-    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
+    remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>; // Special Agent Note: ParameterizedQuery FROM ballerina/sql package
 
     # Executes a SQL query that is expected to return a single row or value as the result.
     # 
@@ -1367,27 +1817,48 @@
     # Closes the PostgreSQL client and shuts down the connection pool.
     # The client should be closed only at the end of the application lifetime, or when performing graceful stops in a service.
     # 
-    remote function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
+    function close() returns sql:Error|(); // Special Agent Note: Error FROM ballerina/sql package
 }
 
 // --- Service ---
 
-service postgresql:Service on new postgresql:CdcListener(PostgresListenerConfiguration config = {database: {databaseName: "", username: "", password: ""}}) {
+service postgresql:Service on new postgresql:CdcListener(postgresql:PostgresListenerConfiguration config = {database: {databaseName: "", username: "", password: ""}}) {
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
 
     # Triggers when a monitored table is truncated
+    # + tableName - The name of the table which was truncated
+    # Required parameters: none — every parameter in the signature may be omitted.
+    # Optional parameters (may be omitted): tableName
     remote function onTruncate(string tableName) returns error?;
 
     # Triggers when an error occurs during event processing before mandatory functions are invoked
+    # + cdcError - The error occurred during message processing
     remote function onError(cdc:Error cdcError);
 }
`````

# data.csv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `data.csv` |
| **Old file** | `data.csv/old/ballerina_data.csv.bal.txt` |
| **New file** | `data.csv/new/ballerina_data.csv.bal.txt` |
| **Old lines** | 595 |
| **New lines** | 601 |
| **Lines added** | 15 |
| **Lines removed** | 9 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 8 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (2)

- `annotation Name`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 328–334 | 328–335 | Types | +2 | −1 |
| 2 | 419–443 | 420–444 | Types | +6 | −6 |
| 3 | 466–472 | 467–473 | Types | +1 | −1 |
| 4 | 592–595 | 593–601 | Functions | +6 | −1 |

---

## Unified diff

`````diff
--- data.csv/old/ballerina_data.csv.bal.txt	2026-08-12 23:21:51
+++ data.csv/new/ballerina_data.csv.bal.txt	2026-08-12 23:23:51
@@ -328,7 +328,8 @@
 # Represents a nil value as Ballerina nil value `()`.
 const string NIL = "()";
 
-// Unknown type: Error
+# Represents an error.
+type Error error;
 
 # Defines the name of the JSON Object key.
 # 
@@ -419,25 +420,25 @@
 
 type ParseOptions record {
     # The delimiter character used for separating fields in the data.
-    ballerina/lang.string:0.0.0:Char delimiter?;
+    string:Char delimiter?;
     # The character encoding of the data.
     string encoding?;
     # The locale used for parsing.
     string locale?;
     # The character used to enclose text fields.
-    ballerina/lang.string:0.0.0:Char textEnclosure?;
+    string:Char textEnclosure?;
     # The character used for escaping.
-    ballerina/lang.string:0.0.0:Char escapeChar?;
+    string:Char escapeChar?;
     # The line terminator(s) used in the data.
     "
 "|"
 "|LineTerminator[] lineTerminator?;
     # The value to represent nil.
-    ballerina/data.csv:0.10.0:NilValue? nilValue?;
+    NilValue? nilValue?;
     # The character used to indicate comments in the data.
-    ballerina/lang.string:0.0.0:Char comment?;
+    string:Char comment?;
     # Specifies whether the header is present and, if so, the number of header lines.
-    ballerina/lang.int:0.0.0:Unsigned32? header?;
+    int:Unsigned32? header?;
     # Custom headers for the data, if headers are absent.
     string[]? customHeadersIfHeadersAbsent?;
     record {|boolean nilAsOptionalField; boolean absentAsNilableType; anydata...;|}|false allowDataProjection?;
@@ -466,7 +467,7 @@
 type ParseListOptions record {
     # If `0`, all the source data will treat as data rows.
 Otherwise specify the header rows(Starts from 1) in the source data.
-    ballerina/lang.int:0.0.0:Unsigned32 headerRows?;
+    int:Unsigned32 headerRows?;
     # Specify the header names of the source data.
 This field will overwrite the header values in the header rows.
 This will be mandatory if the header row parameter is larger than one.
@@ -592,4 +593,9 @@
 # + options - Options to be used for filtering in the projection
 # + t - Target type (must be a record type or anydata[])
 # + return - On success, a stream of values belonging to the given target type, else returns an `csv:Error` value.
-function parseToStream(stream<byte[], error?> csvByteStream, ParseOptions options = {}, record {|anydata...;|}|anydata[] t = record {|anydata...;|}|anydata[]) returns stream<t, ballerina/data.csv:0.10.0:Error?>|Error;
+function parseToStream(stream<byte[], error?> csvByteStream, ParseOptions options = {}, record {|anydata...;|}|anydata[] t = record {|anydata...;|}|anydata[]) returns stream<t, Error?>|Error;
+
+// --- Annotations ---
+
+# The annotation is used to overwrite the existing record field name.
+public annotation NameConfig Name on record field;
`````

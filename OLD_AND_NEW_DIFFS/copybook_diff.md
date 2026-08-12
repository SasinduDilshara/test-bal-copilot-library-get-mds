# copybook — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `copybook` |
| **Old file** | `copybook/old/ballerinax_copybook.bal.txt` |
| **New file** | `copybook/new/ballerinax_copybook.bal.txt` |
| **Old lines** | 30 |
| **New lines** | 40 |
| **Lines added** | 12 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 3 | 3 |

### Declarations added (5)

- `class Converter`
- `function fromBytes`
- `function init`
- `function toBytes`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 19–25 | 19–26 | Types | +2 | −1 |
| 2 | 27–30 | 28–40 | Types | +10 | −1 |

---

## Unified diff

`````diff
--- copybook/old/ballerinax_copybook.bal.txt	2026-08-12 12:57:30
+++ copybook/new/ballerinax_copybook.bal.txt	2026-08-12 13:19:19
@@ -19,7 +19,8 @@
 # Represents the EBCDIC encoding
 const string EBCDIC = "EBCDIC";
 
-// Unknown type: Error
+# Represents copybook module related errors.
+type Error error;
 
 # Represents the encoding types used for the input or output byte arrays.
 enum Encoding {
@@ -27,4 +28,13 @@
     ASCII
 }
 
-// Unknown type: Converter
+# Initializes the converter with a schema.
+class Converter {
+    function init(string schemaFilePath) returns Error?;
+
+    # Converts the provided record or map<json> value to bytes.
+    function toBytes(record {|anydata...;|} input, string|() targetRecordName = (), Encoding encoding = "EBCDIC") returns byte[]|Error;
+
+    # Converts the given copybook bytes to a Ballerina record.
+    function fromBytes(byte[] bytes, string|() targetRecordName = (), Encoding encoding = "EBCDIC") returns map<json>|Error;
+}
`````

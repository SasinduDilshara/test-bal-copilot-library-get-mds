# serdes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `serdes` |
| **Old file** | `serdes/old/ballerina_serdes.bal.txt` |
| **New file** | `serdes/new/ballerina_serdes.bal.txt` |
| **Old lines** | 132 |
| **New lines** | 149 |
| **Lines added** | 19 |
| **Lines removed** | 2 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (5)

- `class Proto3Schema`
- `function deserialize`
- `function init`
- `function serialize`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 121–132 | 121–149 | Types | +19 | −2 |

---

## Unified diff

`````diff
--- serdes/old/ballerina_serdes.bal.txt	2026-08-12 23:21:51
+++ serdes/new/ballerina_serdes.bal.txt	2026-08-12 23:23:51
@@ -121,12 +121,29 @@
 
 # A Schema object that can be used to create custom serializers/deserializers.
 class Schema {
+
+    function serialize(anydata data) returns byte[]|Error;
+
+    function deserialize(byte[] encodedMessage, anydata T = <>) returns T|Error;
 }
 
-// Unknown type: Error
+# Represents any error related to Ballerina SerDes module
+type Error error;
 
-// Unknown type: Proto3Schema
+# Generates a schema for a given data type.
+# 
+class Proto3Schema {
+    function init(anydata ballerinaDataType) returns Error?;
 
+    # Serializes a given value.
+    # 
+    function serialize(anydata data) returns byte[]|Error;
+
+    # Deserializes a given array of bytes.
+    # 
+    function deserialize(byte[] encodedMessage, anydata T = anydata) returns T|Error;
+}
+
 // --- Functions ---
 
 function generateSchema(Schema serdes, anydata T) returns Error|();
`````

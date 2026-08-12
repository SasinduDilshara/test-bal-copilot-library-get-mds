# avro — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `avro` |
| **Old file** | `avro/old/ballerina_avro.bal.txt` |
| **New file** | `avro/new/ballerina_avro.bal.txt` |
| **Old lines** | 61 |
| **New lines** | 90 |
| **Lines added** | 31 |
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
| `// --- section ---` markers | 3 | 3 |

### Declarations added (5)

- `class Schema`
- `function fromAvro`
- `function init`
- `function toAvro`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 56–61 | 56–90 | END README | +31 | −2 |

---

## Unified diff

`````diff
--- avro/old/ballerina_avro.bal.txt	2026-08-12 23:21:51
+++ avro/new/ballerina_avro.bal.txt	2026-08-12 23:23:51
@@ -56,6 +56,35 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents any error related to Ballerina Avro module
+type Error error;
 
-// Unknown type: Schema
+# Initializes the Avro schema with the given schema definition.
+# 
+# ```ballerina
+# avro:Schema schema = check new(string `{"type": "int", "name" : "intValue", "namespace": "data" }`);
+# ```
+# 
+class Schema {
+    function init(string schema) returns Error?;
+
+    # Serializes the given data according to the Avro format.
+    # 
+    # ```ballerina
+    # avro:Schema schema = check new(string `{"type": "int", "name" : "data", "namespace": "example.avro" }`);
+    # int value = 5;
+    # byte[] serializedData = check schema.toAvro(value);
+    # ```
+    # 
+    function toAvro(anydata data) returns byte[]|Error;
+
+    # Deserializes the given Avro encoded message to the given data type.
+    # 
+    # ```ballerina
+    # avro:Schema schema = check new(string `{"type": "int", "name" : "data", "namespace": "example.avro" }`);
+    # byte[] data = [10] //Avro encoded message;
+    # int deserializedData = check schema.fromAvro(data);
+    # ```
+    # 
+    function fromAvro(byte[] data, anydata targetType = anydata) returns targetType|Error;
+}
`````

# data.yaml — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `data.yaml` |
| **Old file** | `data.yaml/old/ballerina_data.yaml.bal.txt` |
| **New file** | `data.yaml/new/ballerina_data.yaml.bal.txt` |
| **Old lines** | 191 |
| **New lines** | 198 |
| **Lines added** | 8 |
| **Lines removed** | 1 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (2)

- `annotation Name`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 127–133 | 127–135 | Types | +3 | −1 |
| 2 | 189–191 | 191–198 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- data.yaml/old/ballerina_data.yaml.bal.txt	2026-08-12 23:21:51
+++ data.yaml/new/ballerina_data.yaml.bal.txt	2026-08-12 23:23:51
@@ -127,7 +127,9 @@
     boolean flowStyle?;
 };
 
-// Unknown type: Error
+# Represents the error type of the ballerina/data.yaml module. This error type represents any error that can occur
+# during the execution of data.yaml APIs.
+type Error error;
 
 # Defines the name of the JSON Object key.
 
@@ -189,3 +191,8 @@
 # + config - Options used to get desired toString representation
 # + return - On success, returns to string value, else returns an `yaml:Error`
 function toYamlString(anydata yamlValue, WriteConfig config = {}) returns string|Error;
+
+// --- Annotations ---
+
+# The annotation is used to overwrite the existing record field name.
+public annotation NameConfig Name on record field;
`````

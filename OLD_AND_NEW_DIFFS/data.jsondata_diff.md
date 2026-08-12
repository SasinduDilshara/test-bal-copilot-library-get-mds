# data.jsondata — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `data.jsondata` |
| **Old file** | `data.jsondata/old/ballerina_data.jsondata.bal.txt` |
| **New file** | `data.jsondata/new/ballerina_data.jsondata.bal.txt` |
| **Old lines** | 307 |
| **New lines** | 314 |
| **Lines added** | 9 |
| **Lines removed** | 2 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (3)

- `annotation Name`
- `type Error`
- `type JsonPathValue`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 223–229 | 223–231 | END README | +3 | −1 |
| 2 | 243–249 | 245–251 | Types | +1 | −1 |
| 3 | 305–307 | 307–314 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- data.jsondata/old/ballerina_data.jsondata.bal.txt	2026-08-12 23:21:51
+++ data.jsondata/new/ballerina_data.jsondata.bal.txt	2026-08-12 23:23:51
@@ -223,7 +223,9 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents the error type of the ballerina/data.jsondata module. This error type represents any error that can occur
+# during the execution of jsondata APIs.
+type Error error;
 
 # Represent the options that can be used to modify the behaviour of the projection.
 # 
@@ -243,7 +245,7 @@
     string value;
 };
 
-// Unknown type: JsonPathValue
+type JsonPathValue json;
 
 class JsonPathRawTemplate {
 }
@@ -305,3 +307,8 @@
 # + query - JSON path expression
 # + return - extracted details as JSON value, a jsonpath:Error otherwise
 function read(json 'json, JsonPathRawTemplate query) returns json|Error;
+
+// --- Annotations ---
+
+# The annotation is used to overwrite the existing record field name.
+public annotation NameConfig Name on record field;
`````

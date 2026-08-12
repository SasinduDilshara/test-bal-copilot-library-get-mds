# constraint — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `constraint` |
| **Old file** | `constraint/old/ballerina_constraint.bal.txt` |
| **New file** | `constraint/new/ballerina_constraint.bal.txt` |
| **Old lines** | 257 |
| **New lines** | 290 |
| **Lines added** | 38 |
| **Lines removed** | 5 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (9)

- `annotation Array`
- `annotation Date`
- `annotation Float`
- `annotation Int`
- `annotation Number`
- `annotation String`
- `type Error`
- `type TypeConversionError`
- `type ValidationError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 207–213 | 207–213 | Types | +1 | −1 |
| 2 | 235–250 | 235–253 | Types | +7 | −4 |
| 3 | 255–257 | 258–290 | Functions | +30 | −0 |

---

## Unified diff

`````diff
--- constraint/old/ballerina_constraint.bal.txt	2026-08-12 23:21:51
+++ constraint/new/ballerina_constraint.bal.txt	2026-08-12 23:23:51
@@ -207,7 +207,7 @@
     # The inclusive upper bound of the number of characters of the constrained `string` type
     int|record {|int value; string message;|} maxLength?;
     # The regular expression to be matched with the constrained `string` type
-    ballerina/lang.string:0.0.0:RegExp|record {|ballerina/lang.string:0.0.0:RegExp value; string message;|} pattern?;
+    string:RegExp|record {|string:RegExp value; string message;|} pattern?;
 };
 
 # Represents the constraints associated with `anydata[]` type.
@@ -235,16 +235,19 @@
 
 type DateConstraints record {
     # date option to be validated
-    ballerina/constraint:1.7.0:DateOption|record {|ballerina/constraint:1.7.0:DateOption value; string message;|} option?;
+    DateOption|record {|DateOption value; string message;|} option?;
     # The message to be returned in case of the constraint violation
     string message?;
 };
 
-// Unknown type: Error
+# Represents the generic error type of the module.
+type Error error;
 
-// Unknown type: ValidationError
+# Represents the errors occurs during constraint validations.
+type ValidationError error;
 
-// Unknown type: TypeConversionError
+# Represents the errors occurs during the type conversion.
+type TypeConversionError error;
 
 // --- Functions ---
 
@@ -255,3 +258,33 @@
 # + td - The type descriptor of the value to be constrained
 # + return - The type descriptor of the value which is validated or else an `constraint:Error` in case of an error
 function validate(anydata value, anydata td = anydata) returns td|Error;
+
+// --- Annotations ---
+
+# The annotation, which is used for the constraints of the `int` type.
+public annotation IntConstraints Int on type, record field;
+
+# The annotation, which is used for the constraints of the `float` type.
+public annotation FloatConstraints Float on type, record field;
+
+# The annotation, which is used for the constraints of the `int`, `float`, and `decimal` types.
+public annotation NumberConstraints Number on type, record field;
+
+# The annotation, which is used for the constraints of the `string` type.
+public annotation StringConstraints String on type, record field;
+
+# The annotation, which is used for the constraints of the `anydata[]` type.
+public annotation ArrayConstraints Array on type, record field;
+
+# The annotation, which is used for the constraints of the `Date` type, which is structurally equivalent
+# to the following record:
+# ```ballerina
+# type Date record {
+#    int year;
+#    int month;
+#    int day;
+# };
+# ```
+# This annotation will enable validation on the date fields in the record. Additionally,
+# the `option` field can be used to validate the date against the provided option.
+public annotation DateConstraints Date on type, record field;
`````

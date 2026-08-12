# log — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `log` |
| **Old file** | `log/old/ballerina_log.bal.txt` |
| **New file** | `log/new/ballerina_log.bal.txt` |
| **Old lines** | 628 |
| **New lines** | 676 |
| **Lines added** | 64 |
| **Lines removed** | 16 |
| **Hunks** | 11 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 7 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (9)

- `annotation Sensitive`
- `function getById`
- `function getIds`
- `function getLevel`
- `function setLevel`
- `function withContext`
- `type Error`
- `type ReplacementFunction`
- `type Valuer`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 332–341 | 332–375 | Types | +35 | −1 |
| 2 | 346–352 | 380–389 | Types | +4 | −1 |
| 3 | 355–361 | 392–398 | Types | +1 | −1 |
| 4 | 463–469 | 500–506 | Types | +1 | −1 |
| 5 | 485–502 | 522–548 | Types | +12 | −3 |
| 6 | 507–513 | 553–559 | Types | +1 | −1 |
| 7 | 541–549 | 587–594 | Functions | +1 | −2 |
| 8 | 554–562 | 599–606 | Functions | +1 | −2 |
| 9 | 566–574 | 610–617 | Functions | +1 | −2 |
| 10 | 578–586 | 621–628 | Functions | +1 | −2 |
| 11 | 626–628 | 668–676 | Functions | +6 | −0 |

---

## Unified diff

`````diff
--- log/old/ballerina_log.bal.txt	2026-08-12 23:21:51
+++ log/new/ballerina_log.bal.txt	2026-08-12 23:23:51
@@ -332,10 +332,44 @@
 # Exclude the field from log output
 const string EXCLUDE = "EXCLUDE";
 
-// Unknown type: Error
+# Represents errors specific to the Log module.
+type Error error;
 
 # Logger object type defines an interface for logging messages
 class Logger {
+
+    # Prints debug logs.
+    # 
+    function printDebug(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
+
+    # Prints info logs.
+    # 
+    function printInfo(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
+
+    # Prints warn logs.
+    # 
+    function printWarn(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
+
+    # Prints error logs.
+    # 
+    function printError(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
+
+    # Creates a new child/derived logger with the given key-values.
+    # 
+    function withContext(KeyValues keyValues) returns Logger|error;
+
+    # Returns the effective log level of this logger.
+    # For root and custom loggers, returns the explicitly set level.
+    # For child loggers (created via `withContext`), returns the inherited level from the parent logger.
+    # 
+    function getLevel() returns Level;
+
+    # Sets the log level of this logger at runtime.
+    # This is supported on root loggers, module loggers, and loggers created via `fromConfig`.
+    # Child loggers (created via `withContext`) do not support this operation and will return an error.
+    # To change a child logger's effective level, set the level on its parent logger instead.
+    # 
+    function setLevel(Level level) returns error?;
 }
 
 # Log level types.
@@ -346,7 +380,10 @@
     DEBUG
 }
 
-// Unknown type: Valuer
+# A function that returns a value of type `anydata`.
+# Useful in scenarios where computation is required to retrieve the value.
+# This function is executed only if the specific log level is enabled.
+type Valuer function () returns anydata;
 
 # Raw templates for logging.
 # 
@@ -355,7 +392,7 @@
 }
 
 # A value that can be of type `anydata`, a function pointer, or a raw template.
-type Value anydata|ballerina/log:2.17.0:Valuer|ballerina/log:2.17.0:PrintableRawTemplate;
+type Value anydata|Valuer|PrintableRawTemplate;
 
 # Key-value pairs to be displayed in the log.
 # 
@@ -463,7 +500,7 @@
 };
 
 # Log output destination.
-type OutputDestination ballerina/log:2.17.0:StandardDestination|ballerina/log:2.17.0:FileOutputDestination;
+type OutputDestination StandardDestination|FileOutputDestination;
 
 # File opening options for writing.
 # 
@@ -485,18 +522,27 @@
     # Log level to use. Default is the logger level configured in the module level
     Level level?;
     # List of destinations to log to. Default is the logger destinations configured in the module level
-    ballerina/log:2.17.0:OutputDestination[] & readonly destinations?;
+    OutputDestination[] & readonly destinations?;
     # Additional key-value pairs to include in the log messages. Default is the key-values configured in the module level
-    ballerina/log:2.17.0:AnydataKeyValues & readonly keyValues?;
+    AnydataKeyValues & readonly keyValues?;
     # Enable sensitive data masking. Default is the module level configuration
     boolean enableSensitiveDataMasking?;
 };
 
 # Provides access to the logger registry for discovering and managing registered loggers.
 class LoggerRegistry {
+
+    # Returns the IDs of all registered loggers.
+    # 
+    function getIds() returns string[];
+
+    # Returns a logger by its registered ID.
+    # 
+    function getById(string id) returns Logger|();
 }
 
-// Unknown type: ReplacementFunction
+# Replacement function type for sensitive data masking
+type ReplacementFunction function (string input) returns string;
 
 # Replacement strategy for sensitive data
 
@@ -507,7 +553,7 @@
 };
 
 # Masking strategy for sensitive data
-type MaskingStrategy "EXCLUDE"|ballerina/log:2.17.0:Replacement;
+type MaskingStrategy "EXCLUDE"|Replacement;
 
 # Represents sensitive data with a masking strategy
 
@@ -541,9 +587,8 @@
 # + msg - The message to be logged
 # + 'error - The error struct to be logged
 # + stackTrace - The error stack trace to be logged
-# + Additional Values - Capture key value pairs
 # + keyValues - The key-value pairs to be logged
-function printDebug(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), Value Additional Values, KeyValues keyValues) returns ();
+function printDebug(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
 
 # Prints error logs.
 # ```ballerina
@@ -554,9 +599,8 @@
 # + msg - The message to be logged
 # + 'error - The error struct to be logged
 # + stackTrace - The error stack trace to be logged
-# + Additional Values - Capture key value pairs
 # + keyValues - The key-value pairs to be logged
-function printError(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), Value Additional Values, KeyValues keyValues) returns ();
+function printError(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
 
 # Prints info logs.
 # ```ballerina
@@ -566,9 +610,8 @@
 # + msg - The message to be logged
 # + 'error - The error struct to be logged
 # + stackTrace - The error stack trace to be logged
-# + Additional Values - Capture key value pairs
 # + keyValues - The key-value pairs to be logged
-function printInfo(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), Value Additional Values, KeyValues keyValues) returns ();
+function printInfo(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
 
 # Prints warn logs.
 # ```ballerina
@@ -578,9 +621,8 @@
 # + msg - The message to be logged
 # + 'error - The error struct to be logged
 # + stackTrace - The error stack trace to be logged
-# + Additional Values - Capture key value pairs
 # + keyValues - The key-value pairs to be logged
-function printWarn(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), Value Additional Values, KeyValues keyValues) returns ();
+function printWarn(string|PrintableRawTemplate msg, error|() 'error = (), error:StackFrame[]|() stackTrace = (), KeyValues keyValues) returns ();
 
 # Sets the log output to a file. All subsequent logs of the entire application will be written to this file.
 # ```ballerina
@@ -626,3 +668,9 @@
 # + data - The data to be masked
 # + return - The masked string representation of the data
 function toMaskedString(anydata data) returns string;
+
+// --- Annotations ---
+
+# Marks a record field or type as sensitive, excluding it from log output
+# The default strategy is to exclude the field from log output
+public annotation SensitiveConfig Sensitive on record field;
`````

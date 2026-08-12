# os — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `os` |
| **Old file** | `os/old/ballerina_os.bal.txt` |
| **New file** | `os/new/ballerina_os.bal.txt` |
| **Old lines** | 102 |
| **New lines** | 129 |
| **Lines added** | 32 |
| **Lines removed** | 5 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `class Process`
- `function exit`
- `function output`
- `function waitForExit`
- `type Error`
- `type ProcessExecError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 28–39 | 28–67 | Types | +31 | −3 |
| 2 | 96–102 | 124–129 | Functions | +1 | −2 |

---

## Unified diff

`````diff
--- os/old/ballerina_os.bal.txt	2026-08-12 23:21:51
+++ os/new/ballerina_os.bal.txt	2026-08-12 23:23:51
@@ -28,12 +28,40 @@
     never command?;
 };
 
-// Unknown type: Error
+# Represents OS module related errors.
+type Error error;
 
-// Unknown type: ProcessExecError
+# Process Execution error that returns when the os:Exec function fails.
+type ProcessExecError error;
 
-// Unknown type: Process
+# This object contains information on a process being created from Ballerina.
+# This is returned from the `exec` function in the `os` module.
+class Process {
 
+    # Waits for the process to finish its work and exit. 
+    # This will return 0 if successful, or a different value during failure depending on the operating system.
+    # ```ballerina
+    # int|os:Error exitCode = process.waitForExit();
+    # ```
+    # 
+    function waitForExit() returns int|Error;
+
+    # Returns the standard output as default. Option provided to return standard error by providing file descriptor.
+    # If the process was not finished and exited explicitly by running process.waitForExit(), then process.output() will finish the work and exit and return the output. 
+    # ```ballerina
+    # byte[]|os:Error err = process.output(io:stderr);
+    # ```
+    # 
+    function output(io:FileOutputStream fileOutputStream = 1) returns byte[]|Error; // Special Agent Note: FileOutputStream FROM ballerina/io package
+
+    # Terminates the process.
+    # ```ballerina
+    # process.exit();
+    # ```
+    # 
+    function exit() returns ();
+}
+
 // --- Functions ---
 
 # Returns the environment variable value associated with the provided name.
@@ -96,7 +124,6 @@
 # ```
 # 
 # + command - The command to be executed
-# + Additional Values - Capture key value pairs
 # + envProperties - The environment properties
 # + return - Process object in success, or an Error if a failure occurs
-function exec(Command command, anydata Additional Values, EnvProperties envProperties) returns Process|Error;
+function exec(Command command, EnvProperties envProperties) returns Process|Error;
`````

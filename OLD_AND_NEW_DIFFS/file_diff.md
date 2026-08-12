# file — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `file` |
| **Old file** | `file/old/ballerina_file.bal.txt` |
| **New file** | `file/new/ballerina_file.bal.txt` |
| **Old lines** | 416 |
| **New lines** | 456 |
| **Lines added** | 60 |
| **Lines removed** | 20 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 14 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (20)

- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function init`
- `type Error`
- `type FileNotFoundError`
- `type FileSystemError`
- `type GenericError`
- `type IOError`
- `type InvalidOperationError`
- `type InvalidPathError`
- `type InvalidPatternError`
- `type NotLinkError`
- `type PermissionError`
- `type RelativePathError`
- `type SecurityError`
- `type UNCPathError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 131–161 | 131–174 | Types | +26 | −13 |
| 2 | 186–193 | 199–230 | Types | +25 | −1 |
| 3 | 247–253 | 284–290 | Functions | +1 | −1 |
| 4 | 257–263 | 294–300 | Functions | +1 | −1 |
| 5 | 404–416 | 441–456 | Functions | +7 | −4 |

---

## Unified diff

`````diff
--- file/old/ballerina_file.bal.txt	2026-08-12 23:21:51
+++ file/new/ballerina_file.bal.txt	2026-08-12 23:23:51
@@ -131,31 +131,44 @@
 class Service {
 }
 
-// Unknown type: Error
+# Represents file system related errors.
+type Error error;
 
-// Unknown type: InvalidOperationError
+# Represents an error that occurs when a file system operation is denied due to invalidity.
+type InvalidOperationError error;
 
-// Unknown type: PermissionError
+# Represents an error that occurs when a file system operation is denied, due to the absence of file permission.
+type PermissionError error;
 
-// Unknown type: FileSystemError
+# Represents an error that occurs when a file system operation fails.
+type FileSystemError error;
 
-// Unknown type: FileNotFoundError
+# Represents an error, which occurs when the file/directory does not exist in the given file path.
+type FileNotFoundError error;
 
-// Unknown type: NotLinkError
+# Represents an error, which occurs when the file in the given file path is not a symbolic link.
+type NotLinkError error;
 
-// Unknown type: IOError
+# Represents an IO error, which occurs when trying to access the file in the given file path.
+type IOError error;
 
-// Unknown type: SecurityError
+# Represents a security error, which occurs when trying to access the file in the given file path.
+type SecurityError error;
 
-// Unknown type: InvalidPathError
+# Represents an error, which occurs when the given file path is invalid.
+type InvalidPathError error;
 
-// Unknown type: InvalidPatternError
+# Represents an error, which occurs when the given pattern is not a valid file path pattern.
+type InvalidPatternError error;
 
-// Unknown type: RelativePathError
+# Represents an error, which occurs when the given target file path cannot be derived relative to the base file path.
+type RelativePathError error;
 
-// Unknown type: UNCPathError
+# Represents an error, which occurs in the UNC path.
+type UNCPathError error;
 
-// Unknown type: GenericError
+# Represents a generic error for the file path.
+type GenericError error;
 
 # Metadata record contains metadata information of a file.
 # This record is returned by getMetaData function.
@@ -186,8 +199,32 @@
     boolean recursive?;
 };
 
-// Unknown type: Listener
+# Creates a new Directory listener.
+# 
+class Listener {
+    function init(string path = "", boolean recursive = false, ListenerConfig listenerConfig) returns error?;
 
+    # Starts the `file:Listener`.
+    # 
+    function 'start() returns error?;
+
+    # Stops the `file:Listener` gracefully.
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the `file:Listener` forcefully.
+    # 
+    function immediateStop() returns error?;
+
+    # Binds a service to the `file:Listener`.
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Stops listening to the directory and detaches the service from the `file:Listener`.
+    # 
+    function detach(Service s) returns error?;
+}
+
 // --- Functions ---
 
 # Returns the current working directory.
@@ -247,7 +284,7 @@
 # 
 # + path - String value of the file path.
 # + return - The `MetaData` instance with the file metadata or else a `file:Error`
-function getMetaData(string path) returns ballerina/file:1.13.0:MetaData & readonly|Error;
+function getMetaData(string path) returns MetaData & readonly|Error;
 
 # Reads the directory and returns a list of metadata of files and directories
 # inside the specified directory.
@@ -257,7 +294,7 @@
 # 
 # + path - String value of the directory path
 # + return - The `MetaData` array or else a `file:Error` if there is an error
-function readDir(string path) returns ballerina/file:1.13.0:MetaData[] & readonly|Error;
+function readDir(string path) returns MetaData[] & readonly|Error;
 
 # Copy the file/directory in the old path to the new path.
 # ```ballerina
@@ -404,13 +441,16 @@
 
 // --- Service ---
 
-service file:Service on new file:Listener(ListenerConfig listenerConfig = {path: ""}) {
+service file:Service on new file:Listener(file:ListenerConfig listenerConfig = {path: ""}) {
     # The `onCreate` remote method will be triggered when a file is created in the specified directory
-    remote function onCreate(FileEvent event) returns error?;
+    # + event - The File event
+    remote function onCreate(file:FileEvent event) returns error?;
 
     # The `onDelete` remote method will be triggered when a file is deleted in the specified directory
-    remote function onDelete(FileEvent event) returns error?;
+    # + event - The File event
+    remote function onDelete(file:FileEvent event) returns error?;
 
     # The `onModify` remote method will be triggered when a file is modified in the specified directory
-    remote function onModify(FileEvent event) returns error?;
+    # + event - The File event
+    remote function onModify(file:FileEvent event) returns error?;
 }
`````

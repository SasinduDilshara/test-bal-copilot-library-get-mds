# task — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `task` |
| **Old file** | `task/old/ballerina_task.bal.txt` |
| **New file** | `task/new/ballerina_task.bal.txt` |
| **Old lines** | 448 |
| **New lines** | 477 |
| **Lines added** | 33 |
| **Lines removed** | 4 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (9)

- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function execute`
- `function gracefulStop`
- `function immediateStop`
- `function init`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 238–244 | 238–244 | Types | +1 | −1 |
| 2 | 340–351 | 340–380 | Types | +32 | −3 |

---

## Unified diff

`````diff
--- task/old/ballerina_task.bal.txt	2026-08-12 23:21:51
+++ task/new/ballerina_task.bal.txt	2026-08-12 23:23:51
@@ -238,7 +238,7 @@
 };
 
 # Represents the configuration required to connect to a database related to task coordination.
-type DatabaseConfig ballerina/task:2.11.2:MysqlConfig|ballerina/task:2.11.2:PostgresqlConfig;
+type DatabaseConfig MysqlConfig|PostgresqlConfig;
 
 # Represents the configuration required for task coordination.
 # 
@@ -340,12 +340,41 @@
 
 # The Ballerina Job object provides the abstraction for a job instance, which schedules to execute periodically.
 class Job {
-}
 
-// Unknown type: Error
+    # Executes by the Scheduler when the scheduled trigger fires.
+    function execute() returns ();
+}
 
-// Unknown type: Listener
+# Represents the error type of the `ballerina/task` module. This error type represents any error that can occur during
+# the execution of the task APIs.
+type Error error;
 
+# Initializes the task 'listener.
+# 
+class Listener {
+    function init(TriggerConfiguration trigger = {interval: 0.0d}, WarmBackupConfig|() warmBackupConfig = (), ListenerConfiguration config) returns Error?;
+
+    # Attaches a service to the 'listener.
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns Error|();
+
+    # Detaches a service from the 'listener.
+    # 
+    function detach(Service s) returns Error|();
+
+    # Starts the 'listener.
+    # 
+    function 'start() returns Error|();
+
+    # Stops the 'listener gracefully.
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the 'listener immediately.
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Functions ---
 
 # Gets time in milliseconds of the given `time:Civil`.
`````

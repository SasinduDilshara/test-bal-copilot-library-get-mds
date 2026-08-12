# observe — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `observe` |
| **Old file** | `observe/old/ballerina_observe.bal.txt` |
| **New file** | `observe/new/ballerina_observe.bal.txt` |
| **Old lines** | 508 |
| **New lines** | 570 |
| **Lines added** | 64 |
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
| `// --- section ---` markers | 4 | 5 |

### Declarations added (12)

- `annotation on`
- `class Counter`
- `class Gauge`
- `function decrement`
- `function getSnapshot`
- `function getValue`
- `function increment`
- `function init`
- `function register`
- `function reset`
- `function setValue`
- `function unregister`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 400–409 | 400–464 | Types | +57 | −2 |
| 2 | 506–508 | 561–570 | Functions | +7 | −0 |

---

## Unified diff

`````diff
--- observe/old/ballerina_observe.bal.txt	2026-08-12 23:21:51
+++ observe/new/ballerina_observe.bal.txt	2026-08-12 23:23:51
@@ -400,10 +400,65 @@
     int buckets;
 };
 
-// Unknown type: Counter
+# This instantiates the Counter object. Name field is mandatory, and description and tags fields
+# are optional and have its own default values when no params are passed.
+# 
+class Counter {
+    function init(string name, string|() desc = "", map<string>|() tags = ()) returns ();
 
-// Unknown type: Gauge
+    # Register the counter metric instance with the Metric Registry.
+    # 
+    function register() returns error?;
+
+    # Unregister the counter metric instance with the Metric Registry.
+    function unregister() returns ();
+
+    # Increment the counter's value by an amount.
+    # 
+    function increment(int amount = 0) returns ();
+
+    # Resets the counter's value to zero.
+    function reset() returns ();
+
+    # Retrieves the counter's current value.
+    # 
+    function getValue() returns int;
+}
+
+# This instantiates the Gauge object. Name field is mandatory, and description, tags, and statitics config fields
+# are optional and have its own default values when no params are passed.
+# 
+class Gauge {
+    function init(string name, string|() desc = "", map<string>|() tags = (), StatisticConfig[]|() statisticConfig = ()) returns ();
+
+    # Register the gauge metric instance with the Metric Registry.
+    # 
+    function register() returns error?;
 
+    # Unregister the counter metric instance with the Metric Registry.
+    function unregister() returns ();
+
+    # Increment the gauge's value by an amount.
+    # 
+    function increment(float amount = 0.0) returns ();
+
+    # Decrement the gauge's value by an amount.
+    # 
+    function decrement(float amount = 0.0) returns ();
+
+    # Sets the instantaneous value for gauge.
+    # 
+    function setValue(float amount) returns ();
+
+    # Retrieves the gauge's current value.
+    # 
+    function getValue() returns float;
+
+    # Retrieves statistics snapshots based on the statistics configs of the gauge.
+    # 
+    function getSnapshot() returns Snapshot[]|();
+}
+
 // --- Functions ---
 
 # Check whether observability is enabled.
@@ -506,3 +561,10 @@
 # + tags - The key/value pair tags associated with the metric that should be looked up
 # + return - The metric instance
 function lookupMetric(string name, map<string>|() tags = ()) returns Counter|Gauge|();
+
+// --- Annotations ---
+
+# This is used for making a function observable.
+# Can be applied to functions which are not observable by default to make them observable.
+# 
+public annotation Observable on function;
`````

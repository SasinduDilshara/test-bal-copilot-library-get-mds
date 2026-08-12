# aws.lambda — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.lambda` |
| **Old file** | `aws.lambda/old/ballerinax_aws.lambda.bal.txt` |
| **New file** | `aws.lambda/new/ballerinax_aws.lambda.bal.txt` |
| **Old lines** | 343 |
| **New lines** | 365 |
| **Lines added** | 23 |
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

### Declarations added (8)

- `annotation on`
- `class Context`
- `function getDeadlineMs`
- `function getInvokedFunctionArn`
- `function getRemainingExecutionTime`
- `function getRequestId`
- `function getTraceId`
- `function init`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 25–32 | 25–49 | END README | +18 | −1 |
| 2 | 341–343 | 358–365 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- aws.lambda/old/ballerinax_aws.lambda.bal.txt	2026-08-12 12:57:30
+++ aws.lambda/new/ballerinax_aws.lambda.bal.txt	2026-08-12 13:19:19
@@ -25,8 +25,25 @@
 
 // --- Types ---
 
-// Unknown type: Context
+class Context {
+    function init(string requestId, int deadlineMs, string invokedFunctionArn, string traceId) returns ();
+
+    # Returns the unique id for this request.
+    function getRequestId() returns string;
+
+    # Returns the request execution deadline in milliseconds from the epoch.
+    function getDeadlineMs() returns int;
+
+    # Returns the ARN of the function being invoked.
+    function getInvokedFunctionArn() returns string;
+
+    # Returns the trace id for this request
+    function getTraceId() returns string;
 
+    # Returns the remaining execution time for this request in milliseconds
+    function getRemainingExecutionTime() returns int;
+}
+
 # Represents the details of the identity related to the S3 service.
 # 
 
@@ -341,3 +358,8 @@
 
 # Process and excute the handler.  
 function __process() returns ();
+
+// --- Annotations ---
+
+# The annotation, which is used to mark the function as an AWS Lambda function.
+public annotation Function on function;
`````

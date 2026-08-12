# azure.functions — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `azure.functions` |
| **Old file** | `azure.functions/old/ballerinax_azure.functions.bal.txt` |
| **New file** | `azure.functions/new/ballerinax_azure.functions.bal.txt` |
| **Old lines** | 231 |
| **New lines** | 338 |
| **Lines added** | 119 |
| **Lines removed** | 12 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 11 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 3 | 4 |

### Declarations added (27)

- `annotation BindingName`
- `annotation BlobInput`
- `annotation BlobOutput`
- `annotation CosmosDBInput`
- `annotation CosmosDBOutput`
- `annotation Function`
- `annotation Header`
- `annotation QueueOutput`
- `annotation TwilioSmsOutput`
- `annotation on`
- `class BlobListener`
- `class CosmosDBListener`
- `class HttpListener`
- `class QueueListener`
- `class TimerListener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function init`
- `type Error`
- `type FunctionNotFoundError`
- `type HeaderNotFoundError`
- `type InvalidPayloadError`
- `type PayloadNotFoundError`
- `type UnsupportedTypeError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 161–177 | 161–177 | Types | +6 | −6 |
| 2 | 218–231 | 218–338 | Types | +113 | −6 |

---

## Unified diff

`````diff
--- azure.functions/old/ballerinax_azure.functions.bal.txt	2026-08-12 12:57:30
+++ azure.functions/new/ballerinax_azure.functions.bal.txt	2026-08-12 13:19:19
@@ -161,17 +161,17 @@
     string name?;
 };
 
-// Unknown type: Error
+type Error error;
 
-// Unknown type: FunctionNotFoundError
+type FunctionNotFoundError error;
 
-// Unknown type: PayloadNotFoundError
+type PayloadNotFoundError error;
 
-// Unknown type: InvalidPayloadError
+type InvalidPayloadError error;
 
-// Unknown type: HeaderNotFoundError
+type HeaderNotFoundError error;
 
-// Unknown type: UnsupportedTypeError
+type UnsupportedTypeError error;
 
 class HttpService {
 }
@@ -218,14 +218,121 @@
 class BlobService {
 }
 
-type RemoteService ballerinax/azure.functions:4.2.0:QueueService|ballerinax/azure.functions:4.2.0:CosmosService|ballerinax/azure.functions:4.2.0:TimerService|ballerinax/azure.functions:4.2.0:BlobService;
+type RemoteService QueueService|CosmosService|TimerService|BlobService;
 
-// Unknown type: BlobListener
+class BlobListener {
+    function init() returns error?;
 
-// Unknown type: CosmosDBListener
+    function attach(BlobService svc, string[]|string|() name = ()) returns error?;
 
-// Unknown type: HttpListener
+    function detach(BlobService svc) returns error?;
 
-// Unknown type: QueueListener
+    function 'start() returns error?;
 
-// Unknown type: TimerListener
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+class CosmosDBListener {
+    function init() returns error?;
+
+    function attach(CosmosService svc, string[]|string|() name = ()) returns error?;
+
+    function detach(CosmosService svc) returns error?;
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+class HttpListener {
+    function init() returns error?;
+
+    function attach(HttpService svc, string[]|string|() name = ()) returns error?;
+
+    function detach(HttpService svc) returns error?;
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+class QueueListener {
+    function init() returns error?;
+
+    function attach(QueueService svc, string[]|string|() name = ()) returns error?;
+
+    function detach(QueueService svc) returns error?;
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+class TimerListener {
+    function init() returns error?;
+
+    function attach(TimerService svc, string[]|string|() name = ()) returns error?;
+
+    function detach(TimerService svc) returns error?;
+
+    function 'start() returns error?;
+
+    function gracefulStop() returns error?;
+
+    function immediateStop() returns error?;
+}
+
+// --- Annotations ---
+
+public annotation Payload on parameter, return;
+
+public annotation FunctionConfiguration Function on function, return;
+
+public const annotation HTTPTriggerConfiguration HttpTrigger on service, source listener;
+
+# The annotation which is used to define the Header resource signature parameter.
+public annotation HttpHeader Header on parameter;
+
+# @azurefunctions:HttpOutput annotation
+public annotation HttpOutput on return, field;
+
+# @azurefunctions:QueueOutput annotation.
+public annotation QueueConfiguration QueueOutput on return, field;
+
+# @azurefunctions:QueueOutput annotation.
+public const annotation QueueConfiguration QueueTrigger on service, source listener;
+
+# @azurefunctions:TimerTrigger annotation.
+public const annotation TimerTriggerConfiguration TimerTrigger on service, source listener;
+
+# @azurefunctions:BlobTrigger annotation.
+public const annotation BlobConfiguration BlobTrigger on service, source listener;
+
+# @azurefunctions:BlobInput annotation.
+public annotation BlobConfiguration BlobInput on parameter;
+
+# @azurefunctions:BlobOutput annotation.
+public annotation BlobConfiguration BlobOutput on return, field;
+
+# @azurefunctions:CosmosDBTrigger annotation.
+public const annotation CosmosDBTriggerConfiguration CosmosDBTrigger on service, source listener;
+
+# @azurefunctions:CosmosDBInput annotation.
+public annotation CosmosDBInputConfiguration CosmosDBInput on parameter;
+
+# @azurefunctions:CosmosDBOutput annotation.
+public annotation CosmosDBOutputConfiguration CosmosDBOutput on return, field;
+
+# @azurefunctions:TwilioSmsOutput annotation.
+public annotation TwilioSmsConfiguration TwilioSmsOutput on return, field;
+
+# @azurefunctions:BindingName annotation.
+public annotation BindingNameConfiguration BindingName on parameter;
`````

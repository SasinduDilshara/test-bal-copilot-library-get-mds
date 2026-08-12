# gcloud.pubsub — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `gcloud.pubsub` |
| **Old file** | `gcloud.pubsub/old/ballerinax_gcloud.pubsub.bal.txt` |
| **New file** | `gcloud.pubsub/new/ballerinax_gcloud.pubsub.bal.txt` |
| **Old lines** | 347 |
| **New lines** | 394 |
| **Lines added** | 51 |
| **Lines removed** | 4 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (8)

- `annotation ServiceConfig`
- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 230–236 | 230–237 | Types | +2 | −1 |
| 2 | 297–309 | 298–351 | Types | +43 | −2 |
| 3 | 322–328 | 364–370 | Client | +1 | −1 |
| 4 | 345–347 | 387–394 | Client | +5 | −0 |

---

## Unified diff

`````diff
--- gcloud.pubsub/old/ballerinax_gcloud.pubsub.bal.txt	2026-08-12 12:57:30
+++ gcloud.pubsub/new/ballerinax_gcloud.pubsub.bal.txt	2026-08-12 13:19:19
@@ -230,7 +230,8 @@
 class Service {
 }
 
-// Unknown type: Error
+# Represents Google Cloud Pub/Sub module related errors.
+type Error error;
 
 # Represents credentials for authenticating with Google Cloud Pub/Sub.
 # 
@@ -297,13 +298,54 @@
     string orderingKey?;
 };
 
-// Unknown type: Listener
+# Initializes a Listener object with the given subscription and configuration.
+# ```ballerina
+# pubsub:Listener pubsubListener = check new("my-subscription", projectId = "my-project");
+# ```
+# 
+class Listener {
+    function init(string subscriptionName, string projectId = "", Credentials credentials = {}, ListenerConfiguration listenerConfig) returns Error?;
 
+    # Attaches the service to the `pubsub:Listener` endpoint.
+    # ```ballerina
+    # check pubsubListener.attach(service);
+    # ```
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Starts consuming messages on the attached service.
+    # ```ballerina
+    # check pubsubListener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Detaches a service from the `pubsub:Listener` endpoint.
+    # ```ballerina
+    # check pubsubListener.detach(service);
+    # ```
+    # 
+    function detach(Service s) returns error?;
+
+    # Stops consuming messages and gracefully shuts down the subscriber.
+    # ```ballerina
+    # check pubsubListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Immediately stops consuming messages and terminates the subscriber.
+    # ```ballerina
+    # check pubsubListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+}
+
 // --- Client ---
 
 # Provides functionality to acknowledge or reject messages received by the listener service.
 client class Caller {
-    function init() returns pubsub:pubsub:Caller;
 
     # Acknowledges the received message.
     # ```ballerina
@@ -322,7 +364,7 @@
 
 # Represents a Google Cloud Pub/Sub publisher endpoint.
 client class Publisher {
-    function init(string topicName, string projectId = "", Credentials credentials = {}, boolean enableBatching = true, BatchSettings batchSettings = {}, boolean enableMessageOrdering = false, PublisherConfiguration config) returns ballerinax/gcloud.pubsub:0.1.1:Error?;
+    function init(string topicName, string projectId = "", Credentials credentials = {}, boolean enableBatching = true, BatchSettings batchSettings = {}, boolean enableMessageOrdering = false, PublisherConfiguration config) returns Error?;
 
     # Publishes a message to the topic.
     # ```ballerina
@@ -345,3 +387,8 @@
     # 
     remote function close() returns Error|();
 }
+
+// --- Annotations ---
+
+# The annotation to configure the Pub/Sub service.
+public annotation PubSubServiceConfig ServiceConfig on service, class;
`````

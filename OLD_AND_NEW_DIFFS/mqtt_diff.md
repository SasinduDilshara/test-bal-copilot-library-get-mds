# mqtt — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mqtt` |
| **Old file** | `mqtt/old/ballerina_mqtt.bal.txt` |
| **New file** | `mqtt/new/ballerina_mqtt.bal.txt` |
| **Old lines** | 308 |
| **New lines** | 351 |
| **Lines added** | 50 |
| **Lines removed** | 7 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (7)

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
| 1 | 83–89 | 83–90 | Types | +2 | −1 |
| 2 | 158–164 | 159–165 | Types | +1 | −1 |
| 3 | 223–235 | 224–277 | Types | +43 | −2 |
| 4 | 248–254 | 290–296 | Client | +1 | −1 |
| 5 | 302–308 | 344–351 | Client | +3 | −2 |

---

## Unified diff

`````diff
--- mqtt/old/ballerina_mqtt.bal.txt	2026-08-12 12:57:29
+++ mqtt/new/ballerina_mqtt.bal.txt	2026-08-12 13:19:19
@@ -83,7 +83,8 @@
     int reasonCode?;
 };
 
-// Unknown type: Error
+# The common error type for the module.
+type Error error<ErrorDetails>;
 
 # An MQTT message holds the application payload and other metadata.
 # 
@@ -158,7 +159,7 @@
     # Combination of certificate and private key of the client or a `crypto:KeyStore`
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # Related protocol
-    record {|ballerina/mqtt:1.4.1:Protocol name; string version;|} protocol?;
+    record {|Protocol name; string version;|} protocol?;
 };
 
 # Represents a combination of certificate, private key, and private key password if encrypted.
@@ -223,13 +224,54 @@
 class Service {
 }
 
-// Unknown type: Listener
+# Creates a new `mqtt:Listener`.
+# ```ballerina
+# mqtt:Listener 'listener = check new(mqtt:DEFAULT_URL, "listener-unique-id", "mqtt/topic");
+# ```
+# 
+class Listener {
+    function init(string serverUri, string clientId, string|string[]|Subscription|Subscription[] subscriptions, ConnectionConfiguration connectionConfig = {}, boolean manualAcks = false, ListenerConfiguration config) returns Error?;
 
+    # Starts the registered services.
+    # ```ballerina
+    # mqtt:Error? result = 'listener.'start();
+    # ```
+    # 
+    function 'start() returns Error|();
+
+    # Stops the MQTT listener gracefully.
+    # ```ballerina
+    # mqtt:Error? result = 'listener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the mqtt listener immediately.
+    # ```ballerina
+    # mqtt:Error? result = 'listener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns Error|();
+
+    # Attaches a service to the listener.
+    # ```ballerina
+    # mqtt:Error? result = 'listener.attach(mqttService);
+    # ```
+    # 
+    function attach(Service 'service, string[]|string|() name = ()) returns Error|();
+
+    # Detaches a consumer service from the listener.
+    # ```ballerina
+    # mqtt:Error? result = 'listener.detach(mqttService);
+    # ```
+    # 
+    function detach(Service 'service) returns Error|();
+}
+
 // --- Client ---
 
 # Represents the client that is used to complete received messages.
 client class Caller {
-    function init() returns ballerina/mqtt:mqtt:Caller;
 
     # Completes the received message.
     # ```ballerina
@@ -248,7 +290,7 @@
 
 # Represents the client that is used to publish messages to the server.
 client class Client {
-    function init(string serverUri, string clientId, ConnectionConfiguration connectionConfig = {}, WillDetails willDetails = {willMessage: {payload: []}, destinationTopic: ""}, ClientConfiguration config) returns ballerina/mqtt:1.4.1:Error?;
+    function init(string serverUri, string clientId, ConnectionConfiguration connectionConfig = {}, WillDetails willDetails = {willMessage: {payload: []}, destinationTopic: ""}, ClientConfiguration config) returns Error?;
 
     # Publishes a message to a topic.
     # ```ballerina
@@ -302,7 +344,8 @@
 
 // --- Service ---
 
-service mqtt:Service on new mqtt:Listener(string serverUri = "", string clientId = "", string|string[]|Subscription|Subscription[] subscriptions = "", ListenerConfiguration config = {}) {
+service mqtt:Service on new mqtt:Listener(string serverUri, string clientId, string|string[]|mqtt:Subscription|mqtt:Subscription[] subscriptions, mqtt:ListenerConfiguration config = {}) {
     # The `onMessage` remote method will be triggered when a message is received from a subscribed topic.
-    remote function onMessage(Message message) returns error?;
+    # + message - The messages received for the topic
+    remote function onMessage(mqtt:Message message) returns error?;
 }
`````

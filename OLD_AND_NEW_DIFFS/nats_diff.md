# nats — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `nats` |
| **Old file** | `nats/old/ballerinax_nats.bal.txt` |
| **New file** | `nats/new/ballerinax_nats.bal.txt` |
| **Old lines** | 552 |
| **New lines** | 646 |
| **Lines added** | 104 |
| **Lines removed** | 10 |
| **Hunks** | 6 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (13)

- `annotation Payload`
- `annotation ServiceConfig`
- `annotation StreamServiceConfig`
- `class JetStreamListener`
- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `type Error`
- `type PayloadBindingError`
- `type PayloadValidationError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 175–185 | 175–188 | Types | +6 | −3 |
| 2 | 338–344 | 341–347 | Types | +1 | −1 |
| 3 | 418–432 | 421–516 | Types | +84 | −3 |
| 4 | 447–458 | 531–541 | Client | +1 | −2 |
| 5 | 482–488 | 565–571 | Client | +1 | −1 |
| 6 | 550–552 | 633–646 | Client | +11 | −0 |

---

## Unified diff

`````diff
--- nats/old/ballerinax_nats.bal.txt	2026-08-12 12:57:30
+++ nats/new/ballerinax_nats.bal.txt	2026-08-12 13:19:19
@@ -175,11 +175,14 @@
 # Default URL for NATS connections.
 const string DEFAULT_URL = "nats://localhost:4222";
 
-// Unknown type: Error
+# Represents the NATS module related errors.
+type Error error;
 
-// Unknown type: PayloadBindingError
+# Represents an error, which occurred due to payload binding.
+type PayloadBindingError error;
 
-// Unknown type: PayloadValidationError
+# Represents an error, which occurred due to payload constraint validation.
+type PayloadValidationError error;
 
 # Determines the properties for a stream.
 # 
@@ -338,7 +341,7 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and private key of the client
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerinax/nats:3.3.1:Protocol name;|} protocol?;
+    record {|Protocol name;|} protocol?;
 };
 
 # Represents combination of certificate, private key and private key password if encrypted.
@@ -418,15 +421,96 @@
 class Service {
 }
 
-// Unknown type: JetStreamListener
+# Initializes the NATS JetStream listener.
+# 
+class JetStreamListener {
+    function init(Client natsClient) returns Error?;
 
-// Unknown type: Listener
+    # Binds a service to the `nats:JetStreamListener`.
+    # ```ballerina
+    # check jetStreamListener.attach(service, "serviceName");
+    # ```
+    # 
+    function attach(JetStreamService s, string[]|string|() name = ()) returns error?;
+
+    # Stops consuming messages and detaches the service from the `nats:JetStreamListener`.
+    # ```ballerina
+    # check jetStreamListener.detach(service);
+    # ```
+    # 
+    function detach(JetStreamService s) returns error?;
+
+    # Starts the `nats:JetStreamListener`.
+    # ```ballerina
+    # check jetStreamListener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Stops the `nats:JetStreamListener` gracefully.
+    # ```ballerina
+    # check jetStreamListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the `nats:JetStreamListener` forcefully.
+    # ```ballerina
+    # check jetStreamListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+}
+
+# Initializes the NATS listener.
+# ```ballerina
+# nats:Listener natsListener = check new(nats:DEFAULT_URL);
+# ```
+# 
+class Listener {
+    function init(string|string[] url, string connectionName = "ballerina-nats", RetryConfig retryConfig = {}, Ping ping = {}, Credentials|Tokens auth = {username: "", password: ""}, string inboxPrefix = "_INBOX.", boolean noEcho = false, SecureSocket secureSocket = {cert: {path: "", password: ""}}, boolean validation = true, ConnectionConfiguration config) returns Error?;
 
+    # Binds a service to the `nats:Listener`.
+    # ```ballerina
+    # check natsListener.attach(service, "serviceName");
+    # ```
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Stops consuming messages and detaches the service from the `nats:Listener`.
+    # ```ballerina
+    # check natsListener.detach(service);
+    # ```
+    # 
+    function detach(Service s) returns error?;
+
+    # Starts the `nats:Listener`.
+    # ```ballerina
+    # check natsListener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Stops the `nats:Listener` gracefully.
+    # ```ballerina
+    # check natsListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the `nats:Listener` forcefully.
+    # ```ballerina
+    # check natsListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+}
+
 // --- Client ---
 
 # The client provides the capability to publish messages to the NATS server.
 client class Client {
-    function init(string|string[] url, string connectionName = "ballerina-nats", RetryConfig retryConfig = {}, Ping ping = {}, Credentials|Tokens auth = {username: "", password: ""}, string inboxPrefix = "_INBOX.", boolean noEcho = false, SecureSocket secureSocket = {cert: {path: "", password: ""}}, boolean validation = true, ConnectionConfiguration config) returns ballerinax/nats:3.3.1:Error?;
+    function init(string|string[] url, string connectionName = "ballerina-nats", RetryConfig retryConfig = {}, Ping ping = {}, Credentials|Tokens auth = {username: "", password: ""}, string inboxPrefix = "_INBOX.", boolean noEcho = false, SecureSocket secureSocket = {cert: {path: "", password: ""}}, boolean validation = true, ConnectionConfiguration config) returns Error?;
 
     # Publishes data to a given subject.
     # ```ballerina
@@ -447,12 +531,11 @@
     # check natsClient.close();
     # ```
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
 
 # The client that provides functionality related to acknowledging a JetStream message.
 client class JetStreamCaller {
-    function init() returns ballerinax/nats:nats:JetStreamCaller;
 
     # Acknowledges a JetStream messages received from a Consumer, indicating
     # the message should not be received again later.
@@ -482,7 +565,7 @@
 # The client provides the capability to publish messages to the NATS JetStream server and 
 # manage streams.
 client class JetStreamClient {
-    function init(Client natsClient) returns ballerinax/nats:3.3.1:Error?;
+    function init(Client natsClient) returns Error?;
 
     # Publishes data to a given subject.
     # ```ballerina
@@ -550,3 +633,14 @@
     # 
     remote function purgeStream(string streamName) returns Error|();
 }
+
+// --- Annotations ---
+
+# The annotation, which is used to configure the basic subscription.
+public annotation JetStreamServiceConfigData StreamServiceConfig on service, class;
+
+# The annotation which is used to define the payload parameter in the `onMessage` service method.
+public annotation NatsPayload Payload on parameter;
+
+# The annotation, which is used to configure the basic subscription.
+public annotation ServiceConfigData ServiceConfig on service, class;
`````

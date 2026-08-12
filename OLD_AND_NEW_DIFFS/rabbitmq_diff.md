# rabbitmq — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `rabbitmq` |
| **Old file** | `rabbitmq/old/ballerinax_rabbitmq.bal.txt` |
| **New file** | `rabbitmq/new/ballerinax_rabbitmq.bal.txt` |
| **Old lines** | 622 |
| **New lines** | 695 |
| **Lines added** | 89 |
| **Lines removed** | 16 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 6 | 6 |

### Declarations added (10)

- `annotation Payload`
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
| 1 | 344–350 | 344–350 | Types | +1 | −1 |
| 2 | 443–465 | 443–511 | Types | +51 | −5 |
| 3 | 478–484 | 524–530 | Client | +1 | −1 |
| 4 | 605–622 | 651–695 | Client | +36 | −9 |

---

## Unified diff

`````diff
--- rabbitmq/old/ballerinax_rabbitmq.bal.txt	2026-08-12 12:57:30
+++ rabbitmq/new/ballerinax_rabbitmq.bal.txt	2026-08-12 13:19:19
@@ -344,7 +344,7 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and private key of the client
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerinax/rabbitmq:3.6.0:Protocol name;|} protocol?;
+    record {|Protocol name;|} protocol?;
     # Enable/disable host name verification
     boolean verifyHostName?;
 };
@@ -443,23 +443,69 @@
 type RabbitmqPayload record {
 };
 
-// Unknown type: Error
+# Represents the RabbitMQ module related errors.
+type Error error;
 
-// Unknown type: PayloadBindingError
+# Represents an error, which occurred due to payload binding.
+type PayloadBindingError error;
 
-// Unknown type: PayloadValidationError
+# Represents an error, which occurred due to payload constraint validation.
+type PayloadValidationError error;
 
 # The RabbitMQ service type.
 class Service {
 }
 
-// Unknown type: Listener
+# Initializes a Listener object with the given connection configuration. Sets the global QoS settings,
+# which will be applied to the entire `rabbitmq:Listener`.
+# ```ballerina
+# rabbitmq:Listener rabbitmqListener = check new(rabbitmq:DEFAULT_HOST, rabbitmq:DEFAULT_PORT);
+# ```
+# 
+class Listener {
+    function init(string host, int port, QosSettings|() qosSettings = (), string username = "", string password = "", string virtualHost = "", decimal connectionTimeout = 0.0d, decimal handshakeTimeout = 0.0d, decimal shutdownTimeout = 0.0d, decimal heartbeat = 0.0d, boolean validation = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, Credentials auth = {username: "", password: ""}, Address[]|() failoverAddresses = (), ConnectionConfiguration connectionData) returns Error?;
+
+    # Attaches the service to the `rabbitmq:Listener` endpoint.
+    # ```ballerina
+    # check rabbitmqListener.attach(service, "serviceName");
+    # ```
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Starts consuming the messages on all the attached services.
+    # ```ballerina
+    # check rabbitmqListener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
 
+    # Stops consuming messages and detaches the service from the `rabbitmq:Listener` endpoint.
+    # ```ballerina
+    # check rabbitmqListener.detach(service);
+    # ```
+    # 
+    function detach(Service s) returns error?;
+
+    # Stops consuming messages through all consumer services by terminating the connection and all its channels.
+    # ```ballerina
+    # check rabbitmqListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops consuming messages through all the consumer services and terminates the connection
+    # with the server.
+    # ```ballerina
+    # check rabbitmqListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+}
+
 // --- Client ---
 
 # Provides the functionality to manipulate the messages received by the consumer services.
 client class Caller {
-    function init() returns ballerinax/rabbitmq:rabbitmq:Caller;
 
     # Acknowledges one or several received messages.
     # ```ballerina
@@ -478,7 +524,7 @@
 
 # The Ballerina interface to provide AMQP Channel related functionality.
 client class Client {
-    function init(string host, int port, string username = "", string password = "", string virtualHost = "", decimal connectionTimeout = 0.0d, decimal handshakeTimeout = 0.0d, decimal shutdownTimeout = 0.0d, decimal heartbeat = 0.0d, boolean validation = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, Credentials auth = {username: "", password: ""}, Address[]|() failoverAddresses = (), ConnectionConfiguration connectionData) returns ballerinax/rabbitmq:3.6.0:Error?;
+    function init(string host, int port, string username = "", string password = "", string virtualHost = "", decimal connectionTimeout = 0.0d, decimal handshakeTimeout = 0.0d, decimal shutdownTimeout = 0.0d, decimal heartbeat = 0.0d, boolean validation = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, Credentials auth = {username: "", password: ""}, Address[]|() failoverAddresses = (), ConnectionConfiguration connectionData) returns Error?;
 
     # Declares a non-exclusive, non-auto-delete, and durable queue with the given configurations.
     # ```ballerina
@@ -605,18 +651,45 @@
 
 // --- Service ---
 
-service rabbitmq:Service on new rabbitmq:Listener(string host = "", int port = 0, QosSettings|() qosSettings = (), ConnectionConfiguration connectionData = {}) {
-    # The `onMessage` remote method will be triggered when a message is received in the specified queue
-    remote function onMessage(AnydataMessage message, Caller caller) returns error?;
+# The service identifier accepts a quoted string literal, e.g. `"orders"`; it may be omitted.
+# A RabbitMQ consumer needs its queue name from exactly one source: @rabbitmq:ServiceConfig { queueName } or the service identifier.
+# Prefer the `queueName` field of @rabbitmq:ServiceConfig unless the requirement says otherwise.
+# A RabbitMQ service must implement exactly one of onMessage or onRequest.
+# Optional: this service may carry the @rabbitmq:ServiceConfig annotation. Replace {...} with its fields, which are those of rabbitmq:RabbitMQServiceConfig.
+@rabbitmq:ServiceConfig {...} // optional
+service rabbitmq:Service on new rabbitmq:Listener(string host, int port, rabbitmq:QosSettings|() qosSettings = (), rabbitmq:ConnectionConfiguration connectionData = {}) {
+    # Invoked once per message delivered from the subscribed queue. Use this for consume-only workloads; use onRequest instead when the publisher expects a reply.
+    # + message - The delivered message. Declare a narrower type to project the payload, see the messagePayload data-binding rule.
+    # + caller - Handle for explicitly acknowledging or rejecting the message. Needed only under client acknowledgement.
+    # `message` may also be: rabbitmq:BytesMessage
+    # `message` may bind directly to: anydata — but never rabbitmq:AnydataMessage
+    # `message` may bind to a record that includes `*rabbitmq:AnydataMessage;` and overrides only `content`
+    # The `message` parameter may carry @rabbitmq:Payload, written `@rabbitmq:Payload {}` before its type. Its fields are those of rabbitmq:RabbitmqPayload.
+    # Required parameters: message
+    # Optional parameters (may be omitted): caller
+    remote function onMessage(rabbitmq:AnydataMessage message, rabbitmq:Caller caller) returns error?; // optional
 
-    # The `onRequest` remote method will be triggered when a message is received in the specified queue and a response is expected
-    remote function onRequest(AnydataMessage message, Caller caller) returns anydata|error;
+    # Invoked once per message delivered from the subscribed queue, for RPC-style consumers. Whatever the handler returns is published back to the message's reply-to queue, which is why it returns anydata rather than ().
+    # + message - The delivered request message. Declare a narrower type to project the payload, see the messagePayload data-binding rule.
+    # + caller - Handle for explicitly acknowledging or rejecting the message. Needed only under client acknowledgement.
+    # `message` may also be: rabbitmq:BytesMessage
+    # `message` may bind directly to: anydata — but never rabbitmq:AnydataMessage
+    # `message` may bind to a record that includes `*rabbitmq:AnydataMessage;` and overrides only `content`
+    # The `message` parameter may carry @rabbitmq:Payload, written `@rabbitmq:Payload {}` before its type. Its fields are those of rabbitmq:RabbitmqPayload.
+    # Required parameters: message
+    # Optional parameters (may be omitted): caller
+    remote function onRequest(rabbitmq:AnydataMessage message, rabbitmq:Caller caller) returns anydata|error; // optional
 
-    # The `onError` remote method will be triggered when an error occurs during the message processing
-    remote function onError(AnydataMessage message, Error rabbitmqError) returns error?;
+    # Invoked when a delivered message cannot be dispatched, most commonly when its payload fails to bind to the declared parameter type.
+    # + message - The message that could not be dispatched, in its unprojected form.
+    # + err - The failure that prevented dispatch.
+    remote function onError(rabbitmq:AnydataMessage message, rabbitmq:Error err) returns error?; // optional
 }
 
 // --- Annotations ---
 
-# Define advanced queue configurations 
-public annotation RabbitMQServiceConfig ServiceConfig on service;
+# The annotation, which is used to configure the subscription.
+public annotation RabbitMQServiceConfig ServiceConfig on service, class;
+
+# The annotation which is used to define the payload parameter in the `onMessage` service method.
+public annotation RabbitmqPayload Payload on parameter;
`````

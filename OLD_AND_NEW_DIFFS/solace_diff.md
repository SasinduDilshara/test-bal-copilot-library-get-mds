# solace — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `solace` |
| **Old file** | `solace/old/ballerinax_solace.bal.txt` |
| **New file** | `solace/new/ballerinax_solace.bal.txt` |
| **Old lines** | 796 |
| **New lines** | 840 |
| **Lines added** | 61 |
| **Lines removed** | 17 |
| **Hunks** | 11 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 18 | 0 |
| `// --- section ---` markers | 6 | 6 |

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
| 1 | 234–240 | 234–241 | Types | +2 | −1 |
| 2 | 266–272 | 267–273 | Types | +1 | −1 |
| 3 | 315–324 | 316–325 | Types | +2 | −2 |
| 4 | 488–494 | 489–495 | Types | +1 | −1 |
| 5 | 550–556 | 551–557 | Types | +1 | −1 |
| 6 | 581–587 | 582–588 | Types | +1 | −1 |
| 7 | 598–610 | 599–647 | Types | +39 | −3 |
| 8 | 613–619 | 650–655 | Client | +0 | −1 |
| 9 | 676–682 | 712–718 | Client | +1 | −1 |
| 10 | 755–761 | 791–797 | Client | +1 | −1 |
| 11 | 782–796 | 818–840 | Client | +12 | −4 |

---

## Unified diff

`````diff
--- solace/old/ballerinax_solace.bal.txt	2026-08-12 12:57:30
+++ solace/new/ballerinax_solace.bal.txt	2026-08-12 13:19:19
@@ -234,7 +234,8 @@
 # A property key used internally to mark that a message's text payload is XML.
 const string SOLACE_ISXML_PROP = "solace_isXML";
 
-// Unknown type: Error
+# Represents a Solace distinct error.
+type Error error;
 
 # The Solace service type attached to a `solace:Listener` for asynchronous (push-based) consumption.
 # 
@@ -266,7 +267,7 @@
     string queueName;
 };
 
-type Destination ballerinax/solace:0.4.0:Topic|ballerinax/solace:0.4.0:Queue;
+type Destination Topic|Queue;
 
 # Acknowledgement modes for message consumption
 enum AcknowledgementMode {
@@ -315,10 +316,10 @@
 
 # OAuth2 authentication configuration (mutually exclusive - use either access token or ID token)
 # When using OAuth2 authentication scheme, exactly one of OAuth2AccessTokenAuth or OidcIdTokenAuth must be provided
-type OAuth2Configuration ballerinax/solace:0.4.0:OAuth2AccessTokenAuth|ballerinax/solace:0.4.0:OidcIdTokenAuth;
+type OAuth2Configuration OAuth2AccessTokenAuth|OidcIdTokenAuth;
 
 # Authentication configuration (basic, Kerberos, or OAuth2)
-type AuthConfiguration ballerinax/solace:0.4.0:BasicAuthConfiguration|ballerinax/solace:0.4.0:KerberosConfiguration|ballerinax/solace:0.4.0:OAuth2AccessTokenAuth|ballerinax/solace:0.4.0:OidcIdTokenAuth;
+type AuthConfiguration BasicAuthConfiguration|KerberosConfiguration|OAuth2AccessTokenAuth|OidcIdTokenAuth;
 
 # SSL/TLS certificate validation configuration
 
@@ -488,7 +489,7 @@
 };
 
 # Consumer subscription configuration: QueueConfiguration or TopicConfiguration
-type SubscriptionConfiguration ballerinax/solace:0.4.0:QueueConfiguration|ballerinax/solace:0.4.0:TopicConfiguration;
+type SubscriptionConfiguration QueueConfiguration|TopicConfiguration;
 
 # Consumer configuration for synchronous (pull-based) message consumption via MessageConsumer
 
@@ -550,7 +551,7 @@
 };
 
 # Service subscription configuration (sealed: QueueServiceConfiguration | TopicServiceConfiguration)
-type ServiceConfiguration ballerinax/solace:0.4.0:QueueServiceConfiguration|ballerinax/solace:0.4.0:TopicServiceConfiguration;
+type ServiceConfiguration QueueServiceConfiguration|TopicServiceConfiguration;
 
 # Message type for publishing/consuming
 
@@ -581,7 +582,7 @@
 Set by the application for message ordering and duplicate detection.
     int sequenceNumber?;
     # Properties map for custom key-value pairs
-    map<ballerinax/solace:0.4.0:Property> properties?;
+    map<Property> properties?;
     # Application-specific user data attachment (max 36 bytes)
     byte[] userData?;
     # Receive timestamp in UTC milliseconds from epoch (set by broker)
@@ -598,13 +599,49 @@
 };
 
 # Represents the allowed value types for a Solace message property.
-type Property boolean|int|byte|float|string|byte[]|map<ballerinax/solace:0.4.0:Property>;
+type Property boolean|int|byte|float|string|byte[]|map<Property>;
 
 # Represents the allowed value types for entries in a Solace MapMessage payload.
-type Value boolean|int|byte|float|string|byte[]|map<ballerinax/solace:0.4.0:Value>;
+type Value boolean|int|byte|float|string|byte[]|map<Value>;
 
-// Unknown type: Listener
+# Initialize a new listener with the given connection configuration.
+# 
+class Listener {
+    function init(string url, string messageVpn = "", AuthConfiguration auth = {username: ""}, SecureSocket secureSocket = {}, string clientName = "", string clientDescription = "", boolean transacted = false, int compressionLevel = 0, string localhost = "", decimal connectTimeout = 0.0d, decimal readTimeout = 0.0d, RetryConfiguration retryConfig = {}, boolean generateReceiveTimestamps = false, boolean calculateMessageExpiration = false, ListenerConfiguration config) returns Error?;
+
+    # Attach a service to the listener.
+    # 
+    # The service must declare a remote `onMessage` method and may optionally declare an `onError`
+    # method. Its subscription is read from the `@solace:ServiceConfig` annotation.
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns Error|();
+
+    # Detach a service from the listener.
+    # 
+    # Stops and closes the flow/consumer associated with the service.
+    # 
+    function detach(Service s) returns Error|();
+
+    # Start the listener.
+    # 
+    # Begins delivering messages to all attached services.
+    # 
+    function 'start() returns Error|();
 
+    # Gracefully stop the listener.
+    # 
+    # Stops delivery to attached services and waits for in-flight message processing to complete
+    # before closing resources.
+    # 
+    function gracefulStop() returns Error|();
+
+    # Immediately stop the listener.
+    # 
+    # Stops delivery and closes resources without waiting for in-flight processing.
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Caller for explicit acknowledgement and transaction control within a service's `onMessage` method.
@@ -613,7 +650,6 @@
 # `onMessage`. Use it when the service is configured with `ackMode = CLIENT_ACK` and needs manual
 # acknowledgement, or when the listener connection is transacted and needs commit/rollback control.
 client class Caller {
-    function init() returns ballerinax/solace:solace:Caller;
 
     # Acknowledge a message in `CLIENT_ACK` mode.
     # 
@@ -676,7 +712,7 @@
 # solace:Message? msg = check consumer->receive(10.0);
 # ```
 client class MessageConsumer {
-    function init(string url, string messageVpn = "", AuthConfiguration auth = {username: ""}, SecureSocket secureSocket = {}, string clientName = "", string clientDescription = "", boolean transacted = false, int compressionLevel = 0, string localhost = "", decimal connectTimeout = 0.0d, decimal readTimeout = 0.0d, RetryConfiguration retryConfig = {}, anydata Additional Values, boolean generateReceiveTimestamps = false, boolean calculateMessageExpiration = false, SubscriptionConfiguration subscriptionConfig = {}, ConsumerConfiguration config) returns ballerinax/solace:0.4.0:Error?;
+    function init(string url, string messageVpn = "", AuthConfiguration auth = {username: ""}, SecureSocket secureSocket = {}, string clientName = "", string clientDescription = "", boolean transacted = false, int compressionLevel = 0, string localhost = "", decimal connectTimeout = 0.0d, decimal readTimeout = 0.0d, RetryConfiguration retryConfig = {}, boolean generateReceiveTimestamps = false, boolean calculateMessageExpiration = false, SubscriptionConfiguration subscriptionConfig = {}, ConsumerConfiguration config) returns Error?;
 
     # Receive a message with a timeout.
     # 
@@ -755,7 +791,7 @@
 # check producer->close();
 # ```
 client class MessageProducer {
-    function init(string url, string messageVpn = "", AuthConfiguration auth = {username: ""}, SecureSocket secureSocket = {}, string clientName = "", string clientDescription = "", boolean transacted = false, int compressionLevel = 0, string localhost = "", decimal connectTimeout = 0.0d, decimal readTimeout = 0.0d, RetryConfiguration retryConfig = {}, anydata Additional Values, boolean generateSendTimestamps = false, boolean generateSequenceNumbers = false, ProducerConfiguration config) returns ballerinax/solace:0.4.0:Error?;
+    function init(string url, string messageVpn = "", AuthConfiguration auth = {username: ""}, SecureSocket secureSocket = {}, string clientName = "", string clientDescription = "", boolean transacted = false, int compressionLevel = 0, string localhost = "", decimal connectTimeout = 0.0d, decimal readTimeout = 0.0d, RetryConfiguration retryConfig = {}, boolean generateSendTimestamps = false, boolean generateSequenceNumbers = false, ProducerConfiguration config) returns Error?;
 
     # Send a message to the specified destination.
     # 
@@ -782,15 +818,23 @@
 
 // --- Service ---
 
-service solace:Service on new solace:Listener(string url = "", ListenerConfiguration config = {}) {
+service solace:Service on new solace:Listener(string url, solace:ListenerConfiguration config = {}) {
     # Triggers when a message is received from a Solace queue or topic
-    remote function onMessage(Message message, Caller caller) returns error?;
+    # + message - The received Solace message
+    # + caller - The Solace caller to control transactions and message acknowledgement
+    # Required parameters: message
+    # Optional parameters (may be omitted): caller
+    remote function onMessage(solace:Message message, solace:Caller caller) returns error?;
 
     # Triggers when an error occurs during message processing
-    remote function onError(Error solaceError) returns error?;
+    # + solaceError - The error occurred during message processing
+    remote function onError(solace:Error solaceError) returns error?;
 }
 
 // --- Annotations ---
 
-# Define advanced configurations like queue or topic name
+# The service configuration annotation for a Solace service attached to a `solace:Listener`.
+# 
+# Specifies the subscription (queue or topic) and the flow options for the service.
+# Exactly one of `queueName` or `topicName` must be provided.
 public annotation ServiceConfiguration ServiceConfig on service;
`````

# java.jms — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `java.jms` |
| **Old file** | `java.jms/old/ballerinax_java.jms.bal.txt` |
| **New file** | `java.jms/new/ballerinax_java.jms.bal.txt` |
| **Old lines** | 505 |
| **New lines** | 558 |
| **Lines added** | 62 |
| **Lines removed** | 9 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 4 |

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
| 1 | 187–193 | 187–194 | Types | +2 | −1 |
| 2 | 328–340 | 329–393 | Types | +54 | −2 |
| 3 | 357–363 | 410–416 | Client | +1 | −1 |
| 4 | 392–398 | 445–451 | Client | +1 | −1 |
| 5 | 425–431 | 478–484 | Client | +1 | −1 |
| 6 | 450–456 | 503–509 | Client | +1 | −1 |
| 7 | 470–476 | 523–529 | Client | +1 | −1 |
| 8 | 480–486 | 533–539 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- java.jms/old/ballerinax_java.jms.bal.txt	2026-08-12 12:57:30
+++ java.jms/new/ballerinax_java.jms.bal.txt	2026-08-12 13:19:19
@@ -187,7 +187,8 @@
     string name?;
 };
 
-// Unknown type: Error
+# Represents a JMS distinct error.
+type Error error;
 
 # Represent the JMS Message used to send and receive content from the a JMS provider.
 # 
@@ -328,13 +329,65 @@
     SESSION_TRANSACTED
 }
 
-// Unknown type: Listener
+# Creates a new `jms:Listener`.
+# ```ballerina
+# listener jms:Listener messageListener = check new(
+#   connectionConfig = {
+#       initialContextFactory: "org.apache.activemq.jndi.ActiveMQInitialContextFactory",
+#       providerUrl: "tcp://localhost:61616"
+#   },
+#   consumerOptions = {
+#       destination: {
+#           'type: jms:QUEUE,
+#           name: "test-queue"
+#       }
+#   }
+# );
+# ```
+# 
+class Listener {
+    function init(ConnectionConfiguration connectionConfig = {initialContextFactory: "", providerUrl: ""}, AcknowledgementMode acknowledgementMode = AUTO_ACKNOWLEDGE, ConsumerOptions consumerOptions = {destination: {'type: "TEMPORARY_TOPIC"}}, MessageListenerConfigurations listenerConfig) returns Error?;
 
+    # Attaches a message consumer service to a listener.
+    # ```ballerina
+    # check messageListener.attach(jmsService);
+    # ```
+    # 
+    function attach(Service 'service, string[]|string|() name = ()) returns Error|();
+
+    # Detaches a message consumer service from the the listener.
+    # ```ballerina
+    # check messageListener.detach(jmsService);
+    # ```
+    # 
+    function detach(Service 'service) returns Error|();
+
+    # Starts the endpoint.
+    # ```ballerina
+    # check messageListener.'start();
+    # ```
+    # 
+    function 'start() returns Error|();
+
+    # Stops the JMS listener gracefully.
+    # ```ballerina
+    # check messageListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the JMS listener immediately.
+    # ```ballerina
+    # check messageListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Represents a JMS caller, which can be used to mark JMS message as received.
 client class Caller {
-    function init() returns jms:jms:Caller;
 
     # Mark a JMS message as received.
     # 
@@ -357,7 +410,7 @@
 
 # Represents JMS Connection.
 client class Connection {
-    function init(string initialContextFactory = "", string providerUrl = "", string connectionFactoryName = "ConnectionFactory", string username = "", string password = "", map<string> properties = {}, ConnectionConfiguration connectionConfig) returns ballerinax/java.jms:1.2.1:Error?;
+    function init(string initialContextFactory = "", string providerUrl = "", string connectionFactoryName = "ConnectionFactory", string username = "", string password = "", map<string> properties = {}, ConnectionConfiguration connectionConfig) returns Error?;
 
     # Create a Session object, specifying transacted and acknowledgeMode.
     # ```ballerina
@@ -392,7 +445,7 @@
 
 # JMS Message Consumer client object to receive messages from both queues and topics.
 client class MessageConsumer {
-    function init(Session session, ConsumerType type = "DEFAULT", Destination destination = {'type: "TEMPORARY_TOPIC"}, string messageSelector = "", boolean noLocal = false, string subscriberName = "", ConsumerOptions consumerOptions) returns ballerinax/java.jms:1.2.1:Error?;
+    function init(Session session, ConsumerType type = "DEFAULT", Destination destination = {'type: "TEMPORARY_TOPIC"}, string messageSelector = "", boolean noLocal = false, string subscriberName = "", ConsumerOptions consumerOptions) returns Error?;
 
     # Receives the next message that arrives within the specified timeout interval.
     # ```ballerina
@@ -425,7 +478,7 @@
 
 # JMS Message Producer client object to send messages to both queues and topics.
 client class MessageProducer {
-    function init(Session session, Destination|() destination = ()) returns ballerinax/java.jms:1.2.1:Error?;
+    function init(Session session, Destination|() destination = ()) returns Error?;
 
     # Sends a message to the JMS provider.
     # ```ballerina
@@ -450,7 +503,7 @@
 
 # Represents the JMS session.
 client class Session {
-    function init(Connection connection, AcknowledgementMode ackMode) returns ballerinax/java.jms:1.2.1:Error?;
+    function init(Connection connection, AcknowledgementMode ackMode) returns Error?;
 
     # Unsubscribe a durable subscription that has been created by this session.
     # It is erroneous for a client to delete a durable subscription while there is an active (not closed) consumer
@@ -470,7 +523,7 @@
     # });
     # ```
     # 
-    remote function createProducer(Destination|() destination = ()) returns MessageProducer|Error;
+    function createProducer(Destination|() destination = ()) returns MessageProducer|Error;
 
     # Creates a MessageConsumer for the specified destination.
     # ```ballerina
@@ -480,7 +533,7 @@
     # });
     # ```
     # 
-    remote function createConsumer(ConsumerType type = "DEFAULT", Destination destination = {'type: "TEMPORARY_TOPIC"}, string messageSelector = "", boolean noLocal = false, string subscriberName = "", ConsumerOptions consumerOptions) returns MessageConsumer|Error;
+    function createConsumer(ConsumerType type = "DEFAULT", Destination destination = {'type: "TEMPORARY_TOPIC"}, string messageSelector = "", boolean noLocal = false, string subscriberName = "", ConsumerOptions consumerOptions) returns MessageConsumer|Error;
 
     # Commits all messages sent/received in this transaction and releases any locks currently held.
     # ```ballerina
`````

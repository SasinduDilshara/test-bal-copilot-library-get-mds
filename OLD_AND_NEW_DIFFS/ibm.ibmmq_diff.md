# ibm.ibmmq — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ibm.ibmmq` |
| **Old file** | `ibm.ibmmq/old/ballerinax_ibm.ibmmq.bal.txt` |
| **New file** | `ibm.ibmmq/new/ballerinax_ibm.ibmmq.bal.txt` |
| **Old lines** | 979 |
| **New lines** | 1033 |
| **Lines added** | 68 |
| **Lines removed** | 14 |
| **Hunks** | 10 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 11 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (16)

- `annotation ServiceConfig`
- `class Listener`
- `class QueueManager`
- `client class Destination`
- `function 'start`
- `function accessQueue`
- `function accessTopic`
- `function attach`
- `function close`
- `function detach`
- `function disconnect`
- `function get`
- `function gracefulStop`
- `function immediateStop`
- `function put`
- `type Error`

### Declarations removed (1)

- `class Destination`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 507–513 | 507–519 | Types | +7 | −1 |
| 2 | 522–528 | 528–535 | Types | +2 | −1 |
| 3 | 576–582 | 583–589 | Types | +1 | −1 |
| 4 | 610–616 | 617–623 | Types | +1 | −1 |
| 5 | 745–759 | 752–766 | Types | +4 | −4 |
| 6 | 847–853 | 854–860 | Types | +1 | −1 |
| 7 | 883–897 | 890–948 | Types | +47 | −3 |
| 8 | 914–920 | 965–970 | Client | +0 | −1 |
| 9 | 940–946 | 990–995 | Client | +0 | −1 |
| 10 | 977–979 | 1026–1033 | Client | +5 | −0 |

---

## Unified diff

`````diff
--- ibm.ibmmq/old/ballerinax_ibm.ibmmq.bal.txt	2026-08-12 12:57:30
+++ ibm.ibmmq/new/ballerinax_ibm.ibmmq.bal.txt	2026-08-12 13:19:19
@@ -507,7 +507,13 @@
 const string DUPS_OK_ACKNOWLEDGE = "DUPS_OK_ACKNOWLEDGE";
 
 # IBM MQ destination client type.
-class Destination {
+client class Destination {
+
+    remote function put(Message message, int options = 0) returns Error|();
+
+    remote function get(int options = 0, int waitInterval = 10, MatchOptions matchOptions = {}, GetMessageOptions getMessageOptions) returns Message|Error|();
+
+    remote function close() returns Error|();
 }
 
 # The error details type for the IBM MQ module.
@@ -522,7 +528,8 @@
     int completionCode?;
 };
 
-// Unknown type: Error
+# Represents a IBM MQ distinct error.
+type Error error<ErrorDetails>;
 
 # Represents an IBMMQ service object that can be attached to an `ibmmq:Listener`.
 class Service {
@@ -576,7 +583,7 @@
 };
 
 # The service configuration type for the `ibmmq:Service`.
-type ServiceConfiguration ballerinax/ibm.ibmmq:1.4.4:QueueConfig|ballerinax/ibm.ibmmq:1.4.4:TopicConfig;
+type ServiceConfiguration QueueConfig|TopicConfig;
 
 # Options which can be provided when opening an IBM MQ topic.
 type OPEN_TOPIC_OPTION 1|2;
@@ -610,7 +617,7 @@
     int version?;
     # Table containing all occurrences of field values matching
 the specified field name in the folder
-    table<ballerinax/ibm.ibmmq:1.4.4:MQRFH2Field> key(folder,field) fieldValues?;
+    table<MQRFH2Field> key(folder,field) fieldValues?;
 };
 
 # Record defining a field in the MQRFH2 record.
@@ -745,15 +752,15 @@
     # This is the transaction instance identifier
     byte[] tranInstanceId?;
     # This indicates the IMS conversation state
-    ballerina/lang.string:0.0.0:Char tranState?;
+    string:Char tranState?;
     # IMS commit mode
-    ballerina/lang.string:0.0.0:Char commitMode?;
+    string:Char commitMode?;
     # This indicates the IMS security processing required
-    ballerina/lang.string:0.0.0:Char securityScope?;
+    string:Char securityScope?;
 };
 
 # Header types that are provided in the IBM MQ message.
-type Header ballerinax/ibm.ibmmq:1.4.4:MQRFH2|ballerinax/ibm.ibmmq:1.4.4:MQRFH|ballerinax/ibm.ibmmq:1.4.4:MQCIH|ballerinax/ibm.ibmmq:1.4.4:MQIIH;
+type Header MQRFH2|MQRFH|MQCIH|MQIIH;
 
 # The coded character set used in application message data.
 type MessageCharset -3|850|819|-4|0|37|-1|-2|0|0|1200|1208;
@@ -847,7 +854,7 @@
 
 type Message record {
     # Message properties
-    map<ballerinax/ibm.ibmmq:1.4.4:Property> properties?;
+    map<Property> properties?;
     # Format associated with the header
     string format?;
     # Message identifier
@@ -883,15 +890,59 @@
     byte[] payload;
 };
 
-// Unknown type: Listener
+# Initializes the IBMMQ listener.
+class Listener {
+    function init(string name = "", string host = "", int port = 1414, string channel = "", string userID = "", string password = "", SecureSocket secureSocket = {cert: {path: "", password: ""}}, SslCipherSuite sslCipherSuite = "SSL_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA", QueueManagerConfiguration configurations) returns Error?;
 
-// Unknown type: QueueManager
+    # Attaches an IBMMQ service to the IBMMQ listener.
+    function attach(Service s, string[]|string|() name = ()) returns Error|();
+
+    # Detaches an IBMMQ service from the IBMMQ listener.
+    function detach(Service s) returns Error|();
+
+    # Starts the IBMMQ listener.
+    function 'start() returns Error|();
+
+    # Gracefully stops the IBMMQ listener.
+    function gracefulStop() returns Error|();
+
+    # Immediately stops the IBMMQ listener.
+    function immediateStop() returns Error|();
+}
 
+# Initialize an IBM MQ queue manager.
+# ```ballerina
+# ibmmq:QueueManager queueManager = check new(name = "QM1", host = "localhost", channel = "DEV.APP.SVRCONN");
+# ```
+# 
+class QueueManager {
+    function init(string name = "", string host = "", int port = 1414, string channel = "", string userID = "", string password = "", SecureSocket secureSocket = {cert: {path: "", password: ""}}, SslCipherSuite sslCipherSuite = "SSL_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA", QueueManagerConfiguration configurations) returns Error?;
+
+    # Establishes access to an IBM MQ queue on this queue manager.
+    # ```ballerina
+    # ibmmq:Queue queue = check queueManager.accessQueue("queue1", ibmmq:MQOO_OUTPUT);
+    # ```
+    # 
+    function accessQueue(string queueName, int options) returns Queue|Error;
+
+    # Establishes access to an IBM MQ topic on this queue manager.
+    # ```ballerina
+    # ibmmq:Topic topic = check queueManager.accessTopic(
+    #   "dev", "DEV.BASE.TOPIC", ibmmq:OPEN_AS_PUBLICATION, ibmmq:MQOO_OUTPUT
+    # );
+    # ```
+    # 
+    function accessTopic(string topicName, string topicString, OPEN_TOPIC_OPTION openTopicOption, int options) returns Topic|Error;
+
+    # Ends the connection to the IBM MQ queue manager.
+    # 
+    function disconnect() returns Error|();
+}
+
 // --- Client ---
 
 # Represents a IBM MQ caller, which can be used to mark IBM MQ message as received.
 client class Caller {
-    function init() returns ibmmq:ibmmq:Caller;
 
     # Mark an IBM MQ message as received.
     # 
@@ -914,7 +965,6 @@
 
 # IBM MQ Queue client.
 client class Queue {
-    function init() returns ibmmq:ibmmq:Queue;
 
     # Puts a message to an IBM MQ queue.
     # ```ballerina
@@ -940,7 +990,6 @@
 
 # IBM MQ Topic client.
 client class Topic {
-    function init() returns ibmmq:ibmmq:Topic;
 
     # Puts a message to an IBM MQ topic.
     # ```ballerina
@@ -977,3 +1026,8 @@
     # 
     remote function send(Message message) returns Error|();
 }
+
+// --- Annotations ---
+
+# Annotation to configure the `ibmmq:Service`.
+public annotation ServiceConfiguration ServiceConfig on service;
`````

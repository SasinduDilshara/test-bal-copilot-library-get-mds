# udp — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `udp` |
| **Old file** | `udp/old/ballerina_udp.bal.txt` |
| **New file** | `udp/new/ballerina_udp.bal.txt` |
| **Old lines** | 205 |
| **New lines** | 239 |
| **Lines added** | 39 |
| **Lines removed** | 5 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
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
| 1 | 129–138 | 129–172 | Types | +36 | −2 |
| 2 | 153–159 | 187–193 | Client | +1 | −1 |
| 3 | 179–185 | 213–219 | Client | +1 | −1 |
| 4 | 194–200 | 228–234 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- udp/old/ballerina_udp.bal.txt	2026-08-12 12:57:29
+++ udp/new/ballerina_udp.bal.txt	2026-08-12 13:19:19
@@ -129,10 +129,44 @@
 class Service {
 }
 
-// Unknown type: Error
+# Represents udp module related errors.
+type Error error;
 
-// Unknown type: Listener
+# Initializes the UDP listener based on the privovided configurations. 
+# ```ballerina
+#  listener Listener|error? udpServer = new (8080);
+# ```
+class Listener {
+    function init(int localPort, string remoteHost = "", int remotePort = 0, string localHost = "", ListenerConfiguration config) returns Error?;
 
+    # Binds a service to the `udp:Listener`.
+    # ```ballerina
+    # udp:error? result = udpListener.attach(helloService);
+    # ```
+    # 
+    function attach(Service s, () name = ()) returns error?;
+
+    # Starts the registered service programmatically.
+    # 
+    function 'start() returns error?;
+
+    # Stops the service listener gracefully. Already-accepted requests will be
+    # served before connection closure.
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the service listener immediately. It is not implemented yet.
+    # 
+    function immediateStop() returns error?;
+
+    # Stops consuming messages and detaches the service from the `udp:Listener`.
+    # ```ballerina
+    # udp:error? result = udpListener.detach(helloService);
+    # ```
+    # 
+    function detach(Service s) returns error?;
+}
+
 // --- Client ---
 
 # Represents caller object in UDP service remote methods.
@@ -153,7 +187,7 @@
 # Initializes the UDP connection oriented client based on the 
 # provided configurations.
 client class ConnectClient {
-    function init(string remoteHost, int remotePort, decimal timeout = 300, string localHost = "", anydata Additional Values, ConnectClientConfiguration config) returns ballerina/udp:1.13.6:Error?;
+    function init(string remoteHost, int remotePort, decimal timeout = 300, string localHost = "", ConnectClientConfiguration config) returns Error?;
 
     # Sends the given data to the connected remote host.
     # ```ballerina
@@ -179,7 +213,7 @@
 
 # Initializes the UDP connectionless client based on the provided configurations.
 client class Client {
-    function init(decimal timeout = 300, string localHost = "", anydata Additional Values, ClientConfiguration config) returns ballerina/udp:1.13.6:Error?;
+    function init(decimal timeout = 300, string localHost = "", ClientConfiguration config) returns Error?;
 
     # Sends the given data to the specified remote host.
     # ```ballerina
@@ -194,7 +228,7 @@
     # udp:Datagram|udp:Error result = socketClient->receiveDatagram();
     # ```
     # 
-    remote function receiveDatagram() returns ballerina/udp:1.13.6:Datagram & readonly|Error;
+    remote function receiveDatagram() returns Datagram & readonly|Error;
 
     # Free up the occupied socket.
     # ```ballerina
`````

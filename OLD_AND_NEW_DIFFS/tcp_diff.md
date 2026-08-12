# tcp — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `tcp` |
| **Old file** | `tcp/old/ballerina_tcp.bal.txt` |
| **New file** | `tcp/new/ballerina_tcp.bal.txt` |
| **Old lines** | 251 |
| **New lines** | 285 |
| **Lines added** | 41 |
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
| 1 | 134–140 | 134–140 | Types | +1 | −1 |
| 2 | 167–173 | 167–173 | Types | +1 | −1 |
| 3 | 197–206 | 197–239 | Types | +35 | −2 |
| 4 | 219–225 | 252–258 | Client | +1 | −1 |
| 5 | 245–251 | 278–285 | Client | +3 | −2 |

---

## Unified diff

`````diff
--- tcp/old/ballerina_tcp.bal.txt	2026-08-12 12:57:29
+++ tcp/new/ballerina_tcp.bal.txt	2026-08-12 13:19:19
@@ -134,7 +134,7 @@
     # Configurations associated with `crypto:TrustStore` or single certificate file that the client trusts
     crypto:TrustStore|string cert?; // Special Agent Note: TrustStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerina/tcp:1.13.8:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # List of ciphers to be used
 E.g., `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
     string[] ciphers?;
@@ -167,7 +167,7 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and (PKCS8) private key of the server
     crypto:KeyStore|CertKey key; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerina/tcp:1.13.8:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # List of ciphers to be used
 E.g., `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
     string[] ciphers?;
@@ -197,10 +197,43 @@
 class ConnectionService {
 }
 
-// Unknown type: Error
+# Represents TCP module related errors.
+type Error error;
 
-// Unknown type: Listener
+# Initializes the TCP listener based on the provided configurations.
+# ```ballerina
+#  listener Listener|error? server1 = new (8080);
+# ```
+class Listener {
+    function init(int localPort, string localHost = "", ListenerSecureSocket secureSocket = {'key: {path: "", password: ""}}, ListenerConfiguration config) returns Error?;
+
+    # Binds a service to the `tcp:Listener`.
+    # ```ballerina
+    # tcp:error? result = tcpListener.attach(helloService);
+    # ```
+    # 
+    function attach(Service tcpService, string[]|string|() name = ()) returns error?;
+
+    # Starts the registered service programmatically.
+    # 
+    function 'start() returns error?;
+
+    # Stops the service listener gracefully. Already-accepted requests will be served before the connection closure.
+    # 
+    function gracefulStop() returns error?;
 
+    # Stops the service listener immediately. It is not implemented yet.
+    # 
+    function immediateStop() returns error?;
+
+    # Stops consuming messages and detaches the service from the `tcp:Listener`.
+    # ```ballerina
+    # tcp:error? result = tcpListener.detach(helloService);
+    # ```
+    # 
+    function detach(Service tcpService) returns error?;
+}
+
 // --- Client ---
 
 # Represents caller object in tcp service remote methods.
@@ -219,7 +252,7 @@
 
 # Initializes the TCP connection client based on the provided configurations.
 client class Client {
-    function init(string remoteHost, int remotePort, string localHost = "", decimal timeout = 300, decimal writeTimeout = 300, ClientSecureSocket secureSocket = {}, ClientConfiguration config) returns ballerina/tcp:1.13.8:Error?;
+    function init(string remoteHost, int remotePort, string localHost = "", decimal timeout = 300, decimal writeTimeout = 300, ClientSecureSocket secureSocket = {}, ClientConfiguration config) returns Error?;
 
     # Sends the given data to the connected remote host.
     # ```ballerina
@@ -245,7 +278,8 @@
 
 // --- Service ---
 
-service tcp:Service on new tcp:Listener(int localPort = 0, ListenerConfiguration config = {}) {
+service tcp:Service on new tcp:Listener(int localPort, tcp:ListenerConfiguration config = {}) {
     # The `onConnect` remote method will be triggered when a message is received from a tcp client
-    remote function onConnect(Caller caller) returns ConnectionService|Error?;
+    # + caller - The new client connection
+    remote function onConnect(tcp:Caller caller) returns tcp:ConnectionService|tcp:Error?;
 }
`````

# websocket — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `websocket` |
| **Old file** | `websocket/old/ballerina_websocket.bal.txt` |
| **New file** | `websocket/new/ballerina_websocket.bal.txt` |
| **Old lines** | 831 |
| **New lines** | 988 |
| **Lines added** | 203 |
| **Lines removed** | 46 |
| **Hunks** | 12 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 19 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 31 | 0 |
| `// --- section ---` markers | 5 | 7 |

### Declarations added (35)

- `annotation DispatcherConfig`
- `annotation ServiceConfig`
- `class CustomCloseFrameType`
- `class Listener`
- `class PredefinedCloseFrameType`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function onBinaryMessage`
- `function onClose`
- `function onError`
- `function onIdleTimeout`
- `function onMessage`
- `function onOpen`
- `function onPing`
- `function onPong`
- `function onTextMessage`
- `type AuthError`
- `type AuthnError`
- `type AuthzError`
- `type ConnectionClosureError`
- `type ConnectionError`
- `type CorruptedFrameError`
- `type Error`
- `type HandshakeTimedOut`
- `type InvalidContinuationFrameError`
- `type InvalidHandshakeError`
- `type PayloadBindingError`
- `type PayloadTooLargeError`
- `type PayloadValidationError`
- `type ReadTimedOutError`
- `type SslError`
- `type UpgradeError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 319–325 | 319–325 | Types | +1 | −1 |
| 2 | 419–428 | 419–428 | Types | +2 | −2 |
| 3 | 431–437 | 431–438 | Types | +2 | −1 |
| 4 | 440–446 | 441–448 | Types | +2 | −1 |
| 5 | 491–497 | 493–499 | Types | +1 | −1 |
| 6 | 526–534 | 528–536 | Types | +3 | −3 |
| 7 | 543–579 | 545–597 | Types | +33 | −17 |
| 8 | 617–624 | 635–642 | Types | +2 | −2 |
| 9 | 673–680 | 691–723 | Types | +26 | −1 |
| 10 | 711–748 | 754–791 | Client | +9 | −9 |
| 11 | 769–803 | 812–846 | Client | +8 | −8 |
| 12 | 829–831 | 872–988 | Functions | +114 | −0 |

---

## Unified diff

`````diff
--- websocket/old/ballerina_websocket.bal.txt	2026-08-12 12:57:29
+++ websocket/new/ballerina_websocket.bal.txt	2026-08-12 13:19:19
@@ -319,7 +319,7 @@
 };
 
 # Defines the authentication configurations for the WebSocket listener.
-type ListenerAuthConfig ballerina/websocket:2.15.5:FileUserStoreConfigWithScopes|ballerina/websocket:2.15.5:LdapUserStoreConfigWithScopes|ballerina/websocket:2.15.5:JwtValidatorConfigWithScopes|ballerina/websocket:2.15.5:OAuth2IntrospectionConfigWithScopes;
+type ListenerAuthConfig FileUserStoreConfigWithScopes|LdapUserStoreConfigWithScopes|JwtValidatorConfigWithScopes|OAuth2IntrospectionConfigWithScopes;
 
 # Configurations used to define dispatching rules for remote functions.
 # 
@@ -419,10 +419,10 @@
 };
 
 # Represents OAuth2 grant configurations for OAuth2 authentication.
-type OAuth2GrantConfig ballerina/websocket:2.15.5:OAuth2ClientCredentialsGrantConfig|ballerina/websocket:2.15.5:OAuth2PasswordGrantConfig|ballerina/websocket:2.15.5:OAuth2RefreshTokenGrantConfig|ballerina/websocket:2.15.5:OAuth2JwtBearerGrantConfig;
+type OAuth2GrantConfig OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
 # Defines the authentication configurations for the WebSocket client.
-type ClientAuthConfig ballerina/websocket:2.15.5:CredentialsConfig|ballerina/websocket:2.15.5:BearerTokenConfig|ballerina/websocket:2.15.5:JwtIssuerConfig|ballerina/websocket:2.15.5:OAuth2ClientCredentialsGrantConfig|ballerina/websocket:2.15.5:OAuth2PasswordGrantConfig|ballerina/websocket:2.15.5:OAuth2RefreshTokenGrantConfig|ballerina/websocket:2.15.5:OAuth2JwtBearerGrantConfig;
+type ClientAuthConfig CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
 
 type CustomCloseFrame record {
@@ -431,7 +431,8 @@
     string reason?;
 };
 
-// Unknown type: CustomCloseFrameType
+class CustomCloseFrameType {
+}
 
 
 type NormalClosure record {
@@ -440,7 +441,8 @@
     string reason?;
 };
 
-// Unknown type: PredefinedCloseFrameType
+class PredefinedCloseFrameType {
+}
 
 
 type GoingAway record {
@@ -491,7 +493,7 @@
     string reason?;
 };
 
-type CloseFrame ballerina/websocket:2.15.5:NormalClosure|ballerina/websocket:2.15.5:GoingAway|ballerina/websocket:2.15.5:ProtocolError|ballerina/websocket:2.15.5:UnsupportedData|ballerina/websocket:2.15.5:InvalidPayload|ballerina/websocket:2.15.5:PolicyViolation|ballerina/websocket:2.15.5:MessageTooBig|ballerina/websocket:2.15.5:InternalServerError|ballerina/websocket:2.15.5:CustomCloseFrame;
+type CloseFrame NormalClosure|GoingAway|ProtocolError|UnsupportedData|InvalidPayload|PolicyViolation|MessageTooBig|InternalServerError|CustomCloseFrame;
 
 # Provides a set of configurations for HTTP service endpoints.
 # 
@@ -526,9 +528,9 @@
 
 type ListenerSecureSocket record {
     crypto:KeyStore|http:CertKey key; // Special Agent Note: KeyStore FROM ballerina/crypto package, CertKey FROM ballerina/http package
-    record {|ballerina/http:2.16.6:VerifyClient verifyClient; ballerina/crypto:2.12.1:TrustStore|string cert;|} mutualSsl?;
-    record {|ballerina/http:2.16.6:Protocol name; string[] versions;|} protocol?;
-    record {|ballerina/http:2.16.6:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|http:VerifyClient verifyClient; crypto:TrustStore|string cert;|} mutualSsl?;
+    record {|http:Protocol name; string[] versions;|} protocol?;
+    record {|http:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     string[] ciphers?;
     boolean shareSession?;
     decimal handshakeTimeout?;
@@ -543,37 +545,53 @@
     int maxEntityBodySize?;
 };
 
-// Unknown type: Error
+# Represents any error related to the WebSocket module.
+type Error error;
 
-// Unknown type: InvalidHandshakeError
+# Raised during the handshake when the WebSocket upgrade fails.
+type InvalidHandshakeError error;
 
-// Unknown type: PayloadTooLargeError
+# Raised when receiving a frame with a payload exceeding the maximum size.
+type PayloadTooLargeError error;
 
-// Unknown type: CorruptedFrameError
+# Raised when the other side breaks the protocol.
+type CorruptedFrameError error;
 
-// Unknown type: ConnectionError
+# Raised during connection failures.
+type ConnectionError error;
 
-// Unknown type: ConnectionClosureError
-
-// Unknown type: InvalidContinuationFrameError
+# Raised during failures in connection closure.
+type ConnectionClosureError error;
 
-// Unknown type: UpgradeError
+# Raised when an out of order/invalid continuation frame is received.
+type InvalidContinuationFrameError error;
 
-// Unknown type: HandshakeTimedOut
+# Raised when the WebSocket upgrade is not accepted.
+type UpgradeError error;
 
-// Unknown type: ReadTimedOutError
+# Raised when the initial WebSocket handshake timed out.
+type HandshakeTimedOut error;
 
-// Unknown type: AuthError
+# Raised when the client read time out reaches.
+type ReadTimedOutError error;
 
-// Unknown type: AuthnError
+# Defines the Auth error types that returned from the client.
+type AuthError error;
 
-// Unknown type: AuthzError
+# Defines the authentication error type that returned from the listener.
+type AuthnError error;
 
-// Unknown type: SslError
+# Defines the authorization error type that returned from the listener.
+type AuthzError error;
 
-// Unknown type: PayloadBindingError
+# Raised when the SSL handshake fails.
+type SslError error;
+
+# Represents an error, which occurred due to payload binding.
+type PayloadBindingError error;
 
-// Unknown type: PayloadValidationError
+# Represents an error, which occurred due to payload constraint validation.
+type PayloadValidationError error;
 
 # Common client configurations for WebSocket clients.
 # 
@@ -617,8 +635,8 @@
     boolean enable?;
     crypto:TrustStore|string cert?; // Special Agent Note: TrustStore FROM ballerina/crypto package
     crypto:KeyStore|http:CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package, CertKey FROM ballerina/http package
-    record {|ballerina/http:2.16.6:Protocol name; string[] versions;|} protocol?;
-    record {|ballerina/http:2.16.6:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|http:Protocol name; string[] versions;|} protocol?;
+    record {|http:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     string[] ciphers?;
     boolean verifyHostName?;
     boolean shareSession?;
@@ -673,8 +691,33 @@
 class UpgradeService {
 }
 
-// Unknown type: Listener
+# Gets invoked during the module initialization to initialize the listener.
+# 
+class Listener {
+    function init(int|http:Listener 'listener, string host = "0.0.0.0", ListenerHttp1Settings http1Settings = {}, ListenerSecureSocket secureSocket = {'key: {path: "", password: ""}}, decimal timeout = 120, string|() server = (), boolean webSocketCompressionEnabled = true, RequestLimitConfigs requestLimits = {}, ListenerConfiguration config) returns Error?; // Special Agent Note: Listener FROM ballerina/http package
 
+    # Starts the registered service programmatically.
+    # 
+    function 'start() returns error?;
+
+    # Stops the service listener gracefully. Already-accepted requests will be served before connection closure.
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the service listener immediately. It is not implemented yet.
+    # 
+    function immediateStop() returns error?;
+
+    # Attaches a service to the listener.
+    # 
+    function attach(UpgradeService websocketService, string[]|string|() name = ()) returns error?;
+
+    # Detaches a WebSocket service from the listener. Note that detaching a WebSocket service would not affect
+    # The functionality of the existing connections.
+    # 
+    function detach(UpgradeService websocketService) returns error?;
+}
+
 // --- Client ---
 
 # Represents a WebSocket caller.
@@ -711,38 +754,38 @@
 
     # Sets a connection related attribute.
     # 
-    remote function setAttribute(string key, value:Cloneable value) returns ();
+    function setAttribute(string key, value:Cloneable value) returns ();
 
     # Gets connection related attribute if any.
     # 
-    remote function getAttribute(string key) returns Cloneable?;
+    function getAttribute(string key) returns Cloneable?;
 
     # Removes connection related attribute if any.
     # 
-    remote function removeAttribute(string key) returns Cloneable?;
+    function removeAttribute(string key) returns Cloneable?;
 
     # Gives the connection id associated with this connection.
     # 
-    remote function getConnectionId() returns string;
+    function getConnectionId() returns string;
 
     # Gives the subprotocol if any that is negotiated with the client.
     # 
-    remote function getNegotiatedSubProtocol() returns string?;
+    function getNegotiatedSubProtocol() returns string?;
 
     # Gives the secured status of the connection.
     # 
-    remote function isSecure() returns boolean;
+    function isSecure() returns boolean;
 
     # Gives the open or closed status of the connection.
     # 
-    remote function isOpen() returns boolean;
+    function isOpen() returns boolean;
 }
 
 # Represents a WebSocket synchronous client endpoint.
 client class Client {
-    function init(string url, string[] subProtocols = [], map<string> customHeaders = {}, decimal readTimeout = 0.0d, decimal writeTimeout = 0.0d, ClientSecureSocket|() secureSocket = (), int maxFrameSize = 0, boolean webSocketCompressionEnabled = false, decimal handShakeTimeout = 0.0d, http:Cookie[] cookies = [], ClientAuthConfig auth = {username: "", password: ""}, PingPongService pingPongHandler = object {}, WebSocketRetryConfig|() retryConfig = (), boolean validation = false, ClientConfiguration config) returns ballerina/websocket:2.15.5:Error?; // Special Agent Note: Cookie FROM ballerina/http package
+    function init(string url, string[] subProtocols = [], map<string> customHeaders = {}, decimal readTimeout = 0.0d, decimal writeTimeout = 0.0d, ClientSecureSocket|() secureSocket = (), int maxFrameSize = 0, boolean webSocketCompressionEnabled = false, decimal handShakeTimeout = 0.0d, http:Cookie[] cookies = [], ClientAuthConfig auth = {username: "", password: ""}, PingPongService pingPongHandler = object {}, WebSocketRetryConfig|() retryConfig = (), boolean validation = false, ClientConfiguration config) returns Error?; // Special Agent Note: Cookie FROM ballerina/http package
 
-    remote function initEndpoint() returns Error|();
+    function initEndpoint() returns Error|();
 
     # Writes text messages to the connection. If an error occurs while sending the text message to the connection, that message
     # will be lost.
@@ -769,35 +812,35 @@
 
     # Sets a connection-related attribute.
     # 
-    remote function setAttribute(string key, string|int value) returns ();
+    function setAttribute(string key, string|int value) returns ();
 
     # Gets connection-related attributes if any.
     # 
-    remote function getAttribute(string key) returns string|int?;
+    function getAttribute(string key) returns string|int?;
 
     # Removes connection related attribute if any.
     # 
-    remote function removeAttribute(string key) returns string|int?;
+    function removeAttribute(string key) returns string|int?;
 
     # Gives the connection id associated with this connection.
     # 
-    remote function getConnectionId() returns string;
+    function getConnectionId() returns string;
 
     # Gives the subprotocol if any that is negotiated with the client.
     # 
-    remote function getNegotiatedSubProtocol() returns string?;
+    function getNegotiatedSubProtocol() returns string?;
 
     # Gives the secured status of the connection.
     # 
-    remote function isSecure() returns boolean;
+    function isSecure() returns boolean;
 
     # Gives the open or closed status of the connection.
     # 
-    remote function isOpen() returns boolean;
+    function isOpen() returns boolean;
 
     # Gives the HTTP response if any received for the client handshake request.
     # 
-    remote function getHttpResponse() returns http:Response|(); // Special Agent Note: Response FROM ballerina/http package
+    function getHttpResponse() returns http:Response|(); // Special Agent Note: Response FROM ballerina/http package
 
     # Reads text messages in a synchronous manner.
     # 
@@ -829,3 +872,117 @@
 # 
 # + config - Represents the cookies to be added
 function addCookies(ClientConfiguration config) returns ();
+
+// --- Service ---
+
+# The service identifier requires a base path, e.g. `/orders` — replace `/basePath`.
+# Optional: this service may carry the @websocket:ServiceConfig annotation. Replace {...} with its fields, which are those of websocket:WSServiceConfig.
+@websocket:ServiceConfig {...} // optional
+service websocket:UpgradeService /basePath on new websocket:Listener(int|http:Listener 'listener, websocket:ListenerConfiguration config = {}) {
+    # The only handler an upgrade service has. Runs on the initial HTTP request and decides whether to upgrade the connection. Return the service that will handle the resulting connection, or an UpgradeError to reject the upgrade.
+    # Resource: the accessor must be one of `get`; a path is required and is author-chosen — replace `pathSegment`.
+    # + request - The HTTP request that initiated the upgrade, inspect its headers here to authenticate or route before accepting.
+    # Required parameters: none — every parameter in the signature may be omitted.
+    # Optional parameters (may be omitted): request
+    resource function get pathSegment(http:Request request) returns websocket:Service|websocket:UpgradeError; // required
+}
+
+# onMessage and onTextMessage cannot coexist, onMessage already receives text frames.
+# onMessage and onBinaryMessage cannot coexist, onMessage already receives binary frames.
+// This service type is never attached to a listener — no listener in this library declares it.
+// Write it as a `service class` that includes the type, and return an instance of that class
+// wherever a `websocket:Service` is required.
+service class ServiceImpl {
+    *websocket:Service;
+
+    // This service type takes any number of remote handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, each following one of these 2 shapes:
+    //
+    // Shape 1 of 2:
+    // A custom dispatched handler. When the service config sets a dispatcherKey, the value of that field in an inbound message picks the handler by name: the value is camel cased and prefixed with on, so an event of "heartbeat" reaches onHeartbeat. A DispatcherConfig annotation overrides that derivation with an explicit dispatcherValue. A message matching nothing falls back to onMessage, or is ignored when that is absent too.
+    // + caller - Handle for sending messages back over this connection.
+    // + message - The inbound message, bound to the declared type.
+    // Required parameters: message
+    // Optional parameters (may be omitted): caller
+    // A handler may carry @websocket:DispatcherConfig. Its fields are those of websocket:WsDispatcherConfig.
+    // @websocket:DispatcherConfig {} // optional
+    // remote function <handlerName>(websocket:Caller caller, anydata message) returns anydata|websocket:CloseFrame|error?;
+    //
+    // Shape 2 of 2:
+    // A custom error handler, paired to a dispatched handler by name: that handler's name plus Error, so onHeartbeat pairs with onHeartbeatError. It receives the binding failure for that message type. Without it the failure falls back to onError.
+    // + caller - Handle for sending messages back over this connection.
+    // + err - The failure that prevented the message from binding.
+    // Required parameters: err
+    // Optional parameters (may be omitted): caller
+    // remote function <handlerName>(websocket:Caller caller, error err) returns error?;
+
+    # Invoked once, after the handshake completes and the connection is established.
+    # + caller - Handle for sending messages back over this connection.
+    # Required parameters: none — every parameter in the signature may be omitted.
+    # Optional parameters (may be omitted): caller
+    remote function onOpen(websocket:Caller caller) returns error? { } // optional
+
+    # Invoked for every inbound message, text or binary alike. Declaring this handler rules out onTextMessage and onBinaryMessage, it already covers both. It is also the fallback for a custom message type that matched no dispatched handler.
+    # + caller - Handle for sending messages back over this connection.
+    # + data - The inbound message. A text frame deserializes straight to the declared type. A binary frame is read as bytes and then deserialized, unless the declared type is byte[]. A binding failure closes the connection with status 1003.
+    # Required parameters: data
+    # Optional parameters (may be omitted): caller
+    remote function onMessage(websocket:Caller caller, anydata data) returns anydata|websocket:CloseFrame|error? { } // optional
+
+    # Invoked for every inbound text frame.
+    # + caller - Handle for sending messages back over this connection.
+    # + text - The text frame's content.
+    # Required parameters: text
+    # Optional parameters (may be omitted): caller
+    remote function onTextMessage(websocket:Caller caller, string text) returns anydata|websocket:CloseFrame|error? { } // optional
+
+    # Invoked for every inbound binary frame.
+    # + caller - Handle for sending messages back over this connection.
+    # + data - The binary frame's content.
+    # Required parameters: data
+    # Optional parameters (may be omitted): caller
+    remote function onBinaryMessage(websocket:Caller caller, byte[] data) returns anydata|websocket:CloseFrame|error? { } // optional
+
+    # Invoked when the peer sends a ping frame. Declaring it makes replying your responsibility, without it the library sends the pong automatically.
+    # + caller - Handle for sending messages back over this connection.
+    # + data - The ping frame's application data.
+    # Required parameters: data
+    # Optional parameters (may be omitted): caller
+    remote function onPing(websocket:Caller caller, byte[] data) returns error? { } // optional
+
+    # Invoked when the peer sends a pong frame, normally in reply to a ping this service sent.
+    # + caller - Handle for sending messages back over this connection.
+    # + data - The pong frame's application data.
+    # Required parameters: data
+    # Optional parameters (may be omitted): caller
+    remote function onPong(websocket:Caller caller, byte[] data) { } // optional
+
+    # Invoked when no message has arrived for the idleTimeout set in the service config. The listener's own timeout does not trigger it, that one covers only the initial upgrade request.
+    # + caller - Handle for sending messages back over this connection.
+    # Required parameters: none — every parameter in the signature may be omitted.
+    # Optional parameters (may be omitted): caller
+    remote function onIdleTimeout(websocket:Caller caller) returns error? { } // optional
+
+    # Invoked when a close frame arrives from the peer.
+    # + caller - Handle for this connection, already closing, sends will not reach the peer.
+    # + statusCode - The WebSocket close status code the peer sent.
+    # + reason - The human-readable close reason the peer sent.
+    # Required parameters: statusCode, reason
+    # Optional parameters (may be omitted): caller
+    remote function onClose(websocket:Caller caller, int statusCode, string reason) { } // optional
+
+    # Invoked when the connection fails, always preceded by a connection closure with the matching close frame. Also the fallback for a binding failure when no matching custom error handler is declared.
+    # + caller - Handle for sending messages back over this connection.
+    # + err - The failure that interrupted the connection.
+    # Required parameters: err
+    # Optional parameters (may be omitted): caller
+    remote function onError(websocket:Caller caller, error err) returns error? { } // optional
+}
+
+// --- Annotations ---
+
+# The annotation which is used to configure a WebSocket service.
+public annotation WSServiceConfig ServiceConfig on service;
+
+# The annotation which is used to configure the dispatching rules for WebSocket remote functions.
+public annotation WsDispatcherConfig DispatcherConfig on function;
`````

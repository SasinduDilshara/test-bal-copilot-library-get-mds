# mcp — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mcp` |
| **Old file** | `mcp/old/ballerina_mcp.bal.txt` |
| **New file** | `mcp/new/ballerina_mcp.bal.txt` |
| **Old lines** | 1058 |
| **New lines** | 1258 |
| **Lines added** | 239 |
| **Lines removed** | 39 |
| **Hunks** | 10 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 28 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 22 | 0 |
| `// --- section ---` markers | 6 | 6 |

### Declarations added (47)

- `annotation StreamableHttpServiceConfig`
- `annotation Tool`
- `class Listener`
- `class Session`
- `class StreamableHttpListener`
- `function 'start`
- `function attach`
- `function clear`
- `function detach`
- `function get`
- `function getSessionId`
- `function getWithType`
- `function gracefulStop`
- `function hasKey`
- `function immediateStop`
- `function isEmpty`
- `function keys`
- `function onCallTool`
- `function onListTools`
- `function remove`
- `function set`
- `function size`
- `type ClientError`
- `type ClientInitializationError`
- `type Cursor`
- `type Error`
- `type HttpClientError`
- `type InvalidMessageTypeError`
- `type JsonRpcMessageTransformationError`
- `type ListToolsError`
- `type MalformedResponseError`
- `type MissingSseDataError`
- `type ParameterBindingError`
- `type ProtocolVersionError`
- `type ResponseParsingError`
- `type ServerError`
- `type ServerResponseError`
- `type SessionOperationError`
- `type SseEventStreamError`
- `type SseStreamEstablishmentError`
- `type StreamError`
- `type StreamableHttpTransportError`
- `type ToolCallError`
- `type TransportError`
- `type TypeConversionError`
- `type UninitializedTransportError`
- `type UnsupportedContentTypeError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 345–397 | 345–422 | Types | +50 | −25 |
| 2 | 458–464 | 483–489 | Types | +1 | −1 |
| 3 | 703–709 | 728–734 | Types | +1 | −1 |
| 4 | 714–720 | 739–746 | Types | +2 | −1 |
| 5 | 798–807 | 824–833 | Types | +2 | −2 |
| 6 | 821–830 | 847–856 | Types | +2 | −2 |
| 7 | 992–997 | 1018–1027 | Types | +4 | −0 |
| 8 | 1014–1030 | 1044–1152 | Types | +96 | −4 |
| 9 | 1032–1038 | 1154–1160 | Client | +1 | −1 |
| 10 | 1049–1058 | 1171–1258 | Client | +80 | −2 |

---

## Unified diff

`````diff
--- mcp/old/ballerina_mcp.bal.txt	2026-08-12 12:57:29
+++ mcp/new/ballerina_mcp.bal.txt	2026-08-12 13:19:19
@@ -345,53 +345,78 @@
 # Task-augmented execution is required for this tool.
 const string TASK_SUPPORT_REQUIRED = "required";
 
-// Unknown type: Error
+# Defines the common base error type for this module.
+type Error error;
 
-// Unknown type: ClientError
+# Error for failures occurring within client operations.
+type ClientError error;
 
-// Unknown type: StreamError
+# Error for failures during streaming operations.
+type StreamError Error & ClientError;
 
-// Unknown type: TransportError
+# Error for failures during transport operations.
+type TransportError error;
 
-// Unknown type: ServerResponseError
-
-// Unknown type: SseEventStreamError
+# Error for invalid or unexpected responses from the server.
+type ServerResponseError Error & ClientError;
 
-// Unknown type: JsonRpcMessageTransformationError
+# Error for failures while processing SSE event streams.
+type SseEventStreamError error;
 
-// Unknown type: MissingSseDataError
+# Error for JSON-RPC message transformation failures during streaming.
+type JsonRpcMessageTransformationError error;
 
-// Unknown type: TypeConversionError
+# Error when required data is missing from an SSE event.
+type MissingSseDataError error;
+
+# Error for failures converting JSON to JsonRpcMessage.
+type TypeConversionError error;
 
-// Unknown type: InvalidMessageTypeError
+# Error when an invalid message type is received from the server.
+type InvalidMessageTypeError error;
 
-// Unknown type: MalformedResponseError
+# Error when the server response is malformed or unexpected.
+type MalformedResponseError error;
 
-// Unknown type: StreamableHttpTransportError
+# Error for failures during HTTP transport operations.
+type StreamableHttpTransportError TransportError & ClientError;
 
-// Unknown type: HttpClientError
+# Error for failures during HTTP client operations.
+type HttpClientError error;
 
-// Unknown type: UnsupportedContentTypeError
+# Error for unsupported content types in HTTP responses.
+type UnsupportedContentTypeError error;
 
-// Unknown type: SessionOperationError
+# Error for failures during session operations.
+type SessionOperationError error;
 
-// Unknown type: ResponseParsingError
+# Error for failures while parsing HTTP response content.
+type ResponseParsingError error;
 
-// Unknown type: SseStreamEstablishmentError
+# Error for failures during SSE stream establishment.
+type SseStreamEstablishmentError error;
 
-// Unknown type: UninitializedTransportError
+# Error for operations attempted before transport initialization.
+type UninitializedTransportError error;
 
-// Unknown type: ClientInitializationError
+# Error for failures during client initialization.
+type ClientInitializationError error;
 
-// Unknown type: ProtocolVersionError
+# Error for protocol version negotiation failures.
+type ProtocolVersionError error;
 
-// Unknown type: ListToolsError
+# Error for failures during tool listing operations.
+type ListToolsError error;
 
-// Unknown type: ToolCallError
+# Error for failures during tool execution operations.
+type ToolCallError error;
 
-// Unknown type: ServerError
+# Errors for failures occurring during server operations.
+type ServerError error;
 
-// Unknown type: ParameterBindingError
+# Error for failures while binding tool parameters from the incoming request,
+# such as missing or invalid header values.
+type ParameterBindingError error;
 
 # Represents a generic request in the protocol
 
@@ -458,7 +483,7 @@
     # The JSON-RPC protocol version
     "2.0" jsonrpc;
     # Identifier of the request
-    ballerina/mcp:1.2.0:RequestId? id;
+    RequestId? id;
     # The error information
     record {|int code; string message; anydata data?; anydata...;|} 'error;
 };
@@ -703,7 +728,7 @@
 };
 
 # A content block that can be text, image, audio, resource link, or embedded resource.
-type ContentBlock ballerina/mcp:1.2.0:TextContent|ballerina/mcp:1.2.0:ImageContent|ballerina/mcp:1.2.0:AudioContent|ballerina/mcp:1.2.0:ResourceLink|ballerina/mcp:1.2.0:EmbeddedResource;
+type ContentBlock TextContent|ImageContent|AudioContent|ResourceLink|EmbeddedResource;
 
 # Result that supports pagination
 
@@ -714,7 +739,8 @@
     record {|anydata...;|} _meta?;
 };
 
-// Unknown type: Cursor
+# An opaque token used to represent a cursor for pagination.
+type Cursor string;
 
 # The server's response to a tools/list request from the client.
 
@@ -798,10 +824,10 @@
 };
 
 # Represents a result sent from the server to the client.
-type ServerResult ballerina/mcp:1.2.0:InitializeResult|ballerina/mcp:1.2.0:CallToolResult|ballerina/mcp:1.2.0:ListToolsResult;
+type ServerResult InitializeResult|CallToolResult|ListToolsResult;
 
 # Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.
-type JsonRpcMessage ballerina/mcp:1.2.0:JsonRpcRequest|ballerina/mcp:1.2.0:JsonRpcNotification|ballerina/mcp:1.2.0:JsonRpcError|ballerina/mcp:1.2.0:JsonRpcResponse;
+type JsonRpcMessage JsonRpcRequest|JsonRpcNotification|JsonRpcError|JsonRpcResponse;
 
 # Configuration options for initializing an MCP listener.
 
@@ -821,10 +847,10 @@
 };
 
 # Represents a non-error type that can be cloned.
-type Cloneable any & readonly|xml|ballerina/mcp:1.2.0:Cloneable[]|map<ballerina/mcp:1.2.0:Cloneable>|table<map<ballerina/mcp:1.2.0:Cloneable>>;
+type Cloneable any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>;
 
 # Represents the type of a value stored in the `Session` object.
-type SessionEntry any & readonly|xml|ballerina/mcp:1.2.0:Cloneable[]|map<ballerina/mcp:1.2.0:Cloneable>|table<map<ballerina/mcp:1.2.0:Cloneable>>|isolated object {};
+type SessionEntry any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>|isolated object {};
 
 # Configuration options for the Streamable HTTP client transport.
 # 
@@ -992,6 +1018,10 @@
 # Defines a transport-agnostic MCP service interface that handles incoming MCP requests with
 # manual control over tool listing and invocation.
 class AdvancedService {
+
+    remote function onListTools() returns ListToolsResult|ServerError;
+
+    remote function onCallTool(CallToolParams params, Session|() session = ()) returns CallToolResult|ServerError;
 }
 
 # Defines a transport-agnostic basic MCP service interface. Tools are declared as `remote`
@@ -1014,17 +1044,109 @@
 class StreamableHttpAdvancedService {
 }
 
-// Unknown type: StreamableHttpListener
+# Initializes the Listener.
+# 
+class StreamableHttpListener {
+    function init(int|http:Listener listenTo, string host = "", http:ListenerHttp1Settings http1Settings = {}, http:ListenerSecureSocket|() secureSocket = (), http:HttpVersion httpVersion = "2.0", decimal timeout = 0.0d, string|() server = (), http:RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0.0d, http:ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 0, decimal minIdleTimeInStaleState = 0.0d, decimal timeBetweenStaleEviction = 0.0d, ListenerConfiguration config) returns Error?; // Special Agent Note: Listener, ListenerHttp1Settings, ListenerSecureSocket, HttpVersion, RequestLimitConfigs, ServerSocketConfig FROM ballerina/http package
 
-// Unknown type: Listener
+    # Attaches an MCP service to the listener under the specified path(s).
+    # 
+    function attach(Service|AdvancedService|StreamableHttpService|StreamableHttpAdvancedService mcpService, string[]|string|() name = ()) returns Error|();
 
-// Unknown type: Session
+    # Detaches the MCP service from the listener.
+    # 
+    function detach(Service|AdvancedService|StreamableHttpService|StreamableHttpAdvancedService mcpService) returns Error|();
+
+    # Starts the listener (begin accepting connections).
+    # 
+    function 'start() returns Error|();
+
+    # Gracefully stops the listener (completes active requests before shutting down).
+    # 
+    function gracefulStop() returns Error|();
+
+    # Immediately stops the listener (terminates all connections).
+    # 
+    function immediateStop() returns Error|();
+}
+
+# Initializes the Listener.
+# 
+@deprecated
+class Listener {
+    function init(int|http:Listener listenTo, string host = "", http:ListenerHttp1Settings http1Settings = {}, http:ListenerSecureSocket|() secureSocket = (), http:HttpVersion httpVersion = "2.0", decimal timeout = 0.0d, string|() server = (), http:RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0.0d, http:ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 0, decimal minIdleTimeInStaleState = 0.0d, decimal timeBetweenStaleEviction = 0.0d, ListenerConfiguration config) returns Error?; // Special Agent Note: Listener, ListenerHttp1Settings, ListenerSecureSocket, HttpVersion, RequestLimitConfigs, ServerSocketConfig FROM ballerina/http package
+
+    # Attaches an MCP service to the listener under the specified path(s).
+    # 
+    function attach(Service|AdvancedService|StreamableHttpService|StreamableHttpAdvancedService mcpService, string[]|string|() name = ()) returns Error|();
+
+    # Detaches the MCP service from the listener.
+    # 
+    function detach(Service|AdvancedService|StreamableHttpService|StreamableHttpAdvancedService mcpService) returns Error|();
+
+    # Starts the listener (begin accepting connections).
+    # 
+    function 'start() returns Error|();
+
+    # Gracefully stops the listener (completes active requests before shutting down).
+    # 
+    function gracefulStop() returns Error|();
 
+    # Immediately stops the listener (terminates all connections).
+    # 
+    function immediateStop() returns Error|();
+}
+
+# Creates a new MCP session with the given session ID.
+# 
+class Session {
+    function init(string sessionId) returns ();
+
+    # Gets the session ID.
+    # 
+    function getSessionId() returns string;
+
+    # Adds or updates an entry in the session.
+    # 
+    function set(string key, SessionEntry value) returns ();
+
+    # Retrieves a value from the session by key. Panics if the key does not exist.
+    # 
+    function get(string key) returns SessionEntry;
+
+    # Checks if the session contains an entry for the given key.
+    # 
+    function hasKey(string key) returns boolean;
+
+    # Returns all the keys currently stored in the session.
+    # 
+    function keys() returns string[];
+
+    # Retrieves and casts a value from the session to the specified type.
+    # 
+    function getWithType(string key, any & readonly|xml|mcp:Cloneable[]|map<mcp:Cloneable>|table<map<mcp:Cloneable>>|isolated object {} targetType = mcp:SessionEntry) returns targetType|Error;
+
+    # Removes the entry associated with the given key. Panics if the key does not exist.
+    # 
+    function remove(string key) returns ();
+
+    # Gets the number of entries in the session.
+    # 
+    function size() returns int;
+
+    # Clears all entries from the session.
+    function clear() returns ();
+
+    # Checks if the session is empty.
+    # 
+    function isEmpty() returns boolean;
+}
+
 // --- Client ---
 
 # Represents an MCP client built on top of the Streamable HTTP transport.
 client class StreamableHttpClient {
-    function init(string serverUrl, http:HttpVersion httpVersion = "2.0", http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", http:FollowRedirects|() followRedirects = (), http:PoolConfiguration|() poolConfig = (), http:CacheConfig cache = {}, http:Compression compression = "AUTO", http:CredentialsConfig|http:BearerTokenConfig|http:JwtIssuerConfig|http:OAuth2ClientCredentialsGrantConfig|http:OAuth2PasswordGrantConfig|http:OAuth2RefreshTokenGrantConfig|http:OAuth2JwtBearerGrantConfig|() auth = (), http:CircuitBreakerConfig|() circuitBreaker = (), http:RetryConfig|() retryConfig = (), http:CookieConfig|() cookieConfig = (), http:ResponseLimitConfigs responseLimits = {}, http:ProxyConfig|() proxy = (), boolean validation = false, http:ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, http:ClientSecureSocket|() secureSocket = (), string sessionId = "", StreamableHttpClientTransportConfig config) returns ballerina/mcp:1.2.0:ClientError?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, CacheConfig, Compression, CredentialsConfig, BearerTokenConfig, JwtIssuerConfig, OAuth2ClientCredentialsGrantConfig, OAuth2PasswordGrantConfig, OAuth2RefreshTokenGrantConfig, OAuth2JwtBearerGrantConfig, CircuitBreakerConfig, RetryConfig, CookieConfig, ResponseLimitConfigs, ProxyConfig, ClientSocketConfig, ClientSecureSocket FROM ballerina/http package
+    function init(string serverUrl, http:HttpVersion httpVersion = "2.0", http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", http:FollowRedirects|() followRedirects = (), http:PoolConfiguration|() poolConfig = (), http:CacheConfig cache = {}, http:Compression compression = "AUTO", http:CredentialsConfig|http:BearerTokenConfig|http:JwtIssuerConfig|http:OAuth2ClientCredentialsGrantConfig|http:OAuth2PasswordGrantConfig|http:OAuth2RefreshTokenGrantConfig|http:OAuth2JwtBearerGrantConfig|() auth = (), http:CircuitBreakerConfig|() circuitBreaker = (), http:RetryConfig|() retryConfig = (), http:CookieConfig|() cookieConfig = (), http:ResponseLimitConfigs responseLimits = {}, http:ProxyConfig|() proxy = (), boolean validation = false, http:ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, http:ClientSecureSocket|() secureSocket = (), string sessionId = "", StreamableHttpClientTransportConfig config) returns ClientError?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, CacheConfig, Compression, CredentialsConfig, BearerTokenConfig, JwtIssuerConfig, OAuth2ClientCredentialsGrantConfig, OAuth2PasswordGrantConfig, OAuth2RefreshTokenGrantConfig, OAuth2JwtBearerGrantConfig, CircuitBreakerConfig, RetryConfig, CookieConfig, ResponseLimitConfigs, ProxyConfig, ClientSocketConfig, ClientSecureSocket FROM ballerina/http package
 
     # Initializes the MCP connection by performing protocol handshake and capability exchange.
     # 
@@ -1032,7 +1154,7 @@
 
     # Opens a server-sent events (SSE) stream for asynchronous server-to-client communication.
     # 
-    remote function subscribeToServerMessages() returns stream<ballerina/mcp:1.2.0:JsonRpcMessage, ballerina/mcp:1.2.0:StreamError?>|ClientError;
+    remote function subscribeToServerMessages() returns stream<JsonRpcMessage, StreamError?>|ClientError;
 
     # Retrieves the list of available tools from the server.
     # 
@@ -1049,10 +1171,88 @@
 
 // --- Service ---
 
-service mcp:Service on new mcp:Listener(int|http:Listener listenTo = 0, ListenerConfiguration config = {}) {
+// This library declares 4 service types. Each is individually optional —
+// declare the ones the requirement needs, not all of them.
+
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# Optional: this service may carry the @mcp:ServiceConfig annotation. Replace {...} with its fields, which are those of mcp:ServiceConfiguration.
+@mcp:ServiceConfig {...} // optional
+service mcp:Service on new mcp:StreamableHttpListener(int|http:Listener listenTo, mcp:ListenerConfiguration config = {}) {
+    // This service type takes any number of remote handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, following this shape:
+    // One remote method per MCP tool. The method name becomes the tool name and its parameters become the tool's input schema, both discovered automatically, with no explicit registration.
+    // + session - The client session, when the server is running in a stateful session mode.
+    // Zero or more further parameters of type anydata may be added, each independently named.
+    // Required parameters: none — every parameter in the signature may be omitted.
+    // Optional parameters (may be omitted): session
+    // A handler may carry @mcp:Tool. Its fields are those of mcp:McpToolConfig.
+    // @mcp:Tool {} // optional
+    // remote function <handlerName>(mcp:Session session) returns anydata|error;
 }
 
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# Optional: this service may carry the @mcp:ServiceConfig annotation. Replace {...} with its fields, which are those of mcp:ServiceConfiguration.
+@mcp:ServiceConfig {...} // optional
+service mcp:AdvancedService on new mcp:StreamableHttpListener(int|http:Listener listenTo, mcp:ListenerConfiguration config = {}) {
+    isolated remote function onListTools() returns mcp:ListToolsResult|mcp:ServerError;
+
+    # Required parameters: params
+    # Optional parameters (may be omitted): session
+    isolated remote function onCallTool(mcp:CallToolParams params, mcp:Session|() session) returns mcp:CallToolResult|mcp:ServerError;
+}
+
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# Optional: this service may carry the @mcp:StreamableHttpServiceConfig annotation. Replace {...} with its fields, which are those of mcp:StreamableHttpServiceConfiguration.
+@mcp:StreamableHttpServiceConfig {...} // optional
+service mcp:StreamableHttpService on new mcp:StreamableHttpListener(int|http:Listener listenTo, mcp:ListenerConfiguration config = {}) {
+    // This service type takes any number of remote handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, following this shape:
+    // One remote method per MCP tool, served over the streamable HTTP transport. Tool name and input schema are discovered from the method signature.
+    // + session - The client session, when the server is running in a stateful session mode.
+    // + headers - Read-only access to the inbound HTTP request headers.
+    // + request - The raw inbound HTTP request, for anything the bound parameters do not expose.
+    // Zero or more further parameters of type anydata may be added, each independently named.
+    // Zero or more further parameters (the `@http:Header` slot) of type string (or int, boolean, decimal, float) may be added, each independently named.
+    // Each repeated `string` parameter may carry @http:Header, written `@http:Header {}` before its type. Its fields are those of http:HttpHeader. Special Agent Note: Header, HttpHeader FROM ballerina/http package
+    // Required parameters: none — every parameter in the signature may be omitted.
+    // Optional parameters (may be omitted): session, headers, request
+    // A handler may carry @mcp:Tool. Its fields are those of mcp:McpToolConfig.
+    // @mcp:Tool {} // optional
+    // remote function <handlerName>(mcp:Session session, http:Headers headers, http:Request request) returns anydata|error;
+}
+
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# Optional: this service may carry the @mcp:StreamableHttpServiceConfig annotation. Replace {...} with its fields, which are those of mcp:StreamableHttpServiceConfiguration.
+@mcp:StreamableHttpServiceConfig {...} // optional
+service mcp:StreamableHttpAdvancedService on new mcp:StreamableHttpListener(int|http:Listener listenTo, mcp:ListenerConfiguration config = {}) {
+    # Invoked when a client asks for this server's tool catalogue. Use this when the catalogue is computed at runtime rather than discovered from remote methods.
+    # + headers - Read-only access to the inbound HTTP request headers.
+    # + request - The raw inbound HTTP request, for anything the bound parameters do not expose.
+    # Zero or more further parameters (the `@http:Header` slot) of type string (or int, boolean, decimal, float) may be added, each independently named.
+    # Each repeated `string` parameter may carry @http:Header, written `@http:Header {}` before its type. Its fields are those of http:HttpHeader. Special Agent Note: Header, HttpHeader FROM ballerina/http package
+    # Required parameters: none — every parameter in the signature may be omitted.
+    # Optional parameters (may be omitted): headers, request
+    remote function onListTools(http:Headers headers, http:Request request) returns mcp:ListToolsResult|mcp:ServerError; // required
+
+    # Invoked when a client invokes a tool by name. Dispatching to the right implementation and binding the arguments are the service's own responsibility here, unlike the automatic form.
+    # + params - The tool name and the arguments the client supplied for it.
+    # + session - The client session, when the server is running in a stateful session mode.
+    # + headers - Read-only access to the inbound HTTP request headers.
+    # + request - The raw inbound HTTP request, for anything the bound parameters do not expose.
+    # Zero or more further parameters (the `@http:Header` slot) of type string (or int, boolean, decimal, float) may be added, each independently named.
+    # Each repeated `string` parameter may carry @http:Header, written `@http:Header {}` before its type. Its fields are those of http:HttpHeader. Special Agent Note: Header, HttpHeader FROM ballerina/http package
+    # Required parameters: params
+    # Optional parameters (may be omitted): session, headers, request
+    remote function onCallTool(mcp:CallToolParams params, mcp:Session session, http:Headers headers, http:Request request) returns mcp:CallToolResult|mcp:ServerError; // required
+}
+
 // --- Annotations ---
 
-# Define mcp service configuration
+# Annotation to mark a function as an MCP tool configuration.
+public annotation McpToolConfig Tool on object function;
+
+# Annotation to provide configuration to MCP services.
 public annotation ServiceConfiguration ServiceConfig on service;
+
+# Annotation to provide configuration to Streamable HTTP MCP services.
+public annotation StreamableHttpServiceConfiguration StreamableHttpServiceConfig on service;
`````

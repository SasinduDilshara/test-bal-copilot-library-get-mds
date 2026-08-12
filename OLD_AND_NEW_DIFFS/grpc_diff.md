# grpc — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `grpc` |
| **Old file** | `grpc/old/ballerina_grpc.bal.txt` |
| **New file** | `grpc/new/ballerina_grpc.bal.txt` |
| **Old lines** | 1239 |
| **New lines** | 1406 |
| **Lines added** | 214 |
| **Lines removed** | 47 |
| **Hunks** | 14 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 29 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 25 | 0 |
| `// --- section ---` markers | 5 | 7 |

### Declarations added (40)

- `annotation Descriptor`
- `annotation ServiceConfig`
- `annotation ServiceDescriptor`
- `class ClientBasicAuthHandler`
- `class ClientBearerTokenAuthHandler`
- `class ClientSelfSignedJwtAuthHandler`
- `class Listener`
- `class ListenerFileUserStoreBasicAuthHandler`
- `class ListenerJwtAuthHandler`
- `function 'start`
- `function attach`
- `function authenticate`
- `function authorize`
- `function detach`
- `function enrich`
- `function gracefulStop`
- `function immediateStop`
- `type AbortedError`
- `type AllRetryAttemptsFailed`
- `type AlreadyExistsError`
- `type CancelledError`
- `type ClientAuthError`
- `type DataLossError`
- `type DataMismatchError`
- `type DeadlineExceededError`
- `type Error`
- `type ErrorType`
- `type FailedPreconditionError`
- `type InternalError`
- `type InvalidArgumentError`
- `type NotFoundError`
- `type OutOfRangeError`
- `type PermissionDeniedError`
- `type ResiliencyError`
- `type ResourceExhaustedError`
- `type StreamClosedError`
- `type UnKnownError`
- `type UnauthenticatedError`
- `type UnavailableError`
- `type UnimplementedError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 551–557 | 551–557 | Types | +1 | −1 |
| 2 | 643–663 | 643–711 | Types | +56 | −8 |
| 3 | 692–700 | 740–750 | Types | +4 | −2 |
| 4 | 727–735 | 777–785 | Types | +2 | −2 |
| 5 | 788–834 | 838–905 | Types | +42 | −21 |
| 6 | 986–996 | 1057–1067 | Types | +3 | −3 |
| 7 | 1002–1009 | 1073–1123 | Types | +44 | −1 |
| 8 | 1040–1053 | 1154–1166 | Client | +1 | −2 |
| 9 | 1068–1074 | 1181–1187 | Client | +1 | −1 |
| 10 | 1080–1093 | 1193–1206 | Client | +2 | −2 |
| 11 | 1101–1107 | 1214–1220 | Client | +1 | −1 |
| 12 | 1122–1128 | 1235–1241 | Client | +1 | −1 |
| 13 | 1130–1142 | 1243–1254 | Client | +1 | −2 |
| 14 | 1237–1239 | 1349–1406 | Functions | +55 | −0 |

---

## Unified diff

`````diff
--- grpc/old/ballerina_grpc.bal.txt	2026-08-12 12:57:29
+++ grpc/new/ballerina_grpc.bal.txt	2026-08-12 13:19:19
@@ -551,7 +551,7 @@
 };
 
 # Defines the authentication configurations for the gRPC listener.
-type ListenerAuthConfig ballerina/grpc:1.14.7:FileUserStoreConfigWithScopes|ballerina/grpc:1.14.7:LdapUserStoreConfigWithScopes|ballerina/grpc:1.14.7:JwtValidatorConfigWithScopes|ballerina/grpc:1.14.7:OAuth2IntrospectionConfigWithScopes;
+type ListenerAuthConfig FileUserStoreConfigWithScopes|LdapUserStoreConfigWithScopes|JwtValidatorConfigWithScopes|OAuth2IntrospectionConfigWithScopes;
 
 # Represents credentials for Basic Auth authentication.
 
@@ -643,21 +643,69 @@
 };
 
 # Represents OAuth2 grant configurations for OAuth2 authentication.
-type OAuth2GrantConfig ballerina/grpc:1.14.7:OAuth2ClientCredentialsGrantConfig|ballerina/grpc:1.14.7:OAuth2PasswordGrantConfig|ballerina/grpc:1.14.7:OAuth2RefreshTokenGrantConfig|ballerina/grpc:1.14.7:OAuth2JwtBearerGrantConfig;
+type OAuth2GrantConfig OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
 # Defines the authentication configurations for the HTTP client.
-type ClientAuthConfig ballerina/grpc:1.14.7:CredentialsConfig|ballerina/grpc:1.14.7:BearerTokenConfig|ballerina/grpc:1.14.7:JwtIssuerConfig|ballerina/grpc:1.14.7:OAuth2ClientCredentialsGrantConfig|ballerina/grpc:1.14.7:OAuth2PasswordGrantConfig|ballerina/grpc:1.14.7:OAuth2RefreshTokenGrantConfig|ballerina/grpc:1.14.7:OAuth2JwtBearerGrantConfig;
+type ClientAuthConfig CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
-// Unknown type: ClientBasicAuthHandler
-
-// Unknown type: ClientBearerTokenAuthHandler
+# Initializes the Basic Auth handler for client authentication.
+# 
+class ClientBasicAuthHandler {
+    function init(CredentialsConfig config) returns ();
 
-// Unknown type: ClientSelfSignedJwtAuthHandler
+    # Enriches the headers with the relevant authentication requirements.
+    # 
+    function enrich(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+}
 
-// Unknown type: ListenerFileUserStoreBasicAuthHandler
+# Initializes the Bearer token auth handler for client authentication.
+# 
+class ClientBearerTokenAuthHandler {
+    function init(BearerTokenConfig config) returns ();
+
+    # Enriches the headers with the relevant authentication requirements.
+    # 
+    function enrich(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+}
 
-// Unknown type: ListenerJwtAuthHandler
+# Initializes the self-signed JWT handler for client authentication.
+# 
+class ClientSelfSignedJwtAuthHandler {
+    function init(JwtIssuerConfig config) returns ();
+
+    # Enriches the headers with the relevant authentication requirements.
+    # 
+    function enrich(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+}
+
+# Initializes the `grpc:ListenerFileUserStoreBasicAuthHandler` object.
+# 
+class ListenerFileUserStoreBasicAuthHandler {
+    function init(FileUserStoreConfig config = {}) returns ();
+
+    # Authenticates with the relevant authentication requirements.
+    # 
+    function authenticate(map<string|string[]> headers) returns auth:UserDetails|UnauthenticatedError; // Special Agent Note: UserDetails FROM ballerina/auth package
 
+    # Authorizes with the relevant authorization requirements.
+    # 
+    function authorize(auth:UserDetails userDetails, string|string[] expectedScopes) returns PermissionDeniedError|(); // Special Agent Note: UserDetails FROM ballerina/auth package
+}
+
+# Initializes the JWT auth handler for the listener authentication.
+# 
+class ListenerJwtAuthHandler {
+    function init(JwtValidatorConfig config) returns ();
+
+    # Authenticates with the relevant authentication requirements.
+    # 
+    function authenticate(map<string|string[]> headers) returns jwt:Payload|UnauthenticatedError; // Special Agent Note: Payload FROM ballerina/jwt package
+
+    # Authorizes with the relevant authorization requirements.
+    # 
+    function authorize(jwt:Payload jwtPayload, string|string[] expectedScopes) returns PermissionDeniedError|(); // Special Agent Note: Payload FROM ballerina/jwt package
+}
+
 # Configurations for managing the gRPC client connection pool.
 # 
 
@@ -692,9 +740,11 @@
     ErrorType[] errorTypes?;
 };
 
-// Unknown type: Error
+# Represents gRPC related errors.
+type Error error;
 
-// Unknown type: ErrorType
+# Represents gRPC related error types.
+type ErrorType typedesc<Error>;
 
 # Configurations for managing the gRPC client endpoint.
 # 
@@ -727,9 +777,9 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and private key of the client
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerina/grpc:1.14.7:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # Certificate validation against OCSP_CRL, OCSP_STAPLING related options
-    record {|ballerina/grpc:1.14.7:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     # List of ciphers to be used
 eg: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     string[] ciphers?;
@@ -788,47 +838,68 @@
     REQUIRE
 }
 
-// Unknown type: CancelledError
+# Represents the operation canceled(typically by the caller) error.
+type CancelledError error;
 
-// Unknown type: UnKnownError
+# Represents unknown error(e.g., Status value received is unknown).
+type UnKnownError error;
 
-// Unknown type: InvalidArgumentError
+# Represents client specified an invalid argument error.
+type InvalidArgumentError error;
 
-// Unknown type: DeadlineExceededError
+# Represents operation expired before completion error.
+type DeadlineExceededError error;
 
-// Unknown type: NotFoundError
+# Represents requested entity (e.g., file or directory) not found error.
+type NotFoundError error;
 
-// Unknown type: AlreadyExistsError
+# Represents error occur when attempt to create an entity which already exists.
+type AlreadyExistsError error;
 
-// Unknown type: PermissionDeniedError
+# Represents error occur when the caller does not have permission to execute the specified operation.
+type PermissionDeniedError error;
 
-// Unknown type: UnauthenticatedError
+# Represents error occur when the request does not have valid authentication credentials for the operation.
+type UnauthenticatedError error;
 
-// Unknown type: ResourceExhaustedError
+# Represents error occur when the resource is exhausted.
+type ResourceExhaustedError error;
 
-// Unknown type: FailedPreconditionError
+# Represents error occur when operation is rejected because the system is not in a state required for the operation's execution.
+type FailedPreconditionError error;
 
-// Unknown type: AbortedError
+# Represents error occur when operation is aborted.
+type AbortedError error;
 
-// Unknown type: OutOfRangeError
+# Represents error occur when specified value is out of range.
+type OutOfRangeError error;
 
-// Unknown type: UnimplementedError
+# Represents error occur when operation is not implemented or not supported/enabled in this service.
+type UnimplementedError error;
 
-// Unknown type: InternalError
+# Represents internal error.
+type InternalError error;
 
-// Unknown type: UnavailableError
+# Represents error occur when the service is currently unavailable.
+type UnavailableError error;
 
-// Unknown type: DataLossError
+# Represents unrecoverable data loss or corruption erros.
+type DataLossError error;
 
-// Unknown type: ResiliencyError
+# Represents all the resiliency-related errors.
+type ResiliencyError error;
 
-// Unknown type: AllRetryAttemptsFailed
+# Represents error scenario where the maximum retry attempts are done and still received an error.
+type AllRetryAttemptsFailed error;
 
-// Unknown type: StreamClosedError
+# Represents an error when calling next when the stream has closed.
+type StreamClosedError error;
 
-// Unknown type: DataMismatchError
+# Represents an error when expected data type is not available.
+type DataMismatchError error;
 
-// Unknown type: ClientAuthError
+# Represents an error when client authentication error occured.
+type ClientAuthError error;
 
 # Represents gRPC trace log configuration.
 # 
@@ -986,11 +1057,11 @@
     # Configurations associated with a `crypto:KeyStore` or combination of a certificate and private key of the server
     crypto:KeyStore|CertKey key; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # Configurations associated with mutual SSL operations
-    record {|ballerina/grpc:1.14.7:VerifyClient verifyClient; ballerina/crypto:2.12.1:TrustStore|string cert;|} mutualSsl?;
+    record {|VerifyClient verifyClient; crypto:TrustStore|string cert;|} mutualSsl?;
     # SSL/TLS protocol related options
-    record {|ballerina/grpc:1.14.7:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # Certificate validation against OCSP_CRL, OCSP_STAPLING related options
-    record {|ballerina/grpc:1.14.7:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     # List of ciphers to be used
 eg: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     string[] ciphers?;
@@ -1002,8 +1073,51 @@
     decimal sessionTimeout?;
 };
 
-// Unknown type: Listener
+# Gets called when the endpoint is being initialized during the module init time.
+# ```ballerina
+# listener grpc:Listener listenerEp = new (9092);
+# ```
+# 
+class Listener {
+    function init(int port, string host = "0.0.0.0", ListenerSecureSocket|() secureSocket = (), decimal timeout = 120, int maxInboundMessageSize = 4194304, int maxHeaderSize = 8192, boolean reflectionEnabled = false, ListenerConfiguration config) returns error?;
 
+    # Starts the registered service.
+    # ```ballerina
+    # error? result = listenerEp.'start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Stops the service listener gracefully. Already-accepted requests will be served before the connection closure.
+    # ```ballerina
+    # error? result = listenerEp.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the registered service.
+    # ```ballerina
+    # error? result = listenerEp.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Gets called every time a service attaches itself to this endpoint - also happens at module init time.
+    # ```ballerina
+    # error? result = listenerEp.attach(helloService);
+    # ```
+    # 
+    function attach(Service grpcService, string[]|string|() name = ()) returns error?;
+
+    # Detaches an HTTP or WebSocket service from the listener. Note that detaching a WebSocket service would not affect
+    # the functionality of the existing connections.
+    # ```ballerina
+    # error? result = listenerEp.detach(helloService);
+    # ```
+    # 
+    function detach(Service grpcService) returns error?;
+}
+
 // --- Client ---
 
 # Defines the OAuth2 handler for client authentication.
@@ -1040,14 +1154,13 @@
 # The base client used in the generated client code to provide remote functions for interacting with the caller.
 # 
 client class Caller {
-    function init() returns ballerina/grpc:grpc:Caller;
 
     # Returns the unique identification of the caller.
     # ```ballerina
     # int result = caller.getId();
     # ```
     # 
-    remote function getId() returns int;
+    function getId() returns int;
 
     # Sends the outbound response to the caller.
     # ```ballerina
@@ -1068,7 +1181,7 @@
     # boolean result = caller.isCancelled();
     # ```
     # 
-    remote function isCancelled() returns boolean;
+    function isCancelled() returns boolean;
 
     # Sends a server error to the caller.
     # ```ballerina
@@ -1080,14 +1193,14 @@
 
 # The base client used in the generated client code to provide the capability for initiating the contact and executing remote calls with a remote gRPC service.
 client class Client {
-    function init(string url, decimal timeout = 60, PoolConfiguration|() poolConfig = (), ClientSecureSocket|() secureSocket = (), Compression compression = AUTO, RetryConfiguration|() retryConfiguration = (), CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), int maxInboundMessageSize = 4194304, ClientConfiguration config) returns ballerina/grpc:1.14.7:Error?;
+    function init(string url, decimal timeout = 60, PoolConfiguration|() poolConfig = (), ClientSecureSocket|() secureSocket = (), Compression compression = AUTO, RetryConfiguration|() retryConfiguration = (), CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), int maxInboundMessageSize = 4194304, ClientConfiguration config) returns Error?;
 
     # Calls when initializing the client endpoint with the service descriptor data extracted from the proto file.
     # ```ballerina
     # grpc:Error? result = grpcClient.initStub(self, ROOT_DESCRIPTOR, getDescriptorMap());
     # ```
     # 
-    remote function initStub(AbstractClientEndpoint clientEndpoint, string descriptorKey, map<any> descriptorMap = {}) returns Error|();
+    function initStub(AbstractClientEndpoint clientEndpoint, string descriptorKey, map<any> descriptorMap = {}) returns Error|();
 
     # Calls when executing a unary gRPC service.
     # ```ballerina
@@ -1101,7 +1214,7 @@
     # [stream<anydata, grpc:Error?>, map<string|string[]>]|grpc:Error result = grpcClient->executeServerStreaming("HelloWorld/hello", req, headers);
     # ```
     # 
-    remote function executeServerStreaming(string methodID, anydata payload, map<string|string[]> headers = {}) returns [stream<anydata, ballerina/grpc:1.14.7:Error?>, map<string|string[]>]|Error;
+    remote function executeServerStreaming(string methodID, anydata payload, map<string|string[]> headers = {}) returns [stream<anydata, Error?>, map<string|string[]>]|Error;
 
     # Calls when executing a client streaming call with a gRPC service.
     # ```ballerina
@@ -1122,7 +1235,7 @@
 client class ServerReflectionServerReflectionResponseCaller {
     function init(Caller caller) returns ();
 
-    remote function getId() returns int;
+    function getId() returns int;
 
     remote function sendServerReflectionResponse(ServerReflectionResponse response) returns Error|();
 
@@ -1130,13 +1243,12 @@
 
     remote function complete() returns Error|();
 
-    remote function isCancelled() returns boolean;
+    function isCancelled() returns boolean;
 }
 
 # The base client used in the generated client code to provide the gRPC streaming client actions for
 # interacting  with the gRPC server.
 client class StreamingClient {
-    function init() returns ballerina/grpc:grpc:StreamingClient;
 
     # Sends the request message to the server.
     # ```ballerina
@@ -1237,3 +1349,58 @@
 # + headerName - The header name
 # + return - Header value array
 function getHeaders(map<string|string[]> headerMap, string headerName) returns string[]|Error;
+
+// --- Service ---
+
+# The service identifier requires a quoted string literal, e.g. `"orders"` — replace `"identifier"`.
+# Mandatory: this service must carry the @grpc:Descriptor annotation. Replace {...} with its fields, which are those of grpc:DescriptorData.
+# Optional: this service may carry the @grpc:ServiceConfig annotation. Replace {...} with its fields, which are those of grpc:GrpcServiceConfig.
+@grpc:Descriptor {...} // required
+@grpc:ServiceConfig {...} // optional
+service grpc:Service "identifier" on new grpc:Listener(int port, grpc:ListenerConfiguration config = {}) {
+    // This service type takes any number of remote handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, each following one of these 4 shapes:
+    //
+    // Shape 1 of 4:
+    // Handles a simple RPC, one request message in and one response message out. The method name is the RPC name from the proto definition. Return the response directly, or take a caller and send through it, in which case the method returns error? instead.
+    // + caller - Generated caller for this RPC, used to send the response asynchronously. Must come first when present. Declaring it changes the return type to error?.
+    // + request - The inbound request message. Absent when the RPC input is google.protobuf.Empty.
+    // Required parameters: none — every parameter in the signature may be omitted.
+    // Optional parameters (may be omitted): caller, request
+    // remote function <handlerName>(grpc:Caller caller, anydata request) returns anydata|error?;
+    //
+    // Shape 2 of 4:
+    // Handles a server streaming RPC, one request message in and a stream of response messages out. Return the stream directly, or take a caller and send each message through it, in which case the method returns error? instead.
+    // + caller - Generated caller for this RPC, used to send each response message. Must come first when present. Declaring it changes the return type to error?.
+    // + request - The inbound request message. Absent when the RPC input is google.protobuf.Empty.
+    // Required parameters: none — every parameter in the signature may be omitted.
+    // Optional parameters (may be omitted): caller, request
+    // remote function <handlerName>(grpc:Caller caller, anydata request) returns stream<anydata, grpc:Error?>|error?;
+    //
+    // Shape 3 of 4:
+    // Handles a client streaming RPC, a stream of request messages in and one response message out. Return the response directly, or take a caller and send through it, in which case the method returns error? instead.
+    // + caller - Generated caller for this RPC, used to send the response asynchronously. Must come first when present. Declaring it changes the return type to error?.
+    // + clientStream - The inbound request messages, consumed as a stream.
+    // Required parameters: clientStream
+    // Optional parameters (may be omitted): caller
+    // remote function <handlerName>(grpc:Caller caller, stream<anydata, grpc:Error?> clientStream) returns anydata|error?;
+    //
+    // Shape 4 of 4:
+    // Handles a bidirectional streaming RPC, with request and response messages flowing independently in both directions. Taking a caller is the practical form here, since it lets responses be sent while the request stream is still being consumed.
+    // + caller - Generated caller for this RPC, used to send response messages while the request stream is still open. Must come first when present. Declaring it changes the return type to error?.
+    // + clientStream - The inbound request messages, consumed as a stream.
+    // Required parameters: clientStream
+    // Optional parameters (may be omitted): caller
+    // remote function <handlerName>(grpc:Caller caller, stream<anydata, grpc:Error?> clientStream) returns stream<anydata, grpc:Error?>|error?;
+}
+
+// --- Annotations ---
+
+# Service descriptor annotation.
+public annotation ServiceDescriptorData ServiceDescriptor on service;
+
+# Service descriptor annotation.
+public annotation DescriptorData Descriptor on service;
+
+# The annotation which is used to configure a gRPC service.
+public annotation GrpcServiceConfig ServiceConfig on service;
`````

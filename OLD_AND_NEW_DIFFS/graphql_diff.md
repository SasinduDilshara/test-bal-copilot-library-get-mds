# graphql — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `graphql` |
| **Old file** | `graphql/old/ballerina_graphql.bal.txt` |
| **New file** | `graphql/new/ballerina_graphql.bal.txt` |
| **Old lines** | 1578 |
| **New lines** | 1722 |
| **Lines added** | 177 |
| **Lines removed** | 33 |
| **Hunks** | 11 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 13 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 27 | 0 |
| `// --- section ---` markers | 8 | 7 |

### Declarations added (36)

- `annotation InterceptorConfig`
- `annotation on`
- `class Context`
- `class Field`
- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function execute`
- `function get`
- `function getAlias`
- `function getDataLoader`
- `function getLocation`
- `function getName`
- `function getPath`
- `function getSubfieldNames`
- `function getSubfields`
- `function getType`
- `function gracefulStop`
- `function immediateStop`
- `function invalidate`
- `function invalidateAll`
- `function registerDataLoader`
- `function remove`
- `function resolve`
- `function set`
- `type AuthnError`
- `type AuthzError`
- `type ClientError`
- `type ContextInit`
- `type Error`
- `type HttpError`
- `type InvalidDocumentError`
- `type PayloadBindingError`
- `type RequestError`
- `type ServerError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 892–898 | 892–898 | Types | +1 | −1 |
| 2 | 1009–1017 | 1009–1061 | Types | +46 | −2 |
| 3 | 1104–1109 | 1148–1155 | Types | +2 | −0 |
| 4 | 1126–1132 | 1172–1182 | Types | +5 | −1 |
| 5 | 1165–1171 | 1215–1221 | Types | +1 | −1 |
| 6 | 1269–1297 | 1319–1357 | Types | +22 | −12 |
| 7 | 1321–1329 | 1381–1389 | Types | +3 | −3 |
| 8 | 1420–1427 | 1480–1487 | Types | +2 | −2 |
| 9 | 1504–1510 | 1564–1570 | Types | +1 | −1 |
| 10 | 1527–1541 | 1587–1650 | Types | +52 | −3 |
| 11 | 1564–1578 | 1673–1722 | Functions | +42 | −7 |

---

## Unified diff

`````diff
--- graphql/old/ballerina_graphql.bal.txt	2026-08-12 12:57:29
+++ graphql/new/ballerina_graphql.bal.txt	2026-08-12 13:19:19
@@ -892,7 +892,7 @@
 a compilation error.
     string schemaString?;
     # GraphQL service level interceptors
-    (ballerina/graphql:1.17.0:Interceptor & readonly)|(ballerina/graphql:1.17.0:Interceptor & readonly)[] & readonly interceptors?;
+    (Interceptor & readonly)|(Interceptor & readonly)[] & readonly interceptors?;
     # Whether to enable or disable the introspection on the service
     boolean introspection?;
     # Whether to enable or disable the constraint validation
@@ -1009,9 +1009,53 @@
 };
 
 # Defines the authentication configurations for the GraphQL listener.
-type ListenerAuthConfig ballerina/graphql:1.17.0:FileUserStoreConfigWithScopes|ballerina/graphql:1.17.0:LdapUserStoreConfigWithScopes|ballerina/graphql:1.17.0:JwtValidatorConfigWithScopes|ballerina/graphql:1.17.0:OAuth2IntrospectionConfigWithScopes;
+type ListenerAuthConfig FileUserStoreConfigWithScopes|LdapUserStoreConfigWithScopes|JwtValidatorConfigWithScopes|OAuth2IntrospectionConfigWithScopes;
 
-// Unknown type: Context
+class Context {
+    function init() returns ();
+
+    # Sets a given value for a given key in the GraphQL context.
+    # 
+    function set(string 'key, readonly|xml<xml:Element|xml:Comment|xml:ProcessingInstruction|xml:Text>|value:Cloneable[]|map<value:Cloneable>|table<map<value:Cloneable>>|isolated object {} value) returns ();
+
+    # Retrieves a value using the given key from the GraphQL context.
+    # ```ballerina
+    # string userId = check context.get("userId").ensureType();  
+    # ```
+    # 
+    function get(string 'key) returns readonly|xml<>|Cloneable[]|map<value:Cloneable>|table<map<value:Cloneable>>|isolated object {}|Error;
+
+    # Removes a value using the given key from the GraphQL context.
+    # ```ballerina
+    # string userId = check context.remove("userId").ensureType();  
+    # ```
+    # 
+    function remove(string 'key) returns readonly|xml<>|Cloneable[]|map<value:Cloneable>|table<map<value:Cloneable>>|isolated object {}|Error;
+
+    # Register a given DataLoader instance for a given key in the GraphQL context.
+    # ```ballerina
+    # dataloader:DataLoader userDataLoader = new dataloader:DefaultDataLoader(batchUsers);
+    # check context.registerDataLoader("user", userDataLoader);
+    # ```
+    # 
+    function registerDataLoader(string key, dataloader:DataLoader dataloader) returns (); // Special Agent Note: DataLoader FROM ballerina/graphql.dataloader package
+
+    # Retrieves a DataLoader instance using the given key from the GraphQL context.
+    # ```ballerina
+    # dataloader:DataLoader userDataLoader = check context.getDataLoader("user");
+    # ```
+    function getDataLoader(string key) returns dataloader:DataLoader; // Special Agent Note: DataLoader FROM ballerina/graphql.dataloader package
+
+    # Remove cache entries related to the given path.
+    # 
+    function invalidate(string path) returns error?;
+
+    # Remove all cache entries.
+    # 
+    function invalidateAll() returns error?;
+
+    function resolve(Field 'field) returns anydata;
+}
 
 # Represents an error in GraphQL.
 
@@ -1104,6 +1148,8 @@
 
 # Represent a GraphQL interceptor
 class Interceptor {
+
+    remote function execute(Context context, Field 'field) returns anydata|error;
 }
 
 # Represent the cache configurations of GraphQL server.
@@ -1126,7 +1172,11 @@
     boolean warnOnly?;
 };
 
-// Unknown type: ContextInit
+# Function type for initializing the `graphql:Context` object.
+# This function will be called with the `http:Request` and the `http:RequestContext` objects from the original request
+# received to the GraphQL endpoint.
+# 
+type ContextInit function (http:RequestContext requestContext, http:Request request) returns Context|error;
 
 # Represent CORS configurations for internal HTTP service
 
@@ -1165,7 +1215,7 @@
 
 type GraphqlResourceConfig record {
     # GraphQL field level interceptors
-    (ballerina/graphql:1.17.0:Interceptor & readonly)|(ballerina/graphql:1.17.0:Interceptor & readonly)[] & readonly interceptors?;
+    (Interceptor & readonly)|(Interceptor & readonly)[] & readonly interceptors?;
     # The name of the instance method to be used for prefetching
     string prefetchMethodName?;
     # The cache configurations for the fields
@@ -1269,29 +1319,39 @@
 };
 
 # Represents OAuth2 grant configurations for OAuth2 authentication.
-type OAuth2GrantConfig ballerina/graphql:1.17.0:OAuth2ClientCredentialsGrantConfig|ballerina/graphql:1.17.0:OAuth2PasswordGrantConfig|ballerina/graphql:1.17.0:OAuth2RefreshTokenGrantConfig|ballerina/graphql:1.17.0:OAuth2JwtBearerGrantConfig;
+type OAuth2GrantConfig OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
 # Defines the authentication configurations for the GraphQL client.
-type ClientAuthConfig ballerina/graphql:1.17.0:CredentialsConfig|ballerina/graphql:1.17.0:BearerTokenConfig|ballerina/graphql:1.17.0:JwtIssuerConfig|ballerina/graphql:1.17.0:OAuth2ClientCredentialsGrantConfig|ballerina/graphql:1.17.0:OAuth2PasswordGrantConfig|ballerina/graphql:1.17.0:OAuth2RefreshTokenGrantConfig|ballerina/graphql:1.17.0:OAuth2JwtBearerGrantConfig;
+type ClientAuthConfig CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
-// Unknown type: Error
+# Represents any error related to the Ballerina GraphQL module.
+type Error error;
 
-// Unknown type: AuthnError
+# Represents the authentication error type.
+type AuthnError error;
 
-// Unknown type: AuthzError
+# Represents the authorization error type.
+type AuthzError error;
 
-// Unknown type: ClientError
+# Represents GraphQL client related generic errors.
+type ClientError error;
 
-// Unknown type: RequestError
+# Represents GraphQL client side or network level errors.
+type RequestError error;
 
-// Unknown type: HttpError
+# Represents network level errors.
+type HttpError error<record {|anydata body;|}>;
 
-// Unknown type: InvalidDocumentError
-
-// Unknown type: ServerError
+# Represents GraphQL errors due to request validation.
+type InvalidDocumentError error<record {|ErrorDetail[]? errors;|}>;
 
-// Unknown type: PayloadBindingError
+# Represents GraphQL API response during GraphQL API server side errors.
+@deprecated
+type ServerError error<record {|json? data?; ErrorDetail[] errors; map<json>? extensions?;|}>;
 
+# Represents client side data binding error.
+type PayloadBindingError error<record {|ErrorDetail[]? errors;|}>;
+
 # Provides a set of configurations for configure the underlying HTTP listener of the GraphQL listener.
 
 type ListenerConfiguration record {
@@ -1321,9 +1381,9 @@
 
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
@@ -1420,8 +1480,8 @@
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
@@ -1504,7 +1564,7 @@
     # File stream encoding
     string encoding;
     # File content as a stream of `byte[]`
-    stream<byte[], ballerina/io:1.8.1:Error?> byteStream;
+    stream<byte[], io:Error?> byteStream;
 };
 
 # Represents the target type binding record with data and extensions of a GraphQL response for `executeWithType` method.
@@ -1527,15 +1587,64 @@
     record {|anydata...;|}|map<json?> data?;
 };
 
-// Unknown type: Field
+class Field {
+    function init(parser:FieldNode internalNode, __Type fieldType, __Type parentType, service object {}|() serviceObject = (), (string|int)[] & readonly path = [], parser:RootOperationType operationType = parser:OPERATION_QUERY, string[] resourcePath = [], any|error fieldValue = (), ServerCacheConfig|() cacheConfig = (), string[] & readonly parentArgHashes = [], boolean isAlreadyCached = false) returns (); // Special Agent Note: FieldNode, RootOperationType FROM ballerina/graphql.parser package
 
-// Unknown type: Listener
+    # Returns the name of the field.
+    function getName() returns string;
 
+    # Returns the effective alias of the field.
+    function getAlias() returns string;
+
+    # Returns the current path of the field. If the field returns an array, the path will include the index of the
+    # element.
+    function getPath() returns (string|int)[] & readonly;
+
+    # Returns the subfields of this field as a `Field` object array.
+    function getSubfields() returns Field[]|();
+
+    # Returns the names of the subfields of this field as a string array.
+    function getSubfieldNames() returns string[];
+
+    # Returns the type of the field.
+    function getType() returns __Type;
+
+    # Returns the location of the field in the GraphQL document.
+    function getLocation() returns Location;
+}
+
+# Invoked during the initialization of a `graphql:Listener`. Either an `http:Listener` or a port number must be
+# provided to initialize the listener.
+# 
+class Listener {
+    function init(int|http:Listener listenTo, string host = "", http:ListenerHttp1Settings http1Settings = {}, http:ListenerSecureSocket|() secureSocket = (), http:HttpVersion httpVersion = "2.0", decimal timeout = 0.0d, string|() server = (), http:RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0.0d, http:ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 0, decimal minIdleTimeInStaleState = 0.0d, decimal timeBetweenStaleEviction = 0.0d, ListenerConfiguration configuration) returns Error?; // Special Agent Note: Listener, ListenerHttp1Settings, ListenerSecureSocket, HttpVersion, RequestLimitConfigs, ServerSocketConfig FROM ballerina/http package
+
+    # Attaches the provided service to the Listener.
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns Error|();
+
+    # Detaches the provided service from the Listener.
+    # 
+    function detach(Service s) returns Error|();
+
+    # Starts the attached service.
+    # 
+    function 'start() returns Error|();
+
+    # Gracefully stops the graphql listener. Already accepted requests will be served before the connection closure.
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the service listener immediately.
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # The Ballerina GraphQL client that can be used to communicate with GraphQL APIs.
 client class Client {
-    function init(string serviceUrl, ClientHttp1Settings http1Settings = {}, decimal timeout = 60, string forwarded = "disable", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = AUTO, CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ClientSecureSocket|() secureSocket = (), ProxyConfig|() proxy = (), boolean validation = true, ClientConfiguration clientConfig) returns ballerina/graphql:1.17.0:ClientError?;
+    function init(string serviceUrl, ClientHttp1Settings http1Settings = {}, decimal timeout = 60, string forwarded = "disable", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = AUTO, CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ClientSecureSocket|() secureSocket = (), ProxyConfig|() proxy = (), boolean validation = true, ClientConfiguration clientConfig) returns ClientError?;
 
     # Executes a GraphQL document and data binds the GraphQL response to a record with data and extensions
     # which is a subtype of GenericResponse.
@@ -1564,15 +1673,50 @@
 
 // --- Service ---
 
-// --- Service (generic) ---
-// Service Type: Service
-// Listener: graphql:Listener(int|http:Listener listenTo, ListenerConfiguration configuration)
-// Instructions:
+# The service identifier requires a base path, e.g. `/orders` — replace `/basePath`.
+# Optional: this service may carry the @graphql:ServiceConfig annotation. Replace {...} with its fields, which are those of graphql:GraphqlServiceConfig.
+@graphql:ServiceConfig {...} // optional
+service graphql:Service /basePath on new graphql:Listener(int|http:Listener listenTo, graphql:ListenerConfiguration configuration = {}) {
+    // This service type takes any number of handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, each following one of these 3 shapes:
+    //
+    // Shape 1 of 3:
+    // One resource method per GraphQL query field. The field name is the resource path, and the return type becomes that field's type in the generated schema.
+    // Resource: the accessor must be one of `get`; a path is required and is author-chosen — replace `pathSegment`.
+    // Zero or more further parameters (the `@graphql:ID` slot) of type anydata may be added, each independently named.
+    // Each repeated `anydata` parameter may carry @graphql:ID, written `@graphql:ID {}` before its type.
+    // A handler may carry @graphql:ResourceConfig. Its fields are those of graphql:GraphqlResourceConfig.
+    // @graphql:ResourceConfig {} // optional
+    // resource function get pathSegment() returns anydata|error;
+    //
+    // Shape 2 of 3:
+    // One remote method per GraphQL mutation field. Remote methods are exposed as mutations; resource methods are queries.
+    // Zero or more further parameters (the `@graphql:ID` slot) of type anydata may be added, each independently named.
+    // Each repeated `anydata` parameter may carry @graphql:ID, written `@graphql:ID {}` before its type.
+    // A handler may carry @graphql:ResourceConfig. Its fields are those of graphql:GraphqlResourceConfig.
+    // @graphql:ResourceConfig {} // optional
+    // remote function <handlerName>() returns anydata|error;
+    //
+    // Shape 3 of 3:
+    // One subscribe resource method per GraphQL subscription field. Each value emitted on the returned stream is delivered to subscribed clients as one update.
+    // Resource: the accessor must be one of `subscribe`; a path is required and is author-chosen — replace `pathSegment`.
+    // Zero or more further parameters (the `@graphql:ID` slot) of type anydata may be added, each independently named.
+    // Each repeated `anydata` parameter may carry @graphql:ID, written `@graphql:ID {}` before its type.
+    // A handler may carry @graphql:ResourceConfig. Its fields are those of graphql:GraphqlResourceConfig.
+    // @graphql:ResourceConfig {} // optional
+    // resource function subscribe pathSegment() returns stream<anydata, error?>;
+}
 
 // --- Annotations ---
 
-# Define service configurations such as maximum query depth.
+# The annotation to configure a GraphQL service.
 public annotation GraphqlServiceConfig ServiceConfig on service;
 
-# Define configurations such as field level cache.
-public annotation GraphqlResourceConfig ResourceConfig on service_function;
+# The annotation to configure a GraphQL resolver.
+public annotation GraphqlResourceConfig ResourceConfig on object function;
+
+# The annotation to configure a GraphQL interceptor.
+public annotation GraphqlInterceptorConfig InterceptorConfig on class;
+
+# Represents the annotation of the ID type.
+public annotation ID on parameter, return, record field;
`````

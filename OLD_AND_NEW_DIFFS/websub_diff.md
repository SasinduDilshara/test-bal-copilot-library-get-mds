# websub — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `websub` |
| **Old file** | `websub/old/ballerina_websub.bal.txt` |
| **New file** | `websub/new/ballerina_websub.bal.txt` |
| **Old lines** | 445 |
| **New lines** | 539 |
| **Lines added** | 110 |
| **Lines removed** | 16 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 11 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 5 | 7 |

### Declarations added (23)

- `annotation SubscriberServiceConfig`
- `class Listener`
- `function 'start`
- `function attach`
- `function attachWithConfig`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function onEventNotification`
- `function onHubError`
- `function onSubscriptionValidationDenied`
- `function onSubscriptionVerification`
- `function onUnsubscriptionVerification`
- `type Error`
- `type InternalHubError`
- `type ListenerError`
- `type ResourceDiscoveryFailedError`
- `type ServiceExecutionError`
- `type SubscriptionDeletedError`
- `type SubscriptionDeniedError`
- `type SubscriptionInitiationError`
- `type SubscriptionVerificationError`
- `type UnsubscriptionVerificationError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 247–253 | 247–253 | Types | +1 | −1 |
| 2 | 367–403 | 367–465 | Types | +76 | −14 |
| 3 | 409–415 | 471–477 | Client | +1 | −1 |
| 4 | 443–445 | 505–539 | Functions | +32 | −0 |

---

## Unified diff

`````diff
--- websub/old/ballerina_websub.bal.txt	2026-08-12 12:57:29
+++ websub/new/ballerina_websub.bal.txt	2026-08-12 13:19:19
@@ -247,7 +247,7 @@
     # The configuration for the subscriber client used to interact with the discovered/specified hub
     ClientConfiguration httpConfig?;
     # HTTP client configurations for resource discovery
-    record {|string|string[] accept?; string|string[] acceptLanguage?; ballerina/websub:2.15.0:ClientConfiguration httpConfig?;|} discoveryConfig?;
+    record {|string|string[] accept?; string|string[] acceptLanguage?; ClientConfiguration httpConfig?;|} discoveryConfig?;
     # Additional parameters, which need to be sent with the subscription/unsubscription request
     map<string> customParams?;
     # Additional HTTP headers, which need to be sent with the subscription/unsubscription request
@@ -367,37 +367,99 @@
     http:Response response; // Special Agent Note: Response FROM ballerina/http package
 };
 
-// Unknown type: Error
-
-// Unknown type: ServiceExecutionError
+# Represents a webSub distinct error.
+type Error error<CommonResponse>;
 
-// Unknown type: ListenerError
+# Represents a websub service execution error.
+type ServiceExecutionError error<CommonResponse>;
+
+# Represents a listener errors.
+type ListenerError error<CommonResponse>;
 
-// Unknown type: ResourceDiscoveryFailedError
+# Represents a resource-discovery failed error.
+type ResourceDiscoveryFailedError error<CommonResponse>;
 
-// Unknown type: SubscriptionInitiationError
-
-// Unknown type: SubscriptionVerificationError
+# Represents a subscription-initiation failed error.
+type SubscriptionInitiationError error<CommonResponse>;
 
-// Unknown type: UnsubscriptionVerificationError
+# Represents a subscription verificatation error.
+type SubscriptionVerificationError error<CommonResponse>;
 
-// Unknown type: SubscriptionDeniedError
+# Represents a unsubscription verificatation error.
+type UnsubscriptionVerificationError error<CommonResponse>;
 
-// Unknown type: InternalHubError
+# Represents a subscription-denied error.
+type SubscriptionDeniedError error<CommonResponse>;
 
-// Unknown type: SubscriptionDeletedError
+# Represents an internal hub error occurred during subscription verification.
+type InternalHubError error<CommonResponse>;
+
+# Represents the subscription-delete action from the `subscriber`.
+type SubscriptionDeletedError error<CommonResponse>;
 
 # The WebSub service type.
 class SubscriberService {
 }
 
-// Unknown type: Listener
+# Initiliazes `websub:Listener` instance.
+# ```ballerina
+# listener websub:Listener websubListenerEp = check new (9090);
+# ```
+# 
+class Listener {
+    function init(int|http:Listener listenTo, string host = "", http:ListenerHttp1Settings http1Settings = {}, http:ListenerSecureSocket|() secureSocket = (), http:HttpVersion httpVersion = "2.0", decimal timeout = 0.0d, string|() server = (), http:RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0.0d, http:ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 0, decimal minIdleTimeInStaleState = 0.0d, decimal timeBetweenStaleEviction = 0.0d, decimal gracefulShutdownPeriod = 20, ListenerConfiguration config) returns Error?; // Special Agent Note: Listener, ListenerHttp1Settings, ListenerSecureSocket, HttpVersion, RequestLimitConfigs, ServerSocketConfig FROM ballerina/http package
+
+    # Attaches the provided `websub:SubscriberService` to the `websub:Listener`.
+    # ```ballerina
+    # check websubListenerEp.attach('service, "/subscriber");
+    # ```
+    # 
+    function attach(SubscriberService 'service, string[]|string|() name = ()) returns Error|();
+
+    # Attaches the provided Service to the `websub:Listener` with custom `websub:SubscriberServiceConfiguration`.
+    # ```ballerina
+    # check websubListenerEp.attachWithConfig('service, {
+    #    target: "http://0.0.0.0:9191/common/discovery",
+    #    leaseSeconds: 36000
+    # }, "/subscriber");
+    # ```
+    # 
+    function attachWithConfig(SubscriberService 'service, SubscriberServiceConfiguration configuration, string[]|string|() name = ()) returns Error|();
+
+    # Detaches the provided `websub:SubscriberService` from the `websub:Listener`.
+    # ```ballerina
+    # check websubListenerEp.detach('service);
+    # ```
+    # 
+    function detach(SubscriberService 'service) returns Error|();
 
+    # Starts the registered service programmatically..
+    # ```ballerina
+    # check websubListenerEp.'start();
+    # ```
+    # 
+    function 'start() returns Error|();
+
+    # Stops the service listener gracefully. Already-accepted requests will be served before connection closure.
+    # ```ballerina
+    # check websubListenerEp.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the service listener immediately.
+    # ```ballerina
+    # check websubListenerEp.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Represents resource-discovery service which identify the `hub` and `topic` from `resource-URL`.
 client class DiscoveryService {
-    function init(string discoveryUrl, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:FollowRedirects followRedirects = {}, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns ballerina/websub:2.15.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, ClientAuthConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
+    function init(string discoveryUrl, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:FollowRedirects followRedirects = {}, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, ClientAuthConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
 
     # Discovers the URLs of the hub and topic defined by a resource URL.
     # ```ballerina
@@ -409,7 +471,7 @@
 
 # The HTTP based client for WebSub subscription and unsubscription.
 client class SubscriptionClient {
-    function init(string url, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:FollowRedirects followRedirects = {}, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns ballerina/websub:2.15.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, ClientAuthConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
+    function init(string url, http:HttpVersion httpVersion = http:HTTP_2_0, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:FollowRedirects followRedirects = {}, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, FollowRedirects, PoolConfiguration, ClientAuthConfig, RetryConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
 
     # Sends a subscription request to the provided `hub`.
     # ```ballerina
@@ -443,3 +505,35 @@
 # + return - The header values the specified header key maps to or the `http:HeaderNotFoundError` if the header is not
 found.
 function getHeaders(ContentDistributionMessage msg, string headerName) returns string[]|http:HeaderNotFoundError; // Special Agent Note: HeaderNotFoundError FROM ballerina/http package
+
+// --- Service ---
+
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# Optional: this service may carry the @websub:SubscriberServiceConfig annotation. Replace {...} with its fields, which are those of websub:SubscriberServiceConfiguration.
+@websub:SubscriberServiceConfig {...} // optional
+service websub:SubscriberService on new websub:Listener(int|http:Listener listenTo, websub:ListenerConfiguration config = {}) {
+    # Invoked when the hub delivers a content update for a topic this subscriber is subscribed to. This is the handler that does the actual work.
+    # + event - The delivered content update, including its payload and the topic it came from.
+    remote function onEventNotification(websub:ContentDistributionMessage event) returns websub:Acknowledgement|websub:SubscriptionDeletedError?; // required
+
+    # Invoked when the hub asks this subscriber to confirm an intent to subscribe. Return success to complete the subscription, or an error to reject it.
+    # + msg - The hub's verification challenge for the pending subscription.
+    remote function onSubscriptionVerification(websub:SubscriptionVerification msg) returns websub:SubscriptionVerificationSuccess|websub:SubscriptionVerificationError; // optional
+
+    # Invoked when the hub asks this subscriber to confirm an intent to unsubscribe.
+    # + msg - The hub's verification challenge for the pending unsubscription.
+    remote function onUnsubscriptionVerification(websub:UnsubscriptionVerification msg) returns websub:UnsubscriptionVerificationSuccess|websub:UnsubscriptionVerificationError; // optional
+
+    # Invoked when the hub refuses a subscription request outright, rather than proceeding to verification.
+    # + msg - The hub's stated reason for refusing the subscription.
+    remote function onSubscriptionValidationDenied(websub:SubscriptionDeniedError msg) returns websub:Acknowledgement?; // optional
+
+    # Invoked when the hub reports a failure to this subscriber.
+    # + err - The failure the hub reported.
+    remote function onHubError(websub:InternalHubError err) returns websub:Acknowledgement?; // optional
+}
+
+// --- Annotations ---
+
+# WebSub Subscriber Configuration for the service, indicating subscription related parameters.
+public annotation SubscriberServiceConfiguration SubscriberServiceConfig on service;
`````

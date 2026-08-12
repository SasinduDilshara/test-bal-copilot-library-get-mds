# websubhub — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `websubhub` |
| **Old file** | `websubhub/old/ballerina_websubhub.bal.txt` |
| **New file** | `websubhub/new/ballerina_websubhub.bal.txt` |
| **Old lines** | 512 |
| **New lines** | 587 |
| **Lines added** | 96 |
| **Lines removed** | 21 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 18 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (25)

- `annotation ServiceConfig`
- `class Controller`
- `class Listener`
- `class StatusOK`
- `class StatusPermanentRedirect`
- `class StatusTemporaryRedirect`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function markAsVerified`
- `type BadSubscriptionError`
- `type BadUnsubscriptionError`
- `type ContentDeliveryError`
- `type Error`
- `type InternalSubscriptionError`
- `type InternalUnsubscriptionError`
- `type ServiceExecutionError`
- `type SubscriptionDeletedError`
- `type SubscriptionDeniedError`
- `type TopicDeregistrationError`
- `type TopicRegistrationError`
- `type UnsubscriptionDeniedError`
- `type UpdateMessageError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 226–232 | 226–235 | Types | +4 | −1 |
| 2 | 425–473 | 428–543 | Types | +86 | −19 |
| 3 | 479–485 | 549–555 | Client | +1 | −1 |
| 4 | 510–512 | 580–587 | Client | +5 | −0 |

---

## Unified diff

`````diff
--- websubhub/old/ballerina_websubhub.bal.txt	2026-08-12 23:21:51
+++ websubhub/new/ballerina_websubhub.bal.txt	2026-08-12 23:23:51
@@ -226,7 +226,10 @@
     string|byte[]|json|xml|map<string>? body?;
 };
 
-// Unknown type: StatusOK
+# Response status OK.
+# 
+class StatusOK {
+}
 
 # Record to represent the topic-registration request body.
 # 
@@ -425,49 +428,116 @@
     decimal timeBetweenStaleEviction?;
 };
 
-// Unknown type: Error
+# Represents a websubhub distinct error.
+type Error error<CommonResponse>;
 
-// Unknown type: ServiceExecutionError
-
-// Unknown type: TopicRegistrationError
+# Represents a websubhub service execution error.
+type ServiceExecutionError error<CommonResponse>;
 
-// Unknown type: TopicDeregistrationError
+# Error type representing the errors in the topic registration action.
+type TopicRegistrationError error<CommonResponse>;
 
-// Unknown type: BadSubscriptionError
+# Error type representing the errors in the topic unregistration action.
+type TopicDeregistrationError error<CommonResponse>;
+
+# Error type representing the errors in the subscription request.
+type BadSubscriptionError error<CommonResponse>;
 
-// Unknown type: InternalSubscriptionError
+# Error type representing the internal errors in the subscription action.
+type InternalSubscriptionError error<CommonResponse>;
 
-// Unknown type: SubscriptionDeniedError
+# Error type representing the validation errors in the subscription request body.
+type SubscriptionDeniedError error<CommonResponse>;
 
-// Unknown type: BadUnsubscriptionError
+# Error type representing the errors in the unsubscription request.
+type BadUnsubscriptionError error<CommonResponse>;
 
-// Unknown type: InternalUnsubscriptionError
+# Error type representing the internal errors in the unsubscription action.
+type InternalUnsubscriptionError error<CommonResponse>;
 
-// Unknown type: UnsubscriptionDeniedError
+# Error type representing the validation errors in the unsubscription request body.
+type UnsubscriptionDeniedError error<CommonResponse>;
 
-// Unknown type: UpdateMessageError
+# Error type representing the errors in the content update request.
+type UpdateMessageError error<CommonResponse>;
 
-// Unknown type: SubscriptionDeletedError
+# Error type representing the subscriber ending the subscription
+# by sending `HTTP 410` for the content delivery response.
+type SubscriptionDeletedError error<CommonResponse>;
 
-// Unknown type: ContentDeliveryError
+# Error type representing the internal errors in the content distribution.
+type ContentDeliveryError error<CommonResponse>;
 
 # The WebSubHub service type.
 class Service {
 }
 
-// Unknown type: StatusTemporaryRedirect
+# Response status Temporary Redirect.
+# 
+class StatusTemporaryRedirect {
+}
 
-// Unknown type: StatusPermanentRedirect
+# Response status Permanent Redirect.
+class StatusPermanentRedirect {
+}
 
-// Unknown type: Controller
+class Controller {
+    function init(boolean autoVerifySubscriptionIntent) returns ();
 
-// Unknown type: Listener
+    # Marks a particular subscription as verified.
+    # 
+    function markAsVerified(Subscription|Unsubscription subscription) returns Error|();
+}
 
+# Initiliazes the `websubhub:Listener` instance.
+# ```ballerina
+# listener websubhub:Listener hubListenerEp = check new (9090);
+# ```
+# 
+class Listener {
+    function init(int|http:Listener listenTo, string host = "", http:ListenerHttp1Settings http1Settings = {}, http:ListenerSecureSocket|() secureSocket = (), http:HttpVersion httpVersion = "2.0", decimal timeout = 0.0d, string|() server = (), http:RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0.0d, http:ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 0, decimal minIdleTimeInStaleState = 0.0d, decimal timeBetweenStaleEviction = 0.0d, ListenerConfiguration config) returns Error?; // Special Agent Note: Listener, ListenerHttp1Settings, ListenerSecureSocket, HttpVersion, RequestLimitConfigs, ServerSocketConfig FROM ballerina/http package
+
+    # Attaches the provided `websubhub:Service` to the `websubhub:Listener`.
+    # ```ballerina
+    # check hubListenerEp.attach('service, "/hub");
+    # ```
+    # 
+    function attach(Service 'service, string[]|string|() name = ()) returns Error|();
+
+    # Detaches the provided `websubhub:Service` from the `websubhub:Listener`.
+    # ```ballerina
+    # check hubListenerEp.detach('service);
+    # ```
+    # 
+    function detach(Service s) returns Error|();
+
+    # Starts the registered service programmatically.
+    # ```ballerina
+    # check hubListenerEp.'start();
+    # ```
+    # 
+    function 'start() returns Error|();
+
+    # Gracefully stops the hub listener. Already-accepted requests will be served before the connection closure.
+    # ```ballerina
+    # check hubListenerEp.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the service listener immediately.
+    # ```ballerina
+    # check hubListenerEp.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # HTTP Based client for WebSub content publishing to subscribers
 client class HubClient {
-    function init(Subscription subscription, http:HttpVersion httpVersion = 1.1, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ProxyConfig|() proxy = (), http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns ballerina/websubhub:1.16.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, ClientAuthConfig, RetryConfig, ProxyConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
+    function init(Subscription subscription, http:HttpVersion httpVersion = 1.1, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ProxyConfig|() proxy = (), http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, ClientAuthConfig, RetryConfig, ProxyConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
 
     # Distributes the published content to the subscribers.
     # ```ballerina
@@ -479,7 +549,7 @@
 
 # The HTTP based client for WebSub topic registration and deregistration, and notifying the hub of new updates.
 client class PublisherClient {
-    function init(string url, http:HttpVersion httpVersion = 1.1, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ProxyConfig|() proxy = (), http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns ballerina/websubhub:1.16.0:Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, ClientAuthConfig, RetryConfig, ProxyConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
+    function init(string url, http:HttpVersion httpVersion = 1.1, http:ClientHttp1Settings http1Settings = {}, http:ClientHttp2Settings http2Settings = {}, decimal timeout = 60, http:PoolConfiguration poolConfig = {}, http:ClientAuthConfig auth = {username: "", password: ""}, http:RetryConfig retryConfig = {}, http:ProxyConfig|() proxy = (), http:ResponseLimitConfigs responseLimits = {}, http:ClientSecureSocket secureSocket = {}, http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config) returns Error?; // Special Agent Note: HttpVersion, ClientHttp1Settings, ClientHttp2Settings, PoolConfiguration, ClientAuthConfig, RetryConfig, ProxyConfig, ResponseLimitConfigs, ClientSecureSocket, CircuitBreakerConfig FROM ballerina/http package
 
     # Registers a topic in a Ballerina WebSub Hub to which the subscribers can subscribe and the publisher will publish updates.
     # ```ballerina
@@ -510,3 +580,8 @@
     # 
     remote function notifyUpdate(string topic) returns Acknowledgement|UpdateMessageError;
 }
+
+// --- Annotations ---
+
+# WebSub Hub Configuration for the service.
+public annotation ServiceConfiguration ServiceConfig on service;
`````

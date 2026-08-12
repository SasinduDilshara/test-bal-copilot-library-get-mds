# http — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `http` |
| **Old file** | `http/old/ballerina_http.bal.txt` |
| **New file** | `http/new/ballerina_http.bal.txt` |
| **Old lines** | 3532 |
| **New lines** | 4669 |
| **Lines added** | 1368 |
| **Lines removed** | 231 |
| **Hunks** | 112 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 155 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 117 | 0 |
| `// --- section ---` markers | 8 | 7 |

### Declarations added (250)

- `annotation Cache`
- `annotation CallerInfo`
- `annotation Header`
- `annotation Payload`
- `annotation Query`
- `class ClientBasicAuthHandler`
- `class ClientBearerTokenAuthHandler`
- `class ClientSelfSignedJwtAuthHandler`
- `class Cookie`
- `class CookieStore`
- `class CsvPersistentCookieHandler`
- `class DefaultStatus`
- `class Headers`
- `class HttpCache`
- `class HttpFuture`
- `class Listener`
- `class ListenerFileUserStoreBasicAuthHandler`
- `class ListenerJwtAuthHandler`
- `class LoadBalancerRoundRobinRule`
- `class PushPromise`
- `class Request`
- `class RequestCacheControl`
- `class RequestContext`
- `class Response`
- `class ResponseCacheControl`
- `class StatusAccepted`
- `class StatusAlreadyReported`
- `class StatusBadGateway`
- `class StatusBadRequest`
- `class StatusConflict`
- `class StatusContinue`
- `class StatusCreated`
- `class StatusEarlyHints`
- `class StatusExpectationFailed`
- `class StatusFailedDependency`
- `class StatusForbidden`
- `class StatusFound`
- `class StatusGatewayTimeout`
- `class StatusGone`
- `class StatusHttpVersionNotSupported`
- `class StatusIMUsed`
- `class StatusInsufficientStorage`
- `class StatusInternalServerError`
- `class StatusLengthRequired`
- `class StatusLocked`
- `class StatusLoopDetected`
- `class StatusMethodNotAllowed`
- `class StatusMisdirectedRequest`
- `class StatusMovedPermanently`
- `class StatusMultiStatus`
- `class StatusMultipleChoices`
- `class StatusNetworkAuthenticationRequired`
- `class StatusNoContent`
- `class StatusNonAuthoritativeInformation`
- `class StatusNotAcceptable`
- `class StatusNotExtended`
- `class StatusNotFound`
- `class StatusNotImplemented`
- `class StatusNotModified`
- `class StatusOK`
- `class StatusPartialContent`
- `class StatusPayloadTooLarge`
- `class StatusPaymentRequired`
- `class StatusPermanentRedirect`
- `class StatusPreconditionFailed`
- `class StatusPreconditionRequired`
- `class StatusProcessing`
- `class StatusProxyAuthenticationRequired`
- `class StatusRangeNotSatisfiable`
- `class StatusRequestHeaderFieldsTooLarge`
- `class StatusRequestTimeout`
- `class StatusResetContent`
- `class StatusSeeOther`
- `class StatusServiceUnavailable`
- `class StatusSwitchingProtocols`
- `class StatusTemporaryRedirect`
- `class StatusTooEarly`
- `class StatusTooManyRequests`
- `class StatusUnauthorized`
- `class StatusUnavailableDueToLegalReasons`
- `class StatusUnprocessableEntity`
- `class StatusUnsupportedMediaType`
- `class StatusUpgradeRequired`
- `class StatusUriTooLong`
- `class StatusUseProxy`
- `class StatusVariantAlsoNegotiates`
- `client class ClientObject`
- `client class StatusCodeClientObject`
- `function 'start`
- `function addCookie`
- `function addCookies`
- `function addHeader`
- `function attach`
- `function authenticate`
- `function authorize`
- `function buildCacheControlDirectives`
- `function createInterceptors`
- `function delete`
- `function detach`
- `function enrich`
- `function execute`
- `function expects100Continue`
- `function forward`
- `function get`
- `function getAllCookies`
- `function getBinaryPayload`
- `function getBodyParts`
- `function getByteStream`
- `function getConfig`
- `function getContentType`
- `function getCookies`
- `function getCookiesByDomain`
- `function getCookiesByName`
- `function getEntity`
- `function getFormParams`
- `function getHeader`
- `function getHeaderNames`
- `function getHeaders`
- `function getJsonPayload`
- `function getMatrixParams`
- `function getNextClient`
- `function getNextPromise`
- `function getPort`
- `function getPromisedResponse`
- `function getQueryParamValue`
- `function getQueryParamValues`
- `function getQueryParams`
- `function getResponse`
- `function getSseEventStream`
- `function getStatusCodeRecord`
- `function getTextPayload`
- `function getWithType`
- `function getXmlPayload`
- `function gracefulStop`
- `function hasHeader`
- `function hasKey`
- `function hasPromise`
- `function head`
- `function immediateStop`
- `function isPersistent`
- `function isValid`
- `function keys`
- `function next`
- `function options`
- `function patch`
- `function populateFields`
- `function post`
- `function put`
- `function rejectPromise`
- `function remove`
- `function removeAllCookies`
- `function removeAllHeaders`
- `function removeCookie`
- `function removeCookiesByDomain`
- `function removeCookiesFromRemoteStore`
- `function removeExpiredCookies`
- `function removeHeader`
- `function set`
- `function setAnydataAsJsonPayload`
- `function setBinaryPayload`
- `function setBodyParts`
- `function setByteStream`
- `function setContentType`
- `function setETag`
- `function setEntity`
- `function setFileAsPayload`
- `function setHeader`
- `function setJsonPayload`
- `function setLastModified`
- `function setPayload`
- `function setSseEventStream`
- `function setTextPayload`
- `function setXmlPayload`
- `function storeCookie`
- `function submit`
- `function toStringValue`
- `type AllLoadBalanceEndpointsFailedError`
- `type AllRetryAttemptsFailed`
- `type ApplicationResponseError`
- `type BadMatrixParamError`
- `type CircuitBreakerConfigError`
- `type ClientAuthError`
- `type ClientConnectorError`
- `type ClientError`
- `type ClientRequestError`
- `type CookieHandlingError`
- `type Error`
- `type FailoverActionFailedError`
- `type FailoverAllEndpointsFailedError`
- `type GenericClientError`
- `type GenericListenerError`
- `type HeaderBindingError`
- `type HeaderNotFoundError`
- `type HeaderValidationError`
- `type Http2ClientError`
- `type IdleTimeoutError`
- `type InboundRequestError`
- `type InboundResponseError`
- `type InitializingInboundRequestError`
- `type InitializingInboundResponseError`
- `type InitializingOutboundRequestError`
- `type InitializingOutboundResponseError`
- `type Initiating100ContinueResponseError`
- `type InterceptorReturnError`
- `type InvalidCookieError`
- `type ListenerAuthError`
- `type ListenerAuthnError`
- `type ListenerAuthzError`
- `type ListenerError`
- `type LoadBalanceActionError`
- `type MaximumWaitTimeExceededError`
- `type MediaTypeBindingError`
- `type MediaTypeValidationError`
- `type NoContentError`
- `type OutboundRequestError`
- `type OutboundResponseError`
- `type PathParameterBindingError`
- `type PayloadBindingError`
- `type PayloadValidationError`
- `type QueryParameterBindingError`
- `type QueryParameterValidationError`
- `type ReadingInboundRequestBodyError`
- `type ReadingInboundRequestHeadersError`
- `type ReadingInboundResponseBodyError`
- `type ReadingInboundResponseHeadersError`
- `type RemoteServerError`
- `type ReqCtxMemberType`
- `type RequestDispatchingError`
- `type RequestNotAcceptableError`
- `type ResiliencyError`
- `type ResourceDispatchingError`
- `type ResourceDispatchingServerError`
- `type ResourceMethodNotAllowedError`
- `type ResourceNotFoundError`
- `type ResourcePathValidationError`
- `type ServiceDispatchingError`
- `type ServiceNotFoundError`
- `type SslError`
- `type StatusCodeBindingClientRequestError`
- `type StatusCodeBindingRemoteServerError`
- `type StatusCodeResponseBindingError`
- `type TargetType`
- `type UnsupportedActionError`
- `type UnsupportedRequestMediaTypeError`
- `type UpstreamServiceUnavailableError`
- `type Writing100ContinueResponseError`
- `type WritingOutboundRequestBodyError`
- `type WritingOutboundRequestHeadersError`
- `type WritingOutboundResponseBodyError`
- `type WritingOutboundResponseHeadersError`

### Declarations removed (2)

- `class ClientObject`
- `class StatusCodeClientObject`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 705–711 | 705–711 | Types | +1 | −1 |
| 2 | 769–782 | 769–830 | Types | +53 | −5 |
| 3 | 826–837 | 874–909 | Types | +28 | −4 |
| 4 | 896–901 | 968–989 | Types | +16 | −0 |
| 5 | 921–927 | 1009–1015 | Types | +1 | −1 |
| 6 | 1025–1039 | 1113–1309 | Types | +186 | −4 |
| 7 | 1063–1069 | 1333–1342 | Types | +4 | −1 |
| 8 | 1076–1082 | 1349–1358 | Types | +4 | −1 |
| 9 | 1089–1095 | 1365–1374 | Types | +4 | −1 |
| 10 | 1102–1108 | 1381–1390 | Types | +4 | −1 |
| 11 | 1115–1121 | 1397–1406 | Types | +4 | −1 |
| 12 | 1128–1134 | 1413–1422 | Types | +4 | −1 |
| 13 | 1141–1147 | 1429–1438 | Types | +4 | −1 |
| 14 | 1154–1160 | 1445–1454 | Types | +4 | −1 |
| 15 | 1166–1172 | 1460–1469 | Types | +4 | −1 |
| 16 | 1179–1185 | 1476–1485 | Types | +4 | −1 |
| 17 | 1192–1198 | 1492–1501 | Types | +4 | −1 |
| 18 | 1205–1211 | 1508–1517 | Types | +4 | −1 |
| 19 | 1218–1224 | 1524–1533 | Types | +4 | −1 |
| 20 | 1231–1237 | 1540–1549 | Types | +4 | −1 |
| 21 | 1244–1250 | 1556–1565 | Types | +4 | −1 |
| 22 | 1257–1263 | 1572–1581 | Types | +4 | −1 |
| 23 | 1270–1276 | 1588–1597 | Types | +4 | −1 |
| 24 | 1283–1289 | 1604–1613 | Types | +4 | −1 |
| 25 | 1296–1302 | 1620–1629 | Types | +4 | −1 |
| 26 | 1309–1315 | 1636–1645 | Types | +4 | −1 |
| 27 | 1322–1328 | 1652–1661 | Types | +4 | −1 |
| 28 | 1335–1341 | 1668–1677 | Types | +4 | −1 |
| 29 | 1348–1354 | 1684–1693 | Types | +4 | −1 |
| 30 | 1361–1367 | 1700–1709 | Types | +4 | −1 |
| 31 | 1374–1380 | 1716–1725 | Types | +4 | −1 |
| 32 | 1387–1393 | 1732–1741 | Types | +4 | −1 |
| 33 | 1400–1406 | 1748–1757 | Types | +4 | −1 |
| 34 | 1413–1419 | 1764–1773 | Types | +4 | −1 |
| 35 | 1426–1432 | 1780–1789 | Types | +4 | −1 |
| 36 | 1439–1445 | 1796–1805 | Types | +4 | −1 |
| 37 | 1452–1458 | 1812–1821 | Types | +4 | −1 |
| 38 | 1465–1471 | 1828–1837 | Types | +4 | −1 |
| 39 | 1478–1484 | 1844–1853 | Types | +4 | −1 |
| 40 | 1491–1497 | 1860–1869 | Types | +4 | −1 |
| 41 | 1504–1510 | 1876–1885 | Types | +4 | −1 |
| 42 | 1517–1523 | 1892–1901 | Types | +4 | −1 |
| 43 | 1530–1536 | 1908–1917 | Types | +4 | −1 |
| 44 | 1543–1549 | 1924–1933 | Types | +4 | −1 |
| 45 | 1556–1562 | 1940–1949 | Types | +4 | −1 |
| 46 | 1569–1575 | 1956–1965 | Types | +4 | −1 |
| 47 | 1582–1588 | 1972–1981 | Types | +4 | −1 |
| 48 | 1595–1601 | 1988–1997 | Types | +4 | −1 |
| 49 | 1608–1614 | 2004–2013 | Types | +4 | −1 |
| 50 | 1621–1627 | 2020–2029 | Types | +4 | −1 |
| 51 | 1634–1640 | 2036–2045 | Types | +4 | −1 |
| 52 | 1647–1653 | 2052–2061 | Types | +4 | −1 |
| 53 | 1660–1666 | 2068–2077 | Types | +4 | −1 |
| 54 | 1673–1679 | 2084–2093 | Types | +4 | −1 |
| 55 | 1686–1692 | 2100–2109 | Types | +4 | −1 |
| 56 | 1699–1705 | 2116–2125 | Types | +4 | −1 |
| 57 | 1712–1718 | 2132–2141 | Types | +4 | −1 |
| 58 | 1725–1731 | 2148–2157 | Types | +4 | −1 |
| 59 | 1738–1744 | 2164–2173 | Types | +4 | −1 |
| 60 | 1751–1757 | 2180–2189 | Types | +4 | −1 |
| 61 | 1764–1770 | 2196–2205 | Types | +4 | −1 |
| 62 | 1777–1783 | 2212–2221 | Types | +4 | −1 |
| 63 | 1790–1796 | 2228–2237 | Types | +4 | −1 |
| 64 | 1803–1809 | 2244–2253 | Types | +4 | −1 |
| 65 | 1816–1822 | 2260–2269 | Types | +4 | −1 |
| 66 | 1829–1835 | 2276–2285 | Types | +4 | −1 |
| 67 | 1842–1848 | 2292–2301 | Types | +4 | −1 |
| 68 | 1855–1866 | 2308–2322 | Types | +6 | −3 |
| 69 | 1932–1940 | 2388–2396 | Types | +2 | −2 |
| 70 | 2237–2243 | 2693–2789 | Types | +91 | −1 |
| 71 | 2247–2253 | 2793–2799 | Types | +1 | −1 |
| 72 | 2304–2453 | 2850–3070 | Types | +143 | −72 |
| 73 | 2467–2479 | 3084–3100 | Types | +6 | −2 |
| 74 | 2534–2545 | 3155–3167 | Types | +4 | −3 |
| 75 | 2631–2641 | 3253–3263 | Types | +3 | −3 |
| 76 | 2707–2713 | 3329–3425 | Types | +91 | −1 |
| 77 | 2740–2753 | 3452–3639 | Types | +178 | −4 |
| 78 | 2763–2769 | 3649–3658 | Types | +4 | −1 |
| 79 | 2782–2788 | 3671–3677 | Types | +1 | −1 |
| 80 | 2886–2891 | 3775–3784 | Types | +4 | −0 |
| 81 | 2919–2942 | 3812–4040 | Types | +214 | −9 |
| 82 | 2949–2959 | 4047–4057 | Client | +2 | −2 |
| 83 | 2981–2991 | 4079–4089 | Client | +2 | −2 |
| 84 | 2993–2999 | 4091–4097 | Client | +1 | −1 |
| 85 | 3001–3007 | 4099–4105 | Client | +1 | −1 |
| 86 | 3009–3015 | 4107–4113 | Client | +1 | −1 |
| 87 | 3017–3023 | 4115–4121 | Client | +1 | −1 |
| 88 | 3025–3031 | 4123–4129 | Client | +1 | −1 |
| 89 | 3033–3039 | 4131–4137 | Client | +1 | −1 |
| 90 | 3073–3091 | 4171–4189 | Client | +4 | −4 |
| 91 | 3119–3136 | 4217–4234 | Client | +3 | −3 |
| 92 | 3138–3144 | 4236–4242 | Client | +1 | −1 |
| 93 | 3146–3152 | 4244–4250 | Client | +1 | −1 |
| 94 | 3154–3160 | 4252–4258 | Client | +1 | −1 |
| 95 | 3162–3168 | 4260–4266 | Client | +1 | −1 |
| 96 | 3170–3176 | 4268–4274 | Client | +1 | −1 |
| 97 | 3178–3184 | 4276–4282 | Client | +1 | −1 |
| 98 | 3220–3248 | 4318–4346 | Client | +6 | −6 |
| 99 | 3250–3256 | 4348–4354 | Client | +1 | −1 |
| 100 | 3258–3264 | 4356–4362 | Client | +1 | −1 |
| 101 | 3266–3272 | 4364–4370 | Client | +1 | −1 |
| 102 | 3274–3280 | 4372–4378 | Client | +1 | −1 |
| 103 | 3282–3288 | 4380–4386 | Client | +1 | −1 |
| 104 | 3290–3296 | 4388–4394 | Client | +1 | −1 |
| 105 | 3333–3349 | 4431–4447 | Client | +3 | −3 |
| 106 | 3351–3357 | 4449–4455 | Client | +1 | −1 |
| 107 | 3359–3365 | 4457–4463 | Client | +1 | −1 |
| 108 | 3367–3373 | 4465–4471 | Client | +1 | −1 |
| 109 | 3375–3381 | 4473–4479 | Client | +1 | −1 |
| 110 | 3383–3389 | 4481–4487 | Client | +1 | −1 |
| 111 | 3391–3397 | 4489–4495 | Client | +1 | −1 |
| 112 | 3518–3532 | 4616–4669 | Functions | +47 | −8 |

---

## Unified diff

`````diff
--- http/old/ballerina_http.bal.txt	2026-08-12 12:57:29
+++ http/new/ballerina_http.bal.txt	2026-08-12 13:19:19
@@ -705,7 +705,7 @@
 };
 
 # Represents OAuth2 grant configurations for OAuth2 authentication.
-type OAuth2GrantConfig ballerina/http:2.16.6:OAuth2ClientCredentialsGrantConfig|ballerina/http:2.16.6:OAuth2PasswordGrantConfig|ballerina/http:2.16.6:OAuth2RefreshTokenGrantConfig|ballerina/http:2.16.6:OAuth2JwtBearerGrantConfig;
+type OAuth2GrantConfig OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
 # Represents file user store configurations for Basic Auth authentication.
 
@@ -769,14 +769,62 @@
 };
 
 # Defines the authentication configurations for the HTTP client.
-type ClientAuthConfig ballerina/http:2.16.6:CredentialsConfig|ballerina/http:2.16.6:BearerTokenConfig|ballerina/http:2.16.6:JwtIssuerConfig|ballerina/http:2.16.6:OAuth2ClientCredentialsGrantConfig|ballerina/http:2.16.6:OAuth2PasswordGrantConfig|ballerina/http:2.16.6:OAuth2RefreshTokenGrantConfig|ballerina/http:2.16.6:OAuth2JwtBearerGrantConfig;
+type ClientAuthConfig CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig;
 
-// Unknown type: ClientBasicAuthHandler
-
-// Unknown type: ClientBearerTokenAuthHandler
+# Initializes the `http:ClientBasicAuthHandler` object.
+# 
+class ClientBasicAuthHandler {
+    function init(CredentialsConfig config) returns ();
 
-// Unknown type: ClientSelfSignedJwtAuthHandler
+    # Enrich the request with the relevant authentication requirements.
+    # 
+    function enrich(Request req) returns Request|ClientAuthError;
+
+    # Enrich the headers map with the relevant authentication requirements.
+    # 
+    function enrichHeaders(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
 
+    # Returns the headers map with the relevant authentication requirements.
+    # 
+    function getSecurityHeaders() returns map<string|string[]>|ClientAuthError;
+}
+
+# Initializes the `http:ClientBearerTokenAuthHandler` object.
+# 
+class ClientBearerTokenAuthHandler {
+    function init(BearerTokenConfig config) returns ();
+
+    # Enrich the request with the relevant authentication requirements.
+    # 
+    function enrich(Request req) returns Request|ClientAuthError;
+
+    # Enrich the headers map with the relevant authentication requirements.
+    # 
+    function enrichHeaders(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+
+    # Returns the headers map with the relevant authentication requirements.
+    # 
+    function getSecurityHeaders() returns map<string|string[]>|ClientAuthError;
+}
+
+# Initializes the `http:ClientSelfSignedJwtAuthProvider` object.
+# 
+class ClientSelfSignedJwtAuthHandler {
+    function init(JwtIssuerConfig config) returns ();
+
+    # Enrich the request with the relevant authentication requirements.
+    # 
+    function enrich(Request req) returns Request|ClientAuthError;
+
+    # Enrich the headers map with the relevant authentication requirements.
+    # 
+    function enrichHeaders(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+
+    # Returns the headers map with the relevant authentication requirements.
+    # 
+    function getSecurityHeaders() returns map<string|string[]>|ClientAuthError;
+}
+
 # Represents the auth annotation for file user store configurations with scopes.
 # 
 
@@ -826,12 +874,36 @@
 };
 
 # Defines the authentication configurations for the HTTP listener.
-type ListenerAuthConfig ballerina/http:2.16.6:FileUserStoreConfigWithScopes|ballerina/http:2.16.6:LdapUserStoreConfigWithScopes|ballerina/http:2.16.6:JwtValidatorConfigWithScopes|ballerina/http:2.16.6:OAuth2IntrospectionConfigWithScopes;
-
-// Unknown type: ListenerFileUserStoreBasicAuthHandler
+type ListenerAuthConfig FileUserStoreConfigWithScopes|LdapUserStoreConfigWithScopes|JwtValidatorConfigWithScopes|OAuth2IntrospectionConfigWithScopes;
 
-// Unknown type: ListenerJwtAuthHandler
+# Initializes the `http:ListenerFileUserStoreBasicAuthHandler` object.
+# 
+class ListenerFileUserStoreBasicAuthHandler {
+    function init(FileUserStoreConfig config = {}) returns ();
 
+    # Authenticates with the relevant authentication requirements.
+    # 
+    function authenticate(Request|Headers|string data) returns auth:UserDetails|Unauthorized; // Special Agent Note: UserDetails FROM ballerina/auth package
+
+    # Authorizes with the relevant authorization requirements.
+    # 
+    function authorize(auth:UserDetails userDetails, string|string[] expectedScopes) returns Forbidden|(); // Special Agent Note: UserDetails FROM ballerina/auth package
+}
+
+# Initializes the `http:ListenerJwtAuthHandler` object.
+# 
+class ListenerJwtAuthHandler {
+    function init(JwtValidatorConfig config) returns ();
+
+    # Authenticates with the relevant authentication requirements.
+    # 
+    function authenticate(Request|Headers|string data) returns jwt:Payload|Unauthorized; // Special Agent Note: Payload FROM ballerina/jwt package
+
+    # Authorizes with the relevant authorization requirements.
+    # 
+    function authorize(jwt:Payload jwtPayload, string|string[] expectedScopes) returns Forbidden|(); // Special Agent Note: Payload FROM ballerina/jwt package
+}
+
 # Represents a Server Sent Event emitted from a service.
 
 type SseEvent record {
@@ -896,6 +968,22 @@
 
 # The representation of a persistent cookie handler object type for managing persistent cookies.
 class PersistentCookieHandler {
+
+    # Adds a persistent cookie to the cookie store.
+    # 
+    function storeCookie(Cookie cookie) returns CookieHandlingError|();
+
+    # Gets all persistent cookies.
+    # 
+    function getAllCookies() returns Cookie[]|CookieHandlingError;
+
+    # Removes a specific persistent cookie.
+    # 
+    function removeCookie(string name, string domain, string path) returns CookieHandlingError|();
+
+    # Removes all persistent cookies.
+    # 
+    function removeAllCookies() returns CookieHandlingError|();
 }
 
 # Contains the configurations for an HTTP service.
@@ -921,7 +1009,7 @@
     # Enables the inbound payload validation functionality which provided by the constraint package. Enabled by default
     boolean validation?;
     # The service object type which defines the service contract. This is auto-generated at compile-time
-    typedesc<ballerina/http:2.16.6:ServiceContract> serviceType?;
+    typedesc<ServiceContract> serviceType?;
     # Base path to be used with the service implementation. This is only allowed on service contract types
     string basePath?;
     # Enables or disables relaxed data binding on the service side. Disabled by default. 
@@ -1025,15 +1113,197 @@
 
 type HttpCallerInfo record {
     # Specifies the type of response
-    typedesc<ballerina/http:2.16.6:ResponseMessage|ballerina/http:2.16.6:StatusCodeResponse|ballerina/http:2.16.6:Error> respondType?;
+    typedesc<ResponseMessage|StatusCodeResponse|Error> respondType?;
 };
 
-// Unknown type: Response
+class Response {
+    function init() returns ();
 
-// Unknown type: ResponseCacheControl
+    # Gets the `Entity` associated with the response.
+    # 
+    function getEntity() returns mime:Entity|ClientError; // Special Agent Note: Entity FROM ballerina/mime package
 
+    # Sets the provided `Entity` to the response.
+    # 
+    function setEntity(mime:Entity e) returns (); // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Checks whether the requested header key exists in the header map.
+    # 
+    function hasHeader(string headerName, HeaderPosition position = "leading") returns boolean;
+
+    # Returns the value of the specified header. If the specified header key maps to multiple values, the first of
+    # these values is returned.
+    # 
+    function getHeader(string headerName, HeaderPosition position = "leading") returns string|HeaderNotFoundError;
+
+    # Adds the specified header to the response. Existing header values are not replaced, except for the `Content-Type`
+    # header. In the case of the `Content-Type` header, the existing value is replaced with the specified value.
+    # . Panic if an illegal header is passed.
+    # 
+    function addHeader(string headerName, string headerValue, HeaderPosition position = "leading") returns ();
+
+    # Gets all the header values to which the specified header key maps to.
+    # 
+    function getHeaders(string headerName, HeaderPosition position = "leading") returns string[]|HeaderNotFoundError;
+
+    # Sets the specified header to the response. If a mapping already exists for the specified header key, the
+    # existing header value is replaced with the specified header value. Panic if an illegal header is passed.
+    # 
+    function setHeader(string headerName, string headerValue, HeaderPosition position = "leading") returns ();
+
+    # Removes the specified header from the response.
+    # 
+    function removeHeader(string headerName, HeaderPosition position = "leading") returns ();
+
+    # Removes all the headers from the response.
+    # 
+    function removeAllHeaders(HeaderPosition position = "leading") returns ();
+
+    # Gets all the names of the headers of the response.
+    # 
+    function getHeaderNames(HeaderPosition position = "leading") returns string[];
+
+    # Sets the `content-type` header to the response.
+    # 
+    function setContentType(string contentType) returns error?;
+
+    # Gets the type of the payload of the response (i.e., the `content-type` header value).
+    # 
+    function getContentType() returns string;
+
+    # Extract `json` payload from the response. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not JSON, an `http:ClientError` is returned.
+    # 
+    function getJsonPayload() returns json|ClientError;
+
+    # Extracts `xml` payload from the response. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not XML, an `http:ClientError` is returned.
+    # 
+    function getXmlPayload() returns xml|ClientError;
+
+    # Extracts `text` payload from the response. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not of type text, an `http:ClientError` is returned.
+    # 
+    function getTextPayload() returns string|ClientError;
+
+    # Gets the response payload as  a stream of byte[], except in the case of multiparts. To retrieve multiparts, use
+    # `Response.getBodyParts()`.
+    # 
+    function getByteStream(int arraySize = 0) returns stream<byte[], io:Error?>|ClientError;
+
+    # Gets the response payload as a `byte[]`.
+    # 
+    function getBinaryPayload() returns byte[]|ClientError;
+
+    # Gets the response payload as a `stream` of SseEvent.
+    # 
+    function getSseEventStream() returns stream<SseEvent, error?>|ClientError;
+
+    # Extracts body parts from the response. If the content type is not a composite media type, an error is returned.
+    # 
+    function getBodyParts() returns mime:Entity[]|ClientError; // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Sets the `etag` header for the given payload. The ETag is generated using a CRC32 hash isolated function.
+    # 
+    function setETag(json|xml|string|byte[] payload) returns ();
+
+    # Sets the current time as the `last-modified` header.
+    function setLastModified() returns ();
+
+    # Sets a `json` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/json`. Any existing content-type can be
+    # overridden by passing the content-type as an optional parameter.
+    # 
+    function setJsonPayload(json payload, string|() contentType = ()) returns ();
+
+    # Sets a `anydata` payaload, as a `json` payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/json`. Any existing content-type can be
+    # overridden by passing the content-type as an optional parameter.
+    # 
+    function setAnydataAsJsonPayload(anydata payload, string|() contentType = ()) returns ();
+
+    # Sets an `xml` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/xml`. Any existing content-type can be
+    # overridden by passing the content-type as an optional parameter.
+    # 
+    function setXmlPayload(xml payload, string|() contentType = ()) returns ();
+
+    # Sets a `string` as the payload. If the content-type header is not set then this method set
+    # content-type headers with the default content-type, which is `text/plain`. Any
+    # existing content-type can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setTextPayload(string payload, string|() contentType = ()) returns ();
+
+    # Sets a `byte[]` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/octet-stream`. Any existing content-type
+    # can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setBinaryPayload(byte[] payload, string|() contentType = ()) returns ();
+
+    # Set multiparts as the payload. If the content-type header is not set then this method
+    # set content-type headers with the default content-type, which is `multipart/form-data`.
+    # Any existing content-type can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setBodyParts(mime:Entity[] bodyParts, string|() contentType = ()) returns (); // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Sets the content of the specified file as the entity body of the response. If the content-type header
+    # is not set then this method set content-type headers with the default content-type, which is
+    # `application/octet-stream`. Any existing content-type can be overridden by passing the content-type
+    # as an optional parameter.
+    # 
+    function setFileAsPayload(string filePath, string|() contentType = ()) returns ();
+
+    # Sets a `Stream` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/octet-stream`. Any existing content-type can
+    # be overridden by passing the content-type as an optional parameter.
+    # 
+    function setByteStream(stream<byte[], io:Error?> byteStream, string|() contentType = ()) returns ();
+
+    # Sets an `http:SseEvent` stream as the payload, along with the Content-Type and Cache-Control 
+    # headers set to 'text/event-stream' and 'no-cache', respectively.
+    # 
+    function setSseEventStream(stream<http:SseEvent, error?>|stream<http:SseEvent, error> eventStream) returns ();
+
+    # Sets the response payload. This method overrides any existing content-type by passing the content-type
+    # as an optional parameter. If the content type parameter is not provided then the default value derived
+    # from the payload will be used as content-type only when there are no existing content-type header. If
+    # the payload is non-json typed value then the value is converted to json using the `toJson` method.
+    # 
+    function setPayload(anydata|mime:Entity[]|stream<byte[], io:Error?>|stream<http:SseEvent, error?> payload, string|() contentType = ()) returns ();
+
+    # Adds the cookie to response.
+    # 
+    function addCookie(Cookie cookie) returns ();
+
+    # Deletes the cookies in the client's cookie store.
+    # 
+    function removeCookiesFromRemoteStore(Cookie[] cookiesToRemove) returns ();
+
+    # Gets cookies from the response.
+    # 
+    function getCookies() returns Cookie[];
+
+    # Gets the status code response record from the response.
+    # 
+    function getStatusCodeRecord() returns StatusCodeRecord|error;
+}
+
+# Configures cache control directives for an `http:Response`.
+# 
+class ResponseCacheControl {
+
+    function populateFields(HttpCacheConfig cacheConfig) returns ();
+
+    # Builds the cache control directives string from the current `http:ResponseCacheControl` configurations.
+    # 
+    function buildCacheControlDirectives() returns string;
+}
+
 # The types of messages that are accepted by HTTP `listener` when sending out the outbound response.
-type ResponseMessage anydata|ballerina/http:2.16.6:Response|ballerina/mime:2.12.2:Entity[]|stream<byte[], ballerina/io:1.8.1:Error?>|stream<ballerina/http:2.16.6:SseEvent, error?>|stream<ballerina/http:2.16.6:SseEvent, error>;
+type ResponseMessage anydata|Response|mime:Entity[]|stream<byte[], io:Error?>|stream<SseEvent, error?>|stream<SseEvent, error>;
 
 # The common attributed of response status code record type.
 # 
@@ -1063,7 +1333,10 @@
 class Status {
 }
 
-// Unknown type: StatusContinue
+# Represents the status code of `STATUS_CONTINUE`.
+# 
+class StatusContinue {
+}
 
 # The status code response record of `SwitchingProtocols`.
 # 
@@ -1076,7 +1349,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusSwitchingProtocols
+# Represents the status code of `STATUS_SWITCHING_PROTOCOLS`.
+# 
+class StatusSwitchingProtocols {
+}
 
 # The status code response record of `Processing`.
 # 
@@ -1089,7 +1365,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusProcessing
+# Represents the status code of `STATUS_PROCESSING`.
+# 
+class StatusProcessing {
+}
 
 # The status code response record of `EarlyHints`.
 # 
@@ -1102,7 +1381,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusEarlyHints
+# Represents the status code of `STATUS_EARLY_HINTS`.
+# 
+class StatusEarlyHints {
+}
 
 # The status code response record of `Ok`.
 # 
@@ -1115,7 +1397,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusOK
+# Represents the status code of `STATUS_OK`.
+# 
+class StatusOK {
+}
 
 # The status code response record of `Created`.
 # 
@@ -1128,7 +1413,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusCreated
+# Represents the status code of `STATUS_CREATED`.
+# 
+class StatusCreated {
+}
 
 # The status code response record of `Accepted`.
 # 
@@ -1141,7 +1429,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusAccepted
+# Represents the status code of `STATUS_ACCEPTED`.
+# 
+class StatusAccepted {
+}
 
 # The status code response record of `NonAuthoritativeInformation`.
 # 
@@ -1154,7 +1445,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNonAuthoritativeInformation
+# Represents the status code of `STATUS_NON_AUTHORITATIVE_INFORMATION`.
+# 
+class StatusNonAuthoritativeInformation {
+}
 
 # The status code response record of `NoContent`.
 # 
@@ -1166,7 +1460,10 @@
     StatusNoContent status?;
 };
 
-// Unknown type: StatusNoContent
+# Represents the status code of `STATUS_NO_CONTENT`.
+# 
+class StatusNoContent {
+}
 
 # The status code response record of `ResetContent`.
 # 
@@ -1179,7 +1476,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusResetContent
+# Represents the status code of `STATUS_RESET_CONTENT`.
+# 
+class StatusResetContent {
+}
 
 # The status code response record of `PartialContent`.
 # 
@@ -1192,7 +1492,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPartialContent
+# Represents the status code of `STATUS_PARTIAL_CONTENT`.
+# 
+class StatusPartialContent {
+}
 
 # The status code response record of `MultiStatus`.
 # 
@@ -1205,7 +1508,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusMultiStatus
+# Represents the status code of `STATUS_MULTI_STATUS`.
+# 
+class StatusMultiStatus {
+}
 
 # The status code response record of `AlreadyReported`.
 # 
@@ -1218,7 +1524,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusAlreadyReported
+# Represents the status code of `STATUS_ALREADY_REPORTED`.
+# 
+class StatusAlreadyReported {
+}
 
 # The status code response record of `IMUsed`.
 # 
@@ -1231,7 +1540,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusIMUsed
+# Represents the status code of `STATUS_IM_USED`.
+# 
+class StatusIMUsed {
+}
 
 # The status code response record of `MultipleChoices`.
 # 
@@ -1244,7 +1556,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusMultipleChoices
+# Represents the status code of `STATUS_MULTIPLE_CHOICES`.
+# 
+class StatusMultipleChoices {
+}
 
 # The status code response record of `MovedPermanently`.
 # 
@@ -1257,7 +1572,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusMovedPermanently
+# Represents the status code of `STATUS_MOVED_PERMANENTLY`.
+# 
+class StatusMovedPermanently {
+}
 
 # The status code response record of `Found`.
 # 
@@ -1270,7 +1588,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusFound
+# Represents the status code of `STATUS_FOUND`.
+# 
+class StatusFound {
+}
 
 # The status code response record of `SeeOther`.
 # 
@@ -1283,7 +1604,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusSeeOther
+# Represents the status code of `STATUS_SEE_OTHER`.
+# 
+class StatusSeeOther {
+}
 
 # The status code response record of `NotModified`.
 # 
@@ -1296,7 +1620,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNotModified
+# Represents the status code of `STATUS_NOT_MODIFIED`.
+# 
+class StatusNotModified {
+}
 
 # The status code response record of `UseProxy`.
 # 
@@ -1309,7 +1636,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUseProxy
+# Represents the status code of `STATUS_USE_PROXY`.
+# 
+class StatusUseProxy {
+}
 
 # The status code response record of `TemporaryRedirect`.
 # 
@@ -1322,7 +1652,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusTemporaryRedirect
+# Represents the status code of `STATUS_TEMPORARY_REDIRECT`.
+# 
+class StatusTemporaryRedirect {
+}
 
 # The status code response record of `PermanentRedirect`.
 # 
@@ -1335,7 +1668,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPermanentRedirect
+# Represents the status code of `STATUS_PERMANENT_REDIRECT`.
+# 
+class StatusPermanentRedirect {
+}
 
 # The status code response record of `BadRequest`.
 # 
@@ -1348,7 +1684,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusBadRequest
+# Represents the status code of `STATUS_BAD_REQUEST`.
+# 
+class StatusBadRequest {
+}
 
 # The status code response record of `Unauthorized`.
 # 
@@ -1361,7 +1700,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUnauthorized
+# Represents the status code of `STATUS_UNAUTHORIZED`.
+# 
+class StatusUnauthorized {
+}
 
 # The status code response record of `PaymentRequired`.
 # 
@@ -1374,7 +1716,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPaymentRequired
+# Represents the status code of `STATUS_PAYMENT_REQUIRED`.
+# 
+class StatusPaymentRequired {
+}
 
 # The status code response record of `Forbidden`.
 # 
@@ -1387,7 +1732,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusForbidden
+# Represents the status code of `STATUS_FORBIDDEN`.
+# 
+class StatusForbidden {
+}
 
 # The status code response record of `NotFound`.
 # 
@@ -1400,7 +1748,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNotFound
+# Represents the status code of `STATUS_NOT_FOUND`.
+# 
+class StatusNotFound {
+}
 
 # The status code response record of `MethodNotAllowed`.
 # 
@@ -1413,7 +1764,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusMethodNotAllowed
+# Represents the status code of `STATUS_METHOD_NOT_ALLOWED`.
+# 
+class StatusMethodNotAllowed {
+}
 
 # The status code response record of `NotAcceptable`.
 # 
@@ -1426,7 +1780,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNotAcceptable
+# Represents the status code of `STATUS_NOT_ACCEPTABLE`.
+# 
+class StatusNotAcceptable {
+}
 
 # The status code response record of `ProxyAuthenticationRequired`.
 # 
@@ -1439,7 +1796,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusProxyAuthenticationRequired
+# Represents the status code of `STATUS_PROXY_AUTHENTICATION_REQUIRED`.
+# 
+class StatusProxyAuthenticationRequired {
+}
 
 # The status code response record of `RequestTimeout`.
 # 
@@ -1452,7 +1812,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusRequestTimeout
+# Represents the status code of `STATUS_REQUEST_TIMEOUT`.
+# 
+class StatusRequestTimeout {
+}
 
 # The status code response record of `Conflict`.
 # 
@@ -1465,7 +1828,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusConflict
+# Represents the status code of `STATUS_CONFLICT`.
+# 
+class StatusConflict {
+}
 
 # The status code response record of `Gone`.
 # 
@@ -1478,7 +1844,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusGone
+# Represents the status code of `STATUS_GONE`.
+# 
+class StatusGone {
+}
 
 # The status code response record of `LengthRequired`.
 # 
@@ -1491,7 +1860,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusLengthRequired
+# Represents the status code of `STATUS_LENGTH_REQUIRED`.
+# 
+class StatusLengthRequired {
+}
 
 # The status code response record of `PreconditionFailed`.
 # 
@@ -1504,7 +1876,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPreconditionFailed
+# Represents the status code of `STATUS_PRECONDITION_FAILED`.
+# 
+class StatusPreconditionFailed {
+}
 
 # The status code response record of `PayloadTooLarge`.
 # 
@@ -1517,7 +1892,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPayloadTooLarge
+# Represents the status code of `STATUS_PAYLOAD_TOO_LARGE`.
+# 
+class StatusPayloadTooLarge {
+}
 
 # The status code response record of `UriTooLong`.
 # 
@@ -1530,7 +1908,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUriTooLong
+# Represents the status code of `STATUS_URI_TOO_LONG`.
+# 
+class StatusUriTooLong {
+}
 
 # The status code response record of `UnsupportedMediaType`.
 # 
@@ -1543,7 +1924,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUnsupportedMediaType
+# Represents the status code of `STATUS_UNSUPPORTED_MEDIA_TYPE`.
+# 
+class StatusUnsupportedMediaType {
+}
 
 # The status code response record of `RangeNotSatisfiable`.
 # 
@@ -1556,7 +1940,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusRangeNotSatisfiable
+# Represents the status code of `STATUS_RANGE_NOT_SATISFIABLE`.
+# 
+class StatusRangeNotSatisfiable {
+}
 
 # The status code response record of `ExpectationFailed`.
 # 
@@ -1569,7 +1956,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusExpectationFailed
+# Represents the status code of `STATUS_EXPECTATION_FAILED`.
+# 
+class StatusExpectationFailed {
+}
 
 # The status code response record of `MisdirectedRequest`.
 # 
@@ -1582,7 +1972,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusMisdirectedRequest
+# Represents the status code of `STATUS_MISDIRECTED_REQUEST`.
+# 
+class StatusMisdirectedRequest {
+}
 
 # The status code response record of `UnprocessableEntity`.
 # 
@@ -1595,7 +1988,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUnprocessableEntity
+# Represents the status code of `STATUS_UNPROCESSABLE_ENTITY`.
+# 
+class StatusUnprocessableEntity {
+}
 
 # The status code response record of `Locked`.
 # 
@@ -1608,7 +2004,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusLocked
+# Represents the status code of `STATUS_LOCKED`.
+# 
+class StatusLocked {
+}
 
 # The status code response record of `FailedDependency`.
 # 
@@ -1621,7 +2020,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusFailedDependency
+# Represents the status code of `STATUS_FAILED_DEPENDENCY`.
+# 
+class StatusFailedDependency {
+}
 
 # The status code response record of `TooEarly`.
 # 
@@ -1634,7 +2036,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusTooEarly
+# Represents the status code of `STATUS_TOO_EARLY`.
+# 
+class StatusTooEarly {
+}
 
 # The status code response record of `PreconditionRequired`.
 # 
@@ -1647,7 +2052,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusPreconditionRequired
+# Represents the status code of `STATUS_PRECONDITION_REQUIRED`.
+# 
+class StatusPreconditionRequired {
+}
 
 # The status code response record of `UnavailableDueToLegalReasons`.
 # 
@@ -1660,7 +2068,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUnavailableDueToLegalReasons
+# Represents the status code of `STATUS_UNAVAILABLE_DUE_TO_LEGAL_REASONS`.
+# 
+class StatusUnavailableDueToLegalReasons {
+}
 
 # The status code response record of `UpgradeRequired`.
 # 
@@ -1673,7 +2084,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusUpgradeRequired
+# Represents the status code of `STATUS_UPGRADE_REQUIRED`.
+# 
+class StatusUpgradeRequired {
+}
 
 # The status code response record of `TooManyRequests`.
 # 
@@ -1686,7 +2100,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusTooManyRequests
+# Represents the status code of `STATUS_TOO_MANY_REQUESTS`.
+# 
+class StatusTooManyRequests {
+}
 
 # The status code response record of `RequestHeaderFieldsTooLarge`.
 # 
@@ -1699,7 +2116,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusRequestHeaderFieldsTooLarge
+# Represents the status code of `STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE`.
+# 
+class StatusRequestHeaderFieldsTooLarge {
+}
 
 # The status code response record of `InternalServerError`.
 # 
@@ -1712,7 +2132,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusInternalServerError
+# Represents the status code of `STATUS_INTERNAL_SERVER_ERROR`.
+# 
+class StatusInternalServerError {
+}
 
 # The status code response record of `NotImplemented`.
 # 
@@ -1725,7 +2148,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNotImplemented
+# Represents the status code of `STATUS_NOT_IMPLEMENTED`.
+# 
+class StatusNotImplemented {
+}
 
 # The status code response record of `BadGateway`.
 # 
@@ -1738,7 +2164,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusBadGateway
+# Represents the status code of `STATUS_BAD_GATEWAY`.
+# 
+class StatusBadGateway {
+}
 
 # The status code response record of `ServiceUnavailable`.
 # 
@@ -1751,7 +2180,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusServiceUnavailable
+# Represents the status code of `STATUS_SERVICE_UNAVAILABLE`.
+# 
+class StatusServiceUnavailable {
+}
 
 # The status code response record of `GatewayTimeout`.
 # 
@@ -1764,7 +2196,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusGatewayTimeout
+# Represents the status code of `STATUS_GATEWAY_TIMEOUT`.
+# 
+class StatusGatewayTimeout {
+}
 
 # The status code response record of `HttpVersionNotSupported`.
 # 
@@ -1777,7 +2212,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusHttpVersionNotSupported
+# Represents the status code of `STATUS_HTTP_VERSION_NOT_SUPPORTED`.
+# 
+class StatusHttpVersionNotSupported {
+}
 
 # The status code response record of `VariantAlsoNegotiates`.
 # 
@@ -1790,7 +2228,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusVariantAlsoNegotiates
+# Represents the status code of `STATUS_VARIANT_ALSO_NEGOTIATES`.
+# 
+class StatusVariantAlsoNegotiates {
+}
 
 # The status code response record of `InsufficientStorage`.
 # 
@@ -1803,7 +2244,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusInsufficientStorage
+# Represents the status code of `STATUS_INSUFFICIENT_STORAGE`.
+# 
+class StatusInsufficientStorage {
+}
 
 # The status code response record of `LoopDetected`.
 # 
@@ -1816,7 +2260,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusLoopDetected
+# Represents the status code of `STATUS_LOOP_DETECTED`.
+# 
+class StatusLoopDetected {
+}
 
 # The status code response record of `NotExtended`.
 # 
@@ -1829,7 +2276,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNotExtended
+# Represents the status code of `STATUS_NOT_EXTENDED`.
+# 
+class StatusNotExtended {
+}
 
 # The status code response record of `NetworkAuthenticationRequired`.
 # 
@@ -1842,7 +2292,10 @@
     anydata body?;
 };
 
-// Unknown type: StatusNetworkAuthenticationRequired
+# Represents the status code of `STATUS_NETWORK_AUTHENTICATION_REQUIRED`.
+# 
+class StatusNetworkAuthenticationRequired {
+}
 
 # The default status code response record.
 # 
@@ -1855,12 +2308,15 @@
     anydata body?;
 };
 
-// Unknown type: DefaultStatus
+class DefaultStatus {
+    function init(int code) returns ();
+}
 
 # Defines the possible status code response record types.
-type StatusCodeResponse ballerina/http:2.16.6:Continue|ballerina/http:2.16.6:SwitchingProtocols|ballerina/http:2.16.6:Processing|ballerina/http:2.16.6:EarlyHints|ballerina/http:2.16.6:Ok|ballerina/http:2.16.6:Created|ballerina/http:2.16.6:Accepted|ballerina/http:2.16.6:NonAuthoritativeInformation|ballerina/http:2.16.6:NoContent|ballerina/http:2.16.6:ResetContent|ballerina/http:2.16.6:PartialContent|ballerina/http:2.16.6:MultiStatus|ballerina/http:2.16.6:AlreadyReported|ballerina/http:2.16.6:IMUsed|ballerina/http:2.16.6:MultipleChoices|ballerina/http:2.16.6:MovedPermanently|ballerina/http:2.16.6:Found|ballerina/http:2.16.6:SeeOther|ballerina/http:2.16.6:NotModified|ballerina/http:2.16.6:UseProxy|ballerina/http:2.16.6:TemporaryRedirect|ballerina/http:2.16.6:PermanentRedirect|ballerina/http:2.16.6:BadRequest|ballerina/http:2.16.6:Unauthorized|ballerina/http:2.16.6:PaymentRequired|ballerina/http:2.16.6:Forbidden|ballerina/http:2.16.6:NotFound|ballerina/http:2.16.6:MethodNotAllowed|ballerina/http:2.16.6:NotAcceptable|ballerina/http:2.16.6:ProxyAuthenticationRequired|ballerina/http:2.16.6:RequestTimeout|ballerina/http:2.16.6:Conflict|ballerina/http:2.16.6:Gone|ballerina/http:2.16.6:LengthRequired|ballerina/http:2.16.6:PreconditionFailed|ballerina/http:2.16.6:PayloadTooLarge|ballerina/http:2.16.6:UriTooLong|ballerina/http:2.16.6:UnsupportedMediaType|ballerina/http:2.16.6:RangeNotSatisfiable|ballerina/http:2.16.6:ExpectationFailed|ballerina/http:2.16.6:MisdirectedRequest|ballerina/http:2.16.6:UnprocessableEntity|ballerina/http:2.16.6:Locked|ballerina/http:2.16.6:FailedDependency|ballerina/http:2.16.6:TooEarly|ballerina/http:2.16.6:PreconditionRequired|ballerina/http:2.16.6:UnavailableDueToLegalReasons|ballerina/http:2.16.6:UpgradeRequired|ballerina/http:2.16.6:TooManyRequests|ballerina/http:2.16.6:RequestHeaderFieldsTooLarge|ballerina/http:2.16.6:InternalServerError|ballerina/http:2.16.6:NotImplemented|ballerina/http:2.16.6:BadGateway|ballerina/http:2.16.6:ServiceUnavailable|ballerina/http:2.16.6:GatewayTimeout|ballerina/http:2.16.6:HttpVersionNotSupported|ballerina/http:2.16.6:VariantAlsoNegotiates|ballerina/http:2.16.6:InsufficientStorage|ballerina/http:2.16.6:LoopDetected|ballerina/http:2.16.6:NotExtended|ballerina/http:2.16.6:NetworkAuthenticationRequired|ballerina/http:2.16.6:DefaultStatusCodeResponse;
+type StatusCodeResponse Continue|SwitchingProtocols|Processing|EarlyHints|Ok|Created|Accepted|NonAuthoritativeInformation|NoContent|ResetContent|PartialContent|MultiStatus|AlreadyReported|IMUsed|MultipleChoices|MovedPermanently|Found|SeeOther|NotModified|UseProxy|TemporaryRedirect|PermanentRedirect|BadRequest|Unauthorized|PaymentRequired|Forbidden|NotFound|MethodNotAllowed|NotAcceptable|ProxyAuthenticationRequired|RequestTimeout|Conflict|Gone|LengthRequired|PreconditionFailed|PayloadTooLarge|UriTooLong|UnsupportedMediaType|RangeNotSatisfiable|ExpectationFailed|MisdirectedRequest|UnprocessableEntity|Locked|FailedDependency|TooEarly|PreconditionRequired|UnavailableDueToLegalReasons|UpgradeRequired|TooManyRequests|RequestHeaderFieldsTooLarge|InternalServerError|NotImplemented|BadGateway|ServiceUnavailable|GatewayTimeout|HttpVersionNotSupported|VariantAlsoNegotiates|InsufficientStorage|LoopDetected|NotExtended|NetworkAuthenticationRequired|DefaultStatusCodeResponse;
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Defines the Header resource signature parameter.
 # 
@@ -1932,9 +2388,9 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and private key of the client
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # SSL/TLS protocol related options
-    record {|ballerina/http:2.16.6:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # Certificate validation against OCSP_CRL, OCSP_STAPLING related options
-    record {|ballerina/http:2.16.6:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     # List of ciphers to be used
 eg: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     string[] ciphers?;
@@ -2237,7 +2693,97 @@
 }
 
 # The representation of the http Client object type for managing resilient clients.
-class ClientObject {
+client class ClientObject {
+
+    # The client resource function to send HTTP POST requests to HTTP endpoints.
+    # 
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP PUT requests to HTTP endpoints.
+    # 
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP PATCH requests to HTTP endpoints.
+    # 
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP DELETE requests to HTTP endpoints.
+    # 
+    resource function delete [... path](RequestMessage message = (), map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP HEAD requests to HTTP endpoints.
+    # 
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
+
+    # The client resource function to send HTTP GET requests to HTTP endpoints.
+    # 
+    resource function get [... path](map<string|string[]>|() headers = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP OPTIONS requests to HTTP endpoints.
+    # 
+    resource function options [... path](map<string|string[]>|() headers = (), TargetType targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The `Client.post()` function can be used to send HTTP POST requests to HTTP endpoints.
+    # 
+    remote function post(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.put()` function can be used to send HTTP PUT requests to HTTP endpoints.
+    # 
+    remote function put(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.patch()` function can be used to send HTTP PATCH requests to HTTP endpoints.
+    # 
+    remote function patch(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.delete()` function can be used to send HTTP DELETE requests to HTTP endpoints.
+    # 
+    remote function delete(string path, RequestMessage message = (), map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.head()` function can be used to send HTTP HEAD requests to HTTP endpoints.
+    # 
+    remote function head(string path, map<string|string[]>|() headers = ()) returns Response|ClientError;
+
+    # The `Client.get()` function can be used to send HTTP GET requests to HTTP endpoints.
+    # 
+    remote function get(string path, map<string|string[]>|() headers = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.options()` function can be used to send HTTP OPTIONS requests to HTTP endpoints.
+    # 
+    remote function options(string path, map<string|string[]>|() headers = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # Invokes an HTTP call with the specified HTTP verb.
+    # 
+    remote function execute(string httpVerb, string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), TargetType targetType = <>) returns targetType|ClientError;
+
+    # The `Client.forward()` function can be used to invoke an HTTP call with inbound request's HTTP verb
+    # 
+    remote function forward(string path, Request request, TargetType targetType = <>) returns targetType|ClientError;
+
+    # Submits an HTTP request to a service with the specified HTTP verb.
+    # The `Client->submit()` function does not give out a `http:Response` as the result.
+    # Rather it returns an `http:HttpFuture` which can be used to do further interactions with the endpoint.
+    # 
+    remote function submit(string httpVerb, string path, RequestMessage message) returns HttpFuture|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function getResponse(HttpFuture httpFuture) returns Response|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function hasPromise(HttpFuture httpFuture) returns boolean;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function getNextPromise(HttpFuture httpFuture) returns PushPromise|ClientError;
+
+    # Passes the request to an actual network call.
+    # 
+    remote function getPromisedResponse(PushPromise promise) returns Response|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function rejectPromise(PushPromise promise) returns ();
 }
 
 # Defines the path parameter types.
@@ -2247,7 +2793,7 @@
 type SimpleQueryParamType boolean|int|float|decimal|string;
 
 # Defines the query parameter type supported with client resource methods.
-type QueryParamType ballerina/http:2.16.6:SimpleQueryParamType[]|boolean|int|float|decimal|string;
+type QueryParamType SimpleQueryParamType[]|boolean|int|float|decimal|string;
 
 # Defines the record type of query parameters supported with client resource methods.
 
@@ -2304,150 +2850,221 @@
     error[] httpActionErr?;
 };
 
-// Unknown type: ListenerError
+# Defines the possible listener error types.
+type ListenerError error;
 
-// Unknown type: ClientError
+# Defines the possible client error types.
+type ClientError error;
 
-// Unknown type: HeaderNotFoundError
+# Represents a header not found error when retrieving headers.
+type HeaderNotFoundError error;
 
-// Unknown type: HeaderBindingError
+# Represents an error, which occurred due to header binding.
+type HeaderBindingError error;
 
-// Unknown type: PayloadBindingError
+# Represents an error, which occurred due to payload binding.
+type PayloadBindingError error;
 
-// Unknown type: MediaTypeBindingError
+# Represents an error, which occurred due to media-type binding.
+type MediaTypeBindingError error;
 
-// Unknown type: InboundRequestError
+# Defines the listener error types that returned while receiving inbound request.
+type InboundRequestError error;
 
-// Unknown type: OutboundResponseError
+# Defines the listener error types that returned while sending outbound response.
+type OutboundResponseError error;
 
-// Unknown type: GenericListenerError
+# Represents a generic listener error.
+type GenericListenerError error;
 
-// Unknown type: InterceptorReturnError
+# Represents an error, which occurred due to a failure in interceptor return.
+type InterceptorReturnError ListenerError & httpscerr:InternalServerErrorError;
 
-// Unknown type: HeaderValidationError
+# Represents an error, which occurred due to a header constraint validation.
+type HeaderValidationError error;
 
-// Unknown type: NoContentError
+# Represents an error, which occurred due to the absence of the payload.
+type NoContentError error;
 
-// Unknown type: PayloadValidationError
+# Represents an error, which occurred due to payload constraint validation.
+type PayloadValidationError error;
 
-// Unknown type: QueryParameterBindingError
+# Represents an error, which occurred due to a query parameter binding.
+type QueryParameterBindingError ListenerError & httpscerr:BadRequestError;
 
-// Unknown type: QueryParameterValidationError
+# Represents an error, which occurred due to a query parameter constraint validation.
+type QueryParameterValidationError error<record {|map<string|string[]> headers?; anydata body?; anydata...;|}>;
 
-// Unknown type: PathParameterBindingError
+# Represents an error, which occurred due to a path parameter binding.
+type PathParameterBindingError ListenerError & httpscerr:BadRequestError;
 
-// Unknown type: MediaTypeValidationError
+# Represents an error, which occurred due to media type validation.
+type MediaTypeValidationError error;
 
-// Unknown type: RequestDispatchingError
+# Represents an error, which occurred during the request dispatching.
+type RequestDispatchingError error;
 
-// Unknown type: ServiceDispatchingError
+# Represents an error, which occurred during the service dispatching.
+type ServiceDispatchingError error;
 
-// Unknown type: ResourceDispatchingError
+# Represents an error, which occurred during the resource dispatching.
+type ResourceDispatchingError error;
 
-// Unknown type: ListenerAuthError
+# Defines the auth error types that returned from listener.
+type ListenerAuthError error;
 
-// Unknown type: ListenerAuthnError
+# Defines the authentication error types that returned from listener.
+type ListenerAuthnError httpscerr:UnauthorizedError & ListenerAuthError;
 
-// Unknown type: ListenerAuthzError
+# Defines the authorization error types that returned from listener.
+type ListenerAuthzError httpscerr:ForbiddenError & ListenerAuthError;
 
-// Unknown type: OutboundRequestError
+# Defines the client error types that returned while sending outbound request.
+type OutboundRequestError error;
 
-// Unknown type: InboundResponseError
+# Defines the client error types that returned while receiving inbound response.
+type InboundResponseError error;
 
-// Unknown type: ClientAuthError
+# Defines the Auth error types that returned from client.
+type ClientAuthError error;
 
-// Unknown type: ResiliencyError
+# Defines the resiliency error types that returned from client.
+type ResiliencyError error;
 
-// Unknown type: GenericClientError
+# Represents a generic client error.
+type GenericClientError error;
 
-// Unknown type: Http2ClientError
+# Represents an HTTP/2 client generic error.
+type Http2ClientError error;
 
-// Unknown type: SslError
+# Represents a client error that occurred due to SSL failure.
+type SslError error;
 
-// Unknown type: ApplicationResponseError
+# Represents both 4XX and 5XX application response client error.
+type ApplicationResponseError error<record {|int statusCode; map<string[]> headers; anydata body; anydata...;|}>;
 
-// Unknown type: UnsupportedActionError
+# Represents a client error that occurred due to unsupported action invocation.
+type UnsupportedActionError error;
 
-// Unknown type: MaximumWaitTimeExceededError
+# Represents a client error that occurred exceeding maximum wait time.
+type MaximumWaitTimeExceededError error;
 
-// Unknown type: CookieHandlingError
+# Represents a cookie error that occurred when using the cookies.
+type CookieHandlingError error;
 
-// Unknown type: ClientConnectorError
+# Represents a client connector error that occurred.
+type ClientConnectorError error;
 
-// Unknown type: ClientRequestError
+# Represents an error, which occurred due to bad syntax or incomplete info in the client request(4xx HTTP response).
+type ClientRequestError error<record {|int statusCode; map<string[]> headers; anydata body; anydata...;|}>;
 
-// Unknown type: RemoteServerError
+# Represents an error, which occurred due to a failure of the remote server(5xx HTTP response).
+type RemoteServerError error<record {|int statusCode; map<string[]> headers; anydata body; anydata...;|}>;
 
-// Unknown type: FailoverAllEndpointsFailedError
+# Represents a client error that occurred due to all the failover endpoint failure.
+type FailoverAllEndpointsFailedError error;
 
-// Unknown type: FailoverActionFailedError
+# Represents a client error that occurred due to failover action failure.
+type FailoverActionFailedError error;
 
-// Unknown type: UpstreamServiceUnavailableError
+# Represents a client error that occurred due to upstream service unavailability.
+type UpstreamServiceUnavailableError error;
 
-// Unknown type: AllLoadBalanceEndpointsFailedError
+# Represents a client error that occurred due to all the load balance endpoint failure.
+type AllLoadBalanceEndpointsFailedError error;
 
-// Unknown type: CircuitBreakerConfigError
+# Represents a client error that occurred due to circuit breaker configuration error.
+type CircuitBreakerConfigError error;
 
-// Unknown type: AllRetryAttemptsFailed
+# Represents a client error that occurred due to all the the retry attempts failure.
+type AllRetryAttemptsFailed error;
 
-// Unknown type: IdleTimeoutError
+# Represents the error that triggered upon a request/response idle timeout.
+type IdleTimeoutError error;
 
-// Unknown type: LoadBalanceActionError
+# Represents an error occurred in an remote function of the Load Balance connector.
+type LoadBalanceActionError ResiliencyError & error<LoadBalanceActionErrorData>;
 
-// Unknown type: InitializingOutboundRequestError
+# Represents a client error that occurred due to outbound request initialization failure.
+type InitializingOutboundRequestError error;
 
-// Unknown type: WritingOutboundRequestHeadersError
+# Represents a client error that occurred while writing outbound request headers.
+type WritingOutboundRequestHeadersError error;
 
-// Unknown type: WritingOutboundRequestBodyError
+# Represents a client error that occurred while writing outbound request entity body.
+type WritingOutboundRequestBodyError error;
 
-// Unknown type: InitializingInboundResponseError
+# Represents a client error that occurred due to inbound response initialization failure.
+type InitializingInboundResponseError error;
 
-// Unknown type: ReadingInboundResponseHeadersError
+# Represents a client error that occurred while reading inbound response headers.
+type ReadingInboundResponseHeadersError error;
 
-// Unknown type: ReadingInboundResponseBodyError
+# Represents a client error that occurred while reading inbound response entity body.
+type ReadingInboundResponseBodyError error;
 
-// Unknown type: InitializingInboundRequestError
+# Represents a listener error that occurred due to inbound request initialization failure.
+type InitializingInboundRequestError error;
 
-// Unknown type: ReadingInboundRequestHeadersError
+# Represents a listener error that occurred while reading inbound request headers.
+type ReadingInboundRequestHeadersError error;
 
-// Unknown type: ReadingInboundRequestBodyError
+# Represents a listener error that occurred while writing the inbound request entity body.
+type ReadingInboundRequestBodyError error;
 
-// Unknown type: InitializingOutboundResponseError
+# Represents a listener error that occurred due to outbound response initialization failure.
+type InitializingOutboundResponseError error;
 
-// Unknown type: WritingOutboundResponseHeadersError
+# Represents a listener error that occurred while writing outbound response headers.
+type WritingOutboundResponseHeadersError error;
 
-// Unknown type: WritingOutboundResponseBodyError
+# Represents a listener error that occurred while writing outbound response entity body.
+type WritingOutboundResponseBodyError error;
 
-// Unknown type: Initiating100ContinueResponseError
+# Represents an error that occurred due to 100 continue response initialization failure.
+type Initiating100ContinueResponseError error;
 
-// Unknown type: Writing100ContinueResponseError
+# Represents an error that occurred while writing 100 continue response.
+type Writing100ContinueResponseError error;
 
-// Unknown type: InvalidCookieError
+# Represents a cookie error that occurred when sending cookies in the response.
+type InvalidCookieError error;
 
-// Unknown type: ServiceNotFoundError
+# Represents Service Not Found error.
+type ServiceNotFoundError httpscerr:NotFoundError & ServiceDispatchingError;
 
-// Unknown type: BadMatrixParamError
+# Represents Bad Matrix Parameter in the request error.
+type BadMatrixParamError httpscerr:BadRequestError & ServiceDispatchingError;
 
-// Unknown type: ResourceNotFoundError
+# Represents an error, which occurred when the resource is not found during dispatching.
+type ResourceNotFoundError httpscerr:NotFoundError & ResourceDispatchingError;
 
-// Unknown type: ResourcePathValidationError
+# Represents an error, which occurred due to a path parameter constraint validation.
+type ResourcePathValidationError httpscerr:BadRequestError & ResourceDispatchingError;
 
-// Unknown type: ResourceMethodNotAllowedError
+# Represents an error, which occurred when the resource method is not allowed during dispatching.
+type ResourceMethodNotAllowedError httpscerr:MethodNotAllowedError & ResourceDispatchingError;
 
-// Unknown type: UnsupportedRequestMediaTypeError
+# Represents an error, which occurred when the media type is not supported during dispatching.
+type UnsupportedRequestMediaTypeError httpscerr:UnsupportedMediaTypeError & ResourceDispatchingError;
 
-// Unknown type: RequestNotAcceptableError
+# Represents an error, which occurred when the payload is not acceptable during dispatching.
+type RequestNotAcceptableError httpscerr:NotAcceptableError & ResourceDispatchingError;
 
-// Unknown type: ResourceDispatchingServerError
+# Represents other internal server errors during dispatching.
+type ResourceDispatchingServerError httpscerr:InternalServerErrorError & ResourceDispatchingError;
 
-// Unknown type: StatusCodeResponseBindingError
+# Represents the client status code binding error
+type StatusCodeResponseBindingError ClientError & error<StatusCodeBindingErrorDetail>;
 
-// Unknown type: StatusCodeBindingClientRequestError
+# Represents the status code binding error that occurred due to 4XX status code response binding
+type StatusCodeBindingClientRequestError StatusCodeResponseBindingError & ClientRequestError;
 
-// Unknown type: StatusCodeBindingRemoteServerError
+# Represents the status code binding error that occurred due to 5XX status code response binding
+type StatusCodeBindingRemoteServerError StatusCodeResponseBindingError & RemoteServerError;
 
 # Represents the client status code response data binding error
-type StatusCodeResponseDataBindingError ballerina/http:2.16.6:MediaTypeBindingStatusCodeClientError|ballerina/http:2.16.6:PayloadBindingStatusCodeClientError|ballerina/http:2.16.6:HeaderBindingStatusCodeClientError;
+type StatusCodeResponseDataBindingError MediaTypeBindingStatusCodeClientError|PayloadBindingStatusCodeClientError|HeaderBindingStatusCodeClientError;
 
 # The HTTP request interceptor service object type
 class RequestInterceptor {
@@ -2467,13 +3084,17 @@
 
 # The service type to be used when engaging interceptors at the service level
 class InterceptableService {
+
+    # Function to define interceptor pipeline
+    # 
+    function createInterceptors() returns RequestInterceptor|ResponseInterceptor|RequestErrorInterceptor|ResponseErrorInterceptor|Interceptor[];
 }
 
 # The return type of an interceptor service function
-type NextService ballerina/http:2.16.6:RequestInterceptor|ballerina/http:2.16.6:ResponseInterceptor|ballerina/http:2.16.6:Service;
+type NextService RequestInterceptor|ResponseInterceptor|Service;
 
 # Types of HTTP interceptor services
-type Interceptor ballerina/http:2.16.6:RequestInterceptor|ballerina/http:2.16.6:ResponseInterceptor|ballerina/http:2.16.6:RequestErrorInterceptor|ballerina/http:2.16.6:ResponseErrorInterceptor;
+type Interceptor RequestInterceptor|ResponseInterceptor|RequestErrorInterceptor|ResponseErrorInterceptor;
 
 # Represents HTTP trace log configuration.
 
@@ -2534,12 +3155,13 @@
 type MutualSslStatus "passed"|"failed"|();
 
 # Represents a non-error type that can be cloned.
-type Cloneable any & readonly|xml|ballerina/http:2.16.6:Cloneable[]|map<ballerina/http:2.16.6:Cloneable>|table<map<ballerina/http:2.16.6:Cloneable>>;
+type Cloneable any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>;
 
 # Request context member type.
-type ReqCtxMember any & readonly|xml|ballerina/http:2.16.6:Cloneable[]|map<ballerina/http:2.16.6:Cloneable>|table<map<ballerina/http:2.16.6:Cloneable>>|isolated object {};
+type ReqCtxMember any & readonly|xml|Cloneable[]|map<Cloneable>|table<map<Cloneable>>|isolated object {};
 
-// Unknown type: ReqCtxMemberType
+# Request context member type descriptor.
+type ReqCtxMemberType typedesc<ReqCtxMember>;
 
 # Defines a status code response record type
 
@@ -2631,11 +3253,11 @@
     # Configurations associated with `crypto:KeyStore` or combination of certificate and (PKCS8) private key of the server
     crypto:KeyStore|CertKey key; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # Configures associated with mutual SSL operations
-    record {|ballerina/http:2.16.6:VerifyClient verifyClient; ballerina/crypto:2.12.1:TrustStore|string cert;|} mutualSsl?;
+    record {|VerifyClient verifyClient; crypto:TrustStore|string cert;|} mutualSsl?;
     # SSL/TLS protocol related options
-    record {|ballerina/http:2.16.6:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # Certificate validation against OCSP_CRL, OCSP_STAPLING related options
-    record {|ballerina/http:2.16.6:CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
+    record {|CertValidationType 'type; int cacheSize; int cacheValidityPeriod;|} certValidation?;
     # List of ciphers to be used
 eg: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     string[] ciphers?;
@@ -2707,7 +3329,97 @@
 };
 
 # The representation of the http Status Code Client object type for managing resilient clients.
-class StatusCodeClientObject {
+client class StatusCodeClientObject {
+
+    # The client resource function to send HTTP POST requests to HTTP endpoints.
+    # 
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP PUT requests to HTTP endpoints.
+    # 
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP PATCH requests to HTTP endpoints.
+    # 
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP DELETE requests to HTTP endpoints.
+    # 
+    resource function delete [... path](RequestMessage message = (), map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP HEAD requests to HTTP endpoints.
+    # 
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
+
+    # The client resource function to send HTTP GET requests to HTTP endpoints.
+    # 
+    resource function get [... path](map<string|string[]>|() headers = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The client resource function to send HTTP OPTIONS requests to HTTP endpoints.
+    # 
+    resource function options [... path](map<string|string[]>|() headers = (), http:StatusCodeResponse targetType = <>, QueryParams params) returns targetType|ClientError;
+
+    # The `Client.post()` function can be used to send HTTP POST requests to HTTP endpoints.
+    # 
+    remote function post(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.put()` function can be used to send HTTP PUT requests to HTTP endpoints.
+    # 
+    remote function put(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.patch()` function can be used to send HTTP PATCH requests to HTTP endpoints.
+    # 
+    remote function patch(string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.delete()` function can be used to send HTTP DELETE requests to HTTP endpoints.
+    # 
+    remote function delete(string path, RequestMessage message = (), map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.head()` function can be used to send HTTP HEAD requests to HTTP endpoints.
+    # 
+    remote function head(string path, map<string|string[]>|() headers = ()) returns Response|ClientError;
+
+    # The `Client.get()` function can be used to send HTTP GET requests to HTTP endpoints.
+    # 
+    remote function get(string path, map<string|string[]>|() headers = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.options()` function can be used to send HTTP OPTIONS requests to HTTP endpoints.
+    # 
+    remote function options(string path, map<string|string[]>|() headers = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # Invokes an HTTP call with the specified HTTP verb.
+    # 
+    remote function execute(string httpVerb, string path, RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # The `Client.forward()` function can be used to invoke an HTTP call with inbound request's HTTP verb
+    # 
+    remote function forward(string path, Request request, http:StatusCodeResponse targetType = <>) returns targetType|ClientError;
+
+    # Submits an HTTP request to a service with the specified HTTP verb.
+    # The `Client->submit()` function does not give out a `http:Response` as the result.
+    # Rather it returns an `http:HttpFuture` which can be used to do further interactions with the endpoint.
+    # 
+    remote function submit(string httpVerb, string path, RequestMessage message) returns HttpFuture|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function getResponse(HttpFuture httpFuture) returns Response|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function hasPromise(HttpFuture httpFuture) returns boolean;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function getNextPromise(HttpFuture httpFuture) returns PushPromise|ClientError;
+
+    # Passes the request to an actual network call.
+    # 
+    remote function getPromisedResponse(PushPromise promise) returns Response|ClientError;
+
+    # This just pass the request to actual network call.
+    # 
+    remote function rejectPromise(PushPromise promise) returns ();
 }
 
 # The status code response record of `NetworkAuthorizationRequired`.
@@ -2740,14 +3452,188 @@
     string method;
 };
 
-// Unknown type: Request
+class Request {
+    function init() returns ();
 
-// Unknown type: RequestCacheControl
+    # Sets the provided `Entity` to the request.
+    # 
+    function setEntity(mime:Entity e) returns (); // Special Agent Note: Entity FROM ballerina/mime package
 
+    # Gets the query parameters of the request as a map consisting of a string array.
+    # 
+    function getQueryParams() returns map<string[]>;
+
+    # Gets the query param value associated with the given key.
+    # 
+    function getQueryParamValue(string key) returns string?;
+
+    # Gets all the query param values associated with the given key.
+    # 
+    function getQueryParamValues(string key) returns string[]?;
+
+    # Gets the matrix parameters of the request.
+    # 
+    function getMatrixParams(string path) returns map<any>;
+
+    # Gets the `Entity` associated with the request.
+    # 
+    function getEntity() returns mime:Entity|ClientError; // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Checks whether the requested header key exists in the header map.
+    # 
+    function hasHeader(string headerName) returns boolean;
+
+    # Returns the value of the specified header. If the specified header key maps to multiple values, the first of
+    # these values is returned.
+    # 
+    function getHeader(string headerName) returns string|HeaderNotFoundError;
+
+    # Gets all the header values to which the specified header key maps to.
+    # 
+    function getHeaders(string headerName) returns string[]|HeaderNotFoundError;
+
+    # Sets the specified header to the request. If a mapping already exists for the specified header key, the existing
+    # header value is replaced with the specified header value. Panic if an illegal header is passed.
+    # 
+    function setHeader(string headerName, string headerValue) returns ();
+
+    # Adds the specified header to the request. Existing header values are not replaced, except for the `Content-Type`
+    # header. In the case of the `Content-Type` header, the existing value is replaced with the specified value.
+    # Panic if an illegal header is passed.
+    # 
+    function addHeader(string headerName, string headerValue) returns ();
+
+    # Removes the specified header from the request.
+    # 
+    function removeHeader(string headerName) returns ();
+
+    # Removes all the headers from the request.
+    function removeAllHeaders() returns ();
+
+    # Gets all the names of the headers of the request.
+    # 
+    function getHeaderNames() returns string[];
+
+    # Checks whether the client expects a `100-continue` response.
+    # 
+    function expects100Continue() returns boolean;
+
+    # Sets the `content-type` header to the request.
+    # 
+    function setContentType(string contentType) returns error?;
+
+    # Gets the type of the payload of the request (i.e: the `content-type` header value).
+    # 
+    function getContentType() returns string;
+
+    # Extract `json` payload from the request. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not JSON, an `http:ClientError` is returned.
+    # 
+    function getJsonPayload() returns json|ClientError;
+
+    # Extracts `xml` payload from the request. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not XML, an `http:ClientError` is returned.
+    # 
+    function getXmlPayload() returns xml|ClientError;
+
+    # Extracts `text` payload from the request. For an empty payload, `http:NoContentError` is returned.
+    # 
+    # If the content type is not of type text, an `http:ClientError` is returned.
+    # 
+    function getTextPayload() returns string|ClientError;
+
+    # Gets the request payload as  a stream of byte[], except in the case of multiparts. To retrieve multiparts, use
+    # `Request.getBodyParts()`.
+    # 
+    function getByteStream(int arraySize = 0) returns stream<byte[], io:Error?>|ClientError;
+
+    # Gets the request payload as a `byte[]`.
+    # 
+    function getBinaryPayload() returns byte[]|ClientError;
+
+    # Gets the form parameters from the HTTP request as a `map` when content type is application/x-www-form-urlencoded.
+    # 
+    function getFormParams() returns map<string>|ClientError;
+
+    # Extracts body parts from the request. If the content type is not a composite media type, an error
+    # is returned.
+    function getBodyParts() returns mime:Entity[]|ClientError; // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Sets a `json` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/json`. Any existing content-type can be
+    # overridden by passing the content-type as an optional parameter. If the given payload is a record type with 
+    # the `@jsondata:Name` annotation, the `jsondata:toJson` function internally converts the record to JSON
+    # 
+    function setJsonPayload(json payload, string|() contentType = ()) returns ();
+
+    # Sets an `xml` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/xml`. Any existing content-type can be
+    # overridden by passing the content-type as an optional parameter.
+    # 
+    function setXmlPayload(xml payload, string|() contentType = ()) returns ();
+
+    # Sets a `string` as the payload. If the content-type header is not set then this method set
+    # content-type headers with the default content-type, which is `text/plain`. Any
+    # existing content-type can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setTextPayload(string payload, string|() contentType = ()) returns ();
+
+    # Sets a `byte[]` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/octet-stream`. Any existing content-type
+    # can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setBinaryPayload(byte[] payload, string|() contentType = ()) returns ();
+
+    # Set multiparts as the payload. If the content-type header is not set then this method
+    # set content-type headers with the default content-type, which is `multipart/form-data`.
+    # Any existing content-type can be overridden by passing the content-type as an optional parameter.
+    # 
+    function setBodyParts(mime:Entity[] bodyParts, string|() contentType = ()) returns (); // Special Agent Note: Entity FROM ballerina/mime package
+
+    # Sets the content of the specified file as the entity body of the request. If the content-type header
+    # is not set then this method set content-type headers with the default content-type, which is
+    # `application/octet-stream`. Any existing content-type can be overridden by passing the content-type
+    # as an optional parameter.
+    # 
+    function setFileAsPayload(string filePath, string|() contentType = ()) returns ();
+
+    # Sets a `Stream` as the payload. If the content-type header is not set then this method set content-type
+    # headers with the default content-type, which is `application/octet-stream`. Any existing content-type can
+    # be overridden by passing the content-type as an optional parameter.
+    # 
+    function setByteStream(stream<byte[], io:Error?> byteStream, string|() contentType = ()) returns ();
+
+    # Sets the request payload. This method overrides any existing content-type by passing the content-type
+    # as an optional parameter. If the content type parameter is not provided then the default value derived
+    # from the payload will be used as content-type only when there are no existing content-type header.
+    # 
+    function setPayload(anydata|mime:Entity[]|stream<byte[], io:Error?> payload, string|() contentType = ()) returns ();
+
+    # Adds cookies to the request.
+    # 
+    function addCookies(Cookie[] cookiesToAdd) returns ();
+
+    # Gets cookies from the request.
+    # 
+    function getCookies() returns Cookie[];
+}
+
+# Configures the cache control directives for an `http:Request`.
+# 
+class RequestCacheControl {
+
+    # Builds the cache control directives string from the current `http:RequestCacheControl` configurations.
+    # 
+    function buildCacheControlDirectives() returns string;
+}
+
 # The types of messages that are accepted by HTTP `client` when sending out the outbound request.
-type RequestMessage anydata|ballerina/http:2.16.6:Request|ballerina/mime:2.12.2:Entity[]|stream<byte[], ballerina/io:1.8.1:Error?>;
+type RequestMessage anydata|Request|mime:Entity[]|stream<byte[], io:Error?>;
 
-// Unknown type: TargetType
+# The types of data values that are expected by the HTTP `client` to return after the data binding operation.
+type TargetType typedesc<Response|anydata|stream<SseEvent, error?>>;
 
 # Defines the HTTP operations related to circuit breaker, failover and load balancer.
 # 
@@ -2763,7 +3649,10 @@
 # `NONE`: No operation should be performed
 type HttpOperation "FORWARD"|"GET"|"POST"|"DELETE"|"OPTIONS"|"PUT"|"PATCH"|"HEAD"|"SUBMIT"|"NONE";
 
-// Unknown type: HttpFuture
+# Represents a 'future' that returns as a result of an asynchronous HTTP request submission.
+# This can be used as a reference to fetch the results of the submission.
+class HttpFuture {
+}
 
 # Represents a server-provided hyperlink
 
@@ -2782,7 +3671,7 @@
 
 type Links record {
     # Map of available links
-    map<ballerina/http:2.16.6:Link> _links;
+    map<Link> _links;
 };
 
 # Represents the parsed header value details
@@ -2886,6 +3775,10 @@
 
 # LoadBalancerRule object type provides a required abstraction to implement different algorithms.
 class LoadBalancerRule {
+
+    # Provides an HTTP client which is chosen according to the algorithm.
+    # 
+    function getNextClient(Client|()[] loadBalanceCallerActionsArray) returns Client|ClientError;
 }
 
 # The configurations related to the load balancing client endpoint. The following fields are inherited from the other
@@ -2919,24 +3812,229 @@
     boolean laxDataBinding?;
 };
 
-// Unknown type: HttpCache
+# Creates the HTTP cache.
+# 
+class HttpCache {
+    function init(CacheConfig cacheConfig) returns ();
+}
 
-// Unknown type: Cookie
+# Initializes the `http:Cookie` object.
+# 
+class Cookie {
+    function init(string name, string value, string path = "", string domain = "", string expires = "", int maxAge = 0, boolean httpOnly = false, boolean secure = false, time:Utc createdTime = time:utcNow(), time:Utc lastAccessedTime = time:utcNow(), boolean hostOnly = false, CookieOptions options) returns (); // Special Agent Note: Utc FROM ballerina/time package
 
-// Unknown type: CookieStore
+    # Checks the persistence of the cookie.
+    # 
+    function isPersistent() returns boolean;
 
-// Unknown type: CsvPersistentCookieHandler
+    # Checks the validity of the attributes of the cookie.
+    # 
+    function isValid() returns boolean|InvalidCookieError;
 
-// Unknown type: PushPromise
+    # Gets the Cookie object in its string representation to be used in the ‘Set-Cookie’ header of the response.
+    # 
+    function toStringValue() returns string;
+}
 
-// Unknown type: Headers
+class CookieStore {
+    function init(PersistentCookieHandler|() persistentCookieHandler = ()) returns ();
 
-// Unknown type: RequestContext
+    # Adds a cookie to the cookie store according to the rules in [RFC-6265](https://tools.ietf.org/html/rfc6265#section-5.3).
+    # 
+    function addCookie(Cookie cookie, CookieConfig cookieConfig, string url, string requestPath) returns CookieHandlingError|();
 
-// Unknown type: Listener
+    # Adds an array of cookies.
+    # 
+    function addCookies(Cookie[] cookiesInResponse, CookieConfig cookieConfig, string url, string requestPath) returns ();
 
-// Unknown type: LoadBalancerRoundRobinRule
+    # Gets the relevant cookies for the given URL and the path according to the rules in [RFC-6265](https://tools.ietf.org/html/rfc6265#section-5.4).
+    # 
+    function getCookies(string url, string requestPath) returns Cookie[];
 
+    # Gets all the cookies in the cookie store.
+    # 
+    function getAllCookies() returns Cookie[];
+
+    # Gets all the cookies, which have the given name as the name of the cookie.
+    # 
+    function getCookiesByName(string cookieName) returns Cookie[];
+
+    # Gets all the cookies, which have the given name as the domain of the cookie.
+    # 
+    function getCookiesByDomain(string domain) returns Cookie[];
+
+    # Removes a specific cookie.
+    # 
+    function removeCookie(string name, string domain, string path) returns CookieHandlingError|();
+
+    # Removes cookies, which match with the given domain.
+    # 
+    function removeCookiesByDomain(string domain) returns CookieHandlingError|();
+
+    # Removes all expired cookies.
+    # 
+    function removeExpiredCookies() returns CookieHandlingError|();
+
+    # Removes all the cookies.
+    # 
+    function removeAllCookies() returns CookieHandlingError|();
+}
+
+class CsvPersistentCookieHandler {
+    function init(string fileName) returns ();
+
+    # Adds a persistent cookie to the cookie store.
+    # 
+    function storeCookie(Cookie cookie) returns CookieHandlingError|();
+
+    # Gets all the persistent cookies.
+    # 
+    function getAllCookies() returns Cookie[]|CookieHandlingError;
+
+    # Removes a specific persistent cookie.
+    # 
+    function removeCookie(string name, string domain, string path) returns CookieHandlingError|();
+
+    # Removes all persistent cookies.
+    # 
+    function removeAllCookies() returns CookieHandlingError|();
+}
+
+# Constructs an `http:PushPromise` from a given path and a method.
+# 
+class PushPromise {
+    function init(string path = "/", string method = "GET") returns ();
+
+    # Checks whether the requested header exists.
+    # 
+    function hasHeader(string headerName) returns boolean;
+
+    # Returns the header value with the specified header name.
+    # If there are more than one header value for the specified header name, the first value is returned.
+    # 
+    function getHeader(string headerName) returns string;
+
+    # Gets transport headers from the `PushPromise`.
+    # 
+    function getHeaders(string headerName) returns string[];
+
+    # Adds the specified key/value pair as an HTTP header to the `http:PushPromise`. In the case of the `Content-Type`
+    # header, the existing value is replaced with the specified value.
+    # 
+    function addHeader(string headerName, string headerValue) returns ();
+
+    # Sets the value of a transport header in the `http:PushPromise`.
+    # 
+    function setHeader(string headerName, string headerValue) returns ();
+
+    # Removes a transport header from the `http:PushPromise`.
+    # 
+    function removeHeader(string headerName) returns ();
+
+    # Removes all transport headers from the `http:PushPromise`.
+    function removeAllHeaders() returns ();
+
+    # Gets all transport header names from the `http:PushPromise`.
+    # 
+    function getHeaderNames() returns string[];
+}
+
+# Represents the headers of the inbound request.
+class Headers {
+
+    # Checks whether the requested header key exists in the header map.
+    # 
+    function hasHeader(string headerName) returns boolean;
+
+    # Returns the value of the specified header. If the specified header key maps to multiple values, the first of
+    # these values is returned.
+    # 
+    function getHeader(string headerName) returns string|HeaderNotFoundError;
+
+    # Gets all the header values to which the specified header key maps to.
+    # 
+    function getHeaders(string headerName) returns string[]|HeaderNotFoundError;
+
+    # Gets all the names of the headers of the request.
+    # 
+    function getHeaderNames() returns string[];
+}
+
+# Represents an HTTP Context that allows user to pass data between interceptors.
+class RequestContext {
+
+    # Sets a member to the request context object.
+    # 
+    function set(string key, ReqCtxMember value) returns ();
+
+    # Gets a member value from the request context object. It panics if there is no such member.
+    # 
+    function get(string key) returns ReqCtxMember;
+
+    # Checks whether the request context object has a member corresponds to the key.
+    # 
+    function hasKey(string key) returns boolean;
+
+    # Returns the member keys of the request context object.
+    # 
+    function keys() returns string[];
+
+    # Gets a member value with type from the request context object.
+    # 
+    function getWithType(string key, any & readonly|xml|http:Cloneable[]|map<http:Cloneable>|table<map<http:Cloneable>>|isolated object {} targetType = http:ReqCtxMember) returns targetType|ListenerError;
+
+    # Removes a member from the request context object. It panics if there is no such member.
+    # 
+    function remove(string key) returns ();
+
+    # Calls the next service in the interceptor pipeline.
+    # 
+    function next() returns RequestInterceptor|ResponseInterceptor|Service|error|();
+}
+
+# Gets invoked during module initialization to initialize the listener.
+# 
+class Listener {
+    function init(int port, string host = "0.0.0.0", ListenerHttp1Settings http1Settings = {}, ListenerSecureSocket|() secureSocket = (), HttpVersion httpVersion = HTTP_2_0, decimal timeout = 60, string|() server = (), RequestLimitConfigs requestLimits = {}, decimal gracefulStopTimeout = 0, ServerSocketConfig socketConfig = {}, int http2InitialWindowSize = 65535, decimal minIdleTimeInStaleState = 300, decimal timeBetweenStaleEviction = 30, ListenerConfiguration config) returns ListenerError?;
+
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
+    function attach(Service httpService, string[]|string|() name = ()) returns error?;
+
+    # Detaches an HTTP service from the listener.
+    # 
+    function detach(Service httpService) returns error?;
+
+    # Retrieves the port of the HTTP listener.
+    # 
+    function getPort() returns int;
+
+    # Retrieves the `InferredListenerConfiguration` of the HTTP listener.
+    # 
+    function getConfig() returns InferredListenerConfiguration & readonly;
+}
+
+# Implementation of round robin load balancing strategy.
+# 
+class LoadBalancerRoundRobinRule {
+
+    # Provides an HTTP client, which is chosen according to the round robin algorithm.
+    # 
+    function getNextClient(Client|()[] loadBalanceCallerActionsArray) returns Client|ClientError;
+}
+
 // --- Client ---
 
 # Defines the OAuth2 handler for client authentication.
@@ -2949,11 +4047,11 @@
 
     # Enrich the headers map with the relevant authentication requirements.
     # 
-    remote function enrichHeaders(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
+    function enrichHeaders(map<string|string[]> headers) returns map<string|string[]>|ClientAuthError;
 
     # Returns the headers map with the relevant authentication requirements.
     # 
-    remote function getSecurityHeaders() returns map<string|string[]>|ClientAuthError;
+    function getSecurityHeaders() returns map<string|string[]>|ClientAuthError;
 }
 
 # Defines the LDAP store Basic Auth handler for listener authentication.
@@ -2981,11 +4079,11 @@
 # The HTTP client provides functionality to connect to remote HTTP services and perform requests using standard HTTP methods like GET, POST, PUT, DELETE, etc.
 # 
 client class Client {
-    function init(string url, HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, ClientSecureSocket|() secureSocket = (), ClientConfiguration config) returns ballerina/http:2.16.6:ClientError?;
+    function init(string url, HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, ClientSecureSocket|() secureSocket = (), ClientConfiguration config) returns ClientError?;
 
     # The client resource function to send HTTP GET requests to HTTP endpoints.
     # 
-    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Retrieve a representation of a specified resource from an HTTP endpoint.
     # 
@@ -2993,7 +4091,7 @@
 
     # The client resource function to send HTTP POST requests to HTTP endpoints.
     # 
-    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Create a new resource or submit data to a resource for processing.
     # 
@@ -3001,7 +4099,7 @@
 
     # The client resource function to send HTTP PUT requests to HTTP endpoints.
     # 
-    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Create a new resource or replace a representation of a specified resource.
     # 
@@ -3009,7 +4107,7 @@
 
     # The client resource function to send HTTP DELETE requests to HTTP endpoints.
     # 
-    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Remove a specified resource from an HTTP endpoint.
     # 
@@ -3017,7 +4115,7 @@
 
     # The client resource function to send HTTP PATCH requests to HTTP endpoints.
     # 
-    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Partially update an existing resource in an HTTP endpoint.
     # 
@@ -3025,7 +4123,7 @@
 
     # The client resource function to send HTTP HEAD requests to HTTP endpoints.
     # 
-    resource function head [... path](map<string|string[]>|() headers = (), QueryParamType Additional Values, QueryParams params) returns Response|ClientError;
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
 
     # Get the metadata of a resource in the form of headers without the body. Often used for testing the resource existence or finding recent modifications.
     # 
@@ -3033,7 +4131,7 @@
 
     # The client resource function to send HTTP OPTIONS requests to HTTP endpoints.
     # 
-    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # Get the communication options for a specified resource.
     # 
@@ -3073,19 +4171,19 @@
 
     # Get the cookie storage associated with this HTTP client. Can be used to access stored cookies for session management.
     # 
-    remote function getCookieStore() returns CookieStore|();
+    function getCookieStore() returns CookieStore|();
 
     # Force the circuit breaker to allow all requests through, ignoring current error rates. Can be used to manually
     # restore service after fixing issues.
-    remote function circuitBreakerForceClose() returns ();
+    function circuitBreakerForceClose() returns ();
 
     # Force the circuit breaker to block all requests until the reset time expires. Can be used to manually stop
     # requests during maintenance or known issues.
-    remote function circuitBreakerForceOpen() returns ();
+    function circuitBreakerForceOpen() returns ();
 
     # Check the current state of the circuit breaker. Can be used to monitor the health status of your HTTP connections.
     # 
-    remote function getCircuitBreakerCurrentState() returns CircuitState;
+    function getCircuitBreakerCurrentState() returns CircuitState;
 }
 
 # The caller actions for responding to client requests.
@@ -3119,18 +4217,18 @@
     # string? remoteHost = caller.getRemoteHostName();
     # ```
     # 
-    remote function getRemoteHostName() returns string?;
+    function getRemoteHostName() returns string?;
 }
 
 # The HTTP status code client provides the capability for initiating contact with a remote HTTP service. The API it
 # provides includes the functions for the standard HTTP methods forwarding a received request and sending requests
 # using custom HTTP verbs. The responses can be binded to `http:StatusCodeResponse` types
 client class StatusCodeClient {
-    function init(string url, HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, ClientSecureSocket|() secureSocket = (), ClientConfiguration config) returns ballerina/http:2.16.6:ClientError?;
+    function init(string url, HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, ClientSecureSocket|() secureSocket = (), ClientConfiguration config) returns ClientError?;
 
     # The client resource function to send HTTP POST requests to HTTP endpoints.
     # 
-    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.post()` function can be used to send HTTP POST requests to HTTP endpoints.
     # 
@@ -3138,7 +4236,7 @@
 
     # The client resource function to send HTTP PUT requests to HTTP endpoints.
     # 
-    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.put()` function can be used to send HTTP PUT requests to HTTP endpoints.
     # 
@@ -3146,7 +4244,7 @@
 
     # The client resource function to send HTTP PATCH requests to HTTP endpoints.
     # 
-    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.patch()` function can be used to send HTTP PATCH requests to HTTP endpoints.
     # 
@@ -3154,7 +4252,7 @@
 
     # The client resource function to send HTTP DELETE requests to HTTP endpoints.
     # 
-    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.delete()` function can be used to send HTTP DELETE requests to HTTP endpoints.
     # 
@@ -3162,7 +4260,7 @@
 
     # The client resource function to send HTTP HEAD requests to HTTP endpoints.
     # 
-    resource function head [... path](map<string|string[]>|() headers = (), QueryParamType Additional Values, QueryParams params) returns Response|ClientError;
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
 
     # The `Client.head()` function can be used to send HTTP HEAD requests to HTTP endpoints.
     # 
@@ -3170,7 +4268,7 @@
 
     # The client resource function to send HTTP GET requests to HTTP endpoints.
     # 
-    resource function get [... path](map<string|string[]>|() headers = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function get [... path](map<string|string[]>|() headers = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.get()` function can be used to send HTTP GET requests to HTTP endpoints.
     # 
@@ -3178,7 +4276,7 @@
 
     # The client resource function to send HTTP OPTIONS requests to HTTP endpoints.
     # 
-    resource function options [... path](map<string|string[]>|() headers = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function options [... path](map<string|string[]>|() headers = (), StatusCodeResponse targetType = http:StatusCodeResponse, QueryParams params) returns targetType|ClientError;
 
     # The `Client.options()` function can be used to send HTTP OPTIONS requests to HTTP endpoints.
     # 
@@ -3220,29 +4318,29 @@
 
     # Retrieves the cookie store of the client.
     # 
-    remote function getCookieStore() returns CookieStore|();
+    function getCookieStore() returns CookieStore|();
 
     # The circuit breaker client related method to force the circuit into a closed state in which it will allow
     # requests regardless of the error percentage until the failure threshold exceeds.
-    remote function circuitBreakerForceClose() returns ();
+    function circuitBreakerForceClose() returns ();
 
     # The circuit breaker client related method to force the circuit into a open state in which it will suspend all
     # requests until `resetTime` interval exceeds.
-    remote function circuitBreakerForceOpen() returns ();
+    function circuitBreakerForceOpen() returns ();
 
     # The circuit breaker client related method to provides the `http:CircuitState` of the circuit breaker.
     # 
-    remote function getCircuitBreakerCurrentState() returns CircuitState;
+    function getCircuitBreakerCurrentState() returns CircuitState;
 }
 
 # An HTTP client endpoint which provides failover support over multiple HTTP clients.
 # 
 client class FailoverClient {
-    function init(HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, TargetService[] targets = [], int[] failoverCodes = [501, 502, 503, 504], decimal interval = 0, FailoverClientConfiguration failoverClientConfig) returns ballerina/http:2.16.6:ClientError?;
+    function init(HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, TargetService[] targets = [], int[] failoverCodes = [501, 502, 503, 504], decimal interval = 0, FailoverClientConfiguration failoverClientConfig) returns ClientError?;
 
     # The POST resource function implementation of the Failover Connector.
     # 
-    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The POST remote function implementation of the Failover Connector.
     # 
@@ -3250,7 +4348,7 @@
 
     # The PUT resource function implementation of the Failover Connector.
     # 
-    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The PUT remote function  implementation of the Failover Connector.
     # 
@@ -3258,7 +4356,7 @@
 
     # The PATCH resource function implementation of the Failover Connector.
     # 
-    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The PATCH remote function implementation of the Failover Connector.
     # 
@@ -3266,7 +4364,7 @@
 
     # The DELETE resource function implementation of the Failover Connector.
     # 
-    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The DELETE remote function implementation of the Failover Connector.
     # 
@@ -3274,7 +4372,7 @@
 
     # The HEAD resource function implementation of the Failover Connector.
     # 
-    resource function head [... path](map<string|string[]>|() headers = (), QueryParamType Additional Values, QueryParams params) returns Response|ClientError;
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
 
     # The HEAD remote function implementation of the Failover Connector.
     # 
@@ -3282,7 +4380,7 @@
 
     # The GET resource function implementation of the Failover Connector.
     # 
-    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The GET remote function implementation of the Failover Connector.
     # 
@@ -3290,7 +4388,7 @@
 
     # The OPTIONS resource function implementation of the Failover Connector.
     # 
-    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The OPTIONS remote function implementation of the Failover Connector.
     # 
@@ -3333,17 +4431,17 @@
 
     # Gets the index of the `TargetService[]` array which given a successful response.
     # 
-    remote function getSucceededEndpointIndex() returns int;
+    function getSucceededEndpointIndex() returns int;
 }
 
 # LoadBalanceClient endpoint provides load balancing functionality over multiple HTTP clients.
 # 
 client class LoadBalanceClient {
-    function init(HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, TargetService[] targets = [], LoadBalancerRule|() lbRule = (), boolean failover = true, LoadBalanceClientConfiguration loadBalanceClientConfig) returns ballerina/http:2.16.6:ClientError?;
+    function init(HttpVersion httpVersion = "2.0", ClientHttp1Settings http1Settings = {}, ClientHttp2Settings http2Settings = {}, decimal timeout = 0.0d, string forwarded = "", FollowRedirects|() followRedirects = (), PoolConfiguration|() poolConfig = (), CacheConfig cache = {}, Compression compression = "AUTO", CredentialsConfig|BearerTokenConfig|JwtIssuerConfig|OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|OAuth2RefreshTokenGrantConfig|OAuth2JwtBearerGrantConfig|() auth = (), CircuitBreakerConfig|() circuitBreaker = (), RetryConfig|() retryConfig = (), CookieConfig|() cookieConfig = (), ResponseLimitConfigs responseLimits = {}, ProxyConfig|() proxy = (), boolean validation = false, ClientSocketConfig socketConfig = {}, boolean laxDataBinding = false, TargetService[] targets = [], LoadBalancerRule|() lbRule = (), boolean failover = true, LoadBalanceClientConfiguration loadBalanceClientConfig) returns ClientError?;
 
     # The POST resource function implementation of the LoadBalancer Connector.
     # 
-    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function post [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The POST remote function implementation of the LoadBalancer Connector.
     # 
@@ -3351,7 +4449,7 @@
 
     # The PUT resource function implementation of the LoadBalancer Connector.
     # 
-    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function put [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The PUT remote function implementation of the Load Balance Connector.
     # 
@@ -3359,7 +4457,7 @@
 
     # The PATCH resource function implementation of the LoadBalancer Connector.
     # 
-    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function patch [... path](RequestMessage message, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The PATCH remote function implementation of the LoadBalancer Connector.
     # 
@@ -3367,7 +4465,7 @@
 
     # The DELETE resource function implementation of the LoadBalancer Connector.
     # 
-    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function delete [... path](RequestMessage message = {}, map<string|string[]>|() headers = (), string|() mediaType = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The DELETE remote function implementation of the LoadBalancer Connector.
     # 
@@ -3375,7 +4473,7 @@
 
     # The HEAD resource function implementation of the LoadBalancer Connector.
     # 
-    resource function head [... path](map<string|string[]>|() headers = (), QueryParamType Additional Values, QueryParams params) returns Response|ClientError;
+    resource function head [... path](map<string|string[]>|() headers = (), QueryParams params) returns Response|ClientError;
 
     # The HEAD remote function implementation of the LoadBalancer Connector.
     # 
@@ -3383,7 +4481,7 @@
 
     # The GET resource function implementation of the LoadBalancer Connector.
     # 
-    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function get [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The GET remote function implementation of the LoadBalancer Connector.
     # 
@@ -3391,7 +4489,7 @@
 
     # The OPTIONS resource function implementation of the LoadBalancer Connector.
     # 
-    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParamType Additional Values, QueryParams params) returns targetType|ClientError;
+    resource function options [... path](map<string|string[]>|() headers = (), http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<http:SseEvent, error?>, QueryParams params) returns targetType|ClientError;
 
     # The OPTIONS remote function implementation of the LoadBalancer Connector.
     # 
@@ -3518,15 +4616,54 @@
 
 // --- Service ---
 
-// --- Service (generic) ---
-// Service Type: Service
-// Listener: http:Listener(int port, ListenerConfiguration config)
-// Instructions:
+# The service identifier requires a base path, e.g. `/orders` — replace `/basePath`.
+# Optional: this service may carry the @http:ServiceConfig annotation. Replace {...} with its fields, which are those of http:HttpServiceConfig.
+@http:ServiceConfig {...} // optional
+service http:Service /basePath on new http:Listener(int port, http:ListenerConfiguration config = {}) {
+    // This service type takes any number of resource handlers, and you choose each one's name.
+    // Declare as many as the requirement needs, following this shape:
+    // Only resource methods are accepted here — a remote method does not compile.
+    // One resource method per HTTP endpoint. The accessor is the HTTP verb and the resource path is the URL path, both are written into the method signature rather than configured here.
+    // + caller - Handle for building and sending the response explicitly, instead of returning a value.
+    // + request - The raw inbound request, for anything the bound parameters do not expose.
+    // + headers - Read-only access to the inbound request headers.
+    // + payload - The request body, bound to the declared type, see the requestPayload data-binding rule.
+    // Resource: the accessor must be one of `get`, `post`, `put`, `delete`, `patch`, `head`, `options`, `default`; a path is required and is author-chosen — replace `pathSegment`.
+    // Zero or more further parameters (the `@http:Query` slot) of type string (or int, boolean, decimal, float) may be added, each independently named.
+    // Zero or more further parameters (the `@http:Header` slot) of type string (or int, boolean, decimal, float) may be added, each independently named.
+    // The `caller` parameter may carry @http:CallerInfo, written `@http:CallerInfo {}` before its type. Its fields are those of http:HttpCallerInfo.
+    // The `payload` parameter may carry @http:Payload, written `@http:Payload {}` before its type. Its fields are those of http:HttpPayload.
+    // Each repeated `string` parameter may carry @http:Query, written `@http:Query {}` before its type. Its fields are those of http:HttpQuery.
+    // Each repeated `string` parameter may carry @http:Header, written `@http:Header {}` before its type. Its fields are those of http:HttpHeader.
+    // The return may carry @http:Cache, written `@http:Cache {}` in the `returns` clause. Its fields are those of http:HttpCacheConfig.
+    // Required parameters: none — every parameter in the signature may be omitted.
+    // Optional parameters (may be omitted): caller, request, headers, payload
+    // A handler may carry @http:ResourceConfig. Its fields are those of http:HttpResourceConfig.
+    // @http:ResourceConfig {} // optional
+    // resource function get pathSegment(http:Caller caller, http:Request request, http:Headers headers, anydata payload) returns anydata|http:Response|error;
+}
 
 // --- Annotations ---
 
-# Define advanced configurations like service level security, etc.
-public annotation HttpServiceConfig ServiceConfig on service;
+# The annotation which is used to configure an HTTP service.
+public annotation HttpServiceConfig ServiceConfig on type, service;
 
-# Define advanced configurations like resource level media types, security, etc.
-public annotation HttpResourceConfig ResourceConfig on service_function;
+# The annotation which is used to configure an HTTP resource.
+public annotation HttpResourceConfig ResourceConfig on object function;
+
+# The annotation which is used to define the Payload resource signature parameter and return parameter.
+public annotation HttpPayload Payload on parameter, return;
+
+# The annotation which is used to configure the type of the response.
+public annotation HttpCallerInfo CallerInfo on parameter;
+
+# The annotation which is used to define the Header parameter.
+public annotation HttpHeader Header on parameter, record field;
+
+# The annotation which is used to define the query parameter.
+public annotation HttpQuery Query on parameter, record field;
+
+# The annotation which is used to define the response cache configuration. This annotation only supports `anydata` and
+# Success(2XX) `StatusCodeResponses` return types. Default annotation adds `must-revalidate,public,max-age=3600` as
+# `cache-control` header in addition to `etag` and `last-modified` headers.
+public annotation HttpCacheConfig Cache on return;
`````

# salesforce — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `salesforce` |
| **Old file** | `salesforce/old/ballerinax_salesforce.bal.txt` |
| **New file** | `salesforce/new/ballerinax_salesforce.bal.txt` |
| **Old lines** | 1769 |
| **New lines** | 1985 |
| **Lines added** | 241 |
| **Lines removed** | 25 |
| **Hunks** | 15 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 11 | 0 |
| `// --- section ---` markers | 5 | 5 |

### Declarations added (25)

- `class InMemoryCoordinator`
- `class InMemoryTokenStore`
- `class Listener`
- `function 'start`
- `function acquireLock`
- `function attach`
- `function attemptLeadership`
- `function clearTokenData`
- `function detach`
- `function getCheckpoint`
- `function getRefreshToken`
- `function getTokenData`
- `function gracefulStop`
- `function immediateStop`
- `function init`
- `function onMessage`
- `function reconnect`
- `function recordEventDispatched`
- `function releaseLock`
- `function relinquishLeadership`
- `function renewLeadership`
- `function saveCheckpoint`
- `function setTokenData`
- `function updateRefreshToken`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 820–825 | 820–889 | Types | +64 | −0 |
| 2 | 835–841 | 899–905 | Types | +1 | −1 |
| 3 | 895–901 | 959–965 | Types | +1 | −1 |
| 4 | 936–942 | 1000–1006 | Types | +1 | −1 |
| 5 | 946–952 | 1010–1016 | Types | +1 | −1 |
| 6 | 958–963 | 1022–1054 | Types | +27 | −0 |
| 7 | 986–992 | 1077–1083 | Types | +1 | −1 |
| 8 | 1040–1059 | 1131–1171 | Types | +23 | −2 |
| 9 | 1485–1491 | 1597–1603 | Types | +1 | −1 |
| 10 | 1513–1519 | 1625–1631 | Types | +1 | −1 |
| 11 | 1534–1545 | 1646–1761 | Types | +108 | −4 |
| 12 | 1575–1581 | 1791–1797 | Client | +1 | −1 |
| 13 | 1695–1701 | 1911–1917 | Client | +1 | −1 |
| 14 | 1740–1746 | 1956–1962 | Client | +1 | −1 |
| 15 | 1750–1769 | 1966–1985 | Client | +9 | −9 |

---

## Unified diff

`````diff
--- salesforce/old/ballerinax_salesforce.bal.txt	2026-08-12 12:57:30
+++ salesforce/new/ballerinax_salesforce.bal.txt	2026-08-12 13:19:19
@@ -820,6 +820,70 @@
 # point one of them acquires the token and resumes the subscription from the
 # last persisted `replayId`.
 class ListenerCoordinator {
+
+    # Attempts to become the leader for the given coordination group.
+    # 
+    # Semantics:
+    # - If no replica currently holds leadership, the caller acquires it.
+    # - If the caller is already the leader, this is a no-op success.
+    # **Implementations MUST NOT refresh the heartbeat timestamp in this
+    # case.** Refreshing the heartbeat from `attemptLeadership()` would
+    # silently renew the lease even when called from `standbyTick()` after
+    # a failed `startListenerWithOAuth2()`, preventing a healthy standby
+    # from taking over. Heartbeat refresh is the exclusive responsibility
+    # of `renewLeadership()`, which is only called from `leaderTick()` while
+    # the CometD subscription is actually active.
+    # - If a different replica holds leadership AND its last heartbeat is
+    # within `livenessInterval` seconds, the caller remains a standby.
+    # - If a different replica holds leadership but its heartbeat is older
+    # than `livenessInterval` seconds, the caller takes over.
+    # 
+    # The implementation MUST treat acquisition as atomic with respect to
+    # concurrent callers (e.g. via `INSERT ... ON CONFLICT DO UPDATE` for
+    # SQL-backed implementations).
+    # 
+    function attemptLeadership(string groupId, string nodeId, decimal livenessInterval) returns boolean|error;
+
+    # Refreshes the leader's heartbeat to keep its lease alive. Should be
+    # invoked at an interval strictly less than `livenessInterval`.
+    # 
+    # If this replica is no longer the recorded leader (e.g. another replica
+    # has taken over after a missed heartbeat), implementations MUST return an
+    # error so the caller can drop back to standby.
+    # 
+    function renewLeadership(string groupId, string nodeId) returns error?;
+
+    # Persists the latest successfully-dispatched `replayId` for a channel so
+    # that the next leader can resume the subscription without re-processing
+    # already-handled events.
+    # 
+    # Called from the event-dispatch path after the user's `onEvent` handler
+    # returns successfully. Implementations are encouraged (but not required)
+    # to batch writes — the contract is "the most recent replayId observed
+    # here MUST be readable by `getCheckpoint` after a leader handover."
+    # 
+    function saveCheckpoint(string channel, int replayId) returns error?;
+
+    # Reads the most recently checkpointed `replayId` for a channel. Returns
+    # `()` if no checkpoint has ever been saved for this channel — in which
+    # case the listener should fall back to its configured `replayFrom`.
+    # 
+    function getCheckpoint(string channel) returns int|error?;
+
+    # Immediately releases the leadership lease for the given coordination group.
+    # Called on graceful shutdown so that standbys can take over at their next
+    # poll tick (`heartbeatInterval` seconds) rather than waiting for the full
+    # `livenessInterval` to expire.
+    # 
+    # Semantics:
+    # - If the caller is the current leader, the lease is cleared immediately
+    # (e.g. DELETE the row, or set `leader_node_id = NULL`).
+    # - If the caller is NOT the current leader (already lost the lease or never
+    # held it), this MUST be a silent no-op — never return an error in that case.
+    # - Implementations MUST be idempotent: calling twice for the same node has
+    # the same effect as calling once.
+    # 
+    function relinquishLeadership(string groupId, string nodeId) returns error?;
 }
 
 # Configurations related to username/password authentication.
@@ -835,7 +899,7 @@
 
 type CommonListenerConfig record {
     # The replay ID to change the point in time when events are read
-    int|ballerinax/salesforce:8.7.0:ReplayOptions replayFrom?;
+    int|ReplayOptions replayFrom?;
     # The maximum time in seconds to wait for establishing a connection to the Salesforce streaming API
     decimal connectionTimeout?;
     # The maximum time in seconds to wait for the long polling transport before considering a request failed
@@ -895,7 +959,7 @@
     CredentialsConfig auth;
     # The type of salesforce environment, if sandbox environment or not
     boolean isSandBox?;
-    int|ballerinax/salesforce:8.7.0:ReplayOptions replayFrom?;
+    int|ReplayOptions replayFrom?;
     decimal connectionTimeout?;
     decimal readTimeout?;
     decimal keepAliveInterval?;
@@ -936,7 +1000,7 @@
 
 See `salesforce:ListenerCoordinationConfig` for field-level documentation.
     ListenerCoordinationConfig coordination?;
-    int|ballerinax/salesforce:8.7.0:ReplayOptions replayFrom?;
+    int|ReplayOptions replayFrom?;
     decimal connectionTimeout?;
     decimal readTimeout?;
     decimal keepAliveInterval?;
@@ -946,7 +1010,7 @@
 };
 
 # OAuth2 authentication configuration type.
-type OAuth2Config ballerina/http:2.16.6:BearerTokenConfig|ballerina/oauth2:2.15.0:PasswordGrantConfig|ballerina/oauth2:2.15.0:RefreshTokenGrantConfig|ballerina/oauth2:2.15.0:ClientCredentialsGrantConfig;
+type OAuth2Config http:BearerTokenConfig|oauth2:PasswordGrantConfig|oauth2:RefreshTokenGrantConfig|oauth2:ClientCredentialsGrantConfig;
 
 # Pluggable token store interface for coordinating token lifecycle across
 # multiple replicas (e.g., in Kubernetes). Implementations must be `isolated`.
@@ -958,6 +1022,33 @@
 # store (e.g., Redis) with advisory locking to prevent Token Replay Attacks caused
 # by concurrent refresh-token usage across pods.
 class TokenStore {
+
+    # Attempts to acquire an advisory lock for token refresh coordination.
+    # Only one replica should refresh at a time to prevent Token Replay Attacks.
+    # 
+    function acquireLock(string lockKey, int ttlSeconds) returns boolean|error;
+
+    # Releases the advisory lock after a refresh cycle completes.
+    # 
+    function releaseLock(string lockKey) returns error?;
+
+    # Reads the current token data from the shared store.
+    # 
+    function getTokenData(string key) returns TokenData|()|error;
+
+    # Writes updated token data to the shared store after a successful refresh.
+    # 
+    function setTokenData(string key, TokenData data) returns error?;
+
+    # Removes token data and its associated lock from the shared store.
+    # Called when the token family is permanently invalidated (e.g., Salesforce
+    # returns `invalid_grant` after absolute session timeout expiry).
+    # 
+    # This prevents "cache poisoning" — without eviction, a restarting replica
+    # would read the dead token from the store, ignore the fresh seed token
+    # from its configuration, and crash in a loop.
+    # 
+    function clearTokenData(string key) returns error?;
 }
 
 # Active-Standby coordination settings for a Salesforce listener.
@@ -986,7 +1077,7 @@
 };
 
 # Salesforce listener configuration type.
-type ListenerConfig ballerinax/salesforce:8.7.0:SoapBasedListenerConfig|ballerinax/salesforce:8.7.0:RestBasedListenerConfig;
+type ListenerConfig SoapBasedListenerConfig|RestBasedListenerConfig;
 
 # Contains data returned from a Change Data Event.
 
@@ -1040,20 +1131,41 @@
     string? message?;
 };
 
-// Unknown type: Error
+# Salesforce connector error.
+type Error error<ErrorDetails>;
 
 # Triggers when a new Change Data Capture event is received from Salesforce channels.
 # Available actions: onCreate, onUpdate, onDelete, and onRestore
 class CdcService {
+
+    # Triggers on a new record create event.
+    # 
+    remote function onCreate(EventData payload) returns error?;
+
+    # Triggers on a record update event.
+    # 
+    remote function onUpdate(EventData payload) returns error?;
+
+    # Triggers on a record delete event.
+    # 
+    remote function onDelete(EventData payload) returns error?;
+
+    # Triggers on a record restore event.
+    # 
+    remote function onRestore(EventData payload) returns error?;
 }
 
 # Triggers when a new Platform Event is received from Salesforce channels.
 # Available action: onMessage
 class PlatformEventsService {
+
+    # Triggers when a Platform Event is published on the subscribed channel.
+    # 
+    remote function onMessage(PlatformEventsMessage message) returns error?;
 }
 
 # This includes the service types for both Change Data Capture and Platform Events.
-type Service ballerinax/salesforce:8.7.0:CdcService|ballerinax/salesforce:8.7.0:PlatformEventsService;
+type Service CdcService|PlatformEventsService;
 
 # Defines the Attribute type.
 # Contains the attribute information of the resultant record.
@@ -1485,7 +1597,7 @@
     string columnDelimiter?;
     string id;
     string operation;
-    string object;
+    string 'object;
     string createdById;
     string createdDate;
     string systemModstamp;
@@ -1513,7 +1625,7 @@
     string columnDelimiter?;
     string id;
     string operation;
-    string object;
+    string 'object;
     string createdById;
     string createdDate;
     string systemModstamp;
@@ -1534,12 +1646,116 @@
     string nextRecordsUrl;
 };
 
-// Unknown type: InMemoryCoordinator
-
-// Unknown type: Listener
+# Default in-process coordinator. Suitable for single-replica deployments and
+# for unit tests where a distributed coordinator is not available.
+# 
+# All shared state is guarded by `lock` blocks, so it is safe to use from
+# concurrent strands. Liveness checks use `livenessInterval` against the
+# wall-clock millisecond delta — this is consistent with the cross-replica
+# semantics, even though contention is not realistic in a single process.
+class InMemoryCoordinator {
 
-// Unknown type: InMemoryTokenStore
+    function attemptLeadership(string groupId, string nodeId, decimal livenessInterval) returns boolean|error;
 
+    function renewLeadership(string groupId, string nodeId) returns error?;
+
+    function saveCheckpoint(string channel, int replayId) returns error?;
+
+    function getCheckpoint(string channel) returns int|error?;
+
+    function relinquishLeadership(string groupId, string nodeId) returns error?;
+}
+
+# Initializes the listener. During initialization you can set the credentials.
+# Create a Salesforce account and obtain tokens following [this guide](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm).
+# 
+@display {label: "Salesforce", iconPath: "icon.png"}
+class Listener {
+    function init(ListenerConfig listenerConfig) returns error?;
+
+    # Attaches the service to the `salesforce:Listener` endpoint.
+    # 
+    # **Breaking change (coordination):** For OAuth2 listeners, each `Listener` instance is bound to
+    # exactly one channel. Attaching a second, different channel returns an error — create a separate
+    # `salesforce:Listener` instance for each channel you need to subscribe to. SOAP listeners are
+    # unaffected and may still attach multiple services on different channels.
+    # 
+    function attach(Service s, string[]|string|() name) returns error?;
+
+    # Starts the subscription and listens to events on all attached services.
+    # 
+    # For OAuth2 (REST-based) listeners this forks the Active-Standby leadership
+    # loop and **always returns `()`** — CometD connection errors are handled
+    # asynchronously inside the loop and surfaced only in log output. Callers
+    # must not assume a successful return means the CometD connection is open;
+    # the connection is established once the leadership loop acquires the lease.
+    # Standby replicas idle in the loop until the leader's lease expires.
+    # 
+    # SOAP-based listeners retain the original direct-start behaviour: the
+    # connection is opened synchronously and any error (e.g. `INVALID_LOGIN`)
+    # is returned to the caller.
+    # 
+    function 'start() returns error?;
+
+    # Stops subscription and detaches the service from the `salesforce:Listener` endpoint.
+    # 
+    function detach(Service s) returns error?;
+
+    # Stops subscription through all consumer services by terminating the CometD
+    # connection. This is a permanent shutdown — call `reconnect()` to re-establish.
+    # 
+    # For standby replicas, this is a no-op on the CometD layer (they hold no
+    # subscription), but the leadership loop is stopped regardless.
+    # 
+    function gracefulStop() returns error?;
+
+    # Re-establishes the CometD connection. Safe to call after `gracefulStop()`
+    # or after a connection drop. Only supported for OAuth2 listeners.
+    # 
+    function reconnect() returns error?;
+
+    # Updates the in-memory refresh token used by the listener.
+    # This is useful after an authorization-code exchange returns a new refresh token.
+    # 
+    function updateRefreshToken(string newRefreshToken) returns error?;
+
+    # Returns the current in-memory refresh token held by the TokenManager.
+    # Use this to read the latest rotated token and persist it to durable storage
+    # so a process restart loads the newest token rather than the original seed.
+    # 
+    function getRefreshToken() returns string|error;
+
+    # Stops subscriptions through all the consumer services and terminates the connection with the server.
+    # 
+    function immediateStop() returns error?;
+
+    # Called by the Java dispatcher (`DispatcherService`) after the user's
+    # `onEvent`/`onCreate`/`onUpdate` etc. handler returns successfully.
+    # Persists the latest replayId so a future leader can resume without
+    # re-delivering already-handled events.
+    # 
+    # This method is intentionally `public` so the Java layer can invoke it
+    # via `runtime.callMethod(listener, "recordEventDispatched", channel, replayId)`.
+    # 
+    function recordEventDispatched(string channel, int replayId) returns ();
+}
+
+# Default in-memory token store for single-replica deployments.
+# `acquireLock()` always succeeds (no contention in a single process).
+# Token data is stored in-process memory — not shared across replicas.
+class InMemoryTokenStore {
+
+    function acquireLock(string lockKey, int ttlSeconds) returns boolean|error;
+
+    function releaseLock(string lockKey) returns error?;
+
+    function getTokenData(string key) returns TokenData|()|error;
+
+    function setTokenData(string key, TokenData data) returns error?;
+
+    function clearTokenData(string key) returns error?;
+}
+
 // --- Client ---
 
 # Ballerina Salesforce connector provides the capability to access Salesforce REST API.
@@ -1575,7 +1791,7 @@
 
     # Lists the Limits information for your organization.
     # 
-    remote function getLimits() returns Limit>|error;
+    remote function getLimits() returns map<Limit>|error;
 
     # Gets an object record by ID.
     # 
@@ -1695,7 +1911,7 @@
     # Creates a bulkv2 query job and provide future value.
     # 
     @deprecated
-    remote function createQueryJobAndWait(BulkCreatePayload payload) returns BulkJobInfo|error>|error;
+    remote function createQueryJobAndWait(BulkCreatePayload payload) returns future<BulkJobInfo|error>|error;
 
     # Retrieves detailed information about a job.
     # 
@@ -1740,7 +1956,7 @@
     # Notifies Salesforce servers that the upload of job data is complete.
     # 
     @deprecated
-    remote function closeIngestJobAndWait(string bulkJobId) returns BulkJobInfo|error>;
+    remote function closeIngestJobAndWait(string bulkJobId) returns error|future<BulkJobInfo|error>;
 
     # Notifies Salesforce servers that the upload of job data is complete.
     # 
@@ -1750,20 +1966,20 @@
 
 // --- Service ---
 
-service salesforce:Service on new salesforce:Listener(ListenerConfig listenerConfig = {auth: {username: "", password: ""}}) {
+service salesforce:Service on new salesforce:Listener(salesforce:ListenerConfig listenerConfig = {auth: {username: "", password: ""}}) {
     # Triggers on a new record create event.
+    # + payload - The information about the triggered event
+    remote function onCreate(salesforce:EventData payload) returns error?;
 
-    remote function onCreate(EventData payload) returns error?;
-
     # Triggers on a record update event.
+    # + payload - The information about the triggered event
+    remote function onUpdate(salesforce:EventData payload) returns error?;
 
-    remote function onUpdate(EventData payload) returns error?;
-
     # Triggers on a record delete event.
+    # + payload - The information about the triggered event
+    remote function onDelete(salesforce:EventData payload) returns error?;
 
-    remote function onDelete(EventData payload) returns error?;
-
     # Triggers on a record restore event.
-
-    remote function onRestore(EventData payload) returns error?;
+    # + payload - The information about the triggered event
+    remote function onRestore(salesforce:EventData payload) returns error?;
 }
`````

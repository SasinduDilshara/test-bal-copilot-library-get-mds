# messaging — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `messaging` |
| **Old file** | `messaging/old/ballerina_messaging.bal.txt` |
| **New file** | `messaging/new/ballerina_messaging.bal.txt` |
| **Old lines** | 219 |
| **New lines** | 264 |
| **Lines added** | 48 |
| **Lines removed** | 3 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (13)

- `class StoreListener`
- `client class Store`
- `function 'start`
- `function acknowledge`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function init`
- `function onMessage`
- `function retrieve`
- `function store`
- `type Error`

### Declarations removed (1)

- `class Store`

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 169–175 | 169–176 | Types | +2 | −1 |
| 2 | 190–204 | 191–249 | Types | +46 | −2 |

---

## Unified diff

`````diff
--- messaging/old/ballerina_messaging.bal.txt	2026-08-12 23:21:51
+++ messaging/new/ballerina_messaging.bal.txt	2026-08-12 23:23:51
@@ -169,7 +169,8 @@
     anydata payload;
 };
 
-// Unknown type: Error
+# Represents the default error type.
+type Error error;
 
 # Represents the message store listener configuration,
 
@@ -190,15 +191,59 @@
 };
 
 # Represents a message store interface for storing and retrieving messages.
-class Store {
+client class Store {
+
+    # Stores a message in the message store.
+    # 
+    remote function store(anydata payload) returns error?;
+
+    # Retrieves the top message from the message store without removing it.
+    # 
+    remote function retrieve() returns Message|error|();
+
+    # Acknowledges the top message retrieved from the message store.
+    # 
+    remote function acknowledge(string id, boolean success = true) returns error?;
 }
 
 # This service object defines the contract for processing messages from a message store.
 class StoreService {
+
+    # This function is called when a new message is received from the message store.
+    # 
+    remote function onMessage(anydata payload) returns error?;
 }
 
-// Unknown type: StoreListener
+# Initializes a new instance of Message Store Listener.
+# 
+class StoreListener {
+    function init(Store messageStore, decimal pollingInterval = 1, int maxRetries = 3, decimal retryInterval = 1, boolean ackWithFailureAfterMaxRetries = true, Store deadLetterStore = object {}, StoreListenerConfiguration config) returns Error?;
 
+    # Attaches a message store service to the listener. Only one service can be attached to this 
+    # listener.
+    # 
+    function attach(StoreService msgStoreService, () path = ()) returns Error|();
+
+    # Detaches the message store service from the listener.
+    # 
+    function detach(StoreService msgStoreService) returns Error|();
+
+    # Starts the message store listener to poll and process messages.
+    # 
+    function 'start() returns Error|();
+
+    # Gracefully stops the message store listener by waiting for any ongoing processing to 
+    # complete before stopping. This is not implemented yet, and currently this will call 
+    # immediateStop.
+    # 
+    function gracefulStop() returns Error|();
+
+    # Immediately stops the message store listener without waiting for any ongoing processing 
+    # to complete.
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Represents an in-memory message store.
`````

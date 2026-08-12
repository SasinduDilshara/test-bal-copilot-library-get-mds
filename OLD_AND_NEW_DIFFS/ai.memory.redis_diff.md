# ai.memory.redis — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.memory.redis` |
| **Old file** | `ai.memory.redis/old/ballerinax_ai.memory.redis.bal.txt` |
| **New file** | `ai.memory.redis/new/ballerinax_ai.memory.redis.bal.txt` |
| **Old lines** | 85 |
| **New lines** | 149 |
| **Lines added** | 66 |
| **Lines removed** | 2 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 3 | 3 |

### Declarations added (16)

- `class ShortTermMemoryStore`
- `function getAll`
- `function getCapacity`
- `function getChatInteractiveMessages`
- `function getChatSystemMessage`
- `function getCheckpoint`
- `function init`
- `function isFull`
- `function put`
- `function putCheckpoint`
- `function removeAll`
- `function removeChatInteractiveMessages`
- `function removeChatSystemMessage`
- `function removeCheckpoint`
- `function takeCheckpoint`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 80–85 | 80–149 | END README | +66 | −2 |

---

## Unified diff

`````diff
--- ai.memory.redis/old/ballerinax_ai.memory.redis.bal.txt	2026-08-12 12:57:29
+++ ai.memory.redis/new/ballerinax_ai.memory.redis.bal.txt	2026-08-12 13:19:19
@@ -80,6 +80,70 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents a distinct error type for memory store errors.
+type Error error;
 
-// Unknown type: ShortTermMemoryStore
+# Initializes the Redis-backed short-term memory store.
+# 
+@display {label: "Redis Short Term Memory Store"}
+class ShortTermMemoryStore {
+    function init(redis:Client|redis:ConnectionConfig redisClient, int maxMessagesPerKey = 20, cache:CacheConfig|() cacheConfig = (), string keyPrefix = "chat_memory") returns Error?; // Special Agent Note: Client, ConnectionConfig FROM ballerinax/redis package, CacheConfig FROM ballerina/cache package
+
+    # Retrieves the system message, if it was provided, for a given key.
+    # 
+    function getChatSystemMessage(string key) returns ai:ChatSystemMessage|Error|(); // Special Agent Note: ChatSystemMessage FROM ballerina/ai package
+
+    # Retrieves all stored interactive chat messages (i.e., all chat messages except the system
+    # message) for a given key.
+    # 
+    function getChatInteractiveMessages(string key) returns ai:ChatInteractiveMessage[]|Error; // Special Agent Note: ChatInteractiveMessage FROM ballerina/ai package
+
+    # Retrieves all stored chat messages for a given key.
+    # 
+    function getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|ai:ChatInteractiveMessage[]|Error; // Special Agent Note: ChatInteractiveMessage FROM ballerina/ai package
+
+    # Adds one or more chat messages to the memory store for a given key.
+    # 
+    function put(string key, ai:ChatUserMessage|ai:ChatSystemMessage|ai:ChatAssistantMessage|ai:ChatFunctionMessage|ai:ChatMessage[] message) returns Error|(); // Special Agent Note: ChatUserMessage, ChatSystemMessage, ChatAssistantMessage, ChatFunctionMessage, ChatMessage FROM ballerina/ai package
+
+    # Removes the system chat message, if specified, for a given key.
+    # 
+    function removeChatSystemMessage(string key) returns Error|();
+
+    # Removes all stored interactive chat messages (i.e., all chat messages except the system
+    # message) for a given key.
+    # 
+    function removeChatInteractiveMessages(string key, int|() count = ()) returns Error|();
+
+    # Removes all stored chat messages for a given key, including any pending human-in-the-loop
+    # approval checkpoint for that key, so clearing a session is atomic and an abandoned pause
+    # does not retain its whole history snapshot indefinitely.
+    # 
+    function removeAll(string key) returns Error|();
+
+    # Checks if the memory store is full for a given key.
+    # 
+    function isFull(string key) returns boolean|Error;
+
+    # Retrieves the maximum number of interactive messages that can be stored for each key.
+    # 
+    function getCapacity() returns int;
+
+    # Stores (or replaces) the pending human-in-the-loop approval for its session.
+    # 
+    function putCheckpoint(ai:PendingApproval approval) returns Error|(); // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Returns the pending human-in-the-loop approval for a session, if any.
+    # 
+    function getCheckpoint(string sessionId) returns ai:PendingApproval|Error|(); // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
+
+    # Fetches and removes pending human-in-the-loop approval checkpoint for a session.
+    # Note: This operation is non-atomic (separate GET and DEL calls).
+    # Concurrent calls may both retrieve the same approval.
+    # 
+    function takeCheckpoint(string sessionId) returns ai:PendingApproval|Error|(); // Special Agent Note: PendingApproval FROM ballerina/ai package
+}
`````

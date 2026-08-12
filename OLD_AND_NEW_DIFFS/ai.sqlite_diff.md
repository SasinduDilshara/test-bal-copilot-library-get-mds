# ai.sqlite — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.sqlite` |
| **Old file** | `ai.sqlite/old/ballerinax_ai.sqlite.bal.txt` |
| **New file** | `ai.sqlite/new/ballerinax_ai.sqlite.bal.txt` |
| **Old lines** | 162 |
| **New lines** | 234 |
| **Lines added** | 74 |
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
| 1 | 123–162 | 123–234 | END README | +74 | −2 |

---

## Unified diff

`````diff
--- ai.sqlite/old/ballerinax_ai.sqlite.bal.txt	2026-08-12 12:57:29
+++ ai.sqlite/new/ballerinax_ai.sqlite.bal.txt	2026-08-12 13:19:19
@@ -123,40 +123,112 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents a distinct error type for memory store errors.
+type Error error;
 
 # Database configuration for the SQLite-backed memory store.
 
+@display {label: "Database Configuration"}
 type DatabaseConfiguration record {
     # JDBC URL for the SQLite database: `jdbc:sqlite:<path>` for a file-backed database
 (e.g., `jdbc:sqlite:./chat.db`) or `jdbc:sqlite::memory:` for an in-process one.
 Must start with `jdbc:sqlite:`.
+    @display {label: "URL"}
     string url;
     # SQLite session-level options applied to every connection the store opens.
+    @display {label: "Options"}
     Options options?;
     # Seconds to wait for a connection from the pool before failing.
+    @display {label: "Connection Timeout"}
     decimal connectionTimeout?;
 };
 
 # SQLite session-level options, applied as `sqlite-jdbc` driver properties to every
 # connection the store opens. Any field left unset falls back to the driver's default.
 
+@display {label: "Options"}
 type Options record {
     # Journaling mode (`PRAGMA journal_mode`). When unset, the database is left at its own
 setting, which is `DELETE` for a newly created file-backed database. `WAL` is recorded
 in the database file itself and so persists for every later connection, whereas the
 other modes apply per connection. This option has no effect on a `jdbc:sqlite::memory:`
 database, whose journal mode is always `MEMORY`.
+    @display {label: "Journal Mode"}
     JournalMode journalMode?;
     # Milliseconds SQLite waits for a lock held by another connection before failing with
 `SQLITE_BUSY` (`PRAGMA busy_timeout`). When unset, the `sqlite-jdbc` driver's default of
 `3000` applies, which is not the same as SQLite's own default of `0`; set `0` explicitly
 to fail immediately. Because the store pins its pool to a single connection, this only
 affects contention with other connections or processes using the same database file.
+    @display {label: "Busy Timeout"}
     int busyTimeout?;
 };
 
 # SQLite journaling mode (`PRAGMA journal_mode`).
+@display {label: "Journal Mode"}
 type JournalMode "DELETE"|"TRUNCATE"|"PERSIST"|"MEMORY"|"WAL"|"OFF";
 
-// Unknown type: ShortTermMemoryStore
+# Initializes the SQLite-backed short-term memory store.
+# 
+@display {label: "SQLite Short Term Memory Store"}
+class ShortTermMemoryStore {
+    function init(@display {label: "Database Connection"} DatabaseConfiguration|jdbc:Client dbConnection, @display {label: "Maximum Messages Per Key"} int maxMessagesPerKey = 20, @display {label: "Table Name"} string tableName = "chat_messages", @display {label: "Checkpoint Table Name"} string checkpointTableName = "checkpoints") returns Error?; // Special Agent Note: Client FROM ballerinax/java.jdbc package
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
+    # approval checkpoint for that key, so clearing a session is atomic and an abandoned pause does
+    # not retain its whole history snapshot indefinitely.
+    # 
+    function removeAll(string key) returns Error|();
+
+    # Checks if the memory store is full for a given key.
+    # 
+    function isFull(string key) returns boolean|Error;
+
+    # Stores (or replaces) the pending human-in-the-loop approval for its session.
+    # 
+    function putCheckpoint(ai:PendingApproval approval) returns Error|(); // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Returns the pending human-in-the-loop approval for a session, if any.
+    # 
+    function getCheckpoint(string sessionId) returns ai:PendingApproval|()|Error; // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
+
+    # Fetches and removes the pending human-in-the-loop approval for a session. The delete-and-return
+    # runs as a single statement so a concurrent duplicate resume for the same session cannot also
+    # claim and execute the same approved tool call.
+    # 
+    function takeCheckpoint(string sessionId) returns ai:PendingApproval|()|Error; // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Retrieves the maximum number of interactive messages that can be stored for each key.
+    # 
+    function getCapacity() returns int;
+}
`````

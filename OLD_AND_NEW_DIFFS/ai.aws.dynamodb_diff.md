# ai.aws.dynamodb — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.aws.dynamodb` |
| **Old file** | `ai.aws.dynamodb/old/ballerinax_ai.aws.dynamodb.bal.txt` |
| **New file** | `ai.aws.dynamodb/new/ballerinax_ai.aws.dynamodb.bal.txt` |
| **Old lines** | 143 |
| **New lines** | 225 |
| **Lines added** | 84 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

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
| 1 | 101–114 | 101–117 | END README | +4 | −1 |
| 2 | 116–143 | 119–225 | Types | +80 | −1 |

---

## Unified diff

`````diff
--- ai.aws.dynamodb/old/ballerinax_ai.aws.dynamodb.bal.txt	2026-08-12 12:57:29
+++ ai.aws.dynamodb/new/ballerinax_ai.aws.dynamodb.bal.txt	2026-08-12 13:19:19
@@ -101,14 +101,17 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents a distinct error type for memory store errors.
+type Error error;
 
 # Configuration for the DynamoDB table that backs the short-term memory store.
 # 
 
+@display {label: "Table Configuration"}
 type TableConfig record {
     # The name of the DynamoDB table used to store chat messages.
 Must be 3-255 characters long and contain only letters, digits, underscores, dots, and hyphens
+    @display {label: "Table Name"}
     string tableName?;
     # Whether the store should create the backing table when it does not
 already exist. Defaults to `true`. When `true`, initialization calls `DescribeTable` (and
@@ -116,28 +119,107 @@
 `dynamodb:CreateTable` IAM permissions. Set to `false` when the table is provisioned out of band
 (e.g. via IaC) and the runtime role is restricted to data-plane permissions; in that case the
 store performs no control-plane calls during initialization and assumes the table already exists
+    @display {label: "Create Table If Not Exists"}
     boolean createTableIfNotExists?;
     # The billing mode to request when the connector creates the table. Defaults to
 `dynamodb:PAY_PER_REQUEST` (on-demand). Note that this differs from the AWS `CreateTable` API
 default of `PROVISIONED`; set this explicitly to `dynamodb:PROVISIONED` (and provide
 `readCapacityUnits`/`writeCapacityUnits`) for provisioned-capacity tables. Ignored when
 `createTableIfNotExists` is `false` or the table already exists
+    @display {label: "Billing Mode"}
     dynamodb:BillingMode billingMode?; // Special Agent Note: BillingMode FROM ballerinax/aws.dynamodb package
     # The read capacity units to provision when `billingMode` is `dynamodb:PROVISIONED`
+    @display {label: "Read Capacity Units"}
     int readCapacityUnits?;
     # The write capacity units to provision when `billingMode` is `dynamodb:PROVISIONED`
+    @display {label: "Write Capacity Units"}
     int writeCapacityUnits?;
     # Whether reads against DynamoDB use strongly consistent reads. Defaults to `false`
 (eventually consistent), matching the DynamoDB default. Strongly consistent reads cost twice the read
 capacity units of eventually consistent reads; set to `true` only when strong consistency is required
+    @display {label: "Consistent Reads"}
     boolean consistentReads?;
     # Optional tags to apply to the DynamoDB table when the connector creates it. Ignored if the
 table already exists
+    @display {label: "Tags"}
     dynamodb:Tag[]|() tags?; // Special Agent Note: Tag FROM ballerinax/aws.dynamodb package
     # Optional server-side encryption settings to apply when the connector creates
 the table. If omitted, the table uses the default AWS-owned encryption key. Ignored if the table
 already exists
+    @display {label: "Server-Side Encryption"}
     dynamodb:SSESpecification|() sseSpecification?; // Special Agent Note: SSESpecification FROM ballerinax/aws.dynamodb package
 };
 
-// Unknown type: ShortTermMemoryStore
+# Initializes the DynamoDB-backed short-term memory store.
+# 
+@display {label: "Amazon DynamoDB Short Term Memory Store"}
+class ShortTermMemoryStore {
+    function init(@display {label: "Database Connection"} dynamodb:ConnectionConfig|dynamodb:Client dbConnection, @display {label: "Max Messages Per Key"} int maxMessagesPerKey = 20, @display {label: "Table Configuration"} TableConfig tableConfig = {}) returns Error?; // Special Agent Note: ConnectionConfig, Client FROM ballerinax/aws.dynamodb package
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
+    # approval checkpoint for that key, so an abandoned pause does not retain its whole history
+    # snapshot indefinitely. The message deletion and the checkpoint deletion are separate
+    # DynamoDB calls and are not atomic; if the second call fails, the error is returned and the
+    # checkpoint is left in place for a retry.
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
+    # Uses `consistentReads` (defaults to `false`, eventually consistent). A `getCheckpoint` call
+    # made shortly after `putCheckpoint` can therefore return `()` even though a checkpoint was
+    # just stored. Set `consistentReads` to `true` if callers need read-after-write for this. Note
+    # `takeCheckpoint` is unaffected - `DeleteItem` (with `ReturnValues`) is always strongly
+    # consistent, regardless of `consistentReads`.
+    # 
+    function getCheckpoint(string sessionId) returns ai:PendingApproval|()|Error; // Special Agent Note: PendingApproval FROM ballerina/ai package
+
+    # Removes the pending human-in-the-loop approval for a session, if any.
+    # 
+    function removeCheckpoint(string sessionId) returns Error|();
+
+    # Fetches and removes the pending human-in-the-loop approval for a session. Uses DynamoDB's
+    # `ReturnValues: ALL_OLD` on the delete so the fetch-and-remove happens as a single atomic
+    # operation - a concurrent duplicate resume for the same session cannot also claim and execute
+    # the same approved tool call.
+    # 
+    function takeCheckpoint(string sessionId) returns ai:PendingApproval|()|Error; // Special Agent Note: PendingApproval FROM ballerina/ai package
+}
`````

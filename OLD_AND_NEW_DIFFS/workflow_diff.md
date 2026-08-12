# workflow — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `workflow` |
| **Old file** | `workflow/old/ballerina_workflow.bal.txt` |
| **New file** | `workflow/new/ballerina_workflow.bal.txt` |
| **Old lines** | 638 |
| **New lines** | 714 |
| **Lines added** | 85 |
| **Lines removed** | 9 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 5 | 6 |

### Declarations added (13)

- `annotation on`
- `class DurableAgent`
- `function bindAgentName`
- `function getDataResult`
- `function getResult`
- `function init`
- `function run`
- `function sendData`
- `function waitForDataResult`
- `function waitForResult`
- `type AgentBusyError`
- `type HumanTaskTimeoutError`
- `type WorkflowBusyError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 318–324 | 318–370 | Types | +47 | −1 |
| 2 | 360–366 | 406–416 | Types | +5 | −1 |
| 3 | 405–411 | 455–463 | Types | +3 | −1 |
| 4 | 420–426 | 472–482 | Types | +5 | −1 |
| 5 | 447–453 | 503–509 | Client | +1 | −1 |
| 6 | 455–473 | 511–529 | Client | +4 | −4 |
| 7 | 636–638 | 692–714 | Functions | +20 | −0 |

---

## Unified diff

`````diff
--- workflow/old/ballerina_workflow.bal.txt	2026-08-12 23:21:51
+++ workflow/new/ballerina_workflow.bal.txt	2026-08-12 23:23:51
@@ -318,7 +318,53 @@
     string|string[] userRoles?;
 };
 
-// Unknown type: DurableAgent
+# Declares the agent. Capabilities are fixed here and registered with the
+# workflow runtime at module init by the compiler plugin.
+# 
+class DurableAgent {
+    function init(ai:SystemPrompt systemPrompt = {role: "", instructions: ""}, ai:ModelProvider model = object {}, anydata|() inputType = string, anydata|() resultType = (), ActivityDecl|function[] activities = [], ToolDecl|ai:ToolConfig|ai:BaseToolKit|function[] tools = [], EventDecl[] events = [], HumanTaskDecl[] humanTasks = [], PeerDecl[] peers = [], int maxIter = 16, DurableAgentConfig config) returns error?; // Special Agent Note: SystemPrompt, ModelProvider, ToolConfig, BaseToolKit FROM ballerina/ai package
+
+    # Binds the agent's stable identity — its module-level variable name — to this
+    # object. Called by the compiler-plugin-generated module-init code; not part of
+    # the public API surface. The first binding wins; later calls are ignored.
+    # 
+    function bindAgentName(string agentName) returns ();
+
+    # Starts the agent durably and returns the new instance ID — always the ID,
+    # never the result (a durable agent may suspend for days on a human task, so
+    # no caller thread is blocked). Outside a workflow this is a top-level start;
+    # inside a `@workflow:Workflow` the agent runs as a Temporal child workflow.
+    # 
+    function run(string query, anydata input = {}) returns string|error;
+
+    # Sends an event to a running instance on a declared channel and returns a
+    # correlation token for reading that turn's response.
+    # 
+    function sendData(string instanceId, string eventName, anydata data) returns string|error;
+
+    # Returns the final result of an instance if it has finished, without waiting.
+    # While the instance is still working (e.g. suspended on a human task) a
+    # `workflow:AgentBusyError` is returned — check back later, or use `waitForResult`.
+    # 
+    function getResult(string instanceId, anydata T = anydata) returns T|error;
+
+    # Returns the response for a specific `sendData` turn if it is ready, without
+    # waiting. While the turn is unanswered a `workflow:AgentBusyError` is returned.
+    # 
+    function getDataResult(string instanceId, string token, anydata T = anydata) returns T|error;
+
+    # Waits until the instance finishes and returns its result. Inside a workflow
+    # this durably suspends the caller (no thread held); from a service it blocks
+    # but is resumable — if the caller crashes, calling again after restart resumes
+    # the wait, because the result lives in history.
+    # 
+    function waitForResult(string instanceId, anydata T = anydata) returns T|error;
+
+    # Waits for a specific `sendData` turn's response (same durability guarantees
+    # as `waitForResult`).
+    # 
+    function waitForDataResult(string instanceId, string token, anydata T = anydata) returns T|error;
+}
 
 # The complete, self-declarative configuration of a durable agent. Capability
 # kinds are separate fields so each renders as its own edge type in the diagram.
@@ -360,7 +406,11 @@
     int maxIter?;
 };
 
-// Unknown type: AgentBusyError
+# Returned by the non-blocking `getResult`/`getDataResult` reads when the agent
+# instance (or the specific turn) is still in progress — e.g. suspended on a human
+# task. Check back later, or use the blocking `waitForResult`/`waitForDataResult`
+# forms, which durably wait and are resumable across crashes.
+type AgentBusyError error;
 
 # Deployment mode for the workflow runtime.
 # 
@@ -405,7 +455,9 @@
     string timedOutAt;
 };
 
-// Unknown type: HumanTaskTimeoutError
+# Returned by `awaitHumanTask` when no human acts within the configured deadline.
+# Catch with `on fail workflow:HumanTaskTimeoutError e` to run compensation logic.
+type HumanTaskTimeoutError error<HumanTaskTimeoutDetail>;
 
 # A data-event turn a durable agent has accepted but not yet answered. Returned
 # by `getPendingAgentEvents` so callers can rediscover in-flight event turns
@@ -420,7 +472,11 @@
     string eventName;
 };
 
-// Unknown type: WorkflowBusyError
+# Returned by the non-blocking `ctx->getChildWorkflowResult` read when the child
+# workflow is still running (e.g. suspended on a human task). Check back later, or
+# use the blocking `ctx->waitForChildWorkflow` form, which durably suspends until
+# the child completes.
+type WorkflowBusyError error;
 
 // --- Client ---
 
@@ -447,7 +503,7 @@
     # check ctx.sleep({seconds: 30});
     # ```
     # 
-    remote function sleep(Duration duration) returns error?;
+    function sleep(Duration duration) returns error?;
 
     # Returns the deterministic workflow time. Use instead of `time:utcNow()` inside workflows.
     # 
@@ -455,19 +511,19 @@
     # time:Utc now = ctx.currentTime();
     # ```
     # 
-    remote function currentTime() returns time:Utc; // Special Agent Note: Utc FROM ballerina/time package
+    function currentTime() returns time:Utc; // Special Agent Note: Utc FROM ballerina/time package
 
     # Checks whether the workflow is recovering from a failure (re-executing recorded history).
     # 
-    remote function isReplaying() returns boolean;
+    function isReplaying() returns boolean;
 
     # Get the unique workflow ID.
     # 
-    remote function getWorkflowId() returns string|error;
+    function getWorkflowId() returns string|error;
 
     # Get the workflow type name.
     # 
-    remote function getWorkflowType() returns string|error;
+    function getWorkflowType() returns string|error;
 
     # Waits for at least `minCount` data futures to complete. Results are a positional tuple
     # aligned to input order. Use nullable types (`T?`) for partial waits.
@@ -636,3 +692,23 @@
 # + userId - The user ID of the person completing the task (used for auditing)
 # + return - An error if the task cannot be found, is already completed, or the caller is unauthorized
 function completeHumanTask(string taskWorkflowId, anydata result, [string, string...]|() callerRoles = (), string|() userId = ()) returns error?;
+
+// --- Annotations ---
+
+# Marks a function as a workflow.
+# 
+# ```ballerina
+# @workflow:Workflow
+# function orderProcess(Order input) returns OrderResult|error {
+# }
+# ```
+public annotation Workflow on function;
+
+# Marks a function as a workflow activity.
+# 
+# ```ballerina
+# @workflow:Activity
+# function sendEmail(EmailRequest req) returns EmailResponse|error {
+# }
+# ```
+public annotation Activity on function;
`````

# hubspot.crm.extensions.timelines — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.extensions.timelines` |
| **Old file** | `hubspot.crm.extensions.timelines/old/ballerinax_hubspot.crm.extensions.timelines.bal.txt` |
| **New file** | `hubspot.crm.extensions.timelines/new/ballerinax_hubspot.crm.extensions.timelines.bal.txt` |
| **Old lines** | 604 |
| **New lines** | 605 |
| **Lines added** | 5 |
| **Lines removed** | 4 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 225–235 | 225–235 | Types | +2 | −2 |
| 2 | 481–486 | 481–487 | Types | +1 | −0 |
| 3 | 529–535 | 530–536 | Types | +1 | −1 |
| 4 | 576–582 | 577–583 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.extensions.timelines/old/ballerinax_hubspot.crm.extensions.timelines.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.extensions.timelines/new/ballerinax_hubspot.crm.extensions.timelines.bal.txt	2026-08-12 13:19:19
@@ -225,11 +225,11 @@
     # The label of the modal window that displays the iframe contents
     string headerLabel;
     # The width of the modal window in pixels
-    ballerina/lang.int:0.0.0:Signed32 width;
+    int:Signed32 width;
     # The URI of the iframe contents
     string url;
     # The height of the modal window in pixels
-    ballerina/lang.int:0.0.0:Signed32 height;
+    int:Signed32 height;
 };
 
 # The state of the timeline event
@@ -481,6 +481,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -529,7 +530,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing
@@ -576,7 +577,7 @@
 
     # Renders the header or detail as HTML
     # 
-    resource function get events/[string eventTemplateId]/[string eventId]/render(map<string|string[]> headers = {}, boolean detail = false, anydata Additional Values, GetEventsEventTemplateIdEventIdRenderGetRenderByIdQueries queries) returns string|error;
+    resource function get events/[string eventTemplateId]/[string eventId]/render(map<string|string[]> headers = {}, boolean detail = false, GetEventsEventTemplateIdEventIdRenderGetRenderByIdQueries queries) returns string|error;
 
     # List all event templates for your app
     # 
`````

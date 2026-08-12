# hubspot.crm.pipelines — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.pipelines` |
| **Old file** | `hubspot.crm.pipelines/old/ballerinax_hubspot.crm.pipelines.bal.txt` |
| **New file** | `hubspot.crm.pipelines/new/ballerinax_hubspot.crm.pipelines.bal.txt` |
| **Old lines** | 469 |
| **New lines** | 470 |
| **Lines added** | 12 |
| **Lines removed** | 11 |
| **Hunks** | 9 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 8 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 177–183 | 177–183 | Types | +1 | −1 |
| 2 | 188–194 | 188–194 | Types | +1 | −1 |
| 3 | 209–215 | 209–215 | Types | +1 | −1 |
| 4 | 253–261 | 253–261 | Types | +2 | −2 |
| 5 | 290–296 | 290–296 | Types | +1 | −1 |
| 6 | 311–317 | 311–317 | Types | +1 | −1 |
| 7 | 320–326 | 320–326 | Types | +1 | −1 |
| 8 | 359–364 | 359–365 | Types | +1 | −0 |
| 9 | 421–435 | 422–436 | Client | +3 | −3 |

---

## Unified diff

`````diff
--- hubspot.crm.pipelines/old/ballerinax_hubspot.crm.pipelines.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.pipelines/new/ballerinax_hubspot.crm.pipelines.bal.txt	2026-08-12 13:19:19
@@ -177,7 +177,7 @@
 For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`
     record {|string...;|} metadata?;
     # The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline
     string label?;
 };
@@ -188,7 +188,7 @@
     # Whether the pipeline is archived. This property should only be provided when restoring an archived pipeline. If it's provided in any other call, the request will fail and a `400 Bad Request` will be returned
     boolean archived?;
     # The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A unique label used to organize pipelines in HubSpot's UI
     string label?;
 };
@@ -209,7 +209,7 @@
 For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`
     record {|string...;|} metadata?;
     # The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # Controls who can write to this pipeline stage
     "CRM_PERMISSIONS_ENFORCEMENT"|"READ_ONLY"|"INTERNAL_ONLY" writePermissions?;
     # A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline
@@ -253,9 +253,9 @@
     # Serialized snapshot of the object at the time of the audit event
     string rawObject?;
     # ID of the user who performed the audited action
-    ballerina/lang.int:0.0.0:Signed32 fromUserId?;
+    int:Signed32 fromUserId?;
     # ID of the HubSpot portal where the action occurred
-    ballerina/lang.int:0.0.0:Signed32 portalId;
+    int:Signed32 portalId;
     # The type of action recorded in the audit entry
     string action;
     # Human-readable description of the audited action
@@ -290,7 +290,7 @@
     # Whether the pipeline is archived
     boolean archived;
     # The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # The stages associated with the pipeline. They can be retrieved and updated via the pipeline stages endpoints
     PipelineStage[] stages;
     # A unique label used to organize pipelines in HubSpot's UI
@@ -311,7 +311,7 @@
 For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`
     record {|string...;|} metadata?;
     # The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline
     string label;
 };
@@ -320,7 +320,7 @@
 
 type PipelineInput record {
     # The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # Pipeline stage inputs used to create the new or replacement pipeline
     PipelineStageInput[] stages;
     # A unique label used to organize pipelines in HubSpot's UI
@@ -359,6 +359,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -421,15 +422,15 @@
 
     # Replace a pipeline
     # 
-    resource function put [string objectType]/[string pipelineId](PipelineInput payload, map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, anydata Additional Values, PutCrmV3PipelinesObjectTypePipelineIdReplaceQueries queries) returns Pipeline|error;
+    resource function put [string objectType]/[string pipelineId](PipelineInput payload, map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, PutCrmV3PipelinesObjectTypePipelineIdReplaceQueries queries) returns Pipeline|error;
 
     # Delete a pipeline
     # 
-    resource function delete [string objectType]/[string pipelineId](map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, anydata Additional Values, DeleteCrmV3PipelinesObjectTypePipelineIdArchiveQueries queries) returns error?;
+    resource function delete [string objectType]/[string pipelineId](map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, DeleteCrmV3PipelinesObjectTypePipelineIdArchiveQueries queries) returns error?;
 
     # Update a pipeline
     # 
-    resource function patch [string objectType]/[string pipelineId](PipelinePatchInput payload, map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, anydata Additional Values, PatchCrmV3PipelinesObjectTypePipelineIdUpdateQueries queries) returns Pipeline|error;
+    resource function patch [string objectType]/[string pipelineId](PipelinePatchInput payload, map<string|string[]> headers = {}, boolean validateDealStageUsagesBeforeDelete = false, boolean validateReferencesBeforeDelete = false, PatchCrmV3PipelinesObjectTypePipelineIdUpdateQueries queries) returns Pipeline|error;
 
     # Audit all pipeline changes
     # 
`````

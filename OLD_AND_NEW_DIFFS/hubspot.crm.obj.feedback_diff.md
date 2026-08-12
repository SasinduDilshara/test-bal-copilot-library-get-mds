# hubspot.crm.obj.feedback — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.feedback` |
| **Old file** | `hubspot.crm.obj.feedback/old/ballerinax_hubspot.crm.obj.feedback.bal.txt` |
| **New file** | `hubspot.crm.obj.feedback/new/ballerinax_hubspot.crm.obj.feedback.bal.txt` |
| **Old lines** | 780 |
| **New lines** | 781 |
| **Lines added** | 16 |
| **Lines removed** | 15 |
| **Hunks** | 15 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 11 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 292–298 | 292–298 | Types | +1 | −1 |
| 2 | 329–335 | 329–335 | Types | +1 | −1 |
| 3 | 348–354 | 348–354 | Types | +1 | −1 |
| 4 | 397–403 | 397–403 | Types | +1 | −1 |
| 5 | 424–430 | 424–430 | Types | +1 | −1 |
| 6 | 510–516 | 510–516 | Types | +1 | −1 |
| 7 | 519–524 | 519–525 | Types | +1 | −0 |
| 8 | 578–584 | 579–585 | Types | +1 | −1 |
| 9 | 591–597 | 592–598 | Types | +1 | −1 |
| 10 | 608–614 | 609–615 | Types | +1 | −1 |
| 11 | 660–666 | 661–667 | Types | +1 | −1 |
| 12 | 668–674 | 669–675 | Types | +1 | −1 |
| 13 | 736–746 | 737–747 | Client | +2 | −2 |
| 14 | 748–754 | 749–755 | Client | +1 | −1 |
| 15 | 764–770 | 765–771 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.feedback/old/ballerinax_hubspot.crm.obj.feedback.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.feedback/new/ballerinax_hubspot.crm.obj.feedback.bal.txt	2026-08-12 13:19:19
@@ -292,7 +292,7 @@
     # The category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -329,7 +329,7 @@
     # Timestamp when the feedback submission was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.feedback:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the feedback submission
     string id;
     # Key-value map of feedback submission property names and their values
@@ -348,7 +348,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated the value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The actual property value recorded at the given timestamp
     string value;
     # Timestamp indicating when the value was recorded
@@ -397,7 +397,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing
@@ -424,7 +424,7 @@
     # Indicates whether the object was newly created by the upsert
     boolean 'new;
     # A map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.feedback:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the object
     string id;
     # A map of property names to their current values
@@ -510,7 +510,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of feedback submissions matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of feedback submission objects returned in this page
@@ -519,6 +519,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -578,7 +579,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -591,7 +592,7 @@
     # Full-text search query string to filter feedback submissions
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Pagination cursor token for the next page of results
     string after?;
     # List of property names to sort results by
@@ -608,7 +609,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -660,7 +661,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM object collections keyed by association type
-    record {|ballerinax/hubspot.crm.obj.feedback:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the feedback submission was created
     string createdAt;
     # Indicates whether the feedback submission is archived
@@ -668,7 +669,7 @@
     # Timestamp when the feedback submission was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.feedback:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the feedback submission object
     string id;
     # Key-value map of the feedback submission's current property values
@@ -736,11 +737,11 @@
 
     # Read a batch of submissions
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsFeedbackSubmissionsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsFeedbackSubmissionsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Get a feedback submission
     # 
-    resource function get [string feedbackSubmissionId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsFeedbackSubmissionsFeedbackSubmissionIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string feedbackSubmissionId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsFeedbackSubmissionsFeedbackSubmissionIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a feedback submission
     # 
@@ -748,7 +749,7 @@
 
     # Update a feedback submission
     # 
-    resource function patch [string feedbackSubmissionId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsFeedbackSubmissionsFeedbackSubmissionIdQueries queries) returns SimplePublicObject|error;
+    resource function patch [string feedbackSubmissionId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsFeedbackSubmissionsFeedbackSubmissionIdQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of submissions
     # 
@@ -764,7 +765,7 @@
 
     # List feedback submissions
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsFeedbackSubmissionsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsFeedbackSubmissionsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a feedback submission
     # 
`````

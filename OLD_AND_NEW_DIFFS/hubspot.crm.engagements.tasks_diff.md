# hubspot.crm.engagements.tasks — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagements.tasks` |
| **Old file** | `hubspot.crm.engagements.tasks/old/ballerinax_hubspot.crm.engagements.tasks.bal.txt` |
| **New file** | `hubspot.crm.engagements.tasks/new/ballerinax_hubspot.crm.engagements.tasks.bal.txt` |
| **Old lines** | 790 |
| **New lines** | 791 |
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
| 1 | 304–310 | 304–310 | Types | +1 | −1 |
| 2 | 326–332 | 326–332 | Types | +1 | −1 |
| 3 | 363–369 | 363–369 | Types | +1 | −1 |
| 4 | 382–388 | 382–388 | Types | +1 | −1 |
| 5 | 431–437 | 431–437 | Types | +1 | −1 |
| 6 | 458–464 | 458–464 | Types | +1 | −1 |
| 7 | 559–565 | 559–565 | Types | +1 | −1 |
| 8 | 568–573 | 568–574 | Types | +1 | −0 |
| 9 | 623–629 | 624–630 | Types | +1 | −1 |
| 10 | 647–653 | 648–654 | Types | +1 | −1 |
| 11 | 684–690 | 685–691 | Types | +1 | −1 |
| 12 | 692–698 | 693–699 | Types | +1 | −1 |
| 13 | 746–756 | 747–757 | Client | +2 | −2 |
| 14 | 758–764 | 759–765 | Client | +1 | −1 |
| 15 | 774–780 | 775–781 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagements.tasks/old/ballerinax_hubspot.crm.engagements.tasks.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagements.tasks/new/ballerinax_hubspot.crm.engagements.tasks.bal.txt	2026-08-12 13:19:19
@@ -304,7 +304,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -326,7 +326,7 @@
     # The category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -363,7 +363,7 @@
     # Timestamp when the task record was archived
     string archivedAt?;
     # Map of task property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.engagements.tasks:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the task record
     string id;
     # Map of task property names to their current values
@@ -382,7 +382,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated this value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value recorded at the given timestamp
     string value;
     # Datetime when this value was recorded or last updated
@@ -431,7 +431,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -458,7 +458,7 @@
     # Indicates whether the task was newly created by the upsert operation
     boolean 'new;
     # A map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.engagements.tasks:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the task
     string id;
     # A map of the task's property names to their current values
@@ -559,7 +559,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of task records matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of task objects returned in the current page
@@ -568,6 +568,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -623,7 +624,7 @@
     # Full-text search query string to filter task results
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -647,7 +648,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation started
@@ -684,7 +685,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections, keyed by association type
-    record {|ballerinax/hubspot.crm.engagements.tasks:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the task was created
     string createdAt;
     # Indicates whether the task has been archived
@@ -692,7 +693,7 @@
     # Timestamp indicating when the task was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.engagements.tasks:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the task object
     string id;
     # Map of task property names to their current string values
@@ -746,11 +747,11 @@
 
     # Read tasks by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsTasksBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsTasksBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Read a task
     # 
-    resource function get [string taskId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTasksTaskIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string taskId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsTasksTaskIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a task
     # 
@@ -758,7 +759,7 @@
 
     # Update a task
     # 
-    resource function patch [string taskId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsTasksTaskIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string taskId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsTasksTaskIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of tasks by ID
     # 
@@ -774,7 +775,7 @@
 
     # List of the tasks
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTasksGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsTasksGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a task
     # 
`````

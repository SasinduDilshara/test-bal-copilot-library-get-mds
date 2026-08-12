# hubspot.crm.obj.leads — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.leads` |
| **Old file** | `hubspot.crm.obj.leads/old/ballerinax_hubspot.crm.obj.leads.bal.txt` |
| **New file** | `hubspot.crm.obj.leads/new/ballerinax_hubspot.crm.obj.leads.bal.txt` |
| **Old lines** | 803 |
| **New lines** | 804 |
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
| 1 | 317–323 | 317–323 | Types | +1 | −1 |
| 2 | 339–345 | 339–345 | Types | +1 | −1 |
| 3 | 376–382 | 376–382 | Types | +1 | −1 |
| 4 | 395–401 | 395–401 | Types | +1 | −1 |
| 5 | 444–450 | 444–450 | Types | +1 | −1 |
| 6 | 471–477 | 471–477 | Types | +1 | −1 |
| 7 | 557–563 | 557–563 | Types | +1 | −1 |
| 8 | 566–571 | 566–572 | Types | +1 | −0 |
| 9 | 628–634 | 629–635 | Types | +1 | −1 |
| 10 | 645–651 | 646–652 | Types | +1 | −1 |
| 11 | 682–688 | 683–689 | Types | +1 | −1 |
| 12 | 690–696 | 691–697 | Types | +1 | −1 |
| 13 | 759–769 | 760–770 | Client | +2 | −2 |
| 14 | 771–777 | 772–778 | Client | +1 | −1 |
| 15 | 787–793 | 788–794 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.leads/old/ballerinax_hubspot.crm.obj.leads.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.leads/new/ballerinax_hubspot.crm.obj.leads.bal.txt	2026-08-12 13:19:19
@@ -317,7 +317,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -339,7 +339,7 @@
     # Category of the association: HubSpot-defined, user-defined, or integrator-defined
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -376,7 +376,7 @@
     # Timestamp when the lead record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.leads:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the lead record
     string id;
     # Map of lead property names to their current values
@@ -395,7 +395,7 @@
     # A human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated this property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string
     string value;
     # Timestamp indicating when this value was last updated
@@ -444,7 +444,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -471,7 +471,7 @@
     # Indicates whether the lead was newly created by the upsert
     boolean 'new;
     # A map of lead property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.leads:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the lead record
     string id;
     # A map of lead property names to their current values
@@ -557,7 +557,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of leads matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object providing a reference to the next page of results
     ForwardPaging paging?;
     # Array of lead records returned in the current page
@@ -566,6 +566,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -628,7 +629,7 @@
     # Full-text search query string to match against lead records
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of sort criteria to order the search results
@@ -645,7 +646,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -682,7 +683,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object types to their associated record collections
-    record {|ballerinax/hubspot.crm.obj.leads:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the lead record was created
     string createdAt;
     # Indicates whether the lead record is archived
@@ -690,7 +691,7 @@
     # Timestamp when the lead record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.leads:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the lead record
     string id;
     # Key-value map of the lead's current property names and values
@@ -759,11 +760,11 @@
 
     # Read a batch of leads
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsLeadsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsLeadsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a lead by ID
     # 
-    resource function get [string leadsId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsLeadsLeadsIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string leadsId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsLeadsLeadsIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a lead by ID
     # 
@@ -771,7 +772,7 @@
 
     # Partially update a lead
     # 
-    resource function patch [string leadsId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsLeadsLeadsIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string leadsId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsLeadsLeadsIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of leads by ID
     # 
@@ -787,7 +788,7 @@
 
     # List a page of leads
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsLeadsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsLeadsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a lead
     # 
`````

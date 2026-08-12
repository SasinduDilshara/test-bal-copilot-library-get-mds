# hubspot.crm.obj.deals — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.deals` |
| **Old file** | `hubspot.crm.obj.deals/old/ballerinax_hubspot.crm.obj.deals.bal.txt` |
| **New file** | `hubspot.crm.obj.deals/new/ballerinax_hubspot.crm.obj.deals.bal.txt` |
| **Old lines** | 795 |
| **New lines** | 796 |
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
| 1 | 308–314 | 308–314 | Types | +1 | −1 |
| 2 | 345–351 | 345–351 | Types | +1 | −1 |
| 3 | 364–370 | 364–370 | Types | +1 | −1 |
| 4 | 413–419 | 413–419 | Types | +1 | −1 |
| 5 | 440–446 | 440–446 | Types | +1 | −1 |
| 6 | 526–532 | 526–532 | Types | +1 | −1 |
| 7 | 535–540 | 535–541 | Types | +1 | −0 |
| 8 | 590–596 | 591–597 | Types | +1 | −1 |
| 9 | 607–613 | 608–614 | Types | +1 | −1 |
| 10 | 644–650 | 645–651 | Types | +1 | −1 |
| 11 | 652–658 | 653–659 | Types | +1 | −1 |
| 12 | 733–739 | 734–740 | Types | +1 | −1 |
| 13 | 747–757 | 748–758 | Client | +2 | −2 |
| 14 | 759–765 | 760–766 | Client | +1 | −1 |
| 15 | 779–785 | 780–786 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.deals/old/ballerinax_hubspot.crm.obj.deals.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.deals/new/ballerinax_hubspot.crm.obj.deals.bal.txt	2026-08-12 13:19:19
@@ -308,7 +308,7 @@
     # Category of the association: HubSpot-defined, user-defined, or integrator-defined
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory?;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId?;
+    int:Signed32 associationTypeId?;
 };
 
 # Contains the unique identifier for a public object
@@ -345,7 +345,7 @@
     # Timestamp when the deal was archived
     string archivedAt?;
     # Map of deal property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.deals:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the deal
     string id;
     # Map of deal property names to their current values
@@ -364,7 +364,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated this value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value stored as a string
     string value;
     # Datetime when this value was last recorded or updated
@@ -413,7 +413,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -440,7 +440,7 @@
     # Indicates whether the record was created (true) or updated (false) by the upsert
     boolean 'new;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.deals:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the upserted deal object
     string id;
     # Key-value map of deal property names to their values
@@ -526,7 +526,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of deals matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of deal objects returned in the current page
@@ -535,6 +535,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -590,7 +591,7 @@
     # Full-text search query string to filter deals
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -607,7 +608,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -644,7 +645,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections keyed by association type
-    record {|ballerinax/hubspot.crm.obj.deals:1.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the deal record was created
     string createdAt;
     # Indicates whether the deal record is archived
@@ -652,7 +653,7 @@
     # Timestamp indicating when the deal record was archived
     string archivedAt?;
     # Map of deal properties with their full historical value changes
-    record {|ballerinax/hubspot.crm.obj.deals:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the deal record
     string id;
     # Map of deal property names to their current string values
@@ -733,7 +734,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -747,11 +748,11 @@
 
     # Read deals by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsDealsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsDealsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a deal by ID
     # 
-    resource function get [string dealId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsDealsDealIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string dealId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsDealsDealIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a deal by ID
     # 
@@ -759,7 +760,7 @@
 
     # Update a deal by ID
     # 
-    resource function patch [string dealId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsDealsDealIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string dealId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsDealsDealIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Merge two deals
     # 
@@ -779,7 +780,7 @@
 
     # List a page of deals
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsDealsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsDealsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new deal
     # 
`````

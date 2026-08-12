# hubspot.crm.obj.products — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.products` |
| **Old file** | `hubspot.crm.obj.products/old/ballerinax_hubspot.crm.obj.products.bal.txt` |
| **New file** | `hubspot.crm.obj.products/new/ballerinax_hubspot.crm.obj.products.bal.txt` |
| **Old lines** | 781 |
| **New lines** | 782 |
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
| 1 | 300–306 | 300–306 | Types | +1 | −1 |
| 2 | 337–343 | 337–343 | Types | +1 | −1 |
| 3 | 356–362 | 356–362 | Types | +1 | −1 |
| 4 | 395–401 | 395–401 | Types | +1 | −1 |
| 5 | 422–428 | 422–428 | Types | +1 | −1 |
| 6 | 449–455 | 449–455 | Types | +1 | −1 |
| 7 | 535–541 | 535–541 | Types | +1 | −1 |
| 8 | 544–549 | 544–550 | Types | +1 | −0 |
| 9 | 599–605 | 600–606 | Types | +1 | −1 |
| 10 | 623–629 | 624–630 | Types | +1 | −1 |
| 11 | 660–666 | 661–667 | Types | +1 | −1 |
| 12 | 668–674 | 669–675 | Types | +1 | −1 |
| 13 | 737–747 | 738–748 | Client | +2 | −2 |
| 14 | 749–755 | 750–756 | Client | +1 | −1 |
| 15 | 765–771 | 766–772 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.products/old/ballerinax_hubspot.crm.obj.products.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.products/new/ballerinax_hubspot.crm.obj.products.bal.txt	2026-08-12 13:19:19
@@ -300,7 +300,7 @@
     # The category that defines the origin of the association type
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # The numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -337,7 +337,7 @@
     # Timestamp when the product record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.products:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the product record
     string id;
     # Map of property names to their current values for the product
@@ -356,7 +356,7 @@
     # Human-readable label describing the source of the value
     string sourceLabel?;
     # ID of the user who last updated this property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value associated with the given timestamp
     string value;
     # Timestamp when this property value was last updated
@@ -395,7 +395,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -422,7 +422,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -449,7 +449,7 @@
     # Indicates whether the record was newly created by the upsert
     boolean 'new;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.products:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the product record
     string id;
     # Map of property names to their current values for the product
@@ -535,7 +535,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of results matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object providing a cursor for retrieving the next page of results
     ForwardPaging paging?;
     # Array of product objects returned in the current page
@@ -544,6 +544,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -599,7 +600,7 @@
     # Full-text search query string to match against product records
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of sort criteria to order search results
@@ -623,7 +624,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing
@@ -660,7 +661,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections keyed by association type
-    record {|ballerinax/hubspot.crm.obj.products:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the product record was created
     string createdAt;
     # Indicates whether the product record is archived
@@ -668,7 +669,7 @@
     # Timestamp indicating when the product record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.products:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the product record
     string id;
     # Key-value map of product property names to their current string values
@@ -737,11 +738,11 @@
 
     # Read products by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a product by ID
     # 
-    resource function get [string productId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetProductIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string productId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetProductIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a product by ID
     # 
@@ -749,7 +750,7 @@
 
     # Partially update a product
     # 
-    resource function patch [string productId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchProductIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string productId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchProductIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of products by ID
     # 
@@ -765,7 +766,7 @@
 
     # Retrieve a page of products
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new product
     # 
`````

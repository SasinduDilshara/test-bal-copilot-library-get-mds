# hubspot.crm.obj.lineitems — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.lineitems` |
| **Old file** | `hubspot.crm.obj.lineitems/old/ballerinax_hubspot.crm.obj.lineitems.bal.txt` |
| **New file** | `hubspot.crm.obj.lineitems/new/ballerinax_hubspot.crm.obj.lineitems.bal.txt` |
| **Old lines** | 797 |
| **New lines** | 798 |
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
| 1 | 324–330 | 324–330 | Types | +1 | −1 |
| 2 | 361–367 | 361–367 | Types | +1 | −1 |
| 3 | 380–386 | 380–386 | Types | +1 | −1 |
| 4 | 429–435 | 429–435 | Types | +1 | −1 |
| 5 | 456–462 | 456–462 | Types | +1 | −1 |
| 6 | 542–548 | 542–548 | Types | +1 | −1 |
| 7 | 558–563 | 558–564 | Types | +1 | −0 |
| 8 | 620–626 | 621–627 | Types | +1 | −1 |
| 9 | 637–643 | 638–644 | Types | +1 | −1 |
| 10 | 674–680 | 675–681 | Types | +1 | −1 |
| 11 | 682–688 | 683–689 | Types | +1 | −1 |
| 12 | 739–745 | 740–746 | Types | +1 | −1 |
| 13 | 753–763 | 754–764 | Client | +2 | −2 |
| 14 | 765–771 | 766–772 | Client | +1 | −1 |
| 15 | 781–787 | 782–788 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.lineitems/old/ballerinax_hubspot.crm.obj.lineitems.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.lineitems/new/ballerinax_hubspot.crm.obj.lineitems.bal.txt	2026-08-12 13:19:19
@@ -324,7 +324,7 @@
     # The category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier specifying the association type within its category
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -361,7 +361,7 @@
     # Timestamp when the line item was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.lineitems:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the line item
     string id;
     # Map of line item property names to their current values
@@ -380,7 +380,7 @@
     # Human-readable label describing the source of the value
     string sourceLabel?;
     # ID of the user who last updated this property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value stored for this line item
     string value;
     # Timestamp indicating when this property value was last updated
@@ -429,7 +429,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -456,7 +456,7 @@
     # Indicates whether the line item was newly created by the upsert
     boolean 'new;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.lineitems:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the line item
     string id;
     # Map of property names to their current values for the line item
@@ -542,7 +542,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of line items matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of line item objects returned in the current page
@@ -558,6 +558,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -620,7 +621,7 @@
     # Full-text search query string to match against line items
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -637,7 +638,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -674,7 +675,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM objects, keyed by association type label
-    record {|ballerinax/hubspot.crm.obj.lineitems:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the line item was created
     string createdAt;
     # Indicates whether the line item has been archived
@@ -682,7 +683,7 @@
     # Timestamp indicating when the line item was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.lineitems:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the line item
     string id;
     # Key-value map of the line item's current property names and values
@@ -739,7 +740,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -753,11 +754,11 @@
 
     # Read line items by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsLineItemsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsLineItemsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a line item by ID
     # 
-    resource function get [string lineItemId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsLineItemsLineItemIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string lineItemId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsLineItemsLineItemIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a line item by ID
     # 
@@ -765,7 +766,7 @@
 
     # Update a line item by ID
     # 
-    resource function patch [string lineItemId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsLineItemsLineItemIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string lineItemId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsLineItemsLineItemIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of line items by ID
     # 
@@ -781,7 +782,7 @@
 
     # List a page of line items
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsLineItemsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsLineItemsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a line item
     # 
`````

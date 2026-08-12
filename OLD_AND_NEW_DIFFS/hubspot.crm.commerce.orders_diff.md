# hubspot.crm.commerce.orders — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.commerce.orders` |
| **Old file** | `hubspot.crm.commerce.orders/old/ballerinax_hubspot.crm.commerce.orders.bal.txt` |
| **New file** | `hubspot.crm.commerce.orders/new/ballerinax_hubspot.crm.commerce.orders.bal.txt` |
| **Old lines** | 785 |
| **New lines** | 786 |
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
| 1 | 307–313 | 307–313 | Types | +1 | −1 |
| 2 | 329–335 | 329–335 | Types | +1 | −1 |
| 3 | 366–372 | 366–372 | Types | +1 | −1 |
| 4 | 385–391 | 385–391 | Types | +1 | −1 |
| 5 | 434–440 | 434–440 | Types | +1 | −1 |
| 6 | 461–467 | 461–467 | Types | +1 | −1 |
| 7 | 554–560 | 554–560 | Types | +1 | −1 |
| 8 | 563–568 | 563–569 | Types | +1 | −0 |
| 9 | 618–624 | 619–625 | Types | +1 | −1 |
| 10 | 635–641 | 636–642 | Types | +1 | −1 |
| 11 | 672–678 | 673–679 | Types | +1 | −1 |
| 12 | 680–686 | 681–687 | Types | +1 | −1 |
| 13 | 741–751 | 742–752 | Client | +2 | −2 |
| 14 | 753–759 | 754–760 | Client | +1 | −1 |
| 15 | 769–775 | 770–776 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.commerce.orders/old/ballerinax_hubspot.crm.commerce.orders.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.commerce.orders/new/ballerinax_hubspot.crm.commerce.orders.bal.txt	2026-08-12 13:19:19
@@ -307,7 +307,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -329,7 +329,7 @@
     # Category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -366,7 +366,7 @@
     # Timestamp when the order was archived
     string archivedAt?;
     # Map of order properties including their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.orders:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the order object
     string id;
     # Map of order property names to their current values
@@ -385,7 +385,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated this value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string
     string value;
     # Timestamp indicating when the value was last updated
@@ -434,7 +434,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -461,7 +461,7 @@
     # Indicates whether the object was newly created by the upsert
     boolean 'new;
     # A map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.orders:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the object
     string id;
     # A map of property names to their current string values
@@ -554,7 +554,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of orders matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of order objects returned in the current page
@@ -563,6 +563,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -618,7 +619,7 @@
     # Full-text search query string to match against order records
     string query?;
     # Maximum number of results to return in the response
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -635,7 +636,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing
@@ -672,7 +673,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections keyed by association type
-    record {|ballerinax/hubspot.crm.commerce.orders:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the order record was created
     string createdAt;
     # Indicates whether the order record is archived
@@ -680,7 +681,7 @@
     # Timestamp when the order record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.orders:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the order record
     string id;
     # Key-value map of the order's current property names and values
@@ -741,11 +742,11 @@
 
     # Read a batch of orders by ID
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsOrdersBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsOrdersBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve an order by ID
     # 
-    resource function get [string orderId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsOrdersOrderIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string orderId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsOrdersOrderIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive an order by ID
     # 
@@ -753,7 +754,7 @@
 
     # Update an order by ID
     # 
-    resource function patch [string orderId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsOrdersOrderIdQueries queries) returns SimplePublicObject|error;
+    resource function patch [string orderId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsOrdersOrderIdQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of orders by ID
     # 
@@ -769,7 +770,7 @@
 
     # List all orders
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsOrdersQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsOrdersQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new order
     # 
`````

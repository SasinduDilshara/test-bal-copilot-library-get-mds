# hubspot.crm.commerce.carts — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.commerce.carts` |
| **Old file** | `hubspot.crm.commerce.carts/old/ballerinax_hubspot.crm.commerce.carts.bal.txt` |
| **New file** | `hubspot.crm.commerce.carts/new/ballerinax_hubspot.crm.commerce.carts.bal.txt` |
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
| 1 | 298–304 | 298–304 | Types | +1 | −1 |
| 2 | 335–341 | 335–341 | Types | +1 | −1 |
| 3 | 354–360 | 354–360 | Types | +1 | −1 |
| 4 | 402–408 | 402–408 | Types | +1 | −1 |
| 5 | 429–435 | 429–435 | Types | +1 | −1 |
| 6 | 508–514 | 508–514 | Types | +1 | −1 |
| 7 | 539–545 | 539–545 | Types | +1 | −1 |
| 8 | 548–553 | 548–554 | Types | +1 | −0 |
| 9 | 610–616 | 611–617 | Types | +1 | −1 |
| 10 | 627–633 | 628–634 | Types | +1 | −1 |
| 11 | 664–670 | 665–671 | Types | +1 | −1 |
| 12 | 672–678 | 673–679 | Types | +1 | −1 |
| 13 | 737–747 | 738–748 | Client | +2 | −2 |
| 14 | 749–755 | 750–756 | Client | +1 | −1 |
| 15 | 765–771 | 766–772 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.commerce.carts/old/ballerinax_hubspot.crm.commerce.carts.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.commerce.carts/new/ballerinax_hubspot.crm.commerce.carts.bal.txt	2026-08-12 13:19:19
@@ -298,7 +298,7 @@
     # The category of the association: HubSpot-defined, user-defined, or integrator-defined
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric ID identifying the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -335,7 +335,7 @@
     # Timestamp indicating when the cart object was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.carts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the cart object
     string id;
     # Map of cart property names to their current values
@@ -354,7 +354,7 @@
     # Human-readable label describing the source of the value
     string sourceLabel?;
     # ID of the user who last updated the property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value associated with the cart record
     string value;
     # Timestamp indicating when the property value was last updated
@@ -402,7 +402,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch request was received
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing
@@ -429,7 +429,7 @@
     # Indicates whether the object was newly created by the upsert
     boolean 'new;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.carts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the cart object
     string id;
     # Map of property names to their current string values
@@ -508,7 +508,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -539,7 +539,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of cart objects matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based result traversal
     ForwardPaging paging?;
     # Array of cart objects returned in the current page
@@ -548,6 +548,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -610,7 +611,7 @@
     # Full-text search query string to match against cart properties
     string query?;
     # Maximum number of cart objects to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of sort criteria to order the search results
@@ -627,7 +628,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing
@@ -664,7 +665,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections, keyed by association type
-    record {|ballerinax/hubspot.crm.commerce.carts:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the cart record was created
     string createdAt;
     # Indicates whether the cart record has been archived
@@ -672,7 +673,7 @@
     # Timestamp indicating when the cart record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.carts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the cart record
     string id;
     # Key-value pairs of cart property names and their current values
@@ -737,11 +738,11 @@
 
     # Read a batch of carts by internal ID, or unique property values
     # 
-    resource function post carts/batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsCartsBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post carts/batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsCartsBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a cart by ID
     # 
-    resource function get carts/[string cartId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCartsCartIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get carts/[string cartId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsCartsCartIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a cart by ID
     # 
@@ -749,7 +750,7 @@
 
     # Update a cart by ID
     # 
-    resource function patch carts/[string cartId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsCartsCartIdQueries queries) returns SimplePublicObject|error;
+    resource function patch carts/[string cartId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsCartsCartIdQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of carts by ID
     # 
@@ -765,7 +766,7 @@
 
     # Retrieve a page of carts
     # 
-    resource function get carts(map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCartsQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get carts(map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsCartsQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new cart
     # 
`````

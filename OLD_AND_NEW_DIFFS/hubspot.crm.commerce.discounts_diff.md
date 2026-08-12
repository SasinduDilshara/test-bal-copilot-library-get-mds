# hubspot.crm.commerce.discounts — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.commerce.discounts` |
| **Old file** | `hubspot.crm.commerce.discounts/old/ballerinax_hubspot.crm.commerce.discounts.bal.txt` |
| **New file** | `hubspot.crm.commerce.discounts/new/ballerinax_hubspot.crm.commerce.discounts.bal.txt` |
| **Old lines** | 763 |
| **New lines** | 764 |
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
| 1 | 275–281 | 275–281 | Types | +1 | −1 |
| 2 | 312–318 | 312–318 | Types | +1 | −1 |
| 3 | 331–337 | 331–337 | Types | +1 | −1 |
| 4 | 370–376 | 370–376 | Types | +1 | −1 |
| 5 | 397–403 | 397–403 | Types | +1 | −1 |
| 6 | 424–430 | 424–430 | Types | +1 | −1 |
| 7 | 517–523 | 517–523 | Types | +1 | −1 |
| 8 | 526–531 | 526–532 | Types | +1 | −0 |
| 9 | 581–587 | 582–588 | Types | +1 | −1 |
| 10 | 598–604 | 599–605 | Types | +1 | −1 |
| 11 | 635–641 | 636–642 | Types | +1 | −1 |
| 12 | 643–649 | 644–650 | Types | +1 | −1 |
| 13 | 719–729 | 720–730 | Client | +2 | −2 |
| 14 | 731–737 | 732–738 | Client | +1 | −1 |
| 15 | 747–753 | 748–754 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.commerce.discounts/old/ballerinax_hubspot.crm.commerce.discounts.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.commerce.discounts/new/ballerinax_hubspot.crm.commerce.discounts.bal.txt	2026-08-12 13:19:19
@@ -275,7 +275,7 @@
     # Category of the association: HubSpot-defined, user-defined, or integrator-defined.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a reference to a public object by its unique identifier.
@@ -312,7 +312,7 @@
     # Timestamp when the discount record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.commerce.discounts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the discount record.
     string id;
     # Map of discount property names to their current string values.
@@ -331,7 +331,7 @@
     # Human-readable label describing the value's source.
     string sourceLabel?;
     # ID of the user who last updated this value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string.
     string value;
     # Datetime when this value was last updated.
@@ -370,7 +370,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -397,7 +397,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing.
@@ -424,7 +424,7 @@
     # Indicates whether the object was newly created by the upsert.
     boolean 'new;
     # A map of property values including their historical change records.
-    record {|ballerinax/hubspot.crm.commerce.discounts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the object.
     string id;
     # A map of the object's property names to their current values.
@@ -517,7 +517,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of discount records matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object providing a cursor for forward navigation.
     ForwardPaging paging?;
     # Array of discount objects returned in the current page.
@@ -526,6 +526,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -581,7 +582,7 @@
     # Full-text search query string to filter discounts.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results.
     string after?;
     # List of sort criteria to order the search results.
@@ -598,7 +599,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -635,7 +636,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated objects grouped by association type.
-    record {|ballerinax/hubspot.crm.commerce.discounts:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the discount object was created.
     string createdAt;
     # Indicates whether the discount object is archived.
@@ -643,7 +644,7 @@
     # Timestamp when the discount object was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.commerce.discounts:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the discount object.
     string id;
     # Key-value map of the discount object's current property values.
@@ -719,11 +720,11 @@
 
     # Read a batch of discounts
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsDiscountsBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsDiscountsBatchReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a discount by ID
     # 
-    resource function get [string discountId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsDiscountsDiscountIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string discountId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsDiscountsDiscountIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a discount by ID
     # 
@@ -731,7 +732,7 @@
 
     # Update a discount by ID
     # 
-    resource function patch [string discountId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsDiscountsDiscountIdQueries queries) returns SimplePublicObject|error;
+    resource function patch [string discountId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsDiscountsDiscountIdQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of discounts by ID
     # 
@@ -747,7 +748,7 @@
 
     # List all discounts
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsDiscountsQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsDiscountsQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a discount
     # 
`````

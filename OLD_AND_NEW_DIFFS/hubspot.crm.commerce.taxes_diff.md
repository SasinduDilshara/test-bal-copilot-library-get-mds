# hubspot.crm.commerce.taxes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.commerce.taxes` |
| **Old file** | `hubspot.crm.commerce.taxes/old/ballerinax_hubspot.crm.commerce.taxes.bal.txt` |
| **New file** | `hubspot.crm.commerce.taxes/new/ballerinax_hubspot.crm.commerce.taxes.bal.txt` |
| **Old lines** | 761 |
| **New lines** | 762 |
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
| 1 | 280–286 | 280–286 | Types | +1 | −1 |
| 2 | 317–323 | 317–323 | Types | +1 | −1 |
| 3 | 336–342 | 336–342 | Types | +1 | −1 |
| 4 | 385–391 | 385–391 | Types | +1 | −1 |
| 5 | 412–418 | 412–418 | Types | +1 | −1 |
| 6 | 498–504 | 498–504 | Types | +1 | −1 |
| 7 | 507–512 | 507–513 | Types | +1 | −0 |
| 8 | 581–587 | 582–588 | Types | +1 | −1 |
| 9 | 594–600 | 595–601 | Types | +1 | −1 |
| 10 | 611–617 | 612–618 | Types | +1 | −1 |
| 11 | 648–654 | 649–655 | Types | +1 | −1 |
| 12 | 656–662 | 657–663 | Types | +1 | −1 |
| 13 | 717–727 | 718–728 | Client | +2 | −2 |
| 14 | 729–735 | 730–736 | Client | +1 | −1 |
| 15 | 745–751 | 746–752 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.commerce.taxes/old/ballerinax_hubspot.crm.commerce.taxes.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.commerce.taxes/new/ballerinax_hubspot.crm.commerce.taxes.bal.txt	2026-08-12 13:19:19
@@ -280,7 +280,7 @@
     # Source category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier specifying the association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string.
@@ -317,7 +317,7 @@
     # Timestamp when the tax record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.commerce.taxes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the tax record.
     string id;
     # Key-value map of the tax record's property names and their current values.
@@ -336,7 +336,7 @@
     # Human-readable label describing the value's source.
     string sourceLabel?;
     # ID of the user who last updated the value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value recorded at the associated timestamp.
     string value;
     # Datetime when the value was recorded or last updated.
@@ -385,7 +385,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -412,7 +412,7 @@
     # Indicates whether the object was newly created by the upsert.
     boolean 'new;
     # A map of property values including their historical change timestamps.
-    record {|ballerinax/hubspot.crm.commerce.taxes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the upserted object.
     string id;
     # A map of property names to their current string values.
@@ -498,7 +498,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of tax records matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object for forward-direction cursor navigation.
     ForwardPaging paging?;
     # Array of tax records returned in the current page.
@@ -507,6 +507,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -581,7 +582,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -594,7 +595,7 @@
     # Full-text search query string to filter tax records.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Pagination cursor token for the next page of results.
     string after?;
     # List of sort criteria to order the search results.
@@ -611,7 +612,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -648,7 +649,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object types to their related record collections.
-    record {|ballerinax/hubspot.crm.commerce.taxes:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the tax record was created.
     string createdAt;
     # Indicates whether the tax record is archived.
@@ -656,7 +657,7 @@
     # Timestamp when the tax record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.commerce.taxes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the tax record.
     string id;
     # Key-value map of the tax record's current property values.
@@ -717,11 +718,11 @@
 
     # Read a batch of taxes by ID
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsTaxesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsTaxesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a tax by ID
     # 
-    resource function get [string taxId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTaxesTaxIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string taxId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsTaxesTaxIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a tax by ID
     # 
@@ -729,7 +730,7 @@
 
     # Partially update a tax
     # 
-    resource function patch [string taxId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsTaxesTaxIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string taxId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsTaxesTaxIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of taxes by ID
     # 
@@ -745,7 +746,7 @@
 
     # Retrieve a page of taxes
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTaxesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsTaxesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new tax
     # 
`````

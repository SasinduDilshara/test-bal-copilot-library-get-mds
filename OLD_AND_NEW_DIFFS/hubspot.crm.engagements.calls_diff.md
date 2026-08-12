# hubspot.crm.engagements.calls — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagements.calls` |
| **Old file** | `hubspot.crm.engagements.calls/old/ballerinax_hubspot.crm.engagements.calls.bal.txt` |
| **New file** | `hubspot.crm.engagements.calls/new/ballerinax_hubspot.crm.engagements.calls.bal.txt` |
| **Old lines** | 826 |
| **New lines** | 827 |
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
| 1 | 338–344 | 338–344 | Types | +1 | −1 |
| 2 | 375–381 | 375–381 | Types | +1 | −1 |
| 3 | 394–400 | 394–400 | Types | +1 | −1 |
| 4 | 443–449 | 443–449 | Types | +1 | −1 |
| 5 | 470–476 | 470–476 | Types | +1 | −1 |
| 6 | 571–577 | 571–577 | Types | +1 | −1 |
| 7 | 580–585 | 580–586 | Types | +1 | −0 |
| 8 | 639–645 | 640–646 | Types | +1 | −1 |
| 9 | 659–665 | 660–666 | Types | +1 | −1 |
| 10 | 676–682 | 677–683 | Types | +1 | −1 |
| 11 | 713–719 | 714–720 | Types | +1 | −1 |
| 12 | 721–727 | 722–728 | Types | +1 | −1 |
| 13 | 782–792 | 783–793 | Client | +2 | −2 |
| 14 | 794–800 | 795–801 | Client | +1 | −1 |
| 15 | 810–816 | 811–817 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagements.calls/old/ballerinax_hubspot.crm.engagements.calls.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagements.calls/new/ballerinax_hubspot.crm.engagements.calls.bal.txt	2026-08-12 13:19:19
@@ -338,7 +338,7 @@
     # The source category of the association type (e.g., HUBSPOT_DEFINED).
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a single unique ID.
@@ -375,7 +375,7 @@
     # Timestamp when the call record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagements.calls:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the call record.
     string id;
     # Map of call property names to their current values.
@@ -394,7 +394,7 @@
     # Human-readable label describing the source of the value.
     string sourceLabel?;
     # ID of the user who last updated this property value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value string.
     string value;
     # Datetime when this property value was last updated.
@@ -443,7 +443,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered in the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -470,7 +470,7 @@
     # Indicates whether the object was newly created by the upsert.
     boolean 'new;
     # A map of property values including their historical change records.
-    record {|ballerinax/hubspot.crm.engagements.calls:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the upserted object.
     string id;
     # A map of property names to their current string values.
@@ -571,7 +571,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of call records matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation.
     ForwardPaging paging?;
     # Array of call records returned in the current page.
@@ -580,6 +580,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -639,7 +640,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -659,7 +660,7 @@
     # Full-text search query string to filter call records.
     string query?;
     # Maximum number of results to return in the response.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results.
     string after?;
     # List of sort criteria to order the search results.
@@ -676,7 +677,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing.
@@ -713,7 +714,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM objects grouped by association type.
-    record {|ballerinax/hubspot.crm.engagements.calls:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the call record was created.
     string createdAt;
     # Indicates whether the call record is archived.
@@ -721,7 +722,7 @@
     # Timestamp when the call record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagements.calls:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the call record.
     string id;
     # Key-value map of the call object's current property values.
@@ -782,11 +783,11 @@
 
     # Retrieve a batch of calls
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsCallsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsCallsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a call
     # 
-    resource function get [string callId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCallsCallIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string callId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsCallsCallIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a call
     # 
@@ -794,7 +795,7 @@
 
     # Update a call
     # 
-    resource function patch [string callId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsCallsCallIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string callId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsCallsCallIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of calls
     # 
@@ -810,7 +811,7 @@
 
     # Retrieve calls
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCallsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsCallsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a call
     # 
`````

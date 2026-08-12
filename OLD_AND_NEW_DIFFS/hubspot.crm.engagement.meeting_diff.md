# hubspot.crm.engagement.meeting — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagement.meeting` |
| **Old file** | `hubspot.crm.engagement.meeting/old/ballerinax_hubspot.crm.engagement.meeting.bal.txt` |
| **New file** | `hubspot.crm.engagement.meeting/new/ballerinax_hubspot.crm.engagement.meeting.bal.txt` |
| **Old lines** | 773 |
| **New lines** | 774 |
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
| 1 | 285–291 | 285–291 | Types | +1 | −1 |
| 2 | 322–328 | 322–328 | Types | +1 | −1 |
| 3 | 341–347 | 341–347 | Types | +1 | −1 |
| 4 | 390–396 | 390–396 | Types | +1 | −1 |
| 5 | 417–423 | 417–423 | Types | +1 | −1 |
| 6 | 510–516 | 510–516 | Types | +1 | −1 |
| 7 | 527–533 | 527–533 | Types | +1 | −1 |
| 8 | 536–541 | 536–542 | Types | +1 | −0 |
| 9 | 591–597 | 592–598 | Types | +1 | −1 |
| 10 | 608–614 | 609–615 | Types | +1 | −1 |
| 11 | 645–651 | 646–652 | Types | +1 | −1 |
| 12 | 653–659 | 654–660 | Types | +1 | −1 |
| 13 | 729–739 | 730–740 | Client | +2 | −2 |
| 14 | 741–747 | 742–748 | Client | +1 | −1 |
| 15 | 757–763 | 758–764 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagement.meeting/old/ballerinax_hubspot.crm.engagement.meeting.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagement.meeting/new/ballerinax_hubspot.crm.engagement.meeting.bal.txt	2026-08-12 13:19:19
@@ -285,7 +285,7 @@
     # Category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object reference identified by a unique ID string.
@@ -322,7 +322,7 @@
     # Timestamp when the meeting record was archived.
     string archivedAt?;
     # Map of meeting properties to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.meeting:2.0.0:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the meeting record.
     string id;
     # Key-value map of the meeting's property names and their current values.
@@ -341,7 +341,7 @@
     # Human-readable label describing the value's source.
     string sourceLabel?;
     # ID of the user who last updated this value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string.
     string value;
     # Timestamp indicating when this value was last updated.
@@ -390,7 +390,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -417,7 +417,7 @@
     # Indicates whether the object was newly created by the upsert.
     boolean 'new;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.meeting:2.0.0:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the meeting object.
     string id;
     # Key-value map of the meeting's property names and values.
@@ -510,7 +510,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of meeting records matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based result navigation.
     ForwardPaging paging?;
     # Array of meeting objects returned in the current page.
@@ -527,7 +527,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -536,6 +536,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -591,7 +592,7 @@
     # Full-text search query string to filter meeting results.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results.
     string after?;
     # List of property names to sort results by.
@@ -608,7 +609,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -645,7 +646,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections keyed by association type.
-    record {|ballerinax/hubspot.crm.engagement.meeting:2.0.0:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp when the meeting record was created.
     string createdAt;
     # Indicates whether the meeting record is archived.
@@ -653,7 +654,7 @@
     # Timestamp when the meeting record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.meeting:2.0.0:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the meeting record.
     string id;
     # Key-value map of the meeting's current property names and values.
@@ -729,11 +730,11 @@
 
     # Read a batch of meetings
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsMeetingsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsMeetingsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a meeting by ID
     # 
-    resource function get [string meetingId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsMeetingsMeetingIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string meetingId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsMeetingsMeetingIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a meeting by ID
     # 
@@ -741,7 +742,7 @@
 
     # Partially update a meeting
     # 
-    resource function patch [string meetingId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsMeetingsMeetingIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string meetingId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsMeetingsMeetingIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of meetings by ID
     # 
@@ -757,7 +758,7 @@
 
     # List a page of meetings
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsMeetingsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsMeetingsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a meeting
     # 
`````

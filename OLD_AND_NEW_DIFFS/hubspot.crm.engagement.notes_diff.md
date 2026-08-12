# hubspot.crm.engagement.notes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagement.notes` |
| **Old file** | `hubspot.crm.engagement.notes/old/ballerinax_hubspot.crm.engagement.notes.bal.txt` |
| **New file** | `hubspot.crm.engagement.notes/new/ballerinax_hubspot.crm.engagement.notes.bal.txt` |
| **Old lines** | 784 |
| **New lines** | 785 |
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
| 1 | 296–302 | 296–302 | Types | +1 | −1 |
| 2 | 340–346 | 340–346 | Types | +1 | −1 |
| 3 | 359–365 | 359–365 | Types | +1 | −1 |
| 4 | 376–382 | 376–382 | Types | +1 | −1 |
| 5 | 440–446 | 440–446 | Types | +1 | −1 |
| 6 | 467–473 | 467–473 | Types | +1 | −1 |
| 7 | 560–566 | 560–566 | Types | +1 | −1 |
| 8 | 569–574 | 569–575 | Types | +1 | −0 |
| 9 | 624–630 | 625–631 | Types | +1 | −1 |
| 10 | 641–647 | 642–648 | Types | +1 | −1 |
| 11 | 678–684 | 679–685 | Types | +1 | −1 |
| 12 | 686–692 | 687–693 | Types | +1 | −1 |
| 13 | 740–750 | 741–751 | Client | +2 | −2 |
| 14 | 752–758 | 753–759 | Client | +1 | −1 |
| 15 | 768–774 | 769–775 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagement.notes/old/ballerinax_hubspot.crm.engagement.notes.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagement.notes/new/ballerinax_hubspot.crm.engagement.notes.bal.txt	2026-08-12 13:19:19
@@ -296,7 +296,7 @@
     # Category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identified by a unique string ID.
@@ -340,7 +340,7 @@
     # Timestamp when the note was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.notes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the note object.
     string id;
     # Map of note property names to their current values.
@@ -359,7 +359,7 @@
     # Human-readable label describing the value's source.
     string sourceLabel?;
     # ID of the user who last updated this value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string.
     string value;
     # Timestamp when this value was recorded or last updated.
@@ -376,7 +376,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -440,7 +440,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -467,7 +467,7 @@
     # Indicates whether the note was newly created by the upsert.
     boolean 'new;
     # A map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.notes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the note.
     string id;
     # A map of the note's property names to their current values.
@@ -560,7 +560,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of notes matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object containing a reference to the next results page.
     ForwardPaging paging?;
     # Array of note objects returned in the current page.
@@ -569,6 +569,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -624,7 +625,7 @@
     # Full-text search query string to filter notes.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results.
     string after?;
     # List of sort criteria to order the search results.
@@ -641,7 +642,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing.
@@ -678,7 +679,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object types to their related record collections.
-    record {|ballerinax/hubspot.crm.engagement.notes:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the note was created.
     string createdAt;
     # Indicates whether the note has been archived.
@@ -686,7 +687,7 @@
     # Timestamp indicating when the note was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagement.notes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the note object.
     string id;
     # Key-value map of the note's current property names and values.
@@ -740,11 +741,11 @@
 
     # Read a batch of notes
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsNotesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsNotesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a note by ID
     # 
-    resource function get [string noteId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsNotesNoteIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string noteId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsNotesNoteIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a note by ID
     # 
@@ -752,7 +753,7 @@
 
     # Partially update a note
     # 
-    resource function patch [string noteId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsNotesNoteIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string noteId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsNotesNoteIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of notes by ID
     # 
@@ -768,7 +769,7 @@
 
     # Retrieve a page of notes
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsNotesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsNotesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new note
     # 
`````

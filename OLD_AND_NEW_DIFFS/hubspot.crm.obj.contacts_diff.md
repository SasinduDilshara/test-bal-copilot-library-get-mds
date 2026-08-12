# hubspot.crm.obj.contacts — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.contacts` |
| **Old file** | `hubspot.crm.obj.contacts/old/ballerinax_hubspot.crm.obj.contacts.bal.txt` |
| **New file** | `hubspot.crm.obj.contacts/new/ballerinax_hubspot.crm.obj.contacts.bal.txt` |
| **Old lines** | 782 |
| **New lines** | 783 |
| **Lines added** | 15 |
| **Lines removed** | 14 |
| **Hunks** | 14 |

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
| 1 | 277–283 | 277–283 | Types | +1 | −1 |
| 2 | 314–320 | 314–320 | Types | +1 | −1 |
| 3 | 333–339 | 333–339 | Types | +1 | −1 |
| 4 | 382–388 | 382–388 | Types | +1 | −1 |
| 5 | 409–415 | 409–415 | Types | +1 | −1 |
| 6 | 458–464 | 458–464 | Types | +1 | −1 |
| 7 | 512–518 | 512–518 | Types | +1 | −1 |
| 8 | 521–526 | 521–527 | Types | +1 | −0 |
| 9 | 576–582 | 577–583 | Types | +1 | −1 |
| 10 | 593–599 | 594–600 | Types | +1 | −1 |
| 11 | 646–652 | 647–653 | Types | +1 | −1 |
| 12 | 654–660 | 655–661 | Types | +1 | −1 |
| 13 | 730–740 | 731–741 | Client | +2 | −2 |
| 14 | 766–772 | 767–773 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.contacts/old/ballerinax_hubspot.crm.obj.contacts.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.contacts/new/ballerinax_hubspot.crm.obj.contacts.bal.txt	2026-08-12 13:19:19
@@ -277,7 +277,7 @@
     # The category defining who created the association type.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory?;
     # Numeric identifier for the specific association type.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId?;
+    int:Signed32 associationTypeId?;
 };
 
 # Represents a reference to a public object by its unique identifier.
@@ -314,7 +314,7 @@
     # Timestamp when the contact record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.obj.contacts:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier for the contact record.
     string id;
     # Map of contact property names to their current values.
@@ -333,7 +333,7 @@
     # Human-readable label describing the source of the property value.
     string sourceLabel?;
     # ID of the user who last updated the property value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value associated with the given timestamp and source.
     string value;
     # Timestamp indicating when the property value was last updated.
@@ -382,7 +382,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing.
@@ -409,7 +409,7 @@
     # Indicates whether the contact record was newly created by the upsert operation.
     boolean 'new;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.obj.contacts:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the upserted contact record.
     string id;
     # Map of property names to their current values for the contact.
@@ -458,7 +458,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -512,7 +512,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of contacts matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object providing a cursor for forward navigation through results.
     ForwardPaging paging?;
     # Array of contact objects returned in the current page.
@@ -521,6 +521,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -576,7 +577,7 @@
     # Full-text search query string to match against contact records.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results.
     string after?;
     # List of property names to sort results by.
@@ -593,7 +594,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing.
@@ -646,7 +647,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM object collections keyed by association type.
-    record {|ballerinax/hubspot.crm.obj.contacts:1.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the contact record was created.
     string createdAt;
     # Indicates whether the contact record has been archived.
@@ -654,7 +655,7 @@
     # Timestamp indicating when the contact record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.contacts:1.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the contact object
     string id;
     # Map of contact property names to their current values
@@ -730,11 +731,11 @@
 
     # Read contacts by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsContactsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsContactsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a contact by ID
     # 
-    resource function get [string contactId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string[] properties = [], anydata Additional Values, GetCrmV3ObjectsContactsContactIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string contactId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string[] properties = [], GetCrmV3ObjectsContactsContactIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a contact by ID
     # 
@@ -766,7 +767,7 @@
 
     # Retrieve a page of contacts
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsContactsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsContactsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new contact
     # 
`````

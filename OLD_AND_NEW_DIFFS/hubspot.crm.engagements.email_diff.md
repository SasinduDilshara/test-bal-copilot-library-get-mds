# hubspot.crm.engagements.email — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagements.email` |
| **Old file** | `hubspot.crm.engagements.email/old/ballerinax_hubspot.crm.engagements.email.bal.txt` |
| **New file** | `hubspot.crm.engagements.email/new/ballerinax_hubspot.crm.engagements.email.bal.txt` |
| **Old lines** | 777 |
| **New lines** | 778 |
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
| 1 | 306–312 | 306–312 | Types | +1 | −1 |
| 2 | 343–349 | 343–349 | Types | +1 | −1 |
| 3 | 362–368 | 362–368 | Types | +1 | −1 |
| 4 | 410–416 | 410–416 | Types | +1 | −1 |
| 5 | 437–443 | 437–443 | Types | +1 | −1 |
| 6 | 530–536 | 530–536 | Types | +1 | −1 |
| 7 | 539–544 | 539–545 | Types | +1 | −0 |
| 8 | 594–600 | 595–601 | Types | +1 | −1 |
| 9 | 611–617 | 612–618 | Types | +1 | −1 |
| 10 | 663–669 | 664–670 | Types | +1 | −1 |
| 11 | 671–677 | 672–678 | Types | +1 | −1 |
| 12 | 719–725 | 720–726 | Types | +1 | −1 |
| 13 | 733–743 | 734–744 | Client | +2 | −2 |
| 14 | 745–751 | 746–752 | Client | +1 | −1 |
| 15 | 761–767 | 762–768 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagements.email/old/ballerinax_hubspot.crm.engagements.email.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagements.email/new/ballerinax_hubspot.crm.engagements.email.bal.txt	2026-08-12 13:19:19
@@ -306,7 +306,7 @@
     # Category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier specifying the type of association
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -343,7 +343,7 @@
     # Timestamp when the email record was archived
     string archivedAt?;
     # Map of email properties to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.engagements.email:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the email record
     string id;
     # Key-value map of email properties and their current values
@@ -362,7 +362,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated the value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The actual property value recorded at the given timestamp
     string value;
     # Datetime when the value was recorded or last updated
@@ -410,7 +410,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -437,7 +437,7 @@
     # Indicates whether the object was newly created by the upsert
     boolean 'new;
     # A map of property values including their historical change records
-    record {|ballerinax/hubspot.crm.engagements.email:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the email object
     string id;
     # A map of the email object's property names to their current values
@@ -530,7 +530,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of email records matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of email objects returned in the current page
@@ -539,6 +539,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -594,7 +595,7 @@
     # Full-text search query string to filter email results
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -611,7 +612,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing
@@ -663,7 +664,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM objects grouped by association type
-    record {|ballerinax/hubspot.crm.engagements.email:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the email record was created
     string createdAt;
     # Indicates whether the email record has been archived
@@ -671,7 +672,7 @@
     # Timestamp indicating when the email record was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.engagements.email:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the email record
     string id;
     # Key-value map of the email record's current property values
@@ -719,7 +720,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -733,11 +734,11 @@
 
     # Read a batch of emails by internal ID, or unique property values
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsEmailsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsEmailsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Read an Object identified by `{emailId}`. `{emailId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param
     # 
-    resource function get [string emailId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsEmailsEmailIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string emailId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsEmailsEmailIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Move an email to the recycling bin
     # 
@@ -745,7 +746,7 @@
 
     # Partially update an email by ID
     # 
-    resource function patch [string emailId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsEmailsEmailIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string emailId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsEmailsEmailIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of emails by ID
     # 
@@ -761,7 +762,7 @@
 
     # Retrieve a page of emails
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsEmailsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsEmailsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new email object
     # 
`````

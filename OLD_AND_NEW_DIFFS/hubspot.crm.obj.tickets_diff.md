# hubspot.crm.obj.tickets — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.tickets` |
| **Old file** | `hubspot.crm.obj.tickets/old/ballerinax_hubspot.crm.obj.tickets.bal.txt` |
| **New file** | `hubspot.crm.obj.tickets/new/ballerinax_hubspot.crm.obj.tickets.bal.txt` |
| **Old lines** | 786 |
| **New lines** | 787 |
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
| 4 | 397–403 | 397–403 | Types | +1 | −1 |
| 5 | 424–430 | 424–430 | Types | +1 | −1 |
| 6 | 510–516 | 510–516 | Types | +1 | −1 |
| 7 | 527–533 | 527–533 | Types | +1 | −1 |
| 8 | 536–541 | 536–542 | Types | +1 | −0 |
| 9 | 591–597 | 592–598 | Types | +1 | −1 |
| 10 | 608–614 | 609–615 | Types | +1 | −1 |
| 11 | 660–666 | 661–667 | Types | +1 | −1 |
| 12 | 668–674 | 669–675 | Types | +1 | −1 |
| 13 | 738–748 | 739–749 | Client | +2 | −2 |
| 14 | 750–756 | 751–757 | Client | +1 | −1 |
| 15 | 770–776 | 771–777 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.tickets/old/ballerinax_hubspot.crm.obj.tickets.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.tickets/new/ballerinax_hubspot.crm.obj.tickets.bal.txt	2026-08-12 13:19:19
@@ -285,7 +285,7 @@
     # Category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory?;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId?;
+    int:Signed32 associationTypeId?;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -322,7 +322,7 @@
     # Timestamp when the ticket was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.tickets:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the ticket
     string id;
     # Map of ticket property names to their current values
@@ -341,7 +341,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated this property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value at the recorded timestamp
     string value;
     # Datetime when this property value was recorded
@@ -397,7 +397,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -424,7 +424,7 @@
     # Indicates whether the ticket was newly created by the upsert
     boolean 'new;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.tickets:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the upserted ticket object
     string id;
     # Key-value map of ticket property names and their values
@@ -510,7 +510,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of tickets matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination object providing a cursor for forward navigation
     ForwardPaging paging?;
     # Array of ticket objects returned in the current page
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
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -591,7 +592,7 @@
     # Full-text search query string to match against ticket properties
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -608,7 +609,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation started processing
@@ -660,7 +661,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated object collections keyed by association type
-    record {|ballerinax/hubspot.crm.obj.tickets:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the ticket was created
     string createdAt;
     # Indicates whether the ticket has been archived
@@ -668,7 +669,7 @@
     # Timestamp indicating when the ticket was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.obj.tickets:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the ticket object
     string id;
     # Map of ticket property names to their current string values
@@ -738,11 +739,11 @@
 
     # Read tickets by ID or property
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsTicketsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsTicketsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a ticket by ID
     # 
-    resource function get [string ticketId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTicketsTicketIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string ticketId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsTicketsTicketIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a ticket by ID
     # 
@@ -750,7 +751,7 @@
 
     # Update a ticket by ID
     # 
-    resource function patch [string ticketId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsTicketsTicketIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string ticketId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsTicketsTicketIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Merge two tickets with same type
     # 
@@ -770,7 +771,7 @@
 
     # List a page of tickets
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsTicketsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsTicketsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a new ticket
     # 
`````

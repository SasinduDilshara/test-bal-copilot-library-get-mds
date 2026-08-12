# hubspot.crm.engagements.communications — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.engagements.communications` |
| **Old file** | `hubspot.crm.engagements.communications/old/ballerinax_hubspot.crm.engagements.communications.bal.txt` |
| **New file** | `hubspot.crm.engagements.communications/new/ballerinax_hubspot.crm.engagements.communications.bal.txt` |
| **Old lines** | 772 |
| **New lines** | 773 |
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
| 4 | 411–417 | 411–417 | Types | +1 | −1 |
| 5 | 438–444 | 438–444 | Types | +1 | −1 |
| 6 | 524–530 | 524–530 | Types | +1 | −1 |
| 7 | 533–538 | 533–539 | Types | +1 | −0 |
| 8 | 588–594 | 589–595 | Types | +1 | −1 |
| 9 | 605–611 | 606–612 | Types | +1 | −1 |
| 10 | 639–645 | 640–646 | Types | +1 | −1 |
| 11 | 659–665 | 660–666 | Types | +1 | −1 |
| 12 | 667–673 | 668–674 | Types | +1 | −1 |
| 13 | 728–738 | 729–739 | Client | +2 | −2 |
| 14 | 740–746 | 741–747 | Client | +1 | −1 |
| 15 | 756–762 | 757–763 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.engagements.communications/old/ballerinax_hubspot.crm.engagements.communications.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.engagements.communications/new/ballerinax_hubspot.crm.engagements.communications.bal.txt	2026-08-12 13:19:19
@@ -306,7 +306,7 @@
     # Source category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED.
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier specifying the type of association.
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string.
@@ -343,7 +343,7 @@
     # Timestamp when the communication record was archived.
     string archivedAt?;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagements.communications:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the communication record.
     string id;
     # Map of communication property names to their current values.
@@ -362,7 +362,7 @@
     # Human-readable label describing the value's source.
     string sourceLabel?;
     # ID of the user who last updated this value.
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value as a string.
     string value;
     # Timestamp of when this value was last updated.
@@ -411,7 +411,7 @@
     # Timestamp when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested.
     string requestedAt?;
     # Timestamp when the batch operation began processing.
@@ -438,7 +438,7 @@
     # Indicates whether the object was newly created by the upsert.
     boolean 'new;
     # Map of property names to their historical values with timestamps.
-    record {|ballerinax/hubspot.crm.engagements.communications:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the communication object.
     string id;
     # Map of property names to their current values for the object.
@@ -524,7 +524,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of communication records matching the request.
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation.
     ForwardPaging paging?;
     # Array of communication objects returned in the current page.
@@ -533,6 +533,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -588,7 +589,7 @@
     # Full-text search query string to filter communications.
     string query?;
     # Maximum number of results to return per page.
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Pagination cursor token for the next page of results.
     string after?;
     # List of property names to sort results by.
@@ -605,7 +606,7 @@
     # Timestamp indicating when the batch operation completed.
     string completedAt;
     # Total number of errors encountered during the batch operation.
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested.
     string requestedAt?;
     # Timestamp indicating when the batch operation started processing.
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
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM object collections keyed by association type.
-    record {|ballerinax/hubspot.crm.engagements.communications:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the communication object was created.
     string createdAt;
     # Indicates whether the communication object is archived.
@@ -667,7 +668,7 @@
     # Timestamp indicating when the communication object was archived.
     string archivedAt?;
     # Map of property value histories, each containing timestamped prior values.
-    record {|ballerinax/hubspot.crm.engagements.communications:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the communication object.
     string id;
     # Key-value map of the communication object's current property values.
@@ -728,11 +729,11 @@
 
     # Retrieve a batch of messages
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsCommunicationsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsCommunicationsBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a message
     # 
-    resource function get [string communicationId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCommunicationsCommunicationIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string communicationId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsCommunicationsCommunicationIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a message
     # 
@@ -740,7 +741,7 @@
 
     # Update a message
     # 
-    resource function patch [string communicationId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsCommunicationsCommunicationIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string communicationId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsCommunicationsCommunicationIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of messages
     # 
@@ -756,7 +757,7 @@
 
     # Retrieve messages
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCommunicationsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsCommunicationsGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a communication
     # 
`````

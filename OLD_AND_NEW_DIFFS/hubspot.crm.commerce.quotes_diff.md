# hubspot.crm.commerce.quotes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.commerce.quotes` |
| **Old file** | `hubspot.crm.commerce.quotes/old/ballerinax_hubspot.crm.commerce.quotes.bal.txt` |
| **New file** | `hubspot.crm.commerce.quotes/new/ballerinax_hubspot.crm.commerce.quotes.bal.txt` |
| **Old lines** | 792 |
| **New lines** | 793 |
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
| 1 | 304–310 | 304–310 | Types | +1 | −1 |
| 2 | 324–330 | 324–330 | Types | +1 | −1 |
| 3 | 358–364 | 358–364 | Types | +1 | −1 |
| 4 | 377–383 | 377–383 | Types | +1 | −1 |
| 5 | 426–432 | 426–432 | Types | +1 | −1 |
| 6 | 453–459 | 453–459 | Types | +1 | −1 |
| 7 | 539–545 | 539–545 | Types | +1 | −1 |
| 8 | 548–553 | 548–554 | Types | +1 | −0 |
| 9 | 617–623 | 618–624 | Types | +1 | −1 |
| 10 | 634–640 | 635–641 | Types | +1 | −1 |
| 11 | 686–692 | 687–693 | Types | +1 | −1 |
| 12 | 694–700 | 695–701 | Types | +1 | −1 |
| 13 | 748–758 | 749–759 | Client | +2 | −2 |
| 14 | 760–766 | 761–767 | Client | +1 | −1 |
| 15 | 776–782 | 777–783 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.commerce.quotes/old/ballerinax_hubspot.crm.commerce.quotes.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.commerce.quotes/new/ballerinax_hubspot.crm.commerce.quotes.bal.txt	2026-08-12 13:19:19
@@ -304,7 +304,7 @@
     # The category of the association: HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Represents a public object identifier containing a unique ID string
@@ -324,7 +324,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -358,7 +358,7 @@
     # Timestamp when the quote was archived
     string archivedAt?;
     # Map of quote property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.quotes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the quote object
     string id;
     # Map of quote property names to their current values
@@ -377,7 +377,7 @@
     # Human-readable label describing the value's source
     string sourceLabel?;
     # ID of the user who last updated the value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # The property value recorded at the associated timestamp
     string value;
     # Datetime when the value was recorded or last updated
@@ -426,7 +426,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch request was received
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -453,7 +453,7 @@
     # Indicates whether the object was newly created by the upsert
     boolean 'new;
     # A map of property values including their historical change records
-    record {|ballerinax/hubspot.crm.commerce.quotes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # The unique identifier of the upserted object
     string id;
     # A map of the object's current property names and their values
@@ -539,7 +539,7 @@
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
     # Total number of quotes matching the request
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only cursor-based navigation
     ForwardPaging paging?;
     # Array of quote objects returned in the current page
@@ -548,6 +548,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -617,7 +618,7 @@
     # Full-text search query string to filter quotes
     string query?;
     # Maximum number of results to return per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Pagination cursor token for retrieving the next page of results
     string after?;
     # List of property names to sort results by
@@ -634,7 +635,7 @@
     # Timestamp indicating when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp indicating when the batch operation was requested
     string requestedAt?;
     # Timestamp indicating when the batch operation began processing
@@ -686,7 +687,7 @@
 
 type SimplePublicObjectWithAssociations record {
     # Map of associated CRM object types to their related record collections
-    record {|ballerinax/hubspot.crm.commerce.quotes:2.0.2:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     # Timestamp indicating when the quote was created
     string createdAt;
     # Indicates whether the quote has been archived
@@ -694,7 +695,7 @@
     # Timestamp indicating when the quote was archived
     string archivedAt?;
     # Map of property names to their historical values with timestamps
-    record {|ballerinax/hubspot.crm.commerce.quotes:2.0.2:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     # Unique identifier of the quote object
     string id;
     # Key-value map of the quote's current property names and values
@@ -748,11 +749,11 @@
 
     # Read a batch of quotes
     # 
-    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsQuotesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsQuotesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Retrieve a quote by ID
     # 
-    resource function get [string quoteId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsQuotesQuoteIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get [string quoteId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsQuotesQuoteIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive a quote by ID
     # 
@@ -760,7 +761,7 @@
 
     # Partially update a quote
     # 
-    resource function patch [string quoteId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsQuotesQuoteIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch [string quoteId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsQuotesQuoteIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Archive a batch of quotes by ID
     # 
@@ -776,7 +777,7 @@
 
     # List a page of quotes
     # 
-    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsQuotesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsQuotesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create a quote
     # 
`````

# hubspot.crm.associations — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.associations` |
| **Old file** | `hubspot.crm.associations/old/ballerinax_hubspot.crm.associations.bal.txt` |
| **New file** | `hubspot.crm.associations/new/ballerinax_hubspot.crm.associations.bal.txt` |
| **Old lines** | 681 |
| **New lines** | 682 |
| **Lines added** | 10 |
| **Lines removed** | 9 |
| **Hunks** | 10 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 8 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 278–284 | 278–284 | Types | +1 | −1 |
| 2 | 289–295 | 289–295 | Types | +1 | −1 |
| 3 | 352–358 | 352–358 | Types | +1 | −1 |
| 4 | 415–421 | 415–421 | Types | +1 | −1 |
| 5 | 453–458 | 453–459 | Types | +1 | −0 |
| 6 | 508–514 | 509–515 | Types | +1 | −1 |
| 7 | 580–586 | 581–587 | Types | +1 | −1 |
| 8 | 601–607 | 602–608 | Types | +1 | −1 |
| 9 | 629–635 | 630–636 | Types | +1 | −1 |
| 10 | 673–679 | 674–680 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.associations/old/ballerinax_hubspot.crm.associations.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.associations/new/ballerinax_hubspot.crm.associations.bal.txt	2026-08-12 13:19:19
@@ -278,7 +278,7 @@
     # Email address of the user who requested the report
     string userEmail;
     # Numeric ID of the user who requested the report
-    ballerina/lang.int:0.0.0:Signed32 userId;
+    int:Signed32 userId;
     # Represents a date-time value with timezone offset and date-only flag
     DateTime enqueueTime;
 };
@@ -289,7 +289,7 @@
     # Indicates whether the value represents a date without time
     boolean dateOnly;
     # Timezone offset in minutes from UTC
-    ballerina/lang.int:0.0.0:Signed32 timeZoneShift;
+    int:Signed32 timeZoneShift;
     # The numeric date-time value, typically as a Unix timestamp
     int value;
 };
@@ -352,7 +352,7 @@
 
 type AssociationSpecWithLabel record {
     # Numeric identifier for the association type
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # Optional human-readable label describing the association type
     string? label?;
     # Defines the origin of the association type
@@ -415,7 +415,7 @@
     # Category indicating who defined the association type
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory;
     # Numeric identifier for the specific association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
 };
 
 # Batch response containing labeled associations between object pairs with processing status
@@ -453,6 +453,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -508,7 +509,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation started processing
@@ -580,7 +581,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during batch processing
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation started processing
@@ -601,7 +602,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch request was received
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -629,7 +630,7 @@
 
 type GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries record {
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
@@ -673,7 +674,7 @@
 
     # List associations by type
     # 
-    resource function get objects/[string objectType]/[string objectId]/associations/[string toObjectType](map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", anydata Additional Values, GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries queries) returns CollectionResponseMultiAssociatedObjectWithLabelForwardPaging|error;
+    resource function get objects/[string objectType]/[string objectId]/associations/[string toObjectType](map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", GetObjectsObjectTypeObjectIdAssociationsToObjectTypeGetPageQueries queries) returns CollectionResponseMultiAssociatedObjectWithLabelForwardPaging|error;
 
     # Create default association
     # 
`````

# hubspot.crm.obj.companies — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.companies` |
| **Old file** | `hubspot.crm.obj.companies/old/ballerinax_hubspot.crm.obj.companies.bal.txt` |
| **New file** | `hubspot.crm.obj.companies/new/ballerinax_hubspot.crm.obj.companies.bal.txt` |
| **Old lines** | 648 |
| **New lines** | 649 |
| **Lines added** | 16 |
| **Lines removed** | 15 |
| **Hunks** | 13 |

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
| 1 | 219–225 | 219–225 | Types | +1 | −1 |
| 2 | 306–312 | 306–312 | Types | +1 | −1 |
| 3 | 329–335 | 329–335 | Types | +1 | −1 |
| 4 | 340–346 | 340–346 | Types | +1 | −1 |
| 5 | 373–379 | 373–379 | Types | +1 | −1 |
| 6 | 388–394 | 388–394 | Types | +1 | −1 |
| 7 | 455–467 | 455–468 | Types | +2 | −1 |
| 8 | 521–527 | 522–528 | Types | +1 | −1 |
| 9 | 531–537 | 532–538 | Types | +1 | −1 |
| 10 | 554–564 | 555–565 | Types | +2 | −2 |
| 11 | 602–612 | 603–613 | Client | +2 | −2 |
| 12 | 614–620 | 615–621 | Client | +1 | −1 |
| 13 | 634–640 | 635–641 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.companies/old/ballerinax_hubspot.crm.obj.companies.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.companies/new/ballerinax_hubspot.crm.obj.companies.bal.txt	2026-08-12 13:19:19
@@ -219,7 +219,7 @@
     # A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request
     string[] propertiesWithHistory?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored
@@ -306,7 +306,7 @@
 
 type AssociationSpec record {
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" associationCategory?;
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId?;
+    int:Signed32 associationTypeId?;
 };
 
 
@@ -329,7 +329,7 @@
     string createdAt;
     boolean archived?;
     string archivedAt?;
-    record {|ballerinax/hubspot.crm.obj.companies:2.0.1:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     string id;
     record {|string?...;|} properties;
     string updatedAt;
@@ -340,7 +340,7 @@
     string sourceId?;
     string sourceType;
     string sourceLabel?;
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     string value;
     string timestamp;
 };
@@ -373,7 +373,7 @@
 
 type BatchResponseSimplePublicUpsertObjectWithErrors record {
     string completedAt;
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     string requestedAt?;
     string startedAt;
     record {|string...;|} links?;
@@ -388,7 +388,7 @@
     boolean archived?;
     string archivedAt?;
     boolean 'new;
-    record {|ballerinax/hubspot.crm.obj.companies:2.0.1:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     string id;
     record {|string...;|} properties;
     string updatedAt;
@@ -455,13 +455,14 @@
 
 
 type CollectionResponseWithTotalSimplePublicObjectForwardPaging record {
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     ForwardPaging paging?;
     SimplePublicObject[] results;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -521,7 +522,7 @@
 
 type PublicObjectSearchRequest record {
     string query?;
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     string after?;
     string[] sorts?;
     string[] properties?;
@@ -531,7 +532,7 @@
 
 type BatchResponseSimplePublicObjectWithErrors record {
     string completedAt;
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     string requestedAt?;
     string startedAt;
     record {|string...;|} links?;
@@ -554,11 +555,11 @@
 
 
 type SimplePublicObjectWithAssociations record {
-    record {|ballerinax/hubspot.crm.obj.companies:2.0.1:CollectionResponseAssociatedId...;|} associations?;
+    record {|CollectionResponseAssociatedId...;|} associations?;
     string createdAt;
     boolean archived?;
     string archivedAt?;
-    record {|ballerinax/hubspot.crm.obj.companies:2.0.1:ValueWithTimestamp[]...;|} propertiesWithHistory?;
+    record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;
     string id;
     record {|string?...;|} properties;
     string updatedAt;
@@ -602,11 +603,11 @@
 
     # Read a batch of companies by internal ID, or unique property values
     # 
-    resource function post companies/batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PostCrmV3ObjectsCompaniesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
+    resource function post companies/batch/read(BatchReadInputSimplePublicObjectId payload, map<string|string[]> headers = {}, boolean archived = false, PostCrmV3ObjectsCompaniesBatchReadReadQueries queries) returns BatchResponseSimplePublicObject|BatchResponseSimplePublicObjectWithErrors|error;
 
     # Read
     # 
-    resource function get companies/[string companyId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCompaniesCompanyIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
+    resource function get companies/[string companyId](map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], string idProperty = "", string[] properties = [], GetCrmV3ObjectsCompaniesCompanyIdGetByIdQueries queries) returns SimplePublicObjectWithAssociations|error;
 
     # Archive
     # 
@@ -614,7 +615,7 @@
 
     # Update
     # 
-    resource function patch companies/[string companyId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", anydata Additional Values, PatchCrmV3ObjectsCompaniesCompanyIdUpdateQueries queries) returns SimplePublicObject|error;
+    resource function patch companies/[string companyId](SimplePublicObjectInput payload, map<string|string[]> headers = {}, string idProperty = "", PatchCrmV3ObjectsCompaniesCompanyIdUpdateQueries queries) returns SimplePublicObject|error;
 
     # Merge two companies with same type
     # 
@@ -634,7 +635,7 @@
 
     # List
     # 
-    resource function get companies(map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], anydata Additional Values, GetCrmV3ObjectsCompaniesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
+    resource function get companies(map<string|string[]> headers = {}, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsCompaniesGetPageQueries queries) returns CollectionResponseSimplePublicObjectWithAssociationsForwardPaging|error;
 
     # Create
     # 
`````

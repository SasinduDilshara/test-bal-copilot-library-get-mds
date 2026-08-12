# scim — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `scim` |
| **Old file** | `scim/old/ballerinax_scim.bal.txt` |
| **New file** | `scim/new/ballerinax_scim.bal.txt` |
| **Old lines** | 917 |
| **New lines** | 918 |
| **Lines added** | 20 |
| **Lines removed** | 19 |
| **Hunks** | 12 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 16 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type OperationObBulk`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 108–118 | 108–118 | Types | +2 | −2 |
| 2 | 171–179 | 171–179 | Types | +2 | −2 |
| 3 | 386–391 | 386–392 | Types | +1 | −0 |
| 4 | 592–598 | 593–599 | Types | +1 | −1 |
| 5 | 641–651 | 642–652 | Types | +2 | −2 |
| 6 | 707–713 | 708–714 | Types | +1 | −1 |
| 7 | 727–733 | 728–734 | Types | +1 | −1 |
| 8 | 849–859 | 850–860 | Client | +2 | −2 |
| 9 | 861–871 | 862–872 | Client | +2 | −2 |
| 10 | 873–887 | 874–888 | Client | +3 | −3 |
| 11 | 889–899 | 890–900 | Client | +2 | −2 |
| 12 | 901–907 | 902–908 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- scim/old/ballerinax_scim.bal.txt	2026-08-12 12:57:30
+++ scim/new/ballerinax_scim.bal.txt	2026-08-12 13:19:19
@@ -108,11 +108,11 @@
     # Filter expression for filtering
     string filter?;
     # The 1-based index of the first query result
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    int:Signed32 startIndex?;
     # The name of the user store where filtering needs to be applied.
     string domain?;
     # Specifies the desired maximum number of query results per page.
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
     # SCIM defined attributes parameter.
     string attributes?;
     # SCIM defined excludedAttribute parameter.
@@ -171,9 +171,9 @@
     # The name of the user store where filtering needs to be applied.
     string domain?;
     # The 1-based index of the first query result
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    int:Signed32 startIndex?;
     # Specifies the desired maximum number of query results per page. </br>(For organizations created on or after November 19, 2024, a threshold value of 100 will be applied to the count parameter. To fetch more users, use pagination.)
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
 };
 
 
@@ -386,6 +386,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:OAuth2ClientCredentialsGrantConfig auth; // Special Agent Note: OAuth2ClientCredentialsGrantConfig FROM ballerina/http package
@@ -592,7 +593,7 @@
     string value;
 };
 
-type Bulk_body ballerinax/scim:1.0.2:BulkUserCreateObject|ballerinax/scim:1.0.2:BulkUserUpdateObject|ballerinax/scim:1.0.2:BulkUserReplaceObject|ballerinax/scim:1.0.2:BulkUserDeleteObject|ballerinax/scim:1.0.2:BulkGroupCreateObject|ballerinax/scim:1.0.2:BulkGroupUpdateObject|ballerinax/scim:1.0.2:BulkGroupReplaceObject|ballerinax/scim:1.0.2:BulkGroupDeleteObject;
+type Bulk_body BulkUserCreateObject|BulkUserUpdateObject|BulkUserReplaceObject|BulkUserDeleteObject|BulkGroupCreateObject|BulkGroupUpdateObject|BulkGroupReplaceObject|BulkGroupDeleteObject;
 
 
 type GroupSearchResponseObject record {
@@ -641,11 +642,11 @@
     # The expression used for filtering. Supported filters are ‘Ew’, ‘Eq’, ‘Co’, ‘Sw’, ‘Ne’ and ‘and’.
     string filter?;
     # The 1-based index of the first query result
-    ballerina/lang.int:0.0.0:Signed32 startIndex?;
+    int:Signed32 startIndex?;
     # The name of the user store where filtering needs to be applied.
     string domain?;
     # Specifies the desired maximum number of query results per page.
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
     # SCIM defined attributes parameter.
     string attributes?;
     # SCIM defined excludedAttribute parameter.
@@ -707,7 +708,7 @@
     boolean verifyEmail?;
 };
 
-type Users_body ballerinax/scim:1.0.2:UserObject|ballerinax/scim:1.0.2:UserObjectPassInvite;
+type Users_body UserObject|UserObjectPassInvite;
 
 
 type OperationMeItem_value record {
@@ -727,7 +728,7 @@
     OperationMeItem_value value?;
 };
 
-// Unknown type: OperationObBulk
+type OperationObBulk OperationObBulk_inner[];
 
 
 type ResourceTypeResponse record {
@@ -849,11 +850,11 @@
 
     # Filter Users
     # 
-    resource function get Users(map<string|string[]> headers = {}, string filter = "", int:Signed32 startIndex = 0, string domain = "", int:Signed32 count = 0, string attributes = "", string excludedAttributes = "", anydata Additional Values, GetUserQueries queries) returns UserObjectListResponseObject|error;
+    resource function get Users(map<string|string[]> headers = {}, string filter = "", int:Signed32 startIndex = 0, string domain = "", int:Signed32 count = 0, string attributes = "", string excludedAttributes = "", GetUserQueries queries) returns UserObjectListResponseObject|error;
 
     # Create User
     # 
-    resource function post Users(Users_body payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, CreateUserQueries queries) returns UserResponseObject|error;
+    resource function post Users(Users_body payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", CreateUserQueries queries) returns UserResponseObject|error;
 
     # Search Users
     # 
@@ -861,11 +862,11 @@
 
     # Get User by ID
     # 
-    resource function get Users/[string id](map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, GetUserByIdQueries queries) returns UserResponseObject|error;
+    resource function get Users/[string id](map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", GetUserByIdQueries queries) returns UserResponseObject|error;
 
     # Update User - PUT
     # 
-    resource function put Users/[string id](UserUpdateObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, UpdateUserQueries queries) returns UserResponseObject|error;
+    resource function put Users/[string id](UserUpdateObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", UpdateUserQueries queries) returns UserResponseObject|error;
 
     # Delete User by ID
     # 
@@ -873,15 +874,15 @@
 
     # Update User - PATCH
     # 
-    resource function patch Users/[string id](PatchOperationInput payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, PatchUserQueries queries) returns UserResponseObject|error;
+    resource function patch Users/[string id](PatchOperationInput payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", PatchUserQueries queries) returns UserResponseObject|error;
 
     # Filter Groups
     # 
-    resource function get Groups(map<string|string[]> headers = {}, string filter = "", int:Signed32 startIndex = 0, string domain = "", int:Signed32 count = 0, string attributes = "", string excludedAttributes = "", anydata Additional Values, GetGroupQueries queries) returns GroupsListResponseObject|error;
+    resource function get Groups(map<string|string[]> headers = {}, string filter = "", int:Signed32 startIndex = 0, string domain = "", int:Signed32 count = 0, string attributes = "", string excludedAttributes = "", GetGroupQueries queries) returns GroupsListResponseObject|error;
 
     # Create Group
     # 
-    resource function post Groups(GroupRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, CreateGroupQueries queries) returns GroupResponseObject|error;
+    resource function post Groups(GroupRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", CreateGroupQueries queries) returns GroupResponseObject|error;
 
     # Search Groups
     # 
@@ -889,11 +890,11 @@
 
     # Get Group by ID
     # 
-    resource function get Groups/[string id](map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, GetGroupByIdQueries queries) returns GroupResponseObject|error;
+    resource function get Groups/[string id](map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", GetGroupByIdQueries queries) returns GroupResponseObject|error;
 
     # Update Group - PUT
     # 
-    resource function put Groups/[string id](GroupPutRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, UpdateGroupQueries queries) returns GroupPutResponseObject|error;
+    resource function put Groups/[string id](GroupPutRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", UpdateGroupQueries queries) returns GroupPutResponseObject|error;
 
     # Delete Group
     # 
@@ -901,7 +902,7 @@
 
     # Update Group - PATCH
     # 
-    resource function patch Groups/[string id](PatchGroupOperationRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", anydata Additional Values, PatchGroupQueries queries) returns PatchGroupOperationResponseObject|error;
+    resource function patch Groups/[string id](PatchGroupOperationRequestObject payload, map<string|string[]> headers = {}, string attributes = "", string excludedAttributes = "", PatchGroupQueries queries) returns PatchGroupOperationResponseObject|error;
 
     # Create/Update/Replace/Delete SCIM Resources (Users/ Groups) in Bulk
     # 
`````

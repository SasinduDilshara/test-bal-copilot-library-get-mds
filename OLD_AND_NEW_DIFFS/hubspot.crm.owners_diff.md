# hubspot.crm.owners — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.owners` |
| **Old file** | `hubspot.crm.owners/old/ballerinax_hubspot.crm.owners.bal.txt` |
| **New file** | `hubspot.crm.owners/new/ballerinax_hubspot.crm.owners.bal.txt` |
| **Old lines** | 362 |
| **New lines** | 365 |
| **Lines added** | 8 |
| **Lines removed** | 5 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 242–252 | 242–252 | Types | +2 | −2 |
| 2 | 282–289 | 282–291 | Types | +2 | −0 |
| 3 | 293–299 | 295–301 | Types | +1 | −1 |
| 4 | 302–307 | 304–310 | Types | +1 | −0 |
| 5 | 354–362 | 357–365 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- hubspot.crm.owners/old/ballerinax_hubspot.crm.owners.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.owners/new/ballerinax_hubspot.crm.owners.bal.txt	2026-08-12 13:19:19
@@ -242,11 +242,11 @@
     # The unique identifier for the owner
     string id;
     # The unique identifier for the owner, including inactive owners
-    ballerina/lang.int:0.0.0:Signed32 userIdIncludingInactive?;
+    int:Signed32 userIdIncludingInactive?;
     # The type of owner
     "PERSON"|"QUEUE" 'type;
     # The unique identifier for the owner
-    ballerina/lang.int:0.0.0:Signed32 userId?;
+    int:Signed32 userId?;
     # The email address of the owner
     string email?;
     # The date and time the owner was last updated
@@ -282,8 +282,10 @@
 
 type ApiKeysConfig record {
     # Used to authenticate requests from legacy private apps
+    @display {label: "", kind: "password"}
     string privateAppLegacy;
     # Used to authenticate requests from private apps
+    @display {label: "", kind: "password"}
     string privateApp;
 };
 
@@ -293,7 +295,7 @@
     # Whether to return only results that have been archived
     boolean archived?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # Filter by email address (optional)
@@ -302,6 +304,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -354,9 +357,9 @@
 
     # Get a page of owners
     # 
-    resource function get (map<string|string[]> headers = {}, boolean archived = false, int:Signed32 limit = 0, string after = "", string email = "", anydata Additional Values, GetCrmV3OwnersGetPageQueries queries) returns CollectionResponsePublicOwnerForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, boolean archived = false, int:Signed32 limit = 0, string after = "", string email = "", GetCrmV3OwnersGetPageQueries queries) returns CollectionResponsePublicOwnerForwardPaging|error;
 
     # Read owner by ID or userId
     # 
-    resource function get [int:Signed32 ownerId](map<string|string[]> headers = {}, boolean archived = false, "id"|"userId" idProperty = "id", anydata Additional Values, GetCrmV3OwnersOwnerIdGetByIdQueries queries) returns PublicOwner|error;
+    resource function get [int:Signed32 ownerId](map<string|string[]> headers = {}, boolean archived = false, "id"|"userId" idProperty = "id", GetCrmV3OwnersOwnerIdGetByIdQueries queries) returns PublicOwner|error;
 }
`````

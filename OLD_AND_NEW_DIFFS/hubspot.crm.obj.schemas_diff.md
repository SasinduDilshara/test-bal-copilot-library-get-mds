# hubspot.crm.obj.schemas — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.obj.schemas` |
| **Old file** | `hubspot.crm.obj.schemas/old/ballerinax_hubspot.crm.obj.schemas.bal.txt` |
| **New file** | `hubspot.crm.obj.schemas/new/ballerinax_hubspot.crm.obj.schemas.bal.txt` |
| **Old lines** | 567 |
| **New lines** | 568 |
| **Lines added** | 10 |
| **Lines removed** | 9 |
| **Hunks** | 9 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 7 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 218–227 | 218–227 | Types | +2 | −2 |
| 2 | 267–273 | 267–273 | Types | +1 | −1 |
| 3 | 319–325 | 319–325 | Types | +1 | −1 |
| 4 | 354–360 | 354–360 | Types | +1 | −1 |
| 5 | 378–384 | 378–384 | Types | +1 | −1 |
| 6 | 401–407 | 401–407 | Types | +1 | −1 |
| 7 | 489–494 | 489–495 | Types | +1 | −0 |
| 8 | 539–545 | 540–546 | Client | +1 | −1 |
| 9 | 551–557 | 552–558 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.obj.schemas/old/ballerinax_hubspot.crm.obj.schemas.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.obj.schemas/new/ballerinax_hubspot.crm.obj.schemas.bal.txt	2026-08-12 13:19:19
@@ -218,10 +218,10 @@
     AssociationDefinition[] associations;
     # The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type
     string[] secondaryDisplayProperties?;
-    ballerina/lang.int:0.0.0:Signed32 createdByUserId?;
+    int:Signed32 createdByUserId?;
     string objectTypeId?;
     string description?;
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId?;
+    int:Signed32 updatedByUserId?;
     # An assigned unique ID for the object, including portal ID and object name
     string fullyQualifiedName?;
     # Singular and plural labels for the object. Used in CRM display
@@ -267,7 +267,7 @@
 type Property record {
     boolean hidden?;
     # The order that this property should be displayed in the HubSpot UI relative to other properties for this object type. Properties are displayed in order starting with the lowest positive integer value. A value of -1 will cause the property to be displayed **after** any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the property that will be shown as help text in HubSpot
     string description;
     # Whether the property will display the currency symbol set in the account settings
@@ -319,7 +319,7 @@
     # Hidden options will not be displayed in HubSpot
     boolean hidden;
     # Options are displayed in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the option
     string description?;
     # A human-readable option label that will be shown in HubSpot
@@ -354,7 +354,7 @@
     # Names of properties that will be indexed for this object type in by HubSpot's product search
     string[] searchableProperties?;
     # The ID of the account that this object type is specific to
-    ballerina/lang.int:0.0.0:Signed32 portalId?;
+    int:Signed32 portalId?;
     # The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type
     string primaryDisplayProperty?;
     # A unique name for this object. For internal use only
@@ -378,7 +378,7 @@
     # Hidden options won't be shown in HubSpot
     boolean hidden;
     # Options are shown in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # A description of the option
     string description?;
     # A human-readable option label that will be shown in HubSpot
@@ -401,7 +401,7 @@
     # Controls how the property options will be sorted in the HubSpot UI
     "DISPLAY_ORDER"|"ALPHABETICAL" optionSortStrategy?;
     # The order that this property should be displayed in the HubSpot UI relative to other properties for this object type. Properties are displayed in order starting with the lowest positive integer value. A value of -1 will cause the property to be displayed **after** any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the property that will be shown as help text in HubSpot
     string description?;
     # Whether the property will display the currency symbol in the HubSpot UI
@@ -489,6 +489,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -539,7 +540,7 @@
 
     # Get all schemas
     # 
-    resource function get (map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, GetCrmObjectSchemasV3SchemasGetAllQueries queries) returns CollectionResponseObjectSchemaNoPaging|error;
+    resource function get (map<string|string[]> headers = {}, boolean archived = false, GetCrmObjectSchemasV3SchemasGetAllQueries queries) returns CollectionResponseObjectSchemaNoPaging|error;
 
     # Create a new schema
     # 
@@ -551,7 +552,7 @@
 
     # Delete a schema
     # 
-    resource function delete [string objectType](map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, DeleteCrmObjectSchemasV3SchemasObjectTypeArchiveQueries queries) returns error?;
+    resource function delete [string objectType](map<string|string[]> headers = {}, boolean archived = false, DeleteCrmObjectSchemasV3SchemasObjectTypeArchiveQueries queries) returns error?;
 
     # Update a schema
     # 
`````

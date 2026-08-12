# hubspot.crm.associations.schema — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.associations.schema` |
| **Old file** | `hubspot.crm.associations.schema/old/ballerinax_hubspot.crm.associations.schema.bal.txt` |
| **New file** | `hubspot.crm.associations.schema/new/ballerinax_hubspot.crm.associations.schema.bal.txt` |
| **Old lines** | 581 |
| **New lines** | 582 |
| **Lines added** | 14 |
| **Lines removed** | 13 |
| **Hunks** | 9 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 13 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 243–249 | 243–249 | Types | +1 | −1 |
| 2 | 262–270 | 262–270 | Types | +2 | −2 |
| 3 | 335–341 | 335–341 | Types | +1 | −1 |
| 4 | 361–369 | 361–369 | Types | +2 | −2 |
| 5 | 372–393 | 372–393 | Types | +4 | −4 |
| 6 | 396–402 | 396–402 | Types | +1 | −1 |
| 7 | 405–411 | 405–411 | Types | +1 | −1 |
| 8 | 472–478 | 472–478 | Types | +1 | −1 |
| 9 | 489–494 | 489–495 | Types | +1 | −0 |

---

## Unified diff

`````diff
--- hubspot.crm.associations.schema/old/ballerinax_hubspot.crm.associations.schema.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.associations.schema/new/ballerinax_hubspot.crm.associations.schema.bal.txt	2026-08-12 13:19:19
@@ -243,7 +243,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -262,9 +262,9 @@
 
 type PublicAssociationDefinitionUserConfiguration record {
     # User-enforced maximum number of target objects. Nullable
-    ballerina/lang.int:0.0.0:Signed32? userEnforcedMaxToObjectIds?;
+    int:Signed32? userEnforcedMaxToObjectIds?;
     # The numeric ID identifying the association type
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # Custom display label for the association definition
     string? label?;
     # The origin category of the association definition: HubSpot-defined, user-defined, or integrator-defined
@@ -335,7 +335,7 @@
 
 type PublicAssociationSpec record {
     # Numeric identifier for the association type
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # Category classification of the association type
     string category;
 };
@@ -361,9 +361,9 @@
 
 type PublicAssociationDefinitionConfigurationUpdateResult record {
     # Maximum number of target object IDs enforced for this association type
-    ballerina/lang.int:0.0.0:Signed32 userEnforcedMaxToObjectIds?;
+    int:Signed32 userEnforcedMaxToObjectIds?;
     # Numeric identifier of the association type
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # Category indicating who defined the association type
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" category;
 };
@@ -372,22 +372,22 @@
 
 type PublicAssociationDefinitionConfigurationUpdateRequest record {
     # Numeric identifier of the association type to update
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # The category of the association definition to update
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" category;
     # Maximum number of target objects allowed in this association
-    ballerina/lang.int:0.0.0:Signed32 maxToObjectIds;
+    int:Signed32 maxToObjectIds;
 };
 
 # Request body for creating a configuration for an association definition, specifying its type, category, and object limit
 
 type PublicAssociationDefinitionConfigurationCreateRequest record {
     # The numeric ID of the association type to configure
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # The category of the association definition to configure
     "HUBSPOT_DEFINED"|"USER_DEFINED"|"INTEGRATOR_DEFINED" category;
     # Maximum number of target objects allowed in this association
-    ballerina/lang.int:0.0.0:Signed32 maxToObjectIds;
+    int:Signed32 maxToObjectIds;
 };
 
 # Request body for updating an association definition's label and optional inverse label
@@ -396,7 +396,7 @@
     # The inverse label for the reverse direction of the association
     string inverseLabel?;
     # The numeric ID of the association type to update
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
     # The display label for the association definition. Nullable
     string? label;
 };
@@ -405,7 +405,7 @@
 
 type AssociationSpecWithLabel record {
     # The numeric ID identifying the association type
-    ballerina/lang.int:0.0.0:Signed32 typeId;
+    int:Signed32 typeId;
     # The display label for the association type. Nullable
     string? label?;
     # The category classifying the origin of the association type
@@ -472,7 +472,7 @@
     # Timestamp when the batch update operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch update operation was requested
     string requestedAt?;
     # Timestamp when the batch update operation started processing
@@ -489,6 +489,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
`````

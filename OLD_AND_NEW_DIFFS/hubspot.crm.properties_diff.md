# hubspot.crm.properties — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.properties` |
| **Old file** | `hubspot.crm.properties/old/ballerinax_hubspot.crm.properties.bal.txt` |
| **New file** | `hubspot.crm.properties/new/ballerinax_hubspot.crm.properties.bal.txt` |
| **Old lines** | 575 |
| **New lines** | 576 |
| **Lines added** | 12 |
| **Lines removed** | 11 |
| **Hunks** | 12 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 9 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 240–246 | 240–246 | Types | +1 | −1 |
| 2 | 294–300 | 294–300 | Types | +1 | −1 |
| 3 | 310–316 | 310–316 | Types | +1 | −1 |
| 4 | 320–326 | 320–326 | Types | +1 | −1 |
| 5 | 352–358 | 352–358 | Types | +1 | −1 |
| 6 | 388–394 | 388–394 | Types | +1 | −1 |
| 7 | 414–420 | 414–420 | Types | +1 | −1 |
| 8 | 427–433 | 427–433 | Types | +1 | −1 |
| 9 | 455–461 | 455–461 | Types | +1 | −1 |
| 10 | 477–482 | 477–483 | Types | +1 | −0 |
| 11 | 543–549 | 544–550 | Client | +1 | −1 |
| 12 | 563–569 | 564–570 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.properties/old/ballerinax_hubspot.crm.properties.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.properties/new/ballerinax_hubspot.crm.properties.bal.txt	2026-08-12 13:19:19
@@ -240,7 +240,7 @@
     boolean hidden?;
     PropertyModificationMetadata modificationMetadata?;
     # Properties are shown in order, starting with the lowest positive integer value
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the property that will be shown as help text in HubSpot
     string description;
     # Whether or not the property will display the currency symbol set in the account settings
@@ -294,7 +294,7 @@
     # Hidden options will not be displayed in HubSpot
     boolean hidden;
     # Options are displayed in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the option
     string description?;
     # A human-readable option label that will be shown in HubSpot
@@ -310,7 +310,7 @@
     # The internal property group name, which must be used when referencing the property group via the API
     string name;
     # Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # A human-readable label that will be shown in HubSpot
     string label;
 };
@@ -320,7 +320,7 @@
     # If true, the property won't be visible and can't be used in HubSpot
     boolean hidden?;
     # Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the property that will be shown as help text in HubSpot
     string description?;
     # A human-readable property label that will be shown in HubSpot
@@ -352,7 +352,7 @@
     # Hidden options won't be shown in HubSpot
     boolean hidden;
     # Options are shown in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the option
     string description?;
     # A human-readable option label that will be shown in HubSpot
@@ -388,7 +388,7 @@
     # A list of valid options for the property
     OptionInput[] options?;
     # Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the Property to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A description of the property that will be shown as help text in HubSpot
     string description?;
     # Represents a formula that is used to compute a calculated property
@@ -414,7 +414,7 @@
     # The internal property group name, which must be used when referencing the property group via the API
     string name;
     # Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A human-readable label that will be shown in HubSpot
     string label;
 };
@@ -427,7 +427,7 @@
 
 type BatchResponsePropertyWithErrors record {
     string completedAt;
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     string requestedAt?;
     string startedAt;
     record {|string...;|} links?;
@@ -455,7 +455,7 @@
 
 type PropertyGroupUpdate record {
     # Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values
-    ballerina/lang.int:0.0.0:Signed32 displayOrder?;
+    int:Signed32 displayOrder?;
     # A human-readable label that will be shown in HubSpot
     string label?;
 };
@@ -477,6 +477,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -543,7 +544,7 @@
 
     # Read a property
     # 
-    resource function get [string objectType]/[string propertyName](map<string|string[]> headers = {}, boolean archived = false, string properties = "", anydata Additional Values, GetCrmV3PropertiesObjectTypePropertyNameGetByNameQueries queries) returns Property|error;
+    resource function get [string objectType]/[string propertyName](map<string|string[]> headers = {}, boolean archived = false, string properties = "", GetCrmV3PropertiesObjectTypePropertyNameGetByNameQueries queries) returns Property|error;
 
     # Archive a property
     # 
@@ -563,7 +564,7 @@
 
     # Read all properties
     # 
-    resource function get [string objectType](map<string|string[]> headers = {}, boolean archived = false, string properties = "", anydata Additional Values, GetCrmV3PropertiesObjectTypeGetAllQueries queries) returns CollectionResponsePropertyNoPaging|error;
+    resource function get [string objectType](map<string|string[]> headers = {}, boolean archived = false, string properties = "", GetCrmV3PropertiesObjectTypeGetAllQueries queries) returns CollectionResponsePropertyNoPaging|error;
 
     # Create a property
     # 
`````

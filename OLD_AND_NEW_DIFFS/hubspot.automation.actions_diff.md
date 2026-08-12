# hubspot.automation.actions — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.automation.actions` |
| **Old file** | `hubspot.automation.actions/old/ballerinax_hubspot.automation.actions.bal.txt` |
| **New file** | `hubspot.automation.actions/new/ballerinax_hubspot.automation.actions.bal.txt` |
| **Old lines** | 673 |
| **New lines** | 674 |
| **Lines added** | 13 |
| **Lines removed** | 12 |
| **Hunks** | 11 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 12 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 237–243 | 237–243 | Types | +1 | −1 |
| 2 | 313–319 | 313–319 | Types | +1 | −1 |
| 3 | 358–364 | 358–364 | Types | +1 | −1 |
| 4 | 421–433 | 421–434 | Types | +2 | −1 |
| 5 | 515–521 | 516–522 | Types | +1 | −1 |
| 6 | 557–563 | 558–564 | Types | +1 | −1 |
| 7 | 580–590 | 581–591 | Types | +2 | −2 |
| 8 | 597–603 | 598–604 | Types | +1 | −1 |
| 9 | 617–623 | 618–624 | Client | +1 | −1 |
| 10 | 645–651 | 646–652 | Client | +1 | −1 |
| 11 | 669–673 | 670–674 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.automation.actions/old/ballerinax_hubspot.automation.actions.bal.txt	2026-08-12 12:57:30
+++ hubspot.automation.actions/new/ballerinax_hubspot.automation.actions.bal.txt	2026-08-12 13:19:19
@@ -237,7 +237,7 @@
     # Indicates whether the action is published and available for use.
     boolean published;
     # Localized display labels for the action, keyed by language code.
-    record {|ballerinax/hubspot.automation.actions:2.0.0:PublicActionLabels...;|} labels;
+    record {|PublicActionLabels...;|} labels;
     # List of input fields the action accepts during execution.
     InputFieldDefinition[] inputFields;
     # List of output fields the action returns after execution.
@@ -313,7 +313,7 @@
     # Whether this option is hidden from the user interface.
     boolean hidden;
     # Numeric order in which the option appears in the UI.
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     # Numeric double value associated with the option.
     decimal doubleData;
     # Human-readable description of the option.
@@ -358,7 +358,7 @@
 };
 
 # Defines a field dependency as either a single-field or conditional single-field dependency type.
-type PublicActionDefinitionInputFieldDependencies ballerinax/hubspot.automation.actions:2.0.0:PublicSingleFieldDependency|ballerinax/hubspot.automation.actions:2.0.0:PublicConditionalSingleFieldDependency;
+type PublicActionDefinitionInputFieldDependencies PublicSingleFieldDependency|PublicConditionalSingleFieldDependency;
 
 # Defines a translation rule mapping execution conditions to a display label.
 
@@ -421,13 +421,14 @@
     # Whether to return only results that have been archived
     boolean archived?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -515,7 +516,7 @@
 };
 
 # Input field dependency definition; either a single or conditional single field dependency
-type PublicActionDefinitionEggInputFieldDependencies ballerinax/hubspot.automation.actions:2.0.0:PublicSingleFieldDependency|ballerinax/hubspot.automation.actions:2.0.0:PublicConditionalSingleFieldDependency;
+type PublicActionDefinitionEggInputFieldDependencies PublicSingleFieldDependency|PublicConditionalSingleFieldDependency;
 
 # Represents the Queries record for the operation: get-/{appId}/{definitionId}_getById
 
@@ -557,7 +558,7 @@
     # Options for a public object request, specifying which properties to retrieve.
     PublicObjectRequestOptions objectRequestOptions?;
     # Localized display labels for the action, keyed by language code.
-    record {|ballerinax/hubspot.automation.actions:2.0.0:PublicActionLabels...;|} labels;
+    record {|PublicActionLabels...;|} labels;
 };
 
 # Partial update payload for modifying an existing custom action definition.
@@ -580,11 +581,11 @@
     # Options for a public object request, specifying which properties to retrieve.
     PublicObjectRequestOptions objectRequestOptions?;
     # Localized display labels for the action, keyed by language code.
-    record {|ballerinax/hubspot.automation.actions:2.0.0:PublicActionLabels...;|} labels?;
+    record {|PublicActionLabels...;|} labels?;
 };
 
 # A field dependency rule; either a single-field or conditional single-field dependency.
-type PublicActionDefinitionPatchInputFieldDependencies ballerinax/hubspot.automation.actions:2.0.0:PublicSingleFieldDependency|ballerinax/hubspot.automation.actions:2.0.0:PublicConditionalSingleFieldDependency;
+type PublicActionDefinitionPatchInputFieldDependencies PublicSingleFieldDependency|PublicConditionalSingleFieldDependency;
 
 # A batch of callback completion requests to resolve multiple pending action callbacks.
 
@@ -597,7 +598,7 @@
 
 type GetAppIdDefinitionIdRevisionsGetPageQueries record {
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
@@ -617,7 +618,7 @@
 
     # Get paged extension definitions
     # 
-    resource function get [int:Signed32 appId](map<string|string[]> headers = {}, boolean archived = false, int:Signed32 limit = 0, string after = "", anydata Additional Values, GetAppIdGetPageQueries queries) returns CollectionResponsePublicActionDefinitionForwardPaging|error;
+    resource function get [int:Signed32 appId](map<string|string[]> headers = {}, boolean archived = false, int:Signed32 limit = 0, string after = "", GetAppIdGetPageQueries queries) returns CollectionResponsePublicActionDefinitionForwardPaging|error;
 
     # Create a new extension definition
     # 
@@ -645,7 +646,7 @@
 
     # Get extension definition by Id
     # 
-    resource function get [int:Signed32 appId]/[string definitionId](map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, GetAppIdDefinitionIdGetByIdQueries queries) returns PublicActionDefinition|error;
+    resource function get [int:Signed32 appId]/[string definitionId](map<string|string[]> headers = {}, boolean archived = false, GetAppIdDefinitionIdGetByIdQueries queries) returns PublicActionDefinition|error;
 
     # Archive an extension definition
     # 
@@ -669,5 +670,5 @@
 
     # List all definition revisions
     # 
-    resource function get [int:Signed32 appId]/[string definitionId]/revisions(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", anydata Additional Values, GetAppIdDefinitionIdRevisionsGetPageQueries queries) returns CollectionResponsePublicActionRevisionForwardPaging|error;
+    resource function get [int:Signed32 appId]/[string definitionId]/revisions(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", GetAppIdDefinitionIdRevisionsGetPageQueries queries) returns CollectionResponsePublicActionRevisionForwardPaging|error;
 }
`````

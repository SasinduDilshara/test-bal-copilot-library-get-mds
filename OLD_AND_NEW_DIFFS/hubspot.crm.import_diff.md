# hubspot.crm.import — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.import` |
| **Old file** | `hubspot.crm.import/old/ballerinax_hubspot.crm.import.bal.txt` |
| **New file** | `hubspot.crm.import/new/ballerinax_hubspot.crm.import.bal.txt` |
| **Old lines** | 525 |
| **New lines** | 526 |
| **Lines added** | 12 |
| **Lines removed** | 11 |
| **Hunks** | 9 |

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
| 1 | 260–273 | 260–273 | Types | +2 | −2 |
| 2 | 295–301 | 295–301 | Types | +1 | −1 |
| 3 | 332–342 | 332–342 | Types | +2 | −2 |
| 4 | 360–366 | 360–366 | Types | +1 | −1 |
| 5 | 378–384 | 378–384 | Types | +1 | −1 |
| 6 | 389–395 | 389–395 | Types | +1 | −1 |
| 7 | 401–407 | 401–407 | Types | +1 | −1 |
| 8 | 456–461 | 456–462 | Types | +1 | −0 |
| 9 | 513–523 | 514–524 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- hubspot.crm.import/old/ballerinax_hubspot.crm.import.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.import/new/ballerinax_hubspot.crm.import.bal.txt	2026-08-12 13:19:19
@@ -260,14 +260,14 @@
     # The source type of the template: admin-defined, previous import, or user file
     "admin_defined"|"previous_import"|"user_file" templateType;
     # The unique identifier of the import template
-    ballerina/lang.int:0.0.0:Signed32 templateId;
+    int:Signed32 templateId;
 };
 
 # Metadata summarizing the outcomes, file IDs, and object lists associated with a CRM import operation
 
 type PublicImportMetadata record {
     # Summarized outcomes of each row a developer attempted to import into HubSpot
-    record {|ballerina/lang.int:0.0.0:Signed32...;|} counters;
+    record {|int:Signed32...;|} counters;
     # The IDs of files uploaded in the File Manager API
     string[] fileIds;
     # The lists containing the imported objects
@@ -295,7 +295,7 @@
     # System or integration that originated this property value
     "UNKNOWN"|"IMPORT"|"API"|"FORM"|"ANALYTICS"|"MIGRATION"|"SALESFORCE"|"INTEGRATION"|"CONTACTS_WEB"|"WAL_INCREMENTAL"|"TASK"|"EMAIL"|"WORKFLOWS"|"CALCULATED"|"SOCIAL"|"BATCH_UPDATE"|"SIGNALS"|"BIDEN"|"DEFAULT"|"COMPANIES"|"DEALS"|"ASSISTS"|"PRESENTATIONS"|"TALLY"|"SIDEKICK"|"CRM_UI"|"MERGE_CONTACTS"|"PORTAL_USER_ASSOCIATOR"|"INTEGRATIONS_PLATFORM"|"BCC_TO_CRM"|"FORWARD_TO_CRM"|"ENGAGEMENTS"|"SALES"|"HEISENBERG"|"LEADIN"|"GMAIL_INTEGRATION"|"ACADEMY"|"SALES_MESSAGES"|"AVATARS_SERVICE"|"MERGE_COMPANIES"|"SEQUENCES"|"COMPANY_FAMILIES"|"MOBILE_IOS"|"MOBILE_ANDROID"|"CONTACTS"|"ASSOCIATIONS"|"EXTENSION"|"SUCCESS"|"BOT"|"INTEGRATIONS_SYNC"|"AUTOMATION_PLATFORM"|"CONVERSATIONS"|"EMAIL_INTEGRATION"|"CONTENT_MEMBERSHIP"|"QUOTES"|"BET_ASSIGNMENT"|"QUOTAS"|"BET_CRM_CONNECTOR"|"MEETINGS"|"MERGE_OBJECTS"|"RECYCLING_BIN"|"ADS"|"AI_GROUP"|"COMMUNICATOR"|"SETTINGS"|"PROPERTY_SETTINGS"|"PIPELINE_SETTINGS"|"COMPANY_INSIGHTS"|"BEHAVIORAL_EVENTS"|"PAYMENTS"|"GOALS"|"PORTAL_OBJECT_SYNC"|"APPROVALS"|"FILE_MANAGER"|"MARKETPLACE"|"INTERNAL_PROCESSING"|"FORECASTING"|"SLACK_INTEGRATION"|"CRM_UI_BULK_ACTION"|"WORKFLOW_CONTACT_DELETE_ACTION"|"ACCEPTANCE_TEST"|"PLAYBOOKS"|"CHATSPOT"|"FLYWHEEL_PRODUCT_DATA_SYNC"|"HELP_DESK"|"BILLING"|"DATA_ENRICHMENT"|"AUTOMATION_JOURNEY"|"MICROAPPS"|"INTENT"|"PROSPECTING_AGENT" 'source;
     # ID of the user who last updated this property value
-    ballerina/lang.int:0.0.0:Signed32 updatedByUserId;
+    int:Signed32 updatedByUserId;
     # Timestamp (ms) used to determine value persistence ordering
     int persistenceTimestamp;
     # Additional metadata string describing the value's source context
@@ -332,11 +332,11 @@
     # Indicates whether the row contains encrypted property values
     boolean containsEncryptedProperties;
     # The line number of this row within the import file
-    ballerina/lang.int:0.0.0:Signed32 lineNumber;
+    int:Signed32 lineNumber;
     # The name of the sheet or page containing this row
     string pageName?;
     # The unique identifier of the import file this row belongs to
-    ballerina/lang.int:0.0.0:Signed32 fileId;
+    int:Signed32 fileId;
 };
 
 # Represents the status and lifecycle timestamps of an asynchronous action, including start, completion, and current processing state
@@ -360,7 +360,7 @@
     # A cursor token to retrieve results appearing before this value in the paginated list
     string before?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
@@ -378,7 +378,7 @@
     # Set to True to receive the data values for the errored row
     boolean includeRowData?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
     # Set to True to receive a message explaining the error
@@ -389,7 +389,7 @@
 
 type PublicImportError record {
     # Unix timestamp (int32) when the import error was recorded
-    ballerina/lang.int:0.0.0:Signed32 createdAt;
+    int:Signed32 createdAt;
     # Additional contextual detail about the import error
     string extraContext?;
     # Identifier of the object type involved in the import error
@@ -401,7 +401,7 @@
     # Human-readable description of the import error
     string errorMessage?;
     # Column number in the import file where the error was detected
-    ballerina/lang.int:0.0.0:Signed32 knownColumnNumber?;
+    int:Signed32 knownColumnNumber?;
     # Formatted representation of the invalid value for display purposes
     string invalidValueToDisplay?;
     # Unique identifier for the import error record
@@ -456,6 +456,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -513,11 +514,11 @@
 
     # Retrieve errors for an import
     # 
-    resource function get [int importId]/errors(map<string|string[]> headers = {}, boolean includeRowData = false, int:Signed32 limit = 0, string after = "", boolean includeErrorMessage = false, anydata Additional Values, GetImportIdErrorsGetErrorsQueries queries) returns CollectionResponsePublicImportErrorForwardPaging|error;
+    resource function get [int importId]/errors(map<string|string[]> headers = {}, boolean includeRowData = false, int:Signed32 limit = 0, string after = "", boolean includeErrorMessage = false, GetImportIdErrorsGetErrorsQueries queries) returns CollectionResponsePublicImportErrorForwardPaging|error;
 
     # Get active imports
     # 
-    resource function get (map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, GetGetPageQueries queries) returns CollectionResponsePublicImportResponse|error;
+    resource function get (map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", GetGetPageQueries queries) returns CollectionResponsePublicImportResponse|error;
 
     # Start a new import
     # 
`````

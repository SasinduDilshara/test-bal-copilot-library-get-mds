# hubspot.marketing.subscriptions — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.subscriptions` |
| **Old file** | `hubspot.marketing.subscriptions/old/ballerinax_hubspot.marketing.subscriptions.bal.txt` |
| **New file** | `hubspot.marketing.subscriptions/new/ballerinax_hubspot.marketing.subscriptions.bal.txt` |
| **Old lines** | 761 |
| **New lines** | 762 |
| **Lines added** | 20 |
| **Lines removed** | 19 |
| **Hunks** | 12 |

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
| 1 | 209–215 | 209–215 | Types | +1 | −1 |
| 2 | 300–306 | 300–306 | Types | +1 | −1 |
| 3 | 317–323 | 317–323 | Types | +1 | −1 |
| 4 | 364–370 | 364–370 | Types | +1 | −1 |
| 5 | 412–428 | 412–428 | Types | +3 | −3 |
| 6 | 467–473 | 467–473 | Types | +1 | −1 |
| 7 | 493–498 | 493–499 | Types | +1 | −0 |
| 8 | 572–578 | 573–579 | Types | +1 | −1 |
| 9 | 599–605 | 600–606 | Types | +1 | −1 |
| 10 | 619–625 | 620–626 | Types | +1 | −1 |
| 11 | 681–687 | 682–688 | Types | +1 | −1 |
| 12 | 729–759 | 730–760 | Client | +7 | −7 |

---

## Unified diff

`````diff
--- hubspot.marketing.subscriptions/old/ballerinax_hubspot.marketing.subscriptions.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.subscriptions/new/ballerinax_hubspot.marketing.subscriptions.bal.txt	2026-08-12 13:19:19
@@ -209,7 +209,7 @@
     # Timestamp when the action completed
     string completedAt;
     # Total number of errors encountered during processing
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the action was requested
     string requestedAt?;
     # Timestamp when the action began processing
@@ -300,7 +300,7 @@
     # The source that initiated the subscription status change
     string 'source;
     # The unique identifier of the subscription type
-    ballerina/lang.int:0.0.0:Signed32 subscriptionId;
+    int:Signed32 subscriptionId;
     # A human-readable explanation of the legal basis for processing
     string? legalBasisExplanation?;
     # The unique identifier of the associated business unit
@@ -317,7 +317,7 @@
     # The date and time when the bulk batch operation completed
     string completedAt;
     # The total number of errors encountered during the bulk batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch request was received
     string requestedAt?;
     # Timestamp when batch processing began
@@ -364,7 +364,7 @@
     # The date and time when the action completed
     string completedAt;
     # The number of errors encountered during the action
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # The date and time when the action was requested
     string requestedAt?;
     # The date and time when the action began processing
@@ -412,17 +412,17 @@
 
 type PublicSubscriptionTranslation record {
     # Unix timestamp (int32) when the translation was created
-    ballerina/lang.int:0.0.0:Signed32 createdAt;
+    int:Signed32 createdAt;
     # Localized display name of the subscription
     string name;
     # Localized description of the subscription
     string description;
     # ID of the subscription this translation belongs to
-    ballerina/lang.int:0.0.0:Signed32 subscriptionId;
+    int:Signed32 subscriptionId;
     # BCP 47 language code for this translation (e.g., 'en', 'fr')
     string languageCode;
     # Unix timestamp (int32) when the translation was last updated
-    ballerina/lang.int:0.0.0:Signed32 updatedAt;
+    int:Signed32 updatedAt;
 };
 
 # Represents the Queries record for the operation: postCommunicationPreferencesV4StatusesBatchRead
@@ -467,7 +467,7 @@
     # Timestamp when the batch opt-out operation completed
     string completedAt;
     # Total number of errors encountered in the batch opt-out operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch opt-out operation was requested
     string requestedAt?;
     # Timestamp when the batch opt-out operation began processing
@@ -493,6 +493,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -572,7 +573,7 @@
     # The date and time when the batch operation completed
     string completedAt;
     # The total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # The date and time when the batch operation was requested
     string requestedAt?;
     # The date and time when the batch operation began processing
@@ -599,7 +600,7 @@
     # The legal basis for communication
     "LEGITIMATE_INTEREST_PQL"|"LEGITIMATE_INTEREST_CLIENT"|"PERFORMANCE_OF_CONTRACT"|"CONSENT_WITH_NOTICE"|"NON_GDPR"|"PROCESS_AND_STORE"|"LEGITIMATE_INTEREST_OTHER" legalBasis?;
     # The ID of the subscription to update
-    ballerina/lang.int:0.0.0:Signed32 subscriptionId;
+    int:Signed32 subscriptionId;
     # The explanation for the legal basis
     string legalBasisExplanation?;
 };
@@ -619,7 +620,7 @@
     # Timestamp when the action operation completed
     string completedAt;
     # The total number of errors encountered during processing
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the action was requested
     string requestedAt?;
     # Timestamp when the action processing began
@@ -681,7 +682,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered in the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -729,31 +730,31 @@
 
     # Get contact's unsubscribed status
     # 
-    remote function getCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, anydata Additional Values, GetCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries) returns ActionResponseWithResultsPublicWideStatus|error;
+    remote function getCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, GetCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries) returns ActionResponseWithResultsPublicWideStatus|error;
 
     # Unsubscribe contact from all
     # 
-    remote function postCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, anydata Additional Values, PostCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries) returns ActionResponseWithResultsPublicStatus|error;
+    remote function postCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, PostCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries) returns ActionResponseWithResultsPublicStatus|error;
 
     # Batch retrieve subscription statuses
     # 
-    remote function postCommunicationPreferencesV4StatusesBatchRead(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, anydata Additional Values, PostCommunicationPreferencesV4StatusesBatchReadQueries queries) returns BatchResponsePublicStatusBulkResponse|BatchResponsePublicStatusBulkResponseWithErrors|error;
+    remote function postCommunicationPreferencesV4StatusesBatchRead(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, PostCommunicationPreferencesV4StatusesBatchReadQueries queries) returns BatchResponsePublicStatusBulkResponse|BatchResponsePublicStatusBulkResponseWithErrors|error;
 
     # Batch unsubscribe all contacts
     # 
-    remote function postCommunicationPreferencesV4StatusesBatchUnsubscribeAll(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, anydata Additional Values, PostCommunicationPreferencesV4StatusesBatchUnsubscribeAllQueries queries) returns BatchResponsePublicBulkOptOutFromAllResponse|error;
+    remote function postCommunicationPreferencesV4StatusesBatchUnsubscribeAll(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, boolean verbose = false, PostCommunicationPreferencesV4StatusesBatchUnsubscribeAllQueries queries) returns BatchResponsePublicBulkOptOutFromAllResponse|error;
 
     # Retrieve all subscription definitions
     # 
-    remote function getCommunicationPreferencesV4Definitions(map<string|string[]> headers = {}, boolean includeTranslations = false, int businessUnitId = 0, anydata Additional Values, GetCommunicationPreferencesV4DefinitionsQueries queries) returns ActionResponseWithResultsSubscriptionDefinition|error;
+    remote function getCommunicationPreferencesV4Definitions(map<string|string[]> headers = {}, boolean includeTranslations = false, int businessUnitId = 0, GetCommunicationPreferencesV4DefinitionsQueries queries) returns ActionResponseWithResultsSubscriptionDefinition|error;
 
     # Batch get opted-out contacts
     # 
-    remote function postCommunicationPreferencesV4StatusesBatchUnsubscribeAllRead(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, anydata Additional Values, PostCommunicationPreferencesV4StatusesBatchUnsubscribeAllReadQueries queries) returns BatchResponsePublicWideStatusBulkResponse|BatchResponsePublicWideStatusBulkResponseWithErrors|error;
+    remote function postCommunicationPreferencesV4StatusesBatchUnsubscribeAllRead(BatchInputString payload, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, PostCommunicationPreferencesV4StatusesBatchUnsubscribeAllReadQueries queries) returns BatchResponsePublicWideStatusBulkResponse|BatchResponsePublicWideStatusBulkResponseWithErrors|error;
 
     # Get contact subscription prefs
     # 
-    remote function getCommunicationPreferencesV4StatusesSubscriberIdString(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, anydata Additional Values, GetCommunicationPreferencesV4StatusesSubscriberIdStringQueries queries) returns ActionResponseWithResultsPublicStatus|error;
+    remote function getCommunicationPreferencesV4StatusesSubscriberIdString(string subscriberIdString, map<string|string[]> headers = {}, "EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL", int businessUnitId = 0, GetCommunicationPreferencesV4StatusesSubscriberIdStringQueries queries) returns ActionResponseWithResultsPublicStatus|error;
 
     # Update contact subscription status
     # 
`````

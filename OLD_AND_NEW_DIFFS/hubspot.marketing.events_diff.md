# hubspot.marketing.events — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.events` |
| **Old file** | `hubspot.marketing.events/old/ballerinax_hubspot.marketing.events.bal.txt` |
| **New file** | `hubspot.marketing.events/new/ballerinax_hubspot.marketing.events.bal.txt` |
| **Old lines** | 1366 |
| **New lines** | 1367 |
| **Lines added** | 43 |
| **Lines removed** | 42 |
| **Hunks** | 30 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 28 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 277–283 | 277–283 | Types | +1 | −1 |
| 2 | 303–309 | 303–309 | Types | +1 | −1 |
| 3 | 326–338 | 326–338 | Types | +2 | −2 |
| 4 | 340–348 | 340–348 | Types | +2 | −2 |
| 5 | 459–465 | 459–465 | Types | +1 | −1 |
| 6 | 485–495 | 485–496 | Types | +2 | −1 |
| 7 | 563–569 | 564–570 | Types | +1 | −1 |
| 8 | 580–586 | 581–587 | Types | +1 | −1 |
| 9 | 671–677 | 672–678 | Types | +1 | −1 |
| 10 | 765–771 | 766–772 | Types | +1 | −1 |
| 11 | 920–926 | 921–927 | Types | +1 | −1 |
| 12 | 929–935 | 930–936 | Types | +1 | −1 |
| 13 | 952–958 | 953–959 | Types | +1 | −1 |
| 14 | 1012–1024 | 1013–1025 | Types | +2 | −2 |
| 15 | 1028–1036 | 1029–1037 | Types | +2 | −2 |
| 16 | 1073–1079 | 1074–1080 | Types | +1 | −1 |
| 17 | 1115–1121 | 1116–1122 | Types | +1 | −1 |
| 18 | 1134–1146 | 1135–1147 | Types | +4 | −4 |
| 19 | 1154–1160 | 1155–1161 | Types | +1 | −1 |
| 20 | 1182–1188 | 1183–1189 | Types | +1 | −1 |
| 21 | 1193–1199 | 1194–1200 | Types | +1 | −1 |
| 22 | 1222–1240 | 1223–1241 | Client | +4 | −4 |
| 23 | 1242–1252 | 1243–1253 | Client | +2 | −2 |
| 24 | 1254–1264 | 1255–1265 | Client | +2 | −2 |
| 25 | 1286–1292 | 1287–1293 | Client | +1 | −1 |
| 26 | 1318–1324 | 1319–1325 | Client | +1 | −1 |
| 27 | 1330–1336 | 1331–1337 | Client | +1 | −1 |
| 28 | 1342–1348 | 1343–1349 | Client | +1 | −1 |
| 29 | 1350–1356 | 1351–1357 | Client | +1 | −1 |
| 30 | 1362–1366 | 1363–1367 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.marketing.events/old/ballerinax_hubspot.marketing.events.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.events/new/ballerinax_hubspot.marketing.events.bal.txt	2026-08-12 13:19:19
@@ -277,7 +277,7 @@
     # The identifier of the Contact. It may be email or internal id
     string contactIdentifier?;
     # The limit for response size. The default value is 10, the max number is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The participation state value. It may be REGISTERED, CANCELLED, ATTENDED, NO_SHOW
     string state?;
     # The cursor indicating the position of the last retrieved item
@@ -303,7 +303,7 @@
     # Contact's attendance status: REGISTERED, ATTENDED, CANCELLED, EMPTY, or NO_SHOW
     "REGISTERED"|"ATTENDED"|"CANCELLED"|"EMPTY"|"NO_SHOW" attendanceState;
     # Total duration in seconds the contact attended the event
-    ballerina/lang.int:0.0.0:Signed32 attendanceDurationSeconds?;
+    int:Signed32 attendanceDurationSeconds?;
 };
 
 # Response object containing a HubSpot contact's ID and email address
@@ -326,13 +326,13 @@
 
 type MarketingEventPublicReadResponse record {
     # The number of HubSpot contacts that registered for this marketing event
-    ballerina/lang.int:0.0.0:Signed32 registrants;
+    int:Signed32 registrants;
     # The name of the organizer of the marketing event
     string eventOrganizer;
     # A URL in the external event application where the marketing event can be managed
     string eventUrl?;
     # The number of HubSpot contacts that attended this marketing event
-    ballerina/lang.int:0.0.0:Signed32 attendees;
+    int:Signed32 attendees;
     # The type of the marketing event
     string eventType?;
     # Indicates whether the marketing event has been completed
@@ -340,9 +340,9 @@
     # The end date and time of the marketing event
     string endDateTime?;
     # The number of HubSpot contacts that registered for this marketing event, but did not attend. This field only had a value when the event is over
-    ballerina/lang.int:0.0.0:Signed32 noShows;
+    int:Signed32 noShows;
     # The number of HubSpot contacts that registered for this marketing event, but later cancelled their registration
-    ballerina/lang.int:0.0.0:Signed32 cancellations;
+    int:Signed32 cancellations;
     # Timestamp when the marketing event record was created
     string createdAt;
     # The start date and time of the marketing event
@@ -459,7 +459,7 @@
     # Timestamp when the list was deleted, if applicable
     string deletedAt?;
     # The version number of the list
-    ballerina/lang.int:0.0.0:Signed32 listVersion;
+    int:Signed32 listVersion;
     # The total number of members in the list
     int size?;
     # The display name of the list
@@ -485,11 +485,12 @@
     # The id of the marketing event in the external event application
     string externalEventId;
     # The id of the application that created the marketing event in HubSpot
-    ballerina/lang.int:0.0.0:Signed32 appId;
+    int:Signed32 appId;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -563,7 +564,7 @@
     # The event ID from the external event application
     string externalEventId;
     # The ID of the app that created the marketing event
-    ballerina/lang.int:0.0.0:Signed32 appId;
+    int:Signed32 appId;
     # The HubSpot object ID of the marketing event
     string objectId;
 };
@@ -580,7 +581,7 @@
     # The identifier of the Contact. It may be email or internal id
     string contactIdentifier?;
     # The limit for response size. The default value is 10, the max number is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The participation state value. It may be REGISTERED, CANCELLED, ATTENDED, NO_SHOW
     string state?;
     # The cursor indicating the position of the last retrieved item
@@ -671,7 +672,7 @@
 
 type CollectionResponseWithTotalPublicListNoPaging record {
     # The total number of results in the collection
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # The array of public list objects returned in the response
     PublicList[] results;
 };
@@ -765,7 +766,7 @@
     # The datetime when the batch operation completed
     string completedAt;
     # The total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # The datetime when the batch operation was requested
     string requestedAt?;
     # The datetime when the batch operation started processing
@@ -920,7 +921,7 @@
 
 type CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging record {
     # Total number of marketing event identifier results returned
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # List of marketing event identifier response objects
     MarketingEventIdentifiersResponse[] results;
 };
@@ -929,7 +930,7 @@
 
 type EventDetailSettings record {
     # The id of the application the settings are for
-    ballerina/lang.int:0.0.0:Signed32 appId;
+    int:Signed32 appId;
     # The url that will be used to fetch marketing event details by id
     string eventDetailsUrl;
 };
@@ -952,7 +953,7 @@
 
 type GetParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactIdQueries record {
     # The limit for response size. The default value is 10, the max number is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The participation state value. It may be REGISTERED, CANCELLED, ATTENDED, NO_SHOW
     string state?;
     # The cursor indicating the position of the last retrieved item
@@ -1012,13 +1013,13 @@
 
 type MarketingEventPublicReadResponseV2 record {
     # The total number of contacts registered for the event
-    ballerina/lang.int:0.0.0:Signed32 registrants?;
+    int:Signed32 registrants?;
     # The name of the person or organization hosting the event
     string eventOrganizer?;
     # The URL where the marketing event can be accessed or viewed
     string eventUrl?;
     # The total number of contacts who attended the event
-    ballerina/lang.int:0.0.0:Signed32 attendees?;
+    int:Signed32 attendees?;
     # Object containing identifying information about the application associated with a marketing event
     AppInfo appInfo?;
     # The category or format type of the marketing event
@@ -1028,9 +1029,9 @@
     # The date and time when the marketing event ends
     string endDateTime?;
     # The number of registered contacts who did not attend the event
-    ballerina/lang.int:0.0.0:Signed32 noShows?;
+    int:Signed32 noShows?;
     # The total number of registrations cancelled for the event
-    ballerina/lang.int:0.0.0:Signed32 cancellations?;
+    int:Signed32 cancellations?;
     # The date and time when the marketing event record was created
     string createdAt;
     # The date and time when the marketing event begins
@@ -1073,7 +1074,7 @@
     # The datetime the batch operation completed
     string completedAt;
     # The total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # The datetime the batch operation was requested
     string requestedAt?;
     # The datetime the batch operation started processing
@@ -1115,7 +1116,7 @@
     # Timestamp when the batch operation completed
     string completedAt;
     # Total number of errors encountered during the batch operation
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch operation was requested
     string requestedAt?;
     # Timestamp when the batch operation began processing
@@ -1134,13 +1135,13 @@
 
 type AttendanceCounters record {
     # Number of contacts who attended the event
-    ballerina/lang.int:0.0.0:Signed32 attended;
+    int:Signed32 attended;
     # Number of contacts registered for the event
-    ballerina/lang.int:0.0.0:Signed32 registered;
+    int:Signed32 registered;
     # Number of contacts who cancelled their registration
-    ballerina/lang.int:0.0.0:Signed32 cancelled;
+    int:Signed32 cancelled;
     # Number of registered contacts who did not attend
-    ballerina/lang.int:0.0.0:Signed32 noShows;
+    int:Signed32 noShows;
 };
 
 # Represents the Queries record for the operation: postAttendanceExternalEventIdSubscriberStateEmailCreateRecordByContactEmails
@@ -1154,7 +1155,7 @@
 
 type CollectionResponseWithTotalParticipationBreakdownForwardPaging record {
     # Total number of participation breakdown records available
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Pagination metadata for forward-only traversal, containing a reference to the next page of results
     ForwardPaging paging?;
     # List of participation breakdown records for the current page
@@ -1182,7 +1183,7 @@
 
 type GetQueries record {
     # The limit for response size. The default value is 10, the max number is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The cursor indicating the position of the last retrieved item
     string after?;
 };
@@ -1193,7 +1194,7 @@
     # Timestamp when the batch request completed
     string completedAt;
     # Total number of errors encountered in the batch request
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     # Timestamp when the batch request was received
     string requestedAt?;
     # Timestamp when the batch request began processing
@@ -1222,19 +1223,19 @@
 
     # Record participants by contact IDs
     # 
-    remote function postAttendanceExternalEventIdSubscriberStateCreateRecordByContactIds(string externalEventId, string subscriberState, BatchInputMarketingEventSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostAttendanceExternalEventIdSubscriberStateCreateRecordByContactIdsQueries queries) returns BatchResponseSubscriberVidResponse|error;
+    remote function postAttendanceExternalEventIdSubscriberStateCreateRecordByContactIds(string externalEventId, string subscriberState, BatchInputMarketingEventSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", PostAttendanceExternalEventIdSubscriberStateCreateRecordByContactIdsQueries queries) returns BatchResponseSubscriberVidResponse|error;
 
     # Get participations breakdown by event
     # 
-    remote function getParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventId(int marketingEventId, map<string|string[]> headers = {}, string contactIdentifier = "", int:Signed32 limit = 0, string state = "", string after = "", anydata Additional Values, GetParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
+    remote function getParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventId(int marketingEventId, map<string|string[]> headers = {}, string contactIdentifier = "", int:Signed32 limit = 0, string state = "", string after = "", GetParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
 
     # Record subscriber state by contact
     # 
-    remote function postEventsExternalEventIdSubscriberStateUpsertUpsertByContactId(string externalEventId, string subscriberState, BatchInputMarketingEventSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostEventsExternalEventIdSubscriberStateUpsertUpsertByContactIdQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    remote function postEventsExternalEventIdSubscriberStateUpsertUpsertByContactId(string externalEventId, string subscriberState, BatchInputMarketingEventSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", PostEventsExternalEventIdSubscriberStateUpsertUpsertByContactIdQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Get Marketing Event by External IDs
     # 
-    remote function getEventsExternalEventIdGetDetails(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, GetEventsExternalEventIdGetDetailsQueries queries) returns MarketingEventPublicReadResponse|error;
+    remote function getEventsExternalEventIdGetDetails(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", GetEventsExternalEventIdGetDetailsQueries queries) returns MarketingEventPublicReadResponse|error;
 
     # Create or update a marketing event
     # 
@@ -1242,11 +1243,11 @@
 
     # Delete event by external IDs
     # 
-    remote function deleteEventsExternalEventIdArchive(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, DeleteEventsExternalEventIdArchiveQueries queries) returns error?;
+    remote function deleteEventsExternalEventIdArchive(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", DeleteEventsExternalEventIdArchiveQueries queries) returns error?;
 
     # Update event by external IDs
     # 
-    remote function patchEventsExternalEventIdUpdate(string externalEventId, MarketingEventUpdateRequestParams payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PatchEventsExternalEventIdUpdateQueries queries) returns MarketingEventPublicDefaultResponse|error;
+    remote function patchEventsExternalEventIdUpdate(string externalEventId, MarketingEventUpdateRequestParams payload, map<string|string[]> headers = {}, string externalAccountId = "", PatchEventsExternalEventIdUpdateQueries queries) returns MarketingEventPublicDefaultResponse|error;
 
     # Upsert multiple marketing events
     # 
@@ -1254,11 +1255,11 @@
 
     # Record participants by email
     # 
-    remote function postAttendanceExternalEventIdSubscriberStateEmailCreateRecordByContactEmails(string externalEventId, string subscriberState, BatchInputMarketingEventEmailSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostAttendanceExternalEventIdSubscriberStateEmailCreateRecordByContactEmailsQueries queries) returns BatchResponseSubscriberEmailResponse|error;
+    remote function postAttendanceExternalEventIdSubscriberStateEmailCreateRecordByContactEmails(string externalEventId, string subscriberState, BatchInputMarketingEventEmailSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", PostAttendanceExternalEventIdSubscriberStateEmailCreateRecordByContactEmailsQueries queries) returns BatchResponseSubscriberEmailResponse|error;
 
     # Get participation breakdown
     # 
-    remote function getParticipationsExternalAccountIdExternalEventIdBreakdownGetParticipationsBreakdownByExternalEventId(string externalAccountId, string externalEventId, map<string|string[]> headers = {}, string contactIdentifier = "", int:Signed32 limit = 0, string state = "", string after = "", anydata Additional Values, GetParticipationsExternalAccountIdExternalEventIdBreakdownGetParticipationsBreakdownByExternalEventIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
+    remote function getParticipationsExternalAccountIdExternalEventIdBreakdownGetParticipationsBreakdownByExternalEventId(string externalAccountId, string externalEventId, map<string|string[]> headers = {}, string contactIdentifier = "", int:Signed32 limit = 0, string state = "", string after = "", GetParticipationsExternalAccountIdExternalEventIdBreakdownGetParticipationsBreakdownByExternalEventIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
 
     # Get Marketing Event by objectId
     # 
@@ -1286,7 +1287,7 @@
 
     # Get all marketing event
     # 
-    remote function get(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", anydata Additional Values, GetQueries queries) returns CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging|error;
+    remote function get(map<string|string[]> headers = {}, int:Signed32 limit = 0, string after = "", GetQueries queries) returns CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging|error;
 
     # Batch update events by ObjectId
     # 
@@ -1318,7 +1319,7 @@
 
     # Mark a marketing event as cancelled
     # 
-    remote function postEventsExternalEventIdCancelCancel(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostEventsExternalEventIdCancelCancelQueries queries) returns MarketingEventDefaultResponse|error;
+    remote function postEventsExternalEventIdCancelCancel(string externalEventId, map<string|string[]> headers = {}, string externalAccountId = "", PostEventsExternalEventIdCancelCancelQueries queries) returns MarketingEventDefaultResponse|error;
 
     # Associate list with event
     # 
@@ -1330,7 +1331,7 @@
 
     # Record subscriber state by email
     # 
-    remote function postEventsExternalEventIdSubscriberStateEmailUpsertUpsertByContactEmail(string externalEventId, string subscriberState, BatchInputMarketingEventEmailSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostEventsExternalEventIdSubscriberStateEmailUpsertUpsertByContactEmailQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
+    remote function postEventsExternalEventIdSubscriberStateEmailUpsertUpsertByContactEmail(string externalEventId, string subscriberState, BatchInputMarketingEventEmailSubscriber payload, map<string|string[]> headers = {}, string externalAccountId = "", PostEventsExternalEventIdSubscriberStateEmailUpsertUpsertByContactEmailQueries queries) returns http:Response|error; // Special Agent Note: Response FROM ballerina/http package
 
     # Associate list with event
     # 
@@ -1342,7 +1343,7 @@
 
     # Mark a marketing event as completed
     # 
-    remote function postEventsExternalEventIdCompleteComplete(string externalEventId, MarketingEventCompleteRequestParams payload, map<string|string[]> headers = {}, string externalAccountId = "", anydata Additional Values, PostEventsExternalEventIdCompleteCompleteQueries queries) returns MarketingEventDefaultResponse|error;
+    remote function postEventsExternalEventIdCompleteComplete(string externalEventId, MarketingEventCompleteRequestParams payload, map<string|string[]> headers = {}, string externalAccountId = "", PostEventsExternalEventIdCompleteCompleteQueries queries) returns MarketingEventDefaultResponse|error;
 
     # Create a marketing event
     # 
@@ -1350,7 +1351,7 @@
 
     # Get participation breakdown
     # 
-    remote function getParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactId(string contactIdentifier, map<string|string[]> headers = {}, int:Signed32 limit = 0, string state = "", string after = "", anydata Additional Values, GetParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
+    remote function getParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactId(string contactIdentifier, map<string|string[]> headers = {}, int:Signed32 limit = 0, string state = "", string after = "", GetParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactIdQueries queries) returns CollectionResponseWithTotalParticipationBreakdownForwardPaging|error;
 
     # Retrieve the application settings
     # 
@@ -1362,5 +1363,5 @@
 
     # Find events by external ID
     # 
-    remote function getEventsSearchDoSearch(map<string|string[]> headers = {}, string q = "", anydata Additional Values, GetEventsSearchDoSearchQueries queries) returns CollectionResponseSearchPublicResponseWrapperNoPaging|error;
+    remote function getEventsSearchDoSearch(map<string|string[]> headers = {}, string q = "", GetEventsSearchDoSearchQueries queries) returns CollectionResponseSearchPublicResponseWrapperNoPaging|error;
 }
`````

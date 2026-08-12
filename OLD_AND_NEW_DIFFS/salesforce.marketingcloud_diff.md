# salesforce.marketingcloud — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `salesforce.marketingcloud` |
| **Old file** | `salesforce.marketingcloud/old/ballerinax_salesforce.marketingcloud.bal.txt` |
| **New file** | `salesforce.marketingcloud/new/ballerinax_salesforce.marketingcloud.bal.txt` |
| **Old lines** | 1636 |
| **New lines** | 1675 |
| **Lines added** | 54 |
| **Lines removed** | 15 |
| **Hunks** | 25 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type DataExtensionRowSet`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 435–442 | 435–444 | Types | +2 | −0 |
| 2 | 554–573 | 556–581 | Types | +6 | −0 |
| 3 | 691–707 | 699–720 | Types | +5 | −0 |
| 4 | 834–843 | 847–859 | Types | +3 | −0 |
| 5 | 858–867 | 874–886 | Types | +3 | −0 |
| 6 | 935–940 | 954–960 | Types | +1 | −0 |
| 7 | 943–950 | 963–972 | Types | +2 | −0 |
| 8 | 963–972 | 985–996 | Types | +2 | −0 |
| 9 | 1125–1130 | 1149–1155 | Types | +1 | −0 |
| 10 | 1269–1288 | 1294–1318 | Types | +6 | −1 |
| 11 | 1292–1299 | 1322–1331 | Types | +2 | −0 |
| 12 | 1301–1306 | 1333–1339 | Types | +1 | −0 |
| 13 | 1348–1361 | 1381–1399 | Types | +5 | −0 |
| 14 | 1425–1430 | 1463–1469 | Types | +1 | −0 |
| 15 | 1436–1442 | 1475–1481 | Client | +1 | −1 |
| 16 | 1468–1474 | 1507–1513 | Client | +1 | −1 |
| 17 | 1492–1498 | 1531–1537 | Client | +1 | −1 |
| 18 | 1500–1510 | 1539–1549 | Client | +2 | −2 |
| 19 | 1512–1518 | 1551–1557 | Client | +1 | −1 |
| 20 | 1520–1526 | 1559–1565 | Client | +1 | −1 |
| 21 | 1568–1578 | 1607–1617 | Client | +2 | −2 |
| 22 | 1584–1594 | 1623–1633 | Client | +2 | −2 |
| 23 | 1596–1602 | 1635–1641 | Client | +1 | −1 |
| 24 | 1604–1610 | 1643–1649 | Client | +1 | −1 |
| 25 | 1612–1618 | 1651–1657 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- salesforce.marketingcloud/old/ballerinax_salesforce.marketingcloud.bal.txt	2026-08-12 12:57:30
+++ salesforce.marketingcloud/new/ballerinax_salesforce.marketingcloud.bal.txt	2026-08-12 13:19:19
@@ -435,8 +435,10 @@
     # Version of the Journey Spec used.
     decimal workflowApiVersion;
     # An array of goals containing a single object. Journeys only support one goal.
+    @constraint:Array {maxLength: 1}
     Goal[] goals?;
     # An array of triggers containing a single object. Journeys only support one trigger.
+    @constraint:Array {maxLength: 1}
     EventDefinition[] triggers?;
     # An object that contains default values for the journey, such as email expressions. Example: { "email": ["{{Event.event-key.EmailAddress}}", "{{Contact.Default.Email}}"] }
     Defaults defaults?;
@@ -554,20 +556,26 @@
 
 type GetCampaignsQueries record {
     # The field and sort method to use to sort the results. You can sort on these fields: modifiedDate, createdDate, name, and id. You can sort these fields in ascending (ASC) or descending (DESC) order. The default value is 'modifiedDate DESC'
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
 };
 
 
 type FireEvent record {
     # Key of the entry event defined in Journey Builder
+    @jsondata:Name {value: "EventDefinitionKey"}
     string eventDefinitionKey;
     # Unique identifier for the contact
+    @jsondata:Name {value: "ContactKey"}
     string contactKey;
     # Additional attributes required by the entry event schema
+    @jsondata:Name {value: "Data"}
     record {|anydata...;|} data?;
 };
 
@@ -691,17 +699,22 @@
 
 type GetEmailDefinitionsQueries record {
     # Filter by status type. Accepted values are active, inactive, or deleted. Valid operations are eq and neq
+    @http:Query {name: "$filter"}
     string filter?;
     # Sort by a dimension. You can sort by only one dimension. Accepted values are definitionKey, name, createdDate, modifiedDate, and status
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2ClientCredentialsGrantConfig auth;
@@ -834,10 +847,13 @@
 
 type ContactExitRequest record {
     # List of version numbers of the journey to remove contact from
+    @jsondata:Name {value: "Versions"}
     int[] versions?;
     # ID that uniquely identifies a subscriber or contact. Can be a single contact or an array of up to 50
+    @jsondata:Name {value: "ContactKey"}
     string contactKey;
     # Customer Key that uniquely identifies the journey
+    @jsondata:Name {value: "DefinitionKey"}
     string definitionKey;
 };
 
@@ -858,10 +874,13 @@
     # End date and time in UTC of the date range
     string enddateutc?;
     # Determines which property to use for sorting and the direction in which to sort the data
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
     # Start date and time in UTC of the date range
     string startdateutc?;
@@ -935,6 +954,7 @@
     # The version number of the workflowApiVersion value to retrieve. The default value is 1
     decimal specificApiVersionNumber?;
     # The field and sort method to use to sort the results. You can sort on these fields: ModifiedDate, Name, Performance. You can sort these fields in ascending (ASC) or descending (DESC) order. The default value is modifiedDate DESC
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # A search string to apply to the request. The API searches the name and description of each journey for this string, and returns all matching journeys
     string nameOrDescription?;
@@ -943,8 +963,10 @@
     # A tag to use to filter the results. When you specify this parameter, the API returns only journeys with the specified tag
     string tag?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
     # The type of definition to retrieve. The only accepted value is transactional, which retrieves all transactional send definitions
     "transactional" definitionType?;
@@ -963,10 +985,12 @@
     # Job status (New, Staging, Queued, Processing, Complete, Error)
     "New"|"Staging"|"Queued"|"Processing"|"Complete"|"Error" jobStatus?;
     # Data extension customer key (required)
+    @constraint:String {maxLength: 36}
     string destinationCustomerKey;
     # Supported data operation types (required)
     "AddAndUpdate"|"AddAndDoNotUpdate"|"UpdateButDoNotAdd"|"Overwrite" updateType;
     # Can specify a value up to 8 hours - this value drives the time allocated to stage data before starting a job. Note: For larger staging time (over 8 hours), contact support
+    @constraint:Int {maxValue: 8}
     int jobExpirationHours?;
 };
 
@@ -1125,6 +1149,7 @@
 
 type ContactMembershipRequest record {
     # The list of unique keys that identify the contacts
+    @jsondata:Name {value: "ContactKeyList"}
     string[] contactKeyList?;
 };
 
@@ -1269,20 +1294,25 @@
     int versionNumber?;
 };
 
-// Unknown type: DataExtensionRowSet
+# An array of data extension rows to be upserted
+type DataExtensionRowSet DataExtensionRow[];
 
 # Represents the Queries record for the operation: getCategories
 
 type GetCategoriesQueries record {
     # Filter by ParentId using a simple operator and value. ParentId is the only allowed field. If you don't provide a $filter parameter, the query returns all the Categories in your MID
+    @http:Query {name: "$filter"}
     string filter?;
     # Determines which category property to use for sorting, and also determines the direction in which to sort the data. If you don't provide the $orderBy parameter, the results are sorted by category ID in ascending order
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # Determines which MIDs the query results come from. To return categories that reside in your MID, either don't add the scope parameter or call the endpoint like this: .../categories?scope=Ours. To return categories that are shared to your MID, or that you have shared with other MIDs, call the endpoint like this: .../categories?scope=Shared. To return all categories visible to your MID, call the endpoint like this: .../categories?scope=Ours,Shared
     "Ours"|"Shared"|"Ours,Shared" scope?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
 };
 
@@ -1292,8 +1322,10 @@
     # Filter event definitions by name substring
     string name?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
 };
 
@@ -1301,6 +1333,7 @@
 
 type SearchContactPreferencesQueries record {
     # For contact key, use 1. For contact ID, use 2
+    @http:Query {name: "ReferenceType"}
     1|2 referenceType;
 };
 
@@ -1348,14 +1381,19 @@
 
 type GetAssetsQueries record {
     # Filter by an asset's property using a simple operator and value
+    @http:Query {name: "$filter"}
     string filter?;
     # Determines which asset property to use for sorting, and also determines the direction in which to sort the data. If you don't provide the $orderBy parameter, the results are sorted by asset ID in ascending order
+    @http:Query {name: "$orderBy"}
     string orderBy?;
     # Comma-delimited string of asset properties used to reduce the size of your results to only the properties you need
+    @http:Query {name: "$fields"}
     string fields?;
     # The page number of results to retrieve. The default value is 1
+    @http:Query {name: "$page"}
     int page?;
     # The number of items to return on a page of results. The default and maximum value is 50
+    @http:Query {name: "$pageSize"}
     int pageSize?;
 };
 
@@ -1425,6 +1463,7 @@
     # List of contact keys or IDs to delete
     string[] values;
     # Type of delete operation to perform
+    @jsondata:Name {value: "DeleteOperationType"}
     "ContactAndAttributes"|"AttributesOnly" deleteOperationType;
 };
 
@@ -1436,7 +1475,7 @@
 
     # Get Event Definitions
     # 
-    remote function getEventDefinitions(map<string|string[]> headers = {}, string name = "", int page = 0, int pageSize = 0, anydata Additional Values, GetEventDefinitionsQueries queries) returns EventDefinitionList|error;
+    remote function getEventDefinitions(map<string|string[]> headers = {}, string name = "", int page = 0, int pageSize = 0, GetEventDefinitionsQueries queries) returns EventDefinitionList|error;
 
     # Create Event Definition
     # 
@@ -1468,7 +1507,7 @@
 
     # Get Interactions (Journeys)
     # 
-    remote function getJourneys(map<string|string[]> headers = {}, boolean mostRecentVersionOnly = false, decimal specificApiVersionNumber = 0.0d, string orderBy = "", string nameOrDescription = "", Extras extras = "all", string tag = "", int page = 0, int pageSize = 0, "transactional" definitionType = "transactional", int versionNumber = 0, JourneyStatus status = "Deleted", anydata Additional Values, GetJourneysQueries queries) returns JourneysList|error;
+    remote function getJourneys(map<string|string[]> headers = {}, boolean mostRecentVersionOnly = false, decimal specificApiVersionNumber = 0.0d, string orderBy = "", string nameOrDescription = "", Extras extras = "all", string tag = "", int page = 0, int pageSize = 0, "transactional" definitionType = "transactional", int versionNumber = 0, JourneyStatus status = "Deleted", GetJourneysQueries queries) returns JourneysList|error;
 
     # Update an existing Journey version
     # 
@@ -1492,7 +1531,7 @@
 
     # Get Interactions (Journeys) - By ID
     # 
-    remote function getJourneyById(string journeyId, map<string|string[]> headers = {}, Extras extras = "all", int versionNumber = 0, anydata Additional Values, GetJourneyByIdQueries queries) returns Journey|error;
+    remote function getJourneyById(string journeyId, map<string|string[]> headers = {}, Extras extras = "all", int versionNumber = 0, GetJourneyByIdQueries queries) returns Journey|error;
 
     # Update an existing Journey version
     # 
@@ -1500,11 +1539,11 @@
 
     # Delete Interaction (Journey) - By ID
     # 
-    remote function deleteJourneyById(string journeyId, map<string|string[]> headers = {}, int versionNumber = 0, anydata Additional Values, DeleteJourneyByIdQueries queries) returns json|error;
+    remote function deleteJourneyById(string journeyId, map<string|string[]> headers = {}, int versionNumber = 0, DeleteJourneyByIdQueries queries) returns json|error;
 
     # Get Interactions (Journeys) - By Key
     # 
-    remote function getJourneyByKey(string 'key, map<string|string[]> headers = {}, Extras extras = "all", int versionNumber = 0, anydata Additional Values, GetJourneyByKeyQueries queries) returns Journey|error;
+    remote function getJourneyByKey(string 'key, map<string|string[]> headers = {}, Extras extras = "all", int versionNumber = 0, GetJourneyByKeyQueries queries) returns Journey|error;
 
     # Update existing Journey version
     # 
@@ -1512,7 +1551,7 @@
 
     # Delete Interaction (Journey) - By Key
     # 
-    remote function deleteJourneyByKey(string 'key, map<string|string[]> headers = {}, int versionNumber = 0, anydata Additional Values, DeleteJourneyByKeyQueries queries) returns json|error;
+    remote function deleteJourneyByKey(string 'key, map<string|string[]> headers = {}, int versionNumber = 0, DeleteJourneyByKeyQueries queries) returns json|error;
 
     # Validate Address
     # 
@@ -1520,7 +1559,7 @@
 
     # Get Campaigns
     # 
-    remote function getCampaigns(map<string|string[]> headers = {}, string orderBy = "", int page = 0, int pageSize = 0, anydata Additional Values, GetCampaignsQueries queries) returns CampaignList|error;
+    remote function getCampaigns(map<string|string[]> headers = {}, string orderBy = "", int page = 0, int pageSize = 0, GetCampaignsQueries queries) returns CampaignList|error;
 
     # Create Campaign
     # 
@@ -1568,11 +1607,11 @@
 
     # Delete Contact - By Key
     # 
-    remote function deleteContact(ContactDeleteRequest payload, map<string|string[]> headers = {}, "ids"|"keys" type = "ids", anydata Additional Values, DeleteContactQueries queries) returns ContactDeleteResponse|error;
+    remote function deleteContact(ContactDeleteRequest payload, map<string|string[]> headers = {}, "ids"|"keys" type = "ids", DeleteContactQueries queries) returns ContactDeleteResponse|error;
 
     # Get Contact Delete Request Details
     # 
-    remote function getContactDeleteRequests(map<string|string[]> headers = {}, 1|5|7 statusid = 1, string enddateutc = "", string orderBy = "", int page = 0, int pageSize = 0, string startdateutc = "", anydata Additional Values, GetContactDeleteRequestsQueries queries) returns ContactDeleteRequestsResponse|error;
+    remote function getContactDeleteRequests(map<string|string[]> headers = {}, 1|5|7 statusid = 1, string enddateutc = "", string orderBy = "", int page = 0, int pageSize = 0, string startdateutc = "", GetContactDeleteRequestsQueries queries) returns ContactDeleteRequestsResponse|error;
 
     # Get Contact Preferences
     # 
@@ -1584,11 +1623,11 @@
 
     # Search Contact Preferences
     # 
-    remote function searchContactPreferences(SearchPreferencesRequest payload, map<string|string[]> headers = {}, 1|2 referenceType = 1, anydata Additional Values, SearchContactPreferencesQueries queries) returns SearchPreferencesResponse|error;
+    remote function searchContactPreferences(SearchPreferencesRequest payload, map<string|string[]> headers = {}, 1|2 referenceType = 1, SearchContactPreferencesQueries queries) returns SearchPreferencesResponse|error;
 
     # Get Content Assets
     # 
-    remote function getAssets(map<string|string[]> headers = {}, string filter = "", string orderBy = "", string fields = "", int page = 0, int pageSize = 0, anydata Additional Values, GetAssetsQueries queries) returns AssetList|error;
+    remote function getAssets(map<string|string[]> headers = {}, string filter = "", string orderBy = "", string fields = "", int page = 0, int pageSize = 0, GetAssetsQueries queries) returns AssetList|error;
 
     # Create Content Asset
     # 
@@ -1596,7 +1635,7 @@
 
     # Delete Content Asset
     # 
-    remote function deleteAsset(int id, map<string|string[]> headers = {}, boolean isCDNDelete = false, anydata Additional Values, DeleteAssetQueries queries) returns error?;
+    remote function deleteAsset(int id, map<string|string[]> headers = {}, boolean isCDNDelete = false, DeleteAssetQueries queries) returns error?;
 
     # Update Content Asset
     # 
@@ -1604,7 +1643,7 @@
 
     # Get Content Categories
     # 
-    remote function getCategories(map<string|string[]> headers = {}, string filter = "", string orderBy = "", "Ours"|"Shared"|"Ours,Shared" scope = "Ours", int page = 0, int pageSize = 0, anydata Additional Values, GetCategoriesQueries queries) returns CategoryList|error;
+    remote function getCategories(map<string|string[]> headers = {}, string filter = "", string orderBy = "", "Ours"|"Shared"|"Ours,Shared" scope = "Ours", int page = 0, int pageSize = 0, GetCategoriesQueries queries) returns CategoryList|error;
 
     # Create Content Category
     # 
@@ -1612,7 +1651,7 @@
 
     # Get Email Definitions
     # 
-    remote function getEmailDefinitions(map<string|string[]> headers = {}, string filter = "", string orderBy = "", int page = 0, int pageSize = 0, anydata Additional Values, GetEmailDefinitionsQueries queries) returns EmailDefinitionList|error;
+    remote function getEmailDefinitions(map<string|string[]> headers = {}, string filter = "", string orderBy = "", int page = 0, int pageSize = 0, GetEmailDefinitionsQueries queries) returns EmailDefinitionList|error;
 
     # Create Email Definition
     # 
`````

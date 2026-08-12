# hubspot.marketing.campaigns — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.campaigns` |
| **Old file** | `hubspot.marketing.campaigns/old/ballerinax_hubspot.marketing.campaigns.bal.txt` |
| **New file** | `hubspot.marketing.campaigns/new/ballerinax_hubspot.marketing.campaigns.bal.txt` |
| **Old lines** | 672 |
| **New lines** | 673 |
| **Lines added** | 26 |
| **Lines removed** | 25 |
| **Hunks** | 17 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 18 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 286–292 | 286–292 | Types | +1 | −1 |
| 2 | 298–304 | 298–304 | Types | +1 | −1 |
| 3 | 340–346 | 340–346 | Types | +1 | −1 |
| 4 | 370–382 | 370–382 | Types | +3 | −3 |
| 5 | 407–412 | 407–413 | Types | +1 | −0 |
| 6 | 467–479 | 468–480 | Types | +3 | −3 |
| 7 | 493–502 | 494–503 | Types | +4 | −4 |
| 8 | 507–513 | 508–514 | Types | +1 | −1 |
| 9 | 518–524 | 519–525 | Types | +1 | −1 |
| 10 | 571–579 | 572–580 | Types | +2 | −2 |
| 11 | 588–594 | 589–595 | Types | +1 | −1 |
| 12 | 608–614 | 609–615 | Client | +1 | −1 |
| 13 | 616–622 | 617–623 | Client | +1 | −1 |
| 14 | 624–634 | 625–635 | Client | +2 | −2 |
| 15 | 644–650 | 645–651 | Client | +1 | −1 |
| 16 | 656–662 | 657–663 | Client | +1 | −1 |
| 17 | 668–672 | 669–673 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.marketing.campaigns/old/ballerinax_hubspot.marketing.campaigns.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.campaigns/new/ballerinax_hubspot.marketing.campaigns.bal.txt	2026-08-12 13:19:19
@@ -286,7 +286,7 @@
 
 type BatchResponsePublicCampaignWithAssetsWithErrors record {
     string completedAt;
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     string requestedAt?;
     string startedAt;
     record {|string...;|} links?;
@@ -298,7 +298,7 @@
 
 type PublicCampaignWithAssets record {
     string createdAt;
-    record {|ballerinax/hubspot.marketing.campaigns:2.0.2:CollectionResponsePublicCampaignAsset...;|} assets;
+    record {|CollectionResponsePublicCampaignAsset...;|} assets;
     string id;
     record {|string...;|} properties;
     string updatedAt;
@@ -340,7 +340,7 @@
 
 type BatchResponsePublicCampaignWithErrors record {
     string completedAt;
-    ballerina/lang.int:0.0.0:Signed32 numErrors?;
+    int:Signed32 numErrors?;
     string requestedAt?;
     string startedAt;
     record {|string...;|} links?;
@@ -370,13 +370,13 @@
 
 
 type PublicSpendItem record {
-    ballerina/lang.int:0.0.0:Signed32 createdAt;
+    int:Signed32 createdAt;
     decimal amount;
     string name;
     string description?;
     string id;
-    ballerina/lang.int:0.0.0:Signed32 'order;
-    ballerina/lang.int:0.0.0:Signed32 updatedAt;
+    int:Signed32 'order;
+    int:Signed32 updatedAt;
 };
 
 
@@ -407,6 +407,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -467,13 +468,13 @@
 
 
 type PublicBudgetItem record {
-    ballerina/lang.int:0.0.0:Signed32 createdAt;
+    int:Signed32 createdAt;
     decimal amount;
     string name;
     string description?;
     string id;
-    ballerina/lang.int:0.0.0:Signed32 'order;
-    ballerina/lang.int:0.0.0:Signed32 updatedAt;
+    int:Signed32 'order;
+    int:Signed32 updatedAt;
 };
 
 
@@ -493,10 +494,10 @@
 
 
 type MetricsCounters record {
-    ballerina/lang.int:0.0.0:Signed32 sessions;
-    ballerina/lang.int:0.0.0:Signed32 newContactsFirstTouch;
-    ballerina/lang.int:0.0.0:Signed32 influencedContacts;
-    ballerina/lang.int:0.0.0:Signed32 newContactsLastTouch;
+    int:Signed32 sessions;
+    int:Signed32 newContactsFirstTouch;
+    int:Signed32 influencedContacts;
+    int:Signed32 newContactsLastTouch;
 };
 
 # Represents the Queries record for the operation: get-/marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}
@@ -507,7 +508,7 @@
     string endDate?;
     # Limit for the number of contacts to fetch
 Default: 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # A cursor for pagination. If provided, the results will start after the given cursor.
 Example: NTI1Cg%3D%3D
     string after?;
@@ -518,7 +519,7 @@
 
 
 type CollectionResponseWithTotalPublicCampaignForwardPaging record {
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     ForwardPaging paging?;
     PublicCampaign[] results;
 };
@@ -571,9 +572,9 @@
 
 
 type RevenueAttributionAggregate record {
-    ballerina/lang.int:0.0.0:Signed32 contactsNumber?;
+    int:Signed32 contactsNumber?;
     decimal dealAmount?;
-    ballerina/lang.int:0.0.0:Signed32 dealsNumber?;
+    int:Signed32 dealsNumber?;
     decimal revenueAmount?;
     "AED"|"AFN"|"ALL"|"AMD"|"ANG"|"AOA"|"ARS"|"AUD"|"AWG"|"AZN"|"BAM"|"BBD"|"BDT"|"BGN"|"BHD"|"BIF"|"BMD"|"BND"|"BOB"|"BOV"|"BRL"|"BSD"|"BTN"|"BWP"|"BYN"|"BZD"|"CAD"|"CDF"|"CHE"|"CHF"|"CHW"|"CLF"|"CLP"|"CNY"|"COP"|"COU"|"CRC"|"CUC"|"CUP"|"CVE"|"CZK"|"DJF"|"DKK"|"DOP"|"DZD"|"EGP"|"ERN"|"ETB"|"EUR"|"FJD"|"FKP"|"GBP"|"GEL"|"GHS"|"GIP"|"GMD"|"GNF"|"GTQ"|"GYD"|"HKD"|"HNL"|"HRK"|"HTG"|"HUF"|"IDR"|"ILS"|"INR"|"IQD"|"IRR"|"ISK"|"JMD"|"JOD"|"JPY"|"KES"|"KGS"|"KHR"|"KMF"|"KPW"|"KRW"|"KWD"|"KYD"|"KZT"|"LAK"|"LBP"|"LKR"|"LRD"|"LSL"|"LYD"|"MAD"|"MDL"|"MGA"|"MKD"|"MMK"|"MNT"|"MOP"|"MRU"|"MUR"|"MVR"|"MWK"|"MXN"|"MXV"|"MYR"|"MZN"|"NAD"|"NGN"|"NIO"|"NOK"|"NPR"|"NZD"|"OMR"|"PAB"|"PEN"|"PGK"|"PHP"|"PKR"|"PLN"|"PYG"|"QAR"|"RON"|"RSD"|"RUB"|"RWF"|"SAR"|"SBD"|"SCR"|"SDG"|"SEK"|"SGD"|"SHP"|"SLL"|"SOS"|"SRD"|"SSP"|"STN"|"SVC"|"SYP"|"SZL"|"THB"|"TJS"|"TMT"|"TND"|"TOP"|"TRY"|"TTD"|"TWD"|"TZS"|"UAH"|"UGX"|"USD"|"USN"|"UYI"|"UYU"|"UZS"|"VEF"|"VND"|"VUV"|"WST"|"XAF"|"XAG"|"XAU"|"XBA"|"XBB"|"XBC"|"XBD"|"XCD"|"XDR"|"XOF"|"XPD"|"XPF"|"XPT"|"XSU"|"XUA"|"YER"|"ZAR"|"ZMW"|"ZWL" currencyCode?;
 };
@@ -588,7 +589,7 @@
 type GetMarketingV3CampaignsQueries record {
     # The maximum number of results to return. Allowed values range from 1 to 100
 Default: 50
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # A filter to return campaigns whose names contain the specified substring. This allows partial matching of campaign names, returning all campaigns that include the given substring in their name. If this parameter is not provided, the search will return all campaigns
     string name?;
     # The field by which to sort the results. Allowed values are hs_name, createdAt, updatedAt. An optional '-' before the property name can denote descending order
@@ -608,7 +609,7 @@
 
     # Campaign search
     # 
-    resource function get (map<string|string[]> headers = {}, int:Signed32 limit = 0, string name = "", string sort = "", string after = "", string[] properties = [], anydata Additional Values, GetMarketingV3CampaignsQueries queries) returns CollectionResponseWithTotalPublicCampaignForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, int:Signed32 limit = 0, string name = "", string sort = "", string after = "", string[] properties = [], GetMarketingV3CampaignsQueries queries) returns CollectionResponseWithTotalPublicCampaignForwardPaging|error;
 
     # Create a campaign
     # 
@@ -616,7 +617,7 @@
 
     # Read a batch of campaigns
     # 
-    resource function post batch/read(BatchInputPublicCampaignReadInput payload, map<string|string[]> headers = {}, string endDate = "", string startDate = "", string[] properties = [], anydata Additional Values, PostMarketingV3CampaignsBatchReadQueries queries) returns BatchResponsePublicCampaignWithAssets|BatchResponsePublicCampaignWithAssetsWithErrors|error;
+    resource function post batch/read(BatchInputPublicCampaignReadInput payload, map<string|string[]> headers = {}, string endDate = "", string startDate = "", string[] properties = [], PostMarketingV3CampaignsBatchReadQueries queries) returns BatchResponsePublicCampaignWithAssets|BatchResponsePublicCampaignWithAssetsWithErrors|error;
 
     # Update a batch of campaigns
     # 
@@ -624,11 +625,11 @@
 
     # Get Campaign Metrics
     # 
-    resource function get [string campaignGuid]/reports/metrics(map<string|string[]> headers = {}, string endDate = "", string startDate = "", anydata Additional Values, GetMarketingV3CampaignsCampaignGuidReportsMetricsQueries queries) returns MetricsCounters|error;
+    resource function get [string campaignGuid]/reports/metrics(map<string|string[]> headers = {}, string endDate = "", string startDate = "", GetMarketingV3CampaignsCampaignGuidReportsMetricsQueries queries) returns MetricsCounters|error;
 
     # List assets
     # 
-    resource function get [string campaignGuid]/assets/[string assetType](map<string|string[]> headers = {}, string endDate = "", string limit = "", string after = "", string startDate = "", anydata Additional Values, GetMarketingV3CampaignsCampaignGuidAssetsAssetTypeQueries queries) returns CollectionResponsePublicCampaignAssetForwardPaging|error;
+    resource function get [string campaignGuid]/assets/[string assetType](map<string|string[]> headers = {}, string endDate = "", string limit = "", string after = "", string startDate = "", GetMarketingV3CampaignsCampaignGuidAssetsAssetTypeQueries queries) returns CollectionResponsePublicCampaignAssetForwardPaging|error;
 
     # Delete a batch of campaigns
     # 
@@ -644,7 +645,7 @@
 
     # Fetch revenue
     # 
-    resource function get [string campaignGuid]/reports/revenue(map<string|string[]> headers = {}, string attributionModel = "", string endDate = "", string startDate = "", anydata Additional Values, GetMarketingV3CampaignsCampaignGuidReportsRevenueQueries queries) returns RevenueAttributionAggregate|error;
+    resource function get [string campaignGuid]/reports/revenue(map<string|string[]> headers = {}, string attributionModel = "", string endDate = "", string startDate = "", GetMarketingV3CampaignsCampaignGuidReportsRevenueQueries queries) returns RevenueAttributionAggregate|error;
 
     # Create a batch of campaigns
     # 
@@ -656,7 +657,7 @@
 
     # Read a campaign
     # 
-    resource function get [string campaignGuid](map<string|string[]> headers = {}, string endDate = "", string startDate = "", string[] properties = [], anydata Additional Values, GetMarketingV3CampaignsCampaignGuidQueries queries) returns PublicCampaignWithAssets|error;
+    resource function get [string campaignGuid](map<string|string[]> headers = {}, string endDate = "", string startDate = "", string[] properties = [], GetMarketingV3CampaignsCampaignGuidQueries queries) returns PublicCampaignWithAssets|error;
 
     # Delete campaign 
     # 
@@ -668,5 +669,5 @@
 
     # Fetch contact IDs
     # 
-    resource function get [string campaignGuid]/reports/contacts/[string contactType](map<string|string[]> headers = {}, string endDate = "", int:Signed32 limit = 0, string after = "", string startDate = "", anydata Additional Values, GetMarketingV3CampaignsCampaignGuidReportsContactsContactTypeQueries queries) returns CollectionResponseContactReferenceForwardPaging|error;
+    resource function get [string campaignGuid]/reports/contacts/[string contactType](map<string|string[]> headers = {}, string endDate = "", int:Signed32 limit = 0, string after = "", string startDate = "", GetMarketingV3CampaignsCampaignGuidReportsContactsContactTypeQueries queries) returns CollectionResponseContactReferenceForwardPaging|error;
 }
`````

# hubspot.marketing.transactional — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.transactional` |
| **Old file** | `hubspot.marketing.transactional/old/ballerinax_hubspot.marketing.transactional.bal.txt` |
| **New file** | `hubspot.marketing.transactional/new/ballerinax_hubspot.marketing.transactional.bal.txt` |
| **Old lines** | 407 |
| **New lines** | 408 |
| **Lines added** | 4 |
| **Lines removed** | 3 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 236–242 | 236–242 | Types | +1 | −1 |
| 2 | 301–307 | 301–307 | Types | +1 | −1 |
| 3 | 334–339 | 334–340 | Types | +1 | −0 |
| 4 | 387–393 | 388–394 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.marketing.transactional/old/ballerinax_hubspot.marketing.transactional.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.transactional/new/ballerinax_hubspot.marketing.transactional.bal.txt	2026-08-12 13:19:19
@@ -236,7 +236,7 @@
 Note: Custom properties do not currently support arrays. To provide a listing in an email, one workaround is to build an HTML list (either with tables or ul) and specify it as a custom property
     record {|record {|anydata...;|}...;|} customProperties?;
     # The content ID for the transactional email, which can be found in email tool UI
-    ballerina/lang.int:0.0.0:Signed32 emailId;
+    int:Signed32 emailId;
     # A JSON object containing anything you want to override
     PublicSingleSendEmail message;
     # The contactProperties field is a map of contact property values. Each contact property value contains a name and value property. Each property will get set on the contact record and will be visible in the template under {{ contact.NAME }}. Use these properties when you want to set a contact property while you're sending the email. For example, when sending a reciept you may want to set a last_paid_date property, as the sending of the receipt will have information about the last payment
@@ -301,7 +301,7 @@
 
 type GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries record {
     # Maximum number of tokens to return
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Identifier assigned to the campaign provided during the token creation
     string emailCampaignId?;
     # Starting point to get the next set of results
@@ -334,6 +334,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -387,7 +388,7 @@
 
     # Query SMTP API tokens by campaign
     # 
-    resource function get smtp\-tokens(map<string|string[]> headers = {}, int:Signed32 limit = 0, string emailCampaignId = "", string after = "", string campaignName = "", anydata Additional Values, GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries queries) returns CollectionResponseSmtpApiTokenViewForwardPaging|error;
+    resource function get smtp\-tokens(map<string|string[]> headers = {}, int:Signed32 limit = 0, string emailCampaignId = "", string after = "", string campaignName = "", GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries queries) returns CollectionResponseSmtpApiTokenViewForwardPaging|error;
 
     # Create a SMTP API token
     # 
`````

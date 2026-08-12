# hubspot.marketing.emails — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.emails` |
| **Old file** | `hubspot.marketing.emails/old/ballerinax_hubspot.marketing.emails.bal.txt` |
| **New file** | `hubspot.marketing.emails/new/ballerinax_hubspot.marketing.emails.bal.txt` |
| **Old lines** | 1010 |
| **New lines** | 1011 |
| **Lines added** | 25 |
| **Lines removed** | 24 |
| **Hunks** | 20 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 17 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 235–248 | 235–248 | Types | +2 | −2 |
| 2 | 379–385 | 379–385 | Types | +1 | −1 |
| 3 | 435–441 | 435–441 | Types | +1 | −1 |
| 4 | 449–457 | 449–457 | Types | +2 | −2 |
| 5 | 470–476 | 470–476 | Types | +1 | −1 |
| 6 | 491–497 | 491–497 | Types | +1 | −1 |
| 7 | 547–553 | 547–553 | Types | +1 | −1 |
| 8 | 557–563 | 557–563 | Types | +1 | −1 |
| 9 | 576–584 | 576–584 | Types | +2 | −2 |
| 10 | 627–633 | 627–633 | Types | +1 | −1 |
| 11 | 762–767 | 762–768 | Types | +1 | −0 |
| 12 | 814–820 | 815–821 | Types | +1 | −1 |
| 13 | 838–844 | 839–845 | Types | +1 | −1 |
| 14 | 876–882 | 877–883 | Types | +1 | −1 |
| 15 | 909–915 | 910–916 | Types | +1 | −1 |
| 16 | 934–940 | 935–941 | Client | +1 | −1 |
| 17 | 946–952 | 947–953 | Client | +1 | −1 |
| 18 | 970–976 | 971–977 | Client | +1 | −1 |
| 19 | 986–992 | 987–993 | Client | +1 | −1 |
| 20 | 998–1010 | 999–1011 | Client | +3 | −3 |

---

## Unified diff

`````diff
--- hubspot.marketing.emails/old/ballerinax_hubspot.marketing.emails.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.emails/new/ballerinax_hubspot.marketing.emails.bal.txt	2026-08-12 13:19:19
@@ -235,14 +235,14 @@
     # The line style of the divider (e.g., solid, dashed)
     string lineType?;
     # The height of the divider in pixels
-    ballerina/lang.int:0.0.0:Signed32 height?;
+    int:Signed32 height?;
 };
 
 # Response object for collections of marketing emails with pagination information
 
 type CollectionResponseWithTotalVersionPublicEmail record {
     # Total number of content emails
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Contains information pagination of results
     Paging paging?;
     # Collection of emails
@@ -379,7 +379,7 @@
 
 type PublicEmailContent record {
     # Map of smart field keys to their SmartEmailField configurations
-    record {|ballerinax/hubspot.marketing.emails:1.0.2:SmartEmailField...;|} smartFields?;
+    record {|SmartEmailField...;|} smartFields?;
     # Key-value map of theme setting overrides applied to the email
     record {|record {|anydata...;|}...;|} themeSettingsValues?;
     # Map of flexible layout areas and their content configurations
@@ -435,7 +435,7 @@
     # Color of the border surrounding the email body
     string bodyBorderColor?;
     # Width in pixels of the border surrounding the email body
-    ballerina/lang.int:0.0.0:Signed32 bodyBorderWidth?;
+    int:Signed32 bodyBorderWidth?;
     # Defines font styling properties including size, color, weight, and decoration for email text elements
     PublicFontStyle linksFont?;
     # Background color of the email template
@@ -449,9 +449,9 @@
     # Line height applied to the secondary font text
     string secondaryFontLineHeight?;
     # Font size in points applied to primary text in the email
-    ballerina/lang.int:0.0.0:Signed32 primaryFontSize?;
+    int:Signed32 primaryFontSize?;
     # Font size in points applied to secondary text in the email
-    ballerina/lang.int:0.0.0:Signed32 secondaryFontSize?;
+    int:Signed32 secondaryFontSize?;
     # Color applied to primary font text in the email
     string primaryFontColor?;
     # Defines font styling properties including size, color, weight, and decoration for email text elements
@@ -470,7 +470,7 @@
 
 type PublicFontStyle record {
     # Font size in points
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # Font color as a hex or CSS color value
     string color?;
     # Indicates whether the text is underlined
@@ -491,7 +491,7 @@
     # Defines font styling properties including size, color, weight, and decoration for email text elements
     PublicFontStyle fontStyle?;
     # Corner radius of the button in pixels
-    ballerina/lang.int:0.0.0:Signed32 cornerRadius?;
+    int:Signed32 cornerRadius?;
 };
 
 # Web version page settings for a marketing email, including URL, redirect configuration, metadata, and expiry details
@@ -547,7 +547,7 @@
 
 type PublicRssEmailDetails record {
     # Maximum width in pixels for images in blog RSS emails
-    ballerina/lang.int:0.0.0:Signed32 blogImageMaxWidth?;
+    int:Signed32 blogImageMaxWidth?;
     # Type classification of the blog RSS email
     string blogEmailType?;
     # ID of the HubSpot blog associated with the RSS email
@@ -557,7 +557,7 @@
     # Scheduling timing configuration for the RSS email sends
     record {|record {|anydata...;|}...;|} timing?;
     # Maximum number of RSS feed entries to include in the email
-    ballerina/lang.int:0.0.0:Signed32 maxEntries?;
+    int:Signed32 maxEntries?;
     # Whether to use the RSS feed headline as the email subject line
     boolean useHeadlineAsSubject?;
     # Layout style used to render blog content in the RSS email
@@ -576,9 +576,9 @@
     # Status of the AB test
     "master"|"variant"|"loser_variant"|"mab_master"|"mab_variant"|"automated_master"|"automated_variant"|"automated_loser_variant" abStatus?;
     # The size of your test group
-    ballerina/lang.int:0.0.0:Signed32 abTestPercentage?;
+    int:Signed32 abTestPercentage?;
     # Time limit on gathering test results. After this time is up, the winning version will be sent to the remaining contacts
-    ballerina/lang.int:0.0.0:Signed32 hoursToWait?;
+    int:Signed32 hoursToWait?;
     # The ID of the AB test
     string testId?;
     # Metric to determine the version that will be sent to the remaining contacts
@@ -627,7 +627,7 @@
 
 type CollectionResponseWithTotalPublicEmailForwardPaging record {
     # Total number of content emails
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Forward pagination object containing the next page cursor
     ForwardPaging paging?;
     # Collection of emails
@@ -762,6 +762,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -814,7 +815,7 @@
 
 type CollectionResponseWithTotalEmailStatisticIntervalNoPaging record {
     # Total number of objects
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Collection of objects
     EmailStatisticInterval[] results;
 };
@@ -838,7 +839,7 @@
     # The cursor token value to get the previous set of results. You can get this from the `paging.prev.before` JSON property of a paged response containing more results
     string before?;
     # The maximum number of results to return. Default is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The cursor token value to get the next set of results. You can get this from the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
@@ -876,7 +877,7 @@
     # List of email IDs that were sent during the time span
     int[] emails?;
     # The aggregated statistics per campaign
-    record {|ballerinax/hubspot.marketing.emails:1.0.2:EmailStatisticsData...;|} campaignAggregations?;
+    record {|EmailStatisticsData...;|} campaignAggregations?;
     # Aggregated email performance statistics including counters, engagement ratios, device breakdowns, and delivery qualifier metrics
     EmailStatisticsData aggregate?;
 };
@@ -909,7 +910,7 @@
     # Include statistics with emails
     boolean includeStats?;
     # The maximum number of results to return. Default is 100
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # Only return emails created before the specified time
     string createdBefore?;
     # The cursor token value to get the next set of results. You can get this from the `paging.next.after` JSON property of a paged response containing more results
@@ -934,7 +935,7 @@
 
     # Get aggregated statistics
     # 
-    resource function get statistics/list(map<string|string[]> headers = {}, int[] emailIds = [], string property = "", string endTimestamp = "", string startTimestamp = "", anydata Additional Values, GetStatisticsListQueries queries) returns AggregateEmailStatistics|error;
+    resource function get statistics/list(map<string|string[]> headers = {}, int[] emailIds = [], string property = "", string endTimestamp = "", string startTimestamp = "", GetStatisticsListQueries queries) returns AggregateEmailStatistics|error;
 
     # Publish or send a marketing email
     # 
@@ -946,7 +947,7 @@
 
     # Get aggregated statistic intervals
     # 
-    resource function get statistics/histogram(map<string|string[]> headers = {}, int[] emailIds = [], "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"QUARTER_HOUR"|"MINUTE"|"SECOND" interval = "YEAR", string endTimestamp = "", string startTimestamp = "", anydata Additional Values, GetStatisticsHistogramQueries queries) returns CollectionResponseWithTotalEmailStatisticIntervalNoPaging|error;
+    resource function get statistics/histogram(map<string|string[]> headers = {}, int[] emailIds = [], "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"QUARTER_HOUR"|"MINUTE"|"SECOND" interval = "YEAR", string endTimestamp = "", string startTimestamp = "", GetStatisticsHistogramQueries queries) returns CollectionResponseWithTotalEmailStatisticIntervalNoPaging|error;
 
     # Get an A/B email variation
     # 
@@ -970,7 +971,7 @@
 
     # Get revisions of a marketing email
     # 
-    resource function get [string emailId]/revisions(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, GetEmailIdRevisionsQueries queries) returns CollectionResponseWithTotalVersionPublicEmail|error;
+    resource function get [string emailId]/revisions(map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", GetEmailIdRevisionsQueries queries) returns CollectionResponseWithTotalVersionPublicEmail|error;
 
     # Unpublish or cancel an email
     # 
@@ -986,7 +987,7 @@
 
     # List all marketing emails
     # 
-    resource function get (map<string|string[]> headers = {}, string updatedAfter = "", boolean isPublished = false, string[] sort = [], string createdAfter = "", "AB_EMAIL"|"BATCH_EMAIL"|"LOCALTIME_EMAIL"|"AUTOMATED_AB_EMAIL"|"BLOG_EMAIL"|"BLOG_EMAIL_CHILD"|"RSS_EMAIL"|"RSS_EMAIL_CHILD"|"RESUBSCRIBE_EMAIL"|"OPTIN_EMAIL"|"OPTIN_FOLLOWUP_EMAIL"|"AUTOMATED_EMAIL"|"FEEDBACK_CES_EMAIL"|"FEEDBACK_CUSTOM_EMAIL"|"FEEDBACK_CUSTOM_SURVEY_EMAIL"|"FEEDBACK_NPS_EMAIL"|"FOLLOWUP_EMAIL"|"LEADFLOW_EMAIL"|"SINGLE_SEND_API"|"MARKETING_SINGLE_SEND_API"|"SMTP_TOKEN"|"TICKET_EMAIL"|"MEMBERSHIP_REGISTRATION_EMAIL"|"MEMBERSHIP_PASSWORD_SAVED_EMAIL"|"MEMBERSHIP_PASSWORD_RESET_EMAIL"|"MEMBERSHIP_EMAIL_VERIFICATION_EMAIL"|"MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL"|"MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL"|"MEMBERSHIP_OTP_LOGIN_EMAIL"|"MEMBERSHIP_FOLLOW_UP_EMAIL"|"MEMBERSHIP_VERIFICATION_EMAIL" type = "AB_EMAIL", string[] includedProperties = [], boolean workflowNames = false, string createdAt = "", string updatedBefore = "", boolean archived = false, boolean marketingCampaignNames = false, boolean includeStats = false, int:Signed32 limit = 0, string createdBefore = "", string after = "", string updatedAt = "", anydata Additional Values, GetQueries queries) returns CollectionResponseWithTotalPublicEmailForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, string updatedAfter = "", boolean isPublished = false, string[] sort = [], string createdAfter = "", "AB_EMAIL"|"BATCH_EMAIL"|"LOCALTIME_EMAIL"|"AUTOMATED_AB_EMAIL"|"BLOG_EMAIL"|"BLOG_EMAIL_CHILD"|"RSS_EMAIL"|"RSS_EMAIL_CHILD"|"RESUBSCRIBE_EMAIL"|"OPTIN_EMAIL"|"OPTIN_FOLLOWUP_EMAIL"|"AUTOMATED_EMAIL"|"FEEDBACK_CES_EMAIL"|"FEEDBACK_CUSTOM_EMAIL"|"FEEDBACK_CUSTOM_SURVEY_EMAIL"|"FEEDBACK_NPS_EMAIL"|"FOLLOWUP_EMAIL"|"LEADFLOW_EMAIL"|"SINGLE_SEND_API"|"MARKETING_SINGLE_SEND_API"|"SMTP_TOKEN"|"TICKET_EMAIL"|"MEMBERSHIP_REGISTRATION_EMAIL"|"MEMBERSHIP_PASSWORD_SAVED_EMAIL"|"MEMBERSHIP_PASSWORD_RESET_EMAIL"|"MEMBERSHIP_EMAIL_VERIFICATION_EMAIL"|"MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL"|"MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL"|"MEMBERSHIP_OTP_LOGIN_EMAIL"|"MEMBERSHIP_FOLLOW_UP_EMAIL"|"MEMBERSHIP_VERIFICATION_EMAIL" type = "AB_EMAIL", string[] includedProperties = [], boolean workflowNames = false, string createdAt = "", string updatedBefore = "", boolean archived = false, boolean marketingCampaignNames = false, boolean includeStats = false, int:Signed32 limit = 0, string createdBefore = "", string after = "", string updatedAt = "", GetQueries queries) returns CollectionResponseWithTotalPublicEmailForwardPaging|error;
 
     # Create a new marketing email
     # 
@@ -998,13 +999,13 @@
 
     # Get a marketing email by ID
     # 
-    resource function get [string emailId](map<string|string[]> headers = {}, boolean workflowNames = false, boolean archived = false, boolean marketingCampaignNames = false, boolean includeStats = false, string[] includedProperties = [], anydata Additional Values, GetEmailIdQueries queries) returns PublicEmail|error;
+    resource function get [string emailId](map<string|string[]> headers = {}, boolean workflowNames = false, boolean archived = false, boolean marketingCampaignNames = false, boolean includeStats = false, string[] includedProperties = [], GetEmailIdQueries queries) returns PublicEmail|error;
 
     # Delete a marketing email
     # 
-    resource function delete [string emailId](map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, DeleteEmailIdQueries queries) returns error?;
+    resource function delete [string emailId](map<string|string[]> headers = {}, boolean archived = false, DeleteEmailIdQueries queries) returns error?;
 
     # Update a marketing email
     # 
-    resource function patch [string emailId](EmailUpdateRequest payload, map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, PatchEmailIdQueries queries) returns PublicEmail|error;
+    resource function patch [string emailId](EmailUpdateRequest payload, map<string|string[]> headers = {}, boolean archived = false, PatchEmailIdQueries queries) returns PublicEmail|error;
 }
`````

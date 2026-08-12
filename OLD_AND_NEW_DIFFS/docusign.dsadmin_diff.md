# docusign.dsadmin — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `docusign.dsadmin` |
| **Old file** | `docusign.dsadmin/old/ballerinax_docusign.dsadmin.bal.txt` |
| **New file** | `docusign.dsadmin/new/ballerinax_docusign.dsadmin.bal.txt` |
| **Old lines** | 2514 |
| **New lines** | 2516 |
| **Lines added** | 54 |
| **Lines removed** | 52 |
| **Hunks** | 30 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 51 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type OrganizationAccountSettingsImportResponseArr`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 300–305 | 300–306 | Types | +1 | −0 |
| 2 | 370–375 | 371–377 | Types | +1 | −0 |
| 3 | 379–385 | 381–387 | Types | +1 | −1 |
| 4 | 396–402 | 398–404 | Types | +1 | −1 |
| 5 | 432–448 | 434–450 | Types | +3 | −3 |
| 6 | 483–489 | 485–491 | Types | +1 | −1 |
| 7 | 521–527 | 523–529 | Types | +1 | −1 |
| 8 | 560–566 | 562–568 | Types | +1 | −1 |
| 9 | 581–594 | 583–596 | Types | +8 | −8 |
| 10 | 676–682 | 678–684 | Types | +1 | −1 |
| 11 | 684–690 | 686–692 | Types | +1 | −1 |
| 12 | 700–706 | 702–708 | Types | +1 | −1 |
| 13 | 716–722 | 718–724 | Types | +1 | −1 |
| 14 | 818–824 | 820–826 | Types | +1 | −1 |
| 15 | 925–931 | 927–933 | Types | +1 | −1 |
| 16 | 1023–1029 | 1025–1031 | Types | +1 | −1 |
| 17 | 1045–1051 | 1047–1053 | Types | +1 | −1 |
| 18 | 1194–1200 | 1196–1202 | Types | +1 | −1 |
| 19 | 1304–1310 | 1306–1312 | Types | +1 | −1 |
| 20 | 1320–1326 | 1322–1328 | Types | +1 | −1 |
| 21 | 1331–1337 | 1333–1339 | Types | +1 | −1 |
| 22 | 1372–1378 | 1374–1380 | Types | +1 | −1 |
| 23 | 1533–1545 | 1535–1547 | Types | +4 | −4 |
| 24 | 1570–1579 | 1572–1581 | Types | +3 | −3 |
| 25 | 1599–1612 | 1601–1614 | Types | +8 | −8 |
| 26 | 1669–1675 | 1671–1677 | Types | +1 | −1 |
| 27 | 1950–1956 | 1952–1958 | Types | +1 | −1 |
| 28 | 2013–2019 | 2015–2021 | Types | +1 | −1 |
| 29 | 2055–2070 | 2057–2072 | Types | +4 | −4 |
| 30 | 2089–2095 | 2091–2097 | Types | +1 | −1 |

---

## Unified diff

`````diff
--- docusign.dsadmin/old/ballerinax_docusign.dsadmin.bal.txt	2026-08-12 12:57:30
+++ docusign.dsadmin/new/ballerinax_docusign.dsadmin.bal.txt	2026-08-12 13:19:19
@@ -300,6 +300,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -370,6 +371,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -379,7 +381,7 @@
     string last_modified?;
     string completed?;
     string expires?;
-    ballerina/lang.int:0.0.0:Signed32 percent_completed?;
+    int:Signed32 percent_completed?;
     int number_processed_accounts?;
     int number_unprocessed_accounts?;
     OrganizationAccountSettingsImportResultResponse[] results?;
@@ -396,7 +398,7 @@
 
 type OrganizationAccountSettingsImportResultResponse record {
     string id?;
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     string url?;
     int number_processed_accounts?;
     OASIRR_ErrorDetails error_details?;
@@ -432,17 +434,17 @@
     string email?;
 };
 
-// Unknown type: OrganizationAccountSettingsImportResponseArr
+type OrganizationAccountSettingsImportResponseArr OrganizationAccountSettingsImportResponse[];
 
 
 type OrgReportListResponse_OrgReport record {
     boolean complete?;
     string report_correlation_id?;
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     string report_id?;
     OrgReportListResponse_Requestor requestor?;
     string created_on?;
-    ballerina/lang.int:0.0.0:Signed32 account_export_count?;
+    int:Signed32 account_export_count?;
     string url?;
     string report_type_id?;
     string report_date_range?;
@@ -483,7 +485,7 @@
 
 type AddUserResponse record {
     string id?;
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The full name of the user.
     string user_name?;
     # The user's first name.
@@ -521,7 +523,7 @@
 
 type AddUserResponseAccountProperties record {
     string id?;
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # A list of one or more products and their respective permissions.
     ProductPermissionProfileResponse[] product_permission_profiles?;
     DSGroupResponse[] ds_groups?;
@@ -560,7 +562,7 @@
     string description?;
     boolean is_admin?;
     string last_modified_on?;
-    ballerina/lang.int:0.0.0:Signed32 user_count?;
+    int:Signed32 user_count?;
     int external_account_id?;
     string account_name?;
 };
@@ -581,14 +583,14 @@
     string last_modified?;
     # Status.
     string status?;
-    ballerina/lang.int:0.0.0:Signed32 user_count?;
-    ballerina/lang.int:0.0.0:Signed32 processed_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 added_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 updated_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 closed_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 no_action_required_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 error_count?;
-    ballerina/lang.int:0.0.0:Signed32 warning_count?;
+    int:Signed32 user_count?;
+    int:Signed32 processed_user_count?;
+    int:Signed32 added_user_count?;
+    int:Signed32 updated_user_count?;
+    int:Signed32 closed_user_count?;
+    int:Signed32 no_action_required_user_count?;
+    int:Signed32 error_count?;
+    int:Signed32 warning_count?;
     string invalid_column_headers?;
     string imports_not_found_or_not_available_for_accounts?;
     string imports_failed_for_accounts?;
@@ -676,7 +678,7 @@
 - `unspecified_error`
     string error_type?;
     # The number of errors of this type.
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
 };
 
 
@@ -684,7 +686,7 @@
     # The type of warning.
     string warning_type?;
     # The number of warnings of this type.
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
 };
 
 # A change email request.
@@ -700,7 +702,7 @@
     # The ID of the users whose email address you want to change.
     string id;
     # The site ID.
-    ballerina/lang.int:0.0.0:Signed32 site_id;
+    int:Signed32 site_id;
     # The new email address.
     string email;
 };
@@ -716,7 +718,7 @@
     # The user's unique ID.
     string id?;
     # The site ID of the account.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # This object is an individual permission profile response.
     PermissionProfileResponse permission_profile?;
     # A list of groups that the user belongs to.
@@ -818,7 +820,7 @@
     # The user's unique ID.
     string id;
     # The site ID.
-    ballerina/lang.int:0.0.0:Signed32 site_id;
+    int:Signed32 site_id;
     # The full name of the user.
     string user_name?;
     # The user's first name.
@@ -925,7 +927,7 @@
 
 type AddDSGroupUsersResponse record {
     boolean is_success?;
-    ballerina/lang.int:0.0.0:Signed32 TotalCount?;
+    int:Signed32 TotalCount?;
     # A list of users.
     DSGroupUserResponse[] users?;
 };
@@ -1023,7 +1025,7 @@
 
 type RequiredAttributeMappingResponse record {
     # The unique ID of the attribute.
-    ballerina/lang.int:0.0.0:Signed32 required_attribute_id?;
+    int:Signed32 required_attribute_id?;
     # The name of the attribute.
     string required_attribute_name?;
     # The human-readable name of the attribute.
@@ -1045,7 +1047,7 @@
     # The user's unique ID.
     string id?;
     # The site ID of the organization.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The site name of the account.
     string site_name?;
     # The full name of the user.
@@ -1194,7 +1196,7 @@
     # The external account ID.
     int external_account_id?;
     # The site ID.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
 };
 
 # An ID object.
@@ -1304,7 +1306,7 @@
     # The unique ID of the task request.
     string id?;
     # The ID of the site the response is for.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The URL that returns the results as a CSV text stream.
     string url?;
     # The number of rows returned in the result.
@@ -1320,7 +1322,7 @@
     # The ID of the user whose email address has been updated.
     string id?;
     # The site ID.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The email address.
     string email?;
     # Errors.
@@ -1331,7 +1333,7 @@
 
 type MultiProductUserManagement record {
     string id?;
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The full name of the user.
     string user_name?;
     # The user's first name.
@@ -1372,7 +1374,7 @@
     # The ID of the added user
     string id?;
     # The site ID of the added user.
-    ballerina/lang.int:0.0.0:Signed32 site_id?;
+    int:Signed32 site_id?;
     # The full name of the user.
     string user_name?;
     # The user's first name.
@@ -1533,13 +1535,13 @@
 
 type PagingResponseProperties record {
     # The number of items in a result set (page).
-    ballerina/lang.int:0.0.0:Signed32 result_set_size?;
+    int:Signed32 result_set_size?;
     # The index position of the first result in this set.
-    ballerina/lang.int:0.0.0:Signed32 result_set_start_position?;
+    int:Signed32 result_set_start_position?;
     # The index position of the last result in this set.
-    ballerina/lang.int:0.0.0:Signed32 result_set_end_position?;
+    int:Signed32 result_set_end_position?;
     # The total number of results.
-    ballerina/lang.int:0.0.0:Signed32 total_set_size?;
+    int:Signed32 total_set_size?;
     # A URL to the next set of results. 
     string next?;
     # A URL to the previous set of results. 
@@ -1570,10 +1572,10 @@
 
 type DSGroupUsersResponse record {
     # The page number.
-    ballerina/lang.int:0.0.0:Signed32 page?;
+    int:Signed32 page?;
     # The number of items per page.
-    ballerina/lang.int:0.0.0:Signed32 page_size?;
-    ballerina/lang.int:0.0.0:Signed32 total_count?;
+    int:Signed32 page_size?;
+    int:Signed32 total_count?;
     # A list of users.
     DSGroupUserResponse[] users?;
 };
@@ -1599,14 +1601,14 @@
     string last_modified?;
     # Status.
     string status?;
-    ballerina/lang.int:0.0.0:Signed32 user_count?;
-    ballerina/lang.int:0.0.0:Signed32 processed_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 added_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 updated_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 closed_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 no_action_required_user_count?;
-    ballerina/lang.int:0.0.0:Signed32 error_count?;
-    ballerina/lang.int:0.0.0:Signed32 warning_count?;
+    int:Signed32 user_count?;
+    int:Signed32 processed_user_count?;
+    int:Signed32 added_user_count?;
+    int:Signed32 updated_user_count?;
+    int:Signed32 closed_user_count?;
+    int:Signed32 no_action_required_user_count?;
+    int:Signed32 error_count?;
+    int:Signed32 warning_count?;
     string invalid_column_headers?;
     string imports_not_found_or_not_available_for_accounts?;
     string imports_failed_for_accounts?;
@@ -1669,7 +1671,7 @@
     # When **true,** indicates that the account is compliant.
     boolean compliant?;
     # Reserved for DocuSign.
-    ballerina/lang.int:0.0.0:Signed32 siteId?;
+    int:Signed32 siteId?;
     # Reserved for DocuSign.
     string siteName?;
 };
@@ -1950,7 +1952,7 @@
     # Reserved for DocuSign.
     string orderId?;
     # The number of retries.
-    ballerina/lang.int:0.0.0:Signed32 attempts?;
+    int:Signed32 attempts?;
     # The date that the clone request was initiated.
     string createdDate?;
     # The name of the user who initiated the clone request.
@@ -2013,7 +2015,7 @@
     # A pre-configured GET request to get the status of the export. Generally this is the same URI used to access this endpoint.
     string metadata_url?;
     # An integer between 0 to 100 (inclusive) that reports the progress of the request.
-    ballerina/lang.int:0.0.0:Signed32 percent_completed?;
+    int:Signed32 percent_completed?;
     # The number of rows returned in this request.
     int number_rows?;
     # The size of the request in bytes.
@@ -2055,16 +2057,16 @@
 type OrgReportConfigurationResponse record {
     boolean is_account_limit_disabled?;
     boolean custom_dates_enabled?;
-    ballerina/lang.int:0.0.0:Signed32[] enabled_report_types?;
+    int:Signed32[] enabled_report_types?;
 };
 
 
 type DSGroupListResponse record {
     # The page number.
-    ballerina/lang.int:0.0.0:Signed32 page?;
+    int:Signed32 page?;
     # The number of items per page.
-    ballerina/lang.int:0.0.0:Signed32 page_size?;
-    ballerina/lang.int:0.0.0:Signed32 total_count?;
+    int:Signed32 page_size?;
+    int:Signed32 total_count?;
     # Select users that are members of the specified account. At least one of `email`, `account_id` or `organization_reserved_domain_id` must be specified.
     string account_id?;
     DSGroupResponse[] ds_groups?;
@@ -2089,7 +2091,7 @@
 
 
 type ForceActivateMembershipRequest record {
-    ballerina/lang.int:0.0.0:Signed32 site_id;
+    int:Signed32 site_id;
 };
 
 # Information about users to remove from the group.
`````

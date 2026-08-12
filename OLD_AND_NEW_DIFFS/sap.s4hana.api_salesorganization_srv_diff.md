# sap.s4hana.api_salesorganization_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_salesorganization_srv` |
| **Old file** | `sap.s4hana.api_salesorganization_srv/old/ballerinax_sap.s4hana.api_salesorganization_srv.bal.txt` |
| **New file** | `sap.s4hana.api_salesorganization_srv/new/ballerinax_sap.s4hana.api_salesorganization_srv.bal.txt` |
| **Old lines** | 365 |
| **New lines** | 371 |
| **Lines added** | 21 |
| **Lines removed** | 15 |
| **Hunks** | 10 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 9 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (9)

- `type A_SalesOrganizationExpandOptions`
- `type A_SalesOrganizationOrderByOptions`
- `type A_SalesOrganizationSelectOptions`
- `type A_SalesOrganizationTextExpandOptions`
- `type A_SalesOrganizationTextOrderByOptions`
- `type A_SalesOrganizationTextSelectOptions`
- `type SalesOrganizationOfA_SalesOrganizationTextExpandOptions`
- `type SalesOrganizationOfA_SalesOrganizationTextSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 124–132 | 124–132 | Types | +2 | −2 |
| 2 | 135–141 | 135–143 | Types | +2 | −0 |
| 3 | 143–148 | 145–151 | Types | +1 | −0 |
| 4 | 158–164 | 161–167 | Types | +1 | −1 |
| 5 | 169–177 | 172–180 | Types | +2 | −2 |
| 6 | 184–190 | 187–194 | Types | +2 | −1 |
| 7 | 202–211 | 206–216 | Types | +2 | −1 |
| 8 | 260–265 | 265–271 | Types | +1 | −0 |
| 9 | 291–299 | 297–305 | Types | +2 | −2 |
| 10 | 341–365 | 347–371 | Client | +6 | −6 |

---

## Unified diff

`````diff
--- sap.s4hana.api_salesorganization_srv/old/ballerinax_sap.s4hana.api_salesorganization_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_salesorganization_srv/new/ballerinax_sap.s4hana.api_salesorganization_srv.bal.txt	2026-08-12 13:19:19
@@ -124,9 +124,9 @@
     A_SalesOrganizationTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrganizationTextExpandOptions
+type A_SalesOrganizationTextExpandOptions "to_SalesOrganization"[];
 
-// Unknown type: A_SalesOrganizationTextSelectOptions
+type A_SalesOrganizationTextSelectOptions ("SalesOrganization"|"Language"|"SalesOrganizationName"|"to_SalesOrganization")[];
 
 
 type A_SalesOrganizationTextWrapper record {
@@ -135,7 +135,9 @@
 
 
 type A_SalesOrganizationText record {
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
+    @constraint:String {maxLength: 2}
     string Language?;
     string? SalesOrganizationName?;
     A_SalesOrganization to_SalesOrganization?;
@@ -143,6 +145,7 @@
 
 
 type A_SalesOrganization record {
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
     # Statistics currency
     string? SalesOrganizationCurrency?;
@@ -158,7 +161,7 @@
     A_SalesOrganizationText[] results?;
 };
 
-// Unknown type: SalesOrganizationOfA_SalesOrganizationTextExpandOptions
+type SalesOrganizationOfA_SalesOrganizationTextExpandOptions "to_Text"[];
 
 # Represents the Queries record for the operation: getA_SalesOrganization
 
@@ -169,9 +172,9 @@
     A_SalesOrganizationSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrganizationExpandOptions
+type A_SalesOrganizationExpandOptions "to_Text"[];
 
-// Unknown type: A_SalesOrganizationSelectOptions
+type A_SalesOrganizationSelectOptions ("SalesOrganization"|"SalesOrganizationCurrency"|"CompanyCode"|"IntercompanyBillingCustomer"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrganizationWrapper record {
@@ -184,7 +187,8 @@
     A_SalesOrganization[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
 
 type A_SalesOrganizationWrapper record {
@@ -202,10 +206,11 @@
     A_SalesOrganizationText[] results?;
 };
 
-// Unknown type: SalesOrganizationOfA_SalesOrganizationTextSelectOptions
+type SalesOrganizationOfA_SalesOrganizationTextSelectOptions ("SalesOrganization"|"SalesOrganizationCurrency"|"CompanyCode"|"IntercompanyBillingCustomer"|"to_Text")[];
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -260,6 +265,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -291,9 +297,9 @@
     A_SalesOrganizationTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrganizationTextOrderByOptions
+type A_SalesOrganizationTextOrderByOptions ("SalesOrganization"|"SalesOrganization desc"|"Language"|"Language desc"|"SalesOrganizationName"|"SalesOrganizationName desc")[];
 
-// Unknown type: A_SalesOrganizationOrderByOptions
+type A_SalesOrganizationOrderByOptions ("SalesOrganization"|"SalesOrganization desc"|"SalesOrganizationCurrency"|"SalesOrganizationCurrency desc"|"CompanyCode"|"CompanyCode desc"|"IntercompanyBillingCustomer"|"IntercompanyBillingCustomer desc")[];
 
 # Represents the Queries record for the operation: listA_SalesOrganizations
 
@@ -341,25 +347,25 @@
 
     # Get entity from A_SalesOrganization by key
     # 
-    remote function getA_SalesOrganization(string SalesOrganization, map<string|string[]> headers = {}, A_SalesOrganizationExpandOptions \$expand = [], A_SalesOrganizationSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrganizationQueries queries) returns A_SalesOrganizationWrapper|error;
+    remote function getA_SalesOrganization(string SalesOrganization, map<string|string[]> headers = {}, A_SalesOrganizationExpandOptions \$expand = [], A_SalesOrganizationSelectOptions \$select = [], GetA_SalesOrganizationQueries queries) returns A_SalesOrganizationWrapper|error;
 
     # Get entity from A_SalesOrganizationText by key
     # 
-    remote function getA_SalesOrganizationText(string SalesOrganization, string Language, map<string|string[]> headers = {}, A_SalesOrganizationTextExpandOptions \$expand = [], A_SalesOrganizationTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrganizationTextQueries queries) returns A_SalesOrganizationTextWrapper|error;
+    remote function getA_SalesOrganizationText(string SalesOrganization, string Language, map<string|string[]> headers = {}, A_SalesOrganizationTextExpandOptions \$expand = [], A_SalesOrganizationTextSelectOptions \$select = [], GetA_SalesOrganizationTextQueries queries) returns A_SalesOrganizationTextWrapper|error;
 
     # Get related to_SalesOrganization
     # 
-    remote function getSalesOrganizationOfA_SalesOrganizationText(string SalesOrganization, string Language, map<string|string[]> headers = {}, SalesOrganizationOfA_SalesOrganizationTextExpandOptions \$expand = [], SalesOrganizationOfA_SalesOrganizationTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrganizationOfA_SalesOrganizationTextQueries queries) returns A_SalesOrganizationWrapper|error;
+    remote function getSalesOrganizationOfA_SalesOrganizationText(string SalesOrganization, string Language, map<string|string[]> headers = {}, SalesOrganizationOfA_SalesOrganizationTextExpandOptions \$expand = [], SalesOrganizationOfA_SalesOrganizationTextSelectOptions \$select = [], GetSalesOrganizationOfA_SalesOrganizationTextQueries queries) returns A_SalesOrganizationWrapper|error;
 
     # Get entities from A_SalesOrganizationText
     # 
-    remote function listA_SalesOrganizationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationTextOrderByOptions \$orderby = [], A_SalesOrganizationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrganizationTextsQueries queries) returns CollectionOfA_SalesOrganizationTextWrapper|error;
+    remote function listA_SalesOrganizationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationTextOrderByOptions \$orderby = [], A_SalesOrganizationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationTextSelectOptions \$select = [], ListA_SalesOrganizationTextsQueries queries) returns CollectionOfA_SalesOrganizationTextWrapper|error;
 
     # Get entities from A_SalesOrganization
     # 
-    remote function listA_SalesOrganizations(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationOrderByOptions \$orderby = [], A_SalesOrganizationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrganizationsQueries queries) returns CollectionOfA_SalesOrganizationWrapper|error;
+    remote function listA_SalesOrganizations(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationOrderByOptions \$orderby = [], A_SalesOrganizationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationSelectOptions \$select = [], ListA_SalesOrganizationsQueries queries) returns CollectionOfA_SalesOrganizationWrapper|error;
 
     # Get entities from related to_Text
     # 
-    remote function listTextsOfA_SalesOrganization(string SalesOrganization, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationTextOrderByOptions \$orderby = [], A_SalesOrganizationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesOrganizationQueries queries) returns CollectionOfA_SalesOrganizationTextWrapper|error;
+    remote function listTextsOfA_SalesOrganization(string SalesOrganization, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrganizationTextOrderByOptions \$orderby = [], A_SalesOrganizationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrganizationTextSelectOptions \$select = [], ListTextsOfA_SalesOrganizationQueries queries) returns CollectionOfA_SalesOrganizationTextWrapper|error;
 }
`````

# sap.s4hana.api_salesdistrict_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_salesdistrict_srv` |
| **Old file** | `sap.s4hana.api_salesdistrict_srv/old/ballerinax_sap.s4hana.api_salesdistrict_srv.bal.txt` |
| **New file** | `sap.s4hana.api_salesdistrict_srv/new/ballerinax_sap.s4hana.api_salesdistrict_srv.bal.txt` |
| **Old lines** | 360 |
| **New lines** | 366 |
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

- `type A_SalesDistrictExpandOptions`
- `type A_SalesDistrictOrderByOptions`
- `type A_SalesDistrictSelectOptions`
- `type A_SalesDistrictTextExpandOptions`
- `type A_SalesDistrictTextOrderByOptions`
- `type A_SalesDistrictTextSelectOptions`
- `type SalesDistrictOfA_SalesDistrictTextExpandOptions`
- `type SalesDistrictOfA_SalesDistrictTextSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 115–121 | 115–121 | END README | +1 | −1 |
| 2 | 136–144 | 136–144 | Types | +2 | −2 |
| 3 | 149–155 | 149–155 | Types | +1 | −1 |
| 4 | 160–171 | 160–172 | Types | +3 | −2 |
| 5 | 177–183 | 178–186 | Types | +2 | −0 |
| 6 | 200–206 | 203–210 | Types | +2 | −1 |
| 7 | 223–228 | 227–233 | Types | +1 | −0 |
| 8 | 277–282 | 282–288 | Types | +1 | −0 |
| 9 | 289–297 | 295–303 | Types | +2 | −2 |
| 10 | 336–360 | 342–366 | Client | +6 | −6 |

---

## Unified diff

`````diff
--- sap.s4hana.api_salesdistrict_srv/old/ballerinax_sap.s4hana.api_salesdistrict_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_salesdistrict_srv/new/ballerinax_sap.s4hana.api_salesdistrict_srv.bal.txt	2026-08-12 13:19:19
@@ -115,7 +115,7 @@
 
 // --- Types ---
 
-// Unknown type: A_SalesDistrictTextExpandOptions
+type A_SalesDistrictTextExpandOptions "to_SalesDistrict"[];
 
 # Represents the Queries record for the operation: listTextsOfA_SalesDistrict
 
@@ -136,9 +136,9 @@
     A_SalesDistrictTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesDistrictTextOrderByOptions
+type A_SalesDistrictTextOrderByOptions ("SalesDistrict"|"SalesDistrict desc"|"Language"|"Language desc"|"SalesDistrictName"|"SalesDistrictName desc")[];
 
-// Unknown type: A_SalesDistrictTextSelectOptions
+type A_SalesDistrictTextSelectOptions ("SalesDistrict"|"Language"|"SalesDistrictName"|"to_SalesDistrict")[];
 
 # Represents the Queries record for the operation: getA_SalesDistrictText
 
@@ -149,7 +149,7 @@
     A_SalesDistrictTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesDistrictOrderByOptions
+type A_SalesDistrictOrderByOptions ("SalesDistrict"|"SalesDistrict desc")[];
 
 # Represents the Queries record for the operation: getA_SalesDistrict
 
@@ -160,12 +160,13 @@
     A_SalesDistrictSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesDistrictExpandOptions
+type A_SalesDistrictExpandOptions "to_Text"[];
 
-// Unknown type: A_SalesDistrictSelectOptions
+type A_SalesDistrictSelectOptions ("SalesDistrict"|"to_Text")[];
 
 
 type A_SalesDistrict record {
+    @constraint:String {maxLength: 6}
     string SalesDistrict?;
     A_SalesDistrict_to_Text to_Text?;
 };
@@ -177,7 +178,9 @@
 
 
 type A_SalesDistrictText record {
+    @constraint:String {maxLength: 6}
     string SalesDistrict?;
+    @constraint:String {maxLength: 2}
     string Language?;
     # Name of the District
     string? SalesDistrictName?;
@@ -200,7 +203,8 @@
     A_SalesDistrict[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
 # Represents the Queries record for the operation: listA_SalesDistrictTexts
 
@@ -223,6 +227,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -277,6 +282,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -289,9 +295,9 @@
     SalesDistrictOfA_SalesDistrictTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesDistrictOfA_SalesDistrictTextExpandOptions
+type SalesDistrictOfA_SalesDistrictTextExpandOptions "to_Text"[];
 
-// Unknown type: SalesDistrictOfA_SalesDistrictTextSelectOptions
+type SalesDistrictOfA_SalesDistrictTextSelectOptions ("SalesDistrict"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesDistricts
 
@@ -336,25 +342,25 @@
 
     # Get entity from A_SalesDistrict by key
     # 
-    remote function getA_SalesDistrict(string SalesDistrict, map<string|string[]> headers = {}, A_SalesDistrictExpandOptions \$expand = [], A_SalesDistrictSelectOptions \$select = [], anydata Additional Values, GetA_SalesDistrictQueries queries) returns A_SalesDistrictWrapper|error;
+    remote function getA_SalesDistrict(string SalesDistrict, map<string|string[]> headers = {}, A_SalesDistrictExpandOptions \$expand = [], A_SalesDistrictSelectOptions \$select = [], GetA_SalesDistrictQueries queries) returns A_SalesDistrictWrapper|error;
 
     # Get entity from A_SalesDistrictText by key
     # 
-    remote function getA_SalesDistrictText(string SalesDistrict, string Language, map<string|string[]> headers = {}, A_SalesDistrictTextExpandOptions \$expand = [], A_SalesDistrictTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesDistrictTextQueries queries) returns A_SalesDistrictTextWrapper|error;
+    remote function getA_SalesDistrictText(string SalesDistrict, string Language, map<string|string[]> headers = {}, A_SalesDistrictTextExpandOptions \$expand = [], A_SalesDistrictTextSelectOptions \$select = [], GetA_SalesDistrictTextQueries queries) returns A_SalesDistrictTextWrapper|error;
 
     # Get related to_SalesDistrict
     # 
-    remote function getSalesDistrictOfA_SalesDistrictText(string SalesDistrict, string Language, map<string|string[]> headers = {}, SalesDistrictOfA_SalesDistrictTextExpandOptions \$expand = [], SalesDistrictOfA_SalesDistrictTextSelectOptions \$select = [], anydata Additional Values, GetSalesDistrictOfA_SalesDistrictTextQueries queries) returns A_SalesDistrictWrapper|error;
+    remote function getSalesDistrictOfA_SalesDistrictText(string SalesDistrict, string Language, map<string|string[]> headers = {}, SalesDistrictOfA_SalesDistrictTextExpandOptions \$expand = [], SalesDistrictOfA_SalesDistrictTextSelectOptions \$select = [], GetSalesDistrictOfA_SalesDistrictTextQueries queries) returns A_SalesDistrictWrapper|error;
 
     # Get entities from A_SalesDistrictText
     # 
-    remote function listA_SalesDistrictTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictTextOrderByOptions \$orderby = [], A_SalesDistrictTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesDistrictTextsQueries queries) returns CollectionOfA_SalesDistrictTextWrapper|error;
+    remote function listA_SalesDistrictTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictTextOrderByOptions \$orderby = [], A_SalesDistrictTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictTextSelectOptions \$select = [], ListA_SalesDistrictTextsQueries queries) returns CollectionOfA_SalesDistrictTextWrapper|error;
 
     # Get entities from A_SalesDistrict
     # 
-    remote function listA_SalesDistricts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictOrderByOptions \$orderby = [], A_SalesDistrictExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictSelectOptions \$select = [], anydata Additional Values, ListA_SalesDistrictsQueries queries) returns CollectionOfA_SalesDistrictWrapper|error;
+    remote function listA_SalesDistricts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictOrderByOptions \$orderby = [], A_SalesDistrictExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictSelectOptions \$select = [], ListA_SalesDistrictsQueries queries) returns CollectionOfA_SalesDistrictWrapper|error;
 
     # Get entities from related to_Text
     # 
-    remote function listTextsOfA_SalesDistrict(string SalesDistrict, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictTextOrderByOptions \$orderby = [], A_SalesDistrictTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesDistrictQueries queries) returns CollectionOfA_SalesDistrictTextWrapper|error;
+    remote function listTextsOfA_SalesDistrict(string SalesDistrict, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesDistrictTextOrderByOptions \$orderby = [], A_SalesDistrictTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesDistrictTextSelectOptions \$select = [], ListTextsOfA_SalesDistrictQueries queries) returns CollectionOfA_SalesDistrictTextWrapper|error;
 }
`````

# sap.s4hana.api_sd_incoterms_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sd_incoterms_srv` |
| **Old file** | `sap.s4hana.api_sd_incoterms_srv/old/ballerinax_sap.s4hana.api_sd_incoterms_srv.bal.txt` |
| **New file** | `sap.s4hana.api_sd_incoterms_srv/new/ballerinax_sap.s4hana.api_sd_incoterms_srv.bal.txt` |
| **Old lines** | 498 |
| **New lines** | 507 |
| **Lines added** | 34 |
| **Lines removed** | 25 |
| **Hunks** | 14 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 15 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (15)

- `type A_IncotermsClassificationExpandOptions`
- `type A_IncotermsClassificationOrderByOptions`
- `type A_IncotermsClassificationSelectOptions`
- `type A_IncotermsClassificationTextOrderByOptions`
- `type A_IncotermsClassificationTextSelectOptions`
- `type A_IncotermsVersionExpandOptions`
- `type A_IncotermsVersionOrderByOptions`
- `type A_IncotermsVersionSelectOptions`
- `type A_IncotermsVersionTextOrderByOptions`
- `type A_IncotermsVersionTextSelectOptions`
- `type IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions`
- `type IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions`
- `type IncotermsVersionTextOfA_IncotermsVersionOrderByOptions`
- `type IncotermsVersionTextOfA_IncotermsVersionSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 115–121 | 115–121 | END README | +1 | −1 |
| 2 | 123–133 | 123–136 | Types | +4 | −1 |
| 3 | 135–141 | 138–146 | Types | +2 | −0 |
| 4 | 157–165 | 162–170 | Types | +2 | −2 |
| 5 | 168–178 | 173–183 | Types | +3 | −3 |
| 6 | 187–192 | 192–198 | Types | +1 | −0 |
| 7 | 196–202 | 202–208 | Types | +1 | −1 |
| 8 | 215–221 | 221–227 | Types | +1 | −1 |
| 9 | 226–231 | 232–238 | Types | +1 | −0 |
| 10 | 254–266 | 261–273 | Types | +4 | −4 |
| 11 | 269–274 | 276–282 | Types | +1 | −0 |
| 12 | 323–328 | 331–337 | Types | +1 | −0 |
| 13 | 356–364 | 365–373 | Types | +2 | −2 |
| 14 | 454–496 | 463–505 | Client | +10 | −10 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sd_incoterms_srv/old/ballerinax_sap.s4hana.api_sd_incoterms_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sd_incoterms_srv/new/ballerinax_sap.s4hana.api_sd_incoterms_srv.bal.txt	2026-08-12 13:19:19
@@ -115,7 +115,7 @@
 
 // --- Types ---
 
-// Unknown type: A_IncotermsClassificationTextOrderByOptions
+type A_IncotermsClassificationTextOrderByOptions ("IncotermsClassification"|"IncotermsClassification desc"|"Language"|"Language desc"|"IncotermsClassificationName"|"IncotermsClassificationName desc")[];
 
 
 type CollectionOfA_IncotermsVersionText record {
@@ -123,11 +123,14 @@
     A_IncotermsVersionText[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
 
 type A_IncotermsVersionText record {
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
+    @constraint:String {maxLength: 2}
     string Language?;
     string? IncotermsVersionName?;
 };
@@ -135,7 +138,9 @@
 
 type A_IncotermsClassificationText record {
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 2}
     string Language?;
     string? IncotermsClassificationName?;
 };
@@ -157,9 +162,9 @@
     IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions \$select?;
 };
 
-// Unknown type: IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions
+type IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions ("IncotermsClassification"|"IncotermsClassification desc"|"Language"|"Language desc"|"IncotermsClassificationName"|"IncotermsClassificationName desc")[];
 
-// Unknown type: IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions
+type IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions ("IncotermsClassification"|"Language"|"IncotermsClassificationName")[];
 
 # Represents the Queries record for the operation: getA_IncotermsClassificationText
 
@@ -168,11 +173,11 @@
     A_IncotermsClassificationTextSelectOptions \$select?;
 };
 
-// Unknown type: A_IncotermsClassificationTextSelectOptions
+type A_IncotermsClassificationTextSelectOptions ("IncotermsClassification"|"Language"|"IncotermsClassificationName")[];
 
-// Unknown type: A_IncotermsVersionTextOrderByOptions
+type A_IncotermsVersionTextOrderByOptions ("IncotermsVersion"|"IncotermsVersion desc"|"Language"|"Language desc"|"IncotermsVersionName"|"IncotermsVersionName desc")[];
 
-// Unknown type: A_IncotermsVersionExpandOptions
+type A_IncotermsVersionExpandOptions "to_IncotermsVersionText"[];
 
 
 type CollectionOfA_IncotermsVersionWrapper record {
@@ -187,6 +192,7 @@
 
 
 type A_IncotermsVersion record {
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
     A_IncotermsVersion_to_IncotermsVersionText to_IncotermsVersionText?;
 };
@@ -196,7 +202,7 @@
     A_IncotermsVersionText[] results?;
 };
 
-// Unknown type: A_IncotermsClassificationExpandOptions
+type A_IncotermsClassificationExpandOptions "to_IncotermsClassificationText"[];
 
 # Represents the Queries record for the operation: listA_IncotermsVersionTexts
 
@@ -215,7 +221,7 @@
     A_IncotermsVersionTextSelectOptions \$select?;
 };
 
-// Unknown type: A_IncotermsVersionTextSelectOptions
+type A_IncotermsVersionTextSelectOptions ("IncotermsVersion"|"Language"|"IncotermsVersionName")[];
 
 
 type CollectionOfA_IncotermsClassification record {
@@ -226,6 +232,7 @@
 
 type A_IncotermsClassification record {
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
     # Location is mandatory
     boolean? LocationIsMandatory?;
@@ -254,13 +261,13 @@
     IncotermsVersionTextOfA_IncotermsVersionSelectOptions \$select?;
 };
 
-// Unknown type: IncotermsVersionTextOfA_IncotermsVersionOrderByOptions
+type IncotermsVersionTextOfA_IncotermsVersionOrderByOptions ("IncotermsVersion"|"IncotermsVersion desc"|"Language"|"Language desc"|"IncotermsVersionName"|"IncotermsVersionName desc")[];
 
-// Unknown type: IncotermsVersionTextOfA_IncotermsVersionSelectOptions
+type IncotermsVersionTextOfA_IncotermsVersionSelectOptions ("IncotermsVersion"|"Language"|"IncotermsVersionName")[];
 
-// Unknown type: A_IncotermsVersionOrderByOptions
+type A_IncotermsVersionOrderByOptions ("IncotermsVersion"|"IncotermsVersion desc")[];
 
-// Unknown type: A_IncotermsVersionSelectOptions
+type A_IncotermsVersionSelectOptions ("IncotermsVersion"|"to_IncotermsVersionText")[];
 
 
 type A_IncotermsVersionTextWrapper record {
@@ -269,6 +276,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -323,6 +331,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -356,9 +365,9 @@
     A_IncotermsClassificationSelectOptions \$select?;
 };
 
-// Unknown type: A_IncotermsClassificationOrderByOptions
+type A_IncotermsClassificationOrderByOptions ("IncotermsClassification"|"IncotermsClassification desc"|"LocationIsMandatory"|"LocationIsMandatory desc")[];
 
-// Unknown type: A_IncotermsClassificationSelectOptions
+type A_IncotermsClassificationSelectOptions ("IncotermsClassification"|"LocationIsMandatory"|"to_IncotermsClassificationText")[];
 
 
 type CollectionOfA_IncotermsClassificationWrapper record {
@@ -454,43 +463,43 @@
 
     # Reads the ID and description of a specific Incoterm.
     # 
-    remote function getA_IncotermsClassification(string IncotermsClassification, map<string|string[]> headers = {}, A_IncotermsClassificationExpandOptions \$expand = [], A_IncotermsClassificationSelectOptions \$select = [], anydata Additional Values, GetA_IncotermsClassificationQueries queries) returns A_IncotermsClassificationWrapper|error;
+    remote function getA_IncotermsClassification(string IncotermsClassification, map<string|string[]> headers = {}, A_IncotermsClassificationExpandOptions \$expand = [], A_IncotermsClassificationSelectOptions \$select = [], GetA_IncotermsClassificationQueries queries) returns A_IncotermsClassificationWrapper|error;
 
     # Reads the description of a specific Incoterm in a specific language.
     # 
-    remote function getA_IncotermsClassificationText(string IncotermsClassification, string Language, map<string|string[]> headers = {}, A_IncotermsClassificationTextSelectOptions \$select = [], anydata Additional Values, GetA_IncotermsClassificationTextQueries queries) returns A_IncotermsClassificationTextWrapper|error;
+    remote function getA_IncotermsClassificationText(string IncotermsClassification, string Language, map<string|string[]> headers = {}, A_IncotermsClassificationTextSelectOptions \$select = [], GetA_IncotermsClassificationTextQueries queries) returns A_IncotermsClassificationTextWrapper|error;
 
     # Reads the ID and description of a specific Incoterms version.
     # 
-    remote function getA_IncotermsVersion(string IncotermsVersion, map<string|string[]> headers = {}, A_IncotermsVersionExpandOptions \$expand = [], A_IncotermsVersionSelectOptions \$select = [], anydata Additional Values, GetA_IncotermsVersionQueries queries) returns A_IncotermsVersionWrapper|error;
+    remote function getA_IncotermsVersion(string IncotermsVersion, map<string|string[]> headers = {}, A_IncotermsVersionExpandOptions \$expand = [], A_IncotermsVersionSelectOptions \$select = [], GetA_IncotermsVersionQueries queries) returns A_IncotermsVersionWrapper|error;
 
     # Reads the description of a specific Incoterms version in a specific language.
     # 
-    remote function getA_IncotermsVersionText(string IncotermsVersion, string Language, map<string|string[]> headers = {}, A_IncotermsVersionTextSelectOptions \$select = [], anydata Additional Values, GetA_IncotermsVersionTextQueries queries) returns A_IncotermsVersionTextWrapper|error;
+    remote function getA_IncotermsVersionText(string IncotermsVersion, string Language, map<string|string[]> headers = {}, A_IncotermsVersionTextSelectOptions \$select = [], GetA_IncotermsVersionTextQueries queries) returns A_IncotermsVersionTextWrapper|error;
 
     # Reads the descriptions of all Incoterms.
     # 
-    remote function listA_IncotermsClassificationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsClassificationTextOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsClassificationTextSelectOptions \$select = [], anydata Additional Values, ListA_IncotermsClassificationTextsQueries queries) returns CollectionOfA_IncotermsClassificationTextWrapper|error;
+    remote function listA_IncotermsClassificationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsClassificationTextOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsClassificationTextSelectOptions \$select = [], ListA_IncotermsClassificationTextsQueries queries) returns CollectionOfA_IncotermsClassificationTextWrapper|error;
 
     # Reads the IDs and descriptions of all Incoterms.
     # 
-    remote function listA_IncotermsClassifications(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsClassificationOrderByOptions \$orderby = [], A_IncotermsClassificationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsClassificationSelectOptions \$select = [], anydata Additional Values, ListA_IncotermsClassificationsQueries queries) returns CollectionOfA_IncotermsClassificationWrapper|error;
+    remote function listA_IncotermsClassifications(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsClassificationOrderByOptions \$orderby = [], A_IncotermsClassificationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsClassificationSelectOptions \$select = [], ListA_IncotermsClassificationsQueries queries) returns CollectionOfA_IncotermsClassificationWrapper|error;
 
     # Reads the descriptions of all Incoterms versions.
     # 
-    remote function listA_IncotermsVersionTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsVersionTextOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsVersionTextSelectOptions \$select = [], anydata Additional Values, ListA_IncotermsVersionTextsQueries queries) returns CollectionOfA_IncotermsVersionTextWrapper|error;
+    remote function listA_IncotermsVersionTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsVersionTextOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsVersionTextSelectOptions \$select = [], ListA_IncotermsVersionTextsQueries queries) returns CollectionOfA_IncotermsVersionTextWrapper|error;
 
     # Reads the IDs and descriptions of all Incoterms versions.
     # 
-    remote function listA_IncotermsVersions(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsVersionOrderByOptions \$orderby = [], A_IncotermsVersionExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsVersionSelectOptions \$select = [], anydata Additional Values, ListA_IncotermsVersionsQueries queries) returns CollectionOfA_IncotermsVersionWrapper|error;
+    remote function listA_IncotermsVersions(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_IncotermsVersionOrderByOptions \$orderby = [], A_IncotermsVersionExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_IncotermsVersionSelectOptions \$select = [], ListA_IncotermsVersionsQueries queries) returns CollectionOfA_IncotermsVersionWrapper|error;
 
     # Reads the description of a specific Incoterm.
     # 
-    remote function listIncotermsClassificationTextsOfA_IncotermsClassification(string IncotermsClassification, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions \$select = [], anydata Additional Values, ListIncotermsClassificationTextsOfA_IncotermsClassificationQueries queries) returns CollectionOfA_IncotermsClassificationTextWrapper|error;
+    remote function listIncotermsClassificationTextsOfA_IncotermsClassification(string IncotermsClassification, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", IncotermsClassificationTextOfA_IncotermsClassificationOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", IncotermsClassificationTextOfA_IncotermsClassificationSelectOptions \$select = [], ListIncotermsClassificationTextsOfA_IncotermsClassificationQueries queries) returns CollectionOfA_IncotermsClassificationTextWrapper|error;
 
     # Reads the description of a specific Incoterms version.
     # 
-    remote function listIncotermsVersionTextsOfA_IncotermsVersion(string IncotermsVersion, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", IncotermsVersionTextOfA_IncotermsVersionOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", IncotermsVersionTextOfA_IncotermsVersionSelectOptions \$select = [], anydata Additional Values, ListIncotermsVersionTextsOfA_IncotermsVersionQueries queries) returns CollectionOfA_IncotermsVersionTextWrapper|error;
+    remote function listIncotermsVersionTextsOfA_IncotermsVersion(string IncotermsVersion, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", IncotermsVersionTextOfA_IncotermsVersionOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", IncotermsVersionTextOfA_IncotermsVersionSelectOptions \$select = [], ListIncotermsVersionTextsOfA_IncotermsVersionQueries queries) returns CollectionOfA_IncotermsVersionTextWrapper|error;
 
     # Send a group of requests
     # 
`````

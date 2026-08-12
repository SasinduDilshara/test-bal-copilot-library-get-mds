# sap.s4hana.api_sd_sa_soldtopartydetn — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sd_sa_soldtopartydetn` |
| **Old file** | `sap.s4hana.api_sd_sa_soldtopartydetn/old/ballerinax_sap.s4hana.api_sd_sa_soldtopartydetn.bal.txt` |
| **New file** | `sap.s4hana.api_sd_sa_soldtopartydetn/new/ballerinax_sap.s4hana.api_sd_sa_soldtopartydetn.bal.txt` |
| **Old lines** | 250 |
| **New lines** | 256 |
| **Lines added** | 11 |
| **Lines removed** | 5 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (3)

- `type A_DelivSchedSoldToPartyDetnOrderByOptions`
- `type A_DelivSchedSoldToPartyDetnSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 118–126 | 118–129 | Types | +3 | −0 |
| 2 | 146–164 | 149–169 | Types | +5 | −3 |
| 3 | 197–202 | 202–208 | Types | +1 | −0 |
| 4 | 238–248 | 244–254 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sd_sa_soldtopartydetn/old/ballerinax_sap.s4hana.api_sd_sa_soldtopartydetn.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sd_sa_soldtopartydetn/new/ballerinax_sap.s4hana.api_sd_sa_soldtopartydetn.bal.txt	2026-08-12 13:19:19
@@ -118,9 +118,12 @@
 
 type A_DelivSchedSoldToPartyDetn record {
     # Supplier Number at Customer Location
+    @constraint:String {maxLength: 17}
     string Supplier?;
     # Cust.-Specif. Descr. of Business Partner (Plant, Stor. Loc.)
+    @constraint:String {maxLength: 30}
     string PartnerDescription?;
+    @constraint:String {maxLength: 25}
     string UnloadingPointName?;
     string? SoldToParty?;
 };
@@ -146,19 +149,21 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
-// Unknown type: A_DelivSchedSoldToPartyDetnSelectOptions
+type A_DelivSchedSoldToPartyDetnSelectOptions ("Supplier"|"PartnerDescription"|"UnloadingPointName"|"SoldToParty")[];
 
 
 type A_DelivSchedSoldToPartyDetnWrapper record {
     A_DelivSchedSoldToPartyDetn d?;
 };
 
-// Unknown type: A_DelivSchedSoldToPartyDetnOrderByOptions
+type A_DelivSchedSoldToPartyDetnOrderByOptions ("Supplier"|"Supplier desc"|"PartnerDescription"|"PartnerDescription desc"|"UnloadingPointName"|"UnloadingPointName desc"|"SoldToParty"|"SoldToParty desc")[];
 
 
 type CollectionOfA_DelivSchedSoldToPartyDetn record {
@@ -197,6 +202,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -238,11 +244,11 @@
 
     # Reads a specific sold-to party assignment.
     # 
-    remote function getA_DelivSchedSoldToPartyDetn(string Supplier, string PartnerDescription, string UnloadingPointName, map<string|string[]> headers = {}, A_DelivSchedSoldToPartyDetnSelectOptions \$select = [], anydata Additional Values, GetA_DelivSchedSoldToPartyDetnQueries queries) returns A_DelivSchedSoldToPartyDetnWrapper|error;
+    remote function getA_DelivSchedSoldToPartyDetn(string Supplier, string PartnerDescription, string UnloadingPointName, map<string|string[]> headers = {}, A_DelivSchedSoldToPartyDetnSelectOptions \$select = [], GetA_DelivSchedSoldToPartyDetnQueries queries) returns A_DelivSchedSoldToPartyDetnWrapper|error;
 
     # Reads all sold-to party assignments.
     # 
-    remote function listA_DelivSchedSoldToPartyDetns(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_DelivSchedSoldToPartyDetnOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_DelivSchedSoldToPartyDetnSelectOptions \$select = [], anydata Additional Values, ListA_DelivSchedSoldToPartyDetnsQueries queries) returns CollectionOfA_DelivSchedSoldToPartyDetnWrapper|error;
+    remote function listA_DelivSchedSoldToPartyDetns(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_DelivSchedSoldToPartyDetnOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_DelivSchedSoldToPartyDetnSelectOptions \$select = [], ListA_DelivSchedSoldToPartyDetnsQueries queries) returns CollectionOfA_DelivSchedSoldToPartyDetnWrapper|error;
 
     # Send a group of requests
     # 
`````

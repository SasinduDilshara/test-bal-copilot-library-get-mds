# sap.s4hana.salesarea_0001 — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.salesarea_0001` |
| **Old file** | `sap.s4hana.salesarea_0001/old/ballerinax_sap.s4hana.salesarea_0001.bal.txt` |
| **New file** | `sap.s4hana.salesarea_0001/new/ballerinax_sap.s4hana.salesarea_0001.bal.txt` |
| **Old lines** | 238 |
| **New lines** | 243 |
| **Lines added** | 9 |
| **Lines removed** | 4 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type SalesAreaOrderByOptions`
- `type SalesAreaSelectOptions`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 122–128 | 122–128 | Types | +1 | −1 |
| 2 | 145–150 | 145–151 | Types | +1 | −0 |
| 3 | 165–179 | 166–183 | Types | +4 | −1 |
| 4 | 185–190 | 189–195 | Types | +1 | −0 |
| 5 | 226–236 | 231–241 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- sap.s4hana.salesarea_0001/old/ballerinax_sap.s4hana.salesarea_0001.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.salesarea_0001/new/ballerinax_sap.s4hana.salesarea_0001.bal.txt	2026-08-12 13:19:19
@@ -122,7 +122,7 @@
     SalesAreaSelectOptions \$select?;
 };
 
-// Unknown type: SalesAreaSelectOptions
+type SalesAreaSelectOptions ("SalesOrganization"|"DistributionChannel"|"Division")[];
 
 # Provides settings related to HTTP/1.x protocol.
 
@@ -145,6 +145,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -165,15 +166,18 @@
     SalesAreaSelectOptions \$select?;
 };
 
-// Unknown type: SalesAreaOrderByOptions
+type SalesAreaOrderByOptions ("SalesOrganization"|"SalesOrganization desc"|"DistributionChannel"|"DistributionChannel desc"|"Division"|"Division desc")[];
 
 # The number of entities in the collection. Available when using the [$count](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount) query option.
 type count decimal|string;
 
 
 type SalesArea record {
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
+    @constraint:String {maxLength: 2}
     string DistributionChannel?;
+    @constraint:String {maxLength: 2}
     string Division?;
 };
 
@@ -185,6 +189,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -226,11 +231,11 @@
 
     # Get entity from SalesArea by key
     # 
-    remote function getSalesArea(string SalesOrganization, string DistributionChannel, string Division, map<string|string[]> headers = {}, SalesAreaSelectOptions \$select = [], anydata Additional Values, GetSalesAreaQueries queries) returns SalesArea|error;
+    remote function getSalesArea(string SalesOrganization, string DistributionChannel, string Division, map<string|string[]> headers = {}, SalesAreaSelectOptions \$select = [], GetSalesAreaQueries queries) returns SalesArea|error;
 
     # Get entities from SalesArea
     # 
-    remote function listSalesAreas(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesAreaOrderByOptions \$orderby = [], boolean \$count = false, SalesAreaSelectOptions \$select = [], anydata Additional Values, ListSalesAreasQueries queries) returns CollectionOfSalesArea|error;
+    remote function listSalesAreas(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesAreaOrderByOptions \$orderby = [], boolean \$count = false, SalesAreaSelectOptions \$select = [], ListSalesAreasQueries queries) returns CollectionOfSalesArea|error;
 
     # Send a group of requests
     # 
`````

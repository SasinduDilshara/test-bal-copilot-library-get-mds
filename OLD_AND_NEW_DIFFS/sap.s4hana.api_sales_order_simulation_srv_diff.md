# sap.s4hana.api_sales_order_simulation_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sales_order_simulation_srv` |
| **Old file** | `sap.s4hana.api_sales_order_simulation_srv/old/ballerinax_sap.s4hana.api_sales_order_simulation_srv.bal.txt` |
| **New file** | `sap.s4hana.api_sales_order_simulation_srv/new/ballerinax_sap.s4hana.api_sales_order_simulation_srv.bal.txt` |
| **Old lines** | 1062 |
| **New lines** | 1102 |
| **Lines added** | 45 |
| **Lines removed** | 5 |
| **Hunks** | 22 |

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

- `type A_SlsOrdSimlnValAddedSrvcOrderByOptions`
- `type A_SlsOrdSimlnValAddedSrvcSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 122–129 | 122–131 | Types | +2 | −0 |
| 2 | 145–150 | 147–153 | Types | +1 | −0 |
| 3 | 234–239 | 237–243 | Types | +1 | −0 |
| 4 | 314–319 | 318–324 | Types | +1 | −0 |
| 5 | 335–342 | 340–349 | Types | +2 | −0 |
| 6 | 364–369 | 371–377 | Types | +1 | −0 |
| 7 | 392–397 | 400–406 | Types | +1 | −0 |
| 8 | 419–426 | 428–438 | Types | +3 | −0 |
| 9 | 444–449 | 456–462 | Types | +1 | −0 |
| 10 | 522–527 | 535–541 | Types | +1 | −0 |
| 11 | 535–542 | 549–558 | Types | +2 | −0 |
| 12 | 664–672 | 680–691 | Types | +3 | −0 |
| 13 | 688–698 | 707–721 | Types | +4 | −0 |
| 14 | 740–746 | 763–771 | Types | +2 | −0 |
| 15 | 756–761 | 781–787 | Types | +1 | −0 |
| 16 | 771–779 | 797–808 | Types | +3 | −0 |
| 17 | 813–819 | 842–848 | Types | +1 | −1 |
| 18 | 853–859 | 882–888 | Types | +1 | −1 |
| 19 | 883–893 | 912–926 | Types | +4 | −0 |
| 20 | 926–935 | 959–970 | Types | +3 | −1 |
| 21 | 984–999 | 1019–1039 | Types | +5 | −0 |
| 22 | 1046–1056 | 1086–1096 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sales_order_simulation_srv/old/ballerinax_sap.s4hana.api_sales_order_simulation_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sales_order_simulation_srv/new/ballerinax_sap.s4hana.api_sales_order_simulation_srv.bal.txt	2026-08-12 13:19:19
@@ -122,8 +122,10 @@
 
 
 type CreateA_SalesOrderPrcgElmntSimln record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -145,6 +147,7 @@
 
 
 type CreateA_SalesOrderSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     string? SalesOrderType?;
     string? SalesOrganization?;
@@ -234,6 +237,7 @@
 
 type CreateA_SalesOrderItemSimulation record {
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -314,6 +318,7 @@
 
 
 type CreateA_SalesOrderItemPartnerSimln record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -335,8 +340,10 @@
 
 
 type CreateA_SalesOrderItmPrcgElmntSimln record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -364,6 +371,7 @@
 
 
 type CreateA_SalesOrderScheduleLineSimln record {
+    @constraint:String {maxLength: 4}
     string ScheduleLine;
     # Requested Delivery Date
     string? RequestedDeliveryDate?;
@@ -392,6 +400,7 @@
 
 
 type CreateA_SalesOrderPartnerSimulation record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -419,8 +428,11 @@
 
 
 type A_SalesOrderScheduleLineSimln record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 4}
     string ScheduleLine?;
     # Requested Delivery Date
     string? RequestedDeliveryDate?;
@@ -444,6 +456,7 @@
 
 
 type A_SalesOrderSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     string? SalesOrderType?;
     string? SalesOrganization?;
@@ -522,6 +535,7 @@
 
 
 type A_SalesOrderCreditSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Overall Status of Credit Checks
     string? TotalCreditCheckStatus?;
@@ -535,8 +549,10 @@
 
 
 type A_SalesOrderItemSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -664,9 +680,12 @@
 
 
 type A_SalesOrderItemPartnerSimln record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -688,11 +707,15 @@
 
 
 type A_SalesOrderItmPrcgElmntSimln record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionType?;
     # Condition Pricing Date
@@ -740,7 +763,9 @@
 
 
 type A_SalesOrderPartnerSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -756,6 +781,7 @@
 
 
 type A_SalesOrderPricingSimulation record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Net Value of the Sales Document in Document Currency
     string? TotalNetAmount?;
@@ -771,9 +797,12 @@
 
 
 type A_SalesOrderPrcgElmntSimln record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionType?;
     # Condition Pricing Date
@@ -813,7 +842,7 @@
     A_SalesOrderSimulation to_SalesOrder?;
 };
 
-// Unknown type: A_SlsOrdSimlnValAddedSrvcOrderByOptions
+type A_SlsOrdSimlnValAddedSrvcOrderByOptions ("ValueAddedServiceType"|"ValueAddedServiceType desc"|"ValueAddedSubServiceType"|"ValueAddedSubServiceType desc"|"SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"ValAddedSrvcTransactionNumber"|"ValAddedSrvcTransactionNumber desc"|"ValAddedSrvcItemGroup"|"ValAddedSrvcItemGroup desc"|"ValAddedSrvcItemNumber"|"ValAddedSrvcItemNumber desc"|"ValueAddedServiceProduct"|"ValueAddedServiceProduct desc"|"ValAddedSrvcHasToBeOrdered"|"ValAddedSrvcHasToBeOrdered desc"|"ValAddedSrvcIncrement"|"ValAddedSrvcIncrement desc"|"ValueAddedServiceChargeCode"|"ValueAddedServiceChargeCode desc"|"ValAddedSrvcIsCreatedManually"|"ValAddedSrvcIsCreatedManually desc"|"ValAddedSrvcItemNumberInSD"|"ValAddedSrvcItemNumberInSD desc"|"ValAddedSrvcIsRlvtForProcmt"|"ValAddedSrvcIsRlvtForProcmt desc"|"ValueAddedServiceText1"|"ValueAddedServiceText1 desc"|"ValueAddedServiceText2"|"ValueAddedServiceText2 desc"|"ValueAddedServiceText3"|"ValueAddedServiceText3 desc")[];
 
 
 type UpdateA_SlsOrdSimlnValAddedSrvc record {
@@ -853,7 +882,7 @@
     A_SlsOrdSimlnValAddedSrvcSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsOrdSimlnValAddedSrvcSelectOptions
+type A_SlsOrdSimlnValAddedSrvcSelectOptions ("ValueAddedServiceType"|"ValueAddedSubServiceType"|"SalesOrder"|"SalesOrderItem"|"ValAddedSrvcTransactionNumber"|"ValAddedSrvcItemGroup"|"ValAddedSrvcItemNumber"|"ValueAddedServiceProduct"|"ValAddedSrvcHasToBeOrdered"|"ValAddedSrvcIncrement"|"ValueAddedServiceChargeCode"|"ValAddedSrvcIsCreatedManually"|"ValAddedSrvcItemNumberInSD"|"ValAddedSrvcIsRlvtForProcmt"|"ValueAddedServiceText1"|"ValueAddedServiceText2"|"ValueAddedServiceText3"|"ValueAddedServiceLongText")[];
 
 
 type Modified\ A_SlsOrdSimlnValAddedSrvcType record {
@@ -883,11 +912,15 @@
 
 
 type A_SlsOrdSimlnValAddedSrvc record {
+    @constraint:String {maxLength: 2}
     string ValueAddedServiceType?;
+    @constraint:String {maxLength: 5}
     string ValueAddedSubServiceType?;
     # Document Number of Reference Document
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Item Number of the Reference Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     string? ValAddedSrvcTransactionNumber?;
     string? ValAddedSrvcItemGroup?;
@@ -926,10 +959,12 @@
     A_SlsOrdSimlnValAddedSrvc[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -984,16 +1019,21 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
 
 type CreateA_SlsOrdSimlnValAddedSrvc record {
+    @constraint:String {maxLength: 2}
     string ValueAddedServiceType;
+    @constraint:String {maxLength: 5}
     string ValueAddedSubServiceType;
     # Document Number of Reference Document
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # Item Number of the Reference Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # VAS Material Number
     string? ValueAddedServiceProduct?;
@@ -1046,11 +1086,11 @@
 
     # Get entity from A_SlsOrdSimlnValAddedSrvc by key
     # 
-    remote function getA_SlsOrdSimlnValAddedSrvc(string ValueAddedServiceType, string ValueAddedSubServiceType, string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SlsOrdSimlnValAddedSrvcSelectOptions \$select = [], anydata Additional Values, GetA_SlsOrdSimlnValAddedSrvcQueries queries) returns A_SlsOrdSimlnValAddedSrvcWrapper|error;
+    remote function getA_SlsOrdSimlnValAddedSrvc(string ValueAddedServiceType, string ValueAddedSubServiceType, string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SlsOrdSimlnValAddedSrvcSelectOptions \$select = [], GetA_SlsOrdSimlnValAddedSrvcQueries queries) returns A_SlsOrdSimlnValAddedSrvcWrapper|error;
 
     # Get entities from A_SlsOrdSimlnValAddedSrvc
     # 
-    remote function listA_SlsOrdSimlnValAddedSrvcs(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrdSimlnValAddedSrvcOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrdSimlnValAddedSrvcSelectOptions \$select = [], anydata Additional Values, ListA_SlsOrdSimlnValAddedSrvcsQueries queries) returns CollectionOfA_SlsOrdSimlnValAddedSrvcWrapper|error;
+    remote function listA_SlsOrdSimlnValAddedSrvcs(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrdSimlnValAddedSrvcOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrdSimlnValAddedSrvcSelectOptions \$select = [], ListA_SlsOrdSimlnValAddedSrvcsQueries queries) returns CollectionOfA_SlsOrdSimlnValAddedSrvcWrapper|error;
 
     # Update entity in A_SlsOrdSimlnValAddedSrvc
     # 
`````

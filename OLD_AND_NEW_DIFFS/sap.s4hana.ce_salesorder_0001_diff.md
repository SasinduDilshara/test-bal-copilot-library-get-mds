# sap.s4hana.ce_salesorder_0001 — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.ce_salesorder_0001` |
| **Old file** | `sap.s4hana.ce_salesorder_0001/old/ballerinax_sap.s4hana.ce_salesorder_0001.bal.txt` |
| **New file** | `sap.s4hana.ce_salesorder_0001/new/ballerinax_sap.s4hana.ce_salesorder_0001.bal.txt` |
| **Old lines** | 2070 |
| **New lines** | 2419 |
| **Lines added** | 434 |
| **Lines removed** | 85 |
| **Hunks** | 57 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 47 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (47)

- `type ItemOfSalesOrderItemPartnerExpandOptions`
- `type ItemOfSalesOrderItemPartnerSelectOptions`
- `type ItemOfSalesOrderItemPricingElementExpandOptions`
- `type ItemOfSalesOrderItemPricingElementSelectOptions`
- `type ItemOfSalesOrderItemTextExpandOptions`
- `type ItemOfSalesOrderItemTextSelectOptions`
- `type ItemOfSalesOrderScheduleLineExpandOptions`
- `type ItemOfSalesOrderScheduleLineSelectOptions`
- `type ItemPartnerOfSalesOrderItemExpandOptions`
- `type ItemPartnerOfSalesOrderItemOrderByOptions`
- `type ItemPartnerOfSalesOrderItemSelectOptions`
- `type ItemPricingElementOfSalesOrderItemExpandOptions`
- `type ItemPricingElementOfSalesOrderItemOrderByOptions`
- `type ItemPricingElementOfSalesOrderItemSelectOptions`
- `type ItemTextOfSalesOrderItemExpandOptions`
- `type ItemTextOfSalesOrderItemOrderByOptions`
- `type ItemTextOfSalesOrderItemSelectOptions`
- `type SalesOrderExpandOptions`
- `type SalesOrderItemExpandOptions`
- `type SalesOrderItemOrderByOptions`
- `type SalesOrderItemPartnerExpandOptions`
- `type SalesOrderItemPartnerOrderByOptions`
- `type SalesOrderItemPartnerSelectOptions`
- `type SalesOrderItemPricingElementExpandOptions`
- `type SalesOrderItemPricingElementOrderByOptions`
- `type SalesOrderItemPricingElementSelectOptions`
- `type SalesOrderItemSelectOptions`
- `type SalesOrderItemTextExpandOptions`
- `type SalesOrderItemTextOrderByOptions`
- `type SalesOrderItemTextSelectOptions`
- `type SalesOrderOrderByOptions`
- `type SalesOrderPartnerExpandOptions`
- `type SalesOrderPartnerOrderByOptions`
- `type SalesOrderPartnerSelectOptions`
- `type SalesOrderPricingElementExpandOptions`
- `type SalesOrderPricingElementOrderByOptions`
- `type SalesOrderPricingElementSelectOptions`
- `type SalesOrderScheduleLineExpandOptions`
- `type SalesOrderScheduleLineOrderByOptions`
- `type SalesOrderScheduleLineSelectOptions`
- `type SalesOrderSelectOptions`
- `type SalesOrderTextExpandOptions`
- `type SalesOrderTextOrderByOptions`
- `type SalesOrderTextSelectOptions`
- `type ScheduleLineOfSalesOrderItemExpandOptions`
- `type ScheduleLineOfSalesOrderItemOrderByOptions`
- `type ScheduleLineOfSalesOrderItemSelectOptions`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 117–126 | 117–130 | Types | +4 | −0 |
| 2 | 141–184 | 145–205 | Types | +17 | −0 |
| 3 | 190–263 | 211–324 | Types | +40 | −0 |
| 4 | 269–277 | 330–341 | Types | +3 | −0 |
| 5 | 289–309 | 353–385 | Types | +12 | −0 |
| 6 | 312–328 | 388–411 | Types | +7 | −0 |
| 7 | 335–421 | 418–554 | Types | +50 | −0 |
| 8 | 426–432 | 559–567 | Types | +2 | −0 |
| 9 | 441–473 | 576–619 | Types | +11 | −0 |
| 10 | 475–482 | 621–631 | Types | +3 | −0 |
| 11 | 485–519 | 634–680 | Types | +12 | −0 |
| 12 | 522–536 | 683–703 | Types | +6 | −0 |
| 13 | 543–553 | 710–723 | Types | +3 | −0 |
| 14 | 558–590 | 728–773 | Types | +13 | −0 |
| 15 | 592–632 | 775–837 | Types | +22 | −0 |
| 16 | 642–648 | 847–853 | Types | +1 | −1 |
| 17 | 653–659 | 858–864 | Types | +1 | −1 |
| 18 | 664–672 | 869–877 | Types | +2 | −2 |
| 19 | 687–697 | 892–902 | Types | +3 | −3 |
| 20 | 712–722 | 917–927 | Types | +3 | −3 |
| 21 | 727–743 | 932–948 | Types | +6 | −6 |
| 22 | 758–768 | 963–973 | Types | +3 | −3 |
| 23 | 783–791 | 988–996 | Types | +2 | −2 |
| 24 | 801–806 | 1006–1012 | Types | +1 | −0 |
| 25 | 871–880 | 1077–1087 | Types | +2 | −1 |
| 26 | 907–917 | 1114–1124 | Types | +3 | −3 |
| 27 | 931–937 | 1138–1144 | Types | +1 | −1 |
| 28 | 952–960 | 1159–1167 | Types | +2 | −2 |
| 29 | 974–982 | 1181–1189 | Types | +2 | −2 |
| 30 | 987–995 | 1194–1202 | Types | +2 | −2 |
| 31 | 1010–1016 | 1217–1223 | Types | +1 | −1 |
| 32 | 1031–1059 | 1238–1273 | Types | +9 | −2 |
| 33 | 1072–1094 | 1286–1321 | Types | +13 | −0 |
| 34 | 1099–1141 | 1326–1394 | Types | +26 | −0 |
| 35 | 1147–1183 | 1400–1450 | Types | +14 | −0 |
| 36 | 1185–1225 | 1452–1514 | Types | +22 | −0 |
| 37 | 1231–1236 | 1520–1526 | Types | +1 | −0 |
| 38 | 1246–1268 | 1536–1565 | Types | +7 | −0 |
| 39 | 1271–1277 | 1568–1576 | Types | +2 | −0 |
| 40 | 1282–1287 | 1581–1587 | Types | +1 | −0 |
| 41 | 1290–1295 | 1590–1596 | Types | +1 | −0 |
| 42 | 1297–1302 | 1598–1604 | Types | +1 | −0 |
| 43 | 1311–1317 | 1613–1621 | Types | +2 | −0 |
| 44 | 1333–1339 | 1637–1643 | Types | +1 | −1 |
| 45 | 1359–1365 | 1663–1669 | Types | +1 | −1 |
| 46 | 1370–1376 | 1674–1680 | Types | +1 | −1 |
| 47 | 1452–1458 | 1756–1762 | Types | +1 | −1 |
| 48 | 1473–1479 | 1777–1783 | Types | +1 | −1 |
| 49 | 1494–1500 | 1798–1804 | Types | +1 | −1 |
| 50 | 1537–1543 | 1841–1847 | Types | +1 | −1 |
| 51 | 1558–1566 | 1862–1870 | Types | +2 | −2 |
| 52 | 1571–1579 | 1875–1883 | Types | +2 | −2 |
| 53 | 1586–1605 | 1890–1920 | Types | +11 | −0 |
| 54 | 1610–1652 | 1925–1993 | Types | +26 | −0 |
| 55 | 1660–1682 | 2001–2027 | Types | +5 | −1 |
| 56 | 1760–1776 | 2105–2125 | Types | +4 | −0 |
| 57 | 1882–2036 | 2231–2385 | Client | +38 | −38 |

---

## Unified diff

`````diff
--- sap.s4hana.ce_salesorder_0001/old/ballerinax_sap.s4hana.ce_salesorder_0001.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.ce_salesorder_0001/new/ballerinax_sap.s4hana.ce_salesorder_0001.bal.txt	2026-08-12 13:19:19
@@ -117,10 +117,14 @@
 
 
 type SalesOrderItemText record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string LongText?;
     SAP__Message[] SAP__Messages?;
@@ -141,44 +145,61 @@
 
 
 type SalesOrderItem record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
     # Sales Document Item Category
+    @constraint:String {maxLength: 4}
     string SalesOrderItemCategory?;
     # Short Text for Sales Order Item
+    @constraint:String {maxLength: 40}
     string SalesOrderItemText?;
     # Product Number
+    @constraint:String {maxLength: 18}
     string Product?;
+    @constraint:String {maxLength: 9}
     string ProductGroup?;
     # Material Number Used by Customer
+    @constraint:String {maxLength: 35}
     string MaterialByCustomer?;
     # International Article Number (EAN/UPC)
+    @constraint:String {maxLength: 18}
     string InternationalArticleNumber?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     # Cumulative Confirmed Quantity in Sales Unit
     decimal|string ConfdDelivQtyInOrderQtyUnit?;
+    @constraint:String {maxLength: 3}
     string OrderQuantitySAPUnit?;
     # ISO Unit Code for Order Quantity
+    @constraint:String {maxLength: 3}
     string OrderQuantityISOUnit?;
     decimal|string RequestedQuantity?;
     # Unit of the Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantitySAPUnit?;
     # ISO Unit Code for Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantityISOUnit?;
     # Gross Weight of the Item
     decimal|string ItemGrossWeight?;
     # Net Weight of the Item
     decimal|string ItemNetWeight?;
+    @constraint:String {maxLength: 3}
     string ItemWeightSAPUnit?;
     # ISO Unit Code for Item Weight
+    @constraint:String {maxLength: 3}
     string ItemWeightISOUnit?;
     # Volume of the item
     decimal|string ItemVolume?;
+    @constraint:String {maxLength: 3}
     string ItemVolumeSAPUnit?;
     # ISO Unit Code for Item Volume
+    @constraint:String {maxLength: 3}
     string ItemVolumeISOUnit?;
     string? RequestedDeliveryDate?;
     string? ConfirmedDeliveryDate?;
@@ -190,74 +211,114 @@
     # Net Value of the Document Item in Document Currency
     decimal|string NetAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     # Tax Amount in Document Currency
     decimal|string TaxAmount?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
     # Batch Number
+    @constraint:String {maxLength: 10}
     string Batch?;
     # Plant (Own or External)
+    @constraint:String {maxLength: 4}
     string Plant?;
+    @constraint:String {maxLength: 4}
     string StorageLocation?;
     # Shipping Point / Receiving Point
+    @constraint:String {maxLength: 4}
     string ShippingPoint?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 6}
     string Route?;
+    @constraint:String {maxLength: 2}
     string DeliveryPriority?;
     # Partial Delivery at Item Level
+    @constraint:String {maxLength: 1}
     string PartialDeliveryIsAllowed?;
     # Number of Allowed Partial Deliveries
     decimal|string MaxNmbrOfPartialDelivery?;
     # Delivery Date Rule
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Delivery Group (Items are delivered together)
+    @constraint:String {maxLength: 3}
     string DeliveryGroup?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string MaterialPricingGroup?;
+    @constraint:String {maxLength: 4}
     string BusinessArea?;
+    @constraint:String {maxLength: 10}
     string ProfitCenter?;
     # Account Assignment Group for Material
+    @constraint:String {maxLength: 2}
     string MatlAccountAssignmentGroup?;
     # Billing Block for Item
+    @constraint:String {maxLength: 2}
     string ItemBillingBlockReason?;
     # Reason for Rejection of Sales Documents
+    @constraint:String {maxLength: 2}
     string SalesDocumentRjcnReason?;
+    @constraint:String {maxLength: 18}
     string ProductConfiguration?;
     # Overall Processing Status (Item)
+    @constraint:String {maxLength: 1}
     string SDProcessStatus?;
     # Rejection Status (Item)
+    @constraint:String {maxLength: 1}
     string SDDocumentRejectionStatus?;
     # Delivery Status (Item)
+    @constraint:String {maxLength: 1}
     string DeliveryStatus?;
     # Billing Block Status (Item)
+    @constraint:String {maxLength: 1}
     string BillingBlockStatus?;
     # Incompletion Status (Item)
+    @constraint:String {maxLength: 1}
     string ItemGeneralIncompletionStatus?;
     # Delivery Block Status (Item)
+    @constraint:String {maxLength: 1}
     string DeliveryBlockStatus?;
+    @constraint:String {maxLength: 1}
     string SlsOrderItemDownPaymentStatus?;
     # Order-Related Billing Status (Item)
+    @constraint:String {maxLength: 1}
     string OrderRelatedBillingStatus?;
     # Product Marketability Status (Item)
+    @constraint:String {maxLength: 1}
     string ChmlCmplncStatus?;
     # Dangerous Goods Status (Item)
+    @constraint:String {maxLength: 1}
     string DangerousGoodsStatus?;
     # Safety Data Sheet Status (Item)
+    @constraint:String {maxLength: 1}
     string SafetyDataSheetStatus?;
     # Embargo Status (Item)
+    @constraint:String {maxLength: 1}
     string TrdCmplncEmbargoSts?;
     # Screening Status (Item)
+    @constraint:String {maxLength: 1}
     string TrdCmplncSnctndListChkSts?;
     # Legal Control Status (All Schedule Lines)
+    @constraint:String {maxLength: 1}
     string OvrlTrdCmplncLegalCtrlChkSts?;
     SAP__Message[] SAP__Messages?;
     SalesOrderItemPartner[] _ItemPartner?;
@@ -269,9 +330,12 @@
 
 
 type SalesOrderItemPartner record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -289,21 +353,33 @@
 
 
 type SalesOrder record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Language key for sales document type
+    @constraint:String {maxLength: 4}
     string SalesOrderType?;
     # SD document indicator
+    @constraint:String {maxLength: 1}
     string SalesOrderProcessingType?;
+    @constraint:String {maxLength: 10}
     string SoldToParty?;
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
+    @constraint:String {maxLength: 2}
     string DistributionChannel?;
     # Reference distrib.channel for cust.and material masters
+    @constraint:String {maxLength: 2}
     string ReferenceDistributionChannel?;
+    @constraint:String {maxLength: 2}
     string OrganizationDivision?;
+    @constraint:String {maxLength: 4}
     string SalesOffice?;
+    @constraint:String {maxLength: 3}
     string SalesGroup?;
+    @constraint:String {maxLength: 6}
     string SalesDistrict?;
     # Name of Person Responsible for Creating the Object
+    @constraint:String {maxLength: 12}
     string CreatedByUser?;
     # Record Creation Date
     string? CreationDate?;
@@ -312,17 +388,24 @@
     # Last Changed Date Time
     string? LastChangeDateTime?;
     # User Who Last Changed the Business Document
+    @constraint:String {maxLength: 12}
     string LastChangedByUser?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     # Ship-to Party's Customer Reference
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByShipToParty?;
     # Customer Purchase Order Type
+    @constraint:String {maxLength: 4}
     string CustomerPurchaseOrderType?;
     string? CustomerPurchaseOrderDate?;
+    @constraint:String {maxLength: 10}
     string BusinessSolutionOrder?;
     # Document Number of Reference Document
+    @constraint:String {maxLength: 10}
     string ReferenceSDDocument?;
     # Order Reason (Reason for the Business Transaction)
+    @constraint:String {maxLength: 3}
     string SDDocumentReason?;
     # Document Date (Date Received/Sent)
     string? SalesOrderDate?;
@@ -335,87 +418,137 @@
     # Net Value of the Sales Document in Document Currency
     decimal|string TotalNetAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 2}
     string ShippingCondition?;
     # Complete Delivery Defined for Each Sales Order
     boolean CompleteDeliveryIsDefined?;
     boolean SlsDocIsRlvtForProofOfDeliv?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
     # Pricing Procedure in Pricing
+    @constraint:String {maxLength: 6}
     string SDPricingProcedure?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string PriceListType?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 3}
     string TaxDepartureCountry?;
+    @constraint:String {maxLength: 3}
     string VATRegistrationCountry?;
     # Indicator: Triangular Deal Within the EU
     boolean IsEUTriangularDeal?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
+    @constraint:String {maxLength: 1}
     string PaymentMethod?;
     # Company Code to Be Billed
+    @constraint:String {maxLength: 4}
     string BillingCompanyCode?;
+    @constraint:String {maxLength: 4}
     string ControllingArea?;
+    @constraint:String {maxLength: 2}
     string CustomerAccountAssignmentGroup?;
     # Assignment Number
+    @constraint:String {maxLength: 18}
     string AssignmentReference?;
     # Reference Document Number
+    @constraint:String {maxLength: 16}
     string AccountingDocExternalReference?;
     # Customer's Account Number with Credit Limit Reference
+    @constraint:String {maxLength: 10}
     string CustomerCreditAccount?;
     # Billing Block in SD Document
+    @constraint:String {maxLength: 2}
     string HeaderBillingBlockReason?;
     # Delivery Block (Document Header)
+    @constraint:String {maxLength: 2}
     string DeliveryBlockReason?;
     # Approval Request Reason ID
+    @constraint:String {maxLength: 4}
     string SalesOrderApprovalReason?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup1?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup2?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup3?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup4?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup5?;
     # Overall Processing Status (Header/All Items)
+    @constraint:String {maxLength: 1}
     string OverallSDProcessStatus?;
     # Delivery Block Status (Item)
+    @constraint:String {maxLength: 1}
     string OverallDeliveryBlockStatus?;
     # Billing Block Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallBillingBlockStatus?;
     # Delivery Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallDeliveryStatus?;
     # Overall Status of Credit Checks
+    @constraint:String {maxLength: 1}
     string TotalCreditCheckStatus?;
     # Rejection Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallSDDocumentRejectionSts?;
     # Overall Block Status (Header)
+    @constraint:String {maxLength: 1}
     string TotalBlockStatus?;
+    @constraint:String {maxLength: 1}
     string HdrGeneralIncompletionStatus?;
     # Incompletion Status (All Items)
+    @constraint:String {maxLength: 1}
     string OvrlItmGeneralIncompletionSts?;
     # Reference Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallSDDocReferenceStatus?;
     # Document Approval Status
+    @constraint:String {maxLength: 1}
     string SalesDocApprovalStatus?;
     # Product Marketability Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallChmlCmplncStatus?;
     # Dangerous Goods Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallDangerousGoodsStatus?;
     # Safety Data Sheet Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallSafetyDataSheetStatus?;
     # Embargo Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallTrdCmplncEmbargoSts?;
     # Screening Status (All Items)
+    @constraint:String {maxLength: 1}
     string OvrlTrdCmplncSnctndListChkSts?;
+    @constraint:String {maxLength: 1}
     string OvrlTrdCmplncLegalCtrlChkSts?;
+    @constraint:String {maxLength: 1}
     string SalesOrderDownPaymentStatus?;
     # Order-Related Billing Status (All Items)
+    @constraint:String {maxLength: 1}
     string OverallOrdReltdBillgStatus?;
     SAP__Message[] SAP__Messages?;
     SalesOrderItem[] _Item?;
@@ -426,7 +559,9 @@
 
 
 type SalesOrderPartner record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -441,33 +576,44 @@
 
 
 type SalesOrderPricingElement record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
+    @constraint:String {maxLength: 4}
     string ConditionType?;
     # Calculation Type for Condition
+    @constraint:String {maxLength: 3}
     string ConditionCalculationType?;
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Quantity of the Condition Basis
     decimal|string? ConditionBaseQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     # Unit of Measurement
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioSAPUnit?;
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioISOUnit?;
     decimal|string? ConditionAmount?;
     # Amount of the Condition Basis
     decimal|string? ConditionBaseAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     SAP__Message[] SAP__Messages?;
     SalesOrder _SalesOrder?;
@@ -475,8 +621,11 @@
 
 
 type SalesOrderText record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string LongText?;
     SAP__Message[] SAP__Messages?;
@@ -485,35 +634,47 @@
 
 
 type SalesOrderItemPricingElmnt record {
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
+    @constraint:String {maxLength: 4}
     string ConditionType?;
     # Calculation Type for Condition
+    @constraint:String {maxLength: 3}
     string ConditionCalculationType?;
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Quantity of the Condition Basis
     decimal|string? ConditionBaseQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     # Unit of Measurement
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioSAPUnit?;
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioISOUnit?;
     decimal|string? ConditionAmount?;
     # Amount of the Condition Basis
     decimal|string? ConditionBaseAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     SAP__Message[] SAP__Messages?;
     SalesOrderItem _Item?;
@@ -522,15 +683,21 @@
 
 
 type SalesOrderScheduleLine record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 4}
     string ScheduleLine?;
     # Schedule Line Category
+    @constraint:String {maxLength: 2}
     string ScheduleLineCategory?;
     # Order Quantity in Sales Units
     decimal|string? ScheduleLineOrderQuantity?;
+    @constraint:String {maxLength: 3}
     string OrderQuantitySAPUnit?;
     # ISO Unit Code for Order Quantity
+    @constraint:String {maxLength: 3}
     string OrderQuantityISOUnit?;
     # Requested Delivery Date
     string? RequestedDeliveryDate?;
@@ -543,11 +710,14 @@
     # Corrected quantity in sales unit
     decimal|string CorrectedQtyInOrderQtyUnit?;
     # Schedule Line Blocked for Delivery
+    @constraint:String {maxLength: 2}
     string DelivBlockReasonForSchedLine?;
     # Purchase Requisition Number
+    @constraint:String {maxLength: 10}
     string PurchaseRequisition?;
     string? PurchaseRequisitionItem?;
     # Movement Type (Inventory Management)
+    @constraint:String {maxLength: 3}
     string GoodsMovementType?;
     SalesOrderItem _Item?;
     SalesOrder _SalesOrder?;
@@ -558,33 +728,46 @@
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
     # Sales Document Item Category
+    @constraint:String {maxLength: 4}
     string SalesOrderItemCategory?;
     # Short Text for Sales Order Item
+    @constraint:String {maxLength: 40}
     string SalesOrderItemText?;
     # Product Number
+    @constraint:String {maxLength: 18}
     string Product?;
+    @constraint:String {maxLength: 9}
     string ProductGroup?;
     # Material Number Used by Customer
+    @constraint:String {maxLength: 35}
     string MaterialByCustomer?;
     # International Article Number (EAN/UPC)
+    @constraint:String {maxLength: 18}
     string InternationalArticleNumber?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     decimal|string RequestedQuantity?;
     # Unit of the Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantitySAPUnit?;
     # ISO Unit Code for Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantityISOUnit?;
     # Gross Weight of the Item
     decimal|string ItemGrossWeight?;
     # Net Weight of the Item
     decimal|string ItemNetWeight?;
+    @constraint:String {maxLength: 3}
     string ItemWeightSAPUnit?;
     # ISO Unit Code for Item Weight
+    @constraint:String {maxLength: 3}
     string ItemWeightISOUnit?;
     # Volume of the item
     decimal|string ItemVolume?;
+    @constraint:String {maxLength: 3}
     string ItemVolumeSAPUnit?;
     # ISO Unit Code for Item Volume
+    @constraint:String {maxLength: 3}
     string ItemVolumeISOUnit?;
     string? RequestedDeliveryDate?;
     # Date for Pricing and Exchange Rate
@@ -592,41 +775,63 @@
     # Date on which services are rendered
     string? ServicesRenderedDate?;
     string? BillingDocumentDate?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
     # Batch Number
+    @constraint:String {maxLength: 10}
     string Batch?;
     # Plant (Own or External)
+    @constraint:String {maxLength: 4}
     string Plant?;
+    @constraint:String {maxLength: 4}
     string StorageLocation?;
     # Shipping Point / Receiving Point
+    @constraint:String {maxLength: 4}
     string ShippingPoint?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 6}
     string Route?;
+    @constraint:String {maxLength: 2}
     string DeliveryPriority?;
     # Partial Delivery at Item Level
+    @constraint:String {maxLength: 1}
     string PartialDeliveryIsAllowed?;
     # Number of Allowed Partial Deliveries
     decimal|string MaxNmbrOfPartialDelivery?;
     # Delivery Date Rule
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Delivery Group (Items are delivered together)
+    @constraint:String {maxLength: 3}
     string DeliveryGroup?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string MaterialPricingGroup?;
+    @constraint:String {maxLength: 10}
     string ProfitCenter?;
     # Account Assignment Group for Material
+    @constraint:String {maxLength: 2}
     string MatlAccountAssignmentGroup?;
     # Billing Block for Item
+    @constraint:String {maxLength: 2}
     string ItemBillingBlockReason?;
     # Reason for Rejection of Sales Documents
+    @constraint:String {maxLength: 2}
     string SalesDocumentRjcnReason?;
     UpdateSAP__Message[] SAP__Messages?;
 };
@@ -642,7 +847,7 @@
     string? longtextUrl?;
 };
 
-// Unknown type: ItemOfSalesOrderScheduleLineExpandOptions
+type ItemOfSalesOrderScheduleLineExpandOptions ("*"|"_ItemPartner"|"_ItemPricingElement"|"_ItemText"|"_SalesOrder"|"_ScheduleLine")[];
 
 
 type CollectionOfSalesOrderPricingElement record {
@@ -653,7 +858,7 @@
 # The number of entities in the collection. Available when using the [$count](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount) query option.
 type count decimal|string;
 
-// Unknown type: ItemPricingElementOfSalesOrderItemSelectOptions
+type ItemPricingElementOfSalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"ConditionCalculationType"|"ConditionRateAmount"|"ConditionCurrency"|"ConditionQuantity"|"ConditionBaseQuantity"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionRateRatio"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioISOUnit"|"ConditionAmount"|"ConditionBaseAmount"|"TransactionCurrency"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getSalesOrderPricingElement
 
@@ -664,9 +869,9 @@
     SalesOrderPricingElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderPricingElementExpandOptions
+type SalesOrderPricingElementExpandOptions ("*"|"_SalesOrder")[];
 
-// Unknown type: SalesOrderPricingElementSelectOptions
+type SalesOrderPricingElementSelectOptions ("SalesOrder"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"ConditionCalculationType"|"ConditionRateAmount"|"ConditionCurrency"|"ConditionQuantity"|"ConditionBaseQuantity"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionRateRatio"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioISOUnit"|"ConditionAmount"|"ConditionBaseAmount"|"TransactionCurrency"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: listSalesOrders
 
@@ -687,11 +892,11 @@
     SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOrderByOptions
+type SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderType"|"SalesOrderType desc"|"SalesOrderProcessingType"|"SalesOrderProcessingType desc"|"SoldToParty"|"SoldToParty desc"|"SalesOrganization"|"SalesOrganization desc"|"DistributionChannel"|"DistributionChannel desc"|"ReferenceDistributionChannel"|"ReferenceDistributionChannel desc"|"OrganizationDivision"|"OrganizationDivision desc"|"SalesOffice"|"SalesOffice desc"|"SalesGroup"|"SalesGroup desc"|"SalesDistrict"|"SalesDistrict desc"|"CreatedByUser"|"CreatedByUser desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDateTime"|"LastChangeDateTime desc"|"LastChangedByUser"|"LastChangedByUser desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"PurchaseOrderByShipToParty"|"PurchaseOrderByShipToParty desc"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderType desc"|"CustomerPurchaseOrderDate"|"CustomerPurchaseOrderDate desc"|"BusinessSolutionOrder"|"BusinessSolutionOrder desc"|"ReferenceSDDocument"|"ReferenceSDDocument desc"|"SDDocumentReason"|"SDDocumentReason desc"|"SalesOrderDate"|"SalesOrderDate desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"PricingDate"|"PricingDate desc"|"ServicesRenderedDate"|"ServicesRenderedDate desc"|"BillingDocumentDate"|"BillingDocumentDate desc"|"TotalNetAmount"|"TotalNetAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"DeliveryDateTypeRule"|"DeliveryDateTypeRule desc"|"ShippingCondition"|"ShippingCondition desc"|"CompleteDeliveryIsDefined"|"CompleteDeliveryIsDefined desc"|"SlsDocIsRlvtForProofOfDeliv"|"SlsDocIsRlvtForProofOfDeliv desc"|"ShippingType"|"ShippingType desc"|"ReceivingPoint"|"ReceivingPoint desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsVersion"|"IncotermsVersion desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"SDPricingProcedure"|"SDPricingProcedure desc"|"CustomerPriceGroup"|"CustomerPriceGroup desc"|"PriceListType"|"PriceListType desc"|"FixedValueDate"|"FixedValueDate desc"|"TaxDepartureCountry"|"TaxDepartureCountry desc"|"VATRegistrationCountry"|"VATRegistrationCountry desc"|"IsEUTriangularDeal"|"IsEUTriangularDeal desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"PaymentMethod"|"PaymentMethod desc"|"BillingCompanyCode"|"BillingCompanyCode desc"|"ControllingArea"|"ControllingArea desc"|"CustomerAccountAssignmentGroup"|"CustomerAccountAssignmentGroup desc"|"AssignmentReference"|"AssignmentReference desc"|"AccountingDocExternalReference"|"AccountingDocExternalReference desc"|"CustomerCreditAccount"|"CustomerCreditAccount desc"|"HeaderBillingBlockReason"|"HeaderBillingBlockReason desc"|"DeliveryBlockReason"|"DeliveryBlockReason desc"|"SalesOrderApprovalReason"|"SalesOrderApprovalReason desc"|"CustomerGroup"|"CustomerGroup desc"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup1 desc"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup2 desc"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup3 desc"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup4 desc"|"AdditionalCustomerGroup5"|"AdditionalCustomerGroup5 desc"|"OverallSDProcessStatus"|"OverallSDProcessStatus desc"|"OverallDeliveryBlockStatus"|"OverallDeliveryBlockStatus desc"|"OverallBillingBlockStatus"|"OverallBillingBlockStatus desc"|"OverallDeliveryStatus"|"OverallDeliveryStatus desc"|"TotalCreditCheckStatus"|"TotalCreditCheckStatus desc"|"OverallSDDocumentRejectionSts"|"OverallSDDocumentRejectionSts desc"|"TotalBlockStatus"|"TotalBlockStatus desc"|"HdrGeneralIncompletionStatus"|"HdrGeneralIncompletionStatus desc"|"OvrlItmGeneralIncompletionSts"|"OvrlItmGeneralIncompletionSts desc"|"OverallSDDocReferenceStatus"|"OverallSDDocReferenceStatus desc"|"SalesDocApprovalStatus"|"SalesDocApprovalStatus desc"|"OverallChmlCmplncStatus"|"OverallChmlCmplncStatus desc"|"OverallDangerousGoodsStatus"|"OverallDangerousGoodsStatus desc"|"OverallSafetyDataSheetStatus"|"OverallSafetyDataSheetStatus desc"|"OverallTrdCmplncEmbargoSts"|"OverallTrdCmplncEmbargoSts desc"|"OvrlTrdCmplncSnctndListChkSts"|"OvrlTrdCmplncSnctndListChkSts desc"|"OvrlTrdCmplncLegalCtrlChkSts"|"OvrlTrdCmplncLegalCtrlChkSts desc"|"SalesOrderDownPaymentStatus"|"SalesOrderDownPaymentStatus desc"|"OverallOrdReltdBillgStatus"|"OverallOrdReltdBillgStatus desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: SalesOrderExpandOptions
+type SalesOrderExpandOptions ("*"|"_Item"|"_Partner"|"_PricingElement"|"_Text")[];
 
-// Unknown type: SalesOrderSelectOptions
+type SalesOrderSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderProcessingType"|"SoldToParty"|"SalesOrganization"|"DistributionChannel"|"ReferenceDistributionChannel"|"OrganizationDivision"|"SalesOffice"|"SalesGroup"|"SalesDistrict"|"CreatedByUser"|"CreationDate"|"CreationTime"|"LastChangeDateTime"|"LastChangedByUser"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"BusinessSolutionOrder"|"ReferenceSDDocument"|"SDDocumentReason"|"SalesOrderDate"|"RequestedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"TotalNetAmount"|"TransactionCurrency"|"DeliveryDateTypeRule"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"SlsDocIsRlvtForProofOfDeliv"|"ShippingType"|"ReceivingPoint"|"IncotermsClassification"|"IncotermsVersion"|"IncotermsLocation1"|"IncotermsLocation2"|"SDPricingProcedure"|"CustomerPriceGroup"|"PriceListType"|"FixedValueDate"|"TaxDepartureCountry"|"VATRegistrationCountry"|"IsEUTriangularDeal"|"CustomerPaymentTerms"|"PaymentMethod"|"BillingCompanyCode"|"ControllingArea"|"CustomerAccountAssignmentGroup"|"AssignmentReference"|"AccountingDocExternalReference"|"CustomerCreditAccount"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"SalesOrderApprovalReason"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"OverallSDProcessStatus"|"OverallDeliveryBlockStatus"|"OverallBillingBlockStatus"|"OverallDeliveryStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"TotalBlockStatus"|"HdrGeneralIncompletionStatus"|"OvrlItmGeneralIncompletionSts"|"OverallSDDocReferenceStatus"|"SalesDocApprovalStatus"|"OverallChmlCmplncStatus"|"OverallDangerousGoodsStatus"|"OverallSafetyDataSheetStatus"|"OverallTrdCmplncEmbargoSts"|"OvrlTrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SalesOrderDownPaymentStatus"|"OverallOrdReltdBillgStatus"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: listTextsOfSalesOrder
 
@@ -712,11 +917,11 @@
     SalesOrderTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderTextOrderByOptions
+type SalesOrderTextOrderByOptions ("SalesOrder"|"SalesOrder desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: SalesOrderTextExpandOptions
+type SalesOrderTextExpandOptions ("*"|"_SalesOrder")[];
 
-// Unknown type: SalesOrderTextSelectOptions
+type SalesOrderTextSelectOptions ("SalesOrder"|"Language"|"LongTextID"|"LongText"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getItemOfSalesOrderScheduleLine
 
@@ -727,17 +932,17 @@
     ItemOfSalesOrderScheduleLineSelectOptions \$select?;
 };
 
-// Unknown type: ItemOfSalesOrderScheduleLineSelectOptions
+type ItemOfSalesOrderScheduleLineSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"SalesOrderItemCategory"|"SalesOrderItemText"|"Product"|"ProductGroup"|"MaterialByCustomer"|"InternationalArticleNumber"|"PurchaseOrderByCustomer"|"ConfdDelivQtyInOrderQtyUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedQuantity"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"NetAmount"|"TransactionCurrency"|"TaxAmount"|"CustomerGroup"|"Batch"|"Plant"|"StorageLocation"|"ShippingPoint"|"ShippingType"|"Route"|"DeliveryPriority"|"PartialDeliveryIsAllowed"|"MaxNmbrOfPartialDelivery"|"DeliveryDateTypeRule"|"ReceivingPoint"|"DeliveryGroup"|"IncotermsClassification"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerPriceGroup"|"MaterialPricingGroup"|"BusinessArea"|"ProfitCenter"|"MatlAccountAssignmentGroup"|"ItemBillingBlockReason"|"SalesDocumentRjcnReason"|"ProductConfiguration"|"SDProcessStatus"|"SDDocumentRejectionStatus"|"DeliveryStatus"|"BillingBlockStatus"|"ItemGeneralIncompletionStatus"|"DeliveryBlockStatus"|"SlsOrderItemDownPaymentStatus"|"OrderRelatedBillingStatus"|"ChmlCmplncStatus"|"DangerousGoodsStatus"|"SafetyDataSheetStatus"|"TrdCmplncEmbargoSts"|"TrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SAP__Messages")[];
 
-// Unknown type: SalesOrderPartnerExpandOptions
+type SalesOrderPartnerExpandOptions ("*"|"_SalesOrder")[];
 
-// Unknown type: ItemOfSalesOrderItemPricingElementExpandOptions
+type ItemOfSalesOrderItemPricingElementExpandOptions ("*"|"_ItemPartner"|"_ItemPricingElement"|"_ItemText"|"_SalesOrder"|"_ScheduleLine")[];
 
-// Unknown type: SalesOrderItemTextOrderByOptions
+type SalesOrderItemTextOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: SalesOrderPricingElementOrderByOptions
+type SalesOrderPricingElementOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionRateAmount"|"ConditionRateAmount desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionBaseQuantity"|"ConditionBaseQuantity desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionRateRatio"|"ConditionRateRatio desc"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioSAPUnit desc"|"ConditionRateRatioISOUnit"|"ConditionRateRatioISOUnit desc"|"ConditionAmount"|"ConditionAmount desc"|"ConditionBaseAmount"|"ConditionBaseAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: ItemOfSalesOrderItemPartnerSelectOptions
+type ItemOfSalesOrderItemPartnerSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"SalesOrderItemCategory"|"SalesOrderItemText"|"Product"|"ProductGroup"|"MaterialByCustomer"|"InternationalArticleNumber"|"PurchaseOrderByCustomer"|"ConfdDelivQtyInOrderQtyUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedQuantity"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"NetAmount"|"TransactionCurrency"|"TaxAmount"|"CustomerGroup"|"Batch"|"Plant"|"StorageLocation"|"ShippingPoint"|"ShippingType"|"Route"|"DeliveryPriority"|"PartialDeliveryIsAllowed"|"MaxNmbrOfPartialDelivery"|"DeliveryDateTypeRule"|"ReceivingPoint"|"DeliveryGroup"|"IncotermsClassification"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerPriceGroup"|"MaterialPricingGroup"|"BusinessArea"|"ProfitCenter"|"MatlAccountAssignmentGroup"|"ItemBillingBlockReason"|"SalesDocumentRjcnReason"|"ProductConfiguration"|"SDProcessStatus"|"SDDocumentRejectionStatus"|"DeliveryStatus"|"BillingBlockStatus"|"ItemGeneralIncompletionStatus"|"DeliveryBlockStatus"|"SlsOrderItemDownPaymentStatus"|"OrderRelatedBillingStatus"|"ChmlCmplncStatus"|"DangerousGoodsStatus"|"SafetyDataSheetStatus"|"TrdCmplncEmbargoSts"|"TrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: listSalesOrderScheduleLines
 
@@ -758,11 +963,11 @@
     SalesOrderScheduleLineSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderScheduleLineOrderByOptions
+type SalesOrderScheduleLineOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"ScheduleLine"|"ScheduleLine desc"|"ScheduleLineCategory"|"ScheduleLineCategory desc"|"ScheduleLineOrderQuantity"|"ScheduleLineOrderQuantity desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ConfirmedDeliveryDate"|"ConfirmedDeliveryDate desc"|"ConfdOrderQtyByMatlAvailCheck"|"ConfdOrderQtyByMatlAvailCheck desc"|"DeliveredQtyInOrderQtyUnit"|"DeliveredQtyInOrderQtyUnit desc"|"OpenConfdDelivQtyInOrdQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit desc"|"CorrectedQtyInOrderQtyUnit"|"CorrectedQtyInOrderQtyUnit desc"|"DelivBlockReasonForSchedLine"|"DelivBlockReasonForSchedLine desc"|"PurchaseRequisition"|"PurchaseRequisition desc"|"PurchaseRequisitionItem"|"PurchaseRequisitionItem desc"|"GoodsMovementType"|"GoodsMovementType desc")[];
 
-// Unknown type: SalesOrderScheduleLineExpandOptions
+type SalesOrderScheduleLineExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
-// Unknown type: SalesOrderScheduleLineSelectOptions
+type SalesOrderScheduleLineSelectOptions ("SalesOrder"|"SalesOrderItem"|"ScheduleLine"|"ScheduleLineCategory"|"ScheduleLineOrderQuantity"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"ConfdOrderQtyByMatlAvailCheck"|"DeliveredQtyInOrderQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit"|"CorrectedQtyInOrderQtyUnit"|"DelivBlockReasonForSchedLine"|"PurchaseRequisition"|"PurchaseRequisitionItem"|"GoodsMovementType")[];
 
 # Represents the Queries record for the operation: listSalesOrderItemTexts
 
@@ -783,9 +988,9 @@
     SalesOrderItemTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemTextExpandOptions
+type SalesOrderItemTextExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
-// Unknown type: SalesOrderItemTextSelectOptions
+type SalesOrderItemTextSelectOptions ("SalesOrder"|"SalesOrderItem"|"Language"|"LongTextID"|"LongText"|"SAP__Messages")[];
 
 
 type UpdateSalesOrderItemPartner record {
@@ -801,6 +1006,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -871,10 +1077,11 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
-// Unknown type: ScheduleLineOfSalesOrderItemSelectOptions
+type ScheduleLineOfSalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"ScheduleLine"|"ScheduleLineCategory"|"ScheduleLineOrderQuantity"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"ConfdOrderQtyByMatlAvailCheck"|"DeliveredQtyInOrderQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit"|"CorrectedQtyInOrderQtyUnit"|"DelivBlockReasonForSchedLine"|"PurchaseRequisition"|"PurchaseRequisitionItem"|"GoodsMovementType")[];
 
 
 type CollectionOfSalesOrder record {
@@ -907,11 +1114,11 @@
     ItemTextOfSalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: ItemTextOfSalesOrderItemOrderByOptions
+type ItemTextOfSalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: ItemTextOfSalesOrderItemExpandOptions
+type ItemTextOfSalesOrderItemExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
-// Unknown type: ItemTextOfSalesOrderItemSelectOptions
+type ItemTextOfSalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"Language"|"LongTextID"|"LongText"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfSalesOrderItemPartner
 
@@ -931,7 +1138,7 @@
     ItemOfSalesOrderItemPricingElementSelectOptions \$select?;
 };
 
-// Unknown type: ItemOfSalesOrderItemPricingElementSelectOptions
+type ItemOfSalesOrderItemPricingElementSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"SalesOrderItemCategory"|"SalesOrderItemText"|"Product"|"ProductGroup"|"MaterialByCustomer"|"InternationalArticleNumber"|"PurchaseOrderByCustomer"|"ConfdDelivQtyInOrderQtyUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedQuantity"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"NetAmount"|"TransactionCurrency"|"TaxAmount"|"CustomerGroup"|"Batch"|"Plant"|"StorageLocation"|"ShippingPoint"|"ShippingType"|"Route"|"DeliveryPriority"|"PartialDeliveryIsAllowed"|"MaxNmbrOfPartialDelivery"|"DeliveryDateTypeRule"|"ReceivingPoint"|"DeliveryGroup"|"IncotermsClassification"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerPriceGroup"|"MaterialPricingGroup"|"BusinessArea"|"ProfitCenter"|"MatlAccountAssignmentGroup"|"ItemBillingBlockReason"|"SalesDocumentRjcnReason"|"ProductConfiguration"|"SDProcessStatus"|"SDDocumentRejectionStatus"|"DeliveryStatus"|"BillingBlockStatus"|"ItemGeneralIncompletionStatus"|"DeliveryBlockStatus"|"SlsOrderItemDownPaymentStatus"|"OrderRelatedBillingStatus"|"ChmlCmplncStatus"|"DangerousGoodsStatus"|"SafetyDataSheetStatus"|"TrdCmplncEmbargoSts"|"TrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: listPartnersOfSalesOrder
 
@@ -952,9 +1159,9 @@
     SalesOrderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderPartnerOrderByOptions
+type SalesOrderPartnerOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PartnerFunction"|"PartnerFunction desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
-// Unknown type: SalesOrderPartnerSelectOptions
+type SalesOrderPartnerSelectOptions ("SalesOrder"|"PartnerFunction"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getSalesOrderText
 
@@ -974,9 +1181,9 @@
     SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemExpandOptions
+type SalesOrderItemExpandOptions ("*"|"_ItemPartner"|"_ItemPricingElement"|"_ItemText"|"_SalesOrder"|"_ScheduleLine")[];
 
-// Unknown type: SalesOrderItemSelectOptions
+type SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"SalesOrderItemCategory"|"SalesOrderItemText"|"Product"|"ProductGroup"|"MaterialByCustomer"|"InternationalArticleNumber"|"PurchaseOrderByCustomer"|"ConfdDelivQtyInOrderQtyUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedQuantity"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"NetAmount"|"TransactionCurrency"|"TaxAmount"|"CustomerGroup"|"Batch"|"Plant"|"StorageLocation"|"ShippingPoint"|"ShippingType"|"Route"|"DeliveryPriority"|"PartialDeliveryIsAllowed"|"MaxNmbrOfPartialDelivery"|"DeliveryDateTypeRule"|"ReceivingPoint"|"DeliveryGroup"|"IncotermsClassification"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerPriceGroup"|"MaterialPricingGroup"|"BusinessArea"|"ProfitCenter"|"MatlAccountAssignmentGroup"|"ItemBillingBlockReason"|"SalesDocumentRjcnReason"|"ProductConfiguration"|"SDProcessStatus"|"SDDocumentRejectionStatus"|"DeliveryStatus"|"BillingBlockStatus"|"ItemGeneralIncompletionStatus"|"DeliveryBlockStatus"|"SlsOrderItemDownPaymentStatus"|"OrderRelatedBillingStatus"|"ChmlCmplncStatus"|"DangerousGoodsStatus"|"SafetyDataSheetStatus"|"TrdCmplncEmbargoSts"|"TrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfSalesOrderScheduleLine
 
@@ -987,9 +1194,9 @@
     SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemPartnerSelectOptions
+type SalesOrderItemPartnerSelectOptions ("SalesOrder"|"SalesOrderItem"|"PartnerFunction"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"PartnerIsSpecificForSDDocItem"|"SAP__Messages")[];
 
-// Unknown type: SalesOrderItemPricingElementOrderByOptions
+type SalesOrderItemPricingElementOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionRateAmount"|"ConditionRateAmount desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionBaseQuantity"|"ConditionBaseQuantity desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionRateRatio"|"ConditionRateRatio desc"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioSAPUnit desc"|"ConditionRateRatioISOUnit"|"ConditionRateRatioISOUnit desc"|"ConditionAmount"|"ConditionAmount desc"|"ConditionBaseAmount"|"ConditionBaseAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
 # Represents the Queries record for the operation: listSalesOrderItems
 
@@ -1010,7 +1217,7 @@
     SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOrderByOptions
+type SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"HigherLevelItem"|"HigherLevelItem desc"|"SalesOrderItemCategory"|"SalesOrderItemCategory desc"|"SalesOrderItemText"|"SalesOrderItemText desc"|"Product"|"Product desc"|"ProductGroup"|"ProductGroup desc"|"MaterialByCustomer"|"MaterialByCustomer desc"|"InternationalArticleNumber"|"InternationalArticleNumber desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"ConfdDelivQtyInOrderQtyUnit"|"ConfdDelivQtyInOrderQtyUnit desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"RequestedQuantity"|"RequestedQuantity desc"|"RequestedQuantitySAPUnit"|"RequestedQuantitySAPUnit desc"|"RequestedQuantityISOUnit"|"RequestedQuantityISOUnit desc"|"ItemGrossWeight"|"ItemGrossWeight desc"|"ItemNetWeight"|"ItemNetWeight desc"|"ItemWeightSAPUnit"|"ItemWeightSAPUnit desc"|"ItemWeightISOUnit"|"ItemWeightISOUnit desc"|"ItemVolume"|"ItemVolume desc"|"ItemVolumeSAPUnit"|"ItemVolumeSAPUnit desc"|"ItemVolumeISOUnit"|"ItemVolumeISOUnit desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ConfirmedDeliveryDate"|"ConfirmedDeliveryDate desc"|"PricingDate"|"PricingDate desc"|"ServicesRenderedDate"|"ServicesRenderedDate desc"|"BillingDocumentDate"|"BillingDocumentDate desc"|"NetAmount"|"NetAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"TaxAmount"|"TaxAmount desc"|"CustomerGroup"|"CustomerGroup desc"|"Batch"|"Batch desc"|"Plant"|"Plant desc"|"StorageLocation"|"StorageLocation desc"|"ShippingPoint"|"ShippingPoint desc"|"ShippingType"|"ShippingType desc"|"Route"|"Route desc"|"DeliveryPriority"|"DeliveryPriority desc"|"PartialDeliveryIsAllowed"|"PartialDeliveryIsAllowed desc"|"MaxNmbrOfPartialDelivery"|"MaxNmbrOfPartialDelivery desc"|"DeliveryDateTypeRule"|"DeliveryDateTypeRule desc"|"ReceivingPoint"|"ReceivingPoint desc"|"DeliveryGroup"|"DeliveryGroup desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"IncotermsVersion"|"IncotermsVersion desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"FixedValueDate"|"FixedValueDate desc"|"CustomerPriceGroup"|"CustomerPriceGroup desc"|"MaterialPricingGroup"|"MaterialPricingGroup desc"|"BusinessArea"|"BusinessArea desc"|"ProfitCenter"|"ProfitCenter desc"|"MatlAccountAssignmentGroup"|"MatlAccountAssignmentGroup desc"|"ItemBillingBlockReason"|"ItemBillingBlockReason desc"|"SalesDocumentRjcnReason"|"SalesDocumentRjcnReason desc"|"ProductConfiguration"|"ProductConfiguration desc"|"SDProcessStatus"|"SDProcessStatus desc"|"SDDocumentRejectionStatus"|"SDDocumentRejectionStatus desc"|"DeliveryStatus"|"DeliveryStatus desc"|"BillingBlockStatus"|"BillingBlockStatus desc"|"ItemGeneralIncompletionStatus"|"ItemGeneralIncompletionStatus desc"|"DeliveryBlockStatus"|"DeliveryBlockStatus desc"|"SlsOrderItemDownPaymentStatus"|"SlsOrderItemDownPaymentStatus desc"|"OrderRelatedBillingStatus"|"OrderRelatedBillingStatus desc"|"ChmlCmplncStatus"|"ChmlCmplncStatus desc"|"DangerousGoodsStatus"|"DangerousGoodsStatus desc"|"SafetyDataSheetStatus"|"SafetyDataSheetStatus desc"|"TrdCmplncEmbargoSts"|"TrdCmplncEmbargoSts desc"|"TrdCmplncSnctndListChkSts"|"TrdCmplncSnctndListChkSts desc"|"OvrlTrdCmplncLegalCtrlChkSts"|"OvrlTrdCmplncLegalCtrlChkSts desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
 # Represents the Queries record for the operation: listSalesOrderPartners
 
@@ -1031,29 +1238,36 @@
     SalesOrderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: ScheduleLineOfSalesOrderItemExpandOptions
+type ScheduleLineOfSalesOrderItemExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
-// Unknown type: ItemPricingElementOfSalesOrderItemOrderByOptions
+type ItemPricingElementOfSalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionRateAmount"|"ConditionRateAmount desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionBaseQuantity"|"ConditionBaseQuantity desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionRateRatio"|"ConditionRateRatio desc"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioSAPUnit desc"|"ConditionRateRatioISOUnit"|"ConditionRateRatioISOUnit desc"|"ConditionAmount"|"ConditionAmount desc"|"ConditionBaseAmount"|"ConditionBaseAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
 
 type CreateSalesOrderPricingElement record {
+    @constraint:String {maxLength: 4}
     string ConditionType?;
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     # Unit of Measurement
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioSAPUnit?;
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioISOUnit?;
     decimal|string? ConditionAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     CreateSAP__Message[] SAP__Messages?;
     CreateSalesOrder _SalesOrder?;
@@ -1072,23 +1286,36 @@
 
 
 type CreateSalesOrder record {
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # Language key for sales document type
+    @constraint:String {maxLength: 4}
     string SalesOrderType?;
+    @constraint:String {maxLength: 10}
     string SoldToParty?;
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
+    @constraint:String {maxLength: 2}
     string DistributionChannel?;
+    @constraint:String {maxLength: 2}
     string OrganizationDivision?;
+    @constraint:String {maxLength: 4}
     string SalesOffice?;
+    @constraint:String {maxLength: 3}
     string SalesGroup?;
+    @constraint:String {maxLength: 6}
     string SalesDistrict?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     # Ship-to Party's Customer Reference
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByShipToParty?;
     # Customer Purchase Order Type
+    @constraint:String {maxLength: 4}
     string CustomerPurchaseOrderType?;
     string? CustomerPurchaseOrderDate?;
     # Order Reason (Reason for the Business Transaction)
+    @constraint:String {maxLength: 3}
     string SDDocumentReason?;
     # Document Date (Date Received/Sent)
     string? SalesOrderDate?;
@@ -1099,43 +1326,69 @@
     string? ServicesRenderedDate?;
     string? BillingDocumentDate?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 2}
     string ShippingCondition?;
     # Complete Delivery Defined for Each Sales Order
     boolean CompleteDeliveryIsDefined?;
     boolean SlsDocIsRlvtForProofOfDeliv?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string PriceListType?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 3}
     string TaxDepartureCountry?;
+    @constraint:String {maxLength: 3}
     string VATRegistrationCountry?;
     # Indicator: Triangular Deal Within the EU
     boolean IsEUTriangularDeal?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
+    @constraint:String {maxLength: 1}
     string PaymentMethod?;
+    @constraint:String {maxLength: 2}
     string CustomerAccountAssignmentGroup?;
     # Assignment Number
+    @constraint:String {maxLength: 18}
     string AssignmentReference?;
     # Reference Document Number
+    @constraint:String {maxLength: 16}
     string AccountingDocExternalReference?;
     # Billing Block in SD Document
+    @constraint:String {maxLength: 2}
     string HeaderBillingBlockReason?;
     # Delivery Block (Document Header)
+    @constraint:String {maxLength: 2}
     string DeliveryBlockReason?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup1?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup2?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup3?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup4?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup5?;
     CreateSAP__Message[] SAP__Messages?;
     CreateSalesOrderItem[] _Item?;
@@ -1147,37 +1400,51 @@
 
 type CreateSalesOrderItem record {
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
     # Sales Document Item Category
+    @constraint:String {maxLength: 4}
     string SalesOrderItemCategory?;
     # Short Text for Sales Order Item
+    @constraint:String {maxLength: 40}
     string SalesOrderItemText?;
     # Product Number
+    @constraint:String {maxLength: 18}
     string Product?;
+    @constraint:String {maxLength: 9}
     string ProductGroup?;
     # Material Number Used by Customer
+    @constraint:String {maxLength: 35}
     string MaterialByCustomer?;
     # International Article Number (EAN/UPC)
+    @constraint:String {maxLength: 18}
     string InternationalArticleNumber?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     decimal|string RequestedQuantity?;
     # Unit of the Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantitySAPUnit?;
     # ISO Unit Code for Requested Quantity
+    @constraint:String {maxLength: 3}
     string RequestedQuantityISOUnit?;
     # Gross Weight of the Item
     decimal|string ItemGrossWeight?;
     # Net Weight of the Item
     decimal|string ItemNetWeight?;
+    @constraint:String {maxLength: 3}
     string ItemWeightSAPUnit?;
     # ISO Unit Code for Item Weight
+    @constraint:String {maxLength: 3}
     string ItemWeightISOUnit?;
     # Volume of the item
     decimal|string ItemVolume?;
+    @constraint:String {maxLength: 3}
     string ItemVolumeSAPUnit?;
     # ISO Unit Code for Item Volume
+    @constraint:String {maxLength: 3}
     string ItemVolumeISOUnit?;
     string? RequestedDeliveryDate?;
     # Date for Pricing and Exchange Rate
@@ -1185,41 +1452,63 @@
     # Date on which services are rendered
     string? ServicesRenderedDate?;
     string? BillingDocumentDate?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
     # Batch Number
+    @constraint:String {maxLength: 10}
     string Batch?;
     # Plant (Own or External)
+    @constraint:String {maxLength: 4}
     string Plant?;
+    @constraint:String {maxLength: 4}
     string StorageLocation?;
     # Shipping Point / Receiving Point
+    @constraint:String {maxLength: 4}
     string ShippingPoint?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 6}
     string Route?;
+    @constraint:String {maxLength: 2}
     string DeliveryPriority?;
     # Partial Delivery at Item Level
+    @constraint:String {maxLength: 1}
     string PartialDeliveryIsAllowed?;
     # Number of Allowed Partial Deliveries
     decimal|string MaxNmbrOfPartialDelivery?;
     # Delivery Date Rule
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Delivery Group (Items are delivered together)
+    @constraint:String {maxLength: 3}
     string DeliveryGroup?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string MaterialPricingGroup?;
+    @constraint:String {maxLength: 10}
     string ProfitCenter?;
     # Account Assignment Group for Material
+    @constraint:String {maxLength: 2}
     string MatlAccountAssignmentGroup?;
     # Billing Block for Item
+    @constraint:String {maxLength: 2}
     string ItemBillingBlockReason?;
     # Reason for Rejection of Sales Documents
+    @constraint:String {maxLength: 2}
     string SalesDocumentRjcnReason?;
     CreateSAP__Message[] SAP__Messages?;
     CreateSalesOrderItemPartner[] _ItemPartner?;
@@ -1231,6 +1520,7 @@
 
 
 type CreateSalesOrderItemPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1246,23 +1536,30 @@
 
 
 type CreateSalesOrderItemPricingElmnt record {
+    @constraint:String {maxLength: 4}
     string ConditionType?;
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     # Unit of Measurement
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioSAPUnit?;
+    @constraint:String {maxLength: 3}
     string ConditionRateRatioISOUnit?;
     decimal|string? ConditionAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     CreateSAP__Message[] SAP__Messages?;
     CreateSalesOrderItem _Item?;
@@ -1271,7 +1568,9 @@
 
 
 type CreateSalesOrderItemText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string LongText?;
     CreateSAP__Message[] SAP__Messages?;
@@ -1282,6 +1581,7 @@
 
 type CreateSalesOrderScheduleLine record {
     # Schedule Line Category
+    @constraint:String {maxLength: 2}
     string ScheduleLineCategory?;
     # Order Quantity in Sales Units
     decimal|string? ScheduleLineOrderQuantity?;
@@ -1290,6 +1590,7 @@
     # Corrected quantity in sales unit
     decimal|string CorrectedQtyInOrderQtyUnit?;
     # Schedule Line Blocked for Delivery
+    @constraint:String {maxLength: 2}
     string DelivBlockReasonForSchedLine?;
     CreateSalesOrderItem _Item?;
     CreateSalesOrder _SalesOrder?;
@@ -1297,6 +1598,7 @@
 
 
 type CreateSalesOrderPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1311,7 +1613,9 @@
 
 
 type CreateSalesOrderText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string LongText?;
     CreateSAP__Message[] SAP__Messages?;
@@ -1333,7 +1637,7 @@
     SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: ItemPartnerOfSalesOrderItemExpandOptions
+type ItemPartnerOfSalesOrderItemExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
 # Represents the Queries record for the operation: getSalesOrderItemText
 
@@ -1359,7 +1663,7 @@
     SalesOrderItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemPartnerExpandOptions
+type SalesOrderItemPartnerExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfSalesOrderPartner
 
@@ -1370,7 +1674,7 @@
     SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: ItemPartnerOfSalesOrderItemSelectOptions
+type ItemPartnerOfSalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"PartnerFunction"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"PartnerIsSpecificForSDDocItem"|"SAP__Messages")[];
 
 
 type UpdateSalesOrderPartner record {
@@ -1452,7 +1756,7 @@
     ItemPartnerOfSalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: ItemPartnerOfSalesOrderItemOrderByOptions
+type ItemPartnerOfSalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PartnerFunction"|"PartnerFunction desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"PartnerIsSpecificForSDDocItem"|"PartnerIsSpecificForSDDocItem desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
 # Represents the Queries record for the operation: listSalesOrderItemPartners
 
@@ -1473,7 +1777,7 @@
     SalesOrderItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemPartnerOrderByOptions
+type SalesOrderItemPartnerOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PartnerFunction"|"PartnerFunction desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"PartnerIsSpecificForSDDocItem"|"PartnerIsSpecificForSDDocItem desc"|"SAP__Messages"|"SAP__Messages desc")[];
 
 # Represents the Queries record for the operation: listScheduleLinesOfSalesOrderItem
 
@@ -1494,7 +1798,7 @@
     ScheduleLineOfSalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: ScheduleLineOfSalesOrderItemOrderByOptions
+type ScheduleLineOfSalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"ScheduleLine"|"ScheduleLine desc"|"ScheduleLineCategory"|"ScheduleLineCategory desc"|"ScheduleLineOrderQuantity"|"ScheduleLineOrderQuantity desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ConfirmedDeliveryDate"|"ConfirmedDeliveryDate desc"|"ConfdOrderQtyByMatlAvailCheck"|"ConfdOrderQtyByMatlAvailCheck desc"|"DeliveredQtyInOrderQtyUnit"|"DeliveredQtyInOrderQtyUnit desc"|"OpenConfdDelivQtyInOrdQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit desc"|"CorrectedQtyInOrderQtyUnit"|"CorrectedQtyInOrderQtyUnit desc"|"DelivBlockReasonForSchedLine"|"DelivBlockReasonForSchedLine desc"|"PurchaseRequisition"|"PurchaseRequisition desc"|"PurchaseRequisitionItem"|"PurchaseRequisitionItem desc"|"GoodsMovementType"|"GoodsMovementType desc")[];
 
 
 type CollectionOfSalesOrderText record {
@@ -1537,7 +1841,7 @@
     ItemPricingElementOfSalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: ItemPricingElementOfSalesOrderItemExpandOptions
+type ItemPricingElementOfSalesOrderItemExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
 # Represents the Queries record for the operation: listSalesOrderItemPricingElements
 
@@ -1558,9 +1862,9 @@
     SalesOrderItemPricingElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemPricingElementExpandOptions
+type SalesOrderItemPricingElementExpandOptions ("*"|"_Item"|"_SalesOrder")[];
 
-// Unknown type: SalesOrderItemPricingElementSelectOptions
+type SalesOrderItemPricingElementSelectOptions ("SalesOrder"|"SalesOrderItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"ConditionCalculationType"|"ConditionRateAmount"|"ConditionCurrency"|"ConditionQuantity"|"ConditionBaseQuantity"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionRateRatio"|"ConditionRateRatioSAPUnit"|"ConditionRateRatioISOUnit"|"ConditionAmount"|"ConditionBaseAmount"|"TransactionCurrency"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getItemOfSalesOrderItemText
 
@@ -1571,9 +1875,9 @@
     ItemOfSalesOrderItemTextSelectOptions \$select?;
 };
 
-// Unknown type: ItemOfSalesOrderItemTextExpandOptions
+type ItemOfSalesOrderItemTextExpandOptions ("*"|"_ItemPartner"|"_ItemPricingElement"|"_ItemText"|"_SalesOrder"|"_ScheduleLine")[];
 
-// Unknown type: ItemOfSalesOrderItemTextSelectOptions
+type ItemOfSalesOrderItemTextSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"SalesOrderItemCategory"|"SalesOrderItemText"|"Product"|"ProductGroup"|"MaterialByCustomer"|"InternationalArticleNumber"|"PurchaseOrderByCustomer"|"ConfdDelivQtyInOrderQtyUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"RequestedQuantity"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"PricingDate"|"ServicesRenderedDate"|"BillingDocumentDate"|"NetAmount"|"TransactionCurrency"|"TaxAmount"|"CustomerGroup"|"Batch"|"Plant"|"StorageLocation"|"ShippingPoint"|"ShippingType"|"Route"|"DeliveryPriority"|"PartialDeliveryIsAllowed"|"MaxNmbrOfPartialDelivery"|"DeliveryDateTypeRule"|"ReceivingPoint"|"DeliveryGroup"|"IncotermsClassification"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerPriceGroup"|"MaterialPricingGroup"|"BusinessArea"|"ProfitCenter"|"MatlAccountAssignmentGroup"|"ItemBillingBlockReason"|"SalesDocumentRjcnReason"|"ProductConfiguration"|"SDProcessStatus"|"SDDocumentRejectionStatus"|"DeliveryStatus"|"BillingBlockStatus"|"ItemGeneralIncompletionStatus"|"DeliveryBlockStatus"|"SlsOrderItemDownPaymentStatus"|"OrderRelatedBillingStatus"|"ChmlCmplncStatus"|"DangerousGoodsStatus"|"SafetyDataSheetStatus"|"TrdCmplncEmbargoSts"|"TrdCmplncSnctndListChkSts"|"OvrlTrdCmplncLegalCtrlChkSts"|"SAP__Messages")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfSalesOrderText
 
@@ -1586,20 +1890,31 @@
 
 
 type UpdateSalesOrder record {
+    @constraint:String {maxLength: 10}
     string SoldToParty?;
+    @constraint:String {maxLength: 4}
     string SalesOrganization?;
+    @constraint:String {maxLength: 2}
     string DistributionChannel?;
+    @constraint:String {maxLength: 2}
     string OrganizationDivision?;
+    @constraint:String {maxLength: 4}
     string SalesOffice?;
+    @constraint:String {maxLength: 3}
     string SalesGroup?;
+    @constraint:String {maxLength: 6}
     string SalesDistrict?;
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByCustomer?;
     # Ship-to Party's Customer Reference
+    @constraint:String {maxLength: 35}
     string PurchaseOrderByShipToParty?;
     # Customer Purchase Order Type
+    @constraint:String {maxLength: 4}
     string CustomerPurchaseOrderType?;
     string? CustomerPurchaseOrderDate?;
     # Order Reason (Reason for the Business Transaction)
+    @constraint:String {maxLength: 3}
     string SDDocumentReason?;
     # Document Date (Date Received/Sent)
     string? SalesOrderDate?;
@@ -1610,43 +1925,69 @@
     string? ServicesRenderedDate?;
     string? BillingDocumentDate?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
+    @constraint:String {maxLength: 1}
     string DeliveryDateTypeRule?;
+    @constraint:String {maxLength: 2}
     string ShippingCondition?;
     # Complete Delivery Defined for Each Sales Order
     boolean CompleteDeliveryIsDefined?;
     boolean SlsDocIsRlvtForProofOfDeliv?;
+    @constraint:String {maxLength: 2}
     string ShippingType?;
+    @constraint:String {maxLength: 25}
     string ReceivingPoint?;
     # Incoterms (Part 1)
+    @constraint:String {maxLength: 3}
     string IncotermsClassification?;
+    @constraint:String {maxLength: 4}
     string IncotermsVersion?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation1?;
+    @constraint:String {maxLength: 70}
     string IncotermsLocation2?;
+    @constraint:String {maxLength: 2}
     string CustomerPriceGroup?;
+    @constraint:String {maxLength: 2}
     string PriceListType?;
     string? FixedValueDate?;
+    @constraint:String {maxLength: 3}
     string TaxDepartureCountry?;
+    @constraint:String {maxLength: 3}
     string VATRegistrationCountry?;
     # Indicator: Triangular Deal Within the EU
     boolean IsEUTriangularDeal?;
     # Key for Terms of Payment
+    @constraint:String {maxLength: 4}
     string CustomerPaymentTerms?;
+    @constraint:String {maxLength: 1}
     string PaymentMethod?;
+    @constraint:String {maxLength: 2}
     string CustomerAccountAssignmentGroup?;
     # Assignment Number
+    @constraint:String {maxLength: 18}
     string AssignmentReference?;
     # Reference Document Number
+    @constraint:String {maxLength: 16}
     string AccountingDocExternalReference?;
     # Billing Block in SD Document
+    @constraint:String {maxLength: 2}
     string HeaderBillingBlockReason?;
     # Delivery Block (Document Header)
+    @constraint:String {maxLength: 2}
     string DeliveryBlockReason?;
+    @constraint:String {maxLength: 2}
     string CustomerGroup?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup1?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup2?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup3?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup4?;
+    @constraint:String {maxLength: 3}
     string AdditionalCustomerGroup5?;
     UpdateSAP__Message[] SAP__Messages?;
 };
@@ -1660,23 +2001,27 @@
     ItemOfSalesOrderItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: ItemOfSalesOrderItemPartnerExpandOptions
+type ItemOfSalesOrderItemPartnerExpandOptions ("*"|"_ItemPartner"|"_ItemPricingElement"|"_ItemText"|"_SalesOrder"|"_ScheduleLine")[];
 
 
 type UpdateSalesOrderItemPricingElmnt record {
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     decimal|string? ConditionAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     UpdateSAP__Message[] SAP__Messages?;
 };
@@ -1760,17 +2105,21 @@
 type UpdateSalesOrderPricingElement record {
     decimal|string? ConditionRateAmount?;
     # Currency Key
+    @constraint:String {maxLength: 3}
     string ConditionCurrency?;
     # Condition Pricing Unit
     decimal|string? ConditionQuantity?;
     # Condition Unit in the Document
+    @constraint:String {maxLength: 3}
     string ConditionQuantitySAPUnit?;
     # ISO Unit Code for Condition Quantity
+    @constraint:String {maxLength: 3}
     string ConditionQuantityISOUnit?;
     # Condition Ratio (in Percent or Per Mille)
     decimal|string? ConditionRateRatio?;
     decimal|string? ConditionAmount?;
     # SD Document Currency
+    @constraint:String {maxLength: 3}
     string TransactionCurrency?;
     UpdateSAP__Message[] SAP__Messages?;
 };
@@ -1882,155 +2231,155 @@
 
     # Get related _Item
     # 
-    remote function getItemOfSalesOrderItemPartner(string SalesOrder, string salesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, ItemOfSalesOrderItemPartnerExpandOptions \$expand = [], ItemOfSalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, GetItemOfSalesOrderItemPartnerQueries queries) returns SalesOrderItem|error;
+    remote function getItemOfSalesOrderItemPartner(string SalesOrder, string salesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, ItemOfSalesOrderItemPartnerExpandOptions \$expand = [], ItemOfSalesOrderItemPartnerSelectOptions \$select = [], GetItemOfSalesOrderItemPartnerQueries queries) returns SalesOrderItem|error;
 
     # Get related _Item
     # 
-    remote function getItemOfSalesOrderItemPricingElement(string SalesOrder, string salesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, ItemOfSalesOrderItemPricingElementExpandOptions \$expand = [], ItemOfSalesOrderItemPricingElementSelectOptions \$select = [], anydata Additional Values, GetItemOfSalesOrderItemPricingElementQueries queries) returns SalesOrderItem|error;
+    remote function getItemOfSalesOrderItemPricingElement(string SalesOrder, string salesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, ItemOfSalesOrderItemPricingElementExpandOptions \$expand = [], ItemOfSalesOrderItemPricingElementSelectOptions \$select = [], GetItemOfSalesOrderItemPricingElementQueries queries) returns SalesOrderItem|error;
 
     # Get related _Item
     # 
-    remote function getItemOfSalesOrderItemText(string SalesOrder, string salesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, ItemOfSalesOrderItemTextExpandOptions \$expand = [], ItemOfSalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, GetItemOfSalesOrderItemTextQueries queries) returns SalesOrderItem|error;
+    remote function getItemOfSalesOrderItemText(string SalesOrder, string salesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, ItemOfSalesOrderItemTextExpandOptions \$expand = [], ItemOfSalesOrderItemTextSelectOptions \$select = [], GetItemOfSalesOrderItemTextQueries queries) returns SalesOrderItem|error;
 
     # Get related _Item
     # 
-    remote function getItemOfSalesOrderScheduleLine(string SalesOrder, string salesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, ItemOfSalesOrderScheduleLineExpandOptions \$expand = [], ItemOfSalesOrderScheduleLineSelectOptions \$select = [], anydata Additional Values, GetItemOfSalesOrderScheduleLineQueries queries) returns SalesOrderItem|error;
+    remote function getItemOfSalesOrderScheduleLine(string SalesOrder, string salesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, ItemOfSalesOrderScheduleLineExpandOptions \$expand = [], ItemOfSalesOrderScheduleLineSelectOptions \$select = [], GetItemOfSalesOrderScheduleLineQueries queries) returns SalesOrderItem|error;
 
     # Get entity from SalesOrder by key
     # 
-    remote function getSalesOrder(string salesOrder, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderQueries queries) returns SalesOrder|error;
+    remote function getSalesOrder(string salesOrder, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderQueries queries) returns SalesOrder|error;
 
     # Get entity from SalesOrderItem by key
     # 
-    remote function getSalesOrderItem(string SalesOrder, string salesOrderItem, map<string|string[]> headers = {}, SalesOrderItemExpandOptions \$expand = [], SalesOrderItemSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemQueries queries) returns SalesOrderItem|error;
+    remote function getSalesOrderItem(string SalesOrder, string salesOrderItem, map<string|string[]> headers = {}, SalesOrderItemExpandOptions \$expand = [], SalesOrderItemSelectOptions \$select = [], GetSalesOrderItemQueries queries) returns SalesOrderItem|error;
 
     # Get entity from SalesOrderItemPartner by key
     # 
-    remote function getSalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemPartnerQueries queries) returns SalesOrderItemPartner|error;
+    remote function getSalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderItemPartnerSelectOptions \$select = [], GetSalesOrderItemPartnerQueries queries) returns SalesOrderItemPartner|error;
 
     # Get entity from SalesOrderItemPricingElement by key
     # 
-    remote function getSalesOrderItemPricingElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderItemPricingElementExpandOptions \$expand = [], SalesOrderItemPricingElementSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemPricingElementQueries queries) returns SalesOrderItemPricingElmnt|error;
+    remote function getSalesOrderItemPricingElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderItemPricingElementExpandOptions \$expand = [], SalesOrderItemPricingElementSelectOptions \$select = [], GetSalesOrderItemPricingElementQueries queries) returns SalesOrderItemPricingElmnt|error;
 
     # Get entity from SalesOrderItemText by key
     # 
-    remote function getSalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderItemTextExpandOptions \$expand = [], SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemTextQueries queries) returns SalesOrderItemText|error;
+    remote function getSalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderItemTextExpandOptions \$expand = [], SalesOrderItemTextSelectOptions \$select = [], GetSalesOrderItemTextQueries queries) returns SalesOrderItemText|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderItem(string salesOrder, string SalesOrderItem, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderItemQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderItem(string salesOrder, string SalesOrderItem, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderItemQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderItemPartner(string salesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderItemPartnerQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderItemPartner(string salesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderItemPartnerQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderItemPricingElement(string salesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderItemPricingElementQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderItemPricingElement(string salesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderItemPricingElementQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderItemText(string salesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderItemTextQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderItemText(string salesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderItemTextQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderPartner(string salesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderPartnerQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderPartner(string salesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderPartnerQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderPricingElement(string salesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderPricingElementQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderPricingElement(string salesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderPricingElementQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderScheduleLine(string salesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderScheduleLineQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderScheduleLine(string salesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderScheduleLineQueries queries) returns SalesOrder|error;
 
     # Get related _SalesOrder
     # 
-    remote function getSalesOrderOfSalesOrderText(string salesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfSalesOrderTextQueries queries) returns SalesOrder|error;
+    remote function getSalesOrderOfSalesOrderText(string salesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderExpandOptions \$expand = [], SalesOrderSelectOptions \$select = [], GetSalesOrderOfSalesOrderTextQueries queries) returns SalesOrder|error;
 
     # Get entity from SalesOrderPartner by key
     # 
-    remote function getSalesOrderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderPartnerExpandOptions \$expand = [], SalesOrderPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesOrderPartnerQueries queries) returns SalesOrderPartner|error;
+    remote function getSalesOrderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderPartnerExpandOptions \$expand = [], SalesOrderPartnerSelectOptions \$select = [], GetSalesOrderPartnerQueries queries) returns SalesOrderPartner|error;
 
     # Get entity from SalesOrderPricingElement by key
     # 
-    remote function getSalesOrderPricingElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderPricingElementExpandOptions \$expand = [], SalesOrderPricingElementSelectOptions \$select = [], anydata Additional Values, GetSalesOrderPricingElementQueries queries) returns SalesOrderPricingElement|error;
+    remote function getSalesOrderPricingElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderPricingElementExpandOptions \$expand = [], SalesOrderPricingElementSelectOptions \$select = [], GetSalesOrderPricingElementQueries queries) returns SalesOrderPricingElement|error;
 
     # Get entity from SalesOrderScheduleLine by key
     # 
-    remote function getSalesOrderScheduleLine(string SalesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, SalesOrderScheduleLineExpandOptions \$expand = [], SalesOrderScheduleLineSelectOptions \$select = [], anydata Additional Values, GetSalesOrderScheduleLineQueries queries) returns SalesOrderScheduleLine|error;
+    remote function getSalesOrderScheduleLine(string SalesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, SalesOrderScheduleLineExpandOptions \$expand = [], SalesOrderScheduleLineSelectOptions \$select = [], GetSalesOrderScheduleLineQueries queries) returns SalesOrderScheduleLine|error;
 
     # Get entity from SalesOrderText by key
     # 
-    remote function getSalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderTextExpandOptions \$expand = [], SalesOrderTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrderTextQueries queries) returns SalesOrderText|error;
+    remote function getSalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderTextExpandOptions \$expand = [], SalesOrderTextSelectOptions \$select = [], GetSalesOrderTextQueries queries) returns SalesOrderText|error;
 
     # Get entities from related _ItemPartner
     # 
-    remote function listItemPartnersOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ItemPartnerOfSalesOrderItemOrderByOptions \$orderby = [], ItemPartnerOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemPartnerOfSalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListItemPartnersOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemPartner|error;
+    remote function listItemPartnersOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ItemPartnerOfSalesOrderItemOrderByOptions \$orderby = [], ItemPartnerOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemPartnerOfSalesOrderItemSelectOptions \$select = [], ListItemPartnersOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemPartner|error;
 
     # Get entities from related _ItemPricingElement
     # 
-    remote function listItemPricingElementsOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, ItemPricingElementOfSalesOrderItemOrderByOptions \$orderby = [], ItemPricingElementOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemPricingElementOfSalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListItemPricingElementsOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemPricingElmnt|error;
+    remote function listItemPricingElementsOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, ItemPricingElementOfSalesOrderItemOrderByOptions \$orderby = [], ItemPricingElementOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemPricingElementOfSalesOrderItemSelectOptions \$select = [], ListItemPricingElementsOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemPricingElmnt|error;
 
     # Get entities from related _ItemText
     # 
-    remote function listItemTextsOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ItemTextOfSalesOrderItemOrderByOptions \$orderby = [], ItemTextOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemTextOfSalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListItemTextsOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemText|error;
+    remote function listItemTextsOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ItemTextOfSalesOrderItemOrderByOptions \$orderby = [], ItemTextOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ItemTextOfSalesOrderItemSelectOptions \$select = [], ListItemTextsOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderItemText|error;
 
     # Get entities from related _Item
     # 
-    remote function listItemsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemOrderByOptions \$orderby = [], SalesOrderItemExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListItemsOfSalesOrderQueries queries) returns CollectionOfSalesOrderItem|error;
+    remote function listItemsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemOrderByOptions \$orderby = [], SalesOrderItemExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemSelectOptions \$select = [], ListItemsOfSalesOrderQueries queries) returns CollectionOfSalesOrderItem|error;
 
     # Get entities from related _Partner
     # 
-    remote function listPartnersOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPartnerOrderByOptions \$orderby = [], SalesOrderPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfSalesOrderQueries queries) returns CollectionOfSalesOrderPartner|error;
+    remote function listPartnersOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPartnerOrderByOptions \$orderby = [], SalesOrderPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderPartnerSelectOptions \$select = [], ListPartnersOfSalesOrderQueries queries) returns CollectionOfSalesOrderPartner|error;
 
     # Get entities from related _PricingElement
     # 
-    remote function listPricingElementsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, SalesOrderPricingElementOrderByOptions \$orderby = [], SalesOrderPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderPricingElementSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfSalesOrderQueries queries) returns CollectionOfSalesOrderPricingElement|error;
+    remote function listPricingElementsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, SalesOrderPricingElementOrderByOptions \$orderby = [], SalesOrderPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderPricingElementSelectOptions \$select = [], ListPricingElementsOfSalesOrderQueries queries) returns CollectionOfSalesOrderPricingElement|error;
 
     # Get entities from SalesOrderItemPartner
     # 
-    remote function listSalesOrderItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemPartnerOrderByOptions \$orderby = [], SalesOrderItemPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, ListSalesOrderItemPartnersQueries queries) returns CollectionOfSalesOrderItemPartner|error;
+    remote function listSalesOrderItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemPartnerOrderByOptions \$orderby = [], SalesOrderItemPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemPartnerSelectOptions \$select = [], ListSalesOrderItemPartnersQueries queries) returns CollectionOfSalesOrderItemPartner|error;
 
     # Get entities from SalesOrderItemPricingElement
     # 
-    remote function listSalesOrderItemPricingElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemPricingElementOrderByOptions \$orderby = [], SalesOrderItemPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemPricingElementSelectOptions \$select = [], anydata Additional Values, ListSalesOrderItemPricingElementsQueries queries) returns CollectionOfSalesOrderItemPricingElmnt|error;
+    remote function listSalesOrderItemPricingElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemPricingElementOrderByOptions \$orderby = [], SalesOrderItemPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemPricingElementSelectOptions \$select = [], ListSalesOrderItemPricingElementsQueries queries) returns CollectionOfSalesOrderItemPricingElmnt|error;
 
     # Get entities from SalesOrderItemText
     # 
-    remote function listSalesOrderItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemTextOrderByOptions \$orderby = [], SalesOrderItemTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, ListSalesOrderItemTextsQueries queries) returns CollectionOfSalesOrderItemText|error;
+    remote function listSalesOrderItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemTextOrderByOptions \$orderby = [], SalesOrderItemTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemTextSelectOptions \$select = [], ListSalesOrderItemTextsQueries queries) returns CollectionOfSalesOrderItemText|error;
 
     # Get entities from SalesOrderItem
     # 
-    remote function listSalesOrderItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemOrderByOptions \$orderby = [], SalesOrderItemExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListSalesOrderItemsQueries queries) returns CollectionOfSalesOrderItem|error;
+    remote function listSalesOrderItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderItemOrderByOptions \$orderby = [], SalesOrderItemExpandOptions \$expand = [], boolean \$count = false, SalesOrderItemSelectOptions \$select = [], ListSalesOrderItemsQueries queries) returns CollectionOfSalesOrderItem|error;
 
     # Get entities from SalesOrderPartner
     # 
-    remote function listSalesOrderPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPartnerOrderByOptions \$orderby = [], SalesOrderPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderPartnerSelectOptions \$select = [], anydata Additional Values, ListSalesOrderPartnersQueries queries) returns CollectionOfSalesOrderPartner|error;
+    remote function listSalesOrderPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPartnerOrderByOptions \$orderby = [], SalesOrderPartnerExpandOptions \$expand = [], boolean \$count = false, SalesOrderPartnerSelectOptions \$select = [], ListSalesOrderPartnersQueries queries) returns CollectionOfSalesOrderPartner|error;
 
     # Get entities from SalesOrderPricingElement
     # 
-    remote function listSalesOrderPricingElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPricingElementOrderByOptions \$orderby = [], SalesOrderPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderPricingElementSelectOptions \$select = [], anydata Additional Values, ListSalesOrderPricingElementsQueries queries) returns CollectionOfSalesOrderPricingElement|error;
+    remote function listSalesOrderPricingElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderPricingElementOrderByOptions \$orderby = [], SalesOrderPricingElementExpandOptions \$expand = [], boolean \$count = false, SalesOrderPricingElementSelectOptions \$select = [], ListSalesOrderPricingElementsQueries queries) returns CollectionOfSalesOrderPricingElement|error;
 
     # Get entities from SalesOrderScheduleLine
     # 
-    remote function listSalesOrderScheduleLines(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderScheduleLineOrderByOptions \$orderby = [], SalesOrderScheduleLineExpandOptions \$expand = [], boolean \$count = false, SalesOrderScheduleLineSelectOptions \$select = [], anydata Additional Values, ListSalesOrderScheduleLinesQueries queries) returns CollectionOfSalesOrderScheduleLine|error;
+    remote function listSalesOrderScheduleLines(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderScheduleLineOrderByOptions \$orderby = [], SalesOrderScheduleLineExpandOptions \$expand = [], boolean \$count = false, SalesOrderScheduleLineSelectOptions \$select = [], ListSalesOrderScheduleLinesQueries queries) returns CollectionOfSalesOrderScheduleLine|error;
 
     # Get entities from SalesOrderText
     # 
-    remote function listSalesOrderTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderTextOrderByOptions \$orderby = [], SalesOrderTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderTextSelectOptions \$select = [], anydata Additional Values, ListSalesOrderTextsQueries queries) returns CollectionOfSalesOrderText|error;
+    remote function listSalesOrderTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderTextOrderByOptions \$orderby = [], SalesOrderTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderTextSelectOptions \$select = [], ListSalesOrderTextsQueries queries) returns CollectionOfSalesOrderText|error;
 
     # Get entities from SalesOrder
     # 
-    remote function listSalesOrders(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderOrderByOptions \$orderby = [], SalesOrderExpandOptions \$expand = [], boolean \$count = false, SalesOrderSelectOptions \$select = [], anydata Additional Values, ListSalesOrdersQueries queries) returns CollectionOfSalesOrder|error;
+    remote function listSalesOrders(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderOrderByOptions \$orderby = [], SalesOrderExpandOptions \$expand = [], boolean \$count = false, SalesOrderSelectOptions \$select = [], ListSalesOrdersQueries queries) returns CollectionOfSalesOrder|error;
 
     # Get entities from related _ScheduleLine
     # 
-    remote function listScheduleLinesOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ScheduleLineOfSalesOrderItemOrderByOptions \$orderby = [], ScheduleLineOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ScheduleLineOfSalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListScheduleLinesOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderScheduleLine|error;
+    remote function listScheduleLinesOfSalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ScheduleLineOfSalesOrderItemOrderByOptions \$orderby = [], ScheduleLineOfSalesOrderItemExpandOptions \$expand = [], boolean \$count = false, ScheduleLineOfSalesOrderItemSelectOptions \$select = [], ListScheduleLinesOfSalesOrderItemQueries queries) returns CollectionOfSalesOrderScheduleLine|error;
 
     # Get entities from related _Text
     # 
-    remote function listTextsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderTextOrderByOptions \$orderby = [], SalesOrderTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfSalesOrderQueries queries) returns CollectionOfSalesOrderText|error;
+    remote function listTextsOfSalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SalesOrderTextOrderByOptions \$orderby = [], SalesOrderTextExpandOptions \$expand = [], boolean \$count = false, SalesOrderTextSelectOptions \$select = [], ListTextsOfSalesOrderQueries queries) returns CollectionOfSalesOrderText|error;
 
     # Update entity in SalesOrder
     # 
`````

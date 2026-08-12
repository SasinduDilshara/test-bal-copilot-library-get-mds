# sap.s4hana.api_sales_quotation_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sales_quotation_srv` |
| **Old file** | `sap.s4hana.api_sales_quotation_srv/old/ballerinax_sap.s4hana.api_sales_quotation_srv.bal.txt` |
| **New file** | `sap.s4hana.api_sales_quotation_srv/new/ballerinax_sap.s4hana.api_sales_quotation_srv.bal.txt` |
| **Old lines** | 3176 |
| **New lines** | 3232 |
| **Lines added** | 220 |
| **Lines removed** | 164 |
| **Hunks** | 83 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 102 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (102)

- `type A_SalesQuotationExpandOptions`
- `type A_SalesQuotationItemExpandOptions`
- `type A_SalesQuotationItemOrderByOptions`
- `type A_SalesQuotationItemPartnerExpandOptions`
- `type A_SalesQuotationItemPartnerOrderByOptions`
- `type A_SalesQuotationItemPartnerSelectOptions`
- `type A_SalesQuotationItemPrcgElmntExpandOptions`
- `type A_SalesQuotationItemPrcgElmntOrderByOptions`
- `type A_SalesQuotationItemPrcgElmntSelectOptions`
- `type A_SalesQuotationItemSelectOptions`
- `type A_SalesQuotationItemTextExpandOptions`
- `type A_SalesQuotationItemTextOrderByOptions`
- `type A_SalesQuotationItemTextSelectOptions`
- `type A_SalesQuotationOrderByOptions`
- `type A_SalesQuotationPartnerExpandOptions`
- `type A_SalesQuotationPartnerOrderByOptions`
- `type A_SalesQuotationPartnerSelectOptions`
- `type A_SalesQuotationPrcgElmntExpandOptions`
- `type A_SalesQuotationPrcgElmntOrderByOptions`
- `type A_SalesQuotationPrcgElmntSelectOptions`
- `type A_SalesQuotationRelatedObjectExpandOptions`
- `type A_SalesQuotationRelatedObjectOrderByOptions`
- `type A_SalesQuotationRelatedObjectSelectOptions`
- `type A_SalesQuotationSelectOptions`
- `type A_SalesQuotationTextExpandOptions`
- `type A_SalesQuotationTextOrderByOptions`
- `type A_SalesQuotationTextSelectOptions`
- `type A_SlsQtanItemRelatedObjectExpandOptions`
- `type A_SlsQtanItemRelatedObjectOrderByOptions`
- `type A_SlsQtanItemRelatedObjectSelectOptions`
- `type A_SlsQtanItmPrecdgProcFlowExpandOptions`
- `type A_SlsQtanItmPrecdgProcFlowOrderByOptions`
- `type A_SlsQtanItmPrecdgProcFlowSelectOptions`
- `type A_SlsQtanItmSubsqntProcFlowExpandOptions`
- `type A_SlsQtanItmSubsqntProcFlowOrderByOptions`
- `type A_SlsQtanItmSubsqntProcFlowSelectOptions`
- `type A_SlsQtanPrecdgProcFlowExpandOptions`
- `type A_SlsQtanPrecdgProcFlowOrderByOptions`
- `type A_SlsQtanPrecdgProcFlowSelectOptions`
- `type A_SlsQtanSubsqntProcFlowExpandOptions`
- `type A_SlsQtanSubsqntProcFlowOrderByOptions`
- `type A_SlsQtanSubsqntProcFlowSelectOptions`
- `type PrecedingProcFlowDocItemOfA_SalesQuotationItemExpandOptions`
- `type PrecedingProcFlowDocItemOfA_SalesQuotationItemOrderByOptions`
- `type PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions`
- `type PrecedingProcFlowDocOfA_SalesQuotationExpandOptions`
- `type PrecedingProcFlowDocOfA_SalesQuotationOrderByOptions`
- `type PrecedingProcFlowDocOfA_SalesQuotationSelectOptions`
- `type PricingElementOfA_SalesQuotationExpandOptions`
- `type PricingElementOfA_SalesQuotationItemExpandOptions`
- `type PricingElementOfA_SalesQuotationItemOrderByOptions`
- `type PricingElementOfA_SalesQuotationItemSelectOptions`
- `type PricingElementOfA_SalesQuotationOrderByOptions`
- `type PricingElementOfA_SalesQuotationSelectOptions`
- `type RelatedObjectOfA_SalesQuotationItemExpandOptions`
- `type RelatedObjectOfA_SalesQuotationItemOrderByOptions`
- `type RelatedObjectOfA_SalesQuotationItemSelectOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemPartnerExpandOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemPrcgElmntExpandOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemTextExpandOptions`
- `type SalesQuotationItemOfA_SalesQuotationItemTextSelectOptions`
- `type SalesQuotationItemOfA_SlsQtanItemRelatedObjectExpandOptions`
- `type SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions`
- `type SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowExpandOptions`
- `type SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions`
- `type SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowExpandOptions`
- `type SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions`
- `type SalesQuotationOfA_SalesQuotationItemExpandOptions`
- `type SalesQuotationOfA_SalesQuotationItemPartnerExpandOptions`
- `type SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions`
- `type SalesQuotationOfA_SalesQuotationItemPrcgElmntExpandOptions`
- `type SalesQuotationOfA_SalesQuotationItemPrcgElmntSelectOptions`
- `type SalesQuotationOfA_SalesQuotationItemSelectOptions`
- `type SalesQuotationOfA_SalesQuotationItemTextExpandOptions`
- `type SalesQuotationOfA_SalesQuotationItemTextSelectOptions`
- `type SalesQuotationOfA_SalesQuotationPartnerExpandOptions`
- `type SalesQuotationOfA_SalesQuotationPartnerSelectOptions`
- `type SalesQuotationOfA_SalesQuotationPrcgElmntExpandOptions`
- `type SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions`
- `type SalesQuotationOfA_SalesQuotationRelatedObjectExpandOptions`
- `type SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions`
- `type SalesQuotationOfA_SalesQuotationTextExpandOptions`
- `type SalesQuotationOfA_SalesQuotationTextSelectOptions`
- `type SalesQuotationOfA_SlsQtanItemRelatedObjectExpandOptions`
- `type SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions`
- `type SalesQuotationOfA_SlsQtanItmPrecdgProcFlowExpandOptions`
- `type SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions`
- `type SalesQuotationOfA_SlsQtanItmSubsqntProcFlowExpandOptions`
- `type SalesQuotationOfA_SlsQtanItmSubsqntProcFlowSelectOptions`
- `type SalesQuotationOfA_SlsQtanPrecdgProcFlowExpandOptions`
- `type SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions`
- `type SalesQuotationOfA_SlsQtanSubsqntProcFlowExpandOptions`
- `type SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions`
- `type SubsequentProcFlowDocItemOfA_SalesQuotationItemExpandOptions`
- `type SubsequentProcFlowDocItemOfA_SalesQuotationItemOrderByOptions`
- `type SubsequentProcFlowDocItemOfA_SalesQuotationItemSelectOptions`
- `type SubsequentProcFlowDocOfA_SalesQuotationExpandOptions`
- `type SubsequentProcFlowDocOfA_SalesQuotationOrderByOptions`
- `type SubsequentProcFlowDocOfA_SalesQuotationSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 127–134 | 127–137 | Types | +3 | −0 |
| 2 | 136–141 | 139–145 | Types | +1 | −0 |
| 3 | 243–249 | 247–255 | Types | +2 | −0 |
| 4 | 360–368 | 366–377 | Types | +3 | −0 |
| 5 | 386–393 | 395–404 | Types | +2 | −0 |
| 6 | 420–430 | 431–445 | Types | +4 | −0 |
| 7 | 508–516 | 523–534 | Types | +3 | −0 |
| 8 | 532–539 | 550–559 | Types | +2 | −0 |
| 9 | 566–574 | 586–598 | Types | +4 | −0 |
| 10 | 583–589 | 607–615 | Types | +2 | −0 |
| 11 | 606–611 | 632–638 | Types | +1 | −0 |
| 12 | 635–643 | 662–673 | Types | +3 | −0 |
| 13 | 716–723 | 746–755 | Types | +2 | −0 |
| 14 | 738–743 | 770–776 | Types | +1 | −0 |
| 15 | 771–779 | 804–813 | Types | +3 | −2 |
| 16 | 784–792 | 818–826 | Types | +2 | −2 |
| 17 | 794–810 | 828–844 | Types | +6 | −6 |
| 18 | 894–904 | 928–938 | Types | +3 | −3 |
| 19 | 913–918 | 947–953 | Types | +1 | −0 |
| 20 | 983–988 | 1018–1024 | Types | +1 | −0 |
| 21 | 1001–1007 | 1037–1043 | Types | +1 | −1 |
| 22 | 1017–1025 | 1053–1061 | Types | +2 | −2 |
| 23 | 1036–1044 | 1072–1080 | Types | +2 | −2 |
| 24 | 1053–1059 | 1089–1097 | Types | +2 | −0 |
| 25 | 1062–1067 | 1100–1106 | Types | +1 | −0 |
| 26 | 1143–1148 | 1182–1188 | Types | +1 | −0 |
| 27 | 1230–1235 | 1270–1276 | Types | +1 | −0 |
| 28 | 1250–1257 | 1291–1300 | Types | +2 | −0 |
| 29 | 1284–1291 | 1327–1336 | Types | +2 | −0 |
| 30 | 1333–1340 | 1378–1387 | Types | +2 | −0 |
| 31 | 1372–1377 | 1419–1425 | Types | +1 | −0 |
| 32 | 1391–1396 | 1439–1445 | Types | +1 | −0 |
| 33 | 1420–1427 | 1469–1478 | Types | +2 | −0 |
| 34 | 1467–1472 | 1518–1524 | Types | +1 | −0 |
| 35 | 1496–1508 | 1548–1562 | Types | +3 | −1 |
| 36 | 1522–1532 | 1576–1586 | Types | +3 | −3 |
| 37 | 1538–1551 | 1592–1605 | Types | +2 | −2 |
| 38 | 1556–1570 | 1610–1624 | Types | +5 | −5 |
| 39 | 1582–1605 | 1636–1659 | Types | +7 | −7 |
| 40 | 1615–1621 | 1669–1675 | Types | +1 | −1 |
| 41 | 1626–1634 | 1680–1688 | Types | +2 | −2 |
| 42 | 1649–1655 | 1703–1709 | Types | +1 | −1 |
| 43 | 1660–1668 | 1714–1722 | Types | +2 | −2 |
| 44 | 1673–1681 | 1727–1735 | Types | +2 | −2 |
| 45 | 1692–1698 | 1746–1752 | Types | +1 | −1 |
| 46 | 1713–1723 | 1767–1777 | Types | +3 | −3 |
| 47 | 1728–1740 | 1782–1794 | Types | +4 | −4 |
| 48 | 1745–1757 | 1799–1811 | Types | +4 | −4 |
| 49 | 1762–1772 | 1816–1826 | Types | +3 | −3 |
| 50 | 1783–1789 | 1837–1843 | Types | +1 | −1 |
| 51 | 1813–1830 | 1867–1884 | Types | +4 | −4 |
| 52 | 1845–1851 | 1899–1905 | Types | +1 | −1 |
| 53 | 1875–1883 | 1929–1937 | Types | +2 | −2 |
| 54 | 1898–1904 | 1952–1958 | Types | +1 | −1 |
| 55 | 1916–1924 | 1970–1978 | Types | +2 | −2 |
| 56 | 1980–1986 | 2034–2040 | Types | +1 | −1 |
| 57 | 2001–2007 | 2055–2061 | Types | +1 | −1 |
| 58 | 2031–2039 | 2085–2093 | Types | +2 | −2 |
| 59 | 2059–2065 | 2113–2119 | Types | +1 | −1 |
| 60 | 2070–2076 | 2124–2130 | Types | +1 | −1 |
| 61 | 2081–2095 | 2135–2149 | Types | +5 | −5 |
| 62 | 2115–2123 | 2169–2177 | Types | +2 | −2 |
| 63 | 2138–2144 | 2192–2198 | Types | +1 | −1 |
| 64 | 2149–2157 | 2203–2211 | Types | +2 | −2 |
| 65 | 2167–2173 | 2221–2227 | Types | +1 | −1 |
| 66 | 2192–2197 | 2246–2252 | Types | +1 | −0 |
| 67 | 2204–2210 | 2259–2265 | Types | +1 | −1 |
| 68 | 2265–2271 | 2320–2326 | Types | +1 | −1 |
| 69 | 2286–2292 | 2341–2347 | Types | +1 | −1 |
| 70 | 2307–2315 | 2362–2370 | Types | +2 | −2 |
| 71 | 2417–2423 | 2472–2478 | Types | +1 | −1 |
| 72 | 2458–2464 | 2513–2519 | Types | +1 | −1 |
| 73 | 2479–2485 | 2534–2540 | Types | +1 | −1 |
| 74 | 2499–2505 | 2554–2560 | Types | +1 | −1 |
| 75 | 2510–2516 | 2565–2571 | Types | +1 | −1 |
| 76 | 2531–2537 | 2586–2592 | Types | +1 | −1 |
| 77 | 2611–2617 | 2666–2672 | Types | +1 | −1 |
| 78 | 2657–2663 | 2712–2718 | Types | +1 | −1 |
| 79 | 2712–2718 | 2767–2773 | Types | +1 | −1 |
| 80 | 2763–2769 | 2818–2824 | Types | +1 | −1 |
| 81 | 2788–2793 | 2843–2849 | Types | +1 | −0 |
| 82 | 2892–3134 | 2948–3190 | Client | +60 | −60 |
| 83 | 3168–3176 | 3224–3232 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sales_quotation_srv/old/ballerinax_sap.s4hana.api_sales_quotation_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sales_quotation_srv/new/ballerinax_sap.s4hana.api_sales_quotation_srv.bal.txt	2026-08-12 13:19:19
@@ -127,8 +127,11 @@
 
 
 type A_SalesQuotationText record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string? LongText?;
     A_SalesQuotation to_SalesQuotation?;
@@ -136,6 +139,7 @@
 
 
 type A_SalesQuotation record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     string? SalesQuotationType?;
     string? SalesOrganization?;
@@ -243,7 +247,9 @@
 
 
 type A_SalesQuotationItem record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -360,9 +366,12 @@
 
 type A_SalesQuotationItemPartner record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # Item number of the SD document
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     string? PartnerFunctionInternalCode?;
     # Customer Number
@@ -386,8 +395,10 @@
 
 type A_SlsQtanItmPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # Subsequent Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -420,11 +431,15 @@
 
 
 type A_SalesQuotationItemPrcgElmnt record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # Condition item number
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionType?;
     # Timestamp for Pricing
@@ -508,9 +523,12 @@
 
 
 type A_SlsQtanItemRelatedObject record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
     # Sequence Number of the Related Object of an SD Document
+    @constraint:String {maxLength: 4}
     string SDDocRelatedObjectSequenceNmbr?;
     # Type of the Related Object of an SD Document
     string? SDDocumentRelatedObjectType?;
@@ -532,8 +550,10 @@
 
 type A_SlsQtanItmSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # Preceding Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -566,9 +586,13 @@
 
 
 type A_SalesQuotationItemText record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string? LongText?;
     A_SalesQuotation to_SalesQuotation?;
@@ -583,7 +607,9 @@
 
 type A_SalesQuotationPartner record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     string? PartnerFunctionInternalCode?;
     # Customer Number
@@ -606,6 +632,7 @@
 
 type A_SlsQtanPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -635,9 +662,12 @@
 
 
 type A_SalesQuotationPrcgElmnt record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionType?;
     # Timestamp for Pricing
@@ -716,8 +746,10 @@
 
 
 type A_SalesQuotationRelatedObject record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # Sequence Number of the Related Object of an SD Document
+    @constraint:String {maxLength: 4}
     string SDDocRelatedObjectSequenceNmbr?;
     # Type of the Related Object of an SD Document
     string? SDDocumentRelatedObjectType?;
@@ -738,6 +770,7 @@
 
 type A_SlsQtanSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesQuotation?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -771,9 +804,10 @@
     A_SalesQuotation[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
-// Unknown type: A_SalesQuotationItemExpandOptions
+type A_SalesQuotationItemExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationRelatedObject
 
@@ -784,9 +818,9 @@
     A_SalesQuotationRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationRelatedObjectExpandOptions
+type A_SalesQuotationRelatedObjectExpandOptions "to_SalesQuotation"[];
 
-// Unknown type: A_SalesQuotationRelatedObjectSelectOptions
+type A_SalesQuotationRelatedObjectSelectOptions ("SalesQuotation"|"SDDocRelatedObjectSequenceNmbr"|"SDDocumentRelatedObjectType"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference2"|"to_SalesQuotation")[];
 
 
 type CollectionOfA_SalesQuotationItemPrcgElmnt record {
@@ -794,17 +828,17 @@
     A_SalesQuotationItemPrcgElmnt[] results?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemSelectOptions
+type SalesQuotationOfA_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions
+type SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: PricingElementOfA_SalesQuotationItemSelectOptions
+type PricingElementOfA_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowExpandOptions
+type SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: A_SalesQuotationTextExpandOptions
+type A_SalesQuotationTextExpandOptions "to_SalesQuotation"[];
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemPrcgElmntExpandOptions
+type SalesQuotationOfA_SalesQuotationItemPrcgElmntExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type Modified\ A_SalesQuotationItemType record {
@@ -894,11 +928,11 @@
     SalesQuotationOfA_SalesQuotationTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationTextExpandOptions
+type SalesQuotationOfA_SalesQuotationTextExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SalesQuotationTextSelectOptions
+type SalesQuotationOfA_SalesQuotationTextSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions
+type PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentItem"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type UpdateA_SalesQuotationItemPartner record {
@@ -913,6 +947,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -983,6 +1018,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -1001,7 +1037,7 @@
     boolean Boolean?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationPrcgElmntExpandOptions
+type SalesQuotationOfA_SalesQuotationPrcgElmntExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type A_SlsQtanPrecdgProcFlowWrapper record {
@@ -1017,9 +1053,9 @@
     A_SalesQuotationItemPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationItemPrcgElmntExpandOptions
+type A_SalesQuotationItemPrcgElmntExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: A_SalesQuotationItemPrcgElmntSelectOptions
+type A_SalesQuotationItemPrcgElmntSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type FunctionResult_2 record {
@@ -1036,9 +1072,9 @@
     A_SalesQuotationItemPrcgElmnt d?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanItmSubsqntProcFlowExpandOptions
+type SalesQuotationOfA_SlsQtanItmSubsqntProcFlowExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SlsQtanItmSubsqntProcFlowSelectOptions
+type SalesQuotationOfA_SlsQtanItmSubsqntProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type CollectionOfA_SlsQtanPrecdgProcFlowWrapper record {
@@ -1053,7 +1089,9 @@
 
 
 type CreateA_SalesQuotationItemText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string? LongText?;
     CreateA_SalesQuotation to_SalesQuotation?;
@@ -1062,6 +1100,7 @@
 
 
 type CreateA_SalesQuotation record {
+    @constraint:String {maxLength: 10}
     string SalesQuotation;
     string? SalesQuotationType?;
     string? SalesOrganization?;
@@ -1143,6 +1182,7 @@
 
 
 type CreateA_SalesQuotationItem record {
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -1230,6 +1270,7 @@
 
 
 type CreateA_SalesQuotationItemPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1250,8 +1291,10 @@
 
 type CreateA_SlsQtanItmPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesQuotation;
     # Subsequent Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1284,8 +1327,10 @@
 
 
 type CreateA_SalesQuotationItemPrcgElmnt record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -1333,8 +1378,10 @@
 
 type CreateA_SlsQtanItmSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesQuotation;
     # Preceding Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesQuotationItem;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1372,6 +1419,7 @@
 
 
 type CreateA_SalesQuotationPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1391,6 +1439,7 @@
 
 type CreateA_SlsQtanPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesQuotation;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1420,8 +1469,10 @@
 
 
 type CreateA_SalesQuotationPrcgElmnt record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -1467,6 +1518,7 @@
 
 type CreateA_SlsQtanSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesQuotation;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1496,13 +1548,15 @@
 
 
 type CreateA_SalesQuotationText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string? LongText?;
     CreateA_SalesQuotation to_SalesQuotation?;
 };
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesQuotationSelectOptions
+type SubsequentProcFlowDocOfA_SalesQuotationSelectOptions ("SalesQuotation"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SlsQtanItmSubsqntProcFlow
 
@@ -1522,11 +1576,11 @@
     SalesQuotationOfA_SalesQuotationItemTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemTextExpandOptions
+type SalesQuotationOfA_SalesQuotationItemTextExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemTextSelectOptions
+type SalesQuotationOfA_SalesQuotationItemTextSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SlsQtanSubsqntProcFlowSelectOptions
+type A_SlsQtanSubsqntProcFlowSelectOptions ("SalesQuotation"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation")[];
 
 
 type A_SalesQuotationItemPartnerWrapper record {
@@ -1538,14 +1592,14 @@
     string? LongText?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions
+type SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type A_SalesQuotationRelatedObjectWrapper record {
     A_SalesQuotationRelatedObject d?;
 };
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesQuotationExpandOptions
+type SubsequentProcFlowDocOfA_SalesQuotationExpandOptions "to_SalesQuotation"[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationPrcgElmnt
 
@@ -1556,15 +1610,15 @@
     A_SalesQuotationPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationPrcgElmntExpandOptions
+type A_SalesQuotationPrcgElmntExpandOptions "to_SalesQuotation"[];
 
-// Unknown type: A_SalesQuotationPrcgElmntSelectOptions
+type A_SalesQuotationPrcgElmntSelectOptions ("SalesQuotation"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesQuotation")[];
 
-// Unknown type: A_SalesQuotationItemPrcgElmntOrderByOptions
+type A_SalesQuotationItemPrcgElmntOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
-// Unknown type: A_SlsQtanItmPrecdgProcFlowSelectOptions
+type A_SlsQtanItmPrecdgProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentItem"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesQuotationItemOrderByOptions
+type PrecedingProcFlowDocItemOfA_SalesQuotationItemOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentItem"|"PrecedingDocumentItem desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 
 type CollectionOfA_SalesQuotationItemPartnerWrapper record {
@@ -1582,24 +1636,24 @@
     UpdateA_SalesQuotationItemPartner d?;
 };
 
-// Unknown type: A_SalesQuotationTextSelectOptions
+type A_SalesQuotationTextSelectOptions ("SalesQuotation"|"Language"|"LongTextID"|"LongText"|"to_SalesQuotation")[];
 
-// Unknown type: PricingElementOfA_SalesQuotationExpandOptions
+type PricingElementOfA_SalesQuotationExpandOptions "to_SalesQuotation"[];
 
 
 type A_SlsQtanItemRelatedObjectWrapper record {
     A_SlsQtanItemRelatedObject d?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions
+type SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesQuotationOrderByOptions
+type A_SalesQuotationOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationType"|"SalesQuotationType desc"|"SalesOrganization"|"SalesOrganization desc"|"DistributionChannel"|"DistributionChannel desc"|"OrganizationDivision"|"OrganizationDivision desc"|"SalesGroup"|"SalesGroup desc"|"SalesOffice"|"SalesOffice desc"|"SalesDistrict"|"SalesDistrict desc"|"SoldToParty"|"SoldToParty desc"|"CreationDate"|"CreationDate desc"|"CreatedByUser"|"CreatedByUser desc"|"LastChangeDate"|"LastChangeDate desc"|"LastChangeDateTime"|"LastChangeDateTime desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderType desc"|"CustomerPurchaseOrderDate"|"CustomerPurchaseOrderDate desc"|"SalesQuotationDate"|"SalesQuotationDate desc"|"TotalNetAmount"|"TotalNetAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SDDocumentReason"|"SDDocumentReason desc"|"PricingDate"|"PricingDate desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ShippingCondition"|"ShippingCondition desc"|"CompleteDeliveryIsDefined"|"CompleteDeliveryIsDefined desc"|"ShippingType"|"ShippingType desc"|"HeaderBillingBlockReason"|"HeaderBillingBlockReason desc"|"DeliveryBlockReason"|"DeliveryBlockReason desc"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityStartDate desc"|"BindingPeriodValidityEndDate"|"BindingPeriodValidityEndDate desc"|"HdrOrderProbabilityInPercent"|"HdrOrderProbabilityInPercent desc"|"ExpectedOrderNetAmount"|"ExpectedOrderNetAmount desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"IncotermsVersion"|"IncotermsVersion desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"CustomerPriceGroup"|"CustomerPriceGroup desc"|"PriceListType"|"PriceListType desc"|"PaymentMethod"|"PaymentMethod desc"|"CustomerTaxClassification1"|"CustomerTaxClassification1 desc"|"CustomerTaxClassification2"|"CustomerTaxClassification2 desc"|"CustomerTaxClassification3"|"CustomerTaxClassification3 desc"|"CustomerTaxClassification4"|"CustomerTaxClassification4 desc"|"CustomerTaxClassification5"|"CustomerTaxClassification5 desc"|"CustomerTaxClassification6"|"CustomerTaxClassification6 desc"|"CustomerTaxClassification7"|"CustomerTaxClassification7 desc"|"CustomerTaxClassification8"|"CustomerTaxClassification8 desc"|"CustomerTaxClassification9"|"CustomerTaxClassification9 desc"|"ReferenceSDDocument"|"ReferenceSDDocument desc"|"ReferenceSDDocumentCategory"|"ReferenceSDDocumentCategory desc"|"SalesQuotationApprovalReason"|"SalesQuotationApprovalReason desc"|"SalesDocApprovalStatus"|"SalesDocApprovalStatus desc"|"OverallSDProcessStatus"|"OverallSDProcessStatus desc"|"TotalCreditCheckStatus"|"TotalCreditCheckStatus desc"|"OverallSDDocumentRejectionSts"|"OverallSDDocumentRejectionSts desc")[];
 
-// Unknown type: A_SalesQuotationItemTextExpandOptions
+type A_SalesQuotationItemTextExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: A_SlsQtanPrecdgProcFlowSelectOptions
+type A_SlsQtanPrecdgProcFlowSelectOptions ("SalesQuotation"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation")[];
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemPrcgElmntSelectOptions
+type SalesQuotationOfA_SalesQuotationItemPrcgElmntSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationText
 
@@ -1615,7 +1669,7 @@
     A_SalesQuotationText d?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationPartnerExpandOptions
+type SalesQuotationOfA_SalesQuotationPartnerExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SalesQuotationPartner
 
@@ -1626,9 +1680,9 @@
     SalesQuotationOfA_SalesQuotationPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationPartnerSelectOptions
+type SalesQuotationOfA_SalesQuotationPartnerSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesQuotationItemSelectOptions
+type A_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: listRelatedObjectsOfA_SalesQuotation
 
@@ -1649,7 +1703,7 @@
     A_SalesQuotationRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationRelatedObjectOrderByOptions
+type A_SalesQuotationRelatedObjectOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SDDocRelatedObjectSequenceNmbr"|"SDDocRelatedObjectSequenceNmbr desc"|"SDDocumentRelatedObjectType"|"SDDocumentRelatedObjectType desc"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectSystem desc"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference1 desc"|"SDDocRelatedObjectReference2"|"SDDocRelatedObjectReference2 desc")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationPartner
 
@@ -1660,9 +1714,9 @@
     A_SalesQuotationPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationPartnerExpandOptions
+type A_SalesQuotationPartnerExpandOptions "to_SalesQuotation"[];
 
-// Unknown type: A_SalesQuotationPartnerSelectOptions
+type A_SalesQuotationPartnerSelectOptions ("SalesQuotation"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"to_SalesQuotation")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationItemText
 
@@ -1673,9 +1727,9 @@
     A_SalesQuotationItemTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationItemTextSelectOptions
+type A_SalesQuotationItemTextSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"Language"|"LongTextID"|"LongText"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: PricingElementOfA_SalesQuotationItemExpandOptions
+type PricingElementOfA_SalesQuotationItemExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type CollectionOfA_SalesQuotationRelatedObject record {
@@ -1692,7 +1746,7 @@
     A_SlsQtanPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsQtanPrecdgProcFlowExpandOptions
+type A_SlsQtanPrecdgProcFlowExpandOptions "to_SalesQuotation"[];
 
 # Represents the Queries record for the operation: listRelatedObjectsOfA_SalesQuotationItem
 
@@ -1713,11 +1767,11 @@
     RelatedObjectOfA_SalesQuotationItemSelectOptions \$select?;
 };
 
-// Unknown type: RelatedObjectOfA_SalesQuotationItemOrderByOptions
+type RelatedObjectOfA_SalesQuotationItemOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"SDDocRelatedObjectSequenceNmbr"|"SDDocRelatedObjectSequenceNmbr desc"|"SDDocumentRelatedObjectType"|"SDDocumentRelatedObjectType desc"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectSystem desc"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference1 desc"|"SDDocRelatedObjectReference2"|"SDDocRelatedObjectReference2 desc")[];
 
-// Unknown type: RelatedObjectOfA_SalesQuotationItemExpandOptions
+type RelatedObjectOfA_SalesQuotationItemExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: RelatedObjectOfA_SalesQuotationItemSelectOptions
+type RelatedObjectOfA_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"SDDocRelatedObjectSequenceNmbr"|"SDDocumentRelatedObjectType"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference2"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationItem
 
@@ -1728,13 +1782,13 @@
     A_SalesQuotationItemSelectOptions \$select?;
 };
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesQuotationExpandOptions
+type PrecedingProcFlowDocOfA_SalesQuotationExpandOptions "to_SalesQuotation"[];
 
-// Unknown type: A_SalesQuotationItemTextOrderByOptions
+type A_SalesQuotationItemTextOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc")[];
 
-// Unknown type: A_SlsQtanItmSubsqntProcFlowOrderByOptions
+type A_SlsQtanItmSubsqntProcFlowOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentItem"|"SubsequentDocumentItem desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: A_SlsQtanItemRelatedObjectOrderByOptions
+type A_SlsQtanItemRelatedObjectOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"SDDocRelatedObjectSequenceNmbr"|"SDDocRelatedObjectSequenceNmbr desc"|"SDDocumentRelatedObjectType"|"SDDocumentRelatedObjectType desc"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectSystem desc"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference1 desc"|"SDDocRelatedObjectReference2"|"SDDocRelatedObjectReference2 desc")[];
 
 # Represents the Queries record for the operation: getSalesQuotationItemOfA_SlsQtanItemRelatedObject
 
@@ -1745,13 +1799,13 @@
     SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItemRelatedObjectExpandOptions
+type SalesQuotationItemOfA_SlsQtanItemRelatedObjectExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions
+type SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemPartnerExpandOptions
+type SalesQuotationItemOfA_SalesQuotationItemPartnerExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: A_SlsQtanPrecdgProcFlowOrderByOptions
+type A_SlsQtanPrecdgProcFlowOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SlsQtanItemRelatedObject
 
@@ -1762,11 +1816,11 @@
     SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanItemRelatedObjectExpandOptions
+type SalesQuotationOfA_SlsQtanItemRelatedObjectExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions
+type SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: PricingElementOfA_SalesQuotationSelectOptions
+type PricingElementOfA_SalesQuotationSelectOptions ("SalesQuotation"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesQuotation")[];
 
 
 type CollectionOfA_SlsQtanItmPrecdgProcFlow record {
@@ -1783,7 +1837,7 @@
     SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions
+type SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SalesQuotationItemPrcgElmnt
 
@@ -1813,18 +1867,18 @@
     A_SlsQtanItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsQtanItmPrecdgProcFlowOrderByOptions
+type A_SlsQtanItmPrecdgProcFlowOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentItem"|"PrecedingDocumentItem desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: A_SlsQtanItmPrecdgProcFlowExpandOptions
+type A_SlsQtanItmPrecdgProcFlowExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type A_SalesQuotationPartnerWrapper record {
     A_SalesQuotationPartner d?;
 };
 
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesQuotationItemExpandOptions
+type PrecedingProcFlowDocItemOfA_SalesQuotationItemExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: A_SlsQtanSubsqntProcFlowExpandOptions
+type A_SlsQtanSubsqntProcFlowExpandOptions "to_SalesQuotation"[];
 
 # Represents the Queries record for the operation: listA_SalesQuotationPrcgElmnts
 
@@ -1845,7 +1899,7 @@
     A_SalesQuotationPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationPrcgElmntOrderByOptions
+type A_SalesQuotationPrcgElmntOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 # Represents the Queries record for the operation: listTextsOfA_SalesQuotationItem
 
@@ -1875,9 +1929,9 @@
     A_SlsQtanSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemTextSelectOptions
+type SalesQuotationItemOfA_SalesQuotationItemTextSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: A_SalesQuotationItemPartnerExpandOptions
+type A_SalesQuotationItemPartnerExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 # Represents the Queries record for the operation: listPricingElementsOfA_SalesQuotation
 
@@ -1898,7 +1952,7 @@
     PricingElementOfA_SalesQuotationSelectOptions \$select?;
 };
 
-// Unknown type: PricingElementOfA_SalesQuotationOrderByOptions
+type PricingElementOfA_SalesQuotationOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 
 type CollectionOfA_SlsQtanItmPrecdgProcFlowWrapper record {
@@ -1916,9 +1970,9 @@
     A_SlsQtanItemRelatedObject[] results?;
 };
 
-// Unknown type: A_SalesQuotationPartnerOrderByOptions
+type A_SalesQuotationPartnerOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"PartnerFunction"|"PartnerFunction desc"|"PartnerFunctionInternalCode"|"PartnerFunctionInternalCode desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"ReferenceBusinessPartner"|"ReferenceBusinessPartner desc")[];
 
-// Unknown type: A_SalesQuotationSelectOptions
+type A_SalesQuotationSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type Modified\ A_SalesQuotationPrcgElmntType record {
@@ -1980,7 +2034,7 @@
     PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions
+type SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesQuotationPartners
 
@@ -2001,7 +2055,7 @@
     A_SalesQuotationPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesQuotationItemExpandOptions
+type SubsequentProcFlowDocItemOfA_SalesQuotationItemExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 # Represents the Queries record for the operation: listA_SlsQtanPrecdgProcFlows
 
@@ -2031,9 +2085,9 @@
     A_SlsQtanItemRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsQtanItemRelatedObjectExpandOptions
+type A_SlsQtanItemRelatedObjectExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: A_SlsQtanItemRelatedObjectSelectOptions
+type A_SlsQtanItemRelatedObjectSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"SDDocRelatedObjectSequenceNmbr"|"SDDocumentRelatedObjectType"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference2"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type A_SlsQtanItmPrecdgProcFlowWrapper record {
@@ -2059,7 +2113,7 @@
     string? TransactionCurrency?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanPrecdgProcFlowExpandOptions
+type SalesQuotationOfA_SlsQtanPrecdgProcFlowExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotationItemPartner
 
@@ -2070,7 +2124,7 @@
     A_SalesQuotationItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationItemPartnerSelectOptions
+type A_SalesQuotationItemPartnerSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SlsQtanSubsqntProcFlow
 
@@ -2081,15 +2135,15 @@
     SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanSubsqntProcFlowExpandOptions
+type SalesQuotationOfA_SlsQtanSubsqntProcFlowExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions
+type SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SalesQuotationOfA_SlsQtanItmPrecdgProcFlowExpandOptions
+type SalesQuotationOfA_SlsQtanItmPrecdgProcFlowExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesQuotationItemOrderByOptions
+type SubsequentProcFlowDocItemOfA_SalesQuotationItemOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentItem"|"SubsequentDocumentItem desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions
+type SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type CollectionOfA_SalesQuotationItemTextWrapper record {
@@ -2115,9 +2169,9 @@
     A_SalesQuotationItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationItemOrderByOptions
+type A_SalesQuotationItemOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"HigherLevelItem"|"HigherLevelItem desc"|"SalesQuotationItemCategory"|"SalesQuotationItemCategory desc"|"SalesQuotationItemText"|"SalesQuotationItemText desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"Material"|"Material desc"|"MaterialByCustomer"|"MaterialByCustomer desc"|"PricingReferenceMaterial"|"PricingReferenceMaterial desc"|"RequestedQuantity"|"RequestedQuantity desc"|"RequestedQuantityUnit"|"RequestedQuantityUnit desc"|"RequestedQuantitySAPUnit"|"RequestedQuantitySAPUnit desc"|"RequestedQuantityISOUnit"|"RequestedQuantityISOUnit desc"|"ItemOrderProbabilityInPercent"|"ItemOrderProbabilityInPercent desc"|"AlternativeToItem"|"AlternativeToItem desc"|"ItemGrossWeight"|"ItemGrossWeight desc"|"ItemNetWeight"|"ItemNetWeight desc"|"ItemWeightUnit"|"ItemWeightUnit desc"|"ItemWeightSAPUnit"|"ItemWeightSAPUnit desc"|"ItemWeightISOUnit"|"ItemWeightISOUnit desc"|"ItemVolume"|"ItemVolume desc"|"ItemVolumeUnit"|"ItemVolumeUnit desc"|"ItemVolumeSAPUnit"|"ItemVolumeSAPUnit desc"|"ItemVolumeISOUnit"|"ItemVolumeISOUnit desc"|"TransactionCurrency"|"TransactionCurrency desc"|"NetAmount"|"NetAmount desc"|"MaterialGroup"|"MaterialGroup desc"|"MaterialPricingGroup"|"MaterialPricingGroup desc"|"Batch"|"Batch desc"|"Plant"|"Plant desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"ProductTaxClassification1"|"ProductTaxClassification1 desc"|"ProductTaxClassification2"|"ProductTaxClassification2 desc"|"ProductTaxClassification3"|"ProductTaxClassification3 desc"|"ProductTaxClassification4"|"ProductTaxClassification4 desc"|"ProductTaxClassification5"|"ProductTaxClassification5 desc"|"ProductTaxClassification6"|"ProductTaxClassification6 desc"|"ProductTaxClassification7"|"ProductTaxClassification7 desc"|"ProductTaxClassification8"|"ProductTaxClassification8 desc"|"ProductTaxClassification9"|"ProductTaxClassification9 desc"|"SalesDocumentRjcnReason"|"SalesDocumentRjcnReason desc"|"WBSElement"|"WBSElement desc"|"ProfitCenter"|"ProfitCenter desc"|"ReferenceSDDocument"|"ReferenceSDDocument desc"|"ReferenceSDDocumentItem"|"ReferenceSDDocumentItem desc"|"SDProcessStatus"|"SDProcessStatus desc"|"Subtotal1Amount"|"Subtotal1Amount desc"|"Subtotal2Amount"|"Subtotal2Amount desc"|"Subtotal3Amount"|"Subtotal3Amount desc"|"Subtotal4Amount"|"Subtotal4Amount desc"|"Subtotal5Amount"|"Subtotal5Amount desc"|"Subtotal6Amount"|"Subtotal6Amount desc")[];
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemTextExpandOptions
+type SalesQuotationItemOfA_SalesQuotationItemTextExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: listSubsequentProcFlowDocsOfA_SalesQuotation
 
@@ -2138,7 +2192,7 @@
     SubsequentProcFlowDocOfA_SalesQuotationSelectOptions \$select?;
 };
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesQuotationOrderByOptions
+type SubsequentProcFlowDocOfA_SalesQuotationOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 # Represents the Queries record for the operation: getA_SlsQtanItmSubsqntProcFlow
 
@@ -2149,9 +2203,9 @@
     A_SlsQtanItmSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsQtanItmSubsqntProcFlowExpandOptions
+type A_SlsQtanItmSubsqntProcFlowExpandOptions ("to_SalesQuotation"|"to_SalesQuotationItem")[];
 
-// Unknown type: A_SlsQtanItmSubsqntProcFlowSelectOptions
+type A_SlsQtanItmSubsqntProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentItem"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 
 type A_SalesQuotationItemTextWrapper record {
@@ -2167,7 +2221,7 @@
     SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemPartnerExpandOptions
+type SalesQuotationOfA_SalesQuotationItemPartnerExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SlsQtanItemRelatedObjects
 
@@ -2192,6 +2246,7 @@
 
 type RejectApprovalRequestQueries record {
     # Value needs to be enclosed in single quotes
+    @constraint:String {maxLength: 11002, pattern: re `^'[^']*(''[^']*)*'$`}
     string SalesQuotation;
 };
 
@@ -2204,7 +2259,7 @@
     SalesQuotationOfA_SalesQuotationItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationItemExpandOptions
+type SalesQuotationOfA_SalesQuotationItemExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesQuotationItemPrcgElmnts
 
@@ -2265,7 +2320,7 @@
     SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemPrcgElmntExpandOptions
+type SalesQuotationItemOfA_SalesQuotationItemPrcgElmntExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesQuotationTexts
 
@@ -2286,7 +2341,7 @@
     A_SalesQuotationTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationTextOrderByOptions
+type A_SalesQuotationTextOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc")[];
 
 # Represents the Queries record for the operation: listPrecedingProcFlowDocsOfA_SalesQuotation
 
@@ -2307,9 +2362,9 @@
     PrecedingProcFlowDocOfA_SalesQuotationSelectOptions \$select?;
 };
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesQuotationOrderByOptions
+type PrecedingProcFlowDocOfA_SalesQuotationOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesQuotationSelectOptions
+type PrecedingProcFlowDocOfA_SalesQuotationSelectOptions ("SalesQuotation"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation")[];
 
 
 type A_SalesQuotationWrapper record {
@@ -2417,7 +2472,7 @@
     A_SlsQtanItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: PricingElementOfA_SalesQuotationItemOrderByOptions
+type PricingElementOfA_SalesQuotationItemOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 
 type CollectionOfA_SalesQuotationRelatedObjectWrapper record {
@@ -2458,7 +2513,7 @@
     SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowExpandOptions
+type SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowExpandOptions ("to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesQuotations
 
@@ -2479,7 +2534,7 @@
     A_SalesQuotationSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationExpandOptions
+type A_SalesQuotationExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesQuotation
 
@@ -2499,7 +2554,7 @@
     SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions
+type SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesQuotationOfA_SlsQtanPrecdgProcFlow
 
@@ -2510,7 +2565,7 @@
     SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions
+type SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions ("SalesQuotation"|"SalesQuotationType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesQuotationDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"CustomerPriceGroup"|"PriceListType"|"PaymentMethod"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"SalesQuotationApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesQuotationItemPartners
 
@@ -2531,7 +2586,7 @@
     A_SalesQuotationItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesQuotationItemPartnerOrderByOptions
+type A_SalesQuotationItemPartnerOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"SalesQuotationItem"|"SalesQuotationItem desc"|"PartnerFunction"|"PartnerFunction desc"|"PartnerFunctionInternalCode"|"PartnerFunctionInternalCode desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"ReferenceBusinessPartner"|"ReferenceBusinessPartner desc")[];
 
 # Represents the Queries record for the operation: listPartnersOfA_SalesQuotationItem
 
@@ -2611,7 +2666,7 @@
     SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationOfA_SalesQuotationRelatedObjectExpandOptions
+type SalesQuotationOfA_SalesQuotationRelatedObjectExpandOptions ("to_Item"|"to_Partner"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type Modified\ A_SalesQuotationItemPrcgElmntType record {
@@ -2657,7 +2712,7 @@
     SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions
+type SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"HigherLevelItem"|"SalesQuotationItemCategory"|"SalesQuotationItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"PricingReferenceMaterial"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"MaterialPricingGroup"|"Batch"|"Plant"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"SalesDocumentRjcnReason"|"WBSElement"|"ProfitCenter"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesQuotation"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type CollectionOfA_SalesQuotationItemWrapper record {
@@ -2712,7 +2767,7 @@
     SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsQtanSubsqntProcFlowOrderByOptions
+type A_SlsQtanSubsqntProcFlowOrderByOptions ("SalesQuotation"|"SalesQuotation desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 
 type CollectionOfA_SalesQuotationTextWrapper record {
@@ -2763,7 +2818,7 @@
     CollectionOfA_SlsQtanItmSubsqntProcFlow d?;
 };
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesQuotationItemSelectOptions
+type SubsequentProcFlowDocItemOfA_SalesQuotationItemSelectOptions ("SalesQuotation"|"SalesQuotationItem"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentItem"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"StatusCode"|"SDDocumentStatusDesc"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesQuotation"|"to_SalesQuotationItem")[];
 
 # Represents the Queries record for the operation: listSubsequentProcFlowDocItemsOfA_SalesQuotationItem
 
@@ -2788,6 +2843,7 @@
 
 type ReleaseApprovalRequestQueries record {
     # Value needs to be enclosed in single quotes
+    @constraint:String {maxLength: 11002, pattern: re `^'[^']*(''[^']*)*'$`}
     string SalesQuotation;
 };
 
@@ -2892,243 +2948,243 @@
 
     # Reads the header of a specific sales quotation.
     # 
-    remote function getA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, A_SalesQuotationExpandOptions \$expand = [], A_SalesQuotationSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, A_SalesQuotationExpandOptions \$expand = [], A_SalesQuotationSelectOptions \$select = [], GetA_SalesQuotationQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads a specific sales quotation item.
     # 
-    remote function getA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, A_SalesQuotationItemExpandOptions \$expand = [], A_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationItemQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, A_SalesQuotationItemExpandOptions \$expand = [], A_SalesQuotationItemSelectOptions \$select = [], GetA_SalesQuotationItemQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the item partners of a specific item and with a specific partner function in a specific sales quotation.
     # 
-    remote function getA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesQuotationItemPartnerExpandOptions \$expand = [], A_SalesQuotationItemPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationItemPartnerWrapper|error;
+    remote function getA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesQuotationItemPartnerExpandOptions \$expand = [], A_SalesQuotationItemPartnerSelectOptions \$select = [], GetA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationItemPartnerWrapper|error;
 
     # Reads the pricing element of a specific sales quotation item.
     # 
-    remote function getA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], A_SalesQuotationItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationItemPrcgElmntWrapper|error;
+    remote function getA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], A_SalesQuotationItemPrcgElmntSelectOptions \$select = [], GetA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationItemPrcgElmntWrapper|error;
 
     # Reads a specific item text.
     # 
-    remote function getA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesQuotationItemTextExpandOptions \$expand = [], A_SalesQuotationItemTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationItemTextWrapper|error;
+    remote function getA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesQuotationItemTextExpandOptions \$expand = [], A_SalesQuotationItemTextSelectOptions \$select = [], GetA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationItemTextWrapper|error;
 
     # Reads the header partners of a specific sales quotation and with a specific partner function.
     # 
-    remote function getA_SalesQuotationPartner(string SalesQuotation, string PartnerFunction, map<string|string[]> headers = {}, A_SalesQuotationPartnerExpandOptions \$expand = [], A_SalesQuotationPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationPartnerQueries queries) returns A_SalesQuotationPartnerWrapper|error;
+    remote function getA_SalesQuotationPartner(string SalesQuotation, string PartnerFunction, map<string|string[]> headers = {}, A_SalesQuotationPartnerExpandOptions \$expand = [], A_SalesQuotationPartnerSelectOptions \$select = [], GetA_SalesQuotationPartnerQueries queries) returns A_SalesQuotationPartnerWrapper|error;
 
     # Reads the header pricing element for a specific sales quotation.
     # 
-    remote function getA_SalesQuotationPrcgElmnt(string SalesQuotation, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesQuotationPrcgElmntExpandOptions \$expand = [], A_SalesQuotationPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationPrcgElmntQueries queries) returns A_SalesQuotationPrcgElmntWrapper|error;
+    remote function getA_SalesQuotationPrcgElmnt(string SalesQuotation, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesQuotationPrcgElmntExpandOptions \$expand = [], A_SalesQuotationPrcgElmntSelectOptions \$select = [], GetA_SalesQuotationPrcgElmntQueries queries) returns A_SalesQuotationPrcgElmntWrapper|error;
 
     # Reads a related object of a sales quotation.
     # 
-    remote function getA_SalesQuotationRelatedObject(string SalesQuotation, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesQuotationRelatedObjectExpandOptions \$expand = [], A_SalesQuotationRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationRelatedObjectQueries queries) returns A_SalesQuotationRelatedObjectWrapper|error;
+    remote function getA_SalesQuotationRelatedObject(string SalesQuotation, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesQuotationRelatedObjectExpandOptions \$expand = [], A_SalesQuotationRelatedObjectSelectOptions \$select = [], GetA_SalesQuotationRelatedObjectQueries queries) returns A_SalesQuotationRelatedObjectWrapper|error;
 
     # Reads the header texts of a specific sales quotation.
     # 
-    remote function getA_SalesQuotationText(string SalesQuotation, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesQuotationTextExpandOptions \$expand = [], A_SalesQuotationTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesQuotationTextQueries queries) returns A_SalesQuotationTextWrapper|error;
+    remote function getA_SalesQuotationText(string SalesQuotation, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesQuotationTextExpandOptions \$expand = [], A_SalesQuotationTextSelectOptions \$select = [], GetA_SalesQuotationTextQueries queries) returns A_SalesQuotationTextWrapper|error;
 
     # Reads a related object from a sales quotation item.
     # 
-    remote function getA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SlsQtanItemRelatedObjectExpandOptions \$expand = [], A_SlsQtanItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetA_SlsQtanItemRelatedObjectQueries queries) returns A_SlsQtanItemRelatedObjectWrapper|error;
+    remote function getA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SlsQtanItemRelatedObjectExpandOptions \$expand = [], A_SlsQtanItemRelatedObjectSelectOptions \$select = [], GetA_SlsQtanItemRelatedObjectQueries queries) returns A_SlsQtanItemRelatedObjectWrapper|error;
 
     # Reads a preceding item of a sales quotation item.
     # 
-    remote function getA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], A_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SlsQtanItmPrecdgProcFlowWrapper|error;
+    remote function getA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], A_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], GetA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SlsQtanItmPrecdgProcFlowWrapper|error;
 
     # Reads a subsequent item of a sales quotation item.
     # 
-    remote function getA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], A_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SlsQtanItmSubsqntProcFlowWrapper|error;
+    remote function getA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], A_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], GetA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SlsQtanItmSubsqntProcFlowWrapper|error;
 
     # Reads a preceding document of a sales quotation.
     # 
-    remote function getA_SlsQtanPrecdgProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], A_SlsQtanPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SlsQtanPrecdgProcFlowQueries queries) returns A_SlsQtanPrecdgProcFlowWrapper|error;
+    remote function getA_SlsQtanPrecdgProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], A_SlsQtanPrecdgProcFlowSelectOptions \$select = [], GetA_SlsQtanPrecdgProcFlowQueries queries) returns A_SlsQtanPrecdgProcFlowWrapper|error;
 
     # Reads a subsequent document of a sales quotation.
     # 
-    remote function getA_SlsQtanSubsqntProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], A_SlsQtanSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SlsQtanSubsqntProcFlowQueries queries) returns A_SlsQtanSubsqntProcFlowWrapper|error;
+    remote function getA_SlsQtanSubsqntProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], A_SlsQtanSubsqntProcFlowSelectOptions \$select = [], GetA_SlsQtanSubsqntProcFlowQueries queries) returns A_SlsQtanSubsqntProcFlowWrapper|error;
 
     # Reads the sales quotation item for a specific partner function of a sales quotation item.
     # 
-    remote function getSalesQuotationItemOfA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemPartnerExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemPartnerExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions \$select = [], GetSalesQuotationItemOfA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation item for a specific pricing element.
     # 
-    remote function getSalesQuotationItemOfA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemPrcgElmntSelectOptions \$select = [], GetSalesQuotationItemOfA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation item for a specific item text.
     # 
-    remote function getSalesQuotationItemOfA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemTextExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemTextSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SalesQuotationItemTextExpandOptions \$expand = [], SalesQuotationItemOfA_SalesQuotationItemTextSelectOptions \$select = [], GetSalesQuotationItemOfA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation item for a related object of a sales quotation item.
     # 
-    remote function getSalesQuotationItemOfA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItemRelatedObjectExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SlsQtanItemRelatedObjectQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItemRelatedObjectExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItemRelatedObjectSelectOptions \$select = [], GetSalesQuotationItemOfA_SlsQtanItemRelatedObjectQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation item for a preceding item of a sales quotation item.
     # 
-    remote function getSalesQuotationItemOfA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], GetSalesQuotationItemOfA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation item for a subsequent item of a sales quotation item.
     # 
-    remote function getSalesQuotationItemOfA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SalesQuotationItemWrapper|error;
+    remote function getSalesQuotationItemOfA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], GetSalesQuotationItemOfA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SalesQuotationItemWrapper|error;
 
     # Reads the sales quotation header for a specific item.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationItemQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationItemQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific partner function of a sales quotation item.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemPartnerExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationItemPartner(string SalesQuotation, string SalesQuotationItem, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemPartnerExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemPartnerSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationItemPartnerQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific pricing element.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationItemPrcgElmnt(string SalesQuotation, string SalesQuotationItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemPrcgElmntSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationItemPrcgElmntQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific text of a sales quotation item.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemTextExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemTextSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationItemText(string SalesQuotation, string SalesQuotationItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationItemTextExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationItemTextSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationItemTextQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific header partner.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationPartner(string SalesQuotation, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationPartnerExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationPartnerQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationPartner(string SalesQuotation, string PartnerFunction, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationPartnerExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationPartnerSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationPartnerQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific pricing element.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationPrcgElmnt(string SalesQuotation, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationPrcgElmntExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationPrcgElmntQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationPrcgElmnt(string SalesQuotation, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationPrcgElmntExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationPrcgElmntSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationPrcgElmntQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a related object of a sales quotation.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationRelatedObject(string SalesQuotation, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationRelatedObjectExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationRelatedObjectQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationRelatedObject(string SalesQuotation, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationRelatedObjectExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationRelatedObjectSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationRelatedObjectQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a specific header text.
     # 
-    remote function getSalesQuotationOfA_SalesQuotationText(string SalesQuotation, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationTextExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationTextSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SalesQuotationTextQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SalesQuotationText(string SalesQuotation, string Language, string LongTextID, map<string|string[]> headers = {}, SalesQuotationOfA_SalesQuotationTextExpandOptions \$expand = [], SalesQuotationOfA_SalesQuotationTextSelectOptions \$select = [], GetSalesQuotationOfA_SalesQuotationTextQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a related object of a sales quotation item.
     # 
-    remote function getSalesQuotationOfA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItemRelatedObjectExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SlsQtanItemRelatedObjectQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SlsQtanItemRelatedObject(string SalesQuotation, string SalesQuotationItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItemRelatedObjectExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItemRelatedObjectSelectOptions \$select = [], GetSalesQuotationOfA_SlsQtanItemRelatedObjectQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a preceding item of a sales quotation item.
     # 
-    remote function getSalesQuotationOfA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SlsQtanItmPrecdgProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], GetSalesQuotationOfA_SlsQtanItmPrecdgProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a subsequent item of a sales quotation item.
     # 
-    remote function getSalesQuotationOfA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SlsQtanItmSubsqntProcFlow(string SalesQuotation, string SalesQuotationItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], GetSalesQuotationOfA_SlsQtanItmSubsqntProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a preceding document of a sales quotation.
     # 
-    remote function getSalesQuotationOfA_SlsQtanPrecdgProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SlsQtanPrecdgProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SlsQtanPrecdgProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanPrecdgProcFlowSelectOptions \$select = [], GetSalesQuotationOfA_SlsQtanPrecdgProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the sales quotation header for a subsequent document of a sales quotation.
     # 
-    remote function getSalesQuotationOfA_SlsQtanSubsqntProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesQuotationOfA_SlsQtanSubsqntProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
+    remote function getSalesQuotationOfA_SlsQtanSubsqntProcFlow(string SalesQuotation, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesQuotationOfA_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], SalesQuotationOfA_SlsQtanSubsqntProcFlowSelectOptions \$select = [], GetSalesQuotationOfA_SlsQtanSubsqntProcFlowQueries queries) returns A_SalesQuotationWrapper|error;
 
     # Reads the item partners for all sales quotations.
     # 
-    remote function listA_SalesQuotationItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPartnerOrderByOptions \$orderby = [], A_SalesQuotationItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationItemPartnersQueries queries) returns CollectionOfA_SalesQuotationItemPartnerWrapper|error;
+    remote function listA_SalesQuotationItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPartnerOrderByOptions \$orderby = [], A_SalesQuotationItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPartnerSelectOptions \$select = [], ListA_SalesQuotationItemPartnersQueries queries) returns CollectionOfA_SalesQuotationItemPartnerWrapper|error;
 
     # Reads the item pricing elements of all sales quotations.
     # 
-    remote function listA_SalesQuotationItemPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPrcgElmntOrderByOptions \$orderby = [], A_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationItemPrcgElmntsQueries queries) returns CollectionOfA_SalesQuotationItemPrcgElmntWrapper|error;
+    remote function listA_SalesQuotationItemPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPrcgElmntOrderByOptions \$orderby = [], A_SalesQuotationItemPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPrcgElmntSelectOptions \$select = [], ListA_SalesQuotationItemPrcgElmntsQueries queries) returns CollectionOfA_SalesQuotationItemPrcgElmntWrapper|error;
 
     # Reads item texts of all sales quotations.
     # 
-    remote function listA_SalesQuotationItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemTextOrderByOptions \$orderby = [], A_SalesQuotationItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationItemTextsQueries queries) returns CollectionOfA_SalesQuotationItemTextWrapper|error;
+    remote function listA_SalesQuotationItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemTextOrderByOptions \$orderby = [], A_SalesQuotationItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemTextSelectOptions \$select = [], ListA_SalesQuotationItemTextsQueries queries) returns CollectionOfA_SalesQuotationItemTextWrapper|error;
 
     # Reads all sales quotation items.
     # 
-    remote function listA_SalesQuotationItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemOrderByOptions \$orderby = [], A_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationItemsQueries queries) returns CollectionOfA_SalesQuotationItemWrapper|error;
+    remote function listA_SalesQuotationItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemOrderByOptions \$orderby = [], A_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemSelectOptions \$select = [], ListA_SalesQuotationItemsQueries queries) returns CollectionOfA_SalesQuotationItemWrapper|error;
 
     # Reads the header partners of all sales quotations.
     # 
-    remote function listA_SalesQuotationPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPartnerOrderByOptions \$orderby = [], A_SalesQuotationPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationPartnersQueries queries) returns CollectionOfA_SalesQuotationPartnerWrapper|error;
+    remote function listA_SalesQuotationPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPartnerOrderByOptions \$orderby = [], A_SalesQuotationPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPartnerSelectOptions \$select = [], ListA_SalesQuotationPartnersQueries queries) returns CollectionOfA_SalesQuotationPartnerWrapper|error;
 
     # Reads the header pricing elements of all sales quotations.
     # 
-    remote function listA_SalesQuotationPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPrcgElmntOrderByOptions \$orderby = [], A_SalesQuotationPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPrcgElmntSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationPrcgElmntsQueries queries) returns CollectionOfA_SalesQuotationPrcgElmntWrapper|error;
+    remote function listA_SalesQuotationPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPrcgElmntOrderByOptions \$orderby = [], A_SalesQuotationPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPrcgElmntSelectOptions \$select = [], ListA_SalesQuotationPrcgElmntsQueries queries) returns CollectionOfA_SalesQuotationPrcgElmntWrapper|error;
 
     # Reads the related objects of all sales quotations.
     # 
-    remote function listA_SalesQuotationRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationRelatedObjectOrderByOptions \$orderby = [], A_SalesQuotationRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationRelatedObjectsQueries queries) returns CollectionOfA_SalesQuotationRelatedObjectWrapper|error;
+    remote function listA_SalesQuotationRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationRelatedObjectOrderByOptions \$orderby = [], A_SalesQuotationRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationRelatedObjectSelectOptions \$select = [], ListA_SalesQuotationRelatedObjectsQueries queries) returns CollectionOfA_SalesQuotationRelatedObjectWrapper|error;
 
     # Reads the header texts of all sales quotations.
     # 
-    remote function listA_SalesQuotationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationTextOrderByOptions \$orderby = [], A_SalesQuotationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationTextsQueries queries) returns CollectionOfA_SalesQuotationTextWrapper|error;
+    remote function listA_SalesQuotationTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationTextOrderByOptions \$orderby = [], A_SalesQuotationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationTextSelectOptions \$select = [], ListA_SalesQuotationTextsQueries queries) returns CollectionOfA_SalesQuotationTextWrapper|error;
 
     # Reads all sales quotation headers.
     # 
-    remote function listA_SalesQuotations(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationOrderByOptions \$orderby = [], A_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationSelectOptions \$select = [], anydata Additional Values, ListA_SalesQuotationsQueries queries) returns CollectionOfA_SalesQuotationWrapper|error;
+    remote function listA_SalesQuotations(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationOrderByOptions \$orderby = [], A_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationSelectOptions \$select = [], ListA_SalesQuotationsQueries queries) returns CollectionOfA_SalesQuotationWrapper|error;
 
     # Reads related objects from all sales quotation items.
     # 
-    remote function listA_SlsQtanItemRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItemRelatedObjectOrderByOptions \$orderby = [], A_SlsQtanItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListA_SlsQtanItemRelatedObjectsQueries queries) returns CollectionOfA_SlsQtanItemRelatedObjectWrapper|error;
+    remote function listA_SlsQtanItemRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItemRelatedObjectOrderByOptions \$orderby = [], A_SlsQtanItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItemRelatedObjectSelectOptions \$select = [], ListA_SlsQtanItemRelatedObjectsQueries queries) returns CollectionOfA_SlsQtanItemRelatedObjectWrapper|error;
 
     # Reads the preceding items of all sales quotation items.
     # 
-    remote function listA_SlsQtanItmPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItmPrecdgProcFlowOrderByOptions \$orderby = [], A_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SlsQtanItmPrecdgProcFlowsQueries queries) returns CollectionOfA_SlsQtanItmPrecdgProcFlowWrapper|error;
+    remote function listA_SlsQtanItmPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItmPrecdgProcFlowOrderByOptions \$orderby = [], A_SlsQtanItmPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItmPrecdgProcFlowSelectOptions \$select = [], ListA_SlsQtanItmPrecdgProcFlowsQueries queries) returns CollectionOfA_SlsQtanItmPrecdgProcFlowWrapper|error;
 
     # Reads the subsequent items of all sales quotation items.
     # 
-    remote function listA_SlsQtanItmSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItmSubsqntProcFlowOrderByOptions \$orderby = [], A_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SlsQtanItmSubsqntProcFlowsQueries queries) returns CollectionOfA_SlsQtanItmSubsqntProcFlowWrapper|error;
+    remote function listA_SlsQtanItmSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanItmSubsqntProcFlowOrderByOptions \$orderby = [], A_SlsQtanItmSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanItmSubsqntProcFlowSelectOptions \$select = [], ListA_SlsQtanItmSubsqntProcFlowsQueries queries) returns CollectionOfA_SlsQtanItmSubsqntProcFlowWrapper|error;
 
     # Reads the preceding documents of all sales quotations.
     # 
-    remote function listA_SlsQtanPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanPrecdgProcFlowOrderByOptions \$orderby = [], A_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SlsQtanPrecdgProcFlowsQueries queries) returns CollectionOfA_SlsQtanPrecdgProcFlowWrapper|error;
+    remote function listA_SlsQtanPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanPrecdgProcFlowOrderByOptions \$orderby = [], A_SlsQtanPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanPrecdgProcFlowSelectOptions \$select = [], ListA_SlsQtanPrecdgProcFlowsQueries queries) returns CollectionOfA_SlsQtanPrecdgProcFlowWrapper|error;
 
     # Reads the subsequent documents of all sales quotations.
     # 
-    remote function listA_SlsQtanSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanSubsqntProcFlowOrderByOptions \$orderby = [], A_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SlsQtanSubsqntProcFlowsQueries queries) returns CollectionOfA_SlsQtanSubsqntProcFlowWrapper|error;
+    remote function listA_SlsQtanSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsQtanSubsqntProcFlowOrderByOptions \$orderby = [], A_SlsQtanSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsQtanSubsqntProcFlowSelectOptions \$select = [], ListA_SlsQtanSubsqntProcFlowsQueries queries) returns CollectionOfA_SlsQtanSubsqntProcFlowWrapper|error;
 
     # Reads all items of a specific sales quotation.
     # 
-    remote function listItemsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemOrderByOptions \$orderby = [], A_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListItemsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationItemWrapper|error;
+    remote function listItemsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemOrderByOptions \$orderby = [], A_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemSelectOptions \$select = [], ListItemsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationItemWrapper|error;
 
     # Reads the header partners of a specific sales quotation.
     # 
-    remote function listPartnersOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPartnerOrderByOptions \$orderby = [], A_SalesQuotationPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationPartnerWrapper|error;
+    remote function listPartnersOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationPartnerOrderByOptions \$orderby = [], A_SalesQuotationPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationPartnerSelectOptions \$select = [], ListPartnersOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationPartnerWrapper|error;
 
     # Reads the item partners of a specific sales quotation item.
     # 
-    remote function listPartnersOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPartnerOrderByOptions \$orderby = [], A_SalesQuotationItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemPartnerWrapper|error;
+    remote function listPartnersOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemPartnerOrderByOptions \$orderby = [], A_SalesQuotationItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemPartnerSelectOptions \$select = [], ListPartnersOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemPartnerWrapper|error;
 
     # Reads the preceding items of a sales quotation item.
     # 
-    remote function listPrecedingProcFlowDocItemsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocItemOfA_SalesQuotationItemOrderByOptions \$orderby = [], PrecedingProcFlowDocItemOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListPrecedingProcFlowDocItemsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItmPrecdgProcFlowWrapper|error;
+    remote function listPrecedingProcFlowDocItemsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocItemOfA_SalesQuotationItemOrderByOptions \$orderby = [], PrecedingProcFlowDocItemOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocItemOfA_SalesQuotationItemSelectOptions \$select = [], ListPrecedingProcFlowDocItemsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItmPrecdgProcFlowWrapper|error;
 
     # Reads the preceding documents of a sales quotation.
     # 
-    remote function listPrecedingProcFlowDocsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocOfA_SalesQuotationOrderByOptions \$orderby = [], PrecedingProcFlowDocOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocOfA_SalesQuotationSelectOptions \$select = [], anydata Additional Values, ListPrecedingProcFlowDocsOfA_SalesQuotationQueries queries) returns CollectionOfA_SlsQtanPrecdgProcFlowWrapper|error;
+    remote function listPrecedingProcFlowDocsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocOfA_SalesQuotationOrderByOptions \$orderby = [], PrecedingProcFlowDocOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocOfA_SalesQuotationSelectOptions \$select = [], ListPrecedingProcFlowDocsOfA_SalesQuotationQueries queries) returns CollectionOfA_SlsQtanPrecdgProcFlowWrapper|error;
 
     # Reads the header pricing element of a specific sales quotation.
     # 
-    remote function listPricingElementsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesQuotationOrderByOptions \$orderby = [], PricingElementOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesQuotationSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationPrcgElmntWrapper|error;
+    remote function listPricingElementsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesQuotationOrderByOptions \$orderby = [], PricingElementOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesQuotationSelectOptions \$select = [], ListPricingElementsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationPrcgElmntWrapper|error;
 
     # Reads the pricing element of a specific sales quotation item.
     # 
-    remote function listPricingElementsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesQuotationItemOrderByOptions \$orderby = [], PricingElementOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemPrcgElmntWrapper|error;
+    remote function listPricingElementsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesQuotationItemOrderByOptions \$orderby = [], PricingElementOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesQuotationItemSelectOptions \$select = [], ListPricingElementsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemPrcgElmntWrapper|error;
 
     # Reads the related objects of a sales quotation.
     # 
-    remote function listRelatedObjectsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationRelatedObjectOrderByOptions \$orderby = [], A_SalesQuotationRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListRelatedObjectsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationRelatedObjectWrapper|error;
+    remote function listRelatedObjectsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationRelatedObjectOrderByOptions \$orderby = [], A_SalesQuotationRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationRelatedObjectSelectOptions \$select = [], ListRelatedObjectsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationRelatedObjectWrapper|error;
 
     # Reads the related objects of a sales quotation item.
     # 
-    remote function listRelatedObjectsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", RelatedObjectOfA_SalesQuotationItemOrderByOptions \$orderby = [], RelatedObjectOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", RelatedObjectOfA_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListRelatedObjectsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItemRelatedObjectWrapper|error;
+    remote function listRelatedObjectsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", RelatedObjectOfA_SalesQuotationItemOrderByOptions \$orderby = [], RelatedObjectOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", RelatedObjectOfA_SalesQuotationItemSelectOptions \$select = [], ListRelatedObjectsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItemRelatedObjectWrapper|error;
 
     # Reads the subsequent items of a sales quotation item.
     # 
-    remote function listSubsequentProcFlowDocItemsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocItemOfA_SalesQuotationItemOrderByOptions \$orderby = [], SubsequentProcFlowDocItemOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocItemOfA_SalesQuotationItemSelectOptions \$select = [], anydata Additional Values, ListSubsequentProcFlowDocItemsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItmSubsqntProcFlowWrapper|error;
+    remote function listSubsequentProcFlowDocItemsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocItemOfA_SalesQuotationItemOrderByOptions \$orderby = [], SubsequentProcFlowDocItemOfA_SalesQuotationItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocItemOfA_SalesQuotationItemSelectOptions \$select = [], ListSubsequentProcFlowDocItemsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SlsQtanItmSubsqntProcFlowWrapper|error;
 
     # Reads the subsequent documents of a sales quotation.
     # 
-    remote function listSubsequentProcFlowDocsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocOfA_SalesQuotationOrderByOptions \$orderby = [], SubsequentProcFlowDocOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocOfA_SalesQuotationSelectOptions \$select = [], anydata Additional Values, ListSubsequentProcFlowDocsOfA_SalesQuotationQueries queries) returns CollectionOfA_SlsQtanSubsqntProcFlowWrapper|error;
+    remote function listSubsequentProcFlowDocsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocOfA_SalesQuotationOrderByOptions \$orderby = [], SubsequentProcFlowDocOfA_SalesQuotationExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocOfA_SalesQuotationSelectOptions \$select = [], ListSubsequentProcFlowDocsOfA_SalesQuotationQueries queries) returns CollectionOfA_SlsQtanSubsqntProcFlowWrapper|error;
 
     # Reads the header texts of a specific sales quotation.
     # 
-    remote function listTextsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationTextOrderByOptions \$orderby = [], A_SalesQuotationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationTextWrapper|error;
+    remote function listTextsOfA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationTextOrderByOptions \$orderby = [], A_SalesQuotationTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationTextSelectOptions \$select = [], ListTextsOfA_SalesQuotationQueries queries) returns CollectionOfA_SalesQuotationTextWrapper|error;
 
     # Reads the text of a specific sales quotation item.
     # 
-    remote function listTextsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemTextOrderByOptions \$orderby = [], A_SalesQuotationItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemTextWrapper|error;
+    remote function listTextsOfA_SalesQuotationItem(string SalesQuotation, string SalesQuotationItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesQuotationItemTextOrderByOptions \$orderby = [], A_SalesQuotationItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesQuotationItemTextSelectOptions \$select = [], ListTextsOfA_SalesQuotationItemQueries queries) returns CollectionOfA_SalesQuotationItemTextWrapper|error;
 
     # Updates a specific sales quotation.
     # 
@@ -3168,9 +3224,9 @@
 
     # Invoke action rejectApprovalRequest
     # 
-    remote function rejectApprovalRequest(map<string|string[]> headers = {}, string SalesQuotation = "", anydata Additional Values, RejectApprovalRequestQueries queries) returns FunctionResult_2|error;
+    remote function rejectApprovalRequest(map<string|string[]> headers = {}, string SalesQuotation = "", RejectApprovalRequestQueries queries) returns FunctionResult_2|error;
 
     # Invoke action releaseApprovalRequest
     # 
-    remote function releaseApprovalRequest(map<string|string[]> headers = {}, string SalesQuotation = "", anydata Additional Values, ReleaseApprovalRequestQueries queries) returns FunctionResult_1|error;
+    remote function releaseApprovalRequest(map<string|string[]> headers = {}, string SalesQuotation = "", ReleaseApprovalRequestQueries queries) returns FunctionResult_1|error;
 }
`````

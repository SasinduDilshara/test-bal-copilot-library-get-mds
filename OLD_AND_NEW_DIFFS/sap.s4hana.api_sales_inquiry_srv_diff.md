# sap.s4hana.api_sales_inquiry_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sales_inquiry_srv` |
| **Old file** | `sap.s4hana.api_sales_inquiry_srv/old/ballerinax_sap.s4hana.api_sales_inquiry_srv.bal.txt` |
| **New file** | `sap.s4hana.api_sales_inquiry_srv/new/ballerinax_sap.s4hana.api_sales_inquiry_srv.bal.txt` |
| **Old lines** | 1131 |
| **New lines** | 1149 |
| **Lines added** | 82 |
| **Lines removed** | 64 |
| **Hunks** | 26 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 39 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (39)

- `type A_SalesInquiryExpandOptions`
- `type A_SalesInquiryItemExpandOptions`
- `type A_SalesInquiryItemOrderByOptions`
- `type A_SalesInquiryItemPartnerExpandOptions`
- `type A_SalesInquiryItemPartnerOrderByOptions`
- `type A_SalesInquiryItemPartnerSelectOptions`
- `type A_SalesInquiryItemPrcgElmntExpandOptions`
- `type A_SalesInquiryItemPrcgElmntOrderByOptions`
- `type A_SalesInquiryItemPrcgElmntSelectOptions`
- `type A_SalesInquiryItemSelectOptions`
- `type A_SalesInquiryOrderByOptions`
- `type A_SalesInquiryPartnerExpandOptions`
- `type A_SalesInquiryPartnerOrderByOptions`
- `type A_SalesInquiryPartnerSelectOptions`
- `type A_SalesInquiryPrcgElmntExpandOptions`
- `type A_SalesInquiryPrcgElmntOrderByOptions`
- `type A_SalesInquiryPrcgElmntSelectOptions`
- `type A_SalesInquirySelectOptions`
- `type PricingElementOfA_SalesInquiryExpandOptions`
- `type PricingElementOfA_SalesInquiryItemExpandOptions`
- `type PricingElementOfA_SalesInquiryItemOrderByOptions`
- `type PricingElementOfA_SalesInquiryItemSelectOptions`
- `type PricingElementOfA_SalesInquiryOrderByOptions`
- `type PricingElementOfA_SalesInquirySelectOptions`
- `type SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions`
- `type SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions`
- `type SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions`
- `type SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions`
- `type SalesInquiryOfA_SalesInquiryItemExpandOptions`
- `type SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions`
- `type SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions`
- `type SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions`
- `type SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions`
- `type SalesInquiryOfA_SalesInquiryItemSelectOptions`
- `type SalesInquiryOfA_SalesInquiryPartnerExpandOptions`
- `type SalesInquiryOfA_SalesInquiryPartnerSelectOptions`
- `type SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions`
- `type SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 122–132 | 122–136 | Types | +4 | −0 |
| 2 | 210–215 | 214–220 | Types | +1 | −0 |
| 3 | 278–284 | 283–291 | Types | +2 | −0 |
| 4 | 339–347 | 346–357 | Types | +3 | −0 |
| 5 | 367–373 | 377–385 | Types | +2 | −0 |
| 6 | 386–394 | 398–409 | Types | +3 | −0 |
| 7 | 488–500 | 503–515 | Types | +4 | −4 |
| 8 | 507–515 | 522–531 | Types | +3 | −2 |
| 9 | 520–534 | 536–550 | Types | +5 | −5 |
| 10 | 549–565 | 565–581 | Types | +6 | −6 |
| 11 | 589–599 | 605–615 | Types | +3 | −3 |
| 12 | 616–621 | 632–638 | Types | +1 | −0 |
| 13 | 670–679 | 687–697 | Types | +2 | −1 |
| 14 | 695–705 | 713–723 | Types | +3 | −3 |
| 15 | 720–726 | 738–744 | Types | +1 | −1 |
| 16 | 731–739 | 749–757 | Types | +2 | −2 |
| 17 | 749–757 | 767–775 | Types | +2 | −2 |
| 18 | 772–780 | 790–798 | Types | +2 | −2 |
| 19 | 796–802 | 814–820 | Types | +1 | −1 |
| 20 | 822–828 | 840–846 | Types | +1 | −1 |
| 21 | 844–850 | 862–868 | Types | +1 | −1 |
| 22 | 874–882 | 892–900 | Types | +2 | −2 |
| 23 | 887–895 | 905–913 | Types | +2 | −2 |
| 24 | 919–925 | 937–943 | Types | +1 | −1 |
| 25 | 1011–1017 | 1029–1035 | Types | +1 | −1 |
| 26 | 1031–1129 | 1049–1147 | Client | +24 | −24 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sales_inquiry_srv/old/ballerinax_sap.s4hana.api_sales_inquiry_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sales_inquiry_srv/new/ballerinax_sap.s4hana.api_sales_inquiry_srv.bal.txt	2026-08-12 13:19:19
@@ -122,11 +122,15 @@
 
 
 type A_SalesInquiryItemPrcgElmnt record {
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
     # Condition item number
+    @constraint:String {maxLength: 6}
     string SalesInquiryItem?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionApplication?;
     string? ConditionType?;
@@ -210,6 +214,7 @@
 
 
 type A_SalesInquiry record {
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
     string? SalesInquiryType?;
     string? SalesOrganization?;
@@ -278,7 +283,9 @@
 
 
 type A_SalesInquiryItem record {
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
+    @constraint:String {maxLength: 6}
     string SalesInquiryItem?;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -339,9 +346,12 @@
 
 type A_SalesInquiryItemPartner record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
     # Item number of the SD document
+    @constraint:String {maxLength: 6}
     string SalesInquiryItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -367,7 +377,9 @@
 
 type A_SalesInquiryPartner record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Customer Number
     string? Customer?;
@@ -386,9 +398,12 @@
 
 
 type A_SalesInquiryPrcgElmnt record {
+    @constraint:String {maxLength: 10}
     string SalesInquiry?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionApplication?;
     string? ConditionType?;
@@ -488,13 +503,13 @@
     A_SalesInquiryItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryItemPartnerOrderByOptions
+type A_SalesInquiryItemPartnerOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"SalesInquiryItem"|"SalesInquiryItem desc"|"PartnerFunction"|"PartnerFunction desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc")[];
 
-// Unknown type: A_SalesInquiryItemPartnerExpandOptions
+type A_SalesInquiryItemPartnerExpandOptions ("to_SalesInquiry"|"to_SalesInquiryItem")[];
 
-// Unknown type: A_SalesInquiryItemPartnerSelectOptions
+type A_SalesInquiryItemPartnerSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"PartnerFunction"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"to_SalesInquiry"|"to_SalesInquiryItem")[];
 
-// Unknown type: A_SalesInquiryItemPrcgElmntOrderByOptions
+type A_SalesInquiryItemPrcgElmntOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"SalesInquiryItem"|"SalesInquiryItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionApplication"|"ConditionApplication desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyNmrtr desc"|"ConditionToBaseQtyDnmntr"|"ConditionToBaseQtyDnmntr desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"AccessNumberOfAccessSequence"|"AccessNumberOfAccessSequence desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"ConditionAlternativeCurrency"|"ConditionAlternativeCurrency desc"|"ConditionAmountInLocalCrcy"|"ConditionAmountInLocalCrcy desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"CumulatedConditionBasisValue"|"CumulatedConditionBasisValue desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 
 type CollectionOfA_SalesInquiryItemPartnerWrapper record {
@@ -507,9 +522,10 @@
     A_SalesInquiryItemPartner[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
-// Unknown type: PricingElementOfA_SalesInquiryOrderByOptions
+type PricingElementOfA_SalesInquiryOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionApplication"|"ConditionApplication desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyNmrtr desc"|"ConditionToBaseQtyDnmntr"|"ConditionToBaseQtyDnmntr desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"AccessNumberOfAccessSequence"|"AccessNumberOfAccessSequence desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"ConditionAlternativeCurrency"|"ConditionAlternativeCurrency desc"|"ConditionAmountInLocalCrcy"|"ConditionAmountInLocalCrcy desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"CumulatedConditionBasisValue"|"CumulatedConditionBasisValue desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 # Represents the Queries record for the operation: getSalesInquiryOfA_SalesInquiryItem
 
@@ -520,15 +536,15 @@
     SalesInquiryOfA_SalesInquiryItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemExpandOptions
+type SalesInquiryOfA_SalesInquiryItemExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemSelectOptions
+type SalesInquiryOfA_SalesInquiryItemSelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: PricingElementOfA_SalesInquiryItemExpandOptions
+type PricingElementOfA_SalesInquiryItemExpandOptions ("to_SalesInquiry"|"to_SalesInquiryItem")[];
 
-// Unknown type: SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions
+type SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"HigherLevelItem"|"SalesInquiryItemCategory"|"SalesInquiryItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"RequestedQuantity"|"RequestedQuantityUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemVolume"|"ItemVolumeUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"Batch"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"SalesDocumentRjcnReason"|"WBSElement"|"SDProcessStatus"|"to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
-// Unknown type: A_SalesInquiryItemOrderByOptions
+type A_SalesInquiryItemOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"SalesInquiryItem"|"SalesInquiryItem desc"|"HigherLevelItem"|"HigherLevelItem desc"|"SalesInquiryItemCategory"|"SalesInquiryItemCategory desc"|"SalesInquiryItemText"|"SalesInquiryItemText desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"Material"|"Material desc"|"MaterialByCustomer"|"MaterialByCustomer desc"|"RequestedQuantity"|"RequestedQuantity desc"|"RequestedQuantityUnit"|"RequestedQuantityUnit desc"|"ItemOrderProbabilityInPercent"|"ItemOrderProbabilityInPercent desc"|"AlternativeToItem"|"AlternativeToItem desc"|"ItemGrossWeight"|"ItemGrossWeight desc"|"ItemNetWeight"|"ItemNetWeight desc"|"ItemWeightUnit"|"ItemWeightUnit desc"|"ItemVolume"|"ItemVolume desc"|"ItemVolumeUnit"|"ItemVolumeUnit desc"|"TransactionCurrency"|"TransactionCurrency desc"|"NetAmount"|"NetAmount desc"|"MaterialGroup"|"MaterialGroup desc"|"Batch"|"Batch desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"SalesDocumentRjcnReason"|"SalesDocumentRjcnReason desc"|"WBSElement"|"WBSElement desc"|"SDProcessStatus"|"SDProcessStatus desc")[];
 
 # Represents the Queries record for the operation: listA_SalesInquiryPartners
 
@@ -549,17 +565,17 @@
     A_SalesInquiryPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryPartnerOrderByOptions
+type A_SalesInquiryPartnerOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"PartnerFunction"|"PartnerFunction desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc")[];
 
-// Unknown type: A_SalesInquiryPartnerExpandOptions
+type A_SalesInquiryPartnerExpandOptions "to_SalesInquiry"[];
 
-// Unknown type: A_SalesInquiryPartnerSelectOptions
-
-// Unknown type: A_SalesInquiryPrcgElmntExpandOptions
+type A_SalesInquiryPartnerSelectOptions ("SalesInquiry"|"PartnerFunction"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"to_SalesInquiry")[];
 
-// Unknown type: PricingElementOfA_SalesInquiryExpandOptions
+type A_SalesInquiryPrcgElmntExpandOptions "to_SalesInquiry"[];
 
+type PricingElementOfA_SalesInquiryExpandOptions "to_SalesInquiry"[];
 
+
 type CollectionOfA_SalesInquiryItemPrcgElmntWrapper record {
     CollectionOfA_SalesInquiryItemPrcgElmnt d?;
 };
@@ -589,11 +605,11 @@
     A_SalesInquiryPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryPrcgElmntOrderByOptions
+type A_SalesInquiryPrcgElmntOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionApplication"|"ConditionApplication desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyNmrtr desc"|"ConditionToBaseQtyDnmntr"|"ConditionToBaseQtyDnmntr desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"AccessNumberOfAccessSequence"|"AccessNumberOfAccessSequence desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"ConditionAlternativeCurrency"|"ConditionAlternativeCurrency desc"|"ConditionAmountInLocalCrcy"|"ConditionAmountInLocalCrcy desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"CumulatedConditionBasisValue"|"CumulatedConditionBasisValue desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
-// Unknown type: A_SalesInquiryPrcgElmntSelectOptions
+type A_SalesInquiryPrcgElmntSelectOptions ("SalesInquiry"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionApplication"|"ConditionType"|"PricingDateTime"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyDnmntr"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"AccessNumberOfAccessSequence"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"ConditionAlternativeCurrency"|"ConditionAmountInLocalCrcy"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"CumulatedConditionBasisValue"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesInquiry")[];
 
-// Unknown type: A_SalesInquiryExpandOptions
+type A_SalesInquiryExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
 # Represents the Queries record for the operation: listPartnersOfA_SalesInquiry
 
@@ -616,6 +632,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:CredentialsConfig auth; // Special Agent Note: CredentialsConfig FROM ballerina/http package
@@ -670,10 +687,11 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
-// Unknown type: A_SalesInquiryItemPrcgElmntExpandOptions
+type A_SalesInquiryItemPrcgElmntExpandOptions ("to_SalesInquiry"|"to_SalesInquiryItem")[];
 
 
 type CollectionOfA_SalesInquiryWrapper record {
@@ -695,11 +713,11 @@
     SalesInquiryOfA_SalesInquiryPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryPartnerExpandOptions
+type SalesInquiryOfA_SalesInquiryPartnerExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: SalesInquiryOfA_SalesInquiryPartnerSelectOptions
+type SalesInquiryOfA_SalesInquiryPartnerSelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: A_SalesInquiryItemSelectOptions
+type A_SalesInquiryItemSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"HigherLevelItem"|"SalesInquiryItemCategory"|"SalesInquiryItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"RequestedQuantity"|"RequestedQuantityUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemVolume"|"ItemVolumeUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"Batch"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"SalesDocumentRjcnReason"|"WBSElement"|"SDProcessStatus"|"to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
 # Represents the Queries record for the operation: listA_SalesInquiryItems
 
@@ -720,7 +738,7 @@
     A_SalesInquiryItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryItemExpandOptions
+type A_SalesInquiryItemExpandOptions ("to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
 # Represents the Queries record for the operation: getSalesInquiryItemOfA_SalesInquiryItemPrcgElmnt
 
@@ -731,9 +749,9 @@
     SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions
+type SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions ("to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
-// Unknown type: SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions
+type SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"HigherLevelItem"|"SalesInquiryItemCategory"|"SalesInquiryItemText"|"PurchaseOrderByCustomer"|"Material"|"MaterialByCustomer"|"RequestedQuantity"|"RequestedQuantityUnit"|"ItemOrderProbabilityInPercent"|"AlternativeToItem"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemVolume"|"ItemVolumeUnit"|"TransactionCurrency"|"NetAmount"|"MaterialGroup"|"Batch"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"CustomerPaymentTerms"|"SalesDocumentRjcnReason"|"WBSElement"|"SDProcessStatus"|"to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
 
 type A_SalesInquiryItemPartnerWrapper record {
@@ -749,9 +767,9 @@
     SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions
+type SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions
+type SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
 # Represents the Queries record for the operation: listA_SalesInquiryItemPrcgElmnts
 
@@ -772,9 +790,9 @@
     A_SalesInquiryItemPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryItemPrcgElmntSelectOptions
+type A_SalesInquiryItemPrcgElmntSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionApplication"|"ConditionType"|"PricingDateTime"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyDnmntr"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"AccessNumberOfAccessSequence"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"ConditionAlternativeCurrency"|"ConditionAmountInLocalCrcy"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"CumulatedConditionBasisValue"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesInquiry"|"to_SalesInquiryItem")[];
 
-// Unknown type: PricingElementOfA_SalesInquiryItemOrderByOptions
+type PricingElementOfA_SalesInquiryItemOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"SalesInquiryItem"|"SalesInquiryItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionApplication"|"ConditionApplication desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyNmrtr desc"|"ConditionToBaseQtyDnmntr"|"ConditionToBaseQtyDnmntr desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"AccessNumberOfAccessSequence"|"AccessNumberOfAccessSequence desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"ConditionAlternativeCurrency"|"ConditionAlternativeCurrency desc"|"ConditionAmountInLocalCrcy"|"ConditionAmountInLocalCrcy desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"CumulatedConditionBasisValue"|"CumulatedConditionBasisValue desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 
 type CollectionOfA_SalesInquiryPartnerWrapper record {
@@ -796,7 +814,7 @@
     A_SalesInquiryItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions
+type SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
 # Represents the Queries record for the operation: getA_SalesInquiryPrcgElmnt
 
@@ -822,7 +840,7 @@
     A_SalesInquirySelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquirySelectOptions
+type A_SalesInquirySelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
 # Represents the Queries record for the operation: getA_SalesInquiryItem
 
@@ -844,7 +862,7 @@
     A_SalesInquiryItem[] results?;
 };
 
-// Unknown type: SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions
+type SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions ("to_Partner"|"to_PricingElement"|"to_SalesInquiry")[];
 
 # Represents the Queries record for the operation: listItemsOfA_SalesInquiry
 
@@ -874,9 +892,9 @@
     A_SalesInquiryPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions
+type SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: PricingElementOfA_SalesInquirySelectOptions
+type PricingElementOfA_SalesInquirySelectOptions ("SalesInquiry"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionApplication"|"ConditionType"|"PricingDateTime"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyDnmntr"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"AccessNumberOfAccessSequence"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"ConditionAlternativeCurrency"|"ConditionAmountInLocalCrcy"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"CumulatedConditionBasisValue"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesInquiry")[];
 
 # Represents the Queries record for the operation: getSalesInquiryOfA_SalesInquiryItemPrcgElmnt
 
@@ -887,9 +905,9 @@
     SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions \$select?;
 };
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions
+type SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions ("to_Item"|"to_Partner"|"to_PricingElement")[];
 
-// Unknown type: SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions
+type SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions ("SalesInquiry"|"SalesInquiryType"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"LastChangeDateTime"|"PurchaseOrderByCustomer"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesInquiryDate"|"TotalNetAmount"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"HeaderBillingBlockReason"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityEndDate"|"HdrOrderProbabilityInPercent"|"ExpectedOrderNetAmount"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPaymentTerms"|"PaymentMethod"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallSDDocumentRejectionSts"|"to_Item"|"to_Partner"|"to_PricingElement")[];
 
 # Represents the Queries record for the operation: getSalesInquiryItemOfA_SalesInquiryItemPartner
 
@@ -919,7 +937,7 @@
     PricingElementOfA_SalesInquirySelectOptions \$select?;
 };
 
-// Unknown type: PricingElementOfA_SalesInquiryItemSelectOptions
+type PricingElementOfA_SalesInquiryItemSelectOptions ("SalesInquiry"|"SalesInquiryItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionApplication"|"ConditionType"|"PricingDateTime"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionToBaseQtyNmrtr"|"ConditionToBaseQtyDnmntr"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"AccessNumberOfAccessSequence"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"ConditionAlternativeCurrency"|"ConditionAmountInLocalCrcy"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"CumulatedConditionBasisValue"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesInquiry"|"to_SalesInquiryItem")[];
 
 # Represents the Queries record for the operation: listPricingElementsOfA_SalesInquiryItem
 
@@ -1011,7 +1029,7 @@
     A_SalesInquirySelectOptions \$select?;
 };
 
-// Unknown type: A_SalesInquiryOrderByOptions
+type A_SalesInquiryOrderByOptions ("SalesInquiry"|"SalesInquiry desc"|"SalesInquiryType"|"SalesInquiryType desc"|"SalesOrganization"|"SalesOrganization desc"|"DistributionChannel"|"DistributionChannel desc"|"OrganizationDivision"|"OrganizationDivision desc"|"SalesGroup"|"SalesGroup desc"|"SalesOffice"|"SalesOffice desc"|"SalesDistrict"|"SalesDistrict desc"|"SoldToParty"|"SoldToParty desc"|"CreationDate"|"CreationDate desc"|"CreatedByUser"|"CreatedByUser desc"|"LastChangeDate"|"LastChangeDate desc"|"LastChangeDateTime"|"LastChangeDateTime desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderType desc"|"CustomerPurchaseOrderDate"|"CustomerPurchaseOrderDate desc"|"SalesInquiryDate"|"SalesInquiryDate desc"|"TotalNetAmount"|"TotalNetAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SDDocumentReason"|"SDDocumentReason desc"|"PricingDate"|"PricingDate desc"|"HeaderBillingBlockReason"|"HeaderBillingBlockReason desc"|"BindingPeriodValidityStartDate"|"BindingPeriodValidityStartDate desc"|"BindingPeriodValidityEndDate"|"BindingPeriodValidityEndDate desc"|"HdrOrderProbabilityInPercent"|"HdrOrderProbabilityInPercent desc"|"ExpectedOrderNetAmount"|"ExpectedOrderNetAmount desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"IncotermsVersion"|"IncotermsVersion desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"PaymentMethod"|"PaymentMethod desc"|"OverallSDProcessStatus"|"OverallSDProcessStatus desc"|"TotalCreditCheckStatus"|"TotalCreditCheckStatus desc"|"OverallSDDocumentRejectionSts"|"OverallSDDocumentRejectionSts desc")[];
 
 
 type CollectionOfA_SalesInquiryPrcgElmntWrapper record {
@@ -1031,99 +1049,99 @@
 
     # Reads a specific sales inquiry header.
     # 
-    remote function getA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, A_SalesInquiryExpandOptions \$expand = [], A_SalesInquirySelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, A_SalesInquiryExpandOptions \$expand = [], A_SalesInquirySelectOptions \$select = [], GetA_SalesInquiryQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads a specific sales inquiry item.
     # 
-    remote function getA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, A_SalesInquiryItemExpandOptions \$expand = [], A_SalesInquiryItemSelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryItemQueries queries) returns A_SalesInquiryItemWrapper|error;
+    remote function getA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, A_SalesInquiryItemExpandOptions \$expand = [], A_SalesInquiryItemSelectOptions \$select = [], GetA_SalesInquiryItemQueries queries) returns A_SalesInquiryItemWrapper|error;
 
     # Reads a specific item-level business partner.
     # 
-    remote function getA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesInquiryItemPartnerExpandOptions \$expand = [], A_SalesInquiryItemPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryItemPartnerWrapper|error;
+    remote function getA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesInquiryItemPartnerExpandOptions \$expand = [], A_SalesInquiryItemPartnerSelectOptions \$select = [], GetA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryItemPartnerWrapper|error;
 
     # Reads a specific item-level pricing element.
     # 
-    remote function getA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], A_SalesInquiryItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryItemPrcgElmntWrapper|error;
+    remote function getA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], A_SalesInquiryItemPrcgElmntSelectOptions \$select = [], GetA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryItemPrcgElmntWrapper|error;
 
     # Reads a specific header-level business partner.
     # 
-    remote function getA_SalesInquiryPartner(string SalesInquiry, string PartnerFunction, map<string|string[]> headers = {}, A_SalesInquiryPartnerExpandOptions \$expand = [], A_SalesInquiryPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryPartnerQueries queries) returns A_SalesInquiryPartnerWrapper|error;
+    remote function getA_SalesInquiryPartner(string SalesInquiry, string PartnerFunction, map<string|string[]> headers = {}, A_SalesInquiryPartnerExpandOptions \$expand = [], A_SalesInquiryPartnerSelectOptions \$select = [], GetA_SalesInquiryPartnerQueries queries) returns A_SalesInquiryPartnerWrapper|error;
 
     # Reads a specific header-level pricing element.
     # 
-    remote function getA_SalesInquiryPrcgElmnt(string SalesInquiry, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesInquiryPrcgElmntExpandOptions \$expand = [], A_SalesInquiryPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetA_SalesInquiryPrcgElmntQueries queries) returns A_SalesInquiryPrcgElmntWrapper|error;
+    remote function getA_SalesInquiryPrcgElmnt(string SalesInquiry, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesInquiryPrcgElmntExpandOptions \$expand = [], A_SalesInquiryPrcgElmntSelectOptions \$select = [], GetA_SalesInquiryPrcgElmntQueries queries) returns A_SalesInquiryPrcgElmntWrapper|error;
 
     # Reads the sales inquiry item for a specific item partner.
     # 
-    remote function getSalesInquiryItemOfA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions \$expand = [], SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryItemOfA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryItemWrapper|error;
+    remote function getSalesInquiryItemOfA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryItemOfA_SalesInquiryItemPartnerExpandOptions \$expand = [], SalesInquiryItemOfA_SalesInquiryItemPartnerSelectOptions \$select = [], GetSalesInquiryItemOfA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryItemWrapper|error;
 
     # Reads the sales inquiry item for a specific item pricing element.
     # 
-    remote function getSalesInquiryItemOfA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryItemOfA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryItemWrapper|error;
+    remote function getSalesInquiryItemOfA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryItemOfA_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], SalesInquiryItemOfA_SalesInquiryItemPrcgElmntSelectOptions \$select = [], GetSalesInquiryItemOfA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryItemWrapper|error;
 
     # Reads the sales inquiry header for a specific item.
     # 
-    remote function getSalesInquiryOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryOfA_SalesInquiryItemQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getSalesInquiryOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemSelectOptions \$select = [], GetSalesInquiryOfA_SalesInquiryItemQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads the sales inquiry header for a specific item partner.
     # 
-    remote function getSalesInquiryOfA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryOfA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getSalesInquiryOfA_SalesInquiryItemPartner(string SalesInquiry, string SalesInquiryItem, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemPartnerExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemPartnerSelectOptions \$select = [], GetSalesInquiryOfA_SalesInquiryItemPartnerQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads the sales inquiry header for a specific item pricing element.
     # 
-    remote function getSalesInquiryOfA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryOfA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getSalesInquiryOfA_SalesInquiryItemPrcgElmnt(string SalesInquiry, string SalesInquiryItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryItemPrcgElmntSelectOptions \$select = [], GetSalesInquiryOfA_SalesInquiryItemPrcgElmntQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads the sales inquiry header for a specific header partner.
     # 
-    remote function getSalesInquiryOfA_SalesInquiryPartner(string SalesInquiry, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryPartnerExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryOfA_SalesInquiryPartnerQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getSalesInquiryOfA_SalesInquiryPartner(string SalesInquiry, string PartnerFunction, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryPartnerExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryPartnerSelectOptions \$select = [], GetSalesInquiryOfA_SalesInquiryPartnerQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads the sales inquiry header for a specific header pricing element.
     # 
-    remote function getSalesInquiryOfA_SalesInquiryPrcgElmnt(string SalesInquiry, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions \$select = [], anydata Additional Values, GetSalesInquiryOfA_SalesInquiryPrcgElmntQueries queries) returns A_SalesInquiryWrapper|error;
+    remote function getSalesInquiryOfA_SalesInquiryPrcgElmnt(string SalesInquiry, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesInquiryOfA_SalesInquiryPrcgElmntExpandOptions \$expand = [], SalesInquiryOfA_SalesInquiryPrcgElmntSelectOptions \$select = [], GetSalesInquiryOfA_SalesInquiryPrcgElmntQueries queries) returns A_SalesInquiryWrapper|error;
 
     # Reads all sales inquiry headers.
     # 
-    remote function listA_SalesInquiries(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryOrderByOptions \$orderby = [], A_SalesInquiryExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquirySelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiriesQueries queries) returns CollectionOfA_SalesInquiryWrapper|error;
+    remote function listA_SalesInquiries(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryOrderByOptions \$orderby = [], A_SalesInquiryExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquirySelectOptions \$select = [], ListA_SalesInquiriesQueries queries) returns CollectionOfA_SalesInquiryWrapper|error;
 
     # Reads the item-level business partners of all sales inquiry items.
     # 
-    remote function listA_SalesInquiryItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPartnerOrderByOptions \$orderby = [], A_SalesInquiryItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiryItemPartnersQueries queries) returns CollectionOfA_SalesInquiryItemPartnerWrapper|error;
+    remote function listA_SalesInquiryItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPartnerOrderByOptions \$orderby = [], A_SalesInquiryItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPartnerSelectOptions \$select = [], ListA_SalesInquiryItemPartnersQueries queries) returns CollectionOfA_SalesInquiryItemPartnerWrapper|error;
 
     # Reads the item-level pricing elements of all sales inquiry items.
     # 
-    remote function listA_SalesInquiryItemPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPrcgElmntOrderByOptions \$orderby = [], A_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPrcgElmntSelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiryItemPrcgElmntsQueries queries) returns CollectionOfA_SalesInquiryItemPrcgElmntWrapper|error;
+    remote function listA_SalesInquiryItemPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPrcgElmntOrderByOptions \$orderby = [], A_SalesInquiryItemPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPrcgElmntSelectOptions \$select = [], ListA_SalesInquiryItemPrcgElmntsQueries queries) returns CollectionOfA_SalesInquiryItemPrcgElmntWrapper|error;
 
     # Reads all sales inquiry items.
     # 
-    remote function listA_SalesInquiryItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemOrderByOptions \$orderby = [], A_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemSelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiryItemsQueries queries) returns CollectionOfA_SalesInquiryItemWrapper|error;
+    remote function listA_SalesInquiryItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemOrderByOptions \$orderby = [], A_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemSelectOptions \$select = [], ListA_SalesInquiryItemsQueries queries) returns CollectionOfA_SalesInquiryItemWrapper|error;
 
     # Reads the header-level business partners of all sales inquiries.
     # 
-    remote function listA_SalesInquiryPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPartnerOrderByOptions \$orderby = [], A_SalesInquiryPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiryPartnersQueries queries) returns CollectionOfA_SalesInquiryPartnerWrapper|error;
+    remote function listA_SalesInquiryPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPartnerOrderByOptions \$orderby = [], A_SalesInquiryPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPartnerSelectOptions \$select = [], ListA_SalesInquiryPartnersQueries queries) returns CollectionOfA_SalesInquiryPartnerWrapper|error;
 
     # Reads the header-level pricing elements of all sales inquiries.
     # 
-    remote function listA_SalesInquiryPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPrcgElmntOrderByOptions \$orderby = [], A_SalesInquiryPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPrcgElmntSelectOptions \$select = [], anydata Additional Values, ListA_SalesInquiryPrcgElmntsQueries queries) returns CollectionOfA_SalesInquiryPrcgElmntWrapper|error;
+    remote function listA_SalesInquiryPrcgElmnts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPrcgElmntOrderByOptions \$orderby = [], A_SalesInquiryPrcgElmntExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPrcgElmntSelectOptions \$select = [], ListA_SalesInquiryPrcgElmntsQueries queries) returns CollectionOfA_SalesInquiryPrcgElmntWrapper|error;
 
     # Reads all items of a specific sales inquiry.
     # 
-    remote function listItemsOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemOrderByOptions \$orderby = [], A_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemSelectOptions \$select = [], anydata Additional Values, ListItemsOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryItemWrapper|error;
+    remote function listItemsOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemOrderByOptions \$orderby = [], A_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemSelectOptions \$select = [], ListItemsOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryItemWrapper|error;
 
     # Reads the header-level business partners of a specific sales inquiry.
     # 
-    remote function listPartnersOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPartnerOrderByOptions \$orderby = [], A_SalesInquiryPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryPartnerWrapper|error;
+    remote function listPartnersOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryPartnerOrderByOptions \$orderby = [], A_SalesInquiryPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryPartnerSelectOptions \$select = [], ListPartnersOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryPartnerWrapper|error;
 
     # Reads the item-level business partners of a specific sales inquiry item.
     # 
-    remote function listPartnersOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPartnerOrderByOptions \$orderby = [], A_SalesInquiryItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesInquiryItemQueries queries) returns CollectionOfA_SalesInquiryItemPartnerWrapper|error;
+    remote function listPartnersOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesInquiryItemPartnerOrderByOptions \$orderby = [], A_SalesInquiryItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesInquiryItemPartnerSelectOptions \$select = [], ListPartnersOfA_SalesInquiryItemQueries queries) returns CollectionOfA_SalesInquiryItemPartnerWrapper|error;
 
     # Reads the header-level pricing elements of a specific sales inquiry.
     # 
-    remote function listPricingElementsOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesInquiryOrderByOptions \$orderby = [], PricingElementOfA_SalesInquiryExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesInquirySelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryPrcgElmntWrapper|error;
+    remote function listPricingElementsOfA_SalesInquiry(string SalesInquiry, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesInquiryOrderByOptions \$orderby = [], PricingElementOfA_SalesInquiryExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesInquirySelectOptions \$select = [], ListPricingElementsOfA_SalesInquiryQueries queries) returns CollectionOfA_SalesInquiryPrcgElmntWrapper|error;
 
     # Reads the item-level pricing elements of a specific sales inquiry item.
     # 
-    remote function listPricingElementsOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesInquiryItemOrderByOptions \$orderby = [], PricingElementOfA_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesInquiryItemSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesInquiryItemQueries queries) returns CollectionOfA_SalesInquiryItemPrcgElmntWrapper|error;
+    remote function listPricingElementsOfA_SalesInquiryItem(string SalesInquiry, string SalesInquiryItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesInquiryItemOrderByOptions \$orderby = [], PricingElementOfA_SalesInquiryItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesInquiryItemSelectOptions \$select = [], ListPricingElementsOfA_SalesInquiryItemQueries queries) returns CollectionOfA_SalesInquiryItemPrcgElmntWrapper|error;
 
     # Send a group of requests
     # 
`````

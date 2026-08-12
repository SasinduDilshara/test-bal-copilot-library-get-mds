# sap.s4hana.api_sales_order_srv — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `sap.s4hana.api_sales_order_srv` |
| **Old file** | `sap.s4hana.api_sales_order_srv/old/ballerinax_sap.s4hana.api_sales_order_srv.bal.txt` |
| **New file** | `sap.s4hana.api_sales_order_srv/new/ballerinax_sap.s4hana.api_sales_order_srv.bal.txt` |
| **Old lines** | 5398 |
| **New lines** | 5487 |
| **Lines added** | 358 |
| **Lines removed** | 269 |
| **Hunks** | 133 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 167 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (167)

- `type A_SalesOrderBillingPlanExpandOptions`
- `type A_SalesOrderBillingPlanItemExpandOptions`
- `type A_SalesOrderBillingPlanItemOrderByOptions`
- `type A_SalesOrderBillingPlanItemSelectOptions`
- `type A_SalesOrderBillingPlanOrderByOptions`
- `type A_SalesOrderBillingPlanSelectOptions`
- `type A_SalesOrderExpandOptions`
- `type A_SalesOrderHeaderPartnerExpandOptions`
- `type A_SalesOrderHeaderPartnerOrderByOptions`
- `type A_SalesOrderHeaderPartnerSelectOptions`
- `type A_SalesOrderHeaderPrElementExpandOptions`
- `type A_SalesOrderHeaderPrElementOrderByOptions`
- `type A_SalesOrderHeaderPrElementSelectOptions`
- `type A_SalesOrderItemBillingPlanExpandOptions`
- `type A_SalesOrderItemBillingPlanOrderByOptions`
- `type A_SalesOrderItemBillingPlanSelectOptions`
- `type A_SalesOrderItemExpandOptions`
- `type A_SalesOrderItemOrderByOptions`
- `type A_SalesOrderItemPartnerAddressExpandOptions`
- `type A_SalesOrderItemPartnerAddressOrderByOptions`
- `type A_SalesOrderItemPartnerAddressSelectOptions`
- `type A_SalesOrderItemPartnerExpandOptions`
- `type A_SalesOrderItemPartnerOrderByOptions`
- `type A_SalesOrderItemPartnerSelectOptions`
- `type A_SalesOrderItemPrElementExpandOptions`
- `type A_SalesOrderItemPrElementOrderByOptions`
- `type A_SalesOrderItemPrElementSelectOptions`
- `type A_SalesOrderItemRelatedObjectExpandOptions`
- `type A_SalesOrderItemRelatedObjectOrderByOptions`
- `type A_SalesOrderItemRelatedObjectSelectOptions`
- `type A_SalesOrderItemSelectOptions`
- `type A_SalesOrderItemTextExpandOptions`
- `type A_SalesOrderItemTextOrderByOptions`
- `type A_SalesOrderItemTextSelectOptions`
- `type A_SalesOrderItmPrecdgProcFlowExpandOptions`
- `type A_SalesOrderItmPrecdgProcFlowOrderByOptions`
- `type A_SalesOrderItmPrecdgProcFlowSelectOptions`
- `type A_SalesOrderItmSubsqntProcFlowExpandOptions`
- `type A_SalesOrderItmSubsqntProcFlowOrderByOptions`
- `type A_SalesOrderItmSubsqntProcFlowSelectOptions`
- `type A_SalesOrderOrderByOptions`
- `type A_SalesOrderPartnerAddressExpandOptions`
- `type A_SalesOrderPartnerAddressOrderByOptions`
- `type A_SalesOrderPartnerAddressSelectOptions`
- `type A_SalesOrderPrecdgProcFlowExpandOptions`
- `type A_SalesOrderPrecdgProcFlowOrderByOptions`
- `type A_SalesOrderPrecdgProcFlowSelectOptions`
- `type A_SalesOrderRelatedObjectExpandOptions`
- `type A_SalesOrderRelatedObjectOrderByOptions`
- `type A_SalesOrderRelatedObjectSelectOptions`
- `type A_SalesOrderScheduleLineOrderByOptions`
- `type A_SalesOrderScheduleLineSelectOptions`
- `type A_SalesOrderSelectOptions`
- `type A_SalesOrderSubsqntProcFlowExpandOptions`
- `type A_SalesOrderSubsqntProcFlowOrderByOptions`
- `type A_SalesOrderSubsqntProcFlowSelectOptions`
- `type A_SalesOrderTextExpandOptions`
- `type A_SalesOrderTextOrderByOptions`
- `type A_SalesOrderTextSelectOptions`
- `type A_SlsOrdPaymentPlanItemDetailsExpandOptions`
- `type A_SlsOrdPaymentPlanItemDetailsOrderByOptions`
- `type A_SlsOrdPaymentPlanItemDetailsSelectOptions`
- `type A_SlsOrderItemBillingPlanItemExpandOptions`
- `type A_SlsOrderItemBillingPlanItemOrderByOptions`
- `type A_SlsOrderItemBillingPlanItemSelectOptions`
- `type AddressOfA_SalesOrderHeaderPartnerExpandOptions`
- `type AddressOfA_SalesOrderHeaderPartnerOrderByOptions`
- `type AddressOfA_SalesOrderHeaderPartnerSelectOptions`
- `type BillingPlanItemOfA_SalesOrderBillingPlanExpandOptions`
- `type BillingPlanItemOfA_SalesOrderBillingPlanOrderByOptions`
- `type BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions`
- `type BillingPlanItemOfA_SalesOrderItemBillingPlanExpandOptions`
- `type BillingPlanItemOfA_SalesOrderItemBillingPlanOrderByOptions`
- `type BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions`
- `type BillingPlanOfA_SalesOrderBillingPlanItemExpandOptions`
- `type BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions`
- `type BillingPlanOfA_SlsOrderItemBillingPlanItemExpandOptions`
- `type BillingPlanOfA_SlsOrderItemBillingPlanItemSelectOptions`
- `type PartnerOfA_SalesOrderExpandOptions`
- `type PartnerOfA_SalesOrderItemPartnerAddressExpandOptions`
- `type PartnerOfA_SalesOrderItemPartnerAddressSelectOptions`
- `type PartnerOfA_SalesOrderOrderByOptions`
- `type PartnerOfA_SalesOrderPartnerAddressExpandOptions`
- `type PartnerOfA_SalesOrderPartnerAddressSelectOptions`
- `type PartnerOfA_SalesOrderSelectOptions`
- `type PaymentPlanItemDetailsOfA_SalesOrderExpandOptions`
- `type PaymentPlanItemDetailsOfA_SalesOrderOrderByOptions`
- `type PaymentPlanItemDetailsOfA_SalesOrderSelectOptions`
- `type PrecedingProcFlowDocItemOfA_SalesOrderItemExpandOptions`
- `type PrecedingProcFlowDocItemOfA_SalesOrderItemOrderByOptions`
- `type PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions`
- `type PrecedingProcFlowDocOfA_SalesOrderExpandOptions`
- `type PrecedingProcFlowDocOfA_SalesOrderOrderByOptions`
- `type PrecedingProcFlowDocOfA_SalesOrderSelectOptions`
- `type PricingElementOfA_SalesOrderExpandOptions`
- `type PricingElementOfA_SalesOrderItemExpandOptions`
- `type PricingElementOfA_SalesOrderItemOrderByOptions`
- `type PricingElementOfA_SalesOrderItemSelectOptions`
- `type PricingElementOfA_SalesOrderOrderByOptions`
- `type PricingElementOfA_SalesOrderSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemBillingPlanExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemBillingPlanSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemPartnerAddressExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemPartnerAddressSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemPartnerExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemPartnerSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemPrElementExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemRelatedObjectExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItemTextExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItemTextSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions`
- `type SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowExpandOptions`
- `type SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions`
- `type SalesOrderItemOfA_SlsOrderItemBillingPlanItemExpandOptions`
- `type SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions`
- `type SalesOrderOfA_SalesOrderBillingPlanExpandOptions`
- `type SalesOrderOfA_SalesOrderBillingPlanItemExpandOptions`
- `type SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions`
- `type SalesOrderOfA_SalesOrderBillingPlanSelectOptions`
- `type SalesOrderOfA_SalesOrderHeaderPartnerExpandOptions`
- `type SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions`
- `type SalesOrderOfA_SalesOrderHeaderPrElementExpandOptions`
- `type SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions`
- `type SalesOrderOfA_SalesOrderItemBillingPlanExpandOptions`
- `type SalesOrderOfA_SalesOrderItemBillingPlanSelectOptions`
- `type SalesOrderOfA_SalesOrderItemExpandOptions`
- `type SalesOrderOfA_SalesOrderItemPartnerAddressExpandOptions`
- `type SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions`
- `type SalesOrderOfA_SalesOrderItemPartnerExpandOptions`
- `type SalesOrderOfA_SalesOrderItemPartnerSelectOptions`
- `type SalesOrderOfA_SalesOrderItemPrElementExpandOptions`
- `type SalesOrderOfA_SalesOrderItemPrElementSelectOptions`
- `type SalesOrderOfA_SalesOrderItemRelatedObjectExpandOptions`
- `type SalesOrderOfA_SalesOrderItemRelatedObjectSelectOptions`
- `type SalesOrderOfA_SalesOrderItemSelectOptions`
- `type SalesOrderOfA_SalesOrderItemTextExpandOptions`
- `type SalesOrderOfA_SalesOrderItemTextSelectOptions`
- `type SalesOrderOfA_SalesOrderItmPrecdgProcFlowExpandOptions`
- `type SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions`
- `type SalesOrderOfA_SalesOrderItmSubsqntProcFlowExpandOptions`
- `type SalesOrderOfA_SalesOrderItmSubsqntProcFlowSelectOptions`
- `type SalesOrderOfA_SalesOrderPartnerAddressExpandOptions`
- `type SalesOrderOfA_SalesOrderPartnerAddressSelectOptions`
- `type SalesOrderOfA_SalesOrderPrecdgProcFlowExpandOptions`
- `type SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions`
- `type SalesOrderOfA_SalesOrderRelatedObjectExpandOptions`
- `type SalesOrderOfA_SalesOrderRelatedObjectSelectOptions`
- `type SalesOrderOfA_SalesOrderSubsqntProcFlowExpandOptions`
- `type SalesOrderOfA_SalesOrderSubsqntProcFlowSelectOptions`
- `type SalesOrderOfA_SalesOrderTextExpandOptions`
- `type SalesOrderOfA_SalesOrderTextSelectOptions`
- `type SalesOrderOfA_SlsOrdPaymentPlanItemDetailsExpandOptions`
- `type SalesOrderOfA_SlsOrdPaymentPlanItemDetailsSelectOptions`
- `type SalesOrderOfA_SlsOrderItemBillingPlanItemExpandOptions`
- `type SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions`
- `type ScheduleLineOfA_SalesOrderItemOrderByOptions`
- `type ScheduleLineOfA_SalesOrderItemSelectOptions`
- `type SubsequentProcFlowDocItemOfA_SalesOrderItemExpandOptions`
- `type SubsequentProcFlowDocItemOfA_SalesOrderItemOrderByOptions`
- `type SubsequentProcFlowDocItemOfA_SalesOrderItemSelectOptions`
- `type SubsequentProcFlowDocOfA_SalesOrderExpandOptions`
- `type SubsequentProcFlowDocOfA_SalesOrderOrderByOptions`
- `type SubsequentProcFlowDocOfA_SalesOrderSelectOptions`
- `type count`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 122–133 | 122–137 | Types | +4 | −0 |
| 2 | 170–179 | 174–186 | Types | +3 | −0 |
| 3 | 205–210 | 212–218 | Types | +1 | −0 |
| 4 | 351–358 | 359–368 | Types | +2 | −0 |
| 5 | 381–390 | 391–403 | Types | +3 | −0 |
| 6 | 431–438 | 444–453 | Types | +2 | −0 |
| 7 | 615–623 | 630–641 | Types | +3 | −0 |
| 8 | 645–655 | 663–677 | Types | +4 | −0 |
| 9 | 710–717 | 732–741 | Types | +2 | −0 |
| 10 | 747–757 | 771–785 | Types | +4 | −0 |
| 11 | 835–844 | 863–875 | Types | +3 | −0 |
| 12 | 859–866 | 890–900 | Types | +3 | −0 |
| 13 | 891–898 | 925–934 | Types | +2 | −0 |
| 14 | 934–943 | 970–983 | Types | +4 | −0 |
| 15 | 951–957 | 991–999 | Types | +2 | −0 |
| 16 | 978–986 | 1020–1031 | Types | +3 | −0 |
| 17 | 1039–1046 | 1084–1093 | Types | +2 | −0 |
| 18 | 1109–1114 | 1156–1162 | Types | +1 | −0 |
| 19 | 1136–1144 | 1184–1195 | Types | +3 | −0 |
| 20 | 1217–1224 | 1268–1277 | Types | +2 | −0 |
| 21 | 1239–1244 | 1292–1298 | Types | +1 | −0 |
| 22 | 1266–1273 | 1320–1330 | Types | +3 | −0 |
| 23 | 1283–1289 | 1340–1346 | Types | +1 | −1 |
| 24 | 1304–1314 | 1361–1371 | Types | +3 | −3 |
| 25 | 1368–1373 | 1425–1431 | Types | +1 | −0 |
| 26 | 1390–1395 | 1448–1454 | Types | +1 | −0 |
| 27 | 1539–1544 | 1598–1604 | Types | +1 | −0 |
| 28 | 1711–1716 | 1771–1777 | Types | +1 | −0 |
| 29 | 1735–1745 | 1796–1810 | Types | +4 | −0 |
| 30 | 1800–1807 | 1865–1874 | Types | +2 | −0 |
| 31 | 1837–1844 | 1904–1913 | Types | +2 | −0 |
| 32 | 1885–1890 | 1954–1960 | Types | +1 | −0 |
| 33 | 1915–1922 | 1985–1994 | Types | +2 | −0 |
| 34 | 1958–1964 | 2030–2038 | Types | +2 | −0 |
| 35 | 1972–1977 | 2046–2052 | Types | +1 | −0 |
| 36 | 1995–2003 | 2070–2081 | Types | +3 | −0 |
| 37 | 2057–2062 | 2135–2141 | Types | +1 | −0 |
| 38 | 2097–2102 | 2176–2182 | Types | +1 | −0 |
| 39 | 2124–2131 | 2204–2213 | Types | +2 | −0 |
| 40 | 2175–2181 | 2257–2265 | Types | +2 | −0 |
| 41 | 2200–2210 | 2284–2294 | Types | +3 | −3 |
| 42 | 2212–2218 | 2296–2303 | Types | +2 | −1 |
| 43 | 2223–2233 | 2308–2318 | Types | +3 | −3 |
| 44 | 2239–2245 | 2324–2330 | Types | +1 | −1 |
| 45 | 2256–2264 | 2341–2349 | Types | +2 | −2 |
| 46 | 2275–2288 | 2360–2373 | Types | +5 | −5 |
| 47 | 2302–2312 | 2387–2397 | Types | +3 | −3 |
| 48 | 2315–2321 | 2400–2406 | Types | +1 | −1 |
| 49 | 2349–2357 | 2434–2442 | Types | +2 | −2 |
| 50 | 2362–2370 | 2447–2455 | Types | +2 | −2 |
| 51 | 2375–2383 | 2460–2468 | Types | +2 | −2 |
| 52 | 2388–2396 | 2473–2481 | Types | +2 | −2 |
| 53 | 2403–2409 | 2488–2494 | Types | +1 | −1 |
| 54 | 2428–2444 | 2513–2529 | Types | +6 | −6 |
| 55 | 2459–2467 | 2544–2552 | Types | +2 | −2 |
| 56 | 2472–2480 | 2557–2565 | Types | +2 | −2 |
| 57 | 2495–2507 | 2580–2592 | Types | +4 | −4 |
| 58 | 2524–2533 | 2609–2619 | Types | +2 | −1 |
| 59 | 2547–2553 | 2633–2639 | Types | +1 | −1 |
| 60 | 2568–2574 | 2654–2660 | Types | +1 | −1 |
| 61 | 2590–2598 | 2676–2684 | Types | +2 | −2 |
| 62 | 2603–2611 | 2689–2697 | Types | +2 | −2 |
| 63 | 2616–2624 | 2702–2710 | Types | +2 | −2 |
| 64 | 2717–2725 | 2803–2811 | Types | +2 | −2 |
| 65 | 2730–2740 | 2816–2826 | Types | +3 | −3 |
| 66 | 2756–2768 | 2842–2854 | Types | +4 | −4 |
| 67 | 2773–2781 | 2859–2867 | Types | +2 | −2 |
| 68 | 2805–2811 | 2891–2897 | Types | +1 | −1 |
| 69 | 2826–2837 | 2912–2923 | Types | +4 | −4 |
| 70 | 2851–2863 | 2937–2949 | Types | +4 | −4 |
| 71 | 2868–2876 | 2954–2962 | Types | +2 | −2 |
| 72 | 2881–2889 | 2967–2975 | Types | +2 | −2 |
| 73 | 2904–2916 | 2990–3002 | Types | +4 | −4 |
| 74 | 2926–2939 | 3012–3025 | Types | +2 | −2 |
| 75 | 2944–2952 | 3030–3038 | Types | +2 | −2 |
| 76 | 2984–2990 | 3070–3076 | Types | +1 | −1 |
| 77 | 3114–3120 | 3200–3206 | Types | +1 | −1 |
| 78 | 3125–3133 | 3211–3219 | Types | +2 | −2 |
| 79 | 3138–3146 | 3224–3232 | Types | +2 | −2 |
| 80 | 3171–3177 | 3257–3263 | Types | +1 | −1 |
| 81 | 3182–3188 | 3268–3274 | Types | +1 | −1 |
| 82 | 3203–3215 | 3289–3301 | Types | +4 | −4 |
| 83 | 3238–3244 | 3324–3330 | Types | +1 | −1 |
| 84 | 3249–3259 | 3335–3345 | Types | +3 | −3 |
| 85 | 3274–3282 | 3360–3368 | Types | +2 | −2 |
| 86 | 3295–3301 | 3381–3387 | Types | +1 | −1 |
| 87 | 3313–3323 | 3399–3409 | Types | +3 | −3 |
| 88 | 3341–3347 | 3427–3433 | Types | +1 | −1 |
| 89 | 3392–3397 | 3478–3484 | Types | +1 | −0 |
| 90 | 3414–3424 | 3501–3511 | Types | +3 | −3 |
| 91 | 3434–3442 | 3521–3529 | Types | +2 | −2 |
| 92 | 3444–3450 | 3531–3537 | Types | +1 | −1 |
| 93 | 3460–3466 | 3547–3553 | Types | +1 | −1 |
| 94 | 3481–3491 | 3568–3578 | Types | +3 | −3 |
| 95 | 3496–3511 | 3583–3598 | Types | +3 | −3 |
| 96 | 3568–3574 | 3655–3661 | Types | +1 | −1 |
| 97 | 3594–3600 | 3681–3687 | Types | +1 | −1 |
| 98 | 3607–3613 | 3694–3700 | Types | +1 | −1 |
| 99 | 3642–3648 | 3729–3735 | Types | +1 | −1 |
| 100 | 3660–3666 | 3747–3753 | Types | +1 | −1 |
| 101 | 3681–3687 | 3768–3774 | Types | +1 | −1 |
| 102 | 3698–3706 | 3785–3793 | Types | +2 | −2 |
| 103 | 3721–3727 | 3808–3814 | Types | +1 | −1 |
| 104 | 3737–3745 | 3824–3832 | Types | +2 | −2 |
| 105 | 3752–3758 | 3839–3845 | Types | +1 | −1 |
| 106 | 3763–3780 | 3850–3868 | Types | +4 | −3 |
| 107 | 3792–3798 | 3880–3886 | Types | +1 | −1 |
| 108 | 3813–3824 | 3901–3913 | Types | +3 | −2 |
| 109 | 3862–3868 | 3951–3957 | Types | +1 | −1 |
| 110 | 3878–3884 | 3967–3973 | Types | +1 | −1 |
| 111 | 3900–3906 | 3989–3995 | Types | +1 | −1 |
| 112 | 3930–3936 | 4019–4025 | Types | +1 | −1 |
| 113 | 3958–3964 | 4047–4053 | Types | +1 | −1 |
| 114 | 3969–3977 | 4058–4066 | Types | +2 | −2 |
| 115 | 3987–3995 | 4076–4084 | Types | +2 | −2 |
| 116 | 4000–4006 | 4089–4095 | Types | +1 | −1 |
| 117 | 4021–4029 | 4110–4118 | Types | +2 | −2 |
| 118 | 4034–4040 | 4123–4129 | Types | +1 | −1 |
| 119 | 4086–4092 | 4175–4181 | Types | +1 | −1 |
| 120 | 4159–4165 | 4248–4254 | Types | +1 | −1 |
| 121 | 4176–4182 | 4265–4271 | Types | +1 | −1 |
| 122 | 4197–4203 | 4286–4292 | Types | +1 | −1 |
| 123 | 4218–4224 | 4307–4313 | Types | +1 | −1 |
| 124 | 4258–4264 | 4347–4353 | Types | +1 | −1 |
| 125 | 4279–4285 | 4368–4374 | Types | +1 | −1 |
| 126 | 4364–4370 | 4453–4459 | Types | +1 | −1 |
| 127 | 4380–4386 | 4469–4475 | Types | +1 | −1 |
| 128 | 4411–4417 | 4500–4506 | Types | +1 | −1 |
| 129 | 4483–4489 | 4572–4578 | Types | +1 | −1 |
| 130 | 4495–4503 | 4584–4592 | Types | +2 | −2 |
| 131 | 4541–4549 | 4630–4638 | Types | +2 | −2 |
| 132 | 4930–5324 | 5019–5413 | Client | +98 | −98 |
| 133 | 5390–5398 | 5479–5487 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- sap.s4hana.api_sales_order_srv/old/ballerinax_sap.s4hana.api_sales_order_srv.bal.txt	2026-08-12 12:57:30
+++ sap.s4hana.api_sales_order_srv/new/ballerinax_sap.s4hana.api_sales_order_srv.bal.txt	2026-08-12 13:19:19
@@ -122,12 +122,16 @@
 
 
 type A_SlsOrderItemBillingPlanItem record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Billing/Invoicing Plan Number
+    @constraint:String {maxLength: 10}
     string BillingPlan?;
     # Item for billing plan/invoice plan/payment cards
+    @constraint:String {maxLength: 6}
     string BillingPlanItem?;
     string? BillingPlanDateCategory?;
     string? BillingPlanBillingDate?;
@@ -170,10 +174,13 @@
 
 
 type A_SalesOrderItemBillingPlan record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Billing/Invoicing Plan Number
+    @constraint:String {maxLength: 10}
     string BillingPlan?;
     # Indicator for Billing Plan on Header
     boolean? BillingPlanIsInHeader?;
@@ -205,6 +212,7 @@
 
 
 type A_SalesOrder record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     string? SalesOrderType?;
     # Language key for sales document type
@@ -351,8 +359,10 @@
 
 
 type A_SalesOrderBillingPlan record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Billing/Invoicing Plan Number
+    @constraint:String {maxLength: 10}
     string BillingPlan?;
     # Start Date of Billing/Invoicing Plan
     string? BillingPlanStartDate?;
@@ -381,10 +391,13 @@
 
 
 type A_SalesOrderBillingPlanItem record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Billing/Invoicing Plan Number
+    @constraint:String {maxLength: 10}
     string BillingPlan?;
     # Item for billing plan/invoice plan/payment cards
+    @constraint:String {maxLength: 6}
     string BillingPlanItem?;
     string? BillingPlanDateCategory?;
     string? BillingPlanBillingDate?;
@@ -431,8 +444,10 @@
 
 
 type A_SalesOrderItem record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -615,9 +630,12 @@
 
 
 type A_SalesOrderItemPartner record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     string? PartnerFunctionInternalCode?;
     # Customer Number
@@ -645,11 +663,15 @@
 
 type A_SalesOrderItemPartnerAddress record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Item number of the SD document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Version ID for International Addresses
+    @constraint:String {maxLength: 1}
     string AddressRepresentationCode?;
     string? CorrespondenceLanguage?;
     # Full Name of Person
@@ -710,8 +732,10 @@
 
 type A_SalesOrderItmPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Subsequent Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -747,11 +771,15 @@
 
 
 type A_SalesOrderItemPrElement record {
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
     # Timestamp for Pricing
@@ -835,10 +863,13 @@
 
 
 type A_SalesOrderItemRelatedObject record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # Sequence Number of the Related Object of an SD Document
+    @constraint:String {maxLength: 4}
     string SDDocRelatedObjectSequenceNmbr?;
     # Type of the Related Object of an SD Document
     string? SDDocumentRelatedObjectType?;
@@ -859,8 +890,11 @@
 
 
 type A_SalesOrderScheduleLine record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 4}
     string ScheduleLine?;
     # Requested Delivery Date
     string? RequestedDeliveryDate?;
@@ -891,8 +925,10 @@
 
 type A_SalesOrderItmSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Preceding Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -934,10 +970,14 @@
 
 
 type A_SalesOrderItemText record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string? LongText?;
     A_SalesOrder to_SalesOrder?;
@@ -951,7 +991,9 @@
 
 
 type A_SalesOrderHeaderPartner record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     string? PartnerFunctionInternalCode?;
     # Customer Number
@@ -978,9 +1020,12 @@
 
 type A_SalesOrderPartnerAddress record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string PartnerFunction?;
     # Version ID for International Addresses
+    @constraint:String {maxLength: 1}
     string AddressRepresentationCode?;
     string? CorrespondenceLanguage?;
     # Full Name of Person
@@ -1039,8 +1084,10 @@
 
 
 type A_SlsOrdPaymentPlanItemDetails record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Item for billing plan/invoice plan/payment cards
+    @constraint:String {maxLength: 6}
     string PaymentPlanItem?;
     # Billing Plan Number / Invoicing Plan Number
     string? PaymentPlan?;
@@ -1109,6 +1156,7 @@
 
 type A_SalesOrderPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -1136,9 +1184,12 @@
 
 
 type A_SalesOrderHeaderPrElement record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep?;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter?;
     string? ConditionType?;
     # Timestamp for Pricing
@@ -1217,8 +1268,10 @@
 
 
 type A_SalesOrderRelatedObject record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # Sequence Number of the Related Object of an SD Document
+    @constraint:String {maxLength: 4}
     string SDDocRelatedObjectSequenceNmbr?;
     # Type of the Related Object of an SD Document
     string? SDDocumentRelatedObjectType?;
@@ -1239,6 +1292,7 @@
 
 type A_SalesOrderSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID?;
@@ -1266,8 +1320,11 @@
 
 
 type A_SalesOrderText record {
+    @constraint:String {maxLength: 10}
     string SalesOrder?;
+    @constraint:String {maxLength: 2}
     string Language?;
+    @constraint:String {maxLength: 4}
     string LongTextID?;
     string? LongText?;
     A_SalesOrder to_SalesOrder?;
@@ -1283,7 +1340,7 @@
     string? LongText?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPrElementExpandOptions
+type SalesOrderOfA_SalesOrderItemPrElementExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listSubsequentProcFlowDocsOfA_SalesOrder
 
@@ -1304,11 +1361,11 @@
     SubsequentProcFlowDocOfA_SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesOrderOrderByOptions
+type SubsequentProcFlowDocOfA_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesOrderExpandOptions
+type SubsequentProcFlowDocOfA_SalesOrderExpandOptions "to_SalesOrder"[];
 
-// Unknown type: SubsequentProcFlowDocOfA_SalesOrderSelectOptions
+type SubsequentProcFlowDocOfA_SalesOrderSelectOptions ("SalesOrder"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"OverallSDProcessStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder")[];
 
 
 type Modified\ A_SalesOrderItemPartnerAddressType record {
@@ -1368,6 +1425,7 @@
 
 type CreateA_SalesOrderSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1390,6 +1448,7 @@
 
 
 type CreateA_SalesOrder record {
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     string? SalesOrderType?;
     string? SalesOrganization?;
@@ -1539,6 +1598,7 @@
 
 type CreateA_SalesOrderItem record {
     # Sales Order Item
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # Higher-Level Item in Bill of Material Structures
     string? HigherLevelItem?;
@@ -1711,6 +1771,7 @@
 
 
 type CreateA_SalesOrderItemPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1735,11 +1796,15 @@
 
 type CreateA_SalesOrderItemPartnerAddress record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # Item number of the SD document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Version ID for International Addresses
+    @constraint:String {maxLength: 1}
     string AddressRepresentationCode;
     string? CorrespondenceLanguage?;
     # Full Name of Person
@@ -1800,8 +1865,10 @@
 
 type CreateA_SalesOrderItmPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # Subsequent Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1837,8 +1904,10 @@
 
 
 type CreateA_SalesOrderItemPrElement record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -1885,6 +1954,7 @@
 
 
 type CreateA_SalesOrderScheduleLine record {
+    @constraint:String {maxLength: 4}
     string ScheduleLine;
     # Requested Delivery Date
     string? RequestedDeliveryDate?;
@@ -1915,8 +1985,10 @@
 
 type CreateA_SalesOrderItmSubsqntProcFlow record {
     # Preceding sales and distribution document
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # Preceding Item of an SD Document
+    @constraint:String {maxLength: 6}
     string SalesOrderItem;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -1958,7 +2030,9 @@
 
 
 type CreateA_SalesOrderItemText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string? LongText?;
     CreateA_SalesOrder to_SalesOrder?;
@@ -1972,6 +2046,7 @@
 
 
 type CreateA_SalesOrderHeaderPartner record {
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Customer Number
     string? Customer?;
@@ -1995,9 +2070,12 @@
 
 type CreateA_SalesOrderPartnerAddress record {
     # Sales and Distribution Document Number
+    @constraint:String {maxLength: 10}
     string SalesOrder;
+    @constraint:String {maxLength: 2}
     string PartnerFunction;
     # Version ID for International Addresses
+    @constraint:String {maxLength: 1}
     string AddressRepresentationCode;
     string? CorrespondenceLanguage?;
     # Full Name of Person
@@ -2057,6 +2135,7 @@
 
 type CreateA_SlsOrdPaymentPlanItemDetails record {
     # Item for billing plan/invoice plan/payment cards
+    @constraint:String {maxLength: 6}
     string PaymentPlanItem;
     # Electronic Payment: Payment Type
     string? ElectronicPaymentType?;
@@ -2097,6 +2176,7 @@
 
 type CreateA_SalesOrderPrecdgProcFlow record {
     # Subsequent Sales and Distribution Document
+    @constraint:String {maxLength: 10}
     string SalesOrder;
     # SD Unique Document Relationship Identification
     string DocRelationshipUUID;
@@ -2124,8 +2204,10 @@
 
 
 type CreateA_SalesOrderHeaderPrElement record {
+    @constraint:String {maxLength: 3}
     string PricingProcedureStep;
     # Condition Counter
+    @constraint:String {maxLength: 3}
     string PricingProcedureCounter;
     string? ConditionType?;
     # Condition Amount or Percentage
@@ -2175,7 +2257,9 @@
 
 
 type CreateA_SalesOrderText record {
+    @constraint:String {maxLength: 2}
     string Language;
+    @constraint:String {maxLength: 4}
     string LongTextID;
     string? LongText?;
     CreateA_SalesOrder to_SalesOrder?;
@@ -2200,11 +2284,11 @@
     A_SalesOrderItemPrElementSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemPrElementOrderByOptions
+type A_SalesOrderItemPrElementOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
-// Unknown type: A_SalesOrderItemPrElementExpandOptions
+type A_SalesOrderItemPrElementExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SalesOrderItemPrElementSelectOptions
+type A_SalesOrderItemPrElementSelectOptions ("SalesOrder"|"SalesOrderItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type CollectionOfA_SalesOrderHeaderPartner record {
@@ -2212,7 +2296,8 @@
     A_SalesOrderHeaderPartner[] results?;
 };
 
-// Unknown type: count
+# The number of entities in the collection. Available when using the [$inlinecount](https://help.sap.com/doc/5890d27be418427993fafa6722cdc03b/Cloud/en-US/OdataV2.pdf#page=67) query option.
+type count string;
 
 # Represents the Queries record for the operation: getA_SalesOrderHeaderPartner
 
@@ -2223,11 +2308,11 @@
     A_SalesOrderHeaderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderHeaderPartnerExpandOptions
+type A_SalesOrderHeaderPartnerExpandOptions ("to_Address"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderHeaderPartnerSelectOptions
+type A_SalesOrderHeaderPartnerSelectOptions ("SalesOrder"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"AddressID"|"VATRegistration"|"to_Address"|"to_SalesOrder")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderHeaderPartnerExpandOptions
+type SalesOrderOfA_SalesOrderHeaderPartnerExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type A_SalesOrderBillingPlanWrapper record {
@@ -2239,7 +2324,7 @@
     A_SalesOrderItemPartner d?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowExpandOptions
+type SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type FunctionResult_1 record {
@@ -2256,9 +2341,9 @@
     boolean Boolean?;
 };
 
-// Unknown type: A_SalesOrderItmSubsqntProcFlowSelectOptions
+type A_SalesOrderItmSubsqntProcFlowSelectOptions ("SalesOrder"|"SalesOrderItem"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentItem"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"RelatedProcFlowDocStsFieldName"|"SDProcessStatus"|"AccountingTransferStatus"|"PrelimBillingDocumentStatus"|"SubsqntDocItmPrecdgDocument"|"SubsqntDocItmPrecdgDocItem"|"SubsqntDocItmPrecdgDocCategory"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: PricingElementOfA_SalesOrderSelectOptions
+type PricingElementOfA_SalesOrderSelectOptions ("SalesOrder"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesOrder")[];
 
 
 type A_SalesOrderItmPrecdgProcFlowWrapper record {
@@ -2275,14 +2360,14 @@
     FunctionResult releaseApprovalRequest?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderPartnerAddressSelectOptions
-
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions
+type SalesOrderOfA_SalesOrderPartnerAddressSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesOrderItemTextOrderByOptions
+type PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentItem"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"RelatedProcFlowDocStsFieldName"|"SDProcessStatus"|"AccountingTransferStatus"|"PrelimBillingDocumentStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SlsOrderItemBillingPlanItemSelectOptions
+type A_SalesOrderItemTextOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc")[];
 
+type A_SlsOrderItemBillingPlanItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"BillingPlan"|"BillingPlanItem"|"BillingPlanDateCategory"|"BillingPlanBillingDate"|"BillingPlanAmount"|"TransactionCurrency"|"BillingPlanAmountPercent"|"CustomerPaymentTerms"|"ProposedBillingDocumentType"|"BillingPlanDateDescriptionCode"|"BillingBlockReason"|"BillingPlanServiceStartDate"|"BillingPlanServiceEndDate"|"BillingPlanRelatedBillgStatus"|"BillingPlanType"|"AdoptingBillingDateID"|"BillingPlanBillingRule"|"BillingPlanMilestoneUsage"|"BillgPlnDteCorrectionRfndType"|"AccountingExchangeRate"|"PostponementReason"|"to_BillingPlan"|"to_SalesOrder"|"to_SalesOrderItem")[];
+
 # Represents the Queries record for the operation: listA_SalesOrderItemPartners
 
 type ListA_SalesOrderItemPartnersQueries record {
@@ -2302,11 +2387,11 @@
     A_SalesOrderItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemPartnerOrderByOptions
+type A_SalesOrderItemPartnerOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PartnerFunction"|"PartnerFunction desc"|"PartnerFunctionInternalCode"|"PartnerFunctionInternalCode desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"ReferenceBusinessPartner"|"ReferenceBusinessPartner desc"|"AddressID"|"AddressID desc"|"VATRegistration"|"VATRegistration desc")[];
 
-// Unknown type: A_SalesOrderItemPartnerExpandOptions
+type A_SalesOrderItemPartnerExpandOptions ("to_Address"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SalesOrderItemPartnerSelectOptions
+type A_SalesOrderItemPartnerSelectOptions ("SalesOrder"|"SalesOrderItem"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"AddressID"|"VATRegistration"|"to_Address"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderScheduleLine
 
@@ -2315,7 +2400,7 @@
     A_SalesOrderScheduleLineSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderScheduleLineSelectOptions
+type A_SalesOrderScheduleLineSelectOptions ("SalesOrder"|"SalesOrderItem"|"ScheduleLine"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ScheduleLineOrderQuantity"|"ConfdOrderQtyByMatlAvailCheck"|"DeliveredQtyInOrderQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit"|"CorrectedQtyInOrderQtyUnit"|"DelivBlockReasonForSchedLine")[];
 
 
 type UpdateA_SlsOrdPaymentPlanItemDetails record {
@@ -2349,9 +2434,9 @@
     string? MaximumToBeAuthorizedAmount?;
 };
 
-// Unknown type: BillingPlanOfA_SlsOrderItemBillingPlanItemExpandOptions
+type BillingPlanOfA_SlsOrderItemBillingPlanItemExpandOptions ("to_BillingPlanItem"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions
+type SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SlsOrdPaymentPlanItemDetails
 
@@ -2362,9 +2447,9 @@
     A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsOrdPaymentPlanItemDetailsExpandOptions
+type A_SlsOrdPaymentPlanItemDetailsExpandOptions "to_SalesOrder"[];
 
-// Unknown type: A_SlsOrdPaymentPlanItemDetailsSelectOptions
+type A_SlsOrdPaymentPlanItemDetailsSelectOptions ("SalesOrder"|"PaymentPlanItem"|"PaymentPlan"|"ElectronicPaymentType"|"ElectronicPayment"|"EPaytValidityStartDate"|"EPaytValidityEndDate"|"ElectronicPaymentHolderName"|"AuthorizedAmountInAuthznCrcy"|"AuthorizationCurrency"|"AuthorizationByDigitalPaytSrvc"|"AuthorizationByAcquirer"|"AuthorizationDate"|"AuthorizationTime"|"AuthorizationStatusName"|"EPaytByDigitalPaymentSrvc"|"ElectronicPaymentCallStatus"|"EPaytAuthorizationResult"|"EPaytToBeAuthorizedAmount"|"EPaytAuthorizationIsExpired"|"EPaytAmountIsChanged"|"PreauthorizationIsRequested"|"PaymentServiceProvider"|"PaymentByPaymentServicePrvdr"|"TransactionByPaytSrvcPrvdr"|"MerchantByClearingHouse"|"PaymentCardAuthznRelationID"|"MaximumToBeAuthorizedAmount"|"PaytPlnForAuthorizationItem"|"PaytPlnItmForAuthorizationItem"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getSalesOrderItemOfA_SalesOrderItemRelatedObject
 
@@ -2375,9 +2460,9 @@
     SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemRelatedObjectExpandOptions
+type SalesOrderItemOfA_SalesOrderItemRelatedObjectExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions
+type SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderPrecdgProcFlow
 
@@ -2388,9 +2473,9 @@
     SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderPrecdgProcFlowExpandOptions
+type SalesOrderOfA_SalesOrderPrecdgProcFlowExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions
+type SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrderItemBillingPlanWrapper record {
@@ -2403,7 +2488,7 @@
     A_SalesOrderItemBillingPlan[] results?;
 };
 
-// Unknown type: BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions
+type BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions ("SalesOrder"|"BillingPlan"|"BillingPlanItem"|"BillingPlanDateCategory"|"BillingPlanBillingDate"|"BillingPlanAmount"|"TransactionCurrency"|"BillingPlanAmountPercent"|"CustomerPaymentTerms"|"ProposedBillingDocumentType"|"BillingPlanDateDescriptionCode"|"BillingBlockReason"|"BillingPlanServiceStartDate"|"BillingPlanServiceEndDate"|"BillingPlanRelatedBillgStatus"|"BillingPlanType"|"AdoptingBillingDateID"|"BillingPlanBillingRule"|"BillingPlanMilestoneUsage"|"BillgPlnDteCorrectionRfndType"|"AccountingExchangeRate"|"PostponementReason"|"to_BillingPlan"|"to_SalesOrder")[];
 
 
 type CollectionOfA_SalesOrderRelatedObject record {
@@ -2428,17 +2513,17 @@
     ScheduleLineOfA_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: ScheduleLineOfA_SalesOrderItemOrderByOptions
+type ScheduleLineOfA_SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"ScheduleLine"|"ScheduleLine desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ConfirmedDeliveryDate"|"ConfirmedDeliveryDate desc"|"OrderQuantityUnit"|"OrderQuantityUnit desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"ScheduleLineOrderQuantity"|"ScheduleLineOrderQuantity desc"|"ConfdOrderQtyByMatlAvailCheck"|"ConfdOrderQtyByMatlAvailCheck desc"|"DeliveredQtyInOrderQtyUnit"|"DeliveredQtyInOrderQtyUnit desc"|"OpenConfdDelivQtyInOrdQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit desc"|"CorrectedQtyInOrderQtyUnit"|"CorrectedQtyInOrderQtyUnit desc"|"DelivBlockReasonForSchedLine"|"DelivBlockReasonForSchedLine desc")[];
 
-// Unknown type: ScheduleLineOfA_SalesOrderItemSelectOptions
+type ScheduleLineOfA_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"ScheduleLine"|"RequestedDeliveryDate"|"ConfirmedDeliveryDate"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ScheduleLineOrderQuantity"|"ConfdOrderQtyByMatlAvailCheck"|"DeliveredQtyInOrderQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit"|"CorrectedQtyInOrderQtyUnit"|"DelivBlockReasonForSchedLine")[];
 
-// Unknown type: A_SlsOrderItemBillingPlanItemOrderByOptions
+type A_SlsOrderItemBillingPlanItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanItem"|"BillingPlanItem desc"|"BillingPlanDateCategory"|"BillingPlanDateCategory desc"|"BillingPlanBillingDate"|"BillingPlanBillingDate desc"|"BillingPlanAmount"|"BillingPlanAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"BillingPlanAmountPercent"|"BillingPlanAmountPercent desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"ProposedBillingDocumentType"|"ProposedBillingDocumentType desc"|"BillingPlanDateDescriptionCode"|"BillingPlanDateDescriptionCode desc"|"BillingBlockReason"|"BillingBlockReason desc"|"BillingPlanServiceStartDate"|"BillingPlanServiceStartDate desc"|"BillingPlanServiceEndDate"|"BillingPlanServiceEndDate desc"|"BillingPlanRelatedBillgStatus"|"BillingPlanRelatedBillgStatus desc"|"BillingPlanType"|"BillingPlanType desc"|"AdoptingBillingDateID"|"AdoptingBillingDateID desc"|"BillingPlanBillingRule"|"BillingPlanBillingRule desc"|"BillingPlanMilestoneUsage"|"BillingPlanMilestoneUsage desc"|"BillgPlnDteCorrectionRfndType"|"BillgPlnDteCorrectionRfndType desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"PostponementReason"|"PostponementReason desc")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItemBillingPlanSelectOptions
+type SalesOrderOfA_SalesOrderItemBillingPlanSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderSubsqntProcFlowSelectOptions
+type SalesOrderOfA_SalesOrderSubsqntProcFlowSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItmSubsqntProcFlowExpandOptions
+type SalesOrderOfA_SalesOrderItmSubsqntProcFlowExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SlsOrdPaymentPlanItemDetails
 
@@ -2459,9 +2544,9 @@
     A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsOrdPaymentPlanItemDetailsOrderByOptions
+type A_SlsOrdPaymentPlanItemDetailsOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PaymentPlanItem"|"PaymentPlanItem desc"|"PaymentPlan"|"PaymentPlan desc"|"ElectronicPaymentType"|"ElectronicPaymentType desc"|"ElectronicPayment"|"ElectronicPayment desc"|"EPaytValidityStartDate"|"EPaytValidityStartDate desc"|"EPaytValidityEndDate"|"EPaytValidityEndDate desc"|"ElectronicPaymentHolderName"|"ElectronicPaymentHolderName desc"|"AuthorizedAmountInAuthznCrcy"|"AuthorizedAmountInAuthznCrcy desc"|"AuthorizationCurrency"|"AuthorizationCurrency desc"|"AuthorizationByDigitalPaytSrvc"|"AuthorizationByDigitalPaytSrvc desc"|"AuthorizationByAcquirer"|"AuthorizationByAcquirer desc"|"AuthorizationDate"|"AuthorizationDate desc"|"AuthorizationTime"|"AuthorizationTime desc"|"AuthorizationStatusName"|"AuthorizationStatusName desc"|"EPaytByDigitalPaymentSrvc"|"EPaytByDigitalPaymentSrvc desc"|"ElectronicPaymentCallStatus"|"ElectronicPaymentCallStatus desc"|"EPaytAuthorizationResult"|"EPaytAuthorizationResult desc"|"EPaytToBeAuthorizedAmount"|"EPaytToBeAuthorizedAmount desc"|"EPaytAuthorizationIsExpired"|"EPaytAuthorizationIsExpired desc"|"EPaytAmountIsChanged"|"EPaytAmountIsChanged desc"|"PreauthorizationIsRequested"|"PreauthorizationIsRequested desc"|"PaymentServiceProvider"|"PaymentServiceProvider desc"|"PaymentByPaymentServicePrvdr"|"PaymentByPaymentServicePrvdr desc"|"TransactionByPaytSrvcPrvdr"|"TransactionByPaytSrvcPrvdr desc"|"MerchantByClearingHouse"|"MerchantByClearingHouse desc"|"PaymentCardAuthznRelationID"|"PaymentCardAuthznRelationID desc"|"MaximumToBeAuthorizedAmount"|"MaximumToBeAuthorizedAmount desc"|"PaytPlnForAuthorizationItem"|"PaytPlnForAuthorizationItem desc"|"PaytPlnItmForAuthorizationItem"|"PaytPlnItmForAuthorizationItem desc")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderRelatedObjectExpandOptions
+type SalesOrderOfA_SalesOrderRelatedObjectExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderText
 
@@ -2472,9 +2557,9 @@
     SalesOrderOfA_SalesOrderTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderTextExpandOptions
+type SalesOrderOfA_SalesOrderTextExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderTextSelectOptions
+type SalesOrderOfA_SalesOrderTextSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderBillingPlans
 
@@ -2495,13 +2580,13 @@
     A_SalesOrderBillingPlanSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderBillingPlanOrderByOptions
+type A_SalesOrderBillingPlanOrderByOptions ("SalesOrder"|"SalesOrder desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanStartDate"|"BillingPlanStartDate desc"|"BillingPlanStartDateRule"|"BillingPlanStartDateRule desc"|"ReferenceBillingPlan"|"ReferenceBillingPlan desc"|"BillingPlanCategory"|"BillingPlanCategory desc"|"BillingPlanType"|"BillingPlanType desc"|"BillingPlanEndDate"|"BillingPlanEndDate desc"|"BillingPlanEndDateRule"|"BillingPlanEndDateRule desc"|"BillingPlanSearchTerm"|"BillingPlanSearchTerm desc")[];
 
-// Unknown type: A_SalesOrderBillingPlanExpandOptions
+type A_SalesOrderBillingPlanExpandOptions ("to_BillingPlanItem"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderBillingPlanSelectOptions
+type A_SalesOrderBillingPlanSelectOptions ("SalesOrder"|"BillingPlan"|"BillingPlanStartDate"|"BillingPlanStartDateRule"|"ReferenceBillingPlan"|"BillingPlanCategory"|"BillingPlanType"|"BillingPlanEndDate"|"BillingPlanEndDateRule"|"BillingPlanSearchTerm"|"to_BillingPlanItem"|"to_SalesOrder")[];
 
-// Unknown type: BillingPlanItemOfA_SalesOrderItemBillingPlanOrderByOptions
+type BillingPlanItemOfA_SalesOrderItemBillingPlanOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanItem"|"BillingPlanItem desc"|"BillingPlanDateCategory"|"BillingPlanDateCategory desc"|"BillingPlanBillingDate"|"BillingPlanBillingDate desc"|"BillingPlanAmount"|"BillingPlanAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"BillingPlanAmountPercent"|"BillingPlanAmountPercent desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"ProposedBillingDocumentType"|"ProposedBillingDocumentType desc"|"BillingPlanDateDescriptionCode"|"BillingPlanDateDescriptionCode desc"|"BillingBlockReason"|"BillingBlockReason desc"|"BillingPlanServiceStartDate"|"BillingPlanServiceStartDate desc"|"BillingPlanServiceEndDate"|"BillingPlanServiceEndDate desc"|"BillingPlanRelatedBillgStatus"|"BillingPlanRelatedBillgStatus desc"|"BillingPlanType"|"BillingPlanType desc"|"AdoptingBillingDateID"|"AdoptingBillingDateID desc"|"BillingPlanBillingRule"|"BillingPlanBillingRule desc"|"BillingPlanMilestoneUsage"|"BillingPlanMilestoneUsage desc"|"BillgPlnDteCorrectionRfndType"|"BillgPlnDteCorrectionRfndType desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"PostponementReason"|"PostponementReason desc")[];
 
 # Provides settings related to HTTP/1.x protocol.
 
@@ -2524,10 +2609,11 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
-// Unknown type: A_SalesOrderPrecdgProcFlowExpandOptions
+type A_SalesOrderPrecdgProcFlowExpandOptions "to_SalesOrder"[];
 
 # Represents the Queries record for the operation: getA_SalesOrderBillingPlan
 
@@ -2547,7 +2633,7 @@
     A_SalesOrderPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderPrecdgProcFlowSelectOptions
+type A_SalesOrderPrecdgProcFlowSelectOptions ("SalesOrder"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"OverallSDProcessStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: listA_SlsOrderItemBillingPlanItems
 
@@ -2568,7 +2654,7 @@
     A_SlsOrderItemBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SlsOrderItemBillingPlanItemExpandOptions
+type A_SlsOrderItemBillingPlanItemExpandOptions ("to_BillingPlan"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type CollectionOfA_SalesOrderPrecdgProcFlowWrapper record {
@@ -2590,9 +2676,9 @@
     A_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemExpandOptions
+type A_SalesOrderItemExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: A_SalesOrderItemSelectOptions
+type A_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SlsOrderItemBillingPlanItem
 
@@ -2603,9 +2689,9 @@
     SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SlsOrderItemBillingPlanItemExpandOptions
+type SalesOrderOfA_SlsOrderItemBillingPlanItemExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions
+type SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderBillingPlanItem
 
@@ -2616,9 +2702,9 @@
     SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderBillingPlanItemExpandOptions
+type SalesOrderOfA_SalesOrderBillingPlanItemExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions
+type SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type UpdateA_SalesOrder record {
@@ -2717,9 +2803,9 @@
     string? ServicesRenderedDate?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderHeaderPrElementExpandOptions
+type SalesOrderOfA_SalesOrderHeaderPrElementExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: PartnerOfA_SalesOrderPartnerAddressSelectOptions
+type PartnerOfA_SalesOrderPartnerAddressSelectOptions ("SalesOrder"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"AddressID"|"VATRegistration"|"to_Address"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderItemText
 
@@ -2730,11 +2816,11 @@
     SalesOrderOfA_SalesOrderItemTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemTextExpandOptions
+type SalesOrderOfA_SalesOrderItemTextExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItemTextSelectOptions
+type SalesOrderOfA_SalesOrderItemTextSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesOrderTextOrderByOptions
+type A_SalesOrderTextOrderByOptions ("SalesOrder"|"SalesOrder desc"|"Language"|"Language desc"|"LongTextID"|"LongTextID desc")[];
 
 
 type CollectionOfA_SalesOrderPartnerAddressWrapper record {
@@ -2756,13 +2842,13 @@
     SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItmPrecdgProcFlowExpandOptions
+type SalesOrderOfA_SalesOrderItmPrecdgProcFlowExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions
+type SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: AddressOfA_SalesOrderHeaderPartnerOrderByOptions
+type AddressOfA_SalesOrderHeaderPartnerOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PartnerFunction"|"PartnerFunction desc"|"AddressRepresentationCode"|"AddressRepresentationCode desc"|"CorrespondenceLanguage"|"CorrespondenceLanguage desc"|"AddresseeFullName"|"AddresseeFullName desc"|"OrganizationName1"|"OrganizationName1 desc"|"OrganizationName2"|"OrganizationName2 desc"|"OrganizationName3"|"OrganizationName3 desc"|"OrganizationName4"|"OrganizationName4 desc"|"CityName"|"CityName desc"|"DistrictName"|"DistrictName desc"|"PostalCode"|"PostalCode desc"|"StreetPrefixName1"|"StreetPrefixName1 desc"|"StreetPrefixName2"|"StreetPrefixName2 desc"|"StreetName"|"StreetName desc"|"StreetSuffixName1"|"StreetSuffixName1 desc"|"StreetSuffixName2"|"StreetSuffixName2 desc"|"HouseNumber"|"HouseNumber desc"|"Country"|"Country desc"|"Region"|"Region desc"|"FormOfAddress"|"FormOfAddress desc"|"TaxJurisdiction"|"TaxJurisdiction desc"|"TransportZone"|"TransportZone desc"|"POBox"|"POBox desc"|"POBoxPostalCode"|"POBoxPostalCode desc"|"EmailAddress"|"EmailAddress desc"|"MobilePhoneCountry"|"MobilePhoneCountry desc"|"MobileNumber"|"MobileNumber desc"|"PhoneNumberCountry"|"PhoneNumberCountry desc"|"PhoneNumber"|"PhoneNumber desc"|"PhoneExtensionNumber"|"PhoneExtensionNumber desc"|"FaxNumberCountry"|"FaxNumberCountry desc"|"FaxAreaCodeSubscriberNumber"|"FaxAreaCodeSubscriberNumber desc"|"FaxExtensionNumber"|"FaxExtensionNumber desc")[];
 
-// Unknown type: SalesOrderOfA_SlsOrdPaymentPlanItemDetailsExpandOptions
+type SalesOrderOfA_SlsOrdPaymentPlanItemDetailsExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderBillingPlanItem
 
@@ -2773,9 +2859,9 @@
     A_SalesOrderBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderBillingPlanItemExpandOptions
+type A_SalesOrderBillingPlanItemExpandOptions ("to_BillingPlan"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderBillingPlanItemSelectOptions
+type A_SalesOrderBillingPlanItemSelectOptions ("SalesOrder"|"BillingPlan"|"BillingPlanItem"|"BillingPlanDateCategory"|"BillingPlanBillingDate"|"BillingPlanAmount"|"TransactionCurrency"|"BillingPlanAmountPercent"|"CustomerPaymentTerms"|"ProposedBillingDocumentType"|"BillingPlanDateDescriptionCode"|"BillingBlockReason"|"BillingPlanServiceStartDate"|"BillingPlanServiceEndDate"|"BillingPlanRelatedBillgStatus"|"BillingPlanType"|"AdoptingBillingDateID"|"BillingPlanBillingRule"|"BillingPlanMilestoneUsage"|"BillgPlnDteCorrectionRfndType"|"AccountingExchangeRate"|"PostponementReason"|"to_BillingPlan"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderItemPartner
 
@@ -2805,7 +2891,7 @@
     A_SalesOrderBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderBillingPlanItemOrderByOptions
+type A_SalesOrderBillingPlanItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanItem"|"BillingPlanItem desc"|"BillingPlanDateCategory"|"BillingPlanDateCategory desc"|"BillingPlanBillingDate"|"BillingPlanBillingDate desc"|"BillingPlanAmount"|"BillingPlanAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"BillingPlanAmountPercent"|"BillingPlanAmountPercent desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"ProposedBillingDocumentType"|"ProposedBillingDocumentType desc"|"BillingPlanDateDescriptionCode"|"BillingPlanDateDescriptionCode desc"|"BillingBlockReason"|"BillingBlockReason desc"|"BillingPlanServiceStartDate"|"BillingPlanServiceStartDate desc"|"BillingPlanServiceEndDate"|"BillingPlanServiceEndDate desc"|"BillingPlanRelatedBillgStatus"|"BillingPlanRelatedBillgStatus desc"|"BillingPlanType"|"BillingPlanType desc"|"AdoptingBillingDateID"|"AdoptingBillingDateID desc"|"BillingPlanBillingRule"|"BillingPlanBillingRule desc"|"BillingPlanMilestoneUsage"|"BillingPlanMilestoneUsage desc"|"BillgPlnDteCorrectionRfndType"|"BillgPlnDteCorrectionRfndType desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"PostponementReason"|"PostponementReason desc")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderSubsqntProcFlows
 
@@ -2826,12 +2912,12 @@
     A_SalesOrderSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderSubsqntProcFlowOrderByOptions
+type A_SalesOrderSubsqntProcFlowOrderByOptions ("SalesOrder"|"SalesOrder desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
+
+type A_SalesOrderSubsqntProcFlowExpandOptions "to_SalesOrder"[];
 
-// Unknown type: A_SalesOrderSubsqntProcFlowExpandOptions
+type A_SalesOrderSubsqntProcFlowSelectOptions ("SalesOrder"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"OverallSDProcessStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderSubsqntProcFlowSelectOptions
-
 # Represents the Queries record for the operation: listPaymentPlanItemDetailsOfA_SalesOrder
 
 type ListPaymentPlanItemDetailsOfA_SalesOrderQueries record {
@@ -2851,13 +2937,13 @@
     PaymentPlanItemDetailsOfA_SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: PaymentPlanItemDetailsOfA_SalesOrderOrderByOptions
+type PaymentPlanItemDetailsOfA_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PaymentPlanItem"|"PaymentPlanItem desc"|"PaymentPlan"|"PaymentPlan desc"|"ElectronicPaymentType"|"ElectronicPaymentType desc"|"ElectronicPayment"|"ElectronicPayment desc"|"EPaytValidityStartDate"|"EPaytValidityStartDate desc"|"EPaytValidityEndDate"|"EPaytValidityEndDate desc"|"ElectronicPaymentHolderName"|"ElectronicPaymentHolderName desc"|"AuthorizedAmountInAuthznCrcy"|"AuthorizedAmountInAuthznCrcy desc"|"AuthorizationCurrency"|"AuthorizationCurrency desc"|"AuthorizationByDigitalPaytSrvc"|"AuthorizationByDigitalPaytSrvc desc"|"AuthorizationByAcquirer"|"AuthorizationByAcquirer desc"|"AuthorizationDate"|"AuthorizationDate desc"|"AuthorizationTime"|"AuthorizationTime desc"|"AuthorizationStatusName"|"AuthorizationStatusName desc"|"EPaytByDigitalPaymentSrvc"|"EPaytByDigitalPaymentSrvc desc"|"ElectronicPaymentCallStatus"|"ElectronicPaymentCallStatus desc"|"EPaytAuthorizationResult"|"EPaytAuthorizationResult desc"|"EPaytToBeAuthorizedAmount"|"EPaytToBeAuthorizedAmount desc"|"EPaytAuthorizationIsExpired"|"EPaytAuthorizationIsExpired desc"|"EPaytAmountIsChanged"|"EPaytAmountIsChanged desc"|"PreauthorizationIsRequested"|"PreauthorizationIsRequested desc"|"PaymentServiceProvider"|"PaymentServiceProvider desc"|"PaymentByPaymentServicePrvdr"|"PaymentByPaymentServicePrvdr desc"|"TransactionByPaytSrvcPrvdr"|"TransactionByPaytSrvcPrvdr desc"|"MerchantByClearingHouse"|"MerchantByClearingHouse desc"|"PaymentCardAuthznRelationID"|"PaymentCardAuthznRelationID desc"|"MaximumToBeAuthorizedAmount"|"MaximumToBeAuthorizedAmount desc"|"PaytPlnForAuthorizationItem"|"PaytPlnForAuthorizationItem desc"|"PaytPlnItmForAuthorizationItem"|"PaytPlnItmForAuthorizationItem desc")[];
 
-// Unknown type: PaymentPlanItemDetailsOfA_SalesOrderExpandOptions
+type PaymentPlanItemDetailsOfA_SalesOrderExpandOptions "to_SalesOrder"[];
 
-// Unknown type: PaymentPlanItemDetailsOfA_SalesOrderSelectOptions
+type PaymentPlanItemDetailsOfA_SalesOrderSelectOptions ("SalesOrder"|"PaymentPlanItem"|"PaymentPlan"|"ElectronicPaymentType"|"ElectronicPayment"|"EPaytValidityStartDate"|"EPaytValidityEndDate"|"ElectronicPaymentHolderName"|"AuthorizedAmountInAuthznCrcy"|"AuthorizationCurrency"|"AuthorizationByDigitalPaytSrvc"|"AuthorizationByAcquirer"|"AuthorizationDate"|"AuthorizationTime"|"AuthorizationStatusName"|"EPaytByDigitalPaymentSrvc"|"ElectronicPaymentCallStatus"|"EPaytAuthorizationResult"|"EPaytToBeAuthorizedAmount"|"EPaytAuthorizationIsExpired"|"EPaytAmountIsChanged"|"PreauthorizationIsRequested"|"PaymentServiceProvider"|"PaymentByPaymentServicePrvdr"|"TransactionByPaytSrvcPrvdr"|"MerchantByClearingHouse"|"PaymentCardAuthznRelationID"|"MaximumToBeAuthorizedAmount"|"PaytPlnForAuthorizationItem"|"PaytPlnItmForAuthorizationItem"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderItemPartnerAddressOrderByOptions
+type A_SalesOrderItemPartnerAddressOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PartnerFunction"|"PartnerFunction desc"|"AddressRepresentationCode"|"AddressRepresentationCode desc"|"CorrespondenceLanguage"|"CorrespondenceLanguage desc"|"AddresseeFullName"|"AddresseeFullName desc"|"OrganizationName1"|"OrganizationName1 desc"|"OrganizationName2"|"OrganizationName2 desc"|"OrganizationName3"|"OrganizationName3 desc"|"OrganizationName4"|"OrganizationName4 desc"|"CityName"|"CityName desc"|"DistrictName"|"DistrictName desc"|"PostalCode"|"PostalCode desc"|"StreetName"|"StreetName desc"|"StreetPrefixName1"|"StreetPrefixName1 desc"|"StreetPrefixName2"|"StreetPrefixName2 desc"|"StreetSuffixName1"|"StreetSuffixName1 desc"|"StreetSuffixName2"|"StreetSuffixName2 desc"|"HouseNumber"|"HouseNumber desc"|"Country"|"Country desc"|"Region"|"Region desc"|"FormOfAddress"|"FormOfAddress desc"|"TaxJurisdiction"|"TaxJurisdiction desc"|"TransportZone"|"TransportZone desc"|"POBox"|"POBox desc"|"POBoxPostalCode"|"POBoxPostalCode desc"|"EmailAddress"|"EmailAddress desc"|"MobilePhoneCountry"|"MobilePhoneCountry desc"|"MobileNumber"|"MobileNumber desc"|"PhoneNumberCountry"|"PhoneNumberCountry desc"|"PhoneNumber"|"PhoneNumber desc"|"PhoneExtensionNumber"|"PhoneExtensionNumber desc"|"FaxNumberCountry"|"FaxNumberCountry desc"|"FaxAreaCodeSubscriberNumber"|"FaxAreaCodeSubscriberNumber desc"|"FaxExtensionNumber"|"FaxExtensionNumber desc")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderPartnerAddress
 
@@ -2868,9 +2954,9 @@
     A_SalesOrderPartnerAddressSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderPartnerAddressExpandOptions
+type A_SalesOrderPartnerAddressExpandOptions ("to_Partner"|"to_SalesOrder")[];
 
-// Unknown type: A_SalesOrderPartnerAddressSelectOptions
+type A_SalesOrderPartnerAddressSelectOptions ("SalesOrder"|"PartnerFunction"|"AddressRepresentationCode"|"CorrespondenceLanguage"|"AddresseeFullName"|"OrganizationName1"|"OrganizationName2"|"OrganizationName3"|"OrganizationName4"|"CityName"|"DistrictName"|"PostalCode"|"StreetPrefixName1"|"StreetPrefixName2"|"StreetName"|"StreetSuffixName1"|"StreetSuffixName2"|"HouseNumber"|"Country"|"Region"|"FormOfAddress"|"TaxJurisdiction"|"TransportZone"|"POBox"|"POBoxPostalCode"|"EmailAddress"|"MobilePhoneCountry"|"MobileNumber"|"PhoneNumberCountry"|"PhoneNumber"|"PhoneExtensionNumber"|"FaxNumberCountry"|"FaxAreaCodeSubscriberNumber"|"FaxExtensionNumber"|"to_Partner"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderHeaderPrElement
 
@@ -2881,9 +2967,9 @@
     A_SalesOrderHeaderPrElementSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderHeaderPrElementExpandOptions
+type A_SalesOrderHeaderPrElementExpandOptions "to_SalesOrder"[];
 
-// Unknown type: A_SalesOrderHeaderPrElementSelectOptions
+type A_SalesOrderHeaderPrElementSelectOptions ("SalesOrder"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: listPricingElementsOfA_SalesOrderItem
 
@@ -2904,13 +2990,13 @@
     PricingElementOfA_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: PricingElementOfA_SalesOrderItemOrderByOptions
+type PricingElementOfA_SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"IsRelevantForAccrual"|"IsRelevantForAccrual desc"|"CndnIsRelevantForInvoiceList"|"CndnIsRelevantForInvoiceList desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
-// Unknown type: PricingElementOfA_SalesOrderItemExpandOptions
+type PricingElementOfA_SalesOrderItemExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: PricingElementOfA_SalesOrderItemSelectOptions
+type PricingElementOfA_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"PricingProcedureStep"|"PricingProcedureCounter"|"ConditionType"|"PricingDateTime"|"PriceConditionDeterminationDte"|"ConditionCalculationType"|"ConditionBaseValue"|"ConditionRateValue"|"ConditionCurrency"|"ConditionQuantity"|"ConditionQuantityUnit"|"ConditionQuantitySAPUnit"|"ConditionQuantityISOUnit"|"ConditionCategory"|"ConditionIsForStatistics"|"PricingScaleType"|"IsRelevantForAccrual"|"CndnIsRelevantForInvoiceList"|"ConditionOrigin"|"IsGroupCondition"|"ConditionRecord"|"ConditionSequentialNumber"|"TaxCode"|"WithholdingTaxCode"|"CndnRoundingOffDiffAmount"|"ConditionAmount"|"TransactionCurrency"|"ConditionControl"|"ConditionInactiveReason"|"ConditionClass"|"PrcgProcedureCounterForHeader"|"FactorForConditionBasisValue"|"StructureCondition"|"PeriodFactorForCndnBasisValue"|"PricingScaleBasis"|"ConditionScaleBasisValue"|"ConditionScaleBasisUnit"|"ConditionScaleBasisCurrency"|"CndnIsRelevantForIntcoBilling"|"ConditionIsManuallyChanged"|"ConditionIsForConfiguration"|"VariantCondition"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPartnerAddressExpandOptions
+type SalesOrderItemOfA_SalesOrderItemPartnerAddressExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type A_SalesOrderHeaderPartnerWrapper record {
@@ -2926,14 +3012,14 @@
     SalesOrderOfA_SalesOrderPartnerAddressSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderPartnerAddressExpandOptions
+type SalesOrderOfA_SalesOrderPartnerAddressExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type A_SalesOrderItemRelatedObjectWrapper record {
     A_SalesOrderItemRelatedObject d?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderBillingPlanSelectOptions
+type SalesOrderOfA_SalesOrderBillingPlanSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderItem
 
@@ -2944,9 +3030,9 @@
     SalesOrderOfA_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemExpandOptions
+type SalesOrderOfA_SalesOrderItemExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItemSelectOptions
+type SalesOrderOfA_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrderItemRelatedObject record {
@@ -2984,7 +3070,7 @@
     SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowExpandOptions
+type SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type UpdateA_SalesOrderItem record {
@@ -3114,7 +3200,7 @@
     A_SalesOrder[] results?;
 };
 
-// Unknown type: A_SalesOrderScheduleLineOrderByOptions
+type A_SalesOrderScheduleLineOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"ScheduleLine"|"ScheduleLine desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ConfirmedDeliveryDate"|"ConfirmedDeliveryDate desc"|"OrderQuantityUnit"|"OrderQuantityUnit desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"ScheduleLineOrderQuantity"|"ScheduleLineOrderQuantity desc"|"ConfdOrderQtyByMatlAvailCheck"|"ConfdOrderQtyByMatlAvailCheck desc"|"DeliveredQtyInOrderQtyUnit"|"DeliveredQtyInOrderQtyUnit desc"|"OpenConfdDelivQtyInOrdQtyUnit"|"OpenConfdDelivQtyInOrdQtyUnit desc"|"CorrectedQtyInOrderQtyUnit"|"CorrectedQtyInOrderQtyUnit desc"|"DelivBlockReasonForSchedLine"|"DelivBlockReasonForSchedLine desc")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderHeaderPrElement
 
@@ -3125,9 +3211,9 @@
     SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions
+type SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesOrderItemOrderByOptions
+type PrecedingProcFlowDocItemOfA_SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentItem"|"PrecedingDocumentItem desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 # Represents the Queries record for the operation: getSalesOrderItemOfA_SlsOrderItemBillingPlanItem
 
@@ -3138,9 +3224,9 @@
     SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SlsOrderItemBillingPlanItemExpandOptions
+type SalesOrderItemOfA_SlsOrderItemBillingPlanItemExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions
+type SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type UpdateA_SalesOrderBillingPlan record {
@@ -3171,7 +3257,7 @@
     A_SalesOrderHeaderPrElementSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderHeaderPrElementOrderByOptions
+type A_SalesOrderHeaderPrElementOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderItmSubsqntProcFlow
 
@@ -3182,7 +3268,7 @@
     A_SalesOrderItmSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItmSubsqntProcFlowExpandOptions
+type A_SalesOrderItmSubsqntProcFlowExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: listRelatedObjectsOfA_SalesOrderItem
 
@@ -3203,13 +3289,13 @@
     A_SalesOrderItemRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemRelatedObjectOrderByOptions
+type A_SalesOrderItemRelatedObjectOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"SDDocRelatedObjectSequenceNmbr"|"SDDocRelatedObjectSequenceNmbr desc"|"SDDocumentRelatedObjectType"|"SDDocumentRelatedObjectType desc"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectSystem desc"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference1 desc"|"SDDocRelatedObjectReference2"|"SDDocRelatedObjectReference2 desc")[];
 
-// Unknown type: A_SalesOrderItemRelatedObjectExpandOptions
+type A_SalesOrderItemRelatedObjectExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SalesOrderItemRelatedObjectSelectOptions
+type A_SalesOrderItemRelatedObjectSelectOptions ("SalesOrder"|"SalesOrderItem"|"SDDocRelatedObjectSequenceNmbr"|"SDDocumentRelatedObjectType"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference2"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemTextExpandOptions
+type SalesOrderItemOfA_SalesOrderItemTextExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type UpdateA_SalesOrderBillingPlanItem record {
@@ -3238,7 +3324,7 @@
     string? LongText?;
 };
 
-// Unknown type: BillingPlanItemOfA_SalesOrderBillingPlanOrderByOptions
+type BillingPlanItemOfA_SalesOrderBillingPlanOrderByOptions ("SalesOrder"|"SalesOrder desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanItem"|"BillingPlanItem desc"|"BillingPlanDateCategory"|"BillingPlanDateCategory desc"|"BillingPlanBillingDate"|"BillingPlanBillingDate desc"|"BillingPlanAmount"|"BillingPlanAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"BillingPlanAmountPercent"|"BillingPlanAmountPercent desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"ProposedBillingDocumentType"|"ProposedBillingDocumentType desc"|"BillingPlanDateDescriptionCode"|"BillingPlanDateDescriptionCode desc"|"BillingBlockReason"|"BillingBlockReason desc"|"BillingPlanServiceStartDate"|"BillingPlanServiceStartDate desc"|"BillingPlanServiceEndDate"|"BillingPlanServiceEndDate desc"|"BillingPlanRelatedBillgStatus"|"BillingPlanRelatedBillgStatus desc"|"BillingPlanType"|"BillingPlanType desc"|"AdoptingBillingDateID"|"AdoptingBillingDateID desc"|"BillingPlanBillingRule"|"BillingPlanBillingRule desc"|"BillingPlanMilestoneUsage"|"BillingPlanMilestoneUsage desc"|"BillgPlnDteCorrectionRfndType"|"BillgPlnDteCorrectionRfndType desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"PostponementReason"|"PostponementReason desc")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderBillingPlan
 
@@ -3249,11 +3335,11 @@
     SalesOrderOfA_SalesOrderBillingPlanSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderBillingPlanExpandOptions
+type SalesOrderOfA_SalesOrderBillingPlanExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesOrderExpandOptions
+type A_SalesOrderExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesOrderTextExpandOptions
+type A_SalesOrderTextExpandOptions "to_SalesOrder"[];
 
 # Represents the Queries record for the operation: listA_SalesOrders
 
@@ -3274,9 +3360,9 @@
     A_SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderOrderByOptions
+type A_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderType"|"SalesOrderType desc"|"SalesOrderTypeInternalCode"|"SalesOrderTypeInternalCode desc"|"SalesOrganization"|"SalesOrganization desc"|"DistributionChannel"|"DistributionChannel desc"|"OrganizationDivision"|"OrganizationDivision desc"|"SalesGroup"|"SalesGroup desc"|"SalesOffice"|"SalesOffice desc"|"SalesDistrict"|"SalesDistrict desc"|"SoldToParty"|"SoldToParty desc"|"CreationDate"|"CreationDate desc"|"CreatedByUser"|"CreatedByUser desc"|"LastChangeDate"|"LastChangeDate desc"|"SenderBusinessSystemName"|"SenderBusinessSystemName desc"|"ExternalDocumentID"|"ExternalDocumentID desc"|"LastChangeDateTime"|"LastChangeDateTime desc"|"ExternalDocLastChangeDateTime"|"ExternalDocLastChangeDateTime desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"PurchaseOrderByShipToParty"|"PurchaseOrderByShipToParty desc"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderType desc"|"CustomerPurchaseOrderDate"|"CustomerPurchaseOrderDate desc"|"SalesOrderDate"|"SalesOrderDate desc"|"TotalNetAmount"|"TotalNetAmount desc"|"OverallDeliveryStatus"|"OverallDeliveryStatus desc"|"TotalBlockStatus"|"TotalBlockStatus desc"|"OverallOrdReltdBillgStatus"|"OverallOrdReltdBillgStatus desc"|"OverallSDDocReferenceStatus"|"OverallSDDocReferenceStatus desc"|"TransactionCurrency"|"TransactionCurrency desc"|"SDDocumentReason"|"SDDocumentReason desc"|"PricingDate"|"PricingDate desc"|"PriceDetnExchangeRate"|"PriceDetnExchangeRate desc"|"BillingPlan"|"BillingPlan desc"|"RequestedDeliveryDate"|"RequestedDeliveryDate desc"|"ShippingCondition"|"ShippingCondition desc"|"CompleteDeliveryIsDefined"|"CompleteDeliveryIsDefined desc"|"ShippingType"|"ShippingType desc"|"HeaderBillingBlockReason"|"HeaderBillingBlockReason desc"|"DeliveryBlockReason"|"DeliveryBlockReason desc"|"DeliveryDateTypeRule"|"DeliveryDateTypeRule desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"IncotermsVersion"|"IncotermsVersion desc"|"CustomerPriceGroup"|"CustomerPriceGroup desc"|"PriceListType"|"PriceListType desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"PaymentMethod"|"PaymentMethod desc"|"FixedValueDate"|"FixedValueDate desc"|"AssignmentReference"|"AssignmentReference desc"|"ReferenceSDDocument"|"ReferenceSDDocument desc"|"ReferenceSDDocumentCategory"|"ReferenceSDDocumentCategory desc"|"AccountingDocExternalReference"|"AccountingDocExternalReference desc"|"CustomerAccountAssignmentGroup"|"CustomerAccountAssignmentGroup desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"CustomerGroup"|"CustomerGroup desc"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup1 desc"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup2 desc"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup3 desc"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup4 desc"|"AdditionalCustomerGroup5"|"AdditionalCustomerGroup5 desc"|"SlsDocIsRlvtForProofOfDeliv"|"SlsDocIsRlvtForProofOfDeliv desc"|"CustomerTaxClassification1"|"CustomerTaxClassification1 desc"|"CustomerTaxClassification2"|"CustomerTaxClassification2 desc"|"CustomerTaxClassification3"|"CustomerTaxClassification3 desc"|"CustomerTaxClassification4"|"CustomerTaxClassification4 desc"|"CustomerTaxClassification5"|"CustomerTaxClassification5 desc"|"CustomerTaxClassification6"|"CustomerTaxClassification6 desc"|"CustomerTaxClassification7"|"CustomerTaxClassification7 desc"|"CustomerTaxClassification8"|"CustomerTaxClassification8 desc"|"CustomerTaxClassification9"|"CustomerTaxClassification9 desc"|"TaxDepartureCountry"|"TaxDepartureCountry desc"|"VATRegistrationCountry"|"VATRegistrationCountry desc"|"SalesOrderApprovalReason"|"SalesOrderApprovalReason desc"|"SalesDocApprovalStatus"|"SalesDocApprovalStatus desc"|"OverallSDProcessStatus"|"OverallSDProcessStatus desc"|"TotalCreditCheckStatus"|"TotalCreditCheckStatus desc"|"OverallTotalDeliveryStatus"|"OverallTotalDeliveryStatus desc"|"OverallSDDocumentRejectionSts"|"OverallSDDocumentRejectionSts desc"|"BillingDocumentDate"|"BillingDocumentDate desc"|"ContractAccount"|"ContractAccount desc"|"AdditionalValueDays"|"AdditionalValueDays desc"|"CustomerPurchaseOrderSuplmnt"|"CustomerPurchaseOrderSuplmnt desc"|"ServicesRenderedDate"|"ServicesRenderedDate desc")[];
 
-// Unknown type: A_SalesOrderSelectOptions
+type A_SalesOrderSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderScheduleLines
 
@@ -3295,7 +3381,7 @@
     A_SalesOrderScheduleLineSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemBillingPlanSelectOptions
+type SalesOrderItemOfA_SalesOrderItemBillingPlanSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrderScheduleLineWrapper record {
@@ -3313,11 +3399,11 @@
     A_SalesOrderScheduleLine d?;
 };
 
-// Unknown type: PartnerOfA_SalesOrderOrderByOptions
+type PartnerOfA_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PartnerFunction"|"PartnerFunction desc"|"PartnerFunctionInternalCode"|"PartnerFunctionInternalCode desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"ReferenceBusinessPartner"|"ReferenceBusinessPartner desc"|"AddressID"|"AddressID desc"|"VATRegistration"|"VATRegistration desc")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPartnerExpandOptions
+type SalesOrderOfA_SalesOrderItemPartnerExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: A_SalesOrderItemBillingPlanExpandOptions
+type A_SalesOrderItemBillingPlanExpandOptions ("to_BillingPlanItem"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type Modified\ A_SlsOrderItemBillingPlanItemType record {
@@ -3341,7 +3427,7 @@
     string? BillingBlockReason?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemBillingPlanExpandOptions
+type SalesOrderItemOfA_SalesOrderItemBillingPlanExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrderItemPrElementWrapper record {
@@ -3392,6 +3478,7 @@
 
 type RejectApprovalRequestQueries record {
     # Value needs to be enclosed in single quotes
+    @constraint:String {maxLength: 11002, pattern: re `^'[^']*(''[^']*)*'$`}
     string SalesOrder;
 };
 
@@ -3414,11 +3501,11 @@
     A_SalesOrderRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderRelatedObjectOrderByOptions
+type A_SalesOrderRelatedObjectOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SDDocRelatedObjectSequenceNmbr"|"SDDocRelatedObjectSequenceNmbr desc"|"SDDocumentRelatedObjectType"|"SDDocumentRelatedObjectType desc"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectSystem desc"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference1 desc"|"SDDocRelatedObjectReference2"|"SDDocRelatedObjectReference2 desc")[];
 
-// Unknown type: A_SalesOrderRelatedObjectExpandOptions
+type A_SalesOrderRelatedObjectExpandOptions "to_SalesOrder"[];
 
-// Unknown type: A_SalesOrderRelatedObjectSelectOptions
+type A_SalesOrderRelatedObjectSelectOptions ("SalesOrder"|"SDDocRelatedObjectSequenceNmbr"|"SDDocumentRelatedObjectType"|"SDDocRelatedObjectSystem"|"SDDocRelatedObjectReference1"|"SDDocRelatedObjectReference2"|"to_SalesOrder")[];
 
 
 type CollectionOfA_SalesOrderRelatedObjectWrapper record {
@@ -3434,9 +3521,9 @@
     SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPartnerAddressExpandOptions
+type SalesOrderOfA_SalesOrderItemPartnerAddressExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions
+type SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type CollectionOfA_SalesOrderItemText record {
@@ -3444,7 +3531,7 @@
     A_SalesOrderItemText[] results?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderRelatedObjectSelectOptions
+type SalesOrderOfA_SalesOrderRelatedObjectSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type UpdateA_SalesOrderItemPartner record {
@@ -3460,7 +3547,7 @@
     string? VATRegistration?;
 };
 
-// Unknown type: A_SalesOrderItmSubsqntProcFlowOrderByOptions
+type A_SalesOrderItmSubsqntProcFlowOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentItem"|"SubsequentDocumentItem desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"SubsqntDocItmPrecdgDocument"|"SubsqntDocItmPrecdgDocument desc"|"SubsqntDocItmPrecdgDocItem"|"SubsqntDocItmPrecdgDocItem desc"|"SubsqntDocItmPrecdgDocCategory"|"SubsqntDocItmPrecdgDocCategory desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 # Represents the Queries record for the operation: listTextsOfA_SalesOrderItem
 
@@ -3481,11 +3568,11 @@
     A_SalesOrderItemTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemTextExpandOptions
+type A_SalesOrderItemTextExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SalesOrderItemTextSelectOptions
+type A_SalesOrderItemTextSelectOptions ("SalesOrder"|"SalesOrderItem"|"Language"|"LongTextID"|"LongText"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: PartnerOfA_SalesOrderExpandOptions
+type PartnerOfA_SalesOrderExpandOptions ("to_Address"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getPartnerOfA_SalesOrderItemPartnerAddress
 
@@ -3496,16 +3583,16 @@
     PartnerOfA_SalesOrderItemPartnerAddressSelectOptions \$select?;
 };
 
-// Unknown type: PartnerOfA_SalesOrderItemPartnerAddressExpandOptions
+type PartnerOfA_SalesOrderItemPartnerAddressExpandOptions ("to_Address"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: PartnerOfA_SalesOrderItemPartnerAddressSelectOptions
+type PartnerOfA_SalesOrderItemPartnerAddressSelectOptions ("SalesOrder"|"SalesOrderItem"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"AddressID"|"VATRegistration"|"to_Address"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type Modified\ A_SalesOrderType record {
     UpdateA_SalesOrder d?;
 };
 
-// Unknown type: PartnerOfA_SalesOrderSelectOptions
+type PartnerOfA_SalesOrderSelectOptions ("SalesOrder"|"PartnerFunction"|"PartnerFunctionInternalCode"|"Customer"|"Supplier"|"Personnel"|"ContactPerson"|"ReferenceBusinessPartner"|"AddressID"|"VATRegistration"|"to_Address"|"to_SalesOrder")[];
 
 
 type CollectionOfA_SalesOrderText record {
@@ -3568,7 +3655,7 @@
     string? FaxExtensionNumber?;
 };
 
-// Unknown type: A_SalesOrderItemBillingPlanOrderByOptions
+type A_SalesOrderItemBillingPlanOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"BillingPlan"|"BillingPlan desc"|"BillingPlanIsInHeader"|"BillingPlanIsInHeader desc"|"BillingPlanStartDate"|"BillingPlanStartDate desc"|"BillingPlanStartDateRule"|"BillingPlanStartDateRule desc"|"ReferenceBillingPlan"|"ReferenceBillingPlan desc"|"BillingPlanCategory"|"BillingPlanCategory desc"|"BillingPlanType"|"BillingPlanType desc"|"BillingPlanEndDate"|"BillingPlanEndDate desc"|"BillingPlanEndDateRule"|"BillingPlanEndDateRule desc"|"BillingPlanSearchTerm"|"BillingPlanSearchTerm desc")[];
 
 
 type A_SalesOrderItemPartnerAddressWrapper record {
@@ -3594,7 +3681,7 @@
     A_SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: BillingPlanOfA_SalesOrderBillingPlanItemExpandOptions
+type BillingPlanOfA_SalesOrderBillingPlanItemExpandOptions ("to_BillingPlanItem"|"to_SalesOrder")[];
 
 
 type CollectionOfA_SlsOrderItemBillingPlanItemWrapper record {
@@ -3607,7 +3694,7 @@
     A_SlsOrderItemBillingPlanItem[] results?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPrElementExpandOptions
+type SalesOrderItemOfA_SalesOrderItemPrElementExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type UpdateA_SalesOrderHeaderPartner record {
@@ -3642,7 +3729,7 @@
     A_SalesOrderHeaderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderHeaderPartnerOrderByOptions
+type A_SalesOrderHeaderPartnerOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PartnerFunction"|"PartnerFunction desc"|"PartnerFunctionInternalCode"|"PartnerFunctionInternalCode desc"|"Customer"|"Customer desc"|"Supplier"|"Supplier desc"|"Personnel"|"Personnel desc"|"ContactPerson"|"ContactPerson desc"|"ReferenceBusinessPartner"|"ReferenceBusinessPartner desc"|"AddressID"|"AddressID desc"|"VATRegistration"|"VATRegistration desc")[];
 
 
 type A_SalesOrderSubsqntProcFlowWrapper record {
@@ -3660,7 +3747,7 @@
     A_SalesOrderSubsqntProcFlow[] results?;
 };
 
-// Unknown type: SalesOrderOfA_SlsOrdPaymentPlanItemDetailsSelectOptions
+type SalesOrderOfA_SlsOrdPaymentPlanItemDetailsSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderTexts
 
@@ -3681,7 +3768,7 @@
     A_SalesOrderTextSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderTextSelectOptions
+type A_SalesOrderTextSelectOptions ("SalesOrder"|"Language"|"LongTextID"|"LongText"|"to_SalesOrder")[];
 
 
 type A_SalesOrderItemBillingPlanWrapper record {
@@ -3698,9 +3785,9 @@
     UpdateA_SalesOrderHeaderPartner d?;
 };
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesOrderOrderByOptions
+type PrecedingProcFlowDocOfA_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesOrderExpandOptions
+type PrecedingProcFlowDocOfA_SalesOrderExpandOptions "to_SalesOrder"[];
 
 # Represents the Queries record for the operation: listPrecedingProcFlowDocItemsOfA_SalesOrderItem
 
@@ -3721,7 +3808,7 @@
     PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: PrecedingProcFlowDocItemOfA_SalesOrderItemExpandOptions
+type PrecedingProcFlowDocItemOfA_SalesOrderItemExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type Modified\ A_SalesOrderItemType record {
@@ -3737,9 +3824,9 @@
     A_SalesOrderItemPrElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPartnerExpandOptions
+type SalesOrderItemOfA_SalesOrderItemPartnerExpandOptions ("to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions
+type BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions ("SalesOrder"|"SalesOrderItem"|"BillingPlan"|"BillingPlanItem"|"BillingPlanDateCategory"|"BillingPlanBillingDate"|"BillingPlanAmount"|"TransactionCurrency"|"BillingPlanAmountPercent"|"CustomerPaymentTerms"|"ProposedBillingDocumentType"|"BillingPlanDateDescriptionCode"|"BillingBlockReason"|"BillingPlanServiceStartDate"|"BillingPlanServiceEndDate"|"BillingPlanRelatedBillgStatus"|"BillingPlanType"|"AdoptingBillingDateID"|"BillingPlanBillingRule"|"BillingPlanMilestoneUsage"|"BillgPlnDteCorrectionRfndType"|"AccountingExchangeRate"|"PostponementReason"|"to_BillingPlan"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type CollectionOfA_SalesOrderBillingPlanItemWrapper record {
@@ -3752,7 +3839,7 @@
     A_SalesOrderBillingPlanItem[] results?;
 };
 
-// Unknown type: A_SalesOrderPartnerAddressOrderByOptions
+type A_SalesOrderPartnerAddressOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PartnerFunction"|"PartnerFunction desc"|"AddressRepresentationCode"|"AddressRepresentationCode desc"|"CorrespondenceLanguage"|"CorrespondenceLanguage desc"|"AddresseeFullName"|"AddresseeFullName desc"|"OrganizationName1"|"OrganizationName1 desc"|"OrganizationName2"|"OrganizationName2 desc"|"OrganizationName3"|"OrganizationName3 desc"|"OrganizationName4"|"OrganizationName4 desc"|"CityName"|"CityName desc"|"DistrictName"|"DistrictName desc"|"PostalCode"|"PostalCode desc"|"StreetPrefixName1"|"StreetPrefixName1 desc"|"StreetPrefixName2"|"StreetPrefixName2 desc"|"StreetName"|"StreetName desc"|"StreetSuffixName1"|"StreetSuffixName1 desc"|"StreetSuffixName2"|"StreetSuffixName2 desc"|"HouseNumber"|"HouseNumber desc"|"Country"|"Country desc"|"Region"|"Region desc"|"FormOfAddress"|"FormOfAddress desc"|"TaxJurisdiction"|"TaxJurisdiction desc"|"TransportZone"|"TransportZone desc"|"POBox"|"POBox desc"|"POBoxPostalCode"|"POBoxPostalCode desc"|"EmailAddress"|"EmailAddress desc"|"MobilePhoneCountry"|"MobilePhoneCountry desc"|"MobileNumber"|"MobileNumber desc"|"PhoneNumberCountry"|"PhoneNumberCountry desc"|"PhoneNumber"|"PhoneNumber desc"|"PhoneExtensionNumber"|"PhoneExtensionNumber desc"|"FaxNumberCountry"|"FaxNumberCountry desc"|"FaxAreaCodeSubscriberNumber"|"FaxAreaCodeSubscriberNumber desc"|"FaxExtensionNumber"|"FaxExtensionNumber desc")[];
 
 # Represents the Queries record for the operation: getSalesOrderItemOfA_SalesOrderItemPrElement
 
@@ -3763,18 +3850,19 @@
     SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions
+type SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: releaseApprovalRequest
 
 type ReleaseApprovalRequestQueries record {
     # Value needs to be enclosed in single quotes
+    @constraint:String {maxLength: 11002, pattern: re `^'[^']*(''[^']*)*'$`}
     string SalesOrder;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemRelatedObjectExpandOptions
+type SalesOrderOfA_SalesOrderItemRelatedObjectExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPartnerAddressSelectOptions
+type SalesOrderItemOfA_SalesOrderItemPartnerAddressSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type A_SalesOrderBillingPlanItemWrapper record {
@@ -3792,7 +3880,7 @@
     A_SalesOrderHeaderPrElement[] results?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemBillingPlanExpandOptions
+type SalesOrderOfA_SalesOrderItemBillingPlanExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listAddressesOfA_SalesOrderHeaderPartner
 
@@ -3813,12 +3901,13 @@
     AddressOfA_SalesOrderHeaderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: AddressOfA_SalesOrderHeaderPartnerExpandOptions
+type AddressOfA_SalesOrderHeaderPartnerExpandOptions ("to_Partner"|"to_SalesOrder")[];
 
-// Unknown type: AddressOfA_SalesOrderHeaderPartnerSelectOptions
+type AddressOfA_SalesOrderHeaderPartnerSelectOptions ("SalesOrder"|"PartnerFunction"|"AddressRepresentationCode"|"CorrespondenceLanguage"|"AddresseeFullName"|"OrganizationName1"|"OrganizationName2"|"OrganizationName3"|"OrganizationName4"|"CityName"|"DistrictName"|"PostalCode"|"StreetPrefixName1"|"StreetPrefixName2"|"StreetName"|"StreetSuffixName1"|"StreetSuffixName2"|"HouseNumber"|"Country"|"Region"|"FormOfAddress"|"TaxJurisdiction"|"TransportZone"|"POBox"|"POBoxPostalCode"|"EmailAddress"|"MobilePhoneCountry"|"MobileNumber"|"PhoneNumberCountry"|"PhoneNumber"|"PhoneExtensionNumber"|"FaxNumberCountry"|"FaxAreaCodeSubscriberNumber"|"FaxExtensionNumber"|"to_Partner"|"to_SalesOrder")[];
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -3862,7 +3951,7 @@
     CollectionOfA_SalesOrderHeaderPartner d?;
 };
 
-// Unknown type: PartnerOfA_SalesOrderPartnerAddressExpandOptions
+type PartnerOfA_SalesOrderPartnerAddressExpandOptions ("to_Address"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: getSalesOrderItemOfA_SalesOrderItemBillingPlan
 
@@ -3878,7 +3967,7 @@
     A_SalesOrderRelatedObject d?;
 };
 
-// Unknown type: PricingElementOfA_SalesOrderExpandOptions
+type PricingElementOfA_SalesOrderExpandOptions "to_SalesOrder"[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderItemBillingPlan
 
@@ -3900,7 +3989,7 @@
     A_SalesOrderItemPartnerAddress[] results?;
 };
 
-// Unknown type: BillingPlanOfA_SlsOrderItemBillingPlanItemSelectOptions
+type BillingPlanOfA_SlsOrderItemBillingPlanItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"BillingPlan"|"BillingPlanIsInHeader"|"BillingPlanStartDate"|"BillingPlanStartDateRule"|"ReferenceBillingPlan"|"BillingPlanCategory"|"BillingPlanType"|"BillingPlanEndDate"|"BillingPlanEndDateRule"|"BillingPlanSearchTerm"|"to_BillingPlanItem"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: getA_SlsOrderItemBillingPlanItem
 
@@ -3930,7 +4019,7 @@
     A_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemOrderByOptions
+type A_SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"HigherLevelItem"|"HigherLevelItem desc"|"HigherLevelItemUsage"|"HigherLevelItemUsage desc"|"SalesOrderItemCategory"|"SalesOrderItemCategory desc"|"SalesOrderItemText"|"SalesOrderItemText desc"|"PurchaseOrderByCustomer"|"PurchaseOrderByCustomer desc"|"PurchaseOrderByShipToParty"|"PurchaseOrderByShipToParty desc"|"UnderlyingPurchaseOrderItem"|"UnderlyingPurchaseOrderItem desc"|"ExternalItemID"|"ExternalItemID desc"|"Material"|"Material desc"|"MaterialByCustomer"|"MaterialByCustomer desc"|"PricingDate"|"PricingDate desc"|"PricingReferenceMaterial"|"PricingReferenceMaterial desc"|"BillingPlan"|"BillingPlan desc"|"RequestedQuantity"|"RequestedQuantity desc"|"RequestedQuantityUnit"|"RequestedQuantityUnit desc"|"RequestedQuantitySAPUnit"|"RequestedQuantitySAPUnit desc"|"RequestedQuantityISOUnit"|"RequestedQuantityISOUnit desc"|"OrderQuantityUnit"|"OrderQuantityUnit desc"|"OrderQuantitySAPUnit"|"OrderQuantitySAPUnit desc"|"OrderQuantityISOUnit"|"OrderQuantityISOUnit desc"|"ConfdDelivQtyInOrderQtyUnit"|"ConfdDelivQtyInOrderQtyUnit desc"|"ItemGrossWeight"|"ItemGrossWeight desc"|"ItemNetWeight"|"ItemNetWeight desc"|"ItemWeightUnit"|"ItemWeightUnit desc"|"ItemWeightSAPUnit"|"ItemWeightSAPUnit desc"|"ItemWeightISOUnit"|"ItemWeightISOUnit desc"|"ItemVolume"|"ItemVolume desc"|"ItemVolumeUnit"|"ItemVolumeUnit desc"|"ItemVolumeSAPUnit"|"ItemVolumeSAPUnit desc"|"ItemVolumeISOUnit"|"ItemVolumeISOUnit desc"|"TransactionCurrency"|"TransactionCurrency desc"|"NetAmount"|"NetAmount desc"|"TotalSDDocReferenceStatus"|"TotalSDDocReferenceStatus desc"|"SDDocReferenceStatus"|"SDDocReferenceStatus desc"|"MaterialSubstitutionReason"|"MaterialSubstitutionReason desc"|"MaterialGroup"|"MaterialGroup desc"|"MaterialPricingGroup"|"MaterialPricingGroup desc"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup1 desc"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup2 desc"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup3 desc"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup4 desc"|"AdditionalMaterialGroup5"|"AdditionalMaterialGroup5 desc"|"BillingDocumentDate"|"BillingDocumentDate desc"|"ContractAccount"|"ContractAccount desc"|"AdditionalValueDays"|"AdditionalValueDays desc"|"ServicesRenderedDate"|"ServicesRenderedDate desc"|"Batch"|"Batch desc"|"ProductionPlant"|"ProductionPlant desc"|"OriginalPlant"|"OriginalPlant desc"|"AltvBsdConfSubstitutionStatus"|"AltvBsdConfSubstitutionStatus desc"|"StorageLocation"|"StorageLocation desc"|"DeliveryGroup"|"DeliveryGroup desc"|"ShippingPoint"|"ShippingPoint desc"|"ShippingType"|"ShippingType desc"|"DeliveryPriority"|"DeliveryPriority desc"|"DeliveryDateQuantityIsFixed"|"DeliveryDateQuantityIsFixed desc"|"DeliveryDateTypeRule"|"DeliveryDateTypeRule desc"|"IncotermsClassification"|"IncotermsClassification desc"|"IncotermsTransferLocation"|"IncotermsTransferLocation desc"|"IncotermsLocation1"|"IncotermsLocation1 desc"|"IncotermsLocation2"|"IncotermsLocation2 desc"|"TaxAmount"|"TaxAmount desc"|"ProductTaxClassification1"|"ProductTaxClassification1 desc"|"ProductTaxClassification2"|"ProductTaxClassification2 desc"|"ProductTaxClassification3"|"ProductTaxClassification3 desc"|"ProductTaxClassification4"|"ProductTaxClassification4 desc"|"ProductTaxClassification5"|"ProductTaxClassification5 desc"|"ProductTaxClassification6"|"ProductTaxClassification6 desc"|"ProductTaxClassification7"|"ProductTaxClassification7 desc"|"ProductTaxClassification8"|"ProductTaxClassification8 desc"|"ProductTaxClassification9"|"ProductTaxClassification9 desc"|"MatlAccountAssignmentGroup"|"MatlAccountAssignmentGroup desc"|"CostAmount"|"CostAmount desc"|"CustomerPaymentTerms"|"CustomerPaymentTerms desc"|"FixedValueDate"|"FixedValueDate desc"|"CustomerGroup"|"CustomerGroup desc"|"SalesDocumentRjcnReason"|"SalesDocumentRjcnReason desc"|"ItemBillingBlockReason"|"ItemBillingBlockReason desc"|"SlsDocIsRlvtForProofOfDeliv"|"SlsDocIsRlvtForProofOfDeliv desc"|"WBSElement"|"WBSElement desc"|"ProfitCenter"|"ProfitCenter desc"|"AccountingExchangeRate"|"AccountingExchangeRate desc"|"ReferenceSDDocument"|"ReferenceSDDocument desc"|"ReferenceSDDocumentItem"|"ReferenceSDDocumentItem desc"|"SDProcessStatus"|"SDProcessStatus desc"|"DeliveryStatus"|"DeliveryStatus desc"|"OrderRelatedBillingStatus"|"OrderRelatedBillingStatus desc"|"Subtotal1Amount"|"Subtotal1Amount desc"|"Subtotal2Amount"|"Subtotal2Amount desc"|"Subtotal3Amount"|"Subtotal3Amount desc"|"Subtotal4Amount"|"Subtotal4Amount desc"|"Subtotal5Amount"|"Subtotal5Amount desc"|"Subtotal6Amount"|"Subtotal6Amount desc")[];
 
 
 type Modified\ A_SalesOrderItemBillingPlanType record {
@@ -3958,7 +4047,7 @@
     SalesOrderOfA_SalesOrderItemPrElementSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPrElementSelectOptions
+type SalesOrderOfA_SalesOrderItemPrElementSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderItmPrecdgProcFlow
 
@@ -3969,9 +4058,9 @@
     A_SalesOrderItmPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItmPrecdgProcFlowExpandOptions
+type A_SalesOrderItmPrecdgProcFlowExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
-// Unknown type: A_SalesOrderItmPrecdgProcFlowSelectOptions
+type A_SalesOrderItmPrecdgProcFlowSelectOptions ("SalesOrder"|"SalesOrderItem"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentItem"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"RelatedProcFlowDocStsFieldName"|"SDProcessStatus"|"AccountingTransferStatus"|"PrelimBillingDocumentStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type A_SalesOrderWrapper record {
@@ -3987,9 +4076,9 @@
     SalesOrderItemOfA_SalesOrderItemTextSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemTextSelectOptions
+type SalesOrderItemOfA_SalesOrderItemTextSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesOrderItemSelectOptions
+type SubsequentProcFlowDocItemOfA_SalesOrderItemSelectOptions ("SalesOrder"|"SalesOrderItem"|"DocRelationshipUUID"|"SubsequentDocument"|"SubsequentDocumentItem"|"SubsequentDocumentCategory"|"ProcessFlowLevel"|"RelatedProcFlowDocStsFieldName"|"SDProcessStatus"|"AccountingTransferStatus"|"PrelimBillingDocumentStatus"|"SubsqntDocItmPrecdgDocument"|"SubsqntDocItmPrecdgDocItem"|"SubsqntDocItmPrecdgDocCategory"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderSubsqntProcFlow
 
@@ -4000,7 +4089,7 @@
     A_SalesOrderSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderSubsqntProcFlowExpandOptions
+type SalesOrderOfA_SalesOrderSubsqntProcFlowExpandOptions ("to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderPrecdgProcFlows
 
@@ -4021,9 +4110,9 @@
     A_SalesOrderPrecdgProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderPrecdgProcFlowOrderByOptions
+type A_SalesOrderPrecdgProcFlowOrderByOptions ("SalesOrder"|"SalesOrder desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: SalesOrderOfA_SalesOrderItmSubsqntProcFlowSelectOptions
+type SalesOrderOfA_SalesOrderItmSubsqntProcFlowSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderRelatedObject
 
@@ -4034,7 +4123,7 @@
     A_SalesOrderRelatedObjectSelectOptions \$select?;
 };
 
-// Unknown type: PrecedingProcFlowDocOfA_SalesOrderSelectOptions
+type PrecedingProcFlowDocOfA_SalesOrderSelectOptions ("SalesOrder"|"DocRelationshipUUID"|"PrecedingDocument"|"PrecedingDocumentCategory"|"ProcessFlowLevel"|"OverallSDProcessStatus"|"CreationDate"|"CreationTime"|"LastChangeDate"|"to_SalesOrder")[];
 
 
 type CollectionOfA_SlsOrdPaymentPlanItemDetailsWrapper record {
@@ -4086,7 +4175,7 @@
     PrecedingProcFlowDocOfA_SalesOrderSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions
+type SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 # Represents the Queries record for the operation: getA_SalesOrderText
 
@@ -4159,7 +4248,7 @@
     A_SalesOrderItemSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemBillingPlanSelectOptions
+type A_SalesOrderItemBillingPlanSelectOptions ("SalesOrder"|"SalesOrderItem"|"BillingPlan"|"BillingPlanIsInHeader"|"BillingPlanStartDate"|"BillingPlanStartDateRule"|"ReferenceBillingPlan"|"BillingPlanCategory"|"BillingPlanType"|"BillingPlanEndDate"|"BillingPlanEndDateRule"|"BillingPlanSearchTerm"|"to_BillingPlanItem"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderSubsqntProcFlow
 
@@ -4176,7 +4265,7 @@
     A_SalesOrderBillingPlan[] results?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions
+type SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: listBillingPlanItemsOfA_SalesOrderBillingPlan
 
@@ -4197,7 +4286,7 @@
     BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions \$select?;
 };
 
-// Unknown type: BillingPlanItemOfA_SalesOrderBillingPlanExpandOptions
+type BillingPlanItemOfA_SalesOrderBillingPlanExpandOptions ("to_BillingPlan"|"to_SalesOrder")[];
 
 # Represents the Queries record for the operation: listBillingPlanItemsOfA_SalesOrderItemBillingPlan
 
@@ -4218,7 +4307,7 @@
     BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions \$select?;
 };
 
-// Unknown type: BillingPlanItemOfA_SalesOrderItemBillingPlanExpandOptions
+type BillingPlanItemOfA_SalesOrderItemBillingPlanExpandOptions ("to_BillingPlan"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type CollectionOfA_SalesOrderBillingPlanWrapper record {
@@ -4258,7 +4347,7 @@
     BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions \$select?;
 };
 
-// Unknown type: BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions
+type BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions ("SalesOrder"|"BillingPlan"|"BillingPlanStartDate"|"BillingPlanStartDateRule"|"ReferenceBillingPlan"|"BillingPlanCategory"|"BillingPlanType"|"BillingPlanEndDate"|"BillingPlanEndDateRule"|"BillingPlanSearchTerm"|"to_BillingPlanItem"|"to_SalesOrder")[];
 
 
 type Modified\ A_SlsOrdPaymentPlanItemDetailsType record {
@@ -4279,7 +4368,7 @@
     CollectionOfA_SalesOrderText d?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemRelatedObjectSelectOptions
+type SalesOrderOfA_SalesOrderItemRelatedObjectSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderItemRelatedObject
 
@@ -4364,7 +4453,7 @@
     SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemPartnerAddressExpandOptions
+type A_SalesOrderItemPartnerAddressExpandOptions ("to_Partner"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 
 type A_SalesOrderPartnerAddressWrapper record {
@@ -4380,7 +4469,7 @@
     SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderItemOfA_SalesOrderItemPartnerSelectOptions
+type SalesOrderItemOfA_SalesOrderItemPartnerSelectOptions ("SalesOrder"|"SalesOrderItem"|"HigherLevelItem"|"HigherLevelItemUsage"|"SalesOrderItemCategory"|"SalesOrderItemText"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"UnderlyingPurchaseOrderItem"|"ExternalItemID"|"Material"|"MaterialByCustomer"|"PricingDate"|"PricingReferenceMaterial"|"BillingPlan"|"RequestedQuantity"|"RequestedQuantityUnit"|"RequestedQuantitySAPUnit"|"RequestedQuantityISOUnit"|"OrderQuantityUnit"|"OrderQuantitySAPUnit"|"OrderQuantityISOUnit"|"ConfdDelivQtyInOrderQtyUnit"|"ItemGrossWeight"|"ItemNetWeight"|"ItemWeightUnit"|"ItemWeightSAPUnit"|"ItemWeightISOUnit"|"ItemVolume"|"ItemVolumeUnit"|"ItemVolumeSAPUnit"|"ItemVolumeISOUnit"|"TransactionCurrency"|"NetAmount"|"TotalSDDocReferenceStatus"|"SDDocReferenceStatus"|"MaterialSubstitutionReason"|"MaterialGroup"|"MaterialPricingGroup"|"AdditionalMaterialGroup1"|"AdditionalMaterialGroup2"|"AdditionalMaterialGroup3"|"AdditionalMaterialGroup4"|"AdditionalMaterialGroup5"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"ServicesRenderedDate"|"Batch"|"ProductionPlant"|"OriginalPlant"|"AltvBsdConfSubstitutionStatus"|"StorageLocation"|"DeliveryGroup"|"ShippingPoint"|"ShippingType"|"DeliveryPriority"|"DeliveryDateQuantityIsFixed"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"TaxAmount"|"ProductTaxClassification1"|"ProductTaxClassification2"|"ProductTaxClassification3"|"ProductTaxClassification4"|"ProductTaxClassification5"|"ProductTaxClassification6"|"ProductTaxClassification7"|"ProductTaxClassification8"|"ProductTaxClassification9"|"MatlAccountAssignmentGroup"|"CostAmount"|"CustomerPaymentTerms"|"FixedValueDate"|"CustomerGroup"|"SalesDocumentRjcnReason"|"ItemBillingBlockReason"|"SlsDocIsRlvtForProofOfDeliv"|"WBSElement"|"ProfitCenter"|"AccountingExchangeRate"|"ReferenceSDDocument"|"ReferenceSDDocumentItem"|"SDProcessStatus"|"DeliveryStatus"|"OrderRelatedBillingStatus"|"Subtotal1Amount"|"Subtotal2Amount"|"Subtotal3Amount"|"Subtotal4Amount"|"Subtotal5Amount"|"Subtotal6Amount"|"to_BillingPlan"|"to_Partner"|"to_PrecedingProcFlowDocItem"|"to_PricingElement"|"to_RelatedObject"|"to_SalesOrder"|"to_ScheduleLine"|"to_SubsequentProcFlowDocItem"|"to_Text")[];
 
 
 type Modified\ A_SalesOrderBillingPlanType record {
@@ -4411,7 +4500,7 @@
     A_SalesOrderItemPartnerAddressSelectOptions \$select?;
 };
 
-// Unknown type: A_SalesOrderItemPartnerAddressSelectOptions
+type A_SalesOrderItemPartnerAddressSelectOptions ("SalesOrder"|"SalesOrderItem"|"PartnerFunction"|"AddressRepresentationCode"|"CorrespondenceLanguage"|"AddresseeFullName"|"OrganizationName1"|"OrganizationName2"|"OrganizationName3"|"OrganizationName4"|"CityName"|"DistrictName"|"PostalCode"|"StreetName"|"StreetPrefixName1"|"StreetPrefixName2"|"StreetSuffixName1"|"StreetSuffixName2"|"HouseNumber"|"Country"|"Region"|"FormOfAddress"|"TaxJurisdiction"|"TransportZone"|"POBox"|"POBoxPostalCode"|"EmailAddress"|"MobilePhoneCountry"|"MobileNumber"|"PhoneNumberCountry"|"PhoneNumber"|"PhoneExtensionNumber"|"FaxNumberCountry"|"FaxAreaCodeSubscriberNumber"|"FaxExtensionNumber"|"to_Partner"|"to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: getBillingPlanOfA_SalesOrder
 
@@ -4483,7 +4572,7 @@
     SalesOrderOfA_SalesOrderItemPartnerSelectOptions \$select?;
 };
 
-// Unknown type: SalesOrderOfA_SalesOrderItemPartnerSelectOptions
+type SalesOrderOfA_SalesOrderItemPartnerSelectOptions ("SalesOrder"|"SalesOrderType"|"SalesOrderTypeInternalCode"|"SalesOrganization"|"DistributionChannel"|"OrganizationDivision"|"SalesGroup"|"SalesOffice"|"SalesDistrict"|"SoldToParty"|"CreationDate"|"CreatedByUser"|"LastChangeDate"|"SenderBusinessSystemName"|"ExternalDocumentID"|"LastChangeDateTime"|"ExternalDocLastChangeDateTime"|"PurchaseOrderByCustomer"|"PurchaseOrderByShipToParty"|"CustomerPurchaseOrderType"|"CustomerPurchaseOrderDate"|"SalesOrderDate"|"TotalNetAmount"|"OverallDeliveryStatus"|"TotalBlockStatus"|"OverallOrdReltdBillgStatus"|"OverallSDDocReferenceStatus"|"TransactionCurrency"|"SDDocumentReason"|"PricingDate"|"PriceDetnExchangeRate"|"BillingPlan"|"RequestedDeliveryDate"|"ShippingCondition"|"CompleteDeliveryIsDefined"|"ShippingType"|"HeaderBillingBlockReason"|"DeliveryBlockReason"|"DeliveryDateTypeRule"|"IncotermsClassification"|"IncotermsTransferLocation"|"IncotermsLocation1"|"IncotermsLocation2"|"IncotermsVersion"|"CustomerPriceGroup"|"PriceListType"|"CustomerPaymentTerms"|"PaymentMethod"|"FixedValueDate"|"AssignmentReference"|"ReferenceSDDocument"|"ReferenceSDDocumentCategory"|"AccountingDocExternalReference"|"CustomerAccountAssignmentGroup"|"AccountingExchangeRate"|"CustomerGroup"|"AdditionalCustomerGroup1"|"AdditionalCustomerGroup2"|"AdditionalCustomerGroup3"|"AdditionalCustomerGroup4"|"AdditionalCustomerGroup5"|"SlsDocIsRlvtForProofOfDeliv"|"CustomerTaxClassification1"|"CustomerTaxClassification2"|"CustomerTaxClassification3"|"CustomerTaxClassification4"|"CustomerTaxClassification5"|"CustomerTaxClassification6"|"CustomerTaxClassification7"|"CustomerTaxClassification8"|"CustomerTaxClassification9"|"TaxDepartureCountry"|"VATRegistrationCountry"|"SalesOrderApprovalReason"|"SalesDocApprovalStatus"|"OverallSDProcessStatus"|"TotalCreditCheckStatus"|"OverallTotalDeliveryStatus"|"OverallSDDocumentRejectionSts"|"BillingDocumentDate"|"ContractAccount"|"AdditionalValueDays"|"CustomerPurchaseOrderSuplmnt"|"ServicesRenderedDate"|"to_BillingPlan"|"to_Item"|"to_Partner"|"to_PaymentPlanItemDetails"|"to_PrecedingProcFlowDoc"|"to_PricingElement"|"to_RelatedObject"|"to_SubsequentProcFlowDoc"|"to_Text")[];
 
 
 type A_SalesOrderItmSubsqntProcFlowWrapper record {
@@ -4495,9 +4584,9 @@
     UpdateA_SalesOrderItemPartner d?;
 };
 
-// Unknown type: PricingElementOfA_SalesOrderOrderByOptions
+type PricingElementOfA_SalesOrderOrderByOptions ("SalesOrder"|"SalesOrder desc"|"PricingProcedureStep"|"PricingProcedureStep desc"|"PricingProcedureCounter"|"PricingProcedureCounter desc"|"ConditionType"|"ConditionType desc"|"PricingDateTime"|"PricingDateTime desc"|"PriceConditionDeterminationDte"|"PriceConditionDeterminationDte desc"|"ConditionCalculationType"|"ConditionCalculationType desc"|"ConditionBaseValue"|"ConditionBaseValue desc"|"ConditionRateValue"|"ConditionRateValue desc"|"ConditionCurrency"|"ConditionCurrency desc"|"ConditionQuantity"|"ConditionQuantity desc"|"ConditionQuantityUnit"|"ConditionQuantityUnit desc"|"ConditionQuantitySAPUnit"|"ConditionQuantitySAPUnit desc"|"ConditionQuantityISOUnit"|"ConditionQuantityISOUnit desc"|"ConditionCategory"|"ConditionCategory desc"|"ConditionIsForStatistics"|"ConditionIsForStatistics desc"|"PricingScaleType"|"PricingScaleType desc"|"ConditionOrigin"|"ConditionOrigin desc"|"IsGroupCondition"|"IsGroupCondition desc"|"ConditionRecord"|"ConditionRecord desc"|"ConditionSequentialNumber"|"ConditionSequentialNumber desc"|"TaxCode"|"TaxCode desc"|"WithholdingTaxCode"|"WithholdingTaxCode desc"|"CndnRoundingOffDiffAmount"|"CndnRoundingOffDiffAmount desc"|"ConditionAmount"|"ConditionAmount desc"|"TransactionCurrency"|"TransactionCurrency desc"|"ConditionControl"|"ConditionControl desc"|"ConditionInactiveReason"|"ConditionInactiveReason desc"|"ConditionClass"|"ConditionClass desc"|"PrcgProcedureCounterForHeader"|"PrcgProcedureCounterForHeader desc"|"FactorForConditionBasisValue"|"FactorForConditionBasisValue desc"|"StructureCondition"|"StructureCondition desc"|"PeriodFactorForCndnBasisValue"|"PeriodFactorForCndnBasisValue desc"|"PricingScaleBasis"|"PricingScaleBasis desc"|"ConditionScaleBasisValue"|"ConditionScaleBasisValue desc"|"ConditionScaleBasisUnit"|"ConditionScaleBasisUnit desc"|"ConditionScaleBasisCurrency"|"ConditionScaleBasisCurrency desc"|"CndnIsRelevantForIntcoBilling"|"CndnIsRelevantForIntcoBilling desc"|"ConditionIsManuallyChanged"|"ConditionIsManuallyChanged desc"|"ConditionIsForConfiguration"|"ConditionIsForConfiguration desc"|"VariantCondition"|"VariantCondition desc")[];
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesOrderItemExpandOptions
+type SubsequentProcFlowDocItemOfA_SalesOrderItemExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];
 
 # Represents the Queries record for the operation: listA_SalesOrderRelatedObjects
 
@@ -4541,9 +4630,9 @@
     A_SalesOrderPrecdgProcFlow d?;
 };
 
-// Unknown type: SubsequentProcFlowDocItemOfA_SalesOrderItemOrderByOptions
+type SubsequentProcFlowDocItemOfA_SalesOrderItemOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"SubsequentDocument"|"SubsequentDocument desc"|"SubsequentDocumentItem"|"SubsequentDocumentItem desc"|"SubsequentDocumentCategory"|"SubsequentDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"SubsqntDocItmPrecdgDocument"|"SubsqntDocItmPrecdgDocument desc"|"SubsqntDocItmPrecdgDocItem"|"SubsqntDocItmPrecdgDocItem desc"|"SubsqntDocItmPrecdgDocCategory"|"SubsqntDocItmPrecdgDocCategory desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
-// Unknown type: A_SalesOrderItmPrecdgProcFlowOrderByOptions
+type A_SalesOrderItmPrecdgProcFlowOrderByOptions ("SalesOrder"|"SalesOrder desc"|"SalesOrderItem"|"SalesOrderItem desc"|"DocRelationshipUUID"|"DocRelationshipUUID desc"|"PrecedingDocument"|"PrecedingDocument desc"|"PrecedingDocumentItem"|"PrecedingDocumentItem desc"|"PrecedingDocumentCategory"|"PrecedingDocumentCategory desc"|"ProcessFlowLevel"|"ProcessFlowLevel desc"|"CreationDate"|"CreationDate desc"|"CreationTime"|"CreationTime desc"|"LastChangeDate"|"LastChangeDate desc")[];
 
 # Represents the Queries record for the operation: getSalesOrderOfA_SalesOrderItmSubsqntProcFlow
 
@@ -4930,395 +5019,395 @@
 
     # Reads the header of a sales order.
     # 
-    remote function getA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, A_SalesOrderExpandOptions \$expand = [], A_SalesOrderSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, A_SalesOrderExpandOptions \$expand = [], A_SalesOrderSelectOptions \$select = [], GetA_SalesOrderQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the billing plan of a sales order.
     # 
-    remote function getA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, A_SalesOrderBillingPlanExpandOptions \$expand = [], A_SalesOrderBillingPlanSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderBillingPlanQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
+    remote function getA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, A_SalesOrderBillingPlanExpandOptions \$expand = [], A_SalesOrderBillingPlanSelectOptions \$select = [], GetA_SalesOrderBillingPlanQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
 
     # Reads a billing plan item of a sales order.
     # 
-    remote function getA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, A_SalesOrderBillingPlanItemExpandOptions \$expand = [], A_SalesOrderBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderBillingPlanItemWrapper|error;
+    remote function getA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, A_SalesOrderBillingPlanItemExpandOptions \$expand = [], A_SalesOrderBillingPlanItemSelectOptions \$select = [], GetA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderBillingPlanItemWrapper|error;
 
     # Reads the header partners of a sales order and a partner function.
     # 
-    remote function getA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, A_SalesOrderHeaderPartnerExpandOptions \$expand = [], A_SalesOrderHeaderPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderHeaderPartnerQueries queries) returns A_SalesOrderHeaderPartnerWrapper|error;
+    remote function getA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, A_SalesOrderHeaderPartnerExpandOptions \$expand = [], A_SalesOrderHeaderPartnerSelectOptions \$select = [], GetA_SalesOrderHeaderPartnerQueries queries) returns A_SalesOrderHeaderPartnerWrapper|error;
 
     # Reads the header pricing element for a sales order.
     # 
-    remote function getA_SalesOrderHeaderPrElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesOrderHeaderPrElementExpandOptions \$expand = [], A_SalesOrderHeaderPrElementSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderHeaderPrElementQueries queries) returns A_SalesOrderHeaderPrElementWrapper|error;
+    remote function getA_SalesOrderHeaderPrElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesOrderHeaderPrElementExpandOptions \$expand = [], A_SalesOrderHeaderPrElementSelectOptions \$select = [], GetA_SalesOrderHeaderPrElementQueries queries) returns A_SalesOrderHeaderPrElementWrapper|error;
 
     # Reads a sales order item.
     # 
-    remote function getA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SalesOrderItemExpandOptions \$expand = [], A_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SalesOrderItemExpandOptions \$expand = [], A_SalesOrderItemSelectOptions \$select = [], GetA_SalesOrderItemQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the billing plan of a sales order item.
     # 
-    remote function getA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, A_SalesOrderItemBillingPlanExpandOptions \$expand = [], A_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
+    remote function getA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, A_SalesOrderItemBillingPlanExpandOptions \$expand = [], A_SalesOrderItemBillingPlanSelectOptions \$select = [], GetA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
 
     # Reads an item partner of an item with a specific partner function in a specific sales order.
     # 
-    remote function getA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesOrderItemPartnerExpandOptions \$expand = [], A_SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderItemPartnerWrapper|error;
+    remote function getA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, A_SalesOrderItemPartnerExpandOptions \$expand = [], A_SalesOrderItemPartnerSelectOptions \$select = [], GetA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderItemPartnerWrapper|error;
 
     # Reads the address of an item partner of a sales order.
     # 
-    remote function getA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], A_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemPartnerAddressWrapper|error;
+    remote function getA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], A_SalesOrderItemPartnerAddressSelectOptions \$select = [], GetA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemPartnerAddressWrapper|error;
 
     # Reads the pricing element of a item with specific pricing details.
     # 
-    remote function getA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesOrderItemPrElementExpandOptions \$expand = [], A_SalesOrderItemPrElementSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderItemPrElementWrapper|error;
+    remote function getA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, A_SalesOrderItemPrElementExpandOptions \$expand = [], A_SalesOrderItemPrElementSelectOptions \$select = [], GetA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderItemPrElementWrapper|error;
 
     # Reads a related object from a sales order item.
     # 
-    remote function getA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], A_SalesOrderItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderItemRelatedObjectWrapper|error;
+    remote function getA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], A_SalesOrderItemRelatedObjectSelectOptions \$select = [], GetA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderItemRelatedObjectWrapper|error;
 
     # Reads an item text.
     # 
-    remote function getA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesOrderItemTextExpandOptions \$expand = [], A_SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItemTextQueries queries) returns A_SalesOrderItemTextWrapper|error;
+    remote function getA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesOrderItemTextExpandOptions \$expand = [], A_SalesOrderItemTextSelectOptions \$select = [], GetA_SalesOrderItemTextQueries queries) returns A_SalesOrderItemTextWrapper|error;
 
     # Reads a preceding item for a sales order item.
     # 
-    remote function getA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], A_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderItmPrecdgProcFlowWrapper|error;
+    remote function getA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], A_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], GetA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderItmPrecdgProcFlowWrapper|error;
 
     # Reads a subsequent item for a sales order item.
     # 
-    remote function getA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], A_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderItmSubsqntProcFlowWrapper|error;
+    remote function getA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], A_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], GetA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderItmSubsqntProcFlowWrapper|error;
 
     # Reads the address of a header partner of a sales order.
     # 
-    remote function getA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, A_SalesOrderPartnerAddressExpandOptions \$expand = [], A_SalesOrderPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderPartnerAddressWrapper|error;
+    remote function getA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, A_SalesOrderPartnerAddressExpandOptions \$expand = [], A_SalesOrderPartnerAddressSelectOptions \$select = [], GetA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderPartnerAddressWrapper|error;
 
     # Reads a preceding document for a sales order.
     # 
-    remote function getA_SalesOrderPrecdgProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], A_SalesOrderPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderPrecdgProcFlowQueries queries) returns A_SalesOrderPrecdgProcFlowWrapper|error;
+    remote function getA_SalesOrderPrecdgProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], A_SalesOrderPrecdgProcFlowSelectOptions \$select = [], GetA_SalesOrderPrecdgProcFlowQueries queries) returns A_SalesOrderPrecdgProcFlowWrapper|error;
 
     # Reads a related object from the header of a specific sales order.
     # 
-    remote function getA_SalesOrderRelatedObject(string SalesOrder, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesOrderRelatedObjectExpandOptions \$expand = [], A_SalesOrderRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderRelatedObjectQueries queries) returns A_SalesOrderRelatedObjectWrapper|error;
+    remote function getA_SalesOrderRelatedObject(string SalesOrder, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, A_SalesOrderRelatedObjectExpandOptions \$expand = [], A_SalesOrderRelatedObjectSelectOptions \$select = [], GetA_SalesOrderRelatedObjectQueries queries) returns A_SalesOrderRelatedObjectWrapper|error;
 
     # Reads a schedule line.
     # 
-    remote function getA_SalesOrderScheduleLine(string SalesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, A_SalesOrderScheduleLineSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderScheduleLineQueries queries) returns A_SalesOrderScheduleLineWrapper|error;
+    remote function getA_SalesOrderScheduleLine(string SalesOrder, string SalesOrderItem, string ScheduleLine, map<string|string[]> headers = {}, A_SalesOrderScheduleLineSelectOptions \$select = [], GetA_SalesOrderScheduleLineQueries queries) returns A_SalesOrderScheduleLineWrapper|error;
 
     # Reads a subsequent document of a sales order.
     # 
-    remote function getA_SalesOrderSubsqntProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], A_SalesOrderSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderSubsqntProcFlowQueries queries) returns A_SalesOrderSubsqntProcFlowWrapper|error;
+    remote function getA_SalesOrderSubsqntProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, A_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], A_SalesOrderSubsqntProcFlowSelectOptions \$select = [], GetA_SalesOrderSubsqntProcFlowQueries queries) returns A_SalesOrderSubsqntProcFlowWrapper|error;
 
     # Reads a header text from a sales order.
     # 
-    remote function getA_SalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesOrderTextExpandOptions \$expand = [], A_SalesOrderTextSelectOptions \$select = [], anydata Additional Values, GetA_SalesOrderTextQueries queries) returns A_SalesOrderTextWrapper|error;
+    remote function getA_SalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, A_SalesOrderTextExpandOptions \$expand = [], A_SalesOrderTextSelectOptions \$select = [], GetA_SalesOrderTextQueries queries) returns A_SalesOrderTextWrapper|error;
 
     # Reads a payment plan item of a sales order.
     # 
-    remote function getA_SlsOrdPaymentPlanItemDetails(string SalesOrder, string PaymentPlanItem, map<string|string[]> headers = {}, A_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], anydata Additional Values, GetA_SlsOrdPaymentPlanItemDetailsQueries queries) returns A_SlsOrdPaymentPlanItemDetailsWrapper|error;
+    remote function getA_SlsOrdPaymentPlanItemDetails(string SalesOrder, string PaymentPlanItem, map<string|string[]> headers = {}, A_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], GetA_SlsOrdPaymentPlanItemDetailsQueries queries) returns A_SlsOrdPaymentPlanItemDetailsWrapper|error;
 
     # Reads a billing plan item of a sales order item.
     # 
-    remote function getA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, A_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], A_SlsOrderItemBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetA_SlsOrderItemBillingPlanItemQueries queries) returns A_SlsOrderItemBillingPlanItemWrapper|error;
+    remote function getA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, A_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], A_SlsOrderItemBillingPlanItemSelectOptions \$select = [], GetA_SlsOrderItemBillingPlanItemQueries queries) returns A_SlsOrderItemBillingPlanItemWrapper|error;
 
     # Reads the billing plan of a sales order.
     # 
-    remote function getBillingPlanOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, A_SalesOrderBillingPlanExpandOptions \$expand = [], A_SalesOrderBillingPlanSelectOptions \$select = [], anydata Additional Values, GetBillingPlanOfA_SalesOrderQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
+    remote function getBillingPlanOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, A_SalesOrderBillingPlanExpandOptions \$expand = [], A_SalesOrderBillingPlanSelectOptions \$select = [], GetBillingPlanOfA_SalesOrderQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
 
     # Reads the billing plan of a billing plan item of a sales order header.
     # 
-    remote function getBillingPlanOfA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, BillingPlanOfA_SalesOrderBillingPlanItemExpandOptions \$expand = [], BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetBillingPlanOfA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
+    remote function getBillingPlanOfA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, BillingPlanOfA_SalesOrderBillingPlanItemExpandOptions \$expand = [], BillingPlanOfA_SalesOrderBillingPlanItemSelectOptions \$select = [], GetBillingPlanOfA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderBillingPlanWrapper|error;
 
     # Reads the billing plan of a sales order item.
     # 
-    remote function getBillingPlanOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SalesOrderItemBillingPlanExpandOptions \$expand = [], A_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, GetBillingPlanOfA_SalesOrderItemQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
+    remote function getBillingPlanOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, A_SalesOrderItemBillingPlanExpandOptions \$expand = [], A_SalesOrderItemBillingPlanSelectOptions \$select = [], GetBillingPlanOfA_SalesOrderItemQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
 
     # Reads the item billing plan for an item billing plan item.
     # 
-    remote function getBillingPlanOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, BillingPlanOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], BillingPlanOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetBillingPlanOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
+    remote function getBillingPlanOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, BillingPlanOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], BillingPlanOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], GetBillingPlanOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderItemBillingPlanWrapper|error;
 
     # Reads the sales order item partner for an item partner address.
     # 
-    remote function getPartnerOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, PartnerOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], PartnerOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetPartnerOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemPartnerWrapper|error;
+    remote function getPartnerOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, PartnerOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], PartnerOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], GetPartnerOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemPartnerWrapper|error;
 
     # Reads the sales order header partner for a header partner address.
     # 
-    remote function getPartnerOfA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, PartnerOfA_SalesOrderPartnerAddressExpandOptions \$expand = [], PartnerOfA_SalesOrderPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetPartnerOfA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderHeaderPartnerWrapper|error;
+    remote function getPartnerOfA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, PartnerOfA_SalesOrderPartnerAddressExpandOptions \$expand = [], PartnerOfA_SalesOrderPartnerAddressSelectOptions \$select = [], GetPartnerOfA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderHeaderPartnerWrapper|error;
 
     # Reads the sales order item for an item billing plan.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for a partner function of a sales order item.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPartnerSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for an item partner address.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for a pricing element.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPrElementExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemPrElementExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemPrElementSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for a related object.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemRelatedObjectExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemRelatedObjectExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemRelatedObjectSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for an item text.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemTextExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItemTextQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItemTextExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItemTextSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItemTextQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item data for a preceding item of a sales order.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item data for a subsequent item of a sales order.
     # 
-    remote function getSalesOrderItemOfA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], SalesOrderItemOfA_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], GetSalesOrderItemOfA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order item for a billing plan item of this sales order item.
     # 
-    remote function getSalesOrderItemOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderItemOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetSalesOrderItemOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderItemWrapper|error;
+    remote function getSalesOrderItemOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderItemOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], SalesOrderItemOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], GetSalesOrderItemOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderItemWrapper|error;
 
     # Reads the sales order header for a billing plan.
     # 
-    remote function getSalesOrderOfA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderBillingPlanExpandOptions \$expand = [], SalesOrderOfA_SalesOrderBillingPlanSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderBillingPlanQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderBillingPlanExpandOptions \$expand = [], SalesOrderOfA_SalesOrderBillingPlanSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderBillingPlanQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a billing plan item of a sales order.
     # 
-    remote function getSalesOrderOfA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderBillingPlanItemExpandOptions \$expand = [], SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderBillingPlanItem(string SalesOrder, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderBillingPlanItemExpandOptions \$expand = [], SalesOrderOfA_SalesOrderBillingPlanItemSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderBillingPlanItemQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a header partner.
     # 
-    remote function getSalesOrderOfA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderHeaderPartnerExpandOptions \$expand = [], SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderHeaderPartnerQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderHeaderPartnerExpandOptions \$expand = [], SalesOrderOfA_SalesOrderHeaderPartnerSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderHeaderPartnerQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a pricing element.
     # 
-    remote function getSalesOrderOfA_SalesOrderHeaderPrElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderHeaderPrElementExpandOptions \$expand = [], SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderHeaderPrElementQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderHeaderPrElement(string SalesOrder, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderHeaderPrElementExpandOptions \$expand = [], SalesOrderOfA_SalesOrderHeaderPrElementSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderHeaderPrElementQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header of a sales order item.
     # 
-    remote function getSalesOrderOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for an item billing plan.
     # 
-    remote function getSalesOrderOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemBillingPlanQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header of a partner function of a sales order item.
     # 
-    remote function getSalesOrderOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPartnerExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPartnerSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemPartnerQueries queries) returns A_SalesOrderWrapper|error;
 
     # Get related to_SalesOrder
     # 
-    remote function getSalesOrderOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemPartnerAddress(string SalesOrder, string SalesOrderItem, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPartnerAddressExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPartnerAddressSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemPartnerAddressQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a pricing element.
     # 
-    remote function getSalesOrderOfA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPrElementExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPrElementSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemPrElement(string SalesOrder, string SalesOrderItem, string PricingProcedureStep, string PricingProcedureCounter, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemPrElementExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemPrElementSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemPrElementQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a related object of a sales order item.
     # 
-    remote function getSalesOrderOfA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemRelatedObjectExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemRelatedObject(string SalesOrder, string SalesOrderItem, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemRelatedObjectExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemRelatedObjectSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemRelatedObjectQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a text of a sales order item.
     # 
-    remote function getSalesOrderOfA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemTextExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItemTextQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItemText(string SalesOrder, string SalesOrderItem, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItemTextExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItemTextSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItemTextQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header data of a preceding item of a sales order.
     # 
-    remote function getSalesOrderOfA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItmPrecdgProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItmPrecdgProcFlowQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header data for a subsequent item of a sales order.
     # 
-    remote function getSalesOrderOfA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderItmSubsqntProcFlow(string SalesOrder, string SalesOrderItem, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderItmSubsqntProcFlowQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order for a header partner address.
     # 
-    remote function getSalesOrderOfA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderPartnerAddressExpandOptions \$expand = [], SalesOrderOfA_SalesOrderPartnerAddressSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderPartnerAddress(string SalesOrder, string PartnerFunction, string AddressRepresentationCode, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderPartnerAddressExpandOptions \$expand = [], SalesOrderOfA_SalesOrderPartnerAddressSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderPartnerAddressQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header data for a preceding document of a sales order.
     # 
-    remote function getSalesOrderOfA_SalesOrderPrecdgProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderPrecdgProcFlowQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderPrecdgProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderPrecdgProcFlowSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderPrecdgProcFlowQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a related object.
     # 
-    remote function getSalesOrderOfA_SalesOrderRelatedObject(string SalesOrder, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderRelatedObjectExpandOptions \$expand = [], SalesOrderOfA_SalesOrderRelatedObjectSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderRelatedObjectQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderRelatedObject(string SalesOrder, string SDDocRelatedObjectSequenceNmbr, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderRelatedObjectExpandOptions \$expand = [], SalesOrderOfA_SalesOrderRelatedObjectSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderRelatedObjectQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header data for a subsequent document of a sales order.
     # 
-    remote function getSalesOrderOfA_SalesOrderSubsqntProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderSubsqntProcFlowQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderSubsqntProcFlow(string SalesOrder, string DocRelationshipUUID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], SalesOrderOfA_SalesOrderSubsqntProcFlowSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderSubsqntProcFlowQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a header text.
     # 
-    remote function getSalesOrderOfA_SalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderTextExpandOptions \$expand = [], SalesOrderOfA_SalesOrderTextSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SalesOrderTextQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SalesOrderText(string SalesOrder, string Language, string LongTextID, map<string|string[]> headers = {}, SalesOrderOfA_SalesOrderTextExpandOptions \$expand = [], SalesOrderOfA_SalesOrderTextSelectOptions \$select = [], GetSalesOrderOfA_SalesOrderTextQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for a payment plan item.
     # 
-    remote function getSalesOrderOfA_SlsOrdPaymentPlanItemDetails(string SalesOrder, string PaymentPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], SalesOrderOfA_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SlsOrdPaymentPlanItemDetailsQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SlsOrdPaymentPlanItemDetails(string SalesOrder, string PaymentPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], SalesOrderOfA_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], GetSalesOrderOfA_SlsOrdPaymentPlanItemDetailsQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the sales order header for an item billing plan item.
     # 
-    remote function getSalesOrderOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], anydata Additional Values, GetSalesOrderOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderWrapper|error;
+    remote function getSalesOrderOfA_SlsOrderItemBillingPlanItem(string SalesOrder, string SalesOrderItem, string BillingPlan, string BillingPlanItem, map<string|string[]> headers = {}, SalesOrderOfA_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], SalesOrderOfA_SlsOrderItemBillingPlanItemSelectOptions \$select = [], GetSalesOrderOfA_SlsOrderItemBillingPlanItemQueries queries) returns A_SalesOrderWrapper|error;
 
     # Reads the billing plan items of all sales orders.
     # 
-    remote function listA_SalesOrderBillingPlanItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderBillingPlanItemOrderByOptions \$orderby = [], A_SalesOrderBillingPlanItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderBillingPlanItemSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderBillingPlanItemsQueries queries) returns CollectionOfA_SalesOrderBillingPlanItemWrapper|error;
+    remote function listA_SalesOrderBillingPlanItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderBillingPlanItemOrderByOptions \$orderby = [], A_SalesOrderBillingPlanItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderBillingPlanItemSelectOptions \$select = [], ListA_SalesOrderBillingPlanItemsQueries queries) returns CollectionOfA_SalesOrderBillingPlanItemWrapper|error;
 
     # Reads the billing plans of all sales orders.
     # 
-    remote function listA_SalesOrderBillingPlans(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderBillingPlanOrderByOptions \$orderby = [], A_SalesOrderBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderBillingPlanSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderBillingPlansQueries queries) returns CollectionOfA_SalesOrderBillingPlanWrapper|error;
+    remote function listA_SalesOrderBillingPlans(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderBillingPlanOrderByOptions \$orderby = [], A_SalesOrderBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderBillingPlanSelectOptions \$select = [], ListA_SalesOrderBillingPlansQueries queries) returns CollectionOfA_SalesOrderBillingPlanWrapper|error;
 
     # Reads the header partners of all sales orders.
     # 
-    remote function listA_SalesOrderHeaderPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderHeaderPartnerOrderByOptions \$orderby = [], A_SalesOrderHeaderPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderHeaderPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderHeaderPartnersQueries queries) returns CollectionOfA_SalesOrderHeaderPartnerWrapper|error;
+    remote function listA_SalesOrderHeaderPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderHeaderPartnerOrderByOptions \$orderby = [], A_SalesOrderHeaderPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderHeaderPartnerSelectOptions \$select = [], ListA_SalesOrderHeaderPartnersQueries queries) returns CollectionOfA_SalesOrderHeaderPartnerWrapper|error;
 
     # Reads the header pricing elements of all sales orders.
     # 
-    remote function listA_SalesOrderHeaderPrElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderHeaderPrElementOrderByOptions \$orderby = [], A_SalesOrderHeaderPrElementExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderHeaderPrElementSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderHeaderPrElementsQueries queries) returns CollectionOfA_SalesOrderHeaderPrElementWrapper|error;
+    remote function listA_SalesOrderHeaderPrElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderHeaderPrElementOrderByOptions \$orderby = [], A_SalesOrderHeaderPrElementExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderHeaderPrElementSelectOptions \$select = [], ListA_SalesOrderHeaderPrElementsQueries queries) returns CollectionOfA_SalesOrderHeaderPrElementWrapper|error;
 
     # Reads the billing plans of all sales order items.
     # 
-    remote function listA_SalesOrderItemBillingPlans(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemBillingPlanOrderByOptions \$orderby = [], A_SalesOrderItemBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemBillingPlansQueries queries) returns CollectionOfA_SalesOrderItemBillingPlanWrapper|error;
+    remote function listA_SalesOrderItemBillingPlans(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemBillingPlanOrderByOptions \$orderby = [], A_SalesOrderItemBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemBillingPlanSelectOptions \$select = [], ListA_SalesOrderItemBillingPlansQueries queries) returns CollectionOfA_SalesOrderItemBillingPlanWrapper|error;
 
     # Reads all addresses for item partners of sales orders.
     # 
-    remote function listA_SalesOrderItemPartnerAddresses(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemPartnerAddressesQueries queries) returns CollectionOfA_SalesOrderItemPartnerAddressWrapper|error;
+    remote function listA_SalesOrderItemPartnerAddresses(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerAddressSelectOptions \$select = [], ListA_SalesOrderItemPartnerAddressesQueries queries) returns CollectionOfA_SalesOrderItemPartnerAddressWrapper|error;
 
     # Reads the item partners for all sales orders.
     # 
-    remote function listA_SalesOrderItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerOrderByOptions \$orderby = [], A_SalesOrderItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemPartnersQueries queries) returns CollectionOfA_SalesOrderItemPartnerWrapper|error;
+    remote function listA_SalesOrderItemPartners(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerOrderByOptions \$orderby = [], A_SalesOrderItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerSelectOptions \$select = [], ListA_SalesOrderItemPartnersQueries queries) returns CollectionOfA_SalesOrderItemPartnerWrapper|error;
 
     # Reads the item pricing elements of all sales orders.
     # 
-    remote function listA_SalesOrderItemPrElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPrElementOrderByOptions \$orderby = [], A_SalesOrderItemPrElementExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPrElementSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemPrElementsQueries queries) returns CollectionOfA_SalesOrderItemPrElementWrapper|error;
+    remote function listA_SalesOrderItemPrElements(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPrElementOrderByOptions \$orderby = [], A_SalesOrderItemPrElementExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPrElementSelectOptions \$select = [], ListA_SalesOrderItemPrElementsQueries queries) returns CollectionOfA_SalesOrderItemPrElementWrapper|error;
 
     # Reads related objects from the items of all sales orders.
     # 
-    remote function listA_SalesOrderItemRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemRelatedObjectsQueries queries) returns CollectionOfA_SalesOrderItemRelatedObjectWrapper|error;
+    remote function listA_SalesOrderItemRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemRelatedObjectSelectOptions \$select = [], ListA_SalesOrderItemRelatedObjectsQueries queries) returns CollectionOfA_SalesOrderItemRelatedObjectWrapper|error;
 
     # Reads item texts of all sales orders.
     # 
-    remote function listA_SalesOrderItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemTextOrderByOptions \$orderby = [], A_SalesOrderItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemTextsQueries queries) returns CollectionOfA_SalesOrderItemTextWrapper|error;
+    remote function listA_SalesOrderItemTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemTextOrderByOptions \$orderby = [], A_SalesOrderItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemTextSelectOptions \$select = [], ListA_SalesOrderItemTextsQueries queries) returns CollectionOfA_SalesOrderItemTextWrapper|error;
 
     # Reads all sales order items.
     # 
-    remote function listA_SalesOrderItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemOrderByOptions \$orderby = [], A_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItemsQueries queries) returns CollectionOfA_SalesOrderItemWrapper|error;
+    remote function listA_SalesOrderItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemOrderByOptions \$orderby = [], A_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemSelectOptions \$select = [], ListA_SalesOrderItemsQueries queries) returns CollectionOfA_SalesOrderItemWrapper|error;
 
     # Reads the preceding items of all sales orders items.
     # 
-    remote function listA_SalesOrderItmPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItmPrecdgProcFlowOrderByOptions \$orderby = [], A_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItmPrecdgProcFlowsQueries queries) returns CollectionOfA_SalesOrderItmPrecdgProcFlowWrapper|error;
+    remote function listA_SalesOrderItmPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItmPrecdgProcFlowOrderByOptions \$orderby = [], A_SalesOrderItmPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItmPrecdgProcFlowSelectOptions \$select = [], ListA_SalesOrderItmPrecdgProcFlowsQueries queries) returns CollectionOfA_SalesOrderItmPrecdgProcFlowWrapper|error;
 
     # Reads the subsequent items of all sales orders items.
     # 
-    remote function listA_SalesOrderItmSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItmSubsqntProcFlowOrderByOptions \$orderby = [], A_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderItmSubsqntProcFlowsQueries queries) returns CollectionOfA_SalesOrderItmSubsqntProcFlowWrapper|error;
+    remote function listA_SalesOrderItmSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItmSubsqntProcFlowOrderByOptions \$orderby = [], A_SalesOrderItmSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItmSubsqntProcFlowSelectOptions \$select = [], ListA_SalesOrderItmSubsqntProcFlowsQueries queries) returns CollectionOfA_SalesOrderItmSubsqntProcFlowWrapper|error;
 
     # Reads all addresses for header partners of sales orders.
     # 
-    remote function listA_SalesOrderPartnerAddresses(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderPartnerAddressSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderPartnerAddressesQueries queries) returns CollectionOfA_SalesOrderPartnerAddressWrapper|error;
+    remote function listA_SalesOrderPartnerAddresses(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderPartnerAddressSelectOptions \$select = [], ListA_SalesOrderPartnerAddressesQueries queries) returns CollectionOfA_SalesOrderPartnerAddressWrapper|error;
 
     # Reads the preceding documents of all sales orders.
     # 
-    remote function listA_SalesOrderPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderPrecdgProcFlowOrderByOptions \$orderby = [], A_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderPrecdgProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderPrecdgProcFlowsQueries queries) returns CollectionOfA_SalesOrderPrecdgProcFlowWrapper|error;
+    remote function listA_SalesOrderPrecdgProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderPrecdgProcFlowOrderByOptions \$orderby = [], A_SalesOrderPrecdgProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderPrecdgProcFlowSelectOptions \$select = [], ListA_SalesOrderPrecdgProcFlowsQueries queries) returns CollectionOfA_SalesOrderPrecdgProcFlowWrapper|error;
 
     # Reads related objects from the headers of all sales orders.
     # 
-    remote function listA_SalesOrderRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderRelatedObjectsQueries queries) returns CollectionOfA_SalesOrderRelatedObjectWrapper|error;
+    remote function listA_SalesOrderRelatedObjects(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderRelatedObjectSelectOptions \$select = [], ListA_SalesOrderRelatedObjectsQueries queries) returns CollectionOfA_SalesOrderRelatedObjectWrapper|error;
 
     # Reads the schedule lines of all sales orders.
     # 
-    remote function listA_SalesOrderScheduleLines(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderScheduleLineOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderScheduleLineSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderScheduleLinesQueries queries) returns CollectionOfA_SalesOrderScheduleLineWrapper|error;
+    remote function listA_SalesOrderScheduleLines(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderScheduleLineOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderScheduleLineSelectOptions \$select = [], ListA_SalesOrderScheduleLinesQueries queries) returns CollectionOfA_SalesOrderScheduleLineWrapper|error;
 
     # Reads the subsequent documents of all sales orders.
     # 
-    remote function listA_SalesOrderSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderSubsqntProcFlowOrderByOptions \$orderby = [], A_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderSubsqntProcFlowSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderSubsqntProcFlowsQueries queries) returns CollectionOfA_SalesOrderSubsqntProcFlowWrapper|error;
+    remote function listA_SalesOrderSubsqntProcFlows(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderSubsqntProcFlowOrderByOptions \$orderby = [], A_SalesOrderSubsqntProcFlowExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderSubsqntProcFlowSelectOptions \$select = [], ListA_SalesOrderSubsqntProcFlowsQueries queries) returns CollectionOfA_SalesOrderSubsqntProcFlowWrapper|error;
 
     # Reads the header texts of all sales orders.
     # 
-    remote function listA_SalesOrderTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderTextOrderByOptions \$orderby = [], A_SalesOrderTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderTextSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrderTextsQueries queries) returns CollectionOfA_SalesOrderTextWrapper|error;
+    remote function listA_SalesOrderTexts(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderTextOrderByOptions \$orderby = [], A_SalesOrderTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderTextSelectOptions \$select = [], ListA_SalesOrderTextsQueries queries) returns CollectionOfA_SalesOrderTextWrapper|error;
 
     # Reads all sales order headers.
     # 
-    remote function listA_SalesOrders(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderOrderByOptions \$orderby = [], A_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListA_SalesOrdersQueries queries) returns CollectionOfA_SalesOrderWrapper|error;
+    remote function listA_SalesOrders(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderOrderByOptions \$orderby = [], A_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderSelectOptions \$select = [], ListA_SalesOrdersQueries queries) returns CollectionOfA_SalesOrderWrapper|error;
 
     # Reads the payment plans of all sales orders.
     # 
-    remote function listA_SlsOrdPaymentPlanItemDetails(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrdPaymentPlanItemDetailsOrderByOptions \$orderby = [], A_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], anydata Additional Values, ListA_SlsOrdPaymentPlanItemDetailsQueries queries) returns CollectionOfA_SlsOrdPaymentPlanItemDetailsWrapper|error;
+    remote function listA_SlsOrdPaymentPlanItemDetails(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrdPaymentPlanItemDetailsOrderByOptions \$orderby = [], A_SlsOrdPaymentPlanItemDetailsExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrdPaymentPlanItemDetailsSelectOptions \$select = [], ListA_SlsOrdPaymentPlanItemDetailsQueries queries) returns CollectionOfA_SlsOrdPaymentPlanItemDetailsWrapper|error;
 
     # Reads the billing plan items of all sales order items.
     # 
-    remote function listA_SlsOrderItemBillingPlanItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrderItemBillingPlanItemOrderByOptions \$orderby = [], A_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrderItemBillingPlanItemSelectOptions \$select = [], anydata Additional Values, ListA_SlsOrderItemBillingPlanItemsQueries queries) returns CollectionOfA_SlsOrderItemBillingPlanItemWrapper|error;
+    remote function listA_SlsOrderItemBillingPlanItems(map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SlsOrderItemBillingPlanItemOrderByOptions \$orderby = [], A_SlsOrderItemBillingPlanItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SlsOrderItemBillingPlanItemSelectOptions \$select = [], ListA_SlsOrderItemBillingPlanItemsQueries queries) returns CollectionOfA_SlsOrderItemBillingPlanItemWrapper|error;
 
     # Reads the address of a sales order header partner.
     # 
-    remote function listAddressesOfA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", AddressOfA_SalesOrderHeaderPartnerOrderByOptions \$orderby = [], AddressOfA_SalesOrderHeaderPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", AddressOfA_SalesOrderHeaderPartnerSelectOptions \$select = [], anydata Additional Values, ListAddressesOfA_SalesOrderHeaderPartnerQueries queries) returns CollectionOfA_SalesOrderPartnerAddressWrapper|error;
+    remote function listAddressesOfA_SalesOrderHeaderPartner(string SalesOrder, string PartnerFunction, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", AddressOfA_SalesOrderHeaderPartnerOrderByOptions \$orderby = [], AddressOfA_SalesOrderHeaderPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", AddressOfA_SalesOrderHeaderPartnerSelectOptions \$select = [], ListAddressesOfA_SalesOrderHeaderPartnerQueries queries) returns CollectionOfA_SalesOrderPartnerAddressWrapper|error;
 
     # Reads the item address of a sales order item partner.
     # 
-    remote function listAddressesOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerAddressSelectOptions \$select = [], anydata Additional Values, ListAddressesOfA_SalesOrderItemPartnerQueries queries) returns CollectionOfA_SalesOrderItemPartnerAddressWrapper|error;
+    remote function listAddressesOfA_SalesOrderItemPartner(string SalesOrder, string SalesOrderItem, string PartnerFunction, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerAddressOrderByOptions \$orderby = [], A_SalesOrderItemPartnerAddressExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerAddressSelectOptions \$select = [], ListAddressesOfA_SalesOrderItemPartnerQueries queries) returns CollectionOfA_SalesOrderItemPartnerAddressWrapper|error;
 
     # Reads the billing plan items of a sales order billing plan.
     # 
-    remote function listBillingPlanItemsOfA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", BillingPlanItemOfA_SalesOrderBillingPlanOrderByOptions \$orderby = [], BillingPlanItemOfA_SalesOrderBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions \$select = [], anydata Additional Values, ListBillingPlanItemsOfA_SalesOrderBillingPlanQueries queries) returns CollectionOfA_SalesOrderBillingPlanItemWrapper|error;
+    remote function listBillingPlanItemsOfA_SalesOrderBillingPlan(string SalesOrder, string BillingPlan, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", BillingPlanItemOfA_SalesOrderBillingPlanOrderByOptions \$orderby = [], BillingPlanItemOfA_SalesOrderBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", BillingPlanItemOfA_SalesOrderBillingPlanSelectOptions \$select = [], ListBillingPlanItemsOfA_SalesOrderBillingPlanQueries queries) returns CollectionOfA_SalesOrderBillingPlanItemWrapper|error;
 
     # Reads the billing plan items of a sales order item billing plan.
     # 
-    remote function listBillingPlanItemsOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", BillingPlanItemOfA_SalesOrderItemBillingPlanOrderByOptions \$orderby = [], BillingPlanItemOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], anydata Additional Values, ListBillingPlanItemsOfA_SalesOrderItemBillingPlanQueries queries) returns CollectionOfA_SlsOrderItemBillingPlanItemWrapper|error;
+    remote function listBillingPlanItemsOfA_SalesOrderItemBillingPlan(string SalesOrder, string SalesOrderItem, string BillingPlan, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", BillingPlanItemOfA_SalesOrderItemBillingPlanOrderByOptions \$orderby = [], BillingPlanItemOfA_SalesOrderItemBillingPlanExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", BillingPlanItemOfA_SalesOrderItemBillingPlanSelectOptions \$select = [], ListBillingPlanItemsOfA_SalesOrderItemBillingPlanQueries queries) returns CollectionOfA_SlsOrderItemBillingPlanItemWrapper|error;
 
     # Reads all items of a sales order.
     # 
-    remote function listItemsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemOrderByOptions \$orderby = [], A_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListItemsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderItemWrapper|error;
+    remote function listItemsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemOrderByOptions \$orderby = [], A_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemSelectOptions \$select = [], ListItemsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderItemWrapper|error;
 
     # Reads the header partners of a sales order.
     # 
-    remote function listPartnersOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PartnerOfA_SalesOrderOrderByOptions \$orderby = [], PartnerOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PartnerOfA_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderHeaderPartnerWrapper|error;
+    remote function listPartnersOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PartnerOfA_SalesOrderOrderByOptions \$orderby = [], PartnerOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PartnerOfA_SalesOrderSelectOptions \$select = [], ListPartnersOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderHeaderPartnerWrapper|error;
 
     # Reads the item partners of a specific sales order item.
     # 
-    remote function listPartnersOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerOrderByOptions \$orderby = [], A_SalesOrderItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerSelectOptions \$select = [], anydata Additional Values, ListPartnersOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemPartnerWrapper|error;
+    remote function listPartnersOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemPartnerOrderByOptions \$orderby = [], A_SalesOrderItemPartnerExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemPartnerSelectOptions \$select = [], ListPartnersOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemPartnerWrapper|error;
 
     # Reads the header payment plan of a specific sales order.
     # 
-    remote function listPaymentPlanItemDetailsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PaymentPlanItemDetailsOfA_SalesOrderOrderByOptions \$orderby = [], PaymentPlanItemDetailsOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PaymentPlanItemDetailsOfA_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListPaymentPlanItemDetailsOfA_SalesOrderQueries queries) returns CollectionOfA_SlsOrdPaymentPlanItemDetailsWrapper|error;
+    remote function listPaymentPlanItemDetailsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PaymentPlanItemDetailsOfA_SalesOrderOrderByOptions \$orderby = [], PaymentPlanItemDetailsOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PaymentPlanItemDetailsOfA_SalesOrderSelectOptions \$select = [], ListPaymentPlanItemDetailsOfA_SalesOrderQueries queries) returns CollectionOfA_SlsOrdPaymentPlanItemDetailsWrapper|error;
 
     # Get entities from related to_PrecedingProcFlowDocItem
     # 
-    remote function listPrecedingProcFlowDocItemsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocItemOfA_SalesOrderItemOrderByOptions \$orderby = [], PrecedingProcFlowDocItemOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListPrecedingProcFlowDocItemsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItmPrecdgProcFlowWrapper|error;
+    remote function listPrecedingProcFlowDocItemsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocItemOfA_SalesOrderItemOrderByOptions \$orderby = [], PrecedingProcFlowDocItemOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocItemOfA_SalesOrderItemSelectOptions \$select = [], ListPrecedingProcFlowDocItemsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItmPrecdgProcFlowWrapper|error;
 
     # Get entities from related to_PrecedingProcFlowDoc
     # 
-    remote function listPrecedingProcFlowDocsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocOfA_SalesOrderOrderByOptions \$orderby = [], PrecedingProcFlowDocOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocOfA_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListPrecedingProcFlowDocsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderPrecdgProcFlowWrapper|error;
+    remote function listPrecedingProcFlowDocsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PrecedingProcFlowDocOfA_SalesOrderOrderByOptions \$orderby = [], PrecedingProcFlowDocOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PrecedingProcFlowDocOfA_SalesOrderSelectOptions \$select = [], ListPrecedingProcFlowDocsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderPrecdgProcFlowWrapper|error;
 
     # Reads the pricing element of a sales order.
     # 
-    remote function listPricingElementsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesOrderOrderByOptions \$orderby = [], PricingElementOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderHeaderPrElementWrapper|error;
+    remote function listPricingElementsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesOrderOrderByOptions \$orderby = [], PricingElementOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesOrderSelectOptions \$select = [], ListPricingElementsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderHeaderPrElementWrapper|error;
 
     # Reads the pricing element of a sales order item.
     # 
-    remote function listPricingElementsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesOrderItemOrderByOptions \$orderby = [], PricingElementOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListPricingElementsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemPrElementWrapper|error;
+    remote function listPricingElementsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", PricingElementOfA_SalesOrderItemOrderByOptions \$orderby = [], PricingElementOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", PricingElementOfA_SalesOrderItemSelectOptions \$select = [], ListPricingElementsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemPrElementWrapper|error;
 
     # Reads the related objects of a sales order header.
     # 
-    remote function listRelatedObjectsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListRelatedObjectsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderRelatedObjectWrapper|error;
+    remote function listRelatedObjectsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderRelatedObjectSelectOptions \$select = [], ListRelatedObjectsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderRelatedObjectWrapper|error;
 
     # Reads the related object of a sales order item.
     # 
-    remote function listRelatedObjectsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemRelatedObjectSelectOptions \$select = [], anydata Additional Values, ListRelatedObjectsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemRelatedObjectWrapper|error;
+    remote function listRelatedObjectsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemRelatedObjectOrderByOptions \$orderby = [], A_SalesOrderItemRelatedObjectExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemRelatedObjectSelectOptions \$select = [], ListRelatedObjectsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemRelatedObjectWrapper|error;
 
     # Reads the schedule lines of a sales order item.
     # 
-    remote function listScheduleLinesOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ScheduleLineOfA_SalesOrderItemOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", ScheduleLineOfA_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListScheduleLinesOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderScheduleLineWrapper|error;
+    remote function listScheduleLinesOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", ScheduleLineOfA_SalesOrderItemOrderByOptions \$orderby = [], "allpages"|"none" \$inlinecount = "allpages", ScheduleLineOfA_SalesOrderItemSelectOptions \$select = [], ListScheduleLinesOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderScheduleLineWrapper|error;
 
     # Get entities from related to_SubsequentProcFlowDocItem
     # 
-    remote function listSubsequentProcFlowDocItemsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocItemOfA_SalesOrderItemOrderByOptions \$orderby = [], SubsequentProcFlowDocItemOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocItemOfA_SalesOrderItemSelectOptions \$select = [], anydata Additional Values, ListSubsequentProcFlowDocItemsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItmSubsqntProcFlowWrapper|error;
+    remote function listSubsequentProcFlowDocItemsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocItemOfA_SalesOrderItemOrderByOptions \$orderby = [], SubsequentProcFlowDocItemOfA_SalesOrderItemExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocItemOfA_SalesOrderItemSelectOptions \$select = [], ListSubsequentProcFlowDocItemsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItmSubsqntProcFlowWrapper|error;
 
     # Get entities from related to_SubsequentProcFlowDoc
     # 
-    remote function listSubsequentProcFlowDocsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocOfA_SalesOrderOrderByOptions \$orderby = [], SubsequentProcFlowDocOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocOfA_SalesOrderSelectOptions \$select = [], anydata Additional Values, ListSubsequentProcFlowDocsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderSubsqntProcFlowWrapper|error;
+    remote function listSubsequentProcFlowDocsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", SubsequentProcFlowDocOfA_SalesOrderOrderByOptions \$orderby = [], SubsequentProcFlowDocOfA_SalesOrderExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", SubsequentProcFlowDocOfA_SalesOrderSelectOptions \$select = [], ListSubsequentProcFlowDocsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderSubsqntProcFlowWrapper|error;
 
     # Reads the header texts of a sales order.
     # 
-    remote function listTextsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderTextOrderByOptions \$orderby = [], A_SalesOrderTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderTextWrapper|error;
+    remote function listTextsOfA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderTextOrderByOptions \$orderby = [], A_SalesOrderTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderTextSelectOptions \$select = [], ListTextsOfA_SalesOrderQueries queries) returns CollectionOfA_SalesOrderTextWrapper|error;
 
     # Reads the text of a sales order item.
     # 
-    remote function listTextsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemTextOrderByOptions \$orderby = [], A_SalesOrderItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemTextSelectOptions \$select = [], anydata Additional Values, ListTextsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemTextWrapper|error;
+    remote function listTextsOfA_SalesOrderItem(string SalesOrder, string SalesOrderItem, map<string|string[]> headers = {}, int \$skip = 0, int \$top = 0, string \$filter = "", A_SalesOrderItemTextOrderByOptions \$orderby = [], A_SalesOrderItemTextExpandOptions \$expand = [], "allpages"|"none" \$inlinecount = "allpages", A_SalesOrderItemTextSelectOptions \$select = [], ListTextsOfA_SalesOrderItemQueries queries) returns CollectionOfA_SalesOrderItemTextWrapper|error;
 
     # Updates a sales order.
     # 
@@ -5390,9 +5479,9 @@
 
     # Invoke action rejectApprovalRequest
     # 
-    remote function rejectApprovalRequest(map<string|string[]> headers = {}, string SalesOrder = "", anydata Additional Values, RejectApprovalRequestQueries queries) returns FunctionResult_1|error;
+    remote function rejectApprovalRequest(map<string|string[]> headers = {}, string SalesOrder = "", RejectApprovalRequestQueries queries) returns FunctionResult_1|error;
 
     # Invoke action releaseApprovalRequest
     # 
-    remote function releaseApprovalRequest(map<string|string[]> headers = {}, string SalesOrder = "", anydata Additional Values, ReleaseApprovalRequestQueries queries) returns FunctionResult_2|error;
+    remote function releaseApprovalRequest(map<string|string[]> headers = {}, string SalesOrder = "", ReleaseApprovalRequestQueries queries) returns FunctionResult_2|error;
 }
`````

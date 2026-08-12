# hubspot.crm.lists — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.lists` |
| **Old file** | `hubspot.crm.lists/old/ballerinax_hubspot.crm.lists.bal.txt` |
| **New file** | `hubspot.crm.lists/new/ballerinax_hubspot.crm.lists.bal.txt` |
| **Old lines** | 1860 |
| **New lines** | 1861 |
| **Lines added** | 115 |
| **Lines removed** | 114 |
| **Hunks** | 36 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 335 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 261–267 | 261–267 | Types | +1 | −1 |
| 2 | 270–282 | 270–282 | Types | +2 | −2 |
| 3 | 321–327 | 321–327 | Types | +1 | −1 |
| 4 | 334–340 | 334–340 | Types | +1 | −1 |
| 5 | 369–379 | 369–379 | Types | +2 | −2 |
| 6 | 399–409 | 399–409 | Types | +2 | −2 |
| 7 | 420–426 | 420–426 | Types | +1 | −1 |
| 8 | 450–474 | 450–474 | Types | +7 | −7 |
| 9 | 490–542 | 490–542 | Types | +18 | −18 |
| 10 | 545–652 | 545–652 | Types | +33 | −33 |
| 11 | 697–703 | 697–703 | Types | +1 | −1 |
| 12 | 712–722 | 712–722 | Types | +2 | −2 |
| 13 | 877–883 | 877–883 | Types | +1 | −1 |
| 14 | 1057–1063 | 1057–1063 | Types | +1 | −1 |
| 15 | 1108–1114 | 1108–1114 | Types | +1 | −1 |
| 16 | 1225–1231 | 1225–1231 | Types | +1 | −1 |
| 17 | 1235–1283 | 1235–1283 | Types | +15 | −15 |
| 18 | 1292–1310 | 1292–1310 | Types | +4 | −4 |
| 19 | 1317–1327 | 1317–1327 | Types | +2 | −2 |
| 20 | 1340–1348 | 1340–1348 | Types | +2 | −2 |
| 21 | 1369–1375 | 1369–1375 | Types | +1 | −1 |
| 22 | 1407–1413 | 1407–1413 | Types | +1 | −1 |
| 23 | 1436–1441 | 1436–1442 | Types | +1 | −0 |
| 24 | 1594–1600 | 1595–1601 | Types | +1 | −1 |
| 25 | 1625–1631 | 1626–1632 | Types | +1 | −1 |
| 26 | 1640–1646 | 1641–1647 | Types | +1 | −1 |
| 27 | 1746–1752 | 1747–1753 | Types | +1 | −1 |
| 28 | 1760–1766 | 1761–1767 | Client | +1 | −1 |
| 29 | 1768–1774 | 1769–1775 | Client | +1 | −1 |
| 30 | 1776–1782 | 1777–1783 | Client | +1 | −1 |
| 31 | 1792–1798 | 1793–1799 | Client | +1 | −1 |
| 32 | 1800–1806 | 1801–1807 | Client | +1 | −1 |
| 33 | 1812–1822 | 1813–1823 | Client | +2 | −2 |
| 34 | 1828–1834 | 1829–1835 | Client | +1 | −1 |
| 35 | 1836–1842 | 1837–1843 | Client | +1 | −1 |
| 36 | 1848–1854 | 1849–1855 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.crm.lists/old/ballerinax_hubspot.crm.lists.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.lists/new/ballerinax_hubspot.crm.lists.bal.txt	2026-08-12 13:19:19
@@ -261,7 +261,7 @@
     # The comparison operator applied to the datetime property value
     string operator;
     # The reference timestamp (int32) used in the datetime comparison
-    ballerina/lang.int:0.0.0:Signed32 timestamp;
+    int:Signed32 timestamp;
 };
 
 # A property operation that filters records where a date value falls within a specified range
@@ -270,13 +270,13 @@
     # Whether to include objects with no value set for this property
     boolean includeObjectsWithNoValueSet;
     # The upper bound of the date range as an integer value
-    ballerina/lang.int:0.0.0:Signed32 upperBound;
+    int:Signed32 upperBound;
     # Whether the date value requires time zone conversion
     boolean requiresTimeZoneConversion;
     # The operation type identifier, always set to RANGED_DATE
     "RANGED_DATE" operationType?;
     # The lower bound of the date range as an integer value
-    ballerina/lang.int:0.0.0:Signed32 lowerBound;
+    int:Signed32 lowerBound;
     # The comparison operator applied to the ranged date property
     string operator;
 };
@@ -321,7 +321,7 @@
     # The operation type identifier; always set to ROLLING_DATE_RANGE
     "ROLLING_DATE_RANGE" operationType?;
     # The number of days defining the rolling date range window
-    ballerina/lang.int:0.0.0:Signed32 numberOfDays;
+    int:Signed32 numberOfDays;
     # The comparison operator applied within the rolling date range
     string operator;
 };
@@ -334,7 +334,7 @@
     # The operation type identifier, fixed as ROLLING_PROPERTY_UPDATED
     "ROLLING_PROPERTY_UPDATED" operationType?;
     # The number of days in the rolling window for the property update check
-    ballerina/lang.int:0.0.0:Signed32 numberOfDays;
+    int:Signed32 numberOfDays;
     # The comparison operator applied in the rolling property updated operation
     string operator;
 };
@@ -369,11 +369,11 @@
     # Whether to include records with no value set for the property
     boolean includeObjectsWithNoValueSet;
     # The inclusive upper bound of the numeric range
-    ballerina/lang.int:0.0.0:Signed32 upperBound;
+    int:Signed32 upperBound;
     # The operation type identifier; always 'NUMBER_RANGED'
     "NUMBER_RANGED" operationType?;
     # The inclusive lower bound of the numeric range
-    ballerina/lang.int:0.0.0:Signed32 lowerBound;
+    int:Signed32 lowerBound;
     # The comparison operator applied to evaluate the numeric range
     string operator;
 };
@@ -399,11 +399,11 @@
     # The month component of the target date for the filter operation
     string month;
     # The year component of the target date for the filter operation
-    ballerina/lang.int:0.0.0:Signed32 year;
+    int:Signed32 year;
     # Operation type identifier, fixed as 'DATE'
     "DATE" operationType?;
     # The day component of the target date for the filter operation
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # The comparison operator applied to the date property value
     string operator;
 };
@@ -420,7 +420,7 @@
     # Discriminator identifying this operation as type CALENDAR_DATE
     "CALENDAR_DATE" operationType?;
     # Number of time units used in the calendar date evaluation
-    ballerina/lang.int:0.0.0:Signed32 timeUnitCount?;
+    int:Signed32 timeUnitCount?;
     # The comparison operator applied to the date property
     string operator;
     # The unit of time used for the date property operation
@@ -450,25 +450,25 @@
 
 type PublicDatePoint record {
     # The month component of the date point (1–12)
-    ballerina/lang.int:0.0.0:Signed32 month;
+    int:Signed32 month;
     # The hour component of the time (0–23)
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The year component of the date point
-    ballerina/lang.int:0.0.0:Signed32 year;
+    int:Signed32 year;
     # The source used to determine the time zone
     string timezoneSource?;
     # The millisecond component of the time (0–999)
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # The time type identifier, fixed as 'DATE'
     "DATE" timeType?;
     # The IANA time zone ID used to interpret the date point
     string zoneId;
     # The day component of the date point (1–31)
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # The minute component of the time (0–59)
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the date-time value
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # A time point defined relative to a named index reference such as now, today, or a fiscal period
@@ -490,53 +490,53 @@
 
 type PublicIndexOffset record {
     # Milliseconds component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 milliseconds?;
+    int:Signed32 milliseconds?;
     # Hours component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 hours?;
+    int:Signed32 hours?;
     # Seconds component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 seconds?;
+    int:Signed32 seconds?;
     # Months component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 months?;
+    int:Signed32 months?;
     # Weeks component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 weeks?;
-    # Minutes component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 minutes?;
+    int:Signed32 weeks?;
+    # Minutes component of the time offset
+    int:Signed32 minutes?;
     # Quarters component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 quarters?;
+    int:Signed32 quarters?;
     # Days component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 days?;
+    int:Signed32 days?;
     # Years component of the time offset
-    ballerina/lang.int:0.0.0:Signed32 years?;
+    int:Signed32 years?;
 };
 
 # A relative date reference representing the current moment, with optional time offset components
 
 type PublicNowReference record {
     # The hour component of the now reference time
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # Millisecond component of the current time reference
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # Reference type identifier, fixed value 'NOW'
     "NOW" referenceType?;
     # Minute component of the current time reference
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # Second component of the current time reference
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # A relative date reference representing today, with optional time components for precise intraday targeting
 
 type PublicTodayReference record {
     # The hour component of the today reference time
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The millisecond component of the today reference time
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # The reference type identifier, fixed value 'TODAY'
     "TODAY" referenceType?;
     # The minute component of the today reference time
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the today reference time
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # A time reference anchored to a specific day and optional time within a week
@@ -545,108 +545,108 @@
     # The day of the week for the reference point
     "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY" dayOfWeek;
     # The hour component of the week reference time
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The millisecond component of the week reference time
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # The reference type identifier, fixed value 'WEEK'
     "WEEK" referenceType?;
     # The minute component of the week reference time
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the week reference time
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # Defines a fiscal quarter time reference with date and time components
 
 type PublicFiscalQuarterReference record {
     # The hour component of the fiscal quarter reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The month component of the fiscal quarter reference date
-    ballerina/lang.int:0.0.0:Signed32 month;
+    int:Signed32 month;
     # The millisecond component of the fiscal quarter reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # The reference type identifier, always set to 'FISCAL_QUARTER'
     "FISCAL_QUARTER" referenceType?;
     # The day component of the fiscal quarter reference date
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # The minute component of the fiscal quarter reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the fiscal quarter reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # A time reference point anchored to a fiscal year boundary
 
 type PublicFiscalYearReference record {
     # Hour component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # Month component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 month;
+    int:Signed32 month;
     # Millisecond component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # Discriminator identifying this reference as type FISCAL_YEAR
     "FISCAL_YEAR" referenceType?;
     # Day component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # Minute component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # Second component of the fiscal year reference timestamp
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # A date/time reference anchored to a specific year, with optional time components
 
 type PublicYearReference record {
     # The hour component of the year reference time
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The month component of the year reference date
-    ballerina/lang.int:0.0.0:Signed32 month;
+    int:Signed32 month;
     # The millisecond component of the year reference time
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # Identifies the reference type; always set to 'YEAR'
     "YEAR" referenceType?;
     # The day component of the year reference date
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # The minute component of the year reference time
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the year reference time
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # Represents a quarter-based time reference with specific date and time components for filtering or segmentation
 
 type PublicQuarterReference record {
     # The hour component of the quarter reference time
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # The month component of the quarter reference date
-    ballerina/lang.int:0.0.0:Signed32 month;
+    int:Signed32 month;
     # The millisecond component of the quarter reference time
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # Identifies the reference type; always set to QUARTER for this schema
     "QUARTER" referenceType?;
     # The day component of the quarter reference date
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # The minute component of the quarter reference time
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # The second component of the quarter reference time
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # Defines a time reference anchored to a specific day and time within the current month
 
 type PublicMonthReference record {
     # Hour component of the month-based time reference
-    ballerina/lang.int:0.0.0:Signed32 hour?;
+    int:Signed32 hour?;
     # Millisecond component of the month-based time reference
-    ballerina/lang.int:0.0.0:Signed32 millisecond?;
+    int:Signed32 millisecond?;
     # Reference type identifier, fixed value 'MONTH'
     "MONTH" referenceType?;
     # Day of the month for the time reference
-    ballerina/lang.int:0.0.0:Signed32 day;
+    int:Signed32 day;
     # Minute component of the month-based time reference
-    ballerina/lang.int:0.0.0:Signed32 minute?;
+    int:Signed32 minute?;
     # Second component of the month-based time reference
-    ballerina/lang.int:0.0.0:Signed32 second?;
+    int:Signed32 second?;
 };
 
 # Represents a time value derived from a referenced property, including timezone and reference type configuration
@@ -697,7 +697,7 @@
     # The object type of the associated records being evaluated
     string toObjectType?;
     # Numeric ID identifying the association type
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
     # Category classifying the association relationship
     string associationCategory;
     # Filter type discriminator; always 'ASSOCIATION' for this filter
@@ -712,11 +712,11 @@
 
 type PublicNumOccurrencesRefineBy record {
     # The maximum number of occurrences allowed to match the filter
-    ballerina/lang.int:0.0.0:Signed32 maxOccurrences?;
+    int:Signed32 maxOccurrences?;
     # The refine-by type; always 'NUM_OCCURRENCES'
     "NUM_OCCURRENCES" 'type?;
     # The minimum number of occurrences required to match the filter
-    ballerina/lang.int:0.0.0:Signed32 minOccurrences?;
+    int:Signed32 minOccurrences?;
 };
 
 # Refine-by definition that filters based on a predefined set of occurrence values
@@ -877,7 +877,7 @@
 
 type PublicIntegrationEventFilter record {
     # The numeric ID of the integration event type to filter on
-    ballerina/lang.int:0.0.0:Signed32 eventTypeId;
+    int:Signed32 eventTypeId;
     # The metadata conditions applied to the integration event filter
     PublicEventFilterMetadata[] filterLines;
     # The filter type identifier, always 'INTEGRATION_EVENT'
@@ -1057,7 +1057,7 @@
     # Refines the filter by specifying occurrence count, set, or timestamp-based constraints
     PublicNumOccurrencesRefineBy|PublicSetOccurrencesRefineBy|PublicRelativeComparativeTimestampRefineBy|PublicRelativeRangedTimestampRefineBy|PublicAbsoluteComparativeTimestampRefineBy|PublicAbsoluteRangedTimestampRefineBy|PublicAllHistoryRefineBy|PublicTimePointOperation|PublicRangedTimeOperation coalescingRefineBy;
     # The numeric ID identifying the association type to filter on
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
     # The category of the association type used in the filter
     string associationCategory;
     # The filter type identifier; must be set to NUM_ASSOCIATIONS
@@ -1108,7 +1108,7 @@
 };
 
 # A filter applied within an association branch; one of many supported filter types
-type PublicAssociationFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicAssociationFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # Filter branch scoped to associated object property conditions
 
@@ -1225,7 +1225,7 @@
     # Logical operator applied across the filter branch conditions
     string filterBranchOperator;
     # Numeric ID identifying the association type for this filter branch
-    ballerina/lang.int:0.0.0:Signed32 associationTypeId;
+    int:Signed32 associationTypeId;
     # Category classifying the type of association being filtered
     string associationCategory;
     # Array of filter definitions applied within this association filter branch
@@ -1235,49 +1235,49 @@
 };
 
 # A filter branch node within an association filter, accepting one of several supported branch types including OR, AND, NOT ALL, NOT ANY, restricted, unified events, property association, or association branches
-type PublicAssociationFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicAssociationFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A polymorphic filter branch supporting OR, AND, NOT ALL, NOT ANY, restricted, unified events, property association, and association branch types
-type PublicUnifiedEventsFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicUnifiedEventsFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A filter branch condition for unified events, accepting one of the supported filter types such as property, association, analytics, form submission, email, subscription, campaign, survey, webinar, or list filters
-type PublicUnifiedEventsFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicUnifiedEventsFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # A polymorphic filter branch that resolves to one of the supported branch types: OR, AND, NOT_ALL, NOT_ANY, restricted, unified events, property association, or association
-type PublicRestrictedFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicRestrictedFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A filter applied within a restricted branch; must match exactly one of the supported filter types
-type PublicRestrictedFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicRestrictedFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # A filter branch variant used within a NOT ANY branch, accepting one of several supported filter branch types
-type PublicNotAnyFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicNotAnyFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A union of all supported filter types applicable within a NOT ANY filter branch
-type PublicNotAnyFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicNotAnyFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # A filter branch that accepts one of several supported filter branch types
-type PublicNotAllFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicNotAllFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A union type representing any supported filter variant applicable within a NOT ALL filter branch
-type PublicNotAllFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicNotAllFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # The collection of nested filter branches combined using AND logic. Each branch must be one of the supported filter branch types
-type PublicAndFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicAndFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A union type representing any supported filter that can appear within an AND filter branch
-type PublicAndFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicAndFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # A nested filter branch within an OR branch; one of several supported branch types
-type PublicOrFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicOrFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A filter within an OR branch, represented as one of the supported filter types
-type PublicOrFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicOrFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # A filter branch node within a property association filter, accepting one of several supported branch types including OR, AND, NOT ALL, NOT ANY, restricted, unified events, property association, or association branches
-type PublicPropertyAssociationFilterBranchFilterBranches ballerinax/hubspot.crm.lists:1.0.2:PublicOrFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAndFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAllFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicNotAnyFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicRestrictedFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationFilterBranch|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationFilterBranch;
+type PublicPropertyAssociationFilterBranchFilterBranches PublicOrFilterBranch|PublicAndFilterBranch|PublicNotAllFilterBranch|PublicNotAnyFilterBranch|PublicRestrictedFilterBranch|PublicUnifiedEventsFilterBranch|PublicPropertyAssociationFilterBranch|PublicAssociationFilterBranch;
 
 # A polymorphic filter supporting one of many available filter types for property association branches
-type PublicPropertyAssociationFilterBranchFilters ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPageViewAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCtaAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEventAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicFormSubmissionOnPageFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicIntegrationEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCommunicationSubscriptionFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicCampaignInfluencedFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicSurveyMonkeyValueFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicWebinarFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicEmailEventFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPrivacyAnalyticsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsSearchFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicAdsTimeFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicNumAssociationsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicUnifiedEventsFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyAssociationInListFilter|ballerinax/hubspot.crm.lists:1.0.2:PublicConstantFilter;
+type PublicPropertyAssociationFilterBranchFilters PublicPropertyFilter|PublicAssociationInListFilter|PublicPageViewAnalyticsFilter|PublicCtaAnalyticsFilter|PublicEventAnalyticsFilter|PublicFormSubmissionFilter|PublicFormSubmissionOnPageFilter|PublicIntegrationEventFilter|PublicEmailSubscriptionFilter|PublicCommunicationSubscriptionFilter|PublicCampaignInfluencedFilter|PublicSurveyMonkeyFilter|PublicSurveyMonkeyValueFilter|PublicWebinarFilter|PublicEmailEventFilter|PublicPrivacyAnalyticsFilter|PublicAdsSearchFilter|PublicAdsTimeFilter|PublicInListFilter|PublicNumAssociationsFilter|PublicUnifiedEventsFilter|PublicPropertyAssociationInListFilter|PublicConstantFilter;
 
 # Response containing a single retrieved list folder object
 
@@ -1292,19 +1292,19 @@
     # The time the folder was created at
     string createdAt?;
     # The Id of the folder this folder is in, the root folder is represented as 0
-    ballerina/lang.int:0.0.0:Signed32 parentFolderId;
+    int:Signed32 parentFolderId;
     # Nested subfolders contained within this folder
     PublicListFolder[] childNodes;
     # The name of the folder
     string name?;
     # The Id of the folder
-    ballerina/lang.int:0.0.0:Signed32 id;
+    int:Signed32 id;
     # An array of list Id's contained in this folder
-    ballerina/lang.int:0.0.0:Signed32[] childLists;
+    int:Signed32[] childLists;
     # The time that the contents of the folder was last updated at
     string updatedContentsAt?;
     # The user Id of the owner of the folder
-    ballerina/lang.int:0.0.0:Signed32 userId?;
+    int:Signed32 userId?;
     # The time the folder was last updated at
     string updatedAt?;
 };
@@ -1317,11 +1317,11 @@
 If no value is provided, or if an empty list is provided, then the results will not be filtered by _listId_
     string[] listIds?;
     # Value used to paginate through lists. The _offset_ provided in the response can be used in the next request to fetch the next page of results. Defaults to _0_ if no offset is provided
-    ballerina/lang.int:0.0.0:Signed32 offset?;
+    int:Signed32 offset?;
     # The _query_ that will be used to search for lists by list name. If no _query_ is provided, then the results will include all lists
     string query?;
     # The number of lists to include in the response. Defaults to _20_ if no value is provided. The max _count_ is _500_
-    ballerina/lang.int:0.0.0:Signed32 count?;
+    int:Signed32 count?;
     # The _processingTypes_ that will be used to filter results by _processingType_. If values are provided, then the response will only include results that have a _processingType_ in this array
 
 If no value is provided, or if an empty list is provided, then results will not be filtered by _processingType_
@@ -1340,9 +1340,9 @@
 
 type ListSearchResponse record {
     # The total number of lists that match the search criteria
-    ballerina/lang.int:0.0.0:Signed32 total;
+    int:Signed32 total;
     # Value to be passed in a future request to paginate through list search results
-    ballerina/lang.int:0.0.0:Signed32 offset;
+    int:Signed32 offset;
     # The lists that matched the search criteria
     PublicObjectListSearchResult[] lists;
     # Whether or not there are more results to page through
@@ -1369,7 +1369,7 @@
     # The time when the list was deleted
     string deletedAt?;
     # The version of the list
-    ballerina/lang.int:0.0.0:Signed32 listVersion;
+    int:Signed32 listVersion;
     # The name of the list
     string name;
     # The name and value of any additional properties that exist for this list and that were included in the search request
@@ -1407,7 +1407,7 @@
     # The time when the list was deleted
     string deletedAt?;
     # The version of the list
-    ballerina/lang.int:0.0.0:Signed32 listVersion;
+    int:Signed32 listVersion;
     # The total number of records currently in the list
     int size?;
     # The name of the list
@@ -1436,6 +1436,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -1594,7 +1595,7 @@
 If provided, then the records in the response will be the records preceding the offset, sorted in *descending* order
     string before?;
     # The number of records to return in the response. The maximum _limit_ is 250
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging offset token for the page that comes _after_ the previously requested records
 
 If provided, then the records in the response will be the records following the offset, sorted in *ascending* order. Takes precedence over the _before_ offset
@@ -1625,7 +1626,7 @@
     # The unique identifier of the list
     string listId;
     # The version number of the list at time of membership
-    ballerina/lang.int:0.0.0:Signed32 listVersion;
+    int:Signed32 listVersion;
     # Timestamp of the most recent addition to the list
     string lastAddedTimestamp;
     # Timestamp when the record was first added to the list
@@ -1640,7 +1641,7 @@
 If provided, then the records in the response will be the records preceding the offset, sorted in *descending* order
     string before?;
     # The number of records to return in the response. The maximum _limit_ is 250
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging offset token for the page that comes _after_ the previously requested records
 
 If provided, then the records in the response will be the records following the offset, sorted in *ascending* order. Takes precedence over the _before_ offset
@@ -1746,7 +1747,7 @@
     # The list of custom properties to tie to the list. Custom property name is the key, the value is the value
     record {|string...;|} customProperties?;
     # The ID of the folder that the list should be created in. If left blank, then the list will be created in the root of the list folder structure
-    ballerina/lang.int:0.0.0:Signed32 listFolderId?;
+    int:Signed32 listFolderId?;
     # The name of the list, which must be globally unique across all public lists in the portal
     string name;
     # The root filter branch defining membership criteria for dynamic lists
@@ -1760,7 +1761,7 @@
 
     # Update List Name
     # 
-    remote function putListIdUpdateListNameUpdateName(string listId, map<string|string[]> headers = {}, string listName = "", boolean includeFilters = false, anydata Additional Values, PutListIdUpdateListNameUpdateNameQueries queries) returns ListUpdateResponse|error;
+    remote function putListIdUpdateListNameUpdateName(string listId, map<string|string[]> headers = {}, string listName = "", boolean includeFilters = false, PutListIdUpdateListNameUpdateNameQueries queries) returns ListUpdateResponse|error;
 
     # Add and/or Remove Records from a List
     # 
@@ -1768,7 +1769,7 @@
 
     # Fetch List by ID
     # 
-    remote function getListIdGetById(string listId, map<string|string[]> headers = {}, boolean includeFilters = false, anydata Additional Values, GetListIdGetByIdQueries queries) returns ListFetchResponse|error;
+    remote function getListIdGetById(string listId, map<string|string[]> headers = {}, boolean includeFilters = false, GetListIdGetByIdQueries queries) returns ListFetchResponse|error;
 
     # Delete a List
     # 
@@ -1776,7 +1777,7 @@
 
     # Update List Filter Definition
     # 
-    remote function putListIdUpdateListFiltersUpdateListFilters(string listId, ListFilterUpdateRequest payload, map<string|string[]> headers = {}, boolean enrollObjectsInWorkflows = false, anydata Additional Values, PutListIdUpdateListFiltersUpdateListFiltersQueries queries) returns ListUpdateResponse|error;
+    remote function putListIdUpdateListFiltersUpdateListFilters(string listId, ListFilterUpdateRequest payload, map<string|string[]> headers = {}, boolean enrollObjectsInWorkflows = false, PutListIdUpdateListFiltersUpdateListFiltersQueries queries) returns ListUpdateResponse|error;
 
     # Search Lists
     # 
@@ -1792,7 +1793,7 @@
 
     # Fetch List by Name
     # 
-    remote function getObjectTypeIdObjectTypeIdNameListNameGetByName(string listName, string objectTypeId, map<string|string[]> headers = {}, boolean includeFilters = false, anydata Additional Values, GetObjectTypeIdObjectTypeIdNameListNameGetByNameQueries queries) returns ListFetchResponse|error;
+    remote function getObjectTypeIdObjectTypeIdNameListNameGetByName(string listName, string objectTypeId, map<string|string[]> headers = {}, boolean includeFilters = false, GetObjectTypeIdObjectTypeIdNameListNameGetByNameQueries queries) returns ListFetchResponse|error;
 
     # Moves a folder
     # 
@@ -1800,7 +1801,7 @@
 
     # Translate legacy list ID to modern ID
     # 
-    remote function getIdmappingTranslateLegacyListIdToListId(map<string|string[]> headers = {}, string legacyListId = "", anydata Additional Values, GetIdmappingTranslateLegacyListIdToListIdQueries queries) returns PublicMigrationMapping|error;
+    remote function getIdmappingTranslateLegacyListIdToListId(map<string|string[]> headers = {}, string legacyListId = "", GetIdmappingTranslateLegacyListIdToListIdQueries queries) returns PublicMigrationMapping|error;
 
     # Batch translate legacy list IDs
     # 
@@ -1812,11 +1813,11 @@
 
     # Rename a folder
     # 
-    remote function putFoldersFolderIdRenameRename(string folderId, map<string|string[]> headers = {}, string newFolderName = "", anydata Additional Values, PutFoldersFolderIdRenameRenameQueries queries) returns ListFolderFetchResponse|error;
+    remote function putFoldersFolderIdRenameRename(string folderId, map<string|string[]> headers = {}, string newFolderName = "", PutFoldersFolderIdRenameRenameQueries queries) returns ListFolderFetchResponse|error;
 
     # Get memberships by join date
     # 
-    remote function getListIdMembershipsJoinOrderGetPageOrderedByAddedToListDate(string listId, map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, GetListIdMembershipsJoinOrderGetPageOrderedByAddedToListDateQueries queries) returns ApiCollectionResponseJoinTimeAndRecordId|error;
+    remote function getListIdMembershipsJoinOrderGetPageOrderedByAddedToListDate(string listId, map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", GetListIdMembershipsJoinOrderGetPageOrderedByAddedToListDateQueries queries) returns ApiCollectionResponseJoinTimeAndRecordId|error;
 
     # Add all records from source list
     # 
@@ -1828,7 +1829,7 @@
 
     # Fetch Multiple Lists
     # 
-    remote function getGetAll(map<string|string[]> headers = {}, string[] listIds = [], boolean includeFilters = false, anydata Additional Values, GetGetAllQueries queries) returns ListsByIdResponse|error;
+    remote function getGetAll(map<string|string[]> headers = {}, string[] listIds = [], boolean includeFilters = false, GetGetAllQueries queries) returns ListsByIdResponse|error;
 
     # Create List
     # 
@@ -1836,7 +1837,7 @@
 
     # Retrieves a folder
     # 
-    remote function getFoldersGetAll(map<string|string[]> headers = {}, string folderId = "", anydata Additional Values, GetFoldersGetAllQueries queries) returns ListFolderFetchResponse|error;
+    remote function getFoldersGetAll(map<string|string[]> headers = {}, string folderId = "", GetFoldersGetAllQueries queries) returns ListFolderFetchResponse|error;
 
     # Creates a folder
     # 
@@ -1848,7 +1849,7 @@
 
     # Fetch List Memberships Ordered by ID
     # 
-    remote function getListIdMembershipsGetPage(string listId, map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", anydata Additional Values, GetListIdMembershipsGetPageQueries queries) returns ApiCollectionResponseJoinTimeAndRecordId|error;
+    remote function getListIdMembershipsGetPage(string listId, map<string|string[]> headers = {}, string before = "", int:Signed32 limit = 0, string after = "", GetListIdMembershipsGetPageQueries queries) returns ApiCollectionResponseJoinTimeAndRecordId|error;
 
     # Delete All Records from a List
     # 
`````

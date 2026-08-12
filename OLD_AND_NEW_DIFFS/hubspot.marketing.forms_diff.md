# hubspot.marketing.forms — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.marketing.forms` |
| **Old file** | `hubspot.marketing.forms/old/ballerinax_hubspot.marketing.forms.bal.txt` |
| **New file** | `hubspot.marketing.forms/new/ballerinax_hubspot.marketing.forms.bal.txt` |
| **Old lines** | 1043 |
| **New lines** | 1044 |
| **Lines added** | 11 |
| **Lines removed** | 10 |
| **Hunks** | 9 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 20 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 392–399 | 392–399 | Types | +2 | −2 |
| 2 | 503–510 | 503–510 | Types | +2 | −2 |
| 3 | 558–564 | 558–564 | Types | +1 | −1 |
| 4 | 714–720 | 714–720 | Types | +1 | −1 |
| 5 | 786–792 | 786–792 | Types | +1 | −1 |
| 6 | 890–896 | 890–896 | Types | +1 | −1 |
| 7 | 928–933 | 928–934 | Types | +1 | −0 |
| 8 | 1019–1025 | 1020–1026 | Client | +1 | −1 |
| 9 | 1035–1041 | 1036–1042 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- hubspot.marketing.forms/old/ballerinax_hubspot.marketing.forms.bal.txt	2026-08-12 12:57:30
+++ hubspot.marketing.forms/new/ballerinax_hubspot.marketing.forms.bal.txt	2026-08-12 13:19:19
@@ -392,8 +392,8 @@
 # Describes how a phone number should be validated
 
 type PhoneFieldValidation record {
-    ballerina/lang.int:0.0.0:Signed32 minAllowedDigits;
-    ballerina/lang.int:0.0.0:Signed32 maxAllowedDigits;
+    int:Signed32 minAllowedDigits;
+    int:Signed32 maxAllowedDigits;
 };
 
 # A form field used for collecting a mobile phone number
@@ -503,8 +503,8 @@
 # Describes how a numeric value should be validated
 
 type NumberFieldValidation record {
-    ballerina/lang.int:0.0.0:Signed32 minAllowedDigits;
-    ballerina/lang.int:0.0.0:Signed32 maxAllowedDigits;
+    int:Signed32 minAllowedDigits;
+    int:Signed32 maxAllowedDigits;
 };
 
 # A form field consisting of a single checkbox
@@ -558,7 +558,7 @@
 
 type EnumeratedFieldOption record {
     # The order the choices will be displayed in
-    ballerina/lang.int:0.0.0:Signed32 displayOrder;
+    int:Signed32 displayOrder;
     string description?;
     # The visible label for this choice
     string label;
@@ -714,7 +714,7 @@
     FieldGroupFields[] fields;
 };
 
-type FieldGroupFields ballerinax/hubspot.marketing.forms:1.0.2:EmailField|ballerinax/hubspot.marketing.forms:1.0.2:PhoneField|ballerinax/hubspot.marketing.forms:1.0.2:MobilePhoneField|ballerinax/hubspot.marketing.forms:1.0.2:SingleLineTextField|ballerinax/hubspot.marketing.forms:1.0.2:MultiLineTextField|ballerinax/hubspot.marketing.forms:1.0.2:NumberField|ballerinax/hubspot.marketing.forms:1.0.2:SingleCheckboxField|ballerinax/hubspot.marketing.forms:1.0.2:MultipleCheckboxesField|ballerinax/hubspot.marketing.forms:1.0.2:DropdownField|ballerinax/hubspot.marketing.forms:1.0.2:RadioField|ballerinax/hubspot.marketing.forms:1.0.2:DatepickerField|ballerinax/hubspot.marketing.forms:1.0.2:FileField|ballerinax/hubspot.marketing.forms:1.0.2:PaymentLinkRadioField;
+type FieldGroupFields EmailField|PhoneField|MobilePhoneField|SingleLineTextField|MultiLineTextField|NumberField|SingleCheckboxField|MultipleCheckboxesField|DropdownField|RadioField|DatepickerField|FileField|PaymentLinkRadioField;
 
 
 type HubSpotFormConfiguration record {
@@ -786,7 +786,7 @@
 
 
 type LegalConsentCheckbox record {
-    ballerina/lang.int:0.0.0:Signed32 subscriptionTypeId;
+    int:Signed32 subscriptionTypeId;
     # The main label for the form field
     string label;
     # Whether this checkbox is required when submitting the form
@@ -890,7 +890,7 @@
     # Whether to return only results that have been archived
     boolean archived?;
     # The maximum number of results to display per page
-    ballerina/lang.int:0.0.0:Signed32 'limit?;
+    int:Signed32 'limit?;
     # The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results
     string after?;
 };
@@ -928,6 +928,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Provides Auth configurations needed when communicating with a remote HTTP endpoint.
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -1019,7 +1020,7 @@
 
     # Get a form definition
     # 
-    resource function get [string formId](map<string|string[]> headers = {}, boolean archived = false, anydata Additional Values, GetMarketingV3FormsFormIdGetByIdQueries queries) returns FormDefinitionBase|error;
+    resource function get [string formId](map<string|string[]> headers = {}, boolean archived = false, GetMarketingV3FormsFormIdGetByIdQueries queries) returns FormDefinitionBase|error;
 
     # Update a form definition
     # 
@@ -1035,7 +1036,7 @@
 
     # Get a list of forms
     # 
-    resource function get (map<string|string[]> headers = {}, ("hubspot"|"captured"|"flow"|"blog_comment"|"all")[] formTypes = [], boolean archived = false, int:Signed32 limit = 0, string after = "", anydata Additional Values, GetMarketingV3FormsGetPageQueries queries) returns CollectionResponseFormDefinitionBaseForwardPaging|error;
+    resource function get (map<string|string[]> headers = {}, ("hubspot"|"captured"|"flow"|"blog_comment"|"all")[] formTypes = [], boolean archived = false, int:Signed32 limit = 0, string after = "", GetMarketingV3FormsGetPageQueries queries) returns CollectionResponseFormDefinitionBaseForwardPaging|error;
 
     # Create a form
     # 
`````

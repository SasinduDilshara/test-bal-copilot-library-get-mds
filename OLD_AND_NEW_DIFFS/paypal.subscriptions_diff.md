# paypal.subscriptions — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `paypal.subscriptions` |
| **Old file** | `paypal.subscriptions/old/ballerinax_paypal.subscriptions.bal.txt` |
| **New file** | `paypal.subscriptions/new/ballerinax_paypal.subscriptions.bal.txt` |
| **Old lines** | 1154 |
| **New lines** | 1272 |
| **Lines added** | 133 |
| **Lines removed** | 15 |
| **Hunks** | 48 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 11 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (11)

- `type AccountId`
- `type CountryCode`
- `type CurrencyCode`
- `type DateNoTime`
- `type DateTime`
- `type DateYearMonth`
- `type Email`
- `type EmailAddress`
- `type Language`
- `type PatchRequest`
- `type Percentage`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 158–178 | 158–184 | Types | +8 | −2 |
| 2 | 180–190 | 186–199 | Types | +4 | −1 |
| 3 | 192–215 | 201–230 | Types | +7 | −1 |
| 4 | 235–274 | 250–305 | Types | +17 | −1 |
| 5 | 276–293 | 307–331 | Types | +7 | −0 |
| 6 | 296–301 | 334–340 | Types | +1 | −0 |
| 7 | 310–315 | 349–355 | Types | +1 | −0 |
| 8 | 317–324 | 357–366 | Types | +2 | −0 |
| 9 | 327–332 | 369–375 | Types | +1 | −0 |
| 10 | 334–339 | 377–383 | Types | +1 | −0 |
| 11 | 341–354 | 385–402 | Types | +5 | −1 |
| 12 | 359–365 | 407–415 | Types | +3 | −1 |
| 13 | 397–402 | 447–453 | Types | +1 | −0 |
| 14 | 412–421 | 463–475 | Types | +3 | −0 |
| 15 | 424–433 | 478–490 | Types | +4 | −1 |
| 16 | 435–440 | 492–498 | Types | +1 | −0 |
| 17 | 457–463 | 515–523 | Types | +3 | −1 |
| 18 | 468–473 | 528–534 | Types | +1 | −0 |
| 19 | 478–489 | 539–554 | Types | +4 | −0 |
| 20 | 528–537 | 593–605 | Types | +3 | −0 |
| 21 | 556–562 | 624–632 | Types | +3 | −1 |
| 22 | 564–569 | 634–640 | Types | +1 | −0 |
| 23 | 601–606 | 672–678 | Types | +1 | −0 |
| 24 | 629–634 | 701–707 | Types | +1 | −0 |
| 25 | 642–648 | 715–721 | Types | +1 | −1 |
| 26 | 671–685 | 744–761 | Types | +3 | −0 |
| 27 | 722–727 | 798–804 | Types | +1 | −0 |
| 28 | 731–742 | 808–822 | Types | +3 | −0 |
| 29 | 749–754 | 829–835 | Types | +1 | −0 |
| 30 | 763–770 | 844–853 | Types | +2 | −0 |
| 31 | 776–791 | 859–879 | Types | +5 | −0 |
| 32 | 827–844 | 915–938 | Types | +6 | −0 |
| 33 | 848–857 | 942–953 | Types | +2 | −0 |
| 34 | 862–867 | 958–964 | Types | +1 | −0 |
| 35 | 901–906 | 998–1004 | Types | +1 | −0 |
| 36 | 908–918 | 1006–1018 | Types | +2 | −0 |
| 37 | 959–964 | 1059–1065 | Types | +1 | −0 |
| 38 | 975–981 | 1076–1083 | Types | +2 | −1 |
| 39 | 990–995 | 1092–1098 | Types | +1 | −0 |
| 40 | 1000–1011 | 1103–1118 | Types | +4 | −0 |
| 41 | 1017–1024 | 1124–1133 | Types | +2 | −0 |
| 42 | 1026–1031 | 1135–1141 | Types | +1 | −0 |
| 43 | 1040–1053 | 1150–1166 | Types | +3 | −0 |
| 44 | 1062–1067 | 1175–1181 | Types | +1 | −0 |
| 45 | 1073–1084 | 1187–1202 | Types | +4 | −0 |
| 46 | 1090–1096 | 1208–1214 | Client | +1 | −1 |
| 47 | 1122–1128 | 1240–1246 | Client | +1 | −1 |
| 48 | 1150–1154 | 1268–1272 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- paypal.subscriptions/old/ballerinax_paypal.subscriptions.bal.txt	2026-08-12 12:57:30
+++ paypal.subscriptions/new/ballerinax_paypal.subscriptions.bal.txt	2026-08-12 13:19:19
@@ -158,21 +158,27 @@
     oauth2:ClientConfiguration clientConfig?; // Special Agent Note: ClientConfiguration FROM ballerina/oauth2 package
 };
 
-// Unknown type: Email
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254}
+type Email string;
 
-// Unknown type: AccountId
+# The account identifier for a PayPal account
+@constraint:String {maxLength: 13, minLength: 13, pattern: re `^[2-9A-HJ-NP-Z]{13}$`}
+type AccountId string;
 
 # The request to update the quantity of the product or service in a subscription. You can also use this method to switch the plan and update the `shipping_amount` and `shipping_address` values for the subscription. This type of update requires the buyer's consent
 
 type SubscriptionReviseRequest record {
     Money shipping_amount?;
     # The quantity of the product or service in the subscription
+    @constraint:String {maxLength: 32, minLength: 1, pattern: re `^([0-9]+|([0-9]+)?[.][0-9]+)$`}
     string quantity?;
     ApplicationContext application_context?;
     ShippingDetail shipping_address?;
     # An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object
     PlanOverride plan?;
     # The unique PayPal-generated ID for the plan
+    @constraint:String {maxLength: 50, minLength: 3}
     string plan_id?;
 };
 
@@ -180,11 +186,14 @@
 
 type Money record {
     # The value, which might be:<ul><li>An integer for currencies like `JPY` that are not typically fractional.</li><li>A decimal fraction for currencies like `TND` that are subdivided into thousandths.</li></ul>For the required number of decimal places for a currency code, see [Currency Codes](/docs/integration/direct/rest/currency-codes/)
+    @constraint:String {maxLength: 32, pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
     string value;
     CurrencyCode currency_code;
 };
 
-// Unknown type: CurrencyCode
+# The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency
+@constraint:String {maxLength: 3, minLength: 3}
+type CurrencyCode string;
 
 # The application context, which customizes the payer experience during the subscription approval process with PayPal
 
@@ -192,24 +201,30 @@
     # Configures the label name to `Continue` or `Subscribe Now` for subscription consent experience
     "CONTINUE"|"SUBSCRIBE_NOW" user_action?;
     # The URL where the customer is redirected after the customer approves the payment
+    @constraint:String {maxLength: 4000, minLength: 10}
     string return_url;
     # The label that overrides the business name in the PayPal account on the PayPal site
+    @constraint:String {maxLength: 127, minLength: 1}
     string brand_name?;
     # The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/docs/integration/direct/rest/country-codes/)
     Language locale?;
     # The URL where the customer is redirected after the customer cancels the payment
+    @constraint:String {maxLength: 4000, minLength: 10}
     string cancel_url;
     # The location from which the shipping address is derived
     "GET_FROM_FILE"|"NO_SHIPPING"|"SET_PROVIDED_ADDRESS" shipping_preference?;
     PaymentMethod payment_method?;
 };
 
-// Unknown type: Language
+# The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/docs/integration/direct/rest/country-codes/)
+@constraint:String {maxLength: 10, minLength: 2, pattern: re `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}))?$`}
+type Language string;
 
 # The customer and merchant payment preferences
 
 type PaymentMethod record {
     # The customer-selected payment method on the merchant site
+    @constraint:String {minLength: 1, pattern: re `^[0-9A-Z_]+$`}
     string payer_selected?;
     PayeePaymentMethodPreference payee_preferred?;
     # NACHA (the regulatory body governing the ACH network) requires that API callers (merchants, partners) obtain the consumer’s explicit authorization before initiating a transaction. To stay compliant, you’ll need to make sure that you retain a compliant authorization for each transaction that you originate to the ACH Network using this API. ACH transactions are categorized (using SEC codes) by how you capture authorization from the Receiver (the person whose bank account is being debited or credited). PayPal supports the following SEC codes
@@ -235,40 +250,56 @@
 type AddressPortable record {
     CountryCode country_code;
     # The highest level sub-division in a country, which is usually a province, state, or ISO-3166-2 subdivision. Format for postal delivery. For example, `CA` and not `California`. Value, by country, is:<ul><li>UK. A county.</li><li>US. A state.</li><li>Canada. A province.</li><li>Japan. A prefecture.</li><li>Switzerland. A kanton.</li></ul>
+    @constraint:String {maxLength: 300}
     string admin_area_1?;
     # The first line of the address. For example, number or street. For example, `173 Drury Lane`. Required for data entry and compliance and risk checks. Must contain the full address
+    @constraint:String {maxLength: 300}
     string address_line_1?;
     # A sub-locality, suburb, neighborhood, or district. Smaller than `admin_area_level_2`. Value is:<ul><li>Brazil. Suburb, bairro, or neighborhood.</li><li>India. Sub-locality or district. Street name information is not always available but a sub-locality or district can be a very small area.</li></ul>
+    @constraint:String {maxLength: 100}
     string admin_area_3?;
     AddressDetails address_details?;
     # A city, town, or village. Smaller than `admin_area_level_1`
+    @constraint:String {maxLength: 120}
     string admin_area_2?;
     # The third line of the address, if needed. For example, a street complement for Brazil, direction text, such as `next to Walmart`, or a landmark in an Indian address
+    @constraint:String {maxLength: 100}
     string address_line_3?;
     # The second line of the address. For example, suite or apartment number
+    @constraint:String {maxLength: 300}
     string address_line_2?;
     # The neighborhood, ward, or district. Smaller than `admin_area_level_3` or `sub_locality`. Value is:<ul><li>The postal sorting code for Guernsey and many French territories, such as French Guiana.</li><li>The fine-grained administrative levels in China.</li></ul>
+    @constraint:String {maxLength: 100}
     string admin_area_4?;
     # The postal code, which is the zip code or equivalent. Typically required for countries with a postal code or an equivalent. See [postal code](https://en.wikipedia.org/wiki/Postal_code)
+    @constraint:String {maxLength: 60}
     string postal_code?;
 };
 
-// Unknown type: CountryCode
+# The [two-character ISO 3166-1 code](/docs/integration/direct/rest/country-codes/) that identifies the country or region.<blockquote><strong>Note:</strong> The country code for Great Britain is <code>GB</code> and not <code>UK</code> as used in the top-level domain names for that country. Use the `C2` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.</blockquote>
+@constraint:String {maxLength: 2, minLength: 2, pattern: re `^([A-Z]{2}|C2)$`}
+type CountryCode string;
 
 # The non-portable additional address details that are sometimes needed for compliance, risk, or other scenarios where fine-grain address information might be needed. Not portable with common third party and open source. Redundant with core fields.<br/>For example, `address_portable.address_line_1` is usually a combination of `address_details.street_number`, `street_name`, and `street_type`
 
 type AddressDetails record {
     # A named locations that represents the premise. Usually a building name or number or collection of buildings with a common name or number. For example, <code>Craven House</code>
+    @constraint:String {maxLength: 100}
     string building_name?;
     # The street number
+    @constraint:String {maxLength: 100}
     string street_number?;
     # The street type. For example, avenue, boulevard, road, or expressway
+    @constraint:String {maxLength: 100}
     string street_type?;
     # The first-order entity below a named building or location that represents the sub-premises. Usually a single building within a collection of buildings with a common name. Can be a flat, story, floor, room, or apartment
+    @constraint:String {maxLength: 100}
     string sub_building?;
     # The delivery service. Post office box, bag number, or post office name
+    @constraint:String {maxLength: 100}
     string delivery_service?;
     # The street name. Just `Drury` in `Drury Lane`
+    @constraint:String {maxLength: 100}
     string street_name?;
 };
 
@@ -276,18 +307,25 @@
 
 type Name record {
     # When the party is a person, the party's full name
+    @constraint:String {maxLength: 300}
     string full_name?;
     # The prefix, or title, to the party's name
+    @constraint:String {maxLength: 140}
     string prefix?;
     # When the party is a person, the party's surname or family name. Also known as the last name. Required when the party is a person. Use also to store multiple surnames including the matronymic, or mother's, surname
+    @constraint:String {maxLength: 140}
     string surname?;
     # When the party is a person, the party's given, or first, name
+    @constraint:String {maxLength: 140}
     string given_name?;
     # When the party is a person, the party's middle name. Use also to store multiple middle names including the patronymic, or father's, middle name
+    @constraint:String {maxLength: 140}
     string middle_name?;
     # The suffix for the party's name
+    @constraint:String {maxLength: 140}
     string suffix?;
     # DEPRECATED. The party's alternate name. Can be a business name, nickname, or any other name that cannot be split into first, last name. Required when the party is a business
+    @constraint:String {maxLength: 300}
     string alternate_full_name?;
 };
 
@@ -296,6 +334,7 @@
 type PlanOverride record {
     PaymentPreferencesOverride payment_preferences?;
     # An array of billing cycles for trial billing and regular billing. The subscription billing cycle definition has to adhere to the plan billing cycle definition
+    @constraint:Array {maxLength: 12, minLength: 1}
     BillingCycleOverride[] billing_cycles?;
     # The tax details
     TaxesOverride taxes?;
@@ -310,6 +349,7 @@
     # Indicates whether to automatically bill the outstanding amount in the next billing cycle
     boolean auto_bill_outstanding?;
     # The maximum number of payment failures before a subscription is suspended. For example, if `payment_failure_threshold` is `2`, the subscription automatically updates to the `SUSPEND` state if two consecutive payments fail
+    @constraint:Int {minValue: 0, maxValue: 999}
     int payment_failure_threshold?;
 };
 
@@ -317,8 +357,10 @@
 
 type BillingCycleOverride record {
     # The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a `sequence` of `1` while a regular billing cycle has a `sequence` of `2`, so that trial cycle runs before the regular cycle
+    @constraint:Int {minValue: 1, maxValue: 99}
     int sequence;
     # The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>). Regular billing cycles can be executed infinite times (value of <code>0</code> for <code>total_cycles</code>) or a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>)
+    @constraint:Int {minValue: 0, maxValue: 999}
     int total_cycles?;
     PricingScheme pricing_scheme?;
 };
@@ -327,6 +369,7 @@
 
 type PricingScheme record {
     # An array of pricing tiers which are used for billing volume/tiered plans. pricing_model field has to be specified
+    @constraint:Array {maxLength: 32, minLength: 1}
     PricingTier[] tiers?;
     DateTime update_time?;
     DateTime create_time?;
@@ -334,6 +377,7 @@
     "VOLUME"|"TIERED" pricing_model?;
     Money fixed_price?;
     # The version of the pricing scheme
+    @constraint:Int {minValue: 0, maxValue: 999}
     int version?;
 };
 
@@ -341,14 +385,18 @@
 
 type PricingTier record {
     # The starting quantity for the tier
+    @constraint:String {maxLength: 32, minLength: 1, pattern: re `^([0-9]+|([0-9]+)?[.][0-9]+)$`}
     string starting_quantity;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount;
     # The ending quantity for the tier. Optional for the last tier
+    @constraint:String {maxLength: 32, minLength: 1, pattern: re `^([0-9]+|([0-9]+)?[.][0-9]+)$`}
     string ending_quantity?;
 };
 
-// Unknown type: DateTime
+# The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
+@constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
+type DateTime string;
 
 # The tax details
 
@@ -359,7 +407,9 @@
     Percentage percentage?;
 };
 
-// Unknown type: Percentage
+# The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`
+@constraint:String {pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
+type Percentage string;
 
 
 type SubscriptionReviseResponseAllOf2 record {
@@ -397,6 +447,7 @@
 
 type UpdatePricingSchemeRequest record {
     # The billing cycle sequence
+    @constraint:Int {minValue: 1, maxValue: 99}
     int billing_cycle_sequence;
     PricingScheme pricing_scheme;
 };
@@ -412,10 +463,13 @@
 
 type Card record {
     # The primary account number (PAN) for the payment card
+    @constraint:String {maxLength: 19, minLength: 13}
     string number;
     # The three- or four-digit security code of the card. Also known as the CVV, CVC, CVN, CVE, or CID. This parameter cannot be present in the request when `payment_initiator=MERCHANT`
+    @constraint:String {pattern: re `[0-9]{3,4}`}
     string security_code?;
     # The card holder's name as it appears on the card
+    @constraint:String {maxLength: 300}
     string name?;
     AddressPortable billing_address?;
     # The PayPal-generated ID for the card
@@ -424,10 +478,13 @@
     DateYearMonth expiry;
     CardBrand card_type?;
     # The last digits of the payment card
+    @constraint:String {pattern: re `[0-9]{2,}`}
     string last_digits?;
 };
 
-// Unknown type: DateYearMonth
+# The year and month, in ISO-8601 `YYYY-MM` date format. See [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6)
+@constraint:String {maxLength: 7, minLength: 7, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])$`}
+type DateYearMonth string;
 
 # The card network or brand. Applies to credit, debit, gift, and payment cards
 type CardBrand "VISA"|"MASTERCARD"|"DISCOVER"|"AMEX"|"SOLO"|"JCB"|"STAR"|"DELTA"|"SWITCH"|"MAESTRO"|"CB_NATIONALE"|"CONFIGOGA"|"CONFIDIS"|"ELECTRON"|"CETELEM"|"CHINA_UNION_PAY";
@@ -435,6 +492,7 @@
 
 type TransactionAllOf2 record {
     # The PayPal-generated transaction ID.
+    @constraint:String {maxLength: 50, minLength: 3}
     string id?;
     # The breakdown details for the amount. Includes the gross, tax, fee, and shipping amounts
     AmountWithBreakdown amount_with_breakdown?;
@@ -457,7 +515,9 @@
     Money net_amount?;
 };
 
-// Unknown type: EmailAddress
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254, minLength: 3, pattern: re `^.+@[^"\-].+$`}
+type EmailAddress string;
 
 # The payment preferences for a subscription
 
@@ -468,6 +528,7 @@
     # Indicates whether to automatically bill the outstanding amount in the next billing cycle
     boolean auto_bill_outstanding?;
     # The maximum number of payment failures before a subscription is suspended. For example, if `payment_failure_threshold` is `2`, the subscription automatically updates to the `SUSPEND` state if two consecutive payments fail
+    @constraint:Int {minValue: 0, maxValue: 999}
     int payment_failure_threshold?;
 };
 
@@ -478,12 +539,16 @@
 
 type TransactionsList record {
     # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links)
+    @constraint:Array {maxLength: 10, minLength: 1}
     LinkDescription[] links?;
     # The total number of pages
+    @constraint:Int {minValue: 0, maxValue: 100000000}
     int total_pages?;
     # An array of transactions
+    @constraint:Array {maxLength: 32767}
     Transaction[] transactions?;
     # The total number of items
+    @constraint:Int {minValue: 0, maxValue: 500000000}
     int total_items?;
 };
 
@@ -528,10 +593,13 @@
 
 type Phone record {
     # The country calling code (CC), in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). The combined length of the CC and the national number must not be greater than 15 digits. The national number consists of a national destination code (NDC) and subscriber number (SN)
+    @constraint:String {maxLength: 3, minLength: 1, pattern: re `^[0-9]{1,3}?$`}
     string country_code;
     # The extension number
+    @constraint:String {maxLength: 15, minLength: 1, pattern: re `^[0-9]{1,15}?$`}
     string extension_number?;
     # The national number, in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). The combined length of the country calling code (CC) and the national number must not be greater than 15 digits. The national number consists of a national destination code (NDC) and subscriber number (SN)
+    @constraint:String {maxLength: 14, minLength: 1, pattern: re `^[0-9]{1,14}?$`}
     string national_number;
 };
 
@@ -556,7 +624,9 @@
     AddressPortable address?;
 };
 
-// Unknown type: DateNoTime
+# The stand-alone date, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). To represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone data. Whenever possible, use the standard `date_time` type. This regular expression does not validate all dates. For example, February 31 is valid and nothing is known about leap years
+@constraint:String {maxLength: 10, minLength: 10, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$`}
+type DateNoTime string;
 
 # The tax ID of the customer. The customer is also known as the payer. Both `tax_id` and `tax_id_type` are required
 
@@ -564,6 +634,7 @@
     # The customer's tax ID type
     "BR_CPF"|"BR_CNPJ" tax_id_type;
     # The customer's tax ID value
+    @constraint:String {maxLength: 14}
     string tax_id;
 };
 
@@ -601,6 +672,7 @@
     # The payment card type
     "CREDIT"|"DEBIT"|"PREPAID"|"UNKNOWN" 'type?;
     # The last digits of the payment card
+    @constraint:String {pattern: re `[0-9]{2,}`}
     string last_digits?;
     # The card network or brand. Applies to credit, debit, gift, and payment cards
     CardBrand brand?;
@@ -629,6 +701,7 @@
 
 type CardResponseWithBillingAddressAllOf2 record {
     # The card holder's name as it appears on the card.
+    @constraint:String {maxLength: 300, minLength: 2}
     string name?;
     # The portable international postal address. Maps to [AddressValidationMetadata](https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling form controls: the autocomplete attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute)
     AddressPortable billing_address?;
@@ -642,7 +715,7 @@
 
 type CardResponseWithBillingAddress record {
     AuthenticationResponse authentication_result?;
-    "CREDIT"|"DEBIT"|"PREPAID"|"UNKNOWN" type?;
+    "CREDIT"|"DEBIT"|"PREPAID"|"UNKNOWN" 'type?;
     string last_digits?;
     CardBrand brand?;
     string name?;
@@ -671,15 +744,18 @@
     Money shipping_amount?;
     DateTime start_time?;
     # The quantity of the product in the subscription
+    @constraint:String {maxLength: 32, minLength: 1, pattern: re `^([0-9]+|([0-9]+)?[.][0-9]+)$`}
     string quantity?;
     # The subscriber request information
     SubscriberRequest subscriber?;
     # The custom id for the subscription. Can be invoice id
+    @constraint:String {maxLength: 127, minLength: 1}
     string custom_id?;
     ApplicationContext application_context?;
     # An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object
     PlanOverride plan?;
     # The ID of the plan
+    @constraint:String {maxLength: 50, minLength: 3}
     string plan_id;
     # DEPRECATED. Indicates whether the subscription auto-renews after the billing cycles complete
 
@@ -722,6 +798,7 @@
 
 type SubscriptionStatus record {
     # The reason or notes for the status of the subscription
+    @constraint:String {maxLength: 128, minLength: 1}
     string status_change_note?;
     # The status of the subscription
     "APPROVAL_PENDING"|"APPROVED"|"ACTIVE"|"SUSPENDED"|"CANCELLED"|"EXPIRED" status?;
@@ -731,12 +808,15 @@
 
 type SubscriptionAllOf2 record {
     # The PayPal-generated ID for the subscription.
+    @constraint:String {maxLength: 50, minLength: 3}
     string id?;
     # The ID of the plan.
+    @constraint:String {maxLength: 50, minLength: 3}
     string plan_id?;
     # The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
     DateTime start_time?;
     # The quantity of the product in the subscription.
+    @constraint:String {maxLength: 32, minLength: 1, pattern: re `^([0-9]+|([0-9]+)?[.][0-9]+)$`}
     string quantity?;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money shipping_amount?;
@@ -749,6 +829,7 @@
     # The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
     DateTime update_time?;
     # The custom id for the subscription. Can be invoice id.
+    @constraint:String {maxLength: 127, minLength: 1}
     string custom_id?;
     # Indicates whether the subscription has overridden any plan attributes.
     boolean plan_overridden?;
@@ -763,8 +844,10 @@
 type SubscriptionBillingInfo record {
     DateTime final_payment_time?;
     # The trial and regular billing executions
+    @constraint:Array {maxLength: 3}
     CycleExecution[] cycle_executions?;
     # The number of consecutive payment failures. Resets to `0` after a successful payment. If this reaches the `payment_failure_threshold` value, the subscription updates to the `SUSPENDED` state
+    @constraint:Int {minValue: 0, maxValue: 999}
     int failed_payments_count;
     DateTime next_billing_time?;
     FailedPaymentDetails last_failed_payment?;
@@ -776,16 +859,21 @@
 
 type CycleExecution record {
     # The order in which to run this cycle among other billing cycles
+    @constraint:Int {minValue: 0, maxValue: 99}
     int sequence;
     # For a finite billing cycle, cycles_remaining is the number of remaining cycles. For an infinite billing cycle, cycles_remaining is set as 0
+    @constraint:Int {minValue: 0, maxValue: 9999}
     int cycles_remaining?;
     # The type of the billing cycle
     "REGULAR"|"TRIAL" tenure_type;
     # The number of billing cycles that have completed
+    @constraint:Int {minValue: 0, maxValue: 9999}
     int cycles_completed;
     # The active pricing scheme version for the billing cycle
+    @constraint:Int {minValue: 1, maxValue: 99}
     int current_pricing_scheme_version?;
     # The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>). Regular billing cycles can be executed infinite times (value of <code>0</code> for <code>total_cycles</code>) or a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>)
+    @constraint:Int {minValue: 0, maxValue: 999}
     int total_cycles?;
 };
 
@@ -827,18 +915,24 @@
     DateTime create_time?;
     PaymentPreferences payment_preferences?;
     # The ID for the product
+    @constraint:String {maxLength: 50, minLength: 6}
     string product_id?;
     # The plan name
+    @constraint:String {maxLength: 127, minLength: 1}
     string name?;
     # An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle
+    @constraint:Array {maxLength: 12, minLength: 1}
     BillingCycle[] billing_cycles?;
     # The detailed description of the plan
+    @constraint:String {maxLength: 127, minLength: 1}
     string description?;
     # The tax details
     Taxes taxes?;
     # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links)
+    @constraint:Array {maxLength: 10, minLength: 1}
     LinkDescription[] links?;
     # The unique PayPal-generated ID for the plan
+    @constraint:String {maxLength: 50, minLength: 3}
     string id?;
     # The plan status
     "CREATED"|"INACTIVE"|"ACTIVE" status?;
@@ -848,10 +942,12 @@
 
 type BillingCycle record {
     # The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a `sequence` of `1` while a regular billing cycle has a `sequence` of `2`, so that trial cycle runs before the regular cycle
+    @constraint:Int {minValue: 1, maxValue: 99}
     int sequence;
     # The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are allowed per plan
     "REGULAR"|"TRIAL" tenure_type;
     # The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>). Regular billing cycles can be executed infinite times (value of <code>0</code> for <code>total_cycles</code>) or a finite number of times (value between <code>1</code> and <code>999</code> for <code>total_cycles</code>)
+    @constraint:Int {minValue: 0, maxValue: 999}
     int total_cycles?;
     PricingScheme pricing_scheme?;
     # The frequency of the billing cycle
@@ -862,6 +958,7 @@
 
 type Frequency record {
     # The number of intervals after which a subscriber is billed. For example, if the `interval_unit` is `DAY` with an `interval_count` of  `2`, the subscription is billed once every two days. The following table lists the maximum allowed values for the `interval_count` for each `interval_unit`:<table><thead><tr><th><code>Interval unit</code></th><th>Maximum interval count</th></tr></thead><tbody><tr><td><code>DAY</code></td><td align="right">365</td></tr><tr><td><code>WEEK</code></td><td align="right">52</td></tr><tr><td><code>MONTH</code></td><td align="right">12</td></tr><tr><td><code>YEAR</code></td><td align="right">1</td></tr></tbody></table>
+    @constraint:Int {minValue: 1, maxValue: 365}
     int interval_count?;
     # The interval at which the subscription is charged or billed
     "DAY"|"WEEK"|"MONTH"|"YEAR" interval_unit;
@@ -901,6 +998,7 @@
 
 type SubscriptionCancelRequest record {
     # The reason for the cancellation of a subscription
+    @constraint:String {maxLength: 128, minLength: 1}
     string reason;
 };
 
@@ -908,11 +1006,13 @@
 
 type SubscriptionsGetQueries record {
     # List of fields that are to be returned in the response. Possible value for fields are last_failed_payment and plan
+    @constraint:String {maxLength: 100, minLength: 1}
     string fields?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2ClientCredentialsGrantConfig auth;
@@ -959,6 +1059,7 @@
 
 type SubscriptionSuspendRequest record {
     # The reason for suspenson of the subscription
+    @constraint:String {maxLength: 128, minLength: 1}
     string reason;
 };
 
@@ -975,7 +1076,8 @@
     anydata value?;
 };
 
-// Unknown type: PatchRequest
+# An array of JSON patch objects to apply partial updates to resources
+type PatchRequest Patch[];
 
 # Represents the Headers record for the operation: subscriptions.create
 
@@ -990,6 +1092,7 @@
 
 type UpdatePricingSchemesListRequest record {
     # An array of pricing schemes
+    @constraint:Array {maxLength: 99, minLength: 1}
     UpdatePricingSchemeRequest[] pricing_schemes;
 };
 
@@ -1000,12 +1103,16 @@
     boolean quantity_supported?;
     PaymentPreferences payment_preferences;
     # The ID of the product created through Catalog Products API
+    @constraint:String {maxLength: 50, minLength: 6}
     string product_id;
     # The plan name
+    @constraint:String {maxLength: 127, minLength: 1}
     string name;
     # An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle
+    @constraint:Array {maxLength: 12, minLength: 1}
     BillingCycle[] billing_cycles;
     # The detailed description of the plan
+    @constraint:String {maxLength: 127, minLength: 1}
     string description?;
     # The tax details
     Taxes taxes?;
@@ -1017,8 +1124,10 @@
 
 type SubscriptionsTransactionsQueries record {
     # The start time of the range of transactions to list
+    @constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
     string start_time;
     # The end time of the range of transactions to list
+    @constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
     string end_time;
 };
 
@@ -1026,6 +1135,7 @@
 
 type SubscriptionActivateRequest record {
     # The reason for activation of a subscription. Required to reactivate the subscription
+    @constraint:String {maxLength: 128, minLength: 1}
     string reason?;
 };
 
@@ -1040,14 +1150,17 @@
 
 type PlansListQueries record {
     # Filters the response by a Product ID
+    @constraint:String {maxLength: 50, minLength: 6}
     string product_id?;
     # Filters the response by list of plan IDs. Filter supports upto 10 plan IDs
     string plan_ids?;
     # A non-zero integer which is the start index of the entire list of items to return in the response. The combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items
+    @constraint:Int {minValue: 1, maxValue: 100000}
     int page?;
     # Indicates whether to show the total count in the response
     boolean total_required?;
     # The number of items to return in the response
+    @constraint:Int {minValue: 1, maxValue: 20}
     int page_size?;
 };
 
@@ -1062,6 +1175,7 @@
 
 type SubscriptionCaptureRequest record {
     # The reason or note for the subscription charge
+    @constraint:String {maxLength: 128, minLength: 1}
     string note;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount;
@@ -1073,12 +1187,16 @@
 
 type PlanCollection record {
     # An array of plans
+    @constraint:Array {maxLength: 32767}
     Plan[] plans?;
     # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links)
+    @constraint:Array {maxLength: 10, minLength: 1}
     LinkDescription[] links?;
     # The total number of pages
+    @constraint:Int {minValue: 0, maxValue: 100000000}
     int total_pages?;
     # The total number of items
+    @constraint:Int {minValue: 0, maxValue: 500000000}
     int total_items?;
 };
 
@@ -1090,7 +1208,7 @@
 
     # List plans
     # 
-    resource function get plans(PlansListHeaders headers = {}, string product_id = "", string plan_ids = "", int page = 0, boolean total_required = false, int page_size = 0, anydata Additional Values, PlansListQueries queries) returns PlanCollection|error;
+    resource function get plans(PlansListHeaders headers = {}, string product_id = "", string plan_ids = "", int page = 0, boolean total_required = false, int page_size = 0, PlansListQueries queries) returns PlanCollection|error;
 
     # Create plan
     # 
@@ -1122,7 +1240,7 @@
 
     # Show subscription details
     # 
-    resource function get subscriptions/[string id](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, SubscriptionsGetQueries queries) returns Subscription|error;
+    resource function get subscriptions/[string id](map<string|string[]> headers = {}, string fields = "", SubscriptionsGetQueries queries) returns Subscription|error;
 
     # Update subscription
     # 
@@ -1150,5 +1268,5 @@
 
     # List transactions for subscription
     # 
-    resource function get subscriptions/[string id]/transactions(map<string|string[]> headers = {}, string start_time = "", string end_time = "", anydata Additional Values, SubscriptionsTransactionsQueries queries) returns TransactionsList|error;
+    resource function get subscriptions/[string id]/transactions(map<string|string[]> headers = {}, string start_time = "", string end_time = "", SubscriptionsTransactionsQueries queries) returns TransactionsList|error;
 }
`````

# paypal.invoices — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `paypal.invoices` |
| **Old file** | `paypal.invoices/old/ballerinax_paypal.invoices.bal.txt` |
| **New file** | `paypal.invoices/new/ballerinax_paypal.invoices.bal.txt` |
| **Old lines** | 1153 |
| **New lines** | 1251 |
| **Lines added** | 109 |
| **Lines removed** | 11 |
| **Hunks** | 36 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 7 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (7)

- `type CountryCode`
- `type CurrencyCode`
- `type DateNoTime`
- `type DateTime`
- `type EmailAddress`
- `type Language`
- `type Percentage`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 160–179 | 160–185 | Types | +7 | −1 |
| 2 | 182–199 | 188–211 | Types | +7 | −1 |
| 3 | 203–209 | 215–223 | Types | +3 | −1 |
| 4 | 327–349 | 341–368 | Types | +5 | −0 |
| 5 | 355–360 | 374–380 | Types | +1 | −0 |
| 6 | 376–381 | 396–402 | Types | +1 | −0 |
| 7 | 395–406 | 416–430 | Types | +4 | −1 |
| 8 | 408–413 | 432–438 | Types | +1 | −0 |
| 9 | 450–455 | 475–481 | Types | +1 | −0 |
| 10 | 468–473 | 494–500 | Types | +1 | −0 |
| 11 | 475–480 | 502–508 | Types | +1 | −0 |
| 12 | 482–487 | 510–516 | Types | +1 | −0 |
| 13 | 492–497 | 521–527 | Types | +1 | −0 |
| 14 | 507–524 | 537–561 | Types | +7 | −0 |
| 15 | 527–566 | 564–619 | Types | +17 | −1 |
| 16 | 592–612 | 645–671 | Types | +7 | −1 |
| 17 | 628–634 | 687–695 | Types | +3 | −1 |
| 18 | 647–652 | 708–714 | Types | +1 | −0 |
| 19 | 660–665 | 722–728 | Types | +1 | −0 |
| 20 | 671–682 | 734–749 | Types | +4 | −0 |
| 21 | 709–719 | 776–789 | Types | +3 | −0 |
| 22 | 721–726 | 791–797 | Types | +1 | −0 |
| 23 | 735–744 | 806–818 | Types | +3 | −0 |
| 24 | 766–771 | 840–846 | Types | +1 | −0 |
| 25 | 773–778 | 848–854 | Types | +1 | −0 |
| 26 | 825–834 | 901–913 | Types | +3 | −0 |
| 27 | 864–874 | 943–955 | Types | +2 | −0 |
| 28 | 915–926 | 996–1009 | Types | +2 | −0 |
| 29 | 964–977 | 1047–1063 | Types | +3 | −0 |
| 30 | 1009–1018 | 1095–1106 | Types | +2 | −0 |
| 31 | 1028–1043 | 1116–1136 | Types | +5 | −0 |
| 32 | 1045–1056 | 1138–1152 | Types | +3 | −0 |
| 33 | 1058–1067 | 1154–1165 | Types | +2 | −0 |
| 34 | 1073–1079 | 1171–1177 | Client | +1 | −1 |
| 35 | 1121–1127 | 1219–1225 | Client | +1 | −1 |
| 36 | 1129–1139 | 1227–1237 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- paypal.invoices/old/ballerinax_paypal.invoices.bal.txt	2026-08-12 12:57:30
+++ paypal.invoices/new/ballerinax_paypal.invoices.bal.txt	2026-08-12 13:19:19
@@ -160,20 +160,26 @@
 
 type Detail record {
     # The reference data. Includes a post office (PO) number.
+    @constraint:String {maxLength: 120}
     string reference?;
     # The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency
     CurrencyCode currency_code;
     # A note to the invoice recipient. Also appears on the invoice notification email.
+    @constraint:String {maxLength: 4000}
     string note?;
     # The general terms of the invoice. Can include return or cancellation policy and other terms and conditions.
+    @constraint:String {maxLength: 4000}
     string terms_and_conditions?;
     # A private bookkeeping memo for the user.
+    @constraint:String {maxLength: 500}
     string memo?;
     # An array of PayPal IDs for the files that are attached to an invoice.
     FileReference[] attachments?;
 };
 
-// Unknown type: CurrencyCode
+# The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency
+@constraint:String {maxLength: 3, minLength: 3}
+type CurrencyCode string;
 
 # The file reference. Can be a file in PayPal MediaServ, PayPal DMS, or other custom store
 
@@ -182,18 +188,24 @@
     string content_type?;
     DateTime create_time?;
     # The size of the file, in bytes
+    @constraint:String {pattern: re `^[0-9]+$`}
     string size?;
     # The reference URL for the file
+    @constraint:String {maxLength: 2000, minLength: 1}
     string reference_url?;
     # The ID of the referenced file
+    @constraint:String {maxLength: 255, minLength: 1}
     string id?;
 };
 
-// Unknown type: DateTime
+# The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
+@constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
+type DateTime string;
 
 
 type InvoiceDetailAllOf2 record {
     # The invoice number. Default is the number that is auto-incremented number from the last number.
+    @constraint:String {maxLength: 127}
     string invoice_number?;
     # The stand-alone date, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). To represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone data. Whenever possible, use the standard `date_time` type. This regular expression does not validate all dates. For example, February 31 is valid and nothing is known about leap years
     DateNoTime invoice_date?;
@@ -203,7 +215,9 @@
     Metadata metadata?;
 };
 
-// Unknown type: DateNoTime
+# The stand-alone date, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). To represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone data. Whenever possible, use the standard `date_time` type. This regular expression does not validate all dates. For example, February 31 is valid and nothing is known about leap years
+@constraint:String {maxLength: 10, minLength: 10, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$`}
+type DateNoTime string;
 
 # The payment term of the invoice. Payment can be due upon receipt, a specified date, or in a set number of days
 
@@ -327,23 +341,28 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money gratuity?;
     # The billing and shipping information. Includes name, email, address, phone and language
+    @constraint:Array {maxLength: 100}
     RecipientInfo[] primary_recipients?;
     # The invoicing refund details. Includes the refund type, date, amount, and method
     Refunds refunds?;
     Money due_amount?;
     # The parent ID to an invoice that defines the group invoice to which the invoice is related
+    @constraint:String {maxLength: 30}
     string parent_id?;
     # The invoicer business information that appears on the invoice
     InvoicerInfo invoicer?;
     # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links)
     LinkDescription[] links?;
     # The ID of the invoice
+    @constraint:String {maxLength: 30}
     string id?;
     # The details of the invoice. Includes invoice number, date, payment terms, and audit metadata
     InvoiceDetail detail;
     # An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>
+    @constraint:Array {maxLength: 100}
     EmailAddress[] additional_recipients?;
     # An array of invoice line item information
+    @constraint:Array {maxLength: 100}
     Item[] items?;
     # The status of the invoice
     InvoiceStatus status?;
@@ -355,6 +374,7 @@
     # The breakdown of the amount. Includes total item amount, total tax amount, custom amount, and shipping and discounts, if any
     AmountWithBreakdown breakdown?;
     # The value, which might be:<ul><li>An integer for currencies like `JPY` that are not typically fractional.</li><li>A decimal fraction for currencies like `TND` that are subdivided into thousandths.</li></ul>For the required number of decimal places for a currency code, see [Currency Codes](/docs/integration/direct/rest/currency-codes/)
+    @constraint:String {maxLength: 32, pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
     string value?;
     CurrencyCode currency_code?;
 };
@@ -376,6 +396,7 @@
 
 type Money record {
     # The value, which might be:<ul><li>An integer for currencies like `JPY` that are not typically fractional.</li><li>A decimal fraction for currencies like `TND` that are subdivided into thousandths.</li></ul>For the required number of decimal places for a currency code, see [Currency Codes](/docs/integration/direct/rest/currency-codes/)
+    @constraint:String {maxLength: 32, pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
     string value;
     CurrencyCode currency_code;
 };
@@ -395,12 +416,15 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # The name of the tax applied on the invoice items
+    @constraint:String {maxLength: 100}
     string name;
     # The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`
     Percentage percent;
 };
 
-// Unknown type: Percentage
+# The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`
+@constraint:String {pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
+type Percentage string;
 
 # The custom amount to apply to an invoice. If you include a label, you must include a custom amount
 
@@ -408,6 +432,7 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # The label to the custom amount of the invoice
+    @constraint:String {maxLength: 50}
     string label;
 };
 
@@ -450,6 +475,7 @@
 
 type ConfigurationAllOf2 record {
     # The template ID. The template determines the layout of the invoice. Includes which fields to show and hide.
+    @constraint:String {maxLength: 30}
     string template_id?;
 };
 
@@ -468,6 +494,7 @@
 type Payments record {
     Money paid_amount?;
     # An array of payment details for the invoice. The payment details of the invoice like payment type, method, date, discount and transaction type
+    @constraint:Array {maxLength: 100}
     PaymentDetail[] transactions?;
 };
 
@@ -475,6 +502,7 @@
 
 type PaymentDetail record {
     # A note associated with an external cash or check payment
+    @constraint:String {maxLength: 2000}
     string note?;
     ContactNameAddress shipping_info?;
     # The currency and amount for a financial transaction, such as a balance or payment due
@@ -482,6 +510,7 @@
     # The payment mode or method through which the invoicer can accept the payments
     PaymentMethod method;
     # The ID for a PayPal payment transaction. Required for the `PAYPAL` payment type
+    @constraint:String {maxLength: 22}
     string payment_id?;
     # The payment type. Can be PayPal or an external payment. Includes cash or a check
     PaymentType 'type?;
@@ -492,6 +521,7 @@
 
 type BusinessName record {
     # Required. The business name of the party
+    @constraint:String {maxLength: 300}
     string business_name?;
 };
 
@@ -507,18 +537,25 @@
 
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
 
@@ -527,40 +564,56 @@
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
     # The first-order entity below a named building or location that represents the sub-premise. Usually a single building within a collection of buildings with a common name. Can be a flat, story, floor, room, or apartment
+    @constraint:String {maxLength: 100}
     string sub_building?;
     # The delivery service. Post office box, bag number, or post office name
+    @constraint:String {maxLength: 100}
     string delivery_service?;
     # The street name. Just `Drury` in `Drury Lane`
+    @constraint:String {maxLength: 100}
     string street_name?;
 };
 
@@ -592,21 +645,27 @@
     # The invoice recipient's phone numbers. Extension number is not supported.
     PhoneDetail[] phones?;
     # Any additional information about the recipient.
+    @constraint:String {maxLength: 40}
     string additional_info?;
     # The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/docs/integration/direct/rest/country-codes/)
     Language language?;
 };
 
-// Unknown type: EmailAddress
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254, minLength: 3, pattern: re `^.+@[^"\-].+$`}
+type EmailAddress string;
 
 # The phone number, in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en)
 
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
 
@@ -628,7 +687,9 @@
     string national_number;
 };
 
-// Unknown type: Language
+# The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/docs/integration/direct/rest/country-codes/)
+@constraint:String {maxLength: 10, minLength: 2, pattern: re `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}))?$`}
+type Language string;
 
 # The billing information of the invoice recipient. Includes name, address, email, phone, and language
 
@@ -647,6 +708,7 @@
 type Refunds record {
     Money refund_amount?;
     # An array of refund details for the invoice. Includes the refund type, date, amount, and method
+    @constraint:Array {maxLength: 100}
     RefundDetail[] transactions?;
 };
 
@@ -660,6 +722,7 @@
     # The payment type. Can be PayPal or an external payment. Includes cash or a check
     PaymentType 'type?;
     # The ID for a PayPal payment transaction. Required for the `PAYPAL` payment type
+    @constraint:String {maxLength: 22}
     string refund_id?;
     DateNoTime refund_date?;
 };
@@ -671,12 +734,16 @@
     # An array of invoicer's phone numbers. The invoicer can choose to hide the phone number on the invoice.
     PhoneDetail[] phones?;
     # The invoicer's website.
+    @constraint:String {maxLength: 2048}
     string website?;
     # The invoicer's tax ID.
+    @constraint:String {maxLength: 100}
     string tax_id?;
     # Any additional information. Includes business hours.
+    @constraint:String {maxLength: 400}
     string additional_notes?;
     # The full URL to an external logo image. The logo image must not be larger than 250 pixels wide by 90 pixels high.
+    @constraint:String {maxLength: 2000}
     string logo_url?;
 };
 
@@ -709,11 +776,14 @@
 
 type Item record {
     # The quantity of the item that the invoicer provides to the payer. Value is from `-1000000` to `1000000`. Supports up to five decimal places
+    @constraint:String {maxLength: 14}
     string quantity;
     DateNoTime item_date?;
     # The item name for the invoice line item
+    @constraint:String {maxLength: 200}
     string name;
     # The item description for the invoice line item
+    @constraint:String {maxLength: 1000}
     string description?;
     # The discount as a percent or amount at invoice level. The invoice discount amount is subtracted from the item total
     Discount discount?;
@@ -721,6 +791,7 @@
     # The tax information. Includes the tax name and tax rate of invoice items. The tax amount is added to the item total
     Tax tax?;
     # The ID of the invoice line item
+    @constraint:String {maxLength: 22}
     string id?;
     Money unit_amount;
 };
@@ -735,10 +806,13 @@
 
 type QrConfig record {
     # The width, in pixels, of the QR code image. Value is from `150` to `500`
+    @constraint:Int {minValue: 150, maxValue: 500}
     int width?;
     # The type of URL for which to generate a QR code. Valid values are `pay` and `details`
+    @constraint:String {maxLength: 7}
     string action?;
     # The height, in pixels, of the QR code image. Value is from `150` to `500`
+    @constraint:Int {minValue: 150, maxValue: 500}
     int height?;
 };
 
@@ -766,6 +840,7 @@
     boolean standard_template?;
     TemplateInfo template_info?;
     # The template name.<blockquote><strong>Note:</strong> The template name must be unique.</blockquote>
+    @constraint:String {maxLength: 500, minLength: 1}
     string name?;
     UnitOfMeasure unit_of_measure?;
     # Indicates whether this template is the default template. A invoicer can have one default template
@@ -773,6 +848,7 @@
     # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links)
     LinkDescription[] links?;
     # The ID of the template
+    @constraint:String {maxLength: 30}
     string id?;
 };
 
@@ -825,10 +901,13 @@
     # The template-related details. Includes notes, terms and conditions, memo, and attachments
     TemplateDetail detail?;
     # The billing and shipping information. Includes name, email, address, phone, and language
+    @constraint:Array {maxLength: 100}
     RecipientInfo[] primary_recipients?;
     # An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>
+    @constraint:Array {maxLength: 100}
     EmailAddress[] additional_recipients?;
     # An array of invoice line-item information
+    @constraint:Array {maxLength: 100}
     Item[] items?;
 };
 
@@ -864,11 +943,13 @@
 
 type InvoiceNumber record {
     # The invoice number. If you omit this value, the default is the auto-incremented number from the last number
+    @constraint:String {maxLength: 25}
     string invoice_number?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2ClientCredentialsGrantConfig auth;
@@ -915,12 +996,14 @@
 
 type InvoicesListQueries record {
     # The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates
+    @constraint:Int {minValue: 1, maxValue: 1000}
     int page?;
     # The fields to return in the response. Value is `all` or `none`. To return only the template name, ID, and default attributes, specify `none`
     string fields?;
     # Indicates whether the to show <code>total_pages</code> and <code>total_items</code> in the response
     boolean total_required?;
     # The maximum number of templates to return in the response
+    @constraint:Int {minValue: 1, maxValue: 100}
     int page_size?;
 };
 
@@ -964,14 +1047,17 @@
 
 type Notification record {
     # A note to the payer
+    @constraint:String {maxLength: 4000}
     string note?;
     # Indicates whether to send a copy of the email to the recipient
     boolean send_to_recipient?;
     # The subject of the email that is sent as a notification to the recipient
+    @constraint:String {maxLength: 4000}
     string subject?;
     # Indicates whether to send a copy of the email to the merchant
     boolean send_to_invoicer?;
     # An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>
+    @constraint:Array {maxLength: 100}
     EmailAddress[] additional_recipients?;
 };
 
@@ -1009,10 +1095,12 @@
 
 type InvoicesSearchInvoicesQueries record {
     # The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates
+    @constraint:Int {minValue: 1, maxValue: 1000}
     int page?;
     # Indicates whether the to show <code>total_pages</code> and <code>total_items</code> in the response
     boolean total_required?;
     # The maximum number of templates to return in the response
+    @constraint:Int {minValue: 1, maxValue: 100}
     int page_size?;
 };
 
@@ -1028,16 +1116,21 @@
 type SearchData record {
     DateTimeRange payment_date_range?;
     # Filters the search by the recipient last name
+    @constraint:String {maxLength: 140}
     string recipient_last_name?;
     # Filters the search by the recipient first name
+    @constraint:String {maxLength: 140}
     string recipient_first_name?;
     # Filters the search by the email address
+    @constraint:String {maxLength: 254}
     string recipient_email?;
     DateRange invoice_date_range?;
     # A private bookkeeping memo for the user
+    @constraint:String {maxLength: 500}
     string memo?;
     CurrencyCode currency_code?;
     # The reference data, such as a PO number
+    @constraint:String {maxLength: 120}
     string reference?;
     AmountRange total_amount_range?;
     # Indicates whether to list merchant-archived invoices in the response. Value is:<ul><li><code>true</code>. Response lists only merchant-archived invoices.</li><li><code>false</code>. Response lists only unarchived invoices.</li><li><code>null</code>. Response lists all invoices.</li></ul>
@@ -1045,12 +1138,15 @@
     DateRange due_date_range?;
     DateTimeRange creation_date_range?;
     # Filters the search by the recipient business name
+    @constraint:String {maxLength: 300}
     string recipient_business_name?;
     # A CSV file of fields to return for the user, if available. Because the invoice object can be very large, field filtering is required. Valid collection fields are <code>items</code>, <code>payments</code>, <code>refunds</code>, <code>additional_recipients_info</code>, and <code>attachments</code>
     string[] fields?;
     # Filters the search by the invoice number
+    @constraint:String {maxLength: 25}
     string invoice_number?;
     # An array of status values
+    @constraint:Array {maxLength: 5}
     InvoiceStatus[] status?;
 };
 
@@ -1058,10 +1154,12 @@
 
 type TemplatesListQueries record {
     # The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates
+    @constraint:Int {minValue: 1, maxValue: 1000}
     int page?;
     # The fields to return in the response. Value is `all` or `none`. To return only the template name, ID, and default attributes, specify `none`
     string fields?;
     # The maximum number of templates to return in the response
+    @constraint:Int {minValue: 1, maxValue: 100}
     int page_size?;
 };
 
@@ -1073,7 +1171,7 @@
 
     # List invoices
     # 
-    resource function get invoices(map<string|string[]> headers = {}, int page = 0, string fields = "", boolean total_required = false, int page_size = 0, anydata Additional Values, InvoicesListQueries queries) returns Invoices|error;
+    resource function get invoices(map<string|string[]> headers = {}, int page = 0, string fields = "", boolean total_required = false, int page_size = 0, InvoicesListQueries queries) returns Invoices|error;
 
     # Create draft invoice
     # 
@@ -1121,7 +1219,7 @@
 
     # Fully update invoice
     # 
-    resource function put invoices/[string invoiceId](Invoice payload, InvoicesUpdateHeaders headers = {}, boolean send_to_recipient = false, boolean send_to_invoicer = false, anydata Additional Values, InvoicesUpdateQueries queries) returns Invoice|error;
+    resource function put invoices/[string invoiceId](Invoice payload, InvoicesUpdateHeaders headers = {}, boolean send_to_recipient = false, boolean send_to_invoicer = false, InvoicesUpdateQueries queries) returns Invoice|error;
 
     # Delete invoice
     # 
@@ -1129,11 +1227,11 @@
 
     # Search for invoices
     # 
-    resource function post search\-invoices(SearchData payload, map<string|string[]> headers = {}, int page = 0, boolean total_required = false, int page_size = 0, anydata Additional Values, InvoicesSearchInvoicesQueries queries) returns Invoices|error;
+    resource function post search\-invoices(SearchData payload, map<string|string[]> headers = {}, int page = 0, boolean total_required = false, int page_size = 0, InvoicesSearchInvoicesQueries queries) returns Invoices|error;
 
     # List templates
     # 
-    resource function get templates(map<string|string[]> headers = {}, int page = 0, string fields = "", int page_size = 0, anydata Additional Values, TemplatesListQueries queries) returns Templates|error;
+    resource function get templates(map<string|string[]> headers = {}, int page = 0, string fields = "", int page_size = 0, TemplatesListQueries queries) returns Templates|error;
 
     # Create template
     # 
`````

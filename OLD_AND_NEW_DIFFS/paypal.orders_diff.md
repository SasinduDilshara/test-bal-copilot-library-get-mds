# paypal.orders — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `paypal.orders` |
| **Old file** | `paypal.orders/old/ballerinax_paypal.orders.bal.txt` |
| **New file** | `paypal.orders/new/ballerinax_paypal.orders.bal.txt` |
| **Old lines** | 2219 |
| **New lines** | 2410 |
| **Lines added** | 228 |
| **Lines removed** | 37 |
| **Hunks** | 83 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 33 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (33)

- `type AccountId`
- `type AccountId2`
- `type AltpayRecurringAttributes`
- `type AltpayRecurringAttributesRequest`
- `type ApplePayAttributes`
- `type AuthenticationFlow`
- `type Bic`
- `type BillingAgreementId`
- `type BinDetailsProductsItemsString`
- `type CobrandedCardLabelsItemsString`
- `type CountryCode`
- `type CountryCode2`
- `type CurrencyCode`
- `type DateNoTime`
- `type DateTime`
- `type DateYearMonth`
- `type Email`
- `type EmailAddress`
- `type ExemptionDetails`
- `type FullName`
- `type GooglePayRequest`
- `type IbanLastChars`
- `type InstrumentId`
- `type IpAddress`
- `type Language`
- `type MerchantPartnerCustomerId`
- `type PatchRequest`
- `type StoreInVaultInstruction`
- `type TrackerStatus`
- `type UniversalProductCode`
- `type Url`
- `type VaultId`
- `type VaultOwnerId`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 142–148 | 142–150 | Types | +3 | −1 |
| 2 | 158–171 | 160–178 | Types | +6 | −1 |
| 3 | 179–194 | 186–209 | Types | +14 | −6 |
| 4 | 202–208 | 217–223 | Types | +1 | −1 |
| 5 | 223–229 | 238–244 | Types | +1 | −1 |
| 6 | 239–244 | 254–260 | Types | +1 | −0 |
| 7 | 247–262 | 263–284 | Types | +9 | −3 |
| 8 | 266–273 | 288–297 | Types | +2 | −0 |
| 9 | 292–303 | 316–331 | Types | +4 | −0 |
| 10 | 306–311 | 334–340 | Types | +1 | −0 |
| 11 | 368–377 | 397–409 | Types | +4 | −1 |
| 12 | 384–389 | 416–422 | Types | +1 | −0 |
| 13 | 400–405 | 433–439 | Types | +1 | −0 |
| 14 | 436–445 | 470–482 | Types | +3 | −0 |
| 15 | 494–501 | 531–540 | Types | +2 | −0 |
| 16 | 511–516 | 550–556 | Types | +1 | −0 |
| 17 | 519–524 | 559–565 | Types | +1 | −0 |
| 18 | 546–552 | 587–595 | Types | +3 | −1 |
| 19 | 572–578 | 615–623 | Types | +3 | −1 |
| 20 | 592–598 | 637–645 | Types | +3 | −1 |
| 21 | 620–644 | 667–696 | Types | +7 | −2 |
| 22 | 656–661 | 708–714 | Types | +1 | −0 |
| 23 | 695–706 | 748–763 | Types | +4 | −0 |
| 24 | 708–717 | 765–777 | Types | +4 | −1 |
| 25 | 726–731 | 786–792 | Types | +1 | −0 |
| 26 | 739–748 | 800–811 | Types | +3 | −1 |
| 27 | 761–766 | 824–830 | Types | +1 | −0 |
| 28 | 795–805 | 859–871 | Types | +3 | −1 |
| 29 | 822–828 | 888–896 | Types | +3 | −1 |
| 30 | 840–849 | 908–919 | Types | +2 | −0 |
| 31 | 852–872 | 922–950 | Types | +8 | −0 |
| 32 | 874–889 | 952–973 | Types | +6 | −0 |
| 33 | 891–905 | 975–993 | Types | +4 | −0 |
| 34 | 908–919 | 996–1009 | Types | +2 | −0 |
| 35 | 952–998 | 1042–1106 | Types | +20 | −2 |
| 36 | 1002–1007 | 1110–1116 | Types | +1 | −0 |
| 37 | 1009–1024 | 1118–1139 | Types | +6 | −0 |
| 38 | 1026–1031 | 1141–1147 | Types | +1 | −0 |
| 39 | 1051–1072 | 1167–1195 | Types | +8 | −1 |
| 40 | 1083–1090 | 1206–1215 | Types | +2 | −0 |
| 41 | 1095–1100 | 1220–1226 | Types | +1 | −0 |
| 42 | 1102–1109 | 1228–1237 | Types | +2 | −0 |
| 43 | 1118–1123 | 1246–1252 | Types | +1 | −0 |
| 44 | 1174–1179 | 1303–1309 | Types | +1 | −0 |
| 45 | 1198–1212 | 1328–1346 | Types | +5 | −1 |
| 46 | 1216–1225 | 1350–1362 | Types | +3 | −0 |
| 47 | 1231–1236 | 1368–1374 | Types | +1 | −0 |
| 48 | 1293–1298 | 1431–1437 | Types | +1 | −0 |
| 49 | 1338–1345 | 1477–1486 | Types | +2 | −0 |
| 50 | 1348–1353 | 1489–1495 | Types | +1 | −0 |
| 51 | 1359–1368 | 1501–1513 | Types | +4 | −1 |
| 52 | 1376–1382 | 1521–1527 | Types | +1 | −1 |
| 53 | 1414–1419 | 1559–1565 | Types | +1 | −0 |
| 54 | 1441–1446 | 1587–1593 | Types | +1 | −0 |
| 55 | 1463–1468 | 1610–1616 | Types | +1 | −0 |
| 56 | 1474–1481 | 1622–1631 | Types | +2 | −0 |
| 57 | 1541–1547 | 1691–1699 | Types | +3 | −1 |
| 58 | 1556–1564 | 1708–1719 | Types | +5 | −2 |
| 59 | 1611–1617 | 1766–1772 | Types | +1 | −1 |
| 60 | 1635–1640 | 1790–1796 | Types | +1 | −0 |
| 61 | 1651–1656 | 1807–1813 | Types | +1 | −0 |
| 62 | 1662–1667 | 1819–1825 | Types | +1 | −0 |
| 63 | 1671–1680 | 1829–1841 | Types | +3 | −0 |
| 64 | 1687–1692 | 1848–1854 | Types | +1 | −0 |
| 65 | 1695–1701 | 1857–1863 | Types | +1 | −1 |
| 66 | 1734–1746 | 1896–1911 | Types | +3 | −0 |
| 67 | 1765–1771 | 1930–1936 | Types | +1 | −1 |
| 68 | 1791–1796 | 1956–1962 | Types | +1 | −0 |
| 69 | 1805–1816 | 1971–1985 | Types | +3 | −0 |
| 70 | 1820–1825 | 1989–1995 | Types | +1 | −0 |
| 71 | 1844–1849 | 2014–2020 | Types | +1 | −0 |
| 72 | 1879–1890 | 2050–2064 | Types | +3 | −0 |
| 73 | 1893–1902 | 2067–2079 | Types | +3 | −0 |
| 74 | 1922–1927 | 2099–2105 | Types | +1 | −0 |
| 75 | 2010–2019 | 2188–2200 | Types | +3 | −0 |
| 76 | 2050–2056 | 2231–2237 | Types | +1 | −1 |
| 77 | 2076–2081 | 2257–2263 | Types | +1 | −0 |
| 78 | 2095–2100 | 2277–2283 | Types | +1 | −0 |
| 79 | 2111–2116 | 2294–2300 | Types | +1 | −0 |
| 80 | 2138–2143 | 2322–2328 | Types | +1 | −0 |
| 81 | 2155–2170 | 2340–2360 | Types | +5 | −0 |
| 82 | 2176–2181 | 2366–2372 | Types | +1 | −0 |
| 83 | 2191–2197 | 2382–2388 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- paypal.orders/old/ballerinax_paypal.orders.bal.txt	2026-08-12 12:57:30
+++ paypal.orders/new/ballerinax_paypal.orders.bal.txt	2026-08-12 13:19:19
@@ -142,7 +142,9 @@
     MerchantPartnerCustomerId id?;
 };
 
-// Unknown type: Email
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254, minLength: 3}
+type Email string;
 
 # The phone information
 
@@ -158,14 +160,19 @@
 
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
 
-// Unknown type: MerchantPartnerCustomerId
+# The unique ID for a customer generated by PayPal
+@constraint:String {maxLength: 22, minLength: 1, pattern: re `^[0-9a-zA-Z_-]+$`}
+type MerchantPartnerCustomerId string;
 
 # Information used to pay using iDEAL
 
@@ -179,16 +186,24 @@
     IbanLastChars iban_last_chars?;
 };
 
-// Unknown type: CountryCode
+# The [two-character ISO 3166-1 code](/api/rest/reference/country-codes/) that identifies the country or region.<blockquote><strong>Note:</strong> The country code for Great Britain is <code>GB</code> and not <code>UK</code> as used in the top-level domain names for that country. Use the `C2` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.</blockquote>
+@constraint:String {maxLength: 2, minLength: 2, pattern: re `^([A-Z]{2}|C2)$`}
+type CountryCode string;
 
-// Unknown type: FullName
-
-// Unknown type: AltpayRecurringAttributes
+# The full name representation like Mr J Smith
+@constraint:String {maxLength: 300, minLength: 3}
+type FullName string;
 
-// Unknown type: Bic
+type AltpayRecurringAttributes anydata;
 
-// Unknown type: IbanLastChars
+# The business identification code (BIC). In payments systems, a BIC is used to identify a specific business, most commonly a bank
+@constraint:String {maxLength: 11, minLength: 8, pattern: re `^[A-Z-a-z0-9]{4}[A-Z-a-z]{2}[A-Z-a-z0-9]{2}([A-Z-a-z0-9]{3})?$`}
+type Bic string;
 
+# The last characters of the IBAN used to pay
+@constraint:String {maxLength: 34, minLength: 4, pattern: re `[a-zA-Z0-9]{4}`}
+type IbanLastChars string;
+
 # Information needed to pay using giropay
 
 type Giropay record {
@@ -202,7 +217,7 @@
 # The phone type
 type PhoneType2 "FAX"|"HOME"|"MOBILE"|"OTHER"|"PAGER"|"WORK";
 
-// Unknown type: AltpayRecurringAttributesRequest
+type AltpayRecurringAttributesRequest anydata;
 
 
 type PaypalWalletVaultResponseAllOf2 record {
@@ -223,7 +238,7 @@
     MerchantPartnerCustomerId id?;
 };
 
-// Unknown type: VaultOwnerId
+type VaultOwnerId anydata;
 
 # Information needed to pay using eps
 
@@ -239,6 +254,7 @@
 type ExperienceContextBase record {
     Url return_url?;
     # The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.*$`}
     string brand_name?;
     # The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/)
     Language locale?;
@@ -247,16 +263,22 @@
     "GET_FROM_FILE"|"NO_SHIPPING"|"SET_PROVIDED_ADDRESS" shipping_preference?;
 };
 
-// Unknown type: Url
+# Describes the URL
+type Url string;
 
-// Unknown type: Language
+# The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/)
+@constraint:String {maxLength: 10, minLength: 2, pattern: re `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}|[0-9]{3}))?$`}
+type Language string;
 
-// Unknown type: CurrencyCode
+# The [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) that identifies the currency
+@constraint:String {maxLength: 3, minLength: 3}
+type CurrencyCode string;
 
 # Customizes the buyer experience during the approval process for payment with Venmo.<blockquote><strong>Note:</strong> Partners and Marketplaces might configure <code>shipping_preference</code> during partner account setup, which overrides the request values.</blockquote>
 
 type VenmoWalletExperienceContext record {
     # The business name of the merchant. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.*$`}
     string brand_name?;
     # The location from which the shipping address is derived
     "GET_FROM_FILE"|"NO_SHIPPING"|"SET_PROVIDED_ADDRESS" shipping_preference?;
@@ -266,8 +288,10 @@
 
 type VaultResponse record {
     # An array of request-related HATEOAS links
+    @constraint:Array {maxLength: 10, minLength: 1}
     LinkDescription[] links?;
     # The PayPal-generated ID for the saved payment source
+    @constraint:String {maxLength: 255, minLength: 1}
     string id?;
     # The vault status
 
@@ -292,12 +316,16 @@
 
 type ApplePayPaymentData record {
     # Bank Key encrypted Apple Pay PIN. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 2000, minLength: 1, pattern: re `^.*$`}
     string pin?;
     # Encoded Apple Pay EMV Payment Structure used for payments in China. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 2000, minLength: 1, pattern: re `^.*$`}
     string emv_data?;
     # ECI indicator, as defined by 3- Secure. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 256, minLength: 1, pattern: re `^.*$`}
     string eci_indicator?;
     # Online payment cryptogram, as defined by 3D Secure. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 2000, minLength: 1, pattern: re `^.*$`}
     string cryptogram?;
 };
 
@@ -306,6 +334,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2ClientCredentialsGrantConfig auth;
@@ -368,10 +397,13 @@
     # An Internet Protocol address (IP address). This address assigns a numerical label to each device that is connected to a computer network through the Internet Protocol. Supports IPv4 and IPv6 addresses
     IpAddress consumer_ip?;
     # The payer's User Agent. For example, Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0).
+    @constraint:String {maxLength: 256, minLength: 1, pattern: re `^.*$`}
     string consumer_user_agent?;
 };
 
-// Unknown type: IpAddress
+# An Internet Protocol address (IP address). This address assigns a numerical label to each device that is connected to a computer network through the Internet Protocol. Supports IPv4 and IPv6 addresses
+@constraint:String {maxLength: 39, minLength: 7, pattern: re `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$`}
+type IpAddress string;
 
 # A classification for the method of purchase fulfillment
 type ShippingType "SHIPPING"|"PICKUP"|"PICKUP_IN_STORE"|"PICKUP_FROM_PERSON";
@@ -384,6 +416,7 @@
     # An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see <a href="/api/rest/requests/#paypal-auth-assertion">PayPal-Auth-Assertion</a>
     string PayPal\-Auth\-Assertion?;
     # The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>
+    @constraint:String {maxLength: 25, minLength: 1, pattern: re `^[a-zA-Z=]*$`}
     string Prefer?;
     string PayPal\-Client\-Metadata\-Id?;
 };
@@ -400,6 +433,7 @@
     # DEPRECATED. The URL where the customer is redirected after the customer approves the payment. The fields in `application_context` are now available in the `experience_context` object under the `payment_source` which supports them (eg. `payment_source.paypal.experience_context.return_url`). Please specify this field in the `experience_context` object instead of the `application_context` object
     string return_url?;
     # DEPRECATED. The label that overrides the business name in the PayPal account on the PayPal site. The fields in `application_context` are now available in the `experience_context` object under the `payment_source` which supports them (eg. `payment_source.paypal.experience_context.brand_name`). Please specify this field in the `experience_context` object instead of the `application_context` object
+    @constraint:String {maxLength: 127, minLength: 1}
     string brand_name?;
     # The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/)
     Language locale?;
@@ -436,10 +470,13 @@
 
 type NetworkTransactionReference record {
     # The date that the transaction was authorized by the scheme. This field may not be returned for all networks. MasterCard refers to this field as "BankNet reference date
+    @constraint:String {maxLength: 4, minLength: 4, pattern: re `^[0-9]+$`}
     string date?;
     # Reference ID issued for the card transaction. This ID can be used to track the transaction across processors, card brands and issuing banks
+    @constraint:String {maxLength: 36, minLength: 1, pattern: re `^[a-zA-Z0-9]+$`}
     string acquirer_reference_number?;
     # Transaction reference id returned by the scheme. For Visa and Amex, this is the "Tran id" field in response. For MasterCard, this is the "BankNet reference id" field in response. For Discover, this is the "NRID" field in response. The pattern we expect for this field from Visa/Amex/CB/Discover is numeric, Mastercard/BNPP is alphanumeric and Paysecure is alphanumeric with special character -
+    @constraint:String {maxLength: 36, minLength: 9, pattern: re `^[a-zA-Z0-9-_@.:&+=*^'~#!$%()]+$`}
     string id;
     # The card network or brand. Applies to credit, debit, gift, and payment cards
     CardBrand network?;
@@ -494,8 +531,10 @@
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
     string invoice_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^[A-Za-z0-9-_.,]*$`}
     string custom_id?;
     # Reference ID issued for the card transaction. This ID can be used to track the transaction across processors, card brands and issuing banks.
+    @constraint:String {maxLength: 36, minLength: 1, pattern: re `^[a-zA-Z0-9]+$`}
     string acquirer_reference_number?;
     # The reason for the refund. Appears in both the payer's transaction history and the emails that the payer receives.
     string note_to_payer?;
@@ -511,6 +550,7 @@
 
 type Money record {
     # The value, which might be:<ul><li>An integer for currencies like `JPY` that are not typically fractional.</li><li>A decimal fraction for currencies like `TND` that are subdivided into thousandths.</li></ul>For the required number of decimal places for a currency code, see [Currency Codes](/api/rest/reference/currency-codes/)
+    @constraint:String {maxLength: 32, pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
     string value;
     CurrencyCode currency_code;
 };
@@ -519,6 +559,7 @@
 
 type MerchantPayableBreakdown record {
     # An array of platform or partner fees, commissions, or brokerage fees for the refund
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
     Money net_amount_in_receivable_currency?;
     Money total_refunded_amount?;
@@ -546,7 +587,9 @@
     AccountId merchant_id?;
 };
 
-// Unknown type: AccountId
+# The account identifier for a PayPal account
+@constraint:String {maxLength: 13, minLength: 13, pattern: re `^[2-9A-HJ-NP-Z]{13}$`}
+type AccountId string;
 
 # The net amount. Returned when the currency of the refund is different from the currency of the PayPal account where the merchant holds their funds
 
@@ -572,7 +615,9 @@
     DateTime create_time?;
 };
 
-// Unknown type: DateTime
+# The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
+@constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
+type DateTime string;
 
 # The refund information
 
@@ -592,7 +637,9 @@
     DateTime create_time?;
 };
 
-// Unknown type: DateNoTime
+# The stand-alone date, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). To represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone data. Whenever possible, use the standard `date_time` type. This regular expression does not validate all dates. For example, February 31 is valid and nothing is known about leap years
+@constraint:String {maxLength: 10, minLength: 10, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$`}
+type DateNoTime string;
 
 # The status of a captured payment
 
@@ -620,25 +667,30 @@
     LinkDescription[] links?;
 };
 
-// Unknown type: TrackerStatus
+type TrackerStatus anydata;
 
 # The details of the items in the shipment
 
 type TrackerItem record {
     # The item quantity. Must be a whole number
+    @constraint:String {maxLength: 10, minLength: 1, pattern: re `^[1-9][0-9]{0,9}$`}
     string quantity?;
     # The URL of the item's image. File type and size restrictions apply. An image that violates these restrictions will not be honored
+    @constraint:String {maxLength: 2048, minLength: 1, pattern: re `^(https:)([/|.|\w|\s|-])*\.(?:jpg|gif|png|jpeg|JPG|GIF|PNG|JPEG)`}
     string image_url?;
     # The item name or title
+    @constraint:String {maxLength: 127, minLength: 1}
     string name?;
     UniversalProductCode upc?;
     # The stock keeping unit (SKU) for the item. This can contain unicode characters
+    @constraint:String {maxLength: 127, minLength: 1}
     string sku?;
     # The URL to the item being purchased. Visible to buyer and used in buyer experiences
+    @constraint:String {maxLength: 2048, minLength: 1}
     string url?;
 };
 
-// Unknown type: UniversalProductCode
+type UniversalProductCode anydata;
 
 # Represents the Headers record for the operation: orders.track.create
 
@@ -656,6 +708,7 @@
     # The type of landing page to show on the PayPal site for customer checkout
     "LOGIN"|"GUEST_CHECKOUT"|"NO_PREFERENCE" landing_page?;
     # The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.*$`}
     string brand_name?;
     # The merchant-preferred payment methods
     "UNRESTRICTED"|"IMMEDIATE_PAYMENT_REQUIRED" payment_method_preference?;
@@ -695,12 +748,16 @@
 
 type BlikOneClick record {
     # The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant
+    @constraint:String {maxLength: 64, minLength: 3, pattern: re `^[ -~]{3,64}$`}
     string consumer_reference;
     # A Blik-defined identifier for a specific Blik-enabled bank account that is associated with a given merchant. Used only in conjunction with a Consumer Reference
+    @constraint:String {maxLength: 19, minLength: 1, pattern: re `^[0-9]+$`}
     string alias_key?;
     # A bank defined identifier used as a display name to allow the payer to differentiate between multiple registered bank accounts
+    @constraint:String {maxLength: 35, minLength: 8, pattern: re `^[ -~]{8,35}$`}
     string alias_label?;
     # The 6-digit code used to authenticate a consumer within BLIK
+    @constraint:String {maxLength: 6, minLength: 6, pattern: re `^[0-9]{6}$`}
     string auth_code?;
 };
 
@@ -708,10 +765,13 @@
 
 type BlikSeamless record {
     # The 6-digit code used to authenticate a consumer within BLIK
+    @constraint:String {maxLength: 6, minLength: 6, pattern: re `^[0-9]{6}$`}
     string auth_code;
 };
 
-// Unknown type: EmailAddress
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254, minLength: 3}
+type EmailAddress string;
 
 # Information needed to pay using giropay
 
@@ -726,6 +786,7 @@
 
 type PaypalWalletAttributesResponse record {
     # An array of merchant cobranded cards used by buyer to complete an order. This array will be present if a merchant has onboarded their cobranded card with PayPal and provided corresponding label(s)
+    @constraint:Array {maxLength: 25}
     CobrandedCard[] cobranded_cards?;
     # The details about a saved PayPal Wallet payment source
     PaypalWalletVaultResponse vault?;
@@ -739,10 +800,12 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # Array of labels for the cobranded card
+    @constraint:Array {maxLength: 25, minLength: 1}
     CobrandedCardLabelsItemsString[] labels?;
 };
 
-// Unknown type: CobrandedCardLabelsItemsString
+@constraint:String {maxLength: 256, minLength: 1}
+type CobrandedCardLabelsItemsString string;
 
 # The details about a saved PayPal Wallet payment source
 
@@ -761,6 +824,7 @@
 
 type SellerReceivableBreakdown record {
     # An array of platform or partner fees, commissions, or brokerage fees that associated with the captured payment
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
     ExchangeRate exchange_rate?;
     Money paypal_fee?;
@@ -795,11 +859,13 @@
     StoreInVaultInstruction store_in_vault;
 };
 
-// Unknown type: StoreInVaultInstruction
+# Defines how and when the payment source gets vaulted
+type StoreInVaultInstruction "ON_SUCCESS";
 
 
 type VaultVenmoWalletBaseAllOf2 record {
     # The description displayed to Venmo consumer on the approval flow for Venmo, as well as on the Venmo payment token management experience on Venmo.com.
+    @constraint:String {maxLength: 128, minLength: 1}
     string description?;
     # Expected business/pricing model for the billing agreement.
     "IMMEDIATE"|"DEFERRED"|"RECURRING_PREPAID"|"RECURRING_POSTPAID"|"THRESHOLD_PREPAID"|"THRESHOLD_POSTPAID" usage_pattern?;
@@ -822,7 +888,9 @@
     boolean permit_multiple_payment_tokens?;
 };
 
-// Unknown type: VaultId
+# The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the saved payment source can be used for future transactions
+@constraint:String {maxLength: 255, minLength: 1, pattern: re `^[0-9a-zA-Z_-]+$`}
+type VaultId string;
 
 # Provides additional details to process a payment using a `card` that has been stored or is intended to be stored (also referred to as stored_credential or card-on-file).<br/>Parameter compatibility:<br/><ul><li>`payment_type=ONE_TIME` is compatible only with `payment_initiator=CUSTOMER`.</li><li>`usage=FIRST` is compatible only with `payment_initiator=CUSTOMER`.</li><li>`previous_transaction_reference` or `previous_network_transaction_reference` is compatible only with `payment_initiator=MERCHANT`.</li><li>Only one of the parameters - `previous_transaction_reference` and `previous_network_transaction_reference` - can be present in the request.</li></ul>
 
@@ -840,10 +908,12 @@
     Money shipping_amount?;
     Money duty_amount?;
     # Use this field to specify the postal code of the shipping location
+    @constraint:String {maxLength: 60, minLength: 1, pattern: re `^[a-zA-Z0-9_'.-]*$`}
     string ships_from_postal_code?;
     Money discount_amount?;
     AddressPortable shipping_address?;
     # A list of the items that were purchased with this payment. If your merchant account has been configured for Level 3 processing this field will be passed to the processor on your behalf
+    @constraint:Array {maxLength: 100, minLength: 1}
     LineItem[] line_items?;
 };
 
@@ -852,21 +922,29 @@
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
 
@@ -874,16 +952,22 @@
 
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
 
@@ -891,15 +975,19 @@
 
 type Item record {
     # The item quantity. Must be a whole number
+    @constraint:String {maxLength: 10, pattern: re `^[1-9][0-9]{0,9}$`}
     string quantity;
     # The item name or title
+    @constraint:String {maxLength: 127, minLength: 1}
     string name;
     # The detailed item description
+    @constraint:String {maxLength: 127}
     string description?;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money tax?;
     Money unit_amount;
     # The stock keeping unit (SKU) for the item
+    @constraint:String {maxLength: 127}
     string sku?;
     # The item category type
     "DIGITAL_GOODS"|"PHYSICAL_GOODS"|"DONATION" category?;
@@ -908,12 +996,14 @@
 
 type LineItemAllOf2 record {
     # Code used to classify items purchased and track the total amount spent across various categories of products and services. Different corporate purchasing organizations may use different standards, but the United Nations Standard Products and Services Code (UNSPSC) is frequently used.
+    @constraint:String {maxLength: 12, minLength: 1, pattern: re `^[a-zA-Z0-9_'.-]*$`}
     string commodity_code?;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money discount_amount?;
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money total_amount?;
     # Unit of measure is a standard used to express the magnitude of a quantity in international trade. Most commonly used (but not limited to) examples are: Acre (ACR), Ampere (AMP), Centigram (CGM), Centimetre (CMT), Cubic inch (INQ), Cubic metre (MTQ), Fluid ounce (OZA), Foot (FOT), Hour (HUR), Item (ITM), Kilogram (KGM), Kilometre (KMT), Kilowatt (KWT), Liquid gallon (GLL), Liter (LTR), Pounds (LBS), Square foot (FTK).
+    @constraint:String {maxLength: 12, minLength: 1, pattern: re `^[a-zA-Z0-9_'.-]*$`}
     string unit_of_measure?;
 };
 
@@ -952,47 +1042,65 @@
     "VERIFIED"|"UNVERIFIED" account_status?;
 };
 
-// Unknown type: AccountId2
+# The PayPal payer ID, which is a masked version of the PayPal account number intended for use with third parties. The account number is reversibly encrypted and a proprietary variant of Base32 is used to encode the result
+@constraint:String {maxLength: 13, minLength: 13, pattern: re `^[2-9A-HJ-NP-Z]{13}$`}
+type AccountId2 string;
 
 # The portable international postal address. Maps to [AddressValidationMetadata](https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling form controls: the autocomplete attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute)
 
 type AddressPortable2 record {
     CountryCode2 country_code;
     # The highest-level sub-division in a country, which is usually a province, state, or ISO-3166-2 subdivision. This data is formatted for postal delivery, for example, `CA` and not `California`. Value, by country, is:<ul><li>UK. A county.</li><li>US. A state.</li><li>Canada. A province.</li><li>Japan. A prefecture.</li><li>Switzerland. A *kanton*.</li></ul>
+    @constraint:String {maxLength: 300}
     string admin_area_1?;
     # The first line of the address, such as number and street, for example, `173 Drury Lane`. Needed for data entry, and Compliance and Risk checks. This field needs to pass the full address
+    @constraint:String {maxLength: 300}
     string address_line_1?;
     # The sub-locality, suburb, neighborhood, or district. This is smaller than `admin_area_level_2`. Value is:<ul><li>Brazil. Suburb, *bairro*, or neighborhood.</li><li>India. Sub-locality or district. Street name information isn't always available, but a sub-locality or district can be a very small area.</li></ul>
+    @constraint:String {maxLength: 100}
     string admin_area_3?;
     AddressDetails1 address_details?;
     # A city, town, or village. Smaller than `admin_area_level_1`
+    @constraint:String {maxLength: 120}
     string admin_area_2?;
     # The third line of the address, if needed. Examples include a street complement for Brazil, direction text, such as `next to Walmart`, or a landmark in an Indian address
+    @constraint:String {maxLength: 100}
     string address_line_3?;
     # The second line of the address, for example, a suite or apartment number
+    @constraint:String {maxLength: 300}
     string address_line_2?;
     # The neighborhood, ward, or district. This is smaller than `admin_area_level_3` or `sub_locality`. Value is:<ul><li>The postal sorting code that is used in Guernsey and many French territories, such as French Guiana.</li><li>The fine-grained administrative levels in China.</li></ul>
+    @constraint:String {maxLength: 100}
     string admin_area_4?;
     # The postal code, which is the ZIP code or equivalent. Typically required for countries with a postal code or an equivalent. See [postal code](https://en.wikipedia.org/wiki/Postal_code)
+    @constraint:String {maxLength: 60}
     string postal_code?;
 };
 
-// Unknown type: CountryCode2
+# The [2-character ISO 3166-1 code](/api/rest/reference/country-codes/) that identifies the country or region.<blockquote><strong>Note:</strong> The country code for Great Britain is <code>GB</code> and not <code>UK</code> as used in the top-level domain names for that country. Use the `C2` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.</blockquote>
+@constraint:String {maxLength: 2, minLength: 2, pattern: re `^([A-Z]{2}|C2)$`}
+type CountryCode2 string;
 
 # The non-portable additional address details include fine-grain address information for Compliance, Risk, and other scenarios. This isn't portable with common third-party and open source applications. This can include data that is redundant with core fields. For example, `address_portable.address_line_1` is usually a combination of `address_details.street_number`, `street_name`, and `street_type`
 
 type AddressDetails1 record {
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
 
@@ -1002,6 +1110,7 @@
     # The customer's tax ID type
     "BR_CPF"|"BR_CNPJ" tax_id_type;
     # The customer's tax ID value
+    @constraint:String {maxLength: 14, minLength: 1, pattern: re `([a-zA-Z0-9])`}
     string tax_id;
 };
 
@@ -1009,16 +1118,22 @@
 
 type Name2 record {
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
 };
 
@@ -1026,6 +1141,7 @@
 
 type Phone2 record {
     # The national number, in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). The combined length of the country calling code (CC) and the national number must not be greater than 15 digits. The national number consists of a national destination code (NDC) and subscriber number (SN)
+    @constraint:String {maxLength: 14, minLength: 1, pattern: re `^[0-9]{1,14}?$`}
     string national_number;
 };
 
@@ -1051,22 +1167,29 @@
 
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
 
-// Unknown type: AuthenticationFlow
+type AuthenticationFlow anydata;
 
 # The tracking response on creation of tracker
 
@@ -1083,8 +1206,10 @@
 
 type ShipmentTracker record {
     # The PayPal transaction ID
+    @constraint:String {maxLength: 50, minLength: 1, pattern: re `^[a-zA-Z0-9]*$`}
     string transaction_id;
     # The quantity of items shipped
+    @constraint:Int {minValue: 1, maxValue: 100}
     int quantity?;
     # If true, sends an email notification to the buyer of the PayPal transaction. The email contains the tracking information that was uploaded through the API
     boolean notify_buyer?;
@@ -1095,6 +1220,7 @@
     # To denote whether the shipment is sent forward to the receiver or returned back
     "FORWARD"|"RETURN" shipment_direction?;
     # The postage payment ID. This property supports Unicode
+    @constraint:String {maxLength: 64, minLength: 1}
     string postage_payment_id?;
     # The carrier for the shipment. Some carriers have a global version as well as local subsidiaries. The subsidiaries are repeated over many countries and might also have an entry in the global list. Choose the carrier for your country. If the carrier is not available for your country, choose the global version of the carrier. If your carrier name is not in the list, set `carrier` to `OTHER` and set carrier name in `carrier_name_other`. For allowed values, see <a href="/docs/tracking/reference/carriers/">Carriers</a>
     ShipmentCarrier carrier?;
@@ -1102,8 +1228,10 @@
     "MERCHANT"|"CONSUMER"|"PARTNER" shipment_uploader?;
     DateTime last_updated_time?;
     # The name of the carrier for the shipment. Provide this value only if the carrier parameter is OTHER. This property supports Unicode
+    @constraint:String {maxLength: 64, minLength: 1}
     string carrier_name_other?;
     # The tracking number for the shipment. This property supports Unicode
+    @constraint:String {maxLength: 64, minLength: 1}
     string tracking_number?;
     # The status of the item shipment. For allowed values, see <a href="/docs/tracking/reference/shipping-status/">Shipping Statuses</a>
     ShipmentTrackingStatus status;
@@ -1118,6 +1246,7 @@
 
 type OrderTrackerRequestAllOf2 record {
     # The PayPal capture ID.
+    @constraint:String {maxLength: 50, minLength: 1, pattern: re `^[a-zA-Z0-9]*$`}
     string capture_id;
     # If true, sends an email notification to the payer of the PayPal transaction. The email contains the tracking information that was uploaded through the API.
     boolean notify_payer?;
@@ -1174,6 +1303,7 @@
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
     string invoice_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
+    @constraint:String {maxLength: 127}
     string custom_id?;
     # Reference values used by the card network to identify a transaction
     NetworkTransactionReference network_transaction_reference?;
@@ -1198,15 +1328,19 @@
 
 type BinDetails record {
     # The Bank Identification Number (BIN) signifies the number that is being used to identify the granular level details (except the PII information) of the card
+    @constraint:String {maxLength: 25, minLength: 1, pattern: re `^[0-9]+$`}
     string bin?;
     CountryCode bin_country_code?;
     # The issuer of the card instrument
+    @constraint:String {maxLength: 64, minLength: 1}
     string issuing_bank?;
     # The type of card product assigned to the BIN by the issuer. These values are defined by the issuer and may change over time. Some examples include: PREPAID_GIFT, CONSUMER, CORPORATE
+    @constraint:Array {maxLength: 256, minLength: 1}
     BinDetailsProductsItemsString[] products?;
 };
 
-// Unknown type: BinDetailsProductsItemsString
+@constraint:String {maxLength: 255, minLength: 1}
+type BinDetailsProductsItemsString string;
 
 # Status of Authentication eligibility
 type Enrolled "Y"|"N"|"U"|"B";
@@ -1216,10 +1350,13 @@
 type P24 record {
     CountryCode country_code?;
     # P24 generated payment description
+    @constraint:String {maxLength: 2000, minLength: 1}
     string payment_descriptor?;
     # Numeric identifier of the payment scheme or bank used for the payment
+    @constraint:String {maxLength: 300, minLength: 1}
     string method_id?;
     # Friendly name of the payment scheme or bank used for the payment
+    @constraint:String {maxLength: 2000, minLength: 1}
     string method_description?;
     # The full name representation like Mr J Smith
     FullName name?;
@@ -1231,6 +1368,7 @@
 
 type BlikOneClickResponse record {
     # The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant
+    @constraint:String {maxLength: 64, minLength: 3, pattern: re `^[ -~]{3,64}$`}
     string consumer_reference?;
 };
 
@@ -1293,6 +1431,7 @@
     FullName name?;
     AltpayRecurringAttributes attributes?;
     # The last digits of the card used to fund the Bancontact payment
+    @constraint:String {maxLength: 4, minLength: 4, pattern: re `[0-9]{4}`}
     string card_last_digits?;
     # The business identification code (BIC). In payments systems, a BIC is used to identify a specific business, most commonly a bank
     Bic bic?;
@@ -1338,8 +1477,10 @@
     AuthenticationResponse authentication_result?;
     BinDetails bin_details?;
     # The card holder's name as it appears on the card
+    @constraint:String {maxLength: 300, minLength: 2}
     string name?;
     # Array of brands or networks associated with the card
+    @constraint:Array {maxLength: 256, minLength: 1}
     CardBrand[] available_networks?;
     # Additional attributes associated with the use of this card
     CardAttributesResponse attributes?;
@@ -1348,6 +1489,7 @@
     # The payment card type
     "CREDIT"|"DEBIT"|"PREPAID"|"UNKNOWN" 'type?;
     # The last digits of the payment card
+    @constraint:String {pattern: re `[0-9]{2,}`}
     string last_digits?;
     # The card network or brand. Applies to credit, debit, gift, and payment cards
     CardBrand brand?;
@@ -1359,10 +1501,13 @@
     # The year and month, in ISO-8601 `YYYY-MM` date format. See [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6)
     DateYearMonth expiry?;
     # The last digits of the payment card
+    @constraint:String {maxLength: 4, minLength: 2, pattern: re `[0-9]{2,}`}
     string last_digits?;
 };
 
-// Unknown type: DateYearMonth
+# The year and month, in ISO-8601 `YYYY-MM` date format. See [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6)
+@constraint:String {maxLength: 7, minLength: 7, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])$`}
+type DateYearMonth string;
 
 # Results of Authentication such as 3D Secure
 
@@ -1376,7 +1521,7 @@
 # Liability shift indicator. The outcome of the issuer's authentication
 type LiabilityShift "NO"|"POSSIBLE"|"UNKNOWN";
 
-// Unknown type: ExemptionDetails
+type ExemptionDetails anydata;
 
 # Results of 3D Secure Authentication
 
@@ -1414,6 +1559,7 @@
     # The portable international postal address. Maps to [AddressValidationMetadata](https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling form controls: the autocomplete attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute)
     AddressPortable2 address?;
     # The Venmo user name chosen by the user, also know as a Venmo handle
+    @constraint:String {maxLength: 50, minLength: 1, pattern: re `^[-a-zA-Z0-9_]*$`}
     string user_name?;
     # The name of the party
     Name2 name?;
@@ -1441,6 +1587,7 @@
 
 type VaultPaypalWalletBaseAllOf2 record {
     # The description displayed to PayPal consumer on the approval flow for PayPal, as well as on the PayPal payment token management experience on PayPal.com.
+    @constraint:String {maxLength: 128, minLength: 1}
     string description?;
     # Expected business/pricing model for the billing agreement.
     "IMMEDIATE"|"DEFERRED"|"RECURRING_PREPAID"|"RECURRING_POSTPAID"|"THRESHOLD_PREPAID"|"THRESHOLD_POSTPAID" usage_pattern?;
@@ -1463,6 +1610,7 @@
     # The name of the party
     Name name?;
     # An array of shipping options that the payee or merchant offers to the payer to ship or pick up their items
+    @constraint:Array {maxLength: 10}
     ShippingOption[] options?;
     # A classification for the method of purchase fulfillment (e.g shipping, in-store pickup, etc). Either `type` or `options` may be present, but not both
     "SHIPPING"|"PICKUP_IN_PERSON"|"PICKUP_IN_STORE"|"PICKUP_FROM_PERSON" 'type?;
@@ -1474,8 +1622,10 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # A unique ID that identifies a payer-selected shipping option
+    @constraint:String {maxLength: 127}
     string id;
     # A description that the payer sees, which helps them choose an appropriate shipping option. For example, `Free Shipping`, `USPS Priority Shipping`, `Expédition prioritaire USPS`, or `USPS yōuxiān fā huò`. Localize this description to the payer's locale
+    @constraint:String {maxLength: 127}
     string label;
     # A classification for the method of purchase fulfillment
     ShippingType 'type?;
@@ -1541,7 +1691,9 @@
     VaultId vault_id?;
 };
 
-// Unknown type: BillingAgreementId
+# The PayPal billing agreement ID. References an approved recurring payment for goods or services
+@constraint:String {maxLength: 128, minLength: 2, pattern: re `^[a-zA-Z0-9-]+$`}
+type BillingAgreementId string;
 
 # The JSON patch object to apply partial updates to resources
 
@@ -1556,9 +1708,12 @@
     anydata value?;
 };
 
-// Unknown type: PatchRequest
+# An array of JSON patch objects to apply partial updates to resources
+type PatchRequest Patch[];
 
-// Unknown type: InstrumentId
+# The identifier of the instrument
+@constraint:String {maxLength: 256, minLength: 1, pattern: re `^[A-Za-z0-9-_.+=]+$`}
+type InstrumentId string;
 
 # Completes an capture payment for an order
 
@@ -1611,7 +1766,7 @@
     Bic bic?;
 };
 
-// Unknown type: GooglePayRequest
+type GooglePayRequest anydata;
 
 # Information needed to pay using Trustly
 
@@ -1635,6 +1790,7 @@
 
 type Token record {
     # The PayPal-generated ID for the token
+    @constraint:String {maxLength: 255, minLength: 1, pattern: re `^[0-9a-zA-Z_-]+$`}
     string id;
     # The tokenization method that generated the ID
     "BILLING_AGREEMENT" 'type;
@@ -1651,6 +1807,7 @@
     Phone phone_number?;
     ApplePayAttributes attributes?;
     # ApplePay transaction identifier, this will be the unique identifier for this transaction provided by Apple. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 250, minLength: 1, pattern: re `^.*$`}
     string id?;
     VaultId vault_id?;
 };
@@ -1662,6 +1819,7 @@
     Card tokenized_card;
     ApplePayPaymentData payment_data?;
     # Apple Pay Hex-encoded device manufacturer identifier. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 2000, minLength: 1, pattern: re `^.*$`}
     string device_manufacturer_id?;
     # Indicates the type of payment data passed, in case of Non China the payment data is 3DSECURE and for China it is EMV
     "3DSECURE"|"EMV" payment_data_type?;
@@ -1671,10 +1829,13 @@
 
 type Card record {
     # The primary account number (PAN) for the payment card
+    @constraint:String {maxLength: 19, minLength: 13, pattern: re `^[0-9]{13,19}$`}
     string number?;
     # The three- or four-digit security code of the card. Also known as the CVV, CVC, CVN, CVE, or CID. This parameter cannot be present in the request when `payment_initiator=MERCHANT`
+    @constraint:String {maxLength: 4, minLength: 3, pattern: re `^[0-9]{3,4}$`}
     string security_code?;
     # The card holder's name as it appears on the card
+    @constraint:String {maxLength: 300, minLength: 1, pattern: re `^.{1,300}$`}
     string name?;
     AddressPortable billing_address?;
     # Additional attributes associated with the use of this card
@@ -1687,6 +1848,7 @@
     # Type of card. i.e Credit, Debit and so on
     CardType 'type?;
     # The last digits of the payment card
+    @constraint:String {maxLength: 4, minLength: 2, pattern: re `^[0-9]{2,4}$`}
     string last_digits?;
     # The card network or brand. Applies to credit, debit, gift, and payment cards
     CardBrand brand?;
@@ -1695,7 +1857,7 @@
 # Type of card. i.e Credit, Debit and so on
 type CardType "CREDIT"|"DEBIT"|"PREPAID"|"STORE"|"UNKNOWN";
 
-// Unknown type: ApplePayAttributes
+type ApplePayAttributes anydata;
 
 # Information needed to pay using Bancontact
 
@@ -1734,13 +1896,16 @@
 
 type NetworkTokenRequest record {
     # Third party network token number
+    @constraint:String {maxLength: 19, minLength: 13, pattern: re `^[0-9]{13,19}$`}
     string number;
     EciFlag eci_flag?;
     # The year and month, in ISO-8601 `YYYY-MM` date format. See [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6)
     DateYearMonth expiry;
     # A TRID, or a Token Requestor ID, is an identifier used by merchants to request network tokens from card networks. A TRID is a precursor to obtaining a network token for a credit card primary account number (PAN), and will aid in enabling secure card on file (COF) payments and reducing fraud
+    @constraint:String {maxLength: 11, minLength: 1, pattern: re `^[0-9A-Z_]+$`}
     string token_requestor_id?;
     # An Encrypted one-time use value that's sent along with Network Token. This field is not required to be present for recurring transactions
+    @constraint:String {maxLength: 32, minLength: 28, pattern: re `^.*$`}
     string cryptogram?;
 };
 
@@ -1765,7 +1930,7 @@
     InstrumentId id?;
     DateYearMonth expiry?;
     CardBrand card_type?;
-    CardType type?;
+    CardType 'type?;
     string last_digits?;
     CardBrand brand?;
     VaultId vault_id?;
@@ -1791,6 +1956,7 @@
     # An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see <a href="/api/rest/requests/#paypal-auth-assertion">PayPal-Auth-Assertion</a>
     string PayPal\-Auth\-Assertion?;
     # The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>
+    @constraint:String {maxLength: 25, minLength: 1, pattern: re `^[a-zA-Z=]*$`}
     string Prefer?;
     string PayPal\-Client\-Metadata\-Id?;
 };
@@ -1805,12 +1971,15 @@
 
 type OrderConfirmApplicationContext record {
     # The URL where the customer is redirected after the customer approves the payment
+    @constraint:String {maxLength: 4000, minLength: 10}
     string return_url?;
     # Label to present to your payer as part of the PayPal hosted web experience
+    @constraint:String {maxLength: 127, minLength: 1}
     string brand_name?;
     # The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/)
     Language locale?;
     # The URL where the customer is redirected after the customer cancels the payment
+    @constraint:String {maxLength: 4000, minLength: 10}
     string cancel_url?;
     StoredPaymentSource stored_payment_source?;
 };
@@ -1820,6 +1989,7 @@
 type Level2CardProcessingData record {
     Money tax_total?;
     # Use this field to pass a purchase identification value of up to 12 ASCII characters for AIB and 17 ASCII characters for all other processors
+    @constraint:String {maxLength: 17, minLength: 1}
     string invoice_id?;
 };
 
@@ -1844,6 +2014,7 @@
     # The customer who approves and pays for the order. The customer is also known as the payer
     Payer payer?;
     # An array of purchase units. Each purchase unit establishes a contract between a customer and merchant. Each purchase unit represents either a full or partial order that the customer intends to purchase from the merchant.
+    @constraint:Array {maxLength: 10, minLength: 1}
     PurchaseUnit[] purchase_units?;
     # The order status
     OrderStatus status?;
@@ -1879,12 +2050,15 @@
     # The total order amount with an optional breakdown that provides details, such as the total item amount, total tax amount, shipping, handling, insurance, and discounts, if any.<br/>If you specify `amount.breakdown`, the amount equals `item_total` plus `tax_total` plus `shipping` plus `handling` plus `insurance` minus `shipping_discount` minus discount.<br/>The amount must be a positive number. For listed of supported currencies and decimal precision, see the PayPal REST APIs <a href="/docs/integration/direct/rest/currency-codes/">Currency Codes</a>
     AmountWithBreakdown amount?;
     # The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must update the order through `PATCH`. If you omit this value and the order contains only one purchase unit, PayPal sets this value to `default`. <blockquote><strong>Note:</strong> If there are multiple purchase units, <code>reference_id</code> is required for each purchase unit.</blockquote>
+    @constraint:String {maxLength: 256, minLength: 1}
     string reference_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports
+    @constraint:String {maxLength: 127, minLength: 1}
     string custom_id?;
     # The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments, captured payments, and refunds
     PaymentCollection payments?;
     # The purchase description
+    @constraint:String {maxLength: 127, minLength: 1}
     string description?;
     PaymentInstruction payment_instruction?;
     # The merchant who receives the funds and fulfills the order. The merchant is also known as the payee
@@ -1893,10 +2067,13 @@
     # The order shipping details
     ShippingWithTrackingDetails shipping?;
     # The payment descriptor on account transactions on the customer's credit card statement, that PayPal sends to processors. The maximum length of the soft descriptor information that you can pass in the API field is 22 characters, in the following format:<code>22 - len(PAYPAL * (8)) - len(<var>Descriptor in Payment Receiving Preferences of Merchant account</var> + 1)</code>The PAYPAL prefix uses 8 characters.<br/><br/>The soft descriptor supports the following ASCII characters:<ul><li>Alphanumeric characters</li><li>Dashes</li><li>Asterisks</li><li>Periods (.)</li><li>Spaces</li></ul>For Wallet payments marketplace integrations:<ul><li>The merchant descriptor in the Payment Receiving Preferences must be the marketplace name.</li><li>You can't use the remaining space to show the customer service number.</li><li>The remaining spaces can be a combination of seller name and country.</li></ul><br/>For unbranded payments (Direct Card) marketplace integrations, use a combination of the seller name and phone number
+    @constraint:String {maxLength: 22, minLength: 1}
     string soft_descriptor?;
     # The API caller-provided external invoice ID for this order
+    @constraint:String {maxLength: 127, minLength: 1}
     string invoice_id?;
     # The PayPal-generated ID for the purchase unit. This ID appears in both the payer's transaction history and the emails that the payer receives. In addition, this ID is available in transaction and settlement reports that merchants and API callers can use to reconcile transactions. This ID is only available when an order is saved by calling <code>v2/checkout/orders/id/save</code>
+    @constraint:String {maxLength: 19, minLength: 1}
     string id?;
     # An array of items that the customer purchases from the merchant
     Item[] items?;
@@ -1922,6 +2099,7 @@
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
     string invoice_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
+    @constraint:String {maxLength: 127}
     string custom_id?;
     # Reference values used by the card network to identify a transaction
     NetworkTransactionReference network_transaction_reference?;
@@ -2010,10 +2188,13 @@
 type PaymentInstruction record {
     DisbursementMode disbursement_mode?;
     # An array of various fees, commissions, tips, or donations. This field is only applicable to merchants that been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
     # FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for eligible integrations) to be used when amount is settled/received into the payee account
+    @constraint:String {maxLength: 4000, minLength: 1, pattern: re `^.*$`}
     string payee_receivable_fx_rate_id?;
     # This field is only enabled for selected merchants/partners to use and provides the ability to trigger a specific pricing rate/plan for a payment transaction. The list of eligible 'payee_pricing_tier_id' would be provided to you by your Account Manager. Specifying values other than the one provided to you by your account manager would result in an error
+    @constraint:String {maxLength: 20, minLength: 1, pattern: re `^.*$`}
     string payee_pricing_tier_id?;
 };
 
@@ -2050,7 +2231,7 @@
     AddressPortable address?;
     Name name?;
     ShippingOption[] options?;
-    "SHIPPING"|"PICKUP_IN_PERSON"|"PICKUP_IN_STORE"|"PICKUP_FROM_PERSON" type?;
+    "SHIPPING"|"PICKUP_IN_PERSON"|"PICKUP_IN_STORE"|"PICKUP_FROM_PERSON" 'type?;
     Tracker[] trackers?;
 };
 
@@ -2076,6 +2257,7 @@
     string PayPal\-Request\-Id?;
     string PayPal\-Client\-Metadata\-Id?;
     # The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>
+    @constraint:String {maxLength: 25, minLength: 1, pattern: re `^[a-zA-Z=]*$`}
     string Prefer?;
     string PayPal\-Partner\-Attribution\-Id?;
 };
@@ -2095,6 +2277,7 @@
 
 type OrdersGetQueries record {
     # A comma-separated list of fields that should be returned for the order. Valid filter field is `payment_source`
+    @constraint:String {pattern: re `^[a-z_]*$`}
     string fields?;
 };
 
@@ -2111,6 +2294,7 @@
     # The customer who approves and pays for the order. The customer is also known as the payer
     Payer payer?;
     # An array of purchase units. Each purchase unit establishes a contract between a customer and merchant. Each purchase unit represents either a full or partial order that the customer intends to purchase from the merchant.
+    @constraint:Array {maxLength: 10, minLength: 1}
     PurchaseUnit[] purchase_units?;
     # The order status
     OrderStatus status?;
@@ -2138,6 +2322,7 @@
 type OrderRequest record {
     OrderApplicationContext application_context?;
     # An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee
+    @constraint:Array {maxLength: 10, minLength: 1}
     PurchaseUnitRequest[] purchase_units;
     PaymentSource payment_source?;
     # The intent to either capture payment immediately or authorize a payment for an order after order creation
@@ -2155,16 +2340,21 @@
     AmountWithBreakdown amount;
     SupplementaryData supplementary_data?;
     # The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must update the order through `PATCH`. If you omit this value and the order contains only one purchase unit, PayPal sets this value to `default`
+    @constraint:String {maxLength: 256, minLength: 1}
     string reference_id?;
     # The shipping details
     ShippingDetail shipping?;
     # The soft descriptor is the dynamic text used to construct the statement descriptor that appears on a payer's card statement.<br><br>If an Order is paid using the "PayPal Wallet", the statement descriptor will appear in following format on the payer's card statement: <code><var>PAYPAL_prefix</var>+(space)+<var>merchant_descriptor</var>+(space)+ <var>soft_descriptor</var></code><blockquote><strong>Note:</strong> The merchant descriptor is the descriptor of the merchant’s payment receiving preferences which can be seen by logging into the merchant account https://www.sandbox.paypal.com/businessprofile/settings/info/edit</blockquote>The <code>PAYPAL</code> prefix uses 8 characters. Only the first 22 characters will be displayed in the statement. <br>For example, if:<ul><li>The PayPal prefix toggle is <code>PAYPAL *</code>.</li><li>The merchant descriptor in the profile is <code>Janes Gift</code>.</li><li>The soft descriptor is <code>800-123-1234</code>.</li></ul>Then, the statement descriptor on the card is <code>PAYPAL * Janes Gift 80</code>
+    @constraint:String {maxLength: 22, minLength: 1}
     string soft_descriptor?;
     # The API caller-provided external ID. Used to reconcile client transactions with PayPal transactions. Appears in transaction and settlement reports but is not visible to the payer
+    @constraint:String {maxLength: 127, minLength: 1}
     string custom_id?;
     # The purchase description. The maximum length of the character is dependent on the type of characters used. The character length is specified assuming a US ASCII character. Depending on type of character; (e.g. accented character, Japanese characters) the number of characters that that can be specified as input might not equal the permissible max length
+    @constraint:String {maxLength: 127, minLength: 1}
     string description?;
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives
+    @constraint:String {maxLength: 127, minLength: 1}
     string invoice_id?;
     PaymentInstruction payment_instruction?;
     # An array of items that the customer purchases from the merchant
@@ -2176,6 +2366,7 @@
 type OrdersConfirmHeaders record {
     string PayPal\-Client\-Metadata\-Id?;
     # The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>
+    @constraint:String {maxLength: 25, minLength: 1, pattern: re `^[a-zA-Z=]*$`}
     string Prefer?;
 };
 
@@ -2191,7 +2382,7 @@
 
     # Show order details
     # 
-    resource function get orders/[string id](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, OrdersGetQueries queries) returns Order|error;
+    resource function get orders/[string id](map<string|string[]> headers = {}, string fields = "", OrdersGetQueries queries) returns Order|error;
 
     # Update order
     # 
`````

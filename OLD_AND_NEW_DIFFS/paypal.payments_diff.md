# paypal.payments — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `paypal.payments` |
| **Old file** | `paypal.payments/old/ballerinax_paypal.payments.bal.txt` |
| **New file** | `paypal.payments/new/ballerinax_paypal.payments.bal.txt` |
| **Old lines** | 716 |
| **New lines** | 750 |
| **Lines added** | 38 |
| **Lines removed** | 4 |
| **Hunks** | 15 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (4)

- `type AccountId`
- `type CurrencyCode`
- `type DateTime`
- `type Email`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 142–150 | 142–154 | Types | +6 | −2 |
| 2 | 155–160 | 159–165 | Types | +1 | −0 |
| 3 | 170–189 | 175–200 | Types | +7 | −1 |
| 4 | 201–207 | 212–220 | Types | +3 | −1 |
| 5 | 218–225 | 231–240 | Types | +2 | −0 |
| 6 | 247–252 | 262–268 | Types | +1 | −0 |
| 7 | 268–273 | 284–290 | Types | +1 | −0 |
| 8 | 362–367 | 379–385 | Types | +1 | −0 |
| 9 | 446–455 | 464–476 | Types | +3 | −0 |
| 10 | 484–491 | 505–514 | Types | +2 | −0 |
| 11 | 501–506 | 524–530 | Types | +1 | −0 |
| 12 | 567–576 | 591–603 | Types | +3 | −0 |
| 13 | 635–648 | 662–678 | Types | +3 | −0 |
| 14 | 652–661 | 682–694 | Types | +3 | −0 |
| 15 | 664–669 | 697–703 | Types | +1 | −0 |

---

## Unified diff

`````diff
--- paypal.payments/old/ballerinax_paypal.payments.bal.txt	2026-08-12 12:57:30
+++ paypal.payments/new/ballerinax_paypal.payments.bal.txt	2026-08-12 13:19:19
@@ -142,9 +142,13 @@
     oauth2:ClientConfiguration clientConfig?; // Special Agent Note: ClientConfiguration FROM ballerina/oauth2 package
 };
 
-// Unknown type: Email
+# The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>
+@constraint:String {maxLength: 254, minLength: 3}
+type Email string;
 
-// Unknown type: AccountId
+# The account identifier for a PayPal account
+@constraint:String {maxLength: 13, minLength: 13, pattern: re `^[2-9A-HJ-NP-Z]{13}$`}
+type AccountId string;
 
 
 type AuthorizationAllOf2 record {
@@ -155,6 +159,7 @@
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
     string invoice_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
+    @constraint:String {maxLength: 127}
     string custom_id?;
     # Reference values used by the card network to identify a transaction
     NetworkTransactionReference network_transaction_reference?;
@@ -170,20 +175,26 @@
 
 type Money record {
     # The value, which might be:<ul><li>An integer for currencies like `JPY` that are not typically fractional.</li><li>A decimal fraction for currencies like `TND` that are subdivided into thousandths.</li></ul>For the required number of decimal places for a currency code, see [Currency Codes](/api/rest/reference/currency-codes/)
+    @constraint:String {maxLength: 32, pattern: re `^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$`}
     string value;
     CurrencyCode currency_code;
 };
 
-// Unknown type: CurrencyCode
+# The [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) that identifies the currency
+@constraint:String {maxLength: 3, minLength: 3}
+type CurrencyCode string;
 
 # Reference values used by the card network to identify a transaction
 
 type NetworkTransactionReference record {
     # The date that the transaction was authorized by the scheme. This field may not be returned for all networks. MasterCard refers to this field as "BankNet reference date
+    @constraint:String {maxLength: 4, minLength: 4, pattern: re `^[0-9]+$`}
     string date?;
     # Reference ID issued for the card transaction. This ID can be used to track the transaction across processors, card brands and issuing banks
+    @constraint:String {maxLength: 36, minLength: 1, pattern: re `^[a-zA-Z0-9]+$`}
     string acquirer_reference_number?;
     # Transaction reference id returned by the scheme. For Visa and Amex, this is the "Tran id" field in response. For MasterCard, this is the "BankNet reference id" field in response. For Discover, this is the "NRID" field in response. The pattern we expect for this field from Visa/Amex/CB/Discover is numeric, Mastercard/BNPP is alphanumeric and Paysecure is alphanumeric with special character -
+    @constraint:String {maxLength: 36, minLength: 9, pattern: re `^[a-zA-Z0-9-]+$`}
     string id;
     # The card network or brand. Applies to credit, debit, gift, and payment cards
     CardBrand network?;
@@ -201,7 +212,9 @@
     "ELIGIBLE"|"PARTIALLY_ELIGIBLE"|"NOT_ELIGIBLE" status?;
 };
 
-// Unknown type: DateTime
+# The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>
+@constraint:String {maxLength: 64, minLength: 20, pattern: re `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$`}
+type DateTime string;
 
 # The request-related [HATEOAS link](/api/rest/responses/#hateoas-links) information
 
@@ -218,8 +231,10 @@
 
 type SupplementaryPurchaseData record {
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.{1,127}$`}
     string invoice_id?;
     # An informational note about this settlement. Appears in both the payer's transaction history and the emails that the payer receives
+    @constraint:String {maxLength: 255, minLength: 1, pattern: re `^.{1,255}$`}
     string note_to_payer?;
 };
 
@@ -247,6 +262,7 @@
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
     string invoice_id?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
+    @constraint:String {maxLength: 127}
     string custom_id?;
     # Reference values used by the card network to identify a transaction
     NetworkTransactionReference network_transaction_reference?;
@@ -268,6 +284,7 @@
 
 type SellerReceivableBreakdown record {
     # An array of platform or partner fees, commissions, or brokerage fees that associated with the captured payment
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
     ExchangeRate exchange_rate?;
     Money paypal_fee?;
@@ -362,6 +379,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     OAuth2ClientCredentialsGrantConfig auth;
@@ -446,10 +464,13 @@
 
 type RelatedIds record {
     # Authorization ID related to the resource
+    @constraint:String {maxLength: 20, minLength: 1, pattern: re `^[A-Z0-9]+$`}
     string authorization_id?;
     # Capture ID related to the resource
+    @constraint:String {maxLength: 20, minLength: 1, pattern: re `^[A-Z0-9]+$`}
     string capture_id?;
     # Order ID related to the resource
+    @constraint:String {maxLength: 20, minLength: 1, pattern: re `^[A-Z0-9]+$`}
     string order_id?;
 };
 
@@ -484,8 +505,10 @@
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
@@ -501,6 +524,7 @@
 
 type MerchantPayableBreakdown record {
     # An array of platform or partner fees, commissions, or brokerage fees for the refund
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
     Money net_amount_in_receivable_currency?;
     Money total_refunded_amount?;
@@ -567,10 +591,13 @@
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
 
@@ -635,14 +662,17 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
+    @constraint:String {maxLength: 127}
     string invoice_id?;
     # Indicates whether you can make additional captures against the authorized payment. Set to `true` if you do not intend to capture additional payments against the authorization. Set to `false` if you intend to capture additional payments against the authorization.
     boolean final_capture?;
     # Any additional payment instructions to be consider during payment processing. This processing instruction is applicable for Capturing an order or Authorizing an Order
     PaymentInstruction payment_instruction?;
     # An informational note about this settlement. Appears in both the payer's transaction history and the emails that the payer receives.
+    @constraint:String {maxLength: 255}
     string note_to_payer?;
     # The payment descriptor on the payer's account statement.
+    @constraint:String {maxLength: 22}
     string soft_descriptor?;
 };
 
@@ -652,10 +682,13 @@
     # The currency and amount for a financial transaction, such as a balance or payment due
     Money amount?;
     # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.*$`}
     string custom_id?;
     # The API caller-provided external invoice ID for this order. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 127, minLength: 1, pattern: re `^.*$`}
     string invoice_id?;
     # The reason for the refund. Appears in both the payer's transaction history and the emails that the payer receives. The pattern is defined by an external party and supports Unicode
+    @constraint:String {maxLength: 255, minLength: 1, pattern: re `^.*$`}
     string note_to_payer?;
     PaymentInstruction2 payment_instruction?;
 };
@@ -664,6 +697,7 @@
 
 type PaymentInstruction2 record {
     # Specifies the amount that the API caller will contribute to the refund being processed. The amount needs to be lower than platform_fees amount originally captured or the amount that is remaining if multiple refunds have been processed. This field is only applicable to merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability
+    @constraint:Array {maxLength: 1}
     PlatformFee[] platform_fees?;
 };
 
`````

# guidewire.insnow — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `guidewire.insnow` |
| **Old file** | `guidewire.insnow/old/ballerinax_guidewire.insnow.bal.txt` |
| **New file** | `guidewire.insnow/new/ballerinax_guidewire.insnow.bal.txt` |
| **Old lines** | 2237 |
| **New lines** | 2249 |
| **Lines added** | 20 |
| **Lines removed** | 8 |
| **Hunks** | 15 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 127–132 | 127–133 | Types | +1 | −0 |
| 2 | 146–151 | 147–153 | Types | +1 | −0 |
| 3 | 1206–1211 | 1208–1214 | Types | +1 | −0 |
| 4 | 1300–1305 | 1303–1309 | Types | +1 | −0 |
| 5 | 1310–1315 | 1314–1320 | Types | +1 | −0 |
| 6 | 1484–1489 | 1489–1495 | Types | +1 | −0 |
| 7 | 1530–1535 | 1536–1542 | Types | +1 | −0 |
| 8 | 1624–1629 | 1631–1637 | Types | +1 | −0 |
| 9 | 1722–1729 | 1730–1739 | Types | +2 | −0 |
| 10 | 2025–2036 | 2035–2048 | Types | +2 | −0 |
| 11 | 2129–2135 | 2141–2147 | Client | +1 | −1 |
| 12 | 2137–2143 | 2149–2155 | Client | +1 | −1 |
| 13 | 2145–2159 | 2157–2171 | Client | +3 | −3 |
| 14 | 2185–2191 | 2197–2203 | Client | +1 | −1 |
| 15 | 2225–2235 | 2237–2247 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- guidewire.insnow/old/ballerinax_guidewire.insnow.bal.txt	2026-08-12 12:57:30
+++ guidewire.insnow/new/ballerinax_guidewire.insnow.bal.txt	2026-08-12 13:19:19
@@ -127,6 +127,7 @@
     # A general reference identifier for the policy item, usable for cross-referencing or linkage
     string ref?;
     # Hypermedia links associated with the policy item, providing navigational URLs to related resources
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # Captures essential identification and reference information for a customer, supporting customer management, service, and correspondence within the insurance system
     CustomerInfo customerInfo?;
@@ -146,6 +147,7 @@
     # Reference to the statement account related to the policy, used for financial transactions and billing
     string statementAccountRef?;
     # A collection of hypermedia links to related resources, facilitating navigation and further actions
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # Version identifier for the policy information, denoting the format or structure level of the policy data
     string version?;
@@ -1206,6 +1208,7 @@
 
 type Document record {
     # Hypermedia links related to the document, providing navigational paths to related data and actions available for the document
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # Identifier of the user who added the document, useful for audit trails and permissions management
     string addUser?;
@@ -1300,6 +1303,7 @@
     # List of additional insured entities for workers' compensation policies, detailing parties other than the primary insured that receive coverage
     WCAdditionalInsured[] wcAdditionalInsureds?;
     # The revision identifier of the policy, used for tracking changes and ensuring data consistency
+    @jsondata:Name {value: "_revision"}
     string revision?;
     # A counter indicating the number of times the policy has been updated
     int updateCount?;
@@ -1310,6 +1314,7 @@
     # Reference identifier for the account associated with billing statements for the policy
     string statementAccountRef?;
     # Hypermedia links associated with the policy item, providing navigational URLs to related resources
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # A list of states in which workers' compensation coverage is included within the policy as proposed by this quote, reflecting multi-state operations and compliance
     WCCoveredState[] wcCoveredStates?;
@@ -1484,6 +1489,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|http:CredentialsConfig auth; // Special Agent Note: BearerTokenConfig, CredentialsConfig FROM ballerina/http package
@@ -1530,6 +1536,7 @@
 
 type ApplicationMini record {
     # A collection of hypermedia links to related resources, enabling easy navigation to detailed views of the application, policy information, and other associated resources
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # The unique identifier assigned to the application, serving as a primary reference for tracking and management throughout the application process
     string applicationNumber?;
@@ -1624,6 +1631,7 @@
     # A unique reference identifier for the application, used within the system for tracking, management, and retrieval purposes
     string ref?;
     # Hypermedia links related to the application, facilitating navigation to related resources and actions such as editing or inquiry
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # Indicates whether the current user is permitted to make inquiries regarding the application, typically used for customer service and support roles
     boolean canInquiry?;
@@ -1722,8 +1730,10 @@
     # An array of Address objects that detail the driver's associated addresses, including home, mailing, and potentially other types of addresses
     Address[] addresses?;
     # A versioning identifier used to manage concurrent updates to the driver resource, ensuring data integrity through optimistic locking mechanisms
+    @jsondata:Name {value: "_revision"}
     string revision?;
     # A collection of hypermedia links related to the driver, providing quick access to related resources and actions such as fetching detailed information or initiating workflows
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # Contains details regarding the erasure of data, including who performed the erasure, when it was done, and the specific item erased, ensuring compliance with data protection and privacy regulations
     EraseInfo eraseInfo?;
@@ -2025,12 +2035,14 @@
     # List of additional insured entities for workers' compensation policies, detailing parties other than the primary insured that receive coverage
     WCAdditionalInsured[] wcAdditionalInsureds?;
     # A system-generated version identifier for the quote, used to manage updates and ensure data integrity through optimistic concurrency control
+    @jsondata:Name {value: "_revision"}
     string revision?;
     # Represents an insured entity or individual within the system, encompassing both basic identification and specific insurance-related information
     Insured insured?;
     # A reference to the statement account associated with this quote, used for billing and financial transactions related to the policy
     string statementAccountRef?;
     # A collection of hypermedia links to related resources and actions available for the quote, facilitating easy navigation and interaction within the API ecosystem
+    @jsondata:Name {value: "_links"}
     Link[] links?;
     # A list of states in which workers' compensation coverage is included within the policy as proposed by this quote, reflecting multi-state operations and compliance
     WCCoveredState[] wcCoveredStates?;
@@ -2129,7 +2141,7 @@
 
     # Returns a list of supported countries.
     # 
-    resource function get addresses/countries(map<string|string[]> headers = {}, "asc"|"desc" sortType = "asc", anydata Additional Values, GetSupportedCountriesQueries queries) returns ListCountry|error;
+    resource function get addresses/countries(map<string|string[]> headers = {}, "asc"|"desc" sortType = "asc", GetSupportedCountriesQueries queries) returns ListCountry|error;
 
     # Returns the AddressCountryTemplate bean for the given IsoCd (e.g. US).
     # 
@@ -2137,7 +2149,7 @@
 
     # Fills an address from a Google Places search. Using the placeId from a Google Places search, an address will be returned that has all of the address components filled. If the placeId is not known, Google Places will be called to search and fill the address components.
     # 
-    resource function get addresses/googlePlacesFill(map<string|string[]> headers = {}, string placeId = "", string addressLine = "", anydata Additional Values, FillAddressFromGooglePlacesQueries queries) returns Address|error;
+    resource function get addresses/googlePlacesFill(map<string|string[]> headers = {}, string placeId = "", string addressLine = "", FillAddressFromGooglePlacesQueries queries) returns Address|error;
 
     # Indicates whether a given address is already verified.
     # 
@@ -2145,15 +2157,15 @@
 
     # Normalizes, verifies, and provides a more complete address. The verified address may include additional address properties. The response either returns one or more addresses that match the given address, or it will return an error if the address cannot be verified. If more than one address is returned, select an address and then resubmit the API request to perform address verification on the selected address.
     # 
-    resource function post addresses/verificationRequest(ListAddress payload, map<string|string[]> headers = {}, "Combined"|"Uncombined" addressType = "Combined", anydata Additional Values, VerifyAddressQueries queries) returns error?;
+    resource function post addresses/verificationRequest(ListAddress payload, map<string|string[]> headers = {}, "Combined"|"Uncombined" addressType = "Combined", VerifyAddressQueries queries) returns error?;
 
     # Returns a list of quotes or applications.
     # 
-    resource function get applications(map<string|string[]> headers = {}, string createdSinceDate = "", string applicationOrQuoteNumber = "", string transactionCd = "", boolean includeDeleted = false, string type = "", boolean recentlyViewed = false, string policyId = "", string providerId = "", string continuationId = "", string transactionCdGroup = "", string customerId = "", boolean includeClosed = false, string limit = "", string optionalFields = "", string status = "", anydata Additional Values, GetQuotesQueries queries) returns ListApplication|error;
+    resource function get applications(map<string|string[]> headers = {}, string createdSinceDate = "", string applicationOrQuoteNumber = "", string transactionCd = "", boolean includeDeleted = false, string type = "", boolean recentlyViewed = false, string policyId = "", string providerId = "", string continuationId = "", string transactionCdGroup = "", string customerId = "", boolean includeClosed = false, string limit = "", string optionalFields = "", string status = "", GetQuotesQueries queries) returns ListApplication|error;
 
     # Starts a new QuickQuote or Quote. To create a QuickQuote, basicPolicy productVersionIdRef (e.g. Homeowners-1.00.00), providerRef (e.g. 19), and effectiveDt strings are required. To create a Quote, basicPolicy productVersionIdRef, providerRef, and effectiveDt strings, plus one piece of insured information to create a customer, are required.
     # 
-    resource function post applications(Quote payload, map<string|string[]> headers = {}, string requestedTypeCd = "", anydata Additional Values, CreateQuoteQueries queries) returns error?;
+    resource function post applications(Quote payload, map<string|string[]> headers = {}, string requestedTypeCd = "", CreateQuoteQueries queries) returns error?;
 
     # Delete the quote or application.
     # 
@@ -2185,7 +2197,7 @@
 
     # Returns a list of the drivers or non-drivers of a quote or application.
     # 
-    resource function get applications/[string systemId]/drivers(map<string|string[]> headers = {}, "Driver"|"NonDriver" typeCd = "Driver", string continuationId = "", string limit = "", boolean includeDeleted = false, anydata Additional Values, GetDriversQueries queries) returns ListDriver|error;
+    resource function get applications/[string systemId]/drivers(map<string|string[]> headers = {}, "Driver"|"NonDriver" typeCd = "Driver", string continuationId = "", string limit = "", boolean includeDeleted = false, GetDriversQueries queries) returns ListDriver|error;
 
     # Creates a new driver or non-driver. You must include a partyTypeCd (DriverParty or NonDriverParty). Other details may be required depending on the insurance product being quoted.
     # 
@@ -2225,11 +2237,11 @@
 
     # Returns a list of policies.
     # 
-    resource function get policies(map<string|string[]> headers = {}, boolean recentlyViewed = false, string providerRef = "", string createdSinceDate = "", string continuationId = "", string customerId = "", string limit = "", string policyNumber = "", string expiredDateAfter = "", boolean includePriorTerms = false, string optionalFields = "", string status = "", anydata Additional Values, GetPoliciesQueries queries) returns ListPolicy|error;
+    resource function get policies(map<string|string[]> headers = {}, boolean recentlyViewed = false, string providerRef = "", string createdSinceDate = "", string continuationId = "", string customerId = "", string limit = "", string policyNumber = "", string expiredDateAfter = "", boolean includePriorTerms = false, string optionalFields = "", string status = "", GetPoliciesQueries queries) returns ListPolicy|error;
 
     # Returns the full details of a policy.
     # 
-    resource function get policies/[string systemId](map<string|string[]> headers = {}, string asOfDate = "", anydata Additional Values, GetPolicyQueries queries) returns PolicyDetails|error;
+    resource function get policies/[string systemId](map<string|string[]> headers = {}, string asOfDate = "", GetPolicyQueries queries) returns PolicyDetails|error;
 
     # Updates the preferred delivery method and insured email address of the policy. Requires the systemId.
     # 
`````

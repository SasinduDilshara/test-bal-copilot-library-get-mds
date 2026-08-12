# aws.marketplace.mpe — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.marketplace.mpe` |
| **Old file** | `aws.marketplace.mpe/old/ballerinax_aws.marketplace.mpe.bal.txt` |
| **New file** | `aws.marketplace.mpe/new/ballerinax_aws.marketplace.mpe.bal.txt` |
| **Old lines** | 221 |
| **New lines** | 226 |
| **Lines added** | 9 |
| **Lines removed** | 4 |
| **Hunks** | 6 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 134–140 | 134–141 | END README | +2 | −1 |
| 2 | 146–152 | 147–153 | Types | +1 | −1 |
| 3 | 156–167 | 157–170 | Types | +2 | −0 |
| 4 | 169–176 | 172–181 | Types | +2 | −0 |
| 5 | 203–209 | 208–214 | Client | +1 | −1 |
| 6 | 217–221 | 222–226 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.marketplace.mpe/old/ballerinax_aws.marketplace.mpe.bal.txt	2026-08-12 12:57:30
+++ aws.marketplace.mpe/new/ballerinax_aws.marketplace.mpe.bal.txt	2026-08-12 13:19:19
@@ -134,7 +134,8 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents an AWS Marketplace Entitlement distinct error.
+type Error error<aws:ErrorDetails>;
 
 # Represents the connection configuration for the AWS Marketplace Entitlement service client.
 
@@ -146,7 +147,7 @@
     auth:AuthConfig auth; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package
     # AWS region: an `aws:Region` enum member or a plain region
 string (e.g., `"us-east-1"`) for regions not yet in the enum
-    ballerinax/aws:1.0.1:Region|string region;
+    aws:Region|string region;
     # Optional endpoint options: FIPS/dualstack variants, or a custom
 endpoint override (e.g. LocalStack, VPC interface endpoints)
     aws:EndpointConfig endpoint?; // Special Agent Note: EndpointConfig FROM ballerinax/aws package
@@ -156,12 +157,14 @@
 
 type EntitlementsRequest record {
     # Product code is used to uniquely identify a product in AWS Marketplace
+    @constraint:String { minLength: 1, maxLength: 255 }
     string productCode;
     # A parameter which is used to filter out entitlements for a specific customer or a specific dimension
     EntitlementFilter filter?;
     # The maximum number of results to return in a single call
     int maxResults?;
     # The token for pagination to retrieve the next set of results
+    @constraint:String { pattern: re `\S+` }
     string nextToken?;
 };
 
@@ -169,8 +172,10 @@
 
 type EntitlementFilter record {
     # Customer identifier based filter
+    @constraint:Array { minLength: 1 }
     string[] customerIdentifier?;
     # Product dimension based filter
+    @constraint:Array { minLength: 1 }
     string[] dimension?;
 };
 
@@ -203,7 +208,7 @@
 
 # AWS Marketplace Entitlement service client.
 client class Client {
-    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig configs) returns ballerinax/aws.marketplace.mpe:1.0.0:Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
+    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig configs) returns Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
 
     # Retrieves the entitlement values for a given product.
     # ```ballerina
@@ -217,5 +222,5 @@
     # check mpe.close();
     # ```
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
`````

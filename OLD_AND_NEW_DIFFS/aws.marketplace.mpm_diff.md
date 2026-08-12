# aws.marketplace.mpm — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.marketplace.mpm` |
| **Old file** | `aws.marketplace.mpm/old/ballerinax_aws.marketplace.mpm.bal.txt` |
| **New file** | `aws.marketplace.mpm/new/ballerinax_aws.marketplace.mpm.bal.txt` |
| **Old lines** | 295 |
| **New lines** | 307 |
| **Lines added** | 16 |
| **Lines removed** | 4 |
| **Hunks** | 8 |

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
| 1 | 166–172 | 166–173 | Types | +2 | −1 |
| 2 | 178–184 | 179–185 | Types | +1 | −1 |
| 3 | 199–206 | 200–209 | Types | +2 | −0 |
| 4 | 208–223 | 211–231 | Types | +5 | −0 |
| 5 | 225–232 | 233–242 | Types | +2 | −0 |
| 6 | 234–241 | 244–253 | Types | +2 | −0 |
| 7 | 270–276 | 282–288 | Client | +1 | −1 |
| 8 | 291–295 | 303–307 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.marketplace.mpm/old/ballerinax_aws.marketplace.mpm.bal.txt	2026-08-12 12:57:30
+++ aws.marketplace.mpm/new/ballerinax_aws.marketplace.mpm.bal.txt	2026-08-12 13:19:19
@@ -166,7 +166,8 @@
 # The provided `UsageRecord` matches a previously metered `UsageRecord` in terms of customer, dimension, and time
 const string DUPLICATE_RECORD = "DuplicateRecord";
 
-// Unknown type: Error
+# Represents a AWS Marketplace Metering distinct error.
+type Error error<aws:ErrorDetails>;
 
 # Represents the connection configuration for the AWS Marketplace Metering service client.
 
@@ -178,7 +179,7 @@
     auth:AuthConfig auth; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package
     # AWS region: an `aws:Region` enum member or a plain region
 string (e.g., `"us-east-1"`) for regions not yet in the enum
-    ballerinax/aws:1.0.1:Region|string region;
+    aws:Region|string region;
     # Optional endpoint options: FIPS/dualstack variants, or a custom
 endpoint override (e.g. LocalStack, VPC interface endpoints)
     aws:EndpointConfig endpoint?; // Special Agent Note: EndpointConfig FROM ballerinax/aws package
@@ -199,8 +200,10 @@
 
 type BatchMeterUsageRequest record {
     # The unique identifier for the Marketplace product
+    @constraint:String { pattern: re `^[-a-zA-Z0-9/=:_.@]{1,255}$` }
     string productCode;
     # The set of usage records. Each usage record provides information about an instance of product usage. 
+    @constraint:Array { maxLength: 25 }
     UsageRecord[] usageRecords?;
 };
 
@@ -208,16 +211,21 @@
 
 type UsageRecord record {
     # The unique identifier used to identify an individual customer
+    @constraint:String { pattern: re `[\s\S]{1,255}$` }
     string customerIdentifier?;
     # The AWS account ID of the buyer
+    @constraint:String { pattern: re `^[0-9]{1,255}$` }
     string customerAWSAccountId?;
     # The dimension for which the usage is being reported
+    @constraint:String { pattern: re `[\s\S]{1,255}$` }
     string dimension;
     # The timestamp when the usage occurred (in UTC)
     time:Utc timestamp; // Special Agent Note: Utc FROM ballerina/time package
     # The quantity of usage consumed
+    @constraint:Int { minValue: 0, maxValue: 2147483647 }
     int quantity?;
     # The list of usage allocations
+    @constraint:Array { minLength: 1, maxLength: 2500 }
     UsageAllocation[] usageAllocations?;
 };
 
@@ -225,8 +233,10 @@
 
 type UsageAllocation record {
     # The total quantity allocated to this bucket of usage
+    @constraint:Int { minValue: 0, maxValue: 2147483647 }
     int allocatedUsageQuantity;
     # The set of tags that define the bucket of usage
+    @constraint:Array { minLength: 1, maxLength: 5 }
     Tag[] tags?;
 };
 
@@ -234,8 +244,10 @@
 
 type Tag record {
     # The label that acts as the category for the specific tag values
+    @constraint:String { pattern: re `^[a-zA-Z0-9+ -=._:/@]{1,100}$` }
     string 'key;
     # The descriptor within a tag category (key)
+    @constraint:String { pattern: re `^[a-zA-Z0-9+ -=._:/@]{1,256}$` }
     string value;
 };
 
@@ -270,7 +282,7 @@
 
 # AWS Marketplace metering client.
 client class Client {
-    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig configs) returns ballerinax/aws.marketplace.mpm:1.0.0:Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
+    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig configs) returns Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
 
     # Retrieves customer details mapped to a registration token.
     # ```ballerina
@@ -291,5 +303,5 @@
     # check mpm.close();
     # ```
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
`````

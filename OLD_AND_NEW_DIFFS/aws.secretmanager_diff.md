# aws.secretmanager — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.secretmanager` |
| **Old file** | `aws.secretmanager/old/ballerinax_aws.secretmanager.bal.txt` |
| **New file** | `aws.secretmanager/new/ballerinax_aws.secretmanager.bal.txt` |
| **Old lines** | 459 |
| **New lines** | 471 |
| **Lines added** | 17 |
| **Lines removed** | 5 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (3)

- `type Error`
- `type FilterValue`
- `type SecretId`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 186–192 | 186–193 | Types | +2 | −1 |
| 2 | 255–261 | 256–264 | Types | +3 | −1 |
| 3 | 295–301 | 298–304 | Types | +1 | −1 |
| 4 | 344–351 | 347–356 | Types | +2 | −0 |
| 5 | 370–384 | 375–393 | Types | +4 | −0 |
| 6 | 388–400 | 397–412 | Types | +4 | −1 |
| 7 | 425–431 | 437–443 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.secretmanager/old/ballerinax_aws.secretmanager.bal.txt	2026-08-12 12:57:30
+++ aws.secretmanager/new/ballerinax_aws.secretmanager.bal.txt	2026-08-12 13:19:19
@@ -186,7 +186,8 @@
     string errorMessage?;
 };
 
-// Unknown type: Error
+# Represents a AWS Secret Manager distinct error.
+type Error error<ErrorDetails>;
 
 # Represents the Client configurations for AWS Secret Manager service.
 
@@ -255,7 +256,9 @@
     string sessionToken?;
 };
 
-// Unknown type: SecretId
+# The ARN or name of the secret.
+@constraint:String { minLength: { value: 1, message: "SecretId must contain at least 1 character" }, maxLength: { value: 2048, message: "SecretId cannot exceed 2048 characters" } }
+type SecretId string;
 
 # Represents the results retrieved from `GetEntitlements` operation.
 
@@ -295,7 +298,7 @@
     # The list of tags attached to the secret
     Tag[] tags?;
     # A list of the versions of the secret that have staging labels attached
-    map<ballerinax/aws.secretmanager:0.4.1:StagingStatus[]> versionToStages?;
+    map<StagingStatus[]> versionToStages?;
 };
 
 # Represents the replication status of a secret in AWS Secrets Manager.
@@ -344,8 +347,10 @@
 
 type SecretVersionSelector record {
     # The unique identifier of the version of the secret
+    @constraint:String { minLength: { value: 32, message: "VersionId must be at least 32 characters long" }, maxLength: { value: 64, message: "VersionId cannot exceed 64 characters" } }
     string versionId?;
     # The staging label of the version of the secret
+    @constraint:String { minLength: { value: 1, message: "VersionStage must contain at least 1 character" }, maxLength: { value: 256, message: "VersionStage cannot exceed 256 characters" } }
     string versionStage?;
 };
 
@@ -370,15 +375,19 @@
 
 type BatchGetSecretValueRequest record {
     # The filters to choose which secrets to retrieve
+    @constraint:Array { maxLength: { value: 10, message: "Can only have maximum 10 filters per request" } }
     SecretValueFilter[] filters?;
     # The number of results to include in the response. If there are more results available, 
 in the response, Secrets Manager includes `nextToken`. To use this parameter, 
 you must also use the `filters` parameter
+    @constraint:Int { minValue: { value: 1, message: "MaxResults must be at least 1" }, maxValue: { value: 20, message: "MaxResults cannot exceed 20" } }
     int maxResults?;
     # A token that indicates where the output should continue from, 
 if a previous call did not show all results
+    @constraint:String { minLength: { value: 1, message: "NextToken must contain at least 1 character" }, maxLength: { value: 4096, message: "NextToken cannot exceed 4096 characters" } }
     string nextToken?;
     # The ARN or names of the secrets to retrieve. You must include `filters` or `secretIds`, but not both
+    @constraint:Array { minLength: { value: 1, message: "Should have atleast 1 secretId per request" }, maxLength: { value: 20, message: "Can only have maximum 20 secretIds per request" } }
     SecretId[] secretIds?;
 };
 
@@ -388,13 +397,16 @@
     # The key used to filter secrets
     FilterKey 'key?;
     # A list of values associated with the filter key
+    @constraint:Array { minLength: { value: 1, message: "The `values` must contain at least 1 element" }, maxLength: { value: 10, message: "The `values` cannot contain more than 10 elements" } }
     FilterValue[] values?;
 };
 
 # The allowed filter keys for `SecretValueFilter`.
 type FilterKey "description"|"name"|"tag-key"|"tag-value"|"primary-region"|"owning-service"|"all";
 
-// Unknown type: FilterValue
+# Represents a value used in the filter criteria for a `SecretValueFilter`.
+@constraint:String { pattern: { value: re `^!?[a-zA-Z0-9 :_@/+=.\-!]{0,512}$`, message: "Invalid filter value format" } }
+type FilterValue string;
 
 # Represents the response returned by the `batchGetSecretValue` API of the AWS Secrets Manager connector.
 
@@ -425,7 +437,7 @@
 
 # AWS Secret Manager client.
 client class Client {
-    function init(Region region = "us-west-2", StaticAuthConfig|"EC2_IAM_ROLE"|"DEFAULT_CREDENTIALS" auth = {accessKeyId: "", secretAccessKey: ""}, ConnectionConfig configs) returns ballerinax/aws.secretmanager:0.4.1:Error?;
+    function init(Region region = "us-west-2", StaticAuthConfig|"EC2_IAM_ROLE"|"DEFAULT_CREDENTIALS" auth = {accessKeyId: "", secretAccessKey: ""}, ConnectionConfig configs) returns Error?;
 
     # Retrieves the details of a secret. It does not include the encrypted secret value. 
     # Secrets Manager only returns fields that have a value in the response. 
`````

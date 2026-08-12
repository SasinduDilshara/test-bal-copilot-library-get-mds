# aws.sqs — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.sqs` |
| **Old file** | `aws.sqs/old/ballerinax_aws.sqs.bal.txt` |
| **New file** | `aws.sqs/new/ballerinax_aws.sqs.bal.txt` |
| **Old lines** | 885 |
| **New lines** | 911 |
| **Lines added** | 34 |
| **Lines removed** | 8 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 5 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (8)

- `annotation ServiceConfig`
- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 320–326 | 320–329 | Types | +4 | −1 |
| 2 | 333–339 | 336–342 | Types | +1 | −1 |
| 3 | 362–368 | 365–371 | Types | +1 | −1 |
| 4 | 429–435 | 432–438 | Types | +1 | −1 |
| 5 | 469–475 | 472–478 | Types | +1 | −1 |
| 6 | 773–785 | 776–806 | Types | +20 | −2 |
| 7 | 792–798 | 813–819 | Client | +1 | −1 |
| 8 | 883–885 | 904–911 | Client | +5 | −0 |

---

## Unified diff

`````diff
--- aws.sqs/old/ballerinax_aws.sqs.bal.txt	2026-08-12 12:57:30
+++ aws.sqs/new/ballerinax_aws.sqs.bal.txt	2026-08-12 13:19:19
@@ -320,7 +320,10 @@
 
 const string REDRIVE_ALLOW_POLICY = "RedriveAllowPolicy";
 
-// Unknown type: Error
+# Represents a AWS SQS distinct error. The fields of `aws:ErrorDetails` are populated
+# when the failure originates from an AWS SQS service call, and are left unset when the
+# failure occurs before a response is received (e.g. an invalid configuration).
+type Error error<aws:ErrorDetails>;
 
 # Represents the connection configuration for the Amazon SQS client.
 # 
@@ -333,7 +336,7 @@
     auth:AuthConfig auth; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package
     # AWS region: an `aws:Region` enum member or a plain region
 string (e.g., `"us-east-1"`) for regions not yet in the enum
-    ballerinax/aws:1.0.1:Region|string region;
+    aws:Region|string region;
     # Optional endpoint options: FIPS/dualstack variants, or a custom
 endpoint override (e.g. LocalStack, VPC interface endpoints)
     aws:EndpointConfig endpoint?; // Special Agent Note: EndpointConfig FROM ballerinax/aws package
@@ -362,7 +365,7 @@
     # Duration to delay the message, in seconds (0 to 900)
     int delaySeconds?;
     # Custom attributes to attach to the message
-    map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue> messageAttributes?;
+    map<MessageAttributeValue> messageAttributes?;
     # X-Ray tracing header for distributed tracing support
     string awsTraceHeader?;
     # Token for deduplicating messages (FIFO only)
@@ -429,7 +432,7 @@
     # MD5 digest of the non-URL-encoded attribute string
     string md5OfMessageAttributes?;
     # User-defined attributes attached to the message
-    map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue> messageAttributes?;
+    map<MessageAttributeValue> messageAttributes?;
     # Unique ID assigned to the message
     string messageId?;
     # Token required to delete or change visibility of the message
@@ -469,7 +472,7 @@
     # The body of the message
     string body;
     int delaySeconds?;
-    map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue> messageAttributes?;
+    map<MessageAttributeValue> messageAttributes?;
     string awsTraceHeader?;
     string messageDeduplicationId?;
     string messageGroupId?;
@@ -773,13 +776,31 @@
     boolean autoDelete?;
 };
 
-// Unknown type: Listener
+# Initializes the AWS SQS listener.
+# 
+class Listener {
+    function init(ConnectionConfig connectionConfig, PollingConfig pollingConfig = {}) returns Error?;
+
+    # Attaches an SQS service to the SQS listener.
+    function attach(Service s, () path = ()) returns Error|();
+
+    # Detaches an SQS service from the SQS listener.
+    function detach(Service s) returns Error|();
 
+    # Starts the SQS listener.
+    function 'start() returns Error|();
+
+    # Gracefully stops the SQS listener.
+    function gracefulStop() returns Error|();
+
+    # Immediately stops the SQS listener.
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Provides control over message deletion from the queue after processing.
 client class Caller {
-    function init() returns sqs:sqs:Caller;
 
     # Delete the message from the queue after successful processing.
     # 
@@ -792,7 +813,7 @@
 # Supports static credentials, profile-based credentials, and the default AWS credential
 # provider chain (environment variables, ECS container credentials, EC2 instance profiles, etc.).
 client class Client {
-    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig connectionConfig) returns ballerinax/aws.sqs:5.0.0:Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
+    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig connectionConfig) returns Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
 
     # Delivers a message to the specified SQS queue.
     # 
@@ -883,3 +904,8 @@
     # 
     remote function close() returns Error|();
 }
+
+// --- Annotations ---
+
+# Annotation to configure the `sqs:Service`.
+public annotation ServiceConfigType ServiceConfig on service;
`````

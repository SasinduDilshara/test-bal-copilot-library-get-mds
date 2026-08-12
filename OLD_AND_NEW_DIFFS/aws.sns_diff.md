# aws.sns — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.sns` |
| **Old file** | `aws.sns/old/ballerinax_aws.sns.bal.txt` |
| **New file** | `aws.sns/new/ballerinax_aws.sns.bal.txt` |
| **Old lines** | 1237 |
| **New lines** | 1245 |
| **Lines added** | 28 |
| **Lines removed** | 20 |
| **Hunks** | 14 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 6 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `type CalculateSignatureFailedError`
- `type Error`
- `type GenerateRequestFailed`
- `type InternalError`
- `type OperationError`
- `type ResponseHandleFailedError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 334–350 | 334–356 | Types | +13 | −7 |
| 2 | 818–830 | 824–836 | Types | +2 | −2 |
| 3 | 835–841 | 841–847 | Types | +1 | −1 |
| 4 | 980–985 | 986–992 | Types | +1 | −0 |
| 5 | 988–994 | 995–1001 | Types | +1 | −1 |
| 6 | 1036–1041 | 1043–1049 | Client | +1 | −0 |
| 7 | 1052–1058 | 1060–1066 | Client | +1 | −1 |
| 8 | 1082–1088 | 1090–1096 | Client | +1 | −1 |
| 9 | 1116–1122 | 1124–1130 | Client | +1 | −1 |
| 10 | 1138–1144 | 1146–1152 | Client | +1 | −1 |
| 11 | 1164–1170 | 1172–1178 | Client | +1 | −1 |
| 12 | 1176–1186 | 1184–1194 | Client | +2 | −2 |
| 13 | 1194–1200 | 1202–1208 | Client | +1 | −1 |
| 14 | 1233–1237 | 1241–1245 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.sns/old/ballerinax_aws.sns.bal.txt	2026-08-12 12:57:30
+++ aws.sns/new/ballerinax_aws.sns.bal.txt	2026-08-12 13:19:19
@@ -334,17 +334,23 @@
 
 const string PREMIUM = "Premium";
 
-// Unknown type: Error
-
-// Unknown type: GenerateRequestFailed
+# Reperesents the generic error type for the `aws.sns` module.
+type Error error;
 
-// Unknown type: OperationError
+# Represents an error that occurs when generating an API request.
+type GenerateRequestFailed error;
 
-// Unknown type: ResponseHandleFailedError
+# Represents an error that occurs when the API action cannot be completed due to user error.
+type OperationError error;
 
-// Unknown type: CalculateSignatureFailedError
+# Represents an error that occurs when the API response is in an unexpected format.
+type ResponseHandleFailedError error;
 
-// Unknown type: InternalError
+# Represents an error that occurs when calculating the signature.
+type CalculateSignatureFailedError error;
+
+# Represents an error that occurs when the API action cannot be completed due to an unknown server error.
+type InternalError error;
 
 
 type ListTopicsResponse record {
@@ -818,13 +824,13 @@
 # Represents a message that is published to an Amazon SNS topic. If you are publishing to a topic and you want to send
 # the same message to all transport protocols, include the text of the message as a `string` value. If you want to send
 # different messages for each transport protocol use a `MessageRecord` value. 
-type Message string|ballerinax/aws.sns:4.0.1:MessageRecord;
+type Message string|MessageRecord;
 
 # Represents an element of the String.Array type of a message attribute value.
 type StringArrayElement string|int|float|decimal|boolean|();
 
 # Represents an attribute value of a message.
-type MessageAttributeValue string|ballerinax/aws.sns:4.0.1:StringArrayElement[]|int|float|decimal|byte[];
+type MessageAttributeValue string|StringArrayElement[]|int|float|decimal|byte[];
 
 # Represents the details of a single message in a publish batch request.
 # 
@@ -835,7 +841,7 @@
     # The message to send
     Message message;
     # The attributes of the message
-    map<ballerinax/aws.sns:4.0.1:MessageAttributeValue> attributes?;
+    map<MessageAttributeValue> attributes?;
     # Every message must have a unique `deduplicationId`, which is a token used for deduplication 
 of sent messages. If a message with a particular `deduplicationId` is sent successfully, any 
 message sent with the same `deduplicationId` during the 5-minute deduplication interval is 
@@ -980,6 +986,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Authentication configuration: any standard credential source supported by
 AWS — static credentials, an AWS profile, STS assume-role,
@@ -988,7 +995,7 @@
     auth:AuthConfig auth; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package
     # AWS region: an `aws:Region` enum member or a plain region
 string (e.g., `"us-east-1"`) for regions not yet in the enum
-    ballerinax/aws:1.0.1:Region|string region?;
+    aws:Region|string region?;
     # Optional endpoint options: FIPS/dualstack variants, or a custom
 endpoint override (e.g. LocalStack, VPC interface endpoints)
     aws:EndpointConfig endpoint?; // Special Agent Note: EndpointConfig FROM ballerinax/aws package
@@ -1036,6 +1043,7 @@
 # Ballerina Amazon SNS API connector provides the capability to access Amazon's Simple Notification Service.
 # This connector allows you to create and manage SNS topics and subscriptions.
 # 
+@display {label: "Amazon SNS Client", iconPath: "icon.png"}
 client class Client {
     function init(ConnectionConfig config) returns error?;
 
@@ -1052,7 +1060,7 @@
 
     # Returns the topics ARNs that are owned by the AWS account.
     # 
-    remote function listTopics() returns Error?>;
+    remote function listTopics() returns stream<string, Error?>;
 
     # Retrieves an existing topic along with its attributes.
     # 
@@ -1082,7 +1090,7 @@
 
     # Retrieves the requester's subscriptions.
     # 
-    remote function listSubscriptions(string|() topicArn = ()) returns Error?>;
+    remote function listSubscriptions(string|() topicArn = ()) returns stream<Subscription, Error?>;
 
     # Retrieves the attributes of the requested subscription.
     # 
@@ -1116,7 +1124,7 @@
 
     # Retrives the platform application objects for the supported push notification services.
     # 
-    remote function listPlatformApplications() returns Error?>;
+    remote function listPlatformApplications() returns stream<PlatformApplication, Error?>;
 
     # Retrieves a platform application object for one of the supported push notification services.
     # 
@@ -1138,7 +1146,7 @@
 
     # Retrieves the endpoints associated with a specific platform application.
     # 
-    remote function listEndpoints(string platformApplicationArn) returns Error?>;
+    remote function listEndpoints(string platformApplicationArn) returns stream<Endpoint, Error?>;
 
     # Retrieves a platform application endpoint.
     # 
@@ -1164,7 +1172,7 @@
 
     # Retrieves the current verified and pending destination phone numbers in the SMS sandbox.
     # 
-    remote function listSMSSandboxPhoneNumbers() returns Error?>;
+    remote function listSMSSandboxPhoneNumbers() returns stream<SMSSandboxPhoneNumber, Error?>;
 
     # Deletes a verified or pending phone number from the SMS sandbox.
     # 
@@ -1176,11 +1184,11 @@
 
     # Retrieves the calling AWS account's dedicated origination numbers and their metadata. 
     # 
-    remote function listOriginationNumbers() returns Error?>;
+    remote function listOriginationNumbers() returns stream<OriginationPhoneNumber, Error?>;
 
     # Retrieves a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.
     # 
-    remote function listPhoneNumbersOptedOut() returns Error?>;
+    remote function listPhoneNumbersOptedOut() returns stream<string, Error?>;
 
     # Checks whether a phone number is opted out, meaning you cannot send SMS messages to it.
     # 
@@ -1194,7 +1202,7 @@
     # Adds tags to the specified Amazon SNS topic. A new tag with a key identical to that of an existing tag overwrites 
     # the existing tag.
     # 
-    remote function tagResource(string topicArn, string Additional Values, Tags tags) returns Error|();
+    remote function tagResource(string topicArn, Tags tags) returns Error|();
 
     # Lists the tags for the specified Amazon SNS topic.
     # 
@@ -1233,5 +1241,5 @@
     # refresh threads and any HTTP connections opened for STS/SSO). Call when the
     # client is no longer needed.
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
`````

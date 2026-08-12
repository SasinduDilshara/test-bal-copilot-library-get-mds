# aws.redshiftdata — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.redshiftdata` |
| **Old file** | `aws.redshiftdata/old/ballerinax_aws.redshiftdata.bal.txt` |
| **New file** | `aws.redshiftdata/new/ballerinax_aws.redshiftdata.bal.txt` |
| **Old lines** | 531 |
| **New lines** | 540 |
| **Lines added** | 15 |
| **Lines removed** | 6 |
| **Hunks** | 9 |

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
- `type SessionId`
- `type StatementId`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 275–281 | 275–282 | Types | +2 | −1 |
| 2 | 364–369 | 365–371 | Types | +1 | −0 |
| 3 | 372–377 | 374–380 | Types | +1 | −0 |
| 4 | 386–395 | 389–401 | Types | +4 | −1 |
| 5 | 401–406 | 407–413 | Types | +1 | −0 |
| 6 | 421–427 | 428–436 | Types | +3 | −1 |
| 7 | 476–482 | 485–491 | Types | +1 | −1 |
| 8 | 490–496 | 499–505 | Client | +1 | −1 |
| 9 | 513–519 | 522–528 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- aws.redshiftdata/old/ballerinax_aws.redshiftdata.bal.txt	2026-08-12 12:57:30
+++ aws.redshiftdata/new/ballerinax_aws.redshiftdata.bal.txt	2026-08-12 13:19:19
@@ -275,7 +275,8 @@
     string errorMessage?;
 };
 
-// Unknown type: Error
+# Represents a AWS Redshift Data distinct error.
+type Error error<ErrorDetails>;
 
 # Represents connection configurations related to Redshift Data API.
 # 
@@ -364,6 +365,7 @@
 
 type Cluster record {
     # The cluster identifier 
+    @constraint:String { minLength: { value: 1, message: "The cluster ID should be at least 1 character long" }, maxLength: { value: 63, message: "The cluster ID should be at most 63 characters long" } }
     string id;
     # The name of the database
     string database;
@@ -372,6 +374,7 @@
     # The name or ARN of the secret that enables access to the database
     string secretArn?;
     # The number of seconds to keep the session alive after the query finishes
+    @constraint:Int { minValue: { value: 0, message: "The sessionKeepAliveSeconds should be greater than or equal to 0" }, maxValue: { value: 86400, message: "The sessionKeepAliveSeconds should be less than or equal to 86400" } }
     int sessionKeepAliveSeconds?;
 };
 
@@ -386,10 +389,13 @@
     # The name or ARN of the secret that enables access to the database
     string secretArn?;
     # The number of seconds to keep the session alive after the query finishes
+    @constraint:Int { minValue: { value: 0, message: "The sessionKeepAliveSeconds should be greater than or equal to 0" }, maxValue: { value: 86400, message: "The sessionKeepAliveSeconds should be less than or equal to 86400" } }
     int sessionKeepAliveSeconds?;
 };
 
-// Unknown type: SessionId
+# The session identifier of the query.
+@constraint:String { pattern: { value: re `^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d+)?$`, message: "Invalid session ID format" } }
+type SessionId string;
 
 # Represents the configuration details required for `execute` method.
 # 
@@ -401,6 +407,7 @@
     # A unique, case-sensitive identifier that you provide to ensure the idempotency of the request 
     string clientToken?;
     # The name of the SQL statement
+    @constraint:String { minLength: { value: 1, message: "The statement name should be at least 1 character long" }, maxLength: { value: 500, message: "The statement name should be at most 500 characters long" } }
     string statementName?;
     # Flag which indicates to send an event after the SQL statement execution 
 to an event bus instance running in Amazon EventBridge
@@ -421,7 +428,9 @@
     SessionId sessionId?;
 };
 
-// Unknown type: StatementId
+# The identifier of the SQL statement
+@constraint:String { pattern: { message: "Invalid statement ID format", value: re `^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d+)?$` } }
+type StatementId string;
 
 # Information about an SQL statement.
 # 
@@ -476,7 +485,7 @@
     StatementId statementId;
     time:Utc createdAt; // Special Agent Note: Utc FROM ballerina/time package
     decimal duration;
-    string error?;
+    string 'error?;
     boolean hasResultSet;
     string queryString?;
     int redshiftQueryId;
@@ -490,7 +499,7 @@
 
 # The AWS Redshift Data API client.
 client class Client {
-    function init(Region region = "us-west-2", StaticAuthConfig|EC2IAMRoleConfig auth = {accessKeyId: "", secretAccessKey: ""}, Cluster|WorkGroup dbAccessConfig = {id: "", database: ""}, ConnectionConfig connectionConfig) returns ballerinax/aws.redshiftdata:1.1.0:Error?;
+    function init(Region region = "us-west-2", StaticAuthConfig|EC2IAMRoleConfig auth = {accessKeyId: "", secretAccessKey: ""}, Cluster|WorkGroup dbAccessConfig = {id: "", database: ""}, ConnectionConfig connectionConfig) returns Error?;
 
     # Runs an SQL statement, which can be data manipulation language (DML) or data definition language (DDL).
     # ```ballerina
@@ -513,7 +522,7 @@
     # stream<User, Error?> response = check redshift->getResultAsStream("<statement-id>");
     # ```
     # 
-    remote function getResultAsStream(StatementId statementId, record {|anydata...;|} rowTypes = record {|anydata...;|}) returns stream<rowTypes, ballerinax/aws.redshiftdata:1.1.0:Error?>|Error;
+    remote function getResultAsStream(StatementId statementId, record {|anydata...;|} rowTypes = record {|anydata...;|}) returns stream<rowTypes, Error?>|Error;
 
     # Retrieves the execution status for a previously executed SQL statement.
     # ```ballerina
`````

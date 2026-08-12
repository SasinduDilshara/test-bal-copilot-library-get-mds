# aws.s3 — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `aws.s3` |
| **Old file** | `aws.s3/old/ballerinax_aws.s3.bal.txt` |
| **New file** | `aws.s3/new/ballerinax_aws.s3.bal.txt` |
| **Old lines** | 650 |
| **New lines** | 677 |
| **Lines added** | 54 |
| **Lines removed** | 27 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 6 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `type BucketAlreadyExistsError`
- `type BucketAlreadyOwnedByYouError`
- `type BucketNotEmptyError`
- `type Error`
- `type NoSuchBucketError`
- `type NoSuchKeyError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 197–213 | 197–220 | Types | +13 | −6 |
| 2 | 215–221 | 222–228 | Types | +1 | −1 |
| 3 | 557–624 | 564–647 | Client | +31 | −15 |
| 4 | 630–650 | 653–677 | Client | +9 | −5 |

---

## Unified diff

`````diff
--- aws.s3/old/ballerinax_aws.s3.bal.txt	2026-08-12 12:57:30
+++ aws.s3/new/ballerinax_aws.s3.bal.txt	2026-08-12 13:19:19
@@ -197,17 +197,24 @@
 # HTTP PUT method
 const string PUT = "PUT";
 
-// Unknown type: Error
+# Represents the base error type for this module.
+# This is a distinct type to avoid mixing with generic `error` values.
+type Error error;
 
-// Unknown type: NoSuchKeyError
+# Represents an error when the specified key does not exist.
+type NoSuchKeyError error;
 
-// Unknown type: BucketAlreadyExistsError
+# Represents an error when trying to create a bucket that already exists.
+type BucketAlreadyExistsError error;
 
-// Unknown type: BucketAlreadyOwnedByYouError
+# Represents an error when the bucket already exists and is owned by you.
+type BucketAlreadyOwnedByYouError error;
 
-// Unknown type: NoSuchBucketError
+# Represents an error when the specified bucket does not exist.
+type NoSuchBucketError error;
 
-// Unknown type: BucketNotEmptyError
+# Represents an error when the bucket is not empty (for deletion).
+type BucketNotEmptyError error;
 
 # Configuration for the AWS S3 Client.
 
@@ -215,7 +222,7 @@
     # Authentication configuration
     auth:AuthConfig auth; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package
     # The AWS Region. If you don't specify an AWS region, Client uses US East (N. Virginia) as default region
-    ballerinax/aws:1.0.1:Region|string region?;
+    aws:Region|string region?;
     # Optional endpoint configuration for FIPS, dualstack, or custom endpoint overrides (e.g., LocalStack)
     aws:EndpointConfig endpoint?; // Special Agent Note: EndpointConfig FROM ballerinax/aws package
 };
@@ -557,68 +564,84 @@
 # Provides access to Amazon Simple Storage Service (S3) using the AWS SDK for Java V2.
 # Supports static credentials, profile-based credentials, and the default AWS credential
 # provider chain (environment variables, ECS container credentials, EC2 instance profiles, etc.).
+@display {label: "AWS S3 Client", iconPath: "icon.png"}
 client class Client {
-    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = aws:US_EAST_1, aws:EndpointConfig endpoint = {}, ConnectionConfig config) returns ballerinax/aws.s3:4.0.0:Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
+    function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|"us-west-1"|"us-isof-south-1"|"us-isof-east-1"|"us-isob-west-1"|"us-isob-east-1"|"us-iso-west-1"|"us-iso-east-1"|"us-gov-west-1"|"us-gov-east-1"|"us-east-2"|"us-east-1"|"sa-east-1"|"mx-central-1"|"me-south-1"|"me-central-1"|"il-central-1"|"eusc-de-east-1"|"eu-isoe-west-1"|"eu-west-3"|"eu-west-2"|"eu-west-1"|"eu-south-2"|"eu-south-1"|"eu-north-1"|"eu-central-2"|"eu-central-1"|"cn-northwest-1"|"cn-north-1"|"ca-west-1"|"ca-central-1"|"aws-iso-f-global"|"aws-iso-e-global"|"aws-iso-b-global"|"aws-iso-global"|"aws-us-gov-global"|"aws-cn-global"|"aws-global"|"ap-southeast-7"|"ap-southeast-6"|"ap-southeast-5"|"ap-southeast-4"|"ap-southeast-3"|"ap-southeast-2"|"ap-southeast-1"|"ap-south-2"|"ap-south-1"|"ap-northeast-3"|"ap-northeast-2"|"ap-northeast-1"|"ap-east-2"|"ap-east-1"|"af-south-1"|string region = aws:US_EAST_1, aws:EndpointConfig endpoint = {}, ConnectionConfig config) returns Error?; // Special Agent Note: AuthConfig FROM ballerinax/aws.auth package, EndpointConfig FROM ballerinax/aws package
 
     # Creates an S3 bucket.
     # 
-    remote function createBucket(string bucketName, CannedACL acl = "bucket-owner-full-control", ObjectOwnership objectOwnership = "BucketOwnerPreferred", boolean objectLockEnabled = false, CreateBucketConfig config) returns Error|();
+    @display {label: "Create Bucket"}
+    remote function createBucket(@display {label: "Bucket Name"} string bucketName, CannedACL acl = "bucket-owner-full-control", ObjectOwnership objectOwnership = "BucketOwnerPreferred", boolean objectLockEnabled = false, CreateBucketConfig config) returns Error|();
 
     # Deletes an S3 bucket.
     # 
-    remote function deleteBucket(string bucketName) returns Error|();
+    @display {label: "Delete Bucket"}
+    remote function deleteBucket(@display {label: "Bucket Name"} string bucketName) returns Error|();
 
     # Lists all buckets in the AWS account.
     # 
+    @display {label: "List Buckets"}
     remote function listBuckets() returns Bucket[]|Error;
 
     # Gets the AWS region of a bucket.
     # 
-    remote function getBucketLocation(string bucketName) returns string|Error;
+    @display {label: "Get Bucket Location"}
+    remote function getBucketLocation(@display {label: "Bucket Name"} string bucketName) returns string|Error;
 
     # Uploads an S3 object from a file path.
     # 
-    remote function putObjectFromFile(string bucketName, string objectKey, string filePath, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", PutObjectConfig config) returns Error|();
+    @display {label: "Put Object From File"}
+    remote function putObjectFromFile(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "File Path"} string filePath, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", PutObjectConfig config) returns Error|();
 
     # Uploads an S3 object from content.
     # 
-    remote function putObject(string bucketName, string objectKey, UploadContent content, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", PutObjectConfig config) returns Error|();
+    @display {label: "Put Object"}
+    remote function putObject(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Content"} UploadContent content, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", PutObjectConfig config) returns Error|();
 
     # Uploads an S3 object from a stream.
     # 
-    remote function putObjectAsStream(string bucketName, string objectKey, stream<byte[], error?> contentStream, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", int contentLength = 0, PutObjectStreamConfig config) returns Error|();
+    @display {label: "Put Object As Stream"}
+    remote function putObjectAsStream(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Content Stream"} stream<byte[], error?> contentStream, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string contentLanguage = "", string expires = "", string tagging = "", string serverSideEncryption = "", FileFormat fileFormat = "CSV", int contentLength = 0, PutObjectStreamConfig config) returns Error|();
 
     # Downloads an S3 object from an S3 bucket.
     # 
-    remote function getObject(string bucketName, string objectKey, byte[]|string|json|xml|record {|anydata...;|}|record {|anydata...;|}[]|stream<byte[], error?>|stream<record {|anydata...;|}, error?> targetType = s3:RetrievableType, string versionId = "", string range = "", string ifMatch = "", string ifNoneMatch = "", string ifModifiedSince = "", string ifUnmodifiedSince = "", int partNumber = 0, string responseContentType = "", string responseContentDisposition = "", GetObjectConfig config) returns targetType|Error;
+    @display {label: "Get Object"}
+    remote function getObject(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, byte[]|string|json|xml|record {|anydata...;|}|record {|anydata...;|}[]|stream<byte[], error?>|stream<record {|anydata...;|}, error?> targetType = s3:RetrievableType, string versionId = "", string range = "", string ifMatch = "", string ifNoneMatch = "", string ifModifiedSince = "", string ifUnmodifiedSince = "", int partNumber = 0, string responseContentType = "", string responseContentDisposition = "", GetObjectConfig config) returns targetType|Error;
 
     # Deletes an S3 object from an S3 bucket.
     # 
-    remote function deleteObject(string bucketName, string objectKey, string versionId = "", string mfa = "", boolean bypassGovernanceRetention = false, DeleteObjectConfig config) returns Error|();
+    @display {label: "Delete Object"}
+    remote function deleteObject(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, string versionId = "", string mfa = "", boolean bypassGovernanceRetention = false, DeleteObjectConfig config) returns Error|();
 
     # Lists S3 objects in an S3 bucket.
     # 
-    remote function listObjects(string bucketName, string prefix = "", string delimiter = "", int maxKeys = 0, string continuationToken = "", string startAfter = "", boolean fetchOwner = false, string encodingType = "", ListObjectsConfig config) returns ListObjectsResponse|Error;
+    @display {label: "List Objects"}
+    remote function listObjects(@display {label: "Bucket Name"} string bucketName, string prefix = "", string delimiter = "", int maxKeys = 0, string continuationToken = "", string startAfter = "", boolean fetchOwner = false, string encodingType = "", ListObjectsConfig config) returns ListObjectsResponse|Error;
 
     # Creates a presigned URL for temporary access to an S3 object.
     # 
-    remote function createPresignedUrl(string bucketName, string objectKey, int expirationMinutes = 0, HttpMethod httpMethod = "PUT", string contentType = "", string contentDisposition = "", string responseContentType = "", string versionId = "", PresignedUrlConfig config) returns string|Error;
+    @display {label: "Create Presigned URL"}
+    remote function createPresignedUrl(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, int expirationMinutes = 0, HttpMethod httpMethod = "PUT", string contentType = "", string contentDisposition = "", string responseContentType = "", string versionId = "", PresignedUrlConfig config) returns string|Error;
 
     # Gets metadata for an S3 object without downloading it.
     # 
-    remote function getObjectMetadata(string bucketName, string objectKey, string versionId = "", int partNumber = 0, string ifMatch = "", string ifNoneMatch = "", string ifModifiedSince = "", string ifUnmodifiedSince = "", HeadObjectConfig config) returns ObjectMetadata|Error;
+    @display {label: "Get Object Metadata"}
+    remote function getObjectMetadata(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, string versionId = "", int partNumber = 0, string ifMatch = "", string ifNoneMatch = "", string ifModifiedSince = "", string ifUnmodifiedSince = "", HeadObjectConfig config) returns ObjectMetadata|Error;
 
     # Copies an S3 object from one location to another.
     # 
-    remote function copyObject(string sourceBucket, string sourceKey, string destinationBucket, string destinationKey, CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", string metadataDirective = "", map<string> metadata = {}, string contentType = "", string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string tagging = "", string copySourceIfMatch = "", string copySourceIfNoneMatch = "", string copySourceIfModifiedSince = "", string copySourceIfUnmodifiedSince = "", CopyObjectConfig config) returns Error|();
+    @display {label: "Copy Object"}
+    remote function copyObject(@display {label: "Source Bucket"} string sourceBucket, @display {label: "Source Key"} string sourceKey, @display {label: "Destination Bucket"} string destinationBucket, @display {label: "Destination Key"} string destinationKey, CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", string metadataDirective = "", map<string> metadata = {}, string contentType = "", string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string tagging = "", string copySourceIfMatch = "", string copySourceIfNoneMatch = "", string copySourceIfModifiedSince = "", string copySourceIfUnmodifiedSince = "", CopyObjectConfig config) returns Error|();
 
     # Checks if an S3 object exists in an S3 bucket.
     # 
-    remote function doesObjectExist(string bucketName, string objectKey) returns boolean|Error;
+    @display {label: "Does Object Exist"}
+    remote function doesObjectExist(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey) returns boolean|Error;
 
     # Creates a multipart upload.
     # 
-    remote function createMultipartUpload(string bucketName, string objectKey, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string tagging = "", string serverSideEncryption = "", MultipartUploadConfig config) returns string|Error;
+    @display {label: "Create Multipart Upload"}
+    remote function createMultipartUpload(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, string contentType = "", CannedACL acl = "bucket-owner-full-control", StorageClass storageClass = "DEEP_ARCHIVE", map<string> metadata = {}, string cacheControl = "", string contentDisposition = "", string contentEncoding = "", string tagging = "", string serverSideEncryption = "", MultipartUploadConfig config) returns string|Error;
 
     # Uploads a part in a multipart upload.
     # Supported content types: `byte[]`, `string`, `json`, `xml`, `record {}`, `record {}[]`,
@@ -630,21 +653,25 @@
     # The records are serialized as CSV (field names as headers).
     # `stream<byte[], error?>` content is collected into bytes before uploading.
     # 
-    remote function uploadPart(string bucketName, string objectKey, string uploadId, int partNumber, UploadContent content, int contentLength = 0, string contentMD5 = "", FileFormat fileFormat = "CSV", UploadPartConfig config) returns string|Error;
+    @display {label: "Upload Part"}
+    remote function uploadPart(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Upload ID"} string uploadId, @display {label: "Part Number"} int partNumber, @display {label: "Content"} UploadContent content, int contentLength = 0, string contentMD5 = "", FileFormat fileFormat = "CSV", UploadPartConfig config) returns string|Error;
 
     # Uploads a part from a stream.
     # 
-    remote function uploadPartAsStream(string bucketName, string objectKey, string uploadId, int partNumber, stream<byte[], error?> contentStream, int contentLength = 0, string contentMD5 = "", FileFormat fileFormat = "CSV", UploadStreamPartConfig config) returns string|Error;
+    @display {label: "Upload Part As Stream"}
+    remote function uploadPartAsStream(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Upload ID"} string uploadId, @display {label: "Part Number"} int partNumber, @display {label: "Content Stream"} stream<byte[], error?> contentStream, int contentLength = 0, string contentMD5 = "", FileFormat fileFormat = "CSV", UploadStreamPartConfig config) returns string|Error;
 
     # Completes a multipart upload.
     # 
-    remote function completeMultipartUpload(string bucketName, string objectKey, string uploadId, int[] partNumbers, string[] etags) returns Error|();
+    @display {label: "Complete Multipart Upload"}
+    remote function completeMultipartUpload(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Upload ID"} string uploadId, @display {label: "Part Numbers"} int[] partNumbers, @display {label: "ETags"} string[] etags) returns Error|();
 
     # Aborts a multipart upload.
     # 
-    remote function abortMultipartUpload(string bucketName, string objectKey, string uploadId) returns Error|();
+    @display {label: "Abort Multipart Upload"}
+    remote function abortMultipartUpload(@display {label: "Bucket Name"} string bucketName, @display {label: "Object Key"} string objectKey, @display {label: "Upload ID"} string uploadId) returns Error|();
 
     # Closes the underlying S3 client and releases resources.
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
`````

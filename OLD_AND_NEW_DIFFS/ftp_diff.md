# ftp — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ftp` |
| **Old file** | `ftp/old/ballerina_ftp.bal.txt` |
| **New file** | `ftp/new/ballerina_ftp.bal.txt` |
| **Old lines** | 1564 |
| **New lines** | 1703 |
| **Lines added** | 174 |
| **Lines removed** | 35 |
| **Hunks** | 6 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 10 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 6 | 6 |

### Declarations added (18)

- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function onFileChange`
- `function poll`
- `function register`
- `type AllRetryAttemptsFailedError`
- `type CircuitBreakerOpenError`
- `type ConnectionError`
- `type ContentBindingError`
- `type Error`
- `type FileAlreadyExistsError`
- `type FileNotFoundError`
- `type InvalidConfigError`
- `type ServiceUnavailableError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 951–975 | 951–986 | Types | +19 | −8 |
| 2 | 979–990 | 990–1014 | Types | +17 | −4 |
| 3 | 1121–1134 | 1145–1211 | Types | +55 | −2 |
| 4 | 1136–1142 | 1213–1219 | Client | +1 | −1 |
| 5 | 1342–1348 | 1419–1425 | Client | +1 | −1 |
| 6 | 1532–1564 | 1609–1703 | Client | +81 | −19 |

---

## Unified diff

`````diff
--- ftp/old/ballerina_ftp.bal.txt	2026-08-12 12:57:29
+++ ftp/new/ballerina_ftp.bal.txt	2026-08-12 13:19:19
@@ -951,25 +951,36 @@
     # `true` if the input type is a file stream
     boolean isFile?;
     # Content read from the input file stream
-    stream<byte[] & readonly, ballerina/io:1.8.1:Error?> fileContent?;
+    stream<byte[] & readonly, io:Error?> fileContent?;
     # Input content as text
     string textContent?;
     # If `true`, input will be compressed before uploading
     boolean compressInput?;
 };
 
-// Unknown type: Error
-
-// Unknown type: ConnectionError
+# Defines the common error type for the module.
+type Error error;
 
-// Unknown type: FileNotFoundError
+# Error when connecting to the FTP/SFTP server.
+# This includes network failures, host unreachable, connection refused, etc.
+type ConnectionError error;
 
-// Unknown type: FileAlreadyExistsError
+# Error when a requested file or directory is not found.
+type FileNotFoundError error;
 
-// Unknown type: InvalidConfigError
+# Error when attempting to create a file or directory that already exists.
+type FileAlreadyExistsError error;
 
-// Unknown type: ServiceUnavailableError
+# Error when FTP/SFTP configuration is invalid.
+# This includes invalid port numbers, invalid regex patterns, invalid timeout values, etc.
+type InvalidConfigError error;
 
+# Error when the FTP/SFTP service is temporarily unavailable.
+# This is a transient error indicating the operation may succeed on retry.
+# Common causes include: server overload (421), connection issues (425, 426),
+# temporary file locks (450), or server-side processing errors (451).
+type ServiceUnavailableError error;
+
 # Detail record for ContentBindingError providing additional context about the binding failure.
 
 type ContentBindingErrorDetail record {
@@ -979,12 +990,25 @@
     byte[] content?;
 };
 
-// Unknown type: ContentBindingError
-
-// Unknown type: AllRetryAttemptsFailedError
+# Error when file content cannot be converted to the expected type.
+# This includes JSON/XML parsing errors, CSV format errors, and record type binding failures.
+# This error type is applicable to both Client operations and Listener callbacks.
+# 
+# When used with the Listener, if an `onError` remote function is defined in the service,
+# it will be invoked with this error type, allowing for custom error handling such as
+# moving failed files to an error folder or sending notifications.
+type ContentBindingError Error & error<ContentBindingErrorDetail>;
 
-// Unknown type: CircuitBreakerOpenError
+# Error when all retry attempts have been exhausted.
+# This error wraps the last failure encountered during retry attempts.
+type AllRetryAttemptsFailedError error;
 
+# Error returned when the circuit breaker is in OPEN state.
+# This indicates the FTP server is unavailable and requests are being blocked
+# to prevent cascade failures. The client should implement fallback logic
+# or wait for the circuit to transition to HALF_OPEN state.
+type CircuitBreakerOpenError error;
+
 # Metadata about a file or directory on the FTP server.
 
 type FileInfo record {
@@ -1121,14 +1145,67 @@
 class Service {
 }
 
-// Unknown type: Listener
+# Gets invoked during object initialization.
+# 
+class Listener {
+    function init(Protocol protocol = FTP, string host = "127.0.0.1", int port = 21, AuthConfiguration auth = {}, string path = "/", string fileNamePattern = "", decimal pollingInterval = 60, boolean userDirIsRoot = false, FileAgeFilter fileAgeFilter = {}, FileDependencyCondition[] fileDependencyConditions = [], boolean laxDataBinding = false, decimal connectTimeout = 30.0, SocketConfig socketConfig = {}, ProxyConfiguration proxy = {host: "", port: 0}, FileTransferMode fileTransferMode = BINARY, TransferCompression[] sftpCompression = [NO], string sftpSshKnownHosts = "", FailSafeOptions csvFailSafe = {}, CoordinationConfig coordination = {memberId: "", coordinationGroup: ""}, RetryConfig retryConfig = {}, ListenerConfiguration listenerConfig) returns Error?;
+
+    # Starts the FTP listener and begins monitoring for file changes.
+    # ```ballerina
+    # error? response = listener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
 
+    # Attaches an FTP service to the listener.
+    # ```ballerina
+    # error? response = listener.attach(service1);
+    # ```
+    # 
+    function attach(Service ftpService, string[]|string|() name = ()) returns error?;
+
+    # Stops the FTP listener and detaches the service.
+    # ```ballerina
+    # error? response = listener.detach(service1);
+    # ```
+    # 
+    function detach(Service ftpService) returns error?;
+
+    # Stops the FTP listener immediately.
+    # ```ballerina
+    # error? response = listener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Stops the FTP listener gracefully.
+    # ```ballerina
+    # error? response = listener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Polls the FTP server for new or deleted files.
+    # ```ballerina
+    # error? response = listener.poll();
+    # ```
+    # 
+    function poll() returns error?;
+
+    # Registers an FTP service with the listener.
+    # ```ballerina
+    # error? response = listener.register(ftpService, name);
+    # ```
+    # 
+    function register(Service ftpService, string|() name) returns error?;
+}
+
 // --- Client ---
 
 # FTP client for connecting to and managing FTP/SFTP servers.
 # Supports reading files in various formats (text, JSON, XML, CSV, bytes) and writing files with overwrite or append options.
 client class Client {
-    function init(ClientConfiguration clientConfig) returns ballerina/ftp:2.20.1:Error?;
+    function init(ClientConfiguration clientConfig) returns Error?;
 
     # Retrieves the file content from a remote resource.
     # ```ballerina
@@ -1136,7 +1213,7 @@
     # ```
     # 
     @deprecated
-    remote function get(string path) returns stream<byte[] & readonly, ballerina/io:1.8.1:Error?>|Error;
+    remote function get(string path) returns stream<byte[] & readonly, io:Error?>|Error;
 
     # Retrieves the file content as bytes from a remote resource.
     # ```ballerina
@@ -1342,7 +1419,7 @@
     # ```
     # 
     @deprecated
-    remote function get(string path) returns stream<byte[] & readonly, ballerina/io:1.8.1:Error?>|Error;
+    remote function get(string path) returns stream<byte[] & readonly, io:Error?>|Error;
 
     # Retrieves the file content as bytes from a remote resource.
     # ```ballerina
@@ -1532,33 +1609,95 @@
 
 // --- Service ---
 
-service ftp:Service on new ftp:Listener(ListenerConfiguration listenerConfig = {}) {
-    # Triggered when a CSV file is added to the monitored FTP location. Supports raw 2D string arrays, data binding to custom record types, and streaming for large files
-    remote function onFileCsv(string[][] content, FileInfo fileInfo, Caller caller) returns error?;
+# onFileChange and onFileCsv cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# onFileChange and onFileJson cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# onFileChange and onFileXml cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# onFileChange and onFileText cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# onFileChange and onFile cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# onFileChange and onFileDelete cannot coexist: onFileChange already reports every file in the poll, so the typed handler would process the same file twice.
+# An FTP service must declare at least one file handler. onError alone never receives a file, so the service would do nothing.
+# Mandatory: this service must carry the @ftp:ServiceConfig annotation. Replace {...} with its fields, which are those of ftp:ServiceConfiguration.
+@ftp:ServiceConfig {...} // required
+service ftp:Service on new ftp:Listener(ftp:ListenerConfiguration listenerConfig = {}) {
+    # Invoked for each .csv file found in the watched directory. Declaring a stream parameter reads the file in chunks instead of loading it into memory.
+    # + contents - The parsed rows, see the csvContent data-binding rule for the batched and streamed forms.
+    # + fileInfo - The file's name, path, size, and timestamps.
+    # + caller - The FTP connection, for reading or writing other files while this one is being processed.
+    # `contents` may also be: record {}[], stream<string[], error?>, stream<record {}, error?>
+    # Required parameters: contents, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFileCsv(string[][] contents, ftp:FileInfo fileInfo, ftp:Caller caller) returns error?; // optional
 
-    # Triggered when a JSON file is added to the monitored FTP location. Supports raw json or data binding to custom record types
-    remote function onFileJson(json content, FileInfo fileInfo, Caller caller) returns error?;
+    # Invoked for each .json file found in the watched directory.
+    # + content - The parsed content, bind a record type to project it, see the jsonContent data-binding rule.
+    # + fileInfo - The file's name, path, size, and timestamps.
+    # `content` may bind directly to: record {}
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFileJson(json content, ftp:FileInfo fileInfo) returns error?; // optional
 
-    # Triggered when an XML file is added to the monitored FTP location
-    remote function onFileXml(xml content, FileInfo fileInfo, Caller caller) returns error?;
+    # Invoked for each .xml file found in the watched directory.
+    # + content - The parsed content, bind a record type to project it, see the xmlContent data-binding rule.
+    # + fileInfo - The file's name, path, size, and timestamps.
+    # `content` may bind directly to: record {}
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFileXml(xml content, ftp:FileInfo fileInfo) returns error?; // optional
 
-    # Triggered when a text file is added to the monitored FTP location
-    remote function onFileText(string content, FileInfo fileInfo, Caller caller) returns error?;
+    # Invoked for each plain-text file found in the watched directory.
+    # + content - The file's text content.
+    # + fileInfo - The file's name, path, size, and timestamps.
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFileText(string content, ftp:FileInfo fileInfo) returns error?; // optional
 
-    # Triggered when any file is added to the monitored FTP location. Supports raw byte arrays and streaming for large binary files
-    remote function onFile(byte[] content, FileInfo fileInfo, Caller caller) returns error?;
+    # Invoked for any file no typed handler matched, and as the fallback when a typed handler is not declared. Content arrives as raw bytes.
+    # + content - The file's bytes. Declare the stream form to read large files in chunks rather than loading them into memory.
+    # + fileInfo - The file's name, path, size, and timestamps.
+    # `content` may also be: stream<byte[], error?>
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFile(byte[] content, ftp:FileInfo fileInfo) returns error?; // optional
 
-    # Triggered when a file is deleted from the monitored FTP location
-    remote function onFileDelete(string deletedFile, Caller caller) returns error?;
+    # Invoked when a file disappears from the watched directory. There is no content or file metadata, because the file is already gone.
+    # + deleteFiles - Path of the file that was deleted.
+    # + caller - The FTP connection, for acting on the share in response to the deletion.
+    # Required parameters: deleteFiles
+    # Optional parameters (may be omitted): caller
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onFileDelete(string deleteFiles, ftp:Caller caller) returns error?; // optional
 
-    # Triggered when an error occurs during file processing. Implement this to handle failures gracefully
-    remote function onError(Error ftpError, Caller caller) returns error?;
+    # Invoked when the listener fails to poll, read, or bind a file, and when a handler itself returns an error. Without it, failures are logged and polling continues.
+    # + ftpError - The failure that interrupted processing.
+    # + caller - The FTP connection, for acting on the share while handling the failure.
+    # Required parameters: ftpError
+    # Optional parameters (may be omitted): caller
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    @ftp:FunctionConfig {...} // optional
+    remote function onError(ftp:Error ftpError, ftp:Caller caller) returns error?; // optional
+
+    # Invoked once per poll with the complete set of files added and deleted since the previous poll.
+    # + watchEvent - The files added and deleted in this poll.
+    # Optional: this handler may carry the @ftp:FunctionConfig annotation. Replace {...} with its fields, which are those of ftp:FtpFunctionConfig.
+    #
+    # # Deprecated
+    # Superseded by the typed content handlers. onFileChange only reports which files changed, leaving the read and the parse to the handler, whereas onFileText, onFileJson, onFileXml, onFileCsv and onFile deliver the file body already bound to a declared type.
+    @ftp:FunctionConfig {...} // optional
+    @deprecated
+    remote function onFileChange(ftp:WatchEvent watchEvent) returns error?; // optional
 }
 
 // --- Annotations ---
 
-# Define service-level configuration such as the FTP directory path to monitor
-public annotation FtpServiceConfig ServiceConfig on service;
+# Annotation to configure FTP service remote functions.
+# This can be used to specify which file patterns should be handled by a particular content method
+# and what actions to perform after processing.
+public annotation FtpFunctionConfig FunctionConfig on service remote function;
 
-# Configure pre/post processing actions on the file (e.g., move or delete the file after processing)
-public annotation FtpFunctionConfig FunctionConfig on service_function;
+# Annotation to configure FTP service monitoring path and file patterns.
+# This annotation allows each service to define its own monitoring configuration,
+# enabling multiple services on a single listener to monitor different paths independently.
+public annotation ServiceConfiguration ServiceConfig on service;
`````

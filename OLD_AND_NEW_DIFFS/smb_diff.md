# smb — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `smb` |
| **Old file** | `smb/old/ballerina_smb.bal.txt` |
| **New file** | `smb/new/ballerina_smb.bal.txt` |
| **Old lines** | 973 |
| **New lines** | 1148 |
| **Lines added** | 181 |
| **Lines removed** | 6 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 6 |

### Declarations added (23)

- `annotation FunctionConfig`
- `annotation ServiceConfig`
- `class ContentByteStream`
- `class ContentCsvRecordStream`
- `class ContentCsvStringArrayStream`
- `class Listener`
- `function 'start`
- `function attach`
- `function close`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function next`
- `function onError`
- `function onFile`
- `function onFileCsv`
- `function onFileDelete`
- `function onFileJson`
- `function onFileText`
- `function onFileXml`
- `function poll`
- `function register`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 354–360 | 354–361 | Types | +2 | −1 |
| 2 | 560–573 | 561–660 | Types | +90 | −4 |
| 3 | 769–775 | 856–862 | Client | +1 | −1 |
| 4 | 971–973 | 1058–1148 | Client | +88 | −0 |

---

## Unified diff

`````diff
--- smb/old/ballerina_smb.bal.txt	2026-08-12 23:21:51
+++ smb/new/ballerina_smb.bal.txt	2026-08-12 23:23:51
@@ -354,7 +354,8 @@
     KerberosConfig kerberosConfig?;
 };
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Configuration for the SMB client.
 # 
@@ -560,14 +561,100 @@
     record {|anydata...;|} value;
 };
 
-// Unknown type: ContentByteStream
+class ContentByteStream {
+    function init(Error|() err = ()) returns ();
 
-// Unknown type: ContentCsvRecordStream
+    # Reads and return the next `byte[]` chunk of the stream.
+    # 
+    function next() returns record {|byte[] value;|}|error?;
 
-// Unknown type: ContentCsvStringArrayStream
+    # Closes the stream. The primary usage of this function is to close the stream without reaching the end.
+    # If the stream reaches the end, the `contentByteStream.next` will automatically close the stream.
+    # 
+    function close() returns error?;
+}
 
-// Unknown type: Listener
+class ContentCsvRecordStream {
+    function init(Error|() err = ()) returns ();
+
+    # Reads and return the next CSV record as `record{}`.
+    # 
+    function next() returns record {|record {|anydata...;|} value;|}|error?;
+
+    # Closes the stream. The primary usage of this function is to close the stream without reaching the end.
+    # If the stream reaches the end, the `contentCsvRecordStream.next` will automatically close the stream.
+    # 
+    function close() returns error?;
+}
 
+class ContentCsvStringArrayStream {
+    function init(Error|() err = ()) returns ();
+
+    # Reads and return the next CSV record as `string[]`.
+    # 
+    function next() returns record {|string[] value;|}|error?;
+
+    # Closes the stream. The primary usage of this function is to close the stream without reaching the end.
+    # If the stream reaches the end, the `contentCsvStringArrayStream.next` will automatically close the stream.
+    # 
+    function close() returns error?;
+}
+
+# Gets invoked during object initialization.
+# 
+class Listener {
+    function init(string host = "localhost", int port = 445, string share = "", AuthConfiguration auth = {}, string fileNamePattern = "", decimal pollingInterval = 60, Dialect[] dialects = [SMB_3_1_1, SMB_3_0_2, SMB_3_0, SMB_2_1, SMB_2_0_2], boolean signRequired = false, boolean encryptData = false, boolean enableDfs = false, int bufferSize = 65536, decimal connectTimeout = 30.0, boolean laxDataBinding = false, FailSafeOptions csvFailSafe = {}, ListenerConfiguration listenerConfig) returns Error?;
+
+    # Starts the SMB listener and begins monitoring for file changes.
+    # ```ballerina
+    # error? response = listener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Attaches an SMB service to the listener.
+    # ```ballerina
+    # error? response = listener.attach(service1);
+    # ```
+    # 
+    function attach(Service smbService, string[]|string|() name = ()) returns error?;
+
+    # Stops the SMB listener and detaches the service.
+    # ```ballerina
+    # error? response = listener.detach(service1);
+    # ```
+    # 
+    function detach(Service smbService) returns error?;
+
+    # Stops the SMB listener immediately.
+    # ```ballerina
+    # error? response = listener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Stops the SMB listener gracefully.
+    # ```ballerina
+    # error? response = listener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Polls the SMB server for new or deleted files.
+    # ```ballerina
+    # error? response = listener.poll();
+    # ```
+    # 
+    function poll() returns error?;
+
+    # Registers an SMB service with the listener.
+    # ```ballerina
+    # error? response = listener.register(smbService, name);
+    # ```
+    # 
+    function register(Service smbService, string|() name) returns error?;
+}
+
 // --- Client ---
 
 # Provides access to the SMB share from within a service's remote methods.
@@ -769,7 +856,7 @@
 # Connects to an SMB share to read, write, and manage its files and directories.
 # Reads and writes text, JSON, XML, CSV, and binary content, with streaming support for large files.
 client class Client {
-    function init(ClientConfiguration clientConfig) returns ballerina/smb:2.0.1:Error?;
+    function init(ClientConfiguration clientConfig) returns Error?;
 
     # Writes byte array content to a file on an SMB share.
     # ```ballerina
@@ -971,3 +1058,91 @@
     # 
     remote function close() returns Error|();
 }
+
+// --- Service ---
+
+# The service identifier accepts a base path, e.g. `/orders`; it may be omitted.
+# An SMB service must declare at least one onFile* handler or onFileDelete, otherwise nothing is ever dispatched. onError alone does not count.
+# An SMB service needs its watched path from exactly one source: @smb:ServiceConfig { path } or the service identifier.
+# Prefer the `path` field of @smb:ServiceConfig unless the requirement says otherwise.
+# Mandatory: this service must carry the @smb:ServiceConfig annotation. Replace {...} with its fields, which are those of smb:SmbServiceConfig.
+@smb:ServiceConfig {...} // required
+service smb:Service on new smb:Listener(smb:ListenerConfiguration listenerConfig = {}) {
+    # Invoked for each .txt, .log, or .md file found in the watched directory. Falls through to onFile when not declared.
+    # + content - The file's text content.
+    # + caller - The share connection, for reading or writing other files while this one is being processed.
+    # + fileInfo - The file's name, path, size, timestamps, and attributes.
+    # Required parameters: content, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFileText(string content, smb:Caller caller, smb:FileInfo fileInfo) returns error?; // optional
+
+    # Invoked for each .json file found in the watched directory. Falls through to onFile when not declared.
+    # + content - The parsed content, bind a record type to project it, see the jsonContent data-binding rule.
+    # + caller - The share connection, for reading or writing other files while this one is being processed.
+    # + fileInfo - The file's name, path, size, timestamps, and attributes.
+    # `content` may bind directly to: record {}
+    # Required parameters: content, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFileJson(json content, smb:Caller caller, smb:FileInfo fileInfo) returns error?; // optional
+
+    # Invoked for each .xml file found in the watched directory. Falls through to onFile when not declared.
+    # + content - The parsed content, bind a record type to project it, see the xmlContent data-binding rule.
+    # + caller - The share connection, for reading or writing other files while this one is being processed.
+    # + fileInfo - The file's name, path, size, timestamps, and attributes.
+    # `content` may bind directly to: record {}
+    # Required parameters: content, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFileXml(xml content, smb:Caller caller, smb:FileInfo fileInfo) returns error?; // optional
+
+    # Invoked for each .csv file found in the watched directory. Declaring a stream parameter reads the file in chunks instead of loading it into memory.
+    # + content - The parsed rows, see the csvContent data-binding rule for the batched and streamed forms.
+    # + caller - The share connection, for reading or writing other files while this one is being processed.
+    # + fileInfo - The file's name, path, size, timestamps, and attributes.
+    # `content` may also be: record {}[], stream<string[], error?>, stream<record {}, error?>
+    # Required parameters: content, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFileCsv(string[][] content, smb:Caller caller, smb:FileInfo fileInfo) returns error?; // optional
+
+    # Invoked for any file no typed handler matched, and as the fallback when a typed handler is not declared. Content arrives as raw bytes.
+    # + content - The file's bytes. Declare the stream form to read large files in chunks rather than loading them into memory.
+    # + caller - The share connection, for reading or writing other files while this one is being processed.
+    # + fileInfo - The file's name, path, size, timestamps, and attributes.
+    # `content` may also be: stream<byte[], error?>
+    # Required parameters: content, fileInfo
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFile(byte[] content, smb:Caller caller, smb:FileInfo fileInfo) returns error?; // optional
+
+    # Invoked when a file disappears from the watched directory. There is no content and no file metadata, because the file is already gone.
+    # + path - Path of the file that was deleted.
+    # + caller - The share connection, for acting on the share in response to the deletion.
+    # Required parameters: path
+    # Optional parameters (may be omitted): caller
+    # Mandatory: this handler must carry the @smb:FunctionConfig annotation. Replace {...} with its fields, which are those of smb:FunctionConfiguration.
+    @smb:FunctionConfig {...} // required
+    remote function onFileDelete(string path, smb:Caller caller) returns error?; // optional
+
+    # Invoked when the listener fails to poll, read, or bind a file, and when a handler itself returns an error. Without it, failures are logged and polling continues.
+    # + err - The failure that interrupted processing.
+    # + caller - The share connection, for acting on the share while handling the failure.
+    # Required parameters: err
+    # Optional parameters (may be omitted): caller
+    remote function onError(smb:Error err, smb:Caller caller) returns error?; // optional
+}
+
+// --- Annotations ---
+
+# The annotation to configure an SMB content handler method.
+public annotation FunctionConfiguration FunctionConfig on service remote function;
+
+# The annotation to configure an SMB service.
+public annotation SmbServiceConfig ServiceConfig on service;
`````

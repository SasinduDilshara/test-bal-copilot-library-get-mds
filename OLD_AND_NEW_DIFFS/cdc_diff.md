# cdc — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `cdc` |
| **Old file** | `cdc/old/ballerinax_cdc.bal.txt` |
| **New file** | `cdc/new/ballerinax_cdc.bal.txt` |
| **Old lines** | 1310 |
| **New lines** | 1339 |
| **Lines added** | 37 |
| **Lines removed** | 8 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 15 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (10)

- `annotation ServiceConfig`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `type Error`
- `type EventProcessingError`
- `type OperationNotPermittedError`
- `type PayloadBindingError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 237–252 | 237–276 | Types | +28 | −4 |
| 2 | 429–437 | 453–461 | Types | +2 | −2 |
| 3 | 1064–1073 | 1088–1097 | Types | +2 | −2 |
| 4 | 1308–1310 | 1332–1339 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- cdc/old/ballerinax_cdc.bal.txt	2026-08-12 12:57:30
+++ cdc/new/ballerinax_cdc.bal.txt	2026-08-12 13:19:19
@@ -237,16 +237,40 @@
     json payload;
 };
 
-// Unknown type: Error
+# Defines the common error type for the CDC module.
+type Error error;
 
-// Unknown type: EventProcessingError
+# Represents an error that occurred during event processing.
+type EventProcessingError error<record {|json payload; anydata...;|}>;
 
-// Unknown type: PayloadBindingError
+# Represents an error that occurred due to payload binding issues.
+type PayloadBindingError error<record {|json payload; anydata...;|}>;
 
-// Unknown type: OperationNotPermittedError
+# Represents an error that occurred due to an operation not being permitted.
+type OperationNotPermittedError error;
 
 # Represents a Ballerina CDC MySQL Listener.
 class Listener {
+
+    # Attaches a CDC service to the listener.
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns Error|();
+
+    # Starts the CDC listener.
+    # 
+    function 'start() returns Error|();
+
+    # Detaches a CDC service from the listener.
+    # 
+    function detach(Service s) returns Error|();
+
+    # Stops the listener gracefully.
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the listener immediately.
+    # 
+    function immediateStop() returns Error|();
 }
 
 # Represents a CDC service in Ballerina.
@@ -429,9 +453,9 @@
     # Configurations associated with crypto:TrustStore or single certificate file that the client trusts
     crypto:TrustStore|string cert; // Special Agent Note: TrustStore FROM ballerina/crypto package
     # Configurations associated with crypto:KeyStore or combination of certificate and private key of the client
-    record {|ballerina/crypto:2.12.1:KeyStore keyStore; string keyPassword?;|}|KafkaSecureSocketCertKey key?;
+    record {|crypto:KeyStore keyStore; string keyPassword?;|}|KafkaSecureSocketCertKey key?;
     # SSL/TLS protocol related options
-    record {|ballerinax/cdc:1.4.0:KafkaSecureSocketProtocol name; string[] versions?;|} protocol?;
+    record {|KafkaSecureSocketProtocol name; string[] versions?;|} protocol?;
     # List of ciphers to be used. By default, all the available cipher suites are supported
     string[] ciphers?;
     # Name of the security provider used for SSL connections. The default value is the default security provider
@@ -1064,10 +1088,10 @@
 };
 
 # Union type representing all supported internal schema history storage configurations.
-type InternalSchemaStorage ballerinax/cdc:1.4.0:FileInternalSchemaStorage|ballerinax/cdc:1.4.0:KafkaInternalSchemaStorage|ballerinax/cdc:1.4.0:MemoryInternalSchemaStorage|ballerinax/cdc:1.4.0:JdbcInternalSchemaStorage|ballerinax/cdc:1.4.0:RedisInternalSchemaStorage|ballerinax/cdc:1.4.0:AmazonS3InternalSchemaStorage|ballerinax/cdc:1.4.0:AzureBlobInternalSchemaStorage|ballerinax/cdc:1.4.0:RocketMQInternalSchemaStorage;
+type InternalSchemaStorage FileInternalSchemaStorage|KafkaInternalSchemaStorage|MemoryInternalSchemaStorage|JdbcInternalSchemaStorage|RedisInternalSchemaStorage|AmazonS3InternalSchemaStorage|AzureBlobInternalSchemaStorage|RocketMQInternalSchemaStorage;
 
 # Union type representing all supported offset storage configurations.
-type OffsetStorage ballerinax/cdc:1.4.0:FileOffsetStorage|ballerinax/cdc:1.4.0:KafkaOffsetStorage|ballerinax/cdc:1.4.0:MemoryOffsetStorage|ballerinax/cdc:1.4.0:JdbcOffsetStorage|ballerinax/cdc:1.4.0:RedisOffsetStorage;
+type OffsetStorage FileOffsetStorage|KafkaOffsetStorage|MemoryOffsetStorage|JdbcOffsetStorage|RedisOffsetStorage;
 
 # Base CDC listener configuration.
 # 
@@ -1308,3 +1332,8 @@
 # + configMap - Map to populate with additional configuration properties
 # + optionsSubType - Type descriptor for the options subtype
 function populateAdditionalConfigurations(Options options, map<string> configMap, cdc:Options optionsSubType) returns ();
+
+// --- Annotations ---
+
+# The annotation to configure a CDC service.
+public annotation CdcServiceConfig ServiceConfig on service;
`````

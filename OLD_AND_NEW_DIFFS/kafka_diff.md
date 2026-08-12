# kafka — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `kafka` |
| **Old file** | `kafka/old/ballerinax_kafka.bal.txt` |
| **New file** | `kafka/new/ballerinax_kafka.bal.txt` |
| **Old lines** | 936 |
| **New lines** | 1011 |
| **Lines added** | 94 |
| **Lines removed** | 19 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 8 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 5 | 0 |
| `// --- section ---` markers | 5 | 6 |

### Declarations added (16)

- `annotation Payload`
- `class AvroDeserializer`
- `class AvroSerializer`
- `class Listener`
- `function 'start`
- `function attach`
- `function deserialize`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function serialize`
- `type Error`
- `type PayloadBindingError`
- `type PayloadValidationError`
- `type TopicPartitionOffset`
- `type TopicPartitionTimestamp`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 284–292 | 284–292 | Types | +2 | −2 |
| 2 | 625–635 | 625–638 | Types | +6 | −3 |
| 3 | 637–649 | 640–661 | Types | +10 | −1 |
| 4 | 656–662 | 668–675 | Types | +2 | −1 |
| 5 | 675–691 | 688–750 | Types | +51 | −5 |
| 6 | 712–718 | 771–777 | Client | +1 | −1 |
| 7 | 887–893 | 946–952 | Client | +1 | −1 |
| 8 | 927–936 | 986–1011 | Client | +21 | −5 |

---

## Unified diff

`````diff
--- kafka/old/ballerinax_kafka.bal.txt	2026-08-12 12:57:30
+++ kafka/new/ballerinax_kafka.bal.txt	2026-08-12 13:19:19
@@ -284,9 +284,9 @@
     # Configurations associated with crypto:TrustStore or single certificate file that the client trusts
     crypto:TrustStore|string cert; // Special Agent Note: TrustStore FROM ballerina/crypto package
     # Configurations associated with crypto:KeyStore or combination of certificate and private key of the client
-    record {|ballerina/crypto:2.12.1:KeyStore keyStore; string keyPassword?;|}|CertKey key?;
+    record {|crypto:KeyStore keyStore; string keyPassword?;|}|CertKey key?;
     # SSL/TLS protocol related options
-    record {|ballerinax/kafka:4.6.5:Protocol name; string[] versions?;|} protocol?;
+    record {|Protocol name; string[] versions?;|} protocol?;
     # List of ciphers to be used. By default, all the available cipher suites are supported
     string[] ciphers?;
     # Name of the security provider used for SSL connections. The default value is the default security provider
@@ -625,11 +625,14 @@
 type KafkaPayload record {
 };
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
-// Unknown type: PayloadBindingError
+# Represents an error, which occurred due to payload binding.
+type PayloadBindingError error<record {|TopicPartition partition; int offset;|}>;
 
-// Unknown type: PayloadValidationError
+# Represents an error, which occurred due to payload constraint validation.
+type PayloadValidationError error<record {|record {|string topic; int partition;|} partition; int offset;|}>;
 
 # The Kafka service type.
 class Service {
@@ -637,13 +640,22 @@
 
 # Interface for serializing a given value
 class Serializer {
+
+    # Serializes a given value using the provided schema
+    # 
+    function serialize(anydata value, string schema, string subject) returns byte[]|error;
 }
 
 # Interface for deserializing a given value
 class Deserializer {
+
+    # Deserializes the provided value
+    # 
+    function deserialize(byte[] value) returns anydata|error;
 }
 
-// Unknown type: TopicPartitionTimestamp
+# Represents a topic partition and a timestamp.
+type TopicPartitionTimestamp [TopicPartition, int];
 
 # Represents an offset and a timestamp for a topic partition.
 
@@ -656,7 +668,8 @@
     int? leaderEpoch?;
 };
 
-// Unknown type: TopicPartitionOffset
+# Represents a topic partition and an offset with a timestamp.
+type TopicPartitionOffset [TopicPartition, OffsetAndTimestamp?];
 
 # Represents metadata of a Kafka record.
 
@@ -675,17 +688,63 @@
     int partition;
 };
 
-// Unknown type: Listener
-
-// Unknown type: AvroSerializer
+# Creates a new `kafka:Listener`.
+# 
+class Listener {
+    function init(string|string[] bootstrapServers, string groupId = "", string|string[] topics = "", OffsetResetMethod offsetReset = "earliest", string partitionAssignmentStrategy = "", string metricsRecordingLevel = "", string metricsReporterClasses = "", string clientId = "", string interceptorClasses = "", IsolationLevel isolationLevel = "read_committed", string schemaRegistryUrl = "", map<anydata> & readonly schemaRegistryConfig = {}, DeserializerType keyDeserializerType = DES_BYTE_ARRAY, DeserializerType valueDeserializerType = DES_BYTE_ARRAY, map<string> additionalProperties = {}, decimal sessionTimeout = 0.0d, decimal heartBeatInterval = 0.0d, decimal metadataMaxAge = 0.0d, decimal autoCommitInterval = 0.0d, int maxPartitionFetchBytes = 0, int sendBuffer = 0, int receiveBuffer = 0, int fetchMinBytes = 0, int fetchMaxBytes = 0, decimal fetchMaxWaitTime = 0.0d, decimal reconnectBackoffTimeMax = 0.0d, decimal retryBackoff = 0.0d, decimal metricsSampleWindow = 0.0d, int metricsNumSamples = 0, decimal requestTimeout = 0.0d, decimal connectionMaxIdleTime = 0.0d, int maxPollRecords = 0, int maxPollInterval = 0, decimal reconnectBackoffTime = 0.0d, decimal pollingTimeout = 0.0d, decimal pollingInterval = 0.0d, int concurrentConsumers = 0, decimal defaultApiTimeout = 0.0d, boolean autoCommit = true, boolean checkCRCS = true, boolean excludeInternalTopics = true, boolean decoupleProcessing = false, boolean validation = true, boolean autoSeekOnValidationFailure = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, AuthenticationConfiguration auth = {username: "", password: ""}, SecurityProtocol securityProtocol = PLAINTEXT, ConsumerConfiguration config) returns Error?;
 
-// Unknown type: AvroDeserializer
+    # Starts the registered services.
+    # ```ballerina
+    # error? result = listener.'start();
+    # ```
+    # 
+    function 'start() returns error?;
 
+    # Stops the Kafka listener gracefully.
+    # ```ballerina
+    # error? result = listener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Stops the kafka listener immediately.
+    # ```ballerina
+    # error? result = listener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Attaches a service to the listener.
+    # ```ballerina
+    # error? result = listener.attach(kafkaService);
+    # ```
+    # 
+    function attach(Service 'service, string[]|string|() name = ()) returns error?;
+
+    # Detaches a consumer service from the listener.
+    # ```ballerina
+    # error? result = listener.detach(kafkaService);
+    # ```
+    # 
+    function detach(Service 'service) returns error?;
+}
+
+class AvroSerializer {
+    function init(anydata & readonly schemaRegistryConfig, string schema) returns error?;
+
+    function serialize(anydata value, string schema, string subject) returns byte[]|error;
+}
+
+class AvroDeserializer {
+    function init(anydata & readonly schemaRegistryConfig) returns error?;
+
+    function deserialize(byte[] value) returns anydata|error;
+}
+
 // --- Client ---
 
 # Represents a Kafka caller, which can be used to commit the offsets consumed by the service.
 client class Caller {
-    function init() returns ballerinax/kafka:kafka:Caller;
 
     # Commits the currently consumed offsets of the service.
     # ```ballerina
@@ -712,7 +771,7 @@
 # Represents a Kafka consumer endpoint.
 # 
 client class Consumer {
-    function init(string|string[] bootstrapServers, string groupId = "", string|string[] topics = "", OffsetResetMethod offsetReset = "earliest", string partitionAssignmentStrategy = "", string metricsRecordingLevel = "", string metricsReporterClasses = "", string clientId = "", string interceptorClasses = "", IsolationLevel isolationLevel = "read_committed", string schemaRegistryUrl = "", map<anydata> & readonly schemaRegistryConfig = {}, DeserializerType keyDeserializerType = DES_BYTE_ARRAY, DeserializerType valueDeserializerType = DES_BYTE_ARRAY, map<string> additionalProperties = {}, decimal sessionTimeout = 0.0d, decimal heartBeatInterval = 0.0d, decimal metadataMaxAge = 0.0d, decimal autoCommitInterval = 0.0d, int maxPartitionFetchBytes = 0, int sendBuffer = 0, int receiveBuffer = 0, int fetchMinBytes = 0, int fetchMaxBytes = 0, decimal fetchMaxWaitTime = 0.0d, decimal reconnectBackoffTimeMax = 0.0d, decimal retryBackoff = 0.0d, decimal metricsSampleWindow = 0.0d, int metricsNumSamples = 0, decimal requestTimeout = 0.0d, decimal connectionMaxIdleTime = 0.0d, int maxPollRecords = 0, int maxPollInterval = 0, decimal reconnectBackoffTime = 0.0d, decimal pollingTimeout = 0.0d, decimal pollingInterval = 0.0d, int concurrentConsumers = 0, decimal defaultApiTimeout = 0.0d, boolean autoCommit = true, boolean checkCRCS = true, boolean excludeInternalTopics = true, boolean decoupleProcessing = false, boolean validation = true, boolean autoSeekOnValidationFailure = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, AuthenticationConfiguration auth = {username: "", password: ""}, SecurityProtocol securityProtocol = PLAINTEXT, ConsumerConfiguration config) returns ballerinax/kafka:4.6.5:Error?;
+    function init(string|string[] bootstrapServers, string groupId = "", string|string[] topics = "", OffsetResetMethod offsetReset = "earliest", string partitionAssignmentStrategy = "", string metricsRecordingLevel = "", string metricsReporterClasses = "", string clientId = "", string interceptorClasses = "", IsolationLevel isolationLevel = "read_committed", string schemaRegistryUrl = "", map<anydata> & readonly schemaRegistryConfig = {}, DeserializerType keyDeserializerType = DES_BYTE_ARRAY, DeserializerType valueDeserializerType = DES_BYTE_ARRAY, map<string> additionalProperties = {}, decimal sessionTimeout = 0.0d, decimal heartBeatInterval = 0.0d, decimal metadataMaxAge = 0.0d, decimal autoCommitInterval = 0.0d, int maxPartitionFetchBytes = 0, int sendBuffer = 0, int receiveBuffer = 0, int fetchMinBytes = 0, int fetchMaxBytes = 0, decimal fetchMaxWaitTime = 0.0d, decimal reconnectBackoffTimeMax = 0.0d, decimal retryBackoff = 0.0d, decimal metricsSampleWindow = 0.0d, int metricsNumSamples = 0, decimal requestTimeout = 0.0d, decimal connectionMaxIdleTime = 0.0d, int maxPollRecords = 0, int maxPollInterval = 0, decimal reconnectBackoffTime = 0.0d, decimal pollingTimeout = 0.0d, decimal pollingInterval = 0.0d, int concurrentConsumers = 0, decimal defaultApiTimeout = 0.0d, boolean autoCommit = true, boolean checkCRCS = true, boolean excludeInternalTopics = true, boolean decoupleProcessing = false, boolean validation = true, boolean autoSeekOnValidationFailure = true, SecureSocket secureSocket = {cert: {path: "", password: ""}}, AuthenticationConfiguration auth = {username: "", password: ""}, SecurityProtocol securityProtocol = PLAINTEXT, ConsumerConfiguration config) returns Error?;
 
     # Assigns consumer to a set of topic partitions.
     # ```ballerina
@@ -887,7 +946,7 @@
 # Represents a Kafka producer endpoint.
 # 
 client class Producer {
-    function init(string|string[] bootstrapServers, ProducerAcks acks = 1, CompressionType compressionType = none, string clientId = "", string metricsRecordingLevel = "", string metricReporterClasses = "", string partitionerClass = "", string interceptorClasses = "", string transactionalId = "", string schemaRegistryUrl = "", string avroSchema = "", string keySchema = "", string valueSchema = "", map<anydata> schemaRegistryConfig = {}, SerializerType keySerializerType = SER_BYTE_ARRAY, SerializerType valueSerializerType = SER_BYTE_ARRAY, map<string> additionalProperties = {}, int bufferMemory = 0, int retryCount = 0, int batchSize = 0, decimal linger = 0.0d, int sendBuffer = 0, int receiveBuffer = 0, int maxRequestSize = 0, decimal reconnectBackoffTime = 0.0d, decimal reconnectBackoffMaxTime = 0.0d, decimal retryBackoffTime = 0.0d, decimal maxBlock = 0.0d, decimal requestTimeout = 0.0d, decimal metadataMaxAge = 0.0d, decimal metricsSampleWindow = 0.0d, int metricsNumSamples = 0, int maxInFlightRequestsPerConnection = 0, decimal connectionsMaxIdleTime = 0.0d, decimal transactionTimeout = 0.0d, boolean enableIdempotence = false, SecureSocket secureSocket = {cert: {path: "", password: ""}}, AuthenticationConfiguration auth = {username: "", password: ""}, SecurityProtocol securityProtocol = PLAINTEXT, ProducerConfiguration config) returns ballerinax/kafka:4.6.5:Error?;
+    function init(string|string[] bootstrapServers, ProducerAcks acks = 1, CompressionType compressionType = none, string clientId = "", string metricsRecordingLevel = "", string metricReporterClasses = "", string partitionerClass = "", string interceptorClasses = "", string transactionalId = "", string schemaRegistryUrl = "", string avroSchema = "", string keySchema = "", string valueSchema = "", map<anydata> schemaRegistryConfig = {}, SerializerType keySerializerType = SER_BYTE_ARRAY, SerializerType valueSerializerType = SER_BYTE_ARRAY, map<string> additionalProperties = {}, int bufferMemory = 0, int retryCount = 0, int batchSize = 0, decimal linger = 0.0d, int sendBuffer = 0, int receiveBuffer = 0, int maxRequestSize = 0, decimal reconnectBackoffTime = 0.0d, decimal reconnectBackoffMaxTime = 0.0d, decimal retryBackoffTime = 0.0d, decimal maxBlock = 0.0d, decimal requestTimeout = 0.0d, decimal metadataMaxAge = 0.0d, decimal metricsSampleWindow = 0.0d, int metricsNumSamples = 0, int maxInFlightRequestsPerConnection = 0, decimal connectionsMaxIdleTime = 0.0d, decimal transactionTimeout = 0.0d, boolean enableIdempotence = false, SecureSocket secureSocket = {cert: {path: "", password: ""}}, AuthenticationConfiguration auth = {username: "", password: ""}, SecurityProtocol securityProtocol = PLAINTEXT, ProducerConfiguration config) returns Error?;
 
     # Closes the producer connection to the external Kafka broker.
     # ```ballerina
@@ -927,10 +986,26 @@
 
 // --- Service ---
 
-service kafka:Service on new kafka:Listener(string|string[] bootstrapServers = "", ConsumerConfiguration config = {}) {
-    # The `onConsumerRecord` remote method will be triggered when a message is received from Kafka topic(s)
-    remote function onConsumerRecord(AnydataConsumerRecord[] messages, Caller caller) returns error?;
+# This service type attaches to exactly one listener — do not write `on l1, l2`.
+# This listener hosts at most one service in total — any second service, of any type, needs its own listener.
+service kafka:Service on new kafka:Listener(string|string[] bootstrapServers, kafka:ConsumerConfiguration config = {}) {
+    # Invoked with each batch of records polled from the subscribed topics. The listener polls on its configured interval and dispatches everything it received as one batch.
+    # + caller - Handle for committing offsets explicitly. Needed only when auto-commit is disabled.
+    # + records - The polled batch. Declare a narrower element type to project each record's value, see the consumerRecordPayload data-binding rule.
+    # `records` may also be: kafka:BytesConsumerRecord[]
+    # `records` may bind to a batch: anydata[] — but never kafka:AnydataConsumerRecord
+    # `records` may bind to an array of records that include `*kafka:AnydataConsumerRecord;` and override only `value`
+    # The `records` parameter may carry @kafka:Payload, written `@kafka:Payload {}` before its type. Its fields are those of kafka:KafkaPayload.
+    # Required parameters: records
+    # Optional parameters (may be omitted): caller
+    remote function onConsumerRecord(kafka:Caller caller, kafka:AnydataConsumerRecord[] records) returns error?; // required
 
-    # The `onError` remote method will be triggered when an error occurs during the message processing
-    remote function onError(Error kafkaError) returns error?;
+    # Invoked when polling fails, or when a polled batch cannot be dispatched, most commonly because a record's value fails to bind to the declared type.
+    # + err - The failure that prevented the batch from being delivered.
+    remote function onError(kafka:Error err) returns error?; // optional
 }
+
+// --- Annotations ---
+
+# The annotation which is used to define the payload parameter in the `onConsumerRecord` service method.
+public annotation KafkaPayload Payload on parameter;
`````

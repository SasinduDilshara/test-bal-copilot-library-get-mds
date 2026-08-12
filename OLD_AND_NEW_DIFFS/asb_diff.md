# asb — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `asb` |
| **Old file** | `asb/old/ballerinax_asb.bal.txt` |
| **New file** | `asb/new/ballerinax_asb.bal.txt` |
| **Old lines** | 1368 |
| **New lines** | 1699 |
| **Lines added** | 379 |
| **Lines removed** | 48 |
| **Hunks** | 31 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 6 | 6 |

### Declarations added (9)

- `class Listener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `type AdminActionError`
- `type Error`
- `type MessageRetrievalError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 280–365 | 280–399 | Types | +37 | −3 |
| 2 | 368–442 | 402–503 | Types | +27 | −0 |
| 3 | 444–479 | 505–550 | Types | +10 | −0 |
| 4 | 488–501 | 559–577 | Types | +5 | −0 |
| 5 | 508–522 | 584–603 | Types | +5 | −0 |
| 6 | 531–536 | 612–618 | Types | +1 | −0 |
| 7 | 547–552 | 629–635 | Types | +1 | −0 |
| 8 | 557–562 | 640–646 | Types | +1 | −0 |
| 9 | 565–570 | 649–655 | Types | +1 | −0 |
| 10 | 575–580 | 660–666 | Types | +1 | −0 |
| 11 | 583–588 | 669–675 | Types | +1 | −0 |
| 12 | 591–634 | 678–738 | Types | +17 | −0 |
| 13 | 644–711 | 748–843 | Types | +28 | −0 |
| 14 | 714–771 | 846–927 | Types | +24 | −0 |
| 15 | 775–850 | 931–1038 | Types | +32 | −0 |
| 16 | 853–976 | 1041–1218 | Types | +54 | −0 |
| 17 | 1010–1053 | 1252–1349 | Types | +59 | −5 |
| 18 | 1055–1124 | 1351–1430 | Client | +20 | −10 |
| 19 | 1126–1166 | 1432–1478 | Client | +12 | −6 |
| 20 | 1174–1192 | 1486–1505 | Client | +4 | −3 |
| 21 | 1197–1203 | 1510–1516 | Client | +1 | −1 |
| 22 | 1207–1240 | 1520–1557 | Client | +9 | −5 |
| 23 | 1243–1249 | 1560–1567 | Client | +2 | −1 |
| 24 | 1253–1259 | 1571–1578 | Client | +2 | −1 |
| 25 | 1262–1268 | 1581–1588 | Client | +2 | −1 |
| 26 | 1271–1277 | 1591–1598 | Client | +2 | −1 |
| 27 | 1279–1285 | 1600–1607 | Client | +2 | −1 |
| 28 | 1287–1320 | 1609–1647 | Client | +9 | −4 |
| 29 | 1323–1336 | 1650–1663 | Client | +2 | −2 |
| 30 | 1338–1350 | 1665–1679 | Client | +3 | −1 |
| 31 | 1359–1368 | 1688–1699 | Functions | +5 | −3 |

---

## Unified diff

`````diff
--- asb/old/ballerinax_asb.bal.txt	2026-08-12 12:57:30
+++ asb/new/ballerinax_asb.bal.txt	2026-08-12 13:19:19
@@ -280,86 +280,120 @@
 const string BYTE_ARRAY = "application/octet-stream";
 
 # Retry attempts happen at fixed intervals; each delay is a consistent duration.
+@display {label: "Retry on fixed intervals"}
 const string FIXED = "FIXED";
 
 # Retry attempts will delay based on a backoff strategy, where each attempt will increase the duration that it waits before retrying.
+@display {label: "Retry based on a backoff strategy"}
 const string EXPONENTIAL = "EXPONENTIAL";
 
+@display {label: "Queue"}
 const string QUEUE = "queue";
 
+@display {label: "Topic"}
 const string TOPIC = "topic";
 
+@display {label: "RECEIVE AND DELETE"}
 const string RECEIVE_AND_DELETE = "RECEIVE_AND_DELETE";
 
+@display {label: "PEEK LOCK"}
 const string PEEK_LOCK = "PEEK_LOCK";
 
+@display {label: "DEBUG"}
 const string DEBUG = "DEBUG";
 
+@display {label: "INFO"}
 const string INFO = "INFO";
 
+@display {label: "WARNING"}
 const string WARNING = "WARNING";
 
+@display {label: "ERROR"}
 const string ERROR = "ERROR";
 
+@display {label: "FATAL"}
 const string FATAL = "FATAL";
 
+@display {label: "OFF"}
 const string OFF = "OFF";
 
+@display {label: "MANAGE"}
 const string MANAGE = "MANAGE";
 
+@display {label: "SEND"}
 const string SEND = "SEND";
 
+@display {label: "LISTEN"}
 const string LISTEN = "LISTEN";
 
+@display {label: "ACTIVE"}
 const string ACTIVE = "Active";
 
+@display {label: "CREATING"}
 const string CREATING = "Creating";
 
+@display {label: "DELETING"}
 const string DELETING = "Deleting";
 
+@display {label: "DISABLED"}
 const string DISABLED = "Disabled";
 
+@display {label: "RECEIVE_DISABLED"}
 const string RECEIVE_DISABLED = "ReceiveDisabled";
 
+@display {label: "RENAMING"}
 const string RENAMING = "Renaming";
 
+@display {label: "RESTORING"}
 const string RESTORING = "Restoring";
 
+@display {label: "SEND_DISABLED"}
 const string SEND_DISABLED = "SendDisabled";
 
+@display {label: "UNKNOWN"}
 const string UNKNOWN = "Unknown";
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Represents message retrieval error context.
 # 
 
 type ErrorContext record {
     # The entity path of the error source  
+    @display {label: "Entity Path"}
     string entityPath;
     # The name of the originating class    
+    @display {label: "Class Name"}
     string className;
     # The namespace of the error source  
+    @display {label: "Namespace"}
     string namespace;
     # The error source, such as a function or action name   
+    @display {label: "Error Source"}
     string errorSource;
     # The reason for the error
+    @display {label: "Reason"}
     string reason;
 };
 
-// Unknown type: MessageRetrievalError
+# Error type to capture the errors occurred while retrieving messages in Azure service bus listener.
+type MessageRetrievalError Error & error<ErrorContext>;
 
 # Represents admin action error context.
 # 
 
 type AdminErrorContext record {
     # The HTTP status code returned by the ASB Admin API
+    @display {label: "Status code"}
     int statusCode;
     # The reason for the error
+    @display {label: "Reason"}
     string reason;
 };
 
-// Unknown type: AdminActionError
+# Error type to capture errors while executing the administrator actions
+type AdminActionError Error & error<AdminErrorContext>;
 
 # The ASB service type.
 class Service {
@@ -368,75 +402,102 @@
 # Azure service bus message batch representation.
 # 
 
+@display {label: "Batch Message"}
 type MessageBatch record {
     # Number of messages in a batch  
+    @display {label: "Message Count"}
     int messageCount?;
     # Array of Azure service bus message representation (Array of Message records)
+    @display {label: "Array of Messages"}
     Message[] messages?;
 };
 
 # Azure service bus Message representation.
 # 
 
+@display {label: "Message"}
 type Message record {
     # Message body, Here the connector supports AMQP message body types - DATA and VALUE, However, DATA type message bodies  
 will be received in Ballerina Byte[] type. VALUE message bodies can be any primitive AMQP type. therefore, the connector  
 supports for string, int or byte[]. Please refer Azure docs (https://learn.microsoft.com/en-us/java/api/com.azure.core.amqp.models.amqpmessagebody?view=azure-java-stable)  
 and AMQP docs (https://qpid.apache.org/amqp/type-reference.html#PrimitiveTypes)  
+    @display {label: "Message Body"}
     anydata body;
     # Message content type, with a descriptor following the format of `RFC2045`, (e.g. `application/json`) (optional)
+    @display {label: "Content Type"}
     string contentType?;
     # Message Id (optional)  
+    @display {label: "Message Id"}
     string messageId?;
     # Message to (optional)  
+    @display {label: "To"}
     string to?;
     # Message reply to (optional)  
+    @display {label: "Reply To"}
     string replyTo?;
     # Identifier of the session to reply to (optional)  
+    @display {label: "Reply To Session Id"}
     string replyToSessionId?;
     # Message label (optional)  
+    @display {label: "Label"}
     string label?;
     # Message session Id (optional)  
+    @display {label: "Session Id"}
     string sessionId?;
     # Message correlationId (optional)  
+    @display {label: "Correlation Id"}
     string correlationId?;
     # Message partition key (optional)  
+    @display {label: "Partition Key"}
     string partitionKey?;
     # Message time to live in seconds (optional)  
+    @display {label: "Time To Live"}
     int timeToLive?;
     # Message sequence number (optional)  
+    @display {label: "Sequence Number"}
     int sequenceNumber?;
     # Message lock token (optional)  
+    @display {label: "Lock Token"}
     string lockToken?;
     # Message broker application specific properties (optional)  
     ApplicationProperties applicationProperties?;
     # Number of times a message has been delivered in a queue/subscription  
+    @display {label: "Delivery Count"}
     int deliveryCount?;
     # Timestamp indicating when a message was added to the queue/subscription 
+    @display {label: "Enqueued Time"}
     string enqueuedTime?;
     # Sequence number assigned to a message when it is added to the queue/subscription 
+    @display {label: "Enqueued SequenceNumber"}
     int enqueuedSequenceNumber?;
     # Error description of why a message went to a dead-letter queue  
+    @display {label: "DeadLetter Error Description"}
     string deadLetterErrorDescription?;
     # Reason why a message was moved to a dead-letter queue  
+    @display {label: "DeadLetter Reason"}
     string deadLetterReason?;
     # Original queue/subscription where the message was before being moved to the dead-letter queue 
+    @display {label: "DeadLetter Source"}
     string deadLetterSource?;
     # Current state of a message in the queue/subscription, could be "Active", "Scheduled", "Deferred", etc.
+    @display {label: "Message State"}
     string state?;
 };
 
 # Azure service bus message, application specific properties representation.
 # 
 
+@display {label: "Application Properties"}
 type ApplicationProperties record {
     # Key-value pairs for each brokered property (optional)
+    @display {label: "Properties"}
     map<anydata> properties?;
 };
 
 # Configurations used to create an `asb:Connection`.
 # 
 
+@display {label: "Receiver Connection Config"}
 type ASBServiceReceiverConfig record {
     # Service bus connection string with Shared Access Signatures  
 ConnectionString format:
@@ -444,36 +505,46 @@
 SharedAccessKeyName=SHARED_ACCESS_KEY_NAME;SharedAccessKey=SHARED_ACCESS_KEY or
 Endpoint=sb://namespace_DNS_Name;EntityPath=EVENT_HUB_NAME;
 SharedAccessSignatureToken=SHARED_ACCESS_SIGNATURE_TOKEN
+    @display {label: "ConnectionString"}
     string connectionString;
     # This field holds the configuration details of either a topic or a queue. The type of the entity is
 determined by the entityType field. The actual configuration details are stored in either a
 TopicSubsConfig or a QueueConfig record
+    @display {label: "Entity Configuration"}
     TopicSubsConfig|QueueConfig entityConfig;
     # This field holds the receive modes(RECEIVE_AND_DELETE/PEEK_LOCK) for the connection. The receive mode determines how messages are 
 retrieved from the entity. The default value is PEEK_LOCK  
+    @display {label: "Receive Mode"}
     ReceiveMode receiveMode?;
     # Max lock renewal duration under PEEK_LOCK mode in seconds. Setting to 0 disables auto-renewal. 
 For RECEIVE_AND_DELETE mode, auto-renewal is disabled. Default 300 seconds.
+    @display {label: "Max Auto Lock Renew Duration"}
     int maxAutoLockRenewDuration?;
     # Retry configurations related to underlying AMQP message receiver
+    @display {label: "AMQP retry configurations"}
     AmqpRetryOptions amqpRetryOptions?;
 };
 
 # This record holds the configuration details of a topic and its associated subscription in Azure Service Bus.
 # 
 
+@display {label: "Topic/Subscriptions Configurations"}
 type TopicSubsConfig record {
     # A string field that holds the name of the topic  
+    @display {label: "Topic Name"}
     string topicName;
     # A string field that holds the name of the subscription associated with the topic
+    @display {label: "Subscription Name"}
     string subscriptionName;
 };
 
 # This record holds the configuration details of a queue in Azure Service Bus.
 # 
 
+@display {label: "Queue Configurations"}
 type QueueConfig record {
     # A string field that holds the name of the queue
+    @display {label: "Queue Name"}
     string queueName;
 };
 
@@ -488,14 +559,19 @@
 
 type AmqpRetryOptions record {
     # Maximum number of retry attempts  
+    @display {label: "Max retry attempts"}
     int maxRetries?;
     # Delay between retry attempts in seconds 
+    @display {label: "Duration between retries"}
     decimal delay?;
     # Maximum permissible delay between retry attempts in seconds
+    @display {label: "Maximum duration between retries"}
     decimal maxDelay?;
     # Maximum duration to wait for completion of a single attempt in seconds  
+    @display {label: "Timeout duration for retry attempt"}
     decimal tryTimeout?;
     # Approach to use for calculating retry delays
+    @display {label: "Approach to calculated the retry"}
     AmqpRetryMode retryMode?;
 };
 
@@ -508,15 +584,20 @@
 # Holds the configuration details needed to create a sender connection to Azure Service Bus.
 # 
 
+@display {label: "Sender Connection Config"}
 type ASBServiceSenderConfig record {
     # An enumeration value of type EntityType, which specifies whether the connection is for a topic or a queue. 
 The valid values are TOPIC and QUEUE
+    @display {label: "EntityType"}
     EntityType entityType;
     # A string field that holds the name of the topic or queue
+    @display {label: "Queue/Topic Name"}
     string topicOrQueueName;
     # A string field that holds the Service Bus connection string with Shared Access Signatures.
+    @display {label: "ConnectionString"}
     string connectionString;
     # Retry configurations related to underlying AMQP message sender
+    @display {label: "AMQP retry configurations"}
     AmqpRetryOptions amqpRetryOptions?;
 };
 
@@ -531,6 +612,7 @@
 
 type CustomConfiguration record {
     # Enables the connector debug log prints (log4j log levels), default: OFF
+    @display {label: "Log Level"}
     LogLevel logLevel?;
 };
 
@@ -547,6 +629,7 @@
 # SQL Rule.
 # 
 
+@display {label: "SQL Rule"}
 type SqlRule record {
     # Represents a filter which is a composition of an expression and an action that is executed in the pub/sub pipeline
     string filter;
@@ -557,6 +640,7 @@
 # Create Rule Options.
 # 
 
+@display {label: "Create Rule Options"}
 type CreateRuleOptions record {
     # Represents a SQL filter which is a composition of an expression and an action that is executed in the pub/sub pipeline
     SqlRule rule?;
@@ -565,6 +649,7 @@
 # Rule Properties.
 # 
 
+@display {label: "Rule Properties"}
 type RuleProperties record {
     # Represents a SQL filter which is a composition of an expression and an action that is executed in the pub/sub pipeline
     SqlRule rule;
@@ -575,6 +660,7 @@
 # Update Rule Options.
 # 
 
+@display {label: "Update Rule Options"}
 type UpdateRuleOptions record {
     # Represents a SQL filter which is a composition of an expression and an action that is executed in the pub/sub pipeline
     SqlRule rule?;
@@ -583,6 +669,7 @@
 # Rule List.
 # 
 
+@display {label: "Rule List"}
 type RuleList record {
     # The list of rules
     RuleProperties[] list;
@@ -591,44 +678,61 @@
 # Create Subscription Options.
 # 
 
+@display {label: "Create Subscription Options"}
 type CreateSubscriptionOptions record {
     # ISO 8601 timeSpan idle interval after which the subscription is automatically deleted
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # Value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # ISO 8601 default message timespan to live value
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # Value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Filter Evaluation Exceptions"}
     boolean deadLetteringOnFilterEvaluationExceptions?;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo?;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward To"}
     string forwardTo?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes
+    @display {label: "Lock Duration"}
     Duration lockDuration?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # A value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the subscription
+    @display {label: "User Metadata"}
     string userMetadata?;
 };
 
 # Duration.
 # 
 
+@display {label: "Duration"}
 type Duration record {
     # Seconds
+    @display {label: "Seconds"}
     int seconds?;
     # Nanoseconds
+    @display {label: "Nano Seconds"}
     int nanoseconds?;
 };
 
 # Entity status
+@display {label: "Entity Status"}
 enum EntityStatus {
     UNKNOWN,
     SEND_DISABLED,
@@ -644,68 +748,96 @@
 # SubscriptionProperties.
 # 
 
+@display {label: "Subscription Properties"}
 type SubscriptionProperties record {
     # ISO 8601 timeSpan idle interval after which the subscription is automatically deleted
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle;
     # ISO 8601 default message timespan to live value
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward To"}
     string forwardTo;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes
+    @display {label: "Lock Duration"}
     Duration lockDuration;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status;
     # The name of the subscription
+    @display {label: "Subscription Name"}
     string subscriptionName;
     # The name of the topic under which subscription exists
+    @display {label: "Topic Name"}
     string topicName;
     # Metadata associated with the subscription
+    @display {label: "User Metadata"}
     string userMetadata;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations;
     # A value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Filter Evaluation Exceptions"}
     boolean deadLetteringOnFilterEvaluationExceptions;
     # A value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration;
     # A value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession;
 };
 
 # Update Subscription Options.
 # 
 
+@display {label: "Update Subscription Options"}
 type UpdateSubscriptionOptions record {
     # ISO 8601 timeSpan idle interval after which the subscription is automatically deleted
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # ISO 8601 default message timespan to live value
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # Value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # Value that indicates whether this subscription has dead letter support when a message expires
+    @display {label: "Dead Lettering On Filter Evaluation Exceptions"}
     boolean deadLetteringOnFilterEvaluationExceptions?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo?;
     # The name of the recipient entity to which all the messages sent to the subscription are forwarded to
+    @display {label: "Forward To"}
     string forwardTo?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes
+    @display {label: "Lock Duration"}
     Duration lockDuration?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the subscription
+    @display {label: "User Metadata"}
     string userMetadata?;
 };
 
 # Subscription List.
 # 
 
+@display {label: "Subscription List"}
 type SubscriptionList record {
     # The list of subscriptions
     SubscriptionProperties[] list;
@@ -714,58 +846,82 @@
 # TopicProperties.
 # 
 
+@display {label: "Topic Properties"}
 type TopicProperties record {
     # The name of the topic to create
+    @display {label: "Name"}
     string name;
     # Authorization rules for resource
+    @display {label: "Authorization Rules"}
     AuthorizationRule[] authorizationRules;
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning;
     # Defines whether ordering needs to be maintained
+    @display {label: "Support Ordering"}
     boolean supportOrdering;
 };
 
 # AuthorizationRule.
 # 
 
+@display {label: "Authorization Rule"}
 type AuthorizationRule record {
     # The rights associated with the rule
+    @display {label: "Access Rights"}
     AccessRight[] accessRights;
     # The type of the claim
+    @display {label: "Claim Type"}
     string claimType;
     # The value of the claim
+    @display {label: "Claim Value"}
     string claimValue;
     # The exact time the rule was created
+    @display {label: "Created At"}
     string createdAt;
     # The name of the key that was used
+    @display {label: "Key Name"}
     string keyName;
     # The exact time the rule was modified
+    @display {label: "Modified At"}
     string modifiedAt;
     # The primary key associated with the rule
+    @display {label: "Primary Key"}
     string primaryKey;
     # The secondary key associated with the rule
+    @display {label: "Secondary Key"}
     string secondaryKey;
 };
 
 # Access rights
+@display {label: "Access Rights"}
 enum AccessRight {
     LISTEN,
     SEND,
@@ -775,76 +931,108 @@
 # Create Topic Options.
 # 
 
+@display {label: "Create Topic Options"}
 type CreateTopicOptions record {
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow?;
     # ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
+    @display {label: "Lock Duration"}
     Duration lockDuration?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10.
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # Value that indicates whether this queue has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection?;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning?;
     # Value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession?;
     # Defines whether ordering needs to be maintained
+    @display {label: "Support Ordering"}
     boolean supportOrdering?;
 };
 
 # Upadate Topic Propertise.
 # 
 
+@display {label: "Update Topic Options"}
 type UpdateTopicOptions record {
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10.
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # Value that indicates whether this queue has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection?;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning?;
     # Value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession?;
     # Defines whether ordering needs to be maintained
+    @display {label: "Support Ordering"}
     boolean supportOrdering?;
 };
 
 # Topic List
 # 
 
+@display {label: "Topic List"}
 type TopicList record {
     # The list of topics.
     TopicProperties[] list;
@@ -853,124 +1041,178 @@
 # # QueueProperties.
 # 
 
+@display {label: "Queue Properties"}
 type QueueProperties record {
     # Authorization rules for resource
+    @display {label: "Authorization Rules"}
     AuthorizationRule[] authorizationRules;
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow;
     # The name of the recipient entity to which all the dead-lettered messages of this subscription are forwarded to.
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo;
     # The name of the recipient entity to which all the messages sent to the queue are forwarded to.
+    @display {label: "Forward To"}
     string forwardTo;
     # ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
+    @display {label: "Lock Duration"}
     Duration lockDuration;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10.
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes;
     # The name of the queue to create
+    @display {label: "Name"}
     string name;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations;
     # Value that indicates whether this queue has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning;
     # Value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession;
 };
 
 # Create Queue Options.
 # 
 
+@display {label: "Create Queue Options"}
 type CreateQueueOptions record {
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow?;
     # The name of the recipient entity to which all the dead-lettered messages of this subscription are forwarded to.
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo?;
     # The name of the recipient entity to which all the messages sent to the queue are forwarded to
+    @display {label: "Forward To"}
     string forwardTo?;
     # ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
+    @display {label: "Lock Duration"}
     Duration lockDuration?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10.
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # Value that indicates whether this queue has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection?;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning?;
     # Value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession?;
 };
 
 # Update Queue Options.
 # 
 
+@display {label: "Update Queue Options"}
 type UpdateQueueOptions record {
     # ISO 8601 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
+    @display {label: "Auto Delete On Idle"}
     Duration autoDeleteOnIdle?;
     # ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus.
+    @display {label: "Default Message Time To Live"}
     Duration defaultMessageTimeToLive?;
     # ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
+    @display {label: "Duplicate Detection History Time Window"}
     Duration duplicateDetectionHistoryTimeWindow?;
     # The name of the recipient entity to which all the dead-lettered messages of this subscription are forwarded to.
+    @display {label: "Forward Dead Lettered Messages To"}
     string forwardDeadLetteredMessagesTo?;
     # The name of the recipient entity to which all the messages sent to the queue are forwarded to
+    @display {label: "Forward To"}
     string forwardTo?;
     # ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
+    @display {label: "Lock Duration"}
     Duration lockDuration?;
     # The maximum delivery count. A message is automatically deadlettered after this number of deliveries. Default value is 10.
+    @display {label: "Max Delivery Count"}
     int maxDeliveryCount?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Message Size In Kilobytes"}
     int maxMessageSizeInKilobytes?;
     # The maximum size of the queue in megabytes, which is the size of memory allocated for the queue
+    @display {label: "Max Size In Megabytes"}
     int maxSizeInMegabytes?;
     # Enumerates the possible values for the status of a messaging entity
+    @display {label: "Status"}
     EntityStatus status?;
     # Metadata associated with the queue
+    @display {label: "User Metadata"}
     string userMetadata?;
     # Value that indicates whether server-side batched operations are enabled
+    @display {label: "Enable Batched Operations"}
     boolean enableBatchedOperations?;
     # Value that indicates whether this queue has dead letter support when a message expires
+    @display {label: "Dead Lettering On Message Expiration"}
     boolean deadLetteringOnMessageExpiration?;
     # Value indicating if this queue requires duplicate detection
+    @display {label: "Requires Duplicate Detection"}
     boolean requiresDuplicateDetection?;
     # Value that indicates whether the queue is to be partitioned across multiple message brokers
+    @display {label: "Enable Partitioning"}
     boolean enablePartitioning?;
     # Value that indicates whether the queue supports the concept of sessions
+    @display {label: "Requires Session"}
     boolean requiresSession?;
 };
 
 # Queue List.
 # 
 
+@display {label: "Queue List"}
 type QueueList record {
     # The list of queues
     QueueProperties[] list;
@@ -1010,44 +1252,98 @@
 
 type Options record {
     # Enables the connector debug log prints (log4j log levels), default: OFF
+    @display {label: "Log Level"}
     LogLevel logLevel?;
 };
 
-// Unknown type: Listener
+# Creates a new `asb:Listener`.
+# ```ballerina
+# listener asb:Listener asbListener = check new (
+#   connectionString = "xxxxxxxx",
+#   entityConfig = {
+#       queueName: "test-queue"
+#   },
+#   autoComplete = false
+# );
+# ```
+# 
+class Listener {
+    function init(string connectionString = "", TopicSubsConfig|QueueConfig entityConfig = {topicName: "", subscriptionName: ""}, ReceiveMode receiveMode = "PEEK_LOCK", int maxAutoLockRenewDuration = 0, AmqpRetryOptions amqpRetryOptions = {}, boolean autoComplete = true, int prefetchCount = 0, int maxConcurrency = 1, ListenerConfiguration config) returns Error?;
 
+    # Attaches an `asb:Service` to a listener.
+    # ```ballerina
+    # check asbListener.attach(asbService);
+    # ```
+    # 
+    function attach(Service 'service, string[]|string|() name = ()) returns Error|();
+
+    # Detaches an `asb:Service` from the the listener.
+    # ```ballerina
+    # check asbListener.detach(asbService);
+    # ```
+    # 
+    function detach(Service 'service) returns Error|();
+
+    # Starts the `asb:Listener`.
+    # ```ballerina
+    # check asbListener.'start();
+    # ```
+    # 
+    function 'start() returns Error|();
+
+    # Stops the `asb:Listener` gracefully.
+    # ```ballerina
+    # check asbListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns Error|();
+
+    # Stops the `asb:Listener` immediately.
+    # ```ballerina
+    # check asbListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns Error|();
+}
+
 // --- Client ---
 
 # Ballerina Service Bus connector provides the capability to access Azure Service Bus SDK.
 # Service Bus API provides data access to highly reliable queues and publish/subscribe topics of Azure Service Bus with deep feature capabilities.
+@display {label: "Azure Service Bus Administrator", iconPath: "icon.png"}
 client class Administrator {
-    function init(string connectionString) returns ballerinax/asb:3.10.0:Error?;
+    function init(@display {label: "Azure Service Bus connection string"} string connectionString) returns Error?;
 
     # Create a topic with the given name or name and options.
     # ```ballerina
     # asb:TopicProperties? topicProperties = check admin->createTopic("topic-1");
     # ```
     # 
-    remote function createTopic(string topicName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, boolean supportOrdering = false, anydata Additional Values, CreateTopicOptions topicOptions) returns TopicProperties|Error|();
+    @display {label: "Create Topic"}
+    remote function createTopic(@display {label: "Topic"} string topicName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, boolean supportOrdering = false, @display {label: "Topic Options"} CreateTopicOptions topicOptions) returns TopicProperties|Error|();
 
     # Get the topic with the given name.
     # ```ballerina
     # asb:TopicProperties? topicProperties = check admin->getTopic("topic-1");
     # ```
     # 
-    remote function getTopic(string topicName) returns TopicProperties|Error|();
+    @display {label: "Get Topic"}
+    remote function getTopic(@display {label: "Topic"} string topicName) returns TopicProperties|Error|();
 
     # Update the topic with the given options.
     # ```ballerina
     # asb:TopicProperties? topicProp = check admin->updateTopic("topic-1", supportOrdering = true);
     # ```
     # 
-    remote function updateTopic(string topicName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, boolean supportOrdering = false, anydata Additional Values, UpdateTopicOptions topicOptions) returns TopicProperties|Error|();
+    @display {label: "Update Topics"}
+    remote function updateTopic(@display {label: "Topic"} string topicName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, boolean supportOrdering = false, @display {label: "Update Topic Options"} UpdateTopicOptions topicOptions) returns TopicProperties|Error|();
 
     # List the topics.
     # ```ballerina
     # asb:TopicList? topics = check admin->listTopics();
     # ```
     # 
+    @display {label: "List Topics"}
     remote function listTopics() returns TopicList|Error|();
 
     # Delete the topic with the given name.
@@ -1055,70 +1351,80 @@
     # check admin->deleteTopic("topic-1");
     # ```
     # 
-    remote function deleteTopic(string topicName) returns Error|();
+    @display {label: "Delete Topic"}
+    remote function deleteTopic(@display {label: "Topic"} string topicName) returns Error|();
 
     # Create a subscription with the given name or name and options.
     # ```ballerina
     # asb:SubscriptionProperties? subscriptionProperties = check admin->createSubscription("topic-1", "sub-a");
     # ```
     # 
-    remote function createSubscription(string topicName, string subscriptionName, Duration autoDeleteOnIdle = {}, boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, Duration defaultMessageTimeToLive = {}, boolean deadLetteringOnFilterEvaluationExceptions = false, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, boolean requiresSession = false, EntityStatus status = "Unknown", string userMetadata = "", anydata Additional Values, CreateSubscriptionOptions subscriptionOptions) returns SubscriptionProperties|Error|();
+    @display {label: "Create Subscription"}
+    remote function createSubscription(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, Duration autoDeleteOnIdle = {}, boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, Duration defaultMessageTimeToLive = {}, boolean deadLetteringOnFilterEvaluationExceptions = false, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, boolean requiresSession = false, EntityStatus status = "Unknown", string userMetadata = "", @display {label: "Subscription Options"} CreateSubscriptionOptions subscriptionOptions) returns SubscriptionProperties|Error|();
 
     # Get the subscription with the given name.
     # ```ballerina
     # asb:SubscriptionProperties? subscriptionProperties = check admin->getSubscription("topic-1", "sub-a");
     # ```
     # 
-    remote function getSubscription(string topicName, string subscriptionName) returns SubscriptionProperties|Error|();
+    @display {label: "Get Subscription"}
+    remote function getSubscription(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName) returns SubscriptionProperties|Error|();
 
     # Update the subscription with the given options.
     # ```ballerina
     # asb:SubscriptionProperties? subProp = check admin->updateSubscription("topic-1", "sub-a", maxDeliveryCount = 10);
     # ```
     # 
-    remote function updateSubscription(string topicName, string subscriptionName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, boolean deadLetteringOnMessageExpiration = false, boolean deadLetteringOnFilterEvaluationExceptions = false, boolean enableBatchedOperations = false, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, EntityStatus status = "Unknown", string userMetadata = "", anydata Additional Values, UpdateSubscriptionOptions subscriptionOptions) returns SubscriptionProperties|Error|();
+    @display {label: "Update Subscription"}
+    remote function updateSubscription(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, boolean deadLetteringOnMessageExpiration = false, boolean deadLetteringOnFilterEvaluationExceptions = false, boolean enableBatchedOperations = false, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, EntityStatus status = "Unknown", string userMetadata = "", @display {label: "Update Subscription Options"} UpdateSubscriptionOptions subscriptionOptions) returns SubscriptionProperties|Error|();
 
     # List the subscriptions.
     # ```ballerina
     # asb:SubscriptionList? subscriptions = check admin->listSubscriptions("topic-1");
     # ```
     # 
-    remote function listSubscriptions(string topicName) returns SubscriptionList|Error|();
+    @display {label: "List Subscriptions"}
+    remote function listSubscriptions(@display {label: "Topic"} string topicName) returns SubscriptionList|Error|();
 
     # Delete the subscription with the given name.
     # ```ballerina
     # check admin->deleteSubscription("topic-1", "sub-a");
     # ```
     # 
-    remote function deleteSubscription(string topicName, string subscriptionName) returns Error|();
+    @display {label: "Delete Subscription"}
+    remote function deleteSubscription(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName) returns Error|();
 
     # Get the status of existance of a topic with the given name.
     # ```ballerina
     # boolean exists = check admin->topicExists("topic-1");
     # ```
     # 
-    remote function topicExists(string topicName) returns boolean|Error|();
+    @display {label: "is Topic Exists"}
+    remote function topicExists(@display {label: "Exists"} string topicName) returns boolean|Error|();
 
     # Get the status of existance of a subscription with the given name.
     # ```ballerina
     # boolean exists = check admin->subscriptionExists("topic-1", "sub-a");
     # ```
     # 
-    remote function subscriptionExists(string topicName, string subscriptionName) returns boolean|Error|();
+    @display {label: "is Subscription Exists"}
+    remote function subscriptionExists(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName) returns boolean|Error|();
 
     # Create a rule with the given name or name and options.
     # ```ballerina
     # asb:RuleProperties? properties = check admin->createRule("topic-1", "sub-a", "rule-1");
     # ```
     # 
-    remote function createRule(string topicName, string subscriptionName, string ruleName, SqlRule rule = {filter: "", action: ""}, anydata Additional Values, CreateRuleOptions ruleOptions) returns RuleProperties|Error|();
+    @display {label: "Create Rule"}
+    remote function createRule(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, @display {label: "Rule"} string ruleName, SqlRule rule = {filter: "", action: ""}, @display {label: "Rule Options"} CreateRuleOptions ruleOptions) returns RuleProperties|Error|();
 
     # Get the rule with the given name.
     # ```ballerina
     # asb:RuleProperties? properties = check admin->getRule("topic-1", "sub-a", "rule-1");
     # ```
     # 
-    remote function getRule(string topicName, string subscriptionName, string ruleName) returns RuleProperties|Error|();
+    @display {label: "Get Rule"}
+    remote function getRule(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, @display {label: "Rule"} string ruleName) returns RuleProperties|Error|();
 
     # Update the rule with the options.
     # ```ballerina
@@ -1126,41 +1432,47 @@
     # asb:RuleProperties? ruleProperties = check admin->updateRule("topic-1", "sub-a", "rule-1", rule = rule);
     # ```
     # 
-    remote function updateRule(string topicName, string subscriptionName, string ruleName, SqlRule rule = {filter: "", action: ""}, anydata Additional Values, UpdateRuleOptions ruleOptions) returns RuleProperties|Error|();
+    @display {label: "Update Rule"}
+    remote function updateRule(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, @display {label: "Rule"} string ruleName, SqlRule rule = {filter: "", action: ""}, @display {label: "Update Rule Options"} UpdateRuleOptions ruleOptions) returns RuleProperties|Error|();
 
     # List the rules.
     # ```ballerina
     # asb:RuleList? rules = check admin->listRules("topic-1", "sub-a");
     # ```
     # 
-    remote function listRules(string topicName, string subscriptionName) returns RuleList|Error|();
+    @display {label: "List Rules"}
+    remote function listRules(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName) returns RuleList|Error|();
 
     # Delete the rule with the given name.
     # ```ballerina
     # check admin->deleteRule("topic-1", "sub-a", "rule-1");
     # ```
-    remote function deleteRule(string topicName, string subscriptionName, string ruleName) returns Error|();
+    @display {label: "Delete Rule"}
+    remote function deleteRule(@display {label: "Topic"} string topicName, @display {label: "Subscription"} string subscriptionName, @display {label: "Rule"} string ruleName) returns Error|();
 
     # Create a queue with the given name or name and options.
     # ```ballerina
     # asb:QueueProperties queueProperties = check admin->createQueue("queue-1");
     # ```
     # 
-    remote function createQueue(string queueName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, anydata Additional Values, CreateQueueOptions queueOptions) returns QueueProperties|Error|();
+    @display {label: "Create Queue"}
+    remote function createQueue(@display {label: "Queue"} string queueName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, @display {label: "Queue Options"} CreateQueueOptions queueOptions) returns QueueProperties|Error|();
 
     # Get the queue with the given name.
     # ```ballerina
     # asb:QueueProperties? queueProperties = check admin->getQueue("queue-1");
     # ```
     # 
-    remote function getQueue(string queueName) returns QueueProperties|Error|();
+    @display {label: "Get Queue"}
+    remote function getQueue(@display {label: "Queue"} string queueName) returns QueueProperties|Error|();
 
     # Update the queue with the options.
     # ```ballerina
     # asb:QueueProperties? queueProperties = check admin->updateQueue("queue-1", maxDeliveryCount = 10);
     # ```
     # 
-    remote function updateQueue(string queueName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, anydata Additional Values, UpdateQueueOptions queueOptions) returns QueueProperties|Error|();
+    @display {label: "Update Queue"}
+    remote function updateQueue(@display {label: "Queue"} string queueName, Duration autoDeleteOnIdle = {}, Duration defaultMessageTimeToLive = {}, Duration duplicateDetectionHistoryTimeWindow = {}, string forwardDeadLetteredMessagesTo = "", string forwardTo = "", Duration lockDuration = {}, int maxDeliveryCount = 0, int maxMessageSizeInKilobytes = 0, int maxSizeInMegabytes = 0, EntityStatus status = "Unknown", string userMetadata = "", boolean enableBatchedOperations = false, boolean deadLetteringOnMessageExpiration = false, boolean requiresDuplicateDetection = false, boolean enablePartitioning = false, boolean requiresSession = false, @display {label: "Update Queue Options"} UpdateQueueOptions queueOptions) returns QueueProperties|Error|();
 
     # List the queues.
     # ```ballerina
@@ -1174,19 +1486,20 @@
     # check admin->deleteQueue("queue-1");
     # ```
     # 
-    remote function deleteQueue(string queueName) returns Error|();
+    @display {label: "Delete Queue"}
+    remote function deleteQueue(@display {label: "Queue"} string queueName) returns Error|();
 
     # Check whether the queue exists.
     # ```ballerina
     # boolean exists = check admin->queueExists("queue-1");
     # ```
     # 
-    remote function queueExists(string queueName) returns boolean|Error|();
+    @display {label: "is Queue Exists"}
+    remote function queueExists(@display {label: "Exists"} string queueName) returns boolean|Error|();
 }
 
 # Represents a ASB caller, which can be used to mark messages as complete, abandon, deadLetter, or defer.
 client class Caller {
-    function init() returns ballerinax/asb:asb:Caller;
 
     # Complete message from queue or subscription based on messageLockToken. Declares the message processing to be 
     # successfully completed, removing the message from the queue.
@@ -1197,7 +1510,7 @@
     # the time being, returning the message immediately back to the queue to be picked up by another (or the same) 
     # receiver.
     # 
-    remote function abandon(anydata Additional Values, record {|anydata...;|} propertiesToModify) returns Error|();
+    remote function abandon(record {|anydata...;|} propertiesToModify) returns Error|();
 
     # Dead-Letter the message & moves the message to the Dead-Letter Queue based on messageLockToken. Transfer 
     # the message from the primary queue into a special "dead-letter sub-queue".
@@ -1207,34 +1520,38 @@
     # Defer the message in a Queue or Subscription based on messageLockToken.  It prevents the message from being 
     # directly received from the queue by setting it aside such that it must be received by sequence number.
     # 
-    remote function defer(anydata Additional Values, record {|anydata...;|} propertiesToModify) returns Error|();
+    remote function defer(record {|anydata...;|} propertiesToModify) returns Error|();
 }
 
 # Ballerina Service Bus connector provides the capability to access Azure Service Bus SDK.
 # Service Bus API provides data access to highly reliable queues and publish/subscribe topics of Azure Service Bus with deep feature capabilities.
+@display {label: "Azure Service Bus Message Receiver", iconPath: "icon.png"}
 client class MessageReceiver {
-    function init(ASBServiceReceiverConfig config) returns ballerinax/asb:3.10.0:Error?;
+    function init(ASBServiceReceiverConfig config) returns Error?;
 
     # Receive message from queue or subscription.
     # ```ballerina
     # asb:Message? message = check receiver->receive();
     # ```
     # 
-    remote function receive(int|() serverWaitTime = (), Message T = asb:Message, boolean deadLettered = false) returns T|Error|();
+    @display {label: "Receive Message"}
+    remote function receive(@display {label: "Server Wait Time"} int|() serverWaitTime = (), @display {label: "Expected Type"} Message T = asb:Message, @display {label: "Dead-Lettered Messages"} boolean deadLettered = false) returns T|Error|();
 
     # Receive message payload from queue or subscription.
     # ```ballerina
     # string messagePayload = check receiver->receivePayload();
     # ```
     # 
-    remote function receivePayload(int|() serverWaitTime = (), anydata T = anydata, boolean deadLettered = false) returns T|Error;
+    @display {label: "Receive Message Payload"}
+    remote function receivePayload(@display {label: "Server Wait Time"} int|() serverWaitTime = (), @display {label: "Expected Type"} anydata T = anydata, @display {label: "Dead-Lettered Messages"} boolean deadLettered = false) returns T|Error;
 
     # Receive batch of messages from queue or subscription.
     # ```ballerina
     # asb:MessageBatch batch = check receiver->receiveBatch(10);
     # ```
     # 
-    remote function receiveBatch(int maxMessageCount, int|() serverWaitTime = (), boolean deadLettered = false) returns MessageBatch|Error|();
+    @display {label: "Receive Batch Message"}
+    remote function receiveBatch(@display {label: "Maximum Message Count"} int maxMessageCount, @display {label: "Server Wait Time"} int|() serverWaitTime = (), @display {label: "Dead-Lettered Messages"} boolean deadLettered = false) returns MessageBatch|Error|();
 
     # Complete message from queue or subscription based on messageLockToken. Declares the message processing to be 
     # successfully completed, removing the message from the queue.
@@ -1243,7 +1560,8 @@
     # check receiver->complete(message);
     # ```
     # 
-    remote function complete(Message message) returns Error|();
+    @display {label: "Complete Message"}
+    remote function complete(@display {label: "Message"} Message message) returns Error|();
 
     # Abandon message from queue or subscription based on messageLockToken. Abandon processing of the message for 
     # the time being, returning the message immediately back to the queue to be picked up by another (or the same) 
@@ -1253,7 +1571,8 @@
     # check receiver->abandon(message);
     # ```
     # 
-    remote function abandon(Message message) returns Error|();
+    @display {label: "Abandon Message"}
+    remote function abandon(@display {label: "Message"} Message message) returns Error|();
 
     # Dead-Letter the message & moves the message to the Dead-Letter Queue based on messageLockToken. Transfer 
     # the message from the primary queue into a special "dead-letter sub-queue".
@@ -1262,7 +1581,8 @@
     # check receiver->deadLetter(message);
     # ```
     # 
-    remote function deadLetter(Message message, string deadLetterReason = "", string|() deadLetterErrorDescription = ()) returns Error|();
+    @display {label: "Dead Letter Message"}
+    remote function deadLetter(@display {label: "Message"} Message message, @display {label: "Dead Letter Reason"} string deadLetterReason = "", @display {label: "Dead Letter Description"} string|() deadLetterErrorDescription = ()) returns Error|();
 
     # Defer the message in a Queue or Subscription based on messageLockToken.  It prevents the message from being 
     # directly received from the queue by setting it aside such that it must be received by sequence number.
@@ -1271,7 +1591,8 @@
     # int sequenceNumber = check receiver->defer(message);
     # ```
     # 
-    remote function defer(Message message) returns int|Error;
+    @display {label: "Defer Message"}
+    remote function defer(@display {label: "Message"} Message message) returns int|Error;
 
     # Receives a deferred Message. Deferred messages can only be received by using sequence number and return
     # Message object.
@@ -1279,7 +1600,8 @@
     # asb:Message? message = check receiver->receiveDeferred(1);
     # ```
     # 
-    remote function receiveDeferred(int sequenceNumber) returns Message|Error|();
+    @display {label: "Receive Deferred Message"}
+    remote function receiveDeferred(@display {label: "Deferred Msg Seq Num"} int sequenceNumber) returns Message|Error|();
 
     # The operation renews lock on a message in a queue or subscription based on messageLockToken.
     # ```ballerina
@@ -1287,34 +1609,39 @@
     # check receiver->renewLock(message);
     # ```
     # 
-    remote function renewLock(Message message) returns Error|();
+    @display {label: "Renew Lock On Message"}
+    remote function renewLock(@display {label: "Message"} Message message) returns Error|();
 
     # Closes the ASB receiver connection.
     # ```ballerina
     # check receiver->close();
     # ```
     # 
+    @display {label: "Close Receiver Connection"}
     remote function close() returns Error|();
 }
 
 # Ballerina Service Bus connector provides the capability to access Azure Service Bus SDK.
 # Service Bus API provides data access to highly reliable queues and publish/subscribe topics of Azure Service Bus with deep feature capabilities.
+@display {label: "Azure Service Bus Message Sender", iconPath: "icon.png"}
 client class MessageSender {
-    function init(ASBServiceSenderConfig config) returns ballerinax/asb:3.10.0:Error?;
+    function init(ASBServiceSenderConfig config) returns Error?;
 
     # Send message to queue or topic with a message body.
     # ```ballerina
     # check sender->send({body: "Sample text message", contentType: asb:TEXT});
     # ```
     # 
-    remote function send(Message message) returns Error|();
+    @display {label: "Send Message"}
+    remote function send(@display {label: "Message Record"} Message message) returns Error|();
 
     # Send message to queue or topic with a message body.
     # ```ballerina
     # check sender->sendPayload("Sample text message");
     # ```
     # 
-    remote function sendPayload(anydata messagePayload) returns Error|();
+    @display {label: "Send Message Payload"}
+    remote function sendPayload(@display {label: "Message Payload"} anydata messagePayload) returns Error|();
 
     # Sends a scheduled message to the Azure Service Bus entity this sender is connected to. 
     # A scheduled message is enqueued and made available to receivers only at the scheduled enqueue time.
@@ -1323,14 +1650,14 @@
     # check sender->send({body: "Sample text message", contentType: asb:TEXT}, scheduledTime);
     # ```
     # 
-    remote function schedule(Message message, time:Civil scheduledEnqueueTime) returns int|Error; // Special Agent Note: Civil FROM ballerina/time package
+    remote function schedule(@display {label: "Message Record or Payload"} Message message, time:Civil scheduledEnqueueTime) returns int|Error; // Special Agent Note: Civil FROM ballerina/time package
 
     # Cancels the enqueuing of a scheduled message, if they are not already enqueued.
     # ```ballerina
     # check sender->cancel(1);
     # ```
     # 
-    remote function cancel(int sequenceNumber) returns Error|();
+    remote function cancel(@display {label: "Sequence Number"} int sequenceNumber) returns Error|();
 
     # Send batch of messages to queue or topic.
     # ```ballerina
@@ -1338,13 +1665,15 @@
     # check sender->sendBatch(batch);
     # ```
     # 
-    remote function sendBatch(MessageBatch messageBatch) returns Error|();
+    @display {label: "Send Batch Message"}
+    remote function sendBatch(@display {label: "Message Batch"} MessageBatch messageBatch) returns Error|();
 
     # Closes the ASB sender connection.
     # ```ballerina
     # check sender->close();
     # ```
     # 
+    @display {label: "Close Sender Connection"}
     remote function close() returns Error|();
 }
 
@@ -1359,10 +1688,12 @@
 
 // --- Service ---
 
-service asb:Service on new asb:Listener(ListenerConfiguration config = {connectionString: "", entityConfig: {topicName: "", subscriptionName: ""}}) {
+service asb:Service on new asb:Listener(asb:ListenerConfiguration config = {connectionString: "", entityConfig: {topicName: "", subscriptionName: ""}}) {
     # Triggers when new message received for the azure service bus
-    remote function onMessage(Message message) returns error?;
+    # + message - The received message
+    remote function onMessage(asb:Message message) returns error?;
 
     # Triggers when error occurred in the azure service bus
-    remote function onError(MessageRetrievalError asbErr) returns error?;
+    # + asbErr - The messages received for the topic
+    remote function onError(asb:MessageRetrievalError asbErr) returns error?;
 }
`````

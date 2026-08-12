# mongodb — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mongodb` |
| **Old file** | `mongodb/old/ballerinax_mongodb.bal.txt` |
| **New file** | `mongodb/new/ballerinax_mongodb.bal.txt` |
| **Old lines** | 608 |
| **New lines** | 707 |
| **Lines added** | 108 |
| **Lines removed** | 9 |
| **Hunks** | 12 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 6 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type ApplicationError`
- `type DatabaseError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 166–299 | 166–350 | Types | +54 | −3 |
| 2 | 308–319 | 359–374 | Types | +4 | −0 |
| 3 | 321–328 | 376–385 | Types | +2 | −0 |
| 4 | 330–339 | 387–399 | Types | +3 | −0 |
| 5 | 367–402 | 427–478 | Types | +16 | −0 |
| 6 | 404–417 | 480–498 | Types | +5 | −0 |
| 7 | 419–428 | 500–512 | Types | +3 | −0 |
| 8 | 430–441 | 514–529 | Types | +4 | −0 |
| 9 | 468–477 | 556–568 | Types | +3 | −0 |
| 10 | 479–517 | 570–615 | Types | +11 | −4 |
| 11 | 543–549 | 641–647 | Client | +1 | −1 |
| 12 | 587–594 | 685–693 | Client | +2 | −1 |

---

## Unified diff

`````diff
--- mongodb/old/ballerinax_mongodb.bal.txt	2026-08-12 12:57:30
+++ mongodb/new/ballerinax_mongodb.bal.txt	2026-08-12 13:19:19
@@ -166,134 +166,185 @@
     string mongoDBExceptionType;
 };
 
-// Unknown type: DatabaseError
+# Represents an error caused by an issue related to database accessibility, erroneous queries, constraint violations,
+# database resource clean-up, and other similar scenarios.
+type DatabaseError error<DatabaseErrorDetail>;
 
-// Unknown type: ApplicationError
+# Represents an error originating from application-level causes.
+type ApplicationError error;
 
 # Represents a database or application level error returned from the MongoDB client remote functions.
-type Error ballerinax/mongodb:5.2.4:DatabaseError|ballerinax/mongodb:5.2.4:ApplicationError|error;
+type Error DatabaseError|ApplicationError|error;
 
 # Represents the Client configurations for MongoDB.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # connection - Connection string or the connection parameters for the MongoDB connection
+    @display {label: "Connection"}
     ConnectionParameters|string connection;
     # The additional connection options for the MongoDB connection
+    @display {label: "Connection Options"}
     ConnectionProperties options?;
 };
 
 # Represents the MongoDB connection parameters.
 
+@display {label: "Connection Parameters"}
 type ConnectionParameters record {
     # Server address (or the list of server addresses for replica sets) of the MongoDB server
+    @display {label: "Server Address"}
     ServerAddress|ServerAddress[] serverAddress?;
     # The authentication configurations for the MongoDB connection
+    @display {label: "Authentication"}
     BasicAuthCredential|ScramSha1AuthCredential|ScramSha256AuthCredential|X509Credential|GssApiCredential auth?;
 };
 
 # Represents the MongoDB server address.
 
+@display {label: "Server Address"}
 type ServerAddress record {
     # The host address of the MongoDB server
+    @display {label: "Host"}
     string host?;
     # The port of the MongoDB server
+    @display {label: "Port"}
     int port?;
 };
 
 # Represents the Basic Authentication configurations for MongoDB.
 
+@display {label: "Basic Auth Credential"}
 type BasicAuthCredential record {
     # The authentication mechanism to use
+    @display {label: "Auth Mechanism"}
     "PLAIN" authMechanism?;
     # The username for the database connection
+    @display {label: "Username"}
     string username;
     # The password for the database connection
+    @display {label: "Password"}
     string password;
     # The source database for authenticate the client. Usually the database name
+    @display {label: "Auth Source Database"}
     string database;
 };
 
 # Represents the SCRAM-SHA-1 authentication configurations for MongoDB.
 
+@display {label: "SCRAM-SHA-1 Credential"}
 type ScramSha1AuthCredential record {
     # The authentication mechanism to use
+    @display {label: "Auth Mechanism"}
     "SCRAM_SHA_1" authMechanism?;
     # The username for the database connection
+    @display {label: "Username"}
     string username;
     # The password for the database connection
+    @display {label: "Password"}
     string password;
     # The source database for authenticate the client. Usually the database name
+    @display {label: "Auth Source Database"}
     string database;
 };
 
 # Represents the SCRAM-SHA-256 authentication configurations for MongoDB.
 
+@display {label: "SCRAM-SHA-256 Credential"}
 type ScramSha256AuthCredential record {
     # The authentication mechanism to use
+    @display {label: "Auth Mechanism"}
     "SCRAM_SHA_256" authMechanism?;
     # The username for the database connection
+    @display {label: "Username"}
     string username;
     # The password for the database connection
+    @display {label: "Password"}
     string password;
     # The source database for authenticate the client. Usually the database name
+    @display {label: "Auth Source Database"}
     string database;
 };
 
 # Represents the X509 authentication configurations for MongoDB.
 
+@display {label: "X509 Credential"}
 type X509Credential record {
     # The authentication mechanism to use
+    @display {label: "Auth Mechanism"}
     "MONGODB_X509" authMechanism?;
     # The username for authenticating the client certificate
+    @display {label: "Username"}
     string username?;
 };
 
 # Represents the GSSAPI authentication configurations for MongoDB.
 
+@display {label: "GSSAPI Credential"}
 type GssApiCredential record {
     # The authentication mechanism to use
+    @display {label: "Auth Mechanism"}
     "GSSAPI" authMechanism?;
     # The username for the database connection
+    @display {label: "Username"}
     string username;
     # The service name for the database connection. Use this to override the default service name of `mongodb`
+    @display {label: "Service Name"}
     string serviceName?;
 };
 
 # Represents the MongoDB connection pool properties.
 
+@display {label: "Connection Properties"}
 type ConnectionProperties record {
     # The read concern level to use
+    @display {label: "Read Concern"}
     ReadConcern readConcern?;
     # The write concern level to use
+    @display {label: "Write Concern"}
     string writeConcern?;
     # The read preference for the replica set
+    @display {label: "Read Preference"}
     string readPreference?;
     # The replica set name if it is to connect to replicas
+    @display {label: "Replica Set"}
     string replicaSet?;
     # Whether SSL connection is enabled
+    @display {label: "SSL Enabled"}
     boolean sslEnabled?;
     # Whether invalid host names should be allowed
+    @display {label: "SSL Invalid Host Name Allowed"}
     boolean invalidHostNameAllowed?;
     # Configurations related to facilitating secure connection
+    @display {label: "Secure Socket"}
     SecureSocket secureSocket?;
     # Whether to retry writing failures
+    @display {label: "Retry Writes"}
     boolean retryWrites?;
     # The timeout for the socket
+    @display {label: "Socket Timeout"}
     int socketTimeout?;
     # The timeout for the connection
+    @display {label: "Connection Timeout"}
     int connectionTimeout?;
     # The maximum connection pool size
+    @display {label: "Maximum Pool Size"}
     int maxPoolSize?;
     # The maximum idle time for a pooled connection in milliseconds
+    @display {label: "Maximum Idle Time"}
     int maxIdleTime?;
     # The maximum life time for a pooled connection in milliseconds
+    @display {label: "Maximum Life Time"}
     int maxLifeTime?;
     # The minimum connection pool size
+    @display {label: "Minimum Pool Size"}
     int minPoolSize?;
     # The local threshold latency in milliseconds
+    @display {label: "Local Threshold"}
     int localThreshold?;
     # The heartbeat frequency in milliseconds. This is the frequency that the driver will attempt
 to determine the current state of each server in the cluster.
+    @display {label: "Heartbeat Frequency"}
     int heartbeatFrequency?;
 };
 
@@ -308,12 +359,16 @@
 
 # Represents the configurations related to facilitating secure connection.
 
+@display {label: "Secure Socket"}
 type SecureSocket record {
     # Configurations associated with the TrustStore
+    @display {label: "Trust Store"}
     crypto:TrustStore trustStore; // Special Agent Note: TrustStore FROM ballerina/crypto package
     # Configurations associated with the KeyStore
+    @display {label: "Key Store"}
     crypto:KeyStore keyStore; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # The standard name of the requested protocol
+    @display {label: "Protocol"}
     string protocol;
 };
 
@@ -321,8 +376,10 @@
 
 type InsertOneOptions record {
     # The comment to send with the operation
+    @display {label: "Comment"}
     string comment?;
     # Whether to bypass the document validation
+    @display {label: "Bypass Document Validation"}
     boolean bypassDocumentValidation?;
 };
 
@@ -330,10 +387,13 @@
 
 type InsertManyOptions record {
     # The comment to send with the operation
+    @display {label: "Comment"}
     string comment?;
     # Whether to bypass the document validation
+    @display {label: "Bypass Document Validation"}
     boolean bypassDocumentValidation?;
     # Whether to insert documents in the order provided
+    @display {label: "Ordered"}
     boolean ordered?;
 };
 
@@ -367,36 +427,52 @@
 
 type CreateIndexOptions record {
     # Whether to create the index in the background
+    @display {label: "Background"}
     boolean background?;
     # Whether to create a unique index
+    @display {label: "Unique"}
     boolean unique?;
     # Name of the index
+    @display {label: "Index Name"}
     string name?;
     # Should the index only reference documents with the specified field
+    @display {label: "Sparse"}
     boolean sparse?;
     # The time to live for documents in the collection in seconds
+    @display {label: "Time to Live"}
     int expireAfterSeconds?;
     # The version of the index
+    @display {label: "Version"}
     int version?;
     # Sets the weighting object for use with a text index
+    @display {label: "Weights"}
     map<json> weights?;
     # The default language for the index
+    @display {label: "Default Language"}
     string defaultLanguage?;
     # Sets the name of the field that contains the language string
+    @display {label: "Language Override"}
     string languageOverride?;
     # Set the text index version number
+    @display {label: "Text Index Version"}
     int textVersion?;
     # Sets the 2D sphere index version number
+    @display {label: "2D Sphere Index Version"}
     int sphereVersion?;
     # Sets the number of precision of the stored geohash value of the location data in 2D indexes
+    @display {label: "Bits"}
     int bits?;
     # Sets the lower inclusive boundary for the longitude and latitude values for 2D indexes
+    @display {label: "Min"}
     float min?;
     # Sets the upper inclusive boundary for the longitude and latitude values for 2D indexes
+    @display {label: "Max"}
     float max?;
     # Sets the filter expression for the documents to be included in the index
+    @display {label: "Partial Filter Expression"}
     map<json> partialFilterExpression?;
     # Should the index be hidden from the query planner
+    @display {label: "Hidden"}
     boolean hidden?;
 };
 
@@ -404,14 +480,19 @@
 
 type UpdateOptions record {
     # Whether to upsert if the document does not exist
+    @display {label: "Upsert"}
     boolean upsert?;
     # Whether to bypass the document validation
+    @display {label: "Bypass Document Validation"}
     boolean bypassDocumentValidation?;
     # The comment to send with the operation
+    @display {label: "Comment"}
     string comment?;
     # The hint to use
+    @display {label: "Hint"}
     map<json> hint?;
     # The hint string to use
+    @display {label: "Hint String"}
     string hintString?;
 };
 
@@ -419,10 +500,13 @@
 
 type DeleteOptions record {
     # The comment to send with the operation
+    @display {label: "Comment"}
     string comment?;
     # The hint to use
+    @display {label: "Hint"}
     map<json> hint?;
     # The hint string to use
+    @display {label: "Hint String"}
     string hintString?;
 };
 
@@ -430,12 +514,16 @@
 
 type Index record {
     # The name space of the index
+    @display {label: "Name Space"}
     string ns;
     # The index version
+    @display {label: "Version"}
     int v;
     # The name of the index
+    @display {label: "Name"}
     string name;
     # The key of the index
+    @display {label: "Key"}
     map<json> key;
 };
 
@@ -468,10 +556,13 @@
 
 type UpdateResult record {
     # The number of documents matched by the update operation
+    @display {label: "Matched Count"}
     int matchedCount;
     # The number of documents modified by the update operation
+    @display {label: "Modified Count"}
     int modifiedCount;
     # The identifier of the inserted document if the upsert option is used
+    @display {label: "Upserted Id"}
     string upsertedId?;
 };
 
@@ -479,39 +570,46 @@
 
 type DeleteResult record {
     # The number of documents deleted by the delete operation
+    @display {label: "Deleted Count"}
     int deletedCount;
     # Whether the delete operation was acknowledged
+    @display {label: "Acknowledged"}
     boolean acknowledged;
 };
 
 // --- Client ---
 
 # Represents a MongoDB client that can be used to interact with a MongoDB server.
+@display {label: "MongoDB Client", iconPath: "icon.png"}
 client class Client {
-    function init(ConnectionParameters|string connection = {}, ConnectionProperties options = {}, ConnectionConfig config) returns ballerinax/mongodb:5.2.4:Error?;
+    function init(ConnectionParameters|string connection = {}, ConnectionProperties options = {}, ConnectionConfig config) returns Error?;
 
     # Lists the database names in the MongoDB server.
     # 
+    @display {label: "List Database Names"}
     remote function listDatabaseNames() returns string[]|DatabaseError|ApplicationError|error;
 
     # Retrieves a database from the MongoDB server.
     # 
-    remote function getDatabase(string databaseName) returns Database|DatabaseError|ApplicationError|error;
+    @display {label: "Get Database"}
+    remote function getDatabase(@display {label: "Database Name"} string databaseName) returns Database|DatabaseError|ApplicationError|error;
 
     # Closes the client.
     # 
     # > **Note:** Use a single client instance for the lifetime of the application and close it when the application is done.
     # 
+    @display {label: "Close the Client"}
     remote function close() returns DatabaseError|ApplicationError|error|();
 }
 
 # Represents a MongoDB collection that can be used to perform operations on the collection.
+@display {label: "MongoDB Collection"}
 client class Collection {
-    function init(Database database, string collectionName) returns ballerinax/mongodb:5.2.4:Error?;
+    function init(Database database, string collectionName) returns Error?;
 
     # Returns the name of the collection.
     # 
-    remote function name() returns string;
+    function name() returns string;
 
     # Inserts a single document into the collection.
     # 
@@ -543,7 +641,7 @@
     # 
     # > **Note:** Close the resulted stream once the operation is completed.
     # 
-    remote function listIndexes() returns stream<ballerinax/mongodb:5.2.4:Index, error?>|DatabaseError|ApplicationError|error;
+    remote function listIndexes() returns stream<Index, error?>|DatabaseError|ApplicationError|error;
 
     # Drops an index from the collection.
     # 
@@ -587,8 +685,9 @@
 }
 
 # Represents a MongoDB database.
+@display {label: "MongoDB Database"}
 client class Database {
-    function init(Client 'client, string databaseName) returns ballerinax/mongodb:5.2.4:Error?;
+    function init(Client 'client, string databaseName) returns Error?;
 
     # Lists all the collections in the database.
     # 
`````

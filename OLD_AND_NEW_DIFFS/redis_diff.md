# redis — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `redis` |
| **Old file** | `redis/old/ballerinax_redis.bal.txt` |
| **New file** | `redis/new/ballerinax_redis.bal.txt` |
| **Old lines** | 695 |
| **New lines** | 838 |
| **Lines added** | 253 |
| **Lines removed** | 110 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type ConnectionUri`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 130–181 | 130–202 | Types | +23 | −2 |
| 2 | 194–223 | 215–255 | Types | +11 | −0 |
| 3 | 234–667 | 266–805 | Client | +211 | −105 |
| 4 | 671–695 | 809–838 | Client | +8 | −3 |

---

## Unified diff

`````diff
--- redis/old/ballerinax_redis.bal.txt	2026-08-12 12:57:30
+++ redis/new/ballerinax_redis.bal.txt	2026-08-12 13:19:19
@@ -130,52 +130,73 @@
 
 const string FULL = "FULL";
 
-// Unknown type: Error
+# Represents a redis generic error
+type Error error;
 
 # The client endpoint configuration for Redis.
 # 
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Connection configurations of the Redis server. This can be either a single URI or a set of parameters
+    @display {label: "Connection Type"}
     ConnectionUri|ConnectionParams connection?;
     # Flag to indicate whether connection pooling is enabled
+    @display {label: "Connection Pooling Enabled"}
     boolean connectionPooling?;
     # Flag to indicate whether the connection is a cluster connection
+    @display {label: "Cluster Mode Enabled"}
     boolean isClusterConnection?;
     # Configurations related to SSL/TLS encryption
+    @display {label: "Secure Socket Configurations"}
     SecureSocket secureSocket?;
 };
 
-// Unknown type: ConnectionUri
+# The redis Connection URI based configurations. This can become useful when working with 
+# managed Redis databases, where the cloud provider usually provides a connection URI.
+# 
+@display {label: "Connection URI"}
+type ConnectionUri string;
 
 # The connection parameters based configurations.
 # 
 
+@display {label: "Connection Parameters"}
 type ConnectionParams record {
     # Host address of the Redis database  
+    @display {label: "Host"}
     string host?;
     # Port of the Redis database  
+    @display {label: "Port"}
     int port?;
     # The username for the Redis database
+    @display {label: "Username"}
     string username?;
     # The password for the Redis database  
+    @display {label: "Password"}
     string password?;
     # Other connection options of the connection configuration
+    @display {label: "Connection Options"}
     Options options?;
 };
 
 # Connection options for Redis client endpoint.
 # 
 
+@display {label: "Connection Options"}
 type Options record {
     # Name of the client
+    @display {label: "Client Name"}
     string clientName?;
     # Database index which the client should interact with. Not applicable for cluster connections
+    @display {label: "Database Index"}
     int database?;
     # Connection timeout in seconds
+    @display {label: "Connection Timeout"}
     int connectionTimeout?;
     # TCP keep-alive configuration for detecting stale connections.
 Set to `()` (nil) to disable. Default is `()` (disabled).
+    @display {label: "Keep Alive Configuration"}
     KeepAliveConfig|() keepAlive?;
 };
 
@@ -194,30 +215,41 @@
 # Configurations for secure communication with the Redis server.
 # 
 
+@display {label: "Secure Socket Configurations"}
 type SecureSocket record {
     # Configurations associated with `crypto:TrustStore` or single certificate file that the client trusts  
+    @display {label: "Certificate"}
     crypto:TrustStore|string cert?; // Special Agent Note: TrustStore FROM ballerina/crypto package
     # Configurations associated with `crypto:KeyStore` or combination of certificate and private key of the client  
+    @display {label: "Key"}
     crypto:KeyStore|CertKey key?; // Special Agent Note: KeyStore FROM ballerina/crypto package
     # List of protocols used for the connection established to Redis Server, such as TLSv1.2, TLSv1.1, TLSv1.
+    @display {label: "Protocols to be used for the connection to the Redis Server"}
     string[] protocols?;
     # List of ciphers to be used for SSL connections
+    @display {label: "Ciphers"}
     string[] ciphers?;
     # The SSL/TLS verification mode. This can be either NONE, CA, or FULL.
+    @display {label: "Peer Verification Mode"}
     SslVerifyMode verifyMode?;
     # Whether StartTLS is enabled
+    @display {label: "StartTLS Enabled"}
     boolean startTls?;
 };
 
 # Represents a combination of certificate, private key, and private key password if encrypted.
 # 
 
+@display {label: "Certificate Key Configurations"}
 type CertKey record {
     # File containing the certificate
+    @display {label: "Certificate File Path"}
     string certFile;
     # File containing the private key in PKCS8 format
+    @display {label: "Private Key File Path"}
     string keyFile;
     # Password of the private key if it is encrypted
+    @display {label: "Private Key Password"}
     string keyPassword?;
 };
 
@@ -234,434 +266,540 @@
 # Ballerina Redis connector provides the capability to access Redis cache.
 # This connector lets you to perform operations to access and manipulate key-value data stored in a Redis database. 
 # 
+@display {label: "Redis Client", iconPath: "icon.png"}
 client class Client {
-    function init(ConnectionUri|ConnectionParams connection = "redis://localhost:6379", boolean connectionPooling = false, boolean isClusterConnection = false, SecureSocket secureSocket = {}, ConnectionConfig config) returns ballerinax/redis:3.4.1:Error?;
+    function init(ConnectionUri|ConnectionParams connection = "redis://localhost:6379", boolean connectionPooling = false, boolean isClusterConnection = false, SecureSocket secureSocket = {}, ConnectionConfig config) returns Error?;
 
     # Append a value to a key.
     # 
-    remote function append(string key, string value) returns int|Error;
+    @display {label: "Enrich Value"}
+    remote function append(@display {label: "Key"} string key, @display {label: "Value To Append"} string value) returns int|Error;
 
     # Count set bits in a string.
     # 
-    remote function bitCount(string key) returns int|Error;
+    @display {label: "Get Bits of String"}
+    remote function bitCount(@display {label: "Key"} string key) returns int|Error;
 
     # Perform bitwise AND between strings.
     # 
-    remote function bitOpAnd(string destination, string[] keys) returns int|Error;
+    @display {label: "Perform Bitwise AND"}
+    remote function bitOpAnd(@display {label: "Result Key"} string destination, @display {label: "Key Array To Perform AND"} string[] keys) returns int|Error;
 
     # Perform bitwise OR between strings.
     # 
-    remote function bitOpOr(string destination, string[] keys) returns int|Error;
+    @display {label: "Perform Bitwise OR"}
+    remote function bitOpOr(@display {label: "Result Key"} string destination, @display {label: "Key Array to Perform OR"} string[] keys) returns int|Error;
 
     # Perform bitwise NOT on a string.
     # 
-    remote function bitOpNot(string destination, string key) returns int|Error;
+    @display {label: "Perform Bitwise NOT"}
+    remote function bitOpNot(@display {label: "Result Key"} string destination, @display {label: "Key to Perform NOT"} string key) returns int|Error;
 
     # Perform bitwise XOR between strings.
     # 
-    remote function bitOpXor(string destination, string[] keys) returns int|Error;
+    @display {label: "Perform Bitwise XOR"}
+    remote function bitOpXor(@display {label: "Result Key"} string destination, @display {label: "Key Array To Perform XOR"} string[] keys) returns int|Error;
 
     # Decrement integer value of a key by one.
     # 
-    remote function decr(string key) returns int|Error;
+    @display {label: "Decrement(By One)"}
+    remote function decr(@display {label: "Key"} string key) returns int|Error;
 
     # Decrement integer value of a key by the given number.
     # 
-    remote function decrBy(string key, int value) returns int|Error;
+    @display {label: "Decrement (By Number)"}
+    remote function decrBy(@display {label: "Key"} string key, @display {label: "Value To Decrement"} int value) returns int|Error;
 
     # Returns bit value at offset in the string value stored at key.
     # 
-    remote function getBit(string key, int offset) returns int|Error;
+    @display {label: "Get Bit At Offset"}
+    remote function getBit(@display {label: "Key"} string key, @display {label: "Offset"} int offset) returns int|Error;
 
     # Get substring of string stored at a key.
     # 
-    remote function getRange(string key, int startPos, int end) returns string|Error;
+    @display {label: "Get Substring"}
+    remote function getRange(@display {label: "Key"} string key, @display {label: "Start Position"} int startPos, @display {label: "End Position"} int end) returns string|Error;
 
     # Set string value of key and return its existing value.
     # 
-    remote function getSet(string key, string value) returns string|Error|();
+    @display {label: "Get And Set Value"}
+    remote function getSet(@display {label: "Key"} string key, @display {label: "New Value"} string value) returns string|Error|();
 
     # Get value of key.
     # 
-    remote function get(string key) returns string|Error|();
+    @display {label: "Get Value"}
+    remote function get(@display {label: "Key"} string key) returns string|Error|();
 
     # Increment integer value of a key by one.
     # 
-    remote function incr(string key) returns int|Error;
+    @display {label: "Increment (By One)"}
+    remote function incr(@display {label: "Key"} string key) returns int|Error;
 
     # Increment integer value of key by the given amount.
     # 
-    remote function incrBy(string key, int value) returns int|Error;
+    @display {label: "Increment (By Number)"}
+    remote function incrBy(@display {label: "Key"} string key, @display {label: "Increment Value"} int value) returns int|Error;
 
     # Increment integer value of key by the given float.
     # 
-    remote function incrByFloat(string key, float value) returns float|Error;
+    @display {label: "Increment (By Float)"}
+    remote function incrByFloat(@display {label: "Key"} string key, @display {label: "Increment Value"} float value) returns float|Error;
 
     # Get values of all given keys. Fails with an `Error` if any of the given keys does not
     # exist, since the returned type cannot represent a missing value. Use `mGetOptional` instead
     # if any of the given keys might not exist.
     # 
-    remote function mGet(string[] keys) returns string[]|Error;
+    @display {label: "Get Values"}
+    remote function mGet(@display {label: "Keys"} string[] keys) returns string[]|Error;
 
     # Get values of all given keys. Unlike `mGet`, a key that does not exist is represented as
     # `()` in the returned array.
     # 
-    remote function mGetOptional(string[] keys) returns string|()[]|Error;
+    @display {label: "Get Values (Optional)"}
+    remote function mGetOptional(@display {label: "Keys"} string[] keys) returns string|()[]|Error;
 
     # Set multiple keys to multiple values.
     # 
-    remote function mSet(map<any> keyValueMap) returns string|Error;
+    @display {label: "Set Values"}
+    remote function mSet(@display {label: "Key-Value Pair Map"} map<any> keyValueMap) returns string|Error;
 
     # Set multiple keys to multiple values, only if none of the keys exist.
     # 
-    remote function mSetNx(map<any> keyValueMap) returns boolean|Error;
+    @display {label: "Set Values If Absent"}
+    remote function mSetNx(@display {label: "Map of Key Value Pairs"} map<any> keyValueMap) returns boolean|Error;
 
     # Set value and expiration in milliseconds of a key.
     # 
-    remote function pSetEx(string key, string value, int expirationTime) returns string|Error;
+    @display {label: "Set Expirable Value (ms)"}
+    remote function pSetEx(@display {label: "Key"} string key, @display {label: "Value"} string value, @display {label: "TTL (ms)"} int expirationTime) returns string|Error;
 
     # Set the value of a key.
     # 
-    remote function set(string key, string value) returns string|Error;
+    @display {label: "Set Value"}
+    remote function set(@display {label: "Key"} string key, @display {label: "Value"} string value) returns string|Error;
 
     # Sets or clears the bit at offset in the string value stored at key.
     # 
-    remote function setBit(string key, int value, int offset) returns int|Error;
+    @display {label: "Set Bit From Offset"}
+    remote function setBit(@display {label: "Key"} string key, @display {label: "Value"} int value, @display {label: "Offset"} int offset) returns int|Error;
 
     # Set the value and expiration of a key.
     # 
-    remote function setEx(string key, string value, int expirationTime) returns string|Error;
+    @display {label: "Set Expirable Value (s)"}
+    remote function setEx(@display {label: "Key"} string key, @display {label: "Value"} string value, @display {label: "TTL (s)"} int expirationTime) returns string|Error;
 
     # Set value of a key, only if key does not exist.
     # 
-    remote function setNx(string key, string value) returns boolean|Error;
+    @display {label: "Set Value If Absent"}
+    remote function setNx(@display {label: "Key"} string key, @display {label: "Value"} string value) returns boolean|Error;
 
     # Set the value and expiration of a key, only if the key does not exist. Combines `setNx` and `setEx`
     # into a single atomic operation (`SET key value NX EX expirationTime`).
     # 
-    remote function setNxEx(string key, string value, int expirationTime) returns boolean|Error;
+    @display {label: "Set Expirable Value If Absent"}
+    remote function setNxEx(@display {label: "Key"} string key, @display {label: "Value"} string value, @display {label: "TTL (s)"} int expirationTime) returns boolean|Error;
 
     # Overwrite part of string at key starting at the specified offset.
     # 
-    remote function setRange(string key, int offset, string value) returns int|Error;
+    @display {label: "Overwrite Value From Offset"}
+    remote function setRange(@display {label: "Key"} string key, @display {label: "Start Position"} int offset, @display {label: "Value"} string value) returns int|Error;
 
     # Get length of value stored in a key.
     # 
-    remote function strLen(string key) returns int|Error;
+    @display {label: "Get String Length"}
+    remote function strLen(@display {label: "Key"} string key) returns int|Error;
 
     # Prepend one or multiple values to list.
     # 
-    remote function lPush(string key, string[] values) returns int|Error;
+    @display {label: "Push Value To List"}
+    remote function lPush(@display {label: "Key"} string key, @display {label: "Values"} string[] values) returns int|Error;
 
     # Remove and get the first element in a list.
     # 
-    remote function lPop(string key) returns string|Error|();
+    @display {label: "Pop Value From List"}
+    remote function lPop(@display {label: "Key"} string key) returns string|Error|();
 
     # Prepend one or multiple values to a list, only if the list exists.
     # 
-    remote function lPushX(string key, string[] values) returns int|Error;
+    @display {label: "Push To Available List"}
+    remote function lPushX(@display {label: "Key"} string key, @display {label: "Values"} string[] values) returns int|Error;
 
     # Remove and get the first element in a list, or block until one is available.
     # 
-    remote function bLPop(int timeOut, string[] keys) returns map<any>|Error;
+    @display {label: "Pop List First Element And Block If Absent"}
+    remote function bLPop(@display {label: "Timeout (s)"} int timeOut, @display {label: "Keys"} string[] keys) returns map<any>|Error;
 
     # Remove and get the last element in a list, or block until one is available.
     # 
-    remote function bRPop(int timeout, string[] keys) returns map<any>|Error;
+    @display {label: "Pop List Last Element And Block If Absent"}
+    remote function bRPop(@display {label: "Timeout (s)"} int timeout, @display {label: "Key Referring To a Values"} string[] keys) returns map<any>|Error;
 
     # Get an element from list by its index.
     # 
-    remote function lIndex(string key, int index) returns string|Error|();
+    @display {label: "Get List Element By Index"}
+    remote function lIndex(@display {label: "Key"} string key, @display {label: "Index"} int index) returns string|Error|();
 
     # Insert an element before or after another element in a list.
     # 
-    remote function lInsert(string key, boolean before, string pivot, string value) returns int|Error;
+    @display {label: "Insert To List In Specific Position"}
+    remote function lInsert(@display {label: "Key"} string key, @display {label: "Insert Before or Not"} boolean before, @display {label: "Place To Insert"} string pivot, @display {label: "Value"} string value) returns int|Error;
 
     # Get length of a list.
     # 
-    remote function lLen(string key) returns int|Error;
+    @display {label: "Get List Length"}
+    remote function lLen(@display {label: "Key"} string key) returns int|Error;
 
     # Get a range of elements from a list.
     # 
-    remote function lRange(string key, int startPos, int stopPos) returns string[]|Error;
+    @display {label: "Get Range of List Elements"}
+    remote function lRange(@display {label: "Key"} string key, @display {label: "Start Position"} int startPos, @display {label: "End Position"} int stopPos) returns string[]|Error;
 
     # Remove elements from list.
     # 
-    remote function lRem(string key, int count, string value) returns int|Error;
+    @display {label: "Remove List Elements"}
+    remote function lRem(@display {label: "Key"} string key, @display {label: "Member Count"} int count, @display {label: "Value"} string value) returns int|Error;
 
     # Set the value of an element in a list by its index.
     # 
-    remote function lSet(string key, int index, string value) returns string|Error;
+    @display {label: "Set List Element At Index"}
+    remote function lSet(@display {label: "Key"} string key, @display {label: "Index"} int index, @display {label: "Value"} string value) returns string|Error;
 
     # Trim list to the specified range.
     # 
-    remote function lTrim(string key, int startPos, int stopPos) returns string|Error;
+    @display {label: "Trim List To Range"}
+    remote function lTrim(@display {label: "Key"} string key, @display {label: "Start Position"} int startPos, @display {label: "End Position"} int stopPos) returns string|Error;
 
     # Remove and get the last element in a list.
     # 
-    remote function rPop(string key) returns string|Error|();
+    @display {label: "Pop List Last Element"}
+    remote function rPop(@display {label: "Key"} string key) returns string|Error|();
 
     # Remove the last element in a list, append it to another list and return it.
     # 
-    remote function rPopLPush(string src, string destination) returns string|Error;
+    @display {label: "Move List Last Element To Another"}
+    remote function rPopLPush(@display {label: "Current Key"} string src, @display {label: "Destination Key"} string destination) returns string|Error;
 
     # Append one or multiple values to a list.
     # 
-    remote function rPush(string key, string[] values) returns int|Error;
+    @display {label: "Enrich Values To List"}
+    remote function rPush(@display {label: "Key"} string key, @display {label: "Values"} string[] values) returns int|Error;
 
     # Append one or multiple values to a list, only if the list exists.
     # 
-    remote function rPushX(string key, string[] values) returns int|Error;
+    @display {label: "Enrich Values To List If Exists"}
+    remote function rPushX(@display {label: "Key"} string key, @display {label: "Values"} string[] values) returns int|Error;
 
     # Add one or more members to a set.
     # 
-    remote function sAdd(string key, string[] values) returns int|Error;
+    @display {label: "Add Members To Set"}
+    remote function sAdd(@display {label: "Key"} string key, @display {label: "Values"} string[] values) returns int|Error;
 
     # Get the number of members in a set
     # 
-    remote function sCard(string key) returns int|Error;
+    @display {label: "Get Member Count In Set"}
+    remote function sCard(@display {label: "Key"} string key) returns int|Error;
 
     # Return set resulting from the difference between the first set and all the successive sets
     # 
-    remote function sDiff(string[] keys) returns string[]|Error;
+    @display {label: "Get Difference of Set"}
+    remote function sDiff(@display {label: "Keys"} string[] keys) returns string[]|Error;
 
     # Obtain the set resulting from the difference between the first set and all the successive.
     # sets and store at the provided destination.
     # 
-    remote function sDiffStore(string destination, string[] keys) returns int|Error;
+    @display {label: "Set Difference of Set"}
+    remote function sDiffStore(@display {label: "Destination Key"} string destination, @display {label: "Keys"} string[] keys) returns int|Error;
 
     # Return the intersection of the provided sets.
     # 
-    remote function sInter(string[] keys) returns string[]|Error;
+    @display {label: "Get Intersections of Sets"}
+    remote function sInter(@display {label: "Keys"} string[] keys) returns string[]|Error;
 
     # Obtain the intersection of the provided sets and store at the provided destination.
     # 
-    remote function sInterStore(string destination, string[] keys) returns int|Error;
+    @display {label: "Set Intersections of Sets"}
+    remote function sInterStore(@display {label: "Destination Key"} string destination, @display {label: "Keys"} string[] keys) returns int|Error;
 
     # Determine if a given value is a member of a set.
     # 
-    remote function sIsMember(string key, string value) returns boolean|Error;
+    @display {label: "Check Value In Set"}
+    remote function sIsMember(@display {label: "Key"} string key, @display {label: "Value"} string value) returns boolean|Error;
 
     # Get all members in a set.
     # 
-    remote function sMembers(string key) returns string[]|Error;
+    @display {label: "Get Members In Set"}
+    remote function sMembers(@display {label: "Key"} string key) returns string[]|Error;
 
     # Move a member from one set to another.
     # 
-    remote function sMove(string src, string destination, string member) returns boolean|Error;
+    @display {label: "Move Member Between Sets"}
+    remote function sMove(@display {label: "Source Key"} string src, @display {label: "Destination Key"} string destination, @display {label: "Member"} string member) returns boolean|Error;
 
     # Remove and return a random member from a set.
     # 
-    remote function sPop(string key, int count) returns string[]|Error|();
+    @display {label: "Pop Set Random Member"}
+    remote function sPop(@display {label: "Key"} string key, @display {label: "Member Count"} int count) returns string[]|Error|();
 
     # Get one or multiple random members from a set.
     # 
-    remote function sRandMember(string key, int count) returns string[]|Error;
+    @display {label: "Get Random Members In Set"}
+    remote function sRandMember(@display {label: "Key"} string key, @display {label: "Member Count"} int count) returns string[]|Error;
 
     # Remove one or more members from a set.
     # 
-    remote function sRem(string key, string[] members) returns int|Error;
+    @display {label: "Remove Members In Set"}
+    remote function sRem(@display {label: "Key"} string key, @display {label: "Members"} string[] members) returns int|Error;
 
     # Return the union of multiple sets.
     # 
-    remote function sUnion(string[] keys) returns string[]|Error;
+    @display {label: "Get Multiple Sets Union"}
+    remote function sUnion(@display {label: "Keys"} string[] keys) returns string[]|Error;
 
     # Return the union of multiple sets.
     # 
-    remote function sUnionStore(string destination, string[] keys) returns int|Error;
+    @display {label: "Set Multiple Sets Union"}
+    remote function sUnionStore(@display {label: "Destination Key"} string destination, @display {label: "Keys"} string[] keys) returns int|Error;
 
     # Add one or more members to a sorted set, or update its score if it already exist.
     # 
-    remote function zAdd(string key, map<any> memberScoreMap) returns int|Error;
+    @display {label: "Set Sorted Set Members"}
+    remote function zAdd(@display {label: "Key"} string key, @display {label: "Member-Value Pairs"} map<any> memberScoreMap) returns int|Error;
 
     # Get the number of members in a sorted set.
     # 
-    remote function zCard(string key) returns int|Error;
+    @display {label: "Get Sorted Set Member Count"}
+    remote function zCard(@display {label: "Key"} string key) returns int|Error;
 
     # Count the members in a sorted set with scores within the given range.
     # 
-    remote function zCount(string key, float min, float max) returns int|Error;
+    @display {label: "Get Sorted Set Member Count (By Range)"}
+    remote function zCount(@display {label: "Key"} string key, @display {label: "Minimum Value"} float min, @display {label: "Maximum Value"} float max) returns int|Error;
 
     # Increment the score of a member in a sorted set.
     # 
-    remote function zIncrBy(string key, float amount, string member) returns float|Error;
+    @display {label: "Increment Sorted Set Member"}
+    remote function zIncrBy(@display {label: "Key"} string key, @display {label: "Value"} float amount, @display {label: "Member"} string member) returns float|Error;
 
     # Intersect multiple sorted sets and store the resulting sorted set in a new key.
     # 
-    remote function zInterStore(string destination, string[] keys) returns int|Error;
+    @display {label: "Get Member Count (Sorted Sets Intersection)"}
+    remote function zInterStore(@display {label: "Destination Key"} string destination, @display {label: "Keys"} string[] keys) returns int|Error;
 
     # Count the members in a sorted set within the given lexicographical range.
     # 
-    remote function zLexCount(string key, string min, string max) returns int|Error;
+    @display {label: "Get Member Count (Lexicographical Range)"}
+    remote function zLexCount(@display {label: "Key"} string key, @display {label: "Minimum Value"} string min, @display {label: "Maximum Value"} string max) returns int|Error;
 
     # Return a range of members in a sorted set, by index.
     # 
-    remote function zRange(string key, int min, int max) returns string[]|Error;
+    @display {label: "Get Sorted Set Members (By Index Range)"}
+    remote function zRange(@display {label: "Key"} string key, @display {label: "Minimum Index"} int min, @display {label: "Maximum Index"} int max) returns string[]|Error;
 
     # Return a range of members in a sorted set, by lexicographical range from lowest to highest.
     # 
-    remote function zRangeByLex(string key, string min, string max) returns string[]|Error;
+    @display {label: "Get Sorted Set Members From Lowest (By Lexicographical Range)"}
+    remote function zRangeByLex(@display {label: "Key"} string key, @display {label: "Minimum Value"} string min, @display {label: "Maximum Value"} string max) returns string[]|Error;
 
     # Return a range of members in a sorted set, by lexicographical range ordered from highest to
     # lowest.
     # 
-    remote function zRevRangeByLex(string key, string min, string max) returns string[]|Error;
+    @display {label: "Get Sorted Set Members From Highest (By Lexicographical Range)"}
+    remote function zRevRangeByLex(@display {label: "Key"} string key, @display {label: "Minimum Value"} string min, @display {label: "Maximum Value"} string max) returns string[]|Error;
 
     # Return a range of members in a sorted set, by score from lowest to highest.
     # 
-    remote function zRangeByScore(string key, float min, float max) returns string[]|Error;
+    @display {label: "Get Sorted Set Members (By Score Range)"}
+    remote function zRangeByScore(@display {label: "Key"} string key, @display {label: "Minimum Value"} float min, @display {label: "Maximum Value"} float max) returns string[]|Error;
 
     # Determine index of a member in a sorted set.
     # 
-    remote function zRank(string key, string member) returns int|Error;
+    @display {label: "Get Sorted Set Member Index"}
+    remote function zRank(@display {label: "Key"} string key, @display {label: "Member"} string member) returns int|Error;
 
     # Remove one or more members from a sorted set
     # 
-    remote function zRem(string key, string[] members) returns int|Error;
+    @display {label: "Remove Sorted Set Members"}
+    remote function zRem(@display {label: "Key"} string key, @display {label: "Members"} string[] members) returns int|Error;
 
     # Remove all members in a sorted set between the given lexicographical range.
     # 
-    remote function zRemRangeByLex(string key, string min, string max) returns int|Error;
+    @display {label: "Deleted Member Count Between Lexicographical Range"}
+    remote function zRemRangeByLex(@display {label: "Key"} string key, @display {label: "Minimum Value"} string min, @display {label: "Maximum Value"} string max) returns int|Error;
 
     # Remove all members in a sorted set within the given indices.
     # 
-    remote function zRemRangeByRank(string key, int min, int max) returns int|Error;
+    @display {label: "Deleted Member Count Between Indexes"}
+    remote function zRemRangeByRank(@display {label: "Key"} string key, @display {label: "Minimum Index"} int min, @display {label: "Maximum Index"} int max) returns int|Error;
 
     # Remove all members in a sorted set within the given scores.
     # 
-    remote function zRemRangeByScore(string key, float min, float max) returns int|Error;
+    @display {label: "Deleted Member Count Between Scores"}
+    remote function zRemRangeByScore(@display {label: "Key"} string key, @display {label: "Minimum Value"} float min, @display {label: "Maximum Value"} float max) returns int|Error;
 
     # Return a range of members in a sorted set, by index, ordered highest to lowest.
     # 
-    remote function zRevRange(string key, int min, int max) returns string[]|Error;
+    @display {label: "Get Members (By Index Range)"}
+    remote function zRevRange(@display {label: "Key"} string key, @display {label: "Minimum Index"} int min, @display {label: "Maximum Index"} int max) returns string[]|Error;
 
     # Return a range of members in a sorted set, by score from highest to lowest.
     # 
-    remote function zRevRangeByScore(string key, float min, float max) returns string[]|Error;
+    @display {label: "Get Members (By Score Range)"}
+    remote function zRevRangeByScore(@display {label: "Key"} string key, @display {label: "Minimum Value"} float min, @display {label: "Maximum Value"} float max) returns string[]|Error;
 
     # Determine the index of a member in a sorted set
     # 
-    remote function zRevRank(string key, string member) returns int|Error;
+    @display {label: "Get Sorted Set Member Index"}
+    remote function zRevRank(@display {label: "Key"} string key, @display {label: "Member"} string member) returns int|Error;
 
     # Determine the score of a member in a sorted set
     # 
-    remote function zScore(string key, string member) returns float|Error;
+    @display {label: "Get Sorted Set Member Score"}
+    remote function zScore(@display {label: "Key"} string key, @display {label: "Member"} string member) returns float|Error;
 
     # Return the union of multiple sorted sets
     # 
-    remote function zUnionStore(string destination, string[] keys) returns int|Error;
+    @display {label: "Get Sorted Sets Union"}
+    remote function zUnionStore(@display {label: "Destination Key"} string destination, @display {label: "Keys"} string[] keys) returns int|Error;
 
     # Delete one or more hash fields.
     # 
-    remote function hDel(string key, string[] fields) returns int|Error;
+    @display {label: "Delete Hash Fields"}
+    remote function hDel(@display {label: "Key"} string key, @display {label: "Fields"} string[] fields) returns int|Error;
 
     # Determine if a hash field exists.
     # 
-    remote function hExists(string key, string 'field) returns boolean|Error;
+    @display {label: "Check Hash Field Availability"}
+    remote function hExists(@display {label: "Key"} string key, @display {label: "Field"} string 'field) returns boolean|Error;
 
     # Get the value of a hash field.
     # 
-    remote function hGet(string key, string 'field) returns string|Error;
+    @display {label: "Get Hash Field Value"}
+    remote function hGet(@display {label: "Key"} string key, @display {label: "Field"} string 'field) returns string|Error;
 
     # Get the all values of a hash.
     # 
-    remote function hGetAll(string key) returns map<any>|Error;
+    @display {label: "Get Hash Values"}
+    remote function hGetAll(@display {label: "Key"} string key) returns map<any>|Error;
 
     # Increment the integer value of a hash field by the given number.
     # 
-    remote function hIncrBy(string key, string 'field, int amount) returns int|Error;
+    @display {label: "Increment Hash Field (By Number)"}
+    remote function hIncrBy(@display {label: "Key"} string key, @display {label: "Field"} string 'field, @display {label: "Increment Value"} int amount) returns int|Error;
 
     # Increment the float value of a hash field by the given number.
     # 
-    remote function hIncrByFloat(string key, string 'field, float amount) returns float|Error;
+    @display {label: "Increment Hash Field (By Float)"}
+    remote function hIncrByFloat(@display {label: "Key"} string key, @display {label: "Field"} string 'field, @display {label: "Value To Increment"} float amount) returns float|Error;
 
     # Get all the fields in a hash.
     # 
-    remote function hKeys(string key) returns string[]|Error;
+    @display {label: "Get Hash Fields"}
+    remote function hKeys(@display {label: "Key"} string key) returns string[]|Error;
 
     # Get the number of fields in a hash.
     # 
-    remote function hLen(string key) returns int|Error;
+    @display {label: "Get Hash Fields Count"}
+    remote function hLen(@display {label: "Key"} string key) returns int|Error;
 
     # Get the values of all the given hash fields.
     # 
-    remote function hMGet(string key, string[] fields) returns map<any>|Error;
+    @display {label: "Get Hash Fields Values"}
+    remote function hMGet(@display {label: "Key"} string key, @display {label: "Fields"} string[] fields) returns map<any>|Error;
 
     # Set multiple hash fields to multiple values.
     # 
-    remote function hMSet(string key, map<any> fieldValueMap) returns string|Error;
+    @display {label: "Set Hash Fields"}
+    remote function hMSet(@display {label: "Key"} string key, @display {label: "Field-Value Pairs"} map<any> fieldValueMap) returns string|Error;
 
     # Set the string value of a hash field.
     # 
-    remote function hSet(string key, string 'field, string value) returns boolean|Error;
+    @display {label: "Set Hash Field"}
+    remote function hSet(@display {label: "Key"} string key, @display {label: "Hash Field"} string 'field, @display {label: "Value"} string value) returns boolean|Error;
 
     # Set the string value of a hash field, only if the field does not exist.
     # 
-    remote function hSetNx(string key, string 'field, string value) returns boolean|Error;
+    @display {label: "Set Hash Field If Absent"}
+    remote function hSetNx(@display {label: "Key"} string key, @display {label: "Hash Field"} string 'field, @display {label: "Value"} string value) returns boolean|Error;
 
     # Get the string length of the field value in a hash.
     # 
-    remote function hStrLen(string key, string 'field) returns int|Error;
+    @display {label: "Get Value String Length"}
+    remote function hStrLen(@display {label: "Key"} string key, @display {label: "Hash Field"} string 'field) returns int|Error;
 
     # Get all the values in a hash.
     # 
-    remote function hVals(string key) returns string[]|Error;
+    @display {label: "Get Values In Hash"}
+    remote function hVals(@display {label: "Key"} string key) returns string[]|Error;
 
     # Delete one or more keys.
     # 
-    remote function del(string[] keys) returns int|Error;
+    @display {label: "Delete Keys"}
+    remote function del(@display {label: "Keys"} string[] keys) returns int|Error;
 
     # Determine how many keys exist.
     # 
-    remote function exists(string[] keys) returns int|Error;
+    @display {label: "Check Keys"}
+    remote function exists(@display {label: "Keys"} string[] keys) returns int|Error;
 
     # Set a key's time to live in seconds.
     # 
-    remote function expire(string key, int seconds) returns boolean|Error;
+    @display {label: "Set TTL (s)"}
+    remote function expire(@display {label: "Key"} string key, @display {label: "TTL (s)"} int seconds) returns boolean|Error;
 
     # Find all keys matching the given pattern.
     # 
-    remote function keys(string pattern) returns string[]|Error;
+    @display {label: "Get Matching Keys"}
+    remote function keys(@display {label: "Pattern String"} string pattern) returns string[]|Error;
 
     # Move a key to another database.
     # 
-    remote function move(string key, int database) returns boolean|Error;
+    @display {label: "Move Key"}
+    remote function move(@display {label: "Key"} string key, @display {label: "Destination Database"} int database) returns boolean|Error;
 
     # Remove the expiration from a key.
     # 
-    remote function persist(string key) returns boolean|Error;
+    @display {label: "Remove Key Timeout"}
+    remote function persist(@display {label: "Key"} string key) returns boolean|Error;
 
     # Set a key's time to live in milliseconds.
     # 
-    remote function pExpire(string key, int expirationTime) returns boolean|Error;
+    @display {label: "Set TTL (ms)"}
+    remote function pExpire(@display {label: "Key"} string key, @display {label: "TTL (ms)"} int expirationTime) returns boolean|Error;
 
     # Get the time to live for a key in milliseconds.
     # 
-    remote function pTtl(string key) returns int|Error;
+    @display {label: "Get TTL (ms)"}
+    remote function pTtl(@display {label: "Key"} string key) returns int|Error;
 
     # Return a random key from the keyspace.
     # 
+    @display {label: "Get Random Key"}
     remote function randomKey() returns string|Error|();
 
     # Rename a key.
     # 
-    remote function rename(string key, string newName) returns string|Error;
+    @display {label: "Rename Key"}
+    remote function rename(@display {label: "Key"} string key, @display {label: "New Key Name"} string newName) returns string|Error;
 
     # Rename a key, only if the new key does not exist.
     # 
-    remote function renameNx(string key, string newName) returns boolean|Error;
+    @display {label: "Rename Key If Absent"}
+    remote function renameNx(@display {label: "Key"} string key, @display {label: "New Key Name"} string newName) returns boolean|Error;
 
     # Sort elements in a list, set or sorted set.
     # 
-    remote function sort(string key) returns string[]|Error;
+    @display {label: "Sort Elements"}
+    remote function sort(@display {label: "Key"} string key) returns string[]|Error;
 
     # Get the time to live for a key.
     # 
-    remote function ttl(string key) returns int|Error;
+    @display {label: "Get Key TTL"}
+    remote function ttl(@display {label: "Key"} string key) returns int|Error;
 
     # Determine the type stored at key.
     # 
-    remote function redisType(string key) returns string|Error;
+    @display {label: "Get Key Type"}
+    remote function redisType(@display {label: "Key"} string key) returns string|Error;
 
     # Retrieve information and statistics about the cluster observed by the current node.
     # This command is exclusively available in cluster mode. If the connection is in a non-clustered mode,
@@ -671,25 +809,30 @@
 
     # Ping the server.
     # 
+    @display {label: "Ping the server"}
     remote function ping() returns string|Error;
 
     # Authenticate to the server.
     # 
-    remote function auth(string password) returns string|Error;
+    @display {label: "Authenticate Server"}
+    remote function auth(@display {label: "Password"} string password) returns string|Error;
 
     # Echo the given string.
     # 
-    remote function echo(string message) returns string|Error;
+    @display {label: "Echo Input String"}
+    remote function echo(@display {label: "String To Echo"} string message) returns string|Error;
 
     # Remove all the keys from the currently selected database.
     # 
+    @display {label: "Flush Database"}
     remote function flushDb() returns string|Error;
 
     # Remove all the keys from all the databases.
     # 
+    @display {label: "Flush All Databases"}
     remote function flushAll() returns string|Error;
 
     # Close the connection.
     # 
-    remote function close() returns Error|();
+    function close() returns Error|();
 }
`````

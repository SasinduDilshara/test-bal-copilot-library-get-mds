# jwt — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `jwt` |
| **Old file** | `jwt/old/ballerina_jwt.bal.txt` |
| **New file** | `jwt/new/ballerina_jwt.bal.txt` |
| **Old lines** | 274 |
| **New lines** | 298 |
| **Lines added** | 31 |
| **Lines removed** | 7 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 6 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `class ClientSelfSignedJwtAuthProvider`
- `class ListenerJwtAuthProvider`
- `function authenticate`
- `function generateToken`
- `function init`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 126–132 | 126–134 | Types | +3 | −1 |
| 2 | 157–163 | 159–165 | Types | +1 | −1 |
| 3 | 189–199 | 191–201 | Types | +2 | −2 |
| 4 | 238–247 | 240–271 | Types | +24 | −2 |
| 5 | 271–274 | 295–298 | Functions | +1 | −1 |

---

## Unified diff

`````diff
--- jwt/old/ballerina_jwt.bal.txt	2026-08-12 23:21:51
+++ jwt/new/ballerina_jwt.bal.txt	2026-08-12 23:23:51
@@ -126,7 +126,9 @@
     string jti?;
 };
 
-// Unknown type: Error
+# Represents the error type of the module. This will be returned if an error occurred while issuing/validating a JWT
+# or any operation related to JWT auth providers.
+type Error error;
 
 # Represents JWT issuer configurations.
 # 
@@ -157,7 +159,7 @@
     # Cryptographic signing algorithm for JWS
     SigningAlgorithm algorithm?;
     # KeyStore configurations, private key configurations, `crypto:PrivateKey` or shared key configurations
-    record {|ballerina/crypto:2.12.1:KeyStore keyStore; string keyAlias; string keyPassword;|}|record {|string keyFile; string keyPassword?;|}|crypto:PrivateKey|string config?; // Special Agent Note: PrivateKey FROM ballerina/crypto package
+    record {|crypto:KeyStore keyStore; string keyAlias; string keyPassword;|}|record {|string keyFile; string keyPassword?;|}|crypto:PrivateKey|string config?; // Special Agent Note: PrivateKey FROM ballerina/crypto package
 };
 
 # Represents JWT validator configurations.
@@ -189,11 +191,11 @@
 
 type ValidatorSignatureConfig record {
     # JWKS configurations
-    record {|string url; ballerina/cache:3.10.0:CacheConfig cacheConfig?; ballerina/jwt:2.15.1:ClientConfiguration clientConfig;|} jwksConfig?;
+    record {|string url; cache:CacheConfig cacheConfig?; ClientConfiguration clientConfig;|} jwksConfig?;
     # Public certificate file path or a `crypto:PublicKey`
     string|crypto:PublicKey certFile?; // Special Agent Note: PublicKey FROM ballerina/crypto package
     # JWT TrustStore configurations
-    record {|ballerina/crypto:2.12.1:TrustStore trustStore; string certAlias;|} trustStoreConfig?;
+    record {|crypto:TrustStore trustStore; string certAlias;|} trustStoreConfig?;
     # HMAC secret configuration
     string secret?;
 };
@@ -238,10 +240,32 @@
     string keyPassword?;
 };
 
-// Unknown type: ClientSelfSignedJwtAuthProvider
+# Provides authentication based on the provided JWT configurations.
+# 
+class ClientSelfSignedJwtAuthProvider {
+    function init(IssuerConfig issuerConfig) returns ();
 
-// Unknown type: ListenerJwtAuthProvider
+    # Issues a self-signed JWT for authentication.
+    # ```ballerina
+    # string token = check provider.generateToken();
+    # ```
+    # 
+    function generateToken() returns string|Error;
+}
 
+# Provides authentication based on the provided JWT.
+# 
+class ListenerJwtAuthProvider {
+    function init(ValidatorConfig validatorConfig) returns ();
+
+    # Authenticates the provided JWT.
+    # ```ballerina
+    # boolean result = check provider.authenticate("<credential>");
+    # ```
+    # 
+    function authenticate(string credential) returns Payload|Error;
+}
+
 // --- Functions ---
 
 # Issues a JWT based on the provided configurations. JWT will be signed (JWS) if `crypto:KeyStore` information is
@@ -271,4 +295,4 @@
 # 
 # + jwt - JWT that needs to be decoded
 # + return - The `jwt:Header` and `jwt:Payload` as a tuple or else a `jwt:Error` if an error occurred
-function decode(string jwt) returns [ballerina/jwt:2.15.1:Header, ballerina/jwt:2.15.1:Payload]|Error;
+function decode(string jwt) returns [Header, Payload]|Error;
`````

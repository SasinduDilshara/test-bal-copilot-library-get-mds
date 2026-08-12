# auth — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `auth` |
| **Old file** | `auth/old/ballerina_auth.bal.txt` |
| **New file** | `auth/new/ballerina_auth.bal.txt` |
| **Old lines** | 142 |
| **New lines** | 182 |
| **Lines added** | 44 |
| **Lines removed** | 4 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (7)

- `class ClientBasicAuthProvider`
- `class ListenerFileUserStoreBasicAuthProvider`
- `class ListenerLdapUserStoreBasicAuthProvider`
- `function authenticate`
- `function generateToken`
- `function init`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 46–52 | 46–55 | Types | +4 | −1 |
| 2 | 63–68 | 66–75 | Types | +4 | −0 |
| 3 | 124–135 | 131–175 | Types | +36 | −3 |

---

## Unified diff

`````diff
--- auth/old/ballerina_auth.bal.txt	2026-08-12 23:21:51
+++ auth/new/ballerina_auth.bal.txt	2026-08-12 23:23:51
@@ -46,7 +46,10 @@
     string[] scopes?;
 };
 
-// Unknown type: Error
+# Represents the error type of the module. This will be returned if an error occurred while any of the listener
+# Basic Auth providers try to authenticate the received credentials and client Basic Auth providers try to generate
+# the token.
+type Error error;
 
 # Represents credentials for Basic Auth authentication.
 # 
@@ -63,6 +66,10 @@
 # Any type of implementation such as file store, LDAP user store, in memory user store, JDBC user store etc. should be
 # object-wise similar.
 class ListenerBasicAuthProvider {
+
+    # Authenticates the user based on the user credentials (i.e., the username/password).
+    # 
+    function authenticate(string credential) returns UserDetails|Error;
 }
 
 # Represents the file user store configurations.
@@ -124,12 +131,45 @@
     crypto:TrustStore|string cert; // Special Agent Note: TrustStore FROM ballerina/crypto package
 };
 
-// Unknown type: ClientBasicAuthProvider
+# Provides authentication based on the provided Basic Auth configurations.
+# 
+class ClientBasicAuthProvider {
+    function init(CredentialsConfig credentialsConfig) returns ();
 
-// Unknown type: ListenerFileUserStoreBasicAuthProvider
+    # Generates a Base64-encoded token for Basic Auth authentication.
+    # ```ballerina
+    # string token = check provider.generateToken();
+    # ```
+    # 
+    function generateToken() returns string|Error;
+}
 
-// Unknown type: ListenerLdapUserStoreBasicAuthProvider
+# Provides authentication based on the provided configurations.
+# 
+class ListenerFileUserStoreBasicAuthProvider {
+    function init(FileUserStoreConfig fileUserStoreConfig = {}) returns ();
 
+    # Authenticate the Base64-encoded `username:password` credentials.
+    # ```ballerina
+    # auth:UserDetails result = check provider.authenticate("<credential>");
+    # ```
+    # 
+    function authenticate(string credential) returns UserDetails|Error;
+}
+
+# Creates an LDAP auth store with the provided configurations.
+# 
+class ListenerLdapUserStoreBasicAuthProvider {
+    function init(LdapUserStoreConfig ldapUserStoreConfig) returns ();
+
+    # Attempts to authenticate the Base64-encoded `username:password` credentials.
+    # ```ballerina
+    # auth:UserDetails result = check provider.authenticate("<credential>");
+    # ```
+    # 
+    function authenticate(string credential) returns UserDetails|Error;
+}
+
 // --- Functions ---
 
 # Extracts the username and the password from the Base64-encoded `username:password` value.
`````

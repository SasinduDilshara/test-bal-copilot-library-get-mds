# oauth2 — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `oauth2` |
| **Old file** | `oauth2/old/ballerina_oauth2.bal.txt` |
| **New file** | `oauth2/new/ballerina_oauth2.bal.txt` |
| **Old lines** | 283 |
| **New lines** | 307 |
| **Lines added** | 29 |
| **Lines removed** | 5 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 7 | 0 |
| `// --- section ---` markers | 3 | 3 |

### Declarations added (6)

- `class ClientOAuth2Provider`
- `class ListenerOAuth2Provider`
- `function authorize`
- `function generateToken`
- `function init`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 173–179 | 173–179 | Types | +1 | −1 |
| 2 | 226–232 | 226–232 | Types | +1 | −1 |
| 3 | 276–283 | 276–307 | Types | +27 | −3 |

---

## Unified diff

`````diff
--- oauth2/old/ballerina_oauth2.bal.txt	2026-08-12 23:21:51
+++ oauth2/new/ballerina_oauth2.bal.txt	2026-08-12 23:23:51
@@ -173,7 +173,7 @@
 };
 
 # Represents the the authentication configuration types for the HTTP client used for token introspection.
-type ClientAuth ballerina/oauth2:2.15.0:ClientCredentialsGrantConfig|ballerina/oauth2:2.15.0:PasswordGrantConfig|ballerina/oauth2:2.15.0:RefreshTokenGrantConfig;
+type ClientAuth ClientCredentialsGrantConfig|PasswordGrantConfig|RefreshTokenGrantConfig;
 
 # Represents the SSL/TLS configurations.
 # 
@@ -226,7 +226,7 @@
 };
 
 # Represents the grant type configurations supported for OAuth2.
-type GrantConfig ballerina/oauth2:2.15.0:ClientCredentialsGrantConfig|ballerina/oauth2:2.15.0:PasswordGrantConfig|ballerina/oauth2:2.15.0:RefreshTokenGrantConfig|ballerina/oauth2:2.15.0:JwtBearerGrantConfig;
+type GrantConfig ClientCredentialsGrantConfig|PasswordGrantConfig|RefreshTokenGrantConfig|JwtBearerGrantConfig;
 
 # Represents the introspection endpoint configurations.
 # 
@@ -276,8 +276,32 @@
     string jti?;
 };
 
-// Unknown type: Error
+# Represents the error type of the module. This will be returned if an error occurred while the listener OAuth2 provider
+# tries to validate the received credentials and the client OAuth2 provider tries to generate the token.
+type Error error;
 
-// Unknown type: ClientOAuth2Provider
+# Provides authorization based on the provided OAuth2 configurations.
+# 
+class ClientOAuth2Provider {
+    function init(GrantConfig grantConfig) returns ();
 
-// Unknown type: ListenerOAuth2Provider
+    # Get an OAuth2 access token from the token endpoint.
+    # ```ballerina
+    # string token = check provider.generateToken();
+    # ```
+    # 
+    function generateToken() returns string|Error;
+}
+
+# Provides authorization based on the provided introspection configurations.
+# 
+class ListenerOAuth2Provider {
+    function init(IntrospectionConfig introspectionConfig) returns ();
+
+    # Validates the provided OAuth2 acess token against the introspection endpoint.
+    # ```ballerina
+    # boolean result = check provider.authorize("<credential>");
+    # ```
+    # 
+    function authorize(string credential, map<string>|() optionalParams = ()) returns IntrospectionResponse|Error;
+}
`````

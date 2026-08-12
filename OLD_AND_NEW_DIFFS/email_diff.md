# email — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `email` |
| **Old file** | `email/old/ballerina_email.bal.txt` |
| **New file** | `email/new/ballerina_email.bal.txt` |
| **Old lines** | 718 |
| **New lines** | 811 |
| **Lines added** | 101 |
| **Lines removed** | 8 |
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

### Declarations added (9)

- `class ImapListener`
- `class PopListener`
- `function 'start`
- `function attach`
- `function detach`
- `function gracefulStop`
- `function immediateStop`
- `function register`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 515–521 | 515–521 | Types | +1 | −1 |
| 2 | 566–578 | 566–579 | Types | +3 | −2 |
| 3 | 653–667 | 654–760 | Types | +95 | −3 |
| 4 | 680–686 | 773–779 | Client | +1 | −1 |
| 5 | 699–705 | 792–798 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- email/old/ballerina_email.bal.txt	2026-08-12 12:57:29
+++ email/new/ballerina_email.bal.txt	2026-08-12 13:19:19
@@ -515,7 +515,7 @@
     # Server certificate path
     string cert;
     # SSL or TLS protocol
-    record {|ballerina/email:2.14.0:Protocol name; string[] versions;|} protocol?;
+    record {|Protocol name; string[] versions;|} protocol?;
     # Ciper used
     string[] ciphers?;
     # Enable hostname verification
@@ -566,13 +566,14 @@
 
 # OAuth2 grant configuration for SMTP authentication.
 # Can be either `OAuth2ClientCredentialsGrantConfig` or `OAuth2PasswordGrantConfig`.
-type OAuth2GrantConfig ballerina/email:2.14.0:OAuth2ClientCredentialsGrantConfig|ballerina/email:2.14.0:OAuth2PasswordGrantConfig;
+type OAuth2GrantConfig OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig;
 
 # Represents a Email service.
 class Service {
 }
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Configuration of the IMAP Endpoint.
 # 
@@ -653,15 +654,107 @@
     OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|string auth?;
 };
 
-// Unknown type: ImapListener
+# Gets invoked during the `email:ImapListener` initialization.
+# 
+class ImapListener {
+    function init(ImapListenerConfiguration listenerConfig) returns Error?;
 
-// Unknown type: PopListener
+    # Starts the `email:ImapListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Binds a service to the `email:ImapListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.attach(helloService, hello);
+    # ```
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Stops consuming messages and detaches the service from the `email:ImapListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.detach(helloService);
+    # ```
+    # 
+    function detach(Service s) returns error?;
 
+    # Stops the `email:ImapListener` forcefully.
+    # ```ballerina
+    # email:Error? result = emailListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Stops the `email:ImapListener` gracefully.
+    # ```ballerina
+    # email:Error? result = emailListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Registers for the Email service.
+    # ```ballerina
+    # emailListener.register(helloService, hello);
+    # ```
+    # 
+    function register(Service emailService, string|() name) returns ();
+}
+
+# Gets invoked during the `email:PopListener` initialization.
+# 
+class PopListener {
+    function init(PopListenerConfiguration listenerConfig) returns Error?;
+
+    # Starts the `email:PopListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.start();
+    # ```
+    # 
+    function 'start() returns error?;
+
+    # Binds a service to the `email:PopListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.attach(helloService, hello);
+    # ```
+    # 
+    function attach(Service s, string[]|string|() name = ()) returns error?;
+
+    # Stops consuming messages and detaches the service from the `email:PopListener`.
+    # ```ballerina
+    # email:Error? result = emailListener.detach(helloService);
+    # ```
+    # 
+    function detach(Service s) returns error?;
+
+    # Stops the `email:PopListener` forcefully.
+    # ```ballerina
+    # email:Error? result = emailListener.immediateStop();
+    # ```
+    # 
+    function immediateStop() returns error?;
+
+    # Stops the `email:PopListener` gracefully.
+    # ```ballerina
+    # email:Error? result = emailListener.gracefulStop();
+    # ```
+    # 
+    function gracefulStop() returns error?;
+
+    # Registers for the Email service.
+    # ```ballerina
+    # emailListener.register(helloService, hello);
+    # ```
+    # 
+    function register(Service emailService, string|() name) returns ();
+}
+
 // --- Client ---
 
 # Represents an IMAP Client, which interacts with an IMAP Server.
 client class ImapClient {
-    function init(string host, string username, string password, int port = 993, Security security = SSL, SecureSocket secureSocket = {cert: ""}, ImapConfiguration clientConfig) returns ballerina/email:2.14.0:Error?;
+    function init(string host, string username, string password, int port = 993, Security security = SSL, SecureSocket secureSocket = {cert: ""}, ImapConfiguration clientConfig) returns Error?;
 
     # Reads a message.
     # ```ballerina
@@ -680,7 +773,7 @@
 
 # Represents a POP Client, which interacts with a POP Server.
 client class PopClient {
-    function init(string host, string username, string password, int port = 995, Security security = SSL, SecureSocket secureSocket = {cert: ""}, PopConfiguration clientConfig) returns ballerina/email:2.14.0:Error?;
+    function init(string host, string username, string password, int port = 995, Security security = SSL, SecureSocket secureSocket = {cert: ""}, PopConfiguration clientConfig) returns Error?;
 
     # Reads a message.
     # ```ballerina
@@ -699,7 +792,7 @@
 
 # Represents an SMTP Client, which interacts with an SMTP Server.
 client class SmtpClient {
-    function init(string host, string|() username = (), string|() password = (), int port = 465, Security security = SSL, SecureSocket secureSocket = {cert: ""}, OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|string auth = {tokenUrl: "", clientId: "", clientSecret: ""}, SmtpConfiguration clientConfig) returns ballerina/email:2.14.0:Error?;
+    function init(string host, string|() username = (), string|() password = (), int port = 465, Security security = SSL, SecureSocket secureSocket = {cert: ""}, OAuth2ClientCredentialsGrantConfig|OAuth2PasswordGrantConfig|string auth = {tokenUrl: "", clientId: "", clientSecret: ""}, SmtpConfiguration clientConfig) returns Error?;
 
     # Sends an email message.
     # ```ballerina
`````

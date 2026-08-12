# ldap — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ldap` |
| **Old file** | `ldap/old/ballerina_ldap.bal.txt` |
| **New file** | `ldap/new/ballerina_ldap.bal.txt` |
| **Old lines** | 552 |
| **New lines** | 553 |
| **Lines added** | 3 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 267–273 | 267–274 | Types | +2 | −1 |
| 2 | 458–464 | 459–465 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- ldap/old/ballerina_ldap.bal.txt	2026-08-12 23:21:51
+++ ldap/new/ballerina_ldap.bal.txt	2026-08-12 23:23:51
@@ -267,7 +267,8 @@
     string resultCode?;
 };
 
-// Unknown type: Error
+# Represents any error related to Ballerina LDAP module
+type Error error<ErrorDetails>;
 
 # Provides a set of configurations to connect with a directory server.
 # 
@@ -458,7 +459,7 @@
 
 # Consists of APIs to integrate with LDAP.
 client class Client {
-    function init(string hostName = "", int port = 0, string domainName = "", string password = "", ClientSecureSocket clientSecureSocket = {}, ConnectionConfig config) returns ballerina/ldap:1.4.0:Error?;
+    function init(string hostName = "", int port = 0, string domainName = "", string password = "", ClientSecureSocket clientSecureSocket = {}, ConnectionConfig config) returns Error?;
 
     # Creates an entry in a directory server.
     # 
`````

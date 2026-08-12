# googleapis.gmail — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `googleapis.gmail` |
| **Old file** | `googleapis.gmail/old/ballerinax_googleapis.gmail.bal.txt` |
| **New file** | `googleapis.gmail/new/ballerinax_googleapis.gmail.bal.txt` |
| **Old lines** | 730 |
| **New lines** | 735 |
| **Lines added** | 17 |
| **Lines removed** | 12 |
| **Hunks** | 7 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 9 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (3)

- `type Error`
- `type FileGenericError`
- `type ValueEncodeError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 169–182 | 169–186 | Types | +7 | −3 |
| 2 | 247–252 | 251–257 | Types | +1 | −0 |
| 3 | 264–272 | 269–277 | Types | +2 | −2 |
| 4 | 287–293 | 292–298 | Types | +1 | −1 |
| 5 | 328–334 | 333–339 | Types | +1 | −1 |
| 6 | 378–384 | 383–389 | Types | +1 | −1 |
| 7 | 511–525 | 516–530 | Types | +4 | −4 |

---

## Unified diff

`````diff
--- googleapis.gmail/old/ballerinax_googleapis.gmail.bal.txt	2026-08-12 12:57:30
+++ googleapis.gmail/new/ballerinax_googleapis.gmail.bal.txt	2026-08-12 13:19:19
@@ -169,14 +169,18 @@
 # Holds value for message type **text/html**.
 const string CONTENT_TYPE_TEXT_HTML = "text/html";
 
-// Unknown type: Error
+# Defines the generic error type for the `gmail` module.
+type Error error;
 
-// Unknown type: FileGenericError
+# Error that occurs when there is an issue with inline images or attachments. This could be due to issues like file not found, unsupported file type, etc.
+type FileGenericError error;
 
-// Unknown type: ValueEncodeError
+# Error that occurs when an invalid encoded value is provided for the `data` fields.
+type ValueEncodeError error;
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -247,6 +251,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -264,9 +269,9 @@
     # The ID of the mailbox's current history record.
     string historyId?;
     # The total number of messages in the mailbox.
-    ballerina/lang.int:0.0.0:Signed32 messagesTotal?;
+    int:Signed32 messagesTotal?;
     # The total number of threads in the mailbox.
-    ballerina/lang.int:0.0.0:Signed32 threadsTotal?;
+    int:Signed32 threadsTotal?;
 };
 
 # An email message.
@@ -287,7 +292,7 @@
     # The internal message creation timestamp (epoch ms), which determines ordering in the inbox. For normal SMTP-received email, this represents the time the message was originally accepted by Google, which is more reliable than the `Date` header. However, for API-migrated mail, it can be configured by client to be based on the `Date` header.
     string internalDate?;
     # Estimated size in bytes of the message.
-    ballerina/lang.int:0.0.0:Signed32 sizeEstimate?;
+    int:Signed32 sizeEstimate?;
     # Email header **To**
     string[] to?;
     # Email header **From**
@@ -328,7 +333,7 @@
     # The body data of a MIME message part as raw decoded bytes. May be empty for MIME container types that have no message body or when the body data is sent as a separate attachment. An attachment ID is present if the body data is contained in a separate attachment.
     byte[] rawData?;
     # Number of bytes for the message part data.
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
     # The child MIME message parts of this part. This only applies to container MIME message parts, for example `multipart/*`. For non- container MIME message part types, such as `text/plain`, this field is empty. For more information, see RFC 1521.
     MessagePart[] parts?;
 };
@@ -378,7 +383,7 @@
     # The attachment data as raw decoded bytes. Populated for binary content that cannot be represented as a UTF-8 string (e.g. PDF, images).
     byte[] rawData?;
     # Number of bytes for the message part data (encoding notwithstanding).
-    ballerina/lang.int:0.0.0:Signed32 size?;
+    int:Signed32 size?;
 };
 
 # Message Send Request-Payload (Charset UTF-8 will be used to encode the message body).
@@ -511,15 +516,15 @@
     # The visibility of messages with this label in the message list in the Gmail web interface.
     "show"|"hide" messageListVisibility?;
     # The total number of messages with the label.
-    ballerina/lang.int:0.0.0:Signed32 messagesTotal?;
+    int:Signed32 messagesTotal?;
     # The number of unread messages with the label.
-    ballerina/lang.int:0.0.0:Signed32 messagesUnread?;
+    int:Signed32 messagesUnread?;
     # The display name of the label.
     string name?;
     # The total number of threads with the label.
-    ballerina/lang.int:0.0.0:Signed32 threadsTotal?;
+    int:Signed32 threadsTotal?;
     # The number of unread threads with the label.
-    ballerina/lang.int:0.0.0:Signed32 threadsUnread?;
+    int:Signed32 threadsUnread?;
     # The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the `INBOX` and `UNREAD` labels from messages and threads, but cannot apply or remove the `DRAFTS` or `SENT` labels from messages or threads.
     "system"|"user" 'type?;
 };
`````

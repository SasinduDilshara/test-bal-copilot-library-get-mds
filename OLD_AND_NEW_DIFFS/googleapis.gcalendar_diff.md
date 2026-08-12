# googleapis.gcalendar — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `googleapis.gcalendar` |
| **Old file** | `googleapis.gcalendar/old/ballerinax_googleapis.gcalendar.bal.txt` |
| **New file** | `googleapis.gcalendar/new/ballerinax_googleapis.gcalendar.bal.txt` |
| **Old lines** | 1240 |
| **New lines** | 1243 |
| **Lines added** | 14 |
| **Lines removed** | 11 |
| **Hunks** | 9 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 10 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 292–301 | 292–303 | END README | +3 | −1 |
| 2 | 366–371 | 368–374 | Types | +1 | −0 |
| 3 | 413–421 | 416–424 | Types | +2 | −2 |
| 4 | 646–652 | 649–655 | Types | +1 | −1 |
| 5 | 781–787 | 784–790 | Types | +1 | −1 |
| 6 | 837–843 | 840–846 | Types | +1 | −1 |
| 7 | 1086–1094 | 1089–1097 | Types | +2 | −2 |
| 8 | 1103–1111 | 1106–1114 | Types | +2 | −2 |
| 9 | 1116–1122 | 1119–1125 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- googleapis.gcalendar/old/ballerinax_googleapis.gcalendar.bal.txt	2026-08-12 12:57:30
+++ googleapis.gcalendar/new/ballerinax_googleapis.gcalendar.bal.txt	2026-08-12 13:19:19
@@ -292,10 +292,12 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents any error related to the `gcalendar` module.
+type Error error;
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -366,6 +368,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -413,9 +416,9 @@
 
 type FreeBusyResponse record {
     # List of free/busy information for calendars.
-    record {|ballerinax/googleapis.gcalendar:4.0.1:FreeBusyCalendar...;|} calendars?;
+    record {|FreeBusyCalendar...;|} calendars?;
     # Expansion of groups.
-    record {|ballerinax/googleapis.gcalendar:4.0.1:FreeBusyGroup...;|} groups?;
+    record {|FreeBusyGroup...;|} groups?;
     # Type of the resource ("calendar#freeBusy").
     string kind?;
     # The end of the interval.
@@ -646,7 +649,7 @@
     string method?;
     # Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes).
 Required when adding a reminder.
-    ballerina/lang.int:0.0.0:Signed32 minutes?;
+    int:Signed32 minutes?;
 };
 
 # The notifications that the authenticated user is receiving for this calendar.
@@ -781,7 +784,7 @@
     # Information about the event's reminders for the authenticated user.
     EventReminders reminders?;
     # Sequence number as per iCalendar.
-    ballerina/lang.int:0.0.0:Signed32 sequence?;
+    int:Signed32 sequence?;
     # Source from which the event was created. For example, a web page, an email message or any document identifiable by an URL with HTTP or HTTPS scheme. Can only be seen or modified by the creator of the event.
     EventSource 'source?;
     # Defines the start date and time of the event
@@ -837,7 +840,7 @@
 
 type EventAttendee record {
     # Number of additional guests. Optional. The default is 0.
-    ballerina/lang.int:0.0.0:Signed32 additionalGuests?;
+    int:Signed32 additionalGuests?;
     # The attendee's response comment. Optional.
     string comment?;
     # The attendee's name, if available. Optional.
@@ -1086,9 +1089,9 @@
 
 type FreeBusyRequest record {
     # Maximal number of calendars for which FreeBusy information is to be provided. Optional. Maximum value is 50.
-    ballerina/lang.int:0.0.0:Signed32 calendarExpansionMax?;
+    int:Signed32 calendarExpansionMax?;
     # Maximal number of calendar identifiers to be provided for a single group. Optional. An error is returned for a group with more members than this value. Maximum value is 100.
-    ballerina/lang.int:0.0.0:Signed32 groupExpansionMax?;
+    int:Signed32 groupExpansionMax?;
     # List of calendars and/or groups to query.
     FreeBusyRequestItem[] items?;
     # The end of the interval for the query formatted as per RFC3339.
@@ -1103,9 +1106,9 @@
 
 type Colors record {
     # A global palette of calendar colors, mapping from the color ID to its definition. A calendarListEntry resource refers to one of these color IDs in its colorId field. Read-only.
-    record {|ballerinax/googleapis.gcalendar:4.0.1:ColorDefinition...;|} calendar?;
+    record {|ColorDefinition...;|} calendar?;
     # A global palette of event colors, mapping from the color ID to its definition. An event resource may refer to one of these color IDs in its colorId field. Read-only.
-    record {|ballerinax/googleapis.gcalendar:4.0.1:ColorDefinition...;|} event?;
+    record {|ColorDefinition...;|} event?;
     # Type of the resource ("calendar#colors").
     string kind?;
     # Last modification time of the color palette (as a RFC3339 timestamp). Read-only.
@@ -1116,7 +1119,7 @@
 
 # Manipulates events and other calendar data.
 client class Client {
-    function init(ConnectionConfig config, string serviceUrl = "https://www.googleapis.com/calendar/v3") returns ballerinax/googleapis.gcalendar:4.0.1:Error?;
+    function init(ConnectionConfig config, string serviceUrl = "https://www.googleapis.com/calendar/v3") returns Error?;
 
     # Creates a secondary calendar.
     # 
`````

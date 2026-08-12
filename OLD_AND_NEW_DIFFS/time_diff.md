# time — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `time` |
| **Old file** | `time/old/ballerina_time.bal.txt` |
| **New file** | `time/new/ballerina_time.bal.txt` |
| **Old lines** | 429 |
| **New lines** | 494 |
| **Lines added** | 70 |
| **Lines removed** | 5 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (10)

- `class TimeZone`
- `function civilAddDuration`
- `function fixedOffset`
- `function init`
- `function utcFromCivil`
- `function utcToCivil`
- `type Error`
- `type FormatError`
- `type Seconds`
- `type Utc`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 126–138 | 126–161 | Types | +27 | −4 |
| 2 | 244–253 | 267–318 | Types | +43 | −1 |

---

## Unified diff

`````diff
--- time/old/ballerina_time.bal.txt	2026-08-12 23:21:51
+++ time/new/ballerina_time.bal.txt	2026-08-12 23:23:51
@@ -126,13 +126,36 @@
 
 const string ZONE_OFFSET_WITH_TIME_ABBREV_COMMENT = "ZONE_OFFSET_WITH_TIME_ABBREV_COMMENT";
 
-// Unknown type: Error
+# Represents a generic module-level error.
+type Error error;
 
-// Unknown type: FormatError
+# An error to be returned when arguments are invalid.
+type FormatError error;
 
-// Unknown type: Seconds
+# Holds the seconds as a decimal value.  
+type Seconds decimal;
 
-// Unknown type: Utc
+# Point on UTC time-scale.
+# This is represented by a tuple of length 2.
+# The tuple is an ordered type and so the values can be
+# compared using the Ballerina <, <=, >, >= operators.
+# The first member of the tuple is int representing an integral number of
+# seconds from the epoch.
+# Epoch is the traditional UNIX epoch of `1970-01-01T00:00:00Z`.
+# The second member of the tuple is a decimal giving the fraction of
+# a second.
+# For times before the epoch, n is negative and f is
+# non-negative. In other words, the UTC time represented
+# is on or after the second specified by n.
+# Leap seconds are handled as follows. The first member
+# of the tuple ignores leap seconds: it assumes that every day
+# has 86400 seconds. The second member of the tuple is >= 0.
+# and is < 1 except during positive leaps seconds in which it
+# is >= 1 and < 2. So given a tuple [n,f] after the epoch,
+# n / 86400 gives the day number, and (n % 86400) + f gives the
+# time in seconds since midnight UTC (for which the limit is
+# 86401 on day with a positive leap second).
+type Utc readonly & [int, decimal];
 
 # Day of the week according to the US convention, starting on Sunday.
 type DayOfWeek 0|1|2|3|4|5|6;
@@ -244,10 +267,52 @@
 
 # Abstract object representation to handle time zones.  
 class Zone {
+
+    # Returns the fixed zone offset if the time zone is always at a fixed offset from UTC; otherwise, returns nil.
+    # 
+    function fixedOffset() returns ZoneOffset|();
+
+    # Converts a given civil record to a UTC timestamp based on the time zone value.
+    # 
+    function utcFromCivil(Civil civil) returns Utc|Error;
+
+    # Converts a given UTC timestamp to a civil record based on the time zone value.
+    # 
+    function utcToCivil(Utc utc) returns Civil;
+
+    # Adds the given time duration to the specified civil date-time based on the time zone.
+    # The operation assumes that all days have exactly 86,400 seconds.
+    # 
+    function civilAddDuration(Civil civil, Duration duration) returns Civil|Error;
 }
 
-// Unknown type: TimeZone
+# Initializes a `TimeZone` object using a zone ID or the system default time zone.
+# 
+class TimeZone {
+    function init(string|() zoneId = ()) returns Error?;
 
+    # Returns the fixed zone offset if the time zone is always at a fixed offset from UTC; otherwise, returns nil.
+    # 
+    function fixedOffset() returns ZoneOffset|();
+
+    # Converts a given civil record to a UTC timestamp based on the time zone value.
+    # 
+    function utcFromCivil(Civil civil) returns Utc|Error;
+
+    # Converts a given UTC timestamp to a civil record based on the time zone value.
+    # 
+    function utcToCivil(Utc utc) returns Civil;
+
+    # Adds the given time duration to the specified civil date-time based on the time zone.
+    # The operation assumes that all days have exactly 86,400 seconds.
+    # ```ballerina
+    # time:TimeZone timeZone = check new("Asia/Colombo");
+    # time:Civil civil = check time:civilFromString("2025-04-25T10:15:30.00Z");
+    # time:Civil|time:Error updatedCivil = timeZone.civilAddDuration(civil, {years: 1, days: 3, hours: 4});
+    # ```
+    function civilAddDuration(Civil civil, Duration duration) returns Civil|Error;
+}
+
 // --- Functions ---
 
 # Returns the `time:Utc` representing the current time (current instant of the system clock in seconds from the epoch of `1970-01-01T00:00:00`).
`````

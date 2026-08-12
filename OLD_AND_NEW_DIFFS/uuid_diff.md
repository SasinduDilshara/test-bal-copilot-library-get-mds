# uuid — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `uuid` |
| **Old file** | `uuid/old/ballerina_uuid.bal.txt` |
| **New file** | `uuid/new/ballerina_uuid.bal.txt` |
| **Old lines** | 249 |
| **New lines** | 250 |
| **Lines added** | 7 |
| **Lines removed** | 6 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 5 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 58–72 | 58–72 | Types | +5 | −5 |
| 2 | 92–98 | 92–99 | Types | +2 | −1 |

---

## Unified diff

`````diff
--- uuid/old/ballerina_uuid.bal.txt	2026-08-12 23:21:51
+++ uuid/new/ballerina_uuid.bal.txt	2026-08-12 23:23:51
@@ -58,15 +58,15 @@
 
 type Uuid record {
     # The low field of the timestamp
-    ballerina/lang.int:0.0.0:Unsigned32 timeLow;
+    int:Unsigned32 timeLow;
     # The middle field of the timestamp
-    ballerina/lang.int:0.0.0:Unsigned16 timeMid;
+    int:Unsigned16 timeMid;
     # The high field of the timestamp multiplexed with the version number
-    ballerina/lang.int:0.0.0:Unsigned16 timeHiAndVersion;
+    int:Unsigned16 timeHiAndVersion;
     # The high field of the clock sequence multiplexed with the variant
-    ballerina/lang.int:0.0.0:Unsigned8 clockSeqHiAndReserved;
+    int:Unsigned8 clockSeqHiAndReserved;
     # The low field of the clock sequence
-    ballerina/lang.int:0.0.0:Unsigned8 clockSeqLo;
+    int:Unsigned8 clockSeqLo;
     # The spatially unique node identifier
     int node;
     # Rest field
@@ -92,7 +92,8 @@
     NAME_SPACE_DNS
 }
 
-// Unknown type: Error
+# Represents UUID module related errors.
+type Error error;
 
 // --- Functions ---
 
`````

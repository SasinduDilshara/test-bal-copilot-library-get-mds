# regex — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `regex` |
| **Old file** | `regex/old/ballerina_regex.bal.txt` |
| **New file** | `regex/new/ballerina_regex.bal.txt` |
| **Old lines** | 202 |
| **New lines** | 204 |
| **Lines added** | 3 |
| **Lines removed** | 1 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `function get`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 58–63 | 58–65 | Types | +2 | −0 |
| 2 | 73–79 | 75–81 | Types | +1 | −1 |

---

## Unified diff

`````diff
--- regex/old/ballerina_regex.bal.txt	2026-08-12 23:21:51
+++ regex/new/ballerina_regex.bal.txt	2026-08-12 23:23:51
@@ -58,6 +58,8 @@
 
 # Abstract object representation to hold information about matched regex groups.
 class Groups {
+
+    function get(int index) returns PartMatch|();
 }
 
 # Holds the results of a match against a regular expression. 
@@ -73,7 +75,7 @@
 };
 
 # A type to be used to get a replacement string.
-type Replacement ballerina/regex:1.4.3:ReplacerFunction|string;
+type Replacement ReplacerFunction|string;
 
 // --- Functions ---
 
`````

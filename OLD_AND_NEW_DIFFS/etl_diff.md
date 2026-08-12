# etl — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `etl` |
| **Old file** | `etl/old/ballerina_etl.bal.txt` |
| **New file** | `etl/new/ballerina_etl.bal.txt` |
| **Old lines** | 588 |
| **New lines** | 593 |
| **Lines added** | 7 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type CategoryRanges`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 167–173 | 167–174 | Types | +2 | −1 |
| 2 | 187–193 | 188–198 | Types | +5 | −1 |

---

## Unified diff

`````diff
--- etl/old/ballerina_etl.bal.txt	2026-08-12 23:21:51
+++ etl/new/ballerina_etl.bal.txt	2026-08-12 23:23:51
@@ -167,7 +167,8 @@
     GPT_4_TURBO
 }
 
-// Unknown type: Error
+# Represents ETL module related errors.
+type Error error;
 
 # Represents the available comparison operations for the `filterDataByRelativeExp` API.
 # 
@@ -187,7 +188,11 @@
     ASCENDING
 }
 
-// Unknown type: CategoryRanges
+# Represents the category ranges in the `categorizeNumeric` API
+# - `float` - Represents the minimum value.
+# - `float[]` - Represents the intermediate breakpoints.
+# - `float` - Represents the maximum value.
+type CategoryRanges [float, float[], float];
 
 // --- Functions ---
 
`````

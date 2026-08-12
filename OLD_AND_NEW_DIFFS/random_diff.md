# random — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `random` |
| **Old file** | `random/old/ballerina_random.bal.txt` |
| **New file** | `random/new/ballerina_random.bal.txt` |
| **Old lines** | 43 |
| **New lines** | 45 |
| **Lines added** | 4 |
| **Lines removed** | 2 |
| **Hunks** | 1 |

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

- `type ArithmeticError`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 17–25 | 17–27 | END README | +4 | −2 |

---

## Unified diff

`````diff
--- random/old/ballerina_random.bal.txt	2026-08-12 23:21:51
+++ random/new/ballerina_random.bal.txt	2026-08-12 23:23:51
@@ -17,9 +17,11 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents Random module related errors.
+type Error error;
 
-// Unknown type: ArithmeticError
+# Represents the arithmetic error.
+type ArithmeticError error;
 
 // --- Functions ---
 
`````

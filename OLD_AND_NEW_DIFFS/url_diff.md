# url — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `url` |
| **Old file** | `url/old/ballerina_url.bal.txt` |
| **New file** | `url/new/ballerina_url.bal.txt` |
| **Old lines** | 44 |
| **New lines** | 45 |
| **Lines added** | 2 |
| **Lines removed** | 1 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 17–23 | 17–24 | END README | +2 | −1 |

---

## Unified diff

`````diff
--- url/old/ballerina_url.bal.txt	2026-08-12 23:21:51
+++ url/new/ballerina_url.bal.txt	2026-08-12 23:23:51
@@ -17,7 +17,8 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents the error type of the module.
+type Error error;
 
 // --- Functions ---
 
`````

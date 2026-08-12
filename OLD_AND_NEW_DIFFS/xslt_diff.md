# xslt — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `xslt` |
| **Old file** | `xslt/old/ballerina_xslt.bal.txt` |
| **New file** | `xslt/new/ballerina_xslt.bal.txt` |
| **Old lines** | 38 |
| **New lines** | 39 |
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

- `type TransformError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 21–27 | 21–28 | END README | +2 | −1 |

---

## Unified diff

`````diff
--- xslt/old/ballerina_xslt.bal.txt	2026-08-12 23:21:51
+++ xslt/new/ballerina_xslt.bal.txt	2026-08-12 23:23:51
@@ -21,7 +21,8 @@
 
 // --- Types ---
 
-// Unknown type: TransformError
+# Represents an `xslt:TransformError` with the message and the cause.
+type TransformError error;
 
 // --- Functions ---
 
`````

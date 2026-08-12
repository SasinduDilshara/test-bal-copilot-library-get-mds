# confluent.cavroserdes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `confluent.cavroserdes` |
| **Old file** | `confluent.cavroserdes/old/ballerinax_confluent.cavroserdes.bal.txt` |
| **New file** | `confluent.cavroserdes/new/ballerinax_confluent.cavroserdes.bal.txt` |
| **Old lines** | 94 |
| **New lines** | 95 |
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
| 1 | 71–77 | 71–78 | END README | +2 | −1 |

---

## Unified diff

`````diff
--- confluent.cavroserdes/old/ballerinax_confluent.cavroserdes.bal.txt	2026-08-12 12:57:30
+++ confluent.cavroserdes/new/ballerinax_confluent.cavroserdes.bal.txt	2026-08-12 13:19:19
@@ -71,7 +71,8 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents any error related to the module.
+type Error error;
 
 // --- Functions ---
 
`````

# azure_storage_service — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `azure_storage_service` |
| **Old file** | `azure_storage_service/old/ballerinax_azure_storage_service.bal.txt` |
| **New file** | `azure_storage_service/new/ballerinax_azure_storage_service.bal.txt` |
| **Old lines** | 37 |
| **New lines** | 38 |
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
| `// --- section ---` markers | 3 | 3 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 34–37 | 34–38 | END README | +2 | −1 |

---

## Unified diff

`````diff
--- azure_storage_service/old/ballerinax_azure_storage_service.bal.txt	2026-08-12 12:57:30
+++ azure_storage_service/new/ballerinax_azure_storage_service.bal.txt	2026-08-12 13:19:19
@@ -34,4 +34,5 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents storage module error.
+type Error error;
`````

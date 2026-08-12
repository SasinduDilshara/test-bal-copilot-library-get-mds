# ai.microsoft.sharepoint — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.microsoft.sharepoint` |
| **Old file** | `ai.microsoft.sharepoint/old/ballerinax_ai.microsoft.sharepoint.bal.txt` |
| **New file** | `ai.microsoft.sharepoint/new/ballerinax_ai.microsoft.sharepoint.bal.txt` |
| **Old lines** | 309 |
| **New lines** | 318 |
| **Lines added** | 10 |
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

### Declarations added (3)

- `class TextDataLoader`
- `function init`
- `function load`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 306–309 | 306–318 | Types | +10 | −1 |

---

## Unified diff

`````diff
--- ai.microsoft.sharepoint/old/ballerinax_ai.microsoft.sharepoint.bal.txt	2026-08-12 12:57:29
+++ ai.microsoft.sharepoint/new/ballerinax_ai.microsoft.sharepoint.bal.txt	2026-08-12 13:19:19
@@ -306,4 +306,13 @@
     string[]? pages?;
 };
 
-// Unknown type: TextDataLoader
+# Initializes the SharePoint data loader.
+# 
+@display {label: "Microsoft SharePoint Text Data Loader"}
+class TextDataLoader {
+    function init(@display {label: "SharePoint Connection Configurations"} ConnectionConfig sharePointConnectionConfigs, @display {label: "Data Sources"} Source[] sources) returns ai:Error?;
+
+    # Loads the configured SharePoint documents.
+    # 
+    function load() returns ai:Document[]|ai:Document|ai:Error; // Special Agent Note: Document, Error FROM ballerina/ai package
+}
`````

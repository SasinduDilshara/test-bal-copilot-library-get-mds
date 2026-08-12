# ai.weaviate — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.weaviate` |
| **Old file** | `ai.weaviate/old/ballerinax_ai.weaviate.bal.txt` |
| **New file** | `ai.weaviate/new/ballerinax_ai.weaviate.bal.txt` |
| **Old lines** | 160 |
| **New lines** | 176 |
| **Lines added** | 17 |
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

### Declarations added (5)

- `class VectorStore`
- `function add`
- `function delete`
- `function init`
- `function query`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 157–160 | 157–176 | Types | +17 | −1 |

---

## Unified diff

`````diff
--- ai.weaviate/old/ballerinax_ai.weaviate.bal.txt	2026-08-12 12:57:29
+++ ai.weaviate/new/ballerinax_ai.weaviate.bal.txt	2026-08-12 13:19:19
@@ -157,4 +157,20 @@
     boolean validation?;
 };
 
-// Unknown type: VectorStore
+# Initializes the Weaviate vector store with the given configuration.
+# 
+class VectorStore {
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Weaviate Configuration"} Configuration config, @display {label: "HTTP Configuration"} ConnectionConfig httpConfig = {}) returns ai:Error?;
+
+    # Adds a list of vector entries to the Weaviate vector store.
+    # 
+    function add(ai:VectorEntry[] entries) returns ai:Error|(); // Special Agent Note: VectorEntry, Error FROM ballerina/ai package
+
+    # Deletes a vector entry from the Weaviate vector store.
+    # 
+    function delete(string|string[] ids) returns ai:Error|(); // Special Agent Note: Error FROM ballerina/ai package
+
+    # Queries the Weaviate vector store for vector entries.
+    # 
+    function query(ai:VectorStoreQuery query) returns ai:VectorMatch[]|ai:Error; // Special Agent Note: VectorStoreQuery, VectorMatch, Error FROM ballerina/ai package
+}
`````

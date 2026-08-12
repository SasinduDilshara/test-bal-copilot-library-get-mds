# ai.milvus — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.milvus` |
| **Old file** | `ai.milvus/old/ballerinax_ai.milvus.bal.txt` |
| **New file** | `ai.milvus/new/ballerinax_ai.milvus.bal.txt` |
| **Old lines** | 130 |
| **New lines** | 146 |
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
| 1 | 127–130 | 127–146 | Types | +17 | −1 |

---

## Unified diff

`````diff
--- ai.milvus/old/ballerinax_ai.milvus.bal.txt	2026-08-12 12:57:29
+++ ai.milvus/new/ballerinax_ai.milvus.bal.txt	2026-08-12 13:19:19
@@ -127,4 +127,20 @@
     string[] additionalFields?;
 };
 
-// Unknown type: VectorStore
+# Initializes the Milvus vector store with the given configuration.
+# 
+class VectorStore {
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Milvus Configuration"} Configuration config, @display {label: "HTTP Configuration"} milvus:ConnectionConfig httpConfig = {}) returns ai:Error?; // Special Agent Note: ConnectionConfig FROM ballerinax/milvus package
+
+    # Adds the given vector entries to the Milvus vector store.
+    # 
+    function add(ai:VectorEntry[] entries) returns ai:Error|(); // Special Agent Note: VectorEntry, Error FROM ballerina/ai package
+
+    # Deletes vector entries from the store by their reference document ID.
+    # 
+    function delete(string|string[] ids) returns ai:Error|(); // Special Agent Note: Error FROM ballerina/ai package
+
+    # Queries Milvus using the provided embedding vector and returns the top matches.
+    # 
+    function query(ai:VectorStoreQuery query) returns ai:VectorMatch[]|ai:Error; // Special Agent Note: VectorStoreQuery, VectorMatch, Error FROM ballerina/ai package
+}
`````

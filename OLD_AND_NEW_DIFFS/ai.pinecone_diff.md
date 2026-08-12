# ai.pinecone — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.pinecone` |
| **Old file** | `ai.pinecone/old/ballerinax_ai.pinecone.bal.txt` |
| **New file** | `ai.pinecone/new/ballerinax_ai.pinecone.bal.txt` |
| **Old lines** | 73 |
| **New lines** | 89 |
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
| 1 | 70–73 | 70–89 | Types | +17 | −1 |

---

## Unified diff

`````diff
--- ai.pinecone/old/ballerinax_ai.pinecone.bal.txt	2026-08-12 12:57:29
+++ ai.pinecone/new/ballerinax_ai.pinecone.bal.txt	2026-08-12 13:19:19
@@ -70,4 +70,20 @@
     ai:SparseVector sparseVector?; // Special Agent Note: SparseVector FROM ballerina/ai package
 };
 
-// Unknown type: VectorStore
+# Initializes the PineconeVectorStore with the given configuration.
+# 
+class VectorStore {
+    function init(@display {label: "Service URL"} string serviceUrl, @display {label: "API Key"} string apiKey, @display {label: "Query Mode"} ai:VectorStoreQueryMode queryMode = ai:DENSE, @display {label: "Pinecone Configuration"} Configuration config = {}, @display {label: "HTTP Configuration"} vector:ConnectionConfig httpConfig = {}) returns ai:Error?; // Special Agent Note: VectorStoreQueryMode FROM ballerina/ai package, ConnectionConfig FROM ballerinax/pinecone.vector package
+
+    # Adds the given vector entries to the Pinecone vector store.
+    # 
+    function add(ai:VectorEntry[] entries) returns ai:Error|(); // Special Agent Note: VectorEntry, Error FROM ballerina/ai package
+
+    # Queries Pinecone using the provided embedding vector and returns the top matches.
+    # 
+    function query(ai:VectorStoreQuery queryVector) returns ai:VectorMatch[]|ai:Error; // Special Agent Note: VectorStoreQuery, VectorMatch, Error FROM ballerina/ai package
+
+    # Deletes vector entries from the store by their reference document ID.
+    # 
+    function delete(string|string[] refDocIds) returns ai:Error|(); // Special Agent Note: Error FROM ballerina/ai package
+}
`````

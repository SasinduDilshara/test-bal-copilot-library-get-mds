# ai.pgvector — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.pgvector` |
| **Old file** | `ai.pgvector/old/ballerinax_ai.pgvector.bal.txt` |
| **New file** | `ai.pgvector/new/ballerinax_ai.pgvector.bal.txt` |
| **Old lines** | 120 |
| **New lines** | 136 |
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
| 1 | 117–120 | 117–136 | Types | +17 | −1 |

---

## Unified diff

`````diff
--- ai.pgvector/old/ballerinax_ai.pgvector.bal.txt	2026-08-12 12:57:29
+++ ai.pgvector/new/ballerinax_ai.pgvector.bal.txt	2026-08-12 13:19:19
@@ -117,4 +117,20 @@
     COSINE
 }
 
-// Unknown type: VectorStore
+# Initializes the pgvector vector store with the provided configuration.
+# 
+class VectorStore {
+    function init(@display {label: "Host name"} string host, @display {label: "Username"} string user, @display {label: "Password"} string password, @display {label: "Database name"} string database, @display {label: "Table name"} string tableName = "vector_store", @display {label: "Port number"} int port = 5432, @display {label: "Additional set of configurations for the database"} postgresql:Options options = {}, @display {label: "Properties to configure connection pool"} sql:ConnectionPool connectionPool = {}, @display {label: "Configurations for the vector store"} Configuration configs = {}) returns ai:Error?; // Special Agent Note: Options FROM ballerinax/postgresql package, ConnectionPool FROM ballerina/sql package
+
+    # Adds vector entries to the vector store database.
+    # 
+    function add(ai:VectorEntry[] entries) returns ai:Error|(); // Special Agent Note: VectorEntry, Error FROM ballerina/ai package
+
+    # Deletes vector entries from the vector store database by ID(s).
+    # 
+    function delete(string|string[] ids) returns ai:Error|(); // Special Agent Note: Error FROM ballerina/ai package
+
+    # Queries the vector store for matches to the given query embedding and filters.
+    # 
+    function query(ai:VectorStoreQuery query) returns ai:VectorMatch[]|ai:Error; // Special Agent Note: VectorStoreQuery, VectorMatch, Error FROM ballerina/ai package
+}
`````

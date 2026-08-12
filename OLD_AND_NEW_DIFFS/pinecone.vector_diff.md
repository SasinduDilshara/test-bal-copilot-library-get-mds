# pinecone.vector — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `pinecone.vector` |
| **Old file** | `pinecone.vector/old/ballerinax_pinecone.vector.bal.txt` |
| **New file** | `pinecone.vector/new/ballerinax_pinecone.vector.bal.txt` |
| **Old lines** | 305 |
| **New lines** | 314 |
| **Lines added** | 16 |
| **Lines removed** | 7 |
| **Hunks** | 10 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (5)

- `type ErrorMessage`
- `type NamespaceName`
- `type VectorData`
- `type VectorDimensionality`
- `type VectorId`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 64–69 | 64–70 | Types | +1 | −0 |
| 2 | 116–121 | 117–123 | Types | +1 | −0 |
| 3 | 141–146 | 143–149 | Types | +1 | −0 |
| 4 | 154–162 | 157–167 | Types | +4 | −2 |
| 5 | 167–173 | 172–179 | Types | +2 | −1 |
| 6 | 193–199 | 199–205 | Types | +1 | −1 |
| 7 | 201–207 | 207–215 | Types | +3 | −1 |
| 8 | 217–223 | 225–231 | Types | +1 | −1 |
| 9 | 261–267 | 269–275 | Types | +1 | −1 |
| 10 | 276–281 | 284–290 | Client | +1 | −0 |

---

## Unified diff

`````diff
--- pinecone.vector/old/ballerinax_pinecone.vector.bal.txt	2026-08-12 12:57:30
+++ pinecone.vector/new/ballerinax_pinecone.vector.bal.txt	2026-08-12 13:19:19
@@ -64,6 +64,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
@@ -116,6 +117,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -141,6 +143,7 @@
     # An index namespace name
     NamespaceName namespace?;
     # The number of results to return for each query.
+    @constraint:Int {maxValue: 10000}
     int topK;
     # If this parameter is present, the operation only affects vectors that satisfy the filter. See https://www.pinecone.io/docs/metadata-filtering/.
     VectorFilter filter?;
@@ -154,9 +157,11 @@
     VectorId id?;
 };
 
-// Unknown type: NamespaceName
+# An index namespace name
+type NamespaceName string;
 
-// Unknown type: VectorData
+# Vector dense data. This should be the same length as the dimension of the index being queried.
+type VectorData float[];
 
 # Vector sparse data. Represented as a list of indices and a list of corresponded values, which must be the same length.
 
@@ -167,7 +172,8 @@
     float[] values;
 };
 
-// Unknown type: VectorId
+# The unique ID of a vector
+type VectorId string;
 
 
 type UpdateRequest record {
@@ -193,7 +199,7 @@
 
 
 type DescribeIndexStatsResponse record {
-    record {|ballerinax/pinecone.vector:1.0.2:IndexNamespaceStats...;|} namespaces?;
+    record {|IndexNamespaceStats...;|} namespaces?;
     # The number of dimensions in the vector representation
     VectorDimensionality dimension?;
     # The fullness of the index, regardless of whether a metadata filter expression was passed. The granularity of this metric is 10%.
@@ -201,7 +207,9 @@
     int totalVectorCount?;
 };
 
-// Unknown type: VectorDimensionality
+# The number of dimensions in the vector representation
+@constraint:Int {minValue: 1, maxValue: 20000}
+type VectorDimensionality int;
 
 
 type Vector record {
@@ -217,7 +225,7 @@
 # The response for the `Fetch` operation.
 
 type FetchResponse record {
-    record {|ballerinax/pinecone.vector:1.0.2:Vector...;|} vectors?;
+    record {|Vector...;|} vectors?;
     # The namespace of the vectors.
     string namespace?;
 };
@@ -261,7 +269,7 @@
     NamespaceName namespace?;
 };
 
-// Unknown type: ErrorMessage
+type ErrorMessage string;
 
 
 type DeleteRequest record {
@@ -276,6 +284,7 @@
 // --- Client ---
 
 # This is a generated connector for the `Vector Operations` under [Pinecone Vector Database API](https://docs.pinecone.io/reference) OpenAPI specification. Pinecone is a fully managed vector database which supports building developer-friendly, easily scalable, and high-performance vector search applications without infrastructure hassles.
+@display {label: "Pinecone Vector", iconPath: "icon.png"}
 client class Client {
     function init(ApiKeysConfig apiKeyConfig, string serviceUrl, ConnectionConfig config = {}) returns error?;
 
`````

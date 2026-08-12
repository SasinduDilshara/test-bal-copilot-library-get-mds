# weaviate — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `weaviate` |
| **Old file** | `weaviate/old/ballerinax_weaviate.bal.txt` |
| **New file** | `weaviate/new/ballerinax_weaviate.bal.txt` |
| **Old lines** | 662 |
| **New lines** | 669 |
| **Lines added** | 14 |
| **Lines removed** | 7 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (5)

- `type C11yVector`
- `type GraphQLQueries`
- `type GraphQLResponses`
- `type MultipleRef`
- `type ObjectsGetResponseArr`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 116–121 | 116–122 | Types | +1 | −0 |
| 2 | 170–175 | 171–177 | Types | +1 | −0 |
| 3 | 203–209 | 205–212 | Types | +2 | −1 |
| 4 | 217–223 | 220–226 | Types | +1 | −1 |
| 5 | 274–280 | 277–283 | Types | +1 | −1 |
| 6 | 432–438 | 435–442 | Types | +2 | −1 |
| 7 | 565–578 | 569–584 | Types | +5 | −3 |
| 8 | 589–594 | 595–601 | Client | +1 | −0 |

---

## Unified diff

`````diff
--- weaviate/old/ballerinax_weaviate.bal.txt	2026-08-12 12:57:30
+++ weaviate/new/ballerinax_weaviate.bal.txt	2026-08-12 13:19:20
@@ -116,6 +116,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -170,6 +171,7 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
@@ -203,7 +205,8 @@
 type PropertySchema record {
 };
 
-// Unknown type: C11yVector
+# A Vector in the Contextionary
+type C11yVector float[];
 
 # Additional Meta information about a single object object.
 
@@ -217,7 +220,7 @@
     Deprecation[]|() deprecations?;
     # Results for this specific Object.
     ObjectsGetResponse_result result?;
-    string class?;
+    string 'class?;
     VectorWeights|() vectorWeights?;
     PropertySchema properties?;
     string id?;
@@ -274,7 +277,7 @@
     string message?;
 };
 
-// Unknown type: ObjectsGetResponseArr
+type ObjectsGetResponseArr ObjectsGetResponse[];
 
 # Definitions of semantic schemas (also see: https://github.com/weaviate/weaviate-semantic-schemas).
 
@@ -432,7 +435,8 @@
     record {|anydata...;|} variables?;
 };
 
-// Unknown type: GraphQLQueries
+# A list of GraphQL queries.
+type GraphQLQueries GraphQLQuery[];
 
 # JSON object value.
 
@@ -565,14 +569,16 @@
 
 type GraphQLResponse record {
     # GraphQL data object.
-    record {|ballerinax/weaviate:1.0.2:JsonObject...;|} data?;
+    record {|JsonObject...;|} data?;
     # Array with errors.
     GraphQLError[]|() errors?;
 };
 
-// Unknown type: MultipleRef
+# Multiple instances of references to other objects.
+type MultipleRef SingleRef[];
 
-// Unknown type: GraphQLResponses
+# A list of GraphQL responses.
+type GraphQLResponses GraphQLResponse[];
 
 # List of Objects.
 
@@ -589,6 +595,7 @@
 
 # This is a generated connector for [Weaviate Vector Search Engine API](https://weaviate.io/developers/weaviate/api) OpenAPI specification.
 # Weaviate API provide access to the manipulations of weaviate schema, objects and search vectors based on various criterias.
+@display {label: "Weaviate", iconPath: "icon.png"}
 client class Client {
     function init(ConnectionConfig config, string serviceUrl = "/v1") returns error?;
 
`````

# azure.ai.search.index — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `azure.ai.search.index` |
| **Old file** | `azure.ai.search.index/old/ballerinax_azure.ai.search.index.bal.txt` |
| **New file** | `azure.ai.search.index/new/ballerinax_azure.ai.search.index.bal.txt` |
| **Old lines** | 831 |
| **New lines** | 833 |
| **Lines added** | 27 |
| **Lines removed** | 25 |
| **Hunks** | 14 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 16 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 132–138 | 132–138 | Types | +1 | −1 |
| 2 | 159–165 | 159–165 | Types | +1 | −1 |
| 3 | 211–217 | 211–217 | Types | +1 | −1 |
| 4 | 249–254 | 249–255 | Types | +1 | −0 |
| 5 | 342–348 | 343–349 | Types | +1 | −1 |
| 6 | 397–411 | 398–412 | Types | +3 | −3 |
| 7 | 439–445 | 440–446 | Types | +1 | −1 |
| 8 | 591–597 | 592–599 | Types | +2 | −1 |
| 9 | 611–617 | 613–619 | Types | +1 | −1 |
| 10 | 619–625 | 621–627 | Types | +1 | −1 |
| 11 | 668–674 | 670–676 | Types | +1 | −1 |
| 12 | 702–708 | 704–710 | Types | +1 | −1 |
| 13 | 757–771 | 759–773 | Types | +3 | −3 |
| 14 | 795–831 | 797–833 | Client | +9 | −9 |

---

## Unified diff

`````diff
--- azure.ai.search.index/old/ballerinax_azure.ai.search.index.bal.txt	2026-08-12 12:57:30
+++ azure.ai.search.index/new/ballerinax_azure.ai.search.index.bal.txt	2026-08-12 13:19:19
@@ -132,7 +132,7 @@
     # The name of the suggester as specified in the suggesters collection that's part of the index definition.
     string suggesterName;
     # The number of suggestions to retrieve. This must be a value between 1 and 100. The default is 5.
-    ballerina/lang.int:0.0.0:Signed32 top?;
+    int:Signed32 top?;
 };
 
 # Represents the Headers record for the operation: documentsCount
@@ -159,7 +159,7 @@
     # A number between 0 and 100 indicating the percentage of the index that must be covered by a suggestions query in order for the query to be reported as a success. This parameter can be useful for ensuring search availability even for services with only one replica. The default is 80.
     decimal minimumCoverage?;
     # The number of suggestions to retrieve. The value must be a number between 1 and 100. The default is 5.
-    ballerina/lang.int:0.0.0:Signed32 \$top?;
+    int:Signed32 \$top?;
     # An OData expression that filters the documents considered for suggestions.
     string \$filter?;
     # The list of OData $orderby expressions by which to sort the results. Each expression can be either a field name or a call to either the geo.distance() or the search.score() functions. Each expression can be followed by asc to indicate ascending, or desc to indicate descending. The default is ascending order. Ties will be broken by the match scores of documents. If no $orderby is specified, the default sort order is descending by document match score. There can be at most 32 $orderby clauses.
@@ -211,7 +211,7 @@
     # A value indicating whether the indexing operation succeeded for the document identified by the key.
     boolean status;
     # The status code of the indexing operation. Possible values include: 200 for a successful update or delete, 201 for successful document creation, 400 for a malformed input document, 404 for document not found, 409 for a version conflict, 422 when the index is temporarily unavailable, or 503 for when the service is too busy.
-    ballerina/lang.int:0.0.0:Signed32 statusCode;
+    int:Signed32 statusCode;
 };
 
 # A value that specifies whether we want to calculate scoring statistics (such as document frequency) globally for more consistent scoring, or locally, for lower latency. The default is 'local'. Use 'global' to aggregate scoring statistics globally before scoring. Using global scoring statistics can increase latency of search queries.
@@ -249,6 +249,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
@@ -342,7 +343,7 @@
     # A value indicating the percentage of the index that was included in the query, or null if minimumCoverage was not specified in the request.
     decimal \@search\.coverage?;
     # The facet query results for the search operation, organized as a collection of buckets for each faceted field; null if the query did not include any facet expressions.
-    record {|ballerinax/azure.ai.search.index:1.0.2:FacetResult[]...;|} \@search\.facets?;
+    record {|FacetResult[]...;|} \@search\.facets?;
     # The answers query results for the search operation; null if the answers query parameter was not specified or set to 'none'.
     AnswerResult[]|() \@search\.answers?;
     # Parameters for filtering, sorting, faceting, paging, and other search query behaviors.
@@ -397,15 +398,15 @@
     # The comma-separated list of fields to retrieve. If unspecified, all fields marked as retrievable in the schema are included.
     string 'select?;
     # The number of search results to skip. This value cannot be greater than 100,000. If you need to scan documents in sequence, but cannot use skip due to this limitation, consider using orderby on a totally-ordered key and filter with a range query instead.
-    ballerina/lang.int:0.0.0:Signed32 skip?;
+    int:Signed32 skip?;
     # The number of search results to retrieve. This can be used in conjunction with $skip to implement client-side paging of search results. If results are truncated due to server-side paging, the response will include a continuation token that can be used to issue another Search request for the next page of results.
-    ballerina/lang.int:0.0.0:Signed32 top?;
+    int:Signed32 top?;
     # The name of a semantic configuration that will be used when processing documents for queries of type semantic.
     string semanticConfiguration?;
     # Allows the user to choose whether a semantic call should fail completely, or to return partial results.
     SemanticErrorHandling semanticErrorHandling?;
     # Allows the user to set an upper bound on the amount of time it takes for semantic enrichment to finish processing before the request fails.
-    ballerina/lang.int:0.0.0:Signed32? semanticMaxWaitInMilliseconds?;
+    int:Signed32? semanticMaxWaitInMilliseconds?;
     # Allows setting a separate search query that will be solely used for semantic reranking, semantic captions and semantic answers. Is useful for scenarios where there is a need to use different queries between the base retrieval and ranking phase, and the L2 semantic phase.
     string semanticQuery?;
     # This parameter is only valid if the query type is `semantic`. If set, the query returns answers extracted from key passages in the highest ranked documents. The number of answers returned can be configured by appending the pipe character `|` followed by the `count-<number of answers>` option after the answers parameter value, such as `extractive|count-3`. Default count is 1. The confidence threshold can be configured by appending the pipe character `|` followed by the `threshold-<confidence threshold>` option after the answers parameter value, such as `extractive|threshold-0.9`. Default threshold is 0.7.
@@ -439,7 +440,7 @@
     # The kind of vector query being performed.
     VectorQueryKind kind;
     # Number of nearest neighbors to return as top hits.
-    ballerina/lang.int:0.0.0:Signed32 k?;
+    int:Signed32 k?;
     # Vector Fields of type Collection(Edm.Single) to be included in the vector searched.
     string fields?;
     # When true, triggers an exhaustive k-nearest neighbor search across all vectors within the vector index. Useful for scenarios where exact matches are critical, such as determining ground truth values.
@@ -591,7 +592,8 @@
 
 type DocumentsSearchGetQueries record {
     # Allows the user to set an upper bound on the amount of time it takes for semantic enrichment to finish processing before the request fails.
-    ballerina/lang.int:0.0.0:Signed32 semanticMaxWaitInMilliseconds?;
+    @constraint:Int {minValue: 700}
+    int:Signed32 semanticMaxWaitInMilliseconds?;
     # Client Api Version.
     string api\-version;
     # Allows setting a separate search query that will be solely used for semantic reranking, semantic captions and semantic answers. Is useful for scenarios where there is a need to use different queries between the base retrieval and ranking phase, and the L2 semantic phase.
@@ -611,7 +613,7 @@
     # A number between 0 and 100 indicating the percentage of the index that must be covered by a search query in order for the query to be reported as a success. This parameter can be useful for ensuring search availability even for services with only one replica. The default is 100.
     decimal minimumCoverage?;
     # The number of search results to skip. This value cannot be greater than 100,000. If you need to scan documents in sequence, but cannot use $skip due to this limitation, consider using $orderby on a totally-ordered key and $filter with a range query instead.
-    ballerina/lang.int:0.0.0:Signed32 \$skip?;
+    int:Signed32 \$skip?;
     # The list of parameter values to be used in scoring functions (for example, referencePointParameter) using the format name-values. For example, if the scoring profile defines a function with a parameter called 'mylocation' the parameter string would be "mylocation--122.2,44.8" (without the quotes).
     string[] scoringParameter?;
     # The list of field names to which to scope the full-text search. When using fielded search (fieldName:searchExpression) in a full Lucene query, the field names of each fielded search expression take precedence over any field names listed in this parameter.
@@ -619,7 +621,7 @@
     # The name of the semantic configuration that lists which fields should be used for semantic ranking, captions, highlights, and answers
     string semanticConfiguration?;
     # The number of search results to retrieve. This can be used in conjunction with $skip to implement client-side paging of search results. If results are truncated due to server-side paging, the response will include a continuation token that can be used to issue another Search request for the next page of results.
-    ballerina/lang.int:0.0.0:Signed32 \$top?;
+    int:Signed32 \$top?;
     # Enables a debugging tool that can be used to further explore your search results.
     "disabled"|"vector" debug?;
     # A value to be used to create a sticky session, which can help to get more consistent results. As long as the same sessionId is used, a best-effort attempt will be made to target the same replica set. Be wary that reusing the same sessionID values repeatedly can interfere with the load balancing of the requests across replicas and adversely affect the performance of the search service. The value used as sessionId cannot start with a '_' character.
@@ -668,7 +670,7 @@
     # The name of the suggester as specified in the suggesters collection that's part of the index definition.
     string suggesterName;
     # The number of auto-completed terms to retrieve. This must be a value between 1 and 100. The default is 5.
-    ballerina/lang.int:0.0.0:Signed32 top?;
+    int:Signed32 top?;
 };
 
 # Specifies the mode for Autocomplete. The default is 'oneTerm'. Use 'twoTerms' to get shingles and 'oneTermWithContext' to use the current context in producing autocomplete terms.
@@ -702,7 +704,7 @@
     # Specifies the mode for Autocomplete. The default is 'oneTerm'. Use 'twoTerms' to get shingles and 'oneTermWithContext' to use the current context while producing auto-completed terms.
     "oneTerm"|"twoTerms"|"oneTermWithContext" autocompleteMode?;
     # The number of auto-completed terms to retrieve. This must be a value between 1 and 100. The default is 5.
-    ballerina/lang.int:0.0.0:Signed32 \$top?;
+    int:Signed32 \$top?;
     # An OData expression that filters the documents used to produce completed terms for the Autocomplete result.
     string \$filter?;
     # The name of the suggester as specified in the suggesters collection that's part of the index definition.
@@ -757,15 +759,15 @@
     # The comma-separated list of fields to retrieve. If unspecified, all fields marked as retrievable in the schema are included.
     string 'select?;
     # The number of search results to skip. This value cannot be greater than 100,000. If you need to scan documents in sequence, but cannot use skip due to this limitation, consider using orderby on a totally-ordered key and filter with a range query instead.
-    ballerina/lang.int:0.0.0:Signed32 skip?;
+    int:Signed32 skip?;
     # The number of search results to retrieve. This can be used in conjunction with $skip to implement client-side paging of search results. If results are truncated due to server-side paging, the response will include a continuation token that can be used to issue another Search request for the next page of results.
-    ballerina/lang.int:0.0.0:Signed32 top?;
+    int:Signed32 top?;
     # The name of a semantic configuration that will be used when processing documents for queries of type semantic.
     string semanticConfiguration?;
     # Allows the user to choose whether a semantic call should fail completely, or to return partial results.
     SemanticErrorHandling semanticErrorHandling?;
     # Allows the user to set an upper bound on the amount of time it takes for semantic enrichment to finish processing before the request fails.
-    ballerina/lang.int:0.0.0:Signed32? semanticMaxWaitInMilliseconds?;
+    int:Signed32? semanticMaxWaitInMilliseconds?;
     # Allows setting a separate search query that will be solely used for semantic reranking, semantic captions and semantic answers. Is useful for scenarios where there is a need to use different queries between the base retrieval and ranking phase, and the L2 semantic phase.
     string semanticQuery?;
     # This parameter is only valid if the query type is `semantic`. If set, the query returns answers extracted from key passages in the highest ranked documents. The number of answers returned can be configured by appending the pipe character `|` followed by the `count-<number of answers>` option after the answers parameter value, such as `extractive|count-3`. Default count is 1. The confidence threshold can be configured by appending the pipe character `|` followed by the `threshold-<confidence threshold>` option after the answers parameter value, such as `extractive|threshold-0.9`. Default threshold is 0.7.
@@ -795,37 +797,37 @@
 
     # Queries the number of documents in the index.
     # 
-    remote function documentsCount(DocumentsCountHeaders headers = {}, string api\-version = "", anydata Additional Values, DocumentsCountQueries queries) returns int|error;
+    remote function documentsCount(DocumentsCountHeaders headers = {}, string api\-version = "", DocumentsCountQueries queries) returns int|error;
 
     # Searches for documents in the index.
     # 
-    remote function documentsSearchGet(DocumentsSearchGetHeaders headers = {}, int:Signed32 semanticMaxWaitInMilliseconds = 0, string api\-version = "", string semanticQuery = "", string scoringProfile = "", "any"|"all" searchMode = "any", "none"|"extractive" answers = "none", "none"|"extractive" captions = "none", string[] highlight = [], string search = "", decimal minimumCoverage = 0.0d, int:Signed32 \$skip = 0, string[] scoringParameter = [], string[] searchFields = [], string semanticConfiguration = "", int:Signed32 \$top = 0, "disabled"|"vector" debug = "disabled", string sessionId = "", string highlightPreTag = "", "partial"|"fail" semanticErrorHandling = "partial", "simple"|"full"|"semantic" queryType = "simple", "local"|"global" scoringStatistics = "local", string \$filter = "", string[] \$orderby = [], string highlightPostTag = "", string[] facet = [], boolean \$count = false, string[] \$select = [], anydata Additional Values, DocumentsSearchGetQueries queries) returns SearchDocumentsResult|error;
+    remote function documentsSearchGet(DocumentsSearchGetHeaders headers = {}, int:Signed32 semanticMaxWaitInMilliseconds = 0, string api\-version = "", string semanticQuery = "", string scoringProfile = "", "any"|"all" searchMode = "any", "none"|"extractive" answers = "none", "none"|"extractive" captions = "none", string[] highlight = [], string search = "", decimal minimumCoverage = 0.0d, int:Signed32 \$skip = 0, string[] scoringParameter = [], string[] searchFields = [], string semanticConfiguration = "", int:Signed32 \$top = 0, "disabled"|"vector" debug = "disabled", string sessionId = "", string highlightPreTag = "", "partial"|"fail" semanticErrorHandling = "partial", "simple"|"full"|"semantic" queryType = "simple", "local"|"global" scoringStatistics = "local", string \$filter = "", string[] \$orderby = [], string highlightPostTag = "", string[] facet = [], boolean \$count = false, string[] \$select = [], DocumentsSearchGetQueries queries) returns SearchDocumentsResult|error;
 
     # Searches for documents in the index.
     # 
-    remote function documentsSearchPost(docs_search_post_search_body payload, DocumentsSearchPostHeaders headers = {}, string api\-version = "", anydata Additional Values, DocumentsSearchPostQueries queries) returns SearchDocumentsResult|error;
+    remote function documentsSearchPost(docs_search_post_search_body payload, DocumentsSearchPostHeaders headers = {}, string api\-version = "", DocumentsSearchPostQueries queries) returns SearchDocumentsResult|error;
 
     # Retrieves a document from the index.
     # 
-    remote function documentsGet(string 'key, DocumentsGetHeaders headers = {}, string api\-version = "", string[] \$select = [], anydata Additional Values, DocumentsGetQueries queries) returns LookupDocument|error;
+    remote function documentsGet(string 'key, DocumentsGetHeaders headers = {}, string api\-version = "", string[] \$select = [], DocumentsGetQueries queries) returns LookupDocument|error;
 
     # Suggests documents in the index that match the given partial query text.
     # 
-    remote function documentsSuggestGet(DocumentsSuggestGetHeaders headers = {}, string api\-version = "", string search = "", decimal minimumCoverage = 0.0d, int:Signed32 \$top = 0, string \$filter = "", string[] \$orderby = [], string suggesterName = "", string highlightPostTag = "", string[] searchFields = [], string highlightPreTag = "", boolean fuzzy = false, string[] \$select = [], anydata Additional Values, DocumentsSuggestGetQueries queries) returns SuggestDocumentsResult|error;
+    remote function documentsSuggestGet(DocumentsSuggestGetHeaders headers = {}, string api\-version = "", string search = "", decimal minimumCoverage = 0.0d, int:Signed32 \$top = 0, string \$filter = "", string[] \$orderby = [], string suggesterName = "", string highlightPostTag = "", string[] searchFields = [], string highlightPreTag = "", boolean fuzzy = false, string[] \$select = [], DocumentsSuggestGetQueries queries) returns SuggestDocumentsResult|error;
 
     # Suggests documents in the index that match the given partial query text.
     # 
-    remote function documentsSuggestPost(SuggestRequest payload, DocumentsSuggestPostHeaders headers = {}, string api\-version = "", anydata Additional Values, DocumentsSuggestPostQueries queries) returns SuggestDocumentsResult|error;
+    remote function documentsSuggestPost(SuggestRequest payload, DocumentsSuggestPostHeaders headers = {}, string api\-version = "", DocumentsSuggestPostQueries queries) returns SuggestDocumentsResult|error;
 
     # Sends a batch of document write actions to the index.
     # 
-    remote function documentsIndex(IndexBatch payload, DocumentsIndexHeaders headers = {}, string api\-version = "", anydata Additional Values, DocumentsIndexQueries queries) returns IndexDocumentsResult|error;
+    remote function documentsIndex(IndexBatch payload, DocumentsIndexHeaders headers = {}, string api\-version = "", DocumentsIndexQueries queries) returns IndexDocumentsResult|error;
 
     # Autocompletes incomplete query terms based on input text and matching terms in the index.
     # 
-    remote function documentsAutocompleteGet(DocumentsAutocompleteGetHeaders headers = {}, string api\-version = "", string search = "", decimal minimumCoverage = 0.0d, "oneTerm"|"twoTerms"|"oneTermWithContext" autocompleteMode = "oneTerm", int:Signed32 \$top = 0, string \$filter = "", string suggesterName = "", string highlightPostTag = "", string[] searchFields = [], string highlightPreTag = "", boolean fuzzy = false, anydata Additional Values, DocumentsAutocompleteGetQueries queries) returns AutocompleteResult|error;
+    remote function documentsAutocompleteGet(DocumentsAutocompleteGetHeaders headers = {}, string api\-version = "", string search = "", decimal minimumCoverage = 0.0d, "oneTerm"|"twoTerms"|"oneTermWithContext" autocompleteMode = "oneTerm", int:Signed32 \$top = 0, string \$filter = "", string suggesterName = "", string highlightPostTag = "", string[] searchFields = [], string highlightPreTag = "", boolean fuzzy = false, DocumentsAutocompleteGetQueries queries) returns AutocompleteResult|error;
 
     # Autocompletes incomplete query terms based on input text and matching terms in the index.
     # 
-    remote function documentsAutocompletePost(AutocompleteRequest payload, DocumentsAutocompletePostHeaders headers = {}, string api\-version = "", anydata Additional Values, DocumentsAutocompletePostQueries queries) returns AutocompleteResult|error;
+    remote function documentsAutocompletePost(AutocompleteRequest payload, DocumentsAutocompletePostHeaders headers = {}, string api\-version = "", DocumentsAutocompletePostQueries queries) returns AutocompleteResult|error;
 }
`````

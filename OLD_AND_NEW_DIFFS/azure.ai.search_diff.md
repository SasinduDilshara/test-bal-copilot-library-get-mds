# azure.ai.search — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `azure.ai.search` |
| **Old file** | `azure.ai.search/old/ballerinax_azure.ai.search.bal.txt` |
| **New file** | `azure.ai.search/new/ballerinax_azure.ai.search.bal.txt` |
| **Old lines** | 1856 |
| **New lines** | 1859 |
| **Lines added** | 51 |
| **Lines removed** | 48 |
| **Hunks** | 11 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 15 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (2)

- `type CharFilterName`
- `type VectorEncodingFormat`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 357–367 | 357–367 | Types | +3 | −3 |
| 2 | 413–423 | 413–423 | Types | +3 | −3 |
| 3 | 585–590 | 585–591 | Types | +1 | −0 |
| 4 | 752–760 | 753–761 | Types | +2 | −2 |
| 5 | 772–778 | 773–779 | Types | +1 | −1 |
| 6 | 843–849 | 844–850 | Types | +1 | −1 |
| 7 | 1016–1022 | 1017–1023 | Types | +1 | −1 |
| 8 | 1030–1036 | 1031–1038 | Types | +2 | −1 |
| 9 | 1420–1426 | 1422–1429 | Types | +2 | −1 |
| 10 | 1662–1674 | 1665–1677 | Types | +4 | −4 |
| 11 | 1732–1856 | 1735–1859 | Client | +31 | −31 |

---

## Unified diff

`````diff
--- azure.ai.search/old/ballerinax_azure.ai.search.bal.txt	2026-08-12 12:57:30
+++ azure.ai.search/new/ballerinax_azure.ai.search.bal.txt	2026-08-12 13:19:19
@@ -357,11 +357,11 @@
     # The token returned by the analyzer.
     string token;
     # The index of the first character of the token in the input text.
-    ballerina/lang.int:0.0.0:Signed32 startOffset;
+    int:Signed32 startOffset;
     # The index of the last character of the token in the input text.
-    ballerina/lang.int:0.0.0:Signed32 endOffset;
+    int:Signed32 endOffset;
     # The position of the token in the input text relative to other tokens. The first token in the input text has position 0, the next has position 1, and so on. Depending on the analyzer used, some tokens might have the same position, for example if they are synonyms of each other.
-    ballerina/lang.int:0.0.0:Signed32 position;
+    int:Signed32 position;
 };
 
 # Response from a List Indexers request. If successful, it includes the full definitions of all indexers.
@@ -413,11 +413,11 @@
 
 type IndexingParameters record {
     # The number of items that are read from the data source and indexed as a single batch in order to improve performance. The default depends on the data source type.
-    ballerina/lang.int:0.0.0:Signed32? batchSize?;
+    int:Signed32? batchSize?;
     # The maximum number of items that can fail indexing for indexer execution to still be considered successful. -1 means no limit. Default is 0.
-    ballerina/lang.int:0.0.0:Signed32? maxFailedItems?;
+    int:Signed32? maxFailedItems?;
     # The maximum number of items in a single batch that can fail indexing for the batch to still be considered successful. -1 means no limit. Default is 0.
-    ballerina/lang.int:0.0.0:Signed32? maxFailedItemsPerBatch?;
+    int:Signed32? maxFailedItemsPerBatch?;
     # A dictionary of indexer-specific configuration properties. Each name is the name of a specific property. Each value must be of a primitive type.
     IndexingParametersConfiguration configuration?;
 };
@@ -585,6 +585,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
@@ -752,9 +753,9 @@
     # The item-level indexing warnings.
     SearchIndexerWarning[] warnings;
     # The number of items that were processed during this indexer execution. This includes both successfully processed items and items where indexing was attempted but failed.
-    ballerina/lang.int:0.0.0:Signed32 itemsProcessed;
+    int:Signed32 itemsProcessed;
     # The number of items that failed to be indexed during this indexer execution.
-    ballerina/lang.int:0.0.0:Signed32 itemsFailed;
+    int:Signed32 itemsFailed;
     # Change tracking state with which an indexer execution started.
     string initialTrackingState?;
     # Change tracking state with which an indexer execution finished.
@@ -772,7 +773,7 @@
     # The message describing the error that occurred while processing the item.
     string errorMessage;
     # The status code indicating why the indexing operation failed. Possible values include: 400 for a malformed input document, 404 for document not found, 409 for a version conflict, 422 when the index is temporarily unavailable, or 503 for when the service is too busy.
-    ballerina/lang.int:0.0.0:Signed32 statusCode;
+    int:Signed32 statusCode;
     # The name of the source at which the error originated. For example, this could refer to a particular skill in the attached skillset. This may not be always available.
     string name?;
     # Additional, verbose details about the error to assist in debugging the indexer. This may not be always available.
@@ -843,7 +844,7 @@
     # Contains the options for rescoring.
     RescoringOptions rescoringOptions?;
     # The number of dimensions to truncate the vectors to. Truncating the vectors reduces the size of the vectors and the amount of data that needs to be transferred during search. This can save storage cost and improve search performance at the expense of recall. It should be only used for embeddings trained with Matryoshka Representation Learning (MRL) such as OpenAI text-embedding-3-large (small). The default value is null, which means no truncation.
-    ballerina/lang.int:0.0.0:Signed32? truncationDimension?;
+    int:Signed32? truncationDimension?;
 };
 
 # The compression method used for indexing and querying.
@@ -1016,7 +1017,7 @@
     # Defines the names of all text normalizers supported by the search engine.
     LexicalNormalizerName normalizer?;
     # The dimensionality of the vector field.
-    ballerina/lang.int:0.0.0:Signed32? dimensions?;
+    int:Signed32? dimensions?;
     # The name of the vector search profile that specifies the algorithm and vectorizer to use when searching the vector field.
     string? vectorSearchProfile?;
     # The encoding format for interpreting vector field contents.
@@ -1030,7 +1031,8 @@
 # Defines the names of all text normalizers supported by the search engine.
 type LexicalNormalizerName "asciifolding"|"elision"|"lowercase"|"standard"|"uppercase";
 
-// Unknown type: VectorEncodingFormat
+# The encoding format for interpreting vector field contents.
+type VectorEncodingFormat "packedBit";
 
 # Defines parameters for a search index that influence scoring in search queries.
 
@@ -1420,7 +1422,8 @@
     string x\-ms\-client\-request\-id?;
 };
 
-// Unknown type: CharFilterName
+# Defines the names of all character filters supported by the search engine.
+type CharFilterName "html_strip";
 
 # Represents the Queries record for the operation: indexersRun
 
@@ -1662,13 +1665,13 @@
 
 type ServiceLimits record {
     # The maximum allowed fields per index.
-    ballerina/lang.int:0.0.0:Signed32? maxFieldsPerIndex?;
+    int:Signed32? maxFieldsPerIndex?;
     # The maximum depth which you can nest sub-fields in an index, including the top-level complex field. For example, a/b/c has a nesting depth of 3.
-    ballerina/lang.int:0.0.0:Signed32? maxFieldNestingDepthPerIndex?;
+    int:Signed32? maxFieldNestingDepthPerIndex?;
     # The maximum number of fields of type Collection(Edm.ComplexType) allowed in an index.
-    ballerina/lang.int:0.0.0:Signed32? maxComplexCollectionFieldsPerIndex?;
+    int:Signed32? maxComplexCollectionFieldsPerIndex?;
     # The maximum number of objects in complex collections allowed per document.
-    ballerina/lang.int:0.0.0:Signed32? maxComplexObjectsInCollectionsPerDocument?;
+    int:Signed32? maxComplexObjectsInCollectionsPerDocument?;
     # The maximum amount of storage in bytes allowed per index.
     int? maxStoragePerIndex?;
 };
@@ -1732,125 +1735,125 @@
 
     # Retrieves a datasource definition.
     # 
-    remote function dataSourcesGet(string dataSourceName, DataSourcesGetHeaders headers = {}, string api\-version = "", anydata Additional Values, DataSourcesGetQueries queries) returns SearchIndexerDataSource|error;
+    remote function dataSourcesGet(string dataSourceName, DataSourcesGetHeaders headers = {}, string api\-version = "", DataSourcesGetQueries queries) returns SearchIndexerDataSource|error;
 
     # Creates a new datasource or updates a datasource if it already exists.
     # 
-    remote function dataSourcesCreateOrUpdate(string dataSourceName, DataSourcesCreateOrUpdateHeaders headers, SearchIndexerDataSource payload, string api\-version = "", anydata Additional Values, DataSourcesCreateOrUpdateQueries queries) returns SearchIndexerDataSource|error;
+    remote function dataSourcesCreateOrUpdate(string dataSourceName, DataSourcesCreateOrUpdateHeaders headers, SearchIndexerDataSource payload, string api\-version = "", DataSourcesCreateOrUpdateQueries queries) returns SearchIndexerDataSource|error;
 
     # Deletes a datasource.
     # 
-    remote function dataSourcesDelete(string dataSourceName, DataSourcesDeleteHeaders headers = {}, string api\-version = "", anydata Additional Values, DataSourcesDeleteQueries queries) returns error?;
+    remote function dataSourcesDelete(string dataSourceName, DataSourcesDeleteHeaders headers = {}, string api\-version = "", DataSourcesDeleteQueries queries) returns error?;
 
     # Lists all datasources available for a search service.
     # 
-    remote function dataSourcesList(DataSourcesListHeaders headers = {}, string api\-version = "", string \$select = "", anydata Additional Values, DataSourcesListQueries queries) returns ListDataSourcesResult|error;
+    remote function dataSourcesList(DataSourcesListHeaders headers = {}, string api\-version = "", string \$select = "", DataSourcesListQueries queries) returns ListDataSourcesResult|error;
 
     # Creates a new datasource.
     # 
-    remote function dataSourcesCreate(SearchIndexerDataSource payload, DataSourcesCreateHeaders headers = {}, string api\-version = "", anydata Additional Values, DataSourcesCreateQueries queries) returns SearchIndexerDataSource|error;
+    remote function dataSourcesCreate(SearchIndexerDataSource payload, DataSourcesCreateHeaders headers = {}, string api\-version = "", DataSourcesCreateQueries queries) returns SearchIndexerDataSource|error;
 
     # Resets the change tracking state associated with an indexer.
     # 
-    remote function indexersReset(string indexerName, IndexersResetHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersResetQueries queries) returns error?;
+    remote function indexersReset(string indexerName, IndexersResetHeaders headers = {}, string api\-version = "", IndexersResetQueries queries) returns error?;
 
     # Runs an indexer on-demand.
     # 
-    remote function indexersRun(string indexerName, IndexersRunHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersRunQueries queries) returns error?;
+    remote function indexersRun(string indexerName, IndexersRunHeaders headers = {}, string api\-version = "", IndexersRunQueries queries) returns error?;
 
     # Retrieves an indexer definition.
     # 
-    remote function indexersGet(string indexerName, IndexersGetHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersGetQueries queries) returns SearchIndexer|error;
+    remote function indexersGet(string indexerName, IndexersGetHeaders headers = {}, string api\-version = "", IndexersGetQueries queries) returns SearchIndexer|error;
 
     # Creates a new indexer or updates an indexer if it already exists.
     # 
-    remote function indexersCreateOrUpdate(string indexerName, IndexersCreateOrUpdateHeaders headers, SearchIndexer payload, string api\-version = "", anydata Additional Values, IndexersCreateOrUpdateQueries queries) returns SearchIndexer|error;
+    remote function indexersCreateOrUpdate(string indexerName, IndexersCreateOrUpdateHeaders headers, SearchIndexer payload, string api\-version = "", IndexersCreateOrUpdateQueries queries) returns SearchIndexer|error;
 
     # Deletes an indexer.
     # 
-    remote function indexersDelete(string indexerName, IndexersDeleteHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersDeleteQueries queries) returns error?;
+    remote function indexersDelete(string indexerName, IndexersDeleteHeaders headers = {}, string api\-version = "", IndexersDeleteQueries queries) returns error?;
 
     # Lists all indexers available for a search service.
     # 
-    remote function indexersList(IndexersListHeaders headers = {}, string api\-version = "", string \$select = "", anydata Additional Values, IndexersListQueries queries) returns ListIndexersResult|error;
+    remote function indexersList(IndexersListHeaders headers = {}, string api\-version = "", string \$select = "", IndexersListQueries queries) returns ListIndexersResult|error;
 
     # Creates a new indexer.
     # 
-    remote function indexersCreate(SearchIndexer payload, IndexersCreateHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersCreateQueries queries) returns SearchIndexer|error;
+    remote function indexersCreate(SearchIndexer payload, IndexersCreateHeaders headers = {}, string api\-version = "", IndexersCreateQueries queries) returns SearchIndexer|error;
 
     # Returns the current status and execution history of an indexer.
     # 
-    remote function indexersGetStatus(string indexerName, IndexersGetStatusHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexersGetStatusQueries queries) returns SearchIndexerStatus|error;
+    remote function indexersGetStatus(string indexerName, IndexersGetStatusHeaders headers = {}, string api\-version = "", IndexersGetStatusQueries queries) returns SearchIndexerStatus|error;
 
     # Retrieves a skillset in a search service.
     # 
-    remote function skillsetsGet(string skillsetName, SkillsetsGetHeaders headers = {}, string api\-version = "", anydata Additional Values, SkillsetsGetQueries queries) returns SearchIndexerSkillset|error;
+    remote function skillsetsGet(string skillsetName, SkillsetsGetHeaders headers = {}, string api\-version = "", SkillsetsGetQueries queries) returns SearchIndexerSkillset|error;
 
     # Creates a new skillset in a search service or updates the skillset if it already exists.
     # 
-    remote function skillsetsCreateOrUpdate(string skillsetName, SkillsetsCreateOrUpdateHeaders headers, SearchIndexerSkillset payload, string api\-version = "", anydata Additional Values, SkillsetsCreateOrUpdateQueries queries) returns SearchIndexerSkillset|error;
+    remote function skillsetsCreateOrUpdate(string skillsetName, SkillsetsCreateOrUpdateHeaders headers, SearchIndexerSkillset payload, string api\-version = "", SkillsetsCreateOrUpdateQueries queries) returns SearchIndexerSkillset|error;
 
     # Deletes a skillset in a search service.
     # 
-    remote function skillsetsDelete(string skillsetName, SkillsetsDeleteHeaders headers = {}, string api\-version = "", anydata Additional Values, SkillsetsDeleteQueries queries) returns error?;
+    remote function skillsetsDelete(string skillsetName, SkillsetsDeleteHeaders headers = {}, string api\-version = "", SkillsetsDeleteQueries queries) returns error?;
 
     # List all skillsets in a search service.
     # 
-    remote function skillsetsList(SkillsetsListHeaders headers = {}, string api\-version = "", string \$select = "", anydata Additional Values, SkillsetsListQueries queries) returns ListSkillsetsResult|error;
+    remote function skillsetsList(SkillsetsListHeaders headers = {}, string api\-version = "", string \$select = "", SkillsetsListQueries queries) returns ListSkillsetsResult|error;
 
     # Creates a new skillset in a search service.
     # 
-    remote function skillsetsCreate(SearchIndexerSkillset payload, SkillsetsCreateHeaders headers = {}, string api\-version = "", anydata Additional Values, SkillsetsCreateQueries queries) returns SearchIndexerSkillset|error;
+    remote function skillsetsCreate(SearchIndexerSkillset payload, SkillsetsCreateHeaders headers = {}, string api\-version = "", SkillsetsCreateQueries queries) returns SearchIndexerSkillset|error;
 
     # Retrieves a synonym map definition.
     # 
-    remote function synonymMapsGet(string synonymMapName, SynonymMapsGetHeaders headers = {}, string api\-version = "", anydata Additional Values, SynonymMapsGetQueries queries) returns SynonymMap|error;
+    remote function synonymMapsGet(string synonymMapName, SynonymMapsGetHeaders headers = {}, string api\-version = "", SynonymMapsGetQueries queries) returns SynonymMap|error;
 
     # Creates a new synonym map or updates a synonym map if it already exists.
     # 
-    remote function synonymMapsCreateOrUpdate(string synonymMapName, SynonymMapsCreateOrUpdateHeaders headers, SynonymMap payload, string api\-version = "", anydata Additional Values, SynonymMapsCreateOrUpdateQueries queries) returns SynonymMap|error;
+    remote function synonymMapsCreateOrUpdate(string synonymMapName, SynonymMapsCreateOrUpdateHeaders headers, SynonymMap payload, string api\-version = "", SynonymMapsCreateOrUpdateQueries queries) returns SynonymMap|error;
 
     # Deletes a synonym map.
     # 
-    remote function synonymMapsDelete(string synonymMapName, SynonymMapsDeleteHeaders headers = {}, string api\-version = "", anydata Additional Values, SynonymMapsDeleteQueries queries) returns error?;
+    remote function synonymMapsDelete(string synonymMapName, SynonymMapsDeleteHeaders headers = {}, string api\-version = "", SynonymMapsDeleteQueries queries) returns error?;
 
     # Lists all synonym maps available for a search service.
     # 
-    remote function synonymMapsList(SynonymMapsListHeaders headers = {}, string api\-version = "", string \$select = "", anydata Additional Values, SynonymMapsListQueries queries) returns ListSynonymMapsResult|error;
+    remote function synonymMapsList(SynonymMapsListHeaders headers = {}, string api\-version = "", string \$select = "", SynonymMapsListQueries queries) returns ListSynonymMapsResult|error;
 
     # Creates a new synonym map.
     # 
-    remote function synonymMapsCreate(SynonymMap payload, SynonymMapsCreateHeaders headers = {}, string api\-version = "", anydata Additional Values, SynonymMapsCreateQueries queries) returns SynonymMap|error;
+    remote function synonymMapsCreate(SynonymMap payload, SynonymMapsCreateHeaders headers = {}, string api\-version = "", SynonymMapsCreateQueries queries) returns SynonymMap|error;
 
     # Lists all indexes available for a search service.
     # 
-    remote function indexesList(IndexesListHeaders headers = {}, string api\-version = "", string \$select = "", anydata Additional Values, IndexesListQueries queries) returns ListIndexesResult|error;
+    remote function indexesList(IndexesListHeaders headers = {}, string api\-version = "", string \$select = "", IndexesListQueries queries) returns ListIndexesResult|error;
 
     # Creates a new search index.
     # 
-    remote function indexesCreate(SearchIndex payload, IndexesCreateHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexesCreateQueries queries) returns SearchIndex|error;
+    remote function indexesCreate(SearchIndex payload, IndexesCreateHeaders headers = {}, string api\-version = "", IndexesCreateQueries queries) returns SearchIndex|error;
 
     # Retrieves an index definition.
     # 
-    remote function indexesGet(string indexName, IndexesGetHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexesGetQueries queries) returns SearchIndex|error;
+    remote function indexesGet(string indexName, IndexesGetHeaders headers = {}, string api\-version = "", IndexesGetQueries queries) returns SearchIndex|error;
 
     # Creates a new search index or updates an index if it already exists.
     # 
-    remote function indexesCreateOrUpdate(string indexName, IndexesCreateOrUpdateHeaders headers, SearchIndex payload, string api\-version = "", boolean allowIndexDowntime = false, anydata Additional Values, IndexesCreateOrUpdateQueries queries) returns SearchIndex|error;
+    remote function indexesCreateOrUpdate(string indexName, IndexesCreateOrUpdateHeaders headers, SearchIndex payload, string api\-version = "", boolean allowIndexDowntime = false, IndexesCreateOrUpdateQueries queries) returns SearchIndex|error;
 
     # Deletes a search index and all the documents it contains. This operation is permanent, with no recovery option. Make sure you have a master copy of your index definition, data ingestion code, and a backup of the primary data source in case you need to re-build the index.
     # 
-    remote function indexesDelete(string indexName, IndexesDeleteHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexesDeleteQueries queries) returns error?;
+    remote function indexesDelete(string indexName, IndexesDeleteHeaders headers = {}, string api\-version = "", IndexesDeleteQueries queries) returns error?;
 
     # Returns statistics for the given index, including a document count and storage usage.
     # 
-    remote function indexesGetStatistics(string indexName, IndexesGetStatisticsHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexesGetStatisticsQueries queries) returns GetIndexStatisticsResult|error;
+    remote function indexesGetStatistics(string indexName, IndexesGetStatisticsHeaders headers = {}, string api\-version = "", IndexesGetStatisticsQueries queries) returns GetIndexStatisticsResult|error;
 
     # Shows how an analyzer breaks text into tokens.
     # 
-    remote function indexesAnalyze(string indexName, AnalyzeRequest payload, IndexesAnalyzeHeaders headers = {}, string api\-version = "", anydata Additional Values, IndexesAnalyzeQueries queries) returns AnalyzeResult|error;
+    remote function indexesAnalyze(string indexName, AnalyzeRequest payload, IndexesAnalyzeHeaders headers = {}, string api\-version = "", IndexesAnalyzeQueries queries) returns AnalyzeResult|error;
 
     # Gets service level statistics for a search service.
     # 
-    remote function getServiceStatistics(GetServiceStatisticsHeaders headers = {}, string api\-version = "", anydata Additional Values, GetServiceStatisticsQueries queries) returns ServiceStatistics|error;
+    remote function getServiceStatistics(GetServiceStatisticsHeaders headers = {}, string api\-version = "", GetServiceStatisticsQueries queries) returns ServiceStatistics|error;
 }
`````

# mistral — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mistral` |
| **Old file** | `mistral/old/ballerinax_mistral.bal.txt` |
| **New file** | `mistral/new/ballerinax_mistral.bal.txt` |
| **Old lines** | 1248 |
| **New lines** | 1409 |
| **Lines added** | 175 |
| **Lines removed** | 14 |
| **Hunks** | 55 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 14 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type ToolTypes`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 100–105 | 100–106 | Types | +1 | −0 |
| 2 | 117–123 | 118–124 | Types | +1 | −1 |
| 3 | 129–134 | 130–136 | Types | +1 | −0 |
| 4 | 139–144 | 141–147 | Types | +1 | −0 |
| 5 | 152–157 | 155–161 | Types | +1 | −0 |
| 6 | 165–182 | 169–189 | Types | +4 | −1 |
| 7 | 191–196 | 198–204 | Types | +1 | −0 |
| 8 | 201–206 | 209–215 | Types | +1 | −0 |
| 9 | 208–241 | 217–260 | Types | +10 | −0 |
| 10 | 244–249 | 263–269 | Types | +1 | −0 |
| 11 | 255–260 | 275–281 | Types | +1 | −0 |
| 12 | 262–271 | 283–295 | Types | +3 | −0 |
| 13 | 274–281 | 298–307 | Types | +2 | −0 |
| 14 | 289–299 | 315–328 | Types | +3 | −0 |
| 15 | 308–328 | 337–364 | Types | +7 | −0 |
| 16 | 367–380 | 403–421 | Types | +5 | −0 |
| 17 | 397–402 | 438–444 | Types | +1 | −0 |
| 18 | 410–417 | 452–462 | Types | +3 | −0 |
| 19 | 425–431 | 470–476 | Types | +1 | −1 |
| 20 | 439–452 | 484–499 | Types | +3 | −1 |
| 21 | 455–465 | 502–514 | Types | +2 | −0 |
| 22 | 470–480 | 519–532 | Types | +3 | −0 |
| 23 | 484–493 | 536–549 | Types | +4 | −0 |
| 24 | 498–517 | 554–576 | Types | +4 | −1 |
| 25 | 545–551 | 604–610 | Types | +1 | −1 |
| 26 | 562–606 | 621–681 | Types | +16 | −0 |
| 27 | 609–616 | 684–694 | Types | +3 | −0 |
| 28 | 619–626 | 697–706 | Types | +2 | −0 |
| 29 | 629–647 | 709–735 | Types | +8 | −0 |
| 30 | 655–660 | 743–749 | Types | +1 | −0 |
| 31 | 674–679 | 763–769 | Types | +1 | −0 |
| 32 | 687–697 | 777–790 | Types | +3 | −0 |
| 33 | 699–707 | 792–802 | Types | +2 | −0 |
| 34 | 722–737 | 817–837 | Types | +5 | −0 |
| 35 | 740–753 | 840–856 | Types | +3 | −0 |
| 36 | 760–766 | 863–871 | Types | +2 | −0 |
| 37 | 769–774 | 874–880 | Types | +1 | −0 |
| 38 | 779–790 | 885–899 | Types | +3 | −0 |
| 39 | 794–803 | 903–915 | Types | +3 | −0 |
| 40 | 805–827 | 917–946 | Types | +7 | −0 |
| 41 | 851–871 | 970–994 | Types | +5 | −1 |
| 42 | 894–910 | 1017–1043 | Types | +10 | −0 |
| 43 | 921–926 | 1054–1060 | Types | +1 | −0 |
| 44 | 956–979 | 1090–1117 | Types | +4 | −0 |
| 45 | 1000–1011 | 1138–1152 | Types | +3 | −0 |
| 46 | 1020–1045 | 1161–1193 | Types | +8 | −1 |
| 47 | 1048–1053 | 1196–1202 | Types | +1 | −0 |
| 48 | 1056–1075 | 1205–1231 | Types | +7 | −0 |
| 49 | 1080–1085 | 1236–1242 | Types | +1 | −0 |
| 50 | 1093–1099 | 1250–1258 | Types | +2 | −0 |
| 51 | 1104–1111 | 1263–1272 | Types | +2 | −0 |
| 52 | 1117–1123 | 1278–1284 | Types | +1 | −1 |
| 53 | 1148–1154 | 1309–1315 | Client | +1 | −1 |
| 54 | 1168–1182 | 1329–1343 | Client | +3 | −3 |
| 55 | 1204–1210 | 1365–1371 | Client | +1 | −1 |

---

## Unified diff

`````diff
--- mistral/old/ballerinax_mistral.bal.txt	2026-08-12 12:57:30
+++ mistral/new/ballerinax_mistral.bal.txt	2026-08-12 13:19:19
@@ -100,6 +100,7 @@
 for the user to perform sanity checks (see `LegacyJobMetadataOut` response).
 * Otherwise, the job is started and the query returns the job ID along with some of the
 input parameters (see `JobOut` response)
+    @http:Query {name: "dry_run"}
     boolean? dryRun?;
 };
 
@@ -117,7 +118,7 @@
     record {|anydata...;|}|string arguments;
 };
 
-// Unknown type: ToolTypes
+type ToolTypes "function";
 
 
 type JsonSchema record {
@@ -129,6 +130,7 @@
 
 
 type ChatCompletionChoice record {
+    @jsondata:Name {value: "finish_reason"}
     "stop"|"length"|"model_length"|"error"|"tool_calls" finishReason;
     int index;
     AssistantMessage message;
@@ -139,6 +141,7 @@
     "assistant" role?;
     # Set this to `true` when adding an assistant message as prefix to condition the model response. The role of the prefix message is to force the model to start its answer by the content of the message
     boolean prefix?;
+    @jsondata:Name {value: "tool_calls"}
     ToolCall[]|() toolCalls?;
     string|ContentChunk[]|() content?;
 };
@@ -152,6 +155,7 @@
 # {"type":"image_url","image_url":{"url":"data:image/png;base64,iVBORw0
 
 type ImageURLChunk record {
+    @jsondata:Name {value: "image_url"}
     ImageURL|string imageUrl;
     "image_url" 'type?;
 };
@@ -165,18 +169,21 @@
 
 type DocumentURLChunk record {
     # The filename of the document
+    @jsondata:Name {value: "document_name"}
     string? documentName?;
     string 'type?;
+    @jsondata:Name {value: "document_url"}
     string documentUrl;
 };
 
 
 type ReferenceChunk record {
+    @jsondata:Name {value: "reference_ids"}
     int[] referenceIds;
     "reference" 'type?;
 };
 
-type ContentChunk ballerinax/mistral:1.0.2:TextChunk|ballerinax/mistral:1.0.2:ImageURLChunk|ballerinax/mistral:1.0.2:DocumentURLChunk|ballerinax/mistral:1.0.2:ReferenceChunk;
+type ContentChunk TextChunk|ImageURLChunk|DocumentURLChunk|ReferenceChunk;
 
 
 type ArchiveFTModelOut record {
@@ -191,6 +198,7 @@
     OCRPageObject[] pages;
     # The model used to generate the OCR
     string model;
+    @jsondata:Name {value: "usage_info"}
     OCRUsageInfo usageInfo;
 };
 
@@ -201,6 +209,7 @@
     # The markdown string response of the page
     string markdown;
     # The page index in a pdf document starting from 0
+    @constraint:Int {minValue: 0}
     int index;
     OCRPageDimensions dimensions;
 };
@@ -208,34 +217,44 @@
 
 type OCRImageObject record {
     # X coordinate of bottom-right corner of the extracted image
+    @jsondata:Name {value: "bottom_right_x"}
     int? bottomRightX;
     # Y coordinate of bottom-right corner of the extracted image
+    @jsondata:Name {value: "bottom_right_y"}
     int? bottomRightY;
     # Base64 string of the extracted image
+    @jsondata:Name {value: "image_base64"}
     string? imageBase64?;
     # Y coordinate of top-left corner of the extracted image
+    @jsondata:Name {value: "top_left_y"}
     int? topLeftY;
     # Image ID for extracted image in a page
     string id;
     # X coordinate of top-left corner of the extracted image
+    @jsondata:Name {value: "top_left_x"}
     int? topLeftX;
 };
 
 
 type OCRPageDimensions record {
     # Width of the image in pixels
+    @constraint:Int {minValue: 0}
     int width;
     # Dots per inch of the page-image
+    @constraint:Int {minValue: 0}
     int dpi;
     # Height of the image in pixels
+    @constraint:Int {minValue: 0}
     int height;
 };
 
 
 type OCRUsageInfo record {
     # Number of pages processed
+    @jsondata:Name {value: "pages_processed"}
     int pagesProcessed;
     # Document size in bytes
+    @jsondata:Name {value: "doc_size_bytes"}
     int? docSizeBytes?;
 };
 
@@ -244,6 +263,7 @@
     string owner;
     string? ref?;
     string name;
+    @constraint:Number {minValueExclusive: 0}
     decimal weight?;
     "github" 'type?;
     string token;
@@ -255,6 +275,7 @@
     # The name of the event
     string name;
     # The UNIX timestamp (in seconds) of the event
+    @jsondata:Name {value: "created_at"}
     int createdAt;
 };
 
@@ -262,10 +283,13 @@
 
 type JobsApiRoutesFineTuningGetFineTuningJobsQueries record {
     # The Weights and Biases project to filter on. When set, the other results are not displayed
+    @http:Query {name: "wandb_project"}
     string? wandbProject?;
     # The Weight and Biases run name to filter on. When set, the other results are not displayed
+    @http:Query {name: "wandb_name"}
     string? wandbName?;
     # The date/time to filter on. When set, the results for previous creation times are not displayed
+    @http:Query {name: "created_after"}
     string? createdAfter?;
     # The model name used for fine-tuning to filter on. When set, the other results are not displayed
     string? model?;
@@ -274,8 +298,10 @@
     # The model suffix to filter on. When set, the other results are not displayed
     string? suffix?;
     # When set, only return results for jobs created by the API caller. Other results are not displayed
+    @http:Query {name: "created_by_me"}
     boolean createdByMe?;
     # The number of items to return per page
+    @http:Query {name: "page_size"}
     int pageSize?;
     # The current job state to filter on. When set, the other results are not displayed
     "CANCELLATION_REQUESTED"?|"QUEUED"|"STARTED"|"VALIDATING"|"VALIDATED"|"RUNNING"|"FAILED_VALIDATION"|"FAILED"|"SUCCESS"|"CANCELLED" status?;
@@ -289,11 +315,14 @@
     # The size of the file, in bytes
     int bytes;
     # The UNIX timestamp (in seconds) of the event
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The unique identifier of the file
     string id;
     Source 'source;
+    @jsondata:Name {value: "sample_type"}
     SampleType sampleType;
+    @jsondata:Name {value: "num_lines"}
     int? numLines?;
     # The object type, which is always "file"
     string 'object;
@@ -308,21 +337,28 @@
 # The fine-tuning hyperparameter settings used in a fine-tune job
 
 type TrainingParametersIn record {
+    @jsondata:Name {value: "fim_ratio"}
     decimal? fimRatio?;
     # (Advanced Usage) Weight decay adds a term to the loss function that is proportional to the sum of the squared weights. This term reduces the magnitude of the weights and prevents them from growing too large
+    @jsondata:Name {value: "weight_decay"}
     decimal? weightDecay?;
     # The number of training steps to perform. A training step refers to a single update of the model weights during the fine-tuning process. This update is typically calculated using a batch of samples from the training dataset
+    @jsondata:Name {value: "training_steps"}
     int? trainingSteps?;
     # A parameter describing how much to adjust the pre-trained model's weights in response to the estimated error each time the weights are updated during the fine-tuning process
+    @jsondata:Name {value: "learning_rate"}
     decimal learningRate?;
     decimal? epochs?;
+    @jsondata:Name {value: "seq_len"}
     int? seqLen?;
     # (Advanced Usage) A parameter that specifies the percentage of the total training steps at which the learning rate warm-up phase ends. During this phase, the learning rate gradually increases from a small value to the initial learning rate, helping to stabilize the training process and improve convergence. Similar to `pct_start` in [mistral-finetune](https://github.com/mistralai/mistral-finetune)
+    @jsondata:Name {value: "warmup_fraction"}
     decimal? warmupFraction?;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -367,14 +403,19 @@
 
 
 type FTModelCapabilitiesOut record {
+    @jsondata:Name {value: "completion_chat"}
     boolean completionChat?;
+    @jsondata:Name {value: "function_calling"}
     boolean functionCalling?;
+    @jsondata:Name {value: "fine_tuning"}
     boolean fineTuning?;
+    @jsondata:Name {value: "completion_fim"}
     boolean completionFim?;
 };
 
 
 type ResponseFormat record {
+    @jsondata:Name {value: "json_schema"}
     JsonSchema jsonSchema?;
     # An object specifying the format that the model must output. Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is in JSON. When using JSON mode you MUST also instruct the model to produce JSON yourself with a system or a user message
     ResponseFormats 'type?;
@@ -397,6 +438,7 @@
     # The name of the project that the new run will be created under
     string project;
     "wandb" 'type?;
+    @jsondata:Name {value: "run_name"}
     string? runName?;
 };
 
@@ -410,8 +452,11 @@
 
 
 type UsageInfo record {
+    @jsondata:Name {value: "completion_tokens"}
     int completionTokens;
+    @jsondata:Name {value: "prompt_tokens"}
     int promptTokens;
+    @jsondata:Name {value: "total_tokens"}
     int totalTokens;
 };
 
@@ -425,7 +470,7 @@
     UsageInfo usage?;
     string model?;
     string id?;
-    string object?;
+    string 'object?;
     int created?;
 };
 
@@ -439,14 +484,16 @@
     UsageInfo usage?;
     string model?;
     string id?;
-    string object?;
+    string 'object?;
     int created?;
     ChatCompletionChoice[] choices?;
 };
 
 
 type TrainingFile record {
+    @jsondata:Name {value: "file_id"}
     string fileId;
+    @constraint:Number {minValueExclusive: 0}
     decimal weight?;
 };
 
@@ -455,11 +502,13 @@
     boolean archived;
     FTModelCapabilitiesOut capabilities;
     string[] aliases?;
+    @jsondata:Name {value: "max_context_length"}
     int maxContextLength?;
     int created;
     string root;
     string? name?;
     string? description?;
+    @jsondata:Name {value: "owned_by"}
     string ownedBy;
     string id;
     string job;
@@ -470,11 +519,14 @@
 type BaseModelCard record {
     ModelCapabilities capabilities;
     string[] aliases?;
+    @jsondata:Name {value: "max_context_length"}
     int maxContextLength?;
     int created?;
     string? name?;
+    @jsondata:Name {value: "default_model_temperature"}
     decimal? defaultModelTemperature?;
     string? description?;
+    @jsondata:Name {value: "owned_by"}
     string ownedBy?;
     string id;
     string? deprecation?;
@@ -484,10 +536,14 @@
 
 
 type ModelCapabilities record {
+    @jsondata:Name {value: "completion_chat"}
     boolean completionChat?;
+    @jsondata:Name {value: "function_calling"}
     boolean functionCalling?;
     boolean vision?;
+    @jsondata:Name {value: "fine_tuning"}
     boolean fineTuning?;
+    @jsondata:Name {value: "completion_fim"}
     boolean completionFim?;
 };
 
@@ -498,20 +554,23 @@
     string[] aliases?;
     int created?;
     string? description?;
+    @jsondata:Name {value: "owned_by"}
     string ownedBy?;
     string? deprecation?;
     "fine-tuned" 'type?;
     boolean archived?;
+    @jsondata:Name {value: "max_context_length"}
     int maxContextLength?;
     string root;
     string? name?;
+    @jsondata:Name {value: "default_model_temperature"}
     decimal? defaultModelTemperature?;
     string id;
     string job;
     string 'object?;
 };
 
-type ModelListData ballerinax/mistral:1.0.2:BaseModelCard|ballerinax/mistral:1.0.2:FTModelCard;
+type ModelListData BaseModelCard|FTModelCard;
 
 
 type ClassificationRequest record {
@@ -545,7 +604,7 @@
     string model?;
     UsageInfo usage?;
     string id?;
-    string object?;
+    string 'object?;
     int created?;
     ChatCompletionChoice[] choices?;
 };
@@ -562,45 +621,61 @@
 
 
 type DetailedJobOut record {
+    @jsondata:Name {value: "job_type"}
     string jobType;
     JobMetadataOut metadata?;
+    @jsondata:Name {value: "fine_tuned_model"}
     string? fineTunedModel?;
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     CheckpointOut[] checkpoints?;
     string? suffix?;
+    @jsondata:Name {value: "auto_start"}
     boolean autoStart;
+    @jsondata:Name {value: "training_files"}
     string[] trainingFiles;
     DetailedJobOutRepositories[] repositories?;
     TrainingParameters hyperparameters;
     # The name of the model to fine-tune
     FineTuneableModel model;
     string id;
+    @jsondata:Name {value: "trained_tokens"}
     int? trainedTokens?;
+    @jsondata:Name {value: "modified_at"}
     int modifiedAt;
     DetailedJobOutIntegrations[]|() integrations?;
     # Event items are created every time the status of a fine-tuning job changes. The timestamped list of all events is accessible here
     EventOut[] events?;
     "QUEUED"|"STARTED"|"VALIDATING"|"VALIDATED"|"RUNNING"|"FAILED_VALIDATION"|"FAILED"|"SUCCESS"|"CANCELLED"|"CANCELLATION_REQUESTED" status;
+    @jsondata:Name {value: "validation_files"}
     string[]? validationFiles?;
     "job" 'object?;
 };
 
 
 type JobMetadataOut record {
+    @jsondata:Name {value: "data_tokens"}
     int? dataTokens?;
+    @jsondata:Name {value: "train_tokens_per_step"}
     int? trainTokensPerStep?;
     decimal? cost?;
+    @jsondata:Name {value: "cost_currency"}
     string? costCurrency?;
+    @jsondata:Name {value: "estimated_start_time"}
     int? estimatedStartTime?;
+    @jsondata:Name {value: "expected_duration_seconds"}
     int? expectedDurationSeconds?;
+    @jsondata:Name {value: "train_tokens"}
     int? trainTokens?;
 };
 
 
 type CheckpointOut record {
     # The step number that the checkpoint was created at
+    @jsondata:Name {value: "step_number"}
     int stepNumber;
     # The UNIX timestamp (in seconds) for when the checkpoint was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # Metrics at the step number during the fine-tuning job. Use these metrics to assess if the training is going smoothly (loss should decrease, token accuracy should increase)
     MetricOut metrics;
@@ -609,8 +684,11 @@
 # Metrics at the step number during the fine-tuning job. Use these metrics to assess if the training is going smoothly (loss should decrease, token accuracy should increase)
 
 type MetricOut record {
+    @jsondata:Name {value: "valid_loss"}
     decimal? validLoss?;
+    @jsondata:Name {value: "valid_mean_token_accuracy"}
     decimal? validMeanTokenAccuracy?;
+    @jsondata:Name {value: "train_loss"}
     decimal? trainLoss?;
 };
 
@@ -619,8 +697,10 @@
     string owner;
     string? ref?;
     string name;
+    @constraint:Number {minValueExclusive: 0}
     decimal weight?;
     "github" 'type?;
+    @jsondata:Name {value: "commit_id"}
     string commitId;
 };
 
@@ -629,19 +709,27 @@
     string owner;
     string? ref?;
     string name;
+    @constraint:Number {minValueExclusive: 0}
     decimal weight?;
     "github" 'type?;
+    @jsondata:Name {value: "commit_id"}
     string commitId;
 };
 
 
 type TrainingParameters record {
+    @jsondata:Name {value: "fim_ratio"}
     decimal? fimRatio?;
+    @jsondata:Name {value: "weight_decay"}
     decimal? weightDecay?;
+    @jsondata:Name {value: "training_steps"}
     int? trainingSteps?;
+    @jsondata:Name {value: "learning_rate"}
     decimal learningRate?;
     decimal? epochs?;
+    @jsondata:Name {value: "seq_len"}
     int? seqLen?;
+    @jsondata:Name {value: "warmup_fraction"}
     decimal? warmupFraction?;
 };
 
@@ -655,6 +743,7 @@
     # The name of the project that the new run will be created under
     string project;
     "wandb" 'type?;
+    @jsondata:Name {value: "run_name"}
     string? runName?;
 };
 
@@ -674,6 +763,7 @@
 
 type ClassificationObject record {
     # Classifier result
+    @jsondata:Name {value: "category_scores"}
     record {||} categoryScores?;
     # Classifier result thresholded
     record {|boolean...;|} categories?;
@@ -687,11 +777,14 @@
     # The size of the file, in bytes
     int bytes;
     # The UNIX timestamp (in seconds) of the event
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The unique identifier of the file
     string id;
     Source 'source;
+    @jsondata:Name {value: "sample_type"}
     SampleType sampleType;
+    @jsondata:Name {value: "num_lines"}
     int? numLines?;
     # The object type, which is always "file"
     string 'object;
@@ -699,9 +792,11 @@
 
 
 type BatchJobIn record {
+    @jsondata:Name {value: "input_files"}
     string[] inputFiles;
     ApiEndpoint endpoint;
     record {|string...;|}? metadata?;
+    @jsondata:Name {value: "timeout_hours"}
     int timeoutHours?;
     string model;
 };
@@ -722,16 +817,21 @@
 
 type JobOut record {
     # The type of job (`FT` for fine-tuning)
+    @jsondata:Name {value: "job_type"}
     string jobType;
     JobMetadataOut metadata?;
     # The name of the fine-tuned model that is being created. The value will be `null` if the fine-tuning job is still running
+    @jsondata:Name {value: "fine_tuned_model"}
     string? fineTunedModel?;
     # The UNIX timestamp (in seconds) for when the fine-tuning job was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # Optional text/code that adds more context for the model. When given a `prompt` and a `suffix` the model will fill what is between them. When `suffix` is not provided, the model will simply execute completion starting with `prompt`
     string? suffix?;
+    @jsondata:Name {value: "auto_start"}
     boolean autoStart;
     # A list containing the IDs of uploaded files that contain training data
+    @jsondata:Name {value: "training_files"}
     string[] trainingFiles;
     DetailedJobOutRepositories[] repositories?;
     TrainingParameters hyperparameters;
@@ -740,14 +840,17 @@
     # The ID of the job
     string id;
     # Total number of tokens trained
+    @jsondata:Name {value: "trained_tokens"}
     int? trainedTokens?;
     # The UNIX timestamp (in seconds) for when the fine-tuning job was last modified
+    @jsondata:Name {value: "modified_at"}
     int modifiedAt;
     # A list of integrations enabled for your fine-tuning job
     DetailedJobOutIntegrations[]|() integrations?;
     # The current status of the fine-tuning job
     "QUEUED"|"STARTED"|"VALIDATING"|"VALIDATED"|"RUNNING"|"FAILED_VALIDATION"|"FAILED"|"SUCCESS"|"CANCELLED"|"CANCELLATION_REQUESTED" status;
     # A list containing the IDs of uploaded files that contain validation data
+    @jsondata:Name {value: "validation_files"}
     string[]? validationFiles?;
     # The object type of the fine-tuning job
     "job" 'object?;
@@ -760,7 +863,9 @@
     FilePurpose purpose?;
     int page?;
     Source[]|() 'source?;
+    @http:Query {name: "sample_type"}
     SampleType[]|() sampleType?;
+    @http:Query {name: "page_size"}
     int pageSize?;
 };
 
@@ -769,6 +874,7 @@
     string owner;
     string? ref?;
     string name;
+    @constraint:Number {minValueExclusive: 0}
     decimal weight?;
     "github" 'type?;
     string token;
@@ -779,12 +885,15 @@
     # Specific pages user wants to process in various formats: single number, range, or list of both. Starts from 0
     int[]? pages?;
     # Minimum height and width of image to extract
+    @jsondata:Name {value: "image_min_size"}
     int? imageMinSize?;
     # Document to run OCR on
     DocumentURLChunk|ImageURLChunk document;
     # Include image URLs in response
+    @jsondata:Name {value: "include_image_base64"}
     boolean? includeImageBase64?;
     # Max images to extract
+    @jsondata:Name {value: "image_limit"}
     int? imageLimit?;
     string? model;
     string id?;
@@ -794,10 +903,13 @@
 
 type JobsApiRoutesBatchGetBatchJobsQueries record {
     record {|anydata...;|}? metadata?;
+    @http:Query {name: "created_after"}
     string? createdAfter?;
     string? model?;
     int page?;
+    @http:Query {name: "created_by_me"}
     boolean createdByMe?;
+    @http:Query {name: "page_size"}
     int pageSize?;
     BatchJobStatus status?;
 };
@@ -805,23 +917,30 @@
 
 type LegacyJobMetadataOut record {
     # The total number of tokens in the training dataset
+    @jsondata:Name {value: "data_tokens"}
     int? dataTokens?;
     # The number of tokens consumed by one training step
+    @jsondata:Name {value: "train_tokens_per_step"}
     int? trainTokensPerStep?;
     # The cost of the fine-tuning job
     decimal? cost?;
     # The currency used for the fine-tuning job cost
+    @jsondata:Name {value: "cost_currency"}
     string? costCurrency?;
+    @jsondata:Name {value: "estimated_start_time"}
     int? estimatedStartTime?;
     # The approximated time (in seconds) for the fine-tuning process to complete
+    @jsondata:Name {value: "expected_duration_seconds"}
     int? expectedDurationSeconds?;
     boolean deprecated?;
     string details;
     # The total number of tokens used during the fine-tuning process
+    @jsondata:Name {value: "train_tokens"}
     int? trainTokens?;
     # The number of complete passes through the entire training dataset
     decimal? epochs?;
     # The number of training steps to perform. A training step refers to a single update of the model weights during the fine-tuning process. This update is typically calculated using a batch of samples from the training dataset
+    @jsondata:Name {value: "training_steps"}
     int? trainingSteps?;
     "job.metadata" 'object?;
 };
@@ -851,21 +970,25 @@
     # The size of the file, in bytes
     int bytes;
     # The UNIX timestamp (in seconds) of the event
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The unique identifier of the file
     string id;
     Source 'source;
+    @jsondata:Name {value: "sample_type"}
     SampleType sampleType;
+    @jsondata:Name {value: "num_lines"}
     int? numLines?;
     # The object type, which is always "file"
     string 'object;
 };
 
-type ResponseRetrieveModelV1ModelsModelIdGet ballerinax/mistral:1.0.2:BaseModelCard|ballerinax/mistral:1.0.2:FTModelCard;
+type ResponseRetrieveModelV1ModelsModelIdGet BaseModelCard|FTModelCard;
 
 
 type ToolMessage record {
     "tool" role?;
+    @jsondata:Name {value: "tool_call_id"}
     string? toolCallId?;
     string? name?;
     string|ContentChunk[]|() content;
@@ -894,17 +1017,27 @@
 
 
 type BatchJobOut record {
+    @jsondata:Name {value: "succeeded_requests"}
     int succeededRequests;
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "failed_requests"}
     int failedRequests;
+    @jsondata:Name {value: "created_at"}
     int createdAt;
+    @jsondata:Name {value: "output_file"}
     string? outputFile?;
+    @jsondata:Name {value: "error_file"}
     string? errorFile?;
+    @jsondata:Name {value: "input_files"}
     string[] inputFiles;
+    @jsondata:Name {value: "completed_at"}
     int? completedAt?;
     string endpoint;
+    @jsondata:Name {value: "completed_requests"}
     int completedRequests;
+    @jsondata:Name {value: "total_requests"}
     int totalRequests;
+    @jsondata:Name {value: "started_at"}
     int? startedAt?;
     string model;
     string id;
@@ -921,6 +1054,7 @@
 
 
 type ChatModerationRequest record {
+    @jsondata:Name {value: "truncate_for_context_length"}
     boolean truncateForContextLength?;
     # Chat to classify
     SystemMessage|UserMessage|AssistantMessage|ToolMessage[]|SystemMessage|UserMessage|AssistantMessage|ToolMessage[][] input;
@@ -956,24 +1090,28 @@
 
 type WandbIntegration record {
     # The WandB API key to use for authentication
+    @jsondata:Name {value: "api_key"}
     string apiKey;
     # A display name to set for the run. If not set, will use the job ID as the name
     string? name?;
     # The name of the project that the new run will be created under
     string project;
     "wandb" 'type?;
+    @jsondata:Name {value: "run_name"}
     string? runName?;
 };
 
 
 type JobInIntegrations record {
     # The WandB API key to use for authentication
+    @jsondata:Name {value: "api_key"}
     string apiKey;
     # A display name to set for the run. If not set, will use the job ID as the name
     string? name?;
     # The name of the project that the new run will be created under
     string project;
     "wandb" 'type?;
+    @jsondata:Name {value: "run_name"}
     string? runName?;
 };
 
@@ -1000,12 +1138,15 @@
 
 type FIMCompletionRequest record {
     # Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both
+    @jsondata:Name {value: "top_p"}
     decimal topP?;
     # The seed to use for random sampling. If set, different calls will generate deterministic results
+    @jsondata:Name {value: "random_seed"}
     int? randomSeed?;
     # Stop generation if this token is detected. Or if one of these tokens is detected when providing an array
     string|string[] stop?;
     # The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length
+    @jsondata:Name {value: "max_tokens"}
     int? maxTokens?;
     # Whether to stream back partial progress. If set, tokens will be sent as data-only server-side events as they become available, with the stream terminated by a data: [DONE] message. Otherwise, the server will hold the request open until the timeout or until completion, with the response containing the full result as JSON
     boolean 'stream?;
@@ -1020,26 +1161,33 @@
     # The text/code to complete
     string prompt;
     # The minimum number of tokens to generate in the completion
+    @jsondata:Name {value: "min_tokens"}
     int? minTokens?;
 };
 
-type AgentsCompletionRequestMessages ballerinax/mistral:1.0.2:SystemMessage|ballerinax/mistral:1.0.2:UserMessage|ballerinax/mistral:1.0.2:AssistantMessage|ballerinax/mistral:1.0.2:ToolMessage;
+type AgentsCompletionRequestMessages SystemMessage|UserMessage|AssistantMessage|ToolMessage;
 
 
 type AgentsCompletionRequest record {
     # The seed to use for random sampling. If set, different calls will generate deterministic results
+    @jsondata:Name {value: "random_seed"}
     int? randomSeed?;
     # The ID of the agent to use for this completion
+    @jsondata:Name {value: "agent_id"}
     string agentId;
     # The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length
+    @jsondata:Name {value: "max_tokens"}
     int? maxTokens?;
     # presence_penalty determines how much the model penalizes the repetition of words or phrases. A higher presence penalty encourages the model to use a wider variety of words and phrases, making the output more diverse and creative
+    @jsondata:Name {value: "presence_penalty"}
     decimal presencePenalty?;
     Tool[]|() tools?;
     # Number of completions to return for each request, input tokens are only billed once
     int? n?;
+    @jsondata:Name {value: "response_format"}
     ResponseFormat responseFormat?;
     # frequency_penalty penalizes the repetition of words based on their frequency in the generated text. A higher frequency penalty discourages the model from repeating words that have already appeared frequently in the output, promoting diversity and reducing repetition
+    @jsondata:Name {value: "frequency_penalty"}
     decimal frequencyPenalty?;
     # Stop generation if this token is detected. Or if one of these tokens is detected when providing an array
     string|string[] stop?;
@@ -1048,6 +1196,7 @@
     Prediction prediction?;
     # The prompt(s) to generate completions for, encoded as a list of dict with role and content
     AgentsCompletionRequestMessages[] messages;
+    @jsondata:Name {value: "tool_choice"}
     ToolChoice|ToolChoiceEnum toolChoice?;
 };
 
@@ -1056,20 +1205,27 @@
 
 type ChatCompletionRequest record {
     # The seed to use for random sampling. If set, different calls will generate deterministic results
+    @jsondata:Name {value: "random_seed"}
     int? randomSeed?;
     # Whether to inject a safety prompt before all conversations
+    @jsondata:Name {value: "safe_prompt"}
     boolean safePrompt?;
     # The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length
+    @jsondata:Name {value: "max_tokens"}
     int? maxTokens?;
     # presence_penalty determines how much the model penalizes the repetition of words or phrases. A higher presence penalty encourages the model to use a wider variety of words and phrases, making the output more diverse and creative
+    @jsondata:Name {value: "presence_penalty"}
     decimal presencePenalty?;
     Tool[]|() tools?;
     # Number of completions to return for each request, input tokens are only billed once
     int? n?;
     # Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both
+    @jsondata:Name {value: "top_p"}
     decimal topP?;
+    @jsondata:Name {value: "response_format"}
     ResponseFormat responseFormat?;
     # frequency_penalty penalizes the repetition of words based on their frequency in the generated text. A higher frequency penalty discourages the model from repeating words that have already appeared frequently in the output, promoting diversity and reducing repetition
+    @jsondata:Name {value: "frequency_penalty"}
     decimal frequencyPenalty?;
     # Stop generation if this token is detected. Or if one of these tokens is detected when providing an array
     string|string[] stop?;
@@ -1080,6 +1236,7 @@
     Prediction prediction?;
     # The prompt(s) to generate completions for, encoded as a list of dict with role and content
     AgentsCompletionRequestMessages[] messages;
+    @jsondata:Name {value: "tool_choice"}
     ToolChoice|ToolChoiceEnum toolChoice?;
     # ID of the model to use. You can use the [List Available Models](/api/#tag/models/operation/list_models_v1_models_get) API to see all of your available models, or see our [Model overview](/models) for model descriptions
     string model;
@@ -1093,7 +1250,9 @@
 
 
 type JobIn record {
+    @jsondata:Name {value: "training_files"}
     TrainingFile[] trainingFiles?;
+    @constraint:Array {maxLength: 50}
     JobInRepositories[] repositories?;
     # The fine-tuning hyperparameter settings used in a fine-tune job
     TrainingParametersIn hyperparameters;
@@ -1104,8 +1263,10 @@
     # A list of integrations to enable for your fine-tuning job
     JobInIntegrations[]|() integrations?;
     # A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files
+    @jsondata:Name {value: "validation_files"}
     string[]? validationFiles?;
     # This field will be required in a future release
+    @jsondata:Name {value: "auto_start"}
     boolean autoStart?;
 };
 
@@ -1117,7 +1278,7 @@
     string model?;
 };
 
-type Response ballerinax/mistral:1.0.2:JobOut|ballerinax/mistral:1.0.2:LegacyJobMetadataOut;
+type Response JobOut|LegacyJobMetadataOut;
 
 
 type EmbeddingResponse record {
@@ -1148,7 +1309,7 @@
 
     # List Files
     # 
-    resource function get files(map<string|string[]> headers = {}, string|() search = (), FilePurpose purpose = "fine-tune", int page = 0, Source[]|() source = (), SampleType[]|() sampleType = (), int pageSize = 0, anydata Additional Values, FilesApiRoutesListFilesQueries queries) returns ListFilesOut|error;
+    resource function get files(map<string|string[]> headers = {}, string|() search = (), FilePurpose purpose = "fine-tune", int page = 0, Source[]|() source = (), SampleType[]|() sampleType = (), int pageSize = 0, FilesApiRoutesListFilesQueries queries) returns ListFilesOut|error;
 
     # Upload File
     # 
@@ -1168,15 +1329,15 @@
 
     # Get Signed Url
     # 
-    resource function get files/[string fileId]/url(map<string|string[]> headers = {}, int expiry = 0, anydata Additional Values, FilesApiRoutesGetSignedUrlQueries queries) returns FileSignedURL|error;
+    resource function get files/[string fileId]/url(map<string|string[]> headers = {}, int expiry = 0, FilesApiRoutesGetSignedUrlQueries queries) returns FileSignedURL|error;
 
     # Get Fine Tuning Jobs
     # 
-    resource function get fine_tuning/jobs(map<string|string[]> headers = {}, string|() wandbProject = (), string|() wandbName = (), string|() createdAfter = (), string|() model = (), int page = 0, string|() suffix = (), boolean createdByMe = false, int pageSize = 0, "CANCELLATION_REQUESTED"|()|"QUEUED"|"STARTED"|"VALIDATING"|"VALIDATED"|"RUNNING"|"FAILED_VALIDATION"|"FAILED"|"SUCCESS"|"CANCELLED" status = (), anydata Additional Values, JobsApiRoutesFineTuningGetFineTuningJobsQueries queries) returns JobsOut|error;
+    resource function get fine_tuning/jobs(map<string|string[]> headers = {}, string|() wandbProject = (), string|() wandbName = (), string|() createdAfter = (), string|() model = (), int page = 0, string|() suffix = (), boolean createdByMe = false, int pageSize = 0, "CANCELLATION_REQUESTED"|()|"QUEUED"|"STARTED"|"VALIDATING"|"VALIDATED"|"RUNNING"|"FAILED_VALIDATION"|"FAILED"|"SUCCESS"|"CANCELLED" status = (), JobsApiRoutesFineTuningGetFineTuningJobsQueries queries) returns JobsOut|error;
 
     # Create Fine Tuning Job
     # 
-    resource function post fine_tuning/jobs(JobIn payload, map<string|string[]> headers = {}, boolean|() dryRun = (), anydata Additional Values, JobsApiRoutesFineTuningCreateFineTuningJobQueries queries) returns JobOut|LegacyJobMetadataOut|error;
+    resource function post fine_tuning/jobs(JobIn payload, map<string|string[]> headers = {}, boolean|() dryRun = (), JobsApiRoutesFineTuningCreateFineTuningJobQueries queries) returns JobOut|LegacyJobMetadataOut|error;
 
     # Get Fine Tuning Job
     # 
@@ -1204,7 +1365,7 @@
 
     # Get Batch Jobs
     # 
-    resource function get batch/jobs(map<string|string[]> headers = {}, record {|anydata...;|}|() metadata = (), string|() createdAfter = (), string|() model = (), int page = 0, boolean createdByMe = false, int pageSize = 0, BatchJobStatus status = "QUEUED", anydata Additional Values, JobsApiRoutesBatchGetBatchJobsQueries queries) returns BatchJobsOut|error;
+    resource function get batch/jobs(map<string|string[]> headers = {}, record {|anydata...;|}|() metadata = (), string|() createdAfter = (), string|() model = (), int page = 0, boolean createdByMe = false, int pageSize = 0, BatchJobStatus status = "QUEUED", JobsApiRoutesBatchGetBatchJobsQueries queries) returns BatchJobsOut|error;
 
     # Create Batch Job
     # 
`````

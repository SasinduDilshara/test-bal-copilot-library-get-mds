# openai.finetunes — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `openai.finetunes` |
| **Old file** | `openai.finetunes/old/ballerinax_openai.finetunes.bal.txt` |
| **New file** | `openai.finetunes/new/ballerinax_openai.finetunes.bal.txt` |
| **Old lines** | 3035 |
| **New lines** | 3330 |
| **Lines added** | 333 |
| **Lines removed** | 38 |
| **Hunks** | 122 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 6 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 51 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (6)

- `type ChatCompletionMessageToolCalls`
- `type CreateAssistantRequestToolResourcesFileSearch`
- `type CreateThreadRequestToolResourcesFileSearch`
- `type InputItemsArray`
- `type ParallelToolCalls`
- `type PromptItemsArray`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 129–144 | 129–148 | Types | +4 | −0 |
| 2 | 147–157 | 151–167 | Types | +6 | −0 |
| 3 | 161–169 | 171–182 | Types | +3 | −0 |
| 4 | 172–218 | 185–250 | Types | +19 | −0 |
| 5 | 223–228 | 255–261 | Types | +1 | −0 |
| 6 | 232–237 | 265–271 | Types | +1 | −0 |
| 7 | 259–268 | 293–305 | Types | +3 | −0 |
| 8 | 274–279 | 311–317 | Types | +1 | −0 |
| 9 | 285–290 | 323–329 | Types | +1 | −0 |
| 10 | 314–320 | 353–359 | Types | +1 | −1 |
| 11 | 331–337 | 370–376 | Types | +1 | −1 |
| 12 | 352–358 | 391–397 | Types | +1 | −1 |
| 13 | 374–385 | 413–426 | Types | +3 | −1 |
| 14 | 407–438 | 448–489 | Types | +10 | −0 |
| 15 | 452–457 | 503–509 | Types | +1 | −0 |
| 16 | 463–473 | 515–526 | Types | +2 | −1 |
| 17 | 476–481 | 529–535 | Types | +1 | −0 |
| 18 | 484–489 | 538–544 | Types | +1 | −0 |
| 19 | 506–520 | 561–578 | Types | +5 | −2 |
| 20 | 543–549 | 601–607 | Types | +1 | −1 |
| 21 | 554–559 | 612–618 | Types | +1 | −0 |
| 22 | 615–633 | 674–695 | Types | +4 | −1 |
| 23 | 677–682 | 739–745 | Types | +1 | −0 |
| 24 | 697–734 | 760–806 | Types | +9 | −0 |
| 25 | 742–756 | 814–830 | Types | +3 | −1 |
| 26 | 762–767 | 836–842 | Types | +1 | −0 |
| 27 | 770–788 | 845–867 | Types | +4 | −0 |
| 28 | 804–811 | 883–893 | Types | +3 | −0 |
| 29 | 816–829 | 898–915 | Types | +4 | −0 |
| 30 | 834–843 | 920–930 | Types | +2 | −1 |
| 31 | 850–855 | 937–943 | Types | +1 | −0 |
| 32 | 884–899 | 972–990 | Types | +3 | −0 |
| 33 | 904–913 | 995–1006 | Types | +2 | −0 |
| 34 | 919–928 | 1012–1023 | Types | +2 | −0 |
| 35 | 933–946 | 1028–1045 | Types | +4 | −0 |
| 36 | 949–955 | 1048–1056 | Types | +2 | −0 |
| 37 | 959–965 | 1060–1068 | Types | +2 | −0 |
| 38 | 1025–1030 | 1128–1134 | Types | +1 | −0 |
| 39 | 1038–1052 | 1142–1158 | Types | +3 | −1 |
| 40 | 1068–1073 | 1174–1180 | Types | +1 | −0 |
| 41 | 1084–1095 | 1191–1203 | Types | +2 | −1 |
| 42 | 1097–1120 | 1205–1235 | Types | +7 | −0 |
| 43 | 1123–1141 | 1238–1260 | Types | +4 | −0 |
| 44 | 1143–1152 | 1262–1274 | Types | +3 | −0 |
| 45 | 1154–1159 | 1276–1282 | Types | +1 | −0 |
| 46 | 1162–1167 | 1285–1291 | Types | +1 | −0 |
| 47 | 1197–1210 | 1321–1336 | Types | +3 | −1 |
| 48 | 1212–1235 | 1338–1367 | Types | +7 | −1 |
| 49 | 1242–1247 | 1374–1380 | Types | +1 | −0 |
| 50 | 1259–1264 | 1392–1398 | Types | +1 | −0 |
| 51 | 1269–1274 | 1403–1409 | Types | +1 | −0 |
| 52 | 1277–1286 | 1412–1423 | Types | +2 | −0 |
| 53 | 1299–1314 | 1436–1454 | Types | +3 | −0 |
| 54 | 1320–1325 | 1460–1466 | Types | +1 | −0 |
| 55 | 1329–1335 | 1470–1476 | Types | +1 | −1 |
| 56 | 1347–1352 | 1488–1494 | Types | +1 | −0 |
| 57 | 1357–1362 | 1499–1505 | Types | +1 | −0 |
| 58 | 1365–1373 | 1508–1519 | Types | +3 | −0 |
| 59 | 1381–1386 | 1527–1533 | Types | +1 | −0 |
| 60 | 1420–1442 | 1567–1596 | Types | +7 | −0 |
| 61 | 1447–1460 | 1601–1615 | Types | +3 | −2 |
| 62 | 1468–1481 | 1623–1640 | Types | +4 | −0 |
| 63 | 1485–1503 | 1644–1667 | Types | +5 | −0 |
| 64 | 1511–1540 | 1675–1709 | Types | +6 | −1 |
| 65 | 1562–1569 | 1731–1740 | Types | +2 | −0 |
| 66 | 1576–1587 | 1747–1759 | Types | +3 | −2 |
| 67 | 1607–1616 | 1779–1791 | Types | +3 | −0 |
| 68 | 1624–1629 | 1799–1805 | Types | +1 | −0 |
| 69 | 1663–1672 | 1839–1850 | Types | +2 | −0 |
| 70 | 1683–1696 | 1861–1878 | Types | +4 | −0 |
| 71 | 1698–1733 | 1880–1929 | Types | +14 | −0 |
| 72 | 1752–1776 | 1948–1977 | Types | +6 | −1 |
| 73 | 1803–1808 | 2004–2010 | Types | +1 | −0 |
| 74 | 1835–1841 | 2037–2043 | Types | +1 | −1 |
| 75 | 1859–1875 | 2061–2082 | Types | +5 | −0 |
| 76 | 1901–1906 | 2108–2114 | Types | +1 | −0 |
| 77 | 1920–1962 | 2128–2182 | Types | +12 | −0 |
| 78 | 1968–1973 | 2188–2194 | Types | +1 | −0 |
| 79 | 2004–2034 | 2225–2265 | Types | +10 | −0 |
| 80 | 2039–2044 | 2270–2276 | Types | +1 | −0 |
| 81 | 2064–2069 | 2296–2302 | Types | +1 | −0 |
| 82 | 2078–2083 | 2311–2317 | Types | +1 | −0 |
| 83 | 2097–2108 | 2331–2345 | Types | +3 | −0 |
| 84 | 2137–2150 | 2374–2389 | Types | +3 | −1 |
| 85 | 2166–2171 | 2405–2411 | Types | +1 | −0 |
| 86 | 2179–2184 | 2419–2425 | Types | +1 | −0 |
| 87 | 2201–2215 | 2442–2460 | Types | +4 | −0 |
| 88 | 2219–2224 | 2464–2470 | Types | +1 | −0 |
| 89 | 2227–2232 | 2473–2479 | Types | +1 | −0 |
| 90 | 2251–2274 | 2498–2528 | Types | +7 | −0 |
| 91 | 2301–2306 | 2555–2561 | Types | +1 | −0 |
| 92 | 2317–2322 | 2572–2578 | Types | +1 | −0 |
| 93 | 2360–2370 | 2616–2629 | Types | +3 | −0 |
| 94 | 2376–2381 | 2635–2641 | Types | +1 | −0 |
| 95 | 2390–2396 | 2650–2658 | Types | +2 | −0 |
| 96 | 2399–2408 | 2661–2672 | Types | +2 | −0 |
| 97 | 2413–2418 | 2677–2683 | Types | +1 | −0 |
| 98 | 2421–2444 | 2686–2717 | Types | +8 | −0 |
| 99 | 2447–2452 | 2720–2726 | Types | +1 | −0 |
| 100 | 2481–2492 | 2755–2769 | Types | +3 | −0 |
| 101 | 2497–2502 | 2774–2780 | Types | +1 | −0 |
| 102 | 2522–2527 | 2800–2806 | Types | +1 | −0 |
| 103 | 2534–2553 | 2813–2836 | Types | +4 | −0 |
| 104 | 2585–2593 | 2868–2876 | Types | +2 | −2 |
| 105 | 2601–2613 | 2884–2899 | Types | +3 | −0 |
| 106 | 2623–2634 | 2909–2923 | Types | +3 | −0 |
| 107 | 2639–2644 | 2928–2934 | Types | +1 | −0 |
| 108 | 2660–2667 | 2950–2959 | Types | +2 | −0 |
| 109 | 2679–2684 | 2971–2977 | Types | +1 | −0 |
| 110 | 2687–2692 | 2980–2986 | Types | +1 | −0 |
| 111 | 2697–2702 | 2991–2997 | Types | +1 | −0 |
| 112 | 2768–2774 | 3063–3069 | Client | +1 | −1 |
| 113 | 2829–2835 | 3124–3130 | Client | +1 | −1 |
| 114 | 2847–2853 | 3142–3148 | Client | +1 | −1 |
| 115 | 2855–2861 | 3150–3156 | Client | +1 | −1 |
| 116 | 2875–2881 | 3170–3176 | Client | +1 | −1 |
| 117 | 2911–2917 | 3206–3212 | Client | +1 | −1 |
| 118 | 2935–2941 | 3230–3236 | Client | +1 | −1 |
| 119 | 2959–2965 | 3254–3260 | Client | +1 | −1 |
| 120 | 2967–2973 | 3262–3268 | Client | +1 | −1 |
| 121 | 2987–2993 | 3282–3288 | Client | +1 | −1 |
| 122 | 3015–3025 | 3310–3320 | Client | +2 | −2 |

---

## Unified diff

`````diff
--- openai.finetunes/old/ballerinax_openai.finetunes.bal.txt	2026-08-12 12:57:30
+++ openai.finetunes/new/ballerinax_openai.finetunes.bal.txt	2026-08-12 13:19:19
@@ -129,16 +129,20 @@
 
 type FineTuningJobCheckpoint record {
     # The step number that the checkpoint was created at
+    @jsondata:Name {value: "step_number"}
     int stepNumber;
     # The Unix timestamp (in seconds) for when the checkpoint was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The name of the fine-tuning job that this checkpoint was created from
+    @jsondata:Name {value: "fine_tuning_job_id"}
     string fineTuningJobId;
     # The checkpoint identifier, which can be referenced in the API endpoints
     string id;
     # Metrics at the step number during the fine-tuning job
     FineTuningJobCheckpointMetrics metrics;
     # The name of the fine-tuned checkpoint model that is created
+    @jsondata:Name {value: "fine_tuned_model_checkpoint"}
     string fineTunedModelCheckpoint;
     # The object type, which is always "fine_tuning.job.checkpoint"
     "fine_tuning.job.checkpoint" 'object;
@@ -147,11 +151,17 @@
 # Metrics at the step number during the fine-tuning job
 
 type FineTuningJobCheckpointMetrics record {
+    @jsondata:Name {value: "full_valid_mean_token_accuracy"}
     decimal fullValidMeanTokenAccuracy?;
+    @jsondata:Name {value: "valid_loss"}
     decimal validLoss?;
+    @jsondata:Name {value: "full_valid_loss"}
     decimal fullValidLoss?;
+    @jsondata:Name {value: "train_mean_token_accuracy"}
     decimal trainMeanTokenAccuracy?;
+    @jsondata:Name {value: "valid_mean_token_accuracy"}
     decimal validMeanTokenAccuracy?;
+    @jsondata:Name {value: "train_loss"}
     decimal trainLoss?;
     decimal step?;
 };
@@ -161,9 +171,12 @@
 
 
 type ListRunsResponse record {
+    @jsondata:Name {value: "first_id"}
     string firstId;
     RunObject[] data;
+    @jsondata:Name {value: "last_id"}
     string lastId;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     string 'object;
 };
@@ -172,47 +185,66 @@
 
 type RunObject record {
     # The Unix timestamp (in seconds) for when the run was cancelled
+    @jsondata:Name {value: "cancelled_at"}
     int? cancelledAt;
     # The instructions that the [assistant](/docs/api-reference/assistants) used for this run
     string instructions;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata;
     # The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run
+    @jsondata:Name {value: "assistant_id"}
     string assistantId;
+    @jsondata:Name {value: "required_action"}
     RunObjectRequiredAction|() requiredAction;
     # Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.)
     RunCompletionUsage|() usage;
     # The Unix timestamp (in seconds) for when the run was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The list of tools that the [assistant](/docs/api-reference/assistants) used for this run
+    @constraint:Array {maxLength: 20}
     RunObjectTools[] tools?;
     # The nucleus sampling value used for this run. If not set, defaults to 1
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # The maximum number of completion tokens specified to have been used over the course of the run
+    @jsondata:Name {value: "max_completion_tokens"}
     int? maxCompletionTokens;
     # The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run
+    @jsondata:Name {value: "thread_id"}
     string threadId;
     # The Unix timestamp (in seconds) for when the run will expire
+    @jsondata:Name {value: "expires_at"}
     int? expiresAt;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat;
     # The sampling temperature used for this run. If not set, defaults to 1
     decimal? temperature?;
+    @jsondata:Name {value: "tool_choice"}
     AssistantsApiToolChoiceOption toolChoice;
     # The model that the [assistant](/docs/api-reference/assistants) used for this run
     string model;
     # The identifier, which can be referenced in API endpoints
     string id;
+    @jsondata:Name {value: "last_error"}
     RunObjectLastError|() lastError;
+    @jsondata:Name {value: "incomplete_details"}
     RunObjectIncompleteDetails|() incompleteDetails;
+    @jsondata:Name {value: "truncation_strategy"}
     TruncationObject truncationStrategy;
     # The Unix timestamp (in seconds) for when the run was completed
+    @jsondata:Name {value: "completed_at"}
     int? completedAt;
+    @jsondata:Name {value: "parallel_tool_calls"}
     ParallelToolCalls parallelToolCalls;
     # The Unix timestamp (in seconds) for when the run was started
+    @jsondata:Name {value: "started_at"}
     int? startedAt;
     # The Unix timestamp (in seconds) for when the run failed
+    @jsondata:Name {value: "failed_at"}
     int? failedAt;
     # The maximum number of prompt tokens specified to have been used over the course of the run
+    @jsondata:Name {value: "max_prompt_tokens"}
     int? maxPromptTokens;
     # The object type, which is always `thread.run`
     "thread.run" 'object;
@@ -223,6 +255,7 @@
 # Details on the action required to continue the run. Will be `null` if no action is required
 
 type RunObjectRequiredAction record {
+    @jsondata:Name {value: "submit_tool_outputs"}
     RunObjectRequiredActionSubmitToolOutputs submitToolOutputs;
     # For now, this is always `submit_tool_outputs`
     "submit_tool_outputs" 'type;
@@ -232,6 +265,7 @@
 
 type RunObjectRequiredActionSubmitToolOutputs record {
     # A list of the relevant tool calls
+    @jsondata:Name {value: "tool_calls"}
     RunToolCallObject[] toolCalls;
 };
 
@@ -259,10 +293,13 @@
 
 type RunCompletionUsage record {
     # Number of completion tokens used over the course of the run
+    @jsondata:Name {value: "completion_tokens"}
     int completionTokens;
     # Number of prompt tokens used over the course of the run
+    @jsondata:Name {value: "prompt_tokens"}
     int promptTokens;
     # Total number of tokens used (prompt + completion)
+    @jsondata:Name {value: "total_tokens"}
     int totalTokens;
 };
 
@@ -274,6 +311,7 @@
 
 
 type AssistantToolsFileSearch record {
+    @jsondata:Name {value: "file_search"}
     AssistantToolsFileSearchFileSearch fileSearch?;
     # The type of tool being defined: `file_search`
     "file_search" 'type;
@@ -285,6 +323,7 @@
     # The maximum number of results the file search tool should output. The default is 20 for gpt-4* models and 5 for gpt-3.5-turbo. This number should be between 1 and 50 inclusive.
 
 Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search/number-of-chunks-returned) for more information
+    @jsondata:Name {value: "max_num_results"}
     int maxNumResults?;
 };
 
@@ -314,7 +353,7 @@
 type FunctionParameters record {
 };
 
-type RunObjectTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type RunObjectTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
 # `auto` is the default value
 type AssistantsApiResponseFormatOptionOneOf1 "none"|"auto";
@@ -331,7 +370,7 @@
 # Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.
 # 
 # **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length
-type AssistantsApiResponseFormatOption ballerinax/openai.finetunes:3.0.0:AssistantsApiResponseFormatOptionOneOf1|ballerinax/openai.finetunes:3.0.0:AssistantsApiResponseFormat;
+type AssistantsApiResponseFormatOption AssistantsApiResponseFormatOptionOneOf1|AssistantsApiResponseFormat;
 
 # Specifies a tool the model should use. Use to force the model to call a specific tool
 
@@ -352,7 +391,7 @@
 # `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
 # `required` means the model must call one or more tools before responding to the user.
 # Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool
-type AssistantsApiToolChoiceOption ballerinax/openai.finetunes:3.0.0:AssistantsApiToolChoiceOptionOneOf1|ballerinax/openai.finetunes:3.0.0:AssistantsNamedToolChoice;
+type AssistantsApiToolChoiceOption AssistantsApiToolChoiceOptionOneOf1|AssistantsNamedToolChoice;
 
 # The last error associated with this run. Will be `null` if there are no errors
 
@@ -374,12 +413,14 @@
 
 type TruncationObject record {
     # The number of most recent messages from the thread when constructing the context for the run
+    @jsondata:Name {value: "last_messages"}
     int? lastMessages?;
     # The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`
     "auto"|"last_messages" 'type;
 };
 
-// Unknown type: ParallelToolCalls
+# Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use
+type ParallelToolCalls boolean;
 
 
 type RunStepDetailsToolCallsFunctionObject record {
@@ -407,32 +448,42 @@
     # Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis
     string? instructions?;
     # Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions
+    @jsondata:Name {value: "additional_instructions"}
     string? additionalInstructions?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
     # The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run
+    @jsondata:Name {value: "assistant_id"}
     string assistantId;
     # Adds additional messages to the thread before creating the run
+    @jsondata:Name {value: "additional_messages"}
     CreateMessageRequest[]|() additionalMessages?;
     # Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis
     CreateRunRequestTools[]|() tools?;
+    @jsondata:Name {value: "truncation_strategy"}
     TruncationObject truncationStrategy?;
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or temperature but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info
+    @jsondata:Name {value: "max_completion_tokens"}
     int? maxCompletionTokens?;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat?;
+    @jsondata:Name {value: "parallel_tool_calls"}
     ParallelToolCalls parallelToolCalls?;
     # If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message
     boolean? 'stream?;
     # What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic
     decimal? temperature?;
+    @jsondata:Name {value: "tool_choice"}
     AssistantsApiToolChoiceOption toolChoice?;
     # The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used
     "gpt-3.5-turbo-16k-0613"?|string|"gpt-4o"|"gpt-4o-2024-05-13"|"gpt-4o-mini"|"gpt-4o-mini-2024-07-18"|"gpt-4-turbo"|"gpt-4-turbo-2024-04-09"|"gpt-4-0125-preview"|"gpt-4-turbo-preview"|"gpt-4-1106-preview"|"gpt-4-vision-preview"|"gpt-4"|"gpt-4-0314"|"gpt-4-0613"|"gpt-4-32k"|"gpt-4-32k-0314"|"gpt-4-32k-0613"|"gpt-3.5-turbo"|"gpt-3.5-turbo-16k"|"gpt-3.5-turbo-0613"|"gpt-3.5-turbo-1106"|"gpt-3.5-turbo-0125" model?;
     # The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info
+    @jsondata:Name {value: "max_prompt_tokens"}
     int? maxPromptTokens?;
 };
 
@@ -452,6 +503,7 @@
 
 type CreateMessageRequestAttachments record {
     # The ID of the file to attach to the message
+    @jsondata:Name {value: "file_id"}
     string fileId?;
     # The tools to add this file to
     CreateMessageRequestTools[] tools?;
@@ -463,11 +515,12 @@
     "file_search" 'type;
 };
 
-type CreateMessageRequestTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearchTypeOnly;
+type CreateMessageRequestTools AssistantToolsCode|AssistantToolsFileSearchTypeOnly;
 
 # References an image [File](/docs/api-reference/files) in the content of a message
 
 type MessageContentImageFileObject record {
+    @jsondata:Name {value: "image_file"}
     MessageContentImageFileObjectImageFile imageFile;
     # Always `image_file`
     "image_file" 'type;
@@ -476,6 +529,7 @@
 
 type MessageContentImageFileObjectImageFile record {
     # The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content
+    @jsondata:Name {value: "file_id"}
     string fileId;
     # Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`
     "auto"|"low"|"high" detail?;
@@ -484,6 +538,7 @@
 # References an image URL in the content of a message
 
 type MessageContentImageUrlObject record {
+    @jsondata:Name {value: "image_url"}
     MessageContentImageUrlObjectImageUrl imageUrl;
     # The type of the content part
     "image_url" 'type;
@@ -506,15 +561,18 @@
     "text" 'type;
 };
 
-type CreateRunRequestTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type CreateRunRequestTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
-// Unknown type: InputItemsArray
+type InputItemsArray int[];
 
 
 type ListFineTuningJobCheckpointsResponse record {
+    @jsondata:Name {value: "first_id"}
     string? firstId?;
     FineTuningJobCheckpoint[] data;
+    @jsondata:Name {value: "last_id"}
     string? lastId?;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     "list" 'object;
 };
@@ -543,7 +601,7 @@
 # Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.
 # 
 # `none` is the default when no tools are present. `auto` is the default if tools are present
-type ChatCompletionToolChoiceOption ballerinax/openai.finetunes:3.0.0:ChatCompletionToolChoiceOptionOneOf1|ballerinax/openai.finetunes:3.0.0:ChatCompletionNamedToolChoice;
+type ChatCompletionToolChoiceOption ChatCompletionToolChoiceOptionOneOf1|ChatCompletionNamedToolChoice;
 
 # The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`
 
@@ -554,6 +612,7 @@
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -615,19 +674,22 @@
     string arguments;
 };
 
-// Unknown type: ChatCompletionMessageToolCalls
+# The tool calls generated by the model, such as function calls
+type ChatCompletionMessageToolCalls ChatCompletionMessageToolCall[];
 
 
 type CreateEmbeddingRequest record {
     # Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens
     string|string[]|int[]|InputItemsArray[] input;
     # The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/)
+    @jsondata:Name {value: "encoding_format"}
     "float"|"base64" encodingFormat?;
     # ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them
     string|"text-embedding-ada-002"|"text-embedding-3-small"|"text-embedding-3-large" model;
     # A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)
     string user?;
     # The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models
+    @constraint:Int {minValue: 1}
     int dimensions?;
 };
 
@@ -677,6 +739,7 @@
     # The MIME type of the file.
 
 This must fall within the supported MIME types for your file purpose. See the supported MIME types for assistants and vision
+    @jsondata:Name {value: "mime_type"}
     string mimeType;
     # The number of bytes in the file you are uploading
     int bytes;
@@ -697,38 +760,47 @@
     # The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech/voice-options)
     "alloy"|"echo"|"fable"|"onyx"|"nova"|"shimmer" voice;
     # The text to generate audio for. The maximum length is 4096 characters
+    @constraint:String {maxLength: 4096}
     string input;
     # The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`
+    @jsondata:Name {value: "response_format"}
     "mp3"|"opus"|"aac"|"flac"|"wav"|"pcm" responseFormat?;
     # One of the available [TTS models](/docs/models/tts): `tts-1` or `tts-1-hd`
     string|"tts-1"|"tts-1-hd" model;
     # The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default
+    @constraint:Number {minValue: 0.25, maxValue: 4.0}
     decimal speed?;
 };
 
 # A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type AssistantObjectToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     AssistantObjectToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     AssistantObjectToolResourcesFileSearch fileSearch?;
 };
 
 
 type AssistantObjectToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool`
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
 
 type AssistantObjectToolResourcesFileSearch record {
     # The ID of the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant
+    @jsondata:Name {value: "vector_store_ids"}
     string[] vectorStoreIds?;
 };
 
 
 type CreateVectorStoreFileRequest record {
+    @jsondata:Name {value: "chunking_strategy"}
     ChunkingStrategyRequestParam chunkingStrategy?;
     # A [File](/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files
+    @jsondata:Name {value: "file_id"}
     string fileId;
 };
 
@@ -742,15 +814,17 @@
 
 type StaticChunkingStrategy record {
     # The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`
+    @jsondata:Name {value: "max_chunk_size_tokens"}
     int maxChunkSizeTokens;
     # The number of tokens that overlap between chunks. The default value is `400`.
 
 Note that the overlap must not exceed half of `max_chunk_size_tokens`
+    @jsondata:Name {value: "chunk_overlap_tokens"}
     int chunkOverlapTokens;
 };
 
 # The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy
-type ChunkingStrategyRequestParam ballerinax/openai.finetunes:3.0.0:AutoChunkingStrategyRequestParam|ballerinax/openai.finetunes:3.0.0:StaticChunkingStrategyRequestParam;
+type ChunkingStrategyRequestParam AutoChunkingStrategyRequestParam|StaticChunkingStrategyRequestParam;
 
 
 type ChatCompletionRequestMessageContentPartText record {
@@ -762,6 +836,7 @@
 
 
 type ModifyThreadRequest record {
+    @jsondata:Name {value: "tool_resources"}
     ModifyThreadRequestToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
@@ -770,19 +845,23 @@
 # A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type ModifyThreadRequestToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     ModifyThreadRequestToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     ModifyThreadRequestToolResourcesFileSearch fileSearch?;
 };
 
 
 type ModifyThreadRequestToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
 
 type ModifyThreadRequestToolResourcesFileSearch record {
     # The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread
+    @jsondata:Name {value: "vector_store_ids"}
     string[] vectorStoreIds?;
 };
 
@@ -804,8 +883,11 @@
 # A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files
 
 type MessageContentTextAnnotationsFileCitationObject record {
+    @jsondata:Name {value: "start_index"}
     int startIndex;
+    @jsondata:Name {value: "file_citation"}
     MessageContentTextAnnotationsFileCitationObjectFileCitation fileCitation;
+    @jsondata:Name {value: "end_index"}
     int endIndex;
     # The text in the message content that needs to be replaced
     string text;
@@ -816,14 +898,18 @@
 
 type MessageContentTextAnnotationsFileCitationObjectFileCitation record {
     # The ID of the specific File the citation is from
+    @jsondata:Name {value: "file_id"}
     string fileId;
 };
 
 # A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file
 
 type MessageContentTextAnnotationsFilePathObject record {
+    @jsondata:Name {value: "file_path"}
     MessageContentTextAnnotationsFilePathObjectFilePath filePath;
+    @jsondata:Name {value: "start_index"}
     int startIndex;
+    @jsondata:Name {value: "end_index"}
     int endIndex;
     # The text in the message content that needs to be replaced
     string text;
@@ -834,10 +920,11 @@
 
 type MessageContentTextAnnotationsFilePathObjectFilePath record {
     # The ID of the file that was generated
+    @jsondata:Name {value: "file_id"}
     string fileId;
 };
 
-type MessageContentTextObjectTextAnnotations ballerinax/openai.finetunes:3.0.0:MessageContentTextAnnotationsFileCitationObject|ballerinax/openai.finetunes:3.0.0:MessageContentTextAnnotationsFilePathObject;
+type MessageContentTextObjectTextAnnotations MessageContentTextAnnotationsFileCitationObject|MessageContentTextAnnotationsFilePathObject;
 
 
 type DeleteMessageResponse record {
@@ -850,6 +937,7 @@
 
 type ListMessagesQueries record {
     # Filter messages by the run ID that generated them
+    @http:Query {name: "run_id"}
     string runId?;
     # A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list
     string before?;
@@ -884,16 +972,19 @@
 
 type RunStepDetailsMessageCreationObjectMessageCreation record {
     # The ID of the message that was created by this run step
+    @jsondata:Name {value: "message_id"}
     string messageId;
 };
 
 
 type CreateChatCompletionRequest record {
     # An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used
+    @jsondata:Name {value: "top_logprobs"}
     int? topLogprobs?;
     # Modify the likelihood of specified tokens appearing in the completion.
 
 Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token
+    @jsondata:Name {value: "logit_bias"}
     record {|int...;|}? logitBias?;
     # This feature is in Beta.
 If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
@@ -904,10 +995,12 @@
 A list of functions the model may generate JSON inputs for
 
     @deprecated
+    @constraint:Array {maxLength: 128, minLength: 1}
     ChatCompletionFunctions[] functions?;
     # The maximum number of [tokens](/tokenizer) that can be generated in the chat completion.
 
 The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens
+    @jsondata:Name {value: "max_tokens"}
     int? maxTokens?;
     # Deprecated in favor of `tool_choice`.
 
@@ -919,10 +1012,12 @@
 `none` is the default when no functions are present. `auto` is the default if functions are present
 
     @deprecated
+    @jsondata:Name {value: "function_call"}
     ChatCompletionFunctionCallOption|"none"|"auto" functionCall?;
     # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
 
 [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
+    @jsondata:Name {value: "presence_penalty"}
     decimal? presencePenalty?;
     # A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported
     ChatCompletionTool[] tools?;
@@ -933,14 +1028,18 @@
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or `temperature` but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
 
 [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
+    @jsondata:Name {value: "frequency_penalty"}
     decimal? frequencyPenalty?;
+    @jsondata:Name {value: "response_format"}
     CreateChatCompletionRequestResponseFormat responseFormat?;
     # Up to 4 sequences where the API will stop generating further tokens
     string|string[]? stop?;
+    @jsondata:Name {value: "parallel_tool_calls"}
     ParallelToolCalls parallelToolCalls?;
     # If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions)
     boolean? 'stream?;
@@ -949,7 +1048,9 @@
 We generally recommend altering this or `top_p` but not both
     decimal? temperature?;
     # A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models)
+    @constraint:Array {minLength: 1}
     ChatCompletionRequestMessage[] messages;
+    @jsondata:Name {value: "tool_choice"}
     ChatCompletionToolChoiceOption toolChoice?;
     # ID of the model to use. See the [model endpoint compatibility](/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API
     string|"gpt-4o"|"gpt-4o-2024-05-13"|"gpt-4o-mini"|"gpt-4o-mini-2024-07-18"|"gpt-4-turbo"|"gpt-4-turbo-2024-04-09"|"gpt-4-0125-preview"|"gpt-4-turbo-preview"|"gpt-4-1106-preview"|"gpt-4-vision-preview"|"gpt-4"|"gpt-4-0314"|"gpt-4-0613"|"gpt-4-32k"|"gpt-4-32k-0314"|"gpt-4-32k-0613"|"gpt-3.5-turbo"|"gpt-3.5-turbo-16k"|"gpt-3.5-turbo-0301"|"gpt-3.5-turbo-0613"|"gpt-3.5-turbo-1106"|"gpt-3.5-turbo-0125"|"gpt-3.5-turbo-16k-0613" model;
@@ -959,7 +1060,9 @@
 - When not set, the default behavior is 'auto'.
 
 When this parameter is set, the response body will include the `service_tier` utilized
+    @jsondata:Name {value: "service_tier"}
     "default"?|"auto" serviceTier?;
+    @jsondata:Name {value: "stream_options"}
     ChatCompletionStreamOptions|() streamOptions?;
     # A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)
     string user?;
@@ -1025,6 +1128,7 @@
 
 
 type ChatCompletionRequestMessageContentPartImage record {
+    @jsondata:Name {value: "image_url"}
     ChatCompletionRequestMessageContentPartImageImageUrl imageUrl;
     # The type of the content part
     "image_url" 'type;
@@ -1038,15 +1142,17 @@
     string url;
 };
 
-type ChatCompletionRequestMessageContentPart ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestMessageContentPartText|ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestMessageContentPartImage;
+type ChatCompletionRequestMessageContentPart ChatCompletionRequestMessageContentPartText|ChatCompletionRequestMessageContentPartImage;
 
 
 type ChatCompletionRequestAssistantMessage record {
     # The role of the messages author, in this case `assistant`
     "assistant" role;
+    @jsondata:Name {value: "function_call"}
     ChatCompletionRequestAssistantMessageFunctionCall|() functionCall?;
     # An optional name for the participant. Provides the model information to differentiate between participants of the same role
     string name?;
+    @jsondata:Name {value: "tool_calls"}
     ChatCompletionMessageToolCalls toolCalls?;
     # The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified
     string? content?;
@@ -1068,6 +1174,7 @@
     # The role of the messages author, in this case `tool`
     "tool" role;
     # Tool call that this message is responding to
+    @jsondata:Name {value: "tool_call_id"}
     string toolCallId;
     # The contents of the tool message
     string content;
@@ -1084,12 +1191,13 @@
     string? content;
 };
 
-type ChatCompletionRequestMessage ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestSystemMessage|ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestUserMessage|ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestAssistantMessage|ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestToolMessage|ballerinax/openai.finetunes:3.0.0:ChatCompletionRequestFunctionMessage;
+type ChatCompletionRequestMessage ChatCompletionRequestSystemMessage|ChatCompletionRequestUserMessage|ChatCompletionRequestAssistantMessage|ChatCompletionRequestToolMessage|ChatCompletionRequestFunctionMessage;
 
 # Options for streaming response. Only set this when you set `stream: true`
 
 type ChatCompletionStreamOptions record {
     # If set, an additional chunk will be streamed before the `data: [DONE]` message. The `usage` field on this chunk shows the token usage statistics for the entire request, and the `choices` field will always be an empty array. All other chunks will also include a `usage` field, but with a null value
+    @jsondata:Name {value: "include_usage"}
     boolean includeUsage?;
 };
 
@@ -1097,24 +1205,31 @@
 
 type CreateModerationResponseCategories record {
     # Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders
+    @jsondata:Name {value: "self-harm/intent"}
     boolean selfHarmIntent;
     # Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste
+    @jsondata:Name {value: "hate/threatening"}
     boolean hateThreatening;
     # Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts
+    @jsondata:Name {value: "self-harm/instructions"}
     boolean selfHarmInstructions;
     # Sexual content that includes an individual who is under 18 years old
+    @jsondata:Name {value: "sexual/minors"}
     boolean sexualMinors;
     # Harassment content that also includes violence or serious harm towards any target
+    @jsondata:Name {value: "harassment/threatening"}
     boolean harassmentThreatening;
     # Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment
     boolean hate;
     # Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders
+    @jsondata:Name {value: "self-harm"}
     boolean selfHarm;
     # Content that expresses, incites, or promotes harassing language towards any target
     boolean harassment;
     # Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness)
     boolean sexual;
     # Content that depicts death, violence, or physical injury in graphic detail
+    @jsondata:Name {value: "violence/graphic"}
     boolean violenceGraphic;
     # Content that depicts death, violence, or physical injury
     boolean violence;
@@ -1123,19 +1238,23 @@
 # A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type ModifyAssistantRequestToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     ModifyAssistantRequestToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     ModifyAssistantRequestToolResourcesFileSearch fileSearch?;
 };
 
 
 type ModifyAssistantRequestToolResourcesCodeInterpreter record {
     # Overrides the list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
 
 type ModifyAssistantRequestToolResourcesFileSearch record {
     # Overrides the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant
+    @jsondata:Name {value: "vector_store_ids"}
     string[] vectorStoreIds?;
 };
 
@@ -1143,10 +1262,13 @@
 
 type CompletionUsage record {
     # Number of tokens in the generated completion
+    @jsondata:Name {value: "completion_tokens"}
     int completionTokens;
     # Number of tokens in the prompt
+    @jsondata:Name {value: "prompt_tokens"}
     int promptTokens;
     # Total number of tokens used in the request (prompt + completion)
+    @jsondata:Name {value: "total_tokens"}
     int totalTokens;
 };
 
@@ -1154,6 +1276,7 @@
 
 type RunStepDetailsToolCallsObject record {
     # An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`
+    @jsondata:Name {value: "tool_calls"}
     RunStepDetailsToolCallsObjectToolCalls[] toolCalls;
     # Always `tool_calls`
     "tool_calls" 'type;
@@ -1162,6 +1285,7 @@
 # Details of the Code Interpreter tool call the run step was involved in
 
 type RunStepDetailsToolCallsCodeObject record {
+    @jsondata:Name {value: "code_interpreter"}
     RunStepDetailsToolCallsCodeObjectCodeInterpreter codeInterpreter;
     # The ID of the tool call
     string id;
@@ -1197,14 +1321,16 @@
 
 type RunStepDetailsToolCallsCodeOutputImageObjectImage record {
     # The [file](/docs/api-reference/files) ID of the image
+    @jsondata:Name {value: "file_id"}
     string fileId;
 };
 
-type RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputs ballerinax/openai.finetunes:3.0.0:RunStepDetailsToolCallsCodeOutputLogsObject|ballerinax/openai.finetunes:3.0.0:RunStepDetailsToolCallsCodeOutputImageObject;
+type RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputs RunStepDetailsToolCallsCodeOutputLogsObject|RunStepDetailsToolCallsCodeOutputImageObject;
 
 
 type RunStepDetailsToolCallsFileSearchObject record {
     # For now, this is always going to be an empty object
+    @jsondata:Name {value: "file_search"}
     record {|anydata...;|} fileSearch;
     # The ID of the tool call object
     string id;
@@ -1212,24 +1338,30 @@
     "file_search" 'type;
 };
 
-type RunStepDetailsToolCallsObjectToolCalls ballerinax/openai.finetunes:3.0.0:RunStepDetailsToolCallsCodeObject|ballerinax/openai.finetunes:3.0.0:RunStepDetailsToolCallsFileSearchObject|ballerinax/openai.finetunes:3.0.0:RunStepDetailsToolCallsFunctionObject;
+type RunStepDetailsToolCallsObjectToolCalls RunStepDetailsToolCallsCodeObject|RunStepDetailsToolCallsFileSearchObject|RunStepDetailsToolCallsFunctionObject;
 
 # A vector store is a collection of processed files can be used by the `file_search` tool
 
 type VectorStoreObject record {
+    @jsondata:Name {value: "file_counts"}
     VectorStoreObjectFileCounts fileCounts;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata;
     # The Unix timestamp (in seconds) for when the vector store will expire
+    @jsondata:Name {value: "expires_at"}
     int? expiresAt?;
+    @jsondata:Name {value: "expires_after"}
     VectorStoreExpirationAfter expiresAfter?;
     # The Unix timestamp (in seconds) for when the vector store was last active
+    @jsondata:Name {value: "last_active_at"}
     int? lastActiveAt;
     # The total number of bytes used by the files in the vector store
+    @jsondata:Name {value: "usage_bytes"}
     int usageBytes;
     # The name of the vector store
     string name;
     # The Unix timestamp (in seconds) for when the vector store was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The identifier, which can be referenced in API endpoints
     string id;
@@ -1242,6 +1374,7 @@
 
 type VectorStoreObjectFileCounts record {
     # The number of files that are currently being processed
+    @jsondata:Name {value: "in_progress"}
     int inProgress;
     # The total number of files
     int total;
@@ -1259,6 +1392,7 @@
     # Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`
     "last_active_at" anchor;
     # The number of days after the anchor time that the vector store will expire
+    @constraint:Int {minValue: 1, maxValue: 365}
     int days;
 };
 
@@ -1269,6 +1403,7 @@
 Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.
 
 As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated
+    @jsondata:Name {value: "logit_bias"}
     record {|int...;|}? logitBias?;
     # If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
 
@@ -1277,10 +1412,12 @@
     # The maximum number of [tokens](/tokenizer) that can be generated in the completion.
 
 The token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens
+    @jsondata:Name {value: "max_tokens"}
     int? maxTokens?;
     # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
 
 [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
+    @jsondata:Name {value: "presence_penalty"}
     decimal? presencePenalty?;
     # Echo back the prompt in addition to the completion
     boolean? echo?;
@@ -1299,16 +1436,19 @@
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or `temperature` but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
 
 [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
+    @jsondata:Name {value: "frequency_penalty"}
     decimal? frequencyPenalty?;
     # Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.
 
 When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.
 
 **Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`
+    @jsondata:Name {value: "best_of"}
     int? bestOf?;
     # Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence
     string|string[]?? stop?;
@@ -1320,6 +1460,7 @@
     decimal? temperature?;
     # ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them
     string|"gpt-3.5-turbo-instruct"|"davinci-002"|"babbage-002" model;
+    @jsondata:Name {value: "stream_options"}
     ChatCompletionStreamOptions|() streamOptions?;
     # The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.
 
@@ -1329,7 +1470,7 @@
     string user?;
 };
 
-// Unknown type: PromptItemsArray
+type PromptItemsArray int[];
 
 # Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint)
 
@@ -1347,6 +1488,7 @@
     # This fingerprint represents the backend configuration that the model runs with.
 
 Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism
+    @jsondata:Name {value: "system_fingerprint"}
     string systemFingerprint?;
     # The object type, which is always "text_completion"
     "text_completion" 'object;
@@ -1357,6 +1499,7 @@
     # The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
 `length` if the maximum number of tokens specified in the request was reached,
 or `content_filter` if content was omitted due to a flag from our content filters
+    @jsondata:Name {value: "finish_reason"}
     "stop"|"length"|"content_filter" finishReason;
     int index;
     string text;
@@ -1365,9 +1508,12 @@
 
 
 type CreateCompletionResponseLogprobs record {
+    @jsondata:Name {value: "top_logprobs"}
     record {||}[] topLogprobs?;
+    @jsondata:Name {value: "token_logprobs"}
     decimal[] tokenLogprobs?;
     string[] tokens?;
+    @jsondata:Name {value: "text_offset"}
     int[] textOffset?;
 };
 
@@ -1381,6 +1527,7 @@
 
 type ChatCompletionTokenLogprob record {
     # List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned
+    @jsondata:Name {value: "top_logprobs"}
     ChatCompletionTokenLogprobTopLogprobs[] topLogprobs;
     # The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely
     decimal logprob;
@@ -1420,23 +1567,30 @@
     # The entity that produced the message. One of `user` or `assistant`
     "user"|"assistant" role;
     # If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message
+    @jsondata:Name {value: "assistant_id"}
     string? assistantId;
     # The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints
+    @jsondata:Name {value: "run_id"}
     string? runId;
     # A list of files attached to the message, and the tools they were added to
     MessageObjectAttachments[]|() attachments;
     # The Unix timestamp (in seconds) for when the message was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The content of the message in array of text and/or images
     MessageObjectContent[] content;
     # The Unix timestamp (in seconds) for when the message was completed
+    @jsondata:Name {value: "completed_at"}
     int? completedAt;
     # The [thread](/docs/api-reference/threads) ID that this message belongs to
+    @jsondata:Name {value: "thread_id"}
     string threadId;
     # The identifier, which can be referenced in API endpoints
     string id;
     # The Unix timestamp (in seconds) for when the message was marked as incomplete
+    @jsondata:Name {value: "incomplete_at"}
     int? incompleteAt;
+    @jsondata:Name {value: "incomplete_details"}
     MessageObjectIncompleteDetails|() incompleteDetails;
     # The object type, which is always `thread.message`
     "thread.message" 'object;
@@ -1447,14 +1601,15 @@
 
 type MessageObjectAttachments record {
     # The ID of the file to attach to the message
+    @jsondata:Name {value: "file_id"}
     string fileId?;
     # The tools to add this file to
     MessageObjectTools[] tools?;
 };
 
-type MessageObjectTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearchTypeOnly;
+type MessageObjectTools AssistantToolsCode|AssistantToolsFileSearchTypeOnly;
 
-type MessageObjectContent ballerinax/openai.finetunes:3.0.0:MessageContentImageFileObject|ballerinax/openai.finetunes:3.0.0:MessageContentImageUrlObject|ballerinax/openai.finetunes:3.0.0:MessageContentTextObject;
+type MessageObjectContent MessageContentImageFileObject|MessageContentImageUrlObject|MessageContentTextObject;
 
 # On an incomplete message, details about why the message is incomplete
 
@@ -1468,14 +1623,18 @@
 type FineTuningJobHyperparameters record {
     # The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
 "auto" decides the optimal number of epochs based on the size of the dataset. If setting the number manually, we support any number between 1 and 50 epochs
+    @jsondata:Name {value: "n_epochs"}
     int|"auto" nEpochs?;
 };
 
 
 type ListAssistantsResponse record {
+    @jsondata:Name {value: "first_id"}
     string firstId;
     AssistantObject[] data;
+    @jsondata:Name {value: "last_id"}
     string lastId;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     string 'object;
 };
@@ -1485,19 +1644,24 @@
 type AssistantObject record {
     # The system instructions that the assistant uses. The maximum length is 256,000 characters
     string? instructions;
+    @jsondata:Name {value: "tool_resources"}
     AssistantObjectToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata;
     # The Unix timestamp (in seconds) for when the assistant was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The description of the assistant. The maximum length is 512 characters
     string? description;
     # A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`
+    @constraint:Array {maxLength: 128}
     AssistantObjectTools[] tools?;
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or temperature but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat?;
     # The name of the assistant. The maximum length is 256 characters
     string? name;
@@ -1511,30 +1675,35 @@
     "assistant" 'object;
 };
 
-type AssistantObjectTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type AssistantObjectTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
 # A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type ThreadObjectToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     ThreadObjectToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     ThreadObjectToolResourcesFileSearch fileSearch?;
 };
 
 
 type ThreadObjectToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
 
 type ThreadObjectToolResourcesFileSearch record {
     # The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread
+    @jsondata:Name {value: "vector_store_ids"}
     string[] vectorStoreIds?;
 };
 
 
 type CreateThreadAndRunRequestToolResourcesFileSearch record {
     # The ID of the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant
+    @jsondata:Name {value: "vector_store_ids"}
     string[] vectorStoreIds?;
 };
 
@@ -1562,8 +1731,10 @@
     # Temperature parameter used for generating the segment
     float temperature;
     # Average logprob of the segment. If the value is lower than -1, consider the logprobs failed
+    @jsondata:Name {value: "avg_logprob"}
     float avgLogprob;
     # Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent
+    @jsondata:Name {value: "no_speech_prob"}
     float noSpeechProb;
     # End time of the segment in seconds
     float end;
@@ -1576,12 +1747,13 @@
     # Seek offset of the segment
     int seek;
     # Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed
+    @jsondata:Name {value: "compression_ratio"}
     float compressionRatio;
 };
 
-type InlineResponse2001 ballerinax/openai.finetunes:3.0.0:CreateTranslationResponseJson|ballerinax/openai.finetunes:3.0.0:CreateTranslationResponseVerboseJson;
+type InlineResponse2001 CreateTranslationResponseJson|CreateTranslationResponseVerboseJson;
 
-type CreateThreadAndRunRequestTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type CreateThreadAndRunRequestTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
 # Represents the Queries record for the operation: listRuns
 
@@ -1607,10 +1779,13 @@
 
 type RunStepCompletionUsage record {
     # Number of completion tokens used over the course of the run step
+    @jsondata:Name {value: "completion_tokens"}
     int completionTokens;
     # Number of prompt tokens used over the course of the run step
+    @jsondata:Name {value: "prompt_tokens"}
     int promptTokens;
     # Total number of tokens used (prompt + completion)
+    @jsondata:Name {value: "total_tokens"}
     int totalTokens;
 };
 
@@ -1624,6 +1799,7 @@
 
 type CreateImageRequest record {
     # The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated
+    @jsondata:Name {value: "response_format"}
     "b64_json"?|"url" responseFormat?;
     # The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models
     "1024x1792"?|"256x256"|"512x512"|"1024x1024"|"1792x1024" size?;
@@ -1663,10 +1839,12 @@
 
 type CreateTranscriptionRequest record {
     # The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency
+    @jsondata:Name {value: "timestamp_granularities[]"}
     ("word"|"segment")[] timestampGranularities?;
     # The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm
     record {|byte[] fileContent; string fileName; anydata...;|} file;
     # The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`
+    @jsondata:Name {value: "response_format"}
     "json"|"text"|"srt"|"verbose_json"|"vtt" responseFormat?;
     # The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit
     decimal temperature?;
@@ -1683,14 +1861,18 @@
     # The output of the tool call to be submitted to continue the run
     string output?;
     # The ID of the tool call in the `required_action` object within the run object the output is being submitted for
+    @jsondata:Name {value: "tool_call_id"}
     string toolCallId?;
 };
 
 
 type ListBatchesResponse record {
+    @jsondata:Name {value: "first_id"}
     string firstId?;
     Batch[] data;
+    @jsondata:Name {value: "last_id"}
     string lastId?;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     "list" 'object;
 };
@@ -1698,36 +1880,50 @@
 
 type Batch record {
     # The Unix timestamp (in seconds) for when the batch was cancelled
+    @jsondata:Name {value: "cancelled_at"}
     int cancelledAt?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "request_counts"}
     BatchRequestCounts requestCounts?;
     # The ID of the input file for the batch
+    @jsondata:Name {value: "input_file_id"}
     string inputFileId;
     # The ID of the file containing the outputs of successfully executed requests
+    @jsondata:Name {value: "output_file_id"}
     string outputFileId?;
     # The ID of the file containing the outputs of requests with errors
+    @jsondata:Name {value: "error_file_id"}
     string errorFileId?;
     # The Unix timestamp (in seconds) for when the batch was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The Unix timestamp (in seconds) for when the batch started processing
+    @jsondata:Name {value: "in_progress_at"}
     int inProgressAt?;
     # The Unix timestamp (in seconds) for when the batch expired
+    @jsondata:Name {value: "expired_at"}
     int expiredAt?;
     # The Unix timestamp (in seconds) for when the batch started finalizing
+    @jsondata:Name {value: "finalizing_at"}
     int finalizingAt?;
     # The Unix timestamp (in seconds) for when the batch was completed
+    @jsondata:Name {value: "completed_at"}
     int completedAt?;
     # The OpenAI API endpoint used by the batch
     string endpoint;
     # The Unix timestamp (in seconds) for when the batch will expire
+    @jsondata:Name {value: "expires_at"}
     int expiresAt?;
     # The Unix timestamp (in seconds) for when the batch started cancelling
+    @jsondata:Name {value: "cancelling_at"}
     int cancellingAt?;
     # The time frame within which the batch should be processed
+    @jsondata:Name {value: "completion_window"}
     string completionWindow;
     string id;
     # The Unix timestamp (in seconds) for when the batch failed
+    @jsondata:Name {value: "failed_at"}
     int failedAt?;
     BatchErrors errors?;
     # The object type, which is always `batch`
@@ -1752,25 +1948,30 @@
 
 type CreateEmbeddingResponseUsage record {
     # The number of tokens used by the prompt
+    @jsondata:Name {value: "prompt_tokens"}
     int promptTokens;
     # The total number of tokens used by the request
+    @jsondata:Name {value: "total_tokens"}
     int totalTokens;
 };
 
 # A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type CreateThreadRequestToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     CreateThreadRequestToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     CreateThreadRequestToolResourcesFileSearch fileSearch?;
 };
 
 
 type CreateThreadRequestToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
-// Unknown type: CreateThreadRequestToolResourcesFileSearch
+type CreateThreadRequestToolResourcesFileSearch anydata;
 
 # Represents the Queries record for the operation: listRunSteps
 
@@ -1803,6 +2004,7 @@
 
 type CreateThreadAndRunRequestToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
@@ -1835,7 +2037,7 @@
     string? status_details?;
 };
 
-type ModifyAssistantRequestTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type ModifyAssistantRequestTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
 # Represents the Queries record for the operation: listBatches
 
@@ -1859,17 +2061,22 @@
 
 type VectorStoreFileObject record {
     # The strategy used to chunk the file
+    @jsondata:Name {value: "chunking_strategy"}
     StaticChunkingStrategyResponseParam|OtherChunkingStrategyResponseParam chunkingStrategy?;
     # The total vector store usage in bytes. Note that this may be different from the original file size
+    @jsondata:Name {value: "usage_bytes"}
     int usageBytes;
     # The Unix timestamp (in seconds) for when the vector store file was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The identifier, which can be referenced in API endpoints
     string id;
+    @jsondata:Name {value: "last_error"}
     VectorStoreFileObjectLastError|() lastError;
     # The object type, which is always `vector_store.file`
     "vector_store.file" 'object;
     # The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to
+    @jsondata:Name {value: "vector_store_id"}
     string vectorStoreId;
     # The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use
     "in_progress"|"completed"|"cancelled"|"failed" status;
@@ -1901,6 +2108,7 @@
 
 type CompleteUploadRequest record {
     # The ordered list of Part IDs
+    @jsondata:Name {value: "part_ids"}
     string[] partIds;
     # The optional md5 checksum for the file contents to verify if the bytes uploaded matches what you expect
     string md5?;
@@ -1920,43 +2128,55 @@
 type CreateThreadAndRunRequest record {
     # Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis
     string? instructions?;
+    @jsondata:Name {value: "tool_resources"}
     CreateThreadAndRunRequestToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
     # The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run
+    @jsondata:Name {value: "assistant_id"}
     string assistantId;
     CreateThreadRequest thread?;
     # Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis
     CreateThreadAndRunRequestTools[]|() tools?;
+    @jsondata:Name {value: "truncation_strategy"}
     TruncationObject truncationStrategy?;
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or temperature but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info
+    @jsondata:Name {value: "max_completion_tokens"}
     int? maxCompletionTokens?;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat?;
+    @jsondata:Name {value: "parallel_tool_calls"}
     ParallelToolCalls parallelToolCalls?;
     # If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message
     boolean? 'stream?;
     # What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic
     decimal? temperature?;
+    @jsondata:Name {value: "tool_choice"}
     AssistantsApiToolChoiceOption toolChoice?;
     # The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used
     "gpt-3.5-turbo-16k-0613"?|string|"gpt-4o"|"gpt-4o-2024-05-13"|"gpt-4o-mini"|"gpt-4o-mini-2024-07-18"|"gpt-4-turbo"|"gpt-4-turbo-2024-04-09"|"gpt-4-0125-preview"|"gpt-4-turbo-preview"|"gpt-4-1106-preview"|"gpt-4-vision-preview"|"gpt-4"|"gpt-4-0314"|"gpt-4-0613"|"gpt-4-32k"|"gpt-4-32k-0314"|"gpt-4-32k-0613"|"gpt-3.5-turbo"|"gpt-3.5-turbo-16k"|"gpt-3.5-turbo-0613"|"gpt-3.5-turbo-1106"|"gpt-3.5-turbo-0125" model?;
     # The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info
+    @jsondata:Name {value: "max_prompt_tokens"}
     int? maxPromptTokens?;
 };
 
 # A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type CreateThreadAndRunRequestToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     CreateThreadAndRunRequestToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     CreateThreadAndRunRequestToolResourcesFileSearch fileSearch?;
 };
 
 
 type CreateThreadRequest record {
+    @jsondata:Name {value: "tool_resources"}
     CreateThreadRequestToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
@@ -1968,6 +2188,7 @@
 
 type FineTuningJobEvent record {
     "info"|"warn"|"error" level;
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     string id;
     string message;
@@ -2004,31 +2225,41 @@
 
 type RunStepObject record {
     # The Unix timestamp (in seconds) for when the run step was cancelled
+    @jsondata:Name {value: "cancelled_at"}
     int? cancelledAt;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata;
     # The ID of the [assistant](/docs/api-reference/assistants) associated with the run step
+    @jsondata:Name {value: "assistant_id"}
     string assistantId;
     # The ID of the [run](/docs/api-reference/runs) that this run step is a part of
+    @jsondata:Name {value: "run_id"}
     string runId;
     # Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`
     RunStepCompletionUsage|() usage;
     # The Unix timestamp (in seconds) for when the run step was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired
+    @jsondata:Name {value: "expired_at"}
     int? expiredAt;
     # The type of run step, which can be either `message_creation` or `tool_calls`
     "message_creation"|"tool_calls" 'type;
     # The details of the run step
+    @jsondata:Name {value: "step_details"}
     RunStepDetailsMessageCreationObject|RunStepDetailsToolCallsObject stepDetails;
     # The Unix timestamp (in seconds) for when the run step completed
+    @jsondata:Name {value: "completed_at"}
     int? completedAt;
     # The ID of the [thread](/docs/api-reference/threads) that was run
+    @jsondata:Name {value: "thread_id"}
     string threadId;
     # The identifier of the run step, which can be referenced in API endpoints
     string id;
+    @jsondata:Name {value: "last_error"}
     RunStepObjectLastError|() lastError;
     # The Unix timestamp (in seconds) for when the run step failed
+    @jsondata:Name {value: "failed_at"}
     int? failedAt;
     # The object type, which is always `thread.run.step`
     "thread.run.step" 'object;
@@ -2039,6 +2270,7 @@
 # Details of the message creation by the run step
 
 type RunStepDetailsMessageCreationObject record {
+    @jsondata:Name {value: "message_creation"}
     RunStepDetailsMessageCreationObjectMessageCreation messageCreation;
     # Always `message_creation`
     "message_creation" 'type;
@@ -2064,6 +2296,7 @@
 The contents of the file should differ depending on if the model uses the [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) format.
 
 See the [fine-tuning guide](/docs/guides/fine-tuning) for more details
+    @jsondata:Name {value: "training_file"}
     string trainingFile;
     # The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
 If a seed is not specified, one will be generated for you
@@ -2078,6 +2311,7 @@
 Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.
 
 See the [fine-tuning guide](/docs/guides/fine-tuning) for more details
+    @jsondata:Name {value: "validation_file"}
     string? validationFile?;
     # The hyperparameters used for the fine-tuning job
     CreateFineTuningJobRequestHyperparameters hyperparameters?;
@@ -2097,12 +2331,15 @@
 type CreateFineTuningJobRequestHyperparameters record {
     # Number of examples in each batch. A larger batch size means that model parameters
 are updated less frequently, but with lower variance
+    @jsondata:Name {value: "batch_size"}
     int|"auto" batchSize?;
     # The number of epochs to train the model for. An epoch refers to one full cycle
 through the training dataset
+    @jsondata:Name {value: "n_epochs"}
     int|"auto" nEpochs?;
     # Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
 overfitting
+    @jsondata:Name {value: "learning_rate_multiplier"}
     decimal|"auto" learningRateMultiplier?;
 };
 
@@ -2137,14 +2374,16 @@
 
 type Image record {
     # The prompt that was used to generate the image, if there was any revision to the prompt
+    @jsondata:Name {value: "revised_prompt"}
     string revisedPrompt?;
     # The base64-encoded JSON of the generated image, if `response_format` is `b64_json`
+    @jsondata:Name {value: "b64_json"}
     string b64Json?;
     # The URL of the generated image, if `response_format` is `url` (default)
     string url?;
 };
 
-type CreateAssistantRequestTools ballerinax/openai.finetunes:3.0.0:AssistantToolsCode|ballerinax/openai.finetunes:3.0.0:AssistantToolsFileSearch|ballerinax/openai.finetunes:3.0.0:AssistantToolsFunction;
+type CreateAssistantRequestTools AssistantToolsCode|AssistantToolsFileSearch|AssistantToolsFunction;
 
 # Represents a verbose json transcription response returned by model, based on the provided input
 
@@ -2166,6 +2405,7 @@
     # The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm
     record {|byte[] fileContent; string fileName; anydata...;|} file;
     # The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`
+    @jsondata:Name {value: "response_format"}
     string responseFormat?;
     # The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit
     decimal temperature?;
@@ -2179,6 +2419,7 @@
 type UpdateVectorStoreRequest record {
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "expires_after"}
     VectorStoreExpirationAfter expiresAfter?;
     # The name of the vector store
     string? name?;
@@ -2201,15 +2442,19 @@
 See [upload file](/docs/api-reference/files/create) for how to upload a file.
 
 Your input file must be formatted as a [JSONL file](/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 100 MB in size
+    @jsondata:Name {value: "input_file_id"}
     string inputFileId;
     # The time frame within which the batch should be processed. Currently only `24h` is supported
+    @jsondata:Name {value: "completion_window"}
     "24h" completionWindow;
 };
 
 
 type CreateVectorStoreFileBatchRequest record {
+    @jsondata:Name {value: "chunking_strategy"}
     ChunkingStrategyRequestParam chunkingStrategy?;
     # A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds;
 };
 
@@ -2219,6 +2464,7 @@
     # The name of the file to be uploaded
     string filename;
     # The Unix timestamp (in seconds) for when the Upload was created
+    @jsondata:Name {value: "expires_at"}
     int expiresAt;
     # The `File` object represents a document that has been uploaded to OpenAI
     OpenAIFile file?;
@@ -2227,6 +2473,7 @@
     # The intended number of bytes to be uploaded
     int bytes;
     # The Unix timestamp (in seconds) for when the Upload was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The Upload unique identifier, which can be referenced in API endpoints
     string id;
@@ -2251,24 +2498,31 @@
 
 type CreateModerationResponseCategoryScores record {
     # The score for the category 'self-harm/intent'
+    @jsondata:Name {value: "self-harm/intent"}
     decimal selfHarmIntent;
     # The score for the category 'hate/threatening'
+    @jsondata:Name {value: "hate/threatening"}
     decimal hateThreatening;
     # The score for the category 'self-harm/instructions'
+    @jsondata:Name {value: "self-harm/instructions"}
     decimal selfHarmInstructions;
     # The score for the category 'sexual/minors'
+    @jsondata:Name {value: "sexual/minors"}
     decimal sexualMinors;
     # The score for the category 'harassment/threatening'
+    @jsondata:Name {value: "harassment/threatening"}
     decimal harassmentThreatening;
     # The score for the category 'hate'
     decimal hate;
     # The score for the category 'self-harm'
+    @jsondata:Name {value: "self-harm"}
     decimal selfHarm;
     # The score for the category 'harassment'
     decimal harassment;
     # The score for the category 'sexual'
     decimal sexual;
     # The score for the category 'violence/graphic'
+    @jsondata:Name {value: "violence/graphic"}
     decimal violenceGraphic;
     # The score for the category 'violence'
     decimal violence;
@@ -2301,6 +2555,7 @@
 
 type VectorStoreFileBatchObjectFileCounts record {
     # The number of files that are currently being processed
+    @jsondata:Name {value: "in_progress"}
     int inProgress;
     # The total number of files
     int total;
@@ -2317,6 +2572,7 @@
     # The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask
     record {|byte[] fileContent; string fileName; anydata...;|} image;
     # The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated
+    @jsondata:Name {value: "response_format"}
     "b64_json"?|"url" responseFormat?;
     # The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`
     "1024x1024"?|"256x256"|"512x512" size?;
@@ -2360,11 +2616,14 @@
 
 type CreateVectorStoreRequest record {
     # The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty
+    @jsondata:Name {value: "chunking_strategy"}
     AutoChunkingStrategyRequestParam|StaticChunkingStrategyRequestParam chunkingStrategy?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "expires_after"}
     VectorStoreExpirationAfter expiresAfter?;
     # A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
     # The name of the vector store
     string name?;
@@ -2376,6 +2635,7 @@
 `length` if the maximum number of tokens specified in the request was reached,
 `content_filter` if content was omitted due to a flag from our content filters,
 `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function
+    @jsondata:Name {value: "finish_reason"}
     "stop"|"length"|"tool_calls"|"content_filter"|"function_call" finishReason;
     # The index of the choice in the list of choices
     int index;
@@ -2390,7 +2650,9 @@
 type ChatCompletionResponseMessage record {
     # The role of the author of this message
     "assistant" role;
+    @jsondata:Name {value: "function_call"}
     ChatCompletionResponseMessageFunctionCall functionCall?;
+    @jsondata:Name {value: "tool_calls"}
     ChatCompletionMessageToolCalls toolCalls?;
     # The contents of the message
     string? content;
@@ -2399,10 +2661,12 @@
 # Represents a thread that contains [messages](/docs/api-reference/messages)
 
 type ThreadObject record {
+    @jsondata:Name {value: "tool_resources"}
     ThreadObjectToolResources|() toolResources;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata;
     # The Unix timestamp (in seconds) for when the thread was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The identifier, which can be referenced in API endpoints
     string id;
@@ -2413,6 +2677,7 @@
 
 type ListPaginatedFineTuningJobsResponse record {
     FineTuningJob[] data;
+    @jsondata:Name {value: "has_more"}
     boolean hasMore;
     "list" 'object;
 };
@@ -2421,24 +2686,32 @@
 
 type FineTuningJob record {
     # The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents)
+    @jsondata:Name {value: "training_file"}
     string trainingFile;
     # The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents)
+    @jsondata:Name {value: "result_files"}
     string[] resultFiles;
     # The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running
+    @jsondata:Name {value: "finished_at"}
     int? finishedAt;
     # The seed used for the fine-tuning job
     int seed;
     # The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running
+    @jsondata:Name {value: "fine_tuned_model"}
     string? fineTunedModel;
     # The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents)
+    @jsondata:Name {value: "validation_file"}
     string? validationFile;
     # The Unix timestamp (in seconds) for when the fine-tuning job was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure
     FineTuningJobError|() 'error;
     # The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running
+    @jsondata:Name {value: "estimated_finish"}
     int? estimatedFinish?;
     # The organization that owns the fine-tuning job
+    @jsondata:Name {value: "organization_id"}
     string organizationId;
     # The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details
     FineTuningJobHyperparameters hyperparameters;
@@ -2447,6 +2720,7 @@
     # The object identifier, which can be referenced in the API endpoints
     string id;
     # The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running
+    @jsondata:Name {value: "trained_tokens"}
     int? trainedTokens;
     # A list of integrations to enable for this fine-tuning job
     FineTuningJobIntegrations[]|() integrations?;
@@ -2481,12 +2755,15 @@
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or temperature but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # The system instructions that the assistant uses. The maximum length is 256,000 characters
     string? instructions?;
+    @jsondata:Name {value: "tool_resources"}
     ModifyAssistantRequestToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat?;
     # The name of the assistant. The maximum length is 256 characters
     string? name?;
@@ -2497,6 +2774,7 @@
     # ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them
     string model?;
     # A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`
+    @constraint:Array {maxLength: 128}
     ModifyAssistantRequestTools[] tools?;
 };
 
@@ -2522,6 +2800,7 @@
 
 
 type CreateModerationResponseResults record {
+    @jsondata:Name {value: "category_scores"}
     CreateModerationResponseCategoryScores categoryScores;
     # Whether any of the below categories are flagged
     boolean flagged;
@@ -2534,20 +2813,24 @@
     # If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message
     boolean? 'stream?;
     # A list of tools for which the outputs are being submitted
+    @jsondata:Name {value: "tool_outputs"}
     SubmitToolOutputsRunRequestToolOutputs[] toolOutputs;
 };
 
 # A batch of files attached to a vector store
 
 type VectorStoreFileBatchObject record {
+    @jsondata:Name {value: "file_counts"}
     VectorStoreFileBatchObjectFileCounts fileCounts;
     # The Unix timestamp (in seconds) for when the vector store files batch was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The identifier, which can be referenced in API endpoints
     string id;
     # The object type, which is always `vector_store.file_batch`
     "vector_store.files_batch" 'object;
     # The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to
+    @jsondata:Name {value: "vector_store_id"}
     string vectorStoreId;
     # The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`
     "in_progress"|"completed"|"cancelled"|"failed" status;
@@ -2585,9 +2868,9 @@
     "list" 'object;
 };
 
-// Unknown type: CreateAssistantRequestToolResourcesFileSearch
+type CreateAssistantRequestToolResourcesFileSearch anydata;
 
-type InlineResponse200 ballerinax/openai.finetunes:3.0.0:CreateTranscriptionResponseJson|ballerinax/openai.finetunes:3.0.0:CreateTranscriptionResponseVerboseJson;
+type InlineResponse200 CreateTranscriptionResponseJson|CreateTranscriptionResponseVerboseJson;
 
 # Represents the Queries record for the operation: listFineTuningJobCheckpoints
 
@@ -2601,13 +2884,16 @@
 # A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs
 
 type CreateAssistantRequestToolResources record {
+    @jsondata:Name {value: "code_interpreter"}
     CreateAssistantRequestToolResourcesCodeInterpreter codeInterpreter?;
+    @jsondata:Name {value: "file_search"}
     CreateAssistantRequestToolResourcesFileSearch fileSearch?;
 };
 
 
 type CreateAssistantRequestToolResourcesCodeInterpreter record {
     # A list of [file](/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool
+    @jsondata:Name {value: "file_ids"}
     string[] fileIds?;
 };
 
@@ -2623,12 +2909,15 @@
     # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
 
 We generally recommend altering this or temperature but not both
+    @jsondata:Name {value: "top_p"}
     decimal? topP?;
     # The system instructions that the assistant uses. The maximum length is 256,000 characters
     string? instructions?;
+    @jsondata:Name {value: "tool_resources"}
     CreateAssistantRequestToolResources|() toolResources?;
     # Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long
     record {|anydata...;|}? metadata?;
+    @jsondata:Name {value: "response_format"}
     AssistantsApiResponseFormatOption responseFormat?;
     # The name of the assistant. The maximum length is 256 characters
     string? name?;
@@ -2639,6 +2928,7 @@
     # ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them
     string|"gpt-4o"|"gpt-4o-2024-05-13"|"gpt-4o-mini"|"gpt-4o-mini-2024-07-18"|"gpt-4-turbo"|"gpt-4-turbo-2024-04-09"|"gpt-4-0125-preview"|"gpt-4-turbo-preview"|"gpt-4-1106-preview"|"gpt-4-vision-preview"|"gpt-4"|"gpt-4-0314"|"gpt-4-0613"|"gpt-4-32k"|"gpt-4-32k-0314"|"gpt-4-32k-0613"|"gpt-3.5-turbo"|"gpt-3.5-turbo-16k"|"gpt-3.5-turbo-0613"|"gpt-3.5-turbo-1106"|"gpt-3.5-turbo-0125"|"gpt-3.5-turbo-16k-0613" model;
     # A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`
+    @constraint:Array {maxLength: 128}
     CreateAssistantRequestTools[] tools?;
 };
 
@@ -2660,8 +2950,10 @@
 
 type UploadPart record {
     # The ID of the Upload object that this Part was added to
+    @jsondata:Name {value: "upload_id"}
     string uploadId;
     # The Unix timestamp (in seconds) for when the Part was created
+    @jsondata:Name {value: "created_at"}
     int createdAt;
     # The upload Part unique identifier, which can be referenced in API endpoints
     string id;
@@ -2679,6 +2971,7 @@
     # The model used for the chat completion
     string model;
     # The service tier used for processing the request. This field is only included if the `service_tier` parameter is specified in the request
+    @jsondata:Name {value: "service_tier"}
     "default"?|"scale" serviceTier?;
     # A unique identifier for the chat completion
     string id;
@@ -2687,6 +2980,7 @@
     # This fingerprint represents the backend configuration that the model runs with.
 
 Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism
+    @jsondata:Name {value: "system_fingerprint"}
     string systemFingerprint?;
     # The object type, which is always `chat.completion`
     "chat.completion" 'object;
@@ -2697,6 +2991,7 @@
     # The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square
     record {|byte[] fileContent; string fileName; anydata...;|} image;
     # The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated
+    @jsondata:Name {value: "response_format"}
     "b64_json"?|"url" responseFormat?;
     # The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`
     "1024x1024"?|"256x256"|"512x512" size?;
@@ -2768,7 +3063,7 @@
 
     # Returns a list of files that belong to the user's organization.
     # 
-    resource function get files(map<string|string[]> headers = {}, string purpose = "", anydata Additional Values, ListFilesQueries queries) returns ListFilesResponse|error;
+    resource function get files(map<string|string[]> headers = {}, string purpose = "", ListFilesQueries queries) returns ListFilesResponse|error;
 
     # Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.
     # 
@@ -2829,7 +3124,7 @@
 
     # List your organization's fine-tuning jobs
     # 
-    resource function get fine_tuning/jobs(map<string|string[]> headers = {}, int limit = 0, string after = "", anydata Additional Values, ListPaginatedFineTuningJobsQueries queries) returns ListPaginatedFineTuningJobsResponse|error;
+    resource function get fine_tuning/jobs(map<string|string[]> headers = {}, int limit = 0, string after = "", ListPaginatedFineTuningJobsQueries queries) returns ListPaginatedFineTuningJobsResponse|error;
 
     # Creates a fine-tuning job which begins the process of creating a new model from a given dataset.
     # 
@@ -2847,7 +3142,7 @@
 
     # Get status updates for a fine-tuning job.
     # 
-    resource function get fine_tuning/jobs/[string fineTuningJobId]/events(map<string|string[]> headers = {}, int limit = 0, string after = "", anydata Additional Values, ListFineTuningEventsQueries queries) returns ListFineTuningJobEventsResponse|error;
+    resource function get fine_tuning/jobs/[string fineTuningJobId]/events(map<string|string[]> headers = {}, int limit = 0, string after = "", ListFineTuningEventsQueries queries) returns ListFineTuningJobEventsResponse|error;
 
     # Immediately cancel a fine-tune job.
     # 
@@ -2855,7 +3150,7 @@
 
     # List checkpoints for a fine-tuning job.
     # 
-    resource function get fine_tuning/jobs/[string fineTuningJobId]/checkpoints(map<string|string[]> headers = {}, int limit = 0, string after = "", anydata Additional Values, ListFineTuningJobCheckpointsQueries queries) returns ListFineTuningJobCheckpointsResponse|error;
+    resource function get fine_tuning/jobs/[string fineTuningJobId]/checkpoints(map<string|string[]> headers = {}, int limit = 0, string after = "", ListFineTuningJobCheckpointsQueries queries) returns ListFineTuningJobCheckpointsResponse|error;
 
     # Lists the currently available models, and provides basic information about each one such as the owner and availability.
     # 
@@ -2875,7 +3170,7 @@
 
     # Returns a list of assistants.
     # 
-    resource function get assistants(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListAssistantsQueries queries) returns ListAssistantsResponse|error;
+    resource function get assistants(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListAssistantsQueries queries) returns ListAssistantsResponse|error;
 
     # Create an assistant with a model and instructions.
     # 
@@ -2911,7 +3206,7 @@
 
     # Returns a list of messages for a given thread.
     # 
-    resource function get threads/[string threadId]/messages(map<string|string[]> headers = {}, string runId = "", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListMessagesQueries queries) returns ListMessagesResponse|error;
+    resource function get threads/[string threadId]/messages(map<string|string[]> headers = {}, string runId = "", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListMessagesQueries queries) returns ListMessagesResponse|error;
 
     # Create a message.
     # 
@@ -2935,7 +3230,7 @@
 
     # Returns a list of runs belonging to a thread.
     # 
-    resource function get threads/[string threadId]/runs(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListRunsQueries queries) returns ListRunsResponse|error;
+    resource function get threads/[string threadId]/runs(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListRunsQueries queries) returns ListRunsResponse|error;
 
     # Create a run.
     # 
@@ -2959,7 +3254,7 @@
 
     # Returns a list of run steps belonging to a run.
     # 
-    resource function get threads/[string threadId]/runs/[string runId]/steps(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListRunStepsQueries queries) returns ListRunStepsResponse|error;
+    resource function get threads/[string threadId]/runs/[string runId]/steps(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListRunStepsQueries queries) returns ListRunStepsResponse|error;
 
     # Retrieves a run step.
     # 
@@ -2967,7 +3262,7 @@
 
     # Returns a list of vector stores.
     # 
-    resource function get vector_stores(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListVectorStoresQueries queries) returns ListVectorStoresResponse|error;
+    resource function get vector_stores(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListVectorStoresQueries queries) returns ListVectorStoresResponse|error;
 
     # Create a vector store.
     # 
@@ -2987,7 +3282,7 @@
 
     # Returns a list of vector store files.
     # 
-    resource function get vector_stores/[string vectorStoreId]/files(map<string|string[]> headers = {}, "in_progress"|"completed"|"failed"|"cancelled" filter = "in_progress", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListVectorStoreFilesQueries queries) returns ListVectorStoreFilesResponse|error;
+    resource function get vector_stores/[string vectorStoreId]/files(map<string|string[]> headers = {}, "in_progress"|"completed"|"failed"|"cancelled" filter = "in_progress", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListVectorStoreFilesQueries queries) returns ListVectorStoreFilesResponse|error;
 
     # Create a vector store file by attaching a [File](/docs/api-reference/files) to a [vector store](/docs/api-reference/vector-stores/object).
     # 
@@ -3015,11 +3310,11 @@
 
     # Returns a list of vector store files in a batch.
     # 
-    resource function get vector_stores/[string vectorStoreId]/file_batches/[string batchId]/files(map<string|string[]> headers = {}, "in_progress"|"completed"|"failed"|"cancelled" filter = "in_progress", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", anydata Additional Values, ListFilesInVectorStoreBatchQueries queries) returns ListVectorStoreFilesResponse|error;
+    resource function get vector_stores/[string vectorStoreId]/file_batches/[string batchId]/files(map<string|string[]> headers = {}, "in_progress"|"completed"|"failed"|"cancelled" filter = "in_progress", string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListFilesInVectorStoreBatchQueries queries) returns ListVectorStoreFilesResponse|error;
 
     # List your organization's batches.
     # 
-    resource function get batches(map<string|string[]> headers = {}, int limit = 0, string after = "", anydata Additional Values, ListBatchesQueries queries) returns ListBatchesResponse|error;
+    resource function get batches(map<string|string[]> headers = {}, int limit = 0, string after = "", ListBatchesQueries queries) returns ListBatchesResponse|error;
 
     # Creates and executes a batch from an uploaded file of requests
     # 
`````

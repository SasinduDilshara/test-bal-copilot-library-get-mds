# ai.eval — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `ai.eval` |
| **Old file** | `ai.eval/old/ballerina_ai.eval.bal.txt` |
| **New file** | `ai.eval/new/ballerina_ai.eval.bal.txt` |
| **Old lines** | 470 |
| **New lines** | 502 |
| **Lines added** | 33 |
| **Lines removed** | 1 |
| **Hunks** | 24 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (2)

- `annotation EvalTemplate`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 218–224 | 218–225 | Types | +2 | −1 |
| 2 | 238–243 | 239–245 | Functions | +1 | −0 |
| 3 | 248–253 | 250–256 | Functions | +1 | −0 |
| 4 | 259–264 | 262–268 | Functions | +1 | −0 |
| 5 | 269–274 | 273–279 | Functions | +1 | −0 |
| 6 | 280–285 | 285–291 | Functions | +1 | −0 |
| 7 | 290–295 | 296–302 | Functions | +1 | −0 |
| 8 | 300–305 | 307–313 | Functions | +1 | −0 |
| 9 | 310–315 | 318–324 | Functions | +1 | −0 |
| 10 | 321–326 | 330–336 | Functions | +1 | −0 |
| 11 | 332–337 | 342–348 | Functions | +1 | −0 |
| 12 | 343–348 | 354–360 | Functions | +1 | −0 |
| 13 | 353–358 | 365–371 | Functions | +1 | −0 |
| 14 | 363–368 | 376–382 | Functions | +1 | −0 |
| 15 | 374–379 | 388–394 | Functions | +1 | −0 |
| 16 | 385–390 | 400–406 | Functions | +1 | −0 |
| 17 | 394–399 | 410–416 | Functions | +1 | −0 |
| 18 | 404–409 | 421–427 | Functions | +1 | −0 |
| 19 | 416–421 | 434–440 | Functions | +1 | −0 |
| 20 | 428–433 | 447–453 | Functions | +1 | −0 |
| 21 | 438–443 | 458–464 | Functions | +1 | −0 |
| 22 | 446–451 | 467–473 | Functions | +1 | −0 |
| 23 | 459–464 | 481–487 | Functions | +1 | −0 |
| 24 | 467–470 | 490–502 | Functions | +9 | −0 |

---

## Unified diff

`````diff
--- ai.eval/old/ballerina_ai.eval.bal.txt	2026-08-12 12:57:29
+++ ai.eval/new/ballerina_ai.eval.bal.txt	2026-08-12 13:19:19
@@ -218,7 +218,8 @@
     boolean needsEvalset;
 };
 
-// Unknown type: Error
+# Represents an error that occurs while evaluating an agent.
+type Error error;
 
 # The matching strategies supported by the tool-trajectory evaluation.
 enum TrajectoryMatchMode {
@@ -238,6 +239,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Semantic Similarity", description: "Uses an LLM judge to compare each agent response against the expected response in the eval set", kind: "LLM_JUDGE", needsEvalset: true}
 function evaluateSemanticSimilarity(ai:Agent targetAgent, ai:ConversationThread thread, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check that the factual information in agent responses is
@@ -248,6 +250,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Output Accuracy", description: "Uses an LLM judge to check the factual correctness of agent responses", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateOutputAccuracy(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response helps the user with what
@@ -259,6 +262,7 @@
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + successCriteria - Optional additional success criteria given to the judge
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Helpfulness", description: "Uses an LLM judge to check whether the agent response actually helps the user", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateHelpfulness(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8, string successCriteria = "") returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response is clear, well-structured,
@@ -269,6 +273,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Clarity", description: "Uses an LLM judge to check readability, structure, and absence of ambiguity in agent responses", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateClarity(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response addresses every part of
@@ -280,6 +285,7 @@
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + expectedCoverage - Optional description of what the response is expected to cover
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Completeness", description: "Uses an LLM judge to check whether the agent response addresses every part of the query", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateCompleteness(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8, string expectedCoverage = "") returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response addresses the same topic
@@ -290,6 +296,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Relevance", description: "Uses an LLM judge to check whether the agent response stays on the query's topic and intent", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateRelevance(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response maintains logical flow and
@@ -300,6 +307,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Coherence", description: "Uses an LLM judge to check logical flow and internal consistency of agent responses", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateCoherence(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent response communicates its content
@@ -310,6 +318,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Conciseness", description: "Uses an LLM judge to check agent responses for unnecessary verbosity and filler", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateConciseness(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check the agent response for harmful, toxic, biased, or
@@ -321,6 +330,7 @@
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + safetyContext - Optional context about the interaction type (e.g. "children's education")
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Safety", description: "Uses an LLM judge to check agent responses for harmful, toxic, biased, or policy-violating content", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateSafety(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8, string safetyContext = "") returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the tone of the agent response is appropriate,
@@ -332,6 +342,7 @@
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + toneContext - Optional context about the expected tone (e.g. "customer support")
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Tone", description: "Uses an LLM judge to check agent responses for appropriate and professional tone", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateTone(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8, string toneContext = "") returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the factual claims in the agent response are
@@ -343,6 +354,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Groundedness", description: "Uses an LLM judge to check that agent response claims are grounded in tool evidence", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateGroundedness(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent's execution steps are logical,
@@ -353,6 +365,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Reasoning Quality", description: "Uses an LLM judge to check whether the agent's execution steps are logical and purposeful", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateReasoningQuality(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent's execution path is efficient, with
@@ -363,6 +376,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Path Efficiency", description: "Uses an LLM judge to detect redundant steps, loops, and wasted work in agent runs", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluatePathEfficiency(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check how gracefully the agent detects and recovers from
@@ -374,6 +388,7 @@
 # + judgeModel - The model provider used as the LLM judge
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Error Recovery", description: "Uses an LLM judge to check how gracefully the agent recovers from errors during execution", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateErrorRecovery(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8) returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Uses an LLM judge to check whether the agent complies with all instructions —
@@ -385,6 +400,7 @@
 # + judgeScoreThreshold - The minimum judge score (in [0.0, 1.0]) required to pass
 # + successCriteria - Optional description of what is expected from the agent
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Instruction Following", description: "Uses an LLM judge to check whether the agent follows system prompt constraints and user instructions", kind: "LLM_JUDGE", needsEvalset: false}
 function evaluateInstructionFollowing(ai:Agent targetAgent, ai:ConversationThread|string queries, ai:ModelProvider judgeModel, float judgeScoreThreshold = 0.8, string successCriteria = "") returns Error|(); // Special Agent Note: Agent, ConversationThread, ModelProvider FROM ballerina/ai package
 
 # Checks that agent response lengths fall within the given bounds (inclusive).
@@ -394,6 +410,7 @@
 # + minLength - The minimum accepted response length (inclusive)
 # + maxLength - The maximum accepted response length (inclusive)
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Length Compliance", description: "Checks that agent response lengths stay within the configured bounds", kind: "RULE_BASED", needsEvalset: false}
 function assertLengthCompliance(ai:Agent targetAgent, ai:ConversationThread|string queries, int minLength = 1, int maxLength = 10000) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks the agent's tool calls against the trajectory recorded in the eval set.
@@ -404,6 +421,7 @@
 # + thread - The conversation thread loaded from an eval set
 # + matchMode - The trajectory matching strategy to apply
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Tool Trajectory", description: "Checks the agent's tool calls against the eval set trajectory using a configurable matching mode", kind: "RULE_BASED", needsEvalset: true}
 function evaluateToolTrajectory(ai:Agent targetAgent, ai:ConversationThread thread, TrajectoryMatchMode matchMode = STRICT) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that every agent response exactly matches the expected response recorded
@@ -416,6 +434,7 @@
 A–Z is folded, so non-ASCII letters still compare case-sensitively
 # + stripWhitespace - Whether to strip leading/trailing whitespace before comparing
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Exact Match", description: "Checks that each agent response exactly matches the expected response in the eval set", kind: "RULE_BASED", needsEvalset: true}
 function assertExactMatch(ai:Agent targetAgent, ai:ConversationThread thread, boolean caseSensitive = true, boolean stripWhitespace = true) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that agent responses contain none of the prohibited strings. For a thread,
@@ -428,6 +447,7 @@
 # + caseSensitive - Whether the matching is case-sensitive. When `false`, only ASCII
 A–Z is folded, so non-ASCII letters still compare case-sensitively
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Content Safety", description: "Checks that agent responses contain none of the configured prohibited strings", kind: "RULE_BASED", needsEvalset: false}
 function assertContentSafety(ai:Agent targetAgent, ai:ConversationThread|string queries, string[] prohibitedStrings, boolean caseSensitive = false) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that the expected response recorded in the eval set appears as a substring
@@ -438,6 +458,7 @@
 # + caseSensitive - Whether the substring matching is case-sensitive. When `false`, only
 ASCII A–Z is folded, so non-ASCII letters still compare case-sensitively
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Contains Match", description: "Checks that the expected response from the eval set appears as a substring of the agent response", kind: "RULE_BASED", needsEvalset: true}
 function assertContainsMatch(ai:Agent targetAgent, ai:ConversationThread thread, boolean caseSensitive = false) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that the agent completes every run within the given number of iterations.
@@ -446,6 +467,7 @@
 # + queries - The eval set conversation thread, or a single user query
 # + maxIterations - The maximum number of iterations allowed per agent run
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Iteration Efficiency", description: "Checks that the agent completes each run within the configured iteration limit", kind: "RULE_BASED", needsEvalset: false}
 function assertIterationEfficiency(ai:Agent targetAgent, ai:ConversationThread|string queries, int maxIterations = 5) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that the required strings all appear in the agent's output. For a thread,
@@ -459,6 +481,7 @@
 # + caseSensitive - Whether the matching is case-sensitive. When `false`, only ASCII
 A–Z is folded, so non-ASCII letters still compare case-sensitively
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Content Coverage", description: "Checks that all required strings appear in the agent output", kind: "RULE_BASED", needsEvalset: false}
 function assertContentCoverage(ai:Agent targetAgent, ai:ConversationThread|string queries, string[] requiredStrings, boolean caseSensitive = false) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
 
 # Checks that the agent produces every response within the given time limit.
@@ -467,4 +490,13 @@
 # + queries - The eval set conversation thread, or a single user query
 # + maxLatencySeconds - The maximum time allowed per agent run, in seconds
 # + return - `()` if the evaluation ran, or an `Error` if it could not; failing verdicts are raised as assertions
+@EvalTemplate {label: "Latency Performance", description: "Checks that the agent responds within the configured time limit", kind: "RULE_BASED", needsEvalset: false}
 function assertLatencyPerformance(ai:Agent targetAgent, ai:ConversationThread|string queries, decimal maxLatencySeconds = 10) returns Error|(); // Special Agent Note: Agent, ConversationThread FROM ballerina/ai package
+
+// --- Annotations ---
+
+# Marks a function as an evaluation template that low-code tooling can discover.
+# 
+# Declared `const` so every attached value is a compile-time constant, letting the
+# Language Server read the metadata from the syntax tree without executing code.
+public annotation EvalTemplateConfig EvalTemplate on function;
`````

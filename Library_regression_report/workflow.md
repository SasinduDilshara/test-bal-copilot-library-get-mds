# ballerina/workflow 0.8.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/workflow` |
| Pinned version | `0.8.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-workflow |
| Tag reviewed | `v0.8.3` (commit `ff0e44b615da18c8635777a4539d8698b23d274e`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/workflow/0.8.3/java21` |
| Old render | `638` lines |
| New render | `714` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three things changed, all in the right
direction:

1. The 4 `// Unknown type:` placeholders in `old` (`DurableAgent`, `AgentBusyError`,
   `HumanTaskTimeoutError`, `WorkflowBusyError`) become real definitions — a full 8-method class and
   3 error type definitions.
2. A new `// --- Annotations ---` section surfaces `@workflow:Workflow` and `@workflow:Activity`,
   the two annotations that are the entire entry point to this library. `old` emitted neither.
3. Five `Context` methods that `old` wrongly rendered as `remote function` are now rendered as plain
   `function`, matching the library source exactly. The distinction is load-bearing here: `ctx.sleep(...)`
   vs `ctx->callActivity(...)` — `old` would have led an LLM to write `ctx->sleep()`, which does not compile.

Nothing was removed. The 9 removed lines are exactly the 4 placeholder comments and the 5 mis-qualified
`remote` method lines. The README block, the `functions` list and the whole `clients` payload are
byte-identical between the two JSONs.

## 2. Change inventory

Line counts (`wc -l`): old 638, new 714. Diff: 85 lines added, 9 removed, 7 hunks.

Removed lines — the complete set (`diff old new | grep '^<'`):

```
// Unknown type: DurableAgent
// Unknown type: AgentBusyError
// Unknown type: HumanTaskTimeoutError
// Unknown type: WorkflowBusyError
    remote function sleep(Duration duration) returns error?;
    remote function currentTime() returns time:Utc; // ...
    remote function isReplaying() returns boolean;
    remote function getWorkflowId() returns string|error;
    remote function getWorkflowType() returns string|error;
```

Top-level declarations added in `new` (6), removed (0):

| Kind | Name | New render line |
|---|---|---|
| class | `DurableAgent` (+ 8 methods: `init`, `bindAgentName`, `run`, `sendData`, `getResult`, `getDataResult`, `waitForResult`, `waitForDataResult`) | 324 |
| type (error) | `AgentBusyError` | 413 |
| type (error) | `HumanTaskTimeoutError` | 460 |
| type (error) | `WorkflowBusyError` | 479 |
| annotation | `Workflow` | 705 |
| annotation | `Activity` | 714 |

Declarations modified (5): `Context.sleep`, `.currentTime`, `.isReplaying`, `.getWorkflowId`,
`.getWorkflowType` — `remote function` → `function`.

Section markers: old 5, new 6 (`// --- Annotations ---` is new).
`// Unknown type:` count: old 4, new 0.
Version-qualified type refs (`mod:x.y.z:Type`): 0 on both sides.

JSON-level comparison (`old/ballerina_workflow.json` vs `new/ballerina_workflow.json`):

| key | old | new |
|---|---|---|
| `typeDefs` | 27 | 27 |
| `clients` | 1 | 1 |
| `functions` | 5 | 5 |
| `services` | 0 | 0 |
| `annotations` | **0** | **2** |
| `readme` | 6993 chars | 6993 chars (identical) |

Only 4 typeDef objects differ, and only by added keys: `DurableAgent` gains `"type": "Class"`; the
three error types gain `"baseType"`. `functions` and `clients` are byte-identical after sort.
This localises the change precisely: the extractor now tags class/error kinds and emits annotations;
the renderer now honours the `"type": "Normal Function"` / `"Remote Function"` field that was already
present in the old JSON but ignored by the old renderer.

## 3. Correctness against library source

Bala `modules/workflow/*.bal` and the GitHub `v0.8.3` `ballerina/*.bal` are identical for all 8 files
(`diff -q` on agent, annotations, config, context, durable_agent, functions, module, types → all "same"),
so source citations below are unambiguous.

Everything `new` adds, checked against source:

| New render | Source | Verdict |
|---|---|---|
| `class DurableAgent { ... }` (l.324) | `durable_agent.bal:198` `public isolated class DurableAgent` | correct (qualifiers dropped, see §5) |
| `function bindAgentName(string agentName) returns ()` | `durable_agent.bal:215` `public isolated function bindAgentName(string agentName)` | correct |
| `function run(string query, anydata input = {})` | `durable_agent.bal:230` `... run(string query, anydata input = ())` | signature correct, default misrendered (§5) |
| `function sendData(string instanceId, string eventName, anydata data) returns string\|error` | `durable_agent.bal:242` | correct |
| `function getResult(string instanceId, anydata T = anydata) returns T\|error` | `durable_agent.bal:257` `typedesc<anydata> T = <>` | correct under the pipeline's typedesc convention (same convention used in `old` for `Context` methods) |
| `function getDataResult(string instanceId, string token, ...)` | `durable_agent.bal:270` | correct |
| `function waitForResult(string instanceId, ...)` | `durable_agent.bal:286` | correct |
| `function waitForDataResult(string instanceId, string token, ...)` | `durable_agent.bal:299` | correct |
| `type AgentBusyError error;` | `durable_agent.bal:179` `public type AgentBusyError distinct error;` | `distinct` dropped (§5) |
| `type HumanTaskTimeoutError error<HumanTaskTimeoutDetail>;` | `types.bal:136` `public type HumanTaskTimeoutError distinct error<HumanTaskTimeoutDetail>;` | detail record correct, `distinct` dropped |
| `type WorkflowBusyError error;` | `types.bal:158` `public type WorkflowBusyError distinct error;` | `distinct` dropped |
| `public annotation Workflow on function;` | `annotations.bal:24` — exact match | correct |
| `public annotation Activity on function;` | `annotations.bal:33` — exact match | correct |

The `remote` fix, verified method by method against `context.bal`:

| Method | Source qualifier (context.bal) | old render | new render |
|---|---|---|---|
| `callActivity` | `remote isolated` (l.56) | `remote` | `remote` ✓ |
| `sleep` | `public isolated` (l.72) | `remote` ✗ | plain ✓ |
| `currentTime` | `public isolated` (l.87) | `remote` ✗ | plain ✓ |
| `isReplaying` | `public isolated` (l.97) | `remote` ✗ | plain ✓ |
| `getWorkflowId` | `public isolated` (l.104) | `remote` ✗ | plain ✓ |
| `getWorkflowType` | `public isolated` (l.111) | `remote` ✗ | plain ✓ |
| `await` | `remote isolated` (l.137) | `remote` | `remote` ✓ |
| `awaitHumanTask` | `remote isolated` (l.169) | `remote` | `remote` ✓ |
| `runChildWorkflow` | `remote isolated` (l.200) | `remote` | `remote` ✓ |
| `getChildWorkflowResult` | `remote isolated` (l.220) | `remote` | `remote` ✓ |
| `waitForChildWorkflow` | `remote isolated` (l.233) | `remote` | `remote` ✓ |
| `callWorkflow` | `remote isolated` (l.252) | `remote` | `remote` ✓ |
| `sendDataToChildWorkflow` | `remote isolated` (l.271) | `remote` | `remote` ✓ |

All 13 methods now match source; 5 were wrong in `old`, 0 are wrong in `new`. The library's own
doc examples confirm the calling convention (`ctx.sleep({seconds: 30})`, `ctx->getChildWorkflowResult(kycId)`).

Cross-package types depended on by others render correctly and identically on both sides:
`time:Utc` in `Context.currentTime` (with the `// Special Agent Note: Utc FROM ballerina/time package`
marker), `ai:SystemPrompt` / `ai:ModelProvider` / `ai:ToolConfig` / `ai:BaseToolKit` in
`DurableAgentConfig` and `DurableAgent.init`.

## 4. Regressions

**None found.**

What I checked to conclude that:
- The full set of deleted lines (`diff | grep '^<'`, 9 lines) — all 9 are the placeholder comments and
  the 5 incorrect `remote` qualifiers. No declaration, parameter, default, return type or doc line is
  deleted.
- Declaration set extracted from both files with `grep -nE '^(public )?(isolated )?(client )?(type|class|function|annotation|const|enum|listener|service)'`:
  `new` is a strict superset of `old` (6 additions, 0 deletions).
- JSON `functions`, `clients` and `readme` compared with `json.dumps(..., sort_keys=True)` — identical.
- README block: lines 7–141 on both sides, byte-identical, 6993 chars in both JSONs.
- Doc-comment quality: 20 stray un-`#`-prefixed doc-continuation lines after the `// --- Types ---`
  marker on **both** sides (identical multiset — `diff` of the sorted line counts shows the only
  difference is the 6 genuinely-new declarations). No doc text was lost or degraded.
- `// Special Agent Note:` cross-package markers: present and unchanged for `time:Utc`, `ai:*`.

## 5. Issues in `new` (independent of `old`)

Five inaccuracies, all inside the newly-rendered `DurableAgent` / error types — i.e. they exist
because `new` renders more, not because `new` degraded anything. Ranked by impact:

1. **`DurableAgent.init` emits a non-compiling parameter list.** The included-record parameter
   `*DurableAgentConfig config` (`durable_agent.bal:207`) is flattened into its 10 fields **and** the
   `config` parameter is retained at the end with no default:
   `function init(ai:SystemPrompt systemPrompt = {...}, ..., int maxIter = 16, DurableAgentConfig config) returns error?;`
   A required parameter after defaultable parameters is invalid Ballerina, and the trailing `config`
   duplicates the ten preceding fields. Root cause is in the JSON, not the renderer: the `config`
   parameter object carries `"optional": true` but no `"default"`, and is present **identically in the
   old JSON** — `old` simply never rendered the class. Also note the real constructor is called with a
   record (`check new ({systemPrompt: ..., model: ...})`, per the class doc), which neither form conveys.

2. **`distinct` dropped on all three error types.** Source declares
   `distinct error` (`durable_agent.bal:179`, `types.bal:136`, `types.bal:158`); the render emits plain
   `error`. Matters here because the docs instruct users to type-test against them
   (`if result is workflow:WorkflowBusyError`), which relies on distinctness.

3. **Parenthesised union-array types lose their parentheses in `init`.**
   `(ActivityDecl|function)[]` → `ActivityDecl|function[]` and
   `(ToolDecl|ai:ToolConfig|ai:BaseToolKit|function)[]` → `ToolDecl|ai:ToolConfig|ai:BaseToolKit|function[]`
   (`durable_agent.bal:166–167`). These denote different types. The same defect is present in the
   `DurableAgentConfig` record on **both** sides (old line 345, new line 391), so the mechanism is
   pre-existing; only the `init` occurrence is new.

4. **`typedesc<anydata>?` collapses to `anydata|()` in `init`** (`inputType`, `resultType`).
   Inconsistent with the `DurableAgentConfig` record two definitions later, which renders the same
   fields correctly as `typedesc<anydata>? inputType?` on both sides.

5. **`DurableAgent.run` default misrendered**: source `anydata input = ()` (`durable_agent.bal:230`)
   renders as `anydata input = {}`. Same defect exists on both sides for
   `Context.runChildWorkflow` (`context.bal:200`) and `Context.callWorkflow` (`context.bal:252`), so it
   is a pre-existing renderer behaviour, not new.

Shared with `old` (listed for completeness, not counted above): closed records `record {| |}` render as
open `record {`; record fields with defaults render as optional `field?` with the default dropped
(all 10 `DurableAgentConfig` fields); `public const NoAutomaticRetry = ()` renders as
`const nil NoAutomaticRetry = ()` (`nil` is not a Ballerina type name); `public type ManualRetry HumanReview`
is expanded to `type ManualRetry string|string[]`, losing the alias; enum members are additionally
emitted as loose `const string` declarations; 20 doc-continuation lines lack their `#` prefix.

## 6. Coverage gaps vs. the library

**Default module (`workflow`): 0 gaps in `new`.** All 27 public symbols declared in
`modules/workflow/*.bal` appear in the new render:

- `annotations.bal`: `Workflow`, `Activity` — **new only** (missing from `old`)
- `context.bal`: `Context` (client class, 13 methods + init)
- `functions.bal`: `run`, `sendData`, `getPendingAgentEvents`, `getWorkflowResult`, `completeHumanTask`
- `types.bal`: `Mode`, `NoAutomaticRetry`, `NoRetry`, `AutoRetry`, `HumanReview`, `ManualRetry`,
  `ActivityOptions`, `HumanTaskTimeoutDetail`, `HumanTaskTimeoutError`*, `PendingAgentEvent`,
  `WorkflowBusyError`*, `Duration`
- `durable_agent.bal`: `EventCardinality`, `EventDecl`, `ActivityDecl`, `ToolDecl`, `HumanTaskDecl`,
  `PeerDecl`, `DurableAgentConfig`, `AgentBusyError`*, `DurableAgent`*

(* = missing from `old`, present in `new`. `old` therefore had 6 coverage gaps; `new` has 0.)

**Submodule-only API — shared gap, both sides.** The bala ships 4 modules
(`modules/`: `workflow`, `workflow.activity`, `workflow.internal`, `workflow.management`), and both
pipelines extract only `pkg.getDefaultModule()`. **69 public declarations** are invisible to both
renders (`grep -hcE '^public ' modules/<m>/*.bal`):

| Submodule | public decls | notable |
|---|---|---|
| `workflow.activity` | 5 | `callRestAPI`, `sendEmail`, `callSoapAPI`, `RestMethod`, `EmailOptions` |
| `workflow.internal` | 12 | `registerWorkflow`, `registerDurableAgent*` — plugin-generated code targets these |
| `workflow.management` | 52 | the entire management API + `ManagementServiceConfig`, `enableManagementApi`, `port` |

This is the biggest practical omission for this library — `workflow.management` is nearly half the
public surface — but it is identical on both sides and not attributable to spec v2.

Also invisible on both sides: the 14 module-level `configurable` variables in `config.bal:27–102`
(`mode`, `url`, `namespace`, `authApiKey`, `taskQueue`, `maxConcurrent*`, `activityRetry*`), which are
the entire runtime configuration story. The pipeline has no `configurable` channel.

## 7. Compiler plugin

`has_plugin: true` — confirmed: `compiler-plugin/compiler-plugin.json` in the bala declares
`plugin_class: io.ballerina.lib.workflow.compiler.WorkflowCompilerPlugin`, backed by
`compiler-plugin/libs/workflow-compiler-plugin-0.8.3.jar`. Source read at `compiler-plugin/src/main/java/io/ballerina/lib/workflow/compiler/` (19 Java files).

`WorkflowCompilerPlugin.init` registers exactly two things (lines 44, 47):
a `WorkflowCodeAnalyzer` and a `WorkflowCodeModifier`.

- **Code modifier** (`WorkflowSourceModifier`): generates a private
  `function __registerWorkflowsAndStart() returns boolean|error` that calls
  `wfInternal:registerWorkflow(fn, "fn", {...})` for every `@Workflow` function, plus a module-init
  call `boolean _ = check __registerWorkflowsAndStart();`. For `DurableAgent` declarations it emits
  the `registerDurableAgent*` calls keyed by the module-level variable name — which is exactly why the
  class doc says the agent must be assigned to a module-level `final` variable and why
  `bindAgentName` exists.
- **Code analyzer** (`WorkflowCodeAnalyzer` + 7 validator/analysis tasks): ~50 diagnostics defined in
  `WorkflowDiagnostic.java` (48 ERROR, 2 WARNING). They encode hard usage rules that the render does
  not state, e.g. `@Workflow function must declare 'workflow:Context' as its first parameter`;
  `@Workflow function can have at most 3 parameters: Context, input, and events`;
  `Direct calls to @Activity functions are not allowed. Use 'ctx->callActivity(functionName, args...)' instead`;
  `Using 'time:utcNow()' inside a @Workflow function is non-deterministic. Use 'ctx.currentTime()' instead`;
  `Named worker declarations are not allowed inside @Workflow functions`; `'fork'`/`'start'` banned inside
  workflows; activity client-object arguments must be module-level `final`/`configurable`.

**Gap:** none of these constraints are expressible in the render's declaration syntax, and the render
does not carry them. The README block partially compensates — it shows the canonical
`function processOrder(workflow:Context ctx, OrderRequest request)` shape and a `ctx->callActivity` call
— but an LLM working from the render alone has no signal that `fork`, `start`, named workers or direct
activity calls are compile errors. This is a pipeline-wide limitation, identical on both sides.
One thing the render now *does* get right that the plugin depends on: the `@Workflow`/`@Activity`
annotations themselves, which `old` omitted entirely — without them nothing the plugin does is reachable.

## 8. Other considerations

- **Pre-1.0 (`0.8.3`)**. Central reports `deprecated: null`, `deprecateMessage: ""`; built for
  `ballerinaVersion 2201.13.4`, `balaVersion 3.0.0`. API is not stability-guaranteed.
- **Size**: 714 lines / ~74.8 KB JSON (old: 638 lines / ~74.1 KB). The +12% line growth buys the
  library's central abstraction (`DurableAgent`) and its two annotations — a very good token trade.
- **`bindAgentName` is rendered** even though its own doc says "not part of the public API surface".
  It is genuinely `public` in source (`durable_agent.bal:215`), so the render is faithful; but it is
  noise that an LLM could be tempted to call. Not a render defect.
- **The single highest-value fix in this diff** is the annotations section. `ballerina/workflow` is
  annotation-driven: without `@workflow:Workflow` / `@workflow:Activity` an LLM cannot write a single
  working program from the render. `old` shipped 638 lines that omitted both.
- **Second-highest** is the `remote` correction. `old` told the consumer to write `ctx->sleep(...)`
  and `ctx->currentTime()`; both are compile errors. Five methods, all of them on the hot path.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v0.8.3 …/module-ballerina-workflow` | success; HEAD `ff0e44b615da18c8635777a4539d8698b23d274e`, tag `v0.8.3` |
| `diff -q ballerina/<f>.bal <bala>/modules/workflow/<f>.bal` × 8 | all identical (agent, annotations, config, context, durable_agent, functions, module, types) |
| `wc -l old/new .bal.txt` | 638 / 714 |
| `diff old new \| grep -c '^>'` | 85 added |
| `diff old new \| grep '^<'` | 9 removed — listed verbatim in §2 |
| `grep -c '^// Unknown type:'` | old 4, new 0 |
| `grep -n '^// --- '` | old 5 markers (README/END README/Types/Client/Functions); new 6 (+ Annotations at 696) |
| `grep -nE '^(public )?(isolated )?(client )?(type\|class\|function\|annotation\|const\|enum\|listener\|service)'` on both | new = old + 6 (DurableAgent, AgentBusyError, HumanTaskTimeoutError, WorkflowBusyError, Workflow, Activity); 0 removed |
| Python: compare `typeDefs` by name, old vs new | name sets equal (27 each); 4 objects differ, only by added `type`/`baseType` keys |
| Python: `json.dumps(functions/clients, sort_keys=True)` old vs new | identical |
| Python: `readme` old vs new | identical, 6993 chars |
| Python: `clients[0].functions[*].type` in **old** JSON | `sleep`/`currentTime`/`isReplaying`/`getWorkflowId`/`getWorkflowType` already tagged `"Normal Function"`; the other 8 `"Remote Function"` — old renderer ignored the field |
| Python: `DurableAgent.init` parameters in **old** JSON | 11 params incl. trailing `config` with `"optional": true` and no `"default"`; identical in new |
| `grep -nE 'remote function\|public isolated function' <bala>/modules/workflow/context.bal` | 8 remote, 5 public non-remote — matches `new` exactly (table in §3) |
| `grep -nE '^public ' <bala>/modules/workflow/*.bal` | 27 public decls in default module; all 27 present in `new` |
| `grep -hcE '^public ' <bala>/modules/workflow.{activity,internal,management}/*.bal` | 5 + 12 + 52 = 69 submodule publics, absent from both renders |
| `grep -nE 'configurable' <bala>/modules/workflow/config.bal` | 14 configurables, absent from both renders |
| `sed -n '195,360p' durable_agent.bal` | `public isolated class DurableAgent`, `init(*DurableAgentConfig config)`, `run(..., anydata input = ())`, `typedesc<anydata> T = <>` on the 4 result readers |
| `sed -n '130,180p' durable_agent.bal` | `DurableAgentConfig` field types incl. `(ActivityDecl\|function)[]`, `typedesc<anydata>? inputType = string`; `AgentBusyError distinct error` |
| `grep -n 'public annotation' annotations.bal` | l.24 `Workflow on function`, l.33 `Activity on function` — exact match to new render l.705/714 |
| doc-continuation lines after `// --- Types ---` (`grep -E '^[a-z\`(]'` minus declaration keywords) | 20 old, 20 new (multiset diff shows only the 6 new declarations differ) |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/workflow/0.8.3` | version 0.8.3, `deprecated: null`, ballerinaVersion 2201.13.4, modules `[workflow, workflow.activity, workflow.internal, workflow.management]` |
| `cat <bala>/compiler-plugin/compiler-plugin.json` | plugin class `io.ballerina.lib.workflow.compiler.WorkflowCompilerPlugin`, jar `workflow-compiler-plugin-0.8.3.jar` |
| `find compiler-plugin -name '*.java'` | 19 files; `WorkflowCompilerPlugin.java:44,47` register `WorkflowCodeAnalyzer` + `WorkflowCodeModifier` |
| `grep -c 'DiagnosticSeverity.ERROR/WARNING' WorkflowDiagnostic.java` | 48 ERROR, 2 WARNING |

## 10. Caveats and unverified items

- The renders were not re-generated; I audited the committed artefacts. I did not re-run the two-stage
  pipeline, so I cannot independently confirm the renders correspond to the stated `ballerina-vscode`
  commits (`eb5d81b3` / `412ba01e`) — I took that from the brief.
- I did not read the `toSyntaxString` TypeScript source on either side, so the attribution of each
  behaviour change to "extractor" vs "renderer" is inferred from the JSON delta (which is exact and
  reproducible) rather than from reading the diff of the two implementations. The inference for the
  `remote` fix is strong: the JSONs are byte-identical for `clients`, so the change must be in the
  renderer.
- The compiler-plugin behaviour is read from `v0.8.3` Java source, not from decompiling the shipped
  `workflow-compiler-plugin-0.8.3.jar`. The bala's `.bal` files match the tag exactly, so the jar
  almost certainly does too, but I did not verify the jar's bytecode.
- `ballerina/workflow` is not on the pinned-version list in `CLAUDE.md`; the version `0.8.3` and all
  paths come from `manifest44.json`, which the task states is authoritative. I did not reconcile that
  discrepancy.
- I did not attempt to compile either render. Claims that a construct is "non-compiling"
  (§5 item 1) rest on the Ballerina spec rule that a required parameter may not follow a defaultable
  one, not on a compiler run.

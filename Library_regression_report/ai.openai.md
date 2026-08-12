# ballerinax/ai.openai 1.4.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.openai` |
| Pinned version | `1.4.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.openai |
| Tag reviewed | `v1.4.0` (exact tag exists; `.bal` sources byte-identical to the bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.openai/1.4.0` |
| Old render | `370` lines |
| New render | `393` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Spec v2 is a strict improvement for this library. Nothing is removed, renamed, truncated, or
degraded. Three things change:

1. **`@display` annotations are now rendered** — 32 occurrences in `new`, 0 in `old`. That is
   *exactly* the number present in the library source (`grep -o '@display' modules/ai.openai/*.bal
   | wc -l` = 32), and the label multiset matches the source byte-for-byte.
2. **`ballerina/ai:1.13.0:Error?` → `ai:Error?`** on both `init` return types — the version/module
   qualified form is gone (2 occurrences in `old`, 0 in `new`), and the new form matches the
   `ai:` prefix already used everywhere else in the same file.
3. **A new `// --- Annotations ---` section** exposing `public annotation map<json> JsonSchema on
   type;`, which is a genuinely public symbol of the default module that `old` omitted entirely.

A whole-JSON value diff with `annotations` keys stripped produces **12 diff lines total**, all of
them the `ai:Error?` normalization. There is no other semantic change anywhere in the model.

Zero `// Unknown type:` lines on either side (this library has no error/object/other typedefs), so
the headline spec-v2 fix does not apply here.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 370 | 393 |
| Section markers (`// --- `) | 4 | 5 (`Annotations` added) |
| `// Unknown type:` | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 2 | 0 |
| `@display` occurrences | 0 | 32 |
| JSON `typeDefs` | 77 | 77 |
| JSON `clients` | 2 | 2 |
| JSON `functions` / `services` | 0 / 0 | 0 / 0 |
| JSON `annotations` | 0 | 1 |

**Declarations added (1):** `public annotation map<json> JsonSchema on type;` (render line 393).

**Declarations removed (0).** Verified: the top-level declaration sets extracted with
`grep -nE '^(public )?(isolated )?(distinct )?(client )?(type|class|enum|const|annotation|function|listener|service)'`
are identical modulo the one added annotation — 71 `const string`, `ConnectionConfig`, `ApiType`,
`ReasoningEffort`, `OPEN_AI_MODEL_NAMES`, `OPEN_AI_EMBEDDING_MODEL_NAMES`, `EmbeddingProvider`,
`ModelProvider` on both sides.

**Declarations modified (2):** `EmbeddingProvider.init` and `ModelProvider.init` — parameter-level
`@display` annotations added and return type normalized to `ai:Error?`.
Plus 19 record-field/typedef-level `@display` lines added and 1 parameter annotation on
`ModelProvider.generate`'s `td` parameter.

**README section:** `diff` of lines 1–62 of both files is empty — byte-identical, no content lost.
Full 52-line `docs/README.md` is embedded on both sides.

## 3. Correctness against library source

Every addition in `new` was checked against the bala (which is byte-identical to the `v1.4.0` tag —
`diff -rq src/ballerina <bala>/modules/ai.openai` reports only non-`.bal` files as extra).

| New render item | Source location | Verdict |
|---|---|---|
| `@display {label: "Connection Configuration"}` on `ConnectionConfig` | `types.bal:20` | correct |
| 14 field-level `@display` labels on `ConnectionConfig` fields | `types.bal:23–77` | correct, all 14 match |
| `@display {label: "OpenAI API Type"}` on `ApiType` | `types.bal:81` | correct |
| `@display {label: "Reasoning Effort"}` on `ReasoningEffort` | `types.bal:100` | correct |
| `@display {label: "OpenAI Model Names"}` on `OPEN_AI_MODEL_NAMES` | `types.bal:111` | correct |
| `@display {label: "OpenAI Embedding Model Names"}` on `OPEN_AI_EMBEDDING_MODEL_NAMES` | `types.bal:177` | correct |
| `EmbeddingProvider.init` param labels: API Key / Embedding Model Type / Service URL / Connection Configuration | `embedding-provider.bal:34–37` | correct, all 4 match |
| `ModelProvider.init` param labels: API Key / Model Type / Service URL / Maximum Tokens / Temperature / Reasoning Effort / API Type / Connection Configuration | `model-provider.bal:53–60` | correct, all 8 match |
| `@display {label: "Expected type"}` on `generate`'s `td` | `model-provider.bal:153` | correct |
| `public annotation map<json> JsonSchema on type;` | `to_json_schema.bal:32` | correct — exact text match including `map<json>` constraint and `on type` attach point |
| `returns ai:Error?` on both `init`s | `embedding-provider.bal:37`, `model-provider.bal:60` (`returns ai:Error?`) | correct — `ai` is the import prefix used by the library itself |

Formal proof that the labels are exhaustive and exact:
`diff <(grep -oh '@display {label: "[^"]*"}' <bala>/modules/ai.openai/*.bal | sort | uniq -c | sort -k2) <(grep -o '@display {label: "[^"]*"}' <new render> | sort | uniq -c | sort -k2)` → **empty**.

Client methods verified against source (unchanged between renders, both correct):
- `EmbeddingProvider.embed(ai:Chunk) returns ai:Vector|ai:SparseVector|ai:HybridVector|ai:Error` —
  source is `returns ai:Embedding|ai:Error` (`embedding-provider.bal:73`); `ai:Embedding` is
  `Vector|SparseVector|HybridVector` (`ballerina/ai:1.13.0` `rag-types.bal:37`), so the expansion is
  semantically exact.
- `EmbeddingProvider.batchEmbed(ai:Chunk[]) returns ai:Embedding[]|ai:Error` — `embedding-provider.bal:106`. Exact.
- `ModelProvider.chat(ai:ChatMessage[]|ai:ChatUserMessage, ai:ChatCompletionFunctions[] tools = [], string|() stop = ()) returns ai:ChatAssistantMessage|ai:Error` — `model-provider.bal:138-139`. Exact.
- `ModelProvider.generate(ai:Prompt, ... td) returns td|ai:Error` — `model-provider.bal:153-154`. See §5 for the `td` type erasure (shared with `old`).

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Full structural JSON key diff: `only old: []` — not a single key path present in `old` is absent
  from `new`.
- Full JSON *value* diff with `annotations` sub-objects stripped: 12 unified-diff lines, all two
  hunks being `"ballerina/ai:1.13.0:Error?"` → `"ai:Error?"`. No other value changed anywhere.
- Declaration-set diff of the two `.bal.txt` files: identical apart from the added annotation.
- README block (render lines 1–62) diffed line-by-line: identical.
- Counts held constant: `typeDefs` 77→77, `clients` 2→2, `// Unknown type:` 0→0, orphan doc lines
  (`^    # $`) 4→4, `record {|` 0→0, `compression = AUTO` 2→2.
- The precomputed diff's claim of "3 lines removed" was verified: those are the 3 modified lines
  (2 `init` signatures + 1 `generate` signature), each replaced by a superset line. No deletion.

## 5. Issues in `new` (independent of `old`)

All of the following are present **identically in `old`** — they are pre-existing renderer
limitations, not introduced by spec v2. Listed because they mislead an LLM consuming the render.

1. **`ConnectionConfig` defaults are dropped and closedness is lost.** Source (`types.bal:21`) is a
   closed record `record {| ... |}` where `httpVersion = http:HTTP_2_0`, `timeout = 60`,
   `forwarded = "disable"`, `compression = http:COMPRESSION_AUTO`, `validation = true` are
   *defaulted required* fields. The render emits an **open** `record { ... }` with every field marked
   optional (`?`) and no defaults. 14/14 fields affected.
2. **Non-compiling string default:** `string serviceUrl = https://api.openai.com/v1` — the URL is
   unquoted. Source uses the constant `DEFAULT_OPENAI_SERVICE_URL` (`model-provider.bal:25`).
3. **Wrong symbol for the compression default:** render says `http:Compression compression = AUTO`;
   source says `http:COMPRESSION_AUTO` (`types.bal:53`). `AUTO` is not a symbol in scope.
4. **Included-record parameter mangled.** Source declares `*ConnectionConfig connectionConfig`
   (rest-of-record inclusion). The render both flattens all 14 fields into positional parameters
   *and* appends a plain `ConnectionConfig connectionConfig` (no `*`) after `boolean validation`.
   The API is represented twice and the resulting signature does not compile.
5. **`typedesc` erased:** `generate`'s `td` is `typedesc<anydata> td = <>` in source
   (`model-provider.bal:153`); the render writes `anydata td = anydata`, which is both the wrong
   type and an invalid default expression.
6. **Named enum replaced by an inline string union:** `reasoningEffort` is `ReasoningEffort?` in
   source (`model-provider.bal:58`); the render expands it to
   `"xhigh"|"high"|"medium"|"low"|"minimal"|"none"|()`, losing the reference to the `ReasoningEffort`
   enum that is defined 100 lines above in the same render.
7. **Enum members lose their string values and are reversed.** Source `ReasoningEffort` is
   `NONE="none" … XHIGH="xhigh"`; render lists `XHIGH, HIGH, MEDIUM, LOW, MINIMAL, NONE` with no
   values. The values are recoverable from the 71 synthesized `const string` declarations above, but
   the association is only by name. Same for `OPEN_AI_MODEL_NAMES` (reversed) and `ApiType`.
8. **Class modifiers dropped:** source is `public isolated distinct client class ModelProvider` /
   `public distinct isolated client class EmbeddingProvider`; render emits bare `client class X`.
   `public isolated function init` becomes `function init`; `isolated remote function` becomes
   `remote function`.
9. **Doc parameter descriptions dropped.** Every method keeps its summary line but the `+ param -`
   and `+ return -` lines are stripped, leaving 4 orphan `# ` lines (identical count both sides).
10. **Enum-member doc comments dropped** — e.g. `ApiType.CHAT_COMPLETIONS`'s
    `# Use the OpenAI Chat Completions API (`/chat/completions`)` survives only as a comment above
    the synthesized `const string CHAT_COMPLETIONS`, not on the enum member.

## 6. Coverage gaps vs. the library

The package exports exactly one module, `ai.openai`, and it is the default module
(`package.json: "export": ["ai.openai"]`; `modules/` contains only `ai.openai`). **There is no
submodule-only API**, so the shared `getDefaultModule()` limitation costs nothing here.

Public symbols of the default module (from `grep -nE '^\s*public' modules/ai.openai/*.bal`):

| Symbol | in `old` | in `new` |
|---|---|---|
| `ModelProvider` (class) | yes | yes |
| `EmbeddingProvider` (class) | yes | yes |
| `ConnectionConfig` | yes | yes |
| `ApiType` | yes | yes |
| `ReasoningEffort` | yes | yes |
| `OPEN_AI_MODEL_NAMES` | yes | yes |
| `OPEN_AI_EMBEDDING_MODEL_NAMES` | yes | yes |
| `annotation JsonSchema` | **NO** | yes |

So `old` had one true coverage gap; `new` has **zero missing public declarations**.

One remaining gap shared by both renders: the **type inclusions are not rendered**. Source declares
`*ai:ModelProvider;` (`model-provider.bal:31`) and `*ai:EmbeddingProvider;`
(`embedding-provider.bal:22`). Neither render shows this, so a consumer cannot tell from the render
that `openai:ModelProvider` is assignable to `ai:ModelProvider` — which is the single most common way
this library is used, and is in fact what the render's own README snippet does at line 49
(`final ai:ModelProvider openAiModel = check new openai:ModelProvider(...)`). Counted as 1 coverage gap.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` registers `io.ballerina.lib.ai.openai.AiOpenAICompilerPlugin`
with two jars (`ai.openai-compiler-plugin-1.4.0.jar`, `ballerina-to-openapi-2.3.0.jar`).

`AiOpenAICompilerPlugin.java:33` registers a single `AiOpenAICodeModifier` — a **code modifier**, not
a validator. `GenerateMethodModificationTask` walks call sites of `ModelProvider.generate`, derives
an OpenAPI schema for the inferred `td` typedesc via `OpenAPISchema2JsonSchema`
(`GenerateMethodModificationTask.java:287-293`), and injects it as a `@ai:JsonSchema` annotation on
the corresponding type definition (`SCHEMA_ANNOTATION_IDENTIFIER = "JsonSchema"`, line 398). At
runtime `to_json_schema.bal:34-36` reads `expectedResponseTypedesc.@ai:JsonSchema` to build the
response schema. The plugin emits no diagnostics and contributes no code actions.

**Relevance to the render:** the annotation the plugin writes is precisely
`public annotation map<json> JsonSchema on type;` — the one declaration `new` adds and `old` lacked.
So spec v2 closes the gap that mattered most for this specific plugin. Nothing else the plugin
implies is missing from `new`.

## 8. Other considerations

- Version is stable (`1.4.0`, ≥1.0). Central reports `deprecated: null`, empty `deprecateMessage`.
  `pullCount: 56`, created 2026-08-04.
- `graalvmCompatible: true`, `ballerina_version: 2201.12.0`, `platform: java21`.
- Size impact of spec v2 here is trivial: +23 lines / +6.2%. Token cost of the `@display` metadata is
  small and it is genuinely useful (these are the labels the low-code editor shows).
- GitHub `v1.4.0` and the published bala agree exactly on all 7 `.bal` files, so there is no
  source/artifact drift to worry about for this library.
- The render is not compilable Ballerina (see §5 items 2–5), but that is uniformly true of both
  sides and is a property of the renderer, not of this library.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/new .bal.txt` | 370 / 393 |
| `git ls-remote --tags <repo>` | `v1.4.0` present (`2d19f4d4…`, peeled `cd639e21…`) |
| `git clone --depth 1 --branch v1.4.0` | success |
| `diff -rq src/ballerina <bala>/modules/ai.openai` | only `Ballerina.toml`, `CompilerPlugin.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png` extra; all `.bal` identical |
| `ls <bala>/java21/modules` | `ai.openai` only — no submodules |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers / 5 markers (`Annotations` added at 391) |
| `grep -cE 'org/mod:x.y.z:'` old / new | 2 / 0 |
| `grep -o '@display' \| wc -l` old / new / source | 0 / 32 / 32 |
| `diff` of sorted+counted `@display {label:"…"}` source vs new | empty (identical with multiplicity) |
| JSON key-path set diff | `only old: []`; `only new:` 13 paths, all under `annotations` |
| JSON value diff with `annotations` stripped | 12 lines, 2 hunks, both `ballerina/ai:1.13.0:Error?` → `ai:Error?` |
| JSON section counts | typeDefs 77→77, clients 2→2, functions 0→0, services 0→0, annotations 0→1 |
| `diff <(sed -n 1,62p old) <(sed -n 1,62p new)` | identical (README block) |
| `wc -l <bala>/docs/README.md` | 52 |
| Declaration grep, old vs new | identical set + `public annotation map<json> JsonSchema on type;` |
| `grep -c '^    # $'` old / new | 4 / 4 |
| `grep -c 'compression = AUTO'` old / new | 2 / 2 |
| `grep -nE '^\s*public' <bala>/modules/ai.openai/*.bal` | 8 public symbols enumerated in §6 |
| `types.bal:20,81,100,111,177` | `@display` on ConnectionConfig / ApiType / ReasoningEffort / OPEN_AI_MODEL_NAMES / OPEN_AI_EMBEDDING_MODEL_NAMES |
| `embedding-provider.bal:34-37` | 4 `@display` param labels on `init` |
| `model-provider.bal:53-60` | 8 `@display` param labels on `init` |
| `model-provider.bal:153` | `generate(ai:Prompt prompt, @display {label: "Expected type"} typedesc<anydata> td = <>)` |
| `to_json_schema.bal:32` | `public annotation map<json> JsonSchema on type;` |
| `ballerina/ai/1.13.0 rag-types.bal:37` | `public type Embedding Vector\|SparseVector\|HybridVector;` |
| `<bala>/compiler-plugin/compiler-plugin.json` | `plugin_class: io.ballerina.lib.ai.openai.AiOpenAICompilerPlugin` |
| `AiOpenAICompilerPlugin.java:33` | `context.addCodeModifier(new AiOpenAICodeModifier())` — modifier only, no analysis task |
| `GenerateMethodModificationTask.java:398` | `SCHEMA_ANNOTATION_IDENTIFIER = "JsonSchema"` |
| `curl api.central.ballerina.io/.../ballerinax/ai.openai/1.4.0` | `deprecated: null`, `modules: [ai.openai]`, `pullCount: 56` |
| `<bala>/package.json` | `export: ["ai.openai"]`, `graalvmCompatible: true`, `ballerina_version: 2201.12.0` |

## 10. Caveats and unverified items

- I did not decompile `ai.openai-compiler-plugin-1.4.0.jar`; the plugin analysis is based on the
  Java source at tag `v1.4.0`, which for the `.bal` files is provably identical to the bala. The jar
  itself is assumed to be built from that source — **unverified**.
- The renders were not fed to `bal build`, so "non-compiling" claims in §5 are based on reading the
  syntax (unquoted URL literal, `= anydata` as a default, undefined `AUTO`, `*`-less included-record
  param), not on a compiler run.
- I did not re-run the two-stage pipeline; the audit compares the supplied artifacts as given.
- The `ai:Embedding` union expansion was confirmed against the locally cached
  `ballerina/ai/1.13.0` bala. I did not confirm that 1.13.0 is the version the extractor resolved on
  *both* sides — but `old` explicitly prints `ballerina/ai:1.13.0:Error?`, and `new` prints the
  unqualified `ai:Error?`, so `new`'s resolved version is inferred, not directly observed.

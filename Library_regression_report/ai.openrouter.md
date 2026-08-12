# ballerinax/ai.openrouter 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.openrouter` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.openrouter |
| Tag reviewed | `v1.0.2` (annotated → commit `e4fdfa2439d5d7c853c74215d93a96be74e1ff6b`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.openrouter/1.0.2/java21` |
| Old render | `148` lines |
| New render | `165` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The `new` render is a strict superset of `old`. A path-level diff of the two JSON models shows
**0 paths present only in `old`**, **64 paths present only in `new`**, and **2 changed values**.
All 64 additions are `@display` annotation captures (name + value pairs, 32 annotations), every one
of which is verified present verbatim in the published source. Both changed values are a fix: the
non-compiling version-qualified return type `ballerina/ai:1.13.0:Error?` on both `init` methods
becomes the correct `ai:Error?`.

Nothing was dropped, truncated or mangled. `// Unknown type:` count is 0 on both sides (this library
has no `Error`/object/`Other` type defs to degrade), so spec v2's headline improvement does not apply
here; the gain is annotations plus the type-reference fix.

Coverage of the default module is complete: the module exports exactly three public symbols and all
three are rendered. Several rendering inaccuracies remain, but every one of them except a single
provenance-note omission is present identically in `old` and is therefore not a regression.

## 2. Change inventory

Line counts (`wc -l`): old 148, new 165. Textual diff: **20 lines added, 3 lines removed, 4 hunks**
(3 "removed" lines are the two `init` lines and the `generate` line, each replaced by an annotated
variant — no declaration is lost).

Declaration-level inventory — **added 0, removed 0**. Both renders contain exactly:

| Kind | Count | Names |
|---|---|---|
| Type (record) | 1 | `ConnectionConfig` (14 fields, identical in both) |
| Client class | 2 | `EmbeddingProvider`, `ModelProvider` |
| Client method | 6 | `EmbeddingProvider.init/embed/batchEmbed`, `ModelProvider.init/chat/generate` |
| Module-level function | 0 | — |
| Enum / const / annotation / service / listener | 0 | — |
| README section | 1 | byte-identical (`readme` string equal in both JSONs) |
| `// --- ` section markers | 4 → 4 | README, END README, Types, Client |

Modifications, exhaustively (this is the whole diff):

1. **`@display` annotations added — 32 occurrences on 20 lines in `new`, 0 in `old`.**
   - 1 on the `ConnectionConfig` type def (`{label: "Connection Configuration"}`)
   - 14 on `ConnectionConfig` fields (one per field)
   - 2 on the client classes (`OpenRouter Embedding Provider`, `OpenRouter Model Provider`)
   - 6 inline on `EmbeddingProvider.init` params (`apiKey`, `modelType`, `serviceUrl`, `siteUrl`,
     `siteName`, `connectionConfig`)
   - 8 inline on `ModelProvider.init` params (the above plus `maxTokens`, `temperature`)
   - 1 inline on `ModelProvider.generate` param `td` (`{label: "Expected type"}`)
2. **Return-type fix, 2 occurrences.** `EmbeddingProvider.init` and `ModelProvider.init`:
   `returns ballerina/ai:1.13.0:Error?` → `returns ai:Error?`. Version/module-qualified refs: 2 in
   `old`, 0 in `new`.

No parameter, default value, doc line, type or method text differs otherwise.

## 3. Correctness against library source

GitHub `v1.0.2` and the bala are byte-identical for all five module sources (`diff -q`:
`types.bal`, `model-provider.bal`, `embedding-provider.bal`, `provider_utils.bal`,
`to_json_schema.bal` all IDENTICAL), so there is no source-of-truth conflict.

Every `@display` label added by `new` was checked against the source:

| Render location | Source | Verified |
|---|---|---|
| `type ConnectionConfig` label `Connection Configuration` | `modules/ai.openrouter/types.bal:20` | yes |
| 14 field labels (`HTTP Version` … `Payload Validation`) | `types.bal:24,28,32,36,40,44,48,52,56,60,64,68,72,76` | yes, in file order, one per field |
| `client class EmbeddingProvider` label `OpenRouter Embedding Provider` | `embedding-provider.bal:24-26` | yes |
| `client class ModelProvider` label `OpenRouter Model Provider` | `model-provider.bal:28-30` | yes |
| `EmbeddingProvider.init` param labels | `embedding-provider.bal:42-47` (`API Key`, `Model Type`, `Service URL`, `Site URL`, `Site Name`, `Connection Configuration`) | yes, all 6 |
| `ModelProvider.init` param labels | `model-provider.bal:50-57` (adds `Maximum Tokens`, `Temperature`) | yes, all 8 |
| `generate` param `td` label `Expected type` | `model-provider.bal:176` | yes |

Return-type fix: `embedding-provider.bal:47` and `model-provider.bal:57` both declare
`... *ConnectionConfig connectionConfig) returns ai:Error?`. `new` matches the source exactly;
`old`'s `ballerina/ai:1.13.0:Error?` is not valid Ballerina syntax.

Other signatures (unchanged between renders) checked against source:
- `chat(ai:ChatMessage[]|ai:ChatUserMessage messages, ai:ChatCompletionFunctions[] tools = [], string|() stop = ())`
  → `model-provider.bal:84-85` declares `string? stop = ()`; `string|()` is the same type. Correct.
- `batchEmbed(ai:Chunk[] chunks) returns ai:Embedding[]|ai:Error` → `embedding-provider.bal:126`. Exact match.
- `embed(ai:Chunk chunk) returns ai:Vector|ai:SparseVector|ai:HybridVector|ai:Error` →
  `embedding-provider.bal:71` declares `ai:Embedding|ai:Error`. `ballerina/ai` 1.13.0
  `rag-types.bal:37` defines `public type Embedding Vector|SparseVector|HybridVector`, so the render
  is the expanded but semantically identical form. Not an error, but the alias name is lost (both sides).
- `ConnectionConfig` field list and optionality: 14 optional fields in the render, 14 `?`-suffixed
  fields in `types.bal:21-78`. Match.

No invented symbol appears in `new`.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Structural JSON diff over every leaf path: `ONLY OLD = 0`. Nothing that existed in the old model is
  absent from the new model.
- `CHANGED = 2`, and both changes move the value *toward* the source (`ai:Error?`), not away.
- README string and `description` string compare equal between the two JSONs (`==` → `True`).
- Section markers 4 → 4; declaration counts identical (1 type, 2 clients, 6 client methods, 0 functions,
  0 enums/consts/annotations/services/listeners on both sides).
- No doc line, parameter, default value or return type is removed anywhere in the textual diff — the
  only removed lines are three that are re-emitted with annotations added.

## 5. Issues in `new` (independent of `old`)

Seven inaccuracies remain in the `new` render. Items 1–6 are present **identically in `old`** (shared
pipeline limitations, listed here because the brief asks for issues in `new` regardless of `old`);
item 7 is specific to `new`.

1. **Unquoted string default — non-compiling.** Both `init` lines render
   `string serviceUrl = https://openrouter.ai/api/v1`. Source is
   `serviceUrl = DEFAULT_OPENROUTER_SERVICE_URL` where `model-provider.bal:22` defines
   `const DEFAULT_OPENROUTER_SERVICE_URL = "https://openrouter.ai/api/v1"`. The quotes are stripped,
   yielding a syntax error if copied. (new:138, new:154; old:122, old:137)
2. **`typedesc` collapsed to `anydata`.** `generate` renders `anydata td = anydata`; source
   (`model-provider.bal:176`) is `typedesc<anydata> td = <>`. Both the `typedesc` wrapper and the
   infer-default `<>` are lost, and `= anydata` is not a valid default expression. An LLM would write
   a wrong call site. (new:164, old:147)
3. **Included-record parameter double-counted.** Source `init` takes `*ConnectionConfig connectionConfig`
   (`embedding-provider.bal:47`, `model-provider.bal:57`). The render expands all 14 `ConnectionConfig`
   fields as individual defaulted params **and** appends a required, undefaulted
   `ConnectionConfig connectionConfig` param after them. That is both duplicative and non-compiling
   (required param after defaulted params), and the `*` include marker is gone.
4. **Record openness lost.** `type ConnectionConfig record {` — source `types.bal:21` is
   `public type ConnectionConfig record {|` (closed). The render implies an open record.
5. **Qualifiers and type inclusions dropped.** Source declares
   `public isolated distinct client class` with `*ai:EmbeddingProvider` / `*ai:ModelProvider`
   inclusions (`embedding-provider.bal:27-28`, `model-provider.bal:31-32`); the render emits bare
   `client class` with no inclusion. `public isolated function init` → `function init`;
   `isolated remote function` → `remote function`. The fact that these classes *implement the
   `ballerina/ai` provider abstractions* — the single most important fact about this library — is
   absent from both renders.
6. **Parameter-level docs dropped.** Source carries 27 `# + <param> - ...` doc lines
   (16 in `model-provider.bal`, 11 in `embedding-provider.bal`); the renders contain **0**, leaving
   dangling empty `# ` lines after each method description (new:141,145,157,163).
7. **Provenance note omits `ai:Error` on `init` (new only).** With `old`'s fully-qualified
   `ballerina/ai:1.13.0:Error?` replaced by the bare `ai:Error?`, the trailing
   `// Special Agent Note:` on both `init` lines still lists only the `ballerina/http` types, so the
   `ai:` prefix on `init` has no declared origin on that line. The other four methods do carry
   `Error FROM ballerina/ai package` notes, and the render's header has no `import ballerina/ai`.
   Very minor and still a net improvement over the non-compiling old form.

## 6. Coverage gaps vs. the library

**0 gaps.**

The bala contains exactly one module (`modules/ai.openrouter` — the default module), so the
`getDefaultModule()`-only extraction limitation is inert for this library; there is no submodule API
to miss.

Complete list of `public` symbols in the default module (`grep -nE 'public (type|class|function|const|enum|annotation)'` over all five `.bal` files):

| Symbol | Kind | In renders |
|---|---|---|
| `ConnectionConfig` | public type | yes (both) |
| `EmbeddingProvider` | public isolated distinct client class | yes (both) |
| `ModelProvider` | public isolated distinct client class | yes (both) |

No public module-level functions, constants, enums, annotations, services or listeners exist. The
remaining declarations (`JsonSchema`, `JsonArraySchema`, `ResponseSchema`, `DocumentContentPart`,
`DEFAULT_OPENROUTER_SERVICE_URL`, `DEFAULT_MAX_TOKEN_COUNT`, `JSON_CONVERSION_ERROR`, `CONVERSION_ERROR`,
`ERROR_MESSAGE`, `RESULT`, `GET_RESULTS_TOOL`, `FUNCTION`, `NO_RELEVANT_RESPONSE_FROM_THE_LLM`) are
module-private and correctly excluded from both renders.

## 7. Compiler plugin

Present: `compiler-plugin/compiler-plugin.json` declares
`plugin_class = io.ballerina.lib.ai.openrouter.compiler.AiOpenRouterCompilerPlugin` with deps
`ai.openrouter-compiler-plugin-1.0.2.jar` and `ballerina-to-openapi-2.3.0.jar`.

What it contributes (`AiOpenRouterCompilerPlugin.java:35`): a single `context.addCodeModifier(new AiOpenRouterCodeModifier())`.
No `CodeAnalyzer`, no code actions, no diagnostics are registered. `GenerateMethodModificationTask`
(`GenerateMethodModificationTask.java:81`, inner `GenerateMethodJsonSchemaGenerator:211`,
`TypeDefinitionModifier:395`) rewrites `generate` call sites at compile time to inject a generated JSON
schema for the inferred `td` type.

Nothing the plugin implies is missing from the render beyond what section 5 item 2 already covers: the
render's loss of `typedesc<anydata> td = <>` erases exactly the inference point the plugin operates on,
though `generate`'s doc comment does mention `@ai:JsonSchema` (that annotation is owned by
`ballerina/ai`, not by this package, so its absence from this render's `annotations` list — 0 in both
JSONs — is correct).

## 8. Other considerations

- **Version pinning.** Both sides render `ballerinax/ai.openrouter` and the bala inspected is exactly
  `1.0.2`. No version drift observed; the only version string anywhere in either render was the
  `ballerina/ai:1.13.0:` qualifier in `old`, now removed.
- **Pre-1.0 / stability.** The package is at `1.0.2` (stable). `Ballerina.toml` at the tag pins
  `distribution = "2201.12.6"`. No deprecation markers found in the sources or the renders.
- **Size / token impact.** JSON grew 34,345 → 39,577 bytes (+15.2%); render grew 148 → 165 lines
  (+11.5%). Small in absolute terms. The added `@display` labels are UI metadata; they add modest
  token cost and are of limited value to an LLM consumer, but they do carry human-readable names for
  every config field, and they are faithful to the source.
- **README fidelity.** The `readme` field equals the bala `docs/README.md` exactly (diff shows only a
  trailing-newline difference at line 71/70), and is byte-identical between old and new.
- **Doc quality.** Class and method descriptions survive intact; only per-parameter docs are lost
  (section 5 item 6), on both sides equally.
- **Encoding.** No mojibake or non-UTF-8 artefacts observed in either render.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 148 / 165 |
| `git ls-remote --tags <repo>` | tags `v1.0.0`, `v1.0.1`, `v1.0.2`; exact match `v1.0.2` → `e4fdfa2439d5…` |
| `git clone --depth 1 --branch v1.0.2 <repo> src` | success; `src/ballerina/*.bal`, `src/compiler-plugin/` present |
| `ls <bala>/java21/modules` | single module `ai.openrouter` (default module only) |
| `diff -q <bala>/modules/ai.openrouter/*.bal src/ballerina/*.bal` | all 5 files IDENTICAL |
| `grep -c '^// Unknown type:' old new` | 0 / 0 |
| `diff -u old new \| grep -c '^+'` | 21 (incl. `+++` header) → 20 added lines; 3 removed lines |
| Python leaf-path diff of the two JSONs | ONLY OLD 0 · ONLY NEW 64 · CHANGED 2 |
| Changed paths | `/clients/[0]/functions/[0]/return/type/name` and `/clients/[1]/…`: `ballerina/ai:1.13.0:Error?` → `ai:Error?` |
| Added paths | 64 = 32 `annotations[].name`/`.value` pairs, all `display` |
| `grep -o '@display' new \| wc -l` / same on old | 32 / 0 |
| `json['readme'] == `, `json['description'] ==` | True, True |
| `diff <(new json readme) <bala>/docs/README.md` | only trailing newline (`71d70`) |
| `grep -nE 'public (type\|class\|function\|const\|enum\|annotation)' <bala>/modules/ai.openrouter/*.bal` | 3 public symbols: `ConnectionConfig` (types.bal:21), `EmbeddingProvider` (embedding-provider.bal:27), `ModelProvider` (model-provider.bal:31) |
| `types.bal:20-77` `@display` labels | 1 type-level + 14 field-level, match render lines 85–128 |
| `embedding-provider.bal:42-47`, `model-provider.bal:50-57,176` | init/generate param `@display` labels match render lines 138, 154, 164 |
| `embedding-provider.bal:47`, `model-provider.bal:57` | `returns ai:Error?` — confirms new is correct |
| `model-provider.bal:84-85` | `chat(... string? stop = ()) returns ai:ChatAssistantMessage\|ai:Error` — matches both renders |
| `embedding-provider.bal:71,126` | `embed → ai:Embedding\|ai:Error`, `batchEmbed → ai:Embedding[]\|ai:Error` |
| `ballerina/ai/1.13.0 rag-types.bal:37` | `public type Embedding Vector\|SparseVector\|HybridVector` — explains render's expanded `embed` return |
| `model-provider.bal:22` | `const DEFAULT_OPENROUTER_SERVICE_URL = "https://openrouter.ai/api/v1"` — render drops the quotes |
| `model-provider.bal:176` | `typedesc<anydata> td = <>` vs render `anydata td = anydata` |
| `grep -c '# + ' <bala>/modules/ai.openrouter/{model,embedding}-provider.bal` | 16 + 11 = 27 param doc lines in source; `grep -c '^ *# + ' old new` → 0 / 0 |
| `cat <bala>/compiler-plugin/compiler-plugin.json` | `AiOpenRouterCompilerPlugin`, 2 dep jars |
| `grep -n 'addCodeModifier\|addCodeAnalyzer' src/compiler-plugin/**/AiOpenRouterCompilerPlugin.java` | line 35, code modifier only; no analyzer/diagnostics |
| `wc -c old.json new.json` | 34,345 / 39,577 bytes |
| `OLD_AND_NEW_DIFFS/ai.openrouter_diff.md` | claims 148/165 lines, +20/−3, 4 hunks, 0 declarations added/removed, 2→0 version-qualified refs — all independently reproduced above |

## 10. Caveats and unverified items

- **Neither render was compiled.** The syntax problems listed in section 5 (unquoted URL default,
  `anydata td = anydata`, required param after defaulted params) are identified by reading against the
  Ballerina grammar, not by running `bal build` on the render. Both renders are prose-style API digests,
  not intended to be compiled, so this is a fidelity observation rather than a verified build failure.
- **`ballerina/ai` 1.13.0 was read from the local bala** at
  `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/ai/1.13.0` to resolve
  `ai:Embedding`. Only that one type alias was checked; the other `ai:` types referenced by the render
  (`Chunk`, `ChatMessage`, `ChatUserMessage`, `ChatCompletionFunctions`, `ChatAssistantMessage`,
  `Prompt`, `Error`) were not individually resolved, since they are unchanged between old and new and
  outside this library.
- **Ballerina Central metadata was not re-queried** over the network; the module list was taken from the
  bala's `modules/` directory, which the brief designates as authoritative for what the extractor saw.
- The `@display` annotation *values* are rendered as the raw mapping-constructor text
  (`{label: "…"}`); whether the downstream Copilot consumer parses that form was not verified — it is
  outside the scope of comparing the two renders.

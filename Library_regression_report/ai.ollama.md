# ballerinax/ai.ollama 1.2.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.ollama` |
| Pinned version | `1.2.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.ollama |
| Tag reviewed | `v1.2.4` |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.ollama/1.2.4/java21` |
| Old render | `155` lines |
| New render | `197` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` for this library. Nothing was removed, truncated, or made less
accurate. Three things changed:

1. All 34 `@display` annotations and all 9 `@jsondata:Name` annotations present in the library
   source are now rendered (`old` rendered zero annotations). The rendered labels/values match the
   source byte-for-byte.
2. The version-qualified return type `ballerina/ai:1.13.0:Error?` on `ModelProvider.init` became
   `ai:Error?`, which is what the source actually writes (`provider.bal:47`).
3. A new `// --- Annotations ---` section surfaces `public annotation map<json> JsonSchema on type;`
   — a genuine public export of the default module (`to_json_schema.bal:32`) that `old` omitted
   entirely.

Both renders share a set of pre-existing fidelity problems (dropped record-field defaults, dropped
`public`/`isolated`, flattened included-record parameters, an unquoted URL default, `typedesc<anydata>`
rendered as `anydata`). These are identical on both sides and are therefore **not** regressions, but
they are listed in §5 because they are still wrong in `new`.

## 2. Change inventory

Line counts (`wc -l`): old **155**, new **197**.
Diff accounting (`diff old new | grep -c '^<' / '^>'`): **2 lines removed, 44 lines added**.
The 2 removed lines are the `init` and `generate` signature lines, each replaced by an annotated
version of the same signature — no declaration lost.

| Kind | old | new | Delta |
|---|---|---|---|
| Type definitions (`type … record`) | 2 (`ConnectionConfig`, `OllamaModelParameters`) | 2 (same) | 0 |
| Client classes | 1 (`ModelProvider`) | 1 (same) | 0 |
| Client methods | 3 (`init`, `chat`, `generate`) | 3 (same) | 0 |
| Module-level functions | 0 | 0 | 0 |
| Services / listeners | 0 | 0 | 0 |
| Enums / constants | 0 | 0 | 0 |
| **Annotations** | **0** | **1** (`JsonSchema`) | **+1** |
| `// --- section ---` markers | 4 | 5 (`Annotations` added) | +1 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 | −1 |
| `@display` occurrences | 0 | 34 | +34 |
| `@jsondata:Name` occurrences | 0 | 9 | +9 |

JSON-level: the key-path set of `new/ballerinax_ai.ollama.json` is a strict superset of `old`'s
(`only in old: []`). New key paths are `/annotations[]/*`, `/typeDefs[]/annotations*`,
`/typeDefs[]/fields[]/annotations*`, `/clients[]/annotations*`,
`/clients[]/functions[]/parameters[]/annotations*`. `init` has 30 parameters in both, with identical
names, types and defaults; the only per-parameter difference is the added `annotations` array.

README payload is byte-identical between `old`, `new`, and `docs/README.md` in the bala (48 lines).

## 3. Correctness against library source

The bala's `modules/ai.ollama/*.bal` are byte-identical to the upstream `v1.2.4` tag's
`ballerina/*.bal` (`diff -q` on all four files → identical), so GitHub and the bala agree.

Everything `new` adds was verified against the source:

- **`@display` labels** — `diff <(grep -ho 'label: "[^"]*"' bala/*.bal | sort) <(same on new render)`
  → **identical**. 34 occurrences in source, 34 in the render.
  Spot checks: `ConnectionConfig` type label `types.bal:21`; the 14 field labels `types.bal:25,29,33,37,41,45,49,53,57,61,65,69,73,77`; `OllamaModelParameters` type label `types.bal:84`; class label `provider.bal:27-29`; `init` param labels `provider.bal:44,45,46,47`; `generate` `td` label `provider.bal:124`.
- **`@jsondata:Name` values** — same sorted-set diff → **identical**. 9 in source, 9 in the render
  (`mirostat_eta`, `mirostat_tau`, `num_ctx`, `repeat_last_n`, `repeat_penalty`, `num_predict`,
  `top_k`, `top_p`, `min_p`; `types.bal:95,101,106,113,120,136,143,150,156`). Correctly **not**
  emitted on `mirostat`, `temperature`, `seed`, which carry no `@jsondata:Name` in the source.
- **`public annotation map<json> JsonSchema on type;`** (new render line 197) is character-for-character
  the source declaration at `to_json_schema.bal:32`.
- **`returns ai:Error?`** on `init` (new render line 183) matches `provider.bal:47`; `old`'s
  `ballerina/ai:1.13.0:Error?` did not.
- **`chat`** signature unchanged and correct vs `provider.bal:65-66` (`string|() stop = ()` is an
  accurate spelling of `string? stop = ()`).
- **`generate`** return `td|ai:Error` matches `provider.bal:124-125`.

## 4. Regressions

**None found.**

What was checked to conclude that:
- `diff old new | grep '^<'` returns exactly 2 lines, both of which are the pre-annotation forms of
  `init` and `generate`; the replacing `>` lines contain the identical text plus `@display` prefixes
  (verified by eye on both full signature strings).
- Declaration sets extracted from both JSONs are equal for `typeDefs`, `clients`, client
  `functions`, `functions`, and `services`; only `annotations` grew (0 → 1).
- JSON key-path set: `only in old: []` — no field of the model was dropped.
- `init` parameter list compared element-by-element ignoring `annotations`: **zero differences**,
  order preserved, 30 params on both sides.
- README text identical across old/new/bala.
- No new `// Unknown type:` lines (0 on both sides), no lost section markers (old's 4 markers all
  present in new).

## 5. Issues in `new` (independent of `old`)

All of the following are also present in `old` unless marked *new-only*. They are inaccuracies of the
render relative to the library source, not regressions.

1. **Record field defaults dropped and required fields turned optional.** Source
   `ConnectionConfig` (`types.bal:22-79`) is a closed record whose fields carry defaults, e.g.
   `http:HttpVersion httpVersion = http:HTTP_2_0;` (`types.bal:26`), `decimal timeout = 60;` (`:38`),
   `boolean validation = true;` (`:78`). The render emits `http:HttpVersion httpVersion?;`
   (new line 67), `decimal timeout?;`, `boolean validation?;`. Same for all 12 fields of
   `OllamaModelParameters` (`types.bal:85-159`), e.g. `0|1|2 mirostat = 0;` → `0|1|2 mirostat?;`
   (new line 119). An LLM reading this cannot see any default value.
2. **Closed records rendered as open.** Both types are `record {| … |}` in source; the render emits
   `record { … }` (new lines 64, 113).
3. **`public` and `isolated` qualifiers dropped.** Source has `public type ConnectionConfig`,
   `public type OllamaModelParameters`, `public isolated client class ModelProvider`
   (`types.bal:22,85`, `provider.bal:30`). Render emits `type …` / `client class …`.
4. **`*ai:ModelProvider` type inclusion not rendered.** `provider.bal:31` declares that
   `ModelProvider` includes the `ai:ModelProvider` object type. Nothing in either render conveys that
   this class is usable as an `ai:ModelProvider`, which is exactly how the README example uses it.
5. **Included-record parameters flattened *and* duplicated.** Source `init` has 4 parameters:
   `modelType`, `serviceUrl`, `*OllamaModelParameters modleParameters`, `*ConnectionConfig connectionConfig`
   (`provider.bal:44-47`). The render emits 30 parameters: the 12 `OllamaModelParameters` fields,
   then a bare `OllamaModelParameters modleParameters` with no `*` and no default, then the 14
   `ConnectionConfig` fields, then a bare `ConnectionConfig connectionConfig`. The result is not
   valid Ballerina (required params follow defaulted ones) and misrepresents the call shape.
6. **Unquoted string default.** `string serviceUrl = http://localhost:11434` (new line 183). The
   source default is the constant `DEFAULT_OLLAMA_SERVICE_URL = "http://localhost:11434"`
   (`provider.bal:23,45`). The render inlines the value without quotes — non-compiling, and an LLM
   copying it produces a syntax error.
7. **`http:Compression compression = AUTO`** (new line 183). Source default is
   `http:COMPRESSION_AUTO` (`types.bal:54`). `AUTO` is an undefined symbol in the rendered context.
8. **`generate`'s `td` parameter has the wrong type.** Source:
   `typedesc<anydata> td = <>` (`provider.bal:124`). Render: `anydata td = anydata` (new line 192).
   Both the `typedesc<…>` wrapper and the inferred-default `<>` are lost, and the fabricated default
   `anydata` is not a value.
9. **Multi-line doc comments lose the `#` on continuation lines.** e.g. new lines 114-117 render as
   `    # Enable Mirostat sampling…` followed by three bare markdown lines at column 0
   (`- \`0\` = disabled`) inside the record body — non-compiling text.
10. *(new-only, cosmetic)* **`jsondata:` prefix used without an import.** The render's import block is
    only `import ballerinax/ai.ollama;` (line 5); `@jsondata:Name` (new lines 122, 126, …) joins the
    already-unimported `http:` and `ai:` prefixes. Consistent with existing renderer behaviour, but it
    is a new unresolved prefix introduced by `new`.

## 6. Coverage gaps vs. the library

Default module `ai.ollama` is the **only** module (`bala/…/modules/` contains just `ai.ollama`;
`package.json` `"export": ["ai.ollama"]`; Central lists one module). **There is no submodule-only API,
so the shared `getDefaultModule()` limitation does not bite this library.**

Complete list of `public` symbols in the default module (`grep -n '^public\|^\s*public ' bala/*.bal`):

| Public symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `ConnectionConfig` | `types.bal:22` | yes | yes |
| `OllamaModelParameters` | `types.bal:85` | yes | yes |
| `ModelProvider` (client class) | `provider.bal:30` | yes | yes |
| `annotation JsonSchema` | `to_json_schema.bal:32` | **no** | yes |

**Coverage gaps in `new`: 0.** `old` had 1 (the annotation).

Non-public module members (`OllamaResponse`, `OllamaMessage`, `OllamaToolCall`, `OllamaFunction`,
`JsonSchema`/`JsonArraySchema` records, `ResponseSchema`, `ChatContent`, all module-level
`isolated function`s, all `const`s) are correctly absent from both renders.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json`: `plugin_id: ai-ollama-compiler-plugin`,
`plugin_class: io.ballerina.lib.ai.ollama.AiOllamaCompilerPlugin`, with
`ai.ollama-compiler-plugin-1.2.4.jar` and `ballerina-to-openapi-2.3.0.jar` as dependencies.

Source (`compiler-plugin/src/main/java/io/ballerina/lib/ai/ollama/`, 599 lines across 4 classes):

- `AiOllamaCompilerPlugin` registers `AiOllamaCodeModifier` (a `CodeModifier`, not a validator) —
  so the plugin contributes **no diagnostics and no code actions**.
- `AiOllamaCodeModifier` wires a `TypeMapperImplInitializer` (`MODULE_PART` syntax analysis) plus a
  `GenerateMethodModificationTask` source modifier.
- `GenerateMethodModificationTask` (481 lines) finds calls to `ModelProvider.generate`, derives the
  expected return type's OpenAPI schema, converts it with `OpenAPISchema2JsonSchema`, and attaches
  an `ai:JsonSchema` annotation to the call — injecting `import ballerina/ai;` if not already
  present (`:166`, `:410`, `:466-467`).

Notable: the annotation the plugin attaches is `ballerina/ai`'s `JsonSchema`
(`AI_MODULE_NAME = "ai"`, `BALLERINA_ORG_NAME = "ballerina"`, lines 81-82), and the runtime lookup in
`to_json_schema.bal:35` reads `expectedResponseTypedesc.@ai:JsonSchema`. The module's *own*
`ai.ollama:JsonSchema` annotation that `new` now renders is therefore not referenced by the plugin or
by module code — it is a public but effectively vestigial export. Rendering it is factually correct;
its practical value to an LLM is low, and there is a mild risk the model writes
`@ollama:JsonSchema` where `@ai:JsonSchema` is meant.

Nothing else the plugin implies is missing from the render: it generates no public types or
functions, only rewrites user call sites.

## 8. Other considerations

- Version is stable (1.2.4, `>=1.0.0`); Central reports `deprecated: null`, `deprecateMessage: ""`,
  pull count 2031. Built with `ballerina_version: 2201.12.0`, `graalvmCompatible: true`.
- Size: the render grew 155 → 197 lines (+27%) purely from annotations. Token cost is small in
  absolute terms and the `@display` labels are useful UI/intent hints. `@jsondata:Name` values are
  genuinely load-bearing (they are the on-the-wire Ollama option names), so their inclusion improves
  the render's usefulness for anyone reasoning about the emitted payload.
- Neither render is compilable Ballerina (see §5 items 5-9). This is a renderer-wide characteristic,
  not specific to this library.
- README quality is good and both renders carry it intact; note the README itself has upstream typos
  ("Intialize", and a "Step 4" that follows "Step 2") — reproduced faithfully, not a render defect.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 155 / 197 |
| `diff old new \| grep -c '^<'` / `'^>'` | 2 / 44 |
| `diff old new \| grep '^<'` | only the `init` and `generate` signature lines |
| `diff old new \| grep '^>' \| grep -v '@display\|@jsondata'` | 4 lines: blank, `// --- Annotations ---`, blank, `public annotation map<json> JsonSchema on type;` |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 1 / 0 |
| `grep -n '^// --- '` old / new | old: 7,57,59,141 · new: 7,57,59,178,195 |
| `grep -o '@display' bala/*.bal \| wc -l` vs new render | 34 vs 34 |
| `grep -o '@jsondata:Name' bala/*.bal \| wc -l` vs new render | 9 vs 9 |
| `diff <(grep -ho 'label: "[^"]*"' bala/*.bal \| sort) <(… new render …)` | identical |
| `diff <(grep -ho '@jsondata:Name {value: "[^"]*"}' bala/*.bal \| sort) <(… new render …)` | identical |
| JSON key-path set diff (old vs new) | `only in old: []`; 17 new paths, all under `annotations` |
| JSON declaration sets | typeDefs `[ConnectionConfig, OllamaModelParameters]`, clients `[ModelProvider: init, chat, generate]`, functions `[]`, services `0` — equal on both sides |
| JSON `init` params compared element-wise (annotations excluded) | 30 params, zero differences |
| JSON `init` return type | old `ballerina/ai:1.13.0:Error?` → new `ai:Error?` |
| JSON `readme` old vs new | identical; and identical to `bala/docs/README.md` (48 lines) |
| `gh api repos/…/module-ballerinax-ai.ollama/tags` | `v1.2.4` present (10 tags) |
| `git clone --depth 1 --branch v1.2.4` | succeeded |
| `diff -q ballerina/{provider,types,to_json_schema,provider_utils}.bal` vs bala `modules/ai.ollama/` | all 4 identical |
| `ls bala/…/modules/` | single module `ai.ollama` (no submodules) |
| `grep -n '^public\|^\s*public ' bala/…/*.bal` | 4 public exports + `public isolated function init` |
| `cat bala/…/compiler-plugin/compiler-plugin.json` | `ai-ollama-compiler-plugin` / `AiOllamaCompilerPlugin` / 2 jars |
| `grep -n 'AI_MODULE_NAME\|aiPrefix\|SCHEMA_ANNOTATION_IDENTIFIER' GenerateMethodModificationTask.java` | plugin emits `ai:JsonSchema`, not `ollama:JsonSchema` |
| `curl api.central.ballerina.io/…/ballerinax/ai.ollama/1.2.4` | `deprecated: None`, 1 module, pullCount 2031 |
| `bala/…/package.json` | version 1.2.4, `export: ["ai.ollama"]`, ballerina_version 2201.12.0 |
| new render lines 114-117 (`sed -n`) | continuation doc lines emitted without `#`, at column 0 |

## 10. Caveats and unverified items

- The two renders were taken as given; the pipeline was **not** re-run, so this report verifies the
  render *contents* against the library, not that re-running the pipeline reproduces them.
- The compiler-plugin behaviour was read from Java source at `v1.2.4`; the plugin was not executed,
  so the claim that it attaches `ai:JsonSchema` (rather than `ollama:JsonSchema`) rests on source
  reading (`GenerateMethodModificationTask.java:81-82, 410, 466-467`), not on observed output.
- Whether `@display` metadata placed after a blank line following the doc comment (e.g. new lines
  61-64) still binds the doc string to the declaration under the Ballerina parser was not tested; the
  blank line is present in `old` too, so it is not a `new` behaviour either way.
- `git ls-remote` / `git clone` initially failed inside the sandbox (port 443 blocked); tags and the
  clone were obtained with network access enabled. No information was taken from an unverified
  source.

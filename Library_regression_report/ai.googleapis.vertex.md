# ballerinax/ai.googleapis.vertex 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.googleapis.vertex` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.googleapis.vertex |
| Tag reviewed | `v1.0.2` (commit `fb90b7a8d414a230c0a8f665c905b3196a143a4a`, grafted shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.googleapis.vertex/1.0.2` |
| Old render | `257` lines |
| New render | `277` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module connector (8 public symbols in the default module). `new` is strictly better
than `old`: it restores the one degraded type (`ServiceAccountJsonFilePath`), removes all 5
version/module-qualified type references that made `old` non-compiling, and adds the 20 `@display`
annotations that exist in the library source — all 26 distinct labels match the source 1:1. No
declaration, parameter, default, doc line, or README content was lost. Zero regressions found.

Several inaccuracies remain, but every one of them is present identically in `old` (record
closed-ness/defaults dropped, `*ConnectionConfig` included-param handling, bare `AUTO` default,
`typedesc<anydata>` flattened to `anydata`), so they are pre-existing renderer/extractor limits, not
spec-v2 damage.

## 2. Change inventory

Line counts: `old` 257, `new` 277 (`wc -l`). Diff: +25 / −5 across 6 hunks.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 1 | 0 |
| Version-qualified type refs (`org/mod:1.2.3:Type`) | 5 occurrences | 0 |
| `@display` annotations | 0 | 20 |
| `// --- ` section markers | 4 | 4 |
| Top-level doc (`#`) lines | 39 | 42 |
| JSON size (bytes) | 42,526 | 47,669 |

**Declarations — added (1), removed (0), modified (7).**

Set diff of top-level declarations (`diff <(grep -oE '^(type|enum|const|client class|class) [A-Za-z_]+' old|sort) <(… new|sort)`) yields exactly one line: `> type ServiceAccountJsonFilePath`.

| Kind | old | new | Note |
|---|---|---|---|
| `const` | 3 | 3 | unchanged (`TEXT_EMBEDDING_005/004`, `TEXT_MULTILINGUAL_EMBEDDING_002`) |
| `type` (record) | 3 | 3 | `ConnectionConfig` gained 15 `@display` lines |
| `type` (union) | 1 | 1 | `VertexAiAuth` refs de-qualified |
| `type` (other/alias) | 0 | 1 | **added** `ServiceAccountJsonFilePath string` (was `// Unknown type:`) |
| `enum` | 1 | 1 | identical |
| `client class` | 2 | 2 | each gained a class-level `@display` |
| client methods | 6 | 6 | same 6: `init`, `embed`, `batchEmbed` / `init`, `chat`, `generate` |
| module-level functions / services / annotations | 0 / 0 / 0 | 0 / 0 / 0 | JSON `functions`, `services`, `annotations` all empty on both sides |

**Modified declarations (all 6 hunks):**

1. `ConnectionConfig` (old:142 → new:143): +1 type-level and +14 field-level `@display` lines.
2. `ServiceAccountJsonFilePath` (old:195 → new:210–213): `// Unknown type: ServiceAccountJsonFilePath` replaced by the doc comment + `type ServiceAccountJsonFilePath string;`. Driven by the extractor: new JSON adds `"baseType": "string"` to that `Other` typeDef; old JSON has no `baseType`.
3. `VertexAiAuth` (old:203 → new:221): `ballerinax/ai.googleapis.vertex:1.0.2:X|…` → `OAuth2RefreshConfig|ServiceAccountConfig|ServiceAccountJsonFilePath`. Confirmed at JSON level: union `members[].name` changed from fully-qualified to bare.
4. `EmbeddingProvider` (old:216 → new:234–236): class `@display`, 5 param `@display`s, return type `ballerina/ai:1.13.0:Error?` → `ai:Error?`.
5. `ModelProvider` (old:245 → new:264–266): same pattern, 7 param `@display`s.
6. `generate` (old:256 → new:276): `td` param gained `@display {label: "Expected type"}`.

README block (lines 1–130) is byte-identical between the two renders (`diff <(head -138 old) <(head -138 new)` → no output) and the JSON `readme` field is identical on both sides and equal to the bala `docs/README.md` (121 lines, string compare `True`).

## 3. Correctness against library source

Repo tag `v1.0.2` and the bala agree exactly — all 8 `.bal` files compare byte-identical
(`diff -q src/ballerina/<f> bala/modules/ai.googleapis.vertex/<f>` → SAME for types.bal,
model-provider.bal, embedding-provider.bal, auth_utils.bal, provider_utils.bal, to_json_schema.bal,
anthropic-utils.bal, mistral-utils.bal).

Everything `new` adds or changes was verified against the source:

| New render | Source evidence | Verdict |
|---|---|---|
| `type ServiceAccountJsonFilePath string;` (new:213) + its 3 doc lines | `types.bal:89-92` — `public type ServiceAccountJsonFilePath string;` with identical doc | correct |
| `type VertexAiAuth OAuth2RefreshConfig\|ServiceAccountConfig\|ServiceAccountJsonFilePath;` (new:221) | `types.bal:87` — identical member order | correct |
| `@display {label: "Connection Configuration"}` on `ConnectionConfig` | `types.bal:21` | correct |
| 14 field `@display`s on `ConnectionConfig` | `types.bal:25,29,33,37,41,45,49,53,57,61,65,69,73,77` | correct |
| `@display {label: "Google Vertex Embedding Provider"}` | `embedding-provider.bal:25` | correct |
| `@display {label: "Google Vertex Model Provider"}` | `model-provider.bal:40` | correct |
| `EmbeddingProvider.init` param labels Auth/Project ID/Location/Model Type/Service URL/Connection Configuration | `embedding-provider.bal:47-52` | correct, same order |
| `ModelProvider.init` param labels Auth/Project ID/Model/Location/Service URL/Maximum Tokens/Temperature/Connection Configuration | `model-provider.bal:70-77` | correct, same order |
| `@display {label: "Expected type"}` on `generate`'s `td` | `model-provider.bal:238` | correct |
| `ai:Error?` return on both `init`s | `embedding-provider.bal:52`, `model-provider.bal:78` | correct |

Label census is exact: `grep -o '@display {label: "[^"]*"}' | sort | uniq -c` produces the **same 26
distinct labels with the same multiplicities** for the bala source and for the new render (Auth×2,
Connection Configuration×3, Location×2, Project ID×2, Service URL×2, all others ×1).

Signatures unchanged between sides were also spot-checked and match source: `chat`
(`model-provider.bal:168-169` — `ai:ChatMessage[]|ai:ChatUserMessage messages,
ai:ChatCompletionFunctions[] tools = [], string? stop = ()` → rendered as `string|() stop = ()`,
equivalent), `batchEmbed` (`embedding-provider.bal:147`), enum members
(`types.bal:133-137`), consts (`types.bal:134-136`).

## 4. Regressions

**None found.**

What I checked to conclude that:
- Declaration set diff (top-level + client methods): only addition, no removal — `type ServiceAccountJsonFilePath` added; method lists identical (`init/embed/batchEmbed`, `init/chat/generate`).
- Removed diff lines (5 total) are all the *left* halves of in-place replacements (hunk-by-hunk read of `OLD_AND_NEW_DIFFS/ai.googleapis.vertex_diff.md` against both files) — no line removed without a strictly richer replacement.
- Doc content: `#` doc-line count went 39 → 42 (the 3 added lines are `ServiceAccountJsonFilePath`'s doc, previously suppressed by the `Unknown type` degradation). No doc text deleted.
- README section identical byte-for-byte; section markers unchanged (4/4).
- Parameters, defaults and return types: every `init`/`chat`/`generate`/`embed`/`batchEmbed` parameter, default value and return type present in `old` is present in `new` (line-by-line comparison of old:217/246/251/256 vs new:236/266/271/276).
- Syntax quality *improved*: `old` emitted `ballerina/ai:1.13.0:Error?` and
  `ballerinax/ai.googleapis.vertex:1.0.2:OAuth2RefreshConfig|…`, which are not valid Ballerina type
  references; `new` emits resolvable names.

## 5. Issues in `new` (independent of `old`)

All nine below are present **identically in `old`** — none is caused by spec v2 — but they are real
inaccuracies vs. the library source that a consumer of the render would be misled by.

1. **`ConnectionConfig` rendered as an open record with every field optional and no defaults.**
   Source `types.bal:22-79` is a *closed* record (`record {| … |}`) where `httpVersion = http:HTTP_2_0`,
   `timeout = 60`, `forwarded = "disable"`, `compression = http:COMPRESSION_AUTO`, `validation = true`
   are required-with-default, not optional. Render (new:143-186) shows all 14 fields as `?` in an open
   record. Confirmed to originate in the extractor: JSON field objects carry `"optional": true` and no
   default.
2. **`readonly &` and closed-record shape dropped on `OAuth2RefreshConfig` and `ServiceAccountConfig`.**
   Source `types.bal:98` / `types.bal:112` are `readonly & record {| … |}`; render emits plain open
   `record { … }` (new:193, new:204).
3. **Field-level documentation lost for those two records.** Source documents every field
   (`types.bal:99-106`, `113-118`: "OAuth2 client ID", "Service account email (`client_email` …)", …);
   both JSONs carry `"description": ""` for all of them, so the render has none.
4. **Field defaults lost for those records**: `refreshUrl = "https://oauth2.googleapis.com/token"`
   (`types.bal:106`) and `scopes = ["https://www.googleapis.com/auth/cloud-platform"]`
   (`types.bal:118`) are rendered as bare optional fields.
5. **`*ConnectionConfig` included-record parameter is both expanded and duplicated.** Source
   `model-provider.bal:77` / `embedding-provider.bal:52` declare a single
   `*ConnectionConfig connectionConfig`. The render expands it into 14 individual defaulted params
   *and then* appends a required `ConnectionConfig connectionConfig` with no default, after defaulted
   params — a signature that is neither valid Ballerina nor callable as shown (new:236, new:266).
6. **`http:Compression compression = AUTO`** (new:236, new:266): `AUTO` is the *string value* of
   `http:COMPRESSION_AUTO` (`ballerina/http` 2.16.6 `http_constants.bal:105,109`:
   `public type Compression COMPRESSION_AUTO|…; public const COMPRESSION_AUTO = "AUTO";`). A bare
   `AUTO` does not resolve in user code; the correct default is `http:COMPRESSION_AUTO`.
7. **`generate` loses the typedesc**: source `model-provider.bal:238` is
   `typedesc<anydata> td = <>` (inferred type descriptor, external `@java:Method`); render shows
   `anydata td = anydata`, which is not valid syntax and misrepresents the API. JSON already encodes
   it as `{"type":{"name":"anydata"},"default":"anydata"}` on both sides — an extractor issue.
8. **Parameter documentation is present in the JSON but dropped by the renderer.** e.g. the `generate`
   JSON carries `"description": "The prompt to use"` / `"Type descriptor specifying the expected
   return type format"`, yet the render emits only the method description followed by a dangling
   `# ` line (new:239, 246, 270, 275). The `+ auth - …` / `+ projectId - …` param docs from
   `model-provider.bal:56-68` and `embedding-provider.bal:38-45` are lost entirely.
9. **Modifiers and type inclusions not rendered**: source classes are
   `public isolated distinct client class` with `*ai:ModelProvider` / `*ai:EmbeddingProvider`
   inclusions (`model-provider.bal:41-42`, `embedding-provider.bal:26-27`); the render shows plain
   `client class` with no inclusion, so the render never states that these types implement the
   `ai:ModelProvider` / `ai:EmbeddingProvider` contracts. Related minor: `embed` is rendered as
   returning `ai:Vector|ai:SparseVector|ai:HybridVector|ai:Error` (the expansion of `ai:Embedding`)
   while the adjacent `batchEmbed` keeps `ai:Embedding[]` — inconsistent, though not wrong; and enum
   members are rendered without their string values (`types.bal:134-136`) in a different order than
   the source, the values surviving only via the three separate `const` declarations.

## 6. Coverage gaps vs. the library

**Zero gaps.** The default module exports exactly 8 public symbols
(`grep -rnE '^\s*public ' bala/modules/ai.googleapis.vertex/*.bal`):

| Public symbol | Source | In `old` | In `new` |
|---|---|---|---|
| `ConnectionConfig` | types.bal:22 | yes | yes |
| `VertexAiAuth` | types.bal:87 | yes (mangled refs) | yes |
| `ServiceAccountJsonFilePath` | types.bal:92 | **no** (`// Unknown type:`) | yes |
| `OAuth2RefreshConfig` | types.bal:98 | yes | yes |
| `ServiceAccountConfig` | types.bal:112 | yes | yes |
| `VertexAiEmbeddingModelNames` | types.bal:133 | yes | yes |
| `EmbeddingProvider` (+ `init`, `embed`, `batchEmbed`) | embedding-provider.bal:26,46,116,147 | yes | yes |
| `ModelProvider` (+ `init`, `chat`, `generate`) | model-provider.bal:41,69,168,237 | yes | yes |

No submodule gap: the bala contains a single module directory
(`modules/ai.googleapis.vertex`), and `package.json` `"export": ["ai.googleapis.vertex"]`; Central
also lists exactly one module. Non-public internal types (`VertexAiPart`, `AnthropicMessage`,
`MistralResponse`, `ChatResult`, …) and private methods are correctly absent from both renders.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `plugin_class:
io.ballerina.lib.ai.googleapis.vertex.compiler.AiVertexAICompilerPlugin` with two jars
(`ai.googleapis.vertex-compiler-plugin-1.0.2.jar`, `ballerina-to-openapi-2.3.0.jar`).

Source (`compiler-plugin/src/main/java/io/ballerina/lib/ai/googleapis/vertex/compiler/`):
`AiVertexAICompilerPlugin` registers a single `CodeModifier` (`AiVertexAICodeModifier`), which runs
`GenerateMethodModificationTask`. That task walks call sites of `ModelProvider`'s `generate` remote
method, derives an OpenAPI schema for the inferred `td` type via `ballerina-to-openapi`'s
`TypeMapper`, converts it with `OpenAPISchema2JsonSchema`, and injects an `@ai:JsonSchema { … }`
annotation on the target type definition if one is not already present
(`GenerateMethodModificationTask.java:174-175, 211-238, 273, 289-295, 396, 443-450`;
`TypeMapperImplInitializer.java`). It contributes **no** code actions and **no** diagnostics.

Implication for the render: nothing the plugin defines is a public API symbol, so nothing is missing
from the render on that account. The one thing worth noting is that the plugin's entire purpose is
the inferred-typedesc `generate` API, and both renders misrepresent that signature as
`anydata td = anydata` (issue 5.7). The README (rendered verbatim in both) does show the manual
`@ai:JsonSchema` form, so an LLM reading the render still sees the pattern.

## 8. Other considerations

- **Pre-1.0 / stability**: version `1.0.2` is a stable release. Central reports
  `deprecated: null`, empty `deprecateMessage`, 2,211 pulls, published 2026-07-16.
- **Version drift**: none. Both renders are `ballerinax/ai.googleapis.vertex:1.0.2`; the repo tag
  `v1.0.2` sources are byte-identical to the bala sources.
- **Size/token impact**: `new` is +20 render lines (+7.8%) and +5,143 JSON bytes (+12.1%), entirely
  from `@display` annotations plus the one restored type. The `@display` labels are low-information
  for an LLM consumer (they duplicate the parameter names in title case) and materially lengthen the
  two already very long `init` lines; that is a cost, not an error.
- **Doc quality**: README is high quality and rendered in full (121 lines, verbatim). Class-level
  docs are rich; the loss of `+ param -` docs (issue 5.8) is the main doc deficiency, shared by both.
- **`ballerina/ai` dependency**: `ai:Error`, `ai:Chunk`, `ai:Prompt` etc. are annotated with the
  "Special Agent Note: … FROM ballerina/ai package" trailer on both sides; `new` correctly renders
  them with the `ai:` prefix rather than `ballerina/ai:1.13.0:`.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 257 / 277 |
| `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| `grep -o 'ballerinax/ai.googleapis.vertex:1.0.2:\|ballerina/ai:1.13.0:' old \| wc -l` | 5 (new: `grep -c ':1\.[0-9]*\.[0-9]*:'` = 0) |
| `grep -c '@display'` old / new | 0 / 20 |
| `grep -n '^// --- ' new` | 4 markers: README(7), END README(130), Types(132), Client(230) |
| `diff <(head -138 old) <(head -138 new)` | empty → README + consts identical |
| `diff <(grep -oE '^(type\|enum\|const\|client class\|class) [A-Za-z_]+' old\|sort) <(… new\|sort)` | single line `> type ServiceAccountJsonFilePath` |
| `grep -nE '^    (remote )?function' old` / `new` | 6 methods each, same names/order |
| `grep -c '^#' old` / `new` | 39 / 42 |
| `wc -c old/*.json new/*.json` | 42,526 / 47,669 |
| `git ls-remote --tags <repo>` | tags `v1.0.0`, `v1.0.1`, `v1.0.2` → exact tag `v1.0.2` exists |
| `git clone --depth 1 --branch v1.0.2 …` + `git log -1` | `fb90b7a8d414a230c0a8f665c905b3196a143a4a (tag: v1.0.2)` |
| `diff -q src/ballerina/<f> bala/modules/ai.googleapis.vertex/<f>` × 8 | SAME for all 8 `.bal` files |
| `grep -rnE '^\s*public ' bala/modules/…/*.bal` | 10 hits → 8 public symbols (2 are the `init`s) |
| `grep -h -o '@display {label: "[^"]*"}' \| sort \| uniq -c` on bala source vs new render | identical 26-label census |
| `ls bala/…/modules/` | single dir `ai.googleapis.vertex` → no submodules |
| `cat bala/…/package.json` | `"export": ["ai.googleapis.vertex"]`, ballerina_version 2201.12.6, graalvmCompatible true |
| `cat bala/…/compiler-plugin/compiler-plugin.json` | plugin class + 2 dependency jars |
| Python: JSON `typeDefs` comparison old vs new | same 9 typeDefs; `ServiceAccountJsonFilePath` gains `"baseType":"string"` in new; `ConnectionConfig` gains `annotations` at type and field level; `VertexAiAuth` union member names de-qualified |
| Python: JSON `readme` vs bala `docs/README.md` | equal (`True`), 121 lines both; old readme == new readme (`True`) |
| Python: JSON `functions` / `services` / `annotations` | 0 / 0 / `[]` on both sides |
| `grep -n 'COMPRESSION_AUTO\|public enum Compression'` in ballerina/http 2.16.6 bala | `http_constants.bal:105,109` → `AUTO` is the value of `http:COMPRESSION_AUTO` |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/ai.googleapis.vertex/1.0.2` | deprecated `None`, 1 module, pullCount 2211 |
| `grep -n 'JsonSchema\|generate\|typedesc' GenerateMethodModificationTask.java` | code modifier injects `@ai:JsonSchema`; no code actions, no diagnostics |

## 10. Caveats and unverified items

- The clone is shallow/grafted (`--depth 1`), so no repository history was inspected; this does not
  affect any claim, since the tagged sources were compared byte-for-byte with the bala.
- The first GitHub clone attempt timed out (transient network); the retry succeeded. No claim rests
  on the failed attempt.
- I did not compile the render as Ballerina code. Syntax judgements in §5 (items 5, 6, 7) are based
  on reading the language rules and the `ballerina/http` constant definitions, not on running
  `bal build`.
- The claim that these renders were produced from the two `ballerina-vscode` commits named in the
  brief is taken from the brief; I did not re-run the render pipeline to reproduce either file.
- `pullCount`/`createdDate` come from Ballerina Central at review time and may change.

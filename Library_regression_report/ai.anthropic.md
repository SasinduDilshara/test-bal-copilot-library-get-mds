# ballerinax/ai.anthropic 1.3.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.anthropic` |
| Pinned version | `1.3.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.anthropic |
| Tag reviewed | `v1.3.4` (commit `0c86161`, exact match) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.anthropic/1.3.4` |
| Old render | `168` lines (7,753 bytes) |
| New render | `188` lines (8,699 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old`. Nothing was removed, truncated, or degraded. Three changes:

1. All 22 `@display` annotations that exist in the library source are now emitted (0 in `old`), on the record type, its 14 fields, the enum, 5 `init` parameters and 1 `generate` parameter. Labels match the source exactly, including multiplicity — no invented annotations.
2. The one version/module-qualified type reference in `old` (`returns ballerina/ai:1.13.0:Error?` on `init`) is now `returns ai:Error?`, which matches the library source verbatim and is valid Ballerina.
3. A new `// --- Annotations ---` section emits `public annotation map<json> JsonSchema on type;`, a genuine public export of the default module that `old` dropped entirely.

Both renders share a set of pre-existing extractor inaccuracies (unquoted string default, `*ConnectionConfig` include-record flattening plus duplication, `typedesc<anydata> td = <>` rendered as `anydata td = anydata`, missing `public`/`isolated` qualifiers, closed record rendered as open). None of these changed between the two sides, so none is a regression; they are recorded in §5 for completeness.

## 2. Change inventory

Line counts (`wc -l`): old 168, new 188 (+20 lines, +11.9%). JSON: old 26,254 bytes, new 29,933 bytes.

Declaration sets extracted from both renders and compared (script in §9):

| | old | new |
|---|---|---|
| Total top-level + client-member declarations | 24 | 25 |
| Declarations only in `old` | — | **0** |
| Declarations only in `new` | — | **1** (`public annotation map<json> JsonSchema on type;`) |

By kind (identical on both sides except the annotation):

| Kind | old | new |
|---|---|---|
| `const` | 18 | 18 |
| `type` (record) | 1 | 1 |
| `enum` | 1 | 1 |
| `client class` | 1 | 1 |
| client methods (`init`, `chat`, `generate`) | 3 | 3 |
| `annotation` | 0 | **1** |
| `function` (module-level) | 0 | 0 |
| `service` / `listener` | 0 | 0 |

Declarations **modified** (4): `ConnectionConfig` (+1 type-level and +14 field-level `@display`), `ANTHROPIC_MODEL_NAMES` (+1 `@display`), `ModelProvider.init` (+5 param `@display`, return type `ballerina/ai:1.13.0:Error?` → `ai:Error?`), `ModelProvider.generate` (+1 param `@display`).

Signals verified directly with `grep -c`:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 |
| `// --- ` section markers | 4 | 5 |
| `@display` occurrences | 0 | 22 |
| Non-ASCII bytes | 0 | 0 |

JSON-level structural diff (all key paths, recursive): **zero paths present in `old` but absent in `new`**. New paths in `new` are only: `/annotations[]/{name,attachmentPoint,typeConstraint}`, `/typeDefs[]/annotations[]`, `/typeDefs[]/fields[]/annotations[]`, `/clients[]/functions[]/parameters[]/annotations[]`. `typeDefs` = 20 on both sides; `clients` = 1 on both; `readme` length = 1,647 chars on both (README block is byte-identical).

## 3. Correctness against library source

Bala module sources are **byte-identical** to upstream `v1.3.4` (`diff -q` on all four `.bal` files plus `README.md` → identical), so GitHub and the bala agree and either can be cited.

Everything `new` adds or changes was checked against source:

- `public annotation map<json> JsonSchema on type;` — exact, `modules/ai.anthropic/to_json_schema.bal:32`. Attachment point `on type` and type constraint `map<json>` both correct (JSON: `{"name":"JsonSchema","attachmentPoint":"TYPE","typeConstraint":{"name":"map<json>"}}`).
- `returns ai:Error?` on `init` — exact, `model-provider.bal:51` (`... *ConnectionConfig connectionConfig) returns ai:Error?`). `old`'s `ballerina/ai:1.13.0:Error?` is not writable Ballerina; `new` is.
- All 22 `@display` labels — verified exhaustively, not spot-checked: `diff` of `grep -oh '@display {label: "[^"]*"}' | sort | uniq -c` over the three bala `.bal` files vs. the new render is **empty**, i.e. the multiset of labels is identical. Source locations: `types.bal:20` (type), `types.bal:24,28,32,36,40,44,48,52,56,60,64,68,72,76` (14 fields), `types.bal:81` (enum), `model-provider.bal:47,48,49,50,51` (init params `modelType`, `serviceUrl`, `maxTokens`, `temperature`, `connectionConfig`), `model-provider.bal:174` (`generate` param `td`, label `"Expected type"`). Count: 16 in `types.bal` + 6 in `model-provider.bal` = 22, matching the render's 22.
- Placement is correct: type-level annotation before `type ConnectionConfig`, field annotations after each field's doc line, parameter annotations inline before the parameter type — all valid Ballerina metadata positions.
- Unchanged declarations re-verified against source: `chat` (`model-provider.bal:88`), enum members and values (`types.bal:83-100`, all 18 present and values correct), `ConnectionConfig` field names/types (`types.bal:21-78`, all 14 present).

## 4. Regressions

**None found.**

Basis for that conclusion:
- Declaration-set diff: `only old: []` — no declaration lost.
- JSON key-path diff: no path present in `old` and missing in `new`.
- README block: byte-identical (no hunk in the diff covers lines 1–98 other than the annotation additions; `readme` field length identical at 1,647 chars).
- All doc comments (`#` lines) preserved; `init` param defaults byte-identical between the two JSONs (all 20 parameters compared pairwise, including `serviceUrl='https://api.anthropic.com/v1'`, `maxTokens='512'`, `temperature='0.7'`, `httpVersion='http:HTTP_2_0'`, `forwarded='"disable"'`, `validation='true'`).
- Return types on `chat` and `generate` unchanged; the only return-type change (`init`) is strictly more accurate.
- No new malformed syntax: the two lines rewritten in `new` (init, generate) remain parseable to the same degree as before, and the added annotation line is valid Ballerina.

## 5. Issues in `new` (independent of `old`)

All of the following are **present identically in `old`** — they are extractor-level inaccuracies, not introduced by spec v2. Listed because they mislead an LLM consuming either render.

1. **Unquoted string default** — `string serviceUrl = https://api.anthropic.com/v1` (new:175, old:159). Non-compiling; the JSON stores the default without quotes (`"default": "https://api.anthropic.com/v1"`) while `forwarded` correctly stores `"\"disable\""`. Source: `model-provider.bal:48` (`= DEFAULT_ANTHROPIC_SERVICE_URL`).
2. **`generate`'s typedesc parameter is mangled** — render shows `anydata td = anydata`; source `model-provider.bal:174` is `typedesc<anydata> td = <>`. Both the `typedesc<>` wrapper and the inferred-default `<>` are lost, and `= anydata` is not valid syntax.
3. **`*ConnectionConfig` include-record param is flattened *and* duplicated** — the render lists the 14 `ConnectionConfig` fields as individual `init` parameters *and* then a final `ConnectionConfig connectionConfig` parameter with no default, placed after defaulted parameters. Source has only `*ConnectionConfig connectionConfig` (`model-provider.bal:51`). The `*` is absent, so the render implies a 20-argument positional signature that does not exist.
4. **`compression` default wrong** — render `http:Compression compression = AUTO`; source `types.bal:53` is `http:Compression compression = http:COMPRESSION_AUTO`. `AUTO` is not a resolvable symbol here.
5. **Qualifiers dropped** — `public` and `isolated` are missing from `ModelProvider` (source: `public isolated client class`), `ConnectionConfig`, `ANTHROPIC_MODEL_NAMES`, `init`, `chat`, `generate`. `new` now emits `public` on the annotation only (1 occurrence), which makes the render internally inconsistent — a reader may infer the other symbols are not public.
6. **Closed record rendered as open** — `type ConnectionConfig record { ... }`; source is `record {| ... |}` (`types.bal:21,78`).
7. **Field defaults become optional markers** — e.g. `http:HttpVersion httpVersion?` in the render vs. `http:HttpVersion httpVersion = http:HTTP_2_0;` in `types.bal:25` (also `timeout`, `forwarded`, `compression`, `validation`). The render says "optional, no default"; the source says "required with default". Identical in both JSONs (`"optional": true`, `"defaultValue"` absent), so this is an extractor gap on both sides.
8. **`*ai:ModelProvider` inclusion not surfaced** — `model-provider.bal:29` includes the `ai:ModelProvider` object type; neither render states that `ModelProvider` conforms to it. Only the README snippet hints at it.
9. **`stop` union widened cosmetically** — `string|() stop = ()` vs. source `string? stop = ()` (`model-provider.bal:88`). Semantically equivalent; noted only for completeness.

## 6. Coverage gaps vs. the library

Complete set of public declarations in the default (and only) module, from `grep -nE '^\s*public ' modules/ai.anthropic/*.bal`:

| Public symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `ModelProvider` (client class) | `model-provider.bal:28` | yes | yes |
| `ModelProvider.init` | `model-provider.bal:46` | yes | yes |
| `ConnectionConfig` (record) | `types.bal:21` | yes | yes |
| `ANTHROPIC_MODEL_NAMES` (enum, 18 members) | `types.bal:82` | yes | yes |
| `JsonSchema` (annotation) | `to_json_schema.bal:32` | **no** | yes |

Plus the two non-`public` but externally reachable `remote` methods `chat` (`model-provider.bal:88`) and `generate` (`model-provider.bal:174`) — both present in both renders.

**Coverage gaps in `new`: 0.** `old` had 1 (the `JsonSchema` annotation).

Submodule API: none. The bala contains exactly one module directory (`modules/ai.anthropic`) and Central reports `modules: ['ai.anthropic']`, so the `getDefaultModule()`-only extraction limitation costs this library nothing.

Non-public symbols correctly absent from both renders: `AnthropicMessage`, `AnthropicApiResponse`, `ContentBlock`, `Usage`, `AnthropicTool` (`types.bal:104-165`), the local `JsonSchema`/`JsonArraySchema` records (`to_json_schema.bal:20,27`), the `DEFAULT_*` / `ANTHROPIC_API_VERSION` module constants (`model-provider.bal:22-25`), and the private/isolated helper functions.

## 7. Compiler plugin

Plugin: `io.ballerina.lib.ai.anthropic.AiAnthropicCompilerPlugin` (`compiler-plugin/compiler-plugin.json`), with `ballerina-to-openapi-2.3.0.jar` as a dependency.

- It registers exactly one task: `context.addCodeModifier(new AiAnthropicCodeModifier())` (`AiAnthropicCompilerPlugin.java:33`). No code actions, no validations, no diagnostics.
- `GenerateMethodModificationTask.java` walks call sites of `ModelProvider`'s `generate` method (`GENERATE_METHOD_NAME = "generate"`, line 210), derives an OpenAPI-then-JSON-Schema representation of the inferred `td` type (`OpenAPISchema2JsonSchema`, lines 287-293) and **injects** a `JsonSchema` annotation onto the user's type definition (`getSchemaAnnotation`, line ~466), adding a `ballerina/ai` import where needed.
- The injected annotation is prefixed with the **`ballerina/ai`** module prefix (`aiPrefix`, defaulting to `AI_MODULE_NAME`; `TypeDefinitionModifier`, lines 397-411 and `isJsonSchemaAnnotationAvailable`, lines 454-462), and the runtime lookup is likewise `expectedResponseTypedesc.@ai:JsonSchema` (`to_json_schema.bal:35`). So the annotation the plugin and runtime actually consume is `ai:JsonSchema`, **not** the `anthropic:JsonSchema` that `new` now renders.
- Consequence: `new`'s new annotation line is a faithful report of the module's public API, but it is a redundant/vestigial export — a model reading the render could plausibly write `@anthropic:JsonSchema {...}`, which the plugin's `isJsonSchemaAnnotationAvailable` check would not recognise. This is a library-design wart, not a renderer defect, and it is strictly better than `old`, which showed the symbol not at all. No plugin-implied artifact is missing from `new`.

## 8. Other considerations

- Version `1.3.4` is post-1.0 and stable. Central reports `deprecated: None`, `pullCount: 2363`, `ballerinaVersion: 2201.12.0`.
- Token cost: `new` is +946 bytes / +20 lines (+11.9%) over `old`. The added `@display` labels are UI metadata of little value to a code-generating LLM; the `ai:Error?` fix and the annotation are of real value. The cost is small in absolute terms for a library this size.
- Doc quality (both renders, inherited from the library README, `docs/README.md`): typo "nessary" (line 23), and the Quickstart jumps from "Step 2" to "Step 4" (line 51). The Step 2 snippet also passes three positional arguments — `new anthropic:ModelProvider("anthropicAiApiKey", anthropic:CLAUDE_3_7_SONNET_20250219, "2023-06-01")` — where the third positional parameter is `serviceUrl`, not an API version; `ANTHROPIC_API_VERSION` is a private constant (`model-provider.bal:25`) and not settable. This misleading snippet is verbatim in both renders and is a library-README bug, not a renderer bug.
- Neither render emits a syntactically valid compilation unit (see §5 items 1-4), so the output must be read as reference material, not copy-pasteable code. Unchanged between sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `python3` manifest lookup for `ai.anthropic` | version 1.3.4; all paths as given |
| `wc -c -l` both renders | old 168 lines / 7,753 B; new 188 lines / 8,699 B |
| `wc -c` both JSONs | old 26,254 B; new 29,933 B |
| `git ls-remote --tags .../module-ballerinax-ai.anthropic` | `refs/tags/v1.3.4` → `0c861610176e237c3ebee7d3a8b46bfbbeca4ce0` |
| clone at `v1.3.4`; `git log --oneline -1` / `git describe --tags` | `0c86161 [Gradle Release Plugin] - pre tag commit: 'v1.3.4'`; `v1.3.4` |
| `diff -q` bala `modules/ai.anthropic/{types,to_json_schema,model-provider,provider_utils}.bal` vs upstream `ballerina/*.bal` | all 4 identical |
| `diff` bala `docs/README.md` vs upstream `ballerina/README.md` | identical |
| `find . -type f` in bala | 1 module only; compiler-plugin + native jars present |
| `ls modules/` in bala | `ai.anthropic` (single, default module) |
| `curl api.central.ballerina.io/.../ballerinax/ai.anthropic/1.3.4` | `modules: ['ai.anthropic']`, `deprecated: None`, pulls 2363 |
| `grep -nE '^\s*public ' modules/ai.anthropic/*.bal` | 5 public decls: `ModelProvider`:28, `init`:46, `ConnectionConfig`:21, `ANTHROPIC_MODEL_NAMES`:82, `JsonSchema` annotation:32 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both | old 1, new 0 |
| `grep -c '^// --- '` both | old 4, new 5 |
| `grep -oc '@display'` both | old 0, new 22 |
| `grep -c '\bpublic\b'` / `'\bisolated\b'` both | old 0/0, new 1/0 |
| `LC_ALL=C grep -c '[^ -~]'` both | 0 / 0 |
| `grep -h -c '@display'` bala `types.bal` / `model-provider.bal` | 16 / 6 = 22 total |
| `diff <(grep -oh '@display {label:...}' bala/*.bal \| sort \| uniq -c) <(same on new render)` | empty → label multisets identical |
| Python recursive JSON key-path set diff (old vs new) | paths only in old: `[]`; only in new: 13 annotation-related paths |
| Python: `typeDefs` names + kinds both JSONs | identical 20-entry list (18 Constant, 1 Record, 1 Enum) |
| Python: `clients[0].functions` names both | `['init','chat','generate']` on both |
| Python: `functions[*].return.type.name` both | init `ballerina/ai:1.13.0:Error?` → `ai:Error?`; chat and generate unchanged |
| Python: `init.parameters` names + defaults both | 20 params, names and all defaults byte-identical |
| Python: `ConnectionConfig.fields` both | 14 fields, `optional: true`, no `defaultValue`, identical both sides |
| Python declaration-set extraction from both renders | old 24, new 25; only-old `[]`; only-new `public annotation map<json> JsonSchema on type;` |
| Read `model-provider.bal:16-145`, `165-186` | init signature `*ConnectionConfig`, `returns ai:Error?`; `generate(ai:Prompt, typedesc<anydata> td = <>) returns td\|ai:Error` |
| Read `types.bal` (full, 165 lines) | `record {\|...\|}`, field defaults, 18 enum members with values, 5 non-public records |
| Read `to_json_schema.bal` (full, 105 lines) | `public annotation map<json> JsonSchema on type;`:32; runtime reads `@ai:JsonSchema`:35 |
| `grep`/`sed` `GenerateMethodModificationTask.java`, `AiAnthropicCompilerPlugin.java` | single code modifier; injects `ai:`-prefixed `JsonSchema` on `generate` target types |
| Read `OLD_AND_NEW_DIFFS/ai.anthropic_diff.md` | 3 hunks, +22/−2; all claims re-verified above and found accurate |

## 10. Caveats and unverified items

- The renders were not compiled. Syntax-validity claims in §5 are from reading the text against the Ballerina grammar and the library source, not from a `bal build` run. This affects both sides equally and does not bear on the regression verdict.
- Whether the extractor *could* surface `*ConnectionConfig` / `*ai:ModelProvider` inclusions, or the closed-record `{| |}` form, was not investigated in the `ballerina-vscode` sources; those are reported as observed output gaps common to both sides, not as diagnosed extractor bugs.
- The precomputed diff's "Lines removed = 2" figure was accepted as a diff artifact of the two rewritten lines (init, generate); the declaration-set and JSON key-path comparisons independently confirm nothing was actually removed.
- The scratch clone directory already contained `src` when the clone was attempted (`fatal: destination path 'src' already exists`); its identity was then verified directly (`git describe --tags` → `v1.3.4`, HEAD `0c86161`) and its contents diffed against the bala, so the tag under review is confirmed despite the reused checkout.

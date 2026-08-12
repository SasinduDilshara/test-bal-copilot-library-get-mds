# ballerinax/ai.mistral 1.2.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.mistral` |
| Pinned version | `1.2.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.mistral |
| Tag reviewed | `v1.2.4` (commit `c553cae7e7dba08170b811fe7c34944ba7606fdd`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.mistral/1.2.4/java21` |
| Old render | `211` lines (8,891 bytes) |
| New render | `232` lines (9,909 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The change is purely additive plus one type-reference cleanup. `new` adds 24 `@display` annotations
(exactly the 24 that exist in the published source, with byte-identical label text), adds the
previously-missing `public annotation map<json> JsonSchema on type;` declaration under a new
`// --- Annotations ---` section, and replaces the version-qualified return type
`ballerina/ai:1.13.0:Error?` with `ai:Error?` (which is literally what the source writes).

Nothing is removed. The declaration set grows from 35 to 36; no declaration, parameter, default,
return type, doc line or README byte is lost. Both renders contain 0 `// Unknown type:` placeholders,
so the spec-v2 degraded-type fix is a no-op for this library.

Several accuracy defects do exist in `new` — lost record field defaults, an unquoted URL default, a
wrong `Compression` default symbol, a mangled `generate` type-descriptor parameter, a duplicated
included-record parameter — but every one of them is present verbatim in `old` as well. They are
pre-existing pipeline behaviour, not regressions introduced by spec v2.

## 2. Change inventory

Mechanical totals (verified against the files, not copied from the diff md):

| Metric | old | new |
|---|---|---|
| Lines | 211 | 232 |
| Bytes | 8,891 | 9,909 |
| JSON bytes | 30,109 | 34,098 |
| `// Unknown type:` lines | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 1 | 0 |
| `// --- ` section markers | 4 | 5 |
| `@display` occurrences | 0 | 24 |
| Module-level declarations (regex-extracted) | 35 | 36 |
| Client member functions | 3 (`init`, `chat`, `generate`) | 3 (same) |
| JSON `typeDefs` | 34 | 34 |
| JSON `clients` / `functions` / `services` | 1 / 0 / 0 | 1 / 0 / 0 |
| JSON `annotations` | 0 | 1 |

Sorted-line diff: **25** differing lines total — 23 added, 2 removed. The only two removed lines are
the *old* forms of the `init` and `generate` signatures, both replaced by longer annotated forms on
the `new` side. No content-bearing line disappears.

### Added (1 declaration)

| Kind | Declaration | Where |
|---|---|---|
| annotation | `public annotation map<json> JsonSchema on type;` | new:232, under new `// --- Annotations ---` section (new:230) |

### Removed (0 declarations)

`diff <(sort old) <(sort new) \| grep '^<'` yields only the two superseded signature lines. Declaration-set
diff (`old.decls` vs `new.decls`) shows exactly one line, `> public annotation map`. Nothing removed.

### Modified (2 declarations + 17 type/field/param sites)

| Kind | Declaration | Change in `new` |
|---|---|---|
| client method | `ModelProvider.init` | +5 param-level `@display` annotations; return type `ballerina/ai:1.13.0:Error?` → `ai:Error?` |
| client method | `ModelProvider.generate` | +1 param-level `@display {label: "Expected type"}` on `td` |
| client class | `ModelProvider` | +`@display {label: "Mistral Model Provider"}` |
| type | `ConnectionConfig` | +1 type-level and +14 field-level `@display` |
| enum | `MISTRAL_AI_MODEL_NAMES` | +`@display {label: "Mistral AI Model Names"}` |

The full JSON diff (235 unified-diff lines) contains **only** `annotations` array insertions plus the
single `"name": "ballerina/ai:1.13.0:Error?"` → `"name": "ai:Error?"` edit. No other JSON key changes.
README (1,659 bytes) and `description` are byte-identical between sides and byte-identical to
`java21/docs/README.md`.

## 3. Correctness against library source

GitHub `v1.2.4` and the bala agree exactly: `diff -r src/ballerina <bala>/modules/ai.mistral` reports
only non-`.bal` extras (`Ballerina.toml`, `CompilerPlugin.toml`, `Dependencies.toml`, `README.md`,
`build.gradle`, `icon.png`, `tests`). All four `.bal` files are identical, so source citations below
apply to both.

**Annotations added by `new` — 24/24 exact match, 0 invented.**
Source has exactly 24 `@display` annotations (23 single-line + one multi-line at
`model-provider.bal:29-31`). `new` renders exactly 24. The multiset of label strings is identical
between source and `new` (`grep -o '@display {label: "[^"]*"}' | sort | uniq -c` produces the same
table on both, once the multi-line `"Mistral Model Provider"` is accounted for). Verified sites:

- `types.bal:21` `@display {label: "Connection Configuration"}` on `ConnectionConfig` → new:130 ✓
- `types.bal:25,29,33,37,41,45,49,53,57,61,65,69,73,77` — 14 field labels → new:133,136,139,142,145,148,151,154,157,160,163,166,169,172 ✓ (order and label text match field-for-field)
- `types.bal:82` `"Mistral AI Model Names"` on the enum → new:177 ✓
- `model-provider.bal:29-31` `"Mistral Model Provider"` on the class → new:216 ✓
- `model-provider.bal:48-53` `"API Key"`, `"Model Type"`, `"Service URL"`, `"Maximum Tokens"`, `"Temperature"`, `"Connection Configuration"` on `init` params → new:218 ✓ (all six, correct parameter association)
- `model-provider.bal:178` `@display {label: "Expected type"}` on `generate`'s `td` → new:227 ✓

**`JsonSchema` annotation.** `to_json_schema.bal:32` declares `public annotation map<json> JsonSchema on type;`.
`new:232` renders it identically (name, type constraint `map<json>`, attachment point `type`). Correct.
It is the only `public annotation` in the module (`grep -nE '\bpublic\b'` over all four `.bal` files
returns exactly 5 hits: `ConnectionConfig`, `MISTRAL_AI_MODEL_NAMES`, `ModelProvider`, `init`, `JsonSchema`).

**`ai:Error?` return type.** `model-provider.bal:54` reads `) returns ai:Error? {`. `new` matches the
source spelling; `old`'s `ballerina/ai:1.13.0:Error?` was a synthetic fully-qualified form that is not
valid Ballerina. Correct improvement.

**Enum membership.** `types.bal:83-116` declares 32 members; both renders emit 32 `const string`
lines and 32 enum members. Counts match.

## 4. Regressions

**None found.**

Checked, specifically:

1. **Declaration loss** — declaration-set diff shows one addition, zero deletions (§2).
2. **Parameter loss** — `init` parameter list: 20 params in both sides, same names, same order, same
   defaults (`512`, `0.7`, `60`, `"disable"`, `true`, `{}`, `AUTO`, `HTTP_2_0`, `https://api.mistral.ai/v1`).
   `chat` (3 params) and `generate` (2 params) unchanged apart from the added annotation.
3. **Default-value loss** — the JSON diff contains no removal of any `"default"` key; every `"default"`
   line in the diff appears as unchanged context beside an inserted `annotations` block.
4. **Return-type loss** — `init`: `ai:Error?` (source-accurate, see §3). `chat`:
   `ai:ChatAssistantMessage|ai:Error` unchanged. `generate`: `td|ai:Error` unchanged.
5. **Doc loss** — all `#` doc comment lines identical; README block (render lines 7–60) is
   byte-identical between sides (`diff` on that range → IDENTICAL).
6. **`Special Agent Note` trailers** — preserved on all three lines that had them. One narrow
   observation: on the `init` line the trailer lists only the `ballerina/http` types, so in `new` the
   `ai:` prefix on `ai:Error?` carries no "FROM ballerina/ai package" hint, whereas `old` spelled the
   package out inside the type name. This is not a regression in accuracy — `ai:Error?` is exactly
   what the source writes, and the `chat`/`generate` lines two lines below both carry
   `Error FROM ballerina/ai package` — but it is the one respect in which `old` was more explicit.
7. **Malformed syntax newly introduced** — none. The three syntax problems in `new` (unquoted URL
   default, `AUTO`, trailing required `ConnectionConfig connectionConfig`) are character-for-character
   present in `old:201` as well.
8. **Section markers** — all four `old` markers survive; `new` adds a fifth.

## 5. Issues in `new` (independent of `old`)

All nine are also present in `old`; none is caused by spec v2. Listed because they misinform an LLM
consuming the render.

1. **`ConnectionConfig` field defaults are dropped and required fields become optional.**
   Source (`types.bal:22-79`) is a *closed* record `record {|…|}` in which five fields have defaults:
   `httpVersion = http:HTTP_2_0` (26), `timeout = 60` (38), `forwarded = "disable"` (42),
   `compression = http:COMPRESSION_AUTO` (54), `validation = true` (78). The render (new:131-174)
   emits an *open* record `record {` with all 15 fields marked `?` and no defaults. Both the
   closedness and the defaults are lost.
2. **Unquoted string default.** `new:218` renders `string serviceUrl = https://api.mistral.ai/v1`.
   The JSON holds `"default": "https://api.mistral.ai/v1"`; the renderer omits the quotes, producing
   non-compiling Ballerina.
3. **Wrong `Compression` default symbol.** `new:218` says `http:Compression compression = AUTO`.
   Source default is `http:COMPRESSION_AUTO` (`types.bal:54`). `AUTO` does not exist in `ballerina/http`.
4. **`generate` parameter type mangled.** Source (`model-provider.bal:178`) is
   `typedesc<anydata> td = <>`. Render: `anydata td = anydata`. Both the type (`typedesc<anydata>` →
   `anydata`) and the inferred-typedesc default (`<>` → the literal token `anydata`) are wrong.
5. **Included-record parameter duplicated.** Source `init` takes `*ConnectionConfig connectionConfig`
   (`model-provider.bal:53`). The render flattens the record's 15 fields into the parameter list *and*
   also appends `ConnectionConfig connectionConfig` — a required parameter placed after 18 defaultable
   ones, which is not legal Ballerina and implies 16 extra arguments that do not exist.
6. **Visibility and isolation modifiers dropped.** Source declares `public type ConnectionConfig`,
   `public enum MISTRAL_AI_MODEL_NAMES`, `public isolated client class ModelProvider`,
   `public isolated function init`, `isolated remote function chat/generate`. The render emits
   `type`, `enum`, `client class`, `function`, `remote function` with no `public` and no `isolated`
   (the sole exception being `public annotation JsonSchema`, which is rendered with `public`).
7. **Enum values detached from members and order reversed.** The enum body (new:178-211) lists bare
   member names with no `= "mistral-small-latest"` values, in exact reverse of declaration order
   (`types.bal:84-115` starts at `MISTRAL_SMALL_LATEST`; the render ends with it). The values are
   instead emitted as 32 free-standing `const string NAME = "value";` declarations (new:64-126) that
   do not exist as module-level constants in the library — the real module constants
   (`DEFAULT_MISTRAL_AI_SERVICE_URL`, `DEFAULT_MAX_TOKEN_COUNT`, `DEFAULT_TEMPERATURE` at
   `model-provider.bal:24-26`) are non-public and correctly omitted.
8. **Missing imports.** The header emits only `import ballerinax/ai.mistral;` (new:5) while the body
   uses `http:` and `ai:` prefixes throughout. The `// Special Agent Note` trailers partially
   compensate, but the render is not self-consistent as Ballerina.
9. **`*ai:ModelProvider` type inclusion not represented.** `model-provider.bal:33` includes the
   `ai:ModelProvider` object type in the class; the render gives no indication that `ModelProvider`
   is assignable to `ai:ModelProvider`, which is precisely how the README uses it
   (`final ai:ModelProvider mistralModel = check new mistral:ModelProvider(...)`, new:48).

## 6. Coverage gaps vs. the library

**Zero gaps.** `java21/package.json` `export` is `["ai.mistral"]` and the Central API reports
`modules: ['ai.mistral']` — a single module, no submodules, so the shared `getDefaultModule()`
limitation cannot bite here.

The default module's complete public surface is 4 symbols (`grep -nE '\bpublic\b'` over all four
`.bal` files):

| Public symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `ConnectionConfig` (type) | `types.bal:22` | yes | yes |
| `MISTRAL_AI_MODEL_NAMES` (enum, 32 members) | `types.bal:83` | yes | yes |
| `ModelProvider` (client class: `init`, `chat`, `generate`) | `model-provider.bal:32` | yes | yes |
| `JsonSchema` (annotation) | `to_json_schema.bal:32` | **no** | yes |

Nothing is absent from both renders. `JsonSchema` was absent from `old` only — that is the
improvement, not a gap.

## 7. Compiler plugin

`compiler-plugin.json` registers `io.ballerina.lib.ai.mistral.AiMistralCompilerPlugin`, which adds a
single **code modifier** (`AiMistralCodeModifier`), not an analyzer or code-action provider:

- `GenerateMethodModificationTask.java` (483 lines) walks `generate(...)` call sites, derives a JSON
  Schema for the inferred `td` type via `ballerina-to-openapi-2.3.0.jar` /
  `OpenAPISchema2JsonSchema`, and injects it at compile time. It recognises the
  `JsonSchema` annotation identifier (`SCHEMA_ANNOTATION_IDENTIFIER = "JsonSchema"`, lines 400, 448-469).
- `TypeMapperImplInitializer.java`, `AiMistralCompilerPlugin.java` (35 lines) are wiring only.
- The plugin reports no diagnostics of its own beyond bailing out when
  `compilation.diagnosticResult().errorCount() > 0` (line 99). No code actions, no generated
  Ballerina artifacts.

The one render-visible implication of the plugin is the `JsonSchema` annotation, which is the symbol
`new` newly surfaces and `old` omitted. So on this axis `new` is exactly right and `old` was
incomplete. Nothing else the plugin implies is missing from `new`.

## 8. Other considerations

- **Size/token impact:** render +21 lines / +1,018 bytes (+11.4%); JSON +3,989 bytes (+13.2%). Small
  in absolute terms. The `@display` labels are largely redundant with the field/parameter names they
  annotate (`"Timeout"` on `timeout`, `"Proxy Configuration"` on `proxy`), so the added tokens carry
  little information for an LLM — but they are faithful to the source and are what an IDE-oriented
  extractor is expected to emit.
- **Not deprecated.** Central API: `deprecated: None`, `deprecateMessage: ""`, `visibility: public`,
  `pullCount: 2073`, `ballerinaVersion: 2201.12.0`.
- **Stable version** (1.2.4), so no pre-1.0 caveat.
- **Doc quality in the library itself:** README typos survive into both renders verbatim —
  "nessary" (new:23), "Intialize" (new:40), and the step sequence jumps from "Step 1" to "Step 2" to
  "Step 4" (new:32, 40, 51). Not a render defect.
- **Doubled `#` in a doc comment:** `model-provider.bal:39` is `# # Initializes the Mistral AI model…`.
  Neither render shows it — the extractor drops `init`'s description entirely (the JSON keeps
  per-parameter descriptions but the `.bal.txt` emits no doc block above `init`), which is a
  pre-existing shared gap, not a `new` regression.
- **Parameter documentation is in the JSON but not the render.** `"description": "The Mistral AI API key"`
  etc. exist in both JSONs; `toSyntaxString` renders only the function-level description and an empty
  `# ` line. Shared behaviour, unchanged between sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -lc old/…bal.txt new/…bal.txt` | 211 / 8891 and 232 / 9909 |
| `wc -c old/*.json new/*.json` | 30,109 and 34,098 |
| `grep -c '^// Unknown type:'` both sides | 0 and 0 |
| `grep -cE ':[0-9]+\.[0-9]+\.[0-9]+:'` both sides | 1 and 0 |
| `grep -n '^// --- '` | old: 7,60,62,197 (4); new: 7,60,62,213,230 (5) |
| `diff <(sort old) <(sort new) \| grep -c '^[<>]'` | 25 |
| `diff <(sort old) <(sort new) \| grep '^<'` | 2 lines — old `init` and old `generate` signatures only |
| declaration-regex sets diff | 35 → 36; single addition `public annotation map` |
| `grep -oE '(remote )?function [a-zA-Z]+\('` both sides | identical: `init`, `chat`, `generate` |
| Python `json.dumps(sort_keys)` unified diff of the two JSONs | 235 lines; all inserts are `annotations` arrays; single value edit `ballerina/ai:1.13.0:Error?` → `ai:Error?` |
| JSON top-level counts | typeDefs 34/34, clients 1/1, functions 0/0, services 0/0, annotations 0/1 |
| JSON `typeDefs` name lists compared | identical, same order, no set difference |
| `readme` field vs `java21/docs/README.md` | equal (1,659 bytes); `new.readme == old.readme` True; `description` equal |
| `diff <(sed -n '7,60p' old) <(sed -n '7,60p' new)` | IDENTICAL |
| `git ls-remote --tags <repo>` | `v1.2.4` present → cloned `--depth 1 --branch v1.2.4`, HEAD `c553cae` |
| `diff -r src/ballerina <bala>/modules/ai.mistral` | only non-`.bal` extras differ; all 4 `.bal` files identical |
| `grep -nE '\bpublic\b' <bala>/modules/ai.mistral/*.bal` | 5 hits: `types.bal:22,83`, `model-provider.bal:32,48`, `to_json_schema.bal:32` |
| `grep -c '@display' <bala>/…/*.bal` | 24 lines (23 single-line + 1 multi-line opener at `model-provider.bal:29`) |
| `grep -o '@display' new/…bal.txt \| wc -l` | 24 |
| label multiset, source vs `new` | identical (22 distinct labels, `"Connection Configuration"` ×2) |
| `grep -c '^const string ' ` both sides | 32 and 32; source enum has 32 members (`types.bal:84-115`) |
| `types.bal:22` | `public type ConnectionConfig record {\|` — closed record (render shows open, no `public`) |
| `types.bal:26,38,42,54,78` | field defaults `http:HTTP_2_0`, `60`, `"disable"`, `http:COMPRESSION_AUTO`, `true` — absent from both renders |
| `model-provider.bal:48-54` | `init` signature incl. `*ConnectionConfig connectionConfig` and `returns ai:Error?` |
| `model-provider.bal:91` | `isolated remote function chat(… string? stop = ())` vs render `string\|() stop = ()` |
| `model-provider.bal:178` | `isolated remote function generate(ai:Prompt prompt, @display {label: "Expected type"} typedesc<anydata> td = <>)` |
| `cat compiler-plugin/compiler-plugin.json` | plugin id `ai-mistral-compiler-plugin`, class `AiMistralCompilerPlugin`, deps `ai.mistral-compiler-plugin-1.2.4.jar`, `ballerina-to-openapi-2.3.0.jar` |
| `wc -l compiler-plugin/src/.../ *.java` | 4 files, 601 lines; `GenerateMethodModificationTask.java` 483 |
| `grep -n 'JsonSchema\|Diagnostic\|CodeAction' GenerateMethodModificationTask.java` | `SCHEMA_ANNOTATION_IDENTIFIER = "JsonSchema"` (400), checks at 448/456/465/469; no diagnostics, no code actions |
| `ls <bala>/java21/modules` | single dir `ai.mistral` |
| `package.json` `export` | `["ai.mistral"]` |
| Central API `…/ballerinax/ai.mistral/1.2.4` | `modules: ['ai.mistral']`, `deprecated: None`, `visibility: public`, `pullCount: 2073`, `ballerinaVersion: 2201.12.0` |

## 10. Caveats and unverified items

- **Neither render was compiled.** Claims that specific rendered lines are "non-compiling Ballerina"
  (unquoted `https://…` default, `AUTO`, required parameter after defaultable ones) are from reading
  the grammar, not from running `bal build` on the render. The renders are documentation artifacts,
  not compilation units (they also lack the `ballerina/http` and `ballerina/ai` imports), so
  compiling them is not meaningful; the observations stand as accuracy problems regardless.
- **Cross-package types not checked against their own packages.** `http:Compression`,
  `ai:Prompt`, `ai:ChatMessage` etc. were verified only as the spellings the `ai.mistral` source uses.
  I did not open the `ballerina/http` 2.x or `ballerina/ai` 1.13.0 balas to confirm those symbols
  exist as rendered — except `http:COMPRESSION_AUTO` vs `AUTO`, where the discrepancy is visible
  entirely within `types.bal:54`.
- **Renderer/extractor code not read.** Which of the two spec-v2 stages (Java extractor vs
  TypeScript `toSyntaxString`) is responsible for each §5 defect is unattributed; I audited outputs
  against the library, not the pipeline.
- **`old`'s `mcp`-only renderer patch** (`service.methods ?? []`) is irrelevant here: this library has
  0 services in both JSONs.
- Everything else asserted in this report comes from a command listed in §9.

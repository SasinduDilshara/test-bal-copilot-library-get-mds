# ballerinax/ai.deepseek 1.1.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.deepseek` |
| Pinned version | `1.1.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.deepseek |
| Tag reviewed | `v1.1.4` (commit `e1e50b1f6adf30788fec8724b0ca1e335baaa499`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.deepseek/1.1.4` |
| Old render | `125` lines |
| New render | `144` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` for this library. The JSON diff contains exactly **two** removals
(`"annotations": []` → populated, and one changed `returnType.name`) and **no** dropped declaration,
parameter, default, doc line, or README byte. Spec v2 delivers three concrete gains:

1. `@display` annotations are now carried through — 15 on `ConnectionConfig` (1 type-level + 14
   field-level) and 7 on client-class parameters. All 22 match the library source verbatim.
2. The module's exported annotation `public annotation map<json> JsonSchema on type;` is emitted in a
   new `// --- Annotations ---` section. It was entirely absent from `old`, which had a 100% coverage
   gap on annotations.
3. The version-qualified type reference `ballerina/ai:1.13.0:Error?` is corrected to `ai:Error?`
   (version-qualified refs: 1 in `old`, 0 in `new`).

Zero regressions. Nine pre-existing render inaccuracies survive unchanged into `new` (section 5); they
are shared with `old` and are not caused by spec v2, but they are real and worth fixing.

## 2. Change inventory

Line counts: `old` 125, `new` 144 (`wc -l`). Unified diff: 21 added lines, 2 removed lines, 3 hunks.

### Top-level declarations

| Kind | old | new | Delta |
|---|---|---|---|
| `const` | 2 | 2 | 0 |
| `enum` | 1 | 1 | 0 |
| `type` (record) | 2 | 2 | 0 |
| `client class` | 1 | 1 | 0 |
| `annotation` | 0 | 1 | **+1 (`JsonSchema`)** |
| client methods | 3 (`init`, `chat`, `generate`) | 3 | 0 |
| **Total** | **6 + 3 methods** | **7 + 3 methods** | **+1** |

Section markers: `old` 4 (`README`, `END README`, `Types`, `Client`); `new` 5 (adds `Annotations`).

### Declarations modified (2)

| Location | old | new |
|---|---|---|
| `ModelProvider.init` return type | `ballerina/ai:1.13.0:Error?` | `ai:Error?` |
| `ConnectionConfig` + 6 params | no annotations | `@display {...}` on 15 record positions + 7 params |

### Declarations added (1)

`new:144` — `public annotation map<json> JsonSchema on type;`

### Declarations removed (0)

None. Verified by `diff -u old.pp.json new.pp.json | grep '^-'`, which returns exactly two lines:
`- "annotations": [],` and `- "name": "ballerina/ai:1.13.0:Error?"`.

> Note: the precomputed diff at `OLD_AND_NEW_DIFFS/ai.deepseek_diff.md` reports "Declarations added
> (0)". That is wrong — its extractor does not recognise `public annotation`. The `JsonSchema`
> annotation is a genuine added declaration. All other figures in that file (125/144 lines, 21/2,
> 3 hunks, 0 unknown types, 1→0 version-qualified refs, 4→5 markers) reproduce exactly.

### `@display` labels added in `new` — all 22 verified against source

Type-level: `ConnectionConfig` → `"Connection Configuration"` (`types.bal:26`).
Record fields (`types.bal:29–81`): HTTP Version, HTTP1 Settings, HTTP2 Settings, Timeout, Forwarded,
Pool Configuration, Cache Configuration, Compression, Circuit Breaker Configuration,
Retry Configuration, Response Limit Configuration, Secure Socket Configuration, Proxy Configuration,
Payload Validation — 14/14 exact string match.
`init` params (`model-provider.bal:44–49`): API Key, Model Type, Service URL, Maximum Token,
Temperature, Connection Configuration — 6/6 exact match.
`generate` param (`model-provider.bal:175`): `@display {label: "Expected type"}` — exact match.

## 3. Correctness against library source

The bala module sources and the `v1.1.4` upstream `ballerina/` sources are **byte-identical**
(`diff -q` on all four `.bal` files returned no output), so GitHub and the bala do not disagree here.

Everything `new` adds or changes is correct:

- `public annotation map<json> JsonSchema on type;` — `to_json_schema.bal:32` reads
  `public annotation map<json> JsonSchema on type;`. Identical, including the `map<json>` type
  constraint and the `on type` attachment point (JSON: `"attachmentPoint": "TYPE"`).
- `init` returns `ai:Error?` — `model-provider.bal:50` reads `) returns ai:Error? {`. The `new`
  rendering is right; `old`'s `ballerina/ai:1.13.0:Error?` was not valid Ballerina.
- All 22 `@display` labels — verified line by line above.

Unchanged items re-verified against source (not regressions, confirming `new` did not damage them):

- `ModelProvider` doc string matches `model-provider.bal:27`.
- `chat(ai:ChatMessage[]|ai:ChatUserMessage messages, ai:ChatCompletionFunctions[] tools, string|() stop = ())
  returns ai:ChatAssistantMessage|ai:Error` matches `model-provider.bal:88–89` (`string?` rendered as
  the equivalent `string|()`).
- `DeepseekChatResponseFunction {string name; string arguments;}` matches `types.bal:86–89`.
- `DEEPSEEK_CHAT = "deepseek-chat"`, `DEEPSEEK_REASONER = "deepseek-reasoner"` match `types.bal:21–22`.
- README block is byte-identical between `old` and `new` (JSON `readme` fields compare equal), and
  matches `docs/README.md` in the bala.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full unified diff of both renders — every `-` line has a corresponding `+` line that is a strict
  superset of it (the two `init` lines, the two `generate` lines). No content removed.
- Full pretty-printed, key-sorted JSON diff — only two `-` lines exist repo-side, both accounted for
  as improvements (empty annotations array replaced, version-qualified type name corrected).
- Declaration set comparison: identical `typeDefs` name list (5), identical client function list
  (`init`, `chat`, `generate`), identical `functions`/`services` counts (0/0).
- Parameter-level: `init` has the same 20 parameters with the same defaults in both; `chat` and
  `generate` parameter lists are unchanged apart from the added `@display`.
- Docs: `readme` and `description` compare equal between the two JSONs.
- Degraded types: `grep -c '^// Unknown type:'` = 0 in both, so spec v2 had nothing to repair here and
  nothing to break.

## 5. Issues in `new` (independent of `old`)

These are all inaccuracies vs. the library source that exist in `new`. Items 1–9 are also present in
`old` (shared renderer limitations, **not** spec-v2 regressions); item 10 is specific to `new`'s new
output.

1. **Unquoted string default — non-compiling.** `new:130`:
   `string serviceUrl = https://api.deepseek.com`. Source resolves `DEFAULT_DEEPSEEK_SERVICE_URL`
   (`model-provider.bal:23`) to `"https://api.deepseek.com"`; the quotes are stripped in the render.
   An LLM copying this emits invalid Ballerina.
2. **Wrong enum constant.** `new:130`: `http:Compression compression = AUTO`. Source is
   `http:COMPRESSION_AUTO` (`types.bal:60`). `AUTO` is not a resolvable symbol.
3. **Included-record parameter mangled.** Source is
   `@display {...} *ConnectionConfig connectionConfig` (`model-provider.bal:49`) — an included record
   parameter. The render drops the `*` and emits a *required* `ConnectionConfig connectionConfig`
   positioned after 19 defaultable parameters, which is both wrong semantics (it is not required) and
   invalid parameter ordering.
4. **`ConnectionConfig` shape wrong.** Source is a closed record `record {| |}` (`types.bal:27`) in
   which `httpVersion`, `timeout`, `forwarded`, `compression`, `validation` are required fields with
   defaults. The render emits an open `record { }` with **all 14 fields optional (`?`)** and no
   defaults. Both the closedness and the five defaults are lost.
5. **`generate` parameter type wrong.** Source: `typedesc<anydata> td = <>` (inferred typedesc,
   `model-provider.bal:175`). Render: `anydata td = anydata` — wrong type and a nonsensical default.
   This is materially misleading: the whole point of `generate` is the inferred typedesc argument.
6. **Enum flattened.** Source `public enum DEEPSEEK_MODEL_NAMES { DEEPSEEK_CHAT = "deepseek-chat",
   DEEPSEEK_REASONER = "deepseek-reasoner" }` (`types.bal:20–23`). Render hoists the values into two
   standalone `const string` declarations and leaves a value-less enum body with the members in
   reversed order (`DEEPSEEK_REASONER, DEEPSEEK_CHAT`).
7. **Qualifiers dropped.** `public` is stripped from `ConnectionConfig`, `DeepseekChatResponseFunction`,
   `DEEPSEEK_MODEL_NAMES` and `ModelProvider`; `isolated` is stripped from the class, `init`, `chat`
   and `generate`. Only the added `annotation` keeps `public`, making the render internally
   inconsistent about visibility.
8. **Parameter docs dropped.** Source has `# + apiKey - ...` etc. (`model-provider.bal:36–43`,
   `84–87`, `171–174`). The render keeps only the summary line and leaves a dangling empty `# ` line
   (`new:133`, `new:138`).
9. **`*ai:ModelProvider` inclusion not represented.** `model-provider.bal:29` declares
   `*ai:ModelProvider`. Neither render shows it, yet the README in the same render assigns the client
   to `ai:ModelProvider deepseekModel`. A consumer cannot tell from the API section why that is legal.
10. **`new`-only, minor:** the newly surfaced `deepseek:JsonSchema` annotation is real public API but
    is effectively dead for users — `to_json_schema.bal:37` reads `expectedResponseTypedesc.@ai:JsonSchema`
    (the `ballerina/ai` annotation), and the compiler plugin injects `ai:JsonSchema`, not
    `deepseek:JsonSchema` (`GenerateMethodModificationTask.java:399, 466–468`). Rendering it without
    that context could lead an LLM to write `@deepseek:JsonSchema`, which the runtime never reads.
    The render is faithful to the source; the ambiguity is inherited from the library.

## 6. Coverage gaps vs. the library

**0 missing public symbols in `new`.** `package.json` declares a single export, `ai.deepseek`, which
is the default module — there are **no submodules**, so the shared `getDefaultModule()` limitation does
not apply to this library.

Complete public-symbol set of the default module (`grep -nE '^public |^    public ' *.bal` in the bala):

| Symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `ModelProvider` (isolated client class) | `model-provider.bal:28` | yes | yes |
| `ModelProvider.init` | `model-provider.bal:44` | yes | yes |
| `ModelProvider.chat` (remote) | `model-provider.bal:88` | yes | yes |
| `ModelProvider.generate` (remote) | `model-provider.bal:175` | yes | yes |
| `DEEPSEEK_MODEL_NAMES` (enum) | `types.bal:20` | yes | yes |
| `ConnectionConfig` | `types.bal:27` | yes | yes |
| `DeepseekChatResponseFunction` | `types.bal:86` | yes | yes |
| `JsonSchema` (annotation) | `to_json_schema.bal:32` | **no** | yes |

So `old` had one coverage gap; `new` has none. Not a symbol, but unrepresented in both: the
`*ai:ModelProvider` type inclusion (section 5, item 9).

Correctly excluded from both renders: the ~20 non-public types in `types.bal`
(`DeepSeekChatCompletionRequest`, `DeepseekTool`, `DeepSeekUsage`, …), the module-private `JsonSchema`
/ `JsonArraySchema` records in `to_json_schema.bal`, and all `isolated function` helpers.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.lib.ai.deepseek.AiDeepseekCompilerPlugin`
with two jars (`ai.deepseek-compiler-plugin-1.1.4.jar`, `ballerina-to-openapi-2.3.0.jar`).

What it does (upstream `compiler-plugin/src/main/java/io/ballerina/lib/ai/deepseek/`):

- `AiDeepseekCompilerPlugin.java:31` registers a single `CodeModifier` — no code analyzers, so the
  plugin contributes **no diagnostics and no code actions**, only source modification.
- `GenerateMethodModificationTask` walks calls to `ModelProvider.generate`, derives an OpenAPI schema
  for the inferred typedesc via `ballerina-to-openapi`, converts it with `OpenAPISchema2JsonSchema`
  (`:288–294`), and attaches `@ai:JsonSchema {…}` to the corresponding type definition
  (`TypeDefinitionModifier`, `:398–470`), adding a `ballerina/ai` import where needed (`:432`).

Render implications: the plugin's contribution is entirely automatic and build-time — there is no
user-facing symbol it implies that is absent from `new`. The one thing worth noting is the mismatch in
section 5 item 10: the plugin writes `ai:JsonSchema`, while the annotation `new` now advertises is
`deepseek:JsonSchema`. Nothing the plugin implies is missing from the render.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/ai.deepseek/1.1.4`: `"deprecated": null`,
  `"deprecateMessage": ""`, `"visibility": "public"`, 2,020 pulls, built on Ballerina `2201.12.0`.
- **Stable version** (1.1.4, post-1.0), single module, `graalvmCompatible: true`.
- **Size/token impact is negligible**: +19 lines (+15.2%), all of it annotations plus one
  declaration. No token-budget concern for a 144-line render.
- **Doc quality inherited from the library, not the renderer**: the README rendered in both sides
  contains "the nessary configuration" (typo), an empty gap where prerequisites should be, and jumps
  from "Step 1"/"Step 2" straight to "Step 4". Source `model-provider.bal:36–41` also documents a
  parameter named `model` that does not exist (it is `modelType`) and misspells `temperateure`.
  Worth reporting upstream; out of scope for this regression review.
- The `new` render is still not compilable Ballerina (section 5 items 1–3), but neither is `old`, and
  `new` is strictly closer to the source.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 125 / 144 |
| 2 | `git ls-remote --tags <repo>` | `v1.1.4` → `e1e50b1f6adf30788fec8724b0ca1e335baaa499` |
| 3 | `git clone --depth 1 --branch v1.1.4 <repo> src` | OK, exact tag |
| 4 | `diff -q` bala `modules/ai.deepseek/*.bal` vs `src/ballerina/*.bal` (4 files) | identical, no output |
| 5 | `diff -u old/*.bal.txt new/*.bal.txt` | 3 hunks; 21 added, 2 removed lines |
| 6 | `diff -u old.pp.json new.pp.json \| grep '^-'` | exactly 2 lines: `"annotations": []`, `"name": "ballerina/ai:1.13.0:Error?"` |
| 7 | JSON `typeDefs` names, both sides | identical 5: `DEEPSEEK_CHAT`, `DEEPSEEK_REASONER`, `DEEPSEEK_MODEL_NAMES`, `ConnectionConfig`, `DeepseekChatResponseFunction` |
| 8 | JSON `clients[0].functions` names, both sides | identical 3: `init`, `chat`, `generate` |
| 9 | JSON `annotations` length | old 0, new 1 (`JsonSchema`, `TYPE`, `map<json>`) |
| 10 | JSON `readme` / `description` equality old vs new | `True` / `True` |
| 11 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 12 | `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | old 1, new 0 |
| 13 | `grep -n '^// --- '` both renders | old 4 markers, new 5 (adds `Annotations` at `new:142`) |
| 14 | `grep -nE '^(public )?(type\|const\|enum\|client class\|class\|annotation\|...)' new` | 7 top-level declarations (listed §2) |
| 15 | `grep -nE '^public \|^    public ' bala/*.bal` | 6 public symbols + 2 remote methods (table §6) |
| 16 | `bala/.../to_json_schema.bal:32` | `public annotation map<json> JsonSchema on type;` — matches `new:144` |
| 17 | `bala/.../model-provider.bal:44–50` | 6 `@display` labels + `returns ai:Error?` — match `new:130` |
| 18 | `bala/.../model-provider.bal:175` | `typedesc<anydata> td = <>` with `@display {label: "Expected type"}` |
| 19 | `bala/.../types.bal:26–81` | 1 + 14 `@display` labels, closed record, 5 defaults |
| 20 | `bala/.../types.bal:20–23` | enum with values `deepseek-chat` / `deepseek-reasoner` |
| 21 | `cat compiler-plugin/compiler-plugin.json` | 1 plugin class, 2 jars |
| 22 | `AiDeepseekCompilerPlugin.java:31` | `addCodeModifier` only — no analyzer/code actions |
| 23 | `GenerateMethodModificationTask.java:399, 466–468` | injects `<aiPrefix>:JsonSchema`, aiPrefix defaults to `ai` |
| 24 | `cat package.json` | `"export": ["ai.deepseek"]` — single module, no submodules |
| 25 | `curl api.central.ballerina.io/.../ballerinax/ai.deepseek/1.1.4` | not deprecated, 1 module, 2020 pulls |
| 26 | Cross-check of `OLD_AND_NEW_DIFFS/ai.deepseek_diff.md` | all counts reproduce; its "Declarations added (0)" is incorrect |

## 10. Caveats and unverified items

- The compiler plugin was reviewed from **upstream Java source at tag `v1.1.4`**, not by decompiling
  the shipped `ai.deepseek-compiler-plugin-1.1.4.jar`. The `.bal` sources in the bala are byte-identical
  to upstream at that tag, which is strong indirect evidence the jar matches, but the jar bytes
  themselves were not verified.
- Native behaviour in `ai.deepseek-native-1.1.4.jar` (`generateJsonSchemaForTypedescNative`,
  `getArrayMemberType`, `containsNil`, `Generator.generate`) was not inspected. It has no bearing on
  the render, which is built from Ballerina signatures only.
- I did not re-run the two-stage render pipeline; the audit compares the provided artifacts as-is.
  The claim that both sides used the same pinned version rests on the brief's `PIN_OK` statement plus
  the fact that both JSONs carry an identical `name`, `description` and `readme` — I found no
  contrary evidence.
- Whether the nine shared inaccuracies in section 5 are fixed elsewhere in spec v2 for other
  libraries was not investigated; this review is scoped to `ai.deepseek`.

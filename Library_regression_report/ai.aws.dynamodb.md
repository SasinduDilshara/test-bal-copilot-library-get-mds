# ballerinax/ai.aws.dynamodb 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.aws.dynamodb` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.aws.dynamodb |
| Tag reviewed | `v1.0.0` (commit `8d9b35ce1cb5a074c5bc2cefa2371c1c572d1bd2`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.aws.dynamodb/1.0.0` |
| Old render | `143` lines |
| New render | `225` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The package exports exactly one module (`ai.aws.dynamodb`, `package.json` `export` list) with three
public symbols: `Error`, `TableConfig`, `ShortTermMemoryStore`. `old` rendered only `TableConfig`;
`Error` and `ShortTermMemoryStore` both degraded to `// Unknown type:` placeholders, so the entire
14-method public API of the store class was invisible. `new` emits real definitions for all three,
adds all 13 `@display` annotations from the source, and drops zero content: the README block and the
`TableConfig` body are byte-identical between the two sides. No regression found.

`new` introduces one genuine defect of its own: a double module prefix (`ai:ai:`) in the `getAll`
return type, which makes that one line non-compiling Ballerina. Everything else flagged below is a
pre-existing renderer convention shared by both sides.

## 2. Change inventory

Line counts (`wc -l`): old `143`, new `225` (+82).

`// Unknown type:` placeholders (`grep -c '^// Unknown type:'`): old `2`, new `0`.

Section markers (`grep -n '^// --- '`): 3 on both sides (`README`, `END README`, `Types`).

| Kind | old | new | delta |
|---|---|---|---|
| Error type definition | 0 (placeholder `// Unknown type: Error`) | 1 (`type Error error;`) | +1 |
| Record type | 1 (`TableConfig`, 8 fields) | 1 (`TableConfig`, 8 fields) | 0 |
| Class | 0 (placeholder `// Unknown type: ShortTermMemoryStore`) | 1 (`class ShortTermMemoryStore`) | +1 |
| Class methods rendered | 0 | 14 | +14 |
| `@display` annotation occurrences | 0 | 13 | +13 |
| `Special Agent Note` cross-package markers | 3 | 11 | +8 |
| README lines | 92 (+ blank) | 92 (+ blank) | 0 |
| Declarations removed | — | — | 0 |

The 14 methods added: `init`, `getChatSystemMessage`, `getChatInteractiveMessages`, `getAll`, `put`,
`removeChatSystemMessage`, `removeChatInteractiveMessages`, `removeAll`, `isFull`, `getCapacity`,
`putCheckpoint`, `getCheckpoint`, `removeCheckpoint`, `takeCheckpoint`.

Root cause of the improvement, from the JSONs: the `ShortTermMemoryStore` typeDef node in
`old/…json` already carried the full `functions` array but had **no `type` field**; `new/…json` sets
`"type": "Class"`. `main`'s `renderTypeDef` therefore had no branch to take and fell through to the
placeholder. Likewise `Error` gained `"baseType": "error"`. `new` also adds `annotations` arrays to
the class, the record, record fields, and `init` parameters — absent from `old/…json` entirely.

## 3. Correctness against library source

Upstream `ballerina/store.bal` and `ballerina/types.bal` at tag `v1.0.0` are byte-identical to the
bala's `modules/ai.aws.dynamodb/*.bal` (`diff -q`, no output), so GitHub and the bala agree.

Public surface in the bala (`grep -nE '^\s*public'` on `store.bal`; `types.bal` has no public
symbols): `Error` (L24), `TableConfig` (L52), `ShortTermMemoryStore` (L137) plus its 14 public
methods at L153, 194, 219, 234, 248, 290, 309, 340, 357, 366, 374, 401, 430, 449. `new` renders all
14, in source order, with matching names.

Spot checks of what `new` adds:

- `init` — source L153–155: `public isolated function init(@display {label: "Database Connection"}
  dynamodb:ConnectionConfig|dynamodb:Client dbConnection, @display {label: "Max Messages Per Key"}
  int maxMessagesPerKey = 20, @display {label: "Table Configuration"} TableConfig tableConfig = {})
  returns Error?`. Render L157 matches exactly, including both defaults (`20`, `{}`) and all three
  parameter `@display` labels. ✔
- `put` — source L248: `put(string key, ai:ChatMessage|ai:ChatMessage[] message) returns Error?`.
  Render L174 expands to `ai:ChatUserMessage|ai:ChatSystemMessage|ai:ChatAssistantMessage|
  ai:ChatFunctionMessage|ai:ChatMessage[]`. Verified equivalent: `ballerina/ai` 1.13.0 (the resolved
  dependency per `dependency-graph.json`) defines at `model-provider.bal:79`
  `public type ChatMessage ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage`.
  Semantically correct. ✔
- `getChatInteractiveMessages` — source L219 returns `ai:ChatInteractiveMessage[]|Error`; render
  L166 matches. ✔
- `removeChatInteractiveMessages` — source L309 `(string key, int? count = ())`; render L183
  `(string key, int|() count = ())` — equivalent, default preserved. ✔
- `getCheckpoint` / `takeCheckpoint` — source L401 / L449 return `ai:PendingApproval?|Error`; render
  L213 / L224 `ai:PendingApproval|()|Error`. Equivalent. ✔
- `getCapacity` — source L366 `returns int`; render L199 matches. ✔
- `@display` annotations: 13 occurrences in `store.bal`, 13 in the new render (`grep -o '@display' |
  wc -l` = 13 on both). Labels compared by eye against L51–L67, L136, L153–155 — all match. ✔
- `Error` — source L24 `public type Error distinct ai:MemoryError;`; render L105 `type Error error;`.
  Correct as far as it goes but lossy (see §5.2). ✚

## 4. Regressions

**None found.**

What was checked to conclude that:

- `diff` of the README block (render lines 7–99) between old and new: identical (only a trailing
  blank line differs in the new file). The block also matches the bala's `docs/README.md` (92 lines)
  line-for-line.
- Precomputed diff reports `Declarations removed: 0`; verified independently — the unified diff's
  only two `-` lines are the two `// Unknown type:` placeholders, both replaced by real definitions.
- `TableConfig`: same 8 fields, same order, same types, same doc text on both sides; `new` only
  interleaves `@display` lines. No field, type, doc line, or `Special Agent Note` was dropped.
- No version/module-qualified refs (`mod:1.2.3:Type`) exist on either side (0 matches both files),
  so nothing was gained or lost there.
- No declaration present in `old` is absent from `new`.

## 5. Issues in `new` (independent of `old`)

1. **Malformed double module prefix — `new` only.** Render L170:
   `function getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|…`.
   Source L234–235 is `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]`. Traced to the
   renderer, not the extractor: `new/…json` holds the type name
   `"[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error"` — the
   tuple text already carries `ai:` prefixes while the union member is bare — plus a link
   `{category: external, recordName: ChatInteractiveMessage, libraryName: ballerina/ai}`. The
   renderer prefixes every occurrence of the linked name, so the already-qualified occurrence inside
   the tuple becomes `ai:ai:`. This is the only non-compiling token introduced by `new`.
   Related: the `Special Agent Note` on that line lists only `ChatInteractiveMessage`; the
   `ChatSystemMessage` origin is not declared, because it has no link entry in the JSON.
2. **`distinct ai:MemoryError` derivation lost.** Source L24 makes `Error` a distinct subtype of
   `ai:MemoryError` (itself `distinct Error` at `ballerina/ai` `error.bal:96`). `new` renders
   `type Error error;`. An LLM reading this cannot tell the store's errors are `ai:MemoryError`
   values, which matters for `is ai:MemoryError` narrowing. Strictly an improvement over `old`'s
   nothing, but incomplete. The JSON node carries only `"baseType": "error"` — the information is
   dropped at extraction, not rendering.
3. **Object-type inclusion `*ai:ShortTermMemoryStore` lost.** Source L138. The class implements the
   `ballerina/ai` store contract; this is the reason the README's examples assign it to an
   `ai:ShortTermMemoryStore` variable. The string `inclusion`/`include` does not appear anywhere in
   `new/…json`, so the render cannot show it. An LLM sees a standalone class with no stated
   relationship to `ai:ShortTermMemoryStore`, contradicting the README that sits 60 lines above.
4. **`TableConfig` shape and defaults wrong — shared with `old`.** Source L52 is a **closed** record
   `public type TableConfig record {| … |}` whose 8 fields all have **defaults**
   (`tableName = "chat_memory"`, `createTableIfNotExists = true`,
   `billingMode = dynamodb:PAY_PER_REQUEST`, `readCapacityUnits = 5`, `writeCapacityUnits = 5`,
   `consistentReads = false`, `tags = ()`, `sseSpecification = ()`). Both renders emit an **open**
   `record { … }` with every field marked optional (`string tableName?;`) and **no default values**.
   Both JSONs set `"optional": true` with no `default` key on all 8 fields (`default` appears only on
   `init` parameters). The literal `chat_memory` occurs exactly once in `new/…json` — in the README
   text, not in the type model.
5. **Doc-comment continuation lines are not `#`-prefixed — shared with `old`.** e.g. render L113
   `Must be 3-255 characters long and contain only letters, digits, underscores, dots, and hyphens`
   sits inside the record body with no `#`. Affects 6 of the 8 field docs. Non-compiling as written.
6. **Qualifiers dropped — shared convention.** `public`, `isolated`, and `distinct` never appear in
   either render; the class body uses object-type method syntax (`function f(...) returns T;` with no
   body). Consistent across the whole corpus, listed here for completeness rather than as a defect
   specific to this library.

## 6. Coverage gaps vs. the library

**None.** `package.json` `export` lists a single module, `ai.aws.dynamodb`; the bala's `modules/`
directory contains only `ai.aws.dynamodb` (files `store.bal`, `types.bal`). There is no submodule
API, so the shared `getDefaultModule()` limitation is inert for this package.

All 3 public symbols of the default module appear in `new`. `types.bal` (203 lines) declares only
module-private types (`Prompt`, `ChatUserMessageDatabaseMessage`, `ChatSystemMessageDatabaseMessage`,
`ChatMessageDatabaseMessage`, `ChatInteractiveMessageDatabaseMessage`, `IterationDatabaseMessage`,
`ApprovalDatabaseMessage`) and private functions — correctly excluded from both renders. The class's
`private final` fields (`dynamodbClient`, `maxMessagesPerKey`, `tableName`, `consistentReads`,
`store.bal` L140–143) are likewise correctly absent.

`old`, by contrast, has an effective coverage gap of 2 of 3 public symbols (14 methods invisible).

## 7. Compiler plugin

The package ships **no compiler plugin**. Evidence: the bala contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/compiler-plugin.json`; and `find . -iname '*compiler-plugin*'` over the v1.0.0
clone returns nothing. Nothing plugin-derived is therefore expected in, or missing from, the render.

Validation that a plugin might otherwise have surfaced is done at runtime instead — `init` rejects
bad table names via `isValidTableName` (`store.bal` L156–160, L913) — and that behaviour is visible
in the render only through the `tableName` doc text ("Must be 3-255 characters long…"), which both
renders carry.

## 8. Other considerations

- Version `1.0.0` is a first stable release; `bala.json`/`package.json` show no deprecation flag and
  Central metadata was not contradicted. `graalvmCompatible: true`, `ballerina_version 2201.12.0`.
- Size: +82 lines (~57%) for the full public API of the store. Token cost is negligible; the render
  is 225 lines total. This is a high-value-per-token improvement — the README already tells an LLM to
  call `new dynamodb:ShortTermMemoryStore(...)`, and `old` gave it no constructor signature to work
  from.
- The `getAll` return type is genuinely awkward (`[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]
  |ai:ChatInteractiveMessage[]|Error`); the `ai:ai:` corruption lands on exactly the type an LLM is
  most likely to need to destructure, so it is worth fixing despite being a single token.
- Source doc comments use `# + return -` (singular) rather than `# + returns -` on several methods
  (e.g. `store.bal` L233, L247); return descriptions are captured in the JSON regardless but are not
  emitted by either renderer.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags <repo>` | single tag `v1.0.0` → `8d9b35ce…` (peeled) |
| `git clone --depth 1 --branch v1.0.0 … src` | OK, HEAD `8d9b35ce1cb5a074c5bc2cefa2371c1c572d1bd2` |
| `diff -q src/ballerina/store.bal <bala>/modules/ai.aws.dynamodb/store.bal` | no output (identical) |
| `diff -q src/ballerina/types.bal <bala>/modules/ai.aws.dynamodb/types.bal` | no output (identical) |
| `find src -iname '*compiler-plugin*'` | no matches |
| `ls -R <bala>` | `any/{bala.json,dependency-graph.json,docs,modules,package.json}`; `modules/ai.aws.dynamodb/{store.bal,types.bal}` |
| `wc -l <bala>/modules/ai.aws.dynamodb/*.bal` | store.bal 944, types.bal 203 |
| `cat <bala>/package.json` | `export: ["ai.aws.dynamodb"]`, version 1.0.0, ballerina_version 2201.12.0 |
| `wc -l old/*.bal.txt new/*.bal.txt` | 143 / 225 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- '` old / new | 3 / 3 markers |
| `grep -o '@display' new/*.bal.txt \| wc -l` | 13 |
| `grep -o '@display' <bala>/…/store.bal \| wc -l` | 13 |
| `grep -c 'Special Agent Note'` old / new | 3 / 11 |
| `grep -c '^    function ' new/*.bal.txt` | 14 |
| `grep -nE '^\s*public' <bala>/…/store.bal` | `Error` L24, `TableConfig` L52, class L137, 14 public methods L153–L449 |
| `diff` of render lines 7–99, old vs new | identical |
| `diff <bala>/docs/README.md` vs new render README block | only a trailing blank line |
| JSON typeDef `type` field, old vs new | old: `Error`, `Record`, **absent**; new: `Error`, `Record`, `Class` |
| JSON `Error` node, old vs new | new adds `"baseType": "error"` |
| JSON `TableConfig` field keys, old vs new | new adds `annotations`; neither has `default` |
| JSON search for `inclusion`/`include`/`isolated`/`public`/`MemoryError` | 0 occurrences each |
| JSON `getAll` return type name (new) | `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|ChatInteractiveMessage[]\|Error` with one `ChatInteractiveMessage` link |
| `grep 'public type ChatMessage ' <ai-1.13.0-bala>/modules/ai/model-provider.bal` | L79: union of the 4 message types — confirms `put` expansion |
| `grep 'public type MemoryError ' <ai-1.13.0-bala>/modules/ai/error.bal` | L96: `distinct Error` |
| `dependency-graph.json` | `ballerina/ai` resolved at `1.13.0` |

Bala root abbreviated above as `<bala>` =
`/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.aws.dynamodb/1.0.0/any`.

## 10. Caveats and unverified items

- The claim that the `ai:ai:` duplication originates in `toSyntaxString` rather than the Java
  extractor is inferred from the JSON contents (tuple text already prefixed + a link on the same
  name), not from reading the renderer source, which was not in scope for this review. The
  *observable* defect in the render is verified directly.
- Central registry metadata was not re-queried over HTTP; package identity, version, module list, and
  absence of deprecation were taken from the bala's `package.json` / `bala.json`, which the brief
  designates as authoritative for what the pipeline consumed.
- Doc-string text equality between render and source was verified by reading both, not by an
  automated character-level diff (the render reflows `#`-stripped doc lines, so a mechanical diff is
  not meaningful).
- Whether the renderer *intends* to drop `public`/`isolated`/`distinct` qualifiers and record
  closedness (§5.4, §5.6) is a design question about the pipeline; this review only records that the
  rendered text differs from the library source there, identically on both sides.

# ballerinax/ai.memory.mssql 1.3.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.memory.mssql` |
| Pinned version | `1.3.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.memory.mssql |
| Tag reviewed | `v1.3.0` (annotated, `f7ed7c86` -> `6d25093e`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.memory.mssql/1.3.0` |
| Old render | `108` lines |
| New render | `171` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module library: the default module exports exactly three public symbols
(`Error`, `DatabaseConfiguration`, `ShortTermMemoryStore`). `old` rendered only one of them
(`DatabaseConfiguration`); the other two collapsed to `// Unknown type:` stubs, which meant the
entire public API surface — the 14 public methods of `ShortTermMemoryStore` — was invisible to any
LLM consuming the render. `new` emits the error typedef and the full class with all 14 methods,
their doc comments, parameter defaults and return types, all verified against the published source.

Nothing that was present and correct in `old` is missing, truncated, or degraded in `new`: the
diff is strictly two removals (`// Unknown type: Error`, `// Unknown type: ShortTermMemoryStore`)
replaced by real definitions. README section, module header, and the `DatabaseConfiguration`
record are byte-identical between the two sides.

One real defect exists in `new` only: `getAll`'s return type is emitted as
`[ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]` — a doubled `ai:` module prefix, which
is non-compiling Ballerina. It is not a regression (the method did not exist in `old` at all) but
it is a renderer bug worth filing.

## 2. Change inventory

Line counts (`wc -l`): old **108**, new **171** (+63 net; +65 added, −2 removed, 2 hunks).

`// Unknown type:` placeholders: old **2**, new **0** (`grep -c`).
Version/module-qualified refs (`mod:1.2.3:Type`): old **0**, new **0** in the render text
(they existed in the old JSON only — see below).

| Kind | old | new | delta |
|---|---|---|---|
| Rendered record types | 1 (`DatabaseConfiguration`) | 1 | 0 |
| Rendered error typedefs | 0 (stub) | 1 (`Error`) | +1 |
| Rendered classes | 0 (stub) | 1 (`ShortTermMemoryStore`) | +1 |
| Class methods rendered | 0 | 14 | +14 |
| Free functions / clients / services / annotations | 0 | 0 | 0 |
| README section lines | 73 | 73 | 0 |

Declarations added in `new` (16 total): `type Error`, `class ShortTermMemoryStore`, and its
methods `init`, `getChatSystemMessage`, `getChatInteractiveMessages`, `getAll`, `put`,
`removeChatSystemMessage`, `removeChatInteractiveMessages`, `removeAll`, `isFull`, `getCapacity`,
`putCheckpoint`, `getCheckpoint`, `removeCheckpoint`, `takeCheckpoint`.

Declarations removed: **none**.

JSON-level diff (both JSONs normalised and sorted; only 4 changes in 21 KB):
1. `Error` typeDef gains `"baseType": "error"`.
2. `ShortTermMemoryStore` typeDef gains `"type": "Class"` — this alone is what unblocks the
   renderer; the 14 functions were already present in the **old** JSON but `renderTypeDef` on
   `main` had no `Class` branch and fell through to `// Unknown type:`.
3. `init` return type de-qualified: `ballerinax/ai.memory.mssql:1.3.0:Error?` -> `Error?`.
4. `getAll` return type de-qualified: `[ballerina/ai:1.13.0:ChatSystemMessage, ballerina/ai:1.13.0:ChatInteractiveMessage...]|...`
   -> `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|...`.

Change 4 is the direct cause of the `ai:ai:` defect: the JSON now already carries an `ai:` prefix
inside the tuple, and the renderer's link-based prefixing (driven by the `ChatInteractiveMessage`
external link) prepends a second one.

## 3. Correctness against library source

Upstream `v1.3.0` `ballerina/store.bal` and `ballerina/types.bal` are **byte-identical** to the
bala's `modules/ai.memory.mssql/store.bal` and `types.bal` (`diff` exit 0), so GitHub and the bala
agree and either can be cited.

All 14 public methods verified one-for-one against `store.bal` (bala path
`.../modules/ai.memory.mssql/store.bal`):

| Render (new) | Source line | Source signature | Match |
|---|---|---|---|
| `init(mssql:Client\|DatabaseConfiguration mssqlClient, int maxMessagesPerKey = 20, cache:CacheConfig\|() cacheConfig = (), string tableName = "ChatMessages", string checkpointTableName = "Checkpoints") returns Error?` | 82–86 | identical modulo `public isolated` and `?`->`\|()` | yes |
| `getChatSystemMessage(string key) returns ai:ChatSystemMessage\|Error\|()` | 122 | `returns ai:ChatSystemMessage\|Error?` | yes |
| `getChatInteractiveMessages(string key) returns ai:ChatInteractiveMessage[]\|Error` | 163 | same | yes |
| `getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | 187–188 | `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | **no — doubled prefix** |
| `put(string key, ai:ChatUserMessage\|ai:ChatSystemMessage\|ai:ChatAssistantMessage\|ai:ChatFunctionMessage\|ai:ChatMessage[] message) returns Error\|()` | 213 | `ai:ChatMessage\|ai:ChatMessage[] message` | yes (union expanded) |
| `removeChatSystemMessage(string key) returns Error\|()` | 330 | same | yes |
| `removeChatInteractiveMessages(string key, int\|() count = ()) returns Error\|()` | 360 | `int? count = ()` | yes |
| `removeAll(string key) returns Error\|()` | 412 | same | yes |
| `isFull(string key) returns boolean\|Error` | 452 | same | yes |
| `getCapacity() returns int` | 625 | same | yes |
| `putCheckpoint(ai:PendingApproval approval) returns Error\|()` | 633 | same | yes |
| `getCheckpoint(string sessionId) returns ai:PendingApproval\|()\|Error` | 658 | `ai:PendingApproval?\|Error` | yes |
| `removeCheckpoint(string sessionId) returns Error\|()` | 683 | same | yes |
| `takeCheckpoint(string sessionId) returns ai:PendingApproval\|()\|Error` | 702 | `ai:PendingApproval?\|Error` | yes |

The `put` expansion is sound: `ballerina/ai` 1.13.0 `model-provider.bal:79` defines
`public type ChatMessage ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage`,
so `ChatMessage|ChatMessage[]` == the rendered union. `ChatInteractiveMessage` at
`model-provider.bal:83` likewise checks out.

Method count: `grep -c 'function ' new render` = **14**; `grep -c '    public isolated function' store.bal` = **14**. No public method omitted, none invented.

Doc comments in the class body match the source doc comments verbatim (e.g. the three-line
`removeAll` note about atomic session clearing, `store.bal:406–411`).

`DatabaseConfiguration` (rendered identically in both sides) matches `store.bal:30–46` on field
names, types and doc strings — with the caveats in §5.

README: render lines 8–80 are byte-identical to `docs/README.md` in the bala (only a trailing
newline differs), and identical between `old` and `new`.

## 4. Regressions

**None found.**

What I checked to conclude that:
- Full `diff -u old new` on the renders: exactly 2 hunks, 2 lines removed, both of them
  `// Unknown type:` placeholders. No declaration, parameter, default, return type, doc line, or
  README line disappears.
- `diff` of the two normalised JSONs: 4 changed keys, all additive or de-qualifying; nothing
  dropped.
- README section extracted from both renders and diffed: identical.
- `DatabaseConfiguration` block compared line-by-line across sides: identical, including both
  `Special Agent Note` annotations for `mssql:Options` and `sql:ConnectionPool`.
- Version-qualified refs: `old` render had 0 in text; nothing was lost by the JSON de-qualification.

## 5. Issues in `new` (independent of `old`)

1. **Malformed type — doubled module prefix (new-only, would not compile).**
   `new` line 125: `returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|...`.
   Source (`store.bal:188`) is `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]`. Caused by the
   JSON now storing an already-prefixed tuple (`new` JSON `getAll.return.type.name`) while the
   renderer still applies its own `ai:` prefix from the `ChatInteractiveMessage` external link.
   Only occurrence in the file; the sibling `ai:ChatInteractiveMessage[]` in the same union is
   correct.
2. **`Error` loses its parentage.** `new` renders `type Error error;`; source (`store.bal:25`) is
   `public type Error distinct ai:MemoryError;`. The `distinct` qualifier and the `ai:MemoryError`
   base are dropped, so an LLM cannot tell this error is assignable to `ai:MemoryError`. Still a
   large net gain over `old`'s `// Unknown type: Error`.
3. **Class doc is the constructor's doc, not the class's.** `new` line 109 attaches
   `# Initializes the MS SQL-backed short-term memory store.` to `class ShortTermMemoryStore`. The
   class's actual doc (`store.bal:54`) is
   `# Represents an MS SQL-backed short-term memory store for messages.` The extractor put `init`'s
   description into the class-level `description` field (present in the **old** JSON too, just never
   rendered).
4. **`*ai:ShortTermMemoryStore` inclusion not represented.** `store.bal:56` includes the
   `ai:ShortTermMemoryStore` object type; neither JSON has any field for type inclusions, so the
   render never states that this class satisfies the `ai` memory-store contract — which is precisely
   the fact the README's examples rely on (`ai:ShortTermMemoryStore store = check new mssql:ShortTermMemoryStore(...)`).
   Shared extractor gap, but only visible now that the class renders.
5. **`DatabaseConfiguration` rendered as an open record.** Source (`store.bal:30`) is closed:
   `record {| ... |}`. Both renders emit `record { ... }`. Shared with `old`.
6. **`DatabaseConfiguration` field defaults lost.** Source has `string host = "localhost"`,
   `string user = "sa"`, `int port = 1433`; both renders show them as `string host?;`, `string user?;`,
   `int port?;` — defaulted-and-therefore-optional, but the actual default values are gone. Shared
   with `old`. (Contrast: method parameter defaults *are* preserved, e.g. `maxMessagesPerKey = 20`.)

## 6. Coverage gaps vs. the library

Default module public symbols (`grep -n public store.bal types.bal`): `Error` (store.bal:25),
`DatabaseConfiguration` (store.bal:30), `ShortTermMemoryStore` (store.bal:55). The two `public final`
hits in `types.bal:109–110` are fields of a non-public class and correctly not exported.

- Present in `new`: all 3. **Coverage gaps in `new`: 0.**
- Present in `old`: 1 (`DatabaseConfiguration`); 2 degraded to stubs.
- Submodule-only API: **none**. `package.json` `export` is `["ai.memory.mssql"]` and the bala has a
  single `modules/ai.memory.mssql` directory, so the `getDefaultModule()`-only extraction loses
  nothing here. Central metadata confirms one module.

## 7. Compiler plugin

**No compiler plugin.** `find` over the `v1.3.0` clone for `*compiler-plugin*` returns nothing, the
repo has no `compiler-plugin/` Gradle subproject (only `ballerina/` and `build-config/`), and the
bala contains no `compiler-plugin/` directory (`ls -R` of the bala: `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` only). Nothing plugin-derived is
therefore expected in the render, and nothing is missing on that account.

## 8. Other considerations

- **Not deprecated.** Central `deprecated: null`, `visibility: public`, `graalvmCompatible: Yes`,
  `ballerinaVersion 2201.12.0`, `pullCount 5` (very new package — created 2026-08-03).
- **Version is stable (1.3.0)**, so the render is expected to be API-authoritative.
- **Size/token impact is negligible**: +63 lines (~+58 %) on a 108-line file. The render is
  dominated by the README (73 of 171 lines).
- **Doc quality**: the source doc comments are unusually good (per-parameter `+ x -` docs on every
  method). The renderer drops all parameter-level doc text for class methods — only the method
  summary survives. This applies to both sides and is a renderer design choice, not a regression,
  but it is the largest remaining information loss for this library (e.g. the `tableName` validation
  rule "must start with a letter or underscore…" documented at `store.bal:75–80` is absent from the
  render, so an LLM could suggest an invalid table name that fails at runtime).
- **Trailing newline**: both `.bal.txt` files end without a trailing newline (as do the JSONs).
- The `Special Agent Note` trailing comments are preserved and correct on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 108 / 171 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` on both renders | 0 hits both |
| `diff -u old/*.bal.txt new/*.bal.txt` | 2 hunks, +65 / −2 |
| JSON normalise + `diff -u` | 4 changes: `+baseType:error`, `+type:Class`, 2 de-qualified type names |
| `ls -R <bala>` | `any/{bala.json,dependency-graph.json,docs/README.md,modules/ai.memory.mssql/{store.bal,types.bal},package.json}` — no compiler-plugin |
| `git ls-remote --tags <repo>` | `v1.3.0` exists (`f7ed7c86`, peeled `6d25093e`); latest tag |
| `git clone --depth 1 --branch v1.3.0` | OK -> `work/ai.memory.mssql/src` |
| `diff src/ballerina/store.bal <bala>/modules/.../store.bal` | identical (STORE_IDENTICAL) |
| `diff src/ballerina/types.bal <bala>/modules/.../types.bal` | identical (TYPES_IDENTICAL) |
| `grep -n public store.bal types.bal` | 17 hits; 3 public top-level symbols + 14 public methods |
| `grep -c '    public isolated function' store.bal` | 14 |
| `grep -c 'function ' new render` | 14 |
| `sed -n '180,200p' store.bal` | `getAll` returns `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|...` — single `ai:` |
| `sed -n '20,60p;70,125p' store.bal` | `Error distinct ai:MemoryError` (25); `DatabaseConfiguration record {\| \|}` with `host="localhost"`, `user="sa"`, `port=1433` (30–46); class doc "Represents an MS SQL-backed…" (54); `*ai:ShortTermMemoryStore` (56); `init` signature (82–86) |
| `grep 'type ChatMessage \|type ChatInteractiveMessage ' <ai 1.13.0 bala>` | `model-provider.bal:79`, `:83` — confirms `put` union expansion |
| `diff <(sed -n '8,80p' new render) <bala>/docs/README.md` | identical except missing trailing newline |
| `diff <(sed -n '8,80p' old render) <(sed -n '8,80p' new render)` | identical |
| `curl api.central.ballerina.io/.../ballerinax/ai.memory.mssql/1.3.0` | not deprecated, public, graalvmCompatible Yes, modules `['ai.memory.mssql']` |
| `cat <bala>/any/package.json` | `export: ["ai.memory.mssql"]`, ballerina_version 2201.12.0 |
| `cat OLD_AND_NEW_DIFFS/ai.memory.mssql_diff.md` | its counts (108/171, +65/−2, 2/0 unknowns, 16 added decls) all reproduced independently |

## 10. Caveats and unverified items

- I did not compile either render. "Non-compiling" for the `ai:ai:` token is a syntax/semantic
  judgement from the Ballerina module-prefix rules, not from a compiler run.
- I attributed the `ai:ai:` doubling to the interaction between the de-qualified JSON type name and
  the renderer's link-driven prefixing. That is inferred from the JSON diff (the old JSON had
  `ballerina/ai:1.13.0:` prefixes, the new has `ai:`) plus the surviving external link on
  `ChatInteractiveMessage`; I did not read the `to-syntax-string.ts` source to confirm the code path.
- The class-level description mismatch is confirmed against the JSON of both sides, but I did not
  trace which Java extractor method assigns it.
- Central `pullCount`/`createdDate` were read once from the live API; they will drift.
- `ballerina/ai` was inspected at 1.13.0 from the local bala cache (the version the old JSON's
  qualified refs name). I did not verify that the pipeline resolved exactly that version on both
  sides — the new JSON no longer records the version, so this is unverifiable from the artifacts.

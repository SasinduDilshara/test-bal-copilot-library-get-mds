# ballerinax/ai.memory.postgresql 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.memory.postgresql` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.memory.postgresql |
| Tag reviewed | `v1.0.0` (commit `bb6b5c18d859ac00f3f8a0984bf306ddcb61bf2d`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.memory.postgresql/1.0.0` |
| Old render | `133` lines |
| New render | `203` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library has exactly three public symbols in its single (default) module: `Error`,
`DatabaseConfiguration`, `ShortTermMemoryStore`. `old` rendered only `DatabaseConfiguration`;
`Error` and `ShortTermMemoryStore` both degraded to `// Unknown type:` placeholders, meaning the
entire client-facing API surface (the 14 public methods of the store class) was invisible to a
consuming LLM. `new` emits both: `type Error error;` and a full `class ShortTermMemoryStore` body
with all 14 public methods, correct parameter names, defaults and return types, plus `@display`
annotations on the record, its fields, the class and the `init` parameters.

Nothing present in `old` was dropped or degraded in `new` (declarations removed: 0; README byte-identical).
`new` carries one genuine defect of its own — a malformed `ai:ai:ChatInteractiveMessage` type
reference in `getAll` — and a few fidelity losses shared with, or newly exposed by, the class body.
None of these are regressions relative to `old`, because `old` rendered no class body at all.

## 2. Change inventory

Line counts (`wc -l`): old `133`, new `203` (+70 net; diff reports +72 / −2, 1 hunk).

| Kind | old | new | delta |
|---|---|---|---|
| `// --- section ---` markers | 3 | 3 | 0 |
| `// Unknown type:` placeholders | 2 (`Error`, `ShortTermMemoryStore`) | 0 | −2 |
| Record type defs rendered | 1 (`DatabaseConfiguration`) | 1 | 0 |
| Error type defs rendered | 0 | 1 (`Error`) | +1 |
| Classes rendered | 0 | 1 (`ShortTermMemoryStore`) | +1 |
| Class methods rendered | 0 | 14 | +14 |
| Module-level functions | 0 | 0 | 0 |
| Clients / services / annotations (JSON arrays) | 0/0/0 | 0/0/0 | 0 |
| `@display` annotations rendered | 0 | 13 (1 record + 7 fields + 1 class + 4 init params) | +13 |

**Added (16 declarations):** `type Error`; `class ShortTermMemoryStore`; methods `init`,
`getChatSystemMessage`, `getChatInteractiveMessages`, `getAll`, `put`, `removeChatSystemMessage`,
`removeChatInteractiveMessages`, `removeAll`, `isFull`, `getCapacity`, `putCheckpoint`,
`getCheckpoint`, `removeCheckpoint`, `takeCheckpoint`.

**Removed:** none (0).

**Modified:** `DatabaseConfiguration` — field set, order, types, optionality and doc strings are
byte-identical between the two renders; the only change is the addition of `@display` annotations on
the record and each of its 7 fields.

**Unchanged:** lines 1–108 (header, import, README block) are byte-identical
(`diff <(sed -n '1,108p' old) <(sed -n '1,108p' new)` → no output). Both JSON `readme` values are
identical to each other and byte-identical to the bala `docs/README.md` (3941 chars).

**JSON-level cause of the improvement:** the old JSON already carried `ShortTermMemoryStore` with all
14 functions, but had no `"type"` key on the typeDef; `new` adds `"type": "Class"` (and
`"baseType": "error"` on `Error`), which is what lets `renderTypeDef` dispatch instead of falling
through to `// Unknown type:`. So the loss in `old` was purely a renderer dispatch gap, not an
extraction gap.

## 3. Correctness against library source

Bala `modules/ai.memory.postgresql/{store.bal,types.bal}` is byte-identical to the `v1.0.0` tag
(`diff` on both files → no output), so GitHub and the bala agree; line numbers below are from
`store.bal` (identical in both).

All 14 rendered methods checked against source, one by one:

| Rendered (new) | Source | Match |
|---|---|---|
| `init(DatabaseConfiguration\|postgresql:Client dbConnection, int maxMessagesPerKey = 20, string tableName = "chat_messages", string checkpointTableName = "checkpoints") returns Error?` | store.bal:82–86 | yes (defaults `20` / `"chat_messages"` / `"checkpoints"` all correct) |
| `getChatSystemMessage(string key) returns ai:ChatSystemMessage\|Error\|()` | store.bal:146 (`ai:ChatSystemMessage\|Error?`) | yes |
| `getChatInteractiveMessages(string key) returns ai:ChatInteractiveMessage[]\|Error` | store.bal:177 | yes |
| `getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | store.bal:190–191 | **no** — see §5.1 (`ai:ai:`) |
| `put(string key, ai:ChatUserMessage\|ai:ChatSystemMessage\|ai:ChatAssistantMessage\|ai:ChatFunctionMessage\|ai:ChatMessage[] message) returns Error\|()` | store.bal:200 (`ai:ChatMessage\|ai:ChatMessage[]`) | equivalent (the union is `ai:ChatMessage` expanded to its four members), not literal |
| `removeChatSystemMessage(string key) returns Error\|()` | store.bal:263 | yes |
| `removeChatInteractiveMessages(string key, int\|() count = ()) returns Error\|()` | store.bal:283 | yes |
| `removeAll(string key) returns Error\|()` | store.bal:323 | yes |
| `isFull(string key) returns boolean\|Error` | store.bal:362 | yes |
| `getCapacity() returns int` | store.bal:513 | yes |
| `putCheckpoint(ai:PendingApproval approval) returns Error\|()` | store.bal:521 | yes |
| `getCheckpoint(string sessionId) returns ai:PendingApproval\|()\|Error` | store.bal:542 | yes |
| `removeCheckpoint(string sessionId) returns Error\|()` | store.bal:571 | yes |
| `takeCheckpoint(string sessionId) returns ai:PendingApproval\|()\|Error` | store.bal:589 | yes |

Private methods correctly excluded from `new`: `putAll`, `updateSystemMessage`, `initializeDatabase`,
`ensureCheckpointTable`, `checkpointTableExists`, `getAllFromDatabase`. Module-level non-public
functions (`buildUpsertQuery`, `replaceTableNamePlaceholder`, `partitionMessagesByType`,
`getLatestSystemMessage`, and all of `types.bal`) and the non-public `TABLE_NAME_REGEX`
(store.bal:23) are correctly excluded from both renders. No invented symbols: every declaration in
`new` exists in the source.

`@display` labels in `new` were spot-checked against source and all match verbatim: class
`"PostgreSQL Short Term Memory Store"` (store.bal:55), record `"Database Configuration"`
(store.bal:29), fields `Host`/`Username`/`Password`/`Database Name`/`Port`/`Options`/`Connection Pool`
(store.bal:31–50), init params `Database Connection`/`Max Messages Per Key`/`Table Name`/
`Checkpoint Table Name` (store.bal:82–85).

## 4. Regressions

**None found.**

Checked: (a) mechanical diff reports 0 declarations removed and a single hunk that is purely
additive apart from the two `// Unknown type:` lines being replaced by real definitions;
(b) README section is byte-identical over lines 1–108; (c) `DatabaseConfiguration` field list, order,
types, optionality, doc comments and the two `// Special Agent Note:` cross-package annotations are
unchanged between renders; (d) section markers count 3 on both sides; (e) both JSONs have the same
three typeDefs and empty `clients`/`functions`/`services`/`annotations` arrays; (f) `old`'s
version-qualified refs (`ballerina/ai:1.13.0:ChatSystemMessage`,
`ballerinax/ai.memory.postgresql:1.0.0:Error?` in the JSON) are gone in `new` — an improvement, and
they never reached the `old` render text anyway because the class was a placeholder there.

## 5. Issues in `new` (independent of `old`)

**5.1 Malformed double module prefix in `getAll` (only real defect).**
new render line 159:
```
function getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|ai:ChatInteractiveMessage[]|Error;
```
`ai:ai:ChatInteractiveMessage` does not compile. Root cause is visible in the JSON: `new` already
emits the module prefix inside the type name (`"[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error"`),
and the renderer then prefixes every occurrence of the linked name `ChatInteractiveMessage` with
`ai:` again, hitting the already-prefixed occurrence. (`old` JSON used
`ballerina/ai:1.13.0:ChatInteractiveMessage`, which did not collide.) Only one occurrence in the
whole file (`grep -n 'ai:ai:'` → 1 hit in new, 0 in old). This is a `new`-side renderer bug that
would generalise to any tuple/inline type where the extractor pre-qualifies a linked type.

**5.2 `Error` loses its distinct base type.** Source (store.bal:26) is
`public type Error distinct ai:MemoryError;`; `new` renders `type Error error;`. Valid syntax, but a
consumer cannot tell the error is an `ai:MemoryError` subtype, which matters for `ai` framework
interop. Still strictly better than `old`'s `// Unknown type: Error`.

**5.3 Class inclusion `*ai:ShortTermMemoryStore` is not rendered.** Source store.bal:57. The whole
point of this library is that the class implements the `ai:ShortTermMemoryStore` object type (the
README's own examples assign it to an `ai:ShortTermMemoryStore` variable). Absent from `new`, so the
render does not convey the assignability the README relies on.

**5.4 `DatabaseConfiguration` fidelity (shared with `old`, present in both).**
Source (store.bal:30–51) is a **closed** record `record {| ... |}` in which `host = "localhost"`,
`username = "postgres"` and `port = 5432` are *defaultable* fields, not optional ones. Both renders
show an **open** `record { ... }` with `string host?; string username?; int port?;` and no default
values. An LLM reading either render would believe these fields may be absent at runtime and would
not know the defaults. Confirmed to originate in the JSON (`"optional": true`, no `"default"` key on
these fields) on both sides, so it is an extractor limitation, not introduced by spec v2.

**5.5 Parameter-level documentation dropped; empty doc lines.** The JSON carries a `description` for
every parameter and return value, but the render emits only the method summary followed by a bare
`# ` line (13 occurrences of `^    # $` in `new`, plus one at class level). E.g. the `init` doc
explaining the `tableName` regex constraint and lower-case folding, and
`removeChatInteractiveMessages`'s `count` semantics, are lost. Cosmetically the dangling `# ` lines
add noise. Not a regression (`old` rendered no method docs at all), but it is information available
in the JSON that the renderer discards.

**5.6 Qualifiers not rendered.** `public`, `isolated` are dropped from the class and all methods.
This is the render convention across both sides (`old` also renders `type DatabaseConfiguration`
without `public`), so it is noted for completeness only.

## 6. Coverage gaps vs. the library

**0 gaps in `new`.** Central metadata reports a single module (`modules: ['ai.memory.postgresql']`),
and the bala contains exactly one directory under `modules/`, so there is no submodule API and no
shared submodule gap. The default module exports exactly three public symbols (`grep -n '^public '`
on store.bal → lines 26, 30, 56); all three appear in `new`. `old` covered 1 of 3 in usable form
(2 were `// Unknown type:` placeholders with no members).

## 7. Compiler plugin

None. The repo at `v1.0.0` contains no `compiler-plugin`, `*-compiler-plugin` or
`ballerina-*-compiler-plugin` directory (`ls` of repo root: `LICENSE README.md ballerina build-config
build.gradle gradle gradle.properties gradlew gradlew.bat issue_template.md
pull_request_template.md settings.gradle`), and the bala has no `compiler-plugin/` directory
(`ls` of the bala `any/` dir: `bala.json dependency-graph.json docs modules package.json`). Nothing
plugin-implied is therefore missing from the render.

## 8. Other considerations

- Package is not deprecated (`deprecated: None`, empty `deprecateMessage`). Version `1.0.0` is a
  stable first release; pull count 5, created 2026-08-02.
- `ballerinax/postgresql.driver` is imported as `_` in the source; neither render mentions it. A user
  reusing the `postgresql:Client` overload does not need it, so this is acceptable, but the render
  gives no hint that the driver import is bundled.
- Size impact is small: +70 lines / roughly +2.9 KB of render text for the entire client API. The
  README block (103 lines) is still ~51% of the `new` render and ~78% of `old`.
- Both renders inline the README verbatim including the SQL schema block, which is high-value context
  for this library.
- The `// Special Agent Note: X FROM <org>/<pkg> package` trailer convention is preserved and
  correctly applied in `new` for `ballerina/ai`, `ballerinax/postgresql` and `ballerina/sql` refs.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 133 / 203 |
| `grep -c '^// Unknown type:' old` | 2 |
| `grep -c '^// Unknown type:' new` | 0 |
| `grep -n '^// --- ' old` / `new` | 3 markers each (README, END README, Types), same line numbers |
| `diff <(sed -n '1,108p' old) <(sed -n '1,108p' new)` | no output → README block identical |
| `grep -n 'ai:ai:' new old` | 1 hit, new:159; 0 hits in old |
| `grep -c '^    # $' new` | 13 |
| `git ls-remote --tags <repo>` | only `v1.0.0` → `bb6b5c18…` |
| `git clone --depth 1 --branch v1.0.0` | OK, HEAD `bb6b5c18d859ac00f3f8a0984bf306ddcb61bf2d` |
| `diff src/ballerina/store.bal <bala>/modules/ai.memory.postgresql/store.bal` | no output (STORE_SAME) |
| `diff src/ballerina/types.bal <bala>/modules/…/types.bal` | no output (TYPES_SAME) |
| `grep -n 'version' src/ballerina/Ballerina.toml` | `version = "1.0.0"` |
| `ls <bala>/any/modules` | single dir `ai.memory.postgresql` |
| `ls <bala>/any` | `bala.json dependency-graph.json docs modules package.json` — no `compiler-plugin/` |
| `grep -nE '^public ' store.bal` | 26 `Error`, 30 `DatabaseConfiguration`, 56 `ShortTermMemoryStore` |
| `grep -n 'public isolated function' store.bal` | 14 methods at lines 82,146,177,190,200,263,283,323,362,513,521,542,571,589 |
| `grep -n '\*ai:' store.bal` | 57 `*ai:ShortTermMemoryStore;` — absent from both renders |
| `grep -n 'string host\|string username\|int port' store.bal` | 33 `= "localhost"`, 36 `= "postgres"`, 45 `= 5432` |
| JSON top-level keys, both sides | `name, description, readme, typeDefs, clients, functions, services, annotations`; typeDefs=3, all other arrays empty on both sides |
| JSON typeDef keys | old `Error{type:Error}`, `ShortTermMemoryStore{no type key, functions:14}`; new adds `baseType:error`, `type:Class`, `annotations` |
| JSON `getAll` return type | old `[ballerina/ai:1.13.0:ChatSystemMessage, ballerina/ai:1.13.0:ChatInteractiveMessage...]\|ChatInteractiveMessage[]\|Error`; new `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|ChatInteractiveMessage[]\|Error` |
| JSON `DatabaseConfiguration.fields` | 7 fields both sides; `host/username/port` marked `optional:true`, no `default` key, on both sides |
| JSON `readme` vs bala `docs/README.md` | identical, 3941 chars; old readme == new readme |
| Central API `packages/ballerinax/ai.memory.postgresql/1.0.0` | `deprecated: None`, `modules: ['ai.memory.postgresql']`, Apache-2.0, pullCount 5 |
| `OLD_AND_NEW_DIFFS/ai.memory.postgresql_diff.md` | 16 declarations added, 0 removed, 1 hunk, +72/−2 — verified against the files |

## 10. Caveats and unverified items

- The renders were not compiled. The `ai:ai:ChatInteractiveMessage` defect is asserted as
  non-compiling on the basis of Ballerina syntax (a qualified name cannot carry two module
  prefixes), not on a compiler run.
- The claim in §5.1 about the renderer's prefixing logic is inferred from the JSON→render delta on
  this library only; the `to-syntax-string` renderer source was not read as part of this review.
- `ai:ShortTermMemoryStore`, `ai:MemoryError`, `ai:PendingApproval`, `ai:ChatMessage` and friends
  were not cross-checked against the `ballerina/ai` 1.13.0 bala; they are referenced here only as
  they appear in this library's own source.
- Semantic equivalence of the expanded `put` union (§3) rests on `ai:ChatMessage` being exactly
  `ChatUserMessage|ChatSystemMessage|ChatAssistantMessage|ChatFunctionMessage`, which is what the
  extractor emitted but was not independently confirmed against the `ballerina/ai` source.

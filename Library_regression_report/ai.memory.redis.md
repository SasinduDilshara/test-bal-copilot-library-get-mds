# ballerinax/ai.memory.redis 1.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.memory.redis` |
| Pinned version | `1.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.memory.redis |
| Tag reviewed | `v1.1.0` (commit `3d8c5437be6c4e13b7b96aea9aa7ff33185dd8ed`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.memory.redis/1.1.0` |
| Old render | `85` lines |
| New render | `149` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`old` degraded the library's entire public API to two placeholder lines
(`// Unknown type: Error`, `// Unknown type: ShortTermMemoryStore`) — the render carried the README
and nothing else. `new` emits the real `Error` type definition and the full `ShortTermMemoryStore`
class with all 14 public methods, their parameters, defaults, return types, doc summaries, the
`@display` annotation, and cross-package provenance notes. Nothing that was present in `old` is
missing or degraded in `new`. All 14 method signatures were checked one-by-one against the bala
source and match (modulo the equivalent `T?` → `T|()` rewriting and the expansion of the
`ai:ChatMessage` alias into its four members, which is semantically exact).

One real defect is introduced by `new`: the `getAll` return type renders as
`[ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]` — a doubled module prefix that is not
valid Ballerina. A handful of smaller fidelity losses (`distinct ai:MemoryError` flattened to
`error`, class doc replaced by the `init` doc, `*ai:ShortTermMemoryStore;` inclusion and
`public`/`isolated` qualifiers dropped) also exist in `new`, but none of them are regressions —
`old` rendered no class body at all.

## 2. Change inventory

Line counts (`wc -l`): old **85**, new **149**. Single diff hunk: old lines 80–85 → new lines 80–149
(+66 / −2).

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| `// --- ` section markers | 3 | 3 |
| Version-qualified type refs (`mod:1.2.3:Type`) in render | 0 | 0 |
| Version-qualified type refs in JSON | 2 | 0 |

Declarations removed in `new`: **0**.

Declarations added in `new`: **16** (1 type, 1 class, 14 class methods):

| Kind | Names |
|---|---|
| type (1) | `Error` |
| class (1) | `ShortTermMemoryStore` (with `@display {label: "Redis Short Term Memory Store"}`) |
| constructor (1) | `init` |
| methods (13) | `getChatSystemMessage`, `getChatInteractiveMessages`, `getAll`, `put`, `removeChatSystemMessage`, `removeChatInteractiveMessages`, `removeAll`, `isFull`, `getCapacity`, `putCheckpoint`, `getCheckpoint`, `removeCheckpoint`, `takeCheckpoint` |

README section: byte-identical between the two renders and byte-identical to
`any/docs/README.md` (71 lines, `diff` exit 0). No README content lost.

JSON-level diff (`typeDefs` only; `readme`, `functions`, `clients`, `services`, `annotations`,
`name`, `description` are all byte-identical between old and new JSON):

1. `Error` gains `"baseType": "error"`.
2. `ShortTermMemoryStore` gains `"annotations": [{"name":"display","value":"{label: \"Redis Short Term Memory Store\"}"}]`.
3. `ShortTermMemoryStore` gains `"type": "Class"`.
4. `init` return type: `ballerinax/ai.memory.redis:1.1.0:Error?` → `Error?` (de-versioned).
5. `getAll` return type: `[ballerina/ai:1.13.0:ChatSystemMessage, ballerina/ai:1.13.0:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error`
   → `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error`.

Items 3 + 2 are what unlock the class rendering; items 4/5 are the documented spec-v2 de-versioning.

## 3. Correctness against library source

Upstream `v1.1.0` `ballerina/store.bal` and `ballerina/types.bal` are **identical** to the bala's
`modules/ai.memory.redis/store.bal` and `types.bal` (`diff` with blank lines stripped, exit 0), so
GitHub and the bala agree; citations below use the bala.

All public declarations in the default module (`grep -nE '^\s*public ' modules/ai.memory.redis/*.bal`):

| Source | New render | Match? |
|---|---|---|
| `store.bal:22` `public type Error distinct ai:MemoryError;` | line 84 `type Error error;` | partial — see §5.2 |
| `store.bal:32` `public isolated class ShortTermMemoryStore` + `store.bal:31` `@display{label:"Redis Short Term Memory Store"}` | lines 88–89 | annotation exact; qualifiers dropped |
| `store.bal:47-50` `init(redis:Client\|redis:ConnectionConfig redisClient, int maxMessagesPerKey = 20, cache:CacheConfig? cacheConfig = (), string keyPrefix = "chat_memory") returns Error?` | line 90 | ✅ exact (incl. all three defaults `20`, `()`, `"chat_memory"`) |
| `store.bal:97` `getChatSystemMessage(string key) returns ai:ChatSystemMessage\|Error?` | line 94 `... returns ai:ChatSystemMessage\|Error\|()` | ✅ equivalent |
| `store.bal:130` `getChatInteractiveMessages(string key) returns ai:ChatInteractiveMessage[]\|Error` | line 99 | ✅ exact |
| `store.bal:154-155` `getAll(string key) returns [ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | line 103 | ❌ `ai:ai:ChatInteractiveMessage` — see §5.1 |
| `store.bal:182` `put(string key, ai:ChatMessage\|ai:ChatMessage[] message) returns Error?` | line 107 `put(string key, ai:ChatUserMessage\|ai:ChatSystemMessage\|ai:ChatAssistantMessage\|ai:ChatFunctionMessage\|ai:ChatMessage[] message) returns Error\|()` | ✅ equivalent — `ai:ChatMessage` is exactly that 4-way union (`ballerina/ai` 1.13.0 `model-provider.bal:79`) |
| `store.bal:292` `removeChatSystemMessage(string key) returns Error?` | line 111 | ✅ |
| `store.bal:316` `removeChatInteractiveMessages(string key, int? count = ()) returns Error?` | line 116 `int\|() count = ()` | ✅ equivalent, default preserved |
| `store.bal:357` `removeAll(string key) returns Error?` | line 122 | ✅ |
| `store.bal:371` `isFull(string key) returns boolean\|Error` | line 126 | ✅ |
| `store.bal:463` `getCapacity() returns int` | line 130 | ✅ |
| `store.bal:471` `putCheckpoint(ai:PendingApproval approval) returns Error?` | line 134 | ✅ |
| `store.bal:483` `getCheckpoint(string sessionId) returns ai:PendingApproval\|Error?` | line 138 | ✅ |
| `store.bal:503` `removeCheckpoint(string sessionId) returns Error?` | line 142 | ✅ |
| `store.bal:516` `takeCheckpoint(string sessionId) returns ai:PendingApproval\|Error?` | line 148 | ✅ |

Private methods (`systemKey`, `interactiveKey`, `checkpointKey`, `putAll`, `updateCache`,
`cacheFromRedis`, `removeCacheEntry`, `getCacheEntry`) and module-private helpers in `types.bal` are
correctly **absent** from both renders.

Doc summaries in `new` match the source doc comments verbatim, including the multi-line ones
(`removeAll` at `store.bal:350-356`, `takeCheckpoint` at `store.bal:510-515`).

Cross-package "Special Agent Note" comments are accurate: `redis:Client`/`redis:ConnectionConfig` →
`ballerinax/redis`, `cache:CacheConfig` → `ballerina/cache`, all `Chat*`/`PendingApproval` →
`ballerina/ai`.

## 4. Regressions

**None found.**

Checked to conclude this:
- Declarations removed in `new`: 0 (mechanical diff hunk removes only the two `// Unknown type:` lines).
- README section: byte-identical old vs new, and identical to the bala README.
- `// --- ` section markers: 3 in both.
- JSON: every top-level key except `typeDefs` is byte-identical; within `typeDefs` the only changes
  are additive (`baseType`, `annotations`, `type`) or de-versioning of type-ref strings. No
  parameter, default, doc string, or return type was dropped between old and new JSON.
- Nothing correct in `old` is absent from `new`: `old` contained no signatures at all.

## 5. Issues in `new` (independent of `old`)

**5.1 (real defect) Doubled module prefix in `getAll` return type — non-compiling syntax.**
Render line 103:
```
function getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|ai:ChatInteractiveMessage[]|Error;
```
`ai:ai:ChatInteractiveMessage` is not valid Ballerina. Root cause is a JSON/renderer mismatch, not
either side alone: the new JSON emits the tuple member already qualified
(`"[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error"`) while also
carrying an external link for `ChatInteractiveMessage` → `ballerina/ai`; `toSyntaxString` then
prefixes *every* occurrence of `ChatInteractiveMessage`, so the already-qualified one becomes
`ai:ai:` and the bare trailing one correctly becomes `ai:`. Note the asymmetry: `ChatSystemMessage`
has no link entry in that member's `links` array, so it escaped double-prefixing. Introduced by
spec v2 (old JSON used fully-versioned `ballerina/ai:1.13.0:` names and old never rendered the class).

**5.2 `Error` loses its `distinct ai:MemoryError` parentage.** Source `store.bal:22` is
`public type Error distinct ai:MemoryError;`; `new` renders `type Error error;`. An LLM reading this
cannot tell that `redis:Error` is assignable to `ai:MemoryError`/`ai:Error`, which matters because
the store is normally used through the `ai:ShortTermMemoryStore` object type.

**5.3 Class-level doc is wrong — it is `init`'s doc.** Source `store.bal:30` documents the class as
`# Represents a Redis-backed short-term memory store for messages.`, and `store.bal:40` documents
`init` as `# Initializes the Redis-backed short-term memory store.`. `new` prints the *init* text as
the class doc (line 86) and leaves `init` (line 90) undocumented. This originates in the JSON
(`typeDefs[1].description`), which is byte-identical in old and new — so it is an extractor quirk
that pre-dates spec v2, only now visible because the class renders at all.

**5.4 `*ai:ShortTermMemoryStore;` object-type inclusion is not rendered.** Source `store.bal:33`.
The README (rendered above, lines 52 and 68) assigns instances to `ai:ShortTermMemoryStore`, but the
class body gives no indication that the class implements that object type.

**5.5 `public` and `isolated` qualifiers are dropped** on `type Error`, on `class
ShortTermMemoryStore`, and on all 14 methods. As rendered, everything reads as module-private and
non-isolated; `isolated` matters for use inside `isolated` agent code.

**5.6 No import lines for referenced modules, and a prefix collision.** The render's only import is
`import ballerinax/ai.memory.redis;` (line 4), whose *default* prefix is `redis` — yet `redis:Client`
and `redis:ConnectionConfig` on line 90 mean `ballerinax/redis`. The "Special Agent Note" disambiguates,
and the README shows the `as redisStore` aliasing workaround, but the bare signature is ambiguous.

**5.7 Parameter documentation is dropped.** The JSON carries per-parameter descriptions (e.g.
`init.redisClient` → "The Redis client or connection configuration to connect to the Redis server";
`put.message` → the three-line note about only the last system message being persisted), but the
render emits only the summary line followed by an empty `# `. Return descriptions are dropped too.
Renderer-wide behaviour, not library-specific.

## 6. Coverage gaps vs. the library

**None.** `package.json` `"export": ["ai.memory.redis"]` and the bala `modules/` listing contain
exactly one module — the default module — so there is no submodule-only API and no shared
submodule gap for this library. The default module exports exactly two public symbols (`Error`,
`ShortTermMemoryStore`); both appear in `new`, with all 14 public methods of the class. `old`
listed both names but with zero members.

Central metadata confirms a single module (`modules: [{name: "ai.memory.redis"}]`).

## 7. Compiler plugin

The bala has **no** `compiler-plugin/` directory
(`ls .../1.1.0/any` → `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`), and
the upstream repo at `v1.1.0` has no `compiler-plugin` module (`ls src` → `ballerina`,
`build-config`, `gradle`, …). Nothing is contributed by a plugin, so nothing plugin-derived is
missing from the render.

The library does depend on `ballerina/ai` 1.13.0, which *does* ship a compiler plugin
(`ai-compiler-plugin-1.13.0.jar`), but that plugin's behaviour belongs to `ballerina/ai`'s own render.

## 8. Other considerations

- Not deprecated (`deprecated: null`, empty `deprecateMessage` from Central).
- Version `1.1.0` is post-1.0, so the API is nominally stable; `pullCount` is 6, i.e. a very new
  package (created 2026-06-02 per `createdDate`).
- No `configurable`, `annotation`, `listener`, or `service` declarations exist in the module
  (`grep` returned nothing), consistent with the empty `functions`/`clients`/`services`/`annotations`
  arrays in both JSONs.
- Size/token impact: 2,547 → 6,127 bytes (+141%). Trivial in absolute terms; the added content is
  the entire usable API surface, so the trade is strongly favourable.
- The `@display` annotation now surfaces, which helps low-code/agent tooling label the store.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 85 / 149 |
| `ls -R <bala>` | `any/{bala.json,dependency-graph.json,docs,modules,package.json}`; modules → `ai.memory.redis/{store.bal,types.bal}`; no `compiler-plugin/` |
| `wc -l modules/ai.memory.redis/*.bal` | store.bal 554, types.bal 224 |
| `grep -nE '^\s*public ' modules/ai.memory.redis/*.bal` | 2 module-level publics (`Error` L22, `ShortTermMemoryStore` L32) + 14 public methods (L47,97,130,154,182,292,316,357,371,463,471,483,503,516); 2 public fields inside an anonymous `ai:Prompt` object in types.bal L113-114 (not module-level) |
| `grep -nE 'configurable\|annotation\|listener\|service ' modules/*.bal` | no matches |
| `cat any/package.json` | `export: ["ai.memory.redis"]`, ballerina_version 2201.12.0, graalvmCompatible true |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1`, `v1.1.0` → exact tag `v1.1.0` exists |
| `git clone --depth 1 --branch v1.1.0` + `git log -1` | `3d8c5437be6c4e13b7b96aea9aa7ff33185dd8ed (grafted, HEAD, tag: v1.1.0)` |
| `diff <(sed '/^$/d' src/ballerina/store.bal) <(sed '/^$/d' bala/.../store.bal)` | IDENTICAL |
| `diff` same for `types.bal` | IDENTICAL |
| Python top-level JSON key compare | only `typeDefs` differs (9330 → 9394 chars); `readme`, `functions`, `clients`, `services`, `annotations`, `name`, `description` byte-identical |
| Python unified diff of `typeDefs` | 5 changes: +`baseType: "error"`, +`annotations[display]`, +`type: "Class"`, `init` return de-versioned, `getAll` return de-versioned |
| Dump of new JSON `init`/`getAll`/`put` | defaults `20`, `()`, `"chat_memory"` present; `getAll` return string is `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error` with an external link only for `ChatInteractiveMessage` → confirms §5.1 is renderer-side |
| `grep "public type ChatMessage " ballerina/ai/1.13.0/.../model-provider.bal` | L79 `ChatUserMessage\|ChatSystemMessage\|ChatAssistantMessage\|ChatFunctionMessage` → `put` expansion is exact |
| `grep "public type MemoryError" .../error.bal` | L96 `public type MemoryError distinct Error;` → confirms §5.2 loss |
| `grep "public type ShortTermMemoryStore" .../short_term_memory_store.bal` | L26 `isolated object {` → confirms §5.4 relevance |
| `diff <bala>/docs/README.md <(sed -n '7,77p' new render)` | README_IDENTICAL (71 lines) |
| `diff <(sed -n '7,77p' old) <(sed -n '7,77p' new)` | README_SAME_BOTH_RENDERS |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep -c '^// --- '` | old 3, new 3 |
| Central API `packages/ballerinax/ai.memory.redis/1.1.0` | not deprecated; single module; pullCount 6 |

## 10. Caveats and unverified items

- The renders were not recompiled or re-derived; this audit compares the supplied artefacts against
  the bala and upstream source. The claim that §5.1 originates in `toSyntaxString` rather than the
  Java extractor is inferred from the JSON contents (correct string + a link that triggers
  prefixing) — the TypeScript renderer source was not read, so the exact code path is **unverified**.
- The precomputed diff at `OLD_AND_NEW_DIFFS/ai.memory.redis_diff.md` was cross-checked against the
  two files and its counts (85/149, +66/−2, 16 added declarations, 0 removed) were reproduced
  independently; no discrepancies.
- Runtime/behavioural correctness of the library itself was not tested — only signature and
  documentation fidelity of the render.

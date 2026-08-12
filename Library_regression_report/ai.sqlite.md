# ballerinax/ai.sqlite 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.sqlite` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.sqlite |
| Tag reviewed | `v1.0.0` (commit `c51d9cfc8223063a1f9e13deea0ba92b42e2d998`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.sqlite/1.0.0/java21` |
| Old render | `162` lines |
| New render | `234` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library has exactly five public symbols in its single (default) module: `Error`,
`DatabaseConfiguration`, `Options`, `JournalMode`, `ShortTermMemoryStore`. `old` rendered three of
them and degraded the other two to bare `// Unknown type:` placeholders — including
`ShortTermMemoryStore`, which is the entire usable API surface (14 public methods). `new` renders all
five, adding the class with all 14 public methods, their parameters, defaults, return types and
`@display` annotations. Nothing present in `old` was lost: the only two removed lines are the two
`// Unknown type:` placeholders. README content is byte-identical on both sides and equals the bala
`docs/README.md` exactly.

One real defect exists in `new`'s new content: `getAll`'s return type is rendered as
`[ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]` — a doubled module prefix that does not
compile. It is not a regression (old emitted no signature at all there) but it is wrong output.

## 2. Change inventory

`wc -l`: old 162, new 234. Precomputed diff: +74 / −2, 1 hunk (old 123–162 → new 123–234).

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 | −2 |
| top-level `type` declarations rendered | 3 | 4 | +1 (`Error`) |
| `class` declarations rendered | 0 | 1 | +1 (`ShortTermMemoryStore`) |
| class methods rendered | 0 | 14 | +14 |
| `// --- section ---` markers | 3 | 3 | 0 |
| version-qualified type refs (`mod:1.2.3:Type`) in render | 0 | 0 | 0 |
| README characters | 5878 | 5878 | 0 |

Declarations **added** (16): `type Error`; `class ShortTermMemoryStore` with `init`,
`getChatSystemMessage`, `getChatInteractiveMessages`, `getAll`, `put`, `removeChatSystemMessage`,
`removeChatInteractiveMessages`, `removeAll`, `isFull`, `putCheckpoint`, `getCheckpoint`,
`removeCheckpoint`, `takeCheckpoint`, `getCapacity`.

Declarations **removed**: none.

Declarations **modified**: `DatabaseConfiguration`, `Options`, `JournalMode` — unchanged in
structure; `new` additionally emits their `@display` annotations (1 type-level annotation each, plus
one per field: `URL`, `Options`, `Connection Timeout`, `Journal Mode`, `Busy Timeout`).

JSON level (both files have the same top-level keys and 5 `typeDefs`, `clients`/`functions`/
`services`/`annotations` all empty on both sides):

| typeDef | old JSON | new JSON |
|---|---|---|
| `Error` | `type: Error` | `type: Error`, `baseType: error` |
| `DatabaseConfiguration` | Record, 3 fields | + 1 annotation (and per-field annotations) |
| `Options` | Record, 2 fields | + 1 annotation |
| `JournalMode` | Union, 6 members | + 1 annotation |
| `ShortTermMemoryStore` | *no `type` key*, 14 functions | `type: Class`, 14 functions, 1 annotation |

The 14 methods were already in the `old` JSON — `old`'s `renderTypeDef` simply had no branch for a
typeDef lacking a recognised `type`, so it printed `// Unknown type: ShortTermMemoryStore`. The
regression fix is in the renderer/extractor tagging, not in extraction volume.

Also visible in the JSON: `old` emitted version-qualified refs inside type names
(`[ballerina/ai:1.13.0:ChatSystemMessage, ballerina/ai:1.13.0:ChatInteractiveMessage...]`), `new`
emits `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]`. This never reached `old`'s rendered
text because the class was never rendered.

## 3. Correctness against library source

Bala `modules/ai.sqlite/store.bal` and `types.bal` are byte-identical to the upstream `v1.0.0`
sources (`diff` returned no output for both files), so GitHub and the bala agree.

All 14 rendered methods checked against `store.bal`:

| Rendered (new) | Source (`store.bal`) | Verdict |
|---|---|---|
| `init(DatabaseConfiguration\|jdbc:Client dbConnection, int maxMessagesPerKey = 20, string tableName = "chat_messages", string checkpointTableName = "checkpoints") returns Error?` | L95–98 | correct, incl. all 4 `@display` labels and all 3 defaults |
| `getChatSystemMessage(string key) returns ai:ChatSystemMessage\|Error\|()` | L167 `returns ai:ChatSystemMessage\|Error?` | equivalent |
| `getChatInteractiveMessages(string key) returns ai:ChatInteractiveMessage[]\|Error` | L199 | correct |
| `getAll(string key) returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | L212–213 `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|ai:ChatInteractiveMessage[]\|Error` | **malformed** — see §5.1 |
| `put(string key, ai:ChatUserMessage\|ai:ChatSystemMessage\|ai:ChatAssistantMessage\|ai:ChatFunctionMessage\|ai:ChatMessage[] message) returns Error\|()` | L222 `put(string key, ai:ChatMessage\|ai:ChatMessage[] message) returns Error?` | equivalent — `ai:ChatMessage` is exactly that 4-way union (`ballerina/ai` 1.13.0 `model-provider.bal:79`) |
| `removeChatSystemMessage(string key) returns Error\|()` | L293 | correct |
| `removeChatInteractiveMessages(string key, int\|() count = ()) returns Error\|()` | L313 `int? count = ()` | equivalent |
| `removeAll(string key) returns Error\|()` | L353 | correct |
| `isFull(string key) returns boolean\|Error` | L391 | correct |
| `putCheckpoint(ai:PendingApproval approval) returns Error\|()` | L405 | correct |
| `getCheckpoint(string sessionId) returns ai:PendingApproval\|()\|Error` | L426 `ai:PendingApproval?\|Error` | equivalent |
| `removeCheckpoint(string sessionId) returns Error\|()` | L451 | correct |
| `takeCheckpoint(string sessionId) returns ai:PendingApproval?\|Error` | L470 | correct |
| `getCapacity() returns int` | L648 | correct |

The 7 `private isolated function` members (`putAll` L247, `updateSystemMessage` L275,
`ensureCheckpointTable` L498, `checkpointTableExists` L524, `initializeDatabase` L534,
`loadFromDatabase` L578, `countInteractiveMessages` L633) are correctly excluded from both renders,
as are the 4 module-private helper functions (`replaceTableNamePlaceholder` L653,
`partitionMessagesByType` L660, `getLatestSystemMessage` L676, `buildDriverProperties` L685) and all
of `types.bal` (no `public` declarations there).

`JournalMode`'s six members match `store.bal:63` exactly. `Error` is `distinct ai:MemoryError`
(`store.bal:23`); `ai:MemoryError` is itself `distinct Error` in `ballerina/ai` (`error.bal:96`).

## 4. Regressions

**None found.**

Checked to conclude this:
- `diff` shows exactly 2 removed lines, both `// Unknown type:` placeholders (`// Unknown type: Error`
  at old:126 and `// Unknown type: ShortTermMemoryStore` at old:162). No declaration, parameter,
  default, return type or doc line present in `old` is absent from `new`.
- README block extracted with `sed -n '/--- README ---/,/--- END README ---/p'` from both files:
  byte-identical (`diff` empty). JSON `readme` fields compare equal (5878 chars each).
- Section markers identical (3 each, same names, same line numbers 6/122/124).
- `DatabaseConfiguration`, `Options`, `JournalMode` bodies are unchanged apart from purely additive
  `@display` lines.
- No version-qualified type refs appear in either rendered file, so no ref-quality loss.
- `grep -c '^// Unknown type:'` → old 2, new 0.

## 5. Issues in `new` (independent of `old`)

**5.1 `ai:ai:ChatInteractiveMessage` — malformed, non-compiling type (the one real defect).**
`new/ballerinax_ai.sqlite.bal.txt:188` renders
`returns [ai:ChatSystemMessage, ai:ai:ChatInteractiveMessage...]|ai:ChatInteractiveMessage[]|Error`.
Root cause is visible in the JSON: `new`'s `getAll.return.type.name` is already prefix-qualified
(`[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]|ChatInteractiveMessage[]|Error`), and the
renderer then prefixes every occurrence of the linked external name `ChatInteractiveMessage` with
`ai:`, doubling the already-qualified one. Only one such occurrence exists in this library
(`grep -n 'ai:ai:'` → 1 hit in `new`, 0 in `old`). Likely to recur in any library whose extracted
type name mixes pre-qualified and bare occurrences of the same external type.

**5.2 `Error` loses its base type.** Source is `public type Error distinct ai:MemoryError`
(`store.bal:23`); `new` renders `type Error error;` (line 127). The JSON only carries
`baseType: "error"`, so the `distinct ai:MemoryError` relationship — which is what makes this store's
errors catchable as `ai:MemoryError` — is not recoverable from the render. Still a large improvement
over `old`, which rendered nothing.

**5.3 Class documentation is the constructor's, not the class's.** Source class doc is
`# Represents a SQLite-backed short-term memory store for messages.` (`store.bal:65`); `new` renders
`# Initializes the SQLite-backed short-term memory store.` above `class ShortTermMemoryStore`
(line 171). This comes from the extractor — `old`'s JSON has the same wrong `description` on the
typeDef — but it only becomes visible in `new`. `init` itself is then rendered with no doc.

**5.4 Type inclusion `*ai:ShortTermMemoryStore` is not rendered.** `store.bal:69` includes the
`ai:ShortTermMemoryStore` object type; that is the whole point of the module (README line 50:
`ai:ShortTermMemoryStore store = check new sqlite:ShortTermMemoryStore({url});`). The render's class
body shows no inclusion, so an LLM relying on the type section alone cannot know the class is
assignable to `ai:ShortTermMemoryStore`. The README section does convey it, so impact is mitigated.

**5.5 Qualifiers dropped.** `public isolated class` → `class`; `public isolated function` → `function`
for all 14 methods. Isolatedness matters for use inside `isolated` service/agent code.

**5.6 Record defaults lost and closed records rendered as open.** Source has
`Options options = {};` and `decimal connectionTimeout = 30.0;` inside `record {| ... |}`
(`store.bal:27–39`). The extractor marks both as `optional: true` with no `default` key (verified in
both JSONs), so both renders emit `Options options?;` / `decimal connectionTimeout?;` inside
`record { ... }`. The `30.0` default survives only in the README's Configuration table. Present in
`old` too — shared, not a regression.

**5.7 Parameter and return documentation dropped.** The JSON carries per-parameter `description`
and a return `description` (e.g. `init.return.description = "An error if the initialization fails"`),
but the render emits only the leading description line followed by a dangling `# ` line (e.g.
new:172, 178, 183…). 14 empty `# ` lines are emitted this way.

**5.8 Undeclared prefixes.** The render's import block is only `import ballerinax/ai.sqlite;`
(line 4) yet the body uses `ai:` and `jdbc:` prefixes. The trailing `// Special Agent Note: … FROM
ballerina/ai package` comments compensate, but the file as printed is not compilable. Renderer-wide
convention, not specific to this library.

No invented symbols, no encoding problems (the README's `…` and `—` round-trip correctly), and no
missing public API (see §6).

## 6. Coverage gaps vs. the library

**Zero coverage gaps in `new`.** The bala exports one module only (`package.json` `export:
["ai.sqlite"]`; `modules/` contains only `ai.sqlite`; Central metadata lists exactly one module), so
the `getDefaultModule()`-only extraction loses nothing here — there is no submodule-only API.

`grep -nE '^public ' modules/ai.sqlite/*.bal` yields exactly 5 declarations; all 5 are rendered in
`new`. In `old`, 2 of 5 (`Error`, `ShortTermMemoryStore`) were placeholders, i.e. `old` had a 2-symbol
gap covering 14 of the library's 14 callable methods.

Not rendered on either side, correctly: `types.bal` has no `public` declarations (all its records and
functions are module-private), and there are no annotations, listeners, services, constants or
configurable variables in the package (`grep -nE '^(annotation|listener|service|const|configurable)'`
→ no matches).

## 7. Compiler plugin

The package has **no compiler plugin**. The bala contains no `compiler-plugin/` directory and no
`compiler-plugin.json`; the upstream repo at `v1.0.0` has no `*compiler-plugin*` path
(`find . -iname '*compiler-plugin*'` → empty). The only platform artifact is
`platform/java21/sqlite-jdbc-3.46.1.0.jar`, declared in `Ballerina.toml` as an
`org.xerial:sqlite-jdbc` 3.46.1.0 dependency — a runtime driver, contributing nothing to the render.
Nothing plugin-implied is therefore missing.

## 8. Other considerations

- Version pin is consistent everywhere: `Ballerina.toml` `version = "1.0.0"`, bala path `1.0.0`,
  `package.json` `version: 1.0.0`, Central `1.0.0`. Central reports `deprecated: null`,
  `visibility: public`, `ballerinaVersion: 2201.12.0`.
- This is a `1.0.0` release (not pre-1.0), so no instability caveat.
- Size: 7,934 → 11,941 bytes (+50%), 162 → 234 lines. Small in absolute terms; the added 72 lines
  buy the entire callable API, which is a very favourable token trade.
- Doc quality is high: every public method has a description, and the README (5,878 chars, 116 of the
  234 rendered lines — ~50% of the render) carries a Configuration table, a Schema section with DDL,
  and two full quickstart snippets. An LLM has enough to write correct code from `new`; from `old` it
  had the README only and no method signatures.
- `@display` annotations added by `new` (11 in total across types, fields and parameters) are
  low-signal for code generation but harmless and faithful to source.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 162 / 234 |
| `ls -R <bala>` | `java21/{bala.json,dependency-graph.json,docs,modules,package.json,platform}`; `modules/ai.sqlite/{store.bal,types.bal}`; `platform/java21/sqlite-jdbc-3.46.1.0.jar` |
| `git ls-remote --tags <repo>` | only `v1.0.0` → `c51d9cfc8223063a1f9e13deea0ba92b42e2d998` |
| `git clone --depth 1 --branch v1.0.0` | ok; HEAD `c51d9cf` "[Gradle Release Plugin] - pre tag commit: 'v1.0.0'" |
| `diff <bala>/modules/ai.sqlite/store.bal <src>/ballerina/store.bal` | identical |
| `diff <bala>/modules/ai.sqlite/types.bal <src>/ballerina/types.bal` | identical |
| `grep -nE '^public ' modules/ai.sqlite/*.bal` | 5 hits (store.bal:23,27,44,63,67); none in types.bal |
| `grep -nE '^(annotation\|listener\|service\|const\|configurable)' modules/ai.sqlite/*.bal` | no matches |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep -n 'ai:ai:'` | new:188 (1 hit), old 0 hits |
| `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` on renders | 0 hits both sides |
| `grep -n '^// --- '` | 6/122/124 on both sides, same names |
| `diff` of README blocks (sed range) | identical |
| Python: `old.json['readme'] == new.json['readme']` | `True`, 5878 chars each |
| Python: render readme vs bala `docs/README.md` | equal after strip (only a trailing `\n` differs) |
| Python: typeDef summary both JSONs | 5 typeDefs each; `new` adds `type: Class` on `ShortTermMemoryStore`, `baseType: error` on `Error`, 1 annotation on each of 4 typeDefs |
| Python: class function names both JSONs | identical list of 14, same order; all `returnType` keys null (return lives under `return`) |
| Python: `getAll` JSON return type | old `[ballerina/ai:1.13.0:ChatSystemMessage, ballerina/ai:1.13.0:ChatInteractiveMessage...]\|…`; new `[ai:ChatSystemMessage, ai:ChatInteractiveMessage...]\|…` |
| Python: `DatabaseConfiguration`/`Options` field JSON | `optional: True` with no `default` on `options`, `connectionTimeout`, `journalMode`, `busyTimeout` — both sides |
| `sed -n '25,66p' store.bal` | `record {\|…\|}` closed; `Options options = {};`, `decimal connectionTimeout = 30.0;` |
| `sed -n '60,110p;205,232p' store.bal` | class doc "Represents a SQLite-backed short-term memory store for messages."; `*ai:ShortTermMemoryStore` inclusion at L69; `init` L95–98; `getAll` L212–213 |
| `grep 'public type ChatMessage\|ChatInteractiveMessage\|MemoryError' <ballerina/ai 1.13.0 bala>` | `ChatMessage` = 4-way union (model-provider.bal:79); `MemoryError distinct Error` (error.bal:96) |
| `curl api.central.ballerina.io/.../ballerinax/ai.sqlite/1.0.0` | 1 module `ai.sqlite`, `deprecated: null`, `visibility: public`, `ballerinaVersion 2201.12.0` |
| `cat ballerina/Ballerina.toml` (upstream) | `version = "1.0.0"`, no compiler-plugin section, `org.xerial:sqlite-jdbc:3.46.1.0` |
| `find . -iname '*compiler-plugin*'` (upstream) | no matches |
| `grep -cE '^type \|^class \|^    function '` on renders | old 3/0/0, new 4/1/14 |
| `OLD_AND_NEW_DIFFS/ai.sqlite_diff.md` claims (+74/−2, 16 added, 0 removed) | verified against the two files |

## 10. Caveats and unverified items

- The renderer source itself was not inspected, so the root cause given for the `ai:ai:` doubling
  (§5.1) is inferred from the JSON-vs-render comparison, not read from the renderer code. The
  observed defect itself is directly verified.
- Semantic equivalence of `int?` ↔ `int|()`, `T?|Error` ↔ `T|()|Error`, and the `ai:ChatMessage`
  union expansion is asserted from the Ballerina type system and the `ballerina/ai` 1.13.0 bala
  definitions; the renders were not compiled (they cannot be, per §5.8).
- Whether the `@display` annotations are consumed by any downstream tooling was not investigated;
  they are reported only as additive content.

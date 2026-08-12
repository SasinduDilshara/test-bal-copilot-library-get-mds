# ballerinax/ai.devant 1.0.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.devant` |
| Pinned version | `1.0.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.devant |
| Tag reviewed | `v1.0.4` (commit `d94fa77`, `git describe` = `v1.0.4`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.devant/1.0.4` |
| Old render | `79` lines |
| New render | `94` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small single-module package (5 `.bal` files, 8 public symbols). Upstream `v1.0.4` sources are
byte-identical to the bala's `modules/ai.devant/*.bal` (all five files `diff` clean), so both renders
were produced from the same source the reviewer can read.

`old` degraded three type defs to bare `// Unknown type:` lines (`Error`, `Chunker`,
`BinaryDataLoader`) — i.e. the two public classes, the entire callable API of the package, were
invisible to an LLM. `new` emits real definitions for all three: 0 `// Unknown type:` lines remain.
Nothing was dropped or reworded: README, module description, the 4 enum-member consts and
`enum ChunkStrategy` are byte-identical between the two renders. **No regression.**

The newly surfaced class bodies do carry accuracy defects (contradictory `init` signature for the
included-record param, wrong default values for 8 inherited `ai:ConnectionConfig` fields, lost
`public isolated` qualifiers, lost class-level docs, lost `*ai:Chunker` inclusion). All of these come
from data that is **identical in both JSONs** — the old renderer simply never printed it — so they
are latent extractor defects newly made visible, not regressions caused by spec v2.

## 2. Change inventory

Render diff (`diff -u old new`): 2 hunks, +18 / −3 lines.

Removed from `old` (3 lines, all placeholders):

| Removed line | Kind |
|---|---|
| `// Unknown type: Error` | type placeholder |
| `// Unknown type: Chunker` | type placeholder |
| `// Unknown type: BinaryDataLoader` | type placeholder |

Added in `new` (7 declarations):

| Kind | Declaration |
|---|---|
| type | `type Error error;` |
| class | `class Chunker { … }` |
| class method (constructor) | `Chunker.init(...)` — 20 rendered params |
| class method | `Chunker.chunk(ai:Document) returns ai:Chunk[]\|ai:Error` |
| class | `class BinaryDataLoader { … }` |
| class method (constructor) | `BinaryDataLoader.init(string path) returns ai:Error?` |
| class method | `BinaryDataLoader.load() returns ai:Document[]\|ai:Document\|ai:Error` |

Unchanged in both renders: 4 `const string` (RECURSIVE / SENTENCE / PARAGRAPH / CHARACTER),
`enum ChunkStrategy` (4 members), README block, 3 `// --- ` section markers, module description.
`clients`, `functions`, `services`, `annotations` are all empty arrays in **both** JSONs.

JSON-level diff (`json.dumps` unified diff = 70 lines, all additive/rewrites, no deletions):
- `+ "type": "Class"` on `Chunker` and `BinaryDataLoader` (this is what unblocks rendering).
- `+ "baseType": "error"` on `Error`.
- `+ "annotations": [{"name":"display", …}]` on 6 params (`serviceUrl`, `accessToken`,
  `maxChunkSize`, `maxOverlapSize`, `strategy`, `connectionConfig`) — new in spec v2.
- `- "name": "ballerina/ai:1.13.0:Error?"` → `+ "name": "ai:Error?"` on 2 returns
  (`Chunker.init`, `BinaryDataLoader.init`) — version-qualified refs removed, an improvement
  (it never reached the old render because the class was a placeholder).

## 3. Correctness against library source

Bala/upstream (`modules/ai.devant/`, paths below are bala = upstream, identical):

| Rendered in `new` | Source | Match |
|---|---|---|
| `class Chunker` | `chunker.bal:23` `public isolated class Chunker` | name yes; `public isolated` and `*ai:Chunker` inclusion dropped |
| `function init(... ) returns ai:Error?` | `chunker.bal:40-45` | params 1-5 + defaults `500`, `50`, `RECURSIVE` and all 5 `@display` labels correct; return correct; included-record param mis-rendered (§5.2) |
| `function chunk(ai:Document document) returns ai:Chunk[]\|ai:Error` | `chunker.bal:66` | exact match (modulo `public isolated`) |
| `class BinaryDataLoader` | `dataloader.bal:23` | name yes; `public isolated` + `*ai:DataLoader` dropped |
| `function init(string path) returns ai:Error?` | `dataloader.bal:30` | exact match |
| `function load() returns ai:Document[]\|ai:Document\|ai:Error` | `dataloader.bal:47` | exact match |
| `type Error error;` | `error.bal:18` `public type Error distinct error;` | `distinct` and `public` lost (§5.1) |
| `enum ChunkStrategy {CHARACTER, PARAGRAPH, SENTENCE, RECURSIVE}` | `types.bal:18-27` | member set correct; declaration order reversed and `= "recursive"` etc. elided (values recovered from the 4 `const string` lines above) — identical in `old`, so not a regression |
| 4 × `const string X = "…"` | `types.bal:20,22,24,26` | values correct |

`Chunker.init`'s flattened HTTP params were checked against `ai:ConnectionConfig`
(`ballerina/ai/1.13.0/java21/modules/ai/types.bal:61-117`): `httpVersion = "2.0"`,
`http1Settings = {}`, `http2Settings = {}`, `cache = {}`, `compression = "AUTO"`,
`responseLimits = {}` are correct; 8 others are not (§5.3).

No invented symbols: every identifier in `new` traces to a source line above.

## 4. Regressions

**None found.** Checks performed to conclude this:
- `diff -u old new` — only 2 hunks, `−3` lines and all three removed lines are
  `// Unknown type:` placeholders; no declaration, doc line, const, enum member or README line is
  deleted.
- Declaration extraction on both files (`grep -nE '^ *(public )?(isolated )?(function|type|class|enum|const|annotation|listener|service)'`):
  old = 5 declarations, new = 12; old's 5 are a subset of new's 12, unchanged verbatim.
- README: `old.readme == new.readme` → `True`, and both equal the bala's `docs/README.md` in full
  (1376 chars, exact prefix + no tail).
- `description` field: `old == new` → `True` (390 chars).
- Version-qualified refs: 0 in both renders; the 2 that existed in the old **JSON**
  (`ballerina/ai:1.13.0:Error?`) are gone in the new JSON — improvement, not loss.
- No annotations, services, clients or functions were present in `old` to lose (all 4 arrays empty
  on both sides).

## 5. Issues in `new` (independent of `old`)

All seven originate in extractor output that is byte-identical in the old JSON; `old`'s renderer
just never printed the class bodies. They are nonetheless what an LLM now consumes.

1. **`type Error error;` loses `distinct` and `public`.** Source is
   `public type Error distinct error;` (`error.bal:18`). The new JSON says
   `"baseType": "error"` — the distinctness is dropped at extraction. An LLM told the type is a plain
   `error` may generate code that treats `devant:Error` as assignable from any error.
2. **`Chunker.init` renders the included-record param twice and drops the `*`.** Source signature
   (`chunker.bal:40-45`) ends with `*ai:ConnectionConfig connectionConfig`. The render emits the 14
   flattened `ai:ConnectionConfig` fields **and then** `@display {label: "Connection Configuration"}
   ai:ConnectionConfig connectionConfig` as a final param with no default (JSON marks it
   `optional: true` but carries no `default`, so the renderer prints it bare, positioned after
   defaulted params). The result is not valid Ballerina and tells the LLM the record can be passed
   both ways at once. 20 params rendered for a 6-param source signature.
3. **8 of the flattened `ai:ConnectionConfig` defaults are wrong** (verified against
   `ballerina/ai/1.13.0/.../ai/types.bal:61-117`):
   - `decimal timeout = 0.0d` — actual `decimal timeout = 60` (line 77).
   - `string forwarded = ""` — actual `= "disable"` (line 81).
   - `boolean validation = false` — actual `= true` (line 116).
   - `poolConfig = {}`, `circuitBreaker = {}`, `retryConfig = {}`, `secureSocket = {}`,
     `proxy = {}` — all five are **optional fields with no default** in the source
     (`poolConfig?` l.85, `circuitBreaker?` l.97, `retryConfig?` l.101, `secureSocket?` l.108,
     `proxy?` l.112). The renderer shows type zero-values instead. `timeout = 0.0d` is the most
     harmful: an LLM copying it would produce a client with a 0-second timeout.
4. **`public isolated` qualifiers dropped** on both classes and all four methods; `isolated` matters
   for using these inside `isolated` contexts / `ai:VectorKnowledgeBase`.
5. **Type inclusions dropped**: `*ai:Chunker` (`chunker.bal:24`) and `*ai:DataLoader`
   (`dataloader.bal:24`) are not rendered, so nothing tells the consumer these classes implement the
   `ai` module's chunker/loader interfaces — the whole point of the package.
6. **Class-level docs replaced by constructor docs.** JSON `typeDefs[Chunker].description` =
   `"Initializes a new \`Chunker\` instance.\n"`, whereas the real class doc is *"Splits documents
   loaded by the `devant:BinaryDataLoader` into smaller chunks using the Devant AI service"*
   (`chunker.bal:21-22`). Same for `BinaryDataLoader` (`dataloader.bal:20-22`, three lines of usage
   guidance, replaced by `"Creates a new \`BinaryDataLoader\` instance."`).
7. **Per-parameter and per-return docs are in the JSON but not rendered**, and the class/method doc
   blocks end in a dangling `# ` line (render lines 78-79, 91-92). Cosmetic + lost detail
   (e.g. `maxOverlapSize`'s two-line explanation).

## 6. Coverage gaps vs. the library

**0 gaps.** `package.json` `export` = `["ai.devant"]` — one module only, the default module, so
there is no submodule-only API and no shared-gap category here.

Full public surface of the default module (`grep -rn "public " modules/ai.devant/*.bal`) and its
presence in `new`:

| Public symbol | Source | In `new`? | In `old`? |
|---|---|---|---|
| `class BinaryDataLoader` | `dataloader.bal:23` | yes | no (placeholder) |
| `BinaryDataLoader.init` | `dataloader.bal:30` | yes | no |
| `BinaryDataLoader.load` | `dataloader.bal:47` | yes | no |
| `enum ChunkStrategy` | `types.bal:18` | yes | yes |
| `type Error` | `error.bal:18` | yes (weakened) | no (placeholder) |
| `class Chunker` | `chunker.bal:23` | yes | no (placeholder) |
| `Chunker.init` | `chunker.bal:40` | yes | no |
| `Chunker.chunk` | `chunker.bal:66` | yes | no |

Non-public module members (`createFileEntity`, `createFormEntity`,
`getContentDispositionForFormData`, `readResponseAsString`, `parseChunks`,
`inheritMetadataFromDocument`, `createDocument` in `utils.bal`; `ChunkData`, `CompletionData`,
`ErrorData` and the 7 non-public consts in `types.bal`; the 2 private `Chunker` methods) are
correctly absent from both renders.

## 7. Compiler plugin

The package ships **no** compiler plugin. Upstream `v1.0.4` has no `compiler-plugin/` or
`*-compiler-plugin/` directory (top level: `LICENSE README.md ballerina build-config build.gradle
gradle gradle.properties gradlew gradlew.bat issue_template.md pull_request_template.md
settings.gradle`; `build-config/` contains only `checkstyle/` and `resources/Ballerina.toml`), and
`ballerina/Ballerina.toml` declares no `[[tool]]`/plugin entry. The bala's top level has only
`bala.json dependency-graph.json docs modules package.json` — no `compiler-plugin/`. Nothing a
plugin would contribute is therefore missing from the render.

Related: the `@display` annotations on `Chunker.init` params are consumed by the
Ballerina Integrator UI (not a plugin artifact); spec v2 now preserves them in the JSON and render,
which is a fidelity gain for that metadata.

## 8. Other considerations

- Pre-1.0-adjacent but stable: `1.0.4`, `distribution = "2201.12.0"`, `graalvmCompatible = true`,
  not a template, no deprecation markers in the bala's `package.json`.
- Size/token impact is negligible: 79 → 94 lines (+19%); the new JSON grew 15,938 → 17,091 bytes
  (+7.2%). The single 1.4 KB `init` line is the bulk of the growth and ~⅔ of it is the redundant
  flattened `ConnectionConfig` block plus the `// Special Agent Note:` trailer.
- The old render was effectively unusable for code generation for this package: with `Chunker` and
  `BinaryDataLoader` both reduced to placeholders, the only machine-readable API left was an enum
  and four consts. The README's Quickstart was the sole source of usage information. `new` fixes
  exactly that, which is why the verdict is an improvement despite §5.
- Docs quality in the library itself is good (every public member has a doc comment with `+ param`
  and `+ return` lines); the loss in §5.6/§5.7 is renderer-side, not the library's fault.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 79 / 94 |
| `diff -u old/…bal.txt new/…bal.txt` | 2 hunks, +18 / −3 |
| `grep -c '^// Unknown type:'` old / new | `3` / `0` |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new render | `0` / `0` |
| `grep -c '^// --- '` (via diff report, re-checked) | 3 markers in both |
| `grep -nE '^ *(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service)'` | old 5 decls, new 12 decls |
| `wc -c old/*.json new/*.json` | 15,938 / 17,091 |
| Python: JSON top-level key/array sizes both sides | `typeDefs` 8 both; `clients`/`functions`/`services`/`annotations` = 0 both; `readme` 1376 both; `description` 390 both |
| Python: `old["readme"]==new["readme"]`, `old["description"]==new["description"]` | `True`, `True` |
| Python: readme vs bala `any/docs/README.md` | equal length 1376, exact prefix, no tail → README rendered in full |
| Python: unified diff of pretty-printed JSONs | 70 lines; additions only (`type: Class` ×2, `baseType: error`, 6 × `annotations`) + 2 rewrites (`ballerina/ai:1.13.0:Error?` → `ai:Error?`); zero deletions |
| Python: per-typeDef equality | `ChunkStrategy` identical; `Error`, `Chunker`, `BinaryDataLoader` differ only as above |
| Python: dump of `Chunker.init` params in new JSON | 20 params; `timeout` default `'0.0d'`, `forwarded` `'""'`, `validation` `'false'`, `poolConfig/circuitBreaker/retryConfig/secureSocket/proxy` `'{}'`, `connectionConfig` `optional: True` with **no** `default` |
| `git ls-remote --tags <repo>` | tags `v1.0.0`…`v1.0.4`; exact match `v1.0.4` |
| `git clone --depth 1 --branch v1.0.4` + `git log -1` / `git describe --tags` | `d94fa77` / `v1.0.4` |
| `diff ballerina/<f>.bal` vs `bala modules/ai.devant/<f>.bal` for all 5 files | identical (chunker, dataloader, error, types, utils) |
| `cat ballerina/Ballerina.toml` | `org=ballerinax name=ai.devant version=1.0.4 distribution=2201.12.0`, no `[[tool]]` |
| `ls` bala `any/` and `any/modules/` | `bala.json dependency-graph.json docs modules package.json`; modules = `ai.devant` only |
| `package.json` `export` | `["ai.devant"]` (single default module) |
| `grep -rn "public " modules/ai.devant/*.bal` | 8 public symbols (listed in §6) |
| `grep -n "ConnectionConfig" -A45` in `ballerina/ai/1.13.0/java21/modules/ai/types.bal` | `timeout = 60` (l.77), `forwarded = "disable"` (l.81), `poolConfig?` (l.85), `circuitBreaker?` (l.97), `retryConfig?` (l.101), `secureSocket?` (l.108), `proxy?` (l.112), `validation = true` (l.116) |
| `dependency-graph.json` | ai.devant depends on `ballerina/http 2.14.11`, `auth 2.14.0`, … ; old JSON confirms `ballerina/ai:1.13.0` |
| `ls build-config`, top-level upstream listing | no compiler-plugin directory |

## 10. Caveats and unverified items

- Neither render was compiled. Statements about `new`'s `Chunker.init` line not being valid
  Ballerina (§5.2) are from reading the grammar (a param with no default cannot follow defaulted
  params; the included-record `*` is absent while its fields are also listed), not from a compiler
  run.
- `ai:ConnectionConfig` defaults were checked against the locally cached `ballerina/ai 1.13.0` bala,
  which is the version the old JSON's version-qualified refs (`ballerina/ai:1.13.0:Error?`) name.
  The bala's `dependency-graph.json` lists direct deps but I did not find an explicit `ballerina/ai`
  pin inside it, so the 1.13.0 attribution rests on the old JSON's qualified ref plus that being the
  only `ballerina/ai` version in the local repository.
- Not investigated: whether the `@display`-annotation additions or the `Class`/`baseType` tagging
  affect downstream prompt assembly beyond `toSyntaxString` (out of scope — only the two renders and
  two JSONs were compared).
- The renderer/extractor source (`ballerina-vscode`, either side) was not read; attribution of §5
  defects to "extractor, unchanged by spec v2" is inferred from the two JSONs being identical on
  those fields, not from reading the Java code.

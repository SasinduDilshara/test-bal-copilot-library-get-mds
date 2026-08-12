# ballerinax/mistral 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mistral` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mistral |
| Tag reviewed | `v1.0.2` (commit `f9e721a9d44f958c1bebac496c4d17f9c3b8f212`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mistral/1.0.2` |
| Old render | `1248` lines |
| New render | `1409` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Every difference is an improvement:

- The one degraded declaration in `old` (`// Unknown type: ToolTypes`) is replaced by the correct
  definition `type ToolTypes "function";` (matches `types.bal:701`).
- 161 annotation lines (`@jsondata:Name`, `@http:Query`, `@constraint:*`, `@display`) are emitted in
  `new`; `old` emitted **zero** real annotations. Every single one was verified to exist in the bala
  source, on the same field. Zero invented annotations.
- 5 lines carrying 14 version-qualified type references (`ballerinax/mistral:1.0.2:TextChunk|…`) are
  replaced by plain type names in `new`.
- 5 client resource-function signatures lose a fabricated, non-compiling parameter
  `anydata Additional Values` that `old` emitted.
- 3 record fields named `object` (a reserved word — non-compiling in `old`) are correctly quoted as
  `'object` in `new`.

Nothing was dropped, truncated or made less accurate. README section, doc comments (243 `#` lines on
both sides) and the full public API surface are byte-identical or improved.

The residual inaccuracies listed in §5 are shared with `old` (pre-existing renderer limitations), not
introduced by spec v2.

## 2. Change inventory

Line counts (`wc -l`): old `1248`, new `1409` (+161).
Diff: 176 added lines, 14 removed lines (`diff -u` → 886-line diff file).

Section markers (`grep -n '^// --- '`) — identical structure on both sides, 4 markers each:

| marker | old line | new line |
|---|---|---|
| `// --- README ---` | 7 | 7 |
| `// --- END README ---` | 92 | 92 |
| `// --- Types ---` | 94 | 94 |
| `// --- Client ---` | 1131 | 1292 |

### Declarations

| kind | old | new | delta |
|---|---|---|---|
| `type` declarations (`^type `) | 102 | 103 | **+1** (`ToolTypes`) |
| `client class Client` | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `resource function` | 28 | 28 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | **−1** |
| module-level `function` / `enum` / `const` / `annotation` / `service` / `listener` | 0 | 0 | 0 |

Declaration-name diff (`diff old.types new.types`): the only difference is `> type ToolTypes`.
**Zero declarations removed.**

### Non-declaration changes

| change | count | direction |
|---|---|---|
| `@jsondata:Name {...}` lines | 0 → 139 | added |
| `@http:Query {name: ...}` lines | 0 → 11 | added |
| `@constraint:{Int,Number,Array} {...}` lines | 0 → 10 | added |
| `@display {label: "Connection Config"}` | 0 → 1 | added |
| lines with `org/mod:x.y.z:Type` refs | 5 → 0 | removed (14 refs) |
| `anydata Additional Values` client params | 5 → 0 | removed |
| `string object?;` (reserved word, unquoted) | 3 → 0 | fixed to `string 'object?;` |
| doc-comment (`#`) lines | 243 → 243 | unchanged |
| non-ASCII bytes | 0 → 0 | unchanged |

### JSON-level inventory

Both JSONs: `typeDefs` = 103, `clients` = 1 (29 functions incl. `init`), `functions`/`services`/
`annotations` = 0. `name`, `description` (317 chars) and `readme` (3012 chars) are byte-identical.
Type-name sets are identical; kind histogram identical (`Record` 89, `Union` 13, `Other` 1).
Structural key diff across all 103 typeDefs: `new` adds `annotations` on 161 nodes and `baseType` on
1 node (`ToolTypes`). Client diff: 5 functions lose exactly one parameter each — in every case the
object `{"name": "Additional Values", "description": "Capture key value pairs", "type": {"name":
"anydata"}, "optional": true}`.

## 3. Correctness against library source

The bala module source and the GitHub `v1.0.2` tree are **identical** (`diff -r` of
`bala/…/modules/mistral/` vs `src/ballerina/` reports only `README.md` and `icon.png` as extra in the
repo — all three `.bal` files match byte-for-byte). So bala and upstream agree; no tie-break needed.

**`ToolTypes` (the only added declaration).** `types.bal:701` — `public type ToolTypes "function";`.
New render line 121: `type ToolTypes "function";` — exact match.

**Union types de-qualified (5).** All verified against `types.bal`:

| render (new) | source | ok |
|---|---|---|
| `type ContentChunk TextChunk\|ImageURLChunk\|DocumentURLChunk\|ReferenceChunk;` (l.186) | `types.bal:279` | ✔ |
| `type ModelListData BaseModelCard\|FTModelCard;` (l.573) | `types.bal:253` | ✔ |
| `type ResponseRetrieveModelV1ModelsModelIdGet BaseModelCard\|FTModelCard;` (l.986) | `types.bal:592` | ✔ |
| `type AgentsCompletionRequestMessages SystemMessage\|UserMessage\|AssistantMessage\|ToolMessage;` (l.1168) | `types.bal:798` | ✔ |
| `type Response JobOut\|LegacyJobMetadataOut;` (l.1281) | `types.bal:1009` | ✔ |

**Annotations — exhaustive verification, not a spot check.** Multiset of annotation strings in the
bala `.bal` sources vs the new render:

| annotation | source | new render | delta | explained by |
|---|---|---|---|---|
| `@jsondata:Name {value: "api_key"}` | 1 | 2 | +1 | alias `JobInIntegrations = WandbIntegration` (`types.bal:714`) inlined |
| `@jsondata:Name {value: "commit_id"}` | 1 | 2 | +1 | alias `DetailedJobOutRepositories = GithubRepositoryOut` (`types.bal:796`) |
| `@jsondata:Name {value: "run_name"}` | 2 | 4 | +2 | aliases `JobInIntegrations` + `DetailedJobOutIntegrations = WandbIntegrationOut` (`types.bal:590`) |
| `@constraint:Number {minValueExclusive: 0}` | 3 | 5 | +2 | aliases `JobInRepositories = GithubRepositoryIn` (`types.bal:480`) + `DetailedJobOutRepositories` |
| **all other 40 distinct annotation strings** | — | — | **0** | exact match |

Every one of the four deltas is fully accounted for by the four `public type X Y;` record aliases the
renderer inlines structurally (on both sides). **No annotation in `new` is invented, and none from the
source is missing.** An annotation→attached-field-name pairing check (`@…` line → next non-doc field
name) produced the same set on both sides modulo those 6 alias duplicates.

**`@display` (type-level).** `types.bal:141-143` carries `@display {label: "Connection Config"}` on
`ConnectionConfig`; new render line 361 reproduces it. `old` had it nowhere (old's only two `@`
occurrences are inside README curl examples at lines 529/533).

**Reserved-word quoting.** `types.bal` declares the field as `'object` in 21 places. `old` emitted
`string object?;` 3 times (uncompilable); `new` emits `string 'object?;`.

**Client surface.** `client.bal` declares `public isolated function init` + 28 `resource isolated
function`s. Both renders emit `function init` + 28 `resource function`s; the accessor/path/return
type of each was compared line-by-line via the unified diff — only the 5 `Additional Values`
parameter removals differ.

## 4. Regressions

**None found.**

Checked, with the result of each check:

- Declaration-name set: `diff` of the sorted `^type ` name lists shows one addition, zero removals.
- JSON typeDef name sets: identical (`set(old) == set(new)` → `True`; both empty-difference).
- Removed-line inventory: `grep '^-' full.diff` yields 14 lines, all of them either the
  `// Unknown type:` placeholder, a version-qualified union alias replaced by its plain form, an
  unquoted `object` field replaced by `'object`, or a client signature whose only change is deletion
  of the fabricated `anydata Additional Values` parameter. No declaration, parameter, default,
  return type or doc line disappears.
- Doc comments: 243 `#` lines on both sides.
- README section (lines 7–92): `diff` reports no difference.
- README/description/name in the JSON: byte-identical.
- Client method count, order, accessors, resource paths and return types: unchanged.
- Parameter defaults in client signatures: unchanged between sides (both carry the same values,
  including the same pre-existing wrong ones noted in §5).

## 5. Issues in `new` (independent of `old`)

All six below are present in `old` as well — they are pre-existing renderer limitations, not spec v2
regressions. They are listed because they are inaccuracies an LLM consuming the render would inherit.

1. **All record-field default values are dropped; defaulted fields are shown as optional.**
   `grep -cE '^    [^#/].* = .*;$' types.bal` → **116** defaulted fields in the source; the Types
   section of both renders contains **0**. Examples:
   `types.bal:449 int pageSize = 100;` → render l.869 `int pageSize?;`;
   `types.bal:764 int expiry = 24;` → render l.1135 `int expiry?;`;
   `types.bal:22 int index = 0; string id = "null";` (`ToolCall`) → render ll.110-111
   `int index?; string id?;`;
   `types.bal:147 http:HttpVersion httpVersion = http:HTTP_2_0;` → render l.366 `httpVersion?;`.
   This both loses the documented default and misstates required-with-default fields as optional.

2. **Closed records are rendered as open.** Source has 31 `record {|` declarations and 54
   `record {`; both renders emit `record {` for all 89 records (`grep -cE '^type .* record \{\|$'`
   → 0). E.g. `ConnectionConfig` (`types.bal:143`, closed) renders open at l.362.

3. **Client query parameters are double-rendered, with two materially wrong defaults.** The source
   signature is `resource isolated function get files(map<…> headers = {}, *FilesApiRoutesListFilesQueries queries)`
   (`client.bal:55`). Both renders flatten the included record into individual parameters **and**
   keep a trailing required `FilesApiRoutesListFilesQueries queries` parameter (new l.1312) — a
   signature that does not compile and does not exist. Worse, the flattened defaults are wrong:
   - `int pageSize = 0` in the render vs `int pageSize = 100` in `types.bal:449` / `510`
     (3 client methods affected: `get files`, `get fine_tuning/jobs`, `get batch/jobs`).
   - `int expiry = 0` (new l.1332) vs `int expiry = 24` in `types.bal:764`.
   - `FilePurpose purpose = "fine-tune"` and `BatchJobStatus status = "QUEUED"` are invented — the
     source fields (`types.bal:443`, `511`) have no default; the value shown is just the first union
     member of `FilePurpose` (`types.bal:514`) / `BatchJobStatus` (`types.bal:288`).

4. **Type aliases are inlined structurally, losing the alias.** The 4 `public type X Y;` aliases at
   `types.bal:480, 590, 714, 796` are emitted as full copies of the target record (e.g. new
   ll.1104-1116 `type JobInIntegrations record { … }` duplicating `WandbIntegration` at
   ll.1090-1102). The render never states that they are the same type.

5. **One doc comment is broken across lines.** `ConnectionConfig.laxDataBinding`'s two-line doc
   (`types.bal:180-181`) renders as l.399 `# Enables relaxed data binding…` followed by l.400
   `and absent fields are handled as \`nilable\` types. Enabled by default.` with **no `#` prefix** —
   a bare statement in type position. Same defect at lines 100 and 102 (`JobsApiRoutes…Queries`
   doc). 3 occurrences, identical in `old`.

6. **Render is not compilable as written.** `public` is stripped from every declaration, and the
   annotation modules now referenced (`jsondata`, `http`, `constraint`) are not imported — the
   preamble has only `import ballerinax/mistral;`. Additionally, the flattened `get files` signature
   uses the parameter name `source` unquoted (new l.1312) whereas the source record field is
   `'source` (`types.bal:445`). This is presentational for an LLM-facing artefact, but worth noting.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`. One gap in `old` (now closed).**

Method: extracted every `public …` module-level declaration from the bala default module
(`modules/mistral/{client,types,utils}.bal`) → 104 symbols (103 types + `Client`); extracted the
rendered declaration names from `new` → 103 `type` names + `client class Client`.
`comm -23 bala.names new.names` → `Client` only (which *is* rendered, as `client class Client`, so
it is a naming artefact of the extraction, not a gap). `comm -13` → empty (no invented symbols).

- `old` did not render the body of `ToolTypes` (`// Unknown type: ToolTypes`) — 1 gap, closed by `new`.
- `utils.bal` contains 9 module-level functions, all non-`public` (`isolated function
  getDeepObjectStyleRequest`, `getFormStyleRequest`, `getSerializedArray`,
  `getSerializedRecordArray`, `getEncodedUri`, `getPathForQueryParam`, `createBodyParts`,
  `constructEntity`, `populateEncodingInfo`) — correctly absent from both renders.
- **No submodule gap.** `package.json` `"export": ["mistral"]` and the bala contains exactly one
  module directory, `modules/mistral`. The whole public API lives in the default module, so the
  known `getDefaultModule()`-only extraction limitation costs nothing here.

## 7. Compiler plugin

**The package ships no compiler plugin.** Evidence:
- The bala at `1.0.2/any/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json` — there is **no** `compiler-plugin/` directory and no `compiler-plugin.json`.
- The upstream repo at `v1.0.2` has no `compiler-plugin`, `*-compiler-plugin` or
  `ballerina-*-compiler-plugin` directory; top-level contents are `LICENSE README.md ballerina
  build-config build.gradle docs examples gradle gradle.properties gradlew gradlew.bat
  issue_template.md pull_request_template.md settings.gradle`.
- `ballerina/Ballerina.toml` declares no `[[tool.…]]` or plugin section.

Consequently nothing plugin-derived is expected in the render and nothing is missing.

## 8. Other considerations

- **Size / tokens.** `new` is 12.9% longer (1248 → 1409 lines). The growth is entirely annotation
  lines. Those annotations carry real information an LLM needs — the JSON wire names
  (`@jsondata:Name`), the HTTP query names (`@http:Query`), and validation bounds
  (`@constraint:*`) — without which generated code would serialise to the wrong field names. Good
  value for the token cost.
- **Version.** Stable `1.0.2`; no deprecation flag in `package.json`. Built with
  `ballerina_version 2201.12.0` (bala) / `distribution = "2201.12.4"` (repo toml) — a normal
  build-vs-source skew, not a problem.
- **Doc quality.** Every client method's doc block is `# <Title>` followed by an empty `# ` line —
  the OpenAPI operation description is empty upstream, so both renders inherit terse method docs.
  Record fields are well documented (243 doc lines).
- **README fidelity.** The 86-line README block is identical on both sides and matches the bala
  `docs/README.md` content in the JSON (`readme` field, 3012 chars, identical old vs new).
- The bala and the GitHub tag agree exactly, so this review had no source-of-truth ambiguity.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags …module-ballerinax-mistral` | `v1.0.0`, `v1.0.1`, `v1.0.2` — exact tag exists |
| 2 | `git clone --depth 1 --branch v1.0.2 …`; `git log -1` | `f9e721a9d44f958c1bebac496c4d17f9c3b8f212`, `tag: v1.0.2` |
| 3 | `diff -r bala/…/modules/mistral/ src/ballerina/ --exclude=tests …` | only `README.md`, `icon.png` extra in repo — `.bal` files identical |
| 4 | `ls bala/…/1.0.2/any/modules` | single module `mistral` — no submodules |
| 5 | `wc -l bala/…/modules/mistral/*.bal` | client 327, types 1067, utils 288 |
| 6 | `wc -l old/new render` | 1248 / 1409 |
| 7 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 8 | `grep -n '^// --- '` both | 4 markers each; Client at 1131 (old) / 1292 (new) |
| 9 | `diff -u old new \| wc -l` | 886 lines; `grep -c '^+'` → 176; removed lines → 14 |
| 10 | `grep -oE '^type [A-Za-z0-9_]+' \| sort` + `diff` | old 102, new 103; only difference `> type ToolTypes` |
| 11 | `grep -c '    resource function '` | 28 both |
| 12 | `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 5 lines (14 refs), new 0 |
| 13 | `grep -c '@jsondata:Name' / '@http:Query' / '@constraint:'` new | 139 / 11 / 10; `grep -cE '^\s*@'` → 161 |
| 14 | `grep -n '@' old render` | 2 hits, both inside README curl examples (ll. 529, 533) — no real annotations |
| 15 | annotation multiset `diff` src `*.bal` vs new render | 4 differences only: `+2` `@constraint:Number`, `+1` `api_key`, `+1` `commit_id`, `+2` `run_name` |
| 16 | `grep -nE '^public type [A-Za-z0-9_]+ [A-Za-z0-9_]+;$' types.bal` | 4 aliases at ll. 480, 590, 714, 796 — exactly account for the 6 duplicate annotations |
| 17 | annotation→field-name pairing extraction, src vs new | same set modulo the 6 alias duplicates; zero misattached |
| 18 | `types.bal:701` vs new l.121 | `public type ToolTypes "function";` ↔ `type ToolTypes "function";` |
| 19 | `types.bal:279 / 253 / 592 / 798 / 1009` vs new ll. 186 / 573 / 986 / 1168 / 1281 | all 5 unions match exactly |
| 20 | `types.bal:141-143` vs new l.361 | `@display {label: "Connection Config"}` present in new, absent in old |
| 21 | JSON structural walk old vs new (103 typeDefs) | added keys: `annotations` ×161, `baseType` ×1; no removed keys |
| 22 | JSON client function param diff | 5 functions each lose exactly `{"name":"Additional Values",…,"type":{"name":"anydata"}}` |
| 23 | JSON `readme`/`description`/`name` equality | all `True`; typeDef name sets equal |
| 24 | `grep -cE '^\s*#'` both renders | 243 / 243 |
| 25 | `diff <(sed -n '7,92p' old) <(sed -n '7,92p' new)` | no difference (README block identical) |
| 26 | `LC_ALL=C grep -c '[^ -~]'` both | 0 / 0 — no encoding damage |
| 27 | `grep -cE '^    [^#/].* = .*;$' types.bal` vs Types section of renders | 116 source defaults → 0 rendered, both sides |
| 28 | `grep -c 'record {\|$' types.bal` / renders | 31 closed in source, 0 closed in either render (89 open) |
| 29 | `types.bal:449 / 510 / 764` vs new ll. 1312 / 1332 / 1365 | `pageSize = 100` → `= 0`; `expiry = 24` → `= 0` (same in old) |
| 30 | `awk` scan for doc lines missing `#` | 3 in each render (ll. 100, 102, 364/400) — identical count |
| 31 | `grep -n '^public…' utils.bal` | 9 module-level functions, none `public` |
| 32 | `comm` bala public symbols (104) vs new render names | `comm -23` → `Client` (rendered as `client class`); `comm -13` → empty |
| 33 | `find bala/…/1.0.2/any -maxdepth 2`; `ls src/` | no `compiler-plugin/`, no `compiler-plugin.json` on either side |
| 34 | `cat src/ballerina/Ballerina.toml` | version `1.0.2`, org `ballerinax`, no tool/plugin section |
| 35 | `cat bala/…/package.json` | `"version": "1.0.2"`, `"export": ["mistral"]`, no deprecation |

## 10. Caveats and unverified items

- Neither render was compiled. Claims about non-compiling constructs (`string object?;` in `old`,
  the duplicated `queries` parameter, missing annotation imports, stripped `public`) are from reading
  the text against the Ballerina grammar, not from a `bal build` run. This does not affect the
  verdict, since the constructs in question are identical or strictly better in `new`.
- Central registry metadata was not re-queried over the network for this library; version, export
  list, keywords and absence of deprecation were read from the bala's `package.json`, which is the
  artefact the extractor actually consumed.
- The `@constraint:*` semantics (e.g. whether `minValueExclusive: 0` on `decimal weight` matches the
  upstream OpenAPI spec) were verified only against the Ballerina source, not against Mistral's
  published OpenAPI document.
- Everything else in this report was verified by a command listed in §9.

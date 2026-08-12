# ballerinax/openai.audio 3.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/openai.audio` |
| Pinned version | `3.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-openai.audio |
| Tag reviewed | `v3.0.0` (exact tag, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/openai.audio/3.0.0` |
| Old render | `2991` lines |
| New render | `3286` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing was dropped: the removed-line
inventory is 38 lines, and every one of them is either (a) a `// Unknown type:` placeholder replaced
by a real type definition, (b) a version-qualified type reference replaced by the plain name, or
(c) a resource-function signature from which a **fabricated, non-compiling parameter**
(`anydata Additional Values`) was removed.

The dominant addition is annotation fidelity: `new` emits 301 annotation lines, and the multiset of
annotation lines in the render is **byte-identical** to the multiset in the published bala source
(`@jsondata:Name` ×281, `@deprecated` ×8, `@constraint:Array` ×6, `@constraint:Int` ×2,
`@constraint:Number` ×1, `@constraint:String` ×1, `@display` ×1, `@http:Query` ×1). `old` carried
only the 8 `@deprecated` lines. Since this connector's Ballerina field names are camelCase while the
OpenAI wire format is snake_case, the 281 `@jsondata:Name` annotations are the only thing that tells
a consuming LLM what the JSON keys actually are — a substantial accuracy gain.

Coverage against the default module is now complete: 0 public symbols missing (was 6).

Remaining inaccuracies are pre-existing and identical on both sides (record-field defaults dropped,
query-record params flattened with invented defaults). They are listed in §5 for completeness but are
not regressions.

## 2. Change inventory

Line counts (`wc -l`): old **2991**, new **3286**. Unified diff: **+333 / −38** added/removed lines,
122 hunks.

Section markers: 4 on both sides (`README`, `END README`, `Types`, `Client`) — README body
byte-identical (`diff` of lines 7–98 on both files: no output).

Declaration counts (grep on line-start declaration keywords):

| Kind | old | new | delta |
|---|---|---|---|
| `type` | 231 | 237 | +6 |
| `client class` | 1 | 1 | 0 |
| `public function` (README sample `main`) | 1 | 1 | 0 |
| `resource function` (inside client) | 68 | 68 | 0 |
| `function init` | 1 | 1 | 0 |
| `// Unknown type:` placeholders | 6 | 0 | −6 |

Declarations added (6) — exactly the 6 that `old` degraded to `// Unknown type:`:

| Added in `new` | Rendered as |
|---|---|
| `ParallelToolCalls` | `type ParallelToolCalls boolean;` |
| `InputItemsArray` | `type InputItemsArray int[];` |
| `ChatCompletionMessageToolCalls` | `type ChatCompletionMessageToolCalls ChatCompletionMessageToolCall[];` |
| `PromptItemsArray` | `type PromptItemsArray int[];` |
| `CreateThreadRequestToolResourcesFileSearch` | `type CreateThreadRequestToolResourcesFileSearch anydata;` |
| `CreateAssistantRequestToolResourcesFileSearch` | `type CreateAssistantRequestToolResourcesFileSearch anydata;` |

Declarations removed: **0** (`comm -23` of the sorted declaration sets yields only the 20
version-qualified union lines, each of which reappears in `new` in unqualified form).

Annotations:

| Annotation | old render | new render | bala source |
|---|---|---|---|
| `@jsondata:Name` | 0 | 281 | 281 |
| `@deprecated` | 8 | 8 | 8 |
| `@constraint:Array` | 0 | 6 | 6 |
| `@constraint:Int` | 0 | 2 | 2 |
| `@constraint:Number` | 0 | 1 | 1 |
| `@constraint:String` | 0 | 1 | 1 |
| `@display` | 0 | 1 | 1 |
| `@http:Query` | 0 | 1 | 1 |
| **total** | **8** | **301** | **301** |

Type-reference qualification: `ballerinax/openai.audio:3.0.0:` appears **51 times on 20 lines** in
`old`, **0 times** in `new`.

Client surface: 69 functions on both sides (68 resource functions + `init`); the accessor+path key
sets are identical. **12** of the 69 differ, all by removal of the `anydata Additional Values`
parameter — after deleting that parameter from the `old` JSON, all 69 function objects compare
byte-identical to `new` (`json.dumps(..., sort_keys=True)`, residual diffs = 0).

JSON level: `typeDefs` = 237 on both sides, identical name sets, identical kind histogram
(`Record` 208, `Union` 23, `Other` 6). `new` adds four JSON key paths that `old` lacks:
`typeDefs[].baseType`, `typeDefs[].annotations[].{name,value}`,
`typeDefs[].fields[].annotations[].{module,name,value}`. No key path exists only in `old`.

## 3. Correctness against library source

Bala default module `openai.audio` contains `client.bal` (857 l), `types.bal` (2692 l),
`utils.bal` (304 l). GitHub `v3.0.0` `ballerina/` matches (same three `.bal` files).

**The 6 newly-rendered types — all exact, including doc text:**

| Render (new) | Bala source |
|---|---|
| `type InputItemsArray int[];` (l.544) | `types.bal:127 public type InputItemsArray int[];` |
| `# The tool calls generated by the model, such as function calls` / `type ChatCompletionMessageToolCalls ChatCompletionMessageToolCall[];` (l.654-655) | `types.bal:227-228` — same doc, same base type |
| `# Whether to enable [parallel function calling](...) during tool use` / `type ParallelToolCalls boolean;` (l.401-402) | `types.bal:268-269` — same doc, same base type |
| `type PromptItemsArray int[];` (l.1447) | `types.bal:724` |
| `type CreateThreadRequestToolResourcesFileSearch anydata;` (l.1927) | `types.bal:1828` |
| `type CreateAssistantRequestToolResourcesFileSearch anydata;` (l.2830) | `types.bal:2387` |

**All 301 annotations verified.** Two independent checks:

1. Multiset equality of annotation text: `grep '^\s*@'` on `new/*.bal.txt` vs on
   `bala/types.bal + client.bal`, both `sort | uniq -c` → `diff` produced no output
   (`ANNOTATION_MULTISETS_IDENTICAL`).
2. Attachment check: each `@jsondata:Name` paired with the declaration line that follows it (skipping
   further annotations) — 281 pairs on each side; after normalising the three known cosmetic
   renderings (`T?` ↔ `T|()`, field-with-default ↔ optional field, `record {}` ↔
   `record {|anydata...;|}`) and union-member ordering, the pair sets agree.

Spot checks against source line numbers:

- `FineTuningJobCheckpoint`: render l.114-132 vs `types.bal:35-53` — all 4 `@jsondata:Name` values
  (`step_number`, `created_at`, `fine_tuning_job_id`, `fine_tuned_model_checkpoint`) and their fields
  match exactly.
- `CreateSpeechRequest`: render l.736-750 — `@constraint:String {maxLength: 4096}` on `input`
  (`types.bal:309-310`), `@constraint:Number {minValue: 0.25, maxValue: 4.0}` on `speed`
  (`types.bal:317-318`), `@jsondata:Name {value: "response_format"}` on `responseFormat`.
- `ListMessagesQueries`: render l.917 `@http:Query {name: "run_id"}` on `runId` — `types.bal:369-370`.
- `ConnectionConfig`: render l.593 `@display {label: "Connection Config"}` — matches source.
- `VectorStoreExpirationAfter`: render l.1369 `@constraint:Int {minValue: 1, maxValue: 365}` on
  `days` — `types.bal:1142-1143`.
- `RunObject.tools`: render l.~180 `@constraint:Array {maxLength: 20}` — `types.bal:1052`.
- All 8 `@deprecated` sites match: 5 on types (`ChatCompletionFunctions`,
  `ChatCompletionRequestAssistantMessageFunctionCall`, `ChatCompletionRequestFunctionMessage`,
  `ChatCompletionResponseMessageFunctionCall`) and fields (`functions`, `functionCall`, `status`,
  `status_details`), same set as `old`.

**Signature correction verified.** `client.bal:150` is
`resource isolated function get files(map<string|string[]> headers = {}, *ListFilesQueries queries) returns ListFilesResponse|error`.
`ListFilesQueries` (`types.bal:2485-2488`) has exactly one field, `string purpose?`, and **no rest
descriptor**. `old` nevertheless rendered a parameter literally named `Additional Values` of type
`anydata` — a symbol that does not exist in the library and is not even a legal Ballerina identifier.
`new` does not emit it. Same confirmed for `get assistants` (`client.bal:392`) and
`get batches` (`client.bal:819`).

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Every removed line in the unified diff was enumerated (`grep '^-' full.diff`, 38 lines) and
  classified: 20 version-qualified union type refs (re-emitted unqualified), 6 `// Unknown type:`
  placeholders (replaced by real definitions), 12 resource-function signatures (re-emitted without
  the fabricated `anydata Additional Values` parameter). No other removals exist.
- Declaration-set comparison (`comm` on sorted, prefix-stripped declaration lines): 0 declarations
  present in `old` and absent from `new`.
- Public-symbol coverage: `comm -23 bala_syms new_syms` → empty (see §6).
- Client JSON: identical 69-function key set; after removing the bogus parameter from `old`, 0
  residual differences across all 69 functions — no parameter, default, or return type was lost.
- README section (lines 7–98) byte-identical.
- Doc-comment prose: no docs dropped. `new` has 20 unprefixed doc-continuation prose lines vs 18 in
  `old`; the 2 extra belong to the newly added type definitions, i.e. more doc text, not less
  (the missing `#` prefix on continuation lines is a pre-existing renderer trait — see §5).
- Non-ASCII content: 1 line on each side (an en dash at `new:1422` / the corresponding `old` line) —
  no encoding regression.

## 5. Issues in `new` (independent of `old`)

All of the following are also present in `old` — they are pre-existing renderer traits, not caused by
spec v2 — but they are inaccuracies a reviewer should know about.

1. **Record field default values are dropped.** `types.bal:318 decimal speed = 1.0;` renders as
   `decimal speed?;` (new l.749, old l.683). Same for `CreateAssistantRequest.topP`
   (`types.bal:2495 decimal? topP = 1;` → `decimal? topP?;`, new l.2870 / old l.2583) and for
   `ListAssistantsQueries.'limit` (`types.bal:2331 int 'limit = 20;` → `int 'limit?;`, new l.2810).
   An LLM reading the render cannot recover the documented defaults.
2. **Closed records rendered as open.** `types.bal` contains 32 `record {|` inclusive-record
   declarations; neither render emits a single `record {| ... |}` type declaration (grep count 0 on
   both). E.g. `CreateAssistantRequest` is `record {|...|}` in source, `record {` in both renders.
3. **Included-record query parameters are both flattened *and* duplicated, with invented defaults.**
   Source: `get assistants(map<string|string[]> headers = {}, *ListAssistantsQueries queries)`.
   Render (both sides): `resource function get assistants(map<string|string[]> headers = {}, string before = "", int limit = 0, string after = "", "asc"|"desc" order = "asc", ListAssistantsQueries queries)`.
   Three problems: the `*` inclusion is lost so the record param is shown as an ordinary (and
   required, trailing, after-defaults) param — non-compiling; the fields appear twice; and the
   defaults are wrong — source has `'limit = 20` and `'order = "desc"` (`types.bal:2331,2335`) but the
   render says `limit = 0` and `order = "asc"`. This affects the 12 `get`-list resource functions.
   Likewise `filter = "in_progress"` is shown for `ListVectorStoreFilesQueries.filter`, which is
   `filter?` with no default in source (`types.bal:248`).
4. **Multi-line doc comments lose the `#` prefix on continuation lines** (20 occurrences in `new`),
   e.g. new l.2867-2868 where `We generally recommend altering this or temperature but not both`
   appears as bare, unindented prose inside a record body — non-compiling Ballerina.
5. **No imports for the annotation modules.** `new` now emits `@jsondata:Name`, `@constraint:*` and
   `@http:Query`, but the render's only import line is `import ballerinax/openai.audio;`
   (l.5 and l.50). The source needs `ballerina/data.jsondata`, `ballerina/constraint`,
   `ballerina/http` (`client.bal:20-22`, `types.bal:20-22`). Code copied verbatim from the render
   would not compile. This is a *new-only* side effect of emitting annotations, though a mild one —
   the render is a reference stub, not a compilable unit, and `old` was equally non-compiling for
   other reasons (items 3–4 above, plus `anydata Additional Values`).
6. **Annotation ordering swapped in one place.** Source `types.bal:428-430` is
   `@constraint:Array {maxLength: 128, minLength: 1}` then `@deprecated`; `new` l.974-976 emits
   `@deprecated` then `@constraint:Array`. Semantically identical; cosmetic only.

## 6. Coverage gaps vs. the library

**0 gaps in `new`.**

`grep -hoE '^public (isolated )?(type|class|const|enum|function|annotation) NAME'` over the bala's
`modules/openai.audio/*.bal` yields **237** distinct public symbols. The `new` render's declaration
names yield **238** — the 237 plus `main`, which is the `public function main()` inside the README
code sample, not a library export. `comm -23 bala_syms new_syms` → empty.

`old` had **6** gaps, exactly the 6 types listed in §2 (they were emitted as `// Unknown type: X`
comments with no definition, so a consumer got the name but neither the base type nor the doc).

No submodule gap: `package.json` `"export": ["openai.audio"]`, the bala has exactly one directory
under `modules/` (`openai.audio`), and Central lists one module for `3.0.0`. Everything public lives
in the default module, so the shared `getDefaultModule()` limitation costs nothing here.

## 7. Compiler plugin

**None.** No `compiler-plugin/`, `*-compiler-plugin/`, or `ballerina-*-compiler-plugin/` directory
exists in the `v3.0.0` clone (`find -maxdepth 3 -iname '*compiler-plugin*'` → no results), and the
bala contains no `compiler-plugin/compiler-plugin.json`. `Ballerina.toml` declares no
`[[platform.java*.dependency]]` plugin entry and no `[package] export` beyond the default.
Nothing plugin-derived is therefore expected in, or missing from, the render.

## 8. Other considerations

- **Not deprecated.** Central `3.0.0`: `deprecated: null`, `deprecateMessage: ""`. Stable major
  version (3.0.0). `ballerinaVersion: 2201.12.2`; bala `distribution = 2201.12.0`. Pull count 45.
- **Pinned version match confirmed on both sides**: every version-qualified reference in `old` reads
  `ballerinax/openai.audio:3.0.0:`. No version drift.
- **Pre-existing library README defect, faithfully reproduced by both renders**: the quick-start
  sample uses `final images:Client openAIAudio = check new ({` — wrong module prefix (`images:`
  instead of `audio:`), and the preceding prose says `audio:ConnectionConfig`. This is verbatim from
  `bala/docs/README.md:48,53`, so it is a library documentation bug, not a render bug. It will
  mislead an LLM in both `old` and `new`.
- **Size / token cost.** 151,776 → 162,898 bytes (+7.3%); JSON 418,017 → 472,526 bytes (+13.0%).
  The extra ~11 KB buys the snake_case wire-name mapping for 281 fields and 10 validation
  constraints — a good trade for an OpenAI connector, where getting the JSON key names wrong is the
  single most likely failure mode.
- The library is an OpenAPI-generated connector: 237 types for one audio-focused service, most of
  which (assistants, threads, runs, vector stores, batches, fine-tuning) are unrelated to audio.
  That bloat is inherent to the library, identical on both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags <repo>` | tags `v2.0.0`, `v3.0.0`; exact match `v3.0.0` (`ae4b212`) |
| 2 | `git clone --depth 1 --branch v3.0.0` (2nd attempt; 1st timed out) | cloned to scratch `src/` |
| 3 | `ls -R <bala>` | one module `openai.audio`; `client.bal`, `types.bal`, `utils.bal`; `docs/README.md`; no `compiler-plugin/` |
| 4 | `wc -l <bala>/modules/openai.audio/*.bal` | 857 / 2692 / 304 = 3853 |
| 5 | `wc -l old new` | 2991 / 3286 |
| 6 | `grep -n '^// --- ' old new` | 4 markers each, same names |
| 7 | `grep -c '^// Unknown type:'` | old 6, new 0 |
| 8 | `grep -n '^// Unknown type:' old` | l.361, 489, 595, 1306, 1726, 2547 |
| 9 | `diff -u old new \| grep -c '^+[^+]' / '^-[^-]'` | +333 / −38 |
| 10 | `grep '^-' full.diff` (all 38) | 20 qualified refs, 6 unknown-type lines, 12 resource-fn signatures |
| 11 | `comm -23/-13` on sorted declaration sets | 0 removed; +6 types, 20 refs unqualified |
| 12 | `grep -c 'ballerinax/openai.audio:3.0.0:'` | old 20 lines / 51 occurrences; new 0 |
| 13 | `grep -o '@[a-zA-Z:]*' \| sort \| uniq -c` on new vs bala | identical histogram (301 each) |
| 14 | `diff` of `sort\|uniq -c` full annotation lines, new vs bala | no output — `ANNOTATION_MULTISETS_IDENTICAL` |
| 15 | awk pairing of `@jsondata:Name` → next decl, new vs bala | 281 pairs each; agree modulo `T?`↔`T\|()`, default→optional, `record {}`↔`record{\|anydata...;\|}`, union ordering |
| 16 | `grep -o '@…' old` | 8, all `@deprecated` |
| 17 | `grep -c '^\s*@' old / new` | 8 / 301 |
| 18 | `diff <(sed -n '7,98p' old) <(sed -n '7,98p' new)` | no output — README identical |
| 19 | `grep 'type <X>' <bala>/types.bal` for the 6 new types | l.127, 228, 269, 724, 1828, 2387 — all match render text and docs |
| 20 | `client.bal:150,392,819` vs render | source uses `*<X>Queries queries`; `Additional Values` absent from source |
| 21 | Python: client JSON, 69 fns each, same accessor+path keys | 12 differ; after stripping `Additional Values`, 0 residual diffs |
| 22 | Python: JSON key-path sets | only-new: `typeDefs[].baseType`, `typeDefs[].annotations[].*`, `typeDefs[].fields[].annotations[].*`; only-old: none |
| 23 | Python: `typeDefs` count / kind histogram | 237 both; Record 208, Union 23, Other 6 both; identical name sets |
| 24 | Python: the 6 `Other` typeDefs | old lacks `baseType`, new has it (`boolean`, `int[]`, `ChatCompletionMessageToolCall[]`, `int[]`, `anydata`, `anydata`) |
| 25 | bala public symbols vs new render symbols (`comm -23`) | 237 vs 238; 0 missing; extra is README's `main` |
| 26 | bala public symbols vs old render symbols | 6 missing (the 6 unknown types) |
| 27 | `grep -c '    resource function '` | 68 both |
| 28 | `grep -c 'record {\|'` bala vs renders | 32 vs 0 vs 0 |
| 29 | `grep -A1 '@deprecated'` old vs new | same 8 sites both sides |
| 30 | `types.bal:2331,2335,248` vs render defaults | source `'limit = 20`, `'order = "desc"`, `filter?`; render `limit = 0`, `order = "asc"`, `filter = "in_progress"` (both sides) |
| 31 | `types.bal:318` vs render l.749 / old l.683 | `decimal speed = 1.0;` → `decimal speed?;` on both sides |
| 32 | `grep -n '^import' old new` vs bala imports | render has only `import ballerinax/openai.audio;`; bala needs jsondata/constraint/http |
| 33 | awk count of unprefixed doc-continuation lines | old 18, new 20 |
| 34 | `LC_ALL=C grep -c '[^\x00-\x7F]'` | 1 line each (en dash, `best_of` doc) |
| 35 | `find src -iname '*compiler-plugin*' -maxdepth 3` | no results |
| 36 | `cat src/ballerina/Ballerina.toml` | version 3.0.0, distribution 2201.12.0, no plugin deps |
| 37 | Central API `/packages/ballerinax/openai.audio/3.0.0` | not deprecated; 1 module; ballerinaVersion 2201.12.2 |
| 38 | `grep 'images:Client' <bala>/docs/README.md` | l.53 — defect originates in the library README |

## 10. Caveats and unverified items

- The first `git clone` attempt failed with a connection timeout to github.com; the retry succeeded
  against the exact tag `v3.0.0`. No fallback to a default branch was needed.
- Annotation correctness was verified by set/multiset equality and by annotation→declaration pairing
  (checks 14–15), plus 7 hand-checked sites with source line numbers. I did not hand-verify all 281
  `@jsondata:Name` sites individually; the pairing check covers them mechanically, and its residual
  differences were all attributable to the four documented cosmetic normalisations. I did not prove
  those normalisations are exhaustive beyond the 54 residual lines inspected.
- Neither render was fed to `bal build`, so "non-compiling" claims in §5 (items 3, 4, 5) are based on
  reading the syntax, not on a compiler run. The specific defects (bare prose inside a record body,
  a required parameter after defaulted ones, missing imports) are unambiguous, but no compiler
  confirmed them.
- Union member ordering differs between render and source in a handful of places
  (e.g. `int|"auto"` vs `"auto"|int`); I treated this as semantically irrelevant and confirmed it is
  identical in `old` and `new`, so it is not a regression either way.
- I did not inspect `utils.bal` (304 lines) in detail; it contains no `public` declarations that the
  symbol extraction (check 25) picked up, so it contributes nothing to the render's expected surface.

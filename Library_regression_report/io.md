# ballerina/io 1.8.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/io` |
| Pinned version | `1.8.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-io |
| Tag reviewed | `v1.8.1` (commit `999ca58ee51d1832433ca3dbb49e06bc5d35ba9e`, grafted shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/io/1.8.1/java21` (central cache) |
| Old render | `356` lines |
| New render | `879` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. The only content `old` had that `new` does
not is 24 `// Unknown type: <Name>` placeholder lines and one version-qualified type reference
(`ballerina/io:1.8.1:PrintableRawTemplate`), both of which `new` replaces with real definitions.
Zero declarations were dropped, mangled, or truncated.

Concretely, spec v2 materialises 15 classes (`ReadableByteChannel`, `WritableByteChannel`, the
character/record/CSV/data channels, the three stream classes, `StringReader`, `CsvIterator`) with
all 81 of their methods, plus the 8 `distinct Error` types and the `Block` type — i.e. the entire
channel-oriented half of `ballerina/io`, which `old` emitted as bare placeholder comments. Every
class and every method name in `new` matches the bala source 1:1.

The residual problems in `new` are all inherited extractor/renderer limitations that simply become
visible now that the class bodies are rendered at all (flattened `distinct` error hierarchy,
`typedesc<>` erasure, dropped per-parameter doc lines). None of them is a regression against `old`,
which showed nothing at all for these symbols.

## 2. Change inventory

Line counts (`wc -l`): old `356`, new `879`, net `+523`.
Unified diff (`diff -u | grep '^+' | grep -v '^+++' | wc -l` / same for `-`): `+548 / -25`, 4 hunks.

### Removed from `new` (25 lines, the complete list)

| Kind | Count | Detail |
|---|---|---|
| `// Unknown type:` placeholders | 24 | 15 object/class types + 8 `Error` types + 1 `Other` type (`Block`) |
| Version-qualified union member | 1 | `type Printable any\|error\|ballerina/io:1.8.1:PrintableRawTemplate;` → `type Printable any\|error\|PrintableRawTemplate;` (old:222 → new:530) |

`grep -c '^// Unknown type:'` → old `24`, new `0`.
No declaration is present in `old` and absent from `new`
(`comm -23` of the sorted top-level declaration sets returned empty).

### Added in `new` (top-level declarations: 39 → 63, +24)

| Kind | Count | Names |
|---|---|---|
| `class` | 15 | `BlockStream`, `CSVStream`, `CsvIterator`, `LineStream`, `ReadableByteChannel`, `ReadableCSVChannel`, `ReadableCharacterChannel`, `ReadableDataChannel`, `ReadableTextRecordChannel`, `StringReader`, `WritableByteChannel`, `WritableCSVChannel`, `WritableCharacterChannel`, `WritableDataChannel`, `WritableTextRecordChannel` |
| `type` (error) | 8 | `Error`, `ConnectionTimedOutError`, `GenericError`, `AccessDeniedError`, `FileNotFoundError`, `TypeMismatchError`, `EofError`, `ConfigurationError` |
| `type` (other) | 1 | `Block` |

Class members added: **81** methods (`grep -cE '^    function '` on new = 81; 0 in old).
Of these, 13 are `init` constructors, 68 are normal methods.

### Unchanged

- README section byte-identical (`sed -n '7,66p' | md5` → `ab3d7c76bb61ad49036f1b0477d1fba6` on both).
- Functions section byte-identical (`diff <(sed -n '250,356p' old) <(sed -n '773,879p' new)` → no output).
- Section markers: 4 in both (`// --- README ---`, `// --- END README ---`, `// --- Types ---`, `// --- Functions ---`).
- JSON top-level counts identical: `typeDefs` 53, `clients` 0, `functions` 10, `services` 0, `annotations` 0, `readme` 2112 chars — on both sides.

### JSON-level cause

`typeDefs` kind histogram: old `{Constant:19, Union:5, Error:8, Enum:2, Record:2, Class:1, Other:1, <no type field>:15}`;
new `{Constant:19, Union:5, Error:8, Enum:2, Record:2, Class:16, Other:1}`.
The old JSON already carried the full member data for the 15 untagged object types (e.g. the
`BlockStream` entry is 1703 bytes in old, 1702 in new) — it just lacked the `"type": "Class"` tag,
so `renderTypeDef` fell through to `// Unknown type:`. Spec v2 also adds a `baseType` field to
`Error` and `Other` typedefs, which is what lets `type Error error;` and
`type Block readonly & byte[];` be emitted.

## 3. Correctness against library source

Bala default module is the only module: `ls .../1.8.1/java21/modules/` → `io`. Central metadata
confirms a single module (`api.central.ballerina.io/2.0/registry/packages/ballerina/io/1.8.1`,
`modules: [{name: "io"}]`). No submodules, so no submodule-only API question arises.

**Class set — exhaustive.** `grep -rn "^public class" <bala>/modules/io/*.bal` returns exactly 15
classes; the new render contains exactly those 15. Two additional non-public classes in the bala
(`PrintableClassImpl`, `PrintableRawTemplateImpl`, `print.bal:95,113`) are correctly absent.

**Method set — exhaustive.** Extracted method names per class from the render and compared against
`grep -nE "^\s+public (isolated )?function" ` per bala file. Exact match for all 15 classes, e.g.:

| Class | Bala source | Render | Match |
|---|---|---|---|
| `ReadableByteChannel` | `readable_byte_channel.bal:26,38,48,59,70,80,91` → `init, read, readAll, blockStream, base64Encode, base64Decode, close` | new:129–177, same 7 | yes |
| `ReadableCharacterChannel` | `readable_character_channel.bal:28,43,52,61,71,81,93,103,114,125` → 10 methods | new:179–246, same 10 | yes |
| `ReadableCSVChannel` | `readable_csv_channel.bal:27,46,65,81,95,113,134,147` → 8 methods | new:276–331, same 8 | yes |
| `WritableDataChannel` | `writable_data_channel.bal:38,51,62,73,84,95,106,118,129,140` → 10 methods | new:705–771, same 10 | yes |
| `CsvIterator` | `types.bal:20` — `next`, `close` only, **no explicit `init`** | new:696–703, `next`, `close` | yes |

**Signature spot-checks (all confirmed correct):**
- `readable_character_channel.bal:93` `readProperty(string key, string defaultValue = "")` → render preserves the `= ""` default.
- `readable_csv_channel.bal:27` `init(ReadableCharacterChannel byteChannel, Separator fs = ",", int nHeaders = 0)` → render identical.
- `readable_csv_channel.bal:133` `@deprecated` on `getTable` → render emits `@deprecated` at new:321.
- `readable_data_channel.bal:25` / `writable_data_channel.bal:38` `ByteOrder bOrder = "BE"` → render identical.
- `readable_byte_channel.bal:48` `returns readonly & byte[]|Error` → render `byte[] & readonly|Error` — reordered but semantically identical (`&` binds tighter than `|`).
- `writable_character_channel.bal:81` `XmlDoctype? xmlDoctype = ()` → render `XmlDoctype|() xmlDoctype = ()` — equivalent.
- `block_stream.bal:39` `returns record {|Block value;|}|Error?` → render `record {|Block value;|}|Error|()` — equivalent, and the version qualifier `ballerina/io:1.8.1:Block` that old's JSON carried is gone.
- `io_error.bal:18–39` — all 8 error names and all 8 doc strings match verbatim.
- `types.bal` `public type Block readonly & byte[];` → render `type Block readonly & byte[];` (new:126).

**Type/const coverage — exhaustive.** All 49 public `type`/`class`/`enum`/`const` names extracted
from the bala `.bal` files appear in the new render (`comm -23` returned empty). The render has 4
extra const names (`OVERWRITE`, `APPEND`, `DOCUMENT_ENTITY`, `EXTERNAL_PARSED_ENTITY`) that are
enum members re-emitted as standalone consts — present identically in `old`.

No invented symbols were found: every class, method, type and const in `new` maps to a real
declaration in the bala.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff` of the two renders: the `<`-side is exactly 25 lines, enumerated in §2, all of which
  are placeholders or a version-qualified reference that `new` replaces with better content.
- Sorted top-level declaration sets compared with `comm`: nothing only-in-old.
- README block md5-identical; `// --- Functions ---` block byte-identical.
- JSON object-by-object comparison of all 53 `typeDefs` by name: names identical on both sides; 25
  entries differ, and every difference is an addition (`type`/`baseType` tags, de-qualified type
  names) except one — `CsvIterator` (see below).
- Per-class method sets compared old-JSON vs new-JSON: identical for 14 of 15 classes.

The single content deletion at JSON level: `CsvIterator` lost a synthesised
`"type": "Constructor"` entry named `init` (old JSON 839 bytes → new 609). This is **not** a
regression: `types.bal:20` defines `public class CsvIterator` with no explicit `init`, and the old
entry advertised a bogus return type `ballerina/io:CsvIterator`. It also never reached the old
render, which emitted `// Unknown type: CsvIterator`.

## 5. Issues in `new` (independent of `old`)

None of these are regressions — `old` rendered nothing for the affected symbols — but they are
inaccuracies a consumer of the `new` render would see.

1. **`distinct` error hierarchy is flattened.** `io_error.bal:21–39` declares
   `public type ConnectionTimedOutError distinct Error;` (and 6 more). The new JSON sets
   `baseType: "error"` for all 8, so the render emits `type ConnectionTimedOutError error;`
   (new:466–487). The relation "`FileNotFoundError` is a subtype of `io:Error`" is lost, and
   `io:Error` itself loses `distinct`. This matters for a foundational module: an LLM reading this
   cannot infer that `if e is io:FileNotFoundError` narrows an `io:Error`.
2. **Class-method parameter/return doc lines are dropped by the renderer.** The new JSON carries
   per-parameter and return descriptions for class methods (e.g. `BlockStream.init.parameters[0].description`
   = "The `io:ReadableByteChannel` that this block stream is referred to"), but the render emits
   0 `# + x - ...` lines inside classes vs 31 at top level
   (`awk '/^class /{inc=1} /^}$/{inc=0} inc && /^    # \+ /' | wc -l` → 0; `grep -c '^# + '` → 31).
   Roughly 200 parameter/return doc strings present in the JSON never reach the render.
3. **Unusable constructors advertised on the byte channels.** `readable_byte_channel.bal:26` and
   `writable_byte_channel.bal:25` declare `isolated function init()` — deliberately *not* public
   ("Adding default init function to prevent object getting initialized from the user code").
   The render shows `function init() returns ();` (new:130, new:334) with no visibility qualifier,
   inviting `new io:ReadableByteChannel()`, which does not compile from user code. Compounding
   this, the only legitimate factories (`openReadableFile`, `openWritableFile`,
   `createReadableChannel`) are excluded from the render entirely (§6), so the render presents no
   valid way to obtain either channel.
4. **`typedesc<>` erased on `getTable` / `toTable`.** `readable_csv_channel.bal:134,147` declare
   `getTable(typedesc<record {}> structType, ...) returns table<record {}>|Error`. The render
   (new:322, new:329) shows `getTable(record {|anydata...;|} structType, ...)`. A call written
   against that shape (`ch.getTable(someRecordValue)`) will not compile — the parameter takes a
   type descriptor, not a value. The doc example immediately above it (`getTable(Employee)`) is
   correct, so the render is internally inconsistent. The JSON is byte-identical on both sides, so
   this is an upstream extractor behaviour, not a spec-v2 change.
5. **`PrintableRawTemplate` rendered as an empty class.** `print.bal:34` declares
   `public type PrintableRawTemplate object { public string[] & readonly strings; public Printable[] insertions; };`
   The render emits `class PrintableRawTemplate {\n}` (new:523) — both public fields lost. Present
   identically in `old` (old:215).
6. **`fileReadCsv` renders a non-compiling default.** `file_csv_io.bal:28` is
   `fileReadCsv(string path, int skipHeaders = 0, typedesc<string[]|map<anydata>> returnType = <>)`.
   The render (new:804) emits
   `fileReadCsv(string path, int skipHeaders = 0, string[]|map<anydata> returnType = string[]|map<anydata>)`
   — the inferred-typedesc default `= <>` becomes a type name used as an expression. Identical in
   `old`.
7. **Enum members duplicated as standalone consts.** `const string OVERWRITE = "OVERWRITE";`,
   `APPEND`, `DOCUMENT_ENTITY`, `EXTERNAL_PARSED_ENTITY` appear as consts (new:102–108) *and* as
   members of `enum FileWriteOption` / `enum XmlEntityType` (new:487–500). No `OVERWRITE` const
   exists in the bala. Identical in `old`.

## 6. Coverage gaps vs. the library

No submodule gap: the package publishes one module (`io`), which is the default module.

**18 of the 28 public module-level functions are absent from BOTH renders.** Source count:
`grep -rhnE "^public (isolated )?function \w+" <bala>/modules/io/*.bal` → 28. Render count
(`grep -cE '^function '`) → 10, identical on both sides.

Missing: `createReadableChannel`, `fileReadBlocksAsStream`, `fileReadCsvAsStream`,
`fileReadLinesAsStream`, `fileReadXml`, `fileWriteBlocksFromStream`, `fileWriteCsvFromStream`,
`fileWriteLinesFromStream`, `fileWriteXml`, `fprint`, `fprintln`, `openReadableCsvFile`,
`openReadableFile`, `openWritableCsvFile`, `openWritableFile`, `print`, `println`, `readln`.

**This is deliberate, not a bug.** The pipeline applies a curated exclusion list at
`flow-model-generator-ls-extension/src/main/resources/copilot/exclusion.json`, whose `ballerina/io`
entry lists exactly these 18 function names (verified by parsing that file in the local
`ballerina-vscode` checkout). The exclusion is applied identically on both sides — both renders
contain the same 10 survivors, byte-for-byte.

Worth flagging to a reviewer: spec v2 now surfaces the full channel-class API (500+ lines) whose
only entry points — `openReadableFile`, `openWritableFile`, `openReadableCsvFile`,
`openWritableCsvFile`, `createReadableChannel` — are on that exclusion list. The exclusion list may
warrant re-examination now that the classes are visible, or the classes are dead weight in the
prompt. Also note `io:println` / `io:print` are excluded, so the render never shows Ballerina's
most-used stdlib function.

Other gaps (both sides): the two public fields of `PrintableRawTemplate` (§5.5).

## 7. Compiler plugin

`has_plugin: true`, confirmed: `<bala>/java21/compiler-plugin/compiler-plugin.json` →
`plugin_id: "io-compiler-plugin"`, `plugin_class: "io.ballerina.stdlib.io.compiler.IOCompilerPlugin"`,
jar `compiler-plugin/libs/io-compiler-plugin-1.8.1.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/stdlib/io/compiler/`, 7 classes):
- `IOCompilerPlugin` registers a single `CodeAnalyzer` (`IOCodeAnalyzer`).
- `IOPathInjectionAnalyzer` is the only analysis task. It is a **static-code-analysis rule only**,
  not a compilation diagnostic.
- `IORule` defines one rule: `AVOID_PATH_TRAVERSAL` — "I/O function calls should not be vulnerable
  to path injection attacks", kind `VULNERABILITY`.
- `Constants.IO_FUNCTIONS` lists the 17 file functions the rule watches (`fileReadBytes`,
  `fileWriteBytes`, `fileReadBlocksAsStream`, … `fileReadXml`).

The plugin contributes **no annotations, no code actions, no generated artifacts, and no new
types** — nothing that should appear in a Copilot render. Consistent with `annotations: []` in both
JSONs. Nothing plugin-implied is missing from the render.

One soft observation: the plugin exists specifically because the file-path functions are
path-injection-sensitive, and 10 of those 17 functions are in the render with no hint of that
concern. Neither side conveys it; not a spec-v2 issue.

## 8. Other considerations

- **Version stability**: both sides at `1.8.1`; the bala `Ballerina.toml` reads `version = "1.8.1"`,
  and the render text contains no other version string in `new` (the sole occurrence,
  `ballerina/io:1.8.1:PrintableRawTemplate`, was in `old` only). No drift.
- **Not deprecated**; Central `deprecateMessage` is empty. `pullCount` 60,920. Stable 1.x.
- **Size / token cost**: 356 → 879 lines, +147%. The bulk (523 net lines) is the channel API. Given
  §6, a large fraction of those lines describes API that cannot be reached through any function the
  render exposes, so the token increase buys less than the line count suggests.
- **Renderer conventions**: class methods are emitted without `public`/`isolated`; `Error?` is
  rendered as `Error|()`. Consistent with the top-level function rendering in both sides;
  not a fidelity loss for an LLM.
- **Cosmetic**: many class-method doc blocks end with a trailing `# ` line (empty doc comment),
  e.g. new:135, new:145. Harmless.
- **Foundational-type check** (per the batch addendum): `io:ReadableByteChannel` is now rendered
  with its complete method set and correct signatures — a clear win for downstream packages
  (`ballerina/ftp`, `ballerina/email`, `mime`) that traffic in it. `io:Error` is rendered but
  without `distinct`, and its 7 subtypes no longer show their parentage (§5.1) — the one place a
  cross-package consumer is still under-served.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git clone --depth 1 --branch v1.8.1 …/module-ballerina-io` | tag exists; HEAD `999ca58ee51d1832433ca3dbb49e06bc5d35ba9e`, `git describe --tags` → `v1.8.1` |
| 2 | `cat src/ballerina/Ballerina.toml` | `org=ballerina name=io version=1.8.1 distribution=2201.12.0` |
| 3 | `wc -l old/ballerina_io.bal.txt new/ballerina_io.bal.txt` | 356 / 879 |
| 4 | `diff -u old new \| grep '^+' \| grep -v '^+++' \| wc -l` | 548 |
| 5 | `diff -u old new \| grep '^-' \| grep -v '^---' \| wc -l` | 25 |
| 6 | `grep -c '^// Unknown type:' old new` | 24 / 0 |
| 7 | `diff old new \| grep '^<'` | 25 lines: 24 placeholders + the `Printable` version-qualified line |
| 8 | `comm -23` of sorted `^(function\|type\|class\|enum\|const\|annotation) NAME` sets | empty (nothing only in old) |
| 9 | `comm -13` of the same sets | 24 names: 15 classes, 9 types |
| 10 | `grep -n '^// --- ' old new` | 4 markers each, same text |
| 11 | `sed -n '7,66p' \| md5` on both | `ab3d7c76bb61ad49036f1b0477d1fba6` both — README identical |
| 12 | `diff <(sed -n '250,356p' old) <(sed -n '773,879p' new)` | no output — Functions section identical |
| 13 | JSON top-level lengths, both sides | typeDefs 53, clients 0, functions 10, services 0, annotations 0, readme 2112 |
| 14 | JSON `typeDefs` kind histogram | old has 15 untagged + 1 Class; new has 16 Class |
| 15 | Per-name JSON typeDef comparison (53 names) | names identical; 25 differ, 24 are pure additions; only `CsvIterator` shrinks (839→609 bytes) |
| 16 | `CsvIterator` JSON dump both sides | new drops a synthesised `init` Constructor with return `ballerina/io:CsvIterator` |
| 17 | `<bala>/modules/io/types.bal:20` | `public class CsvIterator` — no explicit `init`; new is correct |
| 18 | `ls <bala>/java21/modules/` | `io` only — no submodules |
| 19 | Central API `packages/ballerina/io/1.8.1` | `modules: [{name:"io"}]`, `deprecateMessage: ""`, `ballerinaVersion 2201.12.0`, `pullCount 60920` |
| 20 | `grep -rn "^public class" <bala>/modules/io/*.bal` | 15 classes; new render has exactly those 15 |
| 21 | Per-class method-name extraction, render vs bala | exact 1:1 match for all 15 classes |
| 22 | `grep -cE '^    function ' new` | 81 class methods (0 in old) |
| 23 | `<bala>/modules/io/io_error.bal:18–39` | 8 `distinct` error types; new renders all 8 as `type X error;` (new:463–487) |
| 24 | `<bala>/modules/io/readable_csv_channel.bal:133–134` | `@deprecated` + `getTable(typedesc<record {}> …)`; render new:321–322 keeps `@deprecated`, erases `typedesc<>` |
| 25 | `<bala>/modules/io/readable_byte_channel.bal:26`, `writable_byte_channel.bal:25` | `isolated function init()` (non-public); rendered as `function init() returns ();` new:130 / new:334 |
| 26 | `<bala>/modules/io/print.bal:34` | `PrintableRawTemplate` object with 2 public fields; rendered empty in both (old:215 / new:523) |
| 27 | `<bala>/modules/io/file_csv_io.bal:28` | `typedesc<…> returnType = <>` → render new:804 `string[]\|map<anydata> returnType = string[]\|map<anydata>` (both sides) |
| 28 | `grep -rhnE "^public (isolated )?function \w+" <bala>/modules/io/*.bal \| wc -l` | 28 |
| 29 | `grep -cE '^function ' new` (and old) | 10 both sides |
| 30 | Parsed `…/flow-model-generator-ls-extension/src/main/resources/copilot/exclusion.json` | `ballerina/io` entry lists exactly the 18 missing function names |
| 31 | Public type/class/enum/const names: bala vs new render, `comm -23` | empty — full coverage |
| 32 | Same, `comm -13` | 4 extras: `OVERWRITE`, `APPEND`, `DOCUMENT_ENTITY`, `EXTERNAL_PARSED_ENTITY` (enum members re-emitted as consts; also in old) |
| 33 | `cat <bala>/java21/compiler-plugin/compiler-plugin.json` | `io-compiler-plugin`, class `IOCompilerPlugin`, 1 jar |
| 34 | `compiler-plugin/src/main/java/**` (7 classes) | one static-analysis rule `AVOID_PATH_TRAVERSAL` (VULNERABILITY) over 17 file functions; no annotations/code actions |
| 35 | `awk` count of `# + ` doc lines inside classes vs `grep -c '^# + '` | 0 inside classes vs 31 at top level |

## 10. Caveats and unverified items

1. **Exclusion-list provenance.** The `exclusion.json` I read is from the local
   `/Users/admin/Desktop/Copilot-Changes/ballerina-vscode` checkout, which is on branch
   `add-service-index` @ `6e88ec675c` — **neither** of the two commits under review (`eb5d81b3`
   old, `412ba01e` new). I did not re-read that file at either reviewed commit. The inference that
   the same 18 exclusions applied to both renders is nevertheless solid: both JSONs contain the
   same 10 functions and the Functions section is byte-identical.
2. **Java extractor internals not re-read at the reviewed commits.** Statements about *why* the old
   JSON lacked `"type": "Class"` are inferred from the JSON payloads themselves (old carries full
   member data but no `type` tag), not from reading `TypeDefDataBuilder` at `eb5d81b3`.
3. **Not compiled.** I did not attempt to compile any of the render text as Ballerina. Claims that
   `getTable(record {|anydata...;|} …)` and the `fileReadCsv` default are non-compiling are read
   from the language spec and the source signatures, not from a `bal build`.
4. **Docs directory not diffed.** I did not compare `<bala>/java21/docs/` API-doc JSON against the
   renders; the bala `.bal` sources were treated as authoritative, per the brief.
5. **Method-body semantics unverified.** I checked signatures, defaults, qualifiers and doc text,
   not runtime behaviour.
6. **Shallow clone.** The upstream clone is `--depth 1` at `v1.8.1`; I could not inspect history to
   confirm that the tag content equals the published bala. Spot checks (class list, method lists,
   `io_error.bal`, `types.bal`, compiler-plugin sources) agreed between clone and bala in every case
   examined; no disagreement was found, so the "bala wins" tiebreak was never needed.

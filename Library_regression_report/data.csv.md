# ballerina/data.csv 0.10.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/data.csv` |
| Pinned version | `0.10.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-data.csv |
| Tag reviewed | `v0.10.0` (commit `a14f2ed8779f9ec33c6222a9f074c2d71c81601e`) |
| Bala inspected | `/private/tmp/claude-501/.../scratchpad/extrabala/data.csv/0.10.0` (fetched from Central) |
| Old render | `595` lines |
| New render | `601` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Four hunks, 9 lines removed / 15 added.
Three of them are pure fidelity wins: the `Error` type is now emitted as a real definition
(`type Error error;`) instead of `// Unknown type: Error`, eight version-qualified type references
(`ballerina/lang.string:0.0.0:Char`, `ballerina/data.csv:0.10.0:Error`, …) are now rendered as the
idiomatic `string:Char` / `int:Unsigned32` / `Error`, and a new `// --- Annotations ---` section
exposes `public annotation NameConfig Name on record field;`, which `old` omitted entirely
(`annotations: []` in `old` JSON, one entry in `new` JSON).

Nothing was dropped. README, description, all 25 `typeDefs`, and all 6 functions are byte-identical
between the two JSONs except for the three improved entries. No regression found.

Several render inaccuracies remain in `new`, but every one of them is also present in `old` — they
are renderer-wide behaviours (record defaults dropped, closed records opened, `typedesc<…> t = <>`
mangled), not regressions.

## 2. Change inventory

Counts from `diff old new`: 9 removed lines, 15 added lines, 4 hunks.

| Kind | old | new | Δ |
|---|---|---|---|
| `typeDefs` (JSON) | 25 | 25 | 0 |
| `functions` (JSON) | 6 | 6 | 0 |
| `annotations` (JSON) | 0 | 1 | **+1** |
| `clients` / `services` (JSON) | 0 / 0 | 0 / 0 | 0 |
| `// Unknown type:` lines | 1 | 0 | **−1** |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 8 | 0 | **−8** |
| `// --- section ---` markers | 4 | 5 | +1 (`Annotations`) |

**Declarations added in `new` (2):**

- `type Error error;` + its doc `# Represents an error.` — replaces `// Unknown type: Error`
  (old L331 → new L331–332).
- `public annotation NameConfig Name on record field;` + doc, under a new `// --- Annotations ---`
  section (new L598–601).

**Declarations removed in `new`: 0.** Verified by comparing the declaration sets extracted with
`grep -nE '^(public )?(isolated )?(function|type|class|enum|const|annotation|listener|service)'`
from both files, and by comparing `typeDefs`/`functions` name lists in the two JSONs
(`names equal: True`).

**Declarations modified (3 typeDefs + 1 function), all de-qualification:**

| Symbol | old | new |
|---|---|---|
| `ParseOptions.delimiter` / `.textEnclosure` / `.escapeChar` / `.comment` | `ballerina/lang.string:0.0.0:Char` | `string:Char` |
| `ParseOptions.nilValue` | `ballerina/data.csv:0.10.0:NilValue?` | `NilValue?` |
| `ParseOptions.header` | `ballerina/lang.int:0.0.0:Unsigned32?` | `int:Unsigned32?` |
| `ParseListOptions.headerRows` | `ballerina/lang.int:0.0.0:Unsigned32` | `int:Unsigned32` |
| `parseToStream` return | `stream<t, ballerina/data.csv:0.10.0:Error?>|Error` | `stream<t, Error?>|Error` |
| `Error` typeDef (JSON) | `{"type":"Error"}` | `{"type":"Error","baseType":"error"}` |

README block (render L8–291) is identical to `docs/README.md` in the bala apart from one trailing
blank line, and identical between `old` and `new` (`diff` of L1–292 is empty).

## 3. Correctness against library source

The bala's `modules/data.csv/*.bal` are byte-identical to `ballerina/*.bal` at tag `v0.10.0`
(verified per file), so GitHub and the bala agree.

Everything `new` adds or changes checks out:

- `type Error error;` — `modules/data.csv/types.bal:18` `public type Error error;`, doc
  `# Represents an error.` at L17. New render L331–332 matches (minus `public`, see §5).
- `annotation NameConfig Name on record field` — `types.bal:34–35`
  `# The annotation is used to overwrite the existing record field name.` /
  `public const annotation NameConfig Name on record field;`. New render L600–601 matches except
  the `const` qualifier (§5).
- `string:Char` for `delimiter`, `textEnclosure`, `escapeChar`, `comment` — `types.bal:123,129,131,137`.
- `int:Unsigned32? header` — `types.bal:139`; `int:Unsigned32 headerRows` — `types.bal:149`.
- `NilValue? nilValue` — `types.bal:135`.
- `parseToStream(...) returns stream<t, Error?>|Error` — `csv_api.bal:130–132`.

All 6 functions match `csv_api.bal` by name, parameter names/order, and doc text:
`parseString` (L35), `parseBytes` (L53), `parseStream` (L76), `transform` (L93), `parseList` (L110),
`parseToStream` (L130). Their `t` parameter is the one systematically mis-rendered (§5.6).

All 14 public types are present in `new` with correct field names and doc text:
`Error`, `NameConfig`, `Options`, `FailSafeOptions`, `FileOutputMode`, `ErrorLogContentType`,
`LogOutput`, `Location`, `FileWriteOption`, `ParseOptions`, `ParseListOptions`, `TransformOptions`,
`LineTerminator`, `NilValue` — cross-checked field-by-field against `types.bal:18–182`.
The 11 remaining `typeDefs` are the enum members surfaced as `const string` (METADATA, RAW,
RAW_AND_METADATA, APPEND, OVERWRITE, LF, CRLF, NULL, NOT_APPLICABLE, EMPTY_STRING, NIL), which
correctly carry the enum member values and docs.

`*Options` inclusion is flattened correctly (field-wise) into `ParseOptions`, `ParseListOptions`
and `TransformOptions` — the 5 `Options` fields appear at the end of each (new L444–448, L475–479,
L488–492) — though without the inherited docs (§5.7).

## 4. Regressions

**None found.**

What was checked to conclude that:

- `diff old new` — all 4 hunks reviewed line by line; the 9 removed lines are 1 `// Unknown type:`
  placeholder and 8 version-qualified type lines, each replaced by a superset of information.
- JSON structural comparison: identical key sets; identical `typeDefs` name list; identical
  `functions` list except the `parseToStream` return type; `readme` and `description` compare equal;
  `annotations` went 0 → 1 (gain only).
- README section (L1–292) diffs empty.
- No declaration present in `old` is absent from `new` (declaration-set comparison, §2).
- No parameter, default, return type, or doc line is present in `old` and missing in `new`.
- `grep -c 'ballerina[x]*/[a-z.]*:[0-9]'` → 8 in `old`, 0 in `new`; each of the 8 was verified to be
  replaced, not deleted.

## 5. Issues in `new` (independent of `old`)

All seven below are also present in `old` — they are renderer behaviours, not regressions — but
they are inaccuracies an LLM consuming the render would inherit.

1. **`const` dropped from the annotation.** Source `types.bal:35` is
   `public const annotation NameConfig Name on record field;`; render L601 emits
   `public annotation NameConfig Name on record field;`. The JSON has no field carrying the `const`
   qualifier, so this is lost at extraction. Consequence: the render implies the annotation cannot
   be used in a const-annotation context.
2. **Record field defaults are dropped and required fields are marked optional.** Every
   defaulted field in the JSON has `optional: true` and no `defaultValue`. E.g. `ParseOptions.delimiter`
   is `string:Char delimiter = ","` in source (`types.bal:123`) but renders as `string:Char delimiter?`;
   likewise `encoding = "UTF-8"`, `locale = "en_US"`, `textEnclosure = "\""`, `escapeChar = "\\"`,
   `comment = "#"`, `header = 0`, `Options.enableConstraintValidation = true`,
   `FailSafeOptions.enableConsoleLogs = true`, `FileOutputMode.contentType = METADATA`,
   `FileOutputMode.fileWriteOption = APPEND`, `ParseListOptions.headerRows = 0`. An LLM reading the
   render cannot know the defaults and will believe every option field is optional-absent rather
   than defaulted.
3. **Closed records are rendered as open.** `NameConfig`, `FailSafeOptions`, `FileOutputMode`,
   `LogOutput`, `Location`, `ParseOptions`, `ParseListOptions`, `TransformOptions` are all
   `record {| … |}` in source; all render as `record { … }`. Generated code that adds extra fields
   would not compile.
4. **`lineTerminator` union is mangled into physical newlines.** Source
   `LineTerminator|LineTerminator[] lineTerminator` (`types.bal:133`) renders as
   `"\n"|"\r\n"|LineTerminator[]` with the escape sequences expanded to real newline characters,
   so new render L433–435 is three broken physical lines. The same expansion breaks
   `const string LF` (L312–313) and `const string CRLF` (L316–317). Non-compiling as printed.
5. **Enum member values and member docs are dropped, and member order is reversed.**
   `enum LineTerminator { CRLF, LF }` (L452–455) loses `LF = "\n"` / `CRLF = "\r\n"`
   (`types.bal:167,169`); same for `NilValue`, `ErrorLogContentType`, `FileWriteOption`. The member
   docs exist in the JSON (`members[].description`) but the renderer does not print them. Order is
   reversed vs. source in all four enums (e.g. source `METADATA, RAW, RAW_AND_METADATA` → render
   `RAW_AND_METADATA, RAW, METADATA`). The values are recoverable from the `const string` block
   above, but not the association.
6. **Inferred `typedesc` parameters render as non-compiling Ballerina.** Source
   `typedesc<record {}[]|anydata[][]> t = <>` renders as
   `record {|anydata...;|}[]|anydata[][] t = record {|anydata...;|}[]|anydata[][]` — a type
   expression used as a value default. Affects all 6 functions (L513, 529, 548, 563, 578, 596).
   It also widens `record {}` to `record {|anydata...;|}`, and the same widening hits
   `transform(record {}[] csvRecords)` → `record {|anydata...;|}[] csvRecords`.
7. **`public` and `isolated` qualifiers dropped on functions and types; inherited-field docs lost.**
   All 6 functions are `public isolated function` in source but render as bare `function`. The 5
   fields inherited from `*Options` into `ParseOptions`/`ParseListOptions`/`TransformOptions` render
   without their doc comments (new L444–448, L475–479, L488–492), unlike the same fields in the
   `Options` definition itself.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** The bala exports exactly one module (`package.json` → `"export": ["data.csv"]`,
Central metadata lists one module), so there is no submodule-only API and the
`pkg.getDefaultModule()` limitation is a non-issue here.

Public symbols in the default module (`grep 'public' modules/data.csv/*.bal`): 6 functions,
14 types/enums, 1 annotation = 21. All 21 appear in `new`.
`csv_stream.bal`, `init.bal`, `utils.bal` declare nothing public at module level (`class CsvRecordStream`,
`init()`, `setModule()`, `externNextCsvRecord()`, `externCloseCsvStream()`, `printError()` are all
module-private); their absence is correct.

`old` had 1 coverage gap that `new` closes: the `Name` annotation (`old` JSON `annotations: []`).

## 7. Compiler plugin

`has_plugin: true` — confirmed: `compiler-plugin/compiler-plugin.json` in the bala declares
`plugin_class: io.ballerina.lib.data.csvdata.compiler.CsvDataCompilerPlugin`, backed by
`compiler-plugin/libs/data.csv-compiler-plugin-0.10.0.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/lib/data/csvdata/compiler/`, 834 lines):
`CsvDataCompilerPlugin` registers `CsvDataCodeAnalyzer`, which adds a single
`SyntaxNodeAnalysisTask` (`CsvDataTypeValidator`, 640 lines) over `MODULE_PART`. It is
**validation only** — no code actions, no code generation, no modifier tasks, so it contributes
nothing that could appear as API in the render.

It emits 7 diagnostics (`CsvDataDiagnosticCodes`, all severity `ERROR`): `CSV_ERROR_1` duplicate
field, `CSV_ERROR_2` unsupported type, `CSV_ERROR_3` unsupported field type, `CSV_ERROR_4`
unsupported tuple member type, `CSV_ERROR_5` `outputWithHeaders`/`headerOrder` not allowed for
record-array expected types, `CSV_ERROR_6` `customHeadersIfHeadersAbsent` not allowed when header is
present, `CSV_ERROR_7` `customHeaders` required when `headerRows > 1`.

**Gap worth noting (shared, not a regression):** these constraints are compile-time rules an LLM
would benefit from, and none of them are visible in either render — e.g. the render shows
`outputWithHeaders`, `headerOrder`, `header`, `customHeaders`, `customHeadersIfHeadersAbsent` and
`headerRows` as freely combinable optional fields, while the plugin rejects several combinations.
The plugin also only validates a fixed set of call names (`Constants.java:27–32`:
`parseString`, `parseBytes`, `parseStream`, `transform`, `parseList`) — `parseToStream` is **not**
in that list, so the newer streaming API is not validated by the plugin at all. Neither render
conveys any of this; it is outside what `toSyntaxString` models.

## 8. Other considerations

- **Pre-1.0 module** (`0.10.0`). API is not covered by stdlib backward-compatibility guarantees;
  `parseToStream` and the `FailSafeOptions`/`FileOutputMode`/`LogOutput`/`Location`/`ErrorLogContentType`/
  `FileWriteOption` group are recent additions.
- **Not deprecated.** Central metadata for `ballerina/data.csv/0.10.0` returns no deprecation flag;
  `ballerinaVersion: 2201.12.0`, `graalvmCompatible: true`, single module `data.csv`.
- **Size**: 601 lines / 41,207 bytes of JSON — trivial token cost. 284 of the 601 render lines
  (47%) are the README, which is high-quality and example-heavy (9 runnable snippets). Doc coverage
  of the API itself is complete: every function and every record field carries its source doc.
- **Doc-comment artefact**: multi-line record-field docs lose their `# ` continuation prefix, so
  continuation lines are emitted flush-left inside the record body (e.g. new L347–349, L358,
  L469, L472–473, L486). Present in `old` too. Makes the render non-compiling as printed and can
  blur the doc/field boundary.
- The `Error` type is depended on by other packages that wrap `csv:Error`; `new` now renders it
  correctly as `type Error error;` where `old` gave an LLM nothing but a placeholder comment. This
  is the single most valuable change here.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git clone --depth 1 --branch v0.10.0 …/module-ballerina-data.csv` | OK, commit `a14f2ed8` tagged `v0.10.0` |
| 2 | `wc -l data.csv/{old,new}/ballerina_data.csv.bal.txt` | 595 / 601 |
| 3 | `wc -c` on both JSONs | 40,996 / 41,207 |
| 4 | `diff old new \| grep -c '^<'` / `'^>'` | 9 removed / 15 added |
| 5 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 6 | `grep -c 'ballerina[x]*/[a-z.]*:[0-9]'` | old 8, new 0 |
| 7 | `grep -n '^// --- '` | old 4 markers, new 5 (`Annotations` added) |
| 8 | `diff` of render L1–292 (README) old vs new | identical |
| 9 | `diff` render L8–291 vs bala `docs/README.md` | identical but one trailing blank line |
| 10 | Python JSON compare: key sets, `typeDefs` name list | identical; 25 both sides |
| 11 | Python JSON compare: per-typeDef equality | only `Error`, `ParseOptions`, `ParseListOptions` differ (all improvements) |
| 12 | Python JSON compare: per-function equality | only `parseToStream` differs (return de-qualified) |
| 13 | `new` JSON `annotations` | 1 entry: `Name`, `RECORD_FIELD`, typeConstraint `NameConfig`; `old` has 0 |
| 14 | `readme`/`description` JSON equality old vs new | `True` / `True` |
| 15 | `diff` bala `modules/data.csv/*.bal` vs repo `ballerina/*.bal` (5 files) | all IDENTICAL |
| 16 | `grep 'public' modules/data.csv/*.bal` | 21 public symbols, all in `csv_api.bal` + `types.bal` |
| 17 | `grep -c public` on `csv_stream.bal` / `init.bal` / `utils.bal` | 3 (methods of private class) / 0 / 0 |
| 18 | `types.bal:18` | `public type Error error;` — matches new L332 |
| 19 | `types.bal:34–35` | `public const annotation NameConfig Name on record field;` — `const` missing in render |
| 20 | `types.bal:120–142` (`ParseOptions`) | 10 own fields + `*Options`; all 15 rendered; all defaults dropped |
| 21 | `csv_api.bal:35,53,76,93,110,130` | 6 public isolated functions; names/params/docs match render |
| 22 | `new` JSON `ParseOptions.fields[*].defaultValue` | `None` for all 15 |
| 23 | `new` JSON `LineTerminator.members` | `CRLF`, `LF` with docs; values absent, docs not rendered |
| 24 | `compiler-plugin/compiler-plugin.json` (bala) | `CsvDataCompilerPlugin`, jar `data.csv-compiler-plugin-0.10.0.jar` |
| 25 | `CsvDataCodeAnalyzer.java:33–37` | registers `CsvDataTypeValidator` on `MODULE_PART` only |
| 26 | `CsvDataDiagnosticCodes.java:31–45` | 7 ERROR diagnostics, `CSV_ERROR_1`–`CSV_ERROR_7` |
| 27 | `compiler/Constants.java:27–32` | validated calls exclude `parseToStream` |
| 28 | `package.json` (bala) | `export: ["data.csv"]`, single module, `graalvmCompatible: true` |
| 29 | Central API `ballerina/data.csv/0.10.0` | one module, `ballerinaVersion 2201.12.0`, no deprecation |

## 10. Caveats and unverified items

- The compiler-plugin jar in the bala was not decompiled; plugin behaviour is asserted from the
  `v0.10.0` GitHub source, which matches the bala's `.bal` sources byte-for-byte. The plugin jar
  itself is therefore assumed — but not proven — to be built from that same source.
- The claim that the render is "non-compiling as printed" (§5.4, §5.6, §8) is by inspection of the
  syntax; I did not run `bal build` over the rendered text.
- `old`/`new` were not regenerated; the audit uses the committed renders and JSONs in the repo as
  given. The brief's `PIN_OK` claim for both sides was taken as given and is consistent with both
  JSONs describing identical symbol sets.

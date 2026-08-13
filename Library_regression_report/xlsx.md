# ballerina/xlsx 1.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/xlsx` |
| Pinned version | `1.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-xlsx |
| Tag reviewed | `v1.0.1` (clone HEAD `a2fda2b`, "[Gradle Release Plugin] - pre tag commit: 'v1.0.1'") |
| Bala inspected | `/private/tmp/claude-501/-Users-admin-Desktop-Copilot-Changes-Check-contents-test-bal-copilot-library-get-mds/19909936-2e4b-46de-9886-3075396fe81e/scratchpad/extrabala/xlsx/1.0.1` (fetched from Central) |
| Old render | `638` lines |
| New render | `891` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive for this library. The diff is 5 hunks, 269 lines added and 16 removed;
of the 16 removed lines, 14 are content and every one of them is replaced by a strictly more
informative rendering (12 `// Unknown type:` placeholders → real definitions, 2
version-qualified type aliases → clean type refs). No declaration is lost.

`new` closes the entire coverage gap of `old`: the 11 error types and the `Workbook` class become
real definitions, and the `Sheet` (21), `Table` (18) and `Workbook` (13) method bodies — all empty
or absent in `old` — are rendered in full and match the library source method-for-method. The
`@xlsx:Name` annotation, absent from the `old` JSON entirely (`annotations: []`), is now extracted
and rendered.

Remaining inaccuracies in `new` (§5) are renderer/extractor fidelity issues, most of which `old`
already exhibits in its Functions section; they do not constitute a regression.

## 2. Change inventory

Mechanical (verified with `diff -u`, not copied from the precomputed diff):

| metric | value |
|---|---|
| Old lines / New lines | 638 / 891 |
| Hunks | 5 |
| Lines added (incl. blank) | 269 |
| Lines removed (incl. blank) | 16 (14 non-blank) |
| `// Unknown type:` lines | old 12 → new 0 |
| Version-qualified type refs (`org/mod:ver:Type`) | old 2 lines (4 refs) → new 0 |
| `// --- section ---` markers | old 4 → new 5 (`// --- Annotations ---` added) |
| README block (lines 1–210) | byte-identical (`readme` field identical in both JSONs) |

Top-level declaration counts (`grep -oE '^(public )?(function|type|class|enum|const|annotation)'`):

| kind | old | new |
|---|---|---|
| `type` | 24 | 35 |
| `class` | 2 | 3 |
| `enum` | 5 | 5 |
| `const` | 9 | 9 |
| `function` | 6 | 6 |
| `annotation` | 0 | 1 |
| **total** | **46** | **59** |

Added in `new` (13 top-level):

- 11 error types: `Error`, `ParseError`, `FileNotFoundError`, `SheetNotFoundError`,
  `SheetExistsError`, `TypeConversionError`, `ConstraintValidationError`, `TableNotFoundError`,
  `TableExistsError`, `TableOverlapError`, `InvalidTableRangeError`
  (each was `// Unknown type: X` in `old`)
- `class Workbook { … }` (was `// Unknown type: Workbook`)
- `public annotation NameConfig Name on record field;`

Added members (52 method signatures, none present in `old`):

| container | methods in `new` | methods in bala source | match |
|---|---|---|---|
| `class Sheet` | 21 | 21 (`sheet.bal`, `public type Sheet isolated object`) | exact, same names, same order |
| `class Table` | 18 | 18 (`table.bal`, `public type Table isolated object`) | exact, same names, same order |
| `class Workbook` | 13 | 13 (`workbook.bal`, incl. `init`) | exact, same names, same order |

Modified (2 lines):

```
- type CellValue string|int|float|decimal|boolean|ballerina/time:2.8.1:Date|ballerina/time:2.8.1:Civil|ballerina/time:2.8.1:TimeOfDay|();
+ type CellValue string|int|float|decimal|boolean|time:Date|time:Civil|time:TimeOfDay|();
- type Row map<ballerina/xlsx:1.0.1:CellValue>|string[];
+ type Row map<CellValue>|string[];
```

Both new forms are exactly the source spelling (`types.bal:185`, `types.bal:182`).

Removed: **none** (0 declarations). The 14 removed content lines are the 12 placeholders and the
2 superseded type lines above.

JSON-level cause (from the two `*.json` files):
- `typeDefs` count is 49 on both sides; the *content* differs. In `old`, the 11 error typeDefs have
  no `baseType` key and `Workbook` has no `type` key at all (`{'name','description','functions'}`),
  so `renderTypeDef` degraded them. In `new` every typeDef is tagged
  (`Record 19, Error 11, Constant 9, Enum 5, Class 3, Union 2`) and errors carry `baseType`.
- `old` `Sheet`/`Table` typeDefs have keys `{'name','description','type'}` — no `functions` array,
  hence the empty `class Sheet {}` / `class Table {}` bodies. `new` adds `functions` with 21 / 18
  entries. `old` `Workbook` *did* already carry 13 `functions`, but lacked `type`, so the renderer
  discarded all of them.
- `old.annotations == []`; `new.annotations` has 1 entry (`Name`, `RECORD_FIELD`, typeConstraint
  `NameConfig`).

## 3. Correctness against library source

The bala `modules/xlsx/*.bal` and the `v1.0.1` clone `ballerina/*.bal` are byte-identical
(`diff -q` over all 8 files: no output), so source citations below apply to both.

Verified correct in `new`:

- 11 error types exist with these exact names and doc strings — `errors.bal:18–48`.
- `ErrorDetails` fields (`sheetName?`, `tableName?`, `cellAddress?`, `rowNumber?`, `columnNumber?`,
  `fieldName?`) — `errors.bal:51–64`. Rendered identically (modulo open/closed record, §5).
- `Sheet` 21 methods, names and order identical to `sheet.bal:26–190`. Signatures spot-checked:
  - `getUsedCellRange() returns CellRange|()|Error` ≡ `CellRange?|Error` (`sheet.bal:36`)
  - `createTable(string name, CellRange|string range, string[]|() headers = ())` ≡
    `string[]? headers = ()` (`sheet.bal:169`)
  - `createTableFromData(string name, Row[] data, int startRowIndex = 0, int startColumnIndex = 0)`
    ≡ `sheet.bal:182–184` exactly
  - `setColumn`, `setCell`, `setCellByAddress`, `deleteRow`, `rename`, `getTable`, `getTables`,
    `deleteTable` — all match `sheet.bal:115–190`
- `Table` 18 methods identical to `table.bal:35–144`; `resize(CellRange|string newRange)`
  (`table.bal:135`), `hasTotalRow() returns boolean|Error` (`table.bal:114`) verified.
- `Workbook` 13 methods identical to `workbook.bal:34–163`, including `init()`
  (`public isolated function init()`, `workbook.bal:34`). The private members
  (`initNew`, `getSheetByName`, `getSheetByIndex`, `deleteSheetByNameNative`,
  `deleteSheetByIndexNative`, `saveToPathNative`) are correctly **not** rendered.
- Annotation: `public const annotation NameConfig Name on record field;` — `types.bal:58`.
  Attachment point `record field` correct.
- `CellValue` / `Row` unions match `types.bal:182–185` exactly.
- Module-level private functions `init()` (`init.bal:19`) and `printFailSafeWarning`
  (`print_utils.bal:29`) are correctly absent from both renders.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new` produces exactly 5 hunks; every `-` line was enumerated (14 content lines,
  listed in §2) and each has a strictly richer `+` replacement in the same position.
- Declaration-name set diff (`diff` of `grep -E '^(public )?(function|type|class|enum|const|annotation)'`
  over both files) shows **only additions and the 2 type-ref improvements** — 0 removals.
- Public-symbol coverage script: symbols exported by the bala default module and missing from the
  render — `old`: 12 missing; `new`: 0 missing.
- Sections: `new` retains all 4 of `old`'s markers and adds `// --- Annotations ---`.
- README/description: `n["readme"] == o["readme"]` → `True`; `n["description"] == o["description"]`
  → `True`. No doc content lost.
- Functions section (6 top-level functions): byte-identical between the two renders — no parameter,
  default, return type or doc changed there.

## 5. Issues in `new` (independent of `old`)

None of these is a regression; items 5–9 are present in `old` too (in its Functions/Types
sections), items 1–4 are visible only in `new` because the corresponding constructs were not
rendered at all in `old`.

1. **`distinct` and the error hierarchy are erased.** Source (`errors.bal:18–48`) declares
   `public type Error distinct error<ErrorDetails>;` and each subtype as
   `public type ParseError distinct Error;`. `new` renders all eleven as flat
   `type X error<ErrorDetails>;`. The JSON is the origin (`baseType: "error<ErrorDetails>"` for
   `ParseError` too). An LLM reading the render cannot tell that `ParseError`, `SheetNotFoundError`,
   … are subtypes of `xlsx:Error`, which is exactly what user code pattern-matches on
   (`if e is xlsx:SheetNotFoundError`). Still a large net improvement over `// Unknown type:`.
2. **Included-record parameters are flattened *and* duplicated, producing non-compiling
   signatures.** Source `sheet.bal:73` is `putRows(Row[] data, *WriteOptions options)`. `new`
   renders:
   `function putRows(Row[] data, boolean writeHeaders = true, int startRowIndex = 0, SheetWriteMode sheetWriteMode = APPEND, WriteOptions options) returns Error|();`
   — the record's fields are expanded as defaulted params *and* a trailing `options` param with no
   default follows defaulted params, which is invalid Ballerina. Same shape in `Sheet.setRow`
   (`*RowWriteOptions`, `sheet.bal:105`) and `Table.putRows` (`*TableWriteOptions`, `table.bal:109`).
   Identical behaviour already exists in `old`'s Functions section for `writeSheet` (old:588) and
   `writeTable` (old:622), so it is a pre-existing renderer trait, not new.
3. **Invented defaults for optional-without-default record fields.** `WriteOptions.startRowIndex`
   is `int startRowIndex?` with no default (`types.bal:145`) and its own doc says "Omitted, uses the
   mode's natural point: the end of the data for `APPEND`, row 0 otherwise" — yet `new` renders
   `int startRowIndex = 0`, contradicting the doc printed two lines above it. Same for
   `TableWriteOptions.insertAt` (`types.bal:177`) in `Table.putRows`. (`old` has the identical
   invention for `writeTable`'s `insertAt`.)
4. **`typedesc<>` dropped on dependently-typed params.** Source `typedesc<Row> t = <>` renders as
   `xlsx:Row t = <>`; `typedesc<CellValue> t = <>` as `xlsx:CellValue t = <>`;
   `typedesc<map<CellValue>> t = <>` as `map<xlsx:CellValue> t = <>` (`Table.getTotalRow`). The
   self-module `xlsx:` prefix is also inconsistent with every other type ref in the file, which is
   unqualified. `old` shows a different but equally wrong spelling for the same construct in
   top-level functions (`map<xlsx:CellValue>|string[] t = xlsx:Row`).
5. **Closed records rendered as open.** Every record in the library is `record {| … |}`
   (e.g. `ErrorDetails`, `types.bal:51`); both renders emit `record { … };`. An LLM would believe
   extra fields are allowed.
6. **Record field defaults dropped, required-with-default fields shown optional.** e.g.
   `CommonParseOptions.formulaMode = CACHED` and `caseInsensitiveHeaders = false`
   (`types.bal:61–66`) render as `FormulaMode formulaMode?; boolean caseInsensitiveHeaders?;`.
   Defaults survive only in the prose docs. Shared with `old`.
7. **Doc continuation lines lose the `# ` prefix**, emitting bare prose at column 0 inside type
   bodies — 6 occurrences in each render (new:538, 666, 678, 681, 689, 701; same 6 in `old`),
   e.g. `names columns \`col0\`, \`col1\`, and so on.` at new:538. This is non-compiling text.
8. **`Sheet` and `Table` are object *types*, not classes.** Source: `public type Sheet isolated
   object { … };` (`sheet.bal:21`), `public type Table isolated object { … };` (`table.bal:30`).
   Both renders label them `class`. Shared with `old` (which rendered empty class bodies).
9. **Qualifiers dropped**: `public const annotation` → `public annotation` (new:891 vs
   `types.bal:58`), and `public isolated` is stripped from every method and every top-level
   function on both sides. Minor, but `isolated` is API-visible in Ballerina.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** Script result: public top-level symbols in the bala default module that do
not appear in the render — `old`: 12 (`Error`, `ParseError`, `FileNotFoundError`,
`SheetNotFoundError`, `SheetExistsError`, `TypeConversionError`, `ConstraintValidationError`,
`TableNotFoundError`, `TableExistsError`, `TableOverlapError`, `InvalidTableRangeError`,
`Workbook`); `new`: 0.

Method-level: 21/21 `Sheet`, 18/18 `Table`, 13/13 `Workbook` public methods present in `new`;
0/21, 0/18, 0/13 in `old`.

Submodule API: none exists. `package.json` `export: ["xlsx"]`, the bala has a single
`modules/xlsx` directory, and Central reports exactly one module (`ballerina/xlsx`). The
`getDefaultModule()`-only extraction therefore loses nothing here.

## 7. Compiler plugin

`has_plugin: false` — confirmed. The bala root contains only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`, `platform/`; there is no `compiler-plugin/` directory and no
`compiler-plugin.json`. The upstream `settings.gradle` includes only `:xlsx-native`,
`:xlsx-ballerina` and `:checkstyle` — no compiler-plugin subproject. Nothing is contributed by a
plugin, so nothing plugin-implied can be missing from the render.

Note: `@xlsx:Name` is processed by the native runtime (`io.ballerina.lib.xlsx.*`), not by a
compiler plugin, and it *is* now rendered in `new`.

## 8. Other considerations

- **Version/deprecation**: Central reports `ballerina/xlsx` `1.0.1`, `ballerinaVersion 2201.12.0`,
  `pullCount 26`, no `deprecated` field in the response. This is a very new, low-adoption stdlib
  module (copyright headers read 2026).
- **Distribution skew**: the package targets `2201.12.0` while the render pipeline used
  distribution `2201.13.4`. No evidence of any effect on the output.
- **Size/token impact**: +253 lines (+39.7%) for `new`. Given that the added content is the entire
  object API surface of the library — previously invisible — the cost is well spent.
- **`Workbook` construction**: the README (rendered identically on both sides) documents
  `xlsx:Workbook wb1 = new;`. `new` now backs that with `class Workbook { function init() returns (); … }`,
  so the render is self-consistent for the first time; in `old` the README referenced a type the
  render declared "unknown".
- **Enum member order** differs from source in both renders (`enum FormulaMode { TEXT, CACHED }` vs
  source `CACHED, TEXT`), and enum members are additionally emitted as 9 standalone
  `const string X = "X";` declarations. Harmless but duplicative; identical on both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git clone --depth 1 --branch v1.0.1 …/module-ballerina-xlsx` | OK, HEAD `a2fda2b` "pre tag commit: 'v1.0.1'" |
| 2 | `wc -l old/new render` | 638 / 891 |
| 3 | `diff -u old new` → `grep -c '^+'/'^-'/'^@@'` | 269 added, 16 removed, 5 hunks |
| 4 | `grep '^-[^-]' diff` | 14 content lines: 12 `// Unknown type:`, `CellValue`, `Row` |
| 5 | `grep -c '^// Unknown type:'` | old 12, new 0 |
| 6 | `grep -n '^// --- '` | old: README/END README/Types/Functions; new: + `Annotations` |
| 7 | `grep -oE '^(public )?(function\|type\|class\|enum\|const\|annotation)' \| sort \| uniq -c` | old 46 decls, new 59 |
| 8 | `diff` of declaration-name lists | 13 additions, 2 modifications, **0 removals** |
| 9 | Python: parse `class X {` bodies in new render | Sheet 21, Table 18, Workbook 13 methods |
| 10 | Python: parse `public isolated function` in bala `sheet.bal`/`table.bal`/`workbook.bal` | Sheet 21, Table 18, Workbook 13 — name lists identical to #9 |
| 11 | Python: public-symbol coverage (46 source symbols vs render) | old missing 12, new missing 0 |
| 12 | `n["readme"]==o["readme"]`, `n["description"]==o["description"]` | `True`, `True` |
| 13 | JSON typeDef kind census | old `Record 19, Error 11, Constant 9, Enum 5, Class 2, Union 2, None 1`; new `… Class 3`, no `None` |
| 14 | JSON `Sheet`/`Table`/`Workbook` keys | old Sheet/Table lack `functions`; old Workbook lacks `type` (13 functions present but discarded); new all have `type`+`functions` |
| 15 | JSON `annotations` | old `[]`, new 1 (`Name`, `RECORD_FIELD`, `NameConfig`) |
| 16 | JSON `ParseError` | `{"type":"Error","baseType":"error<ErrorDetails>"}` — `distinct Error` lost at extractor level |
| 17 | JSON `Sheet.putRows` params | 5 params: 3 flattened `WriteOptions` fields + `options` (`optional:true`, no default) → invalid rendered signature |
| 18 | `diff -q` bala `modules/xlsx/*.bal` vs clone `ballerina/*.bal` (8 files) | no differences |
| 19 | `errors.bal:18–48` | `distinct error<ErrorDetails>` / `distinct Error` — confirms issue #1 |
| 20 | `types.bal:58` | `public const annotation NameConfig Name on record field;` |
| 21 | `types.bal:145`, `types.bal:177` | `int startRowIndex?`, `int insertAt?` — no defaults; confirms issue #3 |
| 22 | `ls` bala root; `grep include settings.gradle` | no `compiler-plugin/`; only `:xlsx-native`, `:xlsx-ballerina`, `:checkstyle` |
| 23 | `curl api.central.ballerina.io/…/ballerina/xlsx/1.0.1` | 1 module (`xlsx`), `ballerinaVersion 2201.12.0`, pullCount 26, no deprecation flag |
| 24 | `grep -n '^    function ' new render` | 52 method lines; each compared to its source declaration (§3) |
| 25 | `grep` for column-0 doc continuation lines | 6 in `new`, 6 in `old` — shared defect |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that specific rendered lines are "non-compiling Ballerina"
  (§5 items 2 and 7) are based on reading the language rules (required parameter after defaultable
  parameters; bare prose at column 0 inside a type body), not on running `bal build`.
- Signature checking for the 52 rendered methods was done by name-and-text comparison against the
  bala sources; the methods explicitly quoted in §3 were compared field by field, the remainder
  by name/arity. No mismatch was found in the sample, but this is a spot check, not an exhaustive
  token-level diff of all 52.
- The precomputed `OLD_AND_NEW_DIFFS/xlsx_diff.md` was re-derived independently
  (`diff -u`); its counts (269/16/5 hunks, 12→0 unknown types, 56 added declarations) match what
  was measured here. Its "56 declarations added" figure counts class methods as declarations; the
  §2 table above separates the 13 top-level additions from the 52 added method signatures.
- `pullCount 26` and the 2026 copyright headers indicate this module is very new; no assessment of
  runtime behaviour or of the native jar was attempted.

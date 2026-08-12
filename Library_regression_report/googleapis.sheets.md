# ballerinax/googleapis.sheets 4.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/googleapis.sheets` |
| Pinned version | `4.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-googleapis.sheets |
| Tag reviewed | `v4.0.0` (commit `e82538d9893ab03e74e264242bcc0099cf1cbee9`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/googleapis.sheets/4.0.0` |
| Old render | `754` lines |
| New render | `881` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Every one of the 8 diff hunks is either
(a) an `// Unknown type:` placeholder replaced by a real type definition, (b) a `@display`
annotation newly surfaced, or (c) the `Filter` union members losing their `ballerinax/googleapis.sheets:4.0.0:`
version qualification. Nothing was removed, truncated, or mangled.

Hard evidence that nothing was lost:
- 44 callable signatures (`init` + 43 remote functions) exist in both renders, and after stripping
  the newly-added inline `@display {...}` param annotations, **every parameter list, default value
  and return type is byte-identical** between the two.
- 26 record/enum bodies with **109 members total** in both renders; member-by-member set comparison
  shows zero differences.
- README block (lines 1–168) is byte-identical.
- JSON: `typeDefs` 50 → 50 (identical name sets), `clients[0].functions` 44 → 44 (identical name
  sets), `readme` 7107 chars both sides, `services`/`functions`/`annotations` empty both sides.

The gain: 3 degraded types recovered, 263 `@display` annotations surfaced (0 in `old`), 1
version-qualified union cleaned up.

## 2. Change inventory

Diff: 174 lines added, 47 removed, 8 hunks (`diff -u old new`).

| Kind | old | new | Delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 | −3 |
| `type` declarations (named, top-level) | 22 | 25 | +3 |
| `enum` declarations | 6 | 6 | 0 |
| `const` declarations | 20 | 20 | 0 |
| `client class` | 1 | 1 | 0 |
| `remote function` | 43 | 43 | 0 |
| `function init` | 1 | 1 | 0 |
| record/enum member lines | 109 | 109 | 0 |
| `@display` occurrences | 0 | 263 | +263 |
| version-qualified type refs (`:4.0.0:`) | 3 (1 line) | 0 | −3 |
| `// --- ` section markers | 4 | 4 | 0 |
| doc-comment lines (`# `) | 227 | 232 | +5 |

**Declarations added (3)** — all previously `// Unknown type:` stubs:
- `type Error error;`
- `type SpreadsheetError error;`
- `type InvalidRangeError error;`

**Declarations removed: 0.**

**Modified (annotation-only, no signature change):**
- 1 client class (`Client` gains `@display {label: "Google Sheets", iconPath: "icon.png"}`)
- 43 remote functions gain a method-level `@display` and inline param-level `@display`s
- 15 records + 4 enums gain type-level `@display`; ~60 record fields gain field-level `@display`
- `type Filter` union: `ballerinax/googleapis.sheets:4.0.0:A1Range|...` → `A1Range|DeveloperMetadataLookupFilter|GridRangeFilter`

## 3. Correctness against library source

Bala vs. upstream `v4.0.0`: `diff -q` on all six module files (`client.bal`, `constants.bal`,
`data_mappings.bal`, `errors.bal`, `types.bal`, `utils.bal`) reports **no differences**. The bala is
an exact copy of the tagged source, so both are equally authoritative here.

Everything `new` adds was checked:

1. **Error types.** `errors.bal:18,22,26`:
   `public type Error distinct error;`, `public type SpreadsheetError distinct Error;`,
   `public type InvalidRangeError distinct Error;`. All three exist; the doc text emitted by `new`
   (`errors.bal:17,20-21,24-25`) is reproduced verbatim.
2. **`@display` annotations.** Extracted all 264 `@display {label: "..."}` occurrences from the bala
   sources and all 263 from `new`; label multiset comparison shows **one** difference only (see §5.2).
   Spot-checked against source:
   - `types.bal:21` `@display {label: "Connection Config"}` → render line 235.
   - `types.bal:74-75` `@display {label: "", kind: "password"}` on `ProxyConfig.password` → render
     line 307. The empty label and `kind: "password"` are genuinely in the source.
   - `client.bal:23` `@display {label: "Google Sheets", iconPath: "icon.png"}` → render line 652.
   - `client.bal:1062` `@display {label: "Append Value"}` on `appendValues` — the render's apparent
     duplicate label with `appendValue` is a source-side typo, faithfully reproduced.
   - `client.bal:1397` `@display {label: "delete Row Using Data Filters"}` — lowercase `delete` is in
     the source, faithfully reproduced.
   - `client.bal:47-48,63-64,125-126` method + param labels match render lines 660-661, 671-672, 691-692.
3. **`Filter` union.** `types.bal:404`
   `public type Filter A1Range|DeveloperMetadataLookupFilter|GridRangeFilter;` — `new` (line 645)
   matches exactly; `old` (line 562) had the version-qualified form.
4. **Function set.** `client.bal` contains 43 `remote isolated function` declarations; both renders
   emit exactly 43, and the name sets in both JSONs are identical.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new` read in full (642 lines); every `-` line is either an `// Unknown type:` stub, the
  version-qualified `Filter` line, or a signature line re-emitted with `@display` annotations added.
- Signature-level comparison with `@display {...}` stripped: 44/44 functions match on parameter list,
  parameter defaults, and return type. Zero diffs.
- Record/enum member comparison: 26/26 bodies, 109/109 members, zero diffs.
- README/section-marker comparison: bytes 1–168 identical; 4 section markers on both sides.
- JSON comparison: identical `typeDefs` name set (50), identical client function name set (44),
  identical `readme`/`description` lengths.
- Declarations removed: 0.

## 5. Issues in `new` (independent of `old`)

Two are specific to what `new` added; six are pre-existing renderer behaviours that `old` shares
(listed because they are still wrong in `new`).

**Introduced with the new error-type rendering:**

1. **`distinct` and the error subtype hierarchy are flattened.** Source has
   `Error distinct error`, `SpreadsheetError distinct Error`, `InvalidRangeError distinct Error`
   (`errors.bal:18,22,26`). `new` emits all three as `type X error;` (render lines 223, 227, 231);
   the JSON records `"baseType": "error"` for all three. An LLM reading the render cannot tell that
   `SpreadsheetError` and `InvalidRangeError` are subtypes of `Error`, nor that they are distinct.
   Still a large net improvement over `old`'s bare `// Unknown type:` lines.

2. **One `@display` is dropped: the return-type annotation.** `client.bal:127`
   `returns @display {label: "Array of Worksheets"} Sheet[]|error` is not surfaced on
   `getSheets` in `new`. This is why the render has 263 `@display` occurrences vs. 264 in source.
   The identically-labelled field annotation (`types.bal:96`) is present. Only return-position
   annotations are affected; there is exactly one in this library.

**Pre-existing (present identically in `old` and `new`):**

3. **Non-compiling `init` default values.** Render line 654 (`new`) / 570 (`old`):
   `function init(ConnectionConfig config, string serviceUrl = https://sheets.googleapis.com, string driveServiceUrl = https://www.googleapis.com) returns error?;`
   — the string defaults are unquoted. Source uses the constants `BASE_URL` / `DRIVE_BASE_URL`
   (`client.bal:34-35`); the renderer inlined their values without quoting.

4. **Non-compiling doc continuation lines.** 7 doc lines (identical count in both renders) start at
   column 0 without a `#` prefix, e.g. `new` lines 411-412, 500, 552, 556, 569, 584. They break the
   record body they sit inside.

5. **Record fields with defaults rendered as optional.** `types.bal:94,95,97,99` declare
   `string spreadsheetId = ""`, `SpreadsheetProperties properties = {}`, `Sheet[] sheets = []`,
   `string spreadsheetUrl = ""` (required-with-default). The render (lines 315-325) emits them as
   `?` optional and drops the default. Same pattern across `SpreadsheetProperties`, `SheetProperties`,
   `GridProperties`, `ProxyConfig` (`userName`/`password` = `""` → `?`).

6. **Closed records rendered as open.** `ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`,
   `OAuth2RefreshTokenGrantConfig`, `ValuesRange` are `record {| ... |}` in source
   (`types.bal:22,56,66,79,249`); both renders emit `record { ... }`.

7. **Qualifiers dropped.** `public` and `isolated` are absent everywhere; source has
   `public isolated function init` (`client.bal:34`) and `remote isolated function` on all 43 methods.

8. **Enum members duplicated as top-level constants.** Render lines 171-209 emit 20 `const string`
   declarations. `REFRESH_URL` (`constants.bal:21`) is a genuine public const; the other 19 are the
   members of `ValueInputOption`, `ValueRenderOption`, `Visibility`, `LocationType`, `Dimension`,
   `LocationMatchingStrategy`, which are then re-emitted inside their `enum` bodies. Redundant token
   spend, not incorrect.

## 6. Coverage gaps vs. the library

**Zero gaps.** The package exports exactly one module (`export: ["googleapis.sheets"]` in
`package.json`; Ballerina Central lists a single module `googleapis.sheets`), which is the default
module — so the known `getDefaultModule()`-only limitation costs nothing here. There is no
submodule-only API.

All public symbols of the default module are present in both renders:

| Source | Public symbols | In render |
|---|---|---|
| `errors.bal` | `Error`, `SpreadsheetError`, `InvalidRangeError` | 3/3 (`new` only; `old` had stubs) |
| `constants.bal` | `REFRESH_URL`, `ValueInputOption`, `ValueRenderOption` | 3/3 |
| `types.bal` | 20 records + 4 enums + `Filter` (25 total, lines 22–404) | 25/25 |
| `client.bal` | `Client` + `init` + 43 remote functions | 45/45 |

`utils.bal` and `data_mappings.bal` declare no public symbols (`grep -nE '^public ' ` returns nothing).

## 7. Compiler plugin

**None.** The upstream `v4.0.0` tree has no `compiler-plugin`, `*-compiler-plugin`, or
`ballerina-*-compiler-plugin` directory, and the bala contains only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/`. Nothing is
expected to surface in the render from a plugin, and nothing is missing on that account.

## 8. Other considerations

- **Not deprecated.** Central reports `deprecated: null`, `visibility: public`, `pullCount: 312`,
  `ballerinaVersion: 2201.12.0`. Stable major version 4.0.0.
- **Size / token cost.** `new` is +127 lines (+16.8%). The growth is almost entirely `@display`
  annotations, which are UI metadata (low-code palette labels) and carry little value for an LLM
  generating code, but they do reproduce human-readable names for parameters whose doc comments the
  renderer otherwise drops (see below), so they are not pure noise.
- **Parameter docs are dropped on both sides.** Source has full `# + name - ...` doc blocks for every
  remote function (e.g. `client.bal:45-46`); both renders keep only the description line and an empty
  `# `. The new `@display` labels partially compensate.
- **Render is not compilable Ballerina** on either side, due to items §5.3 and §5.4. Unchanged by
  the spec-v2 switch.
- The `@display {label: "Append Value"}` collision between `appendValue`/`appendValues` and the
  lowercase `"delete Row Using Data Filters"` are upstream source defects, not render defects.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 754, new 881 |
| `grep -c '^// Unknown type:'` | old 3, new 0 |
| `grep -n '^// --- '` | both: README 7, END README 167, Types 169, Client (old 564 / new 647) |
| `diff -u old new \| wc -l` | 642 lines; `grep -c '^-[^-]'` = 47, `grep -c '^+[^+]'` = 174 |
| Full read of the unified diff | 8 hunks, all annotation/type-recovery; no deletions of substance |
| `grep -c 'remote function'` | old 43, new 43; `client.bal` has 43 `remote isolated function` |
| Python: regex-extract 44 signatures per render, strip `@display {...}`, compare | 44/44 identical (params, defaults, returns) |
| Python: extract 26 record/enum bodies per render, compare members | 26/26 bodies, 109/109 members, zero diffs |
| `diff <(sed -n '1,168p' old) <(sed -n '1,168p' new)` | identical |
| `grep -o '@display' \| wc -l` | old 0, new 263; bala sources 264 |
| `comm` on unique `@display` labels source vs `new` | none missing; multiset diff = `"Array of Worksheets"` 2→1 (`client.bal:127` return annotation) |
| `grep -n ':4\.0\.0:'` | old: 1 line (562) with 3 refs; new: 0 |
| `grep -c '^\s*# '` | old 227, new 232 |
| JSON compare (python) | `typeDefs` 50/50 same names; `clients[0].functions` 44/44 same names; `readme` 7107/7107; `services`/`functions`/`annotations` empty both |
| JSON `Error`/`SpreadsheetError`/`InvalidRangeError` entries | old `{"type":"Error"}`; new adds `"baseType":"error"` |
| `git ls-remote --tags` | `v4.0.0` → `e82538d9893ab03e74e264242bcc0099cf1cbee9` |
| `git clone --depth 1 --branch v4.0.0` + `diff -q` bala vs `ballerina/*.bal` | all 6 files identical |
| `ls src \| grep -i plugin`, `ls bala/any` | no compiler plugin on either side |
| `cat errors.bal` | 3 `distinct` error types confirmed, lines 18/22/26 |
| `grep -nE '^public '` on `constants.bal`, `utils.bal`, `data_mappings.bal` | 3 / 0 / 0 public symbols |
| `grep -nE '^public (isolated )?(type\|class\|enum\|const\|function...)' types.bal client.bal` | 25 public type-level symbols in `types.bal` |
| `curl api.central.ballerina.io/.../4.0.0` | single module `googleapis.sheets`, `deprecated: null`, `ballerinaVersion 2201.12.0` |
| `awk` for doc lines starting at column 0 inside bodies | 7 in old, 7 in new (new lines 411,412,500,552,556,569,584) |
| `grep -n 'function init'` both renders | unquoted URL defaults present identically (old 570, new 654) |

## 10. Caveats and unverified items

- Neither render was compiled. The syntax defects in §5.3 and §5.4 are identified by inspection
  against the Ballerina grammar, not by running `bal build` on the rendered text.
- I did not re-run the two-stage pipeline; the analysis is of the committed render/JSON artifacts.
  The claim that both sides were produced at the same pinned version rests on the brief plus the
  fact that both JSONs carry identical `readme` (7107 chars), `description`, and `typeDefs` name
  sets — consistent with one library version.
- The exact renderer code path that drops return-position `@display` (§5.2) was not read; the gap is
  established from the 264-vs-263 count and the identification of the single missing occurrence, not
  from the TypeScript/Java source.
- `@display` presence was verified by label multiset comparison against the source, which confirms
  every label reaches the render, but does not prove each annotation is attached to the *same*
  symbol in the render as in the source. Seven attachment points were checked individually
  (§3.2) and all were correct.

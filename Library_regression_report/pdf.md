# ballerina/pdf 0.9.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/pdf` |
| Pinned version | `0.9.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-pdf |
| Tag reviewed | `v0.9.1` (commit `6dff4fecf43e7de390e6e9967f8beb229de8fc2a`, grafted shallow clone) |
| Bala inspected | `/private/tmp/claude-501/-Users-admin-Desktop-Copilot-Changes-Check-contents-test-bal-copilot-library-get-mds/19909936-2e4b-46de-9886-3075396fe81e/scratchpad/extrabala/pdf/0.9.1` |
| Old render | `240` lines |
| New render | `246` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/pdf` is a small, single-module (`pdf`), pre-1.0 standard-library package: 7 public
functions and 10 public type definitions, no client objects, no listeners, no services, no
annotations, no compiler plugin.

The `old` → `new` delta is exactly two changes, both improvements:

1. The four error types (`Error`, `HtmlParseError`, `RenderError`, `ReadError`) were degraded to
   `// Unknown type: <Name>` in `old` (4 occurrences); `new` emits real type definitions with their
   doc comments (0 occurrences of `// Unknown type:`).
2. The one version-qualified type reference `ballerina/pdf:0.9.1:CustomPageSize` in
   `type PageSize` is now the plain `CustomPageSize`.

Nothing is removed, truncated or altered otherwise: the JSON top-level counts are identical on both
sides (7 functions, 13 typeDefs, 0 clients/services/annotations), the README block is byte-identical,
and the 7 function entries are byte-identical between the two JSONs. **No regressions.**

Several accuracy problems do exist in the render, but all except the error-type flattening are
present identically in `old` and `new` — they are pipeline-level issues, not spec-v2 regressions.
The most consequential is `parseHtml`, whose included-record parameter `*ConversionOptions options`
is expanded into named parameters carrying fabricated defaults, plus a trailing `ConversionOptions
options` parameter, producing a signature that does not compile and that contradicts the library's
own documented defaults.

## 2. Change inventory

Files: `pdf/old/ballerina_pdf.bal.txt` 240 lines, `pdf/new/ballerina_pdf.bal.txt` 246 lines
(`wc -l`). Diff: 2 hunks, +11 / −5 lines (`diff -u`).

| Kind | old | new | delta |
|---|---|---|---|
| README section lines | identical | identical | 0 |
| `const` | 3 (`A4`, `LETTER`, `LEGAL`) | 3 | 0 |
| `// Unknown type:` placeholders | 4 | 0 | −4 |
| `type … error;` definitions | 0 | 4 | +4 |
| `enum` | 1 (`StandardPageSize`) | 1 | 0 |
| `type … record { … };` | 4 (`CustomPageSize`, `PageMargins`, `Font`, `ConversionOptions`) | 4 | 0 |
| union `type` | 1 (`PageSize`) | 1 | 0 |
| module-level `function` | 7 | 7 | 0 |
| `class` / `client` / `service` / `listener` / `annotation` | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:ver:Type`) | 1 | 0 | −1 |

Declarations **added** in `new` (4), all as real definitions replacing placeholders:
`type Error error;`, `type HtmlParseError error;`, `type RenderError error;`, `type ReadError error;`
— each now carrying the doc comment from `errors.bal`.

Declarations **removed** in `new`: none.

Declarations **modified** in `new` (1): `type PageSize "LEGAL"|"LETTER"|"A4"|CustomPageSize;`
(was `…|ballerina/pdf:0.9.1:CustomPageSize;`).

JSON-level delta (structural comparison of `old/ballerina_pdf.json` vs `new/ballerina_pdf.json`):
the same 13 typeDef names and 7 function names in the same order; the only field-level differences
are `"baseType": "error"` added to the four error typeDefs, and the `PageSize` union member name
`ballerina/pdf:0.9.1:CustomPageSize` → `CustomPageSize`. `readme` and `description` compare equal.

## 3. Correctness against library source

The bala's `modules/pdf/*.bal` is byte-identical to `ballerina/*.bal` at tag `v0.9.1`
(`diff` on all four files returned no output), so GitHub and the bala agree.

Functions — all 7 present in both renders with matching parameter names, types and return types
against `modules/pdf/pdf_api.bal`:

| Render | Source | line |
|---|---|---|
| `extractText(byte[] pdf) returns string[]\|Error` | `public isolated function extractText(byte[] pdf) returns string[]\|Error` | pdf_api.bal:37 |
| `fileExtractText(string filePath) returns string[]\|Error` | matches | pdf_api.bal:45 |
| `urlExtractText(string url) returns string[]\|Error` | matches | pdf_api.bal:53 |
| `toImages(byte[] pdf) returns string[]\|Error` | matches | pdf_api.bal:63 |
| `fileToImages(string filePath) returns string[]\|Error` | matches | pdf_api.bal:71 |
| `urlToImages(string url) returns string[]\|Error` | matches | pdf_api.bal:79 |
| `parseHtml(string html, …, ConversionOptions options) returns byte[]\|Error` | `public isolated function parseHtml(string html, *ConversionOptions options) returns byte[]\|Error` | pdf_api.bal:26 — **does not match**, see §5.1 |

Types added by `new` — all four exist in `modules/pdf/errors.bal`:

- `Error` — source line 18: `public type Error distinct error;` → rendered `type Error error;`
  (loses `distinct`; see §5.2).
- `HtmlParseError` — line 22: `public type HtmlParseError distinct Error;` → rendered
  `type HtmlParseError error;` (loses `distinct Error`).
- `RenderError` — line 25: `public type RenderError distinct Error;` → same flattening.
- `ReadError` — line 29: `public type ReadError distinct Error;` → same flattening.

Doc comments on all four match the source verbatim (errors.bal:17, 20-21, 24, 27-28).

`PageSize` in `new` (`"LEGAL"|"LETTER"|"A4"|CustomPageSize`) corresponds to
`public type PageSize StandardPageSize|CustomPageSize;` (types.bal:34) with the enum inlined as its
three string literals — semantically equivalent set of values, and the reference to `CustomPageSize`
is now correct and resolvable, whereas `old`'s `ballerina/pdf:0.9.1:CustomPageSize` is not valid
Ballerina syntax.

Other types spot-checked against `modules/pdf/types.bal`: `StandardPageSize` (line 18, three
members), `CustomPageSize` (28, `float width`, `float height`), `PageMargins` (43, four `float`
fields), `Font` (56, `family`/`content`/`bold`/`italic`), `ConversionOptions` (79, six fields) —
all present with correct field names and types in both renders. Field-level fidelity issues
(closedness, defaults) are shared by both sides and covered in §5.

README: the render's README block (3347 chars in the JSON `readme` field) is an exact substring of
the bala's `docs/README.md` (also 3347 chars) — no content lost on either side.

## 4. Regressions

**None found.**

Basis for that conclusion:

- `diff -u old/ballerina_pdf.bal.txt new/ballerina_pdf.bal.txt` yields exactly 2 hunks; every
  removed line is either a `// Unknown type:` placeholder or the version-qualified `PageSize` line.
  No declaration, parameter, default, return type or doc line is dropped.
- Structural JSON comparison: identical typeDef name list (13) and function name list (7) in the
  same order; the only differing fields are the added `baseType: "error"` and the corrected
  `PageSize` member name. `readme` and `description` compare equal.
- Counted signals: `// Unknown type:` 4 → 0; version-qualified refs 1 → 0; section markers 4 → 4.
- All 7 function signatures are byte-identical between the two JSON files (verified by
  `json.dumps(..., sort_keys=True)` equality per function), so `parseHtml`'s defects predate spec v2.

## 5. Issues in `new` (independent of `old`)

Numbered by severity. Items 5.1 and 5.3–5.9 are present verbatim in `old` too; they are recorded
here because the brief asks for inaccuracies in `new` regardless of `old`.

**5.1 `parseHtml` signature is wrong and does not compile (shared with `old`).**
Source (pdf_api.bal:26) is `public isolated function parseHtml(string html, *ConversionOptions options) returns byte[]|Error`.
The render emits:

```
function parseHtml(string html, float fallbackFontSize = 12.0, PageSize pageSize = "LEGAL", PageMargins margins = {}, string additionalCss = "", Font[] customFonts = [], int maxPages = 0, ConversionOptions options) returns byte[]|Error;
```

Three defects: (a) the included-record parameter is expanded into named parameters *and* a trailing
`ConversionOptions options` parameter is retained — the record is offered twice; (b) that trailing
parameter is emitted without a default even though the JSON marks it `"optional": true`, so a
required parameter follows defaultable ones, which is a compile error in Ballerina; (c) the `*`
included-record syntax is lost entirely. An LLM copying this signature will write a call that does
not compile.

**5.2 Error hierarchy flattened (manifests only in `new`, since `old` had no definition at all).**
`Error` is `distinct error` and the other three are `distinct Error`. `new` renders all four as
`type X error;`, so `distinct` is lost and the fact that `HtmlParseError`/`RenderError`/`ReadError`
are subtypes of `Error` is lost. The JSON carries `"baseType": "error"` for all four, so the
flattening happens in the extractor, not the renderer. Consequence: a consumer cannot tell from the
render that `check`ing a `parseHtml` result and matching on `pdf:HtmlParseError` is meaningful.
Still strictly better than `old`'s bare `// Unknown type: HtmlParseError`.

**5.3 Fabricated parameter defaults on `parseHtml` (shared).**
Only `fallbackFontSize = 12.0` exists in the source (types.bal:80). The source declares
`pageSize?`, `margins?`, `additionalCss?`, `customFonts?`, `maxPages?` — optional, no defaults
(types.bal:81-85). The render invents `pageSize = "LEGAL"`, `margins = {}`, `additionalCss = ""`,
`customFonts = []`, `maxPages = 0`. `pageSize = "LEGAL"` directly contradicts the doc comment shown
two lines above it ("otherwise defaults to A4"), and `maxPages = 0` contradicts "Must be greater
than 0 when provided". These are the most likely lines to mislead an LLM after 5.1.

**5.4 Closed records rendered as open (shared).**
`CustomPageSize`, `PageMargins`, `Font` and `ConversionOptions` are all `record {| … |}` in
types.bal (lines 28, 43, 56, 79). All four render as `record { … }`.

**5.5 Record field defaults dropped; required-with-default fields become optional (shared).**
`PageMargins.top/right/bottom/left = 0` (types.bal:44-47), `Font.bold/italic = false` (59-60) and
`ConversionOptions.fallbackFontSize = 12.0` (80) are fields with defaults — the render marks them
`?` (optional) and shows no default value. The default survives only in the doc text.

**5.6 Enum members duplicated as top-level constants; render is not compilable (shared).**
`const string A4 = "A4";`, `const string LETTER`, `const string LEGAL` (render lines 94-98) are the
`StandardPageSize` members, which are also emitted inside `enum StandardPageSize` (lines 114-119 in
`new`). Declaring both in one module is a redefinition error. No standalone `const` declarations
exist in the library source.

**5.7 Enum member order reversed (shared).**
Source order is `A4, LETTER, LEGAL` (types.bal:19-21); render order is `LEGAL, LETTER, A4`. Cosmetic,
but it also drives 5.3's `pageSize = "LEGAL"` (first union member wins).

**5.8 `public` and `isolated` qualifiers dropped everywhere (shared).**
Every function in pdf_api.bal is `public isolated function`; the render shows plain `function`. Every
type is `public type`; the render shows `type`. Relevant here because `isolated` affects usability
from isolated contexts.

**5.9 `PageSize` loses the named enum reference (shared, minor).**
Rendered as `"LEGAL"|"LETTER"|"A4"|CustomPageSize` rather than `StandardPageSize|CustomPageSize`.
Value-equivalent, and arguably more explicit for an LLM, but it hides the relationship to the
`StandardPageSize` enum declared directly above it.

## 6. Coverage gaps vs. the library

**None.** `package.json` declares `"export": ["pdf"]` and Central lists exactly one module (`pdf`);
the bala's `modules/` directory contains only `pdf`, so there is no submodule-only API and the
`getDefaultModule()`-only extraction loses nothing here.

Complete public surface of `modules/pdf` and its presence in the renders:

| Symbol | kind | source | old | new |
|---|---|---|---|---|
| `parseHtml` | function | pdf_api.bal:26 | yes | yes |
| `extractText` | function | pdf_api.bal:37 | yes | yes |
| `fileExtractText` | function | pdf_api.bal:45 | yes | yes |
| `urlExtractText` | function | pdf_api.bal:53 | yes | yes |
| `toImages` | function | pdf_api.bal:63 | yes | yes |
| `fileToImages` | function | pdf_api.bal:71 | yes | yes |
| `urlToImages` | function | pdf_api.bal:79 | yes | yes |
| `Error` | error type | errors.bal:18 | placeholder | yes |
| `HtmlParseError` | error type | errors.bal:22 | placeholder | yes |
| `RenderError` | error type | errors.bal:25 | placeholder | yes |
| `ReadError` | error type | errors.bal:29 | placeholder | yes |
| `StandardPageSize` | enum | types.bal:18 | yes | yes |
| `CustomPageSize` | record | types.bal:28 | yes | yes |
| `PageSize` | union | types.bal:34 | yes | yes |
| `PageMargins` | record | types.bal:43 | yes | yes |
| `Font` | record | types.bal:56 | yes | yes |
| `ConversionOptions` | record | types.bal:79 | yes | yes |

Non-public symbols correctly absent from both renders: `init()` and `setModule()` (init.bal:19,23 —
module-private).

## 7. Compiler plugin

**Absent — confirmed, not assumed.** `has_plugin` is `false` in the manifest. The bala root contains
only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`, `platform/` — there
is no `compiler-plugin/` directory and no `compiler-plugin.json`. In the upstream clone at `v0.9.1`,
`find . -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` returns nothing; the repo's only
Java component is `native/` (the `pdf-native-0.9.1.jar` runtime library referenced from
`Ballerina.toml`'s `[[platform.java21.dependency]]`). Nothing plugin-implied is therefore missing
from the render.

(Note: the manifest addendum said Central-fetched balas have no `platform/` subdirectory; for `pdf`
one does exist — `platform/java21` with 8 jars. This does not affect the review.)

## 8. Other considerations

- **Pre-1.0.** Version `0.9.1`, published against distribution `2201.13.1`, 166 pulls at time of
  review, not deprecated (Central API). API is subject to change; `errors.bal:30` carries a `TODO`
  about adding more distinct error types.
- **Not GraalVM-compatible** (`"graalvmCompatible": false` in `package.json` /
  `graalvmCompatible = "No"` from Central). Not surfaced in either render — a consumer generating a
  native-image service would not learn this from the render. Shared gap, not a spec-v2 issue.
- **Size/token impact is negligible**: +6 lines, +88 bytes of JSON (19280 → 19368 bytes). The render
  is 9.9 KB.
- **Doc quality is good**: every public function and type has a doc comment, and the README's
  "Known limitations" section (render lines 78-88) is genuinely useful context for an LLM deciding
  whether `parseHtml` can render a given page.
- **Multi-line doc continuation lines lose their `# ` prefix** in the record-field and parameter
  docs (e.g. render lines 167-169, 194-196 in `new`): continuation text is emitted flush-left with
  no comment marker, which breaks the comment block. Shared by both sides, introduced by the
  renderer's handling of embedded `\n` in descriptions. Combined with 5.1 and 5.6, the render is not
  compilable Ballerina — treat it as documentation, not as a source file.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l pdf/{old,new}/ballerina_pdf.bal.txt` | 240 / 246 |
| `diff -u old/ballerina_pdf.bal.txt new/ballerina_pdf.bal.txt` | 2 hunks, +11 / −5; content as quoted in §2 |
| `grep -c '^// Unknown type:'` old / new | 4 / 0 |
| `grep -n 'ballerina/pdf:0.9.1'` old / new | old line 126 only / no match |
| `grep -n '^// --- '` old / new | 4 markers each (README, END README, Types, Functions) |
| Python structural JSON compare of `old/new` `*.json` | same 13 typeDef names, same 7 function names; only diffs = `baseType:"error"` ×4 and `PageSize` member rename; `readme` and `description` equal; all 7 functions byte-identical |
| `git clone --depth 1 --branch v0.9.1 …` | success, HEAD `6dff4fecf43e7de390e6e9967f8beb229de8fc2a`, tag `v0.9.1` |
| `diff ballerina/<f>.bal  bala modules/pdf/<f>.bal` for errors/init/pdf_api/types | all identical (no output) |
| `ls` bala root | `bala.json dependency-graph.json docs modules package.json platform` — no `compiler-plugin/` |
| `ls` bala `modules/` | `pdf` only (single module) |
| `find . -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` in clone | no matches |
| `cat package.json` | `"export": ["pdf"]`, `ballerina_version 2201.13.1`, `graalvmCompatible false`, 8 platform deps |
| `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/pdf/0.9.1` | 1 module (`pdf`), `deprecated: None`, pullCount 166, ballerinaVersion 2201.13.1, graalvmCompatible "No" |
| README substring check (`new` JSON `readme` vs bala `docs/README.md`) | both 3347 chars, render readme is an exact substring — nothing lost |
| `parseHtml` JSON param dump (`new`) | 8 params; `options` marked `"optional": true` but rendered with no default; `pageSize` default `"LEGAL"`, `margins` `{}`, `additionalCss` `""`, `customFonts` `[]`, `maxPages` `0` |
| `pdf_api.bal:26` (bala) | `public isolated function parseHtml(string html, *ConversionOptions options)` |
| `types.bal:79-86` (bala) | `ConversionOptions record {| float fallbackFontSize = 12.0; PageSize pageSize?; PageMargins margins?; string additionalCss?; Font[] customFonts?; int maxPages?; |}` |
| `types.bal:18-22` (bala) | `enum StandardPageSize { A4, LETTER, LEGAL }` — source order differs from render |
| `errors.bal:18-29` (bala) | `Error distinct error`; `HtmlParseError`/`RenderError`/`ReadError` are `distinct Error` |
| `OLD_AND_NEW_DIFFS/pdf_diff.md` claims | all verified against the files: 240/246 lines, +11/−5, 2 hunks, 4→0 placeholders, 1→0 qualified refs, 4 declarations added, 0 removed |

## 10. Caveats and unverified items

- The clone is `--depth 1` and grafted, so I verified the tag points at the reviewed tree but did not
  inspect history before `v0.9.1`. Not needed: the bala and the tagged tree are byte-identical for
  all four `.bal` files.
- I did not compile the render or the library; the "does not compile" claims in §5.1, §5.6 and §8
  are read off the Ballerina grammar/semantics (required parameter after defaultable; duplicate
  module-level symbol; unprefixed continuation lines inside a doc-comment block), not from a
  `bal build` run.
- The native jar (`pdf-native-0.9.1.jar`) was not decompiled; runtime behaviour of the external
  functions is out of scope and is not something either render claims to describe.
- I could not determine *why* the extractor synthesizes `pageSize = "LEGAL"` etc.; the pattern
  (first union member, empty literal per type) is consistent with type-driven default synthesis for
  included-record parameters, but I did not read the extractor source to confirm. The observation
  that the JSON is byte-identical between `old` and `new` for all functions is confirmed, and that is
  what matters for the regression verdict.

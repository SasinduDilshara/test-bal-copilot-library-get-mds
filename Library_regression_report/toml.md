# ballerina/toml 0.8.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/toml` |
| Pinned version | `0.8.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-toml |
| Tag reviewed | `v0.8.0` (commit `eeb39c83a7fcd131a39f0b08a7bf8f38b4f61c62`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/toml/0.8.0/any` |
| Old render | `90` lines |
| New render | `94` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/toml` is a small, pure-Ballerina standard-library module: 13 public symbols in the
default (and only exported) module — 9 type definitions and 4 functions. The entire old→new
delta lives in the `Types` section.

`new` fixes both known `main` defects for this library:

- All **4** `// Unknown type:` placeholders in `old` (`WritingError`, `LexicalError`,
  `GrammarError`, `ConversionError`) become real, doc-commented type definitions in `new`.
  `grep -c '^// Unknown type:'` → old `4`, new `0`.
- All **11** version-qualified type references (`ballerina/toml.parser:0.8.0:GrammarError`,
  `ballerina/io:1.8.1:Error`, …) are replaced with module-prefixed refs (`parser:GrammarError`,
  `io:Error`). No occurrences of `:0.8.0:` / `:1.8.1:` / `:1.13.0:` remain in `new`.

Nothing was dropped: the README block, the package description, and the entire `functions`
array are byte-identical between the two JSONs. Both renders share the same set of pre-existing
renderer inaccuracies (duplicated `io:file:Error` union member, included-record-parameter
flattening, lost record defaults/closedness, dropped `distinct`/`public`/`isolated`), none of
which `new` introduces or worsens.

## 2. Change inventory

Line counts (`wc -l`): old render 90, new render 94; old JSON 553, new JSON 557.
JSON diff is 34 changed lines (`diff old.json new.json | grep -c '^[<>]'`), all inside `typeDefs`.

| Kind | old | new | Delta |
|---|---|---|---|
| `type` declarations rendered | 5 | 9 | **+4** |
| `// Unknown type:` placeholders | 4 | 0 | **−4** |
| `function` declarations | 4 | 4 | 0 |
| `class` / `enum` / `const` / `annotation` / `service` / `listener` / client | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `typeDefs` entries in JSON | 9 | 9 | 0 |
| `functions` entries in JSON | 4 | 4 | 0 |
| `clients` / `services` / `annotations` in JSON | 0 | 0 | 0 |

**Declarations added in `new` (4)** — all were `// Unknown type:` stubs in `old`:

| New declaration | old line | new line |
|---|---|---|
| `type WritingError writer:WritingError;` | `23: // Unknown type: WritingError` | 23–24 |
| `type LexicalError lexer:LexicalError;` | `31: // Unknown type: LexicalError` | 32–33 |
| `type GrammarError parser:GrammarError;` | `33: // Unknown type: GrammarError` | 35–36 |
| `type ConversionError parser:ConversionError;` | `35: // Unknown type: ConversionError` | 38–39 |

Each also gained its doc comment, which `old` omitted entirely (e.g. new:33 is preceded by
`# Represents an error caused by the lexical analyzer.`).

**Declarations removed in `new`: 0.**

**Declarations modified (3 unions, rewritten refs only — same members, same order):**

| Type | old | new |
|---|---|---|
| `ParsingError` | `ballerina/toml.parser:0.8.0:GrammarError\|ballerina/toml.parser:0.8.0:ConversionError\|ballerina/toml.lexer:0.8.0:LexicalError` | `parser:GrammarError\|parser:ConversionError\|lexer:LexicalError` |
| `FileError` | `ballerina/io:1.8.1:Error\|ballerina/file:1.13.0:Error` | `io:Error\|file:Error` |
| `Error` | 6 version-qualified members | same 6 members, module-prefixed |

**JSON-level:** the 4 error typeDefs gain a `baseType` field in `new`
(`"baseType": "writer:WritingError"`, `"lexer:LexicalError"`, `"parser:GrammarError"`,
`"parser:ConversionError"`); in `old` those entries were `{"type": "Error"}` with no base, which
is exactly why the renderer degraded them to `// Unknown type:`.

**Unchanged:** `readme` (365 chars) and `description` are equal across JSONs; `functions` arrays
compare equal under `json.dumps`; the README block (render lines 8–15) diffs clean.

## 3. Correctness against library source

The bala's default module is byte-identical to the tagged upstream source — `diff` of
`errors.bal`, `toml.bal`, `types.bal`, `utils.bal` between
`<bala>/any/modules/toml/` and `<clone>/ballerina/` reports no differences for all four files.
Because the library is tiny, this check is exhaustive, not a spot-check.

All 4 declarations added by `new` verified against `<clone>/ballerina/errors.bal`:

| new render | source | verdict |
|---|---|---|
| `# Represents an error caused when writing a TOML file.` / `type WritingError writer:WritingError;` | errors.bal:32–33 `public type WritingError writer:WritingError;` | exact match (minus `public`) |
| `# Represents an error caused by the lexical analyzer.` / `type LexicalError lexer:LexicalError;` | errors.bal:36–37 | exact match |
| `# Represents an error caused for an invalid grammar production.` / `type GrammarError parser:GrammarError;` | errors.bal:39–40 | exact match |
| `# Represents an error caused by the Ballerina lang when converting a data type.` / `type ConversionError parser:ConversionError;` | errors.bal:42–43 | exact match |

The two rewritten unions are semantically faithful expansions, not inventions:

- Source errors.bal:30 is `public type ParsingError parser:ParsingError;`, and
  `<bala>/any/modules/toml.parser/error.bal:18` defines
  `public type ParsingError GrammarError|ConversionError|lexer:LexicalError;` — so `new`'s
  `parser:GrammarError|parser:ConversionError|lexer:LexicalError` is the correct flattening.
- Source errors.bal:23 is `public type Error ParsingError|WritingError|FileError;`; `new` renders
  the transitive leaves `parser:GrammarError|parser:ConversionError|lexer:LexicalError|WritingError|io:Error|file:Error`,
  which is the same set (`FileError` = errors.bal:27 `distinct (io:Error|file:Error)`).
  Note the flattening is inconsistent — `WritingError` is left unexpanded while `ParsingError`
  and `FileError` are expanded — but the resulting type is still correct. Identical behaviour in `old`.

All 4 functions verified against `<clone>/ballerina/toml.bal` (lines 24, 36, 46, 55): names,
parameter names/types/order, defaults (`= 2`, `= true`), and doc text all match. These lines are
identical in both renders, so nothing to attribute to `new`.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Set difference of declaration names extracted with
  `grep -nE '^(type|function)'` from both files: `new` is a strict superset of `old`
  (9 types vs 5, same 4 functions). Nothing in `old` is absent from `new`.
- `diff` of the two JSONs: 34 changed lines, all under `typeDefs`; `functions`, `readme`,
  `description`, `clients`, `services`, `annotations` compare equal.
- README block (render lines 8–15) diffs clean between sides and matches
  `<bala>/any/docs/README.md` (7 lines) verbatim.
- No parameter, default value, return type, doc line, or section marker is present in `old` and
  missing in `new` (section markers: 4 on both sides).

**Informational trade-off (not counted as a regression).** `old` named the defining package
inline (`ballerina/toml.parser:0.8.0:GrammarError`), whereas `new` writes `parser:GrammarError`.
Neither form is valid Ballerina in the render's context — the render's only import is
`import ballerina/toml;`, so no `parser:`/`lexer:`/`writer:`/`io:`/`file:` prefix is bound in
either version. `old` already used the bare-prefix form on all four function signature lines
(e.g. old:63), and both sides keep the `// Special Agent Note: … FROM ballerina/toml.parser package`
trailer on those lines, so package provenance for functions is preserved. What is genuinely lost
in the four type-def lines is that provenance hint — but in `old` three of those four lines did
not exist at all (`// Unknown type:`), so the net information is strictly higher in `new`.

## 5. Issues in `new` (independent of `old`)

All five below are present identically in `old`; they are renderer/extractor limitations, not
regressions. Listed because they misrepresent the library to a consumer of `new`.

1. **Duplicated, malformed union member `io:file:Error|io:file:Error`** in all four function
   return types (new:67, 75, 84, 94). The JSON links are correct — two distinct entries,
   `{"recordName":"Error","libraryName":"ballerina/io"}` and `{"…":"ballerina/file"}` — but the
   renderer concatenates both module prefixes onto each, producing `io:file:Error` twice instead
   of `io:Error|file:Error`. It gets this right in the `FileError` type def (new:27), so the bug
   is in the function-return path only.
2. **Included-record parameters are both flattened and retained.** Source signatures use
   `*ReadConfig config` / `*WriteConfig config` (toml.bal:24, 36, 46, 55). The render emits the
   expanded fields *and* a trailing `ReadConfig config` / `WriteConfig config` parameter, e.g.
   `function readString(string tomlString, boolean parseOffsetDateTime = true, ReadConfig config)`.
   That is non-compiling Ballerina (required parameter after a defaultable one) and duplicates
   the same configuration twice; an LLM copying it will write a call that does not compile.
3. **Record defaults and closedness lost in the type bodies.** Source types.bal:19–29 declares
   closed records with required-with-default fields
   (`record {| int indentationPolicy = 2; boolean allowDottedKeys = true; |}`). Both renders emit
   open `record { … }` with `?`-optional fields and no defaults (JSON: `defaultValue: null`,
   `optional: true` for all three fields). The default values survive only incidentally, in the
   flattened function parameters.
4. **`distinct` and `public`/`isolated` qualifiers dropped.** `FileError` is
   `distinct (io:Error|file:Error)` (errors.bal:27) but renders as a plain union; the underlying
   `GrammarError`/`ConversionError`/`LexicalError`/`WritingError` are `distinct error<…>` in the
   submodules. All type defs and functions lose `public`, and all four functions lose `isolated`.
5. **Unbound module prefixes / missing imports.** `parser:`, `lexer:`, `writer:`, `io:`, `file:`
   appear with no corresponding import line. Worse for this library specifically:
   `toml.parser`, `toml.lexer` and `toml.writer` are marked `"export": false` in the bala's
   `package.json`, so a user *cannot* import them at all — the only legitimate spellings are the
   `toml:`-level aliases. `new` at least now defines those aliases (`type GrammarError …`), which
   `old` did not.

## 6. Coverage gaps vs. the library

**Zero gaps in the default module.** The bala's `package.json` lists `"export": ["toml"]` and
marks `toml.parser`, `toml.writer`, `toml.lexer` as `"export": false`, so the default module is
the entire public API surface. Central metadata for `ballerina/toml/0.8.0` likewise reports
`modules: ['toml']`.

`grep -nE '^public ' <clone>/ballerina/*.bal` yields exactly 13 public symbols:

| Symbol | Source | In `old` | In `new` |
|---|---|---|---|
| `Error` | errors.bal:23 | yes | yes |
| `FileError` | errors.bal:27 | yes | yes |
| `ParsingError` | errors.bal:30 | yes | yes |
| `WritingError` | errors.bal:33 | **stub only** | yes |
| `LexicalError` | errors.bal:37 | **stub only** | yes |
| `GrammarError` | errors.bal:40 | **stub only** | yes |
| `ConversionError` | errors.bal:43 | **stub only** | yes |
| `WriteConfig` | types.bal:19 | yes | yes |
| `ReadConfig` | types.bal:27 | yes | yes |
| `readString` | toml.bal:24 | yes | yes |
| `readFile` | toml.bal:36 | yes | yes |
| `writeString` | toml.bal:46 | yes | yes |
| `writeFile` | toml.bal:55 | yes | yes |

13/13 present in `new`; 9/13 fully present in `old` (4 degraded to placeholders).
The only non-public symbol, `openFile` (utils.bal:21), is correctly absent from both.

Submodule-only API: none is exported, so the known `getDefaultModule()`-only extraction limitation
costs this library nothing. The submodule *error details* record
`toml.lexer:ReadErrorDetails` (`toml.lexer/error.bal:25`) — the `detail` shape behind every error
this module raises — is not reachable in either render, but it is also not exported by the
package, so it is not counted as a gap.

## 7. Compiler plugin

**No compiler plugin.** `manifest.has_plugin` is `false`, and that is confirmed independently:
`ls -a <bala>/any` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json` — no `compiler-plugin/` directory and no `compiler-plugin.json`. The upstream
clone at `v0.8.0` has no `compiler-plugin`, `*-compiler-plugin`, or `native` directory either
(root listing: `LICENSE README.md ballerina build-config build.gradle changelog.md codecov.yml
docs gradle gradle.properties gradlew gradlew.bat issue_template.md pull_request_template.md
settings.gradle spotbugs-exclude.xml`). The module is pure Ballerina with no Java native
component. Nothing plugin-implied is therefore missing from either render.

## 8. Other considerations

- **Pre-1.0 version.** `0.8.0` is below 1.0, so the API is not covered by Ballerina's
  compatibility guarantees. Central reports `deprecated: null`, `visibility: public`,
  `pullCount: 29` — low usage relative to core stdlib modules.
- **Built against an older distro.** `package.json` records `ballerina_version: 2201.12.0` while
  the bala consumed for the render ships in distribution `2201.13.4`. Not an issue — the
  distribution bundles this exact bala.
- **Size/tokens:** trivial. 94 lines / ~4.5 KB of render; the JSON grew 553→557 lines. The
  `+4` lines buy 4 previously-missing public types, an excellent ratio.
- **Doc quality:** every public symbol carries a doc comment, and all of them survive into `new`.
  The two record type defs render a stray empty `# ` continuation line (new:42, 52) — cosmetic,
  identical in `old`.
- **Practical impact of the fix:** `Error`, `GrammarError`, `ConversionError`, `LexicalError` and
  `WritingError` are what a user matches on in `do { } on fail` / `is` checks. With `old`, three of
  those five were invisible to the model. This is the highest-value class of fix for a
  foundational module.

## 9. Evidence log

| Check | Command / file:line | Result |
|---|---|---|
| Manifest entry | `python3 … manifest44.json` | version 0.8.0, `has_plugin: false`, bala from distribution 2201.13.4 |
| Line counts | `wc -l old/* new/*` | old render 90, new render 94; old JSON 553, new JSON 557 |
| Degraded types | `grep -c '^// Unknown type:'` | old `4`, new `0` |
| Declaration sets | `grep -nE '^(type\|function)'` on both | old 5 types + 4 fns; new 9 types + 4 fns |
| Declaration-ish line count | `grep -cE '^(type\|function\|class\|enum\|const\|annotation\|public )'` | old `9`, new `13` |
| Section markers | diff of `^// --- ` lines | 4 on both sides |
| JSON delta | `diff old.json new.json \| grep -c '^[<>]'` | 34 lines, all in `typeDefs` |
| JSON equality | Python: `readme`, `description`, `functions` | all equal across sides |
| `typeDefs` dump | Python over both JSONs | 9 entries both; `new` adds `baseType` on the 4 error types |
| Record fields | Python over `typeDefs[].fields` | both sides: `defaultValue: null`, `optional: true` for all 3 fields |
| Return-type links | `functions[0].return.type.links` | 6 links incl. `Error@ballerina/io` and `Error@ballerina/file` (both sides) |
| Tag resolution | `git ls-remote --tags … \| grep v0.8.0` | `v0.8.0` → `eeb39c83a7fc…` |
| Clone | `git clone --depth 1 --branch v0.8.0 …` | HEAD `eeb39c83a7fc…`, `git describe` → `v0.8.0` |
| Bala vs upstream | `diff` on errors.bal, toml.bal, types.bal, utils.bal | all four identical |
| Public API | `grep -nE '^public ' <clone>/ballerina/*.bal` | 13 symbols (9 types, 4 functions) |
| Submodule error defs | `<bala>/any/modules/toml.{parser,lexer,writer}/error.bal` | parser/error.bal:18,21,24; lexer/error.bal:16,25; writer/error.bal:16 |
| Export set | `<bala>/any/package.json` | `export: ["toml"]`; parser/writer/lexer `export: false` |
| Plugin absence | `ls -a <bala>/any`; upstream root listing | no `compiler-plugin/`, no `native/` |
| README fidelity | `<bala>/any/docs/README.md` (7 lines) vs render lines 8–15 | matches; identical old/new |
| Central metadata | `api.central.ballerina.io/2.0/registry/packages/ballerina/toml/0.8.0` | `deprecated: null`, `modules: ['toml']`, `pullCount: 29` |
| Precomputed diff | `OLD_AND_NEW_DIFFS/toml_diff.md` | claims (+11/−7, 1 hunk, 4 added decls, 4→0 unknowns, 11→0 qualified refs) all reproduced above |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that a signature is "non-compiling" (§5.2) are based on
  the Ballerina rule that a required parameter may not follow a defaultable one, not on a
  compiler run. The renders are documentation artifacts and are not expected to compile as-is.
- I did not re-run the two-stage pipeline; I audited the committed renders and JSONs as given.
  The attribution of every delta to the extractor/renderer change (rather than to a library
  difference) rests on the brief's statement that both sides used the same pinned bala, which is
  consistent with the byte-identical `readme`/`description`/`functions` payloads.
- `ParsingError`'s flattening was verified against the submodule source shipped in the bala; I did
  not verify that the extractor derives it that way in general (single-library observation).
- Nothing else was left unverified: the library is small enough that §3 and §6 are exhaustive
  rather than sampled.

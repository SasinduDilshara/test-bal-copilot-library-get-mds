# ballerina/yaml 0.8.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/yaml` |
| Pinned version | `0.8.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-yaml |
| Tag reviewed | `v0.8.0` (commit `15f706f71ec702ec94380eb506da5c40f864b13d`, grafted shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/yaml/0.8.0/any` |
| Old render | 195 lines |
| New render | 203 lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/yaml` is a small, entirely-declarative library: 4 public functions, 14 public error/type
aliases, 3 public records, 2 public enums — all in the single exported default module `yaml`
(`package.json` marks all 7 submodules `"export": false`).

`new` is strictly better than `old` on this library. The only two changes are the two known spec-v2
behaviours:

1. All 8 `// Unknown type:` placeholders in `old` become real, correctly-documented type
   definitions in `new` (the eight distinct-error aliases: `EmittingError`, `AliasingError`,
   `IndentationError`, `ConversionError`, `ComposeError`, `GrammarError`, `ScanningError`,
   `ConstructionError`).
2. All 31 version-qualified type references (`ballerina/yaml.composer:0.8.0:ComposeError`,
   `ballerina/io:1.8.1:Error`, `ballerina/yaml:0.8.0:SchemaError`, …) collapse to plain
   module-prefixed or bare refs (`composer:ComposeError`, `io:Error`, `SchemaError`).

Nothing was dropped, truncated, or made less accurate. Zero declarations removed. README,
description, function signatures, records, enums and consts are byte-identical between the two
renders.

Several accuracy defects exist in the render, but every one of them is present **identically in both
sides** — they are pre-existing pipeline behaviour, not spec-v2 regressions (see §5).

## 2. Change inventory

Line counts (`wc -l`): old **195**, new **203** (+8).

Declaration-name sets extracted with
`grep -oE '^(function|type|enum|const) [A-Za-z_]+' | sort` and compared with `comm`:

| Kind | old | new | Δ |
|---|---|---|---|
| `const` (enum members surfaced as consts) | 6 | 6 | 0 |
| `type` (record + union + error aliases) | 11 | 19 | **+8** |
| `enum` | 2 | 2 | 0 |
| `function` | 4 | 4 | 0 |
| `class` / `client` / `service` / `listener` / `annotation` | 0 | 0 | 0 |
| **Total declaration lines** | 21 | 29 | +8 |

**Added in `new` (8, all `type`)** — `comm -13` output:
`AliasingError`, `ComposeError`, `ConstructionError`, `ConversionError`, `EmittingError`,
`GrammarError`, `IndentationError`, `ScanningError`.

**Removed in `new`: 0** (`comm -23` empty).

**Modified (10 declarations)** — all de-qualification only:
`ComposingError`, `FileError`, `Error`, `SchemaError`, `ParsingError`, `LexicalError` (union member
refs de-versioned), and the two `YamlType` fields `construct` / `represent`
(`json|ballerina/yaml:0.8.0:SchemaError` → `json|SchemaError`).

Signals: `// Unknown type:` — old **8**, new **0**. Version-qualified refs — old 31, new 0
(`grep -c ':0\.8\.0:\|:1\.8\.1:\|:1\.13\.0:'`). Section markers `// --- ` — 4 in both
(README / END README / Types / Functions), only the `Functions` marker shifted 138 → 146.

JSON stage: both `ballerina_yaml.json` files have the same top-level keys and the same cardinalities
— `typeDefs` 25, `functions` 4, `clients` 0, `services` 0, `annotations` 0; `readme` and
`description` compare equal. The 8 error typeDefs that were `{"type":"Error"}` with no body in
`old` gain a `"baseType"` field in `new` (e.g. `"baseType":"emitter:EmittingError"`), which is what
lets the renderer emit a real definition.

## 3. Correctness against library source

Upstream `ballerina/errors.bal`, `ballerina/types.bal`, `ballerina/yaml.bal` at tag `v0.8.0` are
**byte-identical** to the bala's `modules/yaml/*.bal` (`diff` → identical for all three).

Every one of the 8 newly-emitted types matches the source exactly, doc string included
(`.../any/modules/yaml/errors.bal`):

| New render | Source line | Source declaration | Match |
|---|---|---|---|
| `type EmittingError emitter:EmittingError;` | errors.bal:35 | `public type EmittingError emitter:EmittingError;` | ✅ |
| `type AliasingError common:AliasingError;` | errors.bal:50 | `public type AliasingError common:AliasingError;` | ✅ |
| `type IndentationError common:IndentationError;` | errors.bal:53 | same | ✅ |
| `type ConversionError common:ConversionError;` | errors.bal:56 | same | ✅ |
| `type ComposeError composer:ComposeError;` | errors.bal:59 | same | ✅ |
| `type GrammarError parser:GrammarError;` | errors.bal:62 | same | ✅ |
| `type ScanningError lexer:ScanningError;` | errors.bal:65 | same | ✅ |
| `type ConstructionError schema:ConstructionError;` | errors.bal:68 | same | ✅ |

Doc comments in `new` are verbatim copies of the source doc comments (e.g. errors.bal:64
"Represents an error that is generated when an invalid character for a lexeme is detected." →
new:68).

The de-qualified union members are also faithful: `FileError` in the source is
`distinct (io:Error|file:Error)` (errors.bal:29) and `new` renders `io:Error|file:Error` — the
correct member set. `Error` (errors.bal:25) is `ComposingError|EmittingError|FileError`; both
renders flatten it to the transitive leaf set, and the leaf set in `new`
(`composer:ComposeError|parser:GrammarError|lexer:ScanningError|common:IndentationError|common:ConversionError|common:AliasingError|schema:ConstructionError|EmittingError|io:Error|file:Error`)
is correct given `ComposingError = composer:ComposingError` and the submodule union chains.

Records/enums (types.bal:26–88) verified field-by-field against new:77–144 — all 9 `WriteConfig`
fields, all 5 `ReadConfig` fields, all 5 `YamlType` fields, and both enums' member sets are present
with correct names, types and docs.

Functions (yaml.bal:24, 36, 46, 71): all 4 present in both renders with identical text; parameter
names `yamlString` / `filePath` / `yamlStructure` and the flattened config-record fields with their
source defaults (`indentationPolicy = 2`, `blockLevel = 1`, `schema = CORE_SCHEMA`,
`allowAnchorRedefinition = true`, …) match types.bal:26–51 exactly.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `comm -23` on the sorted declaration-name sets → empty (nothing in `old` is absent from `new`).
- Full `diff -u old new` is only 2 hunks, 24 added / 16 removed lines, all inside the `Types`
  section; the entire `Functions` section (lines 146–203 of `new`) is byte-identical to old lines
  138–195, verified by the absence of any diff hunk there.
- Section markers identical (4 = 4); README block identical and complete vs.
  `bala/.../docs/README.md` (all 7 content lines reproduced verbatim).
- JSON `readme` and `description` fields compare equal; no `typeDefs`/`functions` entry was dropped
  (25/4 on both sides); no field or doc string was removed from any modified typeDef — the only
  JSON deltas are member-name de-qualification and the *added* `baseType` key.
- Nothing became less specific: every changed type reference in `new` still names the same target
  type, only without the redundant `org/module:version:` prefix.

## 5. Issues in `new` (independent of `old`)

All of these are present verbatim in `old` too — they are pipeline-level, not spec-v2 regressions.

1. **Malformed module prefix `io:file:Error|io:file:Error`** (new:158, 170, 186, 203 — all 4
   functions; `grep -c 'io:file:Error'` = 4 in *both* files). The correct rendering is
   `io:Error|file:Error`, as `new` itself produces on line 39 for `FileError`. In the function
   return position the two prefixes are concatenated and the union degenerates to the same term
   twice. Non-compiling and misleading. Note the trailing `// Special Agent Note:` comment does
   disambiguate ("Error FROM ballerina/io package, Error FROM ballerina/file package").
2. **Included-record parameter rendered twice.** Source is
   `public isolated function readString(string yamlString, *ReadConfig config)` (yaml.bal:24). The
   render flattens `*ReadConfig` into 5 defaulted params **and** appends a required
   `ReadConfig config` parameter after them (new:158). A required parameter after defaulted ones is
   invalid Ballerina, and it implies the config can be passed both ways. Same for all 4 functions.
3. **`isolated` qualifier dropped everywhere.** `grep -c isolated` = 0 in both renders, while all 4
   public functions (yaml.bal:24, 36, 46, 71) and both `YamlType` function-typed fields
   (types.bal:64–65) are `isolated` in the source. Relevant for callers writing isolated code.
4. **`distinct` dropped from `FileError`.** Source: `public type FileError distinct (io:Error|file:Error)`
   (errors.bal:29); render: `type FileError io:Error|file:Error` (new:39). `grep -c distinct` = 0
   in both. Changes the type's identity semantics.
5. **Closed records rendered as open, with defaults turned into optionality.** `WriteConfig`,
   `ReadConfig`, `YamlType` are all `record {| ... |}` in types.bal; both renders emit
   `record { ... }` (`grep -c 'record {|'` = 0 in both). Fields that have defaults are marked `?`
   (new:79–95, 135–143) — they are *defaulted*, not optional — and the default values themselves are
   absent from the record body (they do appear in the flattened function params, so the information
   is not entirely lost). `YamlType`'s 3 genuinely-required fields (`tag`, `ballerinaType`, `kind`)
   are correctly rendered without `?`.
6. **Module prefixes are unresolvable in the render.** The only import emitted is
   `import ballerina/yaml;` (line 5 in both), yet the body uses the prefixes `composer:`, `parser:`,
   `lexer:`, `common:`, `schema:`, `emitter:`, `io:`, `file:`. Since `package.json` marks all 7
   `yaml.*` submodules `"export": false`, those types are **not importable by a user at all**.
   `new` mitigates this better than `old`, because it now also defines the top-level aliases
   (`yaml:ComposeError`, `yaml:ScanningError`, …) that users *can* reference. Still, an LLM reading
   `composer:ComposeError` may emit `import ballerina/yaml.composer;`, which will not resolve.
7. **Enum member documentation dropped.** types.bal:70–72 and 81–83 document each member
   (`# + MAPPING - YAML mapping collection`, `# + CORE_SCHEMA - An extension of JSON schema …`);
   neither render carries them (new:100–104, 124–128 are bare member lists). Enum member ordering
   is also reversed relative to the source in both renders — cosmetic only.

## 6. Coverage gaps vs. the library

**Zero gaps.** The exported default module `yaml` declares exactly 23 public symbols:

- 14 types in `errors.bal` (`Error`, `FileError`, `ComposingError`, `EmittingError`, `SchemaError`,
  `ParsingError`, `LexicalError`, `AliasingError`, `IndentationError`, `ConversionError`,
  `ComposeError`, `GrammarError`, `ScanningError`, `ConstructionError`)
- 5 types in `types.bal` (`WriteConfig`, `ReadConfig`, `YamlType`, `FailSafeSchema`, `YAMLSchema`)
- 4 functions in `yaml.bal` (`readString`, `readFile`, `writeString`, `writeFile`)

All 23 appear in `new` (19 `type`/`enum` declarations + 4 functions), plus 6 `const` lines for the
enum members. `old` also nominally lists all 23, but 8 of them are content-free `// Unknown type:`
stubs.

The two non-public module-level functions `openFile` and `generateTagHandlesMap` (utils.bal:23, 40)
and the non-public `readLines` (utils.bal:71) are correctly absent from both renders.

**Submodule API: not applicable as a gap.** `package.json` `"export": ["yaml"]` and every one of the
7 modules `yaml.schema`, `yaml.common`, `yaml.parser`, `yaml.composer`, `yaml.serializer`,
`yaml.emitter`, `yaml.lexer` carries `"export": false`. The `getDefaultModule()`-only extraction
therefore captures the complete public surface of this package — unlike libraries whose API lives in
exported submodules.

## 7. Compiler plugin

Manifest says `has_plugin: false`, confirmed two ways:
- `ls .../0.8.0/any/compiler-plugin` → "No such file or directory"; the bala root contains only
  `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`.
- `find <clone> -maxdepth 2 -iname '*compiler-plugin*'` in the `v0.8.0` checkout → no results.

`ballerina/yaml` ships no compiler plugin, so there are no code actions, validations, generated
artifacts, or plugin-driven annotations that could be expected to surface in the render. Consistently,
`annotations` is `[]` in both JSONs. Nothing missing.

## 8. Other considerations

- **Pre-1.0 version.** `0.8.0` — the package is not yet API-stable; `Ballerina.toml`/`package.json`
  give `ballerina_version: 2201.12.0`, language spec `2024R1`. No deprecation markers appear in the
  bala source (`@deprecated` absent from all 4 default-module `.bal` files).
- **`graalvmCompatible: true`**, platform `any` (pure Ballerina, no JAR dependencies) — the bala has
  no platform-specific subdirectory beyond `any/`.
- **Size/tokens:** 203 lines is negligible; the +8 lines cost is trivially worth the removal of 8
  content-free stubs. The four `// Special Agent Note:` trailing comments on the function lines are
  each ~330 characters and are duplicated verbatim 4 times — roughly 1.3 KB of the file, a
  measurable fraction of a 203-line render, and they exist on both sides.
- **Doc quality:** doc strings are complete and carried through faithfully; some end with trailing
  double-spaces (source artefact, e.g. "Number of whitespace for an indentation  "), harmless.
- The published package compiles upstream (renders are extraction artefacts; the non-compiling
  constructs listed in §5 are renderer output, not library defects).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_yaml.bal.txt new/ballerina_yaml.bal.txt` | 195 / 203 |
| `diff -u old new` | 2 hunks, +24 / −16, both inside `// --- Types ---` |
| `grep -c '^// Unknown type:'` old / new | 8 / 0 |
| `grep -n '^// Unknown type:' old` | lines 35, 52, 54, 56, 58, 60, 62, 64 |
| `comm -23` sorted decl sets | empty → 0 declarations removed |
| `comm -13` sorted decl sets | 8 types added (listed §2) |
| `grep -cE '^(function\|type\|enum\|const) '` old / new | 21 / 29 |
| `diff <(grep -n '^// --- ' old) <(grep -n '^// --- ' new)` | only the `Functions` marker moved 138→146 |
| `grep -n '^import' old new` | `import ballerina/yaml;` at line 5 in both |
| `grep -c 'io:file:Error'` old / new | 4 / 4 |
| `grep -c 'isolated'` old / new | 0 / 0 |
| `grep -c 'distinct'` old / new | 0 / 0 |
| `grep -c 'record {\|'` old / new | 0 / 0 |
| Python JSON compare of `typeDefs` | same 25 names; 15 differ, all de-qualification; 8 gained `baseType`; none lost a field |
| Python JSON compare of `functions` | same 4 names, byte-identical entries |
| Python compare of `readme` / `description` | equal on both sides |
| `git clone --depth 1 --branch v0.8.0 <repo>` | success, HEAD `15f706f7`, tag `v0.8.0` |
| `diff <clone>/ballerina/{errors,types,yaml}.bal <bala>/modules/yaml/` | identical for all 3 |
| `ls <bala>/any/modules` | yaml, yaml.common, yaml.composer, yaml.emitter, yaml.lexer, yaml.parser, yaml.schema, yaml.serializer |
| `cat <bala>/any/package.json` | `export: ["yaml"]`; all 7 submodules `"export": false` |
| `ls <bala>/any/compiler-plugin` | does not exist |
| `find <clone> -iname '*compiler-plugin*'` | no results |
| `head <bala>/any/docs/README.md` vs. render lines 8–15 | verbatim, complete |
| errors.bal:25,29,35,50,53,56,59,62,65,68 vs. new:36,39,42,54,57,60,63,66,69,72 | signatures and docs match |
| types.bal:26–88 vs. new:77–144 | all record fields and enum members match |
| yaml.bal:24,36,46,71 vs. new:158,170,186,203 | function names/params/defaults match; qualifiers and `*Config` handling differ (§5) |

## 10. Caveats and unverified items

- The clone is a shallow, grafted checkout of tag `v0.8.0`; history before that commit was not
  fetched, so I could not diff against neighbouring versions. Not needed — the bala and the tag are
  byte-identical, which is the authoritative comparison.
- I did not read the submodule sources (`yaml.common`, `yaml.composer`, `yaml.lexer`,
  `yaml.parser`, `yaml.schema`, `yaml.emitter`, `yaml.serializer`). The union expansions in `new`
  (e.g. `ComposingError` → 7 leaf members) were validated only for *shape* and against the
  top-level aliases; the exact leaf membership of `composer:ComposingError`,
  `parser:ParsingError`, `lexer:LexicalError` and `schema:SchemaError` inside those submodules is
  **unverified**. Both renders produce the same expansion, so this cannot be a spec-v2 regression
  either way.
- I did not re-run the render pipeline; the audit compares the committed artefacts as given.
- I did not query Ballerina Central's registry API for this package (deprecation status, keywords);
  the bala's `package.json` was used instead and shows no deprecation field. Central-side
  deprecation status is therefore **unverified**.
- The `// Special Agent Note:` comment convention is present on both sides; I did not trace it to
  the renderer source to confirm it is intentional rather than a leaked debug string.

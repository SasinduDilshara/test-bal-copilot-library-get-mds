# ballerina/data.yaml 0.8.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/data.yaml` |
| Pinned version | `0.8.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-data.yaml |
| Tag reviewed | `v0.8.0` (exact tag, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/data.yaml/0.8.0/java21` |
| Old render | `191` lines |
| New render | `198` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`data.yaml` is a small, single-module standard-library package: 10 public symbols in the default
module `data.yaml`, spread over two `.bal` files (`init.bal`, `yaml_api.bal`, 173 lines total in
the bala). The bala sources are byte-identical to the `v0.8.0` GitHub tag (`diff` returned no
output for both files), so upstream and bala agree completely.

`new` differs from `old` in exactly two hunks (+8 / −1 lines, verified with `diff -u`):

1. `// Unknown type: Error` is replaced by a real, documented `type Error error;` definition.
2. A new `// --- Annotations ---` section emits `public annotation NameConfig Name on record field;`,
   the package's only annotation — completely absent from `old`.

Nothing is removed, renamed, reordered, or truncated. The README block, all 4 functions, the enum,
the 3 record types and the 3 constants are byte-identical between the two renders. `new` now covers
100% of the package's public API (10/10 symbols); `old` covered 8 fully, 1 degraded, 1 missing.

Both renders share a set of pre-existing extractor inaccuracies (record fields shown as optional
with defaults dropped, `typedesc<anydata> t = <>` flattened to `anydata t = anydata`, `public`/
`isolated` qualifiers dropped, enum members duplicated as module constants). These are identical on
both sides and are therefore **not** regressions; they are recorded in §5 because they still mislead
a consumer of `new`.

## 2. Change inventory

Counts from `grep -cE` on each render (the `type:` counts below exclude one `type Book record {|`
line that lives inside the README code fence at line 40 of both files).

| Kind | old | new | Δ |
|---|---|---|---|
| `const` | 3 | 3 | 0 |
| `enum` | 1 | 1 | 0 |
| `type` (real declarations) | 3 | 4 | **+1** (`Error`) |
| `function` | 4 | 4 | 0 |
| `annotation` | 0 | 1 | **+1** (`Name`) |
| `class` / `client class` / `service` / `listener` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | **−1** |
| `// --- section ---` markers | 4 | 5 | +1 (`Annotations`) |
| Total lines | 191 | 198 | +7 |

**Declarations added in `new` (2):**

- `type Error error;` with its 2-line doc comment (replacing the `// Unknown type: Error` stub at
  old:130).
- `public annotation NameConfig Name on record field;` with its doc comment (new:195–198).

**Declarations removed in `new`: 0.**
**Declarations modified in `new` (other than the above): 0** — `diff -u` produces only the two
hunks listed above.

**JSON-level inventory** (`old/ballerina_data.yaml.json` 13,940 B vs `new/…json` 14,329 B):

| Field | old | new |
|---|---|---|
| `functions` | 4 | 4 (byte-identical, verified by dict comparison) |
| `typeDefs` | 8 | 8 (only `Error` differs) |
| `annotations` | **0** | **1** |
| `clients` / `services` | 0 / 0 | 0 / 0 |
| `readme` / `description` / `name` | — | identical |

The only `typeDefs` delta is that `new` adds `"baseType": "error"` to the `Error` entry; the renderer
uses that field to emit a definition instead of the placeholder.

## 3. Correctness against library source

Every public symbol checked against the bala at
`…/0.8.0/java21/modules/data.yaml/yaml_api.bal` (identical to `src/ballerina/yaml_api.bal` at tag
`v0.8.0`). This library is small enough to audit exhaustively; all 10 public symbols were checked.

| Symbol | Source | Rendered in `new` | Accurate? |
|---|---|---|---|
| `parseString` | yaml_api.bal:32–34 | new:154 | signature order/types OK; `typedesc<anydata> t = <>` flattened (see §5.3) |
| `parseBytes` | yaml_api.bal:48–50 | new:168 | same |
| `parseStream` | yaml_api.bal:64–66 | new:182 | same, `stream<byte[], error?>` preserved exactly |
| `toYamlString` | yaml_api.bal:77 | new:193 | `anydata yamlValue, WriteConfig config = {}` → `string\|Error` — exact |
| `YAMLSchema` | yaml_api.bal:90–94 | new:88–92 | members correct, order reversed (§5.5) |
| `Options` | yaml_api.bal:97–115 | new:96–107 | field names/types correct; closed→open, defaults lost (§5.1/5.2) |
| `WriteConfig` | yaml_api.bal:118–135 | new:111–128 | all 8 fields, names/types/docs correct; same closed→open + defaults issue |
| `Error` | yaml_api.bal:139 `public type Error distinct error;` | new:130–132 `type Error error;` | **new in `new`**; `distinct` dropped (§5.4) |
| `NameConfig` | yaml_api.bal:142–145 | new:136–139 | `string value;` required — correct |
| `Name` annotation | yaml_api.bal:148 `public const annotation NameConfig Name on record field;` | new:198 | **new in `new`**; `const` dropped (§5.4) |

Both `new`-only additions are genuine: `Error` and `Name` exist verbatim in the pinned source at the
lines cited. Neither is invented.

Doc text fidelity: the annotation's doc string in `new:197` ("The annotation is used to overwrite
the existing record field name.") matches yaml_api.bal:147 exactly. The `Error` doc in new:130–131
matches yaml_api.bal:137–138 exactly (two lines, unwrapped).

README fidelity: `sed -n '8,75p' new/… | diff - docs/Package.md` reports only `68d67` (one trailing
blank line). The rendered README is otherwise a byte-exact copy of the bala's `docs/Package.md`,
which itself is identical to `ballerina/Package.md` at the tag. Identical in `old`.

Non-public symbols correctly excluded from both renders: `NEW_LINE_CHARACTER` (yaml_api.bal:19),
`toYamlStringArray` (yaml_api.bal:82), `init` and `setModule` (init.bal:19, 23).

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- `diff -u old new` on the full render — exit 1 with exactly two hunks, both purely additive apart
  from the removal of the `// Unknown type: Error` stub line. No declaration, parameter, default,
  return type, doc line, or README line is present in `old` and absent in `new`.
- Structured JSON comparison: `functions` dicts compare equal between the two files; `typeDefs` name
  sets identical (`CORE_SCHEMA, Error, FAILSAFE_SCHEMA, JSON_SCHEMA, NameConfig, Options,
  WriteConfig, YAMLSchema` on both sides); the only per-typeDef difference is the *added*
  `baseType: "error"` on `Error`. `clients`, `services` both empty on both sides.
- Section markers: `old` has README/END README/Types/Functions; `new` has those four plus
  `Annotations`. Nothing lost.
- Encoding: both files are UTF-8, both contain the same 4 `⇒` characters in doc examples, zero
  mojibake sequences (`grep -cE 'Ã|â€'` = 0 on both). The spec-v2 change introduced no encoding drift.
- Syntax: no new malformed construct. `type Error error;` and
  `public annotation NameConfig Name on record field;` are both syntactically valid Ballerina.

## 5. Issues in `new` (independent of `old`)

These are inaccuracies versus the library source that exist in `new`. **All but 5.4 are also present
in `old`** — they are extractor-level, not introduced by spec v2.

**5.1 Closed records rendered as open (shared with `old`).** All three record types are `record {| … |}`
(closed) in the source — `Options` (yaml_api.bal:97), `WriteConfig` (:118), `NameConfig` (:142) — but
render as `record { … }`. An LLM could emit an extra field into an `Options` value and produce
non-compiling code.

**5.2 Record field defaults dropped, required fields shown optional (shared with `old`).** Every field
of `Options` and `WriteConfig` has a default in the source (`YAMLSchema schema = CORE_SCHEMA`,
`boolean allowAnchorRedefinition = true`, `int indentationPolicy = 2`, `int blockLevel = 1`, …) and
none is optional. Both renders emit them as `schema?`, `allowAnchorRedefinition?`, `indentationPolicy?`
… with no default shown. The JSON confirms this is upstream of the renderer: every field carries
`"optional": true` and no `default` key. The defaults are lost information for both sides.

**5.3 `typedesc` inference parameter flattened (shared with `old`).** Source declares
`typedesc<anydata> t = <>` for the three `parse*` functions; both renders show `anydata t = anydata`
while still returning `t|Error`. Using `t` as a return type when it is declared `anydata` is not
valid Ballerina — this render is not compilable as written, on either side.

**5.4 Type qualifiers lost on the two symbols `new` adds.** These exist only in `new` because the
declarations themselves only exist in `new`:
- `public type Error distinct error;` (yaml_api.bal:139) renders as `type Error error;` — the
  `distinct` qualifier is dropped. Since `data.yaml:Error` is a distinct error type that other code
  matches on, an LLM told it is a plain `error` alias could write a wrong `is`/`error` check.
- `public const annotation NameConfig Name on record field;` (yaml_api.bal:148) renders as
  `public annotation NameConfig Name on record field;` — `const` dropped. Harmless for typical usage
  but not the true declaration.

Both are still a large net improvement over `old`, which emitted a bare stub and nothing at all
respectively.

**5.5 Enum members duplicated as constants and reordered (shared with `old`).** Both renders emit
`const string FAILSAFE_SCHEMA = "FAILSAFE_SCHEMA";` / `JSON_SCHEMA` / `CORE_SCHEMA` as three
module-level constants (render lines 80–84) *in addition to* the `YAMLSchema` enum. The source has no
such module-level constants — they are the enum members surfaced twice (they appear as separate
`typeDefs` entries in both JSONs). Harmless in practice (`yaml:CORE_SCHEMA` is valid), but it is
invented structure. Separately, the enum members render in the order `CORE_SCHEMA, JSON_SCHEMA,
FAILSAFE_SCHEMA` while the source order is `FAILSAFE_SCHEMA, JSON_SCHEMA, CORE_SCHEMA` — cosmetic.

**5.6 `public`/`isolated` qualifiers dropped from functions (shared with `old`).** All four functions
are `public isolated function` in the source; both renders emit bare `function`. Consistent renderer
convention rather than a per-library defect.

## 6. Coverage gaps vs. the library

**`new`: zero gaps.** The bala's `package.json` lists `"export": ["data.yaml"]` and `modules/`
contains only `data.yaml` — there are **no submodules**, so the known `getDefaultModule()`-only
limitation costs this library nothing. Central's metadata for `ballerina/data.yaml/0.8.0` likewise
reports a single module.

`grep -nE '^public ' modules/data.yaml/*.bal` yields exactly 10 public declarations. All 10 appear in
`new`. In `old`, 8 appear fully, `Error` is degraded to a placeholder, and `Name` is absent — 1 gap
plus 1 degradation, both closed by `new`.

| Public symbol | in `old`? | in `new`? |
|---|---|---|
| `parseString`, `parseBytes`, `parseStream`, `toYamlString` | yes | yes |
| `YAMLSchema`, `Options`, `WriteConfig`, `NameConfig` | yes | yes |
| `Error` | placeholder only | yes |
| `Name` (annotation) | **no** | yes |

No submodule-only API exists, so there is no shared submodule gap to note.

## 7. Compiler plugin

`has_plugin: true` — confirmed. The bala carries `compiler-plugin/compiler-plugin.json`:

```
plugin_id:    constraint-compiler-plugin
plugin_class: io.ballerina.lib.data.yaml.compiler.YamlDataCompilerPlugin
dependency:   compiler-plugin/libs/data.yaml-compiler-plugin-0.8.0.jar
```

Source at the tag: `compiler-plugin/src/main/java/io/ballerina/lib/data/yaml/compiler/` — 5 classes
(`YamlDataCompilerPlugin`, `YamlDataCodeAnalyzer`, `YamlDataTypeValidator`, `YamlDataDiagnosticCodes`,
`Constants`).

What it contributes — **validation only, no code generation and no code actions**:

- Two compile-time diagnostics (`YamlDataDiagnosticCodes.java:31–32`), both severity `ERROR`:
  - `YAML_ERROR_201` "invalid field: duplicate field found"
  - `YAML_ERROR_202` "unsupported type: type is not supported"
- `YamlDataTypeValidator` inspects the expected type at call sites of `parseString`, `parseBytes`,
  `parseStream` (`Constants.java:32–34`) and at module variable / type definitions, walking record,
  union and tuple types (`validateRecordType`, `validateUnionType`, `validateTupleType`,
  `validateExpectedType` at lines 191–236) to reject unsupported expected types.
- It resolves the `Name` annotation (`Constants.NAME = "Name"`, `getNameFromAnnotation` at line 297,
  `isYamlImport` at line 321) so that duplicate-field detection accounts for renamed fields.

Nothing the plugin implies is missing from `new`: the only user-facing symbol the plugin depends on
is the `Name` annotation and its `NameConfig` constraint type, and **both are now rendered** (new:198
and new:136–139). This is precisely the gap `old` had — `old` rendered `NameConfig` but never told a
consumer that the `@yaml:Name` annotation exists, making the record-field-renaming feature
undiscoverable from the render. The plugin's diagnostics themselves are not renderable API.

## 8. Other considerations

- **Pre-1.0 version.** `0.8.0` — the package is below 1.0 and its API may still change. Not a render
  defect; worth knowing when this render is used as ground truth.
- **Not deprecated.** Central reports `deprecated: null`, `deprecateMessage: ""`. `graalvmCompatible:
  true`, license Apache-2.0, keywords `["yaml"]`, 27 pulls at time of check.
- **Distribution skew.** `Ballerina.toml` declares `distribution = "2201.12.0"` while the bala used
  for the renders ships inside distribution `2201.13.4`. Version in `Ballerina.toml` is `0.8.0`, so
  the pin is correct; no drift.
- **Size/token impact is negligible.** +7 lines (+3.7%), +389 bytes of JSON (+2.8%). This library
  will not be a token-budget concern in a Copilot context.
- **Doc quality of the library itself is mediocre in places.** `Options` field docs are placeholder
  text in the source ("schema - field description", "allowAnchorRedefinition - field description" —
  yaml_api.bal:98, 100, 102). The render faithfully reproduces this; the weakness is upstream, not in
  either renderer.
- **README is a duplicated `Package.md`.** The repo has both `ballerina/Module.md` and
  `ballerina/Package.md` (they differ), but the bala ships only `docs/Package.md`, and that is what
  both renders embed. No content is lost relative to what the extractor could see.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git clone --depth 1 --branch v0.8.0 …/module-ballerina-data.yaml` | tag exists, clone OK (detached HEAD) |
| 2 | `ls …/0.8.0` and `…/0.8.0/java21` | platform dir `java21`; contains `modules/`, `docs/`, `compiler-plugin/`, `package.json`, `bala.json`, `dependency-graph.json` |
| 3 | `ls …/java21/modules` | single module `data.yaml` → no submodules |
| 4 | `wc -l …/modules/data.yaml/*.bal` | `init.bal` 25, `yaml_api.bal` 148 (173 total) |
| 5 | `diff bala/init.bal src/ballerina/init.bal` | identical (`SAME_init`) |
| 6 | `diff bala/yaml_api.bal src/ballerina/yaml_api.bal` | identical (`SAME_api`) |
| 7 | `cat …/ballerina/Ballerina.toml` | `org=ballerina name=data.yaml version=0.8.0` → pin confirmed |
| 8 | `wc -l old/…bal.txt new/…bal.txt` | 191 / 198 |
| 9 | `diff -u old new` | exit 1; 2 hunks; +8 −1 lines; no deletions other than the `Unknown type` stub |
| 10 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 11 | `grep -cE '^const '` | old 3, new 3 |
| 12 | `grep -cE '^enum '` | old 1, new 1 |
| 13 | `grep -cE '^type '` | old 4, new 5 (each includes 1 README-code-fence line → 3 vs 4 real) |
| 14 | `grep -cE '^function '` | old 4, new 4 |
| 15 | `grep -cE '^public annotation '` | old 0, new 1 |
| 16 | `grep -cE '^(class\|client class\|service)'` | 0 / 0 |
| 17 | `grep -c '^// --- '` | old 4, new 5 |
| 18 | `grep -n '^// --- ' new` | lines 7, 76, 78, 141, 195 |
| 19 | `wc -c` on JSONs | old 13,940 B, new 14,329 B |
| 20 | Python dict compare of JSON top-level keys | same 8 keys both sides |
| 21 | Python compare of `functions` | identical both sides (4 each) |
| 22 | Python compare of `typeDefs` | 8 each, same names; only `Error` differs — `new` adds `"baseType":"error"` |
| 23 | Python dump of `annotations` | old `[]`; new 1 entry: `Name`, `RECORD_FIELD`, typeConstraint `NameConfig` |
| 24 | `grep -nE '^public ' bala/modules/data.yaml/*.bal` | 10 public symbols (yaml_api.bal:32,48,64,77,90,97,118,139,142,148) |
| 25 | `grep -nE '^(const\|isolated function\|function\|type\|enum\|class\|annotation)'` | 4 non-public module-level symbols, all correctly absent from both renders |
| 26 | yaml_api.bal:139 | `public type Error distinct error;` vs new:132 `type Error error;` → `distinct` dropped |
| 27 | yaml_api.bal:148 | `public const annotation NameConfig Name on record field;` vs new:198 → `const` dropped |
| 28 | yaml_api.bal:97,118,142 | all three records are `record {\| … \|}` (closed); both renders emit open `record { }` |
| 29 | yaml_api.bal:99–114, 120–134 | every field has a default; both renders emit `?` and no default |
| 30 | yaml_api.bal:33,49,65 | `typedesc<anydata> t = <>`; both renders emit `anydata t = anydata` |
| 31 | yaml_api.bal:90–94 vs render 88–92 | enum member order reversed (source FAILSAFE,JSON,CORE) |
| 32 | `sed -n '8,75p' new \| diff - bala/docs/Package.md` | only `68d67` (trailing blank line) → README byte-exact |
| 33 | `diff bala/docs/Package.md src/ballerina/Package.md` | identical |
| 34 | `ls bala/docs` | only `Package.md` (no `Module.md` in bala) |
| 35 | `cat bala/compiler-plugin/compiler-plugin.json` | `constraint-compiler-plugin` / `YamlDataCompilerPlugin` / jar 0.8.0 |
| 36 | `find compiler-plugin -name '*.java'` | 5 classes + `module-info.java` |
| 37 | `YamlDataDiagnosticCodes.java:31–32` | `YAML_ERROR_201` duplicate field, `YAML_ERROR_202` unsupported type, both ERROR |
| 38 | `Constants.java:32–37` | plugin keys off `parseString`/`parseBytes`/`parseStream`, `Name`, `ballerina`, `data.yaml` |
| 39 | `YamlDataTypeValidator.java:170–321` | validates expected types at parse-call sites; resolves `Name` annotation for duplicate detection |
| 40 | `python3 -c` on `bala/package.json` | `export: ["data.yaml"]`, `graalvmCompatible: true`, `template: false` |
| 41 | Central API `packages/ballerina/data.yaml/0.8.0` | `deprecated: null`, 1 module, keywords `["yaml"]`, pullCount 27 |
| 42 | `file -b` on both renders | UTF-8 on both |
| 43 | `grep -c '⇒'` | 4 on both; `grep -cE 'Ã\|â€'` = 0 on both |
| 44 | `OLD_AND_NEW_DIFFS/data.yaml_diff.md` | its claims (191/198 lines, +8/−1, 2 hunks, 1→0 Unknown, 4→5 sections, 2 declarations added) all independently reproduced above |

## 10. Caveats and unverified items

1. **Compilability of the renders was not tested by a Ballerina compiler.** The claim in §5.3 that
   `anydata t = anydata` + `returns t|Error` is not valid Ballerina is from reading the language
   rules for dependently-typed functions, not from running `bal build` on the render. It applies
   equally to both sides, so it does not affect the verdict either way.
2. **The Java compiler-plugin jar in the bala was not decompiled.** §7 is based on the plugin source
   at tag `v0.8.0` plus `compiler-plugin.json` from the bala. The jar is named
   `data.yaml-compiler-plugin-0.8.0.jar`, matching the tag, so source and shipped jar are assumed to
   correspond; that assumption was not byte-verified.
3. **Extractor behaviour was inferred from the two JSONs, not from reading the `ballerina-vscode`
   Java/TypeScript source.** Attributions such as "defaults are dropped upstream of the renderer"
   rest on the JSON containing no `default` key for record fields on either side, which is direct
   evidence of where the loss occurs but not a reading of the extractor code.
4. Everything else in this report was verified by a command whose output is recorded in §9.

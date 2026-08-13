# ballerina/edi 1.6.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/edi` |
| Pinned version | `1.6.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-edi |
| Tag reviewed | `v1.6.0` (commit `1e25cc7`, "[Gradle Release Plugin] - pre tag commit: 'v1.6.0'") |
| Bala inspected | `/private/tmp/claude-501/-Users-admin-Desktop-Copilot-Changes-Check-contents-test-bal-copilot-library-get-mds/19909936-2e4b-46de-9886-3075396fe81e/scratchpad/extrabala/edi/1.6.0` (fetched from Central) |
| Old render | `597` lines |
| New render | `604` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The render diff is small and entirely explained by two known spec-v2 behaviours, both improvements:

1. The four public error types (`Error`, `InvalidEnvelopeError`, `SchemaCompatibilityError`, `SerializationError`) were emitted in `old` as bare `// Unknown type: <Name>` placeholders; `new` emits real type definitions with their doc comments.
2. Version/module-qualified type references (`ballerina/edi:1.6.0:EdiSegSchema`, …) are gone in `new` (4 occurrences on 2 lines → 0), so `map<EdiSegSchema>` and `type EdiUnitSchema EdiSegSchema|EdiSegGroupSchema|EdiUnitRef;` are now valid Ballerina.

Nothing was removed, truncated, or made less accurate. Every other byte of the two renders is byte-identical (unified diff = 2 hunks, +14/−7). Function set (12), README (10,109 chars, identical to the bala `docs/README.md`), and 29 of 33 type definitions are unchanged between sides.

## 2. Change inventory

Line counts: `old` 597, `new` 604 (`wc -l`). Diff: 2 hunks, 14 lines added, 7 removed (`diff -u`).

JSON-level comparison (`old/ballerina_edi.json` vs `new/ballerina_edi.json`):

| key | old | new |
|---|---|---|
| `typeDefs` | 33 | 33 |
| `functions` | 12 | 12 |
| `clients` | 0 | 0 |
| `services` | 0 | 0 |
| `annotations` | 0 | 0 |
| `readme` | 10109 chars | 10109 chars (identical) |
| `description` | "" | "" |

`o['functions'] == n['functions']` → `True`. Only 6 of 33 `typeDefs` differ:

| typeDef | change |
|---|---|
| `EdiUnitSchema` | union member names de-qualified (`ballerina/edi:1.6.0:EdiSegSchema` → `EdiSegSchema`, ×3) |
| `EdiSchema` | field `segmentDefinitions` type `map<ballerina/edi:1.6.0:EdiSegSchema>` → `map<EdiSegSchema>` (only differing field of 10) |
| `Error`, `InvalidEnvelopeError`, `SchemaCompatibilityError`, `SerializationError` | gained `"baseType": "error"`; descriptions unchanged |

Rendered declarations, by kind:

| kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 | −4 |
| `type` (incl. error types) | 24 | 28 | +4 |
| `enum` | 1 | 1 | 0 |
| `const` | 4 | 4 | 0 |
| `function` | 12 | 12 | 0 |
| section markers (`// --- `) | 4 | 4 | 0 |
| version-qualified refs (`ballerina/edi:1.6.0:`) | 4 occurrences / 2 lines | 0 | −4 |

Declarations added: `type Error`, `type InvalidEnvelopeError`, `type SchemaCompatibilityError`, `type SerializationError`. Declarations removed: none.

## 3. Correctness against library source

Bala `modules/edi/*.bal` is byte-identical to the upstream `v1.6.0` `ballerina/` directory (`diff -rq work/edi/src/ballerina <bala>/modules/edi` reports only extra non-`.bal` files: `Ballerina.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png`, `tests/`, `.gitignore`, `.devcontainer.json`, `build.gradle` — no differing common file). So GitHub and bala agree.

Public API in the bala default module (`grep -E '^public (isolated )?(function|type|class|enum|const|annotation|listener)'`): 12 functions, 28 types, 1 enum = 41 symbols. Render carries 12 functions + 33 typeDefs (28 types + 1 enum + 4 enum-member constants). Full match.

Newly added error types verified against `modules/edi/edi_translator.bal`:

| render (new) | source |
|---|---|
| `type Error error;` (L315) | `edi_translator.bal:272` `public type Error distinct error;` |
| `type InvalidEnvelopeError error;` (L319) | `edi_translator.bal:276` `public type InvalidEnvelopeError distinct Error;` |
| `type SchemaCompatibilityError error;` (L323) | `edi_translator.bal:280` `public type SchemaCompatibilityError distinct Error;` |
| `type SerializationError error;` (L327) | `edi_translator.bal:284` `public type SerializationError distinct Error;` |

Names and doc comments are exact; the `distinct` / base-type detail is discussed in §5.

`type EdiUnitSchema EdiSegSchema|EdiSegGroupSchema|EdiUnitRef;` (new L312) matches `schema_types.bal:88` `public type EdiUnitSchema EdiSegSchema|EdiSegGroupSchema|EdiUnitRef;` exactly. `map<EdiSegSchema> segmentDefinitions` (new L216) matches `schema_types.bal:62` `map<EdiSegSchema> segmentDefinitions = {};`.

Spot-checks of unchanged material (all field-for-field correct, in source order, with per-field docs lifted from the `# +` doc tags):

- `X12ISA` (new L332–358) vs `envelope_types.bal:32–47` — 13 fields, all present, all `string`, correct names/order.
- `X12GS` (new L364–381) vs `envelope_types.bal:57–66` — 7 fields.
- `X12Headers` (new L384–389) vs `envelope_types.bal:71–75` — `isa` required, `gs?` optional. Correct.
- `EdifactUNB` / `EdifactMessageIdentifier` / `EdifactUNH` / `EdifactHeaders` (new L425–470) vs `envelope_types.bal:111–151` — exact.
- `EdiInterchange` / `EdiFunctionalGroup` / `EdiTransaction` (new L477–513) vs `envelope_types.bal:158–189` — exact, including `json|error body`.
- `EdiSchema` (new L185–218) vs `schema_types.bal:42–64` — all 10 fields present, including the inline `delimiters` anonymous closed record with all 6 sub-fields.
- All 12 function signatures (new L524–604) match the source one-for-one, e.g. `interchangeFromEdiString(string ediText, EdiSchema schema) returns EdiInterchange|Error` vs `envelope_parser.bal:302`; `getDataType(string typeString) returns EdiDataType` vs `utils.bal:199` (undocumented in source, correctly rendered with no doc). No function in the source has default parameter values, so nothing is lost there.
- README in the render is character-identical to `<bala>/docs/README.md` (`r.strip() == f.strip()` → `True`).
- Em-dash / non-ASCII characters in the docs (`ISA01 — Authorization…`) survive intact in both renders; no mojibake.

## 4. Regressions

**None found.**

What was checked to reach that conclusion: the full unified diff of the two renders (only 2 hunks, both additive/de-qualifying); a key-by-key JSON comparison showing `functions`, `clients`, `services`, `annotations`, `readme`, `description` all identical and only 6 `typeDefs` differing, each in a strictly-more-accurate direction; declaration-set extraction on both files showing 0 removed declarations and identical counts for functions, enums, consts and section markers; and the `// Unknown type:` count dropping 4 → 0 with no new placeholder of any kind appearing.

## 5. Issues in `new` (independent of `old`)

Six inaccuracies exist in `new`. One is new-only (an artefact of spec v2 now emitting these types at all); five are shared verbatim with `old` and are therefore not regressions.

1. **(new-only) `distinct` and the error hierarchy are flattened.** Source declares `Error` as `distinct error` and the other three as `distinct Error`. The render emits all four as plain `type X error;` and the JSON records `"baseType": "error"` for all four. A consumer cannot tell that `InvalidEnvelopeError`/`SchemaCompatibilityError`/`SerializationError` are subtypes of `Error`, nor that these are distinct types (so `error` narrowing / `is` checks documented in the README are not derivable from the render). `old` said nothing at all here, so this is still a net improvement, not a regression.
2. **(shared) Enum members lose their string values.** Source: `public enum EdiDataType { STRING = "string", INT = "int", FLOAT = "float", COMPOSITE = "composite" }` (`edi_types.bal:17`). Both renders emit `enum EdiDataType { COMPOSITE, FLOAT, INT, STRING }` — values dropped and members alphabetised rather than source order. The values do survive separately as `const string STRING = "string";` etc. (render L174–181).
3. **(shared) Those four constants collide with the enum member names.** `const string STRING = "string";` plus `enum EdiDataType { … STRING }` in one namespace would not compile as written. Harmless as documentation, but it is not valid Ballerina.
4. **(shared) Record field defaults are dropped and defaulted fields are re-typed as optional.** E.g. `string tag = "Root_mapping"` → `string tag?`; `boolean truncatable = true` → `boolean truncatable?`; `EdiDataType dataType = STRING` → `EdiDataType dataType?`; `int maxOccurances = 1` → `int maxOccurances?`. Affects `EdiSchema`, `EdiSegSchema`, `EdiSegGroupSchema`, `EdiUnitRef`, `EdiFieldSchema`, `Range`, `EdiComponentSchema`, `EdiSubcomponentSchema`. An LLM writing schema literals from this render cannot know the defaults (notably `Range` defaults `min = 0`, `max = -1`).
5. **(shared) Closed records are rendered open.** Every `record {| … |}` in the source becomes `record { … }` in the render, except the inline `delimiters` record which keeps `{| … |}` (render L194). Since the module rejects unknown schema keys via closed records, this understates strictness.
6. **(shared) Multi-line doc comments lose the `#` prefix on continuation lines.** 8 lines in each render (new L196–197, 201–205, 212) sit inside a record body as bare prose, e.g. `For example, if it is necessary to process X12 transaction sets only, …`. The render is therefore not parseable Ballerina at those points. Identical count in `old` (`awk` count: 8 vs 8).

Also dropped on both sides (cosmetic, listed for completeness, not counted above): `public` and `isolated` qualifiers on all functions and types.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module (`<bala>/modules/edi`, matching `package.json` `"export": ["edi"]` and Central's module list of one), so the `pkg.getDefaultModule()`-only extraction loses nothing here — there is no submodule API. All 41 public symbols of that module appear in both renders (12 functions + 28 types + 1 enum, plus the 4 enum-member constants surfaced as consts = the 33 `typeDefs`). The library exports no clients, services, listeners, classes or annotations (`grep -rn 'public annotation\|client class\|public class\|listener' <bala>/modules/edi/*.bal` → no matches), consistent with `clients`/`services`/`annotations` all being empty arrays in both JSONs.

## 7. Compiler plugin

`has_plugin: false`, confirmed: the bala root contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — there is no `compiler-plugin/` directory and no `compiler-plugin.json`. The upstream `v1.6.0` checkout likewise has no `compiler-plugin` / `*-compiler-plugin` directory. Nothing plugin-derived is expected in, or missing from, the render.

Related but out of scope: the module's companion tooling is the external `edi-tools` CLI (`bal tool pull edi`, `bal edi codegen`), documented in the README and therefore already present in the render's README section. It is a separate distribution, not a compiler plugin of this package.

## 8. Other considerations

- **Version is stable and current.** Central reports `ballerina/edi` `1.6.0`, `deprecated: None`, empty `deprecateMessage`, built with `ballerinaVersion 2201.12.0`, `pullCount 4`, `createdDate 1785766417000` — a recently published release, which explains why the bala was not in the local caches and had to be fetched from Central.
- **Size/token impact is negligible**: +7 lines (+1.2%), and the 4 added type definitions replace 4 placeholder lines with real, doc-carrying declarations — a strictly better information-per-token ratio.
- **Doc quality is high.** Nearly every public type carries `# +` field docs that the renderer propagates per-field; the README (10.1 KB) contains a full quickstart plus a function-overview table, and is reproduced verbatim.
- **The `edi` module is not a dependency-magnet** like `sql`/`io`; its error types are consumed within its own API surface, so the flattened error hierarchy (§5.1) mostly affects users writing `on fail` / `is` narrowing against `edi:InvalidEnvelopeError`.
- Both renders were produced from the same 1.6.0 bala; no version drift observed anywhere (`ballerina/edi:1.6.0:` qualifiers in `old` confirm the same pinned version was consumed on that side).

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ballerina_edi.bal.txt new/ballerina_edi.bal.txt` | 597 / 604 |
| 2 | `diff -u old/... new/...` | 2 hunks, +14/−7; content as quoted in §1/§2 |
| 3 | `grep -c '^// Unknown type:'` old / new | 4 / 0 |
| 4 | `grep -c 'ballerina/edi:1.6.0:'` old / new | 2 lines / 0 (4 occurrences) |
| 5 | `grep -c '^type \|^enum \|^const '` old / new | 29 / 33 |
| 6 | `grep -c '^function '` old / new | 12 / 12 |
| 7 | `grep -n '^// --- '` new | L6 README, L170 END README, L172 Types, L515 Functions (4 markers, same in old) |
| 8 | Python key-by-key JSON compare | typeDefs 33/33, functions 12/12, clients 0/0, services 0/0, annotations 0/0, readme identical (10109), description identical |
| 9 | `o['functions'] == n['functions']` | `True` |
| 10 | typeDef set diff | `only old: set()`, `only new: set()`; 6 changed (listed §2) |
| 11 | `EdiSchema` field-level diff | exactly 1 field differs: `segmentDefinitions` type de-qualified |
| 12 | `git clone --depth 1 --branch v1.6.0 …` | succeeded; `git describe --tags` → `v1.6.0`; HEAD `1e25cc7` |
| 13 | `diff -rq work/edi/src/ballerina <bala>/modules/edi` | no differing common files; only extra non-source files upstream |
| 14 | `grep -rE '^public (isolated )?(function\|type\|class\|enum\|const\|annotation\|listener)' <bala>/modules/edi/*.bal` | 12 functions, 28 types, 1 enum |
| 15 | `<bala>/modules/edi/edi_translator.bal:272,276,280,284` | `public type Error distinct error;` and three `distinct Error` subtypes |
| 16 | `<bala>/modules/edi/edi_types.bal:17` | `public enum EdiDataType { STRING = "string", INT = "int", FLOAT = "float", COMPOSITE = "composite" }` |
| 17 | `<bala>/modules/edi/schema_types.bal:42–145` vs new L185–312 | all fields present; defaults dropped, `{\|…\|}` → `{…}` |
| 18 | `<bala>/modules/edi/envelope_types.bal:32–189` vs new L332–513 | 13 record types field-for-field identical in name/type/order |
| 19 | `<bala>/modules/edi/utils.bal:199` | `public function getDataType(string typeString) returns EdiDataType` — matches new L604 |
| 20 | README compare (render JSON vs `<bala>/docs/README.md`) | `equal: True`, both 10109 chars |
| 21 | `ls -R <bala>/modules` | single module `edi`, 16 `.bal` files |
| 22 | `ls <bala>` | no `compiler-plugin/` (bala root: bala.json, dependency-graph.json, docs, modules, package.json) |
| 23 | `cat <bala>/package.json` | `"export": ["edi"]`, `ballerina_version 2201.12.0`, `graalvmCompatible true`, `template false` |
| 24 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/edi/1.6.0` | 1 module, `deprecated: None`, pullCount 4 |
| 25 | `awk` count of doc-continuation lines lacking `#` inside type bodies | old 8, new 8 (new: L196,197,201,202,203,204,205,212) |
| 26 | `OLD_AND_NEW_DIFFS/edi_diff.md` cross-check | all its figures (597/604, +14/−7, 2 hunks, 4→0 placeholders, 4 added type decls, 0 removed) reproduced independently and confirmed |

## 10. Caveats and unverified items

- Neither render was compiled; "not valid Ballerina" claims in §5 (items 3 and 6) are from reading the emitted text against the language rules, not from a `bal build`. This does not affect the regression verdict, since the identical text is present in `old`.
- The `"baseType": "error"` value in the new JSON is reported as the extractor emitted it; I did not read the spec-v2 extractor source to confirm whether a `distinct` flag or a `Error` base is available and simply unused, versus not modelled at all. The observable outcome (render says `type InvalidEnvelopeError error;`) is verified.
- The `edi-tools` CLI referenced by the README is a separate distribution and was not inspected; nothing in the render depends on it.
- Diff hunk line numbers cited for `old` come from the unified diff; individual `old` line references beyond that were not needed because the two files are identical outside the two hunks.

# ballerina/serdes 0.2.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/serdes` |
| Pinned version | `0.2.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-serdes |
| Tag reviewed | `v0.2.0` (commit `3e7a4830355fdb38e583c1881ee03f0d24bcbf46`) |
| Bala inspected | `/private/tmp/claude-501/.../scratchpad/extrabala/serdes/0.2.0` (fetched from Central) |
| Old render | `132` lines |
| New render | `149` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`serdes` is a tiny 4-file standard-library module with exactly four public symbols in its single
(default) module: the `Schema` object type, the `Error` type, the `Proto3Schema` class, and the
`generateSchema` function. `old` degraded two of those four to bare `// Unknown type:` placeholders
(`Error`, `Proto3Schema`) and rendered `class Schema` with an empty body, so 3 of 4 public symbols
carried no usable API information. `new` emits real definitions for all of them: `type Error error;`,
a populated `class Proto3Schema` with `init`/`serialize`/`deserialize`, and the two `Schema` methods.
Nothing present in `old` was dropped, truncated or made less accurate. Residual inaccuracies remain
in `new` (`typedesc<anydata>` flattened to `anydata`, a fabricated `= anydata` default, `distinct`
dropped from `Error`), but every one of them is either inherited from the extractor JSON that `old`
also carried, or affects only lines `old` did not render at all.

## 2. Change inventory

Line counts (`wc -l`): old `132`, new `149` (+17 net). Single diff hunk, in the `Types` section
(old 121–132 → new 121–149); README (lines 1–118) and the `Functions` section are byte-identical.

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 2 (`Error`, `Proto3Schema`) | 0 | −2 |
| Top-level type declarations rendered with a body | 1 (`class Schema`, empty `{}`) | 3 (`class Schema` +2 methods, `type Error`, `class Proto3Schema` +3 methods) | +2 |
| Object/class member declarations | 0 | 5 | +5 |
| Top-level functions | 1 (`generateSchema`) | 1 (identical text) | 0 |
| Declarations removed | — | — | 0 |
| Version-qualified type refs in render (`org/mod:x.y.z:Type`) | 0 | 0 | 0 |
| Section markers `// --- ` | 4 | 4 | 0 |

Declaration lines added in `new` (7):
`Schema.serialize`, `Schema.deserialize`, `type Error error;`, `class Proto3Schema`,
`Proto3Schema.init`, `Proto3Schema.serialize`, `Proto3Schema.deserialize`.
Declarations removed: **none**.

JSON-level change (both sides have the same 3 `typeDefs` + 1 function):
- `Schema` typeDef gained a `functions` array in `new` (absent in `old`).
- `Error` typeDef gained `"baseType": "error"` in `new`.
- `Proto3Schema` typeDef gained `"type": "Class"` in `new` — this is why `old`'s renderer
  (`renderTypeDef`, which switches on `type`) fell through to `// Unknown type: Proto3Schema`
  even though `old`'s JSON already carried all three method signatures.
- `Proto3Schema.init` return type: `old` JSON `"ballerina/serdes:0.2.0:Error?"` → `new` JSON
  `"Error?"`. The version-qualified form never reached `old`'s render only because the whole
  type was degraded; spec v2 fixes it at the source.

## 3. Correctness against library source

Upstream clone at tag `v0.2.0` and the bala `modules/serdes/*.bal` are **byte-identical**
(`diff -q` clean for all four files: `init.bal`, `proto3_serdes.bal`, `serdes.bal`,
`serdes_errors.bal`), so source citations below are unambiguous.

| Render line (`new`) | Library source | Verdict |
|---|---|---|
| `class Schema { ... }` L123 | `serdes.bal:18` `public type Schema object {` | name/doc correct; kind mislabelled (see §5.4) |
| `function serialize(anydata data) returns byte[]\|Error;` L125 | `serdes.bal:20` `public isolated function serialize(anydata data) returns byte[]\|Error;` | params & return exact; qualifiers dropped |
| `function deserialize(byte[] encodedMessage, anydata T = <>) returns T\|Error;` L127 | `serdes.bal:21` `... deserialize(byte[] encodedMessage, typedesc<anydata> T = <>) returns T\|Error;` | `typedesc<anydata>` → `anydata` (§5.1); default `<>` correct |
| `type Error error;` L131 | `serdes_errors.bal:18` `public type Error distinct error;` | base type correct; `distinct` dropped (§5.3) |
| `class Proto3Schema` L135 | `proto3_serdes.bal:19` `public class Proto3Schema {` | correct kind |
| `function init(anydata ballerinaDataType) returns Error?;` L136 | `proto3_serdes.bal:27` `public isolated function init(typedesc<anydata> ballerinaDataType) returns Error?` | return exact; param type flattened |
| `function serialize(anydata data) returns byte[]\|Error;` L140 | `proto3_serdes.bal:36` | exact (modulo `public isolated`) |
| `function deserialize(byte[] encodedMessage, anydata T = anydata) returns T\|Error;` L144 | `proto3_serdes.bal:47` `... typedesc<anydata> T = <>` | param type flattened **and** default fabricated (§5.2) |
| `function generateSchema(Schema serdes, anydata T) returns Error\|();` L149 (identical in `old`) | `proto3_serdes.bal:63` `public isolated function generateSchema(Schema serdes, typedesc<anydata> T) returns Error?` | `Error\|()` ≡ `Error?`, correct; `T` flattened (same in `old`) |

Docs: every doc string rendered in `new` matches the source doc's first line verbatim
(`serdes.bal:17`, `serdes_errors.bal:17`, `proto3_serdes.bal:23/32/42`). README block is the
package `Package.md` + module `Module.md` concatenation and is identical on both sides
(`readme` field equal in both JSONs).

## 4. Regressions

**None found.**

Checked, with the result stated:
- Declaration set: `new` is a strict superset of `old` — 0 removals (diff shows only `+` lines
  plus the 2 `// Unknown type:` placeholder lines replaced by real definitions).
- README/section content: lines 1–118 and the `// --- Functions ---` block are byte-identical
  (`diff` hunk is confined to 121–149); `readme` and `description` JSON fields compare equal.
- `generateSchema` signature: character-for-character identical in both renders and both JSONs.
- `class Schema` doc comment retained in `new`.
- No type reference in `new` is less specific than in `old`; the one difference
  (`ballerina/serdes:0.2.0:Error?` → `Error?`) is a JSON-level improvement and never appeared in
  `old`'s rendered text.
- No malformed syntax was introduced in a place `old` rendered correctly (the one non-compiling
  construct, `anydata T = anydata`, sits on a line `old` did not emit at all — see §5.2).

## 5. Issues in `new` (independent of `old`)

1. **`typedesc<anydata>` flattened to `anydata`** — 4 occurrences (`Schema.deserialize` T,
   `Proto3Schema.init` ballerinaDataType, `Proto3Schema.deserialize` T, `generateSchema` T).
   Originates in the extractor: both `old` and `new` JSONs carry `"type": {"name": "anydata"}`.
   Materially misleading for this library, whose entire API is typedesc-driven — an LLM reading
   the render would write `check new (studentValue)` instead of `check new (Student)`.
   Only the 4th occurrence was visible in `old`; the other three are newly visible in `new`.
2. **Fabricated default `anydata T = anydata`** (`new` L144). Source is `typedesc<anydata> T = <>`
   (inferred-typedesc default, `proto3_serdes.bal:47`). Both JSONs contain `"default": "anydata"`
   for this parameter, so the renderer is faithful to bad input. Non-compiling as written, and
   inconsistent with `Schema.deserialize` on L127 which correctly renders `= <>` from the same
   language construct.
3. **`distinct` dropped from `Error`** — `type Error error;` vs `public type Error distinct error;`
   (`serdes_errors.bal:18`). JSON has `"baseType": "error"` with no distinctness flag. Low impact
   for callers, but the rendered form would not reproduce the library's error subtyping.
4. **`Schema` rendered as `class`** though it is an object *type* (`public type Schema object`,
   `serdes.bal:18`). Same in `old`; extractor tags it `"type": "Class"`. A user cannot implement
   the "class" as written; `Proto3Schema` is the real class.
5. **`*Schema` type inclusion missing** from `class Proto3Schema` (`proto3_serdes.bal:20`). The
   render therefore does not convey that `Proto3Schema` is a `Schema`, which is exactly what
   `generateSchema(Schema serdes, ...)` needs.
6. **`public` / `isolated` qualifiers dropped** on all 6 rendered functions/methods. Shared with
   `old` (`function generateSchema(...)`). Cosmetic for LLM consumption, but the render is not
   compilable as a module declaration.
7. **Parameter and return doc text dropped.** Both JSONs carry per-parameter `description`
   (e.g. "The data type of the value that needs to be serialized") and return descriptions; the
   renderer emits only the first doc line, leaving three dangling `# ` lines with trailing
   whitespace (`new` L134, L139, L143).
8. **Class doc misattribution**: `# Generates a schema for a given data type.` is printed above
   `class Proto3Schema` (L133) but in the source that doc belongs to `init` (`proto3_serdes.bal:23`);
   the class itself has no doc. Both JSONs place it on the typeDef, so this is extractor-level.

## 6. Coverage gaps vs. the library

**None.** The bala exports exactly one module (`package.json` → `"export": ["serdes"]`,
`modules/` contains only `serdes`), so there is no submodule-only API and the
`getDefaultModule()`-only extraction loses nothing here.

Public symbols in `modules/serdes/*.bal` vs. the renders:

| Symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `public type Schema object` | serdes.bal:18 | yes (empty body) | yes (2 methods) |
| `public type Error distinct error` | serdes_errors.bal:18 | placeholder only | yes |
| `public class Proto3Schema` | proto3_serdes.bal:19 | placeholder only | yes (3 methods) |
| `public isolated function generateSchema` | proto3_serdes.bal:63 | yes | yes |

Correctly omitted (non-public): `function init()` and `function setModule()` (`init.bal:19,23`),
and `isolated function generateProtoFile(string)` (`proto3_serdes.bal:56`) — none carry `public`.

## 7. Compiler plugin

The library ships **no compiler plugin**, confirmed on both sides:
`find <bala> -iname '*compiler-plugin*'` returns nothing (no `compiler-plugin/` directory, no
`compiler-plugin.json`), and the upstream tree at `v0.2.0` has no `*compiler*` directory
(`native/`, `ballerina/`, `load-tests/`, `build-config/` only). `has_plugin: false` in the manifest
is accurate. Nothing plugin-derived is therefore expected in the render, and nothing is missing.

## 8. Other considerations

- **The package is deprecated on Ballerina Central.** `GET /2.0/registry/packages/ballerina/serdes/0.2.0`
  returns `"isDeprecated": true`, `"deprecateMessage": "This library is deprecated and will no longer
  be maintained or updated."` Neither render surfaces this — no deprecation notice appears in the
  README block or anywhere else in `new`. That is the single highest-value fact about this library
  for an LLM consumer and it is absent from both sides. (Not a regression; a shared gap.)
- **Pre-1.0 / low usage**: version `0.2.0`, `pullCount` 11, built against distribution `2201.4.0`
  (much older than the 2201.13.x line used for the renders). `graalvmCompatible: "Yes"`.
- **Size/tokens**: 149 lines total, of which 113 (76%) are README — the package README and the
  module README are near-duplicates of each other and are both emitted in full. The actual API
  surface is 29 lines. Deduplicating the two README blocks would cut this render roughly in half.
- **This is not a foundational module** in the sense of the batch note — nothing in the pinned
  library list imports `ballerina/serdes`, so the `typedesc`-flattening inaccuracy does not
  propagate into other renders.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_serdes.bal.txt new/ballerina_serdes.bal.txt` | 132 / 149 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new render | 0 / 0 |
| `grep -c '^// --- '` old / new | 4 / 4 (via diff report, re-verified by reading both files in full) |
| Read both renders in full (132 + 149 lines) | single divergence region = lines 121–149 |
| `git clone --depth 1 --branch v0.2.0 …` | tag exists; HEAD `3e7a4830355fdb38e583c1881ee03f0d24bcbf46` |
| `diff ballerina/<f>.bal <bala>/modules/serdes/<f>.bal` for all 4 files | identical (`SAME init`, `SAME proto3_serdes`, `SAME serdes`, `SAME serdes_errors`) |
| `ls <bala>/modules` | `serdes` only |
| `cat <bala>/package.json` | `"export": ["serdes"]`, platform `java11`, ballerina_version `2201.4.0` |
| `find <bala> -iname '*compiler-plugin*'` | no output |
| `find <clone> -maxdepth 2 -iname '*compiler*'` | no output |
| JSON typeDef/function name sets, old vs new | both `['Schema','Error','Proto3Schema']` + `['generateSchema']` |
| JSON `readme` and `description` equality old vs new | `True` / `True` |
| JSON `Proto3Schema` old | has 3 `functions` but **no** `"type"` key → old renderer degraded it |
| JSON `Proto3Schema.init.return` old vs new | `"ballerina/serdes:0.2.0:Error?"` → `"Error?"` |
| JSON `Schema` old vs new | no `functions` → 2 `functions` |
| JSON `Error` old vs new | `{name,description,type:"Error"}` → same + `"baseType":"error"` |
| JSON `functions[0]` (`generateSchema`) old vs new | identical objects |
| `grep -n ' $' new/…bal.txt` | 3 lines (134, 139, 143) — dangling `# ` doc lines |
| `grep -nE 'distinct\|isolated\|public \|\*Schema'` both renders | no matches on either side |
| `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/serdes/0.2.0` | `isDeprecated: true`, `pullCount: 11`, 1 module, `ballerinaVersion 2201.4.0` |
| Source line citations | `serdes.bal:17-22`, `serdes_errors.bal:17-18`, `proto3_serdes.bal:19-66`, `init.bal:19-25` (all read in full) |

## 10. Caveats and unverified items

- The renders themselves were not regenerated; this audit compares the supplied `old`/`new`
  artefacts against the library source. Whether the checked-in renders were produced by the
  commits named in the brief is taken on trust (not independently reproducible here).
- The claim that `old`'s `// Unknown type:` degradation is caused by the missing `"type"` key in
  the JSON typeDef is inferred from the `old`/`new` JSON delta plus the brief's description of
  `renderTypeDef`; the `main`-branch renderer source was not read in this session.
- Central's `isDeprecated` flag is reported per-version by the API; whether every published
  `serdes` version is deprecated (i.e. the whole package retired) was not checked.
- The bala for this library was fetched from Central for this review rather than taken from the
  distribution or central cache; the digest returned by the API
  (`sha-256=06a236bf294ea9493caea6557f0dd1cbaa4b5418245a590fe60b393497ebad5f`) was not recomputed
  against the local unzip. Content equality with the tagged upstream sources was verified instead.

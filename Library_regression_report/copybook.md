# ballerinax/copybook 1.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/copybook` |
| Pinned version | `1.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-copybook |
| Tag reviewed | `v1.1.0` (commit `375bcb0b`, peeled `d42a8d7d`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/copybook/1.1.0/java21` |
| Old render | `30` lines |
| New render | `40` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`copybook` is a tiny package: one module (`copybook`), three public symbols in the default module
(`Error`, `Encoding`, `Converter` with 3 public methods). `old` degraded two of those three to
`// Unknown type:` placeholders, exposing zero information about the package's only usable API
(the `Converter` class). `new` emits real definitions for both. Nothing was removed or truncated.

The two JSONs are almost identical (3 differing lines total) — the extractor already carried the
full `Converter` model in `old`; only the `main` renderer failed to print it. `new` additionally
drops the version-qualified type ref `ballerinax/copybook:1.1.0:Error?` in favour of `Error?`.

`new` does surface three pre-existing extractor inaccuracies that `old` hid by printing nothing:
the `encoding` parameter default is rendered as `"EBCDIC"` when the library source says `ASCII`,
the `Converter` class doc is actually `init`'s doc, and `distinct` is dropped from `Error`.
These are inaccuracies newly *visible* in `new`, not regressions — `old` conveyed no information
about them at all.

## 2. Change inventory

Line counts (`wc -l`): old `30`, new `40` (+10).

Signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 2 | 0 |
| Version/module-qualified type refs in render (`:x.y.z:`) | 0 | 0 |
| `// --- ` section markers | 3 | 3 |

Declarations added in `new` (5), none removed (0):

| Kind | Name | old | new |
|---|---|---|---|
| type (error) | `Error` | `// Unknown type: Error` | `type Error error;` + doc |
| class | `Converter` | `// Unknown type: Converter` | `class Converter { … }` + doc |
| class method | `Converter.init` | absent | `function init(string schemaFilePath) returns Error?;` |
| class method | `Converter.toBytes` | absent | full signature + doc |
| class method | `Converter.fromBytes` | absent | full signature + doc |

Unchanged in both: package header, README section (3 content lines, byte-identical), `const string
ASCII`, `const string EBCDIC`, `enum Encoding { EBCDIC, ASCII }`. Both JSONs report
`clients: 0, functions: 0, services: 0, annotations: 0`.

JSON-level diff (`diff` of `python3 -m json.tool` output) is exactly 3 changes:
1. `Error` typeDef gains `"baseType": "error"` in `new`.
2. `Converter` typeDef gains `"type": "Class"` in `new` (absent in `old` — the reason `main`'s
   `renderTypeDef` fell through to `// Unknown type:`).
3. `init` return type name: `"ballerinax/copybook:1.1.0:Error?"` (old) → `"Error?"` (new).

## 3. Correctness against library source

Upstream `ballerina/types.bal` and `ballerina/convertor.bal` at tag `v1.1.0` are byte-identical to
the bala's `modules/copybook/*.bal` (`diff` → no output), so source and bala agree.

Complete public surface of the default module (`grep -rnE '^\s*public ' *.bal` in the bala):

| Symbol | Source | `new` render | Match |
|---|---|---|---|
| `public type Error distinct error;` | `types.bal:18` | `type Error error;` (L23) | partial — `distinct` dropped |
| `public enum Encoding { ASCII, EBCDIC }` | `types.bal:54–59` | `enum Encoding { EBCDIC, ASCII }` (L26–29) | members correct, order reversed |
| `public isolated class Converter` | `convertor.bal:21` | `class Converter` (L32) | yes (`isolated` dropped) |
| `init(string schemaFilePath) returns Error?` | `convertor.bal:27` | L33 | exact |
| `toBytes(record {} input, string? targetRecordName = (), Encoding encoding = ASCII) returns byte[]\|Error` | `convertor.bal:42–43` | L36 | types exact; **default wrong** |
| `fromBytes(byte[] bytes, string? targetRecordName = (), Encoding encoding = ASCII) returns map<json>\|Error` | `convertor.bal:63–64` | L39 | types exact; **default wrong** |

Notes on the "exact" claims:
- `record {}` (source) ≡ `record {|anydata...;|}` (render) — an inclusive record descriptor's
  implicit rest field is `anydata`. Semantically equivalent, correct.
- `string?` (source) rendered as `string|()` — equivalent.
- Return types `byte[]|Error` and `map<json>|Error` match `convertor.bal:43` and `:64` exactly.
- Method docs in the render match the source doc first lines verbatim (`convertor.bal:36`, `:57`).

Non-public symbols correctly absent from both renders: `Iterator` (`types.bal:20`), `ByteIterator`
(`types.bal:25`), `GroupValue`, `FieldValue`, `PrimitiveType`, `PrimitiveArrayType`, consts
`ROOT_JSON_PATH`/`ERRORS`/`DATA`, and the internal visitor classes.

## 4. Regressions

**None found.**

What I checked to conclude that:
- Diff of the two renders shows 2 lines removed, both `// Unknown type:` placeholders that carried
  no information; 12 added. No declaration, parameter, default, return type, or doc line present in
  `old` is missing from `new` (verified by reading both files in full — 30 and 40 lines).
- README section: `diff` of lines 7–12 of both files — identical; both reproduce the bala's
  `docs/Package.md` in full (3 content lines).
- Constants and `enum Encoding`: identical in both (lines 16–20 / 25–29).
- JSON diff is 3 lines, all additive or de-qualifying; no field lost from `old` JSON in `new` JSON.
- No version/module-qualified refs in either render; `new` removes the one such ref present in the
  `old` JSON.

## 5. Issues in `new` (independent of `old`)

1. **Wrong default value for `encoding` (2 occurrences, L36 and L39).** The render says
   `Encoding encoding = "EBCDIC"`; the library source says `Encoding encoding = ASCII`
   (`convertor.bal:42` and `convertor.bal:63`), and the parameter docs say "Default is ASCII"
   (`convertor.bal:40`, `:61`). Root cause is the extractor, not the renderer: **both** JSONs carry
   `"default": "\"EBCDIC\""` for this parameter, so this is a pre-existing bug that `old` merely
   never printed. It is the most misleading item in the render — an LLM copying it would silently
   change the wire encoding of the produced/consumed copybook bytes.
2. **`Converter` class doc is wrong.** The render's doc for `class Converter` (L31) is
   `# Initializes the converter with a schema.` — that is `init`'s doc (`convertor.bal:24`). The
   real class doc is `# This class represents a copybook converter that facilitates the conversion
   of ASCII data to and from JSON data.` (`convertor.bal:20`). Present in both JSONs
   (`typeDefs[Converter].description`), so again extractor-level and newly visible in `new`.
3. **`distinct` dropped from `Error`.** Source `public type Error distinct error;`
   (`types.bal:18`); render `type Error error;` (L23). The JSON has `"baseType": "error"` with no
   distinct flag. Minor — it loses the fact that `Error` is a distinct error type.
4. **Qualifiers dropped**: `public` and `isolated` on `Converter` and all three methods
   (`convertor.bal:21, 27, 42, 63`). Consistent with renderer style across libraries, but it means
   the render does not tell an LLM the class is `isolated`.

Shared with `old` (not attributable to `new`):

5. **Render is not compilable Ballerina.** `const string ASCII = "ASCII";` (L17) and
   `const string EBCDIC = "EBCDIC";` (L20) are the `Encoding` enum's members re-emitted as
   top-level constants, and `enum Encoding` (L26) redeclares the same identifiers — a duplicate
   symbol error if compiled. Identical in `old` (L17/L20/L25). It is also slightly misleading: the
   library has no standalone `ASCII`/`EBCDIC` constants of type `string`; the enum members are
   singleton-typed.
6. **Enum member order reversed** vs `types.bal:54–59` (source: `ASCII` then `EBCDIC`). No semantic
   effect in Ballerina; identical in both renders and both JSONs.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** The bala's `modules/` directory contains exactly one module, `copybook`
(`package.json` `"export": ["copybook"]`; Central metadata lists one module). Every `public`
declaration in that module — `Error`, `Encoding`, `Converter`, `Converter.init`,
`Converter.toBytes`, `Converter.fromBytes` — appears in `new`.

No submodule-only API exists, so the shared `getDefaultModule()` limitation does not apply here.

For reference, `old`'s gaps were 2 symbols + 3 methods (`Error`, `Converter` and its whole method
set) reduced to bare placeholders.

## 7. Compiler plugin

**No compiler plugin.** `find` for `*compiler-plugin*` / `CompilerPlugin*` across the cloned
`v1.1.0` tree returns nothing, and the bala has no `compiler-plugin/` directory (only `docs`,
`modules`, `platform`, `bala.json`, `dependency-graph.json`, `package.json`). Nothing plugin-implied
is therefore missing from the render.

Native side is plain JAR interop (`copybook-native-1.1.0.jar`, `copybook-commons-1.1.0.jar`,
`antlr4-runtime-4.13.1.jar`), which correctly contributes no renderable Ballerina API.

## 8. Other considerations

- **Documentation is genuinely thin upstream**, not lost by the pipeline: `ballerina/Package.md`,
  `ballerina/Module.md` and the repo `README.md` are all 3 lines. The render's README section
  reproduces 100% of `docs/Package.md`. An LLM gets no usage example for this package from either
  render — a real quality gap, but one that must be fixed upstream, not in the renderer. The
  repo does ship `examples/`, which the pipeline does not consume (by design, both sides).
- **Size/tokens**: 40 lines. Negligible. The +10 lines buy the entire usable API surface.
- **Not deprecated**; Central reports empty `deprecateMessage`, `pullCount` 33, built with
  Ballerina `2201.11.0`, `graalvmCompatible: true`.
- **Stable version** (1.1.0), no pre-1.0 caveat.
- Parameter-level doc text (e.g. "Default is ASCII", which would have contradicted the wrong
  default and could have let a reader catch it) is present in both JSONs but not emitted by either
  renderer. Emitting it would mitigate issue #1.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 30 / 40 |
| 2 | `cat -n` both renders (read in full) | contents as quoted above |
| 3 | `grep -c '^// Unknown type:'` both | old 2, new 0 |
| 4 | `grep -nE ':[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` both renders | 0 |
| 5 | `grep -n '^// --- '` new | 3 markers (README / END README / Types) |
| 6 | `diff <(json.tool old.json) <(json.tool new.json)` | 3 changes only (see §2) |
| 7 | `ls -R` bala 1.1.0 | one module `copybook`, 15 `.bal` files, no compiler-plugin dir |
| 8 | `grep -rnE '^\s*public ' *.bal` in bala module | 11 hits; public default-module API = `Error`, `Encoding`, `Converter{init,toBytes,fromBytes}` |
| 9 | `cat -n types.bal` (bala) | `types.bal:18` `public type Error distinct error;`; `:54–59` `enum Encoding { ASCII, EBCDIC }` |
| 10 | `sed -n '1,80p' convertor.bal` (bala) | `:21` `public isolated class Converter`; `:27` init; `:42` toBytes `encoding = ASCII`; `:63` fromBytes `encoding = ASCII` |
| 11 | `git ls-remote --tags` upstream | `v1.1.0` = `375bcb0b…`, peeled `d42a8d7d…` |
| 12 | `git clone --depth 1 --branch v1.1.0` | succeeded into scratch `work/copybook/src` |
| 13 | `diff src/ballerina/types.bal` and `convertor.bal` vs bala equivalents | IDENTICAL (both) |
| 14 | `find . -iname '*compiler-plugin*' -o -iname 'CompilerPlugin*'` in clone | no matches |
| 15 | `wc -l src/ballerina/Module.md src/README.md` | 3 / 3 |
| 16 | `cat` upstream + bala `Package.md` | identical, 3 content lines; matches render README section |
| 17 | `cat` bala `package.json` | `"export": ["copybook"]`, `ballerina_version 2201.11.0`, 3 platform jars |
| 18 | Central API `/2.0/registry/packages/ballerinax/copybook/1.1.0` | version 1.1.0, 1 module, `deprecateMessage` empty, pullCount 33 |
| 19 | Python inspection of `old.json` `Converter.functions` params | `toBytes`/`fromBytes` `encoding` default `"EBCDIC"` in **old** too → extractor-level, pre-existing |
| 20 | `python3 -m json.tool new.json` typeDefs[0..1] | `ASCII`/`EBCDIC` emitted as `"type": "Constant"`, `varType: string` |

## 10. Caveats and unverified items

- **Not verified:** why the extractor resolves the `encoding` default to `"EBCDIC"` instead of
  `ASCII`. I confirmed the wrong value is present in *both* JSONs and therefore predates spec v2,
  but I did not read the Java extractor source to identify the defect (it is outside this library's
  scope). The correlation with the reversed enum-member order (`EBCDIC` listed first in both JSONs)
  is suggestive but **unconfirmed**.
- **Not verified:** whether the renderer intends to drop `distinct` and `isolated` qualifiers
  globally, or whether that is specific to this shape. I only observed it in this library's render.
- **Not verified:** whether the duplicate `const` / enum-member emission (§5.5) is deliberate. It is
  identical on both sides, so it is out of scope for this regression comparison either way.
- Everything else asserted above was checked directly against the bala, the tagged upstream source,
  the two renders, or the two JSONs, as listed in §9.

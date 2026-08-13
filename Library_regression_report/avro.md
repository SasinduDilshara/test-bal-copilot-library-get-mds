# ballerina/avro 1.2.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/avro` |
| Pinned version | `1.2.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-avro |
| Tag reviewed | `v1.2.2` (commit `a2e98640ca79d327c98030fa1b8ca0cdf236f184`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/avro/1.2.2/java21` |
| Old render | `61` lines |
| New render | `90` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`avro` is a tiny module: one default module (`avro`), three `.bal` files, two public
symbols (`Error`, `Schema`). `old` degraded **both** of them to `// Unknown type:` stubs, so the
old render carried the README and literally zero API. `new` emits a real `type Error error;` and a
full `class Schema { init, toAvro, fromAvro }` with doc comments — the entire public API of the
package. Nothing present in `old` is absent from `new`; the diff is purely additive
(+31 / −2 lines, the two removed lines being the `Unknown type` stubs).

The added content is faithful to the source in every declaration name, parameter name, parameter
order and return type, with four fidelity gaps carried up from the extractor JSON (identical in
both sides' JSON, so not caused by spec v2): `distinct` is dropped from `Error`, the `Schema`
class doc is replaced by the `init` doc, `fromAvro`'s `typedesc<anydata> targetType = <>` is
rendered as `anydata targetType = anydata`, and per-parameter/return doc lines are not emitted.

## 2. Change inventory

Line counts (`wc -l`): old **61**, new **90**.

`// Unknown type:` placeholders (`grep -c '^// Unknown type:'`): old **2**, new **0**.
Section markers (`grep -c '^// --- '`): old **3**, new **3** (`README`, `END README`, `Types`) — unchanged.
Version-qualified type refs (`mod:x.y.z:Type`) in the rendered text: old **0**, new **0**.

Declarations **added** in `new` (5), none removed, none modified:

| Kind | Name | Rendered form in `new` |
|---|---|---|
| type (error) | `Error` | `type Error error;` (line 60) |
| class | `Schema` | `class Schema { … }` (lines 68–90) |
| class method (init) | `Schema.init` | `function init(string schema) returns Error?;` (line 69) |
| class method | `Schema.toAvro` | `function toAvro(anydata data) returns byte[]\|Error;` (line 79) |
| class method | `Schema.fromAvro` | `function fromAvro(byte[] data, anydata targetType = anydata) returns targetType\|Error;` (line 89) |

Declarations **removed**: none. Sections lost: none — README block (render lines 8–53) is
byte-identical between the two renders and to `docs/README.md` lines 1–46 in the bala.

Underlying JSON diff (`diff` of pretty-printed old vs new JSON) is 3 hunks only:

```
9c9,10        "type": "Error"          →  "type": "Error", "baseType": "error"
13a15                                  →  "type": "Class"      (Schema; old had no `type` key)
31c33         "ballerina/avro:1.2.2:Error?" → "Error?"          (init return)
```

Everything else in the JSON — descriptions, parameter lists, defaults, return descriptions — is
byte-identical between old and new. So spec v2's change here is: tag the error type with a
`baseType`, tag `Schema` as a `Class`, and strip the version-qualified type reference. Those three
tags are exactly what lets `renderTypeDef` stop degrading and emit real definitions.

## 3. Correctness against library source

The bala's `modules/avro/{error,init,schema}.bal` are byte-identical to the upstream `v1.2.2`
tag's `ballerina/{error,init,schema}.bal` (`diff -q`, all three "identical"), so source and bala
agree and either can be cited.

| Rendered (new) | Source | Verdict |
|---|---|---|
| `type Error error;` | `schema`/`error.bal:18` `public type Error distinct error;` | name + base kind correct; `public` and `distinct` dropped |
| `class Schema` | `schema.bal:20` `public class Schema {` | correct; `public` dropped |
| `function init(string schema) returns Error?;` | `schema.bal:30` `public isolated function init(string schema) returns Error?` | param name/type and return type **exact**; `public isolated` dropped |
| `function toAvro(anydata data) returns byte[]\|Error;` | `schema.bal:48` `public isolated function toAvro(anydata data) returns byte[]\|Error` | param and return **exact**; qualifiers dropped |
| `function fromAvro(byte[] data, anydata targetType = anydata) returns targetType\|Error;` | `schema.bal:63-64` `public isolated function fromAvro(byte[] data, typedesc<anydata> targetType = <>) returns targetType\|Error` | `data` and the return type **exact**; `targetType` type and default **wrong** (see §5.3) |
| doc comment on `toAvro` (render 71–78) | `schema.bal:38-45` | prose + fenced example reproduced verbatim; `+ data -` / `+ return -` lines absent |
| doc comment on `fromAvro` (render 81–88) | `schema.bal:52-59` | prose + example verbatim; param/return doc lines absent |
| README block (render 8–53) | bala `docs/README.md` 1–46 | identical (`diff` clean) |

Private members are correctly excluded: `generateSchema` (`schema.bal:34`, no `public`) and the
module-level `init()`/`setModule()` in `init.bal:19,23` appear in neither render nor either JSON.

## 4. Regressions

**None found.**

Checked, explicitly:
- Declaration sets: `new` is a strict superset of `old` (0 removals in the diff; `old` contained no
  declarations at all beyond the two stubs).
- README/section content: render lines 1–55 are identical in both files (the unified diff's single
  hunk starts at old line 56).
- No parameter, default, return type or doc string present in `old` is missing from `new` — `old`
  carried none of them.
- No version-qualified refs introduced (0 in both renders); the one in the old *JSON*
  (`ballerina/avro:1.2.2:Error?`) is gone in the new JSON, which is a fix, not a loss.
- Syntax: the new render is valid Ballerina apart from the `= anydata` default noted in §5.3.

## 5. Issues in `new` (independent of `old`)

Five, all inherited from the extractor JSON (each is present identically in the `old` JSON too —
`old` simply never rendered them):

1. **`distinct` dropped from `Error`.** Render line 60 `type Error error;` vs `error.bal:18`
   `public type Error distinct error;`. An LLM reading this would not know `avro:Error` is a
   distinct error type, so it may assume any `error` value is assignable to it. Root cause: the
   JSON only records `"baseType": "error"`.
2. **`Schema`'s class-level doc is wrong.** Render lines 62–67 attach *"Initializes the Avro schema
   with the given schema definition"* (the `init` doc, `schema.bal:22-27`) to the class. The real
   class doc, `schema.bal:19` *"The avro schema implementation to support Avro serialization and
   deserialization."*, appears nowhere in the render or in either JSON. The result reads oddly —
   the same doc block is printed twice in a row (class header, then `init`).
3. **`fromAvro` signature is materially wrong.** Render line 89 says
   `anydata targetType = anydata`; the source (`schema.bal:63`) is
   `typedesc<anydata> targetType = <>`. Two problems: the parameter type is a value type instead of
   a `typedesc`, and `= anydata` is not a valid default expression, so this line does not compile as
   written. An LLM would plausibly generate `schema.fromAvro(data, someValue)` instead of relying on
   the inferred-typedesc contextual default. This is the most consequential inaccuracy in the file.
   The JSON carries `"type": {"name": "anydata"}, "default": "anydata"` on both sides.
4. **Per-parameter and return doc lines are dropped.** The JSON holds
   `"The Avro schema definition as a string"`, `"A `byte` array of the serialized data or else an
   `avro:Error`"`, etc.; the renderer emits only the leading prose, so `+ param -` / `+ return -`
   documentation never reaches the output.
5. **Visibility and isolation qualifiers dropped.** `public` is absent from the type, the class and
   all three methods, and `isolated` is absent from all three methods. Renders as `class Schema` /
   `function toAvro`, which is not what a user would write. This is a renderer-wide convention
   rather than an avro-specific defect, but it is a divergence from the source.

## 6. Coverage gaps vs. the library

**Zero.**

The bala exports one module (`package.json` `"export": ["avro"]`; Central metadata lists exactly one
module, `avro`), which *is* the default module — so the known `getDefaultModule()`-only limitation
costs nothing here. Its complete public surface is:

| Symbol | Source | In `new`? | In `old`? |
|---|---|---|---|
| `public type Error distinct error` | `error.bal:18` | yes | no (stub) |
| `public class Schema` | `schema.bal:20` | yes | no (stub) |
| `Schema.init` | `schema.bal:30` | yes | no |
| `Schema.toAvro` | `schema.bal:48` | yes | no |
| `Schema.fromAvro` | `schema.bal:63` | yes | no |

There are no records, enums, constants, annotations, listeners, services, clients or module-level
public functions in this package (`clients`, `functions`, `services`, `annotations` are all `[]` in
both JSONs; `grep -n "public "` over the three source files returns exactly the five hits above).
No submodule-only API exists, so there is no shared submodule gap to report.

## 7. Compiler plugin

**None.** `has_plugin` is `false` in the manifest and this is confirmed independently: the bala root
`/…/avro/1.2.2/java21/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json`, `platform/` — no `compiler-plugin/` directory and no
`compiler-plugin/compiler-plugin.json`. The upstream clone has no `*compiler-plugin*` path either
(`find -iname '*compiler-plugin*'` returns nothing). The `native/` directory is the JNI runtime
implementation (`io.ballerina.lib.avro.Avro`), not a compiler plugin.

Consequently there is nothing plugin-implied (no generated annotations, no validated service
contract, no code actions) that should appear in the render and does not.

## 8. Other considerations

- **Version status**: `1.2.2` is a stable release, not deprecated (`deprecated: null`,
  `deprecateMessage: ""` from Central). Built with `ballerinaVersion` `2201.12.0`; pull count 1108.
- **Size/tokens**: 90 lines total, of which 49 (54%) are the README block and only 32 are API. Both
  renders are dominated by the README; the new render's extra 31 lines are a negligible token cost
  for a 100% increase in API coverage (0 → 5 declarations).
- **Doc quality**: the module docs are good — each method carries a runnable fenced example, and
  those examples survive into the render verbatim, which is the highest-value content here for an
  LLM. Note the README's own `fromAvro` example (`byte[] data = // Avro encoded message ;`) is not
  valid Ballerina; that is an upstream README defect, identical in both renders and in the bala.
- **`init()` module initializer** is intentionally non-public and correctly excluded.
- The library is `graalvmCompatible: true` and `template: false`; nothing in either flag affects the
  render.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l avro/{old,new}/ballerina_avro.bal.txt` | 61 / 90 |
| 2 | `grep -c '^// Unknown type:'` on both renders | old 2, new 0 |
| 3 | `grep -c '^// --- '` on both renders | 3 / 3 |
| 4 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` on both renders | 0 / 0 |
| 5 | Full `cat -n` of both renders (61 + 90 lines, read in entirety) | inventory in §2 |
| 6 | `diff <(python3 -m json.tool old/…json) <(python3 -m json.tool new/…json)` | 3 hunks only: `baseType: error` added, `type: Class` added, `ballerina/avro:1.2.2:Error?` → `Error?` |
| 7 | `wc -c` on both JSONs | 5895 / 5924 bytes |
| 8 | `python3` dump of new JSON keys | `clients`, `functions`, `services`, `annotations` all `[]`; `typeDefs` has 2 entries |
| 9 | `ls -R` of bala `1.2.2` | one platform dir `java21`; `modules/avro/{error,init,schema}.bal`; no `compiler-plugin/` |
| 10 | `cat` of bala `modules/avro/*.bal` | signatures cited in §3 |
| 11 | `cat` of bala `package.json` | `"export": ["avro"]`, version 1.2.2, `ballerina_version` 2201.12.0, `graalvmCompatible: true` |
| 12 | `git clone --depth 1 --branch v1.2.2 …` | success; HEAD `a2e98640ca79d327c98030fa1b8ca0cdf236f184`, tag `v1.2.2` |
| 13 | `diff -q ballerina/{error,init,schema}.bal` vs bala equivalents | all three identical |
| 14 | `grep -rn "public " src/ballerina/*.bal` | 5 hits: `Error` (error.bal:18), `Schema` (schema.bal:20), `init` (:30), `toAvro` (:48), `fromAvro` (:63) |
| 15 | `find src -iname '*compiler-plugin*'` | no matches |
| 16 | `ls -a bala/java21 \| grep -i plugin` | no matches |
| 17 | Central API `GET /2.0/registry/packages/ballerina/avro/1.2.2` | 1 module (`avro`), `deprecated: null`, pullCount 1108, ballerinaVersion 2201.12.0 |
| 18 | `diff <(sed -n '8,53p' new render) <(sed -n '1,46p' bala docs/README.md)` | identical — README passed through verbatim |
| 19 | Read `OLD_AND_NEW_DIFFS/avro_diff.md` and re-verified its 5 added declarations / 0 removed / +31 −2 against the files | all confirmed accurate |

## 10. Caveats and unverified items

- The `distinct`-dropping, wrong-`targetType`, missing-class-doc and missing-param-doc issues are
  attributed to the Java extractor / `ModelToJsonConverter` because they are byte-identical in both
  sides' JSON. I verified that from the JSON files themselves; I did **not** read the extractor
  source, so the precise code path responsible is unverified.
- I did not compile the new render as Ballerina; the claim that
  `anydata targetType = anydata` does not compile is from reading the grammar (a default must be an
  expression, and `anydata` is a type descriptor), not from running `bal build`.
- Claims about *why* spec v2 fixes the degradation (`"type": "Class"` / `"baseType": "error"`
  driving `renderTypeDef`) are inferred from the JSON delta plus the brief's description of
  `renderTypeDef`; I did not read the TypeScript renderer.
- Central's module summary/readme fields are empty strings in the API response; I used the bala's
  `docs/README.md` as the README ground truth instead.

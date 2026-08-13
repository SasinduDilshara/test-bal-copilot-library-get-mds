# ballerina/data.jsondata 1.1.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/data.jsondata` |
| Pinned version | `1.1.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-data.jsondata |
| Tag reviewed | `v1.1.4` (exact tag, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/data.jsondata/1.1.4/java21` |
| Old render | `307` lines |
| New render | `314` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Three hunks, +9/−2 lines. Both
`// Unknown type:` placeholders in `old` (`Error`, `JsonPathValue`) are replaced by real type
definitions in `new`, and `new` recovers the `Name` annotation that `old` omitted entirely
(`annotations` array was `[]` in the old JSON, one entry in the new JSON). Nothing was removed,
renamed, truncated or degraded. The README block, all 7 function entries and the 3 record/class
type defs are byte-identical between the two JSONs.

Residual inaccuracies exist in `new`, but all but two of them are inherited unchanged from `old`
(so they are pipeline-wide rendering conventions, not spec-v2 regressions). The two new-only ones
are lossy qualifiers on the newly emitted declarations: `distinct` dropped from `Error` and `const`
dropped from the `Name` annotation.

## 2. Change inventory

Full mechanical diff (verified by running `diff old new` directly — 3 hunks, matches
`OLD_AND_NEW_DIFFS/data.jsondata_diff.md`):

| # | old line | new line | Change |
|---|---|---|---|
| 1 | 226 | 226–228 | `// Unknown type: Error` → doc comment (2 lines) + `type Error error;` |
| 2 | 246 | 248 | `// Unknown type: JsonPathValue` → `type JsonPathValue json;` |
| 3 | — | 310–314 | New `// --- Annotations ---` section + doc + `public annotation NameConfig Name on record field;` |

Declarations by kind:

| Kind | old | new | Delta |
|---|---|---|---|
| `type` (rendered definitions) | 2 (`Options`, `NameConfig`) | 4 (`Options`, `NameConfig`, `Error`, `JsonPathValue`) | +2 |
| `class` | 1 (`JsonPathRawTemplate`) | 1 | 0 |
| `function` | 7 | 7 | 0 |
| `annotation` | 0 | 1 (`Name`) | +1 |
| `client` / `service` / `listener` / `enum` / `const` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 2 | 0 | −2 |
| `// --- ` section markers | 4 | 5 | +1 (`Annotations`) |

JSON-level (both files parsed with Python, arrays compared):
`typeDefs` 5 → 5 (same names, same order; `Error` and `JsonPathValue` each gained a `baseType`
field: `"error"` and `"json"`), `functions` 7 → 7 and **byte-equal**, `readme` **byte-equal**,
`clients` 0 → 0, `services` 0 → 0, `annotations` **0 → 1**. JSON size 16,334 → 16,749 bytes.

Removed declarations: **none**.

## 3. Correctness against library source

Bala module sources are byte-identical to the `v1.1.4` tag (`diff -q` on all five `.bal` files:
`errors.bal`, `init.bal`, `json_api.bal`, `read.bal`, `utils.bal` — no differences). Verifying the
three things `new` adds:

| New render | Library source | Verdict |
|---|---|---|
| `type Error error;` (l.228) + doc | `errors.bal:19` `public type Error distinct error;`, doc l.17–18 | Base type and doc correct; `distinct` and `public` lost |
| `type JsonPathValue json;` (l.248) | `read.bal:20` `public type JsonPathValue json;` | Correct (`public` lost, consistent with renderer convention) |
| `public annotation NameConfig Name on record field;` (l.314) + doc | `json_api.bal:93` `public const annotation NameConfig Name on record field;`, doc l.92 | Attachment point, type constraint and doc correct; `const` lost |

The new JSON's annotation entry is well-formed: `attachmentPoint: "RECORD_FIELD"`,
`typeConstraint.name: "NameConfig"` with an internal link to the `NameConfig` record that is itself
rendered at l.243–246. The cross-reference resolves inside the render.

The 7 functions (unchanged from `old`) were checked against `json_api.bal:24,33,42,51,58,66` and
`read.bal:37`: names, parameter names/order, `int indentation = 4`, `Options options = {}`,
`stream<byte[], error?>` and the `t|Error` / `json|Error` return unions all match. Doc strings match
verbatim. README block (render l.8–221) matches `docs/README.md` (213 lines) exactly apart from one
trailing blank line.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff old new` returns exactly the 3 hunks above; all are pure additions or placeholder→definition
  replacements. Nothing is deleted except the two `// Unknown type:` comment lines.
- `functions` array in the two JSONs compares `True` for equality — no parameter, default, return
  type or doc was dropped from any function.
- `readme` field compares `True` — no README content lost.
- `typeDefs` name list is identical and in the same order; `Options` and `NameConfig` field lists are
  unchanged (they appear in no diff hunk).
- No malformed syntax introduced: `type Error error;`, `type JsonPathValue json;` and
  `public annotation NameConfig Name on record field;` are all valid Ballerina declarations.
- No version/module-qualified refs (`mod:1.2.3:Type`) in either file (0 in both, per the diff
  signals table, re-confirmed by inspection of the full 314-line new render).

## 5. Issues in `new` (independent of `old`)

Six inaccuracies vs. the library source. Only (1) and (2) are new-only; (3)–(6) are identical in
`old` and are therefore pre-existing renderer behaviour, not spec-v2 effects.

1. **`distinct` lost on `Error`** (new-only). Render l.228 `type Error error;`; source
   `errors.bal:19` `public type Error distinct error;`. The new JSON carries `baseType: "error"`,
   so the distinctness is dropped at extraction, not rendering. Impact is low for consumers (they
   `check`/match on `jsondata:Error` either way) but an LLM told the type is a plain `error` may
   generate code that assumes assignability from any error value.
2. **`const` lost on the `Name` annotation** (new-only). Render l.314 vs. source `json_api.bal:93`
   `public const annotation NameConfig Name on record field;`. Normal `@jsondata:Name {value: "x"}`
   usage is unaffected; only const-context usage is misrepresented.
3. **`JsonPathRawTemplate` rendered as an empty class** (shared with `old`). Render l.250–251
   `class JsonPathRawTemplate { }`. Source `read.bal:22–26` is a public *object type* with
   `*obj:RawTemplate;`, `public string[] & readonly strings;` and `public JsonPathValue[] insertions;`.
   Wrong declaration kind and zero members. This is the parameter type of `read()`, so a consumer
   reading only this render cannot tell that a backtick raw-template literal is what `read` expects
   (the doc example at l.303 is the only hint). Extractor tagged it `"type": "Class"`, so spec v2's
   untagged-object handling did not apply.
4. **`Options` defaults turned into optionality** (shared). Render l.233–238 marks both fields
   `allowDataProjection?` and `enableConstraintValidation?`; source `json_api.bal:75–83` gives them
   *defaults* (`= {}` and `= true`), not optional markers. The inner record's per-field defaults
   (`nilAsOptionalField = false`, `absentAsNilableType = false`) and their doc comments are also
   dropped in the flattened inline form. An LLM cannot learn from this render that constraint
   validation is on by default.
5. **`NameConfig` rendered open** (shared). Render l.243–246 `type NameConfig record { string value; };`
   vs. source `json_api.bal:88–90` `public type NameConfig record {| string value; |};` (closed).
6. **`typedesc<anydata> t = <>` rendered as `anydata t = anydata`** (shared, affects all four
   `parse*` functions, render l.261/269/277/285). Source uses the inferred-typedesc idiom
   (`json_api.bal:24,33,42,51`). The rendered form is not valid Ballerina and actively misleads: it
   suggests passing an `anydata` value as the third argument, when the parameter is a typedesc that
   is normally inferred from the LHS (`Book book = check jsondata:parseAsType(j);`). This is the
   single most misleading line in the render — but it is identical in `old`.

## 6. Coverage gaps vs. the library

The bala has exactly one module (`modules/data.jsondata`) — confirmed by the bala listing and by
Central metadata (`modules` array has a single entry). **No submodule API exists**, so the
`getDefaultModule()`-only extraction limitation costs nothing here.

The default module declares 13 public symbols (`grep -h "^public " modules/data.jsondata/*.bal | wc -l`
→ 13): `Error`, `JsonPathValue`, `JsonPathRawTemplate`, `read`, `parseAsType`, `parseString`,
`parseBytes`, `parseStream`, `toJson`, `prettify`, `Options`, `NameConfig`, `Name`.

- Symbols absent from **both** renders: **0**.
- Symbols absent from `old` only: 1 (`Name` annotation — recovered in `new`); plus `Error` and
  `JsonPathValue` present in name only as placeholders in `old`.
- Partial coverage (both sides): `JsonPathRawTemplate`'s three members (`*obj:RawTemplate`,
  `strings`, `insertions`) appear in neither render — see §5.3. Symbol-level coverage is complete;
  member-level coverage of that one object type is not.

Module-private helpers (`init`, `setModule`, `prettifyJson*`, `readJson`, `JsonPathRawTemplateImpl`)
are correctly excluded from both renders.

## 7. Compiler plugin

`has_plugin: true`, confirmed: `compiler-plugin/compiler-plugin.json` +
`compiler-plugin/libs/data.jsondata-compiler-plugin-1.1.4.jar` in the bala.
`plugin_class: io.ballerina.lib.data.jsondata.compiler.JsondataCompilerPlugin`
(note: `plugin_id` is `constraint-compiler-plugin`, an evident copy-paste in the published package —
harmless, but it is what shipped).

Source (`compiler-plugin/src/main/java/io/ballerina/lib/data/jsondata/compiler/`, 551 lines across
5 files): `JsondataCompilerPlugin` registers a single `JsondataCodeAnalyzer`; the work is in
`JsondataTypeValidator` (389 lines). It contributes **compile-time validation only** — no code
actions, no generated artifacts, no additional annotations:

- `JSON_ERROR_202` "invalid field: duplicate field found" (ERROR) — raised when two record fields
  resolve to the same JSON key after applying `@jsondata:Name` (`JsondataTypeValidator:348`,
  name resolution at `:355–372`).
- `JSON_ERROR_203` "unsupported type: type is not supported" (ERROR) — raised for `table` and `xml`
  target types (`:223–224`) and other unsupported shapes (`:261`).

It only inspects call sites of `parseString`, `parseBytes`, `parseStream`
(`Constants.PARSE_STRING/PARSE_BYTES/PARSE_STREAM`, checked at `:203–205`).

Nothing the plugin implies is missing from the render: the only user-facing symbol it depends on,
the `Name` annotation, is now present in `new` (and was the one thing `old` lacked). The plugin's
type restrictions (no `table`, no `xml` targets) are not expressible in the render and are absent
from both sides — a shared, unavoidable gap rather than a regression.

## 8. Other considerations

- Stable 1.x release, not deprecated (`deprecated: null`, empty `deprecateMessage` from Central).
  Built for `ballerinaVersion 2201.12.0`, bala format 3.0.0, 15,293 pulls.
- Size is dominated by the README: 214 of 314 lines (68%) are README prose. The API surface itself
  renders in ~90 lines. Spec v2 adds only 7 net lines (+2.3%), so there is no token-budget concern.
- Doc quality in the render is good: every function keeps its full param/return doc, and `read()`
  keeps its fenced usage example (l.302–304).
- The `Options` and `parse*` typedesc issues (§5.4, §5.6) are the highest-value fixes for this
  library, but they belong to both pipelines and are out of scope for this regression call.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v1.1.4 <repo> <scratch>/src` | tag exists, clone OK |
| `wc -l old/*.bal.txt new/*.bal.txt` | 307 / 314 |
| `diff old/…bal.txt new/…bal.txt` | 3 hunks: 226c226,228 / 246c248 / 307a310,314 |
| `grep -c '^// Unknown type:'` on both | old 2, new 0 |
| `grep -c '^// --- '` on both | old 4, new 5 |
| Python JSON compare, all top-level keys | `name/description/readme` equal; `typeDefs` 5/5; `functions` 7/7 and equal; `clients` 0/0; `services` 0/0; `annotations` 0 → 1 |
| `wc -c` on both JSONs | 16,334 → 16,749 bytes |
| New JSON `Error` typeDef | `{"type":"Error","baseType":"error"}` — no `distinct` marker |
| New JSON `JsonPathValue` typeDef | `{"type":"Other","baseType":"json"}` |
| New JSON `annotations[0]` | `Name` / `RECORD_FIELD` / `typeConstraint NameConfig` (internal link) |
| `diff -q` bala `.bal` vs. tag `ballerina/*.bal` (5 files) | no differences |
| `grep -h '^public ' modules/data.jsondata/*.bal \| wc -l` | 13 public declarations |
| `errors.bal:19` | `public type Error distinct error;` |
| `read.bal:20` | `public type JsonPathValue json;` |
| `read.bal:22–26` | `public type JsonPathRawTemplate object { *obj:RawTemplate; public string[] & readonly strings; public JsonPathValue[] insertions; }` |
| `json_api.bal:24,33,42,51` | `typedesc<anydata> t = <>` on all four `parse*` |
| `json_api.bal:75–83` | `Options` with `allowDataProjection = {}`, `enableConstraintValidation = true` |
| `json_api.bal:88–90` | `NameConfig` is a **closed** record |
| `json_api.bal:93` | `public const annotation NameConfig Name on record field;` |
| `ls -R` bala root | one module (`data.jsondata`), 5 `.bal` files, `compiler-plugin/`, `docs/README.md` |
| `cat compiler-plugin/compiler-plugin.json` | `plugin_class` `JsondataCompilerPlugin`, `plugin_id` `constraint-compiler-plugin` |
| `wc -l compiler-plugin/**/*.java` | 551 lines / 5 files |
| `JsondataDiagnosticCodes.java:31–32` | `JSON_ERROR_202` DUPLICATE_FIELD, `JSON_ERROR_203` UNSUPPORTED_TYPE, both ERROR |
| `curl` Central `packages/ballerina/data.jsondata/1.1.4` | version 1.1.4, single module, not deprecated, `ballerinaVersion 2201.12.0` |
| `diff` render README block (l.8–221) vs. `docs/README.md` | identical except one trailing blank line |

## 10. Caveats and unverified items

- Neither render was compiled; syntactic validity of the emitted Ballerina was assessed by
  inspection only. The `anydata t = anydata` form (§5.6) is asserted invalid on language grounds,
  not by running the compiler.
- The compiler-plugin JAR in the bala was not decompiled; plugin behaviour is described from the
  `v1.1.4` Java source in the clone, which matches the JAR's version string but was not byte-verified
  against it.
- Whether `distinct` and `const` are dropped by the Java extractor or by `toSyntaxString` was
  inferred from the JSON payload (`baseType: "error"`, no distinctness/const field present), not by
  reading the extractor source — the extractor side is the likely origin but is **unverified**.
- The `plugin_id` mismatch (`constraint-compiler-plugin`) is reported as observed; no upstream issue
  was searched to confirm it is a known defect.

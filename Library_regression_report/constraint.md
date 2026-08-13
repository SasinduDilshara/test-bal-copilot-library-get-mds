# ballerina/constraint 1.7.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/constraint` |
| Pinned version | `1.7.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-constraint |
| Tag reviewed | `v1.7.0` (commit `7e6f193`, resolved via `git ls-remote --tags`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/constraint/1.7.0/java21` |
| Old render | `257` lines (10,067 bytes) |
| New render | `290` lines (11,327 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`constraint` is a tiny stdlib module: one module (the default module `constraint`), 215 lines of
`.bal` across 3 files, 11 public types, 1 public function, 6 public annotations. Because it is small
I audited it **exhaustively** — every declaration in the bala was checked against both renders.

`new` is strictly better than `old` on three axes and loses nothing:

1. The three error types (`Error`, `ValidationError`, `TypeConversionError`) degraded to
   `// Unknown type:` placeholders in `old`; `new` emits real definitions with their doc comments.
2. Four version/module-qualified, non-compiling type references
   (`ballerina/lang.string:0.0.0:RegExp`, `ballerina/constraint:1.7.0:DateOption`) are replaced with
   correct Ballerina syntax (`string:RegExp`, `DateOption`).
3. A whole new `// --- Annotations ---` section renders all 6 constraint annotations. This is the
   single most important improvement for this library: `@constraint:Int`, `@constraint:String` etc.
   **are the library's entire user-facing API surface** — `validate()` is meaningless without them.
   `old` exposed zero annotations, so an LLM reading the `old` render could not write a single
   correct usage of this module.

`diff` confirms **0 declarations removed** and **0 lines of content lost**. Verdict: IMPROVEMENT ONLY.

## 2. Change inventory

Line counts (`wc -l`): old 257, new 290 (+33). Diff: 3 hunks, 38 lines added, 5 removed.

Declaration counts by kind (grep on the two render files, README block excluded where noted):

| Kind | old | new | Δ |
|---|---|---|---|
| `const` | 4 | 4 | 0 |
| `type` | 7 | 10 | **+3** |
| `enum` | 1 | 1 | 0 |
| `function` | 1 | 1 | 0 |
| `public annotation` | 0 | 6 | **+6** |
| `// Unknown type:` placeholders | 3 | 0 | **−3** |
| `// --- section ---` markers | 4 | 5 | +1 |
| version-qualified type refs (occurrences) | 4 | 0 | **−4** |

**Added in `new` (9 declarations):**

- `type Error error;` / `type ValidationError error;` / `type TypeConversionError error;`
  (replacing the 3 `// Unknown type:` lines)
- `public annotation IntConstraints Int on type, record field;`
- `public annotation FloatConstraints Float on type, record field;`
- `public annotation NumberConstraints Number on type, record field;`
- `public annotation StringConstraints String on type, record field;`
- `public annotation ArrayConstraints Array on type, record field;`
- `public annotation DateConstraints Date on type, record field;`

**Removed in `new`: none.** (`diff -u` shows the only `-` lines are the 3 `// Unknown type:`
placeholders and the 2 version-qualified field lines, each replaced in place by a better line.)

**Modified (2 lines):**

- `StringConstraints.pattern`: `ballerina/lang.string:0.0.0:RegExp|record {|...|}` →
  `string:RegExp|record {|string:RegExp value; string message;|}`
- `DateConstraints.option`: `ballerina/constraint:1.7.0:DateOption|record {|...|}` →
  `DateOption|record {|DateOption value; string message;|}`

**JSON level:** both JSONs carry identical `typeDefs` (15), `functions` (1), `clients` (0),
`services` (0) and an identical `readme` (4,475 chars). Differences: `new` adds `"baseType":"error"`
to the 3 error typeDefs, and populates `annotations` with 12 entries (old: 0). File size 16,459 →
21,582 bytes.

## 3. Correctness against library source

The GitHub clone at `v1.7.0` and the bala are **byte-identical** for all three `.bal` files
(`diff` returned no output for `constraint.bal`, `constraint_errors.bal`, `init.bal`), so source
citations below are unambiguous. Line refs are to the bala copy under
`.../1.7.0/java21/modules/constraint/`.

**The 6 annotations added by `new` — all 6 verified exact, including doc text:**

| Render (new) | Source | Match |
|---|---|---|
| `public annotation IntConstraints Int on type, record field;` (L265) | `constraint.bal:20` | exact |
| `public annotation FloatConstraints Float on type, record field;` (L268) | `constraint.bal:23` | exact |
| `public annotation NumberConstraints Number on type, record field;` (L271) | `constraint.bal:26` | exact |
| `public annotation StringConstraints String on type, record field;` (L274) | `constraint.bal:29` | exact |
| `public annotation ArrayConstraints Array on type, record field;` (L277) | `constraint.bal:32` | exact |
| `public annotation DateConstraints Date on type, record field;` (L290) | `constraint.bal:45` | exact |

The 10-line doc comment on `Date` (including the fenced ```ballerina` block showing the `Date`
record shape) is reproduced verbatim from `constraint.bal:34-44` at render L279-289. No truncation.

**The 3 error types added by `new`:**

- Source `constraint_errors.bal:18` — `public type Error distinct error;` → render `type Error error;`
- Source `constraint_errors.bal:21` — `public type ValidationError distinct Error;` → render `type ValidationError error;`
- Source `constraint_errors.bal:24` — `public type TypeConversionError distinct Error;` → render `type TypeConversionError error;`

Names and doc comments are correct; the `distinct` qualifier and the `ValidationError <: Error`
subtype relationship are flattened (see §5.2). Still a large net gain over `// Unknown type:`.

**The 2 corrected field types:**

- `StringConstraints.pattern` source `constraint.bal:123` is `string:RegExp|record{| *ConstraintRecord; string:RegExp value; |}`.
  `new` renders `string:RegExp|record {|string:RegExp value; string message;|}` — the `*ConstraintRecord`
  inclusion is correctly expanded to `value` + `message` (`ConstraintRecord` at `constraint.bal:59-62`
  is `{| anydata value; string message; |}`), and `string:RegExp` is the correct spelling
  (`lang.string` is auto-imported as `string`). `old`'s `ballerina/lang.string:0.0.0:RegExp` is not
  valid Ballerina. **`new` is correct, `old` was not.**
- `DateConstraints.option` source `constraint.bal:154` is `DateOption|record{| *ConstraintRecord; DateOption value; |}`.
  `new` renders `DateOption|record {|DateOption value; string message;|}` — correct.
  `old`'s `ballerina/constraint:1.7.0:DateOption` is not valid Ballerina. **`new` is correct.**

**Unchanged content spot-checked and confirmed accurate in both renders:**

- `ConstraintRecord` (`constraint.bal:59-62`), `IntConstraints` 5 fields (`:71-77`),
  `FloatConstraints` 6 fields (`:87-94`), `NumberConstraints` 6 fields (`:104-111`),
  `StringConstraints` 4 fields (`:119-124`), `ArrayConstraints` 3 fields (`:131-135`),
  `DateConstraints` 2 fields (`:153-156`) — field names, optionality (`?`), base types
  (`int`/`float`/`decimal`) and per-field doc strings all match.
- `DateOption` 4 members (`:142-147`) — all present (order differs, see §5.5).
- README: the render's README block is **byte-identical** to `docs/README.md` in the bala
  (4,475 chars, verified by string comparison in Python) on both sides.

## 4. Regressions

**None found.**

What I checked to conclude that:

- `diff -u old new` in full (33 net lines, 3 hunks) — read every changed line. Every `-` line is
  replaced in place by a superset or a corrected form; no `-` line's content disappears.
- Declaration-set comparison by kind (§2 table): no kind decreased except the
  `// Unknown type:` placeholder count (3 → 0), which is the intended fix.
- The precomputed diff at `OLD_AND_NEW_DIFFS/constraint_diff.md` reports "Declarations removed (0)";
  I verified this independently against the files rather than trusting it.
- README block: identical on both sides and identical to the bala's `docs/README.md`. No doc loss.
- Doc comments on the 7 record types, the enum, and `validate` are byte-identical between `old` and
  `new` (they fall outside all 3 diff hunks).
- `validate`'s signature line is byte-identical on both sides (render L257 old / L260 new).

## 5. Issues in `new` (independent of `old`)

All five below are **shared with `old`** (identical in both JSONs / both renders) except where noted
— they are pipeline limitations, not spec-v2 regressions. Listed because they are inaccuracies a
reviewer of `new` should know about.

**5.1 `validate` signature is wrong (both sides).** Source `constraint.bal:164`:

```ballerina
public isolated function validate(anydata value, typedesc<anydata> td = <>) returns td|Error = @java:Method {...} external;
```

Both renders emit `function validate(anydata value, anydata td = anydata) returns td|Error;`.
Three defects: (a) `td`'s type is `typedesc<anydata>`, rendered as `anydata`; (b) the inferred-typedesc
default `= <>` is rendered as the literal `= anydata`, which is not valid Ballerina and is
meaningless; (c) `public` and `isolated` are dropped. Confirmed identical in both JSONs
(`"type": {"name": "anydata"}, "default": "anydata"`), so this is a pre-existing extractor gap.
Practical impact is limited because the README (present in both renders) shows the correct call
form `constraint:validate(person)`.

**5.2 `distinct` and the error hierarchy are flattened (new only, but net-positive).**
`ValidationError` and `TypeConversionError` are `distinct Error` in the source but render as
`type X error;` — an LLM cannot tell from the render that `ValidationError is Error` holds, or that
these are distinct (not structural) error types. `old` said nothing at all about these types, so
this is a partial improvement rather than a defect introduced by `new`. Root cause visible in the
JSON: `new` adds only `"baseType": "error"`, dropping the `distinct` flag and the true base.

**5.3 Closed records rendered as open (both sides).** `ConstraintRecord`, `IntConstraints`,
`FloatConstraints`, `NumberConstraints`, `StringConstraints`, `ArrayConstraints` are all declared
`record {| ... |}` (closed) in `constraint.bal`; both renders emit `record { ... }` (open). Only
`DateConstraints` is genuinely open in source (`constraint.bal:153`). Note the *inline* records
inside fields *are* correctly rendered closed (`record {|int value; string message;|}`), so the
render is internally inconsistent about closedness.

**5.4 `public` qualifier dropped on all types and the function (both sides).** `grep -E '^public (type|function|isolated)'` on the post-README region of `new` returns 0 hits, yet all 11 types and
`validate` are `public` in source. Only the 6 annotations carry `public` in the render. Cosmetic for
comprehension, but the render as a whole is not compilable Ballerina.

**5.5 `DateOption` enum: member docs dropped, order reversed, and members duplicated as consts
(both sides).** Source `constraint.bal:138-141` documents each member
(`# + PAST - validates whether the date is in the past`, etc.); neither render carries those.
Member order is reversed vs. source (render: `FUTURE_OR_PRESENT, FUTURE, PAST_OR_PRESENT, PAST`;
source: `PAST, PAST_OR_PRESENT, FUTURE, FUTURE_OR_PRESENT`). Additionally both renders emit the four
members *twice* — once as standalone `const string PAST = "PAST";` (L129-135) and again as
`enum DateOption` members (L226-231); as written these are duplicate symbol definitions in one
module and would not compile. Semantically harmless for an LLM (the values are right) but wasteful
and slightly misleading.

## 6. Coverage gaps vs. the library

**Gaps in `new`: 0.** Every public symbol exported by the default module appears in the `new` render.

The bala exports exactly one module (`package.json` `"export": ["constraint"]`; `modules/` contains
only `constraint/`; Ballerina Central metadata for 1.7.0 lists a single module). **There is no
submodule-only API for this package**, so the shared `getDefaultModule()`-only extraction limitation
noted in the brief costs nothing here.

Full public-symbol reconciliation (13 type-level + 6 annotations + 1 function):

| Symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `ConstraintRecord` | constraint.bal:59 | yes | yes |
| `IntConstraints` | :71 | yes | yes |
| `FloatConstraints` | :87 | yes | yes |
| `NumberConstraints` | :104 | yes | yes |
| `StringConstraints` | :119 | yes | yes |
| `ArrayConstraints` | :131 | yes | yes |
| `DateOption` | :142 | yes | yes |
| `DateConstraints` | :153 | yes | yes |
| `Error` | constraint_errors.bal:18 | placeholder only | yes |
| `ValidationError` | :21 | placeholder only | yes |
| `TypeConversionError` | :24 | placeholder only | yes |
| `validate()` | constraint.bal:164 | yes | yes |
| annotations `Int`/`Float`/`Number`/`String`/`Array`/`Date` | :20,23,26,29,32,45 | **no (6 gaps)** | yes |

So the gap count moves from **9 in `old`** (6 annotations entirely absent + 3 error types reduced to
contentless placeholders) to **0 in `new`**.

Non-public symbols correctly excluded from both renders: `DateRecord` (`constraint.bal:49`,
module-private, used only by the compiler plugin), `init()` and `setModule()` (`init.bal:19,23`,
both non-public).

## 7. Compiler plugin

`has_plugin: true` — confirmed present in the bala at
`java21/compiler-plugin/compiler-plugin.json`, declaring `plugin_id: constraint-compiler-plugin`,
`plugin_class: io.ballerina.stdlib.constraint.compiler.ConstraintCompilerPlugin`, backed by
`compiler-plugin/libs/constraint-compiler-plugin-1.7.0.jar`.

What it contributes (read from the `v1.7.0` clone, `compiler-plugin/src/main/java/...`):

- **Validations only — no code actions, no code generation, no modifiers.**
  `ConstraintCompilerPlugin.init()` calls only `context.addCodeAnalyzer(new ConstraintCodeAnalyzer())`.
  A `grep` for `CodeAction|CodeModifier|CodeGenerator` across the plugin sources returns **0 hits**.
- 4 compile-time diagnostics, all severity `ERROR` (`ConstraintDiagnosticCodes.java`):
  `CONSTRAINT_101` invalid annotation on type; `CONSTRAINT_102` no constraints found;
  `CONSTRAINT_103` incompatible constraints; `CONSTRAINT_104` invalid constraint value.
- `ConstraintCompatibilityMatrix.java` encodes which annotation may attach to which Ballerina type
  (`Int`→int, `Float`→float, `Number`→int|float|decimal, `String`→string, `Array`→arrays,
  `Date`→the `DateRecord` shape), plus which constraint fields may co-occur and which values are legal
  (e.g. length/digit constraints must be non-negative).

**Does anything the plugin implies fail to surface in the render?** Partly, and the same on both
sides: the annotation→target-type compatibility matrix and the "at least one constraint required"
rule are compiler-enforced but are not expressible in a Ballerina declaration, so they cannot appear
in the render as declarations. They *are* however documented in the README table (render L18-25),
which both renders carry in full — including the annotation→type mapping. So the practical loss is
nil. The plugin implies no additional public symbols; nothing generated by it is missing.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerina/constraint/1.7.0` returns
  `deprecated: null`, `deprecateMessage: ""`, pullCount 17,978. Stable 1.x version — no pre-1.0 risk.
- **Foundational-type accuracy (per the batch addendum).** The cross-package types other libraries
  depend on here are `constraint:Error` (widely referenced, e.g. by `http` and `openapi`-generated
  code) and `constraint:validate`. `Error` is now a real definition in `new` instead of a
  placeholder — a direct win for any consuming library's render fidelity. `string:RegExp`, an
  externally-owned type, is now spelled correctly in `new` (§3).
- **Size/token impact:** +33 lines / +1,260 bytes in the render (+12.5%); +5,123 bytes in the JSON
  (+31%). Very cheap for the coverage gained. Nothing here approaches a context-budget concern.
- **JSON-level redundancy in `new`:** `annotations` has **12** entries for **6** annotations — each
  is emitted once per attachment point (`"attachmentPoint": "TYPE"` and `"RECORD_FIELD"`), with
  otherwise identical payloads. The renderer collapses them correctly into 6 declarations reading
  `on type, record field`, so the *render* is clean; only the intermediate JSON pays the duplication.
  Worth flagging to the spec-v2 authors as a cheap size win, but it is not a defect in the output.
- **Neither render is compilable Ballerina** (missing `public`, duplicate const/enum symbols,
  `td = anydata`). That is by design for this format — it is an LLM-facing summary, not source.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags .../module-ballerina-constraint \| grep v1.7.0` | tag exists, `7e6f193` (peeled) |
| 2 | `git -C <clone> describe --tags` | `v1.7.0` — clone is at the pinned tag |
| 3 | `diff <clone>/ballerina/{constraint,constraint_errors,init}.bal <bala>/modules/constraint/...` | all 3 identical (no output) |
| 4 | `wc -l` on both renders | old 257, new 290 |
| 5 | `wc -c` on both renders | old 10,067, new 11,327 |
| 6 | `diff -u old new` | 3 hunks, +38 / −5 lines; read in full |
| 7 | `grep -c '^// Unknown type:'` | old 3, new 0 |
| 8 | `grep -oE 'ballerina/[a-z.]+:[0-9]...' \| wc -l` | old 4 occurrences (2 lines), new 0 |
| 9 | `grep -n '^// --- '` | old 4 markers, new 5 (adds `// --- Annotations ---` at L262) |
| 10 | `grep -c` per kind on both renders | const 4/4, type 7/10, enum 1/1, function 1/1, annotation 0/6 |
| 11 | `grep -E '^public (type\|function\|isolated)'` on new, post-README | 0 hits → `public` dropped |
| 12 | `wc -l <bala>/modules/constraint/*.bal` | 166 + 24 + 25 = 215 lines total |
| 13 | `find <bala> -maxdepth 3` + `ls <bala>/*/modules` | single module `constraint`; no submodules |
| 14 | `cat <bala>/package.json` | `"export": ["constraint"]`, `ballerina_version 2201.12.0`, graalvmCompatible |
| 15 | `cat <bala>/compiler-plugin/compiler-plugin.json` | plugin id/class/jar as quoted in §7 |
| 16 | Read `constraint.bal` L1-167 in full | 6 annotations, 7 types, 1 enum, 1 function, 1 private type |
| 17 | `cat -n constraint_errors.bal` | 3 `distinct` error types at L18/21/24 |
| 18 | `cat -n init.bal` | `init()`, `setModule()` — both non-public, correctly absent from renders |
| 19 | Python: compare `<bala>/docs/README.md` with JSON `readme` | both 4,475 chars, **identical** |
| 20 | Python: dump JSON top-level keys/lengths, both sides | typeDefs 15/15, functions 1/1, annotations 0/**12** |
| 21 | Python: dump `Error`/`ValidationError`/`TypeConversionError` typeDefs both sides | new adds `"baseType":"error"`; no `distinct` field either side |
| 22 | Python: dump `validate` function object both sides | **byte-identical**; `td` typed `anydata`, default `"anydata"` |
| 23 | Python: dump all 12 `annotations` entries in new JSON | 6 names × 2 attachmentPoints (TYPE, RECORD_FIELD) |
| 24 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/constraint/1.7.0` | 1 module, not deprecated, 17,978 pulls |
| 25 | `find <clone>/compiler-plugin -name '*.java'` | 19 sources; read plugin entrypoint, diagnostic codes, compat matrix |
| 26 | `grep -rn 'CodeAction\|CodeModifier\|CodeGenerator'` over plugin sources | **0 hits** → analyzer-only plugin |
| 27 | `grep -n '+ PAST\|+ FUTURE' constraint.bal` | 4 enum-member doc lines at L138-141, absent from both renders |
| 28 | Read `OLD_AND_NEW_DIFFS/constraint_diff.md` | claims verified against files; "removed: 0" confirmed independently |

## 10. Caveats and unverified items

- **Renders were not regenerated.** I audited the committed `old`/`new` artifacts as given; I did not
  re-run the two-stage pipeline to confirm they reproduce from the stated commits (`eb5d81b3` /
  `412ba01e`). The brief states both sides were verified `PIN_OK` at 1.7.0, and I found no contrary
  evidence (both JSONs carry identical `typeDefs`, `readme`, and `validate` payloads, consistent with
  a same-version, different-extractor pair).
- **Compiler-plugin jar not decompiled.** My §7 description comes from the `v1.7.0` GitHub sources
  under `compiler-plugin/src/main/java/`, not from the shipped
  `constraint-compiler-plugin-1.7.0.jar` in the bala. Since the three `.bal` files are byte-identical
  between clone and bala, the jar almost certainly matches those sources, but I did not verify the
  jar's bytecode.
- **`old`'s `ballerina/lang.string:0.0.0:RegExp` version string.** The `0.0.0` looks like a
  placeholder emitted by the old extractor rather than a real `lang.string` version; I did not trace
  it to the extractor code to confirm. Immaterial — the whole reference is gone in `new`.
- Everything else in this report was verified directly by the commands in §9.

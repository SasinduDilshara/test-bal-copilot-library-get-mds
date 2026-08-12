# ballerina/ai.eval 0.9.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/ai.eval` |
| Pinned version | `0.9.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-ai.eval |
| Tag reviewed | `v0.9.0` (commit `0890baf47f1d80f3aaf0e26deaba3b5ade7e618f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/ai.eval/0.9.0` |
| Old render | `470` lines |
| New render | `502` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` (+32 lines, zero deletions, zero modifications other than the
`Error` line being upgraded from a stub to a real definition). The diff contains no `-` line except
`// Unknown type: Error`.

Three improvements:
1. The single degraded type in `old` (`// Unknown type: Error`) is replaced by a real definition
   with its doc comment.
2. All 23 `@EvalTemplate` annotation attachments — the entire low-code discovery metadata of this
   package — are now rendered. `old` rendered none.
3. A new `// --- Annotations ---` section declares `EvalTemplate` itself, which `old` omitted
   entirely (the `annotations` array in `old/ballerina_ai.eval.json` is empty; in `new` it has 1 entry).

All 23 public functions, both enums, the record and the error type are present in both renders with
byte-identical signatures. No regression found.

## 2. Change inventory

Line counts: `wc -l` → old 470, new 502 (+32).

`diff -u old/ballerina_ai.eval.bal.txt new/ballerina_ai.eval.bal.txt` yields exactly:

| Change | Count | Net lines |
|---|---|---|
| `// Unknown type: Error` removed, replaced by `# <doc>` + `type Error error;` | 1 | +1 |
| `@EvalTemplate {...}` attachment lines added above functions | 23 | +23 |
| New `// --- Annotations ---` section (marker + blank lines + 4 doc lines + declaration) | 1 section | +8 |
| **Total** | | **+32** ✓ |

Declarations added / removed / modified, by kind:

| Kind | old | new | delta |
|---|---|---|---|
| Functions (top-level, declaration section) | 23 | 23 | 0 — set identical (`comm` on sorted name lists: no missing, no extra) |
| Enums | 2 (`EvalKind`, `TrajectoryMatchMode`) | 2 | 0 |
| Records | 1 (`EvalTemplateConfig`) | 1 | 0 |
| Error types | 0 real (1 `// Unknown type:` stub) | 1 real (`type Error error;`) | **+1 real** |
| `const string` (enum members re-emitted) | 6 | 6 | 0 |
| Annotation declarations | 0 | 1 (`EvalTemplate`) | **+1** |
| Annotation attachments on functions | 0 | 23 | **+23** |
| Clients / services / listeners / classes | 0 | 0 | 0 |
| README section (lines 1–177) | identical | identical | `cmp` on lines 1–177 → byte-identical |

Degraded types: `grep -c '^// Unknown type:'` → old **1**, new **0**.

JSON side (same shape, both have keys `annotations, clients, description, functions, name, readme,
services, typeDefs`): `functions` 23→23, `typeDefs` 10→10, `annotations` **0→1**, `clients` 0→0,
`services` 0→0, `readme` and `description` identical. All 23 function objects differ only by the
added `annotations` field; the `Error` typeDef differs only by the added `"baseType": "error"`.

## 3. Correctness against library source

Sources cross-checked: bala `modules/ai.eval/{annotations,error,llm_judges,rule_based}.bal` (1,586
lines) and upstream tag `v0.9.0` (`ballerina/*.bal`). `annotations.bal`, `error.bal`,
`rule_based.bal` are byte-identical between the tag and the bala; `llm_judges.bal` differs by exactly
2 lines — the bala carries a build-injected `@ai:JsonSchema{...}` on the **private** type
`JudgeVerdict` (line 26). That type is not public and appears in neither render. Everything below is
checked against the bala (authoritative).

**Signatures — exhaustive, all 23 functions.** Parsed every `public isolated function` from the bala
and every `^function ...;` from `new`, normalising `returns Error?` → `returns Error|()`. Result:
**0 mismatches** across all 23 (parameter names, types, order, and every default value —
`judgeScoreThreshold = 0.8`, `minLength = 1`, `maxLength = 10000`, `maxIterations = 5`,
`maxLatencySeconds = 10`, `matchMode = STRICT`, `caseSensitive = true/false`,
`stripWhitespace = true`, `successCriteria = ""`, `safetyContext = ""`, `toneContext = ""`,
`expectedCoverage = ""`). `old` and `new` carry identical signature lines.

**Annotation attachments — exhaustive, all 23.** Parsed the `@EvalTemplate { ... }` bodies from
`llm_judges.bal` (15) and `rule_based.bal` (8) and compared field-by-field against the 23 rendered
attachments in `new`. Result: **0 mismatches, 0 missing, 0 extra**. `label`, `description`, `kind`
and `needsEvalset` match exactly for every function. Spot-cited examples:
- `rule_based.bal:31-37` `Length Compliance / RULE_BASED / needsEvalset: false` →
  `new:413` identical.
- `rule_based.bal:76-82` `Tool Trajectory / RULE_BASED / needsEvalset: true` → `new:424` identical.
- `llm_judges.bal:151-157` `Semantic Similarity / LLM_JUDGE / needsEvalset: true` → `new:243`
  identical.
- `llm_judges.bal:884-890` `Instruction Following / LLM_JUDGE / needsEvalset: false` → `new:403`
  identical.

`kind` is rendered as a quoted string (`kind: "LLM_JUDGE"`) where source writes the enum member
(`kind: LLM_JUDGE`). `EvalKind` is a Ballerina string enum, so `"LLM_JUDGE"` is the member's value
and is type-assignable to the field. Semantically correct, syntactically legal.

**`type Error error;`** — source is `error.bal:18` `public type Error distinct error;`. Doc string
matches (`error.bal:17`). See §5 for the dropped `distinct`.

**`public annotation EvalTemplateConfig EvalTemplate on function;`** — source is `annotations.bal:43`
`public const annotation EvalTemplateConfig EvalTemplate on function;`. Type constraint, name and
attachment point (`on function`) are correct; doc text matches `annotations.bal:39-42`. See §5 for
the dropped `const`.

**`EvalTemplateConfig`** fields match `annotations.bal:27-37` (`string label`, `string description?`,
`EvalKind kind`, `boolean needsEvalset`), including the optional marker on `description`.

**Enums** `EvalKind` (`annotations.bal:18-23`) and `TrajectoryMatchMode` (`rule_based.bal:56`) carry
the right members; ordering is not preserved (see §5), identically in both renders.

## 4. Regressions

**None found.**

What was checked to conclude that:
- `diff -u old new` produces exactly one deleted line in the whole file — `// Unknown type: Error` —
  which is replaced by a superior real definition. There is no other `-` line.
- Function name sets from the declaration sections (lines 178→EOF) of `old` and `new` are identical
  (`diff` on sorted lists → identical), and both equal the 23 public functions in the bala.
- Every signature line is textually unchanged between `old` and `new` (they appear only as context
  lines in the unified diff).
- README section (lines 1–177) is byte-identical (`cmp` → no difference), so no README/example
  content was lost; the three `function agent*` definitions at new:132/148/168 are README code
  samples, not API.
- All doc comments (`#` lines) present in `old` are present unchanged in `new`; no `# + param` line
  is deleted anywhere in the diff.
- No version- or module-qualified type refs (`mod:x.y.z:Type`) exist in either render, so nothing
  was lost through that path.
- JSON: `functions` 23→23, `typeDefs` 10→10, `readme`/`description` identical; the only per-object
  deltas are additive fields.

## 5. Issues in `new` (independent of `old`)

Four fidelity issues. None affect symbol coverage; all are cosmetic-to-minor for an LLM consumer.

1. **`distinct` dropped from the error type.** `new:222` emits `type Error error;`; the library
   declares `public type Error distinct error;` (`error.bal:18`). An LLM told the type is a plain
   `error` could wrongly assume any `error` value is assignable to `ai.eval:Error`. New-only,
   because `old` had no definition at all — a smaller inaccuracy than the stub it replaces.
2. **`const` dropped from the annotation declaration.** `new:502` emits
   `public annotation EvalTemplateConfig EvalTemplate on function;`; source is
   `public const annotation ...` (`annotations.bal:43`). Without `const`, the render implies
   non-constant expressions may be used in the annotation value, which the compiler would reject.
3. **Doc-comment continuation lines lose the leading `#`** — 5 occurrences in each render, e.g.
   `new:417` `A–Z is folded, so non-ASCII letters still compare case-sensitively` and `new:217`
   `false if it runs on ad hoc user queries`. These sit inside `#` doc blocks with no `#`, so the
   render as a whole is not compilable Ballerina and the wrapped sentence reads as stray code. Count
   is identical in `old` (5) and `new` (5) — shared, not a regression. Note the new Annotations
   section does *not* have this defect (its wrapped doc lines are correctly prefixed).
4. **Closed record rendered as open.** `new:208` emits `type EvalTemplateConfig record {` where the
   library declares `record {| ... |}` (`annotations.bal:27`). Identical in `old`; shared renderer
   behaviour.

Non-issues confirmed: no encoding corruption (`grep -c 'â\|Ã'` → 0; the en dash in `A–Z` survives in
both); no invented symbols (render function set == bala public function set exactly); no wrong
types.

Cosmetic, shared with `old`, not counted above: `public` is stripped from every declaration;
enum members are re-emitted as six top-level `const string` entries in the Types section; enum member
order is reversed relative to source (`EvalKind` renders `LLM_JUDGE, RULE_BASED`;
`TrajectoryMatchMode` renders `SUPERSET, SUBSET, UNORDERED, STRICT`).

## 6. Coverage gaps vs. the library

**Zero gaps for `new`.**

The bala has exactly one module — `modules/ai.eval` — which is the default module
(`package.json` `"export": ["ai.eval"]`). There is no submodule API, so the shared
`getDefaultModule()`-only limitation costs this library nothing.

Complete public surface of the default module (5 type-level + 23 functions):

| Symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `EvalKind` (enum) | annotations.bal:18 | yes | yes |
| `EvalTemplateConfig` (record) | annotations.bal:27 | yes | yes |
| `EvalTemplate` (annotation) | annotations.bal:43 | **no** | yes |
| `Error` (distinct error) | error.bal:18 | stub only | yes |
| `TrajectoryMatchMode` (enum) | rule_based.bal:56 | yes | yes |
| 23 public isolated functions | llm_judges.bal (15), rule_based.bal (8) | all 23 | all 23 |

`old` coverage gaps: 1 (`EvalTemplate` absent) plus 1 degraded (`Error`). `new` closes both.

## 7. Compiler plugin

This package ships **no compiler plugin**. `find` over the upstream tag for
`*compiler-plugin*`/`CompilerPlugin*` returns nothing; `ballerina/Ballerina.toml` has no
`[[platform.java21.dependency]]` or `compilerPlugin` entry (only `[package]` and
`[platform.java21] graalvmCompatible = true`); the bala has no `compiler-plugin/` directory
(contents: `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`).

The one plugin-derived artefact visible in the bala comes from the *dependency* `ballerina/ai`: its
plugin injected `@ai:JsonSchema{...}` onto the private record `JudgeVerdict`
(`llm_judges.bal:26`, absent from the GitHub tag). `JudgeVerdict` is module-private, so its absence
from both renders is correct, not a gap.

Nothing a plugin implies should surface is missing. Conversely, `EvalTemplate` metadata is meant to
be read statically by tooling (per its own doc comment), so rendering it — as `new` now does — is
exactly the right call for an LLM-facing view of this package.

## 8. Other considerations

- **Pre-1.0 (`0.9.0`)**: API is not covenant-stable; the `@EvalTemplate` metadata contract in
  particular is tooling-facing and may move. Not a render defect.
- **No deprecations**: no `@deprecated` in any bala `.bal` file.
- **Size/token impact**: +32 lines (+6.8%), +7,013 JSON bytes (59,452 → 66,465, +11.8%). The 23
  annotation lines are long (up to ~190 chars) but each carries genuinely useful selection metadata
  (`kind` tells the consumer whether a judge model is needed; `needsEvalset` tells it whether a
  recorded thread is required). Good value per token.
- **Doc quality**: high. Every function has a summary plus `+ param`/`+ return` docs; both renders
  preserve them.
- **Renders are not compilable Ballerina** (missing `#` on wrapped doc lines, `public` stripped,
  `Error|()` instead of `Error?`). This is the established format of these renders and applies to
  both sides.
- **Published package builds**: bala matches the tagged source except for the plugin-injected
  annotation; nothing suggests a broken publication.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_ai.eval.bal.txt new/ballerina_ai.eval.bal.txt` | 470 / 502 |
| `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| `grep -n '^// --- '` old | README 6, END README 177, Types 179, Functions 231 |
| `grep -n '^// --- '` new | README 6, END README 177, Types 179, Functions 232, **Annotations 496** |
| `diff -u old new` | 1 deletion (`// Unknown type: Error`), 33 insertions; no other `-` line |
| `cmp <(sed -n '1,177p' old) <(sed -n '1,177p' new)` | identical (README untouched) |
| `ls -R <bala>` | single module `ai.eval`; no `compiler-plugin/`; files `annotations.bal error.bal llm_judges.bal rule_based.bal` |
| `wc -l <bala>/modules/ai.eval/*.bal` | 43 / 18 / 1029 / 496 = 1586 |
| `grep -c '^@EvalTemplate {' <bala>/*.bal` | rule_based 8, llm_judges 15 → **23** |
| `grep -c '^@EvalTemplate {' new/*.bal.txt` | **23** |
| `grep -hoE '^public (isolated )?function \w+' <bala>/*.bal \| sort` | 23 names |
| `comm` src fn names vs new render fn names (lines 178+) | 0 missing, 0 extra |
| `diff` old fn names vs new fn names | identical |
| Python: parse 23 bala signatures vs 23 render signatures (normalise `Error?`→`Error|()`) | **0 mismatches** |
| Python: parse 23 bala `@EvalTemplate` bodies vs 23 render attachments (label/description/kind/needsEvalset) | **0 mismatches, 0 missing, 0 extra** |
| `grep -nE '^public (type\|enum\|const\|annotation\|class\|final)' <bala>/*.bal` | 5: `EvalKind`, `EvalTemplateConfig`, `EvalTemplate`, `Error`, `TrajectoryMatchMode` |
| `cat <bala>/package.json` | `"export": ["ai.eval"]`, distribution 2201.12.0, `readme: docs/README.md` |
| `git ls-remote --tags <repo>` | `v0.9.0` → `0890baf47f1d80f3aaf0e26deaba3b5ade7e618f` |
| `git clone --depth 1 --branch v0.9.0` + `diff -q` tag vs bala for 4 `.bal` files | annotations/error/rule_based identical; llm_judges differs by 2 lines (injected `@ai:JsonSchema` on private `JudgeVerdict`) |
| `find <tag> -iname '*compiler-plugin*'` | no results |
| `cat <tag>/ballerina/Ballerina.toml` | no compiler-plugin / java dependency entries |
| Python JSON compare old vs new | keys identical; `functions` 23→23, `typeDefs` 10→10, `annotations` 0→1, `clients`/`services` 0→0, `readme` & `description` identical; 23 function objects differ only by added `annotations`; `Error` typeDef differs only by added `"baseType":"error"` |
| `wc -c old/*.json new/*.json` | 59,452 → 66,465 |
| `grep -c 'â\|Ã' new/*.bal.txt` | 0 (no mojibake) |
| Count of doc-continuation lines missing `#` (lines 178+) | old 5, new 5 |
| `sed -n '496,502p' new` | Annotations section renders doc + `public annotation EvalTemplateConfig EvalTemplate on function;` |
| `sed -n '179,231p' new` | Types section: 6 consts, `EvalKind`, `EvalTemplateConfig`, `Error`, `TrajectoryMatchMode` |

## 10. Caveats and unverified items

- **`@EvalTemplate` value fidelity is verified as text, not as a compile.** I confirmed all 23
  rendered attachments match the source field-for-field, but I did not compile the render, so I
  cannot assert the render as a whole parses — and in fact it does not, because of the unprefixed
  doc-continuation lines (§5.3) present on both sides.
- **`kind: "LLM_JUDGE"` vs `kind: LLM_JUDGE`**: I reason that the quoted form is type-valid because
  `EvalKind` is a string enum, i.e. the singleton union `"RULE_BASED"|"LLM_JUDGE"`. Not verified by
  compilation.
- **Upstream vs bala divergence in `llm_judges.bal`** is limited to the 2 lines shown by
  `diff -q`/`diff -u`; I read the full unified diff and it contains only the injected
  `@ai:JsonSchema` on the private `JudgeVerdict` record. No public API divergence.
- **Ballerina Central metadata** was not re-queried over the network; module/export information was
  taken from the bala `package.json` (`"export": ["ai.eval"]`), which is authoritative for what the
  extractor consumed.
- The old/new pipeline provenance (branches/commits `eb5d81b3` / `412ba01e`) is taken from the
  brief; I did not independently re-run either renderer.

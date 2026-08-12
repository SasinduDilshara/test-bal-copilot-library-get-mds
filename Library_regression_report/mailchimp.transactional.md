# ballerinax/mailchimp.transactional 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mailchimp.transactional` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mailchimp.transactional |
| Tag reviewed | `v1.0.2` (commit `22c6af3307d4f4e61790dfcc468344dc2c3efc58`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mailchimp.transactional/1.0.2` |
| Old render | `3688` lines |
| New render | `4155` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The `new` render is strictly additive over `old`. Net +467 lines: 469 added, 2 removed — and the
only 2 removed lines are the two `// Unknown type:` placeholders, which `new` replaces with real
type definitions. Everything else added is annotation metadata that exists verbatim in the published
source: 444 `@jsondata:Name`, 22 `@constraint:*`, 1 `@display`.

Verified exhaustively (not sampled): the multiset of annotation strings in `new` is byte-identical to
the multiset in the bala's `types.bal`, and all 466 annotation→declaration bindings attach to the same
target as in the source. The README section, the entire Client section (94 resource methods + `init`),
the doc-comment count (1446) and the field-line count (1193) are unchanged between `old` and `new`.
Type coverage is complete in `new`: 198 of 198 public types exported by the default module, exact set
match, zero coverage gaps. `old` had 2 degraded types. No regressions found.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 3688 | 4155 |
| File size | 145,153 B | 165,091 B |
| `// Unknown type:` placeholders | 2 | 0 |
| Version/module-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |
| Top-level `type` declarations | 196 | 198 |
| `const` declarations (README snippet) | 1 | 1 |
| `public function main` (README snippet) | 1 | 1 |
| Doc-comment lines (`^\s*#`) | 1446 | 1446 |
| Field/statement lines (`^\s+\w.*;$`) | 1193 | 1193 |
| Client classes | 1 | 1 |
| Client methods (incl. `init`) | 95 | 95 |
| Brace balance `{`/`}` | 308/308 | 775/775 |
| Non-ASCII lines | 1 | 1 |

Diff totals: `diff -u` → 469 added lines, 2 removed lines, 152 hunks.

### Declarations added (2)

Both are `Other`-kind string subtypes that `old`'s `renderTypeDef` could not render:

| Added declaration | Source location |
|---|---|
| `type TemplatesAddBodyLabelsItemsString string;` (with `@constraint:String {maxLength: 100}`) | `bala .../types.bal:1560-1561` |
| `type TemplatesUpdateBodyLabelsItemsString string;` (with `@constraint:String {maxLength: 100}`) | `bala .../types.bal:3159-3160` |

### Declarations removed (0)

None. `comm -23 old_types new_types` → empty.

### Non-declaration lines added (467) — all annotations

Breakdown of the 469 added lines (all accounted for):

| Added line | Count |
|---|---|
| `@jsondata:Name {value: "…"}` | 444 |
| `@constraint:Int {minValue: 0, maxValue: 100}` | 9 |
| `@constraint:String {maxLength: 255}` | 5 |
| `@constraint:String {maxLength: 100}` | 2 |
| `@constraint:String {maxLength: 1024}` | 2 |
| `@constraint:Array {maxLength: 10}` | 2 |
| `@constraint:String {maxLength: 64}` | 1 |
| `@constraint:Int {minValue: 100, maxValue: 1000}` | 1 |
| `@display {label: "Connection Config"}` | 1 |
| `type TemplatesAddBodyLabelsItemsString string;` | 1 |
| `type TemplatesUpdateBodyLabelsItemsString string;` | 1 |
| **Total** | **469** |

### Sections

Both renders: README `7–133`, Types `135–…`, Client (`old` `3308`, `new` `3775`). Client section is
381 lines on both sides and `diff` reports them identical.

### JSON-level change

Old JSON is a **strict structural subset** of new JSON: a recursive key/value containment check over
the whole document returned **0 differences** (no key removed, no value changed, no list shortened).
`new` adds two things only:
- `baseType` on `Other`-kind typeDefs (e.g. `"baseType": "string"`),
- `annotations: [{name, module, value}]` on typeDefs (3) and record fields (464) — 467 total.

Annotation modules recorded in the new JSON: `ballerina/data.jsondata:Name` ×444,
`ballerina/constraint:String` ×10, `ballerina/constraint:Int` ×10, `ballerina/constraint:Array` ×2,
`display` (no module) ×1.

## 3. Correctness against library source

The upstream tag `v1.0.2` and the bala are **byte-identical** for the two source files that matter:
`diff -q src/ballerina/types.bal bala/.../types.bal` and the same for `client.bal` both returned
clean. So GitHub and the bala agree; no disambiguation needed.

**Annotations — exhaustive, not sampled.**
- Annotation string multiset: `grep -oE '@jsondata:Name \{value: "[^"]*"\}'` over bala `types.bal`
  vs. `new` render → `diff` clean ("JSONDATA NAMES IDENTICAL"), 444 on both sides.
- `grep -oE '@constraint:[A-Za-z]+ \{[^}]*\}'` over both → `diff` clean ("CONSTRAINTS IDENTICAL"),
  22 on both sides (10 Int, 10 String, 2 Array).
- `@display {label: "Connection Config"}`: 1 in bala `types.bal:84`, 1 in `new` render line 390.
- **Binding check**: a script paired every annotation with the next non-doc/non-annotation line in
  both files. 466 pairs in the bala, 466 in `new`, multiset-identical except for two entries where
  the render strips the `public` keyword (`public type TemplatesAddBodyLabelsItemsString string;` →
  `type TemplatesAddBodyLabelsItemsString string;`) — the same `public`-stripping `old` already did
  for all 196 of its types. So every annotation in `new` sits on the correct declaration.

**Types.** All 198 `public type` names in the bala default module appear in `new`; `comm` in both
directions is empty. No invented symbols.

**Client.** All 94 `resource isolated function post <path>` paths in `bala/client.bal` match the 94
`resource function post <path>` paths in the `new` render exactly (`comm -3` empty). Plus `init`.
The client section is unchanged from `old`.

**Spot-checked signatures.**
- `TemplatesAddBodyLabelsItemsString` — bala `types.bal:1560-1561`: `@constraint:String {maxLength: 100}` /
  `public type TemplatesAddBodyLabelsItemsString string;` → `new` lines 923-924 render exactly that.
- `TemplatesAddBody.labels` — bala `types.bal:449-450`: `@constraint:Array {maxLength: 10}` /
  `TemplatesAddBodyLabelsItemsString[] labels?;` → `new` lines 919-920 identical.
- `MessagessendTemplateBody.templateName` → `@jsondata:Name {value: "template_name"}` (`new` line 142);
  matches source.
- `InlineResponse2005` fields `result_url` / `finished_at` / `created_at` → correct names and order.
- `ConnectionConfig` — bala `types.bal:84` `@display {label: "Connection Config"}` → `new` line 390.
- `init(ConnectionConfig config = {}, string serviceUrl = "https://mandrillapp.com/api/1.0") returns error?`
  matches `bala/client.bal` `Client.init`.

## 4. Regressions

**None found.**

What was checked to conclude that:
- `diff -u old new | grep '^-[^-]'` → exactly 2 removed lines, both `// Unknown type:` placeholders.
  Nothing else was deleted or modified.
- Declaration set: `comm -23 old_types.txt new_types.txt` → empty (nothing dropped).
- Client section: `diff old_client.txt new_client.txt` → identical (381 lines each).
- README section (render lines 7–133): `diff` → identical, and matches the bala `docs/README.md`
  (124 lines) verbatim.
- Doc comments: 1446 in both. Field lines: 1193 in both. No docs, defaults, parameters or return
  types dropped.
- JSON containment check: 0 differences — no data present in the old JSON is missing or altered in
  the new JSON.
- Syntax: `{`/`}` balanced in `new` (775/775). Annotation placement follows the required Ballerina
  order (doc comment → annotation → declaration/field), so the added lines do not break parseability.
- No `mod:1.2.3:Type` refs on either side (0/0), so the version-qualified-ref class of change does
  not apply here.

## 5. Issues in `new` (independent of `old`)

1. **Annotation module prefixes are unqualified and no import is shown (minor, cosmetic).** The
   render's only import line is `import ballerinax/mailchimp.transactional;` (line 5). The 466
   emitted annotations use the prefixes `jsondata:` and `constraint:`, whose modules
   (`ballerina/data.jsondata`, `ballerina/constraint`) are recorded in the JSON's `annotations[].module`
   field but never surfaced in the text render. For cross-package *types* the renderer does emit a
   trailing hint (14 × `// Special Agent Note: … FROM ballerina/http package`); annotations get no
   equivalent hint. Impact is low — the render is a reference document, not compilable input, and
   `old` had the same unqualified-prefix pattern for `http:` types — but a consumer could not resolve
   `jsondata` / `constraint` from the render alone.

No wrong types, invented symbols, missing default-module API, broken doc text, or encoding problems
were found. Non-ASCII line count is 1 on both sides (unchanged README content).

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.**

- The bala exports exactly one module: `package.json` `"export": ["mailchimp.transactional"]`, and
  `modules/` contains only `mailchimp.transactional`. Central confirms a single module. So the
  known `getDefaultModule()`-only limitation costs nothing here — there is no submodule API.
- Public types: 198 in bala, 198 in `new` render, exact set match (both `comm` directions empty).
- Non-type public declarations in the bala: `grep -nE '^public (isolated )?(function|class|const|enum|annotation|listener|distinct)'`
  over all three `.bal` files returns exactly one hit — `public isolated client class Client`
  (`client.bal:23`) — which is rendered, with all 94 resource methods.
- `utils.bal:26 isolated function getEncodedUri(...)` is module-private, correctly absent.
- `old` had 2 coverage gaps (the two `// Unknown type:` placeholders rendered with no definition
  and no base type); `new` closes both.

## 7. Compiler plugin

**None.** No `compiler-plugin` / `*-compiler-plugin` directory exists in the repo at `v1.0.2`
(`find src -maxdepth 2 -iname '*compiler*'` → no matches), `Ballerina.toml` declares no
`[[platform.java21.dependency]]` and no `[compilerPlugin]` section, and the bala has no
`compiler-plugin/` entry (only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
`package.json`). Nothing plugin-implied is missing from the render.

## 8. Other considerations

- Not deprecated: Central returns `deprecated: null`, `deprecateMessage: ""`.
- Stable 1.x connector, `distribution = "2201.12.0"`, `graalvmCompatible = true`, pull count 72.
- Size/token impact: `new` is +467 lines / +19,938 bytes (+13.7 %) over `old`. The added
  `@jsondata:Name` lines are high-value for an LLM — this connector's Ballerina field names are
  camelCase while the Mandrill wire format is snake_case (`templateName` ↔ `template_name`), so
  without those annotations the render silently hides the actual JSON contract. Likewise the
  `@constraint:*` annotations carry validation limits (`maxLength: 10` on `labels`, etc.) that were
  entirely absent from `old`.
- The two closed `// Unknown type:` placeholders were pure noise in `old`: they named a type used by
  `TemplatesAddBody.labels` / `TemplatesUpdateBody.labels` while giving no base type at all.
- All three JSON `readme`, `description`, `name` fields are equal between old and new; `annotations`,
  `services`, `functions` are empty arrays on both sides (this package has no module-level
  annotations, services, or public free functions).

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 3688, new 4155 |
| 2 | `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| 3 | `grep -n '^// Unknown type:'` old | lines 838, 2974 |
| 4 | `grep -n '^// --- '` old / new | 4 markers each; Client at 3308 / 3775 |
| 5 | `diff -u old new \| grep '^-[^-]'` | exactly the 2 `// Unknown type:` lines |
| 6 | `diff -u old new \| grep '^+[^+]'` categorised | 469 lines: 444 jsondata, 22 constraint, 1 display, 2 type defs (table in §2) |
| 7 | `grep -c '@jsondata:Name'` bala `types.bal` | 444 |
| 8 | `grep -oE '@constraint:[A-Za-z]+'` bala `types.bal` | 2 Array, 10 Int, 10 String |
| 9 | `grep -n '@display'` bala `*.bal` | 1 hit, `types.bal:84` |
| 10 | `diff` of sorted `@jsondata:Name {…}` strings, bala vs new | identical |
| 11 | `diff` of sorted `@constraint:… {…}` strings, bala vs new | identical |
| 12 | Python annotation→target pairing, bala vs new | 466 vs 466; multiset differs only by stripped `public` on 2 entries |
| 13 | `grep -oE '^type \w+'` old / new / bala `^public type` | 196 / 198 / 198 |
| 14 | `comm -23 src_types new_types` | empty (no public type missing from new) |
| 15 | `comm -13 src_types new_types` | empty (no invented type in new) |
| 16 | `comm` old_types vs new_types | only `TemplatesAddBodyLabelsItemsString`, `TemplatesUpdateBodyLabelsItemsString` added |
| 17 | `diff` of client sections (`tail -n +3308` old vs `tail -n +3775` new) | identical, 381 lines each |
| 18 | Resource paths: bala `client.bal` vs new render | 94 vs 94, `comm -3` empty |
| 19 | `grep -cE '^\s+(remote\|resource) isolated function'` bala `client.bal` | 94 |
| 20 | `grep -nE '^public (isolated )?(function\|class\|const\|enum\|annotation\|listener\|distinct)'` bala `*.bal` | 1 hit: `client.bal:23 public isolated client class Client` |
| 21 | `diff` render README section vs bala `docs/README.md` | identical (124 lines) |
| 22 | `diff` render README section old vs new | identical |
| 23 | `grep -c '^\s*#'` old / new | 1446 / 1446 |
| 24 | `grep -cE '^\s+[A-Za-z].*;$'` old / new | 1193 / 1193 |
| 25 | `grep -cE '[a-zA-Z_.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 0 / 0 |
| 26 | brace balance old / new | 308/308, 775/775 |
| 27 | non-ASCII line count old / new | 1 / 1 |
| 28 | `grep -c 'Special Agent Note'` new | 14 (all `ballerina/http` types in `ConnectionConfig`) |
| 29 | `grep -n '^import'` new render | only `import ballerinax/mailchimp.transactional;` (line 5) |
| 30 | Recursive JSON containment old ⊆ new | 0 differences |
| 31 | JSON typeDefs count old / new | 198 / 198 |
| 32 | JSON annotation counts new | 3 typeDef-level + 464 field-level = 467 |
| 33 | JSON annotation modules new | `ballerina/data.jsondata:Name` 444, `ballerina/constraint:String` 10, `:Int` 10, `:Array` 2, `display` 1 |
| 34 | `git ls-remote --tags` upstream | `v1.0.0`, `v1.0.1`, `v1.0.2` — exact tag exists |
| 35 | `git clone --depth 1 --branch v1.0.2` | HEAD `22c6af3307d4f4e61790dfcc468344dc2c3efc58` |
| 36 | `diff -q src/ballerina/types.bal bala/.../types.bal` | identical |
| 37 | `diff -q src/ballerina/client.bal bala/.../client.bal` | identical |
| 38 | `find src -maxdepth 2 -iname '*compiler*'` | no matches |
| 39 | `Ballerina.toml` at `v1.0.2` | version `1.0.2`, distribution `2201.12.0`, no compiler-plugin section |
| 40 | bala `package.json` | `export: ["mailchimp.transactional"]`, single module |
| 41 | bala `any/` listing | no `compiler-plugin/` entry |
| 42 | Central `GET /2.0/registry/packages/ballerinax/mailchimp.transactional/1.0.2` | version 1.0.2, `deprecated: null`, 1 module, pullCount 72 |
| 43 | bala `types.bal:449-450`, `1560-1561`, `3159-3160` read | confirm `labels` field + both alias types with constraints |
| 44 | new render lines 915-945, 387-393 read | confirm rendered forms match those source lines |

## 10. Caveats and unverified items

- **Compilability was not tested.** Neither render was fed to `bal build`; the syntax assessment rests
  on brace balance, annotation ordering, and per-declaration inspection, not on a compiler run. This
  is inherent to the artefact (the render is a concatenated reference document with unresolvable
  cross-package prefixes such as `http:` and now `jsondata:`), not a defect introduced by `new`.
- **The `@display` annotation's module is `null` in the new JSON.** The render emits `@display {label: …}`
  unqualified, which is how it appears in the source, so this is correct output; but I did not verify
  whether the extractor is deliberately omitting the module for lang-level annotations or simply
  failed to resolve it. Behaviour of the extractor is out of scope for this audit.
- Everything else in this report was verified directly against the bala, the upstream `v1.0.2` tag,
  Central metadata, or the two render/JSON pairs, with the commands listed in §9.

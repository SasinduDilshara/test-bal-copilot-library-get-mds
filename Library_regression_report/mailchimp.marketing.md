# ballerinax/mailchimp.marketing 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mailchimp.marketing` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mailchimp.marketing |
| Tag reviewed | `v1.0.2` (exact tag; source files byte-identical to the bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mailchimp.marketing/1.0.2` |
| Old render | `11579` lines (501,365 bytes) |
| New render | `13811` lines (592,009 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is `old` plus 2,232 annotation lines, minus three classes of defect. After normalising for
those two facts the two renders are byte-identical except for 5 lines, all of which `new` gets right
and `old` got wrong.

Concretely, `new`:

- adds **2,232 annotation lines** — 1,926 `@jsondata:Name`, 242 `@http:Query`, 59 `@constraint:Int`,
  4 `@constraint:String`, 1 `@display`. Every count matches the bala exactly, and an
  annotation→field pairing check matched **2,232 / 2,232**.
- removes the malformed parameter `anydata Additional Values` from **132** of the 274 client
  resource methods (a parameter name containing a space; non-parseable Ballerina).
- removes **10** occurrences of the version-qualified type prefix
  `ballerinax/mailchimp.marketing:1.0.2:` from inline record types.
- fixes **4** occurrences of the reserved word `type` used as a bare field name → `'type`.

Nothing is dropped. Declaration sets, doc comments, README, client method list and all 274 resource
signatures are otherwise identical. Zero coverage gaps against the bala's default (and only) module.

## 2. Change inventory

Line accounting from `diff -u old new` (`full.diff`, 11,585 lines):

| | count |
|---|---|
| Lines added | 2,370 |
| Lines removed | 138 |
| Net | +2,232 (11,579 → 13,811) ✓ |

Added lines break down as:

| Added | n |
|---|---|
| Annotation lines (`@…`) | 2,232 |
| Re-emitted resource-function signatures (minus `anydata Additional Values`) | 132 |
| Re-emitted inline `reportSummary` record (minus version-qualified prefixes) | 2 |
| Re-emitted `type?` → `'type?` field lines | 4 |
| **total** | **2,370** |

Removed lines are exactly the 132 + 2 + 4 pre-images. **No line is removed without a replacement.**

Declaration-set comparison (kinds: `type`/`class`/`enum`/`const`/`annotation`/`listener`/`service`):

```
626 declarations in old, 626 in new
comm -23 old new  → empty      (nothing removed)
comm -13 old new  → empty      (nothing added)
```

Client members:

| | old | new | bala |
|---|---|---|---|
| `resource function` | 274 | 274 | 274 |
| `remote function` | 0 | 0 | 0 |
| `function init` | 1 | 1 | 1 |

Equivalence proof for the client:
```
diff <(grep '    resource function' old | sed 's/anydata Additional Values, //' | sort) \
     <(grep '    resource function' new | sort)
→ no differences  (all 274 identical)
```

Whole-file equivalence proof (strip `    @…` lines from `new`, strip the version prefix and the
bogus param from `old`):
```
diff o_norm.txt n_stripped.txt
→ 5 differing lines only:
   3× / 4 total  "…|\"sms\" type?;"  →  "…|\"sms\" 'type?;"   (new is correct)
   1×           +@display {label: "Connection Config"}          (new is correct)
```

Annotation totals vs. the bala (`modules/mailchimp.marketing/{types,client,utils}.bal`):

| Annotation | bala (line-leading) | new render | bala (all occurrences) | new (all occurrences) |
|---|---|---|---|---|
| `@jsondata:Name` | 1926 | 1926 | 1928 | 1926 |
| `@http:Query` | 242 | 242 | 242 | 242 |
| `@constraint:Int` | 59 | 59 | 59 | 59 |
| `@constraint:String` | 4 | 4 | 4 | 4 |
| `@display` | 1 | 1 | 1 | 1 |
| `@deprecated` | 4 | 0 | 4 | 0 |

`old` contains **0** annotations of any kind.

JSON payloads: same top-level keys, `typeDefs` 626 → 626, `clients` 1 → 1, `functions`/`services`/
`annotations` 0 → 0 on both sides. JSON size 1,750,706 → 2,162,757 bytes.

## 3. Correctness against library source

Upstream `v1.0.2` and the bala agree exactly:

```
diff -q src/ballerina/types.bal  <bala>/modules/mailchimp.marketing/types.bal   → IDENTICAL
diff -q src/ballerina/client.bal <bala>/modules/mailchimp.marketing/client.bal  → IDENTICAL
diff -q src/ballerina/utils.bal  <bala>/modules/mailchimp.marketing/utils.bal   → IDENTICAL
Ballerina.toml: version = "1.0.2"
```

Verification of what `new` adds:

- **Annotation fidelity, exhaustive.** A script paired every line-leading annotation with the
  declaration it precedes, in both the bala and the `new` render, and compared the multisets:
  `bala pairs 2232`, `render pairs 2232`, `0` genuine mismatches (the 3 reported deltas on each side
  are regex artefacts from the `public` keyword and from one inline anonymous record, and resolve to
  the same annotation/field pair).
- **Spot check — `GetTemplatesQueries`** (bala `types.bal:5344-5380` vs `new:7892-7927`): all 8
  `@http:Query` names (`before_date_created`, `exclude_fields`, `created_by`, `since_date_created`,
  `sort_field`, `content_type`, `folder_id`, `sort_dir`) and the `@constraint:Int {maxValue: 1000}`
  on `count` reproduce verbatim, in source order.
- **Spot check — `ConnectionConfig`** (bala `types.bal:5571-5612` vs `new:8177-8216`):
  `@display {label: "Connection Config"}` reproduced verbatim in the correct position.
- **`'type` fix.** bala `types.bal` declares the field as `'type?` (reserved word escaped).
  `old` emitted `type?` in 4 inline anonymous records; `new` emits `'type?`. `new` matches source.
- **Version-qualified refs.** `old:4644` and `old:10412` contained
  `ballerinax/mailchimp.marketing:1.0.2:ReportSummaryEcommerce` etc. (10 occurrences). `new:5621`
  and `new:12636` emit the plain `ReportSummaryEcommerce`, which is what the bala writes.
- **`anydata Additional Values`.** No such parameter exists anywhere in `client.bal`; it was an
  artefact of `old`'s rest-parameter handling. Its removal in `new` matches source.

Public-API coverage against the bala:

```
grep -hoE '^public [a-z ]*' <bala>/modules/mailchimp.marketing/*.bal | sort | uniq -c
  626 public type
    1 public isolated client class      (Client)
→ 627 public declarations
render: 626 typeDefs + 1 client = 627
comm -23 bala_public new_render → only "Client" (rendered as `client class Client`, not a `type`)
comm -13 bala_public new_render → empty (no invented symbols)
```

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

1. Declaration-set diff (626 vs 626, `comm` empty both directions) — nothing dropped.
2. Client member diff — all 274 resource signatures byte-identical after removing the one bogus
   parameter; `init` identical.
3. Whole-file normalised diff — after stripping only the added annotation lines, the removed
   `anydata Additional Values, ` token and the removed version prefix, only 5 lines differ, and all
   5 are corrections in `new`'s favour.
4. README block (`lines 8–83`) — `diff` of `old` and `new` lines 1–84 is empty; and all 76 lines
   round-trip against the bala's `docs/README.md` (0 lines in either direction unmatched).
5. Doc comments — no `#` line is present in `old` and absent in `new` (falls out of check 3).
6. Malformed-syntax scan — exactly one non-conforming line in each file, and it is the *same* line
   (`old:6790` / `new:8216`), so `new` introduces no new syntax breakage.
7. `// Unknown type:` placeholders — 0 in both (this library has no `Error`/object/`Other` typedefs,
   so the headline spec-v2 improvement does not apply here).
8. Non-ASCII characters — 15 lines in both files, matching upstream (13 in `types.bal`, 2 in README);
   no encoding drift.

## 5. Issues in `new` (independent of `old`)

All nine below are also present in `old` except **N5**, which is a side-effect of adding annotations.
None is a regression; they are residual fidelity gaps a reviewer should know about.

**N1 — Record-field default values are dropped and the field is marked optional.**
bala `types.bal:5576` `http:HttpVersion httpVersion = http:HTTP_2_0;` → `new:8182`
`http:HttpVersion httpVersion?;`. Same for `timeout = 30`, `forwarded = "disable"`,
`validation = true`, `laxDataBinding = true`, and `GetTemplatesQueries` `offset = 0` / `count = 10`
(bala `types.bal:5346,5349` → `new:7894,7897` as `int offset?; int count?;`). This changes required
fields into optional ones and hides every default. Present identically in `old`.

**N2 — Closed records are rendered as open.**
bala `public type ConnectionConfig record {| … |};` → `new:8178` `type ConnectionConfig record { … };`.

**N3 — Client method signatures do not match source.**
Source: `resource isolated function get templates(map<string|string[]> headers = {}, *GetTemplatesQueries queries)`
(bala `client.bal:2254`). Render (`new:13462`, and `old:11230`) flattens the included record into 13
positional parameters **and** appends `GetTemplatesQueries queries`, i.e. the query record appears
twice. The flattened parameters also carry invented defaults (`string beforeDateCreated = ""`,
`int count = 0`, `"date_created"|… sortField = "date_created"`) that contradict the source, where
those fields are optional or default to `10`. Applies to all 274 resource methods.

**N4 — One malformed (non-compiling) line.**
`new:8216` (= `old:6790`) emits a doc-comment continuation as bare code inside a record body:
`and absent fields are handled as \`nilable\` types. Enabled by default.` — the `# ` prefix of the
second doc line is lost. It is the only line in either file that is neither blank, comment,
annotation, nor a statement/brace.

**N5 — Annotation module prefixes are used without imports or notes (new-only).**
`new` emits `@jsondata:Name`, `@http:Query`, `@constraint:Int`, `@constraint:String` but the render
declares only `import ballerinax/mailchimp.marketing;` (`new:5`). The bala imports
`ballerina/data.jsondata`, `ballerina/http`, `ballerina/constraint`. The renderer's existing
"Special Agent Note" mechanism (used for `http:CredentialsConfig` etc. in the field position) is not
applied to annotations, so the prefixes are unresolvable for a consumer. Cosmetic for an LLM reader;
worth noting for anyone treating the render as compilable Ballerina.

**N6 — All 4 `@deprecated` markers dropped.**
bala `client.bal:842, 857, 872, 888` mark `get conversations`, `get conversations/[id]`,
`get conversations/[id]/messages`, `get conversations/[id]/messages/[messageId]` deprecated. Neither
render marks them (`new:13002, 13006, 13010, 13014`). An LLM will happily recommend deprecated API.

**N7 — 2 `@jsondata:Name` annotations inside inline anonymous records are dropped.**
bala `types.bal:3195-3196` (`InlineResponse20012FacebookAds.reportSummary`) contains an inner
`@jsondata:Name {value: "click_rate"}`. The render flattens the anonymous record onto one line
(`new:5621`, `new:12636`) and loses it. This is the whole of the 1928 → 1926 delta.

**N8 — `public` / `isolated` qualifiers dropped.**
`public isolated client class Client` → `client class Client`;
`public isolated function init(...)` → `function init(...)`;
`resource isolated function` → `resource function` (all 274).

**N9 — Parameter and return doc lines dropped from client methods.**
bala `client.bal:836-841` carries `# + headers - …`, `# + queries - …`, `# # Deprecated`; the render
keeps only the summary line plus an empty `# `.

## 6. Coverage gaps vs. the library

**None.** The bala exports exactly one module (`package.json` `"export": ["mailchimp.marketing"]`,
`modules/` contains only `mailchimp.marketing/`), so the known default-module-only extraction limit
does not bite here.

- 626 / 626 `public type` present in both renders.
- 1 / 1 `public isolated client class Client` present.
- 274 / 274 `resource isolated function` present; 0 remote functions in source, 0 in render.
- 0 public constants, enums, annotations, listeners or module-level functions exist in the bala
  (`grep -hoE '^public [a-z ]*'` yields only `public type` and `public isolated client class`), so
  nothing of those kinds can be missing.
- No submodule-only API (single module) → no shared submodule gap.

Sub-symbol gaps are listed under §5 (N6, N7, N9) rather than here, since they are attributes of
symbols that *are* present.

## 7. Compiler plugin

**None exists.** `find src -maxdepth 2 -iname '*compiler-plugin*' -o -iname '*plugin*'` on the
`v1.0.2` clone returns nothing; the bala's `any/` directory contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/compiler-plugin.json`. Nothing is expected to surface in the render from a plugin,
and nothing is missing on that account.

The library does depend on annotation-defining packages (`ballerina/data.jsondata`,
`ballerina/constraint`, `ballerina/http`); the render now reproduces their annotations faithfully
(§3), which is the main functional consequence for a consumer generating JSON payloads — `new`
finally exposes the wire-level field names (`_links`, `list_id`, `total_items`, …) that `old` hid
entirely.

## 8. Other considerations

- **Not deprecated.** Ballerina Central reports `deprecated: null`, `deprecateMessage: ""` for
  `ballerinax/mailchimp.marketing/1.0.2`; `ballerinaVersion 2201.12.0`, `pullCount 60`, one module.
- **Post-1.0 stable version.** No pre-release caveat.
- **Size / token cost.** `new` is +19.3% lines and +18.1% bytes (501,365 → 592,009). The JSON grows
  +23.5% (1,750,706 → 2,162,757 bytes). This library is already one of the larger renders; the
  annotation payload is a real but justified cost — without it an LLM cannot produce correct JSON
  field names, since almost every record field is camel-cased in Ballerina and snake_cased on the
  wire (1,926 `@jsondata:Name` renames out of ~5,500 fields).
- **Highest-value fix for consumers.** The `anydata Additional Values` parameter in `old` appeared in
  132 of 274 method signatures. Any LLM copying those signatures would emit code that does not
  parse. Its removal alone justifies the change.
- **Doc quality.** Method-level summaries are one-liners inherited from the Mailchimp OpenAPI spec;
  field docs are rich. Both renders carry the same doc text.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags <repo>` | tags `v1.0.0`, `v1.0.1`, `v1.0.2`; exact match found |
| 2 | `git clone --depth 1 --branch v1.0.2 <repo> src` | success |
| 3 | `diff -q src/ballerina/{types,client,utils}.bal <bala>/modules/mailchimp.marketing/` | all IDENTICAL |
| 4 | `grep -n version src/ballerina/Ballerina.toml` | `version = "1.0.2"` |
| 5 | `wc -l old new` | 11579 / 13811 |
| 6 | `wc -c old new` | 501365 / 592009 |
| 7 | `grep -c '^// Unknown type:' old new` | 0 / 0 |
| 8 | `grep -n '^// --- ' old new` | 4 markers each, same order (README 7/84, Types 86, Client 10479 vs 12711) |
| 9 | type-decl set extraction + `comm` both directions | 626 / 626, both diffs empty |
| 10 | `grep -c '    resource function' old new` | 274 / 274 |
| 11 | `diff <(grep resource old \| sed 's/anydata Additional Values, //' \| sort) <(grep resource new \| sort)` | no differences |
| 12 | `grep -c 'Additional Values' old new` | 132 / 0 |
| 13 | `grep -oE 'ballerinax/mailchimp.marketing:1\.0\.2:' old \| wc -l` / same on new | 10 / 0 |
| 14 | `diff o_norm.txt n_stripped.txt` (annotations + known tokens normalised) | 5 lines: 4× `type?`→`'type?`, 1× `+@display` |
| 15 | `grep '^+' full.diff \| grep -cE '^\+\s*@'` | 2232 of 2370 added lines are annotations |
| 16 | `grep '^-' full.diff \| wc -l` | 138 removed (132 resource + 4 `type?` + 2 reportSummary) |
| 17 | annotation-kind counts, bala vs new (line-leading) | 1926/1926, 242/242, 59/59, 4/4, 1/1 |
| 18 | annotation-kind counts, bala vs new (all occurrences) | `@jsondata:Name` 1928 vs 1926; `@deprecated` 4 vs 0; rest equal |
| 19 | annotation→declaration pairing multiset, bala vs new | 2232 vs 2232, 0 genuine mismatches |
| 20 | annotations by section in new | 2232 in Types (86–12710), 0 in Client (12711+) — matches bala (242+1926+59+4+1 all in `types.bal`, 0 in `client.bal`) |
| 21 | `grep -hoE '^public [a-z ]*' <bala>/*.bal \| sort \| uniq -c` | 626 `public type`, 1 `public isolated client class` |
| 22 | `comm` bala public symbols vs render declarations | only `Client` (rendered as `client class`); nothing invented |
| 23 | `grep -c '^    resource isolated function' <bala>/client.bal` | 274 |
| 24 | `grep -n 'function init' <bala>/client.bal` vs `new:12714` | signature + default `serviceUrl` match |
| 25 | README: `diff <(sed -n 1,84p old) <(sed -n 1,84p new)` | identical |
| 26 | README round-trip vs `<bala>/docs/README.md` | 0 lines unmatched either direction (76 lines) |
| 27 | malformed-line scan (non-blank, non-comment, non-annotation, non-statement) | exactly 1 in each: `old:6790` / `new:8216`, same text |
| 28 | `grep -c 'record {\|' old new` | 47 / 47 (closed-record count unchanged) |
| 29 | `grep -c '^import' old new` + `grep -n '^import' new` | 2 / 2, both `ballerinax/mailchimp.marketing` (self + README sample) |
| 30 | `LC_ALL=C grep -c '[^ -~\t]' old new` | 15 / 15 |
| 31 | `find src -iname '*compiler-plugin*'` and `ls <bala>/any/` | no plugin |
| 32 | `<bala>/any/package.json` | `export: ["mailchimp.marketing"]`, single module, `ballerina_version 2201.12.0`, graalvmCompatible |
| 33 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerinax/mailchimp.marketing/1.0.2` | `deprecated: null`, 1 module, pullCount 60 |
| 34 | JSON structural compare (python) | same keys; `typeDefs` 626/626, `clients` 1/1, `functions`/`services`/`annotations` 0/0 |
| 35 | bala `client.bal:842,857,872,888` `@deprecated` vs `new:13002,13006,13010,13014` | 4 markers absent in both renders |
| 36 | bala `types.bal:3195-3196` inner `@jsondata:Name {value: "click_rate"}` vs `new:5621` | absent (inline anon record flattened) |
| 37 | bala `types.bal:5344-5380` vs `new:7892-7927` (`GetTemplatesQueries`) | all 8 `@http:Query` + `@constraint:Int` reproduced; defaults `0`/`10` lost in both renders |
| 38 | bala `types.bal:5571-5612` vs `new:8177-8216` (`ConnectionConfig`) | `@display` reproduced; 9 field defaults lost, `{\|…\|}` → `{…}` in both renders |

## 10. Caveats and unverified items

- The renders were **not compiled**. Claims about "non-compiling" lines (N4, the
  `anydata Additional Values` parameter, N5's missing imports) are based on Ballerina grammar
  reading, not on a `bal build` run. No Ballerina distribution invocation was attempted, since the
  renders are deliberately body-less stubs and would not compile regardless.
- I did not independently re-run the two-stage extraction pipeline; I audited the committed
  `old`/`new` artefacts as given. The brief's statement that both sides used the same pinned
  version is consistent with everything observed (identical declaration sets, identical README,
  identical doc text), but was not re-derived from the extractor.
- Annotation *argument* values were verified as whole rendered lines against the bala (exact string
  match of e.g. `@jsondata:Name {value: "list_id"}`), and their attachment target was verified by the
  pairing multiset. I did not separately parse annotation argument expressions.
- Field-by-field type checking of all ~5,500 record fields against the bala was not performed
  individually; it is covered transitively by evidence #14 — after normalisation the two renders
  differ in only 5 lines, and `old`'s field rendering was itself derived from the same bala.
- The three "mismatches" reported by the pairing script (#19) were manually inspected and attributed
  to the script's own regex (the `public` keyword and one inline anonymous record). They are not
  render defects, but the attribution is a manual judgement rather than an automated one.

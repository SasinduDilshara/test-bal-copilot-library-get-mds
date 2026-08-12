# ballerinax/zoom.scheduler 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/zoom.scheduler` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-zoom.scheduler |
| Tag reviewed | `v1.0.2` (exact match; commit `8ea190c1ec24cf0f2cc974876b1af3d386d7f0b1`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/zoom.scheduler/1.0.2` |
| Old render | `1419` lines |
| New render | `1673` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The `new` render is a strict superset of `old` in information content. The entire diff (42 hunks,
+268 / −14 lines) decomposes into exactly three effects, all improvements:

1. **254 annotation lines recovered** (`@jsondata:Name` ×182, `@constraint:String` ×28,
   `@http:Query` ×24, `@constraint:Number` ×19, `@display` ×1). These are absent from `old`
   entirely. Verified: the multiset of annotation expressions in `new` is **byte-identical** to
   that in the bala's `types.bal`, and all 253 annotation→field attachments land on the correct
   field of the correct record.
2. **3 `// Unknown type:` placeholders replaced with real definitions.** All three are
   `public type X string;` aliases in the source; `new` emits `type X string;`. `old` had 3 such
   placeholders, `new` has 0.
3. **11 malformed client resource-function signatures repaired.** `old` emitted a synthetic
   parameter literally spelled `anydata Additional Values` (an identifier containing a space —
   non-compiling Ballerina) in every method that has an included-record query parameter. `new`
   drops it.

Nothing is present in `old` and missing from `new`. Declaration name sets are identical apart from
the 3 additions. Doc-comment count is identical (505 in both). README section is byte-identical.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 1419 | 1673 |
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| Section markers (`// --- `) | 4 | 4 |
| `type X ...` declarations | 64 | 67 |
| `client class` | 1 | 1 |
| `resource function` declarations | 17 | 17 |
| `function init` | 1 | 1 |
| Doc-comment lines (`^\s*#`) | 505 | 505 |
| `@jsondata:Name` | 0 | 182 |
| `@constraint:String` | 0 | 28 |
| `@constraint:Number` | 0 | 19 |
| `@http:Query` | 0 | 24 |
| `@display` | 0 | 1 |
| `// Special Agent Note:` cross-package hints | 17 | 17 |

JSON side (`old/*.json` vs `new/*.json`): both have `typeDefs=67`, `clients=1`,
`functions=0`, `services=0`, `annotations=0`; identical typeDef name sets; client has 18 functions
on both sides. Two JSON deltas:

- `{"name":"...AnswerchoicesItemsString","type":"Other"}` gains `"baseType":"string"` in `new`
  (3 typeDefs) — this is what lets the renderer emit a real alias instead of `// Unknown type:`.
- Total client parameter count drops 88 → 77: the 11 bogus `("Additional Values","anydata")`
  parameters are gone.

**Added (3), by kind — all type aliases:**
`InlineResponse2011CustomFieldsAnswerchoicesItemsString`,
`SchedulerschedulesCustomFieldsAnswerchoicesItemsString`,
`SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString`.

**Removed: 0.** **Modified: 11 client resource functions** (parameter removal only) and
~40 records (annotation lines inserted).

## 3. Correctness against library source

The bala's `client.bal`, `types.bal` and `utils.bal` are **byte-identical** to the GitHub `v1.0.2`
tree (`diff` returned no output for all three), so GitHub and the bala agree; no tie-break needed.

- **The 3 new aliases exist verbatim.** `types.bal:286`
  `public type InlineResponse2011CustomFieldsAnswerchoicesItemsString string;`, `types.bal:1073`
  `public type SchedulerschedulesscheduleIdCustomFieldsAnswerchoicesItemsString string;`,
  `types.bal:1091` `public type SchedulerschedulesCustomFieldsAnswerchoicesItemsString string;`.
  `new` renders all three as `type <Name> string;` — correct (the renderer drops `public`
  uniformly on both sides, so this is not a `new` artifact).
- **Annotations — exhaustive check, not a spot-check.** Extracting every
  `@(jsondata:Name|constraint:String|constraint:Number|constraint:Array|http:Query|display) {...}`
  expression from `new` and from `types.bal` and comparing sorted counted multisets:
  `diff` reported no difference (`ANNOTATIONS_IDENTICAL`). Per-annotation totals also match
  individually (182/28/19/24/1 on both sides).
- **Annotation placement.** A script pairing each annotation with the field declaration that
  immediately follows it (within its enclosing record) yields 253 pairs from the source and 247
  from the render, with **zero pairs present in the render but absent from the source**. The 6
  unmatched pairs are all in `InlineResponse200` and are a limitation of my extraction regex
  (fields typed `record {|anydata...;|}[]`), not a render defect — manual comparison of the full
  `InlineResponse200` body shows all 8 annotations present and correctly attached
  (`types.bal:~950` region vs render `type InlineResponse200 record`).
- **`@display` recovery.** `types.bal:289` `@display {label: "Connection Config"}` on
  `ConnectionConfig`. Present in `new` (line 637), absent in `old` (`grep` found no `@display` in
  `old`).
- **Client signatures.** All 17 resource functions in `client.bal` (lines 41–236) appear in both
  renders with matching accessor, path, payload type and return type. Verified path/accessor set:
  `get analytics`, `get|post availability`, `get|delete|patch availability/[availabilityId]`,
  `get events`, `get|delete|patch events/[eventId]`, `get|post schedules`,
  `get|delete|patch schedules/[scheduleId]`, `post schedules/single_use_link`,
  `get users/[userId]`. `init` signature matches `client.bal:31` modulo the `public isolated`
  qualifiers, which the renderer drops on both sides.
- **Quoted keyword identifiers** are preserved: `string 'from?;` in `ListSchedulesQueries` and
  `ReportAnalyticsQueries` renders as `string 'from?;` (3 occurrences, same in both).

## 4. Regressions

**None found.**

What I checked to conclude this:

- Full `diff -u old new` was inspected in its entirety after filtering out annotation-only
  additions; the residual set is exactly 3 `// Unknown type:` → `type … string;` replacements and
  11 client-method lines whose only textual change is deletion of `anydata Additional Values, `.
  No other line is removed or altered anywhere in the file.
- Declaration name sets (`^type \w+`) — `comm` shows nothing in `old` that is not in `new`.
- Doc-comment line count identical (505 = 505), so no documentation was dropped.
- README block (lines 7–170) `diff`s clean.
- `// Special Agent Note:` cross-package hints: 17 on both sides.
- JSON: typeDef name symmetric difference is empty; client function count 18 = 18.

The single piece of information `new` no longer carries is the `Additional Values` pseudo-parameter,
which signalled that the included query record is an open record. I do not count this as a
regression: it was rendered as `anydata Additional Values` — an identifier containing a space, i.e.
syntactically invalid Ballerina that could only mislead a consumer — and the openness of the query
records is still fully expressed by the rendered record definitions themselves.

## 5. Issues in `new` (independent of `old`)

All of the following are present **identically in `old`** (they do not appear in the diff), so they
are renderer-wide characteristics, not spec-v2 defects. Listed because they affect the quality of
what an LLM consumes:

1. **Included-record parameters are both flattened and duplicated.** Source
   (`client.bal:41`) is `resource isolated function get analytics(map<string|string[]> headers = {},
   *ReportAnalyticsQueries queries)`. Both renders emit
   `resource function get analytics(map<string|string[]> headers = {}, string userId = "",
   string from = "", string to = "", string timeZone = "", ReportAnalyticsQueries queries)` —
   the record's fields flattened as defaulted params **and** the record itself as a trailing
   required param. This is non-compiling twice over (required parameter after defaulted ones; the
   same arguments expressible two ways) and could lead a model to call
   `->/analytics(queries = {...})`, which the real API does not accept. Affects 11 methods.
2. **`from` emitted unquoted in parameter lists.** `string from = ""` appears 3 times
   (`get analytics`, `get events`, `get schedules`); `from` is a Ballerina keyword and must be
   `'from`. The renderer gets this right inside record bodies (`string 'from?;`) but not in
   parameter lists.
3. **Field default values are erased and required-with-default fields become optional.**
   `ConnectionConfig` in source has `http:HttpVersion httpVersion = http:HTTP_2_0;`,
   `decimal timeout = 30;`, `boolean validation = true;`, etc.; both renders emit
   `http:HttpVersion httpVersion?;`, `decimal timeout?;`, `boolean validation?;`. The defaults are
   lost entirely.
4. **Closed records rendered as open.** `public type ConnectionConfig record {| … |}` renders as
   `record { … }`. Source has 2 `record {|` occurrences; render has 9, all inline
   `record {|anydata...;|}` (the rendering of source's `record {}`), so the closed/open
   distinction is not conveyed.
5. **Multi-line doc comment continuation loses its `#` prefix.** `new` line 676 reads
   `and absent fields are handled as `nilable` types. Enabled by default.` at column 0 — a bare
   sentence outside any comment, which breaks the syntactic validity of the render. Same in `old`.
6. **`public` and `isolated` qualifiers dropped** on the client class, `init`, all resource
   functions, and all types. Source: `public isolated client class Client` (`client.bal:24`).
7. Non-ASCII characters (`→`, `’`) pass through at lines 29, 1217, 1467 — correct UTF-8, no
   mojibake; noted only for completeness.

## 6. Coverage gaps vs. the library

**Zero gaps.**

The package exports exactly one module, `zoom.scheduler`, which is the default module
(`package.json` `"export": ["zoom.scheduler"]`; `modules/` contains only `zoom.scheduler`). There is
no submodule API, so the known `getDefaultModule()`-only limitation is inert here.

Public symbols in the bala's default module:

| Symbol kind | count in bala | in `new` render | in `old` render |
|---|---|---|---|
| `public type` (types.bal) | 67 | 67 | 67 (3 as `// Unknown type:` placeholders) |
| `public isolated client class Client` | 1 | 1 | 1 |
| Client `init` + resource functions | 18 | 18 | 18 |

`comm` between the bala's 67 `public type` names and the render's 67 `type` names is empty in both
directions. Everything else in the module (`utils.bal`'s 6 functions, `enum EncodingStyle`) is
module-private (no `public` qualifier) and correctly excluded.

## 7. Compiler plugin

The package has **no compiler plugin**: `Ballerina.toml` contains no `[[plugin]]` /
`compiler-plugin` entry, there is no `compiler-plugin/` directory in the repo at `v1.0.2`, and the
bala's `any/` directory contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json` — no `compiler-plugin/compiler-plugin.json`. Nothing plugin-derived is therefore
expected in the render, and nothing is missing.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/zoom.scheduler/1.0.2` returns
  `deprecated: None`, `deprecateMessage: ""`, `visibility: public`, `pullCount: 48`.
  Built with `ballerina_version 2201.12.7`, `graalvmCompatible: true`.
- **Stable version** (1.0.2, post-1.0), so no pre-release caveats.
- **Size/token implications:** +254 lines (+17.9%) for the annotation recovery. This is a
  worthwhile trade — the `@jsondata:Name` mappings are the only place the render states the actual
  wire field names (`time_zone`, `custom_field_id`, …), without which generated code would
  serialize wrong; and the `@constraint:*` annotations carry validation limits (e.g.
  `duration` 15–1440, `capacity` 1–200, `slug` length 3–256) that are otherwise unavailable.
- **Doc quality:** the library's own doc comments are dense and per-field; both renders carry all
  505 of them.
- **Type naming** in the library itself is poor (`InlineResponse2011CustomFieldsAnswerchoicesItemsString`,
  `SchedulerschedulesscheduleIdSegmentsRecurrence1`) — an OpenAPI-generation artifact, not a render
  problem, but it does make the render harder for a model to reason about.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 1419, new 1673 |
| 2 | `grep -c '^// Unknown type:'` | old 3, new 0 |
| 3 | `grep -n '^// Unknown type:' old` | lines 326, 406, 545 |
| 4 | `grep -n '^// --- '` | both: README 7, END README 170, Types 172; Client old 1346 / new 1600 |
| 5 | `git ls-remote --tags <repo>` | tags v1.0.0, v1.0.1, v1.0.2; exact match `v1.0.2` |
| 6 | `git clone --depth 1 --branch v1.0.2` | succeeded, commit `8ea190c` |
| 7 | `diff bala/modules/zoom.scheduler/{client,types,utils}.bal src/ballerina/…` | CLIENT_SAME, TYPES_SAME, UTILS_SAME |
| 8 | `ls bala/any/modules/` | single module `zoom.scheduler` (client.bal, types.bal, utils.bal) |
| 9 | `diff -u old new \| grep -c '^@@'` | 42 hunks |
| 10 | Added lines bucketed by leading token | `@jsondata:Name` 182, `@constraint:String` 28, `@http:Query` 24, `@constraint:Number` 19, `@display` 1, 3 type aliases, 11 resource fns = 268 |
| 11 | Removed lines enumerated | 3 `// Unknown type:` + 11 resource fns = 14 |
| 12 | `diff -u` filtered of annotation-only additions | residual = exactly the 14 removals + their 14 replacements; nothing else |
| 13 | `comm` on `^type \w+` name sets | only-old: ∅; only-new: the 3 aliases |
| 14 | `comm` bala `^public type` (67) vs new `^type` (67) | both directions empty |
| 15 | Per-annotation counts render vs `types.bal` | 182/182, 28/28, 19/19, 24/24, 1/1 |
| 16 | `diff` of sorted counted annotation-expression multisets | identical |
| 17 | Annotation→field pairing script | 253 source pairs, 247 render pairs, 0 render-only pairs; 6 deltas traced to regex miss on `record {|anydata...;|}[]`, manually confirmed correct |
| 18 | `grep -n -B4 '@display'` | source `types.bal:289`; new render line 637; **absent in old** |
| 19 | `types.bal:286,1073,1091` | the 3 `public type … string;` aliases confirmed |
| 20 | `grep -c '^\s*#'` doc lines | old 505, new 505 |
| 21 | `diff <(sed -n '7,170p' old) <(sed -n '7,170p' new)` | identical README |
| 22 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 0, new 0 (no version-qualified refs either side) |
| 23 | `grep -c 'resource function'` | old 17, new 17 |
| 24 | `grep -c 'Special Agent Note'` | old 17, new 17 |
| 25 | JSON: typeDefs/clients/services/functions/annotations lengths | 67/1/0/0/0 both sides; typeDef name symmetric difference ∅ |
| 26 | JSON: `…AnswerchoicesItemsString` typeDef | old `{"type":"Other"}`; new `{"type":"Other","baseType":"string"}` |
| 27 | JSON: total client parameter count | old 88, new 77 (11 × `Additional Values`) |
| 28 | JSON: `get /analytics` parameter list | old ends `('Additional Values','anydata'), ('queries','ReportAnalyticsQueries')`; new ends `('queries','ReportAnalyticsQueries')` |
| 29 | `client.bal:41` vs render | source `*ReportAnalyticsQueries queries`; both renders flatten + duplicate |
| 30 | `grep -c "string from"` / `"'from"` | 3 / 3 in each render (keyword unquoted in param lists on both sides) |
| 31 | `grep -c 'record {\|'` source vs new | 2 vs 9 (closed→open flattening, both sides) |
| 32 | `ConnectionConfig` source `types.bal:288–330` vs new render 635–676 | defaults `= http:HTTP_2_0`, `= 30`, `= "disable"`, `= {}`, `= true` all erased to `?`; broken doc continuation at new:676 — identical in old |
| 33 | `grep 'compiler-plugin' Ballerina.toml`; `ls bala/any/` | no plugin declared, no `compiler-plugin/` in bala |
| 34 | `bala/any/package.json` | export `["zoom.scheduler"]`, ballerina_version 2201.12.7, graalvmCompatible true |
| 35 | `GET api.central.ballerina.io/2.0/registry/packages/ballerinax/zoom.scheduler/1.0.2` | not deprecated, public, 1 module, pullCount 48 |
| 36 | `OLD_AND_NEW_DIFFS/zoom.scheduler_diff.md` header claims (+268/−14, 42 hunks, 3 added decls, 0 removed) | independently reproduced — all correct |

## 10. Caveats and unverified items

- Neither render was compiled or parsed with a Ballerina toolchain; syntax-validity claims in §5 are
  from reading the emitted text against the language rules, not from a compiler run.
- The annotation→field pairing check (evidence #17) used a regex-based extractor; 6 of 253 source
  pairs fell outside its match and were confirmed by manual inspection of `InlineResponse200`
  instead. No automated confirmation exists for those 6.
- I did not attempt to re-run the two-stage render pipeline to reproduce either artifact; the
  provenance of `old`/`new` is taken from the brief (`eb5d81b3` vs `412ba01e`) and was not
  independently verified.
- Section 5 items are asserted to be present in `old` on the basis that they do not appear in
  `diff -u old new`; this is sound but indirect for items 3–6, which I read only in the `new` file.

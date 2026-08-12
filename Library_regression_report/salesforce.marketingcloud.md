# ballerinax/salesforce.marketingcloud 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/salesforce.marketingcloud` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-salesforce.marketingcloud |
| Tag reviewed | `v1.0.2` (source tarball fetched via `gh api .../tarball/v1.0.2`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/salesforce.marketingcloud/1.0.2` |
| Old render | `1636` lines (69,318 bytes) |
| New render | `1675` lines (70,388 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three concrete gains, all verified against the
bala source:

1. All **38 annotation lines** present in the published source (`@http:Query`, `@jsondata:Name`,
   `@constraint:*`, `@display`) now appear in the render — `old` emitted **0**. The rendered set is
   byte-identical to the source set (`diff` on the sorted annotation lines is empty).
2. The single `// Unknown type: DataExtensionRowSet` placeholder in `old` is replaced by the real
   definition `type DataExtensionRowSet DataExtensionRow[];` with its doc comment — matching
   `types.bal:1016-1017`.
3. A **malformed, non-compiling pseudo-parameter** `anydata Additional Values` (note the space in the
   identifier) that `old` emitted in **14** client method signatures is gone in `new`. This came from
   the extractor (it is present in `old/*.json` as a parameter named `"Additional Values"` and absent
   from `new/*.json`), so `new` fixes it at the source, not just cosmetically.

No declaration, parameter, default, doc line, README byte or section marker was lost. The README
block (lines 1–147) is byte-identical between the two renders.

Several inaccuracies remain in `new`, but every one of them is also present in `old` — they are
shared extractor/renderer gaps, not regressions (section 5).

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 1636 | 1675 |
| Bytes | 69,318 | 70,388 |
| Section markers (`// --- `) | 4 | 4 (identical: README / END README / Types / Client) |
| `// Unknown type:` placeholders | 1 | 0 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 |
| `type X …` declarations | 93 | 94 |
| `typeDefs` in JSON | 94 | 94 |
| `client class` | 1 | 1 |
| `remote function` in render | 50 | 50 |
| client `functions` in JSON | 51 (incl. `init`) | 51 (incl. `init`) |
| Annotation lines | 0 | 38 |
| Lines with `Additional Values` | 14 | 0 |
| `# Special Agent Note` cross-package markers | 16 | 16 |

Diff totals: **+54 / −15 lines, 25 hunks**. Fully accounted for:

Added (54)
- 38 annotation lines: `@http:Query` ×25, `@jsondata:Name` ×8, `@constraint:Array` ×2,
  `@constraint:String` ×1, `@constraint:Int` ×1, `@display` ×1.
- 14 corrected `remote function` signatures (the `anydata Additional Values` parameter removed).
- 2 lines for `DataExtensionRowSet` (doc comment + `type` line).

Removed (15)
- 14 old `remote function` signatures containing `anydata Additional Values`.
- 1 `// Unknown type: DataExtensionRowSet` line.

Declarations added: 1 (`type DataExtensionRowSet`). Declarations removed: 0.
Type-name sets: the sorted set of 94 type names in `new` equals the sorted set of 94 public types in
the bala (`comm` both directions empty) and equals `old`'s 93 rendered types plus its 1 Unknown-type
name.

## 3. Correctness against library source

Upstream `v1.0.2` `ballerina/types.bal` and `ballerina/client.bal` are **byte-identical** to the bala's
`modules/salesforce.marketingcloud/types.bal` and `client.bal` (`diff` returned nothing), so GitHub and
the bala agree and either can be cited.

- **Annotations (the bulk of the change).** `grep -hE '^\s*@' bala/*.bal | sed 's/^ *//' | sort` yields
  38 lines; the same extraction on the `new` render yields 38 lines; `diff` between them is empty.
  Every annotation `new` adds is real, at the right field, with the right value. Spot-checked
  anchors: `types.bal:683` `@constraint:Array {maxLength: 1}` above `Goal[] goals?` in `Journey`;
  `types.bal:275,278,281` `@http:Query {name: "$orderBy"/"$page"/"$pageSize"}` in
  `GetCampaignsQueries`; `types.bal:287` `@jsondata:Name {value: "EventDefinitionKey"}` in `FireEvent`;
  `types.bal:419` `@display {label: "Connection Config"}` on `ConnectionConfig`.
- **`DataExtensionRowSet`.** `types.bal:1016-1017` is
  `# An array of data extension rows to be upserted` / `public type DataExtensionRowSet DataExtensionRow[];`.
  `new` renders exactly that (doc + `type DataExtensionRowSet DataExtensionRow[];`). The JSON shows the
  mechanism: both sides carry `"type": "Other"`, but `new` adds `"baseType": "DataExtensionRow[]"`,
  which the spec-v2 renderer uses instead of degrading to `// Unknown type:`.
- **`Additional Values` removal is correct.** No such parameter exists in `client.bal`. E.g.
  `client.bal:302` is
  `remote isolated function getCampaigns(map<string|string[]> headers = {}, *GetCampaignsQueries queries) returns CampaignList|error`.
  The 14 corrected signatures are exactly the 14 methods that take an included-record `*XQueries`
  parameter. Nothing else in those signatures changed (verified line-by-line in the diff hunks).
- **Method inventory.** `client.bal` declares 50 `remote isolated function`s plus `init`; the render
  shows 50 `remote function`s plus `init` on both sides. No method added, dropped or renamed.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full `diff -u old new`: all 15 removed lines are the 14 defective signatures and the 1 Unknown-type
  placeholder; the 14 replacements are the same signatures minus the bogus parameter (character-level
  comparison of each pair in the diff output).
- Type-name set `old ∪ {Unknown}` vs `new`: `diff` empty — nothing dropped.
- README region (lines 1–147) `diff`: identical.
- Section markers: 4 in both, same order.
- Doc comments: no `# ` doc line appears in the removed set.
- Defaults, return types and parameter names on the 14 changed methods: unchanged except for the
  removed pseudo-parameter.
- JSON level: `typeDefs` 94↔94, `clients[0].functions` 51↔51 — no extraction loss.

## 5. Issues in `new` (independent of `old`)

All six are also present in `old`; they are shared pipeline gaps, listed here because the brief asks
for inaccuracies in `new` regardless of `old`.

1. **Defaultable record fields are rendered as optional and their defaults are dropped.** 24 fields in
   `types.bal` have literal defaults (e.g. `types.bal:279 int page = 1;`, `types.bal:282 int pageSize = 50;`,
   `types.bal:263 boolean autoAddSubscriber = true;`, `types.bal:430 decimal timeout = 30;`). The render
   emits `int page?;`, `boolean autoAddSubscriber?;`, `decimal timeout?;`. The JSON is the source of the
   loss: the field carries `"optional": true` with no default key on both sides. An LLM reading the
   render cannot see the real default and will believe the field is merely optional.
2. **Closed records are rendered open.** 3 top-level `public type X record {|…|}` in the bala
   (including `ConnectionConfig`, `types.bal:420`) render as `record {` — 0 occurrences of
   `^type X record {|` in `new`. Inline anonymous `record {|anydata...;|}` fields are preserved.
3. **Included-record parameters are expanded *and* duplicated.** Source is
   `getCampaigns(map<…> headers = {}, *GetCampaignsQueries queries)`; the render emits
   `getCampaigns(map<…> headers = {}, string orderBy = "", int page = 0, int pageSize = 0, GetCampaignsQueries queries)`
   — the record's fields as individual params plus a trailing required-looking `queries` param with no
   default after defaulted params. This is not valid Ballerina and misrepresents the call shape.
4. **Fabricated defaults on those expanded parameters.** They are type-placeholders, not the real
   values: render `int page = 0` / `int pageSize = 0` vs source `= 1` / `= 50` (`types.bal:656,659`);
   render `boolean mostRecentVersionOnly = false` / `decimal specificApiVersionNumber = 0.0d` vs source
   `= true` / `= 1` (`types.bal:641,643`); render `JourneyStatus status = "Deleted"` and
   `1|5|7 statusid = 1` where the source fields are optional with **no** default
   (`types.bal:664`, `types.bal:549`). These are actively wrong values an LLM would copy.
5. **Reserved-word identifier not escaped in parameter position.** `deleteContact` renders
   `"ids"|"keys" type = "ids"`; `type` is a Ballerina keyword. The type definition gets it right
   (`type DeleteContactQueries { … "ids"|"keys" 'type?; }`, new render line 544), so the escaping is
   lost only when the field is flattened into a parameter list. (`string 'key` elsewhere is escaped
   correctly.)
6. **`public` / `isolated` qualifiers dropped.** Source `public isolated function init` and
   `remote isolated function …` render as `function init` / `remote function …`.

## 6. Coverage gaps vs. the library

**None.** The package exports exactly one module — `package.json` `"export": ["salesforce.marketingcloud"]`,
and Central lists a single module for `1.0.2` — which is the default module, so the
`getDefaultModule()`-only extraction loses nothing here.

- Public types: 94 in the bala (`grep -c '^public type ' types.bal`), 94 in `new`, set-equal
  (`comm -23` and `comm -13` both empty).
- Public remote methods: 50 in `client.bal`, 50 in `new` render; `init` present.
- The bala's default module contains no other public declaration kind: `grep -cE '^public (type|const|enum|class|isolated function|function|annotation|listener)'` over all four `.bal` files = 94, i.e. all public declarations are the 94 types (the client class and its methods live inside `client.bal`'s `isolated client class Client`).

## 7. Compiler plugin

The package has **no compiler plugin**. `find` for `*compiler-plugin*` over both the upstream v1.0.2
tree and the bala returns nothing; the bala root contains only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`. Nothing plugin-derived is therefore expected in, or missing
from, the render.

## 8. Other considerations

- Not deprecated (Central `deprecated: null`, `deprecateMessage: ""`). Built for `2201.12.0`.
- Version `1.0.2` is a released 1.x; no pre-1.0 instability caveat.
- Size impact is negligible: +39 lines / +1,070 bytes (+1.5%). The added annotations are high-value
  for an LLM — `@http:Query {name: "$page"}` etc. are the only place the wire-level parameter names
  (`$page`, `$orderBy`, `$filter`, `ContactKey`, `EventDefinitionKey`) appear, and `@constraint:*`
  carries validation limits (`maxLength: 36`, `maxValue: 8`) that exist nowhere else in the render.
- 16 `# Special Agent Note: … FROM ballerina/http package` markers are preserved unchanged on both
  sides.
- The `// --- Types ---` section is unsorted / not grouped, and every type is emitted without the
  `public` qualifier — consistent across both renders.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 1636, new 1675 |
| `wc -c` on both renders | old 69,318, new 70,388 |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -n '^// --- '` | both: lines 7/146/148 + Client (old 1431, new 1470) |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 0, new 0 |
| `diff -u old new \| grep -c '^+[^+]' / '^-[^-]'` | +54 / −15 |
| Diff-line classification (awk) | added = 38 annotations + 14 methods + 2 type lines; removed = 14 methods + 1 Unknown |
| `grep -c 'Additional Values'` | old 14, new 0 |
| `grep -c '^\s*@'` | old 0, new 38 |
| `diff <(annots from bala) <(annots from new)` | empty — ANNOTATIONS_IDENTICAL, 38 each |
| Annotation kind counts, bala vs new | `@constraint:Array` 2/2, `@constraint:Int` 1/1, `@constraint:String` 1/1, `@http:Query` 25/25, `@jsondata:Name` 8/8, `@display` 1/1 |
| `diff <(sed -n 1,147p old) <(sed -n 1,147p new)` | identical (README block) |
| `grep -c '^public type ' bala/types.bal` | 94 |
| `comm` of bala type names vs new type names | both directions empty |
| `diff` of old type-name set (incl. Unknown) vs new | empty |
| `grep -cE '^\s+(remote\|resource) …function ' bala/client.bal` | 50 |
| `grep -cE '^\s+remote function ' render` | old 50, new 50 |
| JSON key counts (python) | both: typeDefs 94, clients 1, functions 0, services 0, annotations 0; `clients[0].functions` 51 |
| JSON `DataExtensionRowSet` entry | old `{"type":"Other"}`; new `{"type":"Other","baseType":"DataExtensionRow[]"}` |
| JSON `getCampaigns` params | old has param `"Additional Values"` (`anydata`); new does not; all other params byte-identical |
| `gh api …/tags` | `v1.0.2`, `v1.0.1`, `v1.0.0` → exact tag `v1.0.2` exists |
| `gh api …/tarball/v1.0.2` → `diff ballerina/types.bal bala/types.bal` | identical |
| `diff ballerina/client.bal bala/client.bal` | identical |
| `bala/…/types.bal:1016-1017` | `# An array of data extension rows to be upserted` / `public type DataExtensionRowSet DataExtensionRow[];` |
| `bala/…/client.bal:302` | `remote isolated function getCampaigns(map<string\|string[]> headers = {}, *GetCampaignsQueries queries) returns CampaignList\|error` |
| `grep -nE '^    \w+ \w+ = ' bala/types.bal \| wc -l` | 24 defaultable fields; all render as `?` in both |
| `grep -c 'record {|' bala/types.bal` vs `grep -cE '^type \w+ record \{\|' new` | 3 vs 0 |
| `grep -n '"ids"\|"keys" type' old new` | present in both (unescaped keyword `type`) |
| `package.json` export list | `["salesforce.marketingcloud"]` — single default module |
| `find` for `*compiler-plugin*` (upstream + bala) | no matches |
| Central API `…/ballerinax/salesforce.marketingcloud/1.0.2` | `deprecated: null`, 1 module, ballerinaVersion 2201.12.0 |
| `OLD_AND_NEW_DIFFS/salesforce.marketingcloud_diff.md` | its figures (1636/1675, +54/−15, 25 hunks, Unknown 1→0, 1 declaration added) all reproduced independently |

## 10. Caveats and unverified items

- `git clone` to github.com timed out in this environment (port 443, 75 s); the upstream source was
  obtained instead via `gh api repos/…/tarball/v1.0.2`, which resolves the same tagged commit. Tag
  existence was confirmed via `gh api …/tags`. This does not affect any finding — the tarball's
  `types.bal`/`client.bal` are byte-identical to the bala, which is authoritative anyway.
- Correctness of the 38 added annotations was verified exhaustively (set-level `diff` against the
  bala), but their *placement* was spot-checked on 4 records rather than all 38 sites; the diff hunks
  show each annotation immediately above the field whose doc comment precedes it, so placement drift
  is unlikely but not machine-verified for every one.
- Whether the render is intended to reproduce `public`/`isolated` qualifiers, closed-record `{|…|}`
  markers, or field defaults is a design question about the renderer that I could not settle from
  these artifacts; they are reported as inaccuracies vs. the source, not as intended behaviour.

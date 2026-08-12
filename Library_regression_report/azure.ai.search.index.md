# ballerinax/azure.ai.search.index 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/azure.ai.search.index` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-azure.ai.search.index |
| Tag reviewed | `v1.0.2` (commit `45cc0489`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/azure.ai.search.index/1.0.2` |
| Old render | `831` lines |
| New render | `833` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library is a single-module, OpenAPI-generated Azure AI Search "index/documents" connector:
1 client class with 10 methods (`init` + 9 remote functions) and 56 public types, all in the
default module `azure.ai.search.index`. Upstream `v1.0.2` sources (`ballerina/client.bal`,
`types.bal`, `utils.bal`) are byte-identical to the bala, so GitHub and the bala agree.

Both renders contain the identical declaration set: 56 types, 1 client, 10 client functions,
0 `// Unknown type:` placeholders, identical header + README block (lines 1–107 diff-clean),
identical `readme` and `description` JSON fields. The only differences between `old` and `new`
are three renderer improvements:

1. 16 version/module-qualified type references normalized (`ballerina/lang.int:0.0.0:Signed32`
   → `int:Signed32`; `record {|ballerinax/azure.ai.search.index:1.0.2:FacetResult[]...;|}` →
   `record {|FacetResult[]...;|}`).
2. A fabricated, non-parsable parameter `anydata Additional Values` removed from all 9 remote
   functions.
3. Two annotations now surfaced that `old` dropped entirely: `@display {label: "Connection
   Config"}` on `ConnectionConfig` and `@constraint:Int {minValue: 700}` on
   `DocumentsSearchGetQueries.semanticMaxWaitInMilliseconds`.

No declaration, field, parameter, default, return type or doc string was lost. No regressions found.

## 2. Change inventory

Line counts: `old` 831, `new` 833 (`wc -l`). Diff: 14 hunks, +27 / −25 lines.

| Kind | old | new | delta |
|---|---|---|---|
| Type definitions (`^type `) | 56 | 56 | 0 |
| Client classes (JSON `clients`) | 1 | 1 | 0 |
| Client functions (JSON) | 10 | 10 | 0 |
| Module-level functions (JSON `functions`) | 0 | 0 | 0 |
| Services / listeners (JSON `services`) | 0 | 0 | 0 |
| Module annotations (JSON `annotations`) | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| `// Special Agent Note` cross-module notes | 14 | 14 | 0 |

Declarations added: **0**. Declarations removed: **0**. Sorted type-name sets are identical
(`diff old_types.txt new_types.txt` → empty).

### Modified (all 17 JSON-level field deltas, enumerated)

**A. Type-reference normalization (16 fields)** — same underlying type, unqualified in `new`:

`SuggestRequest.top`, `DocumentsSuggestGetQueries.$top`, `IndexingResult.statusCode`,
`SearchRequest.skip`, `SearchRequest.top`, `SearchRequest.semanticMaxWaitInMilliseconds`,
`VectorQuery.k`, `DocumentsSearchGetQueries.semanticMaxWaitInMilliseconds`,
`DocumentsSearchGetQueries.$skip`, `DocumentsSearchGetQueries.$top`, `AutocompleteRequest.top`,
`DocumentsAutocompleteGetQueries.$top`, `docs_search_post_search_body.skip`,
`docs_search_post_search_body.top`, `docs_search_post_search_body.semanticMaxWaitInMilliseconds`
(all `ballerina/lang.int:0.0.0:Signed32[?]` → `int:Signed32[?]`), plus
`SearchDocumentsResult.@search.facets`
(`record {|ballerinax/azure.ai.search.index:1.0.2:FacetResult[]...;|}` → `record {|FacetResult[]...;|}`).

**B. Annotation now captured (2 places, +2 render lines)**

- `ConnectionConfig` gains `@display {label: "Connection Config"}` (new render line 252).
- `DocumentsSearchGetQueries.semanticMaxWaitInMilliseconds` gains `@constraint:Int {minValue: 700}`
  (new render line 595).

JSON confirms: `old` has zero annotations on any typeDef or field; `new` has exactly these two.

**C. Client signatures (9 of 10 functions)**

Every remote function lost the parameter literally named `Additional Values` of type `anydata`
(JSON parameter-name diff: `OLD-ONLY ['Additional Values']` for all 9; `init` unaffected).
Nothing else changed in any signature — parameter order, names, types, defaults and return types
are otherwise byte-identical.

## 3. Correctness against library source

Upstream clone `git clone --depth 1 --branch v1.0.2` → `ballerina/{client.bal,types.bal,utils.bal}`
are `diff -q`-identical to the bala's `modules/azure.ai.search.index/*.bal`. All checks below cite
the bala (= upstream).

- `types.bal:396–397` — `@constraint:Int {minValue: 700}` immediately above
  `int:Signed32 semanticMaxWaitInMilliseconds?;` inside `DocumentsSearchGetQueries`. `new` render
  line 595–596 reproduces both lines exactly. `constraint` is the only such annotation in the
  package (`grep -n constraint types.bal` → lines 4, 163, 396 — the first is the import, the
  second a doc comment), so `new` captures 1/1.
- `types.bal:129` — `@display {label: "Connection Config"}` is the only `@display` in the package
  (`grep -n '@display' *.bal` → one hit). `new` render line 252 reproduces it exactly. 1/1.
- `types.bal:211` — `record {|FacetResult[]...;|} \@search\.facets?;`. `new` render line 345 is
  character-identical; `old` carried the version-qualified form.
- `types.bal:341` (`SearchRequest`) and `types.bal:397` — `int:Signed32? …` / `int:Signed32 …`.
  `new` matches; `old` rendered `ballerina/lang.int:0.0.0:Signed32`, which is not a writable
  Ballerina type reference.
- `types.bal:355–358` — `DocumentsCountQueries` has exactly one field, `string api\-version;`
  (required, open record, no rest descriptor declared). This is the record whose implicit
  openness produced `old`'s `anydata Additional Values`.
- `client.bal:8` — `public isolated client class Client`; `client.bal:15` `init(string serviceUrl,
  ConnectionConfig config = {})`. Render: `client class Client` / `function init(string serviceUrl,
  ConnectionConfig config = {}) returns error?` — names, order and the one default match.
- `client.bal:26,38,52,68,82,96,111,126,140` — the 9 remote functions, each declared
  `remote isolated function <name>(… headers = {}, *<Op>Queries queries) returns <T>|error`.
  All 9 names, payload/`'key` positional params, and return types match both renders exactly;
  only `new` drops the bogus extra parameter.
- Type-name set: `grep '^public type' types.bal` → 56 names; identical (sorted `diff`) to the 56
  type names in `new`, and to the 56 in `old`.

Everything `new` adds or changes is confirmed present in the pinned source with the shown form.

## 4. Regressions

**None found.**

Checked, and each came back clean:

- Declaration set: sorted `^type ` name lists from both renders are identical (`diff` empty), and
  both equal the 56 `public type` names in `types.bal`.
- Field-level: a structural JSON walk over all 56 typeDefs comparing every field's every key
  (name, type, description, defaultValue, optional, annotations) reported 17 deltas — all are the
  improvements listed in §2 (16 de-qualifications + 1 added annotation). Zero fields removed, zero
  descriptions changed, zero defaults changed, zero `optional` flags changed.
- Client: 10/10 functions on both sides, same names; per-function parameter-name lists differ only
  by the removal of `Additional Values`; return types unchanged.
- Docs/README: render lines 1–107 (banner, import line, README block, `--- END README ---`) are
  diff-identical between `old` and `new`; JSON `readme` and `description` compare equal, and the
  JSON `readme` is an exact match for the bala's `docs/README.md` (3559 chars both).
- Degradation markers: `// Unknown type:` count is 0 in both; `// Special Agent Note` count is 14
  in both.
- The one thing `new` deletes (`anydata Additional Values`) is not a loss of accurate information:
  the identifier contains a space, so the `old` signature could never parse as Ballerina, and it
  appeared for records like `DocumentsCountQueries` that declare no rest field. Its removal makes
  the signature closer to valid, not less informative. See §5.2 for the residual nuance.

## 5. Issues in `new` (independent of `old`)

These are inaccuracies present in `new`; all except 5.4 are shared with `old` and stem from the
renderer's general handling, not from spec v2.

**5.1 Included-record parameters are expanded AND duplicated, producing non-compiling signatures.**
Source uses `*DocumentsSearchGetQueries queries`. Both renders expand every field of the included
record into a positional defaulted parameter and *then* append a required parameter
`DocumentsSearchGetQueries queries`. A required parameter after defaultable parameters is invalid
Ballerina, and the duplication (27 expanded params plus the record itself in `documentsSearchGet`)
can mislead a consumer into passing the arguments twice. Affects all 9 remote functions.

**5.2 The included open record's rest parameter is now unrepresented.** `old`'s `anydata Additional
Values` was malformed but did correspond to a real thing: including an open record contributes an
additional-values rest parameter. `new` emits nothing in its place. Net positive (invalid syntax
gone) but the concept is now invisible; ideally it would render as `anydata... additionalValues`.

**5.3 Invented default values for required and non-defaulted fields.** `api\-version` is a
*required* field of every `*Queries` record (`types.bal:357` etc., no `?`), yet both renders show
`string api\-version = ""` in all 9 signatures (9 occurrences in each file). Likewise optional
fields with no source default are rendered with synthesized defaults (`int:Signed32 $top = 0`,
`string[] facet = []`, `decimal minimumCoverage = 0.0d`). An LLM reading this would conclude
`api-version` is omittable, which it is not.

**5.4 `@constraint:Int` is emitted with a module prefix but no import and no cross-module note.**
The renderer annotates foreign types with `// Special Agent Note: X FROM ballerina/http package`
(14 such notes), but the new `@constraint:Int` line at new:595 carries no equivalent note and the
render has no `import ballerina/constraint;`. Cosmetic/consistency only — the JSON does record
`module: ballerina/constraint`. `@display` needs no import, so it is unaffected.

**5.5 Qualifiers dropped on the client.** Source is `public isolated client class Client` with
`remote isolated function`s; both renders emit `client class Client` and `remote function`.
Isolation is user-visible API in Ballerina. Shared with `old`, renderer-wide convention.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `export` lists exactly one module: `azure.ai.search.index`; `dependency-graph.json`
  lists one `ballerinax` module entry. There are no submodules, so the known default-module-only
  extraction limitation costs this library nothing.
- Public symbols in the bala's default module: `grep -hoE '^public [a-z ]+' *.bal | sort | uniq -c`
  → 56 `public type` (55 + 1 `public type docs_search_post_search_body` matched separately) and
  1 `public isolated client class`. `utils.bal` has 0 public declarations. There are no public
  constants, enums, listeners, services or module-level functions.
- All 56 types and the client appear in both renders. Nothing exported is missing from either.

## 7. Compiler plugin

The package ships no compiler plugin. The bala root contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/` directory and no `compiler-plugin.json`. The upstream repo at `v1.0.2` has no
`*compiler-plugin*` directory either. Nothing plugin-implied is therefore missing from the render.

The only "plugin-like" behaviour is `ballerina/constraint` (a dependency at 1.7.0), whose
`@constraint:Int` annotation drives runtime payload validation. `new` now surfaces that annotation;
`old` did not — so `new` is strictly better on this axis.

## 8. Other considerations

- Size is unchanged for practical purposes: 831 → 833 lines (+0.24%). Token impact negligible;
  the de-qualification actually shortens 16 lines.
- Central reports `pullCount` 3157, `ballerinaVersion` 2201.12.0, no `deprecated` field in the
  1.0.2 payload. Package is post-1.0 and stable.
- `Ballerina.toml` declares `distribution = "2201.9.3"` while the published `package.json` says
  `ballerina_version: 2201.12.0` — normal (built with a newer distribution), no render impact.
- Doc quality is good: every rendered field carries the OpenAPI-derived description; the README
  block (99 lines) includes Overview, setup and Quickstart and is reproduced verbatim.
- Escaped identifiers (`\$top`, `\@search\.facets`, `api\-version`) round-trip correctly in both
  renders and match the source escaping exactly.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 831 / 833 |
| 2 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 3 | `grep -n '^// --- '` both | 4 markers each; Client section 790 (old) / 792 (new) |
| 4 | `diff -u old new` | 14 hunks, +27/−25, contents as quoted in §2 |
| 5 | `ls -R <bala>` | `docs/`, `modules/azure.ai.search.index/{client,types,utils}.bal`, `package.json`, `dependency-graph.json`; no `compiler-plugin/` |
| 6 | `wc -l <bala>/modules/.../*.bal` | client 147, types 584, utils 203 |
| 7 | `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1`, `v1.0.2` → tag `v1.0.2` = `45cc0489` |
| 8 | `git clone --depth 1 --branch v1.0.2` then `diff -q` per file vs bala | client.bal, types.bal, utils.bal all identical |
| 9 | `grep -n constraint types.bal` | lines 4 (import), 163 (doc text), 396 (`@constraint:Int {minValue: 700}`) |
| 10 | `grep -n '@display' *.bal` | types.bal:129 only |
| 11 | `grep -n 'semanticMaxWaitInMilliseconds' types.bal` | 341, 397 |
| 12 | `grep -n 'facets' types.bal` | 211 `record {\|FacetResult[]...;\|} \@search\.facets?;` |
| 13 | `grep -n -A3 'type DocumentsCountQueries' types.bal` | 355–358, single required field `string api\-version;` |
| 14 | `grep -oE '^public type …' types.bal \| sort` vs `grep -oE '^type …'` on both renders | 56 = 56 = 56; both `diff`s empty |
| 15 | `grep -hoE '^public [a-z ]+' *.bal \| sort \| uniq -c` | 55 `public type`, 1 `public type docs…`, 1 `public isolated client class`; utils.bal 0 |
| 16 | Python JSON walk: top-level keys, list lengths | both `{annotations:0, services:0, functions:0, typeDefs:56, clients:1}` |
| 17 | Python JSON walk: per-typeDef, per-field key comparison | 17 deltas — 16 type de-qualifications + 1 added `constraint:Int` annotation; 0 removals |
| 18 | Python JSON walk: type-level annotations | old `[]`; new `ConnectionConfig→display`, `DocumentsSearchGetQueries.semanticMaxWaitInMilliseconds→constraint/Int` |
| 19 | Python JSON: client function names + parameter names | 10/10 both; `Additional Values` OLD-ONLY in all 9 remote functions |
| 20 | Python: `old.readme == new.readme`, `old.description == new.description` | True / True |
| 21 | Python: `new.readme.strip() == bala docs/README.md.strip()` | True (3559 chars both) |
| 22 | `diff <(sed -n '1,107p' old) <(sed -n '1,107p' new)` | empty — header + README identical |
| 23 | `grep -c 'Special Agent Note'` both | 14 / 14 |
| 24 | `grep -o 'api[^ ]*-version = ""' \| wc -l` both | 9 / 9 |
| 25 | `grep -n 'constraint:' new/*.bal.txt` | single hit, line 595, no accompanying note |
| 26 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/azure.ai.search.index/1.0.2` | one module, `ballerinaVersion 2201.12.0`, `pullCount 3157`, no `deprecated` key |
| 27 | `package.json` `export` + `dependency-graph.json` modules | single module `azure.ai.search.index`; deps constraint 1.7.0, data.jsondata 1.1.3, http 2.14.9, url 2.6.1 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific rendered signatures are non-compiling (§5.1,
  §5.3) are based on reading the Ballerina rules (required params may not follow defaultable ones;
  a required record field is not omittable), not on running `bal build` over the render — the
  render is not a compilable artifact in the first place.
- The pinned-version equality of the two renders' inputs is taken from the brief (`PIN_OK` on both
  sides); I independently confirmed only that the bala on disk is 1.0.2 and that both renders name
  `ballerinax/azure.ai.search.index:1.0.2` (the `old` render's version-qualified `FacetResult`
  reference embeds `1.0.2`, corroborating it).
- The Central API response for 1.0.2 contains no `deprecated` field; I read its absence as
  "not deprecated" rather than verifying deprecation status through a second channel.
- I did not inspect the two `ballerina-vscode` source trees themselves; attribution of each change
  to spec v2 is inferred from the render/JSON evidence plus the brief's description.

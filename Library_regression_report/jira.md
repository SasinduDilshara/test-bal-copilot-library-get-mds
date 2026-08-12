# ballerinax/jira 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/jira` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-jira |
| Tag reviewed | `v2.0.2` (commit `62741eab`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/jira/2.0.2/any` |
| Old render | `16649` lines |
| New render | `16749` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The bala at 2.0.2 is byte-identical to the GitHub tag `v2.0.2` (`diff -q` on all three
`.bal` files: IDENTICAL), so the upstream source is authoritative here and both agree.

`new` is strictly better than `old` on every axis measured:

- **6 degraded `// Unknown type:` placeholders become real definitions.** The rendered
  top-level type-name set in `new` is now an exact match for the 1103 `public type`
  declarations in the bala (`comm` both directions returns empty). `old` was missing 6.
- **240 malformed `anydata Additional Values` pseudo-parameters are gone.** That token
  contains a space inside an identifier and could never compile; it appeared in 240 of the
  591 client resource-function signatures in `old` and in 0 in `new`.
- **290 version-qualified type references are normalised** (265 `ballerina/lang.int:0.0.0:Signed32`
  → `int:Signed32`, 25 `ballerinax/jira:2.0.2:X` → `X`). `new` has 0 remaining
  `mod:x.y.z:Type` refs.
- **100 annotation lines are added, and all 100 match the bala exactly** (66 `@constraint:String`,
  14 `@jsondata:Name`, 11 `@constraint:Array`, 5 `@constraint:Int`, 3 `@http:Header`,
  1 `@display`) — the same per-annotation counts as `grep` over the bala's `types.bal` +
  `client.bal`.
- **No declaration is removed and no client signature changes.** After normalising away the
  two `old`-only artifacts, the 591 client function signatures are byte-identical between
  the two renders (`diff` → 0 lines).

No regressions found. The residual inaccuracies listed in §5 are all present identically in
`old`, i.e. they are pre-existing extractor limitations, not introduced by spec v2.

## 2. Change inventory

Mechanical totals (`diff -u old new`): 407 hunks, +637 lines, −537 lines.

### Top-level declarations

| Kind | old | new | delta |
|---|---|---|---|
| `type` (top-level) | 1097 | 1103 | **+6** |
| `client class` | 1 | 1 | 0 |
| client `function init` | 1 | 1 | 0 |
| client `resource function` | 590 | 590 | 0 |
| `// Unknown type:` placeholders | 6 | 0 | **−6** |
| section markers `// --- ` | 4 | 4 | 0 |

Declarations added (6) — all previously emitted as `// Unknown type:` stubs:

```
type BulkGetUsersQueriesAccountIdItemsString string;                            (@constraint:String {maxLength: 128})
type CreatePrioritySchemeDetailsPriorityIdsItemsInteger int;
type GetUserEmailBulkQueriesAccountIdItemsString string;                        (@constraint:String {maxLength: 128})
type GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString string;  (@constraint:String {maxLength: 20})
type GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString string; (@constraint:String {maxLength: 50})
type JqlQueriesToParseQueriesItemsString string;                                (@constraint:String {minLength: 1})
```

Declarations removed: **0**.

### Classification of every changed line

Removed lines (537) — 100 % accounted for, categories are disjoint (25+265+240+6+1 = 537):

| Category | count | nature |
|---|---|---|
| `ballerina/lang.int:0.0.0:Signed32 …` record fields | 265 | replaced by `int:Signed32 …` |
| resource-fn lines carrying `anydata Additional Values` | 240 | replaced by the same line without that token |
| `ballerinax/jira:2.0.2:X` qualified refs (union aliases, `record {\|X...;\|}` rest types) | 25 | replaced by bare `X` |
| `// Unknown type: …` | 6 | replaced by real definitions |
| `    # The index of the last item returned on the page` | 1 | **diff-alignment artifact only** — the identical line is re-added 3 lines later in the same hunk (`full.diff:1560` removed, `full.diff:1563` added). No doc text is actually lost. |

Added lines (637): 101 contain an annotation (100 annotation lines + 1 line that is a
re-emitted doc comment), the remaining 536 are the normalised replacements above plus the
6 new type declarations.

### JSON-level change

Both JSONs carry 1103 `typeDefs`, 1 client with 591 functions, 0 top-level functions/services,
and an empty library-level `annotations` array. `new` adds two fields to the typeDef schema:
`baseType` (populated on 6 typeDefs) and `annotations` (populated on 6 typeDefs + 94 record
fields = 100, exactly the 100 annotation lines rendered).

README section (lines 1–113) is byte-identical between the two renders.

## 3. Correctness against library source

Everything `new` adds was checked against the bala / tag source. All confirmed.

| Item in `new` | Source evidence | Result |
|---|---|---|
| `type BulkGetUsersQueriesAccountIdItemsString string;` + `@constraint:String {maxLength: 128}` | `ballerina/types.bal:555-556` | exact match |
| `type GetWorkflowTransitionRuleConfigurationsQueriesWithTagsItemsString string;` + `{maxLength: 20}` | `types.bal:1898-1899` | exact match |
| `type GetWorkflowTransitionRuleConfigurationsQueriesWorkflowNamesItemsString string;` + `{maxLength: 50}` | `types.bal:2649-2650` | exact match |
| `type JqlQueriesToParseQueriesItemsString string;` + `{minLength: 1}` | `types.bal:2965-2966` | exact match |
| `type GetUserEmailBulkQueriesAccountIdItemsString string;` + `{maxLength: 128}` | `types.bal:8332-8333` | exact match |
| `type CreatePrioritySchemeDetailsPriorityIdsItemsInteger int;` (no annotation) | `types.bal:4478` — source has no annotation on it either | exact match |
| `UserList`: `@jsondata:Name {value: "end-index"/"max-results"/"start-index"}` on `int:Signed32 endIndex?/maxResults?/startIndex?` | `types.bal:7890-7904` | field order, names, values and annotation placement all identical |
| `UpdateIssueSecurityLevelDetails`: `@constraint:String {maxLength: 255}` on `description?`, `{maxLength: 60}` on `name?` | `types.bal:5352-5358` | exact match |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:10034` | exact match, 1 occurrence in source and 1 in render |
| `@http:Header {name: "Atlassian-Transfer-Id"}` ×3 | `types.bal:835, 7473, 12084` | 3 in source, 3 in render |
| `@constraint:Array` ×11, `@constraint:Int` ×5, `@constraint:String` ×66, `@jsondata:Name` ×14 | `grep -c` over bala `types.bal`+`client.bal` | per-annotation counts identical |
| `record {\|ProjectCreateResourceIdentifier...;\|} explicitMappings?;` ×3 | `types.bal:2125, 4096, 6992` | exact match (`old` wrote `record {\|ballerinax/jira:2.0.2:ProjectCreateResourceIdentifier...;\|}`) |
| `int:Signed32 size?/endIndex?/maxResults?/startIndex?` | `types.bal:7892, 7895, 7898, 7901` | matches source spelling; `old`'s `ballerina/lang.int:0.0.0:Signed32` does not |
| Type-name set (1103) | `comm -23` and `comm -13` of render type names vs. `^public type` names in `types.bal` | both empty — no invented symbol, no missing type |
| 591 client functions | `diff` of normalised signature lists | 0 differing lines |
| `function init(ConnectionConfig config, string serviceUrl = "https://your-domain.atlassian.net/rest") returns error?` | `client.bal:32` | matches (bar the dropped `public isolated`) |

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

1. Full-file `diff -u` (407 hunks) with every one of the 537 removed lines classified into
   the 5 categories in §2 — none of them is a lost declaration, lost doc, lost parameter,
   lost default value, or lost annotation. The single "lost doc line" is a diff-alignment
   artifact re-added in the same hunk (verified at `full.diff:1560` / `:1563`).
2. Declaration-set diff (`decl_old.txt` 1099 lines vs. `decl_new.txt` 1105): 6 additions,
   **0 removals**.
3. Rendered top-level type-name sets: `old` 1097, `new` 1103, `comm -23 rt_old rt_new` is
   empty (nothing in `old` absent from `new`).
4. Client API: 591 signatures each side; after stripping the `old`-only
   `anydata Additional Values, ` token and the `mod:ver:` qualifiers, `diff fn_old fn_new`
   returns 0 lines.
5. README block (lines 1–113): identical.
6. Section markers: 4 in each, same set.
7. Doc-comment volume: 63 case-insensitive "deprecated" mentions in each render (unchanged);
   0 `# + ` parameter-doc lines in each (unchanged).
8. Brace balance: `old` 1796/1796, `new` 1896/1896 — both balanced; `new`'s extra 100 are
   the annotation-value braces.
9. Syntax quality moved in the right direction only: `new` removes the 240 non-compiling
   `anydata Additional Values` params and 290 non-compiling `mod:x.y.z:Type` refs, and
   introduces no new malformed construct (grep for reserved-word params, unbalanced braces,
   and residual `:x.y.z:` refs all clean or unchanged).

## 5. Issues in `new` (independent of `old`)

All six items below are inaccuracies in `new` versus the library source. **Every one is
present identically in `old`** (counts verified on both files), so none is a regression —
they are standing extractor/renderer limitations.

1. **`@deprecated` is never emitted.** The bala's `client.bal` carries 21 `@deprecated`
   annotations (e.g. `client.bal:871` on `post api/'3/expression/eval`,
   `client.bal:1246`, `client.bal:1821`). Renders: `grep -c '@deprecated'` = 0 in both.
   The `# # Deprecated` doc section is dropped too. An LLM reading this render will happily
   recommend 21 deprecated endpoints. This is the most consequential remaining inaccuracy.
2. **Included-record parameters (`*XxxQueries queries`) are rendered as flattened defaulted
   params *plus* a trailing required record param.** Source `client.bal:872`:
   `(JiraExpressionEvalRequestBean payload, map<string|string[]> headers = {}, *EvaluateJiraExpressionQueries queries)`;
   render: `(JiraExpressionEvalRequestBean payload, map<string|string[]> headers = {}, string expand = "", EvaluateJiraExpressionQueries queries)`.
   The `*` is lost, the fields are duplicated, and a required parameter follows defaulted
   ones — a non-compiling signature that also invites the wrong call shape.
3. **Quoted identifiers lose their quote when flattened into parameter lists.** Source
   `types.bal:3378` declares `"syntax"|"type"|"complexity" 'check = "syntax";`; render emits
   `"syntax"|"type"|"complexity" check = "syntax"` (1 occurrence). Same for
   `int:Signed32 limit = 0` (source field is `'limit`) and `string from = ""` at render line
   14472 / `old` 14372. Inside record bodies the quoting is preserved correctly
   (`int:Signed32 'limit?;` ×3), so this is specific to the parameter-flattening path.
4. **Closed records are rendered as open.** The bala declares 722 `public type X record {|`
   and 369 `record {`; both renders emit `record {` for all 1091 (`grep -c '^type .* record {|$'`
   = 0 in `new`). Rest-field semantics are lost at the top level (they *are* preserved for
   inline anonymous records such as `record {|ProjectCreateResourceIdentifier...;|}`).
5. **Parameter/return doc lines are dropped.** `client.bal` has 1950 `# + …` doc lines;
   both renders have 0. Each method keeps only its summary line followed by an empty `# `.
6. **Annotations are emitted without the imports or qualifiers that make them resolvable.**
   `new` writes `@constraint:String`, `@jsondata:Name`, `@http:Header` with no import block
   in the render, and drops `public`/`isolated` from all declarations. Cosmetic for LLM
   consumption, but the render is not compilable as-is.

## 6. Coverage gaps vs. the library

**Zero public symbols of the default module are missing from both renders.**

- `package.json` `export` = `["jira"]`; `modules/` contains exactly one directory, `jira`.
  There is no submodule API, so the known `getDefaultModule()`-only limitation costs nothing
  for this library.
- Default module public surface: 1103 `public type` in `types.bal`, 0 public
  functions/classes/consts/enums/annotations/listeners/services outside the client
  (`grep -nE '^public (function|class|isolated function|const|enum|annotation|listener|service)' ballerina/*.bal` → no hits),
  and `public isolated client class Client` (`client.bal:25`) with 591 resource functions
  (`client.bal:32` init + 590 resource functions).
- `new` renders 1103/1103 types, the client, init and all 590 resource functions.
- `old` was missing 6 type bodies (rendered as `// Unknown type:` stubs) — closed by `new`.

Semantic (non-symbol) coverage gaps shared by both renders are the 21 `@deprecated` markers,
the 1950 parameter-doc lines, and the 722 closed-record markers listed in §5.

## 7. Compiler plugin

No compiler plugin exists for this package. The bala has **no `compiler-plugin/` directory**
(`ls .../any` → `bala.json  dependency-graph.json  docs  modules  package.json`), and the
upstream tag has no `compiler-plugin*` directory (repo top level is
`LICENSE ballerina build-config build.gradle docs examples gradle gradle.properties gradlew
gradlew.bat issue_template.md pull_request_template.md settings.gradle`). Nothing is expected
to surface in the render from a plugin, and nothing is missing on that account.

## 8. Other considerations

- **Not deprecated as a package**; version 2.0.2 is a stable major, built with Ballerina
  `2201.12.0`. 21 *individual endpoints* are deprecated (see §5.1).
- **Size / token cost**: `new` is +100 lines (+0.6 %) over `old`. Trivially more expensive
  for 100 genuine constraint/serialisation-name facts plus 6 previously-blank type bodies,
  and the 240 removed junk tokens offset part of it. Net clearly favourable.
- **Doc quality**: the render's per-method docs are one-line summaries only. Fine for
  discovery, thin for parameter semantics — unchanged between the two sides.
- **`@jsondata:Name` now visible** is a real functional win: fields such as `endIndex` are
  wire-named `end-index`, and `old` gave an LLM no way to know that.
- The generated `*QueriesItems*` types (§2) are OpenAPI-generator artifacts for array item
  constraints; their presence is correct but they carry no doc text in the source either.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/… new/…` | 16649 / 16749 |
| 2 | `grep -c '^// Unknown type:'` | old 6, new 0 (old lines 1340, 2508, 2510, 5612, 7312, 10346) |
| 3 | `grep -n '^// --- '` | both: README@7, END README@113, Types@115, Client@14288(old)/14388(new) |
| 4 | `diff -u old new > full.diff`; `grep -c '^@@'` | 407 hunks |
| 5 | `grep -c '^-[^-]' / '^+[^+]' full.diff` | −537 / +637 |
| 6 | Classification of the 537 removed lines | 265 lang.int-qualified, 240 `Additional Values`, 25 jira-qualified, 6 Unknown-type, 1 diff artifact — sums exactly to 537, categories disjoint |
| 7 | `full.diff:1560` vs `:1563` | same doc line removed and re-added in one hunk → no doc loss |
| 8 | Declaration lists `decl_old.txt`/`decl_new.txt`; `diff <(sort …)` | 1099 vs 1105; 6 additions, 0 removals |
| 9 | `grep -c 'Additional Values'` | old 240, new 0 |
| 10 | `grep -c '^    resource function '` | 590 both |
| 11 | Normalised signature diff `diff fn_old.txt fn_new.txt` | 591 lines each, 0 differences |
| 12 | `grep -c ':[0-9]\+\.[0-9]\+\.[0-9]\+:' new` | 0 |
| 13 | Annotation census `new` | 66 constraint:String, 14 jsondata:Name, 11 constraint:Array, 5 constraint:Int, 3 http:Header, 1 display = 100 |
| 14 | Annotation census bala `types.bal`+`client.bal` | identical 66/14/11/5/3/1 (+21 `@deprecated`, unrendered) |
| 15 | Annotation census `old` | 0 |
| 16 | `git ls-remote --tags` | `v2.0.2` → `62741eab`; cloned `--depth 1 --branch v2.0.2` |
| 17 | `diff -q bala/modules/jira/{client,types,utils}.bal src/ballerina/…` | all three IDENTICAL |
| 18 | `grep -c '^public type ' bala/types.bal` | 1103 |
| 19 | `comm -23` / `comm -13` render-type-names vs source-type-names (new) | both empty (1103 = 1103) |
| 20 | `comm -13 rt_old.txt st.txt` | the 6 names old was missing |
| 21 | `types.bal:555-556, 1898-1899, 2649-2650, 2965-2966, 4478, 8332-8333` | the 6 new types + their constraints verified verbatim |
| 22 | `types.bal:7890-7904` (`UserList`) | matches new render lines incl. all 3 `@jsondata:Name` |
| 23 | `types.bal:5352-5358` (`UpdateIssueSecurityLevelDetails`) | matches new render incl. both `@constraint:String` |
| 24 | `types.bal:10034`, `835`, `7473`, `12084` | `@display` ×1, `@http:Header` ×3 confirmed |
| 25 | `types.bal:2125, 4096, 6992` | `record {\|ProjectCreateResourceIdentifier...;\|} explicitMappings?` confirmed |
| 26 | `grep -c '@deprecated'` bala client.bal / renders | 21 / 0 / 0 |
| 27 | `client.bal:855-875` vs render lines 14678-14680 | `@deprecated`, `# # Deprecated`, `# + …` docs, `*` on the queries param, and `isolated` all dropped in *both* renders |
| 28 | `client.bal:854` + `types.bal:3372-3379` vs render | `'check` → `check` unquoted; `string expand = ""` invented by flattening; both sides |
| 29 | `grep -n 'string from = '` | old:14372, new:14472 — `'from` unquoted, both sides |
| 30 | `grep -c '^public type .* record {|$'` / `record {$` in bala | 722 closed / 369 open; renders emit `record {` 1091× on both sides |
| 31 | `grep -c '^    # + '` | source client.bal 1950; both renders 0 |
| 32 | Brace balance | old 1796/1796, new 1896/1896 |
| 33 | README lines 1-113 `diff` | identical |
| 34 | `ls bala/any` and `ls bala/any/modules` | no `compiler-plugin/`; single module `jira` |
| 35 | `package.json` | `export: ["jira"]`, `ballerina_version: 2201.12.0`, `template: false` |
| 36 | Repo top-level `ls` at v2.0.2 | no compiler-plugin directory |
| 37 | JSON schema comparison | both 1103 typeDefs / 1 client / 591 fns; `new` adds `baseType` (6) and `annotations` (6 typeDef + 94 field = 100) |
| 38 | JSON typeDef name-set equality old vs new | `True` |
| 39 | `grep -oE '^\s*@' new` top-level annotations | 6 (5 `@constraint:String` at render lines 1349, 2525, 2528, 5645, 10414 + `@display` at 12525), all verified against source |
| 40 | `OLD_AND_NEW_DIFFS/jira_diff.md` claims (6 added / 0 removed types, 6→0 Unknown, 327→0 qualified refs, 407 hunks, +637/−537) | independently reproduced; all correct except that my qualifier count splits as 265 lang.int + 25 jira-qualified on the *removed-line* basis (a single removed line can carry several refs, which is where the diff file's 327 *reference* count comes from — not a contradiction) |

## 10. Caveats and unverified items

- Neither render was fed to a Ballerina compiler; syntax claims (`anydata Additional Values`
  being invalid, required-after-defaulted params, keyword-clashing `check`/`limit`/`from`)
  rest on the language rules and on comparison with the source spelling, not on a compile
  run. The direction of the change is unaffected either way: `new` removes malformed
  constructs and adds none.
- I did not exhaustively hand-verify all 1103 rendered record bodies field-by-field against
  `types.bal`; I verified the complete top-level type-name set (exact set equality), every
  one of the 100 annotations by census plus 12 spot-checks with file:line, and every one of
  the 537 removed / 637 added diff lines by category. Fields that are identical in both
  renders and were never touched by the diff were not re-checked against source, since any
  error there would be shared with `old` and therefore not a regression.
- Ballerina Central metadata was not re-queried over the network; the bala's `package.json`
  and `bala.json` were used instead, and the bala is byte-identical to the verified `v2.0.2`
  tag, so the two cannot disagree on module list or version.
- The `# The index of the last item returned on the page` line counted as "removed" by
  `diff` was manually confirmed to be re-added inside the same hunk; if some other tooling
  reports "1 doc line lost", that is the same artifact.

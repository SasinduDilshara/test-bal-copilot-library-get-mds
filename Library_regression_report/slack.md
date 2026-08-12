# ballerinax/slack 5.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/slack` |
| Pinned version | `5.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-slack |
| Tag reviewed | `v5.0.1` (commit `d6c619520f35bd04ed4a411d80d2cb536bcac9a7`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/slack/5.0.1` |
| Old render | `5041` lines |
| New render | `5754` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerinax/slack` 5.0.1 is a single-module, fully OpenAPI-generated connector: one public
`isolated client class Client` with `init` + 174 resource functions, and 506 public type
definitions, all in the default module `slack`. There is no compiler plugin, no submodule, and no
module-level public function, const, enum, annotation, listener or service.

The whole `old` → `new` delta is 132 removed / 845 added lines (`diff old new`), and **every one of
those lines is accounted for by three spec-v2 behaviours, all of them strict improvements**:

1. 31 `// Unknown type: X` placeholders replaced by 31 real type definitions (all verified against
   the bala).
2. 26 lines carrying 67 version-qualified refs (`ballerinax/slack:5.0.1:Type`) re-emitted with
   plain, resolvable type names.
3. 74 client resource-function signatures that contained the syntactically invalid parameter
   `anydata Additional Values` (identifier with a space) now emit without it.

and one addition: 712 annotation instances (`@jsondata:Name`, `@http:Query`, `@constraint:String`,
`@constraint:Array`, `@display`) that `old` dropped entirely are now rendered — matching the bala's
`types.bal` annotation set **exactly, 712 for 712**.

Nothing was removed, truncated, renamed or weakened. **Zero regressions.** Coverage is complete on
both sides for declaration *names*; the residual accuracy defects (quoted-identifier `'` prefix,
lost parentheses, `record {|` → `record {`, dropped `public`/`isolated`) are identical in `old` and
`new` and are pre-existing renderer limitations, not spec-v2 damage.

## 2. Change inventory

Whole-file diff (`diff old/ballerinax_slack.bal.txt new/ballerinax_slack.bal.txt`):

| | count |
|---|---|
| lines removed (`^<`) | 132 |
| lines added (`^>`) | 845 |

Full accounting of the 132 removed lines (no residue):

| category | lines |
|---|---|
| `// Unknown type: X` placeholders | 31 |
| lines containing `ballerinax/slack:5.0.1:` (re-emitted unqualified in `new`) | 26 |
| client resource signatures containing `anydata Additional Values` | 74 |
| blank line (formatting) | 1 |
| **unexplained** | **0** |

Full accounting of the 845 added lines:

| category | lines |
|---|---|
| annotation lines (`^\s*@`) | 712 |
| `type ...` declarations (31 net-new names + 23 re-emitted unqualified) | 54 |
| client resource signatures (the 74 above, minus the bogus param) | 74 |
| inline-record field lines re-emitted unqualified | 3 |
| doc comment for `Blocks` | 1 |
| blank line | 1 |
| **unexplained** | **0** |

Declarations by kind:

| kind | old | new | note |
|---|---|---|---|
| `type` declarations emitted | 475 | 506 | +31 |
| `// Unknown type:` placeholders | 31 | 0 | −31 |
| typeDefs in JSON | 506 | 506 | identical name set (`set(old)^set(new) == {}`) |
| client classes | 1 | 1 | `Client` |
| client functions in JSON | 175 | 175 | `init` + 174 resource functions |
| `resource function` lines in render | 174 | 174 | accessor+path set byte-identical (`diff` on extracted names → no output) |
| module-level functions / services / annotations in JSON | 0 / 0 / 0 | 0 / 0 / 0 | library genuinely has none |
| enums / consts | 0 | 0 | library has none |

**Declarations added (31)** — all previously `// Unknown type:`:
`AppIdDef, Blocks, BotIdDef, ChannelActionsTsAnyOf1, ChannelDef, ChannelIdDef, ChannelNameDef,
CommentIdDef, CommentsObj, ConversationObj, DiscoverableDiscoverableAnyOf12, DmIdDef,
EnterpriseIdDef, EnterpriseNameDef, EnterpriseUserIdDef, FileIdDef, GroupIdDef, OkTrueDef,
OptionalAppIdDef, ReminderIdDef, ResponseMetadataObj, ScopesObj, SubteamIdDef, TeamDef,
TopicPurposeCreatorDef, TsDef, TzTzAnyOf112, TzTzAnyOf12, UserIdDef, UserObj, WorkspaceIdDef`

**Declarations removed: 0** (`comm -23 old_types.txt new_types.txt` → empty).

**Annotations** (old had none at all):

| annotation | new render | bala `types.bal` |
|---|---|---|
| `@jsondata:Name` | 599 | 599 |
| `@http:Query` | 79 | 79 |
| `@constraint:String` | 22 | 22 |
| `@constraint:Array` | 11 | 11 |
| `@display` | 1 | 1 |
| **total annotation lines** | **712** | **712** |

**README / header**: `diff <(sed -n '1,111p' old) <(sed -n '1,111p' new)` → identical. Section
markers identical (4 on each side: `README`, `END README`, `Types`, `Client`).

## 3. Correctness against library source

The bala's `modules/slack/{client.bal,types.bal,utils.bal}` are **byte-identical** to the
`v5.0.1` tag's `ballerina/{client.bal,types.bal,utils.bal}` (`diff -q` → no differences on all
three). So GitHub and the bala agree; either is authoritative.

**All 31 added types verified individually in `types.bal`.** Examples:

- `type TeamDef string;` ← `types.bal:1273 public type TeamDef string;`
- `type OkTrueDef true;` ← `types.bal:1146 public type OkTrueDef true;`
- `type ScopesObj string[];` ← `types.bal:1370`
- `type ChannelActionsTsAnyOf1 int;` ← `types.bal:1386`
- `type CommentsObj anydata[];` ← `types.bal:2900`
- `type ConversationObj InlineArrayItemsConversationObj[];` ← `types.bal:3038`
- `type ResponseMetadataObj InlineArrayItemsResponseMetadataObj[];` ← `types.bal:3251`
- `type InlineArrayItemsConversationObj ConversationObject|ConversationMPIMObject|ConversationIMChannelObjectFromConversationsMethods;` ← `types.bal:3561`
- `type Blocks BlocksInner[];` ← `types.bal:3952` (doc comment "This is a very loose definition…" also matches)
- `type UserObj InlineArrayItemsUserObj[];` ← `types.bal:4108`
- The 20 remaining `*Def` aliases (`TopicPurposeCreatorDef, WorkspaceIdDef, EnterpriseIdDef,
  DiscoverableDiscoverableAnyOf12, EnterpriseNameDef, ChannelNameDef, FileIdDef, ChannelIdDef,
  DmIdDef, GroupIdDef, BotIdDef, TsDef, AppIdDef, CommentIdDef, OptionalAppIdDef, TzTzAnyOf112,
  SubteamIdDef, ReminderIdDef, EnterpriseUserIdDef, ChannelDef`) each matched a
  `public type <name> string;` line in `types.bal` — loop over all 20, zero `MISSING`.

**All 712 annotations verified positionally.** A script extracted every
`(@annotation, value, next-declaration-line)` triple from `types.bal` and from the `new` render and
compared the multisets: 711/711 `jsondata|http|constraint` triples match, with exactly one
difference, and it is a *pre-existing type-formatting* difference, not an annotation error
(parentheses, see §5.2). Sample spot-checks:

- render `@constraint:String {pattern: re \`^[T][A-Z0-9]{2,}$\`}` on `TeamDef` ← `types.bal:1272-1273`
- render `@constraint:String {pattern: re \`^[CGD][A-Z0-9]{8,}$\`}` on `ChannelDef` ← `types.bal:4128-4129`
- render `@constraint:String {pattern: re \`^[UW][A-Z0-9]{8,}$|^$\`}` on `TopicPurposeCreatorDef` ← `types.bal:2255-2256`
- render `@http:Query {name: "team_id"}` / `{name: "enterprise_id"}` on `AdminAppsApprovedListQueries.teamId`/`.enterpriseId` ← `types.bal:2045-2048`
- render `@display {label: "Connection Config"}` on `ConnectionConfig` ← `types.bal` (1 occurrence)

**Client.** `init(ConnectionConfig config, string serviceUrl = "https://slack.com/api") returns error?`
matches `client.bal:31`. All 174 resource accessor+path pairs are identical between the two renders
and count-match `client.bal` (`grep -c '^\s+(resource|remote) ... function' client.bal` = 174).
Spot-check `resource function post admin\.apps\.approve(AdminAppsApproveBody payload,
map<string|string[]> headers = {}) returns DefaultSuccessResponse|error;` ← `client.bal:40`.

**The removed `anydata Additional Values` is not real API.** It is the implicit `anydata...` rest
field of the *open* query records, surfaced by the old extractor as a pseudo-parameter named
`"Additional Values"` with description `"Capture key value pairs"` (visible in
`old/ballerinax_slack.json`, `admin.apps.approved.list` parameter list). `client.bal:52` declares
`(map<string|string[]> headers = {}, *AdminAppsApprovedListQueries queries)` — there is no such
parameter. Removing it is a correctness fix; the record's openness is still conveyed by the
render emitting `record {` (not `record {|`) for that type.

## 4. Regressions

**None found.**

What was checked to conclude that:

- `comm -23 <(type names in old) <(type names in new)` → empty: no type declaration lost.
- JSON `typeDefs` name sets are equal (506 = 506) and the per-kind census is identical
  (`Record: 436, Union: 39, Other: 31` on both sides).
- Client function count identical in JSON (175 = 175); the extracted set of
  `resource function <accessor> <path>` strings is identical (`diff` → no output).
- Every removed line in the whole-file diff falls into the three benign categories above; the
  "unexplained removals" filter returns 0 lines.
- Header + README block (lines 1–111) byte-identical.
- `ConnectionConfig` block byte-identical between renders.
- `Special Agent Note` cross-package markers: 17 in old, 17 in new (none lost).
- No doc comment, default value, return type or parameter (other than the invalid
  `Additional Values`) differs anywhere in the file.
- Non-ASCII byte count identical (2 vs 2) — no encoding damage.

The only information technically *lost* in `new` is the pseudo-parameter that signalled the query
records are open. It was invalid Ballerina (`anydata Additional Values` — space in an identifier),
was not part of the library API, and the same fact is still derivable from the open `record {`
rendering of each `*Queries` type. Not counted as a regression.

## 5. Issues in `new` (independent of `old`)

All of 5.1–5.4 and 5.6–5.7 are **also present in `old`** — they are renderer limitations, listed
here because the brief asks for `new`-side inaccuracies regardless of `old`. Only 5.5 is new-only.

**5.1 Quoted-identifier `'` prefix dropped (18 type definitions + all their references).**
`types.bal` declares 18 types whose names start with a digit and are therefore quoted:
`'200AnyOf1, '200AnyOf11, '200AnyOf12, '200200AnyOf12, '200200AnyOf112, '200200AnyOf122,
'200200200AnyOf1123, '200200200AnyOf1223, '200200200200AnyOf12234, '200Items, '200Team, '200Team1,
'200Team2, '200Team3, '200User, '200User1, '200User2, '200User3`
(`grep -cE "^public type '200" types.bal` = 18). Both renders emit them unquoted, e.g.
`new:1786 type 200AnyOf1 record {` and `type 200Items FilePin|MessagePin;`. These lines do not parse
as Ballerina, and an LLM copying them will write invalid code. Identical in `old` (`old:1397`).

**5.2 Parentheses lost around a union element type (2 field lines).**
`types.bal:2743,2745` declare `(ChannelDef|TeamDef)[][] ids;` and
`(ChannelDef|TeamDef)[][] excludedIds?;`. Both renders emit `ChannelDef|TeamDef[][] ids;` /
`... excludedIds?;` (`old:851-852`, `new:1153,1155`), which parses as
`ChannelDef | (TeamDef[][])` — a semantically different type. The three *record*-union array fields
(`types.bal:971,1540,3702`) do keep their parentheses in both renders, so this is confined to the 2
simple-union cases.

**5.3 Closed records rendered as open.** `types.bal` has 176 `record {|` occurrences; each render
has only 12. E.g. `types.bal:2943 public type ChannelObj record {|` → `new:3736 type ChannelObj
record {`. This tells an LLM the records accept arbitrary extra fields when they do not. Counts are
identical in `old` and `new` (436 open / 12 closed on both sides).

**5.4 `public` and `isolated` qualifiers dropped everywhere.** Render emits
`client class Client {`, `function init(...)`, `resource function post ...`, `type X record {`;
the library declares `public isolated client class Client`, `public isolated function init`,
`resource isolated function post`, `public type X`. Identical in both renders (0 `public type` lines
on either side).

**5.5 (new-only) Annotation prefixes are used without imports.** The render's import block is only
`import ballerinax/slack;` (line 5), yet `new` now emits `@jsondata:`, `@http:` and `@constraint:`
prefixes 712 times. `ballerina/data.jsondata`, `ballerina/http` and `ballerina/constraint` are never
imported in the rendered text. Cosmetic for comprehension, but the snippet is not self-contained.
Note the underlying JSON *does* carry the full module (`"module": "ballerina/http"` etc.), so this
is a `toSyntaxString` presentation gap, not an extractor gap.

**5.6 Included-record query parameters are duplicated and given invented defaults.** For each of the
74 `*Queries` operations both renders flatten the record's fields into positional parameters *and*
keep the record parameter, e.g.
`resource function get admin\.apps\.approved\.list(map<string|string[]> headers = {}, string cursor = "", int limit = 0, string teamId = "", string enterpriseId = "", AdminAppsApprovedListQueries queries)`
against the real `(map<string|string[]> headers = {}, *AdminAppsApprovedListQueries queries)`
(`client.bal:52`). Also, `'limit` (a quoted keyword field, `types.bal:2044`) is de-escaped to
`limit`, and optional fields with no default are given fabricated defaults (`= ""`, `= 0`) — the
defaults originate in the JSON (`"default": "0"`) on **both** sides, so this is an extractor
behaviour unchanged by spec v2.

**5.7 Invented symbols: none.** Every capitalised token used in a type position in `new` resolves to
one of the 506 rendered types, a builtin, or an explicitly flagged external `http:`/`OAuth2*` type
carrying a `// Special Agent Note: … FROM ballerina/http package` comment.

## 6. Coverage gaps vs. the library

**Zero gaps.**

- Public types in the bala default module: 488 matched by `^public type [A-Za-z0-9_]+` plus 18
  quoted `'200*` types = **506**. Types rendered in `new`: **506**.
  `comm -23 <(bala public types) <(new render types)` → **0 lines**.
- Public class: 1 (`Client`) — rendered.
- Public client methods: 174 resource functions + `init` — all rendered on both sides.
- Module-level public functions / consts / enums / annotations / listeners / services in the bala:
  **0** (`grep -nE '^public (isolated )?function |^public (const|enum|annotation|listener|service|class)' *.bal` matches only the `Client` class). Nothing to miss.
- **Submodule API: none.** `package.json` `"export": ["slack"]`; `modules/` contains exactly one
  directory, `slack`, which is the default module. Central metadata lists a single module `slack`.
  The known `getDefaultModule()`-only limitation therefore costs this library nothing.
- `utils.bal` contains only non-public helpers (`createFormURLEncodedRequestBody`,
  `getPathForQueryParam`, …) — correctly absent from both renders.

## 7. Compiler plugin

**No compiler plugin exists.** `find` over the bala returns no `compiler-plugin` entry (no
`compiler-plugin/`, no `compiler-plugin.json`), and the `v5.0.1` tag has no
`*-compiler-plugin` module (`ballerina/`, `build-config/`, `docs/`, `examples/`, `gradle/` only).
The connector is a plain OpenAPI-generated HTTP client, so there are no code actions, validations
or generated artifacts that ought to surface in the render. Nothing missing.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/slack/5.0.1`: `"deprecated": null`,
  `"deprecateMessage": ""`. Stable major (`5.0.1`), built with `ballerinaVersion 2201.12.2`,
  `graalvmCompatible: true`, pullCount 193.
- **Size / token cost.** `new` is 5754 lines / 200 825 bytes vs `old` 5041 lines / 174 187 bytes —
  **+14.1 % lines, +15.3 % bytes**. The JSON grows 780 966 → 903 827 bytes (+15.7 %). The extra
  budget buys 31 real definitions and 712 wire-name/validation annotations. For a Slack connector
  the `@jsondata:Name` mappings are high-value: without them an LLM cannot know that `teamId`
  serialises as `team_id`, `nextCursor` as `next_cursor`, etc. Good trade.
- **Doc quality.** Descriptions come straight from the Slack OpenAPI spec and are preserved
  verbatim on both sides. README block is the full 101-line `docs/README.md`.
- **Render is a stub file, not compilable by design** (function bodies elided, no imports for
  referenced external modules). The syntax defects in §5.1–5.2 are still worth fixing because they
  would be copied verbatim into user code.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 5041 / 5754 |
| 2 | `grep -c '^// Unknown type:' old new` | 31 / 0 |
| 3 | `grep -n '^// --- ' old` / `new` | 4 markers each; Types at 112, Client at 4340 (old) / 5053 (new) |
| 4 | `diff old new \| grep -c '^<'` / `'^>'` | 132 removed / 845 added |
| 5 | removed lines minus {Unknown-type, `ballerinax/slack:5.0.1:`, `Additional Values`} | **0 lines** |
| 6 | added lines minus {annotations, `type `, `resource function`, 3 record lines, doc, blank} | **0 lines** |
| 7 | `comm -23 old_types.txt new_types.txt` | empty → nothing removed |
| 8 | `comm -13 old_types.txt new_types.txt` | 31 names, identical to the 31 Unknown-type placeholders |
| 9 | `grep -c 'ballerinax/slack:5.0.1:'` old / new | 26 lines (67 occurrences) / 0 |
| 10 | `grep -c 'Additional Values'` old client / new client | 74 / 0 |
| 11 | `diff <(resource names old) <(resource names new)` | no output → identical |
| 12 | `grep -cE '^\s*(resource\|remote) ' old_client new_client` | 174 / 174 |
| 13 | `grep -cE '^\s+(resource\|remote) (isolated )?function ' bala/client.bal` | 174 |
| 14 | JSON: `len(typeDefs)` old / new | 506 / 506; symmetric-difference of names = ∅ |
| 15 | JSON: typeDef kind census old / new | `Record 436, Union 39, Other 31` on both |
| 16 | JSON: `len(clients[0].functions)` old / new | 175 / 175 |
| 17 | JSON `TeamDef` old vs new | old `{type:"Other"}` only; new adds `baseType:"string"` + `constraint.String` annotation |
| 18 | JSON `admin.apps.approved.list` params old vs new | old has extra `{"name":"Additional Values","description":"Capture key value pairs","type":"anydata"}`; new does not |
| 19 | bala `client.bal:52` | `resource isolated function get admin\.apps\.approved\.list(map<string\|string[]> headers = {}, *AdminAppsApprovedListQueries queries)` |
| 20 | loop `grep "^public type <t> " types.bal` over all 31 added names | all found, 0 MISSING |
| 21 | annotation counts in `new` render | 599 / 79 / 22 / 11 / 1 = 712 |
| 22 | annotation counts in bala `types.bal` | 599 / 79 / 22 / 11 / 1 = 712 (712 total `^\s*@` lines) |
| 23 | annotation-target triple multiset, bala vs new | 711 vs 711; 1 mismatch, caused by §5.2 parentheses only |
| 24 | `grep -cE '^\s*@' old` | 0 → old dropped every annotation |
| 25 | `diff <(sed -n '1,111p' old) <(sed -n '1,111p' new)` | identical |
| 26 | `diff` of `ConnectionConfig` block old vs new | identical |
| 27 | `grep -c 'Special Agent Note'` old / new | 17 / 17 |
| 28 | `LC_ALL=C grep -c '[^ -~]'` old / new | 2 / 2 |
| 29 | `git ls-remote --tags` | `v5.0.1` → `8e0cb5df…` (peeled `d6c61952…`) |
| 30 | `diff -q bala/modules/slack/{client,types,utils}.bal src/ballerina/…` | all identical |
| 31 | `comm -23 <(bala public types, 488) new_types.txt` | 0 → no public type missing |
| 32 | `grep -cE "^public type '200" types.bal` | 18 → 488+18 = 506 = rendered count |
| 33 | `grep -nE '^public (isolated )?function \|^public (const\|enum\|annotation\|listener\|service)' bala/*.bal` | no matches → no other public API |
| 34 | `ls bala/any/modules` ; `package.json.export` | single module `slack`; `["slack"]` |
| 35 | `find bala -iname '*compiler*'` ; `ls src` | no compiler plugin on either side |
| 36 | `grep -c 'record {\|record {\|'` old / new / bala types.bal | 436/12, 436/12, 265/176 |
| 37 | `grep -n 'excludedIds'` old:852, new:1155 vs `types.bal:2745` | parentheses dropped in both renders |
| 38 | `grep -nE '\([A-Za-z].*\|.*\)\[\]' types.bal` | 5 sites; 3 record-union sites keep parens in both renders, 2 simple-union sites lose them in both |
| 39 | type-position identifier resolution over `new` Types section | every token resolves to a rendered type, a builtin, or a flagged `ballerina/http` type; `BlocksInner` defined |
| 40 | `curl api.central.ballerina.io/.../ballerinax/slack/5.0.1` | `deprecated: null`, 1 module, ballerinaVersion 2201.12.2, pullCount 193 |
| 41 | `wc -c` old/new `.bal.txt` and `.json` | 174187→200825 (+15.3 %), 780966→903827 (+15.7 %) |

## 10. Caveats and unverified items

- **Diff line counts are tool-dependent.** GNU `diff` reports 132 removed / 845 added (matching
  `OLD_AND_NEW_DIFFS/slack_diff.md`); Python `difflib.unified_diff` reports 145/858 on the same
  files. The report uses the GNU `diff` figures throughout. The *content* accounting (§2) is
  unaffected — it partitions the GNU set exhaustively with 0 residue.
- Neither render was fed to `bal build`. Both are stub-style files (function bodies elided, external
  modules unimported) so they cannot compile by construction; the syntax defects in §5.1–§5.2 were
  identified by direct comparison against `types.bal`, not by a compiler.
- I verified all 31 added type definitions and all 712 annotations exhaustively, and the full
  declaration-name sets exhaustively. The *bodies* of the 436 record types were verified by
  differential means (whole-file diff residue = 0) rather than field-by-field against `types.bal`;
  a field-level census of all 506 types against the bala was not performed.
- The precomputed diff reports "Version/module-qualified type refs: 67" (occurrence count) while
  this report also quotes 26 (line count). Both were measured; they are the same phenomenon.
- The `old` renderer patch `service.methods ?? []` is documented as affecting only `ballerina/mcp`;
  this library declares no services (`services: []` in both JSONs), so it is irrelevant here — taken
  as given from the brief, not independently re-verified in the renderer source.

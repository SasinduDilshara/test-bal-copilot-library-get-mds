# ballerinax/zoom.meetings 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/zoom.meetings` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-zoom.meetings |
| Tag reviewed | `v1.0.2` (exact match; tree identical to the bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/zoom.meetings/1.0.2` |
| Old render | `12144` lines |
| New render | `14104` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present and correct in `old` is missing
from `new`. The delta is +2040 / −80 lines across 578 hunks and consists of exactly four things:

1. **+1960 annotation lines** that `old` dropped entirely (`@jsondata:Name`, `@http:Query`,
   `@constraint:String|Array|Int`, `@display`). These carry the wire-format field names —
   without them an LLM cannot know that `numberedQuestions` serialises as `numbered_questions`.
2. **10 `// Unknown type:` placeholders replaced with real type definitions** (all 10 verified
   correct against `types.bal`), plus 3 union aliases that `old` printed with
   `ballerinax/zoom.meetings:1.0.2:` version-qualified operands.
3. **7 reserved-word escapes fixed** (`string from?` → `string 'from?`, `string field?` →
   `string 'field?`, `... type?` → `... 'type?`) — `old` emitted un-escaped Ballerina keywords.
4. **60 bogus `anydata Additional Values` parameters removed** from resource-function signatures
   (a parameter name containing a space — not valid Ballerina).

Doc-comment lines (3212), record fields (3479), resource functions (183) and the README block
(lines 8–164) are byte-identical between the two renders. Declaration coverage of the default
module is **587/587 in `new`** (`old`: 577/587).

## 2. Change inventory

Both files, both JSONs, and the diff were measured directly.

| Metric | old | new |
|---|---|---|
| Lines | 12144 | 14104 |
| Diff | — | +2040 / −80, 578 hunks |
| `// Unknown type:` placeholders | 10 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 7 | 0 |
| Section markers (`// --- `) | 4 | 4 |
| Top-level `type` declarations | 577 | 587 |
| Unique named declarations (type/class/enum/const/fn) | 577 | 587 |
| Resource functions in `client class Client` | 183 | 183 |
| `init` constructor | 1 | 1 |
| Doc lines (`^\s+# `) | 3212 | 3212 |
| Record-field lines | 3479 | 3479 |
| `@jsondata:Name` | 0 | 1724 |
| `@http:Query` | 0 | 123 |
| `@constraint:String` | 0 | 87 |
| `@constraint:Array` | 0 | 22 |
| `@constraint:Int` | 0 | 3 |
| `@display` | 0 | 1 |
| `@deprecated` | 51 | 51 |
| `anydata Additional Values` params | 60 | 0 |

### Declarations added (10, all `type`)

All were `// Unknown type: <Name>` comments in `old`; `new` emits the real definition.

| Render (new) | Source (`modules/zoom.meetings/types.bal`) | Match |
|---|---|---|
| `type UserIdOneOf1 string;` | L2175 `public type UserIdOneOf1 string;` | ✓ |
| `type UserIdUserIdOneOf12 string;` | L10686 | ✓ |
| `type UserIdUserIdUserIdOneOf123 "me";` | L5319 | ✓ |
| `type MeetingIdOneOf1 int;` | L5923 | ✓ |
| `type MeetingIdMeetingIdOneOf12 string;` | L11378 | ✓ |
| `type MeetingId1OneOf1 int;` | L10906 | ✓ |
| `type MeetingId1MeetingId1OneOf12 string;` | L8622 | ✓ |
| `@constraint:String {maxLength: 200}` + `type MeetingsmeetingIdsurveyCustomSurveyQuestionsAnswersItemsString string;` | L2737–2738 | ✓ (incl. annotation) |
| `@constraint:String {maxLength: 200}` + `type WebinarswebinarIdsurveyCustomSurveyQuestionsAnswersItemsString string;` | L2740–2741 | ✓ (incl. annotation) |
| `type WebinarSurveyObjectCustomSurveyQuestionsAnswersItemsString string;` | present in `types.bal` | ✓ |

### Declarations removed

None. `comm -23 old.decls new.decls` → empty.

### Declarations modified

- **3 union aliases de-qualified** — `old`: `type UserId ballerinax/zoom.meetings:1.0.2:UserIdOneOf1|…`;
  `new`: `type UserId UserIdOneOf1|UserIdUserIdOneOf12|UserIdUserIdUserIdOneOf123;`
  (matches `types.bal:5938`). Same for `MeetingId` (L10749) and `MeetingId1` (L3091).
- **60 resource functions**: only change is the deletion of `anydata Additional Values, `.
  Verified mechanically: stripping that literal from the 60 removed lines makes the removed and
  added sets byte-identical.
- **7 field lines**: keyword escaping (5× `'from`, 1× `'field`, 1× `'type`).
- **1960 lines added**: annotations, all of them at record-field or type-alias level.

## 3. Correctness against library source

Upstream `v1.0.2` and the bala are the same tree — `diff -q` on `client.bal`, `types.bal`,
`utils.bal` and `README.md` all report identical. Everything below was therefore checked against
the bala (`.../1.0.2/any/modules/zoom.meetings/`).

- **All 10 added types**: exact match (table above), including the two `@constraint:String
  {maxLength: 200}` annotations at `types.bal:2737` and `2740`.
- **Annotation fidelity, bulk check**: extracted every
  `(annotation-kind, wire-name, field-name)` triple from `new` and from `types.bal` and diffed
  the sets — 476 triples in `new` vs 480 in source. The only differences are the 37 annotations
  that live inside inline anonymous records (see §5.1); every other annotation in `new` has an
  exact counterpart in the source, and `new` invents none.
- **Annotation totals** match the source exactly for `@http:Query` (123/123),
  `@constraint:Array` (22/22), `@constraint:Int` (3/3), `@display` (1/1). `@jsondata:Name`
  (1724 vs 1704) and `@constraint:String` (87 vs 82) are *higher* in the render because the
  renderer flattens `*IncludedRecord` inclusions and therefore repeats the inherited annotated
  fields — not invention.
- **Keyword escapes**: `types.bal` writes `'from` 28× and `'field` in `TrackingField4`. The 5
  fields `old` printed as bare `from` come from `InlineResponse2006AllOf1` (`string 'from?;`) and
  peers; `new` prints `'from`. Correct.
- **`@deprecated`** preserved (e.g. `ListArchivedFilesQueries.groupId`, `types.bal:1072–1075`).
- **Client surface**: `client.bal` has 183 `resource isolated function` + 1 `public isolated
  function init`; `new` renders 183 resource functions + `init` with the exact default
  `serviceUrl = "https://api.zoom.us/v2"` (`client.bal:34`).
- **Sample signature**: `client.bal:1075`
  `resource isolated function get meetings/[int meetingId]/polls(map<string|string[]> headers = {}, *MeetingPollsQueries queries) returns PollList|error`
  → `new:13607`
  `resource function get meetings/[int meetingId]/polls(map<string|string[]> headers = {}, boolean anonymous = false, MeetingPollsQueries queries) returns PollList|error;` — same accessor, path, payload and return type.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Set difference of the 577/587 declaration names: `comm -23 old.decls new.decls` → empty
  (nothing in `old` is absent from `new`).
- Doc-line count identical (3212 both), record-field-line count identical (3479 both), README
  block byte-identical (`diff` of lines 8–164 → empty), section markers 4 both.
- Resource-function count identical (183 both); the 60 modified signatures differ only by the
  removed `anydata Additional Values, ` token (verified by normalised set diff).
- `@deprecated` count identical (51 both).

**One borderline item, judged NOT a regression.** The 60 `*<X>Queries queries` parameters bind to
open records (e.g. `ListArchivedFilesQueries`, `types.bal:1064…`, closed with `};` not `|};`), so
each has an implicit `anydata` rest field. `old` surfaced that as a parameter literally named
`Additional Values` — an identifier containing a space, which is not valid Ballerina and would
invite an LLM to emit `client->/archive_files(…, Additional Values)`. The new JSON drops the
parameter (extractor-side change, confirmed in `new/*.json`). A trace of information ("extra
query params are allowed") is lost, but it was expressed in a form that was actively misleading,
so the net effect is a fix.

## 5. Issues in `new` (independent of `old`)

Item 5.1 is unique to `new`; 5.2–5.7 are pre-existing and identical in `old` — listed because the
brief asks for inaccuracies in `new` regardless of `old`.

**5.1 Annotations inside inline anonymous records are dropped (new-only surface).**
`types.bal` has 4 inline `record { … }` field types; 37 `@jsondata:Name` annotations live inside
them (`grep -cE '^        @jsondata:Name' types.bal` → 37). `new` renders these inline records
as a single flattened line with no annotations, e.g. `new:1369`
`record {|string filePath?; string playUrl?; … string deletedTime?; string recordingStart?; "completed" status?; anydata...;|}[] recordingFiles?;`
whereas `types.bal:1074–1100` annotates `playUrl` → `play_url`, `recordingEnd` →
`recording_end`, `deletedTime` → `deleted_time`, `recordingStart` → `recording_start`.
`grep -c 'value: "play_url"'` → 0 in `new`, 3 in source. This is 37 of 1704 (2.2%) of the
library's `@jsondata:Name` annotations. `old` dropped 100% of them, so this is still a large net
win — but it is an inconsistency an LLM could trip on for cloud-recording payloads.

**5.2 Record-field default values are dropped.** `types.bal` has 329 record fields with defaults
(`^    <type> <name> = …;`); both renders print only 3 with `=`. Fields declared
`int pageSize = 30;` / `boolean numberedQuestions = false;` render as `int pageSize?;` /
`boolean numberedQuestions?;` — required-with-default becomes optional. Shared with `old`.

**5.3 Reserved words still unescaped in parameter lists.** 16 occurrences of `string from = ""`
and 9 of `type = ` inside resource-function parameter lists in **both** renders (e.g. `new:13787`
`resource function get report/users/[meetings:UserId userId]/meetings(…, string from = "", …)`).
`new` fixed the record-field variants but not the parameter variants.

**5.4 Included-record (`*T`) flattening loses docs and annotations.** `InlineResponse2006`
(`types.bal:1677`) includes three records; `new` renders 7 bare fields with no doc comments and
no `@jsondata:Name`, although `InlineResponse2006InlineResponse2006AllOf12` annotates all four of
its fields. Shared with `old`. The included record types themselves are still emitted separately,
so the information is recoverable elsewhere in the file.

**5.5 Doc-comment continuation lines are emitted at column 0 without `#`.** 1852 such lines in the
Types section of *each* render (identical count), e.g. `new:1375-1376`. The render is therefore
not compilable Ballerina and markdown bleeds into the type body. Shared with `old`.

**5.6 `*` lost on included-record parameters, and parameter ordering is invalid.** Source
`*MeetingPollsQueries queries`; render `MeetingPollsQueries queries` — and it is placed after
defaulted parameters with no default of its own. 60 occurrences in both renders.

**5.7 `isolated` qualifier dropped.** `client.bal` declares 184 `isolated function`s; neither
render contains the word `isolated` (0 occurrences in both).

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.**

- Extracted every `^public (isolated )?(type|class|const|enum|function|annotation) <Name>` from
  `client.bal` + `types.bal` + `utils.bal` → **587 names**.
- Extracted the same from `new` → **587 names**. `comm` both directions → empty on both sides:
  no missing public symbol, no invented symbol.
- `old` was missing exactly 10 (the `// Unknown type:` set).
- Client methods: 183 source resource functions → 183 rendered; `init` present.
- **No submodule gap.** `package.json` `"export": ["zoom.meetings"]` and the bala contains a
  single module directory `modules/zoom.meetings/`. The default module *is* the whole public API,
  so the known `getDefaultModule()` limitation costs this library nothing.

## 7. Compiler plugin

The package has no compiler plugin. There is no `compiler-plugin/` directory in the bala
(`ls .../1.0.2/any/` → `bala.json  dependency-graph.json  docs  modules  package.json`), no
`[[platform.java21.dependency]]` plugin entry and no `CompilerPlugin.toml` in `ballerina/Ballerina.toml`,
and the upstream repo at `v1.0.2` contains no `*-compiler-plugin` module. Nothing plugin-implied
is therefore missing from the render.

The library does rely on three annotation-driven runtime modules — `ballerina/jsondata`
(`@jsondata:Name`), `ballerina/http` (`@http:Query`) and `ballerina/constraint`. `old` rendered
none of their annotations; `new` renders them. For an OpenAPI-generated connector where every
field is camel-cased away from its wire name, this is the single most consequential fix in the
diff.

## 8. Other considerations

- **Version integrity**: bala `package.json` reports `1.0.2`, built with `ballerina_version
  2201.12.7`; Central metadata for `ballerinax/zoom.meetings/1.0.2` reports `deprecated: null`,
  a single module `zoom.meetings`, pullCount 53. No drift between the two sides.
- **Size**: `new` is +16.1% lines (12144 → 14104) and +26.5% bytes on the JSON
  (1,440,210 → 1,821,914). For a 14k-line render the extra tokens buy correct wire-format names,
  so the trade is favourable, but this library is already among the larger renders and will
  dominate a context window.
- **Naming quality (library, not renderer)**: the OpenAPI generator produced types such as
  `InlineResponse2006InlineResponse2006InlineResponse2006AllOf123` and
  `WebinarswebinarIdsurveyCustomSurveyQuestionsAnswersItemsString`. Both renders reproduce them
  faithfully; they remain hard for an LLM to use.
- **Neither render compiles** as Ballerina (see 5.3/5.5/5.6). That is a shared property of the
  renderer, not of this change.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 12144 / 14104 |
| 2 | `grep -c '^// Unknown type:'` old / new | 10 / 0 (old at L271,1126,4015,4199,5096,5098,7427,7990,8011,10698) |
| 3 | `grep -n '^// --- '` old / new | 4 markers each, same order (README/END README/Types/Client) |
| 4 | `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1`, `v1.0.2` — exact tag exists |
| 5 | `git clone --depth 1 --branch v1.0.2` then `diff -q` on `client.bal`, `types.bal`, `utils.bal`, `README.md` vs bala | all identical |
| 6 | `ls -R <bala>` | single module `modules/zoom.meetings/`; no `compiler-plugin/` |
| 7 | `diff -u old new > d.diff`; `grep -c '^+' / '^-'` | +2040 / −80 content lines |
| 8 | Removed-line taxonomy | 60 resource fns, 10 unknown-type comments, 3 union aliases, 5 `string from?`, 1 `string field?`, 1 `… type?` = 80 |
| 9 | Added-line taxonomy | 1960 annotations, 13 `^type ` lines, 6 `string '…`, 60 resource fns, remainder blanks |
| 10 | Normalised set diff of the 60 removed vs 60 added resource-fn lines after deleting `anydata Additional Values, ` | identical |
| 11 | `comm -23 old.decls new.decls` | empty → nothing lost |
| 12 | `comm -13 old.decls new.decls` | the 10 types listed in §2 |
| 13 | `comm` src.names (587) vs new.names | empty both directions → full coverage, no invention |
| 14 | `comm -23 src.names old.names` | the same 10 → `old` coverage 577/587 |
| 15 | Annotation totals, source `*.bal` vs `new` | jsondata:Name 1704/1724, http:Query 123/123, constraint:String 82/87, constraint:Array 22/22, constraint:Int 3/3, display 1/1, http:Header 0/0 |
| 16 | Triple-set diff (kind, wire-name, field) source vs new | 480 vs 476; only inline-record annotations differ |
| 17 | `grep -c 'value: "play_url"\|"deleted_time"\|"recording_end"\|"recording_start"'` | source 3/2/3/3, new 0/0/0/0 → §5.1 |
| 18 | `grep -cE '^        @jsondata:Name' types.bal` | 37 nested annotations |
| 19 | `types.bal:1074–1100` vs `new:1369` | inline `recordingFiles` record flattened, annotations gone |
| 20 | `grep -c 'resource isolated function' client.bal` vs `grep -c '    resource function'` renders | 183 / 183 / 183 |
| 21 | `grep -c 'isolated function'` renders | 0 / 0 (source: 184) |
| 22 | `grep -cE '^\s+# '` renders | 3212 / 3212 |
| 23 | `grep -cE '^    [^@#/].*;$'` renders | 3479 / 3479 |
| 24 | `diff <(sed -n '8,164p' old) <(sed -n '8,164p' new)` | empty → README block identical |
| 25 | `grep -c '@deprecated'` renders / types.bal | 51 / 51 / 50 |
| 26 | `grep -o 'string from = '` / `'type = '` renders | 16 / 16 and 9 / 9 → §5.3 |
| 27 | `grep -cE '^    .* = .*;$' types.bal` vs `= ` fields in renders | 329 vs 3 / 3 → §5.2 |
| 28 | `grep -c 'meetings:'` renders | 10 / 7 (3 removed were the version-qualified union operands; the 3 remaining path-param refs and 4 README hits are unchanged) |
| 29 | JSON structure compare | typeDefs 587/587, clients 1/1, client functions 184/184, functions 0/0, services 0/0, annotations 0/0 |
| 30 | First differing client function in JSON (`archive_files`) | `old` has a `{"name":"Additional Values","type":{"name":"anydata"}}` parameter; `new` does not — extractor-side change |
| 31 | Central API `packages/ballerinax/zoom.meetings/1.0.2` | not deprecated; 1 module; pullCount 53 |
| 32 | `types.bal:1677` `InlineResponse2006` vs renders | both flatten 7 fields, both drop inherited docs/annotations → §5.4 |
| 33 | col-0 doc-continuation lines in Types section | 1852 / 1852 → §5.5 |

## 10. Caveats and unverified items

- Annotation verification was done by set comparison of `(kind, wire-name, field-name)` triples
  plus targeted spot checks (10 added types, ~15 individual fields), **not** by a line-by-line
  audit of all 1960 added annotation lines. The set comparison covers every distinct triple, so a
  *duplicated* misplacement (same annotation attached to the right field name in one record but
  the wrong one in another) would not be caught. No evidence of such a case was seen.
- `WebinarSurveyObjectCustomSurveyQuestionsAnswersItemsString` was confirmed present in
  `types.bal` by name and confirmed to render as `string`, but its exact source line number was
  not recorded (the other 9 added types have line numbers).
- The claim that the removed `anydata Additional Values` parameter corresponds to the open-record
  rest field of the `*Queries` parameter is an inference from (a) the open record definitions and
  (b) the JSON entry `{"name":"Additional Values","description":"Capture key value pairs",
  "type":{"name":"anydata"},"optional":true}`. The extractor code itself was not read.
- Neither render was fed to a Ballerina compiler; the "does not compile" statements in §5.3/5.5/5.6
  rest on inspection of the emitted syntax, not on a compiler run.
- The 2201.12.x distribution's own view of the package (what `CopilotLibraryManager` actually
  resolved) was not re-derived; the bala on disk was taken as authoritative per the brief.

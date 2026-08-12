# ballerinax/hubspot.crm.engagement.notes 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.engagement.notes` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.engagement.notes |
| Tag reviewed | `v2.0.2` (commit `4013a312858bf3b218ab2a574dddf326d31d73d4`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.engagement.notes/2.0.2` |
| Old render | `784` lines (34,493 bytes) |
| New render | `785` lines (34,092 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. `new` is +1 line and −401 bytes versus `old`. The declaration set is
byte-identical between the two sides (42 top-level declarations: 41 record types + `client class Client`),
the README block is identical and complete, and neither side emits a `// Unknown type:` placeholder.

The four changes are all spec-v2 fixes:

1. 7 version/module-qualified scalar refs `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`.
2. 4 version/module-qualified inline record rest descriptors
   `record {|ballerinax/hubspot.crm.engagement.notes:2.0.2:X...;|}` → `record {|X...;|}`.
3. The module's single `@display {label: "Connection Config"}` annotation is now captured and rendered
   on `ConnectionConfig` (it was silently dropped in `old`).
4. Four bogus `anydata Additional Values` parameters — an invalid Ballerina identifier synthesised from
   the open-record rest field of the `*…Queries` included-record parameters — are gone.

No declaration, parameter, doc line, default value, or README content was lost. Zero regressions.

Several fidelity defects remain in `new`, but every one of them is present verbatim in `old` too, so they
are shared pre-existing renderer limitations, not spec-v2 regressions. They are listed in §5.

## 2. Change inventory

Declaration sets, extracted and sorted from both renders, are identical:

```
grep -oE '^(type|public type|enum|const|class|client class) [A-Za-z0-9_]+' <render> | sort
old = 42 declarations, new = 42 declarations, diff → empty ("DECL SETS IDENTICAL")
```

| Kind | old | new | Added | Removed | Modified |
|---|---|---|---|---|---|
| `type` (record) | 41 | 41 | 0 | 0 | 12 lines across 10 types |
| `client class` | 1 | 1 | 0 | 0 | 1 (3 resource-method signatures) |
| `enum` / `const` / `annotation` / `service` / `listener` / module-level `function` | 0 | 0 | 0 | 0 | 0 |
| `resource function` (client methods) | 11 | 11 | 0 | 0 | 3 |
| `function init` | 1 | 1 | 0 | 0 | 0 |
| Section markers `// --- ` | 4 | 4 | 0 | 0 | 0 |
| `// Unknown type:` | 0 | 0 | — | — | — |

Diff shape (`diff -u old new`): 15 hunks, 16 lines added, 15 removed — matches
`OLD_AND_NEW_DIFFS/hubspot.crm.engagement.notes_diff.md`, which I re-derived rather than copied.

Line-level change classes (all verified by running `diff -u` and by a JSON-section diff):

| Change | Count | Sites |
|---|---|---|
| `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` | 7 | render lines 296, 359, 376, 440, 560, 625, 642 |
| `record {\|<org>/<pkg>:<ver>:T...;\|}` → `record {\|T...;\|}` | 4 | render lines 340, 467, 679, 686 |
| `@display {label: "Connection Config"}` added | 1 | new render line 572 (the only +1 net line) |
| `anydata Additional Values` parameter removed | 4 | new render lines 744, 748, 756, 772 |
| Version-qualified type refs remaining | 11 → 0 | `grep -c` on both files |

JSON-level (`old/*.json` vs `new/*.json`), section by section:

```
name SAME | description SAME | readme SAME (8,864 chars serialised, identical)
functions SAME ([]) | services SAME ([]) | annotations SAME ([])
typeDefs DIFF (35,224 → 34,974 chars) | clients DIFF (12,200 → 11,720 chars)
```

`typeDefs` diff = the 7 `int:Signed32` fixes, the 4 rest-descriptor fixes, and the added
`"annotations": [{"name": "display", "value": "{label: \"Connection Config\"}"}]` block on
`ConnectionConfig`. `clients` diff = removal of the 4 `{"name": "Additional Values", "type":
{"name":"anydata"}, "description":"Capture key value pairs"}` parameter objects. Nothing else.

## 3. Correctness against library source

Upstream `v2.0.2` is byte-identical to the bala for all three source files, so the two authorities agree:

```
diff src/ballerina/client.bal <bala>/modules/.../client.bal  → CLIENT SAME
diff src/ballerina/types.bal  <bala>/modules/.../types.bal   → TYPES SAME
diff src/ballerina/utils.bal  <bala>/modules/.../utils.bal   → UTILS SAME
src/ballerina/Ballerina.toml:5  version = "2.0.2"
```

Verification of what `new` changed:

- **`int:Signed32` (7 sites).** `grep -c 'int:Signed32' types.bal` = **7**, at lines 89 (`'limit`),
  147 (`numErrors`), 199 (`updatedByUserId`), 234 (`total`), 322 (`'limit`), 350 (`numErrors`),
  386 (`associationTypeId`). Exactly the 7 sites `new` rewrote. `new` matches the source spelling;
  `old`'s `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina and appears nowhere in the source.
- **Record rest descriptors (4 sites).** `types.bal:250, 400, 454` declare
  `record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;` and `types.bal:392` declares
  `record {|CollectionResponseAssociatedId...;|} associations?;`. `new` reproduces these verbatim;
  `old` prefixed the element type with `ballerinax/hubspot.crm.engagement.notes:2.0.2:`.
  (The 4th `propertiesWithHistory` at types.bal:250 belongs to `SimplePublicObject`, whose render at
  new:340 now matches character-for-character.)
- **`@display` annotation.** `grep -n '@display' types.bal client.bal` returns exactly one hit —
  `types.bal:260  @display {label: "Connection Config"}` on `public type ConnectionConfig`. `new` renders
  it at line 572 immediately above `type ConnectionConfig record {`. `old` had 0 of 1 annotations.
- **`Additional Values` removal.** The source has no such parameter anywhere. The four affected methods
  are `client.bal:47` (`post batch/read`), `:67` (`get [string noteId]`), `:100` (`patch [string noteId]`)
  and `:170` (`get .`) — precisely the four that take an open `*…Queries` included record. The parameter
  was the extractor surfacing that open record's implicit `anydata` rest field under the label
  "Additional Values" / "Capture key value pairs". It is not a real parameter and `anydata Additional
  Values` is not parseable Ballerina (space in identifier, plus a required param after defaultable ones).
  Removing it is a correctness win.

Broader spot-checks of unchanged content (both sides identical, both correct):

- All 11 resource methods, their accessors, resource paths, payload types and return-type unions match
  `client.bal:47/67/84/100/118/135/152/170/186/203/220`.
- `init` signature `(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v3/objects/notes") returns error?`
  matches `client.bal:31` exactly, including the default URL.
- README: render `readme` field is 8,647 chars and equal to `<bala>/docs/README.md` (8,647 chars),
  head and tail compared — no truncation.
- `ConnectionConfig.auth` union `http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig|ApiKeysConfig`
  matches `types.bal` and carries the cross-package "Special Agent Note" comment on both sides.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Sorted declaration-name sets from both renders: identical (0 added, 0 removed).
- Full `diff -u old new`: 15 hunks, every one inspected line by line; each is one of the four
  improvement classes above. No hunk removes a type, field, method, parameter, doc comment, default
  value, section marker, or README line.
- Per-key JSON diff: `name`, `description`, `readme`, `functions`, `services`, `annotations` are
  byte-identical; the two that differ shrink only by removing the bogus `Additional Values` params and
  the version prefixes, and grow only by adding the `display` annotation.
- Per-method parameter dump from both JSONs (name / optional / default / type, all 12 client functions):
  the only difference is the absence of the `Additional Values` entry in `new`. Every other parameter
  keeps its name, order, optionality and type.
- `// Unknown type:` count 0 on both sides — no degraded types on either side to compare.
- No non-ASCII bytes in `new` (`grep -P '[^\x00-\x7F]'` → no matches), so no encoding damage.

## 5. Issues in `new` (independent of `old`)

All five are also present in `old` — they are renderer limitations, not spec-v2 defects — but they are
inaccuracies a consuming LLM would act on, so they are recorded here per the brief.

1. **Record-field default values dropped; defaulted fields shown as optional.** `types.bal:61, 85, 133`
   declare `boolean archived = false;` and `types.bal:89` declares `int:Signed32 'limit = 10;`. The
   render emits `boolean archived?;` (new:313, 339, 375) and `int:Signed32 'limit?;` (new:376). Four
   defaults lost; optionality semantics changed (a defaultable field is not an optional field).
2. **Invented / wrong defaults on flattened client query params.** `new:772` renders
   `int:Signed32 limit = 0` for `GetCrmV3ObjectsNotesGetPageQueries.'limit`, whose real default is
   `10` (`types.bal:89`) — an actively wrong value. Likewise `string[] associations = []`,
   `string[] propertiesWithHistory = []`, `string[] properties = []`, `string idProperty = ""`,
   `string after = ""` are shown with defaults, but the corresponding source fields are plain optional
   (`string[] associations?` etc., `types.bal:82–96, 130–140, 214`) and have no defaults at all.
3. **Included-record parameter mis-rendered and duplicated.** Source is
   `*PostCrmV3ObjectsNotesBatchReadReadQueries queries` (`client.bal:47`). The render both flattens the
   record's fields into positional params *and* appends `PostCrmV3ObjectsNotesBatchReadReadQueries
   queries` without the `*` and without a default (new:744, 748, 756, 772). The JSON marks `queries`
   `optional: true`, but the `.bal.txt` shows it as a required param following defaultable params —
   not valid Ballerina, and it double-counts the same query arguments.
4. **Resource path `.` dropped.** `client.bal:170` / `:186` declare `resource isolated function get .(…)`
   and `post .(…)`. The render emits `resource function get (` / `resource function post (`
   (new:772, 776) — a syntax error and ambiguous against the sibling `batch/…` paths.
5. **Qualifiers dropped.** `public isolated client class Client` → `client class Client` (new:739);
   `public isolated function init` → `function init` (new:740); `resource isolated function` →
   `resource function` (all 11). Minor, but the render is not a compilable stand-in for the real API.

## 6. Coverage gaps vs. the library

**None.**

- `<bala>/package.json` `"export": ["hubspot.crm.engagement.notes"]` — a single module, no submodules.
  `<bala>/any/modules/` contains exactly one directory. So there is no submodule-only API and no
  shared submodule gap for this library.
- Public symbols in the default module:
  `grep -oE '^public (type|const|enum) [A-Za-z0-9_]+' types.bal utils.bal` → **41** public types
  (0 public consts, 0 public enums), plus `public isolated client class Client` (`client.bal:23`).
  `utils.bal` exports nothing public (its helpers `getPathForQueryParam`, `getEncodedUri` etc. are
  module-private, and the `Encoding`/`EncodingStyle` types are not `public`).
- `comm` of the source symbol list against the render's type/class list:
  "in src not in render" → empty; "in render not in src" → `Client` only (expected; it is the class).
  **41/41 public types + the client are present in both renders.**

## 7. Compiler plugin

No compiler plugin exists for this package.

- `find . -iname '*compiler-plugin*'` in the upstream clone at `v2.0.2` → no results; the repo has no
  `compiler-plugin/` or `ballerina-*-compiler-plugin/` directory (top-level dirs: `ballerina`,
  `build-config`, `docs`, `examples`, `gradle`).
- The bala has no `compiler-plugin/compiler-plugin.json` (`<bala>/any/` contains only `bala.json`,
  `dependency-graph.json`, `docs/`, `modules/`, `package.json`).

Consequently there are no plugin-contributed code actions, validations, generated artifacts, or
annotations that the render could be missing. The one annotation the package does declare (`@display`)
is a plain `ballerina/jballerina`-level display annotation and is now correctly surfaced in `new`.

## 8. Other considerations

- **Not deprecated, stable major.** Central/package metadata: `version 2.0.2`, `graalvmCompatible: true`,
  `template: false`, built with `ballerina_version 2201.12.2`, `language_spec_version 2024R1`. No
  deprecation marker in `package.json` or `bala.json`.
- **Auto-generated connector.** `client.bal:1-2` — "AUTO-GENERATED FILE. DO NOT MODIFY … by the Ballerina
  OpenAPI tool." All the §5 fidelity gaps stem from how the extractor treats OpenAPI-tool idioms
  (`*…Queries` included records, `.` resource paths), so they will reproduce across every HubSpot
  connector in the pinned list — worth fixing once at the extractor rather than per library.
- **Size / tokens.** `new` is 401 bytes smaller than `old` (34,092 vs 34,493) despite one more line: the
  removed version prefixes and `Additional Values` params outweigh the added annotation. A small token
  win on a library that is ~85% README + record definitions.
- **Doc quality is good.** Every rendered record field carries its source doc comment; the README block
  is complete (setup guide, auth, quickstart) and identical on both sides.
- Both renders emit `import ballerinax/hubspot.crm.engagement.notes;` at the top and reference
  `http:BearerTokenConfig` without an `import ballerina/http;` — the "Special Agent Note" comment
  compensates. Unchanged between sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 784 / 785 |
| 2 | `wc -c old/*.bal.txt new/*.bal.txt` | 34,493 / 34,092 |
| 3 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 4 | `grep -n '^// --- '` both | 4 markers each; README 7–199, Types 201, Client 736 (old) / 737 (new) |
| 5 | `diff -u old new` | 15 hunks, +16 / −15; all inspected |
| 6 | `grep -oE '^(type\|public type\|enum\|const\|class\|client class) NAME' \| sort`, then `diff` | 42 vs 42, "DECL SETS IDENTICAL" |
| 7 | `grep -c 'ballerina/lang.int:0.0.0:Signed32' old` | 7 |
| 8 | `grep -c 'int:Signed32' old / new` | 1 / 8 |
| 9 | Python per-key JSON diff | `typeDefs` and `clients` DIFF; all 6 other keys SAME |
| 10 | Python unified diff of `typeDefs` JSON | 7 Signed32 + 4 rest-descriptor rewrites + 1 added `display` annotation block; nothing else |
| 11 | Python unified diff of `clients` JSON | 4 × removal of `{"name":"Additional Values","type":{"name":"anydata"}}`; nothing else |
| 12 | Python dump of all 12 client functions' params, both sides | identical except the 4 `Additional Values` entries |
| 13 | `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2`; `v2.0.2^{}` = `4013a312858bf3b218ab2a574dddf326d31d73d4` |
| 14 | `git clone --depth 1 --branch v2.0.2` then `diff` vs bala for `client.bal`, `types.bal`, `utils.bal` | CLIENT SAME / TYPES SAME / UTILS SAME |
| 15 | `src/ballerina/Ballerina.toml:5` | `version = "2.0.2"` |
| 16 | `grep -c 'int:Signed32' <bala>/types.bal` + line list | 7 at lines 89, 147, 199, 234, 322, 350, 386 |
| 17 | `grep -n 'record {\|…\|}' <bala>/types.bal` | `ValueWithTimestamp[]` at 250, 400, 454; `CollectionResponseAssociatedId` at 392 |
| 18 | `grep -n '@display' <bala>/types.bal client.bal` | one hit: `types.bal:260` |
| 19 | `grep -n '@display' new/*.bal.txt` | one hit: line 572, above `type ConnectionConfig` |
| 20 | `grep -oE '^public (type\|const\|enum) …' types.bal utils.bal \| sort` | 41 public types, 0 consts, 0 enums |
| 21 | `comm -23 src_names render_names` / `comm -13` | empty / `Client` only |
| 22 | `<bala>/any/package.json` `export`, `<bala>/any/modules/` listing | single module `hubspot.crm.engagement.notes` |
| 23 | `find <clone> -iname '*compiler-plugin*'`; `ls <bala>/any` | no plugin in repo; no `compiler-plugin/` in bala |
| 24 | Python compare render `readme` field vs `<bala>/docs/README.md` | both 8,647 chars, equal, tail intact |
| 25 | `grep -n 'boolean archived' <bala>/types.bal` | `= false` at 61, 85, 133; `?` at 246, 396, 448 |
| 26 | `grep -n 'boolean archived?;' new/*.bal.txt` | 6 hits (313, 339, 375, 428, 464, 686) — 3 of them lose a default |
| 27 | `sed -n '86,90p' <bala>/types.bal` vs `new:376` and `new:772` | source `'limit = 10`; render `'limit?` and `limit = 0` |
| 28 | `grep -n 'resource function get (\|resource function post ('` both | old 771/775, new 772/776 — `.` path lost on both |
| 29 | `grep -n 'client class Client\|function init'` new | 739 / 740 — `public isolated` qualifiers dropped |
| 30 | `LC_ALL=C grep -P '[^\x00-\x7F]' new/*.bal.txt` | no matches |
| 31 | Cross-check of `OLD_AND_NEW_DIFFS/hubspot.crm.engagement.notes_diff.md` against re-run diff | all figures (784/785, +16/−15, 15 hunks, 11→0 qualified refs, 0/0 unknown types, 0 decls added/removed) reproduce |

## 10. Caveats and unverified items

- I did not compile either render. Claims that specific rendered lines are "not valid Ballerina"
  (`anydata Additional Values`, `resource function get (`, required `queries` after defaultable params)
  are based on reading the grammar, not on a `bal build` run.
- I did not re-run the two-stage pipeline; I audited the committed renders/JSONs as given. The
  attribution of each change to spec v2 rests on the brief's statement that the library is identical on
  both sides, which is consistent with everything observed (bala == upstream `v2.0.2`, both renders
  reference `2.0.2`).
- `ballerina/http` types referenced from `ConnectionConfig` (e.g. `http:BearerTokenConfig`,
  `http:ClientConfiguration` field types) were not expanded or checked against the `ballerina/http`
  bala; they are out of scope for this module and are rendered identically on both sides.
- Central registry API was not re-queried; package metadata was read from
  `<bala>/any/package.json` and `bala.json`, which the brief designates as authoritative.

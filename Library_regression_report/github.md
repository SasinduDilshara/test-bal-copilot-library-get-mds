# ballerinax/github 6.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/github` |
| Pinned version | `6.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-github |
| Tag reviewed | `v6.0.0` (commit `6c959b894dca076f6060d1339993118e630fff35`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/github/6.0.0/any` |
| Old render | `22880` lines |
| New render | `26408` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` in information content. Every one of the 64 `// Unknown type:`
placeholders in `old` is replaced by a real, source-exact type alias definition plus its doc comment;
all 170 occurrences of the version-qualified `ballerinax/github:6.0.0:Type` form are replaced by the
plain type name exactly as the library declares it; 3,492 annotation instances
(`@jsondata:Name`, `@http:Query`, `@constraint:*`, `@display`) that `old` dropped entirely are now
emitted and match the published source as an exact multiset; 14 record fields named with the reserved
word `type` are now correctly escaped as `'type`; and a bogus, non-compiling parameter
`anydata Additional Values` is removed from 259 client resource-function signatures.

After normalising for exactly those changes, the two renders are byte-identical
(`diff` residual = 64 lines, all accounted for below). **Nothing was lost.** No declaration,
parameter, default, return type, doc line or README line present in `old` is missing from `new`.

The `@jsondata:Name` recovery is the materially important one for this library: `ballerinax/github`
is an OpenAPI-generated connector whose Ballerina record fields are camelCase while the GitHub wire
format is snake_case. `old` rendered `string expiresAt;` with no indication that the JSON key is
`expires_at`. `new` renders the `@jsondata:Name {value: "expires_at"}` annotation, which is the only
thing in the render that carries the wire-name mapping.

## 2. Change inventory

Line counts (`wc -l`): old `22880`, new `26408` (+3,528, +15.4%).
Raw `diff`: 3,935 added lines, 407 removed lines, 1,043 hunks.

| Kind | old | new | Δ |
|---|---|---|---|
| `// --- section ---` markers | 4 | 4 | 0 |
| README body lines (render lines 8–119) | 112 | 112 | 0 (byte-identical) |
| `// Unknown type:` placeholders | 64 | 0 | −64 |
| `type X …` declarations | 1163 | 1227 | +64 |
| Distinct type names present (defs + stubs) | 1227 | 1227 | 0 |
| Client classes | 1 | 1 | 0 |
| Client methods (`init` + resource functions) | 904 | 904 | 0 |
| Standalone `function` / `enum` / `const` / `annotation` / `service` / `listener` decls | 0 | 0 | 0 |
| Record-field lines (`^    …;`) | 7647 | 7647 | 0 |
| Indented doc-comment lines (`^    # `) | 8476 | 8476 | 0 |
| `ballerinax/github:6.0.0:` qualified refs (occurrences / lines) | 170 / 70 | 0 / 0 | −170 |
| `@jsondata:Name` | 0 | 3165 | +3165 |
| `@http:Query` | 0 | 286 | +286 |
| `@constraint:Array` / `:Int` / `:String` / `:Number` | 0 | 14 / 6 / 20 / 1 | +41 |
| `@display` | 0 | 1 | +1 |
| Fields escaped as `'type;` | 73 lines | 87 lines | +14 |
| File size (bytes) | 966,325 | 1,111,744 | +15.0% |
| Rough token estimate (chars/4) | ~241.6k | ~277.9k | +36.4k |

### 2a. Declarations added (64) — all previously `// Unknown type:` stubs

Set equality verified: `comm -13 old.types new.types` yields exactly 64 names, and
`comm -23 old.unknown new.types` yields **zero** — i.e. every name that `old` stubbed out is a real
definition in `new`, and nothing else was added. All 64 are simple type aliases (none are records):
`grep -c '^type <name> record' → 0` for all 64.

Representative sample (render line → definition, all confirmed identical to source):

| Type | `new` render | `types.bal` |
|---|---|---|
| `ReposownerrepobranchesbranchprotectionrestrictionsappsreposownerrepobranchesbranchprotectionrestrictionsappsOneOf12` | `string[]` (L124) | L21 |
| `SearchResultTextMatches` | `SearchResultTextMatchesInner[]` (L1356) | L19703 |
| `WebhookConfigUrl` | `string` (L2224) | L4293 |
| `ActionsEnabled` | `boolean` (L3943) | L15065 |
| `DependencyGraphDiff` | `DependencyGraphDiffInner[]` (L3928) | L1353 |
| `WaitTimer` | `int` (L7038) | L6892 |
| `AlertNumber` | `int` (L9244) | L5050 |
| `RuleSuites` | `RuleSuitesInner[]` (L11309) | L6732 |
| `ContentDirectory` | `ContentDirectoryInner[]` (L15899) | L12745 |
| `CodeFrequencyStat` | `int[]` (L20703) | L18264 |
| `PreventSelfReview` | `boolean` (L21567) | L19701 |

### 2b. Declarations removed

**None.** `comm -23 old.types new.types` → empty. `comm -23 old.mnames new.mnames` → empty.

### 2c. Declarations modified

- **32 top-level union aliases** lost their `ballerinax/github:6.0.0:` prefixes
  (e.g. `type Cwes ballerinax/github:6.0.0:CwesOneOf1|…` → `type Cwes CwesOneOf1|CwesCwesOneOf12;`).
  All 32 verified equal to the source RHS.
- **38 record-field lines** lost the same prefix
  (e.g. `ballerinax/github:6.0.0:AlertDismissedAt? dismissedAt;` → `AlertDismissedAt? dismissedAt;`).
- **259 client resource functions** lost the parameter `anydata Additional Values`.
- **14 record fields** `… type;` → `… 'type;`.
- **1 type** (`ConnectionConfig`) gained `@display {label: "Connection Config"}`.
- **35 doc-comment lines** added, all belonging to the 64 restored aliases.
- **3,492 annotation lines** added inside records and on 3 type aliases.

### 2d. Normalised residual

```
new  minus annotation-only lines, minus the 64 restored type-alias lines   → new.norm2 (22852 L)
old  with 'ballerinax/github:6.0.0:' stripped, 'anydata Additional Values, '
     stripped, and '// Unknown type:' lines removed                        → old.norm  (22816 L)
diff old.norm new.norm2  →  64 changed lines total
```
Those 64 break down as: 35 `# ` doc lines added (docs of restored aliases), 14 `type;`→`'type;`
pairs (14 `<` + 14 `>`), 1 `@display` line. Nothing else differs anywhere in the file.

## 3. Correctness against library source

The bala and the `v6.0.0` GitHub tag are byte-identical for all three source files
(`diff -q` on `client.bal`, `types.bal`, `utils.bal` → no differences; 11344 / 21546 / 216 lines).
So GitHub source and what the extractor consumed are the same artefact.

1. **64 restored aliases — 100% exact.** Scripted comparison of the render RHS against
   `public type <name> <RHS>;` in `types.bal`: `exact-match: 64  mismatch: 0`.
2. **64 restored doc comments — 100% exact.** Scripted comparison of the doc block preceding each
   restored alias against the doc block preceding the source declaration: `docs match: 64 mismatch: 0`.
3. **32 union aliases — 100% exact** after prefix stripping: `union-alias ok=32 bad=0`; each also
   equals the source line verbatim.
4. **3,492 annotation instances — exact multiset match with source.** Sorted+counted annotation
   lines from `types.bal`+`client.bal` vs. the new render: `diff` → identical, 876 distinct forms.
   Includes the regex constraint
   `` @constraint:String {pattern: re `^ssh-(rsa|dss|ed25519) |^ecdsa-sha2-nistp(256|384|521) |^(sk-ssh-ed25519|sk-ecdsa-sha2-nistp256)@openssh.com `} ``, reproduced character-for-character.
5. **Annotation placement verified.** 3,492 (annotation, next-declaration) adjacency pairs extracted
   from both source and render. 3,039 match exactly; the 453 that do not differ *only* because the
   render turns `field = <default>;` into `field?;` (a pre-existing transformation present in `old`
   too) — e.g. src `@http:Query {name: "per_page"} ||| int perPage = 30;` vs
   new `@http:Query {name: "per_page"} ||| int perPage?;`. No annotation is attached to the wrong field.
6. **`'type` escaping.** All 14 newly escaped fields match source, e.g. `types.bal:3115`
   `"required_deployments" 'type;`. `new` has **0** unescaped ` type;` field lines; `old` had 14.
7. **`@display`** matches `types.bal:17127` (`@display {label: "Connection Config"}` immediately
   above `public type ConnectionConfig record {|`).
8. **Client surface.** Source `client.bal` has 903 `resource isolated function` + 1
   `public isolated function init` = 904; render has exactly 904, with identical accessor+path set on
   both sides. `init` signature in render
   `function init(ConnectionConfig config, string serviceUrl = "https://api.github.com") returns error?;`
   matches `client.bal:28`.
9. **README** in the render is byte-identical to `docs/README.md` in the bala (only a trailing blank
   line differs), and identical between `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Type-name set: `comm -23 old.types new.types` → empty (no type dropped).
- Client method-name/path set: `comm -23 old.mnames new.mnames` → empty (no method dropped).
- Client signatures: `sed 's/anydata Additional Values, //' old.methods` diffed against `new.methods`
  → **identical**. So no parameter, default, or return type changed except the removal of the bogus
  `Additional Values` pseudo-parameter.
- Client JSON model: 904 functions on both sides; 259 differ; a script confirmed
  `diffs explained solely by removing 'Additional Values' param: 259` — i.e. all 259 are that and
  nothing else.
- Record-field line count (7647) and indented doc-line count (8476) identical.
- README block byte-identical.
- Normalised whole-file diff → 64 lines, all additions/fixes (§2d).
- JSON: `typeDefs` count 1227 on both sides, name sets equal, category histogram identical
  (`Record 1101 / Other 64 / Union 62`). `new` adds a `baseType` field on `Other` entries
  (e.g. `WaitTimer` gains `"baseType": "int"`); no field was removed from any entry.

The only thing `new` no longer conveys is that the 259 `*XQueries` records are *open* (the
`anydata...;` rest descriptor, which `old` surfaced as the parameter `anydata Additional Values`).
That representation was syntactically invalid Ballerina (an identifier containing a space, placed
after defaulted parameters) and would have misled a consumer far more than its absence does. I count
this as a fix, not a regression.

## 5. Issues in `new` (independent of `old`)

All of the following are present **identically in `old`**, so none is caused by spec v2, but they are
real inaccuracies in the `new` render that a reviewer should know about.

1. **Record-field default values are dropped and the field is turned optional.** `types.bal` has
   760 record fields with defaults; the render's Types section has **0**
   (`grep -cE '^    [^#@/].* = .*;$'` → src 760, new 0, old 0). E.g. source
   `int perPage = 30;` renders as `int perPage?;`, `"asc"|"desc" direction = "desc";` renders as
   `"asc"|"desc" direction?;`. An LLM reading this cannot know the server-side defaults.
2. **Client resource signatures duplicate the query record and fabricate its defaults.** Source
   declares 259 resource functions with an included-record parameter `*XQueries queries`
   (`grep -c '\*[A-Za-z]*Queries queries)' client.bal` → 259). The render flattens the record's
   fields into the parameter list *and* additionally emits `XQueries queries` — a duplicate,
   non-compiling signature. Worse, the flattened defaults are invented, not read from the record:
   `int perPage = 0` appears 232 times in both renders while the source value is `30` in 226 places
   (`grep -c 'perPage = 30'` in the render → 0); `"asc"|"desc" direction = "asc"` appears 36 times
   while the source declares `= "desc"` in 26 places and `= "asc"` in 1; optional-with-no-default
   fields get invented values (`severity = "unknown"`, `before = ""`, `isWithdrawn = false`).
   Compare render L22801 with `client.bal:47` + `types.bal:SecurityAdvisoriesListGlobalAdvisoriesQueries`.
3. **Reserved word `type` unescaped in client parameter lists.** 4 resource-function signatures on
   each side carry a parameter literally named `type` (should be `'type`), e.g.
   `"reviewed"|"malware"|"unreviewed" type = "reviewed"` in `resource function get advisories`.
   `new` fixed this for record fields but not for client parameters.
4. **Closed records rendered as open.** `types.bal` declares 42 top-level `record {|…|}` types;
   both renders emit only 2 as `record {|` — the other 40 (including `ConnectionConfig`,
   `PublicUser`, `DependabotAlertSecurityAdvisoryIdentifiers`) become open `record {`.
5. **Multi-line doc comments break out of the comment.** 222 lines in the Types section of both
   renders start at column 0 without a `#` prefix — continuation lines of multi-paragraph docs
   (e.g. `- PR_TITLE - default to the pull request's title.` at render L217). This is invalid
   Ballerina and can confuse a parser or a model.
6. **Type-inclusion flattening drops the inclusion and the inherited docs.** Source
   `RepositoryRuleDetailedOneOf1 { *RepositoryRuleCreation; *RepositoryRuleRulesetInfo; }`
   (`types.bal:11304`) renders as an explicit 4-field record with no doc comments on the inherited
   fields (render L15464). This adds 14×3 duplicated `ruleset_*` field lines across the file.
7. **The render is not self-contained.** It emits `@jsondata:…`, `@http:…`, `@constraint:…` and
   `http:BearerTokenConfig` while the only import line is `import ballerinax/github;`. This is by
   design for a context blob, not a compilable unit, but it means the render cannot be pasted and
   compiled.

`T?` in source is rendered as `T|()` (e.g. `NullableSimpleUser? user;` → `NullableSimpleUser|() user;`,
18 occurrences). This is semantically equivalent and identical on both sides — noted, not counted as
an issue.

## 6. Coverage gaps vs. the library

**Zero gaps.**

- The bala exports exactly one module: `package.json` `"export": ["github"]`, and
  `modules/` contains only `github` — i.e. the default module is the entire public API, so the known
  "submodule API not extracted" shared gap does not apply here.
- `grep -hoE '^public type [A-Za-z0-9_]+' *.bal` over the source → **1227** distinct public types.
  `new` render declares **1227** types. `comm` in both directions → **empty**: no source type is
  missing from the render, and the render invents no type that the source does not declare.
- Source has **0** public standalone functions, **0** public enums, **0** public constants,
  **0** public annotations, **0** listeners, **0** services
  (`grep -hnE '^public (isolated )?(function|class|const|enum|annotation|listener|service)'` returns
  only the client class).
- Source has exactly one public class — `public isolated client class Client` (`client.bal:21`) —
  rendered, with all 903 resource functions plus `init`.
- Ballerina Central metadata for `ballerinax/github/6.0.0` lists a single module `github`,
  confirming the above.

## 7. Compiler plugin

`ballerinax/github` **ships no compiler plugin**:

- The bala has no `compiler-plugin/` directory (`ls` of the bala root shows only
  `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`).
- `Ballerina.toml` at `v6.0.0` has no `[[tool …]]`, `[[plugin]]` or `compilerPlugin` section.
- No `compiler-plugin` / `*-compiler-plugin` directory exists anywhere in the repo at `v6.0.0`.

Consequently there are no plugin-contributed code actions, validations, generated artifacts or
annotations that ought to surface in the render, and nothing is absent on that account.

## 8. Other considerations

- **Not deprecated.** Central metadata for `6.0.0` reports no deprecation; version is a stable
  major (`6.0.0`), `pullCount` 595, built for distribution `2201.13.0`, `graalvmCompatible: true`.
- **Size / token cost.** `new` is 15% larger: 1,111,744 bytes vs 966,325 (~278k vs ~242k tokens at
  4 chars/token). The +36k tokens buy 3,492 wire-name/validation annotations and 64 real type
  definitions. For a connector this large the whole render is unlikely to fit a single context
  window either way; the growth is proportionate and the content is high-value.
- **Doc quality is good and unchanged** — 8,476 indented doc lines carried through identically,
  sourced from the GitHub OpenAPI descriptions.
- **Naming.** The library carries machine-generated type names up to 175 characters
  (e.g. `ReposownerrepoissuesissueNumberlabels…OneOf112345`). That is the library's own naming, faithfully
  reproduced on both sides; it is a readability problem for an LLM but not a render defect.
- **The 64 restored aliases are mostly semantically thin** (`string`, `int`, `boolean`, `X[]`), but
  several are load-bearing constituents of unions that the render *does* reference — e.g. `Cwes`,
  `Affects`, `ContentDirectory`, `StargazerResponseAnyOf1` — so in `old` those unions pointed at
  names with no definition anywhere in the file. `new` closes that dangling-reference hole entirely.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/new render` | 22880 / 26408 |
| 2 | `grep -c '^// Unknown type:'` old / new | 64 / 0 |
| 3 | `grep -n '^// --- '` old / new | 4 markers each, same names |
| 4 | `git ls-remote --tags …module-ballerinax-github` | `v6.0.0` → `6c959b894dca076f6060d1339993118e630fff35` |
| 5 | `git clone --depth 1 --branch v6.0.0` | succeeded |
| 6 | `diff -q` bala `client.bal`/`types.bal`/`utils.bal` vs repo `ballerina/` | identical (11344 / 21546 / 216 lines) |
| 7 | `ls bala/…/modules` | only `github` → single-module package |
| 8 | `cat bala/…/package.json` | `"export": ["github"]`, `ballerina_version 2201.13.0` |
| 9 | `ls bala/…/compiler-plugin` | does not exist |
| 10 | `grep -oE '^type X' \| sort -u` old / new | 1163 / 1227 |
| 11 | `comm -23 old.types new.types` | empty (nothing removed) |
| 12 | `comm -13 old.types new.types` | 64 names |
| 13 | `comm -23 old.unknown new.types` | empty (all 64 stubs now defined) |
| 14 | scripted RHS comparison of the 64 vs `types.bal` | `exact-match: 64  mismatch: 0` |
| 15 | scripted doc-block comparison of the 64 vs source | `docs match: 64 mismatch: 0` |
| 16 | `grep -m1 '^type <n> record'` for each of the 64 | 0 → all are plain aliases |
| 17 | `grep -c 'ballerinax/github:6\.0\.0:'` old / new (lines) | 70 / 0; occurrences 170 / 0 |
| 18 | scripted union-alias comparison (32) vs source | `union-alias ok=32 bad=0` |
| 19 | client method sets (`sed 's/(.*//' \| sort -u`) | 904 / 904, `comm` both ways empty |
| 20 | `diff <(sed 's/anydata Additional Values, //' old.methods) new.methods` | **IDENTICAL** |
| 21 | `comm -23 old.methods new.methods \| grep -c 'anydata Additional Values'` | 259 of 259 |
| 22 | JSON: `clients[0].functions` length old / new | 904 / 904; 259 differ |
| 23 | JSON: script "diffs explained solely by removing 'Additional Values'" | 259 |
| 24 | JSON sample of that param | `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}` |
| 25 | JSON `typeDefs` count / name-set / category histogram | 1227 both; sets equal; `Record 1101 / Other 64 / Union 62` both |
| 26 | JSON `Other` entries | `new` adds `baseType` (e.g. `WaitTimer` → `"baseType":"int"`) |
| 27 | `grep -c '@jsondata:Name'` old / new / source `types.bal` | 0 / 3165 / 3165 |
| 28 | `grep -c '@http:Query'` new / source | 286 / 286 |
| 29 | `@constraint:Array/Int/String/Number` new vs source | 14/6/20/1 vs 14/6/20/1 |
| 30 | annotation multiset `diff src.annots new.annots` | **ANNOTATIONS IDENTICAL (multiset)**, 876 distinct forms |
| 31 | annotation→declaration adjacency pairs (script) | 3492 both; 3039 exact; 453 differ only by default→optional |
| 32 | `grep -cE '^    [^#@/].* type\??;$'` old / new | 14 / 0 (reserved word now escaped) |
| 33 | `grep -c "'type"` old / new / source | 73 / 87 / 72 lines (delta = 14 fixes + 15 inclusion-flattened duplicates) |
| 34 | `grep -n '@display'` new / source | render L19665 / `types.bal:17127` |
| 35 | normalised residual `diff old.norm new.norm2` | 64 lines: 35 doc adds, 14+14 `'type`, 1 `@display` |
| 36 | record-field line count old / new | 7647 / 7647 |
| 37 | indented doc-line count old / new | 8476 / 8476 |
| 38 | `diff` README block (render L8–119) vs bala `docs/README.md` | identical but a trailing blank line |
| 39 | source public types (`grep -hoE '^public type X'`) | 1227; `comm` vs new render → empty both ways |
| 40 | source public functions / enums / consts / annotations / listeners / services | 0 each |
| 41 | source client methods | 903 `resource isolated function` + 1 `init` = 904 |
| 42 | `grep -cE '^    [^#@/].* = .*;$'` source `types.bal` / new Types section / old Types section | 760 / 0 / 0 |
| 43 | `grep -c '\*[A-Za-z]*Queries queries)'` source `client.bal` | 259 (all flattened + duplicated in render) |
| 44 | `int perPage = 0` occurrences new / old; `perPage = 30` in render; source `int perPage = 30;` | 232 / 232; 0; 226 |
| 45 | `"asc"\|"desc" direction = "asc"` in new; source `= "desc"` / `= "asc"` | 36; 26 / 1 |
| 46 | top-level `record {\|` source / new render | 42 / 2 |
| 47 | col-0 non-`#` doc continuation lines in Types section, old / new | 222 / 222 |
| 48 | `grep -c 'Special Agent Note'` old / new | 16 / 16 |
| 49 | file sizes old / new | 966,325 B / 1,111,744 B |
| 50 | Central `GET /2.0/registry/packages/ballerinax/github/6.0.0` | 1 module `github`, no deprecation flag, `pullCount` 595 |

## 10. Caveats and unverified items

- **Not verified:** that the `new` render is *syntactically valid Ballerina*. I did not run
  `bal build` over the render (it is not a compilable unit — it lacks the `jsondata`/`http`/
  `constraint` imports and its client class body is elided). Syntax observations in §5 are from
  reading, not from a parser.
- **Not verified:** the exact ballerina-vscode commits (`eb5d81b3` / `412ba01e`) that produced these
  renders. I took the brief's statement at face value; I did not re-run either pipeline.
- **Deprecation status** was read from the Central `2.0/registry/packages` response, which did not
  include a `deprecated` key for this version. I read the absence of the key as "not deprecated";
  I did not confirm via a second endpoint.
- **`@constraint` on client parameters:** the source declares constraints only inside the `*Queries`
  records, and the render's flattened client parameter list does not carry them. Because the render
  also emits the `XQueries queries` parameter (whose record definition *does* carry the constraints),
  the information is not lost from the file — but I did not exhaustively confirm that every
  constrained query field is reachable that way.
- The 453 annotation-adjacency mismatches (§3.5) were attributed to the default→optional
  transformation by inspecting the top 15 of each side, all of which fit that pattern exactly, plus
  the independent finding that the render emits 0 defaulted record fields against 760 in source.
  I did not individually classify all 453.

# ballerinax/hubspot.marketing.emails 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.emails` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.emails |
| Tag reviewed | `v1.0.2` (commit `0790578291939bf6d85819c456ab7fb9e80b1d35`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.emails/1.0.2` |
| Old render | `1010` lines |
| New render | `1011` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module HTTP connector generated from an OpenAPI spec. Public API of the default module is
exactly one client class (`Client`, 1 `init` + 19 resource methods) and 41 public record types.
Both renders cover 100% of that API — identical declaration sets, identical README block, zero
`// Unknown type:` placeholders on either side.

`new` differs from `old` in exactly three ways, all corrections:

1. 15 record fields whose type was mis-rendered as `ballerina/lang.int:0.0.0:Signed32` are now the
   correct `int:Signed32`.
2. 2 inline map types mis-rendered as `record {|ballerinax/hubspot.marketing.emails:1.0.2:X...;|}`
   are now `record {|X...;|}`.
3. 7 resource signatures no longer carry the bogus, non-compiling parameter
   `anydata Additional Values`.
4. `ConnectionConfig` now carries its real `@display {label: "Connection Config"}` annotation,
   which `old` dropped entirely.

Nothing was removed or degraded. Every remaining inaccuracy in `new` is byte-for-byte present in
`old` as well.

## 2. Change inventory

Declaration-set comparison (extracted and sorted, not raw text):

| Kind | old | new | delta |
|---|---|---|---|
| Type definitions | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `resource function` | 19 | 19 | 0 |
| Module-level functions | 0 | 0 | 0 |
| Services / listeners | 0 | 0 | 0 |
| Enums / consts | 0 | 0 | 0 |
| Annotations rendered | 0 | 1 | **+1** |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version/module-qualified type refs | 17 | 0 | **−17** |

`diff old_types.txt new_types.txt` → empty. No declaration added, none removed.

Modified lines, by category (from the JSON diff, which is the ground truth for the render):

| Change | count |
|---|---|
| `"ballerina/lang.int:0.0.0:Signed32"` → `"int:Signed32"` | 15 |
| `record {\|ballerinax/hubspot.marketing.emails:1.0.2:SmartEmailField...;\|}` → `record {\|SmartEmailField...;\|}` | 1 |
| `record {\|…:EmailStatisticsData...;\|}` → `record {\|EmailStatisticsData...;\|}` | 1 |
| Removal of synthetic param `Additional Values` (`anydata`, optional, doc "Capture key value pairs") | 7 |
| `annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]` added to `ConnectionConfig` | 1 |

The 7 removed `Additional Values` params correspond exactly to the 7 resource methods that take an
included-record query param in the source (`statistics/list`, `statistics/histogram`,
`[emailId]/revisions`, `get .`, `get [emailId]`, `delete [emailId]`, `patch [emailId]`).

Section boundaries are unchanged; the +1 net line is the `@display` line at new:763.

## 3. Correctness against library source

Upstream clone at `v1.0.2` was diffed against the bala module directory:
`diff -r src/ballerina <bala>/modules/hubspot.marketing.emails --brief` reports differences only for
build files (`Ballerina.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png`,
`tests/`). `client.bal`, `types.bal`, `utils.bal` are byte-identical. GitHub and the bala agree, so
either can be cited.

Verified for each of `new`'s changes:

- **`int:Signed32` (15 sites).** `grep -c "int:Signed32" types.bal` → **15**, at lines
  43, 49, 149, 169, 366, 386, 404, 468, 482, 484, 514, 516, 562, 572, 636. The `new` Types section
  (lines 204–930) contains **15** occurrences; `old` contains **0**. Exact 1:1 match. `old`'s
  `ballerina/lang.int:0.0.0:Signed32` is not a writable Ballerina type reference.
- **`record {|SmartEmailField...;|}`.** `types.bal:673` reads
  `record {|SmartEmailField...;|} smartFields?;` — `new:382` matches verbatim; `old:382` had the
  self-qualified `ballerinax/hubspot.marketing.emails:1.0.2:` prefix, which is invalid inside the
  module's own render.
- **`record {|EmailStatisticsData...;|}`.** `types.bal:586` — `new:880` matches verbatim.
- **`@display {label: "Connection Config"}`.** `types.bal:302` carries exactly this annotation, and
  it is the **only** annotation anywhere in the module (`grep -nE "^\s*@" *.bal` → 1 hit). `new`
  renders exactly 1 `@display`; `old` renders 0.
- **`Additional Values` removal.** No such symbol exists anywhere in the library source. All 7
  affected methods use included-record params (`*GetQueries queries` etc., `client.bal:47, 97, 197,
  262, 314, 332, 350`). The token `anydata Additional Values` is not a legal Ballerina parameter
  (space in identifier); removing it is a correction.

Resource-method spot check against `client.bal` (all 19 verified by name, path, payload param and
return type):

- `client.bal:31` `init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/marketing/v3/emails") returns error?` — new:934 matches.
- `client.bal:79` `post ab\-test/create\-variation(AbTestCreateRequestVNext payload, …) returns PublicEmail|error` — new:945 matches, escaping preserved.
- `client.bal:146` `post [string emailId]/revisions/[int revisionId]/restore\-to\-draft(…) returns PublicEmail|error` — new:961 matches.
- `client.bal:230` `get [string emailId]/revisions/[string revisionId](…) returns VersionPublicEmail|error` — new:981 matches.
- `client.bal:350` `patch [string emailId](EmailUpdateRequest payload, …, *PatchEmailIdQueries queries) returns PublicEmail|error` — new:1010 matches modulo the shared included-param issue in §5.

Type-set check: the 41 `public type` names in `types.bal` and the 41 type names in the `new` render
are the same set (`comm -23` and `comm -13` both empty).

## 4. Regressions

**None found.**

Basis for that conclusion:

- `diff old_types.txt new_types.txt` → empty (no type lost).
- Resource-function count 19 on both sides; `diff` of the two renders shows no `-` line that removes
  a declaration, a doc comment, a parameter of the real signature, a return type, or a default.
- `diff` of README region (old:7–202 vs new:7–202) → identical.
- Section markers identical (4 on each side, same names).
- Structured JSON diff: 273 diff lines total, and every `-` line falls into one of the four
  corrections in §2. No field, no member, no doc string is present in `old.json` and absent in
  `new.json` other than the 7 synthetic `Additional Values` params.
- `// Unknown type:` count is 0 on both sides, so the usual spec-v2 win does not apply here and
  there is no chance of a spec-v2 replacement being worse than the placeholder.

The only thing `new` "loses" is the 7 `Additional Values` pseudo-parameters. Those signalled that
the `*Queries` records are open records (all 7 are declared `record {` — `types.bal:269, 372, 400,
410, 416, 500, 610`). That signal is now gone, but it was encoded as illegal syntax that no LLM
could reproduce, and the `GetQueries queries` parameter still names the record. Net effect is
positive; not counted as a regression.

## 5. Issues in `new` (independent of `old`)

All six below are identical in `old` — they are renderer-wide behaviours, not spec-v2 defects.
Listed because they misrepresent the library to a consumer.

1. **`public` and `isolated` qualifiers dropped.** Source declares `public isolated client class
   Client` (`client.bal:23`), `public isolated function init` (`:31`), `resource isolated function …`
   and `public type X` for all 41 types. The render emits `client class Client`, `function init`,
   `resource function …`, `type X`. An LLM copying this produces module-private types.
2. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:302`) and `ApiKeysConfig` are
   `record {|…|}`; both renders emit `record {`. Sealedness is lost.
3. **Record field defaults dropped and required fields turned optional.** `ConnectionConfig` in
   source has 9 fields with defaults (`httpVersion = http:HTTP_2_0`, `http1Settings = {}`,
   `http2Settings = {}`, `timeout = 30`, `forwarded = "disable"`, `cache = {}`,
   `compression = http:COMPRESSION_AUTO`, `responseLimits = {}`, `socketConfig = {}`, plus
   `validation = true`, `laxDataBinding = true`). The render emits every one as `field?;` with no
   default. `grep -c ' = '` over the Types section is **0** on both sides — no record default
   survives anywhere in the render.
4. **Included-record params expanded *and* kept.** Source: `resource isolated function get
   statistics/list(map<string|string[]> headers = {}, *GetStatisticsListQueries queries)`. Render:
   the four record fields are inlined as separate params *and* `GetStatisticsListQueries queries` is
   appended. The result is a duplicated parameter list and non-compiling Ballerina (a required
   param after defaulted params, and the `*` is dropped).
5. **Invented defaults on the expanded query params.** All `*Queries` record fields are optional with
   no default (e.g. `int:Signed32 'limit?;` at `types.bal:404`), yet the render gives them concrete
   defaults: `int:Signed32 limit = 0`, `string before = ""`, `string[] sort = []`,
   `"AB_EMAIL"|… type = "AB_EMAIL"`. `limit = 0` in particular contradicts the doc string "Default
   is 100".
6. **Two syntax defects in the emitted text.**
   - Multi-line doc comment continuation loses its `# ` prefix: line `and absent fields are handled
     as \`nilable\` types. Enabled by default` sits at column 0 inside the `ConnectionConfig` body
     (old:803, new:804).
   - The root resource path `.` is emitted as nothing: source `resource isolated function get
     .(…)` (`client.bal:262`) becomes `resource function get (…)` (new:993), likewise
     `post .` → `resource function post (…)` (new:997).

## 6. Coverage gaps vs. the library

**0 gaps.**

- `package.json` `export` lists exactly one module: `hubspot.marketing.emails`. The bala has one
  directory under `modules/`, so there is no submodule API and no shared submodule gap.
- Complete set of `public` symbols in the module (`grep -nE "\bpublic\b" *.bal`): `Client`
  (`client.bal:23`), `Client.init` (`client.bal:31`), and 41 `public type` declarations in
  `types.bal`. Nothing public in `utils.bal` — its 6 functions and `enum EncodingStyle`
  (`utils.bal:37`) are module-private, so their absence from the render is correct.
- All 41 types and the client (init + 19 resources) appear in both renders. `comm` between the bala
  type list and the render type list is empty in both directions.

## 7. Compiler plugin

None. Neither the upstream repo at `v1.0.2` (`ls src` → `LICENSE README.md ballerina build-config
build.gradle docs examples gradle gradle.properties gradlew gradlew.bat settings.gradle`) nor the
bala (`ls <bala>/any` → `bala.json dependency-graph.json docs modules package.json`) contains a
`compiler-plugin` directory or `compiler-plugin.json`. No plugin-contributed code actions,
validations, or generated artifacts exist, so nothing plugin-implied is missing from the render.

## 8. Other considerations

- `package.json` reports `graalvmCompatible: true`, `ballerina_version: 2201.12.2`,
  `template: false`. Not deprecated on Central; no deprecation marker in the bala metadata.
- Version 1.0.2 is a stable 1.x release, so the render is safe to treat as a fixed API surface.
- Size is modest (1011 lines). 726 of them are the Types section and 194 the README; the README is
  reproduced in full from `<bala>/docs/README.md` (193 lines) and is identical on both sides.
- The render carries `// Special Agent Note: X FROM ballerina/http package` trailer comments on
  cross-package types (`http:BearerTokenConfig`, `oauth2:ClientConfiguration`, …). Identical on both
  sides; useful disambiguation, no `import` lines are emitted for `ballerina/http` or
  `ballerina/oauth2` in the render header, which lists only
  `import ballerinax/hubspot.marketing.emails;`.
- `new` is strictly cheaper to tokenise for the same information: the 17 removed
  `org/module:version:` prefixes and 7 removed pseudo-params shorten the text while the file grows
  by one line only because of the added annotation.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 1010 / 1011 |
| 2 | `ls -R <bala>` | one module `hubspot.marketing.emails`; `client.bal`, `types.bal`, `utils.bal`; no `compiler-plugin` |
| 3 | `wc -l <bala>/modules/…/*.bal` | client 363, types 696, utils 219 |
| 4 | `cat <bala>/any/package.json` | version 1.0.2, `export: ["hubspot.marketing.emails"]`, graalvmCompatible true |
| 5 | `git ls-remote --tags <repo>` | `v0.1.0 v1.0.0 v1.0.1 v1.0.2`; exact tag `v1.0.2` exists |
| 6 | `git clone --depth 1 --branch v1.0.2` | HEAD `0790578291939bf6d85819c456ab7fb9e80b1d35`, tag v1.0.2 |
| 7 | `diff -r src/ballerina <bala>/modules/… --brief` | only build files differ; `client.bal`/`types.bal`/`utils.bal` identical |
| 8 | `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| 9 | `grep -cE "[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:"` old / new | 17 / 0 |
| 10 | `grep -n '^// --- '` new | 4 markers: README(7), END README(202), Types(204), Client(931) |
| 11 | `grep -c "resource function"` old / new | 19 / 19 |
| 12 | `grep -cE "function"` `<bala>/client.bal` | 1 `init` + 19 `resource isolated function` |
| 13 | type-name set diff old vs new | empty |
| 14 | `comm -23 bala_types new_types` / `comm -13` | both empty (41 = 41) |
| 15 | `grep -c "int:Signed32" <bala>/types.bal` | 15 |
| 16 | `int:Signed32` in Types section, old / new | 0 / 15 |
| 17 | `grep -c '@display'` old / new | 0 / 1 |
| 18 | `grep -nE "^\s*@" <bala>/*.bal` | 1 hit: `types.bal:302 @display {label: "Connection Config"}` |
| 19 | JSON structure old / new | both: 41 typeDefs, 1 client, 0 functions, 0 services, 0 annotations |
| 20 | `diff -u old.pretty.json new.pretty.json \| wc -l` | 273; all changes = 15 Signed32 + 2 record-rest + 7 `Additional Values` removals + 1 annotation add |
| 21 | `diff old:7–202 new:7–202` (README) | identical |
| 22 | `grep -nE "\bpublic\b" <bala>/*.bal` (excl. `public type`) | `client.bal:23` class, `client.bal:31` init — nothing public in `utils.bal` |
| 23 | `grep -c ' = '` Types section, old / new | 0 / 0 (all record defaults dropped on both sides) |
| 24 | `grep -n "^and absent fields"` old / new | old:803, new:804 — same malformed doc continuation |
| 25 | `sed -n '/public type ConnectionConfig/,/|};/p' <bala>/types.bal` | `record {\|…\|}` closed, 11 fields with defaults — none reproduced in either render |
| 26 | `grep -n "public type Get.*Queries record"` etc. | 7 open `*Queries` records at types.bal 269, 372, 400, 410, 416, 500, 610 |
| 27 | `wc -l <bala>/docs/README.md` | 193 lines, fully reproduced in render lines 8–201 |
| 28 | `sed -n '931,1011p' new` read in full | all 19 resource signatures + init inspected against `client.bal` |

## 10. Caveats and unverified items

- The renders were not compiled. Statements about non-compiling constructs (§5.4, §5.6) are based on
  reading the emitted text against the Ballerina grammar, not on a `bal build` run.
- `Client.init`'s body-level behaviour (auth handling, `serviceUrl` normalisation) was not audited;
  only its signature was compared to `client.bal:31`.
- Doc-string text was compared for the changed regions and for `ConnectionConfig`; a full
  character-by-character comparison of all 41 types' doc comments against `types.bal` was not run.
  The JSON diff (evidence 20) shows no doc-string key changed between `old` and `new`, so this does
  not affect the regression verdict.
- Ballerina Central registry API was not re-queried; package metadata was read from the bala's
  `package.json`, which the brief designates as authoritative for what the extractor consumed.
- The `old` render's `Additional Values` parameter's exact provenance in the extractor (rest-field of
  the open `*Queries` records is the strong inference) was not confirmed by reading the extractor
  source; only its absence from the library source was verified.

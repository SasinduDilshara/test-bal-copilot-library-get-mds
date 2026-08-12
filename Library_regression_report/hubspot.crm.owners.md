# ballerinax/hubspot.crm.owners 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.owners` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.owners |
| Tag reviewed | `v2.0.2` (exact tag; `refs/tags/v2.0.2` -> `e405524`, peeled `f4c22a0`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.owners/2.0.2` |
| Old render | `362` lines |
| New render | `365` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small OpenAPI-generated connector: one default module (`hubspot.crm.owners`), 3 `.bal` files
(client/types/utils, 456 lines total), 10 public types, 1 client class with `init` + 2 resource
functions. No compiler plugin, no submodules.

`new` differs from `old` in exactly 5 hunks (8 lines added, 5 removed), all of them improvements:

1. 3 version-qualified type refs `ballerina/lang.int:0.0.0:Signed32` -> `int:Signed32`.
2. 3 `@display` annotations recovered (2 field-level `password` on `ApiKeysConfig`, 1 type-level
   `Connection Config` on `ConnectionConfig`) — previously dropped entirely.
3. 2 bogus `anydata Additional Values` pseudo-parameters removed from the two resource signatures.

Zero declarations added or removed. Zero `// Unknown type:` placeholders on either side. README
section byte-identical between the two sides. **No regressions found.**

A set of rendering inaccuracies exists in `new` — but every one of them is present verbatim in
`old` too, so none is a regression introduced by spec v2. They are recorded in §5.

## 2. Change inventory

Declaration counts are identical on both sides.

| Kind | old | new | delta |
|---|---|---|---|
| `type ... record` (top-level typedefs) | 10 | 10 | 0 |
| `client class` | 1 | 1 | 0 |
| client `init` | 1 | 1 | 0 |
| client resource functions | 2 | 2 | 0 |
| module-level functions | 0 | 0 | 0 |
| enums / constants / annotations / services / listeners | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| README block lines (incl. markers) | 183 | 183 | 0 |
| JSON `typeDefs` / `clients` / `functions` / `services` / `annotations` | 10/1/0/0/0 | 10/1/0/0/0 | 0 |
| JSON bytes | 34,895 | 34,817 | −78 |

All 10 typedef names present on both sides (verified individually):
`ForwardPaging`, `NextPage`, `GetCrmV3OwnersOwnerIdGetByIdQueries`, `PublicTeam`, `PublicOwner`,
`OAuth2RefreshTokenGrantConfig`, `CollectionResponsePublicOwnerForwardPaging`, `ApiKeysConfig`,
`GetCrmV3OwnersGetPageQueries`, `ConnectionConfig`.

### Modified (5 hunks, all in `new`'s favour)

| # | Location (new) | Change |
|---|---|---|
| 1 | `PublicOwner` L245, L249 | `ballerina/lang.int:0.0.0:Signed32` -> `int:Signed32` (fields `userIdIncludingInactive`, `userId`) |
| 2 | `ApiKeysConfig` L285, L288 | `+ @display {label: "", kind: "password"}` on `privateAppLegacy` and `privateApp` |
| 3 | `GetCrmV3OwnersGetPageQueries` L298 | `ballerina/lang.int:0.0.0:Signed32` -> `int:Signed32` (field `'limit`) |
| 4 | `ConnectionConfig` L307 | `+ @display {label: "Connection Config"}` (type-level) |
| 5 | `Client` L360, L364 | `anydata Additional Values, ` removed from both resource signatures |

Corresponding JSON deltas (the render deltas are fully explained by these — no unaccounted change):
3 × `"name": "ballerina/lang.int:0.0.0:Signed32"` -> `"int:Signed32"`; 3 × new `"annotations"`
arrays; 2 × removal of the `{"name":"Additional Values","description":"Capture key value pairs",
"type":{"name":"anydata"},"optional":true}` parameter object.

## 3. Correctness against library source

Upstream `v2.0.2` and the bala are **byte-identical** for all three `.bal` files
(`diff` returned no output for `client.bal`, `types.bal`, `utils.bal`), so GitHub-vs-bala conflict
does not arise here.

Everything `new` changes is confirmed correct against the source:

| `new` output | Source evidence | Verdict |
|---|---|---|
| `int:Signed32 userIdIncludingInactive?` | `types.bal:61` `int:Signed32 userIdIncludingInactive?;` | correct |
| `int:Signed32 userId?` | `types.bal:65` `int:Signed32 userId?;` | correct |
| `int:Signed32 'limit?` | `types.bal:110` `int:Signed32 'limit = 100;` (type correct; default lost — see §5.1) | type correct |
| `@display {label: "", kind: "password"}` on `privateAppLegacy` | `types.bal:98` — exact match | correct |
| `@display {label: "", kind: "password"}` on `privateApp` | `types.bal:101` — exact match | correct |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:118` — exact match | correct |
| removal of `anydata Additional Values` | no such parameter exists; `client.bal:49,67` take `*GetCrmV3Owners…Queries queries` only | correct removal |

The removed `Additional Values` pseudo-parameter was the renderer's representation of the implicit
`anydata...;` rest field of the two open query records (`types.bal:29`, `types.bal:106`). Its
rendered form (`anydata Additional Values` — an identifier containing a space) was non-compiling
Ballerina and invited an LLM to emit a parameter literally named `Additional Values`. Dropping it
loses the (weak) signal that those records are open; on balance this is a clear net improvement.

Also spot-checked and correct on both sides: `init(ConnectionConfig config, string serviceUrl =
"https://api.hubapi.com/crm/v3/owners") returns error?` vs `client.bal:33`; return types
`CollectionResponsePublicOwnerForwardPaging|error` (`client.bal:49`) and `PublicOwner|error`
(`client.bal:67`); path param `[int:Signed32 ownerId]` (`client.bal:67`); all `PublicOwner`,
`PublicTeam`, `NextPage`, `ForwardPaging`, `CollectionResponsePublicOwnerForwardPaging` field
names/types/optionality (`types.bal:23–93`) match the render exactly.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Full `diff -u old new` on the renders is 5 hunks; every one is inspected above and every one is
  an addition of correct information or removal of incorrect information. No line present in `old`
  carries information that is absent or degraded in `new`.
- Full `diff -u old new` on the JSONs shows only the 8 change sites listed in §2 — nothing else in
  the model changed.
- Declaration sets, section markers, README block, and doc comments are identical (183/183 README
  lines; type and function name sets identical).
- `// Unknown type:` count is 0 on both sides, so the spec-v2 type-def rewrite had nothing to
  degrade here.
- Nothing was truncated: `new` is 3 lines longer, accounted for by 3 added `@display` lines
  (5 added / 2 removed net across hunks 2 and 4 plus the 1-for-1 replacements).

## 5. Issues in `new` (independent of `old`)

All of the following are also present verbatim in `old` — they are shared pipeline limitations,
not spec-v2 regressions. Listed because they would mislead an LLM consuming this render.

1. **Field default values are dropped; defaulted fields are re-rendered as optional.** Source
   `types.bal` has `boolean archived = false` (L31, L108), `"id"|"userId" idProperty = "id"` (L33),
   `int:Signed32 'limit = 100` (L110), `string refreshUrl = "https://api.hubapi.com/oauth/v1/token"`
   (L76), and 11 defaulted fields in `ConnectionConfig` (L123–L158: `httpVersion = http:HTTP_2_0`,
   `timeout = 30`, `forwarded = "disable"`, `compression = http:COMPRESSION_AUTO`,
   `validation = true`, `laxDataBinding = true`, etc.). The render shows all of them as `?` with no
   default. `grep -nE '^\s+[A-Za-z].* = ' new` returns zero matches inside any `type` body.
2. **Closed records rendered as open.** `OAuth2RefreshTokenGrantConfig` (L73), `ApiKeysConfig`
   (L96) and `ConnectionConfig` (L119) are `record {| … |}` in source; the render emits `record {`
   for all three (`grep -c 'record {|' new` = 0).
3. **Resource path `.` is lost.** Source `client.bal:49` is `resource isolated function get .(…)`;
   the render emits `resource function get (…)` — the JSON carries `"paths": []`. This is not
   valid Ballerina and does not tell the caller the call is `client->/(...)`.
4. **Included-record parameter is both flattened and duplicated.** Source takes
   `*GetCrmV3OwnersGetPageQueries queries`. The render emits the record's fields as individual
   parameters *and* a trailing `GetCrmV3OwnersGetPageQueries queries` parameter, with no `*`. The
   resulting signature is non-compiling and lists `archived`/`limit` twice in effect.
5. **Two invented and one wrong parameter default.** JSON/render give `int:Signed32 limit = 0`
   (source default is `100`), `string after = ""` and `string email = ""` (source `types.bal:112,114`
   declare these as `string after?` / `string email?` with **no** default).
6. **`public` and `isolated` qualifiers dropped everywhere** — `public isolated client class Client`
   (`client.bal:25`) renders as `client class Client`; all `public type` render as `type`.
7. **Malformed doc continuation line.** `new` L345–346 (old L342–343): the two-line doc comment for
   `laxDataBinding` loses the `#` on its second line, so `and absent fields are handled as
   `nilable` types. Enabled by default` sits as bare text inside the record body.
8. **`oauth2:` / `http:` prefixed types with no import in the render header.** Header emits only
   `import ballerinax/hubspot.crm.owners;`; the qualified refs rely on the trailing
   `// Special Agent Note: … FROM ballerina/oauth2 package` comments to be resolvable.

## 6. Coverage gaps vs. the library

**None.** The bala exports exactly one module (`package.json` `"export": ["hubspot.crm.owners"]`,
`modules/` contains only `hubspot.crm.owners`), so the `getDefaultModule()`-only extraction loses
nothing here — there are no submodules.

Public symbols in the default module vs. the render:

| Public symbol | Source | In render |
|---|---|---|
| 10 `public type` records | `types.bal:23,29,37,47,73,80,88,96,106,119` | all 10 present |
| `public isolated client class Client` | `client.bal:25` | present |
| `public isolated function init` | `client.bal:33` | present |
| `resource … get .` | `client.bal:49` | present |
| `resource … get [ownerId]` | `client.bal:67` | present |

Everything in `utils.bal` (`SimpleBasicType`, `Encoding`, `EncodingStyle`, `getDeepObjectStyleRequest`,
`getFormStyleRequest`, `getSerializedArray`, `getSerializedRecordArray`, `getEncodedUri`,
`getPathForQueryParam` — `utils.bal:23,26,37,48,74,111,151,175,189`) is module-private and correctly
absent.

Note (not counted as a gap): the client's object fields `final http:Client clientEp` and
`final readonly & ApiKeysConfig? apiKeyConfig` (`client.bal:26–27`) are not marked `private`, so
they are technically object-public; neither render emits them. They are implementation detail and
should not be emitted.

## 7. Compiler plugin

The package has **no compiler plugin**. Verified two ways: `find` for any `*compiler*plugin*` path
in the `v2.0.2` clone returns nothing, and the bala contains no `compiler-plugin/` directory
(`find -maxdepth 2 -type d` yields only `docs`, `modules`, `modules/hubspot.crm.owners`).
Consequently there are no plugin-contributed code actions, validations, generated artifacts or
annotations that should surface in the render. Nothing missing on this axis.

## 8. Other considerations

- **Version integrity**: no drift. `Ballerina.toml` (upstream `v2.0.2`), `bala.json`/`package.json`
  and the manifest all say `2.0.2`. Not deprecated, stable major (`>= 1.0`).
- **Size**: 365 lines / ~19 KB rendered, of which the README block is 183 lines (50%). Token cost is
  negligible; nothing needs trimming.
- **Doc quality**: doc comments are complete and carried through faithfully on both sides; the
  README includes a full setup guide and a working quickstart. The one defect is the unprefixed
  doc continuation line noted in §5.7.
- **Build metadata**: `graalvmCompatible: true`, `ballerina_version 2201.12.2`, distribution
  `2201.12.0`. Auto-generated by the Ballerina OpenAPI tool (header of `client.bal`/`types.bal`).
- The library is a good regression *control*: because it has no `Error`/object/`Other` typedefs,
  spec v2's headline behaviour (replacing `// Unknown type:` with real definitions) is not
  exercised — what is exercised here is the type-ref de-qualification and the annotation capture,
  both of which behave correctly.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 362 / 365 |
| 2 | `grep -c '^// Unknown type:'` on both | 0 / 0 |
| 3 | `diff -u old new` (renders) | 5 hunks, +8 / −5, all listed in §2 |
| 4 | `diff -u old new` (JSONs) | 8 change sites only: 3 type-ref, 3 annotation, 2 param removals |
| 5 | `wc -c` on both JSONs | 34,895 / 34,817 |
| 6 | `python3` count of JSON `typeDefs/clients/functions/services/annotations` | 10/1/0/0/0 on both |
| 7 | `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2` — exact tag exists |
| 8 | `git clone --depth 1 --branch v2.0.2` | OK, `src/ballerina/{client,types,utils}.bal` |
| 9 | `diff src/ballerina/types.bal <bala>/modules/…/types.bal` | identical (`TYPES_IDENTICAL`) |
| 10 | same for `client.bal`, `utils.bal` | identical (`CLIENT_IDENTICAL`, `UTILS_IDENTICAL`) |
| 11 | `cat src/ballerina/Ballerina.toml` | `version = "2.0.2"` — pin confirmed |
| 12 | `cat <bala>/any/package.json` | `"version":"2.0.2"`, `"export":["hubspot.crm.owners"]` |
| 13 | `ls -R <bala>` | `modules/` contains only `hubspot.crm.owners` — no submodules |
| 14 | `find <bala> -maxdepth 2 -type d` | no `compiler-plugin/` |
| 15 | `find src -ipath '*compiler*plugin*'` | no matches |
| 16 | `grep -nE '^(public )?(type\|const\|enum\|class\|…)' bala types.bal utils.bal` | 10 public types; all `utils.bal` symbols module-private |
| 17 | per-type `grep -c "^type <T> record"` on both renders | 10/10 types present on each side |
| 18 | `grep -c 'record {|' new` | 0 (source has 3 closed records) |
| 19 | `grep -nE '^\s+[A-Za-z].* = ' new` | no field defaults inside any type body |
| 20 | `diff` of render README block (L8–188) vs `<bala>/docs/README.md` | identical apart from 1 trailing blank line |
| 21 | README block line count via `awk` between markers | 183 on both sides |
| 22 | `python3` dump of `clients[0].functions` params/defaults (new JSON) | `limit` default `0`, `after`/`email` default `""`, `paths: []` for first resource |
| 23 | `cat <bala>/any/bala.json`, `dependency-graph.json` | bala 3.0.0, WSO2; deps incl. `ballerina/auth`, `oauth2` chain |
| 24 | Read `<bala>/modules/hubspot.crm.owners/client.bal` (78 lines) in full | signatures cited in §3 |
| 25 | Read `<bala>/modules/hubspot.crm.owners/types.bal` (159 lines) in full | defaults/closedness cited in §5 |
| 26 | Read `new/*.bal.txt` (365 lines) in full | §5 items 3,4,6,7,8 located |
| 27 | `sed -n '255,300p'` and `'340,362p'` on `old` render | §5 items 1–8 confirmed present in `old` too |
| 28 | Cross-check against `OLD_AND_NEW_DIFFS/hubspot.crm.owners_diff.md` | its counts (362/365, +8/−5, 5 hunks, 3→0 qualified refs, 0 decls added/removed) all reproduce |

## 10. Caveats and unverified items

- The render is a syntax digest, not a compilation unit; the "non-compiling" observations in §5
  (items 3, 4, 7, 8) are judged against Ballerina grammar, not against an actual `bal build` run.
  No compiler was invoked on the render text.
- §5.1's claim that defaults are dropped is established by grep over the render plus reading the
  source; I did not inspect the Java extractor to confirm *where* the default is discarded.
- The client object fields `clientEp` / `apiKeyConfig` are described as "technically object-public"
  from Ballerina's default-visibility rule; I did not confirm against the published API docs
  (the bala ships only `docs/README.md` and `docs/icon.png`, no API-doc HTML/JSON).
- Ballerina Central registry metadata was not re-queried over the network; version, exports,
  keywords and deprecation status were taken from the bala's `package.json` / `bala.json` and the
  upstream `Ballerina.toml`, which agree with each other and with the pin.

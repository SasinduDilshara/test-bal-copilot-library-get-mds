# ballerinax/hubspot.marketing.transactional 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.transactional` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.transactional |
| Tag reviewed | `v1.0.2` (commit `ddb682d2becd48dc024b87c209b7994e284bd164`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.transactional/1.0.2` |
| Old render | `407` lines |
| New render | `408` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, fully auditable connector: one default module (`hubspot.marketing.transactional`), 13 public
types, one `public isolated client class Client` with `init` + 6 resource methods, no public
functions/services/annotations, no compiler plugin. Both renders cover exactly that surface — 13
typeDefs, 1 client, 7 client functions on each side, identical README (7791 chars, byte-identical to
`docs/README.md` in the bala).

The `old` → `new` delta is 4 hunks, +4/−3 lines, and all three distinct changes are corrections:

1. Two version-qualified type refs `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`.
2. `@display {label: "Connection Config"}` on `ConnectionConfig` is now emitted (it exists in the
   library source and was silently dropped by `old`).
3. A fabricated parameter `anydata Additional Values` was removed from
   `resource function get smtp\-tokens`. It corresponded to no real parameter and was
   syntactically invalid Ballerina (identifier containing a space).

No declaration was added or removed. Zero `// Unknown type:` placeholders on either side. Nothing
present and correct in `old` is missing or degraded in `new`.

## 2. Change inventory

Line counts (`wc -l`): old 407, new 408.

Structural JSON comparison (both JSONs parsed, keys compared):

| top-level key | old | new | equal? |
|---|---|---|---|
| `name` | — | — | same |
| `description` | — | — | same |
| `readme` | 176 lines | 176 lines | same |
| `typeDefs` | 13 | 13 | **DIFF** (2 type-name strings, 1 annotation added) |
| `clients` | 1 (7 functions) | 1 (7 functions) | **DIFF** (1 parameter removed) |
| `functions` | `[]` | `[]` | same |
| `services` | `[]` | `[]` | same |
| `annotations` | `[]` | `[]` | same |

Type-def name list is identical and in identical order on both sides:
`CollectionResponseSmtpApiTokenViewForwardPaging, ForwardPaging, NextPage, SmtpApiTokenView,
PublicSingleSendRequestEgg, PublicSingleSendEmail, EmailSendStatusView, EventIdView,
SmtpApiTokenRequestEgg, GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries,
OAuth2RefreshTokenGrantConfig, ApiKeysConfig, ConnectionConfig`.

Declarations by kind — **added 0, removed 0, modified 3**:

| kind | old | new | modified |
|---|---|---|---|
| record type | 13 | 13 | 3 (`PublicSingleSendRequestEgg`, `GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries`, `ConnectionConfig`) |
| client class | 1 | 1 | 0 |
| client method (`init` + resources) | 7 | 7 | 1 (`get smtp\-tokens`) |
| function / service / listener / enum / const / annotation decl | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` lines | 0 | 0 | — |
| version-qualified type refs | 2 | 0 | −2 |

The three modifications, verbatim:

- `PublicSingleSendRequestEgg.emailId`: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`
  (render line 239; JSON `typeDefs[…].fields[…].type.name`).
- `GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries.'limit`:
  `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (render line 304).
- `ConnectionConfig`: `+ @display {label: "Connection Config"}` (render line 337); in JSON a new
  `annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]` array.
- `Client.get smtp\-tokens`: parameter `{"name": "Additional Values", "description": "Capture key
  value pairs", "type": {"name": "anydata"}, "optional": true}` removed (old JSON
  `clients/0/functions/2/parameters/5`).

## 3. Correctness against library source

The bala's `modules/hubspot.marketing.transactional/{client.bal,types.bal,utils.bal}` are
byte-identical to `ballerina/` at tag `v1.0.2` (`diff -r --brief` reports only non-`.bal` extras on
the GitHub side: `Ballerina.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png`,
`tests`). So GitHub and the bala agree; every citation below holds for both.

Each `new`-side change verified against source:

| change in `new` | source evidence | verdict |
|---|---|---|
| `int:Signed32 emailId` | `types.bal:31` `public type PublicSingleSendRequestEgg record {` … field declared `int:Signed32 emailId;` | correct; `old`'s `ballerina/lang.int:0.0.0:Signed32` was a non-existent spelling |
| `int:Signed32 'limit?` | `types.bal:110-119`, line 112 `int:Signed32 'limit?;` | correct |
| `@display {label: "Connection Config"}` | `types.bal:150` `@display {label: "Connection Config"}` directly above `types.bal:151 public type ConnectionConfig record {\|` | correct; `old` dropped a real annotation |
| removal of `anydata Additional Values` | `client.bal:65` `resource isolated function get smtp\-tokens(map<string\|string[]> headers = {}, *GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries queries) returns CollectionResponseSmtpApiTokenViewForwardPaging\|error` — the function has exactly two parameters; there is no `Additional Values` parameter anywhere in the package | correct removal of an invented symbol |

Unchanged content spot-checked against source (all match):

- `init` signature — render line 383 `function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/marketing/v3/transactional") returns error?` vs `client.bal:31` (identical modulo the dropped `public isolated`, see §5).
- All 6 resource paths and return types — render lines 387/391/395/399/403/407 vs `client.bal:47, 65, 81, 99, 115, 130`. Paths, escaped hyphens, path params (`[string tokenId]`), payload params and return types all match.
- 13 type names and field lists vs `types.bal:23, 31, 44, 62, 78, 96, 104, 110, 122, 130, 137, 145, 151`.
- README block (render lines 7–184) equals `docs/README.md` exactly (string equality check, 7791
  chars both).

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full `diff -u old new` on the renders — only 4 hunks, all listed in §2; nothing is deleted except
  the fabricated `anydata Additional Values` parameter.
- Structural JSON diff (`json.load` + sorted-key unified diff, 1108 vs 1106 lines) — confirms the
  render diff is complete: no field, doc string, default value, or parameter beyond those 4 items
  differs.
- Declaration-set equality: identical type-def name list, identical client function count (7),
  identical section markers (4), identical README length.
- `grep -c '^// Unknown type:'` = 0 on both sides — no degraded types on either side, so no
  spec-v2 emission to compare and no chance of a lost placeholder.
- The one thing removed (`anydata Additional Values`) is not a regression: it exists in no source
  file, it is not valid Ballerina, and the information it purported to carry (that
  `GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries` is an open record accepting extra
  values) is still conveyed by the type def, which both renders emit as an open `record { … }`.

## 5. Issues in `new` (independent of `old`)

All six items below are present **identically in `old`**, i.e. they are pre-existing pipeline
behaviour, not introduced by spec v2. They are recorded because they misrepresent the library.

1. **Closed records rendered as open.** `types.bal:130 OAuth2RefreshTokenGrantConfig`,
   `types.bal:145 ApiKeysConfig` and `types.bal:151 ConnectionConfig` are all declared
   `record {| … |}` (closed). Render lines 315, 331, 338 emit `record { … };` — an LLM would
   conclude arbitrary extra fields are permitted, which will not compile.
2. **Field default values dropped and re-typed as optional.** `ConnectionConfig` in source has 11
   defaulted (therefore *required-with-default*, non-optional) fields:
   `httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`
   (`types.bal:153-190`). The render (lines 342-377) emits every one of them as `field?` with the
   default discarded. The genuinely optional ones (`followRedirects?`, `poolConfig?`,
   `circuitBreaker?`, `retryConfig?`, `cookieConfig?`, `secureSocket?`, `proxy?`) render the same
   way, so the two categories become indistinguishable.
3. **`get smtp\-tokens` signature is duplicated and non-compiling.** Source (`client.bal:65`) takes
   `*GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries queries` (an included record). The
   render (line 391) both flattens the record's fields into positional params *and* keeps a
   `queries` param:
   `resource function get smtp\-tokens(map<string|string[]> headers = {}, int:Signed32 limit = 0, string emailCampaignId = "", string after = "", string campaignName = "", GetMarketingV3TransactionalSmtpTokensGetTokensPageQueries queries) returns …`
   Three defects in that one line: (a) the fields appear twice; (b) the defaults `= 0` / `= ""` are
   invented — the source fields are `'limit?`, `emailCampaignId?`, `after?`, `campaignName?` with no
   defaults; (c) `limit` is spelled without the quoted-identifier escape, whereas source uses
   `'limit` (`limit` is not a reserved word in Ballerina so this is cosmetic, but it no longer
   matches the record field name); and (d) a defaultable parameter is followed by a
   non-defaultable one, which is invalid Ballerina.
4. **Qualifiers dropped.** `public isolated client class Client` (`client.bal:23`) renders as
   `client class Client`; `public isolated function init` (`client.bal:31`) renders as
   `function init`; all `resource isolated function` render as `resource function`. Isolation is
   part of this connector's contract (it is `graalvmCompatible: true`, `isolated` throughout).
5. **Parameter and return docs dropped.** Source has full doc blocks, e.g. `client.bal:44-46`
   `# + headers - Headers to be sent with the request` / `# + return - successful operation`. The
   render keeps only the summary line and leaves a bare `# ` behind it (render lines 386, 390, 394,
   398, 402, 406 — 6 empty doc continuation lines).
6. **Multi-line doc comments lose their `#` prefix, producing non-compiling text.** Render line 236
   (`Note: Custom properties do not currently support arrays…`) and line 376
   (`and absent fields are handled as \`nilable\` types. Enabled by default`) sit inside record
   bodies as bare prose with no `#`. Verified present at old:236/old:375 and new:236/new:376 — an
   exact carry-over, not new.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala's `package.json` exports exactly one module (`"export":
["hubspot.marketing.transactional"]`), which is the default module, so there is no
submodule-only API and the known `getDefaultModule()` limitation does not bite here.

Exhaustive public-symbol enumeration of the default module
(`grep -nE '^public (type|const|class|enum|function|isolated function)|^ *public' modules/hubspot.marketing.transactional/*.bal`):

- 13 `public type` declarations — all 13 present in both renders.
- 1 `public isolated client class Client` (`client.bal:23`) — present.
- 1 `public isolated function init` (`client.bal:31`) — present.
- `utils.bal` contains **no** `public` declarations (grep returns nothing); its helpers
  (`getEncodedUri`, query/header serialisation, etc.) are module-private, so their absence from the
  render is correct.
- No public constants, enums, listeners, services, annotations, or module-level functions exist —
  consistent with the empty `functions`, `services`, `annotations` arrays in both JSONs.

## 7. Compiler plugin

The package ships **no compiler plugin**. Evidence:

- The bala contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` —
  there is no `compiler-plugin/` directory and no `compiler-plugin.json`.
- `find` over the cloned `v1.0.2` tree for `*compiler-plugin*` / `*plugin*` returns nothing.
- `ballerina/Ballerina.toml` has no `[[platform.java*.dependency]]` or `[compiler-plugin]` section.

Consequently there are no plugin-contributed code actions, validations, generated artifacts, or
annotations that ought to appear in the render. Nothing is missing on this axis.

## 8. Other considerations

- **Version/stability.** 1.0.2 is a stable release; `Ballerina.toml` targets distribution
  `2201.12.0`, the bala was built with `2201.12.2`, `graalvmCompatible: true`. Nothing deprecated in
  the source (no `@deprecated`).
- **Generated code.** `client.bal:1-2` marks the package as `AUTO-GENERATED … by the Ballerina
  OpenAPI tool`, which explains the `*Queries` included-record pattern that the renderer mishandles
  (§5.3). Any regression review of sibling `hubspot.*` connectors will hit the same shape.
- **Size / tokens.** 408 lines, of which 178 (44%) are the README block. Cost is negligible; the
  +1 net line from spec v2 is immaterial.
- **Auth surface.** Three auth modes (`http:BearerTokenConfig | OAuth2RefreshTokenGrantConfig |
  ApiKeysConfig`) are all rendered, and the `// Special Agent Note: … FROM ballerina/http package`
  cross-package annotations are intact and identical on both sides.
- **Net effect for an LLM consumer.** `new` strictly reduces the chance of a hallucinated symbol:
  it removes an invented parameter, removes two type names that do not exist in the language
  (`ballerina/lang.int:0.0.0:Signed32`), and adds a real annotation. No offsetting loss.

## 9. Evidence log

| # | Check (command / file:line) | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 407 / 408 |
| 2 | `diff -u old/…bal.txt new/…bal.txt` | 4 hunks, +4/−3 lines (reproduced in full in §2) |
| 3 | `grep -c '^// Unknown type:'` on both renders | 0 / 0 |
| 4 | `grep -n '^// --- ' new/…bal.txt` | 4 markers: README(7), END README(184), Types(186), Client(380); same set in old |
| 5 | `grep -n "Additional Values"` across both renders and both JSONs | old render:390, old JSON:907; **0 hits in new** |
| 6 | python structural diff of the two JSONs (sorted keys, `difflib.unified_diff`) | 1108→1106 lines; exactly 4 changes: param removed, 2 type-name strings, 1 annotation added |
| 7 | python key-by-key JSON comparison | `typeDefs` DIFF, `clients` DIFF; `name`,`description`,`readme`,`functions`,`services`,`annotations` all same |
| 8 | python: typeDef count / names, client count, client fn count, readme lines — both sides | 13 / identical ordered name list, 1, 7, 176 — all equal |
| 9 | `ls -R` of the bala | `any/{bala.json,dependency-graph.json,docs/{README.md,icon.png},modules/hubspot.marketing.transactional/{client.bal,types.bal,utils.bal},package.json}`; no compiler-plugin |
| 10 | `wc -l` bala module sources | client.bal 139, types.bal 191, utils.bal 219 |
| 11 | `git ls-remote --tags <repo>` | tags v0.1.0, v1.0.0, v1.0.1, **v1.0.2** (`ddb682d2becd48dc024b87c209b7994e284bd164`) |
| 12 | `git clone --depth 1 --branch v1.0.2 …` then `diff -r --brief bala/modules/… src/ballerina` | all three `.bal` files identical; only non-source extras differ |
| 13 | `grep -nE '^public (type\|const\|class\|enum\|isolated function\|function)' bala/modules/**/*.bal` | 13 `public type` (types.bal:23,31,44,62,78,96,104,110,122,130,137,145,151) |
| 14 | `grep -n "^public\|^    public"` filtered to non-type decls | `client.bal:23 public isolated client class Client`, `client.bal:31 public isolated function init` — nothing else |
| 15 | `grep -n "public" bala/…/utils.bal` | no matches → no public symbols in utils.bal |
| 16 | `grep -n 'smtp\\-tokens' bala/…/client.bal` | 5 resource fns at :65, :81, :99, :115, :130 (+ `single-email/send` at :47) = 6, matches render |
| 17 | `sed -n '110,119p' types.bal` | `'limit?`, `emailCampaignId?`, `after?`, `campaignName?` — all optional, **no defaults** (contradicts render's `= 0` / `= ""`) |
| 18 | `sed -n '140,191p' types.bal` | `ApiKeysConfig record {\|…\|}`, `@display {label: "Connection Config"}` at :150, `ConnectionConfig record {\|…\|}` with 11 defaulted fields |
| 19 | python: `old_json.readme.strip() == bala/docs/README.md.strip()` | `True` (7791 == 7791 chars) |
| 20 | `awk` for unprefixed doc continuation lines after the Types marker | old:236 & old:375; new:236 & new:376 — same two, carried over |
| 21 | `find src -iname '*compiler-plugin*' -o -iname '*plugin*'` | no matches |
| 22 | `cat src/ballerina/Ballerina.toml` | org/name/version = `ballerinax`/`hubspot.marketing.transactional`/**1.0.2**, distribution 2201.12.0, no plugin section |
| 23 | `cat bala/any/package.json` | version 1.0.2, `"export": ["hubspot.marketing.transactional"]` (single module), graalvmCompatible true |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that particular render lines are "non-compiling Ballerina"
  (§5.1–§5.3, §5.6) are read from the language rules, not from a `bal build` run — the render is a
  documentation artifact and is not expected to compile, so this is stated as a fidelity concern,
  not a build failure.
- Ballerina Central metadata was not re-queried over the network; package identity, version, export
  list and keywords were taken from the bala's `package.json` and the tag's `Ballerina.toml`, which
  agree with each other and with the pinned version.
- The `old`/`new` extractor commits themselves (`eb5d81b3` / `412ba01e`) were not inspected; the
  attribution of each delta to spec v2 rests on the brief plus the observed shape of the changes
  (removal of version-qualified refs and emission of annotations are both documented spec-v2
  behaviours).
- `PIN_OK` at 1.0.2 for both sides was taken from the brief and corroborated only indirectly: the
  two JSONs describe an identical declaration set, and that set matches the 1.0.2 bala exactly.

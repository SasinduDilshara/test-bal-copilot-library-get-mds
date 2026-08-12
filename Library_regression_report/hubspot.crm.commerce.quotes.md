# ballerinax/hubspot.crm.commerce.quotes 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.commerce.quotes` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.commerce.quotes |
| Tag reviewed | `v2.0.2` (commit `25e0d0f33c7bb070f13eb197d62fcc0c5d9e6f28`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.commerce.quotes/2.0.2` |
| Old render | `792` lines |
| New render | `793` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The change is small, fully enumerated, and entirely positive. `new` differs from `old` in exactly
three ways: (a) 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
`ballerinax/hubspot.crm.commerce.quotes:2.0.2:ValueWithTimestamp`) are normalised to the real
Ballerina spellings (`int:Signed32`, `ValueWithTimestamp`); (b) the `@display {label: "Connection
Config"}` annotation on `ConnectionConfig` is now emitted, matching the library source; (c) four
bogus `anydata Additional Values` parameters — syntactically invalid Ballerina (identifier contains
a space) — are dropped from the four client resource functions that take an included-record
`*…Queries` parameter.

No declaration is added or removed. All 41 public types and all 12 client functions (`init` + 11
resource functions) are present on both sides and match the published source. The README section is
byte-identical to the bala README on both sides. Zero `// Unknown type:` placeholders on either side.
No regression found.

## 2. Change inventory

Line counts: old 792, new 793 (`wc -l`). Unified diff: 15 hunks, 16 added lines, 15 removed lines.

Declarations by kind — identical sets on both sides:

| Kind | old | new | delta |
|---|---|---|---|
| `type` definitions | 41 | 41 | 0 |
| client classes | 1 | 1 | 0 |
| client `init` | 1 | 1 | 0 |
| client resource functions | 11 | 11 | 0 |
| module-level functions / services / annotations (JSON `functions`,`services`,`annotations`) | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |

`diff` of the sorted type-name sets extracted from both renders: **identical** (no additions, no
removals). The complete structural delta, taken from a full recursive diff of the two JSONs:

| # | Change | Count | JSON path |
|---|---|---|---|
| 1 | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` | 8 | `typeDefs[8,10,13,18,26,31,32]/fields[*]/type/name` |
| 2 | `record {\|ballerinax/hubspot.crm.commerce.quotes:2.0.2:ValueWithTimestamp[]...;\|}` → `record {\|ValueWithTimestamp[]...;\|}` | 3 | `typeDefs[12,19,36]` |
| 3 | `record {\|…:2.0.2:CollectionResponseAssociatedId...;\|}` → `record {\|CollectionResponseAssociatedId...;\|}` | 1 | `typeDefs[36]/fields[0]` |
| 4 | `annotations: [{name: display, value: {label: "Connection Config"}}]` **added** | 1 | `typeDefs[27]` (`ConnectionConfig`) |
| 5 | parameter `{"name":"Additional Values","type":{"name":"anydata"},"optional":true,"description":"Capture key value pairs"}` **removed** | 4 | `clients[0]/functions[1,2,4,8]/parameters` |

Total qualified type refs: old 11, new 0 (`grep -c 'ballerina/lang.int:0.0.0:\|ballerinax/hubspot.crm.commerce.quotes:2.0.2:'`).

Affected resource functions for change 5: `post batch/read`, `get [string quoteId]`,
`patch [string quoteId]`, `get .` — exactly the four functions whose source signature uses an
included record parameter (`*…Queries queries`, client.bal:47, 68, 103, 177).

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala
`modules/hubspot.crm.commerce.quotes/{client,types,utils}.bal` (`diff -q`, three files, no output),
so GitHub and the bala agree and there is nothing to reconcile.

Verification of each change in `new`:

- `int:Signed32` — source declares `int:Signed32` at types.bal:67, 127, 179, 208, 308, 336, 386
  (7 declaration sites; 8 render occurrences because the same field type appears in the flattened
  `PublicObjectSearchRequest`/query records). `new` matches the source spelling exactly; `old`'s
  `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina and does not appear anywhere in source.
- `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}` — source
  uses unqualified same-module names (types.bal `SimplePublicObject`, `SimplePublicUpsertObject`,
  `SimplePublicObjectWithAssociations` at :216, :444, :390). `new` matches; `old` self-qualified
  with `ballerinax/hubspot.crm.commerce.quotes:2.0.2:` which is not valid Ballerina.
- `@display {label: "Connection Config"}` — present in source at types.bal:234, directly above
  `public type ConnectionConfig record {|`. `new` (render line 551) reproduces it verbatim. It is
  the only `@display` annotation in the package (`grep -n '@display' types.bal` → single hit at 234),
  and `new` emits exactly one (`grep -n '@display'` on the render → line 551 only). No invented
  annotations.
- Removal of `anydata Additional Values` — the four `*…Queries` records are open records
  (`public type PostCrmV3ObjectsQuotesBatchReadReadQueries record {` at types.bal:290, likewise
  :59, :284, :360; note `record {`, not `record {|`), so their implicit rest field is
  `anydata...`. `old` surfaced that rest field as a positional parameter literally named
  `Additional Values`, which cannot compile. The openness is still conveyed in `new` because the
  corresponding type definitions are rendered as `record { … }` (open) — e.g. render line 319
  `type GetCrmV3ObjectsQuotesGetPageQueries record {`. Nothing verifiable was lost.

Spot checks that both renders get right (unchanged by the diff, confirmed against source):
`init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v3/objects/quotes")
returns error?` matches client.bal:32; all 11 resource paths/verbs and return unions match
client.bal:47,68,86,103,122,140,158,177,194,212,230.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full recursive JSON diff of `old` vs `new` (every key, every list element). The complete set of
  differences is the five rows in §2 — there is no other change of any kind.
- Sorted declaration-name sets from both renders: identical (`diff` → no output).
- Section markers: 4 on both sides, same names.
- README region (lines 8–206) of `old` vs `new`: identical (`diff` → no output), and identical to
  the bala `docs/README.md` (198 lines; the render carries one extra trailing blank line).
- `// Unknown type:` count: 0 → 0.
- Invented-default strings in the client section (`associations = []`, `idProperty = ""`,
  `limit = 0`, `properties = []`, `propertiesWithHistory = []`, `archived = false`): identical
  counts 2/2/1/2/2/3 on both sides — nothing gained or lost.
- Closed-record markers `record {|` in the renders: 19 on both sides.
- No parameter, default, return type, or doc comment is dropped in `new` other than the invalid
  `anydata Additional Values` pseudo-parameter, which was not real API.

## 5. Issues in `new` (independent of `old`)

All six items below are present identically in `old`; they are pre-existing extractor behaviour, not
introduced by spec v2. Listed because they mislead an LLM consuming the render.

1. **Invented defaults on flattened query parameters.** Client signatures render optional query
   fields as if they had defaults: `string[] associations = []`, `string idProperty = ""`,
   `string[] properties = []`, `string[] propertiesWithHistory = []` (render lines 755, 764, 782).
   In the source these fields are optional with *no* default (`string[] associations?`,
   `string idProperty?` — types.bal:361, 367, 285, 60); absent ≠ empty for HubSpot query semantics.
2. **Wrong default value.** `resource function get (... int:Signed32 limit = 0 ...)` (render line 782)
   contradicts the source default `int:Signed32 'limit = 10` (types.bal:67).
3. **Record-field defaults dropped in type definitions.** `GetCrmV3ObjectsQuotesGetPageQueries`
   renders `boolean archived?` and `int:Signed32 'limit?` (render lines 323, 327) where the source
   has `boolean archived = false` and `int:Signed32 'limit = 10` (types.bal:63, 67). Same pattern in
   `ConnectionConfig`: `httpVersion?`, `timeout?`, `forwarded?` (render lines 555, 560, 562) vs
   source `httpVersion = http:HTTP_2_0`, `timeout = 30`, `forwarded = "disable"` (types.bal:239–245).
4. **Lost HubSpot-specific default in `OAuth2RefreshTokenGrantConfig`.** Render line 506 is
   `string refreshUrl?`; source (types.bal:193–197) is a closed record including
   `*http:OAuth2RefreshTokenGrantConfig` with `string refreshUrl = "https://api.hubapi.com/oauth/v1/token"`.
   The connector-specific token URL — the one value a user cannot guess — is gone.
5. **Included-record parameters double-rendered and non-compiling.** For the four `*…Queries`
   functions the render emits both the flattened fields *and* a required `…Queries queries`
   parameter after defaulted parameters, e.g. render line 755:
   `resource function get [string quoteId](map<string|string[]> headers = {}, string[] associations = [], …, GetCrmV3ObjectsQuotesQuoteIdGetByIdQueries queries)`.
   A required parameter cannot follow defaulted ones, so the signature is not valid Ballerina, and it
   suggests two mutually exclusive call styles. `new` is strictly better than `old` here (one fewer
   invalid parameter) but the shape is still wrong.
6. **Closed records rendered as open, modifiers dropped.** Source has 21 `record {|` occurrences;
   the renders show 19, and `ConnectionConfig` (types.bal:235), `ApiKeysConfig` (:492) and
   `OAuth2RefreshTokenGrantConfig` (:193) are all rendered as open `record {`. `public` on types and
   `public isolated client class` on `Client` are likewise reduced to `type …` / `client class Client`.
   Presumably a deliberate rendering convention, but it does misstate the record's closedness.

## 6. Coverage gaps vs. the library

**None.**

- The bala exports a single module: `package.json` `"export": ["hubspot.crm.commerce.quotes"]`, and
  `modules/` contains only `hubspot.crm.commerce.quotes`. Central metadata confirms one module. So
  the `getDefaultModule()`-only extraction loses nothing here.
- `grep '^public type'` on the bala `types.bal` yields 41 names; the render's type set is the same
  41 names — `comm -23` (in bala, not in render) and `comm -13` (in render, not in bala) both empty.
- `client.bal` declares `init` + 11 resource functions; the render's client carries 12 functions
  (JSON `clients[0].functions` length 12) with matching names.
- Non-public helpers in `utils.bal` (`SimpleBasicType`, `Encoding`, `EncodingStyle`, etc.) are not
  exported and correctly absent.

## 7. Compiler plugin

The repository at `v2.0.2` contains no compiler plugin: `find . -iname "*compiler-plugin*"` over the
clone returns nothing, the bala has no `compiler-plugin/` directory (bala root contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`), and `Ballerina.toml` has
no `[[plugin]]` section. Nothing plugin-derived is expected in the render, and nothing is missing.

## 8. Other considerations

- Not deprecated: Central `deprecated: null`, `deprecateMessage: ""`. Stable major version 2.0.2.
  Built with Ballerina `2201.12.2`; `Ballerina.toml` distribution `2201.12.0`. `graalvmCompatible: true`.
- Low adoption (`pullCount: 31`), published recently; render quality matters more than churn risk.
- Size is modest (793 lines), 199 of which (25%) are the verbatim README. Removing 4 invalid
  parameters and 11 long qualified type names makes `new` marginally cheaper in tokens despite the
  one extra line.
- The render remains non-compiling Ballerina in the client section for the reason in §5.5, so it
  should be treated as documentation, not as source.
- The `# ` doc line above each resource function is followed by an empty `# ` continuation line on
  both sides (e.g. render lines 749–750); parameter-level docs (`+ headers - …`) from the source are
  not carried into the client render on either side.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 792 / 793 |
| `grep -c '^// Unknown type:'` old, new | 0, 0 |
| `diff -u old new \| grep -c '^+[^+]' / '^-[^-]' / '^@@'` | 16 added, 15 removed, 15 hunks |
| `grep -c 'ballerina/lang.int:0.0.0:\|ballerinax/hubspot.crm.commerce.quotes:2.0.2:'` old, new | 11, 0 |
| `grep -n '^// --- ' old` / `new` | 4 markers each (README/END README/Types/Client) |
| Recursive JSON diff old vs new (python) | Exactly 12 `CHG`/`ADD` + 4 parameter removals; listed in §2 |
| `grep -oE '^(public )?type [A-Za-z0-9_]+'` on both renders, sorted, `diff` | identical, 41 names |
| `grep -oE '^public type [A-Za-z0-9_]+' bala/types.bal` sorted vs render set (`comm -23`, `comm -13`) | both empty → no coverage gap |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, v2.0.2; exact match `v2.0.2` → `25e0d0f3` |
| `git clone --depth 1 --branch v2.0.2` then `diff -q ballerina/{client,types,utils}.bal` vs bala modules | identical, all three |
| `grep -n 'Signed32\|@display' bala/types.bal` | Signed32 at 67,127,179,208,308,336,386; `@display` only at 234 |
| `grep -n '@display' new/*.bal.txt` | single hit, line 551 |
| `grep -nE 'resource isolated function' bala/client.bal` | 11 functions at 47,68,86,103,122,140,158,177,194,212,230 |
| `bala/client.bal:32` | `public isolated function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v3/objects/quotes") returns error?` |
| `python3` JSON: `clients[0].functions` length | 12 (init + 11) |
| `python3` JSON: `functions`, `services`, `annotations` lengths | 0, 0, 0 (both sides) |
| README region `sed -n '8,206p' new` vs bala `docs/README.md` | identical except one trailing blank line (199 vs 198) |
| README region old vs new | identical |
| `grep -c 'record {|'` old, new; `grep -c 'record {|' bala/types.bal` | 19, 19; source 21 |
| `grep -oE 'associations = \[\]\|idProperty = ""\|limit = 0\|properties = \[\]\|propertiesWithHistory = \[\]\|archived = false'` old vs new | identical counts 2/2/1/2/2/3 |
| `bala/types.bal:59-73` (`GetCrmV3ObjectsQuotesGetPageQueries`) | `archived = false`, `'limit = 10`, others optional with no default |
| `bala/types.bal:193-197` (`OAuth2RefreshTokenGrantConfig`) | closed record, `refreshUrl = "https://api.hubapi.com/oauth/v1/token"` |
| `bala/package.json` `export` + `ls bala/modules` | single module `hubspot.crm.commerce.quotes` |
| `find . -iname "*compiler-plugin*"` in clone; `cat ballerina/Ballerina.toml` | no plugin, no `[[plugin]]` |
| Central API `/2.0/registry/packages/ballerinax/hubspot.crm.commerce.quotes/2.0.2` | `deprecated: null`, 1 module, ballerinaVersion 2201.12.2, pullCount 31 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that a rendered signature is "not valid Ballerina" (§5.5,
  and the `anydata Additional Values` parameter in `old`) are based on reading the grammar rules
  (identifier with a space; required parameter after defaulted parameters), not on a compiler run.
- The two-stage pipeline was not re-run; the review takes the supplied `old`/`new` JSON and
  `.bal.txt` artefacts as faithful outputs of the two `ballerina-vscode` revisions named in the brief.
- The brief's statement that both sides were pinned at 2.0.2 is consistent with the evidence
  (`old` embeds the literal string `ballerinax/hubspot.crm.commerce.quotes:2.0.2:` in 4 type refs,
  and both renders describe the same 41 types / 12 client functions as the 2.0.2 bala), but the
  version stamp is not independently recoverable from `new`, which no longer emits qualified refs.
- Ballerina Central's per-version module listing returns empty `summary`/`readme` strings; module
  count was therefore cross-checked against the bala rather than trusted from Central alone.

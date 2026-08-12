# ballerinax/hubspot.marketing.subscriptions 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.subscriptions` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.subscriptions |
| Tag reviewed | `v2.0.2` (annotated, `572edd1f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.subscriptions/2.0.2` |
| Old render | `761` lines |
| New render | `762` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. `new` differs from `old` in exactly three ways, all verified against
the published source:

1. 12 version-qualified type refs `ballerina/lang.int:0.0.0:Signed32` become the correct
   `int:Signed32` (matches the 12 occurrences in the bala's `types.bal`).
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — present in the
   library source, dropped by `old` — is now emitted.
3. A synthetic, syntactically invalid parameter `anydata Additional Values` is removed from 7 remote
   function signatures. It had no counterpart in the library source; it was the extractor's
   rendering of the open-record rest descriptor and it made those 7 signatures non-parseable.

Declaration sets are otherwise byte-identical: same 32 type defs, same 1 client, same 10 client
functions, same README, same section markers. No declaration was added or removed. No regression
found. Several accuracy problems exist in the render, but every one of them is present identically
in `old` and `new` and is therefore not caused by spec v2 (section 5).

## 2. Change inventory

Counts from `diff -u old new` and direct greps on both files and both JSONs.

| Metric | old | new |
|---|---|---|
| Lines | 761 | 762 |
| Section markers `// --- ` | 4 | 4 |
| `// Unknown type:` placeholders | 0 | 0 |
| Version-qualified refs `org/mod:x.y.z:Type` | 12 | 0 |
| `@display` annotations rendered | 0 | 1 |
| `anydata Additional Values` params | 7 | 0 |
| `remote function` declarations | 9 | 9 |
| `type X record` declarations | 32 | 32 |
| `client class` declarations | 1 | 1 |
| JSON `typeDefs` / `clients` / `functions` / `services` / `annotations` | 32 / 1 / 0 / 0 / 0 | 32 / 1 / 0 / 0 / 0 |
| JSON client functions | 10 (`init` + 9 remote) | 10 |

Declarations added: **0**. Declarations removed: **0**. Type-name sets are identical
(`diff old_types.txt new_types.txt` → no output).

Modified declarations, by kind:

| Kind | Count modified | Nature of change |
|---|---|---|
| Record type defs | 12 (11 for the type ref, `ConnectionConfig` for the annotation) | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (12 field occurrences across 11 records: `ActionResponseWithResultsPublicStatus`, `ActionResponseWithResultsPublicWideStatus`, `ActionResponseWithResultsSubscriptionDefinition`, `BatchResponsePublicBulkOptOutFromAllResponse`, `BatchResponsePublicStatus`, `BatchResponsePublicStatusBulkResponseWithErrors`, `BatchResponsePublicWideStatusBulkResponseWithErrors`, `PublicStatus`, `PublicStatusRequest`, `PublicSubscriptionTranslation` ×3); `ConnectionConfig` gains `@display {label: "Connection Config"}` |
| Client remote functions | 7 | dropped the synthetic `anydata Additional Values` parameter |
| Client `init` | 0 | unchanged |
| Enums / constants / annotations / services / listeners / module-level functions | 0 | none exist in this library on either side |
| README block | 0 | identical (JSON `readme` field compares equal) |

The 7 affected functions: `getCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll`,
`postCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll`,
`postCommunicationPreferencesV4StatusesBatchRead`,
`postCommunicationPreferencesV4StatusesBatchUnsubscribeAll`,
`getCommunicationPreferencesV4Definitions`,
`postCommunicationPreferencesV4StatusesBatchUnsubscribeAllRead`,
`getCommunicationPreferencesV4StatusesSubscriberIdString`.
A structural JSON diff of all 10 client functions shows the removed object is exactly
`{"name":"Additional Values","description":"Capture key value pairs","optional":true,"type":{"name":"anydata"}}`
and nothing else changed in any function (no parameter, default, doc or return type touched).

## 3. Correctness against library source

The bala's module sources are byte-identical to upstream tag `v2.0.2`
(`diff -q src/ballerina/{client,types,utils}.bal <bala>/modules/.../` → identical for all three;
README.md also identical). So GitHub and the bala agree; no arbitration needed.

- **`int:Signed32`** — `grep -c "int:Signed32" <bala>/modules/.../types.bal` → **12**, at lines
  27, 83, 99, 165, 210, 280, 286, 290, 320, 346, 364, 449. The new render carries exactly 12
  `int:Signed32` and zero qualified forms. `new` matches the source verbatim; `old` did not.
- **`@display`** — `types.bal:226` is `@display {label: "Connection Config"}` immediately above
  `types.bal:227 public type ConnectionConfig record {|`. It is the only annotation in the whole
  module (`grep -n "@display" types.bal` returns line 226 only). `new` renders it; `old` omitted it.
  The new JSON adds `"annotations":[{"name":"display","value":"{label: \"Connection Config\"}"}]`
  to the `ConnectionConfig` typeDef.
- **`Additional Values`** — no such parameter exists in `client.bal`. The real signatures
  (`client.bal:66, 83, 101, 121, 140, 157, 177`) use an included-record parameter, e.g.
  `remote isolated function getCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAll(string subscriberIdString, map<string|string[]> headers = {}, *GetCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries)`.
  Removing the invented parameter moves the render closer to the source, not further from it. The
  openness of the `*Queries` records is still conveyed — the Queries type defs are rendered as open
  `record { ... }` (e.g. new render line 727 `type GetCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries record {`),
  matching `types.bal:471`.
- **Client shape** — `client.bal:23 public isolated client class Client` and
  `client.bal:31 public isolated function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/communication-preferences/v4") returns error?`.
  Both renders emit `client class Client` with
  `function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/communication-preferences/v4") returns error?` — parameter names, types, default URL and return type all correct.
- **Function inventory** — source declares 9 `remote isolated function` in `client.bal`; both
  renders emit 9, with matching names, payload/headers parameters and return unions (spot-checked
  `postCommunicationPreferencesV4StatusesBatchWrite`, `client.bal:47`, and
  `postCommunicationPreferencesV4StatusesSubscriberIdString`, `client.bal:194` — both exact).

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full `diff -u old new` reviewed line by line — 12 hunks, all three change classes above, nothing else.
- Declaration name sets extracted and compared: 32 type names identical; 10 JSON client function
  names identical; 0 added, 0 removed.
- Per-function structural JSON diff over all 10 client functions: the only deletions are the 7
  `Additional Values` parameter objects. No parameter, default value, optionality flag, description
  or return type was lost.
- Per-typeDef structural JSON diff over all 32 type defs: only the 12 `Signed32` name changes and
  the `ConnectionConfig` annotation addition. No field, doc comment or optionality marker lost.
- README: `old['readme'] == new['readme']` → `True`; `description` also equal; both renders'
  README blocks (lines 8–201) reproduce `docs/README.md` in full, including the final Examples
  bullet.
- Syntax: the removal makes `new` strictly better formed — `anydata Additional Values` contains a
  space in the identifier and is not parseable Ballerina. `new` has 0 such lines.

## 5. Issues in `new` (independent of `old`)

All six below are present **identically in `old` and `new`** (verified: none appears in the diff),
so they are pre-existing extractor/renderer behaviour, not spec-v2 regressions. They still matter
because they misinform an LLM reading the `new` render.

1. **`ConnectionConfig` defaults are dropped and the record is shown as open.** Source
   `types.bal:227-265` is a closed `record {| ... |}` with concrete defaults:
   `httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`.
   Both renders emit `type ConnectionConfig record {` (open) with every one of those fields as a
   plain optional `foo?;` and no default. 11 default values lost.
2. **`OAuth2RefreshTokenGrantConfig` loses the HubSpot-specific `refreshUrl` default.** Source
   `types.bal:189-193` is `record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl = "https://api.hubapi.com/oauth/v1/token"; |}`.
   Render (new, line 439) shows `string refreshUrl?;` — the token endpoint, the single most useful
   fact in that record, is gone; and the closed record is shown as open.
3. **`ApiKeysConfig` closed record shown as open.** Source `types.bal` is `record {| string privateAppLegacy; string privateApp; |}`;
   render emits `type ApiKeysConfig record {`.
4. **Invented parameter defaults on flattened query parameters.** For the 7 functions with a
   `*Queries` parameter, both renders emit `"EMAIL"|"WHATSAPP"|"SMS" channel = "EMAIL"` and
   `int businessUnitId = 0`. In `types.bal` (e.g. lines 471-479) `channel` is **required with no
   default** and `businessUnitId` is **optional with no default**. Only `verbose = false` is real.
   The JSON carries these as `"default": "\"EMAIL\""` / `"default": "0"` on both sides, so the
   fabrication originates upstream of the renderer.
5. **Query parameters are emitted twice and in invalid order.** Each of those 7 signatures lists the
   flattened fields *and* a trailing `<Name>Queries queries` parameter, e.g.
   `..., boolean verbose = false, GetCommunicationPreferencesV4StatusesSubscriberIdStringUnsubscribeAllQueries queries)`.
   A parameter with no default following defaulted parameters is not valid Ballerina, and the
   duplication invites an LLM to pass the same query twice.
6. **Broken doc comment continuation.** In the `ConnectionConfig` block both renders emit
   `and absent fields are handled as nilable types. Enabled by default` on its own line without the
   leading `#`, so the second line of `laxDataBinding`'s doc is loose text inside a record body
   (new render, line 534).

Additionally, and harmlessly: `public` / `isolated` qualifiers are dropped everywhere
(`public isolated client class Client` → `client class Client`), and per-parameter doc lines
(`+ payload - ...`) are not rendered — both identical on the two sides.

## 6. Coverage gaps vs. the library

**Zero gaps.**

- The bala ships a single module, `modules/hubspot.marketing.subscriptions` — the default module.
  `package.json` `"export": ["hubspot.marketing.subscriptions"]`, and Central's package record lists
  exactly one module. There is no submodule-only API, so the known shared `getDefaultModule()`
  limitation does not bite here.
- Public type names extracted from the bala (`grep -oE "^public type [A-Za-z0-9_]+"` → 32 unique)
  compared against type names in the new render (32 unique): `comm -23` (source-only) empty,
  `comm -13` (render-only) empty. Perfect 1:1.
- `public isolated client class Client` and all 9 `remote isolated function`s plus `init` are
  present in both renders.
- `utils.bal` contains 6 module-private `isolated function`s and a private `enum EncodingStyle`;
  none is `public`, so their absence is correct, not a gap.

## 7. Compiler plugin

The package has no compiler plugin. `find src -maxdepth 2 -type d -name "*compiler-plugin*"`
returns nothing at tag `v2.0.2`, and the bala root contains only
`bala.json  dependency-graph.json  docs  modules  package.json` — no `compiler-plugin/` directory
and no `compiler-plugin.json`. Nothing plugin-derived is expected in the render, and nothing is
missing on that account.

## 8. Other considerations

- Not deprecated. Central: `"deprecated": null`, `"deprecateMessage": ""`, `pullCount` 31,
  `ballerinaVersion` 2201.12.2, `graalvmCompatible: true`.
- Stable major (`2.0.2`), OpenAPI-tool generated (`client.bal` header: "AUTO-GENERATED FILE").
- Size impact is negligible: +1 line (+0.13%). The `int:Signed32` change slightly reduces token
  count per occurrence; the `@display` line adds one.
- Doc quality is good — every record field and every remote function carries a description, and the
  full 194-line README (Overview, Setup, Quickstart, Examples) is embedded verbatim.
- The render is not compilable Ballerina on either side (see section 5 items 4–6), but `new` removes
  the one construct that was outright unlexable (`anydata Additional Values`).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 761 / 762 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; README 7/202, Types 204, Client 721 (old) / 722 (new) |
| `diff -u old new` | 12 hunks, +20/−19 lines; all reviewed |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 12 / 0 |
| `grep -c '@display'` old / new | 0 / 1 |
| `grep -c 'Additional Values'` old / new | 7 / 0 |
| `grep -c '    remote function'` old / new | 9 / 9 |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, v2.0.2; `v2.0.2^{}` = `572edd1f1ede64731e8ccd7a2fa569f3b70d1884` |
| `git clone --depth 1 --branch v2.0.2 …` | succeeded into scratch `src/` |
| `diff -q src/ballerina/{client,types,utils}.bal <bala>/modules/…/` | identical (all 3) |
| `diff -q src/ballerina/README.md <bala>/docs/README.md` | identical |
| `grep -c "int:Signed32" <bala>/…/types.bal` | 12 (lines 27, 83, 99, 165, 210, 280, 286, 290, 320, 346, 364, 449) |
| `grep -n "@display" <bala>/…/types.bal` | only line 226, above `ConnectionConfig` (line 227) |
| `grep -n "remote isolated function" <bala>/…/client.bal` | 9 hits (47, 66, 83, 101, 121, 140, 157, 177, 194) |
| `grep -cE "^public type" <bala>/…/types.bal` | 32 |
| Python JSON typeDef diff (32 vs 32) | only 12 `Signed32` renames + 1 annotation addition; 0 added/removed |
| Python JSON client-function diff (10 vs 10) | only 7 × `Additional Values` parameter removed; 0 added/removed |
| `old['readme'] == new['readme']`, `old['description'] == new['description']` | `True`, `True` |
| Render README block (lines 8–201) vs `docs/README.md` | identical content, all 194 lines, both sides |
| `comm -23 src_types.txt new_types.txt` / `comm -13 …` | empty / empty (32 = 32) |
| `diff old_types.txt new_types.txt` | no output (same set) |
| `ls <bala>/…` and `find src -type d -name '*compiler-plugin*'` | no compiler plugin |
| `cat <bala>/package.json` | `export: ["hubspot.marketing.subscriptions"]`, single module |
| `GET api.central.ballerina.io/2.0/registry/packages/ballerinax/hubspot.marketing.subscriptions/2.0.2` | version 2.0.2, not deprecated, 1 module |
| `types.bal:189-193`, `:227-265`, `:471-479` read | verified OAuth2/ConnectionConfig/Queries field defaults and closedness |

## 10. Caveats and unverified items

- The `@display` annotation value is rendered as the raw string `{label: "Connection Config"}`; that
  matches the source text exactly, but whether the renderer's placement (a bare line directly above
  `type`, separated from the doc comment by a blank line) is the intended final format is a
  renderer-design question I did not verify against the spec-v2 design docs.
- The fabricated `channel = "EMAIL"` / `businessUnitId = 0` defaults are present in **both** JSONs,
  so they are produced by the Java extractor, not by `toSyntaxString`. I confirmed they do not exist
  in the library source, but I did not trace where in the extractor they are synthesised — the
  extractor source was not in scope for this review.
- I did not attempt to compile either render; the syntax claims in section 5 (items 4–6) are from
  reading the Ballerina grammar rules, not from a `bal build` run.

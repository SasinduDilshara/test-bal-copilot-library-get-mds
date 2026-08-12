# ballerinax/hubspot.marketing.events 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.events` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.events |
| Tag reviewed | `v1.0.2` (commit `8d333fa7e2fb53f1172291e8aeaeb0410f33c7f9`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.events/1.0.2` |
| Old render | `1366` lines |
| New render | `1367` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three changes, all improvements:

1. 28 record fields whose type was emitted as the version-qualified junk ref
   `ballerina/lang.int:0.0.0:Signed32` are now emitted correctly as `int:Signed32`.
2. 14 client remote-function signatures no longer carry the malformed synthetic parameter
   `anydata Additional Values` (an identifier containing a space — not parseable Ballerina).
3. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig`, which exists in
   the library source, is now surfaced. `old` dropped all annotations (`annotations` key absent from
   every `typeDef` in `old/*.json`; present on exactly 1 typeDef in `new`).

No declaration is added or removed. Both renders carry the full public surface: 66/66 public types,
36/36 remote functions, plus `init`. Both have 0 `// Unknown type:` placeholders. Coverage against
the library is complete on both sides — this package has a single module (`hubspot.marketing.events`)
which is the default module, so the known submodule gap does not apply.

Several accuracy defects remain in `new`, but every one of them is also in `old` (Section 5), so
none is a regression.

## 2. Change inventory

Mechanical (from `diff -u old new`):

| Metric | Value |
|---|---|
| Lines added | 43 |
| Lines removed | 42 |
| Hunks | 30 |
| Net | +1 line |

Declaration-level counts (identical on both sides):

| Kind | old | new | library source |
|---|---|---|---|
| `type` definitions rendered | 66 | 66 | 66 `public type` |
| `client class` | 1 | 1 | 1 (`public isolated client class Client`) |
| `remote function` | 36 | 36 | 36 `remote isolated function` |
| `init` | 1 | 1 | 1 |
| module-level `function` (non-client) | 1 (the `init` line match) | 1 | 0 public |
| `enum` / `const` / `annotation` / `service` / `listener` | 0 | 0 | 0 public |
| `// Unknown type:` placeholders | 0 | 0 | — |
| `// --- section ---` markers | 4 | 4 | — |

**Declarations added: 0. Declarations removed: 0.** Every diff line is a modification inside an
existing declaration. Classification of the 42 removed / 43 added lines:

| Change | Removed | Added |
|---|---|---|
| `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (record fields) | 28 | 28 |
| Client remote-function signature: `anydata Additional Values,` dropped | 14 | 14 |
| `@display {label: "Connection Config"}` emitted | 0 | 1 |

The 28 type-ref fixes span 20 type definitions: `GetParticipationsExternalAccountIdExternalEventIdBreakdownGetParticipationsBreakdownByExternalEventIdQueries`,
`ParticipationProperties`, `MarketingEventPublicReadResponse` (×4), `PublicList`,
`MarketingEventIdentifiersResponse`, `ConnectionConfig` region neighbour `AppInfo`,
`SearchPublicResponseWrapper`, `GetParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventIdQueries`,
`CollectionResponseWithTotalPublicListNoPaging`, `BatchResponseSubscriberVidResponse`-family batch
records (×4), `CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging`,
`EventDetailSettings`, `GetParticipationsContactsContactIdentifierBreakdownGetParticipationsBreakdownByContactIdQueries`,
`MarketingEventPublicReadResponseV2` (×4), `AttendanceCounters` (×4),
`CollectionResponseWithTotalParticipationBreakdownForwardPaging`, `GetQueries`.

JSON-level confirmation: `typeDefs` 66 → 66, identical name sets, 20 typeDefs differ; `clients[0].functions`
37 → 37, identical name sets, 14 differ and the *only* delta in each is the loss of the parameter
`{"name":"Additional Values","type":{"name":"anydata"}}`. No return type, description, or other
parameter changed anywhere. `readme`, `description`, `name`, `functions`, `services`, `annotations`
top-level keys are byte-identical between the two JSONs.

The 14 affected remote functions are exactly those whose `*…Queries` included-record parameter is an
**open** record (`record { … }` rather than `record {| … |}`), i.e. it has an implicit `anydata…;`
rest field. `old` materialised that rest field as a positional parameter literally named
`Additional Values`.

## 3. Correctness against library source

Bala and GitHub tag agree exactly — `diff -q` on all three module files
(`client.bal`, `types.bal`, `utils.bal`) between
`.../bala/…/1.0.2/any/modules/hubspot.marketing.events/` and `src/ballerina/` reports no difference.
So the tag is a faithful stand-in for what the extractor consumed.

Verified for each of the three change classes:

- **`int:Signed32`.** `grep -c 'int:Signed32' types.bal` = **28** in the library source, exactly
  matching the 28 fields corrected in `new`. `new` therefore reproduces the source spelling verbatim;
  `old`'s `ballerina/lang.int:0.0.0:Signed32` was an internal symbol path with a fabricated `0.0.0`
  version and is not valid Ballerina. Spot-checked `types.bal:277-286`
  (`GetParticipationsMarketingEventIdBreakdownGetParticipationsBreakdownByMarketingEventIdQueries.'limit`)
  and the `AttendanceCounters` / `MarketingEventPublicReadResponse` fields.
- **`@display` annotation.** `types.bal:216` is `@display {label: "Connection Config"}` immediately
  above `types.bal:217 public type ConnectionConfig record {|`. It is the **only** `@display` in the
  whole module (`grep -n '@display' *.bal` returns one hit), and `new` emits exactly one `@display`
  line, on the right type, with the right label. Correct and complete.
- **Dropped `anydata Additional Values`.** Confirmed against `client.bal:50, 109, 340, 477, 674` etc.:
  the source parameter lists end in `*XxxQueries queries` and contain no such parameter. E.g.
  `client.bal:674`
  `remote isolated function getEventsSearchDoSearch(map<string|string[]> headers = {}, *GetEventsSearchDoSearchQueries queries) returns CollectionResponseSearchPublicResponseWrapperNoPaging|error`.
  `types.bal:402-405` shows `GetEventsSearchDoSearchQueries` is an open record with a single field
  `string q`. So `old`'s extra parameter was a rest-field artifact, not a real API parameter, and
  removing it moves the render closer to the source.

Full-surface check (script over bala `*.bal` vs both renders): all 66 `public type` names appear in
both renders, no extras; all 36 `remote isolated function` names appear in both renders, no extras.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Full unified diff (329 lines) read end to end; every removed line falls into exactly two buckets
  (`ballerina/lang.int:0.0.0:Signed32` × 28, `anydata Additional Values` × 14) — verified by
  `grep '^-[^-]' full.diff | grep -v … | grep -v …` returning **zero** unclassified removed lines.
- JSON set-difference: `typeDefs` names only-in-old = `[]`; `clients[0].functions` names
  only-in-old = `[]`; per-function parameter set-difference shows the only lost parameter across all
  37 client functions is `Additional Values` (14×). No return type, description, default value, or
  optionality changed.
- `readme` field byte-identical (10964 chars both); README section spans lines 7–270 on both sides
  and the first diff hunk starts at line 277, so no README content was lost.
- Section markers: 4 on both sides, same order (`README`, `END README`, `Types`, `Client`).
- Doc comments: no `#` line appears in the removed set.
- `// Unknown type:` count 0 → 0 (nothing degraded).
- Non-ASCII byte count 0 → 0 (no encoding regression).

## 5. Issues in `new` (independent of `old`)

All of the following are present **identically in `old`**, so none is a regression, but they are real
inaccuracies a consumer of the `new` render would be misled by.

1. **Included-record parameters are rendered twice and lose the `*`.** Source
   `client.bal:50`: `…, map<string|string[]> headers = {}, *PostAttendance…Queries queries)`.
   Render (new:1227): `…, map<string|string[]> headers = {}, string externalAccountId = "", PostAttendance…Queries queries)`
   — the record's field `externalAccountId` (`types.bal:595-598`) is flattened into a parameter **and**
   the record itself is repeated as a plain (non-included) parameter. The result does not compile
   (a required parameter follows defaultable ones, and the argument would be supplied twice) and
   overstates the arity. Affects all 24 functions that take a `*Queries` parameter.
2. **Record field default values are dropped and defaulted fields are re-marked optional.**
   `types.bal:281` `int:Signed32 'limit = 10;` renders as `int:Signed32 'limit?;` (new:277).
   `ConnectionConfig` loses every default: source `decimal timeout = 30`, `string forwarded = "disable"`,
   `http:HttpVersion httpVersion = http:HTTP_2_0`, `http:Compression compression = http:COMPRESSION_AUTO`,
   `boolean validation = true`, `boolean laxDataBinding = true`, `http:ClientHttp1Settings http1Settings = {}`,
   `http2Settings = {}`, `cache = {}`, `responseLimits = {}`, `socketConfig = {}` (`types.bal:216-256`)
   all render as bare `?` fields. An LLM reading this cannot know the real defaults.
3. **Synthetic, wrong defaults on the flattened query parameters.** `int:Signed32 limit = 0`
   (new:1231) where the source default is `10` (`types.bal:281`), and `string externalAccountId = ""`
   where the source field is optional with no default (`types.bal:597`). These are invented values.
4. **Closed records are rendered as open.** `public type ConnectionConfig record {| … |};`
   (`types.bal:217`) renders as `type ConnectionConfig record { … };`. Same for every `record {| |}`
   in the module.
5. **Visibility and isolation qualifiers dropped.** No `public` on any of the 66 types; the client is
   `client class Client` in the render vs `public isolated client class Client` (`client.bal:23`), and
   remote methods lose `isolated`.
6. **Multi-line doc comment mangled into a bare source line.** `new:531-532`:
   ```
       # Enables relaxed data binding on the client side. When enabled, `nil` values are treated as optional,
   and absent fields are handled as `nilable` types. Enabled by default
   ```
   The continuation line lost its `#` prefix and its indentation (source `types.bal:254-255` has both
   lines prefixed with `#`). Identical defect at `old:531`.
7. **Blank line inserted between the doc comment and the declaration**, throughout the Types section,
   which detaches the documentation from the symbol it documents. In `new` this now also separates
   the doc comment from the new `@display` annotation.

Not an issue: the `// Special Agent Note: X FROM ballerina/http package` trailing comments are
deliberate renderer annotations and are identical on both sides.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `export` = `["hubspot.marketing.events"]`; Ballerina Central reports exactly one
  module for `1.0.2`. The bala contains one directory under `modules/`, which is the default module.
  There is therefore no submodule-only API and the known `getDefaultModule()` limitation is inert here.
- Public symbols in the default module: 66 `public type` + 1 `public isolated client class Client`.
  All 67 appear in both renders (verified by name-set comparison).
- Everything in `utils.bal` (`SimpleBasicType`, `Encoding`, `EncodingStyle`, `defaultEncoding`,
  `getDeepObjectStyleRequest`, `getFormStyleRequest`, `getSerializedArray`, `getSerializedRecordArray`,
  `getEncodedUri`, `getPathForQueryParam`) is module-private (no `public` qualifier) and correctly
  absent from both renders.

## 7. Compiler plugin

The package ships **no compiler plugin**. The bala has no `compiler-plugin/` directory
(`ls .../1.0.2/any/` → `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`) and the
repo at `v1.0.2` has no `compiler-plugin` / `*-compiler-plugin` directory at depth ≤ 2. Nothing is
therefore expected to surface in the render from a plugin, and nothing is missing on that account.

## 8. Other considerations

- Not deprecated (Central `deprecated: null`, empty `deprecateMessage`). Stable `1.0.x`.
- Built with `ballerina_version: 2201.12.2`, `graalvmCompatible: true`, `template: false`.
- Size is unchanged in practice (+1 line, ~+0.03%). The `new` render is marginally *cheaper* per token
  despite the extra line, because 28 occurrences of the 33-character `ballerina/lang.int:0.0.0:Signed32`
  collapse to the 12-character `int:Signed32`, and 14 signatures shed `anydata Additional Values, `.
- The `old` render contained two distinct constructs that are not valid Ballerina
  (`ballerina/lang.int:0.0.0:Signed32` as a type, and a parameter named `Additional Values`). Both are
  gone in `new`, which materially improves the render's usability as LLM context. The remaining
  non-compiling constructs listed in Section 5 are shared with `old`.
- Low Central pull count (21) — the render quality for this connector has had little real-world
  exercise.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 1366 / 1367 |
| `diff -u old new \| grep -c '^-[^-]'` / `'^+[^+]'` | 42 removed / 43 added |
| `diff -u old new \| wc -l` | 329 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -c ':0\.0\.0:'` old / new | 28 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 28 / 0 |
| `grep -c 'Additional Values'` old / new | 14 / 0 |
| `grep -c '@display'` old / new | 0 / 1 |
| `grep -n '^// --- '` old / new | 4 markers each (README/END README/Types/Client), Client at 1218 vs 1219 |
| `grep -c '^    remote function'` old / new | 36 / 36 |
| `grep -cE '^(public )?type '` old / new | 66 / 66 |
| `grep -c '^and absent fields'` old / new | 1 (line 531) / 1 (line 532) |
| `LC_ALL=C grep -c '[^ -~]'` old / new | 0 / 0 |
| `grep '^-[^-]' full.diff \| grep -v 'lang.int:0.0.0:Signed32' \| grep -v 'anydata Additional Values'` | empty — all removals classified |
| `grep '^+[^+]' full.diff \| grep -v 'int:Signed32'` | 1 `@display` line + 10 client signature lines (the other 4 signature lines contain `int:Signed32`) |
| `git ls-remote --tags <repo>` | `v0.1.0`, `v1.0.0`, `v1.0.1`, **`v1.0.2`** → `8d333fa7e2fb53f1172291e8aeaeb0410f33c7f9` |
| `git clone --depth 1 --branch v1.0.2` | succeeded |
| `src/ballerina/Ballerina.toml:5` | `version = "1.0.2"` |
| `diff -q bala/modules/hubspot.marketing.events/{client,types,utils}.bal src/ballerina/…` | no differences (all three) |
| bala `package.json` | `export: ["hubspot.marketing.events"]`, `ballerina_version: 2201.12.2`, `graalvmCompatible: true` |
| `ls bala/1.0.2/any/` | `bala.json docs dependency-graph.json modules package.json` — no `compiler-plugin/` |
| `find src -maxdepth 2 -iname '*compiler-plugin*'` | no hits |
| `grep -cE '^public type ' bala types.bal` | 66 |
| `grep -c 'remote isolated function' bala client.bal` | 36 |
| `grep -c 'resource isolated function' bala client.bal` | 0 |
| `grep -c 'int:Signed32' bala types.bal` | 28 |
| `grep -n '@display' bala *.bal` | 1 hit, `types.bal:216` |
| `grep -rnE '^public ' bala/modules/…` | 66 types + 1 `public isolated client class Client` |
| Python: public-type name set vs rendered type name set | old: 0 missing / 0 extra; new: 0 missing / 0 extra |
| Python: source remote-fn name set vs rendered | old: 0 missing / 0 extra; new: 0 missing / 0 extra |
| Python: JSON top-level key comparison | `name`, `description`, `readme` equal; `typeDefs` 66/66; `clients` 1/1; `functions`/`services`/`annotations` 0/0 both |
| Python: JSON typeDef keyset histogram | old: 66× `(description,fields,name,type)`; new: 65× same + 1× with `annotations` |
| Python: JSON typeDefs differing | 20 (all `Signed32` type-name changes + `ConnectionConfig` annotation) |
| Python: JSON client functions differing | 14, each losing only `("Additional Values","anydata",None)`; no return/desc changes |
| `types.bal:216-217` | `@display {label: "Connection Config"}` / `public type ConnectionConfig record {\|` |
| `types.bal:277-286` | `'limit` field has source default `= 10`; render emits `'limit?` and param `limit = 0` |
| `types.bal:402-405` | `GetEventsSearchDoSearchQueries` open record, single field `string q` |
| `types.bal:595-598` | `PostAttendance…Queries` open record, single optional field `externalAccountId` |
| `client.bal:23, 50, 109, 340, 477, 674` | signatures confirmed, all use `*XxxQueries queries` |
| Central API `packages/ballerinax/hubspot.marketing.events/1.0.2` | `deprecated: None`, 1 module, `pullCount: 21` |
| `OLD_AND_NEW_DIFFS/hubspot.marketing.events_diff.md` | claims re-derived independently and confirmed (1366/1367, +43/−42, 30 hunks, 28→0 versioned refs, 0 decls added/removed) |

## 10. Caveats and unverified items

- Neither render was compiled or parsed with the Ballerina compiler; claims that specific rendered
  constructs "do not compile" (Section 5 items 1, 6, and `old`'s `anydata Additional Values`) are
  based on reading the Ballerina grammar, not on a compiler run. The renders are `.bal.txt` context
  documents and are not expected to compile, so this is characterisation rather than a defect claim.
- The two `ballerina-vscode` source trees that produced the renders were not inspected; the causal
  attribution of the three changes to "spec v2" is inferred from the brief plus the observed diff, not
  from reading the extractor/renderer code.
- `dependency-graph.json` and `bala.json` were not examined beyond confirming their presence.
- The README block (lines 7–270) was confirmed byte-identical between the two renders via the JSON
  `readme` field and the absence of diff hunks in that range; its fidelity to the upstream
  `docs/README.md` was not separately audited.

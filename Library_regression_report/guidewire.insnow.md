# ballerinax/guidewire.insnow 0.2.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/guidewire.insnow` |
| Pinned version | `0.2.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-guidewire.insnow |
| Tag reviewed | `v0.2.0` (commit `12b6148e7f42399b5cbf67b20bc5917de030493f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/guidewire.insnow/0.2.0` |
| Old render | `2237` lines |
| New render | `2249` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. The only differences are (a) 12 added lines
carrying 12 annotations that genuinely exist in the published source (11 `@jsondata:Name`,
1 `@display`) and (b) removal of 8 bogus `anydata Additional Values` parameters that were
syntactically invalid Ballerina and did not correspond to any real parameter. Nothing is dropped,
truncated, or made less accurate. The declaration inventory (73 types, 815 record fields, 1 client
class, 28 client functions) is byte-for-byte identical between the two renders apart from those
two changes, and matches the bala source exactly.

Several inaccuracies remain in `new`, but every one of them is also present in `old` (included-record
`*Queries` parameters mis-expanded, invented/dropped default values, closed records rendered as open).
They are renderer-level limitations, not regressions.

## 2. Change inventory

Mechanical totals (`diff -u old new`): 15 hunks, 20 content lines added, 8 content lines removed,
net +12 lines (2237 → 2249).

| Kind | Added | Removed | Modified |
|---|---|---|---|
| Type definitions (`type X record`) | 0 | 0 | 9 (annotations only) |
| Record fields | 0 | 0 | 0 |
| Client classes | 0 | 0 | 0 |
| Client functions | 0 | 0 | 8 (parameter list only) |
| Functions / enums / consts / annotations / services / listeners | 0 | 0 | 0 |
| `@jsondata:Name` annotation lines | 11 | 0 | — |
| `@display` annotation lines | 1 | 0 | — |
| `anydata Additional Values` parameters | 0 | 8 | — |

Set-level checks (all confirm "no add/remove"):

- Type names: `grep -oE '^type [A-Za-z0-9_]+'` → 73 in `old`, 73 in `new`, `diff` empty.
- Record fields: scripted `(record, field)` extraction → 815 pairs in `old`, 815 in `new`, sets equal.
- Resource-function paths: 27 in `old`, 27 in `new`, `diff` empty.
- JSON models: `typeDefs` 73/73, `clients` 1/1, `clients[0].functions` 28/28, `functions` 0/0,
  `services` 0/0, `annotations` 0/0; `name`, `description`, `readme` byte-identical.
- Section markers: 4 in both (`README`, `END README`, `Types`, `Client`).
- `// Unknown type:` placeholders: 0 in both (this library had no degraded types even on `main`).
- Version-qualified type refs (`mod:1.2.3:Type`): 0 in both.

The 9 typeDefs whose JSON changed are exactly `Policy`, `PolicyMini`, `Document`, `PolicyDetails`,
`ConnectionConfig`, `ApplicationMini`, `Application`, `Driver`, `Quote` — in each case the sole delta
is a new `annotations` array on a field (or on the type, for `ConnectionConfig`).

The 8 client functions whose JSON changed are exactly the 8 resource functions that take an included
record `*XQueries queries` parameter. In each, the only delta is the removal of
`{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}`.

## 3. Correctness against library source

The bala's `modules/guidewire.insnow/{client,types,utils}.bal` are byte-identical to
`ballerina/{client,types,utils}.bal` at tag `v0.2.0` (`diff -q`, all three "same"), so GitHub and
the bala agree and either can be cited.

**Annotations added by `new` — all 12 verified real and correctly placed.**

- `types.bal` contains exactly 11 `@jsondata:Name` annotations (8 × `{value: "_links"}`,
  3 × `{value: "_revision"}`) and exactly 1 `@display {label: "Connection Config"}`; there are no
  other annotations anywhere in the module (`grep -hoE '@[a-zA-Z]+:?[a-zA-Z]* ?\{' *.bal`).
- `new` emits exactly 8 × `_links` and 3 × `_revision` — same multiset.
- A scripted pairing of *(record name, annotation value, annotated field)* from the source and from
  `new` produced identical 11-element sorted lists:
  `Application/_links/Link[] links?`, `ApplicationMini/_links/Link[] links?`,
  `Document/_links/Link[] links?`, `Driver/_links/Link[] links?`, `Driver/_revision/string revision?`,
  `Policy/_links/Link[] links?`, `PolicyDetails/_links/Link[] links?`,
  `PolicyDetails/_revision/string revision?`, `PolicyMini/_links/Link[] links?`,
  `Quote/_links/Link[] links?`, `Quote/_revision/string revision?`.
  So every annotation is attached to the correct record *and* the correct field.
- `@display {label: "Connection Config"}` is at `types.bal:515`, immediately above
  `public type ConnectionConfig record {|` — `new` places it in the same position
  (new render line 1492, above `type ConnectionConfig record {`).

This is a material accuracy gain: `_links` / `_revision` are the actual wire names of those JSON
fields. Without the annotation, an LLM reading `old` would emit `links` / `revision` on the wire and
the request/response mapping would be wrong.

**Parameters removed by `new` — verified bogus.**

The real signature at `client.bal:41` is
`resource isolated function get addresses/countries(map<string|string[]> headers = {}, *GetSupportedCountriesQueries queries) returns ListCountry|error`.
There is no parameter named `Additional Values` anywhere in `client.bal`. The old JSON's
`{"name":"Additional Values","description":"Capture key value pairs","type":"anydata"}` is a
docs-model artifact standing in for the open record's implicit `anydata...;` rest descriptor
(`GetSupportedCountriesQueries` is declared `record {` , not `record {| |}`). Rendered into a
parameter list it produced `..., anydata Additional Values, ...` — an identifier containing a space,
which will not parse as Ballerina, positioned as a required parameter that does not exist.

Nuance worth recording: dropping it does lose the only textual hint that these query records are
open. That hint is worth ~nothing here, because the renderer emits *every* record as `record {`
regardless of openness (`ConnectionConfig` is `record {| |}` in source and `record {` in both
renders), so open/closed is not expressible in this format on either side. Net: no real information
lost, one invalid construct removed.

**Everything else spot-checked against source.**

- All 27 resource-function accessor+path strings in `new` match the 27 in `client.bal` exactly
  (`diff` of sorted lists, empty).
- All 27 return types match: e.g. `.../drivers` → `ListDriver|error` (`client.bal:202`),
  `.../documents/[documentId]/content` → `byte[]|error` (`client.bal:191`),
  `post addresses/verificationRequest` → `error?` (`client.bal:85`),
  `patch policies/[systemId]` → `PolicyDetails|error` (`client.bal:345`).
- `init(ConnectionConfig config, string serviceUrl) returns error?` matches `client.bal:31`.
- 73 rendered type names == the 73 `public type` names in `types.bal` (`diff` empty).
- 815 rendered `(record, field)` pairs == the 815 in `types.bal` (set difference empty in both
  directions). No field dropped, none invented.
- README section (render lines 8–117) is a complete reproduction of `docs/README.md` (109 lines);
  `diff` shows only one trailing blank line added. Identical in `old` and `new`.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

1. Full `diff -u old new` read in its entirety (152 lines, 15 hunks). Every removed line is one of
   the 8 `anydata Additional Values` occurrences; every added line is either the same signature
   without that token, or one of the 12 annotation lines. There is no third category.
2. Declaration sets compared by extraction, not by text: type names (73 = 73), record fields
   (815 = 815), resource paths (27 = 27), JSON `typeDefs` names (equal sets), JSON client function
   count (28 = 28). No deletion anywhere.
3. Doc comments: the type-def region of the two files differs only by the 12 annotation lines, so
   no `#` documentation was lost. README block byte-identical between sides.
4. `// Unknown type:` count 0 → 0 (no degradation either way), section markers 4 → 4.
5. Default values, return types and parameter defaults in the 8 changed signatures were compared
   token by token: apart from the deleted bogus parameter, they are character-identical.

## 5. Issues in `new` (independent of `old`)

All seven below are also present verbatim in `old` — they are renderer limitations, not regressions.
Listed because they would mislead an LLM consuming the render.

1. **Included-record parameters are double-rendered.** Source `*GetQuotesQueries queries` becomes,
   in the render, the record's 15 fields flattened as positional parameters *and* a further
   `GetQuotesQueries queries` parameter (new line 2164). The result is neither the real signature
   nor valid Ballerina. Affects all 8 functions with `*XQueries queries`.
2. **Invented default values on the flattened query parameters.** `GetQuotesQueries.createdSinceDate`
   is `string createdSinceDate?;` (`types.bal`, optional, no default) but renders as
   `string createdSinceDate = ""`. Likewise `GetDriversQueries.typeCd?` renders as
   `"Driver"|"NonDriver" typeCd = "Driver"`. An LLM would infer wrong wire defaults.
3. **Real default values dropped in the record type definitions.** `VerifyAddressQueries.addressType = "Combined"`
   renders as `addressType?`; `GetSupportedCountriesQueries.sortType = "asc"` renders as `sortType?`;
   in `ConnectionConfig`, `httpVersion = http:HTTP_2_0`, `timeout = 30`, `forwarded = "disable"`,
   `cache = {}`, `compression = http:COMPRESSION_AUTO`, `responseLimits = {}`, `socketConfig = {}`,
   `validation = true`, `laxDataBinding = true` all render as bare `?`.
4. **Closed records rendered as open.** `public type ConnectionConfig record {| ... |}` renders as
   `type ConnectionConfig record { ... }`.
5. **Parameter ordering is not valid Ballerina.** e.g.
   `(map<string|string[]> headers = {}, "asc"|"desc" sortType = "asc", GetSupportedCountriesQueries queries)`
   places a required parameter after defaultable ones.
6. **A multi-line doc comment loses its `#` continuation prefix.** New render line 1531 is
   `and absent fields are handled as \`nilable\` types. Enabled by default.` at column 0, outside any
   comment (source `types.bal` has `# ` on that continuation line). One occurrence, present in `old`
   at line 1525 too.
7. **`public` and `isolated` qualifiers are dropped everywhere** (`grep -c 'isolated function'` → 0,
   `grep -c '^public type'` → 0 in both renders), so the render cannot be compiled or used to reason
   about concurrency-safety.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

- The bala exports exactly one module: `package.json` `"export": ["guidewire.insnow"]`, and
  `modules/` contains only `guidewire.insnow`. Ballerina Central metadata lists a single module.
  Therefore the `getDefaultModule()`-only extraction limitation described in the brief costs nothing
  here — there are no submodules.
- Public symbols in the default module: 73 `public type` in `types.bal`, plus
  `public isolated client class Client` (`client.bal:24`) with `public isolated function init` and
  27 `resource isolated function`s. `utils.bal` declares only module-private symbols
  (`SimpleBasicType`, `Encoding`, `EncodingStyle`, `defaultEncoding`, and 6 non-public
  `isolated function`s) — correctly excluded.
- All 73 types and all 28 client functions appear in both renders. Nothing public is missing.

## 7. Compiler plugin

The package has **no compiler plugin**: no `compiler-plugin/` directory in the bala
(`ls` of the bala shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json`), and no `*compiler-plugin*` directory anywhere in the `v0.2.0` clone
(`find -maxdepth 2 -iname '*compiler-plugin*'` → empty). `Ballerina.toml` declares no
`[[platform.java*.dependency]]` and no plugin section. Nothing plugin-derived is therefore expected
in, or missing from, the render.

## 8. Other considerations

- **Pre-1.0 version.** `0.2.0` is the latest published version (only `v0.1.0` and `v0.2.0` exist as
  tags). API may change without a major-version signal.
- **Not deprecated.** Central returns `"deprecated": null`, `"deprecateMessage": ""`.
- **Distribution.** `Ballerina.toml` `distribution = "2201.12.2"`, matching Central's
  `ballerinaVersion: 2201.12.2`.
- **Low adoption.** Central `pullCount: 29`.
- **Size/token impact.** +12 lines (+0.54%). Negligible cost for a correctness win of 12
  annotations that fix 11 wire-name mappings.
- **Doc quality is high.** Every type, field and operation carries a `#` doc comment sourced from the
  OpenAPI description; the render preserves them.
- **The render is not compilable Ballerina** on either side (see §5 items 1, 5, 6, 7). This is a
  general property of this output format, not specific to this library.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 2237, new 2249 |
| 2 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 3 | `grep -n '^// --- '` both | 4 markers each; Types at 120 both, Client at 2124 (old) / 2136 (new) |
| 4 | `diff -u old new \| wc -l` | 152 lines; `grep -c '^+'` = 21 (incl. header), `'^-'` = 9 (incl. header) → +20/−8 content |
| 5 | `grep -c 'anydata Additional Values'` | old 8, new 0 |
| 6 | `grep -oE '^\s*@[A-Za-z:]+' \| sort \| uniq -c` | new: 11 `@jsondata:Name`, 1 `@display`; old: none |
| 7 | `ls -R` of bala | modules/ contains only `guidewire.insnow`; no `compiler-plugin/` |
| 8 | `grep -c 'jsondata:Name' bala types.bal` | 11 |
| 9 | `grep -hoE '@jsondata:Name \{value: "[^"]*"\}' \| uniq -c` source vs new | both 8 × `_links`, 3 × `_revision` |
| 10 | Scripted (record, annotation, field) triples, source vs new render | 11 triples each, sorted lists identical → `MATCH` |
| 11 | `grep -n '@display' bala/*.bal` | one hit, `types.bal:515`, on `ConnectionConfig` |
| 12 | `git ls-remote --tags <repo>` | `v0.1.0`, `v0.2.0`; `v0.2.0^{}` = `12b6148e7f42399b5cbf67b20bc5917de030493f` |
| 13 | `git clone --depth 1 --branch v0.2.0` then `diff -q` vs bala for client.bal/types.bal/utils.bal | all three identical |
| 14 | `grep -c '^public type' bala types.bal` | 73 |
| 15 | Rendered type-name lists vs source list (`diff`) | 73/73/73, both diffs empty |
| 16 | Scripted (record, field) pair sets: source / old / new | 815 / 815 / 815; source−new = ∅, new−source = ∅, old == new |
| 17 | Sorted resource accessor+path lists: source / old / new | 27 each; old vs new empty diff; source vs new empty diff |
| 18 | `grep -cE '^\s+resource isolated function' bala client.bal` | 27; plus 1 `public isolated function init` at line 31 |
| 19 | Return types read from `grep -nE '^\s+resource isolated function' client.bal` vs new render | all 27 match |
| 20 | `grep -c '\*[A-Za-z]*Queries queries' client.bal` | 8 — equals the 8 changed client functions |
| 21 | `awk` extraction of `GetSupportedCountriesQueries` / `GetQuotesQueries` / `GetDriversQueries` / `VerifyAddressQueries` from source vs both renders | defaults `= "asc"`, `= "Combined"` present in source, absent (`?`) in both renders |
| 22 | Python JSON compare of both `*.json` | `name`/`description`/`readme` equal; typeDefs 73/73 same names, 9 differ (annotations only); clients 1/1, functions 28/28, 8 differ (removed `Additional Values` param only) |
| 23 | `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | 0 / 0 (no version-qualified refs on either side) |
| 24 | `diff <(sed -n '1,109p' bala/docs/README.md) <(sed -n '8,117p' new render)` | only `109a110 >` (trailing blank line) |
| 25 | `curl` Central `/2.0/registry/packages/ballerinax/guidewire.insnow/0.2.0` | `deprecated: None`, `ballerinaVersion: 2201.12.2`, single module, `pullCount: 29`, `visibility: public` |
| 26 | `grep -nE '^(public\|isolated\|final\|const\|enum\|annotation\|listener\|type\|class\|client\|function\|service)' utils.bal client.bal` | only module-private decls in utils.bal; `public isolated client class Client` at client.bal:24 |
| 27 | Column-0 non-comment non-declaration lines after the README block | old 1, new 2 (the extra is the `@display` line); the shared one is the broken doc continuation at old:1525 / new:1531 |
| 28 | `grep -c 'isolated function'` / `grep -c '^public type'` in new render | 0 / 0 |
| 29 | Precomputed `OLD_AND_NEW_DIFFS/guidewire.insnow_diff.md` | claims +20/−8, 15 hunks, 0 declarations added/removed, 0 unknown types, 0 versioned refs — all independently reproduced above |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that certain constructs are "not valid Ballerina"
  (parameter named `Additional Values`, defaultable-before-required ordering, bare `type`/`limit`
  keywords in flattened parameters) are based on reading the language rules, not on a compiler run.
  They do not affect the verdict, which rests on the diff inventory.
- The exact upstream mechanism that produced the `"Additional Values"` entry in the `old` JSON was
  inferred from its description string (`"Capture key value pairs"`), its `anydata` type, and its
  appearing on exactly the 8 functions with open included-record query parameters. The extractor
  code itself was not read (the `ballerina-vscode` sources are outside this review's scope), so the
  attribution to the open record's rest descriptor is a strong inference, not a code-verified fact.
- Only the Ballerina-visible surface was audited. The upstream OpenAPI specification that generated
  the connector was not compared against the connector, so a mismatch between the spec and the
  generated Ballerina code (if any) would not have been detected here — but it would affect both
  renders equally.

# ballerinax/scim 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/scim` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-scim |
| Tag reviewed | `v1.0.2` (commit `130b7fb895ddffa5dff30bfe9763630813db0540`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/scim/1.0.2` |
| Old render | `917` lines |
| New render | `918` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Twelve hunks, all of them fixes:
version/module-qualified type references are gone (16 occurrences in `old`, 0 in `new`), the single
`// Unknown type:` placeholder is replaced with the real type alias, a `@display` annotation that
`old` dropped is now emitted, and ten malformed `anydata Additional Values` parameters are removed
from the client's resource-function signatures. No declaration, parameter, doc line, or README
content is lost. Every symbol the default module exports (81 public types + `Client` with 17 resource
methods + `init`) is present in both renders, so there is no coverage gap. A handful of rendering
inaccuracies remain, but all of them are present identically in `old` and are therefore not
regressions.

## 2. Change inventory

Line counts (`wc -l`): old 917, new 918 (+1).
Unified diff: 12 hunks, 5 in the `Types` section, 5 in the `Client` section, 2 in `Types` around
`Bulk_body`/`Users_body`.

| Kind | old | new | Δ |
|---|---|---|---|
| `^type ` declarations | 80 | 81 | +1 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| `resource function` in `client class Client` | 17 | 17 | 0 |
| `client class` | 1 | 1 | 0 |
| `@display` annotations | 0 | 1 | +1 |
| Lines carrying version-qualified refs (`org/mod:x.y.z:Type`) | 8 (16 occurrences) | 0 | −8 |
| `Additional Values` pseudo-parameters | 10 | 0 | −10 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `Special Agent Note` cross-package hints | 17 | 17 | 0 |

JSON model (`python3 -m json.tool --sort-keys`, 4369 → 4296 lines): `typeDefs` 81 → 81,
`clients` 1 → 1 (18 functions each: `init` + 17 resources), `functions` 0, `services` 0,
`annotations` 0. Type-name sets are byte-identical between the two JSONs
(`diff /tmp/old_types.txt /tmp/new_types.txt` → SAME).

**Added (1 declaration)**
- `type OperationObBulk OperationObBulk_inner[];` — replaces `// Unknown type: OperationObBulk`.
  In the JSON this shows as a new `"baseType": "OperationObBulk_inner[]"` on the existing
  `"type": "Other"` entry, i.e. no new type, just a rendered body.

**Removed (0 declarations)** — none.

**Modified (5 categories)**
1. `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` — 6 record fields across
   `GetGroupQueries`, `GetUserQueries`, and the second `*Queries` record (render lines 111/115,
   174/176, 645/649).
2. `ballerinax/scim:1.0.2:X` → `X` in the two union aliases: `Bulk_body` (8 members) and
   `Users_body` (2 members).
3. `@display {label: "Connection Config"}` added above `type ConnectionConfig` (render line 389).
4. `// Unknown type: OperationObBulk` → real alias (render line 731).
5. `anydata Additional Values` parameter removed from 10 client resource functions
   (`get Users`, `post Users`, `get Users/[id]`, `put Users/[id]`, `patch Users/[id]`,
   `get Groups`, `post Groups`, `get Groups/[id]`, `put Groups/[id]`, `patch Groups/[id]`).

## 3. Correctness against library source

Upstream `v1.0.2` `ballerina/{client,types,utils}.bal` are byte-identical to the bala's
`modules/scim/*.bal` (`diff -q` → IDENTICAL for all three), so GitHub and the bala agree; both are
authoritative.

Every change in `new` is confirmed correct against that source:

| Change in `new` | Source evidence |
|---|---|
| `int:Signed32 startIndex?` / `count?` | `modules/scim/types.bal:27,31` (`GetGroupQueries`) and the `GetUserQueries` block — declared exactly as `int:Signed32 startIndex?;` / `int:Signed32 count?;`. `new` matches character-for-character; `old`'s `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina. |
| `@display {label: "Connection Config"}` | `modules/scim/types.bal:200` — `@display {label: "Connection Config"}` immediately above `public type ConnectionConfig record {|`. `old` dropped it entirely. |
| `type OperationObBulk OperationObBulk_inner[];` | `modules/scim/types.bal:405` — `public type OperationObBulk OperationObBulk_inner[];`. Referent `OperationObBulk_inner` is defined at `types.bal:55` and rendered at line 149 of both files. |
| `type Bulk_body BulkUserCreateObject\|…\|BulkGroupDeleteObject;` | `modules/scim/types.bal` — `public type Bulk_body BulkUserCreateObject\|BulkUserUpdateObject\|BulkUserReplaceObject\|BulkUserDeleteObject\|BulkGroupCreateObject\|BulkGroupUpdateObject\|BulkGroupReplaceObject\|BulkGroupDeleteObject;` — same 8 members, same order. |
| `type Users_body UserObject\|UserObjectPassInvite;` | same file, 2 members, same order. |
| Removal of `anydata Additional Values` | The 10 affected methods take an included-record param (`*GetUserQueries queries` etc., `client.bal:41,52,79,91,116,130,141,168,180,205`). Those `*Queries` records are **open** (`record { … };`, not `record {| … |}`), so the doc model exposes their implicit rest field as a pseudo-field named `Additional Values` (`"description": "Capture key value pairs", "type": {"name": "anydata"}`). Rendering it as a parameter produced `anydata Additional Values` — an identifier containing a space, i.e. non-compiling, and placed after defaulted params. No source parameter is named that. Removal loses nothing: record openness is still conveyed by rendering the query records with `record {` rather than `record {\|`, and the render already keeps `record {\|` where the source is closed (10 occurrences in both files). |

Also verified unchanged and correct: escaped identifiers survive intact —
`type Enterprise\ User\ Extension record {` (render line 204) matches `types.bal:286`, and the field
`Enterprise\ User\ Extension urn\:ietf\:params\:scim\:schemas\:extension\:enterprise\:2\.0\:User?;`
(render lines 191/275/671/701) matches `types.bal:93,123,352`.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full `diff -u old new` read line by line — 12 hunks, 20 lines added, 19 removed; every removed line
  is either a version-qualified type name, an `anydata Additional Values` parameter, or the
  `// Unknown type:` placeholder. No doc comment, field, parameter, return type, default value, or
  declaration disappears.
- Declaration-set comparison via the JSON models: `typeDefs` name sets are identical (81 = 81, diff
  empty); client function count identical (18 = 18); `functions`/`services`/`annotations` are 0 on
  both sides.
- README: `d['readme'].strip() == docs/README.md.strip()` → `True` for `new` (3524 chars each), and
  the README region (render lines 8–100) is unchanged between the two files — no hunk touches it.
- Section markers: 4 in both (`README`, `END README`, `Types`, `Client`).
- Cross-package hints (`Special Agent Note`): 17 in both.
- `int:Signed32` occurrences in `new`: 8 — the 6 record fields plus the 2 already-correct
  occurrences inside `resource function get Users` / `get Groups`, so nothing was converted the wrong
  way.

## 5. Issues in `new` (independent of `old`)

All five below are present **identically in `old`**, so none is a regression; they are renderer-level
inaccuracies a consumer should know about.

1. **Client resource signatures invent defaults and duplicate the query params.** Source
   (`client.bal:41`) is
   `resource isolated function get Users(map<string|string[]> headers = {}, *GetUserQueries queries)`.
   Render (line 853) is
   `resource function get Users(map<string|string[]> headers = {}, string filter = "", int:Signed32 startIndex = 0, string domain = "", int:Signed32 count = 0, string attributes = "", string excludedAttributes = "", GetUserQueries queries) returns UserObjectListResponseObject|error;`
   — the included record is flattened into scalar params *and* still listed as `GetUserQueries queries`,
   and the defaults `= ""` / `= 0` do not exist in the source (the record fields are optional with no
   default). The result is non-compiling (required param after defaulted params) and could lead an
   LLM to emit `client->/Users(filter = "x")` instead of `client->/Users(queries = {filter: "x"})`.
   Affects all 10 methods with included-record params.
2. **`ConnectionConfig` closed record rendered as open.** Source `types.bal:201` is
   `public type ConnectionConfig record {|` … `|};`; render line 390 emits `record {`. The renderer
   does honour `record {|` elsewhere (10 occurrences in both files), so this is specific to the
   client-config type.
3. **Field default values dropped and turned into optional fields.** In `ConnectionConfig`, source
   defaults `httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`
   (`types.bal:203–238`) all render as `?` with no default (render lines 393–428). Eleven defaults
   lost.
4. **Multi-line doc comment loses its `#` prefix on continuation lines.** Render line 428 is a bare
   `and absent fields are handled as `nilable` types. Enabled by default.` with no leading `#`,
   sitting between two field declarations — invalid syntax. Present at old line 427 too.
5. **`public` / `isolated` modifiers dropped.** All 81 type defs render without `public`; the client
   renders as `client class Client` where the source (`client.bal:24`) is
   `public isolated client class Client`; resource methods lose `isolated`. Consistent renderer
   convention, applied identically on both sides.

## 6. Coverage gaps vs. the library

**None (0 gaps).**

- The bala has exactly one module: `modules/scim` — which is the default module
  (`package.json` `"export": ["scim"]`). There is no submodule API, so the shared
  `getDefaultModule()` limitation is inert here.
- Public types in the bala: 81 (`types.bal`). `typeDefs` in both JSONs: 81. Set difference in both
  directions is empty once the escaped identifiers `Enterprise\ User\ Extension` and
  `Enterprise\ User\ Extension_manager` are matched properly.
- Public client: 1 (`public isolated client class Client`, `client.bal:24`) with 17 resource
  functions + `init` → 18 entries in `clients[0].functions` on both sides; all 17 resource paths
  appear in both renders.
- Public module-level functions, constants, enums, annotations, listeners, services in the bala: 0
  (`grep -nE '^public (isolated )?(function|class|const|enum|annotation|listener)'` returns only the
  client class). The only `enum` in the package, `EncodingStyle` (`utils.bal:37`), is module-private
  and correctly absent. The six helper functions in `utils.bal` (lines 48, 74, 111, 151, 175, 189)
  are all non-public and correctly absent.

## 7. Compiler plugin

The package ships no compiler plugin. Verified on both sides:
`find` for `*compiler-plugin*` / `CompilerPlugin.toml` in the `v1.0.2` clone returns nothing, and the
bala contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/` directory. Nothing plugin-derived is therefore expected in, or missing from, the
render.

## 8. Other considerations

- **Not a pre-1.0 package.** `1.0.2`, `graalvmCompatible: true`, built with Ballerina `2201.12.0`,
  language spec `2024R1`. No deprecation markers in `package.json` or the source.
- **Auto-generated connector.** `types.bal`/`client.bal` carry the
  `// AUTO-GENERATED FILE. DO NOT MODIFY. … Ballerina OpenAPI tool` header, which explains the
  `*_body`, `*_inner`, `*Queries` naming and the awkward escaped identifiers.
- **Size/token impact is negligible**: +1 line (917 → 918), JSON shrinks 4369 → 4296 pretty-printed
  lines because the 10 pseudo-parameters are dropped. `new` is marginally cheaper *and* more accurate.
- **Doc quality is good**: 3524-char README preserved verbatim, per-field doc comments present
  throughout, and 17 `Special Agent Note` hints correctly attribute `http:*` types to
  `ballerina/http`.
- The README embeds four raw GitHub image URLs; harmless but they consume tokens without conveying
  information to an LLM. Same in both renders.

## 9. Evidence log

| # | Command / file:line | Result |
|---|---|---|
| 1 | `wc -l scim/{old,new}/ballerinax_scim.bal.txt` | 917 / 918 |
| 2 | `grep -c '^// Unknown type:'` on both | old 1, new 0 |
| 3 | `diff -u old new` (full output read) | 12 hunks, +20/−19 lines |
| 4 | `grep -cE 'ballerina[x]?/[a-z.]+:[0-9]'` on both | old 8 lines (16 occurrences), new 0 |
| 5 | `grep -c 'Additional Values'` on both | old 10, new 0 |
| 6 | `grep -cE '^type '` on both | old 80, new 81 |
| 7 | `grep -cE '^\s+resource function '` on both | 17 / 17 |
| 8 | `grep -c '@display'` on both | old 0, new 1 |
| 9 | `grep -c 'Special Agent Note'` on both | 17 / 17 |
| 10 | `grep -n '^// --- '` on new | lines 7, 101, 103, 845 (4 markers; same 4 in old) |
| 11 | `python3 -m json.tool --sort-keys` on both JSONs, then `diff -u` | 4369 → 4296 lines; 317 diff lines, all accounted for by items 4/5/8 and the `baseType` addition |
| 12 | JSON model counts | both: typeDefs 81, clients 1 (18 functions), functions 0, services 0, annotations 0; typeDef kinds Record 78 / Union 2 / Other 1 |
| 13 | typeDef name-set diff old vs new | identical (empty diff) |
| 14 | `ls -R` bala `1.0.2/any` | `bala.json`, `dependency-graph.json`, `docs/{README.md,icon.png}`, `modules/scim/{client,types,utils}.bal`, `package.json` — one module, no compiler plugin |
| 15 | `wc -l modules/scim/*.bal` | client 243, types 675, utils 219 |
| 16 | `git ls-remote --tags <repo>` | `v1.0.2` exists → `130b7fb895ddffa5dff30bfe9763630813db0540` |
| 17 | `git clone --depth 1 --branch v1.0.2`; `diff -q` bala vs `src/ballerina/{client,types,utils}.bal` | all three IDENTICAL |
| 18 | `src/ballerina/Ballerina.toml:5` | `version = "1.0.2"` — pin confirmed on the upstream side |
| 19 | `grep -c '^public type' types.bal` | 81 (matches typeDefs) |
| 20 | `grep -n 'OperationObBulk' types.bal` | 55 (`_inner` record), 405 (`OperationObBulk OperationObBulk_inner[]`), 424 (usage) — confirms new's alias |
| 21 | `types.bal:200-201` | `@display {label: "Connection Config"}` + `public type ConnectionConfig record {\|` |
| 22 | `types.bal` `GetUserQueries` / `GetGroupQueries` blocks | `int:Signed32 startIndex?;`, `int:Signed32 count?;`, open records (`};`) |
| 23 | `grep -n 'resource isolated function' client.bal` | 17 methods at lines 41,52,65,79,91,105,116,130,141,154,168,180,194,205,218,230,239; 10 use `*<X>Queries queries` |
| 24 | `client.bal:24` | `public isolated client class Client` |
| 25 | `grep -nE '^public (isolated )?(function\|class\|const\|enum\|annotation\|listener)' modules/scim/*.bal` | only the client class — no public functions/consts/enums |
| 26 | `utils.bal:37` | `enum EncodingStyle` — non-public, correctly absent from render |
| 27 | README equality check (`json['readme'].strip() == docs/README.md.strip()`) | `True`, 3524 chars both |
| 28 | `grep -c 'record {\|'` on both renders | 10 / 10 — closedness rendering unchanged |
| 29 | `grep -n 'Enterprise'` on new render | lines 191, 204, 205, 275, 671, 701 — escaped identifiers intact, match `types.bal:93,123,286,287,352` |
| 30 | `sed -n '389,430p'` new render vs `types.bal:199-238` | 11 field defaults dropped, closed record rendered open, doc continuation line at 428 missing `#` — identical at old lines 388–429 |
| 31 | `find src -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no matches |
| 32 | `OLD_AND_NEW_DIFFS/scim_diff.md` claims (917/918 lines, 12 hunks, 1 declaration added, 0 removed, 16→0 qualified refs, 1→0 unknown types) | all independently reproduced above; its "16" counts occurrences where my grep counted 8 lines — both correct, different units |

## 10. Caveats and unverified items

- The `Additional Values` pseudo-parameter's provenance (the implicit `anydata` rest field of the open
  `*Queries` records surfaced by the doc model) is an inference from the JSON payload
  (`"name": "Additional Values", "description": "Capture key value pairs", "type": "anydata"`,
  optional) combined with the fact that exactly the 10 methods with included open-record params carry
  it and no source parameter has that name. I did not read the extractor code to confirm the
  mechanism. The conclusion that dropping it loses no library information does not depend on the
  mechanism.
- Whether the renderer *should* emit `record {|` for `ConnectionConfig` (item 5.2) is judged from the
  source declaration alone; I did not trace why this type is treated differently from the 10 types
  that do render `record {|`. Either way it is identical in `old` and `new`.
- Ballerina Central metadata was not re-queried over HTTP; the package metadata used here comes from
  the bala's `package.json`, which is the artifact the extractor consumed. No deprecation flag is
  present there, but a Central-side deprecation would not appear in the bala — that specific field is
  unverified.
- The `examples/` and `ballerina/tests/` directories in the clone were not reviewed; they contain no
  public API and do not affect the render.

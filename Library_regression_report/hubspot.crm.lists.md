# ballerinax/hubspot.crm.lists 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.lists` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.lists |
| Tag reviewed | `v1.0.2` (commit `5117e62`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.lists/1.0.2` |
| Old render | `1860` lines (105,486 bytes) |
| New render | `1861` lines (94,747 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. The declaration set is byte-for-byte identical
in membership (125 type defs, 1 client class, 1 `init`, 25 remote functions on both sides — name sets
`diff` clean). Every one of the 36 diff hunks is one of four changes, all of them corrections:

1. 335 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.lists:1.0.2:PublicPropertyFilter`) collapsed to plain `int:Signed32` /
   bare type names → 0 qualified refs remain in `new`.
2. The malformed pseudo-parameter `anydata Additional Values` — an identifier containing a space,
   i.e. non-compiling Ballerina — removed from 10 remote-function signatures (10 → 0 occurrences).
3. `@display {label: "Connection Config"}` now emitted on `ConnectionConfig`, matching
   `types.bal:264` exactly. This is the sole net +1 line.
4. No other content change. README block (lines 7–198) is `diff`-identical; section markers are the
   same 4 on both sides; `Unknown type:` placeholders are 0 on both sides (this library has no
   error/object/other-tagged types, so the headline spec-v2 win does not apply here).

`new` is also 10.2% smaller in bytes (105,486 → 94,747) with zero information loss, which is a
direct token saving for the consuming LLM.

## 2. Change inventory

Computed from `diff -u old new` (36 hunks, 115 lines added, 114 removed):

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations | 125 | 125 | 0 |
| `client class` | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `remote function` | 25 | 25 | 0 |
| `enum` / `const` / `service` / `listener` / module-level `function` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Annotation lines (`^@`) | 0 | 1 | **+1** |
| Version/module-qualified type refs | 335 | 0 | **−335** |
| `anydata Additional Values` pseudo-params | 10 | 0 | **−10** |
| `// --- section ---` markers | 4 | 4 | 0 |
| `Special Agent Note` cross-package hints | 17 | 17 | 0 |
| Non-ASCII characters | 5 | 5 | 0 |

Declarations added: **0**. Declarations removed: **0**.
Name-set diffs (`type` names, `remote function` names) both returned empty.

Breakdown of the 115 added lines: 87 lines where only `ballerina/lang.int:0.0.0:Signed32` →
`int:Signed32`; 16 rewritten union `type` aliases (`Public*FilterBranchFilters` /
`Public*FilterBranchFilterBranches`) losing the `ballerinax/hubspot.crm.lists:1.0.2:` prefix on every
member; 10 rewritten `remote function` signatures (2 of which also carry an `int:Signed32` change);
1 `@display` line; 1 doc-comment line moved by diff alignment inside `PublicIndexOffset` (content
unchanged).

JSON side: both files have the same top-level keys and the same collection sizes
(`typeDefs` 125/125, `clients` 1/1, `functions` 0/0, `services` 0/0, top-level `annotations` 0/0).
The only structural JSON difference found is that the `new` `ConnectionConfig` typeDef gained an
`annotations` array (`[{"name":"display","value":"{label: \"Connection Config\"}"}]`); `old` has no
`annotations` key on any typeDef.

## 3. Correctness against library source

Upstream `v1.0.2` (`ballerina/client.bal`, `ballerina/types.bal`, `ballerina/utils.bal`) is
**byte-identical** to the bala's `modules/hubspot.crm.lists/*.bal` (`diff -q` reported no differences
for all three files), so GitHub and the bala do not disagree here.

Each `new`-side change verified against source:

- `int:Signed32` — `ballerina/types.bal` uses `int:Signed32` 87 times (e.g. `types.bal:1230`
  `int:Signed32 hour?;`). `new` renders exactly that spelling; `old`'s
  `ballerina/lang.int:0.0.0:Signed32` is not a valid type reference anywhere in Ballerina.
- Union aliases — `types.bal:965` `public type PublicOrFilterBranchFilters PublicPropertyFilter|…|PublicConstantFilter;`
  and `types.bal:526` `public type PublicOrFilterBranchFilterBranches PublicOrFilterBranch|…|PublicAssociationFilterBranch;`.
  The `new` render lines are character-for-character equal to the source lines minus the `public`
  keyword. All 16 rewritten aliases follow the same two shapes.
- `@display {label: "Connection Config"}` — `ballerina/types.bal:264`, immediately preceding
  `public type ConnectionConfig record {|` at line 265. Exact match.
- Removal of `anydata Additional Values` — no such parameter exists in any of the 25 remote
  functions in `client.bal`. The 10 affected methods all take an included-record param
  (`*XQueries queries`, e.g. `client.bal:345` `remote isolated function getGetAll(map<string|string[]> headers = {}, *GetGetAllQueries queries)`),
  whose `Queries` record is open; `old` materialised the implicit `anydata...` rest field as a
  parameter literally named `Additional Values`. Removing it is a correctness fix.

Coverage cross-check against source (exhaustive, not sampled):
- `grep -oE '^public type [A-Za-z0-9_]+' ballerina/types.bal` → 125 names; `diff` against the 125
  `^type` names in `new` → empty.
- `grep -oE 'remote isolated function [A-Za-z0-9_]+' ballerina/client.bal` → 25 names; `diff`
  against the 25 `remote function` names in `new` → empty.
- `client.bal:31` `public isolated function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v3/lists") returns error?`
  — present in `new` with matching parameter list, default and return type.
- `client.bal` and `utils.bal` declare 0 module-level `public function`s; `new` correctly has 0.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Full `diff -u` of the two renders was read in its entirety (651 lines); every removed line was
  classified and every removal has a corresponding, more accurate added line. There is no hunk that
  only deletes.
- `diff` of the sorted `type`-name sets and of the sorted `remote function`-name sets between `old`
  and `new`: both empty. Nothing was dropped.
- README block extracted by line range (7–198 on both files) and diffed: identical.
- Section markers, `Special Agent Note` cross-package hints (17 on both) and non-ASCII character
  counts (5 on both) unchanged — no doc text or encoding loss.
- No parameter, default value, or return type was removed by `new` other than the invalid
  `anydata Additional Values` token. Defaults present in `old` (`headers = {}`, `includeFilters = false`,
  `listIds = []`, `before = ""`, `limit = 0`, `after = ""`, `newFolderName = ""`, `listName = ""`,
  `legacyListId = ""`, `enrollObjectsInWorkflows = false`, `serviceUrl = "https://…"`) all survive
  verbatim in `new`.
- `new` contains zero `// Unknown type:` lines and zero qualified refs, so nothing degraded.

## 5. Issues in `new` (independent of `old`)

All five items below are **also present in `old`** — they are pre-existing renderer behaviours, not
introduced by spec v2 — but they remain wrong in `new` and would mislead an LLM consuming the render.

1. **Included-record query params are both flattened and duplicated, and lose the `*`.** Source:
   `client.bal:345` `getGetAll(map<string|string[]> headers = {}, *GetGetAllQueries queries)`.
   Render (`new` line 1832-region): `getGetAll(map<string|string[]> headers = {}, string[] listIds = [], boolean includeFilters = false, GetGetAllQueries queries)`.
   The record's fields are inlined *and* a non-included `queries` param is appended. Affects 10 of 25
   methods (`grep -cE '^    remote function .*Queries queries\)'` → 10). The result does not compile:
   a required param (`queries`) follows defaultable params, and the same values are expressible twice.
2. **Optional record fields become defaulted params with fabricated defaults.**
   `types.bal:1222` `string[] listIds?;` (optional, no default) renders as `string[] listIds = []`;
   `types.bal:684` `string before?;` renders as `string before = ""`. The render asserts defaults the
   library does not define.
3. **A real default value is replaced with a wrong one, and the identifier escape is dropped.**
   `types.bal:686` `int:Signed32 'limit = 100;` renders as `int:Signed32 limit = 0` in both
   `getListIdMembershipsGetPage` (`new` line 1852) and
   `getListIdMembershipsJoinOrderGetPageOrderedByAddedToListDate`. Both the value (100 → 0) and the
   quoted-identifier form (`'limit`) are wrong. Note the render *does* keep `'limit?` correctly in
   the two `*Queries` type definitions (2 occurrences of `'limit` in both files), so the corruption
   is specific to the parameter-flattening path.
4. **Top-level closed records are rendered as open.** Source has 5 `record {|` occurrences
   (`types.bal:238, 265, 483, 1289, 1367`); both renders have 2. `ConnectionConfig` (`new` line 1440),
   `ApiKeysConfig` and `OAuth2RefreshTokenGrantConfig` are emitted as `record {` — an LLM would
   believe arbitrary extra fields are permitted. Inline anonymous closed records
   (`record {|string...;|}`) are preserved correctly.
5. **Qualifiers stripped from the client class and `init`.** Source `client.bal:23`
   `public isolated client class Client` and `client.bal:31` `public isolated function init(...)`
   render as `client class Client` / `function init(...)` (`new` lines 1759–1760). Isolation and
   visibility information is lost.

## 6. Coverage gaps vs. the library

**None.** `package.json` declares a single export, `"export": ["hubspot.crm.lists"]`, and
`modules/` in the bala contains exactly one directory (`hubspot.crm.lists`), which is the default
module. There is therefore no submodule-only API and no shared submodule gap for this library.

All 125 public types, the client class, `init`, and all 25 remote methods from that module appear in
both renders (set diffs in §3 returned empty). No public symbol from the default module is absent
from either render.

## 7. Compiler plugin

The package ships **no compiler plugin**: the bala root contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/` directory and no `compiler-plugin.json`. The upstream repo at `v1.0.2` likewise
has no `*compiler-plugin*` directory (glob matched nothing). Nothing plugin-derived is expected in
the render, and nothing is missing on that account.

## 8. Other considerations

- **Version status**: 1.0.2 is a stable, non-deprecated release. `package.json` reports
  `ballerina_version: 2201.12.2`, `language_spec_version: 2024R1`, `graalvmCompatible: true`,
  `template: false`. Keywords: `lists`, `Vendor/HubSpot`, `Area/CRM & Sales`, `Type/Connector`.
- **Size / token impact**: `new` is 10,739 bytes smaller (105,486 → 94,747, −10.2%) while carrying
  strictly more information (the `@display` annotation). The JSON also shrinks 330,637 → 317,923
  bytes (−3.8%). Removing the 335 `ballerinax/hubspot.crm.lists:1.0.2:` / `ballerina/lang.int:0.0.0:`
  prefixes accounts for nearly all of it.
- **Compilability of the render**: `new` is closer to compiling than `old` (the `Additional Values`
  identifier-with-a-space is gone) but still not compilable, because of §5 items 1–3. This is a
  renderer-wide concern, not a regression.
- **Docs quality**: doc comments are dense and per-field throughout; multi-line docs with blank
  lines inside them (e.g. the paging-offset descriptions around `new` lines 1595, 1641) are rendered
  without the leading `#` on the continuation line, in both renders — cosmetically odd but
  unchanged between sides.
- **API naming**: the generated method names are verbose and path-derived
  (`getObjectTypeIdObjectTypeIdNameListNameGetByName`); this comes from the OpenAPI generator in the
  library itself, not from the renderer.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 1860, new 1861 |
| `wc -c` on both renders | old 105,486, new 94,747 |
| `wc -c` on both JSONs | old 330,637, new 317,923 |
| `diff -u old new \| grep -c '^@@'` | 36 hunks |
| `diff -u ... \| grep -c '^+[^+]'` / `'^-[^-]'` | 115 added / 114 removed |
| `grep -c '^type ' old new` | 125 / 125 |
| `grep -cE '^    remote function' old new` | 25 / 25 |
| `grep -cE '^client class' old new` / `'^    function init'` | 1 / 1 each |
| `grep -c '^// Unknown type:' old new` | 0 / 0 |
| `grep -c '^@' old new` | 0 / 1 |
| `grep -oE '[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` | old 335, new 0 |
| `grep -c 'Additional Values' old new` | old 10, new 0 |
| `grep -c 'Special Agent Note' old new` | 17 / 17 |
| `grep -c -P '[^\x00-\x7F]' old new` | 5 / 5 |
| `grep -n '^// --- ' old new` | old: 7,198,200,1756; new: 7,198,200,1757 |
| `diff <(sed -n '7,198p' old) <(sed -n '7,198p' new)` | empty — README identical |
| `diff` of sorted `^type <name>` sets | empty |
| `diff` of sorted `remote function <name>` sets | empty |
| `git ls-remote --tags <repo>` | tags v0.1.0, v1.0.0, v1.0.1, **v1.0.2** |
| `git clone --depth 1 --branch v1.0.2` → `git log --oneline -1` | `5117e62 [Gradle Release Plugin] - pre tag commit: 'v1.0.2'` |
| `git describe --tags` in clone | `v1.0.2` |
| `grep -n version ballerina/Ballerina.toml` | `version = "1.0.2"` |
| `diff -q` bala `client.bal`/`types.bal`/`utils.bal` vs upstream `ballerina/*.bal` | identical (all 3) |
| `wc -l` bala module sources | client.bal 474, types.bal 1458, utils.bal 219 |
| `grep -cE '^public (type\|function\|class\|const\|enum\|isolated function)' types.bal` | 125 |
| `grep -cE 'remote isolated function' client.bal` | 25 |
| `diff` bala `public type` names vs new render `type` names | empty — full coverage |
| `diff` bala remote-fn names vs new render remote-fn names | empty — full coverage |
| `grep -n '@display' bala/*.bal` | `types.bal:264 @display {label: "Connection Config"}` (only occurrence) |
| `types.bal:265` | `public type ConnectionConfig record {\|` |
| `types.bal:965` vs `new` `type PublicOrFilterBranchFilters …` | identical modulo `public` |
| `types.bal:526` vs `new` `type PublicOrFilterBranchFilterBranches …` | identical modulo `public` |
| `types.bal:686` | `int:Signed32 'limit = 100;` vs render `int:Signed32 limit = 0` |
| `types.bal:1220–1225` (`GetGetAllQueries`) | `listIds?` optional; render says `listIds = []` |
| `grep -c 'record {\|' ` source / old / new | 5 / 2 / 2 |
| `grep -cE '^    remote function .*Queries queries\)' new` | 10 |
| `client.bal:23`, `client.bal:31` | `public isolated client class Client`, `public isolated function init(...)` |
| `ls` bala root | no `compiler-plugin/`; only bala.json, dependency-graph.json, docs, modules, package.json |
| `ls src/*compiler-plugin*` in clone | no matches |
| `cat package.json` | `"export": ["hubspot.crm.lists"]`, single module, `ballerina_version 2201.12.2` |
| JSON key/collection comparison (python) | same keys; typeDefs 125/125, clients 1/1, functions 0/0, services 0/0, annotations 0/0 |
| JSON `ConnectionConfig` annotations (python) | new: `[{"name":"display","value":"{label: \"Connection Config\"}"}]`; old: absent |

## 10. Caveats and unverified items

- Neither render was fed to the Ballerina compiler; the "does not compile" statements in §5 are based
  on reading the syntax against the language rules (identifier containing a space; required
  parameter following defaultable parameters; missing `*` on an included-record parameter), not on a
  compiler run.
- Ballerina Central's registry API was not re-queried; package metadata (version, export list,
  keywords, deprecation status) was taken from the bala's `package.json`, which is the artefact the
  extractor actually consumed. Deprecation status is therefore inferred from the absence of any
  deprecation marker in `package.json` rather than confirmed against Central.
- The claim that the two renders were produced from the two `ballerina-vscode` commits named in the
  brief was taken from the brief; it was not independently re-derived, as the render generation was
  not re-run here.
- §5 items are stated as pre-existing because they were confirmed present in `old` as well; no
  attempt was made to trace them to specific renderer code in either `ballerina-vscode` revision.

# ballerinax/hubspot.crm.engagements.tasks 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.engagements.tasks` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.engagements.tasks |
| Tag reviewed | `v2.0.2` (exact match, commit `1ddfc0ef`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.engagements.tasks/2.0.2` |
| Old render | `790` lines |
| New render | `791` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. The JSON models were diffed field-by-field and **every** difference
between `old` and `new` falls into exactly three buckets, all corrections:

1. 11 version/module-qualified type references normalised (`ballerina/lang.int:0.0.0:Signed32` →
   `int:Signed32`, `ballerinax/hubspot.crm.engagements.tasks:2.0.2:X` → `X`) — 11 in `old`, 0 in `new`.
2. `@display {label: "Connection Config"}` on `ConnectionConfig` now captured (present in source
   `ballerina/types.bal:254`, absent from `old`).
3. 4 spurious `anydata Additional Values` parameters removed from client resource methods — an
   artifact of flattening the *implicit rest field* of an included open record, which rendered as a
   syntactically invalid identifier (space in name).

Nothing was removed, truncated, or made less accurate. Declaration sets are identical: 41 types and
1 client with 12 functions on both sides. README is byte-identical to the bala's `docs/README.md`.

## 2. Change inventory

| Kind | old | new | Δ |
|---|---|---|---|
| `type` declarations | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| Client functions (incl. `init`) | 12 | 12 | 0 |
| `resource function` lines | 11 | 11 | 0 |
| Free functions / services / annotations (JSON arrays) | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| Section markers `// --- ` | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs | 11 | 0 | −11 |
| `@display` annotations rendered | 0 | 1 | +1 |
| `anydata Additional Values` params | 4 | 0 | −4 |
| Total lines | 790 | 791 | +1 |

Declarations added: **0**. Declarations removed: **0**
(`diff` of sorted `^type <Name>` sets is empty).

Raw text diff: 31 changed lines across 15 hunks (16 added, 15 removed).

Field-level JSON diff (exhaustive, every differing leaf listed):

| Type | Field | old | new |
|---|---|---|---|
| `GetCrmV3ObjectsTasksGetPageQueries` | `'limit` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `AssociationSpec` | `associationTypeId` | same | `int:Signed32` |
| `ValueWithTimestamp` | `updatedByUserId` | same | `int:Signed32` |
| `BatchResponseSimplePublicUpsertObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `BatchResponseSimplePublicObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `CollectionResponseWithTotalSimplePublicObjectForwardPaging` | `total` | same | `int:Signed32` |
| `PublicObjectSearchRequest` | `'limit` | same | `int:Signed32` |
| `SimplePublicObject` | `propertiesWithHistory` | `record {\|ballerinax/…:2.0.2:ValueWithTimestamp[]...;\|}` | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicUpsertObject` | `propertiesWithHistory` | same | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `propertiesWithHistory` | same | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `associations` | `record {\|ballerinax/…:2.0.2:CollectionResponseAssociatedId...;\|}` | `record {\|CollectionResponseAssociatedId...;\|}` |
| `ConnectionConfig` | `annotations[0]` | absent | `display` = `{label: "Connection Config"}` |

Client-method parameter changes (4 methods, `Additional Values` dropped):
`post batch/read`, `get [string taskId]`, `patch [string taskId]`, `get .`.

## 3. Correctness against library source

Bala and GitHub `v2.0.2` sources are **byte-identical** (`diff -q` clean for `client.bal`,
`types.bal`, `utils.bal`), so both agree.

- All 7 `int:Signed32` fixes are correct: source `ballerina/types.bal` lines 65, 133, 199, 228, 316,
  350, 386 all declare `int:Signed32`. `new` matches; `old` did not.
- All 4 record-rest-type fixes are correct: source `types.bal:244, 392, 400, 454` declare
  `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}` with bare
  local names. `new` matches; `old` prefixed them with `ballerinax/…:2.0.2:`.
- `@display {label: "Connection Config"}` is genuine — `types.bal:254`, immediately above
  `public type ConnectionConfig record {|`. Not invented.
- `Additional Values` has **no** counterpart in the source. All four Queries records
  (`PatchCrmV3ObjectsTasksTaskIdUpdateQueries:43`, `GetCrmV3ObjectsTasksGetPageQueries:57`,
  `GetCrmV3ObjectsTasksTaskIdGetByIdQueries:161`, `PostCrmV3ObjectsTasksBatchReadReadQueries:340`)
  are open records; `old` materialised their implicit `anydata...` rest field as a parameter literally
  named `Additional Values` (description "Capture key value pairs"). Removing it is correct.
- Type name set: `grep '^public type' bala/types.bal` (41 names) vs `grep '^type' new render`
  (41 names) — `diff` empty. Full parity.
- Client surface: source `client.bal` has `public isolated function init` (line 31) plus 11
  `resource isolated function` (lines 47, 67, 84, 100, 118, 135, 152, 170, 186, 203, 220). The render
  emits exactly those 12, with matching accessors, resource paths, payload types and return unions.

## 4. Regressions

**None found.**

Checked to conclude this:
- Sorted declaration-name sets in the two renders are identical (no drops).
- Every differing JSON leaf between the two models was enumerated programmatically (table in §2);
  all 13 leaf differences are corrections, none is a loss.
- README section: `json['readme']` is identical on both sides (8,625 chars) and identical to
  `bala/any/docs/README.md`.
- Doc comments: no doc string differs between the two models (they would have appeared in the leaf
  diff; none did).
- Return types, defaults, parameter order for the 12 client functions: identical except the removed
  `Additional Values` entries.
- Section markers, `// Unknown type:` count (0 → 0), and `// Special Agent Note:` cross-package
  annotations are unchanged.

The only information technically "lost" is the signal that the Queries records are open (implicit
`anydata` rest field). That signal was already absent from the type definitions on both sides, and in
`old` it was expressed only as an invalid, misleading parameter — so this is a net gain, not a loss.

## 5. Issues in `new` (independent of `old`)

All six below are **pre-existing** — byte-for-byte present in `old` too — so none is a regression, but
they are real inaccuracies a consumer of the render would hit.

1. **Included-record params are both flattened and duplicated.** Source:
   `resource isolated function get [string taskId](map<string|string[]> headers = {}, *GetCrmV3ObjectsTasksTaskIdGetByIdQueries queries)`.
   Render: the record's fields are inlined *and* a further required positional
   `GetCrmV3ObjectsTasksTaskIdGetByIdQueries queries` is appended, with the `*` inclusion sigil lost.
   Contradictory and non-compiling. Affects all 4 methods that take a `*…Queries` param.
2. **Wrong default for `limit`.** Render line 781: `int:Signed32 limit = 0`. Source `types.bal:65`
   declares `int:Signed32 'limit = 10`.
3. **Invented defaults on flattened optional fields.** e.g. `string[] associations = []`,
   `string idProperty = ""`, `string[] properties = []` — the source fields are optional (`?`) with no
   default at all.
4. **Record field defaults dropped in type definitions.** `boolean archived = false` →
   `boolean archived?`; `'limit = 10` → `'limit?`; every `ConnectionConfig` default
   (`httpVersion = http:HTTP_2_0`, `timeout = 30`, `forwarded = "disable"`, `validation = true`,
   `laxDataBinding = true`, …) is rendered as a plain optional field.
5. **Closed record rendered as open.** Source `ConnectionConfig` is `record {| … |}`; render emits
   `record { … }`.
6. **Broken multi-line doc comment.** Render lines 609–610: the continuation of
   `laxDataBinding`'s doc loses its `#` prefix, producing the bare non-comment line
   `and absent fields are handled as `nilable` types. Enabled by default`, which breaks the render as
   Ballerina text.

Also shared and minor: `public` / `isolated` qualifiers are dropped from the client class and its
methods, and `resource isolated function get .` renders as `resource function get (` with no `.`.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala exports a single module (`package.json` → `"export": ["hubspot.crm.engagements.tasks"]`),
which is the default module, so the `getDefaultModule()` limitation is not in play here.

- 41 `public type` in `bala/modules/…/types.bal` → all 41 in both renders (name-set `diff` empty).
- 1 `public isolated client class Client` (`client.bal:23`) → present, all 12 members rendered.
- `utils.bal` contains only module-private symbols (`isolated function getDeepObjectStyleRequest`,
  `getFormStyleRequest`, `getSerializedArray`, `getSerializedRecordArray`, `getEncodedUri`,
  `getPathForQueryParam`, `type Encoding`, `enum EncodingStyle` — none marked `public`), correctly
  excluded.
- No public constants, enums, annotations, listeners, services or free functions exist in the package;
  the JSON's `functions`/`services`/`annotations` arrays are empty on both sides, correctly.

## 7. Compiler plugin

The package ships **no compiler plugin**: no `compiler-plugin/` or `*-compiler-plugin*` directory in
the `v2.0.2` tree, and no `compiler-plugin/compiler-plugin.json` in the bala (bala `any/` contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived is
therefore expected in, or missing from, the render.

## 8. Other considerations

- Version 2.0.2 is a stable major; `package.json` reports `graalvmCompatible: true`,
  `ballerina_version: 2201.12.2`. No deprecation markers in source or bala.
- Size is modest (791 lines); ~197 of them are the README block, which is reproduced verbatim.
- Auth surface (`ApiKeysConfig` with `privateAppLegacy` / `privateApp`, plus
  `OAuth2RefreshTokenGrantConfig` and `http:BearerTokenConfig`) is rendered on both sides — useful for
  an LLM generating connector init code, and `new`'s `@display` label adds the low-code label the
  source declares.
- Neither render is compilable Ballerina (see §5 items 1, 5, 6), but `new` is strictly closer: it
  removes the two most obviously invalid constructs (`ballerina/lang.int:0.0.0:Signed32` and the
  space-containing identifier `Additional Values`).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | 790 / 791 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; `Client` at 742 (old) / 743 (new) |
| `grep -cE '(ballerina\|ballerinax)/[a-z.]+:[0-9.]+:'` both | 11 / 0 |
| `grep -oE '…:[0-9.]+:[A-Za-z0-9_]+' old \| uniq -c` | 7× `lang.int:0.0.0:Signed32`, 3× `…:2.0.2:ValueWithTimestamp`, 1× `…:2.0.2:CollectionResponseAssociatedId` |
| `grep -c '@display'` both | 0 / 1 |
| `grep -c 'Additional Values'` (json, render) | old 4 / 4, new 0 / 0 |
| `diff` of sorted `^type <Name>` sets | empty (identical 41-name sets) |
| `diff old new \| grep -c '^[<>]'` | 31 |
| JSON top-level counts both sides | typeDefs 41, clients 1, functions 0, services 0, annotations 0; client funcs 12 |
| Exhaustive leaf-level JSON diff (python, flatten+compare) | 13 differing leaves, all listed in §2; no other differences |
| `o['readme'] == n['readme']` and vs bala README | True / True (8,625 chars) |
| `git ls-remote --tags <repo>` | `v2.0.2` → `1ddfc0ef820ff328eb3f2c8b5c0ca58859c2b533` |
| `git clone --depth 1 --branch v2.0.2` | succeeded |
| `diff -q bala/modules/…/{client,types,utils}.bal src/ballerina/…` | all identical |
| `grep -n 'int:Signed32' src/ballerina/types.bal` | 7 hits: 65, 133, 199, 228, 316, 350, 386 |
| `grep -n 'ValueWithTimestamp\[\]\.\.\.\|CollectionResponseAssociatedId\.\.\.'` | 4 hits: 244, 392, 400, 454 |
| `grep -n '@display' src/ballerina/types.bal` | line 254, above `public type ConnectionConfig record {\|` (255) |
| `grep -c '^public type' src/ballerina/types.bal` | 41 |
| `grep -n 'resource isolated function\|init' src/ballerina/client.bal` | init:31 + 11 resources (47,67,84,100,118,135,152,170,186,203,220) |
| `grep -n '^public' src/ballerina/utils.bal` | no hits (all private) |
| `find src -iname '*compiler-plugin*'` | no hits |
| bala `package.json` `export` | `["hubspot.crm.engagements.tasks"]` (single, default module) |
| `sed -n '606,612p' new render` | confirms bare continuation line at 610 (also at 609 in old) |

## 10. Caveats and unverified items

- Neither render was fed to `bal build`, so "non-compiling" claims in §5 are from reading the emitted
  text (space in identifier, missing `#` on a doc continuation line, duplicated included-record
  parameter), not from a compiler run.
- The renderer/extractor source itself (`ballerina-vscode` on either side) was not read; the
  attribution of each delta to "spec v2 behaviour" is inferred from the observed data, which is
  nonetheless fully consistent with the brief's stated known behaviours.
- `int:Signed32` still relies on an implicit `ballerina/lang.int` import that the render never emits;
  whether the consuming prompt supplies that context is out of scope here.

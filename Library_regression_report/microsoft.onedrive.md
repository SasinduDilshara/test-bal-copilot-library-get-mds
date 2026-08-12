# ballerinax/microsoft.onedrive 3.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/microsoft.onedrive` |
| Pinned version | `3.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-microsoft.onedrive |
| Tag reviewed | `v3.0.2` (commit `46690e97cde371e0d705843afc08c5099a5459fa`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/microsoft.onedrive/3.0.2` |
| Old render | `10879` lines |
| New render | `11055` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Both renders come from the same library artifact; upstream `v3.0.2` is byte-identical to the bala
(`diff` on `types.bal`, `client.bal`, `utils.bal` → IDENTICAL). The diff is +225 / −49 lines across
123 hunks, and every one of the 49 removed lines is replaced by a strictly more accurate line.

`new` adds four classes of information that `old` dropped entirely, all verified against the bala
source with exact count parity:

* 46 `@constraint:String`, 18 `@constraint:Number`, 102 `@http:Query`, 9 `@http:Header` annotations
  (source has exactly 46 / 18 / 102 / 9). `old` had **0** of each.
* 1 `@display {label: "Connection Config"}` on `ConnectionConfig` (source `types.bal:6184`).
* The previously degraded `// Unknown type: AssignedLicenseDisabledPlansItemsString` is now a real
  definition matching `types.bal:2582-2583`.
* 24 record fields whose names are Ballerina keywords are now correctly quoted (`'type`, `'from`,
  `'error`, `'resource`, `'order`, `'start`, `'source`, `'boolean`) in type-inclusion-flattened
  copies, where `old` emitted them bare and therefore non-compiling.

`new` also removes a fabricated parameter: `old` emitted `anydata Additional Values` (an invalid
identifier — it contains a space) in 24 client method signatures, derived from the open-record rest
descriptor of the `*Queries` included-record params. `new` drops it. 24 occurrences → 0.

No declaration, parameter, doc string, default value, return type or README byte was lost. **No
regressions found.**

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 10879 | 11055 |
| File size | 450,495 B | 462,934 B |
| Section markers (`// --- `) | 4 | 4 |
| `type` declarations | 895 | 896 |
| Client classes | 1 | 1 |
| `remote function` declarations | 78 | 78 |
| `enum` declarations | 0 | 0 |
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |
| `@constraint:String` | 0 | 46 |
| `@constraint:Number` | 0 | 18 |
| `@http:Query` | 0 | 102 |
| `@http:Header` | 0 | 9 |
| `@display` | 0 | 1 |
| `anydata Additional Values` params | 24 | 0 |
| Quoted keyword field names (total occurrences) | 61 | 85 |
| `// Special Agent Note:` cross-package hints | 17 | 17 |
| README bytes (JSON `readme`) | 6827 | 6827 (identical) |

### Declarations added (1)

| Kind | Name | Evidence |
|---|---|---|
| type (string subtype) | `AssignedLicenseDisabledPlansItemsString` | `types.bal:2582-2583`; was `// Unknown type:` in old |

### Declarations removed (0)

None. Set comparison of `^type <Name>` in both renders vs the 896 `^public type` names in
`modules/microsoft.onedrive/types.bal`:

* `comm -23 src_types new_types` → empty (no source type missing from `new`)
* `comm -13 src_types new_types` → empty (no invented type in `new`)
* `comm -23 old_types new_types` → empty (nothing dropped from `old`)

Client method names: `comm` both ways between the 78 `remote isolated function` names in
`client.bal` and the 78 `remote function` names in `new` → both empty.

### Declarations modified (49 lines)

| Change | Count | Nature |
|---|---|---|
| Client method signature: `anydata Additional Values,` removed | 24 | improvement (invalid identifier removed) |
| Record field: bare keyword → quoted keyword | 24 | improvement (matches source, now compiles) |
| `// Unknown type:` → real type def | 1 | improvement |

### Added lines accounted for (225)

175 annotation lines + 1 `type AssignedLicenseDisabledPlansItemsString string;` + 1 `@display`
+ 24 rewritten client signatures + 24 rewritten field lines = 225. ✔

## 3. Correctness against library source

Upstream `v3.0.2` == bala, so both are cited interchangeably.

| Item in `new` | Source evidence | Match |
|---|---|---|
| `@constraint:String {pattern: re \`…uuid…\`}` + `type AssignedLicenseDisabledPlansItemsString string;` | `types.bal:2582-2583` | exact, incl. regex literal |
| `@constraint:Number {minValue: -2147483648, maxValue: 2147483647}` on `OpenShiftItem1.openSlotCount` | `types.bal:7256-7257` | exact |
| Three `@constraint:Number` on `RecurrencePattern.dayOfMonth/interval/month` | `types.bal:4916, 4923, 4926` | exact |
| `@http:Query {name: "$skip"}` … `{name: "$select"}` on `ListDriveQueries` | `types.bal:7346-7352 ff.` | exact |
| `@http:Header {name: "If-Match"}` on `DeleteItemHeaders.ifMatch` | `types.bal:2356-2357` | exact |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:6184` | exact |
| Annotation totals 46/18/102/9 | `grep -c` on `types.bal` → 46/18/102/9 | exact parity |
| All 24 newly quoted field lines | each grepped verbatim in `types.bal` (e.g. `DateTimeTimeZone 'start?;` @600, `ContentTypeOrder 'order?;` @1866, `Thumbnail 'source?;` @2724, `BooleanColumn 'boolean?;` @5262, `Recipient 'from?;` @5485, `Entity 'resource?;` @6392, `AttendeeType 'type?;` @6555) | all present ≥1× |
| 78 client method names | `client.bal` `remote isolated function` set | exact |
| `init(ConnectionConfig config, string serviceUrl = "https://graph.microsoft.com/v1.0/")` | `client.bal:30` | params + default match |
| `search(string driveId, string driveItemId, string\|() q, …)` | `client.bal:497` (`string? q`) | semantically equal |
| Client method docs | JSON: 0 of 79 client-function descriptions differ old↔new | preserved |

Nothing in `new` is invented: the "in new not in src" set comparison is empty for both types and
client methods.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. Full `diff -u old new` (1370 lines) read in its entirety; all 49 removed lines enumerated with
   `grep '^-[^-]' | sort | uniq -c` — 24 client signatures, 24 field lines, 1 `// Unknown type:`,
   each with a corresponding improved `+` line.
2. Type-name set difference `old \ new` → empty.
3. Client method name set difference (old JSON vs new JSON) → empty; both have 79 client functions
   (78 remote + `init`).
4. Per-function parameter-name lists compared old vs new in JSON: 24 functions differ, and in every
   case the sole difference is deletion of the bogus `Additional Values` parameter. Total parameter
   count 388 → 364 = exactly −24.
5. Per-function description comparison old vs new: 0 differences.
6. README (`readme` field) and package `description` in the two JSONs are byte-identical
   (`old['readme'] == new['readme']` → True).
7. Section markers unchanged (4 → 4, README/Types/Client boundaries intact).
8. JSON schema paths: `new` has only additive paths (`typeDefs[].fields[].annotations{name,module,value}`);
   the "old-only paths" set is empty.

## 5. Issues in `new` (independent of `old`)

All of the following are **shared with `old`** (i.e. pre-existing renderer behaviour), except (6)
and (8) which are new-side nits introduced by the annotation feature. None is a regression.

1. **Included-record parameters lose `*` and become ill-formed.** Source:
   `remote isolated function listDrive(map<string|string[]> headers = {}, *ListDriveQueries queries)`
   (`client.bal:45`). Render: `remote function listDrive(map<…> headers = {}, int skip = 0, …,
   string[] select = [], ListDriveQueries queries)`. A required parameter after defaultable
   parameters does not compile, and the `*`-include semantics are lost. 24 occurrences in both
   renders (`grep -c 'Queries queries) returns'` → 24 / 24).
2. **Query parameters are duplicated.** The same 7–9 query fields appear both flattened
   (`int skip = 0, …`) and again inside the trailing `XQueries queries` parameter, in both renders.
   An LLM could plausibly pass both.
3. **`select` is emitted unquoted as a parameter name** (`string[] select = []`, 16 occurrences in
   both renders) while the corresponding record field is correctly `'select`. `select` is a
   Ballerina keyword, so the parameter form would not compile.
4. **Closed records rendered as open.** `types.bal` has 2 `record {|…|}` (`OAuth2RefreshTokenGrantConfig`
   @884, `ConnectionConfig` @6185); both renders emit `record {` (0 occurrences of `record {|` in
   either render).
5. **Record field default values dropped.** `ConnectionConfig` has 11 defaulted fields in source
   (`httpVersion = http:HTTP_2_0`, `timeout = 30`, `forwarded = "disable"`, `cache = {}`,
   `compression = http:COMPRESSION_AUTO`, `responseLimits = {}`, `socketConfig = {}`,
   `validation = true`, `laxDataBinding = true`, `http1Settings = {}`, `http2Settings = {}`); both
   renders emit them as plain optional (`http:HttpVersion httpVersion?;`).
6. **Annotations and docs are not propagated into type-inclusion-flattened copies.** `new` renders
   `WorkbookTableColumn1.index` with its `@constraint:Number` and doc (line 9832-9834) but
   `WorkbookTableColumn` — which is `*Entity; *WorkbookTableColumn1;` in source (`types.bal:4296-4299`)
   — flattens to bare `decimal index?;` (line 9882) with neither doc nor annotation. `old` lost the
   docs the same way; the annotation half of this is new-side, and it makes annotation coverage
   record-dependent rather than wrong.
7. **`isolated` / `public` qualifiers dropped.** Source has `public isolated client class Client`,
   `public isolated function init`, `remote isolated function …`; both renders emit
   `client class Client`, `function init`, `remote function …` (0 occurrences of
   `remote isolated function` in either render).
8. **No import lines for the annotation modules.** The render's only imports are
   `import ballerinax/microsoft.onedrive;` (lines 5 and 124). `new` now emits `constraint:` and (as
   before) `http:` prefixes with no `import ballerina/constraint;` / `import ballerina/http;`. The
   render carries 17 `// Special Agent Note: … FROM ballerina/http package` hints for types but none
   for the annotation modules.

## 6. Coverage gaps vs. the library

**0 gaps.**

* The bala exports exactly one module (`package.json` → `"export": ["microsoft.onedrive"]`,
  `modules/` contains only `microsoft.onedrive`), so the known `getDefaultModule()`-only limitation
  costs nothing here.
* All 896 `public type` names from `types.bal` appear in `new` (set difference both directions is
  empty). `old` was missing 1 (`AssignedLicenseDisabledPlansItemsString` was present in the JSON as
  `{"type":"Other"}` but rendered as a `// Unknown type:` comment).
* All 78 public remote methods plus `init` appear in both renders.
* There are no `public const`, `public enum`, `public annotation`, `public listener` or
  module-level `public function` declarations in the module
  (`grep -E '^public (const|enum|class|function|isolated function|annotation|listener)'` over
  `*.bal` → no matches other than the client class).

## 7. Compiler plugin

The package ships **no compiler plugin**: no `compiler-plugin/` directory in the bala (`ls` of
`.../3.0.2/any` → `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`), and no
`*compiler-plugin*` directory anywhere in the upstream `v3.0.2` tree. Nothing plugin-implied is
therefore missing from the render.

## 8. Other considerations

* **Not deprecated.** Ballerina Central `2.0/registry/packages/ballerinax/microsoft.onedrive/3.0.2`
  → `"deprecated": null`, `"deprecateMessage": ""`, `"visibility": "public"`, `"pullCount": 94`,
  `"ballerinaVersion": "2201.12.0"`.
* **Stable major version** (3.0.2), single exported module, keywords include
  `Type/Connector`, `Vendor/Microsoft`.
* **Size/token impact:** `new` is +176 lines / +12,439 bytes on the render (+1.6 %) and +34,166
  bytes on the JSON (+1.8 %). Small cost for the validation metadata; the removal of the 24
  `anydata Additional Values` fragments partially offsets it.
* **Practical value of the new annotations:** the `@http:Query {name: "$select"}` mappings are the
  only place the render tells a consumer that the Ballerina field `'select` maps to the OData
  `$select` query parameter. Without them (as in `old`) generated code would send `select=` and
  fail against Microsoft Graph. This is the single largest accuracy gain here.
* This is a large, mostly generated Graph-model surface (896 types, 8079-line `types.bal`); doc
  comments are Microsoft-sourced and of good quality, and are preserved verbatim in both renders.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags <repo>` | `v3.0.2` → `f6dc5bf`, peeled `46690e9` |
| 2 | `git clone --depth 1 --branch v3.0.2 … src` | success |
| 3 | `diff -q src/ballerina/{types,client,utils}.bal bala/modules/microsoft.onedrive/` | all IDENTICAL |
| 4 | `wc -l old new` | 10879 / 11055 |
| 5 | `grep -n '^// --- ' old new` | 4 markers each, README@7/164, Types@166, Client@10563(old)/10739(new) |
| 6 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 7 | `diff -u old new > render.diff; wc -l` | 1370 lines; `grep -c '^-[^-]'` 49; `grep -c '^+[^+]'` 225 |
| 8 | `grep '^-[^-]' render.diff \| sort \| uniq -c` | 24 client sigs, 24 field lines, 1 unknown-type line |
| 9 | `grep '^+[^+]' render.diff` bucketed | 175 annotations + 1 type + 1 `@display` + 24 sigs + 24 fields = 225 |
| 10 | `grep -c '@constraint:String\|@constraint:Number\|@http:Query\|@http:Header'` old / new / `types.bal` | 0,0,0,0 / 46,18,102,9 / 46,18,102,9 |
| 11 | `grep -c 'anydata Additional Values'` old / new | 24 / 0 |
| 12 | `grep -c '^type '` old / new; `grep -c '^public type' types.bal` | 895 / 896 / 896 |
| 13 | `comm` on type-name sets (src vs new, src vs new reverse, old vs new) | all three empty |
| 14 | `comm` on client-method-name sets (client.bal vs new, both directions) | both empty; 78 each |
| 15 | JSON: `len(typeDefs)` old/new | 896 / 896 |
| 16 | JSON: recursive key-path sets | new-only: `typeDefs[].fields[].annotations{,/module,/name,/value}`; old-only: `∅` |
| 17 | JSON: `AssignedLicenseDisabledPlansItemsString` typeDef | old `{type:"Other"}`; new adds `baseType:"string"` + constraint annotation |
| 18 | JSON: per-function param-name lists old vs new | 24 functions differ, all `Additional Values` removal; totals 388 → 364 |
| 19 | JSON: per-function description comparison | 0 differences |
| 20 | JSON: `readme` / `description` equality | both `True`; readme 6827 chars |
| 21 | JSON: annotation module/name histogram (new) | `ballerina/constraint:String` 46, `:Number` 18, `ballerina/http:Query` 102, `:Header` 9, `(None):display` 1 |
| 22 | `types.bal:2582-2583`, `:7256`, `:4916/4923/4926`, `:7346-7352`, `:2356`, `:6184` | annotation text matches render verbatim |
| 23 | 24 newly quoted field lines grepped verbatim in `types.bal` | all found (counts 1–7 each) |
| 24 | `grep -oE "'[A-Za-z0-9_]+"` field-name histograms src / old / new | src == old exactly; new ≥ src on `'error` 6→11, `'from` 4→8, `'resource` 4→8, `'type` 16→22 etc. (inclusion-flattened copies now quoted) |
| 25 | `client.bal:45` vs render `listDrive` line | `*ListDriveQueries queries` → `ListDriveQueries queries` (both renders) |
| 26 | `grep -c 'Queries queries) returns'` old / new | 24 / 24 |
| 27 | `grep -c 'string\[\] select = \[\]'` old / new | 16 / 16 |
| 28 | `grep -c 'record {\|'` src / old / new | 2 / 0 / 0 |
| 29 | `ConnectionConfig` defaults in src vs render | 11 defaults in `types.bal:6185…`; 0 in either render |
| 30 | `grep -c 'remote isolated function'` new; `grep -n 'function init'` new | 0; `10742: function init(...)` |
| 31 | `ls bala/3.0.2/any`; `find src -iname '*compiler-plugin*'` | no compiler-plugin dir either place |
| 32 | `package.json` | org/name/version `ballerinax/microsoft.onedrive/3.0.2`, `export:["microsoft.onedrive"]`, ballerina 2201.12.0 |
| 33 | Central API `…/ballerinax/microsoft.onedrive/3.0.2` | not deprecated, 1 module, pullCount 94 |
| 34 | `grep -c 'Special Agent Note'` old / new | 17 / 17 |
| 35 | `grep -n -A10 '^type WorkbookTableColumn record'` new (9880) vs `types.bal:4296` | inclusion flattened without docs/annotations |

## 10. Caveats and unverified items

* **Not compiled.** The renders were not fed to the Ballerina compiler; the "would not compile"
  statements in §5 (items 1, 3) are judgements from the language grammar (required parameter after
  defaultable parameters; `select` as a keyword — corroborated by the OpenAPI generator itself
  quoting it as `'select` in the source record), not from a compiler run.
* **Spot-checked, not exhaustive, on annotation *placement*.** Annotation *counts* were verified to
  match the source exactly (46/18/102/9), and 6 annotation sites were verified verbatim line-by-line
  against `types.bal`. The remaining ~169 sites were not individually diffed against their source
  record; count parity plus zero mismatches in the sample is the basis for the claim.
* **`old`/`new` renderer commits not inspected.** The report attributes behaviour to the renders
  themselves; the `ballerina-vscode` source at `eb5d81b3` / `412ba01e` was not read.
* **`// Special Agent Note` correctness** for the 17 cross-package type hints was not re-verified
  against `ballerina/http`; they are identical in both renders so they cannot be a regression.
* No other unverified claims: every number in this report comes from a command listed in §9.

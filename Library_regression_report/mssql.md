# ballerinax/mssql 1.19.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mssql` |
| Pinned version | `1.19.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mssql |
| Tag reviewed | `v1.19.0` (commit `fac81ac22c17d5e79d5e9f7cfe45b29b168587bb`, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mssql/1.19.0/java21` |
| Old render | `837` lines (35,573 bytes) |
| New render | `899` lines (38,858 bytes) |
| Verdict | **MINOR REGRESSION** |

## 1. Summary

`new` is a large, verified improvement on the rendered `.bal.txt`. All 13 `// Unknown type:` placeholders
(12 spatial/money `*Value` classes + `CdcListener`) become real class definitions whose `init` signatures
match `modules/mssql/types.bal` and `modules/mssql/cdc_listener.bal` exactly. Three genuinely broken
things in `old` are fixed: a truncated, non-parsable return type on `Client.query`
(`returns Error?>;`), an incorrect `remote` qualifier on `Client.close`, and a fabricated service type
`mssql:Service` (no such type exists) replaced by the correct `cdc:Service`. All 15 version-qualified
type references (`ballerinax/mssql:1.19.0:LineStringValue`, …) are gone. Nothing was dropped: 0
declarations removed, and the 559-line README section is byte-identical on both sides.

The single regression is metadata-only and invisible in the rendered text: in the service model JSON the
`tableName` parameter of `onRead`/`onCreate`/`onUpdate`/`onDelete` loses its `"optional": true` flag,
although the CDC handlers really can be written without it. Separately, `new` introduces two render-level
inaccuracies of its own (a spurious trailing `config` parameter on `CdcListener.init`, and an
over-strong "mandatory `@cdc:ServiceConfig`" claim that the library's own example contradicts).

## 2. Change inventory

Counted with `diff -u old new`: **87 lines added, 30 lines removed, 3 hunks** (matches
`OLD_AND_NEW_DIFFS/mssql_diff.md`; the diff file's "+94/−32" includes context-boundary blank lines).

| Signal | old | new |
|---|---|---|
| Lines | 837 | 899 |
| `// Unknown type:` placeholders | 13 | 0 |
| Version-qualified type refs (occurrences) | 15 | 0 |
| `// --- ` section markers | 5 (README, END README, Types, Client, Service) | 5 (same) |
| README section (lines 1–559) | identical (`diff` → no output) | identical |
| JSON `typeDefs` | 31 | 31 (same names; 13 with no `type` tag → `"type": "Class"`) |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 1 / 0 | 1 / 0 / 1 / 0 |

**Added (18 declarations, 0 removed):**

| Kind | Count | Names |
|---|---|---|
| `class` | 13 | `PointValue`, `MultiPointValue`, `LineStringValue`, `MultiLineStringValue`, `CircularStringValue`, `CompoundCurveValue`, `PolygonValue`, `MultiPolygonValue`, `CurvePolygonValue`, `GeometryCollectionValue`, `MoneyValue`, `SmallMoneyValue`, `CdcListener` |
| class method | 5 | `CdcListener.attach`, `.'start`, `.detach`, `.gracefulStop`, `.immediateStop` |

**Modified (not added/removed):**

| Location | old | new |
|---|---|---|
| `Client.init` return | `ballerina/sql:1.19.0:Error?` | `sql:Error?` |
| `Client.query` return | `Error?>` (truncated, non-parsable) | `stream<rowType, sql:Error?>` |
| `Client.close` qualifier | `remote function close()` | `function close()` |
| `type CompoundCurveElement` | `ballerinax/mssql:1.19.0:LineStringValue\|…` | `LineStringValue\|CircularStringValue` |
| `type CircularArcRing` | version-qualified (3 members) | plain (3 members) |
| `type GeometryCollectionElement` | version-qualified (9 members) | plain (9 members) |
| Service type | `service mssql:Service on …` | `service cdc:Service on …` |
| Service block | 5 handlers, terse one-line docs | 5 handlers marked `// optional`, `+ param` docs, `@cdc:ServiceConfig {...}` annotation line, `# Requires: import ballerinax/mssql.cdc.driver as _;`, at-least-one-handler note; type refs module-qualified (`mssql:MsSqlListenerConfiguration`) |

**JSON-only changes** (not surfaced in the render): `services[0]` gains `annotations`, `constraints`,
`requiredImports`, `serviceTypeModule`; all five handlers flip `"optional": false` → `true`; handler
`record {}` parameters gain a `binding.typedescs` block; `tableName` loses `"optional": true`.

## 3. Correctness against library source

Every class `new` adds was checked against the bala (authoritative) and matches upstream `v1.19.0`:

| Rendered signature (new) | Source | Match |
|---|---|---|
| `PointValue.init(Point\|string\|() value = (), int\|() srid = ())` | `modules/mssql/types.bal:64` | yes |
| `MultiPointValue.init(Point[]\|string\|() …)` | `types.bal:79` | yes |
| `LineStringValue.init(Point[]\|string\|() …)` | `types.bal:94` | yes |
| `MultiLineStringValue.init(LineStringValue[]\|string\|() …)` | `types.bal:109` | yes |
| `CircularStringValue.init(Point[]\|string\|() …)` | `types.bal:124` | yes |
| `CompoundCurveValue.init(CompoundCurveElement[]\|string\|() …)` | `types.bal:139` | yes |
| `PolygonValue.init(LineStringValue[]\|string\|() …)` | `types.bal:154` | yes |
| `MultiPolygonValue.init(PolygonValue[]\|string\|() …)` | `types.bal:169` | yes |
| `CurvePolygonValue.init(CircularArcRing[]\|string\|() …)` | `types.bal:184` | yes |
| `GeometryCollectionValue.init(GeometryCollectionElement[]\|string\|() …)` | `types.bal:199` | yes |
| `MoneyValue.init(decimal\|float\|string\|() value = ())` | `types.bal:212` | yes |
| `SmallMoneyValue.init(decimal\|float\|string\|() value = ())` | `types.bal:224` | yes |
| `CdcListener.attach(cdc:Service s, string[]\|string\|() name = ()) returns cdc:Error\|()` | `cdc_listener.bal:44` | yes |
| `CdcListener.'start() returns cdc:Error\|()` | `cdc_listener.bal:51` | yes |
| `CdcListener.detach(cdc:Service s) returns cdc:Error\|()` | `cdc_listener.bal:59` | yes |
| `CdcListener.gracefulStop() returns cdc:Error\|()` | `cdc_listener.bal:66` | yes |
| `CdcListener.immediateStop() returns cdc:Error\|()` | `cdc_listener.bal:73` | yes |

Other `new`-side changes verified correct:

- `Client.close` is `public isolated function close() returns sql:Error?` (`Client.bal:114`) — **not**
  `remote`. `old`'s `remote function close()` was wrong; `new` is right.
- `Client.query` returns `stream<rowType, sql:Error?>` (`Client.bal:57`) — `new` matches; `old`'s
  `returns Error?>` was a truncated fragment.
- `Client.init` returns `sql:Error?` (`Client.bal:37`) — `new` matches.
- The union members of `CompoundCurveElement` / `CircularArcRing` / `GeometryCollectionElement`
  (`types.bal:43,47,51-53`) match `new` exactly, unqualified as they appear in source.
- `service cdc:Service` is correct: `cdc:Service` is defined at
  `~/.ballerina/…/ballerinax/cdc/1.4.0/java21/modules/cdc/service.bal:43` as a distinct service object
  with **no** required methods; `mssql` exports no `Service` type (`package.json` `export: ["mssql"]`,
  and no `Service` symbol in `modules/mssql/*.bal`). `old`'s `service mssql:Service` was an invented symbol.
- `# Requires: import ballerinax/mssql.cdc.driver as _;` is correct — the same import appears at
  `examples/fraud-detection/main.bal:20` and `ballerina/tests/listener_tests.bal:20`, and the package
  `ballerinax/mssql.cdc.driver` exists locally (`bala/ballerinax/mssql.cdc.driver/1.0.2`).
- The at-least-one-handler constraint (`onRead`/`onCreate`/`onUpdate`/`onDelete`) is grounded in the CDC
  compiler plugin: `DiagnosticCodes.CDC_101 = "missing valid remote function: expected at least one of %s
  functions"` with the non-Postgres list `''onRead'', ''onCreate'', ''onUpdate'' or ''onDelete''`
  (extracted from `cdc-compiler-plugin-1.4.0.jar`). Correctly excludes the Postgres-only `onTruncate`.
- Handlers marked `// optional` in `new` is correct (`cdc:Service` is an empty distinct service object;
  `old`'s JSON `"optional": false` implied all five were mandatory).

## 4. Regressions

**One, metadata-only — not visible in the rendered `.bal.txt`.**

1. **`tableName` parameter optionality lost in the service JSON.** In `old/ballerinax_mssql.json`,
   `services[0].methods[*].parameters` marks `tableName` `"optional": true` for `onRead`, `onCreate`,
   `onUpdate`, `onDelete`. In `new/ballerinax_mssql.json` that flag is gone (only the description
   changed alongside it). The library genuinely allows the handler without `tableName` —
   `examples/fraud-detection/main.bal:38` declares `onCreate(Transactions trx)` and
   `ballerina/README.md` (rendered at lines 534–546 of both files) shows
   `onRead(record{} after)`. The CDC plugin validates counts via `CDC_104 "invalid parameter count:
   expected %s"` rather than requiring both. Both renders print `string tableName` identically, so no
   LLM consuming the `.bal.txt` is affected; the loss is only in the JSON model.

Nothing else regressed. Explicitly checked: every removed line
(`diff -u old new | grep '^-[^-]'` → 30 lines) is either an `// Unknown type:` placeholder, a
version-qualified union alias replaced by a plain one, one of the three malformed/incorrect `Client`
lines, or an `old` service line superseded by a richer and more accurate `new` one. No declaration,
parameter, default, return type, doc comment, `// Special Agent Note:` annotation, or README byte was
dropped (README diff over lines 1–559 is empty; `typeDefs` name sets are set-equal; `clients` JSON
differs only in the two fixed type strings).

## 5. Issues in `new` (independent of `old`)

1. **`CdcListener.init` carries a spurious trailing `config` parameter** (new render line 797). Source is
   `public isolated function init(*MsSqlListenerConfiguration config)` (`cdc_listener.bal:30`). The
   extractor correctly flattens the included record's fields into params, but then also emits the
   included-record parameter itself:
   `init(string engineName = "", …, MssqlOptions options = {}, MsSqlListenerConfiguration config)`.
   That is (a) a duplicate of the flattened fields and (b) not valid Ballerina — a required parameter
   cannot follow defaultable ones. Root cause is in the JSON (`"name":"config","optional":true` with no
   `default`), which is byte-identical in `old`'s JSON; it only becomes visible now that the class is
   rendered. Also `MsSqlDatabaseConnection database = {databaseNames: "", username: "", password: ""}`
   shows a synthesized default for a field that is required in `MsSqlListenerConfiguration`
   (`types.bal:248`).
2. **"Mandatory `@cdc:ServiceConfig`" is over-stated** (new render lines 870–873:
   `Mandatory: this service must carry the @cdc:ServiceConfig annotation` / `@cdc:ServiceConfig {...} //
   required`). The annotation is declared `public annotation CdcServiceConfig ServiceConfig on service`
   (cdc `annotations.bal`) and is required only when attaching **multiple** services to one listener —
   `ballerina/tests/listener_tests.bal:80` asserts the runtime message *"The 'cdc:ServiceConfig'
   annotation is mandatory when attaching multiple services to the 'cdc:Listener'."*, and the library's
   own example `examples/fraud-detection/main.bal:37` declares `service cdc:Service on financeDBListener`
   with no annotation. No compiler-plugin diagnostic requires it (the extracted `DiagnosticCodes` enum
   contains no such code). Additionally the literal `{...}` placeholder does not compile if copied
   verbatim, and `CdcServiceConfig` has a required `tables` field the render does not spell out.
3. **`typedesc` parameters are rendered as their constraint, with a type name as the default value**
   (both sides): `query(…, record {|anydata...;|} rowType = record {|anydata...;|})` and
   `queryRow(…, anydata returnType = anydata)` vs. source `typedesc<record {}> rowType = <>` /
   `typedesc<anydata> returnType = <>` (`Client.bal:56,69`). Neither form compiles, and it is internally
   inconsistent with `call(…, typedesc<record {|anydata...;|}>[] rowTypes = [])`, which keeps `typedesc`.
4. **Record defaults dropped and closed records rendered open** (both sides). All 10 rendered records use
   `record {` although 9 of the 12 source records are closed `record {|…|}`; every defaulted field is
   printed as optional with the value discarded — e.g. `boolean useXADatasource?` for
   `useXADatasource = false` (`Client.bal:153`), `string connectorClass?` for the Debezium connector class
   default (`types.bal:295`), `int port?` for `= 1433`, `int tasksMax?` for `= 1`, `decimal lockTimeout?`
   for `= 10`. An LLM cannot recover the required Debezium connector class from the render.
5. **The service listener expression is not valid call syntax** (both sides):
   `on new mssql:CdcListener(mssql:MsSqlListenerConfiguration config = {database: {…}})` — a parameter
   declaration is emitted where an argument list belongs. Real usage is
   `new (database = {…}, options = {…})` (`examples/fraud-detection/main.bal:25`).

## 6. Coverage gaps vs. the library

`package.json` declares `"export": ["mssql"]` and `modules/` contains only `mssql`, so there is **no
submodule-only API** for this package — the `pkg.getDefaultModule()` limitation costs nothing here.

Top-level public symbols of the default module, all 31 present in `new` (13 of them only as
`// Unknown type:` in `old`): 2 enums (`DataQueryMode`, `SourceStructVersion`) + their 4 constants
(`FUNCTION`, `DIRECT`, `V1`, `V2`), 9 records (`Options`, `SecureSocket`, `Point`,
`StreamingConfiguration`, `MsSqlListenerConfiguration`, `MsSqlDatabaseConnection`, `MssqlOptions`,
`ExtendedSnapshotConfiguration`, `DataTypeConfiguration`), 3 unions, 13 classes, plus `client class
Client`. There are no public module-level functions (`grep -E '^public (isolated )?function'` over
`modules/mssql/*.bal` returns nothing; `createClient`, `nativeBatchExecute` and all `populate*` helpers
are module-private and correctly absent). `ClientConfiguration` (`Client.bal:130`) is non-public and
correctly absent from both renders.

**One gap, shared by both renders (1 category, 22 symbols):** the public *fields* of the 13 classes and
their type inclusions are not rendered. `PointValue` etc. each declare `public Point|string? value` and
`public int? srid` (`MoneyValue`/`SmallMoneyValue` have `value` only) — 22 public fields in total — and
every `*Value` class includes `*sql:TypedValue` while `CdcListener` includes `*cdc:Listener`. The JSON
`typeDefs` entries for classes contain a `functions` array only, on both sides. Consequence: a consumer
of the render cannot tell that `PointValue` is an `sql:TypedValue` (i.e. usable inside an
`sql:ParameterizedQuery`), which is the whole purpose of these types. `new` is still strictly better than
`old` here, which showed nothing at all. `distinct`, `isolated` and `public` qualifiers are likewise
dropped on both sides.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.mssql.compiler.MSSQLCompilerPlugin`
(`mssql-compiler-plugin-1.19.0.jar`). Reading the upstream sources at `v1.19.0`, it contributes
**compile-time validation only** — no code actions, no generated artifacts, no annotations, so there is
nothing it implies that ought to appear as a declaration in the render:

- `analyzer/InitializerParamAnalyzer.java` — validates the `connectionPool` argument of `Client.init`:
  `SQL_101` "expected value is greater than one", `SQL_102` "greater than zero", `SQL_103` "greater than
  or equal to 30".
- `analyzer/RecordAnalyzer.java` + `Utils.java` — validates `mssql:Options` literals:
  `MSSQL_101` "expected value greater than or equal to zero" and `MSSQL_102` "greater than or equal to
  -1", applied to `loginTimeout` / `socketTimeout` / `queryTimeout` (`Constants.java:59-61`).

Neither render states these numeric constraints as machine-checkable facts, but the record docs carried
into both renders do convey them informally ("Socket read/write timeout in seconds (0 means no timeout)",
"Query execution timeout in seconds (-1/0 means no timeout)"). No change between `old` and `new`.

The CDC service constraints in `new` come from the *cdc* plugin, not this one, and were verified above
(§3): the `$atLeastOneChangeHandler` constraint corresponds exactly to `CDC_101`.

## 8. Other considerations

- Stable 1.x package, not deprecated; Central metadata `ballerina_version: 2201.13.0`, keywords include
  `Type/Connector` and `Type/Trigger`. No version drift: both sides render `ballerinax/mssql:1.19.0`
  and the pinned bala is the only one consumed.
- Size: +62 lines / +3,285 bytes (+9.2%) for 13 previously-invisible types and richer service guidance —
  a good token trade. The render is dominated by the README (559 of 899 lines, 62%).
- The README section repeats the `ballerinax/mssql.driver as _` requirement for the SQL client (render
  lines 21–34) and is preserved verbatim on both sides, so the two distinct driver packages
  (`mssql.driver` for the client, `mssql.cdc.driver` for the listener) are both discoverable in `new`;
  only the CDC one is missing from `old`'s structured model.
- Enum member string values (`FUNCTION = "function"`, `V1 = "v1"` …) survive only as the four separate
  `const string` declarations; the `enum` bodies list bare member names in an order that differs from
  source (`DIRECT, FUNCTION`). Unchanged between sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 837 / 899 |
| `wc -c old new` | 35,573 / 38,858 |
| `git ls-remote --tags …module-ballerinax-mssql \| grep v1.19.0` | `2e5fc24…` / peeled `fac81ac…` — exact tag exists |
| `git clone --depth 1 --branch v1.19.0 … src`; `git log -1` | `fac81ac22c17d5e79d5e9f7cfe45b29b168587bb (grafted, tag: v1.19.0)` |
| `ls -R <bala>` | `modules/mssql/{Client,cdc_listener,types,utils}.bal`; `compiler-plugin/libs/mssql-compiler-plugin-1.19.0.jar`; `platform/java21/{mssql,sql}-native-1.19.0.jar`; `docs/README.md` |
| `wc -l <bala>/modules/mssql/*.bal` | Client 176, cdc_listener 76, types 317, utils 162 |
| `grep -c '^// Unknown type:'` old / new | 13 / 0 |
| `grep -o 'ballerinax/mssql:1.19.0:\|ballerina/sql:1.19.0:' old \| wc -l` | 15 (0 in new) |
| `grep -n '^// --- '` old / new | 5 markers each, same names |
| `diff -u old new \| grep -c '^+[^+]'` / `'^-[^-]'` | 87 added / 30 removed |
| `diff <(sed -n 1,559p old) <(sed -n 1,559p new)` | empty — README byte-identical |
| `diff -u old new \| grep '^-[^-]'` (full listing reviewed) | 13 placeholders, 3 qualified unions, 3 Client lines, 11 service lines — no content loss |
| Python set-compare of `typeDefs` names (old vs new) | equal (31 each) |
| Python compare of `typeDefs` payloads ignoring `type` tag | only 3 differ: the 3 unions (version qualifiers stripped) |
| Python diff of `clients` JSON | 2 lines: `ballerina/sql:1.19.0:Error?`→`sql:Error?`, `Error?>`→`stream<rowType, sql:Error?>` |
| Python diff of `services` JSON | 162→278 lines; adds `annotations`/`constraints`/`requiredImports`/`serviceTypeModule`, flips 5× `optional:false→true`, drops 5× `tableName "optional": true` |
| `grep -n "function close" <bala>/modules/mssql/Client.bal` | `114: public isolated function close() returns sql:Error?` |
| `Client.bal:56-57` | `remote isolated function query(… typedesc<record {}> rowType = <>) returns stream<rowType, sql:Error?>` |
| `types.bal:59-227` read in full | 12 `public distinct class *Value`, each `*sql:TypedValue` + `public … value` (+ `public int? srid`) |
| `cdc_listener.bal:19-76` read in full | `public isolated class CdcListener { *cdc:Listener; init(*MsSqlListenerConfiguration config); attach; 'start; detach; gracefulStop; immediateStop }` |
| `grep -E '^public (isolated )?function' <bala>/modules/mssql/*.bal` | no matches — no public module-level functions |
| `python3 … package.json` | `export: ["mssql"]`, `ballerina_version: 2201.13.0`, not a template |
| `grep -rn "cdc.driver" src` | `examples/fraud-detection/main.bal:20`, `ballerina/tests/listener_tests.bal:20`, `Dependencies.toml:436/445/452` |
| `grep -rn "ServiceConfig" src` | only `ballerina/tests/listener_tests.bal:80,90,97,159,179` — line 80 asserts it is mandatory *when attaching multiple services* |
| `examples/fraud-detection/main.bal:37` | `service cdc:Service on financeDBListener {` — no `@cdc:ServiceConfig` |
| cdc `modules/cdc/service.bal:43` | `public type Service distinct service object { };` — no required methods |
| cdc `modules/cdc/annotations.bal` | `public annotation CdcServiceConfig ServiceConfig on service;`, `CdcServiceConfig` = `record {| string\|string[] tables; |}` |
| strings extracted from `cdc-compiler-plugin-1.4.0.jar` classes | `CDC_101 "missing valid remote function: expected at least one of %s functions"`, non-Postgres list `''onRead'', ''onCreate'', ''onUpdate'' or ''onDelete''`; `CDC_104 "invalid parameter count: expected %s"`; no mandatory-annotation diagnostic |
| `compiler-plugin/src/…/MSSQLDiagnosticsCode.java` | `SQL_101/102/103`, `MSSQL_101/102` — validation only |
| `compiler-plugin/src/…/Constants.java:59-61` | `loginTimeout`, `socketTimeout`, `queryTimeout` |
| `grep -c 'record {$'` / `'record {|'` in new | 10 open records rendered / 2 occurrences of `record {|anydata...;|}` (inline typedesc constraints) |

## 10. Caveats and unverified items

- The clone is `--depth 1` at `v1.19.0`, so history-based checks (e.g. when `close()` lost its `remote`
  qualifier) were not possible. Where GitHub and the bala could disagree, the bala was used; the two
  agreed everywhere I compared (`Client.bal`, `types.bal`, `cdc_listener.bal` signatures).
- The CDC compiler-plugin behaviour was established by extracting printable strings from
  `cdc-compiler-plugin-1.4.0.jar` (its sources are in a different repo, not cloned). The diagnostic
  codes and messages are quoted verbatim from the class constant pools, but I did not read the plugin's
  control flow, so the exact conditions under which `CDC_104` accepts a 1-parameter handler are
  inferred from the library's own example and README rather than from the validator source.
- I did not compile either render or any generated snippet with `bal build`; claims that specific
  rendered forms "do not compile" (`@cdc:ServiceConfig {...}`, `returnType = anydata`,
  `init(… , MsSqlListenerConfiguration config)` after defaultable params, the listener-argument
  expression) are based on Ballerina language rules, not on an observed compiler error.
- Whether the extra `config` parameter on `CdcListener.init` and the "mandatory annotation" wording are
  intentional product decisions in spec v2 is unknown to me; I report them as inaccuracies against the
  library source and its published example.
- I did not re-query `api.central.ballerina.io` (no network call made for metadata); package facts here
  come from the local bala's `package.json` and `bala.json`.

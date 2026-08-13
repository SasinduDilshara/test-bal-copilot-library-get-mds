# ballerina/sql 1.19.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/sql` |
| Pinned version | `1.19.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-sql |
| Tag reviewed | `v1.19.0` (clone HEAD `25fda3a`, `git describe --tags` → `v1.19.0`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/sql/1.19.0/java21` |
| Old render | `1027` lines (37,362 bytes) |
| New render | `1551` lines (56,979 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly richer than `old` for this library. Every one of the 113 `// Unknown type:`
placeholders in `old` is replaced by a real definition in `new` (103 classes + 10 error types), the
`sql:Client` and `sql:SchemaClient` object types gain their 11 remote/normal methods (`old` rendered
both as empty `class X {}`), 18 version-qualified type references (`ballerina/time:2.8.1:Utc`,
`ballerina/sql:1.19.0:TypedValue`, …) are normalised to `time:Utc` / `TypedValue`, the `Column`
annotation is emitted for the first time, and one **malformed, non-parseable** line in `old`
(`function generateApplicationErrorStream(string message) returns Error?>;`) is corrected to
`returns stream<record {|anydata...;|}, Error?>`.

Nothing that was present and correct in `old` is missing, truncated or degraded in `new`: the
complete set of removed lines is 122 = 113 `// Unknown type:` lines + 9 lines that are each replaced
by a strictly better version. The README block (lines 7–450) is byte-identical on both sides.

This matters more than usual because `sql:Error`, `sql:ParameterizedQuery`, `sql:ExecutionResult`
and the `sql:Client` object type are the contract that `ballerinax/mysql`, `postgresql`, `mssql`,
`oracledb`, `java.jdbc`, `snowflake`, `aws.redshift` and `cdc` all inherit. In `old` an LLM reading
this render was told `sql:Error` was an unknown type and `sql:Client` had no methods at all.

## 2. Change inventory

Line counts (`wc -l`): old **1027**, new **1551**. Diff: **+646 / −122**, 8 hunks
(`diff -u old new`).

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 113 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:`) | 18 | 0 |
| `// --- section ---` markers | 4 | 5 (`Annotations` added) |
| Indented member functions (`^    (remote )?function`) | 0 | 122 |
| `remote function` lines | 0 | 9 |
| Doc-comment lines (`^\s*#`) | 131 | 353 |

### Top-level declarations (body only, i.e. after `// --- END README ---`)

| Kind | old | new |
|---|---|---|
| `UNKNOWN` placeholder | 113 | 0 |
| `class` | 7 | 110 |
| `type` | 13 | 23 |
| `enum` | 6 | 6 |
| `const` | 2 | 2 |
| `function` (module level) | 4 | 4 |
| `annotation` | 0 | 1 |
| **distinct names** | **145** | **146** |

`comm -23` over the two extracted declaration sets: **zero** non-`UNKNOWN` declarations present in
`old` and absent from `new`. `comm -13`: 103 classes + 10 error types + 1 annotation added.

### The 9 non-placeholder lines removed

| removed from `old` | replaced in `new` by |
|---|---|
| `class Client {` | `client class Client {` + 6 methods |
| `class SchemaClient {` | `client class SchemaClient {` + 5 methods |
| `    ballerina/sql:1.19.0:TransactionIsolation? transactionIsolation?;` | `    TransactionIsolation? transactionIsolation?;` |
| `type Value …ballerina/time:2.8.1:Utc…;` | `type Value …time:Utc…;` |
| `type Parameter …ballerina/sql:1.19.0:InOutParameter…;` | `type Parameter …InOutParameter…;` |
| `function generateApplicationErrorStream(string message) returns Error?>;` | `… returns stream<record {|anydata...;|}, Error?>;` |
| 1 `}` + 2 blank lines | re-flowed |

### JSON-level (`old/ballerina_sql.json` vs `new/ballerina_sql.json`)

| | old | new |
|---|---|---|
| `typeDefs` | 160 | 160 (same names, `comm` diff empty both directions) |
| `typeDefs` with no `"type"` tag | 103 | 0 |
| `typeDefs` tagged `Class` | 7 | 110 |
| `Error` typeDefs carrying `baseType` | 0 | 10 |
| member functions inside `typeDefs` | 161 | 122 |
| `annotations` | 0 | 1 |
| top-level `functions` | 4 | 4 |
| `clients` / `services` | 0 / 0 | 0 / 0 |
| `readme` | identical (19,793 chars) | identical |

The member-function count fell by 39 only because `new` **added** 14 real methods (6 on `Client`,
5 on `SchemaClient`, `OutParameter.get`, `CustomResultIterator.nextResult`/`.getNextQueryResult`)
and **dropped 53 synthesised zero-argument `init` constructors** on the `*OutParameter` classes.
Verified programmatically: all 53 dropped constructors had `parameters == []`, and the source
declares no explicit `init` for any of them (`types.bal:1311-1321` `XMLOutParameter` is
representative). No declared constructor was lost — the 50 `*Value` classes with a real `init`
(e.g. `VarcharValue.init(string? value)`) keep it in both JSON and render.

## 3. Correctness against library source

All citations are the bala copy (authoritative), `…/1.19.0/java21/modules/sql/`.

| Rendered in `new` | Source | Match |
|---|---|---|
| `client class Client` + `query/queryRow/execute/batchExecute/call/close` | `client.bal:20-82` | yes — order, names, param names, return types all correspond |
| `remote function execute(ParameterizedQuery sqlQuery) returns ExecutionResult\|Error;` | `client.bal:45` | exact |
| `remote function batchExecute(ParameterizedQuery[] sqlQueries) returns ExecutionResult[]\|Error;` | `client.bal:53` | exact |
| `remote function call(ParameterizedCallQuery sqlQuery, typedesc<record {\|anydata...;\|}>[] rowTypes = [])` | `client.bal:74-75` (`typedesc<record {}>[] rowTypes = []`) | equivalent (`record {}` ≡ `record {\|anydata...;\|}`) |
| `function close() returns Error\|();` | `client.bal:81` (`returns Error?`) | equivalent |
| `client class SchemaClient` + `listTables/getTableInfo/listRoutines/getRoutineInfo/close` | `schema_client.bal:19-55` | exact, incl. `ColumnRetrievalOptions include = COLUMNS_ONLY` (`schema_client.bal:36`) |
| `type Error error;` | `error.bal:39` `public type Error distinct error` | lossy — see §5.4 |
| `type DatabaseError error<record {\|int errorCode; string? sqlState; anydata...;\|}>;` | `error.bal:44` + `DatabaseErrorDetail` `error.bal:32-35` | detail fields correct; `distinct`/`& Error` lost |
| `type BatchExecuteError error<record {\|int errorCode; string? sqlState; ExecutionResult[] executionResults; anydata...;\|}>;` | `error.bal:47` + `error.bal:22-26` | fields correct |
| `public annotation ColumnConfig Column on record field;` | `annotation.bal:24` | byte-for-byte identical |
| `class CustomResultIterator` `nextResult(ResultIterator) returns record {\|anydata...;\|}\|Error\|()`, `getNextQueryResult(ProcedureCallResult) returns boolean\|Error` | `types.bal:1462-1465` | exact |
| `class ResultIterator` `init(Error\|() err = (), CustomResultIterator\|() customResultIterator = ())`, `next() returns record {\|record {\|anydata...;\|} value;\|}\|Error\|()`, `close()` | `types.bal:1382`, `1387`, `1425` | exact |
| `class ProcedureCallResult` `init(CustomResultIterator\|() = ())`, `getNextQueryResult()`, `close()` | `types.bal:1441-1457` | methods exact; public fields missing, §5.6 |
| `class InOutParameter` `init(Value 'in)` | `types.bal:1339-1341` | exact |
| `class VarcharValue { function init(string\|() value = ()) }` | `types.bal:41-46` | exact |
| `TransactionIsolation? transactionIsolation?;` in `ConnectionPool` | `connection-pool.bal:111` | correct (`old` had the version-qualified form) |
| `function generateApplicationErrorStream(string message) returns stream<record {\|anydata...;\|}, Error?>;` | `utils.bal:81` | correct (`old` was truncated to `Error?>`) |
| `const int SUCCESS_NO_INFO = -2;` / `EXECUTION_FAILED = -3;` (new lines 486, 489) | `types.bal:621`, `types.bal:625` | exact |

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff -u old new | grep '^-'` yields exactly 122 lines; 113 are `// Unknown type: X` and the
  remaining 9 are itemised in §2 — every one is superseded by a superset/corrected form.
- Set difference of extracted top-level declarations (`comm -23 d_old d_new`, README excluded)
  returns nothing outside the `UNKNOWN` placeholders.
- README block: `diff <(sed -n '7,450p' old) <(sed -n '7,450p' new)` → identical; JSON `readme`
  fields compare equal (19,793 chars), as do the `description` fields.
- Module-level `functions` array: same 4 names in both JSONs; the `Functions` section text is
  identical except the corrected `generateApplicationErrorStream` return type.
- `enum` (6), `const` (2), `Record` typeDefs (11), `Union` typeDefs (2) counts unchanged in the JSON.
- Brace balance in the declaration body: old 30/30, new 154/154 — no truncated block.
- No new occurrences of `undefined` / `[object Object]` / `NaN`; the only `null` hits are the
  legitimate `boolean nullable;` field, present on both sides. Non-ASCII: 1 line on each side
  (the same smart-quoted README comment at new:186).
- Only member functions were *removed* at the JSON level (53 synthesised no-arg `init`s), and those
  were never rendered by `old` anyway — the classes owning them were all `// Unknown type:` lines.

## 5. Issues in `new` (independent of `old`)

Nine, ordered by impact. Items 2, 3, 6, 8, 9 originate in the Java extractor/JSON and are present
identically in the `old` JSON — they are simply now *visible* because `new` renders the members.

1. **Object types rendered as classes.** `Client`, `SchemaClient`, `OutParameter`,
   `CustomResultIterator`, `ParameterizedQuery`, `ParameterizedCallQuery`, `TypedValue` are
   `public type X … object { … }` in source (`client.bal:20`, `schema_client.bal:19`,
   `types.bal:613`, `types.bal:1366`, `types.bal:1462`) but appear as `class` / `client class`.
   `sql:Client` is abstract — every concrete client is `mysql:Client` etc. — so the render invites
   `new sql:Client()`, which cannot compile. `old` had the same `class` keyword, so this is not a
   regression, but `new` makes it more convincing by attaching methods.
2. **`typedesc<>` stripped on inferred-typedesc parameters.**
   `remote function query(ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = <>)`
   vs source `typedesc<record {}> rowType = <>` (`client.bal:28`); likewise
   `queryRow(… anydata returnType = <>)` vs `typedesc<anydata>` (`client.bal:38`). Confirmed to come
   from the JSON (`"type": {"name": "record {|anydata...;|}"}`) — identical shape in the old JSON.
   Note the inconsistency: `call`'s non-inferred `typedesc<record {|anydata...;|}>[] rowTypes = []`
   keeps its `typedesc`. As written these lines are not valid Ballerina.
3. **Invented default values on 53 `get()` methods.** `function get(anydata typeDesc = anydata)`
   appears 53×; the source default is `<>` (`types.bal:1305`, `1318`, `1349`). `= anydata` is a type
   name in value position — non-compiling, and misleading. `CursorOutParameter.get` has the same
   defect (`record {|anydata...;|} rowType = record {|anydata...;|}` vs `<>`, `types.bal:1330`).
   Only `OutParameter.get` carries the correct `<>` (its JSON entry is the one `new` newly adds).
   Verified byte-identical in the old JSON, so this is an extractor bug, not a spec-v2 bug.
4. **Error hierarchy flattened.** `distinct` is dropped from all 10 error types, and the subtype
   relations are erased: `error.bal:57` `public type DataError distinct ApplicationError` renders as
   `type DataError error;`; `NoRowsError`, `ApplicationError`, `TypeMismatchError`,
   `ConversionError`, `FieldMismatchError`, `UnsupportedTypeError` likewise become bare `error`.
   `DatabaseError`/`BatchExecuteError` inline their detail records rather than referencing
   `DatabaseErrorDetail`/`BatchExecuteErrorDetail`, both of which *are* rendered separately a few
   lines above. Consequence: the render does not tell a consumer that `sql:NoRowsError is sql:Error`
   — the single most common `check`/`is` pattern for every SQL connector.
5. **50 class doc comments missing.** `InOutParameter` (new:860) and the 49 `*Value` classes
   (`VarcharValue` new:896 …) render with no `#` doc, although the source documents them
   (`types.bal:38` `# Represents SQL Varchar type parameter in \`sql:ParameterizedQuery\`.`).
   The JSON carries `"description": ""` for these on **both** sides, so the loss is upstream of the
   renderer.
6. **No object/class fields anywhere.** A scan of every class body in `new` finds 0 non-function
   members. Missing as a result: `ProcedureCallResult.executionResult` and `.queryResult`
   (`types.bal:1437-1439`) — the whole point of `call()`; `ResultIterator.customResultIterator`;
   `ParameterizedQuery.strings` / `.insertions` (`types.bal:615-616`), which leaves
   `class ParameterizedQuery {}` empty at new:849; and `public string? value` on each `*Value` class.
   `old` rendered these classes empty too, so no regression.
7. **`time:` used without an import.** `type Value` and `type Parameter` (new:843, new:877) reference
   `time:Utc`, `time:Civil`, `time:Date`, `time:TimeOfDay`, but the render preamble only emits
   `import ballerina/sql;` (new:5). 10 `time:` occurrences, no `import ballerina/time;`. `old` was
   equally non-compiling here (`ballerina/time:2.8.1:Utc`), so this is a residual, not a regression.
8. **Rest parameter rendered as an array.** `function queryConcat(ParameterizedQuery[] queries)`
   vs source `queryConcat(ParameterizedQuery... queries)` (`utils.bal:21`). The render's own README
   at new:160 shows the correct call `sql:queryConcat(query, query1)`, contradicting the signature.
   Identical on both sides.
9. **`isolated` / `public` qualifiers dropped** on every declaration except the annotation. Shared
   with `old`; cosmetic for LLM consumption but the render is not copy-pasteable.

## 6. Coverage gaps vs. the library

The bala has a **single module** (`ls …/modules` → `sql` only), so there is no submodule-only API
and no shared submodule gap for this library.

Public top-level symbols extracted from the 9 bala `.bal` files: 146 declarations
(`type`/`class`/`enum`/`const`/`function`/`annotation`). After normalising the kind keyword
(object types → `class`) and the annotation name, **all 146 appear in `new`**; 33 appear in `old`.

Absent from **both** renders — 16 `public configurable` module-level variables in
`connection-pool.bal:20-67`:

`maxOpenConnections`, `maxConnectionLifeTime`, `minIdleConnections`, `connectionTimeout`,
`idleTimeout`, `validationTimeout`, `leakDetectionThreshold`, `keepAliveTime`, `poolName`,
`initializationFailTimeout`, `transactionIsolation`, `connectionTestQuery`, `connectionInitSql`,
`readOnly`, `allowPoolSuspension`, `isolateInternalQueries`.

These are the `ballerina.sql.*` Config.toml knobs; the `ConnectionPool` record docs reference them
by name, but the variables themselves are never listed. The extractor emits no module-level
variable category at all (no such key in either JSON). Shared gap — count: **16**.

Field-level gaps (class/object fields, §5.6) are not counted here as they are not top-level symbols.

## 7. Compiler plugin

`has_plugin: true` — confirmed: `…/1.19.0/java21/compiler-plugin/compiler-plugin.json` declares
`plugin_id: sql-compiler-plugin`, `plugin_class: io.ballerina.stdlib.sql.compiler.SQLCompilerPlugin`,
shipping `compiler-plugin/libs/sql-compiler-plugin-1.19.0.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/stdlib/sql/compiler/`, 8 files):

- `SQLCompilerPlugin.java:30` registers exactly one thing: `addCodeAnalyzer(new SQLCodeAnalyzer())`.
  **No code actions, no code modifiers, no generated artifacts, no annotation processing.**
- `analyzer/ConnectionPoolConfigAnalyzer.java` validates `sql:ConnectionPool` literals:
  `SQL_101` `maxOpenConnections` must be ≥ 1 (line 99-103), `SQL_102` `minIdleConnections` must be
  ≥ 0 (110-114), `SQL_103` `maxConnectionLifeTime` must be `0` or ≥ 30 (120-124). All ERROR severity.
- `analyzer/MethodAnalyzer.java` validates the `typedesc` argument passed to `OutParameter.get()`
  per concrete out-parameter class, emitting `SQL_201`–`SQL_231`
  (`SQLDiagnosticsCodes.java:33-45`), e.g. "expected value is any one of `time:Civil`, `time:Utc`,
  `int` or `string`" for timestamp out-parameters.

Nothing the plugin implies is *supposed* to appear as a declaration in the render. Two pieces of
knowledge the plugin encodes are absent from both renders and would help a consumer:
the `ConnectionPool` numeric bounds (the record docs state the defaults but not the constraints),
and the per-class legal `get()` type arguments — every one of the 53 `get` methods carries the same
generic doc "Parses returned SQL value to a ballerina value." This is unchanged between `old` and
`new` and is a limitation of the render format, not a defect of either side.

## 8. Other considerations

- **Size.** `new` is +52 % lines, +53 % bytes (37,362 → 56,979). ~19.6 KB of the render is the
  README, identical on both sides; the growth is entirely declaration bodies. For a foundational
  module imported by ~10 other pinned libraries in this batch, the extra ~5 KB of tokens buys the
  `Client` contract and the error hierarchy, which is a good trade.
- **Downstream blast radius.** `sql:Error`, `sql:ParameterizedQuery`, `sql:ExecutionResult`,
  `sql:ProcedureCallResult`, `sql:ConnectionPool` and `sql:Client` are re-exported/implemented by
  `mysql`, `postgresql`, `mssql`, `oracledb`, `java.jdbc`, `snowflake`, `aws.redshift`, `cdc`. In
  `old`, `sql:Error` and all 9 subtypes were `// Unknown type:` lines. The fix is the single most
  valuable change in this render.
- **Version.** 1.19.0 is stable, not deprecated; no deprecation markers found in the bala sources
  (`grep '@deprecated'` → none) and none rendered.
- **Doc quality.** `new` triples the doc-comment content (131 → 353 `#` lines). One doc bug carried
  from the source data: `OutParameter.get` is documented "Parses returned **Char** SQL value to a
  ballerina value." (new:856) on the generic base type.
- **Neither render is compilable Ballerina** (missing `time` import, `= anydata` defaults, stripped
  `typedesc<>`, object types as classes). This is a pre-existing property of the format on both
  sides; `new` is strictly closer to compilable than `old`, which contained the outright
  syntax-error line `returns Error?>;`.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git describe --tags` in `work/sql/src` | `v1.19.0`, HEAD `25fda3a` "[Gradle Release Plugin] - pre tag commit: 'v1.19.0'" |
| 2 | `wc -l old/ballerina_sql.bal.txt new/ballerina_sql.bal.txt` | 1027 / 1551 |
| 3 | `wc -c` on both renders | 37,362 / 56,979 bytes |
| 4 | `grep -c '^// Unknown type:'` | old 113, new 0 |
| 5 | `grep -n '^// --- '` | old 4 markers; new 5 (adds `// --- Annotations ---` at 1548) |
| 6 | `grep -oE '[a-z_]+/[a-z_.]+:[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` | old 18, new 0 |
| 7 | `diff -u old new \| grep '^-' \| grep -v '^---' \| wc -l` | 122 removed lines |
| 8 | same, filtered `grep -v '^-// Unknown type:'` | 9 lines, all listed in §2 |
| 9 | custom `decl.py` declaration extraction, README stripped | old 145 distinct, new 146 distinct |
| 10 | `comm -23 b_old b_new \| grep -v UNKNOWN` | empty — nothing lost |
| 11 | `comm -13 b_old b_new` kinds | 103 class + 10 type + 1 annotation added |
| 12 | `grep -cE '^    (remote )?function '` | old 0, new 122 |
| 13 | `grep -c 'remote function'` | old 0, new 9 |
| 14 | `grep -c '^\s*#'` | old 131, new 353 |
| 15 | `diff <(sed -n '7,450p' old) <(sed -n '7,450p' new)` | identical |
| 16 | Python: JSON `readme`/`description` equality | both `True`; readme 19,793 chars |
| 17 | Python: JSON section sizes | typeDefs 160→160, functions 4→4, clients 0→0, services 0→0, annotations 0→1 |
| 18 | Python: `Counter(t.get('type'))` over typeDefs | old `{Constant:21, Record:11, Class:7, Enum:6, Error:10, Union:2, <none>:103}`; new same but `Class:110`, no `<none>` |
| 19 | Python: typeDef name set difference | empty in both directions |
| 20 | Python: member-function set diff per typeDef | 53 dropped (all `('init','Constructor')`), 14 added |
| 21 | Python: parameters of the 53 dropped constructors | all `[]` — "dropped ctors with params: 0" |
| 22 | Python: `get()` param type/default in both JSONs | `('typeDesc', 'anydata', 'anydata')` identical old and new → extractor-level, not spec-v2 |
| 23 | Python: `generateApplicationErrorStream` return in JSON | old `Error?>`, new `stream<record {\|anydata...;\|}, Error?>` |
| 24 | Python: `CursorOutParameter.get` return in JSON | old `Error?>`, new `stream<rowType, Error?>` |
| 25 | Python: `Error`-typed typeDefs `baseType` | old all `None`, new all populated (10) |
| 26 | Python: scan of every `class` body in `new` for non-function members | 0 found |
| 27 | Python: `class` lines in `new` with no preceding `#` doc | 50 (`InOutParameter` + 49 `*Value`) |
| 28 | `grep -c 'typeDesc = anydata'` / `'typeDesc = <>'` in new | 53 / 1 |
| 29 | `ls …/1.19.0/java21/modules` | `sql` only — single module |
| 30 | public-symbol extraction from 9 bala `.bal` files | 146 symbols; all present in `new` after kind normalisation |
| 31 | `grep '^public configurable' connection-pool.bal` | 16 variables, none in either render |
| 32 | `cat …/compiler-plugin/compiler-plugin.json` | `sql-compiler-plugin`, `SQLCompilerPlugin`, jar `sql-compiler-plugin-1.19.0.jar` |
| 33 | `SQLCompilerPlugin.java:30` | only `addCodeAnalyzer(new SQLCodeAnalyzer())` |
| 34 | `SQLDiagnosticsCodes.java:28-45` | 3 pool codes (SQL_101-103) + 15 out-param type codes (SQL_201-231) |
| 35 | `client.bal:20-82`, `schema_client.bal:19-55`, `error.bal:22-70`, `annotation.bal:17-24`, `types.bal:36,613,1300-1479` | read in full; used for the §3 signature table |
| 36 | `grep 'undefined\|null\|\[object Object\]\|NaN'` on both bodies | 2 hits each, both the legitimate `nullable` field |
| 37 | `LC_ALL=C grep -c '[^ -~]'` | 1 line each side (README smart quotes, new:186) |
| 38 | brace balance in declaration bodies | old 30/30, new 154/154 |
| 39 | `grep '@deprecated'` over bala `.bal` files | none |

## 10. Caveats and unverified items

- Neither render was compiled or type-checked; "non-compiling" claims in §5 (items 2, 3, 7) are
  reasoned from the Ballerina grammar and the source signatures, not from a `bal build` run.
- The bala at `…/distributions/ballerina-2201.13.4/repo/bala/ballerina/sql/1.19.0/java21` was taken
  as authoritative per the brief; I did not re-query Ballerina Central for `ballerina/sql/1.19.0`
  metadata (module list, keywords, deprecation) — the module list was determined from the bala's
  own `modules/` directory instead.
- The 53 removed `init` constructors were removed *at the JSON level*; I confirmed they were zero-arg
  and undeclared in source, but I did not confirm the intent behind the change in the spec-v2
  extractor code (the `ballerina-vscode` sources were not inspected).
- Attribution of §5 items 2, 3, 5 to the Java extractor rests on the two JSON files being identical
  in those fields; I did not read the `CopilotLibraryManager` / docs-model code to confirm the root
  cause.
- The upstream clone was reused from an existing directory in the scratch dir rather than freshly
  cloned; identity was confirmed via `git describe --tags` → `v1.19.0` and HEAD `25fda3a`. The
  compiler-plugin analysis in §7 is from that clone, since the bala ships only the compiled jar.
- `getGlobalConnectionPool` was confirmed public via the JSON and the render; its declaration is at
  `connection-pool.bal:156`.

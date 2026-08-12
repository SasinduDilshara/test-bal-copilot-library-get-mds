# ballerinax/mysql 1.19.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mysql` |
| Pinned version | `1.19.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mysql |
| Tag reviewed | `v1.19.0` (commit `ddd1ebd22e8060710fd16ce75e5a50d1a0f646f9`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mysql/1.19.0/java21` |
| Old render | `886` lines |
| New render | `934` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders are byte-identical for lines 1–827 (whole README section plus every record/enum/union/
constant). All differences sit in the last ~110 lines. `new` is strictly better on every axis that
changed:

- Both `// Unknown type:` degradations (`CdcListener`, `CustomResultIterator`) become real class
  definitions — 8 previously-invisible methods now appear.
- A malformed, non-parseable return type in `old` (`returns Error?>` on `Client.query`) is fixed to
  the correct `stream<rowType, sql:Error?>`.
- A version-qualified type ref (`ballerina/sql:1.19.0:Error?`) is normalised to `sql:Error?`.
- `Client.close()` is corrected from `remote function` to `function` — the library declares it as a
  plain `public isolated function` (`client.bal:110`).
- Service remote-method parameter docs and required/optional parameter hints are added.

No declaration, parameter, default, return type or doc line present and correct in `old` is missing
or degraded in `new`. Remaining inaccuracies in `new` are either shared with `old` (record defaults,
`typedesc` params, a broken doc-comment wrap) or newly *surfaced* pipeline artifacts inside the
`CdcListener.init` line that `old` simply hid behind `// Unknown type:`.

## 2. Change inventory

Counts from `grep -c` on each render (see Evidence log).

| Kind | old | new | delta |
|---|---|---|---|
| `const string` | 7 | 7 | 0 |
| `type` (record + union) | 15 | 15 | 0 |
| `enum` | 1 | 1 | 0 |
| `class` | 0 | 2 | **+2** |
| `client class` | 1 | 1 | 0 |
| `service` block | 1 | 1 | 0 |
| indented member functions | 16 | 24 | **+8** |
| `// Unknown type:` lines | 2 | 0 | **−2** |

Declarations **added** in `new` (10):
- `class CdcListener` with `init`, `attach`, `'start`, `detach`, `gracefulStop`, `immediateStop` (6 methods)
- `class CustomResultIterator` with `nextResult`, `getNextQueryResult` (2 methods)

Declarations **removed** in `new`: none.

Declarations **modified** in `new` (4 lines):
| line | old | new |
|---|---|---|
| `Client.init` return | `ballerina/sql:1.19.0:Error?` | `sql:Error?` |
| `Client.query` return | `Error?>` (malformed) | `stream<rowType, sql:Error?>` |
| `Client.close` | `remote function close()` | `function close()` |
| service listener arg type | `MySqlListenerConfiguration` | `mysql:MySqlListenerConfiguration` |

Doc-only additions in `new`: 17 `# + <param> - <desc>` lines plus 9 `# Required parameters:` /
`# Optional parameters (may be omitted):` lines across the 5 service remote methods.

Underlying JSON diff (normalised, sorted) is 104 lines and contains exactly five changes:
1. `clients[0].functions[init].return.type.name`: `ballerina/sql:1.19.0:Error?` → `sql:Error?`
2. `clients[0].functions[query].return.type.name`: `Error?>` → `stream<rowType, sql:Error?>`
3. `"optional": false` removed from all 5 service methods (no render effect — see §4)
4. `"type": "Class"` added to the `CdcListener` and `CustomResultIterator` typeDefs (this is what
   stops the renderer degrading them)
5. the synthesised `CustomResultIterator.init` constructor entry (return type
   `ballerinax/mysql:CustomResultIterator`) is dropped

`readme` field is byte-identical between the two JSONs; `typeDefs` differ only by item 4 + 5.

## 3. Correctness against library source

The bala module sources are **byte-identical** to the upstream `v1.19.0` tag (`diff -q` on all five
`.bal` files returned "same"), so GitHub and the bala agree.

Verified for every symbol `new` adds or changes:

| Render (new) | Library source | Verdict |
|---|---|---|
| `class CdcListener` | `cdc_listener.bal:19` `public isolated class CdcListener` | exists |
| `attach(cdc:Service s, string[]|string|() name = ())` → `cdc:Error|()` | `cdc_listener.bal:44` | signature matches |
| `'start()` → `cdc:Error|()` | `cdc_listener.bal:51` | matches |
| `detach(cdc:Service s)` → `cdc:Error|()` | `cdc_listener.bal:59` | matches |
| `gracefulStop()` → `cdc:Error|()` | `cdc_listener.bal:66` | matches |
| `immediateStop()` → `cdc:Error|()` | `cdc_listener.bal:73` | matches |
| `init(...)` | `cdc_listener.bal:30` `public isolated function init(*MySqlListenerConfiguration config)` | **mangled — see §5.1** |
| `class CustomResultIterator` | `types.bal:32` `public distinct class CustomResultIterator` | exists |
| `nextResult(sql:ResultIterator) → record {|anydata...;|}|sql:Error|()` | `types.bal:35` returns `record {}|sql:Error?` | equivalent (`record {}` ≡ `record {|anydata...;|}`) |
| `getNextQueryResult(sql:ProcedureCallResult) → boolean|sql:Error` | `types.bal:40` | exact match |
| `Client.init(...) returns sql:Error?` | `client.bal:35-36` returns `sql:Error?` | matches |
| `Client.query(...) returns stream<rowType, sql:Error?>` | `client.bal:54-55` | matches |
| `function close() returns sql:Error|()` (non-remote) | `client.bal:110` `public isolated function close() returns sql:Error?` | matches — `old`'s `remote` was wrong |

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full `diff -u old/ballerinax_mysql.bal.txt new/ballerinax_mysql.bal.txt` — every `-` line is either
  a `// Unknown type:` degradation, a malformed/over-qualified type, or the incorrect `remote` on
  `close`. Nothing correct was deleted.
- Normalised `diff -u` of the two JSONs (104 lines total) — only the five changes listed in §2.
- Declaration-set comparison by kind (§2 table): no kind lost members.
- README section (`old` lines 7–601 vs `new` lines 7–601) — identical; `readme` JSON field identical.
- All 22 `typeDefs` present on both sides with identical names.

Two items examined and rejected as regressions:

- **`"optional": false` dropped from the 5 service methods in the JSON.** No effect on the rendered
  artifact: the renderer only emits a marker for `optional === true` (`to-syntax-string.ts:447`,
  ` // optional`), so `false` and absent render identically. Both renders show all five remote
  functions with no marker. *(Renderer line reference is from the locally available
  `add-service-index` branch, not the exact `new` commit — see Caveats.)*
- **`CustomResultIterator.init` constructor entry dropped from the JSON.** It was a synthesised entry
  with an invalid return type (`ballerinax/mysql:CustomResultIterator`); the class declares no `init`
  in `types.bal:32-44`. It was never rendered in `old` (the class was `// Unknown type:`), so the
  consumed artifact loses nothing.

## 5. Issues in `new` (independent of `old`)

### 5.1 `CdcListener.init` is mangled — newly visible (new-only exposure)

Rendered (`new` line 834):

```
function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {},
  cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d,
  MySqlDatabaseConnection database = {username: "", password: ""}, MySqlOptions options = {},
  MySqlListenerConfiguration config) returns ();
```

Source (`cdc_listener.bal:30`): `public isolated function init(*MySqlListenerConfiguration config)`.

Problems:
- The included-record (`*`) parameter is **flattened into its 6 fields AND also kept as `config`** —
  the same configuration is offered twice.
- Required `config` appears **after** defaultable params → not valid Ballerina; would not compile.
- **Four default values are factually wrong** (checked against `ballerinax/cdc` 1.4.0
  `types.bal:815-821`, the `*cdc:ListenerConfiguration` this record includes):

  | param | rendered default | real default |
  |---|---|---|
  | `engineName` | `""` | `"ballerina-cdc-connector"` |
  | `internalSchemaStorage` | `{}` | `{fileName: "tmp/dbhistory.dat"}` |
  | `offsetStorage` | `{}` | `{fileName: "tmp/debezium-offsets.dat"}` (and it is a union type — `{}` is not a member) |
  | `livenessInterval` | `0.0d` | `60.0` |
- `database` has **no** default in the source (it is required) but is rendered with the fabricated
  default `{username: "", password: ""}`.

This artifact is present identically in **both** JSONs — it is a shared extractor behaviour, not
introduced by spec v2. `old` merely hid it behind `// Unknown type: CdcListener`. It is nonetheless
the one place where `new` can actively mislead an LLM (e.g. suggesting `livenessInterval` defaults to
0 seconds).

### 5.2 Class modifiers and type inclusions dropped

`new` renders `class CdcListener` and `class CustomResultIterator`. Source has
`public isolated class CdcListener` with `*cdc:Listener` (`cdc_listener.bal:19-20`) and
`public distinct class CustomResultIterator` with `*sql:CustomResultIterator` (`types.bal:32-33`).
Member methods lose their `public isolated` qualifiers. Same pattern on `client class Client`
(source: `public isolated client class Client` with `*sql:Client`, `client.bal:22-23`) — shared with `old`.

### 5.3 Shared inaccuracies (identical in `old` and `new`)

Listed for completeness; none of these changed between the two sides.

- **Record defaults erased.** Every defaultable field is rendered as `field?;` with the default value
  dropped: `Options.useXADatasource = false`, `connectTimeout = 30`, `socketTimeout = 0`,
  `noAccessToProcedureBodies = false` (`client.bal:147-151`); `FailoverConfig.failoverReadOnly = true`
  (`client.bal:164`); `SecureSocket.mode = SSL_PREFERRED` (`client.bal:212`);
  `BinlogConfiguration.bufferSize = 8192` (`types.bal:59`);
  `MySqlDatabaseConnection.connectorClass/hostname/port/databaseServerId/tasksMax`
  (`types.bal:90-101`); `DataTypeConfiguration.*` (`types.bal:123-125`);
  `ExtendedSnapshotConfiguration.lockTimeout = 10` (`types.bal:112`).
- **`typedesc` params degraded to value types.** `query` renders
  `record {|anydata...;|} rowType = record {|anydata...;|}` and `queryRow` renders
  `anydata returnType = anydata`; the source declares `typedesc<record {}> rowType = <>`
  (`client.bal:54`) and `typedesc<anydata> returnType = <>` (`client.bal:67`). Inconsistent — `call`
  *does* render `typedesc<record {|anydata...;|}>[] rowTypes = []` correctly (`client.bal:100`).
- **Broken doc-comment wrap.** Render line 665 emits the continuation `from server` without a leading
  `#`, breaking out of the doc comment inside `type SecureSocket` (source doc `client.bal:210-211`).
  Non-compiling as written.
- **Enum body loses values and reorders.** `enum BigIntUnsignedHandlingMode { PRECISE, LONG }` —
  source order is `LONG = "long", PRECISE = "precise"` (`types.bal:26-29`). The string values survive
  only as the separate `const string LONG = "long"` / `PRECISE = "precise"` lines.
- **Record closedness lost.** All source records are closed (`record {| ... |}`); all render as open
  `record { ... }`.
- **Service block is illustrative, not compilable**: `service mysql:Service on new
  mysql:CdcListener(mysql:MySqlListenerConfiguration config = {...})` puts a parameter declaration
  inside a constructor call. Present in both sides; `new` at least qualifies the type consistently.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module (`modules/mysql`), confirmed by both the bala
directory listing and Central metadata (`modules: [{name: "mysql"}]`), so there is no submodule-only
API and the shared `getDefaultModule()` limitation is inert here.

All 21 `public` declarations in the default module are represented in `new`:

`Client`, `Options`, `FailoverConfig`, `FailoverServer`, `SSL_PREFERRED`, `SSL_REQUIRED`,
`SSL_VERIFY_CA`, `SSL_VERIFY_IDENTITY`, `SSL_DISABLED`, `SSLMode`, `SecureSocket`,
`BigIntUnsignedHandlingMode`, `CustomResultIterator`, `ReplicationConfiguration`,
`BinlogConfiguration`, `MySqlListenerConfiguration`, `MySqlDatabaseConnection`,
`ExtendedSnapshotConfiguration`, `DataTypeConfiguration`, `MySqlOptions`, `CdcListener`.

(`new` additionally renders the two enum members `LONG` / `PRECISE` as top-level constants — a
duplication, not a gap.)

`old` had a **member-level** coverage gap: the 8 methods of `CdcListener` and `CustomResultIterator`
were absent. `new` closes it.

Not rendered on either side, correctly: module-private declarations (`ClientConfiguration`,
`createClient`, `nativeBatchExecute`, `init`/`setModule`, and the 9 non-public `populate*` /
`getMillisecondValueOf` helpers in `utils.bal`).

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` in the bala declares
`io.ballerina.stdlib.mysql.compiler.MySQLCompilerPlugin` backed by
`mysql-compiler-plugin-1.19.0.jar`. Upstream sources show 13 Java classes:

- **`InitializerParamAnalyzer`, `RecordAnalyzer`** — compile-time *validation* of `mysql:Options` /
  `mysql:FailoverConfig` numeric fields. Diagnostics (`MySQLDiagnosticsCode.java:31-35`):
  `SQL_101` "expected value is greater than one", `SQL_102` "greater than zero",
  `SQL_103` "greater than or equal to 30", `MYSQL_101` "greater than or equal to zero".
- **`staticcodeanalyzer/`** (`MySQLStaticCodeAnalyzer`, `SecurePasswordAnalyzer`, `MySQLRule`) — one
  `VULNERABILITY`-kind scan rule: `USE_SECURE_PASSWORD` ("A secure password should be used when
  connecting …").

The plugin contributes **no** code actions, no generated artifacts and no annotations, so there is
nothing it implies that the render should carry as a declaration. The render is however *silent* on
these constraints — because §5.3 erases record defaults, an LLM reading the render sees
`decimal connectTimeout?;` with no hint that the plugin errors when it is `<= 0`, or
`int timeBeforeRetry?;` / `queriesBeforeRetry?` with no ">= 0" hint. That is a pre-existing gap
identical on both sides, not a spec-v2 change.

## 8. Other considerations

- **Version / stability**: `1.19.0`, GA, not deprecated (`deprecateMessage: ""` from Central). Built
  for distribution `2201.13.0`. Pull count 158 at time of check.
- **Size**: 886 → 934 lines (+48, +5.4%). The README section is 595 lines (~67% of `old`, ~64% of
  `new`) and unchanged. The extra 48 lines buy 8 real method signatures + 26 doc lines — good value
  per token.
- **Doc quality**: docs are dense and accurate in the source; the render preserves summaries. Record
  field docs survive; function-level `# + param -` docs survive only for the service block (the
  client and class methods render with a bare `# ` continuation line and no parameter docs) — shared
  on both sides.
- **CDC surface**: a large part of the rendered type surface (`MySqlOptions`,
  `MySqlDatabaseConnection`, `ExtendedSnapshotConfiguration`) is flattened `ballerinax/cdc` content
  carrying `// Special Agent Note: … FROM ballerinax/cdc package` markers. That flattening is
  identical in both renders.
- **No encoding issues**: file is clean UTF-8; no mojibake found.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 886 / 934 |
| 2 | `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| 3 | `grep -n '^// --- '` old | README 7, END 601, Types 603, Client 835, Service 869 |
| 4 | `grep -n '^// --- '` new | README 7, END 601, Types 603, Client 865, Service 899 |
| 5 | `diff -u old new` (full) | 2 hunks, first at line 828 → lines 1–827 identical |
| 6 | `ls -R` bala `1.19.0/java21` | `modules/mysql` only; 5 `.bal` files; `compiler-plugin/libs/mysql-compiler-plugin-1.19.0.jar`; `platform/java21/{mysql,sql}-native-1.19.0.jar` |
| 7 | `git ls-remote --tags …module-ballerinax-mysql \| grep 1.19.0` | `refs/tags/v1.19.0` → `ddd1ebd22e8060710fd16ce75e5a50d1a0f646f9` |
| 8 | `git clone --depth 1 --branch v1.19.0` then `diff -q` on all 5 `.bal` files vs bala | all "same" |
| 9 | `cat ballerina/Ballerina.toml` (clone) | `version = "1.19.0"`, `distribution = "2201.13.0"` — pin confirmed on the source side |
| 10 | `grep -nE '^public ' bala/modules/mysql/*.bal` | 21 public declarations (enumerated in §6) |
| 11 | Python: compare JSON top-level keys/lengths | both: typeDefs 22, clients 1, functions 0, services 1, annotations 0 |
| 12 | Python: `a['readme']==b['readme']` | `True` |
| 13 | `diff -u old.norm.json new.norm.json` (sorted, indented) | 104 lines; 5 changes (§2) |
| 14 | Python dump of `CdcListener.init` params (new JSON) | 7 params: 6 flattened `*MySqlListenerConfiguration` fields + trailing `config` |
| 15 | `sed -n '805,825p' cdc/1.4.0/…/types.bal` | `engineName = "ballerina-cdc-connector"`, `internalSchemaStorage = {fileName: "tmp/dbhistory.dat"}`, `offsetStorage = {fileName: "tmp/debezium-offsets.dat"}`, `livenessInterval = 60.0`, `database` (no default) |
| 16 | `client.bal:110` | `public isolated function close() returns sql:Error?` — non-remote → `new` correct |
| 17 | `client.bal:54-55` | `returns stream<rowType, sql:Error?>` → `new` correct, `old` malformed |
| 18 | `types.bal:32-44` | `CustomResultIterator` declares no `init`; 2 public methods match `new` |
| 19 | `cdc_listener.bal:19-75` | 1 `init` + 5 public methods; all 6 present in `new` |
| 20 | declaration counts by `grep -c` per kind | §2 table |
| 21 | `grep -n "optional" to-syntax-string.ts` (local clone) | line 447: `method.optional ? " // optional" : ""` → `false` and absent render identically |
| 22 | `MySQLDiagnosticsCode.java:31-35` | SQL_101/102/103, MYSQL_101 (all ERROR) |
| 23 | `MySQLRule.java:29-31` | one `VULNERABILITY` rule `USE_SECURE_PASSWORD` |
| 24 | `curl api.central.ballerina.io/…/ballerinax/mysql/1.19.0` | 1 module (`mysql`), `deprecateMessage: ""`, ballerinaVersion `2201.13.0`, pullCount 158 |
| 25 | Manual read of `new` lines 598–934 | issues in §5.2/§5.3 identified; no malformed output beyond those |

## 10. Caveats and unverified items

1. **Renderer source not pinned.** The `optional`-flag claim in §4 was checked against
   `/Users/admin/Desktop/Copilot-Changes/ballerina-vscode` at commit `6e88ec675c` on branch
   `add-service-index`. That checkout does **not** contain the two commits under review
   (`git cat-file -t eb5d81b3` and `412ba01e` both returned "Not a valid object name"), so the
   renderer line reference is indicative, not authoritative. The *observable* fact — all 5 remote
   functions appear unmarked in both renders — is directly verified and is what the conclusion rests on.
2. **Neither render was compiled.** Claims that specific lines "would not compile" (§5.1 param order,
   §5.3 broken doc wrap, service block form) are from reading Ballerina grammar rules, not from
   running `bal build` on the rendered text. The renders are illustrative stubs and are not expected
   to compile as-is.
3. **`ballerinax/cdc` defaults** were read from the locally cached bala `cdc/1.4.0`
   (the version pinned in this run's list). The mysql `Dependencies.toml` was not cross-checked to
   confirm 1.4.0 is exactly what the extractor resolved; if a different cdc version were resolved the
   four wrong-default findings in §5.1 could differ in detail, though the `""` / `{}` / `0.0d`
   placeholders are clearly synthesised regardless.
4. **Compiler-plugin behaviour** was read from Java source at the `v1.19.0` tag; the shipped jar in
   the bala was not decompiled to confirm byte-equivalence. All five `.bal` files matched the tag
   exactly, so divergence is unlikely.
5. `platform/java21/*.jar` native implementations were not inspected; render correctness for
   `external` functions was judged from the Ballerina declarations only.

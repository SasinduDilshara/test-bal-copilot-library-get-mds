# ballerinax/oracledb 1.17.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/oracledb` |
| Pinned version | `1.17.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-oracledb |
| Tag reviewed | `v1.17.0` (commit `fc9e194e345f660ed9e85e5f9ed504d0459951da`, grafted shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/oracledb/1.17.0/java21` |
| Old render | `1091` lines |
| New render | `1151` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. The whole diff is 155 unified-diff lines across 5
hunks and consists of four categories, all improvements:

1. Nine `// Unknown type: <Name>` placeholders in `old` are replaced by real `class` definitions with
   docs and methods (9 classes, 8 additional methods).
2. Eight version/module-qualified type references (`ballerina/lang.int:0.0.0:Unsigned32`,
   `ballerinax/oracledb:1.17.0:ArrayValueType?`, `ballerina/sql:1.19.0:Error?`, `ballerinax/cdc:1.4.0:Error?`)
   are normalised to the idiomatic `int:Unsigned32`, `ArrayValueType?`, `sql:Error?`, `cdc:Error?`.
3. A malformed return type in `old` — `remote function query(...) returns Error?>;` — is corrected to
   `returns stream<rowType, sql:Error?>`, which matches the library source exactly.
4. `Client.close()` is no longer mis-labelled `remote`; the source declares
   `public isolated function close()`, so `new` is correct and `old` was wrong.

Nothing was removed. Declaration set of `old` is a strict subset of `new` (verified by sorted
declaration-line diff: `0a1,9`, 9 additions, 0 deletions). README block (lines 7–570) is byte-identical.

The residual defects listed in §5 are extractor-level (present identically in **both** JSONs) and only
became *visible* in `new` because `old` suppressed those types entirely. They are not regressions.

## 2. Change inventory

Counts from `diff -u old new` (155 lines, 5 hunks) and from declaration extraction.

| Kind | old | new | delta |
|---|---|---|---|
| `type` (records/unions/aliases) | 30 | 30 | 0 |
| `enum` | 5 | 5 | 0 |
| `const` | 12 | 12 | 0 |
| `class` (incl. `client class Client`) | 2 | 11 | **+9** |
| `annotation` | 0 | 0 | 0 |
| module-level `function` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 9 | 0 | **−9** |
| version-qualified type refs | 8 | 0 | **−8** |
| `// --- ` section markers | 4 | 4 | 0 |

**Declarations added (9 classes + their members)**

`CdcListener`, `ObjectTypeValue`, `VarrayValue`, `NestedTableValue`, `ObjectOutParameter`,
`XmlOutParameter`, `IntervalYearToMonthOutParameter`, `IntervalDayToSecondOutParameter`,
`CustomResultIterator` — new render lines 1018–1092.

Methods newly surfaced: `CdcListener.init/attach/'start/detach/gracefulStop/immediateStop`,
`ObjectTypeValue.init`, `VarrayValue.init`, `NestedTableValue.init`, `ObjectOutParameter.init`,
`ObjectOutParameter.get`, `XmlOutParameter.get`, `IntervalYearToMonthOutParameter.get`,
`IntervalDayToSecondOutParameter.get`, `CustomResultIterator.nextResult`,
`CustomResultIterator.getNextQueryResult`.

**Declarations removed: 0.**

**Declarations modified (5 signature/type sites)**

| Site | old | new |
|---|---|---|
| `IntervalYearToMonth.years/months` | `ballerina/lang.int:0.0.0:Unsigned32` | `int:Unsigned32` |
| `IntervalDayToSecond.days/hours/minutes` | `ballerina/lang.int:0.0.0:Unsigned32` | `int:Unsigned32` |
| `Varray.elements`, `NestedTableType.elements` | `ballerinax/oracledb:1.17.0:ArrayValueType?` | `ArrayValueType?` |
| `Client.init` return | `ballerina/sql:1.19.0:Error?` | `sql:Error?` |
| `Client.query` return | `Error?>` (malformed) | `stream<rowType, sql:Error?>` |
| `Client.close` | `remote function close()` | `function close()` |

**JSON-level delta** (sorted-key diff of the two `.json` files): `+9` `"type": "Class"` tags on the nine
typeDefs; 8 type-name normalisations; removal of 4 *spurious empty* `init` constructors that `old`
had invented for `XmlOutParameter`, `IntervalYearToMonthOutParameter`,
`IntervalDayToSecondOutParameter` and `CustomResultIterator` (none of which declares an `init` in the
source). Nothing else changed — parameter lists, defaults and docs are byte-identical between the two
JSONs.

## 3. Correctness against library source

The bala's `modules/oracledb/*.bal` are byte-identical to the `v1.17.0` tag (`diff -q` on all six
files returned no differences), so GitHub and the bala agree.

Spot checks of everything `new` adds or changes:

| Render (new) | Source | Verdict |
|---|---|---|
| `class CdcListener { … }` (L1018) | `cdc_listener.bal:20` `public isolated class CdcListener` | exists |
| `attach(cdc:Service s, string[]\|string\|() name = ()) returns cdc:Error\|()` (L1024) | `cdc_listener.bal:45` `attach(cdc:Service s, string[]\|string? name = ()) returns cdc:Error?` | matches |
| `'start()`, `detach()`, `gracefulStop()`, `immediateStop()` returning `cdc:Error\|()` | `cdc_listener.bal:52,60,67,74` | match |
| `class ObjectTypeValue { function init(ObjectType\|() value = ()) }` (L1042) | `types.bal:82,86` | matches |
| `class VarrayValue { function init(Varray\|() value = ()) }` (L1046) | `types.bal:94,98` | matches |
| `class NestedTableValue { function init(NestedTableType\|() value = ()) }` (L1050) | `types.bal:106,110` | matches |
| `class ObjectOutParameter { function init(string typeName); function get(...) returns typeDesc\|sql:Error }` (L1054–1059) | `types.bal:127,131,139` | matches |
| `class XmlOutParameter` with **no** `init` (L1063) | `types.bal:146` — no `init` declared | correct; `old`'s JSON had invented one |
| `IntervalYearToMonthOutParameter`, `IntervalDayToSecondOutParameter` — `get` only | `types.bal:160,174` — no `init` | correct |
| `CustomResultIterator.nextResult(sql:ResultIterator) returns record {\|anydata...;\|}\|sql:Error\|()` (L1089) | `types.bal:189` `returns record {}\|sql:Error?` — `record {}` has an implicit `anydata` rest field | equivalent |
| `CustomResultIterator.getNextQueryResult(sql:ProcedureCallResult) returns boolean\|sql:Error` (L1091) | `types.bal:194` | matches |
| `Client.query(...) returns stream<rowType, sql:Error?>` (L1103) | `client.bal:57-58` `returns stream<rowType, sql:Error?>` | matches — `old` was malformed |
| `Client.init(...) returns sql:Error?` (L1098) | `client.bal:36-38`, defaults `host="localhost"`, `user="sys"`, `port=1521` | matches |
| `function close() returns sql:Error\|()` (L1150) | `client.bal:138` `public isolated function close()` — **not** remote | `new` correct, `old` wrong |
| `int:Unsigned32` on `IntervalYearToMonth`/`IntervalDayToSecond` | `types.bal` uses `int:Unsigned32` | matches |

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff /tmp/old.decl /tmp/new.decl` on the sorted set of top-level declaration lines yields `0a1,9`
  only — nine additions, zero deletions, zero modifications of a declaration's identity.
- The full `diff -u` is 155 lines; every removed (`-`) line was inspected individually. All removals are
  either `// Unknown type:` placeholders, version-qualified type names, the malformed `Error?>`
  fragment, or the incorrect `remote` keyword on `close`.
- README section (render lines 7–570) is identical (`diff` returned empty).
- Sorted-key JSON diff shows zero removed parameters, zero removed defaults, zero removed doc strings
  except the four descriptions that `old` had attached to *fabricated* empty constructors (the same
  descriptions are still present on the class typeDefs in `new`, and are rendered at L1063, L1071,
  L1079, L1087).
- `grep -c '^// Unknown type:'` → old `9`, new `0`.

## 5. Issues in `new` (independent of `old`)

All five are extractor-side (identical in `old`'s JSON) and were merely hidden by `old`'s placeholders.

1. **`CdcListener.init` parameter list is not valid Ballerina and is self-contradictory** (new L1019).
   The source is `public isolated function init(*OracleListenerConfiguration config)` — a single
   included-record parameter. The extractor expands the record's fields into positional parameters
   *and* keeps a trailing `OracleListenerConfiguration config`, producing
   `init(string engineName = "", …, OracleOptions options = {}, OracleListenerConfiguration config)`.
   A required parameter after defaulted ones will not compile, and the same configuration is
   presented twice. Verified identical in both JSONs (`config` param present in `old` too).

2. **Wrong default values on the inherited `cdc:ListenerConfiguration` fields.** Render shows
   `engineName = ""`, `internalSchemaStorage = {}`, `offsetStorage = {}`, `livenessInterval = 0.0d`.
   The real defaults (`ballerinax/cdc:1.4.0` bala, `types.bal:815-822`) are
   `engineName = "ballerina-cdc-connector"`, `internalSchemaStorage = {fileName: "tmp/dbhistory.dat"}`,
   `offsetStorage = {fileName: "tmp/debezium-offsets.dat"}`, `livenessInterval = 60.0`. The extractor
   emitted type-zero placeholders instead. Additionally `database` is a **required** field of
   `OracleListenerConfiguration` (`listener_types.bal:311`) but is rendered with a synthesised default
   `{databaseName: "", username: "", password: ""}`, implying it is optional.

3. **`typedesc<…>` is erased to the bare type in the four new `get()` methods** (L1059, 1067, 1075,
   1083): `function get(anydata typeDesc = anydata)` instead of
   `get(typedesc<anydata> typeDesc = <>)`. Non-compiling as written and misleading about the
   inferred-typedesc idiom. The same erasure already existed on `Client.queryRow`/`query` in both
   renders, so the pattern is shared, but for these four methods it is only visible in `new`.

4. **Class type inclusions are dropped.** `*sql:OutParameter` (on `ObjectOutParameter`,
   `XmlOutParameter`, `IntervalYearToMonthOutParameter`, `IntervalDayToSecondOutParameter`),
   `*sql:TypedValue` (on `ObjectTypeValue`, `VarrayValue`, `NestedTableValue`) and `*cdc:Listener`
   (on `CdcListener`) do not appear anywhere in the render. Consequently an LLM cannot infer that these
   classes are usable as `sql:OutParameter` inside `sql:ParameterizedCallQuery`, that the `*Value`
   classes are `sql:TypedValue`s usable in `sql:ParameterizedQuery`, or that `CdcListener` is a
   `cdc:Listener`. The JSON model has no field for inclusions (typeDef keys are only
   `name`/`description`/`type`/`functions`). Note: *record* inclusions are handled correctly —
   `OracleListenerConfiguration` is flattened with the `cdc:ListenerConfiguration` fields inlined
   (new L944–952).

5. **Public class fields are dropped.** `ObjectTypeValue.value`, `VarrayValue.value`,
   `NestedTableValue.value` (`types.bal:83,95,107`) and `ObjectOutParameter.typeName`
   (`types.bal:129`) are public fields with doc comments; none appear in the render. Same JSON-model
   limitation as (4).

Cosmetic, not counted: the render omits `public`, `isolated` and `distinct` qualifiers on classes.
This is consistent with how `old` rendered `client class Client`, so it is a stylistic convention of
the renderer rather than a defect introduced here.

## 6. Coverage gaps vs. the library

**Zero gaps.** The package has exactly one module — `modules/oracledb` — which is the default module
(`find` on the bala shows `modules/oracledb/{init,cdc_listener,client,listener_types,types,utils}.bal`
and nothing else), so the "submodule API not extracted" shared gap does not apply here.

`grep -hoE '^public (distinct )?(isolated )?(client )?(type|class|enum|const) …'` over the bala's six
`.bal` files yields **38** public top-level symbols. The `new` JSON exposes 50 names
(49 typeDefs + 1 client). `comm -23 src_syms render_syms` → **empty**: every public symbol is present.
The 12 extra names in the render (`HYBRID`, `IN`, `JKS`, `LOGMINER`, `LOGMINER_UNBUFFERED`, `NONE`,
`NUMERIC`, `ONLINE_CATALOG`, `PKCS12`, `REDO_LOG_CATALOG`, `REGEX`, `STRING`) are enum members
additionally surfaced as `const string` declarations (render L574–596) — present identically in both
renders and traceable to real enum members (e.g. `listener_types.bal:36 HYBRID = "hybrid"`).

Not surfaced by either render, but genuinely non-public: the module-private helpers in `utils.bal`
and `init.bal` (`populate*`, `createClient`, `nativeBatchExecute`, `setModule`). Correctly excluded.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` + `libs/oracledb-compiler-plugin-1.17.0.jar` ship in the bala.
Upstream source at `v1.17.0`: `OracleDBCompilerPlugin`, `OracleDBCodeAnalyzer`, and analyzers
`InitializerParamAnalyzer`, `RecordAnalyzer`, `MethodAnalyzer`.

It contributes **validations only** — no code actions, no annotations, no generated artifacts, so there
is nothing the plugin implies that ought to appear in the render. Diagnostics
(`OracleDBDiagnosticsCode.java:35-39`):

- `ORACLEDB_101` — numeric `Options`/`sql:ConnectionPool` fields (`connectTimeout`, `loginTimeout`,
  `maxOpenConnections`, `maxConnectionLifeTime`, `minIdleConnections`) must be `>= 0`.
- `ORACLEDB_201` — the `typedesc` passed to `ObjectOutParameter.get()` must be a record or object.
- `ORACLEDB_202` — the `typedesc` passed to `XmlOutParameter.get()` must be `xml`.

Observation: `ORACLEDB_201/202` are exactly the constraints that issue §5.3 erases — the render's
`get(anydata typeDesc = anydata)` gives no hint that a record/object (resp. `xml`) is required. This is
a shared extractor limitation, not something `new` broke; the docstrings that survive
("Parses the returned Oracle OBJECT SQL value…", "Parses the returned `Xml` SQL value…") partially
compensate. Neither render mentions the `>= 0` constraint on `Options` numeric fields.

## 8. Other considerations

- Version is stable (1.17.0, non-pre-release); Central metadata / bala show no deprecation marker.
- Size: 1151 lines, of which 564 (49%) are the README block, unchanged between sides. `new` adds 60
  lines (+5.5%) — a negligible token cost for recovering nine public classes.
- The nine classes recovered by `new` are not incidental: `ObjectOutParameter`/`XmlOutParameter`/the
  two interval out-parameters are the documented mechanism for Oracle PL/SQL function calls (see the
  `Client.call` docs at new L1119–1144, which reference `ObjectOutParameter` by name). In `old` those
  docs referenced a symbol the render declared "Unknown type", which is actively misleading for an LLM.
  Likewise `CdcListener` — the entire CDC entry point — had zero API surface in `old`.
- The `// Special Agent Note: … FROM <pkg>` trailing comments are applied consistently to the new
  class bodies (e.g. `cdc:InternalSchemaStorage`, `sql:ResultIterator`), matching `old`'s convention.
- Published package matches the tag byte-for-byte; no non-compiling-published-package concern.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 1091 / 1151 |
| `grep -c '^// Unknown type:'` old, new | 9, 0 |
| `grep -n '^// Unknown type:' old` | L1016–1032: CdcListener, ObjectTypeValue, VarrayValue, NestedTableValue, ObjectOutParameter, XmlOutParameter, IntervalYearToMonthOutParameter, IntervalDayToSecondOutParameter, CustomResultIterator |
| `grep -n '^// --- ' old` / `new` | both 4 markers; Types→Client boundary 1034 → 1094 |
| `diff -u old new \| wc -l` | 155 |
| `diff <(sed -n '7,570p' old) <(sed -n '7,570p' new)` | empty — README identical |
| sorted declaration-line diff (`type\|class\|enum\|const\|function`) | `0a1,9` — 9 classes added, 0 removed |
| `grep -cE '^(public )?type '` old/new | 30 / 30 |
| `grep -cE '^(public )?enum '` old/new | 5 / 5 |
| `grep -cE '^(public )?const '` old/new | 12 / 12 |
| `grep -cE 'class '` old/new | 2 / 11 |
| `python3 -m json.tool --sort-keys` + `diff` on both JSONs | +9 `"type":"Class"`; 8 type-name normalisations; −4 fabricated empty `init` constructors; no param/default/doc losses |
| JSON `CdcListener.init` params, old vs new | byte-identical 7-tuple list incl. trailing `('config','OracleListenerConfiguration',None,True)` |
| JSON `clients[0].functions` types, old vs new | identical; `close` = `Normal Function` on both sides |
| `find …/bala/ballerinax/oracledb/1.17.0 -maxdepth 4` | single module `modules/oracledb`; 6 `.bal` files; `compiler-plugin/libs/oracledb-compiler-plugin-1.17.0.jar` |
| `git ls-remote --tags` | `v1.17.0` → `fc9e194e345f660ed9e85e5f9ed504d0459951da` |
| `git clone --depth 1 --branch v1.17.0`; `git log -1` | HEAD = `fc9e194e…`, tag `v1.17.0` |
| `diff -q` bala `.bal` vs `ballerina/*.bal` (6 files) | all identical |
| `ballerina/Ballerina.toml:18` | `version = "1.17.0"` |
| `client.bal:36-38, 57-58, 138` | init defaults; `query` returns `stream<rowType, sql:Error?>`; `close` is `public isolated`, not remote |
| `types.bal:82-115, 127-200` | class/init/get/field declarations for the 8 new type classes |
| `cdc_listener.bal:20-78` | `CdcListener` class + 6 public methods; `init(*OracleListenerConfiguration config)` |
| `listener_types.bal:309-313` | `OracleListenerConfiguration` includes `*cdc:ListenerConfiguration`, `database` required |
| `…/bala/ballerinax/cdc/1.4.0/…/types.bal:815-822` | real `ListenerConfiguration` defaults (`"ballerina-cdc-connector"`, `{fileName: "tmp/dbhistory.dat"}`, `{fileName: "tmp/debezium-offsets.dat"}`, `60.0`) |
| `OracleDBDiagnosticsCode.java:35-39` | ORACLEDB_101 / 201 / 202 |
| `find compiler-plugin/src -name '*.java'` | 9 files; CodeAnalyzer + 3 analyzers, no code actions |
| `comm -23 src_syms.txt render_syms.txt` | empty — 38/38 public default-module symbols covered |
| `comm -13 src_syms.txt render_syms.txt` | 12 enum-member consts, present identically in both renders (L574–596) |

## 10. Caveats and unverified items

- The `--depth 1` clone is grafted, so I verified the tag by commit SHA against `git ls-remote` rather
  than by walking history. The tag→commit mapping was confirmed
  (`refs/tags/v1.17.0^{}` = `fc9e194e…` = cloned HEAD).
- I did not decompile `oracledb-compiler-plugin-1.17.0.jar`; plugin behaviour is taken from the
  upstream `v1.17.0` Java source, which matches the bala's Ballerina sources byte-for-byte, so the jar
  is very likely built from it — but that build correspondence is **unverified**.
- I did not re-run the two-stage render pipeline; the audit compares the supplied JSON/`.bal.txt`
  artefacts. Whether every difference is attributable to the renderer vs. the extractor was determined
  by diffing the two JSONs (e.g. the `remote`→plain `close` change appears only in the renders, not in
  the JSONs, so it is renderer-side).
- Ballerina Central registry metadata was not re-queried over the network; deprecation status is
  inferred from the absence of any deprecation marker in `package.json`/`bala.json` and from the
  upstream tag. Treat "not deprecated" as **unverified against Central**.
- Semantics of `record {}` vs `record {|anydata...;|}` for `CustomResultIterator.nextResult` is argued
  from the Ballerina implicit-rest-field rule, not from a compiler run.

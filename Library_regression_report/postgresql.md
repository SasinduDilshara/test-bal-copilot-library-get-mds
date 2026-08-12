# ballerinax/postgresql 1.19.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/postgresql` |
| Pinned version | `1.19.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-postgresql |
| Tag reviewed | `v1.19.0` (commit `5e7348f`) — upstream `ballerina/*.bal` is **byte-identical** to the bala module sources |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/postgresql/1.19.0/java21` |
| Old render | `1393` lines (49,029 bytes) |
| New render | `1864` lines (68,039 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. All 126 `// Unknown type:` placeholders in `old`
are replaced by real class definitions in `new` (126 → 0), recovering the entire
`sql:TypedValue` / `sql:OutParameter` surface of the connector plus the `CdcListener` class — 126
top-level classes and 133 member functions that `old` rendered as bare comment stubs.

Only four non-placeholder lines changed, and three of them are corrections:
`ballerina/sql:1.19.0:Error?` → `sql:Error?`, a truncated/malformed
`returns Error?>;` → `returns stream<rowType, sql:Error?>`, and `remote function close()` →
`function close()` (source declares `public isolated function close()`, and the README calls
`dbClient.close()`, so `old` was wrong). Zero declarations were removed. The README block
(lines 7–563) and everything up to line 1083 are byte-identical between the two renders.

The newly surfaced material does carry defects, but every one of them originates in the **JSON
extraction stage and is present identically in both `old` and `new` JSON** — spec v2 only made them
visible by rendering the classes at all. They are recorded in §5, not §4.

## 2. Change inventory

Line counts (`wc -l`): old 1393, new 1864 (+471). `diff -u` reports 603 added / 132 removed lines.

### Top-level declarations (body only, i.e. lines after the README block at 563)

| Kind | old | new | Δ |
|---|---|---|---|
| `class` | 0 | 126 | **+126** |
| `client class` | 1 | 1 | 0 |
| `type` (records) | 32 | 32 | 0 |
| `enum` | 4 | 4 | 0 |
| `const` (enum members) | 14 | 14 | 0 |
| `service` | 1 | 1 | 0 |
| `annotation` / `listener` / module-level `function` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | **126** | **0** | −126 |

Removed declarations: **0**. Verified: of the 132 removed diff lines, 126 are `// Unknown type:`
lines, 2 are blanks, and 4 are the replaced lines listed in §3.

### Member functions (indented `function` / `remote function`, body only)

old 13 → new 146 (**+133**). Breakdown of the 146 in `new`: 85 `init`, 42 `get`, 5 `CdcListener`
lifecycle methods (`attach`, `'start`, `detach`, `gracefulStop`, `immediateStop`), 2
`CustomResultIterator` methods (`nextResult`, `getNextQueryResult`), 6 `Client` remote/normal
methods besides `init`, 6 service `remote function on*`.

New member-function names absent from `old`: `'start`, `attach`, `detach`, `get`,
`getNextQueryResult`, `gracefulStop`, `immediateStop`, `nextResult`.

### Modified lines (all 4)

| # | old | new | assessment |
|---|---|---|---|
| 1 | `Client.init ... returns ballerina/sql:1.19.0:Error?` | `... returns sql:Error?` | fixed |
| 2 | `Client.query ... returns Error?>;` | `... returns stream<rowType, sql:Error?>;` | fixed (old was malformed) |
| 3 | `remote function close() returns sql:Error\|()` | `function close() returns sql:Error\|()` | fixed (source is non-remote) |
| 4 | `service ... CdcListener(PostgresListenerConfiguration config = ...)` | `service ... CdcListener(postgresql:PostgresListenerConfiguration config = ...)` | cosmetic; self-module qualification, consistent with the render's `import ballerinax/postgresql;` header |

### Additive documentation in `new`

- 11 `# + <param> - <doc>` lines and 5 `# Required parameters: …` / `# Optional parameters …` hint
  lines, all inside the `// --- Service ---` block (old had 0 of each).
- `Special Agent Note` cross-package annotations: 34 → 85 (all on newly rendered members).

### Size / token implication

Characters 49,013 → 68,021 (×1.39). Modest for a library whose type surface grew from 0 to 126
classes; the added classes are terse (mostly one `init` or one `get` each).

## 3. Correctness against library source

Sources checked: bala `modules/postgresql/{types,procedure_params,client,cdc_listener,listener_types,record_types,utils,init}.bal`
(2,506 lines total), confirmed identical to upstream tag `v1.19.0` `ballerina/*.bal` (8/8 files
`diff`-clean).

**Whole-surface signature check.** I parsed all 127 `public … class` blocks out of the bala sources
and all 127 rendered classes and compared `init` presence and parameter lists programmatically:

- Class name sets are identical (127 vs 127; the only listing difference is `Client`, which the
  render emits as `client class Client`). No invented classes.
- `init` presence: **0 mismatches** across all 127. The 42 classes with no explicit `init` in the
  source (e.g. `IntervalOutParameter`, procedure_params.bal:21–32) correctly have no `init` in the
  render — `new` is *more* faithful here than the old JSON, which carried a synthetic zero-arg
  constructor for those 42.
- `init` parameter lists: after normalising the render's `T|()` ⇄ `T?` and `(T?)[]` ⇄ `T?[]`
  spellings, **all 85 signatures match the source except `CdcListener.init`** (see §5.1) and the 14
  array-union types (§5.2).

Spot checks with citations:

| Symbol | Source | Render | Result |
|---|---|---|---|
| `InetValue.init` | types.bal:22–31 `init(string? value = ())` | new:1462 `init(string\|() value = ())` | match |
| `InetArrayValue.init` | types.bal:33–40 `init(string?[] value = [])` | new:1466 `init((string?)[] value = [])` | match |
| `MoneyArrayValue.init` | types.bal:692–699 `init(decimal?[]\|float?[]\|string?[] value = <string?[]>[])` | new:1690 `init((decimal?)[]\|(float?)[]\|(string?)[] value = …)` | match |
| `InOutParameter` | procedure_params.bal:597–612 (`init(sql:Value 'in)` + `get`) | new:1441–1447 | match |
| `CustomResultIterator` | procedure_params.bal:615–634 (`nextResult`, `getNextQueryResult`, no init) | new:1450–1459 | match (return `record {}` rendered as `record {\|anydata...;\|}`, see §5.6) |
| `CustomTypeValue.init` | types.bal `init(string sqlTypeName, CustomValues? value = ())` | new:1782 | match |
| `EnumValue.init` | types.bal `init(string sqlTypeName, Enum? value = ())` | new:1786 | match |
| `Client.close` | client.bal:112 `public isolated function close() returns sql:Error?` | new:1821 `function close() …` | match (old was `remote`, wrong) |
| `Client.query` | client.bal:57–61 `returns stream<rowType, sql:Error?>` | new:1797 | match (old was `Error?>`, malformed) |
| `Client.init` | client.bal:36–41 | new:1793 | match |
| `CdcListener.attach/'start/detach/gracefulStop/immediateStop` | cdc_listener.bal:43,50,58,65,72 | new (CdcListener block) | match, incl. `cdc:Error?` returns |
| README block | bala `docs/README.md` (23,567 chars) | JSON `readme` field | byte-identical, both sides |

## 4. Regressions

**None found in the render.**

Basis for that conclusion:
- Declaration-set diff (`class|client class|type|enum|const|annotation|listener|service` names,
  sorted) between old and new: 126 additions, **0 removals**.
- Member-function name-set diff: 8 additions, **0 removals**.
- All 132 removed diff lines accounted for: 126 `// Unknown type:` stubs, 2 blank lines, 4 modified
  lines — of which 3 are demonstrable corrections and 1 is a cosmetic module-qualification (table in §2).
- Lines 1–1083 (header, full README, all 32 records, 4 enums, 14 constants) are `diff`-identical.
- Brace balance in the body region: old 49/49, new 180/180 — nothing truncated.
- No version-qualified type refs remain in `new` (old had 1, at old:1343).

One JSON-level delta with **no render impact**, recorded for completeness rather than as a
functional regression:

- `old/ballerinax_postgresql.json` carried `"optional": false` on each of the 6 service methods
  (`onRead`, `onCreate`, `onUpdate`, `onDelete`, `onTruncate`, `onError`); `new` omits the field.
  Since "absent" and "false" are the same default and `toSyntaxString` does not consume the flag,
  both renders emit identical method lists. Not counted as a regression.

Also note the *removal* of 42 synthetic zero-arg `init` constructors from the JSON (§3) is a
correctness gain, not a loss — those constructors do not exist in the library source.

## 5. Issues in `new` (independent of `old`)

All seven items below are also present in the `old` JSON (verified by diffing the two JSON files
field-by-field); `old` simply hid them behind `// Unknown type:`. They are therefore *newly visible*
extractor defects, not renderer regressions — but they are what an LLM now reads.

**5.1 `CdcListener.init` signature is mangled and non-compiling.**
Source (cdc_listener.bal:30) is `public isolated function init(*PostgresListenerConfiguration config)`.
Render emits:
```
function init(string engineName = "", cdc:InternalSchemaStorage internalSchemaStorage = {},
              cdc:OffsetStorage offsetStorage = {}, decimal livenessInterval = 0.0d,
              PostgresDatabaseConnection database = {databaseName: "", username: "", password: ""},
              PostgreSqlOptions options = {}, PostgresListenerConfiguration config) returns ();
```
Two problems: (a) the included-record parameter is expanded into its 6 fields **and** the record
parameter itself is re-appended, so `config` is duplicated; (b) the required `config` parameter
follows defaultable parameters, which is invalid Ballerina. The correct rendering is
`init(*PostgresListenerConfiguration config)`. This is the only signature in the whole library that
disagrees with the source.

**5.2 Fourteen union-of-optional-array types lose parenthesisation (semantically wrong).**
`T?[]` inside a union is emitted as `T|()[]`, which reparses as `T | (()[])` — "T, or an array of
nil" instead of "array of optional T". Affected lines in `new`: 1498, 1506, 1514, 1522, 1530, 1538,
1546, 1602, 1610, 1618, 1626, 1634, 1642, 1650. Example — `TsRangeArrayValue`, source
types.bal:533 `init(TimestampRange?[]|TimestampCivilRange?[]|string?[] value = <string?[]>[])`,
render new:1634 `init(TimestampRange|()[]|TimestampCivilRange|()[]|string|()[] value = <string?[]>[])`.
The defect is in the extractor: the identical string
`"TimestampRange|()[]|TimestampCivilRange|()[]|string|()[]"` is already in `old`'s JSON. Unions of
purely built-in element types are unaffected (`MoneyArrayValue` correctly renders
`(decimal?)[]|(float?)[]|(string?)[]`), so the trigger is a module-defined element type.

**5.3 Eighty-three classes are rendered with no documentation at all.**
97 typeDefs have an empty `description` in the JSON (identical in both sides): the 14 enum-member
constants plus 83 `*Value` / `*ArrayValue` / `InOutParameter` / `CustomTypeValue` / `EnumValue`
classes. Every one of these is documented in the library — e.g. types.bal:19 `# Represents the
`Inet` PostgreSQL type parameter in `sql:ParameterizedQuery`.` — but the render emits a bare
`class InetValue {` (new:1461). The pattern is that a doc comment containing a `# + value - …`
parameter section loses its summary line. The `*OutParameter` classes, whose docs have no `+`
section, keep their descriptions correctly.

**5.4 `CdcListener`'s class description is the constructor's doc, not the class's.**
Source cdc_listener.bal:18 documents the class as "Represents the Ballerina Postgresql CDC
Listener."; the render (and both JSONs) use "Initializes the Postgresql listener with the given
configuration." — the `init` doc from cdc_listener.bal:27.

**5.5 Type inclusions and public fields are dropped for all 127 classes.**
No render carries `*sql:TypedValue` (all `*Value` classes), `*sql:OutParameter` (all
`*OutParameter` classes), or `*cdc:Listener` (`CdcListener`), nor the `public … value;` field each
`*Value` class exposes (e.g. types.bal:35 `public string?[] value;`). Consequence: an LLM reading
the render cannot tell that `postgresql:InetValue` is usable wherever `sql:TypedValue` is expected —
which is the *entire* point of these 85 classes and is exactly what the README's own examples rely on
(new:308–309, 370, 391).

**5.6 `typedesc<…>` parameters are flattened.**
42 `get` methods render `function get(anydata typeDesc = anydata)`; source is
`get(typedesc<anydata> typeDesc = <>)` (procedure_params.bal:28). Likewise `Client.queryRow`
(`anydata returnType = anydata`) and `Client.query` (`record {|anydata...;|} rowType = …` for
`typedesc<record {}> rowType = <>`). The `queryRow`/`query` cases are identical in `old`, so this is
a long-standing renderer convention rather than a spec-v2 change; it now applies to 42 more methods.

**5.7 `record {}` narrowed to `record {|anydata...;|}`.**
`CustomResultIterator.nextResult` returns `record {}|sql:Error?` in source
(procedure_params.bal:621) but `record {|anydata...;|}|sql:Error|()` in the render — a closed
anydata-rest record rather than an open one. Same convention as `Client.query` in both sides.

## 6. Coverage gaps vs. the library

**Zero gaps.** `package.json` declares `"export": ["postgresql"]` — a single module, no submodules,
so the `getDefaultModule()`-only extraction limitation does not bite here.

Enumerated from the bala sources and matched against `new`:

| Public symbol kind | in bala default module | in `new` render |
|---|---|---|
| classes (incl. `Client`) | 127 | 127 |
| records / type defs | 32 | 32 |
| enums | 4 | 4 |
| enum members (as `const`) | 14 | 14 |
| module-level public functions | 0 | 0 |
| annotations | 0 | 0 |

`diff` of the sorted class-name lists and the sorted type-name lists produced no differences other
than `Client` being emitted as `client class`. (Two apparent extra "types", `Student` and `will`,
were false positives from a `^type ` grep landing inside the README code samples at lines 362 and
386 — they are prose/examples, not rendered declarations, and are present identically in `old`.)

Submodule-only API: none — not applicable to this package.

## 7. Compiler plugin

`compiler-plugin.json` → `io.ballerina.stdlib.postgresql.compiler.PostgreSQLCompilerPlugin`
(jar `postgresql-compiler-plugin-1.19.0.jar`). Reading the upstream plugin source at `v1.19.0`:

- `PostgreSQLCompilerPlugin.init` registers **only** `addCodeAnalyzer(new PostgreSQLCodeAnalyzer())`
  — no code modifier, no code actions, no generated artifacts, no annotations.
- `PostgreSQLCodeAnalyzer` registers three syntax-node analysis tasks:
  `InitializerParamAnalyzer` (on `IMPLICIT_NEW_EXPRESSION` / `EXPLICIT_NEW_EXPRESSION`),
  `RecordAnalyzer` (on `LOCAL_VAR_DECL` / `MODULE_VAR_DECL`), `MethodAnalyzer` (on `METHOD_CALL`).
- Diagnostics emitted (all `ERROR`): `SQL_101` value > 1, `SQL_102` value > 0, `SQL_103` value ≥ 30
  (connection-pool sizing / timeouts), `POSTGRESQL_101` value ≥ 0, `POSTGRESQL_102` value > 0
  (e.g. `preparedStatementThreshold`, `preparedStatementCacheQueries`), and `POSTGRESQL_201`–`204`
  (a `CustomTypeValue`/`EnumValue`/`JsonValue`/`PGXmlValue` argument must be string / record-or-string /
  json-or-string / xml-or-string respectively).

Nothing the plugin produces *should* appear in the render — it is validation-only. The value
constraints it enforces are not representable in either render, which is a shared, pre-existing gap
(partly mitigated by the record field docs, e.g. new:751 "A value of 0 for preparedStatementThreshold
disables the cache"). Note that `POSTGRESQL_201`–`204` constrain exactly the `*Value` classes that
`old` did not render at all, so `new` at least gives an LLM the constructor signatures those
diagnostics police.

## 8. Other considerations

- Central metadata for `ballerinax/postgresql/1.19.0`: `deprecated: null`, `deprecateMessage: ""`,
  `visibility: public`, `ballerinaVersion: 2201.13.0`, single module `postgresql`, pullCount 618.
  Not deprecated, stable 1.x.
- Three record fields are `@deprecated` in `PostgresDatabaseConnection` (`pluginName`, `slotName`,
  `publicationName`, listener_types.bal:108–116); both renders carry the `@deprecated` marker plus
  the "Use `replicationConfig.…` instead" doc line (new:753–761). No loss.
- `bala.json` `bala_version: 3.0.0`, `graalvmCompatible: true`.
- Size: `new` is 1.39× `old` in characters. Given the +126 classes this is a good ratio, but note
  that 85 of the added classes are one-line constructors with (per §5.3) no doc text — high symbol
  density, low prose.
- Encoding: the only non-ASCII character in the body region of `new` is an em dash (U+2014) inside
  the comment at new:1857 (`# Required parameters: none — every parameter …`). Harmless.
- Neither render is valid compilable Ballerina as a whole (it is a synopsis format), but `new`'s
  brace balance is clean (180/180) and the two genuinely non-parseable constructs it introduces are
  §5.1 and §5.2.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 1393 / 1864 |
| `wc -c old new` | 49,029 / 68,039 |
| `grep -c '^// Unknown type:'` old / new | 126 / 0 |
| `grep -n '^// --- '` old / new | 5 markers each: README 7, END README 563, Types 565, Client 1339→1789, Service 1373→1823 |
| `diff` lines 1–1083 old vs new | identical |
| `diff` lines 7–563 (README) old vs new | identical |
| `diff -u \| grep '^-'` | 132 lines: 126 `// Unknown type:`, 2 blank, 4 modified (listed in §2) |
| sorted top-level decl-name diff | `0a1,126` — 126 class additions, 0 removals |
| sorted member-fn-name diff | +8 names (`'start`, `attach`, `detach`, `get`, `getNextQueryResult`, `gracefulStop`, `immediateStop`, `nextResult`), 0 removals |
| body decl counts old / new | old: 1 client class, 32 type, 4 enum, 14 const, 1 service; new: same + 126 class |
| body member-fn counts old / new | 13 / 146 |
| brace balance (body) old / new | 49/49 and 180/180 |
| version-qualified refs (`org/mod:x.y.z:`) old / new | 1 (old:1343) / 0 |
| `grep -c '# + '` old / new | 0 / 11 |
| `grep -c '# Required parameters:'` old / new | 0 / 5 |
| `grep -c 'Special Agent Note'` old / new | 34 / 85 |
| `git ls-remote --tags` | `refs/tags/v1.19.0` → `5e7348f` (annotated) |
| `git clone --depth 1 --branch v1.19.0` + per-file `diff` vs bala | 8/8 `.bal` files identical |
| bala `package.json` | `export: ["postgresql"]`, ballerina 2201.13.0, graalvmCompatible true |
| bala `modules/` listing | single dir `postgresql` — no submodules |
| public classes in bala (`grep '^public … class'`) | 127 (126 + `Client`) |
| public records / enums / module functions / annotations | 32 / 4 / 0 / 0 |
| class-name set: bala vs `new` | identical except `Client` rendered as `client class` |
| type-name set: bala vs `new` | identical (32); `Student`/`will` were README-text grep artifacts (new:362, new:386) |
| programmatic `init` presence check, 127 classes | 0 mismatches |
| programmatic `init` param-list check, 85 inits | 1 real mismatch (`CdcListener`), 44 spelling-only (`T?`↔`T\|()`) |
| `grep -c '\|()\[\]'` old / new | 0 / 14 (lines listed in §5.2) |
| JSON `typeDefs` count old / new | 176 / 176, name sets identical |
| JSON `type` field distribution | old: 126 `null`, 32 Record, 14 Constant, 4 Enum → new: 126 **Class**, 32 Record, 14 Constant, 4 Enum |
| JSON typeDefs differing beyond `type` | 42 — all lost a synthetic zero-arg `init` that does not exist in source |
| JSON `clients` diff | 2 fields: `ballerina/sql:1.19.0:Error?`→`sql:Error?`, `Error?>`→`stream<rowType, sql:Error?>` |
| JSON `services` diff | 6 × `"optional": false` dropped from method entries; no render impact |
| JSON `readme` old vs new vs bala `docs/README.md` | all three identical (23,567 chars) |
| JSON typeDefs with empty `description` | 97 (14 constants + 83 classes), identical both sides |
| `client.bal:112` | `public isolated function close()` — non-remote; README uses `dbClient.close()` (README:191,195) |
| `client.bal:57–58` | `returns stream<rowType, sql:Error?>` — matches `new`, not `old` |
| `cdc_listener.bal:30` | `init(*PostgresListenerConfiguration config)` vs render's 7-param expansion |
| Central API `/2.0/registry/packages/ballerinax/postgresql/1.19.0` | `deprecated: null`, 1 module, public |
| compiler-plugin source `v1.19.0` | analyzer-only: 3 syntax tasks, 9 diagnostic codes, no code actions |
| non-ASCII scan of body region in `new` | 1 hit — em dash at new:1857 |

## 10. Caveats and unverified items

- The class-level "no init in source ⇒ no init in render" check treated a class as having a
  constructor only if it declares `public isolated function init(`. All 127 classes in this package
  use exactly that form (verified by counting `function init` occurrences per file), so the check is
  exhaustive here, but it would not catch a non-`isolated` or non-`public` init in another package.
- §5.6's claim that `typedesc<anydata> typeDesc = <>` *should* render differently is a judgement
  about the renderer's convention, not a defect verified against a specification. The convention is
  identical in `old` for `Client.queryRow`, so it is stable behaviour.
- I did not compile either render; "non-compiling" in §5.1/§5.2 is a reading of the Ballerina grammar
  (required-after-defaultable parameter; `|` binding looser than `[]`), not the output of `bal build`.
- The `ballerinax/cdc` defaults reproduced in `CdcListener.init` (`engineName = ""`,
  `internalSchemaStorage = {}`, `offsetStorage = {}`, `livenessInterval = 0.0d`) come from
  `cdc:ListenerConfiguration`, which `PostgresListenerConfiguration` includes
  (listener_types.bal:128). I confirmed the cdc 1.4.0 bala is present locally but did not
  field-by-field verify those four default values against it — they are identical in the `old` JSON
  either way, so they cannot be a spec-v2 regression.
- The two renders were produced by the pipeline before this review; I audited the artefacts and did
  not re-run stage 1 or stage 2, so I cannot independently confirm which `ballerina-vscode` commit
  produced each file beyond what the brief states.

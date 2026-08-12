# ballerinax/java.jdbc 1.15.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/java.jdbc` |
| Pinned version | `1.15.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-java.jdbc |
| Tag reviewed | `v1.15.1` (commit `cac2172f372b4b27f7e4381c2617269db06d7394`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/java.jdbc/1.15.1/java21` |
| Old render | `545` lines |
| New render | `545` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`java.jdbc` is a tiny package: one default module (`java.jdbc`), one source file (`client.bal`, 170 lines),
three public symbols (`Client`, `Options`, `Operations`). The bala's `modules/java.jdbc/client.bal` is
byte-identical to upstream `ballerina/client.bal` at tag `v1.15.1` (`diff` returned no output).

The two renders differ in exactly **3 lines** (6 diff lines, 2 hunks), all inside the `Client` class, and
all three changes are **fixes**:

1. `init` return type `ballerina/sql:1.19.0:Error?` → `sql:Error?` (version-qualified ref removed).
2. `query` return type `Error?>` → `stream<rowType, sql:Error?>` — `old` emitted a **truncated, syntactically
   broken** type; `new` emits the exact source return type.
3. `close` `remote function` → `function` — `old` mislabelled a normal (non-remote) method as remote even
   though its own JSON said `"type": "Normal Function"`; `new` renders it correctly.

No declaration was added or removed. README, type defs, enum, and all other client methods are byte-identical
between the two sides. No regressions found.

## 2. Change inventory

Line counts (`wc -l`): old 545, new 545. Diff: 3 lines changed (`diff | grep -c '^[<>]'` = 6).

| Kind | old | new | added | removed | modified |
|---|---|---|---|---|---|
| Section markers (`// --- `) | 4 | 4 | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | — | — | — |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 | 0 | 1 | — |
| Top-level `const` | 4 | 4 | 0 | 0 | 0 |
| `type` (record) | 1 (`Options`) | 1 | 0 | 0 | 0 |
| `enum` | 1 (`Operations`) | 1 | 0 | 0 | 0 |
| `client class` | 1 (`Client`) | 1 | 0 | 0 | 0 |
| Client methods | 7 | 7 | 0 | 0 | 3 |
| Top-level functions / services / listeners / annotations | 0 | 0 | 0 | 0 | 0 |

JSON level: the only differing top-level key is `clients` (all of `readme`, `description`, `typeDefs`,
`functions`, `services`, `annotations` compare equal in Python). Within `clients`, only two values differ —
`init.return.type.name` and `query.return.type.name`. The `close` change is purely a **renderer** change:
both JSONs already carry `close → "type": "Normal Function"`, so `old`'s `remote function close()` was a
`toSyntaxString` bug, not a data bug.

Modified client methods, exact:

```
old: function init(...) returns ballerina/sql:1.19.0:Error?;
new: function init(...) returns sql:Error?;

old: remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns Error?>;
new: remote function query(sql:ParameterizedQuery sqlQuery, record {|anydata...;|} rowType = record {|anydata...;|}) returns stream<rowType, sql:Error?>;

old: remote function close() returns sql:Error|();
new: function close() returns sql:Error|();
```

## 3. Correctness against library source

Checked against the bala source (`modules/java.jdbc/client.bal`), which is identical to upstream
`ballerina/client.bal` at `v1.15.1`.

| Render symbol | Source | Verdict |
|---|---|---|
| `client class Client` | client.bal:22 `public isolated client class Client` | correct |
| `init(string url, string?, string?, Options?, sql:ConnectionPool?) returns sql:Error?` | client.bal:34–35 | correct in `new`; `old` had the version-stamped return type |
| `query(...) returns stream<rowType, sql:Error?>` | client.bal:56–57 | **correct in `new`**; `old` was `Error?>` (broken) |
| `queryRow(...) returns returnType\|sql:Error` | client.bal:69–70 | correct (identical both sides) |
| `execute(sql:ParameterizedQuery) returns sql:ExecutionResult\|sql:Error` | client.bal:79–80 | correct |
| `batchExecute(sql:ParameterizedQuery[]) returns sql:ExecutionResult[]\|sql:Error` | client.bal:91 | correct |
| `call(sql:ParameterizedCallQuery, typedesc<record{...}>[] rowTypes = []) returns sql:ProcedureCallResult\|sql:Error` | client.bal:104–105 | correct |
| `close() returns sql:Error\|()` | client.bal:114 `public isolated function close()` — **not** remote | **correct in `new`**; `old` wrongly said `remote` |
| `type Options` with `datasourceName?`, `properties?`, `requestGeneratedKeys` | client.bal:127–131 | fields correct; see §5 for default/closedness loss (both sides) |
| `enum Operations {ALL, BATCH_EXECUTE, EXECUTE, NONE}` | client.bal:134–139 (`NONE, EXECUTE, BATCH_EXECUTE, ALL`) | members correct, order alphabetized (both sides) |
| `const string NONE/EXECUTE/BATCH_EXECUTE/ALL` | enum members re-emitted as constants | value-accurate, redundant (both sides) |

Private symbols correctly excluded from both renders: `ClientConfiguration` (client.bal:150), `createClient`
(157), `nativeBatchExecute` (162), `isRequestGeneratedKeysSupportsBatchExecute` (167).

README: `readme` field in both JSONs is 19,517 chars and compares equal to
`docs/README.md` (467 lines) after strip — full fidelity, no truncation on either side.

## 4. Regressions

**None found.** Basis for that conclusion:

- The complete `diff` between the two renders is 3 changed lines (shown in §2); there is nothing else to
  regress. All three changes move `new` **toward** the library source, verified line-by-line in §3.
- No declaration removed: the sorted declaration sets (`const`/`type`/`enum`/`client class`/method names)
  are identical; `diff <(sort old) <(sort new)` yields only those 3 pairs.
- No docs lost: doc comment lines are identical outside the 3 changed signature lines.
- No parameters, defaults, or return types dropped: parameter lists of all 7 methods are byte-identical;
  the two changed return types both became more complete, not less.
- README and `// --- ` section markers unchanged (4 markers on both sides, same line numbers 7/476/478/510).
- `// Unknown type:` count is 0 on both sides, so no type degraded.

## 5. Issues in `new` (independent of `old`)

All five items below are present **identically in `old`**, i.e. they are pre-existing extractor limitations
carried forward, not introduced by spec v2. They matter because they can mislead an LLM.

1. **`Options.requestGeneratedKeys` default `= ALL` lost, and the field is wrongly marked optional.**
   Source (client.bal:130) is `Operations requestGeneratedKeys = ALL;` — a *required* field with a default.
   The JSON has `"optional": true` and no `default`, so the render emits `Operations requestGeneratedKeys?;`.
   An LLM reading this cannot know the default is `ALL`. (new render line 499.)
2. **`Options` closedness lost.** Source is `record {| ... |}` (closed, client.bal:127); render emits
   `type Options record { ... };` (open). Generated code that adds unknown fields would not compile.
3. **`typedesc` inferred-default parameters are mangled into invalid Ballerina.**
   - `query`: source `typedesc<record {}> rowType = <>` → render `record {|anydata...;|} rowType = record {|anydata...;|}`.
   - `queryRow`: source `typedesc<anydata> returnType = <>` → render `anydata returnType = anydata`.
   The `typedesc<>` wrapper is dropped and a *type* is used as a default *expression*; neither line is
   valid Ballerina. Note the inconsistency: `call` (source `typedesc<record {}>[] rowTypes = []`) keeps its
   `typedesc<...>[]` wrapper correctly, so only the inferred-`<>` form is affected.
4. **Enum member order alphabetized.** Render is `ALL, BATCH_EXECUTE, EXECUTE, NONE`; source order is
   `NONE, EXECUTE, BATCH_EXECUTE, ALL` (client.bal:134–139). Harmless for this enum (string-valued), but the
   render no longer reflects declaration order.
5. **Enum members duplicated as top-level constants.** `const string NONE = "NONE";` etc. (render lines
   480–486) plus the `enum Operations` block. Value-accurate but redundant; may invite `NONE` instead of
   `jdbc:NONE`/`Operations` usage.

Additionally (cosmetic, both sides): the class-inclusion `*sql:Client;` (client.bal:23) is not rendered, and
`isolated`/`public` qualifiers are dropped from all methods — consistent with the render format, no
information loss for API-use purposes since all inherited methods are listed explicitly.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module (`modules/java.jdbc`, verified by `ls` and by Central
metadata which lists a single module `java.jdbc`), and that module is the default module — so the
`getDefaultModule()`-only extraction limitation costs nothing here.

Public symbols in the default module: `Client`, `Options`, `Operations` (grep for `^public ` in
client.bal → lines 22, 34, 114, 127, 134). All three appear in both renders, with all 7 public
`Client` methods. No submodule-only API exists.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `java.jdbc-compiler-plugin-1.15.1.jar`; plugin class
`io.ballerina.stdlib.java.jdbc.compiler.JDBCCompilerPlugin` (ballerina/CompilerPlugin.toml).

Contents (upstream `compiler-plugin/src/main/java/io/ballerina/stdlib/java/jdbc/compiler/`):
`JDBCCompilerPlugin`, `JDBCCodeAnalyzer`, `analyzer/InitializerParamAnalyzer`, `JDBCDiagnosticsCode`,
`Constants`, `Utils`.

The plugin contributes **compile-time validation only** — three ERROR diagnostics on `sql:ConnectionPool`
values passed to `Client.init` (`JDBCDiagnosticsCode.java`):
- `SQL_101` maxOpenConnections: "expected value is greater than one"
- `SQL_102` minIdleConnections: "expected value is greater than zero"
- `SQL_103` maxConnectionLifeTime: "expected value is greater than or equal to 30"

No code actions, no generated artifacts, no annotations, no new public symbols. Nothing the plugin implies
is missing from the render — but note that neither render conveys these value constraints (the
`connectionPool` doc string doesn't mention them). That is a shared, pre-existing informational gap, equal on
both sides; an LLM could emit `maxConnectionLifeTime: 10` and get a compile error.

## 8. Other considerations

- Stable release (`1.15.1`), not deprecated (`deprecated: null`, `deprecateMessage: ""` from Central).
  `visibility: public`, `ballerinaVersion: 2201.13.0`, distribution `2201.13.0` in Ballerina.toml.
- Size is unchanged: 545 lines both sides; JSON 28,463 → 28,466 chars (+3). No token-cost implication.
- 87% of the render (lines 7–476 of 545) is README. The actual API surface is ~70 lines. README content is
  preserved verbatim and includes runnable samples, so the render is doc-heavy but useful.
- `old`'s `returns Error?>` was not just imprecise but **non-parseable** — the single most damaging kind of
  content for an LLM consumer, and `new` eliminates it.
- The render's `query`/`queryRow` lines (issue §5.3) remain non-compilable in `new`; that is the one
  remaining syntax-validity defect in this file.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/… new/…` | 545 / 545 |
| `diff old new` | 2 hunks, 3 changed lines (§2) |
| `diff … \| grep -c '^[<>]'` | 6 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 7, 476, 478, 510 — identical |
| `grep -c` version-qualified refs (from precomputed diff, re-verified by reading line 514) | old 1, new 0 |
| `ls -R` bala | one module `java.jdbc`, one file `client.bal`; `compiler-plugin/libs/java.jdbc-compiler-plugin-1.15.1.jar`; `platform/java21/{java.jdbc-native-1.15.1.jar, sql-native-1.19.0.jar}` |
| `wc -l bala modules/java.jdbc/client.bal` | 170 |
| `git ls-remote --tags <repo> \| grep v1.15` | `v1.15.1` exists → `cac2172f372b4b27f7e4381c2617269db06d7394` |
| `git clone --depth 1 --branch v1.15.1` | ok; HEAD = `cac2172…` tagged `v1.15.1` |
| `diff src/ballerina/client.bal bala/modules/java.jdbc/client.bal` | no output → **identical** |
| `cat src/ballerina/Ballerina.toml` | `version = "1.15.1"` → pin confirmed |
| Python JSON key-by-key compare of old/new | only `clients` differs |
| Python diff of `clients` JSON | 2 value changes: `init.return.type.name`, `query.return.type.name` |
| Python dump of client function `type` fields | `close` = `"Normal Function"` in **both** JSONs → `old`'s `remote` was a renderer bug |
| Python dump of `typeDefs` | `Options` (3 fields, all `optional: true`), `Operations` (4 members, alphabetical), 4 string consts — identical both sides |
| Python dump of `query`/`queryRow`/`call`/`init` parameters | as quoted in §5.3 |
| `readme` length vs `docs/README.md` | 19,517 == 19,517; strip-equal `True` |
| `grep -n` on upstream client.bal | line refs used in §3/§5 (23, 34, 56–57, 69–70, 79, 91, 104, 114, 127, 130, 134, 157, 162, 167) |
| `cat JDBCDiagnosticsCode.java`, `grep` `InitializerParamAnalyzer.java` | SQL_101/102/103 ERROR diagnostics; connection-pool validation only |
| `curl` Central `2.0/registry/packages/ballerinax/java.jdbc/1.15.1` | version 1.15.1, not deprecated, single module `java.jdbc`, public |

## 10. Caveats and unverified items

- The claim that `old`'s `remote function close()` came from the renderer (not the extractor) is inferred
  from both JSONs carrying `"type": "Normal Function"` for `close`; I did not read the `toSyntaxString`
  source on either branch to confirm the code path. The end result (render matches source in `new`, not in
  `old`) is directly verified regardless.
- `sql:*` types referenced in signatures (`ConnectionPool`, `ParameterizedQuery`, `ExecutionResult`,
  `ProcedureCallResult`, `Error`) are not expanded in either render — the reader must know `ballerina/sql`.
  I did not audit the `ballerina/sql` 1.19.0 bala to confirm these names, but they match the pinned
  `sql-native-1.19.0.jar` dependency and the source's own references verbatim.
- Compiler-plugin sources were read from the upstream clone, not decompiled from the shipped jar; I assume
  the `v1.15.1`-tagged plugin source corresponds to `java.jdbc-compiler-plugin-1.15.1.jar` in the bala.
- The `render` pipeline itself was not re-run; this audit compares the committed artifacts as given.

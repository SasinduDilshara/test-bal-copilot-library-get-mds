# ballerinax/mongodb 5.2.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/mongodb` |
| Pinned version | `5.2.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-mongodb |
| Tag reviewed | `v5.2.4` (commit `6889f967fefdfcd56348393c49ef98d511ba19f1`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/mongodb/5.2.4/java21` |
| Old render | `608` lines |
| New render | `707` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present in `old` was dropped: the
declaration set is a superset (27 → 29 type/class/enum declarations, 27 → 27 client methods, 10 →
10 constants), and all 9 removed diff lines are lines that `new` replaced with a more accurate
version. Three concrete improvements: (a) the two `// Unknown type:` placeholders for
`DatabaseError` / `ApplicationError` are replaced by real error-type definitions with their doc
comments, (b) all 6 occurrences of version-qualified type refs (`ballerinax/mongodb:5.2.4:Error`,
`…:Index`) are now plain names, (c) 97 `@display` annotations are emitted, all of which match the
library source exactly, and `Collection.name()` is correctly demoted from `remote function` to
`function` (source: `public isolated function name()`).

No regressions found. Several fidelity problems remain in `new`, but every one of them is present
identically in `old` (verified by diff), so they are pre-existing pipeline gaps, not spec-v2
regressions. The single-module package means there is no submodule coverage gap.

## 2. Change inventory

Mechanical (`diff -u old new`): 12 hunks, **108 lines added, 9 lines removed**.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations | 23 (+2 `// Unknown type:` placeholders) | 25 | +2 real defs |
| `enum` | 1 (`ReadConcern`) | 1 | 0 |
| `client class` | 3 (`Client`, `Collection`, `Database`) | 3 | 0 |
| `const` | 10 | 10 | 0 |
| client methods (`function`/`remote function` inside classes) | 27 | 27 | 0 |
| `@display` annotation lines | 0 | 97 | +97 |
| `// Unknown type:` lines | 2 | 0 | −2 |
| version-qualified type refs (`ballerinax/mongodb:5.2.4:`) | 6 (on 5 lines) | 0 | −6 |
| `// --- section ---` markers | 4 | 4 | 0 |
| JSON `typeDefs` / `clients` / `functions` / `services` | 36 / 3 / 0 / 0 | 36 / 3 / 0 / 0 | 0 |

**Added declarations (2):**

```ballerina
# Represents an error caused by an issue related to database accessibility, erroneous queries, constraint violations,
# database resource clean-up, and other similar scenarios.
type DatabaseError error<DatabaseErrorDetail>;

# Represents an error originating from application-level causes.
type ApplicationError error;
```

**Removed declarations: none** (`comm -23 old.decls new.decls` is empty).

**Modified (9 removed lines, all replaced by a better line):**

| old | new |
|---|---|
| `type Error ballerinax/mongodb:5.2.4:DatabaseError\|ballerinax/mongodb:5.2.4:ApplicationError\|error;` | `type Error DatabaseError\|ApplicationError\|error;` |
| `Client.init(...) returns ballerinax/mongodb:5.2.4:Error?` | `... returns Error?` |
| `Collection.init(...) returns ballerinax/mongodb:5.2.4:Error?` | `... returns Error?` |
| `Database.init(...) returns ballerinax/mongodb:5.2.4:Error?` | `... returns Error?` |
| `listIndexes() returns stream<ballerinax/mongodb:5.2.4:Index, error?>\|…` | `stream<Index, error?>\|…` |
| `remote function getDatabase(string databaseName)` | `remote function getDatabase(@display {label: "Database Name"} string databaseName)` |
| `remote function name() returns string;` | `function name() returns string;` |

**Underlying JSON delta** (structural key diff, `old` vs `new`): `new` adds only new keys, removes
none — `/typeDefs[]/annotations`, `/typeDefs[]/fields[]/annotations`, `/typeDefs[]/baseType`,
`/clients[]/annotations`, `/clients[]/functions[]/annotations`,
`/clients[]/functions[]/parameters[]/annotations`.

## 3. Correctness against library source

Upstream `v5.2.4` `ballerina/*.bal` is **byte-identical** to the bala's `modules/mongodb/*.bal`
(all 7 files, `diff -q`), so source citations below apply to both.

| Thing `new` adds/changes | Verified against | Result |
|---|---|---|
| `type DatabaseError error<DatabaseErrorDetail>;` | `errors.bal:26` `public type DatabaseError distinct error<DatabaseErrorDetail>;` | correct except `distinct` dropped (§5.6) |
| `type ApplicationError error;` | `errors.bal:29` `public type ApplicationError distinct error;` | correct except `distinct` dropped |
| `type Error DatabaseError\|ApplicationError\|error;` | `errors.bal:32` | exact match |
| `function name() returns string;` (non-remote) | `collection.bal:35` `public isolated function name() returns string` | **`new` is right, `old` was wrong** |
| `@display {label: "MongoDB Client", iconPath: "icon.png"}` on `Client` | `client.bal:21` | exact match incl. `iconPath` |
| `@display {label: "MongoDB Collection"}` / `{label: "MongoDB Database"}` | `collection.bal:20`, `database.bal:20` | exact match |
| `@display {label: "List Database Names"}` / `"Get Database"` / `"Close the Client"` | `client.bal:47,57,67` | exact match |
| `@display {label: "Database Name"}` on `getDatabase` param | `client.bal:58` | exact match |
| All 97 rendered `label: "…"` values | 98 `label:` occurrences in `client.bal`/`collection.bal`/`database.bal`/`types.bal` | 97/97 rendered labels exist in source; **zero invented labels**. The one source label not rendered is `label: "Database Names"` at `client.bal:49`, a *return-type* annotation — return annotations are not emitted by either renderer |
| `stream<Index, error?>` return of `listIndexes` | `collection.bal:112` | exact match |

## 4. Regressions

**None found.**

Basis for that conclusion:
- `comm -23` of the sorted `type|class|enum` declaration names: empty (nothing in `old` is absent
  from `new`).
- `diff` of the sorted in-class method-name lists: only `remote function name` → `function name`;
  no method lost.
- Constants: identical 10 lines in both (`AUTH_*` ×5, `LOCAL`/`AVAILABLE`/`MAJORITY`/
  `LINEARIZABLE`/`SNAPSHOT` ×5).
- README block (render lines 8–131) is byte-identical to `docs/README.md` (123 lines) in **both**
  renders — no lost README content.
- JSON `typeDefs` count is 36 on both sides with identical name sets.
- All 9 removed diff lines were manually inspected (table in §2); each is superseded by a strictly
  more accurate line.
- No doc-comment text was removed: the only removed lines are declaration lines.

## 5. Issues in `new` (independent of `old`)

All nine below are also present verbatim in `old` (confirmed: they fall outside the 12 diff hunks,
or the diff shows the identical text on both sides). They are pipeline-wide fidelity gaps, listed
because they mislead an LLM consuming the `new` render.

1. **`Client.init` signature is wrong and non-compiling.** Source (`client.bal:28`) is
   `public isolated function init(*ConnectionConfig config) returns Error?`. Render (new:585):
   `function init(ConnectionParameters|string connection = {}, ConnectionProperties options = {}, ConnectionConfig config) returns Error?;`
   — the included-record parameter is expanded *and* kept, a required parameter (`config`) follows
   defaulted ones (illegal), and `connection = {}` invents a default for a field that is required
   in `ConnectionConfig` (`types.bal:24`).
2. **Closed records rendered as open.** 20 of the 22 record types in `types.bal`/`errors.bal` are
   `record {| … |}`; the render emits `record { … }` for all of them (only 4 `record {|` strings
   survive in the new render, all inside `Collection` method parameter types).
3. **Field defaults dropped and defaulted fields marked optional.** 17 fields in `types.bal` have
   defaults; every one is rendered as `?`. E.g. `ServerAddress.host = "localhost"` (`types.bal:35`)
   → `string host?`; `port = 27017` (`:38`) → `int port?`; `FindOptions.sort = {}` (`:246`) →
   `map<json> sort?`; `InsertManyOptions.ordered = true` (`:240`) → `boolean ordered?`.
4. **`readonly` and const references lost on the 5 `authMechanism` fields.** Source:
   `readonly AUTH_PLAIN authMechanism = AUTH_PLAIN;` (`types.bal:57`) → render:
   `"PLAIN" authMechanism?;`.
5. **Malformed rest field.** `Update` has `map<json>...;` (`types.bal:381`); both renders emit
   `# Rest field` / `map<json> ;` (new:551) — invalid syntax.
6. **`distinct` dropped** from `DatabaseError` and `ApplicationError` in `new`'s otherwise-correct
   new definitions. Consumers cannot tell these are distinct error subtypes.
7. **Inferred `typedesc` parameters mangled.** Source `typedesc<record {|anydata...;|}> targetType = <>`
   (`collection.bal:70`) renders as
   `record {|anydata...;|} targetType = record {|anydata...;|}`; `typedesc<anydata> targetType = <>`
   (`:169`, `:199`) renders as `anydata targetType = anydata`. Neither is valid Ballerina and both
   hide that the type is inferred from the LHS.
8. **Broken doc-comment continuation.** New:345–346 — the second line of
   `ConnectionProperties.heartbeatFrequency`'s doc lacks the leading `#`
   (`to determine the current state of each server in the cluster.` at column 0).
9. **Parameter/return doc lines dropped everywhere.** 0 `# + param -` and 0 `return -` lines in
   either render, although every function in `client.bal`/`collection.bal`/`database.bal` documents
   its parameters and return. Also `public` / `isolated` qualifiers are dropped from all classes and
   methods.

Not counted as issues: the README block is emitted as raw (uncommented) Markdown, so the file as a
whole is not compilable Ballerina — that is the format's design and identical in both renders.
Encoding is clean (no non-ASCII bytes in `new`).

## 6. Coverage gaps vs. the library

**Zero.** The bala exports a single module (`package.json` `"export": ["mongodb"]`,
`modules/` contains only `mongodb`), so `getDefaultModule()`-only extraction loses nothing here and
there is no submodule-only API.

Public symbols in the bala default module: 25 `type`, 1 `enum`, 5 `const`, 3 `client class` = 34.
JSON `typeDefs` = 36 (25 types + 1 enum + 10 constants — the 5 `AUTH_*` consts plus the 5
`ReadConcern` members surfaced as consts), `clients` = 3. All 25 types, the enum, all 3 classes and
all 10 constants appear in the `new` render; `old` was missing only `DatabaseError` and
`ApplicationError` (degraded to placeholders). `result_iterator.bal` declares no public symbols.

## 7. Compiler plugin

The package has **no compiler plugin**: no `compiler-plugin/` directory in the bala, no
`compiler-plugin.json`, no `[[plugin]]`/`compiler` entry in `ballerina/Ballerina.toml`, and no
`*-compiler-plugin` module in the repo at `v5.2.4`. The only native artifact is the Java runtime
binding (`platform/java21/mongodb-native-5.2.4.jar` plus the three MongoDB driver jars). Nothing a
plugin would imply is missing from the render.

## 8. Other considerations

- Version is stable (5.2.4, > 1.0), not deprecated in the package metadata; `graalvmCompatible: true`,
  built with `ballerina_version 2201.12.0`.
- Size impact of spec v2 for this library: +99 lines / +3,737 bytes (21,876 → 25,613 bytes), ~+17%.
  97 of the 108 added lines are `@display` annotations. These are IDE-presentation metadata; they
  cost tokens and add little for code generation, but they are accurate and they are the same
  annotations a human sees in the source.
- The two error types that `old` degraded (`DatabaseError`, `ApplicationError`) are referenced by
  the flattened return type of every single remote method
  (`…|DatabaseError|ApplicationError|error`). In `old` an LLM saw those names used 27 times with no
  definition anywhere; `new` fixes that. This is the highest-value change here.
- `Error?` is flattened to `DatabaseError|ApplicationError|error|()` on remote methods but left as
  `Error?` on `init` — inconsistent, on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 608 / 707 |
| `ls -R …/bala/ballerinax/mongodb/5.2.4` | single module `modules/mongodb`, 7 `.bal` files, no `compiler-plugin/` |
| `git ls-remote --tags …module-ballerinax-mongodb \| grep v5.2` | `v5.2.4` → `6889f967fefdfcd56348393c49ef98d511ba19f1` |
| `git clone --depth 1 --branch v5.2.4` | OK |
| `diff -q src/ballerina/<f>.bal bala/modules/mongodb/<f>.bal` ×7 | all `same` |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep -n '^// --- '` | 4 markers both; `Types` at 134 both, `Client` at 487 (old) / 580 (new) |
| `grep -oE 'ballerinax/mongodb:5\.2\.4:' \| wc -l` | old 6, new 0 |
| `grep -c '@display'` | old 0, new 97 |
| `comm` of sorted `label: "…"` strings, source vs new render | 98 in source, 97 in render; only diff = `"Database Names"` (return annotation, `client.bal:49`); none invented |
| `comm -23 old.decls new.decls` (sorted type/class/enum names) | empty |
| `comm -13 old.decls new.decls` | `type ApplicationError`, `type DatabaseError` |
| `diff` of sorted in-class method lists | only `remote function name` → `function name`; 27 methods both |
| `grep -c '^+' / '^-' render.diff` | 108 added / 9 removed (excluding headers); 97 added lines contain `@display` |
| JSON key-path diff old vs new | `new` adds 16 annotation/`baseType` key paths, removes none |
| JSON `typeDefs`/`clients`/`functions`/`services` counts | 36/3/0/0 on both; identical name sets |
| `sed -n '8,131p' new/…bal.txt` vs `docs/README.md` | identical (1 trailing blank line) |
| `collection.bal:35` | `public isolated function name() returns string` — confirms `new` |
| `client.bal:28` | `public isolated function init(*ConnectionConfig config) returns Error?` — confirms §5.1 |
| `errors.bal:26,29,32` | `distinct` present in source, absent in render (§5.6) |
| `grep -hc 'record {\|' types.bal errors.bal` | 20 closed record types in source; 4 `record {\|` in new render |
| `grep -E '^\s+[^#/].* = .*;$' types.bal \| wc -l` | 17 defaulted fields, all rendered `?` |
| `grep -n -B1 '^to determine'` | line 296 (old) / 346 (new) — uncommented doc continuation, both sides |
| `grep -n -A1 'Rest field'` | `map<json> ;` at old:464 / new:551 — both sides |
| `grep -c '^    # + '` and `grep -c 'return -'` | 0 / 0 on both sides |
| `LC_ALL=C grep -nP '[^\x00-\x7F]' new/…bal.txt` | no matches |
| `package.json` | `export: ["mongodb"]`, `graalvmCompatible: true`, `ballerina_version 2201.12.0` |

## 10. Caveats and unverified items

- The claim "every issue in §5 is also in `old`" rests on the unified diff having only 12 hunks and
  those hunks not touching the cited lines; I spot-checked items 5 and 8 by grepping both files
  directly, and items 1–4, 6, 7, 9 by reading the diff context. I did not re-render either side.
- Ballerina compilability of the renders was not tested with a compiler — the "non-compiling"
  judgements in §5 (items 1, 5, 7) are read from the grammar, not from `bal build` output. This
  makes no practical difference since the file also contains raw Markdown and is not meant to
  compile.
- Central registry API was not re-queried; package metadata was read from the bala's
  `package.json`, which is the artifact the pipeline consumed.
- Whether `@display` annotations are net-useful in a Copilot context is a judgement, not a measured
  fact; only their accuracy was verified.

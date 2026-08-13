# ballerina/task 2.11.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/task` |
| Pinned version | `2.11.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-task |
| Tag reviewed | `v2.11.2` (exact tag, commit `892d896`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/task/2.11.2/java21` |
| Old render | `448` lines |
| New render | `477` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. The full `diff` between the two renders is
39 changed lines in 4 hunks: two `// Unknown type:` placeholders (`Error`, `Listener`) are replaced
by real definitions, the `Job` class gains its `execute()` method, and one version-qualified type
reference (`ballerina/task:2.11.2:MysqlConfig|...`) is normalised to `MysqlConfig|PostgresqlConfig`.
Nothing present in `old` is missing, truncated, or made less accurate in `new`.

The added `Listener` class is a real gain (the whole listener API was invisible in `old`), but its
`init` signature as rendered is inaccurate and non-compiling — see §5.1/§5.2. All 10 module-level
functions and all record/enum definitions are byte-identical between the two renders.

## 2. Change inventory

Whole-file diff (`diff old/ballerina_task.bal.txt new/ballerina_task.bal.txt`): 4 hunks,
33 lines added, 4 lines removed.

| Signal | old | new |
|---|---|---|
| Total lines | 448 | 477 |
| `// Unknown type:` placeholders | 2 (`Error`, `Listener`) | 0 |
| Version-qualified type refs (`ballerina/task:2.11.2:X`) | 2 | 0 |
| `// --- section ---` markers | 4 (README, END README, Types, Functions) | 4 |
| Top-level `type`/`class`/`enum`/`const` lines | 25 | 27 |
| Top-level `function` lines | 10 | 10 |

Declaration-set diff (`grep -oE '^(type|class|enum|const|function) NAME' | sort`):

- **Added (2 top-level):** `class Listener`, `type Error`.
- **Removed:** none.
- **Modified (2):**
  - `type DatabaseConfig` — `ballerina/task:2.11.2:MysqlConfig|ballerina/task:2.11.2:PostgresqlConfig`
    → `MysqlConfig|PostgresqlConfig` (old:241 / new:241). Correct per `commons.bal:25`.
  - `class Job` — was empty `{}` (old:342-343); now carries
    `# Executes by the Scheduler...` + `function execute() returns ();` (new:342-346).
- **Added members inside `class Listener` (6 methods + ctor):** `init`, `attach`, `detach`,
  `'start`, `gracefulStop`, `immediateStop` (new:355-375).

JSON-level cause (both `*.json` have 25 typeDefs / 10 functions / 0 clients / 0 services /
0 annotations on both sides). Only 4 typeDefs differ:

| typeDef | change in `new` JSON |
|---|---|
| `DatabaseConfig` | union member names de-qualified |
| `Job` | gains `functions: [execute]` |
| `Error` | gains `"baseType": "error"` |
| `Listener` | gains `"type": "Class"`; return types de-qualified (`ballerina/task:2.11.2:Error?` → `Error?`); the bogus synthetic parameter `"Additional Values" (anydata, "Capture key value pairs")` is **removed** from `init` |

Note `old`'s JSON already contained the full `Listener` data — it lacked `"type": "Class"`, so
`main`'s `renderTypeDef` fell through to `// Unknown type: Listener`. The extraction was never the
problem for this library; the renderer was.

## 3. Correctness against library source

Source verified against both the clone at tag `v2.11.2` and the bala; the five `.bal` files are
byte-identical between the two (`diff -q` on `commons.bal`, `listener.bal`, `scheduler.bal`,
`task_errors.bal`, `init.bal` — no output). Bala exports exactly one module, `task`
(`package.json: "export": ["task"]`), so there is no submodule API and no submodule gap.

Checks on what `new` adds/changes:

- `type Error error;` (new:350) vs `public type Error distinct error;` (`task_errors.bal:19`) —
  exists; `distinct` dropped (§5.4).
- `class Listener` methods vs `listener.bal:21-73`: `attach(Service s, string[]|string? name = ())
  returns Error?` (l.34), `detach(Service s) returns Error?` (l.42), `'start() returns Error?`
  (l.48), `gracefulStop() returns Error?` (l.55), `immediateStop() returns Error?` (l.62) — all five
  match the render exactly (modulo `Error?` rendered as `Error|()` and the dropped
  `public isolated` qualifiers, which is the render's global convention).
- `init` vs `listener.bal:25` `public isolated function init(*ListenerConfiguration config)
  returns Error?` — mismatched, see §5.1/§5.2.
- `class Job { function execute() returns (); }` (new:342-346) vs `public type Job object { public
  function execute(); }` (`commons.bal:134-138`) — method and nil return correct; `object` rendered
  as `class` is the render's convention.
- `DatabaseConfig` union — `commons.bal:25`, correct.
- Unchanged-but-spot-checked module functions (identical text in both renders):
  `configureWorkerPool(int workerCount = 5, time:Seconds waitingTime = 5) returns Error|()`
  (`scheduler.bal:30`), `scheduleOneTimeJob(Job, time:Civil) returns JobId|Error`
  (`scheduler.bal:46`), `scheduleJobRecurByFrequency(Job, decimal, int maxCount = -1,
  time:Civil|() startTime = (), time:Civil|() endTime = (), TaskPolicy taskPolicy = {})`
  (`scheduler.bal:66-67`), `getTimeInMillies(time:Civil) returns int|Error` (`commons.bal:169`),
  `unscheduleJob`/`pauseAllJobs`/`resumeAllJobs`/`pauseJob`/`resumeJob`/`getRunningJobs`
  (`scheduler.bal:93,103,113,124,135,145`). All 10 signatures and defaults match.
- README block (render lines 8-181) is identical in both renders and corresponds to the bala's
  `docs/README.md` (173 lines).

## 4. Regressions

**None found.**

Basis: the complete `diff` of the two renders is reproduced in §2 and contains only 4 removed lines
— `}` (relocated as `Job` gained a body), `// Unknown type: Error`, `// Unknown type: Listener`, and
the version-qualified `DatabaseConfig` line replaced by a correct one. The declaration-set diff shows
zero removals. Lines 1-240 and 242-341 of the two files are identical (`diff` of the README region
reports no differences; the Functions section is untouched). No parameter, default, return type, or
doc line present in `old` is absent from `new`.

## 5. Issues in `new` (independent of `old`)

Items 1-5 are visible only in `new` because `old` rendered nothing for `Listener`/`Error`; items 6-8
are present identically in both renders.

1. **`Listener.init` has a redundant trailing parameter and is non-compiling.** new:355:
   `function init(TriggerConfiguration trigger = {interval: 0.0d}, WarmBackupConfig|() warmBackupConfig = (), ListenerConfiguration config) returns Error?;`
   The real signature is `init(*ListenerConfiguration config)` (`listener.bal:25`). The extractor
   expands the included-record fields *and* keeps the record parameter itself, so the record is
   offered twice. Worse, `config` is emitted as a required parameter *after* two defaulted ones,
   which Ballerina does not allow — an LLM copying this line produces code that will not compile.
   (`old`'s JSON had the same defect plus an extra synthetic `"Additional Values": anydata`
   parameter; `new`'s JSON drops that one, so this is a partial improvement at the JSON level that
   only becomes visible now.)
2. **Invented default on a required field.** `trigger = {interval: 0.0d}` (new:355). In
   `ListenerConfiguration` (`commons.bal:83-86`) `trigger` has **no** default, and inside
   `TriggerConfiguration` (`commons.bal:97-98`) `interval` is a required `decimal`. The render tells
   the model `trigger` is optional and defaults to a zero interval; both are false.
3. **Wrong class-level doc for `Listener`.** new:352 uses `# Initializes the task 'listener.` (the
   `init` doc). The actual class doc is `# Listener for task scheduling.` (`listener.bal:20`); it
   appears nowhere in the render.
4. **`distinct` dropped from `Error`.** new:350 `type Error error;` vs
   `public type Error distinct error;` (`task_errors.bal:19`). Since `task:Error` is the error type
   other code matches on (`is task:Error`), losing distinctness slightly weakens the contract,
   though the name is right.
5. **Parameter docs dropped inside classes.** `Listener`'s methods render only the summary line and
   an empty `# ` (new:357-375); the JSON carries `+ s - The service to be attached`,
   `+ name - The service name`, `+ return - ...` for each. Module-level functions in the same file
   *do* render `# + param -` lines (new:382-383), so this is inconsistent, not a data gap.
6. **`class Service {}` is empty (both renders, new:205-206).** Source is
   `public type Service distinct service object { isolated function execute() returns error?; }`
   (`commons.bal:20-22`). The required `execute()` method a user must implement is not shown, and
   the JSON `Service` typeDef has no `functions` key on either side. For a scheduling library whose
   listener API is "attach a service that implements `execute()`", this is the single most
   consequential inaccuracy remaining.
7. **Record defaults, closedness and `readonly` lost (both renders).** Every defaulted field is
   rendered as optional with no default, e.g. `int port?` (new:219) for `int port = 3306`
   (`commons.bal:38`), `int livenessCheckInterval?` (new:250) for `= 30`, `int maxCount?` (new:277)
   for `= -1`. Closed records `record {| |}` (`TriggerConfiguration`, `RetryConfiguration`,
   `TaskPolicy`, `JobId`) are all rendered as open `record { }`, and `JobId` loses `readonly &`
   (`commons.bal:129`, new:337-339).
8. **Wrapped doc lines break out of the comment (both renders, 6 occurrences each).** Multi-line
   doc continuations lose their `# ` prefix: new:254, 279, 296, 392, 394, 421 (old:254, 279, 296,
   363, 365, 392) — e.g. new:254 `coordinating the task. It is recommended to use a unique
   identifier for each group of tasks.` sits as bare text inside a record body. Same defect,
   unchanged count, in both renders.

## 6. Coverage gaps vs. the library

Default module `task` is the only module in the bala (`modules/task/`), so nothing is submodule-only.

Public symbols in the bala that appear in **neither** render (2):

| Symbol | Source |
|---|---|
| `public configurable int globalSchedulerWorkerCount = 5` | `commons.bal:74` |
| `public configurable time:Seconds globalSchedulerWaitingTime = 5` | `commons.bal:77` |

`grep -n 'globalScheduler'` over both renders returns nothing. Module-level `configurable`
variables are not a category the extractor emits (the JSON has no field for them), so this is a
shared pipeline gap, not a `new`-side regression.

Everything else public is present in `new`: 10 functions, 8 records/type-aliases, 3 enums (plus
their 9 members as `const string`), `Service`, `Job`, `Error`, `Listener`. Member-level gap:
`Service.execute()` (see §5.6).

## 7. Compiler plugin

`has_plugin: false` — confirmed. The bala root
(`.../2.11.2/java21/`) contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json`, `platform/`; there is no `compiler-plugin/` directory and no
`compiler-plugin.json`. The clone at `v2.11.2` has no `*compiler*plugin*` directory and no
`CompilerPlugin.toml` (`find` returned nothing). `ballerina/task` ships only a native Java runtime
(`native/`). Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- Central metadata for `ballerina/task/2.11.2`: `deprecated: null`, `ballerinaVersion 2201.12.0`,
  pull count 54,967, single module `task`. Stable 2.x release, no deprecation notice to surface.
- Size impact is negligible: +29 lines (+6.5%) for the whole listener API, the error type and the
  `Job.execute` method. Good value per token.
- The listener API (`task:Listener`, `ListenerConfiguration`, `WarmBackupConfig`, task coordination)
  is the newest and least-documented part of this module; `old` made it effectively unusable for a
  model since `Listener` was a bare `// Unknown type:` line while the README (rendered identically
  on both sides, lines 109-179) shows `listener task:Listener taskListener = new (...)` examples.
  `new` closes that contradiction — with the caveat that the `init` line it produces is wrong
  (§5.1/§5.2), and the README examples remain the more reliable guide for constructing a listener.
- Render qualifier convention (both sides): `public`, `isolated`, `distinct`, `service object` and
  `configurable` are all dropped globally. Consistent, so not counted as per-symbol defects, but a
  model consuming this render cannot tell isolated from non-isolated API.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.11.2 …/module-ballerina-task` → `git describe --tags` | `v2.11.2`, commit `892d896` |
| `diff -q <clone>/ballerina/*.bal <bala>/modules/task/*.bal` (5 files) | no differences — bala == tagged source |
| `wc -l old/ballerina_task.bal.txt new/ballerina_task.bal.txt` | 448 / 477 |
| `diff old new` (full) | 4 hunks, +33 / −4 lines (reproduced in §2) |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- ' ` old / new | 4 markers each: 7, 182, 184, 349 (old) / 7, 182, 184, 378 (new) |
| `grep -cE '^(type\|class\|enum\|const) '` old / new | 25 / 27 |
| `grep -cE '^function '` old / new | 10 / 10 |
| decl-set diff (`grep -oE '^(type\|class\|enum\|const\|function) NAME' \| sort`) | added `class Listener`, `type Error`; removed none |
| `diff <(sed -n '1,182p' old) <(sed -n '1,182p' new)` | identical README region |
| JSON structure both sides | 25 typeDefs, 10 functions, 0 clients, 0 services, 0 annotations |
| per-typeDef JSON comparison (python) | 4 differ: `DatabaseConfig`, `Job`, `Error`, `Listener`; none missing on either side |
| `grep -nE '^public (isolated )?(function\|type\|class\|enum\|const\|configurable)' <bala>/modules/task/*.bal` | 28 public decls; cross-checked against render |
| `grep -n 'globalScheduler' old new` | no matches in either render |
| `ls <bala>/java21` + `find <bala> -iname '*compiler-plugin*'` | no compiler plugin |
| `find <clone> -name CompilerPlugin.toml` / `-iname '*compiler*plugin*'` | no matches |
| `<bala>/package.json` | `"export": ["task"]` — single module |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/task/2.11.2` | `deprecated: null`, 1 module, ballerinaVersion 2201.12.0 |
| `wc -l <bala>/docs/README.md` | 173 lines, matches rendered README block |
| broken doc-continuation grep | old: lines 254, 279, 296, 363, 365, 392; new: 254, 279, 296, 392, 394, 421 (6 each) |

## 10. Caveats and unverified items

- The two renders were not regenerated by me; I audited the checked-in artefacts under
  `task/old/` and `task/new/` as given. Their provenance (the two `ballerina-vscode` commits in the
  brief) is taken on trust.
- Whether `Listener.init`'s rendered form (`*ListenerConfiguration` expanded **and** retained) is
  specific to `ballerina/task` or a general spec-v2 behaviour for included-record parameters was not
  determined — I did not read the extractor source, only the two JSONs for this library. In both
  JSONs the defect is present at extraction time, so it is not introduced by the renderer change.
- `time:Seconds` / `time:Civil` are rendered with `// Special Agent Note: … FROM ballerina/time
  package` annotations; I verified the referenced symbols exist in `ballerina/time` only by their
  use in the task source (`commons.bal:17,77,100`), not by inspecting the `ballerina/time` bala.
- Compile-validity claims (e.g. required parameter after defaulted parameters in §5.1) are based on
  the Ballerina language rule, not on an actual `bal build` of the rendered text — the renders are
  API stubs and are not compilable as a whole in any case.

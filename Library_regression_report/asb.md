# ballerinax/asb 3.10.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/asb` |
| Pinned version | `3.10.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-asb |
| Tag reviewed | `v3.10.0` (commit `847edd3`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/asb/3.10.0/java21` |
| Old render | `1368` lines (58,113 bytes) |
| New render | `1699` lines (73,526 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Nothing that `old` rendered was lost:
0 declarations removed, 0 doc lines removed, README section byte-identical. The 331-line growth
comes from four things, all verified correct against the bala source:

1. **`@display` annotations are now emitted** — 345 occurrences in `new`, 0 in `old`. All 184
   distinct labels in the render exist verbatim in the bala source; zero invented labels.
2. **Four previously-degraded types are now rendered** — `Error`, `MessageRetrievalError`,
   `AdminActionError`, `Listener`. `old` emitted `// Unknown type: <Name>` for all four
   (4 occurrences → 0). `Listener` gains its 6 methods.
3. **Version-qualified type refs are gone** — 3 occurrences of `ballerinax/asb:3.10.0:Error?` in
   `old`, 0 in `new` (now plain `Error?`).
4. **Two classes of fabricated content in `old` were deleted** — the bogus `anydata Additional
   Values` parameter (10 occurrences in `old`, 0 in `new`) and an invented
   `Caller.init() returns ballerinax/asb:asb:Caller` that does not exist in the source.

Coverage after the change is complete: all 57 public symbols of the default module `asb` appear in
`new`. `old` was missing 4 of them. The package has exactly one module (`asb`), so there is no
submodule gap.

## 2. Change inventory

Computed from `diff -u old new` (1365-line unified diff, 31 hunks; 380 `+` lines, 48 `-` lines).

### Top-level declaration set (extracted, sorted, `comm`-compared)

| | old | new |
|---|---|---|
| Distinct named declarations | 78 | 82 |
| Removed in `new` | — | **0** |
| Added in `new` | — | **4** |

Added: `type Error`, `type MessageRetrievalError`, `type AdminActionError`, `class Listener`.

### Added lines by category (380 total)

| Category | Count |
|---|---|
| `@display` annotation lines (standalone) | 279 |
| `class Listener` block (doc + 6 method decls + braces) | 50 |
| Three error-type definitions + their docs | 6 |
| Rewritten client-method / init signature lines (annotations inlined) | 43 |
| Service-section param doc lines (`# + message -`, `# + asbErr -`) | 2 |

### Removed lines by category (48 total)

| Category | Count |
|---|---|
| `// Unknown type:` placeholders | 4 |
| Old signature lines replaced by annotated equivalents | 43 |
| Invented `Caller.init` declaration | 1 |

Every removed `function`/`remote function` line has a same-named replacement in `new`
(`comm -23` of removed-fn-names vs added-fn-names → empty), except `Caller.init`, which was
correctly deleted (see §4).

### Signal counts

| Signal | old | new |
|---|---|---|
| `// Unknown type:` | 4 | 0 |
| `mod:x.y.z:Type` refs | 3 | 0 |
| `anydata Additional Values` pseudo-params | 10 | 0 |
| `@display` occurrences | 0 | 345 |
| Section markers `// --- ` | 6 | 6 |
| Doc (`#`) lines | 534 | 575 |
| JSON `typeDefs` / `clients` / `functions` / `services` | 76 / 4 / 1 / 1 | 76 / 4 / 1 / 1 |

JSON `typeDefs` kind histogram changed only in one entry: `old` had one typeDef with **no `type`
field** (`Listener`); in `new` it is `Class`. Otherwise identical
(`Record 33, Constant 32, Enum 6, Error 3`).

## 3. Correctness against library source

The bala's `modules/asb/*.bal` is **byte-identical** to the GitHub `v3.10.0` tree
(`ballerina/*.bal`) for all 11 source files — verified with `diff -q` per file, zero differences.
So GitHub and the bala agree and either can be cited.

Verified for each addition in `new`:

| Item in `new` | Source evidence | Verdict |
|---|---|---|
| `type Error error;` | `modules/asb/errors.bal:18` `public type Error distinct error;` | correct except `distinct` (§5.1) |
| `type MessageRetrievalError Error & error<ErrorContext>;` | `errors.bal:21` | correct except `distinct` |
| `type AdminActionError Error & error<AdminErrorContext>;` | `errors.bal:24` | correct except `distinct` |
| `class Listener` with `attach`/`detach`/`'start`/`gracefulStop`/`immediateStop` | `listener.bal:20,52,63,73,83,93` — all 5 are `public isolated function`, signatures match (`attach(Service 'service, string[]\|string? name = ())`, `detach(Service 'service)`, rest nullary), all return `Error?` | correct |
| `Listener` doc block (`listener asb:Listener asbListener = check new (...)`) | `listener.bal:22-32` | verbatim match |
| `@display {label: "Azure Service Bus Administrator", iconPath: "icon.png"}` | `admin.bal:21` | exact |
| `@display {label: "Azure Service Bus Message Receiver", ...}` | `receiver.bal:21` | exact |
| `@display {label: "is Topic Exists"}` + param `@display {label: "Exists"}` on `topicExists` | `admin.bal:172-173` | exact (including the source's own typo "is Topic Exists" / "Exists") |
| `schedule` / `cancel` carry **only** param-level `@display`, no method-level | `sender.bal:84,97` — source has no method-level annotation on either | correct omission |
| `init(@display {label: "Azure Service Bus connection string"} string connectionString) returns Error?` | `admin.bal:34` | exact |

**Exhaustive label check.** All `label: "…"` strings in `new` (184 distinct) were `comm`-compared
against all `label: "…"` strings in the bala source (185 distinct):
- labels present in the render but **not** in the source: **0** (no invented annotations)
- labels present in the source but not in the render: **1** — `label: "Deferred Message"`, which is
  a **return-type** annotation (`receiver.bal:207`). Occurrence-level: source has 350 `@display`
  tokens, `new` has 345; the difference is exactly the 5 return-position annotations at
  `receiver.bal:79, 97, 115, 189, 207`, none of which the renderer emits.

Removals verified as corrections, not losses:
- `Caller` has **no** `init` in the source (`caller.bal:20-58` declares only `complete`, `abandon`,
  `deadLetter`, `defer`). `old`'s `function init() returns ballerinax/asb:asb:Caller;` was an
  invented symbol; `new` drops it. Correct.
- `anydata Additional Values` was leakage from open-record rest fields
  (e.g. `abandon(*record {|anydata...;|} propertiesToModify)` at `caller.bal:36`). It is not a
  parameter and is not even valid Ballerina (space in identifier). `new` drops all 10. Correct.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Declaration-set `comm -23 old new` → empty (nothing removed).
- Doc-line set `comm -23` over all `^\s*#` lines, whitespace-normalised and deduped → empty
  (no documentation text lost).
- README section (lines 1–262) `diff` → identical.
- Every removed `function` name reappears in an added line (set comparison → empty difference);
  the single genuine deletion (`Caller.init`) is a correction, verified against `caller.bal`.
- Section markers: same 6 in both, same order.
- JSON payloads: identical array lengths for `typeDefs`, `clients`, `functions`, `services`.
- No new `// Unknown type:` lines, no new version-qualified refs, no truncation.
- Client method count and per-class membership unchanged for `Administrator`, `Caller`,
  `MessageReceiver`, `MessageSender`; only annotations were added to their signatures.

## 5. Issues in `new` (independent of `old`)

Ten inaccuracies exist in `new` relative to the library source. Four are in content `new` newly
introduces; six are pre-existing renderer limitations shared with `old` (marked *shared*), listed
here because the brief asks for correctness of `new` regardless of `old`.

1. **`distinct` dropped from all three error types.** Source: `public type Error distinct error;`
   (`errors.bal:18`), `public type MessageRetrievalError distinct Error & error<ErrorContext>;`
   (`errors.bal:21`), `public type AdminActionError distinct Error & error<AdminErrorContext>;`
   (`errors.bal:24`). Render (`new` lines 357, 381, 396) omits `distinct`. This changes error
   subtyping semantics — an LLM could conclude any `error` is assignable to `asb:Error`.
   *(new-side content; `old` rendered nothing at all here, so still net-better.)*
2. **`Listener.init` fabricates a default for a required field.** Render (`new:1271`) shows
   `string connectionString = ""`. Source `ListenerConfiguration` includes
   `*ASBServiceReceiverConfig` whose `connectionString` has **no** default (`types.bal:128`).
   *(new-side content.)*
3. **`Listener.init` shows a wrong default.** Render: `int maxAutoLockRenewDuration = 0`. Source:
   `int maxAutoLockRenewDuration = 300;` (`types.bal:134`). This is a factually incorrect value,
   not just a missing one. *(new-side content.)*
4. **Return-position `@display` annotations are never emitted** — 5 in the source
   (`receiver.bal:79, 97, 115, 189, 207`), 0 in the render. Cosmetic. *(new-side feature gap.)*
5. *shared* — **Included-record parameters (`*T`) are expanded into pseudo-parameters and the
   record parameter is ALSO appended.** e.g. source `createTopic(string topicName,
   *CreateTopicOptions topicOptions)` (`admin.bal:47`) renders as 16 individual defaulted params
   **plus** a trailing required `CreateTopicOptions topicOptions`. A required parameter after
   defaultable parameters is not valid Ballerina, and the arguments are duplicated. Affects 8
   `Administrator` methods, `Caller.deadLetter`, and `Listener.init`. Present identically in `old`.
6. *shared* — **Optional record fields become params with invented zero-value defaults.** All
   `CreateTopicOptions` fields are optional (`types.bal:507-537`, every field ends `?`), yet the
   render assigns `= 0`, `= ""`, `= {}`, `= "Unknown"`.
7. *shared* — **`MessageReceiver.receive` defaults and typedesc are wrong.** Source:
   `receive(int? serverWaitTime = 60, typedesc<Message> T = <>, boolean deadLettered = false)`
   (`receiver.bal:76-78`). Render: `receive(int|() serverWaitTime = (), Message T = asb:Message,
   boolean deadLettered = false)` — the `60` default is lost and `typedesc<…>` is flattened. Same
   for `receivePayload`.
8. *shared* — **`public` and `isolated` qualifiers are not emitted anywhere** (`grep -c '^public '`
   = 3 in both files, all from README code blocks; `isolated` = 2 in both, also README). Everything
   in the library is `public isolated`.
9. *shared* — **`Service` is rendered as `class Service {}`** though the source is
   `public type Service distinct service object { … }` (`service_types.bal:18`). The object's
   remote methods are commented out in the source, so an empty body is defensible, but `class` is
   the wrong construct.
10. *shared* — **Multi-line doc comments lose the `#` prefix on continuation lines.** e.g.
    `new:502-508` (and `old:441-447`): only the first line of the `connectionString` doc carries
    `#`; lines 503–507 start at column 0. The rendered text is therefore not compilable Ballerina.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.**

Public symbols of the default module were extracted from the bala
(`grep -hoE '^public …' modules/asb/*.bal` → 57 names) and compared against names parsed out of
each render:

- Missing from `new`: **0**
- Missing from `old`: **4** — `Error`, `MessageRetrievalError`, `AdminActionError`, `Listener`

The extra names in the render beyond the 57 are the 24 enum members (rendered as `const string`
alongside their `enum` declarations, e.g. `enum LogLevel` at `new:620` with `DEBUG…OFF`) plus
`main` from a README code block — all legitimate.

**No submodule gap.** `package.json` declares `"export": ["asb"]`; the bala contains exactly one
module directory (`modules/asb`); Central metadata for `ballerinax/asb/3.10.0` lists a single
module `asb`. The `getDefaultModule()`-only extraction therefore captures the entire public API.

## 7. Compiler plugin

**The package ships no compiler plugin.** Evidence:
- No `compiler-plugin/` directory and no `compiler-plugin.json` in the bala
  (`ls` of the bala root shows only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
  `package.json`, `platform`, `resources`).
- No `[[tool…]]`/`compilerPlugin` entry in `ballerina/Ballerina.toml` at `v3.10.0`.
- `find` for `*compiler-plugin*` / `*compiler_plugin*` in the upstream tree returns nothing; the
  only Java module is `native/` (the `asb-native` JNI runtime, `org.ballerinax:asb-native:3.10.0`).

Consequently there are no plugin-contributed code actions, validations, or generated artifacts that
should have surfaced in the render, and nothing is missing on that axis.

## 8. Other considerations

- **Not deprecated.** Central `deprecated: null`, `deprecateMessage: ""`, `graalvmCompatible: Yes`,
  `pullCount: 500`, single license `Apache-2.0`.
- **Stable major version** (3.10.0), built against distribution `2201.13.0`.
- **Size/token impact:** +331 lines / +15.4 KB (+26.5% bytes). 279 of the 380 added lines are
  standalone `@display` annotations. These carry graphical-editor labels and are of marginal value
  to an LLM generating code, so most of the size increase buys little for code generation — but the
  genuinely valuable additions (`Listener` + its 6 methods, three error types, removal of 10 bogus
  parameters and one invented `init`) are worth far more than their ~60 lines.
- **`Listener` being renderable at all is the headline win.** `ballerinax/asb` is a trigger-type
  connector; without `class Listener` an LLM had no way to see `attach`/`detach`/`'start`/
  `gracefulStop`/`immediateStop`, and `old` reduced the whole class to one comment line.
- **The Service section improved too:** `new` module-qualifies the types
  (`asb:ListenerConfiguration`, `asb:Message`, `asb:MessageRetrievalError`) where `old` left them
  bare, and adds the `# + message -` / `# + asbErr -` parameter docs.
- **Neither render is compilable Ballerina** (issues 5, 6, 8, 10 above). That is a property of the
  format, not of this change.
- No encoding artefacts observed; both files are clean UTF-8.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 1368, new 1699 |
| 2 | `wc -c` on both renders | old 58,113 B, new 73,526 B |
| 3 | `grep -n '^// --- '` both | 6 markers each, same order (README/END README/Types/Client/Functions/Service) |
| 4 | `grep -c '^// Unknown type:'` | old 4, new 0 |
| 5 | `grep -n '^// Unknown type:' old` | lines 332 `Error`, 350 `MessageRetrievalError`, 362 `AdminActionError`, 1016 `Listener` |
| 6 | `grep -nE '[a-zA-Z_.]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 3 hits (lines 1023, 1216, 1303, all `ballerinax/asb:3.10.0:Error?`); new 0 |
| 7 | `git ls-remote --tags …module-ballerinax-asb` | `v3.10.0` exists → `847edd3` |
| 8 | `git clone --depth 1 --branch v3.10.0` then `git log -1` + `gradle.properties` | commit `847edd3`, `version=3.10.0` — exact tag |
| 9 | `diff -q` bala `modules/asb/*.bal` vs repo `ballerina/*.bal`, 11 files | zero differences — bala == GitHub tag |
| 10 | `diff -u old new > full.diff; wc -l` | 1365 lines, 31 hunks |
| 11 | `grep -c '^+' / '^-'` on full.diff | 380 added, 49 (incl. `---` header) → 48 real removals |
| 12 | `grep '^+' \| grep -cE '^\+\s*@display'` | 279 of 380 added lines are pure `@display` |
| 13 | Declaration-name extraction + `comm` (old vs new) | removed 0; added 4 (`class Listener`, `type Error`, `type MessageRetrievalError`, `type AdminActionError`) |
| 14 | `comm -23` of removed-fn-names vs added-fn-names | empty — every removed function reappears |
| 15 | `diff` of README region (lines 1–262) | IDENTICAL |
| 16 | `grep -c '^\s*#'` doc lines | old 534, new 575 |
| 17 | `comm -23` of deduped doc lines old vs new | empty — no doc text lost |
| 18 | `grep -c 'Additional Values'` | old 10, new 0 |
| 19 | `grep -c '@display'` (lines) / `grep -o` (occurrences) | new 315 lines / 345 occurrences; old 0 / 0 |
| 20 | `comm` of 184 render labels vs 185 source labels | 0 invented; 1 source-only (`"Deferred Message"`, return position) |
| 21 | `grep -hn 'returns @display' modules/asb/*.bal` | 5 hits (receiver.bal 79, 97, 115, 189, 207) = exactly the 350−345 delta |
| 22 | Public-symbol extraction from bala (57 names) vs render names | missing from new: 0; missing from old: 4 |
| 23 | JSON top-level key + array-length comparison | identical: typeDefs 76, clients 4, functions 1, services 1; keys identical |
| 24 | JSON `typeDefs` kind histogram | old `{Record 33, Constant 32, Enum 6, Error 3, Class 1, <no type> 1}`; new `{… Class 2}` — the untyped entry is `Listener` |
| 25 | `admin.bal:21,34,47,172-173` | `@display` on class, `init`, `createTopic(*CreateTopicOptions)`, `topicExists` — all match `new` |
| 26 | `caller.bal:20-58` | no `init`; `abandon`/`defer` take `*record {\|anydata...;\|}`; `deadLetter` takes `*DeadLetterOptions` |
| 27 | `errors.bal:17-24` | three `distinct` error types — `distinct` absent in render |
| 28 | `listener.bal:20,35,52,63,73,83,93` | `init(*ListenerConfiguration)` + 5 public methods — all present in `new` |
| 29 | `types.bal:126-137` (`ASBServiceReceiverConfig`) | `connectionString` required, `maxAutoLockRenewDuration = 300` — render shows `= ""` and `= 0` |
| 30 | `types.bal:507-537` (`CreateTopicOptions`) | all 16 fields optional (`?`) — render invents zero-value defaults |
| 31 | `receiver.bal:76-79` | `int? serverWaitTime = 60`, `typedesc<Message> T = <>` — render shows `int\|() … = ()`, `Message T = asb:Message` |
| 32 | `service_types.bal:18` | `public type Service distinct service object {…}` — render shows `class Service {}` |
| 33 | `sender.bal:84,97` | `schedule`/`cancel` have only param-level `@display` — render matches |
| 34 | `utils.bal:22` | `public isolated function getApplicationPropertyByName(Message, string) returns anydata\|error?` — matches both renders |
| 35 | `ls` bala root + `find` upstream for `*compiler-plugin*` + `Ballerina.toml` | no compiler plugin anywhere |
| 36 | `package.json` `export` + `ls modules/` | single module `asb` — no submodule gap |
| 37 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/asb/3.10.0` | not deprecated, 1 module, graalvmCompatible Yes, pullCount 500 |
| 38 | `sed -n '502,509p' new` / `441,447p' old` | multi-line doc continuation lines lack `#` in both |

## 10. Caveats and unverified items

- The manifest lists `central_source` as `module-ballerinax-azure-service-bus` while the manifest
  `repo` field is `module-ballerinax-asb`. Both hostnames resolve to the same repository content —
  `git ls-remote --tags` returns the identical `v3.10.0` object id (`53cedbf…` / `847edd3…`) for
  both URLs, so the rename is a GitHub redirect and the reviewed tree is correct either way.
- I did not execute the two-stage render pipeline myself; the analysis compares the two supplied
  `.bal.txt` / `.json` artefacts. That the artefacts were produced from the stated
  `ballerina-vscode` commits is taken from the brief and is **unverified** by me.
- `class Service {}` renders with an empty body. Because the source's remote-method declarations
  are commented out in `service_types.bal`, I could not determine whether an ideal renderer would
  emit `onMessage`/`onError` on the type itself — the Service *section* does emit them, sourced
  from trigger metadata rather than from the module. I have not inspected the trigger-metadata
  source, so the provenance of that section is unverified.
- The rendered defaults for included-record expansion (issue 5/6) were spot-checked against
  `CreateTopicOptions`, `ListenerConfiguration`, `ASBServiceReceiverConfig` and `DeadLetterOptions`;
  I did not verify every one of the 8 `Administrator` option records field-by-field, though all
  8 follow the identical all-optional-fields pattern.

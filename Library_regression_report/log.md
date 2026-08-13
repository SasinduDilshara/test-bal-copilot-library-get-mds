# ballerina/log 2.17.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/log` |
| Pinned version | `2.17.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-log |
| Tag reviewed | `v2.17.0` (commit `6c2b68b58ba43bcdfa1aced0efb8c3382f36bf0e`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/log/2.17.0/java21` |
| Old render | `628` lines (19,349 bytes) |
| New render | `676` lines (21,231 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` on this library. All 16 removed lines are defects: 3
`// Unknown type:` placeholders, 5 lines carrying 7 version-qualified type references
(`ballerina/log:2.17.0:Type`), and 8 lines (4 signatures + 4 doc lines) carrying a fabricated
parameter `Value Additional Values` — an identifier with a space in it, which is not valid
Ballerina. `new` adds 64 lines: real definitions for `Error`, `Valuer`, `ReplacementFunction`;
the 7 methods of the `Logger` object type and the 2 methods of `LoggerRegistry` (both classes
were rendered as empty bodies in `old`); and a new `// --- Annotations ---` section carrying
`public annotation SensitiveConfig Sensitive on record field`, which `old` omitted entirely
(`annotations` array is `[]` in the old JSON, length 1 in the new one).

No declaration present in `old` is missing, truncated, or made less accurate in `new`. The
README block (lines 1–285, 7,699 chars) is byte-identical on both sides and byte-identical to
the bala `docs/README.md`. Remaining inaccuracies (§5) are almost all shared with `old` and are
renderer-level, not introduced by spec v2; the one genuinely new-side-only fidelity loss worth
noting is that the newly emitted class methods omit their `# + param -` doc lines even though
those descriptions are present in the new JSON.

## 2. Change inventory

Mechanical (`diff old new`): **64 lines added, 16 removed, 11 hunks**. Verified independently:
`diff | grep -c '^>'` = 64, `grep -c '^<'` = 16, `diff -u | grep -c '^@@'` = 11 — matches
`OLD_AND_NEW_DIFFS/log_diff.md`.

Signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` | 3 | 0 |
| `ballerina/log:2.17.0:` occurrences | 7 (on 5 lines) | 0 |
| `// --- ` section markers | 4 (README, END README, Types, Functions) | 5 (+ Annotations) |
| JSON `annotations` array | 0 entries | 1 entry (`Sensitive`) |
| JSON `typeDefs` / `functions` | 39 / 11 | 39 / 11 (identical names, identical order) |

### Added (13 declarations)

| Kind | Name | Was in `old` |
|---|---|---|
| type (error) | `Error` | `// Unknown type: Error` |
| type (function) | `Valuer` | `// Unknown type: Valuer` |
| type (function) | `ReplacementFunction` | `// Unknown type: ReplacementFunction` |
| class method | `Logger.printDebug` / `.printInfo` / `.printWarn` / `.printError` / `.withContext` / `.getLevel` / `.setLevel` (7) | `class Logger {}` empty |
| class method | `LoggerRegistry.getIds` / `.getById` (2) | `class LoggerRegistry {}` empty |
| annotation | `Sensitive` | absent (no Annotations section) |

### Removed (0 declarations)

Zero. The 16 removed lines are: 3 `// Unknown type:` markers, 4 `# + Additional Values - Capture
key value pairs` doc lines, 4 `printDebug/printError/printInfo/printWarn` signatures (re-emitted
correctly), and 5 lines with version-qualified refs (`Value`, `OutputDestination`,
`Config.destinations`, `Config.keyValues`, `MaskingStrategy`, all re-emitted with plain names).

### Modified

- 4 print functions: bogus param `Value Additional Values` dropped. Confirmed at the JSON layer —
  `old/ballerina_log.json` `printDebug.parameters` has 5 entries including
  `{"name":"Additional Values","type":{"name":"Value"}}`; `new` has 4, matching the source's
  `(msg, 'error, stackTrace, *keyValues)`.
- 7 type references de-qualified: `ballerina/log:2.17.0:Valuer` → `Valuer`, etc.
- JSON gained `baseType` on the three `Error`/`Other` typeDefs and `functions` arrays on the two
  `Class` typeDefs; that is the mechanism behind every render addition above.

## 3. Correctness against library source

The bala module sources are **byte-identical** to the upstream `v2.17.0` tag — verified with
`diff -q` on all six files (`logger.bal`, `init.bal`, `natives.bal`, `root_logger.bal`,
`sensitive_data_masking.bal`, `log_errors.bal`): all IDENTICAL. So GitHub and bala agree and
either can be cited.

Every addition in `new` checked against source:

| New render | Source | Correct? |
|---|---|---|
| `type Error error;` (line 336) | `log_errors.bal:18` `public type Error distinct error;` | type is right, `distinct` dropped (see N1) |
| `type Valuer function () returns anydata;` (386) | `natives.bal:46` `public type Valuer isolated function () returns anydata;` | yes, minus `isolated` |
| `type ReplacementFunction function (string input) returns string;` (545) | `sensitive_data_masking.bal:23` | yes, minus `isolated` |
| `Logger.printDebug/printInfo/printWarn/printError(string\|PrintableRawTemplate msg, error\|() 'error = (), error:StackFrame[]\|() stackTrace = (), KeyValues keyValues) returns ()` (343–355) | `logger.bal:25,33,41,49` `public isolated function printX(string\|PrintableRawTemplate msg, error? 'error = (), error:StackFrame[]? stackTrace = (), *KeyValues keyValues)` | types and defaults match (`error?` ≡ `error\|()`); `*` and `isolated` dropped |
| `Logger.withContext(KeyValues keyValues) returns Logger\|error` (359) | `logger.bal:55` | yes |
| `Logger.getLevel() returns Level` (365) | `logger.bal:62` | yes |
| `Logger.setLevel(Level level) returns error?` (372) | `logger.bal:71` | yes |
| `LoggerRegistry.getIds() returns string[]` (537) | `root_logger.bal:60` | yes |
| `LoggerRegistry.getById(string id) returns Logger\|()` (541) | `root_logger.bal:66` `returns Logger?` | yes (`?` ≡ `\|()`) |
| `public annotation SensitiveConfig Sensitive on record field;` (676) | `sensitive_data_masking.bal:43` — identical text | exact match |
| `type Value anydata\|Valuer\|PrintableRawTemplate;` (395) | `natives.bal:30` | exact match |
| `type OutputDestination StandardDestination\|FileOutputDestination;` (503) | `natives.bal:179` | exact match |
| `type MaskingStrategy "EXCLUDE"\|Replacement;` (556) | `sensitive_data_masking.bal:33` `EXCLUDE\|Replacement` | correct (`EXCLUDE` is the const `"EXCLUDE"`) |
| `Config.destinations` `OutputDestination[] & readonly` / `Config.keyValues` `AnydataKeyValues & readonly` (525,527) | `root_logger.bal:32,34` | correct modulo the general "defaults dropped" issue (N7) |

All 7 de-qualified references now name types that exist in the same render. Nothing invented.

Foundational-type check (this module is imported by most other stdlib packages): the exported
types other packages depend on — `log:Logger`, `log:Error`, `log:KeyValues`, `log:Value`,
`log:Level`, `log:LogFormat`, `log:OutputDestination` — are all present in `new` with correct
shapes; `Logger` and `Error` were the two most damaged in `old` (empty class / `// Unknown type:`)
and are now usable.

## 4. Regressions

**None found.**

What I checked to conclude that:
- Enumerated every removed line (`diff old new | grep '^<'`, 16 lines, all listed in §2) — each is
  either a placeholder, a version-qualified ref replaced by a better ref, or the fabricated
  `Additional Values` parameter. None is a real declaration or a real doc line.
- Compared declaration sets extracted with
  `grep -nE '^(public )?(isolated )?(function|type|class|enum|const|annotation)'` on both files:
  every `old` name appears in `new`; `new` adds `Error`, `Valuer`, `ReplacementFunction`,
  `Sensitive` plus 9 class methods.
- Compared JSON `typeDefs` names+order and `functions` names: identical lists on both sides
  (39 / 11), so nothing was dropped at the extractor layer.
- `diff` of lines 1–290 (README + consts) between the two files: empty — README, description and
  the 16 constants are untouched.
- `@deprecated` count is 2 in both files (lines 526/595 old, 572/637 new) — deprecation markers on
  `processTemplate` and `setOutputFile` survive.
- `fromConfig`'s (flawed) signature is byte-identical in both files (old:621, new:663), so its
  problems are pre-existing, not a `new` regression.

## 5. Issues in `new` (independent of `old`)

Ordered by impact. "shared" = also present in `old`, i.e. renderer-level, not caused by spec v2.

- **N1. `distinct` dropped from `Error`.** `new:336` renders `type Error error;`;
  `log_errors.bal:18` is `public type Error distinct error;`. An LLM told this is a plain `error`
  may write `error e = ...` where a `log:Error` is required. New-side-only (old had no definition
  at all, so this is still a net gain).
- **N2. Object types rendered as `class`, with qualifiers and included-record params lost.**
  `Logger` (`logger.bal:18`) and `LoggerRegistry` (`root_logger.bal:56`) are
  `public type X isolated object {...}`, rendered as `class X { ... }`. Methods lose
  `public isolated`, and `*KeyValues keyValues` becomes `KeyValues keyValues` — which reads as a
  required positional record parameter rather than an included record (named-argument) parameter.
  A model copying `logger.printInfo("msg", (), (), {id: 1})` would be wrong; the real call is
  `logger.printInfo("msg", id = 1)`. Same `*`-loss affects the four module-level print functions
  (shared with `old`).
- **N3. Class-method docs lose parameter/return descriptions.** `new:341–372` emits only the
  summary plus an empty `# ` line; the new JSON *does* carry `parameters[].description` and
  `return.description` for `Logger.*` and `LoggerRegistry.*`. Contrast the module-level functions
  (new:587–590), which do get `# + msg - ...` lines. New-side-only quirk of the class renderer.
- **N4. `isolated` dropped from function types** `Valuer` (`natives.bal:46`) and
  `ReplacementFunction` (`sensitive_data_masking.bal:23`). A user-supplied non-isolated function
  will not typecheck where the render implies it will. New-side-only (no definition in `old`).
- **N5. `fromConfig` signature is wrong on both sides.** old:621 / new:663 render
  `function fromConfig(string id = "", LogFormat format = format, Level level = level, log:OutputDestination[] & readonly destinations = destinations, log:AnydataKeyValues & readonly keyValues = {...keyValues}, boolean enableSensitiveDataMasking = enableSensitiveDataMasking, Config config) returns Logger|Error;`
  Source (`root_logger.bal:101`) is `public isolated function fromConfig(*Config config) returns Logger|Error`.
  Three problems: the included record is expanded into 6 named params *and* the `Config config`
  param is retained (so the render shows 7 params for a 1-param function); the expanded types are
  `log:`-prefixed, which is unresolvable inside the module's own render; the defaults
  (`= format`, `= level`, `= destinations`, `= {...keyValues}`) reference module-level
  configurables that neither render emits (§6). Shared.
- **N6. `KeyValues` rest field is malformed.** old:379 / new:416 render `Value ;` under a
  `# Rest field` comment; source (`natives.bal:65`) is `Value...;`. Also, all closed records
  (`record {|...|}`: `KeyValues`, `StandardDestination`, `RotationConfig`, `Config`,
  `Replacement`, `SensitiveConfig`) are rendered as open `record { ... }`. Shared.
- **N7. Field defaults and `readonly` dropped; defaulted fields shown as optional.** e.g.
  `StandardDestination.'type` is `readonly STDERR|STDOUT 'type = STDERR` (`natives.bal:126`) but
  renders as `"stderr"|"stdout" 'type?;`; `RotationConfig` loses `policy = BOTH`,
  `maxFileSize = 10485760`, `maxAge = 86400`, `maxBackupFiles = 10` (`natives.bal:153–162`);
  `FileOutputDestination.mode = APPEND` and `SensitiveConfig.strategy = EXCLUDE` likewise. The
  effective defaults are the single most useful fact about these config records and they are gone.
  Shared (the JSON has no `default` key on any record field on either side).
- **N8. Multi-line doc continuations are emitted without a `#` prefix**, producing lines that are
  neither comment nor code: `new:479, 482, 485, 516–518, 551, 653–655` (e.g. line 479
  `Default: 10MB (10 * 1024 * 1024 bytes)`). The render as a whole therefore does not parse as
  Ballerina. Shared (old:441,444,447,479–481,504,614–616).
- **N9. `PrintableRawTemplate` rendered as an empty class.** Source (`natives.bal:37–41`) is
  `public type PrintableRawTemplate readonly & object { *object:RawTemplate; public string[] & readonly strings; public Value[] insertions; }`.
  The new JSON typeDef has neither `fields` nor `functions`, so `strings`/`insertions` are absent
  from both renders even though `processTemplate`/`evaluateTemplate` take this type. Shared.
- **N10. Enum members lose their string values and source order.** `enum LogFormat { LOGFMT, JSON_FORMAT }`
  (new:441) omits `= "logfmt"` / `= "json"` (`natives.bal:96–98`); same for `DestinationType`,
  `RotationPolicy`. Order is reversed/permuted vs source (`Level` renders WARN, INFO, ERROR, DEBUG;
  source order is DEBUG, ERROR, INFO, WARN). The values do survive as separate constants
  (new:298–328), so this is mitigated. Shared.
- **N11. `# # Deprecated` doc bodies dropped.** `grep -n 'Deprecated'` returns nothing in either
  render, though `natives.bal:215–216` and `328–330` explain what to use instead
  (`evaluateTemplate`; the `destinations` configurable). `@deprecated` itself is kept. Shared.

## 6. Coverage gaps vs. the library

The bala has exactly one module (`modules/log`) and Central reports `modules: ['log']`, so there
is **no submodule-only API** — nothing is lost to the `getDefaultModule()`-only extraction here.

`grep -n '^public ' modules/log/*.bal` yields 41 public module-level declarations. Missing from
**both** renders (5, all of them public configurable variables):

| Symbol | Source |
|---|---|
| `public configurable LogFormat format = LOGFMT` | `natives.bal:102` |
| `public configurable Level level = INFO` | `natives.bal:105` |
| `public configurable table<Module> key(name) & readonly modules = table []` | `natives.bal:108` |
| `public configurable AnydataKeyValues & readonly keyValues = {}` | `natives.bal:111` |
| `public configurable readonly & OutputDestination[] destinations = [{'type: STDERR}]` | `natives.bal:182` |

These matter more than usual: they are the documented way to configure logging from
`Config.toml`, the README section that shows `[ballerina.log] level = "DEBUG"` relies on them, and
`fromConfig`'s rendered defaults (`format = format`, `level = level`, `destinations = destinations`)
literally reference symbols that appear nowhere else in the render. The extractor emits no
`variables`/`configurables` array in the JSON at all (top-level keys are exactly
`name, description, readme, typeDefs, clients, functions, services, annotations` on both sides).

Also absent, though nested rather than top-level: the two public fields of `PrintableRawTemplate`
(N9). Everything else public — 16 constants, 7 enums, 12 types/objects, 11 functions, 1 annotation
— is present in `new`.

## 7. Compiler plugin

`has_plugin: true`, confirmed: `compiler-plugin/compiler-plugin.json` declares
`plugin_id: log-compiler-plugin`, `plugin_class: io.ballerina.stdlib.log.compiler.LogCompilerPlugin`,
jar `compiler-plugin/libs/log-compiler-plugin-2.17.0.jar`.

What it contributes (read from the clone,
`compiler-plugin/src/main/java/io/ballerina/stdlib/log/compiler/`):

- `LogCompilerPlugin.init` registers **only** a `StaticCodeAnalyzer`, and only when a
  `ScannerContext` is present in `context.userData()` — i.e. the plugin is a `bal scan`
  contributor, not a code generator or code-action provider.
- `staticcodeanalyzer/LogRule.java:31` defines a single rule,
  `AVOID_LOGGING_CONFIGURABLE_VARIABLES` — *"Potentially-sensitive configurable variables are
  logged"*, kind `VULNERABILITY`, declared in `compiler-plugin/src/main/resources/rules.json`.
  `LogStatementAnalyzer.java` implements it: it resolves the `ballerina/log` import prefix and
  flags `printInfo` / `printError` / `printWarn` calls whose arguments reference symbols with the
  `CONFIGURABLE` qualifier.
- `LogCodeModifier.java` (a `CodeModifier` that rewrites log call sites to inject the module name)
  exists in the source tree but is **not referenced by `LogCompilerPlugin`** — `grep -rn
  "LogCodeModifier"` over `compiler-plugin/src` and `compiler-plugin-tests` returns only its own
  declaration. It is dead code at this tag; nothing it would generate needs to appear in a render.

Nothing the plugin implies is missing from `new`. The one plugin-adjacent API surface — the
`@log:Sensitive` annotation and its `SensitiveConfig`/`MaskingStrategy`/`Replacement` types, which
are the sanctioned way to suppress exactly the leakage the rule warns about — was **absent from
`old`** and is now rendered (`new:672–676` plus types at 544–563). That is the single most
valuable addition in this diff. The rule's own subject (configurable variables) is still invisible
to the render, per §6.

## 8. Other considerations

- Version/pin: bala `package.json` says `ballerina/log 2.17.0`; Central confirms `2.17.0`,
  `visibility: public`, `deprecated: null`, pullCount 51,635. Both renders were produced from the
  same bala. No version drift.
- Size: render grew 628→676 lines (+7.6%), 19.3 KB → 21.2 KB (+9.7%); JSON 43.6 KB → 53.0 KB
  (+21.6%). Negligible token cost for a materially more complete API surface.
- Neither render is compilable Ballerina (N6, N8, and the `fromConfig` signature). If the
  consumer is only an LLM reading the text this is tolerable, but `new` did not fix it — it fixed
  one class of it (`Value Additional Values`, an identifier containing a space) while N8's
  bare-text doc continuations remain on both sides.
- Two deprecated functions (`processTemplate`, `setOutputFile`) are rendered with `@deprecated` but
  without the replacement guidance (N11), so a model may still recommend `setOutputFile` over the
  `destinations` configurable — which it cannot see either (§6).
- `log` is a foundational module: `log:Logger` and `log:Error` appear in the public surface of many
  other packages. `old` rendered `Logger` as an empty class and `Error` as `// Unknown type:`;
  after this change both are substantive. That is the cross-library payoff of this diff.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.17.0 …/module-ballerina-log` | success; HEAD `6c2b68b58ba43bcdfa1aced0efb8c3382f36bf0e`, tag `v2.17.0` |
| `diff -q <clone>/ballerina/<f>.bal <bala>/modules/log/<f>.bal` ×6 | all IDENTICAL |
| `wc -l old new` | 628 / 676 |
| `wc -c old new` | 19,349 / 21,231 |
| `grep -c '^// Unknown type:'` | old 3, new 0 |
| `grep -o 'ballerina/log:2.17.0:' \| wc -l` | old 7 (on 5 lines), new 0 |
| `grep -n '^// --- '` | old 4 markers (7,285,287,519); new 5 (7,285,287,565,672) |
| `diff old new \| grep -c '^>' / '^<'` | 64 added / 16 removed |
| `diff -u old new \| grep -c '^@@'` | 11 hunks |
| `diff old new \| grep '^<'` (full listing) | 3 Unknown-type, 4 `Additional Values` doc lines, 4 print signatures, 5 qualified-ref lines |
| `diff <(sed -n '1,290p' old) <(sed -n '1,290p' new)` | empty — README + consts unchanged |
| JSON top-level keys both sides | `name, description, readme, typeDefs, clients, functions, services, annotations` |
| JSON `typeDefs` len / names / order | 39 both, identical lists in identical order |
| JSON `functions` names | identical 11 both sides |
| JSON `annotations` len | old 0, new 1 (`Sensitive`, `RECORD_FIELD`, typeConstraint `SensitiveConfig`) |
| JSON `printDebug.parameters` len | old 5 (incl. `"Additional Values"`), new 4 |
| JSON `Error`/`Valuer`/`ReplacementFunction` | new adds `baseType`: `error`, `function () returns anydata`, `function (string input) returns string` |
| JSON `Logger`/`LoggerRegistry` | new adds `functions` arrays (7 and 2 entries) with param + return descriptions |
| JSON `PrintableRawTemplate` (new) | `{"name","description","type":"Class"}` — no `fields` |
| `new['readme'] == bala docs/README.md` | True (7,699 chars); `old['readme'] == new['readme']` True |
| `grep -n '^public ' <bala>/modules/log/*.bal` | 41 public module-level declarations |
| `grep -n 'configurable' old new` | 0 hits in either render |
| `grep -n '@deprecated' old` / new | 2 each (old 526,595; new 572,637); `grep -n 'Deprecated'` 0 in both |
| `cat compiler-plugin/compiler-plugin.json` | `log-compiler-plugin` / `LogCompilerPlugin` / libs jar 2.17.0 |
| Read `LogCompilerPlugin.java` | registers only `StaticCodeAnalyzer`, gated on `ScannerContext` |
| `LogRule.java:31` | `AVOID_LOGGING_CONFIGURABLE_VARIABLES`, kind `VULNERABILITY` |
| `grep -rn LogCodeModifier compiler-plugin/src compiler-plugin-tests` | only its own class declaration — unregistered |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/log/2.17.0` | version 2.17.0, deprecated null, public, modules `['log']` |
| `ls <bala>/modules` | `log` only — no submodules |

## 10. Caveats and unverified items

- Neither render was compiled or parsed with a Ballerina toolchain; claims that the render is not
  valid Ballerina (N6, N8, N5) are from reading the text against the grammar, not from `bal build`.
- The compiler-plugin jar in the bala was not decompiled; plugin behaviour is taken from the
  `v2.17.0` clone sources, which are byte-identical to the bala for the `.bal` files but were not
  independently verified to be the exact sources of `log-compiler-plugin-2.17.0.jar`.
- I did not re-run the two-stage pipeline; both JSONs and both renders are taken as produced by the
  harness. The claim "same library, both sides" rests on the identical `typeDefs`/`functions` name
  lists and identical README bytes, which is strong but indirect evidence.
- Whether the extractor *can* emit module-level configurable variables at all (i.e. whether §6 is a
  spec-v2 omission or an unimplemented feature on both sides) was not determined — I only observed
  that neither JSON has such a field.

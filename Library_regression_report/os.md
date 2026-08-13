# ballerina/os 1.10.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/os` |
| Pinned version | `1.10.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-os |
| Tag reviewed | `v1.10.1` (commit `8ba80f5c93ce9ba92baf96195fc46643cec6793b`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/os/1.10.1/java21` |
| Old render | `102` lines |
| New render | `129` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`os` is a 4-file, single-module standard library (12 public symbols total). `old` degraded three of
its five type definitions to `// Unknown type:` placeholders — `Error`, `ProcessExecError`, and the
entire `Process` class with all three of its methods. `new` emits real definitions for all three,
raising `// Unknown type:` from 3 to 0 and adding the only object API the module has. The single
line removed from `new` is a synthetic `anydata Additional Values` parameter on `exec` that does not
exist in the library source and was non-compiling Ballerina in `old`; removing it makes the render
strictly more faithful, so it is not scored as a regression. No declaration that is present and
correct in `old` is missing from `new`. Residual inaccuracies exist in `new` (lost `distinct`, lost
`ProcessExecError <: Error` subtyping, lost `*` included-record parameter marker, closed-record
fidelity, dropped `# + param` / `# + return` docs inside the class body) but every one of them is
either shared with `old` or occurs in a region `old` did not render at all.

## 2. Change inventory

Line counts (`wc -l`): old 102, new 129. JSON: old 312 lines, new 296 lines.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines (`grep -c`) | 3 | 0 |
| `// --- ` section markers (`grep -c`) | 4 | 4 |
| Top-level declarations (`grep -cE '^(function\|type\|class\|enum\|const\|annotation) '`) | 9 | 12 |
| `# + return` doc lines (`grep -c`) | 7 | 7 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |

Declarations added in `new` (6) — all previously placeholders or nested inside one:

| Kind | Name | old | new |
|---|---|---|---|
| type (error) | `Error` | `// Unknown type: Error` | `type Error error;` |
| type (error) | `ProcessExecError` | `// Unknown type: ProcessExecError` | `type ProcessExecError error;` |
| class | `Process` | `// Unknown type: Process` | `class Process { … }` (new:39–63) |
| class method | `Process.waitForExit` | absent | `function waitForExit() returns int\|Error;` |
| class method | `Process.output` | absent | `function output(io:FileOutputStream fileOutputStream = 1) returns byte[]\|Error;` |
| class method | `Process.exit` | absent | `function exit() returns ();` |

Declarations removed: none.

Declarations modified (1):

```
- function exec(Command command, anydata Additional Values, EnvProperties envProperties) returns Process|Error;
- # + Additional Values - Capture key value pairs
+ function exec(Command command, EnvProperties envProperties) returns Process|Error;
```

Unchanged: README block (lines 7–16, byte-identical), `Command`, `EnvProperties`, and all 7
module-level functions (`getEnv`, `getUsername`, `getUserHome`, `setEnv`, `unsetEnv`, `listEnv`,
`exec` body/docs apart from the line above).

JSON-level deltas behind the render change (both extractor-side):
- `new` adds `"type": "Class"` to the `Process` typedef and `"baseType": "error"` to `Error` /
  `ProcessExecError`. `old` had neither, which is exactly why `renderTypeDef` fell through to
  `// Unknown type:`.
- `old`'s `Process` carried a synthetic `init` `Constructor` entry returning `ballerina/os:Process`;
  `new` drops it. `Process` declares no `init` in source (`process.bal:22–55`), so the drop is
  correct — and it was never rendered on either side.
- `old`'s `exec` had a third parameter object `{"name":"Additional Values","type":{"name":"anydata"},
  "optional":true}`; `new` does not.

## 3. Correctness against library source

The bala's `modules/os/*.bal` is byte-identical to `ballerina/*.bal` at tag `v1.10.1`
(`diff -q` on `init.bal`, `os.bal`, `os_errors.bal`, `process.bal` — no output). Every check below is
against those files.

| Rendered (new) | Source | Verdict |
|---|---|---|
| `function getEnv(string name) returns string` | `os.bal:36` `public isolated function getEnv(string name) returns string` | match (qualifiers stripped by convention on both sides) |
| `function getUsername() returns string` | `os.bal:51` | match |
| `function getUserHome() returns string` | `os.bal:62` | match |
| `function setEnv(string key, string value) returns Error\|()` | `os.bal:76` `returns Error?` | match (`Error?` ≡ `Error\|()`) |
| `function unsetEnv(string key) returns Error\|()` | `os.bal:94` | match |
| `function listEnv() returns map<string>` | `os.bal:113` | match |
| `function exec(Command command, EnvProperties envProperties) returns Process\|Error` | `os.bal:130` `exec(Command command, *EnvProperties envProperties) returns Process\|Error` | param count/types/order match; `*` (included-record) marker lost — see §5.1 |
| `type Error error;` | `os_errors.bal:18` `public type Error distinct error;` | `distinct` lost — see §5.2 |
| `type ProcessExecError error;` | `os_errors.bal:21` `public type ProcessExecError distinct Error;` | base type wrong: source derives from `Error`, render says bare `error` — see §5.3 |
| `class Process { … }` + docs | `process.bal:20–55` | class doc text matches verbatim |
| `function waitForExit() returns int\|Error;` | `process.bal:31` `public isolated function waitForExit() returns int\|Error` | match |
| `function output(io:FileOutputStream fileOutputStream = 1) returns byte[]\|Error;` | `process.bal:43` `output(io:FileOutputStream fileOutputStream = io:stdout) returns byte[]\|Error` | type and arity match; default rendered as the literal `1`. `ballerina/io` 1.8.0 `constants.bal:67` declares `public const stdout = 1;` and `print.bal:28` `public type FileOutputStream stdout\|stderr;`, so `1` is value-correct and type-valid, just non-idiomatic — see §5.5 |
| `function exit() returns ();` | `process.bal:52` `public isolated function exit()` | match (no return type ≡ `()`) |
| `type Command record { string value; string[] arguments?; }` | `os.bal:19–22` `record {\| string value; string[] arguments = []; \|}` | field names/types match; closedness and default lost — shared with `old`, see §5.4 |
| `type EnvProperties record { never command?; }` | `os.bal:24–27` `record {\| never command?; anydata...; \|}` | rest field `anydata...` lost — shared with `old`, see §5.4 |
| README block (lines 8–14) | `docs/README.md` | identical (`diff` clean modulo blank lines) |

## 4. Regressions

**None found.**

Checked to reach that conclusion:
- Declaration-set diff: `new` removes zero declarations (see §2 table; the precomputed diff's
  "Declarations removed (0)" was independently confirmed by grepping declaration lines out of both
  files and comparing).
- The only textual removals in the whole diff are the two `exec` lines. Evaluated below.
- All 7 module-level function signatures, all `# + param` / `# + return` doc lines for them
  (7 `# + return` on both sides), the README block, and both record typedefs are byte-identical
  across the two files.
- No malformed syntax introduced: `new` has no identifier with an embedded space, no unterminated
  block; `old` had one (`anydata Additional Values`).

Considered and rejected as a regression — the `exec` parameter drop:

`old` rendered `exec(Command command, anydata Additional Values, EnvProperties envProperties)`.
`os.bal:130` declares exactly two parameters, `Command command` and `*EnvProperties envProperties`.
The `Additional Values` entry is not a library symbol, is not a legal Ballerina identifier (embedded
space, so the `old` render does not parse), and its accompanying doc line
`# + Additional Values - Capture key value pairs` does not appear anywhere in the module source or
in `docs/README.md`. It was an extractor artefact standing in for the `anydata...` rest field of
`EnvProperties`. Its removal makes `new` closer to source, not further. The only real loss is a hint
that `exec` accepts arbitrary named env arguments — but that hint is still present in the retained
doc example on new:123 (`os:exec({value: "bal", …}, BAL_CONFIG_FILE = "/abc/Config.toml")`), so an
LLM consuming `new` still sees the calling pattern. Net: not a regression; the underlying
`*`/rest-field modelling weakness is logged in §5.1/§5.4 as a shared issue.

## 5. Issues in `new` (independent of `old`)

All of these are also present in `old` where `old` rendered the construct at all; items 2, 3, 5 and 6
sit in regions `old` degraded to `// Unknown type:`, so they are new-only in the trivial sense that
`new` is the first side to render them.

1. **Included-record parameter marker lost** (new:129). `exec(Command command, EnvProperties
   envProperties)` implies a positional record argument; source `os.bal:130` uses
   `*EnvProperties envProperties`, which means callers pass individual named arguments
   (`os:exec(cmd, BAL_CONFIG_FILE = "…")`), not a record. An LLM following the render would write
   `os:exec(cmd, {})`, which does not compile. Identical modelling on both sides (`old` also had
   `EnvProperties envProperties` as a plain param).
2. **`distinct` dropped from `Error`** (new:32). Source `os_errors.bal:18` is
   `public type Error distinct error;`. `type Error error;` loses the distinct-error semantics.
3. **`ProcessExecError` base type wrong** (new:35). Source `os_errors.bal:21` is
   `public type ProcessExecError distinct Error;` — it is a subtype of `os:Error`. The render emits
   `type ProcessExecError error;`, which severs the relationship; a consumer cannot tell that
   catching `os:Error` also catches `os:ProcessExecError`. The JSON confirms the flattening:
   `"baseType": "error"` for both error typedefs.
4. **Record fidelity** (new:21–29). `Command` is a closed record with a *defaulted required* field
   (`string[] arguments = []`, `os.bal:21`), rendered as an open record with an *optional* field
   `string[] arguments?`. `EnvProperties` (`os.bal:24–27`) is closed with an `anydata...` rest
   descriptor; the rest descriptor is absent from the render, so nothing in `new` states that
   arbitrary `anydata` keys are accepted. Both are shared with `old` and originate in the JSON
   (`"optional": true`, no rest-field key).
5. **`output` default rendered as `1`** (new:55) rather than `io:stdout` (`process.bal:43`).
   Value-correct (`io:stdout == 1`) but loses the symbolic form the doc example uses.
6. **Class-method doc parameters/returns dropped** (new:41–62). The JSON for `Process.waitForExit`
   and `Process.output` carries the return descriptions ("The exit code of the process if it exits
   successfully, or an Error") and the `fileOutputStream` parameter description, matching
   `process.bal:30`, `41–42`. The render emits neither: `grep -c '# + return'` is 7 on both files —
   the 7 module-level functions only — and `# + fileOutputStream` appears nowhere. Each class method
   therefore ends with a dangling bare `# ` line. Renderer-side loss inside class bodies only;
   module-level functions keep their `# + …` lines.
7. **`io:FileOutputStream` referenced without an import** (new:55). The render's only import is
   `import ballerina/os;` (new:5). The renderer compensates with the trailing
   `// Special Agent Note: FileOutputStream FROM ballerina/io package` comment, so this is by design
   rather than a defect, but the emitted snippet is not compilable as-is.

## 6. Coverage gaps vs. the library

**Zero missing public symbols.** The bala exports exactly one module (`package.json`:
`"export": ["os"]`; `modules/` contains only `os`), so there is no submodule API and hence no shared
submodule gap. Complete public surface of `modules/os/*.bal` versus the renders:

| Public symbol | Source | old | new |
|---|---|---|---|
| `Command` | os.bal:19 | rendered | rendered |
| `EnvProperties` | os.bal:24 | rendered | rendered |
| `Error` | os_errors.bal:18 | placeholder | rendered |
| `ProcessExecError` | os_errors.bal:21 | placeholder | rendered |
| `Process` (+ `waitForExit`, `output`, `exit`) | process.bal:22 | placeholder | rendered |
| `getEnv`, `getUsername`, `getUserHome`, `setEnv`, `unsetEnv`, `listEnv`, `exec` | os.bal | rendered | rendered |

Non-public symbols correctly excluded from both: `init`, `setModule` (init.bal), `nativeGetEnv`,
`setEnvExtern`, `listEnvExtern` (os.bal), `nativeWaitForExit`, `nativeExit`, `nativeOutput`
(process.bal). The module declares no constants, enums, annotations, listeners, services or clients
(`clients`, `services`, `annotations` are all empty arrays in both JSONs), so the empty render
sections are correct.

Field-level gaps (not symbol-level, counted in §5.4 instead): `EnvProperties`'s `anydata...` rest
descriptor and `Command.arguments`'s `= []` default appear in neither render.

## 7. Compiler plugin

`has_plugin` is true and confirmed:
`java21/compiler-plugin/compiler-plugin.json` declares `plugin_id: os-compiler-plugin`,
`plugin_class: io.ballerina.stdlib.os.compiler.OSCompilerPlugin`, shipping
`compiler-plugin/libs/os-compiler-plugin-1.10.1.jar`.

What it contributes (from `compiler-plugin/src/main/java/io/ballerina/stdlib/os/compiler/`):
- `OSCompilerPlugin.java:32–38` — registers a code analyzer **only** when a `ScannerContext` is
  present in `context.userData()`, i.e. it runs under `bal scan`, not on ordinary builds.
- `staticcodeanalyzer/OSRule.java:30–33` — two `VULNERABILITY` rules:
  `AVOID_UNSANITIZED_CMD_ARGS` ("Avoid constructing system command arguments from user input without
  proper sanitization") and `AVOID_UNSANITIZED_ENV_VARS` (same for environment variables).
- `staticcodeanalyzer/OSCommandInjectionAnalyzer.java:62–90+` — inspects
  `FunctionCallExpressionNode`s targeting `os:exec` (`command.value` / `command.arguments`) and
  `os:setEnv`, tracing arguments back to public-function parameters to flag taint.
- Supporting: `OSStaticCodeAnalyzer`, `RuleFactory`, `RuleImpl`.

Nothing the plugin implies is missing from the render: it defines **no annotations, no generated
types, and no code actions** — it is purely a static-code-analysis (scan) contribution, so there is
no artefact it should have surfaced. Worth noting for downstream consumers only as guidance: a
render-driven LLM has no signal that interpolating user input into `os:Command.value`/`arguments` or
into `os:setEnv` is flagged as a vulnerability by `bal scan`. That is a render-format limitation
affecting both sides equally, not a `new` regression.

## 8. Other considerations

- Stable 1.x library, not deprecated. `package.json`: `organization: ballerina`, `name: os`,
  `version: 1.10.1`, `export: ["os"]`, `keywords: ["environment"]`, `licenses: ["Apache-2.0"]`.
- Size: +27 lines (+26%) for the whole `Process` API plus two error types. Negligible token cost for
  a materially larger API surface; this is one of the cheapest wins in the batch.
- Doc quality in `new` is good at module level (every module function keeps its description, code
  example, `# + param` and `# + return` lines) and degraded at class level (§5.6).
- The `os` module is imported by other packages mainly for `getEnv`/`setEnv`; those signatures are
  unchanged and correct on both sides, so no downstream render depending on `os:Error` shape is
  affected by this change — though `os:Error`'s `distinct` nature is now stated inaccurately rather
  than not at all (§5.2).
- The `new` render is closer to valid Ballerina than `old` (which contained an unparseable
  identifier), but still not compilable standalone: missing `import ballerina/io;` for
  `io:FileOutputStream`, and error typedefs would need `distinct`.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_os.bal.txt new/ballerina_os.bal.txt old/ballerina_os.json new/ballerina_os.json` | 102 / 129 / 312 / 296 |
| `grep -c '^// Unknown type:'` both renders | old 3, new 0 |
| `grep -c '^// --- '` both renders | 4 / 4 |
| `grep -cE '^(function\|type\|class\|enum\|const\|annotation) '` both renders | old 9, new 12 |
| `grep -c '# + return'` both renders | 7 / 7 (module functions only; none inside `class Process`) |
| `grep -n 'fileOutputStream -' new` | no match — param doc dropped in class body |
| `grep -n '^import' new` | only `5:import ballerina/os;` |
| Read both renders in full (102 + 129 lines) | full declaration inventory in §2 |
| `git clone --depth 1 --branch v1.10.1 …/module-ballerina-os` | success; `git log -1` → `8ba80f5c93ce9ba92baf96195fc46643cec6793b (tag: v1.10.1)` |
| `find <bala> -maxdepth 4` | platform dir `java21`; `modules/os/{init,os,os_errors,process}.bal`; `docs/README.md`; `compiler-plugin/compiler-plugin.json` + jar |
| `ls <bala>/java21/modules/` | `os` only — no submodules |
| `diff -q <clone>/ballerina/<f>.bal <bala>/modules/os/<f>.bal` for all 4 files | no output — byte-identical |
| `cat -n <bala>/modules/os/os.bal` | `exec` at :130 has 2 params, second is `*EnvProperties`; `Command` :19 closed with `arguments = []`; `EnvProperties` :24 closed with `anydata...` |
| `cat -n <bala>/modules/os/os_errors.bal` | `:18 public type Error distinct error;` `:21 public type ProcessExecError distinct Error;` |
| `cat -n <bala>/modules/os/process.bal` | class :22; `waitForExit` :31; `output` :43 default `io:stdout`; `exit` :52; `# + return` docs at :30, :42; `# + fileOutputStream` at :41 |
| `diff` render README block vs `<bala>/docs/README.md` | identical (blank-line-only differences from the grep filter) |
| `python3` dump of both JSONs' `typeDefs`/`functions`/`clients`/`services`/`annotations` | same 5 typeDefs + 7 functions both sides; 0 clients/services/annotations both sides; `new` adds `"type":"Class"` and `"baseType":"error"`; `new` drops `Process.init` and `exec`'s `Additional Values` param |
| `grep -rn "FileOutputStream\|const stdout" <io 1.8.0 bala>` | `constants.bal:67 public const stdout = 1;` `print.bal:28 public type FileOutputStream stdout\|stderr;` → render default `1` is value-correct |
| `cat <bala>/java21/compiler-plugin/compiler-plugin.json` | `os-compiler-plugin`, class `io.ballerina.stdlib.os.compiler.OSCompilerPlugin` |
| Read `OSCompilerPlugin.java`, `OSRule.java`, `OSCommandInjectionAnalyzer.java` (clone) | scan-only analyzer, 2 VULNERABILITY rules, no annotations/code actions |
| `python3` dump of `package.json` | `ballerina/os 1.10.1`, `export: ["os"]`, Apache-2.0 |
| Cross-check of `OLD_AND_NEW_DIFFS/os_diff.md` claims (102/129 lines, 3→0 unknowns, 6 added decls, 0 removed, 2 hunks) | all independently reproduced |

## 10. Caveats and unverified items

- Ballerina Central metadata for `ballerina/os/1.10.1` was **not** re-queried over the network; all
  package metadata in this report comes from the bala's `package.json` and `bala.json`, which the
  brief designates authoritative for what the extractor consumed. Deprecation status is therefore
  unverified from Central (no deprecation marker in the bala).
- The compiler-plugin jar shipped in the bala was not decompiled; plugin behaviour is read from the
  `v1.10.1` tag's Java source, which matched the bala's `.bal` sources byte-for-byte and so is
  assumed consistent. Version string `os-compiler-plugin-1.10.1.jar` corroborates it.
- Whether the missing `# + param` / `# + return` lines inside class bodies is intended renderer
  behaviour or an oversight was not determined — the `ballerina-vscode` renderer source was not
  inspected. The observable fact (present in JSON, absent in render) is confirmed.
- `exec`'s `Additional Values` pseudo-parameter was judged a synthetic stand-in for the
  `EnvProperties` `anydata...` rest field. That interpretation is inference; what is *verified* is
  that no such parameter or doc line exists anywhere in the `v1.10.1` sources or README.

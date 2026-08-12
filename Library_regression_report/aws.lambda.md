# ballerinax/aws.lambda 3.3.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.lambda` |
| Pinned version | `3.3.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.lambda |
| Tag reviewed | `v3.3.0` (commit `a4866dc31eaf564d8b78c5ebf45cc667b51ab3ab`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.lambda/3.3.0` |
| Old render | `343` lines |
| New render | `365` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old`. Nothing was removed: `diff -u` shows exactly 2 hunks,
`+23 / −1` lines, and the only removed line is the degraded placeholder `// Unknown type: Context`.

Two real gains:

1. The `Context` class — the central user-facing object of this module — is now emitted as a real
   `class` with all six methods, replacing a bare `// Unknown type: Context` line.
2. A new `// --- Annotations ---` section emits `public annotation Function on function;`. This is
   the **only** way a user writes an AWS Lambda function in Ballerina (`@lambda:Function`), and it
   was entirely absent from `old`. An LLM consuming the `old` render could not have produced a
   working AWS Lambda program; with `new` it can.

Coverage of the default module's public API is now 100 % (25 / 25 public symbols). No regressions
found. A handful of accuracy defects remain in `new`, but every one of them is also present in
`old` or is a consequence of a JSON field the extractor never populated — none is newly introduced.

## 2. Change inventory

Line counts (`wc -l`): old `343`, new `365`.
Mechanical diff (`diff -u`): 2 hunks, 23 lines added, 1 removed.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- ` section markers | 4 | 5 |
| `^type ` record declarations | 21 | 21 |
| `^class ` declarations | 0 | 1 |
| `^public annotation` declarations | 0 | 1 |

JSON side (`old/*.json` vs `new/*.json`, compared by `json.load` + set/dict equality):

| JSON field | old | new |
|---|---|---|
| `typeDefs` | 22 | 22 (same 22 names) |
| `clients` | 0 | 0 |
| `functions` | 2 | 2 (byte-identical) |
| `services` | 0 | 0 |
| `annotations` | 0 | **1** |
| `readme` | — | identical to old |
| `description` | — | identical to old |

The only differing `typeDefs` entry is `Context`: `new` adds `"type": "Class"`. The `functions`
array inside `Context` (init + 5 methods, with docs and return descriptions) was **already present
in `old`'s JSON** — `old`'s `renderTypeDef` simply had no branch for an untagged type-def and
degraded it to a placeholder. So this is a renderer/extractor tagging fix, not new extraction.

### Declarations added (2 top-level, 8 counting class members)

| Kind | Name |
|---|---|
| class | `Context` |
| class method | `init`, `getRequestId`, `getDeadlineMs`, `getInvokedFunctionArn`, `getTraceId`, `getRemainingExecutionTime` |
| annotation | `Function` (`on function`) |

### Declarations removed

None. Verified: `diff -u` contains exactly one `-` line, `// Unknown type: Context`.

## 3. Correctness against library source

Upstream `v3.3.0` and the bala are byte-identical for all three `.bal` files
(`diff` on `code.bal`, `events.bal`, `annotation.bal` → all clean). So GitHub and bala agree; no
"bala wins" conflict arises.

`Context` (bala `modules/aws.lambda/code.bal:24-77`) — every rendered member checked:

| Rendered | Source | Match |
|---|---|---|
| `class Context` | `code.bal:24` `public class Context {` | yes (modifier dropped, see §5) |
| `init(string requestId, int deadlineMs, string invokedFunctionArn, string traceId) returns ()` | `code.bal:31` `isolated function init(string requestId, int deadlineMs, string invokedFunctionArn, string traceId)` | yes |
| `getRequestId() returns string` | `code.bal:40` | yes |
| `getDeadlineMs() returns int` | `code.bal:46` | yes |
| `getInvokedFunctionArn() returns string` | `code.bal:52` | yes |
| `getTraceId() returns string` | `code.bal:58` | yes |
| `getRemainingExecutionTime() returns int` | `code.bal:64` | yes |

Method count and order match the source exactly; no invented methods. The doc strings rendered
above each method are verbatim from the source doc comments (`code.bal:39,45,51,57,63`).

`Function` annotation — rendered `public annotation Function on function;` vs source
`annotation.bal:18` `public const annotation Function on function;`. Name, visibility and
attachment point are correct; the `const` qualifier is dropped (see §5). Cross-checked against
real usage in `samples/sample1/functions.bal:6` (`@lambda:Function`) — the rendered form is
sufficient for an LLM to write correct code.

Records: all 21 `public type … record` names in `events.bal` (lines 4, 13, 25, 38, 56, 71, 86,
101, 119, 142, 160, 173, 185, 198, 212, 225, 234, 250, 265, 275, 284) appear in both renders,
unchanged between sides.

## 4. Regressions

**None found.**

What was checked to conclude that:

- `diff -u old new` — full output reviewed; the single deleted line is the `// Unknown type:`
  placeholder, which carried no information.
- Declaration-set comparison: `grep -c '^type '` = 21 on both; `grep -n '^// --- '` shows `new`
  keeps all 4 of `old`'s sections and adds one.
- JSON comparison: `readme`, `description` and the whole `functions` array are equal between
  sides; `typeDefs` name sets are equal; the only per-entry difference is the added
  `"type": "Class"` tag on `Context` (nothing dropped from the entry).
- No parameter, default value, return type or doc line present in `old` is absent from `new`
  (byte-level: every `old` line except one appears in `new`).
- No malformed syntax introduced: the emitted `class`/`annotation` blocks are well-formed
  Ballerina declaration syntax.

## 5. Issues in `new` (independent of `old`)

Five defects. All are pre-existing (shared with `old`) or come from an unpopulated extractor
field — none is introduced by spec v2.

1. **`__register` third parameter has the wrong type.** Render (both sides, `new` line 357):
   `function __register(string handler, FunctionType func, anydata eventType) returns ();`
   Source `code.bal:109`: `public function __register(string handler, FunctionType func,
   typedesc<anydata> eventType)`. The `typedesc<…>` wrapper is lost. Shared with `old`.
2. **`FunctionType` is referenced but never defined in the render.** `code.bal:80` declares
   `type FunctionType function (Context, anydata) returns json|error;` **without** `public`, so it
   is not exported and the extractor correctly omits it — but the `__register` signature still
   names it, leaving a dangling reference. The render is therefore not self-consistent as
   Ballerina source. Shared with `old`.
3. **`Context`'s own doc comment is dropped.** Source `code.bal:23` has
   `# Object to represent an AWS Lambda function execution context.`, but the JSON carries
   `"description": ""` for the `Context` typeDef on both sides, so `new` emits the class with no
   leading doc. Visible only in `new` because `old` emitted nothing at all. Extractor gap, not a
   renderer regression.
4. **Qualifiers dropped.** `public` and `isolated` are stripped from the class and all its
   methods; `const` is stripped from the annotation. The render's general convention drops
   `public` on types (all 21 records are rendered bare too), so this is consistent — but the
   `isolated`/`const` loss means the render understates the library's concurrency contract.
5. **Method return-value descriptions are not rendered.** The JSON holds
   `"return": {"description": "the request id", …}` etc. for all five `Context` getters; the
   `.bal.txt` emits only the summary doc line, never a `# + return - …` line. Information present
   in the JSON is discarded by `toSyntaxString` on both sides.

## 6. Coverage gaps vs. the library

**Zero gaps** for `new`.

The bala `package.json` has `"export": ["aws.lambda"]` and `modules/` contains exactly one
directory (`aws.lambda`, the default module) — there is no submodule API, so the shared
`getDefaultModule()` limitation is a no-op for this library.

Full public surface of the default module (25 symbols) vs the renders:

| Symbol group | count | in `old` | in `new` |
|---|---|---|---|
| `public type … record` (events.bal) | 21 | 21 | 21 |
| `public class Context` | 1 | placeholder only | full |
| `public function __register`, `__process` | 2 | 2 | 2 |
| `public const annotation Function` | 1 | **0** | 1 |
| **total** | **25** | 23 (+1 degraded) | **25** |

`old` coverage gap: 1 symbol (`Function` annotation) entirely missing, plus `Context` degraded to
a name-only comment. `new` coverage gap: none.

Non-public symbols correctly absent from both: `FunctionType`, `FunctionEntry`, `BASE_URL`,
`generateContext`, `jsonToEventType`, `processEvent`, and the four private `Context` fields.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` registers
`org.ballerinax.aws.lambda.generator.AWSLambdaCompilerPlugin` (jar
`aws.lambda-compiler-plugin-3.3.0.jar`). Reviewed the upstream sources at `v3.3.0`
(`compiler-plugin/src/main/java/org/ballerinax/aws/lambda/generator/`):

- **Code generation** (`AWSLambdaCodeGenerator`, `LambdaUtils`, `tasks/AWSLambdaCodegenTask`):
  synthesises a `main` that calls `__register` for each `@lambda:Function`-annotated function
  (`Constants.LAMBDA_REG_FUNCTION_NAME = "__register"`, `Constants.java:25`) and then `__process`
  (`LambdaUtils.java:132`), plus the deployment artifacts (zip / docker layer).
- **Detection** (`LambdaFunctionVisitor.java:71`): matches annotations whose symbol name is
  exactly `Function`.
- **Validations**: `A000` — lambda functions only allowed in specific files
  (`validators/AWSLambdaCodeAnalyzerTask.java:51`); `AZ010` — a user-written `main` is not allowed
  (`validators/MainFunctionValidator.java:62`); `AZ011` — lambda functions not allowed inside
  submodules (`validators/SubmoduleValidator.java:45`); `AWS-Lambda-001` — docker/build failures
  (`tasks/AWSLambdaCodegenTask.java:77`).

Implication for the render: the plugin's entire contract keys off the `Function` annotation.
`old` did not surface it, so the render omitted the one construct the plugin requires. `new` fixes
this. The plugin's *constraints* (no user `main`; no lambda functions in submodules) are not
expressible in the render format and are absent from both sides — a documentation-level gap, not a
render defect. `__register`/`__process` are plugin-internal entry points that a user should never
call; both renders expose them, which is mildly noisy but matches the library's own `public`
marking.

## 8. Other considerations

- **Version stability**: upstream `v3.3.0` is the newest tag on the repo; Ballerina Central
  reports `deprecated: null`, keywords `[aws, lambda, serverless, cloud]`. Stable 3.x, not
  pre-1.0. No deprecation warnings to surface.
- **Size**: 365 lines — negligible token cost. The +22 lines buy the module's most important
  construct, so the size/value trade is strongly positive.
- **README staleness (library-side, both renders)**: the embedded README links to
  `.../ballerinax/aws.lambda/0.0.0/aws.lambda/classes/Context` — a `0.0.0` placeholder version in
  the upstream `Package.md`. Faithfully reproduced by both renders; a library bug, not a render
  bug.
- **README is raw Markdown inside a `.bal.txt`** (`## Package Overview` at line 8) — by design of
  the format, delimited by `// --- README ---` / `// --- END README ---`; not a defect.
- **Doc typos carried through** from the source: `# Function Hanlder name` and
  `# Process and excute the handler.` (`code.bal:106,122`). Present in both renders; faithful
  reproduction.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 343 / 365 |
| 2 | `diff -u old/…bal.txt new/…bal.txt` | 2 hunks, +23 / −1; only removed line = `// Unknown type: Context` |
| 3 | `grep -c '^// Unknown type:'` both | old 1, new 0 |
| 4 | `grep -n '^// --- ' both` | old: README/END README/Types/Functions (4); new: same + Annotations at line 362 (5) |
| 5 | `grep -c '^type '` both | 21 / 21 |
| 6 | `grep -c '^class '` / `grep -c '^public annotation'` | old 0/0, new 1/1 |
| 7 | `git ls-remote --tags <repo>` | `v3.3.0` → `a4866dc31eaf564d8b78c5ebf45cc667b51ab3ab` (newest tag) |
| 8 | `git clone --depth 1 --branch v3.3.0 …` | succeeded |
| 9 | `diff src/ballerina/{code,events,annotation}.bal <bala>/modules/aws.lambda/` | all identical (`CODE_SAME`, `EVENTS_SAME`, `ANN_SAME`) |
| 10 | `grep -n version src/ballerina/Ballerina.toml` | `version = "3.3.0"` — pin confirmed on upstream side |
| 11 | `grep -nE '^(public )?(type\|class\|function\|const\|annotation\|isolated function)' <bala>/modules/aws.lambda/*.bal` | 21 public records, 1 public class, 2 public functions, 1 public const annotation, 6 non-public symbols |
| 12 | Python JSON compare of old/new `.json` | `readme`, `description`, `functions` equal; `typeDefs` 22 vs 22 with identical name sets; `annotations` 0 vs 1 |
| 13 | Per-typeDef JSON diff | only `Context` differs; delta = added `"type": "Class"`; its `functions` array identical on both sides |
| 14 | `n['annotations']` dump | `[{"name":"Function","attachmentPoint":"FUNCTION","description":"The annotation, which is used to mark the function as an AWS Lambda function."}]` |
| 15 | `cat <bala>/compiler-plugin/compiler-plugin.json` | plugin id `awslambda`, class `AWSLambdaCompilerPlugin` |
| 16 | `grep -rn 'DiagnosticInfo(' compiler-plugin/src/main/java/…` | codes `AZ010`, `AZ011`, `A000`, `AWS-Lambda-001` |
| 17 | `grep -rn '__register\|__process\|"Function"' compiler-plugin/src/main/java/…` | `Constants.java:25`, `LambdaUtils.java:132`, `LambdaFunctionVisitor.java:71` |
| 18 | `cat src/samples/sample1/functions.bal` | confirms `@lambda:Function` + `lambda:Context` are the user-facing API |
| 19 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerinax/aws.lambda/3.3.0` | one module `aws.lambda`; `deprecated: null` |
| 20 | `python3` read of `<bala>/package.json` | `"export": ["aws.lambda"]` — single default module, no submodules |
| 21 | `ls <bala>/…/modules/` | `aws.lambda` only |
| 22 | `sed -n '26,35p' old/…bal.txt`, `Read new/…bal.txt` (full, 365 lines) | render bodies reviewed line by line |
| 23 | Cross-check of `OLD_AND_NEW_DIFFS/aws.lambda_diff.md` | its counts (343/365, +23/−1, 2 hunks, 1→0 unknown types, 8 added declarations, 0 removed) reproduced independently and confirmed |

## 10. Caveats and unverified items

- The compiler plugin was reviewed from **upstream Java source at `v3.3.0`**, not by decompiling
  the shipped `aws.lambda-compiler-plugin-3.3.0.jar`. Since all three `.bal` files are byte-identical
  between tag and bala, the jar almost certainly matches, but jar↔source equivalence is
  **unverified**.
- Neither render was compiled. The claim that the `FunctionType` reference makes the render
  non-compiling is inferred from the fact that `FunctionType` is declared non-public
  (`code.bal:80`) and appears in no render; it was **not** confirmed with `bal build`. Note this
  affects `old` and `new` equally.
- The brief's statement that both sides were produced at the same pinned version was taken as
  given; I verified the upstream tag and bala are at `3.3.0`, but I did not re-run either render
  pipeline to confirm provenance of the two `.bal.txt` files.
- Whether `isolated` / `const` qualifier loss is an intentional simplification of the render
  format or an omission is **unverified** — I did not read `to-syntax-string.ts` on either side.

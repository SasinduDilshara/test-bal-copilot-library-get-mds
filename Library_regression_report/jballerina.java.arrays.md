# ballerina/jballerina.java.arrays 1.6.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/jballerina.java.arrays` |
| Pinned version | `1.6.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-jballerina.java.arrays |
| Tag reviewed | `v1.6.1` (commit `60699a2`, `[Gradle Release Plugin] - pre tag commit: 'v1.6.1'`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/jballerina.java.arrays/1.6.1/java21` |
| Old render | `115` lines |
| New render | `115` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

The `old` and `new` renders are **byte-identical** (same MD5 `7f315877108a67df5e50f72377117a23`), and the
stage-1 JSONs are byte-identical too (181 lines each, `diff` empty). Spec v2 changed nothing for this
library, which is expected: the module exports only 6 plain functions, no type definitions, no clients,
no services, no annotations — none of the constructs (`Error`, untagged objects, `Other`, version-qualified
type refs) that spec v2 rewrites are present here.

Both renders are faithful to the published bala: the README block is character-for-character identical to
`docs/README.md`, all 6 public default-module functions are present with correct parameter names, types,
defaults, return types and full doc comments. Coverage is complete — there is no public symbol in the
default module missing from either render.

One shared inaccuracy exists on both sides (so not a regression): `newInstance`'s **rest parameter**
`int ...dimensions` is rendered as a plain `int dimensions`.

## 2. Change inventory

| metric | old | new |
|---|---|---|
| render lines | 115 | 115 |
| JSON lines | 181 | 181 |
| render MD5 | `7f315877108a67df5e50f72377117a23` | `7f315877108a67df5e50f72377117a23` |
| `// Unknown type:` lines | 0 | 0 |
| `// --- ` section markers | 3 (`README`, `END README`, `Functions`) | 3 (identical) |
| functions | 6 | 6 |
| typeDefs / clients / services / annotations (JSON) | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |

Declarations added: **0**. Removed: **0**. Modified: **0**.
`diff old new` on both the `.bal.txt` and the `.json` returned exit code 0 with no output.

The precomputed diff at `OLD_AND_NEW_DIFFS/jballerina.java.arrays_diff.md` (0 added, 0 removed, 0 hunks,
"The two files are identical") is confirmed accurate.

Rendered declaration set (identical both sides), `new/...bal.txt`:

```
58: function newInstance(handle classType, int dimensions) returns handle;
71: function get(handle array, int index) returns handle;
84: function set(handle array, int index, handle element) returns ();
94: function getLength(handle array) returns int;
105: function fromHandle(handle array, string jType, string bType = "default") returns any[]|error;
115: function toHandle(any[] array, string jType) returns handle|error;
```

## 3. Correctness against library source

The bala module source and the upstream `v1.6.1` clone are **identical**
(`diff <bala>/modules/jballerina.java.arrays/jarray_utils.bal src/ballerina/jarray_utils.bal` → rc 0),
so there is no bala-vs-GitHub disagreement to adjudicate.

All 6 rendered functions checked line-by-line against `src/ballerina/jarray_utils.bal` (= bala
`modules/jballerina.java.arrays/jarray_utils.bal`):

| render | source line | source signature | match |
|---|---|---|---|
| `newInstance(handle classType, int dimensions) returns handle` | :29 | `public isolated function newInstance(handle classType, int ...dimensions) returns handle` | **partial** — rest param flattened (see §5) |
| `get(handle array, int index) returns handle` | :45 | `public isolated function get(handle array, int index) returns handle` | yes |
| `set(handle array, int index, handle element) returns ()` | :61 | `public isolated function set(handle array, int index, handle element)` | yes (implicit nil return rendered explicitly) |
| `getLength(handle array) returns int` | :73 | `public isolated function getLength(handle array) returns int` | yes |
| `fromHandle(handle array, string jType, string bType = "default") returns any[]\|error` | :86 | `public isolated function fromHandle(handle array, string jType, string bType = "default") returns any[]\|error` | yes — default `"default"` preserved |
| `toHandle(any[] array, string jType) returns handle\|error` | :218 | `public isolated function toHandle(any[] array, string jType) returns handle\|error` | yes |

Doc comments: 18 `# + ` parameter/return doc lines in the render; the source carries the same 18 across the
6 functions. Doc text, including the embedded ` ```ballerina ` examples, is reproduced verbatim.

README: `diff <bala>/docs/README.md <(render lines 8–42)` → identical, 35 lines, no truncation.

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff old/ballerina_jballerina.java.arrays.bal.txt new/ballerina_jballerina.java.arrays.bal.txt` → no
  output, exit 0; MD5s match.
- `diff old/ballerina_jballerina.java.arrays.json new/ballerina_jballerina.java.arrays.json` → no output,
  exit 0. The regression cannot be hidden at the JSON layer either.
- Line counts, section markers, `// Unknown type:` counts (0/0) and declaration lists all match.

Since the two artefacts are bit-for-bit equal, no declaration, parameter, default, return type, doc line,
annotation or README fragment can have been dropped, truncated or mangled by spec v2 for this library.

## 5. Issues in `new` (independent of `old`)

**1 issue** — present in both sides, so it is a pre-existing extractor limitation, not a spec-v2 defect:

1. **Rest parameter flattened to a scalar.** Source (`jarray_utils.bal:29`) declares
   `public isolated function newInstance(handle classType, int ...dimensions) returns handle`.
   The stage-1 JSON models `dimensions` as `{"name":"dimensions","type":{"name":"int"},"optional":true}` —
   type `int`, no `...`, no array, no `default` — and the renderer emits
   `function newInstance(handle classType, int dimensions) returns handle;`.
   Consequence for an LLM consumer: the multi-dimensional form
   `arrays:newInstance(stringClass, 2, 3)`, which the real API supports and which the doc string explicitly
   describes ("The dimensions of the array", "panic … if zero dimensions have been provided"), looks like an
   arity error against the rendered signature. The single-dimension form shown in the README still type-checks.
   Verified identical in `old/…json` and `new/…json`.

No invented symbols, no wrong types elsewhere, no encoding problems, no malformed Ballerina. The rendered
text parses as a valid sequence of Ballerina function declarations apart from the deliberate use of `;`
in place of a body (a render convention used repo-wide).

## 6. Coverage gaps vs. the library

**0 gaps.**

- The bala exports exactly one module: `package.json` `"export": ["jballerina.java.arrays"]`, and
  `modules/` contains only `jballerina.java.arrays` — i.e. the default module *is* the whole package.
  There is no submodule-only API, so the shared `getDefaultModule()`-only limitation costs nothing here.
- `grep -n '^public ' src/ballerina/*.bal` returns exactly 6 symbols: `newInstance`, `get`, `set`,
  `getLength`, `fromHandle`, `toHandle`. All 6 appear in both renders.
- `util_functions.bal` (221 lines, 34 functions such as `wrapIntToChar`, `getBFloatFromJDouble`) declares
  **no** `public` symbols — they are module-private helpers. Their absence from the render is correct, not
  a gap.
- No public types, constants, enums, classes, listeners, services or annotations exist in the module, so
  nothing of those kinds could be missing. Central metadata for `ballerina/jballerina.java.arrays/1.6.1`
  lists a single module and confirms the package is not deprecated.

## 7. Compiler plugin

`has_plugin: false` in the manifest, confirmed independently:
- Bala listing has no `compiler-plugin/` directory — the full tree under the bala root is
  `bala.json`, `dependency-graph.json`, `package.json`, `docs/{icon.png,README.md}`,
  `modules/jballerina.java.arrays/{jarray_utils.bal,util_functions.bal}`. Nothing else.
- Upstream `v1.6.1` clone contains no `*compiler-plugin*` directory (`ls -d *compiler*` → no match); the
  Gradle build has only `ballerina/`, `build-config/`, `test-utils/`.
- `Ballerina.toml` declares no `[[platform.java21.dependency]]` outside a `testOnly` test-utils jar and no
  compiler-plugin section.

This library ships no compiler plugin, so there are no code actions, validations, generated artefacts or
plugin-defined annotations that ought to have surfaced in the render.

## 8. Other considerations

- **Stable, low-churn module.** v1.6.1 is the newest tag on the repo (`git ls-remote --tags` — highest is
  `v1.6.1`); no version drift risk. Central reports `pullCount` 1859, `deprecated: null`.
- **Distribution mismatch is benign.** The bala was built with `ballerina_version: 2201.12.0` but lives in
  the 2201.13.4 distribution repo. This is normal for bundled langlib-adjacent modules and did not affect
  extraction (both sides consumed the same bala).
- **Qualifier stripping is a repo-wide render convention, not a defect here.** All 6 source functions are
  `public isolated function`; the render emits bare `function`. No render in this corpus emits
  `public`/`isolated` from the extractor (the `isolated function` hits found in `ai.eval` and `ai.agent`
  renders are README code-block text, not generated declarations). Flagged for awareness only — it applies
  uniformly to old and new and to every library.
- **Size/token impact: zero delta.** 115 lines on both sides; this is one of the smallest renders in the
  corpus, so spec v2 neither inflates nor shrinks it.
- **Cross-module dependency surface: none.** Unlike `sql`/`io`/`time`, this module exports no types that
  other packages reference by qualified name, so the §4/§5 "foundational type fidelity" concern
  (e.g. `sql:Error`, `time:Utc`) does not apply. Its only external reference is `ballerina/jballerina.java`
  used internally in `@java:Method` annotations, which are not part of the rendered surface.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt old/*.json new/*.json` | 115 / 115 / 181 / 181 |
| 2 | `md5 -q old/…bal.txt` ; `md5 -q new/…bal.txt` | both `7f315877108a67df5e50f72377117a23` |
| 3 | `diff old/…bal.txt new/…bal.txt` | no output, rc 0 |
| 4 | `diff old/…json new/…json` | no output, rc 0 |
| 5 | `grep -c '^// Unknown type:' old new` | 0 and 0 |
| 6 | `grep -n '^// --- ' new/…bal.txt` | lines 7, 44, 46 — README / END README / Functions |
| 7 | `ls <bala>` then `find <bala> -maxdepth 4` | `java21/` only; no `compiler-plugin/` |
| 8 | `cat <bala>/package.json` | version 1.6.1, `export: ["jballerina.java.arrays"]`, ballerina_version 2201.12.0 |
| 9 | `ls <bala>/java21/modules` | single module `jballerina.java.arrays` → no submodule API |
| 10 | `grep -n 'public' <bala>/…/jarray_utils.bal` | 6 public functions at lines 29, 45, 61, 73, 86, 218 |
| 11 | `grep -n 'public' <bala>/…/util_functions.bal` | 34 functions, **zero** public |
| 12 | `wc -l <bala>/…/*.bal` | jarray_utils 317, util_functions 221 |
| 13 | `git ls-remote --tags <repo>` | `v1.6.1` exists (`3dc817e` / `60699a2`), highest tag |
| 14 | `git clone --depth 1 --branch v1.6.1 …` then `git describe --tags` | `v1.6.1`, HEAD `60699a2` |
| 15 | `diff <bala>/…/jarray_utils.bal src/ballerina/jarray_utils.bal` | rc 0 — bala == upstream tag |
| 16 | `grep -n '^public ' src/ballerina/*.bal` | same 6 signatures as #10 |
| 17 | `diff <bala>/docs/README.md <(render lines 8–42)` | identical, "README IDENTICAL" |
| 18 | `wc -l <bala>/docs/README.md` | 35 lines = render lines 8–42 |
| 19 | `grep -c '^# + ' new/…bal.txt` | 18 doc-param lines |
| 20 | `grep -n '^function ' new/…bal.txt` | 6 declarations at lines 58, 71, 84, 94, 105, 115 |
| 21 | `python3` dump of `new/…json` top-level | typeDefs 0, clients 0, functions 6, services 0, annotations 0 |
| 22 | `python3` dump of `functions[0]` (`newInstance`) | `dimensions` → `type:{name:"int"}, optional:true`, no `...`, no default |
| 23 | `python3` dump of `functions[4]` (`fromHandle`) | `bType` → `optional:true, default:"\"default\""` — default preserved |
| 24 | `cat src/ballerina/Ballerina.toml` | version 1.6.1, distribution 2201.12.0, only a `testOnly` platform dep |
| 25 | `ls -d *compiler*` in clone | no match — no compiler plugin |
| 26 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/jballerina.java.arrays/1.6.1` | 1 module, `deprecated: null`, ballerinaVersion 2201.12.0, pullCount 1859 |
| 27 | `grep -rn '\.\.\.' --include='*.bal.txt'` across corpus | no rest-param `...` in this library's renders (confirms #22) |

## 10. Caveats and unverified items

- **`set` return rendering.** The source declares `set(...)` with no return type; the render writes
  `returns ()`. These are semantically equivalent in Ballerina, so I treated it as correct rather than as a
  discrepancy. Not independently confirmed against a renderer spec.
- **Rest-parameter handling is diagnosed at the JSON layer, not at the extractor source.** I confirmed the
  stage-1 JSON already lacks the rest marker (evidence #22), so the loss happens in
  `CopilotLibraryManager`/`ModelToJsonConverter`, not in `toSyntaxString`. I did not read the Java extractor
  code to pinpoint the exact line, since both sides produce identical JSON and the question is out of scope
  for a regression audit.
- **`isolated`/`public` qualifier omission** is asserted to be a corpus-wide convention on the basis of a
  grep across the render corpus (evidence: the only `isolated function` hits are inside README code blocks).
  I did not read the renderer source to confirm this is intentional.
- Everything else in this report was verified directly by a command listed in §9.

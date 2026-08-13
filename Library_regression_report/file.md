# ballerina/file 1.13.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/file` |
| Pinned version | `1.13.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-file |
| Tag reviewed | `v1.13.0` |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/file/1.13.0/java21` |
| Old render | `416` lines |
| New render | `456` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library is identical on both sides (same bala, same pinned version); the bala's
`modules/file/*.bal` are byte-identical to the GitHub `v1.13.0` tag (all 9 files, `diff -q`).

`new` is strictly additive over `old`. It replaces all 14 `// Unknown type:` placeholders with real
definitions (13 error types + the `Listener` class with its 6 methods) and removes both
version-qualified type references (`ballerina/file:1.13.0:MetaData` → `MetaData`), which were not
valid Ballerina. Nothing present in `old` was dropped, truncated, or made less accurate.

The stage-1 JSON is nearly identical between the two sides (35 typeDefs and 19 functions on both).
The only JSON deltas are `"baseType": "error"` added to the 13 error typeDefs, `"type": "Class"`
added to `Listener`, `"optional": false` dropped from the 3 service methods, and the two unqualified
return types. Everything else new in the render was already in `old`'s JSON — the `main` renderer
simply discarded it.

The remaining accuracy problems in `new` (error `distinct`ness, the fabricated `Listener.init`
signature, flattened rest parameters, missing `public`/`isolated`) are extractor-level and, except
for `Listener.init`, are equally present in `old`.

## 2. Change inventory

Line counts (`wc -l`): old `416`, new `456` (+40).

Declarations added in `new` (20), verified by diffing the extracted declaration sets
(`grep -nE '^(type|enum|class|const|function|service|# )'` on both files):

| Kind | Count | Names |
|---|---|---|
| Error type defs | 13 | `Error`, `InvalidOperationError`, `PermissionError`, `FileSystemError`, `FileNotFoundError`, `NotLinkError`, `IOError`, `SecurityError`, `InvalidPathError`, `InvalidPatternError`, `RelativePathError`, `UNCPathError`, `GenericError` |
| Class | 1 | `Listener` |
| Class methods | 6 | `init`, `'start`, `gracefulStop`, `immediateStop`, `attach`, `detach` |

Declarations removed in `new`: **0**.

Modified (3 sites):

| Site | old | new |
|---|---|---|
| `getMetaData` return | `ballerina/file:1.13.0:MetaData & readonly\|Error` | `MetaData & readonly\|Error` |
| `readDir` return | `ballerina/file:1.13.0:MetaData[] & readonly\|Error` | `MetaData[] & readonly\|Error` |
| `// --- Service ---` block | unqualified `ListenerConfig` / `FileEvent`, no `# + event -` docs | `file:ListenerConfig` / `file:FileEvent`, `# + event - The File event` added to all 3 methods |

Signals: `// Unknown type:` — old `14`, new `0`. Version-qualified refs — old `2`, new `0`.
Section markers `// --- ` — `5` on both. Doc-comment lines (`^#`) — old `174`, new `189`.

`comm -23 <(sort old) <(sort new)` yields exactly 20 non-blank lines: the 14 `// Unknown type:`
placeholders, the 2 malformed version-qualified function lines, and the 4 service-block lines that
were replaced by their `file:`-qualified equivalents. No library content was lost.

Unchanged between sides: `name`, `description`, `readme` (byte-equal in both JSONs), all 13
constants, `FileEvent`, the 4 enums, `Service`, `MetaData`, `ListenerConfig`, and all 19 module
functions apart from the two return types above.

## 3. Correctness against library source

Everything `new` adds was checked against the bala (authoritative) and the tag clone.

| Rendered in `new` | Source | Match |
|---|---|---|
| `type Error error;` (l.135) | `file_errors.bal:54` `public type Error distinct error;` | name + doc yes; `distinct` lost |
| 12 error subtypes (l.138–171) | `file_errors.bal:18–51`, each `public type X distinct Error;` | names + docs yes; `distinct Error` parentage lost (see §5.2) |
| `class Listener` (l.204) | `service_endpoint.bal:24` `public isolated class Listener` | yes (`public isolated` not rendered) |
| `function 'start() returns error?` (l.209) | `service_endpoint.bal:39` | yes |
| `function gracefulStop() returns error?` (l.213) | `service_endpoint.bal:46` | yes |
| `function immediateStop() returns error?` (l.217) | `service_endpoint.bal:53` | yes |
| `function attach(Service s, string[]\|string\|() name = ())` (l.221) | `service_endpoint.bal:62` `attach(Service s, string[]\|string? name = ())` | yes (`?` expanded to `\|()`) |
| `function detach(Service s) returns error?` (l.225) | `service_endpoint.bal:70` | yes |
| `function init(string path = "", boolean recursive = false, ListenerConfig listenerConfig)` (l.205) | `service_endpoint.bal:31` `public isolated function init(*ListenerConfig listenerConfig) returns error?` | **no** — see §5.1 |
| `getMetaData ... returns MetaData & readonly\|Error` (l.287) | `file.bal:98` `returns (MetaData & readonly)\|Error` | yes (`&` binds tighter than `\|`, so equivalent) |
| `readDir ... returns MetaData[] & readonly\|Error` (l.297) | `file.bal:120` `returns (MetaData[] & readonly)\|Error` | yes |
| service `file:FileEvent event` (l.447/451/455) | `file_common.bal:21` `public type FileEvent record {\| string name; string operation; \|}` | yes; the `file:` prefix is correct for user code that does `import ballerina/file;` |

Also spot-checked, unchanged on both sides and correct: all 19 function names and parameter lists
against `file.bal:25–192` and `file_path.bal:31–278`; the 4 enums and their members against
`file_common.bal:32–71`; `MetaData`'s 6 fields and `time:Utc modifiedTime` against
`file_meta_data.bal:28–35` (the `// Special Agent Note: Utc FROM ballerina/time package` annotation
is present on both sides).

## 4. Regressions

**None found.**

Checked to conclude this:
- `comm -23 <(sort old) <(sort new)` — the only 20 lines unique to `old` are the 14 degraded
  placeholders, the 2 non-compiling version-qualified return lines, and 4 service lines superseded
  by qualified equivalents. No declaration, parameter, default, return type, or doc sentence exists
  only in `old`.
- Declaration-set diff — 20 additions, 0 removals.
- JSON diff — `readme` and `description` byte-equal; typeDef names identical and in the same order;
  the 19 `functions` entries identical except the 2 return-type strings, which improved.
- Doc-comment line count rose 174 → 189 (13 error-type docs + 3 `# + event -` lines, less
  formatting); no doc line was dropped.
- The `file:` qualification added in the service block is more correct, not less: that block is a
  user-code template that already used `file:Service` and `file:Listener` on both sides, so `old`'s
  bare `ListenerConfig`/`FileEvent` would not resolve there.

## 5. Issues in `new` (independent of `old`)

1. **`Listener.init` signature is fabricated and would not compile** (`new` l.205):
   `function init(string path = "", boolean recursive = false, ListenerConfig listenerConfig) returns error?;`
   The real signature is `init(*ListenerConfig listenerConfig)` (`service_endpoint.bal:31`). The
   extractor flattened the included-record parameter into `path` + `recursive` **and** kept the
   record parameter, producing three parameters where one exists; it also invents a default `""`
   for `path`, which is a required field of `ListenerConfig` (`service_endpoint.bal:79-82`); and it
   emits a parameter with no default after two defaulted ones, which is invalid Ballerina. Note the
   defect is in the JSON (`typeDefs[Listener].functions[init].parameters`), identical on **both**
   sides — `old` merely never rendered it (`// Unknown type: Listener`). So this is new-side visible
   but not caused by the renderer change; the net effect is still positive (5 correct methods gained
   against 1 wrong constructor).
2. **Error hierarchy flattened.** All 13 error types render as `type X error;`, losing `distinct` on
   `Error` and losing `distinct Error` on the 12 subtypes. A consumer reading the render cannot tell
   that `file:FileNotFoundError` is a subtype of `file:Error`, nor that these are distinct (so
   `error` values do not implicitly belong to them). This matters for a foundational module whose
   `file:Error` is matched by dependents. JSON carries only `"baseType": "error"`, so the renderer
   has no better information available.
3. **Rest parameters flattened, one with the wrong type.**
   `joinPath(string... parts)` (`file_path.bal:259`) renders as `function joinPath(string parts)` —
   the element type, not the parameter type; a caller following the render can pass only one
   segment, and the doc example above it (`file:joinPath("/", "foo", "bar")`) contradicts the
   signature. `copy(..., CopyOption... options)` (`file.bal:141-142`) renders as `CopyOption[] options`.
   Identical in `old` (the `functions` arrays are equal apart from the two return types).
4. **`Service` rendered as an empty class.** Source is
   `public type Service distinct service object {};` (`file_common.bal:74`); both renders emit
   `class Service {}`. This misrepresents the service-object contract; the actual remote-method
   contract survives only in the `// --- Service ---` template block.
5. **Closed records rendered as open.** `FileEvent`, `MetaData`, and `ListenerConfig` are all
   `record {| ... |}` in source; both renders emit `record { ... }`.
6. **`ListenerConfig.recursive` default lost.** Source: `boolean recursive = false;`
   (`service_endpoint.bal:81`). Render: `boolean recursive?;` — an optional field with no default,
   which is a different type. Both sides.
7. **`public` and `isolated` qualifiers absent everywhere.** Every function in the library is
   `public isolated function`; the render emits bare `function`. `Listener` is
   `public isolated class`; the render emits `class`. Both sides.
8. **18 orphan doc-continuation lines** that are not prefixed with `#` and sit between the doc block
   and the declaration (e.g. `new` l.245 `create the given current directory.`, l.307–309, l.344–348,
   l.404–407). These would be parse errors if the render were compiled. Count is `18` on both sides
   (same awk filter run against each file).

## 6. Coverage gaps vs. the library

The bala exports exactly one module (`package.json` `"export": ["file"]`; `modules/` contains only
`file/`; Central lists one module). So there is no submodule-only API and no shared submodule gap.

Public symbols of the default module absent from **both** renders — **2**:

| Symbol | Source | Notes |
|---|---|---|
| `pathSeparator` | `file_path.bal:21` `public final string pathSeparator = isWindows ? "\\" : "/";` | Module-level `public final` variables are not extracted (not in `typeDefs` or `functions` of either JSON, verified programmatically). |
| `pathListSeparator` | `file_path.bal:22` `public final string pathListSeparator = isWindows ? ";" : ":";` | Same. |

Both are described prominently in the README section of the render (lines 13–14 of each file), so an
LLM sees them named but gets no declaration — mildly worse than either extreme.

Every other public declaration found by
`grep -n "^public ..." *.bal` (44 hits: 19 functions, 4 enums, 14 type defs, `Service`, `MetaData`,
`ListenerConfig`, `FileEvent`, `Listener`, 2 final vars) is present in `new`.

## 7. Compiler plugin

`has_plugin: true`, confirmed from the bala:
`compiler-plugin/compiler-plugin.json` declares `plugin_id: "file-compiler-plugin"`,
`plugin_class: io.ballerina.stdlib.file.compiler.FileCompilerPlugin`, jar
`file-compiler-plugin-1.13.0.jar`.

What it contributes (read from the clone, `compiler-plugin/src/main/java/io/ballerina/stdlib/file/compiler/`):

- **`FileServiceValidator`** — compile-time validation of any service attached to a `file:Listener`:
  remote method names restricted to `onCreate` / `onModify` / `onDelete` (FILE_103); `remote`
  keyword required (FILE_102); the only allowed parameter type is `file:FileEvent` (FILE_101) and
  exactly one such parameter (FILE_105); return type must be `error?` (FILE_104); at least one
  remote method required (FILE_106). Source: `ErrorCodes.java:26-33`, `FileServiceValidator.java:53-151`.
- **Static code analyzer** (`staticcodeanalyzer/`) — two VULNERABILITY rules:
  `AVOID_INSECURE_DIRECTORY_ACCESS` and `AVOID_PATH_INJECTION` (`FileRule.java`), implemented by
  `InsecureDirectoryAccessAnalyzer` and `FilePathInjectionAnalyzer`. These are scan-time only.
- No code actions, no generated artifacts, no annotations.

Does anything the plugin implies fail to surface in the render? Largely no: the service contract the
validator enforces is exactly what the `// --- Service ---` block emits (three remote methods,
`file:FileEvent` parameter, `error?` return) — and `new` states it slightly better than `old` by
qualifying `file:FileEvent` and documenting the `event` parameter. Two gaps worth noting:
the render does not say that the three remote methods are mutually optional but that **at least one**
is required (FILE_106), and it does not convey that no other method names are permitted (FILE_103) —
an LLM could reasonably invent `onRename`. Neither is a change between `old` and `new`; both derive
from trigger metadata the extractor does not carry.

## 8. Other considerations

- Not deprecated. Central: `deprecated: null`, `pullCount: 49637`, `ballerinaVersion: 2201.12.0`,
  `graalvmCompatible: Yes`, single module `file`.
- Stable 1.x version; no pre-1.0 caveat.
- Size: 456 lines / 40 lines larger than `old` (+9.6%). Negligible token impact for a clear coverage
  gain (13 error types + a 6-method class).
- Doc quality is good — every function carries a runnable ```ballerina example — but the 18
  unprefixed continuation lines (§5.8) mean the render as a whole is not compilable Ballerina on
  either side. It is consumed as context, not compiled, so this is cosmetic-to-moderate.
- The two lost `public final` separators (§6) are the only genuine API omission and are shared.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v1.13.0 https://github.com/ballerina-platform/module-ballerina-file …/work/file/src` | tag exists, clone OK |
| `wc -l old/ballerina_file.bal.txt new/ballerina_file.bal.txt` | 416 / 456 |
| `grep -c '^// Unknown type:'` old / new | 14 / 0 |
| `grep -c '^// --- ' ` (section markers) | 5 / 5 |
| `grep -c '^#'` (doc lines) old / new | 174 / 189 |
| `diff` of declaration sets (`grep -nE '^(type\|enum\|class\|const\|function\|service\|# )'`) | +20 declarations, −0 |
| `comm -23 <(sort old) <(sort new)` | 20 non-blank lines, all placeholders / malformed / superseded |
| JSON: `len(typeDefs)`, `len(functions)`, `len(services)`, `len(clients)`, `len(annotations)` both sides | 35 / 19 / 1 / 0 / 0 — identical |
| JSON: `o['readme']==n['readme']`, `o['description']==n['description']` | `True`, `True` |
| JSON: typeDef name lists equal | `True` |
| JSON: per-typeDef diff | only `baseType:"error"` on 13 error types, `type:"Class"` on `Listener` |
| JSON: per-function diff | only `getMetaData` / `readDir` return-type strings |
| JSON: service diff | only `optional:false` removed from the 3 methods |
| `diff -q` bala `modules/file/*.bal` vs clone `ballerina/*.bal` (9 files) | all identical |
| `grep -n "^public …" ballerina/*.bal` | 44 public declarations enumerated |
| JSON decl-name membership test for `pathSeparator` / `pathListSeparator` | absent from both sides |
| `grep -n "joinPath" bala/file_path.bal` | `:259 public isolated function joinPath(string... parts)` |
| `sed -n '135,160p' bala/file.bal` | `copy(..., CopyOption... options)` confirmed |
| `service_endpoint.bal:31` | `public isolated function init(*ListenerConfig listenerConfig) returns error?` |
| `service_endpoint.bal:79-82` | `ListenerConfig record {\| string path; boolean recursive = false; \|}` |
| `file_common.bal:74` | `public type Service distinct service object {};` |
| `file_errors.bal:18-54` | 12 `distinct Error` subtypes + `Error distinct error` |
| awk count of unprefixed doc-continuation lines (past line 58) | 18 old / 18 new |
| `cat bala/compiler-plugin/compiler-plugin.json` | plugin id/class/jar confirmed |
| `ErrorCodes.java:26-33` | FILE_101…FILE_106 enumerated |
| `FileRule.java` | 2 VULNERABILITY static-analysis rules |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/file/1.13.0` | not deprecated, 1 module, 49637 pulls |

## 10. Caveats and unverified items

- The `Listener.init` parameter list (`path`, `recursive`, `listenerConfig`) originates in the
  stage-1 JSON on **both** sides, so I can attribute it to the extractor rather than the renderer,
  but I did not read the extractor Java to confirm *why* it expands `*ListenerConfig` and then also
  keeps the record parameter. The behaviour itself is verified from the two JSON files.
- I did not compile either render; claims that specific lines "would not compile" are based on
  reading Ballerina grammar (required parameter after defaulted parameters; unprefixed lines inside
  a documentation block), not on running `bal build`.
- The `// --- Service ---` template block's content comes from LS trigger metadata, not from the
  library sources; I verified its method names/types against `file_common.bal` and the compiler
  plugin's validator, but I did not inspect the trigger-metadata model files themselves.
- Both renders were taken as given; I did not re-run the two-stage pipeline to reproduce them.

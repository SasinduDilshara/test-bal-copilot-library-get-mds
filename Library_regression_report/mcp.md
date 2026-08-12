# ballerina/mcp 1.2.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/mcp` |
| Pinned version | `1.2.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-mcp |
| Tag reviewed | `v1.2.0` (commit `7533ffbeea42219fe1f32dfee4033b5483e2896b`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/mcp/1.2.0/java21` |
| Old render | `1058` lines (39,247 bytes) |
| New render | `1258` lines (51,548 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a large, uniform improvement for this library and drops nothing that `old` rendered.

- `old` degraded **28** public symbols to bare `// Unknown type: <Name>` lines (24 error types, 3 classes `Listener` / `StreamableHttpListener` / `Session`, and the `Cursor` type alias). `new` emits real definitions for all 28: `grep -c '^// Unknown type:'` → **28** in `old`, **0** in `new`.
- `old` emitted **22** version-qualified self-references (`ballerina/mcp:1.2.0:RequestId`, …) across 8 lines. `new` emits **0**.
- `old` rendered the Service section as a single empty `service mcp:Service on new mcp:Listener(...) { }` — no handler shape, no annotations, and it named the **deprecated** listener with an invented `listenTo = 0` default. `new` renders all **4** service types on the current `mcp:StreamableHttpListener`, with handler templates, parameter-slot rules and annotation guidance.
- `old` rendered **1** of the library's **3** annotations; `new` renders all 3, and with the library's own doc text instead of a stale trigger-metadata string.
- Public default-module symbol coverage: `102` public symbols; **30** absent as declarations from `old`, **0** absent from `new`.
- Declarations removed by `new`: **0** (verified by set difference, §2).

The remaining defects in `new` are fidelity limitations on the newly-added material (error-type hierarchy flattened, `Session.getWithType` signature mangled, `isolated` and class-level docs dropped) plus inaccuracies inherited unchanged from `old`. None of them removes information that `old` supplied.

## 2. Change inventory

Mechanical shape of the diff (`diff -u old new` → 385 lines, 10 hunks; matches `OLD_AND_NEW_DIFFS/mcp_diff.md`: +239 / −39).

Top-level declarations, extracted with
`grep -hoE "^(public )?(type|class|enum|annotation|client class|const) [A-Za-z_]+|^(public )?(const|annotation) [A-Za-z_<>|]+ [A-Za-z_]+"`:

| kind | old | new | delta |
|---|---|---|---|
| `type` | 52 | 77 | **+25** |
| `class` | 4 | 7 | **+3** |
| `client class` | 1 | 1 | 0 |
| `enum` | 4 | 4 | 0 |
| `const` | 20 | 20 | 0 |
| `annotation` | 1 | 3 | **+2** |
| **total** | **82** | **112** | **+30** |

`comm -23 <(sort decl_old) <(sort decl_new)` → **empty**: nothing declared in `old` is missing from `new`.

Added top-level declarations (30):

- **24 error types** — `Error`, `ClientError`, `StreamError`, `TransportError`, `ServerResponseError`, `SseEventStreamError`, `JsonRpcMessageTransformationError`, `MissingSseDataError`, `TypeConversionError`, `InvalidMessageTypeError`, `MalformedResponseError`, `StreamableHttpTransportError`, `HttpClientError`, `UnsupportedContentTypeError`, `SessionOperationError`, `ResponseParsingError`, `SseStreamEstablishmentError`, `UninitializedTransportError`, `ClientInitializationError`, `ProtocolVersionError`, `ListToolsError`, `ToolCallError`, `ServerError`, `ParameterBindingError`
- **1 type alias** — `Cursor`
- **3 classes** — `StreamableHttpListener`, `Listener` (with `@deprecated`), `Session`
- **2 annotations** — `Tool`, `StreamableHttpServiceConfig`

Added members (17 methods): `AdvancedService.onListTools`, `AdvancedService.onCallTool`; `StreamableHttpListener` / `Listener` × { `init`, `attach`, `detach`, `'start`, `gracefulStop`, `immediateStop` } (the 6 names are shared, so 6 distinct names for 12 rendered stubs); `Session` × { `init`, `getSessionId`, `set`, `get`, `hasKey`, `keys`, `getWithType`, `remove`, `size`, `clear`, `isEmpty` }. Method stub lines: 9 in `old` → 38 in `new`.

Modified (not added) declarations — all 8 changes are de-qualification of self-references:
`JsonRpcError.id`, `ContentBlock`, `ServerResult`, `JsonRpcMessage`, `Cloneable`, `SessionEntry`, `StreamableHttpClient.init` return, `StreamableHttpClient.subscribeToServerMessages` return.

Service section: 1 empty service block → 4 fully-templated service blocks (+80 lines). Annotations section: 1 → 3.

README: byte-identical between the two renders (`diff` of lines 1–288 → identical) and equal to `docs/README.md` in the bala apart from one trailing blank line.

JSON-level inventory (`old/ballerina_mcp.json` vs `new/ballerina_mcp.json`):

| array | old | new |
|---|---|---|
| `typeDefs` | 108 | 108 |
| `services` | 1 | 4 |
| `clients` | 1 | 1 |
| `annotations` | 1 | 3 |
| `functions` | 0 | 0 (correct — the module exports no top-level public function; `grep -n '^public \(isolated \)\?function'` over the bala returns nothing) |

`typeDefs` is **the same 108 entries with the same names on both sides**; 73 are byte-identical and 35 differ. Across those 35, there are 28 removed JSON lines and **0** of them is unexplained: every removal is either a `ballerina/mcp:1.2.0:`-qualified name being replaced by the bare name, or a `"name": "<X>"` line re-emitted with a trailing comma because a sibling field was added. So the extractor lost no `typeDefs` data. The gains are `"type": "Class"` on `Session`/`Listener`/`StreamableHttpListener` (absent in `old`, which is exactly why `main`'s `renderTypeDef` fell through to `// Unknown type:`), `"baseType"` on the error types and on `Cursor`, and a `functions` array on `AdvancedService`.

## 3. Correctness against library source

The GitHub tag and the bala agree exactly: `diff` of `src/ballerina/{types,error,listener,session,streamable_http_client}.bal` against `bala/java21/modules/mcp/` → **SAME** for all five files. `gradle.properties:3` is `version=1.2.0`. Ballerina Central reports `ballerina/mcp/1.2.0`, one module (`mcp`), `deprecated: null`, `ballerinaVersion: 2201.12.0`.

Checks on what `new` adds:

- **24 error types** — all exist as `public type` in `modules/mcp/error.bal:18–91`. Names and doc strings in the render match the source doc comments verbatim (e.g. render `# Error for failures while binding tool parameters from the incoming request,` / `# such as missing or invalid header values.` == `error.bal:89–91`). The module-private `DispatcherError` (`error.bal:87`) is correctly **not** rendered. Base types: 4 of 24 are correct, 20 are flattened — see §5 N1.
- **`Cursor`** — render `type Cursor string;`, source `types.bal:63` `public type Cursor string;`. Correct.
- **`StreamableHttpListener`** — source `listener.bal:24` `public isolated class StreamableHttpListener`; the 6 rendered members match `listener.bal:29 (init), 45 (attach), 62 (detach), 83 ('start), 96 (gracefulStop), 108 (immediateStop)`. `attach`'s rendered `Service|AdvancedService|StreamableHttpService|StreamableHttpAdvancedService mcpService, string[]|string|() name = ()` matches `listener.bal:50` exactly (`string[]|string? name = ()`).
- **`Listener`** — source `listener.bal:118–121`: `@deprecated public isolated class Listener`. `new` emits `@deprecated` and the same 6 members; correct that it is a delegating twin of `StreamableHttpListener`.
- **`Session`** — source `session.bal:25`; all 11 rendered members match `session.bal:32 (init), 39 (getSessionId), 47 (set), 65 (get), 80 (hasKey), 90 (keys), 103 (getWithType), 114 (remove), 126 (size), 135 (clear), 143 (isEmpty)`. `set(string key, SessionEntry value)`, `get(string key) returns SessionEntry`, `keys() returns string[]`, `size() returns int`, `isEmpty() returns boolean` are all exact. `getWithType` is wrong — §5 N2.
- **`AdvancedService.onListTools` / `onCallTool`** — source `types.bal:649–653`: `remote isolated function onListTools() returns ListToolsResult|ServerError;` and `remote isolated function onCallTool(CallToolParams params, Session? session = ()) returns CallToolResult|ServerError;`. Render matches (`Session|() session = ()`), minus the `isolated` qualifier.
- **`StreamableHttpAdvancedService` rendered as an empty `class { }`** — correct: `types.bal:673–674` really is an empty `distinct service object`; the two required methods are enforced by the compiler plugin, not declared (see §7).
- **4 service types** — the render's claim "This library declares 4 service types" matches `types.bal:649 (AdvancedService), 656 (Service), 663 (StreamableHttpService), 673 (StreamableHttpAdvancedService)`.
- **Listener used in the service templates** — `new` uses `mcp:StreamableHttpListener(int|http:Listener listenTo, mcp:ListenerConfiguration config = {})`, which matches `listener.bal:29` (`listenTo` has **no** default; `*ListenerConfiguration config` is an included record). `old` used the deprecated `mcp:Listener` and invented `listenTo = 0` (its JSON literally carries `"default": "0"`). `new` is the more accurate of the two on both counts.
- **3 annotations** — `types.bal:589` `public annotation McpToolConfig Tool on object function;`, `types.bal:627` `public annotation ServiceConfiguration ServiceConfig on service;`, `types.bal:645` `public annotation StreamableHttpServiceConfiguration StreamableHttpServiceConfig on service;`. All three rendered with correct type constraint and attachment point, and with the library's doc text.
- **Client** — unchanged except de-qualification; `streamable_http_client.bal:17` `public distinct isolated client class StreamableHttpClient` with `initialize`, `subscribeToServerMessages`, `listTools`, `callTool`, `close`, all present in both renders.

## 4. Regressions

**Render-visible regressions: none found.**

Basis for that conclusion:
- Declaration-name set difference `old \ new` is **empty** (§2) — no declaration, class, enum, const or annotation disappeared.
- Only 10 hunks exist in the whole diff; every hunk is either an `// Unknown type:` line becoming a real definition, a de-qualification, or an addition. Every region outside those hunks is byte-identical, so no record field, parameter, default, return type or doc line was dropped anywhere else. Records are untouched: `typeDefs` is the same 108 names, and of the 28 removed JSON lines **0** are unexplained data loss (§2).
- README section identical (§2).
- `39` "removed" diff lines break down as 28 `// Unknown type:` placeholders + 8 rewritten qualified-reference lines + 3 blank-line adjustments; none of them carried information that `new` does not carry better.

One non-render-visible metadata nit (documented, not counted as a regression because it never reaches the `.bal.txt` and cannot mislead a consumer of the render): the `ServiceConfig` annotation object in the JSON loses `"displayName": "Service Configuration"` (present in `old/ballerina_mcp.json`, absent in `new/ballerina_mcp.json`). Its companion change is an improvement — `"description"` goes from the stale `"Define mcp service configuration"` to the library's actual doc `"Annotation to provide configuration to MCP services."` (`types.bal:626`).

## 5. Issues in `new` (independent of `old`)

All of these sit on material `old` did not render at all, so they are quality ceilings on the improvement rather than losses.

- **N1 — error hierarchy flattened (20 of 24 types), `distinct` dropped (24 of 24).** Source declares e.g. `public type ClientError distinct Error;` (`error.bal:30`) and `public type ProtocolVersionError distinct ClientInitializationError;` (`error.bal:75`). `new` renders `type ClientError error;` and `type ProtocolVersionError error;`. Verified programmatically against `error.bal`: 24 public `distinct` error types, **20 baseType mismatches**, all of the form *(declared parent)* → `error`. The 4 correct ones are the intersection types (`Error`→`error`, `StreamError`→`Error & ClientError`, `ServerResponseError`→`Error & ClientError`, `StreamableHttpTransportError`→`TransportError & ClientError`). Consequence for an LLM: it cannot tell that `ToolCallError` is a `ClientError`, that `MissingSseDataError` is a `StreamError`, or that `ParameterBindingError` is a `ServerError`, so it cannot reason about `is`/`ensureType` narrowing or which errors a `ClientError`-typed variable can hold.
- **N2 — `Session.getWithType` signature mangled.** Source (`session.bal:103–106`): `public isolated function getWithType(string key, typedesc<SessionEntry> targetType = <>) returns targetType|Error`. Render (new line 1127): `function getWithType(string key, any & readonly|xml|mcp:Cloneable[]|map<mcp:Cloneable>|table<map<mcp:Cloneable>>|isolated object {} targetType = mcp:SessionEntry) returns targetType|Error;`. The `typedesc<...>` wrapper is lost (the parameter is a type descriptor, not a value of that union), and `= mcp:SessionEntry` is not a valid default expression (the source default is the inferred `<>`). An LLM copying this will write `session.getWithType("k", MyRecord)` against a value-typed parameter, or try `= mcp:SessionEntry` literally.
- **N3 — residual `mcp:` self-qualification.** The same line 1127 is the only place in the whole Types/Client body of `new` that qualifies module-local types (`mcp:Cloneable`, `mcp:SessionEntry`); everywhere else uses bare names. Inconsistent, though harmless.
- **N4 — class-level docs replaced by the `init` doc.** `new` renders `# Initializes the Listener.` as the doc for both `StreamableHttpListener` and `Listener`, and `# Creates a new MCP session with the given session ID.` for `Session`. The real class docs — `# A Streamable HTTP transport listener for handling MCP service requests.` (`listener.bal:23`), `# A server listener for handling MCP service requests.` (`listener.bal:114`), `# Represents an MCP session storage object used to maintain session state across requests.` (`session.bal:24`) — are absent. This originates in the extractor, not the renderer: the `Session` `description` field is already `"Creates a new MCP session with the given session ID.\n"` in `old/ballerina_mcp.json`, so `old` had the same defect latent; it only becomes visible now that the classes render.
- **N5 — `Listener`'s deprecation rationale is lost.** `new` emits a bare `@deprecated`, but not the source's `# Deprecated / This listener is renamed to make the transport explicit. Use ``mcp:StreamableHttpListener`` instead.` (`listener.bal:116–117`). The migration target is only implicit (the service templates do use `StreamableHttpListener`).
- **N6 — `isolated` qualifier dropped.** All three added classes are `public isolated class` in source, and all their methods are `isolated`; `new` renders `class Listener {` / `function attach(...)`. Same for `AdvancedService`'s `remote isolated function`s. Affects whether an LLM can use them inside `isolated` contexts.
- **N7 — included-record parameter expanded *and* retained on the listener `init`s.** Source is `public function init(int|http:Listener listenTo, *ListenerConfiguration config) returns Error?` (`listener.bal:29`). `new` renders the 13 fields of `http:ListenerConfiguration` as defaulted parameters *and* then a trailing required `ListenerConfiguration config`, which is not compilable Ballerina (required positional after defaulted, plus a duplicated concept). The expanded defaults are also type-zeros rather than the real ones (`decimal timeout = 0.0d`, `decimal gracefulStopTimeout = 0.0d`). This is the renderer's existing convention — the identical shape is already in `old` on `StreamableHttpClient.init` (`old` line 1027) — so it is not new behaviour, only newly applied to two more constructors.
- **N8 — the `mcp:Meta` handler slot is missing from every service template.** The compiler plugin explicitly supports an optional trailing `mcp:Meta?` tool parameter (`DiagnosticMessage.ERROR_105`: *"Meta parameter ''{1}'' in function ''{0}'' must be the last parameter."*, `ERROR_106`: *"must be optional (e.g., 'mcp:Meta?')"*, and `Utils.java:86` lists *"an optional 'mcp:Meta' parameter"* among the supported shapes). The `new` templates enumerate only `session`, `headers` and `request` as injectable slots; `'Meta' in json.dumps(new['services'])` → `False`. The `Meta` record itself is rendered (new line 439), so the gap is in the handler guidance only.

Inaccuracies present **identically in both** renders (listed for completeness; not attributable to spec v2, since these lines are outside every diff hunk):

- `const intersection SUPPORTED_PROTOCOL_VERSIONS = [2025-11-25, 2025-06-18, 2025-03-26, 2024-11-05, 2024-10-07];` (line 293 in both) — the string elements lost their quotes, so the literal reads as arithmetic; and the type is printed as `intersection` rather than `readonly & string[]`. Source: `types.bal:23–30`.
- `remote function initialize(Implementation clientInfo = {version: "", name: ""}, ...)` in both — the real default is `{name: "MCP Client", version: "1.0.0"}` (`streamable_http_client.bal:42`). An LLM relying on the render would advertise an empty client identity.
- Enum members are rendered without their string values and in reverse declaration order (`enum RequestMethod { REQUEST_CALL_TOOL, REQUEST_LIST_TOOLS, REQUEST_INITIALIZE }`, new line 883, vs `types.bal:34–41`). The values are recoverable from the flattened `const string REQUEST_CALL_TOOL = "tools/call";` lines, so this is redundancy rather than loss.
- `# + param - description` doc lines are dropped from every method in both renders; only the summary line survives, followed by an empty `# `.
- No `public` qualifier on rendered `type` / `class` / `enum` / `const` declarations in either render (annotations do carry it).

## 6. Coverage gaps vs. the library

**Coverage gaps in `new`: 0.**

`ballerina/mcp` publishes exactly one module (`bala/java21/modules/` contains only `mcp`; Central's `modules` array has the single entry `mcp`), which *is* the default module — so the known `getDefaultModule()`-only extraction limitation costs this library nothing, and there is no submodule-only API to report.

Enumerating the 102 public symbol names declared in `bala/java21/modules/mcp/*.bal` (all `public type` / `class` / `client class` / `enum` / `const` / `annotation` declarations) and requiring a matching top-level declaration line in each render:

- absent from `new`: **0**
- absent from `old`: **30** — the 28 `// Unknown type:` names plus the `Tool` and `StreamableHttpServiceConfig` annotations.

The only non-rendered public API surface in `new` is sub-declaration detail, all covered in §5 (the `mcp:Meta` handler slot, error parentage, `isolated`, `typedesc`).

## 7. Compiler plugin

`bala/java21/compiler-plugin/compiler-plugin.json` → `plugin_class: io.ballerina.stdlib.mcp.plugin.McpCompilerPlugin`, deps `mcp-compiler-plugin-1.2.0.jar` + `ballerina-to-openapi-2.3.0.jar`. `McpCompilerPlugin.java:27` registers exactly one thing: `compilerPluginContext.addCodeModifier(new McpCodeModifier())` — so the plugin is a **code modifier**, not just an analyser.

What it contributes:

- **Generated artifact:** `McpSourceModifier` + `SchemaUtils` synthesise a JSON schema for each tool `remote` function from its parameter list and inject/merge it into an `@mcp:Tool` annotation on the method (`createOrUpdateMetadata`, `modifyWithToolAnnotation`). This is exactly the behaviour `new`'s templates describe ("The method name becomes the tool name and its parameters become the tool's input schema, both discovered automatically, with no explicit registration") and that `old` said nothing about.
- **Parameter-shape validations** (`RemoteFunctionAnalysisTask`, `Utils.java:86`): tool parameters must be `anydata`; a `mcp:Session` parameter must be **first** (`ERROR_103`); a `mcp:Meta` parameter must be **last** and **optional** (`ERROR_105`, `ERROR_106`); `@http:Header` params must be `string|int|boolean|decimal|float` (`ERROR_108`); no duplicate injected params (`ERROR_107`); a `mcp:Session` parameter is rejected when `sessionMode` is `STATELESS` (`ERROR_104`); transport-specific parameters are rejected on the transport-agnostic `mcp:Service` (`ERROR_109`).
- **Service-shape validations** (`AdvancedServiceAnalysisTask`): `mcp:StreamableHttpAdvancedService` **must** define `onListTools` and `onCallTool` (`ERROR_110`), each with exactly one of the allowed parameter forms (`ERROR_111`), the mandated return type (`ERROR_112`), and no other remote methods (`ERROR_113`).

Alignment with the render: `new` surfaces the tool-schema mechanism, the `@mcp:Tool` / `@mcp:ServiceConfig` / `@mcp:StreamableHttpServiceConfig` annotation slots, the `session`-first ordering, the `@http:Header` type restriction, and marks `onListTools`/`onCallTool` `// required` on `StreamableHttpAdvancedService` — i.e. it reproduces `ERROR_110`/`ERROR_112`/`ERROR_108`/`ERROR_103` as guidance. Not surfaced: the `mcp:Meta?` slot (§5 N8), the `STATELESS`-forbids-`Session` rule (`ERROR_104`), and the "no other remote methods on `StreamableHttpAdvancedService`" rule (`ERROR_113`). `old` surfaced none of it.

## 8. Other considerations

- **Deprecations.** The package is not deprecated (Central: `deprecated: null`, `deprecateMessage: ""`). Two intra-library deprecations exist: the `Listener` class (`listener.bal:120`) and two fields of `ServiceConfiguration` — `httpConfig` and `sessionMode`, both `@deprecated` at `types.bal:612` / `types.bal:623` in favour of the `@mcp:StreamableHttpServiceConfig` equivalents. `new` marks the class with `@deprecated` but renders **no** field-level deprecation marker on `ServiceConfiguration` (neither does `old`), and its `mcp:Service` template still points at `@mcp:ServiceConfig` — correct for that service type, but a consumer is not told the two HTTP-ish fields inside it are deprecated. This is the main remaining doc-quality gap for the library, and it is shared by both sides.
- **Version.** `1.2.0` is a stable release; `SUPPORTED_PROTOCOL_VERSIONS` covers MCP `2024-10-07` … `2025-11-25`, `LATEST_PROTOCOL_VERSION = "2025-11-25"`.
- **Size / tokens.** +200 lines (+18.9%), 39,247 → 51,548 bytes (+31.3%). The Service section alone grew from 3 lines to 78. For 200 extra lines the render gains 30 top-level declarations, 17 methods and complete service-authoring guidance — a good ratio. `// Special Agent Note:` cross-package hints: 23 → 28.
- **Non-compiling render text.** Neither render is compilable Ballerina as-is (method stubs without bodies, the `intersection` const literal, the expanded-plus-retained included-record params, `= mcp:SessionEntry`). `new` adds two more instances of the included-record pattern (N7) and one new invalid default (N2) but also removes 22 invalid `org/mod:version:Type` references, so net syntactic validity improves.
- **This is the one library affected by the `old`-side renderer patch.** The brief's note is confirmed: `old/ballerina_mcp.json` `services[0]` has keys `['listener','name','type']` only — no `methods` key — which is precisely what the `service.methods ?? []` patch guards. So `old`'s empty service block is the *patched* best case, not a crash.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_mcp.bal.txt new/ballerina_mcp.bal.txt` | 1058 / 1258 |
| `wc -c` on the same two files | 39,247 / 51,548 |
| `grep -c '^// Unknown type:'` old / new | 28 / 0 |
| `grep -o 'ballerina/mcp:1\.2\.0:' \| wc -l` old / new | 22 / 0 (on 8 lines in `old`) |
| `grep -n '^// --- '` old / new | 6 markers each, same names, same order |
| `diff <(sed -n '1,288p' old) <(sed -n '1,288p' new)` | identical (README block) |
| `diff <(sed -n '8,286p' new) bala/java21/docs/README.md` | only a trailing blank line differs |
| `diff -u old new \| wc -l` | 385 lines, 10 hunks (agrees with `OLD_AND_NEW_DIFFS/mcp_diff.md`: +239/−39) |
| declaration extraction, kind counts | old 82 (1 ann, 4 class, 1 client, 20 const, 4 enum, 52 type); new 112 (3, 7, 1, 20, 4, 77) |
| `comm -23 <(sort decl_old) <(sort decl_new)` | empty → 0 declarations removed |
| `comm -13 …` | 30 added top-level declarations (listed §2) |
| `grep -cE '^\s+(isolated )?(remote )?function '` old / new | 9 / 38 |
| `ls bala/1.2.0/java21/modules` | `mcp` only → single (default) module, no submodule gap |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/mcp/1.2.0` | version 1.2.0, `deprecated: null`, `ballerinaVersion 2201.12.0`, modules `[mcp]`, pullCount 1205 |
| `git ls-remote --tags` → `v1.2.0` | `7533ffbeea42219fe1f32dfee4033b5483e2896b`; cloned `--depth 1 --branch v1.2.0` |
| `diff src/ballerina/{types,error,listener,session,streamable_http_client}.bal` vs bala | **SAME** for all 5 |
| `grep -n version src/gradle.properties` | `version=1.2.0` |
| `grep -n '^public \(isolated \)\?function' bala/modules/mcp/*.bal` | no output → JSON `functions: []` is correct |
| JSON array sizes | typeDefs 108/108, services 1/4, clients 1/1, annotations 1/3, functions 0/0 |
| `typeDefs` name-set difference both directions | empty |
| `typeDefs` per-entry diff | 73 identical, 35 differing; 28 removed lines, **0** unexplained |
| `clients` JSON diff | 4 lines, all de-qualification |
| `old['services'][0].keys()` | `['listener','name','type']` — no `methods` key (confirms the `?? []` patch note) |
| `old['services'][0].listener.parameters[0].default` | `"0"` — invented default for `listenTo`, gone in `new` |
| `old['annotations']` | single `ServiceConfig`, `description: "Define mcp service configuration"`, `displayName: "Service Configuration"` |
| `new['annotations']` names | `Tool`, `ServiceConfig`, `StreamableHttpServiceConfig`; `displayName` no longer present on `ServiceConfig`; description now matches `types.bal:626` |
| `new['services']` names | `Service`, `AdvancedService`, `StreamableHttpService`, `StreamableHttpAdvancedService`; all `identifier: {presence: optional, form: [basePath]}` |
| `'Meta' in json.dumps(new['services'])` | `False` → N8 |
| baseType audit: 24 `public type X distinct …` in `error.bal` vs `new` `typeDefs[X].baseType` | **20 mismatches**, all *(parent)* → `error`; 4 correct (all intersections) |
| 102 public default-module symbols vs render declarations | 0 absent from `new`; 30 absent from `old` |
| `bala/java21/compiler-plugin/compiler-plugin.json` | `McpCompilerPlugin`, + `ballerina-to-openapi-2.3.0.jar` |
| `McpCompilerPlugin.java:27` | `addCodeModifier(new McpCodeModifier())` — only registration |
| `diagnostics/DiagnosticMessage.java:25–44` | ERROR_101…ERROR_113 (quoted in §7) |
| `Utils.java:71,86` | `META_TYPE_NAME = "Meta"`; supported-shape string lists `optional 'mcp:Meta' parameter` |
| `SchemaUtils.java:68–71` | Session / Meta / `http:Headers` / `http:Request` / `@http:Header` params excluded from the generated tool schema |
| source spot-checks cited in §3 | `error.bal:18–91`; `types.bal:63,589,627,645,649–653,656,663,673–674,23–30,34–41,612,623`; `listener.bal:23,24,29,45,50,62,83,96,108,114,116–121`; `session.bal:24,25,32,39,47,65,80,90,103–106,114,126,135,143`; `streamable_http_client.bal:17,33,42` |

## 10. Caveats and unverified items

- Neither render was compiled or otherwise executed; syntactic-validity statements (§5, §8) are from reading the text against the Ballerina grammar, not from `bal build`.
- The `old`-side renderer patch (`service.methods ?? []`) was not read in the `ballerina-vscode` sources — neither side's extractor/renderer source was available in this working set. Its effect is inferred from the JSON evidence (`old['services'][0]` genuinely has no `methods` key) and is consistent with the brief; the patch text itself is **unverified**.
- Real default values for the expanded `http:ListenerConfiguration` / client-config fields (N7: `timeout`, `gracefulStopTimeout`, etc.) were not read out of the `ballerina/http` bala; the claim made is only that the rendered values are type-zeros, which is visible in the render itself. The specific assertion that `http:ListenerConfiguration.timeout` defaults to something other than `0` is **unverified**.
- Doc-comment fidelity was spot-checked (all 24 error types, the 3 new classes' member summaries, the 4 service-type docs, the 3 annotations) rather than compared line-by-line for all 108 `typeDefs`. The `typeDefs`-level check that **no** JSON line was lost (0 unexplained removals) covers the rest mechanically.
- `# Deprecated` field-level markers on `ServiceConfiguration.httpConfig` / `.sessionMode` were confirmed absent from both rendered `.bal.txt` files; whether the extractor records them anywhere in the JSON was not checked.

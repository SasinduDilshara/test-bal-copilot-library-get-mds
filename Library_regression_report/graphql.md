# ballerina/graphql 1.17.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/graphql` |
| Pinned version | `1.17.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-graphql |
| Tag reviewed | `v1.17.0` (exact tag, commit `dab2428090f1f7e30e6440454bb4dac079797da1`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/graphql/1.17.0/java21` |
| Old render | `1578` lines |
| New render | `1722` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive for this library. Zero declarations were removed, lines 1–891 (header +
full README) are byte-identical, and all 13 `// Unknown type:` placeholders in `old` are replaced by
real definitions that match the published bala. All 27 version-qualified type references
(`ballerina/graphql:1.17.0:Interceptor`, `ballerina/http:2.16.6:Protocol`, …) are now plain
module-qualified refs. `new` additionally recovers two annotations (`InterceptorConfig`, `ID`) that
`old` omitted entirely, corrects the `ResourceConfig` attach point from `service_function` to the
source-accurate `object function`, adds the `Interceptor.execute` remote method, and replaces `old`'s
empty `// --- Service (generic) ---` stub (4 comment lines, "Instructions:" with nothing after it)
with a 36-line service template describing all three GraphQL handler shapes.

Default-module coverage in `new` is complete: all 76 public symbols of the `graphql` default module
have a real definition. `old` had 14 with no definition.

`new` does introduce inaccuracies of its own inside the newly added declarations (wrong defaults on
the expanded `Listener.init`, flattened error-type hierarchy, unqualified `Cloneable[]`), but none of
these existed correctly in `old` — `old` had nothing there at all — so none are regressions.

## 2. Change inventory

Line counts (`wc -l`): old 1578, new 1722 (+144). Diff: +177 / −33 over 11 hunks.

Section markers (`grep -n '^// --- '`):

| marker | old | new |
|---|---|---|
| README / END README | 7 / 842 | 7 / 842 |
| Types | 844 | 844 |
| Client | 1534 | 1643 |
| Functions | 1552 | 1661 |
| Service | 1565 | 1674 |
| Service (generic) | 1567 | *removed* |
| Annotations | 1572 | 1710 |

Degraded types (`grep -c '^// Unknown type:'`): old **13**, new **0**.

Top-level declaration set (extracted with
`grep -nE '^(public )?(client )?(isolated )?(type|class|enum|const|annotation|service|listener|function|remote function) '`,
signature-stripped and sorted): old 113, new 129, **0 removed**.

Added in `new` (16 top-level):

| kind | added |
|---|---|
| class (3) | `Context`, `Field`, `Listener` |
| error type (9) | `Error`, `AuthnError`, `AuthzError`, `ClientError`, `RequestError`, `HttpError`, `InvalidDocumentError`, `ServerError`, `PayloadBindingError` |
| function type (1) | `ContextInit` |
| annotation (2) | `InterceptorConfig`, `ID` |
| service template (1) | `service graphql:Service /basePath on new graphql:Listener(...)` |

Added members inside existing declarations: `Interceptor.execute` (new:1152); 9 methods on `Context`
(`init`,`set`,`get`,`remove`,`registerDataLoader`,`getDataLoader`,`invalidate`,`invalidateAll`,`resolve`);
8 on `Field` (`init`,`getName`,`getAlias`,`getPath`,`getSubfields`,`getSubfieldNames`,`getType`,`getLocation`);
6 on `Listener` (`init`,`attach`,`detach`,`'start`,`gracefulStop`,`immediateStop`).

Modified (not added/removed):
- 27 version-qualified refs de-qualified (`ListenerAuthConfig`, `ClientAuthConfig`, `OAuth2GrantConfig`,
  `GraphqlServiceConfig.interceptors`, `GraphqlResourceConfig.interceptors`, `ListenerSecureSocket`
  ×3, `ClientSecureSocket` ×2, `Upload.byteStream`, `Client.init` return type).
- `ResourceConfig` attach point `on service_function` → `on object function`.
- Annotation doc strings replaced by the bala's own doc strings (see §3).

JSON side (`old/new *.json`): `typeDefs` 81 → 81 (identical count; `old` already carried
`kind: Error/Other` entries the `old` renderer could not emit), `clients` 1 → 1, `functions` 2 → 2,
`services` 1 → 1, `annotations` 2 → 6 (`ServiceConfig`, `ResourceConfig`, `InterceptorConfig`, and
`ID` three times — once per attach point; the renderer correctly collapses these to one line).
The `services[0]` object changed keys from `{type,name,instructions,listener}` to
`{type,name,listener,annotations,identifier,handlerTemplates}`.

Note: the precomputed diff at `OLD_AND_NEW_DIFFS/graphql_diff.md` lists "36 declarations added",
which counts class/object members as top-level declarations and includes a spurious entry
`annotation on` (a mis-parse of `public annotation ID on parameter, ...`). Its "0 declarations
removed" and its unified diff are correct and were verified line-by-line against the two files.

## 3. Correctness against library source

Checked against the bala (authoritative) at
`.../bala/ballerina/graphql/1.17.0/java21/modules/graphql/` and cross-read against the `v1.17.0`
clone. Bala and GitHub agree for every file inspected.

| render (new) | source | verdict |
|---|---|---|
| `class Context` + 9 methods (1014–1061) | `context.bal:24,29,41,52,67,83,93,101,112,147` — same 9 public members, same order | correct |
| `Context.get/remove … \|Error` | `context.bal:52,67` return `value:Cloneable\|isolated object {}\|Error` | correct (see §5.3 for the qualification defect) |
| `registerDataLoader(string key, dataloader:DataLoader)` | `context.bal:83` | correct |
| `class Field` + `getName/getAlias/getPath/getSubfields/getSubfieldNames/getType/getLocation` | `field.bal:73,84,91,97,107,113,119` — all 7 public methods present, `readonly & (string\|int)[]` ≡ rendered `(string\|int)[] & readonly`, `Field[]?` ≡ `Field[]\|()` | correct |
| `class Listener` + `attach/detach/'start/gracefulStop/immediateStop` | `listener.bal:59,103,125,152,172` — all `returns Error?` ≡ rendered `Error\|()`; the 3 private methods (`initHttpListener`, `initWebsocketListener`, `initGraphiqlService`) are correctly excluded | correct |
| `Interceptor.execute(Context, Field 'field) returns anydata\|error` (1152) | `types.bal:100` verbatim | correct |
| `type ContextInit function (http:RequestContext, http:Request) returns Context\|error` (1179) | `types.bal:37` | correct modulo dropped `isolated` |
| 9 error types (1328–1353) | `errors.bal:18,21,24,29,32,35,38,44,47` — names, doc strings and payload records match; `@deprecated` on `ServerError` preserved (`errors.bal:43`) | correct modulo dropped `distinct`/intersections (§5.2) |
| `public annotation GraphqlServiceConfig ServiceConfig on service;` (1713) | `annotations.bal:48-49` incl. doc string | correct |
| `public annotation GraphqlResourceConfig ResourceConfig on object function;` (1716) | `annotations.bal:63-64` | correct — `old`'s `on service_function` was wrong |
| `public annotation GraphqlInterceptorConfig InterceptorConfig on class;` (1719) | `annotations.bal:72-73` | correct, absent from `old` |
| `public annotation ID on parameter, return, record field;` (1722) | `types.bal:21-22` (`on record field, parameter, return`) | correct; attach-point order differs, semantically identical |
| service template: `get` resource → query, `remote` → mutation, `subscribe` resource → stream subscription | matches `compiler-plugin/.../ServiceValidator.java` handler rules and `types.bal:28` `Service distinct service object {}` | correct |
| de-qualified refs (`http:VerifyClient`, `crypto:TrustStore`, `io:Error`, `Interceptor`, …) | resolve to the same types the qualified `old` forms named | correct |

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff` of the two declaration sets shows **0 removals** (`diff old.decls new.decls` → only `>` lines
  plus 4 `<`/`>` pairs, all of which are de-qualifications or the `ResourceConfig` attach-point fix).
- `diff` of lines 1–891 → identical, so no README, module description, enum, constant or record was
  touched.
- `grep -c '^// Unknown type:'` → 13 in `old`, 0 in `new`; nothing moved the other way.
- Every one of the 76 public default-module symbols has a definition in `new` (§6); 14 did not in `old`.
- The two annotation doc strings that changed text (`ServiceConfig`, `ResourceConfig`) changed *toward*
  the bala's own doc comments (`annotations.bal:48,63`), so this is an accuracy gain, not a loss.
  `old`'s wording ("Define service configurations such as maximum query depth." / "Define
  configurations such as field level cache.") is not present anywhere in the bala.
- The `// --- Service (generic) ---` marker disappearing is not lost content: `old`'s block under it
  was 4 comment lines ending in a bare `// Instructions:` with no body; `new` replaces it with a
  36-line concrete template.
- Shared defects that exist in **both** files (therefore not regressions): the unwrapped doc line
  `a compilation error.` at old:893 / new:893 (breaks out of the `#` doc comment), the bogus
  `targetType = graphql:GenericResponse|record {|anydata...;|}|json` default in `Client` remote
  methods (old:1544,1549 / new:1653,1658), `Client.init` ending with a required `ClientConfiguration
  clientConfig` after defaultable parameters, and closed records (`record {| *http:… |}`) rendered as
  open `record { … }`.

## 5. Issues in `new` (independent of `old`)

All six live inside declarations `new` added, so `old` had no correct version of them.

1. **`Listener.init` defaults are zero-value fillers, and the signature does not compile** (new:1620).
   Source is `init(int|http:Listener listenTo, *ListenerConfiguration configuration) returns Error?`
   (`listener.bal:42`); `ListenerConfiguration` is `record {| *http:ListenerConfiguration; |}`
   (`records.bal:21`). The render expands the included record and invents defaults:

   | field | render | actual (`http_service_endpoint.bal:156-168`, `http_constants.bal:36,40`) |
   |---|---|---|
   | `host` | `""` | `"0.0.0.0"` |
   | `timeout` | `0.0d` | `60` (`DEFAULT_LISTENER_TIMEOUT`) |
   | `http2InitialWindowSize` | `0` | `65535` |
   | `minIdleTimeInStaleState` | `0.0d` | `300` |
   | `timeBetweenStaleEviction` | `0.0d` | `30` |
   | `httpVersion` | `"2.0"` | `HTTP_2_0` — correct |
   | `gracefulStopTimeout` | `0.0d` | `0` — correct |

   `timeout = 0` in particular means "disable timeout" in `http`, the opposite of the real default.
   The signature also ends with a required `ListenerConfiguration configuration` after 12 defaultable
   parameters, which is not valid Ballerina. (`Client.init` has the same trailing-required-param
   shape in both files, so that part is shared, not new.)

2. **Error hierarchy flattened.** `distinct` is dropped and intersections are lost:
   `type AuthnError error;` (new:1331) vs source `public type AuthnError distinct Error;`
   (`errors.bal:21`); likewise `AuthzError`. `RequestError` is `distinct ClientError` but renders as
   bare `error` (new:1340). `HttpError` / `InvalidDocumentError` are
   `distinct (RequestError & error<record {|…|}>)` (`errors.bal:35,38`) but render without the
   `RequestError &` half (new:1343,1346); `ServerError` / `PayloadBindingError` lose `ClientError &`
   (new:1350,1353). An LLM reading `new` cannot tell that `AuthnError` is a `graphql:Error` or that
   `HttpError` is catchable as `ClientError`.

3. **Inconsistent / unresolvable type qualification in `Context`.** `set` (new:1018) writes
   `value:Cloneable[]` but `get` (new:1025) and `remove` (new:1032) write bare `Cloneable[]` — there
   is no `Cloneable` in the `graphql` module, so that reference does not resolve. The same two lines
   render the xml member as `xml<>` while `set` renders it fully as
   `xml<xml:Element|xml:Comment|xml:ProcessingInstruction|xml:Text>`.

4. **`Field.init` is exposed although it is module-private.** `field.bal:38` declares
   `isolated function init(...)` with no `public`; `new:1591` emits it, leaking internal
   `parser:FieldNode` / `parser:RootOperationType` types and suggesting user code can construct a
   `graphql:Field`. (`Context.init` and `Listener.init` are genuinely public, so they are fine.)

5. **`isolated` dropped from `ContextInit`** (new:1179) — source is
   `public type ContextInit isolated function (…)` (`types.bal:37`). A user-supplied non-isolated
   function will not satisfy the real type.

6. **Service template placeholders are not copy-pasteable Ballerina** (new:1677): the listener
   arguments are a *type* signature, `new graphql:Listener(int|http:Listener listenTo,
   graphql:ListenerConfiguration configuration = {})`, rather than argument values, and
   `@graphql:ServiceConfig {...} // optional` is a literal `{...}`. Both are explained by the
   surrounding comments, so this is low severity, but the block is presented as a service definition
   rather than as a comment.

Encoding: 3 non-ASCII lines in `new` (em-dashes in the service template), 0 in `old`; all render as
valid UTF-8, no mojibake.

## 6. Coverage gaps vs. the library

**Default module `graphql`: 0 gaps in `new`.** Extracted 76 public top-level symbols from
`modules/graphql/*.bal` and checked each for a definition line in each render:

- missing a definition in `old`: 14 — `Error`, `AuthnError`, `AuthzError`, `ClientError`,
  `RequestError`, `HttpError`, `InvalidDocumentError`, `ServerError`, `PayloadBindingError`,
  `Context`, `ContextInit`, `Field`, `Listener`, `ID`.
- missing a definition in `new`: **0**.

**Submodule-only API — shared gap, present in both renders** (extraction is `getDefaultModule()`
only). Ballerina Central lists 3 public modules for this package
(`https://api.central.ballerina.io/2.0/registry/packages/ballerina/graphql/1.17.0`); the bala ships 4:

| module | public symbols | in render? |
|---|---|---|
| `graphql.dataloader` | 3 — `DataLoader`, `DefaultDataLoader`, `BatchLoadFunction` | referenced by `Context.registerDataLoader`/`getDataLoader` in `new` via a `// Special Agent Note`, but never defined |
| `graphql.subgraph` | 5 — `Subgraph`, `FederatedEntity`, `ReferenceResolver`, `Representation`, `ANY` | absent from both |
| `graphql.parser` | 54 (`FieldNode`, `RootOperationType`, `Location`, …) | absent from both; referenced by `Field.init` in `new` |

The `graphql.subgraph` gap is the user-facing one: Apollo-Federation services need
`@subgraph:Subgraph` and `@subgraph:Entity`, and neither render mentions them. `graphql.dataloader`
is directly reachable from the rendered `Context` API in `new`, so the dangling `dataloader:DataLoader`
reference is more visible there than in `old` — but the underlying gap is identical on both sides.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.graphql.compiler.GraphqlCompilerPlugin`
(2 jars: `graphql-compiler-plugin-1.17.0.jar`, `graphql-commons-1.17.0.jar`). 35 Java sources.
`GraphqlCompilerPlugin.java:30-33` registers exactly two units:

- **`GraphqlCodeModifier`** (with `GraphqlSourceModifier`, `SchemaGenerator`, `IntrospectionTypeCreator`,
  `InterfaceEntityFinder`, `EntityAnnotationFinder`, `ResourceConfigAnnotationFinder`,
  `CacheConfigContext`) — generates the GraphQL schema at compile time and injects it into
  `GraphqlServiceConfig.schemaString`, and derives `fieldCacheConfig` from resource annotations.
  Both renders carry the doc text for these fields (new:891-893, 902) including "Providing a value
  for this field will end up in a compilation error", so the plugin's contract is visible — although
  the sentence is split across an unprefixed line in both files (§4).
- **`GraphqlCodeAnalyzer`** with `ServiceDeclarationAnalysisTask`, `ServiceAnalysisTask`,
  `ObjectConstructorAnalysisTask`, `ModuleLevelVariableDeclarationAnalysisTask`,
  `AnnotationAnalysisTask`, `InterceptorAnalysisTask` and validators `ServiceValidator`,
  `InterceptorValidator`, `ListenerValidator` — enforces the handler shapes (`get` resources = query
  fields, `remote` methods = mutations, `subscribe` resources = subscriptions returning a stream),
  return-type restrictions, and interceptor/listener well-formedness.

Alignment with the render: `new`'s service template encodes the three handler shapes the
`ServiceValidator` enforces, plus the `@graphql:ResourceConfig` / `@graphql:ID` attachment rules —
this is precisely the plugin-implied knowledge that `old` left as an empty "Instructions:" stub.
Still absent from `new`: the federation path (`EntityAnnotationFinder` looks for
`@subgraph:Entity`, whose annotation lives in the `graphql.subgraph` submodule — see §6), and the
`@graphql:ID` slot is described only in prose inside the template comments.

## 8. Other considerations

- Central metadata: `ballerinaVersion 2201.13.0`, `deprecateMessage: ""` — package is **not**
  deprecated. Version 1.17.0 is post-1.0 and stable.
- One deprecated symbol in the API: `ServerError` (`errors.bal:43`) and, correspondingly,
  `Client.executeWithType`. `new` preserves both `@deprecated` markers; `old` preserved only the one
  on `executeWithType` (its `ServerError` was an `// Unknown type:` line), so `new` is more accurate
  about what not to use.
- Size: +144 lines (+9.1%). Token cost is modest and buys 16 previously invisible top-level
  declarations plus the service template — a good ratio.
- `// Special Agent Note:` cross-package annotations: 31 in `old`, 35 in `new` (4 added, on the new
  `Context`/`Field`/`Listener` members).
- Both renders emit the closed records `ListenerConfiguration`, `ListenerHttp1Settings`,
  `ListenerSecureSocket`, `RequestLimitConfigs`, `ClientHttp1Settings`, etc. as open
  `record { … }` with all fields optional, although the source declares them `record {| *http:X; |}`
  with non-optional defaulted fields (`records.bal:21-70`). Unchanged between the two sides.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l` on both renders | old 1578, new 1722 |
| 2 | `git ls-remote --tags …module-ballerina-graphql \| grep v1.17` | `refs/tags/v1.17.0` → `dab2428…` |
| 3 | `git clone --depth 1 --branch v1.17.0 … src` | succeeded; exact tag, no fallback |
| 4 | `grep -c '^// Unknown type:'` | old 13, new 0 |
| 5 | `grep -n '^// --- '` | old 8 markers, new 7 (table in §2) |
| 6 | `diff <(sed -n '1,891p' old) <(sed -n '1,891p' new)` | identical |
| 7 | declaration-set `diff old.decls new.decls` | 0 removals, 16 additions, 4 modified lines |
| 8 | `ls bala/.../modules` | `graphql`, `graphql.dataloader`, `graphql.parser`, `graphql.subgraph` |
| 9 | 76 public default-module symbols vs. definition lines in each render | 14 undefined in old, 0 in new |
| 10 | `grep -rhoE '^public …' modules/graphql.{dataloader,parser,subgraph}/*.bal` | 3 / 54 / 5 public symbols, none defined in either render |
| 11 | `context.bal:24,29,41,52,67,83,93,101,112,147` | 9 public members ↔ 9 rendered in new:1014-1061 |
| 12 | `field.bal:38,73,84,91,97,107,113,119` | init module-private; 7 public methods ↔ new:1590-1616 |
| 13 | `listener.bal:23,42,59,103,125,152,172,189,215,260` | 5 public methods + init rendered; 3 private methods excluded |
| 14 | `errors.bal:17-47` | 9 public error types, `@deprecated` on `ServerError`; all `distinct`/intersections dropped in new:1328-1353 |
| 15 | `types.bal:21-22,28-29,37,99-101` | `ID` annotation, `Service`, `ContextInit`, `Interceptor.execute` — all match new except dropped `isolated` |
| 16 | `annotations.bal:48-49,63-64,72-73` | 3 annotation decls + doc strings ↔ new:1713,1716,1719; `old` had 2, one with wrong attach point |
| 17 | `records.bal:21-70` | `ListenerConfiguration` etc. are `record {| *http:X; |}` (closed) |
| 18 | `http/2.16.6/.../http_service_endpoint.bal:156-168` + `http_constants.bal:36,40` | real listener-config defaults; 5 of 12 mis-rendered in new:1620 |
| 19 | `curl api.central.ballerina.io/…/ballerina/graphql/1.17.0` | not deprecated; 3 public modules listed |
| 20 | `cat bala/.../compiler-plugin/compiler-plugin.json` + `GraphqlCompilerPlugin.java:30-33` | code modifier + code analyzer; 35 plugin sources enumerated |
| 21 | `python3` on both JSONs | typeDefs 81/81, annotations 2→6, services[0] keys changed |
| 22 | `grep -c 'Special Agent Note'` | old 31, new 35 |
| 23 | `LC_ALL=C grep -n '[^\x00-\x7F]'` | old 0 lines, new 3 (em-dashes, valid UTF-8) |
| 24 | `grep -n '^a compilation error\.$'` | 1 occurrence in each file — shared defect |
| 25 | `grep -n 'targetType = graphql:'` | present in both (old:1544,1549 / new:1653,1658) — shared defect |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that a rendered signature "does not compile" (§5.1, §5.6)
  are read from the Ballerina grammar (required parameter after defaultable parameters; a type
  signature in an argument position), not from a `bal build` run.
- Whether `Field.init` being emitted (§5.4) is intended behaviour of the new extractor or an
  oversight was not determined — the extractor source (`ballerina-vscode`
  `L1_json_and_annotations_with_spec_v2`) was not read; only its output was audited.
- The public-symbol extraction in §6 is regex-based over `modules/**/*.bal` (`^public … <Name>`).
  It will not catch a public symbol declared with an unusual qualifier ordering. Spot checks against
  the bala `docs/` listing were not run, so the count 76 is a lower bound, though every symbol found
  is accounted for in both directions.
- The `graphql.parser` module is public in the bala but is not listed as a public module by Ballerina
  Central; whether its absence from the render is intended was not determined and it is reported
  separately from the two Central-listed submodules.
- The compiler-plugin review is a reading of class names, the plugin entry point and validator file
  names; individual diagnostic codes in `DiagnosticMessage.java` / `CompilationDiagnostic.java` were
  not enumerated one by one.
- `old`'s annotation doc strings ("Define service configurations such as maximum query depth.") do
  not appear in the bala; their origin (a hand-curated table in the old extractor) was not traced.

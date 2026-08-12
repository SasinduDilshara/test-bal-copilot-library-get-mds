# ballerina/grpc 1.14.7 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/grpc` |
| Pinned version | `1.14.7` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-grpc |
| Tag reviewed | `v1.14.7` (commit `89f217a4ee574fbcc63d9c69b7186dde798bb270`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/grpc/1.14.7/java21` |
| Old render | `1239` lines |
| New render | `1406` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present in `old` was dropped: the
top-level declaration set of `new` is a proper superset of `old`'s (0 declarations removed, 33
added). The 29 `// Unknown type:` placeholders in `old` are all resolved into real definitions
(6 classes incl. `Listener`, 23 error/type aliases), all 25 version-qualified type references
(`ballerina/grpc:1.14.7:Type`, `ballerina/grpc:grpc:Type`) are gone, two fabricated constructors
(`Caller.init`, `StreamingClient.init` — neither exists in the source) are removed, and five
methods that `old` wrongly marked `remote` are now correctly plain functions. `new` additionally
gains a `// --- Service ---` template and a `// --- Annotations ---` section with all three
service annotations. README and the `// --- Functions ---` section are byte-identical between the
two renders. Default-module public-API coverage goes from 68/100 symbols in `old` to 100/100 in
`new`.

Residual inaccuracies in `new` are real but minor and none of them is a regression: the `distinct`
error hierarchy is flattened to bare `error`, `Listener.init` inherits the renderer's
include-record flattening artifact that yields a non-compiling parameter order (the same artifact
`old` already had on `Client.init`), and the new service template names only `@grpc:Descriptor`
where the compiler plugin equally accepts `@grpc:ServiceDescriptor`.

## 2. Change inventory

Line counts (`wc -l`): old **1239**, new **1406** (+167). `diff -u` = 407 lines, 14 hunks.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 29 | 0 |
| Version/module-qualified type refs (occurrences) | 25 | 0 |
| `// --- section ---` markers | 5 | 7 |
| `remote function` lines | 28 | 23 |
| Malformed doc-continuation `eg: TLS_ECDHE…` lines | 2 | 2 |
| `Special Agent Note` cross-package hints | 24 | 28 |

### Top-level declarations

Extracted declaration sets (`comm` on sorted declaration headers): **0 removed**, **33 added**.

| Kind | Added in `new` | Names |
|---|---|---|
| class | 6 | `ClientBasicAuthHandler`, `ClientBearerTokenAuthHandler`, `ClientSelfSignedJwtAuthHandler`, `ListenerFileUserStoreBasicAuthHandler`, `ListenerJwtAuthHandler`, `Listener` |
| type (error / alias) | 23 | `Error`, `ErrorType`, `CancelledError`, `UnKnownError`, `InvalidArgumentError`, `DeadlineExceededError`, `NotFoundError`, `AlreadyExistsError`, `PermissionDeniedError`, `UnauthenticatedError`, `ResourceExhaustedError`, `FailedPreconditionError`, `AbortedError`, `OutOfRangeError`, `UnimplementedError`, `InternalError`, `UnavailableError`, `DataLossError`, `ResiliencyError`, `AllRetryAttemptsFailed`, `StreamClosedError`, `DataMismatchError`, `ClientAuthError` |
| annotation | 3 | `ServiceDescriptor`, `Descriptor`, `ServiceConfig` |
| service template | 1 | `service grpc:Service "identifier" on new grpc:Listener(...)` |

### Modified declarations

| Change | Count | Detail |
|---|---|---|
| Version-qualified refs unqualified | 12 lines | `ListenerAuthConfig`, `OAuth2GrantConfig`, `ClientAuthConfig`, 2 inline records in `ClientSecureSocket`, 3 inline records in `ListenerSecureSocket`, `Client.init` return, `Client.executeServerStreaming` return, plus the 2 fabricated `init` returns |
| `remote function` → `function` | 5 | `Caller.getId`, `Caller.isCancelled`, `Client.initStub`, `ServerReflectionServerReflectionResponseCaller.getId`, `…​.isCancelled` |
| Fabricated constructors removed | 2 | `Caller.init() returns ballerina/grpc:grpc:Caller`, `StreamingClient.init() returns ballerina/grpc:grpc:StreamingClient` |

### JSON layer

Both JSONs have identical `typeDefs` (91), `clients` (7), `functions` (7) name sets and an
identical 13 261-char `readme`. `new` adds `services` (0 → 1) and `annotations` (0 → 3). 34
`typeDefs` and 3 `clients` differ in content; the decisive change is that `new` emits a
`"type": "Class"` kind on class typeDefs where `old` emitted none — which is why the `main`
renderer degraded them to `// Unknown type:`.

## 3. Correctness against library source

All checks against the bala's `modules/grpc/*.bal` (authoritative; the v1.14.7 clone agrees).

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `class ClientBasicAuthHandler { init(CredentialsConfig config); enrich(map<string\|string[]>) returns map<string\|string[]>\|ClientAuthError }` | `auth_client_basic_auth_handler.bal:20,27,35` | exact |
| `class ClientBearerTokenAuthHandler { init(BearerTokenConfig); enrich(...) }` | `auth_client_bearer_token_auth_handler.bal:18,25,33` | exact |
| `class ClientSelfSignedJwtAuthHandler { init(JwtIssuerConfig); enrich(...) }` | `auth_client_self_signed_jwt_auth_handler.bal:20,27,35` | exact |
| `class ListenerFileUserStoreBasicAuthHandler { init(FileUserStoreConfig config = {}); authenticate(...) returns auth:UserDetails\|UnauthenticatedError; authorize(auth:UserDetails, string\|string[]) returns PermissionDeniedError\|() }` | `auth_listener_file_user_store_basic_auth_handler.bal:20,27,35,54` | exact (`PermissionDeniedError?` ≡ `PermissionDeniedError\|()`) |
| `class ListenerJwtAuthHandler { init(JwtValidatorConfig); authenticate(...) returns jwt:Payload\|UnauthenticatedError; authorize(jwt:Payload, …) }` | `auth_listener_jwt_auth_handler.bal:22,30,39,58` | exact |
| `class Listener` with `init`, `'start`, `gracefulStop`, `immediateStop`, `attach(Service, string[]\|string\|() = ())`, `detach(Service)` — all `returns error?` | `service_endpoint.bal:22,94,33,48,59,72,84` | all 6 public methods present, signatures match |
| `Listener.init` flattened params `host = "0.0.0.0"`, `secureSocket = ()`, `timeout = 120`, `maxInboundMessageSize = 4194304`, `maxHeaderSize = 8192`, `reflectionEnabled = false` | `ListenerConfiguration` at `service_endpoint.bal:306`; `DEFAULT_LISTENER_TIMEOUT = 120` at `service_endpoint.bal:295` | every field name and default correct |
| `function getId()` / `function isCancelled()` (not `remote`) on `Caller` | `caller.bal:32,65` — `public isolated function` | `new` correct, `old` wrong |
| `function initStub(...)` (not `remote`) on `Client` | `client_endpoint.bal:59` — `public isolated function` | `new` correct, `old` wrong |
| `getId` / `isCancelled` plain on `ServerReflectionServerReflectionResponseCaller` | `reflection_pb.bal` — `public isolated function` (lines 29, 45 of the class block) | `new` correct |
| Removal of `Caller.init` / `StreamingClient.init` | `caller.bal` and `streaming_client.bal` contain **no** `function init` | `new` correct — `old` invented them |
| `annotation ServiceDescriptorData ServiceDescriptor on service`, `annotation DescriptorData Descriptor on service`, `annotation GrpcServiceConfig ServiceConfig on service` | `annotation.bal:27,39,49` | all three exact, correct type constraints and attach points |
| Error aliases' doc strings | `grpc_errors.bal:18–90` | doc text matches verbatim, incl. the source's own typo "erros" on `DataLossError` |
| Service template: remote-only handlers, max 2 params, caller first, `error?` return when caller present | `GrpcServiceValidator.java` + `GrpcCompilerPluginConstants.java:40–51` (`RESOURCES_NOT_ALLOWED`, `MAX_PARAM_COUNT`, `TWO_PARAMS_WITHOUT_CALLER`, `RETURN_WITH_CALLER`) | consistent with the plugin's rules |

## 4. Regressions

**None found.**

What was checked to conclude this:
- Sorted top-level declaration sets diffed with `comm`: the only entries unique to `old` are the
  three union aliases `ClientAuthConfig`, `ListenerAuthConfig`, `OAuth2GrantConfig`, and they are
  unique only because `old` spelled their members `ballerina/grpc:1.14.7:X` and `new` spells them
  `X`. The declarations themselves survive.
- README block (lines 1–377) byte-identical: `diff` returns empty.
- `// --- Functions ---` section (old 1170–1239 vs new 1282–1351) byte-identical: `diff` returns
  empty; all 7 module-level functions (`setCompression`, `setDeadline`, `getDeadline`,
  `isCancelled`, `authenticateResource`, `getHeader`, `getHeaders`) intact.
- JSON `typeDefs` / `clients` / `functions` name sets identical (91 / 7 / 7); no member function
  disappeared from any client except the two fabricated `init`s.
- No parameter, default value, or return type was dropped in `new` anywhere in the 407-line diff —
  every removed line is either an `// Unknown type:` placeholder, a version-qualified spelling
  replaced by an unqualified one, an incorrect `remote` qualifier, or a fabricated constructor.
- `// Unknown type:` count 29 → 0; version-qualified refs 25 → 0.

## 5. Issues in `new` (independent of `old`)

1. **Error hierarchy flattened.** `grpc_errors.bal:18–90` defines `Error` as `distinct error` and
   21 subtypes as `distinct Error` (with `AllRetryAttemptsFailed` being `distinct ResiliencyError`).
   `new` renders every one as a bare `type X error;`, so the subtype relationships — including that
   all of them are assignable to `grpc:Error`, and that `AllRetryAttemptsFailed` is a
   `ResiliencyError` — are not conveyed. Still far better than `old`'s `// Unknown type:` lines.
2. **`Listener.init` parameter order is not valid Ballerina.** `new` line 1080:
   `function init(int port, string host = "0.0.0.0", …, boolean reflectionEnabled = false, ListenerConfiguration config) returns error?;`
   — a required parameter after defaultable ones. This is the renderer's include-record
   (`*ListenerConfiguration`) flattening artifact; `old` already exhibits it on `Client.init`
   (both renders), so it is a pre-existing renderer behaviour newly visible on `Listener`.
   Copied literally it will not compile; the real call is `new grpc:Listener(9090, host = "…")`.
3. **Service template names only `@grpc:Descriptor` as mandatory.**
   `GrpcServiceValidator.validateServiceAnnotation` (compiler-plugin, lines 155–180) accepts
   **either** `ServiceDescriptor` **or** `Descriptor`, and the repo's own example
   (`examples/async-streaming/server/phone_service.bal:24`) plus `protoc`-generated code use
   `@grpc:ServiceDescriptor {descriptor: …, descMap: …}`. `new` lists `ServiceDescriptor` in the
   Annotations section but omits it from the service template, which could steer an LLM to the
   less common form.
4. **Fabricated default in the service JSON.** `new/ballerina_grpc.json` → `services[0].listener.parameters[0]`
   gives `"name": "port"` a `"default": "0"`. `service_endpoint.bal:94` declares
   `init(int port, *ListenerConfiguration config)` — `port` has no default and is required. The
   rendered `.bal.txt` does not print this default, so the impact is confined to the JSON.
5. **Object qualifiers dropped** (`public isolated class` → `class`, `isolated remote function` →
   `remote function`). Shared with `old`; harmless for LLM consumption but worth noting.

### Issues shared by both renders (not attributable to `new`)

- Two doc-comment continuation lines lose their `#` prefix and land bare inside a record body:
  `eg: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA` inside
  `ClientSecureSocket` and `ListenerSecureSocket`. Non-compiling as written. Present 2× in both.
- Inline anonymous-record defaults are dropped in both: `versions = []` (protocol),
  `'type = OCSP_STAPLING` (certValidation), `verifyClient = REQUIRE` (mutualSsl) — cf.
  `service_endpoint.bal:326+`.
- `Client.init` shows the same required-after-defaultable ordering in both renders.

## 6. Coverage gaps vs. the library

**Default module (`modules/grpc`) — 100 public symbols parsed from the bala.**

- `new`: **0** missing. All 100 public `type`/`class`/`enum`/`const`/`function`/`annotation`
  declarations have a corresponding declaration in the render.
- `old`: **32** missing (23 error/alias types, 6 classes, 3 annotations) — the exact set `new`
  restores, minus `Descriptor`/`ServiceConfig`/`ServiceDescriptor` which `old` never had at all.

So the number of default-module public symbols absent from **both** renders is **0**.

**Submodule-only API — shared gap, both sides.** The package exports five non-default modules that
neither render touches (both pipelines use `pkg.getDefaultModule()` only):

| Module | Public symbols |
|---|---|
| `grpc.types.wrappers` | 5 (`IntStream`, `BytesStream`, `FloatStream`, `BooleanStream`, `StringStream`) |
| `grpc.types.any` | 1 |
| `grpc.types.duration` | 1 |
| `grpc.types.struct` | 1 |
| `grpc.types.timestamp` | 1 |

Total 9 symbols. These are used by `protoc`-generated stub code, so their absence is a modest but
real gap — identical on both sides, therefore not a regression.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.grpc.plugin.GrpcCompilerPlugin`,
jar `grpc-compiler-plugin-1.14.7.jar`. It is a **code analyzer only** — no code generation, no
code actions, no generated artifacts. Diagnostics (`GrpcCompilerPluginConstants.java:40–51`):

| Code | Rule | Surfaced in `new` render? |
|---|---|---|
| `GRPC_101` | service must carry `@grpc:ServiceDescriptor` **or** `@grpc:Descriptor` | partially — template marks `@grpc:Descriptor` required, omits the `ServiceDescriptor` alternative |
| `GRPC_102` | resource methods not allowed inside gRPC services | yes — template offers only `remote function` handlers |
| `GRPC_103` | only `error?` return allowed when a caller parameter is present | yes — stated explicitly in all four handler shapes |
| `GRPC_104` | max 2 parameters on a remote function | yes — every shape has at most `caller` + one payload/stream |
| `GRPC_105` | with two parameters the first must be the caller type | yes — "Must come first when present" |
| `GRPC_106` | caller must be the RPC-specific generated caller type | partially — template uses the generic `grpc:Caller`; the plugin expects the generated `<Rpc>Caller` (e.g. `PhoneStreamCallResponseCaller`) for streaming RPCs |
| `GRPC_107` | service name must not be hierarchical | yes — template forces a quoted string-literal identifier |

Nothing the plugin implies is materially absent from `new`; `old` surfaced none of it (no Service
section at all). The remaining looseness is `GRPC_106`: an LLM following the template literally
would write `grpc:Caller` where the generated per-RPC caller type is required for streaming RPCs.
The render also never states that the `descriptor`/`value` field must come from `bal grpc`-generated
stub code, though the README (lines 9–37, identical in both renders) links to that guide.

## 8. Other considerations

- **Not deprecated.** Ballerina Central reports `ballerina/grpc 1.14.7`, `graalvmCompatible: Yes`,
  `ballerinaVersion: 2201.12.0`, `pullCount: 220`; no deprecation field. No `@deprecated` in any
  bala source file.
- **Version integrity.** `package.json` in the bala reads `"version": "1.14.7"`; the render's
  qualified refs in `old` also read `1.14.7`. Same library on both sides; no version drift.
- **Size / tokens.** +167 lines (+13.5%) for a large gain in usable content — 29 dead placeholder
  lines replaced by 6 real class bodies and 23 documented type aliases, plus a 55-line service
  template. Good value per token.
- **Post-1.0, stable.** No pre-release concerns.
- **Doc quality.** Docstrings carry runnable ```ballerina``` examples on `Listener`, `Caller`,
  `Client`, `StreamingClient` — preserved verbatim in `new`. Source typos ("erros", "DEALINE_HEADER")
  are faithfully reproduced, not introduced by the renderer.
- **Encoding.** No mojibake or replacement characters in either render.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 1239 / 1406 |
| `grep -c '^// Unknown type:'` old / new | 29 / 0 |
| `grep -n '^// Unknown type:' old` | 29 lines: 651–659 (5 classes), 695, 697, 791–831 (21 errors), 1005 (`Listener`) |
| `grep -n '^// --- ' old` | 5 markers: README, END README, Types, Client, Functions |
| `grep -n '^// --- ' new` | 7 markers: + Service (1353), Annotations (1397) |
| `diff -u old new \| wc -l` | 407 |
| `grep -oE '(ballerina\|ballerinax)/[a-z_.]+:[0-9.]+:' old \| wc -l` | 23 (+2 `ballerina/grpc:grpc:` = 25) |
| same on `new` | 0 |
| `grep -c 'remote function' old / new` | 28 / 23 |
| `grep -c '^eg: TLS_ECDHE' old / new` | 2 / 2 |
| `grep -c 'Special Agent Note' old / new` | 24 / 28 |
| `comm -23` on sorted declaration headers | 3 old-only entries, all three are the version-qualified spellings of unions that exist in `new` |
| `comm -13` | 36 entries → 33 genuinely new declarations |
| JSON section sizes | old: typeDefs 91, clients 7, functions 7, services 0, annotations 0; new: 91/7/7/**1**/**3** |
| JSON name-set diff (typeDefs, clients, functions) | empty in both directions |
| JSON readme length | 13261 both |
| JSON `typeDefs` content diff | 34 changed; `ClientBasicAuthHandler` gains `"type": "Class"` in `new` |
| JSON `clients` content diff | `Caller`, `Client`, `StreamingClient`; `Caller`/`StreamingClient` lose the phantom `init: Constructor` |
| `diff` README block (1–377) | identical |
| `diff` Functions block (old 1170–1239 / new 1282–1351) | identical |
| Public-symbol parse of `bala/modules/grpc/*.bal` | 100 public symbols |
| Coverage: symbols with no declaration in render | old 32, new 0 |
| Symbols declared in render but not public API | identical set in both (enum members `REQUIRE`/`TLS`/`SSL`/`DTLS`/`OCSP_CRL`/`OCSP_STAPLING`/`OPTIONAL`/`GZIP` — all real `enum` members; `ContextString`/`with` are README-prose false positives of the extraction regex) |
| `caller.bal:32,65` | `public isolated function getId()` / `isCancelled()` — not remote |
| `caller.bal` grep `function init` | no match — `Caller` has no constructor |
| `streaming_client.bal` grep `function init` | no match |
| `client_endpoint.bal:37,59` | `init(string url, *ClientConfiguration config)`, `public isolated function initStub` |
| `service_endpoint.bal:22,33,48,59,72,84,94,204,295,306` | `Listener` class, 6 public methods, `DEFAULT_LISTENER_TIMEOUT = 120`, `ListenerConfiguration` fields, `public type Service distinct service object {}` |
| `grpc_errors.bal:18–90` | `Error distinct error` + 21 `distinct Error` subtypes + `ErrorType typedesc<Error>` |
| `annotation.bal:21–49` | 3 annotations, 3 backing record types |
| `auth_*.bal` greps | 7 auth classes; all signatures matched against render |
| `compiler-plugin.json` | `GrpcCompilerPlugin`, jar 1.14.7 |
| `GrpcCompilerPluginConstants.java:40–51` | 7 diagnostics GRPC_101…GRPC_107 |
| `GrpcServiceValidator.java:160–180` | descriptor annotation mandatory; `ServiceDescriptor` OR `Descriptor` accepted |
| `examples/async-streaming/server/phone_service.bal:24–26` | real-world form is `@grpc:ServiceDescriptor {...}` + `service "Phone" on new grpc:Listener(port)` |
| `git ls-remote --tags` | `v1.14.7` → `89f217a4ee574fbcc63d9c69b7186dde798bb270`; cloned `--depth 1 --branch v1.14.7` |
| Central API `ballerina/grpc/1.14.7` | 200, graalvmCompatible Yes, ballerinaVersion 2201.12.0, pullCount 220, no deprecation |
| Submodule public-symbol counts | wrappers 5, any 1, duration 1, struct 1, timestamp 1 = 9 |

## 10. Caveats and unverified items

- The first `git clone` attempt timed out on a network hiccup; the retry succeeded and the report's
  upstream citations come from the real `v1.14.7` checkout. Where GitHub and the bala could differ,
  the bala was used as the authority per the brief; no discrepancy was observed between them for
  any file consulted.
- `ServerReflectionServerReflectionResponseCaller` method qualifiers were read via a
  `grep -A 40` window on `reflection_pb.bal` rather than an exact absolute-line citation; the
  relative offsets (init +4, getId +8, isCancelled +24 from the class header) are reported instead.
- The "public symbols" inventory (100) comes from a regex parse of the bala's `.bal` files, not
  from a compiler symbol table. It covers `public type/class/enum/const/function/annotation` at
  column 0; a public declaration written with unusual formatting would be missed. Spot checks
  against the render found no such case.
- Whether `service grpc:Service "x" on new grpc:Listener(...)` (the template's typed form) compiles
  against the `distinct service object` type `Service` was reasoned by analogy with `http:Service`,
  not verified by an actual `bal build`. The repo's own examples use the untyped form.
- The claim that `Listener.init`'s rendered parameter order does not compile is from the Ballerina
  required-before-defaultable rule, not from a `bal build` run.
- No attempt was made to re-run the two-stage pipeline; both renders and both JSONs were taken as
  given.

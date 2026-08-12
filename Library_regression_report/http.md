# ballerina/http 2.16.6 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/http` |
| Pinned version | `2.16.6` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-http |
| Tag reviewed | `v2.16.6` (commit `2a1bfcd2720b30ffdb27bd24b21fb1a95f20db54`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/http/2.16.6/java21` |
| Old render | `3532` lines |
| New render | `4669` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a large, uniformly positive change for this library. The 155 `// Unknown type: <Name>`
placeholders in `old` are gone; every one of those 155 names now has a real definition in `new`
(verified individually, 0 missing). All 117 version-qualified type references
(`ballerina/http:2.16.6:Type`) are gone. Four genuinely wrong renderings in `old` are fixed in
`new`: (a) the phantom parameter `QueryParamType Additional Values` on 28 client resource methods,
(b) 12 non-`remote` methods that `old` labelled `remote`, (c) the two annotation attach points
(`on service` / `on service_function` → the source's `on service, type` / `on object function`),
(d) `class ClientObject` → `client class ClientObject`. `new` also adds five annotations that `old`
omitted entirely and replaces `old`'s 4-line empty `// --- Service (generic) ---` stub with a
26-line service/resource template.

Nothing correct in `old` is missing, truncated, or made less accurate in `new` — the complete
old-only line sweep (§4) returns only lines that were replaced by corrected counterparts.

`new` still has real accuracy gaps against the library source (§5), the largest being that object
fields are never rendered (69 of 101 classes come out as empty `class X {}`, including
`http:Response`, which loses `statusCode`/`reasonPhrase`/`cacheControl`) and that 50 error types
collapse to `type X error;`, erasing the whole `http:Error` subtype hierarchy. These are renderer
limitations, not regressions: `old` emitted nothing at all for those types.

## 2. Change inventory

Mechanical diff (`diff -u old new`): **112 hunks, +1368 lines, −231 lines**.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 155 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) — occurrences | 117 | 0 |
| `// --- section ---` markers | 8 | 7 |
| Doc-comment (`#`) lines | 1140 | 1794 |
| Non-ASCII lines | 1 | 6 (all legitimate: smart quotes from source docs / em-dashes in the new service template) |

### Top-level declarations by kind

| Kind | old | new |
|---|---|---|
| `class` | 12 | 91 |
| `client class` | 8 | 10 |
| `type` (record + alias) | 158 | 232 |
| `const` | 161 | 161 |
| `enum` | 5 | 5 |
| module-level `function` | 7 | 7 |
| `public annotation` | 2 | 7 |
| `listener` (README sample) | 1 | 1 |
| service block | 1 (stub, 4 comment lines) | 1 (26-line template) |

### Added (177 new top-level declaration lines)

- 79 `class` + 2 `client class`: 60 `Status*` status-code classes, `Request`, `Response`,
  `RequestContext`, `Headers`, `Listener`, `Cookie`, `CookieStore`, `CsvPersistentCookieHandler`,
  `HttpCache`, `HttpFuture`, `PushPromise`, `RequestCacheControl`, `ResponseCacheControl`,
  `ClientBasicAuthHandler`, `ClientBearerTokenAuthHandler`, `ClientSelfSignedJwtAuthHandler`,
  `ListenerFileUserStoreBasicAuthHandler`, `ListenerJwtAuthHandler`, `LoadBalancerRoundRobinRule`,
  `DefaultStatus`, and the two client object types `ClientObject` / `StatusCodeClientObject`.
- 74 `type` aliases: the entire error hierarchy (`Error`, `ClientError`, `ListenerError`, … 64
  error types) plus `TargetType` and `ReqCtxMemberType`.
- 5 annotations: `Payload`, `CallerInfo`, `Header`, `Query`, `Cache`.
- 102 distinct method names newly rendered inside classes (all verified to exist in source, §3).

### Removed (nothing lost)

The `comm` sweep of old-only lines (§9, cmd 14) returns 32 lines. Every one is a replaced line:
- 2 curated annotation descriptions, replaced by the authoritative source doc strings;
- 2 wrong annotation declarations, replaced by correct ones;
- 4 lines of the empty `// --- Service (generic) ---` stub, replaced by the service template;
- 2 `class ClientObject {` / `class StatusCodeClientObject {`, replaced by `client class …` with
  22 methods each;
- 8 `remote function …` lines, replaced by the correct non-`remote` form;
- 14 client resource-method lines, replaced by the same lines minus the phantom parameter.

Records / enums / constants: structurally byte-identical apart from de-qualification. Comparing
record bodies field-by-field: **135 records in both, 0 added, 0 removed, 5 differ — and all 5
differences are only the removal of `ballerina/http:2.16.6:` / `ballerina/crypto:2.12.1:`
prefixes** (`ClientSecureSocket`, `HttpCallerInfo`, `HttpServiceConfig`, `Links`,
`ListenerSecureSocket`). 5 enums identical, 161 constants identical, 7 module-level functions
byte-identical (`diff` of the whole Functions section is empty). README section (lines 1–127)
byte-identical.

### JSON-stage inventory

| | old | new |
|---|---|---|
| `typeDefs` | 491 | 491 |
| `clients` | 8 | 8 |
| `functions` | 7 | 7 |
| `annotations` | 2 | 11 (attach-point-expanded; renderer merges to 7 declarations) |
| `services` | 1 | 1 |
| `clients.*.parameters` | 428 | 400 (−28 = the phantom `QueryParamType Additional Values`) |
| `typeDefs.*.functions` objects | 210 | 193 |

New JSON keys in `new`: `typeDefs.baseType` (74), `typeDefs.isClient` (2),
`typeDefs.functions.accessor`/`paths` (14 resource functions),
`services.identifier`, `services.handlerTemplates`, `services.annotations`.
Dropped JSON keys: `annotations.displayName` (2 → 0), `services.instructions` (was `""`).

## 3. Correctness against library source

All checks are against the bala (`modules/http/*.bal`), which is byte-identical to the upstream
`v2.16.6` tag for the three files sampled (`http_annotation.bal`, `http_status_code_types.bal`,
`http_errors.bal` — `diff -q` IDENTICAL).

| What `new` changes/adds | Source evidence | Verdict |
|---|---|---|
| `ClientOAuth2Handler.enrichHeaders` / `.getSecurityHeaders` are plain `function`, not `remote` | `auth_client_oauth2_handler.bal:49,62` — `public isolated function` | `new` correct, `old` wrong |
| `Client`/`StatusCodeClient` `.getCookieStore`, `.circuitBreakerForceClose`, `.circuitBreakerForceOpen`, `.getCircuitBreakerCurrentState` are plain functions | `http_client_endpoint.bal:509,517,529,542`; `http_status_code_client.bal:441,449,461,474` | `new` correct, `old` wrong |
| `Caller.getRemoteHostName` plain function | `http_connection.bal:137` | `new` correct, `old` wrong |
| `FailoverClient.getSucceededEndpointIndex` plain function | `resiliency_failover_client.bal:480` | `new` correct, `old` wrong |
| Removal of `QueryParamType Additional Values` param | `http_client_endpoint.bal:73-74` — real signature is `[PathParamType ...path](map<string\|string[]>? headers = (), TargetType targetType = <>, *QueryParams params)`; there is no such parameter | `new` correct, `old` fabricated it |
| `ClientObject`/`StatusCodeClientObject` are client objects | `http_client_object.bal:18` / `http_status_code_client_object.bal:18` — `public type ClientObject client object {` | `new` correct (`client class`), `old` wrong (`class`) |
| `ClientObject.delete(... message = ())` | `http_client_object.bal:69` — `RequestMessage message = ()` | `new` correct |
| `ServiceConfig on type, service` | `http_annotation.bal:66` — `on service, type` | `new` correct (order differs only); `old` said `on service` |
| `ResourceConfig on object function` | `http_annotation.bal:88` | `new` correct; `old` said `on service_function` |
| `Payload on parameter, return` | `http_annotation.bal:98` | correct |
| `CallerInfo on parameter` | `http_annotation.bal:109` | correct |
| `Header on parameter, record field` | `http_annotation.bal:119` (`public const annotation`) | correct modulo dropped `const` |
| `Query on parameter, record field` | `http_annotation.bal:129` (`public const annotation`) | correct modulo dropped `const` |
| `Cache on return` | `http_annotation.bal:166` | correct |
| `ClientBasicAuthHandler` rendered as plain `class` with `init/enrich/enrichHeaders/getSecurityHeaders` | `auth_client_basic_auth_handler.bal:20,27,35,49,62` — `public isolated class`, all `public isolated function` | correct |
| Service template: accessors "get, post, put, delete, patch, head, options, default" | `docs/spec/spec.md:424-425` — "it can be get, post, put, delete, head, patch, options and default" | correct |
| Service template: `on new http:Listener(int port, http:ListenerConfiguration config = {})` | `http_service_endpoint.bal:32` — `init(int port, *ListenerConfiguration config)` | correct representation |
| `InterceptableService.createInterceptors()` | `http_interceptors.bal:41-47` | correct (`Interceptor` expanded to its union members) |
| `Response.setPayload(anydata\|mime:Entity[]\|stream<byte[], io:Error?>\|stream<http:SseEvent, error?>, string? )` | `http_response.bal:529-530` | correct |
| `Request.setPayload(anydata\|mime:Entity[]\|stream<byte[], io:Error?>, string?)` | `http_request.bal:545-546` | correct |
| `Response.setETag(json\|xml\|string\|byte[])` | `http_response.bal:373` | correct |
| `Request.getQueryParamValues(string) returns string[]?` | `http_request.bal:102` | correct |
| `CookieOptions.maxAge = 0` in `Cookie.init` | `cookie.bal:35` | correct |
| `RequestInterceptor` / `ResponseInterceptor` / `Service` / `ServiceContract` rendered empty | `http_interceptors.bal:21,26` — genuinely empty `distinct service object {}` | correct content, wrong kind word (see §5) |

**No invented symbols.** All 102 distinct method names appearing in `new`'s class bodies were
matched against `function <name>(` in the bala default module — 0 not found.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. Whole-file old-only line sweep — every non-blank, whitespace-normalised line of `old` that does
   not appear anywhere in `new`, excluding `// Unknown type:` lines and version-qualified lines:
   **32 lines**, all itemised in §2 "Removed". Each has a corrected counterpart in `new`; none is
   dropped information.
2. Declaration-set diff (`comm` of extracted top-level declarations): 20 old-only entries, of which
   12 are the de-qualified union aliases (all 12 verified present unqualified in `new`), 2 are the
   `class` → `client class` requalification, 2 are the corrected annotations, and 4 are the Service
   stub lines.
3. Record-body diff: 135/135 records present in both, 5 differ, all differences are de-qualification
   only. No field, default, or optionality dropped.
4. Enum bodies: 5/5 identical. Constants: 161/161 identical.
5. Module-level Functions section: `diff` empty.
6. README + header (lines 1–127): `diff` empty.
7. Doc-comment sweep: only 2 unique doc lines exist in `old` and not in `new` — the two curated
   annotation blurbs ("Define advanced configurations like service level security, etc." /
   "…resource level media types, security, etc."), replaced by the actual source doc strings from
   `http_annotation.bal:65,87`. Judged not a regression: the replacement text is authoritative and
   is accompanied by the corrected attach points. Recorded here for the reviewer's awareness only.
8. Coverage: 0 default-module public symbols present in `old` and absent from `new` (§6).
9. No malformed construct exists in `new` that does not also exist in `old` in the same form
   (the `X|()[]` optional-array bug already occurs in `old` as `Bucket|()[]`).

## 5. Issues in `new` (independent of `old`)

Ordered by impact. Items 1–6 are new-only in the sense that `old` did not render the affected
declarations at all; items 7–9 exist identically in `old`.

1. **Object fields are never rendered.** 69 of 101 classes in `new` are emitted as empty
   `class X {}`. Worst cases: `class Response {}` … loses `public int statusCode`,
   `public string reasonPhrase`, `public string server`, `public string resolvedRequestedURI`,
   `public ResponseCacheControl? cacheControl` (`http_response.bal:3-7`) — `statusCode` is one of
   the most-used symbols in the whole library. Every one of the 60 `Status*` classes is emitted
   empty although its entire content is `public STATUS_XXX code` (`http_status_code_types.bal:98-101`),
   and `class Status {}` loses `public int code` (`http_status_code_types.bal:35-37`).
   Shared renderer limitation (`old` also emits 0 field lines inside classes) but only materially
   visible in `new`, which renders 101 classes instead of 20.
2. **Error hierarchy flattened.** 51 lines of the form `type X error;`. For 50 of them the source
   declares a *named* parent, e.g. `public type ListenerError distinct Error;` (`http_errors.bal:53`),
   `public type NoContentError distinct ClientError;` (`:99`),
   `public type UnsupportedActionError distinct GenericClientError;`. The rendered form erases
   which errors are `http:ClientError` vs `http:ListenerError`, which is exactly what an LLM needs
   to write `is http:ClientError` checks. 4 more render as structural `error<record {|…|}>` instead
   of the named parent (e.g. `QueryParameterValidationError`, source `distinct QueryParameterBindingError`,
   `http_errors.bal:118`). Only the 19 intersection types (`X & httpscerr:YError`) keep their parent.
3. **13 dangling `httpscerr:` references.** `new` emits `httpscerr:InternalServerErrorError`,
   `httpscerr:BadRequestError`, `httpscerr:NotFoundError`, etc. (render lines 2881, 2893, 2899,
   2917, 2920, 3034, 3037, 3040, 3043, 3046, 3049, 3052, 3055). The prefix is never imported, never
   defined in the render, and — unlike `mime:` / `auth:` / `oauth2:` / `crypto:` / `jwt:` / `time:` /
   `cache:` / `log:` — carries no `// Special Agent Note: … FROM …` annotation. `http.httpscerr` is
   a submodule of this same package (`package.json` `export: ["http","http.httpscerr"]`), so the
   external-package note mechanism does not fire. `old` had 0 such references.
4. **`Client|()[]` instead of `Client?[]`** in `LoadBalancerRule.getNextClient` (render line 3781)
   and `LoadBalancerRoundRobinRule.getNextClient` (line 4035). Source:
   `resiliency_http_load_balancer_rule.bal:25` — `getNextClient(Client?[] loadBalanceCallerActionsArray)`.
   `Client|()[]` parses as `Client | (()[])`, a different type. Same bug class as the pre-existing
   `Bucket|()[]` that appears once in *both* renders.
5. **Wrong default `int arraySize = 0`** on `Request.getByteStream` and `Response.getByteStream`
   (render lines 1195, 3550). Source default is `8192` (`http_request.bal:329`,
   `http_response.bal:309`); the parameter's own doc text in the same render says "Default size is
   8KB". Traced to the Java extractor, not the TS renderer — both JSONs carry `"default": "0"`, so
   this is an upstream data bug that `new` merely surfaces.
6. **`RequestContext.getWithType` default is a type name.** Rendered as
   `… targetType = http:ReqCtxMember` (render line 3985); also the `typedesc<…>` wrapper is dropped,
   so the parameter type is printed as the bare union. Not valid Ballerina as written.
7. **Included-record parameters are flattened *and* duplicated.** `Listener.init` renders as
   `init(int port, string host = "0.0.0.0", …, ServerSocketConfig socketConfig = {}, …,
   ListenerConfiguration config)` — the fields of `*ListenerConfiguration` are expanded positionally
   *and* the record itself is appended as a trailing parameter (`http_service_endpoint.bal:32` —
   `init(int port, *ListenerConfiguration config)`). Same for `Cookie.init(… , CookieOptions options)`
   (`cookie.bal:75`). Pre-existing: 3 occurrences in `old`, 4 in `new`.
8. **Two contradictory renderings of the same client API inside one file.** In the Types section
   `client class ClientObject` says `TargetType targetType = <>` and `RequestMessage message = ()`;
   in the Client section `client class Client` says
   `http:Response|anydata|stream<http:SseEvent, error?> targetType = http:Response|anydata|stream<…>`
   (a type expression used as a default value) and `RequestMessage message = {}` (source says `()`,
   `http_client_endpoint.bal:225`). `old` had only the second, wrong form; `new` has both, which is
   an improvement in information but a new internal inconsistency.
9. **Shared wrong defaults / lost qualifiers**, present identically in both renders:
   `decimal timeout = 0.0d` ×4 (source `ClientConfiguration.timeout = 30`, `http_types.bal:81`);
   `Caller.respond(… message = {})` (source `= ()`, `http_connection.bal:49`);
   `public isolated`, `readonly`, `distinct`, and `const` qualifiers are dropped everywhere
   (e.g. `public const annotation HttpHeader Header` → `public annotation …`);
   object types (`public type Status distinct object`, `public type RequestInterceptor distinct
   service object`) are printed with the keyword `class`.

Also worth noting: the JSON stage in `new` drops the synthesized `Constructor init` entry for 66
typeDefs (all `Status*`, plus `Headers`, `HttpFuture`, `RequestContext`, `RequestCacheControl`,
`ResponseCacheControl`, `LoadBalancerRoundRobinRule`). Verified that none of those classes declares
an explicit `init` in the source, so the omission is arguably *more* faithful; it has no effect on
the `old` render (those classes were `// Unknown type:` there). It does mean `new` gives no hint
that e.g. `http:ResponseCacheControl cc = new;` is legal. `annotations.displayName` is likewise
dropped from the JSON; it was never rendered.

## 6. Coverage gaps vs. the library

**Default module (`modules/http`): 0 gaps in `new`.**
389 public symbols (`class` / `type` / `const` / `enum` / `annotation` / `function`) were extracted
from the bala's default module and matched against top-level declarations in each render:

| | missing declarations |
|---|---|
| `old` | **155** (81 classes + 74 types — exactly the 155 `// Unknown type:` lines) |
| `new` | **0** |

Member level, `new` is not complete: object fields are absent for all 101 rendered classes (§5.1).

**Submodule-only API — shared gap, not a regression.**
`package.json` exports two modules: `http` and `http.httpscerr`. `http.httpscerr` contributes
**42 public symbols** (`StatusCodeError`, `ErrorDetail`, `DefaultErrorDetail`,
`DefaultStatusCodeError`, and 38 `<Status>Error` types such as `BadRequestError`, `NotFoundError`,
`InternalServerErrorError`). **None of the 42 appears in either render** — both pipelines extract
`pkg.getDefaultModule()` only. `new` makes the gap more conspicuous by emitting 13 `httpscerr:`
references to types it never defines (§5.3).

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.stdlib.http.compiler.HttpCompilerPlugin`
with `http-compiler-plugin-2.16.6.jar` + `ballerina-to-openapi-2.4.0.jar`. Upstream source:
66 Java files under `compiler-plugin/src/main/java/io/ballerina/stdlib/http/compiler/`.

What it contributes:
- **Validators**: `HttpServiceValidator`, `HttpResourceValidator`, `HttpInterceptorServiceValidator`,
  `HttpInterceptorResourceValidator`, `HttpServiceContractResourceValidator`,
  `HttpServiceObjTypeAnalyzer` — resource signature/accessor/return-type rules, `@http:Payload` /
  `@http:Header` / `@http:Query` / `@http:CallerInfo` placement, caller-vs-return-type rules.
- **Code actions** (`codeaction/`, 15 classes): add header/payload/resource parameter, add
  interceptor methods, add response cache config / content type, change header param type,
  `ImplementServiceContract`.
- **Code modifier + OpenAPI** (`codemodifier/`, `oas/`, `OpenAPISpecGenerator`): compile-time
  generation of the service's OpenAPI definition, injected into `HttpServiceConfig.openApiDefinition`,
  and of `HttpServiceConfig.serviceType`.
- **Completions** (`completion/`) and a **static code analyzer** (`staticcodeanalyzer/`, e.g.
  rule `ballerina/http:1` "Avoid allowing default resource accessor", `docs/spec/spec.md:3532`).

Render implications:
- `new`'s service template correctly reflects the plugin's resource-signature rules (accessor set,
  caller/request/headers/payload parameter slots, per-slot annotation placement, `@http:ResourceConfig`
  on the handler, `@http:Cache` on the return). `old` had none of this. Verified the accessor set
  against `docs/spec/spec.md:424-425`.
- Neither render flags that `HttpServiceConfig.openApiDefinition` and `HttpServiceConfig.serviceType`
  are **compiler-generated, not user-settable**, and that `basePath` is "only allowed on service
  contract types" (the doc string does say so, and both renders carry that doc line). An LLM could
  try to set `openApiDefinition` — pre-existing in both, unchanged by spec v2.
- Nothing the plugin implies is present in `old` but absent from `new`.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerina/http/2.16.6`: `deprecated: null`,
  `visibility: public`, `ballerinaVersion 2201.13.0`, modules `["http","http.httpscerr"]`.
  Stable 2.x version; no pre-1.0 caveat.
- **Size / tokens.** `new` is +32% lines (3532 → 4669) and the JSON is +9.8% bytes
  (724,194 → 795,382). The extra 1137 lines buy 155 previously-unrenderable types and ~180 method
  signatures — a good ratio. 60 of the added classes are the empty `Status*` shells, i.e. ~180 lines
  of near-zero-value output that would become useful only if field rendering were fixed (§5.1).
- **Doc quality.** Doc lines rise 1140 → 1794 with no doc text lost (2 curated blurbs swapped for
  source docs). Every added class/method carries its source doc comment.
- **Encoding.** Clean. The 6 non-ASCII lines in `new` are 2 smart quotes inherited from source docs
  and 4 em-dashes authored by the new service template. No mojibake.
- **Compilability.** Neither render is meant to compile verbatim (both use `[... path]`,
  `QueryParams params` without `*`, and type-expression defaults). `new` is closer to compilable
  than `old` in the client sections but introduces `Client|()[]` and
  `targetType = http:ReqCtxMember`.

## 9. Evidence log

1. `git ls-remote --tags …module-ballerina-http | grep 'v2\.16\.[0-9]+$'` → `v2.16.6` exists
   (`287cf01e…`). `git clone --depth 1 --branch v2.16.6` → HEAD `2a1bfcd2720b30ffdb27bd24b21fb1a95f20db54`,
   grafted, tag `v2.16.6`.
2. `diff -q src/ballerina/{http_annotation,http_status_code_types,http_errors}.bal bala/modules/http/…`
   → IDENTICAL ×3. `src/ballerina/Ballerina.toml:4` → `version = "2.16.6"`.
3. `wc -l` renders → old 3532, new 4669.
4. `grep -c '^// Unknown type:'` → old 155, new 0. `sort -u` of the 155 names → 155 distinct.
5. Loop over the 155 names against `grep -E "^(public )?(isolated )?(distinct )?(client )?(class|type|enum|const) <name>\b"` in `new` → `missing=0`.
6. `grep -oE '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:'` → old 117 occurrences on 24 lines, new 0.
7. `awk` over `diff -u old new` → added 1368, removed 231, 112 hunks (matches `OLD_AND_NEW_DIFFS/http_diff.md`).
8. `grep -n '^// --- '` → old 8 markers (incl. `Service (generic)`), new 7.
9. Declaration-set extraction + `comm -23` → 20 old-only entries (12 de-qualified unions, 2 class→client class, 2 annotations, 4 Service stub); each of the 12 unions verified present in `decls_new.txt` (`grep -c` = 1 each).
10. Python record-body comparison → 135 records both sides; only-in-old ∅, only-in-new ∅; 5 differ, all de-qualification only.
11. Python enum comparison → 5/5 identical bodies. `grep '^const '` sorted → 161/161 identical.
12. `diff <(sed -n '3433,3518p' old) <(sed -n '4531,4616p' new)` → empty (Functions section).
13. `diff <(sed -n '1,127p' old) <(sed -n '1,127p' new)` → empty (README + header).
14. `comm -23` of whitespace-normalised unique lines, excluding `// Unknown type:` and version-qualified lines → 32 old-only lines, all itemised in §2.
15. Doc-line `comm` → 1140 vs 1794; only 2 unique old doc lines absent from `new`.
16. Python class-member comparison → old 20 classes / new 101; only-in-old ∅; qualifier changes `ClientObject`, `StatusCodeClientObject` `class`→`client class`; the `remote`→plain changes listed in §3.
17. Source verification of the `remote` fix: `http_client_endpoint.bal:509,517,529,542`;
    `http_status_code_client.bal:441,449,461,474`; `http_connection.bal:137`;
    `resiliency_failover_client.bal:480`; `auth_client_oauth2_handler.bal:49,62` — all
    `public isolated function`, none `remote`.
18. `grep -n "resource .*function get \[" bala/modules/http/*.bal` → 6 hits, all
    `(map<string|string[]>? headers = (), TargetType targetType = <>, *QueryParams params)`;
    no `Additional Values` parameter anywhere in the source.
19. `grep -n "public annotation\|const annotation" bala/modules/http/http_annotation.bal` → 7
    annotations at lines 66, 88, 98, 109, 119, 129, 166; lines 119/129 are `public const annotation`.
20. Python class-empty scan → old 20 classes / 12 empty; new 101 classes / 69 empty.
    `awk` scan for field-shaped lines inside class bodies → 0 in both files.
21. Python: 102 distinct method names in `new` class bodies; each matched against
    `function <name>\s*\(` in the concatenated bala default module → 0 not found.
22. Strict coverage check: 389 public default-module symbols; missing in `old` 155, missing in `new` 0.
23. `grep -c` on `modules/http.httpscerr/*.bal` → 42 public symbols; `grep -c 'httpscerr:'` → old 0, new 13; `grep -o 'FROM ballerina/[a-z.]*'` in `new` → notes only for auth/cache/crypto/jwt/log/mime/oauth/time, none for httpscerr.
24. `grep -oE '[A-Za-z0-9_>]+\|\(\)\[\]'` → old `Bucket|()[]` ×1; new `Bucket|()[]` ×1 + `Client|()[]` ×2. Source `resiliency_http_load_balancer_rule.bal:25` → `Client?[]`.
25. `http_request.bal:329` / `http_response.bal:309` → `arraySize = 8192`; both JSONs carry `"default": "0"` for that parameter (Python dump).
26. `http_types.bal:81` → `decimal timeout = 30`; `grep -c 'decimal timeout = 0.0d'` → 4 in old, 4 in new.
27. `http_connection.bal:49` → `respond(… message = ())`; both renders emit `message = {}` (old line 3098, new line 4196).
28. `http_service_endpoint.bal:32` → `init(int port, *ListenerConfiguration config)`; `cookie.bal:75` → `init(string name, string value, *CookieOptions options)`. `grep -cE 'Configuration [a-z]+\) returns'` → 3 in old, 4 in new.
29. `grep -oE '^type \w+ error;$'` in `new` → 51; loop against `grep "^public type <X> "` in source → 50 of 51 declare a named parent (only `Error` is `distinct error`).
30. Python JSON key-frequency diff → typeDefs 491/491, clients 8/8, functions 7/7, annotations 2/11, `clients.*.parameters` 428/400, `annotations.displayName` 2/0, `services.instructions` 1/0, new `services.handlerTemplates`/`identifier`/`annotations` subtrees, `typeDefs.baseType` 0/74, `typeDefs.isClient` 0/2.
31. Python per-typeDef function-set diff → 72 typeDefs changed: +22 methods each on `ClientObject`/`StatusCodeClientObject`, +4 `PersistentCookieHandler`, +1 `LoadBalancerRule`, +1 `InterceptableService`; −1 synthesized `Constructor init` on 66 typeDefs. `awk` scan of those classes in the bala → none declares an explicit `init`.
32. `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/http/2.16.6` → version 2.16.6, ballerinaVersion 2201.13.0, `deprecated: null`, modules `["http","http.httpscerr"]`.
33. `docs/spec/spec.md:424-425` → accessor list matches the new service template.
34. `find compiler-plugin -name '*.java' | wc -l` → 66; `ls …/codeaction/` → 15 classes; `cat compiler-plugin/compiler-plugin.json` → plugin id/class/jars as quoted in §7.
35. `wc -c` JSONs → old 724,194 / new 795,382. `grep -c -P '[^\x00-\x7F]'` → old 1, new 6 (lines listed and inspected).

## 10. Caveats and unverified items

- The renderer/extractor source (`ballerina-vscode` on either side) was not read; every statement
  about *why* a difference exists is inferred from the two JSONs and the two renders. Where a defect
  is traceable to the JSON stage it is stated as such with the JSON value quoted (arraySize, timeout).
- Only three source files were byte-compared between the `v2.16.6` tag and the bala. The remaining
  files were read from the bala only, which the brief designates authoritative; no contradiction was
  observed in any spot check.
- "0 default-module coverage gaps" is measured at *declaration* granularity (name present as a
  top-level declaration). It is not a claim that every rendered signature is byte-accurate; §3 lists
  the ~30 signatures spot-checked against source, and §5 the inaccuracies found.
- Whether `type X error;` for a `distinct <Parent>` alias is intended behaviour of spec v2 or a
  defect was not established — it is reported as an accuracy gap, not as a bug in a specific
  component.
- The claim that the compiler plugin's OpenAPI code modifier writes `openApiDefinition` was read
  from `OpenAPISpecGenerator.java` / `codemodifier/` file names and the `HttpServiceConfig` doc
  comment; the modifier's runtime behaviour was not executed or traced.
- The two curated annotation blurbs present only in `old` are judged an acceptable replacement
  rather than a regression. That is a judgement call, not a measurement; a reviewer who values the
  curated hint text may wish to count it as one cosmetic regression.

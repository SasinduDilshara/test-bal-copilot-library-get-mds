# ballerina/websub 2.15.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/websub` |
| Pinned version | `2.15.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-websub |
| Tag reviewed | `v2.15.0` (exact tag; shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/websub/2.15.0/java21` |
| Old render | `445` lines |
| New render | `539` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. `diff old new` yields 110 added lines and 16
removed lines; **every removed line is either a `// Unknown type: X` stub (11 lines + 2 stray blanks)
or one of the 3 lines that carried a version-qualified type reference (`ballerina/websub:2.15.0:Error?`,
`…:ClientConfiguration`) which `new` rewrites to the plain name**. No declaration, parameter, default,
return type, doc line or README byte was lost.

`new` gains: 10 real error type definitions, the `Listener` class with all 7 methods, a `// --- Service ---`
section describing the `websub:SubscriberService` shape, and a `// --- Annotations ---` section with
`SubscriberServiceConfig`. The README block (lines 1–199) is byte-identical between the two.

Six accuracy problems exist in `new` that `old` did not have the opportunity to have (it emitted nothing
at all for those symbols). The most consequential is that the service block labels the
`@websub:SubscriberServiceConfig` annotation as **optional**, while the websub compiler plugin rejects a
subscriber service without it at `ERROR` severity (`WEBSUB_101`).

## 2. Change inventory

Line counts (`wc -l`): old **445**, new **539**.

Signals (`grep -c`):

| Signal | old | new |
|---|---|---|
| `// Unknown type:` | 11 | 0 |
| Version-qualified refs (`ballerina/websub:2.15.0:`) | 3 | 0 |
| `// --- ` section markers | 5 | 7 |

Section markers — old: README(7), END README(198), Types(200), Client(396), Functions(428).
New: README(7), END README(198), Types(200), Client(458), Functions(490), **Service(509)**, **Annotations(536)**.

Declarations added in `new` (23; none removed):

| Kind | Count | Names |
|---|---|---|
| `type` (error) | 10 | `Error`, `ServiceExecutionError`, `ListenerError`, `ResourceDiscoveryFailedError`, `SubscriptionInitiationError`, `SubscriptionVerificationError`, `UnsubscriptionVerificationError`, `SubscriptionDeniedError`, `InternalHubError`, `SubscriptionDeletedError` (new:371–398) |
| `class` | 1 | `Listener` (new:409–456) |
| class methods | 7 | `init`, `attach`, `attachWithConfig`, `detach`, `'start`, `gracefulStop`, `immediateStop` |
| `service` template | 1 | `service websub:SubscriberService on new websub:Listener(...)` (new:514–534) |
| service remote methods | 5 | `onEventNotification` (required), `onSubscriptionVerification`, `onUnsubscriptionVerification`, `onSubscriptionValidationDenied`, `onHubError` (all optional) |
| `annotation` | 1 | `public annotation SubscriberServiceConfiguration SubscriberServiceConfig on service;` (new:539) |

Modified (3 lines, all improvements): the two client `init` return types and the inline
`discoveryConfig` record now use unqualified `Error?` / `ClientConfiguration` instead of
`ballerina/websub:2.15.0:…`.

JSON side (full `difflib` diff of the two pretty-printed JSONs): identical except for
(a) `"services": []` → 1 service object, (b) `"annotations": []` → 1 annotation object,
(c) `"baseType": "error<CommonResponse>"` added to the 10 error typeDefs, (d) `"type": "Class"` added to
the `Listener` typeDef (old had no `type` key at all → hence `// Unknown type: Listener`),
(e) 3 version-qualified names unqualified. `typeDefs` is 23 on both sides; `clients` 2; `functions` 2.
The `Listener.init` parameter list in the JSON is **byte-identical** on both sides.

## 3. Correctness against library source

Upstream `v2.15.0` `ballerina/*.bal` is byte-identical to the bala `modules/websub/*.bal` for all 8
API-bearing files checked (`diff -q`: `annotation.bal`, `commons.bal`, `errors.bal`, `sub_listener.bal`,
`subscriber_service.bal`, `subscriber_client.bal`, `resource_discovery.bal`, `utils.bal` — all identical),
so GitHub and the bala do not disagree here.

Verified item by item:

- **10 error types** — `errors.bal:18–45`. All 10 names and all 10 doc strings match the render exactly
  (including the library's own typos "verificatation", "Represents a listener errors."). Base type: see §5.1/§5.2.
- **`Listener` class + methods** — `sub_listener.bal:25` (`public class Listener`), `init` at :38,
  `attach` :62, `attachWithConfig` :86, `detach` :129, `'start` :152, `gracefulStop` :176,
  `immediateStop` :212. All 7 public methods present in the render with matching names, parameter
  names/types and return type `Error?`. The 6 non-public helpers (`executeAttach`,
  `retrieveGeneratedServicePath`, `externAttach`, `detachHttpService`, `retrieveAttachedServices`,
  `waitForVerification`, `isVerificationCompleted`) are correctly excluded.
- **`attach` / `attachWithConfig` / `detach` signatures** — source `string[]|string? name = ()`; render
  `string[]|string|() name = ()`. Semantically equal.
- **Service block vs compiler plugin** — `compiler-plugin/.../task/validator/ServiceDeclarationValidator.java:65–99`.
  `allowedMethods` = exactly the 5 methods the render lists. `allowedParameterTypes` maps each to exactly
  the type the render shows (`onHubError`→`InternalHubError`, `onSubscriptionValidationDenied`→
  `SubscriptionDeniedError`, `onSubscriptionVerification`→`SubscriptionVerification`,
  `onUnsubscriptionVerification`→`UnsubscriptionVerification`, `onEventNotification`→
  `ContentDistributionMessage`). `allowedReturnTypes` matches the render's returns.
  `executeRequiredMethodValidation` (:134–140) makes `onEventNotification` the one required method — the
  render marks exactly that one `// required`. This section is correct.
- **Annotation** — `annotation.bal:50` `public annotation SubscriberServiceConfiguration SubscriberServiceConfig on service;`
  reproduced verbatim at new:539, with the correct doc line from `annotation.bal:49`.
- **`getHeader` / `getHeaders`** — `utils.bal:251,262`; present and correct in both renders.
- **Records** — `ClientConfiguration` (commons.bal:189), `SubscriberServiceConfiguration` (annotation.bal:31),
  `ListenerConfiguration` (commons.bal:110), `SubscriptionChangeRequest/Response` (:123,:137),
  `SubscriptionVerification`/`UnsubscriptionVerification`/`ContentDistributionMessage`/
  `…VerificationSuccess`/`Acknowledgement`: field names, types and doc strings match. Unchanged between
  old and new apart from the one `discoveryConfig` line.
- **Central metadata** — `api.central.ballerina.io/2.0/registry/packages/ballerina/websub/2.15.0`:
  `modules` = `[websub]` only, `deprecated: null`, `ballerinaVersion 2201.12.0`, `graalvmCompatible: Yes`.
  `package.json` `"export": ["websub"]`. Single-module package ⇒ no submodule-only API gap.

## 4. Regressions

**None found.**

Basis: `diff old new | grep '^<'` returns exactly 16 lines, listed and classified individually above —
11 `// Unknown type:` stubs, 2 blank lines adjacent to them, and 3 lines replaced by strictly better
versions of themselves (version-qualified → plain type name). `diff old new | grep -c '^>'` = 110.
A sorted set-difference of declaration headers (`grep -oE '^(public )?(final )?(isolated )?(client )?(type|class|const|annotation|function|service) …' | sort`)
shows 13 additions and **0 deletions**. README lines 1–199 `diff` clean. The pre-existing doc-wrapping
defect (continuation lines losing their leading `#`, e.g. `found.` on its own line) occurs 3 times in
*both* files — unchanged, not a regression.

## 5. Issues in `new` (independent of `old`)

**5.1 `CommonResponse` is referenced 10 times but never defined (dangling type).**
All 10 error typedefs render as `type X error<CommonResponse>;` (new:371–398), but `CommonResponse` is
**not public** in the library (`commons.bal:85` — `type CommonResponse record {| … |}`) and appears
nowhere else in the render (`grep -n CommonResponse` → only those 10 lines). An LLM copying this cannot
resolve the symbol. `old` had 0 references (it emitted stubs). Source of the string is the new JSON field
`"baseType": "error<CommonResponse>"`.

**5.2 `distinct` dropped and the error hierarchy flattened.**
Source: `Error` and `ServiceExecutionError` are `distinct error<CommonResponse>`; the other **8 are
`distinct Error`** (`errors.bal:24–45`). `new` renders all ten identically as `error<CommonResponse>`,
so the render no longer conveys that e.g. `ListenerError`/`SubscriptionDeletedError` are subtypes of
`websub:Error`, nor that these are distinct (nominal) error types. This misleads on `is Error` checks and
on `check`/`error?` narrowing.

**5.3 The service block says the config annotation is optional; the compiler says it is mandatory.**
new:511–513 renders `# Optional: this service may carry the @websub:SubscriberServiceConfig annotation`
and `@websub:SubscriberServiceConfig {...} // optional`. Source of truth:
`ServiceDeclarationValidator.executeServiceAnnotationValidation` (:123–132) raises `WEBSUB_101` whenever
the annotation is absent, and `WebSubDiagnosticCodes.java:29–31` declares `WEBSUB_101` with
`DiagnosticSeverity.ERROR` ("Subscriber service should be annotated with websub:SubscriberServiceConfig").
The underlying JSON carries `"annotations":[{"name":"SubscriberServiceConfig","presence":"optional",…}]`.
A model following this render will emit a websub service that does not compile.

**5.4 Five wrong default values on `Listener.init`.**
new:410 renders `string host = ""`, `decimal timeout = 0.0d`, `int http2InitialWindowSize = 0`,
`decimal minIdleTimeInStaleState = 0.0d`, `decimal timeBetweenStaleEviction = 0.0d`. These fields are
inherited via `*http:ListenerConfiguration` (`commons.bal:110–114`); the real defaults
(`http` 2.16.6 `http_service_endpoint.bal:156–168`) are `host = "0.0.0.0"`, `timeout = DEFAULT_LISTENER_TIMEOUT`
= 60 (`http_constants.bal:36`), `http2InitialWindowSize = 65535`, `minIdleTimeInStaleState = 300`,
`timeBetweenStaleEviction = 30`. The extractor substituted type zero-values. Correct in the render:
`httpVersion = "2.0"`, `gracefulStopTimeout = 0.0d` (`DEFAULT_GRACEFULSTOP_TIMEOUT = 0`,
`http_constants.bal:40`), `gracefulShutdownPeriod = 20` (`commons.bal:113`). These bad defaults already
existed in the **old JSON** (parameter arrays are byte-identical on both sides); `old` simply never
rendered them. So this is a pre-existing extractor defect newly made visible, not a `new` regression.

**5.5 Included-record parameter rendered as a trailing required positional.**
Source is `init(int|http:Listener listenTo, *ListenerConfiguration config)`. `new` expands the 14
`ListenerConfiguration` fields as defaulted params **and then appends** `ListenerConfiguration config`
with no default and no `*`, producing a signature that is not valid Ballerina and that lists the same
configuration twice. The identical pattern already exists in `old` for `DiscoveryService.init` and
`SubscriptionClient.init` (`… http:CircuitBreakerConfig circuitBreaker = {}, ClientConfiguration config)`),
so the behaviour is shared; only its application to `Listener` is new.

**5.6 The service listener expression is a non-compiling placeholder.**
new:514 — `service websub:SubscriberService on new websub:Listener(int|http:Listener listenTo, websub:ListenerConfiguration config = {})`
puts type descriptors in argument position. Additionally, per `ListenerInitAnalysisTask.verifyListenerArgType`
(:115–130) the two-argument form is only accepted when the first argument is an `int` — passing an
`http:Listener` plus a config triggers `WEBSUB_109` (ERROR). The JSON's `listenTo` default (`"0"`) was
also dropped by the renderer. Style note: this section and the annotation section use `websub:`-qualified
names while the rest of the file uses unqualified names.

## 6. Coverage gaps vs. the library

Public symbols exported by the default (and only) module `websub` that appear in **neither** render —
6, all module-level `public final` variables (`commons.bal:159–174`):

| Symbol | Source |
|---|---|
| `ACKNOWLEDGEMENT` | commons.bal:159 |
| `SUBSCRIPTION_VERIFICATION_SUCCESS` | commons.bal:162 |
| `SUBSCRIPTION_VERIFICATION_ERROR` | commons.bal:165 |
| `UNSUBSCRIPTION_VERIFICATION_SUCCESS` | commons.bal:168 |
| `UNSUBSCRIPTION_VERIFICATION_ERROR` | commons.bal:171 |
| `SUBSCRIPTION_DELETED_ERROR` | commons.bal:174 |

Verified by `grep -c` restricted to lines after the README (`awk 'NR>198'`): 0 hits in both renders.
They occur only inside README code samples. Neither JSON has any `constants`/`variables` array, so this is
an extractor-level gap shared by both sides. It matters here because the README's own examples return
`websub:ACKNOWLEDGEMENT` and `websub:SUBSCRIPTION_VERIFICATION_SUCCESS`, so the render tells a model to
use symbols it never declares.

`SubscriberService` renders as an empty `class SubscriberService { }` on both sides (source:
`subscriber_service.bal:17` — `public type SubscriberService distinct service object { }`, whose methods
are commented out in the source). In `new` this is compensated by the `// --- Service ---` block.

No submodule-only API: the package exports one module (`package.json` `"export": ["websub"]`,
`modules/` contains only `websub`), so the shared `getDefaultModule()` limitation costs nothing here.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.websub.WebSubCompilerPlugin`
(`compiler-plugin/libs/websub-compiler-plugin-2.15.0.jar`). It contributes:

- **Validations** (`WebSubCodeAnalyzer` → `ServiceAnalysisTask`, `ServiceDeclarationValidator`,
  `ListenerInitAnalysisTask`, `CheckExpAnalysisTask`): `WEBSUB_100`(W, checkpanic), `WEBSUB_101`(E,
  missing `@SubscriberServiceConfig`), `WEBSUB_102`(E, method must be `remote`), `WEBSUB_103`(E,
  `onEventNotification` required), `WEBSUB_104`(E, disallowed method), `WEBSUB_105`/`106`(E, parameter
  types), `WEBSUB_107`/`108`(E, return types), `WEBSUB_109`(E, listener args).
- **Code action** `MandatoryFunctionsGenerationAction` (`WEBSUB_202`, INTERNAL) which inserts the missing
  mandatory service methods.
- **Code modifier** `WebSubCodeModifier` → `WebSubServiceInfoGeneratorTask` / `ServiceMetaInfoUpdaterTask`
  / `service/path/*`, which generates the unique service path and injects it into the
  `SubscriberServiceConfiguration.servicePath` field at compile time (`WEBSUB_200`, `WEBSUB_201`).

Render coverage: `new`'s service section reproduces the method allow-list, the parameter types, the
return types and the required/optional split faithfully (§3) — this is exactly the plugin-implied
contract that `old` omitted entirely. The one plugin-implied fact `new` gets **wrong** is the mandatory
annotation (§5.3). `servicePath` is surfaced as a settable field in `SubscriberServiceConfiguration` on
both sides (line 256), but its doc string does say "auto-generated at the compile-time", so it is
adequately flagged.

## 8. Other considerations

- Version is stable (2.x), not deprecated, GraalVM-compatible, built with Ballerina 2201.12.0.
- Size/token impact: +94 lines (+21%). Cheap for the information gained (10 error types, a 48-line
  `Listener` class, a 26-line service contract, the annotation).
- 199 of 539 lines (37%) are README passthrough — identical on both sides.
- Pre-existing shared cosmetic defect: 3 doc-comment continuation lines lose their `#` prefix
  (`or a tuple …`, `found.` ×2), leaving bare text inside a declaration block. Present in both files.
- `public` is stripped from every type/class/function in both renders; only the newly added annotation
  line carries `public`. Inconsistent, but harmless for a reference document.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 445 / 539 |
| `grep -c '^// Unknown type:'` | old 11, new 0 |
| `grep -c 'ballerina/websub:2.15.0:'` (via diff) | old 3, new 0 |
| `grep -n '^// --- ' old` | 7,198,200,396,428 |
| `grep -n '^// --- ' new` | 7,198,200,458,490,509,536 |
| `diff old new \| grep '^<'` | 16 lines, all stubs/blank/version-qualified (listed §4) |
| `diff old new \| grep -c '^>'` | 110 |
| `diff <(sed -n 1,199p old) <(sed -n 1,199p new)` | empty (README identical) |
| sorted declaration-header set-difference | +13, −0 |
| `git ls-remote --tags …module-ballerina-websub` → `git clone --depth 1 --branch v2.15.0` | tag exists, cloned |
| `diff -q src/ballerina/<f>.bal bala/modules/websub/<f>.bal` ×8 | all identical |
| `ls bala/…/modules` | only `websub` |
| `cat bala/…/package.json` | `"export": ["websub"]`, ballerina 2201.12.0, graalvmCompatible |
| `curl api.central.ballerina.io/…/ballerina/websub/2.15.0` | 1 module, `deprecated: null` |
| `grep -nE '^public ' bala/modules/websub/*.bal` | 34 public symbols enumerated (basis for §6) |
| `awk 'NR>198' <render> \| grep -c ACKNOWLEDGEMENT` etc. | 0 in both for all 6 constants |
| `grep -n CommonResponse new` | 10 hits, all `error<CommonResponse>`; 0 in old; no definition |
| `errors.bal:18–45` | 2 × `distinct error<CommonResponse>`, 8 × `distinct Error` |
| `ServiceDeclarationValidator.java:65–99` | allowedMethods / param types / return types match render |
| `ServiceDeclarationValidator.java:134–140` | `onEventNotification` is the only required method |
| `ServiceDeclarationValidator.java:123–132` + `WebSubDiagnosticCodes.java:29–31` | `WEBSUB_101` = ERROR, annotation mandatory |
| `ListenerInitAnalysisTask.java:115–130` | 2-arg listener only valid when first arg is `int` (`WEBSUB_109`) |
| `http/2.16.6 http_service_endpoint.bal:156–168`, `http_constants.bal:36,40` | real listener-config defaults (§5.4) |
| Python `difflib` over both JSONs | only services/annotations/baseType/`"type":"Class"`/3 unqualified names differ |
| Python compare of `Listener.init` parameters in both JSONs | byte-identical |

## 10. Caveats and unverified items

- The renders were not compiled. Claims of "non-compiling" (§5.1, §5.5, §5.6) are read from the Ballerina
  grammar and the compiler-plugin rules, not from a `bal build` run.
- I did not decompile `websub-compiler-plugin-2.15.0.jar` in the bala; plugin behaviour is taken from the
  `v2.15.0` GitHub sources, which were shown byte-identical to the bala for all `.bal` files but not
  verified byte-for-byte against the shipped jar.
- I did not re-run the two-stage pipeline; the two JSONs and two `.bal.txt` files were taken as given.
- `http` defaults in §5.4 were read from the locally installed `ballerina/http` **2.16.6** bala. websub
  2.15.0's `Dependencies`/`dependency-graph.json` resolution to that exact http version was not
  independently confirmed; the defaults quoted have been stable across recent http 2.x releases but the
  precise numbers are only verified for 2.16.6.
- Whether the `presence: "optional"` annotation flag (§5.3) originates in the extractor's
  trigger-metadata model or in `CopilotLibraryManager` itself was not traced — I only observed it in the
  produced JSON.

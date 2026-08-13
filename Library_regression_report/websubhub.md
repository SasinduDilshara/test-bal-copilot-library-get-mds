# ballerina/websubhub 1.16.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/websubhub` |
| Pinned version | `1.16.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-websubhub |
| Tag reviewed | `v1.16.0` |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/websubhub/1.16.0/java21` |
| Old render | `512` lines |
| New render | `587` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. All 18 `// Unknown type:` placeholders in
`old` are replaced by real definitions (13 error types, 3 status classes, `Controller`, `Listener`
with all 6 methods), the `ServiceConfig` annotation section appears for the first time, and the two
client `init` signatures lose the `ballerina/websubhub:1.16.0:Error?` version-qualified return in
favour of `Error?`. Nothing present in `old` is missing, truncated, or degraded in `new`: the
mechanical diff has 0 removed declarations, and the only removed lines are the placeholder comments
and the two version-qualified refs. The README block is byte-identical on both sides and identical to
the bala `docs/README.md`.

`new` does carry accuracy losses of its own for the newly emitted material (`distinct` dropped from
the whole error hierarchy, `readonly` classes emitted with empty bodies, `Listener.init` expanded
from an included-record parameter with fabricated defaults), but these are places where `old` emitted
nothing at all, so they are not regressions.

## 2. Change inventory

Line counts (`wc -l`): old `512`, new `587`. Mechanical diff: 96 lines added, 21 removed, 4 hunks.

Declaration counts, body only (everything after `// --- END README ---`, line 124):

| kind | old | new |
|---|---|---|
| `type ...` | 21 | 34 |
| `class ...` | 1 | 6 |
| `client class ...` | 2 | 2 |
| `enum ...` | 1 | 1 |
| `const ...` | 5 | 5 |
| `public annotation ...` | 0 | 1 |
| class/client methods (`    function` / `    remote function`) | 7 | 15 |
| `// Unknown type:` placeholders | 18 | 0 |
| version-qualified type refs (`ballerina/websubhub:1.16.0:Error`) | 2 | 0 |
| section markers `// --- ` | 4 | 5 |

Added in `new` (25 declarations, 0 removed):

- **Error types (13)** — `Error`, `ServiceExecutionError`, `TopicRegistrationError`,
  `TopicDeregistrationError`, `BadSubscriptionError`, `InternalSubscriptionError`,
  `SubscriptionDeniedError`, `BadUnsubscriptionError`, `InternalUnsubscriptionError`,
  `UnsubscriptionDeniedError`, `UpdateMessageError`, `SubscriptionDeletedError`,
  `ContentDeliveryError` (new lines 432–469), each with its doc comment.
- **Classes (5)** — `StatusOK` (231), `StatusTemporaryRedirect` (477), `StatusPermanentRedirect`
  (481), `Controller` (484), `Listener` (497).
- **Methods (8)** — `Controller.init`, `Controller.markAsVerified`, `Listener.init`,
  `Listener.attach`, `Listener.detach`, `Listener.'start`, `Listener.gracefulStop`,
  `Listener.immediateStop`.
- **Annotation section (1)** — `// --- Annotations ---` + `public annotation ServiceConfiguration
  ServiceConfig on service;` (new line 584–587).

Modified in `new`:

- `HubClient.init` (new 539) and `PublisherClient.init` (551): return type
  `ballerina/websubhub:1.16.0:Error?` → `Error?`. Parameters otherwise byte-identical.

JSON-level: both sides have exactly 46 `typeDefs`, the same 46 names, 2 clients, 0 functions,
0 services. 18 typeDefs differ, all by gaining a `type` kind tag (`"type":"Error"` / `"Class"`), and
the 13 error entries additionally gain `"baseType":"error<CommonResponse>"`. `annotations`: 0 in old,
1 in new. So the extractor already carried `Controller`/`Listener` function lists in `old` — the old
*renderer* discarded them; spec v2 emits them.

## 3. Correctness against library source

The bala `modules/websubhub/*.bal` is byte-identical to the `v1.16.0` clone's `ballerina/*.bal`
(`diff -q` over all 10 relevant files: no output). `package.json` reports
`organization=ballerina, name=websubhub, version=1.16.0`; `Ballerina.toml` line 4 `version = "1.16.0"`.
Pin confirmed on both sides.

Spot checks of the newly added material:

| render | library source | verdict |
|---|---|---|
| `type Error error<CommonResponse>` (432) | `errors.bal:18` `public type Error distinct error<CommonResponse>;` | exists; `distinct`/`public` dropped |
| 12 subtypes (435–469) | `errors.bal:21–55` `public type X distinct Error;` | all 12 exist, doc text matches verbatim; rendered as `error<CommonResponse>` rather than `distinct Error` |
| `class StatusOK {}` (231) | `commons.bal:90` `public readonly class StatusOK { *Status; public http:STATUS_OK code = http:STATUS_OK; }` | exists; body/`readonly` lost |
| `class StatusTemporaryRedirect {}` / `StatusPermanentRedirect {}` (477, 481) | `commons.bal:98`, `commons.bal:105` | exist; same loss |
| `Controller.markAsVerified(Subscription\|Unsubscription) returns Error\|()` (494) | `hub_controller.bal:32` `public isolated function markAsVerified(Subscription\|Unsubscription subscription) returns Error?` | signature correct (`Error\|()` ≡ `Error?`); `isolated` dropped |
| `Controller.init(boolean autoVerifySubscriptionIntent)` (485) | `hub_controller.bal:23` | correct |
| `Listener.attach(Service 'service, string[]\|string\|() name = ())` (500) | `hub_listener.bal:60` | correct |
| `Listener.detach(Service s)`, `'start()`, `gracefulStop()`, `immediateStop()` | `hub_listener.bal:104, 117, 130, 141` | correct, all return `Error?` |
| `Listener.init(int\|http:Listener listenTo, …, ListenerConfiguration config) returns Error?` (498) | `hub_listener.bal:35` `init(int\|http:Listener listenTo, *ListenerConfiguration config) returns Error?` | see §5.3 — included-record param expanded with wrong defaults |
| `public annotation ServiceConfiguration ServiceConfig on service;` (587) | `annotation.bal:29` — identical text | correct |
| Doc comments on `Listener` and its methods | `hub_listener.bal:27–34, 52–59, 97–103, 111–116, 124–129, 137–…` | reproduced verbatim including the ```ballerina fenced examples |

`class Service {}` (472) is unchanged from `old` and is structurally accurate: `hub_service.bal:18`
declares `public type Service distinct service object { … }` whose every remote method is commented
out (lines 22–46), so the type genuinely has no members.

## 4. Regressions

**None found.**

Checked:

- `diff -u old new` in full (117 changed lines): every `-` line is either a `// Unknown type: X` placeholder or one of the two `init` lines re-emitted with the version qualifier removed. No declaration, parameter, default, return type, or doc line is dropped.
- Declaration-name sets: all 45 public named declarations in the bala default module (`grep -hoE '^public (isolated |readonly )?(function|type|class|const|annotation|enum) +NAME'`) appear in the `new` body; the only one absent from the `old` body is `ServiceConfig`.
- README: `old` README block == `new` README block == bala `docs/README.md` (exact string compare, 5490 chars, all three equal).
- JSON: `typeDefs` name set identical (46/46); no entry lost a field in `new` — the 18 diffs are all field *additions* (`type`, `baseType`).
- Client sections: `HubClient.notifyContentDistribution` and all four `PublisherClient` remote methods present with identical signatures and docs on both sides.

## 5. Issues in `new` (independent of `old`)

1. **`distinct` and the error hierarchy are erased.** Source (`errors.bal:21–55`) defines 12 types as
   `distinct Error`; `new` renders each as `type X error<CommonResponse>` (432–469). The JSON is the
   origin: `"baseType":"error<CommonResponse>"` for every one, including `Error` itself. An LLM
   reading this cannot tell that `TopicRegistrationError` is a subtype of `Error`, nor that the
   types are mutually non-assignable — it would plausibly emit `Error e = ...; return e;` where a
   `TopicRegistrationError` is required. This is the single most consequential inaccuracy in `new`.
2. **`readonly` classes render as empty bodies.** `StatusOK`/`StatusTemporaryRedirect`/
   `StatusPermanentRedirect` (`commons.bal:90, 98, 105`) each include `*Status` and a `public …code`
   field; `new` emits `class StatusOK {\n}` with `"functions": []` and no fields. `readonly` is
   dropped. Harmless for construction (they are only used as `ContentDistributionSuccess.status`),
   but `.code` is invisible.
3. **`Listener.init` expands an included-record parameter with fabricated defaults.** Source is
   `init(int|http:Listener listenTo, *ListenerConfiguration config)` where `ListenerConfiguration`
   is `record {| *http:ListenerConfiguration; |}` (`commons.bal:380–382`). `new` (line 498) flattens
   it to 12 positional defaulted parameters *plus* a trailing required `ListenerConfiguration config`.
   Comparing with `http` 2.16.3 `http_service_endpoint.bal:156–168`:
   | param | render default | actual default | |
   |---|---|---|---|
   | `host` | `""` | `"0.0.0.0"` | wrong |
   | `httpVersion` | `"2.0"` | `HTTP_2_0` | ok |
   | `timeout` | `0.0d` | `DEFAULT_LISTENER_TIMEOUT` = `60` (`http_constants.bal:36`) | wrong |
   | `gracefulStopTimeout` | `0.0d` | `DEFAULT_GRACEFULSTOP_TIMEOUT` = `0` (`http_constants.bal:40`) | ok |
   | `http2InitialWindowSize` | `0` | `65535` | wrong |
   | `minIdleTimeInStaleState` | `0.0d` | `300` | wrong |
   | `timeBetweenStaleEviction` | `0.0d` | `30` | wrong |
   A required parameter after defaulted ones is also not valid Ballerina. Note this is the *same*
   flattening the pipeline already applied to `HubClient.init`/`PublisherClient.init` in `old`, so it
   is an inherited pipeline behaviour, not new logic — it simply now also affects `Listener`.
4. **Qualifiers dropped.** `public` appears only on the annotation; every `type`/`class`/`const` is
   rendered bare. `isolated` is dropped from `Controller` (source `public isolated class Controller`,
   `hub_controller.bal:18`) and from all `Listener`/`Controller` methods.
5. **`Controller` has no doc comment** (`new` 484) although `hub_controller.bal:17` carries
   `# Component which can use to change the default subcription intent verification flow.` The JSON
   has `"description": ""` for `Controller` on **both** sides, so this is an extractor gap, present
   identically in `old`.
6. **Pre-existing record-shape inaccuracies, unchanged between sides** (listed for completeness — all
   byte-identical in `old`):
   - Fields with defaults render as optional: `TopicRegistration.hubMode?` (source
     `commons.bal:155` `string hubMode = MODE_REGISTER;`, i.e. required-with-default `"register"`),
     same for `TopicDeregistration.hubMode`, `VerifiedSubscription.verificationSuccess`,
     `ContentDistributionSuccess.status`, and all of `CommonResponse`.
   - Record inclusions are flattened without marking them (`ContentDistributionSuccess` shows
     `*CommonResponse`'s four fields inline and un-documented; same for `VerifiedSubscription`,
     `VerifiedUnsubscription`).
   - A wrapped doc line loses its `#` continuation: inside `ContentDistributionSuccess` the text
     `this is a successful response` sits at column 0 between record fields, breaking the comment
     block.
   - `enum MessageType` renders members as `PUBLISH, EVENT`; source order is `EVENT, PUBLISH`
     (`commons.bal:217–220`). Semantically irrelevant, cosmetically wrong.

## 6. Coverage gaps vs. the library

The bala has exactly one module — `modules/websubhub` — so there is no submodule API and no
submodule-only gap.

Absent from **both** renders (14 items): every `public final` module-level value in `commons.bal`
lines 302–349 —
`TOPIC_REGISTRATION_SUCCESS`, `TOPIC_REGISTRATION_ERROR`, `TOPIC_DEREGISTRATION_SUCCESS`,
`TOPIC_DEREGISTRATION_ERROR`, `ACKNOWLEDGEMENT`, `UPDATE_MESSAGE_ERROR`, `SUBSCRIPTION_ACCEPTED`,
`BAD_SUBSCRIPTION_ERROR`, `INTERNAL_SUBSCRIPTION_ERROR`, `SUBSCRIPTION_DENIED_ERROR`,
`UNSUBSCRIPTION_ACCEPTED`, `BAD_UNSUBSCRIPTION_ERROR`, `INTERNAL_UNSUBSCRIPTION_ERROR`,
`UNSUBSCRIPTION_DENIED_ERROR`.
Verified by grepping each name in the render: only `TOPIC_REGISTRATION_SUCCESS` and
`TOPIC_REGISTRATION_ERROR` occur at all, and only inside the README code sample (render lines
95–99), never as declarations. This matters: these constants are the idiomatic return values of hub
remote methods and the README itself tells the reader to `return websubhub:TOPIC_REGISTRATION_ERROR`,
yet the render never declares them. Shared gap — not caused by spec v2.

The `Status` object type (`commons.bal:83`) is module-private and correctly absent.

## 7. Compiler plugin

`has_plugin: true`, confirmed: `compiler-plugin/compiler-plugin.json` declares
`plugin_class: io.ballerina.stdlib.websubhub.WebSubHubCompilerPlugin` with
`compiler-plugin/libs/websubhub-compiler-plugin-1.16.0.jar`. Source: 8 classes under
`compiler-plugin/src/main/java/io/ballerina/stdlib/websubhub/`.

It contributes **validation only** — no code actions, no code generation, no annotations
(`WebSubHubCodeAnalyzer.java:33–41` registers three syntax-node analysis tasks: `CheckExpAnalysisTask`
on check-expressions, `ListenerInitAnalysisTask` on new-expressions, `ServiceAnalysisTask` on service
declarations). Nine diagnostics `WEBSUBHUB_100`–`WEBSUBHUB_108`
(`WebSubHubDiagnosticCodes.java:27–44`).

The material gap: `ServiceDeclarationValidator.java:50–108` is where the **entire `websubhub:Service`
contract lives** — 9 allowed remote methods (`onRegisterTopic`, `onDeregisterTopic`,
`onUpdateMessage`, `onSubscription`, `onSubscriptionValidation`, `onSubscriptionIntentVerified`,
`onUnsubscription`, `onUnsubscriptionValidation`, `onUnsubscriptionIntentVerified`), of which 5 are
**required** (`onRegisterTopic`, `onDeregisterTopic`, `onUpdateMessage`,
`onSubscriptionIntentVerified`, `onUnsubscriptionIntentVerified`), plus the allowed parameter types
and allowed return types per method. Neither render carries any of this as structured content —
`class Service {}` is empty in both, and `services` is `0` in both JSONs. The information survives
only as prose/examples in the README block (the sample service at render lines 90–104 and the
error-meaning table at 111–122). An LLM generating a hub service from this render has no
machine-readable signal that `onRegisterTopic` must be `remote`, must take
`websubhub:TopicRegistration`, and must return
`TopicRegistrationSuccess|TopicRegistrationError`. This is a shared gap, identical on both sides, and
is arguably the largest single deficiency in the render for this library — but spec v2 neither
caused nor worsened it.

## 8. Other considerations

- Stable release (1.16.0, `>= 1.0`), not deprecated, built with Ballerina `2201.12.0` per
  `package.json`; renders were produced under distribution `2201.13.4`.
- Size: 512 → 587 lines (+14.6%). Token cost increase is modest and buys 18 previously-opaque types.
- Neither render is compilable Ballerina (stub bodies, defaulted-then-required params, `class` used
  for `distinct service object` and for `type X error<...>` companions). That is the format's design,
  not a defect introduced here.
- The two `// Special Agent Note:` trailer comments on `HubClient.init`/`PublisherClient.init` are
  preserved verbatim, and a third correctly appears on the new `Listener.init` naming the six
  `ballerina/http` types it references.
- Removal of the `ballerina/websubhub:1.16.0:Error?` version qualifier is a genuine quality win: the
  old form is not valid Ballerina and would confuse type resolution.

## 9. Evidence log

| check | result |
|---|---|
| `wc -l old/… new/…` | 512 / 587 |
| `grep -c '^// Unknown type:'` old / new | 18 / 0 |
| `grep -n '^// Unknown type:' old` | lines 229, 428–464 (18 names) |
| `grep -n '^// --- ' old / new` | 4 markers / 5 (new adds `// --- Annotations ---` at 584) |
| `diff -u old new` | 4 hunks, 96 added / 21 removed; every removal is a placeholder or a version-qualified `init` line |
| `git clone --depth 1 --branch v1.16.0 …` | tag exists, clone succeeded |
| `diff -q bala/modules/websubhub/*.bal  clone/ballerina/*.bal` (10 files) | no differences |
| `package.json` | `organization=ballerina, name=websubhub, version=1.16.0, ballerina_version=2201.12.0` |
| `ls bala/…/modules/` | single module `websubhub` (default) |
| Python compare of both JSONs | typeDefs 46 == 46, names identical; 18 entries changed, all field-additions (`type`, `baseType`); annotations 0 → 1; clients 2 == 2; functions 0 == 0; services 0 == 0 |
| README exact compare (render old, render new, bala `docs/README.md`) | all three equal, 5490 chars |
| `errors.bal:17–55` | 1 + 12 error types, all `distinct`, docs match render text |
| `commons.bal:83–114` | `Status` (private), 3 `public readonly class` with `*Status` + `code` field |
| `commons.bal:380–382` | `ListenerConfiguration record {| *http:ListenerConfiguration; |}` |
| `commons.bal:302–349` | 14 `public final` module-level values |
| grep of those 14 names in `new` render | only 2 occur, both inside the README sample; 0 declarations |
| `hub_listener.bal:21–141` | `Listener` with `init` + 5 public methods + private `retrieveHubUrl`; all 6 public rendered, private correctly omitted |
| `hub_controller.bal:17–52` | `public isolated class Controller`; `init`, `markAsVerified` public, `skipSubscriptionVerification` private — the private one is correctly omitted from the render |
| `hub_service.bal:18–48` | `Service` has zero live members — empty `class Service {}` is accurate |
| `annotation.bal:22–29` | `ServiceConfiguration` record + `ServiceConfig` annotation; both in `new` |
| `http/2.16.3 http_service_endpoint.bal:156–168`, `http_constants.bal:36,40` | actual `ListenerConfiguration` defaults used for the §5.3 table |
| declaration-set check: 45 public names vs render bodies | all 45 present in `new` body; only `ServiceConfig` absent from `old` body |
| `compiler-plugin/compiler-plugin.json`, `WebSubHubCodeAnalyzer.java:33–41`, `WebSubHubDiagnosticCodes.java:27–44`, `ServiceDeclarationValidator.java:50–108` | 3 analysis tasks, 9 diagnostics, service contract (9 methods, 5 required) |
| `OLD_AND_NEW_DIFFS/websubhub_diff.md` | its figures (512/587, 96/21, 18→0, 2→0, 25 added / 0 removed) all reproduced independently |

## 10. Caveats and unverified items

- The compiler-plugin behaviour was read from the `v1.16.0` Java source in the clone; the shipped
  `websubhub-compiler-plugin-1.16.0.jar` in the bala was **not** decompiled to confirm byte-level
  agreement. The clone is at the exact tag and the `.bal` sources matched the bala byte-for-byte, so
  divergence is unlikely but formally unverified.
- I did not re-run the two-stage render pipeline; the analysis compares the committed renders and
  JSONs against the library, taking the JSON as an accurate record of what the extractor produced.
- The `http` defaults in §5.3 were read from `ballerina/http` **2.16.3** (distribution 2201.13.4) and
  cross-checked against **2.16.6** (central cache) — the 13 `ListenerConfiguration` field defaults and
  both timeout constants are identical in the two. The bala's `dependency-graph.json` and the clone's
  `Dependencies.toml` both pin `http 2.14.9`, which is **not** present in any local repository, so I
  could not read that exact version's defaults; the resolver must have used 2.16.3 or 2.16.6. The
  fields in question have been stable across both, but 2.14.9 itself is unverified.
- Whether a required parameter following defaulted parameters causes a *practical* problem for the
  consuming LLM is a judgement, not a measurement.

# ballerina/websocket 2.15.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/websocket` |
| Pinned version | `2.15.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-websocket |
| Tag reviewed | `v2.15.5` (clone HEAD `750a564ee40228cea76cabb4637fc95b38a73fa2`, equals `refs/tags/v2.15.5^{}`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/websocket/2.15.5/java21` |
| Old render | 831 lines (31,777 bytes) |
| New render | 988 lines (40,937 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. Nothing that `old` rendered correctly was
dropped, truncated or made less accurate. The 19 `// Unknown type:` placeholders in `old` become
real definitions (16 error types, the `Listener` class with all 6 of its methods, and the two
close-frame marker classes), all 31 version-qualified type references (`ballerina/websocket:2.15.5:X`,
`ballerina/http:2.16.6:X`, `ballerina/crypto:2.12.1:X`) collapse to plain/prefixed names, two new
sections (`Service`, `Annotations`) appear, and 16 client/caller methods that `old` wrongly labelled
`remote` are corrected to plain methods — matching the published source.

The only behavioural change that *looks* like a loss (`remote function` → `function` on 16 methods)
is a correctness fix: those methods are declared `public isolated function` in the library, not
`remote`. Verified against `websocket_caller.bal:126-177` and `websocket_sync_client.bal:134-194`.

## 2. Change inventory

Counts from `diff -u old new` (12 hunks, 181 added lines, 45 removed lines) and from declaration-set
comparison (`grep -oE '^\s*(public )?(remote )?(isolated )?(function|type|class|...)'`, sorted, `comm`).

| Signal | old | new |
|---|---|---|
| Total lines | 831 | 988 |
| `// Unknown type:` placeholders | 19 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 31 | 0 |
| `// --- section ---` markers | 5 (README, END README, Types, Client, Functions) | 7 (+ Service, + Annotations) |
| Doc-comment lines (`^\s*#`) | 178 | 262 |
| JSON `typeDefs` | 63 | 63 |
| JSON `clients` / `functions` | 2 / 2 | 2 / 2 |
| JSON `services` | 0 | 2 (`Service`, `UpgradeService`) |
| JSON `annotations` | 0 | 2 (`ServiceConfig`, `DispatcherConfig`) |

**Declarations removed: 0.** `comm -23 decls_old decls_new` yields only the 16 `remote function` →
`function` renames listed below; no name disappears.

**Declarations added (36 top-level/member declarations):**

| Kind | Count | Names |
|---|---|---|
| Error type defs | 16 | `Error`, `InvalidHandshakeError`, `PayloadTooLargeError`, `CorruptedFrameError`, `ConnectionError`, `ConnectionClosureError`, `InvalidContinuationFrameError`, `UpgradeError`, `HandshakeTimedOut`, `ReadTimedOutError`, `AuthError`, `AuthnError`, `AuthzError`, `SslError`, `PayloadBindingError`, `PayloadValidationError` |
| Classes | 3 | `Listener`, `CustomCloseFrameType`, `PredefinedCloseFrameType` |
| `Listener` methods | 6 | `init`, `'start`, `gracefulStop`, `immediateStop`, `attach`, `detach` |
| Service templates | 2 | `service websocket:UpgradeService /basePath on new websocket:Listener(...)` (with its `resource function get`), `service class ServiceImpl { *websocket:Service; ... }` |
| Service remote handlers (inside `ServiceImpl`) | 9 | `onOpen`, `onMessage`, `onTextMessage`, `onBinaryMessage`, `onPing`, `onPong`, `onIdleTimeout`, `onClose`, `onError` |
| Annotations | 2 | `ServiceConfig` (on service), `DispatcherConfig` (on function) |

**Declarations modified (not removed):**

* 16 methods lost the `remote` qualifier — `Caller`: `setAttribute`, `getAttribute`, `removeAttribute`,
  `getConnectionId`, `getNegotiatedSubProtocol`, `isSecure`, `isOpen` (7); `Client`: the same 7 plus
  `initEndpoint` and `getHttpResponse` (9). Correct in `new` (see §3).
* 4 union type defs de-qualified: `ListenerAuthConfig`, `OAuth2GrantConfig`, `ClientAuthConfig`,
  `CloseFrame`.
* 5 inline anonymous record fields in `ListenerSecureSocket` / `ClientSecureSocket` de-qualified
  (`ballerina/http:2.16.6:Protocol` → `http:Protocol`, etc.).
* `Client.init` return type `ballerina/websocket:2.15.5:Error?` → `Error?`.
* `remote function` count in the code body: 28 (old, all in `Caller`/`Client`) → 21 (new, `Caller`/`Client`)
  + 9 in the new `ServiceImpl` template + 2 commented shape templates.

**Unchanged:** README block (lines 1–178) is byte-identical; all 34 `Record` typeDefs, 4 `Union`,
3 `Constant` (`AUTH_HEADER`, `AUTH_SCHEME_BASIC`, `AUTH_SCHEME_BEARER`), both module functions
(`authenticateResource`, `addCookies`) and both client classes are present on both sides.

## 3. Correctness against library source

Checked against the bala (`.../modules/websocket/*.bal`, authoritative) and the v2.15.5 clone.

* **`remote` → plain method.** `websocket_caller.bal:126,136,146,155,162,170,177` and
  `websocket_sync_client.bal:62,134,144,154,163,170,177,185,194` declare these as
  `public isolated function`, **not** `remote`. `new` is right, `old` was wrong. The genuinely
  `remote` methods (`writeTextMessage`, `writeBinaryMessage`, `writeMessage`, `ping`, `pong`, `close`,
  `readTextMessage`, `readBinaryMessage`, `readMessage`) keep `remote` in `new` — verified against
  `websocket_caller.bal:36,45,54,67,76,90` and `websocket_sync_client.bal:72,81,89,98,113,201,208,216,225`.
* **16 error types.** All exist: `websocket_errors.bal` declares `public type <X> distinct Error;`
  (and `ConnectionClosureError distinct ConnectionError`, `InvalidContinuationFrameError distinct
  CorruptedFrameError`, `PayloadValidationError distinct PayloadBindingError`). Descriptions in the
  render match the source doc comments verbatim (JSON `description` fields are identical on both sides).
* **`CustomCloseFrameType` / `PredefinedCloseFrameType`.** Real: `close_frame_return_types.bal:17,20`
  `public readonly distinct class`. `new` renders them as empty `class` bodies — the classes genuinely
  have no members.
* **`Listener`.** `service_endpoint.bal:22` `public class Listener`, with
  `'start()` (32), `gracefulStop()` (40), `immediateStop()` (48),
  `attach(UpgradeService websocketService, string[]|string? name = ())` (58),
  `detach(UpgradeService websocketService)` (69),
  `init(int|http:Listener 'listener, *ListenerConfiguration config) returns Error?` (78).
  All 6 present in `new` with matching names, params and return types (the `init` expansion is
  discussed in §5). `old` rendered none of them despite the JSON carrying all 6
  (`old` JSON `typeDefs[Listener].functions` has 6 entries) — the loss was purely in the renderer.
* **Annotations.** `annotation.bal:46` `public annotation WSServiceConfig ServiceConfig on service;`
  and `:56` `public const annotation WsDispatcherConfig DispatcherConfig on function;`. `new` matches
  (it drops `const` on the latter — cosmetic).
* **Service section vs. the compiler plugin** (`compiler-plugin/src/main/java/io/ballerina/stdlib/websocket/plugin/`):
  * "the accessor must be one of `get`", one resource only — `PluginConstants.java:88`
    `INVALID_RESOURCE_ERROR("There should be only one 'get' resource for the service")`.
  * `http:Request` as the only resource parameter — `PluginConstants.java:90`
    `MORE_THAN_ONE_RESOURCE_PARAM_ERROR("There should be only http:Request as a parameter")`.
  * return `Service|UpgradeError` — `WebSocketUpgradeServiceValidator.java:146-170` +
    `PluginConstants.java:27,29`.
  * `onMessage` excludes `onTextMessage`/`onBinaryMessage` — `PluginConstants.java:80`
    `INVALID_REMOTE_FUNCTIONS("Cannot have '{0}' with 'onMessage' remote function")`.
  * Handler signatures match the plugin's own code-action templates exactly:
    `onOpen(websocket:Caller caller) returns websocket:Error?` (`OnOpenCodeTemplate.java:38`),
    `onClose(websocket:Caller caller, int statusCode, string reason)` (`OnCloseCodeTemplate.java:38`),
    `onPing/onPong(websocket:Caller caller, byte[] data)` (`OnPingCodeTemplate.java:38`, `OnPongCodeTemplate.java:38`),
    `onIdleTimeout(websocket:Caller caller)` (`OnIdleTimeoutCodeTemplate.java:38`),
    `onTextMessage(..., string text)` / `onBinaryMessage(..., byte[] data)` (`OnTextMessageCodeTemplate.java:38`, `OnBinaryMessageCodeTemplate.java:38`),
    `onError(websocket:Caller caller, websocket:Error err)` (`OnErrorCodeTemplate.java:38`; the render's
    plain `error err` is also accepted — `Utils.java:193-216` allows generic `error`).
  * dispatcher naming rule ("value is camel cased and prefixed with `on`") — exactly
    `WebSocketResourceDispatcher.java:579-594` (`createCustomRemoteFunction`: `"on " + value`, camel-cased).
  * "A binding failure closes the connection with status 1003" —
    `WebSocketResourceDispatcher.java:600` `webSocketConnection.terminateConnection(1003, ...)`.
  * `DispatcherConfig`/`dispatcherValue` override and duplicate detection —
    `PluginConstants.java:82-88` (`RE_DECLARED_REMOTE_FUNCTIONS`, `DUPLICATED_DISPATCHER_MAPPING_DISPATCHER_VALUE`,
    `INVALID_FUNCTION_ANNOTATION`).

  No invented symbol was found in the Service section.

## 4. Regressions

**None found.**

What was checked to conclude this:
* Declaration-set diff (`comm -23`) between the two renders: the only entries unique to `old` are the
  16 `remote function <name>` forms whose plain-method counterparts exist in `new`; zero names lost.
* JSON diff: `typeDefs` 63 on both sides, same names; `clients` 2, `functions` 2 on both; `new` only
  gains `services` (2) and `annotations` (2).
* README block compared line-for-line (`diff` shows no hunk before line 319) — identical, 178 lines.
* Doc-comment lines: 178 → 262 (no doc text removed; the 45 removed diff lines are the 19 `Unknown type`
  placeholders, the 16 `remote` renames, 5 de-qualified record-field lines, 4 de-qualified unions and
  1 de-qualified return type — each replaced by a superset).
* Public-symbol coverage (all 76 public symbols of the default module): 12 missing from `old`,
  10 from `new` — `new` is a superset of `old`.
* All `Special Agent Note:` cross-package annotations present in `old` are still present in `new`
  (`crypto:KeyStore`, `http:CertKey`, `http:Cookie`, `http:Response`, `crypto:TrustStore`).

## 5. Issues in `new` (independent of `old`)

New-only (they exist in `new` because `new` renders things `old` skipped entirely):

1. **`Listener` class doc is the `init` doc.** `new:694` emits
   `# Gets invoked during the module initialization to initialize the listener.` as the class doc.
   The real class doc (`service_endpoint.bal:19-21`, "This is used for creating WebSocket server
   endpoints…") appears in neither render (`grep -c "This is used for creating WebSocket server endpoints"`
   → 0 in both). Origin is the extractor, not the renderer: `old` JSON `typeDefs[Listener].description`
   already holds the `init` text, and `init` itself is then rendered doc-less.
2. **`Listener.init` signature is not valid Ballerina and invents a default.** `new:697`:
   `function init(int|http:Listener 'listener, string host = "0.0.0.0", ..., RequestLimitConfigs requestLimits = {}, ListenerConfiguration config) returns Error?`.
   The real signature is `init(int|http:Listener 'listener, *ListenerConfiguration config)`
   (`service_endpoint.bal:78`). The render expands the included-record fields *and* keeps a required
   `ListenerConfiguration config` parameter after defaulted ones. Also `ListenerSecureSocket secureSocket
   = {'key: {path: "", password: ""}}` is fabricated — `ListenerConfiguration.secureSocket` is optional
   with **no** default (`service_endpoint.bal:109`). (Same expansion pattern already existed in `old`
   for `Client.init`, so this is inherited renderer behaviour, newly visible on `Listener`.)
3. **Error subtype hierarchy flattened.** All 16 render as `type X error;`. The source declares them
   `distinct Error` (and three of them distinct sub-errors of other module errors). An LLM cannot tell
   from the render that e.g. `UpgradeError` is a `websocket:Error`, or that `ConnectionClosureError`
   narrows `ConnectionError`. The JSON carries only `baseType: "error"`, so the information is lost at
   extraction.
4. **`readonly distinct` dropped** on `class CustomCloseFrameType` / `class PredefinedCloseFrameType`
   (`close_frame_return_types.bal:17,20`). Code that writes `readonly CustomCloseFrameType 'type = …`
   in a `CloseFrame` record cannot be derived from the render.
5. **Ambiguous cross-package note.** `new:697` ends with
   `// Special Agent Note: Listener FROM ballerina/http package` on the line that *defines*
   `class Listener` in `websocket`; it refers to the `http:Listener` parameter but reads as if the
   class itself came from `http`.

Also present in `new` and identically in `old` (shared, pre-existing — not regressions):

6. **Malformed doc continuation lines**: 8 lines inside type bodies continue a doc comment without a
   leading `#` (e.g. `new:198-199`, `202-203` in `WSServiceConfig`) — identical count in both files.
7. **Record field defaults dropped**: `WSServiceConfig` renders `string[] subProtocols?; decimal
   idleTimeout?; int maxFrameSize?; boolean validation?; decimal connectionClosureTimeout?` although
   the source (`annotation.bal:34-43`) gives defaults `[]`, `0`, `65536`, `true`, `60` and those fields
   are not optional.
8. **Unqualified `Cloneable?`**: `Caller.getAttribute`/`removeAttribute` return `Cloneable?` while the
   parameter type is written `value:Cloneable` — the return type needs the `value:` prefix to resolve.
   Same in both renders (old:718,722 / new:761,765).
9. **`Service`, `UpgradeService`, `PingPongService` render as empty `class` bodies** (new:686, 691, 649)
   although they are `distinct service object` types (`websocket_types.bal:18,22,26`). `new` compensates
   for `Service`/`UpgradeService` via the Service section; `PingPongService` (used as
   `ClientConfiguration.pingPongHandler`) still gives no hint of `onPing`/`onPong`.
10. **`Client.init`** carries the same expansion/fabricated-default problem as item 2
    (`auth = {username: "", password: ""}` for an optional field) — byte-identical in both renders
    apart from the de-qualified return type.

## 6. Coverage gaps vs. the library

The bala contains a single module (`modules/websocket`), so there is **no submodule-only API** — the
`getDefaultModule()`-only extraction loses nothing here.

Of the 76 public symbols in the default module, **10 appear in neither render** — all of them
module-level `public final` values (the renderer/extractor emits `const` only, and these are `final`
variables, not constants):

`NORMAL_CLOSURE`, `GOING_AWAY`, `PROTOCOL_ERROR`, `UNSUPPORTED_DATA`, `INVALID_PAYLOAD`,
`POLICY_VIOLATION`, `MESSAGE_TOO_BIG`, `INTERNAL_SERVER_ERROR` (`close_frame_return_types.bal:96-127`,
`public final readonly & <X> <NAME> = {}`), plus `PREDEFINED_CLOSE_FRAME` and `CUSTOM_CLOSE_FRAME`
(`close_frame_return_types.bal:23-24`).

This matters in practice: the render shows `CloseFrame` records with a `readonly PredefinedCloseFrameType
'type` field but no way to obtain a value of that type, so an LLM cannot write a working
`return websocket:NORMAL_CLOSURE;` or a custom close frame. Shared gap — absent from both renders and
from both JSONs (`grep NORMAL_CLOSURE *.json` → 0 hits on both sides).

`old` additionally lacked `ServiceConfig` and `DispatcherConfig` (12 missing); `new` closes those two.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` registers
`io.ballerina.stdlib.websocket.plugin.WebSocketCompilerPlugin` (jars: `websocket-compiler-plugin-2.15.5`,
`websocket-native-2.15.5`, `http-native-2.15.6`).

It contributes (a) validation of the upgrade service (single `get` resource, `http:Request`-only
parameter, `Service|UpgradeError` return), (b) validation of every WebSocket service handler's
parameters and return types, including the `onMessage` vs `onTextMessage`/`onBinaryMessage` exclusion
and `DispatcherConfig` duplicate/misuse checks (24 diagnostics, `PluginConstants.java:60-116`), and
(c) 10 code-action templates that generate the handler skeletons.

Everything the plugin implies is now surfaced in `new`'s `Service` section, and the rendered
signatures line up with the plugin's own templates (§3). Two plugin-enforced rules are **not** in the
render: `DISPATCHER_STREAM_ID_WITHOUT_KEY` (`dispatcherStreamId` requires `dispatcherKey`,
`PluginConstants.java:113`) and `INVALID_CONNECTION_CLOSURE_TIMEOUT` (`:115`) — both are only
discoverable from the `WSServiceConfig` field docs, which the render does carry. `old` surfaced none
of this.

## 8. Other considerations

* Stable, non-deprecated release: `package.json` → `{organization: ballerina, name: websocket,
  version: 2.15.5, ballerina_version: 2201.13.0, template: false}`; Central keywords
  `ws, network, bi-directional, streaming, service, client`.
* Size/tokens: 831 → 988 lines, 31,777 → 40,937 bytes (+28.8% bytes). The extra weight is the Service
  section (~117 lines) and the 16 error definitions; both are high-value for generation, so the
  trade-off is favourable.
* Doc quality is good — descriptions come through verbatim from the source doc comments; the only
  defects are the 8 unprefixed continuation lines (§5.6), which are identical in `old`.
* `websocket` is one of the libraries where `old` was materially unusable for server-side codegen:
  it exposed no `Listener` API, no service shape and no annotations. `new` makes server-side
  generation possible for the first time.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags .../module-ballerina-websocket \| grep 2.15.` | `v2.15.5` → `750a564…` (peeled) |
| `git clone --depth 1 --branch v2.15.5`; `git rev-parse HEAD` | `750a564ee40228cea76cabb4637fc95b38a73fa2` — exact tag |
| `wc -l old new` | 831 / 988 |
| `wc -c old new` | 31777 / 40937 |
| `grep -c '^// Unknown type:'` | old 19, new 0 |
| `grep -oE '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` | old 31, new 0 |
| `grep -n '^// --- '` | old 5 markers, new 7 (adds Service, Annotations) |
| `diff -u old new \| wc -l` / `grep -c '^+[^+]'` / `grep -c '^-[^-]'` | 393 diff lines; +181 / −45 |
| `comm -23 decls_old decls_new` | only the 16 `remote function` renames |
| `comm -13 decls_old decls_new` | 36 new declarations (table in §2) |
| `grep -c '^\s*#'` | old 178, new 262 doc lines |
| `grep -c ';$'` | old 276, new 302 |
| Python JSON compare (`typeDefs/clients/functions/services/annotations`) | 63/2/2/0/0 (old) vs 63/2/2/2/2 (new) |
| Python JSON `Counter(typeDef.type)` | old `{Record:34, Error:16, Union:4, Constant:3, None:3, Class:3}`; new `{Record:34, Error:16, Class:6, Union:4, Constant:3}` |
| Python: `old.typeDefs[Listener].functions` | 6 entries present in `old` JSON but not rendered |
| Python: 76 public symbols vs both renders | missing in `new`: 10 (all `public final` values); missing in `old`: those 10 + `ServiceConfig`, `DispatcherConfig` |
| `websocket_caller.bal:126,136,146,155,162,170,177` | `public isolated function` — confirms `new`'s de-`remote` |
| `websocket_sync_client.bal:62,134,144,154,163,170,177,185,194` | `public isolated function` — same |
| `websocket_caller.bal:36,45,54,67,76,90`; `websocket_sync_client.bal:72,81,89,98,113,201,208,216,225` | genuinely `remote isolated function`; `remote` retained in `new` |
| `service_endpoint.bal:22,32,40,48,58,69,78` | `Listener` class + 6 methods, signatures match `new` |
| `service_endpoint.bal:106-114` | `ListenerConfiguration`: `secureSocket?` has no default → `new`'s `= {'key: …}` is fabricated |
| `service_endpoint.bal:19-21` | real class doc, absent from both renders |
| `close_frame_return_types.bal:17,20,23,24,96-127` | `readonly distinct class` ×2; 10 `public final` values |
| `websocket_types.bal:18,22,26` | `Service`/`UpgradeService`/`PingPongService` are `distinct service object` |
| `annotation.bal:34-43,45-46,51-56` | `WSServiceConfig` defaults; both annotations |
| `PluginConstants.java:27,29,60-116` | 24 diagnostics; upgrade-service and handler rules |
| `OnOpen/OnClose/OnPing/OnPong/OnIdleTimeout/OnText/OnBinary/OnMessage/OnErrorCodeTemplate.java:38` | handler signatures match the render |
| `Utils.java:98-170,193-240,290-345` | param/return validation; `error` accepted for `onError`; anydata-ish returns for data handlers |
| `WebSocketResourceDispatcher.java:579-594` | `createCustomRemoteFunction` = `"on " + camelCase(value)` |
| `WebSocketResourceDispatcher.java:600` | `terminateConnection(1003, …)` on binding error |
| `compiler-plugin/compiler-plugin.json` (bala) | plugin id/class/jars as quoted in §7 |
| `bala/.../package.json` | version 2.15.5, ballerina_version 2201.13.0, not a template |
| `ls bala/.../modules` | single module `websocket` → no submodule gap |
| `grep -c "This is used for creating WebSocket server endpoints"` | 0 in both renders |
| `grep -n 'Cloneable'` | unqualified `Cloneable?` return in both (old:718,722 / new:761,765) |
| `awk` count of unprefixed doc continuation lines | 8 in old, 8 in new |
| `OLD_AND_NEW_DIFFS/websocket_diff.md` claims (19→0 unknowns, 31→0 version refs, 0 removed, 35 added) | all reproduced independently; my declaration count is 36 (the diff's list omits the two service templates and counts the resource differently) |

## 10. Caveats and unverified items

* The two `service` blocks in the new render are deliberately non-compiling templates
  (`@websocket:ServiceConfig {...}`, `on new websocket:Listener(int|http:Listener 'listener, …)` with
  type names in the argument position, `<handlerName>` placeholders). I judged them as guidance text,
  not as code intended to compile; that judgement is mine, and I could not confirm it against a spec
  document for the "spec v2" renderer (no such document was provided).
* I did not execute the Ballerina compiler on either render, so "non-compiling" claims in §5
  (items 2, 6, 8) rest on reading the grammar/source, not on a compile run.
* The scratch clone directory already contained a `src/` checkout when I started; I verified its HEAD
  equals the peeled `v2.15.5` tag (`750a564…`) before using it, but I did not re-clone from scratch.
* The claim that both renders were produced at the same pinned version is taken from the brief plus
  the bala path (`.../websocket/2.15.5`); I found no contrary evidence (both JSONs report identical
  63 `typeDefs` with identical descriptions), but I did not re-run the two-stage pipeline myself.
* Return-type validation for custom dispatched handlers (`returns anydata|websocket:CloseFrame|error?`)
  was verified only for the `onTextMessage`/`onDataFunctions` path (`Utils.java:290-345`); I did not
  trace every branch of `isInvalidReturnType`, so the exact set of permitted `anydata` subtypes is
  unverified.

# ballerina/mqtt 1.4.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/mqtt` |
| Pinned version | `1.4.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-mqtt |
| Tag reviewed | `v1.4.1` (commit `0b183ea668bf7bd009ce03ea2982959d2bbbbb3d`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/mqtt/1.4.1/java21` |
| Old render | `308` lines |
| New render | `351` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly more accurate than `old` for this library. Two `// Unknown type:` placeholders in
`old` (`Error`, `Listener`) become real definitions in `new`, restoring the entire `mqtt:Listener`
class (6 methods, all with doc comments) that `old` dropped completely. Three version/module-qualified
type refs (`ballerina/mqtt:1.4.1:Protocol`, `ballerina/mqtt:1.4.1:Error?`,
`ballerina/mqtt:mqtt:Caller`) are gone. One bogus synthesized declaration in `old`
(`Caller.init() returns ballerina/mqtt:mqtt:Caller` — `Caller` has no `init` in the source) is
removed. The service section drops three invented `= ""` defaults and gains a parameter doc line.
Nothing present and correct in `old` is missing from `new`. README, module description, and all 18
type definitions carry over unchanged.

Both JSONs contain the same 18 typeDefs / 2 clients / 1 service / 0 functions / 0 annotations; the
`Listener` and `Error` improvements are driven by the extractor now tagging them (`"type": "Class"`,
`"baseType": "error<ErrorDetails>"`), which lets the renderer emit them instead of degrading.

## 2. Change inventory

Line counts: `old` 308, `new` 351 (`wc -l`). Unified diff: 50 lines added, 7 removed, 5 hunks
(`diff -u | grep -c '^+' / '^-'`), matching `OLD_AND_NEW_DIFFS/mqtt_diff.md`.

Signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 (`Error`, `Listener`) | 0 |
| `ballerina/mqtt:<ver>:` / `ballerina/mqtt:mqtt:` qualified refs | 3 | 0 |
| `// --- ` section markers | 5 | 5 |
| doc-comment lines (`^\s*#`) | 112 | 144 |

Declarations **added** in `new` (7 top-level/member declarations):

| Kind | Declaration |
|---|---|
| type | `type Error error<ErrorDetails>;` (replaces `// Unknown type: Error`) |
| class | `class Listener { ... }` (replaces `// Unknown type: Listener`) |
| method | `Listener.init(string, string, string\|string[]\|Subscription\|Subscription[], ConnectionConfiguration = {}, boolean = false, ListenerConfiguration) returns Error?` |
| method | `Listener.'start() returns Error\|()` |
| method | `Listener.gracefulStop() returns Error\|()` |
| method | `Listener.immediateStop() returns Error\|()` |
| method | `Listener.attach(Service 'service, string[]\|string\|() name = ()) returns Error\|()` |
| method | `Listener.detach(Service 'service) returns Error\|()` |

Declarations **removed** in `new` (1):

- `Caller.init() returns ballerina/mqtt:mqtt:Caller;` — see §4, this is a correction, not a loss.

Declarations **modified** in `new` (4):

| Location | old | new |
|---|---|---|
| `SecureSocket.protocol` (new:162) | `record {\|ballerina/mqtt:1.4.1:Protocol name; string version;\|}` | `record {\|Protocol name; string version;\|}` |
| `Client.init` return (new:293) | `ballerina/mqtt:1.4.1:Error?` | `Error?` |
| service listener args (new:347) | `(string serverUri = "", string clientId = "", ... subscriptions = "", ListenerConfiguration config = {})` | `(string serverUri, string clientId, ... mqtt:Subscription[] subscriptions, mqtt:ListenerConfiguration config = {})` |
| `onMessage` (new:348-350) | `remote function onMessage(Message message)` , no param doc | `# + message - The messages received for the topic` + `remote function onMessage(mqtt:Message message)` |

Unchanged between sides: README block (lines 7–67, byte-identical, and byte-identical to the bala
`docs/README.md`), module description, all 3 constants, all 13 records, the `Protocol` enum, the
`Service` class, `Caller.complete`/`Caller.respond`, and all 8 `Client` remote methods.

## 3. Correctness against library source

The bala's 8 `.bal` files are byte-identical to the `v1.4.1` GitHub tag (`cmp` on all 8 → SAME), so
source citations below are equally valid for both; paths given are bala paths.

New `Listener` class vs `modules/mqtt/listener.bal`:

| Render (new) | Source | Verdict |
|---|---|---|
| `class Listener` L232 | `public isolated class Listener` L20 | correct (render convention drops `public`/`isolated` everywhere) |
| `init(serverUri, clientId, subscriptions, ...) returns Error?` L233 | `public isolated function init(string serverUri, string clientId, string\|string[]\|Subscription\|Subscription[] subscriptions, *ListenerConfiguration config) returns Error?` L33 | param names/types correct; included-record handling see §5.2 |
| `'start() returns Error\|()` L240 | `public isolated function 'start() returns Error?` L44 | correct |
| `gracefulStop() returns Error\|()` L247 | L54 | correct |
| `immediateStop() returns Error\|()` L254 | L66 | correct |
| `attach(Service 'service, string[]\|string\|() name = ())` L261 | `attach(Service 'service, string[]\|string? name = ())` L80 | correct (`string?` expanded to `string\|()`) |
| `detach(Service 'service) returns Error\|()` L268 | L93 | correct |
| doc comments L227-231, L235-268 | listener.bal L24-27, L38-41, L48-51, L60-63, L72-75, L86-89 | verbatim match |

Private members `externInit` (L99) and `externStart` (L104) are correctly absent from the render.

`type Error error<ErrorDetails>` (new:87) vs `errors.bal:18` `public type Error distinct error<ErrorDetails>;`
— base type correct, `distinct` lost (§5.1).

`SecureSocket.protocol` (new:162) vs `types.bal:123-126`: `record {| Protocol name; string version; |} protocol?;`
— exact match; `old`'s `ballerina/mqtt:1.4.1:Protocol` was wrong.

Service section (new:347) vs `listener.bal:33`: init params are all required in source; `new`
emits them without defaults and `old` invented `= ""` for three of them. `new` is the faithful one.
`ListenerConfiguration config = {}` corresponds to the included record `*ListenerConfiguration config`.

Unchanged-but-verified `Client` methods against `client.bal`: `publish` (L44), `subscribe` (L55),
`receive` (L65), `close` (L77), `isConnected`, `disconnect`, `reconnect`, and `Caller.complete`/
`respond` against `caller.bal` L28/L40 — all names, params, and return types match.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Set-diff of every declaration line in both files (`diff` over `grep -E '^\s*(client class|class|type|enum|const|service|remote function|function)'`): the only `old`-only line is `Caller.init() returns ballerina/mqtt:mqtt:Caller;`.
- That removal is a **correction, not a loss**: `caller.bal` (bala, L20-44) defines `public client isolated class Caller` with only `complete` and `respond` — there is no `init` at all, and the return type `ballerina/mqtt:mqtt:Caller` was doubly malformed (an init returning the class, with an org/module/module-qualified name). `new` emitting no `init` for `Caller` matches the source.
- JSON-level comparison: `typeDefs` name sets identical (18 = 18, no adds/removes); only `Error`, `Listener`, `SecureSocket` differ, all in the direction of more information. `clients` differ only by the removed `Caller.init` and the de-qualified `Client.init` return. `services` differ only by a dropped `"optional": false` flag on `onMessage`.
- README string equality: `old['readme'] == new['readme']` → `True`; both equal the bala `docs/README.md` (2553 chars, both).
- Section markers: same 5 in both.
- No parameter, default value, return type, or doc line present in `old` is absent from `new` (verified per hunk over all 5 hunks).

## 5. Issues in `new` (independent of `old`)

1. **`distinct` lost on `Error`.** `new:87` renders `type Error error<ErrorDetails>;` but
   `errors.bal:18` is `public type Error distinct error<ErrorDetails>;`. The JSON carries
   `"baseType": "error<ErrorDetails>"` with no distinct flag, so the loss is extractor-side. Impact
   is low (an LLM writing `error<ErrorDetails>` where `mqtt:Error` is expected would still type-check
   only loosely), but the render is not exact. New-only content, so not a regression.
2. **Included-record (`*Config`) parameters are flattened *and* duplicated, producing
   non-compiling signatures.** `Listener.init` (new:233) renders as
   `(..., ConnectionConfiguration connectionConfig = {}, boolean manualAcks = false, ListenerConfiguration config)`
   — the fields of `*ListenerConfiguration` are inlined as defaulted params *and* the record itself
   is appended as a trailing required-position param. Source (`listener.bal:33`) has only
   `*ListenerConfiguration config`. Same shape appears on `Client.init` (new:293) — and it is
   identical in `old:251`, so this is a pre-existing renderer convention, not new behaviour; it is
   simply now visible on `Listener` too.
3. **Closed records rendered as open.** All 13 records in the source are `record {| ... |}`
   (e.g. `types.bal:29,43,52,61,77,93,102,111,121,135`; `errors.bal:22`); the render emits
   `record { ... }` for all of them. Present identically in `old`.
4. **`ListenerConfiguration.manualAcks` loses its default and is marked optional.** `new:200` is
   `boolean manualAcks?;`; `types.bal:64` is `boolean manualAcks = false;` (defaultable, not
   optional). Identical in `old`.
5. **`Service` is not a class.** `types.bal:193` is `public type Service distinct service object {};`;
   both renders emit `class Service { }` (JSON `"type": "Class"`). Identical in `old`.
6. **`Client.receive` typedesc parameter is mangled.** `new:314`
   `remote function receive(stream<mqtt:Message, error?> T = stream<mqtt:Message, error?>) returns T|Error;`
   vs `client.bal:65` `isolated remote function receive(typedesc<stream<Message, error?>> T = <>) returns T|Error`.
   The `typedesc<>` wrapper and the inferred `<>` default are both lost, and the printed default is
   not valid Ballerina. Identical in `old`.
7. **Enum members are duplicated as bare module-level constants, and the order is reversed.**
   `new:74,76` emit `const string SSL = "SSL";` / `const string TLS = "TLS";` in addition to
   `enum Protocol { TLS, SSL }` (new:178-181); source `types.bal:142-145` declares only
   `public enum Protocol { SSL, TLS }`. Identical in `old` (JSON typeDefs list `SSL`/`TLS` as
   `Constant` on both sides).

No encoding problems (`grep '[^ -~]'` over `new` → no hits) and no truncated doc text observed.

## 6. Coverage gaps vs. the library

**Zero public symbols of the default module are missing from `new`.** The bala has exactly one
module (`modules/mqtt`), so there is no submodule-only API and no shared submodule gap for this
library.

Full public surface of `modules/mqtt`, all present in `new`:
`DEFAULT_URL` (constants.bal:18), `Error`/`ErrorDetails` (errors.bal:18,22), `Message`,
`MessageProperties`, `ClientConfiguration`, `ListenerConfiguration`, `ConnectionConfiguration`,
`WillDetails`, `Subscription`, `DeliveryToken`, `SecureSocket`, `CertKey`, `Protocol`, `Service`
(types.bal), `Listener` (listener.bal:20), `Caller` (caller.bal:20), `Client` (client.bal:20).
Non-public `StreamIterator` (types.bal:148) and `processSubscriptions` (utils.bal:17) are correctly
absent from both renders.

Gap that is **not** an exported-symbol gap but worth recording: the `// --- Service ---` block on
both sides shows only `remote function onMessage(mqtt:Message message)`. The library additionally
supports an optional second `mqtt:Caller` parameter on `onMessage`, plus `onError(mqtt:Error)` and
`onComplete(mqtt:DeliveryToken)` remote methods (see §7). This block comes from fixed trigger
metadata, not from library extraction, so it is a shared gap on both sides. It is partially mitigated
because the retained README (new:54-63) does show `onMessage(mqtt:Message, mqtt:Caller)` and
`onError(mqtt:Error)`.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` (bala) registers
`io.ballerina.stdlib.mqtt.compiler.MqttCompilerPlugin` with `mqtt-compiler-plugin-1.4.1.jar`.
Source reviewed at `compiler-plugin/src/main/java/io/ballerina/stdlib/mqtt/compiler/`
(`MqttCompilerPlugin`, `MqttServiceAnalyzer`, `MqttServiceAnalysisTask`, `MqttServiceValidator`,
`MqttFunctionValidator`, `PluginConstants`, `PluginUtils`, and two code templates).

What it contributes:

- **Validations** (`PluginConstants.CompilationErrors`, 17 codes MQTT_101–MQTT_117): a service must
  have `onMessage` (MQTT_101); resource functions are banned (MQTT_103); methods must be `remote`
  (MQTT_104); `onMessage` takes a required `mqtt:Message` and an optional `mqtt:Caller`
  (MQTT_105/106/107/108); `onError` requires `mqtt:Error`/`error` (MQTT_111/112/113); `onComplete`
  requires `mqtt:DeliveryToken` (MQTT_115/116/117); returns must be `error?`/`mqtt:Error?`
  (MQTT_109); only one `mqtt:Listener` attachment (MQTT_110).
- **Code actions**: `MqttCodeTemplateWithCallerParameter` / `MqttCodeTemplateWithoutCallerParameter`
  generate the `onMessage` skeleton for an empty service (hint MQTT_114).

Absent from the render: the plugin's `onError` and `onComplete` remote methods and the optional
`mqtt:Caller` parameter on `onMessage` — the render's service shape is narrower than what the
compiler plugin accepts. Absent on both sides, so not a regression; it is a general trigger-metadata
limitation. No plugin-contributed annotations exist that the render should carry (`annotations: []`
in both JSONs, and the module declares none).

## 8. Other considerations

- No deprecations: no `@deprecated` in any bala `.bal` file; version 1.4.1 is stable (>= 1.0).
- Size: 351 lines, small; the 61-line README block is ~17% of the file and is verbatim the published
  `docs/README.md`. Token cost of the change is +43 lines (+14%), all of it real API (`Listener`).
- Doc quality inherited from the library is mostly good, though the render faithfully reproduces two
  upstream typos ("reqeust", `types.bal:41`) and trailing double-spaces in several `# + field` lines.
- `new` writes `Error|()` where the source writes `Error?`; semantically identical, both sides.
- `Listener` in `new` is emitted in the `// --- Types ---` section rather than a listener section;
  cosmetic, and `old` had nothing there at all.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_mqtt.bal.txt new/ballerina_mqtt.bal.txt` | 308 / 351 |
| `diff -u old new \| grep -c '^+' / '^-'` (minus header) | +50 / −7 |
| `diff -u old new \| grep -c '^@@'` | 5 hunks |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -nE 'ballerina/mqtt:' old` | lines 161, 232, 251 (3 hits) |
| `grep -nE '[a-z]+/[a-z.]+:[0-9]' new` | no hits |
| `grep -n '^// --- ' old` / `new` | 5 markers each (README, END README, Types, Client, Service) |
| `grep -c '^\s*#'` old / new | 112 / 144 |
| `diff` of declaration-line sets (old vs new) | +8 lines (Error, Listener + 6 methods), −1 (`Caller.init`), 4 modified |
| `git ls-remote --tags` | `v1.4.1` → `0b183ea668bf7bd009ce03ea2982959d2bbbbb3d` |
| `git clone --depth 1 --branch v1.4.1` | succeeded (2nd attempt; first timed out) |
| `cmp` bala `modules/mqtt/*.bal` vs clone `ballerina/*.bal` (8 files) | all SAME |
| `wc -l` bala module .bal files | 589 lines total across 8 files |
| `ls bala/.../modules` | single module `mqtt` (no submodules) |
| JSON section sizes (old / new) | typeDefs 18/18, clients 2/2, services 1/1, functions 0/0, annotations 0/0 |
| JSON typeDefs name-set diff | `only old: {}`, `only new: {}` |
| JSON typeDefs value diff | `Error`, `Listener`, `SecureSocket` differ only |
| `old['Error']` vs `new['Error']` | new adds `"baseType": "error<ErrorDetails>"` |
| `old['Listener']['type']` vs new | `None` → `"Class"` |
| JSON `clients` diff | `Caller.init` block removed; `Client.init` return `ballerina/mqtt:1.4.1:Error?` → `Error?` |
| JSON `services` diff | only `"optional": false` removed on `onMessage` |
| `old['readme'] == new['readme']` | `True`; both == bala `docs/README.md` (2553 chars) |
| `caller.bal` L17-44 read | no `init` declared → old's `Caller.init` was synthesized/bogus |
| `listener.bal` L20-108 read | all 6 rendered methods + docs verified; 2 private externs correctly omitted |
| `errors.bal` L18 | `public type Error distinct error<ErrorDetails>;` → `distinct` lost in render |
| `types.bal` L29-193 read | 13 records all `record {\| \|}`; `Protocol` = `{SSL, TLS}`; `Service` = `distinct service object {}`; `StreamIterator` non-public |
| `client.bal` L20-80 read | `init` is `*ClientConfiguration`; `receive` is `typedesc<stream<Message, error?>> T = <>` |
| `compiler-plugin.json` (bala) | `MqttCompilerPlugin`, jar `mqtt-compiler-plugin-1.4.1.jar` |
| `PluginConstants.java` L27-72 | MQTT_101–MQTT_117; onMessage/onError/onComplete; Caller/Message/Error/DeliveryToken params; 2 code templates |
| `MqttFunctionValidator.java` L75-128, L193-199 | validates onMessage/onError/onComplete, optional Caller param |
| `LC_ALL=C grep '[^ -~]' new` | no hits (no encoding damage) |
| `grep -rn '@deprecated' bala modules` | no hits |

## 10. Caveats and unverified items

- The first `git clone` attempt failed with a network timeout to github.com; the retry succeeded, and
  the clone is a shallow grafted checkout of tag `v1.4.1`. All source claims were additionally
  confirmed against the bala, which is authoritative.
- Ballerina Central metadata was **not** re-queried over the network for this review; module list,
  version and single-module structure were established from the bala
  (`java21/modules/` contains only `mqtt`) and `package.json`/`compiler-plugin.json`, not from the
  Central API.
- The compiler plugin's runtime behaviour (code-action output, diagnostic emission) was read from
  source only; the plugin jar was not executed or decompiled, and `compiler-plugin-tests/` was not
  run.
- Neither render was compiled; "non-compiling" claims in §5.2 and §5.6 are from reading the emitted
  syntax against the Ballerina grammar (required param after defaulted params; `= stream<...>` as a
  value expression), not from a compiler run.
- Whether the `distinct` qualifier loss on `Error` is intended behaviour of spec v2 or an oversight
  was not determined — only that the JSON does not carry the flag.

# ballerinax/rabbitmq 3.6.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/rabbitmq` |
| Pinned version | `3.6.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-rabbitmq |
| Tag reviewed | `v3.6.0` (commit `e90f5c0f598d6fa6e2e9029d27d51e4a02be2cd2`, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/rabbitmq/3.6.0/java21` |
| Old render | `622` lines |
| New render | `695` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better. All 16 lines removed from `old` are replaced by more accurate content:
the 4 `// Unknown type:` placeholders (`Error`, `PayloadBindingError`, `PayloadValidationError`,
`Listener`) become real definitions, the whole `rabbitmq:Listener` class (6 methods) appears, the
`@rabbitmq:Payload` annotation appears, both version/module-qualified type refs
(`ballerinax/rabbitmq:3.6.0:Protocol`, `ballerinax/rabbitmq:3.6.0:Error?`) are resolved to plain
names, a fabricated `Caller.init() returns ballerinax/rabbitmq:rabbitmq:Caller` is dropped (the
library's `Caller` declares no `init`), `ServiceConfig` gains its real attach points (`on service,
class`) and its real doc string, and the service template gains queue-name/handler-choice
constraints and payload-binding guidance that match the compiler plugin's diagnostics exactly.
No declaration, parameter, default, doc line, or README content present in `old` is lost in `new`.
Remaining inaccuracies (wrong boolean defaults, unquoted string default, `typedesc` mangling,
`distinct` lost) are extractor/renderer defects, all but one of which exist identically in `old`.

## 2. Change inventory

Line counts (`wc -l`): old 622, new 695. `diff old new`: **89 lines added, 16 removed**, 4 hunks.
Lines 1–343 (header, `import`, full README block, all constants and most records) are **byte
identical** (`diff <(sed -n '1,343p' old) <(sed -n '1,343p' new)` → 0 lines of output; README block
lines 7–194 → 0 lines).

Signals: `// Unknown type:` old **4** → new **0**; version/module-qualified type refs old **3** →
new **0**; `// --- ` section markers **6** on both sides.

### Added in `new` (11 declaration lines)

| Kind | Declaration | New render line |
|---|---|---|
| type (error) | `type Error error;` | 446 |
| type (error) | `type PayloadBindingError error;` | 449 |
| type (error) | `type PayloadValidationError error;` | 452 |
| class | `class Listener { … }` | 465 |
| constructor | `Listener.init(string host, int port, QosSettings\|() qosSettings = (), …, ConnectionConfiguration connectionData) returns Error?` | 466 |
| function | `Listener.attach(Service s, string[]\|string\|() name = ()) returns error?` | 473 |
| function | `Listener.'start() returns error?` | 480 |
| function | `Listener.detach(Service s) returns error?` | 487 |
| function | `Listener.gracefulStop() returns error?` | 494 |
| function | `Listener.immediateStop() returns error?` | 502 |
| annotation | `public annotation RabbitmqPayload Payload on parameter;` | 695 |

Plus non-declaration additions: 6 doc/guidance lines above the `service` block, 1
`@rabbitmq:ServiceConfig {...} // optional` line, and ~20 per-method guidance lines inside it
(alternatives, payload binding, required/optional parameter lists).

### Removed from `new` (16 lines, all superseded)

`diff old new | grep '^<'` — every removed line and its replacement:

| Removed from `old` | Replaced in `new` by |
|---|---|
| `record {\|ballerinax/rabbitmq:3.6.0:Protocol name;\|} protocol?;` (old:347) | `record {\|Protocol name;\|} protocol?;` (new:347) |
| `// Unknown type: Error` / `PayloadBindingError` / `PayloadValidationError` / `Listener` (4 lines) | real `type … error;` definitions + `class Listener` |
| `function init() returns ballerinax/rabbitmq:rabbitmq:Caller;` (old:462) | nothing — correct, no such `init` exists in the library |
| `Client.init(…) returns ballerinax/rabbitmq:3.6.0:Error?;` (old:481) | identical signature, `returns Error?` (new:527) |
| `service rabbitmq:Service on new rabbitmq:Listener(string host = "", int port = 0, …)` (old:608) | `… (string host, int port, rabbitmq:QosSettings\|() qosSettings = (), rabbitmq:ConnectionConfiguration connectionData = {})` (new:660) |
| 3 `onMessage`/`onRequest`/`onError` signatures + their 3 one-line docs | same 3 methods, module-qualified param types, richer docs, `// optional` markers |
| `# Define advanced queue configurations ` + `public annotation … ServiceConfig on service;` | `# The annotation, which is used to configure the subscription.` + `… on service, class;` |

### Modified (not added/removed)

- `Client.init` return type de-qualified; `SecureSocket.protocol` inline record de-qualified.
- `onError` parameter renamed `rabbitmqError` → `err` (param names are not part of the remote-method
  contract; plugin `RABBITMQ_107` only checks the two types).
- Service-method descriptions rewritten (behavioural prose instead of one-liners) — see §3.
- JSON only: `typeDefs[].baseType` added; `services[].identifier`, `services[].constraints`,
  `services[].annotations`, `methods[].parameters[].alternatives/annotationRefs/binding` added;
  `annotations[].displayName` (`"Service Configuration"`) dropped. That field was never rendered on
  either side (`grep -c 'Service Configuration'` → 0 in both), so no render impact.
- JSON only: `clients[Caller].functions` 3 → 2 (`init` dropped); `Client` 15 and `MessageStore` 4
  unchanged; `typeDefs` 31 on both sides (same 31 names, `Listener` gains `"type":"Class"`,
  the 3 error types gain `"baseType":"error"`); `annotations` 1 → 3 (ServiceConfig×SERVICE,
  ServiceConfig×CLASS, Payload).

## 3. Correctness against library source

Everything `new` adds was checked against the bala module sources (authoritative) and matches
upstream `v3.6.0` byte-for-byte in the files consulted.

- `class Listener` and its 6 members: `modules/rabbitmq/listener.bal:22` (`public isolated class
  Listener`), `init` at :36, `attach` at :59, `'start` at :69, `detach` at :80, `gracefulStop` at :90,
  `immediateStop` at :101. All names, parameter types, defaults (`QosSettings? qosSettings = ()`,
  `string[]|string? name = ()`) and return types (`Error?` for `init`, `error?` for the rest) match.
  The only private member (`private string connectorId`, :24) is correctly excluded.
- `type Error`/`PayloadBindingError`/`PayloadValidationError`: `rabbitmq_errors.bal:18,21,24`.
  Names and doc strings match; `distinct` and the subtype chain are lost (§5.1).
- `annotation RabbitmqPayload Payload on parameter`: `rabbitmq_commons.bal:179`, doc string
  identical ("The annotation which is used to define the payload parameter in the `onMessage`
  service method.").
- `annotation RabbitMQServiceConfig ServiceConfig on service, class`: `listener.bal:125` — `new`'s
  attach points and doc string ("The annotation, which is used to configure the subscription.") are
  exactly the source's; `old`'s `on service` + "Define advanced queue configurations" were both
  wrong.
- `SecureSocket.protocol` → `record {| Protocol name; |}`: `rabbitmq_commons.bal:138–144`. Correct.
- `Client.init` returning `Error?`: `client.bal:33`. Correct.
- `Caller` has **no** `init` (`caller.bal:20–48` — only `basicAck` :31 and `basicNack` :44), so
  `old`'s `function init() returns ballerinax/rabbitmq:rabbitmq:Caller;` was invented; dropping it
  is a fix.
- Listener args in the service template now required (`string host, int port`) — matches
  `listener.bal:36` where both are required; `old`'s `host = "", port = 0` was fabricated.
- Service-template guidance vs. compiler plugin (`compiler-plugin/src/main/java/io/ballerina/stdlib/rabbitmq/plugin/`):
  "exactly one of onMessage or onRequest" ↔ `PluginConstants.java:69–70`
  (`ON_MESSAGE_OR_ON_REQUEST` RABBITMQ_101, `NO_ON_MESSAGE_OR_ON_REQUEST` RABBITMQ_102); "queue name
  from exactly one source: `@rabbitmq:ServiceConfig { queueName }` or the service identifier" ↔
  `RabbitmqServiceValidator.java:108–114` + `NO_ANNOTATION` RABBITMQ_119 /
  `INVALID_SERVICE_ATTACH_POINT` RABBITMQ_120 (string-literal identifier only); "`message` may bind
  directly to anydata … but never `rabbitmq:AnydataMessage`" ↔ RABBITMQ_108 ("Only subtypes of
  rabbitmq:AnydataMessage or subtypes of anydata"); `caller` optional ↔ RABBITMQ_110/114 (Caller is
  permitted, not required); `BytesMessage` alternative ↔ `message.bal:35` (`*AnydataMessage` with
  `byte[] content`), and the `bindableFields:["content"]` / `fixedFields:["routingKey","exchange",
  "deliveryTag","properties"]` split in the JSON matches `message.bal:24–32` exactly.
- Unchanged-but-verified: `Client`'s 15 methods and `MessageStore`'s 4 methods match `client.bal`
  and `message_store.bal` in name/arity/return type (defaults excepted, §5.3).
- Docs: an exhaustive description-by-description comparison of both JSONs (all 31 typeDefs, all 3
  clients, all 21 client functions, all 3 service methods, `readme`, package `description`) found
  differences in exactly 4 places: the removed `Caller.init` and the 3 deliberately rewritten
  service-method descriptions. Nothing else changed.

## 4. Regressions

**None found.** Basis:

- All 16 removed lines enumerated in §2 with their replacements; each replacement is equal or more
  accurate against the bala source. No declaration name disappears (JSON typeDef name sets are
  identical; the only lost function is the fabricated `Caller.init`).
- Declaration extraction over both files (`grep -nE '^\s*(public )?(isolated )?(remote |resource )?(client )?(function|type|class|enum|const|annotation|listener|service)\b'`): 69 declaration lines in `old`, 79 in `new`; `new ⊃ old` minus `Caller.init` only.
- No parameter, default, or return type was dropped: `Client.init`, all 14 other `Client` methods,
  both `Caller` methods and all 4 `MessageStore` methods are character-identical between the two
  renders apart from `Client.init`'s de-qualified return type.
- No doc/README loss: README block (lines 7–194) identical; description comparison above.
- No new malformed syntax introduced except as noted in §5.2, which mirrors a construct already
  present in `old` (`Client.init`).

## 5. Issues in `new` (independent of `old`)

1. **`distinct`-ness and the error subtype chain are lost.** Source: `Error distinct error`,
   `PayloadBindingError distinct Error`, `PayloadValidationError distinct PayloadBindingError`
   (`rabbitmq_errors.bal:18,21,24`). `new` renders all three as `type X error;` (`baseType:"error"`
   in JSON for all three), so an LLM cannot tell that `PayloadValidationError <: PayloadBindingError
   <: Error`. Still a large improvement over `old`'s bare `// Unknown type:` lines. **New-only** (the
   information did not exist in `old` at all).
2. **`Listener.init` renders as non-compiling Ballerina with invented defaults.** New:466 expands the
   `*ConnectionConfiguration connectionData` included-record parameter into its 11 fields **and**
   keeps a trailing required `ConnectionConfiguration connectionData`, i.e. a required parameter after
   defaultable ones. It also invents defaults for fields that are optional with no default in source
   (`SecureSocket secureSocket = {cert: {path: "", password: ""}}`, `Credentials auth = {username:
   "", password: ""}` vs. `secureSocket?` / `auth?` at `rabbitmq_commons.bal:113–114`); note
   `{path:…}` is not even a valid `crypto:TrustStore|string` literal shape for `cert`. Identical
   treatment already exists for `Client.init` in **both** renders (old:481 / new:527), so this is a
   pre-existing renderer convention now also applied to `Listener`.
3. **Five wrong boolean defaults (present identically in `old`).** The extractor emits the type-zero
   value when a parameter's default is a literal `true`: JSON `"default":"false"` on both sides for
   `Caller.basicNack.requeue` (source `true`, `caller.bal:44`), `Client.basicNack.requeue` (`true`,
   `client.bal:180`), `Client.consumeMessage.autoAck` (`true`, `client.bal:135`),
   `Client.consumePayload.autoAck` (`true`, `client.bal:150`),
   `MessageStore.acknowledge.success` (`true`, `message_store.bal:138`). This inverts
   acknowledgement semantics for a consumer written from the render. (`Client.init.validation = true`
   is correct, so the loss is specific to function-parameter literal defaults.)
4. **Unquoted string default — non-compiling.** `MessageStore.init(…, string host = localhost, …)`
   (old:588, new:634); source default is `DEFAULT_HOST` = `"localhost"`
   (`message_store.bal:23`). JSON carries `"default":"localhost"` on both sides and the renderer
   omits quotes. Shared with `old`.
5. **`typedesc` parameters mangled.** Source `typedesc<AnydataMessage> T = <>` /
   `typedesc<anydata> T = <>` (`client.bal:135,150`) render as `AnydataMessage T =
   rabbitmq:AnydataMessage` and `anydata T = anydata` — neither valid nor meaningful. Shared with
   `old`.
6. **`Service` rendered as an empty class.** Source is `public type Service distinct service object
   {…}` (`service_type.bal:18`); both renders emit `class Service { }`. Shared with `old`.

Minor, both sides: `public`/`isolated`/`client`-on-`Caller` qualifiers are dropped from
declarations; `Error?` returns are written `Error|()`. Both are valid or harmless for an LLM reader.

## 6. Coverage gaps vs. the library

**0 gaps in `new`.** The bala exports exactly one module (`package.json` `"export": ["rabbitmq"]`;
`modules/` contains only `rabbitmq/`; Central `modules` list = `['rabbitmq']`), so there is no
submodule-only API and no shared submodule gap for this library. All 33 public symbols found by
`grep -nE '^public ' modules/rabbitmq/*.bal` appear in `new`: `Caller`, `Listener`, `Client`,
`MessageStore`, `Service`, `AnydataMessage`, `BytesMessage`, `BasicProperties`, `QueueConfig`,
`ExchangeConfig`, `ExchangeType`, `Address`, `ConnectionConfiguration`, `QosSettings`,
`SecureSocket`, `CertKey`, `Protocol`, `Credentials`, `RabbitmqPayload`, `RabbitMQServiceConfig`,
`StoreClientConfiguration`, `StoreClientPublishConfiguration`,
`StoreClientDeclareQueueConfiguration`, `Error`, `PayloadBindingError`, `PayloadValidationError`,
`DEFAULT_HOST`, `DEFAULT_PORT`, `DIRECT_EXCHANGE`, `FANOUT_EXCHANGE`, `TOPIC_EXCHANGE`,
`ServiceConfig`, `Payload`.

For comparison, `old` was missing 2 outright (`Listener` class body, `Payload` annotation) and
degraded 3 (`Error`, `PayloadBindingError`, `PayloadValidationError`) to placeholder comments.

Representational gap shared by both renders: `MessageStore` includes `*messaging:Store`
(`message_store.bal:55`) and neither render mentions it (`grep -c 'messaging:Store'` → 0 in both),
so its role as a `ballerina/messaging` store implementation is invisible. `retrieve()` returning
`messaging:Message` is annotated in both with the cross-package note, so this is cosmetic.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.rabbitmq.plugin.RabbitmqCompilerPlugin`
(jar `rabbitmq-compiler-plugin-3.6.0.jar`). Source read at `v3.6.0`:
`RabbitmqCompilerPlugin`, `RabbitmqServiceAnalysisTask`, `RabbitmqServiceValidator`,
`RabbitmqFunctionValidator`, `RabbitmqCodeAnalyzer`, `RabbitmqCodeTemplate`, `PluginConstants`,
`PluginUtils`.

Contributions: 21 compile-time validations (RABBITMQ_101–121 in `PluginConstants.java:68–104`)
covering handler choice, remote-qualifier/resource-function rules, allowed parameter types and
counts, allowed return types, single-listener attachment, and the ServiceConfig/service-identifier
requirement; plus one code action — `RabbitmqCodeTemplate.java:67` "Insert service template",
triggered by the `TEMPLATE_CODE_GENERATION_HINT` (RABBITMQ_121) emitted for an empty service. It
generates no build artifacts and adds no annotations.

Nothing the plugin implies is missing from `new`: the handler-choice rule, the queue-name-source
rule, `caller` optionality, and the `anydata` / `*AnydataMessage` / `BytesMessage` payload-binding
options are all encoded in `services[].constraints`, `services[].identifier` and
`methods[].parameters[].binding` and surfaced as render comments (see §3). `old` surfaced none of
them. Not encoded on either side (informational only): the return-type restrictions RABBITMQ_116/117
(`error?`/`rabbitmq:Error?` for `onMessage`/`onError`, `anydata|error` for `onRequest`) beyond what
the signatures themselves show, the single-listener rule RABBITMQ_118, and the resource-function
prohibition RABBITMQ_104.

## 8. Other considerations

- Not deprecated; stable major (`3.6.0`); Central `pullCount` 1303; `graalvmCompatible: Yes`;
  built with Ballerina `2201.12.0`.
- Bala and upstream `v3.6.0` agree on every file consulted, so no bala-vs-GitHub conflict arose.
- Size: +73 lines (+11.7%), of which ~30 are the new `Listener` class and ~35 are service-template
  guidance prose. Token cost is modest and buys the listener API plus the plugin's rules; a good
  trade.
- The `Protocol` enum members are emitted twice — as three `const string SSL/TLS/DTLS` entries
  (lines 213–217) and again as `enum Protocol` (line 365) — on both sides. Harmless duplication.
- `README` is reproduced verbatim (185-line `docs/README.md` → render lines 7–194) on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 622 / 695 |
| `diff old new \| grep -c '^>' / '^<'` | 89 added / 16 removed |
| `diff old new \| grep '^<'` | all 16 removed lines enumerated in §2 |
| `grep -c '^// Unknown type:'` | old 4, new 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:\|ballerinax/rabbitmq:rabbitmq:'` | old 3 (lines 347, 462, 481), new 0 |
| `grep -n '^// --- '` | 6 markers each (README/END README/Types/Client/Service/Annotations) |
| `diff <(sed -n '1,343p' old) <(sed -n '1,343p' new)` | empty |
| `diff <(sed -n '7,194p' old) <(sed -n '7,194p' new)` | empty (README identical) |
| declaration extraction on both files | 69 old / 79 new lines; `new ⊃ old` less `Caller.init` |
| `git ls-remote --tags …-rabbitmq \| grep v3.6.0` | `refs/tags/v3.6.0` → `e90f5c0f…` |
| `git clone --depth 1 --branch v3.6.0`; `git describe --tags` | `v3.6.0` (grafted) |
| `ls bala/.../modules` | single module `rabbitmq` (10 `.bal` files, 932 lines) |
| `cat bala/.../package.json` | `"export": ["rabbitmq"]`, `ballerina_version 2201.12.0`, `graalvmCompatible true` |
| `grep -nE '^public ' bala modules/*.bal` | 33 public symbols (listed §6) |
| `caller.bal:20–48` | no `init`; `basicAck(multiple=false)`, `basicNack(multiple=false, requeue=true)` |
| `listener.bal:22,36,59,69,80,90,101,117,125` | Listener class + 6 methods + `RabbitMQServiceConfig` + `ServiceConfig on service, class` |
| `rabbitmq_errors.bal:18,21,24` | `distinct error` chain |
| `rabbitmq_commons.bal:104–179` | ConnectionConfiguration/QosSettings/SecureSocket/CertKey/Protocol/Credentials/RabbitmqPayload/`Payload` |
| `client.bal:33–250` | 15 methods; `consumeMessage/consumePayload autoAck=true`, `basicNack requeue=true`, `typedesc<…> T = <>` |
| `message_store.bal:22–138` | `host = DEFAULT_HOST`, `*messaging:Store`, `acknowledge(success=true)` |
| JSON typeDef name sets | identical (31/31); `Listener` `type: null → "Class"`; 3 error types `baseType: null → "error"` |
| JSON `clients` function lists | Caller 3→2 (`init` dropped), Client 15→15, MessageStore 4→4 |
| JSON `annotations` | old 1 (ServiceConfig/SERVICE, `displayName` present) → new 3 (ServiceConfig/SERVICE, ServiceConfig/CLASS, Payload; no `displayName`) |
| `grep -c 'Service Configuration'` in renders | 0 / 0 (dropped `displayName` never rendered) |
| JSON description comparison (all typeDefs, clients, functions, service methods, readme, description) | only 4 diffs: removed `Caller.init`, 3 rewritten service-method docs |
| JSON param defaults for `requeue`/`autoAck`/`success`/`validation` | identical on both sides; `requeue=false`×2, `autoAck=false`×2, `success=false`, `validation=true` |
| JSON `MessageStore.init` params | `host` default `localhost` (unquoted in render) on both sides |
| new JSON `services[0].constraints` / `identifier` / `annotations` | `$queueNameSource` + `$messageHandlerChoice` (`structure.exactlyOne`), identifier `optional`/`stringLiteral`, ServiceConfig `optional` |
| new JSON `onMessage.parameters[0]` | `alternatives:[BytesMessage]`, `annotationRefs:[Payload]`, `binding.typedescs` with `excludes:[AnydataMessage]` and `bindableFields:["content"]` |
| `PluginConstants.java:68–104` | RABBITMQ_101–121 diagnostics (quoted in §7) |
| `RabbitmqServiceValidator.java:95–120` | annotation-or-string-literal-identifier rule |
| `RabbitmqCodeTemplate.java:47–105` | "Insert service template" code action on RABBITMQ_121 |
| `grep -c 'messaging:Store'` in renders | 0 / 0 |
| Central `GET /2.0/registry/packages/ballerinax/rabbitmq/3.6.0` | `deprecated: null`, `visibility: public`, `pullCount: 1303`, `modules: ['rabbitmq']` |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific rendered signatures are non-compiling
  (§5.2 required-after-defaultable parameter, §5.4 unquoted `localhost`, §5.5 `typedesc` forms) rest
  on Ballerina syntax/semantics, not on a `bal build` run.
- Upstream is a shallow (`--depth 1`) clone at `v3.6.0`; only `ballerina/**` module sources and
  `compiler-plugin/src/main/java/**` were read. `compiler-plugin-tests/`, `native/`, `examples/`
  and `load-tests/` were not reviewed, so plugin behaviour beyond the diagnostic/code-action
  inventory in §7 is unverified.
- Only the `java21` platform directory exists in the bala; no other platform variant was checked
  because none is published.
- Whether the 3 service-method description rewrites and the guidance prose in `new` are authored
  metadata (trigger-metadata models in the extension) rather than derived from library source was
  not traced to its source file — the library's `Service` type is empty
  (`service_type.bal:18–20`), so this content must come from outside the library either way. Its
  factual claims were verified against the compiler plugin (§3), but its provenance was not.
- Ballerina Central was queried once, live, on the review date; `pullCount` is a point-in-time value.

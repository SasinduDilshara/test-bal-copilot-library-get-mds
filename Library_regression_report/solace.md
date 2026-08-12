# ballerinax/solace 0.4.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/solace` |
| Pinned version | `0.4.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-solace |
| Tag reviewed | `v0.4.0` (commit `29eb69a`, `[Gradle Release Plugin] - pre tag commit: 'v0.4.0'`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/solace/0.4.0/java21` |
| Old render | `796` lines |
| New render | `840` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Both renders describe the same 57 typeDefs,
3 clients, 1 service, 1 annotation (JSON top-level counts identical). The 11 diff hunks are all
spec-v2 fixes:

- The 2 `// Unknown type:` placeholders in `old` (`Error`, `Listener`) become real definitions in
  `new`. `Listener` alone recovers a class with 6 members that `old` dropped entirely, even though
  the members were already present in `old`'s JSON.
- All 18 version/module-qualified type references in `old` (17 × `ballerinax/solace:0.4.0:` on 10
  lines, plus 1 × `ballerinax/solace:solace:Caller`) are gone in `new`.
- Two invented/malformed artifacts in `old` are removed: the non-existent `Caller` constructor and
  the `anydata Additional Values` parameter injected into client `init` signatures.
- The `ServiceConfig` annotation doc and the service-template listener arguments in `new` now match
  the published source; `old` had a stale doc string and a wrong `url = ""` default.

No render-level regression was found. Remaining inaccuracies in `new` are extractor-level
default-value/optionality bugs that `old` shares character-for-character everywhere the two files
overlap (the non-diffed 785 lines are byte-identical).

## 2. Change inventory

Mechanical totals (`diff` on the two renders):

| Metric | Value |
|---|---|
| Old lines | 796 |
| New lines | 840 |
| Lines added | 61 |
| Lines removed | 17 |
| Hunks | 11 |
| `// Unknown type:` lines | old 2 → new 0 |
| `ballerinax/solace:0.4.0:` occurrences | old 17 (10 lines) → new 0 |
| `ballerinax/solace:solace:` occurrences | old 1 → new 0 |
| Section markers `// --- ` | 6 in both (README, END README, Types, Client, Service, Annotations) |
| README block | lines 7–167 byte-identical in both (`cmp` clean); full 158-line bala README, not truncated |

JSON-level counts (both files): `typeDefs` 57, `clients` 3 (`Caller`, `MessageConsumer`,
`MessageProducer`), `functions` 0, `services` 1, `annotations` 1. TypeDef name list is identical and
in the same order — no type added or removed, only re-rendered.

### Added in `new` (7 declarations)

| Kind | Declaration |
|---|---|
| type | `type Error error;` (was `// Unknown type: Error`) |
| class | `class Listener { … }` (was `// Unknown type: Listener`) |
| class method | `function init(string url, …, ListenerConfiguration config) returns Error?` |
| class method | `function attach(Service s, string[]\|string\|() name = ()) returns Error\|()` |
| class method | `function detach(Service s) returns Error\|()` |
| class method | `function 'start() returns Error\|()` |
| class method | `function gracefulStop() returns Error\|()` |
| class method | `function immediateStop() returns Error\|()` |

### Removed in `new` (3 items, all of them wrong in `old`)

| Item | Why removal is correct |
|---|---|
| `function init() returns ballerinax/solace:solace:Caller;` inside `client class Caller` | `caller.bal:24-69` declares **no** `init`; the constructor was invented and its return type was doubly-qualified nonsense |
| `anydata Additional Values` parameter in `MessageConsumer.init` and `MessageProducer.init` (2 render occurrences; 3 in `old` JSON, incl. `Listener.init`) | Not a parameter of any `init`; a rest-field artifact rendered as a syntactically invalid parameter name (space in identifier) |
| Annotation doc `# Define advanced configurations like queue or topic name` | Replaced by the real doc from `annotations.bal:17-20` |

### Modified in `new` (kind-grouped)

| Kind | Change | Count |
|---|---|---|
| union typeDefs | member refs de-qualified (`Destination`, `OAuth2Configuration`, `AuthConfiguration`, `SubscriptionConfiguration`, `ServiceConfiguration`, `Property`, `Value`) | 7 |
| record field | `map<ballerinax/solace:0.4.0:Property>` → `map<Property>` in `Message.properties` | 1 |
| client `init` | return type `ballerinax/solace:0.4.0:Error?` → `Error?`; `Additional Values` param dropped (`MessageConsumer`, `MessageProducer`) | 2 |
| service template | `on new solace:Listener(string url = "", ListenerConfiguration config = {})` → `(string url, solace:ListenerConfiguration config = {})` | 1 |
| service methods | param types module-qualified (`solace:Message`, `solace:Caller`, `solace:Error`); per-param doc lines added; `Required parameters: message` / `Optional parameters (may be omitted): caller` added | 2 |
| annotation | doc replaced with the source doc | 1 |

## 3. Correctness against library source

Every item `new` adds or changes, checked against the bala (authoritative) and the `v0.4.0` clone.

| Render (new) | Source | Verdict |
|---|---|---|
| `# Represents a Solace distinct error.` / `type Error error;` | `modules/solace/errors.bal:17-18` → `public type Error distinct error;` | Doc exact; `distinct` lost (see §5.1) |
| `class Listener` with `init`, `attach`, `detach`, `'start`, `gracefulStop`, `immediateStop` — in that order | `listener.bal:56` (`public isolated class Listener`), `:63` init, `:81` attach, `:91` detach, `:100` `'start`, `:110` gracefulStop, `:119` immediateStop | Member set and order exact; private `initListener` (`listener.bal:68`) correctly omitted |
| `function attach(Service s, string[]\|string\|() name = ())` | `listener.bal:81`: `public isolated function attach(Service s, string[]\|string? name = ()) returns Error?` | Correct (`?` expanded to `\|()`) |
| `function init(string url, …, ListenerConfiguration config)` | `listener.bal:63`: `public isolated function init(string url, *ListenerConfiguration config) returns Error?` | Included-record param flattened; see §5.2/§5.3 for defaults and syntax |
| Method docs on all 5 Listener methods | `listener.bal:73-118` doc comments | Text matches verbatim (minus `+ param -` lines) |
| `Caller` has no constructor | `caller.bal:24` — class body starts directly with `ack` | Correct |
| `public annotation ServiceConfiguration ServiceConfig on service;` + 3-line doc | `annotations.bal:17-21` | Verbatim match, incl. "Exactly one of `queueName` or `topicName` must be provided." |
| `on new solace:Listener(string url, solace:ListenerConfiguration config = {})` | `listener.bal:63` — `url` is a required positional param | Correct; `old`'s `string url = ""` was wrong |
| `onMessage(solace:Message message, solace:Caller caller)`, `caller` optional | `types.bal:19-26` documents both 1-param and 2-param forms; `caller.bal:21-22` "supplied as the optional second parameter"; compiler plugin `SOLACE_105`/`SOLACE_107` enforce exactly that | Correct |
| `onError(solace:Error solaceError) returns error?` | `types.bal:25` `onError(solace:Error err) returns solace:Error?`; plugin `SOLACE_108` | Shape correct; param name differs (`solaceError` vs `err`) and return widened to `error?` — comes from the LS trigger metadata, identical in `old` |
| De-qualified union members (`Topic\|Queue`, `QueueConfiguration\|TopicConfiguration`, …) | `types.bal:45` (Destination), `:90` (OAuth2Configuration), `:93` (AuthConfiguration), `:300` (SubscriptionConfiguration), `:350` (ServiceConfiguration), `:397` (Property), `:400` (Value) | All member names exist as public types; de-qualification is faithful |

## 4. Regressions

**None found at the render level.**

What I checked to conclude that:
- Full `diff -u old new` (11 hunks, 17 removed lines) reviewed line by line; every removed line is
  either a version-qualified spelling of a type that `new` still emits, or one of the three invented
  artifacts in §2 (`Caller.init`, `Additional Values`, stale annotation doc).
- Declaration-set comparison: 0 declarations removed (`old` declarations ⊆ `new`). All 52 public
  top-level symbols of the default module resolve in both files (script over `grep '^public '` of the
  10 bala `.bal` files against both renders).
- Per-parameter check of the three `init` signatures: no parameter present in `old` is missing from
  `new` except `Additional Values`; no default value or return type was dropped.
- README block is byte-identical (`cmp` on lines 7–167) — no doc content lost.
- Section markers: 6 in both; nothing dropped from the Client/Service/Annotations sections.

Two JSON-level metadata drops exist but have **zero render impact**, so they are not counted as
render regressions:

1. `annotations[0].displayName: "Service Configuration"` present in `old` JSON, absent in `new`.
   Neither render emits it (`grep -c 'Service Configuration'` on `old` render = 0). This is correct
   information lost from the JSON payload; a future renderer that uses `displayName` would see less
   than `old` did.
2. `services[0].functions[*].optional: false` on `onMessage` and `onError` present in `old` JSON,
   absent in `new`. The `old` value was itself wrong for `onError` (the plugin, `SOLACE_103`, treats
   `onError` as optional), so no correct information was lost. Neither render shows it.

## 5. Issues in `new` (independent of `old`)

1. **`type Error error;` drops `distinct`.** Source is `public type Error distinct error;`
   (`errors.bal:18`). The new JSON carries `"type":"Error","baseType":"error"` with no distinctness
   flag, so the renderer cannot express it. Consequence: an LLM may believe any `error` is assignable
   to `solace:Error`. Net still an improvement over `old`'s bare `// Unknown type: Error`.
2. **Wrong default values in the flattened `Listener.init` parameters.** Compared with
   `types.bal:200-222` (`CommonConnectionConfiguration`) and `types.bal:238-248`:
   | Render (new) | Source default | |
   |---|---|---|
   | `string messageVpn = ""` | `"default"` | wrong |
   | `AuthConfiguration auth = {username: ""}` | field is `auth?` (no default) | invented |
   | `string clientDescription = ""` | `"Ballerina Solace Connector"` | wrong |
   | `decimal connectTimeout = 0.0d` | `30.0` | wrong |
   | `decimal readTimeout = 0.0d` | `10.0` | wrong |
   | `SecureSocket secureSocket = {}` / `RetryConfiguration retryConfig = {}` | both optional, no default | invented |
   These come from the extractor (visible in the JSON `"default"` fields), not the renderer, and the
   same bug is present in `old` for `MessageConsumer.init`/`MessageProducer.init`. It is newly
   *visible* for `Listener` only because `old` rendered no Listener at all.
3. **`Listener.init` is not valid Ballerina.** A required parameter (`ListenerConfiguration config`)
   follows 14 defaultable parameters, and the flattened fields duplicate that same record. Real call
   sites use `check new (url = "...", auth = {...})`. `old` has the identical malformed shape for
   `MessageConsumer.init` and `MessageProducer.init`, so this is a shared renderer pattern, not new.
4. **`Listener`'s class-level documentation is lost.** `listener.bal:19-55` carries a 37-line doc
   with the transacted-session semantics and a full `@solace:ServiceConfig` queue-listener example.
   The render uses the `init` doc (`"Initialize a new listener with the given connection
   configuration."`) as the class doc and leaves `init` undocumented. Also dropped: `public` and
   `isolated` modifiers, and the fact that `Listener` is a listener object rather than a plain class
   (`class Listener`, methods rendered as bare `function`). Not a regression — `old` had none of it.
5. **Inaccuracies `new` inherits verbatim from `old`** (present in `new` regardless of `old`, all in
   the 785 non-diffed lines):
   - All defaulted record fields are rendered as optional with the default erased, e.g.
     `CertificateValidation.enabled` (`types.bal:98`: `boolean enabled = true`) → `boolean enabled?`;
     `TrustStore.format` (`types.bal:120`: `= JKS`) → `SslStoreFormat format?`; all 4
     `RetryConfiguration` fields (`types.bal:188-197`: `= 0/0/3/3.0`) → `?`;
     `SecureSocket.excludedProtocols` (`types.bal:179`: `= []`) → `?`.
   - Closed records (`record {| … |}`) are rendered as open `record { … }` for every type in
     `types.bal`, including `Message`, `ListenerConfiguration`, `ConsumerConfiguration`.
   - `nack(Message message, boolean requeue = false)` in both `Caller` and `MessageConsumer`; source
     is `requeue = true` (`caller.bal:49`, `message_consumer.bal:119`) and the rendered doc text on
     the very next lines says "If true, the message is requeued". Directly contradictory.
   - `SubscriptionConfiguration subscriptionConfig = {}` in `MessageConsumer.init`; the field is
     required (`types.bal:306`) and `{}` satisfies neither `QueueConfiguration` nor
     `TopicConfiguration`.
   - 10 doc-comment continuation lines lack the leading `#` (identical count in both files), e.g.
     new line 219 `If not specified, the default cipher suites for the JVM are used`, lines 243/246,
     284/287/288, 313, 375, 394, 415 — each makes the render non-compilable at that point.
   - `public type Service distinct service object {}` (`types.bal:31`) is rendered as
     `class Service { }`, an empty class, which misrepresents the service-object contract; the actual
     contract survives only inside the (correctly reproduced) doc comment above it.
   - `AuthConfiguration` is flattened from `BasicAuthConfiguration|KerberosConfiguration|OAuth2Configuration`
     to the 4 leaf records, and `SslStoreFormat`/`SslCipherSuite` are inlined as string literals
     instead of the `JKS`/`PKCS12`/cipher constants. Semantically equivalent, cosmetically off.

## 6. Coverage gaps vs. the library

**0 gaps.** All 52 public top-level declarations of the default module appear in both renders.
Script check: extracted `public (isolated )?(client )?(type|class|enum|const|annotation) <Name>` from
all 10 `.bal` files in `bala/.../modules/solace/` (52 declarations) and matched each against a
declaration pattern in each render → `missing in BOTH: []`, `present old, missing new: []`. Note that
in `old`, `Error` and `Listener` "match" only via their `// Unknown type:` placeholders — i.e. named
but empty; `new` supplies real definitions.

No submodule gap: the bala has exactly one module directory (`modules/solace`) and Central reports
`modules: ['solace']`, so the default module is the entire public API. The
`pkg.getDefaultModule()`-only extraction limitation costs this library nothing.

Non-public internals correctly excluded from both: `CommonConnectionConfiguration`,
`CommonConsumerConnectionConfiguration`, `CommonConsumerConfiguration`, `InternalMessage`,
`initListener`/`initConsumer`/`initProducer`/`externSend`, `convertPayload`, `prepareProperties`,
`validateConfigurations` (`validation.bal`), `setModule` (`init.bal`).

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `plugin_class: io.ballerina.lib.solace.compiler.SolaceCompilerPlugin`,
jar `solace-compiler-plugin-0.4.0.jar`. Source (7 classes: `SolaceCompilerPlugin`, `SolaceCodeAnalyzer`,
`SolaceServiceAnalysisTask`, `ConfigurationAnalysisTask`, `ServiceValidator`, `PluginUtils`,
`DiagnosticCode`) is validation-only — no code actions, no generated artifacts, no extra annotations.

11 diagnostics (`DiagnosticCode.java:23-36`), and how the render covers each:

| Code | Rule | Surfaced in `new`? |
|---|---|---|
| SOLACE_101 | service must carry `@solace:ServiceConfig` | Partly — annotation is listed in the Annotations section, but the Service template never shows `@solace:ServiceConfig { … }` attached to the service, so "mandatory" is not conveyed. Same in `old`. |
| SOLACE_102 | no resource methods in a `solace:Service` | No |
| SOLACE_103 | must declare `onMessage`, at most one optional `onError` | Partly — both methods shown, but neither is marked optional (`new` dropped the JSON `optional` flag; `old` had it wrong anyway) |
| SOLACE_104 | only `onMessage`/`onError` allowed | Implied by the template only |
| SOLACE_105/106/107 | `onMessage` = one `solace:Message` + optional `solace:Caller` | **Yes — new only.** `Required parameters: message` / `Optional parameters (may be omitted): caller` is exactly this rule; `old` showed neither |
| SOLACE_108 | `onError` takes exactly one `solace:Error` | Yes (signature) |
| SOLACE_109 | remote methods return something assignable to `error?` | Yes (`returns error?`) |
| SOLACE_201 | `queueName` required when queue is DURABLE | Yes, via doc text on `QueueConfiguration.queueName` / `QueueServiceConfiguration` |
| SOLACE_202 | `endpointName` required when topic is DURABLE | Yes, via doc text on `TopicConfiguration.endpointName` (though the render's broken `#` continuation, new line 313/375, mangles it) |

Nothing the plugin implies is *newly* absent in `new`; `new` closes one gap (SOLACE_105/107) that
`old` left open.

## 8. Other considerations

- Pre-1.0 library (`0.4.0`), not deprecated (`deprecated: null` from Central). Upstream already has a
  `v1.0.0` tag (`git ls-remote --tags` returns only `v0.4.0` and `v1.0.0`), so the pinned render is of
  an older pre-release line. Out of scope to change; noted for awareness.
- Built with `ballerinaVersion 2201.12.0`, `balaVersion 3.0.0`, `pullCount 13`.
- Size/token impact: +44 lines (+5.5%) for a full `Listener` class and 18 de-qualified refs — a good
  trade; de-qualification alone shortens 10 lines substantially.
- Doc quality of the library itself is high (every public field and method documented); the render's
  main fidelity losses are structural (defaults, closed records, `distinct`), not documentary.
- Neither render is compilable Ballerina (bare README prose at top level, 10 unprefixed doc
  continuation lines, malformed `init` parameter ordering). Equally true of both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 796, new 840 |
| `git ls-remote --tags .../module-ballerinax-solace` | `v0.4.0` → `29eb69a`, `v1.0.0` → `026d35b` |
| `git clone --depth 1 --branch v0.4.0`, then `git log --oneline -1` / `git describe --tags` | `29eb69a`, `v0.4.0`; `gradle.properties:3` `version=0.4.0` |
| `ls -R` bala | one module `modules/solace` with 10 `.bal` files (1078 lines total); `compiler-plugin/`, `docs/README.md`, `platform/java21/` (20 jars) |
| `grep -n '^// --- '` both renders | 6 markers each; Types at 169 in both, Client 608→645, Service 783→819, Annotations 793→834 |
| `grep -c '^// Unknown type:'` | old 2 (`Error` line 237, `Listener` line 606), new 0 |
| `grep -o 'ballerinax/solace:0\.4\.0:' \| wc -l` | old 17 (on 10 lines), new 0 |
| `grep -c 'ballerinax/solace:solace:'` | old 1, new 0 |
| `grep -c 'Additional Values'` renders / JSONs | render old 2 / new 0; JSON old 3 / new 0 |
| `diff -u old new \| grep -c '^@@'`; `^<` / `^>` counts | 11 hunks, 17 removed, 61 added |
| `cmp` on README block (lines 7–167) | identical; bala `docs/README.md` = 158 lines, fully present, tail matches |
| Python JSON top-level counts | both: typeDefs 57, clients 3, functions 0, services 1, annotations 1; typeDef name lists equal and same order |
| Full sorted JSON `unified_diff` (225 lines) | only the changes enumerated in §2/§4; `-displayName`, `-optional:false` ×2, `+baseType:"error"`, `+type:"Class"`, `-Additional Values` ×3, `-Caller.init`, 17 de-qualifications |
| `bala/.../errors.bal:17-18` | `public type Error distinct error;` |
| `bala/.../annotations.bal:17-21` | doc matches `new` verbatim |
| `bala/.../caller.bal:24-69` | no `init`; 4 remote methods `ack`, `nack(requeue = true)`, `'commit`, `'rollback` |
| `bala/.../listener.bal:56-121` | `public isolated class Listener`; init `(string url, *ListenerConfiguration config)`; 5 public methods + private `initListener` |
| `bala/.../types.bal:31`, `:96-102`, `:114-135`, `:179`, `:188-197`, `:200-222`, `:238-248`, `:250-253`, `:303-307` | Service object, CertificateValidation/TrustStore/KeyStore/RetryConfiguration defaults, Common*Configuration defaults (`messageVpn="default"`, `clientDescription="Ballerina Solace Connector"`, `connectTimeout=30.0`, `readTimeout=10.0`), ListenerConfiguration, ConsumerConfiguration required `subscriptionConfig` |
| `bala/.../message_consumer.bal:57-155`, `message_producer.bal:47-116` | method sets match both renders; `nack` default `true` |
| Coverage script (52 public decls × 2 renders) | `missing in BOTH: []`, `present old, missing new: []` |
| `grep -cE '^[A-Za-z`(][^;{}]*$'` after line 167 | 10 in old, 10 in new (unprefixed doc continuations) |
| `grep -n 'nack('` both renders | 4 hits, all `requeue = false` |
| `DiagnosticCode.java:23-36` | 11 diagnostics SOLACE_101…109, 201, 202 |
| `curl api.central.ballerina.io/.../ballerinax/solace/0.4.0` | not deprecated, `modules: ['solace']`, ballerinaVersion 2201.12.0 |
| `OLD_AND_NEW_DIFFS/solace_diff.md` cross-check | its figures (796/840, +61/−17, 11 hunks, 2→0 unknown, 18→0 qualified refs, 7 added / 0 removed declarations) all reproduce against the files |

## 10. Caveats and unverified items

- The compiler-plugin jar was not decompiled; plugin behaviour is read from the `v0.4.0` Java source
  in the clone, which the bala's `compiler-plugin.json` names as the same plugin id/version. The bala
  ships only the jar, so bala-vs-source equality for the plugin is unverified (all `.bal` sources
  were compared and used the bala as authority).
- `onError`'s parameter name (`solaceError`) and widened return type (`error?` vs the source's
  `solace:Error?`) originate from LS trigger metadata rather than the library source; I did not read
  the trigger-metadata files in the two `ballerina-vscode` checkouts to confirm which side supplies
  them. Both renders agree, so it cannot be a `new`-side regression.
- Whether the annotation `displayName` field is consumed by any downstream renderer is unverified; I
  confirmed only that it does not appear in either `.bal.txt`.
- No render was regenerated; I audited the committed `old`/`new` artifacts as given.
- I did not attempt to compile either render (they are illustrative stubs with README prose at top
  level, so compilation is not expected to succeed on either side).

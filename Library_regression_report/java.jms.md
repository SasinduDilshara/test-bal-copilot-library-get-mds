# ballerinax/java.jms 1.2.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/java.jms` |
| Pinned version | `1.2.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-java.jms |
| Tag reviewed | `v1.2.1` (annotated tag → commit `38b6ab7`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/java.jms/1.2.1/java21` |
| Old render | `505` lines |
| New render | `558` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module package (`export: ["java.jms"]`, default module only), so there is no submodule
coverage gap. The bala's 10 `.bal` files are byte-identical to upstream `v1.2.1` (`diff` on all
10 → SAME), so the bala and GitHub agree and every finding is attributable to the pipeline.

`new` is strictly better. It recovers the two types that `main` degraded to `// Unknown type:`
(`Error`, `Listener` — the latter with all 6 of its methods and their docs), removes a fabricated
`Caller` constructor that does not exist in the source, strips 4 version-qualified type references
(`ballerinax/java.jms:1.2.1:Error?` → `Error?`), and fixes a mis-qualification where `main`
printed `Session.createProducer`/`createConsumer` as `remote function` although both are plain
`public isolated function` in the source. Nothing present and correct in `old` is absent from
`new`: all 9 deleted lines are either the placeholder comments, the bogus `Caller.init`, or the
5 lines replaced by more accurate versions of themselves.

The remaining inaccuracies (wrong parameter defaults, required-after-defaultable parameter order,
defaultable record fields shown as optional, `distinct` dropped) are present identically in the
two JSONs and therefore pre-date spec v2; they are recorded in §5, not §4.

## 2. Change inventory

Line counts (`wc -l`): old `505`, new `558`. `diff old new`: `62` added lines (`^>`), `9` removed
lines (`^<`), 8 hunks.

Signals:

| Signal | old | new | command |
|---|---|---|---|
| `// Unknown type:` | 2 | 0 | `grep -c '^// Unknown type:'` |
| Version/module-qualified type refs | 5 lines | 0 | `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:\|jms:jms:'` |
| `// --- ` section markers | 4 | 4 | `grep -n '^// --- '` |
| README block | lines 8–105 (98 lines) | lines 8–105 (98 lines), byte-identical | `diff <(sed -n 1,107p old) <(sed -n 1,107p new)` → identical |

### Added (7 declarations)

| Kind | Declaration | new render line | replaces in old |
|---|---|---|---|
| type | `type Error error;` | 191 | `// Unknown type: Error` (old:189) |
| class | `class Listener { … }` | 348–386 | `// Unknown type: Listener` (old:330) |
| member fn | `Listener.init(...)` | 349 | — |
| member fn | `Listener.attach(Service 'service, string[]\|string\|() name = ())` | 356 | — |
| member fn | `Listener.detach(Service 'service)` | 363 | — |
| member fn | `Listener.'start()` | 370 | — |
| member fn | `Listener.gracefulStop()` | 377 | — |
| member fn | `Listener.immediateStop()` | 384 | — |

(6 member functions + 2 top-level = the 7 "declarations added" the mechanical diff counts, which
collapses `Listener` and its constructor into one entry.)

### Removed (1 declaration)

- `Caller.init() returns jms:jms:Caller;` (old:337). Not a regression — see §3.

### Modified (6 declarations)

| Declaration | old | new |
|---|---|---|
| `Connection.init` (new:413) | `… returns ballerinax/java.jms:1.2.1:Error?` | `… returns Error?` |
| `MessageConsumer.init` (new:448) | same qualified form | `… returns Error?` |
| `MessageProducer.init` (new:481) | same qualified form | `… returns Error?` |
| `Session.init` (new:506) | same qualified form | `… returns Error?` |
| `Session.createProducer` (new:526) | `remote function createProducer(…)` | `function createProducer(…)` |
| `Session.createConsumer` (new:536) | `remote function createConsumer(…)` | `function createConsumer(…)` |

Unchanged: all 12 `const string` enum-member declarations, `ConnectionConfiguration`,
`DestinationType`, `Destination`, `Message`, `TextMessage`, `MapMessage`, `BytesMessage`,
`ConsumerType`, `ConsumerOptions`, `Service`, `MessageListenerConfigurations`,
`AcknowledgementMode`, and all 20 client remote/normal functions other than the 6 above.

### JSON-level inventory

Both JSONs have identical top-level shape: `typeDefs` 26, `clients` 5, `functions` 0,
`services` 0, `annotations` 0; `readme`, `description`, `name` byte-identical. A recursive
deep-diff produced exactly these deltas:

- `clients[0].functions` (Caller): length `4 → 3` (the phantom `Constructor` dropped).
- `clients[1..4].functions[0].return.type.name`: `"ballerinax/java.jms:1.2.1:Error?" → "Error?"`.
- `typeDefs[15]` (`Error`): `baseType: "error"` **added** (old had only name/description/type).
- `typeDefs[25]` (`Listener`): `type: "Class"` **added**; its `functions[0].return.type.name`
  de-qualified.

So the `remote → plain` fix in `Session` is renderer-side: both JSONs already carry
`"type": "Normal Function"` for `createProducer`/`createConsumer`; `main`'s renderer printed
`remote` for every method of a `client class`, spec v2 honours the function kind.

## 3. Correctness against library source

Verified against the bala module (identical to upstream `v1.2.1`).

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `type Error error;` | `errors.bal:18` `public type Error distinct error;` | exists; `distinct` lost (§5.1) |
| `class Listener` | `message_listener.bal:36` `public isolated class Listener {` | exists |
| `Listener.init(… MessageListenerConfigurations listenerConfig) returns Error?` | `message_listener.bal:57` `public isolated function init(*MessageListenerConfigurations listenerConfig) returns Error?` | exists; included-record expansion matches the pipeline's convention already used for `Connection.init` in `old` |
| `Listener.attach(Service 'service, string[]\|string\|() name = ()) returns Error\|()` | `message_listener.bal:71` `attach(Service 'service, string[]\|string? name = ())` | exact (`?`→`\|()` is the renderer's normalization) |
| `Listener.detach(Service 'service)` | `message_listener.bal:82` | exact |
| `Listener.'start()` | `message_listener.bal:90` | exact |
| `Listener.gracefulStop()` | `message_listener.bal:99` | exact |
| `Listener.immediateStop()` | `message_listener.bal:109` | exact |
| `Session.createProducer(Destination\|() destination = ()) returns MessageProducer\|Error` — **no** `remote` | `session.bal:55` `public isolated function createProducer(Destination? destination = ()) returns MessageProducer\|Error` — not remote | `new` correct, `old` wrong |
| `Session.createConsumer(...) returns MessageConsumer\|Error` — **no** `remote` | `session.bal:69` `public isolated function createConsumer(*ConsumerOptions consumerOptions)` — not remote | `new` correct, `old` wrong |
| `Caller` has **no** `init` | `caller.bal:20–49`: `public isolated client class Caller` declares only 3 remote functions; no `init` | `new` correct; `old`'s `function init() returns jms:jms:Caller;` was invented and additionally malformed (double module prefix, and a constructor cannot "return" the class type) |
| 4 × `init(...) returns Error?` | `connection.bal:33`, `message_consumer.bal:51`, `message_producer.bal:23`, `session.bal:22` all `returns Error?` | `new` correct; `old`'s `ballerinax/java.jms:1.2.1:Error?` is not a valid type reference in a consumer's code |
| `Listener` docs (the `new(...)` usage example) | `message_listener.bal:39–53` verbatim | exact, including the fenced `ballerina` block |

Also spot-checked unchanged material: `TextMessage` (new:226–241) correctly flattens
`*Message` inclusion from `message.bal:51–54` + `message.bal:33–46`; `AcknowledgementMode`
members match `session.bal:109–126`; `ConsumerOptions` fields match `message_consumer.bal:40–46`.

## 4. Regressions

**None found.**

Basis: the removed-line set is exactly 9 lines, enumerated in full by
`diff old new | grep '^<'`, and each was individually resolved:

1. `// Unknown type: Error` → replaced by a real definition.
2. `// Unknown type: Listener` → replaced by a real 39-line class.
3. `function init() returns jms:jms:Caller;` → correctly deleted; no such member exists in
   `caller.bal`.
4–7. four `init(...) returns ballerinax/java.jms:1.2.1:Error?` → same signatures with a valid
   `Error?` return.
8–9. `remote function createProducer/createConsumer` → same signatures with the correct
   (non-`remote`) qualifier per `session.bal:55,69`.

Additional negative checks that came back clean:
- Declaration sets compared via `grep -nE '^(public )?(client )?(isolated )?(function|type|class|enum|const|annotation|listener|service)'`: `new` is a strict superset of `old` (32 vs 30 top-level entries).
- Member-function sets compared via `grep -nE '^    (remote )?function '`: 26 in `old`, 31 in `new`; every `old` member name survives, with identical parameter lists and defaults except the 6 intended modifications.
- README block byte-identical, and complete against `docs/README.md` (97 source lines, no truncation — render ends on the same closing fence as the file).
- Section markers unchanged (4 → 4), so no section was lost.
- No non-ASCII bytes introduced (`grep -nP '[^\x00-\x7F]'` on `new` → no matches), no mojibake.
- No new `// Unknown type:` lines, no empty class/record bodies introduced.

## 5. Issues in `new` (independent of `old`)

All items below except 5.1 and 5.4 are byte-identical in the two renders or trace to JSON fields
that the deep-diff showed unchanged — i.e. they are extractor-side and pre-date spec v2.

1. **`distinct` dropped from `Error`.** `new:191` emits `type Error error;`; source is
   `public type Error distinct error;` (`errors.bal:18`). The JSON carries
   `{"type":"Error","baseType":"error"}` with no distinctness flag, so the loss is in the
   extractor. Impact is low (assignability, not surface API), but a model told to write
   `distinct` subtypes of `jms:Error` gets no signal. *New-only in the render because `old` had
   no `Error` definition at all — not a regression.*
2. **Wrong parameter defaults, invented by the extractor.** Both JSONs carry
   `"default": "0"` for `MessageConsumer.receive.timeoutMillis` (source default `10000`,
   `message_consumer.bal:84`) and `"default": "\"DUPS_OK_ACKNOWLEDGE\""` for
   `Connection.createSession.ackMode` (source default `AUTO_ACKNOWLEDGE`,
   `connection.bal:50`). The rendered `receive(int timeoutMillis = 0)` (new:455) and
   `createSession(AcknowledgementMode ackMode = "DUPS_OK_ACKNOWLEDGE")` (new:420) will mislead
   an LLM into emitting a non-blocking receive and the wrong acknowledgement mode. Identical in
   `old` (old:402, old:367).
3. **Non-compiling signatures: required parameter after defaultable parameters.** 4 sites in
   `new` — `Connection.init` (413), `MessageConsumer.init` (448), `Session.createConsumer` (536),
   `Listener.init` (349) — all end with a non-defaulted `…Configuration/…Options` parameter after
   defaulted ones. This is invalid Ballerina. 3 of the 4 are verbatim from `old`; the
   `Listener.init` occurrence is new only because `Listener` was previously not rendered at all.
4. **Fabricated defaults on required record fields in `Listener.init`** (new:349):
   `ConnectionConfiguration connectionConfig = {initialContextFactory: "", providerUrl: ""}` and
   `ConsumerOptions consumerOptions = {destination: {'type: "TEMPORARY_TOPIC"}}`. In
   `MessageListenerConfigurations` (`message_listener.bal:29–33`) both fields are **required**
   with no defaults, and `ConsumerOptions.destination` (`message_consumer.bal:41`) is required
   with no default either. Rendering them as defaulted implies `new jms:Listener()` is valid.
   Same synthesis already applied to `Connection.init`/`MessageConsumer.init` in `old`.
5. **Module-private constructors exposed as public API.** `Session.init`
   (`session.bal:22`, no `public`), `MessageConsumer.init` (`message_consumer.bal:51`) and
   `MessageProducer.init` (`message_producer.bal:23`) are not public, yet appear in both renders
   as callable `function init(...)`. Consumers must go through
   `connection->createSession()` / `session.createConsumer()` / `session.createProducer()`.
   Shared with `old`.
6. **Defaultable record fields rendered as optional (`?`) instead of showing the default.**
   `ConnectionConfiguration.connectionFactoryName` and `.properties` (new:163,169 — source
   defaults `"ConnectionFactory"` and `{}`, `connection.bal:99,101`);
   `ConsumerOptions.'type`, `.messageSelector`, `.noLocal` (new:294,299,302 — source defaults
   `DEFAULT`, `""`, `false`, `message_consumer.bal:41,43,44`);
   `MessageListenerConfigurations.acknowledgementMode` (new:320 — source default
   `AUTO_ACKNOWLEDGE`, `message_listener.bal:31`). Shared with `old`.
7. **Malformed doc comment: continuation lines emitted without the `#` prefix.** Inside
   `ConsumerOptions` in both renders, `An empty string indicates that there is no message
   selector for the durable subscription.` and `with the same client identifier, will not be
   added to the durable subscription.` sit at column 0 with no `#`, breaking the record body
   syntactically (1 occurrence each, confirmed by `grep -c` = 1 in both files).
8. **`Service` mis-rendered.** `public type Service distinct service object { … }`
   (`message_listener.bal:20`) becomes `class Service { }` (new:309) in both renders. The
   service-object nature is lost and the render gives no hint that an implementor writes
   `remote function onMessage(jms:Message message, jms:Caller caller) returns error?` — that
   contract is only discoverable from the README example at new:98 and from the commented-out
   line `message_listener.bal:21`. Shared with `old`.
9. **`Listener` class doc replaced by its constructor doc.** The JSON `typeDefs[25].description`
   (identical in both files) is the `init` doc block; the class-level doc
   `# Represents a JMS consumer listener.` (`message_listener.bal:35`) is absent from the render.
   Extractor-side.
10. **Structural fidelity losses, both sides.** Closed records `record {| |}` rendered as open
    `record { }` (`Destination`, `ConnectionConfiguration`, `ConsumerOptions`, `TextMessage`,
    `MapMessage`, `BytesMessage`, `MessageListenerConfigurations`); `readonly &` intersection
    lost on `Destination` (`destination.bal:21`); enum members reversed relative to source
    (`DestinationType` renders `TEMPORARY_TOPIC, TOPIC, TEMPORARY_QUEUE, QUEUE`; source order is
    `QUEUE, TEMPORARY_QUEUE, TOPIC, TEMPORARY_TOPIC`), and each member is additionally duplicated
    as a bare `const string` at new:111–152 with no `= "VALUE"` inside the `enum` body.
11. **Per-parameter documentation dropped for all functions.** Source `# + param - …` lines are
    present in the JSON (`parameters[].description`) but the render emits only the function-level
    description, so e.g. `Listener.attach`'s `+ name - Name of the service` never reaches the
    output. Shared with `old`.

## 6. Coverage gaps vs. the library

`grep -nE '^public ' bala/modules/java.jms/*.bal` yields **19** public top-level declarations.
Mapping to `new`:

| Public symbol | source | in `new`? | in `old`? |
|---|---|---|---|
| `Destination` | destination.bal:21 | yes (183) | yes |
| `DestinationType` | destination.bal:27 | yes (173) | yes |
| `Caller` | caller.bal:20 | yes (390) | yes |
| `Error` | errors.bal:18 | yes (191) | **no** |
| `Connection` | connection.bal:20 | yes (412) | yes |
| `ConnectionConfiguration` | connection.bal:96 | yes (157) | yes |
| `Service` | message_listener.bal:20 | yes (309) | yes |
| `MessageListenerConfigurations` | message_listener.bal:29 | yes (315) | yes |
| `Listener` | message_listener.bal:36 | yes (348) | **no** |
| `Message` | message.bal:33 | yes (196) | yes |
| `TextMessage` | message.bal:51 | yes (226) | yes |
| `MapMessage` | message.bal:59 | yes (246) | yes |
| `BytesMessage` | message.bal:67 | yes (266) | yes |
| `ConsumerType` | message_consumer.bal:20 | yes (284) | yes |
| `ConsumerOptions` | message_consumer.bal:40 | yes (294) | yes |
| `MessageConsumer` | message_consumer.bal:49 | yes (447) | yes |
| `MessageProducer` | message_producer.bal:20 | yes (480) | yes |
| `Session` | session.bal:20 | yes (505) | yes |
| `AcknowledgementMode` | session.bal:109 | yes (325) | yes |

**Coverage gaps in `new`: 0.** `old` had 2 (`Error`, `Listener`).

Member-level: all 14 `remote function`s and all 8 `public isolated function`s of the public
classes appear in `new`. Private helpers (`externInit`, `externSend`, `externSendTo`,
`validateConsumerOptions`, `createJmsMessage`, module-level `init`/`setModule`/`getJmsMessage`/
`constructJmsMessage`/`externWrite*`/`externSet*`) are correctly excluded — the JSON's
top-level `functions` array is empty on both sides, which is right because every module-level
function in this package is non-public.

**Submodule-only API: none.** `package.json` `"export": ["java.jms"]`, `modules/` contains only
`java.jms`, and Central's module list has a single entry. The `getDefaultModule()`-only
extraction limitation therefore costs this library nothing.

## 7. Compiler plugin

**No compiler plugin exists.** `ls` of the bala root shows only
`bala.json  dependency-graph.json  docs  modules  package.json  platform` — no
`compiler-plugin/` directory and no `compiler-plugin.json`. Upstream `v1.2.1` has no
`compiler-plugin`/`*-compiler-plugin` directory either (`find src -maxdepth 2 -iname
'*compiler-plugin*'` → no matches); `native/` contains only runtime code under
`io/ballerina/stdlib`. Consequently there are no plugin-contributed code actions, validations,
annotations, or generated artifacts, and nothing plugin-implied is missing from the render.

Worth noting as the practical consequence: because there is no compiler plugin, the `jms:Service`
contract (`remote function onMessage(jms:Message, jms:Caller)`) is enforced nowhere in the
package metadata and, as noted in §5.8, is not in the render's type surface either. Both sides
share this.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/java.jms/1.2.1`: `deprecateMessage: ""`,
  no `deprecated: true`, `pullCount: 619`, `createdDate` 2026-04-06, `balaVersion: "3.0.0"`.
- **Stable version, `graalvmCompatible: true`**, distribution `2201.11.0`, platform `java21`.
- **Repo URL discrepancy (benign).** `package.json`/`Ballerina.toml` declare
  `source_repository = https://github.com/ballerina-platform/module-ballerina-java.jms`, but the
  live repo (and the one carrying the `v1.2.1` tag) is
  `module-ballerinax-java.jms`. The manifest's `repo` is the correct one.
- **Size / tokens.** `new` is +53 lines (+10.5%) for 2 recovered types and 6 recovered methods —
  a good exchange. Absolute size (558 lines) is small; no token-budget concern.
- **Doc quality.** Source docs are good and the render preserves function-level descriptions with
  their `ballerina` usage examples. Two source typos ride through into both renders unchanged:
  `threre` (connection.bal:60,72,82) and `jsm:Error` (message_consumer.bal:83,94). Not pipeline
  faults.
- **Render is not compilable Ballerina** on either side (§5.3, §5.7). That is inherent to this
  format, but the required-after-defaultable pattern is the kind of thing an LLM will copy.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/… new/…` | 505 / 558 |
| `diff old new \| grep -c '^>'` / `'^<'` | 62 / 9 |
| `diff old new \| grep '^<'` (full listing) | 9 lines, all enumerated in §4 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:\|jms:jms:'` old / new | 5 lines / 0 |
| `grep -n '^// --- '` old / new | 4 markers each, at 7/106/108/333 and 7/106/108/387 |
| `diff <(sed -n 1,107p old) <(sed -n 1,107p new)` | identical (README block unchanged) |
| `wc -l bala/docs/README.md` vs rendered block | 97 vs 98 lines (README + blank); render ends on same closing fence → not truncated |
| `grep -nP '[^\x00-\x7F]' new` | no matches |
| `ls -R` of bala | `modules/java.jms` only; 10 `.bal` files; no `compiler-plugin/` |
| `cat bala/package.json` | `export: ["java.jms"]`, `ballerina_version 2201.11.0`, `platform java21`, `graalvmCompatible true` |
| `git ls-remote --tags module-ballerinax-java.jms` | `v1.2.1` present (annotated, `38b6ab7`) |
| `git clone --depth 1 --branch v1.2.1` + `git describe --tags` | `v1.2.1`, HEAD `38b6ab7 [Gradle Release Plugin] - pre tag commit: 'v1.2.1'` |
| `diff bala/modules/java.jms/<f>.bal src/ballerina/<f>.bal` ×10 | SAME for all 10 files |
| `find src -maxdepth 2 -iname '*compiler-plugin*'` | no matches |
| `grep -nE '^public ' bala/modules/java.jms/*.bal` | 19 public top-level declarations (table in §6) |
| `grep -nE '^    (public )?(isolated )?(remote )?function '` on bala | 38 member functions; 22 public/remote, 16 private |
| `grep -nE '^    (remote )?function '` old / new render | 26 / 31 member functions |
| Recursive JSON deep-diff old vs new | exactly 4 delta groups (§2 "JSON-level inventory") |
| JSON `typeDefs` / `clients` / `functions` / `services` / `annotations` counts | 26/5/0/0/0 on both sides |
| JSON `Session.createProducer.type`, `.createConsumer.type` | `"Normal Function"` in **both** → `old`'s `remote` was a renderer bug |
| JSON `MessageConsumer.receive.parameters[0].default` | `"0"` in both; source `10000` (message_consumer.bal:84) |
| JSON `Connection.createSession.parameters[0].default` | `"\"DUPS_OK_ACKNOWLEDGE\""` in both; source `AUTO_ACKNOWLEDGE` (connection.bal:50) |
| JSON `typeDefs[15]` (`Error`) | old `{name,description,type}`; new adds `baseType:"error"`; neither records `distinct` |
| JSON `typeDefs[25]` (`Listener`) | old lacks `type`; new has `type:"Class"`; `description` identical (= init doc) |
| JSON `clients[0]` (`Caller`) functions | old 4 (incl. phantom `Constructor` returning `jms:jms:Caller`); new 3 |
| `grep -c '^An empty string'` / `'^with the same client'` old & new | 1 each in both files (malformed doc lines, shared) |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/java.jms/1.2.1` | not deprecated; single module `java.jms`; pullCount 619 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims about non-compiling constructs (§5.3, §5.7) are from
  reading the rendered text against the Ballerina grammar, not from a `bal build` run.
- The pipeline itself was not re-executed; both JSONs and both `.bal.txt` files are taken as
  given. The attribution of each delta to "extractor" vs. "renderer" is inferred from the JSON
  deep-diff (e.g. `remote → plain` is renderer-side because the JSON `type` field is unchanged),
  which is strong but indirect evidence.
- `distinct`-ness of `Error` and the `distinct service object` shape of `Service` are absent from
  both JSONs; I confirmed they are absent from the JSON but did not inspect the Java extractor
  source to confirm the model has no field capable of carrying them.
- Whether `Listener.init`'s fabricated record defaults come from the extractor or the renderer is
  **unverified in the code**; I only established that the JSON `default` strings are byte-identical
  between `old` and `new`, so the behaviour is at least unchanged by spec v2.
- Ordering of enum members (§5.10) is reversed relative to source in both renders; I did not
  determine whether this is deliberate or incidental.

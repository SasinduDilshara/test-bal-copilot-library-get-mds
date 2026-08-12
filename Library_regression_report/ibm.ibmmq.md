# ballerinax/ibm.ibmmq 1.4.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ibm.ibmmq` |
| Pinned version | `1.4.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ibm.ibmmq |
| Tag reviewed | `v1.4.4` (commit `f8e5cb05a1b43afd4e0551f06268961a9ef520ba`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ibm.ibmmq/1.4.4/java21` |
| Old render | `979` lines |
| New render | `1033` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better. All 14 removed lines are placeholders, malformed type references, or
bogus constructor lines; not one line of genuine API content is lost. `new` recovers three
declarations that `old` degraded to `// Unknown type:` comments (`Error`, `Listener`,
`QueueManager`), fills in `Destination`'s three remote methods, adds the previously-absent
`ServiceConfig` annotation, and strips 7 version-qualified type references plus 3 malformed
`ibmmq:ibmmq:X` return types.

Critically, the JSON on both sides is nearly identical (129 typeDefs, 3 clients on both) — the
`Listener`/`QueueManager` function data was already fully present in the `old` JSON and was lost
only at render time. So this is a pure renderer fix, and the extractor-side inaccuracies it now
exposes (invented parameter defaults, included-record parameter flattening) pre-date `new`.

## 2. Change inventory

Line counts: `old` 979, `new` 1033 (+68 added, −14 removed, 10 hunks).

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (`org/mod:x.y.z:Type`) | 7 | 0 |
| `ibmmq:ibmmq:` malformed refs | 3 | 0 |
| `// --- section ---` markers | 4 | 5 |
| README section (lines 7–179) | 173 lines | 173 lines, byte-identical |

JSON-level: `typeDefs` 129 → 129, `clients` 3 → 3, `functions` 0 → 0, `services` 0 → 0,
`annotations` **0 → 1**. Nine typeDefs differ; the deltas are `Destination` (+`functions`,
+`isClient`), `Error` (+`baseType`), `Listener`/`QueueManager` (+`"type":"Class"`), and five
records/unions whose only change is type-reference spelling (`Header`, `MQIIH`, `MQRFH2`,
`Message`, `ServiceConfiguration`).

**Declarations added in `new` (5 top-level + 11 members):**

| Kind | Name | Note |
|---|---|---|
| type | `Error` | was `// Unknown type: Error` |
| class | `Listener` | was `// Unknown type: Listener`; +6 members (`init`, `attach`, `detach`, `'start`, `gracefulStop`, `immediateStop`) |
| class | `QueueManager` | was `// Unknown type: QueueManager`; +4 members (`init`, `accessQueue`, `accessTopic`, `disconnect`) |
| annotation | `ServiceConfig` | new `// --- Annotations ---` section |
| client class | `Destination` | replaces empty `class Destination`; +3 remote methods (`put`, `get`, `close`) |

**Declarations removed in `new` (1):** `class Destination` — superseded by `client class Destination`
with a populated body. Not a loss.

**Member declarations removed in `new` (3):** `function init() returns ibmmq:ibmmq:Caller;`,
`... ibmmq:ibmmq:Queue;`, `... ibmmq:ibmmq:Topic;` from the `Caller`/`Queue`/`Topic` client classes.
These were synthesized implicit constructors with a malformed doubly-qualified return type; none of
the three classes declares a `public init` in the source. Removal is a fix, not a loss.

**Type references corrected in `new` (7 lines):**
`ballerinax/ibm.ibmmq:1.4.4:QueueConfig|...:TopicConfig` → `QueueConfig|TopicConfig`;
`table<ballerinax/ibm.ibmmq:1.4.4:MQRFH2Field>` → `table<MQRFH2Field>`;
`ballerina/lang.string:0.0.0:Char` ×3 → `string:Char`;
`type Header ballerinax/ibm.ibmmq:1.4.4:MQRFH2|...` → `type Header MQRFH2|MQRFH|MQCIH|MQIIH`;
`map<ballerinax/ibm.ibmmq:1.4.4:Property>` → `map<Property>`.

## 3. Correctness against library source

Every addition in `new` verified against the bala (authoritative) and cross-checked against the
`v1.4.4` clone; the two agree.

| `new` render | Source | Verdict |
|---|---|---|
| `type Error error<ErrorDetails>;` (l.912) | `errors.bal:18` `public type Error distinct error<ErrorDetails>;` | Exists; `distinct` dropped (§5) |
| `class Listener` + `attach(Service s, string[]\|string\|() name = ())`, `detach(Service s)`, `'start()`, `gracefulStop()`, `immediateStop()` all `returns Error\|()` | `listener.bal:20,33,40,46,52,58` | Exact match (5/5 signatures) |
| `class QueueManager` + `accessQueue(string queueName, int options) returns Queue\|Error`, `accessTopic(string topicName, string topicString, OPEN_TOPIC_OPTION openTopicOption, int options) returns Topic\|Error`, `disconnect() returns Error\|()` | `queue_manager.bal:20,46,63,72` | Exact match (3/3) |
| `client class Destination` + `put(Message message, int options = 0) returns Error\|()`, `get(...) returns Message\|Error\|()`, `close() returns Error\|()` | `destination.bal:20–26` | Members and `put` default `0` correct; `get` shape flattened (§5) |
| `public annotation ServiceConfiguration ServiceConfig on service;` | `types.bal:97` `public annotation ServiceConfiguration ServiceConfig on service;` | Exact match |
| `type ServiceConfiguration QueueConfig\|TopicConfig;` | `types.bal:94` | Exact match |
| `type Header MQRFH2\|MQRFH\|MQCIH\|MQIIH;` | `types.bal:103` | Exact match |
| `map<Property> properties?;` | `types.bal:216` | Exact match |
| `table<MQRFH2Field> key(folder,field) fieldValues?;` | `types.bal:263` `table<MQRFH2Field> key(folder, 'field) fieldValues = table [];` | Type ref now correct; `'field` quoting and `= table []` default still lost (shared with `old`) |
| `string:Char tranState?/commitMode?/securityScope?` | `types.bal:396–398` | Type ref now correct; defaults `" "`, `"0"`, `"C"` still lost (shared with `old`) |
| `type OPEN_TOPIC_OPTION 1\|2;` | `types.bal:100` = `OPEN_AS_SUBSCRIPTION\|OPEN_AS_PUBLICATION`, `constants.bal:18,21` = 1, 2 | Correct (values inlined) |
| `type SslCipherSuite "SSL_..."\|…` (34 members, l.769) | `types.bal` `SslCipherSuite` | Present in both renders |

No invented symbols: all 125 public declarations extracted from the bala's default module map onto
render content (see §6).

## 4. Regressions

**None found.**

Checks performed to conclude this:

1. Full unified diff reviewed line by line. All 14 removed lines enumerated in §2 — 3 placeholders,
   3 bogus `ibmmq:ibmmq:` constructors, 1 empty `class Destination` header, 7 malformed
   version-qualified type refs. Each has a strictly better replacement in `new`.
2. Declaration-set diff: `diff <(grep -oE '^(public )?(isolated )?(client )?(function|type|class|enum|const|annotation) [^ (]+' old | sort) <(… new | sort)` → only additions (`class Listener`, `class QueueManager`, `client class Destination`, `public annotation ServiceConfiguration`, `type Error`) and the one supersession (`class Destination`).
3. JSON set comparison: `set(old typeDefs) - set(new typeDefs)` is **empty**. No typeDef lost.
4. Client method comparison: `Caller` old `[init, acknowledge, 'commit, 'rollback]` → new `[acknowledge, 'commit, 'rollback]`; `Queue` old `[init, put, get, close]` → new `[put, get, close]`; `Topic` old `[init, put, get, close, send]` → new `[put, get, close, send]`. Only the synthetic `init` dropped; all real remote methods, their parameters, defaults, and doc comments are byte-identical between sides.
5. README section (render lines 7–179) diffs clean — no doc content lost.
6. `Queue.put`/`Queue.get`/`Topic.put`/`Topic.get`/`Topic.send` parameter tuples compared at JSON level between sides — identical, including defaults and `optional` flags.
7. No new malformed syntax introduced into any declaration that `old` already rendered correctly.

## 5. Issues in `new` (independent of `old`)

Six accuracy issues. All are extractor-side or renderer-shape defects that also exist in `old`'s
JSON; they become *visible* in `new` only because `new` now renders the declarations at all.

1. **Non-compiling `init` signature on `Listener` and `QueueManager`** (l.895, l.921). Source is
   `public isolated function init(*QueueManagerConfiguration configurations) returns Error?`
   (`listener.bal:25`, `queue_manager.bal:29`). The render flattens the included record into
   individual parameters **and** keeps a trailing `QueueManagerConfiguration configurations` with no
   default — a required parameter after defaultable ones, which Ballerina rejects. Identical JSON on
   both sides (`configurations` has `optional:true` but no `default`), so the renderer omits the
   `=`. Pre-existing pattern: `old` already emitted it for `Queue.get`/`Topic.get`.
2. **Invented defaults for required and optional fields.** `QueueManagerConfiguration` declares
   `string name;`, `string host;`, `string channel;` as *required* with no default
   (`types.bal:131–140`), yet the render shows `name = ""`, `host = ""`, `channel = ""`. Likewise
   `userID?`, `password?`, `secureSocket?`, `sslCipherSuite?` are optional with no defaults but
   render as `= ""`, `= {cert: {path: "", password: ""}}`, `= "SSL_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA"`.
   An LLM reading this would believe `new ibmmq:QueueManager()` compiles. The synthetic defaults are
   present verbatim in the **old** JSON too — extractor-side, not introduced by spec v2.
3. **`Destination.get` flattened the same way** (l.894): source is
   `remote function get(*GetMessageOptions getMessageOptions) returns Message|Error?`
   (`destination.bal:23`), rendered as
   `get(int options = 0, int waitInterval = 10, MatchOptions matchOptions = {}, GetMessageOptions getMessageOptions)`.
   Same required-after-defaultable defect. (Note the `waitInterval = 10` here is *correct* vs
   `types.bal:174`, whereas `Queue.get`/`Topic.get` show `waitInterval = 0` on **both** sides —
   a shared inaccuracy, not a `new` regression.)
4. **`distinct` dropped.** `type Error error<ErrorDetails>;` loses `distinct` (`errors.bal:18`);
   `client class Destination` loses it too (`destination.bal:20`). `grep -c distinct new` = 1, and
   that single hit is inside a doc comment.
5. **`Destination` rendered as a class, not an object type.** Source is
   `public type Destination distinct client object { … };` — a type descriptor that `Queue` and
   `Topic` include via `*Destination`. Rendering `client class Destination { … }` implies it is
   directly instantiable and hides the inclusion relationship. `old` had the same misclassification
   (`"type":"Class"` in both JSONs), so this is not new — only the body is.
6. **Class-level docs replaced by the constructor's doc.** `Listener`'s render description is
   "Initializes the IBMMQ listener." (the `init` doc); the actual class doc, "Represents an IBMMQ
   Listener endpoint that can be used to receive messages from an IBMMQ queue."
   (`listener.bal:19`), is absent. Same for `QueueManager` (`queue_manager.bal:19`, "Represents an
   IBM MQ queue manager."). Present in the `old` JSON `description` field as well.

Cosmetic, not counted above: `public annotation ServiceConfiguration ServiceConfig on service;` is
the only line in the whole render carrying a `public` qualifier; every other declaration omits
visibility and `isolated`. Also `Listener`/`QueueManager`/`Destination` members render without
`isolated`, and `Listener.init` is not marked `public`.

## 6. Coverage gaps vs. the library

**Zero.** All 125 public declarations extracted from the bala's default module
(`modules/ibm.ibmmq/*.bal`) resolve to content in the `new` render.

`old` had exactly **1** gap: the `ServiceConfig` annotation, which `new` closes.

Submodules: none. `package.json` `"export": ["ibm.ibmmq"]` and `modules/` contains only
`ibm.ibmmq`, so the default-module-only extraction limitation costs this library nothing.

**Shared usability gap (inherent to the library, present in both renders and not a render defect):**
`Service` is declared `public type Service distinct service object {};` (`types.bal:20`) — an empty
service object type. Both renders therefore emit `class Service { }` with no methods. The required
service contract (`remote function onMessage(ibmmq:Message message[, ibmmq:Caller caller]) returns error?`,
and the optional `onError`) is enforced only at runtime in the native layer
(`native/src/main/java/io/ballerina/lib/ibm/ibmmq/listener/Service.java:116 validateOnMessageMethod`,
`:120`, `:134`) and documented in `docs/spec/spec.md:716–728`. Neither render conveys it, and the
bala README does not either (its only reference is a link to the `consume-messages-service` example,
README.md:161). An LLM cannot write a working `ibmmq:Service` from either render alone.

Also worth noting: `services` is `0` in both JSONs even though the library has a `Service` type, a
`ServiceConfig` annotation, and a `Listener`. That is consistent between sides.

## 7. Compiler plugin

**No compiler plugin exists.** The bala has no `compiler-plugin/` directory and `package.json`
contains no `compilerPlugin` key; `ballerina/Ballerina.toml` at `v1.4.4` declares no
`[[tool]]`/`compilerPlugin` section and the repo has no `*-compiler-plugin` module (only
`ballerina/` and `native/`).

Consequently the service-shape validation that a plugin would normally provide is done at runtime
in Java (`listener/Service.java:116–134`). Nothing a plugin implies is missing from the render,
because there is no plugin — but see §6: the runtime-only contract means the `onMessage` shape is
invisible in the render, and no plugin diagnostic makes up for it.

## 8. Other considerations

- Version is stable (`1.4.4`), not deprecated; `distribution = "2201.12.0"`, `platform = java21`.
- Size: +54 lines (+5.5%), JSON +2,611 bytes (+2.5%). Negligible token impact for a meaningful
  coverage gain.
- Token quality improves materially: `old` told an LLM only that types named `Listener`,
  `QueueManager`, and `Error` exist, with zero members — the two central entry points of the module.
  A model consuming `old` could not construct a queue manager or open a queue.
- `com.ibm.mq.allclient` is a `provided`-scope platform dependency (Ballerina.toml) and is absent
  from the bala's `platform/java21/` listing. Irrelevant to the render, but relevant if anyone tries
  to compile generated code.
- `docs/spec/spec.md` in the repo is a far richer API description than the README that the render
  embeds; it is not part of the bala and neither pipeline sees it.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 979 / 1033 |
| `grep -c '^// Unknown type:'` old / new | 3 / 0 |
| `grep -n '^// --- ' old` | 4 markers (README, END README, Types, Client) |
| `grep -n '^// --- ' new` | 5 markers (+ Annotations at l.1030) |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 7 / 0 |
| `grep -c 'ibmmq:ibmmq:'` old / new | 3 / 0 |
| `grep -c distinct` old / new | 0 / 1 (doc-comment text only) |
| `diff <(sed -n '7,179p' old) <(sed -n '7,179p' new)` | empty — README identical |
| `git ls-remote --tags …ibm.ibmmq \| grep v1.4.` | `v1.4.4` → `f8e5cb0`; clone verified `(grafted, HEAD, tag: v1.4.4)` |
| `ls -R <bala>` | single module `ibm.ibmmq`; 9 `.bal` files, 1,116 lines; no `compiler-plugin/` |
| `python3` JSON key/list counts | old: typeDefs 129, clients 3, functions 0, services 0, annotations 0 / new: same but annotations 1 |
| JSON `set(old typeDefs) ^ set(new typeDefs)` | both directions empty |
| JSON per-typeDef inequality scan | 9 differ: `Destination`, `Error`, `Header`, `Listener`, `MQIIH`, `MQRFH2`, `Message`, `QueueManager`, `ServiceConfiguration` |
| JSON `old Listener.init` params | already fully populated in `old` — 9 params with defaults; only `"type":"Class"` added in `new` |
| JSON client function-name lists both sides | only `init` dropped from `Caller`/`Queue`/`Topic` |
| JSON `Queue.put`/`Queue.get`/`Topic.*` param tuples both sides | identical (incl. `options` default `0`, `waitInterval` default `0`) |
| 125 public symbols from `<bala>/modules/ibm.ibmmq/*.bal` grepped against each render | missing from `new`: 0; missing from `old`: 1 (`ServiceConfig`) |
| `errors.bal:18` | `public type Error distinct error<ErrorDetails>;` |
| `listener.bal:20,25,33,40,46,52,58` | class + 6 members; all signatures match `new` |
| `queue_manager.bal:20,29,46,63,72` | class + 4 members; all signatures match `new` |
| `destination.bal:20–26` | `public type Destination distinct client object` with `put`/`get`/`close` |
| `types.bal:20,94,97,100,103,131–140,171–177,216,263,396–398` | `Service`, `ServiceConfiguration`, `ServiceConfig`, `OPEN_TOPIC_OPTION`, `Header`, `QueueManagerConfiguration`, `GetMessageOptions`, `map<Property>`, `table<MQRFH2Field> key(folder,'field) = table []`, `string:Char … = " "/"0"/"C"` |
| `constants.bal:18,21,63,173` | `OPEN_AS_SUBSCRIPTION=1`, `OPEN_AS_PUBLICATION=2`, `MQGMO_NO_WAIT=0`, `MQPMO_NO_SYNCPOINT=4` |
| `grep -rn onMessage src` | runtime validation in `native/.../listener/Service.java:116,120,134`; spec at `docs/spec/spec.md:716–728`; no compiler plugin |
| `grep -n 'onMessage\|ServiceConfig' <bala>/docs/README.md` | no hits (README.md is 170 lines; only an example link at :161) |
| `<bala>/package.json` | `"export": ["ibm.ibmmq"]`, no `compilerPlugin` key |

## 10. Caveats and unverified items

- `Queue.put`/`Topic.put` render `int options = 0` while the source default is
  `MQPMO_NO_SYNCPOINT` (= 4, `constants.bal:173`), and `Queue.get`/`Topic.get` render
  `waitInterval = 0` while `GetMessageOptions.waitInterval` defaults to `10` (`types.bal:174`).
  Both wrong values are byte-identical in the `old` and `new` JSON, so they are pre-existing
  extractor bugs, **not** attributable to spec v2. I did not trace the extractor code to explain
  why `Destination.get` gets `10` and `Queue.get` gets `0` from the same record — root cause
  **unverified**.
- I did not compile either render. "Non-compiling" claims in §5 rest on the Ballerina rule that a
  required parameter may not follow a defaultable one; I did not run `bal build` to confirm.
- The `ballerina-vscode` old/new source trees themselves were not inspected; the attribution of each
  change to the renderer vs. the extractor is inferred from the JSON being identical (renderer) or
  differing (extractor), which is a sound but indirect inference.
- Whether `Caller`/`Queue`/`Topic` truly have a usable implicit public `init` (making `old`'s
  `function init() returns ibmmq:ibmmq:Queue;` line semantically defensible before its malformed
  return type) was not verified against the language spec. It is moot: the render is strictly more
  correct without it.

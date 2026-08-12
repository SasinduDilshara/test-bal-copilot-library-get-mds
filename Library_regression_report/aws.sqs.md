# ballerinax/aws.sqs 5.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.sqs` |
| Pinned version | `5.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.sqs |
| Tag reviewed | `v5.0.0` (commit `a5fa4f6`, `git describe --tags` → `v5.0.0`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.sqs/5.0.0/java21` |
| Old render | `885` lines |
| New render | `911` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Every removed line in the diff was either a
`// Unknown type:` placeholder, an invalid version-qualified type reference, or a fabricated
constructor that does not exist in the library source. Nothing correct was lost.

Concretely, `new`:
- replaces `// Unknown type: Error` with the real `type Error error<aws:ErrorDetails>;`
- replaces `// Unknown type: Listener` with the full `Listener` class (6 methods)
- adds the `// --- Annotations ---` section carrying `public annotation ServiceConfigType ServiceConfig on service;` — the single most important missing symbol, since an SQS listener service is unusable without it
- normalises 5 invalid type refs (`ballerinax/aws:1.0.1:Region`, `ballerinax/aws.sqs:5.0.0:MessageAttributeValue` ×3, `ballerinax/aws.sqs:5.0.0:Error?`) to valid `aws:Region`, `MessageAttributeValue`, `Error`
- drops a fabricated `Caller.init() returns sqs:sqs:Caller` that has no counterpart in `caller.bal`

Public-symbol coverage of the default module goes from **39/40 in `old` to 40/40 in `new`**.

## 2. Change inventory

Line counts (`wc -l`): old **885**, new **911** (+26). Diff: 8 hunks, +34 / −8 lines.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 5 | 0 |
| `// --- ` section markers | 4 | 5 (adds `Annotations`) |
| JSON `typeDefs` | 75 | 75 |
| JSON `clients` | 2 | 2 |
| JSON `annotations` | 0 | 1 |
| JSON `functions` / `services` | 0 / 0 | 0 / 0 |

**Added in `new` (by kind):**

| Kind | Symbol | Detail |
|---|---|---|
| type (error) | `Error` | `type Error error<aws:ErrorDetails>;` + 3-line doc; was `// Unknown type: Error` |
| class | `Listener` | full body, 20 lines |
| class method | `Listener.init` | `(ConnectionConfig, PollingConfig = {}) returns Error?` |
| class method | `Listener.attach` | `(Service s, () path = ()) returns Error\|()` |
| class method | `Listener.detach` | `(Service s) returns Error\|()` |
| class method | `Listener.'start` | `() returns Error\|()` |
| class method | `Listener.gracefulStop` | `() returns Error\|()` |
| class method | `Listener.immediateStop` | `() returns Error\|()` |
| annotation | `ServiceConfig` | `public annotation ServiceConfigType ServiceConfig on service;` |

**Removed in `new`:**

| Kind | Symbol | Assessment |
|---|---|---|
| client-class constructor | `Caller.init() returns sqs:sqs:Caller` | Fabricated. `caller.bal` (bala, lines 20–28) declares only `remote function delete()`. `sqs:sqs:Caller` is also not valid Ballerina. Correct removal. |
| comment | `// Unknown type: Error`, `// Unknown type: Listener` | Placeholders, replaced by real definitions. |

**Modified (type-reference normalisation), 5 sites — all in the same direction:**

| old line | old text | new text |
|---|---|---|
| 336 | `ballerinax/aws:1.0.1:Region\|string region;` | `aws:Region\|string region;` |
| 365 | `map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue>` | `map<MessageAttributeValue>` |
| 432 | `map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue>` | `map<MessageAttributeValue>` |
| 472 | `map<ballerinax/aws.sqs:5.0.0:MessageAttributeValue>` | `map<MessageAttributeValue>` |
| 813 | `Client.init ... returns ballerinax/aws.sqs:5.0.0:Error?` | `... returns Error?` |

**Unchanged:** the README block (lines 1–244) is byte-identical between the two renders
(`diff` of lines 1–244 → no output). All 20 `remote function` declarations are identical in both
(`diff` of the extracted `remote function <name>` sets → no output). All 38 `const string`
declarations are identical. All 29 record and 5 enum typedefs are byte-identical except the 4
type-ref sites above.

JSON-level kind census (`type` field of `typeDefs`):

| kind | old | new |
|---|---|---|
| Constant | 38 | 38 |
| Record | 29 | 29 |
| Enum | 5 | 5 |
| Error | 1 | 1 |
| Class | 1 | 2 |
| *(untagged / null)* | 1 (`Listener`) | 0 |

The `old` JSON already contained the full `Listener` member list; it simply carried no `type` tag,
so `renderTypeDef` fell through to the placeholder. `new` tags it `Class` and renders it.

## 3. Correctness against library source

Verified against the bala (authoritative) at
`…/bala/ballerinax/aws.sqs/5.0.0/java21/modules/aws.sqs/`, cross-checked against the `v5.0.0` tag.

| Rendered in `new` | Source | Match |
|---|---|---|
| `type Error error<aws:ErrorDetails>;` | `errors.bal:22` `public type Error distinct error<aws:ErrorDetails>;` | Base type + doc exact; `distinct` dropped (see §5.1) |
| `class Listener` with `init/attach/detach/'start/gracefulStop/immediateStop` | `listener.bal:20–67` — exactly these 6 public methods, in this order | Yes |
| `Listener.init(ConnectionConfig connectionConfig, PollingConfig pollingConfig = {}) returns Error?` | `listener.bal:26` — identical signature and default | Yes |
| `Listener.attach(Service s, () path = ())` | `listener.bal:39` `attach(Service s, null path = ())` | Yes (`null` and `()` denote the same type) |
| `public annotation ServiceConfigType ServiceConfig on service;` | `types.bal:439` — character-for-character identical | Yes |
| annotation doc `Annotation to configure the \`sqs:Service\`.` | `types.bal:438` | Yes |
| `aws:Region\|string region;` in `ConnectionConfig` | `types.bal:31–33` `auth:AuthConfig auth; aws:Region\|string region; aws:EndpointConfig endpoint?;` | Yes |
| `map<MessageAttributeValue> messageAttributes?` | `types.bal:65` (`SendMessageConfig`) — same-module ref, unqualified | Yes |
| `Caller` with only `remote function delete() returns Error\|()` | `caller.bal:20–28` — one remote method, no `init` | Yes |
| 19 `Client` remote methods + `init` | `client.bal:30–226` — `init`, `sendMessage`, `receiveMessage`, `deleteMessage`, `sendMessageBatch`, `deleteMessageBatch`, `createQueue`, `deleteQueue`, `getQueueUrl`, `listQueues`, `getQueueAttributes`, `setQueueAttributes`, `changeMessageVisibility`, `purgeQueue`, `tagQueue`, `untagQueue`, `listQueueTags`, `startMessageMoveTask`, `cancelMessageMoveTask`, `close` | Names/arity match (see §5.3 on included-record flattening) |
| `class Service {}` | `types.bal:426` `public type Service distinct service object {};` | Yes — the source object body is genuinely empty |
| 35 typedefs in `types.bal` | grep of `^public ` in `types.bal` → 35 entries, all present in both renders | Yes |

Programmatic symbol-set comparison (all `public` declarations in the bala default module vs. the
union of render `typeDefs`/`clients`/`annotations`):

```
source public symbols 40
old  render symbols 39  missing: ['ServiceConfig']  extra: []
new  render symbols 40  missing: []                 extra: []
```

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff -u old new` read line by line — 8 hunks, 8 removed lines total, all accounted for in §2.
- Symbol-set difference `old_symbols - new_symbols` → empty set.
- Declaration-set difference for `remote function` names → empty.
- README region (lines 1–244) diffed → identical.
- Per-typedef JSON deep-equality: only `Error`, `Listener`, `ConnectionConfig`, `Message`,
  `SendMessageBatchEntry`, `SendMessageConfig` differ; each difference inspected individually and
  is an added `baseType`, an added `"type":"Class"` tag, or a de-qualified type name — no field,
  default, doc string, or return type was dropped.
- `Caller` JSON diff: the only removal is the `init` Constructor entry, which is fabricated
  (`caller.bal` has no `init`) and whose return type `sqs:sqs:Caller` is not valid syntax.
- Doc-comment continuation defects counted in both: 5 in `old`, 5 in `new` — unchanged.

## 5. Issues in `new` (independent of `old`)

7 issues. Items 3–7 are shared with `old` (renderer/extractor-wide, not introduced here); items 1–2
are specific to the newly-rendered declarations.

1. **`distinct` qualifier dropped from `Error`.** `new` line 326 emits
   `type Error error<aws:ErrorDetails>;`; source `errors.bal:22` is
   `public type Error distinct error<aws:ErrorDetails>;`. The JSON carries
   `"baseType": "error<aws:ErrorDetails>"` with no distinct flag, so the loss is at extraction time.
   Impact is low (assignability of the error subtype), but it is a fidelity gap.

2. **`Listener` class doc replaced by its constructor's doc.** `new` lines 779–781 render
   `# Initializes the AWS SQS listener.` above `class Listener`, and the `init` method itself gets
   no doc. The real class doc, `# Represents an AWS SQS Listener endpoint that can be used to
   receive messages from an SQS queue.` (`listener.bal:19`), is absent from the render *and* from
   the JSON — `typeDefs[Listener].description == "Initializes the AWS SQS listener.\n"`. The Java
   extractor hoists the constructor description onto the class. Mildly misleading but not harmful.

3. **Included-record parameters are flattened *and* duplicated, with invented defaults.**
   `Client.init` in source (`client.bal:30`) is
   `public isolated function init(*ConnectionConfig connectionConfig) returns Error?`.
   Both renders emit
   `function init(auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}, "us-west-2"|…|string region = "us-west-2", aws:EndpointConfig endpoint = {}, ConnectionConfig connectionConfig) returns Error?`.
   Three problems: `auth` and `region` are **required** in `ConnectionConfig` (`types.bal:31–32`)
   but are shown with fabricated defaults; a required positional `ConnectionConfig connectionConfig`
   follows defaulted parameters, which does not compile; and the `region` union is expanded to
   58 string literals (~900 characters on one line) instead of `aws:Region|string`.
   The same pattern applies to `sendMessage`, `receiveMessage`, `createQueue`, `getQueueUrl`,
   `listQueues`, `getQueueAttributes`, `startMessageMoveTask`. An LLM copying
   `sqsClient->sendMessage(url, body, 0, {}, "", "", "")` from this render would be writing against
   a signature that does not exist. Present identically in `old`.

4. **5 doc-comment continuation lines lack the `#` prefix**, making the render non-compiling.
   `new` lines 333–335, 338, 341 (`old` 330–332, 335, 338), all inside `ConnectionConfig`, e.g.
   `AWS — static credentials, an AWS profile, STS assume-role,` at column 0 inside a record body.
   Identical count and text in both sides.

5. **Closed records rendered as open.** Every record in `types.bal` is `record {| … |}`; both renders
   emit `record { … }`. This changes the type's rest-field semantics (29 records affected).

6. **`public` / `isolated` qualifiers dropped everywhere.** `Listener`, `Service`, `Caller`, `Client`
   and all typedefs lose them (source: `public isolated class Listener`, `public isolated client
   class Client`, etc.). Consistent across both renders.

7. **Parameter and return docs discarded by the renderer.** The JSON for e.g. `Listener.attach`
   carries `parameters[].description` ("The SQS Service to attach", "Not applicable for SQS. Must be
   a null value") and `return.description`, but the render emits only the summary line followed by a
   bare `# `. Both sides.

## 6. Coverage gaps vs. the library

**Default-module public symbols missing from `new`: 0.** The 40-symbol comparison in §3 is exact.
(`old` was missing 1: the `ServiceConfig` annotation.)

**Submodule-only API:** none. `package.json` declares `"export": ["aws.sqs"]` and the bala contains
exactly one module directory, `modules/aws.sqs`. `getDefaultModule()`-only extraction costs this
library nothing.

**1 genuine gap, shared by both renders and inherited from upstream:**

- The **`onMessage` / `onError` service contract is undiscoverable.** `types.bal:426` declares
  `public type Service distinct service object {};` — an empty object type — so neither render can
  show what an SQS service must implement. The contract is enforced only at runtime by
  `native/src/main/java/io/ballerina/lib/aws/sqs/listener/Service.java`: exactly one or two remote
  methods; `onMessage` is mandatory; parameters must be `sqs:Message` and optionally `sqs:Caller`;
  a second parameter must be `sqs:Caller`; `sqs:Caller` and `autoDelete: true` are mutually
  exclusive (lines 115–176). The bala README (234 lines) mentions the listener only once, in a link
  to the `basic-queue-consumer` example (line 231), and shows no service code.
  Consequence: an LLM given this render can now write the listener and the `@sqs:ServiceConfig`
  annotation (thanks to `new`) but must still guess the `onMessage` signature. `new` narrows this
  gap substantially; it does not close it.

## 7. Compiler plugin

**This package ships no compiler plugin.** Verified three ways:
- `find <repo> -iname '*compiler-plugin*' -maxdepth 3` → no matches at tag `v5.0.0`.
- The bala root contains only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
  `package.json`, `platform` — no `compiler-plugin/` directory and no
  `compiler-plugin/compiler-plugin.json`.
- The repo's Gradle modules are `ballerina`, `native`, `examples` only.

All service-shape validation is done at runtime in the native JAR
(`aws.sqs-native-5.0.0.jar`, class `io.ballerina.lib.aws.sqs.listener.Service`). Therefore there is
no plugin-contributed code action, diagnostic, or generated artifact that either render should have
surfaced and failed to. Nothing missing on this axis.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/aws.sqs/5.0.0`: `deprecated: null`,
  `deprecateMessage: ""`, `ballerinaVersion: 2201.12.0`, `pullCount: 29`, single module `aws.sqs`.
- **Stable major.** `5.0.0` is a stable release, not pre-1.0. `v5.0.0` is the newest tag on the repo.
- **Size / token impact is negligible.** +26 lines (+2.9%); JSON actually shrinks slightly
  (93,405 → 93,379 bytes) because de-qualifying type names offsets the added `Listener` tag,
  `baseType`, and annotation entry. The single 900-character expanded `region` union in
  `Client.init` remains the largest token sink in the file, unchanged between sides.
- **The `new` render is materially more useful for the listener/trigger use case.** The package is
  keyworded `Type/Trigger` as well as `Type/Connector`; before this change the entire trigger half of
  the API (`Listener`, `ServiceConfig`) was invisible or degraded. That is the headline win here.
- **Neither render compiles as-is** (see §5.3–§5.6). That is a pre-existing property of the
  `toSyntaxString` output format for this library, not a change introduced by spec v2.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/… new/…` | 885 / 911 |
| `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| `grep -n '^// --- '` old / new | old: README, END README, Types, Client (4); new: same + Annotations (5) |
| `diff -u old new` | 8 hunks, +34 / −8 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 5 / 0 |
| `diff <(sed -n '1,244p' old) <(sed -n '1,244p' new)` | no output (README identical) |
| `diff <(grep -o 'remote function [a-zA-Z]*' old\|sort) <(… new\|sort)` | no output; 20 / 20 |
| `git ls-remote --tags …module-ballerinax-aws.sqs` | `v5.0.0` present (`2cb5b3b`, peeled `a5fa4f6`) |
| `git clone --depth 1 --branch v5.0.0`; `git describe --tags` | `v5.0.0`, HEAD `a5fa4f6` |
| `ls <bala>/java21/modules/` | single dir `aws.sqs` → no submodules |
| `ls <bala>/…/modules/aws.sqs/` | `caller.bal client.bal errors.bal init.bal listener.bal types.bal` |
| `errors.bal:22` | `public type Error distinct error<aws:ErrorDetails>;` — `distinct` not in render |
| `caller.bal:20–28` | `public isolated client class Caller` with only `delete()` — no `init` |
| `listener.bal:19–67` | class doc + 6 public methods; matches `new` render body |
| `types.bal:426` | `public type Service distinct service object {};` (empty) |
| `types.bal:439` | `public annotation ServiceConfigType ServiceConfig on service;` — exact match to `new:911` |
| `types.bal:30–33` | `ConnectionConfig` — `auth` and `region` required, `endpoint?` optional |
| `client.bal:30` | `init(*ConnectionConfig connectionConfig) returns Error?` |
| `grep -cE '^public ' types.bal` | 35 public declarations |
| Python symbol-set diff (bala `public` vs render JSON) | source 40; old 39 (missing `ServiceConfig`); new 40 (missing 0, extra 0) |
| Python `typeDefs` deep-equality by name | only 6 differ: `Error`, `Listener`, `ConnectionConfig`, `Message`, `SendMessageBatchEntry`, `SendMessageConfig`; each inspected |
| Python `typeDefs` kind census | old `{Constant:38, Record:29, Enum:5, Error:1, Class:1, None:1}`; new `{Constant:38, Record:29, Enum:5, Class:2, Error:1}` |
| Python `clients` deep-diff | `Caller`: `init` Constructor removed; `Client`: return type de-qualified only |
| `new/…json → typeDefs[Listener].description` | `"Initializes the AWS SQS listener.\n"` (class doc lost at extraction) |
| Python scan for unprefixed doc-continuation lines in Types section | old 5, new 5 (same text, `ConnectionConfig`) |
| `find <repo> -iname '*compiler-plugin*'` | no matches |
| `ls <bala>/java21/` | no `compiler-plugin/` |
| `Service.java:50–176` | runtime validation of `onMessage`/`onError`, `sqs:Message`/`sqs:Caller` params, `autoDelete` exclusivity |
| `examples/basic-queue-consumer/service.bal` | `@sqs:ServiceConfig {…} service on sqsListener { remote function onMessage(sqs:Message message) returns error? }` |
| `wc -l <bala>/docs/README.md` | 234; `grep -ni 'listener\|onMessage'` → 1 hit (example link, line 231) |
| `curl api.central.ballerina.io/…/aws.sqs/5.0.0` | `deprecated: None`, 1 module, `ballerinaVersion 2201.12.0` |
| `wc -c` old/new JSON | 93,405 / 93,379 |

## 10. Caveats and unverified items

- The precomputed diff at `OLD_AND_NEW_DIFFS/aws.sqs_diff.md` reports **"Declarations removed (0)"**.
  That is inaccurate: `Caller.init` was removed (hunk 6, old line 782). Its declaration-extraction
  regex evidently does not match `function init(` inside a client class body. All other figures in
  that file (885/911 lines, +34/−8, 8 hunks, 2→0 placeholders, 5→0 qualified refs, 4→5 markers, the
  8 added declarations) were independently reproduced and are correct. The removal is a *correction*,
  not a regression — `caller.bal` has no `init` — so the verdict is unaffected.
- The scratch clone directory already contained `src` when this review began (the `git clone`
  reported "destination path already exists"); the checkout was therefore validated after the fact
  via `git describe --tags` → `v5.0.0` and `git log -1` → `a5fa4f6` (the peeled `v5.0.0` tag object
  from `git ls-remote`). The tree is the correct tag.
- The `Client.init` `region` parameter's 58-member string-literal union was checked for structural
  identity between old and new (the only textual difference on that line is the return type), but
  the individual literals were not diffed against the `ballerinax/aws` `Region` enum — that enum
  lives in a different package and was not in scope for this review.
- Doc-string content of the 29 records and 5 enums was verified as byte-identical between old and
  new via JSON deep-equality, but was not exhaustively compared field-by-field against `types.bal`
  prose; spot checks on `ConnectionConfig`, `SendMessageConfig`, `MessageAttributeValue`,
  `ReceiveMessageConfig`, and `PollingConfig` all matched.
- Runtime behaviour was not executed; all conclusions are from source, bala, JSON, and render text.

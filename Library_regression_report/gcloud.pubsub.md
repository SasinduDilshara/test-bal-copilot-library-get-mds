# ballerinax/gcloud.pubsub 0.1.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/gcloud.pubsub` |
| Pinned version | `0.1.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-gcloud.pubsub |
| Tag reviewed | `v0.1.1` (commit `ed2016fbd1582e46ee7d80adf9126c81cd6d6c50`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/gcloud.pubsub/0.1.1/java21` |
| Old render | 347 lines |
| New render | 394 lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module connector (7 `.bal` files, 393 lines total; 19 public declarations). The GitHub
tag `v0.1.1` and the bala `modules/gcloud.pubsub/*.bal` are byte-identical, so both sources agree.

`new` is strictly better than `old` on every axis checked:

- The 2 `// Unknown type:` placeholders in `old` (`Error`, `Listener`) become real definitions.
- The whole `Listener` class — the entire consumer-side API of this connector — was invisible in
  `old` and is fully rendered in `new` (init + 5 methods, all matching source).
- The `// --- Annotations ---` section with `ServiceConfig` is new and correct.
- Two `old` render defects are fixed: a fabricated `Caller.init()` returning the malformed type
  `pubsub:pubsub:Caller`, and the version-qualified return type
  `ballerinax/gcloud.pubsub:0.1.1:Error?` on `Publisher.init`.

Nothing present in `old` is missing, truncated, or degraded in `new`. Header, description and the
full README block (lines 1–218) are byte-identical between the two renders.

## 2. Change inventory

Old 347 lines / New 394 lines; 4 hunks, +51 / −4 (verified with `diff -u`, matches
`OLD_AND_NEW_DIFFS/gcloud.pubsub_diff.md`).

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 2 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 |
| `// --- ` section markers | 4 | 5 (`Annotations` added) |

**Added in `new` (8 declarations):**

| Kind | Declaration |
|---|---|
| type | `type Error error;` (replaces `// Unknown type: Error`) |
| class | `class Listener { ... }` (replaces `// Unknown type: Listener`) |
| method | `Listener.init(string subscriptionName, string projectId = "", Credentials credentials = {}, ListenerConfiguration listenerConfig) returns Error?` |
| method | `Listener.attach(Service s, string[]|string|() name = ()) returns error?` |
| method | `Listener.'start() returns error?` |
| method | `Listener.detach(Service s) returns error?` |
| method | `Listener.gracefulStop() returns error?` |
| method | `Listener.immediateStop() returns error?` |
| annotation | `public annotation PubSubServiceConfig ServiceConfig on service, class;` |

**Removed in `new` (1 declaration — a fabrication, see §4):**

- `Caller.init() returns pubsub:pubsub:Caller;`

**Modified in `new` (1):**

- `Publisher.init` return type `ballerinax/gcloud.pubsub:0.1.1:Error?` → `Error?`.

**Unchanged:** README block, `PubSubServiceConfig`, `Service`, `Credentials`, `BatchSettings`,
`PublisherConfiguration`, `ListenerConfiguration`, `Message`, `Caller.ack/nack`,
`Publisher.publish/publishBatch/close`.

JSON side (`old/*.json` vs `new/*.json`): `typeDefs` 9 → 9, `clients` 2 → 2, `functions` 0 → 0,
`services` 0 → 0, `annotations` **0 → 2**. `readme` and `description` fields are identical.
The `Listener` typeDef already carried its full `functions` array in the **old** JSON but lacked a
`"type"` key; `new` sets `"type": "Class"`. `Error` gains `"baseType": "error"`. So the `old` loss
was both an extractor gap (`type` tag missing) and a renderer gap (`renderTypeDef` fallthrough).
The two `annotations` entries (attachmentPoint `SERVICE` and `CLASS`) are correctly merged by the
renderer into the single line `on service, class`.

## 3. Correctness against library source

Bala and GitHub `v0.1.1` are identical — verified per-file with `diff -q` on all 7 `.bal` files, no
output. Every symbol below checked against the bala module source.

| Render (`new`) | Source | Verdict |
|---|---|---|
| `class Listener` + doc | `listener.bal:21` `public isolated class Listener` | correct (qualifiers `public`/`isolated` dropped — render-wide style, also applied to `Publisher`/`Caller`) |
| `Listener.init(...) returns Error?` | `listener.bal:30` `public isolated function init(string subscriptionName, *ListenerConfiguration listenerConfig) returns Error?` | name/return correct; included-record expansion imprecise, see §5 |
| `attach(Service s, string[]|string|() name = ()) returns error?` | `listener.bal:48` `attach(Service s, string[]|string? name = ()) returns error?` | correct (`string?` spelled `string|()`) |
| `'start() returns error?` | `listener.bal:59` | correct |
| `detach(Service s) returns error?` | `listener.bal:72` | correct |
| `gracefulStop() returns error?` | `listener.bal:83` | correct |
| `immediateStop() returns error?` | `listener.bal:94` | correct |
| `public annotation PubSubServiceConfig ServiceConfig on service, class;` | `listener.bal:108` — verbatim identical | correct |
| `type Error error;` | `module_errors.bal:18` `public type Error distinct error;` | `distinct` dropped, see §5 |
| `Caller` with only `ack`/`nack` | `caller.bal:20–43` — class declares **no** `init` | correct; `old`'s `init` was invented |
| `Publisher.init ... returns Error?` | `publisher.bal:27` `returns Error?` | correct |
| `Publisher.publish/publishBatch/close` | `publisher.bal:44/56/67` | correct |
| `PubSubServiceConfig{string subscriptionName;}` | `listener.bal:103` | correct |
| `Credentials`, `ListenerConfiguration`, `Message` fields | `types.bal:22/57/70` | field names/types correct |
| `BatchSettings`, `PublisherConfiguration` | `types.bal:32/45` | names/types correct, defaults lost — shared with `old`, see §8 |
| `class Service {}` | `listener.bal:111` `public type Service distinct service object {}` | shape approximated on both sides, see §8 |

Module-private symbols correctly excluded from both renders: the 15 `const string` in
`constants.bal`, `init()`/`setModule()` in `init.bal`, `createError()` in `module_errors.bal`,
`listenerInit`/`publisherInit` private methods.

## 4. Regressions

**None found.**

Checked:
- Full `diff -u old new`: 4 hunks, all additive except two removals, both verified as fixes to
  incorrect `old` output (fabricated `Caller.init` returning `pubsub:pubsub:Caller`, which is a
  doubled module prefix and not a valid type reference; and the version-qualified
  `ballerinax/gcloud.pubsub:0.1.1:Error?` return type on `Publisher.init`).
- README/header block `sed -n '1,218p'` on both files → byte-identical.
- Declaration-set comparison (§2): removed set = {`Caller.init`} only; no real API lost.
- Every doc comment present in `old` is present verbatim in `new` (no doc text dropped in any hunk).
- No parameter, default value or return type was narrowed or dropped anywhere in `new`.

## 5. Issues in `new` (independent of `old`)

Two, both minor and both confined to newly-added text (`old` emitted nothing here at all, so
neither is a regression):

1. **`distinct` lost on the error type.** `new` renders `type Error error;`; source
   (`module_errors.bal:18`) is `public type Error distinct error;`. A consumer LLM would not know
   the error type is distinct, which matters for `is Error` narrowing against other error types.
2. **`Listener.init` signature is not valid Ballerina and invents a default.**
   `function init(string subscriptionName, string projectId = "", Credentials credentials = {}, ListenerConfiguration listenerConfig) returns Error?` —
   (a) `listenerConfig` is a required positional parameter following defaulted parameters, which
   does not compile; the source uses an included-record parameter `*ListenerConfiguration`;
   (b) `projectId` is shown with default `""`, but `ListenerConfiguration.projectId`
   (`types.bal:58`) is a **required** field with no default, so the render implies the listener can
   be created without a project ID. Note the identical defect already exists in **both** renders on
   `Publisher.init` (`PublisherConfiguration config` trailing, `projectId = ""`), so this is a
   pre-existing renderer pattern now applied to one more constructor, not a new behaviour.

## 6. Coverage gaps vs. the library

**`new`: 0 gaps.** All 19 `public` declarations of the default module `gcloud.pubsub`
(`grep -nE '^\s*public ' modules/gcloud.pubsub/*.bal`) appear in the `new` render: `Caller`
(+`ack`, `nack`), `Publisher` (+`init`, `publish`, `publishBatch`, `close`), `Listener` (+`init`,
`attach`, `'start`, `detach`, `gracefulStop`, `immediateStop`), `Credentials`, `BatchSettings`,
`PublisherConfiguration`, `ListenerConfiguration`, `Message`, `Error`, `PubSubServiceConfig`,
`Service`, annotation `ServiceConfig`.

`old` had 3 gaps: `Error` (placeholder only), `Listener` + its 6 methods (placeholder only), and
the `ServiceConfig` annotation (absent entirely — the `old` JSON had `annotations: []`).

**Submodule API:** none. `package.json` `export` lists exactly `["gcloud.pubsub"]` and
`modules/` contains only `gcloud.pubsub`, which is the default module. Central metadata confirms a
single module. The `getDefaultModule()`-only extraction therefore loses nothing for this library.

## 7. Compiler plugin

This package ships **no compiler plugin**: no `compiler-plugin/` directory in the repo at `v0.1.1`
(repo root contains `ballerina/`, `native/`, `build-config/`, gradle files only), and
`find <bala> -name 'compiler-plugin*'` returns nothing. `native/` is the JVM runtime
implementation (`gcloud.pubsub-native-0.1.1.jar`), not a plugin.

Consequence: the `Service` object type is unconstrained — `listener.bal:111–113` declares
`public type Service distinct service object { }` with the intended
`remote function onMessage(Message message, Caller caller) returns error?` **commented out**, and
there is no plugin to validate it. So the required service method exists only in the README, and
no render can be expected to surface it as a declaration. Nothing plugin-implied is missing.

## 8. Other considerations

- **Pre-1.0 version** (`0.1.1`), 41 pulls, not deprecated (Central API: `deprecated: null`,
  `deprecateMessage: ""`). API may still churn.
- **Shared inaccuracies present in BOTH renders** (not regressions, but worth fixing upstream in
  the renderer):
  - Record **default values are dropped and defaulted fields become optional**:
    `BatchSettings.elementCountThreshold = 100`, `requestByteSizeThreshold = 1000000`,
    `delayThresholdMillis = 10` (`types.bal:33–35`) and `PublisherConfiguration.enableBatching = true`,
    `enableMessageOrdering = false` (`types.bal:48,50`) all render as `int x?` / `boolean x?`.
    The values survive only inside the doc text (`(default: 100)`), never as syntax.
  - **Closed records rendered as open**: every record in `types.bal` and `PubSubServiceConfig` is
    `record {| ... |}` in source but `record { ... }` in both renders.
  - **`Service` rendered as `class Service {}`** rather than `distinct service object`. An LLM
    reading either render cannot tell it must write `service on pubsubListener { remote function
    onMessage(...) }`; that information exists only in the README prose.
  - `Error?` returns are rendered `Error|()` — valid, cosmetic only.
- **Library-side README bug carried verbatim into both renders**: the README service examples use
  `pubsub:PubSubMessage` (3 occurrences, render lines 171/190/205; bala `docs/README.md:164,183,198`)
  but the module exports the type as `Message` (`types.bal:70`). Any LLM following the README will
  emit a non-compiling service. This originates in the library, is identical on both sides, and is
  not attributable to the renderer change.
- **Size/token impact**: +47 lines (+13.5%), 10,612 → 12,043 bytes (+13.5%). Trivial cost for
  recovering the connector's entire listener-side API.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 347 / 394 |
| `ls -la old new` | old 10,612 B / new 12,043 B (`.bal.txt`); 25,850 / 26,222 B (`.json`) |
| `git ls-remote --tags <repo>` | only `v0.1.0`, `v0.1.1`; used `v0.1.1` → `ed2016f` |
| `git clone --depth 1 --branch v0.1.1` | 7 `.bal` files under `src/ballerina/` |
| `diff -q <bala>/modules/gcloud.pubsub/<f>.bal src/ballerina/<f>.bal` ×7 | no output — bala == GitHub tag |
| `wc -l <bala>/modules/gcloud.pubsub/*.bal` | 43/40/25/113/25/71/76 = 393 lines |
| `diff -u old new` | 4 hunks, +51 −4 (matches precomputed diff md) |
| `diff <(sed -n '1,218p' old) <(sed -n '1,218p' new)` | identical (header + README) |
| `grep -c '^// Unknown type:' old new` | old 2, new 0 |
| `grep -nE '^\s*public ' <bala>/modules/gcloud.pubsub/*.bal` | 19 public declarations, all in `new` |
| `find <bala> -name 'compiler-plugin*'`; `ls src` | no compiler plugin |
| `cat <bala>/package.json` | `export: ["gcloud.pubsub"]`, ballerina_version 2201.12.0, platform java21 |
| `ls <bala>/modules` | single module `gcloud.pubsub` (= default module) |
| Python JSON compare | typeDefs 9→9, clients 2→2, annotations 0→2, functions 0→0, services 0→0; readme & description identical |
| Python JSON: old `Listener` typeDef | full `functions` array present, `"type"` key **absent** |
| Python JSON: new `Listener` typeDef | `"type": "Class"`, init return `Error?` |
| Python JSON: `Error` typeDef | old `{type: Error}`; new adds `"baseType": "error"` |
| Python JSON: client functions | old `Caller` had `init → pubsub:pubsub:Caller`; new does not |
| `caller.bal:20–43` | class declares no `init` → `old`'s init was fabricated |
| `listener.bal:21,30,48,59,72,83,94,103,108,111` | all `new` Listener/annotation content verified |
| `publisher.bal:27,44,56,67` | Publisher signatures verified |
| `types.bal:22,32,45,57,70` | record fields verified; defaults at 33–35, 48, 50 |
| `module_errors.bal:18` | `public type Error distinct error;` |
| `grep -n 'PubSubMessage' <bala>/docs/README.md` | lines 164, 183, 198 — library-side README bug |
| Central API `packages/ballerinax/gcloud.pubsub/0.1.1` | not deprecated, public, 1 module, 41 pulls |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that `Listener.init` / `Publisher.init` as rendered do not
  compile are based on reading the Ballerina spec rule that required parameters cannot follow
  defaulted ones; not verified by invoking `bal build`.
- The `native/` Java sources at `v0.1.1` were not read; the review covers the Ballerina-visible API
  surface only, which is what the extractor consumes.
- The claim that `old`'s `Caller.init` is fabricated rests on the absence of any `init` in
  `caller.bal`; the generating LS code path in `ballerina-vscode@eb5d81b3` was not inspected, so the
  mechanism that produced it is unverified (only the fact that it is wrong is verified).

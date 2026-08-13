# ballerina/messaging 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/messaging` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-messaging |
| Tag reviewed | `v1.0.0` |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/messaging/1.0.0/any` |
| Old render | `219` lines |
| New render | `264` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/messaging` is a tiny standard-library module: a single default module `messaging`, four
`.bal` files, seven public symbols, no compiler plugin, no submodules. The upstream tag `v1.0.0`
sources are byte-identical to the bala's `modules/messaging/*.bal` (verified with `diff -r`).

`new` is strictly additive over `old`: +48 lines, −3 lines, 2 hunks. Both `// Unknown type:`
placeholders in `old` (`Error`, `StoreListener`) are gone (2 → 0), and two object types that `old`
rendered as empty shells (`Store`, `StoreService`) now carry their real method sets. No declaration,
parameter, default, return type, or doc line present in `old` is missing from `new`. The README
block (lines 7–159) is byte-identical on both sides.

The improvement is real but not clean: the newly-surfaced `StoreListener.init` signature is
non-compiling — the included-record parameter `*StoreListenerConfiguration config` is flattened into
five defaulted parameters *and* re-emitted as a trailing required `config` parameter, and the
optional `deadLetterStore` field is given an invented default `object {}`. Both defects originate in
the Java extractor (they are present verbatim in **both** JSONs), so `new` did not introduce them —
it merely stopped hiding them behind `// Unknown type: StoreListener`.

## 2. Change inventory

Line counts (`wc -l`): old `219`, new `264`. JSON bytes: old `19432`, new `22354`.

Signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version-qualified type refs in JSON (`ballerina/messaging:1.0.0:…`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `typeDefs` entries | 6 | 6 |
| `clients` / `functions` / `services` / `annotations` entries | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 |

### Added in `new` (13 declarations)

| Kind | Name | Detail |
|---|---|---|
| type | `Error` | replaces `// Unknown type: Error`; rendered `type Error error;` |
| class header | `client class Store` | was `class Store` (empty body) |
| method | `Store.store` / `.retrieve` / `.acknowledge` | 3 remote methods, previously absent |
| method | `StoreService.onMessage` | previously absent |
| class | `StoreListener` | replaces `// Unknown type: StoreListener` |
| method | `StoreListener.init` / `.attach` / `.detach` / `.'start` / `.gracefulStop` / `.immediateStop` | 6 members |

### Removed in `new` (0 semantic removals)

The mechanical diff lists `class Store` as removed; that is the header line being rewritten to
`client class Store` with a populated body, not a removal. The other two removed lines are the two
`// Unknown type:` placeholders.

### Where the change lives

The JSON layer changed too, not just the renderer:

* `old` JSON: `typeDefs["StoreListener"]` has **no** `type` key (keys: `name`, `description`,
  `functions`) → `main`'s `renderTypeDef` falls through to `// Unknown type:` even though the six
  functions were already extracted. `new` JSON adds `"type": "Class"`.
* `old` JSON: `Store` and `StoreService` have `type: "Class"` but **no** `functions` array. `new`
  JSON adds `functions` (3 and 1 respectively) plus `"isClient": true` on `Store`.
* `old` JSON: `Error` = `{name, description, type}`. `new` adds `"baseType": "error"`.
* `old` JSON emitted `"ballerina/messaging:1.0.0:Error?"` as `StoreListener.init`'s return type;
  `new` emits `"Error?"` — the known spec-v2 de-qualification, confirmed here (1 → 0).

## 3. Correctness against library source

Every added member checked against the bala source (identical to `v1.0.0` upstream).

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `remote function store(anydata payload) returns error?` | `msg_store.bal:32` `isolated remote function store(anydata payload) returns error?` | correct (modulo dropped `isolated`) |
| `remote function retrieve() returns Message\|error\|()` | `msg_store.bal:37` `returns Message\|error?` | correct (`Message\|error?` ≡ `Message\|error\|()`) |
| `remote function acknowledge(string id, boolean success = true) returns error?` | `msg_store.bal:45` | correct, default `true` matches |
| `remote function onMessage(anydata payload) returns error?` | `msg_store_service.bal:24` | correct |
| `type Error error;` | `msg_listener.bal:22` `public type Error distinct error;` | mostly correct — `distinct` dropped |
| `function attach(StoreService msgStoreService, () path = ()) returns Error\|()` | `msg_listener.bal:78` | correct |
| `function detach(StoreService msgStoreService) returns Error\|()` | `msg_listener.bal:92` | correct |
| `function 'start() returns Error\|()` | `msg_listener.bal:118` | correct |
| `function gracefulStop() returns Error\|()` | `msg_listener.bal:139` | correct |
| `function immediateStop() returns Error\|()` | `msg_listener.bal:147` | correct |
| `function init(Store messageStore, decimal pollingInterval = 1, …, StoreListenerConfiguration config) returns Error?` | `msg_listener.bal:54` `init(Store messageStore, *StoreListenerConfiguration config) returns Error?` | **incorrect** — see §5.1 |

Doc strings on the added members are copied verbatim from the source doc comments (e.g. the
three-line `gracefulStop` doc matches `msg_listener.bal:134-136`).

Unchanged regions re-verified: `Message` fields match `msg_store.bal:18-23`;
`StoreListenerConfiguration` field names/types match `msg_listener.bal:25-39`; the
`InMemoryMessageStore` client block matches `inmemory_msg_store.bal:26-92` except the `acknowledge`
default (§5.6).

## 4. Regressions

**None found.**

Basis for that conclusion:

* `diff -u old new` produces exactly 2 hunks, `+48 / −3`. The three removed lines are
  `// Unknown type: Error`, `class Store {`, and `// Unknown type: StoreListener`. Each is replaced
  by strictly more content about the same symbol.
* Both JSONs have the identical symbol set: `typeDefs` = `[Message, Error, StoreListenerConfiguration,
  Store, StoreService, StoreListener]`, `clients` = `[InMemoryMessageStore]`, and empty `functions`,
  `services`, `annotations` on both sides.
* README payload is identical (`len(readme)` = 6360 on both sides; render lines 1–159 identical).
* No parameter, default value, or return type present in `old` is altered in `new`
  (`InMemoryMessageStore` block, render lines 249–264 vs old 204–219, is byte-identical).
* No new `// Unknown type:` lines and no new version-qualified refs; both counts move in the
  favourable direction.

## 5. Issues in `new` (independent of `old`)

7 issues. Items 1–4 are visible only in `new` because `old` hid the symbols; items 5–7 are shared
with `old` but are still wrong in `new`.

**5.1 — `StoreListener.init` is non-compiling and semantically wrong (most serious).**
Render line 220:
```ballerina
function init(Store messageStore, decimal pollingInterval = 1, int maxRetries = 3, decimal retryInterval = 1, boolean ackWithFailureAfterMaxRetries = true, Store deadLetterStore = object {}, StoreListenerConfiguration config) returns Error?;
```
Source (`msg_listener.bal:54`) is `init(Store messageStore, *StoreListenerConfiguration config)`.
The included-record parameter has been flattened into its five fields **and** the record itself is
re-emitted as a seventh parameter. Two problems: (a) a parameter with no default (`config`) follows
defaulted parameters, which Ballerina rejects; (b) `config` is duplicated with its own fields. In the
JSON, `config` carries `"optional": true` with no `"default"`, and the renderer prints
`"optional-without-default"` as a bare required parameter. An LLM reading this will write
`new messaging:StoreListener(store, 10, 2, 2, true, dls, {})` or similar — all of which fail.

**5.2 — invented default `Store deadLetterStore = object {}`.**
`msg_listener.bal:38` declares `Store deadLetterStore?;` — optional, no default. The extractor
synthesises `"default": "object {}"` (present in both JSONs, `grep -c 'object {}'` = 1 each). Beyond
being fabricated, `object {}` does not conform to `Store`, which requires three remote methods, so
the line cannot compile.

**5.3 — `distinct` dropped from `Error`.**
`new` emits `type Error error;`; source is `public type Error distinct error;`
(`msg_listener.bal:22`). JSON carries `"baseType": "error"` with no distinctness marker. The rendered
form is valid syntax but loses the distinct-type identity that makes `e is messaging:Error` a
meaningful narrowing.

**5.4 — `StoreListener`'s class-level doc is the constructor's doc.**
Render line 217 reads `# Initializes a new instance of Message Store Listener.` The real type doc is
`# Represents a message store listener that polls messages from a message store and processes them.`
(`msg_listener.bal:41`). The JSON `description` field on the `StoreListener` typeDef holds the init
doc on **both** sides, so this is an extractor issue newly surfaced by `new`.

**5.5 — object types rendered as classes.**
`Store` (`public type Store isolated client object`, `msg_store.bal:26`) is rendered as
`client class Store`, and `StoreService` (`public type StoreService distinct isolated service
object`, `msg_store_service.bal:18`) as `class StoreService`. Neither is instantiable; `Store` is an
interface to implement and `StoreService` is a service-object contract. `class` invites
`new messaging:Store()`, which is invalid. `StoreService`'s `service object` / `distinct` nature is
lost entirely. Shared with `old` for the headers; `new` compounds it by adding method bodies that
make them look like usable classes.

**5.6 — `InMemoryMessageStore.acknowledge` default is wrong.**
Render line 263: `boolean success = false`. Source `inmemory_msg_store.bal:69` is
`boolean success = true`. Confirmed at JSON level on both sides (`"default": "false"`). Note the
render is internally inconsistent: `Store.acknowledge` (line 206) correctly shows `= true` for the
identical signature. Shared with `old`, still wrong in `new`.

**5.7 — record fidelity losses (shared).**
* `Message.id` loses `readonly` (`msg_store.bal:20`).
* Both `Message` and `StoreListenerConfiguration` are closed (`record {| |}`) in source but rendered
  open (`record { }`).
* `StoreListenerConfiguration`'s five defaults (`pollingInterval = 1`, `maxRetries = 3`,
  `retryInterval = 1`, `ackWithFailureAfterMaxRetries = true`) are rendered as `?` optional fields
  with no default shown — the JSON `fields` carry `"optional": true` and no `"default"` on both
  sides. A reader cannot learn the polling defaults from the type block (they are recoverable only
  from the README and from the malformed `init` line).
* Multi-line doc continuations lose their leading `#`, e.g. render lines 180-181 produce a bare
  `If set to 0, the message will not be retried` line inside the record body — not valid Ballerina.
  Identical on both sides.

Module qualifiers `public` and `isolated` are absent throughout on both sides; noted but not counted,
as it appears to be a deliberate render convention.

## 6. Coverage gaps vs. the library

**0 gaps.** The default module `messaging` exports exactly seven public symbols; all seven appear in
both renders.

| Public symbol | Source | In render |
|---|---|---|
| `Message` | `msg_store.bal:18` | yes |
| `Store` | `msg_store.bal:26` | yes |
| `StoreService` | `msg_store_service.bal:18` | yes |
| `InMemoryMessageStore` | `inmemory_msg_store.bal:26` | yes (Client section) |
| `Error` | `msg_listener.bal:22` | `new` only |
| `StoreListenerConfiguration` | `msg_listener.bal:25` | yes |
| `StoreListener` | `msg_listener.bal:42` | `new` only |

Non-public symbols correctly excluded: `InMemoryMessage` (`inmemory_msg_store.bal:20`) and
`PollAndProcessMessages` (`msg_listener.bal:164`).

No submodule-only API: `package.json` `"export": ["messaging"]`, the bala has exactly one directory
under `modules/`, and Central lists exactly one module. The `getDefaultModule()`-only extraction
limitation therefore costs this library nothing.

The module declares no annotations, constants, configurables, module-level functions, or module-level
listeners (`grep -nE '\b(annotation|const|configurable)\b'` over the bala sources returns only doc-text
matches), consistent with the empty `functions`/`services`/`annotations` arrays in both JSONs.

## 7. Compiler plugin

**None.** `has_plugin` is `false` in the manifest, and this is confirmed directly: `ls -a` on the bala
root shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — there is
no `compiler-plugin/` directory and no `compiler-plugin.json`. The upstream `v1.0.0` clone has no
`compiler-plugin` module either (top level is `LICENSE README.md ballerina build-config build.gradle
changelog.md docs examples gradle gradle.properties gradlew gradlew.bat settings.gradle`). Nothing is
missing from the render on plugin grounds.

## 8. Other considerations

* **Not deprecated.** Central `isDeprecated: false`, `deprecateMessage: ""`. Stable 1.0.0,
  `graalvmCompatible: Yes`, 7,849 pulls.
* **The library's own README is out of sync with its API, and both renders faithfully reproduce that.**
  The README (render lines 19–107) documents `MessageStore`, `Service`, and `messaging:Listener`;
  the actual exported names are `Store`, `StoreService`, and `StoreListener`. The README's `Message`
  record also omits `readonly` on `id`. This is an upstream doc bug, not a renderer bug, but it is
  the single largest source of wrong-symbol risk in this render: the README is 152 of the 264 lines
  (58%) and it names three types that do not exist. Worth flagging upstream.
* **Size.** Small on both sides; the +45-line growth is immaterial for token budget and buys the
  entire `StoreListener` lifecycle API, which is the module's primary use case.
* **Net effect on an LLM.** `old` gave no way to construct a listener at all (`// Unknown type:
  StoreListener`) and no methods on `Store`, so implementing a custom message store was impossible
  from the render. `new` makes both possible; the residual risk is concentrated in the `init` line
  (§5.1) and in the README's stale names.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 219, new 264 |
| `wc -c` on both JSONs | old 19432, new 22354 |
| `diff -u old new` | 2 hunks, +48 / −3 |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep -n '^// --- '` | 4 markers each; `--- Client ---` at old:202 / new:247 |
| `grep -o 'ballerina/messaging:1\.0\.0:[A-Za-z?]*'` on JSONs | old: 1 (`…:Error?`), new: 0 |
| `grep -c 'object {}'` on JSONs | old 1, new 1 |
| `git clone --depth 1 --branch v1.0.0 …/module-ballerina-messaging` | succeeded; tag exists |
| `diff -r <clone>/ballerina <bala>/modules/messaging` | no content differences in the 4 `.bal` files; only build/test files extra in the clone |
| `ls -a` bala root | `bala.json dependency-graph.json docs modules package.json` — no `compiler-plugin/` |
| `ls` bala `modules/` | single dir `messaging` |
| `cat` bala `package.json` | `"export": ["messaging"]`, `ballerina_version: 2201.12.0`, `platform: any` |
| `curl` Central `packages/ballerina/messaging/1.0.0` | 1 module, `isDeprecated: false`, `graalvmCompatible: Yes`, pullCount 7849 |
| `grep -nE '^public '` over bala `.bal` files | 7 public symbols enumerated (§6) |
| `grep -nE '\b(annotation\|const\|configurable\|listener)\b'` | only doc-comment/text matches; no declarations |
| Python: JSON `typeDefs` keys per side | `StoreListener` lacks `type` in old, has `"type":"Class"` in new; `Store`/`StoreService` gain `functions` in new; `Error` gains `baseType` in new |
| Python: `StoreListener.init` params in both JSONs | 7 params both sides; `deadLetterStore` `"default":"object {}"`; `config` `"optional":true` with no default — identical old and new |
| Python: `InMemoryMessageStore.acknowledge` params both JSONs | `success` `"default":"false"` on both sides |
| Python: `Message.fields` both JSONs | no `readonly` marker on `id` either side |
| Python: `StoreListenerConfiguration.fields` both JSONs | all five fields `"optional": true`, no `"default"` either side |
| Python: `len(readme)` both JSONs | 6360 both |
| Source line checks | `msg_store.bal:18,20,26,32,37,45`; `msg_store_service.bal:18,24`; `msg_listener.bal:22,25,38,41,42,54,78,92,118,139,147,164`; `inmemory_msg_store.bal:20,26,49,69` |

## 10. Caveats and unverified items

* The two renders were not regenerated during this review; the audit is of the committed
  `old/` and `new/` artifacts as found. Their provenance (the two `ballerina-vscode` commits named in
  the brief) is taken on trust from the brief and was not re-derived.
* The claim that `StoreListener.init` and the `object {}` default are non-compiling is by inspection
  against the Ballerina spec's rule that required parameters may not follow defaulted ones and that
  `object {}` cannot conform to a client object with abstract remote methods; no compiler was run
  against the rendered text (the render is a documentation artifact, not a compilable unit — it has
  no bodies).
* Whether the `pollingInterval`/`maxRetries`/… flattening in `init` is intentional extractor
  behaviour for `*IncludedRecord` parameters (i.e. a deliberate expansion that the renderer then
  mishandles by also printing `config`) versus an outright extractor bug was not determined — the
  Java extractor source was not read for this review. Either way the rendered line is wrong.
* Upstream `README.md` at the repo root was not diffed against `docs/README.md` in the bala; the
  bala's README was compared against the Central `readme` field and against the render, all three of
  which agree.

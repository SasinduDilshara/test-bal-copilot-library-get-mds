# ballerinax/nats 3.3.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/nats` |
| Pinned version | `3.3.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-nats |
| Tag reviewed | `v3.3.1` (commit `7e4fbbcc4cc116f12ae9ef375e10390bc2bfb83a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/nats/3.3.1/java21` |
| Old render | `552` lines |
| New render | `646` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive and strictly more correct than `old` for this library. All 5 `// Unknown type:`
placeholders in `old` are replaced with real definitions, the 3 public annotations that `old` omitted
entirely are now emitted, and all 4 version/module-qualified type references (`ballerinax/nats:3.3.1:Error`,
`ballerinax/nats:nats:JetStreamCaller`, `ballerinax/nats:3.3.1:Protocol`) are gone. Two things disappear from
`new` — a phantom `JetStreamCaller.init()` constructor and the `remote` qualifier on `Client.close()` — and
both removals are corrections: neither exists in the library source. Nothing present and correct in `old` is
missing, truncated, or degraded in `new`. Zero regressions found.

The published bala is byte-identical to the GitHub source at `v3.3.1` (all 12 `.bal` files diff clean), and
the package exports exactly one module (`"export": ["nats"]`), so there is no submodule coverage gap here.

## 2. Change inventory

Line counts: `old` 552, `new` 646 (+104 added, −10 removed, 6 hunks).

Top-level declarations in the render body (grep on `^<kind> `):

| Kind | old | new | delta |
|---|---|---|---|
| `const` | 11 | 11 | 0 |
| `type` (record/error) | 15 | 18 | +3 |
| `enum` | 4 | 4 | 0 |
| `class` | 2 | 4 | +2 |
| `client class` | 3 | 3 | 0 |
| `public annotation` | 0 | 3 | +3 |
| `// Unknown type:` | 5 | 0 | −5 |
| `// --- section ---` markers | 4 | 5 | +1 |
| Class/client methods (excluding the 2 README code-block lines) | 18 | 29 | +11 |
| — of which `remote` | 15 | 14 | −1 |

**Added in `new` (13 declarations, 0 removed at declaration level):**

- Error types (were `// Unknown type:` in `old`): `Error`, `PayloadBindingError`, `PayloadValidationError`
- Classes (were `// Unknown type:` in `old`): `JetStreamListener`, `Listener` — each with 6 methods
  (`init`, `attach`, `detach`, `'start`, `gracefulStop`, `immediateStop`), 12 methods total
- New `// --- Annotations ---` section with `StreamServiceConfig`, `Payload`, `ServiceConfig`

**Removed / altered in `new` (2 items, both corrections — see §4):**

- `JetStreamCaller.init() returns ballerinax/nats:nats:JetStreamCaller;` — deleted
- `remote function close()` → `function close()` on `Client`

**Type-reference normalisation:** `ballerinax/nats:3.3.1:Error?` → `Error?` (×2, `Client.init`,
`JetStreamClient.init`); `record {|ballerinax/nats:3.3.1:Protocol name;|}` → `record {|Protocol name;|}`
(in `SecureSocket`).

**Unchanged:** lines 1–174 are byte-identical between the two files (README section, all consts, all
enums). README payload is 4722 chars in both JSONs.

**JSON level:** both JSONs have 37 `typeDefs`, 3 `clients`, 0 `functions`, 0 `services`. `old` has 0
`annotations`, `new` has 5 (one entry per attachment point; the renderer merges the `SERVICE`/`CLASS` pairs
into the 3 emitted `on service, class` lines). `old` typeDef categories include `Error` and `None`; `new`
has no `None` — `Listener`/`JetStreamListener` are now tagged `Class` and carry a `type` field.

## 3. Correctness against library source

Everything `new` adds was verified against the bala (`modules/nats/*.bal`, identical to GitHub `v3.3.1`).

| New render | Source | Match |
|---|---|---|
| `type Error error;` | `error.bal:18` `public type Error distinct error;` | name/doc ✓, `distinct` lost (§5.1) |
| `type PayloadBindingError error;` | `error.bal:21` `public type PayloadBindingError distinct Error;` | name/doc ✓, base type wrong (§5.1) |
| `type PayloadValidationError error;` | `error.bal:24` `public type PayloadValidationError distinct PayloadBindingError;` | name/doc ✓, base type wrong (§5.1) |
| `class Listener` + 6 methods | `listener.bal:21,30,42,54,65,75,86` | ✓ |
| `class JetStreamListener` + 6 methods | `jetstream_listener.bal:21,26,38,50,61,71,82` | ✓ |
| `function init(Client natsClient) returns Error?` (JetStreamListener) | `jetstream_listener.bal:26` | ✓ exact |
| `function attach(Service s, string[]|string|() name = ())` | `listener.bal:42` `attach(Service s, string[]|string? name = ())` | ✓ (`string?` ≡ `string|()`) |
| `function 'start() returns error?` etc. | `listener.bal:65,75,86` — all `public isolated function`, not remote | ✓ correctly non-remote |
| `public annotation JetStreamServiceConfigData StreamServiceConfig on service, class;` | `jetstream_types.bal:21` | ✓ verbatim |
| `public annotation NatsPayload Payload on parameter;` | `records.bal:160` | ✓ verbatim |
| `public annotation ServiceConfigData ServiceConfig on service, class;` | `types.bal:24` | ✓ verbatim |
| `record {|Protocol name;|} protocol?;` in `SecureSocket` | `records.bal:65–67` | ✓ exact |
| `function close() returns Error|()` | `client.bal:81` `public isolated function close() returns Error?` | ✓ non-remote is correct |
| `JetStreamCaller` with only `ack`/`nak`/`inProgress` | `jetstream_caller.bal:20–55` — no `init` declared | ✓ |

Full method-signature comparison of both JSONs (name, kind, params, defaults, return type) produced 30
signatures for `old` and 29 for `new`; the diff is exactly one line — the deleted phantom
`JetStreamCaller.init|Constructor||->None`. Every other signature is identical between the two sides.

All 14 `remote` markers in `new` were checked against the source: `Client.publishMessage/requestMessage`
(`client.bal:40,69`), `JetStreamCaller.ack/nak/inProgress` (`jetstream_caller.bal:28,39,50`), and
`JetStreamClient.publishMessage/consumeMessage/ack/nak/inProgress/addStream/updateStream/deleteStream/purgeStream`
(`jetstream_client.bal:38,51,64,76,88,100,112,124,136`) — all `isolated remote function` in source. Correct.

## 4. Regressions

**None found.**

Checked, in order:

1. **Declaration-level removals.** The mechanical diff reports 0 removed declarations; independently, every
   one of the 30 public symbols grepped out of `modules/nats/*.bal` that appears in `old` also appears in
   `new` (loop over `/tmp/nats_public.txt` against both files: zero `NEW-MISSING`, five `OLD-MISSING`).
2. **`JetStreamCaller.init()` deleted.** `jetstream_caller.bal:20–55` contains no `init` — the class has only
   `ack`, `nak`, `inProgress`. `old` invented a constructor returning `ballerinax/nats:nats:JetStreamCaller`,
   which is not valid Ballerina and is not a real API. Deletion is a correction, not a loss.
3. **`remote` dropped from `Client.close()`.** `client.bal:81` is `public isolated function close() returns Error? =`
   — it is a normal method called as `natsClient.close()`, exactly as the render's own doc example shows
   (`# check natsClient.close();`). `old` marked it `remote`, which would have led an LLM to emit
   `natsClient->close()`. `new` is correct.
4. **Docs / defaults / return types.** Signature-level JSON diff (§3) shows no parameter, default value, or
   return type changed anywhere except the two items above. README block (lines 1–174) is byte-identical.
5. **Encoding / malformed output.** `grep -P '[^\x00-\x7F]'` on `new` returns nothing; no truncated lines,
   no unbalanced braces introduced by the new sections.

## 5. Issues in `new` (independent of `old`)

Five inaccuracies vs. the library source exist in `new`. Items 5.1–5.2 are new-side only (the affected
declarations did not exist in `old`); 5.3–5.5 are shared with `old` and are therefore not regressions.

1. **Error subtype hierarchy is flattened.** `new` emits `type Error error;`, `type PayloadBindingError error;`,
   `type PayloadValidationError error;`. Source (`error.bal:18,21,24`) is `distinct error`, `distinct Error`,
   `distinct PayloadBindingError`. The `distinct` qualifier and the two-level subtype relationship are lost;
   the JSON carries a flat `"baseType": "error"` for all three, so the loss is at the extractor, not the
   renderer. Impact: an LLM cannot tell that `PayloadValidationError` is a subtype of `PayloadBindingError`
   which is a subtype of `Error`, and cannot write correct `error:Detail`/type-narrowing code. Still a large
   net gain over `old`, which emitted nothing at all for these three types.
2. **`Listener.init` renders a non-compiling parameter list.** `function init(string|string[] url, string connectionName = "ballerina-nats", …, boolean validation = true, ConnectionConfiguration config) returns Error?`
   — the included-record parameter `*ConnectionConfiguration config` (`listener.bal:30`) is expanded into its
   individual fields *and* re-appended as a trailing required `ConnectionConfiguration config`. A required
   parameter after defaulted parameters is invalid Ballerina. This is the same renderer convention already
   applied to `Client.init` in `old`, now newly applied to `Listener` as well.
3. **Typedesc parameter mis-rendered (shared with `old`).** `remote function requestMessage(AnydataMessage message, decimal|() duration = (), AnydataMessage T = nats:AnydataMessage) returns T|Error;`
   — source (`client.bal:69–70`) is `typedesc<AnydataMessage> T = <>`. The rendered form is not valid
   Ballerina and misrepresents `T` as a value parameter. Identical in `old` (line 443) and `new` (line 527).
4. **Service object types rendered as empty classes (shared with `old`).** `class Service {}` and
   `class JetStreamService {}`; source is `public type Service distinct service object {};` (`types.bal:21`)
   and `public type JetStreamService distinct service object {};` (`jetstream_types.bal:18`). Neither render
   conveys that these are service object types, nor the `onMessage`/`onRequest`/`onError` remote-method
   contract the compiler plugin enforces (see §7). The README code block does show a `service nats:Service`
   example, which partially compensates.
5. **All modifiers stripped except on annotations (shared with `old`).** `public`, `isolated`, `distinct`,
   `client`/`service object` are dropped from types, classes and methods, but the three annotation lines are
   emitted with an explicit `public`. Cosmetic inconsistency; no semantic loss for consumption.

Benign, noted for completeness: enum members are also emitted as 11 top-level `const string` lines
(`LIMITS`, `INTEREST`, `WORKQUEUE`, `FILE`, `MEMORY`, `NEW`, `OLD`, `SSL`, `TLS`, `DTLS`, plus the genuine
`DEFAULT_URL`). Enum members are constants in Ballerina, so this is accurate, just duplicated with the four
`enum` blocks. Identical in both renders.

## 6. Coverage gaps vs. the library

**`new`: 0 gaps.** All 29 public symbols exported by the default module `nats` (the only exported module —
`package.json` `"export": ["nats"]`) appear in `new`: `AnydataMessage`, `BytesMessage`, `CertKey`, `Client`,
`ConnectionConfiguration`, `Credentials`, `DEFAULT_URL`, `DiscardPolicy`, `Error`, `JetStreamCaller`,
`JetStreamClient`, `JetStreamListener`, `JetStreamMessage`, `JetStreamService`, `JetStreamServiceConfigData`,
`Listener`, `NatsPayload`, `Payload`, `PayloadBindingError`, `PayloadValidationError`, `PendingLimits`,
`Ping`, `Protocol`, `RetentionPolicy`, `RetryConfig`, `SecureSocket`, `Service`, `ServiceConfig`,
`ServiceConfigData`, `StorageType`, `StreamConfiguration`, `StreamServiceConfig`, `Tokens`.

**`old`: 8 gaps** — `Error`, `PayloadBindingError`, `PayloadValidationError`, `Listener`, `JetStreamListener`
(the 5 `// Unknown type:` placeholders) plus the 3 annotations `ServiceConfig`, `StreamServiceConfig`,
`Payload`, which had no section at all. `Listener` is the primary entry point for every NATS consumer
service, so this was a material gap in `old`.

**Submodule-only API: none.** The bala contains a single module directory (`modules/nats`), so the
`getDefaultModule()`-only extraction limitation costs nothing for this library.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `plugin_class: io.ballerina.stdlib.nats.plugin.NatsCompilerPlugin`,
packaged as `nats-compiler-plugin-3.3.1.jar`. Source at `compiler-plugin/src/main/java/io/ballerina/stdlib/nats/plugin/`:
`NatsCodeAnalyzer`, `NatsServiceAnalysisTask`, `NatsServiceValidator`, `NatsFunctionValidator`,
`NatsCodeTemplate`, `PluginConstants`, `PluginUtils`.

What it contributes:

- **Validations** on `nats:Service` / `nats:JetStreamService` implementations — `PluginConstants` defines
  diagnostics `NATS_101` ("Only one of either onMessage or onRequest is allowed"), `NATS_102` ("Service must
  have either remote method onMessage or onRequest"), plus parameter-count/type rules for `onError`
  (`ONLY_PARAMS_ALLOWED_ON_ERROR`, "Only nats:AnydataMessage …").
- **A code action** (`NatsCodeTemplate`) that inserts
  `remote function onMessage(nats:AnydataMessage message) returns nats:Error? { }` into a service missing it.
- **Recognised service methods** (`PluginConstants:28–30`): `onMessage`, `onRequest`, `onError`.
- **Payload annotation handling** (`PluginConstants:43` `"nats:Payload "`).

**Gap:** neither render surfaces this contract. `class Service {}` and `class JetStreamService {}` are empty
in both `old` and `new`, so an LLM reading the render has no declarative signal that a NATS service must
declare `onMessage` or `onRequest` with a `nats:AnydataMessage` parameter. The only hint is the README code
block (render lines 81–104), which shows `onMessage` and `onRequest` examples. This is a shared gap, not
introduced by `new`; `new` does at least now emit the `ServiceConfig`/`StreamServiceConfig`/`Payload`
annotations that services attach, which is a partial improvement in this area.

## 8. Other considerations

- **Version/stability:** 3.3.1, stable major, built for Ballerina `2201.12.0`. No `@deprecated` annotations
  anywhere in `modules/nats/*.bal`.
- **Bala vs. GitHub:** identical. All 12 `.bal` files in the bala diff clean against `ballerina/` at tag
  `v3.3.1`, so there is no published-vs-source drift to account for.
- **Size/token impact:** +94 lines (+17%). Cheap for what it buys — the entire `Listener` API and the
  annotation set. Render is 646 lines total, well within any practical context budget.
- **Doc quality:** doc comments and ```ballerina examples are preserved verbatim on all new declarations
  (`JetStreamListener.attach`, `Listener.'start`, etc.). Note the recurring trailing `# ` line before each
  declaration — cosmetic, present in both renders.
- **JSON redundancy:** `new`'s `annotations` array holds 5 entries for 3 annotations (one per attachment
  point). The renderer merges them correctly, so this costs only JSON bytes, not render correctness.
- **Practical effect for an LLM:** `old` would have made it impossible to write a NATS consumer service
  (no `Listener`, no `ServiceConfig`) and would have produced `natsClient->close()` and
  `new nats:JetStreamCaller()`. `new` fixes all three.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 552, new 646 |
| 2 | `git ls-remote --tags …module-ballerinax-nats \| grep 3.3.` | `v3.3.1` → `7e4fbbcc…` (exact tag exists) |
| 3 | `git clone --depth 1 --branch v3.3.1` into scratch `src` | succeeded |
| 4 | `diff` each bala `modules/nats/*.bal` vs clone `ballerina/*.bal` | 0 differences, 0 missing (12 files) |
| 5 | `ls bala/…/modules` | single module `nats`; `package.json` `"export": ["nats"]` |
| 6 | `grep -c '^// Unknown type:'` | old 5, new 0 |
| 7 | `grep -n '^// --- '` | old 4 markers (README/END README/Types/Client), new 5 (+ Annotations at 637) |
| 8 | `grep -cE '[a-z]+/[a-z.]+:[0-9]'` | old 3 lines (4 qualified refs total incl. `ballerinax/nats:nats:JetStreamCaller`), new 0 |
| 9 | `diff <(head -174 old) <(head -174 new)` | identical |
| 10 | Grouped `grep -c` by declaration kind (both files) | table in §2 |
| 11 | `grep -nE '^    (remote )?function '` on new | 31 lines − 2 README code-block lines = 29 methods, 14 remote |
| 12 | Python JSON signature extraction + `diff` (30 vs 29 signatures) | only difference: `JetStreamCaller.init\|Constructor\|\|->None` removed |
| 13 | Python JSON key/count dump | both: 37 typeDefs, 3 clients, 0 functions, 0 services, readme 4722 chars; annotations old 0 / new 5 |
| 14 | JSON `typeDef` categories | old `{Class, Constant, Enum, Error, None}`, new `{Class, Constant, Enum, Error, Record}` |
| 15 | `grep -n 'function ' bala client.bal` | `init:29`, `publishMessage:40` (remote), `requestMessage:69` (remote), `close:81` (**not** remote) |
| 16 | `sed -n '18,60p' jetstream_caller.bal` | class has only `ack`/`nak`/`inProgress`; **no `init`** |
| 17 | `grep -n 'function ' listener.bal` / `jetstream_listener.bal` | 6 `public isolated function` each; matches new render exactly |
| 18 | `grep -n 'function ' jetstream_client.bal` | `init` + 9 `isolated remote function`; matches new render |
| 19 | `sed -n '14,30p' error.bal` | `distinct error` / `distinct Error` / `distinct PayloadBindingError` → new renders all as `error` |
| 20 | `sed -n '58,68p' records.bal` | `record {| Protocol name; |} protocol?;` — new matches, old was version-qualified |
| 21 | `sed -n '16,26p' types.bal`, `'14,24p' jetstream_types.bal`, `grep annotation records.bal` | 3 annotations verified verbatim vs new lines 640/643/646 |
| 22 | 30-symbol public-export loop vs both renders | new: 0 missing; old: 5 missing (+3 annotations absent) |
| 23 | `grep -rn deprecated bala/modules/nats/*.bal` | no matches |
| 24 | `cat compiler-plugin.json`; `find compiler-plugin -name '*.java'` | 7 plugin classes; diagnostics `NATS_101`/`NATS_102`, code template inserting `onMessage` |
| 25 | `grep -P '[^\x00-\x7F]' new` | no matches (clean ASCII) |
| 26 | `sed -n` on new lines 176–192, 417–430, 505–545 | inspected error types, Service class, Client class as quoted in §3/§5 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific rendered lines are "not valid Ballerina" (§5.2, §5.3) are
  based on reading the language rules (required parameter after defaulted parameters; `typedesc<T> T = <>`
  inferred-typedesc syntax), not on running `bal build` over the render. The renders are documentation
  artifacts, not compilation units, so this is not expected to be actionable.
- The compiler-plugin behaviour in §7 is read from the Java source in the `v3.3.1` clone, not from decompiling
  the shipped `nats-compiler-plugin-3.3.1.jar` in the bala. Since every `.bal` file in the bala is byte-identical
  to the tag, the jar is assumed to correspond to the same source; this assumption is unverified.
- Ballerina Central registry metadata was not re-queried over the network; module list, version and keywords
  were taken from the bala's own `package.json`, which is the artifact the extractor actually consumed.
- The two `ballerina-vscode` source trees that produced the renders were not inspected; attribution of
  behaviour changes to "spec v2" follows the brief's stated setup and is consistent with what the JSONs show
  (e.g. `baseType` and `type` fields present only on the `new` side), but the extractor code itself was not read.

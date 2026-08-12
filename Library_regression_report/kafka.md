# ballerinax/kafka 4.6.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/kafka` |
| Pinned version | `4.6.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-kafka |
| Tag reviewed | `v4.6.5` (commit `a53c63a6d130590fa7b0c652b97cae6cc85af6ab`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/kafka/4.6.5/java21` |
| Old render | `936` lines |
| New render | `1011` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. The eight `// Unknown type:` stubs in `old`
(`Error`, `PayloadBindingError`, `PayloadValidationError`, `TopicPartitionTimestamp`,
`TopicPartitionOffset`, `Listener`, `AvroSerializer`, `AvroDeserializer`) are replaced by real
definitions; the `Serializer`/`Deserializer` object interfaces gain their method signatures; the
`kafka:Payload` annotation is emitted for the first time; version-qualified type references
(`ballerina/crypto:2.12.1:KeyStore`, `ballerinax/kafka:4.6.5:Error?`) are normalised to plain names;
and the service template now matches the compiler plugin's own code template. One line disappears
from `new` — a fabricated `function init() returns ballerinax/kafka:kafka:Caller;` on `Caller`,
which does not exist in the library source. Nothing correct in `old` is lost.

Diff volume: 82 added lines, 18 removed lines (`diff -u old new`).

## 2. Change inventory

Top-level declaration sets extracted with
`grep -oE '^(public )?(client )?(isolated )?(type|class|enum|const|annotation|function|service) …'`:
`old` = 67 declarations, `new` = 76.

**Only in `new` (9 — all were `// Unknown type:` stubs or absent in `old`):**

| Kind | Name | `new` form |
|---|---|---|
| type | `Error` | `type Error error;` |
| type | `PayloadBindingError` | `type PayloadBindingError error<record {|TopicPartition partition; int offset;|}>;` |
| type | `PayloadValidationError` | `type PayloadValidationError error<record {|record {|string topic; int partition;|} partition; int offset;|}>;` |
| type | `TopicPartitionTimestamp` | `type TopicPartitionTimestamp [TopicPartition, int];` |
| type | `TopicPartitionOffset` | `type TopicPartitionOffset [TopicPartition, OffsetAndTimestamp?];` |
| class | `Listener` | full body: `init` + `'start` + `gracefulStop` + `immediateStop` + `attach` + `detach` |
| class | `AvroSerializer` | `init` + `serialize` |
| class | `AvroDeserializer` | `init` + `deserialize` |
| annotation | `Payload` | `public annotation KafkaPayload Payload on parameter;` (new `// --- Annotations ---` section) |

**Only in `old`: none.**

**Modified in place (6 hunks):**

1. `SecureSocket.key` — `record {|ballerina/crypto:2.12.1:KeyStore keyStore; …|}|CertKey` → `record {|crypto:KeyStore keyStore; …|}|CertKey`.
2. `SecureSocket.protocol` — `record {|ballerinax/kafka:4.6.5:Protocol name; …|}` → `record {|Protocol name; …|}`.
3. `class Serializer` — empty body → gains `function serialize(anydata value, string schema, string subject) returns byte[]|error;` plus doc.
4. `class Deserializer` — empty body → gains `function deserialize(byte[] value) returns anydata|error;` plus doc.
5. `Consumer.init` / `Producer.init` return type — `ballerinax/kafka:4.6.5:Error?` → `Error?` (parameter lists byte-identical otherwise).
6. `Caller` — `function init() returns ballerinax/kafka:kafka:Caller;` removed.
7. Service section rewritten (see §3).

**Unchanged:** README block (lines 7–164, `readme` field byte-identical in both JSONs, 7463 chars),
all 70 `typeDefs` entries by name, 3 clients (`Caller`, `Consumer`, `Producer`), 1 service, 0
module-level functions. Remote-method name sets are identical: 29 distinct names, 35 occurrences in
both renders (`diff old.rfn new.rfn` → identical).

**JSON level:** 11 of 70 `typeDefs` differ. `new` adds `"type": "Class"` to `Listener` /
`AvroSerializer` / `AvroDeserializer` (which is why `old`'s renderer degraded them despite the data
being present — `Listener`'s JSON entry is 11.4 KB on *both* sides), adds `"baseType"` to the error
and tuple types, adds a `functions` array to `Serializer`/`Deserializer`, and drops the
version-qualified names. `annotations` goes 0 → 1.

## 3. Correctness against library source

Checked against the bala (`…/java21/modules/kafka/*.bal`), cross-read against the `v4.6.5` clone.

| `new` render claim | Source | Verdict |
|---|---|---|
| `type TopicPartitionTimestamp [TopicPartition, int];` | `types.bal:134` `public type TopicPartitionTimestamp [TopicPartition, int];` | exact |
| `type TopicPartitionOffset [TopicPartition, OffsetAndTimestamp?];` | `types.bal:147` | exact |
| `AvroSerializer.init(anydata & readonly schemaRegistryConfig, string schema) returns error?` | `types.bal:76` | exact |
| `AvroSerializer.serialize(anydata, string, string) returns byte[]|error` | `types.bal:81` | exact |
| `AvroDeserializer.init(anydata & readonly schemaRegistryConfig) returns error?` | `types.bal:102` | exact |
| `AvroDeserializer.deserialize(byte[]) returns anydata|error` | `types.bal:106` | exact |
| `Serializer.serialize(anydata value, string schema, string subject) returns byte[]|error` | `types.bal:67` | exact (source declares it on an `object` type, not a class — see §5) |
| `Deserializer.deserialize(byte[] value) returns anydata|error` | `types.bal:93` | exact |
| `Listener.'start/gracefulStop/immediateStop() returns error?` | `listener.bal:71,84,95` | exact |
| `Listener.attach(Service 'service, string[]|string|() name = ()) returns error?` | `listener.bal:105` (`string[]|string? name = ()`) | equivalent |
| `Listener.detach(Service 'service) returns error?` | `listener.bal:118` | exact |
| `public annotation KafkaPayload Payload on parameter;` | `kafka_records.bal:348` (identical text, incl. doc line 347) | exact |
| `Caller` has no `init` | `caller.bal:20` — `public client isolated class Caller {` declares only `'commit`, `commitOffset`, `seek`; no `init` | `new` correct, `old` fabricated one |
| `on new kafka:Listener(string|string[] bootstrapServers, kafka:ConsumerConfiguration config = {})` | `listener.bal:36` `init(string|string[] bootstrapServers, *ConsumerConfiguration config)` — `bootstrapServers` is required | `new` correct; `old` wrongly showed `bootstrapServers = ""` |
| `onConsumerRecord(kafka:Caller caller, kafka:AnydataConsumerRecord[] records)` | plugin code template `KafkaCodeTemplateWithCallerParameter.java:52` emits exactly `onConsumerRecord(kafka:Caller caller, …)`; bala README.md:68 shows the same order | matches the library's own canonical form |
| `onError(kafka:Error err) returns error?` | `KafkaFunctionValidator.java:167-190` — 1-param form must be `kafka:Error` | correct |
| service-block notes on `@kafka:Payload`, `anydata[]` batch binding, optional `caller` | `KafkaFunctionValidator.java:207-266` (`ARRAY_TYPE_DESC` → records-or-payload, `QUALIFIED_NAME_REFERENCE` → caller, 1–3 params, order not enforced) | consistent |

Error types (`module_errors.bal:18,21,24`) are rendered with a loss of qualifiers — see §5.

## 4. Regressions

**None found.**

What I checked to conclude that:
- Full `diff -u old new` (185 lines) read line by line: 18 removed lines, all accounted for — 8
  `// Unknown type:` stubs, 6 blank lines around them, 2 version-qualified `init` return-type lines
  replaced by unqualified ones, 1 `SecureSocket` field pair replaced by unqualified ones, and the
  `Caller.init` line.
- Declaration-set comparison: `comm -23 old.decls new.decls` → empty (nothing dropped).
- Remote-method comparison: 29 names / 35 occurrences on both sides, `diff` clean — no client method,
  parameter list, default, or return type was dropped from `Caller`, `Consumer`, or `Producer`.
- README: `readme` JSON field byte-identical (7463 chars); render lines 1–283 identical.
- The one removal, `Caller`'s `function init() returns ballerinax/kafka:kafka:Caller;`, is not a
  regression: `caller.bal` declares no `init`, and the emitted line was malformed anyway (an `init`
  cannot return the class type, and `ballerinax/kafka:kafka:Caller` is not valid syntax).

## 5. Issues in `new` (independent of `old`)

Three material inaccuracies exist in `new`. All are in newly-added content, so they replace nothing
— but they should be noted.

1. **`distinct` dropped from the error hierarchy.** `module_errors.bal:18-24` declares
   `public type Error distinct error;`, `PayloadBindingError distinct (Error & error<PartitionOffset>)`,
   `PayloadValidationError distinct (PayloadBindingError & error<PartitionOffset>)`.
   `new` renders `type Error error;`, and renders both subtypes as bare `error<…>` detail records.
   The subtype relationship (`PayloadValidationError <: PayloadBindingError <: Error`) is therefore
   invisible to a consumer of the render — an LLM cannot infer that catching `kafka:Error` catches
   the binding/validation errors. Source of the loss is the extractor: JSON `baseType` is `"error"` /
   `"error<record {|…|}>"` with no `distinct` and no intersection.
2. **Inconsistent expansion of `PartitionOffset`.** `PayloadBindingError` renders the detail as
   `record {|TopicPartition partition; int offset;|}` (named ref) while `PayloadValidationError`
   renders `record {|record {|string topic; int partition;|} partition; int offset;|}` (fully
   inlined). Both are structurally correct vs. `kafka_records.bal:187,196`, but the asymmetry is
   noise, and neither names `PartitionOffset`, which is a public type the render defines elsewhere.
3. **`Listener.init` is flattened with invented defaults.** Source is
   `init(string|string[] bootstrapServers, *ConsumerConfiguration config) returns Error?`. `new`
   emits all ~50 `ConsumerConfiguration` fields as positional parameters *and* a trailing required
   `ConsumerConfiguration config`, with defaults that do not exist in the record — e.g.
   `string groupId = ""`, `decimal sessionTimeout = 0.0d`, `SecureSocket secureSocket = {cert: {path: "", password: ""}}`
   (`kafka_records.bal:128-180`: those fields are all optional with no default). It also writes
   `SecurityProtocol securityProtocol = PLAINTEXT`, but `PLAINTEXT` is not a symbol in the module —
   the constant is `PROTOCOL_PLAINTEXT` (`constants.bal:124`). As written the signature would not
   compile, and it contradicts the service block two sections later, which correctly shows
   `new kafka:Listener(bootstrapServers, config)`.
   **This is a pre-existing extractor behaviour, not a spec-v2 defect**: the byte-identical
   flattening already appears in `old` for `Consumer.init` and `Producer.init` (render.diff hunks
   @@ -712 and @@ -887 show the parameter lists unchanged between sides). It becomes visible for
   `Listener` only because `old` degraded `Listener` to a stub.

Shared with `old` (not new-side issues, listed for completeness):
- `Serializer` and `Deserializer` are rendered as `class`, but `types.bal:59,87` declare them as
  `object` *types* (`public type Serializer isolated object {…}`). Same for `Service`
  (`types.bal:42`, `distinct service object`), rendered `class Service {}` on both sides.
- Union types built from constants are expanded to string literals on both sides
  (`type OffsetResetMethod "earliest"|"latest"|"none";` at new:430 vs. source
  `OFFSET_RESET_EARLIEST|OFFSET_RESET_LATEST|OFFSET_RESET_NONE`).
- Mixed qualification: Types/Client sections use unqualified names, the Service section uses
  `kafka:` prefixes. Both sides.
- No encoding problems: the em-dashes in `new`'s service commentary are well-formed UTF-8.

## 6. Coverage gaps vs. the library

**Zero gaps.** `package.json` declares `"export": ["kafka"]` and `modules/` contains only `kafka`,
so there is no submodule API and hence no shared submodule gap for this library.

All 66 public top-level symbols declared in `modules/kafka/*.bal`
(`grep -hoE '^public (isolated |client |distinct )*(type|class|enum|const|annotation) [A-Za-z_0-9]+'`)
appear in both renders. All 28 public constants are present as `const string NAME = "…";` in both.
There are no public module-level functions in the source (JSON `functions` = 0 on both sides,
confirmed by grep over the bala).

The difference is quality, not coverage: in `old`, 8 of those 66 symbols appear only as
`// Unknown type: <Name>` with no members (`grep -c '^// Unknown type:'` → 8 in `old`, 0 in `new`).

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` ships `kafka-compiler-plugin-4.6.5.jar`. Source reviewed at
`compiler-plugin/src/main/java/io/ballerina/stdlib/kafka/plugin/`.

- **Validations** (`KafkaFunctionValidator`, `KafkaServiceValidator`): a `kafka:Service` must have
  `onConsumerRecord`; it takes 1–3 parameters drawn from `kafka:Caller`, a consumer-record array, and
  an `@kafka:Payload` data array; `onError` takes `kafka:Error` (+ optional `kafka:Caller`).
- **Code actions**: `KafkaCodeTemplateWithCallerParameter` /
  `KafkaCodeTemplateWithoutCallerParameter` insert the `onConsumerRecord` skeleton.
- **Surfacing in the render**: `new`'s Service section reproduces the plugin's contract closely —
  caller-first parameter order (matching the with-caller template verbatim), required/optional
  markers, the `@kafka:Payload` note pointing at `kafka:KafkaPayload`, `kafka:BytesConsumerRecord[]`
  and `anydata[]` as alternative bindings, and the one-service-per-listener rule. `old` conveyed none
  of this beyond two bare method signatures.
- **Not surfaced on either side**: the plugin's specific diagnostic codes (KAFKA_101…KAFKA_114) and
  the rule that a `@kafka:Payload` parameter and a consumer-record parameter can coexist only in the
  3-parameter form. Minor; the render's prose covers the practical cases.

## 8. Other considerations

- Not deprecated; stable major version (4.x); built for `ballerina_version` 2201.12.0, platform
  `java21`.
- Size: +75 lines (+8.0%) — a small token cost for eight previously-unusable type definitions, a
  fully specified `Listener`, and the annotation.
- The single largest line in `new` is the flattened `Listener.init` (~1.9 KB on one line), matching
  the pre-existing `Consumer.init` / `Producer.init` lines. Three such lines now instead of two.
- The service block's guidance text is hand-authored prose from the spec-v2 trigger metadata, not
  derived from the bala; it was checked against the compiler plugin and found consistent.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags …module-ballerinax-kafka \| grep 4.6.` | `v4.6.5` → `a53c63a6…` |
| `git clone --depth 1 --branch v4.6.5 …` | succeeded |
| `wc -l old/new render` | 936 / 1011 |
| `grep -c '^// Unknown type:'` | old 8, new 0 |
| `grep -n '^// Unknown type:' old` | 628 Error, 630 PayloadBindingError, 632 PayloadValidationError, 646 TopicPartitionTimestamp, 659 TopicPartitionOffset, 678 Listener, 680 AvroSerializer, 682 AvroDeserializer |
| `grep -n '^// --- ' old / new` | old: README/Types/Client/Service; new: same + `Annotations` at 1008 |
| `diff -u old new \| grep -c '^+[^+]' / '^-[^-]'` | 82 added / 18 removed (185-line diff) |
| declaration sets via `comm` | only-in-old: 0; only-in-new: 9 (listed §2) |
| `grep -oE '^    remote function …' \| sort \| uniq -c`, both sides | 29 names, identical sets; 35 total occurrences each |
| JSON section sizes | both: typeDefs 70, clients 3, functions 0, services 1; annotations old 0 / new 1; readme 7463 both, byte-identical |
| JSON typeDef diff | 11 differ: SecureSocket, Error, PayloadBindingError, PayloadValidationError, Serializer, Deserializer, TopicPartitionTimestamp, TopicPartitionOffset, Listener, AvroSerializer, AvroDeserializer |
| JSON `Listener` old vs new | 11412 vs 11406 chars; only `"ballerinax/kafka:4.6.5:Error?"` → `"Error?"` and added `"type": "Class"` |
| JSON `Error` baseType | new `"error"` — no `distinct` |
| `bala .../modules/` listing | single module `kafka`; `package.json` `export: ["kafka"]` |
| public-symbol coverage loop over 66 symbols | 0 missing from `new`, 0 missing from `old` |
| `caller.bal:20-59` | no `init` declared |
| `listener.bal:36` | `init(string|string[] bootstrapServers, *ConsumerConfiguration config) returns Error?` |
| `types.bal:59-110` | `Serializer`/`Deserializer` are object types; `AvroSerializer`/`AvroDeserializer` are isolated classes with the rendered signatures |
| `types.bal:134,147` | tuple types match render exactly |
| `module_errors.bal:18,21,24` | `distinct` + intersections, not reflected in render |
| `kafka_records.bal:128-180` | ConsumerConfiguration fields optional / defaults — contradicts flattened `init` defaults |
| `kafka_records.bal:347-348` | annotation text matches render verbatim |
| `constants.bal:124` | constant is `PROTOCOL_PLAINTEXT`, render writes `PLAINTEXT` |
| `PluginConstants.java:28-53`, `KafkaFunctionValidator.java:160-300` | service contract as described in §7 |
| `KafkaCodeTemplateWithCallerParameter.java:52` | `onConsumerRecord(kafka:Caller caller, …)` — matches `new` |
| bala `docs/README.md:68` | `onConsumerRecord(kafka:Caller caller, kafka:BytesConsumerRecord[] records)` |

## 10. Caveats and unverified items

- The compiler-plugin JAR in the bala was not decompiled; plugin behaviour was read from the
  `v4.6.5` GitHub sources. The bala's `modules/kafka/*.bal` matched the clone's `ballerina/*.bal` for
  every construct I quoted, so divergence is unlikely but not formally proven for the plugin.
- Neither render was compiled. Claims that the flattened `Listener.init` "would not compile" rest on
  reading (`PLAINTEXT` undefined; a required parameter after defaulted ones), not on a `bal build`.
- The service-section prose in `new` originates from spec-v2 trigger metadata that I did not read
  directly; I verified its assertions against the compiler plugin and README instead.
- I did not attempt to re-run the two-stage render pipeline; both renders and JSONs were taken as
  given, and the `old`/`new` provenance (source branches/commits) is from the brief, not
  independently verified.

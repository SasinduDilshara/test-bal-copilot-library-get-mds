# `new/` re-render regression report — `e194a26` vs the committed `new/`

## What is being compared

| | Baseline (`new/` at `HEAD`) | Candidate (regenerated `new/`) |
|---|---|---|
| Repo | local `Check-PR-s/ballerina-vscode` | local `Check-PR-s/ballerina-vscode` |
| Branch | `L1_copilot_metadata_clean` | `fix_identify_issues_after_the_v2_pr_break` |
| Commit | `db90b07c1e0ff83b591e56e67861f700f16603ea` | `e194a26774cc71ec4452faa03b3f447507212c5d` |
| Commit in this repo | `360df54` | working tree |

Both runs rendered the **same 206 libraries at the same pinned versions** — the two
`resolved-versions-new.txt` reports are byte-identical, 206/206 `PIN_OK`. There is no library drift,
so **every difference below is attributable to the source change**, not to a different bala.

`old/` was not touched (0 files changed under any `*/old/`).

## Bottom line

**Not clean. 18 of the 22 changed libraries are improvement-only; 4 carry a real regression, and one of
them (`ballerina/ai`) is serious.**

| | count |
|---|---|
| Libraries byte-identical to baseline | **184** |
| Libraries changed | **22** (44 files: 22 `.json` + 22 `.bal.txt`) |
| — improvement only | 16 |
| — improvement with a minor documented loss | 2 (`mysql`, `postgresql`) |
| — **carrying a regression** | **4** (`ai`, `file`, `ftp`, `kafka`) |

Pipeline health is unchanged and good: `// Unknown type:` = 0, empty renders = 0, all JSON parses with
matching `name`, all headers present.

Net line delta across the renders: **+273 / −113**. Every one of the 113 deleted lines is accounted for
in §1–§3 below.

---

## 1. CONFIRMED REGRESSION — `ballerina/ai` 1.13.0: 17 parameter defaults became wrong

Three client-class `init` signatures changed. 19 defaults moved; **2 improved, 17 became factually
wrong**. Ground truth is `ai:ConnectionConfig` (`modules/ai/types.bal:61`) and, for `McpToolKit`,
`http:CommonClientConfiguration` (`modules/http/http_types.bal:73`) reached through
`mcp:StreamableHttpClientTransportConfig`.

### `McpToolKit.init` — 9 changed

| Parameter | Declared default (ground truth) | Baseline | Candidate | |
|---|---|---|---|---|
| `httpVersion` | `HTTP_2_0` | `http:HTTP_2_0` | `"2.0"` | OK (equivalent literal) |
| `compression` | `COMPRESSION_AUTO` | `AUTO` | `"AUTO"` | **better** (`AUTO` alone was not a valid reference) |
| `timeout` | `30` | `30` | `0.0d` | **WRONG** |
| `forwarded` | `"disable"` | `"disable"` | `""` | **WRONG** |
| `retryConfig` | *(optional, none)* | `()` | `{}` | **WRONG** |
| `cookieConfig` | *(optional, none)* | `()` | `http:COMPRESSION_AUTO` | **WRONG + type-invalid** |
| `responseLimits` | `{}` | `{}` | `()` | **WRONG + type-invalid** |
| `validation` | `true` | `true` | `false` | **WRONG** |
| `sessionId` | *(optional `string`)* | `""` | `{}` | **WRONG + type-invalid** |

### `Wso2EmbeddingProvider.init` and `Wso2ModelProvider.init` — 5 changed each

| Parameter | Declared default | Baseline | Candidate | |
|---|---|---|---|---|
| `httpVersion` | `HTTP_2_0` | `http:HTTP_2_0` | `"2.0"` | OK |
| `timeout` | `60` | `60` | `0.0d` | **WRONG** |
| `forwarded` | `"disable"` | `"disable"` | `{}` | **WRONG + type-invalid** |
| `compression` | `COMPRESSION_AUTO` | `AUTO` | `"disable"` | **WRONG** (it picked up `forwarded`'s default) |
| `validation` | `true` | `true` | `false` | **WRONG** |

The baseline matched the declared defaults on **all 19**. The signature — `compression` receiving
`forwarded`'s value, `cookieConfig` receiving a `Compression` constant, a `string` receiving `{}` — is
defaults **landing on the wrong parameter**, not a deliberate change of formatting.

Five of the 17 are not merely wrong values but **type-invalid Ballerina**: `string forwarded = {}` (×2),
`string sessionId = {}`, `http:CookieConfig|() cookieConfig = http:COMPRESSION_AUTO`,
`http:ResponseLimitConfigs responseLimits = ()`.

### What was ruled out

- **Not flaky.** Stage 1 was re-run for `ballerina/ai` alone on the same branch and same home; the JSON
  came back byte-identical to the committed candidate (`diff` = 0 lines). Deterministic.
- **Not library drift.** `ballerina/ai` resolved `1.13.0 PIN_OK` in both runs.
- **Not the extraction code.** `copilot/util/TypeSymbolExtractor.java`, `copilot/util/SymbolProcessor.java`,
  `copilot/util/LibraryModelConverter.java` and `copilot/model/Parameter.java` are **byte-identical
  (md5-equal) between the two branches**. `copilot/model/Type.java` differs only by an additive
  `subtypeFamily` field. So the trigger is somewhere else in the branch and the root cause is **not
  identified** — this needs an owner on the extension side.

### Context: this is a pre-existing defect class that the branch widened

The same wrong-default signature already exists in the baseline for other libraries and is **unchanged**
by this run — `ballerina/http` renders `decimal timeout = 0.0d`, `boolean validation = false`,
`string forwarded = ""` on both sides, against declared defaults of `30`, `true`, `"disable"`.

| Signature | Baseline | Candidate |
|---|---|---|
| `decimal timeout = 0.0d` | 16 occurrences / 10 libraries | 19 / 10 |
| `boolean validation = false` | 9 / 6 | 12 / 6 |
| `string forwarded = ""` | 8 / 5 | 9 / 5 |

Every added occurrence is in `ballerina/ai` (which went from 1 affected `init` to 4). No new library
entered the defect; `ai` fell further into it.

---

## 2. CONFIRMED REGRESSION — `ballerina/file` 1.13.0: handlers lost `returns error?` on a false premise

`onCreate`, `onModify` and `onDelete` changed from

```ballerina
remote function onCreate(file:FileEvent event) returns error?;
```

to

```ballerina
# ... Declares no return type; the file module rejects any return clause on this handler.
remote function onCreate(file:FileEvent fileEvent); // optional
```

**The premise is wrong.** Decompiling `file-compiler-plugin-1.13.0.jar`,
`FileServiceValidator.validateReturnType` returns without a diagnostic when the return type descriptor is
**empty** *or* when it `isErrorOrNilType`; only anything else raises `FILE_104`. The diagnostic string is
literally *"invalid return type in the remote function `{0}`, only `error?` return type is allowed"* — so
`returns error?` is explicitly permitted. The baseline form compiles; the render now tells the model it
does not.

Net effect: 3 `methods[].return` blocks removed from the JSON, and a false constraint sentence added.

The rest of the `file` change is an improvement (listener/service descriptions, the "must declare at least
one of onCreate/onModify/onDelete" rule, per-parameter prose).

---

## 3. CONFIRMED REGRESSION — `ballerina/ftp` 2.20.1: 6 exclusivity rules deleted

The baseline carried six `structure.atMostOne` rules:

```
# onFileChange and onFileCsv cannot coexist: onFileChange already reports every file in the poll,
# so the typed handler would process the same file twice.
   ... same for onFileJson, onFileXml, onFileText, onFile, onFileDelete
```

All six are gone. This is an **authoring deletion, not a resolver failure** — in
`model-generator-commons/src/main/resources/trigger-metadata-models/ftp/trigger-metadata.json` the
candidate branch keeps only `$atLeastOneFileHandler`. The baseline declared seven rules —
`$eventVsFormatCsv`, `$eventVsFormatJson`, `$eventVsFormatXml`, `$eventVsFormatText`,
`$eventVsFormatFile`, `$eventVsFormatDelete`, `$atLeastOneFileHandler` — the candidate declares one.

`onFileChange` is still offered by the render (correctly marked `@deprecated`), so nothing now stops a
model from declaring it beside `onFileText` — the double-processing the deleted rules warned about.

Note the branch also migrated rule subjects from name-addressing to id-addressing
(`{"kind":"handler","name":"onFileChange"}` → `{"kind":"handler","id":"$service.onFileCsv"}`), per spec
§6.1.1. The six rules were not migrated — they were removed. **Confirm whether that was intended.**

Repo-wide: `cannot coexist` went 8 → 2. The 2 survivors are `websocket`'s, which were kept.

---

## 4. PROBABLE REGRESSION — `ballerinax/kafka` 4.6.5: `@kafka:Payload` slot removed

The `records` parameter of `onConsumerRecord` lost:

```
# The `records` parameter may carry @kafka:Payload, written `@kafka:Payload {}` before its type.
# Its fields are those of kafka:KafkaPayload.
```

Again an authoring deletion — `kafka/trigger-metadata.json` dropped the `$payload` annotation entry and
its `annotationRefs` reference on `params[1]`.

Evidence it is still valid: `kafka_records.bal:348` declares
`public annotation KafkaPayload Payload on parameter;`, and `kafka-compiler-plugin-4.6.5.jar` actively
validates it (`hasPayloadAnnotation`, `payloadExists`, the literal `kafka:Payload`). `ballerinax/rabbitmq`
**kept** its structurally identical `@rabbitmq:Payload` hint in the same run, so the two connectors are now
inconsistent.

Marked *probable* rather than confirmed because I did not establish that the plugin accepts the annotation
specifically on the batch `records` parameter as opposed to a separate payload parameter. **Needs a
one-line confirmation from the connector owner.**

---

## 5. Improvement with a minor loss — `ballerinax/mysql` and `ballerinax/postgresql` 1.19.0

**The loss:** 9 lines of parameter-optionality guidance disappeared
(`# Required parameters: afterEntry` / `# Optional parameters (may be omitted): tableName`, 4 in `mysql`,
5 in `postgresql`).

**Why it is minor:** this is normalization, not a targeted removal. `mssql`, `oracledb` and `cdc` never had
those lines; `mysql` and `postgresql` were the outliers because they were previously rendered by the
generic path. All five CDC renders are now consistent. The gap (nothing states that `tableName` may be
omitted) is now uniform across the CDC family rather than present in two of five.

**Why the net is strongly positive:** the baseline render was **uncompilable**.

```ballerina
service mysql:Service on new mysql:CdcListener(...)          // baseline
```

`ballerinax/mysql` 1.19.0 declares **no `Service` type at all** (verified against the bala: the package has
one module, `mysql`, with no `Service`/`CdcService` declaration). The candidate emits the correct form:

```ballerina
@cdc:ServiceConfig {...} // required
service cdc:Service on new mysql:CdcListener(...)
# Requires: import ballerinax/mysql.cdc.driver as _;
```

plus the mandatory annotation and the driver import, neither of which the baseline mentioned. Same for
`postgresql`. `oracledb` gained a complete Service section it previously did not have at all.

---

## 6. Improvements verified against the pinned balas

Everything the candidate newly asserts was checked against the bala or the compiler-plugin jar at the
pinned version. All of the following are correct:

| Library | New content | Verification |
|---|---|---|
| `ballerina/mqtt` | `onError`, `onComplete(mqtt:DeliveryToken)` handlers added | `mqtt-compiler-plugin-1.4.1.jar` `PluginConstants`/`MqttServiceValidator` recognise exactly `onMessage`, `onError`, `onComplete`; `DeliveryToken` is in `types.bal:111` |
| `ballerina/tcp` | new `ConnectionService` section (`onBytes`/`onError`/`onClose`) | `tcp/service.bal:24` declares `ConnectionService` with those three optional remote methods |
| `ballerinax/salesforce` | `salesforce:Service` split into `CdcService` + `PlatformEventsService`, required `"identifier"`, `listenerConfig` default dropped | `service_types.bal:18` `public type Service CdcService\|PlatformEventsService`; `listener.bal:54` `init(ListenerConfig listenerConfig)` — **no** default, so the baseline's `= {auth: {...}}` was fabricated |
| `ballerinax/asb`, `ballerinax/aws.sqs` | `caller` parameter, settle/delete semantics | `asb/caller.bal:20`, `aws.sqs/caller.bal:20` |
| `ballerinax/mysql`/`postgresql`/`mssql`/`oracledb` | `cdc:Service` + `@cdc:ServiceConfig` + driver import | see §5 |
| `ballerinax/solace` | mandatory `@solace:ServiceConfig`, queue-or-topic exclusivity | `annotations.bal:21`; `ServiceConfiguration = QueueServiceConfiguration\|TopicServiceConfiguration` |
| `http`, `graphql`, `grpc`, `mcp`, `websocket`, `rabbitmq` | 15 new "may be narrowed" hints; `http:StatusCodeResponse` added to the resource return union | additive, consistent with the spec §1.4 `subtypeFamily` flag added in `Type.java` |
| 27 libraries | `services[].description` + `services[].listener.description` | additive prose, no structural change |

Aggregate signal counts, baseline → candidate:

| Signal | Baseline | Candidate |
|---|---|---|
| `must declare at least one` | 4 | 8 |
| `must carry the` (mandatory annotation) | 10 | 14 |
| `from exactly one source` | 2 | 3 |
| `may bind to a record that includes` | 2 | 4 |
| `may be narrowed` | 0 | 15 |
| `cannot coexist` | 8 | **2** |
| `Required/Optional parameters:` | 45 | **39** |

---

## 7. Recommended actions

| # | Action | Owner |
|---|---|---|
| 1 | Fix the `ballerina/ai` parameter-default misassignment. Reproduce with the `ai`-only probe; note the extraction classes are unchanged between branches, so the trigger is elsewhere. Five of the emitted defaults are type-invalid. | extension |
| 2 | Restore `returns error?` on `file`'s `onCreate`/`onModify`/`onDelete` and delete the "rejects any return clause" sentence. | metadata authoring |
| 3 | Confirm whether `ftp`'s six `atMostOne` rules were dropped deliberately or lost in the name→id migration; if the latter, re-author them with `id` subjects. | metadata authoring |
| 4 | Confirm whether `@kafka:Payload` on `records` was removed deliberately; if not, restore it for parity with `rabbitmq`. | connector owner |
| 5 | Optional: consider whether the CDC family should carry parameter-optionality notes at all, so `mysql`/`postgresql` losing them is a decision rather than a side effect. | metadata authoring |
| 6 | Housekeeping: `SUMMARY.md` still names `L1_json_and_annotations_with_spec_v2` / `412ba01e` as the `new` side. The committed baseline actually came from `L1_copilot_metadata_clean` / `db90b07`, and now from `e194a26`. | this repo |

Also worth noting as **pre-existing and untouched** (not regressions of this run): `ballerinax/mongodb`
renders `string connection = {}` on both sides, and the `http`/`mcp`/`websocket`/`websubhub`/`email`/
`graphql`/`websub`/`ai.agent`/`ai.devant` family carries the wrong-default signature described in §1 on
both sides.

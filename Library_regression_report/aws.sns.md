# ballerinax/aws.sns 4.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.sns` |
| Pinned version | `4.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.sns |
| Tag reviewed | `v4.0.1` (commit `3e53fe94cc9d6ffaac7b18ca2bc984ceae7902fa`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.sns/4.0.1` |
| Old render | `1237` lines |
| New render | `1245` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. It fixes four distinct classes of defect and
introduces none:

1. **7 mangled stream return types repaired.** `old` emitted `returns Error?>` — a truncated
   `stream<T, Error?>` that is neither valid Ballerina nor interpretable. `new` emits the full
   `stream<string, Error?>`, `stream<Subscription, Error?>`, etc.
2. **6 error types recovered.** `old` degraded the entire `error.bal` type hierarchy to
   `// Unknown type:` stubs. `new` emits real definitions with doc comments.
3. **A phantom parameter removed.** `old`'s `tagResource` carried an invented parameter
   `string Additional Values` that does not exist in the library. `new` drops it.
4. **`close()` correctly de-`remote`-ed**, and 2 `@display` annotations recovered.

All 43 client methods and all 150 typeDef names are present on both sides; nothing was dropped.
Coverage against the bala's default module is complete (0 missing public symbols). The residual
inaccuracies I found in `new` are all shared with `old` (wrong defaults on two parameters, `*Tags`
included-record marker lost, undeclared type prefixes) plus one new-only fidelity loss (the
`distinct` error subtype hierarchy is flattened).

## 2. Change inventory

Line counts: `old` 1237, `new` 1245 (+8).

JSON-level (structural, not textual):

| | old | new |
|---|---|---|
| `typeDefs` entries | 150 | 150 (identical name list, in identical order) |
| `clients` | 1 | 1 |
| client `functions` | 43 | 43 (identical name set) |
| `functions` / `services` / `annotations` (module level) | 0 / 0 / 0 | 0 / 0 / 0 |
| client object has `annotations` key | no | yes |
| `typeDefs` entries that differ | — | 10 |
| client functions that differ | — | 8 |

Render-level declaration counts:

| kind | old | new |
|---|---|---|
| `^type ` declarations | 28 | 34 |
| `^const ` | 100 | 100 |
| `^enum ` | 16 | 16 |
| `client class` | 1 | 1 |
| `@display` lines | 0 | 2 |
| `remote function` (client) | 42 | 41 |
| `function` (client) | 1 | 2 |
| `// Unknown type:` lines | 6 | 0 |
| version-qualified type refs (`org/mod:x.y.z:Type`) | 4 | 0 |

**Added in `new` (6 type declarations)** — `Error`, `GenerateRequestFailed`, `OperationError`,
`ResponseHandleFailedError`, `CalculateSignatureFailedError`, `InternalError`. These replace the six
`// Unknown type:` stubs at old lines 337–347. JSON gained `"baseType": "error"` on each.

**Added in `new` (2 annotations)** — `@display {label: "Amazon SNS Client", iconPath: "icon.png"}`
on the client class, `@display {label: "Connection Config"}` on `ConnectionConfig`.

**Modified in `new` — return types (7 client methods).** All were `returns Error?>` in `old`:

| method | new return type |
|---|---|
| `listTopics` | `stream<string, Error?>` |
| `listSubscriptions` | `stream<Subscription, Error?>` |
| `listPlatformApplications` | `stream<PlatformApplication, Error?>` |
| `listEndpoints` | `stream<Endpoint, Error?>` |
| `listSMSSandboxPhoneNumbers` | `stream<SMSSandboxPhoneNumber, Error?>` |
| `listOriginationNumbers` | `stream<OriginationPhoneNumber, Error?>` |
| `listPhoneNumbersOptedOut` | `stream<string, Error?>` |

**Modified in `new` — parameters (1 client method).** `tagResource`: `(string topicArn,
string Additional Values, Tags tags)` → `(string topicArn, Tags tags)`.

**Modified in `new` — qualifier (1 client method).** `close`: `remote function` → `function`.
The JSON for `close` is byte-identical on both sides (`"type": "Normal Function"`); only the
renderer changed, so `old` was mis-rendering the `Normal Function` tag as `remote`.

**Modified in `new` — de-qualified type refs (4 sites, 4 typeDefs):**

| old (line) | new |
|---|---|
| `type Message string\|ballerinax/aws.sns:4.0.1:MessageRecord;` (821) | `string\|MessageRecord` |
| `type MessageAttributeValue string\|ballerinax/aws.sns:4.0.1:StringArrayElement[]\|…` (827) | `string\|StringArrayElement[]\|…` |
| `map<ballerinax/aws.sns:4.0.1:MessageAttributeValue> attributes?;` (838, in `PublishBatchRequestEntry`) | `map<MessageAttributeValue>` |
| `ballerinax/aws:1.0.1:Region\|string region?;` (991, in `ConnectionConfig`) | `aws:Region\|string` |

**Removed in `new`:** nothing except the 6 `// Unknown type:` stubs and the phantom
`Additional Values` parameter. README section (lines 7–133) is byte-identical
(`diff` on the region returns empty). The 17 `// Special Agent Note:` external-package annotations
are preserved 17/17.

## 3. Correctness against library source

Upstream `v4.0.1` and the bala are **byte-identical** for all 9 `.bal` files
(`client.bal`, `constants.bal`, `data_mappings.bal`, `error.bal`, `response_types.bal`,
`stream_types.bal`, `types.bal`, `utils.bal`, `validators.bal`), so there is no source/bala
disagreement to adjudicate.

Every change `new` makes is confirmed correct against the source:

- **Stream returns.** `client.bal:119` `isolated remote function listTopics() returns stream<string, Error?>`;
  `:364` `listSubscriptions(string? topicArn = ()) returns stream<Subscription, Error?>`;
  `:475` `listPlatformApplications() returns stream<PlatformApplication, Error?>`;
  `:704` `listOriginationNumbers() returns stream<OriginationPhoneNumber, Error?>`;
  `:714` `listPhoneNumbersOptedOut() returns stream<string, Error?>`.
  (`listEndpoints` `:571` and `listSMSSandboxPhoneNumbers` `:662` wrap their return onto the next
  line; element types `Endpoint` / `SMSSandboxPhoneNumber` confirmed there.) All 7 match `new`.
- **`tagResource`.** `client.bal:759` `isolated remote function tagResource(string topicArn, *Tags tags) returns Error?`
  — two parameters, confirming `Additional Values` in `old` was invented.
- **`close`.** `client.bal:979` `public isolated function close() returns Error?` — **not** remote.
  `new` is right, `old` was wrong.
- **`@display`.** `client.bal:30` `@display {label: "Amazon SNS Client", iconPath: "icon.png"}`;
  `types.bal:570` `@display {label: "Connection Config"}`. Both reproduced verbatim; these are the
  only two `@display` annotations in the module.
- **Error types.** `error.bal:18–33` declares exactly the six types `new` emits, with the same doc
  comments (including the upstream typo "Reperesents"). See §5.1 for the fidelity caveat.
- **`Region`.** `Ballerina.toml`/`Dependencies` place `Region` in `ballerinax/aws`; the field doc
  itself says "an `aws:Region` enum member", so `new`'s `aws:Region` matches the library's own prose.

Full signature sweep: I compared all 43 rendered client signatures against the 43
`function` declarations in `client.bal` (lines 41–979). Names, arities and return types match
one-for-one, with the exceptions catalogued in §5.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full `diff -u old new` reviewed line by line (the whole diff is 10 hunks, all listed in §2).
  Nothing is removed except the 6 `// Unknown type:` stubs and the phantom parameter.
- Declaration name sets compared: `type` names — `new` is a strict superset (6 added, 0 removed);
  client method names — identical 43-element set (`diff` of the sorted name lists is empty).
- JSON `typeDefs` name list is identical and in the same order (150 = 150); client `functions`
  count identical (43 = 43); module-level `functions`/`services`/`annotations` are empty on both.
- README block (render lines 7–133) is byte-identical.
- `// Special Agent Note:` external-package annotations: 17 on both sides.
- `const` count 100 = 100, `enum` count 16 = 16.

One borderline item, which I deliberately do **not** count as a regression: `old` line 991 carried
`ballerinax/aws:1.0.1:Region|string`, which named the owning package and version; `new` emits
`aws:Region|string` and attaches no `// Special Agent Note`, so the render no longer states in-band
that `Region` comes from `ballerinax/aws`. I do not score this as a regression because (a) the `old`
form was not valid Ballerina and could only mislead a code-generating consumer, (b) the field's own
doc comment two lines above already says "an `aws:Region` enum member", and (c) the same record's
`auth` and `endpoint` fields do carry Special Agent Notes naming `ballerinax/aws.auth` and
`ballerinax/aws`, so the package is discoverable from immediate context.

## 5. Issues in `new` (independent of `old`)

Six inaccuracies vs. the library source remain in `new`. Items 5.2–5.6 are shared with `old`
(i.e. not caused by spec v2); only 5.1 is specific to what `new` newly emits.

**5.1 — Error subtype hierarchy is flattened (new-only).**
`new` emits all six error types as `type X error;`. Source (`error.bal:18–33`) is:

```
public type Error distinct error;
public type GenerateRequestFailed distinct Error;
public type OperationError distinct Error;
public type ResponseHandleFailedError distinct Error;
public type CalculateSignatureFailedError distinct Error;
public type InternalError distinct Error;
```

Two facts are lost: the `distinct` qualifier, and the fact that the five specific errors are
subtypes of `Error` rather than siblings of it. The JSON only carries `"baseType": "error"` for all
six, so the loss originates in the extractor, not the renderer. Impact: a consumer cannot infer that
`catch`ing / matching `sns:Error` also covers `sns:OperationError`. Still a large net gain over
`old`, which emitted nothing at all for these types.

**5.2 — Wrong default on `publish`'s `targetType` (shared with `old`).**
Render: `remote function publish(string target, Message message, TargetType targetType = "PHONE_NUMBER", …)`.
Source `client.bal:181`: `TargetType targetType = TOPIC`. `TargetType` is `{TOPIC, ARN, PHONE_NUMBER}`
(`types.bal:90–94`), so the render advertises the *third* member as the default instead of the first.
This is materially misleading — code written against the render would publish to a phone number by
default instead of a topic.

**5.3 — Wrong default and widened type on `createSMSSandboxPhoneNumber`'s `languageCode` (shared).**
Render: `"zh-TW"|"zh-CN"|…|"en-US"|() languageCode = ()`.
Source `client.bal:633`: `LanguageCode? languageCode = EN_US`. The named enum `LanguageCode`
(`types.bal:153`) is expanded into a 13-member string-literal union, and the default `EN_US` is
reported as `()`.

**5.4 — Included-record parameter marker lost on `tagResource` (shared).**
Render: `tagResource(string topicArn, Tags tags)`. Source `client.bal:759`: `*Tags tags`. The `*`
(included record parameter) is dropped and the JSON additionally marks `tags` `"optional": true`.
`tagResource` is the only function in the module using an included record parameter.

**5.5 — Inconsistent `sns:` prefix inside a signature (shared).**
`publish` renders its attributes parameter as `map<sns:MessageAttributeValue>|()` while every other
internal reference in the render is unqualified (e.g. `PublishBatchRequestEntry` uses
`map<MessageAttributeValue>`). Source `client.bal:182` is `map<MessageAttributeValue>?`.

**5.6 — Undeclared type prefixes; render is not compilable as-is (shared).**
The only import line is `import ballerinax/aws.sns;`, yet the body uses `aws:Region`,
`aws:EndpointConfig`, `auth:AuthConfig`, `auth:AssumeRoleConfig`, `auth:ProcessAuthConfig`,
`auth:SsoAuthConfig`, `auth:WebIdentityConfig`, `aws:US*`, `auth:DEFAULT*` and `sns:MessageAttributeValue`.
This is a renderer-wide convention (external types carry `// Special Agent Note` comments instead of
imports), not an aws.sns-specific defect, but it is worth stating that the artifact is a reference
document, not compilable source.

Stylistic, not counted: `returns Error|()` is emitted where the source writes `Error?` (both sides,
all 20 such methods); type declarations omit the `public` qualifier throughout (both sides).

## 6. Coverage gaps vs. the library

**Zero gaps.**

- `package.json` `"export": ["aws.sns"]` and `modules/` contains exactly one directory, `aws.sns` —
  the default module. There is **no submodule-only API**, so the known `getDefaultModule()`
  limitation is inert for this library.
- I extracted all 50 `public type|const|enum|class|annotation` declarations from the bala's nine
  `.bal` files and intersected them with the 150 `typeDefs` names plus the client name in
  `new`: `MISSING from render: 0 []`.
- There are no module-level `public function`, `public service` or `public listener` declarations in
  the bala (`grep` returned nothing), so there is no functional API outside the client class.
- The render's 151 names exceed the 50 public declarations because enum members (e.g.
  `SignatureVersion1`, `TOPIC`, `EN_US`) and module constants are emitted as individual entries.

## 7. Compiler plugin

**None exists.** The upstream `v4.0.1` tree has no `compiler-plugin`, `*-compiler-plugin` or
`CompilerPlugin.toml` (`find` returned nothing), and the bala contains only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/` directory.
Nothing plugin-derived is therefore expected in, or missing from, the render.

## 8. Other considerations

- **Version is stable and non-deprecated.** `4.0.1`, `distribution = "2201.12.0"`,
  `graalvmCompatible = true`, `template = false`.
- **Size.** +8 lines (+0.65%). The 6 recovered error types cost 12 lines; the mangled-return and
  phantom-parameter fixes are net-neutral in line count. Token impact is negligible; the
  correctness gain is not.
- **Upstream doc typo** "Reperesents the generic error type" (`error.bal:17`) is faithfully carried
  into `new`. That is correct behaviour for a render — the typo is the library's, not the pipeline's.
- **Highest-value fix for an LLM consumer** is the stream returns: `returns Error?>` on 7 of the 43
  methods is unparseable and would have led a model to invent a return type for every list/pagination
  operation in the connector.
- **Highest-remaining risk** is §5.2 (`targetType = "PHONE_NUMBER"` instead of `TOPIC`), which is a
  plausible-looking but wrong default that a model would copy verbatim. It predates spec v2.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 1237 / 1245 |
| 2 | `grep -c '^// Unknown type:'` both | old 6, new 0 |
| 3 | `grep -n '^// Unknown type:' old` | lines 337,339,341,343,345,347 → Error, GenerateRequestFailed, OperationError, ResponseHandleFailedError, CalculateSignatureFailedError, InternalError |
| 4 | `grep -n '^// --- ' ` both | old: README 7/133, Types 135, Client 1034 · new: 7/133, 135, 1041 |
| 5 | `diff -u old new` (full) | 10 hunks, all enumerated in §2; no other change |
| 6 | `diff <(sed -n '7,133p' old) <(sed -n '7,133p' new)` | empty → README identical |
| 7 | `diff` of sorted `^type <name>` lists | new adds 6, removes 0 |
| 8 | `diff` of sorted client method-name lists | empty (43 = 43) |
| 9 | Python compare of JSON top-level keys | same 8 keys; typeDefs 150/150, clients 1/1, functions 0/0, services 0/0, annotations 0/0 |
| 10 | Python: typeDefs name lists equal? | `True`, 150 entries, same order |
| 11 | Python: typeDefs differing entries | 10 — Error, GenerateRequestFailed, OperationError, ResponseHandleFailedError, CalculateSignatureFailedError, InternalError, Message, MessageAttributeValue, PublishBatchRequestEntry, ConnectionConfig |
| 12 | Python: client function differing entries | 8 — listTopics, listSubscriptions, listPlatformApplications, listEndpoints, listSMSSandboxPhoneNumbers, listOriginationNumbers, listPhoneNumbersOptedOut, tagResource |
| 13 | Python: client object keys | old `[name,description,functions]`; new adds `annotations` |
| 14 | Python: `close` JSON both sides | byte-identical, `"type": "Normal Function"` → render difference is renderer-side |
| 15 | Python: `tagResource` JSON | old has 3 params incl. `{"name":"Additional Values","type":"string"}`; new has 2 |
| 16 | `grep -c 'Additional Values'` both | old 1, new 0 |
| 17 | `grep -c 'returns Error?>' old` / `grep -c 'returns stream<' new` | 7 / 7 |
| 18 | `grep -cE 'org/mod:x.y.z:' ` both | old 4 (lines 821, 827, 838, 991), new 0 |
| 19 | `grep -c 'Special Agent Note'` both | 17 / 17 |
| 20 | `grep -cE '^const '` / `'^enum '` both | 100/100 and 16/16 |
| 21 | `git ls-remote --tags …module-ballerinax-aws.sns` | `v4.0.1` → `3e53fe94cc9d6ffaac7b18ca2bc984ceae7902fa` |
| 22 | `git clone --depth 1 --branch v4.0.1` | succeeded |
| 23 | `diff -q` bala vs upstream, all 9 `.bal` files | SAME × 9 |
| 24 | `grep -n 'function close' client.bal` | `979: public isolated function close() returns Error?` — not remote |
| 25 | `grep -n 'function tagResource' client.bal` | `759: … tagResource(string topicArn, *Tags tags) returns Error?` |
| 26 | `grep -n '@display' bala/*.bal` | client.bal:30, types.bal:570 — exactly 2 |
| 27 | `cat error.bal` | 6 `distinct` types, hierarchy rooted at `Error distinct error` |
| 28 | `sed -n '181,186p' client.bal` | `TargetType targetType = TOPIC` (render says `"PHONE_NUMBER"`) |
| 29 | `grep -A8 'enum TargetType' types.bal` | `{TOPIC, ARN, PHONE_NUMBER}` at types.bal:90–94 |
| 30 | `sed -n '633,636p' client.bal` | `LanguageCode? languageCode = EN_US` (render says `()`), enum at types.bal:153 |
| 31 | 43 rendered signatures vs 43 `client.bal` declarations | all names/arities/returns match except §5.2–5.5 |
| 32 | `grep -hoE '^public (type\|const\|enum\|class\|annotation)' bala/*.bal` | 50 public symbols |
| 33 | Python set-difference public-symbols − render-names | `MISSING from render: 0 []` |
| 34 | `grep -E '^public (function\|service\|listener)' bala/*.bal` | no matches |
| 35 | `ls bala/…/modules/` and `package.json` `export` | single module `aws.sns` → no submodule gap |
| 36 | `find src -iname '*compiler*plugin*' -o -iname 'CompilerPlugin.toml'` | no matches |
| 37 | `ls bala/…/4.0.1/any` | bala.json, dependency-graph.json, docs, modules, package.json — no compiler-plugin |
| 38 | `cat bala/…/package.json` | version 4.0.1, ballerina_version 2201.12.0, graalvmCompatible true |
| 39 | `grep -oE '\b(aws\|auth\|sns):[A-Za-z]+' new` | `aws:` 3 distinct, `auth:` 6 distinct, `sns:MessageAttributeValue` 1 (rest of `sns:` hits are inside README code blocks) |
| 40 | `grep -n '^type Tags' new` | line 980 — `Tags` is defined in the render, so `tagResource`'s parameter type resolves |

## 10. Caveats and unverified items

- I did not re-run the two-stage pipeline. The audit compares the delivered `old`/`new` JSON and
  `.bal.txt` artifacts against the bala and upstream source; it does not independently reproduce
  them. Attribution of a difference to "extractor" vs. "renderer" is inferred from whether the JSON
  differs (e.g. `close` — JSON identical → renderer; error `baseType` — JSON differs → extractor).
- Ballerina Central metadata was not re-queried over the network; module list, version and keywords
  were taken from the bala's `package.json` and `bala.json`, which are authoritative for what the
  extractor consumed.
- `old`'s phantom `Additional Values` parameter — I confirmed it is absent from the library source,
  but I did not trace which extractor code path fabricated it (the `*Tags` included-record parameter
  at `client.bal:759` is the obvious trigger, since it is the module's only such parameter; that
  causal link is inferred, not proven).
- The claim that all 43 rendered signatures match was established by comparing rendered signature
  text against `grep`-extracted declaration headers; declarations wrapped across multiple source
  lines (`createTopic`, `setTopicAttributes`, `publish`, `publishBatch`, `subscribe`,
  `confirmSubscription`, `createPlatformApplication`, `setSubscriptionAttributes`,
  `getPlatformApplicationAttributes`, `setPlatformApplicationAttributes`, `createEndpoint`,
  `listEndpoints`, `setEndpointAttributes`, `createSMSSandboxPhoneNumber`,
  `listSMSSandboxPhoneNumbers`, `addPermission`) were checked by reading the continuation lines for
  the four cases discussed in §3 and §5; the remaining wrapped declarations were matched on name,
  first-line parameters and return type only.

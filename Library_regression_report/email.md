# ballerina/email 2.14.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/email` |
| Pinned version | `2.14.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-email |
| Tag reviewed | `v2.14.0` (exact match; commit `edc48b12`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/email/2.14.0/java21` |
| Old render | `718` lines (22,953 bytes) |
| New render | `811` lines (25,547 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old`. The complete set of lines present in `old` but absent from `new`
is 8 unique lines: the 3 `// Unknown type:` placeholders and 5 lines carrying version-qualified type
references. Nothing else was removed, reworded, or truncated — every other byte of the 718-line `old`
render survives verbatim in `new`.

`new` adds real definitions for the three types `old` degraded (`Error`, `ImapListener`,
`PopListener`), bringing 17 new declarations (3 top-level + 14 listener methods) and closing the
render's only default-module coverage gap: `new` now covers **21/21** public top-level symbols
exported by the `email` module, versus **18/21** in `old`.

Both renders share several pre-existing fidelity problems (flattened `*IncludedRecord` params
producing non-compiling signatures, `mime:mime:` doubled prefix, 14 dropped record-field defaults,
closed records rendered open). These are identical on both sides and are therefore not regressions.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 718 | 811 |
| Bytes | 22,953 | 25,547 |
| `// Unknown type:` placeholders | 3 | 0 |
| Version-qualified type refs (`ballerina/email:2.14.0:`) | 6 occurrences on 5 lines | 0 |
| `// --- <section> ---` markers | 4 (README, END README, Types, Client) | 4 (identical) |
| Top-level declarations | 26 | 29 |
| Class/client methods (indented `function`) | 11 | 25 |
| `typeDefs` in JSON | 24 | 24 |
| `clients` in JSON | 3 | 3 |
| `functions` / `services` / `annotations` in JSON | 0 / 0 / 0 | 0 / 0 / 0 |

### Declarations added (17)

Top-level (3), all previously `// Unknown type:` stubs:

| Kind | Name | new render line |
|---|---|---|
| type | `Error` (`type Error error;`) | 576 |
| class | `ImapListener` | 659 |
| class | `PopListener` | 707 |

Methods (14) — 7 on each listener class, none of which existed in `old`:

`init`, `'start`, `attach`, `detach`, `immediateStop`, `gracefulStop`, `register`
(× `ImapListener`, × `PopListener`).

### Declarations removed (0)

`diff <(sort old) <(sort new) | grep '^<'` yields exactly 8 unique lines, none of which is a
declaration that disappears — 3 are `// Unknown type:` comments and 5 are the qualified-ref variants
of lines that still exist in `new` in unqualified form.

### Declarations modified (5 lines, 6 ref occurrences)

| Location | old | new |
|---|---|---|
| `SecureSocket.protocol` | `record {\|ballerina/email:2.14.0:Protocol name; ...\|}` | `record {\|Protocol name; ...\|}` |
| `OAuth2GrantConfig` | `ballerina/email:2.14.0:OAuth2ClientCredentialsGrantConfig\|ballerina/email:2.14.0:OAuth2PasswordGrantConfig` | `OAuth2ClientCredentialsGrantConfig\|OAuth2PasswordGrantConfig` |
| `ImapClient.init` return | `returns ballerina/email:2.14.0:Error?` | `returns Error?` |
| `PopClient.init` return | `returns ballerina/email:2.14.0:Error?` | `returns Error?` |
| `SmtpClient.init` return | `returns ballerina/email:2.14.0:Error?` | `returns Error?` |

All five are unambiguous improvements: the module-qualified form is not valid Ballerina and would
mislead a consumer into writing `ballerina/email:2.14.0:Error` in code.

### README section

Byte-identical. `diff <(sed -n '7,428p' old) <(sed -n '7,428p' new)` → empty. JSON `readme` fields
compare equal in Python.

### JSON-level cause of the change

Both JSONs carry the same 24 `typeDefs` with the same names. The difference is the `type` tag:

- `old` JSON: `ImapListener` / `PopListener` have keys `["name","description","functions"]` — **no
  `type` field at all**, so `renderTypeDef` fell through to `// Unknown type:`.
- `new` JSON: both are tagged `"type": "Class"`.
- `Error` is tagged `"type": "Error"` on both sides; `new` additionally carries `"baseType": "error"`.
  `old`'s renderer had no `Error` case, `new`'s does.

So the fix spans both stages (Java extractor tags + TS renderer cases), not the renderer alone.

## 3. Correctness against library source

Verified against the bala module sources (authoritative) and cross-checked against the `v2.14.0`
clone; the two agree for every item below.

| new render | source | match |
|---|---|---|
| `class ImapListener { ... }` with 7 methods | `modules/email/imap_listener_endpoint.bal:21` `public class ImapListener` | yes — class exists and is public |
| `function init(ImapListenerConfiguration listenerConfig) returns Error?` | `imap_listener_endpoint.bal:31` `public isolated function init(ImapListenerConfiguration listenerConfig) returns Error?` | yes |
| `function 'start() returns error?` | `imap_listener_endpoint.bal:50` | yes |
| `function attach(Service s, string[]\|string\|() name = ()) returns error?` | `imap_listener_endpoint.bal:62` `attach(Service s, string[]\|string? name = ())` | yes (`string?` ≡ `string\|()`) |
| `function detach(Service s) returns error?` | `imap_listener_endpoint.bal:76` | yes |
| `function immediateStop() returns error?` | `imap_listener_endpoint.bal:86` | yes |
| `function gracefulStop() returns error?` | `imap_listener_endpoint.bal:96` | yes |
| `function register(Service emailService, string\|() name) returns ()` | `imap_listener_endpoint.bal:124` `public isolated function register(Service emailService, string? name)` | signature matches; source declares no return type, render writes `returns ()` (equivalent) |
| `class PopListener { ... }` with the same 7 methods | `pop_listener_endpoint.bal:22` `public class PopListener` | yes |
| `type Error error;` | `email_errors.bal:18` `public type Error distinct error;` | **partial** — `distinct` dropped (see §5.1) |
| Non-public listener members `internalStart`, `stop`, `poll`, `close`, and the private `Job` class | `imap_listener_endpoint.bal:100,105,113,134,140` | correctly **excluded** from the render |
| `ImapClient.init` / `PopClient.init` / `SmtpClient.init` returning `Error?` | `imap_client_endpoint.bal:29`, `pop_client_endpoint.bal:29`, `smtp_client_endpoint.bal:34` | return type correct; parameter list is a flattened `*Config` (see §5.4, shared with `old`) |
| `SmtpClient.sendMessage(Message email) returns Error\|()` | `smtp_client_endpoint.bal:70` `remote isolated function sendMessage(Message email) returns Error?` | yes |
| `SmtpClient.send(...)` | `smtp_client_endpoint.bal:90` `remote isolated function send(string\|string[] to, string subject, string 'from, string body, *Options options) returns Error?` | first four params correct; `*Options` flattened (shared with `old`) |
| `class Service {}` | `commons.bal:129` `public type Service distinct service object {};` | source object body is genuinely empty; render is faithful modulo `distinct`/`service object` → `class` |

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

1. Full sorted-line set difference `diff <(sort old) <(sort new)` — the `<` side is exactly 8 lines,
   enumerated in §2, none of which is content loss.
2. Top-level declaration sets extracted with
   `grep -nE '^(public )?(isolated )?(remote |client )?(function|type|class|enum|const|annotation|listener|service|public)'`
   and diffed: 26 → 29, **0 removed**, 3 added.
3. Indented method sets extracted with `grep -nE '^ +(remote |resource )?(isolated )?function '` and
   diffed: 11 → 25, **0 removed**, 14 added (3 previously-qualified `init` lines are present in `new`
   in unqualified form, so they are modifications not removals).
4. README block (lines 7–428) diffed — identical; JSON `readme` field compared equal.
5. Section markers compared — same 4 markers, same order.
6. Every record body compared implicitly via (1): since only 8 lines differ, no record lost a field,
   a doc comment, an optional marker, or a type.
7. JSON `typeDefs` name set compared — identical (24 = 24), and `clients`/`functions`/`services`/
   `annotations` counts identical.
8. Doc-comment lines: `new` gains only doc lines attached to the newly emitted declarations; no doc
   comment present in `old` is absent from `new`.

## 5. Issues in `new` (independent of `old`)

Items 5.1–5.3 are newly *visible* in `new` because `old` printed nothing at all for these symbols.
They are inaccuracies in `new`, but not regressions — `old` conveyed strictly less.

**5.1 `distinct` dropped from `Error`.** Source `email_errors.bal:18` is
`public type Error distinct error;`. `new` line 576 renders `type Error error;`. The JSON carries
`"baseType": "error"` with no distinctness flag, so this is lost at extraction. Consequence: a
consumer may believe any `error` is assignable to `email:Error`. Low impact for prompt use, but it is
a semantic inaccuracy. (The same loss affects `Service`: source is `distinct service object`,
rendered `class Service {}` — that one is shared with `old`.)

**5.2 Listener class documentation is the constructor's doc, not the class's.** `new` lines 657–659
and 705–707 render the class-level doc as
`# Gets invoked during the \`email:ImapListener\` initialization.` The actual class doc in the source
is `# Represents a service listener that monitors the email server location.`
(`imap_listener_endpoint.bal:20`, `pop_listener_endpoint.bal:21`). The wrong string is already in the
`old` JSON's `description` field for these typeDefs, so the extractor bug predates spec v2 — it just
became visible now. Impact: the one-line summary an LLM sees for the listeners is misleading.

**5.3 Listeners are rendered as `class`, not as listener objects, with bodyless methods.**
`class ImapListener { function init(...) returns Error?; ... }` is not valid Ballerina — a `class`
requires method bodies. This is the same stub-declaration convention the render already uses for
`client class ImapClient` etc. in `old`, so the style is consistent; it is only a concern if the
render is expected to be compilable. Additionally the listeners' methods are shown without the
`public isolated` qualifiers they carry in source.

**5.4 Shared with `old` — flattened included-record parameters produce non-compiling signatures.**
Source `imap_client_endpoint.bal:29` is
`public isolated function init(string host, string username, string password, *ImapConfiguration clientConfig)`.
Both renders expand `*ImapConfiguration` into `int port = 993, Security security = SSL, SecureSocket secureSocket = {cert: ""}`
**and then also append the required parameter `ImapConfiguration clientConfig`** — a required
parameter after defaulted ones, which Ballerina rejects, and a duplicate representation of the same
data. Identical in `old` and `new` (the only textual difference on these lines is the return type).
Same pattern on `PopClient.init`, `SmtpClient.init`, and `SmtpClient.send` (`*Options options`).

**5.5 Shared with `old` — `mime:mime:Entity` doubled module prefix.** 3 occurrences in each render
(`old` lines 471, 503, 717; same lines in `new`). Not valid Ballerina.

**5.6 Shared with `old` — bogus default `attachments = new ()`.** In `SmtpClient.send`, `attachments`
is rendered with default `new ()` for a union type `mime:Entity|Attachment|...[]`. The source
`Options.attachments` field is optional with no default.

**5.7 Shared with `old` — 14 record-field defaults dropped.** Every defaulted field in the six
config records is rendered as an optional field with no default:

| Record | dropped defaults |
|---|---|
| `ImapConfiguration` | `port = 993`, `security = SSL` |
| `PopConfiguration` | `port = 995`, `security = SSL` |
| `SmtpConfiguration` | `port = 465`, `security = SSL` |
| `ImapListenerConfiguration` | `pollingInterval = 30`, `port = 993`, `security = SSL` |
| `PopListenerConfiguration` | `pollingInterval = 30`, `port = 995`, `security = SSL` |
| `SecureSocket` | `versions = []`, `verifyHostName = true` |

Verified: 14 defaults exist in the bala sources; `grep -E '^ +[A-Za-z].*= '` over the Types section of
`new` (lines 430–752) returns only the two `attach(... name = ())` parameter defaults — zero field
defaults. Identical in `old`. `verifyHostName = true` is the security-relevant one (see §7).

**5.8 Shared with `old` — closed records rendered as open.** All six config records plus `Message`,
`Attachment`, `Options` are `record {| ... |}` in source; all 11 `type X record {` declarations in
both renders use the open form. Only the inline `protocol` record retains `{| |}`.

## 6. Coverage gaps vs. the library

**`new`: 0 gaps.** All 21 public top-level declarations exported by the default `email` module are
present. Source list (`grep -hE '^public ' modules/email/*.bal | sort -u`):

`ImapListener`, `PopListener`, `DEFAULT_FOLDER`, `Protocol`, `Security`, `ImapClient`, `PopClient`,
`SmtpClient`, `Attachment`, `Error`, `ImapConfiguration`, `ImapListenerConfiguration`, `Message`,
`OAuth2ClientCredentialsGrantConfig`, `OAuth2GrantConfig`, `OAuth2PasswordGrantConfig`, `Options`,
`PopConfiguration`, `PopListenerConfiguration`, `SecureSocket`, `Service`, `SmtpConfiguration`
— 21 unique names (the enums `Protocol` and `Security` additionally contribute the 6 constants
`SSL`, `TLS`, `START_TLS_AUTO`, `START_TLS_ALWAYS`, `START_TLS_NEVER`, all rendered on both sides).

**`old`: 3 gaps** — `Error`, `ImapListener`, `PopListener` (present as `// Unknown type:` stubs with
no members; an LLM reading `old` had no way to construct or use either listener).

**Submodules:** none. `bala/.../java21/modules/` contains only `email`, and `package.json` declares
`"export": ["email"]`. Central metadata lists a single module. So there is no submodule-only API and
no shared submodule gap for this library.

**Semantic gap on both sides:** `class Service {}` is empty. That is faithful to the source
(`commons.bal:129–130` — `public type Service distinct service object {};` with an empty body), but
it means neither render states the `onMessage`/`onError` contract at the type level. See §7.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `plugin_id: email-compiler-plugin`,
`plugin_class: io.ballerina.stdlib.email.compiler.EmailCompilerPlugin`, backed by
`email-compiler-plugin-2.14.0.jar`. Upstream sources at `v2.14.0`:

- **`EmailServiceValidator`** — enforces the `email:Service` contract that the empty `service object`
  cannot express. Diagnostics `EMAIL_101`–`EMAIL_107`: service **must** contain an `onMessage`
  function; `onMessage`/`onError` must carry the `remote` keyword and must not be `resource`;
  `onMessage` expects an `email:Message` parameter and `onError` an `email:Error`; return type must be
  a subtype of `error?`; any other function on the service is rejected
  (`FUNCTION_0_NOT_ACCEPTED_BY_THE_SERVICE`). Method names come from
  `native/.../EmailConstants.java:98-99` (`ON_MESSAGE = "onMessage"`, `ON_ERROR = "onError"`).
- **`EmailCodeAnalyzer`**, **`EmailScanCodeAnalyzer`**, **`EmailSmtpClientAnalyzer`** + `RuleFactory`
  / `RuleImpl` — static code analysis. `rules.json` defines exactly one rule:
  `{"id":1,"kind":"VULNERABILITY","description":"Avoid unverified server hostnames during SSL/TLS connections"}`,
  which inspects `secureSocket.verifyHostName` on `SmtpClient`/`PopClient`/`ImapClient`.

**What the plugin implies that is absent from the render:**

1. The `onMessage` / `onError` remote-method contract does not appear in either render's `Service`
   declaration. Mitigated for prompt purposes: the README block (both renders, lines 219–231)
   contains a working `service` sample declaring
   `remote function onMessage(email:Message emailMessage)` and
   `remote function onError(email:Error emailError)`. So the information reaches the model via prose,
   not via the type. Equal on both sides.
2. The `verifyHostName` security rule is undercut by §5.7: `SecureSocket.verifyHostName` renders as
   `boolean verifyHostName?;` with the source default `= true` dropped, on both sides. A model
   generating code has no signal that the safe value is the default. Equal on both sides.

No compiler-plugin-generated types, annotations, or code actions are missing from `new` relative to
`old`.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerina/email/2.14.0`: `deprecated: null`,
  `deprecateMessage: ""`, `visibility: public`, `pullCount: 3008`, `ballerinaVersion: 2201.12.0`.
  Stable 2.x version — no pre-1.0 instability concern.
- **Size / token cost.** +93 lines (+12.9%), +2,594 bytes (+11.3%). Roughly 650 additional tokens for
  two fully documented listener classes and a real `Error` definition — a good ratio.
- **Doc quality.** Method-level doc comments (summary + `ballerina` code fence) survive intact for the
  new listener methods. Parameter-level docs (`+ s - Type descriptor of the service`) are present in
  the JSON but dropped by the renderer for all methods on both sides; record-field docs *are*
  rendered. Consistent with `old`.
- **Published package compiles.** No evidence to the contrary; the bala is a normal `java21` platform
  bala with `dependency-graph.json` and a resolved `javax.mail-1.6.2` / `greenmail-1.6.15` platform
  dependency set.
- **Bala vs. GitHub.** No disagreement found for any symbol checked — `modules/email/*.bal` in the
  bala matches `ballerina/*.bal` at tag `v2.14.0` for all declarations reviewed.

## 9. Evidence log

| # | Command / file:line | Result |
|---|---|---|
| 1 | `wc -l old/ballerina_email.bal.txt new/ballerina_email.bal.txt` | 718 / 811 |
| 2 | `wc -c` on both | 22,953 / 25,547 |
| 3 | `git ls-remote --tags .../module-ballerina-email \| grep v2.14.` | `refs/tags/v2.14.0` → `75b79d39`, peeled `edc48b12` |
| 4 | `git clone --depth 1 --branch v2.14.0 …` | success, into scratch `work/email/src` |
| 5 | `ls bala/.../java21/modules` | single dir `email` — no submodules |
| 6 | `ls bala/.../modules/email` | 8 `.bal` files: commons, email_errors, imap_client_endpoint, imap_listener_endpoint, init, pop_client_endpoint, pop_listener_endpoint, smtp_client_endpoint |
| 7 | `cat bala/.../package.json` | `"export": ["email"]`, `ballerina_version 2201.12.0`, platform `java21` |
| 8 | `grep -c '^// Unknown type:'` old / new | 3 / 0 |
| 9 | `grep -o 'ballerina/email:2\.14\.0:' old \| wc -l` | 6 occurrences (on 5 lines); new: 0 |
| 10 | `grep -n '^// --- ' old` | 7, 428, 430, 660 |
| 11 | `grep -n '^// --- ' new` | 7, 428, 430, 753 |
| 12 | top-level decl grep + `diff` | 26 → 29; added `class ImapListener`, `class PopListener`, `type Error error;`; modified `OAuth2GrantConfig`; **0 removed** |
| 13 | indented-method grep + `diff` | 11 → 25; 14 added; 3 `init` lines changed return type only; **0 removed** |
| 14 | `diff <(sort old) <(sort new) \| grep '^<' \| sort -u` | exactly 8 lines — 3 `// Unknown type:`, 5 version-qualified |
| 15 | `diff <(sed -n '7,428p' old) <(sed -n '7,428p' new)` | empty — README identical |
| 16 | Python: JSON top-level keys + list lengths | both sides: typeDefs 24, clients 3, functions 0, services 0, annotations 0 |
| 17 | Python: JSON typeDef name→type map, both sides | name sets equal; `ImapListener`/`PopListener` untyped in old (`['name','description','functions']`) vs `"Class"` in new |
| 18 | Python: `old['readme'] == new['readme']` | `True` |
| 19 | Python: dump of `Error` typeDef | old `{name, description, type:"Error"}`; new adds `baseType:"error"` — no `distinct` on either |
| 20 | `bala/.../email_errors.bal:18` | `public type Error distinct error;` |
| 21 | `bala/.../imap_listener_endpoint.bal:20-21` | `# Represents a service listener that monitors the email server location.` / `public class ImapListener {` |
| 22 | `bala/.../pop_listener_endpoint.bal:21-22` | same class doc, `public class PopListener {` |
| 23 | `bala/.../imap_listener_endpoint.bal:31,50,62,76,86,96,124` | 7 public methods — match render 1:1 |
| 24 | `bala/.../imap_listener_endpoint.bal:100,105,113,134,140` | non-public `internalStart`/`stop`/`poll`/`close` + private `Job` — correctly excluded |
| 25 | `grep -hE '^public ' bala/.../modules/email/*.bal \| sort -u` | 21 public top-level declarations (listed in §6) |
| 26 | `bala/.../imap_client_endpoint.bal:29-30` | `init(string host, string username, string password, *ImapConfiguration clientConfig) returns Error?` |
| 27 | `bala/.../smtp_client_endpoint.bal:70,90` | `sendMessage(Message email) returns Error?`; `send(string\|string[] to, string subject, string 'from, string body, *Options options) returns Error?` |
| 28 | `grep -c 'mime:mime:'` old / new | 3 / 3 (lines 471, 503, 717 both sides) |
| 29 | `bala/.../commons.bal:85-93` | `SecureSocket` closed record, `versions = []`, `verifyHostName = true` |
| 30 | `sed -n '/^type SecureSocket record/,/^};/p'` old vs new | identical apart from the qualified `Protocol` ref |
| 31 | `grep -c 'record {\|'` and `grep -c '^type .* record {$'` | old 1/11, new 1/11 — identical |
| 32 | Python regex over all `public type X record {\|…\|}` in bala | 14 field defaults across 6 records |
| 33 | `sed -n '430,752p' new \| grep -E '^ +[A-Za-z].*= '` | only the two `attach(… name = ())` lines — 0/14 field defaults rendered |
| 34 | `bala/.../commons.bal:129-130` | `public type Service distinct service object {};` — genuinely empty |
| 35 | `cat bala/.../compiler-plugin/compiler-plugin.json` | `email-compiler-plugin`, `EmailCompilerPlugin`, jar `email-compiler-plugin-2.14.0.jar` |
| 36 | `find src/compiler-plugin -name '*.java'` | `EmailCompilerPlugin`, `EmailCodeAnalyzer`, `EmailServiceValidator`, `EmailScanCodeAnalyzer`, `staticcodeanalyzer/{EmailRule,RuleFactory,RuleImpl,EmailSmtpClientAnalyzer}` |
| 37 | `EmailServiceValidator.java:70-90,155-229` | codes `EMAIL_101`–`EMAIL_107`; `onMessage` mandatory; remote-keyword and return-type checks |
| 38 | `native/.../EmailConstants.java:98-99,156-157` | `ON_MESSAGE`, `ON_ERROR`, `EMAIL_MESSAGE`, `ERROR` |
| 39 | `src/.../rules.json` | one rule: id 1, VULNERABILITY, "Avoid unverified server hostnames during SSL/TLS connections" |
| 40 | `grep -n 'onMessage\|onError' new` | lines 219–230 — inside README block, present on both sides |
| 41 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/email/2.14.0` | `deprecated: null`, `pullCount 3008`, single module `email`, `visibility public` |
| 42 | `grep -n 'verifyHostName' new` | line 251 (README sample) and line 522 (`boolean verifyHostName?;` — no default) |

## 10. Caveats and unverified items

1. **Compiler-plugin behaviour is read from source, not executed.** The `EMAIL_101`–`EMAIL_107`
   diagnostics and the `verifyHostName` vulnerability rule were established by reading
   `EmailServiceValidator.java`, `EmailRule.java`, and `rules.json` at tag `v2.14.0`. I did not compile
   a sample project to observe the diagnostics firing.
2. **The bala's compiler plugin is a jar** (`email-compiler-plugin-2.14.0.jar`); I did not decompile it
   to confirm it is byte-identical to the `v2.14.0` sources. `compiler-plugin.json` and the version in
   the jar filename are consistent with the tag, so I treated the clone as representative.
3. **`distinct` handling is asserted from the JSON, not from renderer source.** I confirmed `new`'s
   JSON emits `"baseType": "error"` with no distinctness marker and that the render prints
   `type Error error;`. I did not read `to-syntax-string.ts` to confirm the renderer *could not* have
   printed `distinct` had the JSON provided it — so the exact stage at which `distinct` is lost
   (extractor vs. renderer) is unverified; only the loss itself is verified.
4. **Method-level parameter docs.** I verified the JSON carries parameter `description` fields and
   that neither render prints them. I did not exhaustively enumerate how many parameter descriptions
   are dropped across all methods; the count is not reported anywhere above.
5. **Compilability of the renders was not machine-checked.** Claims that specific rendered lines are
   not valid Ballerina (`mime:mime:Entity`, required param after defaulted params, bodyless methods in
   a `class`) are from reading the language rules, not from running `bal build` on the render.
6. **No behavioural check of `register`'s `returns ()`.** The source declares no return type; I treat
   `returns ()` as equivalent, which is correct per the language spec but was not compiler-verified.

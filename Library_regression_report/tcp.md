# ballerina/tcp 1.13.8 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/tcp` |
| Pinned version | `1.13.8` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-tcp |
| Tag reviewed | `v1.13.8` (commit `64dcb6991fdd8e0504b7b1a896e244f2afeb211c`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/tcp/1.13.8/java21` |
| Old render | `251` lines |
| New render | `285` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present in `old` was dropped,
truncated or degraded. `new` adds the two public symbols `old` could not render at all
(`tcp:Error`, `tcp:Listener` — 8 declarations in total), removes all 3 version-qualified type
references (`ballerina/tcp:1.13.8:Protocol` / `:Error?`), stops inventing a `= 0` default for the
required `Listener` port in the service stanza, module-qualifies the service-stanza types
(`tcp:Caller`, `tcp:ConnectionService|tcp:Error?` — exactly matching the compiler plugin's own code
template), and emits the `onConnect` parameter doc. The README block is byte-identical on both
sides (one trailing blank line difference vs. the bala README).

All 12 public symbols exported by the single module `tcp` now appear in `new`; `old` covered 10.
The remaining inaccuracies (closed records rendered open, defaulted fields rendered optional,
`distinct` dropped, doc-continuation lines losing their `#`) are almost all shared with `old` and
are renderer-convention issues, not regressions.

## 2. Change inventory

Counts from `diff -u old/ballerina_tcp.bal.txt new/ballerina_tcp.bal.txt` (5 hunks, 41 added /
7 removed lines) and from `grep -nE '^(type |class |client class |enum |const |service |// Unknown type)'`.

| kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 | −2 |
| Version-qualified type refs (`ballerina/tcp:1.13.8:…`) | 3 | 0 | −3 |
| Section markers `// --- ` | 5 | 5 | 0 |
| Top-level decls (const/type/enum/class/client class/service) | 16 | 18 | +2 |
| Class/client-class member functions | 12 | 18 | +6 |

**Added in `new` (8 declarations, 0 removed):**

| symbol | kind | render line (new) |
|---|---|---|
| `Error` | `type Error error;` | 201 |
| `Listener` | `class Listener { … }` | 207 |
| `Listener.init` | constructor | 208 |
| `Listener.attach` | function | 215 |
| `Listener.'start` | function | 219 |
| `Listener.gracefulStop` | function | 223 |
| `Listener.immediateStop` | function | 227 |
| `Listener.detach` | function | 234 |

**Modified (5 sites, all in `new`'s favour):**

1. `ClientSecureSocket.protocol` — `record {|ballerina/tcp:1.13.8:Protocol name; …|}` → `record {|Protocol name; …|}` (old:137 / new:137).
2. `ListenerSecureSocket.protocol` — same change (old:170 / new:170).
3. `Client.init` return — `ballerina/tcp:1.13.8:Error?` → `Error?` (old:222 / new:255).
4. Service stanza listener args — `new tcp:Listener(int localPort = 0, ListenerConfiguration config = {})` → `new tcp:Listener(int localPort, tcp:ListenerConfiguration config = {})` (old:248 / new:281).
5. `onConnect` — `remote function onConnect(Caller caller) returns ConnectionService|Error?;` →
   `# + caller - The new client connection` + `remote function onConnect(tcp:Caller caller) returns tcp:ConnectionService|tcp:Error?;` (old:250 / new:283-284).

**JSON side** (`old/ballerina_tcp.json` vs `new/ballerina_tcp.json`): both have the same 12
`typeDefs`, 2 `clients`, 0 `functions`, 1 `services`, 0 `annotations`. The only JSON deltas are the
2 de-qualified `protocol` record strings, 2 de-qualified `Error?` return names, `"baseType":"error"`
added to `Error`, `"type":"Class"` added to `Listener`, and one stray `"optional": false` dropped
from the `onConnect` return object. Critically, **`old`'s JSON already carried the full `Listener`
function list** — `old`'s renderer simply had no branch for it, so it degraded to
`// Unknown type: Listener`. The gain is entirely renderer-side.

## 3. Correctness against library source

Repo `ballerina/*.bal` at tag `v1.13.8` is byte-identical to the bala's `modules/tcp/*.bal`
(verified with `diff -q` over all 7 files, no output). Checks against
`.../bala/ballerina/tcp/1.13.8/java21/modules/tcp/`:

| render (new) | source | verdict |
|---|---|---|
| `type Error error;` (201) | `socket_error.bal:18` `public type Error distinct error;` | correct except `distinct` dropped |
| `class Listener` (207) | `listener.bal:22` `public isolated class Listener` | correct (visibility/`isolated` are not rendered for any class) |
| `init(int localPort, …) returns Error?` (208) | `listener.bal:30` `init(int localPort, *ListenerConfiguration config) returns Error?` | `localPort` required + `Error?` return correct; see §5 N2/N3 for the expanded params |
| `attach(Service tcpService, string[]\|string\|() name = ()) returns error?` (215) | `listener.bal:42` `attach(Service tcpService, string[]\|string? name = ())` | correct (`string?` ≡ `string\|()`) |
| `'start() returns error?` (219) | `listener.bal:50` | correct |
| `gracefulStop() returns error?` (223) | `listener.bal:58` | correct |
| `immediateStop() returns error?` (227) | `listener.bal:66` | correct, incl. the "not implemented yet" doc |
| `detach(Service tcpService) returns error?` (234) | `listener.bal:77` | correct |
| `record {\|Protocol name; string[] versions;\|}` (137,170) | `secure_socket.bal:31-34, 51-54` | correct type name; `versions = []` default not shown |
| service stanza `new tcp:Listener(int localPort, …)` (281) | `listener.bal:30` — `localPort` has **no** default | `new` correct, `old`'s `= 0` was fabricated |
| `onConnect(tcp:Caller caller) returns tcp:ConnectionService\|tcp:Error?` (284) | `service.bal:20` comment `remote function onConnect(Caller caller) returns ConnectionService\|Error?;` and `AddTcpCodeTemplate.java:52-54` `remote function onConnect(tcp:Caller caller) returns tcp:ConnectionService` | correct, and the `tcp:` prefixing matches the plugin's own generated template |
| `Client.init(... ) returns Error?` (255) | `client.bal:30` | return correct |
| README (8-103) | `docs/README.md` (95 lines) | identical apart from one trailing blank line |

Also verified unchanged/correct on both sides: `Caller` (`caller.bal:26,35,47,56`), `Client`
remote methods (`client.bal:41,55,69`), `ClientConfiguration` (`client.bal:87`), `CertKey`
(`secure_socket.bal:64`), `Protocol` (`secure_socket.bal:71`), `ListenerConfiguration`
(`listener.bal:92`), `Service`/`ConnectionService` (`service.bal:18,24`).

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full `diff -u` of the two renders — 0 declarations removed, 0 doc lines removed, 0 parameters
  removed, 0 return types weakened. All 5 modified sites move *toward* the source (§2, §3).
- README block compared separately (`diff` of lines 1-104): identical.
- Declaration sets extracted with `grep -nE '^(type |class |client class |enum |const |service )'`
  and compared: `new` is a strict superset of `old` (adds `type Error`, `class Listener`).
- Member-function sets: `old` 12, `new` 18; the 12 in `old` are all present verbatim in `new`.
- The one delta that *looks* like a loss — `int localPort = 0` becoming `int localPort` — was
  verified against `listener.bal:30`: the parameter is required with no default, so the old
  default was invented. The JSON still carries `"default": "0"` for it on **both** sides; `new`'s
  renderer correctly suppresses a default on a non-optional parameter.
- The other apparent loss — `ballerina/tcp:1.13.8:` prefixes disappearing — is removal of
  non-compiling syntax, not information: the resulting `Protocol` / `Error?` names resolve
  in-module.

## 5. Issues in `new` (independent of `old`)

New-only (i.e. newly visible because `new` renders `Error`/`Listener` at all):

- **N1. `distinct` dropped from `Error`.** `new:201` `type Error error;` vs
  `socket_error.bal:18` `public type Error distinct error;`. An LLM told to define a matching
  distinct error subtype would get the relationship subtly wrong.
- **N2. `Listener.init` renders an un-compilable parameter list.** `new:208`:
  `function init(int localPort, string localHost = "", ListenerSecureSocket secureSocket = {...}, ListenerConfiguration config)`.
  The included-record parameter `*ListenerConfiguration config` (`listener.bal:30`) is expanded
  into its fields **and** re-emitted as a trailing required `config` parameter after defaulted
  ones. This is the same renderer convention already visible in `Client.init` on both sides
  (`old:222` / `new:255`), so it is shared behaviour, not new logic — but for `Listener` it is
  newly exposed.
- **N3. Fabricated default for `secureSocket`.** `new:208` shows
  `ListenerSecureSocket secureSocket = {'key: {path: "", password: ""}}`. In
  `listener.bal:94` the field is `ListenerSecureSocket secureSocket?;` — optional, **no default**.
  The value comes from the extractor (`new/ballerina_tcp.json` → `typeDefs[Listener].functions[init]
  .parameters[secureSocket].default`), and the identical string is in `old/ballerina_tcp.json`, so
  the fabrication is extractor-side and unchanged; only its visibility is new. It is misleading:
  an empty keystore path/password is not a usable default.

Shared with `old` (present in both renders, verified against source):

- **N4. Closed records rendered as open.** All six record types are `record {| … |}` in
  `secure_socket.bal:28,48,64`, `client.bal:87`, `listener.bal:92`; both renders emit
  `type X record { … };`.
- **N5. Fields that have defaults are rendered as optional (`?`).** `ClientConfiguration.timeout`
  and `.writeTimeout` are `decimal timeout = 300;` (`client.bal:89-90`) but render as
  `decimal timeout?;` (line 120/123). Same for `ClientSecureSocket.enable = true`
  (`secure_socket.bal:29` → line 133) and `ListenerSecureSocket.ciphers = []`
  (`secure_socket.bal:55` → line 173). The concrete `300` / `true` / `[]` values are lost.
- **N6. `Service` and `ConnectionService` render as empty `class` bodies** (lines 193, 197) though
  they are `distinct service object` types (`service.bal:18,24`).
- **N7. `SSL` / `TLS` emitted as module constants** (lines 108, 110) *in addition to*
  `enum Protocol { TLS, SSL }` (line 148). They are enum members, not module-level consts; taken
  literally the render redeclares them. Enum member order is also reversed vs
  `secure_socket.bal:71-74` (source `SSL, TLS`).
- **N8. Doc-comment continuation lines lose the leading `#`.** e.g. new:119 `of 300 seconds(5
  minutes) will be used`, new:139/172 `E.g., \`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\`, …`. These
  lines escape the comment and would not compile if the render were pasted verbatim.

## 6. Coverage gaps vs. the library

The bala exports exactly one module (`ls .../modules` → `tcp`; Central `modules` array has one
entry), so there is **no submodule gap** for this library.

All 12 public symbols of the default module (`grep -nE '^public ' modules/tcp/*.bal`) are present
in `new`: `Client`, `ClientConfiguration`, `Caller`, `Service`, `ConnectionService`, `Listener`,
`ListenerConfiguration`, `ClientSecureSocket`, `ListenerSecureSocket`, `CertKey`, `Protocol`,
`Error`. `old` was missing 2 of them (`Listener`, `Error` — name-only placeholders). There are no
public module-level functions and no annotations in the package.

Remaining gaps, both **shared** (missing from `old` and `new` alike):

- **G1. `Caller`'s 5 public final fields** — `remoteHost`, `remotePort`, `localHost`, `localPort`,
  `id` (`caller.bal:28-32`) — are absent from the rendered `client class Caller` (new:241-251).
  User code reading `caller.remoteHost` is not discoverable from either render.
- **G2. The `ConnectionService` remote-method contract is not rendered.** `service.bal:26-28`
  documents `onError(readonly & Error err)`, `onBytes(readonly & byte[] data)`, `onClose()` only as
  comments, so the extractor never sees them; both renders show `class ConnectionService {}` with
  no members. This is the most consequential omission for code generation — see §7.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` registers `io.ballerina.stdlib.tcp.compiler.TcpCompilerPlugin`
(`compiler-plugin/libs/tcp-compiler-plugin-1.13.8.jar`). Source at the tag contains 11 classes.

- **Validations** (`CompilationErrors.java`, codes `TCP_101`–`TCP_110`): `remote` keyword required
  on service methods; **`TCP_102` "Service does not contain \`onBytes\` function"**; parameter
  count/type checks for `onConnect`/`onBytes`/`onError`/`onClose`; return-type subtype checks;
  `TCP_107` rejects any function the service does not accept.
- **Code action** (`AddTcpCodeTemplate.java`, triggered by hint `TCP_106`): inserts
  `remote function onConnect(tcp:Caller caller) returns tcp:ConnectionService { return new TcpService(); }`
  plus `service class TcpService { *tcp:ConnectionService; remote function onBytes(tcp:Caller caller, readonly & byte[] data) returns tcp:Error? {} }`.

**Implication vs. the render:** `new`'s service stanza matches the plugin's `onConnect` template
exactly (including the `tcp:` prefixes — `old` did not). But neither render surfaces the
`ConnectionService` half of the template, even though the plugin makes `onBytes` effectively
mandatory (`TCP_102`). A model that follows either render literally would emit a service that fails
compilation. Unchanged between `old` and `new`, so not a regression — but the single biggest
remaining accuracy gap for this library.

## 8. Other considerations

- Stable 1.x, not deprecated (Central `deprecated: null`, `deprecateMessage: ""`), `pullCount` 172,
  built for `ballerinaVersion` 2201.12.0, `graalvmCompatible: true`.
- Size impact is negligible: +34 lines (+13.5%), and 2 of the 7 removed lines were pure noise
  (`// Unknown type:` placeholders). The 3 removed `ballerina/tcp:1.13.8:` prefixes shorten types.
- Doc quality of the underlying package is good; the render's remaining defects (N4–N8) originate
  in the renderer's formatting, not in the library's docs.
- Neither render is copy-paste compilable as-is (N7, N8, N2) — but that is equally true of `old`.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/… new/…` | 251 / 285 |
| 2 | `grep -c '^// Unknown type:'` old / new | 2 / 0 |
| 3 | `grep -n '^// --- '` old / new | 5 markers each, same names |
| 4 | `diff -u old new` | 5 hunks, +41 / −7 lines, 0 declarations removed |
| 5 | `diff <(sed -n '1,104p' old) <(sed -n '1,104p' new)` | no output — README block identical |
| 6 | `diff <(sed -n '8,103p' new) bala/docs/README.md` | only `96d95` (one trailing blank line) |
| 7 | `grep -nE '^(type \|class \|client class \|enum \|const \|service \|// Unknown type)'` both | old 16 top-level decls + 2 placeholders; new 18 |
| 8 | `grep -cE '^    (remote )?function '` both | old 12, new 18 |
| 9 | `python3 -m json.tool` + `diff -u` on the two JSONs | 6 deltas only (2× protocol type, 2× `Error?`, `baseType`, `type:"Class"`, 1 stray `optional:false`) |
| 10 | JSON `typeDefs`/`clients`/`services` name lists both sides | identical: 12 / 2 / 1; `functions` 0, `annotations` 0 |
| 11 | `new` JSON `typeDefs[Listener].functions[init]` dump | `secureSocket` `"default": "{'key: {path: \"\", password: \"\"}}"`; `localPort` no default, not optional |
| 12 | `new` JSON `services[0].listener.parameters` | `localPort` `"default": "0"` with no `optional` flag → suppressed by new renderer |
| 13 | `git ls-remote --tags …module-ballerina-tcp` | `v1.13.8` = `64dcb6991fdd8e0504b7b1a896e244f2afeb211c` |
| 14 | `git clone --depth 1 --branch v1.13.8` | success |
| 15 | `diff -q repo/ballerina/*.bal bala/modules/tcp/*.bal` (7 files) | no differences |
| 16 | `wc -l bala/modules/tcp/*.bal` | 393 lines total across 7 files |
| 17 | `grep -nE '^public ' bala/modules/tcp/*.bal` | 12 public symbols (listed in §6) |
| 18 | `grep -n 'annotation' bala/modules/tcp/*.bal` | none |
| 19 | `ls bala/.../modules` | `tcp` only — no submodules |
| 20 | `cat bala/compiler-plugin/compiler-plugin.json` | `tcp-plugin` / `TcpCompilerPlugin` |
| 21 | `grep -rhoE '"(TCP_[0-9]+)"' compiler-plugin/src` | TCP_101–TCP_110 |
| 22 | `sed -n '50,60p' AddTcpCodeTemplate.java` | template uses `tcp:Caller` / `tcp:ConnectionService`, plus `onBytes` in `TcpService` |
| 23 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/tcp/1.13.8` | not deprecated, 1 module, ballerinaVersion 2201.12.0, pullCount 172 |
| 24 | `cat bala/package.json` | version 1.13.8, export `["tcp"]`, graalvmCompatible |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific lines "would not compile" (N2, N7, N8) are from
  reading the syntax against the Ballerina grammar, not from running `bal build`.
- The origin of the fabricated `secureSocket` default (N3) was traced only as far as the extractor
  JSON — identical in both `old` and `new`, so it predates spec v2 — but the Java code that
  synthesises it was not read (the LS source tree was not part of this review's inputs).
- The `// Special Agent Note: TrustStore FROM ballerina/crypto package` annotations (lines 135, 168)
  are identical on both sides and were accepted as-is; the rule that generates them was not audited.
- Enum member ordering (`TLS, SSL` in the render vs `SSL, TLS` in `secure_socket.bal:72-73`) is
  identical on both sides; whether the extractor or the renderer reorders was not determined.

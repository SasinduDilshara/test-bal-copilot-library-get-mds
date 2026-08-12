# ballerina/udp 1.13.6 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/udp` |
| Pinned version | `1.13.6` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-udp |
| Tag reviewed | `v1.13.6` (exact match, commit `eb6cd4997760b39406e66553dae730a681392687`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/udp/1.13.6/java21` |
| Old render | `205` lines |
| New render | `239` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present in `old` was dropped,
truncated, or made less accurate. Three classes of improvement, all verified against the bala
source:

1. Both `// Unknown type:` placeholders (`Error`, `Listener`) are replaced by real definitions.
   `old` had 2 such lines, `new` has 0. `Listener` gains 6 real method signatures.
2. The bogus parameter `anydata Additional Values` — an un-parseable identifier (contains a space)
   emitted for the implicit open-record rest field — is gone from all 3 `init` signatures.
   `old` emitted it 3×, `new` 0×.
3. Version/module-qualified type refs (`ballerina/udp:1.13.6:Error?`, `...:Datagram & readonly`)
   are gone: 3 in `old`, 0 in `new`.

The underlying JSON is otherwise identical: the normalized JSON diff is only 50 lines, and every
hunk is one of the three items above. No declaration, parameter, default, return type, or doc
comment was removed. README is byte-identical to `docs/README.md` in the bala.

Two residual inaccuracies exist in `new` (a lost `distinct` on `Error`, and a non-compiling
`Listener.init` signature), plus one coverage gap shared by both sides (`Caller`'s two public
fields). None of these is a regression.

## 2. Change inventory

Line counts: `old` 205, `new` 239 (+34). Unified diff: 4 hunks, +39/−5 lines.

### Declarations added in `new` (7)

| Kind | Name | New render line |
|---|---|---|
| type (error) | `Error` | 133 |
| class | `Listener` | 139 |
| method | `Listener.init` | 140 |
| method | `Listener.attach` | 147 |
| method | `Listener.'start` | 151 |
| method | `Listener.gracefulStop` | 156 |
| method | `Listener.immediateStop` | 160 |
| method | `Listener.detach` | 167 |

(`Listener` + 6 methods + `Error` — the diff tool's "7 declarations added" counts `class Listener`,
`type Error` and the 5 non-`init` methods; `init` is counted as a method body line.)

### Declarations removed in `new` (0)

None. Top-level declaration sets:

- `old` (8): `ConnectClientConfiguration`, `Datagram`, `ClientConfiguration`,
  `ListenerConfiguration`, `Service`, `Caller`, `ConnectClient`, `Client`
- `new` (10): the same 8, plus `Error` and `Listener`

Class-member function count: `old` 13, `new` 19 (+6, all on `Listener`).

### Declarations modified (3)

| Location | `old` | `new` |
|---|---|---|
| `ConnectClient.init` | `... string localHost = "", anydata Additional Values, ConnectClientConfiguration config) returns ballerina/udp:1.13.6:Error?` | `... string localHost = "", ConnectClientConfiguration config) returns Error?` |
| `Client.init` | `... string localHost = "", anydata Additional Values, ClientConfiguration config) returns ballerina/udp:1.13.6:Error?` | `... string localHost = "", ClientConfiguration config) returns Error?` |
| `Client.receiveDatagram` | `returns ballerina/udp:1.13.6:Datagram & readonly|Error` | `returns Datagram & readonly|Error` |

### Underlying JSON delta

Both JSONs carry 7 `typeDefs` and 3 `clients`. The only structural changes:

- `Listener` typeDef: `old` has no `"type"` key at all → `renderTypeDef` fell through to
  `// Unknown type:`. `new` adds `"type": "Class"`. **The member data (all 6 functions) was already
  present in `old`'s JSON** — it was purely a rendering loss, not an extraction loss.
- `Error` typeDef: both are `"type": "Error"`; `new` adds `"baseType": "error"`, which the new
  renderer uses to emit `type Error error;`.
- Three `"Additional Values"` parameter objects removed.
- Three version-qualified `"name"` values unqualified.

Section markers: 4 in both (`README`, `END README`, `Types`, `Client`) — no structural loss.

## 3. Correctness against library source

Verified against the bala's `modules/udp/*.bal` (authoritative — matches upstream `v1.13.6`;
`ballerina/Ballerina.toml:4` and `gradle.properties:3` both read `1.13.6`).

Public top-level symbols in the default module (10, from
`grep -rhoE '^public [a-z ]*(class|type|function|const|enum|annotation) ...' *.bal`):
`Listener`, `Caller`, `Client`, `ConnectClient`, `ClientConfiguration`, `ConnectClientConfiguration`,
`Datagram`, `Error`, `ListenerConfiguration`, `Service`. **All 10 appear as real declarations in
`new`; only 8 did in `old`.**

Spot-checks of what `new` adds:

| Rendered (new) | Source | Verdict |
|---|---|---|
| `type Error error;` (line 133) | `socket_error.bal:18` `public type Error distinct error;` | exists; `distinct` lost — see §5 |
| `class Listener` (139) | `listener.bal:23` `public class Listener {` | correct kind |
| `Listener.attach(Service s, () name = ()) returns error?` (147) | `listener.bal:43` `public isolated function attach(Service s, () name = ()) returns error?` | **exact match** — the odd `() name = ()` really is in the library source |
| `Listener.'start() returns error?` (151) | `listener.bal:51` | match |
| `Listener.gracefulStop() returns error?` (156) | `listener.bal:60` | match |
| `Listener.immediateStop() returns error?` (160) | `listener.bal:69` | match, incl. "not implemented yet" doc |
| `Listener.detach(Service s) returns error?` (167) | `listener.bal:78` | match |
| `Listener.init(int localPort, ..., ListenerConfiguration config) returns Error?` (140) | `listener.bal:31` `init(int localPort, *ListenerConfiguration config) returns Error?` | param-flattening artefact — see §5 |

Spot-checks of what `new` changes:

- `ConnectClient.init(string remoteHost, int remotePort, decimal timeout = 300, string localHost = "", ConnectClientConfiguration config)` vs
  `connect_client.bal:32` `init(string remoteHost, int remotePort, *ConnectClientConfiguration config)`.
  `timeout = 300` matches `connect_client.bal:76` `decimal timeout = 300;`. Removing
  `anydata Additional Values` is correct: the record's implicit `anydata` rest field is not a
  user-facing parameter.
- `Client.init(decimal timeout = 300, string localHost = "", ClientConfiguration config)` vs
  `connectionless_client.bal:30` `init(*ClientConfiguration config)`; `timeout = 300` matches
  `connectionless_client.bal:87`.
- `Client.receiveDatagram() returns Datagram & readonly|Error` vs
  `connectionless_client.bal:54` `returns (readonly & Datagram)|Error`. Ballerina binds `&` tighter
  than `|`, so the unparenthesised form is semantically identical. Correct, and now uses the local
  name instead of `ballerina/udp:1.13.6:Datagram`.

Unchanged declarations re-verified as still correct in `new`:
`Datagram` (3 required fields — `connectionless_client.bal:74`), `ClientConfiguration` /
`ConnectClientConfiguration` (2 fields each), `ListenerConfiguration` (3 optional fields —
`listener.bal:87`), `Caller.sendBytes` / `Caller.sendDatagram` (`caller.bal:36,46`),
`ConnectClient.writeBytes` / `readBytes` / `close` (`connect_client.bal:43,54,64`),
`Client.sendDatagram` / `close` (`connectionless_client.bal:42,63`).

README: `sed -n '8,72p' new/...bal.txt` vs `docs/README.md` differs only by one trailing blank
line — content is identical, no truncation on either side.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full text of both renders read end to end (205 / 239 lines).
- Top-level declaration sets extracted with `grep -nE '^(client )?(class|type|enum|const|annotation|function) '`
  and compared: `new` is a strict superset of `old` (8 → 10).
- Class-member function counts compared: 13 → 19; no method disappeared from `Caller`,
  `ConnectClient`, or `Client`.
- Normalized (`sort_keys`, `indent`) JSON diff run in full: 50 lines total, all accounted for in
  §2. No `description`, `parameters`, `return`, or `fields` entry was removed except the three
  `"Additional Values"` pseudo-params, which were incorrect to begin with.
- README region diffed against the bala README: identical.
- Doc comments per declaration compared: every `#`-comment block in `old` is present verbatim in
  `new` (the 4 diff hunks touch no doc lines except to add them).
- Version-qualified refs and `// Unknown type:` counts both went to zero — no new degradation
  introduced anywhere.

## 5. Issues in `new` (independent of `old`)

Two, both low severity, neither a regression (the affected declarations did not exist or were
already inaccurate in `old`).

**5.1 — `type Error error;` drops `distinct` (new render line 133).**
Source is `socket_error.bal:18` `public type Error distinct error;`. The render loses the
`distinct` qualifier (and `public`, but visibility is dropped repo-wide by convention). An LLM
reading `type Error error;` may infer that any `error` value is assignable to `udp:Error`, which is
false for a distinct error type. Still a large net improvement over `old`'s bare
`// Unknown type: Error`, which conveyed nothing at all.

**5.2 — `Listener.init` is not valid Ballerina and invents defaults (new render line 140).**
```
function init(int localPort, string remoteHost = "", int remotePort = 0, string localHost = "", ListenerConfiguration config) returns Error?;
```
Source (`listener.bal:31`) is `init(int localPort, *ListenerConfiguration config) returns Error?`.
Two problems:
- The included-record parameter is flattened into individual params **and** the record param is
  retained, so `config` is a required positional parameter following defaulted parameters — that
  does not compile.
- `remoteHost = ""`, `remotePort = 0`, `localHost = ""` are invented. `listener.bal:87-91` declares
  all three fields as optional (`string remoteHost?; int remotePort?; string localHost?;`) with no
  defaults; `""` and `0` are not the library's behaviour (absent means "do not connect to a remote
  host", per the field doc).

This is the same rendering pattern `old` already used for `ConnectClient.init` and `Client.init`
(e.g. `string localHost = ""` where `ClientConfiguration.localHost` is `string localHost?;`), so it
is a pre-existing renderer convention now applied to one more declaration, not a new defect class.
`decimal timeout = 300` in those two is genuine (declared default), only the `localHost` default is
invented.

**Not counted as issues** (shared with `old`, unchanged by the pipeline change):
- `class Service {}` — source is `public type Service distinct service object {...}` (`service.bal:17`),
  a service object type, not a class. Both JSONs tag it `"type": "Class"`, so this originates in the
  Java extractor and is identical on both sides.
- All renders drop `public` / `isolated` / `distinct service` qualifiers throughout.

## 6. Coverage gaps vs. the library

The bala has exactly one module (`modules/udp`), and `package.json` `"export": ["udp"]` — the
default module *is* the whole public API. There is no submodule-only API, so the shared
`getDefaultModule()` limitation costs nothing here.

Top-level public symbols missing from both renders: **none** (all 10 present in `new`).

Member-level gaps present in **both** renders (shared, not regressions):

1. `Caller.remoteHost` — `public string? remoteHost = ();` (`caller.bal:25`). Absent from the
   render and from the JSON: the `Caller` client object in both JSONs has keys
   `['description','functions','name']` only — no `fields` key at all.
2. `Caller.remotePort` — `public int? remotePort = ();` (`caller.bal:26`). Same.

These are documented public fields (`caller.bal:19-21`), and an LLM writing a UDP service cannot
learn from either render that `caller.remoteHost` / `caller.remotePort` are readable. The extractor
appears not to emit fields for client classes at all.

Also unavailable to any render: the optional service methods `onBytes` / `onDatagram` / `onError`.
They exist only as comments inside the `Service` object body (`service.bal:19-22`), so they are not
extractable — but the rendered README (lines 49-71) documents all three with signatures, so the
information is present in both renders via prose.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` in the bala declares `udp-plugin` →
`io.ballerina.stdlib.udp.compiler.UdpCompilerPlugin`, backed by `udp-compiler-plugin-1.13.6.jar`.

From upstream `compiler-plugin/src/main/java/io/ballerina/stdlib/udp/compiler/` (`UdpCompilerPlugin.java:31-33`),
the plugin registers:
- one code analyzer: `UdpServiceAnalyzer` → `UdpServiceValidatorTask` → `UdpServiceValidator`
- two code actions: `OnDatagramCodeTemplate`, `OnBytesCodeTemplate` (generate the `onDatagram` /
  `onBytes` remote function stubs)

`UdpServiceValidator` emits 7 diagnostics (`UDP_101`–`UDP_107`): service must not have both
`onDatagram` and `onBytes`; service must have one of them; missing/invalid parameters; missing
`remote` keyword; invalid return type (must be a subtype of `byte[]|Datagram|Error?`); unaccepted
function names; too many parameters.

**Contributes no types, annotations, or generated symbols** — it is validation + code actions only.
Nothing the plugin implies is missing from the render beyond the service-method contract already
described in the README section. Neither render loses plugin-derived content, and the plugin is
identical for both sides (same bala).

## 8. Other considerations

- **Version**: stable 1.13.6, non-deprecated, `graalvmCompatible: true`, built with
  `ballerina_version 2201.12.0`, `language_spec_version 2024R1`. No pre-1.0 concerns.
- **Size / tokens**: tiny library. 205 → 239 lines (+16.6%), 6,740 → 7,767 bytes (+15.2%). The
  growth buys the entire `Listener` API, which is the primary server-side entry point — very high
  value per added token.
- **Doc quality**: source typo `privovided` (`listener.bal:26`) is faithfully carried into the
  render (line 135). Doc comments for record fields are wrapped mid-sentence with the continuation
  lines un-indented and un-prefixed (e.g. `new` lines 81-83, 107-109, 121-122), producing lines that
  would not parse as doc comments. This is identical in `old` and `new` and originates in the JSON
  descriptions, not the renderer change.
- **Non-compiling render**: as a whole neither render is compilable Ballerina (missing `public`,
  bodiless functions, the `init` param-order problem). `new` is strictly closer to compilable than
  `old`, which additionally had the identifier-with-a-space `anydata Additional Values`.
- `import ballerina/udp;` is emitted at line 5 in both — correct module.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags .../module-ballerina-udp \| grep 1.13` | `v1.13.6` exists → `eb6cd4997760b39406e66553dae730a681392687` |
| `git clone --depth 1 --branch v1.13.6 ... src` | success |
| `grep -n version src/ballerina/Ballerina.toml` | line 4: `version = "1.13.6"` — matches pin |
| `grep -n version src/gradle.properties` | line 3: `version=1.13.6` |
| `ls .../bala/.../1.13.6/java21/modules` | one module: `udp` (no submodules) |
| `cat .../java21/package.json` | `"export": ["udp"]`, `graalvmCompatible: true`, `ballerina_version 2201.12.0` |
| `wc -l old/... new/...` | 205 / 239 |
| `wc -c` (ls -la) | 6740 / 7767 bytes |
| `grep -c '^// Unknown type:'` | old 2, new 0 |
| `grep -c 'ballerina/udp:1\.13\.6:'` | old 3, new 0 |
| `grep -n '^// --- '` | 4 markers each side, same order |
| `grep -nE '^(client )?(class\|type\|...) '` | old 8 top-level decls, new 10 |
| `grep -cE '^    (remote )?function '` | old 13, new 19 |
| `diff <(json.dumps sorted old) <(... new) \| wc -l` | 50 lines total; contents: 3× `Additional Values` removal, 3× unqualified type name, `+baseType: error`, `+type: Class` on `Listener` |
| Python inspect of `typeDefs` | old: `Listener` has `type=None`; new: `type='Class'`. Both have 7 typeDefs / 3 clients |
| Python inspect of `clients[Caller]` keys | `['description','functions','name']` on **both** sides — no `fields` |
| `diff <(sed -n '8,72p' new/...bal.txt) .../docs/README.md` | identical except one trailing blank line |
| `wc -l .../modules/udp/*.bal` | 468 lines total across 7 files |
| `cat .../modules/udp/listener.bal` | init at :31, attach at :43 (`() name = ()` confirmed), 'start :51, gracefulStop :60, immediateStop :69, detach :78, `ListenerConfiguration` :87 (3 optional fields, no defaults) |
| `cat .../modules/udp/socket_error.bal` | :18 `public type Error distinct error;` |
| `cat .../modules/udp/service.bal` | :17 `public type Service distinct service object {...}` (methods commented out) |
| `sed -n '66,82p' connect_client.bal` | `ConnectClientConfiguration`: `decimal timeout = 300; string localHost?;` |
| `sed -n '17,35p' caller.bal` | `public string? remoteHost = ();` :25, `public int? remotePort = ();` :26 |
| `grep -rhoE '^public [a-z ]*(class\|type\|...)' *.bal \| sort` | exactly 10 public top-level symbols |
| `cat .../compiler-plugin/compiler-plugin.json` | `udp-plugin` → `UdpCompilerPlugin`, jar 1.13.6 |
| `grep -n 'add\|class' UdpCompilerPlugin.java` | 1 code analyzer + 2 code actions |
| `grep -n 'CODE_1\|"' UdpServiceValidator.java` | 7 diagnostic codes UDP_101–107 |
| Read `OLD_AND_NEW_DIFFS/udp_diff.md` | its counts (205/239, +39/−5, 4 hunks, 2→0 unknown, 3→0 qualified, 7 added / 0 removed) all reproduced independently — no discrepancies |

## 10. Caveats and unverified items

- The published bala and the `v1.13.6` upstream tag were both inspected; the `modules/udp/*.bal`
  files in the bala were used as authoritative for every signature check. They were not diffed
  file-by-file against `src/ballerina/*.bal`, but every line cited above was read in the bala copy
  directly, so no claim rests on the GitHub copy alone. Line numbers cited are from the bala files
  (which are byte-identical in structure to the upstream `ballerina/` directory for the files
  checked).
- `UdpServiceValidator.java` was inspected by targeted `grep`, not read in full; the diagnostic list
  is derived from its message constants (`CODE_101`–`CODE_107` and their format strings). The claim
  that the plugin contributes no types/annotations rests on `UdpCompilerPlugin.java:31-33`
  registering only an analyzer and two code actions — verified — but the two code-template classes
  were not read line by line.
- Whether the missing `Caller.remoteHost` / `Caller.remotePort` fields are a deliberate extractor
  choice (client objects render methods only) or an oversight was not determined; only the fact of
  their absence on both sides was verified.
- The claim that `new`'s `Listener.init` "does not compile" is a reading of Ballerina's
  positional-after-defaulted parameter rule; it was not confirmed by actually invoking `bal build`
  on the render (the renders are not standalone compilable units in any case).

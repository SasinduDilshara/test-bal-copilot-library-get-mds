# ballerinax/googleapis.gcalendar 4.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/googleapis.gcalendar` |
| Pinned version | `4.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-googleapis.calendar |
| Tag reviewed | `v4.0.1` (exact tag; sources byte-identical to bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/googleapis.gcalendar/4.0.1` |
| Old render | `1240` lines |
| New render | `1243` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The change set is small and entirely positive. `new` gains a real definition for the module's
`Error` type (`old` degraded it to `// Unknown type: Error`), drops all 10 version/module-qualified
type references (`ballerinax/googleapis.gcalendar:4.0.1:X`, `ballerina/lang.int:0.0.0:Signed32`) in
favour of the names a user actually writes, and surfaces two `@display` annotations that exist in
the library source. Nothing is removed: the declaration set is identical apart from the added
`Error`, all 47 public types and all 31 client functions are present on both sides with byte-identical
signatures except `init`'s return type, and the README section is unchanged. No regressions found.

## 2. Change inventory

Line counts (`wc -l`): old `1240`, new `1243`. Unified diff: `+14 / -11` lines across `9` hunks
(`diff -u | grep -c '^+[^+]'` = 14, `'^-[^-]'` = 11).

| Kind | old | new | delta |
|---|---|---|---|
| Top-level `type` declarations | 46 | 47 | +1 (`Error`) |
| `client class` | 1 | 1 | 0 |
| Client methods (`resource function`) | 30 | 30 | 0 |
| Client `init` | 1 | 1 | 0 |
| `enum` / `const` / `annotation` / `service` / `listener` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 10 | 0 | −10 |
| `// --- section ---` markers | 4 | 4 | 0 |
| README body (lines 7–291) | — | — | identical (`diff` empty) |

JSON level (both files parse; same top-level keys): `typeDefs` 47 vs 47 (same name set, no adds/removes),
`clients[0].functions` 31 vs 31, `functions`/`services`/`annotations` 0 on both, `readme` and
`description` byte-equal.

**Added (1)**
- `type Error error;` with doc `# Represents any error related to the \`gcalendar\` module.`
  (new:295–296). In `old` this was `// Unknown type: Error` (old:295).

**Removed (0)** — none. `comm` of the sorted type-name sets shows the only delta is `Error`.

**Modified (9 typeDefs + 1 client function)** — JSON deep-diff identifies exactly:
`ConnectionConfig`, `ProxyConfig` (annotations added); `FreeBusyResponse`, `Colors`,
`EventReminder`, `Event`, `EventAttendee`, `FreeBusyRequest` (type refs de-qualified);
`Error` (gained `baseType: "error"`); and `Client.init` (return type de-qualified).

Rendered effect:
1. `record {|ballerinax/googleapis.gcalendar:4.0.1:FreeBusyCalendar...;|}` → `record {|FreeBusyCalendar...;|}`
   (4 occurrences, in `FreeBusyResponse` ×2 and `Colors` ×2).
2. `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (5 occurrences: `EventReminder.minutes`,
   `Event.sequence`, `EventAttendee.additionalGuests`, `FreeBusyRequest.calendarExpansionMax`,
   `FreeBusyRequest.groupExpansionMax`).
3. `function init(...) returns ballerinax/googleapis.gcalendar:4.0.1:Error?` → `returns Error?`.
4. `@display {label: "Connection Config"}` added above `ConnectionConfig`;
   `@display {label: "", kind: "password"}` added above `ProxyConfig.password`.

## 3. Correctness against library source

Upstream `v4.0.1` `ballerina/{client,types,error,utils}.bal` are byte-identical to the bala's
`modules/googleapis.gcalendar/` copies (`diff -q`, all four silent), so GitHub and bala agree.

Every change in `new` is confirmed against source:

| Change in `new` | Source evidence | Verdict |
|---|---|---|
| `type Error error;` + doc | `error.bal:17-18` — `# Represents any error related to the \`gcalendar\` module.` / `public type Error distinct error;` | correct (see §5 for `distinct`) |
| `record {\|FreeBusyCalendar...;\|}` / `FreeBusyGroup` | `types.bal:87,89` — literally `record {\|FreeBusyCalendar...;\|}` | exact match |
| `record {\|ColorDefinition...;\|}` ×2 | `types.bal:590,592` | exact match |
| `int:Signed32` ×5 | `grep -c 'int:Signed32' types.bal` = 5, render count = 5 (e.g. `types.bal:371` `int:Signed32 minutes?;`) | exact match, count matches |
| `init(...) returns Error?` | `client.bal:28` — `public isolated function init(ConnectionConfig config, string serviceUrl = "https://www.googleapis.com/calendar/v3") returns Error? {` | exact match incl. default URL |
| `@display {label: "Connection Config"}` | `types.bal:20` | exact match |
| `@display {label: "", kind: "password"}` | `types.bal:73` | exact match |

Client surface: source has 30 `resource isolated function` declarations + `init` (31 total);
`new` renders 30 resource functions + `init`, and the rendered path/accessor list matches the source
list one-for-one (`post calendars` … `patch users/me/calendarList/[string calendarId]`). The 30
resource-function signature lines are byte-identical between `old` and `new` (`diff` empty).

## 4. Regressions

**None found.**

What was checked to conclude that:
- Type-name set: `comm -23 old new` (sorted `^type` names) → empty; nothing dropped.
- Client methods: `diff` of the 30 extracted method signature lines old vs new → empty.
- JSON: no `typeDefs` entry present in `old` is absent in `new`; no client function removed
  (31 = 31, same order, only `init` differs).
- README/section content: `diff` of lines 7–291 → identical; all 4 section markers present in both.
- Docs: comment-line count went 361 → 362 (the one added `Error` doc); nothing lost.
- The 11 removed diff lines are exactly the 10 qualified-type lines plus the `// Unknown type: Error`
  placeholder; all are replaced by better lines.
- No malformed syntax introduced: the added lines are a valid type definition, two valid annotation
  attachments and de-qualified type names that are legal Ballerina (the qualified forms in `old`
  were *not* legal Ballerina).

## 5. Issues in `new` (independent of `old`)

Three fidelity losses, all low severity. Only (1) touches changed lines; (2) and (3) are identical
in `old` and are renderer-wide conventions, listed here because the brief asks for inaccuracies
regardless of side.

1. **`distinct` dropped from `Error`.** Source `error.bal:18` is `public type Error distinct error;`;
   `new:296` renders `type Error error;` (JSON `baseType: "error"`). An LLM cannot tell this is a
   distinct error type. Still strictly better than `old`'s `// Unknown type: Error`.
2. **Closed records rendered as open.** `ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`,
   `OAuth2RefreshTokenGrantConfig` are `record {| ... |}` in `types.bal:21,55,65,78`; both renders
   emit `record { ... }`. Identical in `old`.
3. **Field defaults dropped, turning defaulted fields into optional ones.** e.g. `ProxyConfig`
   (`types.bal:65-76`) has `string host = ""`, `int port = 0`, `string userName = ""`,
   `string password = ""`; both renders emit `string host?; int port?; string userName?; string password?;`.
   Same for `ClientHttp1Settings.keepAlive = http:KEEPALIVE_AUTO` / `chunking = http:CHUNKING_AUTO`
   (`types.bal:57,59`) and, most consequentially,
   `OAuth2RefreshTokenGrantConfig.refreshUrl = "https://accounts.google.com/o/oauth2/token"`
   (`types.bal:81`) → `string refreshUrl?;`. A consumer loses the Google-specific default refresh URL.
   Identical in `old`; also, `*http:OAuth2RefreshTokenGrantConfig` inclusion is flattened into
   inline fields on both sides (that flattening is accurate, just undocumented for the inherited fields).

`public` / `isolated` / `client` modifiers are normalised away on both sides (`public isolated client
class Client` → `client class Client`); treated as a render convention, not an inaccuracy.

## 6. Coverage gaps vs. the library

**Zero gaps in the default module.** The bala's default module exports 47 public types
(`grep -cE '^public type'` across `error.bal` + `types.bal` = 47) plus one public class
(`client.bal:20 public isolated client class Client`) and no public module-level functions
(`grep -E '^public' utils.bal` → no matches). `comm` between the bala's public-type list and the
`new` render's type list is empty in both directions — all 47 are rendered, plus the `Client` class.

Submodules: the bala ships `modules/googleapis.gcalendar.mock` alongside the default module, but
`package.json` `"export": ["googleapis.gcalendar"]` lists only the default module, so the mock module
is not public API and its absence from the renders is correct, not a gap.

## 7. Compiler plugin

None. The bala has no `compiler-plugin/` directory (contents: `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json`), and the upstream `v4.0.1` tree has no
`*compiler-plugin*` directory at depth ≤2. `Ballerina.toml` declares only `[build-options]` and
`[platform.java17]`. Nothing plugin-derived is expected in the render, and nothing is missing.

## 8. Other considerations

- Stable release (4.0.1); no deprecation markers in `package.json` or Central metadata fields present
  in the bala. `graalvmCompatible: true`, `ballerina_version: 2201.8.4`.
- Size: 69,693 → 69,532 bytes (−161 B) despite +3 lines — the de-qualified type names more than pay
  for the added `Error` definition and annotations. Token impact is a small net win.
- The `old` render contained 10 lines of non-compiling Ballerina (`ballerina/lang.int:0.0.0:Signed32`,
  `ballerinax/googleapis.gcalendar:4.0.1:Error`). `new` contains none — an LLM copying from `new`
  now produces valid type references.
- The library's own API surface omits the Calendar `settings`/`Setting` endpoints even though the
  `Settings`/`Setting` types are published; that is an upstream library characteristic, identical on
  both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old new` | 1240 / 1243 |
| 2 | `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| 3 | `grep -n '^// --- '` old / new | both: README@7, END README@291, Types@293, Client@1115/1118 |
| 4 | `git ls-remote --tags` on repo | `v4.0.1` exists (`49f1a739…`); cloned `--depth 1 --branch v4.0.1` |
| 5 | `diff -q src/ballerina/{client,types,error,utils}.bal bala/modules/googleapis.gcalendar/…` | all identical |
| 6 | `wc -l` bala module sources | client.bal 841, error.bal 18, types.bal 783, utils.bal 217 |
| 7 | `comm` bala public types vs `new` `^type` names | both directions empty → 47/47 covered |
| 8 | `diff` old vs new sorted `^type` name lists | only addition: `Error` |
| 9 | `diff` of 30 client method signature lines old vs new | empty |
| 10 | `grep -E '(resource\|remote) isolated function' client.bal` count | 30 (+`init` = 31), matches render |
| 11 | JSON compare: `typeDefs` len | 47 / 47, same name set, 9 entries differ |
| 12 | JSON compare: `clients[0].functions` | 31 / 31, only `init` differs |
| 13 | JSON compare: `readme`, `description`, `name` | byte-equal |
| 14 | `diff` old lines 7–291 vs new 7–291 (README) | identical |
| 15 | `grep -cE '[a-z0-9._]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 10 / 0 |
| 16 | `grep -c 'int:Signed32'` bala types.bal / new render | 5 / 5 |
| 17 | `grep -c 'lang.int:0.0.0:Signed32'` old render | 5 |
| 18 | `error.bal:17-18` | `public type Error distinct error;` |
| 19 | `types.bal:20`, `types.bal:73` | the two `@display` annotations |
| 20 | `types.bal:87,89,590,592` | inline `record {\|…...;\|}` map types |
| 21 | `client.bal:28` | `init` signature incl. default `serviceUrl` |
| 22 | `grep -cE '^\s*#'` old / new (doc lines) | 361 / 362 |
| 23 | `grep -c 'Special Agent Note'` old / new | 15 / 15 |
| 24 | `ls` bala root + `find src -maxdepth 2 -iname '*compiler*plugin*'` | no compiler plugin either place |
| 25 | `package.json` `export` | `["googleapis.gcalendar"]` only; `.mock` module not exported |
| 26 | `diff -u old new \| grep -c '^+[^+]' / '^-[^-]'` | 14 / 11 |
| 27 | `ls -la` render/JSON sizes | old 69693 B / new 69532 B |

## 10. Caveats and unverified items

- The renders were not compiled. "Valid Ballerina" claims are based on syntax inspection, not on
  running `bal build` against the rendered text (the render is a stub listing, not a buildable
  package, so compiling it is not meaningful).
- I did not re-run the two-stage extraction pipeline; I audited the supplied renders/JSONs as given
  and cross-checked them against the bala and the `v4.0.1` upstream tag.
- Ballerina Central was not re-queried over the network; version/export/metadata facts come from the
  bala's `package.json` and `bala.json`, which is the artefact the extractor actually consumed.
- Whether losing `distinct` on `Error` and losing record `record {| |}` closedness / field defaults
  is intentional renderer policy (rather than a defect) is unverified — I did not read the
  `toSyntaxString` source. Both behaviours are identical on `old` and `new`, so neither affects the
  regression verdict.

# ballerinax/redis 3.4.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/redis` |
| Pinned version | `3.4.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-redis |
| Tag reviewed | `v3.4.1` (commit `112d08f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/redis/3.4.1` |
| Old render | `695` lines (24,373 bytes) |
| New render | `838` lines (36,963 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerinax/redis` is a single-module package (`export: ["redis"]`, one directory under
`modules/`), so there is no submodule-coverage question. The bala sources are byte-identical to
upstream `v3.4.1` (`diff -q` clean on all four `.bal` files), so GitHub and the bala agree.

Both renders extract exactly the same symbol set: 12 `typeDefs` and 1 client with 113 functions in
both JSONs. When `@display` annotations are stripped from both files, the entire semantic diff is
**four changes, all in `new`'s favour**:

1. `// Unknown type: Error` → a real `type Error error;` with its doc comment.
2. `// Unknown type: ConnectionUri` → a real `type ConnectionUri string;` with its doc comment.
3. `returns ballerinax/redis:3.4.1:Error?` → `returns Error?` (version-qualified ref removed).
4. `remote function close()` → `function close()` — which matches the source
   (`public isolated function close()`, `client.bal:1397`), i.e. `old` was factually wrong.

On top of that, `new` adds 348 `@display` annotations that `old` dropped entirely (180 distinct
annotation texts, **every one of which appears verbatim in the bala source** — zero invented).

Nothing present in `old` is missing, truncated, or degraded in `new`. Regressions: **0**.

## 2. Change inventory

Line counts (`wc -l`): old 695 → new 838 (+143 net; diff reports +253 / −110 raw lines, 4 hunks).

| Kind | old | new | Δ |
|---|---|---|---|
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 2 | 0 | **−2** |
| Version-qualified type refs (`org/mod:ver:Type`) | 1 | 0 | **−1** |
| `typeDefs` in JSON | 12 | 12 | 0 |
| Clients in JSON | 1 | 1 | 0 |
| Client functions in JSON | 113 | 113 | 0 |
| `remote function` lines in render | 112 | 111 | −1 (see below) |
| `@display` occurrences | 0 | 348 | **+348** |
| README block (lines 1–123) | identical | identical | 0 |

**Declarations added in `new` (2):**
- `type Error error;` (+ doc `# Represents a redis generic error`)
- `type ConnectionUri string;` (+ 2-line doc, + `@display {label: "Connection URI"}`)

**Declarations removed in `new`: 0.** The `remote function` count drop from 112→111 is not a
removal — `close()` is still present (new:837), it is simply no longer mis-labelled `remote`.

**Declarations modified in `new` (2):** `Client.init` return type de-qualified; `Client.close`
modifier corrected.

**Annotations added in `new` (348 occurrences / 180 distinct):** on the client class
(`@display {label: "Redis Client", iconPath: "icon.png"}`), on 111 remote functions, on record
type definitions (`ConnectionConfig`, `ConnectionParams`, `Options`, `SecureSocket`, `CertKey`,
`ConnectionUri`), and on record fields and function parameters.

JSON also grew: `old` 123,189 bytes → `new` 181,368 bytes; the client object gains an
`annotations` key (`old` client keys: `name, description, functions`; `new`: `+ annotations`).

## 3. Correctness against library source

Bala sources: `modules/redis/{client.bal (1400 L), types.bal (142 L), errors.bal (18 L), init.bal (25 L)}`.
Verified byte-identical to upstream tag `v3.4.1`.

**Function set (exhaustive).** Extracted all 114 function declarations from `client.bal` and all
113 client functions from `new/ballerinax_redis.json`. `diff` shows exactly one source-only entry:
`initClient` — a non-public, `@java:Method` internal helper (`client.bal:37`), correctly excluded.
Every other function (111 `remote` + `init` + `close`) is present. No invented functions.

**Parameters (exhaustive).** For all 113 rendered functions, every rendered parameter name was
checked against the corresponding source parameter list. Only `init` mismatched (see §5.2); all
111 remote functions match exactly.

**Return types (exhaustive).** All 113 rendered `returns` clauses were compared against the source
return type with `@display` stripped. 113/113 match (the sole reported mismatch was an artifact of
my source-parsing regex on `init`; the rendered `Error?` equals the source `Error?` at
`client.bal:29`). `Error?` is rendered as `Error|()` in some places — semantically equivalent.

**Annotations (exhaustive).** All 180 distinct `@display {...}` strings in `new` were compared with
the 215 distinct `@display` strings in the bala sources — `comm -23` returns empty: **no `@display`
annotation in the render is absent from the source**. Spot-verified: `@display {label: "Redis
Client", iconPath: "icon.png"}` (`client.bal:22` → new:269); `@display {label: "Enrich Value"}` on
`append` (`client.bal:47` → new:275); `@display {label: "Key"}` / `{label: "Value To Append"}`
params (`client.bal:48-49` → new:276); `@display {label: "Connection Config"}` on
`ConnectionConfig` (`types.bal:25` → new:139).

**New type defs verified.** `errors.bal:18` `public type Error distinct error;` → new:134
`type Error error;`. `types.bal:59-63` `public type ConnectionUri string;` with
`@display {label: "Connection URI"}` → new:158-159. Both correct in kind and underlying type
(caveat on `distinct` in §5.1).

**README.** `diff` of lines 1–123 of both renders: identical. JSON `readme` fields byte-identical
(4,205 chars each), `description` identical.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Normalized semantic diff (both files with `@display {...}` stripped, whitespace-trimmed):
  produces exactly 4 changed hunks, all listed in §1, all improvements. Nothing else differs.
- Declaration-name set diff for `remote function`: the only delta is `close`, which is still
  present in `new` and is *more* correct there (source declares it non-remote).
- `typeDefs` name/kind lists in the two JSONs are identical (12 entries, same names, same kinds).
- Client function-name lists in the two JSONs are identical (113 entries).
- README section byte-identical; all doc comments preserved (no doc line appears in the `old`-only
  side of the normalized diff).
- No parameter, default value, or return type present in `old` is absent in `new`.
- No non-ASCII / mojibake introduced (`LC_ALL=C grep '[^ -~]' new/...` → no matches).

## 5. Issues in `new` (independent of `old`)

None of these are regressions — items 2–8 are present identically in `old`.

1. **`distinct` lost on `Error` (new-only, because `old` emitted nothing).** Source
   `errors.bal:18` is `public type Error distinct error;`; `new:134` renders `type Error error;`.
   An LLM consuming this loses the fact that `redis:Error` is a distinct error type, which matters
   for `is redis:Error` narrowing across modules. Still strictly better than `old`'s
   `// Unknown type: Error`.
2. **`Client.init` signature is malformed and non-compiling (shared with `old`).**
   Source (`client.bal:29`): `public isolated function init(*ConnectionConfig config) returns Error?`.
   Render (new:271): `function init(ConnectionUri|ConnectionParams connection = "redis://localhost:6379", boolean connectionPooling = false, boolean isClusterConnection = false, SecureSocket secureSocket = {}, ConnectionConfig config) returns Error?;`
   The included-record parameter is expanded into its fields **and** a trailing required
   `ConnectionConfig config` is appended after defaulted parameters — invalid Ballerina, and it
   suggests a positional call shape that does not exist.
3. **Record field defaults dropped; defaulted fields shown as optional (shared).** e.g.
   `types.bal:47-48` `string host = "localhost"; int port = 6379;` render as `string host?;
   int port?;` (new:168, new:171). Same for `connectionPooling = false`,
   `isClusterConnection = false`, `database = 0`, `connectionTimeout = 60`, `idle = 7200`,
   `interval = 75`, `count = 9`, `verifyMode = FULL`, `startTls = false`. The render therefore
   loses every default value in the config surface — exactly the information an LLM needs to write
   a minimal client init.
4. **Closed records rendered as open (shared).** All 6 record types in `types.bal` are `record {| |}`;
   the render emits `record { }` (`grep -c 'record {|' new` → 0). Implies extra fields are allowed
   when they are not.
5. **`public` / `isolated` qualifiers dropped (shared).** `public isolated client class Client`
   (`client.bal:23`) → `client class Client` (new:270); all `isolated remote function` → `remote
   function` (`grep -c isolated new` → 0). Isolation matters for concurrency-safe usage.
6. **Broken doc comment continuation (shared).** new:197-198 (old:177-178):
   ```
       # TCP keep-alive configuration for detecting stale connections.
   Set to `()` (nil) to disable. Default is `()` (disabled).
   ```
   The second line has no `#` prefix and no indentation — it escapes the doc comment and makes the
   record body non-parsable. Source `types.bal:82-83` has both lines correctly `#`-prefixed.
7. **Enum member order inverted (shared).** Source `types.bal:139-141`: `NONE, CA, FULL`;
   render (new:258-262): `FULL, CA, NONE`. Cosmetic, but the constants block above
   (new:127-131) uses source order, so the file is internally inconsistent.
8. **Return-position `@display` annotations not carried (informational).** Source has 458 `@display`
   occurrences; 110 of them are in `returns @display {...}` position (`grep -c 'returns @display'`
   → 110). 458 − 110 = 348 = exactly what `new` emits. So the omission is systematic and complete,
   not random loss. `old` carried none of the 458.

## 6. Coverage gaps vs. the library

**Zero.** `package.json` declares `export: ["redis"]` and `modules/` contains only `redis`, so the
default module *is* the whole public API — no submodule-only API exists for this package.

Public symbols in the default module, all present in both renders:

| Symbol | Source | In render |
|---|---|---|
| `Client` (client class, 113 exposed functions) | `client.bal:23` | yes |
| `Error` | `errors.bal:18` | `new` yes / `old` degraded |
| `ConnectionConfig` | `types.bal:26` | yes |
| `ConnectionParams` | `types.bal:44` | yes |
| `ConnectionUri` | `types.bal:63` | `new` yes / `old` degraded |
| `KeepAliveConfig` | `types.bal:70` | yes |
| `Options` | `types.bal:85` | yes |
| `SecureSocket` | `types.bal:104` | yes |
| `CertKey` | `types.bal:124` | yes |
| `SslVerifyMode` (+ `NONE`, `CA`, `FULL`) | `types.bal:138` | yes |

Only `initClient` (private helper) and the module `init()`/`setModule()` in `init.bal` are absent,
all correctly so — none are public API.

## 7. Compiler plugin

**This package ships no compiler plugin.** `find <clone> -iname '*compiler-plugin*'` returns
nothing; the bala has no `compiler-plugin/` directory and no `compiler-plugin.json`
(`ls` of the bala root shows only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
`package.json`, `platform`). Nothing plugin-implied is therefore missing from the render.

The package is `graalvmCompatible: true`, built with `ballerina_version: 2201.12.12`, and carries
16 Java platform dependencies (lettuce-core 6.3.1, netty 4.1.136, etc.) — none of which should or
do surface in the render.

## 8. Other considerations

- **No deprecations.** No `@deprecated` in any bala `.bal` file.
- **Stable version.** `3.4.1` is post-1.0 and `v3.4.1` is the latest tag on the repo
  (`git ls-remote --tags` — highest tag is `v3.4.1`).
- **Size / token impact.** Render grew 24,373 → 36,963 bytes (+51.7% bytes, +20.6% lines) and the
  JSON grew 123,189 → 181,368 bytes (+47.2%). Essentially all of the growth is `@display`
  annotation text. For a Copilot prompt these annotations are UI-oriented labels (WSO2 low-code
  designer metadata); they are faithful to the source but carry low semantic value per token for
  code generation. Worth flagging as a cost/benefit question, not a correctness one.
- **Doc quality.** Doc comments are good and fully preserved; only the one broken continuation line
  (§5.6) and the `# + uri - ...` field doc on the non-record `ConnectionUri` (a source-side
  oddity, correctly dropped by both renders).
- **Non-compiling render.** The render as a whole would not compile as Ballerina (§5.2, §5.6), but
  identically so on both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ new/ *.bal.txt` | 695 / 838 |
| 2 | `wc -c` on both renders and both JSONs | 24,373 / 36,963; 123,189 / 181,368 |
| 3 | `grep -c '^// Unknown type:'` both renders | old 2, new 0 |
| 4 | `grep -n '^// --- '` both renders | 4 markers each, same names |
| 5 | `ls -R <bala>/java21` | single module `redis`; no compiler-plugin dir |
| 6 | `cat <bala>/java21/package.json` | `export: ["redis"]`, ballerina 2201.12.12, graalvmCompatible |
| 7 | `wc -l <bala>/modules/redis/*.bal` | client 1400, errors 18, init 25, types 142 |
| 8 | `git ls-remote --tags <repo>` | `v3.4.1` exists and is latest |
| 9 | `git clone --depth 1 --branch v3.4.1`; `git log -1` | commit `112d08f`, `git describe` → `v3.4.1` |
| 10 | `diff -q <clone>/ballerina/*.bal <bala>/modules/redis/*.bal` | all 4 identical |
| 11 | Python normalized diff (both files, `@display` stripped) | 4 hunks only, all improvements |
| 12 | `diff <(grep -oE '^    remote function \w+' old\|sort) <(… new\|sort)` | only `close` differs |
| 13 | `grep -n 'close' both renders` | old:694 `remote function close`, new:837 `function close` |
| 14 | `grep -n 'public isolated function close' client.bal` | line 1397 — non-remote, so `new` is right |
| 15 | JSON typeDefs name+kind list, both sides | identical 12 entries |
| 16 | JSON client function count, both sides | 113 each |
| 17 | `diff` source-function-name list (114) vs JSON list (113) | only `initClient` source-only |
| 18 | Python: all rendered params vs source param lists (113 fns) | 4 mismatches, all on `init` (§5.2) |
| 19 | Python: all rendered return types vs source (113 fns) | 113/113 match |
| 20 | `grep -o '@display' \| wc -l` render/source | old 0, new 348, source 458 |
| 21 | `grep -c 'returns @display' client.bal` | 110 → 458−110 = 348 ✔ |
| 22 | `comm -23 <(uniq @display in new) <(uniq @display in bala src)` | empty — zero invented |
| 23 | `diff <(sed -n 1,123p old) <(sed -n 1,123p new)` | README identical |
| 24 | JSON `readme` / `description` equality | both True, 4,205 chars |
| 25 | `LC_ALL=C grep -n '[^ -~]' new` | no matches (no encoding damage) |
| 26 | `grep -c 'record {|' new` | 0 (closed records rendered open) |
| 27 | `grep -c isolated new` | 0 (isolated qualifier dropped) |
| 28 | `find <clone> -iname '*compiler-plugin*'` | no results |
| 29 | Read new:127-299, new:820-838, old:120-269, old:680-695 | manual inspection of Types + Client head/tail |
| 30 | `cat <bala>/modules/redis/{types,errors,init}.bal` | full read of all non-client sources |

## 10. Caveats and unverified items

- **Return-position `@display` annotations (110)** are absent from `new`. I verified the arithmetic
  (458 − 110 = 348) and that the omission is systematic, but I did not read the spec-v2 extractor
  source to confirm this is intentional design rather than an extraction bug. Recorded as
  informational (§5.8), not as a defect.
- **Line numbers cited for `types.bal`** in §6 are counted from the bala file including its
  15-line licence header; I read the file in full but cited approximate declaration lines rather
  than running `grep -n` for each of the 10 symbols individually.
- I did not attempt to compile either render with `bal build`; the non-compiling claims in §5.2
  and §5.6 are from reading the emitted syntax, not from a compiler run. Both defects are present
  identically on both sides, so they do not affect the verdict either way.
- Ballerina Central metadata was not re-queried over the network; module list and version were
  taken from the bala's `package.json`, which the brief designates as authoritative.

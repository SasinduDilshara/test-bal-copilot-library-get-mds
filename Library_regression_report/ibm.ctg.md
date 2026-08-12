# ballerinax/ibm.ctg 0.1.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ibm.ctg` |
| Pinned version | `0.1.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ibm.ctg |
| Tag reviewed | `v0.1.1` (exact match; commit `8d4a2222b546f416e6b115694f2611ec42cc59dd`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ibm.ctg/0.1.1/java17` |
| Old render | `253` lines |
| New render | `254` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Tiny library: one default module (`ibm.ctg`), 4 `.bal` files, 171 lines total. The whole public
surface is 5 type defs + 1 client class with 3 methods.

`new` differs from `old` in exactly two places, both spec-v2 fixes:

1. `// Unknown type: Error` (degraded placeholder) is replaced by a real definition with its doc
   comment: `# Represents a IBM CTG distinct error.` / `type Error error;`.
2. The version-qualified return type `ballerinax/ibm.ctg:0.1.1:Error?` on `Client.init` becomes the
   plain `Error?`.

Nothing was removed, truncated, or degraded. The README, all 4 record types, and all 3 client
methods are byte-identical between the two renders. **No regressions found.**

Several fidelity issues exist in `new` (dropped `distinct`, dropped record field defaults, an
included-record-parameter expansion that produces non-compiling Ballerina), but every one of them is
present identically in `old`, so they are pre-existing renderer behaviour, not spec-v2 regressions.

## 2. Change inventory

Line counts (`wc -l`): old 253, new 254 (+1). Unified diff: 2 hunks, +3 / −2 lines.

| Kind | old | new | Delta |
|---|---|---|---|
| Type defs rendered | 4 (`ConnectionConfig`, `Auth`, `SecureSocket`, `EciRequest`) | 5 (+ `Error`) | **+1** |
| `// Unknown type:` placeholders | 1 (`Error`) | 0 | **−1** |
| Version-qualified type refs (`ballerinax/ibm.ctg:0.1.1:…`) | 1 | 0 | **−1** |
| Client classes | 1 (`Client`) | 1 | 0 |
| Client methods | 3 (`init`, `execute`, `close`) | 3 | 0 |
| Module-level functions | 0 | 0 | 0 |
| Services / listeners / annotations / enums / consts | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| README block (lines 7–175) | identical | identical | 0 |

**Added declarations (1):** `type Error error;` (with doc comment).
**Removed declarations (0):** none.
**Modified declarations (1):** `Client.init` return type `ballerinax/ibm.ctg:0.1.1:Error?` → `Error?`.

JSON-level diff (`old/*.json` vs `new/*.json`): only 2 of 8 top-level keys differ.

- `typeDefs.Error`: `new` gains `"baseType": "error"`; `old` had no `baseType` (which is why
  `renderTypeDef` fell through to the placeholder).
- `clients[0].init.returnType.name`: `"ballerinax/ibm.ctg:0.1.1:Error?"` → `"Error?"`.
- `readme`, `description`, `name`, `functions` (`[]`), `services` (`[]`), `annotations` (`[]`) are
  byte-identical.

## 3. Correctness against library source

Upstream `v0.1.1` `ballerina/*.bal` is **byte-identical** to the bala's `modules/ibm.ctg/*.bal`
(`diff` returned no output for all 4 files), so GitHub and the bala agree — no tie-break needed.

Verification of the thing `new` adds:

| Render (new) | Library source | Verdict |
|---|---|---|
| `# Represents a IBM CTG distinct error.` `type Error error;` | `errors.bal:17-18` — `# Represents a IBM CTG distinct error.` / `public type Error distinct error;` | Correct name, correct doc, correct base type. `distinct` and `public` are dropped (see §5.1). |
| `returns Error?` on `init` | `client.bal:30` — `public isolated function init(*ConnectionConfig configs) returns Error?` | Correct; `new` now matches the source's spelling, `old` did not. |

Exhaustive check of the rest of the surface (both renders identical here):

| Symbol | Source | In render? | Signature accurate? |
|---|---|---|---|
| `ConnectionConfig` (7 fields) | `types.bal:19-34` | yes | field names/types/optionality-markers as noted in §5.2 |
| `Auth` (`userId`, `password`) | `types.bal:37-42` | yes | exact |
| `SecureSocket` (`sslKeyring`, `sslkeyringPassword?`, `sslCipherSuites?`) | `types.bal:45-52` | yes | exact |
| `EciRequest` (`programName`, `commArea?`, `commAreaSize?`, `timeout`) | `types.bal:55-64` | yes | `timeout` default lost (§5.2) |
| `Error` | `errors.bal:18` | **new only** | see above |
| `Client` | `client.bal:20` | yes | `public isolated` modifiers dropped (both sides) |
| `Client.init` | `client.bal:30` | yes | included-record param expanded (§5.3) |
| `Client.execute` | `client.bal:48` | yes | included-record param expanded (§5.3); return `byte[]\|Error\|()` ≡ source `byte[]\|Error?` |
| `Client.close` | `client.bal:60` | yes | `returns Error\|()` ≡ source `Error?` |

README: the render's README block contains `docs/Package.md` and `docs/modules/ibm.ctg/Module.md`
verbatim (verified by substring containment in the JSON `readme` field; both files are 81 lines /
1961 chars and are in fact identical to each other, which is why the render shows the Quickstart
twice). Nothing lost.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full `diff -u old new` — only the 2 hunks above; no deletions other than the placeholder line and
  the version-qualified type ref, both replaced by strictly better content.
- Declaration set extraction: identical apart from `+type Error`.
- Per-key JSON comparison: 6 of 8 top-level keys byte-identical; the 2 that differ are additive
  (`baseType` added) or a cleanup (unqualified type ref).
- README block (lines 7–175) is character-identical on both sides.
- All 4 record type defs including every doc comment and every field are character-identical.
- `execute` and `close` method blocks are character-identical.
- No `distinct`/doc/default was present in `old` and dropped in `new`.

## 5. Issues in `new` (independent of `old`)

All three are also present in `old` — listed here because they are inaccuracies a consuming LLM
would see in `new`, not because spec v2 introduced them.

**5.1 `distinct` and `public` dropped from the error type.**
Source `errors.bal:18`: `public type Error distinct error;`. Render: `type Error error;`. The JSON
carries `"baseType": "error"`, so the distinctness is lost at extraction, not at render time. Impact
is low (an LLM writing `ctg:Error` still gets valid code) but the render implies a non-distinct error
type. Note `public` is stripped from every type and from the class too, so that part is a uniform
renderer convention, not specific to `Error`.

**5.2 Record field defaults are lost and defaulted fields are re-marked optional.**
Three fields have defaults in source but are rendered as optional with no default:

| Field | Source | Render (both sides) |
|---|---|---|
| `ConnectionConfig.socketConnectTimeout` | `types.bal:27` — `int socketConnectTimeout = 15;` | `int socketConnectTimeout?;` |
| `ConnectionConfig.enableTrace` | `types.bal:33` — `boolean enableTrace = false;` | `boolean enableTrace?;` |
| `EciRequest.timeout` | `types.bal:63` — `int timeout = 10;` | `int timeout?;` |

Also, all four records are closed (`record {| … |}`) in source but rendered open (`record { … }`).
An LLM reading this render could add an unknown field to `EciRequest` and get a compile error.

**5.3 `Client.init` / `Client.execute` render as non-compiling Ballerina.**
Source uses included-record parameters:
`public isolated function init(*ConnectionConfig configs) returns Error?` (`client.bal:30`) and
`isolated remote function execute(*EciRequest request) returns byte[]|Error?` (`client.bal:48`).

The render flattens the included record into synthetic defaulted parameters and then still appends
the record parameter, without the `*`:

```
function init(string host = "", int port = 0, string cicsServer = "", int socketConnectTimeout = 15, Auth auth = {userId: "", password: ""}, SecureSocket secureSocket = {sslKeyring: ""}, boolean enableTrace = false, ConnectionConfig configs) returns Error?;
remote function execute(string programName = "", byte[] commArea = [], int commAreaSize = 0, int timeout = 0, EciRequest request) returns byte[]|Error|();
```

Two problems: (a) a required parameter (`configs` / `request`) after defaultable parameters is a
compile error in Ballerina; (b) the synthesised defaults (`host = ""`, `port = 0`, `timeout = 0`,
`auth = {userId: "", password: ""}`) do not exist in the library — `host`, `port`, `cicsServer` and
`auth` are **required** fields of `ConnectionConfig`, and `EciRequest.timeout` actually defaults to
`10`, not `0`. This is the most misleading part of the render and it is unchanged by spec v2.

**5.4 Doc comments for parameters and returns are dropped on client methods.**
Source `client.bal:28-29`, `46-47`, `59` carry `+ configs -`, `+ request -`, `+ return -` docs; the
render keeps only the description and the code-fence example, and drops `init`'s description
(`# Initialize the Ballerina IBM CTG client.`, `client.bal:22`) entirely. Both sides identical. The
`# ` blank continuation lines left behind (render lines 245, 252) are cosmetic noise.

## 6. Coverage gaps vs. the library

**Zero gaps.** `package.json` declares `"export": ["ibm.ctg"]` — a single module, which is also the
default module, so there is no submodule-only API and the `getDefaultModule()` limitation described
in the brief does not bite here.

Public symbols in `modules/ibm.ctg/*.bal`: `Error`, `ConnectionConfig`, `Auth`, `SecureSocket`,
`EciRequest`, `Client` (+ its `init`, `execute`, `close`). All 6 types/classes and all 3 methods
appear in `new`. `old` was missing `Error` (1 gap) — now closed.

Non-public symbols correctly absent from both renders: `init()` and `setModule()` (`init.bal:19,23`)
and `Client.externInit` (`client.bal:34`) — none are `public`, so their absence is correct, not a gap.

Central metadata confirms exactly one module (`ibm.ctg`) for `0.1.1`.

## 7. Compiler plugin

**No compiler plugin exists.** `find src -iname "*compiler*plugin*"` at tag `v0.1.1` returned
nothing; `ballerina/Ballerina.toml` has no `[[plugin]]` / `compilerPlugin` entry; the bala has no
`compiler-plugin/` directory. The Java side is a runtime native library only
(`native/src/main/java/io/ballerina/lib/ibm/ctg/`: `NativeClientAdaptor`, `ModuleUtils`,
`CommonUtils`, `ConnectionConfig`, `Auth`, `SecureSocket`, `IbmCtgThreadFactory`), surfaced through
`@java:Method` externs. Nothing plugin-derived is expected in the render, and nothing is missing.

## 8. Other considerations

- **Pre-1.0 / unstable.** `0.1.1` is a pre-release version; the API may change without semver
  guarantees. Central reports `pullCount: 38` and `deprecated: null` — not deprecated.
- **Provided-scope dependencies.** `package.json` lists `ctgclient`, `ccf2`, `cicsjee` at `scope:
  provided` — the connector cannot run without the user supplying IBM's proprietary jars. The README
  block in the render does document this (Step 2), so an LLM consuming the render will get it right.
- **Size / tokens.** 254 lines, of which 169 (66%) are the README — and the README content is
  duplicated because `Package.md` and `Module.md` are identical files (both 1961 chars, both
  embedded). Deduplicating would cut the render by roughly a third. This is identical in `old`, so
  not a regression, but it is the single largest token inefficiency here.
- **Doc typos carried through faithfully:** `# Represents a IBM CTG…` and, in the source Quickstart,
  `ctg:ConnectionConfig congig` — these are upstream, not render defects.
- **README/Quickstart vs. actual API mismatch (upstream bug, faithfully reproduced):** the README's
  Step 4 example shows `byte[]? outputPayload = ctg->execute(...)` without `check`, while `execute`
  returns `byte[]|Error?`. Present in both renders because it comes from `Package.md`.

## 9. Evidence log

| Check | Command / file:line | Result |
|---|---|---|
| Line counts | `wc -l old/*.bal.txt new/*.bal.txt` | old 253, new 254 |
| Full text diff | `diff -u old/ballerinax_ibm.ctg.bal.txt new/ballerinax_ibm.ctg.bal.txt` | 2 hunks, +3/−2, shown in §1 |
| Degraded types | `grep -c '^// Unknown type:'` | old 1, new 0 |
| Version-qualified refs | `grep -c 'ballerinax/ibm.ctg:0.1.1:'` | old 1, new 0 |
| Section markers | `grep -n '^// --- '` on new | 4: README (7), END README (175), Types (177), Client (234) |
| JSON top-level key comparison | python `json.dumps(..., sort_keys=True)` per key | `clients` DIFF, `typeDefs` DIFF; `annotations`/`description`/`functions`/`name`/`readme`/`services` SAME |
| JSON typeDef set | python, both files | both `{Auth, ConnectionConfig, EciRequest, Error, SecureSocket}`; only `Error` differs (`baseType: error` added in new) |
| JSON client diff | `difflib.unified_diff` on `clients` | single change: init return `ballerinax/ibm.ctg:0.1.1:Error?` → `Error?` |
| JSON empty collections | python | `functions []`, `services []`, `annotations []` in new |
| Bala layout | `ls -R …/ibm.ctg/0.1.1` | one module `ibm.ctg`; files `client.bal`, `errors.bal`, `init.bal`, `types.bal` (171 lines total) |
| Bala export list | `…/java17/package.json` | `"export": ["ibm.ctg"]` — single module, no submodules |
| Upstream tag resolution | `git ls-remote --tags <repo>` | `v0.1.1` → `8d4a2222b546f416e6b115694f2611ec42cc59dd` |
| Clone | `git clone --depth 1 --branch v0.1.1 <repo> src` | success |
| Upstream vs bala source | `diff bala/modules/ibm.ctg/X.bal src/ballerina/X.bal` for all 4 files | identical (no output) for all 4 |
| Error type source | `src/ballerina/errors.bal:17-18` | `# Represents a IBM CTG distinct error.` / `public type Error distinct error;` |
| Client init source | `src/ballerina/client.bal:30` | `public isolated function init(*ConnectionConfig configs) returns Error?` |
| Client execute source | `src/ballerina/client.bal:48` | `isolated remote function execute(*EciRequest request) returns byte[]\|Error?` |
| Client close source | `src/ballerina/client.bal:60` | `isolated remote function close() returns Error?` |
| Record defaults | `src/ballerina/types.bal:27,33,63` | `= 15`, `= false`, `= 10` — none appear in either render |
| Compiler plugin search | `find src -iname "*compiler*plugin*"`; `grep -n 'compilerPlugin\|\[plugin\]' src/ballerina/Ballerina.toml` | no matches — no plugin |
| Native classes | `ls src/native/src/main/java/io/ballerina/lib/ibm/ctg` | 7 runtime classes, no plugin classes |
| README containment | python substring test of `Package.md` and `Module.md` against JSON `readme` | both `True`; readme 3944 chars = 2 × 1961 + separator |
| Central metadata | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerinax/ibm.ctg/0.1.1` | `deprecated: None`, 1 module, `pullCount 38`, `ballerinaVersion 2201.10.0` |
| Precomputed diff cross-check | `OLD_AND_NEW_DIFFS/ibm.ctg_diff.md` | its figures (253/254, +3/−2, 2 hunks, 1→0 unknown, 1→0 qualified refs, `+type Error`) all reproduce from my own commands |

## 10. Caveats and unverified items

- The renders were not compiled. Claims about non-compiling syntax in §5.3 (required parameter after
  defaultable parameters) are from reading the Ballerina spec rules, not from running `bal build` on
  the render — the render is a stub-only listing (method bodies replaced by `;`) and would not
  compile as-is regardless, so a compile test would not be meaningful.
- I did not independently rebuild the renders from the two `ballerina-vscode` commits; I audited the
  provided artifacts and the library sources. The commit/branch attribution in the brief
  (`eb5d81b3` for `old`, `412ba01e` for `new`) is taken as given.
- The synthetic parameter defaults in §5.3 (`host = ""`, `port = 0`, etc.) are clearly not from the
  library source, but I did not trace which extractor stage invents them — attributing that to a
  specific code path is unverified.

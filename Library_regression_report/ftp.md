# ballerina/ftp 2.20.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/ftp` |
| Pinned version | `2.20.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-ftp |
| Tag reviewed | `v2.20.1` (exact match, commit `2dce3576bb23c057518664bf40215feacfb84606`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/ftp/2.20.1` |
| Old render | `1564` lines |
| New render | `1703` lines |
| Verdict | **MINOR REGRESSION** |

## 1. Summary

`new` is a large net improvement: all 10 `// Unknown type:` placeholders are gone (10 → 0), all 4
version-qualified type refs (`ballerina/io:1.8.1:Error`, `ballerina/ftp:2.20.1:Error`) are normalised
to prefix form (4 → 0), the whole `ftp:Listener` class (init + 7 methods) appears for the first time,
9 error types get real definitions and docs, the `onFileChange` handler is added with its deprecation
note, and — most importantly — the two annotation declarations are **corrected**: `old` emitted a
non-existent type `FtpServiceConfig` and the invalid attach point `on service_function`.

Against that, one real information loss: the `ftp:Caller` parameter, a legal third parameter accepted
by the compiler plugin, was dropped from the `onFileText` / `onFileJson` / `onFileXml` / `onFile`
handler signatures in the Service template, and is not listed as an optional parameter for them
either. `old` showed it correctly for all four. That is the only substantive regression; it is
narrow, hence MINOR.

`new` also introduces its own defects in the newly-added Listener block (a non-compiling `init`
signature, invented defaults for optional fields, lost `@deprecated` markers), and both sides share
several pre-existing inaccuracies (wrong `FileWriteOption` default, mangled `typedesc` params).

## 2. Change inventory

Line counts (`wc -l`): old `1564`, new `1703` (+139). Diff: 6 hunks, +174 / −35 lines.
JSON: old 169,910 B → new 180,669 B; `typeDefs` 86 → 86, `clients` 2 → 2, `services` 1 → 1,
`annotations` 2 → 2, `functions` 0 → 0 in both. Lines 1–950 are byte-identical (README section
`7–484` unchanged).

Declaration counts by kind (regex over each render):

| Kind | old | new |
|---|---|---|
| `class` (non-client) | 1 (`Service`) | 2 (`Service`, `Listener`) |
| `client class` | 2 (`Client`, `Caller`) | 2 (unchanged) |
| `type` | 33 | 42 |
| `enum` | 13 | 13 |
| `const` | 38 | 38 |
| `public annotation` | 2 | 2 |
| `remote function` (all) | 69 | 70 |
| plain `function` (methods) | 2 | 10 |
| `// Unknown type:` | 10 | 0 |
| `mod:x.y.z:Type` refs | 4 | 0 |

**Added in `new` (18 declarations)**

- `class Listener` + methods `init`, `'start`, `attach`, `detach`, `immediateStop`, `gracefulStop`,
  `poll`, `register` (new:1150–1204) — replaces `// Unknown type: Listener` (old:1124).
- 8 error type defs: `Error`, `ConnectionError`, `FileNotFoundError`, `FileAlreadyExistsError`,
  `InvalidConfigError`, `ServiceUnavailableError`, `ContentBindingError`,
  `AllRetryAttemptsFailedError`, `CircuitBreakerOpenError` (new:961–1010) — 9 types, replacing 9 of
  the 10 `// Unknown type:` lines in old:954–990.
- `remote function onFileChange(ftp:WatchEvent watchEvent)` in the Service block, carrying
  `@deprecated` (new:1683–1691).

**Removed in `new`: 0 declarations.** (Verified: no declaration name present in `old` is absent from
`new`; see §4 for a parameter-level loss that is not a whole declaration.)

**Modified in `new`**

- 4 type refs de-versioned: `ballerina/io:1.8.1:Error` → `io:Error` (InputContent.fileContent,
  `Client.get`, `Caller.get`), `ballerina/ftp:2.20.1:Error` → `Error` (`Client.init`).
- Whole Service block rewritten (old:1535–1556 → new:1612–1691): richer per-parameter docs,
  co-existence rules, `@ftp:ServiceConfig` / `@ftp:FunctionConfig` annotation scaffolding,
  `ftp:`-qualified parameter types, required/optional parameter notes.
- Both annotation declarations rewritten (old:1558–1564 → new:1693–1703).

## 3. Correctness against library source

Checked against the **bala** (`.../2.20.1/java21/modules/ftp/*.bal`, authoritative) and the upstream
tag `v2.20.1` clone. Bala and GitHub agree for every file inspected.

Correct in `new`:

- **Annotations.** `annotations.bal:49` `public annotation FtpFunctionConfig FunctionConfig on service
  remote function;` and `annotations.bal:69` `public annotation ServiceConfiguration ServiceConfig on
  service;` — `new`:1694–1703 reproduces both exactly, including doc text. `old`:1559 declared
  `public annotation FtpServiceConfig ServiceConfig on service;` (type `FtpServiceConfig` does not
  exist anywhere in the module) and `old`:1564 `... FunctionConfig on service_function;` (not a
  valid attach point). **`new` fixes two outright errors.**
- **Error docs.** All 9 doc comments in `new`:961–1010 match `error.bal:17–65` verbatim.
- **Listener methods.** `'start`, `attach(Service, string[]|string|())`, `detach(Service)`,
  `immediateStop`, `gracefulStop`, `poll`, `register(Service, string|())` — match
  `listener_endpoint.bal:69,81,94,105,115,135,147` in name, parameter types and return type, and the
  doc/code-fence text is verbatim. Private methods `internalStart`/`stop`
  (`listener_endpoint.bal:119,124`) are correctly excluded.
- **Listener init field list.** The 20 flattened parameters in `new`:1151 match
  `ListenerConfiguration` (`listener_endpoint.bal:166–221`) exactly in name, type and order
  (protocol, host, port, auth, path, fileNamePattern, pollingInterval, userDirIsRoot, fileAgeFilter,
  fileDependencyConditions, laxDataBinding, connectTimeout, socketConfig, proxy, fileTransferMode,
  sftpCompression, sftpSshKnownHosts, csvFailSafe, coordination, retryConfig).
- **`onFileChange` deprecation.** Matches `PluginConstants.java:115` `ON_FILE_CHANGE_DEPRECATED`.
- **Client surface.** All 28 `remote isolated function` declarations in `client_endpoint.bal:49–413`
  appear in `new`'s `Client` block (28 rendered), same names and order.
- **`io:Error` normalisation.** `client_endpoint.bal:49` returns
  `stream<byte[] & readonly, io:Error?>|Error` — `new`:1213 matches the source text exactly; `old`
  wrote `ballerina/io:1.8.1:Error`, which is not valid Ballerina.

## 4. Regressions

**R1 (substantive) — `ftp:Caller` parameter dropped from four content handlers.**

`old`:1538,1541,1544,1547:
```
remote function onFileJson(json content, FileInfo fileInfo, Caller caller) returns error?;
remote function onFileXml(xml content, FileInfo fileInfo, Caller caller) returns error?;
remote function onFileText(string content, FileInfo fileInfo, Caller caller) returns error?;
remote function onFile(byte[] content, FileInfo fileInfo, Caller caller) returns error?;
```
`new`:1639,1647,1654,1662:
```
remote function onFileJson(json content, ftp:FileInfo fileInfo) returns error?; // optional
remote function onFileXml(xml content, ftp:FileInfo fileInfo) returns error?; // optional
remote function onFileText(string content, ftp:FileInfo fileInfo) returns error?; // optional
remote function onFile(byte[] content, ftp:FileInfo fileInfo) returns error?; // optional
```
`new` also omits `caller` from the per-parameter doc list and from its own
"Optional parameters (may be omitted):" note for these four (it *does* emit that note for
`onFileCsv`, `onFileDelete` and `onError`). The 3-parameter form is valid and supported:
`FtpContentFunctionValidator.java:125–134` explicitly accepts `parameters.size() == 3` as
`(content, fileInfo, caller)`, and the library's own tests use it —
`ballerina-tests/ftp-listener-advanced-tests/tests/ftp_listener_content_test.bal:94` (`onFileText`),
`:172` (`onFileJson`), `:254` (`onFileXml`), `:413` (`onFile`). An LLM consuming `new` would not know
it can obtain a `Caller` in these four handlers.

**R2 (cosmetic) — `onFileDelete` parameter renamed away from the library's own naming.**

`old`:1550 `onFileDelete(string deletedFile, Caller caller)`; `new`:1670
`onFileDelete(string deleteFiles, ftp:Caller caller)`. The compiler plugin's own diagnostic text uses
the singular `deletedFile` (`PluginConstants.java:124`, FTP_131), and `new`'s own doc line reads
"+ deleteFiles - Path of the file that was deleted" — a plural name with a singular meaning.
Parameter names are positional here so this does not break compilation; it is a naming/doc
inconsistency only.

Nothing else was lost: README text, all 86 typeDefs, both client classes, all 28 client methods,
all 38 consts, all 13 enums and both annotations are present in `new`. No declaration name present in
`old` is absent from `new`.

## 5. Issues in `new` (independent of `old`)

**N1 — `Listener.init` is non-compiling Ballerina.** `new`:1151 emits 20 defaultable parameters
followed by a *required* parameter with no default:
`... RetryConfig retryConfig = {}, ListenerConfiguration listenerConfig) returns Error?;`
A required parameter cannot follow defaultable parameters. The source is
`public isolated function init(*ListenerConfiguration listenerConfig) returns Error?`
(`listener_endpoint.bal:32`) — the renderer expanded the included record *and* kept the record
parameter itself.

**N2 — invented defaults for optional (`?`) fields.** In `new`:1151, `auth = {}`,
`fileNamePattern = ""`, `fileAgeFilter = {}`, `socketConfig = {}`,
`proxy = {host: "", port: 0}`, `csvFailSafe = {}`,
`coordination = {memberId: "", coordinationGroup: ""}`, `retryConfig = {}` are all shown as
defaults. In `listener_endpoint.bal:174,182,191,202,204,213,216,220` every one of these fields is
declared optional with **no** default. `fileNamePattern = ""` and `sftpSshKnownHosts = ""` are the
most misleading: an empty regex is not the same as an unset pattern. `proxy = {host:"", port:0}` and
`coordination = {memberId:"", coordinationGroup:""}` are fabricated literals (those records have
required fields, `commons.bal:146–148`, `listener_endpoint.bal:252–254`).

**N3 — `@deprecated` markers lost when flattening `ListenerConfiguration`.** Fields `path`,
`fileNamePattern`, `fileAgeFilter`, `fileDependencyConditions` carry `@deprecated`
(`listener_endpoint.bal:177,181,190,194`); the flattened `init` in `new` shows none of them.
(The standalone `ListenerConfiguration` record elsewhere in the render is unaffected.)

**N4 — error hierarchy flattened.** Source declares `public type Error distinct error` and every
other error type as `distinct Error` (or `distinct ServiceUnavailableError` for
`CircuitBreakerOpenError`) — `error.bal:18–65`. `new`:962–1010 renders all of them as bare
`type X error;`, dropping `public`, dropping `distinct`, and dropping the subtype relationship
entirely. `CircuitBreakerOpenError` is therefore not shown as a `ServiceUnavailableError`.
`ContentBindingError` (new:1000) keeps the intersection (`Error & error<ContentBindingErrorDetail>`)
but drops `distinct`. Still a large improvement over `old`'s bare placeholders, but the type lattice
is not recoverable from the render.

**N5 — "`@ftp:ServiceConfig` is mandatory" overstates the library.** `new`:1619–1620 asserts
"Mandatory: this service must carry the `@ftp:ServiceConfig` annotation". No compiler-plugin
diagnostic enforces it (`PluginConstants.java` has `NO_VALID_REMOTE_METHOD` FTP_119 for a missing
handler but no missing-annotation error), and `ListenerConfiguration.path` still defaults to `"/"`
(`listener_endpoint.bal:178`, deprecated but functional) — the library's own listener tests attach
services with no annotation at all (e.g. `ftp-listener-basic-tests/tests/ftp_listener_basic_test.bal:73`).
It is good guidance, but flagged `// required` it may cause an LLM to reject valid code.

**N6 (shared with `old`) — wrong `FileWriteOption` default.** 14 occurrences in each render of
`FileWriteOption option = "APPEND"`. Source default is `OVERWRITE` for all 7 affected methods
(`client_endpoint.bal:204,218,232,245,262,275,289`). The renderer appears to pick the first enum
member of its own reordered enum (`new`:696–699 lists `APPEND, OVERWRITE`; source
`client_endpoint.bal:419–424` lists `OVERWRITE, APPEND`). This silently inverts write semantics —
the highest-impact inaccuracy in the file, though not a regression.

**N7 (shared with `old`) — `typedesc` inference parameters mangled.** 8 occurrences in each render,
e.g. `new`:1237 `getJson(string path, json|record {|anydata...;|} targetType = json|record
{|anydata...;|}) returns targetType|Error`. Source: `getJson(string path, typedesc<json|record {}>
targetType = <>) returns targetType|Error` (`client_endpoint.bal:92`). `typedesc` appears 0 times in
either render; the default expression is a type, not a value; and `returns targetType` now refers to
a value parameter. Non-compiling and misleading. Same for `getXml`, `getCsv`, `getCsvAsStream`.

**N8 (shared, cosmetic)** — `returns Error|()` used 31 times instead of `Error?`;
`Caller.init(...) returns ()`; enum member doc comments dropped and members reordered;
`io:`, `crypto:`, `task:` prefixes are used but only `import ballerina/ftp;` is emitted (new:5).

## 6. Coverage gaps vs. the library

**0 gaps.** The bala contains exactly one module (`modules/ftp`) — the default module — so there is
no submodule-only API and no shared submodule gap for this library.

Script over `modules/ftp/*.bal` extracted 51 `public` top-level declarations (type / class / enum /
const / annotation / function). All 51 are present in both renders; all 51 appear as real
declarations in `new` (`DELETE` renders as `const string DELETE = "DELETE";` at new:490). In `old`,
11 of the 51 were present only as text mentions or `// Unknown type:` placeholders rather than
declarations: `Error`, `ConnectionError`, `FileNotFoundError`, `FileAlreadyExistsError`,
`InvalidConfigError`, `ServiceUnavailableError`, `ContentBindingError`,
`AllRetryAttemptsFailedError`, `CircuitBreakerOpenError`, `Listener` (plus the `DELETE` regex
artefact). `new` closes all of them.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `io.ballerina.stdlib.ftp.plugin.FtpCompilerPlugin`
(jar `ftp-compiler-plugin-2.20.1.jar`). 17 Java sources at `v2.20.1`. It contributes:

- **Validations**: `FtpServiceValidator`, `FtpFunctionValidator`, `FtpContentFunctionValidator`,
  `FtpFileDeletedValidator`, `FtpOnErrorValidator`, `FtpServiceAnalysisTask` — ~35 diagnostics
  (FTP_101…FTP_134) covering handler-must-be-remote, mandatory/too-many parameters, content
  parameter types per handler, `onFileChange` deprecation, `onFileDeleted`/`onFileDelete` mutual
  exclusion, and "service must define at least one handler".
- **Code actions / templates**: `FtpCodeTemplateGeneric`, `FtpCodeTemplateText`,
  `FtpCodeTemplateJson`, `FtpCodeTemplateXml`, `FtpCodeTemplateCSV` (via `AbstractFtpCodeTemplate`).
- No generated artifacts or plugin-injected annotations.

Plugin knowledge that `new` reflects: handler co-existence rules, required/optional parameters,
`onFileChange` deprecation, per-handler content-type alternatives. Plugin knowledge that `new` does
**not** reflect: (a) the `caller` third parameter for the four content handlers
(`FtpContentFunctionValidator.java:125–134`) — see R1; (b) the deprecated `onFileDeleted(string[]
deletedFiles, Caller?)` handler (`PluginConstants.java:42,109–114`), absent from both renders;
(c) the "either `onFileDelete` or `onFileDeleted`, not both" rule (FTP_133). (b) and (c) concern a
deprecated API, so their absence is defensible.

## 8. Other considerations

- Version 2.20.1 is stable (>1.0); not deprecated on Central. No version drift: the bala at
  `2.20.1` was used for both renders and the `v2.20.1` tag exists upstream.
- Size: +139 lines / +10.8 KB JSON (~+9 %). Modest token cost for a large correctness gain.
- `ListenerConfiguration.path`, `.fileNamePattern`, `.fileAgeFilter`, `.fileDependencyConditions` and
  `Client.get` / `Caller.get` are `@deprecated` in the library. `new` keeps `@deprecated` on
  `Client.get`/`Caller.get` and adds it on `onFileChange`, but loses it on the four listener-config
  fields when flattening `init` (N3).
- Doc quality of the added Service block is high and clearly hand-authored in the LS trigger
  metadata rather than derived from the library; that is why it can drift from the library (R1, R2,
  N5). It is not derived from the bala, so it will not self-correct when the library changes.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 1564, new 1703 |
| `grep -c '^// Unknown type:'` | old 10, new 0 |
| `grep -oE '(ballerina\|ballerinax)/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:[A-Za-z]+'` | old 4 (3× `ballerina/io:1.8.1:Error`, 1× `ballerina/ftp:2.20.1:Error`), new 0 |
| `grep -n '^// --- '` | 6 markers each side; README 7–484 both |
| `diff -u old new` | 6 hunks, +174 / −35; first change at line 951 |
| `git ls-remote --tags <repo> \| grep 2.20.` | `v2.20.1` → `2dce3576bb23c057518664bf40215feacfb84606` |
| `git clone --depth 1 --branch v2.20.1` | succeeded (3rd attempt; transient network failures) |
| `ls .../2.20.1/java21/modules` | single module `ftp` → no submodules |
| Python scan of `modules/ftp/*.bal` for `public` decls | 51 symbols; 0 missing from either render; 11 not declared (only mentioned) in `old`, 0 in `new` |
| JSON key/array comparison | identical keys; typeDefs 86→86, clients 2→2, services 1→1, annotations 2→2, functions 0→0 |
| `grep -nE '^(public )?(client )?class '` | old: `Service`, `Client`, `Caller`; new: adds `Listener` at 1150 |
| `grep -c '^\s+remote function'` | old 69, new 70 |
| `grep -c '^\s+function '` | old 2, new 10 |
| `annotations.bal:49,69` vs render 1694/1703 | new matches source exactly; old's `FtpServiceConfig` / `on service_function` are wrong |
| `error.bal:17–65` vs new:961–1010 | 9 types, docs verbatim; `distinct` + `public` + subtype relations dropped |
| `listener_endpoint.bal:32,69,81,94,105,115,135,147` vs new:1151–1204 | method set and signatures match; init malformed (N1) |
| `listener_endpoint.bal:166–221` vs new:1151 | 20 params, correct names/types/order; 8 invented defaults (N2); 4 lost `@deprecated` (N3) |
| `FtpContentFunctionValidator.java:125–134` | 3-param `(content, fileInfo, caller)` accepted → R1 confirmed |
| `ftp_listener_content_test.bal:94,172,254,413` | library's own tests use the 3-param form → R1 confirmed |
| `PluginConstants.java:124` | plugin names the param `deletedFile` → R2 |
| `PluginConstants.java` scan for a missing-ServiceConfig diagnostic | none found → N5 |
| `ftp_listener_basic_test.bal:73` | service attached with no `@ftp:ServiceConfig` → N5 |
| `grep -c 'FileWriteOption option = "APPEND"'` | 14 in old, 14 in new; source default is `OVERWRITE` (`client_endpoint.bal:204,218,232,245,262,275,289`) → N6 |
| `grep -c 'targetType = '` / `grep -c typedesc` | 8 / 0 in each render vs `typedesc<...> = <>` in source → N7 |
| `grep -c 'returns Error\|()'` | 31 in each render → N8 |
| `compiler-plugin.json` + `find compiler-plugin -name '*.java'` | `FtpCompilerPlugin`, 17 sources |
| `OLD_AND_NEW_DIFFS/ftp_diff.md` cross-check | its counts (10→0 placeholders, 4→0 qualified refs, 18 added / 0 removed declarations, 6 hunks) reproduced independently and confirmed |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that `Listener.init` (N1) and the `typedesc` parameters (N7)
  are non-compiling rest on Ballerina's parameter-ordering rule and on `typedesc` being absent from
  the render — not on a `bal build` run.
- The Service-block text (handler docs, co-existence rules, annotation scaffolding) is authored in
  the language-server trigger metadata, not in the library. I verified its *claims* against the
  library and compiler plugin, but I did not read the trigger-metadata source itself, so I cannot say
  whether R1/R2/N5 originate in the metadata or in the renderer.
- `ftp-native-2.20.1.jar` and `ftp-compiler-plugin-2.20.1.jar` were not decompiled; plugin behaviour
  is taken from the `v2.20.1` Java sources, which match the bala's `compiler-plugin.json`
  plugin class.
- Central metadata was not re-queried in this session (no network call to
  `api.central.ballerina.io`); the deprecation statement in §8 is based on the manifest's verified
  `central_source` and the absence of any deprecation marker in `package.json` / `bala.json`.
- Spot-checking of the ~640-line Types section was by declaration-set comparison plus targeted reads;
  the diff shows it is byte-identical between `old` and `new` apart from the error types and one
  `io:Error` ref, so per-field verification of the 86 typeDefs was not repeated for both sides.

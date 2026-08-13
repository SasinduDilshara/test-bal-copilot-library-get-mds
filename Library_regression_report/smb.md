# ballerina/smb 2.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/smb` |
| Pinned version | `2.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-smb |
| Tag reviewed | `v2.0.1` (exact tag, commit `f985f0e`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/smb/2.0.1/java21` |
| Old render | `973` lines |
| New render | `1148` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. All 5 `// Unknown type:` placeholders in `old`
(`Error`, `ContentByteStream`, `ContentCsvRecordStream`, `ContentCsvStringArrayStream`, `Listener`) are
replaced by real definitions, two annotation declarations and a full `// --- Service ---` guidance block
appear for the first time, and the one version-qualified type reference (`ballerina/smb:2.0.1:Error?`)
is normalised to `Error?`. Nothing present in `old` is dropped, truncated, or degraded: the diff is
4 hunks, +181 / −6 lines, and every one of the 6 removed lines is either a placeholder comment or the
version-qualified `init` line.

The newly rendered content is mostly accurate against the library source, with four defects that are
new-side only because the content itself is new (§5), the most significant being the flattened
`Listener.init` signature, which is not valid Ballerina.

## 2. Change inventory

Mechanical figures (all from commands in §9):

| Signal | old | new |
|---|---|---|
| Lines | 973 | 1148 |
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (`org/mod:ver:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 (README, END README, Types, Client) | 6 (+ Service, Annotations) |
| Diff | 4 hunks, +181 / −6 | |
| Non-ASCII lines (README em-dashes) | 8 | 8 |

**Removed declarations: 0.** (`diff` shows no `-` line that carries a declaration; the 6 removed lines
are the 5 placeholder comments and the old `Client.init` line, which is re-emitted in modified form.)

**Added declarations (8 top-level + 24 members):**

| Kind | Name | Members added |
|---|---|---|
| type (error) | `Error` | — |
| class | `ContentByteStream` | `init`, `next`, `close` |
| class | `ContentCsvRecordStream` | `init`, `next`, `close` |
| class | `ContentCsvStringArrayStream` | `init`, `next`, `close` |
| class | `Listener` | `init`, `'start`, `attach`, `detach`, `immediateStop`, `gracefulStop`, `poll`, `register` |
| service block | `service smb:Service on new smb:Listener(...)` | `onFileText`, `onFileJson`, `onFileXml`, `onFileCsv`, `onFile`, `onFileDelete`, `onError` |
| annotation | `FunctionConfig` | — |
| annotation | `ServiceConfig` | — |

Class member functions added: 17. Service remote methods added: 7.

**Modified declarations: 1.**
`Client.init` — `returns ballerina/smb:2.0.1:Error?` (old) → `returns Error?` (new). Improvement; the old
form is not valid Ballerina and would confuse a consumer.

**Unchanged:** README block (lines 1–296 byte-identical), all 34 `typeDefs` names, both client classes
(`Caller`, `Client`) with their 26 remote methods each. JSON-level diff confirms this: the only
`typeDefs` entries that differ are the same 5 (`Error` gains `baseType: "error"`; the 4 object types gain
`type: "Class"`), plus one `Error?` string in `clients`; `services` went `0 → 1` and `annotations`
`0 → 2`.

## 3. Correctness against library source

Checked against the bala (authoritative) at
`…/2.0.1/java21/modules/smb/*.bal`; the GitHub clone at `v2.0.1` matches.

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `type Error error;` | `error.bal:18` `public type Error distinct error;` | present, but loses `distinct` (§5.3) |
| `ContentByteStream.next() returns record {\|byte[] value;\|}\|error?` | `content_byte_stream.bal:34-36` | exact |
| `ContentByteStream.close() returns error?` | `content_byte_stream.bal:44` | exact |
| `ContentCsvRecordStream.next() returns record {\|record {\|anydata...;\|} value;\|}\|error?` | `content_csv_record_stream.bal` (`record {} value`) | matches modulo the renderer's `record {}` → `record {\|anydata...;\|}` normalisation |
| `Listener.'start/attach/detach/immediateStop/gracefulStop/poll/register` | `listener_endpoint.bal:51,68,88,98,106,114,138,150` | all 7 exist, params and return types match (`attach(Service, string[]\|string? name = ())`, `register(Service, string? name)`) |
| `Listener` non-public members `internalStart`, `stop` | `listener_endpoint.bal:92,98` | correctly excluded |
| `public annotation FunctionConfiguration FunctionConfig on service remote function;` | `types.bal:163` | exact |
| `public annotation SmbServiceConfig ServiceConfig on service;` | `types.bal:173` | exact |
| Service handler set `onFile, onFileText, onFileJson, onFileXml, onFileCsv, onFileDelete, onError` | `compiler-plugin/.../PluginConstants.java:34-43` | exact, no invented handler |
| `onFileText(string content, …)` | `SmbContentFunctionValidator.java:143` (`typeKind == STRING`) | correct |
| `onFileJson(json content …)`, "`content` may bind directly to: record {}" | `SmbContentFunctionValidator.java:144` (`JSON \|\| RECORD \|\| isRecordTypeReference`) | correct |
| `onFileXml(xml content …)`, "may bind directly to: record {}" | `…:145` | correct |
| `onFileCsv(string[][] content …)`, alternatives `record {}[]`, `stream<string[], error?>`, `stream<record {}, error?>` | `…:250-251` expected-type message | correct, all four forms |
| `onFile(byte[] content …)`, alternative `stream<byte[], error?>` | `…:246` | correct |
| `onFileDelete(string path, smb:Caller caller)` | `PluginConstants.java` SMB_121/SMB_122 | correct |
| `onError(smb:Error err, smb:Caller caller)` | SMB_131/SMB_132 | correct |
| "at least one `onFile*` or `onFileDelete` required, `onError` alone does not count" | SMB_103 `NO_VALID_REMOTE_METHOD` | correct |
| `Caller`/`Client` 26 remote methods each | `caller.bal`, `client.bal` | names match one-for-one, no invented method |
| `time:Utc modifiedAt/createdAt/accessedAt/writtenAt` with `// Special Agent Note: Utc FROM ballerina/time package` | `types.bal:90-93` | cross-package type resolved correctly in both renders |

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full unified `diff old new` (218 lines, 4 hunks) read end to end — every `-` line is a
  `// Unknown type:` placeholder or the version-qualified `Client.init` line.
- Declaration set extracted from both files with the same regex: `new` is a strict superset of `old`
  (old 43 top-level matches, new 51; no name present in `old` is absent from `new`).
- JSON-level comparison: `name`, `description`, `readme`, `functions` identical; `typeDefs` name-set
  identical (34/34); the only per-entry deltas are additive (`baseType`, `type: "Class"`) or a
  normalisation (`ballerina/smb:2.0.1:Error?` → `Error?`).
- README block (296 lines) diffed separately: identical, and byte-length-identical to the bala's
  `docs/README.md` (10,715 chars both).
- `Caller` and `Client` bodies: unchanged between sides (no hunk touches lines 574–770 / 661–857
  except the one `init` line); the 14 `FileWriteOption option = "APPEND"` occurrences are present in
  both files, so the wrong default is pre-existing, not a regression.

## 5. Issues in `new` (independent of `old`)

Ordered by impact. Items 1–4 are in content that only `new` emits; items 5–9 are present in both files
and therefore also ship in `new`.

1. **`Listener.init` renders a signature that will not compile.** `new:606`:
   `function init(string host = "localhost", …, FailSafeOptions csvFailSafe = {}, ListenerConfiguration listenerConfig) returns Error?;`
   The source is `public isolated function init(*ListenerConfiguration listenerConfig) returns Error?`
   (`listener_endpoint.bal:44`). The renderer flattens the included-record parameter into its 14 fields
   **and** keeps the record parameter itself, emitting a required parameter after defaultable ones —
   invalid in Ballerina, and duplicated information. Root cause is in the JSON, not the renderer: the
   `listenerConfig` parameter carries `"optional": true` with no `default`, and the same parameter list
   appears identically in the `old` JSON (it was simply never rendered).
2. **Invented defaults in that flattened list.** `auth = {}`, `fileNamePattern = ""` and
   `csvFailSafe = {}` are rendered as defaulted, but `types.bal:122,124,133` declare them as optional
   fields (`auth?`, `fileNamePattern?`, `csvFailSafe?`) with no default. `share = ""` and the other
   defaults are correct.
3. **`type Error error;` drops `distinct` and `public`.** Source is `public type Error distinct error;`
   (`error.bal:18`). `smb:Error` is a distinct error type used in every client return type and in the
   `onError` handler contract; rendering it as a plain `error` alias loses the nominal distinction.
   No `public` qualifier is emitted on any type in either render, so that part is a global convention,
   not smb-specific.
4. **Class documentation lost or wrong on the newly rendered classes.**
   `ContentByteStream`, `ContentCsvRecordStream` and `ContentCsvStringArrayStream` render with no doc
   comment at all, though the source carries one (e.g. `content_csv_string_stream.bal:19-20`
   "Stream for reading CSV content row by row from an SMB share."). `Listener` renders with
   `# Gets invoked during object initialization.` — the doc of `init`, not the class doc
   ("Listener for monitoring SMB servers and triggering service functions when files are added or
   deleted.", `listener_endpoint.bal:19`). The empty/incorrect descriptions are already in the JSON on
   **both** sides, so this is an extractor gap that only becomes visible in `new`.
5. **Wrong enum default on all `put*` methods (shared with `old`, 14 occurrences each).**
   Rendered `FileWriteOption option = "APPEND"`; source is `FileWriteOption option = OVERWRITE`
   (`client.bal:49,78,93,108,142,157,173`; `caller.bal:37,65,80,95,113,183,199`). An LLM reading the
   render will believe appends are the default, which is the opposite of the real behaviour. This is
   the most consequential inaccuracy in the file and it is unchanged by spec v2.
6. **`typedesc` parameters render as non-compiling type-as-value defaults (shared).**
   e.g. `new:968` `getCsv(string path, string[][]|record {|anydata...;|}[] targetType = string[][]|record {|anydata...;|}[])`;
   source is `getCsv(string path, typedesc<string[][]|record {}[]> targetType = <>)` (`client.bal:242`).
   Same for `getJson`, `getXml`, `getCsvAsStream`. Identical in `old` (lines 861, 871, 881, 895).
7. **Record field defaults dropped and required-with-default fields shown as optional (shared).**
   `ClientConfiguration.host`/`port`/`dialects`/… render as `string host?;` etc., losing
   `= "localhost"`, `= 445`, the dialect list, `= 65536`, `= 30.0`. `Move.preserveSubDirs` loses
   `= true` (`types.bal:146`). Closed records `record {| |}` render as open `record { }` throughout.
8. **`type MOVE Move;` is flattened into a duplicate record body (shared)** — `new:511` renders
   `type MOVE record { string moveTo; boolean preserveSubDirs?; }`, hiding that `MOVE` is an alias
   (`types.bal:149`). Also `FunctionConfiguration.afterProcess` renders as `MOVE|"DELETE"` where the
   source is `MOVE|DELETE` (a const reference) — readable but not the source form.
9. **`public type Service service object {}` renders as `class Service { }` (shared)** — the
   service-object contract is represented as an empty class.
10. **Editorial: the Service block marks both annotations "required".** `@smb:ServiceConfig {...} // required`
    and `@smb:FunctionConfig {...} // required` on every handler. The compiler plugin does **not**
    validate or require either annotation — `grep -rni 'annot'` across all 9 plugin classes returns no
    annotation handling, and `SmbServiceConfig.path` is documented as defaulting to the service name
    (`types.bal:166`). This comes from the LS-side service metadata (`"presence": "required"` in the
    `services` block of the new JSON), so it is prescriptive guidance rather than a library fact.
    Worth knowing, but not an error in the library rendering.

## 6. Coverage gaps vs. the library

**`new`: 0 gaps.** The bala's default (and only) module `smb` exports 28 public symbols; all 28 appear
in `new`:

`AuthConfiguration, Caller, Client, ClientConfiguration, ContentByteStream, ContentCsvRecordStream,
ContentCsvRecordStreamEntry, ContentCsvStringArrayStream, ContentCsvStringArrayStreamEntry,
ContentStreamEntry, Credentials, DELETE, Dialect, Error, ErrorLogContentType, FailSafeOptions,
FileInfo, FileWriteOption, FunctionConfig, FunctionConfiguration, KerberosConfig, Listener,
ListenerConfiguration, MOVE, Move, Service, ServiceConfig, SmbServiceConfig`

**`old`: 7 gaps** — `Error`, `ContentByteStream`, `ContentCsvRecordStream`, `ContentCsvStringArrayStream`
and `Listener` present only as `// Unknown type:` comments (no members, no signatures), and the
`FunctionConfig` / `ServiceConfig` annotations absent entirely.

**Submodules:** none. `package.json` declares `"export": ["smb"]` and `modules/` contains only `smb`,
so the `getDefaultModule()`-only extraction loses nothing for this library.

## 7. Compiler plugin

`has_plugin: true`, confirmed in the bala:
`compiler-plugin/compiler-plugin.json` → `plugin_class: io.ballerina.lib.smb.plugin.SmbCompilerPlugin`,
`compiler-plugin/libs/smb-compiler-plugin-2.0.1.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/lib/smb/plugin/`, 9 classes) is a **code analyzer
only** — `SmbCodeAnalyzer` registers `SmbServiceAnalysisTask` on service declarations; there are no code
actions, no code modifiers, no generated artifacts. What it enforces:

- Allowed remote method names only (`SMB_101`); no resource methods (`SMB_102`); at least one
  `onFile*` or `onFileDelete` (`SMB_103`).
- Content-handler rules (`SMB_110`–`SMB_116`): `remote` keyword required, content parameter type per
  handler (`string` / `json`|record / `xml`|record / `string[][]`|record[]|streams / `byte[]`|stream),
  only `smb:FileInfo` and `smb:Caller` as extra parameters, no duplicates, return `error?`/`smb:Error?`.
- `onFileDelete` rules (`SMB_120`–`SMB_123`) and `onError` rules (`SMB_130`–`SMB_133`).

Everything the plugin implies is surfaced in `new`'s Service block: the handler set, the per-handler
content types and their alternative binding forms, the required/optional parameter split, and the
"at least one handler" rule. Nothing plugin-implied is missing from `new`. `old` surfaces **none** of it
(no Service section at all) — that is the single largest content gain of spec v2 for this library.
The only mismatch is the reverse direction: `new` asserts the two annotations are mandatory, which the
plugin does not enforce (§5.10).

## 8. Other considerations

- No deprecations: `grep -c '@deprecated\|# Deprecated'` over the bala module sources returns 0.
- Version `2.0.1` is a stable major; built with `ballerina_version: 2201.12.0`.
- Size: +175 lines (+18%) for `new`; the JSON grows 109,144 → 128,451 bytes (+17.7%). Modest cost for
  7 previously-invisible public symbols plus the service contract.
- Doc quality is good: README is 296 rendered lines with runnable examples, and per-field doc comments
  survive into both renders.
- The render is reference material, not compiled, but §5.1 and §5.6 both produce syntax that would not
  compile if copied verbatim — relevant because the Service block is explicitly a code template.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.0.1 …/module-ballerina-smb` + `git describe --tags` | `v2.0.1`, commit `f985f0e` — exact tag exists |
| `ls …/bala/ballerina/smb/2.0.1/java21/modules` | `smb` only — no submodules |
| `python3 …package.json` | `{'organization':'ballerina','name':'smb','version':'2.0.1','ballerina_version':'2201.12.0','export':['smb']}` |
| `wc -l old new` | 973 / 1148 |
| `grep -c '^// Unknown type:'` | old 5, new 0 |
| `grep -n '^// Unknown type:' old` | 357 `Error`, 563 `ContentByteStream`, 565 `ContentCsvRecordStream`, 567 `ContentCsvStringArrayStream`, 569 `Listener` |
| `grep -n '^// --- '` | old 4 markers (7, 296, 298, 571); new 6 (7, 296, 298, 658, 1062, 1142) |
| `diff -u old new \| wc -l` | 218 lines; `grep -c '^+'` 182, `grep -c '^-'` 7 (incl. header lines) → +181 / −6 |
| `diff <(sed -n '1,296p' old) <(sed -n '1,296p' new)` | identical (README unchanged) |
| readme vs `bala/docs/README.md` | both 10,715 chars, prefix-identical |
| `grep -E '^(public \|isolated \|client \|distinct )*(type\|class\|enum\|const\|annotation\|function\|service\|listener) '` | old 43 matches, new 51; new ⊇ old |
| `grep -hnE '^public ' bala/modules/smb/*.bal` | 28 public symbols enumerated (§6) |
| `grep -oE 'remote isolated function [a-zA-Z]+' caller.bal client.bal \| sort` vs render | 26 + 26, one-for-one match |
| `grep -c 'FileWriteOption option = "APPEND"'` | old 14, new 14 |
| `grep -n 'FileWriteOption option' bala/*.bal` | 15 source occurrences, all `= OVERWRITE` |
| `grep -n 'targetType' old/new` | 4 occurrences each, identical mangled form |
| `error.bal:18` | `public type Error distinct error;` |
| `listener_endpoint.bal:44` | `public isolated function init(*ListenerConfiguration listenerConfig) returns Error?` |
| `listener_endpoint.bal:19` | class doc "Listener for monitoring SMB servers…" (not in render) |
| `types.bal:119-135` | `ListenerConfiguration` field defaults, `auth?`/`fileNamePattern?`/`csvFailSafe?` optional-no-default |
| `types.bal:163,173` | both annotation declarations, match render verbatim |
| `PluginConstants.java:34-43` | 7 handler names, match render exactly |
| `SmbContentFunctionValidator.java:142-146,246-251` | per-handler accepted content types, match render's binding notes |
| `grep -rni 'annot' compiler-plugin/src/main/java/…/plugin/` | 3 hits, all in javadoc prose — no annotation validation |
| JSON structural diff (python) | `typeDefs` 34/34 both; differing entries only `Error`, `ContentByteStream`, `ContentCsvRecordStream`, `ContentCsvStringArrayStream`, `Listener`; `services` 0→1; `annotations` 0→2; `functions` 0→0 |
| JSON `Listener.init` params (new) | 15 params, `listenerConfig` has `"optional": true` and **no** `default`; identical list in old JSON |
| `grep -cP '[^\x00-\x7F]'` | 8 lines both sides (README em-dashes) — no encoding regression |
| `grep -c '@deprecated\|# Deprecated' bala/modules/smb/*.bal` | 0 |

## 10. Caveats and unverified items

- Neither render was compiled. The claim that `Listener.init` (§5.1) and the `typedesc` parameters
  (§5.6) are invalid Ballerina rests on the language rule that a required parameter may not follow a
  defaultable one, and on `typedesc<T> p = <>` not being expressible as `T p = T`. Not machine-verified
  with `bal build`.
- Whether `@smb:ServiceConfig` is mandatory in practice was determined from the compiler-plugin source
  and the `path` field doc only; runtime behaviour of a service with no annotation and no identifier
  path was not executed.
- The Service-block guidance text (handler descriptions, "Prefer the `path` field…", required/optional
  parameter lists) originates in LS-side trigger metadata that is not part of this library and was not
  read; it was validated only by cross-checking its factual claims against the compiler plugin.
- `bala_source` was `central cache`; the distribution-bundled bala (if any) was not compared against it.

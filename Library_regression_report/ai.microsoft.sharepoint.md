# ballerinax/ai.microsoft.sharepoint 1.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/ai.microsoft.sharepoint` |
| Pinned version | `1.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-ai.microsoft.sharepoint |
| Tag reviewed | `v1.0.1` (commit `f08072415fe7899b8b9efb249219408d042f3a15`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/ai.microsoft.sharepoint/1.0.1` |
| Old render | `309` lines |
| New render | `318` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module library: 6 public symbols in the default module (5 record types + 1 class).
`diff -u old new` produces exactly **one hunk**, at the end of the file: `old` emitted
`// Unknown type: TextDataLoader` (the library's only class and its entire public behaviour),
`new` emits a real `class TextDataLoader { ... }` with both public methods, their signatures,
their return types and the `@display` annotations.

Everything else — the header, the full 169-line README, and all 5 record type definitions —
is byte-identical between the two renders (verified: the record `typeDefs` compare equal in the
two JSONs, and `diff -u` shows no hunk before line 306).

Net effect: `new` restores the single most important declaration in the library. Zero regressions.
The residual accuracy problems (dropped default values, dropped `public`/`isolated`, closed→open
records, garbled multi-line doc continuations) are present identically in both sides and are
extractor/renderer-level, not caused by spec v2.

## 2. Change inventory

Line counts (`wc -l`): old **309**, new **318** (+9).

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` degraded lines | 1 | 0 | −1 |
| `type ... record {` declarations | 5 | 5 | 0 |
| `class ...` declarations | 0 | 1 | +1 |
| class methods rendered | 0 | 2 (`init`, `load`) | +2 |
| `@display` annotations rendered | 0 | 3 (1 class-level, 2 parameter-level) | +3 |
| README lines | 171 (lines 6–177) | 171 | 0 |
| Section markers (`// --- `) | 3 | 3 | 0 |

JSON level (`typeDefs`, 6 entries on both sides):

| typeDef | old `type` | new `type` | fields | funcs | payload equal? |
|---|---|---|---|---|---|
| `OAuth2ClientCredentialsGrantConfig` | Record | Record | 9 | 0 | SAME |
| `OAuth2RefreshTokenGrantConfig` | Record | Record | 10 | 0 | SAME |
| `ConnectionConfig` | Record | Record | 20 | 0 | SAME |
| `Library` | Record | Record | 4 | 0 | SAME |
| `Source` | Record | Record | 3 | 0 | SAME |
| `TextDataLoader` | *(absent)* | `"Class"` | 0 | 2 | DIFF |

Three concrete JSON deltas on `TextDataLoader`:
1. `"type": "Class"` added — this is what unblocks `renderTypeDef` and removes the `// Unknown type:` line.
2. `annotations` added: class-level `@display {label: "Microsoft SharePoint Text Data Loader"}`
   and per-parameter `@display` on both `init` parameters.
3. `init` return type de-qualified: old `"ballerina/ai:1.13.0:Error?"` → new `"ai:Error?"`.

Nothing was removed. `annotations`, `clients`, `functions`, `services` are all empty lists and
`readme`/`name`/`description` are identical on both sides.

## 3. Correctness against library source

Upstream `v1.0.1` `ballerina/*.bal` is byte-identical to the bala's
`modules/ai.microsoft.sharepoint/*.bal` (`diff -q` clean for all three files), so GitHub and the
bala agree; both were used.

Everything `new` adds checks out against `sharepoint_data_loader.bal`:

| Rendered (new, lines 309–318) | Source | Verdict |
|---|---|---|
| `@display {label: "Microsoft SharePoint Text Data Loader"}` on the class | `sharepoint_data_loader.bal:23-25` | correct |
| `class TextDataLoader` | `sharepoint_data_loader.bal:26` `public isolated class TextDataLoader` | correct name; qualifiers dropped (§5) |
| `function init(@display {label: "SharePoint Connection Configurations"} ConnectionConfig sharePointConnectionConfigs, @display {label: "Data Sources"} Source[] sources) returns ai:Error?` | `sharepoint_data_loader.bal:40-41` | exact match incl. both `@display` labels, param names, order, and return type |
| `function load() returns ai:Document[]\|ai:Document\|ai:Error` | `sharepoint_data_loader.bal:60` | exact match |
| `// Special Agent Note: Document, Error FROM ballerina/ai package` | imports `ballerina/ai` at `:17` | correct provenance |

Record types (identical in both renders) also verified against `types.bal`:
- `ConnectionConfig`: all 20 fields present, in source order, `auth` correctly required
  (`types.bal:36-81`).
- `OAuth2ClientCredentialsGrantConfig` renders 9 fields — the `*http:OAuth2ClientCredentialsGrantConfig`
  inclusion is correctly flattened. Cross-checked against
  `.../distributions/ballerina-2201.12.12/repo/bala/ballerina/oauth2/2.14.1/.../client_oauth2_provider.bal:35-43`
  (`tokenUrl, clientId, clientSecret, scopes, defaultTokenExpTime, clockSkew, optionalParams, credentialBearer, clientConfig`) — set and order match.
- `OAuth2RefreshTokenGrantConfig` renders 10 fields; matches `client_oauth2_provider.bal:106-115`
  plus the module's `refreshUrl` override.
- `Library` (4 fields) and `Source` (3 fields) match `types.bal:86-101` and `types.bal:103-133`.

No invented symbols. The 4 non-public records (`DriveItem`, `Folder`, `File`,
`DriveItemCollectionResponse`, `types.bal:137-172`) and the module-private `DocumentKind` enum
(`utils.bal:100`) are correctly excluded from both renders.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old/…bal.txt new/…bal.txt` — one hunk only, purely additive (`-1` line, `+13` lines).
- Per-typeDef JSON equality: all 5 record typeDefs compare `==` between the two JSONs; the only
  DIFF is `TextDataLoader`, and that diff is strictly additive (`type`, `annotations`) plus a
  de-qualification of one type name.
- README: `readme` string in the new JSON is `==` the bala's `docs/README.md` (169 lines, `strip()`
  equal), and lines 6–177 of both renders are identical — no README content lost.
- Section markers, `import` header, and type ordering identical.
- `// Unknown type:` count: old 1 → new 0.
- Malformed doc-continuation line count identical on both sides (23 vs 23), so `new` did not
  introduce any new formatting damage.

The one de-qualification (`ballerina/ai:1.13.0:Error?` → `ai:Error?`) is an improvement — the old
form is not valid Ballerina and would mislead a code-generating LLM — and it never reached the old
render anyway, since the old render dropped the whole class.

## 5. Issues in `new` (independent of `old`)

These are real inaccuracies in `new` vs. the library source. All but #1–#3 are also present in
`old`; none is a regression, but all mislead a consuming LLM.

1. **Class doc is wrong text.** New line 309 renders `# Initializes the SharePoint data loader.`
   as the class documentation. That is `init`'s doc (`sharepoint_data_loader.bal:34`). The class's
   actual doc, `# A data loader that retrieves documents from SharePoint document libraries as text.`
   (`sharepoint_data_loader.bal:22`), is nowhere in the render. The defect is in the extracted JSON
   (`typeDefs[TextDataLoader].description == "Initializes the SharePoint data loader.\n"` in **both**
   JSONs), but it only becomes visible in `new`.
2. **`*ai:DataLoader` inclusion dropped.** `sharepoint_data_loader.bal:27` declares the class
   implements `ai:DataLoader`; the render gives no hint, so an LLM cannot tell this loader is
   pluggable into `ai:` pipelines.
3. **Parameter and return docs dropped for the class methods.** The JSON carries
   `parameters[].description` and `return.description` for both `init` and `load`; the renderer
   emits none of them (new lines 313, 317 have no `# + param -` / `# + return -` lines).
4. **All 21 record field default values are dropped**, and every field that had a default is
   rendered as optional `?`. Counted from `types.bal`: `OAuth2ClientCredentialsGrantConfig` 1
   (`tokenUrl = "https://login.microsoftonline.com/common/oauth2/v2.0/token"`),
   `OAuth2RefreshTokenGrantConfig` 1 (`refreshUrl`), `ConnectionConfig` 13 (incl.
   `serviceUrl = "https://graph.microsoft.com/v1.0"`, `timeout = 30`, `httpVersion = http:HTTP_2_0`),
   `Library` 4 (`name = "Documents"`, `paths = ["/"]`, `recursive = false`,
   `includeExtensions = ()`), `Source` 2 (`libraries = [{}]`, `pages = ()`). The JSON contains no
   `defaultValue` key anywhere, so this is an extractor gap. Consequence: the render cannot
   distinguish "optional, no default" (`poolConfig?`, `secureSocket?`, …) from "has a meaningful
   default", and the default Graph service URL — the value most likely to be needed — is invisible.
5. **Closed records rendered as open.** All five source types are `record {| … |}`; all five render
   as `record { … }`. An LLM may add fields that will not compile.
6. **`public` / `isolated` qualifiers dropped** on all 6 declarations, and on both class methods.
   The render's only `public` token is inside the README prose.
7. **Multi-line doc comments lose the `#` continuation prefix** — 23 lines in the Types section of
   each render. Worst case is `Source.siteId` (new lines 282–299), where a whole fenced code block
   with box-drawing characters is emitted as bare text inside a record body. This is non-compiling
   Ballerina and visually merges documentation into the type definition.

## 6. Coverage gaps vs. the library

**Zero.** The bala exports one module (`package.json: "export": ["ai.microsoft.sharepoint"]`), which
is the default module; `ls modules/` shows only `ai.microsoft.sharepoint`. So the known
`getDefaultModule()`-only limitation costs nothing here.

`grep -n 'public ' modules/ai.microsoft.sharepoint/*.bal` yields exactly 8 hits = 5 public types
+ the class + its 2 public methods. All 6 top-level public symbols and both methods appear in `new`.
No module-level public functions, constants, enums, annotations, listeners, services or clients
exist, and the renders correctly show none.

Old render coverage gap for comparison: 1 (`TextDataLoader` and its 2 methods).

## 7. Compiler plugin

The package has **no compiler plugin**. `compiler-plugin/` does not exist in the bala
(`ls .../java21/compiler-plugin` → No such file or directory) and there is no `compiler-plugin.json`
or `*CompilerPlugin*` file anywhere in the upstream `v1.0.1` tree. The `native/` directory is a
plain JNI/interop library (Tika + PDFBox text extraction, bound at `utils.bal:159` via
`@java:Method`), not a plugin.

Therefore nothing plugin-implied is missing from the render.

## 8. Other considerations

- **Version**: `1.0.1` is a stable release; not deprecated. Central `source_repository` in
  `package.json` matches the manifest repo URL.
- **Platform dependencies** (Tika 3.2.2, PDFBox 3.0.5, commons-io 2.20.0) and `graalvmCompatible: true`
  are in `package.json` but, by design, not part of the render. Not an issue.
- **Size/tokens**: 318 lines total, of which 171 are README. Trivial cost; the +9 lines that buy the
  class are excellent value.
- **Non-compiling render**: neither render is valid Ballerina, because of item 7 in §5 (bare doc
  continuation lines inside record bodies) and item 5 (`{| |}` → `{ }` with no closing `|`). Shared
  by both sides.
- **`Library` name shadowing**: the module defines a public type named `Library`, which is also the
  renderer's own domain term. No actual conflict in the output, but worth knowing when grepping.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 309 / 318 |
| `grep -c '^// Unknown type:' old` / `new` | 1 / 0 |
| `grep -n '^// --- ' old` / `new` | identical: 6, 177, 179 |
| `diff -u old/…bal.txt new/…bal.txt` | single hunk `@@ -306,4 +306,13 @@`; `-// Unknown type: TextDataLoader`, `+13` lines defining `class TextDataLoader` |
| Python per-key JSON compare | `annotations/clients/description/functions/name/readme/services` SAME; `typeDefs` DIFF (6 vs 6) |
| Python per-typeDef compare | 5 records SAME; `TextDataLoader` DIFF — old lacks `"type"`, new has `"type":"Class"` + `annotations` + `ai:Error?` instead of `ballerina/ai:1.13.0:Error?` |
| `grep 'defaultValue' new/…json` | not present → no defaults extracted |
| `ls .../1.0.1/java21/modules` | only `ai.microsoft.sharepoint` (default module) |
| `cat .../java21/package.json` | `"export": ["ai.microsoft.sharepoint"]`, `ballerina_version 2201.12.0` |
| `ls .../java21/compiler-plugin` | No such file or directory |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1` → `v1.0.1` = `f08072415fe7899b8b9efb249219408d042f3a15` |
| `git clone --depth 1 --branch v1.0.1` | success |
| `diff -q src/ballerina/{sharepoint_data_loader,types,utils}.bal` vs bala | all identical (no output) |
| `diff -q bala/docs/README.md src/ballerina/README.md` | identical |
| Python: JSON `readme` vs `docs/README.md` | `equal: True`, 169 lines both |
| `grep -n 'public ' modules/*.bal` | 8 hits: `sharepoint_data_loader.bal:26,40,60`; `types.bal:20,27,36,86,103` |
| `sharepoint_data_loader.bal:22-25` | class doc `# A data loader that retrieves documents…` + `@display` label |
| `sharepoint_data_loader.bal:27` | `*ai:DataLoader` |
| `sharepoint_data_loader.bal:40-41` | init signature — matches new render line 313 exactly |
| `sharepoint_data_loader.bal:60` | `public isolated function load() returns ai:Document[]\|ai:Document\|ai:Error` — matches new line 317 |
| Python regex count of `= ` defaults in public records of `types.bal` | 21 total (1/1/13/4/2); `awk`+`grep -c` cross-check also 21 |
| Python field counts per typeDef | 9 / 10 / 20 / 4 / 3 — match `types.bal` and oauth2 source |
| oauth2 2.14.1 `client_oauth2_provider.bal:35-43, 106-115` | inherited field sets match the flattened render |
| `grep -cE '^type '` / `'^class '` old, new | 5/0 and 5/1 |
| Malformed doc-continuation line count (awk+grep, lines ≥179) | 23 in old, 23 in new |

## 10. Caveats and unverified items

- The precomputed diff at `OLD_AND_NEW_DIFFS/ai.microsoft.sharepoint_diff.md` was not relied on;
  every claim above comes from a command run directly against the renders, JSONs, bala and clone.
- I did not run the render pipeline myself; both sides are taken as produced. The claim "the two
  sides differ only by extractor/renderer version" is supported here by the bala/upstream identity
  check (same source on both sides) but the pipeline execution itself is out of scope.
- `ballerina/ai` `Document`/`Error`/`DataLoader` definitions were not opened; the `ai:` references
  in the render were checked for exact textual agreement with the library source, not for existence
  in `ballerina/ai` 1.13.0.
- Whether the missing `*ai:DataLoader` inclusion and the missing record default values are intended
  renderer behaviour (rather than defects) was not determined from the renderer source; they are
  reported as accuracy observations, shared by both sides.

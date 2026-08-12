# Copilot library renders — `old/` set

Generated from `ballerina-platform/ballerina-vscode` @ `main`, commit `eb5d81b3b283b5681306a75bfb48aa3172a9fb80`.
Library content resolved from balas at the **exact versions pinned in `CLAUDE.md`** (Ballerina 2201.13.4, Swan Lake Update 13).

## Layout

```
<library_name>/
├── old/   <org>_<name>.json      stage-1 JSON  (CopilotLibraryManager → ModelToJsonConverter)
│          <org>_<name>.bal.txt   stage-2 render (toSyntaxString)
└── new/   <org>_<name>.json      empty placeholder (0 bytes)
           <org>_<name>.bal.txt   empty placeholder (0 bytes)
```

Directory name is the org-stripped `<library_name>`; file names keep the `<org>_<name>` prefix.

## Totals

| | count |
|---|---|
| Libraries requested (unique) | 162 |
| Directories | 162 |
| `old/` JSON produced | **162** |
| `old/` renders produced | **162** |
| Resolved at the pinned version (`PIN_OK`) | **162 / 162** |
| Stage-1 resolution failures | 0 |
| `new/` empty placeholders | 324 (all exactly 0 bytes) |
| Total JSON | 46.8 MB |
| Total rendered | 13.9 MB |

Per-library pinned-vs-resolved evidence is in `versions.txt`.

## Version pinning — how it was enforced

`CopilotLibraryManager` requests every library with a **null version** ("use latest"), so version
selection is not controlled by code. Under Gradle the tests run with `-Dls.test.offline=true`, which
puts `PackageUtil` in `FORCE_OFFLINE` mode: it never contacts Ballerina Central and treats "latest"
as *the highest version present in the build-owned Ballerina home*
(`build/ballerina_dependencies/home`), failing visibly when a package is absent.

Pinning was therefore enforced as data, not code: each of the 162 versions from the `CLAUDE.md`
table was pulled into that home with `bal pull <org>/<name>:<version>` (`BALLERINA_HOME_DIR` set),
after verifying no library had a **newer**-than-pinned version there that would win instead. The
probe then recorded the version actually resolved for every library through the same `PackageUtil`
call the manager uses, and compared it to the pinned table. All 162 returned `PIN_OK`.

This mattered: an earlier pass without the pinned home silently rendered **22 libraries at older
versions** — `openai.chat` 4.0.1 (pinned 5.0.0), `github` 5.1.0 (6.0.0), `salesforce` 8.4.0 (8.7.0),
`mysql`/`postgresql`/`mssql` at 1.17–1.18 (1.19.0) — and left 112 unresolved.

## Deviation from upstream `main`

**One renderer patch was applied**, at the user's direction:

```diff
- for (const method of service.methods) {
+ for (const method of service.methods ?? []) {
```

`to-syntax-string.ts:440` (`renderFixedService`). Without it `ballerina/mcp` crashes with
`TypeError: service.methods is not iterable` — its single fixed service carries only
`type,name,listener`, so `methods` is `undefined`. With the guard, mcp renders to 1,058 lines.

Re-rendering all 162 with the patch changed **only** `ballerina_mcp.bal.txt` (verified by checksum
comparison of every render before and after), so no other output reflects patched behaviour.

Nothing else was modified — `CopilotLibraryManager`, `PackageUtil`, and the rest of
`to-syntax-string.ts` are stock upstream.

## Known gaps

**1. `ballerinax/copybook` renders only 30 lines.**
The published package at the pinned 1.1.0 does not compile — 9 type errors of the form
`incompatible types: expected 'ballerinax/copybook:1.1.0:Node', found '...GroupItem'`. Its main
`Converter` client comes through as `// Unknown type: Converter`. This is a defect in the published
package, not in the pipeline.

**2. `ballerinax/azure_storage_service` renders README only (37 lines).**
Extraction uses `pkg.getDefaultModule()` only. This package's API lives in submodules
(`azure_storage_service.blobs`, `.files`, `.utils`), so none of it is captured. Same root cause
previously seen with `candid` — which now renders 133 lines.

**3. `ballerinax/idetraceprovider` renders 44 lines (README only).**
Genuinely exports no public symbols, so an empty render is correct.

**4. 2,370 `// Unknown type:` lines across 101 of the 162 renders.**
`renderTypeDef` (`to-syntax-string.ts:212`) handles only Record, Enum, Union, Constant, and Class.
Three kinds present in the JSON fall through to a bare comment with no members: `Error`, untagged
object types (no `type` field), and `Other`. Highest counts: `stripe` (610), `discord` (421),
`sap.s4hana.api_sales_order_srv` (167), `http` (155), `postgresql` (126).

## Verification performed

- All 162 JSON files parse; each top-level `name` matches its `org/name`.
- All 162 renders carry the matching `// Library: <org>/<name>` header for their directory.
- All 324 `new/` placeholders confirmed present and exactly 0 bytes.
- No unexpected or missing files in any `old/` or `new/` directory.

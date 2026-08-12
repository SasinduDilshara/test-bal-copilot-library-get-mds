# Copilot library renders — `old/` and `new/`

Both sides render the same 206 libraries at the **exact versions pinned in `CLAUDE.md`**
(Ballerina 2201.13.4, Swan Lake Update 13). Per-library pinned-vs-resolved evidence is in `versions.txt`.

| | `old/` | `new/` |
|---|---|---|
| Source repo | `ballerina-platform/ballerina-vscode` | local `Check-PR-s/ballerina-vscode` |
| Branch | `main` | `L1_json_and_annotations_with_spec_v2` |
| Commit | `eb5d81b3b283b5681306a75bfb48aa3172a9fb80` | `412ba01e36a017d80b299e94ba168db70ba835d9` |

## Layout

```
<library_name>/
├── old/   <org>_<name>.json      stage-1 JSON  (CopilotLibraryManager → ModelToJsonConverter)
│          <org>_<name>.bal.txt   stage-2 render (toSyntaxString)
└── new/   <org>_<name>.json      same pipeline, spec-v2 source
           <org>_<name>.bal.txt
```

Directory name is the org-stripped `<library_name>`; file names keep the `<org>_<name>` prefix.

## Totals

| | `old/` | `new/` |
|---|---|---|
| Libraries | 206 | 206 |
| JSON produced | **206** (48.4 MB) | **206** (52.8 MB) |
| Renders produced | **206** (14.5 MB) | **206** (15.9 MB) |
| Resolved at pinned version | **206 / 206** | **206 / 206** |
| Stage-1 failures | 0 | 0 |
| Render failures | 0 (after the mcp patch below) | 0 |
| `// Unknown type:` lines | **2,656** across 141 libs | **0** |

## How the pinning was enforced (it differs between the two)

**`old/` (`main`)** has no version-aware entry point — `loadFilteredLibraries` requests every library
with a **null version** ("use latest"). Under Gradle the tests run with `-Dls.test.offline=true`,
putting `PackageUtil` in `FORCE_OFFLINE`: it never contacts Central and treats "latest" as *the
highest version present in the build-owned home* (`build/ballerina_dependencies/home`). Pinning was
therefore enforced as data — each pinned version was pulled into that home with `bal pull`, after
confirming no library had a **newer**-than-pinned version there that would win instead.

**`new/` (spec v2)** adds a version-aware overload,
`loadFilteredLibraries(String[], Map<String,String> pinnedVersions)`, which resolves through
`PackageUtil.getModulePackage(project, org, name, pinned)` — an **explicit exact-version** request.
The renders use it, so pinning here is direct rather than inferred.

In both cases the probe recorded the version actually resolved for every library and compared it to
the pinned table; all 206 returned `PIN_OK` on both sides.

This mattered. An early pass without a pinned home silently rendered **22 libraries at older
versions** — `openai.chat` 4.0.1 (pinned 5.0.0), `github` 5.1.0 (6.0.0), `salesforce` 8.4.0 (8.7.0),
`mysql`/`postgresql`/`mssql` at 1.17–1.18 (1.19.0) — and left 112 unresolved. Those renders looked
complete and plausible; only the resolved-version check exposed them.

## Library set

The set grew from 162 to **206**. The 44 added libraries are the `module-ballerina-*` repositories in
the `ballerina-platform` GitHub organisation that were absent from the list and are published to
Ballerina Central, pinned at their latest Central version at the time of the run.

Four `module-ballerina-*` repositories were deliberately **excluded** — they have no package on
Central, so there is nothing to resolve or render: `ballerina/c2c`, `ballerina/docker`,
`ballerina/kubernetes`, `ballerina/data.toml`.

The 44 were rendered with `.claude/skills/render-copilot-libraries`, which enforces the same gates
described above.

## Deviation from source

**`old/` carries one renderer patch**, applied at the user's direction:

```diff
- for (const method of service.methods) {
+ for (const method of service.methods ?? []) {
```

`to-syntax-string.ts:440` (`renderFixedService`). Without it `ballerina/mcp` crashes with
`TypeError: service.methods is not iterable` — its single fixed service carries only
`type,name,listener`, so `methods` is `undefined`. Re-rendering all 162 (the original set) with the patch changed
**only** `ballerina_mcp.bal.txt`, verified by checksum comparison of every render before and after.

**`new/` required no patch** — spec v2 rewrites `to-syntax-string.ts` (2,459 lines vs 592) and the
bug is gone. mcp renders cleanly at 1,258 lines.

Nothing else was modified in either source; the probe test and its `testng.xml` registration were
removed after each run.

## What spec v2 changes in the output

**Type coverage is the headline.** In `main`, `renderTypeDef` handles only Record, Enum, Union,
Constant, and Class; `Error`, untagged object types, and `Other` fall through to a bare
`// Unknown type: <name>` comment with no members — 2,656 such lines across 141 of the 206 renders
(worst: `stripe` 610, `discord` 421, `sap.s4hana.api_sales_order_srv` 167, `http` 155). **Spec v2
emits none.** `ballerinax/copybook` shows it concretely:

```diff
- // Unknown type: Error
+ # Represents copybook module related errors.
+ type Error error;

- // Unknown type: Converter
+ # Initializes the converter with a schema.
+ class Converter {
+     function init(string schemaFilePath) returns Error?;
+     # Converts the provided record or map<json> value to bytes.
+     function toBytes(record {|anydata...;|} input, ...) returns byte[]|Error;
+     ...
+ }
```

## Known gaps

**1. `ballerinax/azure_storage_service` renders README only (37 lines in `old/`).**
Extraction uses `pkg.getDefaultModule()` only, and this package's API lives in submodules
(`azure_storage_service.blobs`, `.files`, `.utils`), so none of it is captured. Verified against the
bala. Previously seen with `candid`, which now renders 133 lines.

**2. `ballerinax/idetraceprovider` renders README only (44 lines).**
Genuinely exports no public symbols, so an empty render is correct.

**3. `ballerinax/copybook`** — the published package at the pinned 1.1.0 does not compile (9 errors of
the form `incompatible types: expected 'Node', found 'GroupItem'`). Extraction still succeeds; its
short `old/` render was caused by the renderer's missing type coverage, not the compile errors, as
the spec-v2 diff above shows.

## Verification performed

- All 412 JSON files parse; each top-level `name` matches its `org/name`.
- All 412 renders carry the matching `// Library: <org>/<name>` header for their directory.
- No empty, missing, or unexpected files in any `old/` or `new/` directory.
- Both stage-1 runs reported `PIN_OK` for all 206 libraries against the `CLAUDE.md` table.

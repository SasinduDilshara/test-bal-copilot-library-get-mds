# ballerinax/azure_storage_service 4.3.4 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/azure_storage_service` |
| Pinned version | `4.3.4` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-azure-storage-service |
| Tag reviewed | `v4.3.4` (commit `464bc3a60278d064204ae62f2a73d02a303e1be2`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/azure_storage_service/4.3.4/java21` |
| Old render | `37` lines |
| New render | `38` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The default module of this package contains exactly one public declaration: `public type Error distinct error;` (bala `modules/azure_storage_service/main.bal:18`). Everything else — both client classes, all records, enums and helper functions — lives in the exported submodules `azure_storage_service.blobs` and `azure_storage_service.files`, which neither side extracts.

The only difference between the two renders is that `old` degraded that one type to `// Unknown type: Error` (no doc, no definition) while `new` emits the doc comment plus a real definition `type Error error;`. Lines 1–34 (header, import, README block, section marker) are byte-identical. No declaration, doc, or README content was lost. One strictly-additive improvement; zero regressions.

## 2. Change inventory

Whole-file diff is a single hunk (old 34–37 → new 34–38): `-1` line, `+2` lines.

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Type definitions rendered | 0 | 1 (`Error`) | +1 |
| Doc comments rendered | 0 | 1 | +1 |
| Functions / clients / services / annotations / consts / enums | 0 | 0 | 0 |
| `// --- ` section markers | 3 | 3 | 0 |
| Version/module-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| README block lines (7–33) | 27 | 27 | 0 |

Declarations added (1): `type Error`.
Declarations removed (0): none.
Declarations modified (0): none — nothing existed in `old` to modify.

JSON side (both files are 4 sections + `typeDefs`): the only change is that `new`'s `typeDefs[0]` gains `"baseType": "error"`; `name`, `description`, `type`, and the whole 1530-char `readme` string are identical. `clients`, `functions`, `services`, `annotations` are empty arrays on both sides.

## 3. Correctness against library source

- Upstream `ballerina/main.bal:17-18` at tag `v4.3.4`:
  ```ballerina
  # Represents storage module error.
  public type Error distinct error;
  ```
  Bala `modules/azure_storage_service/main.bal:17-18` is byte-identical to it. So the render's doc line `# Represents storage module error.` and the symbol name `Error` are exact.
- `Ballerina.toml` in the tag declares `version = "4.3.4"`, `distribution = "2201.12.0"`; bala `package.json` declares the same version and `ballerina_version: 2201.12.0`, and Central reports `4.3.4` / `2201.12.0`. No version drift on either side.
- README: the `readme` field in both JSONs is byte-identical (1530 chars) to bala `docs/README.md`, and the rendered README block reproduces it verbatim.
- The default module has no other public symbol — `grep '^public ' main.bal` returns exactly that one line — so an empty `clients`/`functions`/`services` set is correct *for the default module*.

## 4. Regressions

**None found.** What was checked:

- `diff` of lines 1–34 of the two renders: identical (header, description comment, `import` line, README block, `// --- Types ---` marker).
- The full unified diff is one hunk that only replaces the `// Unknown type: Error` placeholder with the doc + definition. Nothing is deleted except the placeholder itself.
- Declaration sets extracted from both files: `old` = {} plus 1 placeholder; `new` = {`type Error`}. Nothing present in `old` is missing from `new`.
- JSON comparison: `new` is a strict superset of `old` (adds `baseType`, changes nothing else).
- `grep -c '^// Unknown type:'`: `old` 1 → `new` 0.

## 5. Issues in `new` (independent of `old`)

1. **`distinct` and `public` qualifiers not represented** — source is `public type Error distinct error;`, render is `type Error error;`. An LLM reading this cannot tell the type is a *distinct* error, which matters for `is`/error-binding narrowing. This is a renderer-wide convention rather than an azure-specific defect: the new renderer emits no `public` on any type in any library render (e.g. `aws.sqs` new render line 326 `type Error error<aws:ErrorDetails>;` for a source-level distinct error; `websub` line ~370 likewise). Severity: cosmetic/low. It is not a regression — `old` conveyed strictly less (name only, no base type, no doc).
2. **Render is not usable code** — the render advertises `import ballerinax/azure_storage_service;` and then exposes only an error type. There is no client, no connection config, no operation. Any LLM asked to write Azure Blob/File code from this render has nothing to call. This is caused by the coverage gap in §6, not by anything `new` did wrong, and it is identical in `old`.
3. No malformed syntax, no invented symbols, no encoding problems, no truncated docs found in `new`.

## 6. Coverage gaps vs. the library

**Default-module symbols missing from both renders: 0.** The default module exports exactly one symbol (`Error`) and `new` renders it.

**Submodule-only API missing from both renders (shared gap, not a `new` regression): 95 public declarations.** `Ballerina.toml`/`package.json` `export = ["azure_storage_service", "azure_storage_service.files", "azure_storage_service.blobs"]`, so both submodules are part of the package's public surface, but the extractor uses `pkg.getDefaultModule()` only.

| Module | public decls | notable |
|---|---|---|
| `azure_storage_service.blobs` | 46 | `client class BlobClient`, `client class ManagementClient`, `ConnectionConfig`, `Blob`, `BlobProperties`, `ListBlobResult`, `ByteRange`, enums `AuthorizationMethod`/`BlobType`/`PageOperation`/`AccessLevel`, error hierarchy (`ServerError`, `ClientError`, `NotFoundError`, …) |
| `azure_storage_service.files` | 49 | `client class FileClient`, `client class ManagementClient`, `ConnectionConfig`, `SharesList`, `FileList`, `DirectoryList`, `RangeList`, `NoSharesFoundError`, error hierarchy |
| **total** | **95** | 4 client classes, 46 remote/resource methods across them |

`azure_storage_service.utils` is non-exported (`"export": false` in `package.json`) and is correctly absent.

This is by far the dominant accuracy problem for this library, and it is identical on both sides.

## 7. Compiler plugin

No compiler plugin exists. `find` over the `v4.3.4` clone for `*compiler*plugin*` returns nothing, and the bala has no `compiler-plugin/` directory (bala root contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived is therefore expected in, or missing from, either render.

## 8. Other considerations

- Package is **not deprecated** (Central `deprecated: null`, `deprecateMessage: ""`). Pull count 285.
- Version 4.3.4 is a stable (post-1.0) release; `graalvmCompatible: true`.
- The README's Compatibility table still advertises "Ballerina Swan Lake 2201.3.0" while the package is built for 2201.12.0 — a stale doc in the library itself, faithfully reproduced by both renders. Not a render defect.
- Size/token impact is negligible: 37 → 38 lines (2168 → 2198 bytes). Roughly 90% of both renders is the README.
- This library is a candidate for a submodule-extraction follow-up: at 38 lines the render is almost pure README and offers an LLM no API surface at all.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 37 / 38 |
| `diff <(sed -n '1,34p' old) <(sed -n '1,34p' new)` | no output — identical |
| `diff -u old new` | 1 hunk, `-// Unknown type: Error` → `+# Represents storage module error.` / `+type Error error;` |
| `grep -c '^// Unknown type:' old` / `new` | 1 / 0 |
| `grep -c '^// --- ' old` / `new` (from diff doc, re-checked in file) | 3 / 3 |
| `cat -n bala .../modules/azure_storage_service/main.bal` | 18 lines; only decl at 17-18: `# Represents storage module error.` / `public type Error distinct error;` |
| `cat -n src/ballerina/main.bal` @ `v4.3.4` | identical to bala main.bal |
| `git ls-remote --tags <repo>` | `v4.3.4` → `bfeeba51…`, peeled `464bc3a6…` |
| `git clone --depth 1 --branch v4.3.4` | succeeded |
| `cat bala package.json` | version 4.3.4, ballerina_version 2201.12.0, export = [root, .files, .blobs], modules .blobs/.utils/.files with `export:false` flags |
| `cat src/ballerina/Ballerina.toml` | version 4.3.4, distribution 2201.12.0 — matches bala |
| Python compare `new.json['readme']` vs bala `docs/README.md` | identical, 1530 chars both |
| `python3 -m json.tool` on both JSONs + manual compare | only delta: `typeDefs[0].baseType = "error"` added in `new` |
| `grep -c '^public ' bala modules/azure_storage_service.blobs/*.bal` | 46 |
| `grep -c '^public ' bala modules/azure_storage_service.files/*.bal` | 49 |
| `grep '^public isolated client class'` across submodules | 4 (`BlobClient`, `ManagementClient` ×2, `FileClient`) |
| `grep -oE '(remote|resource) [a-z ]*function [A-Za-z]+'` across submodules | 46 methods |
| `find <clone> -iname '*compiler*plugin*'` | no matches |
| `curl api.central.ballerina.io/.../4.3.4` | deprecated: null; modules: root, .blobs, .files |
| Cross-library check `grep '^type .* error;'` in other `new` renders | `public`/`distinct` omitted everywhere → renderer-wide convention |

## 10. Caveats and unverified items

- I did not compile the render. "Non-compiling" claims are based on reading, not on `bal build`. The single emitted line `type Error error;` is syntactically valid Ballerina; the render as a whole is a stub file and was never intended to compile standalone.
- The submodule public-declaration counts (46 / 49 / 95) are line counts of top-level `^public ` declarations in the bala `.bal` sources; they exclude public members declared inside client classes (counted separately as 46 remote/resource methods) and any public symbol not starting at column 0. They are a lower bound on the true public surface.
- I did not diff the two `ballerina-vscode` sources (`eb5d81b3` vs `412ba01e`) directly; statements about renderer-wide behaviour (`public`/`distinct` omission, `baseType` addition) are inferred from the render/JSON outputs across libraries in this repo, not from reading renderer code.
- Whether `getDefaultModule()`-only extraction is intended behaviour for spec v2 was taken from the brief and confirmed empirically (empty `clients`/`functions` in both JSONs despite 4 client classes existing), not from renderer source.

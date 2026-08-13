# ballerina/persist 1.7.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/persist` |
| Pinned version | `1.7.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-persist |
| Tag reviewed | `v1.7.0` (commit `d98dcfd638b12b49c0dd42aabb03648f1b8dc993`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/persist/1.7.0/java21` |
| Old render | `207` lines |
| New render | `211` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/persist` is a tiny module: one exported module (`persist`), 4 `.bal` files, 10 public
declarations total (1 object type, 4 error types, 5 functions). The whole delta between `old` and
`new` is one hunk: the four `// Unknown type:` placeholders for `Error`,
`ConstraintViolationError`, `NotFoundError` and `AlreadyExistsError` are replaced by real
declarations with their doc comments. Nothing is removed, nothing is reworded, the README block and
the entire Functions section are byte-identical. Coverage of the module's public API is complete on
both sides.

The one caveat on the improvement: the new declarations render all four error types as
`type X error;`, so the fact that `ConstraintViolationError`/`NotFoundError`/`AlreadyExistsError`
are `distinct Error` (i.e. subtypes of `persist:Error`) is not conveyed. That is still strictly more
information than `old` gave (which was none), so it is not a regression — but it is a residual
inaccuracy worth knowing for a foundational module whose error type other `persist` datastore
packages match against.

## 2. Change inventory

Line counts (`wc -l`): old **207**, new **211** (+4).

`// Unknown type:` placeholders: old **4**, new **0**.
Version/module-qualified type refs (`mod:1.2.3:Type`): old **0**, new **0**.
Section markers: **4** on both sides (`// --- README ---`, `// --- END README ---`,
`// --- Types ---`, `// --- Functions ---`).

Declaration-set diff (sorted top-level declarations):

| Kind | Added in `new` | Removed in `new` | Modified |
|---|---|---|---|
| type (error) | 4 — `Error`, `ConstraintViolationError`, `NotFoundError`, `AlreadyExistsError` | 0 | 0 |
| class | 0 | 0 | 0 |
| function | 0 | 0 | 0 |
| enum / const / annotation / service / listener / client | 0 | 0 | 0 |

Block-level verification:
- `diff <(sed -n '1,171p' old) <(sed -n '1,171p' new)` → identical (header + full README).
- `diff` of everything from `// --- Functions ---` to EOF → identical (all 5 functions, docs, signatures).
- Only the Types section changed: old lines 179–185 (4 placeholder comments) → new lines 179–189
  (4 doc-commented type definitions).

JSON delta (`old/ballerina_persist.json` vs `new/ballerina_persist.json`, both normalised and
sorted): the **only** structural difference is 4 added `"baseType": "error"` keys, one on each of
the four `"type": "Error"` typeDefs. `typeDefs` 5→5, `functions` 5→5, `clients` 0→0, `services`
0→0, `annotations` 0→0 on both sides. So the extractor change here is purely additive; the renderer
change is `renderBaseTypeDefinition` now handling the `Error`/`Other` categories instead of falling
through to the placeholder.

## 3. Correctness against library source

The GitHub clone at `v1.7.0` and the bala are byte-identical for all four `.bal` files and for
`README.md` (verified with `diff`), so there is no source/bala disagreement to arbitrate.

Every declaration in `new` checked against the bala source
(`.../1.7.0/java21/modules/persist/`):

| Rendered (new) | Source | Verdict |
|---|---|---|
| `class AbstractPersistClient {}` (L176) | `abstract_persist_client.bal:2` `public type AbstractPersistClient distinct object {};` | Present; kind mis-labelled (see §5.2) |
| `type Error error;` (L180) | `errors.bal:18` `public type Error distinct error;` | Present; `distinct` lost (see §5.1) |
| `type ConstraintViolationError error;` (L183) | `errors.bal:21` `public type ConstraintViolationError distinct Error;` | Present; supertype flattened to `error` (§5.1) |
| `type NotFoundError error;` (L186) | `errors.bal:24` `public type NotFoundError distinct Error;` | Present; supertype flattened (§5.1) |
| `type AlreadyExistsError error;` (L189) | `errors.bal:27` `public type AlreadyExistsError distinct Error;` | Present; supertype flattened (§5.1) |
| `function getNotFoundError(string entity, anydata key) returns NotFoundError;` (L198) | `errors.bal:34` | Signature matches exactly (minus `public isolated`) |
| `function getAlreadyExistsError(string entity, anydata key) returns AlreadyExistsError;` (L205) | `errors.bal:49` | Signature matches exactly (minus `public isolated`) |
| `function convertToArray(record {\|anydata...;\|} elementType, record {\|anydata...;\|}[] arr) returns elementType[];` (L207) | `utils.bal:19` `public isolated function convertToArray(typedesc<record {}> elementType, record {}[] arr) returns elementType[]` | **First param type wrong** — `typedesc<...>` lost (§5.3) |
| `function filterRecord(record {\|anydata...;\|} 'object, string[] fields) returns record {\|anydata...;\|};` (L209) | `utils.bal:23` | Matches (`record {}` ≡ `record {\|anydata...;\|}`) |
| `function getKey(anydata\|record {\|anydata...;\|} 'object, string[] keyFields) returns anydata\|record {\|anydata...;\|};` (L211) | `utils.bal:58` | Matches |

Doc comments for the four new error types are copied verbatim from `errors.bal:17,20,23,26`.
The README section (render L7–170) is byte-identical to `docs/README.md` in the bala (163 lines;
diff shows only one trailing blank line in the render).

Non-public functions `init()` and `setModule()` (`init.bal:19,23`) are correctly absent from both
renders.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full-file `diff -u` of old vs new: a single hunk at old 176–188 / new 176–192, `+8 / −4` lines,
  all additions, no deletions of content (the 4 removed lines are the `// Unknown type:` comments
  that the additions replace).
- Sorted declaration-set diff: 4 additions, **0 removals**, 0 modifications.
- README block (L1–171) byte-identical.
- Functions block (from `// --- Functions ---` to EOF) byte-identical — no parameter, default,
  return type, or doc text dropped.
- Normalised JSON diff: additive only (4 `baseType` keys), no key or array element removed.
- No `mod:x.y.z:Type` refs on either side (0/0), so no qualified-ref cleanup to lose.
- New render contains no truncation, no `// Unknown type:` lines, no empty declaration bodies.

## 5. Issues in `new` (independent of `old`)

**5.1 Error subtype hierarchy is flattened (new-only, but an improvement over old's silence).**
`errors.bal:21/24/27` declare `ConstraintViolationError`, `NotFoundError` and `AlreadyExistsError`
as `distinct Error` — subtypes of `persist:Error`. The extractor emits `"baseType": "error"` for
all four (JSON L161–180), and the renderer prints `type X error;`. Consequence for a consumer LLM:
`persist:Error` looks like a peer of the other three rather than their supertype, so patterns such
as `if e is persist:Error` after catching a `NotFoundError`, or `returns Foo|persist:Error`
covering the specific errors, are not derivable from the render. The `distinct` qualifier is also
absent. The renderer documents the `distinct` half of this as a known limitation
(`to-syntax-string.ts:400-402`: *"the rendered form omits `distinct`: the compiler reports `error`
for a `distinct error` declaration, and the qualifier cannot be recovered from the signature"*), and
the value comes from `TypeDefDataBuilder.java:114` (`default -> typeDescriptor.signature()`). Old
rendered nothing at all here, so this is net-positive, but it is not fully faithful.

**5.2 `AbstractPersistClient` is rendered as a `class` (pre-existing; present in both sides).**
Source is `public type AbstractPersistClient distinct object {};` — a distinct *object type*, not a
class, and it cannot be instantiated with `new`. Both renders emit `class AbstractPersistClient {}`
(L176–177), which invites `new persist:AbstractPersistClient()`. Root cause is the extractor's
`typeKind` switch mapping `OBJECT -> TypeCategory.CLASS` (`TypeDefDataBuilder.java:82`).

**5.3 `convertToArray`'s `typedesc` parameter is lost, making the rendered signature
non-compiling (pre-existing; identical in both sides).**
Source: `public isolated function convertToArray(typedesc<record {}> elementType, record {}[] arr)
returns elementType[]` (`utils.bal:19`). Both renders emit
`function convertToArray(record {|anydata...;|} elementType, record {|anydata...;|}[] arr) returns
elementType[];`. A dependently-typed return `elementType[]` is only legal when `elementType` is a
`typedesc` parameter, so as rendered this does not compile, and an LLM copying it would pass a
record value where a typedesc is required.

**5.4 `public` and `isolated` qualifiers are dropped on all declarations (pre-existing, both
sides).** All 10 public symbols lose `public`; the 5 functions lose `isolated`. `public` is
harmless at module-API level (everything rendered is public by construction), but the loss of
`isolated` means a caller cannot tell these are safe to call from an isolated context.

No invented symbols, no broken doc text, no encoding problems: all 5 doc-comment blocks in the new
render match the source comments character-for-character, and the file is clean UTF-8.

## 6. Coverage gaps vs. the library

**Zero gaps.** `package.json` in the bala lists `"export": ["persist"]` and `modules/` contains only
`persist` — there are no submodules, so the shared `getDefaultModule()` limitation does not bite
here. Central metadata for `ballerina/persist/1.7.0` likewise lists exactly one module (`persist`).

All 10 public declarations in the bala (`grep -nE '^public ' modules/persist/*.bal`) appear in the
new render: `AbstractPersistClient`, `Error`, `ConstraintViolationError`, `NotFoundError`,
`AlreadyExistsError`, `getNotFoundError`, `getAlreadyExistsError`, `convertToArray`,
`filterRecord`, `getKey`. The old render covers 6 of 10 as real declarations plus 4 as placeholder
names (name-only, no shape).

The module declares no annotations, no clients, no services and no listeners (`grep -c 'annotation '`
→ 0 in all four files; `annotations`/`clients`/`services` arrays empty in both JSONs), so those
empty sections are correct, not gaps.

## 7. Compiler plugin

`has_plugin: true` — confirmed: the bala contains
`compiler-plugin/compiler-plugin.json` and `compiler-plugin/libs/persist-compiler-plugin-1.7.0.jar`.
Source read at `compiler-plugin/src/main/java/io/ballerina/stdlib/persist/compiler/` (31 Java files).

What it contributes:
- **One code analyzer**, `PersistCodeAnalyzer` (`PersistCodeAnalyzer.java:36`), registering
  `PersistModelDefinitionValidator` on `MODULE_PART` and `IMPORT_PREFIX` syntax nodes. It validates
  the *data-model definition files under the project's `persist/` directory* — entity records must
  be closed, must have an identity field, no optional/defaultable/rest/nillable fields, supported
  simple types only, valid 1-1 / 1-n relations, per-datastore type support
  (`utils/ValidatorsByDatastore.java`).
- **29 diagnostic codes** (`DiagnosticsCodes.java`), 5 of them `INTERNAL` carriers and the rest
  `ERROR` (e.g. `PERSIST_201` "an entity should be a closed record", `PERSIST_401` "an entity cannot
  reference itself in a relation field").
- **12 code actions** registered in `PersistCompilerPlugin.getCodeActions()` (16 files in
  `codeaction/`, incl. 3 abstract bases and a name enum): `ChangeToClosedRecord`, `ChangeTypeToInt`
  / `String` / `Boolean` / `Float` / `Decimal` / `ByteArray`, `ChangeTypeNotNillable`,
  `SwitchRelationOwner`, `RemoveDiagnosticLocation`, `RemoveTextRange`, `AddSingleText`.

Nothing the plugin implies is missing from the render: it defines **no annotations**, no generated
public types, and no API surface of its own — it only constrains user-written model files, which are
outside the module's exported API. The render's empty `annotations` array is therefore correct. The
one thing a consumer would benefit from — the modelling rules the plugin enforces — is already
present in prose in the README section of both renders (entity/identity/nullable/relationship
rules, render L18–169).

## 8. Other considerations

- **Not deprecated.** Central reports `deprecated: null`, `deprecateMessage: ""`, pullCount 1080,
  published 2026-02-24, built with Ballerina `2201.12.0`. Post-1.0 stable version.
- **Size/token cost is trivial and dominated by the README**: 164 of the 211 lines (78%) are the
  README block; the actual API is 40 lines. The +4 lines cost is negligible for a real gain in
  usable API.
- **This module is foundational for the `persist` datastore family** (`persist.sql`,
  `persist.inmemory`, `persist.googlesheets`, and every `bal persist`-generated client), which
  return `persist:Error` and its subtypes. Getting the error names *and their doc comments* into the
  render (new) materially helps an LLM write correct `persist` error handling; the missing
  subtype relation (§5.1) is the remaining gap for that use case.
- The pinned version was independently confirmed `PIN_OK` in `versions.txt:199`
  (`ballerina/persist 1.7.0 1.7.0 1.7.0 PIN_OK`); I did not modify it.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 207, new 211 |
| 2 | `grep -c '^// Unknown type:'` both | old 4, new 0 |
| 3 | `grep -n '^// --- '` both | 4 markers each; Types at 173 both, Functions at 187 (old) / 191 (new) |
| 4 | `grep -cE '[a-z_]+:[0-9]+\.[0-9]+\.[0-9]+:'` both | 0 / 0 |
| 5 | sorted declaration-set `diff` | +4 error types, −0 |
| 6 | `diff <(sed -n '1,171p' old) <(sed -n '1,171p' new)` | identical |
| 7 | `diff` of `// --- Functions ---`→EOF | identical |
| 8 | normalised sorted JSON `diff` | only 4 `"baseType": "error"` added |
| 9 | JSON array lengths both sides | typeDefs 5/5, functions 5/5, clients 0/0, services 0/0, annotations 0/0 |
| 10 | `git clone --depth 1 --branch v1.7.0 …` | succeeded; HEAD `d98dcfd6`, 2026-02-24 |
| 11 | `diff` clone `ballerina/*.bal` vs bala `modules/persist/*.bal` (4 files) | SAME for all 4 |
| 12 | `diff` clone `ballerina/README.md` vs bala `docs/README.md` | SAME |
| 13 | `diff` render README block vs bala `docs/README.md` | only a trailing blank line |
| 14 | `grep -nE '^public ' bala modules/persist/*.bal` | 10 public decls (listed in §6) |
| 15 | `grep -c 'annotation '` on 4 bala `.bal` files | 0, 0, 0, 0 |
| 16 | `cat bala/package.json` | `"export": ["persist"]`, single module, java21 platform |
| 17 | `ls bala/modules` | only `persist` — no submodules |
| 18 | `curl api.central.ballerina.io/…/ballerina/persist/1.7.0` | version 1.7.0, modules `['persist']`, deprecated `None` |
| 19 | `ls bala/compiler-plugin` + `libs` | `compiler-plugin.json`, `persist-compiler-plugin-1.7.0.jar` |
| 20 | `find compiler-plugin -name '*.java' \| wc -l` | 31 |
| 21 | `PersistCompilerPlugin.java` `getCodeActions()` | 12 code actions |
| 22 | `grep -cE '^\s+[A-Z_0-9]+\(' DiagnosticsCodes.java` | 29 diagnostic codes |
| 23 | `PersistCodeAnalyzer.java:36` | one syntax-node analysis task on MODULE_PART / IMPORT_PREFIX |
| 24 | `to-syntax-string.ts:403-435` (new side, commit `bdc5c32c`) | `renderBaseTypeDefinition` now handles `Error`/`Other`; comment at L400-402 documents `distinct` loss |
| 25 | `TypeDefDataBuilder.java:79-117` (new side) | `OBJECT -> CLASS`; `default -> typeDescriptor.signature()` supplies `baseType` |
| 26 | `grep -n persist versions.txt` | line 199, `PIN_OK` |

## 10. Caveats and unverified items

- The local `new`-side checkout at `/Users/admin/Desktop/Check-PR-s/ballerina-vscode` is currently at
  commit `bdc5c32c` on branch `L1_json_and_annotations_with_spec_v2`, whereas the brief states the
  renders were produced at `412ba01e` on that branch. The renderer/extractor code I cite in §5.1 and
  evidence rows 24–25 is therefore read from a *later* commit on the same branch; the cited
  behaviour is consistent with the JSON and render actually present, but I did not check out
  `412ba01e` to confirm those exact lines existed then. All conclusions in §2–§4 rest on the render
  and JSON files themselves, not on that source.
- §5.1's claim that the Ballerina semantic API reports `error` (rather than `Error`) for a
  `distinct Error` declaration is taken from the renderer's own source comment plus the observed
  JSON value; I did not run the extractor to confirm the mechanism independently.
- I did not compile the rendered `.bal.txt` — the §5.3 non-compiling claim is based on reading the
  Ballerina spec rule that dependently-typed returns require a `typedesc` parameter, not on a
  compiler run.
- Everything else in this report was verified directly against files or command output.

# ballerinax/asana 3.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/asana` |
| Pinned version | `3.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-asana |
| Tag reviewed | `v3.0.1` (exact match; peeled commit `93f244aae78ec5c8a482e2f6329588de8c6e3ae8`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/asana/3.0.1` |
| Old render | `7484` lines |
| New render | `8270` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`asana` is a single-module OpenAPI-generated connector (default module `asana`; bala `modules/` contains
only `asana/` with `client.bal`, `types.bal`, `utils.bal`). The upstream tag `v3.0.1` sources are
byte-identical to the bala sources, so GitHub and the bala agree everywhere.

The declaration inventory is **identical** on both sides: 613 named type definitions plus 1 client class,
matching the bala's 613 public type declarations plus `public isolated client class Client` exactly. Nothing
was added or removed. The entire +1009/−223 line delta is accounted for by three changes, all of them
strict improvements:

1. **786 annotation lines restored** (`@jsondata:Name` ×341, `@http:Query` ×395, `@constraint:Int` ×49,
   `@display` ×1). `old` emitted none of these. Every rendered annotation multiset matches the bala exactly.
2. **182 bogus `anydata Additional Values` parameters removed** from client resource-function signatures.
   `old` injected this non-compiling pseudo-parameter (an identifier containing a space) into 182 of the
   184 resource functions.
3. **40 version-qualified type references** (`ballerinax/asana:3.0.1:UserCompact`) collapsed to plain names,
   and **18 Ballerina-keyword field names correctly escaped** (`public` → `'public`, `type` → `'type`,
   `resource` → `'resource`, `external` → `'external`, `source` → `'source`), matching the bala source.

No regression of any kind was found. Zero `// Unknown type:` placeholders on either side.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 7484 | 8270 |
| Section markers (`// --- `) | 4 | 4 |
| `// Unknown type:` | 0 | 0 |
| Named declarations (`type`/`class`/`enum`/`const`/`annotation`/`function`) | 613 | 613 |
| Client classes | 1 | 1 |
| `resource function` members | 184 | 184 |
| Doc-comment lines (`^\s*#`) | 1772 | 1772 |
| `@jsondata:Name` | 0 | 341 |
| `@http:Query` | 0 | 395 |
| `@constraint:Int` | 0 | 49 |
| `@display` | 0 | 1 |
| `@deprecated` | 3 | 3 |
| Version-qualified type refs (`ballerinax/asana:3.0.1:`) | 40 (22 lines) | 0 |
| `anydata Additional Values` pseudo-params | 182 | 0 |
| `// Special Agent Note:` cross-package hints | 17 | 17 |

Unified diff: 371 hunks, 1009 lines added, 223 lines removed (net +786 = exactly the 786 new annotation
lines; the 223 removals are all in-place modifications with a paired addition).

**Declarations added: 0. Declarations removed: 0.** Verified by extracting and sorting every top-level
declaration line from both files: both sets have 613 entries and `diff` reports only two differing lines,
both being the version-qualifier cleanup:

```
< type MembershipCompact ballerinax/asana:3.0.1:GoalMembershipCompact|ballerinax/asana:3.0.1:ProjectMembershipCompactResponse;
> type MembershipCompact GoalMembershipCompact|ProjectMembershipCompactResponse;
< type MembershipResponse ballerinax/asana:3.0.1:GoalMembershipResponse|ballerinax/asana:3.0.1:ProjectMembershipCompactResponse;
> type MembershipResponse GoalMembershipResponse|ProjectMembershipCompactResponse;
```

### Section-by-section

- **Header + README (lines 1–106)**: byte-identical between `old` and `new`. Both contain the complete
  96-line bala `docs/README.md` verbatim (only difference vs. the file is the missing trailing newline).
- **Types (old 107–6742 / new 107–7528)**: after stripping the `ballerinax/asana:3.0.1:` qualifier from
  `old` and the 786 new annotation lines from `new`, both sides reduce to 6636 lines and `diff` reports
  exactly **18 changed lines**, all keyword-escaping fixes. No other content change whatsoever.
- **Client (old 6743–end / new 7529–end)**: after deleting the literal string `anydata Additional Values, `
  from `old`, `diff` reports **0 differences**. The client section changed in exactly one way.

## 3. Correctness against library source

Upstream tag and bala are identical, so both were used interchangeably:

```
diff -q <clone>/ballerina/{client,types,utils}.bal  <bala>/modules/asana/{client,types,utils}.bal
→ client.bal: IDENTICAL   types.bal: IDENTICAL   utils.bal: IDENTICAL
```

Annotation restoration verified exhaustively, not by sampling:

| Annotation | bala `types.bal` | `new` render | Match |
|---|---|---|---|
| `@http:Query {...}` (exact multiset of argument text) | 395 | 395 | identical multiset (`diff` empty) |
| `@constraint:Int {...}` (exact multiset) | 49 | 49 | identical multiset (`diff` empty) |
| `@jsondata:Name {value: "..."}` (exact multiset) | 340 | 341 | 340 identical; the one extra is `"task_resource_subtype"` (explained below) |
| `@deprecated` | 3 | 3 | ✓ |
| `@display {label: "Connection Config"}` | 1 | 1 | ✓ |

The single `@jsondata:Name` surplus is not an invention: bala declares
`public type TaskTemplateRecipeCompact TaskTemplateRecipeCompactAllOf1;` (types.bal:3828, alias of the
record at types.bal:4393). Both renders expand the alias into a second full record body, so the annotation
appears twice. `old` did the same expansion (old:3454 and old:3462), so this is shared, pre-existing
renderer behaviour, not new.

Spot checks of restored content against source:

- `ProjectBaseAllOf2` — new:117–180 vs bala types.bal:98–153. Every `@jsondata:Name` value
  (`start_on`, `custom_field_settings`, `default_access_level`, `due_date`, `created_at`, `due_on`,
  `privacy_setting`, `minimum_access_level_for_sharing`, `html_notes`, `current_status_update`,
  `minimum_access_level_for_customization`, `current_status`, `modified_at`, `default_view`) matches
  position-for-position, as does `@deprecated` on `'public`.
- `AsanaResource` — new:116–121 vs bala types.bal (`@jsondata:Name {value: "resource_type"}` on
  `resourceType`). Correct.
- `@constraint:Int {minValue: 1, maxValue: 100}` on `int 'limit?` — new:855 vs bala types.bal:89. Correct.
- `@display {label: "Connection Config"}` on `ConnectionConfig` — new:5487 vs bala types.bal:3241. Correct.
- `GetAttachmentQueries` (`opt_fields`, `opt_pretty` `@http:Query` names) — new render vs bala
  types.bal:4373–4381. Correct.

Keyword escaping verified against the bala: bala has **zero** unescaped keyword-named record fields
(`grep -nE "^\s+[^ ]+ (type|public|resource|external|source)\?;" types.bal` → 0 matches), and uses
`'resource?` (types.bal:1972, 2307, 4431), `'external?` (2206), `'source?` (4980), `'public?` (133),
`'limit?` (90). `new` reproduces all of these; `old` emitted 16 of them unescaped at top level.

Client surface: all 184 resource functions in bala `client.bal` are present in both renders with matching
paths, and after removing the bogus parameter the two client sections are byte-identical, so every
signature `new` shows was already validated in `old` and matches the bala's method list.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. Declaration-set diff (613 vs 613, only the two version-qualifier lines differ) — nothing dropped.
2. Type-section normalized diff (`old` minus version qualifiers vs `new` minus new annotation lines):
   6636 lines each, 18 differing lines, all of which are `X` → `'X` keyword escapes that make `new` *more*
   correct. Zero lines present in `old` and absent from `new`.
3. Client-section diff after neutralising the `anydata Additional Values, ` string: **0 differences**.
4. Doc-comment line count identical (1772 / 1772); README section byte-identical; `// Special Agent Note:`
   cross-package hints identical (17 / 17); `@deprecated` markers identical (3 / 3).
5. All 40 version-qualified refs removed were replaced by the correct bare type name; each replacement was
   inspected in the 223-line removal set and every removed line has a paired, semantically equal or better
   added line.
6. No `// Unknown type:` placeholder appears in either render (0 / 0), so spec v2's degraded-type fix is
   not exercised here and cannot have side effects.

## 5. Issues in `new` (independent of `old`)

All five items below are present in `new`; **all five are also present in `old`** — none is introduced by
spec v2. They are recorded because they still mislead a consuming LLM.

1. **Annotations are lost through type inclusion.** Restored annotations only appear where the field is
   declared directly in that record's own source. Because both renderers flatten `*Included;` into
   effective fields, inherited fields lose their wire-name annotation. Measured: `new` has 123 top-level
   `string resourceType?;` fields but only **8** carry `@jsondata:Name {value: "resource_type"}` — the
   same 8 the bala declares literally; the other 115 inherit it from `*AsanaResource`. Example:
   `StatusUpdateCompact` (bala types.bal:4535 = `*AsanaResource; *StatusUpdateCompactAllOf2;`) renders at
   new:454–459 with bare `string resourceType?;`. An LLM would serialize `resourceType` instead of
   `resource_type` for those 115 fields. (`old` was worse: 0 of 123.)
2. **Included-record client parameters render as non-compiling signatures.** The bala declares
   `resource isolated function get attachments/[string attachmentGid](map<string|string[]> headers = {}, *GetAttachmentQueries queries)`
   (client.bal:43). Both renders flatten the record's fields into defaultable positional parameters *and*
   then append `GetAttachmentQueries queries` without the `*` — a required parameter after defaultable
   ones, which does not compile. Affects 182 of 184 resource functions. The invented defaults
   (`optFields = []`, `optPretty = false`, `limit = 0`, `offset = ""`) do not exist in the source either;
   the fields are simply optional.
3. **Two unescaped keyword fields remain inside inline record type text** (new:219 and new:438, both the
   flattened `customField` record: `... "text"|"enum"|... type?; ...`). Top-level fields are now escaped,
   but the inline-record serializer is not. Identical defect in `old`.
4. **Closed records are rendered as open.** bala declares 2 closed records (`record {| ... |}`, incl.
   `ConnectionConfig` at types.bal:3242); both renders emit `record { ... }`. Shared.
5. **Annotation prefixes are used without imports.** The render's only import is `import ballerinax/asana;`,
   yet `new` now emits `@jsondata:`, `@constraint:` and `@http:` prefixes (`old` already emitted `http:`
   type refs the same way). Cosmetic for a reference stub, but the snippet is not directly compilable.
   The render does carry `// Special Agent Note: ... FROM ballerina/http package` hints (17 of them) for
   `http:` types, but no equivalent hint for the annotation modules.

Additionally, resource-function parameter docs (`# + attachmentGid - ...`) are dropped by both renders,
leaving a bare `# ` line under each summary. Shared, unchanged.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

```
public (isolated )?(type|class|const|enum|annotation|function|listener) NAME  in bala modules/asana/*.bal → 613 unique names
same extraction from new/ballerinax_asana.bal.txt                            → 613 unique names
comm -23 (bala-only) → empty      comm -13 (render-only) → empty
```

`public isolated client class Client` (client.bal:25) is additionally present in both renders. `utils.bal`
exports nothing public (`grep '^public' utils.bal` → no matches), so nothing is missed there.

No submodule gap: the bala's `modules/` directory contains only `asana`, and `package.json` `"export"` is
`["asana"]`, i.e. the default module is the entire public surface. The known `getDefaultModule()`-only
limitation does not apply to this library.

## 7. Compiler plugin

**None.** The upstream repo at `v3.0.1` has no `compiler-plugin` directory
(`find <clone> -iname '*compiler-plugin*'` → no results), `ballerina/Ballerina.toml` declares no
`[[platform.*.dependency]]` or plugin entry, and the bala contains no `compiler-plugin/` directory
(bala `any/` holds only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`).
Nothing plugin-derived is expected in the render, and nothing is missing.

## 8. Other considerations

- **Deprecations**: 3 `@deprecated` markers, all preserved in both renders (`'public` fields on
  `ProjectBaseAllOf2` and siblings). The doc bodies retain the `*Deprecated:*` prose.
- **Version stability**: 3.0.1 is a stable major release; `graalvmCompatible: true`; built for
  `ballerina_version 2201.12.2`, `distribution = "2201.12.0"`. No deprecation flag on the package.
- **Size/token cost**: `new` is 703 KB / 8270 lines vs `old` 676 KB / 7484 lines — a ~4 % byte increase
  for a large accuracy gain (786 annotation lines carrying wire field names and query-parameter names,
  which are otherwise unrecoverable by a consumer). This is a good trade: without `@jsondata:Name` and
  `@http:Query` an LLM cannot produce correct Asana API payloads or query strings from the record fields
  alone, since almost every field is camelCase-renamed from snake_case.
- **JSON stage**: both `old` and `new` JSONs carry the same shape — `typeDefs: 613`, `clients: 1`,
  `functions: 0`, `services: 0`, `annotations: 0`. The extra ~110 KB in the `new` JSON is the annotation
  metadata. No structural key change.
- **Doc quality**: doc text is verbatim from the OpenAPI description fields and contains raw newlines
  inside single doc comments (e.g. the `modified_at` description spans two render lines with the second
  unprefixed). Identical in both renders; pre-existing.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags .../module-ballerinax-asana` | tags `v2.0.0`, `v3.0.0`, `v3.0.1`; exact match `v3.0.1` |
| `git clone --depth 1 --branch v3.0.1` | succeeded |
| `diff -q <clone>/ballerina/{client,types,utils}.bal <bala>/modules/asana/*.bal` | all three IDENTICAL |
| `ls <bala>/any/modules` | `asana` only → single-module package |
| `<bala>/any/package.json` | `"export": ["asana"]`, version `3.0.1`, `graalvmCompatible: true` |
| `wc -l` both renders | 7484 / 8270 |
| `grep -c '^// Unknown type:'` | 0 / 0 |
| `grep -n '^// --- '` | both: README 7, END README 105, Types 107, Client 6743 (old) / 7529 (new) |
| declaration extraction + `diff` | 613 / 613; only 2 lines differ (version qualifiers) |
| `grep -c '^    resource function'` | 184 / 184; bala client.bal: 184 |
| `grep -c 'anydata Additional Values'` | old 182, new 0; the 2 old fns without it are the 2 with no `*Queries` param |
| client-section `diff` after `sed 's/anydata Additional Values, //'` | **0 lines of difference** |
| types-section `diff` after stripping qualifiers/annotations | 6636 vs 6636 lines, 18 changed lines, all `X?;` → `'X?;` |
| the 18 escapes | `type`×5, `public`×8, `resource`×2, `external`×2, `source`×1 |
| `grep -c 'ballerinax/asana:3.0.1:'` | old 40 occurrences / 22 lines; new 0 |
| annotation counts new vs bala | jsondata 341/340, http:Query 395/395, constraint 49/49, display 1/1, deprecated 3/3 |
| `diff` of `@http:Query {...}` multisets (new vs bala) | identical |
| `diff` of `@constraint:Int {...}` multisets (new vs bala) | identical |
| `diff` of `@jsondata:Name {...}` multisets (new vs bala) | 1 diff: `task_resource_subtype` 2 vs 1 (alias expansion, also in old) |
| `diff` README region (lines 1–106) old vs new | identical; vs bala `docs/README.md` (96 lines): identical modulo trailing newline |
| `grep -c '^\s*#'` doc lines | 1772 / 1772 |
| `grep -c 'Special Agent Note'` | 17 / 17 |
| symbol coverage `comm` bala vs new | both directions empty → 0 gaps |
| `grep -nE "^\s+[^ ]+ (type\|public\|resource\|external\|source)\?;"` in bala | 0 (bala escapes everything) |
| same grep in old render / new render | 16 / 0 |
| `grep -c " type?;"` (inline records) | old 7 lines (5 top-level + 2 inline), new 2 (inline only) |
| `resourceType?` annotation coverage in new | 123 fields, 8 annotated (bala declares 8 literally, 115 via inclusion) |
| `find <clone> -iname '*compiler-plugin*'` | no results |
| JSON key/shape comparison | both: typeDefs 613, clients 1, functions 0, services 0, annotations 0 |
| unified diff stats | 371 hunks, +1009 / −223 |

## 10. Caveats and unverified items

- The renders were **not compiled**. Claims about non-compiling syntax (the flattened `*Queries`
  parameters, the two unescaped inline `type?` fields) are based on reading the Ballerina grammar rules,
  not on running `bal build`. The `anydata Additional Values` case is unambiguous (an identifier containing
  a whitespace), so no compilation was needed there.
- Annotation-restoration correctness was verified by exact multiset comparison of the rendered annotation
  text against the bala plus targeted position checks on 5 records. Per-field positional binding was **not**
  verified for all 786 annotations individually; a mis-attached annotation that preserved the global
  multiset would not have been caught, though the 5 records inspected in full (`ProjectBaseAllOf2`,
  `AsanaResource`, `GetAttachmentQueries`, `ConnectionConfig`, `PaginationQueries`/`'limit`) were all
  correct position-for-position.
- Ballerina Central registry metadata was not re-queried over the network; package identity, version,
  keywords, export list and deprecation status were taken from the bala's `package.json`, which is the
  authoritative artifact the extractor consumed.
- The `ballerina-vscode` renderer sources for the two sides were not read; conclusions about *why* a
  difference exists (e.g. alias expansion, inclusion flattening) are inferred from the rendered output and
  the bala source, and are labelled as such.

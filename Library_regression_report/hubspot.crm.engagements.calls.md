# ballerinax/hubspot.crm.engagements.calls 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.engagements.calls` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.engagements.calls |
| Tag reviewed | `v2.0.2` (exact match; annotated tag `bd9a833`, commit `912f585`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.engagements.calls/2.0.2` |
| Old render | `826` lines |
| New render | `827` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. `diff -u` reports 15 hunks, 16 added lines, 15 removed lines. No
declaration is added or removed on either side: both renders carry exactly the same 41 type
definitions, one client class, and 12 resource functions plus `init`.

`new` changes three things, all fixes:

1. Strips version/module qualification from type references — 11 occurrences in `old`
   (`ballerina/lang.int:0.0.0:Signed32` ×7, `ballerinax/hubspot.crm.engagements.calls:2.0.2:<T>` ×4)
   become plain `int:Signed32` / `<T>`; 0 remain in `new`.
2. Drops the bogus `anydata Additional Values` parameter that `old` emitted for the rest field of
   open included-record query parameters (4 occurrences in `old`, 0 in `new`). That token was
   syntactically invalid Ballerina (a parameter name containing a space).
3. Emits the `@display {label: "Connection Config"}` annotation on `ConnectionConfig`, which is
   genuinely present in the published source (`types.bal:232`) and was absent from `old`.

Nothing is lost. The README block (lines 8–240) is byte-identical between the two renders, and the
JSON `readme` field is identical (10,638 chars both sides). No `// Unknown type:` placeholders on
either side (0 / 0), so this library was not affected by the spec-v2 degraded-type fix.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 826 | 827 |
| `// --- ` section markers | 4 | 4 |
| `// Unknown type:` placeholders | 0 | 0 |
| Top-level `type ` declarations | 41 | 41 |
| Client classes | 1 | 1 |
| Client functions (JSON) | 12 | 12 |
| Module/version-qualified type refs | 11 | 0 |
| `Additional Values` pseudo-params | 4 | 0 |
| `@display` annotations | 0 | 1 |
| JSON `typeDefs` / `functions` / `services` | 41 / 0 / 0 | 41 / 0 / 0 |

**Declarations added: 0. Declarations removed: 0.** Verified by set-comparing the sorted
`^type <Name>` lists from both renders — `diff` returns empty, both sets are 41 names.

Modified declarations, by kind:

| Kind | Count | Change |
|---|---|---|
| Record type (field type ref de-qualified) | 11 field lines across 10 records | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (7); `record {\|ballerinax/…:2.0.2:T…\|}` → `record {\|T…\|}` (4) |
| Record type (annotation added) | 1 (`ConnectionConfig`) | `+@display {label: "Connection Config"}` |
| Client resource function (param removed) | 4 | `anydata Additional Values` dropped |

The 4 affected resource functions: `post batch/read`, `get [string callId]`,
`patch [string callId]`, `get ` (getPage). Confirmed at the JSON level — parameter tuples are
identical between `old` and `new` except for the removal of `('Additional Values','anydata',None)`.

Return types, descriptions, and every other parameter are unchanged: a per-function JSON comparison
of `return` and `description` produced no diffs.

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's
`modules/hubspot.crm.engagements.calls/{client,types,utils}.bal` (`diff` → identical for all three),
so GitHub and the bala agree; no tie-break needed.

Checks on what `new` changed:

- `int:Signed32` — the bala uses exactly `int:Signed32` at `types.bal:111, 177, 206, 290, 316, 344,
  380` (7 occurrences). `new` renders `int:Signed32` in all 7 places. `old`'s
  `ballerina/lang.int:0.0.0:Signed32` was a rendering artefact, not source text. **`new` correct.**
- `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}` — source
  `types.bal` declares these inline rest-field maps unqualified. **`new` correct.**
- `@display {label: "Connection Config"}` on `ConnectionConfig` — present verbatim at
  `types.bal:232`, immediately above `public type ConnectionConfig record {|` at `types.bal:233`.
  It is the only annotation in the whole module (`grep -n '@display\|@constraint\|annotation '` on
  the bala returns exactly that one line). **`new` correct, `old` was missing it.**
- Removal of `anydata Additional Values` — the four affected functions take included-record
  parameters (`*PostCrmV3ObjectsCallsBatchReadReadQueries queries` at `client.bal:47`,
  `*GetCrmV3ObjectsCallsCallIdGetByIdQueries queries` at `client.bal:67`,
  `*PatchCrmV3ObjectsCallsCallIdUpdateQueries queries` at `client.bal:100`,
  `*GetCrmV3ObjectsCallsGetPageQueries queries` at `client.bal:170`). Those records are open
  (`record { … }`, not `record {| … |}`), so the extractor was surfacing the implicit `anydata`
  rest field as a named parameter. No such parameter exists in the source. **`new` correct.**

Client surface, exhaustively cross-checked (small library, 13 members):
`init` (`client.bal:31`), `post batch/read` (47), `get [callId]` (67), `delete [callId]` (84),
`patch [callId]` (100), `post batch/archive` (118), `post batch/create` (135),
`post batch/update` (152), `get .` (170), `post .` (186), `post batch/upsert` (203),
`post search` (220). All 12 resource functions plus `init` appear in both renders with matching
payload types and return unions.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full `diff -u old new` read end-to-end (15 hunks, all listed in §2). Every removed line has a
  corresponding added line that is strictly more accurate, except hunk 7 which is a pure addition.
- Declaration-set comparison: 41 type names in `old`, 41 in `new`, `diff` empty.
- JSON structural comparison: identical top-level keys, identical counts for `typeDefs` (41),
  `clients` (1), `functions` (0), `services` (0), `annotations` (0).
- Per-function JSON parameter/return/description comparison across all 12 client functions — only
  the `Additional Values` removals differ.
- README: `sed -n '8,240p'` of both renders is identical; JSON `readme` strings compare equal.
- No parameter default, return type, or doc line is dropped anywhere in `new`.

## 5. Issues in `new` (independent of `old`)

These are fidelity gaps present in `new` and equally present in `old` — pre-existing extractor
behaviour, not caused by spec v2. Listed because they would mislead an LLM consuming the render.

1. **Included-record query params are both flattened and duplicated.** `new:817`
   renders `resource function get (map<string|string[]> headers = {}, string[] associations = [],
   boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0,
   string after = "", string[] properties = [], GetCrmV3ObjectsCallsGetPageQueries queries)`.
   The source (`client.bal:170`) has only `(map<string|string[]> headers = {},
   *GetCrmV3ObjectsCallsGetPageQueries queries)`. The render lists the record's fields as separate
   parameters *and* the record itself, which is not valid Ballerina and suggests an argument list
   that will not compile. Same for `post batch/read`, `get [callId]`, `patch [callId]`.

2. **Invented / wrong defaults on those flattened params.** `limit = 0` — the source default is
   `'limit = 10` (`types.bal:290`). `idProperty = ""`, `associations = []`, `properties = []`,
   `propertiesWithHistory = []` — these fields are optional with *no* default in the source
   (`types.bal:284, 288, 292, 158, 162`). Only `archived = false` matches.

3. **Record-field defaults dropped; defaulted fields rendered optional.** Source
   `boolean archived = false;` (`types.bal:286`, `:158`) renders as `boolean archived?;`
   (`new:638`, `new:518`); source `int:Signed32 'limit = 10;` (`types.bal:290`) renders as
   `int:Signed32 'limit?;` (`new:643`). The default value is lost and required-with-default becomes
   optional.

4. **Empty resource path rendered without `.`** — `new:817` and `new:821` emit
   `resource function get (` and `resource function post (`; the source is `get .(` / `post .(`
   (`client.bal:170`, `:186`). As written this is not parseable.

5. **Closed records rendered as open.** `OAuth2RefreshTokenGrantConfig` (`types.bal:191`),
   `ConnectionConfig` (`types.bal:233`) and `ApiKeysConfig` (`types.bal:492`) are declared
   `record {| … |}`; all three render as `record { … }` (0 top-level `record {|` in either render).
   Inline rest-field records are preserved correctly (19 `record {|` lines in both renders).

6. **Visibility / isolation qualifiers dropped.** `public isolated client class Client`
   (`client.bal:23`) renders as `client class Client` (`new:781`); `public isolated function init`
   (`client.bal:31`) renders as `function init` (`new:782`); all `resource isolated function`
   render as `resource function`; all `public type` render as `type`.

None of these are new in this change set — all six are byte-identical in `old`.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

The bala exposes a single module (`modules/hubspot.crm.engagements.calls`, matching
`"export": ["hubspot.crm.engagements.calls"]` in `package.json`), which *is* the default module, so
the `getDefaultModule()`-only extraction limitation does not bite here — there are no submodules.

- Public types in the bala: 41. Types in `new` render: 41. `comm -23` (bala minus render) → empty;
  `comm -13` (render minus bala) → empty. Exact 1:1, no invented symbols.
- Public client class: 1 in bala, 1 in render.
- Public module-level functions / constants / enums / annotations / listeners / services in the
  bala: none (`grep "^public \(const\|function\|isolated function\|enum\|annotation\|listener\)"`
  returns nothing). Render correspondingly has 0.

## 7. Compiler plugin

The package ships **no compiler plugin**. `find` over the cloned `v2.0.2` tree for
`*compiler-plugin*` / `*plugin*` returns nothing, `Ballerina.toml` has no `[[plugin]]` or
`[compiler-plugin]` section, and the bala root contains only
`bala.json, dependency-graph.json, docs, modules, package.json` — no `compiler-plugin/`
directory and no `compiler-plugin.json`.

Consequently there are no plugin-generated code actions, validations, or artefacts that could be
missing from the render.

## 8. Other considerations

- **Not deprecated, stable major.** `2.0.2`, `graalvmCompatible: true`, built with Ballerina
  `2201.12.2` (bala `package.json`); `Ballerina.toml` declares `distribution = "2201.12.0"`.
- **Size.** 826 → 827 lines (+1, +0.12%). Token impact is negligible; the de-qualification actually
  makes 11 lines shorter.
- **Doc quality is good.** All 41 typeDefs have a non-empty `description` in the JSON (checked
  programmatically: 0 empty). Field-level doc comments are carried through. Resource-function docs
  are one-liners (`# Retrieve a call`) followed by an empty `# ` line — cosmetic, both sides.
- **Source integrity.** Upstream tag `v2.0.2` and the published bala are byte-identical for all
  three `.bal` files, so the render was produced from exactly the code on GitHub.
- The `ConnectionConfig.auth` line carries the pipeline's `// Special Agent Note: BearerTokenConfig
  FROM ballerina/http package` marker in both renders — unchanged.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 826 / 827 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; `Client` at old:778, new:779 |
| `diff -u old new` (read in full) | 15 hunks, +16 / −15 |
| `grep -cE '[a-z]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 11, new 0 |
| `grep -c 'Additional Values'` | old 4, new 0 |
| `grep -c '@display'` | old 0, new 1 |
| `grep -o '^type [A-Za-z0-9_]*' \| sort` → `diff` | 41 / 41, identical sets |
| `grep -h '^public type' bala/*.bal \| awk '{print $3}' \| sort` | 41 names |
| `comm -23 bala_types render_types` / `comm -13` | empty / empty |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`bd9a833` → `912f585`) |
| `git clone --depth 1 --branch v2.0.2` | success |
| `diff src/ballerina/{client,types,utils}.bal bala/modules/…/` | identical ×3 |
| `grep -n '@display\|@constraint\|annotation ' bala/*.bal` | one hit: `types.bal:232` |
| `grep -n 'int:Signed32' bala/types.bal` | 7 hits: lines 111, 177, 206, 290, 316, 344, 380 |
| `grep -n 'resource isolated function' bala/client.bal` | 12 resource fns + `init` at :31 |
| JSON top-level keys both sides | `annotations, clients, description, functions, name, readme, services, typeDefs` |
| JSON counts | typeDefs 41/41, clients 1/1, client functions 12/12, functions 0/0, services 0/0 |
| JSON `readme` equality | `True`, 10638 chars both |
| JSON `description` equality | `True` |
| JSON `ConnectionConfig.annotations` | old `None`; new `[{'name':'display','value':'{label: "Connection Config"}'}]` |
| Per-function JSON param/return/desc diff | only `('Additional Values','anydata',None)` removed, in `get` (getPage) and `patch` groups |
| `sed -n '8,240p'` README diff | identical |
| `grep -c 'record {\|'` renders | 19 / 19 (inline preserved); 0 / 0 top-level |
| `find src -iname '*compiler-plugin*'` | no results |
| `ls bala/2.0.2/any` | `bala.json dependency-graph.json docs modules package.json` |
| `ls bala/…/modules` | single module `hubspot.crm.engagements.calls` |
| `cat bala/package.json` | version 2.0.2, `export: ["hubspot.crm.engagements.calls"]`, ballerina_version 2201.12.2 |

## 10. Caveats and unverified items

- The pinned version was confirmed from the bala `package.json` (`"version": "2.0.2"`) and the
  upstream `Ballerina.toml` (`version = "2.0.2"`), not by re-querying Ballerina Central; the
  Central registry endpoint was not called for this review. The bala and the tag agree, so the
  version is not in doubt.
- I did not compile either render. Statements that particular constructs "will not compile"
  (§5 items 1 and 4) are read off the Ballerina grammar — a parameter list containing both a
  record's flattened fields and the record, and `resource function get (` with an empty resource
  path — rather than from a compiler run.
- `old`'s `anydata Additional Values` is interpreted as the open-record rest field of the included
  record parameter. That interpretation matches the facts (it appears on exactly the 4 functions
  with `*Queries` included-record params, and all 4 `*Queries` records are open) but I did not read
  the `old` extractor source to confirm the mechanism.
- The two `ballerina-vscode` source trees that produced the renders were not inspected; the review
  is based on the render/JSON artefacts and the library source only.

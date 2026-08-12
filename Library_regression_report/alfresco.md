# ballerinax/alfresco 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/alfresco` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-alfresco |
| Tag reviewed | `v2.0.2` (annotated; peels to `bcb3747c170800aa3dc09870c13d6cc8b213670f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/alfresco/2.0.2/any` |
| Old render | `4567` lines |
| New render | `4654` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The delta between `old` and `new` is exactly two things, and both are improvements:

1. **87 annotation lines added** — `@constraint:Int` (69), `@http:Header` (17), `@display` (1). These
   were completely absent from `old` (`grep -c 'constraint:' old` → 0). The multiset of annotation
   name+value pairs in `new` matches `modules/alfresco/types.bal` in the bala **exactly**
   (35×`{minValue: 0}`, 34×`{minValue: 1}`, 9×`{name: "If-Modified-Since"}`, 8×`{name: "Range"}`,
   1×`{label: "Connection Config"}`), and a pairwise ordered comparison of
   (annotation, value, annotated declaration) over all 87 sites produced **0 mismatches**.
2. **108 client method signatures repaired** — `old` emitted a synthetic parameter rendered as the
   syntactically invalid token sequence `anydata Additional Values` in every method that takes an
   included `*XQueries queries` record. `new` drops it. 108 of 142 remote methods were affected;
   108 is also the exact count of `*…Queries queries` parameters in `client.bal`.

Arithmetic closes exactly: 108 removed lines + 195 added lines, where 195 = 108 rewritten signatures
+ 87 annotations, and 4654 − 4567 = 87. **No other line in the file changed** — no declaration was
added, removed, reordered, or reworded; the README block is byte-identical; type and method name sets
are identical.

Nothing was lost. There are **zero regressions**. `new` is strictly more accurate.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 4567 | 4654 |
| `// Unknown type:` placeholders | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `type` declarations | 295 | 295 |
| `client class` | 1 | 1 |
| `remote function` declarations | 142 | 142 |
| `function init` | 1 | 1 |
| Annotation lines (`@constraint:Int` / `@http:Header` / `@display`) | 0 | 69 / 17 / 1 |
| Signatures containing `anydata Additional Values` | 108 | 0 |
| Record fields carrying a default value | 0 | 0 |

Declaration-set diff (`diff <(grep -oE '^type …' old \| sort -u) <(… new)`) → **identical**, 295 names
on both sides. Remote-method name set diff → **identical**, 142 names on both sides.

Declarations added: **0**. Declarations removed: **0**. Declarations modified: **108** remote
functions (parameter list) + **45** type definitions (annotations attached to 87 sites).

### JSON-level inventory (authoritative, from the two `.json` files)

- Top-level shape identical: `typeDefs` 295 → 295, `clients` 1 → 1, `functions` 0 → 0,
  `services` 0 → 0, `annotations` 0 → 0.
- `typeDefs`: 45 differ. Stripping `annotations` keys from every typeDef and field makes
  **all 295 byte-identical** → the *only* typeDef change is added annotations.
  Annotation objects: old **0**, new **87**.
- Client functions: 143 entries (142 remote + `init`), names identical. 108 differ. Removing the
  parameter named `"Additional Values"` from each old function makes **all 108 byte-identical**
  → the *only* client change is removal of that synthetic parameter.
- New JSON is *smaller* (656,282 B vs 665,472 B) despite the added annotations, because the 108
  removed parameter objects outweigh them.

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's
`modules/alfresco/{client,types,utils}.bal` (`diff -q` → same for all three). GitHub and the bala
agree, so all checks below hold against both.

**Annotations (exhaustive, all 87 sites):** a script extracted every
`@constraint:Int|@http:Header|@display {…}` line and the declaration it annotates (skipping doc
comments) from `types.bal` and from `new/ballerinax_alfresco.bal.txt`. Both produced 87 entries; a
positional zip comparison gave **0 mismatches**. Spot-verified anchor: `types.bal:24-54`
`public type FindPeopleQueries record { … @constraint:Int {minValue: 1} int maxItems = 100; …
@constraint:Int {minValue: 0} int skipCount = 0; }` ↔ `new` lines 83-115. `types.bal:367-368`
`@display {label: "Connection Config"} public type ConnectionConfig record {|` ↔ `new` line ~671.

**Signature repair:** `client.bal:44`
`remote isolated function listComments(string nodeId, map<string|string[]> headers = {}, *ListCommentsQueries queries) returns CommentPaging|error`.
There is no rest/extra parameter in the source. `old` invented `anydata Additional Values`; `new`
does not. The source's `ListCommentsQueries` (`types.bal:595-616`) is an **open** record
(`record {` — 108 of 108 `*Queries` records are open, 0 closed), which is where the extractor's
synthetic "Additional Values" rest descriptor came from; suppressing it is correct for a rendered
signature.

**Symbol coverage:** 295 `^public type` in `types.bal` vs 295 `^type` in `new` → `comm` both ways
returns empty. 142 `remote isolated function` in `client.bal` vs 142 `remote function` in `new` →
`comm -3` empty. `client.bal:26 public isolated client class Client` and `client.bal:33 public
isolated function init(ConnectionConfig config, string serviceUrl) returns error?` both present.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Every one of the 108 removed lines contains `anydata Additional Values`
  (`diff -u … | grep '^-' | grep -vc 'anydata Additional Values'` → **0**). Nothing else was deleted.
- Every one of the 195 added lines is either a rewritten `remote function` line (108) or an
  annotation line (87). 108 + 69 + 17 + 1 = 195 exactly.
- README block (lines 7–77) `diff`s clean between the two renders.
- Type name set, remote-method name set, section markers, `// Unknown type:` count (0 both),
  version-qualified refs (0 both) all unchanged.
- At the JSON level, stripping annotations from `new` typeDefs and the `Additional Values` parameter
  from `old` client functions makes the two documents equivalent — so no doc string, type, default,
  return type, or link was altered.
- No malformed syntax introduced; `new` in fact *removes* the one malformed construct
  (an identifier containing a space).

## 5. Issues in `new` (independent of `old`)

All of the following are also present in `old` (i.e. they are pre-existing pipeline behaviour, not
introduced by spec v2), but they are inaccuracies a consumer of `new` will still hit:

1. **Record field default values are dropped.** `types.bal` has 105 fields with defaults
   (`int maxItems = 100;`, `int skipCount = 0;`, …); the render has **0**. They are emitted as
   optional (`int maxItems?;`). An LLM reading this cannot know the API's default page size is 100.
   (Verified: 105 in source, 0 in old render, 0 in new render.)
2. **Flattened `*Queries` params get fabricated zero-value defaults.** `listComments` renders as
   `int maxItems = 0, string[] fields = [], int skipCount = 0`, but the source record declares
   `maxItems = 100` and `fields` has no default at all. `maxItems = 0` is not just missing
   information, it is *wrong* — the JSON carries `"default": "0"` explicitly. Affects 108 methods.
3. **Invalid parameter ordering in rendered client signatures.** All 108 flattened methods end with
   a non-defaulted `XQueries queries` parameter placed after defaultable parameters, e.g.
   `…, int skipCount = 0, ListCommentsQueries queries)`. Ballerina requires required parameters
   before defaultable ones, so the rendered signature does not compile as written. (The JSON marks
   `queries` `"optional": true`, so this is a renderer-side omission of the default.)
4. **Both the flattened fields and the record are emitted.** Source takes only `*ListCommentsQueries
   queries`; the render lists `maxItems`, `fields`, `skipCount` *and* `ListCommentsQueries queries`,
   which reads as a duplicated/ambiguous API surface.
5. **`public` and `isolated` qualifiers dropped.** 295 `public type` → 0 `public type`;
   `public isolated client class Client` → `client class Client`;
   `remote isolated function` → `remote function`; `public isolated function init` → `function init`.
6. **Closed record rendered as open.** `types.bal:368 public type ConnectionConfig record {|` renders
   as `type ConnectionConfig record {`. (The three anonymous inline closed records at `types.bal:100,
   120, 1191` *are* rendered correctly as `record {|…|}`.)
7. **Continuation lines of multi-line doc comments lose the leading `#`.** 1043 such lines in the
   Types section, identical count in both renders — e.g. `If not supplied then the default value is
   100` sits at column 0 between the `#` line and the field. Makes the block unparseable and can blur
   the doc/code boundary for a consumer.
8. **`constraint` prefix is used without an import.** The render preamble emits only
   `import ballerinax/alfresco;`, yet `new` now writes `@constraint:Int {…}` 69 times. This is the
   one item on this list that is new-only. It is cosmetic given the render is already
   non-compilable (see 3, 5, 7), and `http:` was already used unimported in `old` (15 occurrences,
   32 in `new`) with an explanatory `// Special Agent Note: … FROM ballerina/http package` comment;
   no such note accompanies the `constraint` references.

## 6. Coverage gaps vs. the library

**None.**

- The package has exactly one module, `alfresco`, which *is* the default module
  (`bala/…/any/modules/` lists only `alfresco`; Central metadata `modules: ['alfresco']`). There is
  therefore **no submodule-only API** and no shared submodule gap for this library.
- All 295 `public type` declarations appear in both renders (set difference empty in both
  directions).
- All 142 public remote methods plus `init` appear in both renders.
- `utils.bal` declares only module-private symbols (`SimpleBasicType`, `Encoding`, `EncodingStyle`,
  and 6 `isolated function`s — none marked `public`); their absence from the render is correct.
- There are no public constants, enums, annotations, listeners, services, or module-level functions
  in the package (`grep -E '^public (const|enum|function|isolated function|annotation|listener)'`
  over the bala's three `.bal` files → no hits; JSON `functions`/`services`/`annotations` arrays are
  empty on both sides).

## 7. Compiler plugin

**The package has no compiler plugin.** The bala's `any/` directory contains only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/` and no
`compiler-plugin.json`. Upstream `v2.0.2` has no `compiler-plugin`/`*-compiler-plugin` directory
(`find -maxdepth 2 -iname '*compiler-plugin*'` → empty) and `ballerina/Ballerina.toml` has zero
occurrences of `compiler-plugin`. Nothing plugin-derived is therefore expected in, or missing from,
the render.

The only annotations in the package are `ballerina/constraint`'s `@constraint:Int`,
`ballerina/http`'s `@http:Header`, and the platform `@display` — all three now surface in `new`, and
none of them existed in `old`. This is the single most consequential improvement here: the
`@constraint:Int {minValue: …}` annotations are the only place the render states the API's
validation bounds, and `@http:Header {name: "If-Modified-Since"}` / `{name: "Range"}` are the only
place the wire-level header names are stated (the Ballerina field names `ifModifiedSince` / `range`
do not disclose them).

## 8. Other considerations

- **Not deprecated.** Central: `isDeprecated: false`, `deprecateMessage: ''`,
  `visibility: public`, `graalvmCompatible: Yes`, `ballerinaVersion: 2201.12.4`, `pullCount: 43`.
- **Stable major version** (2.0.2), so no pre-1.0 instability caveat.
- **Size:** `new` is 87 lines (+1.9%) larger in text but the JSON is 9,190 bytes (−1.4%) *smaller*.
  Token impact of the change is essentially neutral-to-favourable.
- **Doc quality:** doc strings are inherited from the Alfresco OpenAPI spec and are complete; the
  README block (69 rendered lines) matches the 68-line `ballerina/README.md` upstream.
- The `@constraint:Int` annotations only appear on `*Queries` records; since the corresponding client
  parameters are flattened with fabricated `= 0` defaults (§5.2), a consumer following the *client
  signature* rather than the *record* would pass `maxItems = 0`, which violates the
  `{minValue: 1}` constraint that `new` now correctly documents on the record. Worth flagging to the
  renderer owners, but it is a pre-existing flattening bug, not a spec-v2 regression.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/… new/…` | 4567 / 4654 |
| 2 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 3 | `grep -n '^// --- '` both | 4 markers each; `Client` at 3988 (old) / 4075 (new) |
| 4 | `diff -u old new \| grep -c '^-'` (excl. `---`) | 108 |
| 5 | `diff -u old new \| grep -c '^+'` (excl. `+++`) | 195 |
| 6 | removed lines not containing `anydata Additional Values` | **0** |
| 7 | added lines: `@constraint:Int` / `@http:Header` / `remote function` | 69 / 17 / 108 (+1 `@display`) = 195 |
| 8 | `grep -c '@constraint:Int' types.bal` (bala) | 69 |
| 9 | `grep -c '@http:Header' types.bal` | 17 |
| 10 | `grep -c '@display' types.bal` | 1 |
| 11 | annotation `{value}` multiset, source vs `new` | identical: 35/34/9/8/1 |
| 12 | python pairwise (annotation, value, annotated decl) source vs `new`, ordered | 87 vs 87 entries, **0 mismatches** |
| 13 | `grep -c 'anydata Additional Values'` old / new | 108 / 0 |
| 14 | `grep -c '\*[A-Za-z]*Queries queries' client.bal` | 108 |
| 15 | `grep -cE '^public type .*Queries record \{$'` (open) / `\{\|$` (closed) | 108 / 0 |
| 16 | `^public type` in types.bal vs `^type` in new render | 295 / 295; `comm` both ways empty |
| 17 | remote method names: client.bal vs new vs old | 142 / 142 / 142; `comm -3` empty; old↔new `diff` identical |
| 18 | JSON top-level: typeDefs / clients / functions / services / annotations | 295→295, 1→1, 0→0, 0→0, 0→0 |
| 19 | JSON typeDefs differing | 45; **0** after stripping `annotations` |
| 20 | JSON annotation objects, old vs new | 0 vs 87 |
| 21 | JSON client functions differing | 108; **0** after removing param `"Additional Values"` from old |
| 22 | JSON byte size old / new | 665,472 / 656,282 |
| 23 | `diff` of render lines 7–77 (README block) old vs new | identical |
| 24 | `git ls-remote --tags` | `v2.0.2` → `bcb3747c170800aa3dc09870c13d6cc8b213670f` |
| 25 | `git clone --depth 1 --branch v2.0.2`; `diff -q` upstream vs bala for client/types/utils.bal | all **same** |
| 26 | `Ballerina.toml:5 version = "2.0.2"`; bala `package.json` name/version | `alfresco` / `2.0.2` — PIN_OK |
| 27 | bala `any/` listing; `find -iname '*compiler-plugin*'` upstream; `grep -c compiler-plugin Ballerina.toml` | no plugin dir; 0 hits; 0 |
| 28 | bala `modules/` listing; Central `modules` field | `alfresco` only (default module) |
| 29 | Central `/2.0/registry/packages/ballerinax/alfresco/2.0.2` | `isDeprecated: false`, `graalvmCompatible: Yes`, `ballerinaVersion: 2201.12.4` |
| 30 | source record fields with `= default` vs render (old/new) | 105 / 0 / 0 |
| 31 | `record {\|` source vs render | 4 (incl. `ConnectionConfig`) vs 18 (inline anon open records normalised to `record {\|anydata...;\|}`); `ConnectionConfig` rendered open in both |
| 32 | `^public type` count in renders | 0 / 0 (qualifier dropped both sides) |
| 33 | doc-continuation lines at column 0 in Types section, old / new | 1043 / 1043 |
| 34 | `^import` lines in renders | `import ballerinax/alfresco;` at 5 and 35, both sides |
| 35 | public non-type decls in bala (`const`/`enum`/`function`/`annotation`/`listener`) | none; only `public isolated client class Client` (client.bal:26) |
| 36 | `client.bal:44` source signature vs `new` line 4082 | source has no rest param; `new` matches modulo flattening |
| 37 | precomputed `OLD_AND_NEW_DIFFS/alfresco_diff.md` header (+195/−108, 102 hunks, 0 decls added/removed) | independently reproduced — accurate |

## 10. Caveats and unverified items

- **Renderer-side vs extractor-side attribution.** I verified *what* changed in the JSON and the
  `.bal.txt`, but I did not read the `ballerina-vscode` `CopilotLibraryManager` /
  `toSyntaxString` sources on either branch, so the claim that annotation emission and
  "Additional Values" suppression originate in the extractor (JSON) rather than the renderer is
  inferred from the JSON diff alone. The JSON diff does show both changes present at the JSON layer,
  which is direct evidence for extractor-side origin; the statement about *why* is not verified.
- **Runtime/compile verification not performed.** I did not attempt to compile the rendered
  `.bal.txt` with a Ballerina toolchain; the invalid-parameter-order and missing-import claims in §5
  are from reading the Ballerina spec's ordering rule against the rendered text, not from a compiler
  error message.
- **Annotation placement check is positional.** The 87-site comparison in §3 relies on the render
  emitting types in the same relative order as `types.bal`. It produced 0 mismatches, which is
  strong evidence, but a name-keyed cross-check per owning type was not separately run.
- Everything else in this report comes from a command whose output is recorded in §9.

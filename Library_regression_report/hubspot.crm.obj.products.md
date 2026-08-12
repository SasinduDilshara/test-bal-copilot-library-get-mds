# ballerinax/hubspot.crm.obj.products 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.products` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.products |
| Tag reviewed | `v2.0.2` (commit `e114d7e1e77fa07bbba517fc0f1511df772b2133`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.products/2.0.2` |
| Old render | `781` lines |
| New render | `782` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders describe an identical API surface: the same 41 type definitions and the same
`client class Client` with `init` + 12 resource functions. No declaration was added or removed.
The only differences are three classes of change, all of which move `new` *closer* to the library
source:

1. **11 version/module-qualified type refs normalised** (`ballerina/lang.int:0.0.0:Signed32` →
   `int:Signed32`; `record {|ballerinax/hubspot.crm.obj.products:2.0.2:ValueWithTimestamp[]...;|}`
   → `record {|ValueWithTimestamp[]...;|}`). The `new` spellings match `types.bal` character for
   character.
2. **4 spurious `anydata Additional Values` parameters removed** from client resource functions.
   These were syntactically invalid Ballerina (identifier with a space) and correspond to no
   parameter in `client.bal`.
3. **1 annotation recovered**: `@display {label: "Connection Config"}` on `ConnectionConfig`, which
   is genuinely present at `types.bal:240` and was silently dropped by `old`.

Nothing present and correct in `old` is missing, truncated, or degraded in `new`. Zero
`// Unknown type:` placeholders on either side (this package has no error/object/`Other` type
defs to degrade). The remaining inaccuracies listed in §5 are pre-existing and byte-identical in
both renders.

## 2. Change inventory

Line counts (`wc -l`): old **781**, new **782** (+1). Section markers: 4 on both sides
(`README`, `END README`, `Types`, `Client`).

Declaration sets are **identical**:

```
diff <(grep -E '^(type|public type|enum|const|annotation|client class|class|function|...) ' old) \
     <(... new)   →  no output  (IDENTICAL decl sets)
```

| Kind | old | new | added | removed |
|---|---|---|---|---|
| `type` (record) definitions | 41 | 41 | 0 | 0 |
| `client class` | 1 | 1 | 0 | 0 |
| client `init` | 1 | 1 | 0 | 0 |
| client resource functions | 12 | 12 | 0 | 0 |
| module-level functions | 0 | 0 | 0 | 0 |
| enums / consts / annotations / services / listeners | 0 | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | — | — |
| Version-qualified type refs | 11 | 0 | — | −11 |
| `Additional Values` pseudo-params | 4 | 0 | — | −4 |
| `@display` annotations rendered | 0 | 1 | +1 | — |

JSON side (structural diff, sorted+pretty): 2567 → 2541 lines, 62 changed lines, comprising
exactly the three classes above. `typeDefs` 41 → 41, `clients` 1 → 1, `functions` 0 → 0,
`services` 0 → 0, `annotations` (top-level) 0 → 0 on both sides.

### Modified lines, grouped

**Types section (12 hunks)**

| Field | Type in `old` | Type in `new` | Source |
|---|---|---|---|
| `AssociationSpec.associationTypeId` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` | `types.bal:372` |
| `ValueWithTimestamp.updatedByUserId` | same pattern | `int:Signed32` | `types.bal:185` |
| `GetGetPageQueries.'limit` | same pattern | `int:Signed32` | `types.bal:95` |
| `BatchResponse….numErrors` (×2) | same pattern | `int:Signed32` | `types.bal:133`, `types.bal:336` |
| `CollectionResponseWithTotal….total` | same pattern | `int:Signed32` | `types.bal:214` |
| `PublicObjectSearchRequest.'limit` | same pattern | `int:Signed32` | `types.bal:302` |
| `…propertiesWithHistory` (×3) | `record {\|ballerinax/hubspot.crm.obj.products:2.0.2:ValueWithTimestamp[]...;\|}` | `record {\|ValueWithTimestamp[]...;\|}` | `types.bal:230,386,440` |
| `SimplePublicObjectWithAssociations.associations` | `record {\|ballerinax/…:2.0.2:CollectionResponseAssociatedId...;\|}` | `record {\|CollectionResponseAssociatedId...;\|}` | `types.bal:378` |
| `ConnectionConfig` | (no annotation) | `@display {label: "Connection Config"}` added above the type | `types.bal:240` |

That accounts for all 11 qualified refs (7 `int:Signed32` + 4 inline records) and the +1 net line.

**Client section (3 hunks, 4 signatures)** — `anydata Additional Values` removed from:
`post batch/read`, `get [string productId]`, `patch [string productId]`, `get ` (get-page).
These are exactly the four resource functions that take an included-record parameter
(`*PostBatchReadReadQueries`, `*GetProductIdGetByIdQueries`, `*PatchProductIdUpdateQueries`,
`*GetGetPageQueries`) whose record type is *open*; `old` surfaced the implicit rest field as a
fake parameter described `"Capture key value pairs"`.

## 3. Correctness against library source

Bala module sources are byte-identical to the `v2.0.2` tag (`diff -q` on all three `.bal` files
returned "same" for `client.bal`, `types.bal`, `utils.bal`), so GitHub and the bala do not
disagree.

- **Type universe**: `grep -E '^public type ' types.bal` → 41 names; `grep -E '^type '` in the
  new render → 41 names. `comm` in both directions is empty — every public type is rendered, and
  the render invents none.
- **`int:Signed32`**: all 7 occurrences in `types.bal` (lines 95, 133, 185, 214, 302, 336, 372)
  are spelled `int:Signed32`. `new` matches; `old` mangled 7/7 (the 6 shown as changed plus
  `'limit` at 302 → the `PublicObjectSearchRequest` hunk).
- **Inline closed records**: `types.bal:230/378/386/440` are literally
  `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}`.
  `new` reproduces them exactly.
- **`@display`**: `types.bal:240` `@display {label: "Connection Config"}` immediately above
  `public type ConnectionConfig record {|`. This is the **only** annotation in the entire package
  (`grep '@' types.bal client.bal` → 1 hit), and `new` renders it verbatim at render line 547.
- **Client operations**: `grep -n "function" client.bal` yields `init` (line 31) plus 12
  `resource isolated function` declarations (lines 47, 67, 84, 100, 118, 135, 152, 170, 186, 203,
  220 …). All 12 appear in both renders with matching HTTP verb, resource path, payload type and
  return union. Spot-checked exhaustively — e.g. `client.bal:203`
  `post batch/upsert(BatchInputSimplePublicObjectBatchInputUpsert payload, map<string|string[]> headers = {}) returns BatchResponseSimplePublicUpsertObject|BatchResponseSimplePublicUpsertObjectWithErrors|error`
  matches render line 779 exactly.
- **`OAuth2RefreshTokenGrantConfig`** (`types.bal:199`) is `record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl = "…"; |}`.
  Both renders flatten the inclusion into the 9 inherited fields plus `refreshUrl` — correct
  expansion, unchanged between sides.
- **`Additional Values` has no source counterpart**: `client.bal` declares no rest parameter and
  no parameter of type `anydata` anywhere. `old`'s emission was fabricated.
- **README**: render lines 8–195 are identical to `any/docs/README.md` lines 1–187 (only a
  trailing blank line differs), and the README block is byte-identical between `old` and `new`.

## 4. Regressions

**None found.**

Checked to conclude this:
- Full structural JSON diff (`json.dumps(sort_keys=True)` + `difflib.unified_diff`) — every one of
  the 62 changed lines is one of: qualified-ref normalisation (11), `Additional Values` removal
  (4 blocks), `@display` addition (1 block). Nothing else was removed from the JSON.
- Declaration-set diff of the two renders is empty (§2).
- README block diff is empty.
- `// Unknown type:` count is 0 → 0; no new degradation.
- Every doc comment line count and text in the changed hunks is preserved; the only removed
  doc string is `"Capture key value pairs"`, which belonged to the fabricated parameter.
- No default value, parameter, return type, or field present in `old` is absent in `new`
  (verified by the JSON diff having no other `-` lines).

## 5. Issues in `new` (independent of `old`)

All of the following are **shared** with `old` byte-for-byte — they are pre-existing renderer
limitations, not spec-v2 regressions — but they are inaccuracies against the library source and
worth recording:

1. **Field default values are dropped and the field is turned optional.** Source
   `types.bal:95 int:Signed32 'limit = 10;` renders as `int:Signed32 'limit?;` (render line 396).
   Same for `boolean archived = false` → `archived?` (render 394),
   `string refreshUrl = "https://api.hubapi.com/oauth/v1/token"` → `string refreshUrl?`
   (render 502), and the whole `ConnectionConfig` block (`decimal timeout = 30` → `decimal timeout?`
   at render 558; `httpVersion`, `http1Settings`, `http2Settings`, `forwarded`, `cache`,
   `compression`, `responseLimits`, `socketConfig`, `validation`, `laxDataBinding` likewise).
   An LLM reading this loses every default and will believe required-with-default fields are
   optional.
2. **Closed records rendered as open.** The three top-level `record {| … |}` types
   (`OAuth2RefreshTokenGrantConfig` `types.bal:199`, `ConnectionConfig` `types.bal:241`,
   `ApiKeysConfig` `types.bal:478`) render as `record {`. Inline anonymous closed records are
   preserved correctly (19 `record {|` in the render vs 18 inline in source — the extra is
   `record {}` at `types.bal:25` rendered as the semantically-equivalent `record {|anydata...;|}`).
3. **Included-record parameters are double-counted.** `client.bal:170`
   `*GetGetPageQueries queries` becomes *both* the expanded scalar params *and* a positional
   `GetGetPageQueries queries` (render line 769). The resulting signature would not compile and
   overstates the arity.
4. **Wrong default in the expanded params.** Render 769 shows `int:Signed32 limit = 0`; the source
   default is `10` (`types.bal:95`). Also `'limit` loses its quoted-identifier form here.
5. **Resource path `.` dropped.** `client.bal:170/186` declare `resource isolated function get .(…)`
   and `post .(…)`; the render emits `resource function get (…)` / `resource function post (…)`
   (render 769, 773) — non-compiling and ambiguous.
6. **Qualifiers dropped.** `public isolated client class Client` → `client class Client`;
   `public isolated function init` → `function init`; `resource isolated function` → `resource function`;
   `public type` → `type`. Isolation/visibility information is not conveyed.
7. **Multi-line doc comment loses its continuation marker.** Render line 585–586 emits
   `and absent fields are handled as \`nilable\` types. Enabled by default` without a leading `#`,
   breaking the doc block (source `types.bal` has it as a `#` continuation line).

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

- The package exports exactly one module (`package.json` `"export": ["hubspot.crm.obj.products"]`,
  `any/modules/` contains only `hubspot.crm.obj.products`, Central metadata lists one module).
  There is therefore no submodule-only API and no shared `getDefaultModule()` gap for this library.
- Public symbols in the default module: 41 `public type` + 1 `public isolated client class Client`.
  All 41 types appear in both renders (`comm` empty both ways); the client class and all 13 of its
  public members (`init` + 12 resource functions) appear in both.
- Non-public symbols correctly excluded: `utils.bal` `enum EncodingStyle` (line 37) and its 6
  module-private `isolated function`s (lines 48, 74, 111, 151, 175, 189) are absent from both
  renders, which is correct.

## 7. Compiler plugin

The package ships **no compiler plugin**: no `compiler-plugin/` or `*-compiler-plugin/` directory
in the `v2.0.2` tree, no `CompilerPlugin.toml`, and no `compiler-plugin/` entry in the bala
(`any/` contains only `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`).
`Ballerina.toml` declares no `[[tool]]` or plugin section. Nothing plugin-derived is therefore
expected in, or missing from, the render.

The one annotation the package does define usage of — `@display` on `ConnectionConfig` — comes
from the standard `ballerina/jballerina.java`/tooling annotation set and is now correctly
surfaced by `new`.

## 8. Other considerations

- **Not deprecated**: Central metadata `"isDeprecated": false`, `"deprecateMessage": ""`.
- **Stable version** (2.0.2), `graalvmCompatible: Yes`, built with Ballerina `2201.12.2`
  (`Ballerina.toml` declares `distribution = "2201.12.0"`).
- **Size/tokens**: renders are ~781/782 lines; JSON 86,248 → 85,130 bytes (−1.3%). `new` is
  marginally cheaper despite adding a line, because the long qualified type names are gone.
- **Doc quality**: every public type and every resource function carries a doc comment; the README
  (187 lines) is fully embedded, including the Quickstart and both example links.
- **Net effect on an LLM consumer**: `new` removes four syntactically illegal parameter
  declarations and eleven type names that do not resolve in user code — both were actively
  misleading. That is a real quality gain even though the API inventory is unchanged.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 781 / 782 |
| 2 | `grep -c '^// Unknown type:'` on both | 0 / 0 |
| 3 | `grep -n '^// --- '` on both | 4 markers each; new shifted +1 after line 546 |
| 4 | `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`e114d7e…`) |
| 5 | `git clone --depth 1 --branch v2.0.2 …` | succeeded |
| 6 | `diff -q bala/modules/*/{client,types,utils}.bal src/ballerina/…` | all three identical |
| 7 | `ls bala/any/modules/` | single module `hubspot.crm.obj.products` |
| 8 | `cat bala/any/package.json` | `"export": ["hubspot.crm.obj.products"]`, version 2.0.2 |
| 9 | `grep -cE '^public type ' types.bal` | 41 |
| 10 | `grep -E '^type ' new render \| awk '{print $2}'` vs bala names, `comm` both ways | both empty → 41/41 exact match |
| 11 | `grep -n "function" client.bal` | `init` + 12 `resource isolated function` |
| 12 | `grep -nE '[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 11 / 0 |
| 13 | `grep -c 'Additional Values'` old / new | 4 / 0 |
| 14 | `grep -n '@display'` old / new | none / render line 547 |
| 15 | `grep -n "@display" types.bal` | line 240, only annotation in package |
| 16 | `grep -n "int:Signed32" types.bal` | 7 hits (95,133,185,214,302,336,372) |
| 17 | `grep -n 'record {\|' types.bal` | 21 (18 inline + 3 top-level closed types) |
| 18 | `grep -c 'record {\|'` old / new render | 19 / 19 |
| 19 | Structural JSON diff (python difflib, sort_keys) | 2567→2541 lines, 62 ± lines, all three known classes |
| 20 | `typeDefs`/`clients`/`functions`/`services`/`annotations` list lengths in both JSONs | 41/1/0/0/0 on both |
| 21 | `diff` of render decl sets old vs new | empty |
| 22 | `diff` of README block (render L8–195 vs `docs/README.md`) | only a trailing blank line |
| 23 | `diff` of README block old vs new render | identical |
| 24 | `find src -iname '*compiler-plugin*' -o -iname CompilerPlugin.toml` | no results |
| 25 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/hubspot.crm.obj.products/2.0.2` | `isDeprecated:false`, 1 module, ballerinaVersion 2201.12.2 |
| 26 | `wc -c old/new .json` | 86,248 / 85,130 |
| 27 | `grep -n 'limit = 0' / 'refreshUrl' / 'decimal timeout' / 'resource function get ('` both renders | present identically in both → shared, not regressions |
| 28 | `grep -nE '^public ' utils.bal client.bal` | only `public isolated client class Client` (client.bal:23) |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that specific rendered signatures (`resource function get (…)`,
  the duplicated included-record parameter) would fail to compile are read off the Ballerina grammar,
  not from a `bal build` run.
- The `old`-side renderer patch (`service.methods ?? []`) is documented as affecting only
  `ballerina/mcp`; this package declares no services (`services: []` in both JSONs), so it is
  irrelevant here — but that patch's source was not independently inspected.
- Bala↔tag equality was verified for the three `.bal` files only; `docs/icon.png` and
  `dependency-graph.json` were not byte-compared.
- Central metadata was fetched live on the review date; if the package is later deprecated or
  re-published this report's §8 would need re-checking.

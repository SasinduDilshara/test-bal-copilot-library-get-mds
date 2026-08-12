# ballerinax/hubspot.crm.properties 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.properties` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.properties |
| Tag reviewed | `v2.0.2` (commit `da0c236`, peeled `646de3a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.properties/2.0.2` |
| Old render | `575` lines |
| New render | `576` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. The diff is 12 hunks, +12/−11 lines, and consists of exactly three
mechanical changes, all improvements:

1. 9 occurrences of the version-qualified type ref `ballerina/lang.int:0.0.0:Signed32` are replaced by
   the real source spelling `int:Signed32`.
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — present in the
   library source, silently dropped by `old` — is now emitted.
3. Two client resource methods lose the pseudo-parameter `anydata Additional Values`, which was
   syntactically invalid Ballerina (identifier containing a space) and was an artifact of the open
   `record {}` rest field on the included-record query params.

Declaration sets are identical on both sides (23 type defs + 1 client class with 13 methods on each).
No declaration, doc comment, field, or README line was lost: docstring line counts are 115 on both
sides and the README block is byte-identical to `docs/README.md` in the bala.

Nothing new was invented: both changed forms were verified against the bala source, which is
byte-identical to the `v2.0.2` upstream tag.

## 2. Change inventory

Counts from `diff -u old new`:

| Metric | Value |
|---|---|
| Hunks | 12 |
| Lines added | 12 |
| Lines removed | 11 |
| `// Unknown type:` lines, old / new | 0 / 0 |
| Version-qualified type refs (`x/y:0.0.0:T`), old / new | 9 / 0 |
| Section markers, old / new | 4 / 4 (`README`, `END README`, `Types`, `Client`) |

Declarations by kind — **identical on both sides**:

| Kind | old | new |
|---|---|---|
| `type` (records) | 23 | 23 |
| `client class` | 1 | 1 |
| client methods (incl. `init`) | 13 | 13 |
| `enum` / `const` / `annotation` / `service` / `listener` / module-level `function` | 0 | 0 |

`diff` of the sorted `^type <Name>` sets → empty (`TYPE SETS IDENTICAL`).
JSON: `annotations`, `description`, `functions`, `name`, `readme`, `services` are byte-identical;
only `typeDefs` and `clients` differ.

Modified declarations (11 total):

| # | Declaration | Change |
|---|---|---|
| 1 | `Property.displayOrder` | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` |
| 2 | `Option.displayOrder` | same |
| 3 | `PropertyGroup.displayOrder` | same |
| 4 | `PropertyCreate.displayOrder` | same |
| 5 | `OptionInput.displayOrder` | same |
| 6 | `PropertyUpdate.displayOrder` | same |
| 7 | `PropertyGroupCreate.displayOrder` | same |
| 8 | `BatchResponsePropertyWithErrors.numErrors` | same |
| 9 | `PropertyGroupUpdate.displayOrder` | same |
| 10 | `ConnectionConfig` | `@display {label: "Connection Config"}` **added** |
| 11 | `Client.get [objectType]/[propertyName]` and `Client.get [objectType]` | pseudo-param `anydata Additional Values` **removed** |

JSON-level confirmation of #11 (parameter lists):

```
old: [objectType, propertyName, headers, archived, properties, 'Additional Values', queries]
new: [objectType, propertyName, headers, archived, properties, queries]
```

Nothing was added or removed at declaration level (0 added, 0 removed).

## 3. Correctness against library source

Upstream `v2.0.2` and the bala are byte-identical (`diff -q` returned "same" for `client.bal`,
`types.bal`, `utils.bal`, and `README.md`), so the bala is authoritative and unambiguous.

- `int:Signed32` — the bala source writes exactly `int:Signed32` at `types.bal:53, 62, 93, 138, 169,
  200, 211, 230` and in `BatchResponsePropertyWithErrors` (line 178 block). `new` matches the source
  spelling on all 9 sites; `old` did not.
- `@display {label: "Connection Config"}` — present at `types.bal:278`, immediately above
  `public type ConnectionConfig record {|`. `new` reproduces it verbatim; `old` omitted it.
- `Additional Values` removal — `client.bal:114` and `client.bal:200` declare the params as
  `*GetCrmV3PropertiesObjectTypePropertyNameGetByNameQueries queries` and
  `*GetCrmV3PropertiesObjectTypeGetAllQueries queries`. Those records (`types.bal:103`, `types.bal:217`)
  are open (`record { ... };`), so the implicit `anydata` rest field is what `old` surfaced as
  `anydata Additional Values`. It is not a real API parameter and it is not valid syntax. Removing it
  is correct.
- Full field-by-field check of `Property` (render lines 236–279 vs `types.bal:223–268`): all 26 fields,
  optionality markers, and doc comments match exactly.
- Client surface: 13 methods in `client.bal` (`init` + 12 resource functions), 13 in the render; paths,
  payload types and return types match, e.g. `post [objectType]/batch/read(BatchReadInputPropertyName
  payload, ...) returns BatchResponseProperty|BatchResponsePropertyWithErrors|error` matches
  `client.bal:163`, and `init(..., string serviceUrl = "https://api.hubapi.com/crm/v3/properties")`
  matches `client.bal:32` including the default.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff -u` of the two renders reviewed hunk by hunk (12 hunks, all listed in §2); every hunk is
  one of the three improvements above.
- Sorted declaration-name sets compared → identical.
- Structural JSON diff: only `typeDefs` (Signed32 rename + `ConnectionConfig.annotations`) and
  `clients` (the two dropped `Additional Values` params) differ; `readme`, `description`,
  `functions`, `services`, `annotations` byte-identical.
- Docstring line count `^    # ` → 115 in both files; no doc text lost.
- README block (`sed -n '8,188p'`) vs `docs/README.md` → identical apart from one trailing blank line;
  identical on the old side too.
- No default value, return type, or parameter present in `old` is absent in `new` other than the
  invalid `Additional Values` pseudo-param.

## 5. Issues in `new` (independent of `old`)

All six below are present **identically in `old`** — they are pre-existing renderer limitations, not
introduced by spec v2. Listed because they misrepresent the library to a consuming LLM.

1. **Included-record query params rendered twice.** Source: `resource isolated function get
   [string objectType](map<string|string[]> headers = {}, *GetCrmV3PropertiesObjectTypeGetAllQueries
   queries)` (`client.bal:200`). Render: `... headers = {}, boolean archived = false, string properties
   = "", GetCrmV3PropertiesObjectTypeGetAllQueries queries)` — the record's fields are flattened *and*
   the record itself is kept as a trailing parameter. This signature does not compile and would lead an
   LLM to pass both forms. Affects the two `get` methods.
2. **Invented default `string properties = ""`.** Source declares `string properties?` with no default
   (`types.bal:106`, `types.bal:220`). The JSON carries no `defaultValue` for it, so the `= ""` is
   introduced by the renderer.
3. **`archived` default lost in the Queries records.** Source: `boolean archived = false` (required
   field with a default, `types.bal:105`/`219`); render: `boolean archived?` — optionality and default
   both wrong.
4. **Record field defaults dropped throughout `ConnectionConfig`.** Source has `httpVersion =
   http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`, `forwarded = "disable"`,
   `cache = {}`, `compression = http:COMPRESSION_AUTO` (`types.bal:280–299`); all render as bare
   optional fields. Same for `OAuth2RefreshTokenGrantConfig.refreshUrl`, whose HubSpot-specific default
   `"https://api.hubapi.com/oauth/v1/token"` (`types.bal:193`) is lost — this one is materially useful
   information for code generation.
5. **Closed records rendered as open.** `ApiKeysConfig`, `ConnectionConfig`, and
   `OAuth2RefreshTokenGrantConfig` are `record {| ... |}` in source (`types.bal:190, 272, 279`) but
   render as `record { ... }`.
6. **Malformed multi-line doc comment.** New render line 519 (old line 518) is
   `and absent fields are handled as \`nilable\` types. Enabled by default.` with no leading `#`, so the
   `laxDataBinding` doc wraps into a bare statement inside a record body — non-compiling text.

## 6. Coverage gaps vs. the library

**0 gaps.**

- The package exports a single module (`package.json` → `"export": ["hubspot.crm.properties"]`; bala
  `modules/` contains only `hubspot.crm.properties`), so the default-module-only extraction loses
  nothing here. No submodule-only API exists.
- The bala declares 24 public symbols: 23 `public type` + 1 `public isolated client class Client`.
  All 24 appear in both renders (set diff of source `^public type` names vs render `^type` names →
  identical).
- `utils.bal` contains 6 functions, plus `type Encoding`, `enum EncodingStyle` and `final
  defaultEncoding` — all module-private (no `public` qualifier), correctly absent from both renders.
- No public constants, annotations, listeners or services exist in the package (`grep '^public
  (const|enum|annotation|function)'` → no matches).

## 7. Compiler plugin

The package ships **no compiler plugin**: `find` over the bala for `*compiler*` returns nothing, there
is no `compiler-plugin/compiler-plugin.json` in the bala, and the upstream tree at `v2.0.2` has no
`compiler-plugin/` or `*-compiler-plugin/` directory (top level: `ballerina`, `build-config`, `docs`,
`examples`, `gradle`, plus build files). Nothing plugin-derived is therefore expected in the render,
and nothing is missing on that account.

## 8. Other considerations

- This is a stable release (`2.0.2`, latest tag in the repo). Not deprecated; `graalvmCompatible: true`;
  built with Ballerina `2201.12.2`.
- The connector is fully OpenAPI-generated (`client.bal` header: "AUTO-GENERATED FILE"), which explains
  the shape of the query-parameter records that the renderer mishandles (§5.1–5.3).
- Size: 576 lines / ~67 KB JSON. The README block occupies 181 of 576 lines (31%) — the largest single
  contributor to token cost. New JSON is 524 bytes *smaller* than old (67,400 vs 67,924) despite the
  added annotation, thanks to the shorter type names.
- `Special Agent Note: X FROM ballerina/http package` trailer comments are used consistently on both
  sides for cross-package types; the `int:Signed32` change means the lang-library reference is now
  spelled the way a user would write it, which is strictly better for code generation.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 575 / 576 |
| `grep -c '^// Unknown type:' old new` | 0 / 0 |
| `grep -n '^// --- ' old` / `new` | 4 markers each (README@7, END README@189, Types@191, Client@522/523) |
| `diff -u old new \| grep -c '^@@'` | 12 |
| `diff -u old new \| grep -c '^+[^+]'` / `'^-[^-]'` | 12 / 11 |
| `grep -c 'ballerina/lang.int:0.0.0:Signed32'` old / new | 9 / 0 (from diff-md signal table, re-verified by hunk inspection) |
| `grep -n '^@' old` / `new` | none / `480:@display {label: "Connection Config"}` |
| `diff <(grep -oE '^type [A-Za-z0-9_]+' old\|sort) <(… new\|sort)` | empty — TYPE SETS IDENTICAL, 23 each |
| `diff <(source public type names) <(render type names)` | empty — IDENTICAL SETS, 23 each |
| `grep -c '^    # ' old new` | 115 / 115 |
| `diff <(sed -n '8,188p' new) bala/docs/README.md` | only `181d180` (trailing blank line) |
| Python structural JSON diff, top-level keys | only `typeDefs` and `clients` differ |
| Python per-typedef JSON diff | 10 typedefs differ: 9 × `Signed32` type-name change, 1 × `ConnectionConfig.annotations` `null` → `[{"name":"display","value":"{label: \"Connection Config\"}"}]` |
| Python per-client-function JSON diff | 13/13 functions matched by key; 2 differ, each by removal of param `{"name":"Additional Values","type":{"name":"anydata"}}` |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v2.0.0`, `v2.0.1`, `v2.0.2` → exact tag `v2.0.2` exists |
| `git clone --depth 1 --branch v2.0.2` | succeeded |
| `diff -q src/ballerina/{client,types,utils}.bal bala/modules/.../` | all "same" |
| `diff -q src/ballerina/README.md bala/docs/README.md` | same |
| `src/ballerina/Ballerina.toml:3-5` | `org = "ballerinax"`, `name = "hubspot.crm.properties"`, `version = "2.0.2"` → pin confirmed on both sides |
| `bala/any/package.json` | `"export": ["hubspot.crm.properties"]`, single module |
| `ls bala/any/modules/` | only `hubspot.crm.properties` |
| `grep -hoE '^public (type\|class\|…)' bala/*.bal \| sort \| uniq -c` | 23 public types + 1 public client class = 24 |
| `grep -cE '^    resource isolated function\|init' bala/client.bal` vs render | 13 / 13 |
| `grep -nE '^(public )?(isolated )?function' bala/utils.bal` | 6 functions, none public |
| `find bala -iname '*compiler*'` and `find src -maxdepth 2 -iname '*compiler*'` | no matches (no compiler plugin) |
| `grep -n 'Additional Values' old` / `new` | lines 546, 566 / none |
| `grep -n '^and absent fields' old` / `new` | 518 / 519 (malformed doc wrap on both sides) |
| `types.bal:278` | `@display {label: "Connection Config"}` confirmed in source |
| `client.bal:114, 200` | `*…Queries queries` included-record params confirmed |
| `types.bal:103–107, 217–221` | Queries records are open, `archived = false`, `properties?` |
| `types.bal:190–194` | `OAuth2RefreshTokenGrantConfig` closed record, `refreshUrl` default = HubSpot token URL |
| render 236–279 vs `types.bal:223–268` | `Property` matches field-for-field |

## 10. Caveats and unverified items

- The `9 → 0` count of version-qualified type refs is taken from the precomputed diff's signal table;
  it was corroborated by counting the 9 corresponding hunks/lines in the unified diff and by the
  per-typedef JSON diff (9 typedefs whose only change is that type name), but the raw `grep -c` on the
  old file was not re-run independently.
- The renders were not compiled. Claims that specific rendered lines are "non-compiling" (§5.1, §5.6,
  and the removed `anydata Additional Values`) are based on reading the Ballerina grammar, not on a
  `bal build`.
- Ballerina Central registry metadata was not re-queried over the network; module list, version, and
  keywords were taken from the bala's `package.json`, which is the same artifact the extractor consumed.
- The old/new `ballerina-vscode` sources themselves were not inspected; attribution of the three changes
  to spec v2 rests on the brief's stated setup plus the fact that the library bytes are provably
  identical on both sides.

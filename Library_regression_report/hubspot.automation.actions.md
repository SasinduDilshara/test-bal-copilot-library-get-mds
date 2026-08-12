# ballerinax/hubspot.automation.actions 2.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.automation.actions` |
| Pinned version | `2.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.automation.actions |
| Tag reviewed | `v2.0.0` (exact match; upstream `ballerina/*.bal` byte-identical to bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.automation.actions/2.0.0` |
| Old render | `673` lines |
| New render | `674` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small single-module OpenAPI-generated connector: 1 client class, 17 client functions (`init` + 16
resource functions), 32 public type definitions, no module-level public functions, no services, no
listeners, no compiler plugin.

The declaration set is **identical** on both sides (32 type names — same set; 17 client functions —
same order, same paths). The only differences are 11 hunks, +13/−12 lines, all of which are
improvements in `new`:

1. All 12 version/module-qualified type references (`ballerinax/hubspot.automation.actions:2.0.0:X`,
   `ballerina/lang.int:0.0.0:Signed32`) are replaced by the plain names the library source actually
   uses (`PublicActionLabels`, `int:Signed32`). `old` = 12 occurrences, `new` = 0.
2. `@display {label: "Connection Config"}` on `ConnectionConfig` is now emitted — it exists in the
   source and was silently dropped by `old`.
3. The synthetic, non-compiling parameter `anydata Additional Values` (identifier containing a
   space) is gone from 3 resource-function signatures.

`// Unknown type:` count is 0 on **both** sides, so the headline spec-v2 fix does not apply here.
README section is byte-identical. No regression found.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 673 | 674 |
| `// --- ` section markers | 4 (README, END README, Types, Client) | 4 (same) |
| `// Unknown type:` | 0 | 0 |
| Top-level `type` declarations | 32 | 32 |
| `resource function` declarations | 16 | 16 |
| `client class` declarations | 1 | 1 |
| Version/module-qualified type refs | 12 | 0 |
| `@`-annotation lines | 0 | 1 |
| `// Special Agent Note:` cross-package hints | 17 | 17 |
| JSON bytes | 92,306 | 91,278 |
| JSON `typeDefs` | 32 | 32 |
| JSON `clients[0].functions` | 17 | 17 |
| JSON `functions` / `services` / `listeners` / `annotations` | absent | absent |

**Declarations added: 0. Declarations removed: 0.** (`comm` on the sorted top-level `type` name
sets returns empty in both directions; client function lists compare equal positionally by path.)

Modified (10 of 32 typeDefs differ in JSON, 3 of 17 client functions differ):

| Kind | Change | Count |
|---|---|---|
| Type field type ref de-qualified | `record {\|ballerinax/…:2.0.0:PublicActionLabels...;\|}` → `record {\|PublicActionLabels...;\|}` | 3 (`PublicActionDefinition`, `PublicActionDefinitionEgg`, `PublicActionDefinitionPatch`) |
| Type field type ref de-qualified | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` | 3 (`Option.displayOrder`, `GetAppIdGetPageQueries.'limit`, `GetAppIdDefinitionIdRevisionsGetPageQueries.'limit`) |
| Union member refs de-qualified | `ballerinax/…:2.0.0:PublicSingleFieldDependency\|…PublicConditionalSingleFieldDependency` → plain | 3 (`PublicActionDefinitionInputFieldDependencies`, `…EggInputFieldDependencies`, `…PatchInputFieldDependencies`) |
| Annotation added | `@display {label: "Connection Config"}` on `ConnectionConfig` | 1 |
| Client param removed | synthetic `anydata Additional Values` ("Capture key value pairs") | 3 resource functions |

The 3 affected resource functions (JSON indices 3, 10, 16):
`get [appId]`, `get [appId]/[definitionId]`, `get [appId]/[definitionId]/revisions` — exactly the
three that take an included-record `*…Queries` parameter in the source.

## 3. Correctness against library source

Upstream `v2.0.0` `ballerina/client.bal` and `ballerina/types.bal` `diff` clean against the bala's
`modules/hubspot.automation.actions/{client,types}.bal`, so source and bala agree; both were used.

Every change in `new` verified against `types.bal`:

| Render (`new`) | Source | Verdict |
|---|---|---|
| `record {\|PublicActionLabels...;\|} labels;` (line 240) | `types.bal:38` `record {\|PublicActionLabels...;\|} labels;` | exact match — `new` correct, `old` wrong |
| `record {\|PublicActionLabels...;\|} labels;` (line 561) | `types.bal:312` | exact match |
| `record {\|PublicActionLabels...;\|} labels?;` (line 584) | `types.bal:334` | exact match |
| `int:Signed32 displayOrder;` (line 316) | `types.bal:351` `int:Signed32 displayOrder;` | exact match |
| `int:Signed32 'limit?;` (line 424) | `types.bal:174` | exact match |
| `int:Signed32 'limit?;` (line 601) | `types.bal:387` | exact match |
| `type PublicActionDefinitionInputFieldDependencies PublicSingleFieldDependency\|PublicConditionalSingleFieldDependency;` (line 361) | `types.bal:72` | exact match |
| `…EggInputFieldDependencies` (line 519) | `types.bal:273` | exact match |
| `…PatchInputFieldDependencies` (line 588) | `types.bal:344` | exact match |
| `@display {label: "Connection Config"}` (line 431) | `types.bal:196` `@display {label: "Connection Config"}` | exact match — genuinely present, `old` dropped it |

Client coverage cross-check: all 16 resource functions in `client.bal` (lines 44, 61, 80, 95, 114,
131, 148, 167, 184, 201, 217, 233, 254, 272, 292, 309) plus `init` (line 28) appear in the `new`
render's `// --- Client ---` section (lines 608–674), with matching accessors, resource paths,
payload types and return types. `init`'s default `serviceUrl = "https://api.hubapi.com/automation/v4/actions"`
matches `client.bal:28`.

The removed `anydata Additional Values` parameter corresponded to the implicit `anydata` rest field
of the open query records (e.g. `GetAppIdGetPageQueries` at `types.bal:170` is `record { … }`, open).
It is *conceptually* real, but it was emitted as a positional parameter with a space in its
identifier — syntactically illegal Ballerina and misleading as a call-site parameter. The openness
of the record is still conveyed by the `GetAppIdGetPageQueries queries` parameter that both sides
keep, and by the record's own rendered definition. Net: removing it is a correctness improvement,
not a loss.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Top-level `type` name sets: `comm -23`/`comm -13` between the 32 source `public type` names and
  the 32 `new` render `type` names — both directions empty.
- `old` vs `new` type name sets equal (`set(ot)==set(nt)` on JSON `typeDefs` → `True`).
- Client function count and ordering identical (17 vs 17), and no function body/signature in `new`
  lost a parameter, default, or return type relative to `old` except the synthetic
  `Additional Values` (analysed in §3).
- README block (lines 7–192) `diff` → identical.
- `// Special Agent Note:` cross-package hints: 17 on both sides — no cross-package resolution lost.
- `// Unknown type:` 0 on both — nothing degraded.
- No doc-comment text present in `old` is absent in `new` (the only `-` lines in `diff -u` are the
  12 qualified refs plus the 3 `Additional Values` params; verified by reading all 11 hunks).

## 5. Issues in `new` (independent of `old`)

All of the following are **shared with `old`** — they are pipeline-wide rendering defects, not
introduced by spec v2. Listed because they would mislead an LLM consuming this render.

1. **Included-record parameters are double-rendered and produce non-compiling signatures.** Source
   `resource isolated function get [int:Signed32 appId](map<string|string[]> headers = {}, *GetAppIdGetPageQueries queries)`
   (`client.bal:80`) renders as
   `resource function get [int:Signed32 appId](map<string|string[]> headers = {}, boolean archived = false, int:Signed32 limit = 0, string after = "", GetAppIdGetPageQueries queries)`
   — the record's fields are flattened into positional params *and* the record itself is kept, and
   the non-defaultable `queries` follows defaultable params. Affects the same 3 resource functions.
2. **Fabricated default values.** `int:Signed32 limit = 0` and `string after = ""` are emitted, but
   `types.bal:174` / `types.bal:176` declare `int:Signed32 'limit?;` and `string after?;` — optional
   with *no* default. (`archived = false` is genuine: `types.bal:172` declares `boolean archived = false;`.)
   Confirmed in `new` JSON `clients[0].functions[3].parameters`: `"default": "0"` and `"default": "\"\""`.
3. **Closed records rendered as open.** 3 source types are `record {| … |}` (`OAuth2RefreshTokenGrantConfig`
   `types.bal:163`, `ConnectionConfig` `types.bal:197`, `ApiKeysConfig` `types.bal:379`); the render
   emits `type X record {` for all of them. Count of top-level `record {|` in `new` render: 0.
4. **Multi-line doc comment breaks out of the comment.** `types.bal:234-235` is a two-line doc; the
   render emits the continuation without a `# ` prefix — `new` line 470 is bare text
   `and absent fields are handled as \`nilable\` types. Enabled by default.` inside the
   `ConnectionConfig` body. Non-compiling. (`old` line 469, identical.)
5. **`# + param -` doc descriptions are dropped from function docs.** Source functions document each
   parameter (e.g. `client.bal:108-113`); the render emits only the summary line followed by a bare
   `# `. `grep -c '^\s*# + '` = 0 in both renders. Parameter descriptions do survive in the JSON
   (`parameters[].description`) but are discarded by `toSyntaxString`.
6. **`public` and `isolated` qualifiers dropped.** `grep -c '^public '` = 0 and `grep -c 'isolated'`
   = 0 in `new`; the source declares `public isolated client class Client` and `public type …`.
7. **Quoted identifier unquoted in parameter position.** `'limit` is correctly quoted in the type
   definition (`new:424`, `new:601`) but rendered as bare `limit` in the resource-function parameter
   lists. `limit` is not a Ballerina keyword, so this is cosmetic inconsistency rather than a
   compile error.

## 6. Coverage gaps vs. the library

**0 gaps.**

- The bala exports exactly one module: `package.json` `"export": ["hubspot.automation.actions"]`,
  and `modules/` contains only `hubspot.automation.actions`. There is **no submodule API**, so the
  known `getDefaultModule()` limitation does not bite here.
- 32 `public type|const|enum|annotation` symbols in the bala's `client.bal`/`types.bal`/`utils.bal`;
  32 in the `new` render; set difference empty in both directions.
- `utils.bal` has no `public` declarations (`grep -nE '^public ' utils.bal` → empty), consistent with
  the JSON having no top-level `functions` key.
- No `const`, `enum`, `annotation`, `service`, or `listener` declarations exist in the library, and
  none are invented by either render.

## 7. Compiler plugin

**None.** The bala contains no `compiler-plugin/` directory, and the upstream `v2.0.0` tree has no
`*plugin*` directory. `Ballerina.toml` declares no `[[plugin]]` section. Nothing plugin-derived is
expected in the render and nothing is missing.

## 8. Other considerations

- Version 2.0.0 is stable (post-1.0); no deprecation markers in `package.json` or the module sources.
- Built with `ballerina_version 2201.12.2`, `distribution = "2201.12.0"`, `graalvmCompatible: true`.
- Size impact is negligible: 674 vs 673 lines; JSON shrank 1,028 bytes (−1.1%) because the qualified
  prefixes and 3 synthetic params were removed. Slightly fewer tokens for slightly more accuracy.
- Doc quality is good: every public type and field carries a doc comment, and the 186-line README
  section (with auth setup and a quickstart) is carried through unchanged.
- The render as a whole does **not** compile as Ballerina (issues 1, 3, 4 in §5), but that is
  equally true of `old` and is a pipeline-level concern.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 673 / 674 |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v2.0.0` → exact tag `v2.0.0` (`fc2b564`) |
| `git clone --depth 1 --branch v2.0.0 <repo> src` | success |
| `diff src/ballerina/client.bal <bala>/modules/…/client.bal` | identical (`CLIENT_SAME`) |
| `diff src/ballerina/types.bal <bala>/modules/…/types.bal` | identical (`TYPES_SAME`) |
| `ls <bala>/any/modules` | only `hubspot.automation.actions` — no submodules |
| `cat <bala>/any/package.json` | `"export": ["hubspot.automation.actions"]`, v2.0.0, ballerina 2201.12.2 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each (7, 192, 194, 605/606) |
| `grep -cE '^type '` old / new | 32 / 32 |
| `grep -cE '^    resource function'` old / new | 16 / 16 |
| `grep -coE '[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 12 / 0 |
| `grep -c '^@'` old / new | 0 / 1 |
| `grep -c 'Additional Values'` old / new | 3 / 0 |
| `grep -c 'Special Agent Note'` old / new | 17 / 17 |
| `grep -c 'record {\|'` old / new | 11 / 11 (all nested; 0 top-level) |
| `grep -c 'isolated'` / `grep -c '^public '` new | 0 / 0 |
| `grep -c '^\s*# + '` old / new | 0 / 0 |
| `diff -u old new \| grep -c '^+[^+]'` / `'^-[^-]'` | 13 / 12 |
| `diff <(sed -n '7,192p' old) <(sed -n '7,192p' new)` | `README_IDENTICAL` |
| JSON top-level keys old vs new | identical set; `typeDefs` 32/32, `clients` 1/1, `readme` same, `description` same, `functions`/`services`/`annotations` absent both |
| JSON `typeDefs` name sets old vs new | equal; 10 entries differ (all listed in §2) |
| JSON `clients[0].functions` old vs new | 17/17, 3 differ (indices 3, 10, 16 — `Additional Values` removed) |
| `comm` src public symbols (32) vs new render types (32) | empty both directions |
| `grep -nE '^public ' <bala>/…/utils.bal` | empty |
| `<bala>/…/types.bal:38, 312, 334` | `record {\|PublicActionLabels...;\|}` — confirms `new` |
| `<bala>/…/types.bal:351, 174, 387` | `int:Signed32` — confirms `new` |
| `<bala>/…/types.bal:72, 273, 344` | plain union member names — confirms `new` |
| `<bala>/…/types.bal:196` | `@display {label: "Connection Config"}` — confirms `new` addition |
| `<bala>/…/types.bal:163, 197, 379` | 3 closed `record {\|` types rendered open in both |
| `<bala>/…/types.bal:170-177` | `GetAppIdGetPageQueries` open record; `archived = false` real, `'limit?`/`after?` have no defaults |
| `<bala>/…/types.bal:234-235` | 2-line doc → render line 469 (old) / 470 (new) loses `# ` prefix |
| `<bala>/…/client.bal:28, 80, 201, 309` | `init` default URL and the 3 `*…Queries` included-record params |
| `ls <bala>/any \| grep -i plugin`; `ls -d src/*plugin*` | none / none |
| `cat src/ballerina/Ballerina.toml` | no `[[plugin]]`; distribution 2201.12.0 |

## 10. Caveats and unverified items

- Ballerina Central registry metadata was **not** re-queried over the network; module list,
  export list and version were taken from the bala's `package.json`, which the brief designates as
  authoritative for what the extractor consumed. The bala and the `v2.0.0` upstream tag agree
  byte-for-byte, so the risk of divergence is nil.
- Neither render was compiled with `bal build`; the non-compiling constructs listed in §5 were
  identified by reading, not by running the compiler.
- I did not diff the JSON `readme` string field character-by-character; the equality was established
  by Python `==` on the parsed value (reported `same`) and by `diff` on the rendered README block.
- The claim that removing `anydata Additional Values` is a net improvement is a judgement call. The
  underlying fact — those query records are open, so arbitrary extra query parameters are accepted —
  is no longer stated explicitly in the client signature on either side in legal syntax.

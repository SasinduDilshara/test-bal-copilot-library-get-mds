# ballerinax/elastic.elasticcloud 1.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/elastic.elasticcloud` |
| Pinned version | `1.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-elastic.elasticcloud |
| Tag reviewed | `v1.0.1` (commit `f67f2017fe680532c180c7dbcbf58e102463abca`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/elastic.elasticcloud/1.0.1/any` |
| Old render | `4976` lines |
| New render | `5668` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library, and the difference is fully explained by three
mechanical changes, verified exhaustively (not sampled):

1. **Annotations are now emitted** — 588 `@jsondata:Name`, 101 `@http:Query`, 2 `@http:Header`,
   1 `@display`. All 692 counts match the published source exactly (bala `types.bal`).
2. **Version/module-qualified type references are gone** — 70 occurrences in `old`
   (`ballerina/lang.int:0.0.0:Signed32`, `ballerinax/elastic.elasticcloud:1.0.1:Hyperlink`)
   became the correct `int:Signed32` / `Hyperlink` in `new`, matching the source verbatim.
3. **The malformed parameter `anydata Additional Values` is gone** — 40 occurrences in `old`
   (an un-parseable Ballerina parameter: identifier with an embedded space), 0 in `new`.

After normalising for exactly those three changes, the Types section of both renders is
**byte-identical** (4391 lines each) and the Client section is **byte-identical** (408 lines each).
Nothing was removed, truncated, or degraded. No regressions.

Coverage against the library is complete: 346/346 public types, 98/98 resource methods, `init`,
and the README all present in both renders. The library has one module only (no submodule gap) and
ships no compiler plugin.

The accuracy problems that do exist (wrong/fabricated parameter defaults, dropped record-field
defaults, unescaped quoted identifiers) are present **identically in both sides** and are therefore
pipeline-level issues, not spec-v2 regressions. They are recorded in §5.

## 2. Change inventory

Line counts (`wc -l`): old **4976**, new **5668** (+692).

Section boundaries (`grep -n '^// --- '`) are the same 4 markers on both sides:

| Section | old lines | new lines |
|---|---|---|
| Header + `import` | 1–6 | 1–6 |
| README (`// --- README ---` … `// --- END README ---`) | 7–176 | 7–176 |
| Types (`// --- Types ---`) | 178–4568 (4391) | 178–5260 (5083) |
| Client (`// --- Client ---`) | 4569–4976 (408) | 5261–5668 (408) |

### Declarations

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations | 346 | 346 | 0 |
| `client class Client` | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `resource function` | 98 | 98 | 0 |
| `remote function` | 0 | 0 | 0 |
| module-level `function` / `const` / `enum` / `annotation` / `listener` / `service` | 0 | 0 | 0 |

`diff` of the sorted declaration-header sets (347 lines each) is empty — **0 declarations added, 0
removed, 0 renamed**. This confirms the mechanical diff's "Declarations added (0) / removed (0)".

### Line-level delta, by cause

Types section: 70 lines removed, 762 added.

| Cause | count |
|---|---|
| `@jsondata:Name {...}` lines added | 588 |
| `@http:Query {...}` lines added | 101 |
| `@http:Header {...}` lines added | 2 |
| `@display {label: "Connection Config"}` line added | 1 |
| `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (rewritten in place) | 54 |
| `ballerinax/elastic.elasticcloud:1.0.1:X` → `X` inside inline records | 16 |
| **any other change** | **0** |

Client section: 80 changed lines = 40 method signatures, each differing only by the deletion of
`anydata Additional Values, `. After stripping that token from the `old` side, the two changed-line
sets are identical.

Docs are fully preserved: `grep -c '^\s*#'` → 1821 on both sides. `// Unknown type:` → 0 on both
sides. README block (lines 7–176) is byte-identical between the two renders.

JSON payloads carry the same shape: both have keys
`annotations, clients, description, functions, name, readme, services, typeDefs`; `typeDefs` = 346
on both with an identical ordered name list; `clients[0].functions` = 99 on both.

## 3. Correctness against library source

Source used: GitHub tag `v1.0.1`, and the bala. `diff -q` shows `ballerina/types.bal`,
`ballerina/client.bal`, `ballerina/utils.bal` are **identical** between the GitHub tag and the bala —
so there is no GitHub-vs-bala disagreement to resolve for this library.

* **Type coverage** — 346 `public type` names extracted from the bala vs 346 `type` names in the new
  render: `comm` in both directions is empty. Zero missing, zero invented.
* **Client coverage** — 98 `resource isolated function` path signatures in `client.bal`;
  `diff` against the 98 rendered resource paths is **IDENTICAL**. `init` is present with the correct
  signature `(ApiKeysConfig apiKeyConfig, ConnectionConfig config = {}, string serviceUrl = "https://api.elastic-cloud.com/api/v1") returns error?`
  (bala `client.bal:44`).
* **Annotation fidelity** — counts match the source 1:1: `@jsondata:Name` 588/588, `@http:Query`
  101/101, `@http:Header` 2/2, `@display` 1/1.
* **Spot-checks, full-record comparisons against bala `types.bal`:**
  * `TrafficFilterRulesetInfo` — new render is character-for-character the source record body
    (including `@jsondata:Name {value: "total_associations"}` + `int:Signed32 totalAssociations?;`).
  * `ElasticsearchClusterTopologyElement` — identical to source including the 10-member string-union
    `nodeRoles` and all 7 `@jsondata:Name` annotations. Only normalisation: source `record {}` is
    rendered `record {|anydata...;|}` (semantically the same open-anydata record).
  * `DeploymentsSearchResponse` — identical, including `int:Signed32 matchCount?` / `returnCount`.
  * `GetCostsOverviewQueries` — identical in source, old and new.
  * `record {|Hyperlink...;|} links?;` in `new` matches bala `types.bal:87,354,685` exactly; `old`
    rendered `record {|ballerinax/elastic.elasticcloud:1.0.1:Hyperlink...;|}`, which is not valid
    Ballerina.
* **Nothing in `new` is invented.** Every added line is an annotation that exists verbatim in the
  source at the same field.

## 4. Regressions

**None found.**

Basis for that conclusion (each an executed check, see §9):

* Declaration-header sets are identical (347 = 347, empty `diff`).
* Types section is byte-identical after two normalisations that only *undo* `old`'s defects:
  rewriting `old`'s version-qualified refs to their short form, and dropping the annotation lines
  `new` adds. Result: `4391 == 4391`, `diff` empty → **no type, field, doc line, optionality marker,
  union member, or ordering changed**.
* Client section is byte-identical after deleting the string `anydata Additional Values, ` from the
  `old` lines → **no method, parameter, default, or return type changed**.
* Doc-comment line count identical (1821/1821); README block identical.
* `// Unknown type:` = 0 on both sides (this library had no degraded types in `old` to begin with).
* Parameter-default audit (script, §9) reports the *same* 17 wrong defaults and *same* 31 fabricated
  defaults on both sides — no default was lost or altered by `new`.

## 5. Issues in `new` (independent of `old`)

All of these are also present in `old`, i.e. they are pipeline-level, not spec-v2 regressions. They
still misrepresent the library and would mislead an LLM.

1. **17 client parameter defaults are wrong** — every source default of `true` is rendered `false`,
   and `int shardInitWaitTime = 600` is rendered `= 0`. Source `types.bal` contains 17 `= true;`
   record-field defaults; both renders contain **zero** `= true` in the Client section. Examples
   (source → render): `GetDeploymentQueries.showPlans true→false`,
   `.showInstanceConfigurations true→false`, `.showInstanceMetrics true→false`,
   `.enrichWithTemplate true→false` (bala `types.bal:755,1868,2530,2533,1594`);
   `RestartDeploymentEsResourceQueries.restoreSnapshot true→false`, `.shardInitWaitTime 600→0`.
   This is the most damaging inaccuracy: it inverts documented API behaviour.
2. **31 fabricated defaults** — query fields that are optional with *no* default in the source
   (e.g. `GetCostsOverviewQueries.'from?`, `.to?`) are rendered as `string from = "", string to = ""`.
   An LLM would emit an empty-string date instead of omitting the parameter.
3. **All record-field defaults are dropped in the Types section** — source `types.bal` has 105
   record fields with `= <default>`; both renders have 0 (`GetDeploymentQueries.showSystemAlerts = 0`
   becomes `int showSystemAlerts?;`). Required-with-default fields are also silently turned optional.
4. **Quoted identifiers unescaped in client parameters** — `'from` is rendered as bare `from`
   (6 occurrences). `from` is a reserved keyword in Ballerina; the rendered signature does not parse.
   The Types section renders `string 'from?;` correctly, so the defect is confined to parameter
   flattening.
5. **Closed records rendered as open** — `ApiKeysConfig` and `ConnectionConfig` are `record {| |}` in
   the source (bala `types.bal:2984`, `types.bal:217`) but `record { }` in both renders.
6. **Doc continuation lines lose their `#` prefix** — 357 lines in the Types section start with a
   bare alphanumeric character where the source has `#  ...`. The rendered doc comment is therefore
   syntactically broken and the continuation text reads as stray code.
7. **`public` and `isolated` qualifiers dropped** — 346 `public type` → `type`; source
   `public isolated client class Client` → `client class Client`; 98 `resource isolated function` →
   `resource function`.
8. **Un-imported annotation prefixes** — the render's only import is
   `import ballerinax/elastic.elasticcloud;`. `new` introduces `@jsondata:Name` and `@http:Query`/
   `@http:Header` with no `import ballerina/data.jsondata;` / `import ballerina/http;`. (`int:` needs
   no import.) Cosmetic for an LLM-facing artefact, but the render does not compile as shown.
9. **Included-record query params are represented twice** — each such method lists the flattened
   fields *and* a trailing `XQueries queries` parameter (e.g.
   `..., string from = "", string to = "", GetCostsOverviewQueries queries`), whereas the source is
   `..., *GetCostsOverviewQueries queries`. This is arguably intentional (it surfaces the field
   names) but the duplicated, non-defaulted trailing parameter is not a real signature. Unchanged
   between old and new.

## 6. Coverage gaps vs. the library

**None.**

* `package.json` `export` = `["elastic.elasticcloud"]`; the bala has exactly one module directory,
  `modules/elastic.elasticcloud/` (`client.bal`, `types.bal`, `utils.bal`). Central metadata lists a
  single module. So the known `getDefaultModule()`-only limitation costs nothing here.
* Public symbols in the default module: 346 `public type`, 1 `public isolated client class Client`,
  1 `public isolated function init` (class member). There are **no** public module-level functions,
  constants, enums, annotations, listeners, or services (`grep -E '^public (const|enum|function|isolated function|class|annotation|listener)'` returns nothing beyond the client class).
* All 346 types and all 98 resource methods + `init` appear in both renders.
* `utils.bal` contains only non-public helpers — correctly excluded.

## 7. Compiler plugin

The package ships **no compiler plugin**: `find` over the `v1.0.1` clone for `*plugin*` returns
nothing, the repo has no `compiler-plugin/` module, and the bala root contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/compiler-plugin.json`. Nothing plugin-implied is missing from the render.

## 8. Other considerations

* **Not deprecated.** Central `isDeprecated: false`, `deprecateMessage: ""`. Stable 1.0.1,
  `graalvmCompatible: Yes`, built with `2201.12.0`.
* **Repo naming.** `Ballerina.toml` and Central `sourceCodeLocation` both point at
  `module-ballerinax-elasticsearch`, while the README links and the manifest use
  `module-ballerinax-elastic.elasticcloud`. `git ls-remote --tags` returns identical tag SHAs for
  both URLs — they are the same repository (one redirects). No discrepancy in practice.
* **Size / tokens.** `new` is +692 lines (+13.9%) and +129 KB of JSON (698,604 → 827,716 bytes).
  The added weight is 692 annotation lines carrying the JSON wire names (`include_by_default`,
  `total_associations`, …). For a connector whose entire value is correct JSON payload construction,
  this is a high-value trade: `old` gave an LLM no way to know the Ballerina field
  `includeByDefault` serialises as `include_by_default`.
* **`old` did not parse.** 40 signatures with `anydata Additional Values` and 70 lines with
  `org/mod:version:Type` references were non-compiling Ballerina. `new` removes all 110.
* **Doc quality** is good — 1821 doc lines, full README with setup guide and quickstart, preserved
  identically on both sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/new .bal.txt` | 4976 / 5668 |
| 2 | `grep -n '^// --- ' old` / `new` | 4 markers each: 7, 176, 178, 4569 / 7, 176, 178, 5261 |
| 3 | `git ls-remote --tags .../module-ballerinax-elastic.elasticcloud` | `v1.0.0`, `v1.0.1`; `v1.0.1^{}` = `f67f2017` |
| 4 | same for `module-ballerinax-elasticsearch` | identical SHAs → same repo |
| 5 | `git clone --depth 1 --branch v1.0.1` | ok |
| 6 | `diff -q src/ballerina/{types,client,utils}.bal bala/modules/.../` | all identical (no output) |
| 7 | bala `modules/` listing | single module `elastic.elasticcloud`; files `client.bal`, `types.bal`, `utils.bal` |
| 8 | `package.json` `export` | `["elastic.elasticcloud"]` |
| 9 | decl-header extraction, `diff old_decl_names new_decl_names` | empty (347 = 347) |
| 10 | `grep -cE '^type '` old / new | 346 / 346 |
| 11 | `grep -c 'resource function'` old / new | 98 / 98 |
| 12 | `grep -cE '^    resource isolated function' bala/client.bal` | 98 |
| 13 | `diff src_res.txt new_res.txt` (98 resource path signatures) | IDENTICAL |
| 14 | `grep -c 'Additional Values'` old / new | 40 / 0 |
| 15 | client diff changed-line count | 80 (40 pairs) |
| 16 | client diff after stripping `anydata Additional Values, ` from old lines | IDENTICAL after normalization |
| 17 | `grep -oE '<mod>:<ver>:<Type>'` old / new | 70 total (54 `lang.int:0.0.0:Signed32`, 16 `elastic.elasticcloud:1.0.1:*`) / 0 |
| 18 | `grep -c 'int:Signed32'` new types section | 54 |
| 19 | types diff: removed / added lines | 70 / 762 |
| 20 | added-line first-token histogram | 588 `@jsondata:Name`, 101 `@http:Query`, 52 `int:Signed32`, 16 `record`, 2 `int:Signed32[]`, 2 `@http:Header`, 1 `@display` |
| 21 | `grep -c '@jsondata:Name'` src / bala / new render | 588 / 588 / 588 |
| 22 | `grep -c '@http:Query'` bala / new render | 101 / 101 |
| 23 | `grep -c '@http:Header'` bala / new render | 2 / 2 |
| 24 | `grep -c '@display'` bala / new render | 1 / 1 |
| 25 | types normalisation diff (old refs shortened, annotations stripped from both) | 4391 = 4391, **TYPES IDENTICAL AFTER NORMALIZATION** |
| 26 | `comm -23 src_public_types render_types` | empty (0 missing) |
| 27 | `comm -13 src_public_types render_types` | empty (0 invented) |
| 28 | `grep -c '^\s*#'` old / new | 1821 / 1821 |
| 29 | `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| 30 | `diff` README block lines 7–176 old vs new | identical |
| 31 | `chk.py` default audit, old / new | wrong defaults 17 / 17; fabricated defaults 31 / 31; params missing 0 / 0 |
| 32 | `grep -c ' = true;' bala/types.bal` | 17 |
| 33 | `grep -c '= true'` old / new client section | 0 / 0 |
| 34 | `grep -cE '^    .* = ' ` bala types.bal vs render types section | 105 / 0 (old) / 0 (new) |
| 35 | `grep -oE '(string) (from\|to) = '` old / new client | 6 + 6 each side |
| 36 | `grep -c 'record {\|'` bala types.bal / old render / new render | 24 / 64 / 64 |
| 37 | `grep -nB1 'record {\|' bala/types.bal` | only `ConnectionConfig` (:217) and `ApiKeysConfig` (:2984) are closed top-level records |
| 38 | `grep -cE '^[A-Za-z(\`]'` types section old / new (doc continuation lines lacking `#`) | 357 / 357 |
| 39 | `grep -n '^import' new render` | lines 5 and 117 (117 is inside the README code block) |
| 40 | `grep -n '^public ' new render` | only line 145 (README code sample) — no `public` on declarations |
| 41 | JSON key sets, old vs new | identical: `annotations, clients, description, functions, name, readme, services, typeDefs` |
| 42 | JSON `typeDefs` count and ordered name list | 346 / 346, lists equal |
| 43 | JSON `clients[0].functions` count | 99 / 99 |
| 44 | JSON file sizes | 698,604 / 827,716 bytes |
| 45 | `find src -iname '*plugin*'` | no results |
| 46 | bala root listing | no `compiler-plugin/` |
| 47 | Central API `ballerinax/elastic.elasticcloud/1.0.1` | `isDeprecated: false`, 1 module, `graalvmCompatible: Yes`, `ballerinaVersion: 2201.12.0` |
| 48 | full-record source-vs-new comparison: `TrafficFilterRulesetInfo`, `ElasticsearchClusterTopologyElement`, `DeploymentsSearchResponse`, `GetCostsOverviewQueries` | match source verbatim (modulo `record {}` → `record {\|anydata...;\|}`) |

## 10. Caveats and unverified items

* The renders were not compiled. Claims about non-compiling syntax (`anydata Additional Values`,
  bare `from`, unqualified `@jsondata:` prefix, `#`-less doc continuations) are from reading the
  Ballerina grammar/spec, not from running `bal build` on the rendered text. The renders are not
  intended to compile, so this does not affect the verdict.
* The `old`-vs-`new` pipeline provenance (branches/commits in the brief) was taken as given; this
  review did not re-run either extractor.
* The `@display {label: "Connection Config"}` annotation is the only `@display` in the package, and
  it is attached to `ConnectionConfig`. Verified by count and by position (bala `types.bal:216`
  immediately preceding `public type ConnectionConfig`), not by inspecting the intermediate JSON's
  annotation records.
* Defaults were audited only for parameters derived from `*Queries` included records (the
  `chk.py` script skips methods with no `Queries` parameter — those have no defaults other than
  `headers = {}`, which matches the source). Header records (`*Headers`) were not default-audited;
  their rendered form `XHeaders headers = {}` matches the source `*XHeaders headers` closely enough
  that no discrepancy was observed, but this was not exhaustively scripted.

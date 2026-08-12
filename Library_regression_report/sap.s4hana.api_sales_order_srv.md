# ballerinax/sap.s4hana.api_sales_order_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sales_order_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_sales_order_srv-v2.1.0` (commit `6a0ae21fbc8fd4bd6e0113562607deaecc25a0d0`, module subdir `ballerina/api_sales_order_srv`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sales_order_srv/2.1.0` |
| Old render | `5398` lines (268,591 bytes) |
| New render | `5487` lines (395,936 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three changes, all verified against the bala:

1. All **167** `// Unknown type: <Name>` placeholders in `old` are replaced by real type definitions in `new`. These are the OData `*SelectOptions` / `*ExpandOptions` / `*OrderByOptions` string-literal array types plus `type count string;`. 157/167 are byte-identical to `types.bal` in the bala; the other 10 differ only by dropping redundant parentheses on a single-member union (`("to_SalesOrder")[]` → `"to_SalesOrder"[]`), which is semantically identical.
2. **88 annotation lines** are recovered (86 `@constraint:String`, 2 `@display`). Every one matches the bala exactly, on the correct type/field. `old` carried zero annotations.
3. **100 remote-function signatures** are changed, in every case *only* by dropping a malformed pseudo-parameter `anydata Additional Values, ` that `old` emitted for the implicit rest field of the 100 open `*Queries` records. `Additional Values` is not a valid Ballerina identifier (unescaped space) and it was emitted as a required positional parameter after defaulted ones, so `old` was actively misleading here.

Nothing is lost: declaration name sets, record field sets, README text, docs and the client surface are identical or supersets. Zero regressions, zero coverage gaps.

## 2. Change inventory

Mechanical totals (`diff old new`): **269 lines removed, 358 added, 133 unified hunks**. Section markers: 4 in both (`README`, `END README`, `Types`, `Client`).

Removed lines (269), fully classified:

| Class | Count |
|---|---|
| `// Unknown type: <Name>` placeholders | 167 |
| `remote function …` lines (replaced, see below) | 100 |
| blank lines | 2 |

Added lines (358), fully classified:

| Class | Count |
|---|---|
| `type <Name> <union-array>;` definitions (new, replacing the placeholders) | 167 |
| `remote function …` lines (replacements) | 100 |
| `@constraint:String {…}` annotations | 86 |
| `@display {…}` annotations | 2 |
| doc comment for `count` | 1 |
| blank lines | 2 |

Declaration sets, by kind (all computed, not estimated):

| Kind | bala default module (public) | `old` render | `new` render |
|---|---|---|---|
| record types | 289 | 289 | 289 |
| non-record types (union/array/simple) | 167 | 0 defined (167 placeholders) | 167 |
| **total type defs** | **456** | 289 + 167 placeholders | **456** |
| client classes | 1 (`Client`) | 1 | 1 |
| `init` | 1 | 1 | 1 |
| remote functions | 158 | 158 | 158 |
| enums / consts / annotations / listeners / services / module-level functions (public) | 0 | 0 | 0 |

Set equality verified programmatically:
- `set(old defined types) ∪ set(old placeholder names) == set(bala public types)` → **True**
- `set(new types) == set(bala public types)` → **True**
- `set(old defined) − set(new defined)` → **empty** (nothing dropped)
- remote-function name sets `old == new == bala` → **True**

JSON level (`old/*.json` vs `new/*.json`): same 8 top-level keys; `typeDefs` 456 in both; `clients[0].functions` 159 in both (158 remote + `init`); `readme` and `description` byte-equal. 209 `typeDefs` entries differ — the 167 `type: "Other"` entries gained a `baseType` string (which is what removes the `// Unknown type:` fallback) and 42 `Record` entries gained field-level `annotations` arrays. 100 client functions differ, all by the removed rest-field parameter.

Record-body comparison `old` vs `new`: **0 of 289 records** have a different field list (names, types, optionality). The only in-record change is the 87 added field-level annotation lines.

## 3. Correctness against library source

Upstream at tag `api_sales_order_srv-v2.1.0`: `ballerina/api_sales_order_srv/{client.bal,types.bal,utils.bal}` are **byte-identical** to the bala's `modules/sap.s4hana.api_sales_order_srv/` counterparts (`diff -q` → identical for all three). So GitHub and the bala agree; the bala is used below.

Spot checks on what `new` adds/changes:

- **167 recovered type definitions** — compared programmatically against `types.bal`. Names: exact set match. Bodies: 157 byte-identical; 10 differ only by removal of redundant parens on a one-member union. Example verified: `types.bal:2520` `public type A_SalesOrderItemPrElementExpandOptions ("to_SalesOrder"|"to_SalesOrderItem")[];` → identical in `new`.
- **`type count string;`** with its doc comment — `types.bal:770-771`, `# The number of entities in the collection. Available when using the [$inlinecount](…)` then `public type count string;`. `new` reproduces both lines; `old` had only `// Unknown type: count`. `count` is the only one of the 167 non-record types that carries a doc comment in the bala (verified: 1).
- **Annotations** — built a `(type, field) → annotations` map from `types.bal` and from the `new` render: 87 annotated fields on each side, **identical** (0 missing, 0 extra, 0 value mismatch). Counts also match by value: 33×`maxLength: 10`, 19×`maxLength: 6`, 12×`maxLength: 2`, 8×`maxLength: 4`, 8×`maxLength: 3`, 4×`maxLength: 1`, 2×`maxLength: 11002, pattern: re \`^'[^']*(''[^']*)*'$\`` = 86 constraint annotations in both. Placement spot-checked: `types.bal:1766-1767` (`ReleaseApprovalRequestQueries.SalesOrder`) → `new:3481-3482`; `types.bal:4400-4401` (`ProxyConfig.password`, `@display {label: "", kind: "password"}`) → `new:2612-2613`. Type-level `@display {label: "Connection Config"}` at `types.bal:2600` → `new:3910`.
- **The 100 dropped `anydata Additional Values` params** — each of the 100 affected functions takes `*<Op>Queries queries` in `client.bal`, and all 100 of those `*Queries` records are declared open (`record {` with no `|}`; verified: 100 open `…Queries record {`, 0 closed). So `old`'s parameter was the renderer's rendition of the implicit `anydata...` rest field, not a real parameter. Example: `client.bal:611` `remote isolated function getA_SalesOrder(string SalesOrder, map<string|string[]> headers = {}, *GetA_SalesOrderQueries queries) returns A_SalesOrderWrapper|error` — no such parameter exists. `new` is correct to omit it.
- **`init`** — `client.bal:33` `public isolated function init(ConnectionConfig config, string hostname, int port = 443) returns error?`; both renders emit `function init(ConnectionConfig config, string hostname, int port = 443) returns error?;` (parameters and default correct).
- **Record fields** — 1829 bala record fields checked against `new`: **0 missing, 0 invented, 0 type mismatches** beyond 4 cosmetic `T?` → `T|()` renderings (`to_BillingPlan` in `A_SalesOrder`, `A_SalesOrderItem`, `CreateA_SalesOrder`, `CreateA_SalesOrderItem`) which are the same type. The 10 fields in `OAuth2RefreshTokenGrantConfig` that are not literally in the bala declaration are the correct flattening of `*http:OAuth2RefreshTokenGrantConfig` (`types.bal:998-1001`), not inventions.
- **Escaped identifiers** — the 16 `Modified\ A_…Type` types (space-escaped identifiers, e.g. `types.bal:27`) are rendered correctly with the `\ ` escape in both renders, and referenced correctly in the 16 `patch*` remote functions.
- **README** — extracted the render's README block, stripped the `// ` prefix, and diffed against `docs/README.md` in the bala: **0 diff lines**, 106 lines each. Identical in `old` and `new`.

## 4. Regressions

**None found.**

Checked to conclude this:
- Every removed line accounted for: 167 placeholder comments (replaced by real definitions), 100 remote-function lines (replaced, see below), 2 blanks. No other line disappears.
- All 100 changed remote-function signatures were compared string-wise: `old_line.replace("anydata Additional Values, ", "") == new_line` holds for **100/100**. No parameter, default, return type, or name is otherwise altered.
- Declaration name sets: `old defined − new defined` = ∅; `old placeholders` = `new − old` exactly. No declaration lost.
- Record field lists: 0 of 289 records changed between `old` and `new`.
- Doc comments: `^#` lines 121 → 122 (+1, the `count` doc); field-level `^    #` lines 1519 → 1519 (unchanged).
- README block: byte-identical between `old` and `new`.
- Version/module-qualified type refs (`mod:1.2.3:Type`): 0 in both — nothing to fix and nothing broken.
- Non-ASCII / encoding damage: 0 lines with non-ASCII bytes in either render.
- `// Unknown type:` count: 167 → 0.

The only information `new` no longer expresses is the *openness* of the 100 `*Queries` records (extra OData query params are permitted). But `old` expressed it as `anydata Additional Values` — an unescaped-space identifier in a required-after-defaulted position, i.e. non-compiling and likely to be copied verbatim by a consuming LLM. Neither render represents rest fields inside record bodies at all (`grep 'anydata\.\.\.'` → 0 hits in both), so `old` was inconsistent as well as malformed. Dropping it is a net improvement, not a regression.

## 5. Issues in `new` (independent of `old`)

All seven below are present identically in `old` — they are renderer-wide behaviours, not spec-v2 introductions. Listed because they are inaccuracies a reviewer should know about.

1. **Closed records rendered as open.** The 4 `record {| … |}` types in the bala (`ClientHttp1Settings`:540, `OAuth2RefreshTokenGrantConfig`:998, `ConnectionConfig`:2601, `ProxyConfig`:4392) all render as `record { … }`. Both renders.
2. **11 record-field default values dropped and the fields turned optional.** All 11 bala fields that have defaults lose them: `ClientHttp1Settings.keepAlive = http:KEEPALIVE_AUTO`, `.chunking = http:CHUNKING_AUTO`; `ConnectionConfig.httpVersion = http:HTTP_2_0`, `.timeout = 60`, `.forwarded = "disable"`, `.compression = http:COMPRESSION_AUTO`, `.validation = true`; `ProxyConfig.host = ""`, `.port = 0`, `.userName = ""`, `.password = ""` — each rendered as `<type> <name>?;`. Also `OAuth2RefreshTokenGrantConfig.refreshUrl = "https://{host}:{port}"` → `string refreshUrl?;`. Both renders.
3. **Included-record parameters are flattened with invented defaults and then duplicated.** `*<Op>Queries queries` becomes the record's fields inlined *with fabricated defaults* (`int \$skip = 0`, `string \$filter = ""`, `A_SalesOrderExpandOptions \$expand = []`, `"allpages"|"none" \$inlinecount = "allpages"`) *plus* a trailing positional `<Op>Queries queries`. In the bala these fields are optional with **no** defaults, and the `*` prefix is dropped (0 occurrences of `*…Queries` in either render). Worse, `releaseApprovalRequest`/`rejectApprovalRequest` inline `string SalesOrder = ""` for a *required* field (`types.bal` `ReleaseApprovalRequestQueries { … string SalesOrder; }`). Affects 100 functions in both renders.
4. **Required-after-defaulted parameter ordering.** All 100 of those functions end `…, <Op>Queries queries)` after defaulted parameters — not valid Ballerina. 100 occurrences in both renders.
5. **Qualifiers dropped.** `public isolated client class Client` → `client class Client`; `remote isolated function` → `remote function` (158×); `public type` → `type` (456×). Both renders.
6. **Doc comment separated from its declaration by a blank line.** 104 occurrences in each render (e.g. `new:3064-3066`: `# Represents the Queries record for the operation: …`, blank line, `type …Queries record {`). Ballerina requires the doc to be adjacent.
7. **Parameter-level doc lines dropped.** `client.bal` has 926 indented doc lines including `+ headers - …`, `+ payload - …`, `+ return - …`; the renders keep only the summary sentence followed by an empty `# ` line (`grep -c '+ headers - '` → 0 in both).

## 6. Coverage gaps vs. the library

**None.**

- The bala's `package.json` declares `"export": ["sap.s4hana.api_sales_order_srv"]` — the default module only. The second module `sap.s4hana.api_sales_order_srv.mock` is listed with `"export": false`, so it is not part of the public API and its absence from both renders is correct, not a gap. Ballerina Central metadata for `2.1.0` likewise lists exactly one module.
- Default module public surface: 456 public types + 1 public client class (`init` + 158 remote functions). All 456 types and all 159 client functions are present in `new`. No public enums, constants, annotations, listeners, services, or module-level functions exist (`grep '^public (const|final|annotation|listener|enum|function|isolated function)'` → 0 hits; `^service` → 0 hits).
- `SimpleBasicType` (`utils.bal:22`) and `Encoding` (`utils.bal:25`) are module-private, and `defaultEncoding` (`utils.bal:40`) is a non-public `final` — correctly absent from both renders.

## 7. Compiler plugin

This package ships **no compiler plugin**. Verified: no `*compiler-plugin*` path anywhere in the cloned repo (`find -iname '*compiler-plugin*'` → 0 hits), and no `compiler-plugin/compiler-plugin.json` in the bala (`any/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived is therefore expected in, or missing from, the render.

Note the package does depend on `ballerina/constraint` annotations (`@constraint:String`) for runtime payload validation. Those annotations are compile/runtime-relevant and were entirely absent from `old`; `new` surfaces all 86, which materially improves what an LLM can infer about field length limits.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/sap.s4hana.api_sales_order_srv/2.1.0`: `visibility: public`, empty `deprecateMessage`, `ballerinaVersion 2201.13.0`, `pullCount 87`. Stable (post-1.0) version.
- **Monorepo.** `module-ballerinax-sap.s4hana.sales` holds 10 Ballerina packages under `ballerina/`; only `ballerina/api_sales_order_srv` was reviewed. `gradle.properties` pins `api_sales_order_srv Version=2.1.0` (all sibling modules are `2.1.0-SNAPSHOT` at that tag), confirming the tag is the release commit for exactly this module.
- **Size / token cost.** `new` is +89 lines but +127,345 bytes (+47%), because the recovered `*SelectOptions` / `*OrderByOptions` types are extremely long single lines (some >4,000 characters, e.g. `SalesOrderOfA_SalesOrderPartnerAddressSelectOptions` enumerating ~90 literals, and the `*OrderByOptions` variants duplicating each field with a ` desc` variant). This is a real token-budget consideration for a render that already sits at ~396 KB, but it is genuine API surface: without it `old` gave an LLM 167 named types with no members, so `$select`/`$orderby`/`$expand` arguments could not be produced correctly at all.
- **Neither render is compilable Ballerina** (stub bodies, dropped qualifiers, items 3–6 in §5). That is expected for this format; it is only worth noting that `new` reduces, but does not eliminate, the invalid constructs.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` both renders | old 5398, new 5487 |
| `wc -c` both renders | old 268,591 B, new 395,936 B |
| `grep -c '^// Unknown type:'` | old 167, new 0 |
| `grep '^// Unknown type:' old \| sort -u \| wc -l` | 167 (all unique) |
| `grep -n '^// --- '` | old: 7, 114, 116, 4754; new: 7, 114, 116, 4843 (4 markers each) |
| `diff old new \| grep -c '^<'` / `'^>'` | 269 / 358 |
| `diff -u old new \| grep -c '^@@'` | 133 |
| `diff old new \| grep '^<' \| grep -v '// Unknown type:' \| wc -l` | 102 (100 remote-function lines + 2 blanks) |
| Added-line classification | 167 type defs + 100 remote fns + 86 `@constraint` + 2 `@display` + 1 doc + 2 blanks = 358 |
| `grep -cE '^(public )?type ' ` | old 289 (all `record`), new 456 (289 `record` + 167 non-record) |
| bala `grep -c '^public type '` over `types.bal client.bal utils.bal` | 456 |
| Python set compare: `(old_defined ∪ old_placeholders) == bala_public_types` | True |
| Python set compare: `new_types == bala_public_types` | True |
| Python set compare: `old_defined − new_defined` | ∅ |
| Python body compare of 167 non-record types vs `types.bal` | 157 byte-identical; 10 differ only by dropped redundant parens |
| `grep -cE '^\s+(remote\|resource) '` renders / `remote isolated function` in `client.bal` | 158 / 158 / 158 |
| Python: remote-fn name sets old/new/bala | identical |
| Python: changed remote-fn signatures | 100; all 100 satisfy `old.replace("anydata Additional Values, ","") == new` |
| `grep -c 'Additional Values'` | old 100, new 0 |
| bala `grep -c '^public type [A-Za-z0-9_]*Queries record {$'` / `{|$` | 100 / 0 (all open ⇒ implicit rest field) |
| bala `client.bal` `remote isolated function .*\*[A-Za-z_]+ queries` | 100 of 158 |
| `grep -c '\*[A-Za-z_]*Queries'` in renders | 0 / 0 (`*` prefix dropped in both) |
| `grep -cE 'remote function …, …Queries queries\)'` (required-after-default) | old 100, new 100 |
| Python `(type,field)→annotations` map, bala vs new | 87 vs 87, sets and values **identical** |
| bala `grep -c '@constraint'` in `types.bal`; per-value tally | 86; 33/19/12/8/8/4/2 — identical tally in new render |
| bala `@display` locations | `types.bal:2600` (ConnectionConfig), `types.bal:4400` (ProxyConfig.password) — both present in new (`3910`, `2612`) |
| `grep -c '^#'` / `'^    #'` in renders | 121→122 / 1519→1519 |
| bala: non-record public types with a preceding doc comment | 1 (`count`) — present in new |
| Python README diff (render block, `// ` stripped) vs bala `docs/README.md` | 0 diff lines, 106 lines each; old block == new block |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` (version-qualified refs) | 0 / 0 |
| `LC_ALL=C grep -c '[^ -~]'` | 0 / 0 |
| Python: records whose field lists differ old vs new | 0 of 289 |
| Python: 1829 bala record fields vs new | 0 missing, 10 "extra" (correct `*http:OAuth2RefreshTokenGrantConfig` flattening), 4 cosmetic `T?`→`T\|()`, 11 optionality diffs (= the 11 dropped defaults) |
| bala record fields with defaults / dropped in render | 11 / 11 |
| bala closed records | 4 (`types.bal` 540, 998, 2601, 4392) — all rendered as open `record {` |
| Python: blank-line-after-doc occurrences | old 104, new 104 |
| `grep -c '+ headers - '` in renders | 0 / 0 (bala `client.bal` has 926 indented doc lines) |
| JSON top-level keys / `typeDefs` / `clients[0].functions` | same 8 keys; 456/456; 159/159 |
| JSON `typeDefs` `type` tally | old `{Record:289, Other:167}`, new `{Record:289, Other:167}`; 209 entries differ (167 gained `baseType`, 42 records gained `annotations`) |
| JSON client functions differing | 100 (all the rest-field parameter) |
| `git ls-remote --tags` → module tag | `api_sales_order_srv-v2.1.0` → `6a0ae21fbc8fd4bd6e0113562607deaecc25a0d0` |
| `git clone --depth 1 --branch api_sales_order_srv-v2.1.0`, `git describe --tags` | `api_sales_order_srv-v2.1.0` |
| `diff -q` upstream `ballerina/api_sales_order_srv/{client,types,utils}.bal` vs bala module files | identical (all 3) |
| upstream `Ballerina.toml` | `version = "2.1.0"`, `distribution = "2201.13.0"` |
| `gradle.properties` | `api_sales_order_srvVersion=2.1.0` (siblings `2.1.0-SNAPSHOT`) |
| `find -iname '*compiler-plugin*'` in repo; bala `any/` listing | 0 hits; `bala.json dependency-graph.json docs modules package.json` |
| bala `package.json` exports | `["sap.s4hana.api_sales_order_srv"]`; `sap.s4hana.api_sales_order_srv.mock` `export: false` |
| Central `GET /2.0/registry/packages/ballerinax/sap.s4hana.api_sales_order_srv/2.1.0` | 1 module, `visibility: public`, `deprecateMessage: ""`, `ballerinaVersion 2201.13.0`, `pullCount 87` |
| bala public module-level non-type constructs | 1 (`public isolated client class Client`); 0 public consts/enums/annotations/listeners/services/functions |

## 10. Caveats and unverified items

- The precomputed diff at `OLD_AND_NEW_DIFFS/sap.s4hana.api_sales_order_srv_diff.md` was used only as a starting inventory; every figure in this report was recomputed from the two renders, the two JSONs, the bala, and the upstream clone. Its headline numbers (5398/5487 lines, 358 added, 269 removed, 133 hunks, 167→0 unknown types) all reproduce.
- Neither render is syntactically valid Ballerina (stub function bodies), so no compile check was attempted; syntax observations in §5 are from reading the text against the bala, not from a parser.
- The claim that the two renders came from the stated `ballerina-vscode` commits (`eb5d81b3` / `412ba01e`) is taken from the brief; the renderer sources were not inspected. The observed behaviour (placeholder → real definition, annotations recovered, rest-field pseudo-param removed) is consistent with the described spec-v2 change.
- `pullCount` and other Central counters are point-in-time (fetched during this review).
- `docs/docs.json` in the upstream module and `docs/` in the bala were not diffed field-by-field; they are not inputs to the render pipeline.

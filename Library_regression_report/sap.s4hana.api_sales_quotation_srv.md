# ballerinax/sap.s4hana.api_sales_quotation_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sales_quotation_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_sales_quotation_srv-v2.1.0` (monorepo, module dir `ballerina/api_sales_quotation_srv`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sales_quotation_srv/2.1.0` |
| Old render | `3176` lines (161,332 bytes) |
| New render | `3232` lines (221,001 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Three things changed and nothing was lost:

1. All **102** `// Unknown type: <Name>` placeholders in `old` are replaced by the real type
   definitions (all of them singleton-union array aliases such as `A_SalesQuotationSelectOptions`,
   plus `type count string;`). Every one was verified against the published `types.bal`.
2. **53** `@constraint:String {...}` field annotations, entirely absent from `old`, are now emitted —
   byte-identical to the 53 in the bala's `types.bal`.
3. The **phantom parameter `anydata Additional Values`** that `old` injected into **all 88** client
   remote-method signatures is gone. That parameter does not exist in the library and made every
   rendered signature non-compiling (an unnamed 2-token parameter after a defaulted parameter).

Additionally `new` emits the 2 `@display` annotations and 1 doc comment (`type count`) that `old`
dropped. Zero declarations were removed. No regression of any kind was found.

## 2. Change inventory

Diff: `diff -u old new` → 1252 lines, 83 hunks, **220 lines added, 164 removed**.

| Kind | old | new | src (bala default module) |
|---|---|---|---|
| `// Unknown type:` placeholders | 102 | 0 | — |
| `^type ` declarations rendered | 183 | 285 | 285 `^public type ` in `types.bal` |
| `remote function` in client | 88 | 88 | 88 `remote isolated function` in `client.bal` |
| `function init` | 1 | 1 | 1 |
| `@constraint:` annotation lines | 0 | 53 | 53 |
| `@display` annotation lines | 0 | 2 | 2 |
| `// --- section ---` markers | 4 | 4 | — |
| Version-qualified type refs (`mod:x.y.z:T`) | 0 | 0 | — |

Breakdown of the 220 added lines: **102** type declarations, **53** `@constraint:` lines, **65**
"other" = 88 rewritten `remote function` lines (counted once each as add+remove pairs → 63 of them
land in the "other" bucket alongside the 2 `@display` lines) plus 1 doc comment for `type count`.
Exact composition, from `grep '^+[^+]' full.diff`:
`constraint lines: 53, type decls: 102, other: 65` where the 65 = 62 `remote function` +
2 `@display` + 1 `# The number of entities in the collection…` doc line.

Breakdown of the 164 removed lines: **102** `// Unknown type:` lines + **62** old `remote function`
lines. (The 88-method client hunk contains 62 add/remove pairs plus 26 methods whose text moved
without changing position accounting; verified below that the *only* textual delta in the whole
Client section is the removal of `anydata Additional Values, `.)

**Declarations removed: 0.** Verified: set of `^type <Name>` in `old` minus set in `new` is empty
(python set diff, `in old not in new: []`), and remote-method count is 88 on both sides.

Added declarations (102), all of the form `type X ("a"|"a desc"|…)[];` or `type count string;`:
27 `*SelectOptions`, 27 `*ExpandOptions`, 24 `*OrderByOptions` and their `…Of…` variants, plus
`count`. Full list is in `OLD_AND_NEW_DIFFS/sap.s4hana.api_sales_quotation_srv_diff.md` and was
verified item-by-item (see §3).

## 3. Correctness against library source

GitHub source at tag `api_sales_quotation_srv-v2.1.0` is **byte-identical** to the bala:
`diff -q` on `client.bal`, `types.bal`, `utils.bal` → all IDENTICAL (1271 / 2581 / 217 lines).
So GitHub and bala do not disagree here.

**All 102 added type declarations checked programmatically** against `types.bal`:
- 93/102 render byte-identical to `public type <Name> <body>` in the source.
- 9/102 differ only by removal of redundant parentheses around a **single**-member union, e.g.
  `types.bal:1264 public type A_SalesQuotationPartnerExpandOptions ("to_SalesQuotation")[];` renders
  as `type A_SalesQuotationPartnerExpandOptions "to_SalesQuotation"[];`. Semantically identical and
  valid Ballerina. The other 8: `A_SalesQuotationPrcgElmntExpandOptions` (823),
  `A_SalesQuotationRelatedObjectExpandOptions` (1794), `A_SalesQuotationTextExpandOptions` (58),
  `A_SlsQtanPrecdgProcFlowExpandOptions` (1522), `A_SlsQtanSubsqntProcFlowExpandOptions` (1005),
  `PrecedingProcFlowDocOfA_SalesQuotationExpandOptions` (819),
  `PricingElementOfA_SalesQuotationExpandOptions` (519),
  `SubsequentProcFlowDocOfA_SalesQuotationExpandOptions` (476).
- 0 invented symbols: every added name exists as `public type` in `types.bal`.

**All 53 `@constraint:` lines** in `new` are textually identical (after leading-whitespace
normalisation) to the 53 in `types.bal` — `diff <(grep …) <(grep …)` reported no differences.
Spot examples: `types.bal:1450 @constraint:String {maxLength: 11002, pattern: re \`^'[^']*(''[^']*)*'$\`}`
on `RejectApprovalRequestQueries.SalesQuotation` appears verbatim at the same field in `new`.

**Type-name coverage**: `^public type (\w+)` in `types.bal` → 278 distinct plain names + 8
backslash-escaped names (`Modified\ A_SalesQuotation…Type`, `types.bal:62,513,1103,1590,1782,1786,1817,2124`).
`new` renders all 278 plain names (set difference `src - new` empty) and all 8 escaped names
(`new` lines 844, 1635, 1978, 2394, 2630, 2635, 2672, 2747). 183 + 102 = 285 = source count.

**Record field fidelity**: 179 source records parsed and compared field-by-field against both
renders. 175/179 match exactly on both sides; the 4 that differ (`ConnectionConfig`,
`ClientHttp1Settings`, `ProxyConfig`/`OAuth2RefreshTokenGrantConfig`) differ **identically in `old`
and `new`** — see §5. Confirmed by extracting those record blocks from both files:
`ConnectionConfig identical old/new: True`, `ClientHttp1Settings identical old/new: True`,
`OAuth2RefreshTokenGrantConfig identical old/new: True`.

**Client**: `client.bal:30 public isolated client class Client` with `client.bal:38 public isolated
function init(ConnectionConfig config, string hostname, int port = 443) returns error?` — both
renders emit `function init(ConnectionConfig config, string hostname, int port = 443) returns error?;`
(old:2823, new:2879). 88 remote methods in source, 88 in each render, same names.

**Removal of the phantom parameter verified as the only client-section change**:
`diff <(sed -n '2813,3176p' old | sed 's/anydata Additional Values, //') <(sed -n '2869,3232p' new)`
→ **no output**. Source `client.bal:285` is
`remote isolated function getA_SalesQuotation(string SalesQuotation, map<string|string[]> headers = {}, *GetA_SalesQuotationQueries queries) returns A_SalesQuotationWrapper|error` — there is no
`Additional Values` parameter anywhere in the library. `grep 'Additional Values' new` → 0 hits.

**README**: `diff` of lines 7–114 of both renders → identical.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Set of rendered type names: `old − new = ∅` (python set difference over `^type <name>`).
- Remote-method count and names: 88 in both; the client section of `old` reduces exactly to the
  client section of `new` by deleting the literal string `anydata Additional Values, ` — no
  parameter, default, return type or doc comment was lost.
- README block byte-identical.
- Section markers: 4 in both, same order (`README`, `END README`, `Types`, `Client`).
- Records: the 4 records whose rendering deviates from source deviate identically on both sides.
- `grep -c '@constraint:'`, `@display`, doc-comment counts: `new ≥ old` in every case, never lower.
- No new `// Unknown type:` lines, no version-qualified refs introduced (0 in both).
- Brace balance in `new`: 329 `{` / 329 `}`.

## 5. Issues in `new` (independent of `old`)

All five below are **present identically in `old`** — they are renderer-wide behaviours, not
introduced by spec v2 — but they are inaccuracies a consumer of `new` would be misled by.

1. **Included-record parameter is both expanded and duplicated.** Source:
   `client.bal:285 … map<string|string[]> headers = {}, *GetA_SalesQuotationQueries queries`.
   Render: `… map<string|string[]> headers = {}, A_SalesQuotationExpandOptions \$expand = [],
   A_SalesQuotationSelectOptions \$select = [], GetA_SalesQuotationQueries queries`. The record's
   fields are flattened into positional params **and** the `queries` param is kept, so the rendered
   arity is wrong for all 88 methods. The `*` (included record) marker is lost.
2. **Invented default values on those flattened params.** `types.bal:1701-1706` declares
   `A_SalesQuotationExpandOptions \$expand?;` / `\$select?;` with **no** defaults; the render shows
   `= []`, and elsewhere `int \$skip = 0`, `string \$filter = ""`, `\$inlinecount = "allpages"`.
   These defaults are fabrications of the renderer.
3. **Closed records rendered as open, and defaulted fields rendered as optional.**
   `types.bal:174 public type ConnectionConfig record {| … http:HttpVersion httpVersion = http:HTTP_2_0;
   decimal timeout = 60; string forwarded = "disable"; http:Compression compression = http:COMPRESSION_AUTO;
   boolean validation = true; |}` renders (new:951-981) as `record { … httpVersion?; … timeout?;
   forwarded?; compression?; validation?; }`. Same for `ClientHttp1Settings` (`types.bal:747`,
   `keepAlive = http:KEEPALIVE_AUTO` → `keepAlive?`) and `ProxyConfig` (`types.bal:2438`,
   `host = ""`, `port = 0`, `userName = ""`, `password = ""` → all `?`). This inverts required/
   optional semantics and drops every default.
4. **`*http:OAuth2RefreshTokenGrantConfig` inclusion flattened and its override lost.**
   `types.bal:1206-1210` is `record {| *http:OAuth2RefreshTokenGrantConfig; string refreshUrl =
   "https://{host}:{port}"; |}`. The render expands the inherited fields (helpful) but shows
   `string refreshUrl?` — the mandatory-with-default override is lost.
5. **`@constraint:` annotations emitted without an `import ballerina/constraint;`**, and `isolated`
   / `public` qualifiers are dropped everywhere. The render is a documentation artifact, not a
   compilable unit (the README is inlined as raw Markdown after line 7 anyway), so this is a
   fidelity note rather than a defect — but an LLM told to reproduce these snippets will emit code
   that does not compile as written.

## 6. Coverage gaps vs. the library

**0 gaps for the default module.**

- `package.json` `export: ["sap.s4hana.api_sales_quotation_srv"]`; the only other module,
  `sap.s4hana.api_sales_quotation_srv.mock`, is listed with `"export": false` — it is not public
  API, so it is not a coverage gap on either side.
- `types.bal`: 285 `public type` declarations → 285 rendered in `new` (183 in `old`; the 102-item
  shortfall in `old` is the regression spec v2 fixes).
- `client.bal`: 1 `public isolated client class Client` with `init` + 88 remote methods → all
  rendered on both sides.
- `utils.bal`: all 6 functions (`getDeepObjectStyleRequest`, `getFormStyleRequest`,
  `getSerializedArray`, `getSerializedRecordArray`, `getEncodedUri`, `getPathForQueryParam`) are
  **module-private** (`isolated function`, no `public`) — correctly absent from both renders.
- No `public const`, `public annotation`, `listener` or `service` declarations exist in the default
  module, so nothing of those kinds is missing.
- Central metadata for `2.1.0` lists exactly one module (`sap.s4hana.api_sales_quotation_srv`),
  consistent with the above.

## 7. Compiler plugin

**None.** `find` for `*compiler*plugin*` over the cloned tag returns nothing, and the bala contains
no `compiler-plugin/` directory (`ls` on the bala root shows only `bala.json`,
`dependency-graph.json`, `docs`, `modules`, `package.json`). This is a generated OpenAPI/OData
connector with no plugin-contributed code actions, validations or annotations, so there is nothing
plugin-implied that the render could be missing.

## 8. Other considerations

- **Version stability**: both renders were produced from the same bala at `2.1.0`; `package.json`
  and `Ballerina.toml` both say `2.1.0`, `distribution/ballerina_version 2201.13.0`. Central reports
  `deprecated: null`. No version drift.
- **Size / tokens**: `new` is +56 lines but **+59,669 bytes (+37 %)** — the added union aliases are
  extremely long single lines (e.g. `SalesQuotationItemOfA_SalesQuotationItemPartnerSelectOptions`
  is ~1.7 kB on one line). This is real information (the exact `$select`/`$orderby`/`$expand` token
  sets an LLM needs to construct valid OData queries), but it materially inflates the context cost
  for this library and for the 9 sibling `sap.s4hana.*` modules.
- **Doc text**: `new` inherits the source's curly quotes (`“deep insert”` at new:2873-2874); UTF-8 is
  preserved correctly, no mojibake. No other non-ASCII in the file.
- **Escaped identifiers** (`Modified\ A_SalesQuotationItemType`, `\$expand`) are rendered with the
  same escaping as the source, so they remain valid Ballerina identifiers.
- The library is a generated SAP OData V2 connector; the 88 remote methods and 285 types are
  entirely machine-generated, which is why the `Unknown type` degradation in `old` hit so hard
  (36 % of all types) — this module family is among the biggest beneficiaries of spec v2.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 3176 / 3232 |
| `wc -c old new` | 161332 / 221001 |
| `grep -c '^// Unknown type:' old new` | 102 / 0 |
| `grep -n '^// --- ' old new` | 4 markers each, same order (7/114/116/2813 vs 7/114/116/2869) |
| `diff -u old new \| wc -l` | 1252 |
| `grep -c '^-[^-]' full.diff` / `'^+[^+]'` | 164 / 220 |
| `grep '^-[^-]' full.diff \| grep -v 'Unknown type'` | 62 lines, all `remote function` with `anydata Additional Values` |
| classification of `^+` lines | 53 `@constraint:`, 102 `type `, 65 other (62 remote fn + 2 `@display` + 1 doc) |
| `diff <(sed 's/anydata Additional Values, //' old-client) new-client` | empty → sole client delta |
| python set diff `old − new` over `^type <name>` | `[]` (0 declarations removed) |
| python set diff `src public types − new` | `[]` (0 missing) |
| 102 added decls vs `types.bal` | 93 byte-identical, 9 differ only by redundant-paren removal, 0 not in source |
| `diff <(grep '@constraint:' types.bal) <(grep '@constraint:' new)` | IDENTICAL (53 lines) |
| `grep -c '@constraint:' old / new / types.bal` | 0 / 53 / 53 |
| `grep -n '@display' types.bal / old / new` | 2 (173, 2444) / 0 / 2 (950, 1021) |
| `grep -c '^    remote function' old / new`; `remote isolated function` in `client.bal` | 88 / 88 / 88 |
| `grep -n 'function init' old / new` | old:2823, new:2879 — identical text; matches `client.bal:38` |
| `diff` README lines 7–114 old vs new | identical |
| 179 source records field-by-field vs old and vs new | 175 match both; 4 deviate identically on both sides |
| `ConnectionConfig` / `ClientHttp1Settings` / `OAuth2RefreshTokenGrantConfig` block old vs new | identical: True / True / True |
| `git ls-remote --tags … \| grep quotation` | `api_sales_quotation_srv-v2.1.0` → `4e9f5b58…` (peeled `6ca21620…`) |
| `git clone --depth 1 --branch api_sales_quotation_srv-v2.1.0` | ok; module at `ballerina/api_sales_quotation_srv` |
| `diff -q` GitHub vs bala for `client.bal`/`types.bal`/`utils.bal` | all IDENTICAL |
| `find src -iname '*compiler*plugin*'` | no results |
| `ls` bala root | `bala.json docs dependency-graph.json modules package.json` — no `compiler-plugin/` |
| `package.json` `export` / `modules` | exports default module only; `.mock` has `"export": false` |
| `grep -E '^(public )?(isolated )?function' utils.bal` | 6 functions, none `public` |
| `curl api.central.ballerina.io/…/2.1.0` | `deprecated: null`, 1 module, pullCount 22 |
| `grep 'Additional Values\|Unknown type\|undefined' new` | 0 hits |
| brace balance in `new` | 329 `{` / 329 `}` |
| `LC_ALL=C grep '[^ -~]' new` | 2 lines (curly quotes in doc text, from source) |

## 10. Caveats and unverified items

- The record field-by-field comparison in §3 used a regex parser over `types.bal`; for four records
  (`ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`, `OAuth2RefreshTokenGrantConfig`) the
  non-greedy block regex straddled record boundaries, so its per-field lists for those four are not
  trustworthy. Those four were therefore re-checked by hand against `types.bal:174-205`, `747-754`,
  `1206-1210`, `2438-2447` and by an exact old-vs-new block comparison; conclusions for them rest on
  the manual check, not the regex.
- I did not compile either render. Claims about "non-compiling" syntax in §5 are from reading the
  text against the Ballerina grammar, not from `bal build`.
- The `old`/`new` renders were taken as given from the library folder; I did not re-run the
  two-stage pipeline to reproduce them, so I cannot independently confirm which `ballerina-vscode`
  commit produced each file beyond what the brief states.
- The 9 single-member-union renderings (`"to_SalesQuotation"[]` vs `("to_SalesQuotation")[]`) are
  asserted to be semantically equivalent Ballerina; this is from the language spec's singleton-type
  rules, not from a compiler run.

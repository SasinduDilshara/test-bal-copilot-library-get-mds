# ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_sd_sa_soldtopartydetn-v2.1.0` (commit `dce5e4a`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn/2.1.0` |
| Old render | `250` lines |
| New render | `256` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small monorepo module (3 `.bal` files, 448 lines total in the bala). The whole public API is
12 public types + 1 public client class with 4 methods.

`new` is strictly better than `old` on every axis measured:

- The 3 `// Unknown type:` placeholders in `old` (`count`, `A_DelivSchedSoldToPartyDetnSelectOptions`,
  `A_DelivSchedSoldToPartyDetnOrderByOptions`) are replaced with real, verbatim-correct type
  definitions plus one doc comment. Render now covers 12/12 public types (old: 9/12).
- 4 annotations that `old` dropped entirely (3× `@constraint:String`, 1× `@display` on
  `ProxyConfig.password`, 1× `@display` on `ConnectionConfig`) now appear, with values byte-identical
  to the source.
- The malformed pseudo-parameter `anydata Additional Values` — which appeared inside two remote
  function signatures in `old` and is not valid Ballerina (identifier with a space) and does not
  exist in the library source — is gone in `new`.

Nothing was removed, truncated or degraded in `new`. JSON deep-comparison of all 12 typeDefs shows
only additive deltas (`baseType`, `annotations`); the only deletion anywhere in the pipeline output
is the bogus `Additional Values` parameter.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 250 | 256 |
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `^type ` declarations rendered | 9 | 12 |
| `client class` | 1 | 1 |
| `function init` | 1 | 1 |
| `remote function` | 3 | 3 |
| JSON `typeDefs` | 12 | 12 |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 |
| README bytes in JSON | 4560 | 4560 (byte-identical to bala `docs/README.md`) |

**Declarations added in `new` (3)** — all previously `// Unknown type:` stubs:

- `type count string;` (+ its doc comment, which `old` also dropped)
- `type A_DelivSchedSoldToPartyDetnSelectOptions (...)[];`
- `type A_DelivSchedSoldToPartyDetnOrderByOptions (...)[];`

**Declarations removed in `new`: 0.**

**Declarations modified (6 sites, all in Types + Client):**

| Location | Change |
|---|---|
| `A_DelivSchedSoldToPartyDetn.Supplier` | `+ @constraint:String {maxLength: 17}` |
| `A_DelivSchedSoldToPartyDetn.PartnerDescription` | `+ @constraint:String {maxLength: 30}` |
| `A_DelivSchedSoldToPartyDetn.UnloadingPointName` | `+ @constraint:String {maxLength: 25}` |
| `ProxyConfig.password` | `+ @display {label: "", kind: "password"}` |
| `ConnectionConfig` (type-level) | `+ @display {label: "Connection Config"}` |
| `getA_DelivSchedSoldToPartyDetn`, `listA_DelivSchedSoldToPartyDetns` | `- anydata Additional Values` parameter |

JSON-level deltas (deep compare, `typeDefs` name order identical on both sides):
`count.baseType`, `SelectOptions.baseType`, `OrderByOptions.baseType` added; `annotations` added on
4 record fields/types; client `parameters` lost the `('Additional Values', {'name':'anydata'})` entry
on the two query operations. No other key differs.

## 3. Correctness against library source

Bala is byte-identical to the upstream tag: `diff` of `client.bal`, `types.bal`, `utils.bal` between
`ballerina/api_sd_sa_soldtopartydetn/` at tag `api_sd_sa_soldtopartydetn-v2.1.0` and the bala
`modules/sap.s4hana.api_sd_sa_soldtopartydetn/` → all three IDENTICAL. So GitHub and bala agree; no
tie-break needed.

Every added/changed item in `new` verified verbatim against `.../modules/sap.s4hana.api_sd_sa_soldtopartydetn/types.bal`:

| Rendered in `new` | Source | Match |
|---|---|---|
| `type count string;` + `# The number of entities in the collection. Available when using the [$inlinecount](...pdf#page=67) query option.` | types.bal:45–46 | exact |
| `type A_DelivSchedSoldToPartyDetnSelectOptions ("Supplier"\|"PartnerDescription"\|"UnloadingPointName"\|"SoldToParty")[];` | types.bal:48 | exact |
| `type A_DelivSchedSoldToPartyDetnOrderByOptions ("Supplier"\|"Supplier desc"\|...\|"SoldToParty desc")[];` | types.bal:54 | exact |
| `@constraint:String {maxLength: 17}` on `Supplier` | types.bal:25 | exact |
| `@constraint:String {maxLength: 30}` on `PartnerDescription` | types.bal:28 | exact |
| `@constraint:String {maxLength: 25}` on `UnloadingPointName` | types.bal:30 | exact |
| `@display {label: "", kind: "password"}` on `ProxyConfig.password` | types.bal:76 | exact |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | types.bal:101 | exact |

The removed `anydata Additional Values` parameter: **no such parameter exists in the source**. Both
operations are declared with an included-record parameter only —
`client.bal:69` `remote isolated function getA_DelivSchedSoldToPartyDetn(string Supplier, string PartnerDescription, string UnloadingPointName, map<string|string[]> headers = {}, *GetA_DelivSchedSoldToPartyDetnQueries queries)` and
`client.bal:81` `remote isolated function listA_DelivSchedSoldToPartyDetns(map<string|string[]> headers = {}, *ListA_DelivSchedSoldToPartyDetnsQueries queries)`.
`GetA_DelivSchedSoldToPartyDetnQueries` (types.bal:62) and `ListA_DelivSchedSoldToPartyDetnsQueries`
(types.bal:85) are open records, so `Additional Values : anydata` was the docs-model rendering of the
implicit `anydata` rest field. Emitting it as a positional parameter was wrong; dropping it is correct.

Client shape verified: `public isolated client class Client` (client.bal:24), `init(ConnectionConfig config, string hostname, int port = 443) returns error?` (client.bal:32), 3 remote functions (client.bal:69, 81, 93). All 4 present in both renders with matching names, return types and the `port = 443` default.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Full `diff -u old new` on the rendered `.bal.txt`: 4 hunks, +11/−5 lines. Every `−` line is either a
  `// Unknown type:` stub replaced by a real definition, or the bogus `anydata Additional Values`
  parameter. No declaration, doc comment, parameter, default value, or return type present in `old`
  is absent from `new`.
- Programmatic deep-diff of both JSONs across all 12 `typeDefs` (type-level keys and every record
  field's every key): all deltas are `None → value` in the `new` direction. Zero `value → None`.
- Declaration-set counts (`^type`, `client class`, `function init`, `remote function`) equal or higher
  in `new`.
- README: identical byte length (4560) on both sides and byte-identical to the bala `docs/README.md`;
  section markers 4 vs 4, so no README/section content lost.
- No version-qualified type references on either side (0 vs 0), so nothing there to regress.

## 5. Issues in `new` (independent of `old`)

None of these are regressions — items 1–6 are present identically in `old` and are renderer-wide
behaviour; item 7 is new-only but cosmetic.

1. **Included-record parameter is rendered both flattened and as a named parameter.** Source has
   `*GetA_DelivSchedSoldToPartyDetnQueries queries`; the render emits
   `..., A_DelivSchedSoldToPartyDetnSelectOptions \$select = [], GetA_DelivSchedSoldToPartyDetnQueries queries`
   — the record's fields as loose parameters *and* the record itself. Same for
   `listA_DelivSchedSoldToPartyDetns` (6 flattened fields + the record). An LLM copying this will
   produce a call that does not compile; the `*` inclusion marker is nowhere in the render.
2. **Required parameter after defaulted parameters.** `queries` is emitted with no default after
   `headers = {}` / `\$select = []`, which is invalid Ballerina.
3. **`isolated` and `public` qualifiers dropped** everywhere (`public isolated client class Client` →
   `client class Client`; `remote isolated function` → `remote function`).
4. **Closed records rendered as open.** `ClientHttp1Settings` (types.bal:36), `ProxyConfig`
   (types.bal:68) and `ConnectionConfig` (types.bal:102) are `record {| ... |}` in source but render
   as `record { ... }`.
5. **Record field default values lost, converted to optional.** e.g. source `string host = "";`,
   `int port = 0;`, `decimal timeout = 60;`, `http:HttpVersion httpVersion = http:HTTP_2_0;`,
   `boolean validation = true;` all render as `... host?;`, `... timeout?;` etc. The concrete defaults
   are not recoverable from the render.
6. **Parameter-level doc comments dropped.** Source documents `+ Supplier - Supplier Number at
   Customer Location`, `+ headers - ...`, `+ return - Retrieved entity` (client.bal:60–66); the render
   keeps only the first doc line and leaves a dangling empty `# ` line under each function.
7. **`@constraint:String` is emitted without any module attribution.** The render's only import is
   `import ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn;`. Cross-package *type* references get a
   `// Special Agent Note: X FROM ballerina/http package` trailer, but the `constraint` annotation
   gets none, even though the JSON carries `"module": "ballerina/constraint"`. New-only, since `old`
   emitted no annotations at all.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

Default module (`modules/sap.s4hana.api_sd_sa_soldtopartydetn/`) public surface:

- 12 `public type` in `types.bal` → all 12 present in `new` (only 9 in `old`).
- 1 `public isolated client class Client` in `client.bal` → present, with all 4 methods.
- `utils.bal` declares no `public` symbols (grep for `^public` returns nothing) — its helpers
  (`getEncodedUri`, `getPathForQueryParam`, `Encoding`, …) are module-private and correctly absent.

Submodule note (shared gap, not applicable here): the bala has a second module
`sap.s4hana.api_sd_sa_soldtopartydetn.mock`, but `package.json` marks it
`{"name": "sap.s4hana.api_sd_sa_soldtopartydetn.mock", "export": false}` and `"export": ["sap.s4hana.api_sd_sa_soldtopartydetn"]`.
It is a non-exported HTTP mock service used by tests, so its absence from both renders is correct,
not a gap.

## 7. Compiler plugin

This package ships **no compiler plugin**. Evidence: the bala root contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no `compiler-plugin/`
and no `compiler-plugin.json`. `find -maxdepth 2 -iname "*compiler-plugin*"` over the cloned repo at
the tag returns nothing. Nothing plugin-implied is therefore missing from the render.

The package does depend on `ballerinax/sap` (`import ballerinax/sap;`, client.bal:21) for the
underlying `sap:Client`, but that is a plain library dependency; the render correctly does not expose
`sap:Client` since the field `final sap:Client clientEp` is private.

## 8. Other considerations

- **Version / stability.** 2.1.0, non-deprecated, built for distribution `2201.13.0`. Keywords mark
  it `Cost/Paid`. Both sides rendered the same pinned version; no drift observed.
- **Size / tokens.** 256 lines — one of the smallest renders in the set. The +6 net lines buy 3
  previously-missing type definitions that the client signatures *reference*
  (`A_DelivSchedSoldToPartyDetnSelectOptions` and `...OrderByOptions` are used as parameter types in
  both remote functions). In `old` those parameter types were dangling references to types the render
  never defined — a real comprehension hazard now fixed.
- **Doc quality.** README is complete (Overview, Setup guide, Quickstart with a compiling snippet,
  Examples) and carried verbatim into both renders.
- **Generated code.** `types.bal` / `client.bal` are OpenAPI-tool generated ("AUTO-GENERATED FILE. DO
  NOT MODIFY."); the sanitations live in `docs/sanitation/*.bal` in the repo and are not part of the
  published package.
- **Monorepo scoping honoured.** Only `ballerina/api_sd_sa_soldtopartydetn/` was reviewed; the other
  9 sibling modules in the repo were ignored.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 250 / 256 |
| 2 | `diff -u old/…bal.txt new/…bal.txt` | 4 hunks, +11 / −5 |
| 3 | `grep -c "^// Unknown type:"` both | old 3, new 0 |
| 4 | `grep -cE ':[0-9]+\.[0-9]+\.[0-9]+:'` both | old 0, new 0 |
| 5 | `grep -n '^// --- '` new | 4 markers (README, END README, Types, Client) |
| 6 | `grep -cE '^type '` both | old 9, new 12 |
| 7 | `grep -cE '^    remote function'` both | 3 and 3 |
| 8 | `git ls-remote --tags <repo> \| grep soldtoparty` | `api_sd_sa_soldtopartydetn-v2.1.0` exists (also v1.0.0, v2.0.0) |
| 9 | `git clone --depth 1 --branch api_sd_sa_soldtopartydetn-v2.1.0 …` + `git describe --tags` | `api_sd_sa_soldtopartydetn-v2.1.0`, commit `dce5e4a` |
| 10 | `diff` bala vs repo for `client.bal`, `types.bal`, `utils.bal` | all IDENTICAL |
| 11 | `grep -n "^public type\|@constraint\|@display\|record {\|"` types.bal | 12 public types; annotations at 25, 28, 30, 76, 101; closed records at 36, 68, 102 |
| 12 | `grep -n "^public" client.bal` | line 24 `public isolated client class Client` |
| 13 | `grep "^public" utils.bal` | no output → no public symbols |
| 14 | `ls` bala root | no `compiler-plugin/`; `find -maxdepth 2 -iname "*compiler-plugin*"` in repo → empty |
| 15 | `package.json` `export` / `modules` | exports default module only; `.mock` has `export: false` |
| 16 | Python deep-diff of both JSONs' `typeDefs` (all keys, all fields) | only additive: 3× `baseType`, 4× `annotations`; zero removals |
| 17 | Python compare of client `functions` params in both JSONs | identical except `('Additional Values', anydata)` removed from 2 functions in `new` |
| 18 | Python compare `readme` in JSON vs bala `docs/README.md` | equal on both sides, 4560 chars |
| 19 | JSON top-level `functions`/`services`/`annotations` | `[]` on both sides |
| 20 | `sed -n '18,98p' client.bal` | confirms `*GetA_…Queries queries` / `*ListA_…Queries queries`, `port = 443`, param docs present in source |
| 21 | Read `OLD_AND_NEW_DIFFS/sap.s4hana.api_sd_sa_soldtopartydetn_diff.md` | its counts (250/256, +11/−5, 4 hunks, 3→0 unknown, 3 decls added) all independently reproduced above |

## 10. Caveats and unverified items

- Neither render was compiled. Claims of non-compiling syntax in §5 (items 1, 2) are from reading the
  emitted text against the Ballerina grammar, not from a `bal build` run. They apply equally to `old`,
  so they do not affect the regression verdict.
- Ballerina Central metadata for `ballerinax/sap.s4hana.api_sd_sa_soldtopartydetn/2.1.0` was not
  re-queried over the network; module list, export flags and keywords were taken from the bala's
  `package.json` and `Ballerina.toml`, which are authoritative for what the extractor consumed.
- The two `ballerina-vscode` source trees (`old` @ `eb5d81b3`, `new` @ `412ba01e`) were not inspected;
  the attribution of each delta to spec v2 behaviour is inferred from the brief plus the observed
  output, not from reading the extractor/renderer diff.

# ballerinax/sap.s4hana.api_sales_order_simulation_srv 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.api_sales_order_simulation_srv` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `api_sales_order_simulation_srv-v2.1.0` (monorepo, module dir `ballerina/api_sales_order_simulation_srv`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.api_sales_order_simulation_srv/2.1.0` |
| Old render | `1062` lines |
| New render | `1102` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library, plus one deletion that is itself a fix.
All three `// Unknown type:` placeholders in `old` become real, byte-exact type definitions in
`new`. 39 annotations that `old` dropped entirely (37 `@constraint:String`, 2 `@display`) are
emitted by `new` and every one matches the bala source exactly, annotation-and-field paired. Two
client remote-function signatures lose a synthetic, non-compiling `anydata Additional Values`
pseudo-parameter that does not exist in the library source — a correctness gain.

A recursive JSON subset check over the whole model found **zero** dropped keys, dropped list
elements or changed values anywhere except those two synthetic parameters. No declaration was
removed. The rendered type set (47) is an exact set-equality match with the 47 public types the
bala's default module exports. Coverage gaps: none.

## 2. Change inventory

Line counts: `old` 1062, `new` 1102 (net +40). Unified diff: 22 hunks, 45 added lines, 5 removed lines.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations rendered | 44 | 47 | +3 |
| `// Unknown type:` placeholders | 3 | 0 | −3 |
| `@constraint:String` lines | 0 | 37 | +37 |
| `@display` lines | 0 | 2 | +2 |
| `client class` | 1 | 1 | 0 |
| `remote function` in client | 7 | 7 | 0 |
| `function init` | 1 | 1 | 0 |
| Section markers (`// --- `) | 4 | 4 | 0 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 | 0 |
| `// Special Agent Note:` cross-package hints | 18 | 18 | 0 |
| Non-ASCII bytes | 0 | 0 | 0 |
| README block (render lines 8–113) | identical | identical | 0 |

Declarations **added** in `new` (3), all previously degraded placeholders:

- `type A_SlsOrdSimlnValAddedSrvcOrderByOptions (...)[]` (union array, 17 members × 2 sort directions)
- `type A_SlsOrdSimlnValAddedSrvcSelectOptions (...)[]` (union array, 18 members)
- `type count string;` — plus its doc comment, which `old` also dropped

Declarations **removed**: none.

Declarations **modified** (2), both in the `// --- Client ---` section:

- `getA_SlsOrdSimlnValAddedSrvc` — parameter `anydata Additional Values` removed (8 → 7 params)
- `listA_SlsOrdSimlnValAddedSrvcs` — parameter `anydata Additional Values` removed (9 → 8 params)

JSON-model delta (recursive diff of `old/*.json` vs `new/*.json`): 44 additions
(`annotations` ×39, `baseType` ×3, `type.links` ×2) and 8 "loss" entries, all 8 of which are the
two removed synthetic params and the resulting index shift. Top-level counts identical on both
sides: `typeDefs` 47/47, `clients` 1/1, `functions` 0/0, `services` 0/0, `annotations` 0/0;
`readme` byte-identical (4530 chars); `name`/`description` identical.

## 3. Correctness against library source

GitHub at tag `api_sales_order_simulation_srv-v2.1.0` and the bala agree byte-for-byte
(`client.bal`, `types.bal`, `utils.bal` all `diff`-identical; module `README.md` identical to
`docs/README.md` in the bala). So there is no GitHub-vs-bala conflict to resolve.

- **All 37 `@constraint:String` annotations verified.** Extracted every `(annotation, next-line
  field)` pair from `types.bal` and from the `new` render, sorted, and diffed: 37 vs 37,
  `IDENTICAL`. e.g. `types.bal:98-99` `@constraint:String {maxLength: 2}` / `string
  PartnerFunction;` appears verbatim in `new` inside `CreateA_SalesOrderItemPartnerSimln`.
- **`A_SlsOrdSimlnValAddedSrvcOrderByOptions`** — `new` line matches `types.bal:31` exactly after
  stripping `public` (string compare: EXACT MATCH).
- **`A_SlsOrdSimlnValAddedSrvcSelectOptions`** — matches `types.bal:920` exactly (EXACT MATCH).
- **`count`** — `types.bal:471-472` carries the doc `# The number of entities in the collection…`
  and `public type count string;`; `new` lines 962-963 reproduce both. `old` had neither.
- **`@display {label: "Connection Config"}`** — `types.bal:326`, on `ConnectionConfig`; `new:967`.
- **`@display {label: "", kind: "password"}`** — `types.bal:508`, on `ProxyConfig.password`;
  `new:1022`.
- **Client** — `client.bal:24` `public isolated client class Client` with `init` + 7 remote
  functions (`createA_SalesOrderSimulation`, `createA_SlsOrdSimlnValAddedSrvc`,
  `deleteA_SlsOrdSimlnValAddedSrvc`, `getA_SlsOrdSimlnValAddedSrvc`,
  `listA_SlsOrdSimlnValAddedSrvcs`, `patchA_SlsOrdSimlnValAddedSrvc`, `performBatchOperation`).
  Both renders emit all 8.
- **`Additional Values` is not real.** `client.bal:113` declares
  `…, map<string|string[]> headers = {}, *GetA_SlsOrdSimlnValAddedSrvcQueries queries)` and
  `client.bal:126` `…, *ListA_SlsOrdSimlnValAddedSrvcsQueries queries)`. There is no `Additional
  Values` parameter. It is the Ballerina doc model's synthetic entry for the open-record rest
  descriptor (JSON: `{"name":"Additional Values","description":"Capture key value pairs",
  "type":{"name":"anydata"}}`). Dropping it makes `new` closer to the source.
- **Type set equality.** 47 `^public type` names in the bala default module vs 47 `^type` names in
  `new`: `comm -23` and `comm -13` both empty.
- **Record field sets.** Parsed all 43 `record {` types from bala and from `new`; field-name
  sequences match for 39 of them. The 4 that my parser flagged (`ConnectionConfig`, `ProxyConfig`,
  `ClientHttp1Settings`, `OAuth2RefreshTokenGrantConfig`) flag identically against `old` too — the
  parser cannot handle defaulted fields (`decimal timeout = 60;`) and record inclusion; the
  underlying JSON subset check proves no field was lost on either side.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Recursive subset check `old JSON ⊆ new JSON`: the only 8 divergences are the two synthetic
  `Additional Values` parameters and the index shift they cause. No doc string, default value,
  parameter, return type, field, or link was dropped.
- `comm` on sorted declaration-name sets: nothing in `old` is absent from `new`.
- README block: `old` lines 8–113 == `new` lines 8–113, and both == the bala `docs/README.md`
  (single trailing-blank-line difference from the raw file).
- `// Special Agent Note:` cross-package hints: 18 in both.
- Section markers: 4 in both, same order.
- Remote-function count and names: identical.
- The only removals in the unified diff are the 3 `// Unknown type:` lines (replaced by real
  definitions) and the 2 client signature lines (replaced by more accurate ones).

## 5. Issues in `new` (independent of `old`)

All of the following are present in `old` as well — none is introduced by spec v2 — but they are
inaccuracies a reviewer of `new` should know about:

1. **Included-record parameters are flattened *and* kept.** `new:1089` renders
   `getA_SlsOrdSimlnValAddedSrvc(…, map<string|string[]> headers = {},
   A_SlsOrdSimlnValAddedSrvcSelectOptions \$select = [], GetA_SlsOrdSimlnValAddedSrvcQueries
   queries)`. The real signature (`client.bal:113`) has `*GetA_SlsOrdSimlnValAddedSrvcQueries
   queries` only. The render both expands the record's fields as positional params and keeps a
   `queries` param, so `$select` is duplicated; and it places a non-defaulted `queries` after
   defaulted params, which is not valid Ballerina. Same for `listA_SlsOrdSimlnValAddedSrvcs`
   (`new:1092`). An LLM copying either signature would produce non-compiling code.
2. **Field default values are dropped and required fields become optional.** `ConnectionConfig`
   in `types.bal:326-357` has `http:HttpVersion httpVersion = http:HTTP_2_0;`, `decimal timeout =
   60;`, `string forwarded = "disable";`, `http:Compression compression = http:COMPRESSION_AUTO;`,
   `boolean validation = true;`. `new:965-999` renders all five as `?`-optional with no default.
   `ProxyConfig` (`types.bal:500-510`, all four fields defaulted) is rendered the same way.
3. **Closed records are rendered as open.** `ConnectionConfig` and `ProxyConfig` are
   `record {| … |}` in source; both renders emit `record { … }`.
4. **`public` / `isolated` qualifiers stripped.** `public isolated client class Client` renders as
   `client class Client`; `public isolated function init` as `function init`; all 47 `public type`
   as `type`.
5. **Annotations are emitted without their imports.** `new` now contains `@constraint:String` and
   `@display` but the render's import block (`new:5`, `new:59`) still lists only the library
   itself; `types.bal:20` imports `ballerina/constraint`. Low severity for a synopsis format, but
   the annotation text is not self-contained.
6. **Per-parameter doc lines are not rendered** on either side — every function doc is reduced to
   the summary line plus a bare `# `. The `# + ValueAddedServiceType - VAS Service Types` style
   docs in `client.bal` are lost in both.

## 6. Coverage gaps vs. the library

**Zero gaps.** The default module `sap.s4hana.api_sales_order_simulation_srv` exports 47 public
types and one public client class; all 48 appear in `new` (and 45 of 48 in `old`, the other 3
being the placeholder-degraded types).

Non-public module-level symbols correctly absent from both renders: `enum EncodingStyle`
(`utils.bal:36`) and the 7 non-public `isolated function`s in `utils.bal` (lines 47, 73, 110, 150,
174, 188). These are not part of the public API.

Submodule note: the bala contains a second module,
`sap.s4hana.api_sales_order_simulation_srv.mock`, but `package.json` marks it `"export": false`
and Ballerina Central lists exactly one module for this version. There is therefore **no**
submodule-only public API and no shared `getDefaultModule()` gap for this library.

## 7. Compiler plugin

This package ships **no compiler plugin**. `find` for `*compiler-plugin*` across the cloned
monorepo returned nothing, and the bala has no `compiler-plugin/` directory (contents:
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived
is expected in the render, and nothing is missing.

The only annotation-bearing dependency is `ballerina/constraint`, whose `@constraint:String`
annotations are runtime validation constraints — these are exactly what `new` now surfaces and
`old` silently discarded. For an LLM writing payloads, the `maxLength` bounds are materially
useful (e.g. `SalesOrder` max 10 chars, `SalesOrderItem` max 6).

## 8. Other considerations

- Version 2.1.0 is stable, `graalvmCompatible: true`, built for `ballerina_version 2201.13.0`.
  Central reports it as not deprecated (`deprecateMessage` empty), pullCount 22.
- Size impact is modest: +40 lines (+3.8%) for a large accuracy gain. The two union-array types
  are single very long lines (~1.5 KB and ~1.0 KB), which raises the token cost of those lines but
  is faithful to the source.
- The library is fully OpenAPI-generated (`// AUTO-GENERATED FILE` header in `client.bal`);
  identifiers like `Modified\ A_SlsOrdSimlnValAddedSrvcType` and `\$select` are genuine quoted
  identifiers in the source, not render corruption — both renders escape them the same way.
- `type count string;` uses `count` as a type name; that is what the library publishes.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 1062, new 1102 |
| `grep -c '^// Unknown type:'` old / new | 3 / 0 |
| `grep -n '^// Unknown type:'` old | lines 816, 856, 929 |
| `grep -n '^// --- '` old / new | 4 markers each (README 7, END README 114, Types 116, Client 1029/1069) |
| `diff -u old new` | 22 hunks, 45 added, 5 removed |
| `grep -c '^+ *@constraint'` / `'^+ *@display'` on diff | 37 / 2 |
| `grep -c '@constraint:String'` bala types.bal / new / old | 37 / 37 / 0 |
| awk-extracted (annotation, field) pairs, bala vs new, sorted diff | 37 vs 37, IDENTICAL |
| `grep -n '@display'` new / old | new 967, 1022 / old none |
| String compare `A_SlsOrdSimlnValAddedSrvcOrderByOptions` bala `types.bal:31` vs new | EXACT MATCH |
| String compare `A_SlsOrdSimlnValAddedSrvcSelectOptions` bala `types.bal:920` vs new | EXACT MATCH |
| `sed -n '460,475p' types.bal` vs `new:962-963` for `count` | doc + `type count string;` both present in new |
| `grep -oE '^public type'` bala (47) vs `^type` new (47), `comm -23` / `comm -13` | both empty — exact set equality |
| `grep -cE '^type '` + unknown, old | 44 + 3 = 47 |
| `grep -c '    remote function'` old / new | 7 / 7 |
| `grep -c 'Special Agent Note'` old / new | 18 / 18 |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 0 / 0 |
| `grep -cP '[^\x00-\x7F]'` old / new | 0 / 0 |
| Recursive JSON subset check old→new | 8 "losses", all the 2 synthetic `Additional Values` params; 44 additions (39 `annotations`, 3 `baseType`, 2 `links`) |
| JSON top-level counts | typeDefs 47/47, clients 1/1, functions 0/0, services 0/0, annotations 0/0, readme identical (4530 chars) |
| `git ls-remote --tags … \| grep simulation` | `api_sales_order_simulation_srv-v2.1.0` → `4689334131d2…` |
| `git clone --depth 1 --branch api_sales_order_simulation_srv-v2.1.0` | success; module at `ballerina/api_sales_order_simulation_srv` |
| `diff` repo vs bala: `client.bal`, `types.bal`, `utils.bal` | all IDENTICAL |
| `diff` repo module `README.md` vs bala `docs/README.md` | identical |
| `diff <(sed -n '8,113p' new) bala/docs/README.md` | only a trailing blank line |
| `diff <(sed -n '8,113p' old) <(sed -n '8,113p' new)` | identical |
| `client.bal:113` / `client.bal:126` | `*GetA_SlsOrdSimlnValAddedSrvcQueries queries` / `*ListA_SlsOrdSimlnValAddedSrvcsQueries queries` — no `Additional Values` param |
| `types.bal:326-357` `ConnectionConfig` | `record {| … |}` with 5 defaulted fields; render shows open record, all optional, no defaults (both sides) |
| `find src -iname '*compiler-plugin*'` | no results |
| `ls bala/any/` | no `compiler-plugin/` directory |
| `bala/any/package.json` | `export: ["sap.s4hana.api_sales_order_simulation_srv"]`; `.mock` module `export: false` |
| Central API `…/ballerinax/sap.s4hana.api_sales_order_simulation_srv/2.1.0` | 1 module, ballerinaVersion 2201.13.0, not deprecated, pullCount 22 |
| `grep -nE '^public \|^…function\|class\|enum…'` on `utils.bal` | `enum EncodingStyle` + 7 functions, all non-public |

## 10. Caveats and unverified items

- I did not compile either render; "non-compiling Ballerina" claims in §5 items 1–3 are read from
  the language rules (required param after defaulted params; open vs closed record), not from a
  compiler run.
- My record field-set parser could not handle defaulted fields or record inclusion, so 4 of 43
  record types were not field-compared textually. They were covered by the JSON subset check
  instead, and they flag identically for `old` and `new`, so the comparison between the two sides
  is unaffected.
- I reviewed only `ballerina/api_sales_order_simulation_srv` in the monorepo, as instructed.
- I did not independently re-run the render pipeline; I audited the supplied artifacts against the
  bala and upstream source.

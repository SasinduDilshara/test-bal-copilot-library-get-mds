# ballerinax/sap.s4hana.salesarea_0001 2.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.s4hana.salesarea_0001` |
| Pinned version | `2.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.s4hana.sales |
| Tag reviewed | `salesarea_0001-v2.1.0` (commit `54f51a95`, module subdir `ballerina/salesarea_0001`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.s4hana.salesarea_0001/2.1.0` |
| Old render | `238` lines |
| New render | `243` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, fully auditable connector: one client class, three remote methods, ten public types, 437
lines of published source. I verified the upstream tag source is **byte-identical** to the bala
(`diff` on all three `.bal` files returned no output), so GitHub and the bala agree completely and
every claim below is checked against the exact source the extractor consumed.

The `old` → `new` diff is five hunks, +9/−4 lines, entirely in the Types and Client sections. Every
change is a strict improvement:

- Two `// Unknown type:` placeholders replaced with the correct real type definitions
  (`SalesAreaSelectOptions`, `SalesAreaOrderByOptions`) — both exactly matching source.
- Five annotations newly surfaced (`@display` ×2, `@constraint:String` ×3) — all matching source.
- A malformed, non-compiling parameter (`anydata Additional Values`, an identifier containing a
  space) removed from two client method signatures.

No declaration was removed, no signature narrowed, no doc lost. **Zero regressions.** Coverage of the
default module is complete: all 10 public types plus the `Client` class appear in both renders.

Both renders still share a set of pre-existing renderer inaccuracies (included-record parameters
mis-expanded, record field defaults dropped, closed records shown as open). These are documented in
§5 because they mislead an LLM consuming the render, but they are identical on both sides and are
not attributable to spec v2.

## 2. Change inventory

Line counts (`wc -l`): old **238**, new **243**. Diff: **5 hunks, 9 lines added, 4 removed**.

| Kind | old | new | Δ |
|---|---|---|---|
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | **2** | **0** | −2 |
| `type` declarations | 8 | **10** | +2 |
| `client class` | 1 | 1 | 0 |
| `remote function` | 3 | 3 | 0 |
| `function init` | 1 | 1 | 0 |
| Annotation lines (`^\s*@`) | **0** | **5** | +5 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 | 0 |
| `import` lines | 2 | 2 | 0 |
| README section bytes | identical | identical | 0 |

### Declarations added (2) — both were degraded placeholders in `old`

| Symbol | old | new |
|---|---|---|
| `SalesAreaSelectOptions` | `// Unknown type: SalesAreaSelectOptions` | `type SalesAreaSelectOptions ("SalesOrganization"\|"DistributionChannel"\|"Division")[];` |
| `SalesAreaOrderByOptions` | `// Unknown type: SalesAreaOrderByOptions` | `type SalesAreaOrderByOptions ("SalesOrganization"\|"SalesOrganization desc"\|"DistributionChannel"\|"DistributionChannel desc"\|"Division"\|"Division desc")[];` |

### Declarations removed (0)

None.

### Declarations modified (6)

| Location | Change |
|---|---|
| `ProxyConfig.password` (new:148) | `+ @display {label: "", kind: "password"}` |
| `SalesArea.SalesOrganization` (new:176) | `+ @constraint:String {maxLength: 4}` |
| `SalesArea.DistributionChannel` (new:178) | `+ @constraint:String {maxLength: 2}` |
| `SalesArea.Division` (new:180) | `+ @constraint:String {maxLength: 2}` |
| `ConnectionConfig` (new:192) | `+ @display {label: "Connection Config"}` |
| `Client.getSalesArea`, `Client.listSalesAreas` (new:234, 238) | `− anydata Additional Values` parameter |

### JSON-level cause

`diff` of the two pretty-printed JSONs shows exactly four classes of change, confirming the render
diff is fully explained upstream in the extractor:

1. `"type": "Other"` entries gain a `"baseType"` string (the two options types) — this is what lets
   `renderTypeDef` emit a real definition instead of the `// Unknown type:` fallback.
2. New `"annotations"` arrays on record fields and on `ConnectionConfig` (5 total, one carrying
   `"module": "ballerina/constraint"`).
3. Removal of the synthetic `{"name": "Additional Values", "description": "Capture key value pairs",
   "type": {"name": "anydata"}, "optional": true}` parameter from both query-bearing methods.

`typeDefs` count is **10 in both** JSONs — `old` already carried the two options types, it simply
could not render them.

## 3. Correctness against library source

Upstream tag source == bala source, verified byte-for-byte:

```
diff .../src/ballerina/salesarea_0001/{client,types,utils}.bal
     .../bala/.../modules/sap.s4hana.salesarea_0001/{client,types,utils}.bal
  → IDENTICAL (all three)
```

Every symbol `new` adds or changes, checked against `types.bal` / `client.bal` (paths relative to
the module dir; line numbers identical in bala and upstream tag):

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `type SalesAreaSelectOptions ("SalesOrganization"\|"DistributionChannel"\|"Division")[];` | `types.bal:29` `public type SalesAreaSelectOptions ("SalesOrganization"\|"DistributionChannel"\|"Division")[];` | **Exact match** (minus `public`) |
| `type SalesAreaOrderByOptions (...6 members...)[];` | `types.bal:57` | **Exact match**, all 6 members and their order preserved |
| `@display {label: "", kind: "password"}` on `password` | `types.bal:85–86` | **Exact match**, incl. the empty `label` |
| `@constraint:String {maxLength: 4}` on `SalesOrganization` | `types.bal:63–64` | **Exact match** |
| `@constraint:String {maxLength: 2}` on `DistributionChannel` | `types.bal:65–66` | **Exact match** |
| `@constraint:String {maxLength: 2}` on `Division` | `types.bal:67–68` | **Exact match** |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | `types.bal:90–91` | **Exact match** |
| Removal of `anydata Additional Values` | No such parameter exists in `client.bal:69` or `:81`. Source uses included-record params `*GetSalesAreaQueries queries` / `*ListSalesAreasQueries queries`. | **Removal is correct**; the parameter was extractor-synthesised from the open records' implicit `anydata` rest field and its name is not a legal Ballerina identifier |

Client surface, checked exhaustively against `client.bal`:

| Render (new) | Source | Note |
|---|---|---|
| `function init(ConnectionConfig config, string hostname, int port = 443) returns error?` | `client.bal:32` | Param names, types, and the `443` default all correct |
| `getSalesArea(string SalesOrganization, string DistributionChannel, string Division, map<string\|string[]> headers = {}, …) returns SalesArea\|error` | `client.bal:69` | Positional params, types, and return type correct |
| `listSalesAreas(map<string\|string[]> headers = {}, …) returns CollectionOfSalesArea\|error` | `client.bal:81` | Correct |
| `performBatchOperation(http:Request request, map<string\|string[]> headers = {}) returns http:Response\|error` | `client.bal:93` | Correct, unchanged between sides |

README: the render's README block (new:8–113) is a verbatim copy of the Central `readme` field and
`docs/README.md`; identical in both renders (no diff hunks in lines 1–121).

## 4. Regressions

**None found.**

What I checked to reach that conclusion:

- Full unified diff of the two renders — all 5 hunks reviewed individually (§2). No hunk removes a
  declaration, parameter, doc line, default value, or return type that was correct in `old`.
- Declaration-set comparison: `grep -E '^type '` yields 8 names in `old`, all 8 present in `new`
  plus 2 more. `grep -E '^\s+remote function '` yields 3 in both, same names.
- Section markers: 4 in both (`README`, `END README`, `Types`, `Client`) — no lost sections.
- README byte range unchanged (no diff hunk before line 122).
- `// Special Agent Note:` cross-package annotations: present and unchanged on all 13 `http:` field
  references and on `performBatchOperation`.
- The only *removal* in the whole diff is `anydata Additional Values`. It is not a regression: it
  does not exist in the library source, its name contains a space (invalid identifier, non-compiling
  render), and it appeared between defaultable and non-defaultable parameters. Removing it makes the
  signature strictly closer to the truth. Its one nugget of real information — that
  `GetSalesAreaQueries` / `ListSalesAreasQueries` are open records accepting extra query keys — is
  now unexpressed; that is a marginal information loss, noted in §8, not a correctness regression.

## 5. Issues in `new` (independent of `old`)

All six are also present in `old` (verified: none appears in any diff hunk), so none is caused by
spec v2 — but each would mislead an LLM consuming the render.

1. **Included-record parameters are mis-rendered, producing a non-compiling signature.** Source:
   `client.bal:69` `…, *GetSalesAreaQueries queries)`. Render (new:234) expands the record's fields
   as loose params *and* keeps a `GetSalesAreaQueries queries` param:
   `…, map<string|string[]> headers = {}, SalesAreaSelectOptions \$select = [], GetSalesAreaQueries queries)`.
   Two defects: (a) the record's fields and the record itself are both listed, which is a duplicate
   surface; (b) `queries` carries neither `?` nor a default despite being `"optional": true` in the
   JSON, so a required parameter follows defaultable ones — that does not compile in Ballerina. Same
   for `listSalesAreas` (new:238). An LLM copying either call site will emit broken code.
2. **Defaults are synthesised that do not exist in source.** `\$select = []`, `\$skip = 0`,
   `\$top = 0`, `\$filter = ""`, `\$count = false` (new:234, 238). In `types.bal:26,44,46,48,52,54`
   these are all *optional fields with no default* (`int \$skip?;` etc.). The JSON carries no
   `defaultValue` for them — the renderer invents a type-shaped placeholder. Sending `$top=0` or
   `$select=[]` to the OData service is not the same as omitting them.
3. **Record field defaults are dropped and the fields are re-labelled optional.** 11 fields lose
   real defaults: `ProxyConfig.host = ""`, `.port = 0`, `.userName = ""`, `.password = ""`
   (`types.bal:79–86`); `ClientHttp1Settings.keepAlive = http:KEEPALIVE_AUTO`,
   `.chunking = http:CHUNKING_AUTO` (`types.bal:34–36`); `ConnectionConfig.httpVersion =
   http:HTTP_2_0`, `.timeout = 60`, `.forwarded = "disable"`, `.compression = http:COMPRESSION_AUTO`,
   `.validation = true` (`types.bal:95–121`). All render as bare `field?` — e.g. new:203
   `decimal timeout?` for source `decimal timeout = 60;`.
4. **Closed records render as open.** `ClientHttp1Settings`, `ProxyConfig`, `ConnectionConfig` are
   `record {| … |}` at `types.bal:32, 77, 91`; all three render as `record { … }` (new:129, 140,
   193). This inverts the type's rest-field semantics.
5. **`@constraint:String` uses a prefix the render never imports.** The render's only import is
   `import ballerinax/sap.s4hana.salesarea_0001;` (new:5). `ballerina/constraint` is named in the
   JSON annotation's `"module"` field but no import line is emitted, so the annotation as printed
   would not resolve. (Cosmetic for comprehension, real if the snippet is copied.)
6. **Client method parameter docs are dropped.** Source `client.bal:63–68` documents
   `+ SalesOrganization - Sales Organization`, `+ DistributionChannel - …`, `+ headers - …`,
   `+ queries - …`, `+ return - Retrieved entity`. The render keeps only the summary line followed by
   an empty `# ` (new:232–233). Likewise `init` (source doc at `client.bal:27–31`) renders with no
   doc at all (new:230). Note the *type* docs are preserved fine — only function-level param/return
   docs are lost.

Also observed, non-defects: `public` and `isolated` modifiers are uniformly stripped (a deliberate
render convention, applied consistently); `count \@odata\.count?` (new:186) correctly reproduces the
escaped field name from `types.bal:72`.

## 6. Coverage gaps vs. the library

**Zero gaps.** The default module exports 12 public symbols
(`grep -nE '^\s*public ' modules/sap.s4hana.salesarea_0001/*.bal`); `init` is a member of `Client`,
so 11 top-level symbols. All 11 appear in both renders:

| Public symbol | Source | In old | In new |
|---|---|---|---|
| `Client` (client class) | `client.bal:24` | yes (229) | yes (229) |
| `GetSalesAreaQueries` | `types.bal:24` | yes | yes (120) |
| `SalesAreaSelectOptions` | `types.bal:29` | placeholder only | yes (125) |
| `ClientHttp1Settings` | `types.bal:32` | yes | yes (129) |
| `ListSalesAreasQueries` | `types.bal:42` | yes | yes (154) |
| `SalesAreaOrderByOptions` | `types.bal:57` | placeholder only | yes (169) |
| `count` | `types.bal:60` | yes | yes (172) |
| `SalesArea` | `types.bal:62` | yes | yes (175) |
| `CollectionOfSalesArea` | `types.bal:71` | yes | yes (185) |
| `ProxyConfig` | `types.bal:77` | yes | yes (140) |
| `ConnectionConfig` | `types.bal:91` | yes | yes (193) |

**Submodule situation — no shared gap here.** The bala has two modules
(`sap.s4hana.salesarea_0001`, `sap.s4hana.salesarea_0001.mock`), but `package.json` declares
`"export": ["sap.s4hana.salesarea_0001"]` and marks the mock module `"export": false`. Central
metadata likewise lists exactly one module. So the default module *is* the entire public API, and
the `getDefaultModule()`-only extraction loses nothing for this library.

`utils.bal` contains no `public` declarations (`SimpleBasicType`, `Encoding`, `EncodingStyle`,
`defaultEncoding` and 6 helper functions are all module-private) — correctly absent from both renders.

## 7. Compiler plugin

**This package ships no compiler plugin.** Searches for `*compiler-plugin*` and `CompilerPlugin.toml`
returned nothing in either the bala or the upstream tag checkout. `Ballerina.toml` declares only
`[package]` and `[build-options] observabilityIncluded = true` — no `[[tool]]`, no plugin
dependency. Nothing plugin-implied is therefore missing from the render.

The only annotation-processing dependency is `ballerina/constraint` 1.7.0 (per
`dependency-graph.json`), whose `@constraint:String` validations `new` now surfaces — an
improvement, since maxLength 4/2/2 on the `SalesArea` key fields is real, enforced runtime behaviour
that an LLM previously could not see.

## 8. Other considerations

- **Not deprecated.** Central: `"isDeprecated": false`, `"deprecateMessage": ""`. Stable major
  version 2.1.0. `graalvmCompatible: Yes`. Pull count 21 (low-traffic connector).
- **Version pinning confirmed on both sides.** Bala dir, `package.json`, upstream `Ballerina.toml`,
  and Central all agree on `2.1.0`. No version drift; the render diff is purely extractor/renderer.
- **Marginal information loss from the `Additional Values` removal.** `GetSalesAreaQueries` and
  `ListSalesAreasQueries` are open records (`record {` not `record {|`), so callers may pass
  additional OData query keys. `old` expressed that — badly, via an invalid `anydata Additional
  Values` parameter; `new` does not express it at all. Net still positive (invalid syntax removed),
  but the openness is now invisible. Would be better solved by rendering `record { … anydata…; }`.
- **Size/token impact is negligible**: +5 lines, +631 JSON bytes (27,870 → 28,501), +301 render
  bytes (10,912 → 11,213). Renders are tiny; no context-budget concern.
- **The render is not compilable Ballerina** on either side, chiefly due to §5 items 1 and 5. It
  reads as an API digest rather than a compilable stub. Worth knowing if downstream tooling ever
  tries to typecheck these.
- **Precomputed diff verified accurate.** `OLD_AND_NEW_DIFFS/sap.s4hana.salesarea_0001_diff.md`
  claims 238/243 lines, +9/−4, 5 hunks, 2→0 unknown types, 2 declarations added, 0 removed. I
  reproduced every one of those figures independently; all correct.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 238 / 243 |
| 2 | `ls -la old new` (byte sizes) | old 10,912 / 27,870; new 11,213 / 28,501 |
| 3 | `diff -u old/*.bal.txt new/*.bal.txt` | 5 hunks, +9/−4; full text reviewed (§2) |
| 4 | `grep -c '^// Unknown type:'` | old **2**, new **0** |
| 5 | `grep -cE '^type '` | old **8**, new **10** |
| 6 | `grep -cE '^\s+remote function '` | old **3**, new **3** |
| 7 | `grep -cE '^\s*@'` | old **0**, new **5** |
| 8 | `grep -n '^// --- '` on new | 4 markers: README (7), END README (114), Types (116), Client (226) |
| 9 | `grep -n '^import'` both | 2 each, identical (lines 5, 59 — line 59 is inside the README block) |
| 10 | `grep -nE '^type '` on new | 10 names enumerated in §6 table |
| 11 | `grep -nE '^\s*@'` on new | new:148, 176, 178, 180, 192 — the 5 annotations |
| 12 | `ls -R <bala>` | modules: `sap.s4hana.salesarea_0001` (client/types/utils.bal), `…​.mock` |
| 13 | `cat <bala>/package.json` | `"export": ["sap.s4hana.salesarea_0001"]`; mock `"export": false`; version 2.1.0 |
| 14 | `cat <bala>/modules/sap.s4hana.salesarea_0001/client.bal` (98 lines) | init:32, getSalesArea:69, listSalesAreas:81, performBatchOperation:93 |
| 15 | `cat <bala>/modules/sap.s4hana.salesarea_0001/types.bal` (122 lines) | 10 public types; annotations at 63,65,67,85,90 |
| 16 | `grep -nE '^\s*public ' <bala>/modules/.../*.bal` | 12 hits (11 top-level + `init`) |
| 17 | `grep -nE '^(public )?(type\|const\|enum\|class\|function\|isolated function\|final)' utils.bal` | 10 hits, **none** `public` |
| 18 | `find <bala> -name '*compiler-plugin*'` | no matches |
| 19 | `python3` dump of `dependency-graph.json` | deps: http 2.16.3, constraint 1.7.0, sap 1.3.1, log, url, os, observe |
| 20 | `git ls-remote --tags <repo> \| grep salesarea_0001` | tags v1.0.0, v2.0.0, **v2.1.0** → `54f51a95` |
| 21 | `git clone --depth 1 --branch salesarea_0001-v2.1.0` | OK; monorepo, module at `ballerina/salesarea_0001` |
| 22 | `cat src/ballerina/salesarea_0001/Ballerina.toml` | org ballerinax, name sap.s4hana.salesarea_0001, **version 2.1.0**, dist 2201.13.0 |
| 23 | `diff src/.../{client,types,utils}.bal <bala>/modules/.../{…}` | **all three IDENTICAL** |
| 24 | `find src -iname '*compiler-plugin*' -o -name 'CompilerPlugin.toml'` | no matches |
| 25 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/sap.s4hana.salesarea_0001/2.1.0` | isDeprecated false; modules list = 1 (default only); graalvmCompatible Yes; pullCount 21 |
| 26 | `diff <(json.tool old.json) <(json.tool new.json)` | 4 change classes: +2 `baseType`, +5 `annotations`, −2 `Additional Values` params |
| 27 | `python3` param dump of `getSalesArea` in both JSONs | old 7 params, new 6; `queries` `"optional": true` in both, no `defaultValue` on any param |
| 28 | `python3` typeDefs count both JSONs | **10 in both** — `old` had the options types, could not render them |
| 29 | `cat OLD_AND_NEW_DIFFS/sap.s4hana.salesarea_0001_diff.md` | every figure independently reproduced; accurate |
| 30 | `sed -n '218,238p' old/*.bal.txt` | confirmed `anydata Additional Values` in both old signatures; `init` doc absent in old too |

## 10. Caveats and unverified items

1. **Render compilability not machine-checked.** The non-compiling constructs in §5 (required param
   after defaultable; unimported `constraint:` prefix; `anydata Additional Values` in `old`) are
   asserted from the Ballerina grammar/spec, not from running `bal build` on the render. The renders
   are digests, not compilation units, so building them was not attempted.
2. **`toSyntaxString` / `renderTypeDef` source not read.** I attributed the `// Unknown type:` →
   real-definition change to the JSON gaining `baseType`, which the JSON diff (check 26/28)
   demonstrates. I did not read the TypeScript renderer to confirm the code path; the causal claim
   is inference from the data, and the data is unambiguous.
3. **Runtime behaviour not exercised.** No call was made against a live S/4HANA endpoint; correctness
   claims are static, source-vs-render only.
4. Everything else in this report was verified directly — notably the upstream-vs-bala byte identity
   (check 23), which removes the usual GitHub/bala ambiguity for this library.

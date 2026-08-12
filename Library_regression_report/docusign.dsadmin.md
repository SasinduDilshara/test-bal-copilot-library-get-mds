# ballerinax/docusign.dsadmin 2.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/docusign.dsadmin` |
| Pinned version | `2.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-docusign.dsadmin |
| Tag reviewed | `v2.0.0` (commit `41b36f8a86513406912ae9210ae1f5d1b2dc018f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/docusign.dsadmin/2.0.0` |
| Old render | `2514` lines |
| New render | `2516` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library is a single-module, fully generated OpenAPI connector: one `public isolated client class Client`
with 58 resource methods plus `init`, and 151 public types. Upstream `ballerina/{client,types,utils}.bal`
at tag `v2.0.0` are byte-identical to the bala's `modules/docusign.dsadmin/*.bal` (`diff -q`, no output),
so source and bala agree and no ambiguity had to be resolved.

The old→new delta is entirely corrective and additive, in three groups:

1. 51 version/module-qualified type references `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`
   (50 scalar fields + 1 array field), matching the library source exactly.
2. One degraded `// Unknown type: OrganizationAccountSettingsImportResponseArr` placeholder replaced by
   the real definition `type OrganizationAccountSettingsImportResponseArr OrganizationAccountSettingsImportResponse[];`.
3. Two `@display` annotations now surfaced (`ConnectionConfig`, `ProxyConfig.password`), both present
   verbatim in the library source.

Nothing was removed. The `clients` section of the two JSONs is byte-identical, the README block is
byte-identical, and the type-name set is unchanged. No regressions found.

## 2. Change inventory

Line counts: old `2514`, new `2516` (`wc -l`). Net +2 = the two added `@display` lines; the
`// Unknown type:` line was replaced 1-for-1 by the type alias.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 1 | 0 |
| `ballerina/lang.int:0.0.0:Signed32` refs | 51 | 0 |
| Any `org/mod:x.y.z:Type` refs (regex sweep) | 51 | 0 |
| `int:Signed32` occurrences (whole file, `grep -o`) | 10 | 61 |
| `^type ` declarations | 150 | 151 |
| `function`/`resource function` declarations | 61 | 61 |
| `enum` / `const` / `class` / `annotation` top-level decls | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `// --- ` section markers | 4 | 4 |

Declarations added (1): `type OrganizationAccountSettingsImportResponseArr`.
Declarations removed: none (`comm -23` on sorted type-name lists → empty).
Client method set: unchanged (`json.dumps(o['clients'])==json.dumps(n['clients'])` → `True`).

JSON-level delta (structural walk of all 151 `typeDefs`, both directions):

| Change | count | example |
|---|---|---|
| field `type.name` `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` | 50 | `OrgReportListResponse_OrgReport.site_id` |
| field `type.name` `...Signed32[]` → `int:Signed32[]` | 1 | `OrgReportConfigurationResponse.enabled_report_types` |
| typedef gains `annotations` key | 1 | `ConnectionConfig` |
| field gains `annotations` key | 1 | `ProxyConfig.password` |
| typedef gains `baseType` key | 1 | `OrganizationAccountSettingsImportResponseArr` (`"Other"` → `"Other"` + `baseType: "OrganizationAccountSettingsImportResponse[]"`) |
| fields dropped / renamed / retyped otherwise | 0 | — |
| doc-string (`description`) changes | 0 | — |

`readme` identical (13 765 chars both sides), `description` identical, `functions`/`services`/`annotations`
arrays empty on both sides, `typeDefs` 151 on both sides.

## 3. Correctness against library source

Verified against the bala (authoritative) and confirmed identical upstream at `v2.0.0`.

- `int:Signed32`: `grep -o 'int:Signed32' modules/docusign.dsadmin/types.bal | wc -l` → **51**.
  New render's Types section (lines 299–2274) → **51** occurrences. Exact match. The old render's
  qualified spelling `ballerina/lang.int:0.0.0:Signed32` appears nowhere in the library source.
- `OrganizationAccountSettingsImportResponseArr`: `types.bal:84`
  `public type OrganizationAccountSettingsImportResponseArr OrganizationAccountSettingsImportResponse[];`
  New render line 437 emits exactly that (minus `public`, per renderer convention). Correct.
- `@display {label: "Connection Config"}`: `types.bal:20`, immediately above `public type ConnectionConfig`.
  New render line 303, same position. Correct.
- `@display {label: "", kind: "password"}`: `types.bal:73`, above `string password = "";` in `ProxyConfig`.
  New render line 374, same position. Correct.
- Type-name set: 151 `^public type` names in the bala vs 151 `^type` names in the new render;
  `comm` both directions → empty. Complete and no invented types.
- Client surface: bala `client.bal` has 58 `resource isolated function` declarations and one
  `public isolated function init` (`client.bal:28`); new render has 58 `resource function` + `init`.
- Spot-checked signatures (bala → new render):
  - `client.bal:63` `get v2/organizations(string? mode = ())` → render 2285 `get v2/organizations(string|() mode = ())` ✔
  - `client.bal:546` `get organizations/[string organizationId]/accounts/[string accountId]/dsgroups(int:Signed32? page = (), int:Signed32? page_size = ())` → render 2439, identical modulo `?`→`|()` ✔
  - `client.bal:808` `get v1/.../accountClones/[string assetGroupWorkId](boolean? include_details = ())` → render 2515 ✔

## 4. Regressions

**None found.**

Basis for that conclusion:
- Full `diff -u old new` reviewed in its entirety (30 hunks, 54 added / 52 removed lines) — every hunk
  is one of the three corrective categories in §1. No hunk deletes a declaration, parameter, default,
  return type, doc comment, or annotation.
- Structural JSON walk over all 151 typedefs (field-set comparison per typedef): `FIELD SET CHANGE`
  bucket empty, `description` bucket empty, no `optional`/`defaultValue` flips.
- `clients` JSON byte-identical → no client-method, parameter, or return-type change.
- `readme` byte-identical → no README/section content lost; both renders keep all 4 section markers.
- Type-name set unchanged; new is a strict superset at the rendered-declaration level (+1).
- Every `int:Signed32` in `new` is syntactically valid without an import (lang.int is implicitly
  imported), whereas the old `ballerina/lang.int:0.0.0:Signed32` was not valid Ballerina at all.

## 5. Issues in `new` (independent of `old`)

All four below are **present identically in `old`** (confirmed: they fall outside every diff hunk), so
they are shared renderer/extractor behaviour, not new defects. Listed because they can mislead an LLM.

1. **Record field defaults dropped; defaultable fields shown as optional.** `ConnectionConfig`
   (`types.bal:20-51`) declares `httpVersion = http:HTTP_2_0`, `timeout = 60`, `forwarded = "disable"`,
   `compression = http:COMPRESSION_AUTO`, `validation = true`; render lines 308–334 emit all of them as
   `?` with no default. Same for `ClientHttp1Settings` (`keepAlive`, `chunking`), `ProxyConfig`
   (`host = ""`, `port = 0`, `userName = ""`, `password = ""` → all `?`), and
   `OAuth2RefreshTokenGrantConfig.refreshUrl` (default `"https://account.docusign.com/oauth/auth"` lost).
2. **Closed records rendered as open.** `types.bal` declares `ConnectionConfig`, `ClientHttp1Settings`,
   `ProxyConfig`, `OAuth2RefreshTokenGrantConfig` as `record {| ... |}`; the render emits `record { ... }`.
3. **`Client.init` signature is not valid Ballerina.** Render line 2281 expands the included record
   parameter `*ConnectionConfig config` (bala `client.bal:28`) into 16 defaulted positional params and
   then appends a *required* `ConnectionConfig config` at the end — a required param after defaulted
   params, and a duplicate of the same data. It also invents a default `auth = {token: ""}` for a field
   that is required in the source, and writes `compression = AUTO` where the source constant is
   `http:COMPRESSION_AUTO` (unqualified, wrong name).
4. **Type-inclusion flattening is unlabelled.** `OAuth2RefreshTokenGrantConfig` includes
   `*http:OAuth2RefreshTokenGrantConfig` (`types.bal:77`); the render (lines 339–351) inlines the
   inherited fields without indicating the inclusion, so the `http:`-module provenance of
   `refreshToken`/`clientId`/`clientSecret`/`scopes`/… is lost.

## 6. Coverage gaps vs. the library

**None.**

- The bala contains exactly one module (`modules/docusign.dsadmin`) — no submodules, so the shared
  `getDefaultModule()` limitation does not apply here.
- Public symbols in the default module: 151 `public type` + 1 `public isolated client class Client`
  (with `init` + 58 resource methods). All 151 types and all 59 client methods appear in both renders.
- Correctly excluded module-private symbols: `enum EncodingStyle` (`utils.bal:34`),
  `type Encoding` (`utils.bal:23`), and the 8 non-public `isolated function`s in `utils.bal` — none are
  `public`, so their absence is correct, not a gap.

## 7. Compiler plugin

The package ships **no compiler plugin**: `find` over the clone (depth 3) returns no
`*compiler-plugin*` path, and the bala root contains only `bala.json`, `dependency-graph.json`,
`docs/`, `modules/`, `package.json` — no `compiler-plugin/`. Nothing plugin-derived is therefore
expected in, or missing from, the render.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/docusign.dsadmin/2.0.0` returns
  `deprecateMessage: ""`, `visibility: "public"`, `pullCount: 13070`. Stable major version (2.0.0).
- **Old distribution.** `Ballerina.toml` / Central both report `distribution = 2201.8.4`, considerably
  older than current Swan Lake updates. Not a render issue.
- **Size/token impact is negligible**: +2 lines (~0.08 %). The change trades 51 long qualified type
  names for short ones, so the new render is slightly *cheaper* in tokens while being more accurate.
- **Doc quality**: several types carry empty doc comments in the source (e.g. `types.bal:85-100`
  `OrgReportListResponse_OrgReport` has bare `#` markers); the render reproduces the resulting empty
  descriptions faithfully on both sides.
- The README block is a full Package.md copy (lines 7–297) including setup screenshots' URLs and a
  quickstart with a `main()` example; unchanged between sides.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `git ls-remote --tags .../module-ballerinax-docusign.dsadmin` | only `v2.0.0` → `41b36f8a…` |
| 2 | `git clone --depth 1 --branch v2.0.0 …` | OK; `ballerina/{client,types,utils}.bal` present |
| 3 | `diff -q src/ballerina/types.bal bala/types.bal`; same for `client.bal`, `utils.bal` | no output (identical) |
| 4 | `wc -l old new` | 2514 / 2516 |
| 5 | `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| 6 | `grep -c 'ballerina/lang.int:0.0.0:Signed32'` old / new | 51 / 0 |
| 7 | `grep -oE '[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:[A-Za-z0-9_]+'` old / new | 51 (all lang.int) / 0 |
| 8 | `diff -u old new` (full, unelided) | 30 hunks; only Signed32 requalification, 2 `@display` adds, 1 Unknown-type→alias |
| 9 | `grep -oE '^type X' | sort` + `comm` both ways | new-only: `OrganizationAccountSettingsImportResponseArr`; old-only: none |
| 10 | `grep -oE '^public type …' bala/*.bal | sort` vs new render type list, `comm` both ways | 151 vs 151, both differences empty |
| 11 | Python structural walk of `typeDefs` (151 each), name-set + per-field compare | 32 typedefs changed; buckets: 50×Signed32, 1×Signed32[], 1×`annotations` (typedef), 1×`annotations` (field), 1×`baseType`; zero field-set or description changes |
| 12 | `json.dumps(o['clients'])==json.dumps(n['clients'])` | `True` |
| 13 | `o['readme']==n['readme']`, `o['description']==n['description']` | `True`, `True` (13 765 chars) |
| 14 | `grep -o 'int:Signed32' bala/types.bal | wc -l` vs new render lines 299–2274 | 51 vs 51 |
| 14b | `grep -o 'int:Signed32'` whole file, old / new | 10 / 61 (old's 51 are spelled `…lang.int:0.0.0:Signed32`; client-section count 10 on both sides) |
| 15 | `bala/types.bal:84` vs new render line 437 | alias definition matches |
| 16 | `bala/types.bal:20` and `:73` vs new render lines 303 and 374 | `@display` annotations match verbatim |
| 17 | `grep -cE '^\s+resource isolated function' bala/client.bal` vs render | 58 vs 58 (+`init` both) |
| 18 | `bala/client.bal:63,546,808` vs render lines 2285, 2439, 2515 | signatures match (`?` rendered `|()`) |
| 19 | `grep -nE '^public ' bala/*.bal` (non-type) | only `client.bal:21 public isolated client class Client` |
| 20 | `grep -nE '^(public )?(const|enum|annotation|listener)' bala/*.bal` | only non-public `enum EncodingStyle` (`utils.bal:34`) |
| 21 | `ls` bala root & `find src -iname '*compiler-plugin*'` | no compiler plugin anywhere |
| 22 | `ls bala/any/modules` | single module `docusign.dsadmin` — no submodules |
| 23 | `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/docusign.dsadmin/2.0.0` | not deprecated, 1 module, `ballerinaVersion 2201.8.4` |
| 24 | Read new render lines 296–405 and 2270–2290 | confirms §5 items 1–4 verbatim; both also present in old (outside all diff hunks) |
| 25 | `OLD_AND_NEW_DIFFS/docusign.dsadmin_diff.md` cross-check | its counts (2514/2516, 1→0 Unknown, 51→0 qualified, +1 decl, 0 removed) all reproduce |

## 10. Caveats and unverified items

- The renders were not recompiled from the two `ballerina-vscode` checkouts; the audit compares the
  supplied artifacts against the library source. The claim that the delta is caused by the extractor
  change (not a library change) is supported by the library being byte-identical on both sides
  (bala == upstream tag) and by the JSON `clients`/`readme` being byte-identical, but the pipeline runs
  themselves were not re-executed here.
- The §5 items are asserted to be identical in `old` on the basis that they lie outside every hunk of
  the full `diff -u`; individual old-side line reads were done only for the `init` line region.
- The two `@display` annotations are the only annotations in the library source (`grep -n '@display'`
  returns exactly 2 hits); no other annotation could be checked for loss because none exist.

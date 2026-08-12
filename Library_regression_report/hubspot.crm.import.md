# ballerinax/hubspot.crm.import 4.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.import` |
| Pinned version | `4.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.import |
| Tag reviewed | `v4.0.2` (exact match; commit `65f1d430622c8754ba2a5f7fee4530be18b1b87c`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.import/4.0.2` |
| Old render | `525` lines |
| New render | `526` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, fully auto-generated OpenAPI connector: one module (`hubspot.crm.import`), 20 public types,
one `Client` class with 5 resource functions + `init`. No module-level functions, services,
listeners, enums, constants or annotations exist in the package, so those sections are legitimately
empty on both sides.

`new` differs from `old` in exactly three ways, all of them corrections:

1. All 9 version-qualified `ballerina/lang.int:0.0.0:Signed32` refs become `int:Signed32` (matches
   the source exactly).
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — present in the
   library source but dropped by `old` — is now emitted.
3. The synthetic, non-compiling `anydata Additional Values` pseudo-parameter is removed from the two
   resource functions that take an included-record query param.

Nothing present in `old` is lost, truncated, or degraded in `new`. `// Unknown type:` count is 0 on
both sides (this package has no error/object/`Other` type defs, so spec v2's main win does not apply
here). README section is byte-identical between the two renders.

## 2. Change inventory

Line counts (`wc -l`): old 525, new 526 (+1).

JSON-level structural comparison (deep recursive diff of the two `.json` files, `old` vs `new`):

| Top-level key | old | new | change |
|---|---|---|---|
| `name`, `description`, `readme` | — | — | identical |
| `typeDefs` | 20 | 20 | same names, same order |
| `clients` | 1 (`Client`) | 1 (`Client`) | same |
| `functions` | 0 | 0 | — |
| `services` | 0 | 0 | — |
| `annotations` | 0 | 0 | — |

Declarations added: **0**. Declarations removed: **0**. Only field/parameter-level changes:

| Kind | Count | Change |
|---|---|---|
| Record field type refs corrected | 9 | `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` (8 scalar + 1 inside `record {\|…...;\|}`) |
| Type annotations added | 1 | `typeDefs[19]` (`ConnectionConfig`) gains `annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]` |
| Client resource-function params removed | 2 | `Additional Values` (`anydata`, "Capture key value pairs") dropped from `get [importId]/errors` (8→7 params) and `get .` (6→5 params) |

The 9 corrected type refs, by owning type:

| Type | Field(s) |
|---|---|
| `PropertyValue` | `updatedByUserId` |
| `ImportTemplate` | `templateId` |
| `PublicImportMetadata` | `counters` (rest type) |
| `ImportRowCore` | `lineNumber`, `fileId` |
| `GetGetPageQueries` | `'limit` |
| `GetImportIdErrorsGetErrorsQueries` | `'limit` |
| `PublicImportError` | `createdAt`, `knownColumnNumber` |

Version-qualified type refs matching `<org>/<mod>:<x.y.z>:`: old **9**, new **0**.

## 3. Correctness against library source

The bala's `modules/hubspot.crm.import/{client.bal,types.bal,utils.bal}` are byte-identical to the
upstream `ballerina/` directory at tag `v4.0.2` (`diff -q` on all three files: identical). So GitHub
and the bala agree; both were used.

All three changes in `new` are confirmed correct:

- `int:Signed32` — every one of the 9 sites is written `int:Signed32` in
  `<bala>/modules/hubspot.crm.import/types.bal` at lines 57, 91, 101, 105, 127, 143, 153, 165, 189.
  `new` matches verbatim; `old`'s `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina.
- `@display {label: "Connection Config"}` — `types.bal:259`, immediately above
  `public type ConnectionConfig record {|` at line 260. It is the only `@`-annotation anywhere in the
  module (`grep -rn '^@' <bala>/modules/hubspot.crm.import/` returns exactly that one line). `new`
  emits it at render line 459 with the identical label.
- `Additional Values` removal — the real signatures are
  `resource isolated function get [int importId]/errors(map<string|string[]> headers = {}, *GetImportIdErrorsGetErrorsQueries queries)`
  (`client.bal:80`) and
  `resource isolated function get .(map<string|string[]> headers = {}, *GetGetPageQueries queries)`
  (`client.bal:96`). There is no `Additional Values` parameter. It was a synthesised artifact of the
  included record's implicit `anydata` rest field, and `old` rendered it as the non-compiling token
  sequence `anydata Additional Values`. Dropping it is correct.

Exhaustive type check (small library, so all 20 were compared field-by-field against `types.bal`):
all 20 public types are present in `new` with the correct field names, order, optionality markers and
types, including the two very large inline string-union enums (`PropertyValue.'source`,
`PublicImportError.errorType` / `objectType`), which are reproduced in full. All 5 resource functions
plus `init` are present with correct accessors, resource paths, return types and doc summaries.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Full `diff -u old new` — 9 hunks, all listed in §2; every `-` line is either a version-qualified
  type ref replaced by the correct one, or the `anydata Additional Values` token.
- Deep recursive JSON diff — reported only `CHG` on 9 type-name strings, one `ADDED` annotation
  array, and two parameter-list length reductions (the `Additional Values` entries). No `REMOVED`
  keys, no dropped typeDefs, no dropped functions.
- Declaration sets identical: 20 typeDefs, same names and order; 1 client, 6 functions, on both sides.
- README section (render lines 1–191) byte-identical between old and new.
- `// Unknown type:` count 0 → 0; section markers 4 → 4.
- No doc string, default value, parameter default, or return type was removed anywhere (the deep
  JSON diff would have surfaced any as `REMOVED`/`CHG`; it did not).

## 5. Issues in `new` (independent of `old`)

All six below are shared with `old` — they are pipeline-wide fidelity limits, not regressions — but
they are inaccuracies in `new` relative to the library source and would mislead a consumer.

1. **Malformed doc-comment continuation** (new:498). The two-line doc on
   `ConnectionConfig.laxDataBinding` (`types.bal:296–297`) loses the `#` prefix on its second line;
   the render emits a bare `and absent fields are handled as \`nilable\` types. Enabled by default`
   inside a record body. Not valid Ballerina. Also present at old:497.
2. **Field defaults dropped; defaultable fields shown as optional.** `ConnectionConfig` (new:460–499)
   renders `httpVersion?`, `http1Settings?`, `http2Settings?`, `timeout?`, `forwarded?`, `cache?`,
   `compression?`, `responseLimits?`, `socketConfig?`, `validation?`, `laxDataBinding?` — but the
   source (`types.bal:261–298`) gives each a required default
   (`http:HTTP_2_0`, `{}`, `{}`, `30`, `"disable"`, `{}`, `http:COMPRESSION_AUTO`, `{}`, `{}`,
   `true`, `true`). Same for `OAuth2RefreshTokenGrantConfig.refreshUrl`
   (`= "https://api.hubapi.com/oauth/v1/token"`, `types.bal:201`) → rendered `string refreshUrl?`.
3. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:260`), `ApiKeysConfig`
   (`types.bal:254`) and `OAuth2RefreshTokenGrantConfig` (`types.bal:197`) are all `record {|…|}` in
   source; the render emits `record {` at new:460, 453, 419.
4. **Included-record query params flattened *and* duplicated, with fabricated defaults.** new:520
   renders `resource function get [int importId]/errors(map<string|string[]> headers = {},
   boolean includeRowData = false, int:Signed32 limit = 0, string after = "",
   boolean includeErrorMessage = false, GetImportIdErrorsGetErrorsQueries queries)`. The real
   signature has only `headers` and `*GetImportIdErrorsGetErrorsQueries queries`. The four expanded
   fields are all *optional with no default* in `GetImportIdErrorsGetErrorsQueries`
   (`types.bal:139–149`), so `limit = 0` / `after = ""` / `= false` are invented values, and listing
   both the expansion and the record itself implies a 6-argument call that does not exist. Same at
   new:521 for `GetGetPageQueries`.
5. **Missing `.` resource path** (new:521): `resource function get (…)` — the source declares
   `resource isolated function get .(…)` (`client.bal:96`). As rendered it does not parse.
6. **Qualifiers dropped.** `public` is absent from all 20 type defs and from `Client`/`init`;
   `isolated` is absent from `init` and all 5 resource functions; `client class Client` (new:504)
   should be `public isolated client class Client` (`client.bal:24`).

## 6. Coverage gaps vs. the library

**0 gaps.**

- `package.json` `export` list is `["hubspot.crm.import"]`; the bala contains exactly one module
  directory, `modules/hubspot.crm.import`. Ballerina Central metadata for `4.0.2` likewise lists a
  single module. There are therefore **no submodules**, and the `getDefaultModule()`-only extraction
  limitation costs nothing here.
- Public symbols in the default module: 20 `public type`s (`types.bal`) + `public isolated client
  class Client` (`client.bal:24`). All 21 appear in both renders.
- `utils.bal` declares only module-private symbols (`type SimpleBasicType`, `type Encoding`,
  `enum EncodingStyle`, and 10 `isolated function`s — none carry `public`). Correctly excluded from
  both renders.

## 7. Compiler plugin

The package has **no compiler plugin**: `find` over the cloned repo for `*compiler-plugin*` /
`*native*` at depth 2 returns nothing, `Ballerina.toml` has no `[[plugin]]` / `[[platform.java*]]`
section, and the bala contains no `compiler-plugin/` directory (bala listing is
`bala.json, dependency-graph.json, docs/, modules/, package.json` only). Nothing plugin-derived is
therefore expected in, or missing from, the render.

## 8. Other considerations

- Not deprecated (`deprecated: null`, empty `deprecateMessage` from Central).
- Stable major version (4.0.2); `distribution = "2201.12.0"`, built with Ballerina `2201.12.2`.
- Size is small and stable: 525 → 526 lines. Token impact of the change is negligible; the two
  giant inline string unions (`PropertyValue.'source`, `PublicImportError.errorType`/`objectType`)
  dominate the render on both sides and are unchanged.
- README section is 184 lines (render lines 7–190) and includes a working `main()` sample; unchanged.
- Net LLM-usability effect of `new`: strictly positive — three constructs that could not compile or
  could not be resolved (`ballerina/lang.int:0.0.0:Signed32`, `anydata Additional Values`) are gone,
  and one piece of real metadata (`@display`) is recovered.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 525 / 526 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each (README, END README, Types, Client) |
| `grep -cE '[a-z]+/[a-zA-Z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 9 / 0 |
| `diff -u old new` | 9 hunks, +12 / −11 lines; all listed in §2 |
| `diff` of render lines 1–191 (README) old vs new | no differences |
| Deep recursive JSON diff (python) old vs new | 9 `CHG` type names, 1 `ADDED` annotations array, 2 param-list `LEN` 8→7 and 6→5; no `REMOVED` |
| JSON top-level counts | typeDefs 20/20, clients 1/1, functions 0/0, services 0/0, annotations 0/0; typeDef name lists equal |
| `git ls-remote --tags <repo>` | tags v3.0.0, v4.0.0, v4.0.1, **v4.0.2** (`65f1d43…`, peeled `12166fa…`) |
| `git clone --depth 1 --branch v4.0.2` | succeeded |
| `diff -q <clone>/ballerina/{client,types,utils}.bal <bala>/modules/hubspot.crm.import/…` | all three **identical** |
| `ls -R <bala>` | `any/{bala.json, dependency-graph.json, docs/{README.md,icon.png}, modules/hubspot.crm.import/{client,types,utils}.bal, package.json}` — no `compiler-plugin/` |
| `<bala>/package.json` `export` | `["hubspot.crm.import"]` (single module) |
| `grep -n 'Signed32' <bala>/…/types.bal` | lines 57, 91, 101, 105, 127, 143, 153, 165, 189 — all `int:Signed32` (9 sites, matches `new`) |
| `grep -rn '^@' <bala>/modules/hubspot.crm.import/` | one hit: `types.bal:259 @display {label: "Connection Config"}` |
| `<bala>/…/client.bal:80,96` | `*GetImportIdErrorsGetErrorsQueries queries` / `get .(… *GetGetPageQueries queries)` — no `Additional Values` param |
| `grep -nE '^(public )?(type\|const\|enum\|class\|function\|isolated function)' <bala>/…/utils.bal` | 12 decls, none `public` |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/hubspot.crm.import/4.0.2` | `deprecated: null`, `ballerinaVersion: 2201.12.2`, `modules: [hubspot.crm.import]` (1 module) |
| `grep -n '^and absent fields' old / new` | old:497, new:498 (shared malformed doc line) |
| `grep -n 'resource function get (\|client class Client\|function init(' new` | 504, 505, 521 |
| `OLD_AND_NEW_DIFFS/hubspot.crm.import_diff.md` claims | verified against the files: line counts, hunk count (9), Unknown-type 0/0, verqual 9→0, 0 decls added/removed — all confirmed |

## 10. Caveats and unverified items

- Neither render was fed to the Ballerina compiler; syntactic claims in §5 (items 1, 4, 5) are based
  on reading the grammar of the emitted text, not on a `bal build`. The specific tokens flagged
  (a doc line lacking `#`, `resource function get (` with no resource path) are unambiguous, but
  "does not compile" is an inference, not a compiler-verified result.
- I did not independently rebuild the renders from the two `ballerina-vscode` commits; the audit
  compares the supplied `old`/`new` artifacts and validates them against the bala and upstream
  source. The brief's attribution of the artifacts to commits `eb5d81b3` / `412ba01e` is taken as
  given.
- §5 items are asserted to be present in `old` as well (hence not regressions); this was confirmed
  by the deep JSON diff reporting no changes in those regions plus direct inspection of
  `old:455–500` and `old:497`, but I did not re-list every one of them line-by-line for `old`.

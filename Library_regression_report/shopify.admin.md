# ballerinax/shopify.admin 3.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/shopify.admin` |
| Pinned version | `3.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-shopify.admin |
| Tag reviewed | `v3.0.0` (exact tag; `git ls-remote --tags` → `41ac3991…`, peeled `3e652061…`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/shopify.admin/3.0.0/any` |
| Old render | `11780` lines |
| New render | `15280` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library, with zero losses.

Two changes, both verified exhaustively:

1. **Types section (+3500 lines, −0 lines).** `new` emits the record-field annotations that `old`
   dropped entirely: 3273 `@jsondata:Name`, 225 `@http:Query`, 2 `@display`. Source `types.bal` in
   the bala contains exactly 3273 / 225 / 2 of these. A programmatic (type, field, annotation-text)
   comparison over all 3499 annotated fields found **0 missing, 0 extra, 0 value mismatches**.
2. **Client section (103 lines modified, no other change).** `old` emitted a fabricated, syntactically
   illegal parameter `anydata Additional Values` in 103 of the 320 client method signatures. It came
   from the JSON parameter entry `{"name": "Additional Values", "description": "Capture key value
   pairs", "type": "anydata"}` — i.e. the implicit `anydata...` rest descriptor of the open
   `*XxxQueries` included-record parameter, leaked as a parameter. `new` drops that entry from the
   JSON and hence from the render. No other client text changed.

Declaration inventory is byte-for-byte equal otherwise: same 912 types, same 320 client functions,
identical README (lines 1–151 diff clean), identical section markers, 0 `// Unknown type:` on both
sides.

## 2. Change inventory

Section boundaries (`grep -n '^// --- '`): README 7–151, Types 153–10489 (old) / 153–13989 (new),
Client 10490–11780 (old) / 13990–15280 (new).

| Item | old | new | Δ |
|---|---|---|---|
| Total lines | 11780 | 15280 | +3500 |
| `type X record` declarations | 912 | 912 | 0 |
| Client classes | 1 | 1 | 0 |
| Client functions (`init` + remote) | 320 | 320 | 0 |
| `remote function` declarations | 319 | 319 | 0 |
| Enums / consts / annotations / services / listeners | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 | 0 |
| `@jsondata:Name` | 0 | 3273 | +3273 |
| `@http:Query` | 0 | 225 | +225 |
| `@display` | 0 | 2 | +2 |
| `anydata Additional Values` params | 103 | 0 | −103 |

Declarations added: **0**. Declarations removed: **0**. Type-name sets are identical
(`comm -23`/`comm -13` on the sorted 912-name lists → both empty). Client method-name sets are
identical (`diff old_methods.txt new_methods.txt` → identical).

Diff decomposition, verified by splitting the two files at the `// --- Client ---` marker:

- Types region diff: **+3500 / −0**. Every added line is an annotation line
  (`@jsondata:Name` / `@http:Query` / `@display`). Zero removals.
- Client region diff: **+103 / −103**. Every `-` line and every `+` line is the same method
  signature with/without `anydata Additional Values, `. Filtering the 103 `-` lines for anything
  *not* containing `anydata Additional Values` returns nothing.

This matches the precomputed `OLD_AND_NEW_DIFFS/shopify.admin_diff.md` (+3603 / −103 = net +3500;
3500 type-section additions + 103 rewritten client lines).

## 3. Correctness against library source

The bala and the GitHub `v3.0.0` tag are byte-identical (`cmp` on `client.bal`, `types.bal`,
`utils.bal` → all SAME), so there is no source ambiguity.

- **Annotations (the whole of what `new` adds).** Parsed `(record type, field, annotation lines)`
  triples out of `modules/shopify.admin/types.bal` and out of the `new` render and compared as sets:
  3499 annotated fields on each side, `source \ render` = 0, `render \ source` = 0, value mismatches
  = 0. Annotation kind totals also match exactly (3273 / 225 / 2 on both sides).
  Spot-checked by hand:
  - `types.bal:12259-12265` `RetrieveAListOfApplicationChargesQueries.sinceId` carries
    `@http:Query {name: "since_id"}` → present verbatim in `new`, absent in `old`.
  - `types.bal:11896-11900` `ApiKeysConfig.xShopifyAccessToken` carries
    `@display {label: "", kind: "password"}` → present in `new`, absent in `old`.
  - `types.bal:9954` type-level `@display {label: "Connection Config"}` on `ConnectionConfig` →
    present in `new`, absent in `old`.
- **Type inventory.** 912 `public type … record` in `types.bal` == 912 in each render, names
  identical both directions. `utils.bal` declares no `public` symbols. `client.bal` declares one
  public symbol, `public isolated client class Client` (line 33).
- **Field inventory.** 6022 record fields in source, 6022 in each render; per-type field-name sets
  match for all 912 types (the only parser deltas were on `ConnectionConfig` default-value literals,
  an artifact of my regex, confirmed by reading `types.bal:9955-9990`).
- **Field types.** 84 field-type spellings differ from source text on **both** sides identically;
  all 84 are semantically equivalent normalisations (`T?` → `T|()`, `record {}` →
  `record {|anydata...;|}`). No side has a wrong type.
- **Client signatures.** 319 `remote isolated function` names in `client.bal` == the 319 in each
  render, `diff` identical. `init` matches `client.bal:42`
  (`init(ApiKeysConfig apiKeyConfig, string serviceUrl, ConnectionConfig config = {}) returns error?`).
  103 methods take `*XxxQueries queries` in source, and exactly 103 render lines carry the
  `…Queries queries)` tail on both sides — the same set that `old` polluted with
  `anydata Additional Values`.
- **The removed parameter does not exist.** `grep -c "Additional Values"` over `types.bal` and
  `client.bal` → 0. It is not a library symbol; `old` invented it. Its removal in `new` is a
  correctness fix, not a loss.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Whole-file `diff -u` split by section. Types region has **zero** deleted lines. Client region has
  103 deleted lines, and every one of them is a signature whose only textual loss is the fabricated
  `anydata Additional Values, ` fragment — verified by grepping the `-` line set for any line lacking
  that fragment (empty result).
- README region (`sed -n '1,151p'`) is identical on both sides — `diff` returns clean.
- Type-name, field-name, field-type, field-optionality, client-method-name sets are all equal
  between `old` and `new` (the field-type/optionality comparisons against source produce byte-equal
  reports for both sides: 84 equivalent type spellings, 11 `ConnectionConfig` optionality deltas).
- Doc comments: the 134 `#` doc lines and 4 section markers are counted identically in both files.
- No annotation, default, return type, or parameter (other than the bogus one) is dropped.
- Non-ASCII content is identical on both sides (3 lines, all typographic apostrophes in prose).

## 5. Issues in `new` (independent of `old`)

Seven. One is introduced by `new`; six are pre-existing pipeline behaviours shared with `old` and are
listed because the brief asks for inaccuracies in `new` regardless of `old`.

1. **(new-only, cosmetic)** The render now uses the prefixes `jsondata:` and `http:` in annotations
   but declares no imports — `grep -c '^import'` over lines 152–15280 of `new` returns 0 (the only
   two `import` lines in the file are inside the README code fences). An LLM copying a rendered type
   definition verbatim gets an unresolved-prefix error unless it also adds
   `import ballerina/data.jsondata;` / `import ballerina/http;`. Low impact — these are library types
   the consumer references rather than redeclares.
2. **(shared)** Included-record parameters are rendered twice and illegally. Source
   `client.bal:109`: `retrieveAListOfApplicationCharges(map<string|string[]> headers = {},
   *RetrieveAListOfApplicationChargesQueries queries)`. Render (`new` line 13990+):
   `…(map<string|string[]> headers = {}, string fields = "", string sinceId = "",
   RetrieveAListOfApplicationChargesQueries queries)` — the included record's fields are flattened
   *and* the record itself is repeated as a required parameter after defaulted ones, which is not
   valid Ballerina. Affects 103 methods on both sides. `new` makes these lines shorter but does not
   fix the shape.
3. **(shared)** Closed records lose closedness: `public type ConnectionConfig record {|…|}`
   (`types.bal:9955`) and `public type ApiKeysConfig record {|…|}` (`types.bal:11896`) both render as
   open `record { … };`.
4. **(shared)** `ConnectionConfig` default values are dropped and required-with-default fields become
   optional: source `http:HttpVersion httpVersion = http:HTTP_2_0;` renders as
   `http:HttpVersion httpVersion?;`. 11 fields affected, identically on both sides.
5. **(shared)** A wrapped doc comment loses its `#` continuation prefix, producing a non-compiling
   bare line: `new` line 12822 / `old` line 9562 — `and absent fields are handled as \`nilable\`
   types. Enabled by default.` sits outside any comment.
6. **(shared)** All 912 types render without the `public` modifier (`grep -c '^public type'` → 0 in
   both), and the client renders as `client class Client` rather than
   `public isolated client class Client`; `remote isolated function` becomes `remote function`
   (0 vs 319). Visibility and isolation qualifiers are uniformly stripped.
7. **(shared)** Size: the new render is 15280 lines / ~640 KB of context for one connector. The
   annotation payload is +3500 lines (+30%). Accurate, but it is a real token cost.

## 6. Coverage gaps vs. the library

**Zero.**

- The package exports exactly one module — `package.json` `"export": ["shopify.admin"]`, and the bala
  has a single directory `modules/shopify.admin`. Central metadata for `ballerinax/shopify.admin/3.0.0`
  lists one module. There is therefore **no submodule-only API**, so the known
  `getDefaultModule()`-only limitation costs this library nothing.
- Default-module public symbols: 912 `public type` (types.bal) + 1 `public isolated client class Client`
  (client.bal:33). All 912 types appear in both renders; the client and all 319 of its remote methods
  plus `init` appear in both. `utils.bal` has no public declarations.
- No public functions, enums, constants, annotations, listeners, or services exist in the library, so
  the renders' zero counts for those are correct, not gaps.

## 7. Compiler plugin

The package ships **no compiler plugin**: the bala has no `compiler-plugin/` directory and no
`compiler-plugin.json` (only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json`), and `find` over the cloned `v3.0.0` tree matches no `*compiler-plugin*` path.
`Ballerina.toml` has no `[[plugin]]` section. Nothing plugin-derived is therefore expected in, or
missing from, either render.

## 8. Other considerations

- Not deprecated: Central returns an empty `deprecateMessage` and no `deprecated` flag for 3.0.0.
- Stable major version (3.0.0), built for distribution `2201.13.0`, `graalvmCompatible = true`.
  Low pull count (49) — this is a recently published major.
- The `@jsondata:Name` / `@http:Query` payload is genuinely valuable for an LLM here: this connector
  is an OpenAPI-generated REST wrapper whose Ballerina field names (`createdAt`, `sinceId`) differ
  from the wire names (`created_at`, `since_id`) in 3498 places. `old` gave a consumer no way to know
  the wire contract; `new` does.
- The `@display {kind: "password"}` on `ApiKeysConfig.xShopifyAccessToken` now surfaces, which is a
  meaningful secret-handling hint that `old` hid.
- README is carried identically and is substantive (145 lines, setup + 4-step quickstart + example
  links).

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 11780 / 15280 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; Client at 10490 (old) / 13990 (new) |
| `git ls-remote --tags <repo>` | `v0.1.0`, `v0.9.0`, `v3.0.0` → exact tag `v3.0.0` exists |
| `git clone --depth 1 --branch v3.0.0` | OK; `ballerina/{client,types,utils}.bal` = 4906 / 12944 / 219 lines |
| `cmp` bala vs clone for the 3 `.bal` files | all SAME |
| `ls bala/any` | no `compiler-plugin/`; `modules/` holds only `shopify.admin` |
| `cat bala/any/package.json` | `"export": ["shopify.admin"]`, ballerina_version 2201.13.0 |
| Central `…/packages/ballerinax/shopify.admin/3.0.0` | 1 module, no deprecation, pullCount 49 |
| `grep -oE '^type X' \| sort` both renders | 912 / 912; `comm` both directions empty |
| `grep -oE 'remote isolated function' client.bal` vs renders | 319 / 319 / 319; `diff` identical |
| JSON `clients[0].functions` length | 320 old, 320 new |
| JSON `typeDefs` length | 912 old, 912 new |
| JSON param dump for `retrieveAListOfApplicationCharges` | old has `{"name":"Additional Values","type":"anydata","description":"Capture key value pairs"}`; new does not |
| `grep -c 'anydata Additional Values'` renders | 103 old, 0 new |
| `grep -c 'Additional Values' bala types.bal + client.bal` | 0 — symbol does not exist in the library |
| Client-region `diff -u` | 103 `-` / 103 `+`; `-` lines lacking `anydata Additional Values` → none |
| Types-region `diff -u` | 3500 `+`, **0** `-` |
| `grep -c` `@jsondata:Name` / `@http:Query` / `@display` in `new` | 3273 / 225 / 2 |
| same greps on bala `types.bal` | 3273 / 225 / 2 |
| same greps on `old` render | 0 / 0 / 0 |
| Annotation triple set-compare (source vs `new`, 3499 fields) | missing 0, extra 0, mismatched 0 |
| Field-name set-compare per type (source vs each render) | 6022 fields each; no real deltas |
| Field-type compare (source vs each render) | 84 differences, identical on both sides, all semantically equivalent (`T?`↔`T\|()`, `record {}`↔`record {\|anydata...;\|}`) |
| Field-optionality compare | 11 `ConnectionConfig` deltas, identical on both sides |
| `diff` README region (lines 1–151) | identical |
| `grep -c '[^ -~]'` both renders | 3 / 3, same lines (prose apostrophes) |
| `grep -c '^public type'` / `remote isolated function` in `new` | 0 / 0 |
| `grep -c '^import'` lines 152–end of `new` | 0 |
| `grep -c 'Queries queries)'` renders vs `\*…Queries queries` in source | 103 / 103 / 103 |
| `OLD_AND_NEW_DIFFS/shopify.admin_diff.md` | +3603 / −103, 0 declarations added or removed — consistent with the above |

## 10. Caveats and unverified items

- Neither render was compiled. The syntax defects noted in §5 (items 2, 3, 5, 6) were identified by
  reading the render against the Ballerina grammar and the library source, not by running `bal build`.
  They are pre-existing on both sides and do not affect the regression verdict.
- Doc-string *text* was compared structurally (`#`-line counts, section markers, README byte diff, and
  the full client-region `diff` showing only the parameter change) rather than sentence by sentence
  across all 912 types. Given the Types region has zero deleted lines, no doc text can have been lost.
- Central's package endpoint was queried for module list and deprecation only; keywords/licensing were
  read from the bala `package.json` instead.
- The claim that `new`'s dropped `Additional Values` entry originates from the open-record rest
  descriptor is an inference from the JSON's description string (`"Capture key value pairs"`) and the
  fact that all 103 affected methods take an open `*XxxQueries` record. The extractor source was not
  read to confirm the mechanism. The conclusion that the parameter is bogus is independently
  established: no such symbol exists anywhere in the library source.

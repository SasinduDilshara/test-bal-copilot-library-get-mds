# ballerinax/paypal.invoices 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/paypal.invoices` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-paypal.invoices |
| Tag reviewed | `v1.0.2` (exact match; `git ls-remote --tags`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/paypal.invoices/1.0.2` |
| Old render | `1153` lines |
| New render | `1251` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Pure improvement. `new` is +109/−11 lines over `old` across 36 hunks. Three things changed, all for the better:

1. All 7 `// Unknown type:` placeholders in `old` are replaced by real, correct `type X string;` definitions with their doc comment and `@constraint:String` annotation (`CurrencyCode`, `DateTime`, `DateNoTime`, `Percentage`, `CountryCode`, `EmailAddress`, `Language`).
2. 90 `@constraint:{String,Int,Array}` annotations are now emitted on record fields and type defs — `old` emitted **zero**. The rendered annotation multiset is byte-identical to the bala's `types.bal` annotation multiset.
3. `@display {label: "Connection Config"}` is now emitted on `ConnectionConfig` (matches bala `types.bal:269`).
4. Four client resource signatures lost the malformed, non-compiling parameter `anydata Additional Values`. That parameter had a space in its identifier and was invalid Ballerina; removing it is a fix, not a loss.

Nothing was removed, truncated, or made less accurate. README, package description, and typeDef name set are byte-identical between the two JSONs. Zero regressions.

Both renders share the same pre-existing fidelity defects (record defaults dropped, `record {|…|}` flattened to open, `isolated`/`public` qualifiers dropped, `*Queries` included-record-params expanded with type-zero defaults, `'202Response` emitted unquoted). Those are listed in §5 because they are still wrong in `new`, but they are unchanged by spec v2.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 1153 | 1251 |
| Diff hunks | — | 36 |
| Lines added / removed | — | +109 / −11 |
| `// Unknown type:` placeholders | 7 | 0 |
| Version/module-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 (README, END README, Types, Client) | 4 (same) |
| Top-level declaration names parsed from render | 83 | 90 |
| `@constraint:` annotation lines | 0 | 90 |
| `@display` annotation lines | 0 | 1 |

### Declarations added in `new` (7 — all previously degraded to `// Unknown type:`)

`type CountryCode`, `type CurrencyCode`, `type DateNoTime`, `type DateTime`, `type EmailAddress`, `type Language`, `type Percentage` — each a `string` subtype with its doc comment and constraint annotation.

### Declarations removed in `new`

None. Verified: `comm -23` of the old vs new declaration-name sets is empty (script in §9).

### Declarations modified in `new`

| Kind | Count | Change |
|---|---|---|
| Record type defs | 30 | `@constraint:*` annotations added to fields (no field added/removed/retyped) |
| Record type def | 1 | `ConnectionConfig` gains `@display {label: "Connection Config"}` |
| Client resource functions | 4 | `anydata Additional Values` parameter dropped (`get invoices`, `put invoices/[invoiceId]`, `post search\-invoices`, `get templates`) |

### JSON-level change

`typeDefs` 88 → 88 (same names, verified set-equal). `clients` 1 → 1. `functions`/`services`/`annotations` 0 on both. `readme` and `description` byte-identical. Two JSON deltas:

- 7 `typeDefs` entries gained `"baseType": "string"` + `"annotations": [...]` (e.g. `CurrencyCode` in `old` is `{"name","description","type":"Other"}`; in `new` it also carries `baseType` and the `ballerina/constraint` `String` annotation). This is the extractor change that makes the 7 renderable.
- 4 `clients[0]` function parameter lists lost the entry `{"name":"Additional Values","type":{"name":"anydata"},"description":"Capture key value pairs","optional":true}`.

## 3. Correctness against library source

Upstream `v1.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's `modules/paypal.invoices/*.bal` (`diff -q`, all three identical), so source and bala agree; checks below cite the bala.

All 7 restored types verified one-by-one against `types.bal` — base type, doc string, and constraint all match:

| Type | bala | render (`new`) | match |
|---|---|---|---|
| `CurrencyCode` | `types.bal:230` `public type CurrencyCode string;` + `@constraint:String {maxLength: 3, minLength: 3}` | `:182` | ✅ |
| `DateTime` | `types.bal:168` + `{maxLength: 64, minLength: 20, pattern: re \`^[0-9]{4}-…\`}` | `:203` | ✅ |
| `DateNoTime` | `types.bal:430` + `{maxLength: 10, minLength: 10, pattern: …}` | `:220` | ✅ |
| `Percentage` | `types.bal:766` + `{pattern: re \`^((-?[0-9]+)\|(-?([0-9]+)?[.][0-9]+))$\`}` | `:427` | ✅ |
| `CountryCode` | `types.bal:674` + `{maxLength: 2, minLength: 2, pattern: re \`^([A-Z]{2}\|C2)$\`}` | `:595` | ✅ |
| `EmailAddress` | `types.bal:409` + `{maxLength: 254, minLength: 3, pattern: re \`^.+@[^"\-].+$\`}` | `:656` | ✅ |
| `Language` | `types.bal:614` + `{maxLength: 10, minLength: 2, pattern: …}` | `:692` | ✅ |

Constraint annotations, exhaustive check (not a spot-check): `diff <(grep -oE '@constraint:.*' bala/types.bal | sed 's/^ *//' | sort) <(grep -oE '@constraint:.*' new.bal.txt | sed 's/^ *//' | sort)` → **no differences**, 90 vs 90. Every constraint the library declares is present in `new`, with no invented ones.

`@display {label: "Connection Config"}` — bala `types.bal:269`, render `new:952`. Correct and correctly attached.

Client: bala `client.bal` declares `init` + 22 resource functions (`grep -n 'resource function' → 22`). `new` renders `init` + all 22, with matching methods, paths, payload types, and return types (e.g. `post invoices/[string invoiceId]/send … returns LinkDescription|'202Response|error` at `client.bal:67` ↔ render `:1182`). No method dropped or invented.

Dropped `Additional Values` parameter is correct behaviour: the four affected methods take `*InvoicesListQueries queries` / `*InvoicesUpdateQueries` / `*InvoicesSearchInvoicesQueries` / `*TemplatesListQueries` (`client.bal:41,195,221,235`). Those query records are **open** (`record {` not `record {|`, e.g. `types.bal:313`), so the extractor had been surfacing the implicit `anydata` rest field as a pseudo-parameter literally named `Additional Values` — an identifier with a space, which does not parse. No real API surface is lost by removing it; the only information forgone is "this record is open", which the render never expressed correctly anyway.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Declaration-name set diff old→new: 0 removed, 7 added (Python set comparison, §9).
- Full `diff -u old new`: every one of the 11 removed lines is either a `// Unknown type: X` placeholder (7) or a client signature line replaced by the same signature minus `anydata Additional Values` (4). No other line disappears.
- README section (render lines 7–155) is untouched — first diff hunk starts at line 160; JSON `readme` fields compare equal.
- Section markers: 4 on both sides, same order.
- No parameter, default, return type, or doc comment present in `old` is absent from `new`.
- No type reference in `new` is less specific than in `old`; `old` had 0 version-qualified refs so there was nothing to lose there either.

## 5. Issues in `new` (independent of `old`)

All six are present in `old` as well — they are renderer/extractor limitations, not spec-v2 regressions. Listed because they are still wrong in `new`.

1. **Record field default values are dropped, and defaulted fields are rendered as optional.** `types.bal` has 37 record fields with defaults (`grep -cE '^    [A-Za-z_].* = ' → 37`). None survive. Examples: `int page = 1` → `int page?`; `string fields = "all"` → `string fields?`; `boolean validation = true` → `boolean validation?`; `int width = 500` → `int width?`. An LLM reading the render will believe these fields are unset by default.
2. **Client query params carry fabricated type-zero defaults.** `resource function get invoices(… int page = 0, string fields = "", boolean total_required = false, int page_size = 0, …)` (render `:1174`) vs the real record defaults `page = 1`, `fields = "all"`, `page_size = 20` (`types.bal:316-323`). Worse for `put invoices/[invoiceId]`: render says `send_to_recipient = false, send_to_invoicer = false` (`:1219`) while `InvoicesUpdateQueries` declares both `= true` (`types.bal:556,558`). This is actively wrong, not merely missing.
3. **`'202Response` loses its quoted-identifier prefix.** Render emits `type 202Response record { … }` (`:1090`) and `returns LinkDescription|202Response|error` (`:1182`); the library declares `public type '202Response` (`types.bal:698`). `202Response` is not a valid Ballerina identifier — the render does not compile as written.
4. **Closed records are flattened to open.** bala has 2 `record {|…|}` (`ConnectionConfig`, `OAuth2ClientCredentialsGrantConfig` region); the render has 0.
5. **A multi-line doc comment is broken.** Render line 991 is a bare `and absent fields are handled as \`nilable\` types. Enabled by default.` with no leading `#` — the continuation line of the `laxDataBinding` doc (`types.bal:308-309`). Non-compiling and visually detached from its field.
6. **Qualifiers and included-record-param syntax are dropped.** `isolated` appears 0 times in the render vs 22 `resource isolated function` + `public isolated client class Client` + `public isolated function init` in `client.bal`; `public` appears once (in a README snippet). `*Queries` included-record-params are rendered as ordinary parameters (`(\*` count in render: 0), duplicated alongside their flattened fields, which is not valid Ballerina and is redundant.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** The bala's default (and only) module declares 89 public symbols — 88 `public type` + 1 `public isolated client class Client`. All 89 appear in `new` (Python set comparison: `missing public: []`). `old` was missing 7 (the degraded types), so `new` closes the gap entirely.

- No submodule-only API: `bala/…/modules/` contains exactly one directory, `paypal.invoices`; Central metadata for `1.0.2` lists `modules: ['paypal.invoices']`. The `getDefaultModule()`-only extraction is therefore complete here.
- `utils.bal` declares 6 functions, all module-private `isolated function` (no `public`) — correctly absent from the render.
- One name in the render is not a library symbol: `main`, which is the `public function main()` inside the README usage snippet, not an emitted declaration. Not a coverage issue.

## 7. Compiler plugin

**None.** The upstream `v1.0.2` tree has no `compiler-plugin`/`*-compiler-plugin` directory (`find src -maxdepth 2 -iname '*compiler-plugin*'` → no results), and the bala contains no `compiler-plugin/` directory (`ls` of the bala root shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived is expected in the render, so nothing is missing on that account.

The library does depend on `ballerina/constraint` for validation, and spec v2 now surfaces those constraints — which is exactly the runtime-validation contract a consumer needs and which `old` hid completely.

## 8. Other considerations

- **Not deprecated.** Central `1.0.2`: `isDeprecated: false`, `deprecateMessage: ""`, `ballerinaVersion: 2201.12.0`.
- **Version stability.** `1.0.2` is a stable 1.x release; the bala `package.json` and upstream `Ballerina.toml` both read `version = "1.0.2"` — pin confirmed on both sides, no drift.
- **Size/token impact.** +98 lines (+8.5%). Cheap for the information gained: the 7 restored types are referenced by many record fields (`CurrencyCode`, `DateTime`, `DateNoTime`, `EmailAddress`, `CountryCode`, `Language`, `Percentage` were all dangling references in `old`, i.e. `old` referenced types it never defined).
- **Doc quality.** Docs are verbatim PayPal API descriptions containing raw HTML (`<blockquote>`, `<ul>`, `<code>`) and site-relative links (`/docs/integration/…`). Carried identically on both sides; slightly noisy for an LLM but not a render defect.
- **Net effect for a consumer LLM.** `old` gave 7 unresolvable type references and no validation limits at all; `new` gives complete, accurate types plus every length/range/pattern constraint. Materially better grounding.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old new` | 1153 / 1251 |
| 2 | `grep -c '^// Unknown type:'` on both | old 7, new 0 |
| 3 | `grep -n '^// --- '` on both | 4 markers each, same order, README block lines 7–155 on both |
| 4 | `diff -u old new \| grep -c '^@@'` / `'^+[^+]'` / `'^-[^-]'` | 36 hunks, +109, −11 |
| 5 | Full read of `diff -u old new` | all 11 removals = 7 placeholders + 4 signature lines; all 109 additions = 7 type defs (21 lines), 90 constraint lines, 1 `@display`, 4 replacement signatures |
| 6 | `ls bala/1.0.2/any/modules` | single module `paypal.invoices` |
| 7 | `wc -l bala/modules/paypal.invoices/*.bal` | client 286, types 908, utils 219 |
| 8 | `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1`, `v1.0.2` — exact tag exists |
| 9 | `git clone --depth 1 --branch v1.0.2` then `diff -q src/ballerina/{client,types,utils}.bal bala/…` | all three **identical** |
| 10 | `grep -c '@constraint:' bala/types.bal` / new / old | 90 / 90 / 0 |
| 11 | `diff <(sorted @constraint lines from bala/types.bal) <(sorted from new)` | **no output — sets identical** |
| 12 | Per-type check of 7 restored types (base type + constraint) vs `types.bal:230,168,430,766,674,409,614` | all 7 match exactly |
| 13 | `grep -n '@display'` bala / new / old | `types.bal:269` / `new:952` / old none |
| 14 | Python: public decls in bala (89) vs render decl names | old: 83 names, 7 public missing (`CountryCode CurrencyCode DateNoTime DateTime EmailAddress Language Percentage`); new: 90 names, **0 missing** |
| 15 | Same script, extras | both sides: `main` only (README snippet) |
| 16 | `grep -n 'resource function' bala/client.bal` | 22 resource functions; all 22 + `init` present in `new` (render lines 1170–1250) |
| 17 | JSON compare (Python): typeDef name sets, `readme`, `description` | identical old↔new; `typeDefs` 88/88, `clients` 1/1, `functions`/`services`/`annotations` 0/0 |
| 18 | JSON `clients` unified diff | only 4 removals, each the `"Additional Values"` / `anydata` param object |
| 19 | JSON `typeDefs` entry for `CurrencyCode` | old `{"type":"Other"}` only; new adds `"baseType":"string"` + `ballerina/constraint` `String` annotation |
| 20 | `grep -c 'record {\|' bala/types.bal` vs new | 2 vs 0 (closed records flattened) |
| 21 | `grep -cE '^    [A-Za-z_].* = ' bala/types.bal` | 37 defaulted fields; 0 defaults rendered |
| 22 | `grep -n '202Response'` bala / old / new | bala `'202Response` (`types.bal:698`, `client.bal:67`); both renders emit unquoted `202Response` |
| 23 | `grep -n '^and absent fields are handled'` | old:910, new:991 — bare continuation line, no `#` |
| 24 | `grep -c 'isolated'` new / `grep -c '(\*'` new | 0 / 0 |
| 25 | `grep -nE '^(public\|isolated\|function)' bala/utils.bal` | 6 functions, none `public` |
| 26 | Central API `packages/ballerinax/paypal.invoices/1.0.2` | `isDeprecated:false`, `ballerinaVersion:2201.12.0`, `modules:['paypal.invoices']` |
| 27 | `find src -maxdepth 2 -iname '*compiler-plugin*'` + bala root `ls` | no compiler plugin on either |

## 10. Caveats and unverified items

- **Renders were not compiled.** The syntax defects in §5 (items 3, 5, 6) are identified by reading against the Ballerina grammar and the library source, not by running `bal build` on the rendered text. The renders are excerpt-style stubs and were never intended to compile, so this is a fidelity observation rather than a verified compile failure.
- **`examples/` and `tests/` in the upstream repo were not reviewed** — neither contributes to the extracted default-module API surface.
- Everything else in this report comes from a command whose output is recorded in §9.

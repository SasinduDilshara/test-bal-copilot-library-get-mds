# ballerinax/stripe 2.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/stripe` |
| Pinned version | `2.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-stripe |
| Tag reviewed | `v2.0.1` (commit `cc0b1b0`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/stripe/2.0.1` |
| Old render | `31426` lines (1,942,846 bytes) |
| New render | `33448` lines (2,016,304 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing was removed. Every one of the 911
lines the diff deletes falls into exactly three buckets, all of which are defects being repaired:

| removed line class | count |
|---|---|
| `// Unknown type: X` placeholders replaced by real definitions | 610 |
| resource-function lines carrying the bogus `anydata Additional Values` parameter | 247 |
| lines carrying version-qualified type refs `ballerinax/stripe:2.0.1:T` | 49 |
| blank-line shuffles + diff header | 5 |
| **total** | **911** |

On the gain side `new` recovers 610 type definitions, 2,020 `@constraint` annotations and 2
`@display` annotations that `old` dropped entirely — the annotation counts match the bala source
*exactly* (2,020 and 2).

Declaration-name sets are identical in size and content once `old`'s placeholders are counted:
2,928 names on both sides, **0 declarations removed, 0 renamed**. Both renders cover 100 % of the
default module's public API (2,927 public types + 1 client class). No coverage gaps.

Remaining inaccuracies (closed-record flattening, dropped field defaults, the duplicated
included-record query parameter) are present identically in `old` and `new` and originate in the
Java extractor, not in the spec-v2 renderer change.

## 2. Change inventory

Line counts (`wc -l`): old `31426`, new `33448` (+2,022, +6.4 %). Bytes: 1,942,846 → 2,016,304 (+3.8 %).

Section markers are identical on both sides (4 each): `// --- README ---` @7, `// --- END README ---`
@197, `// --- Types ---` @199, `// --- Client ---` @28888 (old) / @30910 (new).

### Declarations

Extracted with `grep -nE '^(public )?(isolated )?(type|class|enum|const|annotation|function|listener|service|client class)'`
plus `// Unknown type:` lines (which are `old`'s stand-in for a declaration).

| | old | new |
|---|---|---|
| rendered top-level declarations | 2,318 | 2,928 |
| `// Unknown type:` placeholders | 610 | 0 |
| **total declared names** | **2,928** | **2,928** |
| names only in `old` | — | **0** |
| names only in `new` | — | **610** |

`comm -13 old_names new_names` (610 names) is **byte-identical** to the sorted list of `old`'s 610
`// Unknown type:` names. So the 610 "additions" are precisely the 610 types `old` degraded.

All 610 are single-line type aliases (verified: every one matched `^type <name> <rhs>;`; 0 record/
enum/class bodies among them). 311 of them carry a `@constraint` annotation in `new`.

Breakdown of the 2,932 added lines:

| added line class | count |
|---|---|
| `@constraint:...` annotation lines | 2,020 |
| `type X ...;` declaration lines (610 new + 26 de-qualified rewrites) | 636 |
| `resource function ...` lines (rewritten, `Additional Values` dropped) | 247 |
| `@display {...}` annotation lines | 2 |
| record-field lines rewritten to drop `ballerinax/stripe:2.0.1:` | 23 |
| blank | 4 |

### Kind-by-kind

| kind | old | new | delta |
|---|---|---|---|
| type (record) | 2,210 | 2,210 | 0 |
| type (union) | 107 | 107 | 0 |
| type (alias / "Other") | 0 rendered (610 placeholders) | 610 | +610 rendered |
| client class | 1 | 1 | 0 |
| client `init` | 1 | 1 | 0 |
| client resource functions | 537 | 537 | 0 |
| module-level functions / services / listeners / annotations | 0 | 0 | 0 |
| doc-comment lines (`#`) | 8,751 | 8,751 | 0 |
| `@constraint` lines | 0 | 2,020 | +2,020 |
| `@display` lines | 0 | 2 | +2 |
| README lines 1–197 | identical (`diff` empty) | | |

### JSON level

`typeDefs`: 2,927 on both sides, identical name sets, identical kind distribution
(`Record` 2210 / `Other` 610 / `Union` 107). 1,480 typeDefs differ in content — `new` adds
`baseType` and `annotations`, e.g.

```
OLD: {"name":"GetWebhookEndpointsQueriesExpandItemsString","description":"","type":"Other"}
NEW: {"name":"GetWebhookEndpointsQueriesExpandItemsString","description":"","type":"Other",
      "baseType":"string","annotations":[{"name":"String","module":"ballerina/constraint",
      "value":"{maxLength: 5000}"}]}
```

`clients[0].functions`: 538 on both sides, identical keys. 247 differ; the only difference is the
removal of the synthetic parameter `{"name":"Additional Values","description":"Capture key value
pairs","type":{"name":"anydata"},"optional":true}`. Total parameters 2,634 → 2,387 (−247, exactly
one per affected function). `readme`, `description`, `name`, client description all byte-identical.

## 3. Correctness against library source

Upstream `v2.0.1` and the bala are **byte-identical** for all 8 `.bal` files
(`client.bal`, `utils.bal`, `types_1..6.bal`), so GitHub and the bala do not disagree here.

**All 610 added type aliases verified programmatically, not sampled.** For each added name I
located `^public type <name> <rhs>;` in the bala and compared the RHS to the render:

- added names absent from the bala source: **0**
- RHS mismatches: **0**
- `@constraint` annotations present in source but lost in `new`: **0** (311/311 preserved verbatim)

Spot citations:
- `types_6.bal:820-821` `@constraint:String {maxLength: 5000}` / `public type GetWebhookEndpointsQueriesExpandItemsString string;` → `new:29372-29373` identical (old:27478 `// Unknown type: …`).
- `types_3.bal:1389-1390` `Account_requirementsCurrentlydueItemsString` → `new:1299-1300` identical (old:1249 placeholder).
- `types_4.bal:1928-1929` `CustomerPreferredlocalesItemsString` → present in `new`, placeholder in `old`.
- `types_3.bal:2035` `public type subscription_default_tax_rates SubscriptiondefaulttaxratesItemsString[]|"";` → `new` renders exactly that; `old` rendered `ballerinax/stripe:2.0.1:SubscriptiondefaulttaxratesItemsString[]|""`.

**Annotation totals match the source exactly**: `grep -c '@constraint'` over the bala `.bal` files
= 2,020; `new` render = 2,020; `old` = 0. `@display` = 2 in bala (`types_2.bal`, `types_3.bal`),
2 in `new`, 0 in `old`. The per-variant histogram also matches (1,751 × `maxLength: 5000`,
41 × `100`, 29 × `500`, 26 × `22`, …), including the regex forms
`@constraint:String {maxLength: 5000, pattern: re \`^/v1/file_links\`}`.

**Client**: source has 537 `resource isolated function` + 1 `public isolated function init`
(`client.bal:31`). Both renders emit 537 + 1. 272 of the 537 rendered signatures are byte-identical
to the source declaration (after normalising `isolated` and the trailing `{`→`;`) on **both** sides —
identical score, so no signature accuracy was traded away. The 265 non-identical ones differ for two
shared reasons: union aliases are flattened to their members, and `*XQueries` included-record params
are expanded.

**De-qualification is lossless**: for all 49 `old` lines containing `ballerinax/stripe:2.0.1:`, the
de-qualified string appears verbatim in `new` (`0` unmatched). E.g.
`type inline_response_200_2 ballerinax/stripe:2.0.1:Account|…|ballerinax/stripe:2.0.1:Deleted_card;`
→ `type inline_response_200_2 Account|Bank_account|Card|Source|Deleted_bank_account|Deleted_card;`
(`new:29122`). Source `types_6.bal:172` spells it `Payment_source|Deleted_payment_source`, whose
expansion (`types_5.bal:3769`, `types_6.bal:3194`) is exactly those six members — semantically
equal, and identically flattened on both sides.

**The odd `Checkout\\\\\\\.sessionPaymentmethodtypesItemsString` name is faithful, not a render bug.**
It exists verbatim in the published source (`types_1.bal:3660` and `types_1.bal:3845`), alongside a
separate correctly-escaped `Checkout\.sessionPaymentmethodtypesItemsString` (`types_5.bal:4768`).
Both renders reproduce both, and `grep -cE '\\\\'` = 3 on both sides.

## 4. Regressions

**None found.**

What I checked to conclude that:

1. **Nothing dropped.** Set difference of declaration names, `old` minus `new` = **0**.
2. **Every deleted line accounted for.** All 911 `-` lines classify into the three defect buckets in
   §1; the residue is 4 blank lines and the diff header. No `-` line contains a doc comment, an
   annotation, a parameter, a default value, or a return type that survives nowhere in `new`.
3. **Docs intact.** `#`-comment line count identical (8,751/8,751). README block (lines 1–197)
   `diff`-clean. JSON `readme`/`description` byte-identical.
4. **Signatures intact.** 537 resource functions on both sides; pairwise comparison of the 537
   ordered signatures shows 247 differ and **every one of the 247** is explained exactly by deleting
   the substring `anydata Additional Values, ` (`0` unexplained). Return types, parameter names,
   parameter types, defaults and resource paths are otherwise untouched.
5. **Syntax quality improved, not degraded.** `new` contains 0 occurrences of `undefined`,
   `[object Object]`, `NaN`, `,)`, `((`. Non-ASCII byte-line count identical (241/241). No new
   malformed construct appears in the 2,932 added lines.

### One informational nuance (judged *not* a regression)

Deleting the `Additional Values` pseudo-parameter also deletes the only place where `old` hinted
that a `*GetXQueries queries` included record is an **open** record (it is: e.g.
`GetWebhookEndpointsQueries` at `types_6.bal:4510` is `record { … };`, not `record {| … |}`).
I classify the removal as a fix rather than a loss because:
- `anydata Additional Values` is not valid Ballerina — the identifier contains a space, and it was
  emitted as a *required* parameter positioned after defaultable ones. Any LLM copying it produces
  non-compiling code.
- The openness signal is still available: `new` renders the `GetXQueries` type itself as
  `record { … }` (no `|`), which is the Ballerina spelling for "open".
- The bala contains **0** explicit `anydata...` rest descriptors in its type files
  (`grep -c 'anydata\.\.\.' types_*.bal` = 0 everywhere), so nothing concrete was being reported.

## 5. Issues in `new` (independent of `old`)

All seven below are present **identically in `old`**, i.e. they are pre-existing extractor
behaviours, not introduced by spec v2. Listed because they are inaccuracies a consumer should know
about.

1. **Closed records flattened to open.** The bala declares 268 top-level `public type X record {| … |};`
   (e.g. `ConnectionConfig` `types_3.bal:517`, `ClientHttp1Settings`, `ProxyConfig`, and all 265
   `*_body` request payload types). Both renders emit `type X record {` — `grep -cE '^type \S+ record \{\|$'`
   = **0** in both, `^type \S+ record \{$` = **2210** in both (268 closed + 1942 open). An LLM will
   believe every Stripe request-payload record accepts arbitrary extra fields. This is the most
   consequential shared inaccuracy for this library.
2. **Record-field default values dropped.** The bala has 11 defaulted record fields
   (`types_3.bal`: `host = ""`, `port = 0`, `userName = ""`, `password = ""`,
   `httpVersion = http:HTTP_2_0`, `timeout = 60`, `forwarded = "disable"`,
   `compression = http:COMPRESSION_AUTO`, `validation = true`, `keepAlive = http:KEEPALIVE_AUTO`,
   `chunking = http:CHUNKING_AUTO`). Both renders turn them into optional fields with no default,
   e.g. `http:KeepAlive keepAlive?;` (old:19323, new:20555). Only 1 ` = ` survives in the entire
   Types section on either side.
3. **Included-record parameter duplicated.** `client.bal` uses `*GetXQueries queries` in 247
   resource functions. Both renders expand the record's fields into positional parameters **and**
   keep a trailing `GetXQueries queries` parameter, e.g.
   `resource function get webhook_endpoints(map<string|string[]> headers = {}, string ending_before = "", GetWebhookEndpointsQueriesExpandItemsString[] expand = [], int limit = 0, string starting_after = "", GetWebhookEndpointsQueries queries) returns …`
   (new:32094) versus the real `resource isolated function get webhook_endpoints(map<string|string[]> headers = {}, *GetWebhookEndpointsQueries queries)`
   (`client.bal:3406`). Non-compiling as written, and it also renames `'limit` to `limit`.
4. **`@constraint` used without provenance.** `new` emits 2,020 `@constraint:String {…}` lines but
   no `import ballerina/constraint;` and no `// Special Agent Note: … FROM ballerina/constraint package`
   comment, although it does emit exactly that note style for the 14 `ballerina/http` type references.
   Cosmetic, but inconsistent.
5. **`isolated` qualifier lost everywhere.** `grep -c isolated` = 0 in both renders; every function
   in `client.bal` is `isolated`. `init` renders as `function init(…)` rather than
   `public isolated function init(…)` (`client.bal:31`).
6. **Union aliases flattened.** `inline_response_200_2`, `Payment_source`, `External_account`,
   `Deleted_external_account` etc. are rendered as fully expanded member lists rather than the
   source's named-alias unions. Semantically equal; loses the alias relationship.
7. **Doc comment detached from its declaration.** Both renders insert a blank line between the `#`
   doc block and the declaration (`new:20515-20518`), which in real Ballerina detaches the doc.

## 6. Coverage gaps vs. the library

**Zero gaps.**

The bala exports a single module (`package.json` `"export": ["stripe"]`, `modules/` contains only
`stripe`), so the "default module only" limitation described in the brief costs this library
nothing — there is no submodule API to miss.

Enumerated every `^public (isolated )?(type|const|class|client class|function|annotation|listener)`
across the bala's 8 `.bal` files: **2,928 public declarations** (2,927 `type` + 1 `client class`).
Checked each name against both renders (counting `// Unknown type:` names as present in `old`):

- missing from `old`: **0**
- missing from `new`: **0**

`utils.bal` has 0 public declarations, so the render correctly shows no module-level functions.

## 7. Compiler plugin

**There is none.** No `compiler-plugin/` directory or `compiler-plugin.json` anywhere in the bala
(`find … -iname '*compiler*'` returns nothing), and the upstream `v2.0.1` tree has no
`*-compiler-plugin` module — `ballerina/` contains only `Ballerina.toml`, `Dependencies.toml`,
`Module.md`, `Package.md`, `build.gradle`, `icon.png`, `client.bal`, `utils.bal`, `types_1..6.bal`
and `tests/`. Nothing plugin-derived is therefore expected in the render, and nothing is missing.

## 8. Other considerations

- **Not deprecated.** Central `2.0.1` reports `deprecated: null`, `deprecateMessage: ""`,
  `graalvmCompatible: "Yes"`, `pullCount` 392, `ballerinaVersion` 2201.9.0. Stable major (2.x).
- **Size.** This is one of the largest renders in the set. `new` grows 2,022 lines / 73 KB (+3.8 %
  bytes). The growth is almost entirely the 2,020 `@constraint` lines, which are short; the 610
  recovered type definitions cost far less than they buy, since `old` was emitting 610 useless
  comment lines in their place.
- **Constraint annotations are genuinely valuable here.** 1,751 fields carry
  `maxLength: 5000` and several carry `pattern: re \`^/v1/…\``; `old` gave a consumer no way to know
  any of Stripe's string length limits or path patterns.
- **Doc quality is high and unchanged.** 8,751 doc-comment lines on both sides, including Stripe's
  HTML-flavoured `<p>`/`<a>` descriptions copied verbatim.
- **README is complete** — all 189 lines of the Central readme (overview, setup guide with images,
  quickstart with 3 code blocks, examples) are present in both renders and byte-identical.
- **Escaped-identifier oddity in the published package**: `Checkout\\\\\\\.session…` and
  `Reporting\\\\\\\.report_type…` are genuinely over-escaped in the *library*, and one of them
  co-exists with a correctly-escaped twin. Worth reporting upstream; not a render problem.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/new` | 31426 / 33448 |
| 2 | `wc -c old/new` | 1,942,846 / 2,016,304 |
| 3 | `grep -c '^// Unknown type:'` | old 610, new 0 |
| 4 | `grep -n '^// --- '` | 4 markers both; Client @28888 (old) / @30910 (new) |
| 5 | `git ls-remote --tags …module-ballerinax-stripe` | `v2.0.0`, `v2.0.1` only → tag `v2.0.1` = `cc0b1b0` |
| 6 | `git clone --depth 1 --branch v2.0.1` + `diff` of 8 `.bal` files vs bala | all 8 SAME |
| 7 | `ls bala/any/modules` | `stripe` only (single default module) |
| 8 | declaration-name sets, `comm -23` / `comm -13` | 0 only-in-old, 610 only-in-new |
| 9 | `diff old_unknown.txt added.txt` | IDENTICAL (610 lines) |
| 10 | all 610 added names looked up as `public type` in bala | 0 not found, 0 RHS mismatches |
| 11 | `@constraint` on the 610 added aliases | 311 present in source, 311 preserved, 0 lost |
| 12 | `grep -c '@constraint'` bala vs new vs old | 2020 / 2020 / 0 (histograms match) |
| 13 | `grep -c '@display'` bala vs new vs old | 2 / 2 / 0 |
| 14 | `grep -c '^\s*#'` | 8751 both |
| 15 | classification of 911 `-` lines | 610 unknown + 247 `Additional Values` + 49 qualified + 4 blank + 1 header |
| 16 | classification of 2932 `+` lines | 2020 `@constraint` + 636 `type` + 247 resource fn + 2 `@display` + 23 field + 4 blank |
| 17 | pairwise compare of 537 ordered resource-fn signatures | 247 differ; 0 unexplained by removing `anydata Additional Values, ` |
| 18 | de-qualification check: 49 `old` qualified lines | 0 whose de-qualified form is absent from `new` |
| 19 | resource fn count render vs `client.bal` | 537 / 537 / 537 |
| 20 | `grep -n 'function init'` `client.bal:31` vs render | present both sides, `isolated`/`public` dropped both sides |
| 21 | JSON `typeDefs` counts + kinds | 2927 both, `Record` 2210 / `Other` 610 / `Union` 107 both, name sets equal |
| 22 | JSON typeDefs differing | 1480, 0 with changed kind; delta = added `baseType` + `annotations` |
| 23 | JSON `clients[0].functions` | 538 both, keys equal, 247 differ, param total 2634 → 2387 |
| 24 | JSON `Additional Values` params | old 247, new 0 |
| 25 | JSON `readme`/`description`/client description | byte-identical |
| 26 | `diff` of render lines 1–197 (README block) | empty |
| 27 | public-symbol coverage (2928 decls) vs both renders | 0 missing in old, 0 missing in new |
| 28 | `find bala -iname '*compiler*'` + upstream `ballerina/` listing | no compiler plugin |
| 29 | Central `GET /2.0/registry/packages/ballerinax/stripe/2.0.1` | not deprecated, 1 module, graalvmCompatible Yes |
| 30 | `grep -cE '^public type \S+ record \{\|$'` bala vs `^type \S+ record \{\|$` renders | 268 vs 0 / 0 |
| 31 | `grep -cE '^type \S+ record \{$'` renders | 2210 both (= 268 closed + 1942 open) |
| 32 | `grep -c 'anydata\.\.\.'` bala `types_*.bal` | 0 in all six |
| 33 | `grep -c 'isolated'` renders | 0 both |
| 34 | `grep -cE '\\\\'` renders + bala | 3 / 3 / source `types_1.bal:3660,3845` |
| 35 | junk-token scan (`undefined`, `[object Object]`, `NaN`, `,)`, `((`) | 0 / 0 in both |
| 36 | non-ASCII line count | 241 both |

## 10. Caveats and unverified items

- **`GetWebhookEndpointsQueriesExpandItemsString`-style aliases were verified by exact RHS string
  comparison, not by type-checking.** All 610 matched byte-for-byte, so this is a strong result,
  but it does not prove the renderer would handle a *different* alias shape correctly — every one
  of the 610 in this library happens to be a simple alias.
- **The 265 non-byte-identical resource signatures were not each hand-diffed against the source.**
  I verified that the *same* 272 are byte-identical on both sides and that the only old→new delta is
  the `Additional Values` removal, which is sufficient to rule out a regression, but the residual
  shared inaccuracies (§5.3, §5.6) were confirmed only on sampled functions
  (`webhook_endpoints`, `accounts/[account]/bank_accounts/[id]`, `customers/[customer]/bank_accounts/[id]`).
- **I did not build or compile either render.** Claims that specific constructs are "non-compiling"
  (`anydata Additional Values`, the duplicated `queries` parameter) are based on reading the
  Ballerina grammar, not on running `bal build`.
- **Token-count impact is reported in lines and bytes only**; no tokenizer was run.
- **I did not diff the two `ballerina-vscode` source trees**; the attribution of each change class to
  spec v2 is inferred from the brief plus the observed render/JSON deltas.

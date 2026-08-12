# ballerinax/paypal.orders 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/paypal.orders` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-paypal.orders |
| Tag reviewed | `v2.0.2` (commit `939838609e97f31dd13d999df02288794a72ca3a`, grafted shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/paypal.orders/2.0.2` |
| Old render | `2219` lines |
| New render | `2410` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Spec v2 is a clean, strictly additive improvement for this connector. All 33 `// Unknown type:`
placeholders in `old` are replaced with real, source-accurate type definitions; all 168
`@constraint:*` annotations from the published `types.bal` are now emitted (0 in `old`, 168 in
`new`, byte-identical to source); the `@display {label: "Connection Config"}` annotation is now
surfaced; and three lines of malformed / non-compiling Ballerina in `old` are corrected
(`type` → `'type` on two record fields, and removal of the bogus `anydata Additional Values`
parameter from the `get orders/[string id]` resource signature).

A structural JSON walk of every `typeDef` found **zero** keys removed and zero values changed
between `old` and `new` other than those two field-name corrections — nothing was dropped.
Both renders now cover 206/206 public symbols of the default module (205 public types + the
public client class); coverage is complete on both sides. No regressions found.

## 2. Change inventory

Counts from `diff -u old new` (83 hunks, 227 added lines, 36 removed lines):

| Kind | old | new | delta |
|---|---|---|---|
| Total lines | 2219 | 2410 | +191 |
| Top-level declarations (`type` / `class`) | 173 | 206 | +33 |
| — `type` declarations | 172 | 205 | +33 |
| — `client class` | 1 | 1 | 0 |
| `// Unknown type:` placeholders | 33 | 0 | −33 |
| `@constraint:*` annotation lines | 0 | 168 | +168 |
| `@display` annotation lines | 0 | 1 | +1 |
| Doc-comment lines (`# `) | 586 | 608 | +22 |
| Record-field lines | 778 | 778 | 0 |
| Section markers (`// --- `) | 4 | 4 | 0 |
| Non-compiling `type`/`'type` field lines | 2 | 0 | −2 |
| README section (lines 7–131) | — | — | byte-identical |

**Declarations added (33)** — every one previously emitted as a bare `// Unknown type:` line,
now emitted with its real base type, doc comment and constraint annotation:

| Base form rendered | count | names |
|---|---|---|
| `type X string;` | 22 | AccountId, AccountId2, Bic, BillingAgreementId, BinDetailsProductsItemsString, CobrandedCardLabelsItemsString, CountryCode, CountryCode2, CurrencyCode, DateNoTime, DateTime, DateYearMonth, Email, EmailAddress, FullName, IbanLastChars, InstrumentId, IpAddress, Language, MerchantPartnerCustomerId, Url, VaultId |
| `type X anydata;` | 9 | AltpayRecurringAttributes, AltpayRecurringAttributesRequest, ApplePayAttributes, AuthenticationFlow, ExemptionDetails, GooglePayRequest, TrackerStatus, UniversalProductCode, VaultOwnerId |
| `type X Patch[];` | 1 | PatchRequest |
| `type X "ON_SUCCESS";` | 1 | StoreInVaultInstruction |

**Declarations removed: 0.** (`comm -23 old_decls new_decls` → empty.)

**Lines removed that were not `// Unknown type:` placeholders (3), all replaced by corrected forms:**

| old | new | verdict |
|---|---|---|
| `    CardType type?;` (old:1768) | `    CardType 'type?;` (new:1933) | fix — source uses `'type` |
| `    "SHIPPING"\|"PICKUP_IN_PERSON"\|"PICKUP_IN_STORE"\|"PICKUP_FROM_PERSON" type?;` (old:2053) | same with `'type?` (new:2234) | fix — source uses `'type` |
| `resource function get orders/[string id](map<string\|string[]> headers = {}, string fields = "", anydata Additional Values, OrdersGetQueries queries) returns Order\|error;` (old:2194) | same without `anydata Additional Values` (new:2385) | fix — the old token was a space-containing identifier and could never parse |

**JSON-level change inventory** (`old/*.json` vs `new/*.json`): both have 205 `typeDefs`, 1 client,
0 functions, 0 services, 0 annotations, identical `readme` and `description`. 98 `typeDefs` differ;
a recursive key-by-key walk reports **0 keys removed** and only 2 value changes
(`CardRequest.fields[8].name` and `ShippingWithTrackingDetails.fields[3].name`, both `type` → `'type`).
The extractor additions are new `baseType` fields on `"type": "Other"` defs and new
`annotations: [{name, module, value}]` entries on type defs and record fields.
The client differs in exactly one place: `clients[0].functions[2].parameters` shrinks 5 → 4
(the `"Additional Values"` pseudo-parameter is gone).

## 3. Correctness against library source

Upstream `v2.0.2` and the bala are byte-identical for all four relevant files
(`diff -q` on `client.bal`, `types.bal`, `utils.bal`, `README.md` — all `same`), so GitHub and the
bala do not disagree here.

Verified, exhaustively where feasible:

- **All 33 added types** checked one-by-one against `.../modules/paypal.orders/types.bal`. Every
  rendered base type matches the source declaration. Examples:
  - `types.bal:473 public type Email string;` with `@constraint:String {maxLength: 254, minLength: 3}` at `:472` → new render `147: type Email string;` preceded by the same constraint line at `:146`.
  - `types.bal:1494 public type AltpayRecurringAttributes anydata;` (no doc, no constraint) → new render `197: type AltpayRecurringAttributes anydata;`.
  - `types.bal:712 public type PatchRequest Patch[];` → new render `1712: type PatchRequest Patch[];`.
  - `types.bal:392 public type StoreInVaultInstruction "ON_SUCCESS";` → new render `863: type StoreInVaultInstruction "ON_SUCCESS";`.
  - `types.bal:1604 public type VaultOwnerId anydata;` → new render `type VaultOwnerId anydata;`.
- **All 168 constraint annotations** compared as sorted multisets against source:
  `diff <(grep -o '@constraint:.*' new | sort) <(grep -o '@constraint:.*' types.bal | sort)` →
  **CONSTRAINTS IDENTICAL**. Breakdown matches exactly: 154 `String`, 13 `Array`, 1 `Int`.
- **`@display`**: `types.bal:127 @display {label: "Connection Config"}` → new render `337`. Correct.
- **`'type` escaping**: source has 5 lines using `'type` (`types.bal` 779, 882, 1205, 1333, 1352)
  plus `string 'from?;` at `:794`. New render has 7 `'type` field lines (two records repeat a field
  via `*Included` flattening) and 0 unescaped `type` field names; old had 5 escaped + 2 unescaped.
- **Client**: source `client.bal` declares `init` + 8 resource functions. Both renders emit
  `init` + the same 8, with matching accessors, paths, payload types, header record types and
  return types (`client.bal:40,55,66,79,93,107,121,136`).
- **Large union integrity**: `ShipmentCarrier` (a ~17 KB single-line union) renders at exactly
  17003 bytes in both files vs 17010 in source (difference = the 7-byte `public ` prefix the
  renderer omits by convention). Nothing truncated.
- **Structure**: brace-balance check over the Types + Client sections of `new` ends at depth 0 with
  no negative excursions. 0 lines contain unexpected non-ASCII (no mojibake).

## 4. Regressions

**None found.**

What was checked to conclude this:

1. `comm -23` on the sorted declaration sets of both renders → no declaration present in `old` is
   missing from `new`.
2. Recursive JSON diff over all 205 `typeDefs` and the client: **0 keys removed**, 0 fields lost,
   0 descriptions changed, 0 type names changed except the two `type` → `'type` corrections.
3. All 36 removed diff lines enumerated individually: 33 are `// Unknown type:` placeholders and
   3 are the malformed lines listed in §2, each replaced by a strictly more accurate line.
4. README section (render lines 7–131) `diff`ed between old and new → identical; `readme` field in
   the two JSONs compares equal.
5. Record-field line count identical (778 vs 778) — no field dropped anywhere.
6. Doc-comment count rose 586 → 608; none lost.

The one thing `new` no longer states is that `OrdersGetQueries` is an open record accepting
additional query key/value pairs (`old` conveyed this as `anydata Additional Values`). That is not
counted as a regression: the `old` rendering was an unparsable identifier containing a space, it
appeared in the parameter list rather than on the record, and the record itself is rendered
open (`type OrdersGetQueries record {`) in both files, which already carries the same information.

## 5. Issues in `new` (independent of `old`)

All three are inherited from the shared extractor/renderer and are present identically in `old`;
none is introduced by spec v2.

1. **Included-record parameter is rendered as two parameters.** Source
   `client.bal:55` declares `resource isolated function get orders/[string id](map<string|string[]> headers = {}, *OrdersGetQueries queries)`.
   Both renders emit `..., string fields = "", OrdersGetQueries queries)` — the included record is
   simultaneously flattened into `fields` *and* kept as a nominal `queries` parameter, so the
   rendered arity (3) does not match the real arity (2) and an LLM copying it would produce
   non-compiling code. `new` improves this (drops a third bogus parameter) but does not fix it.
2. **Closed records rendered as open.** `types.bal:128 ConnectionConfig record {|` and
   `types.bal:453 OAuth2ClientCredentialsGrantConfig record {|` are closed; both renders emit
   `record {` (0 occurrences of `record {|` in either file).
3. **Record-field default values dropped.** Source has 19 record fields with defaults
   (e.g. `types.bal:132 http:HttpVersion httpVersion = http:HTTP_2_0;`,
   `:456 string tokenUrl = "https://api-m.sandbox.paypal.com/v1/oauth2/token";`,
   `:189/:744/:1469/:1737 string Prefer = "return=representation";`). Both renders turn these into
   plain optional fields (`http:HttpVersion httpVersion?;`, `string tokenUrl?;`), losing the
   default. `= ` appears only in the client function signatures in both files.

Stylistic, not counted as issues: the renderer omits `public`, `isolated` and the `client` keyword
on `class Client`'s methods, by design and identically on both sides.

## 6. Coverage gaps vs. the library

**None.**

- The bala exports exactly one module (`package.json` `"export": ["paypal.orders"]`, and
  `modules/` contains only `paypal.orders`), which is the default module. Ballerina Central
  metadata for `2.0.2` also lists a single module. So the known `getDefaultModule()`-only
  limitation cannot bite here — there is no submodule API.
- Public symbols in the default module: `grep -hoE '^public …' modules/paypal.orders/*.bal` →
  205 `public type` + 1 `public isolated client class`. `utils.bal` exports nothing public.
- The `new` render contains 205 `type` declarations + 1 `client class`.
  `comm -23 src_types new_render_types` → empty (nothing missing);
  `comm -13` → empty (nothing invented).
- `old` was missing 33 of the 205 types (rendered as placeholders).

## 7. Compiler plugin

The package ships **no compiler plugin**: the bala has no `compiler-plugin/` directory
(`ls .../2.0.2/any` → `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`),
and `find` over the upstream `v2.0.2` tree returns no `*compiler-plugin*` path. Nothing is
therefore expected to be contributed to the render by a plugin, and nothing is absent.

## 8. Other considerations

- Not deprecated (Central `deprecated: null`, `deprecateMessage: ""`). Stable 2.x version.
  `pullCount` 37. Built with Ballerina `2201.12.7`, `graalvmCompatible: true`.
- This is a generated OpenAPI connector (`// AUTO-GENERATED FILE ... by the Ballerina OpenAPI tool`),
  which explains the many `anydata` aliases (9) — they are faithful to the published source, not a
  renderer defect, though they carry no information for a consumer.
- Size/token impact: +191 lines (+8.6%). 168 of the 227 added lines are constraint annotations.
  The single `ShipmentCarrier` union alone is ~17 KB of the ~90 KB file, i.e. a large share of the
  token budget in both renders; unchanged by spec v2.
- The precomputed diff at `OLD_AND_NEW_DIFFS/paypal.orders_diff.md` reports 228 added / 37 removed;
  `diff -u` on the two files gives 227 added / 36 removed. The declaration inventory (33 added,
  0 removed) and the signal table (33 → 0 unknown types, 0 version-qualified refs, 4 → 4 section
  markers) match my own measurements. The 1-line discrepancy in raw add/remove counts is a
  counting-convention difference and does not affect any conclusion.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 2219 / 2410 |
| `grep -c '^// Unknown type:' old` / `new` | 33 / 0 |
| `grep -n '^// --- ' old` / `new` | 4 markers each (README/END README/Types/Client) |
| `diff -u old new > full.diff; grep -c '^@@'` | 83 hunks |
| `grep -c '^+[^+]' full.diff` / `'^-[^-]'` | 227 added / 36 removed |
| Categorised added lines | 168 constraint, 33 typedef, 22 doc, 4 other |
| `comm -23 old_decls.txt new_decls.txt` | empty (no declaration lost) |
| `comm -13 old_decls.txt new_decls.txt` | 33 `type` declarations |
| `grep '^-[^-]' full.diff` (full listing) | 33 Unknown placeholders + 2 `type?` field lines + 1 resource-fn line |
| `grep -c '@constraint:' old` / `new` / `types.bal` | 0 / 168 / 168 |
| `diff <(grep -o '@constraint:.*' new \| sort) <(grep -o '@constraint:.*' types.bal \| sort)` | identical |
| `grep -o '@constraint:[A-Za-z]*' \| uniq -c` new vs source | 154 String / 13 Array / 1 Int, both |
| `grep -c '@display' old` / `new` / `types.bal` | 0 / 1 / 1 (`types.bal:127`) |
| Python recursive walk over `typeDefs` old→new | 2 change events, both `type` → `'type`; 0 keys removed |
| Python recursive walk over `clients` old→new | 1 event: `functions[2].parameters` 5 → 4 |
| `json: len(typeDefs)` old / new | 205 / 205 |
| `json: readme`, `description` old vs new | equal |
| `diff <(sed -n '7,131p' old) <(sed -n '7,131p' new)` | identical |
| `grep -nE ' type\??;' old` / `new` | 2 hits (1768, 2053) / 0 hits |
| `grep -c "'type" old` / `new` / `types.bal` | 5 / 7 / 5 lines |
| `git ls-remote --tags` | `v2.0.2` → `939838609e97f31dd13d999df02288794a72ca3a` |
| `git clone --depth 1 --branch v2.0.2 …` + `git describe --tags` | `v2.0.2`; `ballerina/Ballerina.toml:5 version = "2.0.2"` |
| `diff -q src/ballerina/{client,types,utils}.bal` vs bala | all `same` |
| `diff -q src/ballerina/README.md` vs `bala/docs/README.md` | `same` |
| `grep -hoE '^public …' bala/modules/paypal.orders/*.bal` | 205 `public type` + 1 `public isolated client class` |
| `comm -23 src_types.txt new_render_types` | empty |
| `comm -13 src_types.txt new_render_types` | empty |
| `comm -23 src_types.txt old_render_types` | 33 types (the placeholders) |
| `ls bala/…/2.0.2/any` | no `compiler-plugin/` |
| `find src -iname '*compiler-plugin*'` | no hits |
| `ls bala/…/any/modules` | only `paypal.orders` |
| `package.json` `export` | `["paypal.orders"]` |
| Central API `ballerinax/paypal.orders/2.0.2` | 1 module, `deprecated: null`, ballerinaVersion 2201.12.7 |
| `grep -c 'record {\|' types.bal` / old / new | 2 / 0 / 0 |
| `grep -cE '^\s+\S+ \w+ = ' types.bal` | 19 record-field defaults; 0 rendered on either side |
| `grep '^type ShipmentCarrier' \| wc -c` old / new / source | 17003 / 17003 / 17010 (`public ` prefix) |
| Brace-balance scan of `new` (lines 133–end) | final depth 0, 0 negative excursions |
| Non-ASCII (>U+2500) scan of `new` | 0 lines |
| `grep -c "Additional Values" new` | 0 |

## 10. Caveats and unverified items

- The clone is a shallow, grafted `--depth 1 --branch v2.0.2` checkout, so repository history
  before that tag was not inspected. This does not affect any claim, since all claims are about the
  tree at `v2.0.2`, which was verified byte-identical to the bala.
- I did not compile the render output with the Ballerina compiler; syntax judgements are based on
  brace balance, keyword-escaping checks and reading the source. The parameter-arity mismatch in
  §5.1 and the `anydata Additional Values` token in `old` are asserted as non-compiling on the
  basis of Ballerina grammar (identifiers cannot contain a space; `*R` included-record params are
  a single parameter), not on a compiler run.
- Branch/commit provenance of the two renderer versions (`eb5d81b3` / `412ba01e`) is taken from the
  brief; I did not inspect the `ballerina-vscode` sources myself, so the attribution of each
  behaviour change to a specific renderer commit is unverified — only the observed output
  differences are verified.
- The `examples/` and `ballerina/tests/` directories of the upstream repo were not reviewed; they
  contribute nothing to the render (the extractor consumes only the package's public API).

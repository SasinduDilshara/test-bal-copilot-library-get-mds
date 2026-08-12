# ballerinax/paypal.subscriptions 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/paypal.subscriptions` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-paypal.subscriptions |
| Tag reviewed | `v1.0.2` (commit `156cbf10b59c8cdd5551c0839da833d53e2b56d9`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/paypal.subscriptions/1.0.2` |
| Old render | `1154` lines |
| New render | `1272` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` for this library. Every declaration present in `old` is present
in `new`; nothing was removed, truncated, or made less accurate. The `+118` net lines come from four
changes, all improvements:

1. All 11 `// Unknown type:` placeholders in `old` are replaced by real, correct type definitions
   (`type Email string;`, `type PatchRequest Patch[];`, …), each with its doc comment and its
   `@constraint:*` annotation, byte-identical to the bala source.
2. 106 `@constraint:String|Int|Array` annotations are emitted on record fields (`old`: 0). The set of
   annotation strings is **exactly identical** to the 106 in the bala's `types.bal`.
3. `@display {label: "Connection Config"}` on `ConnectionConfig` is emitted (`old`: 0).
4. Two syntax defects in `old` are fixed: the unescaped keyword field `type?;` is now `'type?;`, and
   the phantom parameter `anydata Additional Values` (an open-record rest field leaking into the
   signature) is dropped from 3 resource-method signatures.

Field-level parity was verified mechanically: both renders contain **384** indented member lines, and
a sorted diff of those lines shows only the 3 client-signature changes above.

Remaining inaccuracies in `new` are all present identically in `old` (defaults dropped, `*Included`
records both flattened and repeated, closed records rendered open). They are pre-existing pipeline
behaviour, not regressions.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Total lines | 1154 | 1272 |
| `// --- section ---` markers | 4 | 4 (`README`, `END README`, `Types`, `Client`) |
| `// Unknown type:` placeholders | 11 | 0 |
| Version/module-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |
| Top-level declarations (`type`/`class`) | 80 | 91 |
| Indented member lines (record fields + client methods) | 384 | 384 |
| `@constraint:*` annotation lines | 0 | 106 |
| `@display` annotation lines | 0 | 1 |
| `@deprecated` annotation lines | 1 | 1 |
| Doc-comment (`#`) lines | 326 | 337 |
| Client resource methods | 17 | 17 |
| `init` methods | 1 | 1 |
| JSON `typeDefs` | 90 | 90 |
| JSON `clients` / `functions` / `services` / `annotations` | 1 / 0 / 0 / 0 | 1 / 0 / 0 / 0 |

Diff shape: 48 hunks, 133 lines added, 15 lines removed.

**Declarations added (11)** — all `type`, all previously `// Unknown type:`:
`AccountId`, `CountryCode`, `CurrencyCode`, `DateNoTime`, `DateTime`, `DateYearMonth`, `Email`,
`EmailAddress`, `Language`, `PatchRequest`, `Percentage`.

**Declarations removed: 0.** `comm -23 old.decls new.decls` is empty.

**Declarations modified (3)** — all client resource methods, all with the phantom
`anydata Additional Values` parameter removed:

```
- resource function get plans(... int page_size = 0, anydata Additional Values, PlansListQueries queries) returns PlanCollection|error;
+ resource function get plans(... int page_size = 0, PlansListQueries queries) returns PlanCollection|error;
- resource function get subscriptions/[string id](map<string|string[]> headers = {}, string fields = "", anydata Additional Values, SubscriptionsGetQueries queries) returns Subscription|error;
+ resource function get subscriptions/[string id](map<string|string[]> headers = {}, string fields = "", SubscriptionsGetQueries queries) returns Subscription|error;
- resource function get subscriptions/[string id]/transactions(..., anydata Additional Values, SubscriptionsTransactionsQueries queries) returns TransactionsList|error;
+ resource function get subscriptions/[string id]/transactions(..., SubscriptionsTransactionsQueries queries) returns TransactionsList|error;
```

**Field modified (1)**: `old:645` `"CREDIT"|"DEBIT"|"PREPAID"|"UNKNOWN" type?;` →
`new:718` `... 'type?;` (in flattened `CardResponseWithBillingAddress`). The source
(`types.bal:509`) uses `'type`, so `new` is correct and `old` was non-compiling.

**Annotations added (107)**: 106 `@constraint:*` + 1 `@display`.

**JSON delta**: 52 of 90 `typeDefs` objects differ; the new extractor adds `baseType` (e.g.
`"PatchRequest": {"type":"Other","baseType":"Patch[]"}`) and per-field annotation data. No `typeDefs`
entry was removed or renamed (`set(old)==set(new)` → `True`).

## 3. Correctness against library source

GitHub `v1.0.2` and the bala are byte-identical for all three `.bal` files (`diff` → IDENTICAL for
`client.bal`, `types.bal`, `utils.bal`), so upstream and bala agree; both were used.

All 11 added types verified against `modules/paypal.subscriptions/types.bal`:

| Rendered type | Source | Match |
|---|---|---|
| `type Email string;` + `@constraint:String {maxLength: 254}` | types.bal:31-32 | exact |
| `type AccountId string;` + `{maxLength: 13, minLength: 13, pattern: re \`^[2-9A-HJ-NP-Z]{13}$\`}` | types.bal:35-36 | exact |
| `type DateTime string;` + 20/64 + RFC3339 pattern | types.bal:62-63 | exact |
| `type CurrencyCode string;` + `{maxLength: 3, minLength: 3}` | types.bal:105-106 | exact |
| `type DateYearMonth string;` + `{maxLength: 7, minLength: 7, ...}` | types.bal:218-219 | exact |
| `type PatchRequest Patch[];` | types.bal:400 | exact |
| `type EmailAddress string;` + `{maxLength: 254, minLength: 3, pattern: re \`^.+@[^"\-].+$\`}` | types.bal:445-446 | exact |
| `type DateNoTime string;` + `{maxLength: 10, minLength: 10, ...}` | types.bal:541-542 | exact |
| `type Language string;` + `{maxLength: 10, minLength: 2, ...}` | types.bal:650-651 | exact |
| `type CountryCode string;` + `{maxLength: 2, minLength: 2, pattern: re \`^([A-Z]{2}\|C2)$\`}` | types.bal:683-684 | exact |
| `type Percentage string;` + `{pattern: re \`^((-?[0-9]+)\|(-?([0-9]+)?[.][0-9]+))$\`}` | types.bal:712-713 | exact |

Their doc comments in `new` are the verbatim source doc text (checked for `Email`, `CountryCode`,
`DateTime`, `PatchRequest`).

Annotations: `grep -oh '@constraint:.*'` from `types.bal` and from `new/*.bal.txt`, sorted and
diffed → **identical, 106 lines each**. No invented, dropped, or altered constraint.

`@display {label: "Connection Config"}` in `new:1015` matches `types.bal:282`.

Client: all 17 `resource isolated function`s in `client.bal` (lines 41, 52, 66, 76, 89, 100, 111,
123, 138, 149, 162, 175, 188, 201, 214, 229) plus `init` (line 31) appear in `new`, with matching
accessor, resource path (including the escaped `update\-pricing\-schemes`), payload/headers types and
return types. `init`'s `serviceUrl` default `"https://api-m.sandbox.paypal.com/v1/billing"` matches
`client.bal:31`.

README: `new` lines 8-141 vs `docs/README.md` → identical apart from one trailing blank line. The
README block in `old` and `new` is byte-identical (`diff` of lines 1-143 → no output).

## 4. Regressions

**None found.**

What was checked to conclude this:
- Sorted top-level declaration sets: `comm -23 old.decls new.decls` → empty (nothing only in `old`).
- Sorted indented-member-line sets (384 vs 384): the only differences are the 3 resource signatures,
  and in each case `new` removed a bogus parameter, keeping every real parameter, default and
  return type.
- All 16 `-` lines in `diff -u old new` are: 11 `// Unknown type:` placeholders, 1 misspelled
  `type?;` field, 3 resource signatures replaced by corrected ones, and the `---` header.
- Doc-comment lines: 326 → 337 (+11, matching the 11 new type docs); none lost.
- `@deprecated` on `SubscriptionRequestPost.auto_renewal` present in both (`old:686`, `new:762`).
- README section identical.
- JSON: 90 `typeDefs` in both, same names; client function list identical (17 methods); no parameter
  or return type removed other than `Additional Values`.

## 5. Issues in `new` (independent of `old`)

All six below are **also present in `old`** — they are pipeline behaviour, not spec-v2 defects. Listed
because they still mislead an LLM reading `new`.

1. **Included-record query parameters are rendered twice and non-compilably.** Source:
   `resource isolated function get plans(PlansListHeaders headers = {}, *PlansListQueries queries)`
   (`client.bal:41`). `new:1211` renders the record's fields flattened *and* a bare
   `PlansListQueries queries` parameter without `*`, placed after defaultable parameters — invalid
   Ballerina. Same for `subscriptions/[id]` (`client.bal:138`) and
   `subscriptions/[id]/transactions` (`client.bal:229`).
2. **Wrong defaults on those flattened query parameters.** `new:1211` shows `int page = 0` and
   `int page_size = 0`; source is `int page = 1` and `int page_size = 10` (`types.bal:746`, `751`).
   `new:1272` shows `string start_time = "", string end_time = ""` although both are **required**
   fields with no default (`types.bal:614`, `617`).
3. **Record-field default values are dropped everywhere.** `types.bal` has 32 defaulted field lines;
   `new` renders those fields as optional (`?`) with no default. Verified names dropped include
   `page`, `page_size`, `total_required`, `Prefer`, `quantity_supported`, `auto_renewal`,
   `auto_bill_outstanding`, `interval_count`, `total_cycles`, `payer_selected`, `user_action`,
   `shipping_preference`, `setup_fee_failure_action`, `payment_failure_threshold`, `inclusive`,
   `status`, `standard_entry_class_code`, `validation`, and the `ConnectionConfig` HTTP fields.
   Identical in `old` (both files have 18 `^    ... = ...;` lines, all in client signatures).
4. **Record inclusions are flattened and lose the inherited fields' docs and constraints.**
   `CardResponseWithBillingAddress` is `record {*CardResponse; *CardResponseWithBillingAddressAllOf2;}`
   (`types.bal:899-902`); `new:700-725` inlines the 8 fields but emits no `@constraint` and no doc for
   `last_digits` / `name` / `billing_address`, which do carry them on the source records. Same in `old`.
5. **Closed records rendered as open.** `OAuth2ClientCredentialsGrantConfig` (`types.bal:24`) and
   `ConnectionConfig` (`types.bal:283`) are `record {| ... |}`; both renders use `record { ... }`
   (`grep -c 'record {|'` → bala 2, old 0, new 0).
6. **`init` loses qualifiers.** Source is `public isolated function init(...)` (`client.bal:31`);
   both renders emit `function init(...)`. Likewise all 17 resource methods lose `isolated`.

Minor/cosmetic: `subscriptions/[id]/capture` returns `Transaction|error?` in source (`client.bal:214`)
and is rendered `Transaction|error|()` — semantically equivalent, valid syntax.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

The bala has a single module (`modules/paypal.subscriptions`, files `client.bal`, `types.bal`,
`utils.bal`), which is the default module; `package.json` `export` is `["paypal.subscriptions"]` and
Central lists exactly one module. So there is no submodule-only API and no shared-gap category here.

Public symbols in the default module: 90 `public type` + 1 `public isolated client class Client`.
`comm -23 bala.decls new.decls` → empty; `comm -13 bala.decls new.decls` → `Client` only (my bala
grep pattern did not catch `public isolated client class`, which is present in `new:1205`). So 91/91
public symbols are rendered.

Everything in `utils.bal` (`SimpleBasicType`, `Encoding`, `EncodingStyle`, `getDeepObjectStyleRequest`,
`getFormStyleRequest`, `getSerializedArray`, `getSerializedRecordArray`, `getEncodedUri`,
`getPathForQueryParam`) is module-private and correctly absent from both renders.

`old` renders 80/91 symbols usefully (11 degraded to `// Unknown type:` name-only lines).

## 7. Compiler plugin

The package has **no compiler plugin**. `find . -iname '*compiler-plugin*'` in the `v1.0.2` clone
returns nothing, and the bala contains no `compiler-plugin/` directory or `compiler-plugin.json`
(bala root has only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`).
Nothing plugin-implied is therefore missing from the render.

The `@constraint:*` annotations come from `ballerina/constraint`, whose validation is applied at
runtime by that module rather than by a plugin owned here; `new` now surfaces them, which is exactly
the information an LLM needs to construct valid payloads.

## 8. Other considerations

- **Version integrity**: `package.json` and `Ballerina.toml` both say `1.0.2`; Central returns
  `version: 1.0.2`, `deprecated: null`, `balaVersion: 3.0.0`, `pullCount: 30`. No drift.
- **Stability**: `1.0.2` is a stable (post-1.0) release. `distribution = "2201.12.0"`,
  `graalvmCompatible = true`.
- **Deprecation inside the API**: `SubscriptionRequestPost.auto_renewal` is `@deprecated`
  (`types.bal:242`); both renders carry the annotation. The accompanying `# Deprecated` doc line is
  rendered as a blank comment line in both.
- **Size/token impact**: +118 lines (+10.2%) for +11 real type definitions and +107 annotations.
  Good value — the 106 constraints encode max/min lengths and regex patterns that an LLM otherwise
  has to guess, and the 11 formerly-unknown types (`DateTime`, `CurrencyCode`, `CountryCode`,
  `PatchRequest`, …) are referenced pervasively by other records.
- **Doc quality**: source doc comments contain raw HTML (`<blockquote>`, `<code>`) and PayPal-relative
  links (`/docs/integration/direct/rest/currency-codes/`). Rendered verbatim — faithful, but the
  relative links are not resolvable. Present identically in the source, so not a pipeline issue.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 1154 / 1272 |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v1.0.1`, `v1.0.2` → chose `v1.0.2` (`156cbf1…`) |
| `git clone --depth 1 --branch v1.0.2 …` | OK |
| `diff src/ballerina/{client,types,utils}.bal <bala>/modules/paypal.subscriptions/` | all IDENTICAL |
| `ls <bala>/any/modules` | single module `paypal.subscriptions` (default module) |
| `cat <bala>/any/package.json` | version 1.0.2, `export: ["paypal.subscriptions"]` |
| `curl api.central.ballerina.io/…/1.0.2` | version 1.0.2, deprecated null, 1 module |
| `grep -c '^// Unknown type:'` | old 11, new 0 |
| `grep -n '^// --- '` | both: lines 7, 142, 144, and Client at old 1085 / new 1203 |
| `diff -u old new` | 48 hunks, 133 `+`, 15 `-` |
| `grep '^-' diff \| grep -v '^---'` | exactly 11 Unknown-type lines, 1 `type?;`, 3 resource signatures |
| `comm -23 old.decls new.decls` | empty (0 declarations removed) |
| `comm -13 old.decls new.decls` | 11 types added (listed §2) |
| `comm -23 bala.decls new.decls` | empty (0 public symbols missing) |
| `comm -13 bala.decls new.decls` | `Client` only (grep-pattern artefact; present at new:1205) |
| sorted member-line diff (`^    [^@#/]`) | 384 vs 384; only the 3 resource signatures differ |
| `diff <(grep -oh '@constraint:.*' types.bal\|sort) <(… new render …)` | ANNOTATIONS IDENTICAL (106 each) |
| `grep -c '@constraint:'` | bala 106, new 106, old 0 |
| `grep -c '@display'` | bala 1, new 1, old 0 |
| `grep -c '@deprecated'` | bala 1, new 1, old 1 |
| `grep -c '^\s*#'` (docs) | old 326, new 337 |
| `grep -n "'type"` | bala 2 (types.bal:509,607); new 3 (245, 673, 718, incl. flattened copy); old 2 + 1 broken `type?;` at 645 |
| `grep -n 'function ' client.bal` | 17 resource fns + init; all 17+1 in both renders |
| `grep -n -A20 'public type CardResponse record'` | types.bal:506-515, inclusion flattening confirmed at types.bal:899-902 |
| `diff <(sed -n '8,141p' new) docs/README.md` | identical except one trailing blank line |
| `diff <(sed -n '1,143p' old) <(sed -n '1,143p' new)` | README IDENTICAL |
| `grep -c 'record {\|'` | bala 2, old 0, new 0 |
| `grep -cE '^    .* = .*;$'` | bala types.bal 32, old 18, new 18 |
| `find . -iname '*compiler-plugin*'` (v1.0.2 clone) | no results |
| Python JSON compare of `typeDefs` | 90 vs 90, same name set, 52 entries enriched with `baseType`/annotations |
| Python JSON compare of `clients[0].functions` | same 17 methods; only param delta is removal of `('Additional Values', anydata)` |
| `grep -n -A20 'type PlansListQueries record' bala/new` | source defaults `page = 1`, `page_size = 10`, `total_required = false` dropped in both renders |

## 10. Caveats and unverified items

- Neither render was compiled. Syntax judgements ("non-compiling", "invalid Ballerina") are from
  reading the Ballerina grammar (unescaped keyword `type` as a field name; a required parameter
  following defaultable parameters), not from a `bal build`. The renders are digests containing
  non-`public` re-declarations and an `import` of the library itself, so they are not intended to
  compile as-is; the point is only that `new` is strictly closer to valid syntax than `old`.
- `bala.decls` was built with `grep -E '^public (type|class|const|enum|annotation)'`, which does not
  match `public isolated client class Client`. `Client` was verified present separately
  (`client.bal:24`, rendered at `new:1205`), so the 91/91 coverage figure holds.
- Field-level parity was established by comparing *sorted sets* of indented member lines, which would
  not detect a field moved between two records if the line text were identical. Given that no
  declaration was added or removed on either side and the per-hunk diff shows only additive
  annotation/doc lines, this risk is negligible but was not separately excluded.
- Constraint annotations were verified as a set (identical multisets of 106 strings), and spot-checked
  in place for the 11 new types and `ConnectionConfig`. Each of the remaining 95 was not individually
  verified as attached to the correct field.
- Central's `readme` and `summary` fields for the module come back empty in the registry API; README
  content was verified against the bala's `docs/README.md` instead.

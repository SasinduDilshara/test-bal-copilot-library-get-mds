# ballerinax/paypal.payments 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/paypal.payments` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-paypal.payments |
| Tag reviewed | `v2.0.2` (exact match found via `git ls-remote --tags`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/paypal.payments/2.0.2` |
| Old render | `716` lines (37,470 bytes) |
| New render | `750` lines (40,301 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old`. The four `// Unknown type:` placeholders in `old`
(`Email`, `AccountId`, `CurrencyCode`, `DateTime`) are replaced by real, correct type definitions,
and 30 previously-dropped annotations (29 `@constraint:*`, 1 `@display`) are now emitted on the
declarations they belong to. Every added line was verified byte-for-byte against the bala source.
No declaration, parameter, default, return type, doc string or README content was lost. The README
section, the whole `// --- Client ---` section, and the top-level JSON `readme`/`description`/
`clients` values are bit-identical between the two sides. Type coverage is 49/49 public types plus
the single `Client` class on both sides; the only thing added is that 4 of those 49 are now
*rendered* instead of stubbed.

## 2. Change inventory

Diff totals (`diff old new`): **38 lines added, 4 lines removed, 15 hunks**.

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 | −4 |
| Rendered `type ` declarations | 45 | 49 | +4 |
| `client class` | 1 | 1 | 0 |
| `resource function` in client | 7 | 7 | 0 |
| `function init` | 1 | 1 | 0 |
| `@constraint:*` annotations | 0 | 29 | +29 |
| `@display` annotations | 0 | 1 | +1 |
| `// --- section ---` markers | 4 | 4 | 0 |
| module-level `function` / `const` / `enum` / `annotation` / `service` / `listener` | 0 | 0 | 0 |
| Version-qualified refs (`mod:1.2.3:Type`) | 0 | 0 | 0 |
| `Special Agent Note` cross-package markers | 16 | 16 | 0 |

**Declarations added (4)** — all replacing a `// Unknown type:` stub, none new to the library:

- `type Email string;` (+ doc, + `@constraint:String {maxLength: 254, minLength: 3}`)
- `type AccountId string;` (+ doc, + `@constraint:String {maxLength: 13, minLength: 13, pattern: re \`^[2-9A-HJ-NP-Z]{13}$\`}`)
- `type CurrencyCode string;` (+ doc, + `@constraint:String {maxLength: 3, minLength: 3}`)
- `type DateTime string;` (+ doc, + `@constraint:String {maxLength: 64, minLength: 20, pattern: …}`)

**Declarations removed (0).** **Declarations modified (14)** — annotation lines inserted, nothing
else touched: `AuthorizationAllOf2`, `Money`, `NetworkTransactionReference`,
`SupplementaryPurchaseData`, `CaptureAllOf2`, `SellerReceivableBreakdown`, `ConnectionConfig`
(`@display`), `RelatedIds`, `RefundAllOf2`, `MerchantPayableBreakdown`, `PaymentInstruction`,
`CaptureRequestAllOf2`, `RefundRequest`, `PaymentInstruction2`.

**JSON level.** Both JSONs have the same 8 top-level keys; `readme`, `description`, `clients`,
`functions` (absent), `services` (absent), `annotations` (absent) are equal. `typeDefs` is 49 in
BOTH — so the extractor already saw all 49 types in `old`; the four were lost only at render time
(`type: "Other"` with no `baseType`). In `new` those entries gain `baseType` and `annotations`.
A recursive subset check over all 49 typeDefs (old ⊆ new, key by key, list element by list element)
returned **0 non-additive differences** — no field, doc string or list entry was changed or removed.

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/types.bal` and `ballerina/client.bal` are **byte-identical** to the
bala's `modules/paypal.payments/types.bal` and `client.bal` (`diff` → no output). So GitHub and the
bala agree and either can be cited.

- `types.bal:31-32` — `@constraint:String {maxLength: 254, minLength: 3}` / `public type Email string;`
  → matches `new` render lines 145-147 exactly, including the doc string.
- `types.bal:35-36` — `AccountId` with the 13-char `^[2-9A-HJ-NP-Z]{13}$` pattern → matches.
- `types.bal:72-73` — `DateTime` with the RFC-3339 pattern → matches character-for-character
  (regex has a `[T,t]` quirk in the source; the render reproduces it verbatim, correctly).
- `types.bal:83-84` — `CurrencyCode {maxLength: 3, minLength: 3}` → matches.
- `types.bal:106` — `@display {label: "Connection Config"}` immediately above
  `public type ConnectionConfig record {|` → matches `new`'s `@display` on `ConnectionConfig`.
- **All 29 `@constraint` annotations, exhaustively.** Extracted each annotation together with the
  declaration line it is attached to from both bala `types.bal` and the `new` render, paired them,
  and sorted: the two 29-element multisets are **identical** (`diff` → no output). Counts also
  match exactly (bala 29, new 29, old 0). No annotation was invented, dropped, reworded or
  re-attached to the wrong field. (Only the *order* differs, because the render orders types by
  reachability rather than source order — that ordering is the same in `old`.)
- **Client**, `client.bal:24-118`: the `// --- Client ---` section is byte-identical between `old`
  and `new`. All 7 resource functions and `init` match the source signatures:
  `get authorizations/[string authorizationId]`, `post …/capture`, `post …/reauthorize`,
  `post …/void`, `get captures/[string captureId]`, `post captures/…/refund`,
  `get refunds/[string refundId]`, with the same payload/headers parameter types, the same
  `headers = {}` defaults, and `init(ConnectionConfig config, string serviceUrl = "https://api-m.sandbox.paypal.com/v2/payments")`.
- **Symbol set**: the 49 `public type` names in `types.bal` and the 49 `type` names in the `new`
  render are the same set (`comm` both directions → empty). No invented symbols.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. Full `diff -u old new` read in its entirety (15 hunks, 38 `+` / 4 `-`). Every one of the 4
   removed lines is a `// Unknown type: X` placeholder replaced by a real definition of `X`.
   No other line was deleted.
2. Recursive old-⊆-new check over the full JSON (all 49 typeDefs, clients, readme, description):
   0 removals, 0 value changes.
3. Client section extracted from both files and diffed: identical.
4. README section: JSON `readme` equal on both sides; section markers 4↔4 at the same relative
   positions (lines 7/126/128 identical, `// --- Client ---` shifts 683→717 purely from the 34
   inserted lines).
5. Declaration-kind census (functions, consts, enums, annotations, services, listeners, resource
   functions, init): unchanged on every axis.
6. No new `// Unknown type:` lines, no new version-qualified type refs, no truncation
   (`new` is larger in both lines and bytes).

## 5. Issues in `new` (independent of `old`)

Two inaccuracies exist in `new` when compared to the library source. Both are also present in `old`,
so neither is a regression, but both misrepresent the library:

1. **Closed records are rendered as open records.** `types.bal:24` `OAuth2ClientCredentialsGrantConfig`
   and `types.bal:107` `ConnectionConfig` are declared `record {| … |}`; both renders emit
   `record {`. Count: 2 closed records in the bala, 0 `record {|` in either render. An LLM would
   believe extra fields are permitted where they are not.
2. **Type inclusion is flattened, and the flattening drops the included fields' docs and
   constraints.** 6 types use `*Included;` inclusion — `Capture` (`*CaptureStatus, *CaptureAllOf2,
   *ActivityTimestamps`), `Capture2`, `Refund`, `Authorization`, `Authorization2`, `CaptureRequest`.
   The render inlines the fields but emits them bare. E.g. `CaptureAllOf2.custom_id` carries
   `@constraint:String {maxLength: 127}` in `new`, yet the flattened `Capture`/`Capture2` copy of
   `custom_id` carries neither the constraint nor its doc comment. Doc-comment count inside those
   6 types: `Capture` 0, `Capture2` 0, `Refund` 0, `Authorization` 0, `Authorization2` 0,
   `CaptureRequest` 2 — identical in `old` and `new`. These 6 are precisely the client's payload and
   return types, so this is the highest-value place for the annotations to be missing.

Non-issues checked and dismissed: `public`/`isolated` qualifiers are stripped throughout the render
by convention (applies to the client class, `init`, resource functions and all types on both sides),
so `type Email string;` rather than `public type Email string;` is consistent, not a defect;
`returns Authorization2|error|()` for the source's `Authorization2|error?` is semantically
equivalent and identical in `old`. No malformed syntax, no mojibake, no truncated doc strings
(the long HTML-bearing docs for `Email`/`DateTime` round-trip intact).

## 6. Coverage gaps vs. the library

**0 gaps.** The bala exports a single module (`package.json` `export: ["paypal.payments"]`, Central
`modules` lists exactly one), so the `getDefaultModule()`-only extraction loses nothing here.

Public symbols in the default module: 49 `public type` + 1 `public isolated client class Client`.
All 50 appear in `new` (49/49 type names matched by set comparison; `Client` with all 7 resource
functions and `init`). There are no public module-level functions, constants, enums, annotations,
listeners or services to miss (`grep -E '^public (function|isolated function|const|enum|annotation|listener|service)' *.bal` → no matches).
The only non-rendered declaration is `utils.bal:26 isolated function getEncodedUri(anydata) returns string`,
which is module-private and correctly excluded. No submodule-only API.

## 7. Compiler plugin

**None.** No `compiler-plugin` directory, `compiler-plugin.json`, or `CompilerPlugin*` source exists
in the bala (`bala/.../any/` contains only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
`package.json`) or anywhere in the `v2.0.2` upstream tree (`find -iname '*compiler-plugin*'` → no
hits). Nothing plugin-derived is therefore expected in the render, and nothing is missing on that
account. Note the package *does* depend on `ballerina/constraint`, whose runtime validation is what
the newly-rendered `@constraint` annotations describe — surfacing them is a genuine semantic gain
for a consumer that must construct valid payloads.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/paypal.payments/2.0.2`: `deprecated: null`,
  `deprecateMessage: ""`, `visibility: public`, `ballerinaVersion: 2201.12.7`.
- **Stable version** (2.0.2, post-1.0). Upstream tag `v2.0.2` exists and its `ballerina/` sources
  match the published bala exactly — no drift between GitHub and Central.
- **Auto-generated connector** (`// AUTO-GENERATED FILE … by the Ballerina OpenAPI tool`), so the
  render's fidelity is bounded by the OpenAPI-generated source, not by hand-written docs.
- **Size/token cost**: +34 lines / +2,831 bytes (+7.6%) for `new`. Cheap relative to the
  information gained — 4 type definitions and 30 annotations that a payload-constructing LLM needs.
- **Doc quality**: doc strings are raw HTML lifted from the PayPal OpenAPI spec (`<blockquote>`,
  `<code>`, `<ul>`), and several contain relative links (`/api/rest/reference/currency-codes/`)
  that are not resolvable. Pre-existing and identical on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 716 / 750 |
| `wc -c old new` | 37,470 / 40,301 bytes |
| `grep -c '^// Unknown type:'` old / new | 4 / 0 |
| `grep -n '^// --- '` old / new | both 4 markers; 7,126,128,683 vs 7,126,128,717 |
| `diff old new \| grep -c '^>'` / `'^<'` | 38 added / 4 removed |
| Full `diff -u old new` | 15 hunks, all additive except the 4 placeholder→definition swaps |
| `grep -cE '^type '` old / new | 45 / 49 |
| `grep -nE '^(public )?(client )?class\|^function\|^const \|^enum \|^annotation '` old / new | `main()` (README sample) + `client class Client` in both |
| Client section extracted (old 683-716, new 717-750) and diffed | identical |
| `grep -c '@constraint:'` bala types.bal / new / old | 29 / 29 / 0 |
| `grep -n 'display' bala types.bal` | 1 hit, `types.bal:106`, above `ConnectionConfig` |
| annotation+attached-declaration pairs, bala vs new, sorted multiset | identical (29 pairs, `diff` empty) |
| `sed -n '25,40p;68,90p' bala types.bal` | `Email` (31-32), `AccountId` (35-36), `DateTime` (72-73), `CurrencyCode` (83-84) match render verbatim |
| JSON top-level key compare | same 8 keys; `readme`, `description`, `clients` equal |
| JSON `typeDefs` length old / new | 49 / 49 |
| JSON recursive old-⊆-new subset check over all typeDefs | 0 non-additive diffs |
| JSON changed typeDefs | 18, all gaining only `baseType` and/or `annotations` |
| `comm` of bala `public type` names vs new render `type` names | both directions empty → 49/49 |
| `git ls-remote --tags <repo>` | `v2.0.0`, `v2.0.1`, `v2.0.2` — exact tag exists |
| `git clone --depth 1 --branch v2.0.2` then `diff ballerina/types.bal` vs bala | IDENTICAL |
| same for `client.bal` | IDENTICAL |
| `find -iname '*compiler-plugin*'` in upstream clone | no hits |
| `ls bala/.../any/` | `bala.json dependency-graph.json docs modules package.json` — no compiler-plugin |
| `ls bala/.../modules/` | single module `paypal.payments` (client.bal, types.bal, utils.bal) |
| `package.json` export list | `["paypal.payments"]` — single default module |
| `grep -E '^public (function\|isolated function\|const\|enum\|annotation\|listener\|service)' *.bal` | no matches |
| `grep -c 'record {\|' ` bala / new render | 2 / 0 |
| inclusion map (awk over types.bal) | 6 types use `*Included;`, 16 inclusion lines total |
| doc-comment count inside the 6 flattened types, old vs new | 0,0,0,0,0,2 in both |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 0 / 0 |
| `grep -c 'Special Agent Note'` old / new | 16 / 16 |
| Central API `packages/ballerinax/paypal.payments/2.0.2` | not deprecated, public, 1 module, bal 2201.12.7 |
| `OLD_AND_NEW_DIFFS/paypal.payments_diff.md` claims (716/750/38/4/15 hunks, 4→0 unknowns, 4 added decls) | all independently reproduced and confirmed |

## 10. Caveats and unverified items

- The renders were not compiled. Syntactic validity of the emitted Ballerina was assessed by
  inspection only; the render is a lossy summary by design (qualifiers stripped, inclusions
  flattened, closed-record markers dropped) and would not compile as-is on either side.
- The two `ballerina-vscode` commits named in the brief (`eb5d81b3`, `412ba01e`) were not inspected;
  the attribution of these differences to "spec v2" is taken from the brief, not re-derived from
  renderer source. The *observed* behaviour (placeholders resolved, annotations emitted) is
  consistent with it.
- `PIN_OK` at 2.0.2 for both sides is taken from the brief. Corroborating evidence found: both JSONs
  carry the same 49 typeDefs with identical field sets, and both match the 2.0.2 bala — a version
  difference would have shown as symbol drift, and none exists.
- Whether the render pipeline *intends* to propagate constraints and docs through flattened type
  inclusions (section 5, item 2) is unknown; it is reported as an accuracy observation about the
  output, not as a confirmed renderer bug.

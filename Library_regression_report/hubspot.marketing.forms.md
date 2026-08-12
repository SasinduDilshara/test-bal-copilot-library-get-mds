# ballerinax/hubspot.marketing.forms 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.marketing.forms` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.marketing.forms |
| Tag reviewed | `v1.0.2` (commit `51b7fb0ca80ea2c4aa7f30110cd90cb9e1d75b97`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.marketing.forms/1.0.2` |
| Old render | `1043` lines |
| New render | `1044` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

A small, single-module, OpenAPI-generated HubSpot connector: 45 public types + 1 client class with
`init` + 6 resource methods. Both renders contain the same declaration set (45 `type` + 1 `client
class`, 7 client functions) and the same README block (lines 7–305 byte-identical). The renders
differ in 9 hunks (+11 / −10 lines). Every difference is a `new` improvement:

1. 20 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.marketing.forms:1.0.2:EmailField`, …) are replaced with the real source
   spelling (`int:Signed32`, `EmailField`) — 0 remain in `new`.
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` is now emitted; it
   exists in the source and was silently dropped by `old`.
3. Two synthetic, non-compiling client parameters named `anydata Additional Values` are removed.

No declaration, parameter, default, return type, doc string or README content was lost. `// Unknown
type:` count is 0 on both sides (this library has no error/object/`Other` type defs, so spec v2's
main win does not apply here).

## 2. Change inventory

Line counts: `old` 1043, `new` 1044 (`wc -l`). Unified diff: 9 hunks, 11 added / 10 removed lines.

| Kind | old | new | Δ |
|---|---|---|---|
| `type` declarations (top-level) | 45 | 45 | 0 |
| ...of which rendered as `record {` | 44 | 44 | 0 |
| ...of which rendered as union alias | 1 | 1 | 0 |
| `client class` | 1 | 1 | 0 |
| client functions (`init` + resources) | 7 | 7 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 20 | 0 | −20 |
| Rendered `@display` annotations | 0 | 1 | +1 |
| `Additional Values` pseudo-params | 2 | 0 | −2 |

**Declarations added: 0. Declarations removed: 0.** (JSON `typeDefs` name sets are equal — set
difference empty in both directions; `clients[0].functions` length 7 on both sides.)

Modified declarations — 7 typeDefs + 2 client functions:

| Declaration | Change in `new` |
|---|---|
| `PhoneFieldValidation` | `minAllowedDigits`, `maxAllowedDigits`: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` |
| `NumberFieldValidation` | same two fields, same fix |
| `EnumeratedFieldOption` | `displayOrder`: same fix |
| `LegalConsentCheckbox` | `subscriptionTypeId`: same fix |
| `GetMarketingV3FormsGetPageQueries` | `'limit`: same fix |
| `FieldGroupFields` | 13 union members lose the `ballerinax/hubspot.marketing.forms:1.0.2:` prefix |
| `ConnectionConfig` | gains `@display {label: "Connection Config"}` (JSON gains an `annotations` key) |
| `Client` resource `get [string formId]` | drops `anydata Additional Values` param |
| `Client` resource `get .` | drops `anydata Additional Values` param |

The JSON diff confirms these are the only model-level changes: `name`, `description`, `readme`,
`functions`, `services`, `annotations` are byte-equal; `typeDefs` differ in exactly the 7 entries
above; `clients[0].functions` differ only in the `parameters` array of the two `get` resources.

## 3. Correctness against library source

Upstream `v1.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's
`modules/hubspot.marketing.forms/*.bal` (`diff -q` → identical for all three). So GitHub and bala
agree; every check below is valid against both.

- `int:Signed32` — source `types.bal:205, 315, 316, 415, 494, 495, 531` all write `int:Signed32`.
  `new` matches exactly; `old`'s `ballerina/lang.int:0.0.0:Signed32` is not valid Ballerina and does
  not appear in the source. ✔ `new` correct.
- `FieldGroupFields` — source `types.bal:539`:
  `public type FieldGroupFields EmailField|PhoneField|MobilePhoneField|SingleLineTextField|MultiLineTextField|NumberField|SingleCheckboxField|MultipleCheckboxesField|DropdownField|RadioField|DatepickerField|FileField|PaymentLinkRadioField;`
  `new` render line 717 is character-for-character the same union (minus `public`). ✔
- `@display {label: "Connection Config"}` — source `types.bal:324`, immediately above
  `public type ConnectionConfig record {|`. It is the only annotation in the entire package
  (`grep -nE '^\s*@[a-zA-Z]' *.bal` → 1 hit). `new` render line 931 reproduces it verbatim. ✔
- `Additional Values` — no such identifier exists anywhere in the source. It was a synthetic entry
  in `old`'s JSON (`{"name":"Additional Values","description":"Capture key value pairs","type":
  {"name":"anydata"}}`), derived from the open-record rest field of the included-record query
  parameters. As rendered (`anydata Additional Values`) it was not parseable Ballerina. Removing it
  is correct. ✔
- Client surface — source `client.bal` declares `init` + `get [string formId]`, `put [string
  formId]`, `delete [string formId]`, `patch [string formId]`, `get .`, `post .`. All 7 appear in
  both renders with matching payload types (`HubSpotFormDefinition`,
  `HubSpotFormDefinitionPatchRequest`, `FormDefinitionCreateRequestBase`) and returns
  (`FormDefinitionBase|error`, `json|error`, `CollectionResponseFormDefinitionBaseForwardPaging|error`).
  `init` default `serviceUrl = "https://api.hubapi.com/marketing/v3/forms"` matches `client.bal:30`. ✔
- Type-name coverage — the 45 `public type` names in `types.bal` and the 45 `typeDefs` names in the
  `new` JSON are the same set (both set differences empty). ✔

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full `diff -u old new` (38 lines of output, 9 hunks) reviewed line by line; every removed line has
  a corresponding, strictly more accurate added line, except the two `Additional Values` removals
  which delete content that does not exist in the library.
- JSON-level set comparison of `typeDefs` names (equal), client function count (7 = 7), and per-field
  comparison of all 45 typeDefs (only the 7 listed in §2 differ, all in the improving direction).
- README block `sed -n '7,305p'` diff → identical; JSON `readme` key equal.
- No parameter, default value, return type, doc comment, or section marker present in `old` is
  absent from `new`. `grep -c '?;'` and the per-declaration field lists are unchanged apart from the
  type-spelling fixes.
- Nothing in `new` is truncated relative to `old`; `new` is 1 line longer (the annotation), and its
  two shortened client signatures are shorter only because a bogus parameter was dropped.

## 5. Issues in `new` (independent of `old`)

These are all inherited fidelity gaps of the shared pipeline — present identically in `old`, so not
regressions — but they are inaccuracies a consumer of the `new` render would hit:

1. **Record field default values are dropped.** Source has 12 fields with initializers
   (`types.bal:310, 329, 331, 333, 335, 337, 343, 345, 353, 359, 361, 364`, e.g.
   `http:HttpVersion httpVersion = http:HTTP_2_0;`, `decimal timeout = 30;`,
   `boolean laxDataBinding = true;`). The render turns every one into an optional field
   (`http:HttpVersion httpVersion?;`) — 0 default-valued fields survive. An LLM cannot learn the
   defaults, and required-with-default is misrepresented as optional.
2. **Closed records are rendered as open.** `OAuth2RefreshTokenGrantConfig` (`types.bal:307`),
   `ConnectionConfig` (`:325`) and `ApiKeysConfig` (`:635`) are `record {| … |}`; the render emits
   `record {` for all three (`grep -c 'record {|'` → 0).
3. **Included-record parameters are both flattened and duplicated.** Source:
   `resource isolated function get [string formId](map<string|string[]> headers = {}, *GetMarketingV3FormsFormIdGetByIdQueries queries)`.
   The render emits the record's fields as individual params **and** a trailing
   `GetMarketingV3FormsFormIdGetByIdQueries queries` with no `*` and no default, placed after
   defaulted params — a signature that neither matches the source nor compiles. Same for
   `get .` (new render lines 1023 and 1039).
4. **Root resource path `.` is lost.** `resource isolated function get .(…)` and `post .(…)` render
   as `resource function get (…)` / `resource function post (…)` (new render lines 1039, 1043),
   which is not valid resource-path syntax and hides the root path from the reader.
5. **Multi-line doc comment loses its `#` continuation.** New render line 970 —
   `and absent fields are handled as `nilable` types. Enabled by default.` — sits at column 0 inside
   the `ConnectionConfig` body as bare text (source `types.bal:363` is a `#` continuation line).
6. **Type aliases are expanded inline.** `FormDefinitionBase`, `FormDefinitionCreateRequestBase` and
   `CollectionResponseFormDefinitionBaseForwardPagingResults` are `public type X HubSpotFormDefinition…;`
   aliases in source (`types.bal:29, 367, 369`) but render as full duplicated record bodies
   (new render lines 837, 981, 870). Structurally faithful, but it triples the record text and hides
   the aliasing.
7. **`public` / `isolated` qualifiers dropped** on the class and all methods (cosmetic; consistent
   across the corpus).

Items 1–7 are identical in `old`; I verified this by confirming the unified diff contains no hunk
touching any of the cited lines other than the `@display` insertion.

## 6. Coverage gaps vs. the library

**None.** The bala's `modules/` directory contains exactly one module,
`hubspot.marketing.forms` (= the default module); `package.json` `"export": ["hubspot.marketing.forms"]`
and Central metadata list a single module. So there is no submodule-only API and no shared
submodule gap.

- All 45 `public type` declarations appear in both renders (set difference empty both ways).
- The single `public isolated client class Client` and all 7 of its functions appear in both.
- `utils.bal` declares `SimpleBasicType`, `Encoding`, `EncodingStyle` (lines 23, 26, 37) — all
  module-private, correctly excluded from both renders.
- No public module-level functions, constants, listeners, services or annotation declarations exist
  in the package, and both renders correctly show `functions: 0`, `services: 0`, `annotations: 0`.

## 7. Compiler plugin

The package ships **no compiler plugin**: no `compiler-plugin/` directory in the upstream tree
(`find . -iname '*compiler-plugin*'` → no hits) and no `compiler-plugin/compiler-plugin.json` in the
bala (`any/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json`). Nothing plugin-derived is therefore expected in, or missing from, the render.

## 8. Other considerations

- Version is stable 1.0.2; Central reports `deprecated: null`, empty `deprecateMessage`, pull count
  34, built with Ballerina `2201.12.2`. No deprecation warnings needed.
- Fully auto-generated by the Ballerina OpenAPI tool ("AUTO-GENERATED FILE. DO NOT MODIFY."), so doc
  strings come from the HubSpot OpenAPI spec; quality is good and both renders preserve them.
- Size is modest (~1.04k lines, JSON 117 KB in `new` vs 118 KB in `old`); `new` is marginally
  cheaper in tokens because the long qualified type names are gone (`FieldGroupFields` alone shrank
  from ~700 to ~250 characters on one line).
- The `new` render's removal of `anydata Additional Values` also removes the only signal that the
  query records are open (`record { … }` with implicit `anydata` rest field). That signal was
  conveyed in a malformed, misleading way, so its loss is not material, but it is a small
  information delta worth noting.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/…bal.txt new/…bal.txt` | 1043 / 1044 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | 4 markers each; README 7–305, Types 307, Client 1015 (old) / 1016 (new) |
| `diff -u old new` | 9 hunks, +11 / −10, 38 output lines |
| `grep -oE '[a-z]+/[A-Za-z0-9_.]+:[0-9]+\.[0-9]+\.[0-9]+:[A-Za-z0-9_]+' \| wc -l` | old 20, new 0 |
| `grep -c 'Additional Values'` | old 2, new 0 |
| `grep -n '^@'` renders | old: none; new: line 931 `@display {label: "Connection Config"}` |
| `diff <(sed -n '7,305p' old) <(sed -n '7,305p' new)` | identical (README preserved) |
| Python JSON compare: `name/description/readme/functions/services/annotations` | equal on both sides |
| Python JSON compare: `typeDefs` count / name sets | 45 / 45, set difference empty both ways |
| Python JSON compare: changed typeDefs | 7 — `PhoneFieldValidation`, `NumberFieldValidation`, `EnumeratedFieldOption`, `FieldGroupFields`, `LegalConsentCheckbox`, `GetMarketingV3FormsGetPageQueries`, `ConnectionConfig` |
| Python JSON compare: `clients[0].functions` | 7 / 7; only 2 differ, only in `parameters` (removal of `Additional Values`) |
| `git ls-remote --tags <repo>` | `v0.1.0, v1.0.0, v1.0.1, v1.0.2` → exact tag `v1.0.2` |
| `git clone --depth 1 --branch v1.0.2` + `git log -1` | `51b7fb0ca80ea2c4aa7f30110cd90cb9e1d75b97`, 2026-06-26 |
| `diff -q src/ballerina/{client,types,utils}.bal bala/modules/…/` | identical ×3 |
| `grep -nE '^public ' bala/modules/*.bal` | 46 public decls = 45 types + 1 client class |
| `grep -nE '^public type … record \{\|'` `types.bal` | 3 closed records (307, 325, 635); `grep -c 'record {|'` in new render → 0 |
| `grep -cE '^\s+[A-Za-z0-9:_<>\|\[\]]+ [A-Za-z0-9_']+ = ' types.bal` | 12 default-valued fields; 0 rendered with defaults |
| `grep -nE '^    resource function (get\|post) \(' new` | lines 1039, 1043 — missing `.` resource path |
| `grep -n '^and absent fields' old new` | old:969, new:970 — broken doc continuation, both sides |
| `types.bal:324` | `@display {label: "Connection Config"}` — confirms new render's addition |
| `types.bal:539` | `FieldGroupFields` union — matches new render line 717 exactly |
| `ls bala/1.0.2/any/modules` | single module `hubspot.marketing.forms` |
| `find src -iname '*compiler-plugin*'` | no hits |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerinax/hubspot.marketing.forms/1.0.2` | 1 module, `deprecated: null`, pullCount 34, ballerinaVersion 2201.12.2 |

## 10. Caveats and unverified items

- Neither render was compiled. Statements about "non-compiling" syntax (§5 items 3–5, and the
  `anydata Additional Values` line in `old`) are based on reading the Ballerina grammar, not on a
  `bal build` run.
- I did not re-run the two-stage pipeline; the audit compares the supplied JSON/render artefacts
  against the bala and upstream source. The claim that the only causal difference is the
  extractor/renderer change is taken from the brief and is consistent with both renders carrying
  identical declaration sets for the same pinned version.
- `dependency-graph.json` and the bala's `docs/README.md` were not diffed against the rendered README
  beyond confirming the rendered README is identical between `old` and `new`.

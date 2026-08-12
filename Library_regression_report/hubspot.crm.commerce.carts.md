# ballerinax/hubspot.crm.commerce.carts 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.commerce.carts` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.commerce.carts |
| Tag reviewed | `v2.0.2` (exact tag, commit `39da7cdd44349ea2d69c6173be16675f2f6add0b`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.commerce.carts/2.0.2` |
| Old render | `781` lines |
| New render | `782` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. The declaration set is byte-identical in membership between the two
renders: 41 type definitions, 1 client class, `init` + 11 resource methods on both sides, 4 section
markers on both sides, and 0 `// Unknown type:` placeholders on both sides. The only changes are
three spec-v2 improvements:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.commerce.carts:2.0.2:ValueWithTimestamp`, …) are now emitted as plain
   `int:Signed32` / `ValueWithTimestamp`.
2. The synthetic, non-compiling parameter `anydata Additional Values` is gone from 4 resource
   signatures.
3. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` — real in the
   library source (`types.bal:239`) and silently dropped by `old` — is now emitted.

No declaration, parameter, doc line, README byte, or return type is lost in `new`. Zero regressions.
Both renders share a set of pre-existing inaccuracies (dropped record-field defaults, fabricated
resource-parameter defaults, duplicated flattened-query parameters, closed records rendered open,
dropped `public`/`isolated` qualifiers, one broken doc-comment line); these are listed in §5 because
the brief asks for issues in `new` regardless of `old`, but none of them are new.

## 2. Change inventory

Line counts: old **781**, new **782**. Diff: **15** lines removed, **16** added, **15** hunks
(`diff -u` on the two `.bal.txt` files).

| Kind | old | new | Δ |
|---|---|---|---|
| `type` definitions (top-level, `^type `) | 41 | 41 | 0 |
| Client classes | 1 | 1 | 0 |
| Client `init` | 1 | 1 | 0 |
| `resource function` methods | 11 | 11 | 0 |
| `service` / `listener` / module-level `function` / `const` / `enum` / `annotation` decls | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 11 | 0 | −11 |
| Annotation lines (`@display`) | 0 | 1 | +1 |
| Synthetic `anydata Additional Values` params | 4 | 0 | −4 |

`diff old_types.txt new_types.txt` over the 41 sorted type names: **identical** (no additions, no
removals, no renames).

Breakdown of the 15 removed / 16 added lines:

- **7** lines: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`
  (fields `AssociationSpec.associationTypeId`, `ValueWithTimestamp.updatedByUserId`,
  `BatchResponseSimplePublicObject.numErrors`, `GetCrmV3ObjectsCartsCartIdQueries.'limit`,
  `CollectionResponseWithTotalSimplePublicObjectForwardPaging.total`,
  `PublicObjectSearchRequest.'limit`, `BatchResponseSimplePublicUpsertObject.numErrors`).
- **4** lines: inline rest-field records
  `record {|ballerinax/hubspot.crm.commerce.carts:2.0.2:ValueWithTimestamp[]...;|}` →
  `record {|ValueWithTimestamp[]...;|}` (×3) and
  `record {|…:CollectionResponseAssociatedId...;|}` → `record {|CollectionResponseAssociatedId...;|}` (×1).
- **4** lines: resource signatures for `post carts/batch/read`, `get carts/[string cartId]`,
  `patch carts/[string cartId]`, `get carts` lose `anydata Additional Values`.
- **+1** net line: `@display {label: "Connection Config"}` inserted above `type ConnectionConfig`
  (this is the only hunk with `+1 / −0`).

JSON side: both JSONs have the same top-level keys, `typeDefs` 41/41, `clients` 1/1, `functions`
0/0, `services` []/[], identical `readme` (9,271 chars, byte-equal) and identical `description`. The
only new JSON key path is `/typeDefs[]/annotations` (with `name` and `value`), populated for exactly
one type: `ConnectionConfig` → `{"name":"display","value":"{label: \"Connection Config\"}"}`.
`"Additional Values"` no longer appears anywhere in the new JSON. New JSON is 85,989 bytes vs
87,115 old (−1.3%).

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/{client,types,utils}.bal` are **byte-identical** to the bala's
`modules/hubspot.crm.commerce.carts/{client,types,utils}.bal` (`diff -q`, all three IDENTICAL), so
GitHub and the bala agree and either can be cited.

Verified for the three changes `new` makes:

- **`int:Signed32`** — `types.bal:197` `int:Signed32 'limit = 10;`, `types.bal` field
  `associationTypeId` etc. all use the `int:Signed32` lang-lib subtype. `int:Signed32` is the
  correct Ballerina spelling; `ballerina/lang.int:0.0.0:Signed32` is not valid syntax. New is right.
- **`ValueWithTimestamp` / `CollectionResponseAssociatedId` unqualified** — both are types defined in
  this same module (`types.bal`, present in the 41-name public type list), so an unqualified
  reference from inside the module is correct; the `org/name:version:` prefix was never valid
  Ballerina. New is right.
- **`@display {label: "Connection Config"}`** — present verbatim at
  `.../modules/hubspot.crm.commerce.carts/types.bal:239`, immediately above
  `public type ConnectionConfig record {|` at line 240. New reproduces it exactly, including label
  text. This is the only annotation in the whole module (`grep -n '@' types.bal` returns one hit),
  so `new` captures 1/1 annotations and `old` captured 0/1.
- **`anydata Additional Values` removal** — the four affected resources are the four that take an
  included query record (`client.bal:47, 66, 97, 167`, all `*<X>Queries queries`). Those query
  records (`types.bal:183, 189, 283, 460`) are open records, and the old extractor materialised
  their `anydata` rest field as a parameter literally named `Additional Values` — an identifier
  containing a space, which cannot compile. Removing it loses no real API: no resource in
  `client.bal` declares such a parameter. New is right.

Client surface cross-check against `client.bal`: `init` (line 31) plus 11 `resource isolated
function` declarations at lines 47, 66, 82, 97, 115, 132, 149, 167, 183, 200, 217 — all 11 appear in
both renders with matching accessor, path, payload type and return union (e.g. `post carts/search`
→ `CollectionResponseWithTotalSimplePublicObjectForwardPaging|error`, matching `client.bal:217`).
`init` default `serviceUrl = "https://api.hubapi.com/crm/v3/objects"` matches `client.bal:31`.

Type coverage: `comm` of the 41 `^public type` names in `types.bal` against the 41 `^type` names in
`new` — empty in both directions. Every public type is rendered; no invented types.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Sorted declaration-name sets (`^type X`) for old and new: `diff` → identical, 41 each.
- Resource method count (`grep -c '^    resource function'`): 11 in new; the client block in the
  unified diff shows only 4 modified lines, all of which are `anydata Additional Values` removals
  with every other token on the line unchanged (payload types, header params, defaults, `queries`
  param, return unions all preserved character-for-character).
- README block: `old["readme"] == new["readme"]` → `True`, both 9,271 chars; section markers
  `// --- README ---`, `// --- END README ---`, `// --- Types ---`, `// --- Client ---` present in
  both (only the `// --- Client ---` marker shifts from line 733 to 734 because of the added
  annotation line).
- `// Unknown type:` count: 0 in old, 0 in new — nothing degraded.
- Doc comments: no `# …` line appears in the removed side of the diff; all 15 removals are the three
  categories enumerated in §2.
- Return types and default values on resource signatures: unchanged on all 4 modified lines.
- The one thing `old` had and `new` does not — `anydata Additional Values` — is not real library API
  and was syntactically invalid (see §3), so its loss is not a regression.

## 5. Issues in `new` (independent of `old`)

All six below are present in **both** renders (verified by their absence from the unified diff), so
none is caused by spec v2. They are reported because they mislead a consuming LLM.

1. **Record-field default values are dropped.** `types.bal` declares 13 fields with defaults; the
   rendered Types section contains 0 `field = value` forms. Each defaulted field is instead rendered
   as optional. Examples: `ConnectionConfig.httpVersion = http:HTTP_2_0` (`types.bal:244`) renders as
   `http:HttpVersion httpVersion?`; `GetCrmV3ObjectsCartsQueries.'limit = 10` (`types.bal:197`)
   renders as `int:Signed32 'limit?` (new render line 511). An LLM reading this cannot know the page
   size default is 10, and will believe required-with-default fields are omissible.
2. **Fabricated defaults on flattened resource parameters.** New render line 769:
   `get carts(… int:Signed32 limit = 0, string after = "", string[] associations = [], string[] properties = [] …)`.
   In the source these are fields of `GetCrmV3ObjectsCartsQueries` — `'limit` defaults to **10**, not
   0, and `after`/`associations`/`properties` are optional with **no** default at all. The rendered
   `limit = 0` is factually wrong against `types.bal:197`.
3. **Duplicated / non-compiling parameter lists.** The same four resources list the flattened query
   fields *and* a `queries` parameter of the query-record type, with the un-defaulted `queries`
   parameter appearing *after* defaulted parameters — invalid Ballerina, and it invites an LLM to
   pass the same value twice. Source signature is simply
   `resource isolated function get carts(map<string|string[]> headers = {}, *GetCrmV3ObjectsCartsQueries queries)`
   (`client.bal:167`).
4. **Closed records rendered as open.** `types.bal` has 3 top-level `record {|…|}` declarations
   (`ConnectionConfig`, `OAuth2RefreshTokenGrantConfig`, `ApiKeysConfig` region); the render has 0
   `type X record {|`. All are emitted as `record {`.
5. **Qualifiers dropped.** `public isolated client class Client` (`client.bal:23`) renders as
   `client class Client`; `resource isolated function` renders as `resource function`; all 41
   `public type` render as bare `type`. As written, the render's symbols would not be visible outside
   the module.
6. **One broken doc-comment line.** New render line 590 is
   `and absent fields are handled as \`nilable\` types. Enabled by default` with no leading `#` — the
   continuation of the two-line doc for `ConnectionConfig.laxDataBinding` (`types.bal:277-278`). It
   sits inside a record body as a bare statement and does not parse. Present identically in `old`.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module (`modules/hubspot.crm.commerce.carts` = the default
module, containing only `client.bal`, `types.bal`, `utils.bal`), so the
`pkg.getDefaultModule()`-only extraction limitation described in the brief does not bite here — there
are no submodules.

Public symbols in the default module:

| Symbol group | count in bala | in `new` render | in `old` render |
|---|---|---|---|
| `public type` | 41 | 41 | 41 |
| `public isolated client class Client` | 1 | 1 | 1 |
| Client methods (`init` + resources) | 12 | 12 | 12 |

`utils.bal` contains 6 functions, all module-private (`isolated function …`, no `public`), so their
absence from the render is correct, not a gap.

## 7. Compiler plugin

**None.** `find` over the `v2.0.2` clone for `*compiler-plugin*` / `CompilerPlugin.toml` returns
nothing, and the bala root contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json` — no `compiler-plugin/` directory and no `compiler-plugin.json`. Nothing plugin-derived
is expected to surface in the render, and nothing is missing on that account.

## 8. Other considerations

- **Package status.** `Ballerina.toml` pins `distribution = "2201.12.0"`. The README carries a
  vendor stability warning ("This package may be changed in the future … currently under development
  … unstable API"), reproduced verbatim in both renders. Package version 2.0.2 itself is stable
  (≥1.0.0); no deprecation markers found in the bala or `Ballerina.toml`.
- **Size / tokens.** Renders are small (781/782 lines); the JSON shrank 1.3% (87,115 → 85,989 bytes)
  because 11 fully-qualified type strings collapsed to short names and 4 synthetic params vanished.
  Net effect on an LLM prompt is slightly fewer tokens for strictly more information (the annotation).
- **Import header.** Both renders emit `import ballerinax/hubspot.crm.commerce.carts;` at the top
  while referring to types unqualified inside the body — cosmetically inconsistent, unchanged between
  sides.
- **Cross-package refs.** `http:*` types in `ConnectionConfig` carry `// Special Agent Note: … FROM
  ballerina/http package` trailer comments in both renders; those are preserved identically.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 781 / 782 |
| 2 | `grep -c '^// Unknown type:'` on both renders | 0 / 0 |
| 3 | `diff -u old new \| grep -c '^-[^-]'` / `'^+[^+]'` | 15 removed / 16 added |
| 4 | `diff -u … \| grep '^-' \| grep -c 'ballerina/lang.int:0.0.0:Signed32'` | 7 |
| 5 | `diff -u … \| grep '^-' \| grep -c 'ballerinax/hubspot.crm.commerce.carts:2.0.2:'` | 4 |
| 6 | `diff -u … \| grep '^-' \| grep -c 'anydata Additional Values'` | 4 |
| 7 | `grep -nE '[a-z]+/[a-zA-Z._]+:[0-9]' new/*.bal.txt` | no matches (0 qualified refs remain) |
| 8 | `grep -n 'Additional Values' new/*.bal.txt` | no matches |
| 9 | `grep -n '^// --- ' old / new` | old: 7, 208, 210, 733; new: 7, 208, 210, 734 (4 markers each) |
| 10 | `grep -oE '^type [A-Za-z0-9_]+' \| sort` old vs new, then `diff` | 41 vs 41, identical |
| 11 | `comm` of bala `^public type` names (41) vs new render type names (41) | empty both directions |
| 12 | `git ls-remote --tags <repo>` | `v1.0.0, v2.0.0, v2.0.1, v2.0.2`; `v2.0.2^{}` = `39da7cdd…` |
| 13 | `git clone --depth 1 --branch v2.0.2` then `diff -q src/ballerina/{client,types,utils}.bal` vs bala | all three IDENTICAL |
| 14 | `find src -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no output |
| 15 | `ls <bala>/any` | `bala.json dependency-graph.json docs modules package.json` (no compiler-plugin) |
| 16 | `ls <bala>/any/modules` | single module `hubspot.crm.commerce.carts` (no submodules) |
| 17 | `grep -nE '^\s*(resource\|remote\|public)' client.bal` | `public isolated client class Client` (23), `init` (31), 11 `resource isolated function` (47, 66, 82, 97, 115, 132, 149, 167, 183, 200, 217) |
| 18 | `grep -c '^    resource function' new/*.bal.txt` | 11 |
| 19 | `grep -n '@' types.bal` | one hit: line 239 `@display {label: "Connection Config"}` |
| 20 | new render lines 548-551 | `@display {label: "Connection Config"}` above `type ConnectionConfig record {` |
| 21 | JSON key-path diff old vs new | only new: `/typeDefs[]/annotations`, `…/name`, `…/value` |
| 22 | JSON `typeDefs` / `clients` / `functions` / `services` counts | 41/41, 1/1, 0/0, []/[] |
| 23 | JSON `readme` equality and length | equal, 9,271 chars both |
| 24 | JSON `"Additional Values" in json.dumps(new)` | `False` |
| 25 | JSON old client param dump | `Additional Values: anydata` present on the 4 query-record resources |
| 26 | `grep -cE '^public type … record \{\|' types.bal` vs `^type … record \{\|` in new render | 3 vs 0 |
| 27 | `grep -cE '^\s+\S+ \S+ = ' types.bal` vs same over render lines 210-733 | 13 vs 0 |
| 28 | `types.bal:197` | `int:Signed32 'limit = 10;` vs render line 769 `int:Signed32 limit = 0` |
| 29 | `awk` scan of render lines 210-734 for non-indented, non-`#`, non-`type`, non-`}` lines | 1 hit: line 590 `and absent fields are handled as \`nilable\` types. Enabled by default` |
| 30 | `grep -E '^(public \|isolated )' new/*.bal.txt` | 1 hit, inside the README code sample only |
| 31 | Precomputed `OLD_AND_NEW_DIFFS/hubspot.crm.commerce.carts_diff.md` | 781/782 lines, +16/−15, 15 hunks, 11→0 qualified refs, 0 declarations added/removed — all figures independently reproduced above |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that specific rendered lines "do not parse"
  (`anydata Additional Values`, the un-`#`-prefixed doc line, `queries` after defaulted params) rest
  on the Ballerina grammar, not on a compiler run.
- The two `ballerina-vscode` source trees (`old` `eb5d81b3`, `new` `412ba01e`) were not inspected; the
  attribution of each change to spec v2 is inferred from the render/JSON deltas and from the brief's
  stated behaviour, and matches it exactly (qualified refs eliminated, annotations added).
- I did not re-query the Ballerina Central registry API; version pinning was confirmed instead from
  the bala path (`.../2.0.2`) and `Ballerina.toml` (`version = "2.0.2"`), and from the exact upstream
  tag `v2.0.2` whose Ballerina sources are byte-identical to the bala's.
- Correctness of the render's `http:*` field types was checked against this package's `types.bal`
  only; the `ballerina/http` package definitions themselves were not opened.

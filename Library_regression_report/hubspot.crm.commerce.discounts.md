# ballerinax/hubspot.crm.commerce.discounts 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.commerce.discounts` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.commerce.discounts |
| Tag reviewed | `v2.0.2` |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.commerce.discounts/2.0.2` |
| Old render | `763` lines |
| New render | `764` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module OpenAPI-generated HubSpot connector (41 public types, 1 client, 12 resource
methods, no public module-level functions). The `old` → `new` delta is 15 hunks, all of them
strictly corrective:

- 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
  `ballerinax/hubspot.crm.commerce.discounts:2.0.2:ValueWithTimestamp`, …) are replaced with the
  plain, source-accurate names (`int:Signed32`, `ValueWithTimestamp`). Verified against the bala
  source — the new spellings are byte-identical to what the library declares.
- The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` is now emitted; `old`
  dropped it. It is the only annotation in the whole module, and it is now the only one rendered.
- Four synthetic `anydata Additional Values` parameters — which were **non-compiling Ballerina**
  (an identifier containing a space) and which correspond to no symbol in the library source — are
  removed from the four resource methods that take an included-record `*…Queries` parameter.

Nothing is removed, truncated, or made less accurate. Declaration counts, record-field counts,
README content and section structure are identical on both sides. No regressions found.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Render lines | 763 | 764 |
| `// Unknown type:` placeholders | 0 | 0 |
| `// --- section ---` markers | 4 | 4 (README @7, END README @178, Types @180, Client @715/716) |
| JSON `typeDefs` | 41 | 41 |
| JSON `clients` | 1 | 1 |
| Client resource/init functions | 12 | 12 |
| JSON `functions` / `services` / `annotations` (top-level) | 0 / 0 / 0 | 0 / 0 / 0 |
| Total record fields across all typeDefs | 169 | 169 |
| Total client function parameters | 45 | 41 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 11 | 0 |
| `@display` annotations emitted | 0 | 1 |
| `anydata Additional Values` params | 4 | 0 |

**Declarations added: 0. Declarations removed: 0.** Type-name sets are identical
(`diff old_types.txt new_types.txt` → empty) and both equal the 41 `public type` names in the bala.

Modified, grouped by kind:

- **Type (record field type refs) — 11 fields across 9 records.**
  `AssociationSpec.associationTypeId`, `ValueWithTimestamp.updatedByUserId`,
  `GetCrmV3ObjectsDiscountsQueries.'limit`, `BatchResponseSimplePublicObjectWithErrors.numErrors`,
  `BatchResponseSimplePublicUpsertObjectWithErrors.numErrors`,
  `CollectionResponseWithTotalSimplePublicObjectForwardPaging.total`,
  `PublicObjectSearchRequest.'limit` (7 × `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`);
  `SimplePublicObject.propertiesWithHistory`, `SimplePublicUpsertObject.propertiesWithHistory`,
  `SimplePublicObjectWithAssociations.propertiesWithHistory`,
  `SimplePublicObjectWithAssociations.associations`
  (4 × `record {|ballerinax/hubspot.crm.commerce.discounts:2.0.2:X…;|}` → `record {|X…;|}`).
- **Type (annotation) — 1.** `ConnectionConfig` gains `@display {label: "Connection Config"}`
  (new render line 529).
- **Client method signatures — 4.** `post batch/read`, `get [string discountId]`,
  `patch [string discountId]`, `get .` each lose the bogus `anydata Additional Values` parameter.

The precomputed diff at `OLD_AND_NEW_DIFFS/hubspot.crm.commerce.discounts_diff.md` (763/764 lines,
16 added, 15 removed, 15 hunks, 11 → 0 qualified refs) was re-derived independently with
`diff -u` and matches exactly.

## 3. Correctness against library source

Upstream `v2.0.2` was cloned and its `ballerina/{client,types,utils}.bal` are **byte-identical** to
the bala's `modules/hubspot.crm.commerce.discounts/*.bal` (`diff -q` → SAME for all three), so the
GitHub tag and the bala agree; either can be cited.

Every change in `new` is confirmed against that source:

| New render | Source (bala `types.bal`) | Verdict |
|---|---|---|
| `int:Signed32 associationTypeId;` | line 366 `int:Signed32 associationTypeId;` | exact |
| `int:Signed32 updatedByUserId?;` | line 179 `int:Signed32 updatedByUserId?;` | exact |
| `int:Signed32 'limit?;` (GetCrmV3ObjectsDiscountsQueries) | line 103 `int:Signed32 'limit = 10;` | type exact (default lost — see §5) |
| `int:Signed32 numErrors?;` ×2 | lines 127, 330 | exact |
| `int:Signed32 total;` | line 214 | exact |
| `int:Signed32 'limit?;` (PublicObjectSearchRequest) | line 302 | exact |
| `record {\|ValueWithTimestamp[]...;\|} propertiesWithHistory?;` ×3 | lines 230, 394, 448 | exact |
| `record {\|CollectionResponseAssociatedId...;\|} associations?;` | line 386 | exact |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | line 240–241 | exact; it is the only `@` annotation in the module (`grep '^@' *.bal` → 1 hit) |

The removed `anydata Additional Values` parameter has **no counterpart in the library**:
`grep -rn 'Additional Values\|Capture key value pairs'` over the entire bala returns nothing. It was
a synthesised placeholder for the open rest-field of the included `*…Queries` record. Its removal
therefore does not drop any real API surface.

The 12 client entries in `new` match `client.bal` one-for-one: `init` (line 31) plus
`post batch/read` (47), `get [discountId]` (68), `delete [discountId]` (86), `patch [discountId]`
(103), `post batch/archive` (122), `post batch/create` (140), `post batch/update` (158), `get .`
(177), `post .` (194), `post batch/upsert` (212), `post search` (230). Payload types and return
unions are identical in both renders and match the source exactly.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:

- Full `diff -u` of the two `.bal.txt` files (only the 15 hunks listed in §2; every one is an
  old→new *correction*, never a deletion of real content).
- Normalized (`json.tool --sort-keys`) diff of the two JSONs: 174 diff lines total = 4 × 8-line
  `Additional Values` removals + 11 one-line type-name corrections + 1 six-line annotation
  insertion. Nothing else changed. Line counts 2565 → 2539, exactly `-32 + 6 = -26`.
- Type-name sets identical old vs new vs bala (41 each).
- Record-field totals identical (169 vs 169), so no field, doc comment, or optionality marker was
  dropped.
- README section byte-identical between old and new (`diff` of lines 1–178 → empty) and identical
  to the bala's `docs/README.md` (170 rendered lines vs 169 file lines; the only difference is one
  trailing blank line added by the renderer).
- `// Special Agent Note:` cross-package hints: 17 in old, 17 in new — none lost.
- `// Unknown type:` placeholders: 0 in both, so the spec-v2 "degraded type" improvement is not
  exercised by this library (it has no error/object/other type defs).

## 5. Issues in `new` (independent of `old`)

All five below are present **identically in `old`**, i.e. pre-existing extractor behaviour, not
introduced by spec v2. They are listed because they would still mislead an LLM reading `new`.

1. **Record-field default values are dropped and turned into `?`.** Source
   `GetCrmV3ObjectsDiscountsQueries` has `boolean archived = false;` (types.bal:99) and
   `int:Signed32 'limit = 10;` (types.bal:103); `new` renders both as optional with no default
   (`boolean archived?;`, `int:Signed32 'limit?;`, render lines 366/370).
   Same for `GetCrmV3ObjectsDiscountsDiscountIdQueries.archived` (types.bal:462 → render line 662)
   and `PostCrmV3ObjectsDiscountsBatchReadQueries.archived` (types.bal:460 → render line 713).
2. **Wrong default for `limit` in the client signature.** `new` line 748 renders
   `int:Signed32 limit = 0`; the real default, inherited from the included record, is `10`
   (types.bal:103). The JSON carries `"default": "0"` on both sides — the wrong value originates in
   the extractor, not the renderer.
3. **Included-record parameters are both flattened and duplicated.** Source declares a single
   included param, e.g. `resource isolated function get .(map<string|string[]> headers = {},
   *GetCrmV3ObjectsDiscountsQueries queries)` (client.bal:177). `new` emits the record's six fields
   as separate parameters **and** an extra `GetCrmV3ObjectsDiscountsQueries queries` parameter
   (line 748), which is not a valid signature and double-counts every query parameter. Affects the
   same 4 methods.
4. **Resource path `.` is rendered as nothing.** `resource function get (` and
   `resource function post (` (lines 748, 752) are not parseable Ballerina; the source is
   `get .(` / `post .(`.
5. **Closed records are rendered as open.** The bala has 3 closed top-level records
   (`ConnectionConfig`, `OAuth2RefreshTokenGrantConfig`, `ApiKeysConfig` — `record {|`) and 38 open
   ones; the render emits all 41 as `record {`. `public` and `isolated` qualifiers are also dropped
   throughout (`grep -c '^public '` → 0), which is a deliberate render convention rather than an
   error, but the closed/open distinction is genuine information loss.

## 6. Coverage gaps vs. the library

**None.** The package exports exactly one module (`package.json` `"export": ["hubspot.crm.commerce.discounts"]`,
Central metadata lists one module), which is the default module, so the
`getDefaultModule()`-only extraction has nothing to miss here.

- `grep -E '^public (type|const|enum|class|annotation)'` over the bala's three `.bal` files yields
  41 names; the JSON `typeDefs` list is the same 41 names (`diff` → empty).
- `grep -E '^public (isolated )?function'` over the bala yields **0** module-level public functions —
  consistent with the render's empty `functions` section.
- `public isolated client class Client` (client.bal:23) is rendered, with all 12 of its methods.
- No submodules exist (`modules/` contains only `hubspot.crm.commerce.discounts`), so there is no
  submodule-only shared gap either.

Non-public helpers in `utils.bal` (`Encoding`, `getPathForQueryParam`, `getEncodedUri`, …) are
correctly absent. Note that `map<Encoding>` appears in the source body only, never in a public
signature, so its absence is not a gap.

## 7. Compiler plugin

**No compiler plugin exists.** `find` for `*compiler-plugin*` in the upstream clone returns nothing,
and the bala contains no `compiler-plugin/` directory (bala tree is `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json` only). Nothing plugin-implied is
therefore missing from the render.

## 8. Other considerations

- **Stability**: `2.0.2` is a stable release; Central reports `deprecated: null`, empty
  `deprecateMessage`, license Apache-2.0, `ballerinaVersion: 2201.12.2`, pullCount 24.
- **Doc quality**: every record field and every client method carries a doc comment in both renders;
  the module-level description and the full 169-line README (Overview, Setup with HubSpot
  developer-account steps, Quickstart, Examples) are reproduced verbatim.
- **Size/tokens**: 764 lines — the +1 line is the `@display` annotation. Removing the 11 fully
  qualified names also shortens several lines materially (e.g. the `propertiesWithHistory` field
  drops ~50 characters each), so the new render is slightly cheaper in tokens despite the extra
  line.
- **Consumer impact**: replacing `ballerina/lang.int:0.0.0:Signed32` with `int:Signed32` is the most
  valuable change here — the old spelling is not writable Ballerina and would have led a code
  generator to emit uncompilable field types in generated records.
- The library is fully OpenAPI-generated ("AUTO-GENERATED FILE. DO NOT MODIFY."), which is why the
  API surface is flat and entirely record/client based.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 763 / 764 |
| `diff -u old new` (renders) | 15 hunks, all listed in §2 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each; Client at 715 (old) / 716 (new) |
| `grep -c 'ballerina/lang.int:0.0.0:Signed32' old` | 7 |
| `grep -c 'ballerinax/hubspot.crm.commerce.discounts:2.0.2:' old` | 4 |
| `grep -cE '[a-z]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:' new` | 0 |
| `grep -c 'int:Signed32' new` | 8 (7 fields + 1 client param) |
| `grep -n 'int:Signed32' bala/types.bal` | 7 hits: lines 103,127,179,214,302,330,366 |
| `grep -n '^@' bala/*.bal` | 1 hit: `types.bal:240 @display {label: "Connection Config"}` |
| `grep -n '@display' old / new renders` | 0 hits / 1 hit (new line 529) |
| `grep -rn 'Additional Values\|Capture key value pairs' bala/` | 0 hits |
| `grep -c '"Additional Values"' old.json / new.json` | 4 / 0 |
| JSON element counts (py) old / new | typeDefs 41/41, clients 1/1, client fns 12/12, functions 0/0, services 0/0, annotations 0/0 |
| Total record fields / client params (py) old / new | 169 & 45 / 169 & 41 |
| `diff` of sorted typeDef name lists: bala vs old, old vs new | both empty (identical) |
| `python3 -m json.tool --sort-keys` diff of the two JSONs | 174 lines; 2565 → 2539 |
| `diff` rendered README (lines 8–177) vs `bala/docs/README.md` | only one trailing blank line differs |
| `diff` old vs new render lines 1–178 | empty (README identical) |
| `grep -c 'Special Agent Note'` old / new | 17 / 17 |
| `git ls-remote --tags <repo>` | v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`f113e1b`, peeled `8f0e2c4`) |
| `git clone --depth 1 --branch v2.0.2` then `diff -q` of `ballerina/{client,types,utils}.bal` vs bala | SAME for all three |
| `grep -n 'version' src/ballerina/Ballerina.toml` | `version = "2.0.2"` |
| `find src -iname '*compiler-plugin*'` / `ls bala` | no plugin, no `compiler-plugin/` dir |
| `ls bala/any/modules/` | single module `hubspot.crm.commerce.discounts` |
| `grep -cE '^public type .* record \{\|' bala/types.bal` | 3 closed / 38 open; render emits 41 open |
| `grep -c '^public ' new render` | 0 |
| `grep -E '^public (isolated )?function' bala/*.bal` | 0 module-level public functions |
| `curl api.central.ballerina.io/.../2.0.2` | `deprecated: None`, 1 module, Apache-2.0, ballerinaVersion 2201.12.2 |
| `cat OLD_AND_NEW_DIFFS/hubspot.crm.commerce.discounts_diff.md` | matches my independently generated `diff -u` exactly |

## 10. Caveats and unverified items

- The renders were not re-generated; this audit compares the two supplied artifacts against the bala
  and upstream source. The claim that both sides were produced from the same pinned version is
  supported by the bala's `2.0.2` path, the `2.0.2` embedded in `old`'s qualified type refs, and the
  identical README/type-name sets — but the two pipeline runs themselves were not re-executed.
- The renders are not compiled or parsed; syntax claims in §5 (items 3–5) are from reading the text
  against the Ballerina grammar, not from running a parser.
- Whether `toSyntaxString` in the `new` source deliberately suppresses the open-record rest-field
  parameter, versus the extractor no longer emitting it, was determined from the JSON (the field is
  absent from `new`'s JSON, so it is an extractor-side change) — but the `ballerina-vscode` source
  for either side was not read, so the exact code path is unverified.

# ballerinax/trello 2.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/trello` |
| Pinned version | `2.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-trello |
| Tag reviewed | `v2.0.1` (commit `519e6b7385f16d0bdeab91b3e798ada056c659c4`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/trello/2.0.1` |
| Old render | `4379` lines (185,858 bytes) |
| New render | `4499` lines (185,416 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing is lost.

Four distinct improvements, all verified against the bala source:

1. All 24 `// Unknown type:` placeholders are replaced by real type definitions that match the
   published source **byte-for-byte** (24/24 exact match).
2. All 65 version-qualified type references (`ballerinax/trello:2.0.1:X`, `ballerina/lang.int:0.0.0:Signed32`)
   are now plain (`X`, `int:Signed32`).
3. Annotations are now emitted and are complete: 89 `@http:Query`, 24 `@constraint:*`,
   3 `@jsondata:Name`, 1 `@display` — exactly matching the source counts (source had 118 annotation
   sites; `new` has 118, `old` had 1).
4. A **fabricated** parameter `anydata Additional Values` — which does not exist anywhere in the
   library and is not even legal Ballerina (space in identifier) — is gone from 150 client method
   signatures. It was removed at the JSON/extractor level, not just at render time.

Declarations removed: **0**. Client methods: 253 on both sides, and after normalising away the
`Additional Values` artifact all 253 signatures are character-identical. README block identical.
Doc-comment lines: 1189 → 1192 (+3, all newly attached to types that `old` degraded).

Coverage against the library is complete on both sides: all 343 `public` type-level symbols of the
default module and all 253 client resource methods appear in both renders. Zero coverage gaps.

## 2. Change inventory

Mechanical diff: 131 hunks, 216 lines removed, 336 lines added (`diff old new`).

| Category | old | new | Δ |
|---|---|---|---|
| Total lines | 4379 | 4499 | +120 |
| Bytes | 185,858 | 185,416 | −442 |
| Top-level declarations (incl. `client class Client`) | 320 | 344 | +24 |
| `// Unknown type:` placeholders | 24 | 0 | −24 |
| Version-qualified refs `org/mod:ver:Type` | 65 | 0 | −65 |
| `@http:Query` | 0 | 89 | +89 |
| `@constraint:*` | 0 | 24 | +24 |
| `@jsondata:Name` | 0 | 3 | +3 |
| `@display` | 0 | 1 | +1 |
| `@deprecated` | 1 | 1 | 0 |
| Client `resource`/`remote` methods | 253 | 253 | 0 |
| `anydata Additional Values` params | 150 | 0 | −150 |
| Doc-comment (`#`) lines | 1189 | 1192 | +3 |
| Section markers (`// --- `) | 4 | 4 | 0 |
| JSON `typeDefs` | 343 | 343 | 0 |
| JSON `typeDefs` of kind `Other` | 24 | 24 | 0 |

**Declarations added (24)** — all `type`, all previously `// Unknown type:` placeholders:

`AttachmentsAttachmentsOneOf12`, `AttachmentsOneOf1`, `CardCheckItemStates`, `Channel`,
`CheckItemStatesOneOf1`, `Id1OneOf2`, `Id2OneOf2`, `IdBoardsOneOf1`, `IdMember1OneOf2`,
`IdMemberOneOf1`, `IdOneOf2`, `InlineParameterItemsIdLabels`, `InlineParameterItemsIdMembers`,
`ListFields`, `MemberFields`, `Pos1Pos1OneOf12`, `Pos2OneOf1`, `Pos3OneOf1`, `PosPosOneOf12`,
`PosStringOrNumberPosStringOrNumberOneOf12`, `TrelloID`, `Value1OneOf1`, `Value1Value1OneOf12`,
`Value1Value1Value1Value1OneOf1234`.

**Declarations removed: 0.** Verified by `diff` of the sorted top-level declaration sets — the only
`<` entries are the 24 placeholders and 23 lines that reappear with the version qualifier stripped.

**Declarations modified (23 `type` lines):** version-qualifier removal only, e.g.
`type Id ballerinax/trello:2.0.1:TrelloID|ballerinax/trello:2.0.1:IdOneOf2;` →
`type Id TrelloID|IdOneOf2;`.

**Modified record fields (11):** `ballerina/lang.int:0.0.0:Signed32 x?` → `int:Signed32 x?`;
`ballerinax/trello:2.0.1:Color? c?` → `Color? c?`.

**Modified client methods (150 of 253):** removal of `anydata Additional Values, ` only.

**Annotation lines added (117)** across records and type defs; **3 doc lines added**
(`# The new name for the List`, `# The new position for the List`, `# Name of the organization`)
now attached to `Value1OneOf1`, `Value1Value1OneOf12`, `Id2OneOf2` respectively.

## 3. Correctness against library source

Bala and upstream `v2.0.1` are byte-identical for `client.bal`, `types.bal`, `utils.bal`
(`diff -q` → identical for all three), so GitHub and the bala do not disagree here.

**All 24 added type definitions verified exactly.** A script compared
`^public type <N> (.+);$` in `bala .../modules/trello/types.bal` against `^(public )?type <N> (.+);$`
in the new render: **24 exact matches, 0 mismatches.** Sample citations (`types.bal` line numbers):

| Type | source line | source RHS | new render |
|---|---|---|---|
| `TrelloID` | 2553 | `string` | `type TrelloID string;` (render:116) |
| `Channel` | 2421 | `"email"` | `type Channel "email";` |
| `AttachmentsOneOf1` | 575 | `"cover"` | `type AttachmentsOneOf1 "cover";` |
| `AttachmentsAttachmentsOneOf12` | 2496 | `boolean` | same |
| `IdBoardsOneOf1` | 2139 | `"mine"` | same |
| `ListFields` | 1352 | `"id"` | same |
| `MemberFields` | 2808 | `"id"` | same |
| `CardCheckItemStates` | 2649 | `CheckItemStatesOneOf1` | same |
| `InlineParameterItemsIdMembers` | 196 | `TrelloID` | same |
| `InlineParameterItemsIdLabels` | 349 | `TrelloID` | same |
| `Pos1Pos1OneOf12` | 2660 | `float` | same |
| `Value1Value1Value1Value1OneOf1234` | 2104 | `boolean` | same |

**Annotations verified positionally, not just by count.** A script extracted every
(annotation-line, annotated-declaration) pair from `types.bal` (118 pairs) and from the new render
(118 pairs). Every annotation string and its target member name/type line up 1:1. The only textual
deltas in the pairing are caused by the renderer's pre-existing habit of dropping field defaults and
marking fields optional (`boolean paidAccount = false;` in source vs `boolean paidAccount?;` in the
render) — the annotation itself and the field name/type always match. Examples confirmed:

- `types.bal:2551` `@constraint:String {pattern: re \`^[0-9a-fA-F]{24}$\`}` on `TrelloID` →
  new render line 115–116, identical.
- `types.bal:155` `@display {label: "Connection Config"}` on `ConnectionConfig` → new render 309.
- `types.bal:771 / 1036 / 1828` `@jsondata:Name {value: "display_cardFront" / "display/cardFront" / "_id"}`
  → new render 1439 / 1718 / 1149. All three present, values correct.
- `@deprecated` on `paidAccount` — present in both old (1010) and new (1021).

**New doc comments verified.** `types.bal:2007` `# Name of the organization` precedes
`public type Id2OneOf2 string;`; `types.bal:2400` `# The new name for the List` precedes
`public type Value1OneOf1 string;`; `types.bal:2049` `# The new position for the List` precedes
`public type Value1Value1OneOf12 float;`. All three now appear in `new` and were absent from `old`
(they were swallowed with the `// Unknown type:` degradation).

**`Additional Values` is confirmed fabricated.** `grep -rn 'Additional Values'` and
`grep -rn 'Capture key value pairs'` over the whole bala return nothing. The source signature is
`resource isolated function get actions/[TrelloID id](map<string|string[]> headers = {}, *GetActionsIdQueries queries)`
(`client.bal:44`) — no such parameter exists. Removing it is a correctness fix.

**README verified verbatim.** `diff` of render lines 8–96 against `docs/README.md` lines 1–88 shows
only one trailing blank line. Identical in `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. Sorted top-level declaration sets diffed (`decl_old.txt` 320 lines vs `decl_new.txt` 344):
   0 entries present in `old` and absent from `new`.
2. All 253 client method signatures extracted from both files; after deleting the literal
   `anydata Additional Values, ` substring from the `old` set, `old == new` element-wise
   (`still differing: 0`).
3. Line-level `difflib` opcode diff with version-qualifier normalisation: every one of the 216
   removed lines falls into exactly one of — 24 placeholders, 23 requalified `type` lines,
   150 client methods (only the fabricated param removed), 19 requalified record-field lines.
   Nothing else was deleted.
4. Doc-comment line count went **up** (1189 → 1192); no `#` line present in `old` is absent in `new`.
5. README block (lines 1–98) byte-identical between the two renders.
6. Section markers unchanged (4 → 4); `@deprecated` retained.
7. Both JSONs report `typeDefs: 343`, `clients[0].functions: 254` — nothing dropped upstream of the
   renderer either.
8. Every added line is syntactically well-formed Ballerina; `new` in fact removes the only malformed
   construct in the file (`anydata Additional Values` — an identifier containing a space).

## 5. Issues in `new` (independent of `old`)

All six below are **shared with `old`** — identical in both renders — so none is a regression. They
are recorded because they are inaccuracies a consuming LLM would inherit.

1. **Record-field default values are dropped, and defaulted fields are rendered optional.**
   `types.bal` has 209 record fields with an initialiser; both renders emit 0. E.g. source
   `GetActionsIdQueries { boolean display = true; string fields = "all"; ... }` renders as
   `boolean display?; string fields?;`. Semantically this turns "defaults to true" into "absent".
2. **Flattened client query parameters carry zero-value defaults instead of the real ones.**
   Render (both sides, line old:3384 / new:3504):
   `..., string memberFields = "", boolean display = false, boolean member = false, boolean memberCreator = false, string fields = "", ...`
   Source `GetActionsIdQueries` (`types.bal`) says
   `memberFields = "avatarHash,fullName,initials,username"`, `display = true`, `member = true`,
   `memberCreator = true`, `fields = "all"`. Confirmed to originate in the **Java extractor**, not
   the renderer: both `old` and `new` JSON carry `"display": {"default": "false"}` etc.
   This actively misinforms — an LLM would believe `display` defaults to `false`.
3. **Client signatures list the flattened query params *and* the included-record param.**
   `..., string memberCreatorFields = "", GetActionsIdQueries queries)` — the real signature is
   `(map<string|string[]> headers = {}, *GetActionsIdQueries queries)`. The rendered form would not
   compile against the real client.
4. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:156`) and `ApiKeysConfig`
   (`types.bal:1875`) are `record {|...|}` in source, `record { ... }` in both renders.
5. **Self-module qualification in resource paths.** 279 occurrences of `trello:TrelloID` /
   `trello:ActionFields` etc. inside the `trello` module's own client — identical count in `old` and
   `new`. Harmless but noisy; note that `new` fixed the *versioned* qualifiers but not these.
6. **Method-level doc detail dropped.** Client methods render as a one-line summary plus an empty
   `# ` line; the source's `# + id - ...`, `# + queries - ...`, `# + return - Success` lines are not
   carried. Also the `isolated` qualifier is dropped (0 occurrences of `isolated function` in either
   render vs 253 in `client.bal`).

## 6. Coverage gaps vs. the library

**Zero gaps.**

- The bala exports exactly one module (`package.json` `"export": ["trello"]`;
  `modules/` contains only `trello/`). There is **no submodule API**, so the shared
  `getDefaultModule()` limitation does not bite this library.
- Public type-level symbols in `modules/trello/*.bal`: **343**. Symbols in the new render: 344
  (343 + `main` from the README code sample). `comm -23 src_syms new_syms` → **empty**.
- Client methods: `grep -cE '^\s+(public )?(resource|remote) isolated function ' client.bal` → 253;
  both renders → 253.
- `utils.bal` contains 6 module-private `isolated function`s (`getEncodedUri`, `getFormStyleRequest`,
  …) — none is `public`, so their absence is correct, not a gap.

## 7. Compiler plugin

**No compiler plugin exists for this package.**

- `find . -iname '*compiler-plugin*'` over the cloned `v2.0.1` tree → no results.
- The bala contains no `compiler-plugin/` directory (`ls .../2.0.1/any` → `bala.json`,
  `dependency-graph.json`, `docs`, `modules`, `package.json`).
- `ballerina/Ballerina.toml` has no `[[plugin]]` / `[[platform.java21.dependency]]` plugin entry.

Consequently there is nothing plugin-derived that should surface in the render. The runtime
behaviours that *are* declarative — `ballerina/constraint` validation (`@constraint:String`,
`@constraint:Int`, `@constraint:Float`, `@constraint:Number`) and `ballerina/http` query-name
mapping (`@http:Query`) — are dependencies (`dependency-graph.json` lists `ballerina/constraint 1.7.0`)
rather than plugins, and `new` now surfaces all 113 of those annotation sites. `old` surfaced none.

## 8. Other considerations

- **Version:** stable `2.0.1`, `graalvmCompatible: true`, built with `ballerina_version 2201.12.7`
  against `distribution = "2201.12.0"`. Not pre-1.0, not deprecated (Central metadata not re-queried;
  see caveats).
- **Deprecation inside the API:** one `@deprecated` member (`paidAccount`), present in both renders.
- **Size / tokens:** `new` is 120 lines longer but **442 bytes smaller** — the 24 added definitions
  and 117 annotation lines are more than paid for by dropping 65 version qualifiers and 150
  `anydata Additional Values, ` fragments. Token cost is effectively flat while information density
  rises substantially.
- **Encoding:** the two non-ASCII characters in `new` (curly apostrophes on render lines 26 and 37)
  come straight from `docs/README.md`, which contains exactly 2 such lines. No corruption.
- **Type naming:** the connector's generated names are poor (`Value1Value1Value1Value1OneOf1234`,
  `PosStringOrNumberPosStringOrNumberOneOf12`). That is an upstream OpenAPI-generation artifact,
  identical in the library source; nothing the render can fix. But it makes point 1/2 of §5 worse in
  practice, because an LLM has little else to go on.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/… new/…` | 4379 / 4499 |
| 2 | `wc -c old/… new/…` | 185,858 / 185,416 |
| 3 | `grep -c '^// Unknown type:'` | old 24, new 0 |
| 4 | `grep -n '^// --- '` both | 4 markers each; Types@99, Client@3377(old)/3497(new) |
| 5 | `git ls-remote --tags <repo>` | `v2.0.0`, `v2.0.1`; `v2.0.1^{}` = `519e6b73…` |
| 6 | `git clone --depth 1 --branch v2.0.1` | success |
| 7 | `diff -q bala/modules/trello/{client,types,utils}.bal src/ballerina/…` | identical ×3 |
| 8 | `ls bala/…/any/modules` | only `trello` — single module, no submodules |
| 9 | `cat package.json` | `"export": ["trello"]`, v2.0.1, graalvmCompatible |
| 10 | `wc -l bala modules` | client.bal 3883, types.bal 2828, utils.bal 219 |
| 11 | sorted top-level decl diff (`decl_old` 320 vs `decl_new` 344) | +24 types, −0 |
| 12 | python exact-compare of 24 type RHS vs `types.bal` | **24 exact, 0 mismatch** |
| 13 | `grep -nE '^public type <N> ' types.bal` for all 24 | all found (lines 196…2824, listed §3) |
| 14 | annotation (annot, target) pairing script | src 118, new 118, old 1; all names/targets align |
| 15 | `grep -c '@http:Query'` src / old / new | 89 / 0 / 89 |
| 16 | `grep -c '@constraint'` src / old / new | 24 / 0 / 24 |
| 17 | `grep -c 'jsondata:Name'` src / old / new | 3 / 0 / 3 |
| 18 | `grep -n '@display'` src / old / new | 1 (types.bal:155) / 0 / 1 (line 309) |
| 19 | `grep -n '@deprecated'` old / new | 1 (1010) / 1 (1021) |
| 20 | client method extraction + `Additional Values` strip | 253 vs 253, **0 still differing** |
| 21 | `grep -c 'anydata Additional Values'` old / new | 150 / 0 |
| 22 | `grep -rn 'Additional Values\|Capture key value pairs' bala/` | **no matches** — fabricated |
| 23 | `grep -o 'ballerinax/trello:2\.0\.1:'` old / new | 54 / 0 |
| 24 | `grep -o 'ballerina/lang\.[a-z]*:0\.0\.0:'` old / new | 11 / 0 (total 65 → 0) |
| 25 | `grep -oE '…trello:[A-Za-z]'` old / new | 279 / 279 (unchanged self-qualification) |
| 26 | `grep -c '^\s*#'` old / new | 1189 / 1192 (+3) |
| 27 | `diff` render lines 1–98 old vs new | identical (README block) |
| 28 | `diff` render 8–96 vs `docs/README.md` 1–88 | only 1 trailing blank |
| 29 | JSON `typeDefs` count old / new | 343 / 343 |
| 30 | JSON `typeDefs` kind histogram old / new | `Record 278, Union 41, Other 24` both |
| 31 | JSON `Other` typeDef keys old / new | old `[name,description,type]`; new adds `baseType,annotations` |
| 32 | JSON `clients[0].functions` old / new | 254 / 254 |
| 33 | JSON `Additional Values` params old / new | 150 / 0 (removed at extractor level) |
| 34 | JSON defaults for `fns[1]` old / new | identical; `display:"false"` both — vs source `= true` |
| 35 | `grep -cE '^\s+(resource\|remote) ' old / new` | 253 / 253 |
| 36 | public-symbol `comm -23 src_syms new_syms` | **empty** (343 src symbols all present) |
| 37 | `comm -13 src_syms new_syms` | only `main` (README sample) |
| 38 | `find . -iname '*compiler-plugin*'` in clone | none |
| 39 | `ls bala/…/any` | no `compiler-plugin/` dir |
| 40 | record-field-with-default count src / old / new | 209 / 0 / 0 |
| 41 | `grep -c 'isolated function'` renders | 0 / 0 (vs 253 in `client.bal`) |
| 42 | `grep -c 'record {\|'` src types.bal / old / new | 2 top-level closed / 22 inline / 22 inline |
| 43 | `LC_ALL=C grep -c '[^ -~]'` README.md / new render | 2 / 2 (same lines) |
| 44 | `grep -c 'Special Agent Note'` old / new | 14 / 14 |

## 10. Caveats and unverified items

1. **Ballerina Central API not re-queried.** Deprecation status and keyword metadata were read from
   the bala's `package.json` and the repo's `Ballerina.toml`, not from
   `api.central.ballerina.io`. Nothing in the local metadata indicates deprecation, but a
   Central-side `deprecated` flag would not have been seen.
2. **Renders were not compiled.** "Syntactically well-formed" in §4 is a reading-level judgement on
   the added lines plus the removal of the one space-in-identifier construct; neither render was fed
   to `bal build`. The pseudo-Ballerina in both files (flattened + record query params, dropped
   `isolated`) would not compile as-is regardless — that is by design of `toSyntaxString`.
3. **Annotation *argument* values were compared as whole strings.** The pairing script matched the
   full annotation text (e.g. `@constraint:Int {minValue: 0, maxValue: 1000}`), so argument order or
   whitespace normalisation by the renderer would have shown as a mismatch — none did. But nested or
   multi-line annotation bodies, had any existed, would not have been fully reconstructed by the
   line-based script. `types.bal` contains no multi-line annotation, so this is not believed to
   matter here.
4. **`old`-side renderer patch (`service.methods ?? []`)** is documented as affecting only
   `ballerina/mcp`; not independently re-verified for this library. This library has no services
   (`services` array empty in both JSONs), so it cannot apply.
5. **Doc-comment content of the 1189 shared `#` lines was not diffed word-by-word**, only counted
   and confirmed non-decreasing; the line-level `difflib` opcode pass would have surfaced any removed
   or altered `#` line, and the only `#` lines in the delta were the 3 additions.

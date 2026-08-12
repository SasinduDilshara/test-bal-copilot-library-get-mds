# ballerinax/smartsheet 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/smartsheet` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-smartsheet |
| Tag reviewed | `v1.0.2` (commit `32c5b0f1273865db24b166b7a94d13b90989b391`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/smartsheet/1.0.2` |
| Old render | `10516` lines |
| New render | `10940` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Single-module connector (bala export list = `["smartsheet"]`), 865 public types + 1 client with
185 functions (184 resource methods + `init`). Both renders carry the identical declaration set;
the JSON payloads both report `typeDefs=865`, `clients=1`, `clients[0].functions=185`,
`functions=0`, `services=0`, `annotations=0`.

`new` is a strict superset of `old` in information content. Four concrete gains, zero losses:

1. All **38** `// Unknown type: X` stubs in `old` are replaced by real type definitions in `new`
   (`old`=38, `new`=0). All 38 match the bala byte-for-byte modulo the `public` keyword.
2. All **171 occurrences (19 lines)** of version-qualified refs
   (`ballerinax/smartsheet:1.0.2:Type`, `ballerina/lang.int:0.0.0:Signed32`) are gone in `new`
   and rendered as plain `Type` / `int:Signed32`.
3. **97** malformed, non-compiling `anydata Additional Values` parameters in `old` client method
   signatures are gone in `new` (`old`=97, `new`=0).
4. Annotations are now emitted. `old` carried 13 annotation lines (all `@deprecated`); `new`
   carries **406**, and every count matches the bala exactly except one benign duplicate
   (see §5.6). The keyword-clashing field `source` is now correctly quoted as `'source`
   (126 occurrences).

Everything else — README, section markers, client method set, method signatures — is unchanged.
The remaining defects in `new` (§5) are all present identically in `old` and are pipeline-wide,
not spec-v2 regressions.

## 2. Change inventory

Line counts: `old` 10516, `new` 10940 (+424). Section markers identical in count and order
(`README`, `END README`, `Types`, `Client`) — only their line offsets shift.

| Region | old lines | new lines | change |
|---|---|---|---|
| Header + README (1–124) | 124 | 124 | byte-identical (`diff` empty) |
| Types (125 → Client marker) | 9626 | 10050 | 183 removed / 607 added |
| Client (marker → EOF) | 766 | 766 | 97 lines changed (only `anydata Additional Values` removal) |

**Declarations by kind** — extracted from both files:

| Kind | old | new | delta |
|---|---|---|---|
| `type` (all, incl. `// Unknown type` stubs) | 827 real + 38 stubs = 865 names | 865 real | +38 real definitions |
| of which `record` bodies | 801 | 801 | 0 |
| `class` / `enum` / `const` / `annotation` / `service` / `listener` | 0 | 0 | 0 |
| `client class Client` | 1 | 1 | 0 |
| client methods (incl. `init`) | 185 | 185 | 0 |

Type-name sets are **exactly equal** (`comm -23` and `comm -13` both empty). Client method
name/path list is **byte-identical** (`diff` on 185 extracted signatures returns nothing).

**Added (38 type definitions)** — all previously `// Unknown type:` stubs:
`Columns ContactOptions FavoritesOneOf2 Format Formula GroupMembersAddArray
GroupsgroupIdmembersOneOf2 IcalEnabled Id Index Locked Name Options Permalink Primary
PropertiesContactOptions PropertiesId PropertiesOptions PropertiesSymbol PropertiesTitle
ReadOnlyFullEnabled ReadOnlyFullShowToolbar ReadOnlyLiteEnabled ReadWriteEnabled
ReadWriteShowToolbar ReportsreportIdsharesOneOf2 SheetssheetIdrowsOneOf2
SheetssheetIdrowsOneOf21 SheetssheetIdsharesOneOf2 Symbol TimestampDateTime TimestampNumber
Title UsersuserIdalternateemailsOneOf2 Validation Version Width
WorkspacesworkspaceIdsharesOneOf2`

**Removed (183 lines) — fully accounted for, nothing lost:**

| Removed | count | replaced in `new` by |
|---|---|---|
| `"WEB_APP"\|…\|"API_ODBC_DRIVER" source?;` | 126 | same line with `'source?;` (valid quoted identifier) |
| `// Unknown type: X` | 38 | 38 real `type X …;` definitions |
| `type X a/b:1.0.2:Y\|…;` alias lines | 18 | same aliases with unqualified refs |
| `ballerina/lang.int:0.0.0:Signed32 maxCount?;` | 1 | `int:Signed32 maxCount?;` |
| **total** | **183** | |

**Added (607 lines):** 38 type definitions (+ their doc/blank lines), 18 clean alias lines,
126 `'source` lines, 1 `int:Signed32` line, and **393 annotation lines**
(254 `@http:Header`, 116 `@constraint:Int`, 11 `@constraint:Number`, 6 `@http:Query`,
4 `@jsondata:Name`, 2 `@deprecated`, 1 `@display` — deltas relative to `old`'s 13).

**Modified:** the 97 client signatures listed above. After normalising away
`anydata Additional Values`, the two client sections are byte-identical
(`diff old_client_norm.txt new_client.txt` → empty).

## 3. Correctness against library source

Upstream `v1.0.2` (`src/ballerina/{client,types,utils}.bal`) is **byte-identical** to the bala
`modules/smartsheet/*.bal` (`diff -q` reports "same" for all three). So GitHub and bala agree;
no conflict to resolve.

- **All 38 newly-emitted types verified individually** against `types.bal`: a scripted
  comparison of `^public type <T> …` (bala, `public` stripped) vs `^type <T> …` (new render)
  gave **exact-match = 38, mismatch = 0**. Examples: `type TimestampDateTime string;`
  (types.bal), `type FavoritesOneOf2 Favorite[];`, `type GroupMembersAddArray GroupMemberAdd[];`,
  `type ContactOptions ContactOption[];`, `type Id decimal;`.
- **Annotation fidelity** — counts in `new` vs the bala's `.bal` sources:

| Annotation | bala | new | old |
|---|---|---|---|
| `@http:Header` | 254 | 254 | 0 |
| `@constraint:Int` | 116 | 116 | 0 |
| `@constraint:Number` | 10 | 11 | 0 |
| `@deprecated` | 15 | 15 | 13 |
| `@display` | 1 | 1 | 0 |
| `@http:Query` | 6 | 6 | 0 |
| `@jsondata:Name` | 4 | 4 | 0 |

  Not just counts — the *values* match. `@http:Header` name histogram is identical
  (`Authorization`×182, `Content-Type`×56, `Content-Disposition`×5, `x-smar-sc-actor-id`×5,
  `Accept`×2, `Accept-Encoding`×2, `Content-Length`×2). `@constraint:Int` histogram identical
  (`{minValue: 0}`×110, `{minValue: 1}`×4, `{minValue: 1, maxValue: 10000}`×2). All 6
  `@http:Query` names and all 4 `@jsondata:Name` values match
  (`access_token`, `refresh_token`, `token_type`, `expires_in`; `include&exclude`,
  `redirect_url`, `client_id`, `client_secret`, `grant_type`, `refresh_token`).
- **`'source` quoting**: bala `types.bal:6139` has
  `"WEB_APP"|…|"API_ODBC_DRIVER" 'source?;`. `new` matches; `old` emitted bare `source?`,
  which is a Ballerina keyword and would not compile.
- **Client**: bala `client.bal` has 184 `resource isolated function` + 1
  `public isolated function init(ConnectionConfig config, string serviceUrl = "https://api.smartsheet.com/2.0")`.
  `new` renders 185 functions with matching paths and return types. Spot-checked 5 against
  `client.bal:688, 1398, 2350, 2174, 602` — path, payload type, headers type and return type all
  match (`get sheets/[decimal sheetId]` → `Sheet|SheetVersion|error`,
  `post sheets/[decimal sheetId]/rows(SheetIdRowsBody1 payload,…)` → `RowMoveResponse|error`,
  `delete webhooks/[string webhookId]` → `WorkspaceShareDeleteResponse|error`,
  `put users/[decimal userId](UserUpdate payload,…)` → `HomeFolderCreateResponse|error`,
  `get search` → `UserCreateResponse|error`).
- **README**: bala `docs/README.md` is 114 lines; render lines 8–121 reproduce it in full
  (`diff` shows only one trailing blank line difference). Identical in `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Type-name sets compared with `comm`: nothing present in `old` is absent from `new`
  (`comm -23 old_types.txt new_types.txt` → empty).
- Client method set compared: `diff old_methods.txt new_methods.txt` → identical (185 each).
- Client bodies compared after normalising the one known removal:
  `sed 's/anydata Additional Values, //g; s/, anydata Additional Values//g' old_client.txt`
  is byte-identical to `new_client.txt`. So no parameter, default, return type or doc line was
  dropped from any of the 185 signatures.
- Every one of the 183 removed lines in the Types section was individually classified
  (table in §2) and each maps to a strictly-better replacement in `new`. Sum = 183, no residue.
- Header + README region: `diff` on lines 1–124 → empty.
- Doc-comment continuation lines (the malformed unprefixed lines, see §5.5): the sorted sets are
  identical between `old` and `new` (357 each); the only `diff` output is three *correctly placed*
  top-level annotation lines added in `new` (`@deprecated`×2, `@display`×1).
- JSON payloads: `typeDefs` name sets equal, `clients[0].functions` = 185 on both sides.

## 5. Issues in `new` (independent of `old`)

All eight below are present **identically in `old`** — they are pipeline-wide behaviours, not
introduced by spec v2. Listed because they still mislead an LLM consuming this render.

1. **Included-record query parameters are double-emitted with fabricated defaults.**
   Source: `client.bal:67` `resource isolated function get contacts(ListContactsHeaders headers = {}, *ListContactsQueries queries)`.
   Render: `resource function get contacts(ListContactsHeaders headers = {}, Timestamp modifiedSince = "", boolean numericDates = false, decimal pageSize = 0.0d, boolean includeAll = false, decimal page = 0.0d, ListContactsQueries queries)`.
   The `*Queries` inclusion is expanded into individual params **and** the record is still passed —
   the signature does not compile, and the fabricated defaults contradict the source:
   `types.bal:1259` has `decimal pageSize = 100`, `types.bal:1263` has `decimal page = 1`, but the
   render says `0.0d` for both. Similarly `get search` renders `string query = ""` where
   `ListSearchQueries.query` is a **required** field.
2. **Record-field default values are dropped entirely.** The bala's `types.bal` has **259**
   fields with defaults; both renders have **0**. Concrete losses:
   `decimal sheetCount = -1` → `decimal sheetCount?;`, `string location = ""` → `string location?;`,
   `decimal expiresIn = 604799` → `decimal expiresIn?;`.
3. **Deprecated client methods lose their deprecation.** `client.bal` marks 4 resource methods
   `@deprecated` with a `# # Deprecated` doc block (lines 318, 435, 653, 672 —
   `get folders/personal`, `post home/folders`, `post sheets`, `post sheets/'import`).
   The Client section of both renders contains **0** `@deprecated` and **0** `# Deprecated`.
   The 15 `@deprecated` in `new` are all on type fields/types; none on methods.
4. **Malformed optional-union ordering.** `types.bal:2655` has
   `"folder"|"home"|"workspace"? destinationType?;`. Both renders emit
   `"workspace"?|"folder"|"home" destinationType?;` — the `?` is attached to the first member,
   which is invalid syntax and changes the meaning. 5 occurrences in each render.
5. **Multi-line doc descriptions break out of the comment.** Where a description contains a
   newline, continuation lines are emitted at column 0 without a `#` prefix, e.g. render line 133
   `The \`"home"\` enum is **Deprecated** since March 25, 2025, and will be removed` sits between
   `# Type of destination container.` and the field. **357 such lines** in each render — this is
   non-compiling and, worse, the text reads as free-floating prose to a consumer.
6. **Type aliases pointing at records are expanded into duplicate record bodies.** `types.bal:409`
   is `public type RowResponse GetRowObject;`, but both renders emit `RowResponse` as a full
   copy of the `GetRowObject` record. Aggregate effect: 771 `record` types in the bala vs **801**
   rendered records in both files. This is also the single source of the `@constraint:Number`
   count discrepancy (11 rendered vs 10 in source — the extra
   `@constraint:Number {minValue: 1}` on `rowNumber` is the duplicated copy in `RowResponse`).
   The annotation itself is correct; only the alias identity is lost.
7. **Closed records rendered as open.** The bala has 2 `record {|…|}` (including
   `ConnectionConfig`, `types.bal:5789`); both renders emit `record {` — 0 closed records.
8. **`isolated` qualifier dropped** on all 185 client functions
   (`resource isolated function` → `resource function`). Cosmetic but signature-inaccurate.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `export` = `["smartsheet"]`; `modules/` contains exactly one directory,
  `smartsheet`. There is **no submodule API**, so the known `getDefaultModule()`-only limitation
  costs this library nothing.
- All **865** `public type` names in `modules/smartsheet/types.bal` appear in `new`
  (`comm -23 bala_types.txt new_types.txt` → empty). No invented symbols either
  (`comm -13` → empty).
- The bala has **0** public module-level `function`, `const`, `enum`, `class`, `listener` or
  `service` — so the renders' zero counts for those are correct, not gaps.
- All 184 resource methods + `init` are present.

Note: `old` technically listed the same 865 names, but 38 of them were content-free
`// Unknown type:` comments. Those are coverage gaps in `old` that `new` closes.

## 7. Compiler plugin

**None exists.** `find` over the `v1.0.2` clone found no `compiler-plugin` directory or module;
the bala contains no `compiler-plugin/compiler-plugin.json`. `Ballerina.toml` declares only
`[platform.java17] graalvmCompatible = true` and `[build-options] observabilityIncluded = true`.
Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- **Deprecations.** The library carries real deprecations that the render under-reports: 4
  deprecated client methods (§5.3) and the `"home"` `destinationType` enum value, whose
  deprecation note survives only as the malformed free-floating text of §5.5. Field-level
  `@deprecated` (15) is now correct in `new`.
- **Size / tokens.** 10940 lines, ~1.63 MB of JSON (`new`) vs 1.58 MB (`old`) — +3.1 %. The
  render grew 4 % for a large fidelity gain; 254 `@http:Header {name: "Authorization"}` lines
  (182 of them the same string) are the bulkiest addition and are arguably low-value repetition,
  but they are faithful to the source.
- **Version stability.** `Ballerina.toml` `version = "1.0.2"`, bala `package.json`
  `"version": "1.0.2"`, tag `v1.0.2` — all agree. Distribution `2201.12.0`. Not deprecated on
  Central metadata in the bala. Post-1.0 stable release.
- **Non-compiling render.** Neither render is valid Ballerina (§5.1, §5.4, §5.5). `new` is
  strictly closer to compiling than `old` (it fixes the `source` keyword clash and the 97
  `anydata Additional Values` params) but still would not build.
- **Naming quality is a source-side problem, not a render problem**: OpenAPI-derived names such
  as `SheetssheetIdrowsOneOf21`, `WorkspacesworkspaceIdsharesOneOf2`, `PropertiesTitle` come
  straight from `types.bal`.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders | old 10516, new 10940 |
| 2 | `grep -c '^// Unknown type:'` | old 38, new 0 |
| 3 | `grep -n '^// --- '` both | 4 markers each, same order (README 7 / END 123 / Types 125 / Client 9751 vs 10175) |
| 4 | `ls -R` bala | one module `smartsheet`; `client.bal`, `types.bal`, `utils.bal`; `docs/README.md`; no compiler-plugin |
| 5 | `wc -l` bala sources | client.bal 2585, types.bal 7842, utils.bal 219 |
| 6 | `git ls-remote --tags` | tags v1.0.0, v1.0.1, v1.0.2 → exact tag `v1.0.2` exists |
| 7 | `git clone --depth 1 --branch v1.0.2` | HEAD `32c5b0f1273865db24b166b7a94d13b90989b391` (2026-04-09) |
| 8 | `diff -q src/ballerina/*.bal  bala/modules/smartsheet/*.bal` | "same" for all 3 files |
| 9 | `comm -23/-13` on type-name sets | both empty → 865 names identical old/new |
| 10 | `comm -12 old_unknown.txt new_types.txt` | 38 → every stub is a real type in `new` |
| 11 | Scripted signature compare of the 38 vs `types.bal` | exact-match 38, mismatch 0 |
| 12 | `diff old_methods.txt new_methods.txt` | identical, 185 lines each |
| 13 | `sed 's/anydata Additional Values…/' old_client.txt; diff` vs new_client.txt | empty → client sections identical otherwise |
| 14 | `grep -c 'Additional Values'` | old 97, new 0 |
| 15 | `grep -cE '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 19 lines (171 occurrences per diff md), new 0 |
| 16 | `diff -u` Types sections | 183 removed / 607 added, 3976-line diff |
| 17 | `grep '^-[^-]' \| uniq -c` on that diff | 126 `source?` + 38 stubs + 18 alias lines + 1 Signed32 = 183 |
| 18 | Annotation histograms, bala vs new vs old | table in §3; all match except `@constraint:Number` 10→11 |
| 19 | `grep -n -A1 '@constraint:Number {minValue: 1}'` bala 4 / new 5 | extra one is in `RowResponse` (alias of `GetRowObject`, `types.bal:409`) |
| 20 | `grep -o '@http:Header {name: "…"}' \| uniq -c` bala vs new | identical 7-entry histogram |
| 21 | `grep -cE '^    .* = ' types.bal` vs render Types sections | bala 259 defaults, old 0, new 0 |
| 22 | `grep -c 'record {\|'` | bala 2, new 0 |
| 23 | `grep -c '^public type .* record'` bala / `^type .* record` renders | 771 / 801 / 801 |
| 24 | `grep -c '@deprecated'` in Client sections | old 0, new 0 (bala client.bal has 4) |
| 25 | `grep -c '"?\|'` (malformed optional union) | old 5, new 5; bala has `"folder"\|"home"\|"workspace"?` at types.bal:2655, 5738 |
| 26 | stray unprefixed doc lines after README | old 357, new 357; `diff` of sorted sets = 3 correctly-placed annotation lines only |
| 27 | `diff` lines 1–124 old vs new | empty |
| 28 | `diff` render README vs `docs/README.md` | only a trailing blank line; 114-line README fully present |
| 29 | JSON structural compare | typeDefs 865/865 (name sets equal), clients 1/1, clients[0].functions 185/185, functions/services/annotations 0 |
| 30 | `grep -c '^    resource isolated function '` client.bal | 184 (+1 `init` = 185) |
| 31 | 5 client signatures spot-checked at client.bal:688, 1398, 2350, 2174, 602 | paths / payloads / returns match `new` |
| 32 | bala `package.json` | `export: ["smartsheet"]`, version 1.0.2, ballerina_version 2201.12.0 |

## 10. Caveats and unverified items

- Neither render was compiled. Claims that specific constructs "would not compile" (§5.1, §5.4,
  §5.5, and `source` as a keyword) are based on reading the Ballerina grammar and on the fact
  that the published source itself writes `'source`, not on running `bal build`.
- Doc-*text* fidelity was verified only by structural comparison and by spot-checking individual
  descriptions; I did not diff all 865 types' doc strings character-by-character against
  `types.bal`. The JSON `description` fields for the first type were confirmed identical between
  `old` and `new`, and the Types-section diff accounts for every changed line, so no doc text can
  have been silently altered between the two renders.
- The `@constraint:Number` 10-vs-11 discrepancy is attributed to `RowResponse` alias expansion;
  this is inferred from the line-context analysis (bala hits inside `UpdateRowsObject`, `Row`,
  `AddRowsObject`, `GetRowObject`; render hits inside those four **plus** `RowResponse`) rather
  than from renderer source code, which I did not read.
- Ballerina Central was not re-queried live; package metadata was taken from the bala's
  `package.json` and `Ballerina.toml`, which are authoritative for what the extractor consumed.
- I did not verify the two `ballerina-vscode` commits (`eb5d81b3` / `412ba01e`) themselves; the
  brief's attribution of the two sides is taken as given.

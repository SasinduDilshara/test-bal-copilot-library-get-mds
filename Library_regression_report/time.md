# ballerina/time 2.8.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/time` |
| Pinned version | `2.8.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-time |
| Tag reviewed | `v2.8.1` (commit `63ee601`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/time/2.8.1/java21` |
| Old render | `429` lines |
| New render | `494` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old`. The only lines removed are the five
`// Unknown type:` placeholders (`Error`, `FormatError`, `Seconds`, `Utc`, `TimeZone`);
`new` replaces them with real definitions and additionally fills in the previously empty
`class Zone` body. Nothing present in `old` is missing, truncated, or degraded in `new`.

This matters more than usual for `time`: `time:Utc` and `time:Error` are consumed by
`sql`, `http`, `email`, `graphql` and most connectors. In `old` an LLM reading this render
saw literally `// Unknown type: Utc` with no structure; in `new` it sees
`type Utc readonly & [int, decimal];`, which matches the library source exactly.

Function set and JSON function/typeDef counts are identical on both sides (18 functions,
25 typeDefs) — the change is entirely in how `typeDefs` are populated and rendered.

## 2. Change inventory

Line counts (`wc -l`): old 429, new 494. Diff: 5 lines removed, 70 added, 2 hunks.

Removed from `old` (all placeholders, `diff old new | grep '^<'`):

```
// Unknown type: Error
// Unknown type: FormatError
// Unknown type: Seconds
// Unknown type: Utc
// Unknown type: TimeZone
```

`grep -c '^// Unknown type:'` → old `5`, new `0`.

Declarations added in `new` (top-level decl-set diff):

| Kind | Name | New render line |
|---|---|---|
| type (error) | `Error` | 130 |
| type (error) | `FormatError` | 132 |
| type (alias) | `Seconds` | 136 |
| type (tuple) | `Utc` | 158 |
| class | `TimeZone` | 291 |

Class members added in `new` (9 method declarations, 5 distinct names):

| Class | Methods | New render lines |
|---|---|---|
| `Zone` (was empty `class Zone {}` in old) | `fixedOffset`, `utcFromCivil`, `utcToCivil`, `civilAddDuration` | 273, 277, 281, 286 |
| `TimeZone` (was `// Unknown type: TimeZone`) | `init`, `fixedOffset`, `utcFromCivil`, `utcToCivil`, `civilAddDuration` | 292, 296, 300, 304, 313 |

Declarations removed: **0**. Modified in place: **0** (every other line is byte-identical;
the 5 removals and 70 additions account for the whole diff).

JSON-level inventory (`json.load` on both sides):

- `typeDefs`: 25 both sides; same name set; 6 entries differ — `Error`, `FormatError`,
  `Seconds`, `Utc` gain `baseType`; `Zone` gains `functions`; `TimeZone` gains `"type":"Class"`.
- `functions`: 18 both sides, **byte-identical** (`changed funcs: []`).
- `clients`, `services`, `annotations`: 0 on both sides.
- `readme` and `description`: identical on both sides.
- Version-qualified type refs: `old` JSON contains `"ballerina/time:2.8.1:Error?"` (the
  `TimeZone.init` return type); `new` renders it as `Error?`. Confirms the spec-v2 behaviour
  described in the brief. It never surfaced in the `old` render because `TimeZone` was a
  placeholder there.

## 3. Correctness against library source

The clone at `v2.8.1` and the bala `modules/time/*.bal` are byte-identical
(`diff -r src/ballerina bala/.../modules/time` reports only non-`.bal` extras:
`Ballerina.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `icon.png`, `tests`).
So GitHub and the bala agree; citations below are to the bala paths.

Each thing `new` adds, checked against source:

| New render | Source | Verdict |
|---|---|---|
| `type Error error;` (130) | `time_errors.bal:18` `public type Error error;` | correct |
| `type FormatError error;` (132) | `time_errors.bal:21` `public type FormatError distinct Error;` | **loses `distinct Error`** — see §5.1 |
| `type Seconds decimal;` (136) | `time_types.bal:20` `public type Seconds decimal;` | correct |
| `type Utc readonly & [int, decimal];` (158) + full 20-line doc | `time_types.bal:42` | correct, doc verbatim |
| `Zone.fixedOffset() returns ZoneOffset\|()` (273) | `time_types.bal:218` `public isolated function fixedOffset() returns ZoneOffset?;` | correct (`?` expanded to `\|()`) |
| `Zone.utcFromCivil(Civil civil) returns Utc\|Error` (277) | `time_types.bal:224` | correct |
| `Zone.utcToCivil(Utc utc) returns Civil` (281) | `time_types.bal:231` | correct |
| `Zone.civilAddDuration(Civil, Duration) returns Civil\|Error` (286) | `time_types.bal:239` | correct |
| `TimeZone.init(string\|() zoneId = ()) returns Error?` (292) | `time_types.bal:251` `public isolated function init(string? zoneId = ()) returns Error?` | correct incl. default |
| `TimeZone.fixedOffset/utcFromCivil/utcToCivil/civilAddDuration` (296–313) | `time_types.bal:262, 270, 285, 299` | correct signatures |
| `TimeZone.civilAddDuration` doc keeps the ```ballerina example | `time_types.bal:291–295` | correct, verbatim |

Unchanged-but-verified (identical on both sides): all 18 module-level functions match the
16 `public isolated function`s in `time_apis.bal` plus `loadSystemZone` (`time_types.bal:324`)
and `getZone` (`time_types.bal:334`) — same names, parameters, defaults and return types.
`utcToEmailString(Utc utc, UtcZoneHandling zh = "0")` matches `time_apis.bal:211` including
the `"0"` default.

README in the JSON is byte-identical to `docs/README.md` (3388 chars, both sides).

## 4. Regressions

**None found.**

Basis for that conclusion:

- `diff old new | grep '^<'` returns exactly 5 lines, all `// Unknown type:` placeholders —
  i.e. no real declaration, parameter, default, return type or doc line exists in `old` and
  not in `new`.
- Top-level declaration-set diff shows 0 removals.
- JSON `functions` arrays are equal object-for-object; `typeDefs` name sets are equal and the
  6 changed entries are all supersets of their `old` counterparts (added `baseType` /
  `functions` / `type` keys, nothing dropped).
- The `old`-only renderer patch (`service.methods ?? []`) is irrelevant here: `services` is
  empty on both sides.
- Foundational types other packages depend on (`time:Utc`, `time:Error`, `time:Seconds`,
  `time:Civil`, `time:ZoneOffset`) are all present in `new`, and the first three are present
  **only** in `new`.

## 5. Issues in `new` (independent of `old`)

4 issues, all low severity; none is a regression (each is either inherited from the extractor
on both sides, or exists only because `new` renders content `old` suppressed entirely).

1. **`FormatError` loses its `distinct Error` relationship.** Source is
   `public type FormatError distinct Error;` (`time_errors.bal:21`); `new` emits
   `type FormatError error;`. The JSON root cause is `"baseType": "error"` for both `Error`
   and `FormatError`, so the render cannot show that `FormatError` is a distinct subtype of
   `Error`. An LLM reading this cannot tell that `error FormatError(...)` is catchable as
   `time:Error`, nor that the two types are not interchangeable.
2. **`TimeZone`'s class doc is the constructor's doc.** `new` line 289 shows
   `# Initializes a TimeZone object using a zone ID or the system default time zone.`; the
   actual class doc is `# Localized time zone implementation to handle time zones.`
   (`time_types.bal:243`). The wrong description is already in the `old` JSON, so this is an
   extractor issue on both sides — it just becomes visible for the first time in `new`.
3. **Parameter/return docs are dropped inside class bodies.** `grep -c '# + '` over the
   `Zone`/`TimeZone` block (new lines 268–315) returns `0`, while the module-level function
   section has 39 `# + ` lines. The JSON does carry the per-parameter descriptions (e.g.
   `"civil": "The civil record to be converted"`), so the renderer discards them for class
   methods. Doc loss only, no signature loss.
4. **The emitted class syntax is not valid Ballerina.** `class Zone { function fixedOffset()
   returns ZoneOffset|(); }` — class methods require bodies; only `object` *types* use `;`.
   `Zone` is in fact `public type Zone readonly & object {...}` (`time_types.bal:213`), not a
   class, and `TimeZone` is `public readonly class TimeZone` with `*Zone` inclusion
   (`time_types.bal:244–245`). The render drops `readonly`, `public`, `isolated` and the
   `*Zone` inclusion. This matches the render's general stub style (module-level functions
   are also body-less) so it is unlikely to mislead on semantics, but the block will not
   compile if copied verbatim.

## 6. Coverage gaps vs. the library

The bala exports exactly one module (`package.json` `"export": ["time"]`; `modules/` contains
only `time/`; Central lists a single module). **No submodule-only API**, so the shared
`getDefaultModule()` limitation costs nothing here.

Public symbols in the default module present in **neither** render — **1**:

| Symbol | Source | Note |
|---|---|---|
| `public final ZoneOffset Z = {hours: 0};` | `time_types.bal:148` | Module-level public `final` variable. Absent from both JSONs and both renders (`grep -n 'ZoneOffset Z'` over all four files → no match). The extractor emits `typeDefs`/`functions`/`clients`/`services`/`annotations` only; there is no channel for module-level variables/finals. An LLM will not know `time:Z` exists. |

All 25 other public type definitions, all 8 public `const int` day constants, the
`HeaderZoneHandling` enum and all 18 public functions are present on both sides.

Type-fidelity losses shared by **both** renders (not coverage gaps, but accuracy notes on
foundational types other packages depend on):

- `ZoneOffset`: source is `readonly & record {| int hours; int minutes = 0; decimal seconds?; |}`
  (`time_types.bal:130`). Both renders emit an open `record { int hours; int minutes?; decimal seconds?; }`
  — `readonly`, the closed-record `{| |}`, the `minutes = 0` default (turned into optional) and
  the three field docs are all lost.
- `Duration`: source is a closed record with `= 0` defaults on all 7 fields
  (`time_types.bal:184–199`); both renders show every field as optional `?`. Field docs survive.
- `DayOfWeek`: source `SUNDAY|MONDAY|...|SATURDAY` (`time_types.bal:60`), rendered as
  `0|1|2|3|4|5|6` — semantically equivalent, less readable.
- `HeaderZoneHandling` members are emitted in reverse source order
  (`ZONE_OFFSET_WITH_TIME_ABBREV_COMMENT, PREFER_ZONE_OFFSET, PREFER_TIME_ABBREV` vs source
  `PREFER_TIME_ABBREV, PREFER_ZONE_OFFSET, ZONE_OFFSET_WITH_TIME_ABBREV_COMMENT`); the enum
  member docs (`time_types.bal:203–205`) are dropped. Harmless.
- `Date`/`TimeOfDay`/`Civil` record inclusions (`*DateFields`, `*TimeOfDayFields`, …) are
  correctly flattened into explicit fields on both sides.

## 7. Compiler plugin

`ballerina/time` ships **no compiler plugin**, confirmed twice:

- Bala root `.../2.8.1/java21/` contains only `bala.json`, `dependency-graph.json`, `docs`,
  `modules`, `package.json`, `platform` — no `compiler-plugin/`;
  `find .../2.8.1 -iname '*compiler-plugin*'` returns nothing.
- The `v2.8.1` clone has no `compiler-plugin`/`*-compiler-plugin` directory
  (`find src -maxdepth 2 -iname '*compiler*plugin*'` → no match); the repo is
  `ballerina/` (Ballerina sources) + `native/` (Java native impl) only.

Nothing plugin-implied is therefore expected in the render, and nothing is missing on that
account. The `native/` jar (`platform/java21/time-native-2.8.1.jar`) backs the `external`
functions; those are private (`externTimeZone*`, `time_types.bal:342–369`) and correctly
absent from both renders.

## 8. Other considerations

- Not deprecated: Central `isDeprecated: false`, empty `deprecateMessage`. Stable 2.x
  version. `graalvmCompatible: Yes`. Pull count 37,908.
- Built with `ballerina_version: 2201.12.0` (`package.json`); renders were produced under
  distribution 2201.13.4 — no resolution problem observed.
- Size: 494 lines is small; the +65 lines (+15%) cost is negligible against the value of
  defining `Utc`/`Error`/`Seconds`, which are referenced by name throughout this render's own
  function signatures and by many downstream libraries.
- Doc quality is high on both sides — README is complete and verbatim, and function docs keep
  their ```ballerina examples.
- Multi-line doc continuation lines are emitted without a leading `#` (e.g. new lines 341,
  349, 442–445), so those lines are not comments. Identical on both sides; pre-existing
  renderer behaviour, not introduced by spec v2.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.8.1 …/module-ballerina-time` → `git log -1` / `git describe --tags` | `63ee601`, `v2.8.1` — exact tag exists |
| `wc -l old/ballerina_time.bal.txt new/ballerina_time.bal.txt` | 429 / 494 |
| `grep -c '^// Unknown type:'` old / new | 5 / 0 |
| `diff old new \| grep -c '^<'` / `'^>'` | 5 / 70 |
| `diff old new \| grep '^<'` | only the 5 `// Unknown type:` lines |
| decl-set diff (`grep -oE '^(function\|type\|class\|enum\|const)[^={;]*'`) | +5 (`type Error`, `type FormatError`, `type Seconds`, `type Utc`, `class TimeZone`), −0 |
| JSON `typeDefs`/`functions` lengths | 25/18 both sides |
| JSON `typeDefs` name-set diff | empty both directions |
| JSON changed typeDefs | `Error`, `FormatError`, `Seconds`, `Utc`, `Zone`, `TimeZone` |
| JSON changed functions | none (`[]`) |
| JSON `readme`/`description` equality old vs new | `True` / `True` |
| JSON readme vs `docs/README.md` | identical, 3388 chars |
| regex for `ballerina/…:version:Type` in JSON | old: `ballerina/time:2.8.1:Error?`; new: none |
| `grep -nE '^public ' bala/modules/time/*.bal` | 41 public decls: 21 types/consts/enums/classes + 18 functions + `final ZoneOffset Z` + `Zone`/`TimeZone` |
| `grep -n 'ZoneOffset Z'` across both renders and both JSONs | no match (exit 1) |
| `diff -r src/ballerina bala/.../modules/time` | `.bal` files identical; only non-source extras differ |
| `ls bala/.../2.8.1/java21` + `find … -iname '*compiler-plugin*'` | no `compiler-plugin` |
| `find src -maxdepth 2 -iname '*compiler*plugin*'` | no match |
| `package.json` `export` / `modules/` listing | `["time"]`, single module `time` |
| Central `…/registry/packages/ballerina/time/2.8.1` | `isDeprecated: false`, 1 module, `ballerinaVersion 2201.12.0`, `graalvmCompatible: Yes`, pullCount 37908 |
| `grep -c '# + '` in new class block (lines 268–315) vs whole file | 0 vs 39 |
| Source citations for signature checks | `time_errors.bal:18,21`; `time_types.bal:20,42,148,213,218,224,231,239,243,244,251,262,270,285,299,324,334`; `time_apis.bal:25–271` |

## 10. Caveats and unverified items

- Neither render was compiled or type-checked; the syntax observations in §5.4 are from
  reading the emitted text against the Ballerina grammar, not from running `bal build`.
- I did not re-run either render pipeline; both `.bal.txt`/`.json` pairs were taken as
  produced. Version pinning (`PIN_OK`) was taken from the brief, but is corroborated
  independently: the `Utc` doc block, the `civilAddDuration` example and the `TimeZone`
  signatures in both renders match the 2.8.1 bala exactly.
- The claim in §5.2 that the wrong `TimeZone` description originates in the extractor is
  based on the `old` JSON carrying the same wrong `description`; I did not read the Java
  `ModelToJsonConverter` source to confirm the mechanism.
- `pullCount`/`createdDate` are point-in-time values from Central at review time.

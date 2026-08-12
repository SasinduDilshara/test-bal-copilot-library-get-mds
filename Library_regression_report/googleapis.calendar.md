# ballerinax/googleapis.calendar 3.2.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/googleapis.calendar` |
| Pinned version | `3.2.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-googleapis.calendar |
| Tag reviewed | no `v3.2.1` tag exists — reviewed branch `3.2.0-version` @ `12b274aa` (its `calendar/Ballerina.toml` declares `version= "3.2.1"`; all 7 `.bal` sources are byte-identical to the bala) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/googleapis.calendar/3.2.1/any` |
| Old render | `804` lines (26,783 bytes) |
| New render | `878` lines (31,003 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. The declaration sets are identical (38 record
types, 1 enum, 2 constants, 1 client class with `init` + 10 remote methods, 1 module-level function,
0 services, 0 annotations on both sides). After stripping the added `@display` annotations, the two
renders differ on exactly **two lines** — and on both of those `old` was emitting **malformed,
non-compiling Ballerina**: it lost the `stream<` prefix from two return types
(`returns Calendar, error?>|error`). `new` emits `returns stream<Calendar, error?>|error` correctly.
The defect is present in `old`'s JSON too, so it is an extractor bug that spec v2 fixes, not a
renderer-only artifact.

`new` additionally recovers 108 `@display` annotation occurrences (type fields, record types, the
client class, client methods, and method parameters) that `old` dropped entirely. All 108 match the
library source verbatim.

Nothing was removed, truncated, or degraded. No regressions found.

## 2. Change inventory

| Metric | old | new | Δ |
|---|---|---|---|
| Lines | 804 | 878 | +74 |
| Bytes | 26,783 | 31,003 | +4,220 (+15.8%) |
| JSON bytes | 82,825 | 100,389 | +17,564 (+21.2%) |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| `// --- section ---` markers | 5 | 5 | 0 |
| JSON `typeDefs` | 41 | 41 | 0 |
| JSON `clients` / client methods | 1 / 11 | 1 / 11 | 0 |
| JSON `functions` | 1 | 1 | 0 |
| JSON `services` / `annotations` | 0 / 0 | 0 / 0 | 0 |
| `@display` occurrences | 0 | 108 | +108 |
| `Special Agent Note` external-type hints | 12 | 12 | 0 |

**Declarations added: 0. Declarations removed: 0. Declarations renamed: 0.**
`set(old typeDefs) == set(new typeDefs)` and `set(old client methods) == set(new client methods)`
(verified in Python from both JSONs).

**Modified declarations (2):**

| Method | old return type | new return type |
|---|---|---|
| `Client.getCalendars` | `Calendar, error?>\|error` (malformed) | `stream<Calendar, error?>\|error` |
| `Client.getEvents` | `Event, error?>\|error` (malformed) | `stream<Event, error?>\|error` |

**Additive-only changes (108 `@display` occurrences)** across 17 diff hunks: 1 on the client class
(`{label: "Google Calendar", iconPath: "icon.png"}`), 10 on remote methods, 30 on method parameters,
67 on record fields spread over `ConnectionConfig`, `InputEvent`, `Time`, `Attendee`,
`ConferenceInputData`, `CreateRequest`, `ConferenceSolutionKey`, `Status`, `Reminders`, `Reminder`,
`Source`, `Attachment`, `EventsToAccess`, `CalendarsToAccess`, `EventFilterCriteria`.

Proof of "additive only": stripping `@display` from `new` reduces the whole-file diff against `old`
to the two return-type lines above (command in Evidence log #7).

The README block (lines 7–82) is byte-identical between the two renders.

## 3. Correctness against library source

The bala's `modules/googleapis.calendar/*.bal` are byte-identical to branch `3.2.0-version` of the
upstream repo (all 7 files, `diff -q`, Evidence #12), so upstream and bala agree.

- **Return types.** `endpoints.bal:59` declares
  `@tainted @display {label: "Stream of Calendars"} stream<Calendar,error?>` and `endpoints.bal:183`
  `returns @tainted @display {label: "Stream of Events"} stream<Event,error?>|error`. `new` matches;
  `old` did not.
- **Record fields — exhaustive check.** All 38 `public type … record` definitions in
  `records.bal` were parsed and compared field-by-field against the 38 record blocks in the `new`
  render: **0 missing fields, 0 type mismatches** (Evidence #13). Optional markers and array/union
  forms match; `T?` in source is rendered as `T|()`, which is semantically identical.
- **`ConnectionConfig`** (`records.bal:22-26`) uses `*config:ConnectionConfig;` inclusion. Both
  renders correctly flatten the included fields (`httpVersion`, `http1Settings`, `timeout`, `cache`,
  `retryConfig`, `secureSocket`, … 14 inherited + `auth`) and annotate the foreign types with
  `Special Agent Note` markers naming `ballerina/http` and `ballerinax/client.config`.
- **Client surface.** `endpoints.bal` declares `public isolated function init` (line 37) and 10
  `remote isolated function`s (lines 57, 72, 93, 111, 134, 157, 180, 196, 214, 235). All 11 appear
  in both renders with matching parameter names, order, and defaults.
- **`@display` labels.** The 108 annotation occurrences in `new` were extracted and sorted against
  the 116 in the bala sources: every one of the 108 matches an occurrence in the source verbatim
  (Evidence #9). The 8 not emitted are all *return-type* annotations (see §5.4).
- **Module function.** `prepareUrlWithEventsOptionalParams` (`utils.bal:138`) is rendered with all 5
  parameters and `returns string`, matching the source.

## 4. Regressions

**None found.**

What was checked to conclude that:
1. Declaration-set equality on both JSONs (typeDefs, client methods, functions, services,
   annotations) — all identical, nothing dropped.
2. Full-file diff with `@display` stripped — only the two return-type lines differ, and both changed
   from broken to correct.
3. README/section markers — identical (5 markers on both, README block byte-identical).
4. Docs — every `#` doc line in `old` is present in `new` (falls out of check 2).
5. Parameter defaults — `= ()` defaults preserved on all optional parameters (falls out of check 2).
6. `// Unknown type:` count is 0 on both sides, so no type degraded.

## 5. Issues in `new` (independent of `old`)

All five below are also present in `old` — they are pre-existing pipeline behaviours, not
regressions — but they are inaccuracies a consuming LLM would see in `new`.

1. **Rest fields are mangled into non-compiling syntax (3 occurrences).** `records.bal` declares
   `public type Private record {| string...; |};` (likewise `Shared`, `Preferences`). Both renders
   emit:
   ```
   type Private record {
       # Rest field
       string ;
   };
   ```
   `string ;` is not valid Ballerina, and the closed-record `{| |}` delimiters are lost, changing an
   open-string-map into what reads as an open record with an unnamed field.
2. **Multi-line doc comments lose their `#` prefix (16 lines).** E.g. in `type ConferenceData` the
   continuation lines of the `conferenceId`, `entryPoints`, and `signature` docs are emitted at
   column 0 with no `#`, e.g. `Can be used by developers to keep track of conferences, …`. This both
   breaks compilation and makes the doc text read as top-level content.
3. **Enum values dropped, and enum members leak as invented constants.** Source is
   `public enum OrderBy { START_TIME = "startTime", UPDATED = "updated" }` (`records.bal:690-693`).
   Both renders emit `enum OrderBy { UPDATED, START_TIME }` — associated string values lost and
   member order reversed — *and* separately emit two module-level declarations
   `const string START_TIME = "startTime";` / `const string UPDATED = "updated";` (new render lines
   86, 88) that do not exist as constants in the library. An LLM could emit
   `calendar:START_TIME` expecting a module constant.
4. **Return-type `@display` annotations not emitted (8 occurrences).** The source annotates 8 return
   types (`endpoints.bal:59, 74, 115, 138, 162, 183, 199, 241`, labels `Stream of Calendars`,
   `Calendar`, `Event` ×4, `Stream of Events`, `Events Response`). `new` recovers parameter-,
   field-, method-, and class-level `@display` but not return-level. Cosmetic; no semantic loss.
5. **Qualifiers dropped.** `public`, `isolated`, and `@tainted` are stripped everywhere:
   `public isolated function init` → `function init`; `remote isolated function` → `remote function`;
   `public isolated function prepareUrlWithEventsOptionalParams` → `function …`. Closed records
   `record {| … |}` are rendered as open `record { … }` (`ConnectionConfig`, `Private`, `Shared`,
   `Preferences`). Consistent on both sides.

## 6. Coverage gaps vs. the library

**None.**

The bala exports exactly one module (`package.json` `"export": ["googleapis.calendar"]`, and Central
lists a single module), which *is* the default module — so there is no submodule-only API and no
shared submodule gap for this library.

Public declarations in the default module: 40 (38 `public type` records, `public enum OrderBy`,
`public isolated client class Client`) plus `public isolated function
prepareUrlWithEventsOptionalParams`. Set difference against the render:

- `public` decls absent from the render: **0** (`Client` is carried in the JSON `clients` array, not
  `typeDefs`).
- Render symbols with no `public` counterpart: `START_TIME`, `UPDATED` — the invented constants from
  §5.3, present in both renders.

Non-public internals (`type Error`, `toEvent`, `prepareUrl`, `checkAndSetErrors`, the 49
module-private `const string`s in `constants.bal`, the JWT handler, the stream implementer) are
correctly excluded from both renders.

## 7. Compiler plugin

This package has **no compiler plugin**. `find` over the bala returns no `compiler-plugin` directory
or `compiler-plugin.json`, and the upstream `calendar/` package directory contains none. Nothing the
plugin layer would imply is therefore missing from the render.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/googleapis.calendar/3.2.1` has an empty
  `deprecateMessage`; no deprecation flag. 2,169 pulls. `graalvmCompatible: "Unknown"`.
- **Old distribution.** Built against `ballerina_version: 2201.4.1` (Nov 2024). The current
  major line of this connector is 4.x (`v4.0.1` upstream), which is a full API rewrite; 3.2.1 is a
  maintenance line pinned deliberately here. Not a render concern.
- **Size/token impact.** `new` is 15.8% larger as text and 21.2% larger as JSON, entirely from
  `@display` metadata. For a 878-line render that is cheap, and the labels are genuinely useful
  natural-language names for parameters (`"Token for Incremental Sync"`, `"Filtering Criteria"`).
  Note the inline parameter annotations make some method signature lines very long — the
  `getEventsResponse` line in `new` is a single 460-character line.
- **The `old` render was actively harmful here.** `returns Calendar, error?>|error` would lead a
  model to generate `Calendar|error` handling for a value that is actually
  `stream<Calendar, error?>`. Fixing it is the single most valuable change in this diff.

## 9. Evidence log

1. `wc -l old/… new/…` → 804 / 878. `wc -c` → 26,783 / 31,003.
2. `grep -c '^// Unknown type:'` on both renders → 0 / 0.
3. `grep -n '^// --- '` → 5 markers each; old at 7/82/84/745/794, new at 7/82/84/808/868.
4. Python over both JSONs: `typeDefs` 41/41, `clients` 1/1, `functions` 1/1, `services` 0/0,
   `annotations` 0/0; `set(old typeDefs) - set(new typeDefs) = ∅` and vice versa; client methods
   11/11 with empty symmetric difference.
5. Python return-type comparison over client methods → only `getCalendars` and `getEvents` differ:
   `"Calendar, error?>|error"` → `"stream<Calendar, error?>|error"`, `"Event, error?>|error"` →
   `"stream<Event, error?>|error"`. Confirms the defect originates in the **JSON**, not the renderer.
6. `grep -n 'stream' old/…bal.txt` → 0 hits; on `new` → lines 820, 850.
7. `diff <(grep -v '^\s*@display' old) <(grep -v '^\s*@display' new | sed 's/@display {[^}]*} //g')`
   → exactly 2 differing lines (755, 779), both the stream fix. **No other textual difference.**
8. `diff <(sed -n 1,83p old) <(sed -n 1,83p new)` → identical README block.
9. `grep -oh '@display *{[^}]*}'` sorted: bala 116 occurrences, `new` render 108, `old` render 0.
   `diff` of the sorted lists → the only bala-side extras are 8 return-type annotations
   (`Event` ×4, `Events Response`, `Stream of Calendars`, `Stream of Events`, `Calendar`).
10. `grep -n 'label: "Event"|…' bala/*.bal` → all 8 are on `returns @tainted @display {…}` at
    `endpoints.bal:59, 74, 115, 138, 162, 183, 199, 241`.
11. `git ls-remote --tags` → no `v3.2.1`; `v3.2.0` and `v4.0.0`/`v4.0.1` exist.
    `git ls-remote --heads` → branch `3.2.0-version` @ `12b274aa`;
    `curl …/3.2.0-version/calendar/Ballerina.toml` → `version= "3.2.1"`.
12. `git clone --depth 1 --branch 3.2.0-version …` then `diff -q` for
    `constants.bal, data_mapping.bal, endpoints.bal, jwt_oauth2_handler.bal, records.bal,
    stream_implementer.bal, utils.bal` against the bala module dir → all identical.
    (`v3.2.0` tag differs in `records.bal` only — that is the 3.2.0→3.2.1 delta.)
13. Python field-by-field comparison of all 38 `public type … record` blocks in `records.bal` vs the
    38 `type … record` blocks in the `new` render → 0 missing fields, 0 type mismatches (the one
    `ConnectionConfig` delta the parser flagged is the `*config:ConnectionConfig` inclusion being
    correctly flattened by the render).
14. `grep -n 'function [a-zA-Z]' bala/endpoints.bal` → `init` at 37 and 10 `remote isolated
    function`s at 57/72/93/111/134/157/180/196/214/235 — all 11 present in both renders.
15. `grep -E '^public …' bala/*.bal` → 40 public declarations; Python set difference vs render
    typeDefs+clients → 0 missing; extras `START_TIME`, `UPDATED` only.
16. `find bala -iname '*compiler*'` → no results; `ls src321/calendar` → no compiler-plugin dir.
17. `curl https://api.central.ballerina.io/2.0/registry/packages/ballerinax/googleapis.calendar/3.2.1`
    → `modules: ['googleapis.calendar']`, `deprecateMessage: ''`, `ballerinaVersion: 2201.4.1`,
    `pullCount: 2169`.
18. `grep -c '^\s*string ;$'` → 3 on both renders (`Private`, `Shared`, `Preferences`).
19. `awk 'NR>82 && /^[A-Za-z0-9-]/ && !/^(type|enum|const|client class|function|import|\/\/)/'`
    → 16 unprefixed doc-continuation lines on both renders.
20. `grep -n -A3 '^enum '` on `new` → `enum OrderBy { UPDATED, START_TIME }` (no values);
    `grep -n 'START_TIME'` → also emitted as `const string START_TIME = "startTime";` at line 86.

## 10. Caveats and unverified items

- **No `v3.2.1` git tag exists** upstream. I resolved the exact sources via branch `3.2.0-version`
  (HEAD `12b274aa`), whose `Ballerina.toml` declares `version= "3.2.1"` and whose 7 `.bal` files are
  byte-identical to the bala. The bala was treated as authoritative regardless, per the brief.
- I did not compile either render. Claims that `string ;` and unprefixed doc-continuation lines are
  non-compiling are read off the Ballerina grammar, not from a `bal build` run.
- Whether the `Special Agent Note` external-type comments correctly describe the *contents* of
  `http:CircuitBreakerConfig` etc. was not checked — those types live in dependency packages and
  are out of scope for this library's render.
- The 8 missing return-type `@display` annotations are reported as an omission in `new`; I did not
  verify whether spec v2 intentionally excludes return-level annotations or whether it is an
  oversight — that would require reading the extractor source, which was not in scope.

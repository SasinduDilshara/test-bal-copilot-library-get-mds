# ballerinax/hubspot.crm.obj.tickets 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.tickets` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.tickets |
| Tag reviewed | `v2.0.2` (commit `ecfa8b8322632384265bb1ec1ef8cc6418aa05b3`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.tickets/2.0.2` |
| Old render | `786` lines |
| New render | `787` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small single-module OpenAPI-generated connector (981 lines of `.bal` in the bala: `client.bal` 249, `types.bal` 513, `utils.bal` 219). Both renders cover the full public surface: 42/42 public types and the single `Client` with `init` + 12 resource methods. Neither render contains any `// Unknown type:` placeholder.

`new` differs from `old` in exactly three ways, all improvements:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`, `ballerinax/hubspot.crm.obj.tickets:2.0.2:ValueWithTimestamp`, …) are normalised to plain `int:Signed32` / `ValueWithTimestamp`.
2. The `@display {label: "Connection Config"}` annotation on `ConnectionConfig` is now emitted (it exists in the library source, `types.bal:240`, and was silently dropped by `old`).
3. The bogus pseudo-parameter `anydata Additional Values` — an invalid Ballerina identifier (contains a space) emitted in 4 client resource signatures — is gone.

No declaration, parameter, doc line, return type or README byte was lost. Everything else that is inaccurate in `new` is byte-identical in `old` (shared renderer behaviour, not a regression).

## 2. Change inventory

Line counts: `old` 786, `new` 787 (+1). `diff -u` yields 15 hunks, 16 added / 15 removed lines.

Declaration-set comparison (`grep -oE '^type [A-Za-z0-9_]+' | sort`, diff): **identical**, 42 types on both sides. Section markers: 4 on both (`// --- README ---`, `// --- END README ---`, `// --- Types ---`, `// --- Client ---`). Resource-function count: 12 on both. README block (lines 7–188) byte-identical.

| Kind | Added | Removed | Modified |
|---|---|---|---|
| type (record/enum/union/const/class) | 0 | 0 | 12 (type-reference spelling in 11 fields + 1 annotation added) |
| annotation emitted on a type | 1 (`@display` on `ConnectionConfig`) | 0 | — |
| client resource function | 0 | 0 | 4 (pseudo-param `anydata Additional Values` removed) |
| client `init` | 0 | 0 | 0 |
| README / docs lines | 0 | 0 | 0 |

JSON-level diff (structural, `typeDefs` and `clients` only; `annotations`, `functions`, `services`, `readme`, `description`, `name` byte-identical):

- `typeDefs`: 11 `type.name` values rewritten (7× `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`, 3× `record {|ballerinax/hubspot.crm.obj.tickets:2.0.2:ValueWithTimestamp[]...;|}` → `record {|ValueWithTimestamp[]...;|}`, 1× the same for `CollectionResponseAssociatedId`), plus one new `annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]` entry on `ConnectionConfig`.
- `clients`: 4 parameter objects removed, each `{"name":"Additional Values","description":"Capture key value pairs","optional":true,"type":{"name":"anydata"}}`.

Qualified-reference count (`grep -cE '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:'`): old 11, new 0.

## 3. Correctness against library source

Upstream `v2.0.2` sources are byte-identical to the bala (`diff src/ballerina/client.bal bala/.../client.bal` → identical; same for `types.bal`), so bala and GitHub agree.

Verified for the three changes in `new`:

- `int:Signed32` — source uses the plain lang-library reference, e.g. `types.bal:232` `int:Signed32 'limit = 10;`, `types.bal:302` `int:Signed32 'limit?;`. `new`'s `int:Signed32` matches source spelling; `old`'s `ballerina/lang.int:0.0.0:Signed32` was an internal symbol path that is not valid Ballerina.
- `record {|ValueWithTimestamp[]...;|}` / `record {|CollectionResponseAssociatedId...;|}` — source `types.bal:394` `record {|CollectionResponseAssociatedId...;|} associations?;` and equivalent `ValueWithTimestamp[]` rest-field declarations. `new` matches source exactly.
- `@display {label: "Connection Config"}` — source `types.bal:240`, immediately above `public type ConnectionConfig record {|`. `new` reproduces it verbatim. It is the only `@display` in the module (`grep -n '@display' types.bal` → single hit at 240), so nothing else of this kind is still missing.
- `anydata Additional Values` removal — the 4 affected methods are exactly the 4 that take an included record param in source: `client.bal:47` `post batch/read(... *PostCrmV3ObjectsTicketsBatchReadReadQueries queries)`, `client.bal:67` `get [string ticketId](... *GetCrmV3ObjectsTicketsTicketIdGetByIdQueries queries)`, `client.bal:100` `patch [string ticketId](... *PatchCrmV3ObjectsTicketsTicketIdUpdateQueries queries)`, `client.bal:187` `get .(... *GetCrmV3ObjectsTicketsGetPageQueries queries)`. There is no parameter named "Additional Values" anywhere in the source; the pseudo-param was the extractor's rendering of the open-record rest field (`anydata...`) of those `Queries` records. Its removal makes the signature closer to the source, not further.

Client surface check: all 13 members of `client.bal` (`init` + 12 resources at lines 31, 47, 67, 84, 100, 118, 135, 152, 169, 187, 203, 220, 237) appear in both renders with matching path segments, payload types and return unions.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Declaration name sets are identical (`diff` of sorted `^type <Name>` lists → no output; 42 = 42).
- The complete `diff -u old new` is 15 hunks and was read in full; every hunk is one of the three improvement categories above. No hunk removes a field, a doc comment, a return type, a default value, or a README line.
- README region (lines 7–188) diffs clean.
- `// Unknown type:` count: 0 in old, 0 in new — no degradation in either direction here (this library never had degraded types).
- The only *content* removed anywhere is the `Additional Values` pseudo-parameter, which was malformed (space in identifier → non-compiling) and named nothing that exists in the library. Its loss carries one small piece of true information — that the `*Queries` records are open (`record {`, not `record {|`) and so accept extra key-value pairs — but that information was already conveyed misleadingly, and the corresponding `Queries` type definitions in the Types section never expressed openness in either render, so nothing that was correct in `old` became wrong in `new`.

## 5. Issues in `new` (independent of `old`)

All five below are byte-identical in `old`; they are shared renderer behaviour, listed because they are inaccuracies an LLM consuming `new` would inherit.

1. **Record-field defaults dropped and defaultable fields marked optional.** Source `types.bal:226` `boolean archived = false;` and `types.bal:232` `int:Signed32 'limit = 10;` render (new line 526/530) as `boolean archived?;` / `int:Signed32 'limit?;`. Same across `ConnectionConfig`: `timeout = 30` → `decimal timeout?;` (new:550), `validation = true` → `boolean validation?;` (new:576), `httpVersion = http:HTTP_2_0` → `http:HttpVersion httpVersion?;` (new:544). No `= ` default survives on any record field.
2. **Closed records rendered as open.** Source has 3 closed top-level records (`types.bal:183` `OAuth2RefreshTokenGrantConfig`, `:241` `ConnectionConfig`, `:500` `ApiKeysConfig`, all `record {|…|}`); all 42 rendered types use `record {` (`grep -c '^type .* record {$'` → 42). Inline closed records are preserved, so this is specific to top-level type defs.
3. **Client query parameters both flattened and duplicated, with invented defaults.** e.g. new:774 `resource function get (…, string[] associations = [], boolean archived = false, string[] propertiesWithHistory = [], int:Signed32 limit = 0, string after = "", string[] properties = [], GetCrmV3ObjectsTicketsGetPageQueries queries)`. Source has a single `*GetCrmV3ObjectsTicketsGetPageQueries queries` included param. The flattened defaults contradict the source: `associations`/`properties`/`propertiesWithHistory`/`after` are optional with **no** default, `idProperty` likewise, and `'limit`'s real default is **10**, not `0`. Additionally the record param `queries` appears *after* defaulted params without `*` and without a default, which is invalid Ballerina parameter ordering.
4. **Empty resource paths rendered as nothing.** Source `resource isolated function get .(…)` and `post .(…)` (client.bal:187, 203) render as `resource function get (` / `resource function post (` (new:774, 778) — the `.` path segment is lost, so the call form `client->/.get()` is not recoverable and the line does not parse.
5. **Qualifiers stripped.** `public isolated function init` → `function init`; every `resource isolated function` → `resource function`; every `public type` → `type` (`grep -c isolated` on the new render → 0). The render is therefore descriptive rather than compilable.

## 6. Coverage gaps vs. the library

**None.** The package has exactly one module (`bala/any/modules/` lists only `hubspot.crm.obj.tickets`; Central metadata lists a single module), so the default-module-only extraction loses nothing here.

- Public types in bala `types.bal`: 42 (`grep -oE '^public type [A-Za-z0-9_]+'`). Types in `new` render: 42. `comm -23` (source-only) → empty; `comm -13` (render-only, i.e. invented symbols) → empty.
- No other public declarations exist in the module: `grep -nE '^public (const|enum|class|function|isolated function|listener|annotation)' *.bal` → no matches. `utils.bal` contains only module-private helpers.
- The `Client` class and all 12 resource methods + `init` are present.

## 7. Compiler plugin

None. `find` over the upstream `v2.0.2` clone for `*compiler-plugin*` → no matches; the bala contains no `compiler-plugin/` directory (`ls bala/2.0.2/any/` → `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`). Nothing plugin-derived is therefore expected in, or missing from, the render.

## 8. Other considerations

- Not deprecated (Central: `deprecated: None`, empty `deprecateMessage`). Built with Ballerina `2201.12.2`; `Ballerina.toml` declares `distribution = "2201.12.0"`. Pull count 24 — low-traffic connector.
- Stable 2.x version; no pre-1.0 instability caveat.
- Size impact is negligible: +1 line, and `new` is slightly cheaper per token because 11 long qualified type paths collapsed to short names.
- Doc quality is good: every rendered record field and every client method carries the source's doc comment; README (182 lines) is carried verbatim including setup steps and quickstart.
- The render remains non-compiling Ballerina for the reasons in §5 (items 3–5) — unchanged from `old`, but worth knowing if these renders are ever fed to a compiler rather than an LLM.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/new .bal.txt` | 786 / 787 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `diff -u old new` (read in full) | 15 hunks, +16 / −15 lines |
| `diff <(grep -oE '^type [A-Za-z0-9_]+' old\|sort) <(… new\|sort)` | no output (identical 42-type sets) |
| `grep -n '^// --- ' new` | lines 7, 188, 190, 735 — 4 markers, same as old |
| `grep -c 'resource function'` old / new | 12 / 12 |
| `grep -cE '[a-z]+/[a-z._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 11 / 0 |
| `grep -c '^@' ` old / new | 0 / 1 (`@display {label: "Connection Config"}`, new:539) |
| `diff <(sed -n '7,188p' old) <(sed -n '7,188p' new)` | identical README |
| Python structural JSON diff of `typeDefs` | 11 `type.name` rewrites + 1 annotations block added |
| Python structural JSON diff of `clients` | 4 `Additional Values` param objects removed; nothing else |
| Python JSON top-level key compare | only `typeDefs` and `clients` differ; `annotations`/`functions`/`services`/`readme`/`description`/`name` identical |
| `git ls-remote --tags <repo>` | `v1.0.0`, `v2.0.0`, `v2.0.1`, `v2.0.2` (`v2.0.2^{}` = `ecfa8b8`) |
| `git clone --depth 1 --branch v2.0.2` | succeeded |
| `diff src/ballerina/client.bal bala/.../client.bal` | identical |
| `diff src/ballerina/types.bal bala/.../types.bal` | identical |
| `wc -l bala/.../{client,types,utils}.bal` | 249 / 513 / 219 |
| `grep -n 'resource function\|isolated function' bala client.bal` | 13 members at lines 31,47,67,84,100,118,135,152,169,187,203,220,237 |
| `grep -oE '^public type …' types.bal \| wc -l` | 42 |
| `comm -23 src_types new_types` / `comm -13` | both empty |
| `grep -nE '^public (const\|enum\|class\|function\|isolated function\|listener\|annotation)' bala/*.bal` | no matches |
| `grep -n '@display' bala types.bal` | single hit, line 240 |
| `grep -nE '^public type … record \{\|' types.bal` | lines 183, 241, 500 (3 closed records) |
| `grep -c '^type .* record {$' new` | 42 (all rendered open) |
| `sed -n '223,240p' types.bal` vs `sed -n '516,540p' new` | `archived = false` → `archived?`; `'limit = 10` → `'limit?` |
| `ls bala/2.0.2/any/`, `find src -iname '*compiler-plugin*'` | no compiler plugin |
| `ls bala/.../modules/` + Central `modules` field | single module `hubspot.crm.obj.tickets` |
| `curl api.central.ballerina.io/.../2.0.2` | `deprecated: None`, `ballerinaVersion: 2201.12.2`, pullCount 24 |

## 10. Caveats and unverified items

- The renders were not re-generated; this audit compares the supplied artefacts. The claim that both sides used the same library version is corroborated indirectly — `old` embeds `ballerinax/hubspot.crm.obj.tickets:2.0.2:` in 11 type refs, matching the pinned bala — but the pipeline runs themselves were not reproduced.
- The rendered signatures were not fed to a Ballerina compiler; the "non-compiling" judgements in §5 (space-containing identifier, missing `.` resource path, required param after defaulted params) are from the language rules, not from a compiler run.
- `utils.bal` was checked only for public declarations (none); its private helper logic was not reviewed since it cannot surface in the render.

# ballerinax/aws.secretmanager 0.4.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.secretmanager` |
| Pinned version | `0.4.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.secretmanager |
| Tag reviewed | `v0.4.1` (annotated tag `76bf9fe`, exact match) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.secretmanager/0.4.1` |
| Old render | `459` lines |
| New render | `471` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module connector (4 `.bal` files, 529 lines). The upstream tag `v0.4.1` is byte-identical
to the bala's `modules/aws.secretmanager/*.bal` (all four files `diff -q` clean), so there is no
GitHub-vs-bala ambiguity for this library.

The `old` → `new` delta is 7 hunks, +17/−5 lines, and is entirely spec-v2 improvement:

- 3 `// Unknown type:` placeholders (`Error`, `SecretId`, `FilterValue`) replaced by real definitions.
- 2 version-qualified type refs (`ballerinax/aws.secretmanager:0.4.1:...`) normalised to plain names.
- 9 `@constraint:*` annotations newly surfaced (2 on type definitions, 7 on record fields), all
  verbatim-correct against source.

Nothing was removed or degraded. Declaration sets, README (2,106 chars, byte-identical), and the
5 client functions are otherwise identical between the two sides.

## 2. Change inventory

Mechanical (`diff -u old new`): 7 hunks, 17 lines added, 5 lines removed.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` lines | 3 | 0 |
| Version-qualified type refs (`mod:0.4.1:Type`) | 2 | 0 |
| `// --- ` section markers | 4 (README/END README/Types/Client) | 4 (same) |
| `@constraint:` annotation lines | 0 | 9 |
| JSON `typeDefs` | 66 | 66 |
| JSON client functions | 5 (`Client`) | 5 (`Client`) |
| JSON top-level `functions` / `services` / `annotations` | 0 / 0 / 0 | 0 / 0 / 0 |

**Declarations added (3)** — all previously degraded to `// Unknown type:`:

| Name | New render |
|---|---|
| `Error` | `type Error error<ErrorDetails>;` + doc |
| `SecretId` | `type SecretId string;` + doc + `@constraint:String` |
| `FilterValue` | `type FilterValue string;` + doc + `@constraint:String` (regex pattern) |

**Declarations removed: 0.** The JSON `typeDefs` name sets are identical (66 = 21 public types/enums/consts
plus the 42 `Region` and 3 `StagingStatus` enum members hoisted as `const string`, minus overlap; verified
by set comparison in Python — zero symmetric difference).

**Declarations modified (2 in render text, 2 in JSON):**

| Location | old | new |
|---|---|---|
| `DescribeSecretResponse.versionToStages` | `map<ballerinax/aws.secretmanager:0.4.1:StagingStatus[]>` | `map<StagingStatus[]>` |
| `Client.init` return | `ballerinax/aws.secretmanager:0.4.1:Error?` | `Error?` |

**Annotations added (9), by owner:**

| Owner | Annotation |
|---|---|
| `SecretId` (type) | `@constraint:String` minLength 1 / maxLength 2048 |
| `FilterValue` (type) | `@constraint:String` pattern `^!?[a-zA-Z0-9 :_@/+=.\-!]{0,512}$` |
| `SecretVersionSelector.versionId` | `@constraint:String` 32 / 64 |
| `SecretVersionSelector.versionStage` | `@constraint:String` 1 / 256 |
| `BatchGetSecretValueRequest.filters` | `@constraint:Array` maxLength 10 |
| `BatchGetSecretValueRequest.maxResults` | `@constraint:Int` 1 / 20 |
| `BatchGetSecretValueRequest.nextToken` | `@constraint:String` 1 / 4096 |
| `BatchGetSecretValueRequest.secretIds` | `@constraint:Array` 1 / 20 |
| `SecretValueFilter.values` | `@constraint:Array` 1 / 10 |

JSON-level: `Error` gained `"baseType": "error<ErrorDetails>"`; `SecretId` and `FilterValue` gained
`"baseType": "string"` plus `annotations` arrays; 5 record fields gained `annotations` arrays.

Unchanged kinds: functions (0 module-level), services (0), listeners (0), module-level annotations (0),
client count (1), client method count (5).

## 3. Correctness against library source

Every added/changed item was checked against the bala (== upstream `v0.4.1`).

| New render | Source | Result |
|---|---|---|
| `type Error error<ErrorDetails>;` | `errors.bal:18` `public type Error distinct error<ErrorDetails>;` | detail type correct; `distinct` and `public` dropped (see §5) |
| `type SecretId string;` + constraint | `types.bal:95–105` | exact match, incl. both messages |
| `type FilterValue string;` + regex constraint | `types.bal:308–314` | exact match, regex and message byte-identical |
| `SecretVersionSelector` field constraints | `types.bal:194–213` | exact match (32/64, 1/256) |
| `BatchGetSecretValueRequest` field constraints | `types.bal:238–281` | exact match (Array 10; Int 1/20; String 1/4096; Array 1/20) |
| `SecretValueFilter.values` constraint | `types.bal:291–300` | exact match (1/10) |
| `map<StagingStatus[]> versionToStages?` | `types.bal` `DescribeSecretResponse` | `StagingStatus` is the real enum (`types.bal:180`); de-qualification correct |
| `init(...) returns Error?` | `client.bal:38` `public isolated function init(*ConnectionConfig configs) returns Error?` | return type correct |

These constraints are **not decorative**: `client.bal:17` imports `ballerina/constraint` and lines 58, 81,
85, 108 call `constraint:validate(...)` on `secretId`, `versionSelector`, and `request`. Violating any
surfaced bound is a runtime error, so exposing them to an LLM is materially valuable.

Coverage cross-check of everything else (unchanged between sides, still verified):

- 21 `public type`/`enum`/`const` declarations in source; all 21 appear in both renders by name.
- `enum Region`: 42 members in source (`types.bal:29–76`), 42 in the render's `enum Region` body and
  42 matching `const string` lines.
- `enum StagingStatus`: 3 members in source, 3 in render.
- `Client`: `init`, `describeSecret`, `getSecretValue`, `batchGetSecretValue`, `close` — all 5 present,
  matching `client.bal:38, 57, 80, 107, 133`.

## 4. Regressions

**None found.**

What was checked to conclude this:

- Full `diff -u` of the two renders read line by line (only 7 hunks; every one is an addition or a
  de-qualification, no content deleted). The 5 removed lines are exactly the 3 `// Unknown type:`
  placeholders and the 2 version-qualified lines that were replaced.
- JSON `typeDefs` name sets compared as sets: identical (66/66, no additions, no deletions).
- Per-typeDef JSON deep comparison: only 7 typeDefs differ, and every difference is *additive*
  (`baseType`, `annotations`) or a de-qualification — no field, doc string, type name, or `optional`
  flag lost.
- Per-client-function JSON deep comparison of all 5 functions: the only difference anywhere is
  `init`'s return type string losing the `ballerinax/aws.secretmanager:0.4.1:` prefix. Parameter
  lists, defaults, and docs are byte-identical.
- README section: `old['readme'] == new['readme']` → `True`, 2,106 chars both sides; 4 section
  markers on both sides at the same relative positions.
- No new `// Unknown type:` lines in `new` (0).

## 5. Issues in `new` (independent of `old`)

These are inaccuracies present in `new`. Only N1 and N5 are introduced by the new content; N2, N3, N4,
N6, N7 are pre-existing renderer behaviour shared with `old` (so not regressions), listed here because
§5 asks for what is wrong in `new` regardless of `old`.

**N1. `distinct` dropped from `Error`.** Source `errors.bal:18` is
`public type Error distinct error<ErrorDetails>;`; `new` line 190 renders `type Error error<ErrorDetails>;`.
An LLM cannot infer that this is a distinct error type (matters for `is`/`error` narrowing and for
`Error` vs `constraint:Error` discrimination). New content, so a fidelity gap in the improvement rather
than a regression.

**N2. Closed records rendered as open.** All 13 record types in the library are closed
(`grep -c 'record {|'` → 12 in `types.bal` + 1 in `errors.bal` = 13). The render emits 13 open
`record {` and 0 `record {|`. This tells an LLM that extra rest fields are allowed, which they are not.
Shared with `old`.

**N3. Included-record parameters flattened *and* duplicated, with invented defaults.** Source signatures
use included-record params (`*ConnectionConfig`, `*SecretVersionSelector`, `*BatchGetSecretValueRequest`).
The render emits both the expanded fields and the record itself, e.g. `new` line 463:

```
remote function batchGetSecretValue(SecretValueFilter[] filters = [], int maxResults = 0, string nextToken = "", SecretId[] secretIds = [], BatchGetSecretValueRequest request) returns BatchGetSecretValueResponse|Error;
```

This does not compile (required param after defaultable, duplicated data), and the fabricated defaults
now directly contradict the constraints `new` just added: `int maxResults = 0` violates
`@constraint:Int { minValue: 1 }`, `string versionId = ""` (in `getSecretValue`) violates
`@constraint:String { minLength: 32 }`, and `SecretId[] secretIds = []` violates
`@constraint:Array { minLength: 1 }`. Shared with `old`, but spec v2 makes the contradiction visible.

**N4. Doc-comment continuation lines lose their `#` prefix.** 3 lines in `new`
(381: `in the response, Secrets Manager includes ...`, 382: `you must also use the ...`,
386: `if a previous call did not show all results`) sit inside a record body with no `#`, which is
malformed Ballerina. Same 3 lines in `old`. Root cause: source doc comments at `types.bal:244–246`
and `259–260` are multi-line and the extractor keeps the embedded `\n`.

**N5. `@constraint:*` annotations used without an import.** The render's only import is
`import ballerinax/aws.secretmanager;` (line 5; line 35 is inside the README code fence). The 9 new
annotations reference the `constraint` prefix with no `import ballerina/constraint;`, so the emitted
snippet is not self-contained. New in `new`.

**N6. `isolated` / `public` qualifiers dropped.** Source: `public isolated client class Client`
(`client.bal:21`) and `isolated remote function` on all 4 methods. Render: `client class Client` and
`remote function`. Also every `public type` renders as bare `type`. Uniform renderer convention,
shared with `old`.

**N7. Enum member values dropped inside the enum body.** `enum Region { US_WEST_2, ... }` omits the
`= "us-west-2"` values that source carries; they are recoverable only from the separately hoisted
`const string US_WEST_2 = "us-west-2";` lines. Shared with `old`. Also note the render's `close()`
returns `Error|()` rather than `Error?` — semantically equivalent, cosmetically odd, shared.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module — `modules/aws.secretmanager/` — and Central metadata
lists exactly one module for `0.4.1`. There is therefore **no submodule-only API**, so the shared
`getDefaultModule()` limitation described in the brief does not apply to this library.

All 21 `public` declarations from the default module plus the `Client` class and its 5 functions appear
in both renders (checked by grepping `^public (type|enum|const|isolated client class)` across the four
bala `.bal` files and matching each name in the render). Nothing exported is absent from `new`.

Non-public symbols correctly absent: `init.bal:19` `function init()` (module init, not public).

## 7. Compiler plugin

**The package ships no compiler plugin.** There is no `compiler-plugin/` directory in the bala
(`ls .../0.4.1/java21/compiler-plugin` → No such file or directory) and no `*compiler*plugin*` path in
the upstream tree at `v0.4.1` (`find -ipath '*compiler*plugin*' -maxdepth 3` → empty). `native/` holds
only the JNI implementation (`native/src`, `build.gradle`, `spotbugs-exclude.xml`). `Ballerina.toml`
declares no `[[plugin]]` section.

Validation is therefore *not* plugin-driven: it is runtime `constraint:validate()` inside the connector
(`client.bal:58, 81, 85, 108`), backed by `ballerina/constraint`'s own plugin. This means the constraint
metadata that spec v2 now surfaces is precisely the information an LLM needs, and nothing a plugin
implies is missing from the render.

## 8. Other considerations

- **Pre-1.0 version.** `0.4.1` is an unstable release (5 tags: v0.1.0 … v0.4.1). Not deprecated —
  Central returns an empty `deprecateMessage`. `pullCount` 27, published 2026-04-08, `graalvmCompatible: Yes`,
  built for distribution `2201.11.0`.
- **Size/token impact is negligible**: +12 lines (+2.6%), 459 → 471. The 9 annotation lines are long
  (up to ~230 chars) so the token increase is somewhat larger than the line count suggests, but this is
  clearly a good trade for constraints that are enforced at runtime.
- **Doc quality nit in the library itself (not the renderer):** `DescribeSecretResponse`'s doc string is
  `"Represents the results retrieved from \`GetEntitlements\` operation."` — a copy-paste from the AWS
  Marketplace connector; the correct operation is `DescribeSecret`. Present verbatim in `types.bal:107`,
  so both renders faithfully reproduce a wrong doc. Worth an upstream issue, not a render finding.
- **Neither render is compilable Ballerina** (N3, N4, N5). That is a pre-existing property of this
  pipeline, not specific to this library.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 459 / 471 |
| `grep -c '^// Unknown type:'` old / new | 3 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each, lines 7/68/70/424 (old) and 7/68/70/436 (new) |
| `diff -u old new` | 7 hunks; `grep -c '^+[^+]'` = 17, `grep -c '^-[^-]'` = 5 |
| `ls -R` bala | single module `modules/aws.secretmanager` (client.bal, errors.bal, init.bal, types.bal); no `compiler-plugin/` |
| `wc -l` bala module | client 137, errors 30, init 25, types 337 = 529 |
| `git ls-remote --tags <repo>` | v0.1.0, v0.2.0, v0.2.1, v0.3.0, v0.4.0, **v0.4.1** |
| `git clone --depth 1 --branch v0.4.1` + `git describe --tags` | `v0.4.1`, HEAD `76bf9fe` |
| `diff -q ballerina/<f>` vs bala for all 4 `.bal` | all "same" — upstream == bala |
| `find . -ipath '*compiler*plugin*' -maxdepth 3` in upstream | no matches |
| `cat errors.bal` | `errors.bal:18` `public type Error distinct error<ErrorDetails>;` → confirms N1 |
| `sed -n '90,120p;185,320p' types.bal` | all 9 constraint blocks read verbatim; match `new` exactly |
| `grep -nE '^public (type\|isolated \|function\|class\|const\|enum\|annotation)' *.bal` | 21 public types/enums/consts + `public isolated client class Client` |
| `grep -nE 'remote function\|function init' client.bal init.bal` | 5 client members at client.bal:38,57,80,107,133; module `init()` at init.bal:19 (non-public) |
| Python set-compare of JSON `typeDefs` names | 66 == 66, identical sets |
| Python deep-compare of `typeDefs` | 7 differ: BatchGetSecretValueRequest, DescribeSecretResponse, Error, FilterValue, SecretId, SecretValueFilter, SecretVersionSelector — all additive/de-qualifying |
| Python deep-compare of 5 client functions | only `init` return type differs (prefix removal) |
| `old['readme'] == new['readme']` | `True`, 2106 chars both |
| `old['description'] == new['description']` | `True` |
| `old['annotations']`, `new['annotations']` | `[]`, `[]` |
| `grep -c 'record {|'` bala | 13 closed records (12 types.bal + 1 errors.bal) |
| `grep -c 'record {$'` / `'record {|'` in new render | 13 / 0 → confirms N2 |
| `grep -n '^import' new render` | lines 5 and 35 (35 inside README fence); `grep -c '@constraint:'` = 9 → confirms N5 |
| `grep -nE '^(in the response\|you must also\|if a previous)'` new / old | 3 lines (381, 382, 386) / 3 → confirms N4, shared |
| Region enum member count: source `sed -n '29,76p' \| grep -c` vs render enum body | 42 / 42 |
| StagingStatus members source vs render | 3 / 3 |
| `grep -n 'constraint:validate' client.bal` | lines 58, 81, 85, 108 → constraints enforced at runtime |
| Central `GET /2.0/registry/packages/ballerinax/aws.secretmanager/0.4.1` | 1 module, ballerinaVersion 2201.11.0, graalvmCompatible Yes, empty deprecateMessage, pullCount 27 |
| Precomputed diff md cross-check | its 459/471, +17/−5, 7 hunks, 3 added decls, 3→0 Unknown, 2→0 qualified refs all reproduced independently — accurate |

## 10. Caveats and unverified items

- Neither render was fed to `bal build`, so "does not compile" claims (N3, N4, N5) are read off the
  Ballerina grammar rather than a compiler run. The specific defects (required param after defaultable,
  `#`-less doc continuation inside a record body, unimported annotation prefix) are unambiguous, but the
  full-file compile status is unverified.
- The two renderer commits (`eb5d81b3` / `412ba01e`) were not inspected; the attribution of each change
  to spec v2 rests on the brief plus the observed diff shape, not on reading renderer code.
- `PIN_OK` at `0.4.1` for both sides is taken from the brief; independently, both JSONs describe the
  same 66 typeDefs and the bala present on disk is `0.4.1` only, which is consistent with it.
- The `native/src` Java implementation was not read. It cannot affect the render (the extractor reads
  Ballerina declarations only), but if a runtime behaviour contradicted a Ballerina doc string, this
  review would not catch it.
- The `DescribeSecretResponse` "GetEntitlements" doc error is asserted from the source text; whether AWS
  Secrets Manager has some operation by that name was not researched (it does not appear in this
  connector's 4 API methods).

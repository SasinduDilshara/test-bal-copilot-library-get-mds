# ballerinax/aws.redshiftdata 1.1.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.redshiftdata` |
| Pinned version | `1.1.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.redshiftdata |
| Tag reviewed | `v1.1.0` (annotated → `6e009b46f100b12f6efc74d968fab38b84a87e8b`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.redshiftdata/1.1.0/java21` |
| Old render | `531` lines |
| New render | `540` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, entirely positive delta. `new` is +9 lines over `old`, across 9 diff hunks, all confined to
the `Types` and `Client` sections. It (a) replaces all 3 `// Unknown type:` placeholders with real
definitions (`Error`, `SessionId`, `StatementId`), (b) surfaces 6 `@constraint:*` annotations that
`old` dropped entirely, (c) fixes the field name `error` → `'error` (quoted identifier — `error` is
a reserved word, so `old`'s form does not compile), and (d) removes the 2 version-qualified type
refs `ballerinax/aws.redshiftdata:1.1.0:Error`. Every one of these changes was checked against the
bala source and matches it. No declaration was removed, no signature narrowed, no doc text lost
(README byte-identical, 8387 chars both sides). The remaining defects in `new` (dropped `distinct`,
open-record rendering, mangled `typedesc` param, fabricated included-record-param defaults,
unprefixed doc continuation lines) are all present in `old` too, except the `distinct` loss which
is new only because `old` emitted nothing at all for `Error`.

The library is single-module (`modules/aws.redshiftdata` only), has no compiler plugin, and exports
16 public symbols from its default module — all 16 are present in both renders (3 of them as bare
placeholders in `old`).

## 2. Change inventory

Line counts (`wc -l`): old **531**, new **540**. Sections (`grep -n '^// --- '`): 4 markers on both
sides (`README`, `END README`, `Types`, `Client`) — no section added or lost.

JSON-level (both files, `typeDefs`/`clients`/`functions`/`services`/`annotations`):

| | old | new |
|---|---|---|
| `typeDefs` | 64 | 64 |
| `clients` | 1 | 1 |
| `functions` / `services` / `annotations` | 0 / 0 / 0 | 0 / 0 / 0 |
| `readme` length (chars) | 8387 | 8387 (identical) |
| `description` | identical | identical |

`typeDefs` name sets are **identical** — nothing added, nothing removed. 7 typeDefs changed content:
`Cluster`, `DescriptionResponse`, `Error`, `ExecutionConfig`, `SessionId`, `StatementId`, `WorkGroup`.
The `clients` block changed in exactly 2 places (both return-type strings).

### Declarations gaining a real body in `new` (3)

| Symbol | old | new |
|---|---|---|
| `Error` | `// Unknown type: Error` | `type Error error<ErrorDetails>;` (JSON gains `"baseType": "error<ErrorDetails>"`) |
| `SessionId` | `// Unknown type: SessionId` | `type SessionId string;` + `@constraint:String` (JSON gains `baseType`, `annotations`) |
| `StatementId` | `// Unknown type: StatementId` | `type StatementId string;` + `@constraint:String` (JSON gains `baseType`, `annotations`) |

`grep -c '^// Unknown type:'` → old **3**, new **0**.

### Annotations recovered in `new` (6, all `ballerina/constraint`)

`grep -c '@constraint:'` → old **0**, new **6**.

| Location | Annotation |
|---|---|
| `Cluster.id` | `@constraint:String { minLength 1, maxLength 63 }` |
| `Cluster.sessionKeepAliveSeconds` | `@constraint:Int { minValue 0, maxValue 86400 }` |
| `WorkGroup.sessionKeepAliveSeconds` | `@constraint:Int { minValue 0, maxValue 86400 }` |
| `ExecutionConfig.statementName` | `@constraint:String { minLength 1, maxLength 500 }` |
| `SessionId` (type-level) | `@constraint:String { pattern: re \`^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d+)?$\` }` |
| `StatementId` (type-level) | `@constraint:String { pattern: re \`^[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d+)?$\` }` |

### Modified declarations (3)

| Symbol | old | new |
|---|---|---|
| `StatementData.error` / `DescriptionResponse` (JSON field name) | `string error?;` | `string 'error?;` |
| `Client.init` return | `ballerinax/aws.redshiftdata:1.1.0:Error?` | `Error?` |
| `Client.getResultAsStream` return | `stream<rowTypes, ballerinax/aws.redshiftdata:1.1.0:Error?>|Error` | `stream<rowTypes, Error?>|Error` |

Version-qualified refs: old **2**, new **0**.

### Declarations removed in `new`

**None.** Verified by set-diff of `typeDefs` names (empty both directions) and by the fact that the
`Client` JSON diff contains only the two return-string edits above.

## 3. Correctness against library source

Bala vs. upstream tag `v1.1.0`: `diff -q` on all 5 `.bal` files (`client.bal`, `errors.bal`,
`init.bal`, `result_iterator.bal`, `types.bal`) → **no differences**. So GitHub and the bala agree;
citations below use bala paths, which are byte-identical to `ballerina/*.bal` at the tag.

| `new` renders | Source | Verdict |
|---|---|---|
| `type Error error<ErrorDetails>;` | `errors.bal:18` `public type Error distinct error<ErrorDetails>;` | correct base type; `distinct` dropped (see §5) |
| `type ErrorDetails record { int httpStatusCode?; string httpStatusText?; string errorCode?; string errorMessage?; }` | `errors.bal:21-30` | fields, types, optionality all match |
| `type SessionId string;` + pattern constraint | `types.bal:158-164` | annotation text and regex match character-for-character |
| `type StatementId string;` + pattern constraint | `types.bal:205-211` | matches, including the `message`-before-`value` key order of the source |
| `Cluster.id` constraint (1..63, cluster-ID messages) | `types.bal:107-117` | matches |
| `Cluster.sessionKeepAliveSeconds` constraint (0..86400) | `types.bal:121-131` | matches |
| `WorkGroup.sessionKeepAliveSeconds` constraint (0..86400) | `types.bal:144-154` | matches |
| `ExecutionConfig.statementName` constraint (1..500) | `types.bal:177-187` | matches |
| `string 'error?;` in `StatementData` | `types.bal:242` `string 'error?;` | **`new` is right, `old` was wrong** — source uses the quoted identifier |
| `Client` remote methods: `execute`, `batchExecute`, `getResultAsStream`, `describe`, `close` + `init` | `client.bal:44, 68, 94, 125, 137, 158` | all 6 present, names and ordering match |
| `enum Status { ALL, FAILED, ABORTED, FINISHED, STARTED, PICKED, SUBMITTED }` | `types.bal:261-269` | all 7 members present (order differs from source; no semantic impact) |
| `DescriptionResponse` fields incl. flattened `*StatementData` members | `types.bal:218-226` + `238-250` | inclusion flattened inline; all 11 inherited + 3 own fields present |

Nothing in `new` is invented: every symbol in the render maps to a source declaration.

## 4. Regressions

**None found.**

What I checked to conclude that:

- Full `diff -u old new` (9 hunks, +15/−6 lines) — every hunk reviewed individually above; none
  removes a declaration, a parameter, a default, a return type, or a doc line.
- `typeDefs` name set-difference in both JSONs: `only old = set()`, `only new = set()`.
- `clients` JSON unified diff: exactly 2 changed lines, both de-qualifying `Error`.
- `readme` field equality: `True`, identical lengths (8387).
- `description` field equality: `True`.
- Section-marker count: 4 → 4.
- The 3 pre-existing malformed doc-continuation lines (`This can be overridden…`, `If a
  dbAccessConfig…`, `to an event bus…`) are present in **both** files (old 289/399/406, new
  290/405/413) — unchanged, not a new defect.
- `Special Agent Note` cross-package hints: 7 in old, 7 in new — none lost.

The one change that could superficially look like a loss — `ballerinax/aws.redshiftdata:1.1.0:Error?`
becoming `Error?` — is a strict improvement: the qualified form is not valid Ballerina type syntax
and `Error` is the same-module type, so the short form is both correct and compilable.

## 5. Issues in `new` (independent of `old`)

Seven, only the first of which is specific to `new`; the rest are shared with `old` and are
renderer-level, not spec-v2-introduced.

1. **`distinct` dropped from `Error`.** Render: `type Error error<ErrorDetails>;`. Source
   (`errors.bal:18`): `public type Error distinct error<ErrorDetails>;`. An LLM reading the render
   cannot tell this is a distinct error type. New-only in the sense that `old` emitted no
   definition at all, so nothing was lost relative to `old`.
2. **`@constraint:` module attribution lost in the rendered text.** The JSON carries
   `"module": "ballerina/constraint"` for all 6 annotations, but the `.bal.txt` emits a bare
   `@constraint:String` with no `// Special Agent Note: … FROM ballerina/constraint` hint — unlike
   `time:Utc` and `sql:ParameterizedQuery`, which do get such notes (7 of them). A consumer has no
   in-render signal that `ballerina/constraint` must be imported.
3. **Closed records rendered as open.** All 10 source record types are `record {| … |}`
   (`types.bal:26, 83, 94, 106, 140, 174, 197, 218, 238`; `errors.bal:21`); both renders emit
   `record { … }`. This misstates the rest-field semantics.
4. **`typedesc` parameter mangled.** Source `client.bal:125`:
   `getResultAsStream(StatementId statementId, typedesc<record {}> rowTypes = <>)`. Both renders:
   `getResultAsStream(StatementId statementId, record {|anydata...;|} rowTypes = record {|anydata...;|})`.
   The parameter type is wrong and the rendered default is not valid Ballerina. The return type
   `stream<rowTypes, Error?>` then references a value as a type.
5. **Included-record parameters expanded with fabricated defaults.** Source: `init(*ConnectionConfig
   connectionConfig)` (`client.bal:44`), `execute(sql:ParameterizedQuery statement, *ExecutionConfig
   executionConfig)` (`client.bal:68`), `batchExecute(…, *ExecutionConfig executionConfig)`
   (`client.bal:94`). Both renders expand the record fields into positional params **and** keep the
   record param, and invent defaults that do not exist in the source — e.g.
   `Region region = "us-west-2"`, `auth = {accessKeyId: "", secretAccessKey: ""}`,
   `dbAccessConfig = {id: "", database: ""}`, `clientToken = ""`, `statementName = ""`,
   `withEvent = false`. The source fields are plain (`region`, `auth` required; the rest optional
   with no defaults). The rendered signatures are also illegal (required param after defaulted
   params) and would mislead an LLM into passing `dbAccessConfig` positionally.
6. **Doc-comment continuation lines emitted unprefixed** (3 places, identical in both files): the
   second line of multi-line `# + field - …` docs loses its `#`, e.g. new:126, new:241, new:249.
   This breaks compilation and reads as stray prose.
7. **`public` and `isolated` qualifiers dropped throughout.** Source declares
   `public isolated client class Client`, `public isolated function init`, `remote isolated
   function …`; renders emit `client class Client`, `function init`, `remote function …`.
   Consistent renderer convention, but it hides the isolation contract.

Minor/cosmetic, not counted above: `close()` is rendered `returns Error|()` where the source says
`returns Error?` (`client.bal:158`) — equivalent, both sides.

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala has exactly one module (`modules/aws.redshiftdata`), so there is no
submodule-only API and the `getDefaultModule()`-only extraction limitation does not bite here.

`grep -rE '^public ' modules/aws.redshiftdata/*.bal` yields 16 public declarations:

`Error`, `ErrorDetails`, `Client`, `ConnectionConfig`, `Region`, `StaticAuthConfig`,
`EC2IAMRoleConfig`, `Cluster`, `WorkGroup`, `SessionId`, `ExecutionConfig`, `ExecutionResponse`,
`StatementId`, `DescriptionResponse`, `StatementData`, `Status`.

All 16 appear in `new` with definitions. All 16 appear in `old` as names, but `Error`, `SessionId`
and `StatementId` only as `// Unknown type:` placeholders with no body.

Non-public symbols correctly absent from both: `ResultIterator` (`result_iterator.bal:20`, module-
private `isolated class`), module `init()`/`setModule()` (`init.bal:19, 23`), and the private
`extern*` / `validateExecutionConfig` methods on `Client`.

## 7. Compiler plugin

**None.** `find` over the cloned repo at `v1.1.0` for `*compiler-plugin*` / `*plugin*` returns
nothing, and the bala has no `compiler-plugin/` directory (`ls .../java21` →
`bala.json  dependency-graph.json  docs  modules  package.json  platform`). The `native/` directory
holds the Java runtime bindings (`io.ballerina.lib.aws.redshiftdata.*`, referenced from
`@java:Method` externals), not a compiler plugin. So there is nothing plugin-derived that ought to
surface in the render and doesn't.

Constraint enforcement here comes from `ballerina/constraint`'s own plugin, not this package's —
and `new` now renders those annotations, which is precisely the behaviour a consumer needs.

## 8. Other considerations

- **Stability**: 1.1.0, post-1.0, not a pre-release. `package.json` shows `template: false`,
  keywords `["Data Warehouse", "Columnar Storage", "Cost/Paid", "vendor/aws"]`. No deprecation
  marker in the bala metadata.
- **Size/tokens**: 540 lines — small. The +9 lines buy 3 real type definitions and 6 constraint
  annotations; excellent value per token. No bloat concern.
- **Constraint visibility matters here.** `SessionId` and `StatementId` are the primary inputs to
  `getResultAsStream` and `describe`; their UUID-shaped regex was completely invisible in `old`
  (both were `// Unknown type:`), so an LLM had no way to know they are `string` at all, let alone
  pattern-constrained. This is the single largest practical gain.
- **Non-compiling render** (both sides): the doc-continuation lines, the `typedesc` param, and the
  required-after-defaulted params in `init`/`execute`/`batchExecute` mean neither render is valid
  Ballerina as a whole. `new` reduces the count of such defects by one (`string error?` →
  `string 'error?`) but does not eliminate them.
- **Enum members are duplicated as consts** in both renders (64 `typeDefs` = 16 public symbols +
  the `Region` and `Status` members emitted as `const string X = "X";`). Unchanged between sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old new` | 531 / 540 |
| `git ls-remote --tags <repo>` | tags `v1.0.0`, `v1.0.1`, `v1.1.0`; exact match `v1.1.0` |
| `git clone --depth 1 --branch v1.1.0 …` | OK → `…/work/aws.redshiftdata/src` |
| `ls .../1.1.0/java21` | `bala.json dependency-graph.json docs modules package.json platform` — no `compiler-plugin/` |
| `ls .../java21/modules` | `aws.redshiftdata` (single module) |
| `diff -q bala/*.bal src/ballerina/*.bal` (5 files) | identical for all 5 |
| `grep -n '^// --- ' old / new` | 4 markers each: 7/163/165/489 (old), 7/163/165/498 (new) |
| `grep -c '^// Unknown type:' old / new` | 3 / 0 (old at lines 278, 392, 424) |
| `grep -c '@constraint:' old / new` | 0 / 6 |
| `grep -c 'Special Agent Note' old / new` | 7 / 7 |
| `grep -nE '^(If a \|to an event bus\|This can be)' old / new` | 3 hits each (old 289/399/406, new 290/405/413) |
| `diff -u old new` | 9 hunks, +15 / −6 lines |
| JSON `typeDefs` set-difference | `only old = set()`, `only new = set()`; 64 both |
| JSON changed typeDefs | `Cluster`, `DescriptionResponse`, `Error`, `ExecutionConfig`, `SessionId`, `StatementId`, `WorkGroup` |
| JSON `readme`/`description` equality | `True` / `True` (8387 chars both) |
| JSON `clients` unified diff | 2 changed lines, both `ballerinax/aws.redshiftdata:1.1.0:Error?` → `Error?` |
| JSON `functions`/`services`/`annotations` | 0/0/0 on both sides |
| `grep -rE '^public ' modules/aws.redshiftdata/*.bal` | 16 public declarations (listed in §6) |
| `errors.bal:18` | `public type Error distinct error<ErrorDetails>;` |
| `types.bal:158-164`, `205-211` | `SessionId` / `StatementId` with pattern constraints — match render |
| `types.bal:107-117`, `121-131`, `144-154`, `177-187` | 4 field constraints — match render |
| `types.bal:242` | `string 'error?;` — confirms `new` correct, `old` wrong |
| `client.bal:23,44,68,94,125,137,158` | `public isolated client class Client` + init + 5 remote methods |
| `client.bal:125` | `typedesc<record {}> rowTypes = <>` vs render's `record {\|anydata...;\|}` |
| `result_iterator.bal:20` | `isolated class ResultIterator` — non-public, correctly absent |
| `package.json` | `name aws.redshiftdata`, `version 1.1.0`, `template false` |
| `find src -iname '*compiler-plugin*'` | no results |

## 10. Caveats and unverified items

- **Ballerina Central API was not re-queried** for this library; module list, keywords and
  non-deprecation were read from the bala's `package.json` and `modules/` listing instead, which is
  the authoritative artefact the extractor consumed. Deprecation status is therefore *unverified*
  via Central, though nothing in the bala metadata flags it.
- **Neither render was compiled.** The non-compiling constructs called out in §5 (items 4, 5, 6)
  were determined by reading the render against the Ballerina grammar and the source, not by running
  `bal build` on the rendered text. The claim "does not compile" is a reading, not an executed test.
- **Enum member ordering** differs from source in both renders (`Status` renders
  ALL/FAILED/ABORTED/FINISHED/STARTED/PICKED/SUBMITTED vs. source order). I treated this as
  semantically irrelevant for Ballerina enums; I did not verify that no downstream consumer depends
  on declaration order.
- I did not diff the `docs/` directory inside the bala against the rendered doc strings field by
  field; doc fidelity was spot-checked against the `#`-comments in the `.bal` sources, which are the
  same text.

# ballerinax/aws.marketplace.mpm 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.marketplace.mpm` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.marketplace.mpm |
| Tag reviewed | `v1.0.0` (commit `0313867f714088166015cce265d10119e167c13b`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.marketplace.mpm/1.0.0/java21` |
| Old render | `295` lines (12,631 bytes) |
| New render | `307` lines (13,283 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Tiny single-module connector (4 `.bal` files, 282 lines total in the bala). The upstream tag `v1.0.0`
sources are byte-identical to the bala sources (`diff` returned no output for `client.bal`,
`types.bal`, `errors.bal`), so GitHub and the bala agree and either is authoritative.

`new` differs from `old` in exactly 8 hunks (+16 / −4 lines). Every one of them is a strict
improvement:

1. `// Unknown type: Error` (1 occurrence in `old`, 0 in `new`) is replaced by a real definition.
2. Two version-qualified type refs (`ballerinax/aws:1.0.1:Region`, `ballerinax/aws.marketplace.mpm:1.0.0:Error`)
   become plain `aws:Region` / `Error` (0 such refs remain in `new`).
3. 11 `@constraint:*` annotations that exist in the library source are now surfaced; `old` had none.
4. `close()` is no longer mislabelled `remote` — the source declares it `public isolated function`,
   not a remote method.

Nothing present in `old` is absent, truncated, or degraded in `new`. Coverage of the default
module's public API is complete on the `new` side (11/11 public symbols). The remaining
inaccuracies (open vs. closed records, non-compiling flattened `init`/`batchMeterUsage`
signatures, lost `= []` default, `distinct` dropped) are shared with `old` except the last, which
is new-only but strictly better than `old`'s total omission of the type.

## 2. Change inventory

Declaration counts (grep over each `.bal.txt`):

| Kind | old | new |
|---|---|---|
| `const string` | 3 | 3 |
| `type ... record`/`error` | 8 | 9 |
| `enum` | 1 | 1 |
| `client class` | 1 | 1 |
| Client methods (`function`/`remote function`) | 4 | 4 |
| `@constraint:*` annotation lines | 0 | 11 |
| `// Unknown type:` placeholders | 1 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

**Added in `new` (1 declaration):**
- `type Error error<aws:ErrorDetails>;` with its doc comment `# Represents a AWS Marketplace Metering distinct error.`
  (replaces `// Unknown type: Error`).

**Removed in `new`:** none. Set difference over JSON `typeDefs` names is empty in both directions
(`only old set()`, `only new set()`); all 13 typeDef names identical.

**Modified in `new` (7 sites):**

| Site | old | new |
|---|---|---|
| `ConnectionConfig.region` | `ballerinax/aws:1.0.1:Region\|string` | `aws:Region\|string` |
| `Client.init` return | `returns ballerinax/aws.marketplace.mpm:1.0.0:Error?` | `returns Error?` |
| `Client.close` qualifier | `remote function close()` | `function close()` |
| `BatchMeterUsageRequest` | no annotations | +2 `@constraint` (String, Array) |
| `UsageRecord` | no annotations | +4 `@constraint` (String×3, Int, Array — 5 lines) |
| `UsageAllocation` | no annotations | +2 `@constraint` (Int, Array) |
| `Tag` | no annotations | +2 `@constraint:String` |

README section (lines 1–157) is byte-identical between the two renders (`diff` of the first 157
lines returned nothing). Top-level `functions`, `services`, `annotations` arrays are empty (`[]`,
`0`, `0`) in both JSONs.

## 3. Correctness against library source

All checks against the bala module sources (identical to upstream `v1.0.0`).

- `type Error error<aws:ErrorDetails>` — `errors.bal:20` declares
  `public type Error distinct error<aws:ErrorDetails>;`. Base type and doc string match; `distinct`
  is dropped (see §5, N1).
- `ConnectionConfig.region` typed `aws:Region|string` — `types.bal:31` declares
  `aws:Region|string region;`. Exact match. `old`'s `ballerinax/aws:1.0.1:Region|string` was not
  valid Ballerina syntax.
- `close()` non-remote — `client.bal:82` declares `public isolated function close() returns Error?`.
  `new` is correct; `old`'s `remote function close()` was wrong. Both JSONs already carried
  `"type": "Normal Function"`, so this was purely a renderer-side defect in `old`.
- All 11 constraint annotations verified one-by-one against `types.bal`:

| Render | Source |
|---|---|
| `BatchMeterUsageRequest.productCode` `@constraint:String { pattern: re \`^[-a-zA-Z0-9/=:_.@]{1,255}$\` }` | `types.bal:50-52` |
| `BatchMeterUsageRequest.usageRecords` `@constraint:Array { maxLength: 25 }` | `types.bal:55-57` |
| `UsageRecord.customerIdentifier` `pattern: re \`[\s\S]{1,255}$\`` | `types.bal:64-66` |
| `UsageRecord.customerAWSAccountId` `pattern: re \`^[0-9]{1,255}$\`` | `types.bal:69-71` |
| `UsageRecord.dimension` `pattern: re \`[\s\S]{1,255}$\`` | `types.bal:74-76` |
| `UsageRecord.quantity` `@constraint:Int { minValue: 0, maxValue: 2147483647 }` | `types.bal:81-84` |
| `UsageRecord.usageAllocations` `@constraint:Array { minLength: 1, maxLength: 2500 }` | `types.bal:87-90` |
| `UsageAllocation.allocatedUsageQuantity` `@constraint:Int { minValue: 0, maxValue: 2147483647 }` | `types.bal:97-100` |
| `UsageAllocation.tags` `@constraint:Array { minLength: 1, maxLength: 5 }` | `types.bal:103-106` |
| `Tag.'key` `pattern: re \`^[a-zA-Z0-9+ -=._:/@]{1,100}$\`` | `types.bal:113-115` |
| `Tag.value` `pattern: re \`^[a-zA-Z0-9+ -=._:/@]{1,256}$\`` | `types.bal:118-120` |

  All 11 match exactly, including regex bodies and numeric bounds. No invented annotations.
- `resolveCustomer(string registrationToken) returns ResolveCustomerResponse|Error` —
  `client.bal:50` `isolated remote function resolveCustomer(string registrationToken) returns ResolveCustomerResponse|Error`.
  Matches (modulo dropped `isolated`).
- Record field types/optionality spot-checked against `types.bal:23-150`: `ResolveCustomerResponse`
  (3 required strings), `BatchMeterUsageResponse` (`UsageRecordResult[] results`,
  `UsageRecord[] unprocessedRecords`, both required), `UsageRecordResult` (3 optional fields),
  `UsageRecord.timestamp` (`time:Utc`, required) — all correct in `new`.
- Enum `UsageRecordStatus` members `SUCCESS`/`CUSTOMER_NOT_SUBSCRIBED`/`DUPLICATE_RECORD` and their
  string values `"Success"`/`"CustomerNotSubscribed"`/`"DuplicateRecord"` match `types.bal:143-150`.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full `diff -u old new` on the two `.bal.txt` files — 8 hunks, all reviewed line by line above.
  No hunk removes a declaration, parameter, default value, return type, doc line, or README content.
- Set difference on JSON `typeDefs` names: empty both ways (13 = 13).
- Structural JSON diff of `clients[0]`: a single changed line (the `init` return type name
  `ballerinax/aws.marketplace.mpm:1.0.0:Error?` → `Error?`). No parameter, doc, or method lost.
- Per-field JSON diff of every changed typeDef: every change is an *added* `annotations` array or a
  de-qualified type name; no field, description, or `optional` flag was removed.
- Declaration counts per kind (§2 table) — identical apart from the one added `type Error`.
- README section (lines 1–157) byte-identical.
- The one qualifier change (`remote function close` → `function close`) makes `new` *match* the
  library source, so it is a fix, not a regression.

## 5. Issues in `new` (independent of `old`)

7 inaccuracies remain in `new`. Only N1 is specific to `new`; N2–N7 are equally present in `old`
(the diff shows no change at those lines), so they are pipeline-wide, not spec-v2 defects.

- **N1 — `distinct` dropped from `Error` (new-only).** `new` line 170 renders
  `type Error error<aws:ErrorDetails>;` but `errors.bal:20` is
  `public type Error distinct error<aws:ErrorDetails>;`. JSON `baseType` is
  `"error<aws:ErrorDetails>"` — the `distinct` qualifier is lost upstream of the renderer.
  Still a large net gain over `old`, which emitted `// Unknown type: Error` with no definition at all.
- **N2 — records rendered open.** All 8 records are `record { ... }` in the render; every one is
  `record {| ... |}` (closed) in `types.bal`. An LLM could emit extra fields that will not compile.
- **N3 — `BatchMeterUsageRequest.usageRecords` default lost.** `types.bal:58` declares
  `UsageRecord[] usageRecords = [];` (required field with a default). Both renders show
  `UsageRecord[] usageRecords?;` — the default is dropped and the field is misreported as optional.
- **N4 — `batchMeterUsage` signature does not compile and carries an invented default.** Render:
  `remote function batchMeterUsage(string productCode = "", UsageRecord[] usageRecords = [], BatchMeterUsageRequest request)`.
  Source (`client.bal:62`) is `isolated remote function batchMeterUsage(*BatchMeterUsageRequest request)`.
  The included-record param is flattened *and* retained, producing a required parameter after
  defaultable ones (invalid Ballerina), and `productCode = ""` is a default that does not exist in
  the source (`types.bal:53` — required, no default).
- **N5 — `init` signature does not compile.** Render ends
  `..., aws:EndpointConfig endpoint = {}, ConnectionConfig configs) returns Error?` — same
  flatten-and-retain problem; source (`client.bal:33`) is `public isolated function init(*ConnectionConfig configs)`.
  Also `auth:AuthConfig auth = {accessKeyId: "", secretAccessKey: ""}` is a synthesised default;
  `types.bal:28` declares `auth:AuthConfig auth;` with no default.
- **N6 — enum member values not on the enum.** `enum UsageRecordStatus { DUPLICATE_RECORD, CUSTOMER_NOT_SUBSCRIBED, SUCCESS }`
  omits the `= "Success"` style values (they are emitted separately as three `const string`s above,
  so the information survives, but the enum body is lossy and the member order is reversed vs. source).
- **N7 — parameter doc lines dropped.** The JSON carries per-parameter descriptions (e.g.
  `registrationToken` → "The registration-token provided by the customer") but the renderer emits
  only the doc header/example block, ending each method doc with a bare `# `.

Also noted, non-defects: `public` and `isolated` qualifiers are stripped throughout (uniform
renderer behaviour); `returns Error|()` on `close` instead of the idiomatic `Error?` (cosmetic,
both sides); `aws:Region` in `ConnectionConfig` carries no `// Special Agent Note: ... FROM ballerinax/aws package`
comment because the JSON has no `links` entry for that field (both sides) — the other cross-package
refs (`auth:AuthConfig`, `aws:EndpointConfig`, `time:Utc`) do carry the note.

## 6. Coverage gaps vs. the library

**0 gaps.** The package exports exactly one module (`package.json` `"export": ["aws.marketplace.mpm"]`,
Central `modules` list has one entry) and it is the default module, so there is no submodule-only API.

All 11 `public` declarations in the bala appear in `new`:

| Public symbol (bala) | In `new` | In `old` |
|---|---|---|
| `ConnectionConfig` (`types.bal:23`) | line 174 | yes |
| `ResolveCustomerResponse` (`types.bal:38`) | line 190 | yes |
| `BatchMeterUsageRequest` (`types.bal:48`) | line 201 | yes |
| `UsageRecord` (`types.bal:62`) | line 212 | yes |
| `UsageAllocation` (`types.bal:95`) | line 234 | yes |
| `Tag` (`types.bal:111`) | line 245 | yes |
| `BatchMeterUsageResponse` (`types.bal:125`) | line 256 | yes |
| `UsageRecordResult` (`types.bal:133`) | line 265 | yes |
| `UsageRecordStatus` (`types.bal:143`) | line 275 | yes |
| `Error` (`errors.bal:20`) | line 170 | **no** (`// Unknown type: Error`) |
| `Client` (`client.bal:21`) | line 284 | yes |

Client method coverage: `init`, `resolveCustomer`, `batchMeterUsage`, `close` — 4/4 public members
present in both. The non-public helpers `externInit` (`client.bal:37`) and `externBatchMeterUsage`
(`client.bal:70`), and the module-level `init()`/`setModule()` (`init.bal:19,23`), are correctly
absent from both renders.

## 7. Compiler plugin

The package ships **no compiler plugin**. Evidence:
- `find . -iname '*compiler-plugin*'` over the cloned `v1.0.0` tree returned nothing.
- The bala root contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json`, `platform/` — no `compiler-plugin/` directory and no `compiler-plugin.json`.
- `native/` holds only the JNI adaptor (`io.ballerina.lib.aws.mpm.NativeClientAdaptor`,
  `ModuleUtils`), not a plugin.

Validation is done at runtime instead, via `ballerina/constraint` inside `batchMeterUsage`
(`client.bal:63-66` calls `constraint:validate` and converts a `constraint:Error` into an
`mpm:Error`). Those constraints are exactly what `new` now surfaces as `@constraint:*` annotations,
so the render is aligned with the library's actual validation behaviour — `old` was not.

## 8. Other considerations

- Not deprecated: Central returns `deprecated: None`, `deprecateMessage: ""`.
- Stable 1.0.0, built with Ballerina `2201.12.0`, `graalvmCompatible: true`, `template: false`.
  Low adoption (`pullCount: 4`).
- Size impact is negligible: +652 bytes (+5.2%), +12 lines. The added constraint annotations are
  high-value tokens (they encode AWS API limits the model would otherwise have to guess).
- The render carries the full README (149 lines, lines 7–155) which is the bulk of the file; only
  ~150 lines are actual API.
- Both renders emit no `import` statements, so `aws:`, `auth:`, `time:`, `constraint:` prefixes are
  unbound in the render text. The `// Special Agent Note: ... FROM <org>/<pkg> package` comments
  cover `auth:AuthConfig`, `aws:EndpointConfig` and `time:Utc`; `aws:ErrorDetails` (new, line 170),
  `aws:Region` (line 179) and `constraint:` (11 sites) have no such note. For `aws:ErrorDetails`
  and the `constraint:` annotations this is a small new surface of unannotated prefixes introduced
  by spec v2, but the prefixes themselves are correct Ballerina and match the source imports
  (`errors.bal:17`, `types.bal:17-20`).

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 295 / 307 |
| 2 | `wc -c old/*.bal.txt new/*.bal.txt` | 12,631 / 13,283 |
| 3 | `grep -c '^// Unknown type:'` | old 1, new 0 |
| 4 | `grep -n '^// --- '` | both: README@7, END README@156, Types@158, Client@269(old)/281(new) |
| 5 | `diff -u old new` | 8 hunks, +16/−4; full text reviewed |
| 6 | `diff <(sed -n 1,157p old) <(sed -n 1,157p new)` | no output — README identical |
| 7 | `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 2, new 0 |
| 8 | `grep -c '@constraint:'` | old 0, new 11 |
| 9 | Declaration greps (`^const `, `^type `, `^enum `, `^client class `, `^    (remote )?function `) | const 3/3, type 8/9, enum 1/1, class 1/1, methods 4/4 |
| 10 | `git ls-remote --tags <repo>` | tags v0.1.0…v1.0.0; exact match `v1.0.0` = `0313867f…` |
| 11 | `git clone --depth 1 --branch v1.0.0` into scratch | succeeded |
| 12 | `diff src/ballerina/{client,types,errors}.bal` vs bala `modules/aws.marketplace.mpm/` | CLIENT_SAME, TYPES_SAME, ERRORS_SAME |
| 13 | `ls bala/java21/modules/aws.marketplace.mpm/` | `client.bal errors.bal init.bal types.bal` (282 lines total) |
| 14 | `ls bala/java21/` | no `compiler-plugin/` |
| 15 | `find . -iname '*compiler-plugin*'` in clone | no matches |
| 16 | `cat package.json` | `"export": ["aws.marketplace.mpm"]`, ballerina_version 2201.12.0, graalvmCompatible true |
| 17 | `curl api.central.ballerina.io/.../ballerinax/aws.marketplace.mpm/1.0.0` | 1 module, `deprecated: None`, pullCount 4 |
| 18 | Python set-diff on JSON `typeDefs` names | `only old set()`, `only new set()`; 13 each |
| 19 | Python unified diff of JSON `clients[0]` | 1 changed line (init return type) |
| 20 | Python per-typeDef JSON diff | changes only in `BatchMeterUsageRequest`, `ConnectionConfig`, `Error`, `Tag`, `UsageAllocation`, `UsageRecord`; all additive (`annotations`, `baseType`) or de-qualification |
| 21 | JSON `clients[0].functions[*].type` both sides | `close` = `"Normal Function"` in old and new → `old`'s `remote` was a renderer defect |
| 22 | `grep -nE '^public ' bala/modules/**/*.bal` | 11 public symbols; all located in `new` (§6 table) |
| 23 | 11 `@constraint` annotations vs `types.bal:50-120` | all 11 match exactly (§3 table) |
| 24 | `client.bal:82` vs render line 307 | source `public isolated function close() returns Error?` → `new` correct |
| 25 | `errors.bal:20` vs render line 170 | `distinct` present in source, absent in render |
| 26 | `types.bal:58` vs render line 207 | source `UsageRecord[] usageRecords = [];` → render `usageRecords?;` |
| 27 | JSON `clients[0].functions[*].parameters` | per-param descriptions present in JSON, absent from rendered text (both sides) |
| 28 | `OLD_AND_NEW_DIFFS/aws.marketplace.mpm_diff.md` claims (295/307, +16/−4, 8 hunks, 1 added `type Error`, unknown 1→0, qualified refs 2→0) | all independently reproduced and confirmed |

## 10. Caveats and unverified items

- The `old`-side renderer defect that emitted `remote function close()` was inferred from the fact
  that both JSONs label `close` as `"Normal Function"`; I did not read the `main`-branch
  `to-syntax-string.ts` source to confirm the exact code path. The *outcome* (source says
  non-remote, `new` says non-remote, `old` said remote) is verified directly.
- Whether the loss of `distinct`, the flattened-but-retained included-record parameters, and the
  synthesised parameter defaults originate in the Java extractor or the TypeScript renderer was not
  determined — I only verified they are present in the JSON (`baseType` lacks `distinct`;
  `parameters` contains both the flattened fields and the record param with `"default"` values), so
  they are at latest an extractor-side artefact. Not attributable to spec v2 either way since
  `old`'s JSON has the identical parameter data.
- I did not compile either render against the Ballerina distribution; the "does not compile" claims
  for N4/N5 rest on the language rule that a required parameter cannot follow defaultable ones, not
  on a compiler run.
- `examples/` and `ballerina/tests/` in the upstream clone were not reviewed; they contribute
  nothing to the render.

# ballerinax/aws.marketplace.mpe 1.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.marketplace.mpe` |
| Pinned version | `1.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.marketplace.mpe |
| Tag reviewed | `v1.0.0` (exact match; commit `4fbb1a14eae4f74e6e119e244405dc613fc1b1ab`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.marketplace.mpe/1.0.0/java21` |
| Old render | `221` lines |
| New render | `226` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small connector: 1 default module, 4 `.bal` files (211 lines total), 6 public types + 1 client class,
3 client methods. Upstream `v1.0.0` sources are byte-identical to the bala sources (verified by `diff`),
so GitHub and the bala agree.

`new` is strictly better than `old` on four counts and loses nothing:

1. `// Unknown type: Error` (old) → a real `type Error error<aws:ErrorDetails>;` definition with its
   doc comment (new). Unknown-type placeholders: old 1 → new 0.
2. Version-qualified type refs eliminated: `ballerinax/aws:1.0.1:Region|string` → `aws:Region|string`,
   `ballerinax/aws.marketplace.mpe:1.0.0:Error?` → `Error?`. Count: old 2 → new 0.
3. Four `@constraint:*` annotations on record fields are now rendered (old: 0), recovering real
   validation semantics that the connector enforces at runtime via `constraint:validate`.
4. `close()` is no longer mislabelled `remote`. Source declares `public isolated function close()`;
   old rendered `remote function close()`, new renders `function close()`. Note the underlying JSON is
   identical on both sides (`"type": "Normal Function"`) — this was a `toSyntaxString` bug, now fixed.

No declaration, parameter, default, return type, doc line, or README byte was lost. README is
byte-identical to `docs/README.md` in the bala on both sides.

Everything wrong in `new` is also wrong in `old` (section 5), except the dropped `distinct` keyword on
`Error`, which is a new-only artefact of newly emitting that type at all.

## 2. Change inventory

Diff: **+9 lines, −4 lines, 6 hunks**. Lines 1–133 (header, self-import, full README) are byte-identical.

### Top-level declarations

| Kind | old | new | delta |
|---|---|---|---|
| `type ... record` | 5 | 5 | 0 |
| `type ... error<>` | 0 | 1 | **+1 (`Error`)** |
| `client class` | 1 | 1 | 0 |
| `// Unknown type:` placeholder | 1 | 0 | **−1 (`Error`, replaced by the real def)** |
| enum / const / annotation / listener / service / module-level function | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |

Declarations **removed**: none. Declarations **added**: `type Error` (was the placeholder).

### Client methods (3 → 3, no add/remove)

| Method | old | new |
|---|---|---|
| `init` | `function init(...) returns ballerinax/aws.marketplace.mpe:1.0.0:Error?` | `function init(...) returns Error?` |
| `getEntitlements` | `remote function getEntitlements(...)` | identical (byte-for-byte) |
| `close` | `remote function close() returns Error\|()` | `function close() returns Error\|()` |

`init`'s 55-member region union, all parameter names, defaults, and the `// Special Agent Note` suffix
are byte-identical between the two `init` lines apart from the return type.

### Record field changes

| Record | change in `new` |
|---|---|
| `ConnectionConfig` | `ballerinax/aws:1.0.1:Region\|string region` → `aws:Region\|string region` |
| `EntitlementsRequest` | `+@constraint:String { minLength: 1, maxLength: 255 }` on `productCode`; `+@constraint:String { pattern: re \`\S+\` }` on `nextToken` |
| `EntitlementFilter` | `+@constraint:Array { minLength: 1 }` on `customerIdentifier` and on `dimension` |
| `EntitlementsResponse`, `Entitlement` | unchanged |

### JSON-level delta (`old.json` 18,359 B → `new.json` 19,140 B)

Sorted-key `json.tool` diff shows exactly 4 categories of change and nothing else:
2 type-name de-qualifications, `+"baseType": "error<aws:ErrorDetails>"` on the `Error` typedef,
and 4 `annotations` arrays. `typeDefs` = 6 on both sides; `clients` = 1; `functions`/`services`/
`annotations` = 0 on both sides; `readme` string identical.

## 3. Correctness against library source

Every added/changed item verified against the bala sources (identical to `v1.0.0` upstream).

| Render (new) | Source | Verdict |
|---|---|---|
| `type Error error<aws:ErrorDetails>;` L138, doc `# Represents an AWS Marketplace Entitlement distinct error.` L137 | `errors.bal:19-20` — `# Represents an AWS Marketplace Entitlement distinct error.` / `public type Error distinct error<aws:ErrorDetails>;` | Correct except `distinct` dropped (§5.1) |
| `aws:Region\|string region` L150 | `types.bal:30` — `aws:Region\|string region;` | Exact match |
| `@constraint:String { minLength: 1, maxLength: 255 }` on `productCode` L160 | `types.bal:39-42` — `@constraint:String { minLength: 1, maxLength: 255 }` | Exact match |
| `@constraint:String { pattern: re \`\S+\` }` on `nextToken` L167 | `types.bal:49-51` — `@constraint:String { pattern: re \`\S+\` }` | Exact match (regex escape preserved) |
| `@constraint:Array { minLength: 1 }` on `customerIdentifier` L175 | `types.bal:58-60` | Exact match |
| `@constraint:Array { minLength: 1 }` on `dimension` L178 | `types.bal:63-65` | Exact match |
| `function close() returns Error\|()` L225 | `client.bal:71` — `public isolated function close() returns Error?` | Not remote — new is correct, old was wrong |
| `remote function getEntitlements(...)` L218 | `client.bal:51` — `isolated remote function getEntitlements(...)` | Remote qualifier correct on both sides |
| `function init(...) returns Error?` L211 | `client.bal:33` — `public isolated function init(*ConnectionConfig configs) returns Error?` | Return type now correct/unqualified; param list is a fabrication shared with `old` (§5.2) |

All 6 public types and all 5 record field sets were checked field-by-field against `types.bal`;
names, types, optionality markers (`?`), and doc strings match on both sides.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new`: 6 hunks, 9 added / 4 removed lines — all 4 removed lines accounted for above,
  each replaced by a strictly more accurate line.
- Declaration set extracted with `grep -nE '^(public )?(type|client class|class|enum|const|annotation|listener|service|function) '`
  on both files: old {ConnectionConfig, EntitlementsRequest, EntitlementFilter, EntitlementsResponse,
  Entitlement, Client}; new = same set **plus** `Error`. Nothing removed.
- Client method set: 3 on both sides, same names, same parameter lists (`init` and `getEntitlements`
  param text byte-identical).
- README: `old.json["readme"] == new.json["readme"]` → `True`; both equal `docs/README.md` in the bala
  (124 lines) → `True`. Lines 1–133 of the two renders diff clean.
- Section markers: 4 on both sides, same 3 sections (`README`, `Types`, `Client`).
- Doc comments: no `#` doc line present in `old` is absent from `new` (verified by the fact that the
  diff removes only 4 lines, none of which is a doc line).
- JSON: sorted-key diff shows only additions and de-qualifications; no field dropped anywhere.

## 5. Issues in `new` (independent of `old`)

7 issues. Only 5.1 is new-only; 5.2–5.7 are present identically in `old` (shared pipeline behaviour,
not caused by spec v2).

1. **`distinct` dropped from `Error`** *(new-only)*. Source `errors.bal:20` is
   `public type Error distinct error<aws:ErrorDetails>;`; render L138 is `type Error error<aws:ErrorDetails>;`.
   The JSON `baseType` is `"error<aws:ErrorDetails>"`, so the loss happens in the Java extractor, not
   the renderer. Impact is low (an LLM will not usually re-declare the error type) but the render
   misstates the type's nominal identity. Also, unlike `auth:AuthConfig` / `aws:EndpointConfig` /
   `time:Utc`, the `aws:ErrorDetails` reference carries **no** `// Special Agent Note: ... FROM ...`
   module attribution, and neither does `aws:Region` at L150 — 3 `Special Agent Note`s cover external
   types, but these two are unattributed and the render emits no `import ballerinax/aws;`.
2. **`Client.init` signature is fabricated.** Source is `init(*ConnectionConfig configs)`. Render L211
   both expands the included record into `auth`, `region`, `endpoint` **and** appends a trailing
   required-looking `ConnectionConfig configs` parameter (JSON marks it `"optional": true`, but the
   renderer emits no `?` and no default). No such signature exists; an LLM copying it would emit
   non-compiling code.
3. **`getEntitlements` has invented defaults.** Render L218:
   `getEntitlements(string productCode = "", EntitlementFilter filter = {}, int maxResults = 0, string nextToken = "", EntitlementsRequest request)`.
   Source `client.bal:51` is `getEntitlements(*EntitlementsRequest request)`, and `productCode` is a
   **required** field (`types.bal:43`) with `@constraint:String {minLength: 1}` — so `productCode = ""`
   is both non-existent and guaranteed to fail validation at runtime. Same trailing-param problem as 5.2.
4. **Closed records rendered as open.** All 5 records are `record {| ... |}` in `types.bal`; the render
   emits `record { ... }` (5 occurrences of `record {$`, 0 of `record {|`). Misstates rest-field
   behaviour.
5. **Qualifiers dropped.** `public` is absent everywhere; `isolated` is dropped from the class and all
   3 methods; `public isolated client class Client` renders as `client class Client`.
6. **Doc-comment continuation lines lose the `#` prefix.** e.g. new L143-146, L149, L152, L186 —
   `# Authentication configuration: ...` followed by bare `AWS — static credentials,` etc. The block is
   not valid Ballerina if pasted, and the text reads as stray code to a parser.
7. **Blank line between doc comment and declaration** for the 5 records (e.g. L156 doc, L157 blank,
   L158 `type EntitlementsRequest record {`), which detaches the doc from the declaration in real
   Ballerina. Inconsistently, the new `Error` typedef (L137-138) has no blank line.

## 6. Coverage gaps vs. the library

**None (0).**

- `package.json` `"export": ["aws.marketplace.mpe"]` — single module, which is the default module.
  `modules/` contains exactly one directory, `aws.marketplace.mpe`. Central metadata lists exactly one
  module. So there is **no submodule-only API** and the `getDefaultModule()`-only extraction loses
  nothing for this library.
- Public symbols in the default module (`grep 'public ' modules/aws.marketplace.mpe/*.bal`):
  `Error`, `ConnectionConfig`, `EntitlementsRequest`, `EntitlementFilter`, `EntitlementsResponse`,
  `Entitlement`, `Client`, `Client.init`, `Client.close`, and remote `Client.getEntitlements`.
  All 10 appear in `new`. In `old`, `Error` appeared only as a placeholder.
- Non-public module members deliberately absent from both renders: `externInit`, `externGetEntitlements`
  (private `@java:Method` externals), `init()`/`setModule()` in `init.bal` (module-level, not public).
  Their absence is correct.

## 7. Compiler plugin

**This package ships no compiler plugin.** Evidence:
- `find src -ipath '*compiler*plugin*'` on the `v1.0.0` clone → no matches.
- The bala has no `compiler-plugin/` directory (`ls .../1.0.0/java21` → `bala.json`, `dependency-graph.json`,
  `docs`, `modules`, `package.json`, `platform` only).
- `Ballerina.toml` declares only `[platform.java21.dependency]` jars — no `[[tool]]` or plugin entry.

Validation is done at runtime inside the connector (`constraint:validate(request)` in `client.bal:52-56`),
not by a plugin. The `@constraint:*` annotations that drive it are now visible in `new` and were not in
`old` — so nothing plugin-implied is missing from the render.

## 8. Other considerations

- **Stable release, not deprecated.** Central: `deprecated: None`, `deprecateMessage: ""`,
  `ballerinaVersion: 2201.12.0`. `pullCount: 4` — a very new/low-traffic package (created
  2026-07-30 per `createdDate` epoch 1785500680000).
- **Size/token impact is negligible**: +5 lines (+2.3%), JSON +781 bytes (+4.3%). No token concern.
- **The single longest line is `init`** (~1.3 KB of region string literals), unchanged between sides.
  It dominates the client section and is the main token cost in this render.
- **Doc quality is good**: every public type and field carries a doc comment, and `getEntitlements`/
  `close` carry runnable ` ```ballerina ` examples, preserved verbatim in both renders.
- The `@constraint` annotations newly surfaced in `new` are materially useful to an LLM: without them
  a generated call can pass `productCode: ""` and get a runtime `Request validation failed:` error.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 221 / 226 |
| `diff -u old new \| grep -c '^+[^+]'` / `'^-[^-]'` | 9 added / 4 removed |
| `diff <(sed -n 1,133p old) <(sed -n 1,133p new)` | empty — header + README identical |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 2, new 0 |
| `grep -c '@constraint:'` | old 0, new 4 |
| `grep -n '^// --- '` | both: L7 README, L133 END README, L135 Types, L202/L207 Client |
| `grep -nE '^(public )?(type\|client class\|...) '` old / new | old 6 decls, new 7 decls (superset) |
| `grep -nE '^    (remote )?function '` old / new | old: init, remote getEntitlements, remote close; new: init, remote getEntitlements, close |
| `git ls-remote --tags <repo>` | `v1.0.0` → `4fbb1a14eae4f74e6e119e244405dc613fc1b1ab` |
| `git clone --depth 1 --branch v1.0.0` then `diff src/ballerina/{client,errors,init,types}.bal` vs bala `modules/aws.marketplace.mpe/` | all 4 IDENTICAL |
| `wc -l` bala `.bal` files | client 75, errors 20, init 25, types 91 = 211 |
| `find src -ipath '*compiler*plugin*'` | no matches |
| `ls .../1.0.0/java21` | no `compiler-plugin/` |
| `diff <(json.tool --sort-keys old.json) <(... new.json)` | 4 change categories only (2 de-qualifications, +baseType, +4 annotation arrays) |
| `json['typeDefs']` lengths | 6 / 6; names identical, order identical |
| `json['clients'][0]['functions']` | 3 / 3; `close` is `"Normal Function"` on **both** sides |
| `old.json['readme'] == new.json['readme']` | `True` |
| `new.json['readme'].strip() == docs/README.md.strip()` | `True` (124 lines) |
| `package.json` `export` | `["aws.marketplace.mpe"]`; `modules/` has 1 dir |
| `curl api.central.ballerina.io/.../1.0.0` | 1 module, `deprecated: None`, `ballerinaVersion 2201.12.0`, `pullCount 4` |
| `client.bal:71` | `public isolated function close() returns Error? = @java:Method ... external;` — **not** remote |
| `client.bal:51` | `isolated remote function getEntitlements(*EntitlementsRequest request)` |
| `client.bal:33` | `public isolated function init(*ConnectionConfig configs) returns Error?` |
| `errors.bal:20` | `public type Error distinct error<aws:ErrorDetails>;` |
| `types.bal:39-42,49-51,58-60,63-65` | the 4 `@constraint` annotations, matching the render verbatim |
| `grep -c 'record {|'` / `'record {$'` in new | 0 / 5 |

## 10. Caveats and unverified items

- **`aws:Region` enum contents not verified.** The 55-member region union in `init` was not checked
  against `ballerinax/aws` 1.0.1's `Region` enum — that dependency package was out of scope and its bala
  was not inspected. The union text is byte-identical between `old` and `new`, so this cannot be a
  regression either way; it is only unverified as an absolute-accuracy claim.
- **Renderer source not read.** The `close()` `remote` → plain change is attributed to `toSyntaxString`
  because the two JSONs are identical at that point (`"type": "Normal Function"` on both sides). The
  `ballerina-vscode` TypeScript source was not inspected to confirm the exact code change.
- **`distinct` loss localised to the extractor by inference**, not by reading `ModelToJsonConverter`:
  the `new` JSON's `baseType` field is already `"error<aws:ErrorDetails>"` without `distinct`, so the
  renderer cannot be at fault. The Java source was not read.
- **No build/compile check was run** on either render; "non-compiling" claims in §5.6/§5.7 are from
  reading the syntax, not from `bal build`.

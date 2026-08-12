# ballerinax/peoplehr 2.2.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/peoplehr` |
| Pinned version | `2.2.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-peoplehr |
| Tag reviewed | `v2.2.1` (commit `2ffe959b25d7c1610bea1c8a374b82b39287d0fc`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/peoplehr/2.2.1` |
| Old render | `1345` lines |
| New render | `1374` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is byte-for-byte identical to `old` except that it emits the library's `@display`
annotations. Stripping every `@display` construct from `new` reproduces `old` exactly
(1345 lines vs 1345 lines, zero residual diff). All 53 `@display` annotations present in the
published source appear in `new`, with values and symbol attachment matching the source
one-for-one. Nothing was dropped, truncated, reordered, or re-typed. No regression.

The library is a single-module connector (default module `peoplehr`) with 59 public types,
1 public client class, 26 remote methods and no compiler plugin. Both renders cover 100% of
that public surface. The upstream tag source and the bala module source are byte-identical.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 1345 | 1374 |
| Diff hunks | 2 | |
| Lines added | 53 | |
| Lines removed | 24 | |
| `// Unknown type:` placeholders | 0 | 0 |
| Version-qualified type refs (`mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `// Special Agent Note:` lines | 11 | 11 |
| `type` declarations | 59 | 59 |
| `client class` declarations | 1 | 1 |
| `remote function` declarations | 26 | 26 |
| `@display` occurrences | 0 | 53 |

Declarations added: **0**. Declarations removed: **0**. Declarations modified: **26 remote
functions + 1 client class + 1 record type + 1 record field**, and in every case the only
modification is an attached `@display` annotation.

All 24 "removed" diff lines are the un-annotated versions of 24 remote-function signature
lines; the corresponding `+` lines are identical apart from a prefixed/inline `@display`.
The other 29 added lines are standalone `@display` lines (24 of them are the net +29 line growth
together with the 1 class-level, 1 type-level, 1 field-level and 2 zero-param method
annotations).

JSON level: `old` JSON is 5354 lines, `new` 5672. Structural key diff is purely additive —
`annotations` (with `name`/`value`) appears on `clients[]`, `clients[].functions[]`,
`clients[].functions[].parameters[]`, `typeDefs[]` and `typeDefs[].fields[]` in `new` and
nowhere in `old`. Deleting the `annotations` key from `new` makes the two JSON documents
compare `==` in Python. `new` carries exactly 53 annotation entries.

Breakdown of the 53 new annotations:

| Attachment point | count |
|---|---|
| Client class (`Client`) | 1 |
| Remote function | 26 |
| Remote function parameter (`payload`) | 24 |
| Type definition (`ConnectionConfig`) | 1 |
| Record field (`apiKey`) | 1 |

## 3. Correctness against library source

Source of truth: the bala module sources, which `diff` reports **identical** to the `v2.2.1`
tag sources for all three files (`client.bal`, `constants.bal`, `types.bal`).

- **Annotation count.** `grep -o '@display' src/peoplehr/*.bal | wc -l` = 53;
  same count in `new` render = 53; same count in `new` JSON = 53.
- **Annotation values.** Extracted all `label:` string values from source (53) and from the
  `new` render (53) and compared as multisets: `in source not render: Counter()`,
  `in render not source: Counter()`. `iconPath` = `["icon.png"]` on both sides;
  `kind` = `["password"]` on both sides.
- **Annotation attachment.** Regex-paired `(label, function-name)` from `src/peoplehr/client.bal`
  (26 pairs) against the same pairs read out of `new`'s JSON `clients[0].functions[]`
  (26 pairs) — zero mismatches. Parameter-level annotations: 24 in source, 24 in `new` JSON.
- **Faithful reproduction of an upstream copy-paste bug.** `client.bal:385` labels
  `getAppraisalDetailsByAppraisalID` as `"Get Appraisal details by employee ID"` — the same
  label used for `getAppraisalDetailsByEmployeeID` at `client.bal:372`. `new` reproduces this
  verbatim. This is a library defect, not a renderer defect.
- **Signatures.** All 26 remote-function signatures extracted from `client.bal` (name, params,
  return type) match the render exactly, e.g.
  `createNewEmployee(NewEmployeeRequest|json payload) returns OperationStatus|error`
  (`client.bal:47`), `getAllVacancies() returns AllVacancies|error` (`client.bal:213-214`),
  `DeleteCustomScreenTransaction(ScreenDetailByTransactionIDRequest payload) returns
  OperationStatus|error` (`client.bal:360`).
- **Type set.** The 59 `public type` names in `types.bal` and the 59 type names in the render
  are the same set (`comm -23` and `comm -13` both empty).
- **`init`.** Source `client.bal:36` `public isolated function init(ConnectionConfig config)
  returns error?`; render `function init(ConnectionConfig config) returns error?` (see §5 on
  the dropped `isolated`/`public` qualifiers, which are shared with `old`).
- **Record inclusion flattening.** `QueryDetail` / `EmployeesResponse` etc. include
  `*PeopleHRGenericResponse`; both renders flatten the three inherited fields
  (`isError`, `Status`, `Message`) inline with correct types. Verified against
  `types.bal:43-55`.
- **Nested/union field types.** `types.bal:69` `Employee?|record {} Result;` renders as
  `Employee|()|record {|anydata...;|} Result;` (render line 337) — semantically equivalent
  (`record {}` is the open inclusive record). Identical in `old`.
- **README.** The `// --- README ---` block (render lines 8-61) is `docs/Package.md` followed
  by `## Module: peoplehr` and the full `docs/modules/peoplehr/Module.md`. Nothing truncated.
  Identical in `old` and `new`.

## 4. Regressions

**None found.**

Basis for that conclusion, all mechanically verified:

1. Normalising `new` by deleting standalone `@display {...}` lines and stripping inline
   `@display {...} ` prefixes yields a file of exactly 1345 lines that is **identical to
   `old`** (`difflib.unified_diff` returns 0 lines).
2. Stripping the `annotations` key recursively from the `new` JSON makes it compare equal
   (`==`) to the `old` JSON. So no field value, type, doc string, ordering or nullability
   changed at the model level either.
3. Declaration counts are unchanged in every category (59 types, 1 client class, 26 remote
   functions, 4 section markers, 11 "Special Agent Note" comments).
4. `// Unknown type:` count is 0 on both sides — this library had no degraded types under
   `main`, so the headline spec-v2 improvement does not apply here; the improvement here is
   annotation capture only.

## 5. Issues in `new` (independent of `old`)

These are inaccuracies present in `new`. All four are **also present in `old`** (the two files
are identical modulo annotations), so none is a regression — but they are worth recording.

1. **Field default values are dropped.** `types.bal:31` declares
   `string baseURL = "https://api.peoplehr.net";` inside `ConnectionConfig`. Both renders emit
   `string baseURL?` — the field is correctly marked optional but the default endpoint is lost.
   An LLM reading this render cannot learn the default base URL from the type (it can still
   find it in the README quickstart snippet, which is included). This is the only defaulted
   field in the whole library (`grep -nE '^\s+[A-Za-z_].*=\s*[^=]' types.bal` → 1 hit).
2. **Parameter and return doc lines are dropped for client methods.** `client.bal` contains 54
   `# + ...` doc lines (`# + payload - ...`, `# + return - ...`); the render contains 0. Each
   method is left with its summary line plus a dangling `# ` line. Record-field docs, by
   contrast, ARE preserved and re-attached to the correct fields.
3. **Closed records are rendered as open.** `types.bal` has 35 `record {|` declarations; the
   render has 3, and all 3 are inline anonymous `record {|anydata...;|}` types inside union
   fields. Every named closed record (e.g. `NewEmployeeRequest`, `types.bal:527`) is rendered
   as `record {` — i.e. the render implies extra fields are permitted where the library
   forbids them.
4. **`public` and `isolated` qualifiers are dropped.** Source declares
   `public isolated client class Client` (`client.bal:25`) and `isolated remote function ...`
   (26 occurrences); the render emits `client class Client` and `remote function ...`. Likewise
   all 59 `public type` become bare `type`. This appears to be a deliberate render convention
   (the render is a synthetic API surface, not compilable source), but it means the render is
   not literally valid module-external Ballerina.

## 6. Coverage gaps vs. the library

**0 gaps.**

- `package.json` `export` = `["peoplehr"]`; Central metadata lists exactly one module,
  `peoplehr`. There is no submodule, so the known `getDefaultModule()`-only limitation has no
  effect on this library.
- Public symbols in the default module: 59 `public type` + `public isolated client class Client`
  (+ its `public isolated function init`). All 59 type names and the client class with all 26
  remote methods and `init` are present in both renders (set comparison, §3).
- The 7 `const string` path constants in `constants.bal` are module-private (no `public`
  modifier) and are correctly absent from both renders.

## 7. Compiler plugin

The package has **no compiler plugin**. `find src -iname '*compiler-plugin*'` returns nothing
in the v2.2.1 tree, and the bala contains no `compiler-plugin/` directory (bala root holds only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing is expected
to surface in the render from a plugin, and nothing is missing on that account.

## 8. Other considerations

- **Stale/legacy package.** Built with `ballerina_version: 2201.4.1` (Central `createdDate`
  2024-02-15), language spec `2022R4`. Not deprecated (`deprecated: null`). Pull count 93.
- **Upstream defects reproduced faithfully.** Besides the duplicated appraisal label (§3), the
  library ships a non-idiomatic exported method name `DeleteCustomScreenTransaction` (PascalCase)
  and typos in doc text (`sucess` in the client doc, `an new employee`). The render carries
  these through unaltered — correct behaviour for a fidelity renderer.
- **Size / token impact.** +29 lines (+2.2%), +318 JSON lines (+5.9%). Negligible cost for
  recovering UI/label metadata (including the `kind: "password"` marker on `apiKey`, which is
  a genuinely useful signal that the field is a secret).
- **`@display {label: ""}`** on `apiKey` has an intentionally empty label in the source
  (`types.bal:25-28`); the render reproduces the empty string rather than omitting the key.
  Correct, if odd-looking.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` on both renders | old 1345, new 1374 |
| `git ls-remote --tags <repo>` | `v2.2.1` → `2ffe959b25d7c1610bea1c8a374b82b39287d0fc` (exact match exists) |
| `git clone --depth 1 --branch v2.2.1` | success; tree = LICENSE, README.md, issue_template.md, peoplehr/, pull_request_template.md |
| `diff src/peoplehr/{client,constants,types}.bal` vs bala `modules/peoplehr/` | identical for all 3 files |
| `wc -l src/peoplehr/*.bal` | client 393, constants 24, types 1078 (1495 total) |
| `grep -n '^// --- ' old/new` | old: 7, 62, 64, 1234; new: 7, 62, 64, 1236 |
| `grep -c '^// Unknown type:' old/new` | 0 / 0 |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:' old/new` | 0 / 0 |
| `grep -c 'Special Agent Note' old/new` | 11 / 11 |
| `diff -u old new \| grep -c '^@@'` | 2 hunks |
| `diff -u old new \| grep -c '^-[^-]'` / `'^+[^+]'` | 24 removed / 53 added |
| `diff -u old new \| grep '^+[^+]' \| grep -vc '@display'` | 0 (every added line contains `@display`) |
| Python: strip `@display` from `new`, `difflib` vs `old` | new normalized = 1345 lines; residual diff = **0 lines** |
| Python: recursive key-set diff of the two JSONs | only-old = `[]`; only-new = 15 paths, all under `annotations` |
| Python: `strip_annotations(old) == strip_annotations(new)` | `True` |
| Python: count annotation entries in new JSON | 53 |
| `grep -o '@display' src/peoplehr/*.bal \| wc -l` | 53 |
| `grep -o '@display' new render \| wc -l` | 53 |
| Python: multiset compare of `label:` values source vs new render | 53 vs 53, both differences empty |
| `iconPath` / `kind` values source vs render | `icon.png` / `password` on both |
| Python: `(label, fn-name)` pairs source `client.bal` vs new JSON | 26 vs 26, zero mismatches |
| Python: parameter-level annotations source vs new JSON | 24 vs 24 |
| `grep -c 'remote function'` src / old / new | 26 / 26 / 26 |
| `grep -cE '^public type' types.bal` vs `grep -cE '^(public )?type ' new render` | 59 / 59 |
| `comm` on sorted type-name lists (src vs new render) | both directions empty |
| `grep -hnE '^\s*public ' src/peoplehr/*.bal` (non-type) | only `client.bal:25` class, `client.bal:36` init |
| `cat src/peoplehr/constants.bal` | 7 `const string` paths, all non-public → correctly absent from render |
| `find src -iname '*compiler-plugin*'`; `ls bala/any` | no plugin; bala root has no `compiler-plugin/` |
| `cat bala/any/package.json` | `export: ["peoplehr"]`, `ballerina_version: 2201.4.1`, icon `docs/icon.png` |
| `curl` Central `/2.0/registry/packages/ballerinax/peoplehr/2.2.1` | 1 module, `deprecated: null`, pullCount 93 |
| `diff Package.md` vs render README block (lines 8-61) | render = Package.md + `## Module: peoplehr` + Module.md, nothing lost |
| `grep -c 'record {|'` src types.bal / new render / old render | 35 / 3 / 3 |
| `grep -cE '^\s*# \+ '` src client.bal / new render | 54 / 0 |
| `grep -nE '^\s+[A-Za-z_].*=\s*[^=]' types.bal` | 1 hit (`baseURL = "https://api.peoplehr.net"`, line 31) |
| Read `new` render lines 64-85, 95-140, 335-341, 365-371, 676-688 | spot-checked against `types.bal:20-31, 38-110, 527-539` — all consistent |
| Reviewed `OLD_AND_NEW_DIFFS/peoplehr_diff.md` | its figures (1345/1374, +53/−24, 2 hunks, 0 decls added/removed) all reproduced independently |

## 10. Caveats and unverified items

- Neither render was compiled; "malformed syntax" was assessed by inspection only. The renders
  are intentionally not compilable module-external Ballerina anyway (missing `public`/`isolated`
  qualifiers, §5.4), so a compile check would not be meaningful.
- I did not execute the two-stage pipeline myself; the `old` and `new` artefacts were taken as
  given from the manifest paths. The claim that both were produced at the same pinned version is
  taken from the brief (`PIN_OK`) and is corroborated by the fact that the two renders are
  identical modulo annotations and that the render's type set matches the v2.2.1 sources exactly.
- The `@display` annotation semantics (that `kind: "password"` marks a secret, that `iconPath` is
  relative to `docs/`) are read from Ballerina convention, not from a spec document I consulted.
- `src/peoplehr/tests/test.bal` was excluded from all source counts (test module, not part of the
  published API); the bala contains no test sources, confirming it is not extracted.

# ballerinax/snowflake 2.2.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/snowflake` |
| Pinned version | `2.2.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-snowflake |
| Tag reviewed | `v2.2.2` (commit `b020253`, exact match) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/snowflake/2.2.2/java21` |
| Old render | `288` lines |
| New render | `290` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module connector (2 `.bal` files, 268 lines, 6 public symbols). `new` differs from
`old` in exactly 3 hunks / 8 changed lines, and every one of those changes moves the render **closer**
to the library source:

- the truncated return type `Error?>` on `query()` is repaired to `stream<rowType, sql:Error?>` (both clients),
- version-qualified refs (`ballerinax/snowflake:2.2.2:BasicAuth`, `ballerina/sql:1.19.0:Error?`) are
  reduced to plain `BasicAuth` / `sql:Error?` (4 occurrences → 0),
- `close()` loses the incorrect `remote` qualifier (source declares it `public isolated function`),
- the `@display {label: "Snowflake", iconPath: "icon.png"}` annotation on both client classes is now emitted.

No declaration is added or removed. No regression found. A handful of fidelity problems exist in
`new`, but every one of them is byte-identical in `old`, so they are pre-existing, not introduced.

## 2. Change inventory

Declaration name sets are identical apart from the `remote` keyword on `close`:

```
diff <(grep -oE '^(client class|type) [A-Za-z]+|^\s+(remote )?function [a-zA-Z]+' old/...) <(same for new)
→ only: "remote function close" ×2  →  "function close" ×2
```

| Kind | old | new | added | removed | modified |
|---|---|---|---|---|---|
| `type` (record) | 3 (`Options`, `BasicAuth`, `KeyBasedAuth`) | 3 | 0 | 0 | 0 |
| `type` (union) | 1 (`AuthConfig`) | 1 | 0 | 0 | 1 (deref'd) |
| `client class` | 2 (`Client`, `AdvancedClient`) | 2 | 0 | 0 | 2 (annotation added) |
| client methods | 16 (8 × 2 classes) | 16 | 0 | 0 | 6 (`init` ×2, `query` ×2, `close` ×2) |
| annotations emitted | 0 | 2 | +2 | 0 | — |
| **total declarations** | **22** | **22** | 0 | 0 | 9 |

Signals (measured, not copied from the mechanical diff):

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| `org/mod:x.y.z:Type` qualified refs | 4 | 0 |
| `// --- section ---` markers | 4 | 4 |
| README section | lines 8–181 | lines 8–181 |

README block is byte-identical between the two renders and byte-identical to the bala's
`docs/README.md` (all 174 lines, nothing truncated).

JSON diff is the same 6 corrections plus 2 `annotations` arrays (`old/*.json` 32,959 B → `new/*.json` 33,219 B).

## 3. Correctness against library source

Upstream `v2.2.2` `ballerina/client.bal` and `ballerina/advanced_client.bal` are **byte-identical** to
the bala's `modules/snowflake/*.bal` (`diff` exit 0 for both), so source and bala agree everywhere.

Each `new`-side change verified against the source:

| Change in `new` | Source evidence | Correct? |
|---|---|---|
| `query(...) returns stream<rowType, sql:Error?>` | `client.bal:48` / `advanced_client.bal:48` `returns stream<rowType, sql:Error?>` | ✅ `new` correct, `old` (`Error?>`) truncated |
| `init(...) returns sql:Error?` | `client.bal:35`, `advanced_client.bal:35` | ✅ |
| `type AuthConfig BasicAuth\|KeyBasedAuth;` | `client.bal:131` `public type AuthConfig BasicAuth\|KeyBasedAuth;` | ✅ |
| `function close()` (no `remote`) | `client.bal:104` / `advanced_client.bal:104` `public isolated function close()` — **not** a remote method | ✅ `new` correct, `old` wrong |
| `@display {label: "Snowflake", iconPath: "icon.png"}` | `client.bal:21`, `advanced_client.bal:21` — verbatim | ✅ |

Unchanged declarations spot-checked against source (all match): `Options` (`client.bal:111`),
`BasicAuth` (`:134`), `KeyBasedAuth` (`:142`), `queryRow` (`:60`), `execute` (`:70`),
`batchExecute` (`:83`), `call` (`:95`).

## 4. Regressions

**None found.**

Checked: (a) full `diff -u old new` — all 3 hunks reviewed line by line, every one is a correction;
(b) declaration name sets compared after sort — identical except the `remote` keyword removal, which
matches source; (c) README section byte-compared old↔new — identical; (d) section markers 4↔4;
(e) `// Unknown type:` 0↔0; (f) full JSON diff — 8 changed values, all corrections plus 2 added
annotation blocks; (g) no doc comment lost (`grep -c '^\s*# '` region unchanged outside hunks);
(h) no declaration, parameter, default value, or return type dropped.

## 5. Issues in `new` (independent of `old`)

All five are byte-identical in `old` — pre-existing extractor/renderer limitations, listed because
they mislead a consuming LLM, not because `new` caused them.

1. **Malformed doc continuation breaks the render's Ballerina syntax** — `new:211` (also `old:211`):
   ```
       # The path to the private key file. The private key file must be in the PKCS#8 format.
   Use forward slashes as file path separators on all operating systems, ...
       string privateKeyPath;
   ```
   The second physical line of the `privateKeyPath` doc (`client.bal:146`) is emitted without the
   `# ` prefix, inside a record body. The rendered file does not parse as Ballerina.
2. **Closed records rendered as open, field defaults dropped** — source `Options` is
   `record {| string? datasourceName = (); map<anydata>? properties = (); |}` (`client.bal:111-116`);
   render (`new:189-194`) emits `record { string? datasourceName?; map<anydata>? properties?; }` —
   loses `{| |}` and converts defaulted fields to optional fields. Same for `BasicAuth` /
   `KeyBasedAuth` (`client.bal:134`, `:142`), which are also `{| |}`.
3. **`typedesc` inferred-type parameters mangled** — source `typedesc<record {}> rowType = <>`
   (`client.bal:47`) renders as `record {|anydata...;|} rowType = record {|anydata...;|}`
   (`new:230`, `:265`): the parameter is no longer a `typedesc`, and the default is not a valid
   expression. Same for `queryRow`: `typedesc<anydata> returnType = <>` (`client.bal:60`) →
   `anydata returnType = anydata` (`new:235`, `:270`). Note `call` gets it right
   (`typedesc<record {|anydata...;|}>[] rowTypes = []`, `new:250`), so the defect is specific to the
   inferred-default (`= <>`) form.
4. **Dangling type parameters in return types** — a direct consequence of (3): `new:230` returns
   `stream<rowType, sql:Error?>` and `new:235` returns `returnType|sql:Error`, but after the mangling
   `rowType`/`returnType` are ordinary value parameters, not typedescs, so the return types do not
   resolve.
5. **Object inclusion and qualifiers not represented** — `*sql:Client` (`client.bal:23`,
   `advanced_client.bal:23`) is absent from both renders, as are `public`/`isolated`. The `*sql:Client`
   omission hides that these clients conform to the standard `sql:Client` object type. (Qualifier
   stripping appears to be the render format's convention.)

Minor/cosmetic: parameter-level docs (`+ sqlQuery - ...`) are dropped, leaving a bare trailing `# `
line on every method (both sides); `close()` returns `sql:Error|()` rather than `sql:Error?`
(semantically equal).

## 6. Coverage gaps vs. the library

**Zero gaps.** The bala exports exactly one module (`snowflake`, = default module;
`package.json` `"export": ["snowflake"]`, Central `modules` list has one entry), so there is no
submodule-only API on either side.

`grep -n '^public ' modules/snowflake/*.bal` yields all 6 public symbols, and all 6 appear in both renders:

| Public symbol | source | in old | in new |
|---|---|---|---|
| `AdvancedClient` | `advanced_client.bal:22` | ✅ | ✅ |
| `Client` | `client.bal:22` | ✅ | ✅ |
| `Options` | `client.bal:111` | ✅ | ✅ |
| `AuthConfig` | `client.bal:131` | ✅ | ✅ |
| `BasicAuth` | `client.bal:134` | ✅ | ✅ |
| `KeyBasedAuth` | `client.bal:142` | ✅ | ✅ |

Non-public symbols correctly absent from both: `ClientConfiguration` (`client.bal:119`),
`createClient` (`:152`), `nativeBatchExecute` (`:157`).

## 7. Compiler plugin

The package ships **no compiler plugin**: `find src -iname '*compiler-plugin*'` over the `v2.2.2`
clone returns nothing, and the bala has no `compiler-plugin/` directory (only
`docs/ modules/ platform/ bala.json dependency-graph.json package.json`). Nothing plugin-derived is
therefore expected in, or missing from, the render.

Native artefacts only: `platform/java21/snowflake-native-2.2.2.jar`, `sql-native-1.15.0.jar`.

## 8. Other considerations

- Not deprecated (Central `deprecated: null`, `deprecateMessage: ""`); stable 2.x; `visibility: public`;
  743 pulls; built with Ballerina `2201.11.0`.
- Size is trivial for token budget: 290 lines / ~13 KB rendered, of which 174 lines (60%) are README.
- The `@display` annotation now surfaced in `new` is useful metadata for tooling but adds no API surface.
- The bala pins `sql-native-1.15.0.jar`, while `old` rendered `ballerina/sql:1.19.0:Error?` — the
  version stamp in `old` was itself inconsistent with the bala's platform dependency, another reason
  the `new` unqualified `sql:Error?` is the better output.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 288 / 290 |
| 2 | `diff -u old/…bal.txt new/…bal.txt` | 3 hunks, 8 changed lines, listed in §2 |
| 3 | `grep -c '^// Unknown type:'` both | 0 / 0 |
| 4 | `grep -oE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:[A-Za-z]+' \| wc -l` | old 4, new 0 |
| 5 | `grep -n '^// --- '` both | 4 markers each, same line numbers (7, 183, 185, 220) |
| 6 | sorted declaration-name diff (client class/type/function) | identical except `remote function close` ×2 → `function close` ×2; 22 decls each side |
| 7 | `diff <(json.tool old.json) <(json.tool new.json)` | 6 value corrections + 2 `annotations` blocks added |
| 8 | `wc -c` JSONs | 32,959 → 33,219 |
| 9 | `git ls-remote --tags` | `v2.2.2` → `5d527da` / peeled `b020253` |
| 10 | `git clone --depth 1 --branch v2.2.2`; `git describe --tags` | `v2.2.2`, HEAD `b020253` |
| 11 | `diff bala/modules/snowflake/client.bal src/ballerina/client.bal` | identical |
| 12 | `diff bala/modules/snowflake/advanced_client.bal src/ballerina/advanced_client.bal` | identical |
| 13 | `wc -l bala modules/*.bal` | 108 + 160 = 268 |
| 14 | `grep -n '^public ' bala/modules/snowflake/*.bal` | 6 public symbols (table in §6) |
| 15 | `client.bal:104`, `advanced_client.bal:104` | `public isolated function close()` — not remote → `new` correct |
| 16 | `client.bal:48`, `advanced_client.bal:48` | `returns stream<rowType, sql:Error?>` → `new` correct |
| 17 | `client.bal:21`, `advanced_client.bal:21` | `@display {label: "Snowflake", iconPath: "icon.png"}` verbatim → `new` correct |
| 18 | `client.bal:131` | `public type AuthConfig BasicAuth\|KeyBasedAuth;` → `new` correct |
| 19 | `diff <(sed -n '8,181p' new) bala/docs/README.md` | identical |
| 20 | `diff <(sed -n '8,181p' old) <(sed -n '8,181p' new)` | identical |
| 21 | `find src -iname '*compiler-plugin*' -maxdepth 3` | no output → no plugin |
| 22 | `ls -R bala/…/2.2.2` | no `compiler-plugin/` dir |
| 23 | `cat bala/…/package.json` | `"export": ["snowflake"]`, single module, java21 |
| 24 | `curl api.central.ballerina.io/…/ballerinax/snowflake/2.2.2` | not deprecated, 1 module, pullCount 743 |
| 25 | `cat src/ballerina/Ballerina.toml` | `version = "2.2.2"` — pin confirmed on the upstream side |

## 10. Caveats and unverified items

- The renders were not compiled. The syntax defects in §5 (items 1, 3, 4) are asserted from reading
  the rendered text against the Ballerina grammar, not from a `bal build` run — the render is a
  documentation artefact and is not expected to compile as-is.
- I did not re-run the two-stage pipeline; I audited the committed `old`/`new` artefacts as given.
  Attribution of each change to spec v2 rests on the brief's stated old/new commits, which I did not
  independently check out.
- The `native/` Java sources were not reviewed; they contribute no Ballerina-visible API beyond the
  `external` bindings already read in the `.bal` files.
- Whether dropping `public`/`isolated` qualifiers and parameter-level docs is intentional render
  policy or a defect is unverified — I did not read the `toSyntaxString` implementation. Either way
  it is identical on both sides.

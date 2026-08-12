# ballerinax/aws.redshift 1.2.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.redshift` |
| Pinned version | `1.2.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.redshift |
| Tag reviewed | `v1.2.2` (commit `a72fa40`, "[Gradle Release Plugin] - pre tag commit: 'v1.2.2'") |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.redshift/1.2.2/java21` |
| Old render | `199` lines |
| New render | `200` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Tiny single-module library: the entire published API is one file (`modules/aws.redshift/client.bal`,
160 lines) containing `client class Client` (init + 5 remote methods + `close`), `type Options`,
`enum SslMode`. The upstream `v1.2.2` `ballerina/client.bal` is byte-identical to the bala's
`client.bal` (`diff` → IDENTICAL), so GitHub and the bala agree.

Lines 1–166 of the two renders are byte-identical (README + Types sections). All change is confined
to the `// --- Client ---` section: three fixes, zero losses.

1. `init` return type `ballerina/sql:1.19.0:Error?` → `sql:Error?` (version-qualified ref removed).
2. `query` return type `Error?>` (truncated, non-parsable) → `stream<rowType, sql:Error?>` (correct).
3. `close` rendered `remote function` → `function`, matching the source where `close` is a
   `public isolated function`, not a remote method.
4. `@display {label: "Redshift", iconPath: "icon.png"}` on `Client` is now emitted (present in the
   source, absent from `old`).

No declaration is added or removed. Every remaining inaccuracy in `new` is byte-for-byte present in
`old` too (verified: the only JSON deltas are the three above; lines 1–166 of the renders identical).

## 2. Change inventory

Declaration counts (grep over each render; `type` count excludes the `type User record {|` that
occurs inside the embedded README at line 97):

| kind | old | new | note |
|---|---|---|---|
| `// --- ` section markers | 4 | 4 | README / END README / Types / Client |
| `// Unknown type:` placeholders | 0 | 0 | no degraded types on either side |
| version-qualified type refs (`org/mod:x.y.z:T`) | 1 | 0 | the `init` return fixed |
| `const` | 3 | 3 | `DISABLE`, `VERIFY_CA`, `VERIFY_FULL` |
| record `type` decls | 1 | 1 | `Options` |
| `enum` | 1 | 1 | `SslMode` (3 members both sides) |
| `client class` | 1 | 1 | `Client` |
| `remote function` (in class) | 6 | 5 | `close` reclassified, not removed |
| non-remote `function` (in class) | 1 | 2 | `init`, `close` |
| annotations (`^@`) | 0 | 1 | `@display` on `Client` |

Declarations added: 0. Declarations removed: 0. Modified: 3 (`init` return, `query` return, `close`
qualifier) + 1 annotation gained.

JSON deltas (`diff -u` of both pretty-printed JSONs — exactly 3 hunks, nothing else):
- `clients[0].functions[init].return.type.name`: `"ballerina/sql:1.19.0:Error?"` → `"sql:Error?"`
- `clients[0].functions[query].return.type.name`: `"Error?>"` → `"stream<rowType, sql:Error?>"`
- `clients[0].annotations`: absent → `[{"name":"display","value":"{label: \"Redshift\", iconPath: \"icon.png\"}"}]`

The `close` change is **renderer-side only**: both JSONs carry `"close": {"type": "Normal Function"}`
identically; `old`'s `toSyntaxString` printed a "Normal Function" client method with the `remote`
keyword, `new` does not.

## 3. Correctness against library source

Checked against `work/aws.redshift/src/ballerina/client.bal` (= bala `modules/aws.redshift/client.bal`):

| render (new) | source | verdict |
|---|---|---|
| `@display {label: "Redshift", iconPath: "icon.png"}` (L169) | L20 identical annotation | correct |
| `function init(string url, string user, string password, Options|() options = (), sql:ConnectionPool|() connectionPool = ()) returns sql:Error?` (L171) | L34-35 `public isolated function init(string url, string user, string password, Options? options = (), sql:ConnectionPool? connectionPool = ()) returns sql:Error?` | correct (`?`→`|()`, `public isolated` dropped — renderer convention) |
| `remote function query(...) returns stream<rowType, sql:Error?>` (L175) | L51-52 `returns stream<rowType, sql:Error?>` | return now exactly correct |
| `remote function queryRow(...) returns returnType|sql:Error` (L180) | L64-65 | correct |
| `remote function execute(sql:ParameterizedQuery sqlQuery) returns sql:ExecutionResult|sql:Error` (L184) | L74-75 | correct |
| `remote function batchExecute(sql:ParameterizedQuery[] sqlQueries) returns sql:ExecutionResult[]|sql:Error` (L191) | L87 | correct |
| `remote function call(sql:ParameterizedCallQuery sqlQuery, typedesc<record {|anydata...;|}>[] rowTypes = []) returns sql:ProcedureCallResult|sql:Error` (L195) | L99-100 `typedesc<record {}>[] rowTypes = []` | correct |
| `function close() returns sql:Error|()` (L199) | L108 `public isolated function close() returns sql:Error?` | correct — **not** remote; `old` was wrong |
| `enum SslMode {VERIFY_FULL, VERIFY_CA, DISABLE}` (L161-165) | L126-133 `DISABLE, VERIFY_CA, VERIFY_FULL` | members correct, order reversed |
| `type Options record { string? datasourceName?; map<anydata>? properties?; SslMode sslMode?; }` (L151-158) | L119-123 closed `record {| string? datasourceName = (); map<anydata>? properties = (); SslMode sslMode = DISABLE; |}` | inaccurate (see §5.1) — identical in `old` |

Correctly excluded (module-private in source): `ClientConfiguration` (L143), `createClient` (L151),
`nativeBatchExecute` (L156). None appear in either render — correct.

## 4. Regressions

**None found.**

Basis for that conclusion:
- `diff -u old new` produces exactly 2 hunks / +4 / −3 lines; every removed line is the pre-fix form
  of a line that `new` re-emits in corrected form. No declaration, doc comment, parameter, default,
  or return type exists in `old` and is missing from `new`.
- `diff` of render lines 1–166 (banner, import, full README, Types section) → identical, so no
  README or type-section content was lost.
- Declaration-set comparison by kind (§2): identical counts except the `remote`→plain reclassification
  of `close`, which matches the source.
- JSON diff has exactly 3 hunks, all additive/corrective; no key removed.
- `// Unknown type:` count 0 → 0 (this library had no degraded types in `old`, so spec v2 has nothing
  to improve there); section markers 4 → 4.

## 5. Issues in `new` (independent of `old`)

All of these are also present verbatim in `old` — they are extractor/renderer-level, not new.

1. **`Options` field defaults and closedness lost.** Source is a closed record whose three fields all
   have defaults (`datasourceName = ()`, `properties = ()`, `sslMode = DISABLE`). The render shows an
   open record (`record {`) with all three fields *optional* (`sslMode?`). Already wrong in the JSON
   (`typeDefs[Options].fields[*].optional = true`, no `default` key), so it is an extractor gap. An
   LLM reading this cannot know that omitting `sslMode` means `DISABLE`, and may emit a rest field.
2. **Enum members duplicated as constants.** `DISABLE`, `VERIFY_CA`, `VERIFY_FULL` are emitted both as
   `const string X = "X";` (render L140/143/146, from JSON `typeDefs` entries of `"type": "Constant"`)
   and as `enum SslMode` members (L161-165). As Ballerina text this is a redeclared-symbol error — the
   render does not compile as written. There are no standalone public constants in the source
   (`client.bal` has none); these three come solely from the enum.
3. **Inferred-typedesc parameters mangled.** Source `typedesc<record {}> rowType = <>` renders as
   `record {|anydata...;|} rowType = record {|anydata...;|}`, and `typedesc<anydata> returnType = <>`
   renders as `anydata returnType = anydata`. Both the parameter type and the "default" are invented;
   `= record {|anydata...;|}` is not valid as a default expression. Same values in both JSONs.
4. **`*sql:Client` type inclusion not represented.** Source L22 includes the `sql:Client` object type;
   `grep -n 'sql:Client'` finds no hit in either render. Nothing in the render tells a consumer this
   client is substitutable for `sql:Client`.
5. **Per-parameter and per-return doc text dropped by the renderer.** The JSON carries every
   `+ param - description` and `+ return - description` string (e.g. `init.parameters[connectionPool].description`,
   `close.return.description = "Possible error when closing the client"`), but no `+ x - ...` line
   appears in the render — only the function's summary sentence survives. Information is present in
   the JSON and lost at `toSyntaxString`.
6. **`init`'s own doc dropped.** `clients[0].functions[init].description = "Initializes AWS Redshift client.\n"`
   exists in the JSON, but render L171 emits the `init` signature with no `#` doc line, unlike every
   other method.
7. **Missing `import ballerina/sql;`.** The render's only import is `import ballerinax/aws.redshift;`
   (L5) while the body uses `sql:ParameterizedQuery`, `sql:Error`, `sql:ConnectionPool`, etc. The
   trailing `// Special Agent Note: ... FROM ballerina/sql package` comments compensate textually, but
   the snippet is not self-contained.
8. **Cosmetic type spelling.** `sql:Error|()` (L199) and `Options|()` (L171) instead of the source's
   `sql:Error?` / `Options?`; `public` and `isolated` qualifiers dropped throughout; `SslMode` member
   order reversed relative to source. Harmless for meaning.

## 6. Coverage gaps vs. the library

`package.json` `export` = `["aws.redshift"]`; `modules/` contains exactly one directory,
`aws.redshift`, with one file `client.bal`. So the default module *is* the whole package — the
`getDefaultModule()`-only extraction limitation costs nothing here.

Public symbols of the default module and their presence:

| symbol | kind | in old | in new |
|---|---|---|---|
| `Client` | public isolated client class | yes | yes |
| `Client.init/query/queryRow/execute/batchExecute/call/close` | 7 methods | all 7 | all 7 |
| `Options` | public record type | yes | yes |
| `SslMode` | public enum | yes | yes |
| `DISABLE` / `VERIFY_CA` / `VERIFY_FULL` | enum members | yes | yes |

**Missing public symbols: 0.** Submodule-only API: none (single module). The `*sql:Client` inclusion
(§5.4) is a fidelity gap, not a missing symbol.

Adjacent note, not a gap in this render: the README (L71-76) instructs users to also import
`ballerinax/aws.redshift.driver as _`, which is a *separate package* not present in this bala and not
in the pinned library list; the render therefore documents an import it carries no API for.

## 7. Compiler plugin

There is none. `find src -maxdepth 2 -iname "*compiler*"` → no results; upstream top level has only
`ballerina/`, `native/`, `examples/`, `docs/`, `build-config/`. The bala has no
`compiler-plugin/compiler-plugin.json` (`ls` of the bala root shows only `bala.json`,
`dependency-graph.json`, `docs`, `modules`, `package.json`, `platform`). Nothing plugin-implied is
therefore missing from the render. The two platform jars (`aws.redshift-native-1.2.2.jar`,
`sql-native-1.15.0.jar`) are native `@java:Method` bindings, not a plugin.

## 8. Other considerations

- Version/stability: `1.2.2`, stable (>=1.0), not deprecated per `package.json`/Central metadata.
  `distribution = "2201.11.0"`, `graalvmCompatible = true`.
- Size: 200 lines total, of which lines 8–135 (128 lines, 64%) are the embedded README. Token cost is
  trivial; no truncation risk. The README is high quality (setup guide, quickstart, two runnable
  snippets) — the main value in this render for an LLM.
- The README snippets use `sql:ParameterizedQuery` and `io:println` without showing `import ballerina/sql`
  / `import ballerina/io`; that is upstream README content, faithfully reproduced, not a render defect.
- `new` is 1 line longer purely because of the added `@display` line.
- The `old` `query` return `Error?>` was actively harmful (a dangling `>`, no `stream<...>`), so the
  fix in `new` is the single most valuable change for this library.

## 9. Evidence log

| check | result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 199 / 200 |
| `diff -u old/…bal.txt new/…bal.txt` | 2 hunks, +4 / −3 lines, both inside `// --- Client ---` |
| `diff <(sed -n '1,166p' old) <(sed -n '1,166p' new)` | identical (README + Types unchanged) |
| `diff -u <(python3 -m json.tool old.json) <(python3 -m json.tool new.json)` | exactly 3 hunks: init return, query return, added `clients[0].annotations` |
| `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| `grep -c '^// --- '` both renders | 4 / 4 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | 1 / 0 |
| `grep -c '^    remote function '` / `'^    function '` | old 6/1, new 5/2 |
| `grep -c '^@'` both renders | 0 / 1 (`@display`) |
| `git ls-remote --tags <repo>` | `v1.2.2` exists → `a72fa40194942d800b09bb96cf7181bdcdd971ce` |
| `git clone --depth 1 --branch v1.2.2`; `git describe --tags` | `v1.2.2`, HEAD `a72fa40` |
| `diff src/ballerina/client.bal <bala>/modules/aws.redshift/client.bal` | IDENTICAL (no drift) |
| `cat src/ballerina/Ballerina.toml` | `org=ballerinax name=aws.redshift version=1.2.2` → PIN_OK |
| `cat <bala>/package.json` | `export: ["aws.redshift"]`, not deprecated, graalvmCompatible |
| `ls -R <bala>` | single module `aws.redshift`, single file `client.bal`; no `compiler-plugin/` |
| `find src -maxdepth 2 -iname "*compiler*"` | no results → no compiler plugin |
| source `client.bal:108` | `public isolated function close() returns sql:Error?` → not remote; `new` correct, `old` wrong |
| both JSONs `clients[0].functions[*].type` | identical lists; `close` = `"Normal Function"` on both sides → `remote` printing was a renderer bug in `old` |
| source `client.bal:119-123` vs render L151-158 | closed record + 3 defaults vs open record + 3 optional fields (same in both renders) |
| source `client.bal:126-133` vs render L161-165 | same 3 members, reversed order (both renders) |
| `grep -n 'sql:Client' old new` | no hits → `*sql:Client` inclusion absent from both |
| `grep -n 'import ' new` | only `import ballerinax/aws.redshift;` (L5) + two README lines |
| JSON `init.description`, `*.parameters[*].description`, `*.return.description` | present in JSON, absent from render text |

## 10. Caveats and unverified items

- The renders/JSONs were not regenerated in this review; I audited the committed artifacts as given.
  The claim that `close`'s `remote`→plain change is renderer-side is inferred from the two JSONs being
  identical on that field — I did not read the `toSyntaxString` source of either branch to confirm the
  code path.
- Ballerina Central metadata was taken from the bala's `package.json` (authoritative for the published
  artifact); I did not re-query `api.central.ballerina.io` in this session, so any Central-only fields
  (e.g. a post-publish deprecation flag) are unverified.
- Render validity claims (§5.2, §5.3) are by inspection of Ballerina syntax rules, not by compiling
  the render — the render is a prompt artifact and was never expected to compile verbatim.
- The `ballerinax/aws.redshift.driver` companion package referenced by the README was not inspected;
  it is outside the pinned library list.

# ballerinax/sap.commerce.webservices 0.9.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap.commerce.webservices` |
| Pinned version | `0.9.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap.commerce.webservices |
| Tag reviewed | `v0.9.1` (commit `3ab7399`, shallow clone) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap.commerce.webservices/0.9.1` |
| Old render | `8233` lines |
| New render | `8242` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The declaration set is byte-for-byte identical between `old` and `new` once three mechanical
transformations are applied. `new` differs from `old` in exactly three ways, all improvements:

1. **146** occurrences of the version-qualified type ref `ballerina/lang.int:0.0.0:Signed32` are
   replaced with the correct `int:Signed32`.
2. **231** bogus synthetic parameters `anydata Additional Values,` are removed from client method
   signatures. These were injected by `old` from the implicit `anydata` rest field of the open
   `*XQueries` included-record parameter and produced non-compiling Ballerina (a parameter name
   containing a space).
3. **9** annotation lines that exist in the library source but were dropped by `old` are now
   emitted: 3 × `@jsondata:Name`, 2 × `@http:Header`, 2 × `@constraint:String`,
   1 × `@constraint:Int`, 1 × `@display`.

Net line delta `+9` = the 9 added annotation lines; the other two transformations are in-place
line rewrites. No declaration, doc line, parameter, return type, or README content is lost.
Neither render contains `// Unknown type:` lines (0 in both), so the spec-v2 degraded-type fix is
not exercised by this library.

## 2. Change inventory

Declaration counts, both renders (identical):

| Kind | old | new | bala source |
|---|---|---|---|
| `type` declarations | 540 | 540 | 540 (`public type` in `types.bal`) |
| `client class` | 1 | 1 | 1 (`public isolated client class Client`) |
| `init` method | 1 | 1 | 1 |
| `remote function` | 337 | 337 | 337 (`remote isolated function`) |
| enum / const / annotation / listener / service | 0 | 0 | 0 |
| doc-comment lines (`# `) | 3198 | 3198 | — |
| `@deprecated` | 26 | 26 | 26 (6 in `types.bal`, 20 in `client.bal`) |
| other annotations | 0 | 9 | 9 |
| `// Unknown type:` | 0 | 0 | — |
| version-qualified type refs | 146 | 0 | — |
| `Additional Values` occurrences | 231 | 0 | — |

Set-equality checks (all passed):
- Type-name sets: `diff` of sorted `^type <Name>` from both renders → identical (540 each).
- Type-name set vs bala `public type` names → identical (540 = 540, `diff` empty).
- Client method signature lists after deleting the literal `anydata Additional Values, ` from the
  `old` lines → `diff` empty over 338 lines each. **No signature differs in any other respect.**
- README block (render lines 8–113) → identical between old and new, and identical to
  `any/docs/README.md` (only difference: trailing-newline at EOF).

Added / removed / modified: **0 declarations added, 0 removed.** 231 client methods modified
(bogus param dropped), 146 record-field lines modified (type ref), 9 fields/types gained an
annotation line.

## 3. Correctness against library source

The bala module source is byte-identical in size to the upstream `v0.9.1` tag
(`client.bal` 4891, `types.bal` 6226, `utils.bal` 304 lines in both), so GitHub and the bala agree.

Everything `new` adds was verified present in the bala source:

| New render | line | Bala source | line |
|---|---|---|---|
| `@jsondata:Name {value: "pA_ID"}` on `SAPCPQConfigurationAttribute.pAID` | 2761 | `types.bal` | 1239 |
| `@jsondata:Name {value: "paV_ID"}` | 2809 | `types.bal` | 3841 |
| `@jsondata:Name {value: "_messages"}` | 3407 | `types.bal` | 4535 |
| `@display {label: "Connection Config"}` on `ConnectionConfig` | 4044 | `types.bal` | 2684 |
| `@http:Header {name: "sap-commerce-cloud-captcha-token"}` (`CreateRegistrationRequestHeaders`) | 4152 | `types.bal` | 2794 |
| `@constraint:String {minLength: 1}` (`BundleStarter.productCode`) | 4202 | `types.bal` | 2855 |
| `@constraint:Int {minValue: 1}` (`BundleStarter.quantity`) | 4205 | `types.bal` | 2858 |
| `@constraint:String {minLength: 1}` (`BundleStarter.templateId`) | 4208 | `types.bal` | 2861 |
| `@http:Header {name: "sap-commerce-cloud-captcha-token"}` (`CreateUserHeaders`) | 5045 | `types.bal` | 4012 |

That is exactly the full set of non-`@deprecated` annotations in the module (9 in the source,
9 in `new`, 0 in `old`) — nothing invented, nothing missed.

The `int:Signed32` rewrite is correct: the bala source itself writes `int:Signed32`
(e.g. `types.bal:1240`, `client.bal:485`), so `new` now matches the source spelling while `old`
emitted `ballerina/lang.int:0.0.0:Signed32`, which is not valid Ballerina.

The removed `anydata Additional Values` parameter does not exist in any source signature; e.g.
`client.bal:45` is
`remote isolated function getBaseSites(map<string|string[]> headers = {}, *GetBaseSitesQueries queries) returns BaseSiteList|xml|error`.
Confirmed in the JSON: `old` carries a parameter object `{"name":"Additional Values",
"description":"Capture key value pairs","type":{"name":"anydata"},"optional":true}` that `new`
omits; all other parameter objects are identical.

Spot-checks of unchanged content against source: `init(ConnectionConfig config, string serviceUrl =
"http://localhost:9001/occ/v2") returns error?` (render 6873 vs `client.bal:34`) — exact match;
`getStoreLocations` / `searchComponentsByIds` / `updateCpqAttribute` / `validateCart` parameter
order and return types match `client.bal:1427 / 269 / 485 / 2814`.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Declaration-name sets are identical (type set diff empty; client method-name set diff empty via
  the JSON: `set(old)-set(new)` and `set(new)-set(old)` both empty over 338 methods).
- After normalising the single known `old` artefact (`anydata Additional Values, `), all 338 client
  signatures are textually identical between the two renders — so no parameter, default, or return
  type was dropped.
- Doc-comment line count identical (3198 / 3198); `Special Agent Note` cross-package hints identical
  (24 / 24); `@deprecated` count identical (26 / 26).
- README section identical.
- Brace balance is even in both (old 885/885, new 894/894).
- Non-ASCII line count identical (1 / 1) — no encoding change.
- `new` has 0 version-qualified refs and 0 `Unknown type` lines.

## 5. Issues in `new` (independent of `old`)

All eight below are **pre-existing and shared with `old`** — none is introduced by spec v2 — but
they are inaccuracies relative to the library source that persist in `new`.

1. **Included-record parameter loses its `*` and becomes a required trailing parameter.** Source:
   `..., map<string|string[]> headers = {}, *GetBaseSitesQueries queries)` (`client.bal:45`).
   Render: `..., map<string|string[]> headers = {}, string fields = "", GetBaseSitesQueries queries)`.
   A non-defaulted parameter after defaulted ones is not valid Ballerina, and the included-record
   fields are *also* flattened into the signature, so each query parameter appears twice. Affects
   all 231 methods that take a `*Queries` parameter.
2. **Real default values of the flattened query params are replaced by type-zero defaults.**
   `GetStoreLocationsQueries` in source (`types.bal`) has `pageSize = 20`, `sort = "asc"`,
   `fields = "DEFAULT"`, `radius = 100000.0`, `accuracy = 0`; the render emits
   `int:Signed32 pageSize = 0, string sort = "", string fields = "", decimal radius = 0.0d`
   (render 7293). An LLM reading this would send wrong defaults.
3. **Record fields with defaults are rendered as optional.** Same record: `string fields = "DEFAULT";`
   → `string fields?;`. Repo-wide, 1893 render lines end in `?;` on both sides while the source
   uses defaults for many of them.
4. **`public` modifier dropped from all 540 type declarations** (`public type X record` → `type X record`).
5. **`public isolated` dropped from the client class**: source `public isolated client class Client`
   (`client.bal:26`) → render `client class Client` (new line 6872).
6. **Closed records rendered as open.** `ConnectionConfig` (`types.bal:2685`),
   `OAuth2ClientCredentialsGrantConfig` (`types.bal:711`) and `OAuth2RefreshTokenGrantConfig`
   (`types.bal:1142`) are `record {| … |}` in source but `record { … }` in both renders
   (bala has 4 `record {|`, renders have 3 — the inline anonymous ones survive).
7. **Broken multi-line doc comment.** New line 4082–4083 emits the second line of the
   `laxDataBinding` doc as `and absent fields are handled as \`nilable\` types. Enabled by default.`
   with no leading `#`, i.e. a bare non-compiling line inside a record body. Identical defect at
   old line 4079.
8. **Parameter-level documentation is dropped.** The source documents every method with
   `# + baseSiteId - …` lines; the render emits `# ` + an empty `# ` line and no `+ param` entries
   (`grep -c '^    # + '` → 0 in both renders).

## 6. Coverage gaps vs. the library

**0 gaps.**

- `package.json` `export` lists exactly one module: `sap.commerce.webservices` (the default module).
- Public symbols in the default module: 540 `public type` (`types.bal`), 1 `public isolated client
  class Client` (`client.bal:26`). `utils.bal` has **no** `public` declarations (all 9 of its
  functions are module-private helpers). No public const, enum, annotation, listener, or service.
- All 540 type names and the client class with all 337 remote functions plus `init` appear in both
  renders — verified by an exact `diff` of the sorted name sets.
- Submodule `sap.commerce.webservices.mock.server` is declared `"export": false` in
  `package.json`, so its 151 `public` declarations are **not** part of the package's public API.
  Its absence from the render is correct, not a gap.

## 7. Compiler plugin

The package ships **no compiler plugin**: `find` over the `v0.9.1` clone for
`*compiler-plugin*` / `*compiler_plugin*` returns nothing, and the bala contains only
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json` — no
`compiler-plugin/compiler-plugin.json`. Nothing plugin-derived is therefore expected in the render,
and nothing is missing on that account.

## 8. Other considerations

- **Pre-1.0 version.** `0.9.1` is an unstable release; the API may change without a major bump.
- **Deprecations.** 26 `@deprecated` markers exist in the source (6 record fields, 20 client
  methods) and all 26 survive in both renders — good, since an LLM needs them.
- **`graalvmCompatible = true`**, distribution `2201.13.0`, no `template`.
- **Size / tokens.** 8242 lines, and the JSON payload shrank from 1,444,715 to 1,389,296 bytes
  (−55,419 B, −3.8%) because of the removed bogus parameters — a small but free token saving with
  no information loss.
- **Renders are not compilable as-is** (items 1, 5, 7 in §5). This is a renderer-wide property, not
  specific to this library, but consumers should not treat the output as valid Ballerina.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 8233 / 8242 |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -n '^// --- '` both | README 7/114, Types 116, Client 6860 (old) / 6869 (new) |
| `diff -u old new` | 2529 lines; 387 `+`, 378 `-` |
| `grep -c 'Additional Values'` old / new | 231 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 146 / 0 |
| `grep -oE '<org>/<mod>:<ver>:<Type>' old \| sort \| uniq -c` | 146 × `ballerina/lang.int:0.0.0:Signed32` (only one distinct) |
| `grep -E '^\s*@' new` minus `@deprecated` | 9 lines (3 jsondata, 2 http:Header, 2 constraint:String, 1 constraint:Int, 1 display) |
| same on `old` | 0 |
| `grep -nE '^\s*@' bala types.bal client.bal \| grep -v @deprecated` | 9 lines — one-to-one match with the 9 above |
| `grep -c '@deprecated'` bala | 6 (`types.bal`) + 20 (`client.bal`) = 26; renders 26 / 26 |
| `diff <(client sigs old \| sed 's/anydata Additional Values, //') <(client sigs new)` | empty, 338 lines each |
| `diff <(sorted type names old) <(sorted type names new)` | empty |
| `diff <(bala public type names) <(new render type names)` | empty, 540 / 540 |
| `grep -cE '^    remote function ' old/new` | 337 / 337 |
| `grep -cE '^(public )?type ' bala/types.bal` | 540 |
| `grep -cE '^    remote isolated function ' bala/client.bal` | 337 |
| `grep -c 'class Client' bala/client.bal` → `client.bal:26 public isolated client class Client` | render: `client class Client` (old 6863, new 6872) |
| `grep -c '^\s*# '` old / new | 3198 / 3198 |
| `grep -c 'Special Agent Note'` old / new | 24 / 24 |
| `grep -c -P '[^\x00-\x7F]'` old / new | 1 / 1 |
| brace counts `{` / `}` | old 885/885, new 894/894 |
| `grep -c 'record {\|'` bala vs renders | 4 vs 3 / 3 |
| `grep -c '^    # + '` old / new | 0 / 0 |
| `diff <(render README lines 8–113) bala/docs/README.md` | only "\ No newline at end of file" |
| JSON: `len(typeDefs)`, `len(clients)`, `len(client.functions)` | 540/1/338 both sides |
| JSON: method-name set difference old↔new | empty both directions |
| JSON: `getBaseSites` parameters | old has extra `{"name":"Additional Values","type":"anydata"}`; otherwise identical |
| `ls -la *.json` | old 1,444,715 B; new 1,389,296 B |
| `git clone --depth 1 --branch v0.9.1 …` | success, `3ab7399 (tag: v0.9.1)` |
| `wc -l` upstream `ballerina/*.bal` vs bala `modules/…/*.bal` | 4891 / 6226 / 304 in both — sources agree |
| `find src -iname '*compiler-plugin*'` | no results |
| bala `package.json` `export` | `["sap.commerce.webservices"]`; mock.server `"export": false` |
| `grep -cE '^public ' bala/utils.bal` | 0 |

## 10. Caveats and unverified items

- The clone is `--depth 1 --branch v0.9.1` (grafted), so commit history before the tag was not
  inspected. Not needed: the tagged tree matches the bala.
- Ballerina Central metadata was not re-queried over the network; module/export information was
  taken from the bala's `package.json`, which the brief designates as authoritative.
- Neither render was compiled. The "non-compiling" claims in §5 (items 1, 5, 7) are based on
  reading the Ballerina grammar rules, not on a `bal build` run; they apply equally to `old` and
  `new` and so do not affect the verdict.
- §5 items 2 and 3 were verified exhaustively for `GetStoreLocationsQueries` and spot-checked on
  `GetBaseSitesQueries`/`GetLanguagesQueries`; the repo-wide magnitude (339 `= `-defaulted lines
  and 1893 `?;` lines, identical on both sides) was measured but not field-by-field audited.

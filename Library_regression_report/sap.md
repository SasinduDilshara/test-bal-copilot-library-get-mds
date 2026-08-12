# ballerinax/sap 1.3.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/sap` |
| Pinned version | `1.3.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-sap |
| Tag reviewed | `v1.3.1` (commit `398ac7ffbe404ec0112dc6f7162f421ec7c7abfc`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/sap/1.3.1/java21` |
| Old render | `207` lines |
| New render | `209` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerinax/sap` is a very small library: one default module (`sap`) with exactly 5 public
declarations (`ClientError`, `CSRFTokenFetchFailure`, `TargetType`, `client isolated class Client`,
and `Client.init`). The whole public surface fits in 431 lines of `.bal`, so this review is
exhaustive rather than a spot-check.

Spec v2 changes the render in exactly three ways, all of them fixes:

1. The two error type aliases (`ClientError`, `CSRFTokenFetchFailure`) go from
   `// Unknown type: <Name>` placeholders to real, source-accurate definitions.
2. Version/module-qualified type references (`ballerina/http:2.16.6:Response`,
   `ballerinax/sap:1.3.1:ClientError`) are replaced with plain `http:Response` / `ClientError`.
3. The bogus, non-compiling parameter `http:QueryParamType Additional Values` (an identifier with a
   space in it) is removed from all 7 resource-function signatures.

Nothing is dropped, truncated, or made less accurate. **No regressions found.** Several
inaccuracies remain in `new`, but every one of them is also present in `old` (identical text), so
they are pre-existing pipeline limitations, not spec-v2 regressions.

## 2. Change inventory

Line counts (`wc -l`): old **207**, new **209**. Unified diff: 7 hunks, +13 / −11 lines.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 2 | 0 |
| `Additional Values` occurrences | 7 | 0 |
| `// --- ` section markers | 4 | 4 |
| README characters (JSON `readme` field) | 5131 | 5131 |
| JSON `typeDefs` | 3 | 3 |
| JSON `clients` | 1 | 1 |
| Client functions in JSON | 15 | 15 |

### Declarations added (2)

| Kind | Name | old | new |
|---|---|---|---|
| type (error alias) | `ClientError` | `// Unknown type: ClientError` | `type ClientError http:ClientError;` + doc line |
| type (error alias) | `CSRFTokenFetchFailure` | `// Unknown type: CSRFTokenFetchFailure` | `type CSRFTokenFetchFailure http:ClientError;` + doc line |

Underlying JSON cause: both `typeDefs` entries have `"type": "Error"`; `new` adds a
`"baseType": "http:ClientError"` field that `old` does not emit, which is what lets the renderer
produce a real definition instead of the placeholder.

### Declarations removed (0)

None. The declaration set is otherwise byte-identical: same 3 types, same 1 client class, same 15
client functions (`init` + 7 resource functions + 7 remote functions), same accessors and names on
both sides.

### Declarations modified (9)

| Kind | Name | Change |
|---|---|---|
| type | `TargetType` | `ballerina/http:2.16.6:Response\|anydata` → `http:Response\|anydata` |
| function | `Client.init` | return `ballerinax/sap:1.3.1:ClientError?` → `ClientError?` |
| resource fn | `post`, `put`, `patch`, `delete`, `head`, `get`, `options` (7) | parameter `http:QueryParamType Additional Values` removed; trailing "Special Agent Note" comment updated to drop `QueryParamType` |

The 7 remote functions (`post`/`put`/`patch`/`delete`/`head`/`get`/`options`) and the README block
are unchanged, byte for byte.

## 3. Correctness against library source

Upstream `v1.3.1` and the bala are **identical** — `diff` on all four `.bal` files and `README.md`
returned no differences (see Evidence log). So GitHub and bala agree; either can be cited.

| Rendered in `new` | Library source | Verdict |
|---|---|---|
| `type ClientError http:ClientError;` with doc "Defines the possible client error types." | `errors.bal:18-19` — `# Defines the possible client error types.` / `public type ClientError http:ClientError;` | exact (minus `public`) |
| `type CSRFTokenFetchFailure http:ClientError;` with doc "Represents an error, which occured due to a CSRF token fetch failure." | `errors.bal:21-22` — same doc (typo "occured" is upstream's) / `public type CSRFTokenFetchFailure http:ClientError;` | exact (minus `public`) |
| `type TargetType http:Response\|anydata;` | `sap_http_client.bal:20-21` — `public type TargetType http:Response\|anydata;` | exact (minus `public`) |
| `client class Client` with the two-line description | `sap_http_client.bal:23-25` — `public client isolated class Client` | correct; `public`/`isolated` dropped (also dropped in `old`) |
| `function init(string url, http:ClientConfiguration config) returns ClientError?` | `sap_http_client.bal:37` — `public isolated function init(string url, http:ClientConfiguration config) returns ClientError?` | signature and return correct |
| 7 remote functions, e.g. `remote function get(string path, map<string\|string[]>\|() headers = (), TargetType targetType = sap:TargetType) returns targetType\|ClientError` | `sap_http_client.bal:274-277` | param names/order/optionality correct; `typedesc<>` wrapper and `= <>` default mis-rendered (see §5) |
| 7 resource functions, e.g. `resource function get [... path](map<string\|string[]>\|() headers = (), TargetType targetType = sap:TargetType, http:QueryParams params) returns targetType\|ClientError` | `sap_http_client.bal:261-265` | param set now matches source exactly (3 params: `headers`, `targetType`, `params`); `old`'s 4th param was spurious |
| `resource function head [... path](...) returns http:Response\|ClientError` | `sap_http_client.bal:238-242` | exact |
| README block (125 lines) | `docs/README.md` (125 lines) | byte-identical to the bala README |

Removal of `Additional Values` verified as correct against source: `*http:QueryParams params` is a
single included-record parameter. `http:QueryParams` (`http_commons.bal:599-605` in the
`ballerina/http:2.16.6` bala) is `record {| never headers?; never targetType?; never message?;
never mediaType?; QueryParamType...; |}`. `old` flattened that record's **rest field descriptor**
into a separate parameter literally named `"Additional Values"` (JSON: `{"name":"Additional
Values","description":"Capture key value pairs","type":{"name":"QueryParamType"}}`), producing
`http:QueryParamType Additional Values` in the signature — an identifier containing a space, which
is not valid Ballerina and does not correspond to any parameter in the source. `new` correctly
emits only the 3 real parameters.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff -u old new` on the render (all 7 hunks read line by line) — every removed line has a
  corresponding added line that is strictly more accurate; no line was removed without replacement.
- Declaration sets compared from the JSON, not just the text: 3 typeDefs both sides (same names),
  1 client both sides, 15 client functions both sides with identical `accessor`/`name` pairs.
- Per-function parameter lists compared from the JSON. The only parameter that disappears anywhere
  is `Additional Values` (7 sites), which does not exist in the library source.
- README: `old['readme'] == new['readme']` → `True`, and both equal the bala `docs/README.md`.
  Library `description` field: `old == new` → `True`. No README/section content lost.
- Section markers: 4 on both sides, same names.
- Defaults, optionality flags and return types compared per parameter in the JSON — unchanged
  except for the two version-qualified return/type strings, which improved.

**One candidate considered and rejected.** Dropping `Additional Values` removes the only textual
hint that arbitrary extra query parameters may be supplied (the rest field `QueryParamType...` of
`http:QueryParams`). That is a small information loss. It is not scored as a regression because
(a) the information was rendered as non-compiling syntax that an LLM copying the render would
reproduce verbatim into broken code, and (b) the `http:QueryParams params` parameter that carries
the same semantics is still present on all 7 resource functions. Net effect is a correctness gain.

## 5. Issues in `new` (independent of `old`)

All six items below are **identical in `old`** — they are pipeline-wide limitations, not spec-v2
defects. Listed because they affect what an LLM would produce from this render.

1. **`typedesc<>` wrapper lost and a default invented.** Source (`sap_http_client.bal:56, 261, 274`
   etc.) declares `typedesc<TargetType> targetType = <>` (inferred typedesc default). All 12
   affected signatures render as `TargetType targetType = sap:TargetType`. Both the type and the
   default are wrong; `sap:TargetType` is not a valid expression. Present at 12 sites in both renders.
2. **Wrong default for `delete`'s `message`.** Source (`sap_http_client.bal:195, 210`) is
   `http:RequestMessage message = ()`. Both renders emit `message = {}` (2 sites, `grep -c` = 2 on
   both files).
3. **Path parameter type dropped.** Source declares `[http:PathParamType... path]`; both renders
   emit `[... path]`. `grep -c PathParamType` = 0 on both files.
4. **Included-record parameter marker lost.** Source `*http:QueryParams params`; both renders emit
   `http:QueryParams params` without the `*`.
5. **`public` / `isolated` qualifiers never emitted.** `grep -cE '\b(isolated|public)\b'` = 0 on
   both renders, though every rendered declaration is `public` and the class and all its methods are
   `isolated`.
6. **Doc parameter/return descriptions dropped.** `grep -c '^\s*# + '` = 0 on both renders, yet the
   JSON carries a `description` for every parameter and return. Every function doc therefore ends
   with a dangling empty `# ` line (e.g. new render lines 155, 159, 163…).
7. **`http:` prefix used without an import.** The render's only import is `import ballerinax/sap;`
   (line 5), but the body references `http:ClientError`, `http:Response`, `http:ClientConfiguration`,
   `http:RequestMessage`, `http:QueryParams`. Same on both sides. The trailing
   `// Special Agent Note: ... FROM ballerina/http package` comments partially compensate.

No invented symbols, no encoding problems, no mangled doc text found in `new`.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.** The default module `sap` exports exactly 5 public declarations
(`grep -nE '^\s*public\b' modules/sap/*.bal` in the bala):

| Symbol | File:line | In render? |
|---|---|---|
| `public type ClientError` | `errors.bal:19` | yes (new only; `old` had the placeholder) |
| `public type CSRFTokenFetchFailure` | `errors.bal:22` | yes (new only; `old` had the placeholder) |
| `public type TargetType` | `sap_http_client.bal:21` | yes (both) |
| `public client isolated class Client` | `sap_http_client.bal:25` | yes (both) |
| `public isolated function init(...)` | `sap_http_client.bal:37` | yes (both) |

Correctly excluded: the 4 module-private consts in `constants.bal` (`SAP_CSRF_HEADER`,
`ACCEPT_HEADER`, `SAP_CSRF_TOKEN_FETCH`, `SAP_CSRF_TOKEN_FAILURE_HEADER_VALUE`), the private
`processGet`/`processPost`/… helpers, the module-private `isCSRFTokenFailure`, and `init.bal`'s
non-public `init()`/`setModule()`.

**Submodule API:** the bala has one extra module, `sap.mock`
(`modules/sap.mock/server.bal`). `package.json` marks it `{"name":"sap.mock","export":false}` — it
is not exported — and it contains **no** `public` declarations (only a test `service
/API_SALES_ORDER_SRV on new http:Listener(9093)` at line 18). So the `getDefaultModule()`-only
extraction loses nothing here. This library has no shared submodule gap.

## 7. Compiler plugin

**This package ships no compiler plugin.** Evidence:
- `ls -a` on the bala root shows only `bala.json`, `dependency-graph.json`, `docs`, `modules`,
  `package.json`, `platform` — no `compiler-plugin/` directory and no `compiler-plugin.json`.
- Upstream `settings.gradle` at `v1.3.1` includes only `:checkstyle`, `:sap-native`,
  `:sap-ballerina`, `:sap-examples` — no compiler-plugin subproject; `find src -iname
  '*compiler-plugin*'` returns nothing.

The only native contribution is the `sap-native-1.3.1.jar` platform dependency
(`io.ballerina.lib.sap`), backing the `@java:Method` external functions. Those externals are
correctly surfaced as ordinary methods in both renders. Nothing plugin-implied is missing.

## 8. Other considerations

- **Version status:** stable 1.3.1, not deprecated. `package.json` keywords: Business
  Management/ERP, Cost/Paid, Vendor/SAP, Area/ERP & Business Operations, Type/Connector. Built for
  `ballerina_version` 2201.13.0, `graalvmCompatible: true`.
- **Size / tokens:** trivially small (11.4 KB new render vs 11.7 KB old — the render shrank slightly
  even while gaining 2 lines, because 7 long spurious parameters were removed). README is 5131 chars
  = ~60% of the render; the API surface itself is ~75 lines.
- **Doc quality:** upstream doc typo "occured" (`errors.bal:21`) is faithfully carried through — an
  upstream issue, not a render issue.
- **Render is still not compilable Ballerina** on either side (missing `import ballerina/http;`,
  `targetType = sap:TargetType` defaults, `[... path]` untyped rest path). That is by design for
  this format, but consumers should not treat the output as copy-pasteable.
- **JSON payload shrank** 44,937 → 41,650 bytes, consistent with dropping 7 spurious parameter
  objects while adding 2 short `baseType` fields.

## 9. Evidence log

| # | Command / file:line | Result |
|---|---|---|
| 1 | `wc -l sap/{old,new}/ballerinax_sap.bal.txt` | old 207, new 209 |
| 2 | `diff -u old/ballerinax_sap.bal.txt new/ballerinax_sap.bal.txt` | 7 hunks; only the changes listed in §2 |
| 3 | `grep -c '^// Unknown type:'` on both | old 2, new 0 |
| 4 | `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` on both | old lines 143 & 150; new 0 matches |
| 5 | `grep -c 'Additional Values'` on both | old 7, new 0 |
| 6 | `grep -n '^// --- '` on both | old 7/134/136/145; new 7/134/136/147 — 4 markers each, same names |
| 7 | `ls -R` bala `1.3.1` | `java21/{bala.json,dependency-graph.json,docs,modules,package.json,platform}`; modules = `sap`, `sap.mock`; no compiler-plugin |
| 8 | `cat` bala `java21/package.json` | `export: ["sap"]`; `modules: [{"name":"sap.mock","export":false}]`; ballerina_version 2201.13.0 |
| 9 | `grep -nE '^\s*public\b' bala modules/sap/*.bal` | 5 hits: errors.bal:19,22; sap_http_client.bal:21,25,37 |
| 10 | `grep -nE '^\s*(public\|service\|listener)' bala modules/sap.mock/server.bal` | 1 hit, line 18, a non-public `service` — no public API |
| 11 | `git ls-remote --tags .../module-ballerinax-sap` | tags v1.0.0…v1.3.1; `v1.3.1` → `398ac7ffbe40…` |
| 12 | `git clone --depth 1 --branch v1.3.1`; `git rev-parse HEAD` | `398ac7ffbe404ec0112dc6f7162f421ec7c7abfc` |
| 13 | `grep -n version src/ballerina/Ballerina.toml` | `version = "1.3.1"` (lines 4, 21) — PIN_OK |
| 14 | `diff src/ballerina/{constants,errors,init,sap_http_client}.bal` vs bala `modules/sap/` | all 4 identical |
| 15 | `diff src/ballerina/README.md` vs bala `docs/README.md` | identical |
| 16 | `cat settings.gradle`; `find src -iname '*compiler-plugin*'` | includes checkstyle/native/ballerina/examples only; find → no results |
| 17 | Python: `o['readme']==n['readme']`, `n['readme']==bala README` | both `True`; 5131 chars each |
| 18 | Python: `o['description']==n['description']` | `True` |
| 19 | Python: per-side typeDefs/clients/functions counts | 3/1/15 on both sides; same names & accessors |
| 20 | Python: per-function parameter name lists, old vs new | identical except `Additional Values` removed from 7 resource functions |
| 21 | Python: dump of `get` resource function JSON, both sides | `old` has 4 params incl. `{"name":"Additional Values","description":"Capture key value pairs","type":{"name":"QueryParamType"}}`; `new` has 3 |
| 22 | Python: dump of `ClientError` typeDef, both sides | old `{name,description,type:"Error"}`; new adds `"baseType":"http:ClientError"` |
| 23 | `grep -rn -A6 'public type QueryParams'` in `ballerina/http:2.16.6` bala | `http_commons.bal:599-605`, rest field `QueryParamType...` — confirms `Additional Values` was the rest-field descriptor |
| 24 | `grep -n 'public type PathParamType'` same file | `http_commons.bal:586` — type exists, dropped by both renders |
| 25 | bala `sap_http_client.bal:55-56, 195, 210, 238-242, 261-265, 274-277` | source signatures used for the §3 comparison table |
| 26 | `grep -c 'message = {}'` on both renders | 2 on each (source says `= ()`) |
| 27 | `grep -c 'PathParamType'` / `grep -c 'typedesc'` on both renders | 0 / 0 on both |
| 28 | `grep -cE '\b(isolated\|public)\b'` on both renders | 0 on both |
| 29 | `grep -c '^\s*# + '` on both renders | 0 on both — param docs dropped |
| 30 | `grep -n '^import'` new render | lines 5 and 92 (line 92 is inside the README code block); no `ballerina/http` import |
| 31 | `ls -la sap/old sap/new` | old json 44,937 B / txt 11,659 B; new json 41,650 B / txt 11,363 B |
| 32 | `OLD_AND_NEW_DIFFS/sap_diff.md` | claims +13/−11, 7 hunks, 2 declarations added, 0 removed — all independently reproduced above |

## 10. Caveats and unverified items

- The `old` render's `TargetType ballerina/http:2.16.6:Response|anydata` line confirms `ballerina/http`
  2.16.6 was the resolved dependency at render time, matching the `http` bala I inspected for
  `QueryParams`/`PathParamType`. `dependency-graph.json` was not separately parsed to re-confirm the
  full transitive set; not material to any finding here.
- I did not compile either render with `bal build`. Statements that the renders are non-compiling
  rest on direct syntactic inspection (identifier with a space, missing import, `= sap:TargetType`
  as a default expression), not on a compiler run.
- The native jar (`sap-native-1.3.1.jar`) was not decompiled; behaviour of the `@java:Method`
  externals is taken from the Ballerina declarations, which is all the extractor sees.
- Nothing else was left unverified — the library is small enough that the public surface was checked
  exhaustively rather than sampled.

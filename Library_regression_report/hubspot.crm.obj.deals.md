# ballerinax/hubspot.crm.obj.deals 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.deals` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.deals |
| Tag reviewed | `v1.0.2` (exact tag, verified via `git ls-remote --tags`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.deals/1.0.2` |
| Old render | `795` lines |
| New render | `796` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module OpenAPI-generated HubSpot connector: 1 client class with 13 functions
(`init` + 12 resource methods) and 42 public types, all in the default module. The two renders are
declaration-for-declaration identical (same 42 types, same client, same 13 methods, byte-identical
README block of 7,984 chars). `new` differs in exactly three ways, all strict improvements:

1. 11 version/module-qualified type references (`ballerina/lang.int:0.0.0:Signed32`,
   `ballerinax/hubspot.crm.obj.deals:1.0.2:ValueWithTimestamp`) are now plain `int:Signed32` /
   `ValueWithTimestamp` — the old form is not valid Ballerina and would mislead a code-generating LLM.
2. `@display {label: "Connection Config"}` on `ConnectionConfig` is now emitted; it exists in the
   published source and was silently dropped by `old`.
3. A bogus synthetic parameter `anydata Additional Values` (an invalid identifier — contains a space)
   was emitted on 4 resource methods by `old` and is gone in `new`.

No declaration, parameter, default, return type, doc string, or README content was lost. Zero
regressions found. Several inaccuracies remain, but every one of them is present identically in
`old` and is therefore a shared renderer limitation, not a spec-v2 regression.

## 2. Change inventory

Line counts: `wc -l` → old 795, new 796 (net +1).
`diff -u` → 15 hunks, 16 lines added, 15 lines removed.

Declaration-set comparison (`diff` of `grep -E '^(type|class|enum|const|annotation|public|@)'`
over both files) yields a single line of difference — the added `@display` annotation.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations | 42 | 42 | 0 |
| client classes | 1 | 1 | 0 |
| client methods (`init` + resource) | 13 | 13 | 0 |
| enum / const / annotation / service / listener decls | 0 | 0 | 0 |
| `@display` annotations rendered | 0 | 1 | **+1** |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| version/module-qualified type refs | 11 | 0 | **−11** |
| `// --- section ---` markers | 4 | 4 | 0 |

JSON-level comparison (`clients[0].functions`, `typeDefs`): 42 typeDefs on both sides with identical
name sets; 11 typeDefs differ (the 11 qualified-ref fields, plus `ConnectionConfig` gaining
`annotations: [{name: "display", value: "{label: \"Connection Config\"}"}]`); 13 client functions on
both sides, 4 of which differ only by removal of the `Additional Values` parameter entry.
`readme`, `functions`, `services`, `annotations` (top level), `description`, `name` are byte-identical.

**Modified — qualified type refs normalised (11 occurrences, 9 record types):**

| Type | Field | old | new |
|---|---|---|---|
| `AssociationSpec` | `associationTypeId` | `ballerina/lang.int:0.0.0:Signed32` | `int:Signed32` |
| `ValueWithTimestamp` | `updatedByUserId` | same | `int:Signed32` |
| `BatchResponseSimplePublicObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `BatchResponseSimplePublicUpsertObjectWithErrors` | `numErrors` | same | `int:Signed32` |
| `CollectionResponseWithTotalSimplePublicObjectForwardPaging` | `total` | same | `int:Signed32` |
| `PublicObjectSearchRequest` | `'limit` | same | `int:Signed32` |
| `GetCrmV3ObjectsDealsGetPageQueries` | `'limit` | same | `int:Signed32` |
| `SimplePublicObject` | `propertiesWithHistory` | `record {\|ballerinax/hubspot.crm.obj.deals:1.0.2:ValueWithTimestamp[]...;\|}` | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicUpsertObject` | `propertiesWithHistory` | same | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `propertiesWithHistory` | same | `record {\|ValueWithTimestamp[]...;\|}` |
| `SimplePublicObjectWithAssociations` | `associations` | `record {\|ballerinax/…:1.0.2:CollectionResponseAssociatedId...;\|}` | `record {\|CollectionResponseAssociatedId...;\|}` |

**Modified — synthetic `anydata Additional Values` param dropped (4 client methods):**
`post batch/read`, `get [string dealId]`, `patch [string dealId]`, `get .` (new render lines
751, 755, 763, 783).

**Added (1):** `@display {label: "Connection Config"}` above `type ConnectionConfig` (new line 537).

**Removed:** none.

## 3. Correctness against library source

Upstream `v1.0.2` clone was diffed against the bala module sources: `client.bal`, `types.bal`,
`utils.bal` are all **identical**, so GitHub and the bala agree and either can be cited.

- **`@display` is real.** `types.bal:230` — `@display {label: "Connection Config"}` immediately
  precedes `public type ConnectionConfig record {|` at `types.bal:231`. `new` reproduces the label
  verbatim. `old` dropped it. ✔ correct addition.
- **`int:Signed32` is the real type.** `types.bal:508` — `int:Signed32 'limit = 10;`;
  `types.bal:47-49` (`AssociationSpec.associationTypeId`) likewise uses `int:Signed32`. The
  `ballerina/lang.int:0.0.0:Signed32` spelling in `old` is a renderer artefact, not source text
  (`grep -c 'lang.int' types.bal` → 0). ✔ `new` matches source.
- **`ValueWithTimestamp` / `CollectionResponseAssociatedId` map value types.** Source
  `types.bal` declares `record {|ValueWithTimestamp[]...;|} propertiesWithHistory?;` unqualified.
  ✔ `new` matches source; `old` did not.
- **`Additional Values` is not a real parameter.** `client.bal:47`, `:67`, `:100`, `:187` declare
  exactly `*PostCrmV3ObjectsDealsBatchReadReadQueries queries` /
  `*GetCrmV3ObjectsDealsDealIdGetByIdQueries queries` /
  `*PatchCrmV3ObjectsDealsDealIdUpdateQueries queries` / `*GetCrmV3ObjectsDealsGetPageQueries queries`
  as the trailing included-record parameter. There is no `Additional Values` parameter anywhere in
  the package. It was the renderer's stand-in for the open-record rest descriptor of the included
  record, and it rendered as syntactically invalid Ballerina. ✔ removing it is correct.
- **Method set matches.** All 12 resource methods in `client.bal` (lines 47, 67, 84, 100, 118, 135,
  152, 169, 187, 203, 220, 237) plus `init` (line 31) appear in `new` with matching accessor, path,
  payload type and return union. `init`'s default `serviceUrl = "https://api.hubapi.com/crm/v3/objects/deals"`
  matches `client.bal:31`.
- **Type name set matches exactly.** `diff` of the 42 `^public type <Name>` names from
  `types.bal` against the 42 `^type <Name>` names in `new` → IDENTICAL.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff -u old new` reviewed line by line (15 hunks; every hunk is one of the three improvement
  categories in §1 — no other change exists in the file).
- Declaration-name sets extracted from both renders and diffed: only the added `@display` line differs.
- JSON models diffed structurally: identical `typeDefs` name set (42/42), identical client function
  count (13/13), identical `readme` string, identical `description`/`name`, empty
  `functions`/`services`/`annotations` on both sides.
- Per-typeDef field-level diff: the only field changes are the 11 type-name normalisations and the
  `annotations` gain on `ConnectionConfig`. No field was dropped, renamed, retyped, or lost its doc.
- Per-function parameter-name diff: the only parameter removed anywhere is `Additional Values`,
  which does not exist in the library. No real parameter, default, or return type was dropped.
- `// Unknown type:` count is 0 on both sides (this library had no degraded types to begin with).

## 5. Issues in `new` (independent of `old`)

All five below are **identical in `old`** — they are pre-existing renderer limitations, listed here
because §5 asks for accuracy problems in `new` regardless of `old`. None is caused by spec v2.

1. **All record-field default values are dropped.** Source has 16 fields with defaults
   (`awk` over `types.bal`); the renders show every one of them as an optional field with no default.
   Examples: `ConnectionConfig.httpVersion = http:HTTP_2_0` → `http:HttpVersion httpVersion?`;
   `ConnectionConfig.timeout = 30` → `decimal timeout?`;
   `OAuth2RefreshTokenGrantConfig.refreshUrl = "https://api.hubapi.com/oauth/v1/token"` (a genuinely
   useful, HubSpot-specific value) → `string refreshUrl?`;
   `GetCrmV3ObjectsDealsGetPageQueries.'limit = 10` → `int:Signed32 'limit?`.
2. **Closed records are rendered as open.** `OAuth2RefreshTokenGrantConfig`, `ConnectionConfig` and
   `ApiKeysConfig` are `record {| … |}` in source (`types.bal:231`, `:484`, and the OAuth2 type);
   all 42 top-level type declarations in `new` render as open `record {`
   (`grep -cE '^type .* record \{\|'` → 0).
3. **Two fabricated parameter defaults on the client.** `resource function get .` renders
   `int:Signed32 limit = 0`, but the source default for `GetCrmV3ObjectsDealsGetPageQueries.'limit`
   is `10` (`types.bal:508`). Several methods render `string idProperty = ""`, but `idProperty` is
   declared optional with **no** default (`types.bal:53`, `:462`). An LLM copying these would send
   `limit=0`/`idProperty=""` on the wire.
4. **Included-record parameters are double-counted.** Four methods list the flattened query fields
   *and* the record itself, e.g.
   `resource function post batch/read(…, boolean archived = false, PostCrmV3ObjectsDealsBatchReadReadQueries queries)`.
   The source has only `*PostCrmV3ObjectsDealsBatchReadReadQueries queries`. The rendered signature
   does not compile and suggests a call shape that does not exist.
5. **`public` / `isolated` / `client` qualifiers are stripped.** Source is
   `public isolated client class Client` with `public isolated function init` and
   `resource isolated function …`; the render emits `client class Client`, `function init`,
   `resource function …` (`grep -cE '^(public|isolated)'` → 0 in both renders).

## 6. Coverage gaps vs. the library

**Zero gaps.**

- `package.json` `export` lists exactly one module: `hubspot.crm.obj.deals`. The bala
  `modules/` directory contains only `hubspot.crm.obj.deals`, which *is* the default module —
  so the known `getDefaultModule()`-only limitation costs this library nothing.
- Public symbols in that module: 42 `public type` in `types.bal` + 1 `public isolated client class Client`
  in `client.bal:23`. `utils.bal` exports nothing public (`grep -E '^public' utils.bal` → no match).
  No public functions, constants, enums, annotations, listeners or services exist.
- All 42 type names and the `Client` class are present in both renders.
- No submodule-only API to report.

## 7. Compiler plugin

The library ships **no compiler plugin**. `find` over the `v1.0.2` clone for
`*compiler-plugin*`/`CompilerPlugin*` returns nothing, and the bala root
(`bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`) has no
`compiler-plugin/` directory or `compiler-plugin.json`. Nothing plugin-derived is therefore expected
in — or missing from — the render.

## 8. Other considerations

- **Stable release.** `1.0.2`, not deprecated, `graalvmCompatible: true`, built with Ballerina
  `2201.12.2` (`Ballerina.toml` declares `distribution = "2201.12.0"`). No pre-1.0 caveats.
- **Size / tokens.** Effectively unchanged: 795 → 796 lines; JSON 87,434 → 86,328 bytes (−1.3%,
  from dropping the qualified prefixes and the 4 synthetic params). No token-budget impact.
- **Doc quality is good.** Every one of the 42 types and all 12 resource methods carry doc comments
  in the render, sourced from the published `.bal` files. The README block (7,984 chars) survives
  intact on both sides, including the setup guide and image links.
- **Cosmetic renderer noise (both sides):** resource-method docs end with a stray `# ` line; the
  `// Special Agent Note: <Type> FROM ballerina/http package` inline comments in `ConnectionConfig`
  and `OAuth2RefreshTokenGrantConfig` are renderer annotations, not source text.
- **Net effect for an LLM consumer:** `new` is strictly safer — it removes 11 non-compiling type
  spellings and 4 non-compiling parameter tokens, and adds one real annotation.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 795 / 796 |
| `diff -u old new` | 15 hunks, +16 / −15 lines; all reviewed |
| `wc -c old/*.json new/*.json` | 87,434 / 86,328 |
| `grep -c '^// Unknown type:'` old / new | 0 / 0 |
| `grep -n '^// --- ' new` | 4 markers: README(7), END README(197), Types(199), Client(744) |
| `grep -cE '^type ' old / new` | 42 / 42 |
| `diff <(grep -E '^(type\|class\|enum\|const\|annotation\|public\|@)' old) <(… new)` | one line: `> @display {label: "Connection Config"}` |
| `grep -cE '^@display' old / new` | 0 / 1 |
| Python: top-level JSON keys old vs new | identical set; `typeDefs` 42/42, `clients` 1/1, `functions` 0/0, `services` 0/0, `annotations` 0/0 |
| Python: `readme` equality | True, 7,984 chars both |
| Python: typeDef name sets | equal; 11 typeDefs differ in content (listed §2) |
| Python: `ConnectionConfig` field diff | `annotations`: `None` → `[{name: display, value: {label: "Connection Config"}}]` |
| Python: client function param-name diff | only `Additional Values` removed, on 4 methods |
| `git ls-remote --tags <repo>` | tags `v0.1.0`, `v1.0.1`, `v1.0.2` → exact tag `v1.0.2` exists |
| `git clone --depth 1 --branch v1.0.2` | succeeded |
| `diff src/ballerina/{client,types,utils}.bal bala/modules/…/` | all three **identical** |
| `wc -l` bala module | client.bal 249, types.bal 513, utils.bal 219 |
| `grep -cE '^public type ' bala/types.bal` | 42 |
| `diff` bala public type names vs `new` type names | IDENTICAL |
| `grep -E '^public ' bala/*.bal` (non-type) | one hit: `client.bal:23 public isolated client class Client` |
| `grep -n 'resource isolated function' bala/client.bal` | 12 methods at lines 47,67,84,100,118,135,152,169,187,203,220,237; `init` at 31 |
| `grep -n '@display' bala/types.bal` | `types.bal:230` — `@display {label: "Connection Config"}` |
| `grep -cE '^public type .* record \{\|' bala/types.bal` | 3 (`OAuth2RefreshTokenGrantConfig`, `ConnectionConfig`, `ApiKeysConfig`) |
| `grep -cE '^type .* record \{\|' new` | 0 (all 42 rendered open) |
| `awk` fields-with-defaults over bala/types.bal | 16 fields; 0 preserved in either render |
| `types.bal:508` | `int:Signed32 'limit = 10;` vs render `int:Signed32 limit = 0` |
| `types.bal:53` / `:462` | `string idProperty?;` (no default) vs render `string idProperty = ""` |
| `find <clone> -iname '*compiler-plugin*'` | no matches |
| `ls bala/1.0.2/any/` | `bala.json dependency-graph.json docs modules package.json` — no compiler-plugin |
| `cat bala/package.json` | version 1.0.2, `export: ["hubspot.crm.obj.deals"]`, graalvmCompatible true |
| `ls bala/modules/` | single module `hubspot.crm.obj.deals` (= default module) |
| Precomputed `OLD_AND_NEW_DIFFS/hubspot.crm.obj.deals_diff.md` | claims 795/796 lines, +16/−15, 15 hunks, 11→0 qualified refs, 0 decls added/removed — **all verified correct** |

## 10. Caveats and unverified items

- The renders were not compiled or fed to a Ballerina parser; syntax-validity statements
  (e.g. "`anydata Additional Values` is invalid Ballerina", "the double-counted parameter list does
  not compile") are based on reading the Ballerina grammar rules for identifiers and included-record
  parameters, not on a parser run.
- The claim that `old`'s qualified refs and `Additional Values` originate in the Java extractor
  rather than the TypeScript renderer was not traced through the `ballerina-vscode` sources; it is
  inferred from the fact that the JSON models themselves already differ in those exact places.
- The `# ` trailing-blank doc lines and `// Special Agent Note:` comments were classified as
  cosmetic renderer output without inspecting the renderer implementation.
- Everything else in this report is backed by a command in §9.

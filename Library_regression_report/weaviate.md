# ballerinax/weaviate 1.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/weaviate` |
| Pinned version | `1.0.2` |
| Upstream repo | https://github.com/ballerina-platform/openapi-connectors/tree/main/openapi/weaviate |
| Tag reviewed | default branch `master` @ `81158a45a86fa9a85de4e7fbd7cdc2a529d50743` (2026-06-16) — no module-scoped tag exists in this monorepo; the checked-out `openapi/weaviate` sources are **byte-identical** to the 1.0.2 bala and `Ballerina.toml` declares `version = "1.0.2"` |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/weaviate/1.0.2` |
| Old render | `662` lines (26,888 bytes) |
| New render | `669` lines (27,159 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. All five `// Unknown type:` placeholders in
`old` (`C11yVector`, `ObjectsGetResponseArr`, `GraphQLQueries`, `MultipleRef`, `GraphQLResponses`)
are replaced by real, correct type-alias definitions with their doc comments; the single
version-qualified type reference (`ballerinax/weaviate:1.0.2:JsonObject`) is now unqualified and
matches the source exactly; the keyword field `class` is now correctly quoted as `'class`; and three
`@display` annotations that exist in the published source are now surfaced. Nothing was dropped,
truncated, or made less accurate. Declaration coverage is identical on both sides (42 types, 1
client class, `init` + 17 resource functions) and matches the bala's default module exactly — zero
coverage gaps. Six inaccuracies remain in `new`, but every one of them is also present in `old`, so
none is a regression.

## 2. Change inventory

Line counts: old 662, new 669 (+7 net). 14 lines added, 7 removed, 8 hunks.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 5 | 0 |
| Version/module-qualified type refs (`org/mod:ver:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |
| `type X ...` declarations | 42 (37 defs + 5 placeholders) | 42 |
| `client class` | 1 | 1 |
| `function init` | 1 | 1 |
| `resource function` | 17 | 17 |
| Non-ASCII bytes | 0 | 0 |

**Declarations added: 0. Declarations removed: 0.** The type-name set is identical on both sides
(`comm` on the extracted name lists returned empty in both directions).

**Declarations modified: 10**, all in `new`'s favour:

| # | Kind | Symbol | old → new |
|---|---|---|---|
| 1 | type alias | `C11yVector` | `// Unknown type: C11yVector` → `# A Vector in the Contextionary` + `type C11yVector float[];` |
| 2 | type alias | `ObjectsGetResponseArr` | `// Unknown type: …` → `type ObjectsGetResponseArr ObjectsGetResponse[];` |
| 3 | type alias | `GraphQLQueries` | `// Unknown type: …` → doc + `type GraphQLQueries GraphQLQuery[];` |
| 4 | type alias | `MultipleRef` | `// Unknown type: …` → doc + `type MultipleRef SingleRef[];` |
| 5 | type alias | `GraphQLResponses` | `// Unknown type: …` → doc + `type GraphQLResponses GraphQLResponse[];` |
| 6 | record field | `ObjectsGetResponse.class` | `string class?;` → `string 'class?;` |
| 7 | record field | `GraphQLResponse.data` | `record {\|ballerinax/weaviate:1.0.2:JsonObject...;\|}` → `record {\|JsonObject...;\|}` |
| 8 | annotation | `ConnectionConfig` | *(absent)* → `@display {label: "Connection Config"}` |
| 9 | annotation | `ProxyConfig.password` | *(absent)* → `@display {label: "", kind: "password"}` |
| 10 | annotation | `Client` | *(absent)* → `@display {label: "Weaviate", iconPath: "icon.png"}` |

JSON-level confirmation (independent of the renderer): in `new/ballerinax_weaviate.json` the five
`"type": "Other"` typeDefs gained a `"baseType"` key; `ProxyConfig.password` and `ConnectionConfig`
gained `"annotations"`; the client object gained `"annotations"`; `ObjectsGetResponse` field `class`
became `'class`. `readme`, `description`, `functions` (`[]`), `services` (`[]`), and top-level
`annotations` (`[]`) are byte-identical between the two JSONs.

## 3. Correctness against library source

Upstream `openapi/weaviate/{types.bal,client.bal,utils.bal}` on the default branch `diff`s clean
against the bala's `modules/weaviate/*.bal` (three empty diffs), so GitHub and the bala agree and
either can be cited.

Every added/changed item in `new` verified against `.../modules/weaviate/types.bal` (449 lines) and
`client.bal` (285 lines):

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `# A Vector in the Contextionary` / `type C11yVector float[];` | `types.bal:295-296` | exact |
| `type ObjectsGetResponseArr ObjectsGetResponse[];` (no doc) | `types.bal:77` (no doc comment in source) | exact |
| `# A list of GraphQL queries.` / `type GraphQLQueries GraphQLQuery[];` | `types.bal:113-114` | exact |
| `# Multiple instances of references to other objects.` / `type MultipleRef SingleRef[];` | `types.bal:318-319` | exact |
| `# A list of GraphQL responses.` / `type GraphQLResponses GraphQLResponse[];` | `types.bal:337-338` | exact |
| `string 'class?;` in `ObjectsGetResponse` | via `*Object` inclusion, `types.bal:419-421` | exact (and now valid Ballerina) |
| `record {\|JsonObject...;\|} data?;` | `types.bal:303-306` | exact |
| `@display {label: "Connection Config"}` | `types.bal:20` | exact |
| `@display {label: "", kind: "password"}` on `password` | `types.bal:73` | exact |
| `@display {label: "Weaviate", iconPath: "icon.png"}` on `Client` | `client.bal:21` | exact |

Exhaustive structural check (small library, so done in full rather than spot-checked):

- **Types.** Parsed all 42 `public type` declarations from `types.bal` and compared against the 42
  typeDefs in `new/ballerinax_weaviate.json`. Set difference empty in both directions.
- **Record fields.** Parsed all 37 record types → 141 fields in the bala. `new` renders 149 fields;
  the 8 extras are exactly the `*Object` inclusion fields flattened into `ObjectsGetResponse`
  (`types.bal:134-135`), which is correct expansion. Zero fields missing.
- **Field types.** Automated comparison of all 141 field type strings: 0 genuine mismatches. The 18
  raw hits were 13 `http:`-prefixed refs (JSON stores the bare name plus an external link; the
  renderer re-adds `http:` — verified in the render text) and 5 `record {}` → `record {|anydata...;|}`
  renderings, which is the identical type by definition.
- **Client.** `client.bal` declares `init` (line 31) + 17 `resource isolated function`s (lines 69,
  81, 99, 112, 128, 143, 160, 171, 184, 199, 212, 224, 233, 245, 254, 266, 277). `new` renders
  `init` + 17 resource functions with matching accessors, paths, parameters, defaults, and return
  types (e.g. `resource function get objects(string|() after = (), int offset = 0, int|() 'limit = (),
  … string|() 'class = ()) returns ObjectsListResponse|error;` vs `client.bal:69` — identical modulo
  the `isolated` qualifier and `?`→`|()` nil-union spelling).
- **README.** The render's `// --- README ---` block (lines 8-112) equals `docs/Package.md` +
  `## Module: weaviate` + `docs/modules/weaviate/Module.md`, identical in `old` and `new`.

## 4. Regressions

**None found.**

What was checked to conclude this:

1. `diff -u old new` in full (8 hunks, all listed in §2) — every hunk is an addition or a
   correction; the only removed lines are the 5 `// Unknown type:` placeholders, the unquoted
   `string class?;`, and the version-qualified `data` field, each replaced by a strictly more
   accurate line.
2. Extracted type-name sets from both renders and `comm`'d them: `old`-only = ∅, `new`-only = ∅
   (the 5 "added" types existed in `old` only as comment placeholders, so the *declaration* count is
   unchanged while the *information* content rose).
3. Per-type JSON deep comparison of all 42 typeDefs: the only differing types are the 8 listed in
   §2, and every difference is an addition (`baseType`, `annotations`) or a correction (`'class`,
   unqualified `JsonObject`). No field, doc string, optionality flag, or link was dropped.
4. Client JSON deep comparison: the only diff is the added client-level `annotations` array. All 18
   function entries (init + 17 resources) are byte-identical between `old` and `new`.
5. `readme`, `description`, `functions`, `services`, top-level `annotations` compared for equality —
   all equal.
6. Section markers: 4 in both. Non-ASCII: 0 in both. No malformed syntax introduced by `new` (the
   one malformed construct, `AdditionalProperties`, is identical in `old` — see §5).

## 5. Issues in `new` (independent of `old`)

All six are also present in `old`; none is caused by spec v2. Listed because they still mislead a
consuming LLM.

1. **`AdditionalProperties` is malformed and non-compiling.** `new:210-213` renders
   ```
   type AdditionalProperties record {
       # Rest field
       record {|anydata...;|} ;
   };
   ```
   A field with a type and no name. The source (`types.bal:226-228`) is
   `public type AdditionalProperties record {| record {}...; |};` — a closed record whose *rest type*
   is `record {}`, not `anydata`. Both the syntax and the rest type are wrong. Identical text at
   `old:210-213`.
2. **All 11 field default values are dropped, and required-with-default fields are shown as
   optional.** `ConnectionConfig.httpVersion = http:HTTP_2_0`, `timeout = 60`,
   `forwarded = "disable"`, `compression = http:COMPRESSION_AUTO`, `validation = true`
   (`types.bal:24,30,32,38,50`); `ClientHttp1Settings.keepAlive`, `chunking` (`types.bal:57,59`);
   `ProxyConfig.host/port/userName/password = ""|0` (`types.bal:67,69,71,74`). All 11 render as
   `field?;` with no default. Verified programmatically: 11 bala fields carry defaults, 11 render as
   optional-without-default, in both renders.
3. **Closed records are rendered as open.** `ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`,
   `AdditionalProperties` are `record {| … |}` in source (`types.bal:21,55,65,226`) but render as
   `record { … }`, which wrongly implies arbitrary extra fields are accepted.
4. **`isolated` and `public` qualifiers dropped.** Source has `public isolated client class Client`
   (`client.bal:22`), `public isolated function init` (`client.bal:31`), and
   `resource isolated function …` throughout; the render emits `client class Client`,
   `function init`, `resource function`.
5. **Doc comments lost on the 8 flattened `*Object` fields.** `ObjectsGetResponse` inlines `Object`'s
   fields (`types.bal:134-135`) but drops their `#` docs — e.g. `'class` renders bare in
   `ObjectsGetResponse` (`new:223`) while carrying `# Class of the Object, defined in the schema.` in
   `Object` (`new:181`, source `types.bal:420`). The type-inclusion relationship itself is also not
   represented.
6. **17 method-level `@display` labels are not captured**, even though `new` now captures client-level
   and record-field-level annotations. `client.bal:68,80,98,111,127,142,159,170,183,198,211,223,232,
   244,253,265,276` each carry `@display {label: "…"}` (e.g. `"List Objects"`, `"Insert Object"`,
   `"Batch Query"`). The `functions[].annotations` array is empty in both JSONs — an inconsistency
   within `new`'s own annotation support, not a regression.

## 6. Coverage gaps vs. the library

**Zero.** The bala has exactly one module (`any/modules/weaviate`) — it *is* the default module — so
there is no submodule-only API and therefore no shared `getDefaultModule()` gap for this library.

- 42 of 42 `public type` declarations in `types.bal` appear in both renders.
- 141 of 141 record fields appear in `new` (plus the 8 correctly flattened inclusion fields).
- `Client` + `init` + all 17 resource functions appear in both renders.
- `utils.bal` contains 6 functions (`getDeepObjectStyleRequest`, `getFormStyleRequest`,
  `getSerializedArray`, `getSerializedRecordArray`, `getEncodedUri`, `getPathForQueryParam`), all
  module-private (`isolated function`, no `public`), correctly absent from both renders.
- The only public member not rendered is the `Client` class's `final http:Client clientEp` field
  (`client.bal:23`), which is an implementation detail and correctly omitted.

## 7. Compiler plugin

None. `find` over the bala returns no `compiler-plugin` directory or `compiler-plugin.json`, and the
upstream `openapi/weaviate` directory contains only `Ballerina.toml`, `Module.md`, `Package.md`,
`client.bal`, `types.bal`, `utils.bal`, `openapi.yaml`, `icon.png`. This is a pure OpenAPI-generated
connector with no code actions, validations, or generated artifacts. Nothing plugin-implied is
missing from the render.

## 8. Other considerations

- **Not deprecated.** Central metadata: `"isDeprecated": false`, `"deprecateMessage": ""`.
- **Stale.** Built against `ballerinaVersion 2201.4.1`, spec `2022R4`, published 2023-05-11
  (`createdDate 1683805063000`), targeting Weaviate API 1.18.0 per `Package.md`. 5,676 pulls.
  `graalvmCompatible: "Yes"`. This staleness affects both sides equally.
- **Monorepo, no per-module tags.** `git ls-remote --tags` on `openapi-connectors` returns only
  repo-wide `vN.N.N` tags (latest `v2.5.5`) and zero tags matching `weaviate`. Version identity was
  instead established by byte-diffing the checked-out sources against the 1.0.2 bala — clean — and
  by `Ballerina.toml:9` declaring `version = "1.0.2"`.
- **Size.** 669 lines / 27,159 bytes. Trivial token cost; the +271 bytes spec v2 adds buy 5 real type
  definitions and 3 annotations.
- **Render is still not directly compilable** (both sides) because of the `AdditionalProperties`
  construct in §5.1 and the dropped `public`/`isolated` qualifiers, but that is the render format's
  convention, not a defect introduced here.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 662 / 669 |
| `wc -c old/*.bal.txt new/*.bal.txt` | 26,888 / 27,159 |
| `diff -u old/ballerinax_weaviate.bal.txt new/ballerinax_weaviate.bal.txt` | 8 hunks, +14 / −7 (all reproduced in §2) |
| `grep -c '^// Unknown type:'` old / new | 5 / 0 |
| `grep -cE ':1\.0\.2:' ` new | 0 (old had 1, at `GraphQLResponse.data`) |
| `grep -c '^// --- '` old / new | 4 / 4 |
| `grep -cP '[^\x00-\x7F]'` old / new | 0 / 0 |
| `grep -c '    resource function'` old / new | 17 / 17 |
| `comm -23/-13` on extracted type-name sets (old, new, bala) | all three sets empty ⇒ 42 = 42 = 42, identical members |
| `git ls-remote --tags …/openapi-connectors \| grep -i weaviate` | exit 1, no match; repo tags are `v2.x.y` only |
| `git clone --depth 1 --filter=blob:none --sparse … && git sparse-checkout set openapi/weaviate` | HEAD `81158a45a86fa9a85de4e7fbd7cdc2a529d50743`, 2026-06-16 |
| `diff src/openapi/weaviate/{types,client,utils}.bal bala/modules/weaviate/…` | all three empty ⇒ upstream ≡ bala |
| `grep -n 'version' src/openapi/weaviate/Ballerina.toml` | line 9: `version = "1.0.2"` |
| `grep -nE '^public (type\|class\|const\|enum\|function)' bala types.bal` | 42 public types |
| `grep -nE 'resource isolated function\|function init' bala client.bal` | init@31 + 17 resource functions |
| `grep -nE '^(public\|isolated)' bala utils.bal` | 6 functions, none public |
| `find bala -iname '*compiler*'` | no results |
| `ls bala/any/modules` | `weaviate` only (single/default module) |
| Python: parse 37 bala record types → 141 fields; compare to `new` JSON | 0 fields missing; 8 extras = `*Object` flattening; 149 total render fields = 141 + 8 |
| Python: compare all 141 field type strings bala vs `new` JSON | 0 genuine mismatches (13 `http:`-prefix artifacts, 5 `record {}` ≡ `record {\|anydata...;\|}`) |
| Python: count bala fields with defaults vs rendered optionality | 11 with defaults; 11 rendered `?` with no default (same in `old`) |
| Python: deep-diff `old` vs `new` JSON typeDefs | 8 types differ, all additions/corrections; 0 removals |
| Python: deep-diff `old` vs `new` JSON clients | single diff: client `annotations` added |
| Python: equality of `readme` / `description` / `functions` / `services` / top-level `annotations` | all equal; readme 4,817 chars |
| `diff` render README block (lines 8-112) vs `docs/…/Module.md` | differs only by the prepended `Package.md` + `## Module: weaviate` header, as designed; identical in both renders |
| `grep -n '@display' bala/*.bal` | 3 rendered (types.bal:20, types.bal:73, client.bal:21) + 17 method-level not rendered |
| `curl api.central.ballerina.io/…/ballerinax/weaviate/1.0.2` | `isDeprecated:false`, 1 module, `ballerinaVersion 2201.4.1`, `graalvmCompatible:Yes`, pulls 5,676 |
| `diff` of `/tmp/w_old.txt` vs `/tmp/w_new.txt` (type-name lists) | empty |

## 10. Caveats and unverified items

1. **No exact-version tag.** `openapi-connectors` publishes only repo-wide `vN.N.N` tags; there is no
   `weaviate-v1.0.2`. The default-branch checkout was used instead. Risk is nil here because the
   checked-out `.bal` files diff clean against the 1.0.2 bala and `Ballerina.toml` pins `1.0.2` — but
   it is a clone of the default branch, not a tag, as the brief requires me to state.
2. **Renderer semantics not independently re-derived.** I did not re-run the two-stage pipeline; I
   audited the supplied `.json` and `.bal.txt` artifacts. The claim that `new`'s changes are caused
   by spec v2 rather than by any other input difference rests on the brief's statement that both
   sides used the same bala at the same pinned version, corroborated by the two JSONs being identical
   except for the 9 documented deltas.
3. **`record {}` vs `record {|anydata...;|}` treated as equivalent** by the Ballerina type system;
   asserted from the language spec, not from a compiler run in this environment.
4. **The 17 method-level `@display` labels** are confirmed absent from both JSONs' `functions[]`
   entries. Whether spec v2 *intends* to capture function-level annotations is unverified — I did not
   read the extractor source, so §5.6 is reported as an observed gap, not as a bug against a spec.

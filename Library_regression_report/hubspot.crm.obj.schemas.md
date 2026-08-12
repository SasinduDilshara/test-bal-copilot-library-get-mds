# ballerinax/hubspot.crm.obj.schemas 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.obj.schemas` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.obj.schemas |
| Tag reviewed | `v2.0.2` (commit `f810994232a07935c46a1084cf75e6733c286cd6`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.obj.schemas/2.0.2/any` |
| Old render | `567` lines |
| New render | `568` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small single-module OpenAPI-generated connector: 18 public types, 1 client class, 7 resource methods
plus `init`. Both renders carry the identical declaration set (18 types, 1 client, 0 module functions,
0 services, 0 annotation declarations — verified from both JSONs). The only differences are three
spec-v2 fixes, all strictly correct:

1. 7 occurrences of the bogus `ballerina/lang.int:0.0.0:Signed32` type reference replaced with the
   real `int:Signed32` (matches source exactly, 7 for 7).
2. `@display {label: "Connection Config"}` on `ConnectionConfig` is now emitted (it exists at
   `types.bal:306` and was silently dropped by `old`).
3. Two client resource signatures no longer contain the malformed pseudo-parameter
   `anydata Additional Values`, which was non-compiling Ballerina and referred to nothing in the source.

No declaration, parameter, default, return type or doc line was lost. No regression found.

## 2. Change inventory

Line counts: old 567, new 568 (`wc -l`). Unified diff: 9 hunks, +10 / −9 lines.

Declaration-set comparison (both JSON and render):

| Kind | old | new | delta |
|---|---|---|---|
| `typeDefs` (JSON) | 18 | 18 | 0 |
| `clients` (JSON) | 1 | 1 | 0 |
| `functions` (JSON) | 0 | 0 | 0 |
| `services` (JSON) | 0 | 0 | 0 |
| `annotations` (JSON, module-level decls) | 0 | 0 | 0 |
| `^type ` in render | 18 | 18 | 0 |
| `enum` / `const` / `listener` | 0 | 0 | 0 |
| client resource/init methods in render | 8 | 8 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs | 7 | 0 | −7 |

Type-name sets are set-identical between old render, new render and the bala's public types
(`comm` produced empty "only in src" and "only in render" lists).

`readme`, `name`, `description` fields of the two JSONs are byte-identical.

### Modified declarations (6 types + 1 client, all field/param-level only)

| Declaration | Change |
|---|---|
| `ObjectTypeDefinition` | `createdByUserId`, `updatedByUserId`: `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32` |
| `Property` | `displayOrder`: same fix |
| `Option` | `displayOrder`: same fix |
| `ObjectSchema` | `portalId`: same fix |
| `OptionInput` | `displayOrder`: same fix |
| `ObjectTypePropertyCreate` | `displayOrder`: same fix |
| `ConnectionConfig` | `@display {label: "Connection Config"}` added |
| `Client.get` (root) | dropped `anydata Additional Values` param |
| `Client.delete [string objectType]` | dropped `anydata Additional Values` param |

Nothing added or removed at declaration level (the precomputed diff's "Declarations added (0) /
removed (0)" is confirmed by the independent `comm` check above).

## 3. Correctness against library source

The bala module sources are **byte-identical** to the upstream `v2.0.2` tag (`diff` on `types.bal`,
`client.bal`, `utils.bal` — all reported identical), so GitHub and the bala agree.

- All 7 `int:Signed32` fields in the source (`types.bal:60, 82, 110, 173, 176, 220, 254`) map 1:1 to
  the 7 fixed lines in `new`. Field names and optionality match:
  `portalId?` (60), `displayOrder` (82, required — render also emits it required), `displayOrder?`
  (110), `createdByUserId?` (173), `updatedByUserId?` (176), `displayOrder?` (220), `displayOrder?` (254).
- `@display {label: "Connection Config"}` — `types.bal:306`, immediately above
  `public type ConnectionConfig record {|` at `types.bal:307`. `new` places it correctly between the
  doc comment and the type. This is the only `@display` in the module, and the only annotation
  attachment in `types.bal` or `client.bal` (grep). Nothing else is missing.
- `anydata Additional Values` in `old`: the two query records
  (`GetCrmObjectSchemasV3SchemasGetAllQueries`, `types.bal:92-95`;
  `DeleteCrmObjectSchemasV3SchemasObjectTypeArchiveQueries`, `types.bal:72-75`) are open records
  (`record { ... }`) whose implicit `anydata` rest field `old` rendered as a parameter literally named
  `Additional Values`. No such parameter exists in the source; removing it is a correctness fix.
- Client methods, checked against `client.bal:32, 48, 64, 82, 98, 115, 134, 153` — all 8 present in
  `new` with matching paths, parameter names/order/defaults and return types.
- `utils.bal` exports no public symbols (`grep '^public'` returned nothing), consistent with
  `functions: 0` in both JSONs.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full unified `diff -u` of the two renders read line by line (9 hunks, all listed in §2). Every
  removed line has a corresponding, strictly more accurate added line except hunk 7, which is a pure
  addition.
- Type-name sets: `comm -23` / `comm -13` between the bala's 18 public types and the `new` render's
  18 rendered types — both empty.
- JSON element counts and name-sets per key (`typeDefs`, `clients`, `functions`, `services`,
  `annotations`) — identical between sides.
- `readme` JSON field and the rendered README block (lines 7–178 on both sides) — identical, no
  content lost.
- No parameter, default value, optional marker or doc comment appears only in `old`.

## 5. Issues in `new` (independent of `old`)

Three inaccuracies exist in `new`, all of which are also present in `old` (shared renderer behaviour,
not introduced by spec v2), listed because they would mislead an LLM consuming the render:

1. **Included-record parameters are double-rendered.** Source:
   `resource isolated function get .(map<string|string[]> headers = {}, *GetCrmObjectSchemasV3SchemasGetAllQueries queries)`
   (`client.bal:48`). Render emits both the flattened field (`boolean archived = false`) *and* a
   positional `GetCrmObjectSchemasV3SchemasGetAllQueries queries` parameter, and drops the `*`
   included-record marker. The rendered signature is not callable as written. Same for the `delete`
   at `client.bal:98`.
2. **`isolated` qualifier and the `.` resource path are dropped** on all client methods
   (`resource isolated function get .` → `resource function get (`). Cosmetic for an LLM, but the
   root-path form is lost.
3. **Closed records are rendered as open.** `OAuth2RefreshTokenGrantConfig` (`types.bal:201`),
   `ApiKeysConfig` (301) and `ConnectionConfig` (307) are `record {| ... |}` in source; both renders
   emit `record { ... }` (0 occurrences of `record {|` in either file).
4. **One doc comment wraps without a `#` prefix.** The `laxDataBinding` field doc in
   `ConnectionConfig` continues onto a bare line `and absent fields are handled as \`nilable\` types...`.
   Present once in each render — non-compiling if the block were pasted as Ballerina.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `export` lists exactly one module: `hubspot.crm.obj.schemas` (the default module).
  There are no submodules (`modules/` contains only `hubspot.crm.obj.schemas`), so the known
  `getDefaultModule()`-only limitation costs nothing here.
- All 18 public types and the single `Client` class with all 8 methods appear in both renders.
- `utils.bal` exports nothing public.

## 7. Compiler plugin

The bala contains **no** `compiler-plugin/` directory and no `compiler-plugin.json`; `find` over the
upstream `v2.0.2` clone found no `*compiler-plugin*` path. This is a plain generated connector with
no plugin-contributed code actions, validations or generated artifacts. Nothing plugin-related is
therefore expected in, or absent from, the render.

## 8. Other considerations

- Version 2.0.2 is stable (post-1.0), not deprecated in the package metadata. Built with Ballerina
  `2201.12.2`, `graalvmCompatible: true`.
- Size impact is negligible: +1 line (~0.2%), so no token-budget consequence.
- Doc quality is good — every type field carries the HubSpot API description; only the eight client
  methods have an empty trailing `# ` line after their one-line description (both sides).
- The `// Special Agent Note: ... FROM ballerina/http package` annotations on `ConnectionConfig`
  fields are identical on both sides and correctly attribute the 15 `http:` types.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 567 / 568 |
| `diff -u old new` | 9 hunks, +10/−9; read in full |
| `grep -c '^// Unknown type:'` both | 0 / 0 |
| `grep -c ':0\.0\.0:\|/lang\.'` both | 7 (old) / 0 (new) |
| `grep -n '^// --- '` both | 4 markers each; `Client` at 534 (old) / 535 (new) |
| `grep -cE '^type '` both | 18 / 18 |
| `grep -cE '^enum \|^const '` both | 0 / 0 |
| Python JSON key/count/name-set compare | typeDefs 18=18, clients 1=1, functions 0=0, services 0=0, annotations 0=0; no name-set differences; `readme`, `name`, `description` equal |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, v2.0.2 → exact match `v2.0.2` |
| `git clone --depth 1 --branch v2.0.2` | succeeded, commit `f810994` |
| `diff bala/types.bal upstream/ballerina/types.bal` | identical |
| `diff bala/client.bal upstream/ballerina/client.bal` | identical |
| `diff bala/utils.bal upstream/ballerina/utils.bal` | identical |
| `grep -oE '^public type ...' types.bal \| sort` | 18 names |
| `comm` src-types vs new-render types | both directions empty |
| `grep -n 'int:Signed32' types.bal` | lines 60, 82, 110, 173, 176, 220, 254 (7) |
| `grep -n '@display' types.bal` | line 306 only |
| `grep -n '@display\|annotation' client.bal` | no matches |
| `grep -n 'resource function\|public function' client.bal` | lines 32, 48, 64, 82, 98, 115, 134, 153 (8) |
| `types.bal:72-75`, `92-95` | both query records are open `record { boolean archived = false; }` |
| `grep -c 'record {|'` both renders | 0 / 0 |
| `grep -c '^and absent fields'` both renders | 1 / 1 |
| `grep '^public' utils.bal` | no matches |
| `ls bala/.../compiler-plugin` | does not exist |
| `find upstream -iname '*compiler-plugin*'` | no matches |
| `ls bala/any/modules` | single dir `hubspot.crm.obj.schemas` |
| `package.json` `export` | `["hubspot.crm.obj.schemas"]` |
| `sed -n '485,495p' new` / `'485,493p' old` | confirms `@display` placement is the sole addition in hunk 7 |
| `sed -n '534,568p' new` | full client section reviewed against `client.bal` |

## 10. Caveats and unverified items

- The Ballerina Central registry API was not re-queried; package metadata (version, exports,
  keywords, non-deprecation) was taken from the bala's `package.json`, which is authoritative for
  what the extractor consumed. Deprecation status on Central is therefore **unverified**.
- The renders were not compiled. Statements about non-compiling constructs (§5 items 1 and 4) are
  from reading the text against the Ballerina grammar, not from a compiler run.
- I did not re-run the two-stage pipeline; the analysis compares the supplied artifacts. The claim
  that the only causal difference is the extractor/renderer change rests on the brief plus the
  observed identity of `name`/`description`/`readme`/declaration sets across both JSONs.

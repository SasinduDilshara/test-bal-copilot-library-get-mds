# ballerinax/hubspot.crm.associations.schema 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.associations.schema` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.associations.schema |
| Tag reviewed | `v2.0.2` (commit `41f402a7bd09104d4ca46992112c3e9e300b0410`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.associations.schema/2.0.2/any` |
| Old render | `581` lines |
| New render | `582` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Small, single-module HTTP connector (533 lines of published `.bal`). The two renders are
declaration-for-declaration identical: same 22 record types, same `Client` class, same `init` plus
9 resource methods, same README block (byte-identical), same 4 section markers, 0
`// Unknown type:` placeholders on either side.

The entire delta is two spec-v2 behaviours, both strictly positive:

1. **13 version-qualified type refs fixed.** `ballerina/lang.int:0.0.0:Signed32` → `int:Signed32`
   (12 occurrences + 1 nullable `Signed32?`). The `old` spelling is not valid Ballerina and would
   not compile; the `new` spelling matches the library source exactly.
2. **1 annotation recovered.** `@display {label: "Connection Config"}` on `ConnectionConfig`, which
   is present in the published source but absent from `old`. It is the only annotation in the whole
   module, so annotation coverage in `new` is 1/1.

No declaration was added or removed. No regression found.

## 2. Change inventory

Line counts: old 581, new 582 (+1). Unified diff: 9 hunks, 14 lines added, 13 removed.

| Kind | old | new | Delta |
|---|---|---|---|
| `type` declarations | 22 | 22 | 0 |
| `client class` | 1 | 1 | 0 |
| `function init` | 1 | 1 | 0 |
| `resource function` | 9 | 9 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 13 | 0 | −13 |
| `// Special Agent Note:` cross-package hints | 17 | 17 | 0 |
| Annotations emitted | 0 | 1 | +1 |

Declarations added: **0**. Declarations removed: **0**. Declarations modified: **9 record types**
(field type spelling only) plus **1 record type** (annotation added).

Modified types and the fields touched:

| Type | Fields respelled to `int:Signed32` |
|---|---|
| `BatchResponsePublicAssociationDefinitionUserConfigurationWithErrors` | `numErrors` |
| `PublicAssociationDefinitionUserConfiguration` | `userEnforcedMaxToObjectIds` (`?`-nullable), `typeId` |
| `PublicAssociationSpec` | `typeId` |
| `PublicAssociationDefinitionConfigurationUpdateResult` | `userEnforcedMaxToObjectIds`, `typeId` |
| `PublicAssociationDefinitionConfigurationUpdateRequest` | `typeId`, `maxToObjectIds` |
| `PublicAssociationDefinitionConfigurationCreateRequest` | `typeId`, `maxToObjectIds` |
| `PublicAssociationDefinitionUpdateRequest` | `associationTypeId` |
| `AssociationSpecWithLabel` | `typeId` |
| `BatchResponsePublicAssociationDefinitionConfigurationUpdateResultWithErrors` | `numErrors` |
| `ConnectionConfig` | (annotation `@display` added; no field change) |

The JSON diff mirrors this exactly: 59 diff lines total — 13 `"name"` respellings plus a single
6-line `"annotations": [{"name":"display","value":"{label: \"Connection Config\"}"}]` insertion.
Nothing else changed in the JSON.

## 3. Correctness against library source

Upstream `v2.0.2` `ballerina/types.bal` and `ballerina/client.bal` are **byte-identical** to the
bala's `modules/hubspot.crm.associations.schema/{types,client}.bal` (`diff` exit 0 both files), so
GitHub and bala agree and either can be cited.

- **`int:Signed32` occurrences.** Source has 13 in `types.bal` (lines 27, 102, 104, 112, 116, 122,
  126, 134, 156, 172, 174, 221, 289) and 1 in `client.bal` line 178 (`[int:Signed32
  associationTypeId]` path param). Total 14. `new` render contains exactly 14 `int:Signed32`
  occurrences — a 1:1 match. `old` contained 13 wrong spellings plus the 1 in the client signature
  (which was never mangled because it comes from the resource path, not the type table).
- **`@display` annotation.** `types.bal:237` is `@display {label: "Connection Config"}`, sitting
  directly above `types.bal:238 public type ConnectionConfig record {|`. It is the only `@`
  annotation anywhere in the module (`grep '^\s*@'` over all three `.bal` files returns exactly that
  one line). `new` reproduces it verbatim; `old` omitted it.
- **All 22 public types.** `grep '^public type' types.bal` yields 22 names; `grep '^type ' ` on both
  renders yields the same 22 names. Set equality confirmed by inspection of both lists.
- **Client surface.** `client.bal:23 public isolated client class Client`. Its 9 `resource isolated
  function` signatures (lines 46, 63, 80, 100, 117, 137, 157, 178, 195) appear in both renders with
  identical parameter lists, defaults (`map<string|string[]> headers = {}`), and return unions —
  e.g. `post .../batch/create` returns
  `BatchResponsePublicAssociationDefinitionUserConfiguration|BatchResponsePublicAssociationDefinitionUserConfigurationWithErrors|error`
  in both source and render. `init` renders as
  `function init(ConnectionConfig config, string serviceUrl = "https://api.hubapi.com/crm/v4/associations") returns error?`,
  matching `client.bal`.

## 4. Regressions

**None found.**

Checked to conclude that: (a) full `diff -u old new` reviewed in its entirety — 9 hunks, all of them
either the `Signed32` respelling or the annotation insertion, no other content change; (b) declaration
counts equal on both sides for every kind (types 22/22, class 1/1, init 1/1, resource functions 9/9);
(c) README section (lines 7–236) is byte-identical between the two renders; (d) `Special Agent Note`
cross-package hints unchanged at 17 on both sides; (e) full JSON diff is 59 lines and contains only
the 13 type-name respellings and the annotation insertion — no dropped fields, docs, defaults, or
return types; (f) no line in `new` is malformed relative to `old`.

## 5. Issues in `new` (independent of `old`)

These are fidelity losses of the renderer that exist in `new`; all of them are equally present in
`old`, so none is a regression, but they misrepresent the library to a consuming LLM.

1. **Closed records rendered as open.** Source declares `ConnectionConfig` (`types.bal:238`),
   `OAuth2RefreshTokenGrantConfig` (`types.bal:198`) and `ApiKeysConfig` (`types.bal:211`) as
   `record {| ... |}`. All three render as `record { ... }`. An LLM would believe extra fields are
   permitted.
2. **Field default values dropped, and required-with-default fields shown as optional.** In
   `ConnectionConfig` the source has 1 required field (`auth`), 11 fields with defaults
   (`httpVersion = http:HTTP_2_0`, `http1Settings = {}`, `http2Settings = {}`, `timeout = 30`,
   `forwarded = "disable"`, `cache = {}`, `compression = http:COMPRESSION_AUTO`,
   `responseLimits = {}`, `socketConfig = {}`, `validation = true`, `laxDataBinding = true`) and 7
   genuinely optional fields. The render shows `auth` required and **18** fields with `?` and no
   default — the 11 defaults are silently lost. Same for
   `OAuth2RefreshTokenGrantConfig.refreshUrl`, whose source default
   `"https://api.hubapi.com/oauth/v1/token"` is dropped and the field marked `?`.
3. **Type inclusion flattened without marking.** `OAuth2RefreshTokenGrantConfig` includes
   `*http:OAuth2RefreshTokenGrantConfig` (`types.bal:199`). The render expands the inherited fields
   (`refreshToken`, `clientId`, `clientSecret`, `scopes`, `defaultTokenExpTime`, `clockSkew`,
   `optionalParams`, `credentialBearer`, `clientConfig`) but marks several inherited-required fields
   correctly while dropping the `*` inclusion notation. Expansion is arguably helpful; the loss of
   the source-of-truth marker is not.
4. **Malformed doc continuation — non-compiling if pasted.** `new` line 531 (old line 530) is
   `and absent fields are handled as \`nilable\` types. Enabled by default` at column 0 with **no**
   leading `#`. The preceding line 530 is the first half of the `laxDataBinding` doc comment. As
   written, the render is not valid Ballerina at that point.
5. **`public` / `isolated` modifiers dropped throughout.** Every `public type` renders as bare
   `type`; `public isolated client class Client` renders as `client class Client`; `resource
   isolated function` renders as `resource function`. Consistent renderer convention, not a
   per-library fault, but it does erase the isolation guarantees of the API.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

`package.json` declares `"export": ["hubspot.crm.associations.schema"]` — a single module, which is
the default module. The bala's `modules/` directory contains exactly one entry
(`hubspot.crm.associations.schema`, with `client.bal`, `types.bal`, `utils.bal`), so the
`getDefaultModule()`-only extraction limitation described in the brief costs this library nothing.

Every public symbol is rendered:
- 22/22 `public type` records.
- 1/1 `public isolated client class Client`, with `init` and all 9 resource methods.
- `utils.bal` (33 lines) declares no public symbols — it holds the internal query/path
  serialization helpers, so its absence from the render is correct, not a gap.

## 7. Compiler plugin

**No compiler plugin exists for this package.** The bala has no `compiler-plugin/` directory
(contents are only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`) and
the upstream repo at `v2.0.2` contains no `compiler-plugin`, `*-compiler-plugin`, or
`CompilerPlugin.toml` anywhere (`find -iname` returned nothing). `Ballerina.toml` declares only
`[package]` and `[build-options] observabilityIncluded = true`. Nothing plugin-derived is therefore
expected in, or missing from, the render.

## 8. Other considerations

- **Version discipline.** Both renders were produced at pinned `2.0.2`; the bala `package.json`
  reports `"version": "2.0.2"`, built with `ballerina_version 2201.12.2` against
  `distribution = "2201.12.0"`. No drift.
- **Not deprecated, stable major.** `2.0.2` is a stable release; `graalvmCompatible: true`,
  `template: false`. No deprecation markers in the package metadata.
- **Size/token impact is negligible.** +1 line, and the JSON actually shrank from 63,259 to 63,119
  bytes (−140) because the long version-qualified names collapsed. Spec v2 is a net token *saving*
  here despite adding an annotation.
- **Doc quality is good.** Every record field and every resource method carries a doc comment in the
  source, and all of them survive into the render.
- **The `old` render was genuinely non-compiling** at 13 sites (`ballerina/lang.int:0.0.0:Signed32`
  is not a legal type reference). `new` fixes all 13. Line 531's stray doc continuation remains the
  only syntax-level defect in `new`.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | 581 / 582 |
| `diff -u old new` (full, read in entirety) | 9 hunks, +14 / −13 |
| `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| `grep -cE '[a-z]+/[a-z_.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | old 13, new 0 |
| `grep -n '^// --- '` both renders | 4 markers each; new shifted +1 after line 489 |
| `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, v2.0.2; exact match `v2.0.2` → `41f402a7…` |
| `git clone --depth 1 --branch v2.0.2` | succeeded into scratch `…/work/hubspot.crm.associations.schema/src` |
| `diff src/ballerina/types.bal <bala>/modules/…/types.bal` | identical (exit 0) |
| `diff src/ballerina/client.bal <bala>/modules/…/client.bal` | identical (exit 0) |
| `wc -l <bala>/modules/…/*.bal` | client 208, types 292, utils 33 = 533 |
| `grep -nE '^public type' types.bal` | 22 types (lines 23…287) |
| `grep -E '^type ' ` on old / new renders | 22 / 22, same names |
| `grep -cE '^\s+resource function '` old / new | 9 / 9 |
| `grep -cE '^\s+function init'` old / new | 1 / 1 |
| `grep -cE '^(client )?class '` old / new | 1 / 1 |
| `grep -c 'Special Agent Note'` old / new | 17 / 17 |
| `grep -c 'int:Signed32'` types.bal / client.bal / new render | 13 / 1 / 14 |
| `grep -n '^\s*@' <bala>/modules/…/*.bal` | one hit: `types.bal:237 @display {label: "Connection Config"}` |
| `diff <(json.tool old.json) <(json.tool new.json) \| wc -l` | 59 lines: 13 name respellings + 6-line annotations block |
| `wc -c old/*.json new/*.json` | 63,259 / 63,119 |
| `diff <(sed -n '7,236p' old) <(sed -n '7,236p' new)` | identical (README block) |
| `grep -n '^and absent fields' old new` | old:530, new:531 — doc continuation with no `#` |
| `find src -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` | no results |
| `ls -R <bala>` | no `compiler-plugin/` directory |
| `cat src/ballerina/Ballerina.toml` | version 2.0.2, distribution 2201.12.0 |
| `<bala>/package.json` | `"version":"2.0.2"`, `"export":["hubspot.crm.associations.schema"]`, single module |
| `sed -n '493,536p' new \| grep -c '?;'` | 18 optional-marked fields in `ConnectionConfig` vs 7 truly optional in source |

## 10. Caveats and unverified items

- The renders were not compiled. Claims about `old`'s 13 type refs being illegal Ballerina, and
  about line 531's missing `#`, are from reading the grammar, not from a `bal build` run.
- Item 5 of section 5 (`public`/`isolated` stripped) is assumed to be a global renderer convention
  rather than a per-library defect; I verified it holds for this library but did not check other
  libraries' renders to confirm it is universal.
- I did not attempt to re-run the two-stage extraction pipeline; the `old`/`new` renders and JSONs
  were taken as given from the library folder.
- Ballerina Central's registry API was not queried directly; package metadata came from the bala's
  `package.json` and the upstream `Ballerina.toml`, which agree with each other.

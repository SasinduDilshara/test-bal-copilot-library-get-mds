# ballerinax/wso2.apim.catalog 1.3.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/wso2.apim.catalog` |
| Pinned version | `1.3.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-wso2.apim.catalog |
| Tag reviewed | `v1.3.0` (exact match; commit `ea793fef2dccfb9e5285865a98a5ca92b60b2036`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/wso2.apim.catalog/1.3.0` |
| Old render | `449` lines |
| New render | `473` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The library has a single module (the default module `wso2.apim.catalog`), 964 lines of Ballerina
across 6 files. The upstream tag `v1.3.0` is byte-identical to the bala for all 6 `.bal` files
(`diff -q` clean), so GitHub and the bala do not disagree anywhere.

`new` is strictly additive over `old`: +25 lines, −1 line, 7 hunks, 0 declarations removed.
The single removed line is the `// Unknown type: Listener` placeholder, replaced by a real
6-method `class Listener` definition. `new` also recovers the module's only public annotation
(`ServiceCatalogConfig`, which is the whole point of this connector's compiler plugin) and 8
field-level annotations (`@display`, `@constraint:String`) that `old` silently dropped. All 8
annotations and the Listener signature were verified line-by-line against the bala source.

No regressions were found. The inaccuracies that do exist (dropped record-field default values,
one wrong parameter default, closed records rendered as open) are present identically in `old`
and `new` and are pre-existing renderer limitations, not spec-v2 regressions.

## 2. Change inventory

Line counts (`wc -l`): old `449`, new `473`. Diff: 7 hunks, +25 / −1.

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| `// --- section ---` markers | 4 (README, END README, Types, Client) | 5 (+ Annotations) |
| Top-level declarations (`^(public )?(type\|class\|enum\|const\|annotation\|client class)`) | 35 | 37 |
| Member functions (`^    (resource \|remote )?function`) | 11 | 17 |
| Annotation lines in render (`^\s*@`) | 0 | 8 |
| Version/module-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |

JSON model comparison (`old/*.json` vs `new/*.json`):

| Key | old | new |
|---|---|---|
| `typeDefs` | 35 | 35 (same names, set difference empty) |
| `clients` | 1 | 1 (byte-identical JSON) |
| `functions` | 0 | 0 |
| `services` | 0 | 0 |
| `annotations` | 0 | **1** (`ServiceCatalogConfig`) |
| `readme` | 1513 chars | 1513 chars (identical) |
| `description` | identical | identical |

Six `typeDefs` entries differ between the JSONs: `ConnectionConfig`, `ProxyConfig`, `ServiceInfo`,
`Service`, `Verifier`, `Listener`. The first five differ only by newly carried annotation metadata;
`Listener` differs by being modelled as a class instead of an unrenderable type.

### Declarations added in `new` (8)

| Kind | Name |
|---|---|
| class | `Listener` |
| class method | `init(int port) returns ()` |
| class method | `'start() returns error?` |
| class method | `gracefulStop() returns error?` |
| class method | `immediateStop() returns error?` |
| class method | `detach(service object {} s) returns error?` |
| class method | `attach(service object {} s, string[]\|() name = ()) returns error?` |
| annotation | `public annotation ServiceCatalogMetaData ServiceCatalogConfig on service;` |

### Annotations added in `new` (8 lines, on 5 records)

| Render location | Annotation | Source |
|---|---|---|
| `ConnectionConfig` (type-level) | `@display {label: "Connection Config"}` | `types.bal:24` |
| `ProxyConfig.password` | `@display {label: "", kind: "password"}` | `types.bal:77` |
| `ServiceInfo.name` | `@constraint:String {pattern: re \`^[^\*]+$\`}` | `types.bal:167` |
| `Service.name` | `@constraint:String {maxLength: 255, minLength: 1, pattern: re \`^[^\*]+$\`}` | `types.bal:117` |
| `Service.description` | `@constraint:String {maxLength: 1024}` | `types.bal:119` |
| `Service.version` | `@constraint:String {maxLength: 30, minLength: 1}` | `types.bal:121` |
| `Service.serviceKey` | `@constraint:String {maxLength: 512}` | `types.bal:123` |
| `Verifier.'key` | `@constraint:String {pattern: re \`^[^\*]+$\`}` | `types.bal:160` |

### Declarations removed in `new` (0)

None. `diff -u` contains exactly one `-` line: `-// Unknown type: Listener`.

## 3. Correctness against library source

Sources cross-checked: bala `modules/wso2.apim.catalog/{client,init,listener,service,types,utils}.bal`
and the identical upstream files at tag `v1.3.0` under `ballerina/`.

**`class Listener` (new only)** — bala `listener.bal:17-39`:

| Render (new, lines 339-350) | Source | Match |
|---|---|---|
| `function init(int port) returns ();` | `public function init(int port) {` (`listener.bal:36`) | yes (nil return made explicit) |
| `function 'start() returns error?;` | `listener.bal:19` | exact |
| `function gracefulStop() returns error?;` | `listener.bal:24` | exact |
| `function immediateStop() returns error?;` | `listener.bal:27` | exact |
| `function detach(service object {} s) returns error?;` | `listener.bal:30` | exact |
| `function attach(service object {} s, string[]\|() name = ())` | `attach(service object {} s, string[]? name = ())` (`listener.bal:33`) | equivalent (`string[]?` expanded to `string[]\|()`) |

The private field `int port` (`listener.bal:18`) is correctly not surfaced.

**`annotation ServiceCatalogConfig` (new only)** — bala `types.bal:210`:
`public annotation ServiceCatalogMetaData ServiceCatalogConfig on service;` — the render line 473
is character-for-character identical to the source. Its type constraint `ServiceCatalogMetaData`
is present in both renders as a type (new line 299).

**All 8 field/type annotations** — each verified against the exact `types.bal` line in the table in
§2; text, field association and record association all correct.

**Public API completeness in `new`**: all 20 public records, 2 public enums, the public client class
and its 10 resource methods + `init`, the public `Listener` class, and the public annotation from
`types.bal` / `client.bal` / `listener.bal` are present in the `new` render (37 top-level decls +
17 member functions).

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new` in full (73 lines of diff, reproduced end-to-end): exactly one deleted line,
  which is the `// Unknown type: Listener` placeholder.
- Declaration-set comparison: `set(old typeDef names) - set(new typeDef names)` is empty.
- `clients` array in the two JSONs compares byte-identical after canonical `json.dumps(sort_keys=True)`,
  so no client method, parameter, default, return type or doc string changed.
- `readme` field identical (1513 chars both sides) and the rendered README block (lines 7-55)
  is unchanged; it is the complete `docs/README.md` (46 lines / 1513 bytes), not truncated.
- Section markers: `new` has all 4 of `old`'s plus a new `// --- Annotations ---`.
- No `mod:x.y.z:Type` qualified refs existed in `old`, so nothing to compare there.
- Ballerina syntax of the added block is well-formed: `returns ()` is a valid nil return-type
  descriptor, `string[]|()` is a valid union, `service object {}` is a valid parameter type.

## 5. Issues in `new` (independent of `old`)

All five below are present identically in `old`; none is caused by spec v2. They are recorded
because they misrepresent the library to a consuming LLM.

1. **Record-field default values are dropped and required-with-default fields become optional.**
   `types.bal` has 20 fields with defaults (`grep -cE '^\s+.* = .*;$' types.bal` → 20); every one
   renders as `Type name?;`. Examples: `ProxyConfig.host = ""` → `string host?;` (new line 149),
   `ServiceArtifact.version = "_"` → `string version?;` (new line 305),
   `ServiceArtifact.securityType = "BASIC"` → `SecurityType securityType?;` (new line 309),
   `ServiceCatalogMetaData.openApiDefinition = []` → `byte[] openApiDefinition?;` (new line 300),
   `ConnectionConfig.httpVersion = http:HTTP_2_0` → `http:HttpVersion httpVersion?;` (new line 90).
   An LLM reading this cannot know the defaults and will believe these fields are omissible-with-nil
   rather than defaulted.

2. **Wrong parameter default on `get services`.** Source `client.bal:139` declares `int 'limit = 25`;
   both renders emit `int 'limit = 0` (new line 429, old line 412). This is an actively incorrect
   value, not just a dropped one.

3. **Closed records rendered as open.** 6 records are `record {| ... |}` in `types.bal`
   (`ConnectionConfig`, `ClientHttp1Settings`, `ProxyConfig`, `OAuth2PasswordGrantConfig`,
   `ServiceCatalogMetaData`, `ServiceArtifact`); all 20 records render as open `record { ... }`.
   Also `OAuth2PasswordGrantConfig`'s `*http:OAuth2PasswordGrantConfig` inclusion is flattened into
   inline fields rather than shown as an include.

4. **Member ordering is reversed / shuffled.** `enum DefinitionType` renders
   `ASYNC_API, GRAPHQL_SDL, WSDL2, WSDL1, OAS3, OAS2` — the exact reverse of `types.bal:233-240`;
   same for `SecurityType`. Union parameters are re-ordered with `()` interleaved, e.g.
   `"ASYNC_API"|()|"OAS"|"WSDL1"|"WSDL2"|"GRAPHQL_SDL" definitionType` vs the source
   `"OAS"|"WSDL1"|"WSDL2"|"GRAPHQL_SDL"|"ASYNC_API"? definitionType`. Semantically equivalent,
   cosmetically noisy.

5. **`public` qualifier stripped everywhere except the annotation.** All 20 records, 2 enums,
   `class Listener` and `client class Client` render without `public`, while line 473 renders
   `public annotation ...`. Copy-pasting the render would not compile as a library.

## 6. Coverage gaps vs. the library

The bala contains exactly one module (`modules/wso2.apim.catalog`), which is the default module and
the only entry in `package.json`'s `export` list. **There is no submodule-only API**, so the shared
`getDefaultModule()` limitation costs this library nothing.

Every `public` symbol of the default module appears in `new`. The gap that remains in **both** renders:

**12 module-level `configurable` variables** (`service.bal:21-44`), none of which appear in either
render (`grep -c '^configurable' *.bal.txt` → 0 for both):
`serviceUrl`, `username`, `password`, `clientId`, `clientSecret`, `tokenUrl`, `port`,
`clientSecureSocketpath`, `clientSecureSocketpassword`, `serverCert`, `scopes`,
`registeredServiceHostUrl`.

This matters more than usual here: the README's Quickstart is *entirely* about setting these in
`Config.toml`, and `registeredServiceHostUrl` (`service.bal:32-44`) carries 13 lines of doc comment
explaining its `string | map<string>` form. That documentation survives only because it is quoted
nowhere — it is not in the render at all. The renderer models `functions`/`typeDefs`/`clients`/
`services`/`annotations` and has no slot for configurable variables.

Symbols missing from `old` but present in `new`: `Listener` (+6 methods) and `ServiceCatalogConfig`.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.wso2.apim.catalog.ServiceCatalogCompilerPlugin`
with deps `wso2.apim.catalog-compiler-plugin-1.3.0.jar` and `ballerina-to-openapi-2.4.0.jar`.

Upstream `compiler-plugin/src/main/java/.../ServiceCatalogCompilerPlugin.java:30-35` registers a
single `CodeModifier` (`ServiceCatalogModifier`), whose `OpenAPIAnnotationModifier` generates the
OpenAPI definition for each `http:Service` and **injects or updates the
`@wso2.apim.catalog:ServiceCatalogConfig {openApiDefinition: ...}` annotation** on it
(`OpenAPIAnnotationModifier.java:125,164-178`; `utils/Constants.java:28,30`). No code actions and no
diagnostics/validations are registered.

Implication for the render: `ServiceCatalogConfig` is the plugin's central artifact, and `old`
omitted it entirely — meaning `old` gave a consumer no way to know the annotation exists. `new`
surfaces it correctly. Nothing else the plugin implies is missing from `new`; the plugin emits no
additional public Ballerina symbols.

Caveat worth flagging to a reviewer: because the annotation is *auto-injected* by the code modifier,
the intended user flow is `import ballerinax/wso2.apim.catalog as _;` plus `remoteManagement=true`,
not hand-writing `@wso2.apim.catalog:ServiceCatalogConfig`. Exposing it could tempt an LLM to write
it manually with a `openApiDefinition` byte array. That is a doc-context issue, not a render error —
the symbol genuinely is public API.

## 8. Other considerations

- Version is stable (1.3.0, ≥ 1.0). Central metadata / `package.json` show no deprecation flag.
  Keywords: `Type/Connector`, `Type/Trigger`, `Vendor/WSO2`, `Area/Developer Tools`.
- `graalvmCompatible: true`; distribution `2201.13.1`; platform `java21` only.
- Size/token impact of spec v2 here is negligible: +24 net lines (+5.3%).
- The render header emits `import ballerinax/wso2.apim.catalog;` (line 5, both sides) whereas the
  documented primary usage is `import ballerinax/wso2.apim.catalog as _;` (README Quickstart step 1
  and the Examples block, both faithfully reproduced inside the README section). A consumer reading
  only the header line gets the less-common usage; the README text corrects it.
- `client.bal` `Client.init` renders as `function init(ConnectionConfig config, string serviceUrl = "https://apis.wso2.com/api/service-catalog/v1") returns error?;` (new line 428), which matches
  `client.bal` exactly including the default serviceUrl — parameter defaults on *functions* are
  preserved even though defaults on *record fields* are not.
- 12 enum members are additionally emitted as bare `const string` declarations (render lines 59-81)
  duplicating `DefinitionType`/`SecurityType` members. Present in both renders; harmless but
  redundant.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | 449 / 473 |
| 2 | `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| 3 | `grep -n '^// --- '` old / new | 4 markers / 5 markers (`Annotations` added) |
| 4 | `diff -u old new` | 7 hunks, +25 / −1; only deletion is `// Unknown type: Listener` |
| 5 | `ls -R <bala>` | single module `wso2.apim.catalog`; 6 `.bal` files; `compiler-plugin/`, `docs/README.md` |
| 6 | `wc -l <bala>/modules/*/*.bal` | client 239, init 25, listener 39, service 160, types 249, utils 252 = 964 |
| 7 | `git ls-remote --tags <repo>` | `v1.3.0` exists → `ea793fef…` (peeled `a038f3cd…`) |
| 8 | `git clone --depth 1 --branch v1.3.0` | success |
| 9 | `diff -q <bala>/modules/*/X.bal <src>/ballerina/X.bal` for all 6 files | no output → all identical |
| 10 | `cat <src>/ballerina/Ballerina.toml` | `version = "1.3.0"` — pin confirmed on the upstream side |
| 11 | `cat <bala>/package.json` | `version 1.3.0`, `export: ["wso2.apim.catalog"]` |
| 12 | Python JSON compare of `typeDefs` name sets | old-only ∅, new-only ∅ |
| 13 | Python JSON compare of `clients` (canonical dump) | identical |
| 14 | Python JSON compare of `readme` / `description` | identical, 1513 chars |
| 15 | Python JSON `annotations` | old `[]`, new `[{"name":"ServiceCatalogConfig","attachmentPoint":"SERVICE","typeConstraint":{"name":"ServiceCatalogMetaData",…}}]` |
| 16 | Per-typeDef JSON compare | 6 differ: ConnectionConfig, ProxyConfig, ServiceInfo, Service, Verifier, Listener |
| 17 | `grep -n "ServiceCatalog\|constraint\|display" <bala>/types.bal` | lines 24, 77, 117, 119, 121, 123, 160, 167, 210 — all 8 render annotations + the annotation decl matched |
| 18 | `cat -n <bala>/listener.bal` | 6 public methods at lines 19, 24, 27, 30, 33, 36 — all 6 in new render |
| 19 | `wc -c -l <bala>/docs/README.md` | 46 lines / 1513 bytes = the `readme` JSON field, so README is complete in both renders |
| 20 | `grep -cE '^(public )?(type\|class\|enum\|const\|annotation\|client class)'` old / new | 35 / 37 |
| 21 | `grep -cE '^    (resource \|remote )?function '` old / new | 11 / 17 |
| 22 | `grep -c '^\s*@'` old / new | 0 / 8 |
| 23 | `grep -c '^configurable' <bala>/service.bal` and `grep -c 'configurable' *.bal.txt` | 12 in source, 0 in each render |
| 24 | `grep -cE '^\s+.* = .*;$' <bala>/types.bal` | 20 fields with defaults; all render as `?` |
| 25 | `client.bal:139` vs new render line 429 | source `int 'limit = 25`, render `int 'limit = 0` |
| 26 | `grep -c 'record {|' <bala>/types.bal` vs `grep -c 'record {$'` new render | 6 closed in source, 0 closed in render (20 open) |
| 27 | `ServiceCatalogCompilerPlugin.java:30-35`, `OpenAPIAnnotationModifier.java:125,164-178`, `utils/Constants.java:28,30` | single CodeModifier injecting `ServiceCatalogConfig{openApiDefinition}`; no code actions, no diagnostics |

## 10. Caveats and unverified items

- Ballerina Central registry API was not re-queried; version/export/keyword facts were taken from the
  bala's `package.json` and the upstream `Ballerina.toml`, which agree with each other. Deprecation
  status is therefore **unverified** (no deprecation marker exists in either artifact I inspected).
- The renders were not compiled. Syntactic well-formedness of the added `class Listener` block was
  assessed by reading, not by running `bal build`.
- The compiler-plugin and native JARs in the bala were not decompiled; plugin behaviour is taken from
  the upstream Java sources at tag `v1.3.0`, which correspond to the same commit that produced the
  bala but were not byte-verified against the shipped JARs.
- Whether `configurable` variables *should* appear in a Copilot render at all is a renderer design
  question I cannot settle; §6 reports the gap factually without asserting it is a defect.

# ballerina/ldap 1.4.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/ldap` |
| Pinned version | `1.4.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-ldap |
| Tag reviewed | `v1.4.0` (commit `707f30c129c171ad652664a99c3c69b7786d0e82`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/ldap/1.4.0/java21` (distribution 2201.13.4) |
| Old render | `552` lines |
| New render | `553` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`old` and `new` differ in exactly two places, both strict improvements:

1. `// Unknown type: Error` in `old` becomes a real definition `type Error error<ErrorDetails>;` with its doc comment in `new`.
2. The `Client.init` return type `ballerina/ldap:1.4.0:Error?` in `old` becomes the plain `Error?` in `new`.

Nothing is dropped, truncated, renamed, or reordered. Declaration coverage of the default module is complete on both sides (15 public types + 1 client class + 11 client methods). All remaining inaccuracies in `new` are pre-existing renderer limitations shared byte-for-byte with `old`, and are listed in §5 for completeness rather than as regressions.

The upstream tag `v1.4.0` sources (`ballerina/{types,client,error}.bal`) are **byte-identical** to the bala's `modules/ldap/*.bal`, so source and bala agree everywhere and no arbitration was needed.

## 2. Change inventory

Full `diff old new` returns exactly 2 hunks, 3 lines added, 2 removed:

```
270c270,271
< // Unknown type: Error
---
> # Represents any error related to Ballerina LDAP module
> type Error error<ErrorDetails>;
461c462
<     function init(... ConnectionConfig config) returns ballerina/ldap:1.4.0:Error?;
---
>     function init(... ConnectionConfig config) returns Error?;
```

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 | 0 | −1 |
| `// --- section ---` markers | 4 | 4 | 0 |
| `type` declarations (non-enum) | 10 | **11** | +1 (`Error`) |
| `enum` declarations | 3 | 3 | 0 |
| `const string` declarations | 56 | 56 | 0 |
| `client class` | 1 | 1 | 0 |
| Client methods (`init` + `remote`) | 11 | 11 | 0 |
| module-level `function` / `service` / `listener` / `annotation` | 0 | 0 | 0 |
| README block lines (7–100) | identical | identical | 0 |

Declarations added: `type Error`. Declarations removed: none. Declarations modified: `Client.init` (return type only).

JSON side, structural diff of `old/ballerina_ldap.json` vs `new/ballerina_ldap.json` (54223 vs 54253 bytes): same 8 top-level keys, same 71 `typeDefs` by name, same 1 client, same 0 functions/services/annotations. Only two value differences:

- `typeDefs["Error"]`: `new` adds `"baseType": "error<ErrorDetails>"`; `old` has only `{"name","description","type":"Error"}`.
- `clients[0].functions["init"].returnParameters[0].type.name`: `"ballerina/ldap:1.4.0:Error?"` → `"Error?"`.

So the render-level change is fully explained by the JSON-level change; the renderer itself introduced no drift.

## 3. Correctness against library source

The default module exports (bala `package.json` → `"export": ["ldap"]`, single module). Every public symbol checked one-by-one — this library is small enough to be exhaustive.

| Symbol | Source | In `new` render | Verdict |
|---|---|---|---|
| `Error` | `error.bal:18` `public type Error distinct error<ErrorDetails>;` | line 271 `type Error error<ErrorDetails>;` | present; `distinct` and `public` dropped (see §5.1) |
| `ErrorDetails` | `error.bal:23` | line 265 | correct (`string resultCode?`) |
| `ConnectionConfig` | `types.bal:24` | line 276 | fields + types + optionality correct |
| `ClientSecureSocket` | `types.bal:40` | line 292 | field defaults dropped (§5.7) |
| `LdapResponse` | `types.bal:53` | line 306 | 5 fields, types correct incl. `Status resultCode` |
| `SearchResult` | `types.bal:66` | line 365 | correct |
| `SearchReference` | `types.bal:78` | line 377 | correct |
| `Control` | `types.bal:90` | line 389 | correct |
| `SearchScope` | `types.bal:96` (enum, 4 members) | line 410, 4 members | correct (order reversed) |
| `AttributeType` | `types.bal:110` | line 399 `boolean\|int\|float\|decimal\|string\|string[]` | exact match |
| `Entry` | `types.bal:112` `record {\| AttributeType...; \|}` | line 403 | rest field malformed (§5.3) |
| `Person` | `types.bal:122` | line 420 | 5 fields correct; `objectClass` union partially expanded (§5.8) |
| `ObjectClass` | `types.bal:134` (enum, 13 members) | line 434, 13 members | correct (order reversed) |
| `DcObject` | `types.bal:154` | line 453 | correct |
| `Status` | `types.bal:160` (enum, **39** members) | line 320, **39** members | member set complete; explicit string values moved to module-level consts (§5.8) |
| `Client` | `client.bal:19` `public isolated client class Client` | line 461 `client class Client` | present; `isolated`/`public` dropped |

Client methods — source `client.bal` vs render, all 11 accounted for:

| Method | Source line | Render signature | Match |
|---|---|---|---|
| `init` | 26 | line 462 | **mangled**, see §5.2 |
| `add` | 46 | `remote function add(string dN, Entry entry) returns LdapResponse\|Error;` | exact |
| `delete` | 58 | `remote function delete(string dN) returns LdapResponse\|Error;` | exact |
| `modify` | 74 | `remote function modify(string dN, Entry entry) returns LdapResponse\|Error;` | exact |
| `modifyDn` | 87 | `remote function modifyDn(string currentDn, string newRdn, boolean deleteOldRdn = false) returns LdapResponse\|Error;` | exact, default `false` preserved |
| `compare` | 102 | `remote function compare(string dN, string attributeName, string assertionValue) returns boolean\|Error;` | exact |
| `getEntry` | 122 | `remote function getEntry(string dN, string[]\|() attributes = (), anydata targetType = anydata) returns targetType\|Error;` | **typedesc mangled**, §5.4 |
| `searchWithType` | 139 | `remote function searchWithType(string baseDn, string filter, SearchScope scope, string[]\|() attributes = (), record {\|anydata...;\|}[] targetType = record {\|anydata...;\|}[]) returns targetType\|Error;` | **typedesc mangled**, §5.5 |
| `search` | 157 | `remote function search(string baseDn, string filter, SearchScope scope, string[]\|() attributes = ()) returns SearchResult\|Error;` | exact |
| `close` | 168 | `remote function close() returns ();` | exact |
| `isConnected` | 178 | `remote function isConnected() returns boolean;` | exact |

Private `initLdapConnection` (`client.bal:31`) is correctly excluded. Module-level non-public `init()` / `setModule()` (`init.bal:19,23`) are correctly excluded.

The added `Error` definition is correct in substance: `error.bal:18` really does define `Error` over `ErrorDetails`, and the doc string `"Represents any error related to Ballerina LDAP module"` matches `error.bal:17` verbatim.

The README block (render lines 8–99) is identical to the bala's `docs/README.md` apart from one trailing blank line (`diff` reports only `92d91 <` a blank).

## 4. Regressions

**None found.**

Basis for that conclusion — every check run against both files:

- `diff old new` produced exactly the two hunks quoted in §2 and nothing else; both are additive/clarifying.
- Non-const top-level declaration lists (`grep -nE '^(public )?(type|enum|class|client class|annotation|listener|service)'`) are identical except `new` gaining `type Error` at line 271.
- `const string` count identical (56 / 56).
- `Status` enum member count identical (39 / 39) and equal to the source's 39.
- Client method count identical (11 / 11); the 10 remote signatures are character-for-character identical between sides.
- Section markers identical (4 / 4); README region identical.
- JSON: `typeDefs` name sets identical (71 / 71), client function name sets identical, no key removed anywhere — `new`'s `Error` entry is a strict superset of `old`'s (adds `baseType`).
- No new `// Unknown type:` lines in `new` (0), no new version-qualified refs in `new` (0).

Nothing present and correct in `old` is missing, truncated, or made less accurate in `new`.

## 5. Issues in `new` (independent of `old`)

All ten below are also present verbatim in `old` except 5.1, which only exists because `new` now emits the type at all (in `old` the type had no body to be wrong about). None is a regression; they are renderer-fidelity limits worth recording.

**5.1 `distinct` dropped on `Error`.** Source `error.bal:18` is `public type Error distinct error<ErrorDetails>;`. Render line 271 emits `type Error error<ErrorDetails>;`. An LLM reading this would not know `ldap:Error` is a distinct error type, so generated code doing `error e` narrowing / `is ldap:Error` checks may be reasoned about incorrectly. This is the one thing to fix in the new emitter — the underlying JSON `baseType` is `"error<ErrorDetails>"`, i.e. the distinctness is already lost upstream of the renderer.

**5.2 `Client.init` signature is non-compiling and carries fabricated defaults.** Source (`client.bal:26`) is `public isolated function init(*ConnectionConfig config) returns Error?`. The render (line 462) is:

```
function init(string hostName = "", int port = 0, string domainName = "", string password = "", ClientSecureSocket clientSecureSocket = {}, ConnectionConfig config) returns Error?;
```

Three separate problems: (a) the included-record parameter is expanded *and* the original `config` parameter is kept, so the same configuration appears twice; (b) a required parameter `config` follows defaulted parameters, which is invalid Ballerina; (c) `hostName`, `port`, `domainName`, `password` are **required** fields of `ConnectionConfig` (`types.bal:25–28`, no defaults) yet the render invents `= ""` / `= 0` for them. An LLM would plausibly emit `new ldap:Client()` with no arguments.

**5.3 `Entry` rest field is malformed.** Source `types.bal:112–114` is `record {| AttributeType...; |}`. Render lines 403–406 emit:

```
type Entry record {
    # Rest field
    AttributeType ;
};
```

`AttributeType ;` is not valid Ballerina (missing field name and missing `...`), and the closed record became open.

**5.4 `getEntry` typedesc parameter mangled.** Source `client.bal:122`: `typedesc<anydata> targetType = <>`. Render: `anydata targetType = anydata` — the `typedesc<>` wrapper is stripped and the inferred-default `<>` becomes the literal token `anydata`. The dependently-typed return `targetType|Error` is preserved, which now has no valid binding.

**5.5 `searchWithType` typedesc parameter mangled.** Source `client.bal:140`: `typedesc<record {}[]> targetType = <>`. Render: `record {|anydata...;|}[] targetType = record {|anydata...;|}[]`. Same stripping problem, plus the open `record {}` was rewritten to the closed `record {|anydata...;|}`.

**5.6 All closed records rendered as open.** Every `record {| ... |}` in `types.bal` (`ConnectionConfig`, `ClientSecureSocket`, `LdapResponse`, `SearchResult`, `SearchReference`, `Control`, `Entry`) is emitted as `record { ... }`. Semantically this permits fields the library rejects.

**5.7 Record field defaults dropped and defaulted fields marked optional.** `ClientSecureSocket` source has `boolean enable = true` (`types.bal:41`), `boolean verifyHostName = true` (`:43`), `string[] tlsVersions = []` (`:44`) — all required-with-default. The render (lines 292–301) emits `boolean enable?;`, `boolean verifyHostName?;`, `string[] tlsVersions?;`, losing all three defaults.

**5.8 Enum handling: duplicate symbols, reversed order, values relocated.** All 56 enum members of `SearchScope`, `ObjectClass`, `Status` are emitted twice — once as module-level `const string X = "...";` (render lines 105–262) and again as bare members inside the `enum` bodies. Taken as one file that is a duplicate-symbol error. The enum bodies also drop the explicit string values that the source assigns (`OPERATIONS_ERROR = "OPERATIONS ERROR"`, `types.bal:164`); the value survives only in the corresponding const. Member order is reversed relative to source in all three enums.

**5.9 `crypto:TrustStore` referenced without an import.** Render line 296 emits `crypto:TrustStore|string cert?; // Special Agent Note: TrustStore FROM ballerina/crypto package`, but the render's import block (line 5) declares only `import ballerina/ldap;`. Source `types.bal:16` does `import ballerina/crypto;`. The trailing comment mitigates this for an LLM reader.

**5.10 Client method parameter and return docs dropped.** The source documents every parameter and return (`+ dN - The distinguished name of the entry`, `+ return - A \`ldap:Error\` if ...`) and the JSON preserves those strings (`parameters[].description`, `returnParameters[].description`), but the render keeps only the method summary and the example code block. Record fields, by contrast, do keep their docs. This affects all 11 methods on both sides.

## 6. Coverage gaps vs. the library

**None.** `package.json` declares `"export": ["ldap"]` and the bala's `modules/` directory contains exactly one entry, `ldap` — there are no submodules, so the known `getDefaultModule()`-only limitation cannot bite here.

Cross-checking the union of public declarations in `modules/ldap/{types,client,error}.bal` against the render: 15 public types/enums, 1 public client class, 11 public/remote client methods — all 27 appear in `new`. The only source declarations absent from the render are the three non-public ones (`initLdapConnection`, module `init`, `setModule`), which correctly should be absent.

## 7. Compiler plugin

**This library ships no compiler plugin**, consistent with `has_plugin: false`.

Evidence: the bala root `.../1.4.0/java21/` contains exactly `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`, `platform/` — no `compiler-plugin/` directory and no `compiler-plugin.json`; `package.json` has no `compilerPluginDependencies` key. The upstream clone at `v1.4.0` has no `*compiler-plugin*` directory at depth ≤2 (top level is `ballerina/`, `native/`, `build-config/`, `examples/`, `docs/`, `gradle/`). `native/` holds only the JNI implementation (`io.ballerina.lib.ldap.Client`, `ModuleUtils`) that backs the `external` functions, shipped as `platform/java21/ldap-native-1.4.0.jar`.

Nothing plugin-implied is therefore missing from the render.

## 8. Other considerations

- **Version fidelity.** Both renders are at `1.4.0`. The bala `package.json` says `version: 1.4.0`, the clone's `ballerina/Ballerina.toml` says `version = "1.4.0"`, and the three `.bal` files are byte-identical between clone and bala. No version drift.
- **Stability.** `1.4.0` is a stable post-1.0 release; nothing deprecated. `@deprecated` appears nowhere in the sources.
- **Size.** 553 lines / 54 KB JSON — small. The one-line growth is negligible for token budget; removing the `mod:version:Type` noise marginally helps tokenization.
- **Foundational-type check.** This module's externally-consumed types are `ldap:Error`, `ldap:Entry`, `ldap:LdapResponse`, `ldap:SearchResult`, `ldap:Status`, `ldap:SearchScope`. `new` renders `Error` accurately in name/base but without `distinct` (§5.1); `Entry`'s rest field is malformed on both sides (§5.3); the rest are accurate. `Client.init` returning plain `Error?` in `new` rather than `ballerina/ldap:1.4.0:Error?` makes the error type resolvable within the render, which is the concrete downstream benefit of this change.
- **Distribution.** Package declares `distribution = "2201.12.0"`; the bala came from distribution `2201.13.4`. Not an issue for the render, noted for completeness.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l ldap/old/*.bal.txt ldap/new/*.bal.txt` | 552 / 553 |
| 2 | `git clone --depth 1 --branch v1.4.0 …/module-ballerina-ldap` | HEAD `707f30c`, `git describe --tags` → `v1.4.0` |
| 3 | `ls -R <bala>/1.4.0` | `java21/{bala.json,dependency-graph.json,docs,modules,package.json,platform}`; `modules/ldap/{client,error,init,types}.bal`; no plugin dir |
| 4 | `wc -l <bala>/modules/ldap/*.bal` | client 181, error 25, init 25, types 238 |
| 5 | `diff -q <clone>/ballerina/{types,client,error}.bal <bala>/modules/ldap/…` | all three identical |
| 6 | `diff old/ballerina_ldap.bal.txt new/…` | exactly 2 hunks (§2); rc=1 |
| 7 | `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| 8 | `grep -nE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 1 hit (line 461) / 0 hits |
| 9 | `grep -n '^// --- '` old / new | 4 markers each (README 7, END README 100, Types 102, Client 457/458) |
| 10 | `grep -nE '^(public )?(type\|enum\|class\|client class\|annotation\|listener\|service)'` | old 15 decls, new 16 (adds `type Error` @271) |
| 11 | `grep -c '^const string'` old / new | 56 / 56 |
| 12 | `awk '/^public enum Status/,/^}/' types.bal \| grep -cE '^    [A-Z]'` | 39 |
| 13 | same awk on old / new render | 39 / 39 |
| 14 | Python structural diff of both JSONs | 71 typeDefs each, identical name sets; only `Error.baseType` and `init` return type differ |
| 15 | Python diff of `clients[0].functions["init"]` JSON | single line: `ballerina/ldap:1.4.0:Error?` → `Error?` |
| 16 | `diff <(sed -n '8,99p' new render) <bala>/docs/README.md` | one blank-line difference only |
| 17 | `python3 … package.json` | `export: ["ldap"]`, `version: 1.4.0`, `ballerina_version: 2201.12.0`, `template: false`, no `compilerPluginDependencies` |
| 18 | `find <clone> -maxdepth 2 -iname '*compiler-plugin*'` | no matches |
| 19 | `grep -n 'distinct error' error.bal` | `error.bal:18` `public type Error distinct error<ErrorDetails>;` |
| 20 | `grep -n 'AttributeType\.\.\.' types.bal` | `types.bal:113` — render emits `AttributeType ;` |
| 21 | `grep -n 'enable = true\|verifyHostName = true\|tlsVersions = \[\]' types.bal` | lines 41, 43, 44 — none present in render |
| 22 | `grep -n 'typedesc<' client.bal` | lines 122, 140 — both mangled in render |
| 23 | `grep -n 'function init(\*ConnectionConfig' client.bal` | line 26 — render expands + duplicates (§5.2) |
| 24 | `grep -n '^import' new render` | only line 5 `import ballerina/ldap;` (line 21 is inside a README fence) |
| 25 | Manual side-by-side of all 10 remote signatures, `client.bal` vs render lines 466–552 | 8 exact, 2 typedesc-mangled (identical text in `old`) |

## 10. Caveats and unverified items

- The two `ballerina-vscode` checkouts that produced the renders were not inspected; the attribution of the two diffs to the spec-v2 extractor change rests on the brief's stated commits plus the JSON-level evidence (item 14/15), which is consistent with it.
- Ballerina Central's registry API was not re-queried; version, export list, and module list were taken from the bala's `package.json` and `Ballerina.toml`, which are authoritative for what the extractor consumed.
- Neither render was compiled. The syntax problems in §5.2–5.5 and §5.8 were identified by reading against the Ballerina grammar and the source, not by running `bal build`. This applies equally to both sides and so does not affect the regression verdict.
- §5.10 (dropped parameter docs) was confirmed for the render and confirmed present in the JSON, but I did not trace which renderer function discards them.

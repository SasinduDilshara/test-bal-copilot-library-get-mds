# ballerina/oauth2 2.15.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/oauth2` |
| Pinned version | `2.15.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-oauth2 |
| Tag reviewed | `v2.15.0` (clone HEAD `6b527ccb42d9f36cf88543f6beabcaa6c7c139d9`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/oauth2/2.15.0/java21` |
| Old render | `283` lines |
| New render | `307` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`oauth2` is a small, single-module standard library: 20 public symbols in the default module, no
client objects, no module-level public functions, no compiler plugin. The two renders differ in
exactly three hunks (+29 / −5 lines).

`new` is strictly better on all three:

1. `Error` is now emitted as a real type definition instead of `// Unknown type: Error`.
2. The two public classes `ClientOAuth2Provider` and `ListenerOAuth2Provider` — including all four
   of their public methods with parameters, defaults, return types and doc comments — are now
   rendered instead of `// Unknown type: <Name>`.
3. Version-qualified type references (`ballerina/oauth2:2.15.0:ClientCredentialsGrantConfig`) in the
   `ClientAuth` and `GrantConfig` union bodies are gone; plain type names are used.

Nothing present in `old` was dropped, truncated or changed for the worse. Lines 1–172, 174–225 and
227–275 are byte-identical between the two files (the only diverging lines in that span are 173 and
226, the two unions). Every remaining inaccuracy I found (open-vs-closed records, dropped field
defaults, unescaped doc continuation lines) exists identically in both renders and is therefore a
shared renderer limitation, not a spec-v2 regression.

## 2. Change inventory

Line counts (`wc -l`): old `283`, new `307`.

JSON payloads (`python3 -m json.tool` + `diff`) differ in only four places:

| JSON change | old | new |
|---|---|---|
| Union `ClientAuth` member names | `ballerina/oauth2:2.15.0:<T>` ×3 | bare `<T>` ×3 |
| Union `GrantConfig` member names | `ballerina/oauth2:2.15.0:<T>` ×4 | bare `<T>` ×4 |
| `Error` typedef | `"type": "Error"` | `"type": "Error"`, `+ "baseType": "error"` |
| Class typedefs | `type` field absent | `"type": "Class"` ×2 |

Top-level JSON section sizes are identical on both sides: `typeDefs` 24, `clients` 0, `functions` 0,
`services` 0, `annotations` 0; `name`, `description`, `readme` byte-identical.

Declarations added in `new` (6, all in the rendered `.bal.txt` only — the underlying JSON already
carried the class bodies in `old`, the `main` renderer just refused to print them):

| Kind | Name |
|---|---|
| type (error) | `Error` |
| class | `ClientOAuth2Provider` |
| class method | `ClientOAuth2Provider.init` |
| class method | `ClientOAuth2Provider.generateToken` |
| class | `ListenerOAuth2Provider` |
| class method | `ListenerOAuth2Provider.init`, `ListenerOAuth2Provider.authorize` |

Declarations removed in `new`: **0**.

Signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Lines carrying `org/mod:x.y.z:Type` refs | 2 (7 occurrences) | 0 |
| `// --- ` section markers | 3 | 3 |
| Record/enum/const/union/class declarations rendered | 21 (of 24 typeDefs) | 24 |

Declaration set rendered by `new` (24): consts `INFER_REFRESH_CONFIG`, `DEFAULT_CONNECT_TIMEOUT`,
`DEFAULT_REQ_TIMEOUT`, `HTTP_1_1`, `HTTP_2`, `AUTH_HEADER_BEARER`, `POST_BODY_BEARER`; records
`ClientCredentialsGrantConfig`, `ClientConfiguration`, `PasswordGrantConfig`, `RefreshConfig`,
`RefreshTokenGrantConfig`, `SecureSocket`, `CertKey`, `JwtBearerGrantConfig`, `IntrospectionConfig`,
`IntrospectionResponse`; enums `CredentialBearer`, `HttpVersion`; unions `ClientAuth`, `GrantConfig`;
error `Error`; classes `ClientOAuth2Provider`, `ListenerOAuth2Provider`.

## 3. Correctness against library source

The bala module sources and the `v2.15.0` clone are byte-identical for all five `.bal` files
(`diff -q` on `client_oauth2_provider.bal`, `init.bal`, `listener_oauth2_provider.bal`,
`oauth2_commons.bal`, `oauth2_errors.bal` — no output). So GitHub and bala agree; citations below use
the bala paths, which are the same text as `ballerina/*.bal` in the clone.

Everything `new` adds, checked line by line:

| Rendered in `new` | Source | Verdict |
|---|---|---|
| `type Error error;` | `oauth2_errors.bal:21` `public type Error distinct error;` | correct base type; `distinct` dropped (see §5) |
| `class ClientOAuth2Provider` | `client_oauth2_provider.bal:193` `public isolated class ClientOAuth2Provider {` | correct name; `public`/`isolated` dropped (render-wide convention) |
| `function init(GrantConfig grantConfig) returns ()` | `client_oauth2_provider.bal:201` `public isolated function init(GrantConfig grantConfig) {` | correct — init has no return type, so `returns ()` is accurate |
| `function generateToken() returns string\|Error` | `client_oauth2_provider.bal:217` `public isolated function generateToken() returns string\|Error {` | exact match |
| `class ListenerOAuth2Provider` | `listener_oauth2_provider.bal:89` `public isolated class ListenerOAuth2Provider {` | correct |
| `function init(IntrospectionConfig introspectionConfig) returns ()` | `listener_oauth2_provider.bal:98` | exact match |
| `function authorize(string credential, map<string>\|() optionalParams = ()) returns IntrospectionResponse\|Error` | `listener_oauth2_provider.bal:122` `public isolated function authorize(string credential, map<string>? optionalParams = ()) returns IntrospectionResponse\|Error {` | exact match (`map<string>?` expanded to `map<string>\|()`, semantically identical); default `()` preserved |
| `type ClientAuth ClientCredentialsGrantConfig\|PasswordGrantConfig\|RefreshTokenGrantConfig;` | `oauth2_commons.bal:42` | exact match |
| `type GrantConfig ClientCredentialsGrantConfig\|PasswordGrantConfig\|RefreshTokenGrantConfig\|JwtBearerGrantConfig;` | `client_oauth2_provider.bal:155` | exact match |

Both class doc comments and the `generateToken` / `authorize` doc code-fences reproduce the source
docs verbatim, including the source's own typo "acess token" (`listener_oauth2_provider.bal:117`).

Spot checks on the unchanged region (identical in both renders): `IntrospectionResponse`'s 12 fields
and their optionality match `listener_oauth2_provider.bal:52-64` exactly; `CertKey`'s three fields
match `oauth2_commons.bal:66-70`; `JwtBearerGrantConfig`'s field names/types match
`client_oauth2_provider.bal:130-142`; README block (render lines 8–23) is byte-identical to
`docs/README.md` lines 1–15 (`diff` reports only a trailing blank line in the render).

## 4. Regressions

**None found.**

What I checked to conclude that:

- `diff -u old/ballerina_oauth2.bal.txt new/ballerina_oauth2.bal.txt` — 3 hunks total, no line in
  `old` was removed except the 2 version-qualified union lines (replaced by correct plain-name
  versions) and the 3 `// Unknown type:` placeholders (replaced by real definitions).
- Declarations removed in `new`: 0 (verified by extracting all top-level `type|class|enum|const`
  declaration names from both files and taking the set difference — empty).
- JSON set difference of `(name, type)` over all 24 typeDefs: the only difference is the two classes
  gaining `"type": "Class"`. No typeDef, field, parameter, default value or doc string was lost.
- Doc strings: none dropped; new content is additive.
- No malformed syntax was introduced by `new`; the two pre-existing malformed doc-continuation lines
  (90, 93) are present in both files at the same line numbers.

## 5. Issues in `new` (independent of `old`)

All but the first are shared with `old` (i.e. pre-existing renderer behaviour), but they are
inaccuracies in `new` and are listed here per the brief.

1. **`distinct` lost on the error type.** `new` line 281 renders `type Error error;` while the source
   is `public type Error distinct error;` (`oauth2_errors.bal:21`). The JSON records
   `"baseType": "error"` only, so the information never reaches the renderer. An LLM reading this
   render would not know `oauth2:Error` is a distinct error type. Still a large net improvement over
   `old`, which rendered nothing at all.
2. **Closed records rendered as open.** 8 of the 10 public records are `record {| ... |}` in the
   source (`ClientCredentialsGrantConfig`, `RefreshConfig`, `PasswordGrantConfig`,
   `RefreshTokenGrantConfig`, `JwtBearerGrantConfig`, `ClientConfiguration`, `SecureSocket`,
   `CertKey`); both renders emit open `record { ... }` (`grep -c 'record {|'` = 0 in both). Only
   `IntrospectionConfig` and `IntrospectionResponse` are genuinely open.
3. **Field defaults dropped and defaulted fields marked optional.** 22 public record fields carry
   defaults in the source (e.g. `decimal defaultTokenExpTime = 3600;`,
   `CredentialBearer credentialBearer = AUTH_HEADER_BEARER;`, `ClientConfiguration clientConfig = {};`,
   `HttpVersion httpVersion = HTTP_1_1;`, `boolean disable = false;`). Both renders emit these as
   `field?` with no default, e.g. `decimal defaultTokenExpTime?` (new line 58). The defaults —
   arguably the most useful thing an LLM could learn about this module — are absent from both sides.
4. **Non-comment doc continuation lines.** `new` lines 90 and 93 (identical in `old`) emit
   `configuration \`globalConnectTimeout\` which defaults to 15 seconds` as bare text inside the
   `ClientConfiguration` record body, with no leading `#`. The render as a whole therefore does not
   parse as Ballerina. Cause: the source doc comment wraps across two lines
   (`oauth2_commons.bal:26-27`) and only the first line gets the `#` prefix.
5. **Enum members duplicated as module-level string consts.** `HTTP_1_1`, `HTTP_2`,
   `AUTH_HEADER_BEARER`, `POST_BODY_BEARER` are rendered both as `const string X = "X";`
   (lines 37–43) and as members of `enum HttpVersion` / `enum CredentialBearer`. They are enum
   members in the source, not public consts — only `INFER_REFRESH_CONFIG`, `DEFAULT_CONNECT_TIMEOUT`
   and `DEFAULT_REQ_TIMEOUT` are `public const`. Both sides.
6. **Enum member order reversed.** Source `HttpVersion { HTTP_1_1, HTTP_2 }` renders as
   `{ HTTP_2, HTTP_1_1 }`; source `CredentialBearer { AUTH_HEADER_BEARER, POST_BODY_BEARER }` renders
   as `{ POST_BODY_BEARER, AUTH_HEADER_BEARER }`. Harmless semantically but reverses the "first
   member looks like the default" heuristic — and the real defaults are `HTTP_1_1` and
   `AUTH_HEADER_BEARER`, i.e. the ones now shown second. Both sides.
7. **Qualifiers dropped throughout.** No `public` on any type, and `isolated` is dropped from both
   classes and all four methods. This is a render-wide convention (no `public` appears anywhere in
   either file), not specific to the classes, but it means the render does not compile as-is and
   loses the isolated-ness that matters for concurrent use of these providers.

## 6. Coverage gaps vs. the library

**None.** The bala's default (and only) module exports exactly 20 public symbols; all 20 appear in
both renders, and `new` additionally renders the 3 that `old` degraded to placeholders.

Public symbols in `modules/oauth2/*.bal` (from `grep -n "public type|public class|public enum|public const|public isolated function"`):
`ClientConfiguration`, `ClientAuth`, `HttpVersion`, `SecureSocket`, `CertKey`, `CredentialBearer`,
`DEFAULT_CONNECT_TIMEOUT`, `DEFAULT_REQ_TIMEOUT`, `IntrospectionConfig`, `IntrospectionResponse`,
`ListenerOAuth2Provider` (+ `init`, `authorize`), `ClientCredentialsGrantConfig`,
`INFER_REFRESH_CONFIG`, `RefreshConfig`, `PasswordGrantConfig`, `RefreshTokenGrantConfig`,
`JwtBearerGrantConfig`, `GrantConfig`, `ClientOAuth2Provider` (+ `init`, `generateToken`), `Error`.

Submodule-only API: **none**. `ls <bala>/modules` lists exactly one directory, `oauth2`, and
`package.json` has `"export": ["oauth2"]`; Central's package metadata for `ballerina/oauth2/2.15.0`
also lists a single module. The `getDefaultModule()`-only extraction limitation therefore costs this
library nothing.

Module-level public functions: there are none in the source, and both renders have `"functions": []` —
correct, not a gap. Likewise `clients: []` is correct: the OAuth2 providers are plain classes, not
`client` objects (`public isolated class`, not `public isolated client class`).

## 7. Compiler plugin

`has_plugin: false` in the manifest, confirmed independently:

- `find <bala root> -iname "*compiler*"` → no results; the bala contains only `bala.json`,
  `dependency-graph.json`, `docs/`, `modules/`, `package.json`, `platform/` — there is no
  `compiler-plugin/` directory and no `compiler-plugin.json`.
- `find <clone> -maxdepth 3 -iname "*compiler-plugin*"` → no results. The repo's only native
  component is `native/` (the `oauth2-native-2.15.0.jar` Java interop backing `doHttpRequest`),
  which is a platform dependency, not a compiler plugin.

Nothing plugin-related is therefore expected in, or missing from, the render.

## 8. Other considerations

- **Version/stability**: `2.15.0`, stable, `graalvmCompatible: true`, built with Ballerina
  `2201.13.0`. Central reports `deprecated: null`, empty `deprecateMessage`, 9,567 pulls. No
  deprecation to flag.
- **Foundational-type accuracy** (per the batch addendum): `oauth2:Error` is the type other packages
  depend on. `new` now renders it (`type Error error;`) where `old` rendered nothing usable — a
  direct improvement for downstream libraries (`http`, `websocket`, etc.) whose auth configs
  reference `oauth2:ClientAuth` / `oauth2:GrantConfig`. Those two unions are now also rendered with
  plain member names instead of `ballerina/oauth2:2.15.0:...`, which is the form a consumer would
  actually write. `crypto:TrustStore`, `crypto:KeyStore` and `cache:CacheConfig` cross-package
  references are rendered identically on both sides, with the `// Special Agent Note: X FROM
  ballerina/Y package` trailer intact (render lines 185, 187, 242).
- **Size/tokens**: both files are tiny (11.8 KB old, 12.6 KB new; +818 bytes, +8.5%). The JSON is
  33.4 KB old / 33.4 KB new. No token-budget concern.
- **Doc quality**: source docs are complete (every public record field and function parameter has a
  `# +` doc line) and survive into the render. The source typo "acess token" is faithfully carried
  through.
- The render is a documentation stub, not compilable Ballerina (no `public`, no `isolated`, class
  bodies are signatures only, plus the two unprefixed doc-continuation lines). That is the
  established convention of this pipeline on both sides.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.15.0 <repo> <scratch>/src` | succeeded; HEAD `6b527ccb42d9f36cf88543f6beabcaa6c7c139d9` |
| `diff -q <bala>/modules/oauth2/<f>.bal <clone>/ballerina/<f>.bal` × 5 files | no differences — bala == tag source |
| `wc -l old/ballerina_oauth2.bal.txt new/ballerina_oauth2.bal.txt` | 283 / 307 |
| `ls -l` on both `.json` | old 33,470 B; new 33,375 B |
| `diff -u old new` (renders) | 3 hunks, +29/−5, full text reviewed |
| `grep -c '^// Unknown type:'` | old 3, new 0 |
| `grep -nE '[a-z]+/[a-z0-9.]+:[0-9]+\.[0-9]+\.[0-9]+:' \| wc -l` | old 2 lines (7 occurrences), new 0 |
| `grep -n '^// --- '` | both: lines 7, 24, 26 (README / END README / Types) |
| `diff <(python3 -m json.tool old.json) <(python3 -m json.tool new.json)` | 4 change sites only (2 unions, `baseType`, 2× `"type":"Class"`) |
| python: section lengths of both JSONs | typeDefs 24/24, clients 0/0, functions 0/0, services 0/0, annotations 0/0; `name`/`description`/`readme` identical |
| python: `(name, type)` set-diff over typeDefs | only `ClientOAuth2Provider`/`ListenerOAuth2Provider` gaining `"Class"` |
| python: dumped both classes' JSON on both sides | function lists, parameters, defaults, returns and docs byte-identical; `old` simply never rendered them |
| `grep -n "public class\|public function\|public isolated function\|public type\|public const\|public enum" <bala>/modules/oauth2/*.bal` | 20 public symbols + 4 public methods; all present in both renders |
| `ls <bala>/modules` | single entry `oauth2` |
| `cat <bala>/package.json` | `"export": ["oauth2"]`, `platform: java21`, `graalvmCompatible: true`, `ballerina_version: 2201.13.0` |
| `find <bala root> -iname "*compiler*"` | no results |
| `find <clone> -maxdepth 3 -iname "*compiler-plugin*"` | no results |
| `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/oauth2/2.15.0` | 1 module (`oauth2`), `deprecated: null`, pullCount 9567 |
| `diff <(sed -n '8,23p' new render) <(sed -n '1,16p' <bala>/docs/README.md)` | identical except one trailing blank line |
| python: parse of `public type X record {\|...\|}` blocks | 10 records: 8 closed, 2 open; 22 fields carry defaults |
| `grep -c 'record {\|'` on renders | 0 in both (all closed records rendered open) |
| `grep -cE '^\s+[A-Za-z].* = '` on renders | old 0, new 1 (the `optionalParams = ()` parameter default) — no field defaults on either side |
| `grep -n "configuration \`global"` on renders | lines 90, 93 in **both** files (unprefixed doc continuation) |
| Source line citations verified by `sed -n` | `oauth2_errors.bal:21`, `client_oauth2_provider.bal:34,47,56,78,105,130,155,193,201,217`, `listener_oauth2_provider.bal:29,52,89,98,122`, `oauth2_commons.bal:31,42,45,55,66,73`, `init.bal:20,23` |

## 10. Caveats and unverified items

- I did not execute the render pipeline myself; I audited the committed artefacts under
  `oauth2/old/` and `oauth2/new/`. The brief's statement that both sides were produced at the same
  pinned version is consistent with what I observed (identical `name`/`description`/`readme`,
  identical typeDef set, identical field/parameter data) but was not independently re-derived.
- Whether `distinct` is recoverable from the extractor's model is unverified — the JSON on both sides
  carries only `"baseType": "error"`, so I cannot say whether the loss originates in the Java
  extractor or in the TypeScript renderer.
- I did not attempt to compile the render with `bal build`; the "does not compile" statements in §5
  are based on reading the syntax (missing `#` prefixes on lines 90/93, signature-only class bodies),
  not on a compiler run.

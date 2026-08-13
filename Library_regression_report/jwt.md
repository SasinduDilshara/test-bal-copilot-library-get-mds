# ballerina/jwt 2.15.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/jwt` |
| Pinned version | `2.15.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-jwt |
| Tag reviewed | `v2.15.1` |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/jwt/2.15.1/java21` |
| Old render | `274` lines |
| New render | `298` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/jwt` is a small, single-module standard library: the bala ships exactly one module
(`modules/jwt`) with 7 `.bal` files and 24 public declarations. All seven bala `.bal` files are
byte-identical to the `v2.15.1` GitHub tag (`diff -q`, 7/7 `SAME`), so upstream source and the
extractor input agree completely.

`new` is a strict superset of `old` in information content. Every one of the five diff hunks is a
fix:

- 3 `// Unknown type:` placeholders (`Error`, `ClientSelfSignedJwtAuthProvider`,
  `ListenerJwtAuthProvider`) become real definitions — 3 → 0.
- 6 version/module-qualified type references (`ballerina/crypto:2.12.1:KeyStore`,
  `ballerina/cache:3.10.0:CacheConfig`, `ballerina/jwt:2.15.1:ClientConfiguration`,
  `ballerina/crypto:2.12.1:TrustStore`, and `ballerina/jwt:2.15.1:Header`/`Payload` in
  `decode`'s return type) become idiomatic refs — 6 → 0.

Nothing is dropped: 0 declarations removed, README byte-identical, module description identical,
all 4 section markers and all 5 "Special Agent Note" cross-package annotations preserved. Public
API coverage in `new` is 24/24. Remaining inaccuracies are minor and mostly shared with `old`.

## 2. Change inventory

Line counts: `old` 274, `new` 298 (`wc -l`). Diff: +31 / −7 across 5 hunks (`diff old new`).

JSON-level structure is unchanged in shape — both sides: `typeDefs` 23, `clients` 0, `functions` 3,
`services` 0, `annotations` 0. `readme` and `description` compare equal. Exactly 5 `typeDefs`
entries differ, plus 1 function.

**Declarations added in `new` (6)** — all previously degraded or absent:

| Kind | Name | Old form |
|---|---|---|
| type (error) | `Error` | `// Unknown type: Error` |
| class | `ClientSelfSignedJwtAuthProvider` | `// Unknown type: ClientSelfSignedJwtAuthProvider` |
| class method | `init(IssuerConfig)` | absent |
| class method | `generateToken()` | absent |
| class | `ListenerJwtAuthProvider` | `// Unknown type: ListenerJwtAuthProvider` |
| class method | `init(ValidatorConfig)` | absent |
| class method | `authenticate(string)` | absent |

(The table lists 5 members under 2 classes; the mechanical diff counts them as 6 top-level
"declarations added" because `init` is deduplicated.)

**Declarations removed in `new`: 0.**

**Declarations modified (4 sites, all type-reference normalisation):**

| Site | old | new |
|---|---|---|
| `IssuerSignatureConfig.config` | `record {\|ballerina/crypto:2.12.1:KeyStore keyStore; …\|}` | `record {\|crypto:KeyStore keyStore; …\|}` |
| `ValidatorSignatureConfig.jwksConfig` | `ballerina/cache:3.10.0:CacheConfig`, `ballerina/jwt:2.15.1:ClientConfiguration` | `cache:CacheConfig`, `ClientConfiguration` |
| `ValidatorSignatureConfig.trustStoreConfig` | `ballerina/crypto:2.12.1:TrustStore` | `crypto:TrustStore` |
| `function decode` return | `[ballerina/jwt:2.15.1:Header, ballerina/jwt:2.15.1:Payload]\|Error` | `[Header, Payload]\|Error` |

**Underlying JSON deltas** (the cause of the render deltas): `Error` gains `"baseType": "error"`;
both provider entries gain `"type": "Class"` (their `functions` arrays were already present and
identical in `old` — `main`'s `renderTypeDef` simply had no branch for an untagged entry); the four
type-name strings above are rewritten. No other JSON field changed.

Signals verified independently: `// Unknown type:` 3 → 0; `ballerina/<mod>:<ver>:` occurrences
6 → 0; `// --- ` section markers 4 → 4; `Special Agent Note` comments 5 → 5.

## 3. Correctness against library source

All 24 public declarations of the default module were enumerated from the bala
(`grep -nE '^public ' modules/jwt/*.bal`) and checked against the render.

| Public symbol | Bala file:line | In `new` render | Correct |
|---|---|---|---|
| `Error` | `jwt_errors.bal:21` | l.131 `type Error error;` | mostly — see §5.1 |
| `SigningAlgorithm` | `jwt_commons.bal:20` | l.93 | yes (const union expanded to string literals) |
| `RS256` `RS384` `RS512` `HS256` `HS384` `HS512` `NONE` | `jwt_commons.bal:23,26,29,32,35,38,41` | l.68–86 | yes |
| `Header` | `jwt_commons.bal:64` | l.98–107 | yes (4 optional fields `alg`,`typ`,`cty`,`kid`) |
| `Payload` | `jwt_commons.bal:80` | l.112–127 | yes (`iss`,`sub`,`aud`,`exp`,`nbf`,`iat`,`jti`) |
| `IssuerConfig` | `jwt_issuer.bal:30` | l.136–153 | yes (closedness lost, §5.5) |
| `IssuerSignatureConfig` | `jwt_issuer.bal:45` | l.158–163 | yes |
| `issue` | `jwt_issuer.bal:65` | l.279 | yes — `(IssuerConfig) returns string\|Error` |
| `ValidatorConfig` | `jwt_validator.bal:36` | l.168–187 | yes |
| `ValidatorSignatureConfig` | `jwt_validator.bal:54` | l.192–201 | yes |
| `ClientConfiguration` | `jwt_validator.bal:72` | l.206–211 | yes |
| `HttpVersion` | `jwt_validator.bal:78` | l.214–217 | yes |
| `SecureSocket` | `jwt_validator.bal:88` | l.222–229 | yes |
| `CertKey` | `jwt_validator.bal:99` | l.234–241 | yes |
| `validate` | `jwt_validator.bal:113` | l.289 | yes — `(string, ValidatorConfig) returns Payload\|Error` |
| `decode` | `jwt_validator.bal:135` | l.298 | yes — `(string) returns [Header, Payload]\|Error` |
| `ClientSelfSignedJwtAuthProvider` | `client_self_signed_jwt_auth_provider.bal:33` | l.245–254 | yes |
| `ListenerJwtAuthProvider` | `listener_jwt_auth_provider.bal:36` | l.258–267 | yes |

Spot-checks on the newly added material specifically:

- `ClientSelfSignedJwtAuthProvider.init(IssuerConfig issuerConfig)` — matches
  `client_self_signed_jwt_auth_provider.bal:39` (`public isolated function init(IssuerConfig issuerConfig)`).
  The render's `returns ()` is an explicit nil return, semantically equivalent to the source's
  omitted return type; not an error.
- `generateToken() returns string|Error` — matches `client_self_signed_jwt_auth_provider.bal:48`.
- `ListenerJwtAuthProvider.init(ValidatorConfig validatorConfig)` — matches
  `listener_jwt_auth_provider.bal:44`.
- `authenticate(string credential) returns Payload|Error` — matches `listener_jwt_auth_provider.bal:75`.
  Note the render's doc example `boolean result = check provider.authenticate(...)` is verbatim
  from the source doc comment (`listener_jwt_auth_provider.bal:70`) and is wrong *in the library
  itself* (the method returns `Payload`, not `boolean`) — faithfully reproduced, not introduced.
- `Error` doc text matches `jwt_errors.bal:19–20` verbatim.
- Cross-package refs `crypto:KeyStore`, `crypto:PrivateKey`, `crypto:PublicKey`, `crypto:TrustStore`,
  `cache:CacheConfig` in `new` match the field types in `jwt_issuer.bal:45–63` and
  `jwt_validator.bal:36–70`. `new`'s unversioned form is the correct way to write these in
  Ballerina; `old`'s `ballerina/crypto:2.12.1:KeyStore` was not valid syntax.

No private/internal symbols leaked into either render (`prepareError`, `preloadJwksToCache`,
`validateFromCache`, `addToCache`, `encodeBase64Url`, `decodeBase64Url`, `setModule` — none appear).

## 4. Regressions

**None found.**

Checked, with the specific method used:

- Declaration set: JSON key-set comparison of `typeDefs` by name — `old only: set()`,
  `new only: set()`; 23 on both sides. `functions` 3/3, same names.
- Textual: full `diff old new` (5 hunks, reproduced in §2) — every `-` line is either an
  `// Unknown type:` placeholder or a version-qualified type reference. No doc line, parameter,
  default value, return type, or record field appears on a `-` line without a superset replacement.
- README/prose: `o['readme'] == n['readme']` → `True`; `o['description'] == n['description']` → `True`.
- Section markers: `grep -c '^// --- '` → 4 on both.
- Cross-package annotations: `grep -c 'Special Agent Note'` → 5 on both.
- Syntax: `new`'s added constructs (`type Error error;`, `class X { function f(...) returns T; }`)
  are well-formed Ballerina declaration syntax; `old`'s removed constructs
  (`ballerina/crypto:2.12.1:KeyStore`) were not. Syntactic validity improved.

## 5. Issues in `new` (independent of `old`)

All six are low severity; none is a regression (items 4–6 are equally present in `old`).

1. **`distinct` dropped from the error type.** Source: `public type Error distinct error;`
   (`jwt_errors.bal:21`). Render: `type Error error;` (l.131). The JSON carries
   `"baseType": "error"` with no distinctness marker, so this is an extractor-level loss.
   Consequence is small (`x is jwt:Error` and `check` still read correctly), but a consumer LLM
   cannot tell that `jwt:Error` is a distinct subtype and e.g. that a plain `error` value is not
   assignable to it.
2. **Class visibility/isolation qualifiers dropped.** Source declares
   `public isolated class ClientSelfSignedJwtAuthProvider` (l.33) and
   `public isolated class ListenerJwtAuthProvider` (l.36); the render emits bare
   `class ClientSelfSignedJwtAuthProvider {` (l.245) / `class ListenerJwtAuthProvider {` (l.258),
   and their methods as bare `function`. This matches the render's global convention (module-level
   `function issue`/`validate`/`decode` are also stripped of `public isolated`), so it is
   consistent — but an LLM told these classes are non-isolated may avoid them in isolated contexts.
3. **Class-method parameter/return docs are discarded by the renderer although present in the JSON.**
   The JSON for `generateToken` carries
   `"return": {"description": "Generated token or else a \`jwt:Error\` if an error occurred", …}` and
   `init` carries `"parameters":[{"name":"issuerConfig","description":"JWT issuer configurations",…}]`,
   yet the render emits only a bare `# ` line (l.252, l.265) where the top-level Functions section
   does emit `# + param -` / `# + return -` lines (l.277–278, 286–288). Inconsistent fidelity;
   information available in the model is thrown away.
4. **Class description is the constructor's doc, not the class's doc.** Render l.243 says
   "Provides authentication based on the provided JWT configurations." — that is the doc of
   `init` (`client_self_signed_jwt_auth_provider.bal:36`). The actual class doc
   ("Represents the client JWT Auth provider, which is used to authenticate with an external
   endpoint…", l.18–19) together with its `new({...})` usage example (l.20–31) is absent from the
   JSON on **both** sides, so the render never sees it. The lost example is the only place the
   docs show how to instantiate these providers.
5. **Closed records rendered as open.** `IssuerConfig`, `IssuerSignatureConfig`,
   `ValidatorSignatureConfig`, `ClientConfiguration`, `SecureSocket`, `CertKey` are all
   `record {| … |}` in source (`jwt_issuer.bal:30,45`; `jwt_validator.bal:54,72,88,99`) but render
   as `record { … };`. `Header`, `Payload`, `ValidatorConfig` are genuinely open and render
   correctly. Present identically in `old`. An LLM may believe it can add arbitrary fields to
   `jwt:IssuerConfig`, which would not compile.
6. **`HTTP_1_1` / `HTTP_2` duplicated as bare consts.** Render l.88–90 emits
   `const string HTTP_1_1 = "HTTP_1_1";` and `const string HTTP_2 = "HTTP_2";` with no doc, and
   then re-declares them as members of `enum HttpVersion` at l.214–217. They are enum members
   (`jwt_validator.bal:78–86`), not standalone module constants. Harmless but redundant; identical
   in `old`.

## 6. Coverage gaps vs. the library

**Zero gaps.** All 24 `public` declarations of the default module `jwt` appear in the `new` render
(mapping table in §3). `old` had 3 gaps in substance (`Error`, both provider classes were reduced
to name-only placeholders with no members).

**No submodule gap:** `modules/` in the bala contains exactly one directory, `jwt`, which *is* the
default module. The known shared limitation (`pkg.getDefaultModule()` only) therefore costs this
library nothing.

Not exported and correctly absent: the `native/` Java classes (`JwtUtils`, `JwksClient`,
`ModuleUtils`, `JwtConstants`) are interop implementation, reachable only through the module-private
`@java:Method` bindings in `jwt_commons.bal:90,94` and `init.bal:23`.

## 7. Compiler plugin

`has_plugin: true` — confirmed: `java21/compiler-plugin/compiler-plugin.json` declares
`plugin_id: jwt-compiler-plugin`, `plugin_class: io.ballerina.stdlib.jwt.compiler.JwtCompilerPlugin`,
backed by `compiler-plugin/libs/jwt-compiler-plugin-2.15.1.jar`.

What it contributes (read from the `v2.15.1` clone,
`compiler-plugin/src/main/java/io/ballerina/stdlib/jwt/compiler/`):

- `JwtCompilerPlugin.init` registers a `JwtCodeAnalyzer` **only when a `ScannerContext` is present
  in `context.userData()`** — i.e. the plugin is purely a *static code analyzer* hook for
  `bal scan`. It adds no code modifiers, no code actions, and no generated artifacts.
- One rule, `JwtRule.AVOID_WEAK_CIPHER_ALGORITHMS` (numeric id 1, kind `VULNERABILITY`):
  "Avoid using weak cipher algorithms when signing and verifying JWTs".
- `JwtCipherAlgorithmAnalyzer` implements it: it inspects calls to `jwt:issue()` and reports when
  `signatureConfig.algorithm` resolves to `NONE`, covering inline mapping literals,
  function-local variables, and module-level config (`JwtCipherAlgorithmAnalyzer.java:57–58,
  79–82, 114–117, 230–246`).

**Nothing the plugin implies is missing from the render.** The plugin defines no annotations
(consistent with `annotations: []` in both JSONs) and no additional types. The only render-relevant
implication is advisory — that `jwt:NONE` is a scan-flagged vulnerability — and the render does
carry the raw signal an LLM needs: `NONE` is documented as "Unsecured JWS (no signing)" (l.85–86)
and is a member of `SigningAlgorithm` (l.93). Neither render states that using it is flagged as a
vulnerability; that is a pre-existing, side-neutral gap, since the pipeline does not extract
compiler-plugin scan rules for any library.

## 8. Other considerations

- **Stability/deprecation:** version `2.15.1` is post-1.0; no `@deprecated` annotation anywhere in
  the bala module sources. Nothing to flag.
- **Size:** 298 lines is tiny; the +24 lines (+8.8%) cost is negligible against making three public
  types usable. Token impact is immaterial.
- **Foundational-type accuracy** (this batch's specific concern): `jwt:Error` is the type other
  packages depend on most (it is the error type surfaced by `http`'s JWT auth handlers). `old`
  rendered it as `// Unknown type: Error`, which is actively misleading for a consumer that must
  write `jwt:Error`; `new` renders a usable definition. `jwt:Payload` and `jwt:Header` — the other
  two types consumed downstream — are correct and unchanged on both sides. Cross-package refs into
  `crypto` and `cache` are now written in valid Ballerina syntax, which matters because those types
  (`crypto:KeyStore`, `crypto:PrivateKey`, `cache:CacheConfig`) are what a user must actually type.
- **Doc-comment bug reproduced from upstream:** `authenticate`'s example says
  `boolean result = check provider.authenticate("<credential>")` while the signature returns
  `Payload|Error`. This is an upstream documentation defect (`listener_jwt_auth_provider.bal:70`),
  newly visible in `new` because the method is now rendered at all. Worth reporting upstream; not a
  pipeline defect.
- **Provenance:** bala and GitHub `v2.15.1` sources are byte-identical for all 7 module files, so
  there is no bala-vs-source ambiguity for this library.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ballerina_jwt.bal.txt new/ballerina_jwt.bal.txt` | 274 / 298 |
| 2 | `git clone --depth 1 --branch v2.15.1 …/module-ballerina-jwt` | tag exists, clone OK |
| 3 | `ls -R <bala>` | single platform dir `java21`; `modules/jwt` only; `compiler-plugin/libs/jwt-compiler-plugin-2.15.1.jar` present |
| 4 | `diff -q <clone>/ballerina/<f> <bala>/modules/jwt/<f>` ×7 | 7/7 `SAME` |
| 5 | `wc -l <bala>/modules/jwt/*.bal` | 1273 lines total across 7 files |
| 6 | `grep -nE '^public ' <bala>/modules/jwt/*.bal` | 24 public declarations (listed in §3) |
| 7 | `grep -c '^// Unknown type:'` old/new | 3 / 0 |
| 8 | `grep -oE 'ballerina/[a-z.]+:[0-9][^:]*:' old \| wc -l` | 6 (0 in new) |
| 9 | `grep -c '^// --- '` old/new | 4 / 4 |
| 10 | `grep -c 'Special Agent Note'` old/new | 5 / 5 |
| 11 | `diff old new` | 5 hunks, +31 / −7; full text reviewed |
| 12 | Python: JSON section sizes | typeDefs 23/23, clients 0/0, functions 3/3, services 0/0, annotations 0/0 |
| 13 | Python: `readme` / `description` equality | both `True` |
| 14 | Python: typeDef name-set difference | `old only: set()`, `new only: set()` |
| 15 | Python: per-typeDef deep compare | 5 differ: `Error`, `ClientSelfSignedJwtAuthProvider`, `ListenerJwtAuthProvider`, `IssuerSignatureConfig`, `ValidatorSignatureConfig` |
| 16 | Python: per-function deep compare | 1 differs: `decode` (return type string only) |
| 17 | Python: dump of `Error` old vs new | new adds `"baseType": "error"`; description identical |
| 18 | Python: dump of `ClientSelfSignedJwtAuthProvider` old vs new | new adds `"type": "Class"`; `functions` array byte-identical in `old` |
| 19 | Read `jwt_errors.bal` | `public type Error distinct error;` (l.21) |
| 20 | Read `client_self_signed_jwt_auth_provider.bal` | `public isolated class` l.33; `init` l.39; `generateToken` l.48; class doc l.18–31 |
| 21 | Read `listener_jwt_auth_provider.bal` | `public isolated class` l.36; `init` l.44; `authenticate` l.75; `boolean` doc defect l.70 |
| 22 | `cat <bala>/compiler-plugin/compiler-plugin.json` | plugin_id `jwt-compiler-plugin`, class `JwtCompilerPlugin` |
| 23 | Read `JwtCompilerPlugin.java` | registers `JwtCodeAnalyzer` only under `ScannerContext` |
| 24 | Read `JwtRule.java` | 1 rule, id 1, kind `VULNERABILITY`, weak cipher algorithms |
| 25 | `grep` `JwtCipherAlgorithmAnalyzer.java` | inspects `jwt:issue()` for `algorithm == NONE` (l.57–58, 114–117, 246) |
| 26 | `cat OLD_AND_NEW_DIFFS/jwt_diff.md` | every figure re-derived independently and matched (checks 1, 7, 8, 9, 11) |

## 10. Caveats and unverified items

1. The compiler-plugin jar in the bala (`jwt-compiler-plugin-2.15.1.jar`) was not decompiled; the
   plugin description in §7 comes from the `v2.15.1` GitHub sources. Since all seven `.bal` files
   are byte-identical between the tag and the bala, the plugin sources are almost certainly the
   same build, but the jar's bytecode was not independently confirmed.
2. Neither render was compiled. Syntactic validity claims in §4 are by inspection of the emitted
   declaration forms, not by running `bal build`. (The renders are declaration stubs with bodies
   elided, so they are not compilable as-is by design.)
3. Ballerina Central metadata for `ballerina/jwt/2.15.1` was not re-queried over the network; the
   module list was taken from the bala's `modules/` directory, which is authoritative for what the
   extractor consumed.
4. §5.4 states the class-level doc is absent from the JSON on both sides — verified for
   `ClientSelfSignedJwtAuthProvider` and `ListenerJwtAuthProvider` by dumping their full JSON
   entries (check 18). Whether this is an extractor limitation or a docs-model limitation upstream
   was not traced into the `CopilotLibraryManager` source.

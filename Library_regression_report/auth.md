# ballerina/auth 2.14.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/auth` |
| Pinned version | `2.14.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-auth |
| Tag reviewed | `v2.14.0` (commit `252ad7ea5daa9488a08694738c462cb0f3790b16`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/auth/2.14.0/java21` |
| Old render | `142` lines |
| New render | `182` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`auth` is a small, single-module standard library: 11 public symbols in the default module, no
compiler plugin, no submodules. The `new` render is a strict superset of `old`. The JSON diff is
exactly three additions and zero removals: `baseType: "error"` on `Error`, a `functions` array on
`ListenerBasicAuthProvider`, and `type: "Class"` on the three provider classes. Those three
`type: "Class"` tags are what let the renderer stop emitting `// Unknown type:` placeholders.

Result: the four `// Unknown type:` placeholders in `old` (`Error`, `ClientBasicAuthProvider`,
`ListenerFileUserStoreBasicAuthProvider`, `ListenerLdapUserStoreBasicAuthProvider`) become real
definitions carrying 7 method/constructor signatures, and `ListenerBasicAuthProvider` gains its one
interface method. Nothing present in `old` is missing, truncated, or degraded in `new`. Every added
signature was verified line-by-line against the bala source, which is byte-identical to the GitHub
tag. All remaining inaccuracies are extraction-level and identical on both sides.

## 2. Change inventory

Line counts (`wc -l`): old `142`, new `182` (+40). JSON: old `451`, new `487`.

`// Unknown type:` placeholders (`grep -c`): old `4`, new `0`.
Section markers (`grep -c '^// --- '`): old `4`, new `4` (README, END README, Types, Functions).
Version-qualified type refs (`grep -cE ':[0-9]+\.[0-9]+\.[0-9]+:'`): old `0`, new `0`.

Top-level declarations (`grep -nE '^(type|class|function|enum|const|annotation|service|listener)'`):

| kind | old | new | delta |
|---|---|---|---|
| `type` (record) | 5 | 5 | 0 |
| `type` (error) | 0 | 1 | +1 (`Error`) |
| `class` | 1 | 4 | +3 |
| `function` (module-level) | 1 | 1 | 0 |
| **total** | **7** | **11** | **+4** |

Nested class members (`grep -nE '^    (function|resource|remote)'`): old `0`, new `7`.

**Added in `new` (11 declarations/members, 0 removed):**

- `type Error error;` (was `// Unknown type: Error`)
- `class ClientBasicAuthProvider` (was `// Unknown type: ClientBasicAuthProvider`), with
  `init(CredentialsConfig credentialsConfig) returns ()` and `generateToken() returns string|Error`
- `class ListenerFileUserStoreBasicAuthProvider` (was placeholder), with
  `init(FileUserStoreConfig fileUserStoreConfig = {}) returns ()` and
  `authenticate(string credential) returns UserDetails|Error`
- `class ListenerLdapUserStoreBasicAuthProvider` (was placeholder), with
  `init(LdapUserStoreConfig ldapUserStoreConfig) returns ()` and
  `authenticate(string credential) returns UserDetails|Error`
- `ListenerBasicAuthProvider.authenticate(string credential) returns UserDetails|Error` (class body
  was empty `{}` in `old`)
- Doc comments for `Error` (3 lines) and for each new class/method, including the
  ` ```ballerina ` usage snippets for `generateToken` and both `authenticate` methods

**Removed in `new`:** none. Confirmed by a sorted-key JSON diff (`diff -u` of
`python3 -m json.tool --sort-keys` on both files) which contains only `+` lines for content.

**Unchanged:** README block (byte-identical between the two renders), all 5 records and all their
fields (`UserDetails` 2, `CredentialsConfig` 2, `FileUserStoreConfig` 0, `LdapUserStoreConfig` 20,
`SecureSocket` 1), and `extractUsernameAndPassword`.

## 3. Correctness against library source

The bala module sources are byte-identical to the GitHub `v2.14.0` tag — a per-file `diff -q` of all
8 `.bal` files under `.../modules/auth/` against `ballerina/` in the clone produced no output. So
citations below are valid for both.

Every one of the 11 additions verified (library-is-small, so this is exhaustive, not a spot-check):

| Render (new) | Source | Verdict |
|---|---|---|
| `type Error error;` | `auth_errors.bal:22` `public type Error distinct error;` | correct base type; `distinct` dropped (§5.1) |
| `class ClientBasicAuthProvider` | `client_basic_auth_provider.bal:35` `public isolated class ClientBasicAuthProvider` | correct |
| `init(CredentialsConfig credentialsConfig) returns ()` | `client_basic_auth_provider.bal:42` `public isolated function init(CredentialsConfig credentialsConfig)` | correct (nil return is accurate) |
| `generateToken() returns string\|Error` | `client_basic_auth_provider.bal:52` | exact match |
| `class ListenerFileUserStoreBasicAuthProvider` | `listener_file_user_store_basic_auth_provider.bal:44` | correct |
| `init(FileUserStoreConfig fileUserStoreConfig = {}) returns ()` | `listener_file_user_store_basic_auth_provider.bal:51` `init(FileUserStoreConfig fileUserStoreConfig = {})` | exact match, default `{}` preserved |
| `authenticate(string credential) returns UserDetails\|Error` | `listener_file_user_store_basic_auth_provider.bal:62` | exact match |
| `class ListenerLdapUserStoreBasicAuthProvider` | `listener_ldap_user_store_basic_auth_provider.bal:87` | correct |
| `init(LdapUserStoreConfig ldapUserStoreConfig) returns ()` | `listener_ldap_user_store_basic_auth_provider.bal:97` | correct |
| `authenticate(string credential) returns UserDetails\|Error` | `listener_ldap_user_store_basic_auth_provider.bal:114` | exact match |
| `ListenerBasicAuthProvider.authenticate(string credential) returns UserDetails\|Error` | `listener_basic_auth_provider.bal:27` | exact match |

Doc text spot-checks: the `Error` doc in `new` (render lines 49–51) reproduces
`auth_errors.bal:19–21` verbatim across all three lines. The `generateToken` doc block (render
lines 139–143) reproduces `client_basic_auth_provider.bal:46–50` including the fenced snippet.

Carried-over content also verified: `LdapUserStoreConfig` has 20 fields in the render and 20 in
`listener_ldap_user_store_basic_auth_provider.bal:42–63`, with field names and types matching in
order; `extractUsernameAndPassword(string credential) returns [string, string]|Error` matches
`auth_utils.bal:27`; `SecureSocket.cert` is `crypto:TrustStore|string`, matching
`listener_ldap_user_store_basic_auth_provider.bal:69`.

The README block in the render is the bala's `docs/README.md` verbatim — `diff` of
`docs/README.md` against render lines 8–34 reports only `26a27 > ` (one trailing blank line).

## 4. Regressions

**None found.**

What was checked to conclude this:

- Sorted-key JSON diff old→new contains no removed content lines — only `baseType`, one `functions`
  array, and three `type: "Class"` values added.
- Declaration set: old's 7 top-level declarations all appear in new with identical text; the
  mechanical diff reports 0 declarations removed, which I confirmed by extracting and comparing the
  `grep -nE '^(type|class|function|...)'` sets from both files.
- README section: byte-identical between old and new (`diff` of the extracted README blocks →
  no differences).
- Record fields: no field, type, optionality marker, or field doc changed in any of the 5 records —
  the unified diff has no hunks touching record bodies other than line renumbering.
- The three `// Unknown type:` removals are replacements by correct definitions, not deletions.
- No malformed or truncated output introduced: new's only structural additions are well-formed
  class bodies (see §5.4 for the one syntactic nit, which is a rendering convention, not a loss).

## 5. Issues in `new` (independent of `old`)

New-only (visible only because `new` now renders these constructs):

1. **`distinct` dropped from `Error`.** Render: `type Error error;`. Source `auth_errors.bal:22`:
   `public type Error distinct error;`. The JSON carries only `baseType: "error"`, so the loss is at
   extraction. Impact is low but real: an LLM cannot tell that `auth:Error` is a distinct error type
   (relevant when narrowing `error` unions in `http`/`websocket` code that imports `auth`).
2. **Class descriptions are the initializer's doc, not the class doc.** `new` line 134 renders
   `ClientBasicAuthProvider` with "Provides authentication based on the provided Basic Auth
   configurations." — that is the `init` doc at `client_basic_auth_provider.bal:39`. The actual class
   doc (`client_basic_auth_provider.bal:26–34`, "Represents the client Basic Auth provider … `new(config)`"
   with its usage snippet) is absent. Same for `ListenerFileUserStoreBasicAuthProvider`
   ("Provides authentication based on the provided configurations." = `init` doc line 48; real class
   doc lines 30–43 with the `Config.toml` snippet lost) and `ListenerLdapUserStoreBasicAuthProvider`
   ("Creates an LDAP auth store with the provided configurations." = `init` doc line 94; real class
   doc lines 76–86 with the `auth:LdapUserStoreConfig` usage snippet lost). The wrong description is
   present in the **old JSON too** — `old` simply never printed it. The construction usage snippets
   that would tell an LLM how to instantiate these providers are therefore missing from both renders.
3. **Method parameter and return docs are dropped inside class bodies.** The JSON for every class
   method carries `parameters[].description` and `return.description` (e.g. `credential` →
   "The Base64-encoded `username:password` value", return → "`auth:UserDetails` if the authentication
   is successful …"), but the render emits only a bare `# ` line after the summary. Contrast the
   module-level `extractUsernameAndPassword` (render lines 180–181), which does get
   `# + credential - …` and `# + return - …`. Information present in the JSON is discarded by the
   renderer for class members.
4. **Bodyless method declarations inside `class`.** `class ListenerBasicAuthProvider { function
   authenticate(...) returns UserDetails|Error; }` is not valid Ballerina — a `class` method needs a
   body, and the source construct is `public type ListenerBasicAuthProvider object { … };`
   (`listener_basic_auth_provider.bal:21`). The `class` keyword for this object type is in `old` too;
   the bodyless member is new. This matches the render's global stub convention (the module-level
   function is bodyless as well), so it is a convention artefact rather than a data loss, but the
   render is not compilable as written and the object-vs-class distinction is lost.

Shared with `old` (inaccurate in `new` regardless):

5. **Closed records rendered as open.** All 5 records are `record {| … |}` in source
   (`auth_commons.bal:21`, `client_basic_auth_provider.bal:21`,
   `listener_file_user_store_basic_auth_provider.bal:26`,
   `listener_ldap_user_store_basic_auth_provider.bal:42` and `:68`) but render as `record { … }`.
   This wrongly suggests extra fields are permitted.
6. **`LdapUserStoreConfig` defaults lost and required fields marked optional.** Source lines 58–61
   declare `userRolesCacheEnabled = false`, `connectionPoolingEnabled = true`,
   `connectionTimeout = 5`, `readTimeout = 60` — fields with defaults, not optional fields. Both
   renders emit `boolean userRolesCacheEnabled?;` etc. (old lines 108/110/112/114, new lines
   115/117/119/121) with no default. The JSON has `"optional": true` and no `defaultValue` key on
   both sides, so this is an extraction-level loss identical in old and new.
7. **`crypto:TrustStore` referenced without an import.** `SecureSocket.cert` is
   `crypto:TrustStore|string` in both renders, but the render preamble imports only
   `ballerina/auth`. The renderer compensates with an inline `// Special Agent Note: TrustStore FROM
   ballerina/crypto package` comment (old line 124 / new line 131), so the information is present,
   just not as a real import.
8. **`public` and `isolated` qualifiers dropped everywhere.** All 11 public symbols are declared
   `public` (9 also `isolated`) in source; neither render emits either qualifier. Consistent across
   both sides and evidently a global renderer convention.

## 6. Coverage gaps vs. the library

**Zero gaps.** `package.json` lists `"export": ["auth"]` and Central reports a single module
`auth`, so the default module *is* the whole public API — the known `getDefaultModule()` submodule
limitation does not apply here.

Public symbols in the default module (`grep -nE '^public (isolated )?(type|class|function|const|enum|annotation|listener)' modules/auth/*.bal` → 11 hits) versus the renders:

| Symbol | source | in `old` | in `new` |
|---|---|---|---|
| `UserDetails` | `auth_commons.bal:21` | yes | yes |
| `Error` | `auth_errors.bal:22` | placeholder only | yes |
| `extractUsernameAndPassword` | `auth_utils.bal:27` | yes | yes |
| `CredentialsConfig` | `client_basic_auth_provider.bal:21` | yes | yes |
| `ClientBasicAuthProvider` | `client_basic_auth_provider.bal:35` | placeholder only | yes |
| `ListenerBasicAuthProvider` | `listener_basic_auth_provider.bal:21` | yes (empty body) | yes (with method) |
| `FileUserStoreConfig` | `listener_file_user_store_basic_auth_provider.bal:26` | yes | yes |
| `ListenerFileUserStoreBasicAuthProvider` | `listener_file_user_store_basic_auth_provider.bal:44` | placeholder only | yes |
| `LdapUserStoreConfig` | `listener_ldap_user_store_basic_auth_provider.bal:42` | yes | yes |
| `SecureSocket` | `listener_ldap_user_store_basic_auth_provider.bal:68` | yes | yes |
| `ListenerLdapUserStoreBasicAuthProvider` | `listener_ldap_user_store_basic_auth_provider.bal:87` | placeholder only | yes |

Correctly excluded from both renders (non-public): `AuthInfo`, `LdapConnection`, the `users`
configurable table, `prepareError`, `checkPasswordEquality`, `init`/`setModule`, and the three
external LDAP `@java:Method` functions.

One item worth flagging as an API-surface gap that is *not* a symbol: the module-level
`configurable table<AuthInfo> key(username) & readonly users`
(`listener_file_user_store_basic_auth_provider.bal:23`) is how the file user store is actually
populated. It is not `public`, so its omission from the render is correct — and the README block
does document the `[[ballerina.auth.users]]` TOML section, so the information survives.

## 7. Compiler plugin

**No compiler plugin.** Confirmed three ways:

- Bala root listing contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json`, `platform/` — no `compiler-plugin/` directory and no
  `compiler-plugin.json` (`ls .../2.14.0/java21 | grep -i plugin` → no match).
- The upstream clone at `v2.14.0` has no `*compiler-plugin*` directory
  (`find . -maxdepth 2 -type d -name '*compiler-plugin*'` → no output). The only native component is
  `native/`, which builds `auth-native-2.14.0.jar` (the LDAP/`ModuleUtils` externals) —
  runtime code, not a compiler plugin.
- Manifest `has_plugin: false`.

Consequently there are no plugin-contributed code actions, validations, generated artifacts, or
annotations that ought to appear in the render. `annotations` is `[]` in both JSONs, correctly.

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerina/auth/2.14.0` returns `deprecated: null`,
  `deprecateMessage: ""`. Stable 2.x version; built with `ballerinaVersion: 2201.12.0`, consumed here
  from distribution 2201.13.4. Pull count 18,266.
- **Size/tokens:** trivial — 182 lines. The +40 lines buy 7 previously invisible method signatures,
  an excellent ratio.
- **Practical impact of the fix:** `old` was actively harmful for this library. All three usable
  provider classes and the module's error type were placeholders, so an LLM reading `old` could see
  `auth:CredentialsConfig` but had no way to know `ClientBasicAuthProvider` exists as a class with
  `generateToken()`, nor that `auth:Error` is an error type. `new` makes the module usable.
- **`FileUserStoreConfig` renders as an empty record**, which is faithful — the source record is
  intentionally blank (`listener_file_user_store_basic_auth_provider.bal:26–28`).
- **Downstream-type note (per the addendum):** `auth:Error` and `auth:UserDetails` are the types
  other packages (`http`, `websocket`, `grpc`, `graphql`) depend on. `UserDetails` is rendered
  accurately on both sides. `auth:Error` is rendered only in `new`, and there without `distinct`
  (§5.1) — still a large net improvement over `old`'s placeholder.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l auth/{old,new}/ballerina_auth.bal.txt` | 142 / 182 |
| `wc -l auth/{old,new}/ballerina_auth.json` | 451 / 487 |
| `grep -c '^// Unknown type:'` old / new | 4 / 0 |
| `grep -c '^// --- '` old / new | 4 / 4 |
| `grep -cE ':[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 0 / 0 |
| `grep -nE '^(type\|class\|function\|enum\|const\|annotation\|service\|listener)'` | old 7 decls, new 11 decls |
| `grep -nE '^    (function\|resource\|remote)'` | old 0 members, new 7 members |
| `diff -u <(json.tool --sort-keys old) <(json.tool --sort-keys new)` | 3 additions (`baseType`, `functions` on `ListenerBasicAuthProvider`, `type:"Class"` ×3); zero removals |
| JSON top-level counts both sides | `clients` 0, `functions` 1, `services` 0, `annotations` 0, `typeDefs` 10 |
| `git clone --depth 1 --branch v2.14.0 …` | succeeded; HEAD `252ad7ea5daa9488a08694738c462cb0f3790b16`, tag `v2.14.0` |
| `grep -n version src/ballerina/Ballerina.toml` | `version = "2.14.0"` (lines 4, 18) — pin confirmed |
| per-file `diff -q` bala `modules/auth/*.bal` vs clone `ballerina/*.bal` (8 files) | no differences — bala == GitHub tag |
| `ls .../2.14.0/java21` | `bala.json docs modules package.json platform dependency-graph.json`; no `compiler-plugin/` |
| `find src -maxdepth 2 -type d -name '*compiler-plugin*'` | no output |
| `package.json` `export` | `["auth"]` — single module |
| `curl api.central.ballerina.io/.../ballerina/auth/2.14.0` | 1 module, `deprecated: null`, `ballerinaVersion 2201.12.0` |
| `grep -nE '^public …' modules/auth/*.bal` | 11 public symbols; all 11 in `new` render |
| `diff docs/README.md <(sed -n '8,34p' new render)` | only `26a27 > ` (trailing blank) |
| `diff` of README blocks old vs new | identical |
| `LdapUserStoreConfig` field count: render vs source | 20 vs 20 |
| `grep -nE '= (false\|true\|5\|60);'` source lines 58–61 vs render lines 115/117/119/121 | 4 defaults present in source, absent + marked `?` in both renders |
| JSON field objects for `userRolesCacheEnabled`/`connectionTimeout` | `"optional": true`, no `defaultValue`, identical old and new |
| JSON `ClientBasicAuthProvider.description` vs `client_basic_auth_provider.bal:26–34` / `:39` | matches the `init` doc, not the class doc |
| JSON class-method `parameters[].description` present vs render output | present in JSON, absent from rendered class bodies |

## 10. Caveats and unverified items

- The class-description issue (§5.2) is reported as an extractor behaviour because the same wrong
  description is in the `old` JSON. I did not read the `CopilotLibraryManager` Java source to
  confirm the rule is "class description := initializer description"; the inference is from the data
  (`ClientBasicAuthProvider.description` byte-equals its `init.description` in both JSONs). Stated as
  observation, not as a claim about the implementation.
- Whether §5.3 (param/return docs dropped for class members) is intended renderer behaviour or an
  oversight is not verified — I did not read `to-syntax-string.ts`. The observable fact is that the
  data exists in the JSON and does not appear in the render.
- The renders themselves were taken as given and not regenerated, so I cannot independently confirm
  which `ballerina-vscode` commit produced each file beyond what the brief states.
- Everything else in this report comes from commands run against the bala, the v2.14.0 clone,
  Central, and the two render/JSON pairs.

# ballerinax/cdc 1.4.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/cdc` |
| Pinned version | `1.4.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-cdc |
| Tag reviewed | `v1.4.0` (commit `f40f99ab7dd37ea5df95ab734303ae206077fd4c`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/cdc/1.4.0/java21` |
| Old render | `1310` lines |
| New render | `1339` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly additive over `old` for this library. The mechanical diff is 8 removed lines and
37 added lines; every removed line is either a degraded `// Unknown type:` placeholder or a
version/module-qualified type reference, and each is replaced by a better rendering. Nothing that was
correct in `old` is missing, truncated, or mangled in `new`.

Concretely `new` gains: 4 real error type definitions (previously `// Unknown type:` stubs), the 5
`Listener` object methods (previously an empty `class Listener {}`), a new `// --- Annotations ---`
section carrying `cdc:ServiceConfig` (the annotation this module's compiler plugin is built around),
and clean unqualified type references in `KafkaSecureSocket`, `InternalSchemaStorage`, and
`OffsetStorage`.

The JSON side confirms this: `typeDefs` count is identical (127 → 127), `functions` are
byte-identical (34, `json.dumps(..., sort_keys=True)` equal), `readme` is identical (4934 chars),
`clients`/`services` are empty on both, and `annotations` goes 0 → 1.

Zero regressions. Zero coverage gaps against the default module. Seven accuracy issues remain in
`new`, four of which are shared with `old` (they are renderer-wide fidelity limits, not spec-v2
defects).

## 2. Change inventory

Line counts (`wc -l`): old 1310, new 1339 (+29 net).
Raw diff: 8 lines only in `old`, 37 lines only in `new`.

### Section markers
| section | old | new |
|---|---|---|
| `// --- README ---` | line 7 | line 7 |
| `// --- END README ---` | line 104 | line 104 |
| `// --- Types ---` | line 106 | line 106 |
| `// --- Functions ---` | line 1090 | line 1114 |
| `// --- Annotations ---` | *absent* | line 1336 |

### Top-level declaration set (extracted names, `sort`ed, `diff`ed)
old 157 declarations → new 162. Nothing removed. Added, all 5:

| kind | name | evidence |
|---|---|---|
| type | `Error` | new:240–241 |
| type | `EventProcessingError` | new:243–244 |
| type | `PayloadBindingError` | new:246–247 |
| type | `OperationNotPermittedError` | new:249–250 |
| annotation | `ServiceConfig` (`CdcServiceConfig` on `service`) | new:1336–1339 |

### Degraded types
`grep -c '^// Unknown type:'` — old **4**, new **0**. The four are exactly the error types above.

### Class members
`class Listener` gained 5 methods in `new` (`attach`, `'start`, `detach`, `gracefulStop`,
`immediateStop`), new:253–272. `old` had `class Listener {\n}` (old:249–250).
`class Service` is an empty body in both (old:275–276, new:299–300) — see §5.

### Type-reference normalisation (3 lines, `old` → `new`)
- `record {|ballerina/crypto:2.12.1:KeyStore keyStore; …|}` → `record {|crypto:KeyStore keyStore; …|}`
- `record {|ballerinax/cdc:1.4.0:KafkaSecureSocketProtocol name; …|}` → `record {|KafkaSecureSocketProtocol name; …|}`
- `type InternalSchemaStorage ballerinax/cdc:1.4.0:File… | …` (8 members) → unqualified 8 members
- `type OffsetStorage ballerinax/cdc:1.4.0:File… | …` (5 members) → unqualified 5 members

### Unchanged
- functions: 34 on both, JSON-identical.
- README block: identical, 4934 chars, `o['readme']==n['readme']` → `True`.
- package description: identical.
- `clients`: 0 on both. `services`: 0 on both.

## 3. Correctness against library source

Upstream `v1.4.0` `ballerina/` sources are byte-identical to the bala's `modules/cdc/*.bal`
(`diff -r src/ballerina <bala>/modules/cdc --brief` reports only extra build files in the clone —
`Ballerina.toml`, `CompilerPlugin.toml`, `Dependencies.toml`, `README.md`, `build.gradle`, `tests`;
no differing `.bal`). `gradle.properties: version=1.4.0`; bala `package.json` →
`{organization: ballerinax, name: cdc, version: 1.4.0, ballerina_version: 2201.12.0}`. Version pin
confirmed on both sides.

### The 4 newly emitted error types (`modules/cdc/errors.bal`)

| source | new render | assessment |
|---|---|---|
| `errors.bal:25` `public type Error distinct error;` | `type Error error;` | correct base, `distinct` dropped |
| `errors.bal:28` `public type EventProcessingError distinct (Error & error<EventProcessingErrorDetail>);` | `type EventProcessingError error<record {|json payload; anydata...;|}>;` | structurally correct — `EventProcessingErrorDetail` (`errors.bal:20–22`) is an open record with a single `json payload` field, so `record {|json payload; anydata...;|}` is its accurate expansion; the `Error &` intersection and `distinct` are dropped |
| `errors.bal:31` `public type PayloadBindingError distinct EventProcessingError;` | `type PayloadBindingError error<record {|json payload; anydata...;|}>;` | expansion correct; the "is a subtype of `EventProcessingError`" relation is lost |
| `errors.bal:34` `public type OperationNotPermittedError distinct Error;` | `type OperationNotPermittedError error;` | expansion correct; subtype relation to `Error` lost |

No invented members. The docs on all four match the source doc comments verbatim.

### The 5 newly emitted `Listener` methods (`modules/cdc/listener.bal:18–47`)

| source | new render |
|---|---|
| `:25` `public isolated function attach(Service s, string[]|string? name = ()) returns Error?;` | `function attach(Service s, string[]|string|() name = ()) returns Error|();` |
| `:30` `public isolated function 'start() returns Error?;` | `function 'start() returns Error|();` |
| `:36` `public isolated function detach(Service s) returns Error?;` | `function detach(Service s) returns Error|();` |
| `:41` `public isolated function gracefulStop() returns Error?;` | `function gracefulStop() returns Error|();` |
| `:46` `public isolated function immediateStop() returns Error?;` | `function immediateStop() returns Error|();` |

Names, arity, parameter types, parameter default (`()`), and return types all match. `string[]|string?`
→ `string[]|string|()` and `Error?` → `Error|()` are equivalent desugarings, both valid Ballerina.
`public`/`isolated` qualifiers are dropped (§5). The 5-method set is complete and no method is invented.

### The new annotation (`modules/cdc/annotations.bal:25`)

Source: `public annotation CdcServiceConfig ServiceConfig on service;`
Render (new:1339): `public annotation CdcServiceConfig ServiceConfig on service;` — exact match.
Its constraint record `CdcServiceConfig` (`annotations.bal:20–22`, `string|string[] tables`) was
already rendered as a type in both sides.

### Type-reference normalisation
`types.bal:184–196` `KafkaSecureSocket` uses `crypto:KeyStore` and same-module
`KafkaSecureSocketProtocol`. `new`'s `crypto:KeyStore` / bare `KafkaSecureSocketProtocol` match the
source prefixing; `old`'s `ballerina/crypto:2.12.1:KeyStore` / `ballerinax/cdc:1.4.0:…` are not valid
Ballerina type syntax. `InternalSchemaStorage` and `OffsetStorage` members likewise resolve to
same-module types, so unqualified is correct.

### Spot-check of unchanged content
`externStart` (`extern_functions.bal:48–50`) carries `# Use externStartWithExtendedConfigs instead.`
+ `@deprecated`; both renders keep the `@deprecated` marker (old:1116 region, new:1140 region).
`SecureDatabaseConnection` (`types.bal:203–206`) fields `sslMode`/`keyStore`/`trustStore` match both
renders (new:468–475).

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff old new | grep '^<'` returns exactly 8 lines. All 8 are enumerated in §2: 4 `// Unknown type:`
  placeholders (replaced by real definitions) and 4 lines carrying `org/mod:version:Type` qualifiers
  (replaced by valid unqualified/prefixed refs). None represents lost information.
- Declaration-name set diff (`comm` on sorted extracted names): 0 removals, 5 additions.
- JSON `typeDefs` name set: `set(old)==set(new)` → `True`; only 8 entries differ and every one of the
  8 is a superset or a cleanup (`Error`, `EventProcessingError`, `PayloadBindingError`,
  `OperationNotPermittedError` gain `baseType`; `Listener` gains `functions`; `KafkaSecureSocket`,
  `InternalSchemaStorage`, `OffsetStorage` lose version qualifiers from type-name strings).
- JSON `functions` arrays are identical under canonical serialisation → no parameter, default, return
  type, or doc was dropped from the 34 module functions.
- `readme` string identical on both sides → no README/section content lost.
- Public-symbol coverage (103 symbols): missing from `old` = 0, missing from `new` = 0.
- Malformed-syntax lines (`^of the JVM` etc.): identical set and count on both sides — see §5,
  pre-existing, not introduced.

## 5. Issues in `new` (independent of `old`)

Three are `new`-side only; four are shared with `old` (marked *shared*) and are renderer-wide limits.

1. **Method doc parameters and return docs are dropped by the renderer.** The new JSON for
   `Listener.attach` carries `parameters[0].description = "The CDC service to attach"`,
   `parameters[1].description = "Attachment points"` and a return description, but the render emits
   only the summary followed by a bare `# ` line (new:254–256). All 5 methods lose their `+ param -`
   and `+ return -` docs. Module-level functions in the `// --- Functions ---` section *do* keep
   these (e.g. new:1117–1120), so this is inconsistent within the same file.
2. **`public` / `isolated` qualifiers dropped on the 5 `Listener` methods.** Source
   (`listener.bal:25,30,36,41,46`) declares all as `public isolated function`; render emits bare
   `function`. Renders as non-public API to a consuming LLM.
3. **`distinct` and error subtype relations are flattened.** `PayloadBindingError` and
   `EventProcessingError` render as the *same* type descriptor
   (`error<record {|json payload; anydata...;|}>`), so the render cannot express that the former is a
   distinct subtype of the latter, nor that all four are distinct from plain `error`. Code that does
   `if e is cdc:PayloadBindingError` is not derivable from the render. Still a large net improvement
   over `old`'s four bare `// Unknown type:` lines.
4. *shared* **Record field default values are dropped.** `types.bal` declares 88 fields with
   defaults; `grep -cE '^\s+[A-Za-z_].* = .*;'` gives 0 in `old` and 1 in `new` (the one hit in `new`
   is the `attach` *parameter* default, not a field). Example: `types.bal:204`
   `SslMode sslMode = PREFERRED;` renders as `SslMode sslMode?;` (old:447, new:471) — a field with a
   default is rendered as an optional field with no default, which is both a lost value and a wrong
   optionality signal.
5. *shared* **Closed records are rendered as open.** 39 of the 46 public records are `record {|…|}`
   in the bala; `grep -cE '^type [A-Za-z0-9_]+ record \{\|'` in `new` = 0, all 46 render as
   `record {`. Inline/nested records keep `{| |}`, so the loss is only at top level.
6. *shared* **5 malformed doc-continuation lines produce non-comment bare text**, making the render
   non-compiling Ballerina. Identical line content and count on both sides (old 384/438/793/1112/1141,
   new 408/462/817/1136/1165), e.g. `of the JVM` at new:462 and
   `listener-specific properties into distinct maps.` at new:1136, both of which are wrapped
   continuation lines of a `#` doc comment emitted without the leading `#`.
7. *shared* **`Service` renders as an empty `class Service {}`** (old:275, new:299). That matches the
   bala literally (`service.bal:44–46` is an empty `distinct service object`), but the actual contract
   — the `onRead`/`onCreate`/`onUpdate`/`onDelete`/`onError`/`onTruncate` remote methods — is enforced
   by the compiler plugin, not the type. The doc-comment example inside the render mentions four of
   them; `onTruncate` appears **0** times in either render (`grep -c 'onTruncate'` = 0/0) even though
   the plugin accepts it for PostgreSQL. See §7.

Also note both renders declare `Listener` as `class`, while the source is
`public type Listener isolated object {…}` (`listener.bal:18`). Shared, cosmetic, and the emitted
member list is correct.

## 6. Coverage gaps vs. the library

**0 gaps.**

- The bala's default module is the only module: `ls <bala>/java21/modules/` → `cdc` alone. There is no
  submodule-only API, so the `getDefaultModule()` limitation described in the brief does not apply
  here.
- 103 distinct public symbols extracted from `modules/cdc/*.bal`
  (`grep -hoE '^public (isolated )?(type|function|class|enum|const|annotation) [A-Za-z0-9_']+'`,
  `sort -u`). Every one appears in `new` and every one appears in `old` (loop-checked with a
  word-boundary grep per name; 0 misses on either side).
- Rendered top-level declaration names in `new` = 104 = the 103 public symbols + the token `string`,
  which is an artefact of my extraction regex matching `const string NAME = …` lines, not an extra
  declaration. `comm -13` (public but not rendered) is empty.
- `EventProcessingErrorDetail`, `CdcServiceConfig`, all 8 `*InternalSchemaStorage` / 5 `*OffsetStorage`
  variants, all 8 `public isolated function extern*` / `isLive` / `externGetAdditionalConfigKeys`, and
  all public constants and enums are present.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` → `plugin_id: cdc-compiler-plugin`,
`plugin_class: io.ballerina.lib.cdc.compiler.CdcCompilerPlugin`, jar `cdc-compiler-plugin-1.4.0.jar`.
Upstream `compiler-plugin/src/main/java/**` has 18 classes: a code analyzer, service/function
validators, a completion provider (`CdcServiceBodyContextProvider`), and 7 code-action classes
(`CdcCodeTemplate`, `CdcCodeTemplateWithTableName`, `ChangeToRemoteMethod`,
`ChangeReturnTypeToCdcError`, `ChangeReturnTypeToError`, …).

Diagnostics (`DiagnosticCodes.java:26–37`): `CDC_101` missing valid remote function, `CDC_102`
resource functions not allowed, `CDC_103` must be `remote`, `CDC_104` invalid parameter count,
`CDC_105` must be a required parameter, `CDC_106` invalid parameter type, `CDC_107` params must be of
the same type, `CDC_108` return must be `error?`/`cdc:Error?`, `CDC_109` one `cdc:Listener` only, plus
internal `CDC_601`/`CDC_602` (empty-service templates, the latter PostgreSQL-specific).

`Constants.java:32–54` defines the accepted service methods: `onRead`, `onCreate`, `onUpdate`,
`onDelete`, `onError`, and `onTruncate` (PostgreSQL only —
`VALID_FUNCTIONS_NON_POSTGRES` omits it).

What the plugin implies vs. what the render carries:
- **Now present in `new`, absent in `old`:** `@cdc:ServiceConfig { tables: … }`. The plugin's whole
  service model is keyed on this annotation, so `old` omitting the entire `Annotations` section was a
  real hole. This is the single most valuable addition in `new` for this library.
- **Still absent in both:** the remote-method contract itself. `class Service {}` conveys no
  signatures; `onTruncate` is never mentioned anywhere in either render; the `error?`/`cdc:Error?`
  return requirement (`CDC_108`) and the one-listener rule (`CDC_109`) are only implicit. A consumer
  LLM must rely on the doc-comment example embedded in the `Service` doc block (which covers
  `onRead`/`onCreate`/`onUpdate`/`onDelete` only) and on the README.

## 8. Other considerations

- **Version stability.** Both sides pinned at 1.4.0, verified against the bala `package.json` and the
  upstream `gradle.properties`. A stable 1.x release; no deprecation on the package itself.
- **Deprecated API surfaced.** `externStart` is `@deprecated` in favour of
  `externStartWithExtendedConfigs` (`extern_functions.bal:48–50`); both renders carry the
  `@deprecated` marker, though the accompanying "use X instead" sentence is one of the malformed
  non-comment lines from §5.6.
- **The `extern*` functions are public but are implementation plumbing.** All 8 are `@java:Method`
  externals intended for the concrete listeners in `ballerinax/mysql`, `ballerinax/postgresql`,
  `ballerinax/mssql`. They occupy ~90 of the ~225 lines of the Functions section on both sides, and a
  consuming LLM could plausibly be misled into calling them directly. Unchanged between sides; not a
  regression, but worth knowing.
- **This module is not usable standalone.** `cdc:Listener` is an abstract object type; users
  instantiate `mysql:CdcListener` / `postgresql:CdcListener`. Neither render can convey that beyond
  the README example (`service on mysqlListener`, new:56).
- **Size/token impact.** +29 lines (+2.2%), negligible. The information density improves materially:
  4 dead placeholder lines become 8 lines of real type definitions, and an empty class body becomes 5
  correct method signatures.

## 9. Evidence log

| # | check | result |
|---|---|---|
| 1 | `wc -l old/ballerinax_cdc.bal.txt new/ballerinax_cdc.bal.txt` | 1310 / 1339 |
| 2 | `grep -c '^// Unknown type:'` old / new | 4 / 0 |
| 3 | `grep -n '^// --- '` old / new | old: 7,104,106,1090 · new: 7,104,106,1114,1336 |
| 4 | `diff -u old new` (full) | 8 `<` lines, 37 `>` lines; hunks at 237, 429, 1064, 1308 |
| 5 | `diff old new \| grep '^<'` | 4 `// Unknown type:` + 4 version-qualified type lines (listed in §4) |
| 6 | declaration-name sets via `grep -oE '^(public )?(isolated )?(type\|function\|class\|enum\|const\|annotation) …' \| sort` then `diff` | 157 → 162; additions only: `annotation CdcServiceConfig`, `type Error`, `type EventProcessingError`, `type OperationNotPermittedError`, `type PayloadBindingError`; 0 removals |
| 7 | JSON top-level keys both sides | identical 8 keys |
| 8 | JSON array lengths old→new | typeDefs 127→127, functions 34→34, clients 0→0, services 0→0, annotations 0→1 |
| 9 | JSON typeDef name sets | `set(old)==set(new)` → True |
| 10 | JSON typeDefs differing entries | 8: Error, EventProcessingError, PayloadBindingError, OperationNotPermittedError (+`baseType`), Listener (+`functions`), KafkaSecureSocket / InternalSchemaStorage / OffsetStorage (qualifier removal) |
| 11 | JSON `functions` canonical compare | identical |
| 12 | JSON `readme` compare | identical, 4934 chars both |
| 13 | JSON `description` compare | identical |
| 14 | JSON `annotations` in new | `ServiceConfig`, attachmentPoint `SERVICE`, typeConstraint `CdcServiceConfig` |
| 15 | `git ls-remote --tags module-ballerinax-cdc` | `v1.4.0` present → `f40f99ab7dd37ea5df95ab734303ae206077fd4c` |
| 16 | `git clone --depth 1 --branch v1.4.0` | success |
| 17 | `diff -r src/ballerina <bala>/modules/cdc --brief` | no differing `.bal`; only build files extra in clone |
| 18 | `src/gradle.properties` | `version=1.4.0` |
| 19 | bala `package.json` | ballerinax/cdc 1.4.0, ballerina_version 2201.12.0 |
| 20 | `ls <bala>/java21/modules/` | `cdc` only — no submodules |
| 21 | `errors.bal:20–34` read | 4 error types + `EventProcessingErrorDetail`; confirms §3 table |
| 22 | `listener.bal:18–47` read | 5 `public isolated function` members; confirms §3 table |
| 23 | `service.bal:44–46` read | `public type Service distinct service object {}` — genuinely empty |
| 24 | `annotations.bal:20–25` read | `CdcServiceConfig` record + `ServiceConfig` annotation; exact match to new:1336–1339 |
| 25 | `types.bal:184–196` read | `KafkaSecureSocket` closed record with `crypto:KeyStore` and `KafkaSecureSocketProtocol`; confirms new's prefixes correct |
| 26 | public-symbol extraction `sort -u` | 103 symbols |
| 27 | per-symbol grep against `old` | 0 missing |
| 28 | per-symbol grep against `new` | 0 missing |
| 29 | `comm -23 rendered public` (new) | only `string` (regex artefact from `const string X =` lines) |
| 30 | `comm -13 rendered public` | empty — no public symbol unrendered |
| 31 | `grep -nE '^\s+[A-Za-z_].* = .*;'` old / new | 0 / 1 (the `attach` param default) vs 88 field defaults in `types.bal` |
| 32 | `grep -cE '^public type … record \{\|'` bala | 39 closed, 7 open |
| 33 | `grep -cE '^type … record \{\|'` new | 0 (all 46 rendered open) |
| 34 | `grep -n '^of the JVM'` old / new | 438 / 462 — present on both |
| 35 | non-comment continuation lines heuristic | identical 5 non-README hits per side (old 384,438,793,1112,1141 · new 408,462,817,1136,1165) |
| 36 | `grep -c 'onTruncate'` old / new | 0 / 0 |
| 37 | `grep -c 'onError'` old / new | 1 / 1 (both inside the `Service` doc block) |
| 38 | `compiler-plugin/compiler-plugin.json` | cdc-compiler-plugin 1.4.0 |
| 39 | `find compiler-plugin -name '*.java'` | 18 classes (validators, completion provider, 7 code actions) |
| 40 | `DiagnosticCodes.java:26–37` | CDC_101–109, CDC_601–602 |
| 41 | `Constants.java:32–54` | valid methods incl. `onTruncate` (PostgreSQL-only) and `onError` |
| 42 | `extern_functions.bal:48–50` | `@deprecated externStart`; marker present in both renders |
| 43 | `sed -n '246,280p' old` / `'268,320p' new` | verified `Listener`/`Service` bodies quoted in §2 |
| 44 | `sed -n '1114,1160p' new` | Functions section head; param docs retained for module functions |

## 10. Caveats and unverified items

1. **Renders were not compiled.** I did not run `bal build` over either `.bal.txt`; the
   "non-compiling" claim in §5.6 rests on reading the emitted lines (bare non-comment prose inside a
   doc block), which is unambiguous, but no compiler confirmed it.
2. **The compiler-plugin jar was not decompiled.** Plugin behaviour in §7 is read from the upstream
   `v1.4.0` Java sources, which I verified match the tag but did not verify byte-for-byte against
   `compiler-plugin/libs/cdc-compiler-plugin-1.4.0.jar` in the bala.
3. **Ballerina Central metadata was not re-queried.** Version, module list, and org/name were
   confirmed from the bala `package.json` and the upstream tag instead; the central API was not hit,
   so any Central-only field (deprecation flag, keywords, pull count) is unverified.
4. **Coverage was checked by symbol name, not by full signature, for the 34 module functions.** Their
   JSON is identical between sides so no cross-side difference is possible; I spot-checked
   `externAttach`, `externDetach`, `externStart`, `externStartWithExtendedConfigs`,
   `externGracefulStop`, `externImmediateStop` against `extern_functions.bal` but did not
   line-by-line verify every one of the 34 against source.
5. **`old`'s renderer patch (`service.methods ?? []`)** is documented as affecting only
   `ballerina/mcp`; I did not independently verify it has no effect here, though `services` is an
   empty array in both JSONs, which makes any effect impossible.

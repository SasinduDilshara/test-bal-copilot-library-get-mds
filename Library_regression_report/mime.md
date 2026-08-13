# ballerina/mime 2.12.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/mime` |
| Pinned version | `2.12.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-mime |
| Tag reviewed | `v2.12.2` |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/mime/2.12.2/java21` |
| Old render | `210` lines |
| New render | `490` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` for this library. Lines 1–122 (header, import, README block, all
29 constants) are byte-identical, and the entire `// --- Functions ---` section (6 module-level
functions, 50 lines) is byte-identical. The only change is that the 19 `// Unknown type:` placeholder
lines in `old` are replaced by real definitions: 16 error type declarations and 3 class bodies
containing 34 methods.

Root cause confirmed at the JSON level: `old`'s JSON emits the three class typeDefs **without a
`"type"` field at all** (keys are only `name`, `description`, `functions`), so `main`'s
`renderTypeDef` switch falls through to `// Unknown type:`. `new` adds `"type": "Class"` and
`"baseType": "error"`, so both kinds render. The two JSONs differ in only 88 lines, all of them this
tagging plus removal of a synthetic `init` constructor and de-versioning of two `io:Error` refs.

Nothing present in `old` is missing, truncated or altered in `new`. Everything `new` adds was
verified against the bala source, which is byte-identical to the GitHub tag. Residual inaccuracies
in `new` (wrong class-method parameter defaults, flattened `distinct` error hierarchy, dropped
per-parameter doc lines, missing public class fields) all trace to the extractor or the class-body
renderer and are not regressions — `old` simply printed nothing there.

## 2. Change inventory

Counts from `grep -c` on both render files:

| Declaration kind | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 19 | 0 |
| `const string ...` | 29 | 29 |
| `type <X> error;` | 0 | 16 |
| `class <X> { ... }` | 0 | 3 |
| Class methods (`^    function `) | 0 | 34 |
| Module-level `function ...` | 6 | 6 |
| `// --- ` section markers | 4 | 4 |
| Version-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| Total lines | 210 | 490 |

**Added in `new` (52 declarations):**
- 16 error types: `Error`, `EncodeError`, `DecodeError`, `GenericMimeError`, `SetHeaderError`,
  `InvalidHeaderValueError`, `InvalidHeaderParamError`, `InvalidContentLengthError`,
  `HeaderNotFoundError`, `InvalidHeaderOperationError`, `SerializationError`, `ParserError`,
  `InvalidContentTypeError`, `HeaderUnavailableError`, `IdleTimeoutTriggeredError`, `NoContentError`
- 3 classes: `Entity` (31 methods), `MediaType` (2 methods), `ContentDisposition` (1 method)

**Removed in `new`:** the 19 `// Unknown type:` comment lines only. No declaration removed.

**Modified in `new`:** none. Verified byte-identical:
- `diff <(sed -n '1,123p' old) <(sed -n '1,122p' new)` → only the one blank line that preceded
  `// Unknown type: Error`.
- `diff <(sed -n '162,211p' old) <(sed -n '442,491p' new)` → identical.

**JSON-level delta** (`diff` of pretty-printed JSONs = 88 changed lines, no other differences):
1. 16 × `"baseType": "error"` added to error typeDefs.
2. 3 × `"type": "Class"` added to class typeDefs (absent in `old` — the placeholder cause).
3. 3 × synthetic `{"name":"init","type":"Constructor","parameters":[]}` entry removed (one per class).
   `Entity` 32→31, `MediaType` 3→2, `ContentDisposition` 2→1 function entries.
4. 2 × `stream<byte[], ballerina/io:1.8.1:Error?>|ParserError` → `stream<byte[], io:Error?>|ParserError`
   (`getByteStream`, `getBodyPartsAsStream`) — de-versioning improvement, invisible in `old`'s render
   because the class was never emitted.

Top-level JSON shape is otherwise unchanged on both sides: `typeDefs` 48, `functions` 6, `clients` 0,
`services` 0, `annotations` 0.

## 3. Correctness against library source

The bala module sources are byte-identical to the GitHub tag `v2.12.2` — `diff -q` returned SAME for
all six files (`natives.bal`, `mime_errors.bal`, `media_types.bal`, `byte_stream.bal`, `init.bal`,
`event_stream_writer.bal`). Checks below cite the bala paths.

**Error types (16/16 correct as to name and doc).** `mime_errors.bal:19–64` declares exactly the 16
public error types in the same order, with the same doc strings as rendered at new:124–170. Example:
`mime_errors.bal:19` `public type Error distinct error;` → new:125 `type Error error;`.

**`Entity` (31/31 methods verified).** `natives.bal:142` `public class Entity`. Every method in the
render exists with a matching name, parameter list and return type:
- `natives.bal:158 setContentType(string mediaType) returns InvalidContentTypeError?` → new:182
  `returns InvalidContentTypeError|()` (equivalent spelling).
- `natives.bal:269 setBody(string|xml|json|byte[]|Entity[]|stream<byte[], io:Error?>)` → new:239, same union.
- `natives.bal:451 getByteStream(int arraySize = 8192) returns stream<byte[], io:Error?>|ParserError`
  → new:329, correct types (default value wrong — §5).
- `natives.bal:468 getBodyParts() returns Entity[]|ParserError` → new:336.
- `natives.bal:523/540/556 getHeader/getHeaders/getHeaderNames` → new:359/366/373, correct
  `string|HeaderNotFoundError`, `string[]|HeaderNotFoundError`, `string[]`.
- Header mutators `addHeader`, `setHeader`, `removeHeader`, `removeAllHeaders`, `hasHeader`
  (`natives.bal:567/585/602/623/635` region) → new:380/388/395/401/408.
No invented methods: the render's 31 `Entity` methods map 1:1 onto the 31 `public isolated function`
declarations inside `public class Entity`.

**`MediaType` (2/2).** `natives.bal:87` `public class MediaType`; `:100 getBaseType() returns string`,
`:110 toString() returns string` → new:420, new:427.

**`ContentDisposition` (1/1).** `natives.bal:59` `public class ContentDisposition`; `:72 toString()
returns string` → new:439.

**Module functions (unchanged from `old`, re-verified).** `natives.bal:727 base64Encode(... string
charset = "utf-8")`, `:740 base64Decode`, `:750 base64EncodeBlob`, `:763 base64DecodeBlob`,
`:788 getMediaType`, `:800 getContentDispositionObject` — all six match new:451–490, including the
correct `charset = "utf-8"` default and the `io:ReadableByteChannel` external-link annotation.

**Constants (29/29).** 20 in `media_types.bal:18–75`, 9 in `natives.bal:22–50`; all present with
matching values in both renders.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Byte-level diff of the shared regions: header/README/constants (old 1–123 vs new 1–122) and the
  whole Functions section (old 162–211 vs new 442–491). Both identical apart from one blank line.
- Declaration-set comparison by kind (§2 table): every kind is equal or larger in `new`; nothing
  dropped.
- No parameter, default value, return type or doc line present in `old` is absent from `new` — the
  only `old` content not carried forward is the 19 `// Unknown type:` comment lines themselves, which
  carried no information.
- `grep -c '^// Unknown type:'` → old 19, new 0. `grep -cE 'mod:x.y.z:Type'` pattern → 0 on both.
- No malformed syntax introduced: the three class bodies are balanced (`class X {` … `}`), all method
  signatures terminate with `;`, and the file has no unterminated doc block.

## 5. Issues in `new` (independent of `old`)

These are inaccuracies visible in `new`. All of them concern the class bodies, which `old` never
emitted, so none is a regression — but each could mislead an LLM.

1. **Class-method default parameter values are wrong (9 parameters).** The render prints zero-values
   instead of the real defaults. Verified in the JSON: both `old` and `new` JSON carry
   `"default": "\"\""` / `"default": "0"`, so this is an **extractor** bug that predates spec v2 and
   only became visible now.
   | render | actual (`natives.bal`) |
   |---|---|
   | new:248 `setFileAsEntityBody(string filePath, string contentType = "")` | `:299` `= "application/octet-stream"` |
   | new:257 `setJson(json jsonContent, string contentType = "")` | `:314` `= "application/json"` |
   | new:273 `setXml(xml xmlContent, string contentType = "")` | `:338` `= "application/xml"` |
   | new:289 `setText(string textContent, string contentType = "")` | `:362` `= "text/plain"` |
   | new:305 `setByteArray(byte[] blobContent, string contentType = "")` | `:388` `= "application/octet-stream"` |
   | new:322 `setByteStream(..., string contentType = "")` | `:430` `= "application/octet-stream"` |
   | new:352 `setBodyParts(Entity[] bodyParts, string contentType = "")` | `:510` `= "multipart/form-data"` |
   | new:329 `getByteStream(int arraySize = 0)` | `:451` `= 8192` |
   | new:343 `getBodyPartsAsStream(int arraySize = 0)` | `:489` `= 8192` |
   Note the contrast: module-level `base64Encode`'s `charset = "utf-8"` **is** correct
   (new:451), so the defect is specific to the class-method extraction path. The doc text rendered
   above each method still states the true default ("The default size is 8KB"), so the render is
   self-contradictory.

2. **Error hierarchy flattened.** Source is `public type Error distinct error;` and 15 ×
   `public type <X> distinct Error;` (`mime_errors.bal:19–64`). `new` renders all 16 as
   `type <X> error;`, dropping `distinct` and the subtype relation to `Error`. A consumer reading the
   render cannot tell that `ParserError` is assignable to `mime:Error`, which is the whole point of
   the module's error model. The JSON's `"type": "Error", "baseType": "error"` does not encode the
   parent type either, so this is an extractor limitation.

3. **Per-parameter and return doc lines dropped for class methods.** `sed -n '175,440p' new | grep -c '# + '`
   → 0, versus 14 in the Functions section. The data is present in the JSON — e.g. `setContentType`
   carries `parameters[0].description` "Content type, which needs to be set to the entity" and
   `return.description` "`()` if successful or else an `mime:InvalidContentTypeError`…" — but the
   class-body renderer emits only the description block and a bare `# ` line. 34 methods are affected.

4. **Public class fields missing (8 fields).** `MediaType` declares `public string primaryType`,
   `subType`, `suffix` and `public map<string> parameters` (`natives.bal:89–92` region);
   `ContentDisposition` declares `public string fileName`, `disposition`, `name` and
   `public map<string> parameters` (`natives.bal:61–64` region). The rendered class bodies contain
   only methods — `grep -nE 'public string|public map<' new` → 0 hits. The fields are absent from the
   JSON on both sides (class typeDefs have keys `name`, `description`, `type`, `functions` only), so
   this is an extractor gap, not a renderer one. Practical impact: an LLM cannot learn how to populate
   a `ContentDisposition` (`cd.name = "..."`, `cd.fileName = "..."`), which is the standard
   `multipart/form-data` usage.

5. **Inconsistent module prefixing in one signature.** new:239
   `setBody(string|xml|json|byte[]|mime:Entity[]|stream<byte[], io:Error?> entityBody)` uses the
   `mime:` prefix for `Entity` while every other reference in the same class body (`setBodyParts`,
   `getBodyParts`) writes bare `Entity[]`. The prefix originates in the JSON type name string
   (`"string|xml|json|byte[]|mime:Entity[]|stream<byte[], io:Error?>"`), identical on both sides.
   Cosmetic, not incorrect for a consumer.

Shared style notes (both sides, not counted above): `public` and `isolated` qualifiers are stripped
from every declaration, and `()` is used for the nil return (`returns ();`) rather than omitting the
return clause. Both are consistent across all libraries in this pipeline.

## 6. Coverage gaps vs. the library

The bala exports exactly one module (`package.json` `"export": ["mime"]`, and
`modules/` contains only `mime/`), so there is **no submodule-only API** and the
`getDefaultModule()`-only extraction loses nothing for this library.

Symbol-level coverage of the default module in `new` is **complete**:

| Kind | in bala source | in `new` render |
|---|---|---|
| public constants | 29 | 29 |
| public error types | 16 | 16 |
| public classes | 3 | 3 |
| public class methods | 34 | 34 |
| public module functions | 6 | 6 |

48 typeDefs + 6 functions accounts for every public top-level symbol. `ByteStream`
(`byte_stream.bal:29`) is module-private (`class ByteStream`, no `public`) and correctly excluded.
`init.bal` and `event_stream_writer.bal` declare no public symbols (`grep -n "public"` → no matches).
`mime` declares no listeners, services, annotations or records, matching the empty JSON arrays.

**Gaps (8), present in NEITHER render:** the 8 public class fields listed in §5 item 4 —
`MediaType.primaryType`, `.subType`, `.suffix`, `.parameters`; `ContentDisposition.fileName`,
`.disposition`, `.name`, `.parameters`. Shared gap, extractor-level.

`Entity`'s six fields (`cType`, `cId`, `cLength`, `cDisposition`, `headerMap`, `headerNames`) are
`private` and are correctly absent.

## 7. Compiler plugin

`has_plugin: false` — confirmed. `find` over the bala root for `compiler-plugin*` returns nothing
(the bala contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`,
`platform/`), and the upstream clone at `v2.12.2` has no `compiler-plugin/`,
`*-compiler-plugin/` or `compiler_plugin/` directory. `ballerina/mime` ships no compiler plugin, so
nothing plugin-derived is expected in the render and nothing is missing.

The package does ship three native JARs (`mime-native-2.12.2.jar`, `mimepull-1.9.11.jar`,
`jakarta.activation-api-2.0.1.jar`); these are runtime externs behind the `@java:Method` bindings, not
plugin artifacts, and correctly do not affect the render.

## 8. Other considerations

- **Foundational-type accuracy.** `mime` is imported by `ballerina/http`, `ballerina/email` and
  others. The cross-module types they depend on render correctly in `new`: `mime:Entity` is now a
  real class with all 31 methods, `mime:Error` and its 15 subtypes are declared (though flattened,
  §5.2), and `stream<byte[], io:Error?>` is de-versioned relative to `old`'s JSON. `mime:MediaType`
  and `mime:ContentDisposition` render as method-only shells — consumers that need to *construct* a
  `ContentDisposition` (the common `http` multipart path) still cannot learn the field names.
- **No deprecations.** `grep -n "@deprecated\|# Deprecated"` over all six module files → no matches.
- **Stable version.** 2.12.2, built with `ballerina_version` 2201.12.0, `graalvmCompatible: true`,
  not a template. No pre-1.0 concerns.
- **Doc quality.** Every rendered symbol carries its upstream doc comment, including the fenced
  ```ballerina usage examples, which survive intact into the class bodies. The README block (25
  lines) is identical on both sides.
- **Size / tokens.** 210 → 490 lines (+133%). For a foundational module of this reach the extra
  ~280 lines are high-value: they replace 19 information-free comment lines with the entity API that
  every multipart use of `http` needs.
- **One non-ASCII sequence**, new:415: `“primaryType/subtype+suffix”` (curly quotes). This is faithful
  to the source (`natives.bal`, `getBaseType` doc) — not an encoding fault introduced by the pipeline.
  It appears inside a doc comment only, so it cannot affect parsing.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/ballerina_mime.bal.txt new/ballerina_mime.bal.txt` | 210 / 490 |
| 2 | `grep -c '^// Unknown type:' old new` | old 19, new 0 |
| 3 | `grep -n '^// --- ' old` / `new` | old: 7,32,34,162; new: 7,32,34,442 (4 markers each) |
| 4 | `diff <(sed -n '1,123p' old) <(sed -n '1,122p' new)` | only `123d122 <` (one blank line) |
| 5 | `diff <(sed -n '162,211p' old) <(sed -n '442,491p' new)` | identical (`IDENTICAL_FUNCS`) |
| 6 | `grep -c '^const string' old new` | 29 / 29 |
| 7 | `grep -c '^type .* error;' old new` | 0 / 16 |
| 8 | `grep -c '^class ' old new` | 0 / 3 |
| 9 | `grep -c '^    function ' old new` | 0 / 34 |
| 10 | `grep -c '^function ' old new` | 6 / 6 |
| 11 | `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:' old new` | 0 / 0 |
| 12 | `diff <(json.tool old.json) <(json.tool new.json) \| grep -c '^[<>]'` | 88 changed lines total |
| 13 | JSON top-level counts both sides | typeDefs 48, functions 6, clients 0, services 0, annotations 0 |
| 14 | `old.json` class typeDef keys | `['name','description','functions']` — **no `type` field** (placeholder cause) |
| 15 | `new.json` class typeDef keys | `['name','description','type','functions']`, `type == "Class"` |
| 16 | JSON function counts per class, old→new | Entity 32→31, MediaType 3→2, ContentDisposition 2→1 (synthetic `init` Constructor removed) |
| 17 | JSON `getByteStream` return, old vs new | `stream<byte[], ballerina/io:1.8.1:Error?>\|ParserError` → `stream<byte[], io:Error?>\|ParserError` |
| 18 | `new.json` typeDef kinds | `['Class','Constant','Error']` |
| 19 | `grep -n "public type" bala/mime_errors.bal` | 16 types, all `distinct error` / `distinct Error` (lines 19–64) |
| 20 | `grep -n "public class" bala/natives.bal` | `ContentDisposition:59`, `MediaType:87`, `Entity:142` |
| 21 | Count of `public isolated function` inside `class Entity` (bala natives.bal, from line 142) | 31 — matches render |
| 22 | `grep -n "contentType = \|arraySize = " bala/natives.bal` | real defaults: 299/314/338/362/388/430/510 (strings), 451/489 (8192) |
| 23 | JSON `default` for those params, old and new | `"\"\""` and `"0"` on **both** sides — pre-existing extractor bug |
| 24 | JSON `default` for module fn `base64Encode.charset` | `"\"utf-8\""` — correct, class-path-specific bug |
| 25 | `sed -n '175,440p' new \| grep -c '# + '` | 0 (class methods) vs 14 in Functions section |
| 26 | `new.json` `Entity.setContentType` | carries param + return descriptions that the render drops |
| 27 | `grep -nE 'public string\|public map<' new render` | 0 hits — class fields absent |
| 28 | `new.json` class typeDef keys (fields?) | no `fields` key — extractor-level gap |
| 29 | `grep -n "^public isolated function" bala/*.bal` | exactly 6 module-level functions |
| 30 | `grep -n "class" bala/byte_stream.bal` | `class ByteStream` at :29 — non-public, correctly excluded |
| 31 | `grep -n "public" bala/init.bal bala/event_stream_writer.bal` | no matches |
| 32 | `grep -n "@deprecated\|# Deprecated" bala/*.bal` | no matches |
| 33 | `ls bala/modules/` | `mime` only — single module, no submodule gap |
| 34 | `bala/package.json` `export` | `["mime"]`; `ballerina_version` 2201.12.0, `graalvmCompatible` true |
| 35 | `git clone --depth 1 --branch v2.12.2 <repo>` | tag exists, clone succeeded |
| 36 | `diff -q bala/modules/mime/<f> src/ballerina/<f>` × 6 | SAME for all six `.bal` files |
| 37 | `find` for `compiler-plugin*` in bala and clone | no matches on either — no plugin |
| 38 | `grep -nP '[^\x00-\x7F]' new` | one hit, line 415 curly quotes, faithful to source |
| 39 | Cross-check of `OLD_AND_NEW_DIFFS/mime_diff.md` | its figures (210/490, +299/−19, 19→0 placeholders, 52 declarations added, 4 markers each) all reproduce |

## 10. Caveats and unverified items

- The renders themselves were not regenerated; this audit compares the committed artifacts against
  the bala and upstream source. Whether re-running the pipeline today reproduces these exact files
  was not tested.
- The `old`/`new` `ballerina-vscode` commits (`eb5d81b3`, `412ba01e`) were not inspected; attribution
  of each behaviour to a specific renderer/extractor code path is inferred from the JSON-vs-render
  evidence (items 14–16, 23–28 in the evidence log), not from reading the pipeline code.
- Whether the synthetic `init` Constructor removed from the JSON in `new` was intended is not
  determinable from the artifacts. It had no effect on either render (`old` never emitted the class),
  and `mime`'s classes have no explicit `init`, so an implicit no-arg constructor exists regardless.
- The render was not compiled. Syntax was checked structurally (balanced class bodies, terminated
  signatures, no stray tokens), not by a Ballerina parser.

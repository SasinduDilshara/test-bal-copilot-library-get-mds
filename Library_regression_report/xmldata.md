# ballerina/xmldata 2.9.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/xmldata` |
| Pinned version | `2.9.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-xmldata |
| Tag reviewed | `v2.9.2` (commit `5a23d76d0881e7c548941861d8741faf0a96dd82`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/xmldata/2.9.2/java21` |
| Old render | `125` lines |
| New render | `144` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`xmldata` is a small, single-module, deprecated standard-library package: 3 `.bal` files, 448 lines,
13 public symbols in the default module. `new` is strictly better than `old`:

- `old` degraded `xmldata:Error` to `// Unknown type: Error`; `new` emits a real definition with docs.
- `old` emitted **no** annotations at all (`annotations: []` in the JSON); `new` extracts all three
  (`Name`, `Namespace`, `Attribute`) and adds a `// --- Annotations ---` section. These annotations are
  central to this library's API — every `toXml`/`fromXml` doc string references them — so their absence
  in `old` was a material coverage hole.

Nothing was dropped, truncated or made less accurate. README, description, all 5 `typeDefs` and all 5
`functions` are byte-identical between the two JSONs (only the `Error` typeDef differs, and only by the
addition of `baseType: "error"`).

Residual inaccuracies exist in `new`, but every one of them is also in `old` except the `distinct`
qualifier loss on `Error` — which only exists in `new` because `old` rendered nothing for `Error` at all.

## 2. Change inventory

| Metric | old | new |
|---|---|---|
| Lines | 125 | 144 |
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified refs (`mod:1.2.3:Type`) | 0 | 0 |
| Section markers (`// --- `) | 4 | 5 |
| JSON `typeDefs` | 5 | 5 |
| JSON `functions` | 5 | 5 |
| JSON `clients` / `services` | 0 / 0 | 0 / 0 |
| JSON `annotations` | 0 | 4 |

Two diff hunks only (old 16–22 → new 16–24; old 123–125 → new 125–144); +20 / −1 lines.

**Added in `new` (4 declarations):**

| Kind | Name | New render line |
|---|---|---|
| type | `Error` (replaces the `// Unknown type: Error` placeholder, with its doc comment) | 19–21 |
| annotation | `Name` (`NameConfig`, `on type, record field`) | 131–134 |
| annotation | `Namespace` (`NamespaceConfig`, `on type`) | 136–139 |
| annotation | `Attribute` (no type constraint, `on record field`) | 141–144 |

**Removed in `new`:** none.

**Modified:** none beyond `Error`. Verified programmatically — all 5 functions compare `True` and 4 of 5
typeDefs compare `True` between the old and new JSON objects; the README strings are identical (891
chars both sides).

Note on the precomputed diff: `OLD_AND_NEW_DIFFS/xmldata_diff.md` lists an added declaration named
`annotation on`. That is a regex artifact of its declaration scraper on the line
`public annotation Attribute on record field;` (which has no type constraint). The real fourth added
declaration is `annotation Attribute`. Also, the new JSON contains **4** annotation entries but the
render emits **3** lines — because `Name` appears twice (`attachmentPoint: TYPE` and
`attachmentPoint: RECORD_FIELD`) and the renderer correctly merges them into `on type, record field`,
matching the source exactly.

## 3. Correctness against library source

The bala module source and the GitHub tag are byte-identical (`diff` returned no output for both
`xmldata.bal` and `error.bal`), so both are authoritative here.

Every symbol added by `new`, verified against the bala:

| Rendered in `new` | Source | Match |
|---|---|---|
| `type Error error;` + doc | `error.bal:19` `public type Error distinct error;` | partial — see §5.1 |
| `public annotation NameConfig Name on type, record field;` | `xmldata.bal:34` `public annotation NameConfig Name on type, record field;` | exact, incl. 3-line doc (`xmldata.bal:31-33`) |
| `public annotation NamespaceConfig Namespace on type;` | `xmldata.bal:48` | exact, incl. doc (`xmldata.bal:45-47`) |
| `public annotation Attribute on record field;` | `xmldata.bal:53` | exact, incl. doc (`xmldata.bal:50-52`) |

The `NameConfig` / `NamespaceConfig` records that the two typed annotations reference are both present
in the render (new lines 26–29, 34–39), so the annotation section is self-consistent — an LLM reading
`new` can construct a valid `@xmldata:Namespace {prefix: "ns", uri: "..."}` attachment. From `old` it
could not, because the annotations were absent entirely.

Carried-over declarations spot-checked against source (identical in both renders): `toXml`
(`xmldata.bal:62`), `fromJson` (`:123`), `toJson` (`:366`), `toRecord` (`:387`, `@deprecated` correctly
carried), `fromXml` (`:401`), `JsonOptions` (`:104`), `XmlOptions` (`:352`). `fromJson`'s return is
rendered `xml|()|Error` against source `xml?|Error` — semantically equivalent, not a defect.

## 4. Regressions

**None found.**

Checked to conclude this:
- Full 144-line new render and 125-line old render read end to end.
- Programmatic object-by-object comparison of both JSONs: `readme` identical, `description` identical
  (both empty), all 5 `functions` equal, 4/5 `typeDefs` equal, and the differing one (`Error`) only
  gained a field. Nothing was removed on either level.
- `diff` produces exactly two hunks with a single deleted line, `// Unknown type: Error`, which is
  replaced by a superset (the real definition plus its doc comment).
- No declaration present in `old` is absent from `new`; the removed-declarations set is empty.

## 5. Issues in `new` (independent of `old`)

5 issues; only 5.1 is unique to `new` (the rest are shared with `old` and are extractor-level, not
introduced by spec v2).

1. **`distinct` dropped from `Error`.** Source (`error.bal:19`) is
   `public type Error distinct error;`; `new` renders `type Error error;`. The new JSON carries
   `{"type":"Error","baseType":"error"}` with no distinctness marker, so this is lost in the Java
   extractor, not the renderer. Impact is low (the type is only consumed, never subtyped by users),
   but an LLM cannot tell this is a distinct error type. Unique to `new` only in the trivial sense that
   `old` rendered no `Error` definition at all.
2. **Closed records rendered as open.** All four record types are declared closed in source —
   `NameConfig` (`:27`), `NamespaceConfig` (`:40`), `JsonOptions` (`:104`), `XmlOptions` (`:352`) all use
   `record {| ... |}` — but both renders emit `record { ... }`. Identical in both sides' JSON.
3. **Inferred-typedesc parameters mangled.** `toRecord`'s source signature is
   `(xml xmlValue, boolean preserveNamespaces = true, typedesc<record {}> returnType = <>)`; both renders
   show `record {|anydata...;|} returnType = record {|anydata...;|}`. Likewise `fromXml`'s
   `typedesc<map<anydata>> returnType = <>` becomes `map<anydata> returnType = map<anydata>`. The
   returned `returnType|Error` is preserved, so the dependently-typed nature is half-visible, but the
   parameter type shown is not the declared one and the default `= record {|anydata...;|}` /
   `= map<anydata>` is not valid Ballerina. Present identically in the old and new JSON.
4. **`public` / `isolated` qualifiers dropped from functions and types.** Every public function in source
   is `public isolated function`; both renders emit bare `function`. Same for `public type`. Only the
   three annotations carry `public` in `new` (`grep -c '^public '`: old 0, new 3), so the render is
   internally inconsistent about visibility markers.
5. **`toRecord` deprecation rationale lost.** Source `xmldata.bal:384-385` carries
   `# # Deprecated` / `# This function is going away in a future release. Use `fromXml` instead.`
   Neither render contains the string "going away" (`grep -c`: 0 and 0). The `@deprecated` marker
   survives but the replacement hint — the actionable part for an LLM — does not.

## 6. Coverage gaps vs. the library

**Zero gaps in `new`.** The bala has exactly one module (`modules/xmldata`, the default module) — no
submodules, so the shared `getDefaultModule()` limitation is not in play for this library.

Complete public surface of the default module, from `grep -nE '^(public )` over the three bala `.bal`
files, versus the renders:

| Public symbol | Source | in `old` | in `new` |
|---|---|---|---|
| `Error` | `error.bal:19` | placeholder only | yes |
| `NameConfig` | `xmldata.bal:27` | yes | yes |
| `NamespaceConfig` | `xmldata.bal:40` | yes | yes |
| `JsonOptions` | `xmldata.bal:104` | yes | yes |
| `XmlOptions` | `xmldata.bal:352` | yes | yes |
| `Name` (annotation) | `xmldata.bal:34` | **no** | yes |
| `Namespace` (annotation) | `xmldata.bal:48` | **no** | yes |
| `Attribute` (annotation) | `xmldata.bal:53` | **no** | yes |
| `toXml` | `xmldata.bal:62` | yes | yes |
| `fromJson` | `xmldata.bal:123` | yes | yes |
| `toJson` | `xmldata.bal:366` | yes | yes |
| `toRecord` | `xmldata.bal:387` | yes | yes |
| `fromXml` | `xmldata.bal:401` | yes | yes |

`old` gap count: 3 (all annotations) plus a degraded `Error`. `new` gap count: 0.

Correctly excluded from both: the four module-private constants (`XMLNS_NAMESPACE_URI`, `CONTENT`,
`ATTRIBUTE_PREFIX`, `XMLNS`, `xmldata.bal:19-22`), the private helper functions, and `init()` /
`setModule()` in `init.bal` — none are `public`.

## 7. Compiler plugin

`has_plugin: true`, confirmed: `compiler-plugin/compiler-plugin.json` in the bala declares
`plugin_id: "xmldata-compiler-plugin"`, `plugin_class:
io.ballerina.stdlib.xmldata.compiler.XmldataCompilerPlugin`, backed by
`compiler-plugin/libs/xmldata-compiler-plugin-2.9.2.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/stdlib/xmldata/compiler/`, 6 classes:
`XmldataCompilerPlugin`, `XmldataCodeAnalyzer`, `XmldataRecordFieldValidator`, `DiagnosticsCodes`,
`object/Record`, `module-info`). It contributes **validations only** — no code actions, no generated
artifacts, no additional annotations. `XmldataRecordFieldValidator` tracks record types used as the
target of `xmldata:toRecord` / `xmldata:fromXml` calls (`XmldataRecordFieldValidator.java:65-66,
119-136`) and emits three diagnostics (`DiagnosticsCodes.java`):

- `XMLDATA_101` (ERROR) — "invalid field type: the record field does not support the optional value type"
- `XMLDATA_102` (ERROR) — "invalid union type: union type does not support multiple non-primitive record types"
- `XMLDATA_103` (WARNING) — "invalid annotation attachment: child record does not allow name annotation"

Nothing the plugin implies is *missing* from `new`: the annotations it validates (`xmldata:Name`,
`XmldataRecordFieldValidator.java:67`) are now rendered, and the `toRecord` doc already states "The
optional value fields are not allowed in the record type" — which is the human-readable form of
`XMLDATA_101`. In `old`, by contrast, the plugin validated `xmldata:Name` attachments that the render
did not even mention. These are compile-time constraints with no render representation on either side;
that is a pipeline-wide limitation, not an xmldata defect.

## 8. Other considerations

- **The library is deprecated.** The README's first line (carried verbatim into both renders, line 7) is
  a deprecation notice steering users to `ballerina/data.xmldata`. Note that Ballerina Central does
  **not** flag the package as deprecated at the registry level: the API response for
  `ballerina/xmldata/2.9.2` returns `deprecated: null` and an empty `deprecateMessage`. So the only
  deprecation signal in the render is prose, and it is preserved on both sides.
- **`toRecord` is itself `@deprecated`** in favour of `fromXml`; both renders carry the marker but not
  the replacement hint (see §5.5).
- **Size / tokens**: negligible — 144 lines. The +19 lines (+15%) buy the entire annotation API.
- The published package compiles and is a released, stable (2.x) version; `balaVersion 3.0.0`.
- Central reports exactly one module for this package, corroborating the bala `modules/` listing.

## 9. Evidence log

| Check | Result |
|---|---|
| `git clone --depth 1 --branch v2.9.2 <repo>` | succeeded; HEAD `5a23d76d0881e7c548941861d8741faf0a96dd82` |
| `diff src/ballerina/xmldata.bal <bala>/modules/xmldata/xmldata.bal` | no output — identical |
| `diff src/ballerina/error.bal <bala>/modules/xmldata/error.bal` | no output — identical |
| `ls -R <bala>` | one module `xmldata`; files `error.bal`, `init.bal`, `xmldata.bal`; `compiler-plugin/`, `docs/`, `platform/java21/` present |
| `wc -l <bala>/modules/xmldata/*.bal` | 19 + 25 + 404 = 448 |
| `wc -l old/new .bal.txt` | 125 / 144 |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -c 'mod:[0-9]' new` | 0 |
| `grep -n '^// --- '` | old: README/END README/Types/Functions (4); new: same + Annotations at line 129 (5) |
| `grep -nE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation...)' *.bal` | 13 public symbols enumerated in §6 |
| JSON key/list sizes both sides | typeDefs 5/5, functions 5/5, clients 0/0, services 0/0, annotations 0 → 4 |
| Python object equality old vs new JSON | readme `True` (891 chars each); description `''` both; functions all 5 `True`; typeDefs `Error` `False`, other 4 `True` |
| new JSON `Error` typeDef | `{"name":"Error","description":"...","type":"Error","baseType":"error"}` — no `distinct` field |
| old JSON `Error` typeDef | same minus `baseType`; old JSON `annotations` == `[]` |
| new JSON `annotations` dump | 4 entries: `Name`/TYPE, `Name`/RECORD_FIELD, `Namespace`/TYPE, `Attribute`/RECORD_FIELD; typeConstraints `NameConfig`, `NameConfig`, `NamespaceConfig`, none |
| `grep -c 'record {|'` in renders | old 1, new 1 (only inside the `toRecord` signature) |
| `grep -c '^public '` in renders | old 0, new 3 (the annotations) |
| `grep -c 'going away'` in renders | old 0, new 0 |
| JSON param dump for `toRecord`/`fromXml` | identical old vs new; `returnType` typed `record {|anydata...;|}` / `map<anydata>` — not `typedesc<...>` |
| `sed -n '380,404p' xmldata.bal` | confirms `typedesc<record {}> returnType = <>` and the `# # Deprecated` doc block |
| `cat compiler-plugin/compiler-plugin.json` (bala) | plugin id/class/jar as quoted in §7 |
| `find compiler-plugin -name '*.java'` | 6 files listed in §7 |
| `DiagnosticsCodes.java:28-35` | XMLDATA_101/102/103 with severities ERROR/ERROR/WARNING |
| `XmldataRecordFieldValidator.java:65-67,119-136` | hooks on `xmldata:toRecord`, `xmldata:fromXml`, `xmldata:Name` |
| `GET api.central.ballerina.io/2.0/registry/packages/ballerina/xmldata/2.9.2` | `deprecated: null`, `deprecateMessage: ""`, 1 module, `balaVersion 3.0.0` |

## 10. Caveats and unverified items

- **Compiler-plugin jar not decompiled.** §7 is based on the tagged Java source in the clone plus the
  bala's `compiler-plugin.json`. The shipped `xmldata-compiler-plugin-2.9.2.jar` bytecode was not
  disassembled to confirm it was built from that exact source. Given `xmldata.bal` and `error.bal` are
  byte-identical between tag and bala, divergence is unlikely but formally unverified.
- **`distinct` provenance.** I established that the new JSON lacks any distinctness marker and therefore
  that the loss occurs at or before the JSON stage. I did not read the Java extractor source to confirm
  whether `distinct` is representable in the spec-v2 JSON schema at all; it may be a schema limitation
  rather than an extraction bug.
- **Renders not regenerated.** I audited the committed `old`/`new` artifacts as given; I did not re-run
  the two-stage pipeline to reproduce them, so I cannot independently confirm the source-side commits
  (`eb5d81b3` / `412ba01e`) stated in the brief.
- Deprecation status is asserted from the README text and Central's (empty) registry flag; I did not
  check whether a later `xmldata` release or the `data.xmldata` successor changes that picture, as it is
  out of scope for a pinned-version audit.

# ballerina/data.xmldata 1.6.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/data.xmldata` |
| Pinned version | `1.6.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-data.xmldata |
| Tag reviewed | `v1.6.3` (exact tag, commit `08e1fc7`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/data.xmldata/1.6.3/java21` |
| Old render | `626` lines |
| New render | `665` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Three changes, all improvements, all confirmed against the published bala source:

1. Eight `ballerina/lang.int:0.0.0:Unsigned32` version-qualified type refs became the correct
   `int:Unsigned32` (matches `xml_api.bal:28,30` verbatim).
2. The single `// Unknown type: Error` placeholder became a real definition with its doc comment.
3. A new `// --- Annotations ---` section emits all 8 public annotations of the module — previously
   absent entirely from `old`. These are the annotations (`@xmldata:Name`, `@xmldata:Namespace`,
   `@xmldata:Attribute`, …) that the README itself instructs users to apply, so their absence in
   `old` was a real functional gap for an LLM consumer.

Nothing was removed, truncated, or made less accurate. `diff` shows 0 removed declarations. README
block, description, all 12 typeDefs and all 8 functions are byte-identical between the two JSONs
except for the type-ref and `Error` changes listed above.

## 2. Change inventory

Line counts (`wc -l`): old 626, new 665 (+39). Diff: 49 added lines, 10 removed lines, 3 hunks.

| Kind | old | new | Δ |
|---|---|---|---|
| `typeDefs` (JSON) | 12 | 12 | 0 |
| `functions` (JSON) | 8 | 8 | 0 |
| `annotations` (JSON) | 0 | 10 | +10 |
| `clients` / `services` (JSON) | 0 / 0 | 0 / 0 | 0 |
| `public annotation` lines (render) | 0 | 8 | +8 |
| `// Unknown type:` lines | 1 | 0 | −1 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 8 | 0 | −8 |
| `// --- ` section markers | 4 | 5 | +1 |

The JSON carries 10 annotation entries because `Name` and `Namespace` are emitted once per
attachment point (`TYPE` and `RECORD_FIELD`); `toSyntaxString` correctly merges each pair into a
single line `... on type, record field`, yielding 8 rendered annotations. Verified: JSON entries
`Name`/`TYPE`, `Name`/`RECORD_FIELD`, `Namespace`/`TYPE`, `Namespace`/`RECORD_FIELD`; render lines
648 and 654.

Declarations added (new only):
- `type Error error;` with its 2-line doc (replaces `// Unknown type: Error`)
- `annotation Element`, `Sequence`, `Choice`, `SequenceOrder`, `Name`, `Namespace`, `Attribute`, `Any`

Declarations removed: **none**.

Declarations modified: `ParticleOccurrence`, `ElementConfig`, `SequenceConfig`, `ChoiceConfig`
(field type refs only, 2 fields each = 8 refs).

The precomputed diff at `OLD_AND_NEW_DIFFS/data.xmldata_diff.md` lists the added declarations as
`annotation Choice / Element / Name / Namespace / Sequence / SequenceOrder / annotation on /
type Error`. Its `annotation on` entry is a regex artifact: it collapses `public annotation Attribute
on record field;` and `public annotation Any on record field;` (annotations with no type constraint)
into one bogus name, so the diff file under-reports by one. Verified by `grep -n '^public annotation'`
on the new render: 8 lines, names Element, Sequence, Choice, SequenceOrder, Name, Namespace,
Attribute, Any.

## 3. Correctness against library source

GitHub `v1.6.3` `ballerina/*.bal` is **byte-identical** to the bala `modules/data.xmldata/*.bal`
(`diff -q` on all three files: `init.bal`, `xml_api.bal`, `xpath_api.bal` — all identical). So
GitHub and the bala agree; no arbitration needed.

Full public surface of the default module (only module in the package; `package.json` `export` =
`["data.xmldata"]`, Central lists exactly one module):

| Source | Symbol | In `new` render? |
|---|---|---|
| `xml_api.bal:26` | `ParticleOccurrence` | yes, L463 |
| `xml_api.bal:34` | `ElementConfig` | yes, L472 |
| `xml_api.bal:42` | `SequenceConfig` | yes, L479 |
| `xml_api.bal:50` | `ChoiceConfig` | yes, L486 |
| `xml_api.bal:58` | `SequenceOrderConfig` | yes, L493 |
| `xml_api.bal:67` | `NameConfig` | yes, L500 |
| `xml_api.bal:79` | `NamespaceConfig` | yes, L507 |
| `xml_api.bal:104` | `Options` | yes, L516 |
| `xml_api.bal:112` | `SourceOptions` | yes, L525 |
| `xml_api.bal:124` | `Error` | yes, L538 (new) / `// Unknown type` in old |
| `xml_api.bal:208` | `JsonOptions` | yes, L542 |
| `xpath_api.bal:20` | `XPathRawTemplate` | yes, L556 (body empty — see §5) |
| `xml_api.bal:132/141/150/159/170/227/487` | `parseAsType`, `parseString`, `parseBytes`, `parseStream`, `toXml`, `fromJson`, `validate` | yes, L567–619 |
| `xpath_api.bal:38` | `transform` | yes, L628 |
| `xml_api.bal:39/47/55/64/76/90/96/101` | annotations `Element`, `Sequence`, `Choice`, `SequenceOrder`, `Name`, `Namespace`, `Attribute`, `Any` | yes, L633–665 (new only) |

Spot checks on the three changes:

- **`int:Unsigned32`.** `xml_api.bal:28` `int:Unsigned32 minOccurs?;` and `:30` `int:Unsigned32
  maxOccurs?;`. `new` renders exactly `int:Unsigned32`. `old`'s `ballerina/lang.int:0.0.0:Unsigned32`
  is not valid Ballerina and the `0.0.0` version is fabricated. Correct in `new`.
- **`Error`.** `xml_api.bal:124` `public type Error distinct error;`, doc at `:122–123`. `new` emits
  the doc verbatim plus `type Error error;`. The `baseType: "error"` field is newly present in the
  new JSON (`{"name":"Error","type":"Error","baseType":"error"}` vs old's `{"name":"Error","type":
  "Error"}`), which is what drives the real definition. `distinct` is not carried — see §5.
- **Annotations.** Each of the 8 was compared line-by-line against its source declaration and doc
  comment. Type constraint, name, and attachment points all match:
  `Element`/`ElementConfig`/`record field` (`:38–39`), `Sequence`/`SequenceConfig`/`record field`
  (`:46–47`), `Choice`/`ChoiceConfig`/`record field` (`:54–55`), `SequenceOrder`/
  `SequenceOrderConfig`/`record field` (`:63–64`), `Name`/`NameConfig`/`type, record field`
  (`:72–76`), `Namespace`/`NamespaceConfig`/`type, record field` (`:86–90`), `Attribute`/no
  constraint/`record field` (`:92–96`), `Any`/no constraint/`record field` (`:98–101`). Doc text is
  reproduced verbatim including the trailing-space artifacts on `:73` and `:87`.

README block: the render's lines 8–456 are byte-identical to `docs/README.md` (448 lines) apart from
one trailing blank line. Identical in both renders (`o['readme'] == n['readme']` → True).

## 4. Regressions

**None found.**

What I checked to conclude this:
- `diff -u old new` in full (only 3 hunks, all shown above); 10 removed lines, all of which are the
  8 version-qualified type-ref lines plus the 2 lines of `// Unknown type: Error` context —
  every one replaced by a strictly more accurate line.
- Set comparison of JSON `typeDefs` names: `removed: set()`.
- Set comparison of JSON `functions` names: identical, 8 on both sides.
- Per-entry deep equality on all 12 typeDefs and all 8 functions: the only entries that differ are
  `ParticleOccurrence`, `ElementConfig`, `SequenceConfig`, `ChoiceConfig` (type refs) and `Error`
  (`baseType` added). All 8 function entries are byte-equal between the two JSONs.
- `readme` and `description` fields byte-equal between JSONs.
- No parameter, default, return type, or doc line is present in `old` and absent in `new`.

## 5. Issues in `new` (independent of `old`)

None of these is a regression — items 2–7 are present identically in `old`. Item 1 and 8 concern
constructs `old` did not render at all.

1. **`distinct` dropped from `Error`.** Source `xml_api.bal:124` is `public type Error distinct
   error;`; `new` renders `type Error error;`. A distinct error type is a nominal subtype — an LLM
   reading this render would believe `xmldata:Error` is a plain `error` alias and might, e.g.,
   generate `error e = ...; return e;` where the API demands the distinct type. The JSON does not
   carry a distinct marker (`baseType` is just `"error"`), so this originates in stage 1.
2. **`XPathRawTemplate` rendered as an empty class.** Source `xpath_api.bal:20–24` is a public
   *object type* with `*obj:RawTemplate` inclusion and two public fields, `public string[] &
   readonly strings;` and `public anydata[] insertions;`. Both renders emit `class XPathRawTemplate
   {\n}` — wrong kind (class vs object type) and no members. JSON on both sides:
   `{"name":"XPathRawTemplate","description":"","type":"Class"}`. Since `transform` takes this as its
   `query` parameter, a consumer has no way to learn from the render that a raw template literal
   (`` xmldata:transform(x, `/book/id`) ``) is what goes there.
3. **`typedesc` inference parameters are mangled into non-compiling text.** `typedesc<record {}> t =
   <>` becomes `record {|anydata...;|} t = record {|anydata...;|}` in `parseAsType`, `parseString`,
   `parseBytes`, `parseStream` (render L567–591) and `typedesc<record {}> schema` becomes
   `record {|anydata...;|} schema` in `validate` (L619); `typedesc<anydata> td = <>` becomes
   `anydata td = anydata` in `transform` (L628). `record {|anydata...;|} t = record {|anydata...;|}`
   is not a valid default-value expression. Identical in `old`.
4. **Record field default values are lost and required-with-default fields are shown optional.**
   Every field carrying a default is rendered with `?` and no default: `Options.attributePrefix =
   EMPTY_STRING` and `.textFieldName = "#content"` (`:106,108`); `SourceOptions.allowDataProjection
   = true`, `.useSemanticEquality = true`, `.enableConstraintValidation = true` (`:115,117,119`);
   `JsonOptions.attributePrefix = "@"`, `.arrayEntryTag = "item"`, `.rootTag = ()`,
   `.textFieldName = CONTENT`, `.userAttributePrefix = EMPTY_STRING` (`:210–219`). The defaults are
   documented behaviour of the API (e.g. `arrayEntryTag` defaulting to `"item"`); an LLM cannot
   recover them from this render. Identical in `old`.
5. **All 12 record types are closed (`record {| |}`) in source but rendered open (`record { }`).**
   This inverts the library's central projection semantics — the README section "Controlling Which
   Elements to Convert" turns entirely on the open/closed distinction. Identical in `old`.
6. **Wrapped doc lines lose their `# ` prefix**, producing bare non-comment text inside the render:
   L548 (`is not in the valid format, ...`), L600 (`successfully converted or else an
   \`xmldata:Error\``), L617 (`Ballerina record type representing the schema defined by the XSD.`),
   L627 (`to the specified type, returns an \`Error\` value`). The rendered file therefore does not
   compile as Ballerina. Identical in `old`.
7. **`isolated` dropped from all 8 functions** (all are `public isolated function` in source).
   Identical in `old`. Low impact.
8. **`const` dropped from the 8 annotation declarations.** Source declares all 8 as `public const
   annotation ...`; `new` renders `public annotation ...`. `const annotation` constrains the
   annotation value to a constant expression, which is why `@xmldata:Name {value: "title-name"}`
   must use literals. New-only in the sense that `old` had no annotation section at all — but this
   is a fidelity nit against the source, not a loss versus `old`.

Not issues (checked and correct): `validate`'s doc parameter order is reordered from the source's
`schema`-then-`xmlValue` to match the actual signature order — an improvement, present on both
sides. `validate` returning `Error|()` rather than `Error?` is valid Ballerina. `SourceOptions`
listing its `*Options`-included fields last rather than first is cosmetic.

## 6. Coverage gaps vs. the library

**Zero module-level gaps.** Every public symbol of the default module appears in `new` — verified
exhaustively (table in §3) by grepping the bala for `^public type`, `^public isolated function|
^public function`, `^public const annotation|^public annotation`, `^public const `, `^public class|
^public isolated class`, and a catch-all `^public ` excluding those forms. Results: 12 public types,
8 public functions, 8 public annotations, 0 public constants, 0 public classes, 0 other public
declarations. All 28 are in `new`.

Submodule API: **none exists**. `modules/` contains exactly one directory, `data.xmldata`, which is
the default module. `package.json` `export` is `["data.xmldata"]` and Central lists one module. So
the known shared `getDefaultModule()` limitation costs this library nothing.

Sub-symbol gaps (not top-level, listed for completeness): `XPathRawTemplate.strings` and
`XPathRawTemplate.insertions` (`xpath_api.bal:22–23`) appear in neither render — see §5 item 2.

Correctly excluded from both renders: `SupportedType` (`xpath_api.bal:29`, non-public), the module
constants `XMLNS_NAMESPACE_URI`, `CONTENT`, `ATTRIBUTE_PREFIX`, `XMLNS`, `EMPTY_STRING`
(`xml_api.bal:19–23`, non-public), and the private helper functions.

## 7. Compiler plugin

`has_plugin: true`, confirmed: `compiler-plugin/compiler-plugin.json` in the bala declares
`plugin_class: io.ballerina.lib.data.xmldata.compiler.XmldataCompilerPlugin`, backed by
`compiler-plugin/libs/data.xmldata-compiler-plugin-1.6.3.jar`.

Source (7 Java files under `compiler-plugin/src/main/java/io/ballerina/lib/data/xmldata/compiler/`):
`XmldataCompilerPlugin` registers a single `XmldataCodeAnalyzer`, which registers
`XmldataRecordFieldValidator` (627 lines) on `SyntaxKind.MODULE_PART`. It contributes
**validation only — no code actions, no code generation, no generated artifacts, no additional
annotations.** Its 11 diagnostics (`XmldataDiagnosticCodes.java:33–51`):

`XML_ERROR_201` duplicate field · `202` unsupported union type · `203` unsupported record field type ·
`204` expected a record type · `205` `@Name` not allowed here · `206` invalid XSD model-group
annotation · `207` invalid sequence type · `208` invalid sequence rest type · `209` invalid choice
rest type · `210` conflicting annotations on one record field · `211` unsupported XPath projection
type.

Entry points it validates: `validateParseFunctionExpectedType` (the four `parse*` functions),
`validateXPathTransformFunctionExpectedType` (`transform`), `validateRecordTypeDefinition`,
`validateXsdModelGroupAnnotations`, `validateChoiceAnnotation`, `validateSequenceAnnotation`,
`validateRecordFieldNames`, `validateRecordFieldType`.

**Does anything the plugin implies fail to surface in the render?** Before this change, yes and
badly: the plugin's entire XSD model-group enforcement (`XML_ERROR_206/207/208/209/210`) is defined
in terms of the `@Element`, `@Sequence`, `@Choice`, `@SequenceOrder` annotations, and `old` rendered
none of them. `new` now emits all four with their type constraints and attachment points, so a
consumer can at least form valid annotation applications. Two things the plugin enforces still are
not visible in `new`: (a) the `SupportedType` union `()|boolean|int|float|decimal|string|xml` that
bounds `transform`'s projection (`xpath_api.bal:29`) is non-public and rendered nowhere, so
`XML_ERROR_211` is unpredictable from the render alone — this is a shared, pre-existing gap;
(b) the closed-record requirement implied by `XML_ERROR_204`/projection semantics is obscured by the
open-record rendering noted in §5 item 5.

## 8. Other considerations

- **Version / stability.** 1.6.3, post-1.0, not deprecated (Central `deprecated: null`,
  `deprecateMessage: ""`). `ballerinaVersion` 2201.12.9, pull count 6,794.
- **No version drift.** Both renders came from the same bala; the two JSONs' `readme`, `description`,
  function set and type set are identical, consistent with the brief's `PIN_OK` claim. No contrary
  evidence found.
- **Size.** 21,150 → 38,938 bytes JSON, 626 → 665 lines rendered (+6.2%). The README block is 449 of
  665 lines (67%) of the render and is unchanged; the entire API surface fits in ~210 lines. Token
  cost of the change is negligible.
- **`source_repository` in `package.json` is stale**: it points at
  `module-ballerina-data-xmldata` (hyphen), while the live repo is `module-ballerina-data.xmldata`
  (dot). The manifest's URL is the correct one and resolves; the `package.json` one 404s. Does not
  affect the render.
- **The render does not compile as Ballerina** on either side (unprefixed doc-continuation lines,
  `record {|anydata...;|} t = record {|anydata...;|}` defaults). This is a general renderer property,
  not specific to this library, and unchanged by the spec-v2 switch.

## 9. Evidence log

| Check | Result |
|---|---|
| `git ls-remote --tags <repo> \| grep v1.6.` | `v1.6.0`, `v1.6.1`, `v1.6.2`, **`v1.6.3`** present |
| clone at `v1.6.3`, `git log --oneline -1` | `08e1fc7 [Gradle Release Plugin] - pre tag commit: 'v1.6.3'`; `git describe --tags` → `v1.6.3` |
| `wc -l old/*.bal.txt new/*.bal.txt` | 626 / 665 |
| `diff -u old new \| grep -c '^+'` / `'^-'` | 49 / 10 (incl. headers); 3 hunks |
| `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 8 / 0 |
| `grep -c '^public annotation' new` | 8 (lines 633,636,639,642,648,654,660,665) |
| JSON top-level counts, old | typeDefs 12, functions 8, annotations 0, clients 0, services 0 |
| JSON top-level counts, new | typeDefs 12, functions 8, annotations 10, clients 0, services 0 |
| Python set-diff on typeDef names | `removed: set()`, `added: set()` |
| Python set-diff on function names | identical, 8 each |
| Python deep-equality per typeDef | differs only for `ParticleOccurrence`, `ElementConfig`, `SequenceConfig`, `ChoiceConfig` (type refs), `Error` (`baseType` added) |
| Python deep-equality per function | 0 of 8 differ |
| `o['readme'] == n['readme']`, `o['description'] == n['description']` | True, True |
| `diff -q` GitHub `ballerina/*.bal` vs bala `modules/data.xmldata/*.bal` | `init.bal`, `xml_api.bal`, `xpath_api.bal` all identical |
| `diff` bala `docs/README.md` vs render lines 8–456 | identical except one trailing blank line (448 lines) |
| `grep -n '^public type'` bala | 12 hits (`xml_api.bal:26,34,42,50,58,67,79,104,112,124,208`; `xpath_api.bal:20`) |
| `grep -n '^public isolated function\|^public function'` bala | 8 hits (`xml_api.bal:132,141,150,159,170,227,487`; `xpath_api.bal:38`) |
| `grep -n '^public const annotation\|^public annotation'` bala | 8 hits (`xml_api.bal:39,47,55,64,76,90,96,101`) |
| `grep -n '^public const '` (non-annotation) / `^public class` / catch-all `^public ` | 0 / 0 / 0 |
| `ls bala/java21/modules` | `data.xmldata` only — no submodules |
| `package.json` `export` | `["data.xmldata"]` |
| `cat compiler-plugin/compiler-plugin.json` | `plugin_class: io.ballerina.lib.data.xmldata.compiler.XmldataCompilerPlugin` |
| `find compiler-plugin -name '*.java' \| wc -l` | 7 |
| `grep` `XmldataDiagnosticCodes.java:33–51` | 11 diagnostics `XML_ERROR_201`…`211` |
| `grep 'addSyntaxNodeAnalysisTask\|addCodeAnalyzer'` | one analyzer, one task, on `SyntaxKind.MODULE_PART`; no code actions, no generators |
| `wc -l XmldataRecordFieldValidator.java` | 627 |
| Central `GET /2.0/registry/packages/ballerina/data.xmldata/1.6.3` | `deprecated: null`, 1 module, `ballerinaVersion 2201.12.9`, pullCount 6794 |
| New JSON annotation dump | 10 entries; `Name` and `Namespace` each duplicated across `TYPE` + `RECORD_FIELD` → merged to 8 render lines |

## 10. Caveats and unverified items

- The claim that both sides used the same bala is inferred, not directly observed: I did not have
  access to the two `ballerina-vscode` checkouts or a pipeline log. The evidence supporting it is
  the byte-identical README, description, function set, and 8-of-8 byte-identical function JSON
  entries. Consistent with the brief's `PIN_OK`, but not independently proven.
- The compiler-plugin jar in the bala (`data.xmldata-compiler-plugin-1.6.3.jar`) was not decompiled;
  plugin behaviour is described from the GitHub `v1.6.3` Java sources, which I verified match the
  bala only for the `.bal` files (the jar is binary, so no equivalent `diff` was possible).
- I did not attempt to compile either render with `bal build`; the non-compiling constructs in §5
  items 3 and 6 were identified by reading, not by running the compiler.
- Whether the stage-1 extractor *could* carry `distinct`, `const`, `isolated`, closed-record `{| |}`,
  field defaults, or object-type members is unknown — I inspected only the emitted JSON, not the
  `CopilotLibraryManager` / `ModelToJsonConverter` source. The report states only that the
  information is absent from the JSON, not why.

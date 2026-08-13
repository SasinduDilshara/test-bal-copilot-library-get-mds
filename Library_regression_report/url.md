# ballerina/url 2.6.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/url` |
| Pinned version | `2.6.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-url |
| Tag reviewed | `v2.6.2` (commit `87d40a0`, "[Gradle Release Plugin] - pre tag commit: 'v2.6.2'") |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/url/2.6.2` (central cache; platform root `java21/`) |
| Old render | `44` lines |
| New render | `45` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/url` is one of the smallest standard-library modules: a single default module `url`
exporting exactly three public symbols — `Error`, `encode()`, `decode()`. The entire public API
fits in 3 source files totalling 86 lines.

The only difference between the two renders is one hunk: `old` degraded the error type to
`// Unknown type: Error` (no doc, no definition); `new` emits a real definition with its doc
comment. Every other byte of the two files is identical — README block, both function
signatures, both doc blocks, section markers. The underlying JSON differs by exactly one added
field (`"baseType": "error"` on the `Error` typeDef).

This is a clean, small improvement with no offsetting loss. One fidelity nit exists in `new`
(the `distinct` qualifier is not carried into the rendered type), but it is an addition that is
slightly imprecise, not a removal of anything `old` had.

## 2. Change inventory

Line counts: `old` = 44, `new` = 45 (`wc -l`). Full `diff` output is a single 1-line-for-2-lines
hunk at line 20:

```
20c20,21
< // Unknown type: Error
---
> # Represents the error type of the module.
> type Error error;
```

Declaration sets (`grep -nE '^(public )?(isolated )?(function|type|class|enum|const|annotation|listener|service)'`):

| Kind | old | new | delta |
|---|---|---|---|
| type | 0 | 1 (`Error`) | **+1** |
| function | 2 (`encode`, `decode`) | 2 (`encode`, `decode`) | 0 |
| class / enum / const / annotation / service / listener / client | 0 | 0 | 0 |

Other signals:

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| `// --- ` section markers | 4 | 4 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 |

Removed declarations: **none**. Modified declarations: **none** (both function lines are
byte-identical across sides). Doc content added: 1 line (`# Represents the error type of the
module.`), which `old` dropped entirely with the placeholder.

JSON delta (`diff` of both pretty-printed JSONs): a single change — `"baseType": "error"` added
to the `Error` entry in `typeDefs`. `functions`, `clients`, `services`, `annotations`, `readme`,
`description` are identical.

## 3. Correctness against library source

The bala's `modules/url/*.bal` is byte-identical to the upstream `ballerina/*.bal` at tag
`v2.6.2` (verified with `diff` on all three files — `init.bal`, `url.bal`, `url_errors.bal`:
IDENTICAL). So GitHub and bala do not disagree here.

Exhaustive check of every public symbol (this library is small enough to verify completely):

| Symbol | Source | Rendered as | Correct? |
|---|---|---|---|
| `Error` | `ballerina/url_errors.bal:18` — `public type Error distinct error;` | `new`: `type Error error;` with doc `# Represents the error type of the module.` (`new/…bal.txt:20-21`); `old`: `// Unknown type: Error` | `new` correct in kind and doc; **`distinct` qualifier not carried** (see §5). `old` conveys nothing. |
| `encode` | `ballerina/url.bal:28` — `public isolated function encode(string value, string charset) returns string\|Error` | both sides: `function encode(string value, string charset) returns string\|Error;` | Parameters, order, types and return union all match. `public`/`isolated` qualifiers dropped — renderer-wide convention, identical on both sides. |
| `decode` | `ballerina/url.bal:41` — `public isolated function decode(string value, string charset) returns string\|Error` | both sides: `function decode(string value, string charset) returns string\|Error;` | Same — matches. |

Doc blocks: the `encode`/`decode` doc comments in both renders reproduce
`ballerina/url.bal:19-27` and `:32-40` verbatim, including the ` ```ballerina ` example blocks
and the `+ value` / `+ charset` / `+ return` parameter docs. Nothing paraphrased or truncated.

README: `new` (and `old`) reproduce all 7 lines of `java21/docs/README.md` verbatim between the
`// --- README ---` / `// --- END README ---` markers (`cat` comparison of both).

Non-public symbols `init()` (`init.bal:19`) and `setModule()` (`init.bal:23`) are module-private
and correctly absent from both renders.

## 4. Regressions

**None found.**

What was checked to reach that conclusion:
- Full `diff old new` — one hunk only, and it is purely additive (1 placeholder line replaced by
  1 doc line + 1 real declaration). No line present in `old` carries information absent from `new`.
- Declaration-set comparison by grep: `new` is a strict superset of `old` (`{encode, decode}` ⊂
  `{Error, encode, decode}`).
- Both function signature lines are byte-identical between sides — no parameter, default, return
  type, or doc line dropped.
- JSON diff: the only change is an *added* field. No key removed, no value altered.
- README section, section markers (4 on both), and the module header comment are unchanged.

Specifically relevant to this batch's concern about foundational cross-package types: `url:Error`
is imported by other packages (e.g. via `string|url:Error` returns). In `old` it was an opaque
`// Unknown type: Error` with no indication it was even an error type; in `new` an LLM reading
the render can see it is an `error`. That is the opposite of a regression.

## 5. Issues in `new` (independent of `old`)

1. **`distinct` qualifier lost on `Error`** (`new/ballerina_url.bal.txt:21`). Source is
   `public type Error distinct error;` (`ballerina/url_errors.bal:18`); the render says
   `type Error error;`. The JSON records only `"baseType": "error"`, so the loss originates in
   the extractor, not the renderer. Practical impact is low — `url:Error` has no subtypes and is
   used only as a whole in `string|Error` returns — but a consumer told the type is a plain
   `error` could wrongly conclude an arbitrary `error` value is assignable to `url:Error`
   (it is not, since the type is distinct). This is an inaccuracy in an *added* line, so it is
   not a regression against `old`, which said nothing at all.

No other issues: no invented symbols, no wrong types, no broken doc text, no malformed syntax
(both function lines and the type line are valid Ballerina declaration forms modulo the elided
`public`/`isolated` qualifiers, which are dropped uniformly by this pipeline on both sides).

On encoding: the doc example contains `…a=12&b=55¶m2=99` (U+00B6 PILCROW) in both renders. This
is **not** a render defect — the same byte sequence is present in the published bala
(`modules/url/url.bal:21`, `:34`) and in the upstream tag `v2.6.2` (`ballerina/url.bal:21`, `:34`,
verified IDENTICAL by `diff`). It is an upstream typo (an unescaped `&para;` HTML entity
collapse) that the pipeline faithfully reproduces on both sides.

## 6. Coverage gaps vs. the library

**None.**

- `package.json` `"export": ["url"]` — a single exported module.
- Bala `modules/` contains exactly one directory, `url` (i.e. the default module). Central
  metadata for `ballerina/url/2.6.2` likewise lists exactly one module, `url`.
- Therefore the `getDefaultModule()`-only extraction limitation described in the brief costs this
  library nothing: there are no submodules to miss.
- All 3 public symbols of that module (`Error`, `encode`, `decode`) appear in `new`. `old` was
  missing 1 of 3 in usable form.

## 7. Compiler plugin

`has_plugin: false` in the manifest, and confirmed independently:
- The bala platform root `java21/` contains only `bala.json`, `dependency-graph.json`, `docs/`,
  `modules/`, `package.json`, `platform/` — there is **no** `compiler-plugin/` directory and no
  `compiler-plugin.json`.
- The upstream clone at `v2.6.2` has no `compiler-plugin`, `*-compiler-plugin`, or
  `ballerina-*-compiler-plugin` directory (`find -maxdepth 2 -iname '*plugin*'` returns nothing);
  the only non-Ballerina source tree is `native/`, which holds the JNI implementation
  (`io.ballerina.stdlib.url.nativeimpl.*`), packaged as `platform/java21/url-native-2.6.2.jar`.

So this library contributes no code actions, validations, generated artifacts, or plugin-driven
annotations, and nothing plugin-implied is missing from the render.

## 8. Other considerations

- **Stability**: `2.6.2` is a stable post-1.0 release; Central reports `deprecated: null`, empty
  `deprecateMessage`, `visibility: public`, `graalvmCompatible: Yes`, 36,632 pulls. No deprecation
  handling is needed in the render.
- **Built with**: `ballerina_version: 2201.12.0`, `language_spec_version: 2024R1`.
- **Size / token implications**: negligible — 44 → 45 lines, 2,919 → 2,946 JSON bytes. The +1 line
  buys the single most useful missing fact in the old render (that `Error` is an error type).
- **Doc quality**: high. Both functions carry full doc comments with runnable examples and per-
  parameter descriptions, all preserved verbatim. The upstream `¶` typo (§5) is the only blemish
  and is inherited, not introduced.
- **`public`/`isolated` elision**: both renders present `function encode(...)` rather than
  `public isolated function encode(...)`. Since every symbol in the render is public by
  construction this is harmless for `public`, but the loss of `isolated` means a consumer cannot
  tell from the render that these functions are safe to call from isolated contexts. Shared by
  both sides; noted for whoever owns the renderer, not a finding against this change.

## 9. Evidence log

| # | Check (command / file:line) | Result |
|---|---|---|
| 1 | `wc -l url/{old,new}/ballerina_url.bal.txt` | 44 / 45 |
| 2 | `diff url/old/ballerina_url.bal.txt url/new/ballerina_url.bal.txt` | single hunk `20c20,21`; placeholder → doc + `type Error error;` |
| 3 | `grep -c '^// Unknown type:'` both files | old 1, new 0 |
| 4 | `grep -c '^// --- '` both files | 4 and 4 |
| 5 | `grep -nE '^(public )?(isolated )?(function\|type\|class\|enum\|const\|annotation\|listener\|service)'` both | old: L33 `encode`, L44 `decode`. new: L21 `type Error`, L34 `encode`, L45 `decode` |
| 6 | `diff <(python3 -m json.tool old/…json) <(python3 -m json.tool new/…json)` | one change: `+ "baseType": "error"` on `typeDefs[0]` |
| 7 | `wc -c` both JSONs | 2,919 / 2,946 bytes |
| 8 | `ls -R /Users/admin/.ballerina/…/ballerina/url/2.6.2` | platform root `java21/`; `modules/url/{init,url,url_errors}.bal`; `platform/java21/url-native-2.6.2.jar`; **no** `compiler-plugin/` |
| 9 | `cat` bala `package.json` | `"export": ["url"]`, `ballerina_version 2201.12.0`, `platform java21`, `template false`, `graalvmCompatible true` |
| 10 | `git clone --depth 1 --branch v2.6.2 …/module-ballerina-url` ; `git describe --tags` | tag `v2.6.2` resolved, HEAD `87d40a0` |
| 11 | `diff <clone>/ballerina/{init,url,url_errors}.bal` vs bala `modules/url/` | all three IDENTICAL |
| 12 | `<clone>/ballerina/url_errors.bal:18` | `public type Error distinct error;` |
| 13 | `<clone>/ballerina/url.bal:28` | `public isolated function encode(string value, string charset) returns string\|Error = @java:Method {…} external;` |
| 14 | `<clone>/ballerina/url.bal:41` | `public isolated function decode(string value, string charset) returns string\|Error = @java:Method {…} external;` |
| 15 | `<clone>/ballerina/init.bal:19,23` | `isolated function init()`, `isolated function setModule()` — both module-private, absent from both renders (correct) |
| 16 | `grep -rn '^public …' <clone>/ballerina/*.bal` | exactly 3 public symbols: `Error`, `encode`, `decode` |
| 17 | `find <clone> -maxdepth 2 -iname '*plugin*'` | no matches |
| 18 | `cat` bala `java21/docs/README.md` (7 lines) vs render README block | verbatim match |
| 19 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/url/2.6.2` | `deprecated: None`, `modules: [url]` (single), `visibility public`, `pullCount 36632`, `graalvmCompatible Yes` |
| 20 | bala `modules/url.bal:21`, `:34` and clone `ballerina/url.bal:21`, `:34` | `¶` present upstream — render faithfully reproduces it on both sides |
| 21 | `cat` bala `dependency-graph.json` | only dependency is `ballerina/jballerina.java 0.0.0`; single module `url` |
| 22 | `cat OLD_AND_NEW_DIFFS/url_diff.md` | claims (+2/−1, 1 hunk, 1 type added, 1→0 unknowns) independently reproduced by checks 1–5 — accurate |

## 10. Caveats and unverified items

- **Whether the lost `distinct` qualifier is intentional.** The extractor emits only
  `"baseType": "error"` (evidence 6); I did not read the spec-v2 extractor source to determine
  whether `distinct` is deliberately elided for all error types or is an oversight specific to
  this shape. The observation in §5 is about the render's fidelity to the library, which is
  verified; the intent behind it is unverified.
- **`public`/`isolated` elision** is stated as a pipeline-wide convention on the basis that it is
  identical on both sides for both functions here. I did not confirm it across other libraries,
  so "renderer-wide" is an inference from a two-function sample; the fact that both sides elide
  them identically here is verified.
- Everything else in this report was verified directly against the bala, the `v2.6.2` upstream
  clone, Central metadata, or the render/JSON files themselves.

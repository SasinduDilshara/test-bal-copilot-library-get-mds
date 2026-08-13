# ballerina/math.vector 1.2.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/math.vector` |
| Pinned version | `1.2.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-math.vector |
| Tag reviewed | `v1.2.0` (commit `4ccfe8c24d15d841748f14b9df8492d9ec970f96`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/math.vector/1.2.0` (source: distribution 2201.13.4) |
| Old render | `101` lines |
| New render | `101` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`old` and `new` are **byte-identical** at both pipeline stages — the stage-1 JSON and the stage-2
`.bal.txt` have the same MD5 on both sides. Spec v2 changed nothing for this library, which is
expected: `math.vector` declares no error types, no untagged objects, no classes, no clients and no
services, so none of the `renderTypeDef` degradation paths that spec v2 repairs are exercised here.
Both renders contain `0` `// Unknown type:` lines and `0` version-qualified type refs.

The render is complete and accurate against the pinned library: all 6 public declarations in the
default (and only) module are present with correct signatures. Three cosmetic fidelity gaps exist
identically on both sides (dropped `isolated` qualifier, enum member order reversed, enum members
re-emitted as standalone `const string` definitions). None are regressions and none change the
semantics an LLM would infer.

## 2. Change inventory

| Metric | `old` | `new` |
|---|---|---|
| Render lines (`wc -l`) | 101 | 101 |
| JSON lines (`wc -l`) | 185 | 185 |
| Render MD5 | `26010fbf378c224d39b788e5585d12bd` | `26010fbf378c224d39b788e5585d12bd` |
| JSON MD5 | `335b25500dc93afd860ffcd455b9e5ad` | `335b25500dc93afd860ffcd455b9e5ad` |
| `// Unknown type:` lines | 0 | 0 |
| Version-qualified refs (`mod:x.y.z:T`) | 0 | 0 |
| Section markers (`// --- `) | 4 | 4 |
| Function stubs | 5 | 5 |
| Enums | 1 | 1 |
| Constants | 2 | 2 |
| Records / classes / clients / services / annotations / listeners | 0 | 0 |

`diff old/ballerina_math.vector.json new/ballerina_math.vector.json` → exit 0, no output.
`diff` of the two `.bal.txt` files → no output.

Declarations added: **0**. Removed: **0**. Modified: **0**.

Both renders carry the same 4 sections: README (lines 7–20), `// --- Types ---` (22), `// --- Functions ---` (36).

## 3. Correctness against library source

Upstream `ballerina/vector.bal` at tag `v1.2.0` is **byte-identical** to the bala's
`any/modules/math.vector/vector.bal` (`diff` → no output), so GitHub and the bala agree; no
tie-break needed.

The source declares exactly 6 public symbols (`grep -nE "^public " src/ballerina/vector.bal`):

| Source line | Source declaration | Rendered as (both sides) | Verdict |
|---|---|---|---|
| 20 | `public enum NormType { L1, L2 }` | `enum NormType { L2, L1 }` (render 31–34) | Present; member order reversed |
| 36 | `public isolated function vectorNorm(float[] v, NormType norm) returns float` | `function vectorNorm(float[] v, NormType norm) returns float;` (render 49) | Params, param types, return type exact; `public`/`isolated` dropped |
| 63 | `public isolated function dotProduct(float[] v1, float[] v2) returns float` | `function dotProduct(float[] v1, float[] v2) returns float;` (render 62) | Exact |
| 86 | `public isolated function cosineSimilarity(float[] v1, float[] v2) returns float` | `function cosineSimilarity(float[] v1, float[] v2) returns float;` (render 75) | Exact |
| 108 | `public isolated function euclideanDistance(float[] v1, float[] v2) returns float` | `function euclideanDistance(float[] v1, float[] v2) returns float;` (render 88) | Exact |
| 131 | `public isolated function manhattanDistance(float[] v1, float[] v2) returns float` | `function manhattanDistance(float[] v1, float[] v2) returns float;` (render 101) | Exact |

This library is small enough to check exhaustively — every public declaration was verified
line-by-line against the bala source, not spot-checked.

Doc comments: all five function docstrings, including the fenced ` ```ballerina ` example blocks and
the `+ param -` / `+ return -` tags, are reproduced verbatim from source (compare source lines 25–35
against render lines 38–48, etc.). The `⇒` character in the examples survives intact in both the
JSON and the render — no mojibake. The `NormType` enum docstring (source 17–19) is reproduced at
render 28–30.

README: the render's README block (lines 8–19) is identical to `any/docs/README.md` and to the
`readme` field returned by Central for `ballerina/math.vector/1.2.0`; the only `diff` hit is the
absence of a trailing newline in the bala file.

Package description line (render line 3) matches Central's `summary` field verbatim.

`float[]` — the only composite type in the API — renders correctly as `float[]` in every position;
there is no other package's type in this API surface, so the foundational-type concern flagged in
the batch addendum (`sql:Error`, `time:Utc`, …) does not apply. `dependency-graph.json` confirms
`math.vector` has **zero** dependencies and imports nothing.

## 4. Regressions

**None found.**

Basis for that conclusion: the `new` render and the `new` stage-1 JSON are byte-identical to `old`
(identical MD5s, empty `diff` at both stages). There is therefore no declaration, parameter,
default, return type, docstring, annotation or README fragment that could have been dropped,
truncated or mangled by spec v2 for this library — the transformation was a no-op. I additionally
confirmed independently that both sides carry 5 function stubs, 1 enum, 2 constants, 4 section
markers, 0 `// Unknown type:` lines and 0 version-qualified type refs, so the identity is not an
artifact of comparing the wrong files.

## 5. Issues in `new` (independent of `old`)

Three fidelity gaps, all cosmetic, all present identically in `old` (so none is a regression), listed
because §5 asks for accuracy against the library regardless of `old`:

1. **`isolated` qualifier dropped from all 5 functions.** Source declares
   `public isolated function vectorNorm(...)` (vector.bal:36); the render emits
   `function vectorNorm(...)` (render:49). Same for the other four. An LLM reading this render cannot
   tell these functions are callable from an `isolated` context — relevant because `math.vector` is a
   leaf utility likely invoked inside isolated service methods. The stage-1 JSON carries no
   `isolated` flag at all (`"type": "Normal Function"` is the only qualifier field), so this is lost
   at extraction, not at render.
2. **Enum member order reversed.** Source is `{ L1, L2 }` (vector.bal:20–23); both JSON
   (`members: [L2, L1]`) and render (`enum NormType { L2, L1 }`, render:31–34) invert it. Semantically
   inert in Ballerina — enum members are order-independent — but it is a needless divergence from the
   published source.
3. **Enum members re-emitted as standalone constants.** The render prepends
   `const string L1 = "L1";` and `const string L2 = "L2";` (render:24, 26) ahead of the `NormType`
   enum. These correspond to no separate declaration in the source; they are the desugared enum
   members surfaced by the semantic API as `"type": "Constant"` typeDefs. The values are correct
   (a Ballerina enum member *is* a string constant), but the duplication is noise and could nudge a
   consumer toward `string`-typed usage instead of `vector:NormType`. Both constants render with an
   empty docstring (`"description": ""` in the JSON), so they carry no explanatory text either.

No invented symbols, no wrong types, no broken doc text, no encoding issues found.

## 6. Coverage gaps vs. the library

**Zero.** The package exports exactly one module (`export: ["math.vector"]` in `package.json`;
Central's `modules` array lists only `math.vector`), and that module is the default module, so the
`pkg.getDefaultModule()`-only extraction limitation shared by both sides costs nothing here.

The bala's `modules/` directory contains a single file, `math.vector/vector.bal`. All 6 public
symbols in it appear in both renders (table in §3). No public symbol is absent from the renders, and
there is no submodule-only API to report separately.

## 7. Compiler plugin

**None.** `has_plugin: false` in the manifest, confirmed two ways:

- The bala root `any/` contains only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
  `package.json` — there is no `compiler-plugin/` directory and no `compiler-plugin.json`.
- `find` for `*compiler-plugin*` / `*compiler_plugin*` across the entire upstream clone at `v1.2.0`
  returns nothing; `settings.gradle`/`build.gradle` define no plugin subproject.

Nothing the library implies should surface via a plugin (code actions, validations, generated
artifacts, plugin-driven annotations) is therefore missing — there is none to miss. The render's
empty `annotations: []` is correct.

## 8. Other considerations

- **Not deprecated.** Central returns `"isDeprecated": false`, `"deprecateMessage": ""`.
- **Stable version.** `1.2.0`, post-1.0, `graalvmCompatible: "Yes"`, `pullCount` 3870.
- **Distribution skew, benign.** The package was built against `2201.12.0` (`Ballerina.toml`
  `distribution`, `package.json` `ballerina_version`) but the bala consumed by the pipeline is the
  one bundled in distribution `2201.13.4`. Contents are unaffected — the bala's `vector.bal` is
  byte-identical to the `v1.2.0` tag.
- **Size / token cost is negligible.** 101 lines, ~3.4 KB of render for a 6-symbol API; there is no
  truncation pressure and no reason to trim.
- **Doc quality is high.** Every public function carries a description, a runnable ` ```ballerina `
  example with the expected result, per-parameter docs and a return doc — all preserved. This is one
  of the better-documented renders an LLM will encounter.
- **Render stubs are not compilable Ballerina** (bodiless `function f(...) returns float;` without
  `external`), but that is the pipeline's stub convention applied uniformly to every library, not a
  defect specific to `math.vector`.
- **Panics are undocumented.** `dotProduct`, `euclideanDistance`, `manhattanDistance` `panic error(...)`
  on length mismatch and `cosineSimilarity` panics on zero vectors (vector.bal:64, 87–88, 109, 132),
  but the source docstrings say nothing about it, so neither render can. Not a pipeline issue — an
  upstream doc gap — but worth knowing, since an LLM generating code from this render has no signal
  that these functions can panic rather than return an `error`.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l` on both renders and both JSONs | old render 101, new render 101, old JSON 185, new JSON 185 |
| 2 | `md5 -q old/…bal.txt new/…bal.txt` | both `26010fbf378c224d39b788e5585d12bd` — identical |
| 3 | `md5 -q old/….json new/….json` | both `335b25500dc93afd860ffcd455b9e5ad` — identical |
| 4 | `diff old/….json new/….json` | exit 0, no output |
| 5 | `diff` of the two `.bal.txt` files | no output |
| 6 | `grep -c '^// Unknown type:'` both renders | 0 and 0 |
| 7 | `grep -cE '[a-z_.]+:[0-9]+\.[0-9]+\.[0-9]+:'` both renders | 0 and 0 |
| 8 | `grep -c '^function '` both renders | 5 and 5 |
| 9 | `grep -c '^// --- '` both renders | 4 and 4; markers at lines 7, 20, 22, 36 |
| 10 | `ls` bala root `…/1.2.0/any` | `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json` — no `compiler-plugin/` |
| 11 | `ls` bala `modules/` | single dir `math.vector`, single file `vector.bal` |
| 12 | `cat` bala `package.json` | `version 1.2.0`, `export: ["math.vector"]`, `ballerina_version 2201.12.0`, `platform any` |
| 13 | `cat` bala `dependency-graph.json` | zero dependencies, single module |
| 14 | `git ls-remote --tags …module-ballerina-math.vector` | `refs/tags/v1.2.0` present (peeled `4ccfe8c2…`) |
| 15 | `git clone --depth 1 --branch v1.2.0` | HEAD `4ccfe8c24d15d841748f14b9df8492d9ec970f96` |
| 16 | `diff src/ballerina/vector.bal bala/modules/math.vector/vector.bal` | no output — identical |
| 17 | `grep -nE "^public " src/ballerina/vector.bal` | 6 hits: lines 20, 36, 63, 86, 108, 131 |
| 18 | `cat src/ballerina/Ballerina.toml` | org `ballerina`, name `math.vector`, version `1.2.0`, distribution `2201.12.0` |
| 19 | `grep version src/gradle.properties` | `version=1.2.0`, `ballerinaLangVersion=2201.12.0` |
| 20 | `find src -iname "*compiler-plugin*" -o -iname "*compiler_plugin*"` | no matches |
| 21 | `diff` bala `docs/README.md` vs render lines 8–19 | identical except trailing newline |
| 22 | Central API `…/registry/packages/ballerina/math.vector/1.2.0` | `isDeprecated:false`, one module `math.vector`, `graalvmCompatible:Yes`, `pullCount:3870`, summary matches render line 3 |
| 23 | Read `new/….json` in full (185 lines) | `clients: []`, `services: []`, `annotations: []`, 3 typeDefs (2 Constant, 1 Enum), 5 functions |
| 24 | Read both renders in full (101 lines each) | signature-by-signature match to §3 table |
| 25 | Read `OLD_AND_NEW_DIFFS/math.vector_diff.md` | claims 0 added / 0 removed / 0 hunks, "files are identical" — independently confirmed by checks 2–5 |

## 10. Caveats and unverified items

- The precomputed diff's claims were re-derived independently (checks 2–5), so nothing was taken on
  its word.
- I did not execute the render pipeline myself; the audit compares the committed `old`/`new`
  artefacts against the bala and upstream source. Given that both sides are byte-identical, a
  re-run could not change the regression verdict for this library.
- The `PIN_OK` determination for both sides is stated in the brief and was not re-derived from the
  render generation logs; however, the render's content is consistent with `1.2.0` (the bala at
  `1.2.0` reproduces every rendered signature and the README exactly), so a version mismatch is
  effectively excluded.
- The three fidelity gaps in §5 are attributed to stage-1 extraction rather than stage-2 rendering
  based on inspecting the stage-1 JSON (which already lacks `isolated`, already lists members in
  `L2, L1` order, and already contains the two Constant typeDefs). I did not read the
  `CopilotLibraryManager` Java source to confirm the mechanism, so that attribution is inference
  from the artefacts, not from the extractor code.

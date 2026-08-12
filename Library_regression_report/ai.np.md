# ballerina/ai.np 0.5.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/ai.np` |
| Pinned version | `0.5.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-ai.np |
| Tag reviewed | `v0.5.1` (commit `fb20ff7393f8c76224b60d57c6cb8dfcdde83787`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/ai.np/0.5.1/java21` |
| Old render | `60` lines |
| New render | `60` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

`ballerina/ai.np` is a compiler-plugin-only package. Its single exported module `ai.np` contains
exactly one source file, `modules/ai.np/main.bal`, whose entire content is the 15-line Apache
licence header — zero declarations of any kind. All functionality lives in the Java compiler plugin
(`ai.np-compiler-plugin-0.5.1.jar`), which rewrites `natural` expressions and `@natural:code`
external function bodies at compile time.

Consequently both renders contain no API at all: a 6-line header/import preamble plus the verbatim
README block. The `old` and `new` renders are **byte-identical** (same MD5), and so are the two
intermediate JSONs. There is nothing for spec v2 to improve or to break here.

## 2. Change inventory

| metric | old | new |
|---|---|---|
| lines | 60 | 60 |
| MD5 (`.bal.txt`) | `92223ba02fe73a1af6f8e34712b2b01f` | `92223ba02fe73a1af6f8e34712b2b01f` |
| MD5 (`.json`) | `6b617790ca69dc28e63ab99a8e58cc60` | `6b617790ca69dc28e63ab99a8e58cc60` |
| `typeDefs` | 0 | 0 |
| `clients` | 0 | 0 |
| `functions` | 0 | 0 |
| `services` | 0 | 0 |
| `annotations` | 0 | 0 |
| `// Unknown type:` lines | 0 | 0 |

`diff -u old/ballerina_ai.np.bal.txt new/ballerina_ai.np.bal.txt` → exit 0, no output.
`diff old/ballerina_ai.np.json new/ballerina_ai.np.json` → exit 0, no output.

Declarations added: **0**. Removed: **0**. Modified: **0**.

(The 5 lines in the render that match a declaration regex — `const int COUNT`, `type Employee`,
`type Department`, `public function main`, `function printEmployeeDataByDepartment` — are all inside
the fenced Ballerina snippet in the README, not extracted API. Verified by reading lines 16–52 of
the render.)

## 3. Correctness against library source

- Header comment and `description` field match the Central `summary` for `ballerina/ai.np/0.5.1`
  character-for-character (checked against
  `https://api.central.ballerina.io/2.0/registry/packages/ballerina/ai.np/0.5.1`).
- README block in the render matches `bala .../java21/docs/README.md` exactly except for one extra
  trailing blank line carried in the JSON `readme` value (`diff` reported only `52d51 < `). Identical
  on both sides; cosmetic.
- `import ballerina/ai.np;` is emitted (render line 5). The module genuinely exists and is the sole
  export listed in `package.json` (`"export": ["ai.np"]`) and in Central's `modules` array.
- No API is rendered, and none should be: `bala .../modules/ai.np/main.bal` is 15 lines of licence
  comment only. Upstream `ballerina/main.bal` at tag `v0.5.1` is byte-equivalent in content — also
  licence-header-only. Bala and GitHub agree.

Since the library's public surface is empty, the correctness check is exhaustive, not a spot-check.

## 4. Regressions

**None found.** Basis:
- The two `.bal.txt` files hash identically, so no declaration, parameter, default, return type,
  doc string, annotation, or README line can have been dropped or altered.
- The two `.json` files hash identically, so the divergence is not merely masked by the renderer.
- Neither render contains `// Unknown type:` lines, so the spec-v2 degradation class that affects
  other libraries does not apply here (there are no `Error`/object/`Other` type defs to degrade).

## 5. Issues in `new` (independent of `old`)

None that are factual errors. Two observations, both shared with `old` and both inherent to the
library rather than the renderer:

1. The render conveys no usable API surface. An LLM reading it learns only the README. That is an
   accurate reflection of the package, but it also means the `@natural:code` annotation and the
   `const natural { ... }` / `natural { ... }` expression forms shown in the README are *not*
   backed by any extracted symbol — they are lang-library constructs (`ballerina/lang.natural`,
   confirmed at `compiler-plugin/src/main/java/.../Commons.java:57`), not `ai.np` declarations.
   The render therefore cannot be used to resolve `natural:code`; that would require rendering
   `ballerina/lang.natural`, a different package.
2. `import ballerina/ai.np;` at render line 5 is a template artefact. Since the module exports
   nothing, a generated program containing that import and no other use of the prefix would fail
   compilation with an unused-import diagnostic. In real projects `ai.np` is added as a dependency
   in `Ballerina.toml` (the plugin runs off the dependency), not imported — none of the upstream
   `examples/` or `ballerina-tests/` `.bal` files import `ballerina/ai.np`. This is a pre-existing
   renderer convention present identically in `old`, not a spec-v2 change.

## 6. Coverage gaps vs. the library

**0 gaps.** The default module `ai.np` exports zero public symbols (`modules/ai.np/main.bal` is
licence-only), so there is nothing the renders could be missing.

Submodule-only API: **none**. `bala .../modules/` lists exactly one directory, `ai.np`, matching
`dependency-graph.json` (one module) and Central's `modules` array (one entry). The known
`getDefaultModule()`-only limitation is therefore inapplicable to this library.

## 7. Compiler plugin

`compiler-plugin/compiler-plugin.json` declares `io.ballerina.lib.ai.np.compilerplugin.CompilerPlugin`
with two jars (`ai.np-compiler-plugin-0.5.1.jar`, `ballerina-to-openapi-2.3.0.jar`).

What it contributes (from the upstream `compiler-plugin/src/main/java/io/ballerina/lib/ai/np/compilerplugin/`
sources and the jar's class listing):

- **Code modification tasks**, not code actions: `CompileTimePromptAsCodeCodeModificationTask`
  (expands `const natural { ... }` and `@natural:code` external functions by calling the codegen
  service) and `RuntimePromptAsCodeCodeModificationTask` (rewrites runtime `natural` expressions and
  generates the JSON schema for the expected type via `NaturalExpressionSchemaGenerator` /
  `TypeDefinitionModifier`).
- **Validators**: `Validator`, `ConstantExpressionValidator`, `AllowedConstructValidator`,
  `CodeGenerationValidator`.
- **Diagnostics** (`diagnostics.properties` in the jar, 2 messages):
  `error.non.json.expected.type.not.yet.supported` and
  `error.code.gen.with.code.annot.not.supported.in.single.bal.file.mode`.

Nothing the plugin implies is expressible as a rendered declaration — it defines no Ballerina-level
annotation or type of its own (the `code` annotation belongs to `ballerina/lang.natural`). So no
plugin-implied symbol is absent from the render. The render does, however, omit any hint that this
package is plugin-only and that `BAL_CODEGEN_URL`/`BAL_CODEGEN_TOKEN` gate its behaviour — except
that the README block does state the env-var requirement (render lines 54–58), so this is covered.

## 8. Other considerations

- **Pre-1.0**: version `0.5.1` is unstable; API may change without semver guarantees.
- **Deprecation**: `isDeprecated: false`, empty `deprecateMessage` (Central API).
- **Distribution skew**: `Ballerina.toml` at tag `v0.5.1` declares `distribution = "2201.11.0"`
  while the published bala's `package.json` records `ballerina_version: 2201.13.0`. Normal — the
  bala records the builder's distribution. Does not affect the render.
- **Size/token cost**: 60 lines, ~2.6 KB JSON. Negligible either side; identical.
- **Doc quality**: README is complete and self-contained, with a working end-to-end example. It is
  the only useful content in the render, and it survives intact.

## 9. Evidence log

| check | result |
|---|---|
| `wc -l old/ballerina_ai.np.bal.txt new/ballerina_ai.np.bal.txt` | 60 / 60 |
| `diff -u old/*.bal.txt new/*.bal.txt` | exit 0, no output |
| `diff old/*.json new/*.json` | exit 0, no output |
| `md5` of both `.bal.txt` | both `92223ba02fe73a1af6f8e34712b2b01f` |
| `md5` of both `.json` | both `6b617790ca69dc28e63ab99a8e58cc60` |
| `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| `grep -n '^// --- '` new render | lines 7 (`README`), 60 (`END README`) — only sections |
| JSON key summary (python) both sides | `typeDefs/clients/functions/services/annotations` all len 0 |
| `ls -R` bala `0.5.1/java21` | `modules/ai.np/main.bal` is the only `.bal` file |
| `Read` bala `modules/ai.np/main.bal` | 15 lines, licence header only, no declarations |
| `cat` bala `package.json` | `"export": ["ai.np"]`, `ballerina_version 2201.13.0`, graalvmCompatible |
| `cat` bala `dependency-graph.json` | 1 package, 1 module, no dependencies |
| `cat` bala `compiler-plugin/compiler-plugin.json` | plugin class + 2 jars |
| `unzip -l` plugin jar | 29 entries; classes listed in §7; `diagnostics.properties` present |
| `unzip -p` jar `diagnostics.properties` | 2 error messages (quoted in §7) |
| `git ls-remote --tags <repo>` | `v0.5.1` → `7f35234…`, peeled `fb20ff7…` |
| `git clone --depth 1 --branch v0.5.1` | succeeded into scratch `work/ai.np/src` |
| `cat src/ballerina/main.bal` | licence header only — matches bala |
| `cat src/ballerina/Ballerina.toml` | org/name/version `ballerina/ai.np/0.5.1`, `distribution = 2201.11.0` |
| `ls src/compiler-plugin/src/main/java/.../compilerplugin/` | 11 Java sources (listed in §7) |
| `grep -n 'lang.natural' Commons.java` | line 57 — `natural:code` is a `ballerina/lang.natural` construct |
| `grep -rn 'import' examples/ ballerina-tests/ *.bal` | no file imports `ballerina/ai.np` |
| Central API `packages/ballerina/ai.np/0.5.1` | `isDeprecated: false`, 1 module `ai.np`, summary matches render header |
| `diff <(json readme) bala/docs/README.md` | only `52d51 <` (one trailing blank line) |
| `cat OLD_AND_NEW_DIFFS/ai.np_diff.md` | claims 0 added / 0 removed / 0 hunks — independently confirmed above |

## 10. Caveats and unverified items

- The renders were not recompiled from the two `ballerina-vscode` sources; the audit takes the
  supplied `old/` and `new/` artefacts as given. Their byte-identity is verified directly.
- The compiler plugin's runtime behaviour (the codegen HTTP call, schema generation output) was not
  executed — it requires `BAL_CODEGEN_URL`/`BAL_CODEGEN_TOKEN` and a live service. Plugin claims in
  §7 come from reading the Java sources at tag `v0.5.1` and the jar's class/resource listing only.
- The claim that a generated program containing a bare `import ballerina/ai.np;` would raise an
  unused-import diagnostic is inferred from the module having zero exported symbols; it was not
  confirmed by running `bal build`.

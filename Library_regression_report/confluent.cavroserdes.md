# ballerinax/confluent.cavroserdes 1.0.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/confluent.cavroserdes` |
| Pinned version | `1.0.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-confluent.cavroserdes |
| Tag reviewed | `v1.0.3` (exact match, commit `250588af980a92d3fb3bb760f517c10b4d79c387`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/confluent.cavroserdes/1.0.3/java21` |
| Old render | `94` lines |
| New render | `95` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

Tiny library: one exported module (`confluent.cavroserdes`), three public symbols (`Error`, `serialize`,
`deserialize`). The entire old↔new delta is a single hunk: `old`'s degraded `// Unknown type: Error`
placeholder is replaced in `new` by a real definition with its doc comment. Everything else — README
block, both function signatures, docs, the `// Special Agent Note` external-type annotations — is
byte-identical. Nothing was dropped, truncated, or made less accurate. `new` is strictly better.

Both renders share pre-existing inaccuracies against the library source (`typedesc<anydata> targetType = <>`
rendered as `anydata targetType = anydata`; `isolated`/`public`/`distinct` qualifiers dropped). These are
not regressions — see §5.

## 2. Change inventory

`diff -u old/ballerinax_confluent.cavroserdes.bal.txt new/ballerinax_confluent.cavroserdes.bal.txt`
→ 1 hunk, +2 / −1 lines.

```diff
@@ -71,7 +71,8 @@
 // --- Types ---

-// Unknown type: Error
+# Represents any error related to the module.
+type Error error;
```

| Kind | old | new | Δ |
|---|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Type definitions rendered | 0 | 1 (`Error`) | +1 |
| Module-level functions | 2 (`serialize`, `deserialize`) | 2 | 0 |
| Clients | 0 | 0 | 0 |
| Services / listeners | 0 | 0 | 0 |
| Enums / constants / annotations | 0 | 0 | 0 |
| `// --- section ---` markers | 4 | 4 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| README block | 61 lines | 61 lines | 0 |

**Added (1):** `type Error error;` (with its `#` doc line).
**Removed (0):** none.
**Modified (0):** no function, parameter, default, return type, or doc line changed. Verified — the
diff has exactly one hunk and it is confined to the `// --- Types ---` section.

JSON side, `diff -u old/*.json new/*.json` → one hunk only: `typeDefs[0]` gains `"baseType": "error"`.
`functions`, `clients`, `services`, `annotations`, `readme`, `description` are identical.

## 3. Correctness against library source

Bala module sources (`.../modules/confluent.cavroserdes/{client,error,init}.bal`) are byte-identical to
the upstream `v1.0.3` tag (`diff -r` clean, `ballerina/client.bal`, `ballerina/error.bal`). The bala
README (`docs/README.md`, 61 lines) is byte-identical to `ballerina/README.md` at the tag.

Complete public surface of the default module (`grep -n 'public ' ballerina/*.bal` at tag v1.0.3):

| Symbol | Source | In `old` | In `new` | Rendered signature accurate? |
|---|---|---|---|---|
| `public type Error distinct error;` | `ballerina/error.bal:18` | ✗ (`// Unknown type: Error`) | ✓ line 75 | Partially — `distinct` and `public` dropped (§5.1) |
| `public isolated function serialize(cregistry:Client registry, string schema, anydata data, string subject) returns byte[]\|Error` | `ballerina/client.bal:28-29` | ✓ | ✓ line 86 | Yes, except `isolated`/`public` (§5.3) |
| `public isolated function deserialize(cregistry:Client registry, byte[] data, typedesc<anydata> targetType = <>) returns targetType\|Error` | `ballerina/client.bal:48-51` | ✓ | ✓ line 95 | No — `targetType` type/default wrong on both sides (§5.2) |

Doc comments in both renders match the source doc comments verbatim (parameter lines `+ registry`,
`+ schema`, `+ data`, `+ subject`, `+ targetType` and the `+ return` lines) — checked against
`client.bal:21-27` and `client.bal:41-47`.

Correctly **excluded** from both renders (all non-public, so rightly absent):
`toBytes` (`client.bal:53`), `getId` (`client.bal:57`), `class Deserializer` (`client.bal:61`),
`init`/`setModule` (`init.bal:19,23`), `const SERIALIZATION_ERROR`/`DESERIALIZATION_ERROR`
(`error.bal:20-21`).

The one thing `new` adds — `Error` — genuinely exists at `ballerina/error.bal:18` with the doc text
shown. The new JSON field `"baseType": "error"` is correct: the source type is `distinct error`.

## 4. Regressions

**None found.**

What was checked to conclude this:
- Full unified diff of the two renders: exactly one hunk, +2/−1, entirely inside `// --- Types ---`.
  No line in `old` other than `// Unknown type: Error` is absent from `new`.
- `diff <(sort old) <(sort new)` equivalent via the JSON: the only removed content is the placeholder.
- Declaration sets compared: both renders carry the same 2 functions; `new` has 1 extra type. No
  declaration, parameter, default value, return type, or doc line present in `old` is missing in `new`.
- README section extracted from both renders and byte-compared to the bala `docs/README.md`
  (after trailing-whitespace strip): identical on both sides, 61 lines each. No README content lost.
- The `// Special Agent Note: Client FROM ballerinax/confluent.cregistry package` trailing annotations
  on both functions survive unchanged in `new`.
- Annotations: neither side has any (`annotations: []` in both JSONs); library declares none, so
  nothing lost.
- `grep -c '^// Unknown type:'`: old 1, new 0.

## 5. Issues in `new` (independent of `old`)

Five inaccuracies exist in `new` versus the library source. Items 5.2–5.5 are present identically in
`old` (shared, not caused by spec v2); 5.1 is new-side-only but replaces a strictly worse placeholder.

**5.1 — `distinct` and `public` dropped from `Error` (new-side only, low severity).**
Source: `public type Error distinct error;` (`ballerina/error.bal:18`).
Render line 75: `type Error error;`.
An LLM reading this cannot tell the error is `distinct`, so it may write `error` where a
`cavroserdes:Error` is required, or assume any `error` value matches `Error`. Still a large net
improvement over `old`'s `// Unknown type: Error`, which conveyed nothing at all.

**5.2 — `deserialize` `targetType` parameter is wrong on both sides (highest-severity item in this render).**
Source (`ballerina/client.bal:48`): `typedesc<anydata> targetType = <>`.
Both renders: `anydata targetType = anydata`.
Two errors: the parameter type is `typedesc<anydata>`, not `anydata`; and the inferred-default marker
`<>` is rendered as the literal token `anydata`, which is not a valid expression in that position. An
LLM could emit `cavroserdes:deserialize(registry, bytes, anydata)`, which does not compile. The
underlying JSON is the source of this on both sides (`"type":{"name":"anydata"}, "default":"anydata"`),
so it is an extractor limitation shared by `main` and spec v2 — **not** a regression.

**5.3 — `isolated` qualifier dropped from both functions (both sides).**
Source has `public isolated function` for both `serialize` and `client.bal:28`/`deserialize`
`client.bal:48`; renders emit bare `function`. Loses the isolation contract relevant to concurrent use.

**5.4 — `public` qualifier absent from every declaration (both sides).**
All three rendered symbols are `public` in source; the render omits the modifier. Consistent
render-wide convention rather than a per-library defect, but it means the text is not directly
copy-pasteable as module source.

**5.5 — `cregistry:Client` is referenced without a corresponding import (both sides).**
The render's only `import` is `import ballerinax/confluent.cavroserdes;` (line 5). Both function
signatures reference `cregistry:Client` with no `import ballerinax/confluent.cregistry;`. Partially
mitigated by the trailing `// Special Agent Note: Client FROM ballerinax/confluent.cregistry package`
comment, which names the owning package. Related: the file is not compilable Ballerina anyway — the
raw README markdown is inlined between the import and the declarations (lines 8–68).

No invented symbols, no broken doc text, no encoding issues found in `new`.

## 6. Coverage gaps vs. the library

**Zero coverage gaps.**

- `package.json` `export` lists exactly one module: `confluent.cavroserdes`. `modules/` in the bala
  contains only `confluent.cavroserdes/`. Central metadata for `1.0.3` lists exactly one module.
  → There are no submodules, so the shared `getDefaultModule()`-only limitation costs nothing here.
- Public symbols in the default module: `Error`, `serialize`, `deserialize` (3 total). All 3 appear in
  `new`; 2 of 3 in `old` (`Error` degraded to a placeholder).
- No public symbol exported by the default module is absent from `new`.

## 7. Compiler plugin

The package ships **no compiler plugin**. Verified two ways:
- `find src -iname '*compiler-plugin*'` at tag `v1.0.3` → no results. Repo top level is
  `ballerina/`, `native/`, `examples/`, `build-config/`, `docs/`, `gradle/` only.
- The bala contains no `compiler-plugin/` directory (`ls` of the `java21` root shows
  `bala.json`, `dependency-graph.json`, `docs`, `modules`, `package.json`, `platform`).

The only Java artifact is the runtime native jar (`platform/java21/confluent.cavroserdes-native-1.0.3.jar`,
declared in `Ballerina.toml` `[[platform.java21.dependency]]`), which backs the `@java:Method` externals
`deserialize`, `toBytes`, `getId`, `setModule` — runtime code, not a plugin. Nothing plugin-implied
(code actions, validations, generated artifacts, plugin-defined annotations) is therefore missing from
the render.

## 8. Other considerations

- **Not deprecated.** Central metadata for `1.0.3`: `deprecateMessage` empty, no `deprecated` flag.
  Stable 1.x release, `pullCount` 7964, `graalvmCompatible: true`, bala format `3.0.0`.
- **Distribution / dependency drift is not a render concern here:** the bala was built against
  `2201.11.0` and pins `ballerinax/confluent.cregistry` `0.4.4` (`dependency-graph.json`), while the
  review list pins `confluent.cregistry` at `0.4.5` separately. This affects neither render; the
  `cregistry:Client` reference is emitted as an unresolved external link on both sides.
- **Size/tokens:** 95 lines, of which 61 (64%) are the inlined README. Negligible token cost; spec v2
  adds 1 net line.
- **README quality is good** — includes a runnable Quickstart. One pre-existing upstream typo is
  faithfully carried into both renders: `cregistry:Client registry = ; // instantiate a schema registry client`
  (line 39) has an empty initializer and would not compile. That is the library's own README text,
  identical in the bala and at the tag; the renderer reproduced it correctly. Worth flagging because an
  LLM may copy it.
- The README quickstart also uses the alias `cavroserdes:` while the render's import line is
  `import ballerinax/confluent.cavroserdes;` — the alias is implicit in Ballerina (last dotted segment),
  so this is correct, just not obvious.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | old 94, new 95 |
| 2 | `diff -u old/*.bal.txt new/*.bal.txt` | 1 hunk, +2/−1, at `@@ -71,7 +71,8 @@`, inside `// --- Types ---` |
| 3 | `diff -u old/*.json new/*.json` | 1 hunk: `typeDefs[0]` gains `"baseType": "error"` |
| 4 | `grep -c '^// Unknown type:'` on both renders | old = 1, new = 0 |
| 5 | `ls -R` of bala `1.0.3` | single platform `java21`; `modules/` holds only `confluent.cavroserdes/` with `client.bal`, `error.bal`, `init.bal`; no `compiler-plugin/` |
| 6 | `cat` bala `package.json` | `export: ["confluent.cavroserdes"]`, `ballerina_version 2201.11.0`, `graalvmCompatible true`, `readme docs/README.md` |
| 7 | `git ls-remote --tags <repo>` | `v1.0.3` exists → `250588af980a92d3fb3bb760f517c10b4d79c387` |
| 8 | `git clone --depth 1 --branch v1.0.3` into scratch `src` | success |
| 9 | `diff ballerina/client.bal <bala>/client.bal` and same for `error.bal` | identical (no output) — GitHub == bala |
| 10 | `grep -n 'public ' src/ballerina/*.bal` | `error.bal:18 public type Error distinct error;`; `client.bal:28 public isolated function serialize(...)`; `client.bal:48 public isolated function deserialize(... typedesc<anydata> targetType = <>)` — exactly 3 public symbols |
| 11 | `diff src/ballerina/README.md <bala>/docs/README.md` | identical |
| 12 | Python: README block extracted from each render vs bala `docs/README.md`, stripped | `True` for both old and new; 61 lines each; JSON `readme` field also matches |
| 13 | Python: JSON top-level list sizes | both sides: `typeDefs` 1 (`Error`), `clients` 0, `functions` 2 (`serialize`,`deserialize`), `services` 0, `annotations` 0 |
| 14 | `grep -n '^import' ` on both renders | only `import ballerinax/confluent.cavroserdes;` at line 5 (and line 30 inside the README code block); no `cregistry` import |
| 15 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerinax/confluent.cavroserdes/1.0.3` | 1 module (`confluent.cavroserdes`), `deprecateMessage` empty, `pullCount` 7964, `balaVersion` 3.0.0 |
| 16 | `find src -iname '*compiler-plugin*'` | no results |
| 17 | Read `new` render lines 1–95 in full; read bala `client.bal`/`error.bal`/`init.bal` in full | small enough for exhaustive review; findings in §3 and §5 |
| 18 | `cat OLD_AND_NEW_DIFFS/confluent.cavroserdes_diff.md` | claims (94/95 lines, +2/−1, 1 hunk, 1→0 unknown types, 1 type added, 0 removed, 0 version-qualified refs) all independently reproduced by checks 1–4 |

## 10. Caveats and unverified items

- **Not verified:** that `toSyntaxString` is *capable* of emitting `distinct`, `isolated`, or `public`
  for any library — I did not read the renderer source (out of scope: only the library folders and the
  bala/upstream sources were inspected). §5.1/§5.3/§5.4 are stated as facts about the rendered output
  versus the library source, not as claims about renderer intent.
- **Not verified:** whether the `targetType` mis-rendering (§5.2) originates in the Java extractor or
  the TypeScript renderer. What is verified is that both JSONs already contain
  `"type":{"name":"anydata"}` with `"default":"anydata"`, so the loss happens at or before JSON
  generation, identically on both sides.
- The native jar (`confluent.cavroserdes-native-1.0.3.jar`) was not decompiled; the `@java:Method`
  external bodies were not inspected. This does not affect the render, which only reflects Ballerina
  declarations.
- Everything else in the report is backed by a command in §9.

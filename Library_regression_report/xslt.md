# ballerina/xslt 2.9.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/xslt` |
| Pinned version | `2.9.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-xslt |
| Tag reviewed | `v2.9.1` (commit `e3e4d826378eddfd35ca175a5ed584cb806f03f8`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/xslt/2.9.1/java21` |
| Old render | `38` lines |
| New render | `39` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/xslt` is one of the smallest standard-library modules: its default (and only) module
exports exactly two public symbols — `public isolated function transform(...)` and
`public type TransformError distinct error;`. Both renders cover both symbols, so coverage is 100%
on both sides.

The single change from `old` to `new` is that the `TransformError` error type is no longer degraded
to a `// Unknown type: TransformError` placeholder; `new` emits a real definition with its doc
comment. Nothing was dropped, reworded, or truncated. One pre-existing renderer defect (a doc
continuation line emitted without its `#` prefix) is present identically on both sides and is
therefore not a regression, but it is recorded in §5 because it makes the emitted snippet
non-compiling Ballerina in `new` as well.

## 2. Change inventory

Line counts (`wc -l`): old `38`, new `39`. Unified diff is a single hunk, `+2 / −1`.

```diff
@@ -21,7 +21,8 @@
 // --- Types ---
-// Unknown type: TransformError
+# Represents an `xslt:TransformError` with the message and the cause.
+type TransformError error;
```

| Kind | old | new | Delta |
|---|---|---|---|
| Functions | 1 (`transform`) | 1 (`transform`) | unchanged, byte-identical |
| Types | 0 real (1 `// Unknown type:` placeholder) | 1 real (`type TransformError error;`) | **+1 real type def** |
| Classes / enums / consts / annotations / services / listeners / clients | 0 | 0 | unchanged |
| Section markers (`// --- `) | 4 | 4 | unchanged |
| `// Unknown type:` lines | 1 | 0 | **−1** |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | unchanged |
| README block | 14 lines, byte-identical to bala `docs/README.md` | same | unchanged |

Stage-1 JSON diff (structural, via `json.load` field comparison): every top-level key
(`name`, `description`, `readme`, `functions`, `clients`, `services`, `annotations`) compares
`SAME`; only `typeDefs` differs, and only by the addition of `"baseType": "error"` on the
`TransformError` entry. So the extractor change for this library is exactly one extra field, and
the renderer turns that field into a real type definition.

## 3. Correctness against library source

Sources checked: clone at tag `v2.9.1` (`ballerina/*.bal`) and the bala's
`modules/xslt/{init,natives,xslt_error}.bal` — the two agree byte-for-byte for the public API.

| Rendered declaration | Library source | Verdict |
|---|---|---|
| `function transform(xml input, xml xsl, map<string\|decimal\|xml> params = {}) returns xml\|error;` | `modules/xslt/natives.bal:29` — `public isolated function transform(xml input, xml xsl, map<string\|decimal\|xml> params = {}) returns xml\|error = @java:Method {...} external;` | Correct. Param names, order, the `{}` default on `params`, and the return type all match. `public`/`isolated`/`external` qualifiers are stripped by the renderer on both sides (render-format convention, not a data loss). |
| `# + input / + xsl / + params / + return` doc lines | `natives.bal:19-28` | Correct — text matches the source doc verbatim, including the ```` ```ballerina ```` example. |
| `# Represents an \`xslt:TransformError\` with the message and the cause.` / `type TransformError error;` | `modules/xslt/xslt_error.bal:17-18` — `public type TransformError distinct error;` | Doc string exact. Definition correct in substance; the `distinct` qualifier is not carried through (see §5). |
| README block | `docs/README.md` (11 lines) | Verified byte-identical: JSON `readme` field length 449 == bala README length 449, and a `difflib.unified_diff` between the two produced no output. |

No invented symbols: every identifier in `new` (`xslt`, `transform`, `TransformError`, `input`,
`xsl`, `params`) exists in the library source.

## 4. Regressions

**None found.**

What was checked to conclude that:
- Full text of both renders read line-by-line (38 and 39 lines — small enough for exhaustive review).
- `diff -u old new` yields exactly one hunk, which is purely additive (`−1` line is the
  `// Unknown type:` placeholder that the added real definition replaces).
- The `transform` function block (old lines 28–38 / new lines 29–39) is character-identical between
  the two files.
- The README block (lines 7–20 on both sides) is character-identical between the two files.
- Stage-1 JSON: all keys except `typeDefs` compare equal; `typeDefs` differs only by an *added*
  field. No parameter, default, doc string, or return type was removed or altered.
- No declaration present in `old` is missing from `new`: the declaration set of `old` is
  `{transform}` plus one placeholder, and `new` is a strict superset (`{transform, TransformError}`).

## 5. Issues in `new` (independent of `old`)

1. **`distinct` qualifier lost on `TransformError`** (new render line 25). Source is
   `public type TransformError distinct error;` (`xslt_error.bal:18`); the render says
   `type TransformError error;`. The stage-1 JSON carries only `"baseType": "error"` with no
   distinctness flag, so this is an extractor-level omission, not a renderer bug. Practical impact
   is low for an LLM consumer (the type is still shown as an error type usable in `xml|error`
   handling), but a consumer cannot tell that `TransformError` is a *distinct* error subtype and so
   cannot reason about `error is xslt:TransformError` narrowing precisely. Note this is strictly
   better than `old`, which emitted no definition at all — hence not a regression.

2. **Doc continuation line emitted without its `#` prefix** (new line 38, old line 37 — identical on
   both sides). The source doc wraps the `+ return` description over two lines; the extractor stores
   it as `"...`XML` object\ncannot be transformed"` and the renderer prefixes only the first line:
   ```
   37:[# + return - The transformed result represented in an XML object or else an `error` if the given `XML` object]
   38:[cannot be transformed]
   ```
   Line 38 is bare text sitting between a doc comment and a function signature, which is **not valid
   Ballerina** and could mislead a model that treats the render as compilable reference code. Shared
   with `old`, so not a regression, but still wrong in `new`.

3. `public` and `isolated` are not rendered on `transform`. Consistent renderer convention across
   both sides and, seemingly, across the whole corpus; noted for completeness rather than as a
   defect specific to this library.

## 6. Coverage gaps vs. the library

**None.** The bala's default module (`modules/xslt/`) contains three `.bal` files with exactly two
`public` declarations:

```
xslt_error.bal:18: public type TransformError distinct error;
natives.bal:29:    public isolated function transform(...) ... external;
```

Both appear in `new`. The remaining module-level functions — `init()` and `setModule()` in
`init.bal:19,23` — are non-public lifecycle/interop bindings and are correctly excluded from both
renders.

No submodule gap: `package.json` declares `"export": ["xslt"]`, the bala's `modules/` directory
contains only `xslt`, and Central metadata for `ballerina/xslt/2.9.1` lists a single module `xslt`.
The known `getDefaultModule()`-only limitation therefore costs this library nothing.

## 7. Compiler plugin

`has_plugin: false` in the manifest, confirmed against the bala: the bala root
(`.../2.9.1/java21/`) contains only `bala.json`, `dependency-graph.json`, `package.json`, `docs/`,
`modules/`, `platform/` — there is no `compiler-plugin/` directory and no
`compiler-plugin.json`. `package.json` declares no compiler-plugin entry. Nothing to report and
nothing plugin-implied is missing from the render.

## 8. Other considerations

- **Version/maturity**: 2.9.1, a stable post-1.0 standard-library module. Central reports
  `deprecated: null`, empty `deprecateMessage`, so it is not deprecated. Built against
  `ballerinaVersion 2201.12.0`; render pipeline ran on distribution 2201.13.4 — no mismatch problems
  observed.
- **Native implementation**: both public API entries are `external` Java bindings
  (`io.ballerina.stdlib.xslt.XsltTransformer`, backed by Saxon-HE 11.4 per `package.json`
  `platformDependencies`). The render correctly presents the Ballerina-level signature and does not
  leak `@java:Method` annotations.
- **Size / token implications**: negligible. 39 lines, ~2.1 KB of JSON. The +1 net line is the
  entire cost of the spec-v2 improvement here.
- **Doc quality**: good. The module doc, the `#` doc for `transform` with a runnable example, and
  the README all survive intact into the render.
- **Foundational-type concern (per batch addendum)**: `xslt:TransformError` is the only type other
  packages could depend on. It is rendered in `new` (absent as a definition in `old`), so on this
  axis `new` is strictly better; the only fidelity gap is `distinct` (§5.1).

## 9. Evidence log

| # | Check (command / file:line) | Result |
|---|---|---|
| 1 | `wc -l old/ballerina_xslt.bal.txt new/ballerina_xslt.bal.txt` | 38 / 39 |
| 2 | `cat -n` of both renders (full text, 38+39 lines) | Read in full; only difference is the Types section |
| 3 | `grep -c '^// Unknown type:'` on old / new | 1 / 0 |
| 4 | `grep -nE 'isolated\|distinct\|public'` on both renders | exit 1, no matches on either side |
| 5 | `git clone --depth 1 --branch v2.9.1 …`; `git log -1` | tag `v2.9.1` = `e3e4d826378eddfd35ca175a5ed584cb806f03f8` |
| 6 | `find <bala> -maxdepth 3` | Platform dir `java21`; contents: bala.json, dependency-graph.json, package.json, docs/, modules/, platform/ — **no compiler-plugin/** |
| 7 | `ls <bala>/modules` | single module `xslt` |
| 8 | `cat` of `<bala>/modules/xslt/{init,natives,xslt_error}.bal` | 3 files; full source read |
| 9 | `grep -nE '^\s*public ' <bala>/modules/xslt/*.bal` | 2 hits: `xslt_error.bal:18` (TransformError), `natives.bal:29` (transform) |
| 10 | `cat <bala>/package.json` | `export: ["xslt"]`, no compiler plugin, platform java21, Saxon-HE-11.4 dep |
| 11 | Python key-by-key comparison of old/new JSON | all keys SAME except `typeDefs` DIFF |
| 12 | `json.dumps` of both `typeDefs` | new adds `"baseType": "error"`; name/description/type identical |
| 13 | `json.dumps` of new `functions` | 3 params with correct names/types, `params` optional with default `{}`, return `xml\|error` |
| 14 | `difflib.unified_diff(bala docs/README.md, json.readme)` | no output — identical; lengths 449 == 449 |
| 15 | `awk` print of new lines 36–39 and old lines 35–38 | Confirms bare `cannot be transformed` line on both sides |
| 16 | `curl https://api.central.ballerina.io/2.0/registry/packages/ballerina/xslt/2.9.1` | deprecated `None`, 1 module `xslt`, ballerinaVersion 2201.12.0 |
| 17 | Read `OLD_AND_NEW_DIFFS/xslt_diff.md` and verified its claims against files | All claims confirmed (38/39 lines, +2/−1, 1 hunk, 1→0 unknown types, +1 type decl) |

## 10. Caveats and unverified items

- The `distinct` omission (§5.1) was localised to the stage-1 JSON (`typeDefs` has no distinctness
  field), but I did not read the `ModelToJsonConverter` / extractor source to confirm whether
  distinctness is representable in the spec-v2 schema at all. Whether this is "not modelled" or
  "modelled but not populated" is **unverified**.
- The claim that stripping `public`/`isolated` is a corpus-wide renderer convention is inferred from
  this library's two renders only; I did not check other libraries' renders to confirm it.
- Everything else in this report was verified directly against the bala, the tagged upstream clone,
  the two renders, the two JSONs, and Central metadata.

# ballerina/random 1.7.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/random` |
| Pinned version | `1.7.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-random |
| Tag reviewed | `v1.7.0` (commit `23e69075544e0cd93a464303ea4a2380a928ab35`, grafted) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/random/1.7.0` (source: distribution 2201.13.4, platform dir `java21`) |
| Old render | `43` lines |
| New render | `45` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/random` is a tiny standard-library module with exactly four public symbols in its single
(default) module: two error types and two functions. The only difference between `old` and `new` is
that the two `// Unknown type:` placeholders in `old` are replaced by real type definitions in `new`.
Nothing was removed, truncated, or reworded. Both functions, their full doc comments, parameter
docs, return docs and signatures are byte-identical across the two renders, and both match the bala
source exactly.

The improvement is real but partial: `new` emits `type Error error;` / `type ArithmeticError error;`
whereas the source declares `public type Error distinct error;` and
`public type ArithmeticError distinct Error;`. The `distinct` qualifier and the
`ArithmeticError <: Error` subtype relation are both flattened away. That is a fidelity limit of the
new emitter, not a regression — `old` conveyed strictly less (a bare name and no definition at all).

## 2. Change inventory

Line counts (`wc -l`): old 43, new 45. Net +2.

Full set of differing lines (`diff old new`) — 2 removed, 4 added, 1 hunk:

| Kind | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 2 (`Error`, `ArithmeticError`) | 0 |
| `type` declarations | 0 | 2 (`Error`, `ArithmeticError`) |
| doc comments on types | 0 | 2 |
| `function` declarations | 2 | 2 (identical text) |
| class / enum / const / annotation / service / listener / client | 0 | 0 |
| `// --- section ---` markers | 4 | 4 (README, END README, Types, Functions) |
| README block | 7 non-blank lines | identical |

Declarations added in `new` (2): `type Error`, `type ArithmeticError`.
Declarations removed in `new` (0) — the only `<` lines in the diff are the two placeholder comments.

JSON-level cause (`old/ballerina_random.json` vs `new/ballerina_random.json`): the two entries under
`typeDefs` are identical except that `new` adds `"baseType": "error"` to each. `functions`,
`clients`, `services`, `annotations`, `name`, `description`, `readme` are byte-identical between the
two JSONs. So the change is a single extractor field plus the corresponding renderer branch.

## 3. Correctness against library source

Default module public surface (from the bala, `modules/random/`; identical to upstream
`ballerina/` dir at tag `v1.7.0`):

| Symbol | Source | Rendered in `new` | Verdict |
|---|---|---|---|
| `createDecimal()` | `natives.bal:30` — `public isolated function createDecimal() returns float` | `function createDecimal() returns float;` (new:34) | correct modulo the renderer's global convention of dropping `public`/`isolated` (same in `old`) |
| `createIntInRange(int, int)` | `natives.bal:43` — `public isolated function createIntInRange(int startRange, int endRange) returns int\|Error` | `function createIntInRange(int startRange, int endRange) returns int\|Error;` (new:45) | correct; param names, order, types and return union all match |
| `Error` | `random_errors.bal:18` — `public type Error distinct error;` | `type Error error;` (new:21) | present, doc correct, but `distinct` dropped |
| `ArithmeticError` | `random_errors.bal:21` — `public type ArithmeticError distinct Error;` | `type ArithmeticError error;` (new:24) | present, doc correct, but `distinct` and the `Error` base dropped |

Doc comments: both function doc blocks in `new` reproduce `natives.bal:24-29` and `natives.bal:34-42`
verbatim, including the fenced ```ballerina examples and the `+ param -` / `+ return -` lines. Both
type doc comments reproduce `random_errors.bal:17` and `random_errors.bal:20` verbatim.

Correctly excluded module-private symbols (no `public` in source, absent from both renders — correct):
`a`, `c`, `m`, `x0` (`natives.bal:19-22`) and `lcg`, `currentTimeInMilliSeconds`, `nextFloat`,
`newSecureRandom`, `nextFloatExtern` (`natives.bal:50-77`). `grep -rn '^public' ballerina/*.bal` in
the tagged clone returns exactly the four symbols in the table above — the coverage is exhaustive.

README: `new` lines 8–15 match `docs/README.md` in the bala (7 lines) with only a trailing blank-line
difference; no content lost.

## 4. Regressions

**None found.** Basis for that conclusion:

- `diff old new` yields exactly one hunk; the only removed lines are
  `// Unknown type: Error` and `// Unknown type: ArithmeticError`. No declaration, parameter,
  default, return type, doc line, or README line appears in `old` and not in `new`.
- Declaration extraction (`grep -nE '^(public )?(function|type|class|enum|const|annotation|listener|service|isolated function)'`)
  gives `{createDecimal, createIntInRange}` for `old` and
  `{Error, ArithmeticError, createDecimal, createIntInRange}` for `new` — a strict superset.
- The two function blocks (doc + signature) are character-identical between the files.
- The four section markers are present in both, in the same order.
- No version/module-qualified type refs (`mod:1.2.3:Type`) in either side — 0 in both, so nothing to
  regress there.
- Rendered Ballerina is syntactically valid in `new`: `type X error;` is a legal type definition, and
  the previous `// Unknown type:` lines were comments, so both files parse.

Foundational-type note (per the batch addendum): `random`'s cross-package-visible type is
`random:Error`, which appears in `createIntInRange`'s return union. It is rendered as `int|Error` in
both sides, and in `new` it now additionally has a definition. Consumers of this render are strictly
better informed than before.

## 5. Issues in `new` (independent of `old`)

Two, both stemming from the same emitter limitation. Neither is a regression (both are also wrong or
worse in `old`), but both would mislead an LLM consuming the render.

1. **`distinct` qualifier dropped.** Source: `public type Error distinct error;`
   (`random_errors.bal:18`). Render: `type Error error;`. `distinct` is semantically load-bearing in
   Ballerina — it makes `Error` a nominal error type, so `error e = ...; e is random:Error` behaves
   differently than the render implies. A model reading this render could conclude any `error` value
   is assignable to `random:Error`.
2. **`ArithmeticError`'s base type flattened to `error`.** Source:
   `public type ArithmeticError distinct Error;` (`random_errors.bal:21`). Render:
   `type ArithmeticError error;`. The `ArithmeticError <: Error` relationship is invisible in the
   render, so a model cannot infer that catching `random:Error` also catches `random:ArithmeticError`.
   The JSON confirms the loss originates upstream of the renderer: both typeDefs carry the same
   `"baseType": "error"` — the extractor never records `Error` as the base.

No invented symbols, no wrong parameter/return types, no broken doc text, no encoding issues:
every identifier in `new` maps 1:1 to a declaration in the bala.

## 6. Coverage gaps vs. the library

**Zero.** The bala's `modules/` directory contains exactly one entry, `random`, i.e. the default
module — there are no submodules, so the shared `getDefaultModule()` limitation described in the
brief has no effect here. `package.json` lists `"export": ["random"]`, confirming the single-module
export set. All four public symbols of that module appear in `new`; two of the four appear only as
degraded placeholders in `old`.

## 7. Compiler plugin

None. `has_plugin` is `false` in the manifest, and this is confirmed on both sides:
`ls -R` over the bala shows only `bala.json`, `dependency-graph.json`, `docs/`, `modules/`,
`package.json` under `java21/` — there is no `compiler-plugin/` directory and no
`compiler-plugin.json`. `find . -iname '*compiler-plugin*' -maxdepth 3` in the tagged upstream clone
returns nothing. Nothing plugin-related is therefore expected in, or missing from, the render.

## 8. Other considerations

- **Stability**: `1.7.0` is a stable post-1.0 release; no deprecation markers in the bala sources or
  in either render.
- **Size/tokens**: 45 lines. Negligible token cost; the +2 lines are a good trade for eliminating two
  content-free placeholders.
- **Distribution provenance**: the bala is the one bundled with Ballerina `2201.13.4`; its
  `package.json` records `ballerina_version: 2201.12.0` and `graalvmCompatible: true`. Upstream tag
  `v1.7.0` and the bala's `.bal` files agree line-for-line, so there is no GitHub/bala divergence to
  arbitrate.
- **Renderer conventions applied uniformly**: `public` and `isolated` are absent from every rendered
  declaration on both sides. That is a global convention of this pipeline, not specific to `random`,
  and it is unchanged by spec v2.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_random.bal.txt new/ballerina_random.bal.txt` | 43 / 45 |
| `cat` both renders in full | full text reviewed (files are 43/45 lines) |
| `diff old new \| grep '^<'` | exactly 2 lines: `// Unknown type: Error`, `// Unknown type: ArithmeticError` |
| `grep -c '^// Unknown type:'` | old = 2, new = 0 |
| `grep -n '^// --- ' new/…` | 4 markers at lines 7, 16, 18, 26 |
| `grep -nE '^(public )?(function\|type\|class\|enum\|const\|annotation\|listener\|service\|isolated function)' old/…` | 2 hits (lines 32, 43) |
| same on `new/…` | 4 hits (lines 21, 24, 34, 45) |
| `grep -c 'distinct' new/…` | 0 |
| `ls -R <bala>` | `java21/{bala.json,dependency-graph.json,docs/,modules/,package.json}`; `modules/` = `random` only; no `compiler-plugin/` |
| `cat -n <bala>/java21/modules/random/natives.bal` | 77 lines; publics at 30 and 43 |
| `cat -n <bala>/java21/modules/random/random_errors.bal` | 21 lines; publics at 18 and 21 |
| `cat <bala>/java21/package.json` | version 1.7.0, `export: ["random"]`, platform java21 |
| `git clone --depth 1 --branch v1.7.0 …` + `git log -1` | tag `v1.7.0` resolved, commit `23e6907` |
| `grep -rn '^public' src/ballerina/*.bal` | 4 hits: `random_errors.bal:18,21`, `natives.bal:30,43` |
| `find src -iname '*compiler-plugin*' -maxdepth 3` | no output |
| Python dump + compare of `old/ballerina_random.json` vs `new/ballerina_random.json` | identical except `"baseType": "error"` added to both `typeDefs` entries |
| `diff` render README block vs `<bala>/java21/docs/README.md` | identical ignoring blank lines (README is 7 lines) |
| `OLD_AND_NEW_DIFFS/random_diff.md` claims (43/45 lines, +4/−2, 1 hunk, 2 types added, 0 removed, 2→0 unknowns, 0 version-qualified refs, 4→4 markers) | all independently reproduced above; no discrepancy |

## 10. Caveats and unverified items

- The clone is shallow/grafted (`--depth 1`), so no history was inspected; only the tree at tag
  `v1.7.0` was read. That tree matches the bala exactly, which is what matters for this audit.
- Neither render was compiled. Syntactic validity of `type Error error;` is asserted from the
  Ballerina grammar, not from a `bal build` run.
- Whether dropping `distinct` and the `ArithmeticError → Error` base is intentional in the spec v2
  design (e.g. deliberate simplification for LLM consumption) is unknown to me; I report it as a
  fidelity loss vs. the source without judging intent.
- `docs/` in the bala contains only `README.md` and `icon.png`; no API doc JSON was available to
  cross-check descriptions against, so doc text was verified against the `.bal` doc comments instead.

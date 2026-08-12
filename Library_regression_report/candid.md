# ballerinax/candid 0.2.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/candid` |
| Pinned version | `0.2.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-candid |
| Tag reviewed | `v0.2.1` (commit `d3232450d10e4617111b24e1045a2a8cbbeb5732`, peeled `fbac99c87950db52a30368002673966ba6a765dc`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/candid/0.2.1` |
| Old render | `133` lines |
| New render | `133` lines |
| Verdict | **NO REGRESSION** |

## 1. Summary

The `old` and `new` renders are **byte-identical** (same MD5), as are the two intermediate JSONs.
There is nothing for spec v2 to change here: `ballerinax/candid`'s default module (`modules/candid/candid.bal`)
is a **zero-byte file**, so the extractor — which reads only `pkg.getDefaultModule()` on both sides —
finds no type defs, no clients, no functions, no services and no annotations. Both renders therefore
consist solely of the package header plus the verbatim `Package.md` README (125 of 133 lines).

The library's entire public API — 140 public top-level declarations across `candid.charitycheckpdf`,
`candid.essentials` and `candid.premier` — is submodule-only and is absent from **both** renders. Per
the brief this is a shared, pre-existing extractor limitation, not a regression introduced by `new`.

## 2. Change inventory

| Kind | old | new | delta |
|---|---|---|---|
| Lines | 133 | 133 | 0 |
| `typeDefs` (JSON) | 0 | 0 | 0 |
| `clients` (JSON) | 0 | 0 | 0 |
| `functions` (JSON) | 0 | 0 | 0 |
| `services` (JSON) | 0 | 0 | 0 |
| `annotations` (JSON) | 0 | 0 | 0 |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Declarations added / removed / modified | — | — | **0 / 0 / 0** |

`diff -u old/ballerinax_candid.bal.txt new/ballerinax_candid.bal.txt` → exit 0, no output.
`diff old/ballerinax_candid.json new/ballerinax_candid.json` → exit 0, no output.
MD5 of both `.bal.txt`: `bc033839942f82b6b649063f492d364b`. MD5 of both `.json`: `1a7472874033cfc63e02d8dbf633f87e`.

The precomputed diff at `OLD_AND_NEW_DIFFS/candid_diff.md` (0 added, 0 removed, 0 hunks, "the two files
are identical") was verified against the files and is correct.

## 3. Correctness against library source

`new` adds nothing over `old`, so correctness reduces to verifying that an empty API surface is the
truthful rendering, and that the README content is accurate.

- Default module is genuinely empty in both sources of truth:
  - bala: `modules/candid/candid.bal` → `0` lines, `grep -cE '^public '` → `0`.
  - upstream tag `v0.2.1`: `ballerina/candid.bal` → `0` bytes (`wc -c`).
  So "no declarations" is correct, not a dropped extraction.
- README in the render is byte-equal to the bala's `docs/Package.md` (only the trailing blank line of
  my extracted slice differs), and `docs/Package.md` in the bala is byte-equal to `ballerina/Package.md`
  at tag `v0.2.1` (`diff` → exit 0). Central's `readme` field for `0.2.1` matches the same text.
- README code snippets spot-checked against the published submodule sources (all present and correct):
  - `charitycheckpdf:Client charitycheckpdf = check new (apiKeyConfig)` → `candid.charitycheckpdf/client.bal:29`
    `public isolated function init(ApiKeysConfig apiKeyConfig, ConnectionConfig config = {}, string serviceUrl = "https://apidata.guidestar.org/charitycheckpdf") returns error?`
  - `charitycheckpdf->/v1/pdf/["EMP-ID-NUM"]` → `candid.charitycheckpdf/client.bal:40` `resource isolated function get v1/pdf/[string ein](...) returns http:Response|error`
  - `essentials->/v3.post(query)` → `candid.essentials/client.bal:73` `resource isolated function post v3(V3Query payload, ...) returns V3EssentialsResponse|error`
  - `premier->/v3/["EMP-ID-NUM"]` → `candid.premier/client.bal:98` `resource isolated function get v3/[string ein](...) returns V3PublicProfile|error`
  - `ApiKeysConfig { subscriptionKey }` → `candid.charitycheckpdf/types.bal:20`, `candid.essentials/types.bal:874`, `candid.premier/types.bal:2252` — all `record {| string subscriptionKey; |}`.

## 4. Regressions

**None found.**

Basis for that conclusion: the two render files and the two JSON files are byte-identical (MD5 above,
`diff` exit 0 on both pairs). No declaration, parameter, default, return type, doc line, README line,
annotation or section marker can have been dropped, truncated or mangled by `new`, because `new`
reproduces `old` exactly. No `// Unknown type:` lines existed in `old` to begin with (count 0), and no
version-qualified type refs exist in either file (there are no type refs at all).

## 5. Issues in `new` (independent of `old`)

1. **Stale field name in the rendered README quickstart (inherited from the library, present in both renders).**
   The render (line 104-106 of `new/ballerinax_candid.bal.txt`) shows:
   ```ballerina
   essentials:V3Query query = {
       search_terms: "candid"
   };
   ```
   In the published 0.2.1 source the field is `searchTerms` — `candid.essentials/types.bal:596-599`:
   ```ballerina
   public type V3Query record {
       @jsondata:Name {value: "search_terms"}
       string searchTerms?;
   ```
   `search_terms` is the wire name, not the Ballerina field name, so the snippet as written would not
   compile. This is an upstream README defect (the README predates the `@jsondata:Name` rename), faithfully
   reproduced by both renderers — not caused by spec v2 — but it is the one piece of content in this
   render that would mislead an LLM.

No other inaccuracies: the render contains no synthesized symbols, no truncation, no encoding damage
(README round-trips byte-for-byte), and its only non-README content is the package name and description,
both matching `bala.json` / Central.

## 6. Coverage gaps vs. the library

- **Default-module public symbols missing from both renders: 0.** The default module `candid` exports
  nothing (`grep -cE '^public ' modules/candid/candid.bal` → 0; file is 0 bytes).
- **Submodule-only public API absent from both renders (shared gap, pre-existing): 140 public top-level
  declarations**, counted with `grep -hE '^public ' <module>/*.bal | wc -l` in the bala:

  | Exported module | public top-level decls | client resource methods |
  |---|---|---|
  | `candid.charitycheckpdf` | 3 (`Client`, `ApiKeysConfig`, `ConnectionConfig`) | 1 |
  | `candid.essentials` | 49 | 6 |
  | `candid.premier` | 88 | 5 |
  | **total** | **140** | **12** |

  (`candid.mock` also ships in the bala but is not in the `export` list in `Ballerina.toml` / `package.json`,
  so it is correctly out of scope.)

  Net effect: for this package the Copilot render carries **0% of the callable API** and is README-only.
  That is a shared limitation of `pkg.getDefaultModule()`-based extraction on both sides, and spec v2
  does not address it.

## 7. Compiler plugin

None. `find . -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` over the tag-`v0.2.1` clone
returns nothing, and the bala has no `compiler-plugin/` directory (only `docs/`, `modules/`,
`bala.json`, `package.json`, `dependency-graph.json`). Nothing plugin-implied is therefore missing
from the render.

## 8. Other considerations

- **Pre-1.0 / unstable.** `0.2.1`; Central reports `isDeprecated: false`, `pullCount: 29`. Low adoption.
- **Distribution skew.** `Ballerina.toml` at the tag declares `distribution = "2201.8.0"`, while the bala
  was built with `ballerina_version: 2201.12.0`. Not render-affecting; noted for completeness.
- **Token size.** 133 lines / ~7 KB — negligible cost, but also negligible value to an LLM consumer beyond
  the setup instructions, since no API is rendered. An LLM asked to write candid code from this render has
  only the README's four snippets to work from, one of which (§5) is wrong.
- **Architectural note.** `candid` is the canonical example of a package whose default module is an empty
  placeholder. Any future fix that extracts exported submodules would change this render from 133 lines to
  a very large one (the submodule sources total 4,820 lines, 3,269 of them `candid.premier/types.bal`).

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l candid/old/*.bal.txt candid/new/*.bal.txt` | 133 / 133 |
| 2 | `diff -u old/ballerinax_candid.bal.txt new/ballerinax_candid.bal.txt` | exit 0, no output |
| 3 | `diff old/ballerinax_candid.json new/ballerinax_candid.json` | exit 0, no output |
| 4 | `md5 old/* new/*` | `.bal.txt` both `bc0338…d364b`; `.json` both `1a7472…3f87e` |
| 5 | `grep -c '^// Unknown type:' old new` | 0 / 0 |
| 6 | JSON key inspection (python `json.load`) | `typeDefs/clients/functions/services/annotations` all length 0 in both |
| 7 | `ls -R <bala>` | modules: `candid`, `candid.charitycheckpdf`, `candid.essentials`, `candid.mock`, `candid.premier`; no `compiler-plugin/` |
| 8 | `wc -l <bala>/modules/candid/candid.bal` | 0 lines (Read reports empty file) |
| 9 | `git ls-remote --tags <repo>` | `v0.2.1` → `d3232450…`, peeled `fbac99c8…` |
| 10 | `git clone --depth 1 --branch v0.2.1` + `wc -c ballerina/candid.bal` | 0 bytes |
| 11 | `find . -iname '*compiler-plugin*' -o -iname 'CompilerPlugin.toml'` in clone | no matches |
| 12 | `diff ballerina/Package.md <bala>/docs/Package.md` | exit 0 (identical) |
| 13 | `diff <render lines 8-132> <bala>/docs/Package.md` | only a trailing blank line in my slice; content identical (124 lines) |
| 14 | `curl api.central.ballerina.io/.../ballerinax/candid/0.2.1` | `isDeprecated:false`, 4 modules listed, `ballerinaVersion 2201.12.0`, readme matches |
| 15 | `cat <bala>/any/package.json` | `export: [candid, candid.charitycheckpdf, candid.essentials, candid.premier]`; `candid.mock` `export:false` |
| 16 | `grep -hE '^public ' <module>/*.bal \| wc -l` per module | 3 / 49 / 88 = 140 |
| 17 | `grep -cE '^ *(remote\|resource) (isolated )?function' */client.bal` | 1 / 6 / 5 = 12 |
| 18 | `grep -n 'public type V3Query record' -A 12 candid.essentials/types.bal` | field is `searchTerms` with `@jsondata:Name {value: "search_terms"}` (line 596-599) |
| 19 | `grep -n 'function init' -A 3 */client.bal` | init signatures as quoted in §3 |
| 20 | `grep -n 'public type ApiKeysConfig' -A 4 */types.bal` | `record {| string subscriptionKey; |}` in all three |
| 21 | `find modules -name '*.bal' \| xargs wc -l` | 4,820 total lines of published Ballerina source |

## 10. Caveats and unverified items

- The tag `v0.2.1` clone and the bala agree on every file compared (`candid.bal` emptiness, `Package.md`),
  so no GitHub-vs-bala conflict had to be resolved.
- I did not attempt to re-run the two-stage render pipeline; the audit compares the supplied artifacts.
  Given the two artifacts are byte-identical this does not affect any conclusion.
- The 140-symbol coverage figure counts `^public ` top-level declarations by grep over the bala's
  `*.bal` files. It counts declarations, not every nested/anonymous type, and excludes members of
  `Client` classes (reported separately as 12 resource methods). It excludes the non-exported
  `candid.mock` module.
- Whether the spec-v2 extractor *intends* to eventually cover exported submodules is outside what I can
  verify from these artifacts; I report only that neither side covers them today.

# ballerinax/hubspot.crm.extensions.videoconferencing 2.0.2 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/hubspot.crm.extensions.videoconferencing` |
| Pinned version | `2.0.2` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-hubspot.crm.extensions.videoconferencing |
| Tag reviewed | `v2.0.2` (commit `9ff065e`, peeled `f51b60f`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/hubspot.crm.extensions.videoconferencing/2.0.2` |
| Old render | `243` lines |
| New render | `245` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

This is a very small, single-module OpenAPI-generated connector: 3 exported types plus one client
class with 3 resource methods. Both renders capture 100% of the default module's public API and
the full README verbatim. The only difference between `old` and `new` is that `new` additionally
emits the two `@display` annotations that exist in the published source (`types.bal:38` and
`types.bal:43`). Nothing is dropped, reordered, or altered. There are zero `// Unknown type:`
placeholders on either side, and zero version-qualified type refs on either side, so the headline
spec-v2 behaviours have no surface to act on here.

Verdict: **IMPROVEMENT ONLY** — 2 lines added, 0 removed, both verified correct against the bala.

## 2. Change inventory

Line counts (`wc -l`): old **243**, new **245**. Mechanical diff: **1 hunk, +2 / −0**.

| Kind | old | new | delta |
|---|---|---|---|
| `type` declarations | 3 (`ExternalSettings`, `ApiKeysConfig`, `ConnectionConfig`) | 3 (same) | 0 |
| `client class` | 1 (`Client`) | 1 | 0 |
| client `init` | 1 | 1 | 0 |
| client resource functions | 3 (`get`, `put`, `delete`) | 3 | 0 |
| module-level functions | 0 | 0 | 0 |
| services / listeners / enums / consts | 0 | 0 | 0 |
| `@display` annotation lines | 0 | 2 | **+2** |
| `// Unknown type:` lines | 0 | 0 | 0 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| `// --- ` section markers | 4 | 4 | 0 |

The complete textual diff of the two renders is:

```diff
 type ApiKeysConfig record {
     # HubSpot developer API key
+    @display {label: "", kind: "password"}
     string hapikey;
 };

 # Provides a set of configurations for controlling the behaviours ...

+@display {label: "Connection Config"}
 type ConnectionConfig record {
```

JSON side: the two JSONs differ only by additive `annotations` arrays (`"annotations"` key
occurrences: old 1 — the top-level empty array; new 3). `python3 -m json.tool` diff shows two
hunks, both pure insertions; `typeDefs`, `clients`, `functions`, `services` name lists are
identical between the two JSONs.

## 3. Correctness against library source

Upstream `v2.0.2` clone and the bala are byte-identical for all three module files and the README
(`diff` returned no differences for `types.bal`, `client.bal`, `utils.bal`, `README.md`), so
GitHub-vs-bala disagreement does not arise here.

Verified item by item:

- `@display {label: "", kind: "password"}` on `hapikey` — matches bala
  `modules/hubspot.crm.extensions.videoconferencing/types.bal:38` exactly (label is genuinely the
  empty string in the source; the render is not truncating it).
- `@display {label: "Connection Config"}` on `ConnectionConfig` — matches `types.bal:43` exactly.
- `ExternalSettings` — all 5 fields, optionality (`string? userVerifyUrl?`, `string createMeetingUrl`
  required, etc.) and field order match `types.bal:23–33`. The missing doc on `fetchAccountsUri` in
  the render is faithful: the source has no doc for that field either (`types.bal:26`).
- `ApiKeysConfig` — single field `string hapikey` required, matches `types.bal:36–40`.
- `ConnectionConfig` — all 19 fields present with the same names, types and docs as
  `types.bal:44–82`.
- `Client` class doc string matches `client.bal:23`.
- `init(ApiKeysConfig apiKeyConfig, ConnectionConfig config = {}, string serviceUrl = "https://api.hubapi.com/crm/v3/extensions/videoconferencing/settings") returns error?`
  — matches `client.bal:33` including the default service URL.
- `resource function get [int:Signed32 appId](map<string|string[]> headers = {}) returns ExternalSettings|error`
  — matches `client.bal:44`.
- `resource function put [int:Signed32 appId](ExternalSettings payload, map<string|string[]> headers = {}) returns ExternalSettings|error`
  — matches `client.bal:57`.
- `resource function delete [int:Signed32 appId](map<string|string[]> headers = {}) returns error?`
  — matches `client.bal:73`.
- README block (render lines 8–158) is identical to `docs/README.md` (150 lines) apart from one
  trailing blank line.

No invented symbols. No signature drift.

## 4. Regressions

**None found.**

Basis for that conclusion:
- The full `diff -u old new` is 2 added lines and 0 removed/changed lines (shown in §2). There is
  physically nothing removed to regress.
- Declaration name sets extracted from both JSONs are identical (`typeDefs`, `clients`, `functions`,
  `services`).
- Section-marker count and positions are unchanged except for the 2-line shift of `// --- Client ---`
  (old line 226 → new line 228) caused by the two inserted annotation lines.
- `// Unknown type:` count is 0 on both sides, so no degraded-type regression is possible.
- README content is unchanged and complete on both sides.

## 5. Issues in `new` (independent of `old`)

All five below are present identically in `old` and are therefore renderer-wide behaviours, not
regressions introduced by spec v2. They are recorded because they affect the accuracy of what an
LLM reads.

1. **Doc parameter/return descriptions are dropped from client methods.** Source `client.bal:41–43`
   documents `+ appId - The ID of the video conference application...`, `+ headers - ...`,
   `+ return - successful operation`. The render emits only the summary plus a dangling empty
   comment line (render new:234–235 `# Get settings` / `# `). Same for `put` (new:238–239) and
   `delete` (new:242–243). An LLM gets no description of `appId` semantics.
2. **Default values on `ConnectionConfig` fields are lost, and required-with-default fields are
   rendered as optional.** Source has `http:HttpVersion httpVersion = http:HTTP_2_0`,
   `decimal timeout = 30`, `string forwarded = "disable"`, `boolean validation = true`,
   `boolean laxDataBinding = true`, etc. (`types.bal:46–81`); the render shows `httpVersion?`,
   `timeout?`, `forwarded?`, `validation?`, `laxDataBinding?` with no defaults (new:189–225).
3. **Closed records are rendered as open records.** `ApiKeysConfig` and `ConnectionConfig` are
   `record {| ... |}` in source (`types.bal:36`, `types.bal:44`); the render emits `record { ... }`.
4. **`public` and `isolated` qualifiers are dropped** — e.g. `public isolated client class Client`
   (`client.bal:24`) renders as `client class Client`; `public isolated function init` renders as
   `function init`.
5. **A wrapped doc line loses its `#` prefix, producing a non-compiling line.** Render new:223–224:
   the `laxDataBinding` doc wraps and the continuation `and absent fields are handled as \`nilable\`
   types. Enabled by default.` appears at column 0 inside the record body with no comment marker.
   Identical in old:221–222. If the render is ever fed to a compiler it will not parse.

## 6. Coverage gaps vs. the library

**None.** The package exports exactly one module (`package.json` `"export": ["hubspot.crm.extensions.videoconferencing"]`,
which is the default module), and the bala `modules/` directory contains only that one module — so
there is no submodule-only API and no shared-gap situation here. Its three files are `client.bal`,
`types.bal`, `utils.bal`; `utils.bal` contains no `public` declarations at all (grep for `public`
returned zero hits), so it exports nothing. Every public symbol — `ExternalSettings`,
`ApiKeysConfig`, `ConnectionConfig`, `Client` (+ `init`, `get`, `put`, `delete`) — appears in both
renders.

## 7. Compiler plugin

The package ships **no compiler plugin**. `find src -maxdepth 2 -iname "*compiler-plugin*"` on the
`v2.0.2` clone returns nothing, and the bala has no `compiler-plugin/` directory (its contents are
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`). Nothing plugin-derived
is therefore expected in, or missing from, the render.

## 8. Other considerations

- Stable release line (`2.0.2`); Ballerina Central reports `deprecated: null`, empty
  `deprecateMessage`, `graalvmCompatible: "Yes"`, built with `ballerinaVersion 2201.12.2`.
- Size is trivial: 245 lines / 23.4 KB JSON. 151 of the 245 render lines (62%) are README; the
  actual API surface is ~85 lines. Token cost is negligible.
- The README is high quality (setup guide, quickstart, two linked examples) and survives rendering
  intact, including the fenced `ballerina`/`toml`/`bash` code blocks.
- Both files are auto-generated by the Ballerina OpenAPI tool (`AUTO-GENERATED FILE. DO NOT MODIFY.`
  headers), so render fidelity here is essentially a fidelity test of the extractor rather than of
  hand-written API design.
- The `@display {label: ""}` on `hapikey` has an empty label in the source itself; the new render is
  faithful, but the annotation carries no information beyond `kind: "password"`.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/*.bal.txt new/*.bal.txt` | old 243, new 245 |
| 2 | `diff -u old/...bal.txt new/...bal.txt` | 1 hunk, +2 −0 (two `@display` lines) |
| 3 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 4 | `grep -n '^// --- '` both renders | 4 markers each; `// --- Client ---` old:226 → new:228 |
| 5 | `diff <(python3 -m json.tool old.json) <(python3 -m json.tool new.json)` | 2 hunks, both pure insertions of `annotations` arrays |
| 6 | `grep -o '"annotations"' old.json \| wc -l` / new | 1 / 3 |
| 7 | Python: top-level key + `typeDefs`/`clients`/`functions` name lists, both JSONs | identical: typeDefs `[ExternalSettings, ApiKeysConfig, ConnectionConfig]`, clients `[Client]`, functions `[]` |
| 8 | `git ls-remote --tags <repo>` | tags v1.0.0, v2.0.0, v2.0.1, **v2.0.2** (`9ff065e`) |
| 9 | `git clone --depth 1 --branch v2.0.2` | succeeded into scratch `src/` |
| 10 | `grep -n version src/ballerina/Ballerina.toml` | `version = "2.0.2"` — matches pin |
| 11 | `diff src/ballerina/{types,client,utils}.bal` vs bala `modules/.../` | all SAME |
| 12 | `diff src/ballerina/README.md` vs bala `docs/README.md` | SAME |
| 13 | `grep -n "@display" bala .../types.bal` | lines 38 and 43 — exactly the two lines `new` adds |
| 14 | `ls bala/.../modules/` | single module `hubspot.crm.extensions.videoconferencing` |
| 15 | `grep -n "public" bala .../utils.bal` | no hits — utils exports nothing |
| 16 | `cat bala/.../package.json` | `export: ["hubspot.crm.extensions.videoconferencing"]`, ballerina_version 2201.12.2, graalvmCompatible true |
| 17 | `find src -maxdepth 2 -iname "*compiler-plugin*"` | no hits |
| 18 | `curl` Central `/2.0/registry/packages/ballerinax/hubspot.crm.extensions.videoconferencing/2.0.2` | 1 module, `deprecated: null`, graalvmCompatible Yes |
| 19 | `diff <(sed -n '8,158p' new render) bala/docs/README.md` | only a trailing blank line differs (README preserved verbatim) |
| 20 | Signature spot-check: render new:232/236/240/244 vs `client.bal:33/44/57/73` | all four match exactly |
| 21 | Field-by-field check: render new:165–226 vs `types.bal:23–82` | all 5 + 1 + 19 fields match; defaults dropped (see §5.2) |
| 22 | `sed -n '218,226p' old render` | confirms the un-prefixed doc continuation line exists in `old` too (§5.5) |
| 23 | Read `OLD_AND_NEW_DIFFS/hubspot.crm.extensions.videoconferencing_diff.md` | its counts (243/245, +2/−0, 1 hunk, 0 unknown types, 4 markers) all independently reproduced above |

## 10. Caveats and unverified items

- Neither render was compiled. The malformed line noted in §5.5 was identified by reading, not by
  running `bal build`; the claim that it "will not parse" is a reasoned assertion about Ballerina
  syntax, not a compiler-verified fact.
- The old/new pipeline commits (`eb5d81b3` / `412ba01e`) were taken from the brief and not
  re-verified; no `ballerina-vscode` checkout was inspected for this library.
- Only the default module was in scope because the package publishes exactly one module; no
  submodule analysis was possible or needed.
- Doc-string and annotation handling for kinds absent from this library (enums, constants, services,
  listeners, module-level functions, error types) could not be exercised here — this library has
  none of them, so this report says nothing about spec v2's behaviour for those kinds.

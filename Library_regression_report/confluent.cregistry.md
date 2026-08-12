# ballerinax/confluent.cregistry 0.4.5 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/confluent.cregistry` |
| Pinned version | `0.4.5` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-confluent.cregistry |
| Tag reviewed | `v0.4.5` (exact match, commit `97c0b952e430c1eee4a73900e009ccae8b303c7e`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/confluent.cregistry/0.4.5` |
| Old render | `120` lines |
| New render | `121` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

This is a tiny library: one default module (`confluent.cregistry`), 4 source files, 130 lines
total, exporting 3 public types and 1 client class with 3 public methods.

The old→new delta is exactly one hunk: the `// Unknown type: Error` placeholder in `old` is
replaced in `new` by a real definition with its doc comment:

```
- // Unknown type: Error
+ # Represents any error related to Ballerina Confluent Schema Registry module.
+ type Error error<ErrorDetails>;
```

The underlying JSON delta is equally minimal — `new` adds `"baseType": "error<ErrorDetails>"` to
the `Error` typeDef; nothing else in the JSON changed. Nothing was removed, truncated, or
reworded. `// Unknown type:` count goes 1 → 0. No regressions found.

Several inaccuracies remain in `new`, but all except one (`distinct` dropped from the new `Error`
line) are byte-identical in `old` and are pre-existing extractor/renderer behaviour, not caused by
spec v2.

## 2. Change inventory

Line counts: `old` 120, `new` 121 (`wc -l`). Diff: 1 hunk, +2 / −1.

| Kind | old | new | delta |
|---|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Version/module-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |
| `// --- ` section markers | 4 | 4 | 0 |
| Top-level `type` declarations | 2 (`ErrorDetails`, `ConnectionConfig`) | 3 (`+Error`) | +1 |
| `client class` | 1 (`Client`) | 1 | 0 |
| Client methods (`init`, `register`, `getSchemaById`) | 3 | 3 | 0 |
| Module-level functions / services / listeners / annotations / enums / consts | 0 | 0 | 0 |
| README block | present, 71 lines (render L7–L77) | identical | 0 |

**Added (1):** `type Error error<ErrorDetails>;` plus its doc line.
**Removed (0):** none.
**Modified (0):** no existing declaration's text changed — the `init`, `register`,
`getSchemaById` signatures and both record bodies are byte-identical between the files (the only
difference in their line numbers is the +1 shift after the new `Error` block).

JSON diff (`python3 -m json.tool` on both, `diff -u`): single hunk, `Error` typeDef gains
`"baseType": "error<ErrorDetails>"`. `typeDefs` order, `clients`, `functions`, `services`,
`annotations`, `readme`, `description` all unchanged.

## 3. Correctness against library source

Upstream `v0.4.5` `ballerina/*.bal` is byte-identical to the bala's
`modules/confluent.cregistry/*.bal` (verified with `diff` on all 4 files — all "same"), so GitHub
and the bala agree; no bala-wins conflict.

Exhaustive check of every public symbol in the default module:

| Symbol | Source | Rendered in `new` | Match |
|---|---|---|---|
| `ErrorDetails` (`record {\| int status?; int errorCode?; \|}`) | `error.bal:21–24` | render L84–89 | fields/optionality/docs correct; closed-ness lost (see §5) |
| `Error` (`public type Error distinct error<ErrorDetails>`) | `error.bal:27` | render L91–92 | base type correct; `distinct` lost (see §5) |
| `ConnectionConfig` (`record {\| string baseUrl; int identityMapCapacity = 1000; map<anydata> originals?; map<string> headers?; \|}`) | `types.bal:24–29` | render L97–106 | names/types/docs correct; default + closed-ness lost (see §5) |
| `Client` (`public isolated client class`) | `client.bal:20` | render L111 | present; `public`/`isolated` dropped |
| `Client.init(*ConnectionConfig config) returns error?` | `client.bal:26` | render L112 | see §5 item 2 — expanded incorrectly |
| `Client.register(string subject, string schema) returns int\|Error` | `client.bal:39` | render L116 | exact match (minus `isolated`) |
| `Client.getSchemaById(int id) returns string\|Error` | `client.bal:45` | render L120 | exact match (minus `isolated`) |

Correctly excluded non-public members: `Client.generateSchemaRegistryClient` (`private`,
`client.bal:31`), module-level `init()` and `setModule()` (`init.bal:19,23`) — none appear in
either render, which is right.

The added `Error` doc string in `new` ("Represents any error related to Ballerina Confluent Schema
Registry module.") matches `error.bal:26` verbatim. The `baseType` `error<ErrorDetails>` matches
`error.bal:27`.

README in the render matches the Central `readme` field and `docs/README.md` in the bala verbatim,
including its pre-existing typo (missing comma after `"basic.auth.user.info"` line in the Step 2
snippet) — that typo is in the published library, not introduced by either renderer.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `diff -u old new` on the `.bal.txt` files: exactly one hunk, purely additive apart from the
  removed `// Unknown type: Error` placeholder line, which carried no information.
- `diff -u` on the pretty-printed JSONs: one hunk, one key added, nothing removed.
- Declaration extraction (`grep -nE '^(public )?(type|client class|...)'`) on both files: `old` set
  is a strict subset of `new` set; no symbol lost.
- Client-method extraction (`grep -nE '^ +(remote )?function'`): all three signatures byte-identical
  across the two files.
- README block, section markers, module description, import line: identical (only-hunk evidence).
- No malformed syntax was introduced by `new`; the one malformed construct (`init`, §5 item 2) is
  present identically in `old`.

## 5. Issues in `new` (independent of `old`)

1. **`distinct` dropped from `Error`** — new-only, because `old` had no definition at all.
   Source `error.bal:27` is `public type Error distinct error<ErrorDetails>;`; the render emits
   `type Error error<ErrorDetails>;`. Losing `distinct` changes the type's semantics (distinct
   errors are not assignable from other `error<ErrorDetails>` values). Low impact for an LLM
   consumer, but it is a fidelity loss in the new emission. Note the JSON `baseType` field is
   `error<ErrorDetails>` — the distinctness is already absent upstream in the extractor, so the
   renderer is faithful to its input.
2. **`Client.init` signature is not valid Ballerina and duplicates the config** (render L112,
   identical in `old` L111):
   `function init(string baseUrl = "", int identityMapCapacity = 1000, map<anydata> originals = {}, map<string> headers = {}, ConnectionConfig config) returns error?;`
   The real signature is `public isolated function init(*ConnectionConfig config) returns error?`
   (`client.bal:26`). The extractor both expands the included-record parameter into its fields *and*
   keeps the `config` parameter, then emits `config` last with no `?` and no default, so a required
   parameter follows defaultable ones — this would not compile, and it invites an LLM to write
   `new (baseUrl, ..., config)`. Shared with `old`; not a spec-v2 regression.
3. **Invented default for `baseUrl`** — JSON gives `"default": "\"\""` for `init`'s `baseUrl`, so
   the render shows `string baseUrl = ""`. `ConnectionConfig.baseUrl` (`types.bal:25`) is a
   **required** field with no default. This makes a mandatory value look omissible. Shared with `old`.
4. **`ConnectionConfig.identityMapCapacity` default lost and optionality inverted** — source
   `types.bal:26` is `int identityMapCapacity = 1000;` (required field with a default); the render
   shows `int identityMapCapacity?;` (optional, no default). The value 1000 does survive in the
   `init` expansion, so the information is not entirely gone from the file. Shared with `old`.
5. **Record closedness and qualifiers dropped throughout** — `ErrorDetails` and `ConnectionConfig`
   are `record {| ... |}` (closed) in source but render as `record { ... }` (open); `Client` is
   `public isolated client class` but renders as `client class`; `register`/`getSchemaById` are
   `remote isolated function` but render as `remote function`; no `public` qualifier appears on any
   type. This is uniform renderer convention, shared with `old`.

Items 2–5 are byte-identical in `old` (confirmed by the single-hunk diff), i.e. pre-existing
behaviour rather than anything spec v2 introduced.

## 6. Coverage gaps vs. the library

**None.** The bala has exactly one module directory, `modules/confluent.cregistry`, which is the
default module — there are no submodules, so the known `getDefaultModule()`-only limitation costs
nothing here. Every public symbol in that module (`ErrorDetails`, `Error`, `ConnectionConfig`,
`Client` and its 3 public methods) appears in `new`. In `old`, `Error` was present in name only
(`// Unknown type: Error`, no base type, no doc) — that was the sole gap and `new` closes it.

## 7. Compiler plugin

No compiler plugin exists. `find` over the cloned `v0.4.5` tree for `*compiler-plugin*` /
`CompilerPlugin*` returns nothing; `ballerina/Ballerina.toml` has no `[[plugin]]` or
`compilerPlugin` entry; the bala has no `compiler-plugin/` directory (its top level is
`bala.json`, `dependency-graph.json`, `docs/`, `modules/`, `package.json`, `platform/`).
The repo's `native/` directory holds the Java interop implementation
(`io.ballerina.lib.confluent.registry.CustomSchemaRegistryClient` / `ModuleUtils`), not a plugin.
Nothing plugin-derived is therefore expected in the render, and nothing is missing on that account.

## 8. Other considerations

- **Pre-1.0 version.** `0.4.5` is unstable; API may change without a major bump. Central reports
  `isDeprecated: false`, `graalvmCompatible: Yes`, `ballerinaVersion: 2201.11.0`.
- **Size / tokens.** 121 lines, of which 71 are the README block — the README is ~59% of the render.
  Non-issue at this size.
- **Doc quality.** All three types and all three client methods carry doc comments, propagated
  correctly. Two trailing-`#` artefacts appear where a multi-line doc's parameter section was
  stripped (render L82, L95, L115, L119) — cosmetic, present in both renders.
- **README code snippet is itself broken Ballerina** (missing comma after the
  `"basic.auth.user.info"` entry in the `originals` map). This is a defect of the published
  package, reproduced faithfully by both renders, and it will mislead an LLM copying the quickstart.
  Fixing it belongs upstream, not in the renderer.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/*.bal.txt new/*.bal.txt` | old 120, new 121 |
| `diff -u old/...bal.txt new/...bal.txt` | 1 hunk at old L88–94 / new L88–95, +2/−1 |
| `diff -u <(json.tool old.json) <(json.tool new.json)` | 1 hunk: `Error` typeDef gains `"baseType": "error<ErrorDetails>"` |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -nE '^(public )?(type\|client class\|class\|enum\|const\|annotation\|listener\|service\|function)'` | old: L58 README `main`, L84 `ErrorDetails`, L96 `ConnectionConfig`, L110 `Client`; new: L58, L84, L92 `Error`, L97, L111 |
| `grep -nE '^ +(remote )?function'` | 3 methods each side, identical text (old L111/115/119, new L112/116/120) |
| `grep -n '^// --- '` (via diff signals) | 4 markers both sides |
| `ls -R <bala>` | one module dir `confluent.cregistry`; files `client.bal error.bal init.bal types.bal`; no `compiler-plugin/` |
| `git ls-remote --tags <repo>` | `v0.4.5` exists → `97c0b952e430c1eee4a73900e009ccae8b303c7e` |
| `git clone --depth 1 --branch v0.4.5` | succeeded |
| `diff <src>/ballerina/{client,error,init,types}.bal <bala>/modules/.../` | all 4 identical |
| `wc -l <bala>/*.bal` | client 50, error 27, init 25, types 28 = 130 |
| `grep -n 'distinct\|identityMapCapacity' <src>/ballerina/*.bal` | `error.bal:27 public type Error distinct error<ErrorDetails>;`, `types.bal:25 int identityMapCapacity = 1000;` |
| `find <src> -iname '*compiler-plugin*' -o -iname 'CompilerPlugin*'` | no matches |
| `grep -n compiler <src>/ballerina/Ballerina.toml` | no matches |
| `curl api.central.ballerina.io/.../0.4.5` | 1 module, not deprecated, java21, balVersion 2201.11.0, readme matches render |
| Read of full `new/*.bal.txt` (121 lines) | contents as described above |
| Read of full `new/*.json` (minus readme) | contents as described above |

## 10. Caveats and unverified items

- The `old`-side and `new`-side `ballerina-vscode` commits (`eb5d81b3`, `412ba01e`) were taken from
  the brief; I did not clone either extension repo to re-derive the renders. The renders and JSONs
  in the library folder were used as given.
- I did not compile the render output with `bal build`; the "would not compile" claim about
  `Client.init` (§5 item 2) is a reading of the Ballerina grammar rule that a required parameter
  cannot follow defaultable parameters, not a compiler result.
- The Java native side (`native/**`) was not reviewed beyond confirming it contains no compiler
  plugin; it is irrelevant to what the extractor sees.
- Nothing else was left unverified — the library is small enough that every public symbol was
  checked individually against source.

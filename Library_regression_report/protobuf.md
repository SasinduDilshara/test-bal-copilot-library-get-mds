# ballerina/protobuf 1.8.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/protobuf` |
| Pinned version | `1.8.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-protobuf |
| Tag reviewed | `v1.8.0` (commit `1bb97267cb53ac5ed5ad93696b2837e44b78869b`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/protobuf/1.8.0` (java21) |
| Old render | 80 lines |
| New render | 86 lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/protobuf` has an unusually small default module: exactly three public declarations
(`MessageDescriptor`, `Error`, `Descriptor`). `old` rendered one of them fully, degraded `Error`
to `// Unknown type: Error`, and omitted the `Descriptor` annotation entirely. `new` renders all
three, adding a real `Error` definition and a new `// --- Annotations ---` section carrying
`public annotation MessageDescriptor Descriptor on type;` — the annotation that every
protoc-generated Ballerina stub attaches (`@protobuf:Descriptor {value: "..."}`), so this is a
materially useful gain. Lines 1–79 are byte-identical between the two renders; nothing was lost.

Both sides omit the entire submodule surface (6 exported `protobuf.types.*` modules, 27 public
declarations including the only two functions in the package, `pack`/`unpack`). That is the known
shared `getDefaultModule()` limitation, present identically on both sides.

## 2. Change inventory

Line counts (`wc -l`): old 80, new 86. Diff: +7 / −1, 1 hunk (old 77–80 → new 77–86).

| Kind | old | new | delta |
|---|---|---|---|
| Record type defs rendered | 1 (`MessageDescriptor`) | 1 (`MessageDescriptor`) | 0 |
| Error type defs rendered | 0 (degraded placeholder) | 1 (`Error`) | +1 |
| Annotations rendered | 0 | 1 (`Descriptor`) | +1 |
| Functions / clients / services / listeners / enums / consts / classes | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| `// --- section ---` markers | 3 (README, END README, Types) | 4 (+ Annotations) | +1 |
| Version-qualified type refs (`mod:x.y.z:Type`) | 0 | 0 | 0 |

**Added in `new` (2 declarations):**
- `type Error error;` (replacing `// Unknown type: Error`)
- `public annotation MessageDescriptor Descriptor on type;` under a new `// --- Annotations ---` section

**Removed in `new`: none.** `diff` of lines 1–79 is empty — README block (62 lines, concatenating
the package README plus all six submodule READMEs) and the `MessageDescriptor` record are unchanged.

JSON-level change (old vs new `ballerina_protobuf.json`): `typeDefs[1]` gains `"baseType": "error"`;
`annotations` goes from `[]` to a one-entry array with `name: Descriptor`, `attachmentPoint: TYPE`,
`typeConstraint.name: MessageDescriptor` plus an internal link to the record.

## 3. Correctness against library source

The bala's `modules/protobuf/*.bal` is byte-identical to the `v1.8.0` clone's `ballerina/*.bal`
(`diff` returned no output for both `annotation.bal` and `natives.bal`), so GitHub and the bala agree.

Default module public API is exactly three declarations:

| Source | Declaration | In `old` | In `new` |
|---|---|---|---|
| `ballerina/natives.bal:18` | `public type Error distinct error;` | `// Unknown type: Error` | `type Error error;` |
| `ballerina/annotation.bal:20` | `public type MessageDescriptor record {\| string value; \|}` | rendered (open record, no `public`) | identical to old |
| `ballerina/annotation.bal:25` | `public annotation MessageDescriptor Descriptor on type;` | absent | `public annotation MessageDescriptor Descriptor on type;` |

- **`Descriptor` annotation** — new render is character-for-character the source declaration,
  including the `public` qualifier, the type constraint, and the `on type` attachment point.
  Doc string `# Annotation definition of the Descriptor` matches `annotation.bal:24`. Correct.
- **`Error`** — doc string `# Represents protobuf module error.` matches `natives.bal:17`. The
  definition itself is approximate: see §5.
- **`MessageDescriptor`** — field name, type (`string`) and field doc
  (`# + value - The descriptor value as a hexadecimal string`, `annotation.bal:19`) all match.
  Record closedness and `public` are lost, in both renders equally.

## 4. Regressions

**None found.** Basis for that conclusion:

- `diff` of old lines 1–79 vs new lines 1–79 is empty → header, README section (all 7 overview
  blocks), and the whole `MessageDescriptor` block are untouched.
- The only removed line in the unified diff is `// Unknown type: Error`, replaced by a real
  definition.
- No declaration present in `old` is missing from `new`; no parameter, default, return type or doc
  line exists anywhere in `old` that is absent in `new` (the library has no functions or clients at
  all in the default module, so there is no signature surface to lose).
- No version-qualified refs existed in `old`, so nothing to compare there (0 → 0).

## 5. Issues in `new` (independent of `old`)

1. **`distinct` dropped from `Error`.** Source (`ballerina/natives.bal:18`) is
   `public type Error distinct error;`; `new` emits `type Error error;`. This matters for a
   foundational module: `protobuf.types.any` derives `public type Error distinct protobuf:Error;`
   (`modules/protobuf.types.any/any.bal:28`), and distinct-ness is what makes `protobuf:Error`
   usable in narrowing error unions. An LLM reading the render would believe any `error` value is
   assignable to `protobuf:Error`. Low practical blast radius here (the type has no members and is
   rarely constructed by users), but it is an inaccuracy.
2. **`public` qualifier omitted on both type defs.** `MessageDescriptor` and `Error` are `public`
   in source but rendered unqualified, while the annotation *is* rendered `public`. The render is
   therefore internally inconsistent and, taken literally as Ballerina source, would declare
   module-private types. Renderer convention rather than data loss — the JSON has no visibility
   field at all — but worth noting.
3. **`MessageDescriptor` rendered as an open record.** Source is closed (`record {| ... |}`,
   `annotation.bal:20-22`); both renders emit `record { ... }`. Present in `new`, inherited from
   `old`, so not a regression.

Minor/cosmetic (not counted above): line 73 is a bare `# ` artifact from the doc-string trailing
newline; the README block is raw Markdown embedded inside a `.bal.txt` file (both sides).

## 6. Coverage gaps vs. the library

**Default module: zero gaps in `new`.** All 3 public declarations from
`modules/protobuf/{natives,annotation}.bal` appear in the new render. `old` had 2 gaps
(the `Descriptor` annotation entirely, and `Error`'s definition).

**Submodule-only API: 27 public declarations, absent from BOTH renders** (shared
`getDefaultModule()` gap, not a `new` regression). Counted via
`grep -hcE '^public ' modules/protobuf.types.*/*.bal` = 27, across the 6 modules that
`package.json` marks `export: true`:

- `protobuf.types.any` (9): `ValueType`, `ValueTypeDesc`, `Error`, `TypeMismatchError`, `Any`,
  `ContextAny`, `ContextAnyStream`, and the **only two functions in the whole package** —
  `public isolated function pack(ValueType message) returns Any|Error` (`any.bal:64`) and
  `public isolated function unpack(Any anyValue, ValueTypeDesc targetTypeOfAny = <>) returns targetTypeOfAny|Error` (`any.bal:75`).
- `protobuf.types.duration` (2), `protobuf.types.empty` (2), `protobuf.types.struct` (2),
  `protobuf.types.timestamp` (2), `protobuf.types.wrappers` (10 — Context/ContextStream pairs for
  boolean, bytes, string, float, int).

This is the most consequential gap for this library: the rendered README says "see the below
**Functions**" seven times and the render contains no functions at all. It is identical on both
sides.

## 7. Compiler plugin

`has_plugin: false` — confirmed independently:
- `find` over the bala root for `*compiler-plugin*` returned 0 hits (no `compiler-plugin/`
  directory, no `compiler-plugin.json`).
- `ballerina/Ballerina.toml` at tag `v1.8.0` has no `[[plugin]]` / `compilerPlugin` entry
  (grep exit 1); the repo has no `compiler-plugin` module (top-level dirs: `ballerina`, `native`,
  `build-config`, `docs`, `gradle`).

Nothing plugin-derived is therefore expected in the render, and nothing is missing on that account.
The `@protobuf:Descriptor` annotation is consumed by the separate `protoc` tool / `ballerina/grpc`
runtime, not by a plugin shipped in this package.

## 8. Other considerations

- **Version/stability:** 1.8.0 is a stable post-1.0 release; `package.json` reports
  `ballerina_version: 2201.12.0`, `graalvmCompatible: true`, `template: false`, no deprecation
  markers. Central metadata not re-queried (see caveats) — bala `package.json` used instead.
- **Size/tokens:** trivial. 86 lines, of which 62 (72%) are README prose and only 17 are actual
  declarations. Token cost is negligible either way; the +6 lines are well spent.
- **Practical value of the addition:** `@protobuf:Descriptor` appears on every message record in
  protoc-generated Ballerina stubs. `old` gave a consumer no way to know the annotation exists;
  `new` gives the exact declaration. This is the single most useful thing the extractor could add
  for this module short of submodule support.
- **Cross-library impact:** grepping all renders in the repo, only `grpc` and `otel` mention
  "protobuf", and neither references the `protobuf:Error` or `protobuf:Descriptor` symbols (matches
  are README prose / proto-file text), so the `distinct` inaccuracy does not propagate into other
  renders in this batch.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l protobuf/old/*.bal.txt protobuf/new/*.bal.txt` | 80 / 86 |
| `wc -l protobuf/old/*.json protobuf/new/*.json` | 29 / 45 |
| `grep -c '^// Unknown type:' old` / `new` | 1 / 0 |
| `grep -cE '[a-z]+:[0-9]+\.[0-9]+\.[0-9]+:' old` / `new` | 0 / 0 |
| `diff <(sed -n '1,79p' old) <(sed -n '1,79p' new)` | empty → lines 1–79 identical |
| `git ls-remote --tags .../module-ballerina-protobuf \| grep v1.8.0` | `v1.8.0` → `1bb97267cb53ac5ed5ad93696b2837e44b78869b` |
| `git clone --depth 1 --branch v1.8.0` | succeeded into scratch `work/protobuf/src` |
| `diff bala/modules/protobuf/annotation.bal src/ballerina/annotation.bal` | identical |
| `diff bala/modules/protobuf/natives.bal src/ballerina/natives.bal` | identical |
| `grep -nE '^public ' bala/modules/protobuf/*.bal` | 3 decls: `natives.bal:18` Error, `annotation.bal:20` MessageDescriptor, `annotation.bal:25` Descriptor |
| `grep -hcE '^public ' bala/modules/protobuf.types.*/*.bal \| paste -sd+ \| bc` | 27 |
| `find bala/1.8.0 -iname '*compiler-plugin*' \| wc -l` | 0 |
| `grep -n 'compilerPlugin\|\[\[plugin' src/ballerina/Ballerina.toml` | no match (exit 1) |
| `cat bala/java21/package.json` | export list = 7 modules (default + 6 submodules); version 1.8.0 |
| `python3 -m json.tool` on both JSONs | old `annotations: []`, no `baseType`; new `annotations: [Descriptor]`, `Error.baseType: "error"` |
| `cat bala/java21/docs/README.md` (204 bytes) | matches render lines 8–12 verbatim |
| `grep -rl 'protobuf' --include='*.bal.txt' .` | only grpc, otel, protobuf folders |

## 10. Caveats and unverified items

- Ballerina Central's registry API was **not** re-queried for `ballerina/protobuf/1.8.0`;
  version/module/deprecation facts in §8 come from the bala's `package.json` and the `v1.8.0`
  `Ballerina.toml`, which are authoritative for what the extractor consumed. Central-only metadata
  (download counts, deprecation flag set after publish) is therefore unverified.
- The bala is `platform: java21`; only that platform directory exists in the distribution repo, so
  no cross-platform comparison was possible (none expected for a stdlib module).
- Whether the extractor *could* have preserved `distinct` and `public` (i.e. whether the loss is in
  the Java `ModelToJsonConverter` or the TypeScript `toSyntaxString`) was not traced into the
  `ballerina-vscode` sources; the JSON simply carries no field for either, so the loss is at or
  before JSON generation. Which of the two stages is responsible is unverified.
- No attempt was made to compile the render as Ballerina source; syntax judgements in §5 are by
  inspection.

# ballerina/regex 1.4.3 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/regex` |
| Pinned version | `1.4.3` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-regex |
| Tag reviewed | `v1.4.3` (exact tag; shallow clone succeeded) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/regex/1.4.3/java11` |
| Old render | `202` lines |
| New render | `204` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`ballerina/regex` is a tiny, **deprecated** standard-library module: one module (`regex`, which is
also the default module), 3 source files, 7 public functions and 4 public types. Both renders cover
100% of the public declaration set (7/7 functions, 4/4 types) and neither contains any
`// Unknown type:` placeholder.

Spec v2 makes exactly two changes, both strict improvements, confirmed by a byte-level JSON diff
that contains no other hunks:

1. `class Groups` gains its `get(int index) returns PartMatch|()` method (`old` emitted an empty
   class body).
2. `type Replacement` loses the bogus version-qualified reference
   `ballerina/regex:1.4.3:ReplacerFunction` and now reads `ReplacerFunction|string`, matching the
   library source verbatim.

No declaration, parameter, default, return type, doc line or README byte is lost. **No regressions.**

Several fidelity defects remain, but every one of them is present identically in `old` and is
therefore not attributable to spec v2 (see §5).

## 2. Change inventory

Line counts (`wc -l`): old **202**, new **204** (+2).

Full unified render diff (`diff -u old new`) is 2 hunks, +3 / −1 lines:

```diff
@@ -58,6 +58,8 @@
 # Abstract object representation to hold information about matched regex groups.
 class Groups {
+
+    function get(int index) returns PartMatch|();
 }
@@ -73,7 +75,7 @@
 # A type to be used to get a replacement string.
-type Replacement ballerina/regex:1.4.3:ReplacerFunction|string;
+type Replacement ReplacerFunction|string;
```

By kind:

| Kind | old | new | Δ |
|---|---|---|---|
| Top-level functions | 7 | 7 | 0 |
| Record types | 2 (`PartMatch`, `Match`) | 2 | 0 |
| Class/object types | 1 (`Groups`) | 1 | 0 |
| Union types | 1 (`Replacement`) | 1 | 0 |
| Enums / consts / annotations / listeners / services / clients | 0 | 0 | 0 |
| Class member functions | 0 | **1** (`Groups.get`) | **+1** |
| `// Unknown type:` placeholders | 0 | 0 | 0 |
| Version-qualified type refs (`org/mod:x.y.z:T`) | 1 | **0** | **−1** |
| `// --- ` section markers | 4 | 4 | 0 |

**Added:** `Groups.get`.
**Removed:** nothing.
**Modified:** `Replacement`'s union member name only.

The JSON diff (`diff` of `python3 -m json.tool` output on both `ballerina_regex.json`) shows the
same and only two changes: a new `functions` array on the `Groups` typeDef, and
`"name": "ballerina/regex:1.4.3:ReplacerFunction"` → `"name": "ReplacerFunction"`. JSON size
15,629 B → 16,187 B. Top-level JSON keys identical; `clients`, `services`, `annotations` are `[]`
on both sides (correct — this module has none).

## 3. Correctness against library source

The bala's `modules/regex/{natives,types,utils}.bal` are **byte-identical** to the `v1.4.3` tag's
`ballerina/{natives,types,utils}.bal` (`diff` returned no output for all three files), so GitHub and
the bala agree and either can be cited. `Ballerina.toml` line 4 = `version = "1.4.3"`; no version
drift.

Both changes in `new` are correct:

- `Groups.get` — `ballerina/types.bal:36`: `public isolated function get(int index) returns PartMatch?;`
  The render's `function get(int index) returns PartMatch|();` matches in name, arity, parameter name
  and type, and return type (`T?` ≡ `T|()`). Also implemented at `ballerina/utils.bal:52`
  (`MatchGroups.get`). **Correct addition.**
- `Replacement` — `ballerina/types.bal:52-53`:
  `public type Replacement ReplacerFunction|string;`. `new` reproduces this exactly; `old`'s
  `ballerina/regex:1.4.3:ReplacerFunction` is not valid Ballerina syntax anywhere. **Correct fix.**

Exhaustive check of the remaining declarations (small library, so all 11 were verified against
`natives.bal` / `types.bal`):

| Render decl | Source | Match? |
|---|---|---|
| `function matches(string stringToMatch, string regex) returns boolean` | `natives.bal:33` | yes |
| `function replace(string originalString, string regex, Replacement replacement, int startIndex = 0) returns string` | `natives.bal:55-56` | yes, incl. `startIndex = 0` default |
| `function replaceAll(string originalString, string regex, Replacement replacement) returns string` | `natives.bal:89` | yes |
| `@deprecated function replaceFirst(string originalString, string regex, string replacement) returns string` | `natives.bal:127-128` | yes, incl. `@deprecated` |
| `function split(string receiver, string delimiter) returns string[]` | `natives.bal:146` | yes |
| `function search(string str, string regex, int startIndex = 0) returns Match\|()` | `natives.bal:166` (`returns Match?`) | yes |
| `function searchAll(string str, string regex) returns Match[]` | `natives.bal:197` | yes |
| `type PartMatch record { string matched; int startIndex; int endIndex; }` | `types.bal:21-25` | fields/types yes; closedness lost (§5.5) |
| `type Match record { Groups groups; string matched; int startIndex; int endIndex; }` | `types.bal:44-48` | yes — `*PartMatch` inclusion correctly flattened |
| `class Groups { function get(...) }` | `types.bal:29-37` | method yes; `count` field and `readonly & object` shape lost (§5.2, §5.3) |
| `type Replacement ReplacerFunction\|string` | `types.bal:53` | yes |

README: the render's `// --- README ---` block reproduces the Central `readme` (package overview +
deprecation notice) followed by the module readme, matching the Central API response for
`ballerina/regex/1.4.3` field-for-field. Identical in both renders.

## 4. Regressions

**None found.**

Basis for that conclusion:
- The complete `diff -u old new` on the rendered `.bal.txt` is 2 hunks / +3 / −1 lines, reproduced
  in full in §2. There is no other textual difference anywhere in the 202/204 lines.
- The complete pretty-printed JSON diff is likewise 2 hunks, both additive/corrective.
- Declaration counts by kind are identical except for the +1 class method (§2 table).
- Function count 7 = 7; type count 4 = 4; `// Unknown type:` 0 = 0; section markers 4 = 4.
- Doc-comment payload is byte-identical (the only lines that moved are the two hunks); the count of
  malformed doc-continuation lines is 7 on both sides, i.e. unchanged.
- No parameter, default value, return type, annotation, or README byte is dropped in `new`.

## 5. Issues in `new` (independent of `old`)

All seven items below are present **identically in `old`** — none is caused by spec v2 — but they
are inaccuracies a consumer of the `new` render would hit.

1. **`ReplacerFunction` is referenced but never defined.** `new:78` emits
   `type Replacement ReplacerFunction|string;` but `ReplacerFunction` is module-private
   (`types.bal:50` — `type ReplacerFunction isolated function (Match matched) returns string;`, no
   `public`), so the extractor correctly omits its definition yet still names it. The render is
   therefore self-inconsistent, and an LLM has no way to learn that a replacement callback has
   signature `isolated function (regex:Match) returns string`. `old` was equally dangling (it just
   spelled the dangling name as `ballerina/regex:1.4.3:ReplacerFunction`); arguably `new`'s
   unqualified form reads more like a locally-declared type and is slightly more misleading, but
   neither form resolves. The right fix would be to inline the function type.
2. **`Groups.count` is missing.** `types.bal:31` declares a public object field `int count;` on
   `Groups`. Neither render mentions it (`grep -c count` = 0 in both). Since `get(i)` panics for
   `i > count`, this is materially useful API that is invisible.
3. **`Groups` is rendered as a `class` with a bodyless method — not valid Ballerina.** Source is
   `public type Groups readonly & object { ... }` (an object *type*, `types.bal:29`). The render
   emits `class Groups { function get(...); }` (`new:60-63`). A Ballerina `class` cannot have an
   abstract method, and the `readonly &` intersection is dropped, so the render implies `Groups` is
   instantiable/mutable when it is a read-only object type users only ever receive.
4. **Doc-comment continuation lines lose their `#` prefix.** 7 lines in each render
   (`new:109, 112, 129, 132, 148, 150, 152`, e.g. bare `substring that matches the provided regex`)
   sit outside any comment, breaking the rendered file as parseable Ballerina and orphaning half of
   four `+ param -` descriptions. Source has them correctly continued (`natives.bal:48-52`).
5. **Closed records rendered as open.** `PartMatch` and `Match` are `record {| ... |}` in
   `types.bal:21` and `:44`; both renders emit `record { ... }`. An LLM would believe rest fields are
   allowed.
6. **`isolated` / `public` qualifiers are dropped everywhere** (`grep -c isolated` = 0,
   `grep -c "public "` = 0 in both renders), although every exported function is
   `public isolated function`. Isolation matters for use inside `isolated` contexts.
7. **`replaceFirst`'s deprecation rationale is dropped.** Source carries
   `# # Deprecated` / `# This function will be removed in a later. Use \`replace\` instead.`
   (`natives.bal:125-126`). The renders keep the bare `@deprecated` annotation but not the "use
   `replace` instead" guidance (`grep -i "will be removed in a later"` = 0 matches in both).

## 6. Coverage gaps vs. the library

The bala's `modules/` directory contains exactly one module, `regex`, which is the package's default
module (`package.json` `"export": ["regex"]`; Central `modules[]` lists only `regex`). **There is no
submodule API**, so the shared `getDefaultModule()`-only limitation costs this library nothing.

Public symbols in the default module vs. the renders:

| Symbol | Source | In renders? |
|---|---|---|
| `matches`, `replace`, `replaceAll`, `replaceFirst`, `split`, `search`, `searchAll` | `natives.bal` (7 `public isolated function`) | all 7 present |
| `PartMatch`, `Groups`, `Match`, `Replacement` | `types.bal` (4 `public type`) | all 4 present |

**Declaration-level coverage gaps: 0.** Every `public` top-level symbol in `natives.bal`,
`types.bal` and `utils.bal` appears in both renders.

**Member-level coverage gap: 1** — the public field `Groups.count` (`types.bal:31`), missing from
both renders (§5.2).

Correctly excluded (non-public, so not part of the API surface): `ReplacerFunction` (`types.bal:50`),
`readonly class MatchGroups` (`utils.bal:39`), and the module-private helpers/externals
`getSubstring`, `getReplacementString`, `getMatcher`, `getPartMatch`, `matchesExternal`,
`replaceFirstExternal`, `splitExternal`, `getBallerinaStringArray`, `getMatcherFromPattern`,
`isMatched`, `getGroup`, `getStartIndex`, `getEndIndex`, `regexCompile`, `getGroupStartIndex`,
`getGroupEndIndex`, `getGroupCount`.

## 7. Compiler plugin

**None.** `has_plugin: false` in the manifest is confirmed against the bala: `ls -a` on
`.../regex/1.4.3/java11/` yields exactly `bala.json`, `dependency-graph.json`, `deprecated.txt`,
`docs`, `modules`, `package.json` — there is no `compiler-plugin/` directory and no
`compiler-plugin.json`. The upstream `v1.4.3` tag likewise has no `compiler-plugin`,
`*-compiler-plugin` or `ballerina-*-compiler-plugin` directory (repo root is `LICENSE`, `README.md`,
`ballerina`, `build-config`, `build.gradle`, `changelog.md`, `codecov.yml`, `docs`, `examples`,
`gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `settings.gradle`, `spotbugs-exclude.xml`).
Nothing plugin-related is therefore expected in, or absent from, the render.

## 8. Other considerations

- **The package is deprecated.** The bala ships a `deprecated.txt`
  ("This library is deprecated and will no longer be maintained or updated. Instead, it is
  recommended to use the ballerina/lang.regexp."), and Central reports `"isDeprecated": true` with
  the same `deprecateMessage`. Neither render surfaces this as structured metadata — it survives
  only because the README text happens to lead with a "**Deprecation Notice:**" blockquote (present
  twice, once from the package readme and once from the module readme). That is enough for an LLM to
  notice, but a machine-readable deprecation flag would be safer. Worth confirming with the owner
  whether a deprecated library should be in the render set at all; per instructions I have not
  changed the list.
- **Redundant README duplication.** The deprecation blockquote and the two near-identical overview
  paragraphs appear twice (render lines 7-16 from the package readme and 33-39 from the module
  readme), costing ~20 of 204 lines. This mirrors Central's own data and is identical on both sides.
- **Size/token impact is negligible**: +2 rendered lines, +558 JSON bytes (+3.6%). No token concern.
- **`replaceFirst` is `@deprecated` at function level too**, and correctly marked in both renders.
- **Version pin is stable**: 1.4.3 is the latest published version, built for `ballerina_version`
  2201.5.0, `graalvmCompatible: "Yes"`, `platform: java11`.
- The `search`/`replace` `startIndex = 0` default is preserved on both sides, which is the one
  non-obvious signature detail an LLM needs; good.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l regex/{old,new}/ballerina_regex.bal.txt` | 202 / 204 |
| 2 | `diff -u old/ballerina_regex.bal.txt new/ballerina_regex.bal.txt` | 2 hunks, +3 −1; only `Groups.get` added and `Replacement` union member renamed |
| 3 | `diff <(python3 -m json.tool old/...json) <(python3 -m json.tool new/...json)` | 2 hunks; `Groups.functions[get]` added; `ballerina/regex:1.4.3:ReplacerFunction` → `ReplacerFunction` |
| 4 | `wc -c old/*.json new/*.json` | 15,629 → 16,187 bytes |
| 5 | `grep -c '^// Unknown type:'` both renders | 0 / 0 |
| 6 | `grep -cE '^(public )?function ' ` both renders | 7 / 7 |
| 7 | `grep -nE '^(type\|class\|enum\|const\|annotation\|listener\|service) '` both | old: PartMatch@50, Groups@60, Match@67, Replacement@76; new: PartMatch@50, Groups@60, Match@69, Replacement@78 |
| 8 | `ls -R /Users/admin/.ballerina/.../regex/1.4.3` | single platform dir `java11`; `modules/regex/{natives,types,utils}.bal` |
| 9 | `ls -a .../1.4.3/java11/` | no `compiler-plugin/` → `has_plugin:false` confirmed |
| 10 | `cat .../java11/deprecated.txt` | package deprecated; recommends `ballerina/lang.regexp` |
| 11 | `cat .../java11/package.json` | version 1.4.3, `"export": ["regex"]`, platform java11, ballerina_version 2201.5.0 |
| 12 | `git clone --depth 1 --branch v1.4.3 <repo> <scratch>/src` | tag exists, clone OK |
| 13 | `diff bala/modules/regex/<f>.bal src/ballerina/<f>.bal` for natives/types/utils | all three IDENTICAL |
| 14 | `grep -n "version" src/ballerina/Ballerina.toml src/gradle.properties` | `1.4.3` in both |
| 15 | `grep -n "public type Groups" -A 12 src/ballerina/types.bal` | `readonly & object`, `int count;` @31, `public isolated function get(int index) returns PartMatch?;` @36 |
| 16 | `grep -n "^public isolated function" src/ballerina/natives.bal` | 7 public functions @33/55/89/128/146/166/197; `@deprecated` @127 |
| 17 | `sed -n '40,60p;120,132p;155,170p' src/ballerina/natives.bal` | `replace(... int startIndex = 0)`, `search(... int startIndex = 0) returns Match?`, `# # Deprecated / This function will be removed in a later.` @125-126 |
| 18 | `grep -cE '^(substring\|substrings\|used\|be replaced\|matches the regex)'` both renders | 7 / 7 malformed doc-continuation lines (unchanged) |
| 19 | `grep -c "count"` / `"readonly"` / `"isolated"` / `"public "` both renders | 0 / 0 / 0 / 0 on both sides |
| 20 | `grep -i "will be removed in a later\|# Deprecated"` both renders | 0 matches on both sides |
| 21 | `grep -ci deprecated` both renders | 3 / 3 (2 README notices + 1 `@deprecated`) |
| 22 | `curl api.central.ballerina.io/2.0/registry/packages/ballerina/regex/1.4.3` | `isDeprecated: true`; `modules: [regex]` only; graalvmCompatible Yes; readme matches render |
| 23 | Python read of `new/ballerina_regex.json` top-level | `clients: []`, `services: []`, `annotations: []`, 4 typeDefs, 7 functions |
| 24 | `OLD_AND_NEW_DIFFS/regex_diff.md` cross-check | its figures (202/204, +3/−1, 2 hunks, 1→0 qualified refs, 1 decl added) all reproduced independently — accurate |

## 10. Caveats and unverified items

- The renders were not compiled. Claims that the emitted text is not valid Ballerina (§5.3 bodyless
  method in a `class`, §5.4 un-prefixed doc continuations) are from reading the language rules and
  the rendered text, not from running `bal build`. The renders are stub/summary artifacts and are
  presumably not meant to compile, so these are fidelity observations, not build failures.
- I did not run the two-stage pipeline myself; I audited the committed `old`/`new` JSON and
  `.bal.txt` artifacts as given. That the `old` side was produced from `eb5d81b3` and `new` from
  `412ba01e` is taken from the brief and was not independently verified.
- §5.1's judgement that `new`'s unqualified `ReplacerFunction` is *marginally* more misleading than
  `old`'s version-qualified dangling name is an opinion; both are objectively unresolvable
  references, and I did not count it as a regression.
- Central's `balaURL` was not downloaded and re-hashed against the local cached bala; equivalence of
  the local bala to the published artifact rests on the local bala being byte-identical to the
  `v1.4.3` git tag (evidence #13), which is strong but indirect.

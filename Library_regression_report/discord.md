# ballerinax/discord 2.0.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/discord` |
| Pinned version | `2.0.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-discord |
| Tag reviewed | `v2.0.1` (commit `2c2de1a0`, peeled `eebdc5d6`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/discord/2.0.1` |
| Old render | `5779` lines |
| New render | `7142` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is a strict superset of `old` in information content. The declaration *set* is byte-for-byte
identical in scope: 935 type definitions and 183 client resource methods + `init` on both sides,
matching exactly the 935 `public type` and 183 `resource isolated function` declarations in the
bala's default module. Every one of the 805 lines removed by `new` falls into one of three
mechanical categories, all of which were defects in `old`:

- 421 `// Unknown type: X` placeholders replaced by real singleton/alias definitions,
- 351 lines carrying non-compiling version-qualified references (`ballerinax/discord:2.0.1:X`,
  `ballerina/lang.int:0.0.0:Signed32`) replaced by clean `X` / `int:Signed32`,
- 31 client resource signatures carrying a fabricated `anydata Additional Values` parameter that
  does not exist in the library source.

`new` additionally recovers 1,191 annotation lines (`@jsondata:Name`, `@constraint:*`, `@http:Query`,
`@http:Header`, `@display`) that `old` dropped entirely — these are wire-format and validation
semantics an LLM cannot infer from the Ballerina field names alone. **No regressions found.**

## 2. Change inventory

Line counts (`wc -l`): old `5779`, new `7142`. Diff: 805 removed, 2168 added, 145 hunks.

### Declaration sets (identical)

| Kind | bala (source of truth) | old render | new render |
|---|---|---|---|
| Public type definitions | 935 | 935 | 935 |
| — of which record types | 369 declared `record` (+2 aliases expanded to records) | 371 | 371 |
| — of which union types (`members`) | — | 143 | 143 |
| — of which singleton/alias (`baseType`) | — | 421 (as `Other`, no body) | 421 (with body) |
| Client classes | 1 (`Client`) | 1 | 1 |
| `resource` methods on `Client` | 183 | 183 | 183 |
| `init` | 1 | 1 | 1 |
| Public standalone functions / services / listeners / annotations | 0 | 0 | 0 |

Set difference of type names between the two renders (after folding `// Unknown type: X` into the
name set): **0 added, 0 removed**.

JSON level (`typeDefs` array): old 935 / new 935; `clients` 1/1; `functions`, `services`,
`annotations` 0/0 on both. `readme` and `description` byte-identical.

### Removed lines — full classification (805 = 805, nothing unaccounted)

| Category | Count |
|---|---|
| `// Unknown type: X` placeholders | 421 |
| Lines containing `ballerinax/discord:2.0.1:` or `ballerina/lang.int:0.0.0:` qualifiers | 351 |
| Client signatures containing `anydata Additional Values` | 31 |
| Blank lines | 2 |
| **Anything else (i.e. real content loss)** | **0** |

### Added lines — full classification (2168 = 2168)

| Category | Count |
|---|---|
| `@jsondata:Name {value: "..."}` | 930 |
| `@constraint:String` / `@constraint:Int` / `@constraint:Array` | 225 |
| `@http:Query` (29) + `@http:Header` (5) | 34 |
| `@display` | 2 |
| `type X ...;` declarations (421 newly-materialised + 101 re-emitted without qualifiers) | 522 |
| Doc-comment lines (`# ...`) | 172 |
| Blank | 2 |
| Other declaration/field lines (31 corrected resource signatures; remainder record fields re-emitted with `int:Signed32` / unqualified type refs) | 281 |

Doc-comment total across the file: old `429` → new `601` (+172, all attached to the 421
previously-degraded types).

### Per-type structural comparison

Parsing both renders into per-type blocks and normalising away (a) module/version qualifiers,
(b) annotation lines, (c) `int:Signed32` vs `Signed32`:

- 189 types byte-identical before any normalisation,
- 421 differ because `old` was a bare `// Unknown type:` stub,
- 195 differ *only* by the annotations `new` adds,
- 130 differ *only* by `Signed32` → `int:Signed32`,
- **0 types remain structurally different** after normalisation.

## 3. Correctness against library source

Upstream `v2.0.1` and the bala are the same bytes — `diff` on `ballerina/types.bal`,
`ballerina/client.bal`, `ballerina/utils.bal` vs `modules/discord/*.bal` reports **IDENTICAL** for
all three files. So GitHub-vs-bala disagreement is not a concern here.

Checks performed:

1. **All 935 public types accounted for.** Set of `^public type X` in the bala (935 names) equals
   the set of `^type X` in `new` (935 names); symmetric difference empty in both directions.
2. **Singleton types `new` materialised are real.** Exhaustive machine comparison of every
   single-line `type X <body>;` in `new` (564) against `^public type X <body>;` in
   `types.bal` (566): 8 name mismatches (see §5, quoted-identifier issue) and 75 body mismatches,
   all of which are the shared `anydata?` → `anydata|()` normalisation and inline expansion of
   `anydata?` aliases — both present identically in `old`. No invented values.
   Hand-verified 12 random samples, e.g. `types.bal:807 public type ACCEPTED 2;` ↔ `new:1908
   type ACCEPTED 2;`; `types.bal:4649 VOICE1 2`; `types.bal:197 INSTAGRAM "instagram"`;
   `types.bal:621 ZEROES "0000"`; `types.bal:1939 Tr "tr"`; `types.bal:4164 SOUNDBOARDSOUNDCREATE
   130`; `types.bal:5830 SpamLinkRuleResponseExemptchannelsItemsString string`.
3. **Record fields.** For every record in the bala, field-name set ⊆ field-name set in `new`:
   0 records lose fields (the single flagged case, `ConnectionConfig`, is a parser artifact of
   default-value syntax — manual `awk` extraction shows `old` and `new` bodies are character-identical).
4. **Annotations are real, not invented.** Bala counts: 922 `@jsondata:Name`, 223 `@constraint:`,
   29 `@http:Query`, 5 `@http:Header`, 2 `@display`. Render `new`: 930 / 225 / 29 / 5 / 2. The +8
   / +2 delta is fully explained by the two alias types that the renderer expands into full record
   copies (`InlineResponseItems2001` = `EntitlementResponse`, 8 `@jsondata:Name` + 1 `@constraint:`;
   `GuildTemplateChannelResponsePermissionOverwrites` = `ChannelPermissionOverwriteResponse`,
   1 `@constraint:`) — a duplication that is present in `old` too. `@http:Query`/`@http:Header`/
   `@display` counts match exactly.
   Spot-checked placement: `types.bal:320-321 @constraint:String {pattern: re
   \`^(0|[1-9][0-9]*)$\`} public type PrivateGuildMemberResponseRolesItemsString string;` ↔
   `new:1020-1021`; `types.bal:2083-2084 RolesOneOf13` ↔ `new:460-461`.
5. **The 31 corrected client signatures.** `client.bal:94` reads
   `resource isolated function get users/\@me/guilds(map<string|string[]> headers = {},
   *ListMyGuildsQueries queries) returns MyGuildResponse[]|error`. `ListMyGuildsQueries`
   (`types.bal:3982-3991`) is a **closed** four-field record with no rest field. `old` emitted an
   extra `anydata Additional Values` parameter; there is no such parameter in the source. `new`
   removes it. Same pattern verified across all 31 affected methods (all take `*<X>Queries queries`).
6. **README / header.** Lines 1-112 (banner, description, README block) are byte-identical between
   the two renders; JSON `readme` fields compare equal.

## 4. Regressions

**None found.**

Basis for that conclusion — each of the following was checked and came back clean:

- Type-name set difference old→new: 0 removed (`comm -23` on sorted name lists, including
  `// Unknown type:` names folded in).
- Client method count: 183 in both; `diff` of the two `// --- Client ---` sections yields exactly
  31 changed line pairs, all of them the `anydata Additional Values` removal, and nothing else.
- Per-type body comparison after normalising qualifiers/annotations/`int:Signed32`: 0 types
  structurally different, i.e. no field, no return type, no union member, no default value was
  dropped.
- Removed-line classification: 805/805 lines accounted for by the three defect categories + 2
  blanks; the "other" bucket is empty.
- Doc comments: monotonically increased (429 → 601); no `# ` line present in `old` is absent in `new`
  (all removed lines are accounted for above, none is a doc line).
- README/description/section markers: identical, 4 markers on both sides.
- Non-ASCII / mojibake: 0 occurrences in both files.
- `// Special Agent Note:` cross-package hints: 19 in both.

## 5. Issues in `new` (independent of `old`)

Seven issues exist in `new`. **Six of the seven are present identically in `old`** and are therefore
shared renderer/extractor limitations, not something `new` introduced. Only issue 1 is new-side.

1. **Unimported module prefixes (new-side, cosmetic).** The render declares only
   `import ballerinax/discord;` (line 5) yet now uses the prefixes `jsondata:`, `constraint:` and
   `int:` (in addition to `http:`, which `old` also used unimported). The rendered text is a
   reference artefact rather than a compilation unit, and `old` was strictly worse (it emitted
   fully version-qualified refs such as `ballerinax/discord:2.0.1:UserResponse`, which are not
   legal Ballerina at all), so this is a net improvement — but the file still would not compile
   as-is.
2. **Quoted identifiers rendered unquoted (shared).** 8 types whose source names begin with a digit
   are declared `public type '200AnyOf4 anydata?;` (`types.bal:469`, `:2048`, …) but render as
   `type 200AnyOf4 anydata|();` — an illegal identifier. Present at `old:1043` and `new:1257`, etc.
   Identical on both sides.
3. **Type aliases expanded into record copies (shared).** `public type InlineResponseItems2001
   EntitlementResponse;` (`types.bal:5022`) and `public type
   GuildTemplateChannelResponsePermissionOverwrites ChannelPermissionOverwriteResponse;`
   (`types.bal:4808`) render as full duplicated record bodies in both `old` and `new`, losing the
   alias relationship and inflating the output.
4. **`isolated` qualifier dropped (shared).** Source declares `public isolated client class Client`
   and `resource isolated function ...` for all 183 methods; both renders emit `client class Client`
   and `resource function ...`.
5. **Included-record parameter rendered twice (shared).** Source
   `*ListMyGuildsQueries queries` is rendered as the flattened fields *and* an additional
   `ListMyGuildsQueries queries` parameter, e.g. `new:6425`:
   `resource function get users/\@me/guilds(map<string|string[]> headers = {}, boolean withCounts =
   false, string before = "", int:Signed32 limit = 0, string after = "", ListMyGuildsQueries
   queries)`. The `*` sigil is lost, so the signature is ambiguous/duplicated. Identical in `old`
   (which additionally had the bogus `anydata Additional Values`). An LLM could plausibly generate
   a call passing both forms.
6. **`ConnectionConfig` default values dropped (shared).** `timeout = 30`, `validation = true`,
   `laxDataBinding = true`, `httpVersion = HTTP_2_0`, etc. appear without defaults in both renders.
7. **One doc comment loses its `#` continuation prefix (shared).** In `ConnectionConfig`, the
   `laxDataBinding` doc wraps onto a second line rendered as bare text
   (`and absent fields are handled as \`nilable\` types. Enabled by default.`) with no leading `#`,
   in both `old` and `new`.

## 6. Coverage gaps vs. the library

**None.**

- The bala exports exactly one module: `package.json` `"export": ["discord"]`, and
  `any/modules/` contains only `discord/` (files `client.bal`, `types.bal`, `utils.bal`). There is
  no submodule API, so the known `getDefaultModule()`-only limitation costs nothing here.
- 935/935 public types present in both renders.
- 183/183 `resource` methods + `init` present in both renders.
- `utils.bal` (332 lines) declares no `public` symbols; nothing missing from it.
- No public standalone functions, enums (`enum` keyword), constants, annotations, listeners or
  services exist in the source, and none are invented by the render.

## 7. Compiler plugin

The package ships **no compiler plugin**. Evidence:

- `find` over the `v2.0.1` clone for `*compiler*plugin*` returns nothing; the repo tree is
  `ballerina/`, `build-config/`, `docs/`, `examples/`, `gradle/`.
- `ballerina/Ballerina.toml` has no `[[plugin]]` / `[platform.*]` compiler-plugin entry.
- The bala's `any/` directory contains only `bala.json`, `dependency-graph.json`, `docs/`,
  `modules/`, `package.json` — no `compiler-plugin/compiler-plugin.json`.

Consequently there are no plugin-contributed code actions, validations, generated artefacts or
annotations that the render could be missing. The only annotations in play are from
`ballerina/jsondata`, `ballerina/constraint`, `ballerina/http` and `ballerina/lang` `@display`, and
`new` reproduces all of them (§3.4).

## 8. Other considerations

- **Not deprecated.** Central metadata for `ballerinax/discord/2.0.1`: `"deprecated": null`,
  `"deprecateMessage": ""`, `pullCount` 50, single module `discord`, bala format 3.0.0.
- **Stable major version** (2.0.1), so no pre-1.0 churn caveat.
- **Size / token impact.** 184,323 → 227,491 bytes of rendered text (+23.4%); JSON 1,059,339 →
  1,284,907 bytes (+21.3%). This is a real prompt-budget cost, but the added bytes are
  high-value: 1,191 annotation lines (wire names + validation constraints) and 421 previously-empty
  type bodies. The library is dominated by 421 machine-generated singleton types (`type ACCEPTED
  2;`) and OpenAPI-derived helper aliases (`…ItemsString`, `…OneOf…`), so much of the growth is
  boilerplate that `old` simply hid behind `// Unknown type:` lines.
- **Practical significance of the `@jsondata:Name` recovery.** 930 fields in this connector have a
  camelCase Ballerina name that differs from the Discord wire name (`guildId` ↔ `guild_id`). `old`
  showed none of the mappings. This is the single largest accuracy gain of `new` for this library.
- **Practical significance of the `Additional Values` removal.** `old` fed an LLM 31 client method
  signatures containing a two-token parameter with a space in its name (`anydata Additional
  Values`) — syntactically impossible Ballerina that would have produced uncompilable generated
  code. That defect is gone in `new`.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ new/ *.bal.txt` | 5779 / 7142 |
| `grep -c '^// Unknown type:'` old / new | 421 / 0 |
| `grep -n '^// --- '` old / new | 4 markers each (README, END README, Types, Client) at 7/112/114/5042 (old) and 7/112/114/6405 (new) |
| `git ls-remote --tags …module-ballerinax-discord` | `v1.0.0`, `v2.0.0`, `v2.0.1` → exact tag `v2.0.1` exists |
| `git clone --depth 1 --branch v2.0.1` | succeeded |
| `diff src/ballerina/{types,client,utils}.bal bala/modules/discord/` | all three **IDENTICAL** |
| `wc -l bala modules/discord/*.bal` | client 3086, types 5897, utils 332 |
| `ls bala/any/modules/` | only `discord` → single default module, no submodules |
| `grep -c '^public type' types.bal` | 935 |
| type-name set: `comm -23 old.types new.types` / `comm -13` | 0 / 0 (935 each) |
| bala public-type names vs render type names (Python set diff) | symmetric difference empty both directions |
| `grep -cE '^\s+(resource\|remote) (isolated )?function'` bala / old / new | 183 / 183 / 183 |
| Python per-type block diff (qualifier-normalised) | 935 vs 935 decls; 189 identical, 746 differing |
| …further normalised for annotations + `int:Signed32` | **0 structurally different** |
| Breakdown of the 746 | 421 unknown-expanded, 195 annotation-only, 130 `Signed32`-only |
| Removed-line classifier (awk over `diff -u`) | unknown=421, qualified=351, `Additional Values`=31, blank=2, **other=0** |
| Added-line classifier | jsondata=930, constraint=225, http=34, display=2, `type`=522, doc=172, blank=2, other=281 (sums to 2168) |
| `grep -c 'Additional Values'` old / new | 31 / 0 |
| `diff` of Client sections | 738 lines each; exactly 31 changed pairs, all the `Additional Values` fix |
| `client.bal:94` | `resource isolated function get users/\@me/guilds(map<string\|string[]> headers = {}, *ListMyGuildsQueries queries) returns MyGuildResponse[]\|error` — no rest/extra param |
| `types.bal:3982-3991` `ListMyGuildsQueries` | closed record, 4 fields, no rest field |
| Qualified-ref census in `old` | 574 × `ballerinax/discord:2.0.1:`, 247 × `ballerina/lang.int:0.0.0:` (821 total); 0 in `new` |
| `grep -cE '(^\|[^:a-zA-Z])Signed32'` new | 0 (all 261 occurrences are `int:Signed32`) |
| Annotation counts bala vs new | jsondata 922/930, constraint 223/225, http:Query 29/29, http:Header 5/5, display 2/2 |
| Δ8 / Δ2 explanation | `InlineResponseItems2001` + `GuildTemplateChannelResponsePermissionOverwrites` alias-to-record expansion (present in `old` too) |
| Record field-set check (369 bala records vs `new`) | 0 records lose fields |
| Doc lines `^\s*# ` old / new | 429 / 601 |
| `diff` README block lines 7-112 | IDENTICAL |
| JSON `typeDefs`/`clients`/`functions`/`services`/`annotations` old vs new | 935/935, 1/1, 0/0, 0/0, 0/0; `readme` and `description` equal |
| JSON typeDef shape old | 421 × `{description,name,type}` (all `type:"Other"`, no body), 371 × fields, 143 × members |
| JSON typeDef shape new | 405 × `{baseType,…}` + 16 × `{annotations,baseType,…}` (= 421, all `type:"Other"`), 370+1 × fields, 143 × members |
| `types.bal:320-321` vs `new:1020-1021` | `@constraint:String` on `PrivateGuildMemberResponseRolesItemsString` matches |
| `types.bal:2083-2084` vs `new:460-461` | `@constraint:String` on `RolesOneOf13` matches |
| Hand-verified singletons | `ACCEPTED 2` (types.bal:807), `VOICE1 2` (:4649), `TALK 1` (:3454), `INSTAGRAM "instagram"` (:197), `GUILDDISCOVERYGRACEPERIODINITIALWARNING 16` (:3123), `ZEROES "0000"` (:621), `QUESTREWARD 10` (:2118), `Tr "tr"` (:1939), `NONE2 0` (:2639), `SOUNDBOARDSOUNDCREATE 130` (:4164), `BulkBanUsersResponseBannedusersItemsString string` (:4197), `MESSAGESEND 1` (:2801) — all match `new` |
| `find` for compiler plugin in clone; `ls bala/any/` | none found; no `compiler-plugin/` in bala |
| `grep -cP '[^\x00-\x7F]'` old / new | 0 / 0 |
| `grep -c 'Special Agent Note'` old / new | 19 / 19 |
| `grep -n '^import'` old / new | line 5 and line 66 (README sample), `import ballerinax/discord;` only, both sides |
| Central API `…/packages/ballerinax/discord/2.0.1` | `deprecated: null`, 1 module `discord`, balaVersion 3.0.0 |
| `ls -la` render/JSON sizes | .bal.txt 184,323 → 227,491 B; .json 1,059,339 → 1,284,907 B |

## 10. Caveats and unverified items

- **Verified with a caveat on scope:** the per-type comparison in §2 was done with a purpose-built
  parser that recognises `type X …;` and `type X record { … };` blocks. It handles every declaration
  form present in this render (935/935 types matched, 0 unparsed), so coverage is complete for this
  library, but the parser is not a general Ballerina parser.
- The `Client` class body was compared as a whole-section `diff` rather than per-method AST; since
  the section is line-for-line aligned (738 lines each, 31 changed pairs) this is exhaustive for
  this library, but it would not detect a reordering that happened to preserve line counts. No
  evidence of reordering was seen.
- I did **not** attempt to compile either render. Statements about "non-compiling" syntax
  (`ballerinax/discord:2.0.1:X`, `anydata Additional Values`, `type 200AnyOf4`, missing imports) are
  based on reading the Ballerina grammar, not on running `bal build`.
- The claim that the two sides were produced from commits `eb5d81b3` / `412ba01e` of
  `ballerina-vscode` is taken from the brief; I did not inspect either extractor/renderer source
  tree, so attributions of *cause* ("spec v2 does X") rest on the brief plus the observed output,
  not on reading the renderer code.
- Central's `pullCount` (50) and `createdDate` are informational only; not used in any conclusion.

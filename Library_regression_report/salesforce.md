# ballerinax/salesforce 8.7.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/salesforce` |
| Pinned version | `8.7.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-salesforce |
| Tag reviewed | `v8.7.0` (exact tag; commit `9089c81a2f859779b3cc2a3b3c78f7ccf3b06ea1`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/salesforce/8.7.0` |
| Old render | `1769` lines |
| New render | `1985` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Nothing present in `old` was dropped: the
top-level declaration name sets are byte-identical (98 entries each) and the README block
(lines 1–739) is identical. All 20 removed lines in the diff are replaced by corrected versions of
the same declarations.

Four categories of improvement, all verified against upstream `v8.7.0`:

1. Four `// Unknown type:` placeholders (`Error`, `Listener`, `InMemoryCoordinator`,
   `InMemoryTokenStore`) become real definitions; `Error` gains its `baseType`
   (`error<ErrorDetails>`) and `Listener` gains its `@display` annotation and all 10 methods.
2. 35 previously-invisible member functions are emitted across 7 classes.
3. Three **mangled, non-compiling** return types in `old` are fixed
   (`returns Limit>|error` → `returns map<Limit>|error`, etc.).
4. 11 version-qualified type refs (`ballerinax/salesforce:8.7.0:ReplayOptions`) become plain
   references; `string object` becomes the correctly-quoted `string 'object`.

The bala's default module is byte-identical to upstream `v8.7.0` (15/15 `.bal` files `diff`-clean),
so signature checks against GitHub are authoritative here.

## 2. Change inventory

Line counts: `old` 1769, `new` 1985 (+216). Diff: 15 hunks, 206 added lines, 20 removed lines.

### Top-level declarations

| | old | new |
|---|---|---|
| Distinct top-level names | 98 | 98 |
| `type` | 43 | 44 |
| `class` (incl. `client class Client`) | 4 | 7 |
| `enum` | 9 | 9 |
| `const` | 33 | 33 |
| `// Unknown type:` placeholders | 4 | 0 |
| `service` blocks | 1 | 1 |
| module-level `function` | 0 | 0 |
| `annotation` | 0 | 0 |

`comm` on the sorted top-level name lists: **removed = 0**. The only asymmetry is the 4
placeholders becoming 4 real declarations:

```
only in old: // Unknown type: Error / InMemoryCoordinator / InMemoryTokenStore / Listener
only in new: type Error, class InMemoryCoordinator, class InMemoryTokenStore, class Listener
```

### Member functions (per class)

| class | old | new | delta |
|---|---|---|---|
| `ListenerCoordinator` | 0 | 5 | +5 |
| `TokenStore` | 0 | 5 | +5 |
| `CdcService` | 0 | 4 | +4 |
| `PlatformEventsService` | 0 | 1 | +1 |
| `InMemoryCoordinator` | (absent) | 5 | +5 |
| `Listener` | (absent) | 10 | +10 |
| `InMemoryTokenStore` | (absent) | 5 | +5 |
| `Client` | 47 | 47 | 0 |
| **total** | 47 | 82 | **+35** |

Diff-level: 42 added `function`/`remote function` lines, 7 removed — the 7 removed are the 3
mangled `Client` signatures and the 4 `Service`-section handlers, each re-emitted corrected.

### Modified (not removed) declarations — 7

| decl | old | new |
|---|---|---|
| `Client.getLimits` | `returns Limit>|error` | `returns map<Limit>|error` |
| `Client.createQueryJobAndWait` | `returns BulkJobInfo\|error>\|error` | `returns future<BulkJobInfo\|error>\|error` |
| `Client.closeIngestJobAndWait` | `returns BulkJobInfo\|error>` | `returns error\|future<BulkJobInfo\|error>` |
| `OAuth2Config` | `ballerina/http:2.16.6:BearerTokenConfig\|…` | `http:BearerTokenConfig\|oauth2:…` |
| `ListenerConfig` / `Service` | `ballerinax/salesforce:8.7.0:X\|…` | `X\|…` |
| `replayFrom` field (×4 records) | `int\|ballerinax/salesforce:8.7.0:ReplayOptions` | `int\|ReplayOptions` |
| `BulkJob.object` / `BulkJobInfo.object` | `string object;` | `string 'object;` |

### Service section

`new` adds `salesforce:` module qualification to the listener config type and the handler payload
types, and restores the `# + payload - The information about the triggered event` parameter docs
that `old` omitted.

### JSON diff

Both JSONs carry 92 `typeDefs`, 1 client (47 functions, identical name sets), 1 service, 0 module
functions, 0 annotations, and an identical 29 965-char `readme`. 16 typeDefs differ; `new` adds two
schema keys, `baseType` and `annotations`. Notably `old`'s `Listener` typeDef had **no `type` key at
all** — which is exactly why `renderTypeDef` in `main` degraded it to `// Unknown type: Listener`
despite the JSON already carrying its 10 functions. `new` sets `"type": "Class"`.

## 3. Correctness against library source

Bala default module == upstream `v8.7.0` `ballerina/*.bal`, all 15 files `diff`-identical, so the
citations below are equally valid for both.

| render (new) | source | verdict |
|---|---|---|
| `type Error error<ErrorDetails>;` | `errors.bal:18` `public type Error error<ErrorDetails>;` | exact |
| `ListenerCoordinator.attemptLeadership(string, string, decimal) returns boolean\|error` | `coordination.bal:57-58` | exact |
| `renewLeadership(string,string) returns error?` | `coordination.bal:70` | exact |
| `saveCheckpoint(string,int) returns error?` | `coordination.bal:84` | exact |
| `getCheckpoint(string) returns int\|error?` | `coordination.bal:92` | exact |
| `relinquishLeadership(string,string) returns error?` | `coordination.bal:110` | exact |
| `InMemoryCoordinator` (5 methods) | `coordination.bal:126,132,163,176,191,197` | exact |
| `TokenStore` / `InMemoryTokenStore` (5 methods each) | `token_store.bal:46,55,61,67,74,86,92,97,102,106,112,118` | exact; `getTokenData` rendered `TokenData\|()\|error` vs source `TokenData?\|error` — semantically identical |
| `CdcService` onCreate/onUpdate/onDelete/onRestore | `service_types.bal:22-46` | exact, incl. doc text |
| `PlatformEventsService.onMessage(PlatformEventsMessage) returns error?` | `service_types.bal:52-58` | exact |
| `class Listener` + `@display {label: "Salesforce", iconPath: "icon.png"}` | `listener.bal:29-30` | exact |
| `Listener.init/attach/'start/detach/gracefulStop/reconnect/updateRefreshToken/getRefreshToken/immediateStop/recordEventDispatched` | `listener.bal:54,166,224,254,265,293,311,327,338,363` | all 10 exact; `attach` rendered `string[]\|string\|() name` vs source `string[]\|string? name` — identical |
| `Client.getLimits() returns map<Limit>\|error` | `client.bal:139` | exact (was mangled in `old`) |
| `Client.createQueryJobAndWait(...) returns future<BulkJobInfo\|error>\|error` | `client.bal:599` | exact (was mangled) |
| `Client.closeIngestJobAndWait(string) returns error\|future<BulkJobInfo\|error>` | `client.bal:823` | exact, incl. union order (was mangled) |
| `type OAuth2Config http:BearerTokenConfig\|oauth2:PasswordGrantConfig\|…` | `data_types.bal:31-33` | exact |
| `BulkJob.'object` / `BulkJobInfo.'object` | `types.bal:336`, `types.bal:384` | exact — `object` is a keyword and `old` emitted it unquoted |
| `Client.init(ConnectionConfig config)` | `client.bal:39` | exact param name |
| `client class Client` with 47 fns | `client.bal:27`, 46 `remote function` + `init` | count matches |

Only non-public class in `listener.bal` is `TokenRefreshJob` (`listener.bal:506`) — correctly absent
from both renders.

## 4. Regressions

**None found.**

What was checked to conclude this:
- `comm -23` on sorted top-level declaration name sets: 0 names present in `old` and absent in `new`.
- `diff` of render lines 1–739 (README block): identical, 0 differences.
- All 20 removed lines in `diff -u old new` inspected individually; every one is replaced by a
  corrected form of the same declaration (table in §2). No declaration, parameter, default value,
  return type, doc line, annotation or section marker is lost.
- Per-class member counts: `Client` unchanged at 47; no class loses members.
- JSON: `typeDefs` 92→92 with 0 removals; `clients[0].functions` name set identical (47/47);
  `readme` byte-length identical; `@deprecated` count identical (14 in both).
- Section markers: 5 in both (`README`, `END README`, `Types`, `Client`, `Service`).
- Unbalanced-angle-bracket scan on declaration lines: `old` 3 malformed, `new` 0.

## 5. Issues in `new` (independent of `old`)

All four below are **also present in `old`** — they are pipeline-wide behaviours, not introduced by
spec v2. Listed because they are inaccuracies a consuming LLM would trip on.

1. **`typedesc` inferred-default params rendered as record values.** 8 client methods render
   `record {|anydata...;|} returnType = record {|anydata...;|}` where the source has
   `typedesc<record {}> returnType = <>` (`client.bal:151`, `:303`, `:520`, …; 18 `typedesc<`
   occurrences in `client.bal`). The rendered form does not compile and misstates the parameter's
   type. Identical string in both renders (`grep -c` = 8 on each).
2. **Object types rendered as `class`.** `ListenerCoordinator` (`coordination.bal:27`) and
   `TokenStore` (`token_store.bal:46`) are `public type X isolated object { … }` contracts;
   `CdcService`/`PlatformEventsService` (`service_types.bal:22,52`) are `service object` types. All
   four render as `class`, and the emitted methods drop the mandatory `public isolated` qualifiers
   (`grep -c isolated` = 2 in both renders, both hits inside the README). A reader is told to write
   `class MyCoordinator { function attemptLeadership(...) }` when the contract requires
   `*ListenerCoordinator;` plus `public isolated function`. `new` makes this more visible because it
   now emits the members — but it is a shared renderer limitation, not a `new` regression.
3. **Non-compiling `Service` template** (both sides): `service salesforce:Service on new
   salesforce:Listener(salesforce:ListenerConfig listenerConfig = {auth: {username: "", password:
   ""}})` puts a parameter *declaration* in argument position.
4. **Module prefixes without imports.** `new` emits `http:BearerTokenConfig`,
   `oauth2:PasswordGrantConfig`, `time:Civil`, `io:ReadableByteChannel` with no import lines. The
   renderer partly compensates with inline `// Special Agent Note: Civil FROM ballerina/time
   package` comments, but `oauth2:` and `http:BearerTokenConfig` in `OAuth2Config` carry no such
   note. `old` was more explicit here (`ballerina/oauth2:2.15.0:PasswordGrantConfig`) at the cost of
   invalid syntax — a deliberate trade, not a defect.

Minor/cosmetic, both sides: the 8 enums' members are also flattened into 33 top-level
`const string` declarations (e.g. `const string V2_INGEST = "V2Ingest"` alongside `enum JobType`),
and `getAllJobs`/`getAllQueryJobs` expand `JobType?` to `"V2Ingest"|"Classic"|"BigObjectIngest"|()`.

## 6. Coverage gaps vs. the library

**Default module: 0 gaps.** All 65 `public` declarations in `modules/salesforce/*.bal` (4 classes,
8 enums, 48 types, 5 consts — extracted by regex over the bala source) appear in `new`. The only
name my automated check flagged (`Client`) is a false positive: it is rendered as
`client class Client` under the `// --- Client ---` marker (new render line 1764) and so is not
matched by the top-level `type|class|enum|const` regex.

**Submodule-only API: shared gap, both sides.** `Ballerina.toml` exports 5 submodules that neither
render contains (both extract via `pkg.getDefaultModule()` only):

| module | public declarations |
|---|---|
| `salesforce.types` | 1174 |
| `salesforce.bulkv2` | 17 |
| `salesforce.bulk` | 10 |
| `salesforce.soap` | 8 |
| `salesforce.apex` | 2 |
| **total** | **1211** |

This matters more than usual here: the package README (rendered in full in both files, lines 7–738)
contains worked examples that call `bulk:BulkJob`, `bulkv2:BulkJob`, `soap:ConvertedLead` etc.
(render lines 413, 415, 507, 594) — types the render never defines. A consuming LLM sees the usage
but not the API. `salesforce.utils` is present in the bala's `modules/` but is not exported, so its
absence is correct.

## 7. Compiler plugin

None. `find` over the `v8.7.0` clone returns no `*compiler-plugin*`/`*compiler_plugin*` path, and
the bala contains no `compiler-plugin/` directory (`java21/` holds only `bala.json`,
`dependency-graph.json`, `docs/`, `modules/`, `package.json`, `platform/`). Nothing plugin-derived
is expected in, or missing from, the render.

The package does ship a native Java layer (`salesforce-native-8.7.0.jar`, CometD 8.0.11, Jetty
12.0.33, opencsv, Jackson) bound via `@java:Method`. That is invisible to the render by design; the
Ballerina-visible surface is fully captured.

## 8. Other considerations

- **Deprecations preserved.** 14 `@deprecated` markers in both renders, matching 14
  `@deprecated` occurrences in `client.bal`. Package itself is not deprecated
  (Central `deprecateMessage` empty, `pullCount` 556, created 2026-06-08).
- **Size.** 64 512 → 74 838 bytes (+16.0%) for the render; 167 716 → 181 602 bytes (+8.3%) for the
  JSON. The +216 render lines buy 35 real method signatures plus their contract docs — an
  unambiguously good token trade, especially for `ListenerCoordinator`/`TokenStore`, which are
  user-implemented interfaces that were completely opaque in `old`.
- **README dominates.** 738 of 1985 lines (37%) are README. Unchanged between sides.
- **Version notes.** `8.7.0` is a stable release built on Ballerina `2201.12.0`; the Active-Standby
  coordination API (`coordination.bal`, `token_store.bal`) is new surface in this version and was
  precisely the part `old` rendered as blank/unknown. `Listener.attach` carries a documented
  breaking change (one channel per OAuth2 `Listener` instance) whose doc text is emitted only by
  `new` — a materially useful gain.

## 9. Evidence log

| check | result |
|---|---|
| `wc -l old/new render` | 1769 / 1985 |
| `grep -c '^// Unknown type:'` | old 4, new 0 |
| `grep -n '^// --- '` | 5 markers each, same order |
| `diff -u old new \| wc -l` | 392; `+` 206, `-` 20 |
| `git ls-remote --tags` | `v8.7.0` present → `9089c81a…` (peeled `2b563bca…`) |
| `git clone --depth 1 --branch v8.7.0` | succeeded |
| `diff bala/modules/salesforce/*.bal vs src/ballerina/*.bal` | 15/15 `SAME` |
| `ls bala/java21/modules` | 7 dirs; `package.json` `export` lists 6 (utils not exported) |
| top-level name sets, `comm -23` / `comm -13` | 4 placeholders out, 4 real decls in; 0 true removals |
| per-class member count script | old {LC:0,TS:0,Cdc:0,PE:0,Client:47}; new {LC:5,TS:5,Cdc:4,PE:1,IMC:5,Listener:10,IMTS:5,Client:47} |
| `grep -cE '^\+\s*(remote )?function ' diff` / `^-` | 42 / 7 |
| `diff` render lines 1–739 | identical (README) |
| JSON structural compare (python) | typeDefs 92/92, 0 add/remove, 16 changed; client fns 47/47 identical names; readme 29965 chars both; new adds `baseType`,`annotations` keys |
| JSON `Listener` typeDef | old has no `type` key → placeholder; new `"type":"Class"` |
| `grep -c '@deprecated'` renders | 14 / 14; `client.bal` 14 |
| `grep -n '@display'` | old 0, new 1 (line 1672) |
| unbalanced `<`/`>` on decl lines | old 3 malformed (1578, 1698, 1743), new 0 |
| `grep -c 'returnType = record {|anydata...;|}'` | old 8, new 8 |
| `grep -c 'typedesc<' src/client.bal` | 18 |
| `grep -c isolated` renders | 2 / 2 (README hits only) |
| source public-symbol extraction (python regex over bala `*.bal`) | 65; 0 absent from `new` after resolving `Client` false positive |
| submodule public decl counts | types 1174, bulkv2 17, bulk 10, soap 8, apex 2 = 1211 |
| `find` for compiler plugin | none in clone; none in bala |
| Central API `ballerinax/salesforce/8.7.0` | 200, not deprecated, 6 modules listed, ballerinaVersion 2201.12.0 |
| signature spot-checks | `coordination.bal:27,57,70,84,92,110,126`; `token_store.bal:24,46,55,61,67,74,86,92`; `service_types.bal:18,22,52`; `errors.bal:18`; `listener.bal:29,30,54,166,224,254,265,293,311,327,338,363,506`; `client.bal:27,39,139,151,303,439,520,599,673,730,823`; `data_types.bal:18,29,31`; `types.bal:336,384` |

## 10. Caveats and unverified items

- Signature verification was done against the upstream `v8.7.0` clone after proving it is
  byte-identical to the bala's default module. Doc-comment *wording* was spot-checked (not
  diffed line-by-line) for the 35 newly-emitted member functions; the 5 sampled in §3 matched
  exactly.
- I did not compile either render. "Malformed / non-compiling" claims rest on Ballerina grammar
  reasoning plus the bracket-balance scan, not on `bal build`.
- The `class` vs `object type` and `typedesc` findings in §5 are characterised as shared with `old`
  on the basis that the exact rendered strings are identical in both files; I did not read the
  renderer source to confirm the mechanism.
- Submodule public-declaration counts are `grep -c '^public '` over the bala module sources, i.e.
  line counts of top-level `public` declarations. They exclude multi-line declarations whose
  `public` keyword is not line-initial, so they are lower bounds.
- Central's `deprecated` boolean is absent from the API response; I inferred not-deprecated from the
  empty `deprecateMessage`.

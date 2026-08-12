# ballerinax/aws.s3 4.0.0 — Copilot render regression report

| | |
|---|---|
| Library | `ballerinax/aws.s3` |
| Pinned version | `4.0.0` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerinax-aws.s3 |
| Tag reviewed | `v4.0.0` (commit `0a179fa32b074a300023d215d264f3eb9290d476`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerinax/aws.s3/4.0.0/java21` |
| Old render | `650` lines |
| New render | `677` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` is strictly better than `old` for this library. Four independent improvements, zero losses:

1. All 6 `// Unknown type:` placeholders (the module's error types) are replaced with real type
   definitions carrying their doc comments (old: 6, new: 0).
2. Both version/module-qualified type refs are normalised (`ballerinax/aws:1.0.1:Region` →
   `aws:Region`, `ballerinax/aws.s3:4.0.0:Error?` → `Error?`); old: 2, new: 0.
3. 67 `@display` annotation instances (1 class-level, 19 function-level, 47 parameter-level) are now
   emitted — `old` emitted none. Every one matches the library source exactly.
4. `close()` is now correctly rendered as a normal method. `old` rendered it `remote function
   close()`, which contradicts the source (`public isolated function close()`) and would have made
   an LLM generate `s3Client->close()` instead of `s3Client.close()`.

Nothing present in `old` is missing, truncated, or degraded in `new`. Zero coverage gaps: all 31
public module-level types plus the `Client` class and all 21 of its methods appear in both renders.
Single-module package (`aws.s3` is the default module), so the shared `getDefaultModule()` limitation
costs nothing here. No compiler plugin exists.

## 2. Change inventory

Line counts (`wc -l`): old 650, new 677 (+27). Diff: 4 hunks, 54 lines added, 27 removed.
Section markers identical on both sides (4 each: README / END README / Types / Client).

**Declarations added in `new` (6)** — all type definitions that were `// Unknown type:` stubs in old:

| Kind | Name |
|---|---|
| Error type | `Error` |
| Error type | `NoSuchKeyError` |
| Error type | `BucketAlreadyExistsError` |
| Error type | `BucketAlreadyOwnedByYouError` |
| Error type | `NoSuchBucketError` |
| Error type | `BucketNotEmptyError` |

**Declarations removed in `new`: 0.** Verified by set-differencing extracted declaration names
(`/tmp/decl_old.txt` vs `/tmp/decl_new.txt`: 49 → 55, diff is pure addition) and by set-differencing
extracted function names (22 vs 22; only difference is `remote function close(` → `function close(`).

**Declarations modified in `new` (22):**

| Kind | Count | Change |
|---|---|---|
| Record field type | 1 | `ConnectionConfig.region`: `ballerinax/aws:1.0.1:Region\|string` → `aws:Region\|string` |
| Client class | 1 | gained `@display {label: "AWS S3 Client", iconPath: "icon.png"}` |
| Constructor | 1 | `init` return `ballerinax/aws.s3:4.0.0:Error?` → `Error?` |
| Remote methods | 19 | gained function-level and parameter-level `@display` annotations |
| Normal method | 1 | `close()` demoted from `remote function` to `function` (correct) |

Kind census of the render's `typeDefs` (identical name-set on both sides, 54 entries):
23 Constant, 17 Record, 6 Error, 5 Enum, 3 Union. `clients`: 1 (21 functions). `functions`,
`services`, `annotations` at package level: 0 on both sides.

JSON-level deltas (structural, both files parsed): 7 changed `typeDefs` (the 6 error types gained
`"baseType": "error"`; `ConnectionConfig.region` type name normalised), and the client object gained
an `annotations` key. `readme` byte-identical between old and new (4593 chars) and identical to the
bala's `docs/README.md` (4593 chars after strip). `description` identical.

## 3. Correctness against library source

Upstream `v4.0.0` and the bala are byte-identical for all six `.bal` files (`diff -q` on
`client.bal`, `errors.bal`, `init.bal`, `stream_iterator.bal`, `types.bal`, `utils.bal` — all quiet),
so source citations below are unambiguous.

**The 6 new error types** — `errors.bal:19,22,25,28,31,34`. All six exist, all six doc comments in
the render match the source verbatim. Caveat on the type expression: see §5.1.

**`close()` is not remote** — `client.bal:417` `public isolated function close() returns Error? {`.
`new`'s `function close() returns Error|();` is correct; `old`'s `remote function close()` was wrong.
Both JSONs already classified it `"type": "Normal Function"`, so this is a renderer fix, not an
extractor fix.

**`@display` annotations** — counted in render vs source:

| Level | source (`client.bal`) | `new` render | match |
|---|---|---|---|
| class | 1 (`client.bal:24`) | 1 | yes |
| function | 19 (`grep -cE '^    @display \{label'`) | 19 | yes |
| parameter | 47 | 47 | yes |
| return value | 9 | 0 | omitted (see §5.3) |

`init` and `close` legitimately carry no `@display` in the source, which is why the function count is
19 and not 21. Spot-checked labels: `"AWS S3 Client", iconPath: "icon.png"` (`client.bal:24`),
`"Create Bucket"` (`:40`), `"Bucket Name"` (`:41`), `"Complete Multipart Upload"` / `"Part Numbers"`
/ `"ETags"` (`:390–395`) — all reproduced exactly.

**`ConnectionConfig.region`** — `types.bal:21` onwards; the field is `aws:Region|string region?`
imported from `ballerinax/aws`. `new`'s `aws:Region|string` is the source form; `old`'s
`ballerinax/aws:1.0.1:Region|string` is not valid Ballerina and pins a dependency version that does
not belong in a type reference.

**Client method roster** — 21 functions in both JSONs, matching `client.bal` exactly: `init`,
`createBucket`, `deleteBucket`, `listBuckets`, `getBucketLocation`, `putObjectFromFile`, `putObject`,
`putObjectAsStream`, `getObject`, `deleteObject`, `listObjects`, `createPresignedUrl`,
`getObjectMetadata`, `copyObject`, `doesObjectExist`, `createMultipartUpload`, `uploadPart`,
`uploadPartAsStream`, `completeMultipartUpload`, `abortMultipartUpload`, `close`.

**Enums** — `CannedACL` (7 members), `ObjectOwnership` (3), `StorageClass` (8), `FileFormat` (3),
`HttpMethod` (2) at `types.bal:301,319,329,59,349`. All 5 enum bodies render with all 23 members and
their doc comments, and the 23 members are additionally flattened into module-level
`const string` declarations. Member values verified against `types.bal:295–354`.

**Unions** — `ContentType`, `UploadContent`, `RetrievableType` (`types.bal:50,53,56`). The render
writes `record {}` as `record {|anydata...;|}`, which is the correct semantic expansion of Ballerina's
inclusive-record type. Identical on both sides.

## 4. Regressions

**None found.**

What was checked to conclude that:

- Full `diff -u old new` read end to end (4 hunks, 81 changed lines). Every removed line has a
  strictly more informative replacement; no line is removed without replacement.
- Declaration-name set difference: `diff /tmp/decl_old.txt /tmp/decl_new.txt` → additions only
  (6 lines), no deletions.
- Function-name set difference: 22 vs 22; the only delta is the `remote` qualifier on `close`, and
  removing it matches `client.bal:417`.
- JSON structural comparison: `typeDefs` name-sets equal (54 = 54, empty symmetric difference);
  `clients[0].functions` name-sets equal (21 = 21); `readme` and `description` byte-identical.
- No parameter, default value, or return type is dropped anywhere: the 19 modified remote-method
  lines were compared token-for-token in the diff — the parameter lists are byte-identical apart from
  interleaved `@display {label: "..."}` prefixes.
- Doc comments: 17 record docs, 5 enum docs, 23 constant docs, 21 method docs present on both sides.
- README: identical bytes on both sides and to the bala README.

## 5. Issues in `new` (independent of `old`)

4 issues. None is a regression; #1 is new-only but is still a large net improvement over the
`// Unknown type:` stub it replaces. #2–#4 are shared with `old`.

**5.1 (new-only) Error type hierarchy is flattened.** Source (`errors.bal:19–34`):

```ballerina
public type Error distinct error;
public type NoSuchKeyError distinct Error;      // and 4 siblings
```

Render (`new`, lines 202–217):

```ballerina
type Error error;
type NoSuchKeyError error;                       // and 4 siblings
```

Two losses: `distinct` is dropped, and the five subtypes are re-parented from `Error` to bare
`error`, so the render does not convey that `NoSuchKeyError` etc. are subtypes of `Error`. The
underlying JSON is the source of this — all six carry `"baseType": "error"` rather than the real base
type. Practical impact is small (`Error` is what every method returns, and the doc comments explain
each subtype), and it is still far better than `old`, which emitted nothing at all for these types.

**5.2 (shared) `getObject`'s `targetType` is rendered as a value, not a typedesc.** Source
(`client.bal:186`): `typedesc<RetrievableType> targetType = <>`. Both renders emit
`byte[]|string|json|xml|...|stream<record {|anydata...;|}, error?> targetType = s3:RetrievableType`.
The dependently-typed nature of the parameter is lost, and `= s3:RetrievableType` is not a valid
default expression. An LLM could plausibly emit `check s3->getObject(b, k, string)` — which happens
to be right — but the render does not explain why.

**5.3 (shared) Return-value `@display` annotations omitted.** 9 in the source
(`grep -oE 'returns @display' client.bal` → 9, e.g. `client.bal:61` `returns @display {label:
"Bucket Names"} Bucket[]|Error`); 0 in either render. `new` emits class/function/parameter
annotations but not return-position ones. Cosmetic for LLM consumption.

**5.4 (shared) Detached doc comments on 17 record definitions.** A blank line is emitted between the
record's doc comment and its `type ... record {` line (e.g. `new` lines 219–221). Identical count on
both sides (17 and 17). Strictly this detaches the Ballerina doc from the declaration; it does not
change the information available to a reader.

Also noted, shared and by design: `public` and `isolated` qualifiers are stripped from all type
definitions and client methods on both sides.

## 6. Coverage gaps vs. the library

**Zero gaps.** The package publishes exactly one module (`aws.s3`, confirmed by the bala's
`modules/` listing and by Central's `modules: ['aws.s3']`), and it is the default module, so the
shared `getDefaultModule()`-only extraction limitation costs nothing here.

Public symbols in the default module (`grep -nE '^public ' modules/aws.s3/*.bal` → 32):
31 types + 1 client class. All 31 types appear in both renders (17 Record + 3 Union + 5 Enum +
6 Error = 31), and `Client` appears with all 21 methods.

`StreamIterator` (`stream_iterator.bal:20`) and `RecordStreamIterator` (`:42`) are module-private
(`isolated class`, no `public`), so their absence is correct, not a gap. The 7 functions in
`utils.bal` are all module-private (`isolated function`, no `public`) — correctly absent.
No public module-level functions, services, listeners, or annotations exist, matching the JSONs'
empty `functions`/`services`/`annotations` arrays.

## 7. Compiler plugin

**No compiler plugin exists for this package.** Verified three ways:

- `find <clone> -iname '*compiler-plugin*' -maxdepth 3` → no results at tag `v4.0.0`.
- `grep -n 'compiler' ballerina/Ballerina.toml` → no match.
- No `compiler-plugin/compiler-plugin.json` in the bala.

The package's native side is a plain JVM interop layer (`aws.s3-native-4.0.0.jar` plus 40+ AWS SDK
v2 jars under `platform/java21/`), reached via `@java:Method` externals. Nothing plugin-implied is
therefore missing from the render.

## 8. Other considerations

- **Not deprecated.** Central reports `deprecated: null`, `deprecateMessage: ""`. Stable 1.0+
  version (`4.0.0`), `balaVersion` 3.0.0, pullCount 101 at time of check.
- **Doc quality is good.** Every public type, field, enum member, and client method carries a doc
  comment, and all of them survive into `new`. The README section (120 rendered lines) reproduces the
  bala README in full, including the Quickstart code blocks.
- **Size / token cost.** `new` is 27 lines (+4.2%) larger than `old`. The `@display` annotations are
  the bulk of the growth and inflate the already very long remote-method signature lines (the
  `putObjectFromFile` line is ~620 chars). This is pure metadata with little value to a code-
  generating LLM; it is the one place where `new` costs tokens without adding generative signal.
- **`init`'s region parameter** is rendered as a 55-member string-literal union spanning ~1.4 KB on a
  single line, on both sides. That single parameter is roughly 2% of the whole render. Unchanged
  between sides, so out of scope, but worth knowing.
- **`config` included-record parameters** (`*GetObjectConfig config` etc.) are rendered as a trailing
  positional `GetObjectConfig config` with no `*` and no default, on both sides — an LLM may not
  realise these are included-record (spread) parameters whose fields can be passed inline.

## 9. Evidence log

| # | Check | Result |
|---|---|---|
| 1 | `wc -l old/…bal.txt new/…bal.txt` | 650 / 677 |
| 2 | `grep -c '^// Unknown type:'` old / new | 6 / 0 |
| 3 | `grep -n '^// --- '` old / new | 4 markers each, same names |
| 4 | `diff -u old new` | 4 hunks, +54 / −27, read in full |
| 5 | `grep -cE '[a-z]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 2 / 0 |
| 6 | `grep -c '@display'` old / new | 0 / 38 lines (67 instances) |
| 7 | declaration-name set diff (`/tmp/decl_old.txt` vs `_new`) | 49 → 55, additions only |
| 8 | function-name set diff (`/tmp/fn_old.txt` vs `_new`) | 22 = 22; only `remote` dropped on `close` |
| 9 | JSON `typeDefs` name-set old vs new | equal, 54 each, no symmetric difference |
| 10 | JSON `typeDefs` content diff | 7 changed: 6 errors gain `baseType`, `ConnectionConfig` region normalised |
| 11 | JSON `clients[0].functions` name-set | equal, 21 each |
| 12 | JSON `readme` / `description` old vs new | byte-identical (4593 chars) |
| 13 | JSON typeDef kind census (new) | 23 Constant, 17 Record, 6 Error, 5 Enum, 3 Union |
| 14 | `ls -R <bala>` | one module dir: `modules/aws.s3`; no `compiler-plugin/` |
| 15 | `git ls-remote --tags` → exact tag | `v4.0.0` = `0a179fa32b074a300023d215d264f3eb9290d476` |
| 16 | `git clone --depth 1 --branch v4.0.0` | succeeded |
| 17 | `diff -q` upstream `ballerina/*.bal` vs bala `modules/aws.s3/*.bal` (6 files) | all identical |
| 18 | `find <clone> -iname '*compiler-plugin*'`; `grep compiler Ballerina.toml` | no results |
| 19 | `errors.bal:19,22,25,28,31,34` | `distinct error` / `distinct Error` ×5 — confirms §5.1 |
| 20 | `client.bal:417` | `public isolated function close() returns Error? {` — confirms §3 close fix |
| 21 | `client.bal:24` | `@display {label: "AWS S3 Client", iconPath: "icon.png"}` |
| 22 | `client.bal:186` | `typedesc<RetrievableType> targetType = <>` — confirms §5.2 |
| 23 | `grep -cE '^    @display \{label' client.bal` vs render fn-level | 19 vs 19 |
| 24 | source param-level `@display` (56 raw − 9 return-level) vs render | 47 vs 47 |
| 25 | `grep -oE 'returns @display' client.bal \| wc -l` vs render | 9 vs 0 — confirms §5.3 |
| 26 | `grep -nE '^public ' modules/aws.s3/*.bal` | 32 symbols (31 types + `Client`) — all rendered |
| 27 | `stream_iterator.bal:20,42` | `isolated class` (not public) — correctly absent |
| 28 | `utils.bal` function scan | 7 functions, none `public` — correctly absent |
| 29 | `types.bal:295–354` enum bodies vs render lines 129–200, 242–470 | all 23 members + values + docs match |
| 30 | awk detached-doc scan (blank line before `type`/`enum`) old / new | 17 / 17 — confirms §5.4 shared |
| 31 | Central API `packages/ballerinax/aws.s3/4.0.0` | not deprecated; `modules: ['aws.s3']` |
| 32 | render `readme` vs bala `docs/README.md` | equal after strip (4593 chars) |
| 33 | `OLD_AND_NEW_DIFFS/aws.s3_diff.md` claims (6 added, 0 removed, 6→0 unknown, 2→0 qualified) | all independently reproduced above |

## 10. Caveats and unverified items

- **Neither render is compiled.** Statements about validity (e.g. `= s3:RetrievableType` in §5.2)
  are read off the Ballerina grammar and the library source, not from a compiler run. The renders are
  LLM context artefacts, not compilation units, so this is expected.
- **Renderer/extractor source not inspected.** I did not read the `ballerina-vscode` `main` vs
  `L1_json_and_annotations_with_spec_v2` code. Attribution of each change to a specific code change
  (e.g. "the renderer no longer forces `remote`") is inferred from the JSON/render pairs — the JSON
  already said `"Normal Function"` on both sides, which localises the `close` fix to the renderer,
  and the error-type `baseType` field appears only in the new JSON, which localises that to the
  extractor. Consistent with the evidence, but not read from the source.
- **`aws:Region` correctness not traced into `ballerinax/aws`.** I confirmed the render matches
  `types.bal`'s written form; I did not open the `ballerinax/aws` bala to confirm `Region` is a
  55-member string union matching the expanded `init` parameter. The two are consistent in shape.
- **`@display` label text verified by count plus spot-check**, not by exhaustive one-to-one
  comparison of all 67 instances. Counts match exactly at every level (1/19/47), and the ~10 labels
  read in the diff and in `client.bal:24–409` all matched verbatim.

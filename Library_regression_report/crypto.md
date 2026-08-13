# ballerina/crypto 2.12.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/crypto` |
| Pinned version | `2.12.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-crypto |
| Tag reviewed | `v2.12.1` (clone HEAD `137e148`, `git describe --tags` = `v2.12.1`) |
| Bala inspected | `/Users/admin/.ballerina/repositories/central.ballerina.io/bala/ballerina/crypto/2.12.1/java21` |
| Old render | `1507` lines (72,725 bytes) |
| New render | `1508` lines (72,715 bytes) |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

The two renders differ in exactly 3 hunks (4 lines added, 3 removed). All three are spec-v2
improvements:

1. `// Unknown type: Error` (old line 126) is replaced by a real definition
   `type Error error;` carrying the doc comment `# Represents the error type of the module.`
2. and 3. Two function return types lose the invalid version qualifier:
   `stream<byte[], ballerina/crypto:2.12.1:Error?>|Error` → `stream<byte[], Error?>|Error`,
   which is exactly what the library source declares.

Nothing is removed, truncated, or degraded. Declaration coverage is 100% of the default module's
public API on both sides (79 functions, 14 types, 3 enums, 11 constants — all present). `crypto`
exports a single module (`crypto`), which is the default module, so there is no submodule gap.

Several rendering inaccuracies do exist (dropped `distinct`, open-vs-closed records, duplicated
enum members, mishandled included-record parameters), but with one exception all of them are
present identically in `old` — they are pipeline-wide behaviours, not regressions from spec v2.

## 2. Change inventory

Full diff between the two renders (`diff -u old new`) — 3 hunks total, verified by hand:

| # | Old lines | New lines | Kind | Change |
|---|---|---|---|---|
| 1 | 126 | 126–127 | type | `// Unknown type: Error` → `# Represents the error type of the module.` + `type Error error;` |
| 2 | 473 | 474 | function | `encryptStreamAsPgp` return type: `stream<byte[], ballerina/crypto:2.12.1:Error?>\|Error` → `stream<byte[], Error?>\|Error` |
| 3 | 502 | 503 | function | `decryptStreamFromPgp` return type: same qualifier removal |

Declaration counts by kind (grep on `^<kind> ` in each render):

| Kind | old | new | Δ |
|---|---|---|---|
| `function` | 79 | 79 | 0 |
| `type` | 13 | 14 | +1 (`Error`) |
| `const` | 32 | 32 | 0 |
| `enum` | 3 | 3 | 0 |
| `class` / `annotation` / `listener` / `service` | 0 | 0 | 0 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| version-qualified type refs (`org/mod:x.y.z:T`) | 2 | 0 | −2 |
| `// --- ` section markers | 4 | 4 | 0 |

Function name sets are byte-identical (`diff` of sorted names → no output).
README block (lines 1–48) is byte-identical between the two renders.

JSON level (structural comparison of both `ballerina_crypto.json`): top-level keys identical;
`clients`, `services`, `annotations` empty on both; `readme` and `description` identical;
`functions` 79 vs 79 and `typeDefs` 49 vs 49 with identical name sets. Only 3 entries differ:

- `typeDefs["Error"]`: `new` adds `"baseType": "error"` (old had only `name`/`description`/`type`).
- `functions["encryptStreamAsPgp"]`, `functions["decryptStreamFromPgp"]`: return-type string only.

## 3. Correctness against library source

Both renders were checked against the bala module source (authoritative) at
`.../2.12.1/java21/modules/crypto/*.bal`, cross-read against the `v2.12.1` clone.

- `Error` — bala `crypto_errors.bal:18`: `public type Error distinct error;`. `new` renders
  `type Error error;` with the correct doc line from `crypto_errors.bal:17`. Base type correct;
  `distinct` qualifier is dropped (see §5.1).
- `encryptStreamAsPgp` — bala `encrypt_decrypt.bal:273-274`:
  `public isolated function encryptStreamAsPgp(stream<byte[], error?> inputStream, string publicKey, *Options options) returns stream<byte[], Error?>|Error`.
  `new` return type `stream<byte[], Error?>|Error` matches the source exactly; `old`'s
  `ballerina/crypto:2.12.1:Error?` does not exist as Ballerina syntax.
- `decryptStreamFromPgp` — bala `encrypt_decrypt.bal:310-311`: return type `stream<byte[], Error?>|Error`.
  `new` matches exactly.
- 12 further signatures spot-checked line-by-line against the bala and found exact matches
  (parameter names, order, defaults, return types), on both sides:
  `encryptAesGcm` (encrypt_decrypt.bal:140), `decryptAesGcm` (:241), `crc32b` (hash.bal:110),
  `hashBcrypt` (:139), `hashArgon2` (:170), `hashPbkdf2` (:200),
  `encryptRsaKemMlKem768Hpke` (hpke.bal:102), `hkdfSha256` (kdf.bal:30),
  `encapsulateMlKem768` (kem.bal:39), `decodeRsaPrivateKeyFromKeyStore` (private_public_key.bal:100),
  `verifyMlDsa65Signature` (sign_verify.bal:240), `equalConstantTime` (utils.bal:27).
- Record shapes verified field-for-field against `private_public_key.bal:53-85` and
  `pgp_utils.bal:24-30`: `PrivateKey{algorithm}`, `PublicKey{algorithm, certificate?}`,
  `Certificate{version0, serial, issuer, subject, notBefore, notAfter, signature, signingAlgorithm}`,
  `Options{compressionAlgorithm, symmetricKeyAlgorithm, armor, withIntegrityCheck, markForYourEyesOnly}`.
  Field names and types all correct, including the awkward-but-real `int version0`.
- Foundational cross-package types: `Certificate.notBefore` / `.notAfter` render as
  `time:Utc` with the inline marker `// Special Agent Note: Utc FROM ballerina/time package`
  (2 occurrences in each render) — correct type name, correct provenance, unchanged between sides.
  `crypto:Error` — the type most other stdlib packages depend on — is only rendered correctly on
  the `new` side.
- `HmacAlgorithm` enum members (`hash.bal:20-24`: SHA1, SHA256, SHA512) all present in both.

## 4. Regressions

**None found.**

Basis for that conclusion:
- The complete `diff -u` between the two renders is 3 hunks (shown in §2) — there is no other
  textual difference anywhere in the 1507/1508 lines.
- Function name sets identical (79 = 79, empty diff). Type/enum/const name sets identical apart
  from the added `Error`.
- Structural JSON diff shows zero entries removed and zero entries whose content shrank; only the
  3 additive/corrective changes listed.
- README section identical (byte-for-byte for lines 1–48); section markers unchanged (4 = 4).
- No parameter, default value, doc line, or return type is dropped in `new`.

## 5. Issues in `new` (independent of `old`)

These are inaccuracies present in the `new` render vs. the library source. Item 1 is new-side only
(it did not exist in `old` because `old` emitted no definition at all); items 2–6 are identical in
`old` and are therefore pipeline-wide, not spec-v2 defects.

1. **`distinct` dropped from `Error`.** Source `crypto_errors.bal:18` is
   `public type Error distinct error;`; `new` renders `type Error error;`. The JSON carries only
   `"baseType": "error"`, so the distinctness is lost at extraction, not rendering. Impact is small
   (an LLM would still write `crypto:Error` correctly) but the render would not reproduce the
   library's actual type identity. `grep -c distinct` on the new render = 0.
2. **Enum members duplicated as top-level constants** (shared with `old`). All 21 members of
   `HmacAlgorithm`, `CompressionAlgorithmTags` and `SymmetricKeyAlgorithmTags` are emitted both as
   `const string SHA1 = "SHA1";` … `const string CAMELLIA_256 = "13";` and again inside the
   `enum` bodies. That is why the render shows 32 constants where the bala declares 11
   (`grep -c '^public const'` = 11). As written the file would not compile (redeclared symbols).
3. **Closed records rendered as open** (shared). Source uses `record {| ... |}` for
   `HybridEncryptionResult`, `EncapsulationResult`, `Options`, `KeyStore`, `TrustStore`,
   `PrivateKey`, `PublicKey`, `Certificate`; the render emits `record { ... }`. This tells a
   consumer that arbitrary extra fields are allowed, which is false.
4. **Record field defaults become optional markers** (shared). `Options` declares
   `CompressionAlgorithmTags compressionAlgorithm = ZIP;` and `SymmetricKeyAlgorithmTags
   symmetricKeyAlgorithm = AES_256;` plus three `boolean … = true;` fields (pgp_utils.bal:25-29).
   The render shows all five as `?`-optional with no defaults.
5. **Included-record parameter `*Options options` mishandled** (shared). Source
   `encryptPgp` (encrypt_decrypt.bal:257) and `encryptStreamAsPgp` (:273) take `*Options options`.
   Both renders expand the record fields into defaulted positional parameters *and* append a
   trailing required `Options options` parameter, e.g. new line 457:
   `function encryptPgp(byte[] plainText, string publicKey, CompressionAlgorithmTags compressionAlgorithm = "1", …, boolean markForYourEyesOnly = true, Options options) returns byte[]|Error;`
   A required parameter after defaultable ones is invalid Ballerina, and the parameter is
   duplicated. This is the most misleading construct in the file for an LLM consumer.
6. **Enum-typed defaults rendered as raw literals** (shared). `compressionAlgorithm = "1"` and
   `symmetricKeyAlgorithm = "9"` instead of the member names `ZIP` / `AES_256`.

## 6. Coverage gaps vs. the library

**None.** The bala default module declares (grep on `^public <kind>` across
`modules/crypto/*.bal`): 79 `public isolated function`, 14 `public type`, 3 `public enum`,
11 `public const` — 107 symbols. Set comparison against the `new` render:

- functions: 79 in bala, 79 in render, `comm` in both directions empty.
- types: 14 in bala, 14 in render, both `comm` directions empty.
- enums: 3 vs 3, identical.
- constants: all 11 bala constants present; the 21 "extra" names in the render are the enum
  members (see §5.2), not missing/invented API.

`package.json` `"export": ["crypto"]` and Central metadata list exactly one module (`crypto`),
which is the default module — so the known `getDefaultModule()` limitation costs nothing here.
The two non-public classes `DecryptedStreamIterator` / `EncryptedStreamIterator`
(`stream_iterators.bal:19,51`) are correctly absent from both renders.

## 7. Compiler plugin

`has_plugin: true` — confirmed: the bala contains
`compiler-plugin/compiler-plugin.json` (`plugin_id: crypto-compiler-plugin`,
`plugin_class: io.ballerina.stdlib.crypto.compiler.CryptoCompilerPlugin`) and
`compiler-plugin/libs/crypto-compiler-plugin-2.12.1.jar`.

Source (`compiler-plugin/src/main/java/io/ballerina/stdlib/crypto/compiler/CryptoCompilerPlugin.java`):
`init()` only registers a `CryptoCodeAnalyzer` when a `ScannerContext` is present in the plugin
user data. The plugin is therefore a **static-code-analysis-only** plugin — no code modifiers, no
code actions, no generated artifacts, no annotations.

`compiler-plugin/src/main/resources/rules.json` declares three `VULNERABILITY` rules:
1. Avoid using insecure cipher modes or padding schemes
2. Avoid using fast hashing algorithms
3. Avoid reusing counter mode initialization vectors

Implemented by `AvoidWeakCipherAlgorithmsRule`, `AvoidFastHashAlgorithmsRule`,
`AvoidReusingCounterModeVectorsRule` under `staticcodeanalyzer/functionrules/`.

Because the plugin contributes no annotations, types, or generated declarations, there is nothing
it implies that should appear in the render. Neither render is missing plugin-derived content.
Worth noting for consumers: the render advertises `hashMd5`, `hashSha1`, `encryptAesEcb`,
`RsaPadding PKCS1`, etc. with no indication that the shipped scanner flags several of these as
vulnerabilities — but that is a pipeline-wide design point, identical on both sides.

## 8. Other considerations

- Not deprecated: Central `deprecated: None`, `deprecateMessage: ""`. Stable 2.x version.
  `pullCount` 58,845, `visibility: public`, built with `ballerinaVersion 2201.12.0`.
- Size/token impact is negligible: `new` is 1 line longer and 10 bytes *smaller*
  (72,715 vs 72,725 bytes); the JSON is 21 bytes smaller (148,075 vs 148,096).
- Doc quality is good on both sides — every function carries its full doc comment including the
  ```ballerina``` example blocks from the source.
- Neither render is compilable Ballerina, for the reasons in §5.2 and §5.5. This is unchanged by
  spec v2; if anything `new` is strictly closer to compilable because it removes the two
  syntactically impossible `ballerina/crypto:2.12.1:Error` references and defines `Error`.
- No encoding problems observed; no mojibake, no truncated lines.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l` both renders | old 1507, new 1508 |
| `wc -c` both renders | old 72,725, new 72,715 |
| `diff -u old new` | 3 hunks, +4/−3 lines (reproduced in §2) |
| `grep -c '^// Unknown type:'` | old 1, new 0 |
| `grep -cE '[a-z]+/[a-z.]+:[0-9]+\.[0-9]+\.[0-9]+:'` | old 2, new 0 |
| `grep -n '^// --- '` | 4 markers each: README, END README, Types, Functions |
| `grep -cE '^function '` | old 79, new 79 |
| `grep -cE '^type '` | old 13, new 14 |
| `grep -cE '^const '` / `^enum ` / `^class ` / `^annotation ` / `^listener ` | 32/3/0/0/0 both sides |
| `diff` of sorted function-name lists | identical (empty output) |
| `comm -23 bala_functions new_functions` | empty (no missing functions) |
| `comm -13 bala_functions new_functions` | empty (no invented functions) |
| `comm` both directions, types (14 vs 14) | empty both ways |
| `diff` enums bala vs new (3 vs 3) | identical |
| `comm -23 bala_consts new_consts` | empty; `comm -13` yields the 21 enum members (§5.2) |
| `grep -hoE '^public [a-z]+ ' modules/crypto/*.bal \| uniq -c` | 79 isolated (functions), 14 type, 3 enum, 11 const |
| `diff` of render lines 1–48 (README) | identical |
| Python structural JSON diff | 79/79 functions, 49/49 typeDefs, same name sets; 3 entries differ (Error `baseType`, 2 return types) |
| `git describe --tags` in clone | `v2.12.1`; HEAD `137e148` "[Gradle Release Plugin] - pre tag commit: 'v2.12.1'" |
| `ls` bala root | `bala.json compiler-plugin dependency-graph.json docs modules package.json platform` |
| `ls modules/` | single dir `crypto` (default module) |
| `cat package.json` | version 2.12.1, `export: ["crypto"]`, platform java21 |
| `cat compiler-plugin/compiler-plugin.json` | plugin_id `crypto-compiler-plugin`, class `CryptoCompilerPlugin` |
| `cat compiler-plugin/src/main/resources/rules.json` (clone) | 3 VULNERABILITY rules |
| `curl api.central.ballerina.io/.../ballerina/crypto/2.12.1` | deprecated=None, 1 module, ballerinaVersion 2201.12.0 |
| bala `crypto_errors.bal:17-18` | `# Represents the error type of the module.` / `public type Error distinct error;` |
| bala `encrypt_decrypt.bal:273-274, 310-311` | `returns stream<byte[], Error?>\|Error` (matches new) |
| bala `pgp_utils.bal:24-30` | `Options` closed record with 5 defaulted fields |
| bala `private_public_key.bal:53-85` | PrivateKey / PublicKey / Certificate closed records |
| 12 function signatures spot-checked vs bala | all exact matches (§3) |
| `grep -c 'Special Agent Note'` | 2 in old, 2 in new |
| `grep -c distinct` new render | 0 |

## 10. Caveats and unverified items

- The compiler-plugin jar in the bala was not decompiled; plugin behaviour was read from the
  `v2.12.1` clone's Java sources, which correspond to the same tag. The bala's
  `compiler-plugin.json` confirms the same plugin class name, so the correspondence is sound but
  not byte-verified.
- The `distinct` loss in §5.1 is attributed to extraction (the JSON `baseType` is plain `"error"`)
  rather than rendering; I did not read the `ModelToJsonConverter` / `toSyntaxString` sources to
  confirm which stage discards it.
- Whether items §5.2–§5.6 are intended pipeline behaviour or latent bugs is out of scope for this
  per-library audit; they are recorded as observed facts, identical on both sides.
- The scratch clone directory already existed from a prior run; I verified its tag
  (`git describe --tags` = `v2.12.1`, HEAD `137e148`) rather than re-cloning.

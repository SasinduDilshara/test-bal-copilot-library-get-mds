# ballerina/soap 2.3.1 — Copilot render regression report

| | |
|---|---|
| Library | `ballerina/soap` |
| Pinned version | `2.3.1` |
| Upstream repo | https://github.com/ballerina-platform/module-ballerina-soap |
| Tag reviewed | `v2.3.1` (exact tag, commit `e7524eb`) |
| Bala inspected | `/Users/admin/.ballerina/ballerina-home/distributions/ballerina-2201.13.4/repo/bala/ballerina/soap/2.3.1/java21` |
| Old render | `709` lines |
| New render | `710` lines |
| Verdict | **IMPROVEMENT ONLY** |

## 1. Summary

`new` differs from `old` in exactly two places, both strict improvements:

1. `soap:Error` was a bare `// Unknown type: Error` placeholder in `old`; `new` emits a real
   definition `type Error error;` with its doc comment.
2. `OutboundSecurityConfig`'s union members were rendered with version-qualified, non-compiling
   refs (`ballerina/soap.wssec:2.3.1:NoPolicy|…`) in `old`; `new` uses module-prefixed
   `wssec:NoPolicy|…`.

Nothing was dropped, truncated, or made less accurate. All 18 public symbols of the default
`soap` module are present in both renders with signatures that match the bala source. The
remaining defects (mangled `crypto:wssec:Error` return type, missing `distinct` on `Error`,
dropped record defaults, missing import lines, no submodule client API) are identical on both
sides and are pre-existing, not introduced by spec v2.

## 2. Change inventory

Whole-file diff (`diff -u old new`): **2 hunks, 3 lines added, 2 lines removed**.

| Kind | old | new | Delta |
|---|---|---|---|
| Total lines | 709 | 710 | +1 |
| `// Unknown type:` placeholders | 1 | 0 | −1 |
| Version-qualified type refs (`org/mod:x.y.z:Type`) | 1 line (6 occurrences) | 0 | −1 |
| `// --- section ---` markers | 4 | 4 | 0 |
| JSON `typeDefs` | 28 | 28 | 0 |
| JSON `functions` | 9 | 9 | 0 |
| JSON `clients` / `services` / `annotations` | 0 / 0 / 0 | 0 / 0 / 0 | 0 |
| Rendered `const` declarations | 19 | 19 | 0 |
| Rendered `type` declarations | 3 | 4 | +1 (`Error`) |
| Rendered `enum` declarations | 5 | 5 | 0 |
| Rendered `function` declarations | 9 | 9 | 0 |

Declarations **added** in `new` (1): `type Error error;` (new:646).
Declarations **removed** in `new`: none.
Declarations **modified** in `new` (1): `type OutboundSecurityConfig` (old:633 → new:633), type
reference form only; the six union members are unchanged in identity and order.

JSON-level: `readme`, `functions`, `description`, `name`, and 26 of 28 `typeDefs` are
byte-identical. The two changed typeDefs are `OutboundSecurityConfig` (member names
`ballerina/soap.wssec:2.3.1:X` → `wssec:X`) and `Error` (gains `"baseType": "error"`).

## 3. Correctness against library source

Default module `soap` in the bala exports 18 public symbols. All 18 appear in both renders.

Functions (bala `modules/soap/soap_utils.bal`), all `public isolated function` except the three
assert helpers which are `public function`:

| Source | Rendered (new) | Match |
|---|---|---|
| `validateTransportBindingPolicy(ClientConfig) returns Error?` (soap_utils.bal:26) | new:694 `returns Error\|()` | yes (`T?` ≡ `T\|()`) |
| `getReadOnlyClientConfig(ClientConfig) returns readonly & ClientConfig` (:41) | new:696 `returns ClientConfig & readonly` | yes (intersection is commutative) |
| `applySecurityPolicies(wssec:OutboundSecurityConfig\|wssec:OutboundSecurityConfig[], xml, boolean soap12 = true) returns xml\|crypto:Error\|wssec:Error` (:45–47) | new:698 | params yes (union expanded inline); **return type wrong**, see §5 |
| `applyInboundConfig(wssec:InboundConfig, xml, boolean soap12 = true) returns xml\|Error` (:67) | new:700 | yes |
| `sendReceive(xml\|mime:Entity[], http:Client, string? soapAction = (), map<string\|string[]> headers = {}, string path = "", boolean soap12 = true) returns xml\|mime:Entity[]\|Error` (:91) | new:702 | yes |
| `sendOnly(…same params…) returns Error?` (:104) | new:704 | yes |
| `assertUsernameToken(string, string, string, wssec:PasswordType, string) returns error?` (:174) | new:706 | yes |
| `assertSymmetricBinding(string, string) returns error?` (:186) | new:708 | yes |
| `assertSignatureWithoutX509(string)` (:192) | new:710 `returns ()` | yes |

Types:

- `ClientConfig` (bala `modules/soap/configs.bal:24`) — 3 fields, docs and types match (new:623–631).
  Closedness and defaults are lost; see §5.
- `OutboundSecurityConfig` = `wssec:OutboundSecurityConfig` (`types.bal:70`), whose definition is
  `NoPolicy|UsernameTokenConfig|TimestampTokenConfig|SymmetricBindingConfig|TransportBindingConfig|AsymmetricBindingConfig`
  (`modules/soap.wssec/records.bal:20`). `new:633` reproduces exactly these six members. Correct.
- `InboundSecurityConfig` = `wssec:InboundConfig` (`types.bal:67`; target at
  `modules/soap.wssec/records.bal:119`) — rendered inline as a record with `crypto:KeyStore
  decryptKeystore?` and `crypto:KeyStore signatureKeystore?` (new:638–643). Matches.
- `Error` (`modules/soap/error.bal:18`, `public type Error distinct error;`) — new:646 renders
  `type Error error;`. Base type correct, `distinct` lost (§5).
- The five enums `PasswordType`, `SignatureAlgorithm`, `EncryptionAlgorithm`,
  `CanonicalizationAlgorithm`, `DigestAlgorithm` (`modules/soap/types.bal:21,30,39,47,56`) — all
  members present in both renders, and their string values are additionally emitted as the 19
  top-level `const string` declarations at new:582–618. Members are emitted in reverse source
  order (e.g. `DERIVED_KEY_DIGEST, DERIVED_KEY_TEXT, DIGEST, TEXT` vs source
  `TEXT, DIGEST, DERIVED_KEY_TEXT, DERIVED_KEY_DIGEST`) — identical on both sides, harmless for
  enums.

Module-private consts in the source (`SOAP_ACTION`, `ACTION`, `NO_POLICY`, `SOAP_RESPONSE_ERROR`,
`INVALID_PROTOCOL_ERROR`) are correctly absent from both renders.

Upstream clone at tag `v2.3.1` agrees with the bala for every file checked (e.g. clone
`ballerina/error.bal:18` is also `public type Error distinct error;`). No GitHub/bala divergence
found.

## 4. Regressions

**None found.**

Basis for that conclusion:
- Full unified diff is 2 hunks / 3 added / 2 removed lines; both hunks were read in full and both
  replace a degraded form with a better one.
- Extracted declaration sets (`grep -nE '^(public )?(function|type|class|enum|const|…)'`) are
  identical between `old` and `new` apart from the single added `type Error error;`.
- JSON comparison: `functions`, `readme`, `description`, `name`, `clients`, `services`,
  `annotations` are equal; only 2 of 28 `typeDefs` differ, and neither loses information.
- No parameter, default value, return type, doc string, section marker, or README byte is lost
  (`readme` field is `==` between the two JSONs; both renders have the same 4 section markers and
  the same 570-line README block).

## 5. Issues in `new` (independent of `old`)

Five, all also present in `old` (i.e. pre-existing, not spec-v2 regressions) except #1 which is
new only because `old` rendered nothing at all for `Error`:

1. **`Error` loses `distinct`.** Source: `public type Error distinct error;`
   (bala `modules/soap/error.bal:18`). Render (new:646): `type Error error;`. An LLM told
   `soap:Error` is a plain `error` may generate `error e = ...` handling that ignores the distinct
   type identity, or omit `soap:` prefixed error construction. Still a large net improvement over
   `old`'s `// Unknown type: Error`.
2. **`applySecurityPolicies` return type is mangled.** Source returns
   `xml|crypto:Error|wssec:Error` (soap_utils.bal:47). Both renders emit
   `xml|crypto:wssec:Error|crypto:wssec:Error` (old:697, new:698) — a doubled module prefix and a
   duplicated member. Non-compiling and misleading. Identical in `old`.
3. **`ClientConfig` closedness and defaults dropped.** Source is
   `record {| http:ClientConfiguration httpConfig = {}; OutboundSecurityConfig|OutboundSecurityConfig[] outboundSecurity = NO_POLICY; InboundSecurityConfig inboundSecurity = {}; |}`
   (configs.bal:24–28). Render (new:623–631) is an open `record { … }` with all three fields marked
   optional (`?`) and no default values shown. Identical in `old`.
4. **`wssec:` prefix is not usable by a consumer.** `soap.wssec` is a non-exported module
   (`package.json` `"modules"` entry `{"name":"soap.wssec","export":false}`; the package-level
   `export` array is `["soap","soap.soap11","soap.soap12"]`). Code following the render's
   `wssec:NoPolicy` etc. cannot compile. `new`'s form is at least valid Ballerina syntax, whereas
   `old`'s `ballerina/soap.wssec:2.3.1:NoPolicy` was not — so this is an improvement, but not a fix.
5. **Render is not self-contained.** The only import emitted is `import ballerina/soap;` (new:5),
   yet the body uses `http:`, `crypto:`, `mime:` and `wssec:` prefixes. Mitigated by the
   `// Special Agent Note: X FROM ballerina/y package` trailing comments, which are present and
   correct on every such line in both renders.

No invented symbols, no encoding damage, no broken doc text found.

## 6. Coverage gaps vs. the library

**Default module (`soap`): 0 gaps.** All 9 public functions and all 9 public types listed in §3
appear in both renders. Verified by `grep -n "public "` over
`bala/…/modules/soap/*.bal` (18 hits) against the rendered declaration list.

**Submodule-only API missing from BOTH renders — shared gap, not a spec-v2 regression** (4 public
symbols across the 2 *exported* modules `soap.soap11` and `soap.soap12`):

| Symbol | Source |
|---|---|
| `soap11:Client` (`public isolated client class`) + `init(string url, *soap:ClientConfig)`, `remote sendReceive(xml\|mime:Entity[], string action, map<string\|string[]> headers = {}, …)`, `remote sendOnly(xml\|mime:Entity[], string action, …)` | `modules/soap.soap11/soap11.bal:25,35,60,116` |
| `soap11:Error` | `modules/soap.soap11/error.bal:18` |
| `soap12:Client` + `init`, `remote sendReceive(xml\|mime:Entity[], string? action = (), …)`, `remote sendOnly` | `modules/soap.soap12/soap12.bal:25,35,60,116` |
| `soap12:Error` | `modules/soap.soap12/error.bal:18` |

This matters more here than for most libraries: the *entire client surface* of `ballerina/soap`
lives in these two submodules, so the API sections of both renders contain zero clients
(`clients: []` in both JSONs). The only saving grace is that the README block does cover them —
the rendered `readme` is 570 lines and concatenates the package README (222 lines) with
`## Module: soap.soap11` (171 lines) and `## Module: soap.soap12` (168 lines), including
`soap11:Client soapClient = check new (…)` and `soapClient->sendReceive(…)` examples. So an LLM
can still write working `soap` code from the README, just not from the typed API section.

`soap.wssec` is not exported, so its absence from the API section is correct — though the rendered
types reference it (§5.4).

## 7. Compiler plugin

**None.** `has_plugin` is `false` in the manifest and this is confirmed by inspection:
`find <bala>/2.3.1 -iname "*compiler-plugin*"` returns nothing, there is no
`compiler-plugin/compiler-plugin.json` in the bala, and
`find <clone> -maxdepth 2 -iname "*compiler-plugin*"` on the `v2.3.1` checkout returns nothing.
The `native/` directory in the repo holds only the WSS4J-backed runtime interop JAR
(`soap-native-2.3.1.jar`, listed under `platformDependencies` in `package.json`), not a plugin.
Nothing plugin-implied is therefore expected in the render.

## 8. Other considerations

- **Version/deprecation.** Central reports `ballerina/soap` 2.3.1 as not deprecated
  (`deprecated: null`), built with `ballerinaVersion 2201.12.11`, 3017 pulls, and lists exactly
  three modules (`soap`, `soap.soap11`, `soap.soap12`) — consistent with the bala. Post-1.0,
  stable. No version drift: both renders were produced from the same 2.3.1 bala.
- **Test helpers in the public API.** `assertUsernameToken`, `assertSymmetricBinding`,
  `assertSignatureWithoutX509` are genuinely `public` in the library (soap_utils.bal:174,186,192)
  and import `ballerina/test`, so rendering them is faithful — but they are test scaffolding
  exposed publicly by the library itself, and they occupy 3 of the 9 rendered functions. This is a
  library-side wart, not a render defect.
- **Size/tokens.** 710 lines / ~48.7 KB JSON; 570 of the 710 render lines (80%) are README. The
  spec-v2 change reduces JSON size marginally (48809 → 48710 bytes) because the long
  version-qualified refs are shortened. No token concern.
- **Qualifiers.** `public` and `isolated` are dropped from every declaration on both sides; the
  render's convention is evidently to omit them. Consistent, so not misleading in isolation.

## 9. Evidence log

| Check | Result |
|---|---|
| `wc -l old/ballerina_soap.bal.txt new/ballerina_soap.bal.txt` | 709 / 710 |
| `diff -u old new \| grep -c '^+[^+]'` / `'^-[^-]'` | 3 added / 2 removed |
| `grep -c '^// Unknown type:'` old / new | 1 / 0 |
| `grep -cE '[a-z]+/[a-z0-9._]+:[0-9]+\.[0-9]+\.[0-9]+:'` old / new | 1 line (6 refs) / 0 |
| `grep -c '^// --- '` old / new | 4 / 4 (README, END README, Types, Functions) |
| `grep -nE '^(public )?(function\|type\|class\|enum\|const\|annotation\|listener\|service\|isolated function)'` on both | identical sets except new:646 `type Error error;`; line numbers shift by +1 after 646 |
| Python JSON compare of `old/ballerina_soap.json` vs `new/ballerina_soap.json` | 8 identical top-level keys; `functions` equal (9 each), `readme` equal, `typeDefs` 28 each with exactly 2 differing (`OutboundSecurityConfig`, `Error`); `clients`/`services`/`annotations` empty in both |
| `wc -c` both JSONs | 48809 old / 48710 new |
| `git clone --depth 1 --branch v2.3.1 …` then `git describe --tags` | `v2.3.1`, commit `e7524eb` ("[Gradle Release Plugin] - pre tag commit: 'v2.3.1'") |
| `ls <bala>/java21/modules` | `soap`, `soap.soap11`, `soap.soap12`, `soap.wssec` |
| `cat <bala>/java21/package.json` | `export: [soap, soap.soap11, soap.soap12]`; `soap.wssec` `export:false`; `ballerina_version 2201.12.11`; 4 platform JARs |
| `grep -n "public " <bala>/java21/modules/soap/*.bal` | 18 public symbols (9 functions, 9 types) — all present in both renders |
| `cat <bala>/java21/modules/soap/{configs,constants,error,types}.bal` | verified `ClientConfig` closed record + 3 defaults; `Error distinct error`; 5 enums with values; 2 type aliases to `wssec` |
| `sed -n '20,115p' <bala>/java21/modules/soap/soap_utils.bal` | verified all 6 non-assert function signatures incl. `applySecurityPolicies … returns xml\|crypto:Error\|wssec:Error` |
| `grep -n "public type\|public enum" <bala>/java21/modules/soap.wssec/*.bal` | `OutboundSecurityConfig` union = the exact 6 members rendered (records.bal:20); `InboundConfig` record (records.bal:119) |
| `grep -n "remote isolated function" <bala>/…/soap11.bal soap12.bal` | 4 remote methods (sendReceive/sendOnly × 2) — in neither render |
| `find <bala>/2.3.1 -iname "*compiler-plugin*"` and same over clone | no matches → no compiler plugin |
| `wc -l <bala>/java21/docs/README.md` and `docs/modules/*/README.md` | 222 + 171 + 168 = 561; rendered `readme` is 570 lines / 24088 chars → package + both module READMEs concatenated |
| `curl api.central.ballerina.io/2.0/registry/packages/ballerina/soap/2.3.1` | not deprecated; 3 modules; 3017 pulls |
| `OLD_AND_NEW_DIFFS/soap_diff.md` claims (709/710, +3/−2, 2 hunks, 1→0 unknown, 6→0 version refs, 1 type added) | all independently reproduced above; no corrections needed |

## 10. Caveats and unverified items

- The render's fidelity claims are made against the **bala** (authoritative, what the extractor
  consumed) and cross-checked against the `v2.3.1` clone; the two agreed on every file I compared,
  but I did not byte-diff the whole clone against the whole bala.
- I did not compile either render. Statements that a construct "does not compile"
  (`ballerina/soap.wssec:2.3.1:NoPolicy`, `crypto:wssec:Error`, `wssec:` refs to a non-exported
  module, missing imports) are based on reading the Ballerina grammar and `package.json` export
  flags, not on running `bal build`.
- The rendered README block was verified to be the concatenation of the three bala READMEs by line
  count (561 source lines vs 570 rendered, difference accounted for by the two
  `## Module: soap.soapXX` separator headings and surrounding blank lines) and by heading sequence,
  not by a full byte-level diff of every README line. It is byte-identical between `old` and `new`,
  so it cannot be a regression either way.
- Whether the extractor *should* have picked up `soap.soap11` / `soap.soap12` is out of scope: per
  the brief, both sides extract only `pkg.getDefaultModule()`, and I confirmed both JSONs have
  `clients: []`. I did not inspect the extractor source to confirm the mechanism.

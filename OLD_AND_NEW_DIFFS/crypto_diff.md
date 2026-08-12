# crypto — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `crypto` |
| **Old file** | `crypto/old/ballerina_crypto.bal.txt` |
| **New file** | `crypto/new/ballerina_crypto.bal.txt` |
| **Old lines** | 1507 |
| **New lines** | 1508 |
| **Lines added** | 4 |
| **Lines removed** | 3 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 2 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 123–129 | 123–130 | Types | +2 | −1 |
| 2 | 470–476 | 471–477 | Functions | +1 | −1 |
| 3 | 499–505 | 500–506 | Functions | +1 | −1 |

---

## Unified diff

`````diff
--- crypto/old/ballerina_crypto.bal.txt	2026-08-12 23:21:51
+++ crypto/new/ballerina_crypto.bal.txt	2026-08-12 23:23:51
@@ -123,7 +123,8 @@
 # Represents the `ML-DSA-65` algorithm.
 const string MLDSA65 = "ML-DSA-65";
 
-// Unknown type: Error
+# Represents the error type of the module.
+type Error error;
 
 # The padding algorithms supported by AES encryption and decryption.
 type AesPadding "NONE"|"PKCS5";
@@ -470,7 +471,7 @@
 # + markForYourEyesOnly - Indicates whether the message is marked as "For Your Eyes Only". When `true`, the literal data packet filename is set to `_CONSOLE`, which signals PGP-compliant applications to treat the content as sensitive and avoid writing it to disk. Set to `false` to omit this marking
 # + options - Optional PGP encryption options, such as compression or cipher preferences
 # + return - The encrypted content as a stream of byte arrays, or a `crypto:Error` if the public key is invalid or an error occurs during encryption
-function encryptStreamAsPgp(stream<byte[], error?> inputStream, string publicKey, CompressionAlgorithmTags compressionAlgorithm = "1", SymmetricKeyAlgorithmTags symmetricKeyAlgorithm = "9", boolean armor = true, boolean withIntegrityCheck = true, boolean markForYourEyesOnly = true, Options options) returns stream<byte[], ballerina/crypto:2.12.1:Error?>|Error;
+function encryptStreamAsPgp(stream<byte[], error?> inputStream, string publicKey, CompressionAlgorithmTags compressionAlgorithm = "1", SymmetricKeyAlgorithmTags symmetricKeyAlgorithm = "9", boolean armor = true, boolean withIntegrityCheck = true, boolean markForYourEyesOnly = true, Options options) returns stream<byte[], Error?>|Error;
 
 # Returns the PGP-decrypted value of the given PGP-encrypted data. If the data is signed, the signature is silently
 # skipped without verification; only decryption is performed.
@@ -499,7 +500,7 @@
 # + privateKey - Path to the private key file in ASCII-armored format
 # + passphrase - The passphrase used to unlock the private key
 # + return - The decrypted content as a stream of byte arrays, or a `crypto:Error` if the key or passphrase is invalid
-function decryptStreamFromPgp(stream<byte[], error?> inputStream, string privateKey, byte[] passphrase) returns stream<byte[], ballerina/crypto:2.12.1:Error?>|Error;
+function decryptStreamFromPgp(stream<byte[], error?> inputStream, string privateKey, byte[] passphrase) returns stream<byte[], Error?>|Error;
 
 # Returns the MD5 hash of the given data.
 # ```ballerina
`````

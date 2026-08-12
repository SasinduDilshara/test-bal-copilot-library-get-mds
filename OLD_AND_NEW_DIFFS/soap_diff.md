# soap — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `soap` |
| **Old file** | `soap/old/ballerina_soap.bal.txt` |
| **New file** | `soap/new/ballerina_soap.bal.txt` |
| **Old lines** | 709 |
| **New lines** | 710 |
| **Lines added** | 3 |
| **Lines removed** | 2 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 6 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 630–636 | 630–636 | Types | +1 | −1 |
| 2 | 642–648 | 642–649 | Types | +2 | −1 |

---

## Unified diff

`````diff
--- soap/old/ballerina_soap.bal.txt	2026-08-12 23:21:51
+++ soap/new/ballerina_soap.bal.txt	2026-08-12 23:23:51
@@ -630,7 +630,7 @@
 };
 
 # Union type of all the outbound web service security configurations.
-type OutboundSecurityConfig ballerina/soap.wssec:2.3.1:NoPolicy|ballerina/soap.wssec:2.3.1:UsernameTokenConfig|ballerina/soap.wssec:2.3.1:TimestampTokenConfig|ballerina/soap.wssec:2.3.1:SymmetricBindingConfig|ballerina/soap.wssec:2.3.1:TransportBindingConfig|ballerina/soap.wssec:2.3.1:AsymmetricBindingConfig;
+type OutboundSecurityConfig wssec:NoPolicy|wssec:UsernameTokenConfig|wssec:TimestampTokenConfig|wssec:SymmetricBindingConfig|wssec:TransportBindingConfig|wssec:AsymmetricBindingConfig;
 
 # Represents the record for outbound security configurations to verify and decrypt SOAP envelopes.
 # 
@@ -642,7 +642,8 @@
     crypto:KeyStore signatureKeystore?; // Special Agent Note: KeyStore FROM ballerina/crypto package
 };
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
 # Represents enums for all the supported password types.
 # 
`````

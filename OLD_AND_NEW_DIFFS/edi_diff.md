# edi — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `edi` |
| **Old file** | `edi/old/ballerina_edi.bal.txt` |
| **New file** | `edi/new/ballerina_edi.bal.txt` |
| **Old lines** | 597 |
| **New lines** | 604 |
| **Lines added** | 14 |
| **Lines removed** | 7 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (4)

- `type Error`
- `type InvalidEnvelopeError`
- `type SchemaCompatibilityError`
- `type SerializationError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 214–220 | 214–220 | Types | +1 | −1 |
| 2 | 309–323 | 309–330 | Types | +13 | −6 |

---

## Unified diff

`````diff
--- edi/old/ballerina_edi.bal.txt	2026-08-12 23:21:51
+++ edi/new/ballerina_edi.bal.txt	2026-08-12 23:23:51
@@ -214,7 +214,7 @@
     # Array of segment and segment group schemas
     EdiUnitSchema[] segments?;
     # Map of segment definitions indexed by the segment code
-    map<ballerina/edi:1.6.0:EdiSegSchema> segmentDefinitions?;
+    map<EdiSegSchema> segmentDefinitions?;
 };
 
 # Structured envelope schema with separate levels for interchange, group (optional),
@@ -309,15 +309,22 @@
     int maxOccurances?;
 };
 
-type EdiUnitSchema ballerina/edi:1.6.0:EdiSegSchema|ballerina/edi:1.6.0:EdiSegGroupSchema|ballerina/edi:1.6.0:EdiUnitRef;
-
-// Unknown type: Error
+type EdiUnitSchema EdiSegSchema|EdiSegGroupSchema|EdiUnitRef;
 
-// Unknown type: InvalidEnvelopeError
+# Represents EDI module related errors
+type Error error;
 
-// Unknown type: SchemaCompatibilityError
+# Represents an input EDI text that does not conform to the expected envelope structure
+# (e.g. a missing or malformed envelope segment, or multiple interchanges in one call).
+type InvalidEnvelopeError error;
 
-// Unknown type: SerializationError
+# Represents a schema that cannot support the requested operation
+# (e.g. no `envelope` declaration, or a fixed-length "FL" schema used with envelope-aware APIs).
+type SchemaCompatibilityError error;
+
+# Represents a refusal to serialize an `EdiInterchange`
+# (e.g. a transaction `body` holds an `error` from a fail-safe parse).
+type SerializationError error;
 
 # Interchange Control Header (X12 ISA segment).
 # 
`````

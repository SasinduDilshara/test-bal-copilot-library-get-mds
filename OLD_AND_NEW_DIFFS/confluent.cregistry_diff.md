# confluent.cregistry — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `confluent.cregistry` |
| **Old file** | `confluent.cregistry/old/ballerinax_confluent.cregistry.bal.txt` |
| **New file** | `confluent.cregistry/new/ballerinax_confluent.cregistry.bal.txt` |
| **Old lines** | 120 |
| **New lines** | 121 |
| **Lines added** | 2 |
| **Lines removed** | 1 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (1)

- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 88–94 | 88–95 | Types | +2 | −1 |

---

## Unified diff

`````diff
--- confluent.cregistry/old/ballerinax_confluent.cregistry.bal.txt	2026-08-12 12:57:30
+++ confluent.cregistry/new/ballerinax_confluent.cregistry.bal.txt	2026-08-12 13:19:19
@@ -88,7 +88,8 @@
     int errorCode?;
 };
 
-// Unknown type: Error
+# Represents any error related to Ballerina Confluent Schema Registry module.
+type Error error<ErrorDetails>;
 
 # Provides a set of configurations to control the behaviours when communicating with a schema registry.
 # 
`````

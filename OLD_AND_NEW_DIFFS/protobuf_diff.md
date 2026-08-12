# protobuf — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `protobuf` |
| **Old file** | `protobuf/old/ballerina_protobuf.bal.txt` |
| **New file** | `protobuf/new/ballerina_protobuf.bal.txt` |
| **Old lines** | 80 |
| **New lines** | 86 |
| **Lines added** | 7 |
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
| `// --- section ---` markers | 3 | 4 |

### Declarations added (2)

- `annotation Descriptor`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 77–80 | 77–86 | Types | +7 | −1 |

---

## Unified diff

`````diff
--- protobuf/old/ballerina_protobuf.bal.txt	2026-08-12 23:21:51
+++ protobuf/new/ballerina_protobuf.bal.txt	2026-08-12 23:23:51
@@ -77,4 +77,10 @@
     string value;
 };
 
-// Unknown type: Error
+# Represents protobuf module error.
+type Error error;
+
+// --- Annotations ---
+
+# Annotation definition of the Descriptor
+public annotation MessageDescriptor Descriptor on type;
`````

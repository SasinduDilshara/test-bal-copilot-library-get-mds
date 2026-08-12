# persist — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `persist` |
| **Old file** | `persist/old/ballerina_persist.bal.txt` |
| **New file** | `persist/new/ballerina_persist.bal.txt` |
| **Old lines** | 207 |
| **New lines** | 211 |
| **Lines added** | 8 |
| **Lines removed** | 4 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (4)

- `type AlreadyExistsError`
- `type ConstraintViolationError`
- `type Error`
- `type NotFoundError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 176–188 | 176–192 | Types | +8 | −4 |

---

## Unified diff

`````diff
--- persist/old/ballerina_persist.bal.txt	2026-08-12 23:21:51
+++ persist/new/ballerina_persist.bal.txt	2026-08-12 23:23:51
@@ -176,13 +176,17 @@
 class AbstractPersistClient {
 }
 
-// Unknown type: Error
+# Defines the generic error type for the `persist` module.
+type Error error;
 
-// Unknown type: ConstraintViolationError
+# Represents an error that occurs when an attempt is made to perform an operation, which violates a foreign key constraint.
+type ConstraintViolationError error;
 
-// Unknown type: NotFoundError
+# Represents an error that occurs when an attempt is made to retrieve a record using a non-existing key.
+type NotFoundError error;
 
-// Unknown type: AlreadyExistsError
+# Represents an error that occurs when the user attempts to create a record which already exists in the database.
+type AlreadyExistsError error;
 
 // --- Functions ---
 
`````

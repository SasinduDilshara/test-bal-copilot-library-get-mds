# yaml — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `yaml` |
| **Old file** | `yaml/old/ballerina_yaml.bal.txt` |
| **New file** | `yaml/new/ballerina_yaml.bal.txt` |
| **Old lines** | 195 |
| **New lines** | 203 |
| **Lines added** | 24 |
| **Lines removed** | 16 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 8 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 31 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (8)

- `type AliasingError`
- `type ComposeError`
- `type ConstructionError`
- `type ConversionError`
- `type EmittingError`
- `type GrammarError`
- `type IndentationError`
- `type ScanningError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 30–67 | 30–75 | Types | +22 | −14 |
| 2 | 106–114 | 114–122 | Types | +2 | −2 |

---

## Unified diff

`````diff
--- yaml/old/ballerina_yaml.bal.txt	2026-08-12 23:21:51
+++ yaml/new/ballerina_yaml.bal.txt	2026-08-12 23:23:51
@@ -30,38 +30,46 @@
 const string CORE_SCHEMA = "CORE_SCHEMA";
 
 # Represents an error caused during the composing.
-type ComposingError ballerina/yaml.composer:0.8.0:ComposeError|ballerina/yaml.parser:0.8.0:GrammarError|ballerina/yaml.lexer:0.8.0:ScanningError|ballerina/yaml.common:0.8.0:IndentationError|ballerina/yaml.common:0.8.0:ConversionError|ballerina/yaml.common:0.8.0:AliasingError|ballerina/yaml.schema:0.8.0:ConstructionError;
+type ComposingError composer:ComposeError|parser:GrammarError|lexer:ScanningError|common:IndentationError|common:ConversionError|common:AliasingError|schema:ConstructionError;
 
-// Unknown type: EmittingError
+# Represents an error caused during the emitting.
+type EmittingError emitter:EmittingError;
 
 # Represents an error caused when failed to access the file.
-type FileError ballerina/io:1.8.1:Error|ballerina/file:1.13.0:Error;
+type FileError io:Error|file:Error;
 
 # Represents the generic error type for the YAML package.
-type Error ballerina/yaml.composer:0.8.0:ComposeError|ballerina/yaml.parser:0.8.0:GrammarError|ballerina/yaml.lexer:0.8.0:ScanningError|ballerina/yaml.common:0.8.0:IndentationError|ballerina/yaml.common:0.8.0:ConversionError|ballerina/yaml.common:0.8.0:AliasingError|ballerina/yaml.schema:0.8.0:ConstructionError|ballerina/yaml:0.8.0:EmittingError|ballerina/io:1.8.1:Error|ballerina/file:1.13.0:Error;
+type Error composer:ComposeError|parser:GrammarError|lexer:ScanningError|common:IndentationError|common:ConversionError|common:AliasingError|schema:ConstructionError|EmittingError|io:Error|file:Error;
 
 # Represents an error caused regarding YAML schema.
-type SchemaError ballerina/yaml.schema:0.8.0:ConstructionError|ballerina/yaml.common:0.8.0:ConversionError;
+type SchemaError schema:ConstructionError|common:ConversionError;
 
 # Represents an error caused during the parsing.
-type ParsingError ballerina/yaml.parser:0.8.0:GrammarError|ballerina/yaml.lexer:0.8.0:ScanningError|ballerina/yaml.common:0.8.0:IndentationError|ballerina/yaml.common:0.8.0:ConversionError|ballerina/yaml.common:0.8.0:AliasingError;
+type ParsingError parser:GrammarError|lexer:ScanningError|common:IndentationError|common:ConversionError|common:AliasingError;
 
 # Represents an error caused during the lexical analyzing.
-type LexicalError ballerina/yaml.lexer:0.8.0:ScanningError|ballerina/yaml.common:0.8.0:IndentationError|ballerina/yaml.common:0.8.0:ConversionError;
+type LexicalError lexer:ScanningError|common:IndentationError|common:ConversionError;
 
-// Unknown type: AliasingError
+# Represents an error caused when failed to alias an anchor.
+type AliasingError common:AliasingError;
 
-// Unknown type: IndentationError
+# Represents an error caused when the indentation is not correct.
+type IndentationError common:IndentationError;
 
-// Unknown type: ConversionError
+# Represents an error caused by the Ballerina lang when converting a data type.
+type ConversionError common:ConversionError;
 
-// Unknown type: ComposeError
+# Represents an error caused for an invalid compose.
+type ComposeError composer:ComposeError;
 
-// Unknown type: GrammarError
+# Represents an error caused for an invalid grammar production.
+type GrammarError parser:GrammarError;
 
-// Unknown type: ScanningError
+# Represents an error that is generated when an invalid character for a lexeme is detected.
+type ScanningError lexer:ScanningError;
 
-// Unknown type: ConstructionError
+# Represents an error caused when constructing a Ballerina data type.
+type ConstructionError schema:ConstructionError;
 
 # Configurations for writing a YAML document.
 # 
@@ -106,9 +114,9 @@
     # Fail safe schema type
     FailSafeSchema kind;
     # Function to generate the Ballerina data structure.  
-    function (json data) returns json|ballerina/yaml:0.8.0:SchemaError construct;
+    function (json data) returns json|SchemaError construct;
     # Function to convert the Ballerina data structure to YAML.
-    function (json data) returns string|ballerina/yaml:0.8.0:SchemaError represent;
+    function (json data) returns string|SchemaError represent;
 };
 
 # Represents the basic YAML types available in the Fail safe schema.
`````

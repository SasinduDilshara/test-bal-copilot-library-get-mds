# toml — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `toml` |
| **Old file** | `toml/old/ballerina_toml.bal.txt` |
| **New file** | `toml/new/ballerina_toml.bal.txt` |
| **Old lines** | 90 |
| **New lines** | 94 |
| **Lines added** | 11 |
| **Lines removed** | 7 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 11 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (4)

- `type ConversionError`
- `type GrammarError`
- `type LexicalError`
- `type WritingError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 18–38 | 18–42 | Types | +11 | −7 |

---

## Unified diff

`````diff
--- toml/old/ballerina_toml.bal.txt	2026-08-12 23:21:51
+++ toml/new/ballerina_toml.bal.txt	2026-08-12 23:23:51
@@ -18,21 +18,25 @@
 // --- Types ---
 
 # Represents an error caused during the parsing.
-type ParsingError ballerina/toml.parser:0.8.0:GrammarError|ballerina/toml.parser:0.8.0:ConversionError|ballerina/toml.lexer:0.8.0:LexicalError;
+type ParsingError parser:GrammarError|parser:ConversionError|lexer:LexicalError;
 
-// Unknown type: WritingError
+# Represents an error caused when writing a TOML file.
+type WritingError writer:WritingError;
 
 # Represents an error caused when failed to access the file.
-type FileError ballerina/io:1.8.1:Error|ballerina/file:1.13.0:Error;
+type FileError io:Error|file:Error;
 
 # Represents the generic error type for the TOML package.
-type Error ballerina/toml.parser:0.8.0:GrammarError|ballerina/toml.parser:0.8.0:ConversionError|ballerina/toml.lexer:0.8.0:LexicalError|ballerina/toml:0.8.0:WritingError|ballerina/io:1.8.1:Error|ballerina/file:1.13.0:Error;
+type Error parser:GrammarError|parser:ConversionError|lexer:LexicalError|WritingError|io:Error|file:Error;
 
-// Unknown type: LexicalError
+# Represents an error caused by the lexical analyzer.
+type LexicalError lexer:LexicalError;
 
-// Unknown type: GrammarError
+# Represents an error caused for an invalid grammar production.
+type GrammarError parser:GrammarError;
 
-// Unknown type: ConversionError
+# Represents an error caused by the Ballerina lang when converting a data type.
+type ConversionError parser:ConversionError;
 
 # Configurations for writing a TOML document.
 # 
`````

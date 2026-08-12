# pdf — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `pdf` |
| **Old file** | `pdf/old/ballerina_pdf.bal.txt` |
| **New file** | `pdf/new/ballerina_pdf.bal.txt` |
| **Old lines** | 240 |
| **New lines** | 246 |
| **Lines added** | 11 |
| **Lines removed** | 5 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 4 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (4)

- `type Error`
- `type HtmlParseError`
- `type ReadError`
- `type RenderError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 97–109 | 97–115 | Types | +10 | −4 |
| 2 | 123–129 | 129–135 | Types | +1 | −1 |

---

## Unified diff

`````diff
--- pdf/old/ballerina_pdf.bal.txt	2026-08-12 23:21:51
+++ pdf/new/ballerina_pdf.bal.txt	2026-08-12 23:23:51
@@ -97,13 +97,19 @@
 
 const string LEGAL = "LEGAL";
 
-// Unknown type: Error
+# Base error type for all PDF module errors.
+type Error error;
 
-// Unknown type: HtmlParseError
+# Error during HTML parsing or preprocessing.
+# Returned when the input HTML cannot be parsed into a valid DOM.
+type HtmlParseError error;
 
-// Unknown type: RenderError
+# Error during the PDF rendering pipeline (layout, painting, or PDF generation).
+type RenderError error;
 
-// Unknown type: ReadError
+# Error during PDF reading operations (text extraction, image conversion).
+# Returned when the input PDF is corrupted, inaccessible, or invalid.
+type ReadError error;
 
 # Standard page size presets for PDF output.
 enum StandardPageSize {
@@ -123,7 +129,7 @@
 };
 
 # Page size for PDF output. Use a standard preset or specify custom dimensions in points.
-type PageSize "LEGAL"|"LETTER"|"A4"|ballerina/pdf:0.9.1:CustomPageSize;
+type PageSize "LEGAL"|"LETTER"|"A4"|CustomPageSize;
 
 # Page margins in points (1 point = 1/72 inch). 
 # This is the default margin for the PDF output.
`````

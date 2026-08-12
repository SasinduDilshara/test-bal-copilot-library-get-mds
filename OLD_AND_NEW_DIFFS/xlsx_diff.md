# xlsx — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `xlsx` |
| **Old file** | `xlsx/old/ballerina_xlsx.bal.txt` |
| **New file** | `xlsx/new/ballerina_xlsx.bal.txt` |
| **Old lines** | 638 |
| **New lines** | 891 |
| **Lines added** | 269 |
| **Lines removed** | 16 |
| **Hunks** | 5 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 12 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 4 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (56)

- `annotation Name`
- `class Workbook`
- `function close`
- `function createSheet`
- `function createTable`
- `function createTableFromData`
- `function deleteRow`
- `function deleteSheet`
- `function deleteTable`
- `function getAllTables`
- `function getCell`
- `function getCellRange`
- `function getColumn`
- `function getColumnCount`
- `function getDataCellRange`
- `function getDataRange`
- `function getDisplayName`
- `function getHeaders`
- `function getName`
- `function getRange`
- `function getRow`
- `function getRowCount`
- `function getRows`
- `function getSheet`
- `function getSheetCount`
- `function getSheetName`
- `function getSheetNames`
- `function getTable`
- `function getTables`
- `function getTotalRow`
- `function getUsedCellRange`
- `function getUsedRange`
- `function hasSheet`
- `function hasTotalRow`
- `function init`
- `function putRows`
- `function rename`
- `function resize`
- `function save`
- `function saveAs`
- `function setCell`
- `function setCellByAddress`
- `function setColumn`
- `function setRow`
- `function toBytes`
- `type ConstraintValidationError`
- `type Error`
- `type FileNotFoundError`
- `type InvalidTableRangeError`
- `type ParseError`
- `type SheetExistsError`
- `type SheetNotFoundError`
- `type TableExistsError`
- `type TableNotFoundError`
- `type TableOverlapError`
- `type TypeConversionError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 255–285 | 255–399 | Types | +127 | −13 |
| 2 | 294–299 | 408–495 | Types | +82 | −0 |
| 3 | 507–517 | 703–713 | Types | +2 | −2 |
| 4 | 548–555 | 744–803 | Types | +53 | −1 |
| 5 | 636–638 | 884–891 | Functions | +5 | −0 |

---

## Unified diff

`````diff
--- xlsx/old/ballerina_xlsx.bal.txt	2026-08-12 23:21:51
+++ xlsx/new/ballerina_xlsx.bal.txt	2026-08-12 23:23:51
@@ -255,31 +255,145 @@
     string fieldName?;
 };
 
-// Unknown type: Error
-
-// Unknown type: ParseError
+# The base type for all `xlsx` module errors.
+type Error error<ErrorDetails>;
 
-// Unknown type: FileNotFoundError
+# The workbook content is malformed or could not be read.
+type ParseError error<ErrorDetails>;
 
-// Unknown type: SheetNotFoundError
+# The XLSX file path does not exist or could not be accessed.
+type FileNotFoundError error<ErrorDetails>;
+
+# No sheet matches the given name or index.
+type SheetNotFoundError error<ErrorDetails>;
 
-// Unknown type: SheetExistsError
+# A sheet with the target name already exists.
+type SheetExistsError error<ErrorDetails>;
 
-// Unknown type: TypeConversionError
+# A cell value could not be converted to the target type.
+type TypeConversionError error<ErrorDetails>;
 
-// Unknown type: ConstraintValidationError
-
-// Unknown type: TableNotFoundError
+# A parsed record failed a `@constraint` rule.
+type ConstraintValidationError error<ErrorDetails>;
 
-// Unknown type: TableExistsError
+# No table matches the given name.
+type TableNotFoundError error<ErrorDetails>;
 
-// Unknown type: TableOverlapError
+# A table with the target name already exists.
+type TableExistsError error<ErrorDetails>;
 
-// Unknown type: InvalidTableRangeError
+# A table write would overlap with another table.
+type TableOverlapError error<ErrorDetails>;
 
+# A table range or insert position is invalid.
+type InvalidTableRangeError error<ErrorDetails>;
+
 # A worksheet in a workbook, with methods to read and write rows, columns, cells, and tables.
 # Obtained from a `Workbook` (for example `getSheet` or `createSheet`); not constructed directly.
 class Sheet {
+
+    # Get the name of the sheet.
+    # 
+    function getName() returns string|Error;
+
+    # Get the used range of the sheet in A1 notation, such as "A1:D50".
+    # 
+    function getUsedRange() returns string|Error;
+
+    # Get the used cell range as a structured record, or nil if the sheet is empty.
+    # 
+    function getUsedCellRange() returns CellRange|()|Error;
+
+    # Get the number of rows with data.
+    # 
+    function getRowCount() returns int|Error;
+
+    # Get the number of columns with data.
+    # 
+    function getColumnCount() returns int|Error;
+
+    # Read all rows from the sheet as records, maps, or a string grid.
+    # 
+    function getRows(ParseOptions options = {}, xlsx:Row t = <>) returns t[]|Error;
+
+    # Read a single row by index as a record, map, or string array.
+    # 
+    function getRow(int index, RowParseOptions options = {}, xlsx:Row t = <>) returns t|Error;
+
+    # Write rows to the sheet (records, maps, or string arrays).
+    # 
+    # By default rows are appended below the existing data; `sheetWriteMode` selects another
+    # disposition.
+    # 
+    function putRows(Row[] data, boolean writeHeaders = true, int startRowIndex = 0, SheetWriteMode sheetWriteMode = APPEND, WriteOptions options) returns Error|();
+
+    # Get a column of values by header name or 0-based index.
+    # 
+    function getColumn(string|int columnRef, ColumnParseOptions options = {}, xlsx:CellValue t = <>) returns t[]|Error;
+
+    # Read a single cell, bound to the target type.
+    # 
+    # The target type drives the binding: the default `CellValue` yields the cell's natural value,
+    # while a `time:Civil` / `time:Date` / `time:TimeOfDay` or scalar target yields that type.
+    # 
+    function getCell(int rowIndex, int columnIndex, xlsx:CellValue t = <>) returns t|Error;
+
+    # Write a single row at the given 0-based row index.
+    # 
+    # By default the row is overwritten; `sheetWriteMode` selects another disposition. For a record
+    # or map, values align to columns by header name, using the header at `options.headerRowIndex`.
+    # 
+    function setRow(int rowIndex, Row data, int headerRowIndex = 0, SheetWriteMode sheetWriteMode = REPLACE, RowWriteOptions options) returns Error|();
+
+    # Write a column of values by header name or 0-based index.
+    # 
+    # Values are written into successive rows below the header row.
+    # 
+    function setColumn(string|int columnRef, CellValue[] data) returns Error|();
+
+    # Write a single cell by 0-based row and column index.
+    # 
+    function setCell(int rowIndex, int columnIndex, CellValue value) returns Error|();
+
+    # Write a single cell by A1-notation address.
+    # 
+    function setCellByAddress(string cellAddress, CellValue value) returns Error|();
+
+    # Delete a row from the sheet; subsequent rows shift up by one.
+    # 
+    function deleteRow(int index) returns Error|();
+
+    # Rename the sheet.
+    # 
+    # The new name must follow Excel rules (at most 31 characters, none of `\ / ? * [ ] :`) and be
+    # unique in the workbook.
+    # 
+    function rename(string newName) returns Error|();
+
+    # Get a table on this sheet by name.
+    # 
+    function getTable(string name) returns Table|Error;
+
+    # Get all tables on this sheet.
+    # 
+    function getTables() returns Table[]|Error;
+
+    # Create a table over an existing range.
+    # 
+    # The range must include a header row. If `headers` is not given, the first row is used.
+    # 
+    function createTable(string name, CellRange|string range, string[]|() headers = ()) returns Table|Error;
+
+    # Write data and wrap it in a new table, computing the range automatically.
+    # 
+    # The table always has a header row: field names (or `@xlsx:Name`) for records, keys for maps,
+    # or the first row for `string[][]`.
+    # 
+    function createTableFromData(string name, Row[] data, int startRowIndex = 0, int startColumnIndex = 0) returns Table|Error;
+
+    # Delete a table from this sheet. The underlying data is preserved.
+    # 
+    function deleteTable(string name) returns Error|();
 }
 
 # An Excel Table (ListObject) in a worksheet, with automatic header handling, an optional totals
@@ -294,6 +408,88 @@
 # check empTable.putRows(newEmployees);
 # ```
 class Table {
+
+    # Get the name of the table. Table names are unique across the workbook.
+    # 
+    function getName() returns string|Error;
+
+    # Get the display name of the table, as shown in the Excel UI.
+    # 
+    function getDisplayName() returns string|Error;
+
+    # Get the name of the sheet that holds this table.
+    # 
+    function getSheetName() returns string|Error;
+
+    # Get the full table range, including the header and totals row, in A1 notation.
+    # 
+    function getRange() returns string|Error;
+
+    # Get the full table range, including the header and totals row, as a `CellRange` (0-based).
+    # 
+    function getCellRange() returns CellRange|Error;
+
+    # Get the data range, excluding the header and totals row, in A1 notation.
+    # 
+    function getDataRange() returns string|Error;
+
+    # Get the data range, excluding the header and totals row, as a `CellRange` (0-based).
+    # 
+    function getDataCellRange() returns CellRange|Error;
+
+    # Get the number of data rows, excluding the header and totals row.
+    # 
+    function getRowCount() returns int|Error;
+
+    # Get the number of columns in the table.
+    # 
+    function getColumnCount() returns int|Error;
+
+    # Get the column header names, in column order.
+    # 
+    function getHeaders() returns string[]|Error;
+
+    # Read all data rows from the table as records, maps, or a string grid.
+    # 
+    # The header and any totals row are excluded.
+    # 
+    function getRows(TableParseOptions options = {}, xlsx:Row t = <>) returns t[]|Error;
+
+    # Read a single data row by index as a record, map, or string array.
+    # 
+    function getRow(int index, TableRowParseOptions options = {}, xlsx:Row t = <>) returns t|Error;
+
+    # Write rows to the table, resizing its data range to fit.
+    # 
+    # By default the data is replaced; `tableWriteMode = APPEND` adds rows below it instead.
+    # A resize that would overlap another table fails with a `TableOverlapError`.
+    # 
+    function putRows(Row[] data, TableWriteMode tableWriteMode = REPLACE, int insertAt = 0, TableWriteOptions options) returns Error|();
+
+    # Check whether the table has a totals row.
+    # 
+    function hasTotalRow() returns boolean|Error;
+
+    # Get the totals row as a map keyed by column name.
+    # 
+    # Each value binds to its natural cell value, or `()` for a blank total cell.
+    # 
+    function getTotalRow(map<xlsx:CellValue> t = <>) returns t|Error;
+
+    # Rename the table. The new name must be unique in the workbook.
+    # 
+    function rename(string newName) returns Error|();
+
+    # Resize the table to a new range, which must include a header row and a data row.
+    # For automatic resizing on write, use `putRows` instead.
+    # 
+    function resize(CellRange|string newRange) returns Error|();
+
+    # Delete a data row by 0-based index; the table shrinks and rows below move up.
+    # 
+    # A table must keep at least one data row, so the last one cannot be deleted.
+    # 
+    function deleteRow(int index) returns Error|();
 }
 
 # How to read cells that contain a formula.
@@ -507,11 +703,11 @@
 };
 
 # An XLSX cell value: a string, number (int/float/decimal), boolean, date/time, or `()` for a blank cell.
-type CellValue string|int|float|decimal|boolean|ballerina/time:2.8.1:Date|ballerina/time:2.8.1:Civil|ballerina/time:2.8.1:TimeOfDay|();
+type CellValue string|int|float|decimal|boolean|time:Date|time:Civil|time:TimeOfDay|();
 
 # A single row: either a `map<CellValue>` keyed by column header, or a `string[]` of cell text
 # in column order. A typed record also binds when every field type is a subtype of `CellValue`.
-type Row map<ballerina/xlsx:1.0.1:CellValue>|string[];
+type Row map<CellValue>|string[];
 
 # A rectangular cell range in a sheet, with all indices 0-based.
 
@@ -548,8 +744,60 @@
     string offendingRow?;
 };
 
-// Unknown type: Workbook
+# Create an empty in-memory workbook. Persist it with `saveAs(path)`, since `save()` has no
+# source path yet. To open an existing workbook, use `xlsx:fromFile` or `xlsx:fromBytes`.
+class Workbook {
+    function init() returns ();
+
+    # Get all sheet names in the workbook.
+    # 
+    function getSheetNames() returns string[]|Error;
 
+    # Get the number of sheets in the workbook.
+    # 
+    function getSheetCount() returns int|Error;
+
+    # Check whether a sheet with the given name exists.
+    # 
+    function hasSheet(string name) returns boolean|Error;
+
+    # Get a sheet by name or 0-based index.
+    # 
+    function getSheet(string|int target) returns Sheet|Error;
+
+    # Create a new sheet in the workbook.
+    # 
+    function createSheet(string name) returns Sheet|Error;
+
+    # Delete a sheet by name or 0-based index.
+    # 
+    function deleteSheet(string|int target) returns Error|();
+
+    # Save the workbook, overwriting the file it was opened from or last saved to with `saveAs`.
+    # 
+    function save() returns Error|();
+
+    # Save the workbook to a new path, which then becomes the target of later `save()` calls.
+    # 
+    function saveAs(string path) returns Error|();
+
+    # Serialize the workbook to a byte array, for example to send as an HTTP response.
+    # 
+    function toBytes() returns byte[]|Error;
+
+    # Close the workbook and release its resources. Call this when done to free memory.
+    # 
+    function close() returns Error|();
+
+    # Get a table by name from anywhere in the workbook. Table names are unique workbook-wide.
+    # 
+    function getTable(string name) returns Table|Error;
+
+    # Get all tables across every sheet in the workbook.
+    # 
+    function getAllTables() returns Table[]|Error;
+}
+
 // --- Functions ---
 
 # Parse a sheet from an XLSX file into records, maps, or a string grid.
@@ -636,3 +884,8 @@
 # + sourceBytes - XLSX content as a byte array
 # + return - The opened workbook, or an error if the bytes are invalid
 function fromBytes(byte[] sourceBytes) returns Workbook|Error;
+
+// --- Annotations ---
+
+# Annotation to specify the Excel column name for a record field.
+public annotation NameConfig Name on record field;
`````

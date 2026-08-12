# googleapis.sheets — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `googleapis.sheets` |
| **Old file** | `googleapis.sheets/old/ballerinax_googleapis.sheets.bal.txt` |
| **New file** | `googleapis.sheets/new/ballerinax_googleapis.sheets.bal.txt` |
| **Old lines** | 754 |
| **New lines** | 881 |
| **Lines added** | 174 |
| **Lines removed** | 47 |
| **Hunks** | 8 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 3 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 3 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (3)

- `type Error`
- `type InvalidRangeError`
- `type SpreadsheetError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 219–232 | 219–238 | Types | +9 | −3 |
| 2 | 297–336 | 303–353 | Types | +11 | −0 |
| 3 | 339–458 | 356–513 | Types | +38 | −0 |
| 4 | 461–466 | 516–522 | Types | +1 | −0 |
| 5 | 471–476 | 527–533 | Types | +1 | −0 |
| 6 | 479–484 | 536–542 | Types | +1 | −0 |
| 7 | 488–577 | 546–662 | Types | +29 | −2 |
| 8 | 579–754 | 664–881 | Client | +84 | −42 |

---

## Unified diff

`````diff
--- googleapis.sheets/old/ballerinax_googleapis.sheets.bal.txt	2026-08-12 12:57:30
+++ googleapis.sheets/new/ballerinax_googleapis.sheets.bal.txt	2026-08-12 13:19:19
@@ -219,14 +219,20 @@
     FORMATTED_VALUE
 }
 
-// Unknown type: Error
+# Defines the generic error type for the `googleapis.sheets` module.
+type Error error;
 
-// Unknown type: SpreadsheetError
+# Error that occurs when a spreadsheet or sheet operation fails. This could be due to the resource not being found,
+# insufficient permissions, or an API-level rejection.
+type SpreadsheetError error;
 
-// Unknown type: InvalidRangeError
+# Error that occurs when an invalid cell range is provided. This could be due to malformed A1 notation or a range
+# that falls outside the bounds of the sheet.
+type InvalidRangeError error;
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # Configurations related to client authentication
     http:BearerTokenConfig|OAuth2RefreshTokenGrantConfig auth; // Special Agent Note: BearerTokenConfig FROM ballerina/http package
@@ -297,40 +303,51 @@
     # Proxy server username
     string userName?;
     # Proxy server password
+    @display {label: "", kind: "password"}
     string password?;
 };
 
 # Spreadsheet information.
 # 
 
+@display {label: "Spreadsheet"}
 type Spreadsheet record {
     # Id of the spreadsheet
+    @display {label: "Spreadsheet Id"}
     string spreadsheetId?;
     # Properties of a spreadsheet
     SpreadsheetProperties properties?;
     # The sheets that are part of a spreadsheet
+    @display {label: "Array of Worksheets"}
     Sheet[] sheets?;
     # The Url of the spreadsheet
+    @display {label: "Spreadsheet Url"}
     string spreadsheetUrl?;
 };
 
 # Spreadsheet properties.
 # 
 
+@display {label: "Spreadsheet Properties"}
 type SpreadsheetProperties record {
     # The title of the spreadsheet
+    @display {label: "Spreadsheet Title"}
     string title?;
     # The locale of the spreadsheet
+    @display {label: "Spreadsheet Locale"}
     string locale?;
     # The amount of time to wait before volatile functions are recalculated
+    @display {label: "Auto Recalculate Time"}
     string autoRecalc?;
     # The time zone of the spreadsheet
+    @display {label: "Spreadsheet Timezone"}
     string timeZone?;
 };
 
 # Worksheet information.
 # 
 
+@display {label: "Worksheet"}
 type Sheet record {
     # Properties of a worksheet
     SheetProperties properties?;
@@ -339,120 +356,158 @@
 # Worksheet properties.
 # 
 
+@display {label: "Worksheet Properties"}
 type SheetProperties record {
     # The ID of the worksheet
+    @display {label: "Worksheet ID"}
     int sheetId?;
     # The name of the worksheet
+    @display {label: "Worksheet Title"}
     string title?;
     # The index of the worksheet within the spreadsheet
+    @display {label: "Worksheet Index"}
     int index?;
     # The type of worksheet
+    @display {label: "Worksheet Type"}
     string sheetType?;
     # Additional properties of the worksheet if this worksheet is a grid
     GridProperties gridProperties?;
     # True if the worksheet is hidden in the UI, false if it is visible
+    @display {label: "Hidden"}
     boolean hidden?;
     # True if the worksheet is an RTL worksheet instead of an LTR worksheet
+    @display {label: "Right To Left"}
     boolean rightToLeft?;
 };
 
 # Grid properties.
 # 
 
+@display {label: "Grid Properties"}
 type GridProperties record {
     # The number of rows in the grid
+    @display {label: "Row Count"}
     int rowCount?;
     # The number of columns in the grid
+    @display {label: "Column Count"}
     int columnCount?;
     # The number of rows that are frozen in the grid
+    @display {label: "Frozen Row Count"}
     int frozenRowCount?;
     # The number of columns that are frozen in the grid
+    @display {label: "Frozen Column Count"}
     int frozenColumnCount?;
     # True if the grid is not showing gridlines in the UI
+    @display {label: "Hide Grid Lines"}
     boolean hideGridlines?;
 };
 
 # Single cell or a group of adjacent cells in a sheet.
 # 
 
+@display {label: "Range"}
 type Range record {
     # The column letter followed by the row number.
 For example for a single cell "A1" refers to the intersection of column "A" with row "1",
 and for a range of cells "A1:D5" refers to the top left cell and the bottom right cell of a range
+    @display {label: "A1 Notation"}
     string a1Notation;
     # Values of the given range
+    @display {label: "Values"}
     (int|string|decimal)[][] values;
 };
 
 # Single column in a sheet.
 # 
 
+@display {label: "Column"}
 type Column record {
     # The column letter
+    @display {label: "Column Letter"}
     string columnPosition;
     # Values of the given column
+    @display {label: "Values"}
     (int|string|decimal)[] values;
 };
 
 # Single row in a sheet.
 # 
 
+@display {label: "Row"}
 type Row record {
     # The row number
+    @display {label: "Row Number"}
     int rowPosition;
     # Values of the given row
+    @display {label: "Values"}
     (int|string|decimal)[] values;
 };
 
 # A1 Notation of a ValueRange
 # 
 
+@display {label: "A1Range"}
 type A1Range record {
     # Sheet name in A1 notation
+    @display {label: "Sheet Name"}
     string sheetName;
     # Starting cell of the range
+    @display {label: "Start Index"}
     string startIndex?;
     # Ending cell of the range
+    @display {label: "End Index"}
     string endIndex?;
 };
 
 # Values related to a single row.
 # 
 
+@display {label: "ValueRange"}
 type ValueRange record {
     # The row number
+    @display {label: "Row Number"}
     int rowPosition;
     # Values of the given row
+    @display {label: "Values"}
     (int|string|decimal|boolean|float)[] values;
     # A1Notation of the range
+    @display {label: "A1 Range"}
     A1Range a1Range;
 };
 
 # Values related to a multiple rows.
 # 
 
+@display {label: "ValuesRange"}
 type ValuesRange record {
     # The row number
+    @display {label: "Starting Row Number"}
     int rowStartPosition;
     # Values of the given rows
+    @display {label: "Values"}
     (int|string|decimal|boolean|float)[][] values;
     # A1Notation of the range
+    @display {label: "A1 Range"}
     A1Range a1Range;
 };
 
 # Single cell in a sheet.
 # 
 
+@display {label: "Cell"}
 type Cell record {
     # The column letter followed by the row number.
 For example for a single cell "A1" refers to the intersection of column "A" with row "1"
+    @display {label: "A1 Notation"}
     string a1Notation;
     # Value of the given cell
+    @display {label: "Value"}
     int|string|decimal value;
 };
 
 # The metadata visibility
 # 
+@display {label: "Metadata Visibility"}
 enum Visibility {
     PROJECT,
     DOCUMENT,
@@ -461,6 +516,7 @@
 
 # The location type for filters
 # 
+@display {label: "Location Type"}
 enum LocationType {
     ROW,
     SHEET,
@@ -471,6 +527,7 @@
 
 # Dimension
 # 
+@display {label: "Dimension"}
 enum Dimension {
     ROWS,
     COLUMNS,
@@ -479,6 +536,7 @@
 
 # The location matching strategy for filters
 # 
+@display {label: "Location Matching Strategy"}
 enum LocationMatchingStrategy {
     INTERSECTING_LOCATION,
     EXACT_LOCATION,
@@ -488,90 +546,117 @@
 # The DeveloperMetadataLookup filter
 # 
 
+@display {label: "DeveloperMetadataLookup Filter"}
 type DeveloperMetadataLookupFilter record {
     # Specified type which the metadata ara associated.
 For more information, see [LocationType](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.developerMetadata#DeveloperMetadata.DeveloperMetadataLocationType)
+    @display {label: "Location Type"}
     LocationType locationType;
     # An enumeration of strategies for matching developer metadata locations.
 For more information, see [locationMatchingStrategy](https://developers.google.com/sheets/api/reference/rest/v4/DataFilter#DeveloperMetadataLocationMatchingStrategy).
+    @display {label: "Location matching strategy"}
     LocationMatchingStrategy locationMatchingStrategy?;
     # The spreadsheet-scoped unique ID that identifies the metadata.
+    @display {label: "Metadata Id"}
     int metadataId?;
     # Key used to identify metadata.
+    @display {label: "Metadata Key"}
     string metadataKey?;
     # Data associated with the metadata's key.
+    @display {label: "Metadata Value"}
     string metadataValue;
     # Visibility scope of the associated metadata
 For more information, see [Visibility](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.developerMetadata#DeveloperMetadata.DeveloperMetadataVisibility).
+    @display {label: "Metadata Visibility"}
     Visibility visibility?;
     # Location of association for metadata
 
+    @display {label: "Metadata Location"}
     MetadataLocation metadataLocation?;
 };
 
 # The Metadata Location
 # 
 
+@display {label: "Metadata Location"}
 type MetadataLocation record {
     # Specified type which the metadata ara associated.
 For more information, see [LocationType](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.developerMetadata#DeveloperMetadata.DeveloperMetadataLocationType)
+    @display {label: "Location Type"}
     LocationType locationType;
     # Whether metadata is associated with an entire spreadsheet.
+    @display {label: "Spreadsheet"}
     boolean spreadsheet;
     # The ID of the worksheet
+    @display {label: "Worksheet ID"}
     int sheetId;
     # Dimension when the metadata is associated with them
 
+    @display {label: "Dimension Range"}
     DimensionRange dimensionRange;
 };
 
 # The Dimension Range
 # 
 
+@display {label: "Dimension Range"}
 type DimensionRange record {
     # The ID of the worksheet
+    @display {label: "Worksheet ID"}
     int sheetId;
     # The dimension of the span
+    @display {label: "Dimension"}
     Dimension dimension;
     # The start (inclusive) of the span, or not set if unbounded
+    @display {label: "Start Index"}
     int startIndex;
     # The end (exclusive) of the span, or not set if unbounded.
 
+    @display {label: "End Index"}
     int endIndex;
 };
 
 # The GridRange filters
 # 
 
+@display {label: "Gridrange Filter"}
 type GridRangeFilter record {
     # The ID of the worksheet
+    @display {label: "Worksheet ID"}
     int sheetId;
     # The start row (inclusive) of the range, or not set if unbounded.
+    @display {label: "Starting Row Index"}
     int startRowIndex?;
     # The end row (exclusive) of the range, or not set if unbounded.
+    @display {label: "Ending Row Index"}
     int endRowIndex?;
     # The start column (inclusive) of the range, or not set if unbounded.
+    @display {label: "Starting Column Index"}
     int startColumnIndex?;
     # The end column (exclusive) of the range, or not set if unbounded.
 
+    @display {label: "Ending Column Index"}
     int endColumnIndex?;
 };
 
 # Type of filter used to match data.
 # 
-type Filter ballerinax/googleapis.sheets:4.0.0:A1Range|ballerinax/googleapis.sheets:4.0.0:DeveloperMetadataLookupFilter|ballerinax/googleapis.sheets:4.0.0:GridRangeFilter;
+@display {label: "Filter"}
+type Filter A1Range|DeveloperMetadataLookupFilter|GridRangeFilter;
 
 // --- Client ---
 
 # Ballerina Google Sheets connector provides the capability to access Google Sheets API.
 # The connector let you perform spreadsheet management operations, worksheet management operations and
 # the capability to handle Google Sheets data level operations.
+@display {label: "Google Sheets", iconPath: "icon.png"}
 client class Client {
     function init(ConnectionConfig config, string serviceUrl = https://sheets.googleapis.com, string driveServiceUrl = https://www.googleapis.com) returns error?;
 
     # Creates a new spreadsheet.
     # 
-    remote function createSpreadsheet(string name) returns Spreadsheet|error;
+    @display {label: "Create Google Sheet"}
+    remote function createSpreadsheet(@display {label: "Google Sheet Name"} string name) returns Spreadsheet|error;
 
     # Deletes a spreadsheet by the given ID.
     # 
@@ -579,176 +664,218 @@
     # your Google Cloud project. The OAuth token must include the
     # `https://www.googleapis.com/auth/drive.file` scope (or broader Drive scope).
     # 
-    remote function deleteSpreadsheet(string spreadsheetId) returns error?;
+    @display {label: "Delete Google Sheet"}
+    remote function deleteSpreadsheet(@display {label: "Google Sheet ID"} string spreadsheetId) returns error?;
 
     # Opens a spreadsheet by the given ID.
     # 
-    remote function openSpreadsheetById(string spreadsheetId) returns Spreadsheet|error;
+    @display {label: "Open Google Sheet By ID"}
+    remote function openSpreadsheetById(@display {label: "Google Sheet ID"} string spreadsheetId) returns Spreadsheet|error;
 
     # Opens a spreadsheet by the given Url.
     # 
-    remote function openSpreadsheetByUrl(string url) returns Spreadsheet|error;
+    @display {label: "Open Google Sheet By Url"}
+    remote function openSpreadsheetByUrl(@display {label: "Google Sheet Url"} string url) returns Spreadsheet|error;
 
     # Renames the spreadsheet with the given name.
     # 
-    remote function renameSpreadsheet(string spreadsheetId, string name) returns error?;
+    @display {label: "Rename Google Sheet"}
+    remote function renameSpreadsheet(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "New Google Sheet Name"} string name) returns error?;
 
     # Get worksheets of the spreadsheet.
     # 
-    remote function getSheets(string spreadsheetId) returns Sheet[]|error;
+    @display {label: "Get Worksheets"}
+    remote function getSheets(@display {label: "Google Sheet ID"} string spreadsheetId) returns Sheet[]|error;
 
     # Get a worksheet of the spreadsheet.
     # 
-    remote function getSheetByName(string spreadsheetId, string sheetName) returns Sheet|error;
+    @display {label: "Get Worksheet By Name"}
+    remote function getSheetByName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName) returns Sheet|error;
 
     # Add a new worksheet.
     # 
-    remote function addSheet(string spreadsheetId, string sheetName) returns Sheet|error;
+    @display {label: "Add New Worksheet"}
+    remote function addSheet(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName) returns Sheet|error;
 
     # Delete specified worksheet by worksheet ID.
     # 
-    remote function removeSheet(string spreadsheetId, int sheetId) returns error?;
+    @display {label: "Remove Worksheet By ID"}
+    remote function removeSheet(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId) returns error?;
 
     # Delete specified worksheet by worksheet name.
     # 
-    remote function removeSheetByName(string spreadsheetId, string sheetName) returns error?;
+    @display {label: "Remove Worksheet"}
+    remote function removeSheetByName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName) returns error?;
 
     # Renames the worksheet of a given spreadsheet with the given name.
     # 
-    remote function renameSheet(string spreadsheetId, string sheetName, string name) returns error?;
+    @display {label: "Rename Worksheet"}
+    remote function renameSheet(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Existing Worksheet Name"} string sheetName, @display {label: "New Worksheet Name"} string name) returns error?;
 
     # Sets the values of the given range of cells of the worksheet.
     # 
-    remote function setRange(string spreadsheetId, string sheetName, Range range, string|() valueInputOption = ()) returns error?;
+    @display {label: "Set Range"}
+    remote function setRange(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, Range range, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error?;
 
     # Gets the given range of the worksheet.
     # 
-    remote function getRange(string spreadsheetId, string sheetName, string a1Notation, string|() valueRenderOption = ()) returns Range|error;
+    @display {label: "Get Range"}
+    remote function getRange(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Range A1 Notation"} string a1Notation, @display {label: "Value Render Option"} string|() valueRenderOption = ()) returns Range|error;
 
     # Clears the range of contents, formats, and data validation rules.
     # 
-    remote function clearRange(string spreadsheetId, string sheetName, string a1Notation) returns error?;
+    @display {label: "Clear Range"}
+    remote function clearRange(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Range A1 Notation"} string a1Notation) returns error?;
 
     # Inserts the given number of columns before the given column position by worksheet ID.
     # 
-    remote function addColumnsBefore(string spreadsheetId, int sheetId, int index, int numberOfColumns) returns error?;
+    @display {label: "Add Columns Before By Sheet ID"}
+    remote function addColumnsBefore(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Column Position"} int index, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Inserts the given number of columns before the given column position by worksheet name.
     # 
-    remote function addColumnsBeforeBySheetName(string spreadsheetId, string sheetName, int index, int numberOfColumns) returns error?;
+    @display {label: "Add Columns Before"}
+    remote function addColumnsBeforeBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Column Position"} int index, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Inserts the given number of columns after the given column position by worksheet ID.
     # 
-    remote function addColumnsAfter(string spreadsheetId, int sheetId, int index, int numberOfColumns) returns error?;
+    @display {label: "Add Columns After By Sheet ID"}
+    remote function addColumnsAfter(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Column Position"} int index, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Inserts the given number of columns after the given column position by worksheet name.
     # 
-    remote function addColumnsAfterBySheetName(string spreadsheetId, string sheetName, int index, int numberOfColumns) returns error?;
+    @display {label: "Add Columns After"}
+    remote function addColumnsAfterBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Column Position"} int index, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Create or Update a Column.
     # 
-    remote function createOrUpdateColumn(string spreadsheetId, string sheetName, string column, (int|string|decimal)[] values, string|() valueInputOption = ()) returns error?;
+    @display {label: "Set Column"}
+    remote function createOrUpdateColumn(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Column Position"} string column, @display {label: "Column Values"} (int|string|decimal)[] values, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error?;
 
     # Gets the values in the given column of the worksheet.
     # 
-    remote function getColumn(string spreadsheetId, string sheetName, string column, string|() valueRenderOption = ()) returns Column|error;
+    @display {label: "Get Column"}
+    remote function getColumn(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Column Position"} string column, @display {label: "Value Render Option"} string|() valueRenderOption = ()) returns Column|error;
 
     # Deletes the given number of columns starting at the given column position by worksheet ID.
     # 
-    remote function deleteColumns(string spreadsheetId, int sheetId, int column, int numberOfColumns) returns error?;
+    @display {label: "Delete Columns By Sheet ID"}
+    remote function deleteColumns(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Starting Column Position"} int column, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Deletes the given number of columns starting at the given column position by worksheet name.
     # 
-    remote function deleteColumnsBySheetName(string spreadsheetId, string sheetName, int column, int numberOfColumns) returns error?;
+    @display {label: "Delete Columns"}
+    remote function deleteColumnsBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Starting Column Position"} int column, @display {label: "Number of Columns"} int numberOfColumns) returns error?;
 
     # Inserts the given number of rows before the given row position by worksheet ID.
     # 
-    remote function addRowsBefore(string spreadsheetId, int sheetId, int index, int numberOfRows) returns error?;
+    @display {label: "Add Rows Before By Sheet ID"}
+    remote function addRowsBefore(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Row Position"} int index, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Inserts the given number of rows before the given row position by worksheet name.
     # 
-    remote function addRowsBeforeBySheetName(string spreadsheetId, string sheetName, int index, int numberOfRows) returns error?;
+    @display {label: "Add Rows Before"}
+    remote function addRowsBeforeBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Row Position"} int index, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Inserts a number of rows after the given row position by worksheet ID.
     # 
-    remote function addRowsAfter(string spreadsheetId, int sheetId, int index, int numberOfRows) returns error?;
+    @display {label: "Add Rows After By Sheet ID"}
+    remote function addRowsAfter(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Row Position"} int index, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Inserts a number of rows after the given row position by worksheet name.
     # 
-    remote function addRowsAfterBySheetName(string spreadsheetId, string sheetName, int index, int numberOfRows) returns error?;
+    @display {label: "Add Rows After"}
+    remote function addRowsAfterBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Row Position"} int index, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Create or update a row.
     # 
-    remote function createOrUpdateRow(string spreadsheetId, string sheetName, int row, (int|string|decimal)[] values, string|() valueInputOption = ()) returns error?;
+    @display {label: "Set Row"}
+    remote function createOrUpdateRow(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Row Position"} int row, @display {label: "Row Values"} (int|string|decimal)[] values, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error?;
 
     # Gets the values in the given row of the worksheet.
     # 
-    remote function getRow(string spreadsheetId, string sheetName, int row, string|() valueRenderOption = ()) returns Row|error;
+    @display {label: "Get Row"}
+    remote function getRow(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Row Position"} int row, @display {label: "Value Render Option"} string|() valueRenderOption = ()) returns Row|error;
 
     # Deletes the given number of rows starting at the given row position by worksheet ID.
     # 
-    remote function deleteRows(string spreadsheetId, int sheetId, int row, int numberOfRows) returns error?;
+    @display {label: "Delete Rows By Sheet ID"}
+    remote function deleteRows(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Starting Row Position"} int row, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Deletes the given number of rows starting at the given row position by worksheet name.
     # 
-    remote function deleteRowsBySheetName(string spreadsheetId, string sheetName, int row, int numberOfRows) returns error?;
+    @display {label: "Delete Rows"}
+    remote function deleteRowsBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Starting Row Position"} int row, @display {label: "Number of Rows"} int numberOfRows) returns error?;
 
     # Sets the value of the given cell of the worksheet.
     # 
-    remote function setCell(string spreadsheetId, string sheetName, string a1Notation, int|string|decimal value, string|() valueInputOption = ()) returns error?;
+    @display {label: "Set Cell"}
+    remote function setCell(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Cell A1 Notation"} string a1Notation, @display {label: "Cell Value"} int|string|decimal value, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error?;
 
     # Gets the value of the given cell of the sheet.
     # 
-    remote function getCell(string spreadsheetId, string sheetName, string a1Notation, string|() valueRenderOption = ()) returns Cell|error;
+    @display {label: "Get Cell"}
+    remote function getCell(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Cell A1 Notation"} string a1Notation, @display {label: "Value Render Option"} string|() valueRenderOption = ()) returns Cell|error;
 
     # Clears the given cell of contents, formats, and data validation rules.
     # 
-    remote function clearCell(string spreadsheetId, string sheetName, string a1Notation) returns error?;
+    @display {label: "Clear Cell"}
+    remote function clearCell(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet name"} string sheetName, @display {label: "Required Cell A1 Notation"} string a1Notation) returns error?;
 
     # Adds the given values to a row at the bottom of the worksheet. The input range is used to search
     # for existing data and find a "table" within that range. Values will be appended to the next row of
     # the table, starting with the first column of the table.
     # 
-    remote function appendValue(string spreadsheetId, (int|string|decimal|boolean|float)[] values, A1Range a1Range, string|() valueInputOption = ()) returns error|ValueRange;
+    @display {label: "Append Value"}
+    remote function appendValue(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Row Values"} (int|string|decimal|boolean|float)[] values, @display {label: "Range A1 Notation"} A1Range a1Range, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error|ValueRange;
 
     # Adds the given values to number of rows at the bottom of the worksheet. The input range is used to search
     # for existing data and find a "table" within that range. Values will be appended to the next rows of
     # the table, starting with the first column of the table.
     # 
-    remote function appendValues(string spreadsheetId, (int|string|decimal|boolean|float)[][] values, A1Range a1Range, string|() valueInputOption = ()) returns error|ValuesRange;
+    @display {label: "Append Value"}
+    remote function appendValues(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Row Values"} (int|string|decimal|boolean|float)[][] values, @display {label: "Range A1 Notation"} A1Range a1Range, @display {label: "Value Input Option"} string|() valueInputOption = ()) returns error|ValuesRange;
 
     # Copies the sheet to a given spreadsheet by worksheet ID.
     # 
-    remote function copyTo(string spreadsheetId, int sheetId, string destinationId) returns error?;
+    @display {label: "Copy Sheet By Sheet ID"}
+    remote function copyTo(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Destination Google Sheet ID"} string destinationId) returns error?;
 
     # Copies the sheet to a given spreadsheet by worksheet name.
     # 
-    remote function copyToBySheetName(string spreadsheetId, string sheetName, string destinationId) returns error?;
+    @display {label: "Copy Worksheet"}
+    remote function copyToBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName, @display {label: "Destination Google Sheet ID"} string destinationId) returns error?;
 
     # Clears the worksheet content and formatting rules by worksheet ID.
     # 
-    remote function clearAll(string spreadsheetId, int sheetId) returns error?;
+    @display {label: "Clear All By Sheet ID"}
+    remote function clearAll(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId) returns error?;
 
     # Clears the worksheet content and formatting rules by worksheet name.
     # 
-    remote function clearAllBySheetName(string spreadsheetId, string sheetName) returns error?;
+    @display {label: "Clear Worksheet"}
+    remote function clearAllBySheetName(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet Name"} string sheetName) returns error?;
 
     # Add developer metadata to the given row.
     # 
-    remote function setRowMetaData(string spreadsheetId, int sheetId, int rowIndex, Visibility visibility, string key, string value) returns error?;
+    @display {label: "Set Row Metadata"}
+    remote function setRowMetaData(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Index of the Row"} int rowIndex, @display {label: "Visibility of the Metadata"} Visibility visibility, @display {label: "Metadata Key"} string key, @display {label: "Metadata Value"} string value) returns error?;
 
     # Fetch rows matching to the given criteria in the filter.
     # Supports A1Range, GridRange and DeveloperMetadataLookup filters.
     # 
-    remote function getRowByDataFilter(string spreadsheetId, int sheetId, Filter filter) returns error|ValueRange[];
+    @display {label: "Get Row Using Data Filters"}
+    remote function getRowByDataFilter(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Filter"} Filter filter) returns error|ValueRange[];
 
     # Update rows matching the user provided data filter.
     # Supports a1Range, gridRange and Developer metadata lookup filters.
     # 
-    remote function updateRowByDataFilter(string spreadsheetId, int sheetId, Filter filter, (int|string|decimal|boolean|float)[] values, string valueInputOption) returns error?;
+    @display {label: "Update Row Using Data Filters"}
+    remote function updateRowByDataFilter(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Filter"} Filter filter, @display {label: "Row Values"} (int|string|decimal|boolean|float)[] values, @display {label: "Value Input Option"} string valueInputOption) returns error?;
 
     # Delete rows matching the user provided data filter
     # Supports a1Range, gridRange and Developer metadata lookup filters
     # 
-    remote function deleteRowByDataFilter(string spreadsheetId, int sheetId, Filter filter) returns error?;
+    @display {label: "delete Row Using Data Filters"}
+    remote function deleteRowByDataFilter(@display {label: "Google Sheet ID"} string spreadsheetId, @display {label: "Worksheet ID"} int sheetId, @display {label: "Filter"} Filter filter) returns error?;
 }
`````

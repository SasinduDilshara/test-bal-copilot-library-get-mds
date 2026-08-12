# io — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `io` |
| **Old file** | `io/old/ballerina_io.bal.txt` |
| **New file** | `io/new/ballerina_io.bal.txt` |
| **Old lines** | 356 |
| **New lines** | 879 |
| **Lines added** | 548 |
| **Lines removed** | 25 |
| **Hunks** | 4 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 24 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 1 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (66)

- `class BlockStream`
- `class CSVStream`
- `class CsvIterator`
- `class LineStream`
- `class ReadableByteChannel`
- `class ReadableCSVChannel`
- `class ReadableCharacterChannel`
- `class ReadableDataChannel`
- `class ReadableTextRecordChannel`
- `class StringReader`
- `class WritableByteChannel`
- `class WritableCSVChannel`
- `class WritableCharacterChannel`
- `class WritableDataChannel`
- `class WritableTextRecordChannel`
- `function base64Decode`
- `function base64Encode`
- `function blockStream`
- `function close`
- `function csvStream`
- `function getNext`
- `function getTable`
- `function hasNext`
- `function init`
- `function lineStream`
- `function next`
- `function read`
- `function readAll`
- `function readAllLines`
- `function readAllProperties`
- `function readBool`
- `function readChar`
- `function readFloat32`
- `function readFloat64`
- `function readInt16`
- `function readInt32`
- `function readInt64`
- `function readJson`
- `function readProperty`
- `function readString`
- `function readVarInt`
- `function readXml`
- `function skipHeaders`
- `function toTable`
- `function write`
- `function writeBool`
- `function writeFloat32`
- `function writeFloat64`
- `function writeInt16`
- `function writeInt32`
- `function writeInt64`
- `function writeJson`
- `function writeLine`
- `function writeProperties`
- `function writeString`
- `function writeVarInt`
- `function writeXml`
- `type AccessDeniedError`
- `type Block`
- `type ConfigurationError`
- `type ConnectionTimedOutError`
- `type EofError`
- `type Error`
- `type FileNotFoundError`
- `type GenericError`
- `type TypeMismatchError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 122–145 | 122–445 | Types | +309 | −9 |
| 2 | 159–179 | 459–487 | Types | +16 | −8 |
| 3 | 219–225 | 527–533 | Types | +1 | −1 |
| 4 | 233–252 | 541–775 | Types | +222 | −7 |

---

## Unified diff

`````diff
--- io/old/ballerina_io.bal.txt	2026-08-12 23:21:51
+++ io/new/ballerina_io.bal.txt	2026-08-12 23:23:51
@@ -122,24 +122,324 @@
 # Specifies the byte order to be the least significant byte first.
 const string LITTLE_ENDIAN = "LE";
 
-// Unknown type: Block
+# The read-only byte array that is used to read the byte content from the streams.
+type Block readonly & byte[];
 
-// Unknown type: ReadableByteChannel
+# Adding default init function to prevent object getting initialized from the user code.
+class ReadableByteChannel {
+    function init() returns ();
 
-// Unknown type: ReadableCharacterChannel
+    # Reads bytes from a given input resource.
+    # This operation will be asynchronous in which the total number of required bytes might not be returned at a given
+    # time. An `io:EofError` will return once the channel reaches the end.
+    # ```ballerina
+    # byte[]|io:Error result = readableByteChannel.read(1000);
+    # ```
+    # 
+    function read(int nBytes) returns byte[]|Error;
 
-// Unknown type: ReadableTextRecordChannel
+    # Reads all content of the channel as a `byte` array and return a read only `byte` array.
+    # ```ballerina
+    # byte[]|io:Error result = readableByteChannel.readAll();
+    # ```
+    # 
+    function readAll() returns byte[] & readonly|Error;
 
-// Unknown type: ReadableCSVChannel
+    # Returns a block stream that can be used to read all `byte` blocks as a stream.
+    # ```ballerina
+    # stream<io:Block, io:Error>|io:Error result = readableByteChannel.blockStream();
+    # ```
+    function blockStream(int blockSize) returns stream<Block, Error?>|Error;
 
-// Unknown type: WritableByteChannel
+    # Encodes a given `io:ReadableByteChannel` using the Base64 encoding scheme.
+    # ```ballerina
+    # io:ReadableByteChannel|Error encodedChannel = readableByteChannel.base64Encode();
+    # ```
+    # 
+    function base64Encode() returns ReadableByteChannel|Error;
 
-// Unknown type: WritableCharacterChannel
+    # Decodes a given Base64 encoded `io:ReadableByteChannel`.
+    # ```ballerina
+    # io:ReadableByteChannel|Error encodedChannel = readableByteChannel.base64Decode();
+    # ```
+    # 
+    function base64Decode() returns ReadableByteChannel|Error;
 
-// Unknown type: WritableTextRecordChannel
+    # Closes the readable byte channel to release any underlying resources.
+    # After a channel is closed, any further reading operations will cause an error.
+    # ```ballerina
+    # io:Error? err = readableByteChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
 
-// Unknown type: WritableCSVChannel
+# Initializes a readable character channel.
+# 
+class ReadableCharacterChannel {
+    function init(ReadableByteChannel byteChannel, string charset) returns ();
 
+    # Reads a given number of characters. This will attempt to read up to the `numberOfChars` characters of the channel.
+    # An `io:EofError` will return once the channel reaches the end.
+    # ```ballerina
+    # string|io:Error result = readableCharChannel.read(1000);
+    # ```
+    # 
+    function read(int numberOfChars) returns string|Error;
+
+    # Reads the entire channel content as a string.
+    # ```ballerina
+    # string|io:Error content = readableCharChannel.readString();
+    # ```
+    function readString() returns string|Error;
+
+    # Reads the entire channel content as a list of lines.
+    # ```ballerina
+    # string[]|io:Error content = readableCharChannel.readAllLines();
+    # ```
+    function readAllLines() returns string[]|Error;
+
+    # Reads a JSON from the given channel.
+    # ```ballerina
+    # json|io:Error result = readableCharChannel.readJson();
+    # ```
+    # 
+    function readJson() returns json|Error;
+
+    # Reads an XML from the given channel.
+    # ```ballerina
+    # json|io:Error result = readableCharChannel.readXml();
+    # ```
+    # 
+    function readXml() returns xml|Error;
+
+    # Reads the value of a specified property key from a properties file.
+    # If the key is not found, the provided default value is returned.
+    # ```ballerina
+    # string|io:Error result = readableCharChannel.readProperty(key, defaultValue);
+    # ```
+    function readProperty(string key, string defaultValue = "") returns string|Error;
+
+    # Returns a stream of lines that can be used to read all the lines in a file as a stream.
+    # ```ballerina
+    # stream<string, io:Error>|io:Error? result = readableCharChannel.lineStream();
+    # ```
+    # 
+    function lineStream() returns stream<string, Error?>|Error;
+
+    # Reads all properties from a properties file.
+    # ```ballerina
+    # map<string>|io:Error result = readableCharChannel.readAllProperties();
+    # ```
+    # 
+    function readAllProperties() returns map<string>|Error;
+
+    # Closes the character channel.
+    # After a channel is closed, any further reading operations will cause an error.
+    # ```ballerina
+    # io:Error? err = readableCharChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a readable text record channel.
+# 
+class ReadableTextRecordChannel {
+    function init(ReadableCharacterChannel charChannel, string fs = "", string rs = "", string fmt = "default") returns ();
+
+    # Checks whether there is a record left to be read.
+    # ```ballerina
+    # boolean hasNext = readableRecChannel.hasNext();
+    # ```
+    # 
+    function hasNext() returns boolean;
+
+    # Reads the next record from the input/output resource.
+    # ```ballerina
+    # string[]|io:Error record = readableRecChannel.getNext();
+    # ```
+    # 
+    function getNext() returns string[]|Error;
+
+    # Closes the record channel.
+    # After a channel is closed, any further reading operations will cause an error.
+    # ```ballerina
+    # io:Error err = readableRecChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a readable CSV channel.
+# 
+class ReadableCSVChannel {
+    function init(ReadableCharacterChannel byteChannel, Separator fs = ",", int nHeaders = 0) returns ();
+
+    # Skips the given number of headers.
+    # ```ballerina
+    # readableCSVChannel.skipHeaders(5);
+    # ```
+    # 
+    function skipHeaders(int nHeaders) returns ();
+
+    # Checks if there is another record available to be read from the CSV channel.
+    # ```ballerina
+    # boolean hasNext = readableCSVChannel.hasNext();
+    # ```
+    # 
+    function hasNext() returns boolean;
+
+    # Gets the next record from the CSV file.
+    # ```ballerina
+    # string[]|io:Error? record = readableCSVChannel.getNext();
+    # ```
+    # 
+    function getNext() returns string[]|Error|();
+
+    # Returns a CSV record stream that can be used to CSV records as a stream.
+    # ```ballerina
+    # stream<string[], io:Error>|io:Error? record = readableCSVChannel.csvStream();
+    # ```
+    # 
+    function csvStream() returns stream<string[], Error?>|Error;
+
+    # Closes the readable CSV channel to release any underlying resources.
+    # After a channel is closed, any further reading operations will cause an error.
+    # ```ballerina
+    # io:Error? err = readableCSVChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+
+    # Returns a table, which corresponds to the CSV records.
+    # ```ballerina
+    # var tblResult1 = readableCSVChannel.getTable(Employee);
+    # var tblResult2 = readableCSVChannel.getTable(Employee, ["id", "name"]);
+    # ```
+    # 
+    @deprecated
+    function getTable(record {|anydata...;|} structType, string[] fieldNames = []) returns table<record {|anydata...;|}>|Error;
+
+    # Returns a table, which corresponds to the CSV records.
+    # ```ballerina
+    # var tblResult = readableCSVChannel.toTable(Employee, ["id", "name"]);
+    # ```
+    # 
+    function toTable(record {|anydata...;|} structType, string[] keyFieldNames) returns table<record {|anydata...;|}>|Error;
+}
+
+# Adding default init function to prevent object getting initialized from the user code.
+class WritableByteChannel {
+    function init() returns ();
+
+    # Sinks bytes from a given input/output resource.
+    # 
+    # This is an asynchronous operation. The method might return before writing all the content.
+    # ```ballerina
+    # int|io:Error result = writableByteChannel.write(record, 0);
+    # ```
+    # 
+    function write(byte[] content, int offset) returns int|Error;
+
+    # Closes the byte channel.
+    # After a channel is closed, any further writing operations will cause an error.
+    # ```ballerina
+    # io:Error err = writableByteChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a writable character channel.
+# 
+class WritableCharacterChannel {
+    function init(WritableByteChannel bChannel, string charset) returns ();
+
+    # Writes a sequence of characters (string) to the writable character channel.
+    # ```ballerina
+    # int|io:Error result = writableCharChannel.write("Content", 0);
+    # ```
+    # 
+    function write(string content, int startOffset) returns int|Error;
+
+    # Writes a string as a line followed by a newline character (`\n`) to the writable character channel.
+    # ```ballerina
+    # io:Error? result = writableCharChannel.writeLine("Content");
+    # ```
+    # 
+    function writeLine(string content) returns Error|();
+
+    # Writes the provided JSON content to the writable character channel.
+    # ```ballerina
+    # io:Error? err = writableCharChannel.writeJson(inputJson, 0);
+    # ```
+    # 
+    function writeJson(json content) returns Error|();
+
+    # Writes the provided XML content to the writable character channel.
+    # ```ballerina
+    # io:Error? err = writableCharChannel.writeXml(inputXml, 0);
+    # ```
+    # 
+    function writeXml(xml content, XmlDoctype|() xmlDoctype = ()) returns Error|();
+
+    # Writes a key-value pair map (`map<string>`) to a property file.
+    # ```ballerina
+    # io:Error? err = writableCharChannel.writeProperties(properties);
+    # ```
+    function writeProperties(map<string> properties, string comment) returns Error|();
+
+    # Closes the character channel.
+    # After a channel is closed, any further writing operations will cause an error.
+    # ```ballerina
+    # io:Error err = writableCharChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a writable text record channel.
+class WritableTextRecordChannel {
+    function init(WritableCharacterChannel characterChannel, string fs = "", string rs = "", string fmt = "default") returns ();
+
+    # Writes records to a given output resource.
+    # ```ballerina
+    # io:Error? err = writableChannel.write(records);
+    # ```
+    # 
+    function write(string[] textRecord) returns Error|();
+
+    # Closes the record channel.
+    # After a channel is closed, any further writing operations will cause an error.
+    # ```ballerina
+    # io:Error? err = writableChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a writable CSV channel.
+# 
+class WritableCSVChannel {
+    function init(WritableCharacterChannel characterChannel, Separator fs = ",") returns ();
+
+    # Writes the record to a given CSV file.
+    # ```ballerina
+    # io:Error err = csvChannel.write(record);
+    # ```
+    # 
+    function write(string[] csvRecord) returns Error|();
+
+    # Closes the writable CSV channel.
+    # After a channel is closed, any further writing operations will cause an error.
+    # ```ballerina
+    # io:Error? err = csvChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
 # Specifies the format used to represent CSV data.
 # 
 # DEFAULT - The default value is the format specified by the CSVChannel. Precedence will be given to the field
@@ -159,21 +459,29 @@
 # COLON - Delimited text records will be separated using a colon(:)
 type Separator ","|"	"|":"|string;
 
-// Unknown type: Error
+# Represents IO module related errors.
+type Error error;
 
-// Unknown type: ConnectionTimedOutError
+# This will return when connection timed out happen when try to connect to a remote host.
+type ConnectionTimedOutError error;
 
-// Unknown type: GenericError
+# Represents generic IO error. The detail record contains the information related to the error.
+type GenericError error;
 
-// Unknown type: AccessDeniedError
+# This will get returned due to file permission issues.
+type AccessDeniedError error;
 
-// Unknown type: FileNotFoundError
+# This will get returned if the file is not available in the given file path.
+type FileNotFoundError error;
 
-// Unknown type: TypeMismatchError
+# This will get returned when there is an mismatch of given type and the expected type.
+type TypeMismatchError error;
 
-// Unknown type: EofError
+# This will get returned if read operations are performed on a channel after it closed.
+type EofError error;
 
-// Unknown type: ConfigurationError
+# This will get returned if there is an invalid configuration.
+type ConfigurationError error;
 
 # Represents a file opening options for writing.
 # 
@@ -219,7 +527,7 @@
 # 1. any typed value
 # 2. errors
 # 3. `io:PrintableRawTemplate` - an raw templated value
-type Printable any|error|ballerina/io:1.8.1:PrintableRawTemplate;
+type Printable any|error|PrintableRawTemplate;
 
 # Defines the output streaming types.
 # 1. `stdout` - standard output stream
@@ -233,20 +541,235 @@
 # LITTLE_ENDIAN - specifies the byte order to be the least significant byte first.
 type ByteOrder "BE"|"LE";
 
-// Unknown type: BlockStream
+# Initializes a stream of `Block` objects.
+# 
+class BlockStream {
+    function init(ReadableByteChannel readableByteChannel, int blockSize) returns ();
 
-// Unknown type: CSVStream
+    # Reads the next block of the stream.
+    # 
+    function next() returns record {|Block value;|}|Error|();
 
-// Unknown type: LineStream
+    # Closes the stream manually.
+    # If not invoked, the stream closes automatically upon reaching end-of-stream.
+    # 
+    function close() returns Error|();
+}
 
-// Unknown type: ReadableDataChannel
+# Initializes a stream of CSV records.
+# 
+class CSVStream {
+    function init(ReadableTextRecordChannel readableTextRecordChannel) returns ();
 
-// Unknown type: StringReader
+    # Reads the next CSV record of the stream.
+    # 
+    function next() returns record {|string[] value;|}|Error|();
 
-// Unknown type: CsvIterator
+    # Closes the stream manually.
+    # If not invoked, the stream closes automatically upon reaching end-of-stream.
+    # 
+    function close() returns Error|();
+}
 
-// Unknown type: WritableDataChannel
+# Initializes A stream of strings(lines).
+# 
+class LineStream {
+    function init(ReadableCharacterChannel readableCharacterChannel) returns ();
 
+    # Reads the next line of the stream.
+    # 
+    function next() returns record {|string value;|}|Error|();
+
+    # Closes the stream manually.
+    # If not invoked, the stream closes automatically upon reaching end-of-stream.
+    # 
+    function close() returns Error|();
+}
+
+# Initializes a readable data channel.
+# 
+class ReadableDataChannel {
+    function init(ReadableByteChannel byteChannel, ByteOrder bOrder = "BE") returns ();
+
+    # Reads a 16 bit integer.
+    # ```ballerina
+    # int|io:Error result = dataChannel.readInt16();
+    # ```
+    # 
+    function readInt16() returns int|Error;
+
+    # Reads a 32 bit integer.
+    # ```ballerina
+    # int|io:Error result = dataChannel.readInt32();
+    # ```
+    # 
+    function readInt32() returns int|Error;
+
+    # Reads a 64 bit integer.
+    # ```ballerina
+    # int|io:Error result = dataChannel.readInt64();
+    # ```
+    # 
+    function readInt64() returns int|Error;
+
+    # Reads a 32 bit float.
+    # ```ballerina
+    # float|io:Error result = dataChannel.readFloat32();
+    # ```
+    # 
+    function readFloat32() returns float|Error;
+
+    # Reads a 64 bit float.
+    # ```ballerina
+    # float|io:Error result = dataChannel.readFloat64();
+    # ```
+    # 
+    function readFloat64() returns float|Error;
+
+    # Reads a byte and convert its value to boolean.
+    # ```ballerina
+    # boolean|io:Error result = dataChannel.readBool();
+    # ```
+    # 
+    function readBool() returns boolean|Error;
+
+    # Reads the string value represented through the provided number of bytes.
+    # ```ballerina
+    # string|io:Error string = dataChannel.readString(10, "UTF-8");
+    # ```
+    # 
+    function readString(int nBytes, string encoding) returns string|Error;
+
+    # Reads a variable length integer.
+    # ```ballerina
+    # int|io:Error result = dataChannel.readVarInt();
+    # ```
+    # 
+    function readVarInt() returns int|Error;
+
+    # Closes the data channel.
+    # After a channel is closed, any further reading operations will cause an error.
+    # ```ballerina
+    # io:Error? err = dataChannel.close();
+    # ```
+    function close() returns Error|();
+}
+
+# Constructs a channel to read string.
+# 
+class StringReader {
+    function init(string content, string encoding = "UTF-8") returns ();
+
+    # Reads string as JSON using the reader.
+    # ```ballerina
+    # io:StringReader reader = new("{\"name\": \"Alice\"}");
+    # json|io:Error? person = reader.readJson();
+    # ```
+    # 
+    function readJson() returns json|Error;
+
+    # Reads a string as XML using the reader.
+    # ```ballerina
+    # io:StringReader reader = new("<Person><Name>Alice</Name></Person>");
+    # xml|io:Error? person = reader.readXml();
+    # ```
+    # 
+    function readXml() returns xml|Error|();
+
+    # Reads the characters from the given string.
+    # ```ballerina
+    # io:StringReader reader = new("Some text");
+    # string|io:Error? person = reader.readChar(4);
+    # ```
+    # 
+    function readChar(int nCharacters) returns string|Error|();
+
+    # Closes the string reader.
+    # ```ballerina
+    # io:Error? err = reader.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
+# The iterator for the stream returned in `readFileCsvAsStream` function.
+class CsvIterator {
+
+    function next() returns record {|anydata value;|}|error?;
+
+    function close() returns Error|();
+}
+
+# Initializes a writable data channel.
+# 
+class WritableDataChannel {
+    function init(WritableByteChannel byteChannel, ByteOrder bOrder = "BE") returns ();
+
+    # Writes a 16 bit integer value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeInt16(length);
+    # ```
+    # 
+    function writeInt16(int value) returns Error|();
+
+    # Writes a 32 bit integer value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeInt32(length);
+    # ```
+    # 
+    function writeInt32(int value) returns Error|();
+
+    # Writes a 64 bit integer value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeInt64(length);
+    # ```
+    # 
+    function writeInt64(int value) returns Error|();
+
+    # Writes a 32 bit float value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeFloat32(3.12);
+    # ```
+    # 
+    function writeFloat32(float value) returns Error|();
+
+    # Writes a 64 bit float value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeFloat64(3.12);
+    # ```
+    # 
+    function writeFloat64(float value) returns Error|();
+
+    # Writes a boolean value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeInt64(length);
+    # ```
+    # 
+    function writeBool(boolean value) returns Error|();
+
+    # Writes a string value to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeString(record);
+    # ```
+    # 
+    function writeString(string value, string encoding) returns Error|();
+
+    # Writes a variable-length integer to the writable data channel.
+    # ```ballerina
+    # io:Error? err = dataChannel.writeVarInt(length);
+    # ```
+    # 
+    function writeVarInt(int value) returns Error|();
+
+    # Closes the data channel.
+    # After a channel is closed, any further writing operations will cause an error.
+    # ```ballerina
+    # io:Error? err = dataChannel.close();
+    # ```
+    # 
+    function close() returns Error|();
+}
+
 // --- Functions ---
 
 # Reads the entire file content as a byte array.
`````

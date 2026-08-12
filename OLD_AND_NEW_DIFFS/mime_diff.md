# mime — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `mime` |
| **Old file** | `mime/old/ballerina_mime.bal.txt` |
| **New file** | `mime/new/ballerina_mime.bal.txt` |
| **Old lines** | 210 |
| **New lines** | 490 |
| **Lines added** | 299 |
| **Lines removed** | 19 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 19 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (52)

- `class ContentDisposition`
- `class Entity`
- `class MediaType`
- `function addHeader`
- `function getBaseType`
- `function getBodyParts`
- `function getBodyPartsAsStream`
- `function getByteArray`
- `function getByteStream`
- `function getContentDisposition`
- `function getContentId`
- `function getContentLength`
- `function getContentType`
- `function getHeader`
- `function getHeaderNames`
- `function getHeaders`
- `function getJson`
- `function getText`
- `function getXml`
- `function hasHeader`
- `function removeAllHeaders`
- `function removeHeader`
- `function setBody`
- `function setBodyParts`
- `function setByteArray`
- `function setByteStream`
- `function setContentDisposition`
- `function setContentId`
- `function setContentLength`
- `function setContentType`
- `function setFileAsEntityBody`
- `function setHeader`
- `function setJson`
- `function setText`
- `function setXml`
- `function toString`
- `type DecodeError`
- `type EncodeError`
- `type Error`
- `type GenericMimeError`
- `type HeaderNotFoundError`
- `type HeaderUnavailableError`
- `type IdleTimeoutTriggeredError`
- `type InvalidContentLengthError`
- `type InvalidContentTypeError`
- `type InvalidHeaderOperationError`
- `type InvalidHeaderParamError`
- `type InvalidHeaderValueError`
- `type NoContentError`
- `type ParserError`
- `type SerializationError`
- `type SetHeaderError`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 121–164 | 121–444 | Types | +299 | −19 |

---

## Unified diff

`````diff
--- mime/old/ballerina_mime.bal.txt	2026-08-12 23:21:51
+++ mime/new/ballerina_mime.bal.txt	2026-08-12 23:23:51
@@ -121,44 +121,324 @@
 # Represents `content-disposition` header name.
 const string CONTENT_DISPOSITION = "content-disposition";
 
-// Unknown type: Error
+# Defines the common error type for the module.
+type Error error;
 
-// Unknown type: EncodeError
+# Represents an `EncodeError` with the message and the cause.
+type EncodeError error;
 
-// Unknown type: DecodeError
+# Represents a `DecodeError` with the message and the cause.
+type DecodeError error;
 
-// Unknown type: GenericMimeError
+# Represents a `GenericMimeError` with the message and the cause.
+type GenericMimeError error;
 
-// Unknown type: SetHeaderError
+# Represents a `SetHeaderError` with the message and the cause.
+type SetHeaderError error;
 
-// Unknown type: InvalidHeaderValueError
+# Represents a `InvalidHeaderValueError` error with the message and the cause.
+type InvalidHeaderValueError error;
 
-// Unknown type: InvalidHeaderParamError
+# Represents a `InvalidHeaderParamError` error with the message and the cause.
+type InvalidHeaderParamError error;
 
-// Unknown type: InvalidContentLengthError
+# Represents a `InvalidContentLengthError` error with the message and the cause.
+type InvalidContentLengthError error;
 
-// Unknown type: HeaderNotFoundError
+# Represents a `HeaderNotFoundError` error with the message and the cause.
+type HeaderNotFoundError error;
 
-// Unknown type: InvalidHeaderOperationError
+# Represents a `InvalidHeaderOperationError` error with the message and the cause.
+type InvalidHeaderOperationError error;
 
-// Unknown type: SerializationError
+# Represents a `SerializationError` error with the message and the cause.
+type SerializationError error;
 
-// Unknown type: ParserError
+# Represents a `ParserError` with the message and the cause.
+type ParserError error;
 
-// Unknown type: InvalidContentTypeError
+# Represents an `InvalidContentTypeError` with the message and the cause.
+type InvalidContentTypeError error;
 
-// Unknown type: HeaderUnavailableError
+# Represents a `HeaderUnavailableError` with the message and the cause.
+type HeaderUnavailableError error;
 
-// Unknown type: IdleTimeoutTriggeredError
+# Represents an `IdleTimeoutTriggeredError` with the message and the cause.
+type IdleTimeoutTriggeredError error;
 
-// Unknown type: NoContentError
+# Represents a `NoContentError` with the message and the cause.
+type NoContentError error;
 
-// Unknown type: Entity
+# Represents the headers and body of a message. This can be used to represent both the entity of a top level message
+# and an entity(body part) inside of a multipart entity.
+# 
+class Entity {
 
-// Unknown type: MediaType
+    # Sets the content-type to the entity.
+    # ```ballerina
+    # mime:InvalidContentTypeError? contentType = mimeEntity.setContentType("application/json");
+    # ```
+    # 
+    function setContentType(string mediaType) returns InvalidContentTypeError|();
 
-// Unknown type: ContentDisposition
+    # Gets the content type of the entity.
+    # ```ballerina
+    # string contentType = mimeEntity.getContentType();
+    # ```
+    # 
+    function getContentType() returns string;
+
+    # Sets the content ID of the entity.
+    # ```ballerina
+    # mimeEntity.setContentId("test-id");
+    # ```
+    # 
+    function setContentId(string contentId) returns ();
+
+    # Gets the content ID of the entity.
+    # ```ballerina
+    # string contentId = mimeEntity.getContentId();
+    # ```
+    # 
+    function getContentId() returns string;
+
+    # Sets the content length of the entity.
+    # ```ballerina
+    # mimeEntity.setContentLength(45555);
+    # ```
+    # 
+    function setContentLength(int contentLength) returns ();
+
+    # Gets the content length of the entity.
+    # ```ballerina
+    # int|error contentLength = mimeEntity.getContentLength();
+    # ```
+    # 
+    function getContentLength() returns int|error;
+
+    # Sets the content disposition of the entity.
+    # ```ballerina
+    # mimeEntity.setContentDisposition(contentDisposition);
+    # ```
+    # 
+    function setContentDisposition(ContentDisposition contentDisposition) returns ();
+
+    # Gets the content disposition of the entity.
+    # ```ballerina
+    # mime:ContentDisposition contentDisposition = mimeEntity.getContentDisposition();
+    # ```
+    # 
+    function getContentDisposition() returns ContentDisposition;
+
+    # Sets the body of the entity with the given content. Note that any string value is set as `text/plain`. To send a
+    # JSON-compatible string, set the content-type header to `application/json` or use the `setJsonPayload` method instead.
+    # ```ballerina
+    # mimeEntity.setBody("body string");
+    # ```
+    # 
+    function setBody(string|xml|json|byte[]|mime:Entity[]|stream<byte[], io:Error?> entityBody) returns ();
+
+    # Sets the entity body with a given file. This method overrides any existing `content-type` headers
+    # with the default content-type, which is `application/octet-stream`. This default value
+    # can be overridden by passing the content type as an optional parameter.
+    # ```ballerina
+    # mimeEntity.setFileAsEntityBody("<file path>");
+    # ```
+    # 
+    function setFileAsEntityBody(string filePath, string contentType = "") returns ();
+
+    # Sets the entity body with the given `json` content. This method overrides any existing `content-type` headers
+    # with the default content-type, which is `application/json`. This default value can be overridden
+    # by passing the content type as an optional parameter.
+    # ```ballerina
+    # mimeEntity.setJson({ "Hello": "World" });
+    # ```
+    # 
+    function setJson(json jsonContent, string contentType = "") returns ();
+
+    # Extracts the JSON body from the entity.
+    # ```ballerina
+    # json|mime:ParserError result = entity.getJson();
+    # ```
+    # 
+    function getJson() returns json|ParserError;
+
+    # Sets the entity body with the given XML content. This method overrides any existing content-type headers
+    # with the default content-type, which is `application/xml`. This default value can be overridden
+    # by passing the content-type as an optional parameter.
+    # ```ballerina
+    # mimeEntity.setXml(xml `<hello> world </hello>`);
+    # ```
+    # 
+    function setXml(xml xmlContent, string contentType = "") returns ();
+
+    # Extracts the `xml` body from the entity.
+    # ```ballerina
+    # xml|mime:ParserError result = entity.getXml();
+    # ```
+    # 
+    function getXml() returns xml|ParserError;
+
+    # Sets the entity body with the given text content. This method overrides any existing content-type headers
+    # with the default content-type, which is `text/plain`. This default value can be overridden
+    # by passing the content type as an optional parameter.
+    # ```ballerina
+    # mimeEntity.setText("Hello World");
+    # ```
+    # 
+    function setText(string textContent, string contentType = "") returns ();
 
+    # Extracts the text body from the entity. If the entity body is not text compatible, an error is returned.
+    # ```ballerina
+    # string|mime:ParserError result = entity.getText();
+    # ```
+    # 
+    function getText() returns string|ParserError;
+
+    # Sets the entity body with the given byte[] content. This method overrides any existing `content-type` headers
+    # with the default content-type, which is `application/octet-stream`. This default value
+    # can be overridden by passing the content type as an optional parameter.
+    # ```ballerina
+    # entity.setByteArray(content.toBytes());
+    # ```
+    # 
+    function setByteArray(byte[] blobContent, string contentType = "") returns ();
+
+    # Gets the entity body as a `byte[]` from a given entity. If the entity size is considerably large, consider
+    # using the `Entity.getByteStream()` method instead.
+    # ```ballerina
+    # byte[]|mime:ParserError result = entity.getByteArray();
+    # ```
+    # 
+    function getByteArray() returns byte[]|ParserError;
+
+    # Sets the entity body with the given byte stream content. This method overrides any existing content-type headers
+    # with the default content-type, which is `application/octet-stream`. This default value
+    # can be overridden by passing the content-type as an optional parameter.
+    # ```ballerina
+    # entity.setByteStream(byteStream);
+    # ```
+    # 
+    function setByteStream(stream<byte[], io:Error?> byteStream, string contentType = "") returns ();
+
+    # Gets the entity body as a stream of `byte[]` from a given entity.
+    # ```ballerina
+    # stream<byte[], io:Error?>|mime:ParserError str = entity.getByteStream();
+    # ```
+    # 
+    function getByteStream(int arraySize = 0) returns stream<byte[], io:Error?>|ParserError;
+
+    # Gets the body parts from a given entity.
+    # ```ballerina
+    # mime:Entity[]|mime:ParserError result = multipartEntity.getBodyParts();
+    # ```
+    # 
+    function getBodyParts() returns Entity[]|ParserError;
+
+    # Gets the body parts as a byte stream from a given entity.
+    # ```ballerina
+    # stream<byte[], io:Error?>|mime:ParserError str = multipartEntity.getBodyPartsAsStream();
+    # ```
+    # 
+    function getBodyPartsAsStream(int arraySize = 0) returns stream<byte[], io:Error?>|ParserError;
+
+    # Sets the body parts to the entity. This method overrides any existing `content-type` headers
+    # with the default `multipart/form-data` content-type. The default `multipart/form-data` value can be overridden
+    # by passing the content type as an optional parameter.
+    # ```ballerina
+    # multipartEntity.setBodyParts(bodyParts, contentType);
+    # ```
+    # 
+    function setBodyParts(Entity[] bodyParts, string contentType = "") returns ();
+
+    # Gets the header value associated with the given header name.
+    # ```ballerina
+    # string|mime:HeaderNotFoundError headerName = mimeEntity.getHeader(mime:CONTENT_LENGTH);
+    # ```
+    # 
+    function getHeader(string headerName) returns string|HeaderNotFoundError;
+
+    # Gets all the header values associated with the given header name.
+    # ```ballerina
+    # string[]|mime:HeaderNotFoundError headerNames = mimeEntity.getHeaders(mime:CONTENT_TYPE);
+    # ```
+    # 
+    function getHeaders(string headerName) returns string[]|HeaderNotFoundError;
+
+    # Gets all the header names.
+    # ```ballerina
+    # string[] headerNames = mimeEntity.getHeaderNames();
+    # ```
+    # 
+    function getHeaderNames() returns string[];
+
+    # Adds the given header value against the given header. Panic if an illegal header is passed.
+    # ```ballerina
+    # mimeEntity.addHeader("custom-header", "header-value");
+    # ```
+    # 
+    function addHeader(string headerName, string headerValue) returns ();
+
+    # Sets the given header value against the existing header. If a header already exists, its value is replaced
+    # with the given header value. Panic if an illegal header is passed.
+    # ```ballerina
+    # mimeEntity.setHeader("custom-header", "header-value");
+    # ```
+    # 
+    function setHeader(string headerName, string headerValue) returns ();
+
+    # Removes the given header from the entity.
+    # ```ballerina
+    # mimeEntity.removeHeader("custom-header");
+    # ```
+    # 
+    function removeHeader(string headerName) returns ();
+
+    # Removes all headers associated with the entity.
+    # ```ballerina
+    # mimeEntity.removeAllHeaders();
+    # ```
+    function removeAllHeaders() returns ();
+
+    # Checks whether the requested header key exists in the header map.
+    # ```ballerina
+    # boolean res = mimeEntity.hasHeader("custom-header");
+    # ```
+    # 
+    function hasHeader(string headerName) returns boolean;
+}
+
+# Describes the nature of the data in the body of a MIME entity.
+# 
+class MediaType {
+
+    # Gets the “primaryType/subtype+suffix” combination in a `string` format.
+    # ```ballerina
+    # string baseType = mediaType.getBaseType();
+    # ```
+    # 
+    function getBaseType() returns string;
+
+    # Converts the media type to a `string`, which is suitable to be used as the value of a corresponding HTTP header.
+    # ```ballerina
+    # string mediaTypeString = mediaType.toString();
+    # ```
+    # 
+    function toString() returns string;
+}
+
+# Represents values in `Content-Disposition` header.
+# 
+class ContentDisposition {
+
+    # Converts the `ContentDisposition` type to a string suitable to use as the value of a corresponding MIME header.
+    # ```ballerina
+    # string contDisposition = contentDisposition.toString();
+    # ```
+    # 
+    function toString() returns string;
+}
+
 // --- Functions ---
 
 # Encodes a given input with MIME specific Base64 encoding scheme.
`````

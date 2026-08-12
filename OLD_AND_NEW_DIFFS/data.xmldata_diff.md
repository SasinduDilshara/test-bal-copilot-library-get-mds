# data.xmldata — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `data.xmldata` |
| **Old file** | `data.xmldata/old/ballerina_data.xmldata.bal.txt` |
| **New file** | `data.xmldata/new/ballerina_data.xmldata.bal.txt` |
| **Old lines** | 626 |
| **New lines** | 665 |
| **Lines added** | 48 |
| **Lines removed** | 9 |
| **Hunks** | 3 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 8 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (8)

- `annotation Choice`
- `annotation Element`
- `annotation Name`
- `annotation Namespace`
- `annotation Sequence`
- `annotation SequenceOrder`
- `annotation on`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 462–491 | 462–491 | Types | +8 | −8 |
| 2 | 533–539 | 533–541 | Types | +3 | −1 |
| 3 | 624–626 | 626–665 | Functions | +37 | −0 |

---

## Unified diff

`````diff
--- data.xmldata/old/ballerina_data.xmldata.bal.txt	2026-08-12 23:21:51
+++ data.xmldata/new/ballerina_data.xmldata.bal.txt	2026-08-12 23:23:51
@@ -462,30 +462,30 @@
 
 type ParticleOccurrence record {
     # Specifies the minimum number of occurrences.
-    ballerina/lang.int:0.0.0:Unsigned32 minOccurs?;
+    int:Unsigned32 minOccurs?;
     # Specifies the maximum number of occurrences.
-    ballerina/lang.int:0.0.0:Unsigned32 maxOccurs?;
+    int:Unsigned32 maxOccurs?;
 };
 
 # Defines the configuration for an XML element in the XML schema (XSD).
 
 type ElementConfig record {
-    ballerina/lang.int:0.0.0:Unsigned32 minOccurs?;
-    ballerina/lang.int:0.0.0:Unsigned32 maxOccurs?;
+    int:Unsigned32 minOccurs?;
+    int:Unsigned32 maxOccurs?;
 };
 
 # Defines the configuration for an XML sequence in the XML schema (XSD).
 
 type SequenceConfig record {
-    ballerina/lang.int:0.0.0:Unsigned32 minOccurs?;
-    ballerina/lang.int:0.0.0:Unsigned32 maxOccurs?;
+    int:Unsigned32 minOccurs?;
+    int:Unsigned32 maxOccurs?;
 };
 
 # Defines the configuration for an XML choice in the XML schema (XSD).
 
 type ChoiceConfig record {
-    ballerina/lang.int:0.0.0:Unsigned32 minOccurs?;
-    ballerina/lang.int:0.0.0:Unsigned32 maxOccurs?;
+    int:Unsigned32 minOccurs?;
+    int:Unsigned32 maxOccurs?;
 };
 
 # Defines the configuration for the sequence order in the XML schema (XSD).
@@ -533,7 +533,9 @@
     string textFieldName?;
 };
 
-// Unknown type: Error
+# Represents the error type of the ballerina/data.xmldata module. This error type represents any error that can occur
+# during the execution of xmldata APIs.
+type Error error;
 
 # Provides configurations for converting JSON to XML.
 
@@ -624,3 +626,40 @@
 # + return - On success, returns the projected value, if either query is invalid or result of query can't be projected
 to the specified type, returns an `Error` value
 function transform(xml xmlValue, XPathRawTemplate query, anydata td = anydata) returns td|Error;
+
+// --- Annotations ---
+
+# Annotation to define schema rules for an XML element in Ballerina.
+public annotation ElementConfig Element on record field;
+
+# Annotation to define schema rules for an XML sequence in Ballerina.
+public annotation SequenceConfig Sequence on record field;
+
+# Annotation to define schema rules for an XML choice in Ballerina.
+public annotation ChoiceConfig Choice on record field;
+
+# Annotation to define schema rules for the sequence order in Ballerina.
+public annotation SequenceOrderConfig SequenceOrder on record field;
+
+# The annotation is used to specify the new name of the existing record name or field name according to the XML format.
+# When using `parseString`, `parseBytes`, `parseStream`, `parseAsType`, this annotation can be used to 
+# validate the name of the XML element with the record field or type.
+# When using `toXml`, this annotation can be used to override the name of field or type.
+public annotation NameConfig Name on type, record field;
+
+# The annotation is used to specify the namespace's prefix and URI of the XML element.
+# When using `parseString`, `parseBytes`, `parseStream`, `parseAsType`, this annotation can be used to 
+# validate the namespace of the XML element with the record field or type.
+# When using `toXml`, this annotation can be used to add the namespace to the XML element.
+public annotation NamespaceConfig Namespace on type, record field;
+
+# The annotation is used to denote the field that is considered an attribute.
+# When using `parseString`, `parseBytes`, `parseStream`, `parseAsType`, this annotation can be used to
+# indicate the record field as an attribute.
+# When using `toXml`, this annotation can be used to add the attribute to the XML element.
+public annotation Attribute on record field;
+
+# The annotation is used to denote a field that can contain xsd:any type value.
+# When using `toXml`, this annotation will use the actual type name of the value as the XML element name
+# instead of the field name.
+public annotation Any on record field;
`````

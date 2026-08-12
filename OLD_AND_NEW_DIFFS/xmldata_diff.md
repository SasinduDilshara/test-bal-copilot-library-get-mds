# xmldata — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `xmldata` |
| **Old file** | `xmldata/old/ballerina_xmldata.bal.txt` |
| **New file** | `xmldata/new/ballerina_xmldata.bal.txt` |
| **Old lines** | 125 |
| **New lines** | 144 |
| **Lines added** | 20 |
| **Lines removed** | 1 |
| **Hunks** | 2 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 1 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 5 |

### Declarations added (4)

- `annotation Name`
- `annotation Namespace`
- `annotation on`
- `type Error`

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 16–22 | 16–24 | END README | +3 | −1 |
| 2 | 123–125 | 125–144 | Functions | +17 | −0 |

---

## Unified diff

`````diff
--- xmldata/old/ballerina_xmldata.bal.txt	2026-08-12 23:21:51
+++ xmldata/new/ballerina_xmldata.bal.txt	2026-08-12 23:23:51
@@ -16,7 +16,9 @@
 
 // --- Types ---
 
-// Unknown type: Error
+# Represents the error type of the ballerina/xmldata module. This error type represents any error that can occur
+# during the execution of xmldata APIs.
+type Error error;
 
 # Defines the name of the XML element.
 # 
@@ -123,3 +125,20 @@
 # + return - The given target type representation of the given XML on success,
 else returns an `xmldata:Error`
 function fromXml(xml xmlValue, map<anydata> returnType = map<anydata>) returns returnType|Error;
+
+// --- Annotations ---
+
+# The annotation is used to specify the new name of the existing record name or field name according to the XML format.
+# In the XML-record conversion, this annotation can be used to override the default XML element name using the
+# `xmldata:toXML` API and validate the overridden XML element name with record field using the `xmldata:fromXml` API.
+public annotation NameConfig Name on type, record field;
+
+# The annotation is used to specify the namespace's prefix and URI of the XML element.
+# In the XML-record conversion, this annotation can be used to add XML namespace using the `xmldata:toXML` API and
+# validate the the XML namespace with record in the `xmldata:fromXml` API.
+public annotation NamespaceConfig Namespace on type;
+
+# The annotation is used to denote the field that is considered an attribute.
+# In the XML-record conversion, this annotation can be used to add XML attribute using the `xmldata:toXML` API and
+# validate the XML attribute with record fields in the `xmldata:fromXml` API.
+public annotation Attribute on record field;
`````

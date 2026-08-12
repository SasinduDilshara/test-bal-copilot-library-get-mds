# hubspot.crm.extensions.videoconferencing — `old` vs `new` render diff

| | |
|---|---|
| **Library folder** | `hubspot.crm.extensions.videoconferencing` |
| **Old file** | `hubspot.crm.extensions.videoconferencing/old/ballerinax_hubspot.crm.extensions.videoconferencing.bal.txt` |
| **New file** | `hubspot.crm.extensions.videoconferencing/new/ballerinax_hubspot.crm.extensions.videoconferencing.bal.txt` |
| **Old lines** | 243 |
| **New lines** | 245 |
| **Lines added** | 2 |
| **Lines removed** | 0 |
| **Hunks** | 1 |

---

## Change overview

> Every figure below is computed directly from the diff and the two files — no interpretation.

### Signals

| Signal | old | new |
|---|---|---|
| `// Unknown type:` placeholders | 0 | 0 |
| Version/module-qualified type refs (e.g. `mod:1.2.3:Type`) | 0 | 0 |
| `// --- section ---` markers | 4 | 4 |

### Declarations added (0)

_none_

### Declarations removed (0)

_none_

### Hunks

| # | Old lines | New lines | Section | Added | Removed |
|---|---|---|---|---|---|
| 1 | 178–188 | 178–190 | Types | +2 | −0 |

---

## Unified diff

`````diff
--- hubspot.crm.extensions.videoconferencing/old/ballerinax_hubspot.crm.extensions.videoconferencing.bal.txt	2026-08-12 12:57:30
+++ hubspot.crm.extensions.videoconferencing/new/ballerinax_hubspot.crm.extensions.videoconferencing.bal.txt	2026-08-12 13:19:19
@@ -178,11 +178,13 @@
 
 type ApiKeysConfig record {
     # HubSpot developer API key
+    @display {label: "", kind: "password"}
     string hapikey;
 };
 
 # Provides a set of configurations for controlling the behaviours when communicating with a remote HTTP endpoint.
 
+@display {label: "Connection Config"}
 type ConnectionConfig record {
     # The HTTP version understood by the client
     http:HttpVersion httpVersion?; // Special Agent Note: HttpVersion FROM ballerina/http package
`````

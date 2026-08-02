# Copilot library renders — WSO2 Integrator 5.0.0 connector set

Generated from `ballerina-platform/ballerina-vscode` @ `main` (commit `145fa81d40d25b64e5c6fbea324e84d8559b1cce`).
Library content resolved from local balas (Ballerina 2201.13.4, Swan Lake Update 13).

## Layout

```
<library_name>/
├── old/   <org>_<name>.json      stage-1 JSON  (CopilotLibraryManager → ModelToJsonConverter)
│          <org>_<name>.bal.txt   stage-2 render (toSyntaxString)
└── new/   <org>_<name>.json      empty placeholder (0 bytes)
           <org>_<name>.bal.txt   empty placeholder (0 bytes)
```

Directory name is the org-stripped `<library_name>`; file names keep the `<org>_<name>` prefix.

## Totals

| | count |
|---|---|
| Libraries requested (unique) | 144 |
| Directories created | 144 |
| `old/` JSON produced | 144 |
| `old/` renders produced | **143** |
| `new/` empty placeholders | 288 (all exactly 0 bytes) |
| Stage-1 resolution failures | 0 |
| Total JSON | 45.7 MB |
| Total rendered | 13 MB |

Verified by 5 independent agents (29/29/29/29/28) plus a separate whole-tree check.
Every `old/*.json` parses and its top-level `name` matches its `org/name`; every render carries
the matching `// Library:` and `import` lines; no unexpected files in any directory.

## Known gaps

**1. `ballerina/mcp` has no render — upstream renderer crash.**
`old/ballerina_mcp.json` is present and valid (120,497 B); `old/ballerina_mcp.bal.txt` is absent.
`renderFixedService` (`to-syntax-string.ts:440`) iterates `service.methods` unguarded, and mcp's single
fixed service carries only `type,name,listener` — `methods` is `undefined`:

```
TypeError: service.methods is not iterable
```

A `service.methods ?? []` guard would fix it. Not applied here — the renderer was left untouched so
the output reflects real `main` behaviour.

**2. `ballerinax/candid` renders empty despite having an API.**
Extraction uses `pkg.getDefaultModule()` only. candid's default module exports nothing; its 140 public
symbols live in 4 submodules (`candid.essentials`, `candid.premier`, `candid.charitycheckpdf`,
`candid.mock`), so none are captured.

Four other libraries render with only a README — `amp`, `idetraceprovider`, `moesif`, `newrelic` —
but those genuinely export 0 public symbols, so an empty render is correct for them.

**3. 2,354 `// Unknown type:` lines across 86 of the 143 renders.**
`renderTypeDef` (`to-syntax-string.ts:212`) handles only Record, Enum, Union, Constant, Class. Three
kinds present in the JSON fall through to a bare comment with no members: `Error`, untagged object
types (no `type` field), and `Other`.

Worst affected: stripe 610, discord 421, sap.s4hana.api_sales_order_srv 167, http 155, github 136,
postgresql 126. 57 libraries have zero.

## Not included

`pgvector` (tracker #26) is excluded — the repo has no `Ballerina.toml` and no source, so there is no
package to resolve. 145 tracker rows minus pgvector and the duplicate Google Calendar entry
(both rows resolve to the same `ballerinax/googleapis.gcalendar`) gives the 144 unique libraries above.

## Reproducing

Stage 1 needs the target balas inside the *test distribution*, not just `~/.ballerina`. The test
resolves against `build/extracted-distribution/jballerina-tools-<ver>/repo/bala`, populated only from
`configurations.ballerinaStdLibs`. Packages absent from it fail in ~20 ms regardless of what `bal pull`
has cached. Copying each bala into that repo before the run is what makes arbitrary libraries resolve.

// Stage 2: stage-1 JSON -> rendered .bal.txt, written into <root>/<name>/<side>/.
//
// Usage:
//   ts-node render.ts <src> <jsonDir> <root> <side> <reportPath>
//
// The renderer is imported from the SOURCE CHECKOUT being rendered, so the output always reflects
// that source's behaviour. toSyntaxString takes an ARRAY, not a single library.
import * as fs from "fs";
import * as path from "path";

const [, , SRC, IN_DIR, ROOT, SIDE, REPORT] = process.argv;
if (!SRC || !IN_DIR || !ROOT || !SIDE || !REPORT) {
    console.error("usage: ts-node render.ts <src> <jsonDir> <root> <side> <reportPath>");
    process.exit(2);
}

const rendererPath = path.join(
    SRC, "packages/ballerina-extension/src/features/ai/utils/libs/to-syntax-string");
// eslint-disable-next-line @typescript-eslint/no-var-requires
const { toSyntaxString } = require(rendererPath);

const lines: string[] = [];
let ok = 0;
let failed = 0;

for (const f of fs.readdirSync(IN_DIR).filter((x) => x.endsWith(".json")).sort()) {
    const base = f.replace(/\.json$/, "");              // <org>_<name>
    const dir = base.substring(base.indexOf("_") + 1);   // org-stripped directory name
    const outDir = path.join(ROOT, dir, SIDE);
    if (!fs.existsSync(outDir)) {
        lines.push(`NODIR|${base}|${outDir}`);
        failed++;
        continue;
    }
    const raw = fs.readFileSync(path.join(IN_DIR, f), "utf-8");
    fs.writeFileSync(path.join(outDir, f), raw, "utf-8");
    try {
        const json = JSON.parse(raw);
        const rendered = toSyntaxString([json]);
        fs.writeFileSync(path.join(outDir, base + ".bal.txt"), rendered, "utf-8");
        lines.push(`OK|${base}|${rendered.split("\n").length}`);
        ok++;
    } catch (e: any) {
        lines.push(`RENDER_FAIL|${base}|${e && e.message ? e.message : String(e)}`);
        failed++;
    }
}

lines.push(`TOTAL ok=${ok} failed=${failed}`);
fs.writeFileSync(REPORT, lines.join("\n") + "\n", "utf-8");
console.log(`rendered ok=${ok} failed=${failed}  (report: ${REPORT})`);
if (failed > 0) {
    console.error("NOTE: failures above are real - report them by name, do not summarise away.");
}

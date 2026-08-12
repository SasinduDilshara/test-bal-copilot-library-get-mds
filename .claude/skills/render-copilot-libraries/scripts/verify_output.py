#!/usr/bin/env python3
"""Final gate: verify the rendered side, and confirm the other side was not disturbed."""
import argparse
import json
import os
import re
import sys


def load_pinned(path):
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line:
            lib, ver = line.rsplit(":", 1)
            out.append((lib, ver))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--pinned", required=True)
    ap.add_argument("--side", required=True, choices=["old", "new"])
    ap.add_argument("--versions-report", help="resolved-versions-<side>.txt, to assert every row is PIN_OK")
    args = ap.parse_args()

    libs = load_pinned(args.pinned)
    other = "new" if args.side == "old" else "old"
    problems, empty, unknown_lines, unknown_libs = [], [], 0, 0
    total_json = total_render = 0

    for lib, _ in libs:
        org, name = lib.split("/")
        base = "%s_%s" % (org, name)
        jp = os.path.join(args.root, name, args.side, base + ".json")
        bp = os.path.join(args.root, name, args.side, base + ".bal.txt")

        for p, kind in ((jp, "json"), (bp, "render")):
            if not os.path.exists(p):
                problems.append(("MISSING", lib, kind))
            elif os.path.getsize(p) == 0:
                empty.append((lib, kind))

        if os.path.exists(jp) and os.path.getsize(jp) > 0:
            total_json += os.path.getsize(jp)
            try:
                if json.load(open(jp, encoding="utf-8")).get("name") != lib:
                    problems.append(("JSON_NAME_MISMATCH", lib, ""))
            except Exception as exc:
                problems.append(("JSON_PARSE", lib, str(exc)[:60]))

        if os.path.exists(bp) and os.path.getsize(bp) > 0:
            total_render += os.path.getsize(bp)
            text = open(bp, encoding="utf-8").read()
            if ("// Library: %s" % lib) not in text:
                problems.append(("HEADER_MISMATCH", lib, ""))
            n = len(re.findall(r"^// Unknown type:", text, re.M))
            if n:
                unknown_lines += n
                unknown_libs += 1

        # the other side must keep whatever it had; flag only structural absence
        for ext in (".json", ".bal.txt"):
            op = os.path.join(args.root, name, other, base + ext)
            if not os.path.exists(op):
                problems.append(("OTHER_SIDE_MISSING", lib, other + ext))

    print("=== VERIFY %s/ (%d libraries) ===" % (args.side, len(libs)))
    print("  JSON    : %.1f MB" % (total_json / 1e6))
    print("  renders : %.1f MB" % (total_render / 1e6))
    print("  '// Unknown type:' : %d lines across %d libraries" % (unknown_lines, unknown_libs))
    print("  empty files        : %d" % len(empty))
    for lib, kind in empty:
        print("     %-52s %s" % (lib, kind))
    print("  problems           : %d" % len(problems))
    for kind, lib, extra in problems[:20]:
        print("     %-22s %-45s %s" % (kind, lib, extra))

    pin_bad = 0
    if args.versions_report and os.path.exists(args.versions_report):
        rows = [l.strip().split("|") for l in open(args.versions_report, encoding="utf-8") if l.strip()]
        pin_bad = [r for r in rows if len(r) > 3 and r[3] != "PIN_OK"]
        print("  version rows       : %d, PIN_OK %d, mismatched %d"
              % (len(rows), len(rows) - len(pin_bad), len(pin_bad)))
        for r in pin_bad[:20]:
            print("     PIN_MISMATCH %-40s pinned=%s resolved=%s" % (r[0], r[1], r[2]))
        pin_bad = len(pin_bad)

    if problems or pin_bad:
        print("\nVERIFY FAILED")
        sys.exit(1)
    if empty:
        print("\nVERIFY PASSED WITH EMPTY FILES - confirm each is a genuine upstream behaviour "
              "(renderer crash vs library exporting nothing) and report it.")
        sys.exit(0)
    print("\nVERIFY PASSED")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the pinned-version list straight from the CLAUDE.md table.

Versions are never invented here: a requested library that is absent from the table is a hard
error, because guessing a version silently produces a wrong-but-plausible render.
"""
import argparse
import os
import re
import sys


def parse_table(root):
    path = os.path.join(root, "CLAUDE.md")
    text = open(path, encoding="utf-8").read()
    blocks = [b for b in re.findall(r"```(.*?)```", text, re.S) if "Pinned Version" in b]
    if not blocks:
        sys.exit("ERROR: no fenced block containing 'Pinned Version' found in %s" % path)
    rows = []
    for line in blocks[-1].strip().splitlines():
        line = line.strip()
        if not line or line.startswith("Module"):
            continue
        parts = re.split(r"\s+", line)
        if len(parts) != 2:
            sys.exit("ERROR: cannot parse table row: %r" % line)
        rows.append((parts[0], parts[1]))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="repo root containing CLAUDE.md")
    ap.add_argument("--out", required=True, help="path to write <org>/<name>:<version> lines")
    ap.add_argument("--only", nargs="*", default=None,
                    help="optional subset of 'org/name' to render; default is every library")
    args = ap.parse_args()

    rows = parse_table(args.root)
    table = dict(rows)
    if len(table) != len(rows):
        dupes = [n for n, _ in rows if list(dict(rows)).count(n) > 1]
        sys.exit("ERROR: duplicate libraries in table: %s" % dupes)

    if args.only:
        missing = [n for n in args.only if n not in table]
        if missing:
            sys.exit("ERROR: not in the CLAUDE.md table (refusing to guess a version): %s"
                     % ", ".join(missing))
        selected = [(n, table[n]) for n in args.only]
    else:
        selected = rows

    with open(args.out, "w", encoding="utf-8") as fh:
        for name, version in selected:
            fh.write("%s:%s\n" % (name, version))

    print("wrote %d libraries to %s (table has %d)" % (len(selected), args.out, len(rows)))


if __name__ == "__main__":
    main()

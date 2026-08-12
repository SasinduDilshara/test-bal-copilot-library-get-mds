#!/usr/bin/env python3
"""Gate before stage 1: every pinned version must be resolvable from the build-owned home.

Under FORCE_OFFLINE the resolver only sees this directory. When the source lacks the
version-aware overload, "latest" means the HIGHEST version here — so a pin that is present but
not highest still resolves to the wrong version. That case is reported as a failure unless
--exact-resolution says the probe asks for the version explicitly.
"""
import argparse
import os
import re
import sys

REL_HOME = ("packages/ballerina-language-server/build/ballerina_dependencies/home/"
            "repositories/central.ballerina.io/bala")


def vkey(v):
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-(.*))?$", v)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4) or "~") if m else (0, 0, 0, "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--pinned", required=True)
    ap.add_argument("--exact-resolution", action="store_true",
                    help="probe requests versions explicitly, so 'pin not highest' is harmless")
    args = ap.parse_args()

    bala = os.path.join(args.src, REL_HOME)
    if not os.path.isdir(bala):
        sys.exit("ERROR: build-owned home not found: %s" % bala)

    missing, not_max, ok = [], [], 0
    for line in open(args.pinned, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        lib, pin = line.rsplit(":", 1)
        org, name = lib.split("/")
        d = os.path.join(bala, org, name)
        versions = sorted([x for x in os.listdir(d) if re.match(r"^\d", x)], key=vkey) \
            if os.path.isdir(d) else []
        if pin not in versions:
            missing.append((lib, pin, versions))
        else:
            ok += 1
            if versions[-1] != pin:
                not_max.append((lib, pin, versions[-1]))

    print("BUILD-OWNED HOME AUDIT")
    print("  pinned version present : %d" % ok)
    print("  pinned version MISSING : %d" % len(missing))
    for lib, pin, have in missing:
        print("     %-52s pin=%-10s have=%s" % (lib, pin, have or "none"))

    if args.exact_resolution:
        print("  pin not highest        : %d (harmless - probe resolves by exact version)" % len(not_max))
        fatal = len(missing)
    else:
        print("  pin NOT HIGHEST        : %d (FATAL - a newer version would resolve instead)" % len(not_max))
        for lib, pin, top in not_max:
            print("     %-52s pin=%-10s would resolve=%s" % (lib, pin, top))
        fatal = len(missing) + len(not_max)

    if fatal:
        print("\nAUDIT FAILED - do not run stage 1. Seed the missing versions, or delete the "
              "newer version directories from the home.")
        sys.exit(1)
    print("\nAUDIT PASSED - every pinned version will resolve exactly.")


if __name__ == "__main__":
    main()

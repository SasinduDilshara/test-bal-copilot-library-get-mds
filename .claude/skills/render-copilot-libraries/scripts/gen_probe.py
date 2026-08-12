#!/usr/bin/env python3
"""Generate the stage-1 probe into the source tree and register it in testng.xml.

Picks the strongest resolution the source supports:
  * version-aware overload present  -> resolve by EXACT version
  * absent (e.g. main)              -> version-less call; the cache seeding is then what pins it
"""
import argparse
import os
import sys

REL_LS = "packages/ballerina-language-server"
REL_EXT = REL_LS + "/flow-model-generator/modules/flow-model-generator-ls-extension"
REL_TEST_JAVA = REL_EXT + "/src/test/java/io/ballerina/flowmodelgenerator/extension/CatalogProbeTest.java"
REL_TESTNG = REL_EXT + "/src/test/resources/testng.xml"
REL_MANAGER = (REL_LS + "/flow-model-generator/modules/flow-model-generator-core/src/main/java/"
               "io/ballerina/flowmodelgenerator/core/copilot/CopilotLibraryManager.java")

PINNED_OVERLOAD = "loadFilteredLibraries(String[] libraryNames, Map<String, String> pinnedVersions)"

CLASS_ENTRY = '            <class name="io.ballerina.flowmodelgenerator.extension.CatalogProbeTest"/>\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="scratch source checkout")
    ap.add_argument("--scratch", required=True, help="scratch dir for outputs")
    ap.add_argument("--side", required=True, choices=["old", "new"])
    args = ap.parse_args()

    manager = os.path.join(args.src, REL_MANAGER)
    if not os.path.exists(manager):
        sys.exit("ERROR: CopilotLibraryManager not found at %s" % manager)
    pinned_supported = PINNED_OVERLOAD in open(manager, encoding="utf-8").read()

    if pinned_supported:
        resolve_expr = ("PackageUtil.getModulePackage(\n"
                        "                        PackageUtil.getSampleProject(), org, name, pinned)")
        load_expr = ("new CopilotLibraryManager()\n"
                     "                        .loadFilteredLibraries(new String[]{lib}, Map.of(lib, pinned))")
        mode = "EXACT-VERSION (version-aware overload present)"
    else:
        resolve_expr = ("PackageUtil.getModulePackage(\n"
                        "                        PackageUtil.getSampleProject(), org, name)")
        load_expr = "new CopilotLibraryManager().loadFilteredLibraries(new String[]{lib})"
        mode = "VERSION-LESS (overload absent) - the seeded cache is what pins the version"

    tmpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "templates", "CatalogProbeTest.java.tmpl")
    body = open(tmpl_path, encoding="utf-8").read()
    body = (body
            .replace("@@OUT_DIR@@", os.path.join(args.scratch, "json-out-" + args.side))
            .replace("@@PINNED_FILE@@", os.path.join(args.scratch, "pinned.txt"))
            .replace("@@VERSION_REPORT@@", os.path.join(args.scratch, "resolved-versions-%s.txt" % args.side))
            .replace("@@STATUS_LOG@@", os.path.join(args.scratch, "stage1-%s.log" % args.side))
            .replace("@@RESOLVE_EXPR@@", resolve_expr)
            .replace("@@LOAD_EXPR@@", load_expr))

    target = os.path.join(args.src, REL_TEST_JAVA)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(body)

    # Registering in testng.xml is mandatory: the suite is driven by this file, so --tests alone
    # fails with "No tests found for given includes".
    testng_path = os.path.join(args.src, REL_TESTNG)
    testng = open(testng_path, encoding="utf-8").read()
    if "CatalogProbeTest" not in testng:
        if "</classes>" not in testng:
            sys.exit("ERROR: no <classes> block in %s" % testng_path)
        testng = testng.replace("</classes>", CLASS_ENTRY + "        </classes>", 1)
        open(testng_path, "w", encoding="utf-8").write(testng)
        registered = "registered"
    else:
        registered = "already registered"

    print("probe written : %s" % target)
    print("resolution    : %s" % mode)
    print("testng.xml    : %s" % registered)


if __name__ == "__main__":
    main()

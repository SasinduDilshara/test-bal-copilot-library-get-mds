#!/bin/bash
# End-to-end driver: source + side (+ optional library subset) -> renders in <root>/<name>/<side>/.
#
#   run.sh --side old|new --source <path-or-git-url> [--libs "org/a org/b"]
#          [--root <repo-root>] [--scratch <dir>] [--donor-home <dir>] [--skip-seed]
#
# Stops at the first failed gate. A wrong-version render looks perfectly valid, so the gates are
# the whole point: never bypass them to "get output".
set -u

SIDE=""; SOURCE=""; LIBS=""; ROOT=""; SCRATCH=""; DONOR=""; SKIP_SEED=0

while [ $# -gt 0 ]; do
    case "$1" in
        --side)       SIDE="$2"; shift 2 ;;
        --source)     SOURCE="$2"; shift 2 ;;
        --libs)       LIBS="$2"; shift 2 ;;
        --root)       ROOT="$2"; shift 2 ;;
        --scratch)    SCRATCH="$2"; shift 2 ;;
        --donor-home) DONOR="$2"; shift 2 ;;
        --skip-seed)  SKIP_SEED=1; shift ;;
        *) echo "unknown arg: $1" >&2; exit 2 ;;
    esac
done

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[ -n "$ROOT" ] || ROOT="$(cd "$SKILL_DIR/../../.." && pwd)"
[ -n "$SCRATCH" ] || SCRATCH="${TMPDIR:-/tmp}/copilot-render-$SIDE"

if [ -z "$SIDE" ] || [ -z "$SOURCE" ]; then
    echo "ERROR: --side and --source are both required." >&2
    echo "  --source is never guessed: it is the checkout whose behaviour the render represents." >&2
    exit 2
fi
case "$SIDE" in old|new) ;; *) echo "ERROR: --side must be 'old' or 'new'" >&2; exit 2 ;; esac
[ -f "$ROOT/CLAUDE.md" ] || { echo "ERROR: no CLAUDE.md at --root $ROOT" >&2; exit 2; }

S="$SCRATCH"; SRC="$S/src"
mkdir -p "$S"
echo "side=$SIDE  source=$SOURCE  root=$ROOT  scratch=$S"

step() { echo; echo "===== $* ====="; }

step "1/8 pinned list from CLAUDE.md"
if [ -n "$LIBS" ]; then
    # shellcheck disable=SC2086
    python3 "$SKILL_DIR/scripts/parse_libs.py" --root "$ROOT" --out "$S/pinned.txt" --only $LIBS || exit 1
else
    python3 "$SKILL_DIR/scripts/parse_libs.py" --root "$ROOT" --out "$S/pinned.txt" || exit 1
fi

step "2/8 prepare source"
"$SKILL_DIR/scripts/prepare_source.sh" "$SOURCE" "$SRC" || exit 1
COMMIT=$(git -C "$SRC" rev-parse HEAD)

step "3/8 install probe"
PROBE_OUT=$(python3 "$SKILL_DIR/scripts/gen_probe.py" --src "$SRC" --scratch "$S" --side "$SIDE") || exit 1
echo "$PROBE_OUT"
EXACT=""
echo "$PROBE_OUT" | grep -q "EXACT-VERSION" && EXACT="--exact-resolution"

step "4/8 provision build-owned ballerina home"
( cd "$SRC/packages/ballerina-language-server" && ./gradlew resolveBallerinaDependencies ) || exit 1

step "5/8 seed pinned versions into that home"
if [ "$SKIP_SEED" = "1" ]; then
    echo "skipped (--skip-seed)"
else
    "$SKILL_DIR/scripts/seed_home.sh" "$SRC" "$S/pinned.txt" "$DONOR" || \
        echo "WARNING: some packages failed to seed - the audit below decides whether that is fatal"
fi

step "GATE A: home audit"
python3 "$SKILL_DIR/scripts/audit_home.py" --src "$SRC" --pinned "$S/pinned.txt" $EXACT || {
    echo "ABORT: pinned versions would not resolve exactly." >&2; exit 1; }

step "6/8 stage 1 (JSON + resolved-version report)"
rm -rf "$S/json-out-$SIDE"; rm -f "$S/stage1-$SIDE.log" "$S/resolved-versions-$SIDE.txt"
( cd "$SRC/packages/ballerina-language-server" && \
  ./gradlew :flow-model-generator:flow-model-generator-ls-extension:test --rerun-tasks \
    --tests "io.ballerina.flowmodelgenerator.extension.CatalogProbeTest" ) || exit 1
grep STAGE1_DONE "$S/stage1-$SIDE.log" || { echo "ABORT: stage 1 produced no completion marker" >&2; exit 1; }

MISMATCH=$(awk -F'|' '$4!="PIN_OK"' "$S/resolved-versions-$SIDE.txt" | wc -l | tr -d ' ')
step "GATE B: every library resolved at its pinned version"
if [ "$MISMATCH" != "0" ]; then
    echo "ABORT: $MISMATCH library(ies) did not resolve at the pinned version:" >&2
    awk -F'|' '$4!="PIN_OK"' "$S/resolved-versions-$SIDE.txt" >&2
    exit 1
fi
echo "all rows PIN_OK"

step "7/8 stage 2 render"
mkdir -p "$S/tsrun"
if [ ! -x "$S/tsrun/node_modules/.bin/ts-node" ]; then
    ( cd "$S/tsrun" && npm init -y >/dev/null 2>&1 && \
      npm install --no-audit --no-fund ts-node typescript@5.6.3 @types/node >/dev/null 2>&1 ) || exit 1
fi
( cd "$S/tsrun" && ./node_modules/.bin/ts-node \
    --compiler-options '{"module":"commonjs","esModuleInterop":true,"skipLibCheck":true,"target":"es2020"}' \
    "$SKILL_DIR/scripts/render.ts" "$SRC" "$S/json-out-$SIDE" "$ROOT" "$SIDE" \
    "$S/render-report-$SIDE.txt" ) || exit 1

step "GATE C: verify output"
python3 "$SKILL_DIR/scripts/verify_output.py" --root "$ROOT" --pinned "$S/pinned.txt" \
    --side "$SIDE" --versions-report "$S/resolved-versions-$SIDE.txt" || exit 1

step "8/8 clean up probe"
rm -f "$SRC/packages/ballerina-language-server/flow-model-generator/modules/flow-model-generator-ls-extension/src/test/java/io/ballerina/flowmodelgenerator/extension/CatalogProbeTest.java"
git -C "$SRC" checkout -- packages/ballerina-language-server/flow-model-generator/modules/flow-model-generator-ls-extension/src/test/resources/testng.xml
git -C "$SRC" status --short

echo
echo "DONE  side=$SIDE  source=$SOURCE  commit=$COMMIT"
echo "  version report : $S/resolved-versions-$SIDE.txt"
echo "  render report  : $S/render-report-$SIDE.txt"
echo "Report any empty renders and any remaining source deviation to the user by name."

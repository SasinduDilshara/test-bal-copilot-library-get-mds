#!/bin/bash
# Put every pinned version into the BUILD-OWNED ballerina home (the only cache test JVMs read).
#
# Run AFTER `./gradlew resolveBallerinaDependencies` — that task can delete the home.
#
# Optional third arg: a donor home from a previous run. Copying balas is far faster than
# re-downloading and the cache is path-independent. --ignore-existing so the branch's own
# provisioned versions win over the donor's.
set -u

SRC="${1:?usage: seed_home.sh <scratch-src> <pinned.txt> [donor-home]}"
PINNED="${2:?usage: seed_home.sh <scratch-src> <pinned.txt> [donor-home]}"
DONOR="${3:-}"

HOME_DIR="$SRC/packages/ballerina-language-server/build/ballerina_dependencies/home"
BALA="$HOME_DIR/repositories/central.ballerina.io/bala"
BAL="${BAL_CMD:-$HOME/.ballerina/ballerina-home/bin/bal}"

[ -d "$HOME_DIR" ] || { echo "ERROR: build-owned home missing; run resolveBallerinaDependencies first" >&2; exit 1; }
[ -x "$BAL" ] || { echo "ERROR: bal not executable at $BAL (override with BAL_CMD)" >&2; exit 1; }

if [ -n "$DONOR" ]; then
    DONOR_BALA="$DONOR/repositories/central.ballerina.io/bala"
    if [ -d "$DONOR_BALA" ]; then
        echo "seeding from donor cache: $DONOR_BALA"
        mkdir -p "$BALA"
        rsync -a --ignore-existing "$DONOR_BALA/" "$BALA/"
    else
        echo "WARNING: donor has no bala dir, ignoring: $DONOR_BALA" >&2
    fi
fi

export BALLERINA_HOME_DIR="$HOME_DIR"
total=$(grep -c . "$PINNED")
i=0
failed=0

while read -r spec; do
    [ -n "$spec" ] || continue
    i=$((i + 1))
    lib="${spec%:*}"; ver="${spec##*:}"
    org="${lib%%/*}"; name="${lib##*/}"

    if [ -d "$BALA/$org/$name/$ver" ]; then
        echo "[$i/$total] cached $spec"
        continue
    fi

    # `bal pull` exits non-zero when a downloaded package merely fails to COMPILE, so the
    # version directory on disk is the truth, not the exit code. Retry once for transient
    # "package not found" from Central.
    "$BAL" pull "$spec" >/dev/null 2>&1
    if [ ! -d "$BALA/$org/$name/$ver" ]; then
        sleep 3
        "$BAL" pull "$spec" >/dev/null 2>&1
    fi

    if [ -d "$BALA/$org/$name/$ver" ]; then
        echo "[$i/$total] pulled $spec"
    else
        echo "[$i/$total] FAILED $spec"
        failed=$((failed + 1))
    fi
done < "$PINNED"

echo "SEED_DONE pulled_or_cached=$((total - failed)) failed=$failed"
[ "$failed" -eq 0 ]

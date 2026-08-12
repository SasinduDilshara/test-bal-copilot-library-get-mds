#!/bin/bash
# Copy (or clone) a ballerina-vscode source into scratch, leaving the user's checkout untouched.
#
# Two macOS-specific traps handled here:
#   - rsync is 2.6.9: --info=progress2 does not exist.
#   - excluding 'build/' also deletes TRACKED files that live in a directory named build
#     (checkstyle config, .github/actions/build/action.yml). We restore them from git.
set -u

SRC="${1:?usage: prepare_source.sh <src-path-or-git-url> <dest>}"
DEST="${2:?usage: prepare_source.sh <src-path-or-git-url> <dest>}"

if [ -d "$DEST/.git" ]; then
    echo "dest already populated: $DEST"
else
    case "$SRC" in
        http*|git@*)
            echo "cloning $SRC ..."
            for i in 1 2 3 4 5; do
                rm -rf "$DEST"
                git -c http.postBuffer=524288000 -c core.compression=0 \
                    clone --depth 1 --no-tags "$SRC" "$DEST" && break
                echo "clone attempt $i failed; retrying"
                sleep 15
            done
            ;;
        *)
            [ -d "$SRC/.git" ] || { echo "ERROR: not a git checkout: $SRC" >&2; exit 1; }
            echo "copying $SRC -> $DEST (excluding node_modules and build outputs) ..."
            mkdir -p "$DEST"
            rsync -a \
                --exclude 'node_modules/' --exclude '/build/' --exclude '*/build/' --exclude '.gradle/' \
                "$SRC/" "$DEST/" || { echo "ERROR: rsync failed" >&2; exit 1; }
            ;;
    esac
fi

[ -d "$DEST/packages" ] || { echo "ERROR: copy/clone incomplete, no packages/ in $DEST" >&2; exit 1; }

# Restore tracked files the build/ exclude removed.
DELETED=$(git -C "$DEST" ls-files -d | wc -l | tr -d ' ')
if [ "$DELETED" != "0" ]; then
    echo "restoring $DELETED tracked file(s) removed by the build/ exclude ..."
    git -C "$DEST" ls-files -d -z | xargs -0 git -C "$DEST" checkout --
fi

STILL=$(git -C "$DEST" ls-files -d | wc -l | tr -d ' ')
if [ "$STILL" != "0" ]; then
    echo "ERROR: $STILL tracked file(s) still missing after restore" >&2
    exit 1
fi

echo "SOURCE_READY $DEST"
echo "SOURCE_COMMIT $(git -C "$DEST" rev-parse HEAD)"
echo "SOURCE_BRANCH $(git -C "$DEST" rev-parse --abbrev-ref HEAD)"

#!/usr/bin/env bash
#
# Usage:
#   dev_cfg.sh backup
#   dev_cfg.sh restore
#
# Description: Backup and resore $HOME/.config/dev directory; use GPG to protect sensitive data.
#
# ENV VARS: (add to $HOME/.profile)
#   DEV_ROOT:                 Dev root directory ($HOME/dev)
#   DEV_CFG_ROOT:             Dev config root ($HOME/.config/dev)
#   DEV_CFG_ROOT_BKUP:        Backup directory
#   DEV_CFG_BKUP_GPG_KEY:     GPG key name
#
# Author: Justin Stout
# Version: 1.0.1

TMP_WORK_DIR=$(mktemp -d -t clip-XXXXXXXXXX)
TMP_CLIP_META_DIR="$TMP_WORK_DIR/clip_meta"

PDF_FILE=$(pwd)/$2

function cleanup {
    rm -rf "$TMP_WORK_DIR"
}


# echo "TMP_WORK_DIR: $TMP_WORK_DIR"
# mkdir -p "$TMP_CLIP_META_DIR"
# echo "clipped" >> "${TMP_CLIP_META_DIR}/clipped"
# echo "clipped"

# $ src/scripts/clip-article.sh https://www.rawstory.com/ayn-rand-philosophy/ meta-test-1.pdf
# exiftool meta-test-1.pdf
dist/article-clipper $1 | pandoc --metadata-file metadata.yaml -f html -t latex -o $PDF_FILE

# pushd $TMP_CLIP_META_DIR
# # zip -ur $ODT_FILE clip_meta
# zip -ur $ODT_FILE clipped
# popd

# ls "$TMP_WORK_DIR"
# ls "$TMP_ODT_UNZIP"

trap cleanup EXIT

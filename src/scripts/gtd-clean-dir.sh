#!/usr/bin/env bash
#
# Usage:
#   gtd-clean-dir.sh TARGET
#
# Description: Prune empty dirs from a directory tree
#
# Author: Justin Stout
# Version: 1.0.0

set -e
set -o pipefail
set -u
IFS=$'\n\t'

echoerr() { printf "%s\n" "$*" >&2 ; }
info()    { echoerr "[INFO]    $*" ; }
warning() { echoerr "[WARNING] $*" ; }
error()   { echoerr "[ERROR]   $*" ; }
fatal()   { echoerr "[FATAL]   $*" ; exit 1 ; }

clean() {
    if [ -d ${1} ];
    then
        find ${1} -type d -empty -delete
    else
        echo "target does not exist"
    fi
}

if [[ $# -ne 1 ]];
then
    echo "Missing TARGET"
else
    clean $1
fi

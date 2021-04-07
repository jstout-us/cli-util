#!/usr/bin/env bash
#
# Usage:
#   git-new-forge.sh FORGE-NAME
#
# Description: Create a new forge directory at $HOME/PFORGE-NAME using standard template.
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

make () {
    local TARGET="$HOME/$1"
}

if [[ $# -ne 1 ]];
then
    echo "Missing FORGE-NAME"
else
    make $1
fi

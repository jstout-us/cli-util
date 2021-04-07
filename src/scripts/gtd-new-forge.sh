#!/usr/bin/env bash
#
# Usage:
#   gtd-new-forge.sh FORGE-NAME
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

    mkdir -p "${TARGET}"/"00 - Inbox"/{"10 - Ideas","20 - Sources","30 - Questions"}
    mkdir -p "${TARGET}"/"10 - Notes"
    mkdir -p "${TARGET}"/"20 - Mgt & Plans"
    mkdir -p "${TARGET}"/"30 - Docs"
    mkdir -p "${TARGET}"/"60 - Children"
    mkdir -p "${TARGET}"/"90 - Closed Projects"
    mkdir -p "${TARGET}"/"91 - Lost Projects"
    mkdir -p "${TARGET}"/"92 - OBE Projects"

cat > "${TARGET}"/"20 - Mgt & Plans"/"00 - README.txt" << EOM
README
===================================================================================================

<intro>

Objectives:
=======================================

1.  TBD
2.  TBD


References:
=======================================

1.  TBD
2.  TBD

EOM

cat > "${TARGET}"/"20 - Mgt & Plans"/"01 - Work Plan.txt" << EOM
Work Plan
===================================================================================================

*   Release 0.1

*   Release 0.2

*   Release 1.0

*   Release 2.0

EOM

}

if [[ $# -ne 1 ]];
then
    echo "Missing FORGE-NAME"
else
    make $1
fi

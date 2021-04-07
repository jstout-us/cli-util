#!/usr/bin/env bash
#
# Usage:
#   gtd-new-project.sh PROJECT-NAME
#
# Description: Create a new project directory at $HOME/PROJECT-NAME using standard template.
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

    mkdir -p "${TARGET}"/"00 - Inbox"
    mkdir -p "${TARGET}"/"10 - Notes"
    mkdir -p "${TARGET}"/"20 - Mgt & Plans"
    mkdir -p "${TARGET}"/"30 - Docs"
    mkdir -p "${TARGET}"/"40 - Working"/{"MS01 - Bootstrap","MS02 - TBD","MS99 - Close"}
    mkdir -p "${TARGET}"/"40 - Working"/"MS90 - Close Out"/{"10 - Lessons Learned","20 - Future Work"}
    mkdir -p "${TARGET}"/"40 - Working"/"MS91 - Publish"/{"T10 - Refs","T20 - Outline","T30 - Draft 1"}
    mkdir -p "${TARGET}"/"40 - Working"/"MS91 - Publish"/{"T31 - Draft 2","T90 - Finalize","T99 - Publish"}
    mkdir -p "${TARGET}"/"99 - Closed"

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

*   MS01 - Bootstrap Project

*   MS02 - TBD

*   MS90 - Close Out

*   MS91 - Publish

*   MS99 - Close Project

EOM

cat > "${TARGET}/40 - Working/MS99 - Close/00 - Conclusions.txt" << EOM
Conclusions
===================================================================================================

*   TBD

EOM
}

if [[ $# -ne 1 ]];
then
    echo "Missing PROJECT-NAME"
else
    make $1
fi

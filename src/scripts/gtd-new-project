#!/usr/bin/env bash
#
# Usage:
#   dev_project_dir.sh make "<path>"
#   dev_project_dir.sh clean "<path>"
#
# Description: Backup and resore $HOME/.config/dev directory; use GPG to protect sensitive data.
#
# make: populate a project directory with our standard layout
# clean: delete all empty directories from a project directory
#
# Author: Justin Stout
# Version: 1.0.0

# Derived from: https://www.nicksantamaria.net/post/boilerplate-bash-script/

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
    local path="$1"
    mkdir -p "${path}"/"00 - Notes"/${USER}/{"Cheat Sheets","Journal","Lessons Learned","Notebook"}
    mkdir -p "${path}"/"20 - Documentation"/{"App Notes","Data Sheets","Design","User"}
    mkdir -p "${path}"/"40 - Working"/"MS01 - Research"/"T01 - TBD"
    mkdir -p "${path}"/"99 - Close Out"
}

clean () {
    local path="$1"
    find ${path} -type d -empty -delete
}

if [[ "${BASH_SOURCE[0]}" = "$0" ]]; then

  if [[ $1 == "make" ]]; then
    make $2

  elif [[ $1 == "clean" ]]; then
    clean $2

  fi

fi

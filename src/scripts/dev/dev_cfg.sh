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


_link_files() {
    ln -sf ${DEV_CFG_ROOT}/home/.gitconfig ${HOME}/.gitconfig

    for key_name in ${DEV_CFG_ROOT}/home/.ssh/*; do
        ln -sf ${key_name} ${HOME}/.ssh/$(basename -- ${key_name})
    done
}


backup() {
    local archive="${DEV_CFG_ROOT_BKUP}/$(date +%Y%m%d_%H%M%S).tar.bz2.gpg"
    info "backup ${DEV_CFG_ROOT} to ${archive}"

    /usr/bin/env tar -jcv -C ${DEV_CFG_ROOT} . | gpg -e -r ${DEV_CFG_BKUP_GPG_KEY} \
                                                    --trust-model always \
                                                    -o ${archive}
}


restore() {
    local latest_backup=$DEV_CFG_ROOT_BKUP/`ls $DEV_CFG_ROOT_BKUP | tail -n 1`

    if [[ -f ${latest_backup} ]]; then
        info "restore ${latest_backup} to ${DEV_CFG_ROOT}"

        rm -rf ${DEV_CFG_ROOT}
        mkdir -p ${DEV_CFG_ROOT}

        gpg -d ${latest_backup} | tar -jxv -C ${DEV_CFG_ROOT}

        _link_files

    else
        fatal "No backup file found."

    fi
}


if [[ "${BASH_SOURCE[0]}" = "$0" ]]; then

  if [[ $1 == "backup" ]]; then
    backup

  elif [[ $1 == "restore" ]]; then
    restore

  fi

fi

#!/usr/bin/env bash
#
# Usage:
#   dev_cfg.sh backup
#   dev_cfg.sh restore
#
# Description: Backup and resore $HOME/dev/.config directory; use GPG to protect sensitive data.
#
# ENV VARS: (add to $HOME/.profile)
#   DEV_CFG_DIR:        Source directory
#   DEV_CFG_DIR_BKUP:   Backup directory
#   DEV_CFG_GPG_KEY:    GPG key name
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


_link_files() {
    ln -sf ${DEV_CFG_DIR}/home/.gitconfig ${HOME}/.gitconfig

    for key_name in ${DEV_CFG_DIR}/home/.ssh/*; do
        ln -sf ${key_name} ${HOME}/.ssh/$(basename -- ${key_name})
    done
}


backup() {
    local archive="${DEV_CFG_DIR_BKUP}/$(date +%Y%m%d_%H%M%S).tar.bz2.gpg"
    info "backup ${DEV_CFG_DIR} to ${archive}"

    /usr/bin/env tar -jcv -C ${DEV_CFG_DIR} . | gpg -e -r ${DEV_CFG_GPG_KEY} \
                                                    --trust-model always \
                                                    -o ${archive}
}


restore() {
    local latest_backup=$DEV_CFG_DIR_BKUP/`ls $DEV_CFG_DIR_BKUP | tail -n 1`

    if [[ -f ${latest_backup} ]]; then
        info "restore ${latest_backup} to ${DEV_CFG_DIR}"

        rm -rf ${DEV_CFG_DIR}
        mkdir -p ${DEV_CFG_DIR}

        gpg -d ${latest_backup} | tar -jxv -C ${DEV_CFG_DIR}

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

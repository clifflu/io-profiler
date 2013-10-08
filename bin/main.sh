#!/bin/bash

#
# Usage:
#   main.sh /mnt/disk
#

DIR_BIN=`dirname "$0"`
DIR_BIN=`pwd`
DIR_PROF=`dirname "$DIR_BIN"`
DIR_LOG="$DIR_PROF/logs"

# "$DIR_BIN/install_pkg.sh"

yum -y install figlet fio 

HOSTNAME=`hostname`
ISO_DATE=`date +"%Y-%m-%dT%H:%M:%SZ"`
mkdir -p "$DIR_LOG/$HOSTNAME"
LOG_FN="$DIR_LOG/$HOSTNAME/$ISO_DATE.log"

touch "$LOG_FN"

for DISK_MP in "$@"
do
    "$DIR_BIN/test.sh" "$DISK_MP" >> "$LOG_FN" 2>&1
done

figlet "done"
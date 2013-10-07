#!/bin/bash

if [ `whoami` != 'root' ]; then
    sudo "$0" "$@"
    exit 0
fi

DIR_ORIGINAL=`pwd`

DIR_BIN=`dirname "$0"`
DIR_BIN=`pwd`

DISK_MP="/tmp"

# "$DIR_BIN/install_pkg.sh"

# run ramfs-based test only if > 1.5GB ram
if [ `free -m|awk 'FNR==2 {print $2}'` -ge 1536 ]; then
   "$DIR_BIN/test_ramfs.sh" "$DISK_MP" 
fi


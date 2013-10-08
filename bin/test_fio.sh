#!/bin/bash

DIR_BIN=`dirname $0`
DIR_BIN=`pwd`
DIR_PROF=`dirname "$DIR_BIN"`
DIR_CONF="$DIR_PROF/conf"

LOC_FIO=`which fio`

DISK_MP="/"
if [ -d "$1" ]; then
    DISK_MP="$1"
fi

NUMOBJS=4
SIZE="256m"

echo "# `basename \"$0\"` $@"
for scr in `ls "$DIR_CONF"`
do
    for bs in 1k 2k 4k 8k 16k 32k 64k 128k 256k
    do
        echo "## BS:$bs, SCR:$scr, NUM: $NUMOBJS, SIZE: $SIZE"
        NUMJOBS=$NUMOBJS SIZE=$SIZE BS=$bs DISK_MP="$DISK_MP" "$LOC_FIO" "$DIR_CONF/$scr"
        echo ""
    done
done

echo ""
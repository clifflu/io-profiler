#!/bin/bash

#
# config
#
LOOPS=3

DD_BS="1k"
DD_COUNT="512k"

FN="data.tmp"

TMPFS_SZ="1024M"
TMPFS_MP="/mnt/tmpfs"
TMPFS_FN="$TMPFS_MP/$FN"

DISK_MP="/tmp"
if [ "x$1" != "x" ]; then
    DISK_MP="$1"
fi
DISK_FN="$DISK_MP/$FN"

#
# Main
#

echo "# `basename \"$0\"` $@"

mkdir -p "$DISK_MP"
mkdir -p "$TMPFS_MP"
mount -t tmpfs -o size="$TMPFS_SZ" none "$TMPFS_MP"

dd if=/dev/zero of="$TMPFS_FN" bs="$DD_BS" count="$DD_COUNT" > /dev/null 2>&1

# ram -> disk
echo "## ram -> disk"
for ((i=1; i<=$LOOPS; i=i+1 ))
do
    echo "### Round $i / $LOOPS"
    /usr/bin/time -v cp "$TMPFS_FN" "$DISK_FN"
done

# disk -> ram
echo "## disk -> ram"
for ((i=1; i<=$LOOPS; i=i+1 ))
do
    echo "### Round $i / $LOOPS"
    /usr/bin/time -v cp "$DISK_FN" "$TMPFS_FN"
done

# cleanup
rm -f "$DISK_FN"
rmdir "$DISK_MP" > /dev/null 2>&1
umount "$TMPFS_MP"

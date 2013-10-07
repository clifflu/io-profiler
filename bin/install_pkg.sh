#!/bin/bash

echo "Installing packages..."

LOC_YUM=`which yum`
if [ "x$LOC_YUM" != "x" ]; then
    yum install fio
fi

DIR_BIN=`dirname "$0"`
cd "$DIR_BIN"

DIR_BIN=`pwd`
DIR_PROF=`dirname "$DIR_BIN"`
HERE=`dirname "$DIR_PROF"`
THERE="test:/home/ec2-user"
TARGET="/io-profiler"

rsync -avzutr "$HERE""$TARGET" "$THERE"
rsync -avzutr "$THERE""$TARGET" "$HERE"

DIR_BIN=`dirname "$0"`
DIR_BIN=`pwd`
DIR_PROF=`dirname "$DIR_BIN"`
HERE=`dirname "$DIR_PROF"`
THERE="test:/home/ec2-user"
TARGET="/prof"

rsync -avzutr "$HERE""$TARGET" "$THERE"
rsync -avzutr "$THERE""$TARGET" "$HERE"

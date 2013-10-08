HERE="/Users/clifflu/Projects/"
THERE="test:/home/ec2-user/"
TARGET="prof"

rsync -avzutr "$HERE""$TARGET" "$THERE"
rsync -avzutr "$THERE""$TARGET" "$HERE"

#!/bin/sh

echo "$(date +"%F-%H%M%S") + <br />" >> README.md
echo 'success update' >> mylog.log

git add .
git commit -m "同步于 $(date +"%F-%H%M%S")"
git push

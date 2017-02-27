#! /bin/sh

echo $(date +"%F-%H%M%S") >> README.md
echo -e '\n' >> README.md

git add .
git commit -m "同步于 $(date +"%F-%H%M%S")"
git push

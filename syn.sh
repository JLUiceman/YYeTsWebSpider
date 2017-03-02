#!/bin/sh

baseUrl=‘http://cili17.com/?_=123’
status_code=$(curl -I $baseUrl | grep '200 OK' | wc -l)
if [ $status_code -eq 1 ];then
  canView='可以'
else
  canView='挂求了'
fi  
  
echo "$(date +"%F-%H%M%S") + <br />" >> README.md
echo "今天mag磁力站能访问吗?$canView" >> README.md

git add .
git commit -m "同步于 $(date +"%F-%H-%-M%-S")"
git push

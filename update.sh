#!/bin/sh

if [ $# -eq 0 ]
then
    echo 'Need commit msg as param'
    exit 2
fi

git add ./solutions
python gen_readme.py
git add ./README.md
git commit -m "$1"
git push origin master

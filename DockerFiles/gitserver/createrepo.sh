#!/bin/sh

#echo $1
#echo $1.git

mkdir -p $PWD/repositories/$1.git
mkdir -p $PWD/programs/$1
#chgrp -R git:developers $PWD/repositories

cd $PWD/repositories/$1.git
git init --bare --shared=group

sed "s/NAME/$1/g" $PWD/post-update-template > $PWD/repositories/$1.git/hooks/post-update
#chgrp git:developers /git/repositories/$1.git

cd $PWD/programs/$1/
git init
touch README
git add .
git commit -am "Initial commit"
git remote add origin git@localhost:/git/repositories/$1.git

git push origin master

#!/bin/sh

docker run -i -t --name=runninggitserver \
  -v $PWD:/localfiles \
  -v $PWD/repositories:/git/repositories \
  -v $PWD/project:/git/projects \
  gitserver \
  /dockerstartscript.sh



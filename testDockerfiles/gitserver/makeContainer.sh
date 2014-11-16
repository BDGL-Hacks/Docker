#!/bin/sh

docker run -i -t --name=runninggitserver -v $PWD:/localfiles gitserver /dockerstartscript.sh



#!/bin/sh

docker run -it --name=runningproxy --privileged -d -p 1723:1723 -v $PWD/chap-secrets:/etc/ppp/chap-secrets -v $PWD/options.pptpd:/etc/ppp/options.pptpd -v $PWD/pptpd.conf:/etc/pptpd.conf proxy /bin/bash #/run.sh

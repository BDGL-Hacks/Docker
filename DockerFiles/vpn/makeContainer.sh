#!/bin/sh

docker run -it --name runningproxy \
             --privileged \
                        -v $PWD/data:/data \
                        -v $PWD/bin/openvpn-run:/bin/openvpn-run   \
           -p 1194:1194/udp \
                        proxy /bin/openvpn-run 

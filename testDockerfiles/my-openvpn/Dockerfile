########################################################################
# I'm going to leave the credit for this guy's design even though I 
# heavily modified it.
#
# Author:       pjan vandaele <pjan@pjan.io>
# Scm url:      https://github.com/pjan/docker-openvpn
# License:      MIT
#
########################################################################
# pull base image
FROM debian:wheezy


RUN \
  apt-get update -q -y && \
  apt-get clean && \
  rm -rf /var/cache/apt/*

# install openvpn, iptables and curl
RUN \
  apt-get install -y -q openvpn iptables curl

#ADD \
#  ./bin /bin

#RUN \
#  chmod 755 /bin/openvpn-run

VOLUME \
  ["/data"]

EXPOSE \
  1194/udp

#ENTRYPOINT \
#  ["/bin/openvpn-run"]

# docker build [--rm] -t <user>/openvpn .
# docker run -v /data --name openvpn-data busybox:ubuntu-14.04
# docker run -d --name openvpn --privileged --volumes-from openvpn-data -p 1194:1194/udp <user>/openvpn

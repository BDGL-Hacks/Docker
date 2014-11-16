FROM debian:wheezy

RUN apt-get update &&\
apt-get install -y pptpd iptables

RUN rm -rf /var/lib/apt/lists/*

EXPOSE 1723



FROM debian:wheezy

RUN apt-get update
RUN apt-get install -yq tinyproxy

ADD startup.sh /startup.sh
ADD tinyproxy.conf /etc/tinyproxy.conf

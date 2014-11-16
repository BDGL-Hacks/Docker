FROM debian:wheezy

RUN apt-get update &&\
apt-get install -yq ssh openssh-server

#ADD sshd_config /etc/ssh/sshd_config

RUN useradd vpn && echo vpn:maroon | chpasswd && chmod 644 /etc/ssh/sshd_config && chown root:root /etc/ssh/sshd_config


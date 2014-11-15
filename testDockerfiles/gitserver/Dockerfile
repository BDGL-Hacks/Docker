FROM debian:wheezy

RUN apt-get update && \
apt-get install -y git openssh-server &&\


groupadd developers && \

useradd -G developers git && \
echo git:lol | chpasswd && \

mkdir -p /git/repositories/practice.git &&\
mkdir -p /git/programs/ &&\ 
cd /git/repositories/practice.git &&\
git init --bare --shared=group &&\
chgrp -R developers /git && /
service ssh start

ADD createrepo /git/
ADD post-update-template /git/



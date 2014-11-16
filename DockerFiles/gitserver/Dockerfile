FROM debian:wheezy

RUN apt-get update && \
apt-get install -y git openssh-server


RUN groupadd developers && \

useradd -G developers -o -u 0  git && \
echo git:lol | chpasswd

RUN mkdir -p /home/git &&\ 
mkdir -p /home/git/.ssh/ &&\


chmod 700 /home/git/.ssh &&\
ssh-keygen -t rsa -f /home/git/.ssh/id_rsa -N "" &&\
chown git:developers -R /home/git && exit


RUN mkdir -p /root/.ssh/ &&\
chmod 700 /root/.ssh/ &&\
ssh-keygen -t rsa -f /root/.ssh/id_rsa -N ""

#ADD authorized_keys /home/git/.ssh/
ADD dockerstartscript.sh /dockerstartscript.sh

RUN mkdir -p /localfiles &&\
mkdir -p /git/ && \
chgrp -R developers /git 

ADD createrepo.sh /git/
ADD post-update-template /git/



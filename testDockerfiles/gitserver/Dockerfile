FROM debian:wheezy

RUN apt-get update && \
apt-get install -y git openssh-server &&\


groupadd developers && \

useradd -G developers git && \
chpasswd git lol && \

mkdir -p repositories/practice.git &&\
chgrp -R developers repositories &&\  
cd repositories/practice.git &&\
git init --bare --shared=group 






#!/bin/sh

if [ ! -e /localfiles/authorized_keys ]
then
cp /home/git/.ssh/id_rsa.pub /localfiles/authorized_keys
cat /root/.ssh/id_rsa.pub >> /localfiles/authorized_keys
chmod 600 /localfiles/authorized_keys
chown git:developers /localfiles/authorized_keys
ln -sf /localfiles/authorized_keys /home/git/.ssh/authorized_keys
chown git:developers /home/git/.ssh/authorized_keys
fi

chown -R git:developers /git
service ssh start

while :
do 
  sleep 1
done


#!/bin/sh

IP=$(cat dns_ip)

curl -X PUT \
      -d '{"domains": ["maroon.gilh"]}' \
          http://$IP:5080/container/name/$1

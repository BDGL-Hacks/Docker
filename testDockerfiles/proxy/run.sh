iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
exec pptpd -f
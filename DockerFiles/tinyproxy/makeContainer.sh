docker run --name=runningtinyproxy --dns $(cat ../dns/dns_ip) tinyproxy service tinyproxy start && /startup.sh

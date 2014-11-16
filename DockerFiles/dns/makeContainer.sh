docker run -d -v /var/run/docker.sock:/docker.sock --name dns \
      phensley/docker-dns-rest --verbose 
sleep 1
python get_ip.py dns > dns_ip

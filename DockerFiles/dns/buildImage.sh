docker run -d -v /var/run/docker.sock:/docker.sock --name dns \
      phensley/docker-dns-rest --verbose 

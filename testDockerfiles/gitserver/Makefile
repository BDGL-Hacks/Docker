build:
	docker build -t gitserver .

connect:
	docker attach runninggitserver

restart: remove create
	
remove: 
	docker rm -f runninggitserver

create:
	./runContainer.sh

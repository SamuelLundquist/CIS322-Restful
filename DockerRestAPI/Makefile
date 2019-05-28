.PHONY: install start stop prune

up: Dockerfile
	sudo docker-compose up

down:
	sudo docker-compose down
	
prune:
	docker system prune -a

default: up

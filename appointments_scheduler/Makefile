build:
	docker-compose build --no-cache

up:
	docker-compose up

restart:
	docker-compose restart scheduler-api

migrate:
	docker-compose exec scheduler-api su -c "python manage.py migrate"

test:
	docker-compose exec scheduler-api su -c "python manage.py test -v2"

down:
	docker-compose down

createsuperuser:
	docker-compose exec scheduler-api su -c "python manage.py createsuperuser"

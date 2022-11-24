start:
	poetry run python manage.py migrate \
	poetry run python manage.py collectstatic \
	poetry run gunicorn config.wsgi:app --bind 0.0.0.0:8000 --reload -w 4

docker_build:
	docker-compose --env-file ./.env up --detach --build

test:
	poetry run python manage.py test utils.tests --settings=config.test
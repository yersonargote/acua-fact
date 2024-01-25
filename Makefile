black:
	poetry run black . --check

ruff:
	poetry run ruff check acua_fact tests

format:
	poetry run black .
	poetry run ruff check acua_fact tests --fix


dup:
	docker-compose up -d

down:
	docker-compose down

clear:
	rm -rf ./acua_fact/ui/assets/*.pdf

check:
	make format

install:
	poetry install

run:
	poetry run uvicorn acua_fact.main:app --reload

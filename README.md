## Описание проекта
Проект разработан с использованием [Python](https://www.python.org/) и [FastAPI](https://fastapi.tiangolo.com/).

## Установка и настройка

```shell
   git clone https://github.com/vebulogmetra/project_task_1.git
```
```shell
   cd project_task_1
```
- Заполнить файл с переменными окружения

```shell
   vim src/config/env-example
```
```shell
   mv src/config/env-example src/config/.env
```
- Для запуска в Docker
```shell
   docker-compose up --build
```
- Перейдите на [Swagger docs](http://0.0.0.0:5000/docs)

Для запуска без Docker и с sqlite установите в /config/settings.py файле DOCKERIZE=False DEVELOPMENT=True
```shell
   sed -i 's/DOCKERIZE=True/DOCKERIZE=False/' src/config/settings.py && \
   sed -i 's/DEVELOPMENT=False/DEVELOPMENT=True/' src/config/settings.py
```
```shell
   poetry install
```
```shell
   python .
```
- Перейдите на [Swagger docs](http://127.0.0.1:5000/docs)

## Запуск тестов

```shell
   pytest tests/
```
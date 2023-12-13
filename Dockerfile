FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.6.1 \
  TZ=Europe/Moscow

RUN pip install "poetry==$POETRY_VERSION" \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --without dev --no-interaction --no-ansi

COPY . /app

COPY ddl_pg.sql /docker-entrypoint-initdb.d/

CMD ["python", "."]

EXPOSE 5000
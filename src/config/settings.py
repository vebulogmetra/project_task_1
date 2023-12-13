import os

from dotenv import load_dotenv

load_dotenv()

DEVELOPMENT = True
DOCKERIZE = False

APP_HOST = "localhost"
APP_PORT = 5000
APP_TITLE = "test_task_rootcode"
APP_API_PREFIX = "/api/v1"

POSTGRES_USER = "myuser"
POSTGRES_PASSWORD = "123"
POSTGRES_DB = "mydb"

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PWD = os.environ.get("POSTGRES_PASSWORD")
DB_NAME = os.environ.get("POSTGRES_DB")

DB_SQLALCHEMY_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
DB_SQLALCHEMY_URL_DOCKER = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@db/{DB_NAME}"
DB_SQLALCHEMY_URL_DEV = "sqlite:///./database.db"

if not DEVELOPMENT:
    db_url = DB_SQLALCHEMY_URL
if DEVELOPMENT:
    db_url = DB_SQLALCHEMY_URL_DEV
if DOCKERIZE:
    db_url = DB_SQLALCHEMY_URL_DOCKER

# db_url = DB_SQLALCHEMY_URL_DEV if DEVELOPMENT else DB_SQLALCHEMY_URL

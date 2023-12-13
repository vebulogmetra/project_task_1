import os
from dotenv import load_dotenv

load_dotenv()


DOCKERIZE = 0
DEVELOPMENT = 1
APP_HOST = "localhost"
APP_PORT = 5000
APP_TITLE = "test_task_rootcode"
APP_API_PREFIX = "/api/v1"

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = 5432
DB_USER = os.environ.get("DB_USER")
DB_PWD = os.environ.get("DB_PWD")
DB_NAME = os.environ.get("DB_NAME")

DB_SQLALCHEMY_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@db/{DB_NAME}"
DB_SQLALCHEMY_URL_DEV = "sqlite:///./database.db"


db_url = DB_SQLALCHEMY_URL_DEV if DEVELOPMENT else DB_SQLALCHEMY_URL

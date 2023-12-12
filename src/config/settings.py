DEVELOPMENT = 1
APP_HOST = "localhost"
APP_PORT = 5000
APP_TITLE = "test_task_rootcode"
APP_API_PREFIX = "/api/v1"

DB_SQLALCHEMY_URL = "postgresql+psycopg2://"
DB_SQLALCHEMY_URL_DEV = "sqlite:///./database.db"


db_url = DB_SQLALCHEMY_URL_DEV if DEVELOPMENT else DB_SQLALCHEMY_URL

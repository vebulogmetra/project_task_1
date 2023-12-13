from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.settings import db_url

engine = create_engine(url=db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


@contextmanager
def session_scope():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_db():
    with session_scope() as db:
        yield db

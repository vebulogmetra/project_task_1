import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.utils.database import Base


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    connection = engine.connect()
    transaction = connection.begin()

    yield TestingSessionLocal

    transaction.rollback()
    connection.close()
    engine.dispose()

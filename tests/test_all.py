from fastapi.testclient import TestClient
from main import app
import os
from src.config import settings

base_api_url = settings.APP_API_PREFIX
import_file_url: str = os.path.join(base_api_url, "import_file")
export_file_url: str = os.path.join(base_api_url, "export_file/4")


client = TestClient(app)


def test_import_file(db):
    with open("example.xlsx", "rb") as file:
        response = client.post(import_file_url, files={"file_": ("test_file.csv", file)})
        assert response.status_code == 200


def test_export_file(db):
    response = client.get(export_file_url)
    assert response.status_code == 200

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books/", json={
        "title": "Sample Book",
        "author": "Author Name",
        "year": 2024,
        "isbn": "1234567890123"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Book"
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, get_engine
from app.models import Base, get_session

# Configuración de Base de Datos de Pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = get_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = get_session(SQLALCHEMY_DATABASE_URL)
        yield db
    finally:
        db.close()

# Sobrescribir dependencia de base de datos para pruebas
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_add_book():
    response = client.post("/books/", json={
        "title": "Integration Test Book",
        "author": "Integration Author",
        "year": 2024,
        "isbn": "123-456-789"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Integration Test Book"
    assert data["author"] == "Integration Author"
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Base, engine, Libro, SessionLocal
from app.schemas import LibroCreate, LibroUpdate, LibroOut

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/libros/", response_model=LibroOut, status_code=201)
def agregar_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = Libro(**libro.dict())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

@app.get("/libros/", response_model=list[LibroOut])
def listar_libros(db: Session = Depends(get_db)):
    return db.query(Libro).all()
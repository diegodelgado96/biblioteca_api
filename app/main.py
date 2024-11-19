from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Biblioteca API",
    description="API REST para gestionar una biblioteca con operaciones CRUD",
    version="1.0.0",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.BookResponse)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/list/", response_model=list[schemas.BookResponse])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/", response_model=list[schemas.BookResponse])
def list_books_by_author_or_year(author: str = None, year: int = None, db: Session = Depends(get_db)):
    return crud.get_books_by_author_year(db, author, year)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
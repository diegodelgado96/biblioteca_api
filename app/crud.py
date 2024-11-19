from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, author: str = None, year: int = None):
    query = db.query(models.Book)
    if author:
        query = query.filter(models.Book.author == author)
    if year:
        query = query.filter(models.Book.year == year)
    return query.all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None
    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book
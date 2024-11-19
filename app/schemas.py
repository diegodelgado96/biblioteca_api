from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    isbn: str | None = None

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class LibroBase(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int
    isbn: str

class LibroCreate(LibroBase):
    pass

class LibroUpdate(BaseModel):
    titulo: str | None = None
    autor: str | None = None
    anio_publicacion: int | None = None
    isbn: str | None = None

class LibroOut(LibroBase):
    id: int

    class Config:
        orm_mode = True
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "postgresql+asyncpg://usuario:contraseña@localhost/biblioteca"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    anio_publicacion = Column(Integer, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
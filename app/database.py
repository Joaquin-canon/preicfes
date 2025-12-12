from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# CONFIGURA TU CONEXIÓN
USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = "3306"
DB_NAME = "proyecto_icfes"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # opcional: muestra las consultas SQL
    future=True
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

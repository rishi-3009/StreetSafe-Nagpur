from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# check_same_thread=False is required for SQLite specifically, since FastAPI
# may access the DB from a different thread than the one that created it.
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Provides a database session to each request, and guarantees
    it gets closed afterward — even if an error happens mid-request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""Database manager."""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get a SQLAlchemy session
@contextmanager
def get_database():
    database = SessionLocal()
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()


# Initialise the database
def init_db():
    Base.metadata.create_all(bind=engine)

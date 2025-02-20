from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.core.config import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


# Dependency to get a SQLAlchemy session
def get_database():
    database = SessionLocal()
    try:
        yield database  # Return the session directly
    finally:
        database.close()  # Ensure the session is closed after use


# Initialise the database
def init_db():
    import app.models  # Import your models here
    SQLModel.metadata.create_all(bind=engine)

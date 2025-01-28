from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a SQLAlchemy session
def get_database():
    database = SessionLocal()
    try:
        yield database  # Return the session directly
    finally:
        database.close()  # Ensure the session is closed after use


# Initialise the database
def init_db():
    Base.metadata.create_all(bind=engine)

"""Project model for SQL database."""
from sqlalchemy import Column, Integer, Text, String

from app.models.base_model import Base


class ContractorType(Base):
    __tablename__ = "contractor_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

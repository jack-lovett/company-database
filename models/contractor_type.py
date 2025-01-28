"""Project model for SQL database."""
from sqlalchemy import Column, Integer, Text, String

from models import Base


class ContractorType(Base):
    __tablename__ = "contractor_type"

    contractor_type_id = Column(Integer, primary_key=True, autoincrement=True)
    contractor_type = Column(String(255), nullable=False)
    contractor_type_description = Column(Text, nullable=True)

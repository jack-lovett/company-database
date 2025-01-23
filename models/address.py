"""Address model for SQL database."""
from sqlalchemy import Column, Integer, Enum, String

from models import Base


class Address(Base):
    """Address model class"""
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address_street = Column(String(45), nullable=False)
    address_suburb = Column(String(45), nullable=False)
    address_city = Column(String(45), nullable=False)
    address_state = Column(String(45), nullable=False)
    address_postal_code = Column(String(45), nullable=False)
    address_country = Column(String(45), nullable=False)
    address_type = Column(Enum("billing_address", "postal_address"), nullable=False)

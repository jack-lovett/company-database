"""Contractor model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Contractor(Base):
    """Contractor model class"""
    __tablename__ = 'contractor'

    contractor_id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=False)

    contact = relationship("Contact", backref="contractor")

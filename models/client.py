"""Project model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from models import Base


class Client(Base):
    """Client model class"""
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True, autoincrement=True)
    primary_contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=False)
    secondary_contact_id = Column(Integer, ForeignKey('contact.contact_id'))
    client_creation_datetime = Column(DateTime, default=func.current_timestamp())

    primary_contact = relationship("Contact", foreign_keys=[primary_contact_id], backref="primary_clients")
    secondary_contact = relationship("Contact", foreign_keys=[secondary_contact_id], backref="secondary_clients")

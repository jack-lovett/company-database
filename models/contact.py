"""Contact model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, String
from sqlalchemy.orm import relationship

from models import Base


class Contact(Base):
    """Contact model class"""
    __tablename__ = 'contact'

    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    postal_address_id = Column(Integer, ForeignKey('address.address_id'))
    contact_first_name = Column(String(45), nullable=False)
    contact_last_name = Column(String(45), nullable=False)
    contact_phone = Column(String(45))
    contact_email = Column(String(45))
    contact_business_name = Column(String(45))
    contact_abn = Column(String(45))
    contact_acn = Column(String(45))
    contact_accounts_email = Column(String(45))
    contact_website = Column(String(45))
    contact_discipline = Column(String(45))
    contact_creation_datetime = Column(DateTime, default=func.current_timestamp())

    address = relationship("Address", foreign_keys=[address_id], backref="contacts")
    postal_address = relationship("Address", foreign_keys=[postal_address_id], backref="postal_contacts")
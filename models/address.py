from sqlalchemy import Column, Integer, Enum, String
from sqlalchemy.orm import relationship

from models import Base


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address_street = Column(String(45), nullable=False)
    address_suburb = Column(String(45), nullable=False)
    address_city = Column(String(45), nullable=False)
    address_state = Column(String(45), nullable=False)
    address_postal_code = Column(String(45), nullable=False)
    address_country = Column(String(45), nullable=False)
    address_type = Column(Enum("billing_address", "postal_address"), nullable=False)

    contacts_as_billing = relationship("Contact", foreign_keys="Contact.address_id", back_populates="billing_address", overlaps="contacts_as_billing")
    contacts_as_postal = relationship("Contact", foreign_keys="Contact.address_id", back_populates="postal_address", overlaps="contacts_as_billing")

    projects = relationship("Project", back_populates="address")

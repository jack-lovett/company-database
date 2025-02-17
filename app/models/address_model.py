from sqlalchemy import Column, Integer, Enum, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(45), nullable=False)
    suburb = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    postal_code = Column(String(4), nullable=False)
    country = Column(String(45), nullable=False)
    type = Column(Enum("billing_address", "postal_address", "shipping_address", "office_address"),
                  nullable=False)

    contacts_as_billing = relationship("Contact",
                                       foreign_keys="Contact.address_id",
                                       back_populates="billing_address")
    contacts_as_postal = relationship("Contact",
                                      foreign_keys="Contact.postal_address_id",
                                      back_populates="postal_address")

    sites = relationship("Site", back_populates="address")

    def __str__(self):
        return f"{self.street}, {self.suburb}, {self.city}, {self.state} {self.postal_code}"

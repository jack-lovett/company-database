from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, func
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=True)
    postal_address_id = Column(Integer, ForeignKey('address.id'), nullable=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
    business_name = Column(String(255), nullable=True)
    abn = Column(String(11), nullable=True)
    accounts_email = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    discipline = Column(String(255), nullable=True)
    creation_datetime = Column(DateTime, default=func.now(), nullable=False)

    contractors = relationship("Contractor", back_populates="contact")

    staff = relationship("Staff", back_populates="contact")

    billing_address = relationship("Address", foreign_keys=[address_id], back_populates="contacts_as_billing",
                                   overlaps="contacts_as_postal")
    postal_address = relationship("Address", foreign_keys=[postal_address_id], back_populates="contacts_as_postal",
                                  overlaps="contacts_as_billing")

    primary_for_clients = relationship("Client", foreign_keys="Client.primary_contact_id",
                                       back_populates="primary_contact")
    secondary_for_clients = relationship("Client", foreign_keys="Client.secondary_contact_id",
                                         back_populates="secondary_contact")

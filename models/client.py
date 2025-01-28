from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from models import Base


class Client(Base):
    __tablename__ = "client"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    primary_contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=False)
    secondary_contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=True)
    client_creation_datetime = Column(DateTime, default=func.now())

    primary_contact = relationship("Contact", foreign_keys=[primary_contact_id], back_populates="primary_for_clients")
    secondary_contact = relationship("Contact", foreign_keys=[secondary_contact_id],
                                     back_populates="secondary_for_clients")

    projects = relationship("Project", back_populates="client")

    notes = relationship("Note", back_populates="client")

    call_logs = relationship("CallLog", back_populates="client")
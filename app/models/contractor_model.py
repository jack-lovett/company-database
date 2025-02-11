from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Contractor(Base):
    __tablename__ = "contractor"

    contractor_id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=False)

    contact = relationship("Contact", back_populates="contractors")

    projects = relationship("Project", secondary="project_has_contractor", back_populates="contractors")

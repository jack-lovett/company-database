from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, Date, DateTime, func
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    status = Column(Enum('lead', 'job', 'completed', 'no_sale', name='status_enum'), nullable=False)
    description = Column(Text, nullable=True)
    initial_inquiry_date = Column(Date, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    storeys = Column(Integer, nullable=True)
    referral_source = Column(
        Enum('google', 'referral', 'repeat_client', 'jkc', 'smce', 'word_of_mouth', 'website',
             name='referral_source_enum'), nullable=True)
    payment_basis = Column(Enum('lump_sum', 'hourly_rate', name='payment_basis_enum'), nullable=True)
    creation_datetime = Column(DateTime, default=func.now(), nullable=False)

    contractors = relationship("Contractor", secondary="project_has_contractor", back_populates="projects")

    budgets = relationship("Budget", back_populates="project")

    client = relationship("Client", back_populates="projects")

    building_classes = relationship("BuildingClass", secondary="project_is_building_class", back_populates="projects")

    staff = relationship("Staff", secondary="staff_project", back_populates="projects")

    staff_times = relationship("StaffTime", back_populates="project")

    notes = relationship("Note", back_populates="project")

    address = relationship("Address", back_populates="projects")

    call_logs = relationship("CallLog", back_populates="project")

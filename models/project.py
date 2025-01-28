from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, Date, DateTime
from sqlalchemy.orm import relationship

from models import Base


class Project(Base):
    __tablename__ = "project"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'), nullable=False)
    project_status = Column(Enum('lead', 'job', 'completed', 'no_sale', name='project_status_enum'), nullable=False)
    project_description = Column(Text, nullable=True)
    project_initial_inquiry_date = Column(Date, nullable=True)
    project_start_date = Column(Date, nullable=True)
    project_end_date = Column(Date, nullable=True)
    project_storeys = Column(Integer, nullable=True)
    project_referral_source = Column(
        Enum('google', 'referral', 'repeat_client', 'jkc', 'smce', 'word_of_mouth', 'website',
             name='project_referral_source_enum'), nullable=True)
    project_payment_basis = Column(Enum('lump_sum', 'hourly_rate', name='project_payment_basis_enum'), nullable=True)
    project_creation_datetime = Column(DateTime, default='CURRENT_TIMESTAMP', nullable=False)

    contractors = relationship("Contractor", secondary="project_has_contractor", back_populates="projects")

    budgets = relationship("Budget", back_populates="project")

    client = relationship("Client", back_populates="projects")

    building_classes = relationship("BuildingClass", secondary="project_is_building_class", back_populates="projects")

    staff = relationship("Staff", secondary="staff_project", back_populates="projects")

    staff_times = relationship("StaffTime", back_populates="project")

    notes = relationship("Note", back_populates="project")

    address = relationship("Address", back_populates="projects")

    call_logs = relationship("CallLog", back_populates="project")
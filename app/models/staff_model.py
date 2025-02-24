from sqlalchemy import Integer, Column, ForeignKey, Enum, Text, Date
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)
    role = Column(Enum('secretary', 'director', 'building_designer', 'draftsperson', 'junior_draftsperson',
                       name='role_enum'), nullable=False)
    employment_status = Column(
        Enum('full_time', 'part_time', 'casual', 'not_employed', name='employment_status_enum'), nullable=False)
    hire_date = Column(Date, nullable=False)
    notes = Column(Text, nullable=True)

    contact = relationship("Contact", back_populates="staff")

    projects = relationship("Project", secondary="staff_project", back_populates="staff")

    staff_times = relationship("StaffTime", back_populates="staff")

    call_logs = relationship("CallLog", back_populates="staff")

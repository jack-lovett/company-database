"""Staff model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship

from models import Base


class Staff(Base):
    """Staff model class"""

    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.contact_id'), nullable=False)
    staff_role = Column(Enum('secretary', 'director', 'building_designer', 'draftsperson', 'junior_draftsperson'),
                        nullable=False)
    staff_employment_status = Column(Enum('full_time', 'part_time', 'casual', 'not_employed'), nullable=False)
    staff_hire_date = Column(DateTime, nullable=False)
    staff_notes = Column(Text)

    contact = relationship("Contact", backref="staff")

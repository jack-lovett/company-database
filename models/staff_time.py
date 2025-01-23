"""Staff time model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models import Base


class StaffTime(Base):
    """Staff time model class"""

    __tablename__ = 'staff_time'
    staff_time_id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id'))
    staff_time_description = Column(String(45))
    staff_time_hours = Column(Integer, nullable=False)

    staff = relationship("Staff", backref="time_entries")
    project = relationship("Project", backref="staff_times")

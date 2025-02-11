from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class StaffTime(Base):
    __tablename__ = "staff_time"

    staff_time_id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=True)
    staff_time_description = Column(String(255), nullable=True)
    staff_time_hours = Column(Integer, nullable=False)

    staff = relationship("Staff", back_populates="staff_times")
    project = relationship("Project", back_populates="staff_times")

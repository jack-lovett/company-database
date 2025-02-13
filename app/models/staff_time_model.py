from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class StaffTime(Base):
    __tablename__ = "staff_time"

    id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    description = Column(String(255), nullable=True)
    hours = Column(Integer, nullable=False)

    staff = relationship("Staff", back_populates="staff_times")
    project = relationship("Project", back_populates="staff_times")

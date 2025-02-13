"""Staff project model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey

from app.models.base_model import Base


class StaffProject(Base):
    __tablename__ = "staff_project"

    staff_id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)

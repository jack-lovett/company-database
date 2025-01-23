"""Staff project model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class StaffProject(Base):
    """Staff project model class"""

    __tablename__ = 'staff_project'
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)

    staff = relationship("Staff", backref="projects")
    project = relationship("Project", backref="staff_members")

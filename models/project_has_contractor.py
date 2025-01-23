"""Project has contractor model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class ProjectHasContractor(Base):
    """Project has contractor class"""

    __tablename__ = 'project_has_contractor'
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    contractor_id = Column(Integer, ForeignKey('contractor.contractor_id'), primary_key=True)
    contractor_type_id = Column(Integer, ForeignKey('contractor_type.contractor_type_id'), nullable=False)

    project = relationship("Project", backref="contractors")
    contractor = relationship("Contractor", backref="projects")
    contractor_type = relationship("ContractorType", backref="project_contractors")
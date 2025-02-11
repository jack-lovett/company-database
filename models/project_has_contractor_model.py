from sqlalchemy import Column, Integer, ForeignKey

from models.base_model import Base


class ProjectHasContractor(Base):
    __tablename__ = "project_has_contractor"

    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    contractor_id = Column(Integer, ForeignKey('contractor.contractor_id'), primary_key=True)
    contractor_type_id = Column(Integer, ForeignKey('contractor_type.contractor_type_id'), nullable=False)

from sqlalchemy import Column, Integer, ForeignKey

from app.models.base_model import Base


class ProjectHasContractor(Base):
    __tablename__ = "project_has_contractor"

    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    contractor_id = Column(Integer, ForeignKey('contractor.id'), primary_key=True)
    contractor_type_id = Column(Integer, ForeignKey('contractor_type.id'), nullable=False)

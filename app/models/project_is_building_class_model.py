from sqlalchemy import Column, ForeignKey, Integer

from app.models.base_model import Base


class ProjectIsBuildingClass(Base):
    __tablename__ = "project_is_building_class"
    building_class_id = Column(Integer, ForeignKey('building_class.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)

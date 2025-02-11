from sqlalchemy import Column, ForeignKey, Integer

from app.models.base_model import Base


class ProjectIsBuildingClass(Base):
    __tablename__ = "project_is_building_class"
    building_class_building_class_id = Column(Integer, ForeignKey('building_class.building_class_id'), primary_key=True)
    project_project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)

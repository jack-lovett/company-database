"""Project is building class model for SQL database."""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models import Base


class ProjectIsBuildingClass(Base):
    """Project is building class model class"""
    __tablename__ = 'project_is_building_class'
    building_class_building_class_id = Column(Integer, ForeignKey('building_class.building_class_id'), primary_key=True)
    project_project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)


"""Building class model for SQL database."""
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from models import Base


class BuildingClass(Base):
    """Building class model class"""

    __tablename__ = 'building_class'
    building_class_id = Column(Integer, primary_key=True, autoincrement=True)
    building_class_code = Column(String(2), nullable=False)
    building_class_description = Column(String(45))

    building_class = relationship("BuildingClass", backref="project_classes")
    project = relationship("Project", backref="building_classes")

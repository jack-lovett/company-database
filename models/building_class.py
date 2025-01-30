from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from models import Base


class BuildingClass(Base):
    __tablename__ = "building_class"

    building_class_id = Column(Integer, primary_key=True, autoincrement=True)
    building_class_code = Column(String(2), nullable=False)
    building_class_description = Column(String(255), nullable=True)

    projects = relationship("Project", secondary="project_is_building_class", back_populates="building_classes")

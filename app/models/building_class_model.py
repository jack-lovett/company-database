from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class BuildingClass(Base):
    __tablename__ = "building_class"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(2), nullable=False)
    description = Column(String(255), nullable=True)

    projects = relationship("Project", secondary="project_is_building_class", back_populates="building_classes")

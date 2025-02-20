from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from app.models.project_is_building_class_model import ProjectIsBuildingClass


class BuildingClass(SQLModel, table=True):
    __tablename__ = 'buildingclass'

    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=2)
    description: Optional[str] = Field(default=None, max_length=255)

    # Relationship
    projects: List["Project"] = Relationship(
        back_populates="building_classes",
        link_model=ProjectIsBuildingClass
    )


class BuildingClassDisplay(SQLModel):
    id: int
    code: str
    description: str

from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class ProjectIsBuildingClass(SQLModel, table=True):
    building_class_id: Optional[int] = Field(
        default=None,
        foreign_key="buildingclass.id",
        primary_key=True
    )
    project_id: Optional[int] = Field(
        default=None,
        foreign_key="project.id",
        primary_key=True
    )


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

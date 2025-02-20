from sqlmodel import SQLModel, Field


class ProjectIsBuildingClass(SQLModel, table=True):
    __tablename__ = 'project_is_building_class'

    building_class_id: int = Field(
        foreign_key="buildingclass.id",
        primary_key=True
    )
    project_id: int = Field(
        foreign_key="project.id",
        primary_key=True
    )


# For API operations
class ProjectIsBuildingClassCreate(SQLModel):
    building_class_id: int
    project_id: int


class ProjectIsBuildingClassDisplay(ProjectIsBuildingClassCreate):
    pass

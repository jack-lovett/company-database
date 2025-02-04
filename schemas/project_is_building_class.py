from pydantic import BaseModel


class ProjectIsBuildingClassBase(BaseModel):
    building_class_building_class_id: int
    project_project_id: int


class ProjectIsBuildingClassCreate(ProjectIsBuildingClassBase):
    pass


class ProjectIsBuildingClassUpdate(ProjectIsBuildingClassBase):
    # In many-to-many relationship tables, we do not update, instead delete entry and create new one
    pass


class ProjectIsBuildingClass(ProjectIsBuildingClassBase):
    class Config:
        from_attributes = True

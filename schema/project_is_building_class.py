from pydantic import BaseModel


class ProjectIsBuildingClassBase(BaseModel):
    building_class_building_class_id: int
    project_project_id: int


class ProjectIsBuildingClassCreate(ProjectIsBuildingClassBase):
    pass


class ProjectIsBuildingClassUpdate(ProjectIsBuildingClassBase):
    pass


class ProjectIsBuildingClass(ProjectIsBuildingClassBase):
    class Config:
        orm_mode = True

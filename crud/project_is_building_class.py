from crud.base import CRUDBase
from models.project_is_building_class import ProjectIsBuildingClass


class CRUDProject_is_building_class(CRUDBase):
    def __init__(self):
        super().__init__(ProjectIsBuildingClass)

from app.crud.base_crud import CRUDBase
from app.models.project_is_building_class_model import ProjectIsBuildingClass


class CRUDProject_is_building_class(CRUDBase):
    def __init__(self):
        super().__init__(ProjectIsBuildingClass)

from app.crud.project_is_building_class_crud import CRUDProject_is_building_class
from app.services.base_service import BaseService


class ProjectIsBuildingClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject_is_building_class())

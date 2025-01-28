from crud.project_is_building_class import CRUDProject_is_building_class
from services.base import BaseService

class ProjectIsBuildingClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject_is_building_class())
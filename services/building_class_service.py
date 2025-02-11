from crud.building_class_crud import CRUDBuildingClass
from services.base_service import BaseService


class BuildingClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDBuildingClass())

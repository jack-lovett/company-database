from app.crud.building_class_crud import CRUDBuildingClass
from app.services.base_service import BaseService


class BuildingClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDBuildingClass())

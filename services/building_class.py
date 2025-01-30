from crud.building_class import CRUDBuildingClass
from services.base import BaseService


class BuildingClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDBuildingClass())

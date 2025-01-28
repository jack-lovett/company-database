from crud.base import CRUDBase
from models.building_class import BuildingClass

class CRUDBuildingClass(CRUDBase):
    def __init__(self):
        super().__init__(BuildingClass)
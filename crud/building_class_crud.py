from crud.base_crud import CRUDBase
from models.building_class_model import BuildingClass


class CRUDBuildingClass(CRUDBase):
    def __init__(self):
        super().__init__(BuildingClass)

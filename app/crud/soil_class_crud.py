from app.crud.base_crud import CRUDBase
from app.models.soil_class_model import SoilClass


class CRUDSoilClass(CRUDBase):
    def __init__(self):
        super().__init__(SoilClass)

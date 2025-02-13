from app.crud.soil_class_crud import CRUDSoilClass
from app.services.base_service import BaseService


class SoilClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDSoilClass())

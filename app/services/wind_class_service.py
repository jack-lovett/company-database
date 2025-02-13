from app.crud.wind_class_crud import CRUDWindClass
from app.services.base_service import BaseService


class WindClassService(BaseService):
    def __init__(self):
        super().__init__(CRUDWindClass())

from app.crud.base_crud import CRUDBase
from app.models.wind_class_model import WindClass


class CRUDWindClass(CRUDBase):
    def __init__(self):
        super().__init__(WindClass)

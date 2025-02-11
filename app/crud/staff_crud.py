from app.crud.base_crud import CRUDBase
from app.models.staff_model import Staff


class CRUDStaff(CRUDBase):
    def __init__(self):
        super().__init__(Staff)

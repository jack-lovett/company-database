from crud.base_crud import CRUDBase
from models.staff_model import Staff


class CRUDStaff(CRUDBase):
    def __init__(self):
        super().__init__(Staff)

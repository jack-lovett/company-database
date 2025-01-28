from crud.base import CRUDBase
from models.staff import Staff

class CRUDStaff(CRUDBase):
    def __init__(self):
        super().__init__(Staff)
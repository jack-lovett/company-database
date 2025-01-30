from crud.base import CRUDBase
from models.staff_time import StaffTime


class CRUDStaff_time(CRUDBase):
    def __init__(self):
        super().__init__(StaffTime)

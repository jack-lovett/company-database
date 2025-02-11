from app.crud.base_crud import CRUDBase
from app.models.staff_time_model import StaffTime


class CRUDStaff_time(CRUDBase):
    def __init__(self):
        super().__init__(StaffTime)

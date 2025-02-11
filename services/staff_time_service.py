from crud.staff_time_crud import CRUDStaff_time
from services.base_service import BaseService


class StaffTimeService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff_time())

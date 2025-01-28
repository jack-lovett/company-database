from crud.staff_time import CRUDStaff_time
from services.base import BaseService

class StaffTimeService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff_time())
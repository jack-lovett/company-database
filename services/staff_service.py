from crud.staff_crud import CRUDStaff
from services.base_service import BaseService


class StaffService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff())

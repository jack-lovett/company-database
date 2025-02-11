from app.crud.staff_crud import CRUDStaff
from app.services.base_service import BaseService


class StaffService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff())

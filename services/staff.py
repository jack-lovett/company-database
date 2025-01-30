from crud.staff import CRUDStaff
from services.base import BaseService


class StaffService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff())

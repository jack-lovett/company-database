from crud.base import CRUDBase
from models.staff_project import StaffProject


class CRUDStaff_project(CRUDBase):
    def __init__(self):
        super().__init__(StaffProject)

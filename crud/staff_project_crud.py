from crud.base_crud import CRUDBase
from models.staff_project_model import StaffProject


class CRUDStaff_project(CRUDBase):
    def __init__(self):
        super().__init__(StaffProject)

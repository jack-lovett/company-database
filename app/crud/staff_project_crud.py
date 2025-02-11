from app.crud.base_crud import CRUDBase
from app.models.staff_project_model import StaffProject


class CRUDStaff_project(CRUDBase):
    def __init__(self):
        super().__init__(StaffProject)

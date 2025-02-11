from crud.staff_project_crud import CRUDStaff_project
from services.base_service import BaseService


class StaffProjectService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff_project())

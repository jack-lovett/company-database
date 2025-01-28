from crud.staff_project import CRUDStaff_project
from services.base import BaseService

class StaffProjectService(BaseService):
    def __init__(self):
        super().__init__(CRUDStaff_project())
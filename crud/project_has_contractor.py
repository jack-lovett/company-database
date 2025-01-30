from crud.base import CRUDBase
from models.project_has_contractor import ProjectHasContractor


class CRUDProject_has_contractor(CRUDBase):
    def __init__(self):
        super().__init__(ProjectHasContractor)

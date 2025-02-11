from app.crud.base_crud import CRUDBase
from app.models.project_has_contractor_model import ProjectHasContractor


class CRUDProject_has_contractor(CRUDBase):
    def __init__(self):
        super().__init__(ProjectHasContractor)

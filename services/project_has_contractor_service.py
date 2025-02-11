from crud.project_has_contractor_crud import CRUDProject_has_contractor
from services.base_service import BaseService


class ProjectHasContractorService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject_has_contractor())

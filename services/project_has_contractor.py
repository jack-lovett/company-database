from crud.project_has_contractor import CRUDProject_has_contractor
from services.base import BaseService


class ProjectHasContractorService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject_has_contractor())

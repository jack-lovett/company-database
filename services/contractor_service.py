from crud.contractor_crud import CRUDContractor
from services.base_service import BaseService


class ContractorService(BaseService):
    def __init__(self):
        super().__init__(CRUDContractor())

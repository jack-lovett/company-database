from crud.contractor_type_crud import CRUDContractor_type
from services.base_service import BaseService


class ContractorTypeService(BaseService):
    def __init__(self):
        super().__init__(CRUDContractor_type())

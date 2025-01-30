from crud.contractor_type import CRUDContractor_type
from services.base import BaseService


class ContractorTypeService(BaseService):
    def __init__(self):
        super().__init__(CRUDContractor_type())

from crud.contractor import CRUDContractor
from services.base import BaseService


class ContractorService(BaseService):
    def __init__(self):
        super().__init__(CRUDContractor())

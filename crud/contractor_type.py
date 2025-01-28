from crud.base import CRUDBase
from models.contractor_type import ContractorType

class CRUDContractor_type(CRUDBase):
    def __init__(self):
        super().__init__(ContractorType)